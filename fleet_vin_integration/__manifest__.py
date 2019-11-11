# -*- coding: utf-8 -*-
{
    'name': "VIN api integration for fleet",
    'summary': """
       VIN number api integration""",

    'description': """
       The VIN standard is applied in many countries and it is used by all large producers of cars.
       This code is used in Australia, New Zealand, the United States of America, Europe and other countries.
       You can easily get details filled in your fields using this module...
       please make sure you have added the fields for integration
    """,

    'author': "shalin wilson",
    'website': "https://www.linkedin.com/in/shalin-wilson-a1318183/",
    'category': 'Uncategorized',
    'version': '13.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'fleet'],
    'license': 'OPL-1',
    'support': 'shalinwilson1994@gmail.com',

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/car_creating_page.xml',
        'demo/demo.xml'
    ],

    'installable': True,
    'application': True,
}
