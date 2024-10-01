{
    'name': 'Custom Biodata Form',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Custom web form for biodata input',
    'description': """
This module adds a custom web form for biodata input on the website.
    """,
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/biodata_views.xml',
        'data/website_menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}