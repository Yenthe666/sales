# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_sale_order_product_price_update_wizard(self):
        """
            Checks if there are any products with new prices on the product compared to on the quotation/order.
            If there are products with new price we show a wizard in which the user can update prices of lines.
        """
        price_updates = []
        for order_line in self.order_line:
            if order_line.product_id:
                product_lst_price_with_pricelist = order_line.order_id.pricelist_id.get_product_price(order_line.product_id, 1, order_line.order_id.partner_id)
                if order_line.product_id.list_price_last_updated \
                        and order_line.product_id.list_price_last_updated > self.create_date\
                        and product_lst_price_with_pricelist != order_line.price_unit:
                    price_updates.append({
                        'sale_order_line_id': order_line.id,
                        'new_price': order_line.product_id.lst_price,
                        'new_price_pricelist': product_lst_price_with_pricelist,
                    })
        price_update_ids = self.env['sale.order.product.price.update'].create(price_updates)
        # If there are new prices, we return the wizard containing the new prices
        if price_update_ids:
            return {
                'type': 'ir.actions.act_window',
                'name': _('Update order line prices'),
                'res_model': 'sale.order.product.price.update.wizard',
                'view_mode': 'form',
                'view_id': 'view_sale_order_product_price_update',
                'views': [(False, 'form')],
                'target': 'new',
                'context': {"default_sale_order_product_price_update_ids": price_update_ids.ids},
            }
        # If there aren't any new prices, we display a notification that there are no new prices
        else:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _("No price updates"),
                    'message': _("All product prices are already up to date"),
                    'sticky': False,
                    'type': 'info'
                }
            }
