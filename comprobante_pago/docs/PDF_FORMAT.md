# Formato del Comprobante de Pago

Este documento describe el diseño y estructura del comprobante de pago generado por el módulo.

## Vista Previa del Diseño

El comprobante de pago tiene un diseño profesional y limpio con las siguientes secciones:

```
┌─────────────────────────────────────────────────────────────────┐
│                         [LOGO EMPRESA]                           │
│                                                                   │
│               ═══════════════════════════════════                │
│                   COMPROBANTE DE PAGO                            │
│            Este documento sirve como comprobante de pago        │
│               ═══════════════════════════════════                │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Información del Cliente                                  │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │ Nombre/Razón Social:  Juan Pérez García                 │   │
│  │ Dirección:            Calle Principal 123, Piso 2       │   │
│  │ Localidad:            Madrid - Comunidad de Madrid      │   │
│  │ ID Fiscal:            B12345678                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Información de la Factura                                │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │ Número de Factura:    INV/2024/00123                    │   │
│  │ Fecha de Emisión:     23/12/2024                        │   │
│  │ Fecha de Vencimiento: 22/01/2025                        │   │
│  │ Referencia:           SO/2024/00456                     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                           │   │
│  │                   IMPORTE TOTAL                          │   │
│  │                                                           │   │
│  │                     € 1,234.56                           │   │
│  │                                                           │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│                      [ ✓ PAGADO ]                                │
│                   (si la factura está pagada)                   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Observaciones                                            │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │ Notas adicionales o comentarios sobre la factura        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│                                                                   │
│         Este comprobante ha sido generado electrónicamente      │
│                    Nombre de la Empresa - NIF                   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

## Características del Diseño

### Colores

- **Color principal:** `#875a7b` (morado Odoo)
- **Color de fondo de recuadros:** `#f5f5f5` (gris claro)
- **Bordes:** `#e0e0e0` (gris medio)
- **Estado pagado:** `#d4edda` fondo, `#155724` texto (verde)

### Tipografía

- **Título principal:** 28px, negrita
- **Subtítulo:** 16px, regular
- **Títulos de sección:** 18px, negrita
- **Etiquetas:** normal, negrita
- **Valores:** normal, regular
- **Importe total:** 32px, negrita

### Secciones

#### 1. Cabecera
- Logo de la empresa (configurado en Odoo)
- Título "COMPROBANTE DE PAGO" destacado
- Subtítulo explicativo
- Línea decorativa inferior

#### 2. Información del Cliente
- Nombre/Razón Social (obligatorio)
- Dirección completa (opcional)
- Localidad y estado (opcional)
- ID Fiscal / NIF (opcional)

#### 3. Información de la Factura
- Número de factura (obligatorio)
- Fecha de emisión (obligatorio)
- Fecha de vencimiento (si existe)
- Referencia / origen (si existe)

#### 4. Importe Total
- Recuadro destacado con borde
- Fondo gris claro
- Importe en grande con símbolo de moneda
- Formato según la moneda configurada

#### 5. Estado de Pago
- Solo visible si la factura está pagada o en proceso de pago
- Badge verde con checkmark
- Mensaje "PAGADO"

#### 6. Observaciones
- Solo visible si existen notas en la factura
- Recuadro con borde izquierdo destacado
- Texto completo de las observaciones

#### 7. Pie de Página
- Texto de generación electrónica
- Nombre de la empresa
- NIF de la empresa
- Formato centrado e itálica

## Adaptabilidad

El diseño se adapta automáticamente a:

- **Longitud de direcciones:** Las direcciones largas se ajustan automáticamente
- **Múltiples monedas:** El símbolo de moneda se adapta según configuración
- **Idiomas:** Compatible con múltiples idiomas (RTL pendiente)
- **Datos faltantes:** Las secciones opcionales se ocultan si no hay datos

## Personalización

### Modificar Colores

Edite las clases CSS en `payment_receipt_template.xml`:

```css
.payment-receipt-title {
    color: #875a7b;  /* Cambiar este valor */
}
```

### Cambiar Tamaño de Fuente

```css
.amount-value {
    font-size: 32px;  /* Ajustar según necesidad */
}
```

### Agregar Nuevos Campos

Agregue nuevas filas en las tablas de información:

```xml
<tr>
    <td class="info-label">Nuevo Campo:</td>
    <td class="info-value">
        <span t-field="o.nuevo_campo"/>
    </td>
</tr>
```

## Compatibilidad de Impresión

El diseño está optimizado para:

- Tamaño A4 (210mm x 297mm)
- Orientación vertical
- Márgenes estándar
- Impresión en blanco y negro (manteniendo contraste)
- Exportación a PDF

## Ejemplo de Uso

### Factura sin pagar
```
COMPROBANTE DE PAGO
-------------------
Cliente: ABC Corp
Factura: INV/2024/001
Fecha: 23/12/2024
Total: € 1,000.00
```

### Factura pagada
```
COMPROBANTE DE PAGO
-------------------
Cliente: ABC Corp
Factura: INV/2024/001
Fecha: 23/12/2024
Total: € 1,000.00
✓ PAGADO
```

## Notas Técnicas

- El logo se obtiene de `company_id.logo` a través del layout externo
- Los campos de dirección usan el widget `contact` de Odoo
- Los importes usan el widget `monetary` para formato correcto
- Las fechas usan el widget `date` para formato local
- El PDF se genera con wkhtmltopdf
