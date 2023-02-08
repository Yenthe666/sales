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
