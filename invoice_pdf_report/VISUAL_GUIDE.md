# Guía Visual del Módulo Invoice PDF Report

## 📁 Estructura del Módulo

```
invoice_pdf_report/
│
├── 📄 __init__.py                  # Inicialización del módulo
├── 📄 __manifest__.py              # Configuración del módulo
├── 📄 LICENSE                      # Licencia LGPL-3
│
├── 📚 Documentación/
│   ├── 📄 README.md               # Documentación principal
│   ├── 📄 DOCUMENTATION.md        # Documentación técnica detallada
│   ├── 📄 TESTING_GUIDE.md        # Guía de instalación y pruebas
│   ├── 📄 CONFIGURATION.md        # Guía de configuración
│   └── 📄 EXAMPLES.md             # Ejemplos de uso
│
├── 📂 reports/                     # Reportes QWeb
│   └── 📄 invoice_report.xml      # Definición del reporte + Template
│
├── 📂 views/                       # Vistas personalizadas
│   └── 📄 invoice_views.xml       # Extensión de vista de factura
│
└── 📂 static/                      # Recursos estáticos
    └── 📂 description/
        └── 📄 index.html          # Descripción para tienda de apps

```

---

## 🎨 Vista Previa del Reporte PDF

```
┌─────────────────────────────────────────────────────┐
│                                                       │
│                    [LOGO EMPRESA]                     │
│                      FACTURA                          │
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│                                                       │
│  ┌─────────────────────┐  ┌─────────────────────┐  │
│  │ Cliente:             │  │ Número de Factura:  │  │
│  │ Juan Pérez           │  │ INV/2024/0001       │  │
│  │                      │  │                     │  │
│  │ Dirección:           │  │ Fecha de Emisión:   │  │
│  │ Calle Principal 123  │  │ 15/01/2024          │  │
│  │                      │  │                     │  │
│  │ Localidad:           │  │ Fecha Vencimiento:  │  │
│  │ Madrid, 28001        │  │ 15/02/2024          │  │
│  │                      │  │                     │  │
│  │ País:                │  │ Estado:             │  │
│  │ España               │  │ ✓ Pagado            │  │
│  └─────────────────────┘  └─────────────────────┘  │
│                                                       │
│  ┌───────────────────────────────────────────────┐  │
│  │ Descripción      │ Cant │ P.Unit │ Subtotal  │  │
│  ├──────────────────┼──────┼────────┼───────────┤  │
│  │ Producto A       │  2   │ 50.00€ │ 100.00€   │  │
│  │ Servicio B       │  1   │ 75.00€ │  75.00€   │  │
│  └───────────────────────────────────────────────┘  │
│                                                       │
│                              Subtotal:   175.00€     │
│                              Impuestos:   36.75€     │
│                              ─────────────────────    │
│                              TOTAL:      211.75€     │
│                                                       │
│  ┌───────────────────────────────────────────────┐  │
│  │ He pagado la cantidad total de 211.75€        │  │
│  │ correspondiente a esta factura.               │  │
│  └───────────────────────────────────────────────┘  │
│                                                       │
└─────────────────────────────────────────────────────┘
```

---

## 🔧 Componentes Clave

### 1. **__manifest__.py**
```python
{
    'name': 'Invoice PDF Report',
    'version': '1.0.0',
    'depends': ['account'],
    'data': [
        'reports/invoice_report.xml',
        'views/invoice_views.xml',
    ],
}
```

**Función:** Define metadatos, dependencias y archivos del módulo.

---

### 2. **reports/invoice_report.xml**

#### Parte A: Definición del Reporte
```xml
<record id="action_report_invoice_pdf" model="ir.actions.report">
    <field name="name">Invoice PDF Report</field>
    <field name="model">account.move</field>
    <field name="report_type">qweb-pdf</field>
    <field name="report_name">invoice_pdf_report.report_invoice_pdf_template</field>
</record>
```

**Función:** Registra el reporte en Odoo como tipo PDF.

#### Parte B: Template QWeb
```xml
<template id="report_invoice_pdf_template">
    <t t-call="web.html_container">
        <t t-foreach="docs" t-as="o">
            <!-- Logo -->
            <img t-att-src="image_data_uri(o.company_id.logo)"/>
            
            <!-- Información Cliente -->
            <t t-esc="o.partner_id.name"/>
            <t t-esc="o.partner_id.street"/>
            
            <!-- Información Factura -->
            <t t-esc="o.name"/>
            <t t-esc="o.invoice_date"/>
            <t t-esc="o.amount_total"/>
            
            <!-- Líneas de Factura -->
            <t t-foreach="o.invoice_line_ids" t-as="line">
                <t t-esc="line.name"/>
            </t>
        </t>
    </t>
</template>
```

**Función:** Define el HTML/CSS que se convertirá en PDF.

---

### 3. **views/invoice_views.xml**

```xml
<record id="view_move_form_inherited" model="ir.ui.view">
    <field name="inherit_id" ref="account.view_move_form"/>
    <field name="arch" type="xml">
        <xpath expr="//header" position="inside">
            <button name="%(action_report_invoice_pdf)d" 
                    string="Imprimir Reporte PDF" 
                    type="action"/>
        </xpath>
    </field>
</record>
```

**Función:** Agrega el botón "Imprimir Reporte PDF" en el header de la vista de factura.

---

## 🎯 Flujo de Funcionamiento

```
┌─────────────────┐
│ Usuario abre    │
│ una factura     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Vista de        │
│ factura con     │ ◄─── views/invoice_views.xml
│ botón agregado  │      (Extensión de vista)
└────────┬────────┘
         │
         │ Click en "Imprimir Reporte PDF"
         │
         ▼
┌─────────────────┐
│ Odoo llama al   │
│ reporte         │ ◄─── Registro ir.actions.report
│ configurado     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ QWeb procesa    │
│ el template     │ ◄─── Template QWeb
│ con datos       │      (reports/invoice_report.xml)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ wkhtmltopdf     │
│ convierte HTML  │
│ a PDF           │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ PDF descargado  │
│ al navegador    │
└─────────────────┘
```

---

## 🎨 Elementos de Diseño

### Colores Utilizados:
- **#333**: Negro suave para texto principal
- **#555**: Gris oscuro para etiquetas
- **#ddd**: Gris claro para bordes
- **#f9f9f9**: Gris muy claro para fondos
- **verde**: Estado "Pagado"
- **naranja**: Estado "Pago Parcial"
- **rojo**: Estado "No Pagado"

### Estilos CSS Principales:
- `.invoice-header`: Header centrado con logo
- `.info-box`: Cajas con borde y fondo para información
- `.details-table`: Tabla de líneas con header oscuro
- `.total-amount`: Monto total destacado
- `.payment-text`: Texto de pago con estilo especial

---

## 📊 Datos del Módulo

| Métrica | Valor |
|---------|-------|
| **Archivos totales** | 11 |
| **Líneas de código XML** | ~250 |
| **Líneas de CSS** | ~80 |
| **Líneas de Python** | ~30 |
| **Tamaño total** | 88 KB |
| **Dependencias** | 1 (account) |
| **Documentación** | 6 archivos |

---

## 🚀 Estados del Reporte

### Estado 1: Factura No Pagada
- Texto: "Reconozco haber recibido esta factura..."
- Color estado: Rojo

### Estado 2: Factura Pagada
- Texto: "He pagado la cantidad total de X €..."
- Color estado: Verde

### Estado 3: Pago Parcial
- Texto: "He pagado parcialmente... Importe pendiente: X €"
- Color estado: Naranja

---

## 🔍 Campos Mostrados en el PDF

### Información del Cliente:
✅ Nombre  
✅ Dirección (calle + calle 2)  
✅ Ciudad  
✅ Estado/Provincia  
✅ Código Postal  
✅ País  

### Información de la Factura:
✅ Número de factura  
✅ Fecha de emisión  
✅ Fecha de vencimiento  
✅ Estado de pago  

### Líneas de Factura:
✅ Descripción del producto/servicio  
✅ Cantidad  
✅ Precio unitario  
✅ Subtotal por línea  

### Totales:
✅ Subtotal sin impuestos  
✅ Impuestos  
✅ Total  
✅ Símbolo de moneda  

---

## ✨ Características Especiales

### 1. **Manejo de Datos Opcionales**
- Si no hay logo, se omite la imagen
- Si no hay fecha de vencimiento, muestra texto alternativo
- Si no hay dirección, solo muestra campos disponibles

### 2. **Soporte Multi-moneda**
- El símbolo de moneda se toma automáticamente de la factura
- Formato de decimales configurable

### 3. **Diseño Responsive**
- Se adapta al tamaño del papel
- Paginación automática para facturas largas

### 4. **Seguridad**
- Sin inyección SQL
- Validación de datos
- Manejo seguro de None/False

---

## 📖 Archivos de Documentación

| Archivo | Propósito | Páginas |
|---------|-----------|---------|
| **README.md** | Descripción general | 1 |
| **DOCUMENTATION.md** | Detalles técnicos | 3 |
| **TESTING_GUIDE.md** | Guía de pruebas | 5 |
| **CONFIGURATION.md** | Configuración | 4 |
| **EXAMPLES.md** | Ejemplos de uso | 5 |

---

## 🎓 Para Desarrolladores

### Personalizar Colores:
```css
.invoice-title {
    color: #0066cc;  /* Tu color aquí */
}
```

### Personalizar Formato de Fecha:
```xml
<t t-esc="o.invoice_date.strftime('%m/%d/%Y')"/>  <!-- Formato USA -->
```

### Agregar Nuevo Campo:
```xml
<div class="info-label">Tu Campo:</div>
<div class="info-value">
    <t t-esc="o.tu_campo_personalizado"/>
</div>
```

---

## ✅ Checklist de Implementación

- [x] Estructura de módulo Odoo estándar
- [x] Definición de reporte en XML
- [x] Template QWeb completo
- [x] Estilos CSS profesionales
- [x] Botón en vista de factura
- [x] Manejo de datos opcionales
- [x] Validación de sintaxis
- [x] Documentación completa
- [x] Ejemplos de uso
- [x] Guías de instalación y testing
- [x] Licencia open source
- [x] Sin vulnerabilidades de seguridad

---

## 📞 Recursos

- **Documentación Odoo**: https://www.odoo.com/documentation
- **QWeb Reports**: https://www.odoo.com/documentation/17.0/developer/reference/backend/reports.html
- **GitHub Repo**: ToniSistemas/odoo-reports

---

**Versión del Módulo:** 1.0.0  
**Autor:** Toni Sistemas  
**Licencia:** LGPL-3  
**Compatibilidad:** Odoo 14.0+
