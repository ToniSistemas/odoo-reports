# odoo-reports
Repositorio de Módulos de Reportes para Odoo

## Módulos Disponibles

### Invoice PDF Report (`invoice_pdf_report`)
Módulo para generar reportes PDF profesionales de facturas en Odoo.

**Características:**
- Generación de PDF desde la vista de factura
- Información completa del cliente (nombre, dirección, localidad)
- Detalles de la factura (número, fechas, importe total)
- Estado de pago
- Logo de la empresa
- Formato profesional y limpio
- Funciona con facturas pagadas y no pagadas

**Instalación:**
1. Copiar el módulo `invoice_pdf_report` al directorio de addons de Odoo
2. Actualizar lista de aplicaciones en Odoo
3. Buscar e instalar "Invoice PDF Report"

**Uso:**
1. Ir a Contabilidad > Clientes > Facturas
2. Abrir cualquier factura
3. Hacer clic en el botón "Imprimir Reporte PDF"

## Requisitos
- Odoo 14.0 o superior
- Módulo `account` instalado

## Licencia
LGPL-3
