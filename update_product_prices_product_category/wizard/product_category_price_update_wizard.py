# -*- coding: utf-8 -*-
import datetime

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import base64
import xlrd


class ProductCategoryPriceUpdateWizard(models.TransientModel):
    _name = "product.category.price.update.wizard"
    _description = "Product category price update wizard"

    increase_price_by = fields.Selection(
        string='Increase price by',
        selection=[
            ('percentage', _('Percentage')),
            ('fixed', _('Fixed price'))
        ],
        default='percentage',
        required=True
    )

    purchase_price = fields.Float(
        string='Purchase price'
    )

    sale_price = fields.Float(
        string='Sale price'
    )

    product_category_id = fields.Many2one(
        comodel_name='product.category',
        string='Product category'
    )

    product_category_child_ids = fields.One2many(
        related='product_category_id.child_id'
    )

    include_sub_categories = fields.Boolean(
        string='Update underlying categories '
    )

    prices_recently_updated = fields.Boolean(
        string='Prices recently updated',
        compute='_compute_prices_recently_updated'
    )

    @api.onchange('product_category_id')
    def _compute_prices_recently_updated(self):
        config_param_days = self.env['ir.config_parameter'].sudo().get_param('update_product_prices_product_category.product_price_update_days_for_warning')
        for record in self:
            if config_param_days \
                    and record.product_category_id.product_category_price_update_timestamp \
                    and datetime.datetime.now() < record.product_category_id.product_category_price_update_timestamp + datetime.timedelta(days=int(config_param_days)):
                record.prices_recently_updated = True
            else:
                record.prices_recently_updated = False

    def action_update_prices(self):
        categories = self.product_category_id
        if self.include_sub_categories:
            child_categories = self.product_category_id.child_id
            while child_categories:
                categories += child_categories
                child_categories = child_categories.child_id

        products = self.env['product.product'].search([
            ('categ_id', 'in', categories.ids)
        ])
        for product in products:
            details = self._get_price_details(product)
            body = 'Price update for category %s:<br/><br/>' % self.product_category_id.name
            if details.get('standard_price'):
                body += 'Sale price: %s -> %s<br/>' % (product.standard_price, details.get('standard_price'))
            if details.get('lst_price'):
                body += 'Cost price: %s -> %s<br/>' % (product.lst_price, details.get('lst_price'))
            product.message_post(message_type='comment', body=body)
            product.update(details)

        categories.update({
            'product_category_price_update_timestamp': datetime.datetime.now()
        })

    def _get_price_details(self, product):
        details = {}
        if self.purchase_price:
            extra_price = self.purchase_price if self.increase_price_by == 'fixed' else self.purchase_price / 100 * product.standard_price
            details['standard_price'] = product.standard_price + extra_price
        if self.sale_price:
            extra_price = self.sale_price if self.increase_price_by == 'fixed' else self.sale_price / 100 * product.lst_price
            details['lst_price'] = product.lst_price + extra_price
        return details
