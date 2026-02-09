from odoo import models, fields

class Vehiculo(models.Model):
    _name = 'vehiculo'
    _description = 'Modelo para representar un vehículo'

    marca = fields.Char(string='Marca', required=True)
    modelo = fields.Char(string='Modelo', required=True)
    kilometros = fields.Float(string='Kilómetros', required=True)


    conductor_id = fields.Many2one('hr.employee', string='Conductor', required=True)