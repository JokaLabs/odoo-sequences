# -*- coding: utf-8 -*-
{
    'name': "Nº de empleado",

    'summary': """
        Agrega un número a los empleados.""",

    'description': """
        Agrega un número de sequencia en los empleados.
    """,

    'author': "Tlacloc-ES",
    'website': "http://www.jokalabs.com | http://github.com/JokaLabs/odoo-sequences",

    'category': 'Herramientas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'views/templates.xml',
        'data/sequence_employee.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}