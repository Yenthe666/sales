from odoo import api, fields, models, _


class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    auto_update_description_updated = fields.Boolean(
        string="Auto update description updated on line?",
        compute="_compute_auto_update_description_updated",
        help="Technical field to show banner on form view"
    )

    @api.depends("sale_order_template_line_ids.auto_update_description")
    def _compute_auto_update_description_updated(self):
        """
        Show banner on template form view if auto_update_description is change for any line
        """
        self.auto_update_description_updated = False
        for template in self:
            for line in template.sale_order_template_line_ids:
                if not line._origin.auto_update_description and \
                        line.auto_update_description != line._origin.auto_update_description:
                    template.auto_update_description_updated = True
                    break
