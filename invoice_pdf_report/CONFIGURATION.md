# Ejemplo de Configuración de Odoo para Invoice PDF Report

## Configuración del archivo odoo.conf

```ini
[options]
# Agregar la ruta donde está el módulo
addons_path = /path/to/odoo/addons,/path/to/custom/addons,/path/to/odoo-reports

# Configuración de reportes PDF
# Asegurar que wkhtmltopdf esté instalado y configurado
report_url = http://localhost:8069

# Otras configuraciones recomendadas para reportes
workers = 2
max_cron_threads = 1
```

## Instalación de wkhtmltopdf (Requerido para PDF)

### Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install wkhtmltopdf
```

### CentOS/RHEL:
```bash
sudo yum install wkhtmltopdf
```

### macOS:
```bash
brew install wkhtmltopdf
```

## Verificar instalación de wkhtmltopdf

```bash
wkhtmltopdf --version
```

Debe mostrar la versión instalada.

## Configuración de Logo de Empresa

Para que el logo aparezca en el reporte:

1. Ir a: **Ajustes > Usuarios & Compañías > Compañías**
2. Seleccionar la compañía
3. En el campo "Logo", subir la imagen del logo
4. Guardar

Formatos recomendados:
- PNG con fondo transparente
- JPG/JPEG
- Tamaño recomendado: 200x100 px
- Tamaño máximo: 1024x1024 px

## Configuración de Información de Compañía

Completar los siguientes campos para que aparezcan en el reporte:

1. **Nombre de la Compañía**: Se muestra en el header
2. **Dirección**: Aparece en el pie de página
3. **Teléfono**: Información de contacto
4. **Email**: Información de contacto
5. **Website**: Información adicional

## Configuración de Información de Clientes

Para que el reporte muestre información completa, asegurar que los clientes tengan:

1. **Nombre** (obligatorio)
2. **Dirección**: Calle, Calle 2
3. **Ciudad**: Localidad
4. **Estado/Provincia**: Estado
5. **Código Postal**: ZIP
6. **País**: País

## Permisos de Usuario

Los siguientes permisos son necesarios para usar el módulo:

- **account.group_account_invoice**: Para acceder a facturas
- **account.group_account_user**: Para crear y modificar facturas

## Configuración de Seguridad (Opcional)

Si quieres restringir quién puede imprimir el reporte:

1. Crear un grupo de seguridad personalizado
2. Modificar el archivo de seguridad (crear `security/ir.model.access.csv`)
3. Asignar permisos específicos

Ejemplo:
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_invoice_pdf_report,access_invoice_pdf_report,model_account_move,base.group_user,1,0,0,0
```

## Personalización del Reporte

Para personalizar colores, fuentes y estilos:

1. Editar el archivo: `reports/invoice_report.xml`
2. Modificar la sección `<style>` dentro del template
3. Actualizar el módulo en Odoo

Ejemplo de personalización de colores:

```css
.invoice-title {
    color: #0066cc;  /* Cambiar color del título */
}

.details-table th {
    background-color: #0066cc;  /* Cambiar color del header de tabla */
}
```

## Traducción del Módulo

Para agregar traducción a otros idiomas:

1. Activar modo desarrollador
2. Ir a: Ajustes > Traducir > Términos de traducción
3. Buscar términos del módulo `invoice_pdf_report`
4. Agregar traducciones

O usar el comando:

```bash
./odoo-bin -d nombre_bd --i18n-export=invoice_pdf_report.pot -l es_ES
# Editar el archivo .pot
./odoo-bin -d nombre_bd --i18n-import=invoice_pdf_report.po -l en_US
```

## Backup del Módulo

Recomendaciones:

1. Mantener copia del módulo en control de versiones (Git)
2. Hacer backup de la base de datos regularmente
3. Documentar personalizaciones realizadas

## Actualización del Módulo

Para actualizar el módulo después de cambios:

1. Modificar archivos necesarios
2. Incrementar versión en `__manifest__.py`
3. Reiniciar Odoo
4. Ir a: Aplicaciones > buscar el módulo > Actualizar

O usar el comando:

```bash
./odoo-bin -d nombre_bd -u invoice_pdf_report
```

## Variables de Entorno Recomendadas

```bash
# Para producción
export ODOO_RC=/etc/odoo/odoo.conf
export ODOO_DATABASE=production_db

# Para desarrollo
export ODOO_RC=/path/to/dev/odoo.conf
export ODOO_DATABASE=dev_db
```

## Logging

Para depurar problemas con el reporte:

```ini
[options]
log_level = debug
log_handler = :DEBUG,werkzeug:WARNING,odoo.addons.invoice_pdf_report:DEBUG
```

## Performance

Para mejorar el rendimiento de generación de PDF:

1. Usar workers en producción
2. Configurar límites de memoria adecuados
3. Optimizar imágenes (logo) para web
4. Limitar el número de líneas por página si es necesario
