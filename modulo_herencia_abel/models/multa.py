# from odoo import models, fields, api


# class modulo_herencia_abel(models.Model):
#     _name = 'modulo_herencia_abel.modulo_herencia_abel'
#     _description = 'modulo_herencia_abel.modulo_herencia_abel'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

