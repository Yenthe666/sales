from odoo import api, fields, models, _


class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    template_type_id = fields.Many2one(
        "sale.order.template.type",
        string="Template Type",
    )
