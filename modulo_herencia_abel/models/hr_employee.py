from odoo import models,fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee' # Heredamos el modelo hr.employee

    multa_ids = fields.One2many(
        'gestion.multa',
        'empleado_id',
        string="Multas del Empleado"
    )