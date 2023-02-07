from odoo import api, fields, models, _


class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    customer_ids = fields.Many2many(
        "res.partner",
        string="Customers",
        help="This template will only be shown on quotations when the customer filled in on the quotation is within "
             "the list of customers filled in on this quotation template. If this field is left empty the quotation "
             "template will always be shown/selectable on the quotation."
    )
