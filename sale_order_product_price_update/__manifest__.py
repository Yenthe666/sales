# -*- coding: utf-8 -*-
{
    'name': "Sale Order Product Price Update",

    'summary': """
        This module adds a button to a quotation/order that enables you to update the order line prices with the latest sale price on the products.
        """,

    'description': """
        This module adds a button to a quotation/order that enables you to update the order line prices with the latest sale price on the products.
    """,

    'author': "Mainframe Monkey",
    'website': "https://www.mainframemonkey.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '15.0.1.0.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': [
        'sale_management',
    ],

    # always loaded
    'data': [
        # SECURITY
        'security/ir.model.access.csv',

        # VIEWS
        'wizards/sale_order_product_price_update_views.xml',
        'views/product_template_views.xml',
        'views/sale_order_views.xml',
    ],
}