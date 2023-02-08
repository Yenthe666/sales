from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.constrains("description_sale")
    def _update_description_sale_quotation_template_lines(self):
        """
            When the description on a product is changed we will check if any of the quotation template lines contains
            this product and if those lines should be updated automatically.
        """
        quotation_template_lines_obj = self.env["sale.order.template.line"]
        for product_template in self:
            quotation_template_lines = quotation_template_lines_obj.search([
                ("auto_update_description", "=", True),
                ("product_id.product_tmpl_id", "=", product_template.id),
            ])
            quotation_template_lines.write({
                "name": product_template.product_variant_ids[0].get_product_multiline_description_sale()
            })
