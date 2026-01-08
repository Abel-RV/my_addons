from odoo import models, fields, api

class proyecto(models.Model):
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
    porcentaje_avance = fields.Float(string="Porcentaje de Avance", default=0.0)
    trabajo_ids = fields.One2many('gestor_proyectos.trabajo', 'proyecto_id', string="Trabajos Asociados")
    avance_individual = fields.Float(string="Avance Individual", default=0.0)
