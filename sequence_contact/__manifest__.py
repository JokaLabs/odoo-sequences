# -*- coding: utf-8 -*-
{
    'name': "Nº de contacto",

    'summary': """
        Agrega un número a los contactos.""",

    'description': """
        Agrega un número de sequencia en los contactos.
    """,

    'author': "Tlacloc-ES",
    'website': "http://www.jokalabs.com | http://github.com/JokaLabs/odoo-sequences",

    'category': 'Herramientas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'views/templates.xml',
        'data/sequence_contact.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}