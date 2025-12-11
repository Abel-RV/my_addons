    from odoo import models, fields, api


    class estado_proyectos(models.Model):
        _name = 'gestor_proyectos.gestors'
        _description = 'gestor_proyectos.gestor_proyectos'

        name = fields.Char()
        value = fields.Integer()
        value2 = fields.Float(compute="_value_pc", store=True)
        description = fields.Text()

#   @api.depends('value')
#    def _value_pc(self):
#        for record in self:
#            record.value2 = float(record.value) / 100

