from odoo import models, fields, api

class trabajo(models.Model):
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
    promedio_avance = fields.Float(string="Promedio de Avance", default=0.0)
    actividad_ids = fields.One2many('gestor_proyectos.actividad', 'trabajo_id', string="Actividades Asociadas")
    importancia = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta')
    ], string="Importancia del Trabajo", default='media')
    avance_individual = fields.Float(string="Avance Individual", default=0.0)