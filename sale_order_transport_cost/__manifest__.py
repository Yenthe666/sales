{
    'name': 'Sale Order Transport Cost',
    'version': '17.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': """Automatically add transport costs to a sale order.""",
    'description': """Automatically add transport costs to a sale order.""",
    'author': "Mainframe Monkey",
    'website': "https://www.mainframemonkey.com",
    'depends': [
        'sale_management'
    ],
    'data': [
        'data/product_product.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
