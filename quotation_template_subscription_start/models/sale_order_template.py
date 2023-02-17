from odoo import api, fields, models, _


class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    start_after_days = fields.Integer(
        string="Start After",
        help="Amount of days after which the subscription should start once the order has been signed/confirmed."
    )
