# Guía de Instalación y Prueba - Invoice PDF Report

## Requisitos Previos

- Odoo instalado (versión 14.0 o superior)
- Acceso a la carpeta de addons de Odoo
- Módulo `account` (Contabilidad) instalado

## Instalación

### Opción 1: Instalación Manual

1. **Copiar el módulo a la carpeta de addons:**
   ```bash
   cp -r invoice_pdf_report /path/to/odoo/addons/
   ```

2. **Reiniciar el servidor de Odoo:**
   ```bash
   # Si usas el comando odoo-bin
   ./odoo-bin -c /path/to/odoo.conf --stop-after-init
   ./odoo-bin -c /path/to/odoo.conf
   
   # O si usas servicio systemd
   sudo systemctl restart odoo
   ```

3. **Actualizar la lista de aplicaciones en Odoo:**
   - Ir a: Aplicaciones (Apps)
   - Click en el menú (☰) > Actualizar Lista de Aplicaciones
   - Confirmar la actualización

4. **Instalar el módulo:**
   - En Aplicaciones, buscar "Invoice PDF Report"
   - Click en "Instalar"

### Opción 2: Instalación con Modo Desarrollador

1. **Activar modo desarrollador:**
   - Ir a: Ajustes > Activar modo de desarrollador

2. **Actualizar lista de aplicaciones:**
   - Aplicaciones > Actualizar Lista de Aplicaciones

3. **Instalar desde apps:**
   - Buscar "Invoice PDF Report"
   - Instalar

## Verificación de la Instalación

### 1. Verificar que el módulo está instalado

```bash
# En la base de datos de Odoo, verificar:
SELECT name, state FROM ir_module_module WHERE name = 'invoice_pdf_report';
```

Debe mostrar `state = 'installed'`

### 2. Verificar que el reporte está registrado

```bash
# Verificar el reporte en la base de datos:
SELECT name, model, report_type FROM ir_actions_report WHERE report_name LIKE '%invoice_pdf_report%';
```

## Pruebas Funcionales

### Prueba 1: Verificar el Botón en la Vista de Factura

1. Ir a: **Contabilidad > Clientes > Facturas**
2. Abrir una factura existente o crear una nueva
3. Verificar que aparece el botón **"Imprimir Reporte PDF"** en el header
4. El botón debe estar visible incluso si la factura no está pagada

### Prueba 2: Generar PDF de Factura No Pagada

1. Crear una nueva factura:
   - Cliente: Seleccionar cualquier cliente
   - Líneas de factura: Agregar al menos un producto/servicio
   - **No confirmar el pago**
2. Guardar la factura
3. Click en "Imprimir Reporte PDF"
4. Verificar que el PDF se descarga correctamente
5. Abrir el PDF y verificar:
   - Logo de la empresa (si está configurado)
   - Información del cliente completa
   - Número y fechas de la factura
   - Líneas de productos/servicios
   - Total correcto
   - Texto: "Reconozco haber recibido esta factura..."

### Prueba 3: Generar PDF de Factura Pagada

1. Tomar una factura existente
2. Registrar el pago completo
3. Click en "Imprimir Reporte PDF"
4. Verificar el PDF:
   - Estado debe mostrar "Pagado" en verde
   - Texto debe decir: "He pagado la cantidad total de..."

### Prueba 4: Generar PDF de Factura con Pago Parcial

1. Crear una factura
2. Registrar un pago parcial
3. Click en "Imprimir Reporte PDF"
4. Verificar el PDF:
   - Estado debe mostrar "Pago Parcial" en naranja
   - Texto debe mostrar el importe pendiente

### Prueba 5: Verificar Formato y Estilos

1. Generar cualquier PDF
2. Verificar elementos de diseño:
   - Header con borde inferior
   - Logo centrado (si existe)
   - Cajas de información con borde y fondo gris claro
   - Tabla de líneas con encabezado oscuro
   - Totales alineados a la derecha
   - Texto de pago con borde izquierdo y fondo gris

## Casos de Prueba Adicionales

### Caso 1: Factura sin Fecha de Vencimiento
- Crear factura sin fecha de vencimiento
- Verificar que muestra "Sin fecha de vencimiento"

### Caso 2: Cliente sin Dirección Completa
- Crear factura para cliente con información incompleta
- Verificar que solo muestra los campos disponibles

### Caso 3: Factura con Múltiples Líneas
- Crear factura con 10+ líneas de productos
- Verificar que todas las líneas se muestran correctamente
- Verificar paginación si es necesario

### Caso 4: Factura con Diferentes Monedas
- Crear factura en USD, EUR, etc.
- Verificar que el símbolo de moneda se muestra correctamente

## Solución de Problemas

### Error: Módulo no aparece en la lista
- Verificar que la carpeta está en el directorio de addons
- Verificar permisos de lectura de los archivos
- Reiniciar el servidor de Odoo
- Actualizar lista de aplicaciones

### Error: Botón no aparece en la vista
- Verificar que el módulo está instalado
- Limpiar caché del navegador
- Actualizar la vista (F5)
- Verificar en modo desarrollador: Vista > Editar FieldView

### Error: PDF no se genera
- Verificar logs de Odoo: `tail -f /var/log/odoo/odoo-server.log`
- Verificar que wkhtmltopdf está instalado
- Verificar permisos de escritura en carpeta temporal

### Error: Faltan datos en el PDF
- Verificar que la factura tiene todos los campos requeridos
- Verificar que el cliente tiene información completa
- Revisar logs para errores específicos

## Testing Automatizado

Si tienes un entorno de testing configurado, puedes ejecutar:

```python
# Test básico de generación de reporte
from odoo.tests import TransactionCase

class TestInvoiceReport(TransactionCase):
    def test_generate_report(self):
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.env.ref('base.res_partner_1').id,
            'invoice_line_ids': [(0, 0, {
                'name': 'Test Product',
                'quantity': 1,
                'price_unit': 100,
            })],
        })
        invoice.action_post()
        
        report = self.env.ref('invoice_pdf_report.action_report_invoice_pdf')
        pdf = report._render_qweb_pdf([invoice.id])
        self.assertTrue(pdf, "El PDF debe generarse correctamente")
```

## Desinstalación

1. Ir a: Aplicaciones
2. Buscar "Invoice PDF Report"
3. Click en Desinstalar
4. Confirmar la desinstalación
5. Opcionalmente, eliminar la carpeta del módulo de addons

## Soporte

Para reportar problemas o sugerencias:
- Crear un issue en el repositorio
- Contactar a Toni Sistemas
