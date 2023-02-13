{
    'name': 'Quotation Template update description',
    'version': '16.0.1.0.1',
    'category': 'Sales',
    'summary': """This modules updates description on quotation template line when description is updated on product.""",
    'description': """This modules updates description on quotation template line when description is updated on product.""",
    'author': "Mainframe Monkey",
    'website': "https://www.mainframemonkey.com",
    'depends': ['sale_management'],
    'data': [
        'views/sale_order_template_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
