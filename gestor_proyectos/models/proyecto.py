from odoo import models, fields, api

class proyecto(models.Model):
    _name = 'gestor_proyectos.proyecto'
    _description = 'gestor_proyectos.proyecto'

    nombre = fields.Char(string="Nombre del Proyecto", required=True)
    descripcion = fields.Text(string="Descripción del Proyecto")
    fecha_inicio = fields.Date(string="Fecha de Inicio")
    fecha_fin = fields.Date(string="Fecha de Fin")
    estado_id = fields.Many2one('gestor_proyectos.estados_proyecto', string="Estado del Proyecto")
    responsable = fields.Char(string="Responsable del Proyecto")
    porcentaje_avance = fields.Float(string="Porcentaje de Avance", default=0.0)
    #trabajo_ids = fields.One2many('gestor_proyectos.trabajo', 'proyecto_id', string="Trabajos Asociados")
    avance_individual = fields.Float(string="Avance Individual", compute='_compute_avance_individual', store=True)
