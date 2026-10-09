# -*- coding: utf-8 -*-
# =============================================================================
#  Fuel Management System
# -----------------------------------------------------------------------------
#  Location  : King Abdulaziz Branch Road, Riyadh, Saudi Arabia
#  Email     : sales@leapai.ai
#  Phone     : +966 53 553 3627
#  Website   : https://leapai.ai
#  Developer : Abdulkaraim Osman — Tech Manager | Backend Engineer | DevOps Engineer
#              at Bab International Corp For Specialized Services
#  LinkedIn  : https://www.linkedin.com/in/abdulkaraim-o-385b7a110/
# =============================================================================
{
    'name': 'Fuel Management System',
    'version': '19.0.1.0.0',
    'summary': 'Petrol Pump & Gas Station ERP – Stations, Pumps, Tanks, Shifts, Readings',
    'description': 'Complete fuel station management: multi-station setup, pump/nozzle/tank tracking, shift operations, meter & dip readings, license compliance, and reporting.',
    'category': 'Industries',
    'author': 'LeapAI',
    'maintainer': 'Abdulkaraim Osman',
    'support': 'sales@leapai.ai',
    'website': 'https://www.leapai.ai',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'product', 'stock', 'account', 'hr', 'purchase'],
    'data': [
        'security/fuel_security.xml',
        'security/ir.model.access.csv',
        'data/fuel_sequence_data.xml',
        'views/fuel_station_views.xml',
        'views/fuel_pump_views.xml',
        'views/fuel_nozzle_views.xml',
        'views/fuel_tank_views.xml',
        'views/fuel_shift_views.xml',
        'views/fuel_meter_reading_views.xml',
        'views/fuel_dip_reading_views.xml',
        'views/fuel_license_views.xml',
        'wizard/fuel_price_wizard_views.xml',
        'report/fuel_shift_report.xml',
        'report/fuel_shift_report_template.xml',
        'views/fuel_menus.xml',
    ],
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
        'static/description/screenshot.jpg',
    ],
    'demo': [
        'demo/fuel_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [],
    },
    'application': True,
    'installable': True,
}
