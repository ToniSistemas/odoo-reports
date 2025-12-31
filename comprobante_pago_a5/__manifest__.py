# -*- coding: utf-8 -*-
{
    'name': 'Comprobante de Pago A5',
    'version': '18.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Generar comprobante de pago PDF en formato A5 desde facturas',
    'description': """
        This module allows you to generate a payment receipt in A5 PDF format 
        from an invoice, even before it is paid.
        
        Features:
        - Payment receipt generation from invoice
        - Professional PDF format in A5 paper size
        - Company logo display
        - Customer and invoice information
        - Can be generated regardless of payment status
        - Optimized layout for A5 paper (148 x 210 mm)
    """,
    'author': 'ToniSistemas',
    'website': 'https://github.com/ToniSistemas/odoo-reports',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'report/comprobante_pago_a5_report.xml',
        'report/comprobante_pago_a5_template.xml',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
