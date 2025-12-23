# Developer Guide - Payment Receipt Report

## Overview

This module extends the Odoo `account.move` model to add payment receipt generation functionality.

## Module Structure

```
payment_receipt_report/
├── __init__.py                      # Module initialization
├── __manifest__.py                  # Module manifest/descriptor
├── models/
│   ├── __init__.py
│   └── account_move.py             # Extends account.move
├── report/
│   ├── payment_receipt_report.xml  # Report definition (ir.actions.report)
│   └── payment_receipt_template.xml # QWeb template
├── security/
│   └── ir.model.access.csv         # Access control rules
├── views/
│   └── account_move_views.xml      # UI modifications
└── docs/
    └── PDF_FORMAT.md               # PDF design documentation
```

## Key Components

### 1. Model Extension (`models/account_move.py`)

```python
class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_print_payment_receipt(self):
        """Trigger payment receipt report generation"""
        self.ensure_one()
        return self.env.ref('payment_receipt_report.action_report_payment_receipt').report_action(self)
```

**Purpose:** Adds method to generate the report

### 2. Report Definition (`report/payment_receipt_report.xml`)

```xml
<record id="action_report_payment_receipt" model="ir.actions.report">
    <field name="name">Payment Receipt</field>
    <field name="model">account.move</field>
    <field name="report_type">qweb-pdf</field>
    <field name="report_name">payment_receipt_report.report_payment_receipt</field>
    ...
</record>
```

**Purpose:** Defines the report action and PDF generation settings

**Key Fields:**
- `report_type`: qweb-pdf (generates PDF)
- `report_name`: References the QWeb template
- `binding_model_id`: Links to account.move model
- `print_report_name`: Dynamic filename for downloaded PDF

### 3. QWeb Template (`report/payment_receipt_template.xml`)

**Structure:**
```xml
<template id="report_payment_receipt">
    <t t-call="web.html_container">
        <t t-foreach="docs" t-as="o">
            <t t-call="web.external_layout">
                <div class="page">
                    <!-- Content here -->
                </div>
            </t>
        </t>
    </t>
</template>
```

**Key QWeb Directives:**
- `t-call="web.external_layout"`: Includes company header/footer with logo
- `t-foreach="docs"`: Iterates over invoice records
- `t-as="o"`: Current invoice object
- `t-field`: Displays field value with automatic formatting
- `t-if`: Conditional rendering
- `t-options`: Widget configuration (e.g., date, monetary)

### 4. View Inheritance (`views/account_move_views.xml`)

```xml
<record id="view_move_form_inherit_payment_receipt" model="ir.ui.view">
    <field name="name">account.move.form.inherit.payment.receipt</field>
    <field name="model">account.move</field>
    <field name="inherit_id" ref="account.view_move_form"/>
    <field name="arch" type="xml">
        <xpath expr="//header/button[@name='action_invoice_print']" position="after">
            <button name="action_print_payment_receipt" 
                    string="Imprimir Comprobante de Pago" 
                    type="object" 
                    .../>
        </xpath>
    </field>
</record>
```

**Purpose:** Adds button to invoice form view header

**XPath Strategy:**
- Finds existing "Print" button
- Inserts new button after it
- Only visible for customer invoices (`out_invoice`, `out_refund`)

### 5. Security Rules (`security/ir.model.access.csv`)

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_payment_receipt_report_user,payment_receipt_report.user,account.model_account_move,base.group_user,1,0,0,0
```

**Purpose:** Grants read access to base users for report generation

## Data Flow

1. **User clicks button** → Triggers `action_print_payment_receipt()`
2. **Method executes** → Returns report action reference
3. **Odoo processes** → Calls QWeb template with invoice data
4. **Template renders** → Generates HTML with invoice data
5. **wkhtmltopdf converts** → Creates PDF from HTML
6. **User downloads** → PDF with dynamic filename

## Available Data in Template

When rendering, the template has access to:

- `o` or `doc`: Current invoice record (account.move)
  - `o.name`: Invoice number
  - `o.partner_id`: Customer record
  - `o.invoice_date`: Invoice date
  - `o.invoice_date_due`: Due date
  - `o.amount_total`: Total amount
  - `o.currency_id`: Currency
  - `o.payment_state`: Payment status
  - `o.company_id`: Company record
  - `o.narration`: Notes/observations

## QWeb Widgets

### Monetary Widget
```xml
<span t-field="o.amount_total" 
      t-options='{"widget": "monetary", "display_currency": o.currency_id}'/>
```
**Output:** € 1,234.56 (formatted with currency symbol)

### Date Widget
```xml
<span t-field="o.invoice_date" t-options='{"widget": "date"}'/>
```
**Output:** 23/12/2024 (formatted according to locale)

### Contact Widget
```xml
<div t-field="o.partner_id" 
     t-options='{"widget": "contact", "fields": ["address"], "no_marker": True}'/>
```
**Output:** Complete formatted address

## Customization Examples

### Add a New Field

1. **In template** (`report/payment_receipt_template.xml`):
```xml
<tr>
    <td class="info-label">Payment Terms:</td>
    <td class="info-value">
        <span t-field="o.invoice_payment_term_id.name"/>
    </td>
</tr>
```

### Modify Colors

1. **In template CSS section**:
```css
.payment-receipt-title {
    color: #0066cc;  /* Change from #875a7b to blue */
}
```

### Change Button Label

1. **In view** (`views/account_move_views.xml`):
```xml
<button name="action_print_payment_receipt" 
        string="Generate Payment Receipt"  <!-- Change here -->
        .../>
```

### Add Conditional Sections

```xml
<div t-if="o.amount_residual > 0">
    <p>Pending Amount: <span t-field="o.amount_residual"/></p>
</div>
```

## Testing

### Manual Testing Steps

1. Install module in test database
2. Create test invoice with sample data
3. Click "Imprimir Comprobante de Pago" button
4. Verify PDF generation
5. Check PDF content and formatting

### Test Cases

- ✅ PDF generates for unpaid invoice
- ✅ PDF generates for paid invoice
- ✅ PDF shows payment status correctly
- ✅ PDF includes all customer data
- ✅ PDF displays company logo
- ✅ PDF handles missing optional fields
- ✅ PDF formats currency correctly
- ✅ Button only appears for customer invoices

## Troubleshooting

### Button not visible
- Check module is installed
- Verify user has correct permissions
- Ensure viewing customer invoice (not vendor bill)

### PDF not generating
- Verify wkhtmltopdf is installed: `wkhtmltopdf --version`
- Check Odoo logs for errors
- Test with simple invoice

### Missing logo
- Configure company logo in Settings → Companies
- Ensure image is uploaded
- Clear browser cache

### Formatting issues
- Review template CSS
- Check browser console for errors
- Test with different browsers

## Performance Considerations

- PDF generation is CPU-intensive (uses wkhtmltopdf)
- Each PDF generation creates temporary files
- For batch operations, consider async processing
- Cache is automatically cleared by Odoo

## Extending the Module

### Add Translations

Create `i18n/es.po`:
```po
msgid "Payment Receipt"
msgstr "Comprobante de Pago"
```

### Add Report Variants

Create multiple templates:
- Simple receipt
- Detailed receipt with line items
- Receipt with payment details

### Add Email Functionality

```python
def action_send_payment_receipt(self):
    """Send payment receipt by email"""
    self.ensure_one()
    template = self.env.ref('payment_receipt_report.email_template_payment_receipt')
    return template.send_mail(self.id, force_send=True)
```

## API Reference

### Methods

#### `action_print_payment_receipt()`
**Description:** Generates and returns payment receipt PDF  
**Parameters:** None (operates on self)  
**Returns:** `ir.actions.report` action  
**Raises:** None  

### Models Referenced

- `account.move`: Invoice/bill model
- `res.partner`: Customer/supplier model
- `res.company`: Company model
- `res.currency`: Currency model

## Dependencies

**Python:**
- No additional Python packages required

**Odoo Modules:**
- `account`: Core accounting module

**System:**
- wkhtmltopdf: For PDF generation

## Version Compatibility

| Odoo Version | Compatible | Notes |
|--------------|-----------|-------|
| 18.0         | ✅        | Primary target |
| 17.0         | ⚠️        | May need minor adjustments |
| 16.0         | ⚠️        | May need adjustments to views |
| 15.0         | ❌        | Requires significant changes |

## Contributing

To contribute:

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## License

LGPL-3 - See LICENSE file for details
