from odoo import api, fields, models, _


class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    auto_update_description = fields.Boolean(
        string="Auto update description ?",
        default=True
    )
