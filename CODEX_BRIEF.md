# Brief operativo para Codex — Anella Café

## Objetivo

Editar y elevar esta demo storefront sin romper su exactitud, trazabilidad ni simulación segura. Debe sentirse como una boutique digital de postres saludables específica de Anella: delicada, editorial, comercial y móvil primero; nunca como una landing genérica.

## Fuente de verdad

Lee antes de modificar:

1. `sources/verified-sources.md`
2. `index.html`
3. `qa/structural-report.json`
4. `qa/qa-report.json`
5. `qa/visual-review.md`
6. `qa/final-contact-sheet.jpg`

El menú oficial preservado es `menu-oficial.pdf`. No inventes productos, ingredientes, precios, ubicaciones, disponibilidad, servicio de entrega, reservas, horarios ni claims médicos.

## Contrato de contenido

Mantén exactamente estos seis productos salvo instrucción explícita y nueva evidencia oficial:

- Torta de Pistacho — 8 €
- Ponqué Chocolate Anella — 8 €
- Torta Zanahoria — 8 €
- Pie de Pistacho — 8 €
- Cheesecake de Frutos Rojos — 7 €
- Brownie — 8 €

Conserva las descripciones exactas de `sources/verified-sources.md`. Cada producto usa su archivo homónimo de `assets/`. Mantén visible la nota: “Imágenes ilustrativas generadas para esta propuesta. No son fotografías oficiales de Anella Café.”

## Dirección visual

- Rosa arcilla `#B97F74`, crema cálido `#F1E2D7`, verde petróleo `#174E58`, carbón suave `#2D3433`.
- Serif editorial fina como voz principal; script solo como acento.
- Ilustración botánica lineal discreta, composición aireada y fotografía luminosa.
- Producto visible en el primer viewport; cards densas y comerciales, no bloques enormes de marketing.
- Mantén detalle, carrito y confirmación como estados visualmente pulidos tanto en desktop como en 390px.

## Reglas funcionales

- Todo permanece estático y local: sin CDN, frameworks, fuentes externas, analytics, `fetch`, XHR ni requests off-origin.
- El carrito persiste en `localStorage` y calcula subtotales reales.
- Pickup y delivery son simulados; delivery exige dirección.
- Exige aceptar la simulación antes de mostrar la vista previa.
- Confirmar no abre WhatsApp, no transmite datos y no ejecuta operaciones externas.
- Conserva `noindex`, el aviso superior de demo, accesibilidad por teclado, `Escape`, foco razonable, alt text y `prefers-reduced-motion`.
- No conviertas el sitio en oficial ni retires los disclosures sin autorización expresa.

## Estructura de publicación

- Fuente editable/publicada: raíz del repositorio.
- Espejo autocontenido: `dist/`.
- Tras editar, sincroniza en `dist/` únicamente: `index.html`, `assets/`, `favicon.svg`, `robots.txt`, `menu-oficial.pdf`.
- El sublink objetivo es `https://gvisoweb.khronosonline.work/demos/anella/`.

## Gate obligatorio antes de entregar

1. `python3 qa/structural-check.py`
2. Extrae de nuevo el script inline a `qa/inline-script.js` si cambió `index.html` y ejecuta `node --check qa/inline-script.js`.
3. `node qa/run-qa.js`
4. Verifica 6 productos, 6 imágenes únicas existentes, cero recursos externos, cero errores de consola/página/request y cero overflow en 1440×1000 y 390×844.
5. Regenera las 10 capturas y `qa/final-contact-sheet.jpg`.
6. Inspecciona visualmente home, catálogo, detalle, carrito y confirmación en desktop y mobile. Corrige antes de declarar PASS.
7. Actualiza `qa/visual-review.md`, `qa/qa-report.json` y `qa/structural-report.json`.

## Definición de terminado

No basta que el HTML cargue. Terminado significa: contenido exacto, flujos simulados completos, apariencia premium específica de Anella, responsive comprobado, reportes PASS, capturas inspeccionadas, raíz y `dist/` sincronizados, commit claro y demo pública verificada por navegación real.
