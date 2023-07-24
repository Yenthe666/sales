# -*- coding: utf-8 -*-
{
    'name': "update_product_prices_by_category",

    'summary': """
        Update product prices for a product category
    """,

    'description': """
        Update product prices for a product category
    """,

    'author': "Mainframe Monkey",
    'website': "https://www.mainframemonkey.com",
    'license': 'LGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_config_parameter.xml',
        'wizard/product_category_price_update_wizard.xml',
        'views/product_category_views.xml',
    ],
}
