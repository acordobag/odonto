# -*- coding: utf-8 -*-
{
    'name': "odonto",

    'summary': """
        Modulo para odontologia""",

    'description': """
        Modulo para odontologia
    """,

    'author': "Adrián Córdoba",
    'website': "",
    "application": True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Medical',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','calendar', 'contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/odonto.customer.xml',
        'views/odonto.event.xml',
        'views/odonto.user.xml',
        'views/odonto.resourses.xml'
    ]
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ], "/odoo/odoo-server/addons/web_calendar/static/lib/fullcalendar/js/fullcalendar.js" cambiar el min y em max time

}