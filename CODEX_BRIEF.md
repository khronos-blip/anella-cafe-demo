# CODEX BRIEF — Anella Café demo

## 1. Objetivo y contrato de edición

Mantén una demo storefront estática, premium, responsive y explícitamente no oficial para Anella Café Valencia. La experiencia debe permitir descubrir seis postres, revisar un carrito y completar una simulación local sin enviar datos ni ejecutar compras.

Antes de editar, inspecciona `sources/verified-sources.md`, `index.html`, este documento y los checks aplicables de `qa/`. No sustituyas hechos verificados por inferencias ni copy creativo.

## 2. Arquitectura actual

- **Fuente editable:** `index.html`.
- **Implementación:** un único documento con HTML semántico, CSS y JavaScript inline.
- **Estado:** objeto de carrito persistido en `localStorage` con clave `anella-demo-cart-v1`.
- **Recursos:** imágenes JPG locales en `assets/generated/`, favicon SVG local y PDF local.
- **Entrega:** `dist/` es un espejo autocontenido de los archivos públicos.
- **Repositorio:** `https://github.com/khronos-blip/anella-cafe-demo`.
- **Demo pública:** `https://khronos-blip.github.io/anella-cafe-demo/`, publicada desde `main` y la raíz del repositorio mediante GitHub Pages.
- **QA estructural:** `qa/structural-check.py` valida `dist/index.html`, catálogo, recursos, disclosures y ausencia de dependencias externas.
- **QA funcional:** `qa/run-qa.js` usa Playwright contra `QA_URL` y cubre desktop y móvil.
- **Backend/integraciones:** ninguno. No hay framework, API, analytics, pagos, formularios remotos, WhatsApp, `fetch` ni XHR.

El sitio debe seguir funcionando como contenido estático servido por HTTP. No introduzcas una toolchain o dependencia si el cambio puede resolverse dentro de la arquitectura actual.

## 3. Fuente de verdad y precedencia

1. `sources/anella-valencia-menu.pdf` y `menu-oficial.pdf`: evidencia local preservada del menú oficial.
2. `sources/verified-sources.md`: selección verificada y transcripción exacta usada por la demo.
3. `index.html`: implementación fuente, que debe coincidir con los hechos anteriores.
4. `dist/`: artefacto público; nunca debe convertirse en una variante independiente.

Si una petición contradice las fuentes o requiere un dato no demostrado, detén solo esa parte y solicita una fuente oficial o una decisión explícita. No uses las imágenes generadas para inferir ingredientes, tamaños o disponibilidad.

## 4. Catálogo inmutable sin nueva evidencia

Conserva exactamente estos seis productos:

| ID | Nombre | Descripción | Precio | Categoría interna |
|---|---|---|---:|---|
| `torta-pistacho` | Torta de Pistacho | Ponqué de textura suave con una cubierta de chocolate blanco y pistacho. | 8 € | `saludables` |
| `ponque-chocolate` | Ponqué Chocolate Anella | Ponqué con textura suave doble capa, cubierto con chocolate y almendra. | 8 € | `saludables` |
| `torta-zanahoria` | Torta Zanahoria | Ponqué con textura húmeda cubierta de yogurt griego con nueces. | 8 € | `saludables` |
| `pie-pistacho` | Pie de Pistacho | Base de galleta con una capa de crema de pistacho con mousse de chocolate. | 8 € | `frias` |
| `cheesecake-frutos-rojos` | Cheesecake de Frutos Rojos | Base de avena con queso crema con una capa de frutos rojos. | 7 € | `frias` |
| `brownie` | Brownie | Torta cremosa de textura húmeda cubierta de chocolate y almendras picadas. | 8 € | `saludables` |

Reglas:

- No añadas productos, variantes, tamaños, promociones, stock, alérgenos ni disponibilidad.
- No cambies nombres, puntuación, ingredientes descriptivos o precios por estilo.
- Conserva una imagen local única por producto.
- Conserva `Imagen ilustrativa` en cada card y el disclosure global exacto: `Imágenes ilustrativas generadas para esta propuesta. No son fotografías oficiales de Anella Café.`
- No presentes imágenes generadas como material oficial.

## 5. Decisiones visuales que deben sobrevivir

- Paleta base: rosa arcilla `#B97F74`, crema `#F1E2D7`, verde petróleo `#174E58` y carbón `#2D3433`.
- Marca tipográfica: `anella` en serif editorial fina y `Café` como acento caligráfico ligero.
- Jerarquía: serif para titulares/producto, sans para interfaz; script solo como acento.
- Motivo secundario: botánica lineal, discreta y no competitiva.
- Tono: femenino, saludable, delicado, artesanal y contemporáneo.
- La página debe sentirse como storefront de producto, no como landing genérica.
- El primer viewport debe conservar barra de demo, marca, búsqueda, carrito, hero compacto, filtros e inicio visible del catálogo.
- Desktop: retícula de tres columnas. Móvil: cards verticales compactas y controles táctiles claros.
- Overlays: modal de detalle, drawer de carrito y confirmación sin solapes, fondos fantasma ni contenido crítico fuera del viewport.
- Respeta `prefers-reduced-motion` y evita overflow horizontal.

## 6. Comportamiento y privacidad

Conserva estos flujos:

1. Buscar por nombre o descripción.
2. Filtrar entre todos, tortas saludables y tortas frías.
3. Abrir detalle, elegir cantidad y añadir al carrito.
4. Ajustar cantidades y ver subtotal en EUR con formato `es-ES`.
5. Persistir el carrito tras recarga.
6. Elegir pickup o delivery.
7. Exigir dirección solo en delivery.
8. Exigir aceptación explícita de que es una simulación.
9. Mostrar vista previa local.
10. Confirmar localmente, vaciar el carrito y mostrar el subtotal revisado.

Restricciones obligatorias:

- No transmitir nombre, dirección, notas, carrito o analítica.
- No conectar WhatsApp, email, teléfono, formularios, APIs, pagos o pedidos reales.
- No cargar CDN, fuentes, scripts, píxeles o imágenes remotas.
- Conserva visibles `Página web demo · Sitio no oficial · Pedido simulado` y los avisos de no envío.
- Conserva `noindex,nofollow,noarchive,nosnippet` y `robots.txt` con `Disallow: /`.

## 7. Checklist antes de editar

- [ ] Leer `sources/verified-sources.md` y localizar el hecho que respalda el cambio.
- [ ] Confirmar si el cambio afecta catálogo, copy verificado, privacidad o disclosures.
- [ ] Revisar la sección correspondiente de `index.html` y el check que la protege.
- [ ] Mantener rutas relativas válidas desde raíz y `dist/`.
- [ ] Evitar dependencias e integraciones externas.
- [ ] Definir cómo se comprobará el cambio en desktop y móvil.

## 8. Checklist de implementación

- [ ] Editar primero `index.html`.
- [ ] Mantener HTML semántico, labels, nombres accesibles y cierre por Escape.
- [ ] Escapar cualquier texto dinámico que pueda entrar en HTML.
- [ ] Mantener precios numéricos en los datos y formatearlos con `Intl.NumberFormat`.
- [ ] Mantener una imagen por producto y actualizar alt/disclosures si cambia un asset autorizado.
- [ ] Sincronizar en `dist/` únicamente archivos públicos: `index.html`, `favicon.svg`, `robots.txt`, `menu-oficial.pdf` y `assets/`.
- [ ] No copiar `sources/`, briefs o artefactos de QA dentro de `dist/`.

## 9. Checklist de QA y comandos

Desde la raíz del proyecto, sincroniza el artefacto público y sirve `dist/`. Después ejecuta:

```bash
python3 qa/structural-check.py
node --check qa/inline-script.js
node --check qa/run-qa.js
QA_URL=http://127.0.0.1:4173 node qa/run-qa.js
QA_URL=http://127.0.0.1:4173 node qa/mobile-compatibility.js
```

El servidor puede levantarse en otra terminal con:

```bash
python3 -m http.server 4173 --directory dist
```

Aceptación mínima:

- [ ] `qa/structural-report.json` termina en `status: pass` y sin checks fallidos.
- [ ] `qa/qa-report.json` termina en `status: pass` y `failedGates` vacío.
- [ ] Siguen existiendo exactamente 6 productos y 6 imágenes únicas.
- [ ] Búsqueda y los tres filtros funcionan.
- [ ] El carrito contiene dos productos distintos y suma 16,00 € en el escenario de prueba.
- [ ] El carrito persiste tras recarga.
- [ ] La aceptación de simulación bloquea el avance cuando falta.
- [ ] Delivery bloquea sin dirección y avanza con dirección.
- [ ] Vista previa y confirmación conservan el subtotal.
- [ ] Hay 0 errores de consola, página, requests fallidas y requests off-origin.
- [ ] No hay overflow horizontal en `1440×1000` ni `390×844`.
- [ ] La matriz móvil pasa en 320, 360, 375, 390, 412 y 430 px, además de orientación horizontal.
- [ ] Inspeccionar home, catálogo, detalle, carrito y confirmación en ambos viewports.
- [ ] Revisar encuadres, legibilidad, overlays, estados vacíos y controles táctiles.

Si una transición produce una captura del estado anterior, espera a que terminen las animaciones del overlay/panel antes de tomar evidencia; no maquilles la captura ni desactives el gate.

## 10. Cierre de una edición

- Resume archivos cambiados y motivo.
- Distingue fuente editada, `dist/` sincronizado, QA automatizado y revisión visual.
- Informa cualquier gate no ejecutado o bloqueo; no declares PASS por inspección parcial.
- No publiques, conectes dominios ni actives integraciones desde este proyecto sin autorización externa específica.
