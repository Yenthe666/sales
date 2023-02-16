{
    'name': 'Quotation Template subscription start',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': """This modules allows you to set delay on subscription creation from template.""",
    'description': """This modules allows you to set delay on subscription creation from template.""",
    'author': "Mainframe Monkey",
    'website': "https://www.mainframemonkey.com",
    'depends': ['sale_subscription'],
    'data': [
        'views/sale_order_template_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
