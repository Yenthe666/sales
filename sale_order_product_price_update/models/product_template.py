# -*- coding: utf-8 -*-
import datetime

from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    list_price_last_updated = fields.Datetime(
        string='Sale price last updated'
    )

    @api.constrains('list_price')
    def _contrains_list_price(self):
        now = datetime.datetime.now()
        for record in self:
            record.list_price_last_updated = now
