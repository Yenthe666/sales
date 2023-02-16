from odoo import api, fields, models, _


class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    start_after_days = fields.Integer(
        string="Start After",
        help="Subscription will be started after configured days."
    )
