from odoo import models, fields, api

class editorial(models.Model):
    _name = "libreria_b.editorial"
    _description = "Descripción del modulo libreria_b.editorial"

    name =fields.Char(string="Nombre de la Editorial",required=True)
    libros_ids=fields.One2many('libreria_b.libro','editorial_id',string='Libros publicados')