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
    'website': "http://githun.com/gofamille",

    'category': 'Real Estate/Brokerage',
    'version': '1.4',

    'depends': ['base'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        # estate property
        'views/estate_property_actions.xml',
        'views/estate_menus.xml',
        'views/estate_property_views.xml',

        # estate property offer
        'views/estate_property_offer_views.xml',

        # estate property type
        'views/estate_property_type_views.xml',

        # estate property tag
        'views/estate_property_tag_views.xml',
        'views/res_users.xml',

        # MASTER DATAS
        # estate property type
        'data/estate_property_type_data.xml',

        # DEMO DATAS
        # estate property
        'demo/estate_property_demo.xml',
        'demo/estate_property_offer_demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
