from odoo import api, fields, models, _


class SaleOrderTemplateLine(models.Model):
    _inherit = "sale.order.template.line"

    auto_update_description = fields.Boolean(
        string="Auto update description ?",
        default=True
    )
