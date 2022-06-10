import datetime

from odoo import fields, models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.constrains('lst_price')
    def _contrains_list_price(self):
        now = datetime.datetime.now()
        for record in self:
            record.list_price_last_updated = now
