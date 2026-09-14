# Anella Café · storefront demo

Demo no oficial de una tienda web para Anella Café Valencia, construida a partir del menú público enlazado desde `@anellacafe_`.

## Demo pública

`https://gvisoweb.khronosonline.work/demos/anella/`

## Editar con Codex

Abre este repositorio en Codex y usa `CODEX_BRIEF.md` como fuente de verdad. El sitio público se sirve desde la raíz (`index.html`, `assets/`, `menu-oficial.pdf`, `favicon.svg`, `robots.txt`). `dist/` es una copia autocontenida de publicación.

## Vista local

```bash
python3 -m http.server 8080
```

Abre `http://127.0.0.1:8080/`.

## QA

```bash
python3 qa/structural-check.py
node --check qa/inline-script.js
node qa/run-qa.js
```

Último resultado verificado: **51/51 gates funcionales PASS**, 6 productos exactos, 6 imágenes únicas, cero dependencias externas, cero requests fuera de origen, cero errores de consola/página y cero overflow horizontal en 1440×1000 y 390×844.

## Límites de la propuesta

- Sitio no oficial y no indexable.
- Pedidos completamente simulados; no envía información ni abre WhatsApp.
- Precios, nombres y descripciones provienen del menú oficial preservado.
- Fotografías de producto generadas para esta propuesta y señaladas como ilustrativas; no son fotografías oficiales de Anella Café.
