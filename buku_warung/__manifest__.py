# -*- coding: utf-8 -*-
{
    'name': "buku_kas",
    'version': "1.0",

    'summary': "for UMKM software",
    'sequence': -100,

    'description': """
        UMKM software for calculate budget and cash
    """,
    'category': 'Productivity',
    'website': "http://www.odoomates.com",
    'depends': [
        'sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale.xml',
        'views/customer.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
