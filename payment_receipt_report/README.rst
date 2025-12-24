================================
Comprobante de Pago
================================

This module allows you to generate a payment receipt in PDF format from invoices in Odoo 18.0, regardless of their payment status.

**Features**

* Generate payment receipt PDF from any invoice
* Professional and clean design
* Displays company logo (from external layout)
* Includes complete customer information (name, address, locality, tax ID)
* Shows invoice details (number, issue date, due date, total amount)
* Works for invoices in any payment state
* One-click button in invoice form view
* Customizable QWeb template

**Installation**

1. Copy the ``payment_receipt_report`` folder to your Odoo addons directory
2. Update the addons list in Odoo: Go to Apps → Update Apps List
3. Search for "Comprobante de Pago" in the Apps menu
4. Click Install

**Configuration**

No configuration is required. The module works out of the box.

**Usage**

1. Navigate to Accounting → Customers → Invoices
2. Open any customer invoice or credit note
3. Click the "Imprimir Comprobante de Pago" button in the header
4. The PDF will be generated and downloaded automatically

**Technical Information**

:Module: payment_receipt_report
:Version: 18.0.1.0.0
:Category: Accounting
:Dependencies: account
:License: LGPL-3

**Structure**

::

    payment_receipt_report/
    ├── __init__.py
    ├── __manifest__.py
    ├── models/
    │   ├── __init__.py
    │   └── account_move.py          # Extends account.move with print action
    ├── report/
    │   ├── payment_receipt_report.xml    # Report definition
    │   └── payment_receipt_template.xml  # QWeb template for PDF
    ├── security/
    │   └── ir.model.access.csv      # Access rights
    └── views/
        └── account_move_views.xml   # Adds button to invoice form

**Customization**

To customize the payment receipt template:

1. Edit ``report/payment_receipt_template.xml``
2. Modify the HTML structure and CSS styles as needed
3. Update the module to apply changes

**Template Structure**

The QWeb template includes:

* **Header**: "COMPROBANTE DE PAGO" title with subtitle
* **Customer Information**: Name, address, locality, tax ID
* **Invoice Information**: Invoice number, dates, reference
* **Amount Box**: Highlighted total amount
* **Payment Status**: Visual indicator if already paid
* **Observations**: Additional notes from invoice
* **Footer**: Company information and electronic generation notice

**Support**

For issues, questions, or contributions:

* Repository: https://github.com/ToniSistemas/odoo-reports
* Create an issue on GitHub

**Credits**

:Author: ToniSistemas
:Maintainer: ToniSistemas

**License**

This module is licensed under LGPL-3.
