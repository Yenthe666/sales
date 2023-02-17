from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _
from odoo.tools.date_utils import get_timedelta


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _confirm_subscription(self):
        """
            Override of the Odoo method at
            https://github.com/odoo/enterprise/blob/a66f3e670334b2813430fb1f3b9e819192cc53b9/sale_subscription/models/sale_order.py#L628
            This allows us to control the start date of the subscription based on the subscription template it's
            configured delay.
        """
        today = fields.Date.today()
        for sub in self:
            if sub.sale_order_template_id.start_after_days:
                today = today + relativedelta(days=sub.sale_order_template_id.start_after_days)
                sub.write({
                    'next_invoice_date': today
                })
            sub._portal_ensure_token()
            # We set the start date and invoice date at the date of confirmation
            if not sub.start_date:
                sub.start_date = today
            end_date = sub.end_date
            if sub.sale_order_template_id.recurring_rule_boundary == 'limited' and not sub.end_date:
                end_date = sub.start_date + get_timedelta(
                    sub.sale_order_template_id.recurring_rule_count, sub.sale_order_template_id.recurring_rule_type
                ) - relativedelta(days=1)
            sub.write({
                'end_date': end_date
            })
            sub.order_line._reset_subscription_qty_to_invoice()
            sub._save_token_from_payment()
