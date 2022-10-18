from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_transport_product(self):
        return {
            'name': _('Transport Cost'),
            'type': 'service',
            'taxes_id': False,
            'supplier_taxes_id': False,
            'sale_ok': True,
            'purchase_ok': False,
            'default_code': 'TRANSPORTCOST',
            'categ_id': self.env.ref('product.product_category_all').id,
            'list_price': 15,
            }

    def _prepare_transport_line(self, transport_product):
        return {
            'name': _('Transportation costs'),
            'order_id': self.id,
            'product_id': transport_product.id,
            'product_uom': transport_product.uom_id.id,
            }

    @api.model
    def create(self, values):
        """
        Add transportation costs to the order if needed
        """
        sale_orders = super().create(values)
        sale_orders._add_transportation_costs()
        return sale_orders

    def _add_transportation_costs(self):
        ICP = self.env['ir.config_parameter'].sudo()
        so_line_env = self.env['sale.order.line']
        product_env = self.env['product.product']
        # Get the order total limit for transportation costs
        order_limit = ICP.get_param('sale_order_transport_cost.sale_order_total_for_transport_cost')
        # If there is an order limit configured and the order is a draft, process transport costs
        if order_limit and order_limit.isdigit():
            for order in self.filtered(lambda o: o.state == "draft"):
                # Get the transport product, create it if it doesn't exist
                transport_product = ICP.get_param('sale_order_transport_cost.product_transport_cost')
                if not transport_product:
                    transport_product = self.env['product.product'].sudo().create(order._prepare_transport_product()).id
                    ICP.set_param('sale_order_transport_cost.product_transport_cost',
                                  transport_product)
                # Check if there already is transport cost
                transport_product = int(transport_product)
                transport_line = order.order_line.filtered(lambda line: line.product_id.id == transport_product)
                # If there is no transport cost and the amount is below the limit, add an order line with the
                # transport cost
                if order.amount_total < int(order_limit) and not transport_line:
                    order_line_vals = order._prepare_transport_line(product_env.browse(transport_product))
                    so_line_env.create(order_line_vals)
                # If there is transport cost, but the total amount is above the limit, remove the transport cost
                elif transport_line and self.amount_total - transport_line[0].price_subtotal >= int(order_limit) and \
                        transport_line:
                    transport_line.unlink()

    def write(self, values):
        """
        Add/remove transportation costs to the order if needed
        """
        sale_order = super(SaleOrder, self).write(values)
        self._add_transportation_costs()
        return sale_order
