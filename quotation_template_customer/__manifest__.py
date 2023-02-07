{
    'name': 'Quotation Template Customer',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': """This module allows you to filter quotation templates based on selected customers.""",
    'description': """This module allows you to filter quotation templates based on selected customers.""",
    'author': "Mainframe Monkey",
    'website': "https://www.mainframemonkey.com",
    'depends': ['sale_management'],
    'data': [
        'views/sale_order_template_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
