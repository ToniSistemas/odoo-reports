# Estructura del Módulo Invoice PDF Report

## Archivos del Módulo

```
invoice_pdf_report/
├── __init__.py                      # Inicialización del módulo
├── __manifest__.py                  # Metadatos del módulo (nombre, versión, dependencias)
├── README.md                        # Documentación del módulo
├── reports/
│   └── invoice_report.xml          # Definición del reporte y plantilla QWeb
├── views/
│   └── invoice_views.xml           # Extensión de vista para agregar botón
└── static/
    └── description/
        └── index.html              # Descripción para la tienda de aplicaciones
```

## Componentes Principales

### 1. __manifest__.py
Define los metadatos del módulo:
- Nombre: Invoice PDF Report
- Versión: 1.0.0
- Categoría: Accounting/Accounting
- Dependencias: account
- Archivos de datos: reports/invoice_report.xml, views/invoice_views.xml

### 2. reports/invoice_report.xml
Contiene dos partes:
- **Definición del Reporte**: Registro `ir.actions.report` que define el reporte PDF
- **Plantilla QWeb**: Template que genera el HTML/PDF con:
  - Logo de la empresa
  - Información del cliente (nombre, dirección, localidad)
  - Detalles de la factura (número, fechas, total)
  - Líneas de factura (descripción, cantidad, precio, subtotal)
  - Estado de pago
  - Texto personalizado según el estado de pago

### 3. views/invoice_views.xml
Extensión de la vista del formulario de factura:
- Hereda de `account.view_move_form`
- Agrega un botón "Imprimir Reporte PDF" en el header
- El botón solo es visible para facturas de cliente (out_invoice, out_refund)
- El botón está disponible independientemente del estado de pago

## Características del Reporte

### Estilos CSS Incluidos
- Header con logo centrado
- Secciones de información con bordes y fondos
- Tabla de líneas de factura con encabezados destacados
- Sección de montos con formato destacado
- Texto de pago con estilo italizado y fondo diferenciado

### Información Mostrada

**Cliente:**
- Nombre
- Dirección completa (calle, calle 2)
- Localidad (ciudad, estado, código postal)
- País

**Factura:**
- Número de factura
- Fecha de emisión
- Fecha de vencimiento
- Estado de pago (Pagado/Pago Parcial/No Pagado)

**Líneas:**
- Descripción del producto/servicio
- Cantidad
- Precio unitario
- Subtotal

**Montos:**
- Subtotal sin impuestos
- Impuestos
- Total

**Texto de Pago:**
- Si está pagado: "He pagado la cantidad total..."
- Si está parcialmente pagado: "He pagado parcialmente... Importe pendiente..."
- Si no está pagado: "Reconozco haber recibido esta factura..."

## Uso

1. Instalar el módulo desde Apps
2. Ir a Contabilidad > Clientes > Facturas
3. Abrir cualquier factura
4. Hacer clic en "Imprimir Reporte PDF"
5. El PDF se genera y descarga automáticamente

## Compatibilidad

- Odoo 14.0+
- Odoo 15.0+
- Odoo 16.0+
- Odoo 17.0+

El módulo es compatible con versiones Community y Enterprise de Odoo.
