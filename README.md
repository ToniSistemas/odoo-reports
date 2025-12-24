# Odoo Reports

Repositorio de módulos de reportes personalizados para Odoo.

## Módulos Disponibles

### Comprobante de Pago

**Versión:** 18.0.1.0.0  
**Estado:** ✅ Listo para producción

Módulo que permite generar comprobantes de pago en formato PDF desde facturas de Odoo 18.0, independientemente del estado de pago.

#### Características Principales

- ✅ Generación de PDF profesional con comprobante de pago
- ✅ Funciona con facturas pagadas y no pagadas
- ✅ Incluye logo de la empresa
- ✅ Información completa del cliente y factura
- ✅ Diseño profesional y personalizable
- ✅ Botón integrado en el formulario de factura
- ✅ Compatible con Odoo 18.0

#### Instalación Rápida

```bash
# Copiar el módulo al directorio de addons
cp -r payment_receipt_report /ruta/a/odoo/addons/

# Instalar mediante CLI
./odoo-bin -c /etc/odoo/odoo.conf -d tu_base_de_datos -i payment_receipt_report
```

#### Documentación

- [README completo](payment_receipt_report/README.rst)
- [Guía de instalación](payment_receipt_report/INSTALL.md)
- [Changelog](payment_receipt_report/CHANGELOG.md)

#### Uso

1. Abrir cualquier factura de cliente en Odoo
2. Hacer clic en el botón "Imprimir Comprobante de Pago"
3. El PDF se generará automáticamente

## Requisitos

- Odoo 18.0
- Python 3.8+
- wkhtmltopdf (para generación de PDFs)

## Soporte

Para reportar problemas o solicitar nuevas funcionalidades:

- **Issues:** https://github.com/ToniSistemas/odoo-reports/issues
- **Pull Requests:** ¡Las contribuciones son bienvenidas!

## Licencia

Todos los módulos en este repositorio están licenciados bajo LGPL-3, a menos que se especifique lo contrario.

## Autor

**ToniSistemas**  
https://github.com/ToniSistemas

---

## Próximos Módulos Planeados

- [ ] Reportes de inventario personalizados
- [ ] Reportes de ventas avanzados
- [ ] Reportes de producción
- [ ] Más formatos de comprobantes

¿Tienes una idea para un nuevo reporte? ¡Abre un issue!
