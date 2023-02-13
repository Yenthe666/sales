from odoo import api, fields, models, _


class SaleOrderTemplateLine(models.Model):
    _inherit = "sale.order.template.line"

    auto_update_description = fields.Boolean(
        string="Auto update description?",
        help="If this boolean is toggled on we will automatically update the description of this line when somebody "
             "changes the description on the linked product. If this boolean is not toggled on we will ignore this "
             "line and will never update the description set on the current quotation template line."
             "This functionality serves as an easy way to manage/update descriptions in bulk for when you work with "
             "many quotation templates.",
        default=True
    )

    @api.onchange("auto_update_description")
    def _onchange_auto_update_description(self):
        """
            When the auto_update_description on a line is changed,
            description should be updated automatically.
        """
        for line in self:
            # check for product_variant_ids since they are not created when we create new template
            if line.auto_update_description:
                line.name = line.product_id.get_product_multiline_description_sale()
