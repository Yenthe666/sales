{
    'name': 'Sale Order Transport Cost',
    'version': '14.0.0.1',
    'category': 'Sales',
    'summary': """Automatically add transport costs to a sale order.""",
    'description': """Automatically add transport costs to a sale order.""",
    'author': "Mainframe Monkey",
    'website': "https://www.mainframemonkey.com",
    'depends': ['l10n_generic_coa', 'sale_management'],
    'data': [
        'data/product_product.xml',
        'views/res_config_settings_views.xml',
        #
        # "views/account_move_views.xml",
        # "views/product_template_views.xml",
        # "views/sale_order_views.xml",
        #
        # "report/account_move_templates.xml",
        # "report/sale_order_portal_templates.xml",
        # "report/sale_order_templates.xml",
    ],
    'installable': True,
    'application': True,
}