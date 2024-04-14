# -*- coding: utf-8 -*-

# pylint: disable=pointless-statement

{
    'name': "Real Estate",

    'summary': """
        Manage your real estate properties with ease.""",

    'description': """
        This module allows you to efficiently manage your real estate properties, 
        including properties for sale or rent, potential clients, lease contracts, etc.
    """,

    'author': "@NathanBangwa243",
    'website': "http://www.gofamille.org",

    'category': 'Sales/Real Estate',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_actions.xml',
        'views/estate_menus.xml',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
