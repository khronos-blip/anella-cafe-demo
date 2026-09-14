# Anella Café — Demo storefront

Storefront responsive y autocontenido creado como **propuesta visual no oficial** para Anella Café Valencia. Presenta una selección verificada de seis postres y permite recorrer un pedido completamente simulado sin enviar datos, procesar pagos ni conectarse con el negocio.

> **Página web demo · Sitio no oficial · Pedido simulado**

- Demo pública: https://khronos-blip.github.io/anella-cafe-demo/
- Repositorio: https://github.com/khronos-blip/anella-cafe-demo

## Qué incluye

- Catálogo de 6 productos con nombre, descripción y precio verificados.
- Búsqueda y filtros por categoría con conteo de resultados y recuperación del estado vacío.
- Modal de detalle y selector de cantidad.
- Carrito persistente mediante `localStorage`.
- Flujo simulado de pickup o delivery.
- Dirección obligatoria para delivery y aceptación explícita de la simulación.
- Vista previa y confirmación sin transmisión de información.
- Diseño responsive validado en desktop y móvil.
- PDF oficial preservado localmente como referencia.
- Imágenes generadas, distintas por producto y marcadas como ilustrativas.
- Navegación accesible por teclado, foco contenido en overlays y retorno al control de origen.
- Cero dependencias de frontend, trackers o requests a terceros.

## Arquitectura

La demo es deliberadamente simple y portable:

- `index.html`: fuente editable principal; contiene HTML, CSS y JavaScript inline.
- `assets/generated/`: imágenes ilustrativas del catálogo.
- `dist/`: paquete estático autocontenido listo para servir.
- `sources/`: fuentes, extracción y registro de hechos verificados.
- `qa/`: validaciones estructurales, pruebas funcionales y evidencia visual.
- `menu-oficial.pdf`: copia local del menú enlazada desde la interfaz.
- `favicon.svg` y `robots.txt`: identidad local y bloqueo de indexación.

No hay framework, backend, API, checkout real ni proceso de build obligatorio.

## Ejecutar localmente

Desde la raíz del proyecto:

```bash
python3 -m http.server 4173 --directory dist
```

Abrir después:

```text
http://127.0.0.1:4173
```

También puede servirse la raíz para revisar `index.html`, pero `dist/` es el artefacto de entrega.

## Fuente de verdad

Los datos comerciales y las decisiones de procedencia están documentados en:

- `sources/verified-sources.md`
- `sources/anella-valencia-menu.pdf`
- `menu-oficial.pdf`

No se deben añadir, completar ni “mejorar” productos, ingredientes, precios, disponibilidad, ubicaciones o condiciones comerciales sin una nueva fuente oficial verificable.

Las imágenes de producto **no son fotografías oficiales de Anella Café**. La atribución visible debe conservarse.

## QA

La entrega actual fue aprobada con:

- 13 comprobaciones estructurales.
- 69 gates funcionales.
- 10 capturas en `1440×1000` y `390×844`.
- 0 errores de consola o página.
- 0 requests fallidas u off-origin.
- 0 overflow horizontal en los estados comprobados.

Con un servidor local activo en el puerto 4173:

```bash
python3 qa/structural-check.py
node --check qa/inline-script.js
node --check qa/run-qa.js
QA_URL=http://127.0.0.1:4173 node qa/run-qa.js
```

Los scripts funcionales requieren Playwright disponible en el entorno. Los resultados quedan en:

- `qa/structural-report.json`
- `qa/qa-report.json`
- `qa/visual-review.md`
- `qa/final-contact-sheet.jpg`
- `qa/screenshots/`

## Flujo de edición

1. Consultar `CODEX_BRIEF.md` antes de modificar catálogo, copy, visuales o comportamiento.
2. Editar `index.html` y los assets fuente necesarios.
3. Sincronizar el paquete `dist/` sin introducir recursos remotos.
4. Ejecutar la suite estructural y funcional completa.
5. Inspeccionar visualmente home, catálogo, detalle, carrito y confirmación en ambos viewports.
6. No publicar ni conectar canales reales desde este repositorio sin autorización separada.

## Estado

Demo estática terminada y verificada el **2026-09-14**. No está afiliada, aprobada ni operada por Anella Café.
