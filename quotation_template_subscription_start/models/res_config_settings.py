# -- coding: utf-8 --
from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    start_after_days = fields.Integer(
        string="Default delay in Subscription",
        help="Amount of days after which the subscription should start once the order has been signed/confirmed.",
        config_parameter='quotation_template_subscription_start.default_start_after_days',
    )
