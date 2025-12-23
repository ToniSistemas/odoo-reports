# -*- coding: utf-8 -*-
{
    'name': 'Invoice PDF Report',
    'version': '1.0.0',
    'category': 'Accounting/Accounting',
    'summary': 'Generate professional PDF reports for invoices',
    'description': """
        Invoice PDF Report
        ==================
        This module adds a professional PDF report for invoices with:
        * Customer information (name, address, location)
        * Invoice details (number, dates, total amount)
        * Payment status
        * Company logo
        * Professional formatting
        
        The report can be generated at any time, regardless of payment status.
    """,
    'author': 'Toni Sistemas',
    'website': 'https://www.tonisistemas.com',
    'depends': ['account'],
    'data': [
        'reports/invoice_report.xml',
        'views/invoice_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
