{
     'name': 'Rental Property',
    'version': '1.0',
    'category': 'Sales',
    'depends': ['sale_management', 'product'],
    'data': [
        'views/rental_property_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
