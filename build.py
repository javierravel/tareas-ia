import html, json, os, datetime
from articulos import ARTICULOS, GUIA, CURSO_N8N, CANAL

BASE = os.environ.get("BASE", "https://javierravel.github.io/tareas-ia")
OUT = os.path.join(os.path.dirname(__file__), "dist")
HOY = datetime.date.today().isoformat()
os.makedirs(OUT, exist_ok=True)

CSS = """
:root{--bg:#0f1420;--card:#171e2e;--ink:#e9edf5;--muted:#9aa6bd;--amber:#f5b82e;--green:#3ddc97;--line:#26304a}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:18px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,sans-serif}
a{color:var(--amber)}a:hover{text-decoration:none}
.wrap{max-width:760px;margin:0 auto;padding:0 20px}
header{border-bottom:1px solid var(--line)}
header .wrap{display:flex;align-items:center;justify-content:space-between;height:64px}
.logo{font-weight:800;color:var(--ink);text-decoration:none;font-size:20px}.logo span{color:var(--amber)}
nav a{color:var(--muted);text-decoration:none;margin-left:18px;font-size:16px}nav a:hover{color:var(--ink)}
h1{font-size:clamp(28px,5vw,40px);line-height:1.2;margin:36px 0 12px}
h2{font-size:24px;margin:40px 0 10px}
.lead{color:var(--muted);font-size:19px;margin:0 0 24px}
.tag{display:inline-block;background:#26304a;color:var(--amber);font-weight:700;font-size:14px;padding:4px 10px;border-radius:99px;margin-top:28px}
li{margin:6px 0}code{background:#222b40;padding:2px 6px;border-radius:6px;font-size:.9em}
.cta{background:linear-gradient(135deg,#1d2640,#20203a);border:1px solid #3a4466;border-radius:16px;padding:22px 24px;margin:28px 0}
.cta b{display:block;font-size:20px;margin-bottom:4px}.cta p{margin:0 0 14px;color:var(--muted)}
.btn{display:inline-block;background:var(--amber);color:#1a1300;font-weight:800;padding:12px 20px;border-radius:12px;text-decoration:none}
.btn:hover{filter:brightness(1.08)}
.prompt{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--amber);border-radius:12px;padding:18px 20px;margin:24px 0}
.prompt .h{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.prompt .h b{color:var(--amber)}.prompt p{margin:0;font-family:ui-monospace,Menlo,monospace;font-size:16px;line-height:1.6}
.copy{background:#26304a;color:var(--ink);border:0;border-radius:8px;padding:6px 12px;font-weight:700;cursor:pointer;font-size:14px}
.video{position:relative;width:100%;max-width:340px;aspect-ratio:9/16;margin:24px auto;border-radius:16px;overflow:hidden;background:#000}
.video iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.faq details{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin:10px 0}
.faq summary{font-weight:700;cursor:pointer}.faq p{margin:10px 0 0;color:var(--muted)}
.nextprev{display:flex;gap:12px;justify-content:space-between;margin:40px 0;flex-wrap:wrap}
.nextprev a{flex:1;min-width:220px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;text-decoration:none;color:var(--ink)}
.nextprev small{display:block;color:var(--muted)}
.cards{display:grid;gap:14px;margin:28px 0}
.card{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;text-decoration:none;color:var(--ink)}
.card:hover{border-color:var(--amber)}.card small{color:var(--amber);font-weight:700}.card h3{margin:4px 0;font-size:20px}.card p{margin:0;color:var(--muted);font-size:16px}
footer{border-top:1px solid var(--line);margin-top:60px;padding:28px 0;color:var(--muted);font-size:15px}
footer a{color:var(--muted)}
.autor{display:flex;gap:14px;align-items:center;background:var(--card);border-radius:14px;padding:16px 18px;margin:36px 0;color:var(--muted);font-size:16px}
.autor b{color:var(--ink)}
"""

JS = """<script>document.querySelectorAll('.copy').forEach(b=>b.addEventListener('click',()=>{const t=b.closest('.prompt').querySelector('p').innerText;navigator.clipboard.writeText(t).then(()=>{b.textContent='¡Copiado!';setTimeout(()=>b.textContent='Copiar',1500)})}))</script>"""


def page(title, desc, path, body, extra_head=""):
    url = f"{BASE}/{path}" if path != "index.html" else f"{BASE}/"
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="google-site-verification" content="j29_lUV5cW3bUKpwCXkFWc7-2CDuGl0R0aA49vF_pfM">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<style>{CSS}</style>
{extra_head}
</head>
<body>
<header><div class="wrap"><a class="logo" href="index.html">Javi <span>Automates</span></a>
<nav><a href="index.html">Tareas</a><a href="sobre.html">Sobre mí</a><a href="{GUIA}">Guía gratis</a></nav></div></header>
<main class="wrap">
{body}
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
        return f"""<div class="cta"><b>🎁 Guía gratis: 10 tareas de oficina que la IA te hace sola</b>
<p>Esta es una de las tareas. Las otras 9, con su prompt y el truco de cada una, en un PDF gratis.</p>
<a class="btn" href="{GUIA}">Quiero la guía gratis</a></div>"""
    return f"""<div class="cta"><b>¿Te sirvió? Hay 9 tareas más.</b>
<p>Bajate la guía gratis: 8 tareas con Claude y 2 automatizaciones con n8n, cada una con su prompt listo para copiar.</p>
<a class="btn" href="{GUIA}">Descargar la guía gratis</a></div>"""


def prompt_box(p):
    if not p:
        return ""
    return f"""<div class="prompt"><div class="h"><b>El prompt</b><button class="copy">Copiar</button></div>
<p>{html.escape(p)}</p></div>
<p style="color:var(--muted);font-size:16px">Cambiá lo que está entre [corchetes] por tus datos.</p>"""


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
    full = f"""<span class="tag">Tarea de oficina #{a['num']}</span>
<h1>{html.escape(a['titulo'])}</h1>
<p class="lead">{html.escape(a['desc'])}</p>
{cta(top=True)}
{body}
{video_html}<h2>Preguntas frecuentes</h2>
<div class="faq">{faq_html}</div>
{cta()}
<div class="autor"><div>✍️</div><div><b>Javier Ravel</b> — trabajo en IT en una universidad y uso IA todos los días para ahorrarme tareas repetitivas. En <a href="{CANAL}">Javi Automates</a> muestro cómo, sin programar.</div></div>
{nav}"""
    extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    open(os.path.join(OUT, a["slug"] + ".html"), "w").write(page(a["titulo"] + " | Javi Automates", a["desc"], a["slug"] + ".html", full, extra))

cards = "".join(f'<a class="card" href="{a["slug"]}.html"><small>Tarea #{a["num"]}</small><h3>{html.escape(a["titulo"])}</h3><p>{html.escape(a["desc"])}</p></a>' for a in ARTICULOS)
idx = f"""<h1>Tareas de oficina que la IA te hace sola</h1>
<p class="lead">Guías cortas, paso a paso y sin programar: el prompt listo para copiar, los errores comunes y un video de 25 segundos. Con Claude y n8n.</p>
{cta(top=True)}
<div class="cards">{cards}</div>"""
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
print("ok", sorted(os.listdir(OUT)))
