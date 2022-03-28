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
    ],
    'installable': True,
    'application': True,
}