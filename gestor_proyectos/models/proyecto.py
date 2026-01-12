from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Proyecto(models.Model):
    _name = 'gestor_proyectos.proyecto'
    _description = 'gestor_proyectos.proyecto'

    name = fields.Char(string="Nombre del Proyecto", required=True)
    descripcion = fields.Text(string="Descripción del Proyecto")
    fecha_inicio = fields.Date(string="Fecha de Inicio")
    fecha_fin = fields.Date(string="Fecha de Fin")
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('en_planificacion', 'En Planificación'),
        ('en_ejecucion', 'En Ejecución'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado')
    ], string="Estado del Proyecto", default='en_planificacion')
    responsable = fields.Many2one('res.users', string="Responsable del Proyecto")
    porcentaje_avance = fields.Float(string="Porcentaje de Avance", compute='_compute_porcentaje_avance', store=True)
    trabajo_ids = fields.One2many('gestor_proyectos.trabajo', 'proyecto_id', string="Trabajos Asociados")
    avance_individual = fields.Float(string="Avance Individual", default=0.0)

    @api.depends('trabajo_ids.promedio_avance', 'trabajo_ids.estado')
    def _compute_porcentaje_avance(self):
        for rec in self:
            trabajos = rec.trabajo_ids
            if trabajos:
                total = sum(t.promedio_avance for t in trabajos)
                rec.porcentaje_avance = total / len(trabajos) if trabajos else 0.0
            else:
                rec.porcentaje_avance = 0.0

    def _update_state_from_trabajos(self):
        for rec in self:
            trabajos = rec.trabajo_ids
            if not trabajos:
                continue
            estados = set(trabajos.mapped('estado'))
            if estados == {'finalizado'}:
                rec.estado = 'finalizado'
            elif 'en_ejecucion' in estados or 'en_progreso' in estados:
                rec.estado = 'en_ejecucion'
            elif 'en_planificacion' in estados and len(estados) == 1:
                rec.estado = 'en_planificacion'
            else:
                # mixed: if any not finalized and any in execution -> ejecucion
                if any(e in estados for e in ['en_ejecucion', 'en_progreso', 'en_revision']):
                    rec.estado = 'en_ejecucion'

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_dates(self):
        for rec in self:
            if rec.fecha_inicio and rec.fecha_fin and rec.fecha_inicio > rec.fecha_fin:
                raise ValidationError('La fecha de inicio no puede ser posterior a la fecha de fin del proyecto')

    def unlink(self):
        for rec in self:
            if rec.trabajo_ids and rec.estado != 'borrador':
                raise ValidationError('No se puede eliminar un proyecto con trabajos asociados salvo que esté en estado Borrador')
        return super(Proyecto, self).unlink()

    def write(self, vals):
        # validate date ranges for trabajos
        if 'fecha_inicio' in vals or 'fecha_fin' in vals:
            for rec in self:
                fstart = vals.get('fecha_inicio', rec.fecha_inicio)
                fend = vals.get('fecha_fin', rec.fecha_fin)
                if fstart and fend and fstart > fend:
                    raise ValidationError('La fecha de inicio no puede ser posterior a la fecha de fin del proyecto')
                # ensure trabajos dates inside new project range
                for t in rec.trabajo_ids:
                    if fstart and t.fecha_inicio and t.fecha_inicio < fstart:
                        raise ValidationError('Al actualizar el proyecto, hay trabajos cuya fecha de inicio queda fuera del rango')
                    if fend and t.fecha_fin and t.fecha_fin > fend:
                        raise ValidationError('Al actualizar el proyecto, hay trabajos cuya fecha de fin queda fuera del rango')
        res = super(Proyecto, self).write(vals)
        # Do not call compute methods manually here — computed fields and depends will update automatically.
        return res
