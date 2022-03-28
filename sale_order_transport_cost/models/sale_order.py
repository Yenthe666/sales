from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def write(self, values):
        """
        Add transportation costs to the order if needed
        """
        sale_order = super(SaleOrder, self).write(values)

        # Get the order total limit for transportation costs
        order_limit = self.env['ir.config_parameter'].get_param('sale_order_transport_cost.sale_order_total_for_transport_cost')

        # If there is an order limit configured and the order is a draft, process transport costs
        if order_limit and order_limit.isdigit() and self.state == 'draft':
            # Get the transport product, create it if it doesn't exist
            transport_product = self.env.ref('sale_order_transport_cost.product_transport_cost', raise_if_not_found=False)
            if not transport_product:
                transport_product = self.env['product.product'].sudo().create({
                    'name': 'Transport Cost',
                    'type': 'service',
                    'taxes_id': False,
                    'supplier_taxes_id': False,
                    'sale_ok': True,
                    'purchase_ok': False,
                    'default_code': 'TRANSPORTCOST',
                    'categ_id': self.env.ref('product.product_category_all').id,
                    'list_price': 15,
                })
                self.env['ir.model.data'].create({
                    'name': 'product_transport_cost',
                    'module': 'sale_order_transport_cost',
                    'res_id': transport_product.id,
                    'model': 'product.product',
                    'noupdate': True
                })

            # Check if there already is a transport cost
            transport_line = self.order_line.filtered(lambda line: line.product_id == transport_product)

            # If there is no transport cost and the amount is below the limit, add an order line with the transport cost
            if self.amount_total < int(order_limit) and not transport_line:
                self.env['sale.order.line'].create({
                    'name': 'Transportation costs',
                    'order_id': self.id,
                    'product_id': transport_product.id
                })

            # If there is a transport cost, but the total amount is above the limit, remove the transport cost
            elif transport_line and self.amount_total - transport_line[0].price_subtotal >= int(order_limit) and transport_line:
                transport_line.unlink()

        return sale_order
