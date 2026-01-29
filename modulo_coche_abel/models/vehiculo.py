#from odoo import models, fields, api


# class modulo_coche_abel(models.Model):
#     _name = 'modulo_coche_abel.modulo_coche_abel'
#     _description = 'modulo_coche_abel.modulo_coche_abel'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

