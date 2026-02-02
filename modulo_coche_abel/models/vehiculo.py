from odoo import models, fields, api


class Vehiculo(models.Model):
    _name = 'gestion.vehiculo'
    _description = 'Modelo de Vehículo'

    name = fields.Char(string="Matricula", required=True)
    marca = fields.Char(string="Marca", required=True)
    modelo = fields.Char(string="Modelo", required=True)
    kilometros = fields.Float(string="Kilómetros", required=True)

    conductor_id= fields.Many2one(
        'hr.employee',
        string="Conductor",
        required=True
    )

