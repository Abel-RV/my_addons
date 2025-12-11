from odoo import models, fields

class autor(models.Model):
    _name ='libreria_b.autor'
    _descripcion ='Descripción del modulo del autor'

    #Define que el campo "nombre" será el que se muestre en vistas Many2One/Many2Many

    _rec_name ='nombre'

    nombre = fields.Char(string="Autor",required=True)
    libros_ids=fields.Many2many('libreria_b.libro',string='Libros')