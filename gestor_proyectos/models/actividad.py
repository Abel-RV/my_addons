from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Actividad(models.Model):
    _name = 'gestor_proyectos.actividad'
    _description = 'gestor_proyectos.actividad'

    nombreActividad = fields.Char(string="Nombre de la Actividad", required=True)
    descripcionActividad = fields.Text(string="Descripción de la Actividad")
    trabajo_id = fields.Many2one('gestor_proyectos.trabajo', string="Trabajo Asociado", required=True)
    personasInvolucradas = fields.Char(string="Personas Involucradas")
    fechaInicioActividad = fields.Date(string="Inicio Planificado")
    fechaFinActividad = fields.Date(string="Fin Planificado")
    estadoActividad = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_curso', 'En Curso'),
        ('en_revision', 'En Revisión'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada')
    ], string="Estado de la Actividad", default='pendiente')
    avanceIndividual = fields.Float(string="Avance Individual", default=0.0)

    @api.constrains('fechaInicioActividad', 'fechaFinActividad', 'trabajo_id')
    def _check_dates_within_trabajo(self):
        for rec in self:
            if rec.trabajo_id:
                t = rec.trabajo_id
                if t.fecha_inicio and rec.fechaInicioActividad and rec.fechaInicioActividad < t.fecha_inicio:
                    raise ValidationError('La fecha de inicio de la actividad no puede ser anterior a la fecha de inicio del trabajo')
                if t.fecha_fin and rec.fechaFinActividad and rec.fechaFinActividad > t.fecha_fin:
                    raise ValidationError('La fecha de fin de la actividad no puede ser posterior a la fecha de fin del trabajo')
                if rec.fechaInicioActividad and rec.fechaFinActividad and rec.fechaInicioActividad > rec.fechaFinActividad:
                    raise ValidationError('La fecha de inicio de la actividad no puede ser posterior a la fecha de fin')

    def _update_parent_progress_and_state(self):
        """Update parent trabajo state (and indirectly proyecto) after activity changes.
        Do not call compute methods directly to avoid recursion; instead compute desired state and write it.
        """
        trabajos_to_check = self.mapped('trabajo_id')
        projects_to_check = trabajos_to_check.mapped('proyecto_id')
        # For each trabajo, compute desired state and update if different
        for trabajo in trabajos_to_check:
            state_map = trabajo._compute_state_from_activities()
            new_state = state_map.get(trabajo.id) if isinstance(state_map, dict) else False
            if new_state and new_state != trabajo.estado:
                try:
                    trabajo.write({'estado': new_state})
                except Exception:
                    # swallow errors to avoid breaking activity save; admins can check logs
                    pass
        # Update projects' states based on trabajos
        for proyecto in projects_to_check:
            try:
                proyecto._update_state_from_trabajos()
            except Exception:
                pass

    def create(self, vals):
        rec = super(Actividad, self).create(vals)
        # Update parents (trabajo.estado and proyecto.estado) safely
        rec._update_parent_progress_and_state()
        return rec

    def write(self, vals):
        res = super(Actividad, self).write(vals)
        # update parents for all records in self
        self._update_parent_progress_and_state()
        return res

    def unlink(self):
        parents = self.mapped('trabajo_id.proyecto_id')
        trabajos = self.mapped('trabajo_id')
        res = super(Actividad, self).unlink()
        # After deletion, update affected trabajos and proyectos
        for trabajo in trabajos:
            try:
                state_map = trabajo._compute_state_from_activities()
                new_state = state_map.get(trabajo.id) if isinstance(state_map, dict) else False
                if new_state and new_state != trabajo.estado:
                    trabajo.write({'estado': new_state})
            except Exception:
                pass
        for proyecto in parents:
            try:
                proyecto._update_state_from_trabajos()
            except Exception:
                pass
        return res
