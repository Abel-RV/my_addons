from odoo import models,fields

class TipoMulta(models.Model):
    _name = 'gestion.tipo_multa'  # Nombre técnico del modelo en la base de datos
    _description = 'Tipos de Multas'  # Descripción del modelo

    name = fields.Char(string="Nombre del Tipo de Multa", required=True)