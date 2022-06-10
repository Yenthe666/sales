# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SaleOrderProductPriceUpdateWizard(models.TransientModel):
    _name = 'sale.order.product.price.update.wizard'
    _description = 'Wizard to update product prices on a sale order'

    sale_order_product_price_update_ids = fields.One2many(
        comodel_name='sale.order.product.price.update',
        inverse_name='sale_order_product_price_update_wizard_id',
        string='Sale order product price updates'
    )

    def save(self):
        """
            Updates the sale price of products on a quotation/order if there are any price changes
        """
        for price_update in self.sale_order_product_price_update_ids:
            if price_update.new_price != price_update.old_price:
                price_update.sale_order_line_id.price_unit = price_update.new_price
        self.cancel()

    def cancel(self):
        """
            Cancel button on the product price update wizard
            Deletes all lines from the wizard
        """
        self.sale_order_product_price_update_ids.unlink()
