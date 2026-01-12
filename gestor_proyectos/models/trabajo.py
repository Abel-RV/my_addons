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

    @api.model_create_multi
    def create(self, vals_list):
        # validate dates within project for each provided vals dict
        for vals in vals_list:
            if vals.get('proyecto_id') and (vals.get('fecha_inicio') or vals.get('fecha_fin')):
                proyecto = self.env['gestor_proyectos.proyecto'].browse(vals['proyecto_id'])
                # convert possible string dates to date objects for comparison
                if proyecto.fecha_inicio and vals.get('fecha_inicio'):
                    if fields.Date.to_date(vals['fecha_inicio']) < fields.Date.to_date(proyecto.fecha_inicio):
                        raise ValidationError('La fecha de inicio del trabajo no puede ser anterior a la del proyecto')
                if proyecto.fecha_fin and vals.get('fecha_fin'):
                    if fields.Date.to_date(vals['fecha_fin']) > fields.Date.to_date(proyecto.fecha_fin):
                        raise ValidationError('La fecha de fin del trabajo no puede ser posterior a la del proyecto')
        recs = super(Trabajo, self).create(vals_list)
        # Trigger parent updates by calling write with empty vals (will run trabajo.write logic)
        try:
            recs.write({})
        except Exception:
            # If something goes wrong, still return created records and let higher-level handlers surface errors
            pass
        return recs

    def write(self, vals):
        # validate dates within project if project and dates provided or changed
        for rec in self:
            proyecto = rec.proyecto_id
            fecha_inicio = vals.get('fecha_inicio', rec.fecha_inicio)
            fecha_fin = vals.get('fecha_fin', rec.fecha_fin)
            # convert to date objects for safe comparison
            if proyecto and proyecto.fecha_inicio and fecha_inicio:
                if fields.Date.to_date(fecha_inicio) < fields.Date.to_date(proyecto.fecha_inicio):
                    raise ValidationError('La fecha de inicio del trabajo no puede ser anterior a la del proyecto')
            if proyecto and proyecto.fecha_fin and fecha_fin:
                if fields.Date.to_date(fecha_fin) > fields.Date.to_date(proyecto.fecha_fin):
                    raise ValidationError('La fecha de fin del trabajo no puede ser posterior a la del proyecto')
        res = super(Trabajo, self).write(vals)
        # After write, ensure parent project state is updated (do not update trabajo state here to avoid recursion)
        projects = self.mapped('proyecto_id')
        for proyecto in projects:
            try:
                proyecto._update_state_from_trabajos()
            except Exception:
                pass
        return res

    def _compute_state_from_activities(self):
        """Compute the desired state for the trabajo based on its activities without writing.
        Returns a string state or False if no change."""
        results = {}
        for rec in self:
            if not rec.actividad_ids:
                results[rec.id] = False
                continue
            estados = set(rec.actividad_ids.mapped('estadoActividad'))
            new_state = None
            if estados == {'finalizada'}:
                new_state = 'finalizado'
            elif 'en_curso' in estados:
                new_state = 'en_progreso'
            elif 'en_revision' in estados:
                new_state = 'en_revision'
            elif 'pendiente' in estados and len(estados) == 1:
                new_state = 'pendiente'
            else:
                if 'en_curso' in estados:
                    new_state = 'en_progreso'
                elif 'en_revision' in estados:
                    new_state = 'en_revision'
                else:
                    new_state = 'pendiente'
            results[rec.id] = new_state
        # return mapping if multiple; for single record caller can index
        return results

    def unlink(self):
        # collect affected projects before deletion
        projects = self.mapped('proyecto_id')
        res = super(Trabajo, self).unlink()
        for proyecto in projects:
            try:
                proyecto._update_state_from_trabajos()
            except Exception:
                pass
        return res