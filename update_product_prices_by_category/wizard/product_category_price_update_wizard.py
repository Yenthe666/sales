# -*- coding: utf-8 -*-
import datetime

from odoo import _, api, fields, models


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

    purchase_price_difference = fields.Float(
        string='Purchase price',
        help=_('You can fill in a percentage or a fixed price to increase the purchase prices.')
    )

    sale_price_difference = fields.Float(
        string='Sale price',
        help=_('You can fill in a percentage or a fixed price to increase the sales prices.')
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

    product_prices_last_updated = fields.Datetime(
        related='product_category_id.product_prices_last_updated',
        string='Product prices last updated'
    )

    @api.onchange('product_category_id')
    def _compute_prices_recently_updated(self):
        """
            Checks when the last price update was and if it is within the period set in the config param.
            If so we show a visual warning in the wizard to warn the user.
        """
        config_param_days = self.env['ir.config_parameter'].sudo().get_param('update_product_prices_by_category.product_price_update_days_for_warning')
        self.prices_recently_updated = False
        for record in self:
            if config_param_days \
                    and record.product_category_id.product_prices_last_updated \
                    and datetime.datetime.now() < record.product_category_id.product_prices_last_updated + datetime.timedelta(days=int(config_param_days)):
                record.prices_recently_updated = True

    def action_update_prices(self):
        if not self.purchase_price_difference and not self.sale_price_difference:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('No sale or purchase price change'),
                    'message': _('You must define at least one price change!'),
                    'sticky': False,
                    'type': 'warning',
                }
            }
        categories = self.product_category_id
        # If the category has underlying categories and the option was selected in the wizard
        # we will add all subcategories to update their prices too.
        if self.include_sub_categories:
            child_categories = self.product_category_id.child_id
            while child_categories:
                categories += child_categories
                child_categories = child_categories.child_id

        # Find all the products of the current category / categories
        products = self.env['product.product'].search([
            ('categ_id', 'in', categories.ids)
        ])

        # Update the details per product
        for product in products:
            details = self._get_price_details(product)
            body = 'Price update for category %s:<br/><br/>' % self.product_category_id.name
            if details.get('lst_price'):
                body += 'Sale price: %s -> %s<br/>' % (
                    f'{product.currency_id.symbol} {round(product.lst_price, 2)}',
                    f"{product.currency_id.symbol} {round(details.get('lst_price'), 2)}"
                )
            if details.get('standard_price'):
                body += 'Cost price: %s -> %s<br/>' % (
                    f'{product.currency_id.symbol} {round(product.standard_price, 2)}',
                    f"{product.currency_id.symbol} {round(details.get('standard_price'), 2)}"
                )
            product.message_post(message_type='comment', body=body)
            # Only one variant, let's post the message on the template too.
            if len(product.product_tmpl_id.product_variant_ids) == 1:
                product.product_tmpl_id.message_post(message_type='comment', body=body)
            product.update(details)

        categories.update({
            'product_prices_last_updated': datetime.datetime.now()
        })
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Product prices updated'),
                'message': _('The prices of %s products have been updated successfully.') % str(len(products)),
                'sticky': False,
                'type': 'success',
                'next': {
                    'name': _('Products with updated price'),
                    'view_mode': 'kanban,list,form',
                    'views': [(self.env.ref('product.product_kanban_view').id, 'kanban'), (self.env.ref('product.product_product_tree_view').id, 'list'), (self.env.ref('product.product_normal_form_view').id, 'form')],
                    'res_model': 'product.product',
                    'type': 'ir.actions.act_window',
                    'target': 'current',
                    'domain': [('id', 'in', products.ids)]
                }
            }
        }

    def _get_price_details(self, product):
        """
            Computes the new cost & sales prices for the current product
            Args:
                product (record): product.product record
            Returns:
                details (dictionary): dictionary with the sales price (lst_price) and cost price (standard_price)
        """
        details = {}
        if self.purchase_price_difference:
            extra_price = self.purchase_price_difference if self.increase_price_by == 'fixed' else \
                self.purchase_price_difference / 100 * product.standard_price
            details['standard_price'] = product.standard_price + extra_price
        if self.sale_price_difference:
            extra_price = self.sale_price_difference if self.increase_price_by == 'fixed' else \
                self.sale_price_difference / 100 * product.lst_price
            details['lst_price'] = product.lst_price + extra_price
        return details
