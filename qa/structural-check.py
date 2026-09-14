from html.parser import HTMLParser
from pathlib import Path
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
html=(DIST/'index.html').read_text(encoding='utf-8')
class StrictishParser(HTMLParser):
    void={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
    def __init__(self): super().__init__(convert_charrefs=True); self.stack=[]; self.errors=[]
    def handle_starttag(self,tag,attrs):
        if tag not in self.void: self.stack.append(tag)
    def handle_startendtag(self,tag,attrs): pass
    def handle_endtag(self,tag):
        if tag in self.void: return
        if not self.stack: self.errors.append(f'Unexpected closing </{tag}>'); return
        if self.stack[-1]!=tag: self.errors.append(f'Closing </{tag}> while <{self.stack[-1]}> is open'); return
        self.stack.pop()
p=StrictishParser(); p.feed(html); p.close()
if p.stack: p.errors.append('Unclosed: '+','.join(p.stack))
products=re.findall(r"\{id:'[^']+',name:'([^']+)',description:'([^']+)',price:(\d+),category:'[^']+',label:'[^']+',image:'([^']+)'\}",html)
images=[DIST/x[3] for x in products]
external=re.findall(r'''(?:src|href)=["'](https?:)?//[^"']+''',html,re.I)
scripts=re.findall(r'<script>([\s\S]*?)</script>',html,re.I)
inline=ROOT/'qa'/'inline-script.js'; inline.write_text('\n'.join(scripts),encoding='utf-8')
expected={
'Torta de Pistacho':('Ponqué de textura suave con una cubierta de chocolate blanco y pistacho.',8),
'Ponqué Chocolate Anella':('Ponqué con textura suave doble capa, cubierto con chocolate y almendra.',8),
'Torta Zanahoria':('Ponqué con textura húmeda cubierta de yogurt griego con nueces.',8),
'Pie de Pistacho':('Base de galleta con una capa de crema de pistacho con mousse de chocolate.',8),
'Cheesecake de Frutos Rojos':('Base de avena con queso crema con una capa de frutos rojos.',7),
'Brownie':('Torta cremosa de textura húmeda cubierta de chocolate y almendras picadas.',8)}
facts={x[0]:(x[1],int(x[2])) for x in products}
checks={
'htmlParser':not p.errors,
'hasDoctype':html.lstrip().lower().startswith('<!doctype html>'),
'exactly6Products':len(products)==6,
'exactVerifiedCopy':facts==expected,
'exactly6UniqueImages':len(set(x[3] for x in products))==6,
'allImagesExist':all(x.exists() and x.stat().st_size>0 for x in images),
'zeroExternalDependencies':not external,
'localFavicon':(DIST/'favicon.svg').exists() and 'href="favicon.svg"' in html,
'robotsNoindex':'noindex' in html and (DIST/'robots.txt').read_text().strip()=='User-agent: *\nDisallow: /',
'localOfficialPdf':(DIST/'menu-oficial.pdf').exists() and 'href="menu-oficial.pdf"' in html,
'disclosureExact':'Página web demo · Sitio no oficial · Pedido simulado' in html,
'noWhatsAppFetchXHR':not re.search(r'whatsapp|wa\.me|wa\.link|fetch\s*\(|XMLHttpRequest',html,re.I),
'inlineScriptExtracted':len(scripts)==1 and inline.stat().st_size>0}
report={'file':'dist/index.html','parser':'python stdlib html.parser with nesting checks','parserErrors':p.errors,'productCount':len(products),'productNames':[x[0] for x in products],'uniqueImageCount':len(set(x[3] for x in products)),'imageFiles':[str(x.relative_to(ROOT)) for x in images],'externalDependencies':external,'checks':checks,'status':'pass' if all(checks.values()) else 'fail','sha256':hashlib.sha256((DIST/'index.html').read_bytes()).hexdigest()}
(ROOT/'qa'/'structural-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(0 if report['status']=='pass' else 1)
