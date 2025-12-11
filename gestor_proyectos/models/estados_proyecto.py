from odoo import models, fields, api

class estados_proyecto(models.Model):
    _name = 'gestor_proyectos.estados_proyecto'
    _description = 'gestor_proyectos.estados_proyecto'

    nombreEstado = fields.Char(string="Nombre del Estado", required=True)
    descripcionEstado = fields.Text(string="Descripción del Estado")
    proyecto_ids = fields.One2many('gestor_proyectos.proyecto', 'estado_id', string="Proyectos Asociados")

#   @api.depends('value')
#    def _value_pc(self):
#        for record in self:
#            record.value2 = float(record.value) / 100

