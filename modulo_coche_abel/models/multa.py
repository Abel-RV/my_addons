from odoo import models, fields, api

class Multa(models.Model):
    _name = 'gestion.multa' # Nombre técnico del modelo en la base de datos
    _description = 'Multas de Empleados' # Descripción del modelo

    # Campo para la fecha en que se impone la multa
    fecha = fields.Date(string="Fecha de la multa", required=True)
    # Campo de texto para describir la razón de la multa
    descripcion = fields.Text(string="Descripción", required=True)
    # Relación Many2one con el modelo 'gestion.tipo_multa' (tipo de sanción)
    tipo_multa_id = fields.Many2one('gestion.tipo_multa', string="Tipo de sanción", required=True)
    # Relación Many2one con el modelo 'hr.employee' (empleado que recibe la multa)
    empleado_id = fields.Many2one('hr.employee', string="Empleado involucrado", required=True)
    # Campo para almacenar el importe monetario de la multa
    importe = fields.Float(string="Importe de la multa")
    # Campo booleano para indicar si la empresa ha pagado la multa
    pagada = fields.Boolean(string="Pagada por la empresa", default=False)
    # Campo calculado basado en el nombre del empleado
    nombre_empleado = fields.Char(string="Nombre Empleado", related='empleado_id.name', store=False)