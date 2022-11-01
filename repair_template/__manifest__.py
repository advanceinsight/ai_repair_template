# -*- coding: utf-8 -*-
{
    'name': "Repair Templates",

    'summary': """Create Repair Templates and apply templates to Repair Orders""",

    'description': """Internal module""",

    'author': "Douwe van Loenen / Advance Insight",
    'website': "http://www.advanceinsight.dev",

    'category': 'Internal',
    'version': '1.0.0',

    'depends': [
        'base',
        'stock',
        'repair',
        'serial_as_asset',
        'sale_management'],

    'data': [
        'views/views.xml',
        'security/ir.model.access.csv',
    ],

    'application': 'False',
    'license': 'OPL-1',
}
