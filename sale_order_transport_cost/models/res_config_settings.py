# -- coding: utf-8 --
from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_order_total_for_transport_cost = fields.Integer(
        string='Sale order total for transport cost',
        help='Orders with a total below this value will have transportation costs.',
        config_parameter='sale_order_transport_cost.sale_order_total_for_transport_cost'
    )
