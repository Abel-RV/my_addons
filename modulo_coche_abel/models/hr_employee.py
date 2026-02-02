from odoo import models,fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee' # Heredamos el modelo hr.employee

    multa_ids = fields.One2many(
        'gestion.multa',
        'empleado_id',
        string="Multas del Empleado"
    )

    vehiculo_id= fields.One2many(
        'gestion.vehiculo',
        'conductor_id',
        string="Vehículos asignados"
    )