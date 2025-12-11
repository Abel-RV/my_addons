from odoo import models, fields, api

class proyecto(models.Model):
    _name = 'gestor_proyectos.proyecto'
    _description = 'gestor_proyectos.proyecto'

    nombreProyecto = fields.Char(string ="Nombre del Proyecto",required=True)
    descripcionProyecto = fields.Text(string="Descripción del Proyecto")
    fechaInicio = fields.Date(string="Fecha de Inicio")
    fechaFin = fields.Date(string="Fecha de Fin")
    prioridad = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta')
    ], string="Prioridad", default='media')
    responsable = fields.Char(string="Responsable")
    progreso = fields.Integer(string="Progreso (%)", default=0) 