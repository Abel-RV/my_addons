from odoo import models,fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee' # Heredamos el modelo hr.employee

    multa_ids = fields.One2many(
        'gestion.multa',  # Modelo relacionado
        'empleado_id',    # Campo Many2one en el modelo gestion.multa que referencia a hr.employee
        string="Multas del Empleado"  # Etiqueta para el campo
    )