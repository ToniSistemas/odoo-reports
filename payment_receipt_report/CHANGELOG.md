# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [18.0.1.0.0] - 2025-12-23

### Added
- Lanzamiento inicial del módulo Comprobante de Pago
- PDF generation for payment receipts from invoices
- Professional QWeb template with company logo support
- Customer information display (name, address, locality, tax ID)
- Invoice information display (number, dates, amount)
- Highlighted total amount box
- Payment status indicator for paid invoices
- "Imprimir Comprobante de Pago" button in invoice form view
- Support for customer invoices and credit notes
- Works regardless of invoice payment status
- Comprehensive documentation (README.rst, INSTALL.md)
- Security rules and access rights
- Compatible with Odoo 18.0

### Technical Details
- Extends `account.move` model with print action
- Custom QWeb report template
- Inherits invoice form view to add button
- Uses external layout for company branding
- Responsive and professional design with CSS styling

### Security
- Access rights for base user group
- Read-only permissions for report generation

## [Unreleased]

### Planned Features
- Multi-language support
- Additional template styles/themes
- Batch printing for multiple invoices
- Email sending capability
- Custom field configuration through settings
