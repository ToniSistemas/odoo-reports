Invoice PDF Report Module
=========================

This Odoo module provides a professional PDF report for invoices.

Features
--------
* Generate professional PDF reports for invoices at any time
* Display customer information (name, address, location)
* Show invoice details (number, issue date, due date, total amount)
* Include payment status information
* Display company logo
* Professional and clean formatting
* Accessible from invoice form view regardless of payment status

Installation
------------
1. Copy this module to your Odoo addons directory
2. Update the apps list (Apps > Update Apps List)
3. Search for "Invoice PDF Report"
4. Click Install

Usage
-----
1. Go to Accounting > Customers > Invoices
2. Open any invoice
3. Click the "Imprimir Reporte PDF" button in the header
4. The PDF report will be generated and downloaded

Technical Details
-----------------
* Depends on: account
* Model: account.move
* Report Type: QWeb PDF
* View Extensions: Adds button to invoice form view

Author
------
Toni Sistemas
