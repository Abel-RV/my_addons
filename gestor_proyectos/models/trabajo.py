from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Trabajo(models.Model):
    _name = 'gestor_proyectos.trabajo'
    _description = 'gestor_proyectos.trabajo'

    descripcion = fields.Text(string="Descripción del Trabajo")
    proyecto_id = fields.Many2one('gestor_proyectos.proyecto', string="Proyecto Asociado", required=True)
    responsable = fields.Char(string="Responsable del Trabajo")
    fecha_inicio = fields.Date(string="Fecha de Inicio")
    fecha_fin = fields.Date(string="Fecha de Fin")
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('en_revision', 'En Revisión'),
        ('finalizado', 'Finalizado')
    ], string="Estado del Trabajo", default='pendiente')
    promedio_avance = fields.Float(string="Promedio de Avance", compute='_compute_promedio_avance', store=True)
    actividad_ids = fields.One2many('gestor_proyectos.actividad', 'trabajo_id', string="Actividades Asociadas")
    importancia = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente')
    ], string="Importancia del Trabajo", default='media')
    avance_individual = fields.Float(string="Avance Individual", default=0.0)

    @api.depends('actividad_ids.avanceIndividual', 'actividad_ids.estadoActividad')
    def _compute_promedio_avance(self):
        for rec in self:
            if rec.actividad_ids:
                total = sum(a.avanceIndividual for a in rec.actividad_ids)
                rec.promedio_avance = total / len(rec.actividad_ids) if rec.actividad_ids else 0.0
            else:
                rec.promedio_avance = 0.0

    @api.model
    def create(self, vals):
        # validate dates within project if provided
        if vals.get('proyecto_id') and (vals.get('fecha_inicio') or vals.get('fecha_fin')):
            proyecto = self.env['gestor_proyectos.proyecto'].browse(vals['proyecto_id'])
            if proyecto.fecha_inicio and vals.get('fecha_inicio') and vals['fecha_inicio'] < proyecto.fecha_inicio:
                raise ValidationError('La fecha de inicio del trabajo no puede ser anterior a la del proyecto')
            if proyecto.fecha_fin and vals.get('fecha_fin') and vals['fecha_fin'] > proyecto.fecha_fin:
                raise ValidationError('La fecha de fin del trabajo no puede ser posterior a la del proyecto')
        return super(Trabajo, self).create(vals)

    def write(self, vals):
        # validate dates within project if project and dates provided or changed
        for rec in self:
            proyecto = rec.proyecto_id
            fecha_inicio = vals.get('fecha_inicio', rec.fecha_inicio)
            fecha_fin = vals.get('fecha_fin', rec.fecha_fin)
            if proyecto and proyecto.fecha_inicio and fecha_inicio and fecha_inicio < proyecto.fecha_inicio:
                raise ValidationError('La fecha de inicio del trabajo no puede ser anterior a la del proyecto')
            if proyecto and proyecto.fecha_fin and fecha_fin and fecha_fin > proyecto.fecha_fin:
                raise ValidationError('La fecha de fin del trabajo no puede ser posterior a la del proyecto')
        res = super(Trabajo, self).write(vals)
        # after write, update state based on activities
        for rec in self:
            rec._update_state_from_activities()
        return res

    def _update_state_from_activities(self):
        for rec in self:
            if not rec.actividad_ids:
                # leave state as set by user if no activities
                continue
            estados = set(rec.actividad_ids.mapped('estadoActividad'))
            if estados == {'finalizada'}:
                rec.estado = 'finalizado'
            elif 'en_curso' in estados:
                rec.estado = 'en_progreso'
            elif 'en_revision' in estados:
                rec.estado = 'en_revision'
            elif 'pendiente' in estados and len(estados) == 1:
                rec.estado = 'pendiente'
            else:
                # mixed states: prioritize in_progress -> revision -> pendiente
                if 'en_curso' in estados:
                    rec.estado = 'en_progreso'
                elif 'en_revision' in estados:
                    rec.estado = 'en_revision'
                else:
                    rec.estado = 'pendiente'
        return True