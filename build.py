import html, json, os, datetime
from articulos import ARTICULOS, GUIA, CURSO_N8N, CANAL

BASE = os.environ.get("BASE", "https://javierravel.github.io/tareas-ia")
OUT = os.path.join(os.path.dirname(__file__), "dist")
HOY = datetime.date.today().isoformat()
os.makedirs(OUT, exist_ok=True)

CSS = """
@font-face{font-family:Archivo;src:url(fonts/archivo.woff2) format("woff2");font-weight:100 900;font-display:swap}
@font-face{font-family:"Source Serif 4";src:url(fonts/source-serif-4.woff2) format("woff2");font-weight:200 900;font-display:swap}
@font-face{font-family:"Source Serif 4";src:url(fonts/source-serif-4-italic.woff2) format("woff2");font-weight:200 900;font-style:italic;font-display:swap}
:root{--paper:#f5f1e8;--sheet:#fcfaf5;--ink:#1d1b16;--muted:#5a5448;--line:#d6cfbf;--blue:#1b3fa0;--hl:#ffd84a;--tint:#ebe5d6;
--sans:Archivo,"Helvetica Neue",Arial,sans-serif;--serif:"Source Serif 4",Georgia,serif;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
--ease:cubic-bezier(.23,1,.32,1)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scrollbar-color:var(--ink) var(--paper)}
body{margin:0;background:var(--paper);color:var(--ink);font:1.125rem/1.62 var(--serif);font-optical-sizing:auto;caret-color:var(--blue)}
::selection{background:var(--hl);color:var(--ink)}
:focus-visible{outline:2px solid var(--blue);outline-offset:3px;border-radius:2px}
a{color:var(--blue);text-decoration-thickness:1px;text-underline-offset:.18em}a:hover{text-decoration-thickness:2px}
.wrap{max-width:44rem;margin:0 auto;padding:0 1.25rem}
header{border-bottom:2px solid var(--ink)}
header .wrap{display:flex;align-items:baseline;justify-content:space-between;gap:.5rem 1.25rem;flex-wrap:wrap;padding-top:1.1rem;padding-bottom:.9rem}
.logo{font:800 1.3rem/1 var(--sans);letter-spacing:-.02em;color:var(--ink);text-decoration:none}
.logo span{background:var(--hl);padding:.1em .22em;margin-left:.08em}
nav{display:flex;gap:1.25rem;font:500 .95rem/1 var(--sans)}
nav a{color:var(--ink);text-decoration:none;padding:.3rem 0;border-bottom:2px solid transparent;transition:border-color 160ms var(--ease)}nav a:hover{border-bottom-color:var(--ink)}
.donde{display:flex;justify-content:space-between;gap:1rem;font:500 .9rem/1.3 var(--sans);color:var(--muted);padding:.8rem 0;border-bottom:1px solid var(--line);font-variant-numeric:tabular-nums}
.donde a{color:var(--muted);text-decoration:none}.donde a:hover{color:var(--ink)}
h1,h2,h3{font-family:var(--sans);text-wrap:balance}
h1{font-weight:800;font-size:clamp(2rem,6vw,3.1rem);line-height:1.06;letter-spacing:-.028em;margin:2.5rem 0 1rem}
h2{font-weight:700;font-size:1.5rem;line-height:1.2;letter-spacing:-.015em;margin:2.9rem 0 .7rem}
p{margin:0 0 1.1rem;max-width:68ch}
.lead{font-size:1.28rem;line-height:1.5;color:var(--muted);margin:0 0 1.8rem}
strong{font-weight:600;padding:0 .12em;background:linear-gradient(transparent 58%,var(--hl) 58%) no-repeat 0 0/100% 100%}
.js main strong{background-size:0% 100%;transition:background-size 280ms var(--ease)}.js main strong.in{background-size:100% 100%}
ul,ol{padding-left:1.4rem;margin:0 0 1.2rem;max-width:68ch}li{margin:.45rem 0;padding-left:.2rem}
ol>li::marker{font:700 .95em var(--sans);font-variant-numeric:tabular-nums}ul>li::marker{color:var(--muted)}
code{font:.86em var(--mono);background:var(--tint);padding:.12em .36em;border-radius:3px}
.btn{display:inline-block;background:var(--ink);color:var(--paper);font:700 1rem/1 var(--sans);padding:.85rem 1.15rem;border-radius:4px;text-decoration:none;transition:background-color 160ms var(--ease),transform 160ms var(--ease)}
.btn:hover{background:var(--blue)}.btn:active{transform:scale(.97)}
.cta{background:var(--hl);border-radius:4px;padding:1.6rem 1.5rem;margin:2.6rem 0}
.cta b{display:block;font:800 1.45rem/1.15 var(--sans);letter-spacing:-.02em;margin-bottom:.45rem;text-wrap:balance}.cta p{margin:0 0 1.1rem}
.cta.slim{background:var(--sheet);border:1px solid var(--ink);padding:.95rem 1.1rem;margin:0 0 2.2rem;display:flex;align-items:center;justify-content:space-between;gap:.8rem 1.25rem;flex-wrap:wrap}
.cta.slim b{font-size:1.02rem;font-weight:700;letter-spacing:0;margin:0;flex:1 1 16rem}
.cta.slim .btn{font-size:.92rem;padding:.65rem .9rem;white-space:nowrap}
.prompt{background:var(--sheet);border:1px solid var(--ink);border-radius:4px;margin:1.8rem 0 .8rem;box-shadow:0 1px 2px rgba(29,27,22,.06),0 14px 28px -18px rgba(29,27,22,.35)}
.prompt .h{display:flex;justify-content:space-between;align-items:center;padding:.6rem .7rem .6rem 1.1rem;border-bottom:1px solid var(--line)}
.prompt .h b{font:700 .95rem/1 var(--sans)}
.prompt p{margin:0;padding:1rem 1.1rem 1.15rem;font:.95rem/1.6 var(--mono);max-width:none;overflow-wrap:anywhere}
.copy{font:600 .88rem/1 var(--sans);color:var(--ink);background:transparent;border:1px solid var(--ink);border-radius:4px;padding:.5rem .8rem;cursor:pointer;transition:background-color 160ms var(--ease),transform 160ms var(--ease)}
.copy:hover{background:var(--tint)}.copy:active{transform:scale(.97)}.copy.ok{background:var(--hl)}
.video{position:relative;width:100%;max-width:340px;aspect-ratio:9/16;margin:1.5rem 0;border:1px solid var(--ink);border-radius:6px;overflow:hidden;background:#000}
.video iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.faq{border-bottom:1px solid var(--line)}
.faq details{border-top:1px solid var(--line);padding:.95rem 0}
.faq summary{font:600 1.05rem/1.35 var(--sans);cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:1rem}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-weight:400;font-size:1.3rem;line-height:1;transition:transform 200ms var(--ease)}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq p{margin:.7rem 0 0;color:var(--muted)}
.autor{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:1.2rem 0;margin:2.6rem 0;color:var(--muted);font-size:1.02rem}
.autor b{color:var(--ink);font-family:var(--sans)}
.nextprev{display:flex;gap:1.5rem;justify-content:space-between;margin:2.6rem 0;flex-wrap:wrap}
.nextprev a{flex:1;min-width:13rem;border-top:2px solid var(--ink);padding-top:.7rem;text-decoration:none;color:var(--ink);font:700 1.1rem/1.25 var(--sans)}
.nextprev a:hover{color:var(--blue)}
.nextprev small{display:block;font-weight:500;font-size:.88rem;color:var(--muted);margin-bottom:.25rem;font-variant-numeric:tabular-nums}
.indice{list-style:none;padding:0;margin:0;max-width:none;border-bottom:2px solid var(--ink)}
.indice li{margin:0;padding:0;border-top:1px solid var(--line)}.indice li:first-child{border-top:2px solid var(--ink)}
.indice a{display:grid;grid-template-columns:3.2rem 1fr;gap:0 .6rem;padding:1.15rem 0;text-decoration:none;color:var(--ink)}
.indice .n{font:800 1.9rem/1 var(--sans);letter-spacing:-.03em;color:var(--muted);font-variant-numeric:tabular-nums;transition:color 160ms var(--ease)}
.indice h3{margin:0 0 .3rem;font-weight:700;font-size:1.28rem;line-height:1.2;letter-spacing:-.012em}
.indice h3 span{background:linear-gradient(var(--hl),var(--hl)) no-repeat 0 88%/0% .42em;transition:background-size 240ms var(--ease)}
.indice a:hover .n{color:var(--ink)}.indice a:hover h3 span{background-size:100% .42em}
.indice p{margin:0;color:var(--muted);font-size:1.02rem;line-height:1.5}
footer{border-top:2px solid var(--ink);margin-top:4rem;padding:1.6rem 0 2.2rem;color:var(--muted);font:500 .92rem/1.6 var(--sans)}
footer p{margin:0 0 .3rem}footer a{color:var(--muted)}footer a:hover{color:var(--ink)}
@media (max-width:30rem){body{font-size:1.06rem}nav{gap:1rem;font-size:.9rem}.indice a{grid-template-columns:2.5rem 1fr}.indice .n{font-size:1.5rem}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}.js main strong{background-size:100% 100%}}
"""

JS = """<script>document.querySelectorAll('.copy').forEach(b=>b.addEventListener('click',()=>{const t=b.closest('.prompt').querySelector('p').innerText;navigator.clipboard.writeText(t).then(()=>{b.textContent='¡Copiado!';b.classList.add('ok');setTimeout(()=>{b.textContent='Copiar';b.classList.remove('ok')},1500)})}));
(()=>{const s=document.querySelectorAll('main strong');if(!('IntersectionObserver' in window)){s.forEach(e=>e.classList.add('in'));return}
const o=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');o.unobserve(e.target)}}),{rootMargin:'0px 0px -12% 0px'});s.forEach(e=>o.observe(e))})()</script>"""


def page(title, desc, path, body, extra_head="", donde=""):
    url = f"{BASE}/{path}" if path != "index.html" else f"{BASE}/"
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="google-site-verification" content="j29_lUV5cW3bUKpwCXkFWc7-2CDuGl0R0aA49vF_pfM">
<meta name="theme-color" content="#f5f1e8">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<link rel="preload" href="fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/source-serif-4.woff2" as="font" type="font/woff2" crossorigin>
<script>document.documentElement.className='js'</script>
<style>{CSS}</style>
{extra_head}
</head>
<body>
<header><div class="wrap"><a class="logo" href="index.html">Javi <span>Automates</span></a>
<nav><a href="index.html">Tareas</a><a href="sobre.html">Sobre mí</a><a href="{GUIA}">Guía gratis</a></nav></div></header>
<main class="wrap">
{donde}{body}
</main>
<footer><div class="wrap">
<p>Javi Automates · IA sin código que te ahorra horas en la oficina.</p>
<p><a href="{CANAL}">YouTube</a> · <a href="{GUIA}">Guía gratis</a> · <a href="sobre.html">Sobre mí</a> · <a href="privacidad.html">Privacidad</a></p>
</div></footer>
{JS}
</body>
</html>
"""


def cta(top=False):
    if top:
        return f"""<div class="cta slim"><b>Guía gratis: 10 tareas de oficina que la IA te hace sola</b>
<a class="btn" href="{GUIA}">Quiero la guía gratis</a></div>"""
    return f"""<div class="cta"><b>¿Te sirvió? Hay 9 tareas más.</b>
<p>Bajate la guía gratis: 8 tareas con Claude y 2 automatizaciones con n8n, cada una con su prompt listo para copiar.</p>
<a class="btn" href="{GUIA}">Descargar la guía gratis</a></div>"""


def prompt_box(p):
    if not p:
        return ""
    return f"""<div class="prompt"><div class="h"><b>El prompt</b><button class="copy">Copiar</button></div>
<p>{html.escape(p)}</p></div>
<p style="color:var(--muted);font-size:1rem">Cambiá lo que está entre [corchetes] por tus datos.</p>"""


N = len(ARTICULOS)
for i, a in enumerate(ARTICULOS):
    body = a["cuerpo"].replace("{prompt}", prompt_box(a["prompt"])).replace("{curso}", CURSO_N8N)
    faq_html = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(r)}</p></details>" for q, r in a["faq"])
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Article", "headline": a["titulo"], "description": a["desc"], "inLanguage": "es",
             "author": {"@type": "Person", "name": "Javier Ravel", "url": CANAL}, "datePublished": a.get("fecha", HOY),
             "mainEntityOfPage": f"{BASE}/{a['slug']}.html"},
            {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in a["faq"]]},
        ],
    }
    prev_a = ARTICULOS[i - 1] if i > 0 else None
    next_a = ARTICULOS[i + 1] if i < N - 1 else None
    nav = '<div class="nextprev">'
    if prev_a:
        nav += f'<a href="{prev_a["slug"]}.html"><small>← Tarea #{prev_a["num"]}</small>{prev_a["corto"]}</a>'
    if next_a:
        nav += f'<a href="{next_a["slug"]}.html" style="text-align:right"><small>Tarea #{next_a["num"]} →</small>{next_a["corto"]}</a>'
    nav += "</div>"
    video_html = ""
    if a.get("video"):
        video_html = f"""<h2>Miralo en 25 segundos</h2>
<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{a['video']}" title="{html.escape(a['corto'])}" loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
"""
    donde = '<div class="donde"><span>Tarea ' + str(a["num"]) + " de " + str(N) + '</span><a href="index.html">Todas las tareas</a></div>\n'
    full = f"""<h1>{html.escape(a['titulo'])}</h1>
<p class="lead">{html.escape(a['desc'])}</p>
{cta(top=True)}
{body}
{video_html}<h2>Preguntas frecuentes</h2>
<div class="faq">{faq_html}</div>
{cta()}
<p class="autor"><b>Javier Ravel</b> — trabajo en IT en una universidad y uso IA todos los días para ahorrarme tareas repetitivas. En <a href="{CANAL}">Javi Automates</a> muestro cómo, sin programar.</p>
{nav}"""
    extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    open(os.path.join(OUT, a["slug"] + ".html"), "w").write(page(a["titulo"] + " | Javi Automates", a["desc"], a["slug"] + ".html", full, extra, donde))

cards = "".join(f'<li><a href="{a["slug"]}.html"><span class="n">{a["num"]}</span><div><h3><span>{html.escape(a["titulo"])}</span></h3><p>{html.escape(a["desc"])}</p></div></a></li>' for a in ARTICULOS)
idx = f"""<h1>Tareas de oficina que la IA te hace sola</h1>
<p class="lead">Guías cortas, paso a paso y sin programar: el prompt listo para copiar, los errores comunes y un video de 25 segundos. Con Claude y n8n.</p>
{cta(top=True)}
<ol class="indice">{cards}</ol>"""
open(os.path.join(OUT, "index.html"), "w").write(page("Tareas de oficina con IA, paso a paso y sin código | Javi Automates",
     "Guías cortas para ahorrar horas en la oficina con IA: presentaciones, plantillas de WhatsApp, manuales, recordatorios y formularios automáticos. Prompts listos para copiar.", "index.html", idx))

sobre = f"""<h1>Sobre mí</h1>
<p>Soy Javier Ravel. Trabajo en IT en una universidad: computadoras, aulas, sistemas de exámenes, grabación de clases. Buena parte de mi trabajo es resolver tareas repetitivas, y hoy las resuelvo con IA.</p>
<p>En <a href="{CANAL}">Javi Automates</a> muestro cómo usar Claude, n8n y otras herramientas para ahorrar horas en la oficina, sin programar. Todo lo que publico lo probé yo.</p>
<p>Los videos usan mi voz clonada con IA y lo aviso en cada uno.</p>
{cta()}"""
open(os.path.join(OUT, "sobre.html"), "w").write(page("Sobre mí | Javi Automates", "Quién escribe estas guías y por qué.", "sobre.html", sobre))

priv = f"""<h1>Política de privacidad</h1>
<p>Última actualización: {HOY}.</p>
<h2>Qué datos se recogen</h2>
<p>Este sitio no tiene formularios ni cuentas. Si descargás la guía gratis, lo hacés en Gumroad, que tiene su propia política de privacidad.</p>
<h2>Videos de YouTube</h2>
<p>Los videos se insertan en modo de privacidad mejorada (youtube-nocookie.com). YouTube puede guardar datos cuando reproducís un video; ver la política de privacidad de Google.</p>
<h2>Publicidad y cookies</h2>
<p>Este sitio puede mostrar anuncios de Google AdSense. Google y sus socios usan cookies para mostrar anuncios según tus visitas anteriores a este y otros sitios. Podés desactivar la publicidad personalizada en <a href="https://adssettings.google.com" rel="nofollow">la configuración de anuncios de Google</a>. Más información en <a href="https://policies.google.com/technologies/ads" rel="nofollow">cómo usa Google las cookies en publicidad</a>.</p>
<h2>Contacto</h2>
<p>Para cualquier consulta sobre esta política, escribime a javiautomates@gmail.com.</p>"""
open(os.path.join(OUT, "privacidad.html"), "w").write(page("Política de privacidad | Javi Automates", "Política de privacidad y cookies.", "privacidad.html", priv))

urls = ["", "sobre.html"] + [a["slug"] + ".html" for a in ARTICULOS]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{BASE}/{u}</loc><lastmod>{HOY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
import shutil
FONTS = os.path.join(os.path.dirname(__file__), "fonts")
os.makedirs(os.path.join(OUT, "fonts"), exist_ok=True)
for f in os.listdir(FONTS):
    shutil.copy(os.path.join(FONTS, f), os.path.join(OUT, "fonts", f))
print("ok", sorted(os.listdir(OUT)))
