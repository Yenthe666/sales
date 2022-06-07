# -*- coding: utf-8 -*-
from odoo import models, fields, _


class ProductCategory(models.Model):
    _inherit = 'product.category'

    product_category_price_update_timestamp = fields.Datetime(
        string='Product price last update'
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
