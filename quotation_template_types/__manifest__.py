{
    'name': 'Quotation Template Types',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': """Define type on quotation templates.""",
    'description': """Define type on quotation templates.""",
    'author': "Mainframe Monkey",
    'website': "https://www.mainframemonkey.com",
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'data/sale_order_template_type_data.xml',
        'views/sale_order_template_type_views.xml',
        'views/sale_order_template_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
