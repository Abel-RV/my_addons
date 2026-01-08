from odoo import models, fields, api

class actividad(models.Model):
    _name = 'gestor_proyectos.actividad'
    _description = 'gestor_proyectos.actividad'

    nombreActividad = fields.Char(string="Nombre de la Actividad", required=True)
    descripcionActividad = fields.Text(string="Descripción de la Actividad")
    trabajo_id = fields.Many2one('gestor_proyectos.trabajo', string="Trabajo Asociado", required=True)
    personasInvolucradas = fields.Char(string="Personas Involucradas")
    inicioPlanificado = fields.Date(string="Inicio Planificado")
    finPlanificado = fields.Date(string="Fin Planificado")
    estadoActividad = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_curso', 'En Curso'),
        ('en_revision', 'En Revisión'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada')
    ], string="Estado de la Actividad", default='pendiente')
    avanceIndividual = fields.Float(string="Avance Individual", default=0.0)
    