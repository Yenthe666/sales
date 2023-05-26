# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SaleOrderProductPriceUpdate(models.TransientModel):
    _name = 'sale.order.product.price.update'
    _description = 'Update prices from order lines'

    sale_order_line_id = fields.Many2one(
        comodel_name='sale.order.line',
        string='Sale order line'
    )

    product_id = fields.Many2one(
        comodel_name='product.product',
        related='sale_order_line_id.product_id',
        string='Product'
    )

    old_price = fields.Float(
        string='Old price',
        related='sale_order_line_id.price_unit'
    )

    new_price = fields.Float(
        string='New public price'
    )

    new_price_pricelist = fields.Float(
        string='New price customer'
    )

    sale_order_product_price_update_wizard_id = fields.Many2one(
        comodel_name='sale.order.product.price.update.wizard',
        string='Sale order product price update wizard'
    )
