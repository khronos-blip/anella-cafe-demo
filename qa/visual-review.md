# Revisión visual final — Anella Café

Fecha: 2026-09-14

## Material inspeccionado

- `qa/product-contact-sheet.jpg` y las 6 imágenes individuales de `assets/generated/*.jpg`.
- 10 capturas finales: home, catálogo, detalle, carrito y confirmación en 1440×1000 y 390×844.
- Contact sheet final: `qa/final-contact-sheet.jpg`.

## Resultado

**PASS.** La demo se percibe como storefront móvil específico de Anella y no como landing genérica. La paleta rosa arcilla, crema, verde petróleo y carbón es consistente; la serif editorial domina, el script se limita a acentos, y la botánica lineal aparece como motivo secundario sin competir con el catálogo.

## Hallazgos verificados

- El primer viewport muestra la barra de demo, marca, búsqueda, carrito, hero compacto, filtros y el inicio del primer producto tanto en desktop como en mobile.
- La composición conserva jerarquía y legibilidad desde 320×568 hasta 430×932, y en 844×390 horizontal; las áreas seguras, el texto del hero y los filtros desplazables no generan overflow.
- El conteo de resultados acompaña la búsqueda y los filtros sin competir con el titular; el filtro activo conserva una señal visual clara en ambos viewports.
- Las 6 imágenes son distintas, luminosas, legibles y coherentes con cada nombre/descripción. Los encuadres conservan el postre completo en cards y detalle, sin cortes críticos.
- Las cards móviles tienen jerarquía clara: categoría, nombre, descripción, precio y acción. En desktop, la retícula de tres columnas mantiene ritmo editorial y densidad comercial.
- El modal de detalle se lee completo en ambos viewports; imagen, cantidad y CTA quedan visibles, con overlay uniforme.
- El drawer muestra 2 productos distintos, controles de cantidad y subtotal de **16,00 €** sin solapes.
- La confirmación muestra el estado correcto y el subtotal revisado en desktop y mobile; no quedan overlays fantasma.
- El detalle, carrito y confirmación contienen el foco mientras están abiertos, dejan el fondo inerte y devuelven el foco al control de origen al cerrar con Escape.
- Los campos permanecen en 16 px para evitar zoom involuntario en iOS y los controles principales conservan objetivos táctiles de al menos 44 px en dispositivos touch.
- No se observan desbordamientos horizontales, texto cortado, controles fuera del viewport, imágenes rotas ni contraste problemático.
- La sección inferior de identidad diferencia visualmente la propuesta sin desplazar el comercio del primer plano.

## Nota de procedencia visual

Las fotografías se presentan de forma visible como **“Imagen ilustrativa”** y la página aclara: **“Imágenes ilustrativas generadas para esta propuesta. No son fotografías oficiales de Anella Café.”**
