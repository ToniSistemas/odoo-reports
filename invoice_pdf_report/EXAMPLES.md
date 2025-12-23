# Ejemplos de Uso - Invoice PDF Report

## Ejemplo 1: Factura Simple

### Datos de entrada:
```
Cliente: Juan Pérez
Dirección: Calle Principal 123
Ciudad: Madrid, 28001
País: España

Factura: INV/2024/0001
Fecha Emisión: 15/01/2024
Fecha Vencimiento: 15/02/2024

Línea 1:
  - Descripción: Servicio de Consultoría
  - Cantidad: 10 horas
  - Precio Unitario: 50.00 €
  - Subtotal: 500.00 €

Impuestos (21%): 105.00 €
Total: 605.00 €

Estado: No Pagado
```

### Resultado esperado en PDF:
- Header con logo de empresa
- Información de cliente en caja izquierda
- Información de factura en caja derecha
- Tabla con línea de servicio
- Total destacado: 605.00 €
- Texto: "Reconozco haber recibido esta factura por un importe de 605.00 €..."

---

## Ejemplo 2: Factura con Múltiples Productos

### Datos de entrada:
```
Cliente: Empresa ABC S.L.
Dirección: Av. de la Constitución 45, Oficina 3B
Ciudad: Barcelona, 08001, Cataluña
País: España

Factura: INV/2024/0002
Fecha Emisión: 20/01/2024
Fecha Vencimiento: 20/03/2024

Línea 1:
  - Descripción: Laptop HP ProBook
  - Cantidad: 2
  - Precio Unitario: 800.00 €
  - Subtotal: 1,600.00 €

Línea 2:
  - Descripción: Monitor Dell 24"
  - Cantidad: 2
  - Precio Unitario: 200.00 €
  - Subtotal: 400.00 €

Línea 3:
  - Descripción: Teclado y Mouse Logitech
  - Cantidad: 2
  - Precio Unitario: 50.00 €
  - Subtotal: 100.00 €

Subtotal: 2,100.00 €
Impuestos (21%): 441.00 €
Total: 2,541.00 €

Estado: Pagado
```

### Resultado esperado en PDF:
- Tres líneas de productos mostradas en tabla
- Total destacado: 2,541.00 €
- Estado "Pagado" en verde
- Texto: "He pagado la cantidad total de 2,541.00 € correspondiente a esta factura."

---

## Ejemplo 3: Factura con Pago Parcial

### Datos de entrada:
```
Cliente: Restaurante El Buen Sabor
Dirección: Plaza Mayor 8
Ciudad: Sevilla, 41001
País: España

Factura: INV/2024/0003
Fecha Emisión: 25/01/2024
Fecha Vencimiento: 10/02/2024

Línea 1:
  - Descripción: Sistema POS Completo
  - Cantidad: 1
  - Precio Unitario: 2,000.00 €
  - Subtotal: 2,000.00 €

Línea 2:
  - Descripción: Instalación y Configuración
  - Cantidad: 1
  - Precio Unitario: 500.00 €
  - Subtotal: 500.00 €

Subtotal: 2,500.00 €
Impuestos (21%): 525.00 €
Total: 3,025.00 €

Pagado: 1,500.00 €
Pendiente: 1,525.00 €

Estado: Pago Parcial
```

### Resultado esperado en PDF:
- Total: 3,025.00 €
- Estado "Pago Parcial" en naranja
- Texto: "He pagado parcialmente esta factura. Importe pendiente: 1,525.00 €"

---

## Ejemplo 4: Factura Internacional (USD)

### Datos de entrada:
```
Cliente: Tech Solutions Inc.
Dirección: 123 Main Street, Suite 456
Ciudad: New York, NY 10001
País: Estados Unidos

Factura: INV/2024/0004
Fecha Emisión: 01/02/2024
Fecha Vencimiento: 01/03/2024

Línea 1:
  - Descripción: Software Development - 40 hours
  - Cantidad: 40
  - Precio Unitario: 75.00 $
  - Subtotal: 3,000.00 $

Línea 2:
  - Descripción: Project Management - 10 hours
  - Cantidad: 10
  - Precio Unitario: 100.00 $
  - Subtotal: 1,000.00 $

Subtotal: 4,000.00 $
Impuestos: 0.00 $ (Servicio internacional)
Total: 4,000.00 $

Estado: No Pagado
```

### Resultado esperado en PDF:
- Dirección completa de USA
- Montos mostrados en USD ($)
- Impuestos en 0.00 $
- Total: 4,000.00 $

---

## Ejemplo 5: Factura con Cliente Mínimo

### Datos de entrada:
```
Cliente: María García
(Sin dirección registrada)
(Sin ciudad registrada)

Factura: INV/2024/0005
Fecha Emisión: 05/02/2024
(Sin fecha vencimiento)

Línea 1:
  - Descripción: Servicio de Diseño Gráfico
  - Cantidad: 1
  - Precio Unitario: 300.00 €
  - Subtotal: 300.00 €

Subtotal: 300.00 €
Impuestos (21%): 63.00 €
Total: 363.00 €

Estado: No Pagado
```

### Resultado esperado en PDF:
- Solo nombre de cliente visible
- Campos de dirección vacíos u ocultos
- "Sin fecha de vencimiento" en lugar de fecha
- Total: 363.00 €
- Reporte generado sin errores

---

## Escenarios de Testing Recomendados

### Test 1: Generación masiva
- Crear 10 facturas diferentes
- Generar PDF de todas simultáneamente
- Verificar que todas se generan correctamente

### Test 2: Diferentes idiomas
- Cambiar idioma de usuario a inglés
- Generar PDF
- Verificar que etiquetas están traducidas

### Test 3: Facturas de crédito (Refund)
- Crear una nota de crédito
- Generar PDF
- Verificar que se muestra correctamente con valores negativos

### Test 4: Performance
- Crear factura con 100 líneas
- Medir tiempo de generación
- Verificar paginación correcta

### Test 5: Sin logo
- Empresa sin logo configurado
- Generar PDF
- Verificar que no hay errores y diseño se adapta

---

## Notas Adicionales

### Formato de Fechas
El formato por defecto es DD/MM/YYYY (europeo). Para cambiar:
- Modificar en el template: `strftime('%m/%d/%Y')` para formato americano

### Decimales
Por defecto se muestran 2 decimales. Para cambiar:
- Modificar formato en template: `'%.3f'` para 3 decimales

### Moneda
El símbolo de moneda se toma automáticamente de `o.currency_id.symbol`

### Campos Personalizados
Si agregas campos personalizados a facturas:
1. Agregar campo en el modelo
2. Modificar template QWeb para mostrarlo
3. Actualizar módulo
