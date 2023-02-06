from odoo import fields, models


class SaleOrderTemplateType(models.Model):
    _name = "sale.order.template.type"
    _description = "Quotation templates type"

    name = fields.Char(
        string='Name',
        translate=True,
        required=True
    )
