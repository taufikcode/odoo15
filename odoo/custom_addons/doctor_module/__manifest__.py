{
    'name': 'Doctor Management',
    'version': '1.0',
    'summary': 'Module for managing doctor data',
    'sequence': -100,
    'description': """
    Custom module to manage doctor data in Odoo 15.
    """,
    'author': 'RSUD Sorong',
    'category': 'Healthcare',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/doctor_view.xml',
        'views/spesialist_views.xml',
        'views/insurance_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}