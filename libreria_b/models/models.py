from odoo import models, fields, api


class libro(models.Model):
     _name = "libreria_b.libro"
     _description = "Descripción del modulo libreria_b.libro"

     # Campo tipo string (obligatorio)
     nombreLibro = fields.Char(
     string="Título del Libro", required=True, help="Título del libro")
     
     # Campo tipo texto largo
     descripcion = fields.Text(string="Descripción del Libro")
     # Campo tipo entero
     numPaginas = fields.Integer(string="Número de Páginas", required=True)
     # Campo tipo float
     precio = fields.Float(
     string="Precio", digits=(10, 2), help="Precio del libro en euros"
     )
     # Campo tipo booleano
     disponible = fields.Boolean(string="¿Disponible?", default=True)
     # Campo tipo fecha
     fechaPublicacion = fields.Date(string="Fecha de Publicación")
     # Campo tipo fecha y hora
     fechaRegistro = fields.Datetime(
     string="Fecha y hora de registro", default=fields.Datetime.now)
     portada = fields.Image(max_width=100,max_height=100)

     #autor=fields.Text(string="Nombre del autor")
     #edad=fields.Integer(string="Edad",required=True)

     autores_ids=fields.Many2many('libreria_b.autor',string='Autores')
     editorial_id=fields.Many2one('libreria_b.editorial',string='Editorial',help='Editorial del libro')


#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
