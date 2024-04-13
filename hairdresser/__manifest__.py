# Copyright © 2022 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'Hairdresser',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """
        Odoo School
        Coursework.
    """,
    'license': 'LGPL-3',
    'author': 'Viktor',
    'sequence': -100,
    'website': 'https://github.com/VictorS111/demo',
    'depends': [
        'web', 'base', 'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/create_booking_view.xml',
        'views/hairdresser_menus.xml',
        'views/hairdresser_views.xml',
        'views/service_views.xml',
        'views/working_hours_views.xml',
        'views/hairdresser_chair_views.xml',
        'views/customer_views.xml',
        'report/booking.xml',
        'report/report.xml',
        'data/customer_data.xml',
        # 'data/service_data.xml',
        # 'data/working_hours_data.xml',
    ],
    'demo': [
        'data/service_data.xml',
        'data/working_hours_data.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
