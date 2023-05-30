# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ProductCategory(models.Model):
    _inherit = 'product.category'

    product_prices_last_updated = fields.Datetime(
        string='Product prices last updated',
        copy=False
    )

    def action_open_product_price_update_wizard(self):
        return {
            'name': _('Update prices'),
            'view_mode': 'form',
            'res_model': 'product.category.price.update.wizard',
            'type': 'ir.actions.act_window',
            'context': "{'default_product_category_id': %s}" % self.id,
            'target': 'new'
        }
