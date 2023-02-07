from odoo import api, fields, models, _


class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    customer_ids = fields.Many2many(
        "res.partner",
        string="Customers",
    )
