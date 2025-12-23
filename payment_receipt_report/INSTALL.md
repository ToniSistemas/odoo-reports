# Payment Receipt Report Module - Installation Guide

## Descripción

Este módulo permite generar comprobantes de pago en formato PDF desde las facturas de Odoo 18.0, independientemente del estado de pago de la factura.

## Características Principales

- ✅ Generación de comprobante de pago en PDF
- ✅ Funciona con facturas en cualquier estado (pagada o no pagada)
- ✅ Incluye logo de la empresa
- ✅ Muestra información completa del cliente y factura
- ✅ Diseño profesional y personalizable
- ✅ Botón de un solo clic en el formulario de factura
- ✅ Compatible con Odoo 18.0

## Requisitos

- Odoo 18.0
- Módulo `account` (Contabilidad) instalado

## Instalación

### Método 1: Manual

1. Copie la carpeta `payment_receipt_report` a su directorio de addons de Odoo:
   ```bash
   cp -r payment_receipt_report /ruta/a/odoo/addons/
   ```

2. Reinicie el servidor de Odoo:
   ```bash
   sudo systemctl restart odoo
   # o
   ./odoo-bin -c /etc/odoo/odoo.conf --stop-after-init
   ```

3. Active el modo desarrollador en Odoo:
   - Vaya a Ajustes
   - Haga clic en "Activar el modo desarrollador"

4. Actualice la lista de aplicaciones:
   - Vaya a Aplicaciones → Actualizar lista de aplicaciones
   - Busque "Payment Receipt Report"
   - Haga clic en "Instalar"

### Método 2: Usando Odoo CLI

```bash
./odoo-bin -c /etc/odoo/odoo.conf -d your_database -i payment_receipt_report --stop-after-init
```

## Uso

### Generar Comprobante de Pago

1. Navegue a **Contabilidad → Clientes → Facturas**
2. Abra cualquier factura de cliente
3. Haga clic en el botón **"Imprimir Comprobante de Pago"** en la cabecera
4. El PDF se generará y descargará automáticamente

### Información Incluida en el Comprobante

El comprobante de pago incluye:

- **Cabecera**: Título "COMPROBANTE DE PAGO" con subtítulo
- **Información del Cliente**:
  - Nombre/Razón Social
  - Dirección completa
  - Localidad y estado
  - ID Fiscal (NIF/CIF)
- **Información de la Factura**:
  - Número de factura
  - Fecha de emisión
  - Fecha de vencimiento
  - Referencia (si existe)
- **Importe Total**: Destacado en un recuadro especial
- **Estado de Pago**: Indicador visual si ya está pagada
- **Observaciones**: Notas adicionales de la factura
- **Pie de página**: Información de la empresa

## Personalización

### Modificar la Plantilla

Para personalizar el diseño del comprobante:

1. Edite el archivo `report/payment_receipt_template.xml`
2. Modifique los estilos CSS en la sección `<style>`
3. Ajuste la estructura HTML según sus necesidades
4. Actualice el módulo en Odoo:
   ```bash
   ./odoo-bin -c /etc/odoo/odoo.conf -d your_database -u payment_receipt_report
   ```

### Cambiar el Nombre del Archivo PDF

Edite el campo `print_report_name` en `report/payment_receipt_report.xml`:

```xml
<field name="print_report_name">'Comprobante_Pago_%s_%s' % (object.name or 'Factura', object.invoice_date or '')</field>
```

### Agregar Campos Adicionales

1. Edite `report/payment_receipt_template.xml`
2. Agregue nuevas filas en las tablas de información:
   ```xml
   <tr>
       <td class="info-label">Nuevo Campo:</td>
       <td class="info-value">
           <span t-field="o.campo_personalizado"/>
       </td>
   </tr>
   ```

## Estructura del Módulo

```
payment_receipt_report/
├── __init__.py                          # Inicialización del módulo
├── __manifest__.py                      # Manifiesto del módulo
├── README.rst                           # Documentación principal
├── INSTALL.md                           # Esta guía
├── models/
│   ├── __init__.py
│   └── account_move.py                  # Extensión del modelo account.move
├── report/
│   ├── payment_receipt_report.xml       # Definición del reporte
│   └── payment_receipt_template.xml     # Plantilla QWeb del PDF
├── security/
│   └── ir.model.access.csv             # Derechos de acceso
├── views/
│   └── account_move_views.xml          # Vista heredada con botón
└── static/
    └── description/
        └── index.html                   # Descripción del módulo
```

## Solución de Problemas

### El botón no aparece

- Verifique que el módulo esté instalado correctamente
- Asegúrese de estar en una factura de cliente (no de proveedor)
- Actualice la página del navegador (Ctrl+F5)

### Error al generar el PDF

- Verifique que `wkhtmltopdf` esté instalado:
  ```bash
  wkhtmltopdf --version
  ```
- Si no está instalado:
  ```bash
  sudo apt-get install wkhtmltopdf
  ```

### El logo no aparece

- Configure el logo de la empresa en Ajustes → Empresas → Su empresa
- Suba una imagen en el campo "Logo"

### Permisos insuficientes

- Verifique que el usuario tenga permisos de "Usuario" (base.group_user)
- Revise los permisos en Ajustes → Usuarios y Empresas → Usuarios

## Desinstalación

1. Vaya a Aplicaciones
2. Busque "Payment Receipt Report"
3. Haga clic en "Desinstalar"
4. Confirme la desinstalación

## Soporte

Para reportar problemas o solicitar características:

- Repositorio: https://github.com/ToniSistemas/odoo-reports
- Cree un issue en GitHub

## Licencia

Este módulo está licenciado bajo LGPL-3.

## Créditos

- Autor: ToniSistemas
- Mantenedor: ToniSistemas

## Compatibilidad

- Odoo 18.0 ✅
- Odoo 17.0 ❌ (requiere adaptación)
- Odoo 16.0 ❌ (requiere adaptación)
