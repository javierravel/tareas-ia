#!/usr/bin/env python3
"""Serie 'Tareas que tu jefe no sabe que hace la IA' (1080x1920, 30 fps).
Usage: render_jefe.py <dir> [frames]   (dir has durs.json and texts.json)"""
import json
import os
import sys

sys.path.insert(0, os.environ.get("REEL_DIR", "/home/claude/reel"))
import render as r  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402

W, H = r.W, r.H
BG, CARD, LINE, WHITE, MUTED, AMBER, GREEN, RED = r.BG, r.CARD, r.LINE, r.WHITE, r.MUTED, r.AMBER, r.GREEN, r.RED
font, card, mix, prog = r.font, r.card, r.mix, r.prog
YEL = (255, 214, 10)
BANNER = (220, 38, 38)

HERE = os.path.abspath(sys.argv[1])
DURS = json.load(open(os.path.join(HERE, "durs.json")))
TEXTS = json.load(open(os.path.join(HERE, "texts.json")))  # on-screen subtitle text per scene (correct spelling)
META = json.load(open(os.path.join(HERE, "meta.json")))
PART = META["part"]  # int = parte de la serie; str = Short suelto (ver PARTS)
PART = int(PART) if str(PART).isdigit() else PART
BANNER_TXT = META.get("banner")  # [linea1, linea2] para Shorts sueltos
PAD = 0.25


def ctext(d, y, text, f, fill=WHITE, x0=0, x1=None):
    x1 = W if x1 is None else x1
    w = d.textlength(text, font=f)
    d.text((x0 + (x1 - x0 - w) / 2, y), text, font=f, fill=fill)


def wrap(d, text, f, width):
    out, cur = [], ""
    for w_ in text.split():
        test = (cur + " " + w_).strip()
        if d.textlength(test, font=f) > width and cur:
            out.append(cur)
            cur = w_
        else:
            cur = test
    out.append(cur)
    return out


def banner(d):
    d.rounded_rectangle((60, 70, W - 60, 250), 28, fill=BANNER)
    if BANNER_TXT:
        ctext(d, 88, BANNER_TXT[0], font("Black", 54), WHITE)
        ctext(d, 158, BANNER_TXT[1], font("Black", 54), YEL)
        return
    ctext(d, 88, "TAREAS QUE TU JEFE NO SABE", font("Black", 54), WHITE)
    ctext(d, 158, f"QUE HACE LA IA  ·  PARTE {PART}", font("Black", 54), YEL)


def subs(d, k, t):
    """Two-word chunks timed by character length; the longest word of the chunk in yellow."""
    words = TEXTS[k].split()
    dur = max(0.5, DURS[k] - PAD)
    total = sum(len(w) + 1 for w in words)
    chunks, acc = [], 0.0
    for i in range(0, len(words), 2):
        ch = words[i:i + 2]
        ln = sum(len(w) + 1 for w in ch)
        chunks.append((acc / total * dur, ch))
        acc += ln
    cur = chunks[0][1]
    for st, ch in chunks:
        if t >= st:
            cur = ch
    f = font("Black", 76)
    hi = max(range(len(cur)), key=lambda j: len(cur[j]))
    parts = [(w.upper(), YEL if j == hi else WHITE) for j, w in enumerate(cur)]
    tw = sum(d.textlength(p + " ", font=f) for p, _ in parts) - d.textlength(" ", font=f)
    x = (W - tw) / 2
    y = 1500
    for p, c in parts:
        for dx, dy in [(-4, 0), (4, 0), (0, -4), (0, 4), (-3, -3), (3, 3), (-3, 3), (3, -3)]:
            d.text((x + dx, y + dy), p, font=f, fill=(0, 0, 0))
        d.text((x, y), p, font=f, fill=c)
        x += d.textlength(p + " ", font=f)


def frame(k, t, draw_fn):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    draw_fn(im, d, t)
    banner(d)
    subs(d, k, t)
    r.label(d)
    return im


# ---------- sheet helpers ----------
COLS = [("A", "Fecha", 230), ("B", "Vendedor", 250), ("C", "Monto", 220)]
ROWS = [("03/03", "Pérez", "12.500"), ("07/03", "Gómez", "8.900"), ("15/03", "Pérez", "21.300"),
        ("22/03", "Ruiz", "5.400"), ("29/03", "Pérez", "14.500"), ("02/04", "Pérez", "9.800")]


def sheet(d, x0, y0, a=1.0, hl=None):
    rh = 78
    x = x0 + 70
    d.rectangle((x0, y0, x0 + 70 + sum(c[2] for c in COLS), y0 + rh * (len(ROWS) + 2)), fill=mix((245, 247, 250), a))
    for col, name, w in COLS:
        d.rectangle((x, y0, x + w, y0 + rh), fill=mix((225, 230, 238), a), outline=mix((200, 205, 215), a))
        ctext(d, y0 + 20, col, font("Bold", 34), mix((90, 100, 120), a), x, x + w)
        d.rectangle((x, y0 + rh, x + w, y0 + 2 * rh), fill=mix((235, 240, 247), a), outline=mix((200, 205, 215), a))
        ctext(d, y0 + rh + 20, name, font("ExtraBold", 34), mix((40, 50, 70), a), x, x + w)
        x += w
    for i, row in enumerate(ROWS):
        yy = y0 + (i + 2) * rh
        d.rectangle((x0, yy, x0 + 70, yy + rh), fill=mix((225, 230, 238), a), outline=mix((200, 205, 215), a))
        ctext(d, yy + 20, str(i + 2), font("Bold", 32), mix((90, 100, 120), a), x0, x0 + 70)
        x = x0 + 70
        for j, (col, name, w) in enumerate(COLS):
            fill = (255, 255, 255)
            if hl and i in hl:
                fill = (255, 243, 196)
            d.rectangle((x, yy, x + w, yy + rh), fill=mix(fill, a), outline=mix((210, 215, 225), a))
            ctext(d, yy + 20, row[j], font("Medium", 36), mix((40, 50, 70), a), x, x + w)
            x += w


# ---------- scenes (Parte 1: fórmulas de Excel) ----------

def s1(im, d, t):
    sheet(d, 100, 330)
    # formula bar with error
    card(d, (100, 1000, 980, 1110), fill=(255, 255, 255), outline=(200, 205, 215), r=14)
    d.text((130, 1028), "fx", font=font("Bold", 40), fill=(120, 130, 150))
    d.text((210, 1026), "=SUMA(¿¿??", font=font("Medium", 44), fill=(40, 50, 70))
    p = prog(t, 1.6, 0.3)
    if p > 0:
        d.rounded_rectangle((300, 1170, 780, 1280), 30, fill=mix(RED, p))
        ctext(d, 1188, "#¿NOMBRE?", font("Black", 62), mix(WHITE, p), 300, 780)
    if t < 1.4:
        s = 1 + 0.15 * (1 - prog(t, 0, 0.3))
        f = font("Black", int(110 * s))
        d.rounded_rectangle((70, 560, W - 70, 860), 40, fill=YEL)
        ctext(d, 610, "GUARDÁ", f, BG)
        ctext(d, 610 + int(120 * s), "ESTE VIDEO", f, BG)


def s2(im, d, t):
    ctext(d, 330, "Se la pedís en castellano", font("Black", 64), WHITE)
    card(d, (80, 470, 1000, 1360), fill=(250, 249, 245), outline=(225, 220, 205), r=30)
    d.text((130, 510), "Claude", font=font("Black", 48), fill=(205, 110, 70))
    msg = "Sumá las ventas de marzo, solo del vendedor Pérez. Fecha en A, vendedor en B, monto en C."
    n = int(len(msg) * min(1.0, max(0.0, t / max(0.8, DURS[1] * 0.75))))
    d.rounded_rectangle((240, 620, 960, 1000), 28, fill=(232, 226, 210))
    f = font("Medium", 44)
    for i, ln in enumerate(wrap(d, msg[:n], f, 660)):
        d.text((280, 650 + i * 60), ln, font=f, fill=(40, 40, 40))
    if n >= len(msg):
        p = prog(t, DURS[1] * 0.8, 0.3)
        d.ellipse((130, 1080, 170, 1120), fill=mix((205, 110, 70), p))
        d.text((190, 1078), "Pensando…", font=font("Medium", 40), fill=mix((120, 120, 120), p))


FORM = '=SUMAR.SI.CONJUNTO(C:C;B:B;"Pérez";A:A;">="&FECHA(2026;3;1);A:A;"<"&FECHA(2026;4;1))'


def s3(im, d, t):
    sheet(d, 100, 330, hl=[0, 2, 4])
    card(d, (60, 1000, 1020, 1260), fill=(255, 255, 255), outline=GREEN, r=16, width=4)
    d.text((90, 1020), "fx", font=font("Bold", 38), fill=(120, 130, 150))
    n = int(len(FORM) * min(1.0, max(0.0, t / max(0.6, DURS[2] * 0.55))))
    f = font("Medium", 36)
    for i, ln in enumerate(wrap(d, FORM[:n].replace(";", "; "), f, 830)):
        d.text((160, 1020 + i * 50), ln, font=f, fill=(30, 40, 60))
    p = prog(t, DURS[2] * 0.6, 0.35)
    if p > 0:
        d.rounded_rectangle((260, 1300, 820, 1420), 30, fill=mix(GREEN, p))
        ctext(d, 1318, "Total: $ 48.300", font("Black", 62), mix(BG, p), 260, 820)


PROMPT = ("Tengo una planilla: [QUÉ HAY EN CADA COLUMNA]. Dame la fórmula de Excel en español para "
          "[LO QUE NECESITÁS]. Explicámela en una línea.")


def s4(im, d, t):
    ctext(d, 330, "EL TRUCO", font("Black", 84), AMBER)
    card(d, (80, 470, 1000, 1380), fill=CARD, outline=AMBER, r=26, width=4)
    d.text((120, 505), "Prompt", font=font("ExtraBold", 42), fill=AMBER)
    n = int(len(PROMPT) * min(1.0, max(0.0, t / max(0.6, DURS[3] * 0.7))))
    f = font("Medium", 46)
    for i, ln in enumerate(wrap(d, PROMPT[:n], f, 820)):
        d.text((120, 590 + i * 66), ln, font=f, fill=WHITE)


def s5(im, d, t):
    ctext(d, 420, "COMENTÁ", font("Black", 130), WHITE)
    pulse = 1 + 0.05 * abs(((t * 2) % 2) - 1)
    ctext(d, 580, "GUIA", font("Black", int(220 * pulse)), YEL)
    ctext(d, 860, "y te mando la guía gratis", font("Bold", 58), WHITE)
    ctext(d, 945, "con 10 tareas más", font("Medium", 50), MUTED)
    by = 1110 + int(30 * abs(((t * 1.6) % 2) - 1))
    cx = W // 2
    d.polygon([(cx - 80, by), (cx + 80, by), (cx, by + 110)], fill=YEL)
    p = prog(t, 0.8, 0.4)
    if p > 0:
        ctext(d, 1300, f"Seguime para la parte {PART + 1}", font("Bold", 52), mix(GREEN, p))



# ---------- generic helpers for parts 2+ ----------

def stamp(d, t):
    if t < 1.4:
        s = 1 + 0.15 * (1 - prog(t, 0, 0.3))
        f = font("Black", int(110 * s))
        d.rounded_rectangle((70, 560, W - 70, 860), 40, fill=YEL)
        ctext(d, 610, "GUARDÁ", f, BG)
        ctext(d, 610 + int(120 * s), "ESTE VIDEO", f, BG)


def chat_scene(title, msg, attach=None):
    def fn(im, d, t):
        ctext(d, 330, title, font("Black", 64), WHITE)
        card(d, (80, 470, 1000, 1360), fill=(250, 249, 245), outline=(225, 220, 205), r=30)
        d.text((130, 510), "Claude", font=font("Black", 48), fill=(205, 110, 70))
        y0 = 620
        if attach:
            d.rounded_rectangle((420, 600, 960, 700), 20, fill=(222, 214, 194))
            d.text((450, 625), attach, font=font("Bold", 40), fill=(80, 70, 50))
            y0 = 730
        n = int(len(msg) * min(1.0, max(0.0, t / max(0.8, DURS[1] * 0.75))))
        f = font("Medium", 44)
        lines = wrap(d, msg, f, 660)
        d.rounded_rectangle((240, y0, 960, y0 + 60 + 60 * len(lines)), 28, fill=(232, 226, 210))
        for i, ln in enumerate(wrap(d, msg[:n], f, 660)):
            d.text((280, y0 + 30 + i * 60), ln, font=f, fill=(40, 40, 40))
        if n >= len(msg):
            p = prog(t, DURS[1] * 0.8, 0.3)
            yy = y0 + 110 + 60 * len(lines)
            d.ellipse((130, yy, 170, yy + 40), fill=mix((205, 110, 70), p))
            d.text((190, yy - 2), "Pensando…", font=font("Medium", 40), fill=mix((120, 120, 120), p))
    return fn


def prompt_scene(prompt):
    def fn(im, d, t):
        ctext(d, 330, "EL TRUCO", font("Black", 84), AMBER)
        card(d, (80, 470, 1000, 1380), fill=CARD, outline=AMBER, r=26, width=4)
        d.text((120, 505), "Prompt", font=font("ExtraBold", 42), fill=AMBER)
        n = int(len(prompt) * min(1.0, max(0.0, t / max(0.6, DURS[3] * 0.7))))
        f = font("Medium", 46)
        for i, ln in enumerate(wrap(d, prompt[:n], f, 820)):
            d.text((120, 590 + i * 66), ln, font=f, fill=WHITE)
    return fn


def reveal_lines(d, t, dur, items, y0, x0=120, f=None, gap=118, color=(40, 50, 70), marks=None):
    f = f or font("Medium", 40)
    for i, txt in enumerate(items):
        p = prog(t, 0.2 + i * dur * 0.13, 0.25)
        if p <= 0:
            continue
        yy = y0 + i * gap
        for j, ln in enumerate(wrap(d, txt, f, 760)):
            d.text((x0 + 40, yy + j * 48), ln, font=f, fill=mix(color, p))
        if marks and marks[i]:
            d.text((x0 - 10, yy - 4), "★", font=font("Black", 46), fill=mix((230, 170, 0), p))
        else:
            d.ellipse((x0, yy + 14, x0 + 18, yy + 32), fill=mix((120, 130, 150), p))


# ---------- Parte 2: resumir 40 mails ----------
MAILS = [("RRHH", "Recordatorio: cargar horas"), ("Proveedor X", "Factura 4471 vencida"), ("Marta", "RE: RE: RE: reunión jueves"),
         ("Newsletter", "10 tips de productividad"), ("Cliente Sosa", "¿Llegó el pedido?"), ("Sistemas", "Cambio de contraseña"),
         ("Jefe", "Necesito el informe HOY"), ("Marketing", "Fotos del evento")]


def p2s1(im, d, t):
    card(d, (60, 300, 1020, 1400), fill=(255, 255, 255), outline=(210, 215, 225), r=24)
    d.text((100, 330), "Bandeja de entrada", font=font("Black", 50), fill=(40, 50, 70))
    d.rounded_rectangle((760, 330, 990, 400), 35, fill=RED)
    n = int(min(40, 3 + t * 30))
    ctext(d, 338, f"{n} sin leer", font("Black", 40), WHITE, 760, 990)
    for i, (who, subj) in enumerate(MAILS):
        yy = 440 + i * 118
        d.line((90, yy - 10, 990, yy - 10), fill=(230, 232, 238), width=2)
        d.ellipse((100, yy + 20, 124, yy + 44), fill=(40, 110, 230))
        d.text((150, yy), who, font=font("Bold", 40), fill=(30, 40, 60))
        d.text((150, yy + 50), subj, font=font("Medium", 36), fill=(110, 120, 140))
    stamp(d, t)


SUM = ["Jefe: quiere el informe hoy, antes de las 17.", "Proveedor X: la factura 4471 vence el lunes.",
       "Cliente Sosa pregunta por su pedido.", "Marta movió la reunión al jueves 10:00.",
       "El resto (24 mails): avisos y newsletters, se pueden ignorar."]


def p2s3(im, d, t):
    card(d, (60, 330, 1020, 1300), fill=(255, 255, 255), outline=GREEN, r=24, width=4)
    d.text((110, 365), "Resumen de 40 mails", font=font("Black", 50), fill=(30, 40, 60))
    reveal_lines(d, t, DURS[2], SUM, 480, gap=150, f=font("Medium", 42), marks=[1, 1, 1, 0, 0])
    p = prog(t, DURS[2] * 0.7, 0.3)
    if p > 0:
        d.rounded_rectangle((210, 1340, 870, 1450), 30, fill=mix(GREEN, p))
        ctext(d, 1358, "40 mails → 5 renglones", font("Black", 54), mix(BG, p), 210, 870)


P2_PROMPT = ("Te pego mis mails sin leer. Resumilos en 5 renglones: qué es urgente, qué puedo ignorar y a quién "
             "contesto primero. Marcá con ★ lo que necesita respuesta hoy.")

# ---------- Parte 3: cliente enojado ----------
ANGRY = "¡¡Es la TERCERA vez que les escribo!! El pedido no llegó y nadie me contesta. INACEPTABLE. Quiero mi plata ya."


def p3s1(im, d, t):
    card(d, (60, 330, 1020, 1250), fill=(255, 255, 255), outline=RED, r=24, width=5)
    d.text((110, 365), "De: Cliente Sosa", font=font("Bold", 42), fill=(30, 40, 60))
    d.text((110, 425), "Asunto: ¡¡RECLAMO!!", font=font("Black", 44), fill=RED)
    f = font("Medium", 46)
    for i, ln in enumerate(wrap(d, ANGRY, f, 840)):
        d.text((110, 530 + i * 66), ln, font=f, fill=(40, 40, 40))
    p = prog(t, 1.5, 0.3)
    if p > 0:
        sh = int(8 * abs(((t * 8) % 2) - 1))
        d.rounded_rectangle((330 + sh, 1300, 750 + sh, 1410), 30, fill=mix(RED, p))
        ctext(d, 1318, "CLIENTE FURIOSO", font("Black", 46), mix(WHITE, p), 330 + sh, 750 + sh)
    stamp(d, t)


REPLY = ("Hola, Sr. Sosa. Tiene razón: tendríamos que haberle contestado antes, le pido disculpas. "
         "Su pedido salió tarde por un error nuestro. Llega el jueves y le devolvemos el envío. "
         "Le escribo yo mismo el jueves para confirmar.")


def p3s3(im, d, t):
    card(d, (60, 330, 1020, 1300), fill=(255, 255, 255), outline=GREEN, r=24, width=4)
    d.text((110, 365), "Respuesta", font=font("Black", 50), fill=(30, 40, 60))
    n = int(len(REPLY) * min(1.0, max(0.0, t / max(0.6, DURS[2] * 0.7))))
    f = font("Medium", 42)
    for i, ln in enumerate(wrap(d, REPLY[:n], f, 840)):
        d.text((110, 460 + i * 60), ln, font=f, fill=(40, 50, 70))
    p = prog(t, DURS[2] * 0.75, 0.3)
    if p > 0:
        d.rounded_rectangle((180, 1340, 900, 1450), 30, fill=mix(GREEN, p))
        ctext(d, 1358, "Disculpa + causa + fecha", font("Black", 52), mix(BG, p), 180, 900)


P3_PROMPT = ("Un cliente me escribió enojado (te lo pego). Puedo ofrecer [LO QUE PODÉS DAR]. Escribí una respuesta "
             "corta: disculpa, causa y solución con fecha. Sin frases de robot como 'lamentamos los inconvenientes'.")

# ---------- Parte 4: acta desde el pizarrón ----------


def p4s1(im, d, t):
    d.rounded_rectangle((50, 320, 1030, 1300), 20, fill=(248, 250, 248), outline=(150, 155, 160), width=12)
    import math
    blue, red, grn = (30, 80, 200), (200, 40, 40), (20, 130, 60)
    items = [("Lanzamiento → 15/12?", blue, 120, 380, -3), ("Ana: presupuesto", red, 140, 520, 2),
             ("Web nueva — Leo", grn, 160, 660, -2), ("¿¿proveedor??", red, 520, 800, 6),
             ("mail clientes viernes", blue, 130, 940, -1), ("OK ✓ precio", grn, 600, 1100, 4)]
    for i, (txt, c, x, y, ang) in enumerate(items):
        p = prog(t, 0.1 + i * 0.12, 0.2)
        if p <= 0:
            continue
        f = font("Bold", 58)
        w = int(d.textlength(txt, font=f)) + 20
        layer = Image.new("RGBA", (w, 90), (0, 0, 0, 0))
        ImageDraw.Draw(layer).text((10, 5), txt, font=f, fill=c + (int(255 * p),))
        layer = layer.rotate(ang, expand=True, resample=Image.BICUBIC)
        im.paste(layer, (x, y), layer)
    d.line((120, 1230, 480, 1180), fill=(30, 80, 200), width=6)
    p = prog(t, DURS[0] * 0.75, 0.25)
    if p > 0:
        d.rounded_rectangle((330, 1330, 750, 1440), 30, fill=mix(RED, p))
        ctext(d, 1348, "¿Quién anotó?", font("Black", 52), mix(WHITE, p), 330, 750)
    stamp(d, t)


ACTA = [("Decisión", "Lanzamiento el 15/12", "—", "—"), ("Tarea", "Presupuesto", "Ana", "lun"),
        ("Tarea", "Web nueva", "Leo", "10/12"), ("Tarea", "Mail a clientes", "Vos", "vie"),
        ("Duda", "¿Qué proveedor?", "—", "No se lee")]


def p4s3(im, d, t):
    d.text((90, 330), "Acta de reunión", font=font("Black", 60), fill=WHITE)
    cols = [("Tipo", 190), ("Qué", 380), ("Quién", 160), ("Cuándo", 190)]
    x0, y0, rh = 40, 440, 120
    x = x0
    for name, w in cols:
        d.rectangle((x, y0, x + w, y0 + 90), fill=(40, 60, 100), outline=(70, 90, 130))
        ctext(d, y0 + 22, name, font("Bold", 40), WHITE, x, x + w)
        x += w
    for i, row in enumerate(ACTA):
        p = prog(t, 0.2 + i * DURS[2] * 0.12, 0.25)
        if p <= 0:
            continue
        yy = y0 + 90 + i * rh
        x = x0
        for j, (name, w) in enumerate(cols):
            fill = (255, 243, 196) if row[0] == "Duda" else (255, 255, 255)
            d.rectangle((x, yy, x + w, yy + rh), fill=mix(fill, p), outline=mix((200, 205, 215), p))
            f = font("Bold" if j == 0 else "Medium", 36)
            ctext(d, yy + 38, row[j], f, mix((40, 50, 70), p), x + 6, x + w - 6)
            x += w
    p = prog(t, DURS[2] * 0.8, 0.3)
    if p > 0:
        d.rounded_rectangle((180, 1300, 900, 1410), 30, fill=mix(GREEN, p))
        ctext(d, 1318, "Foto → acta en 10 segundos", font("Black", 50), mix(BG, p), 180, 900)


P4_PROMPT = ("Esta es la foto del pizarrón de la reunión. Armá el acta en una tabla: decisiones, tareas, quién y para "
             "cuándo. Si algo no se lee, marcalo como duda: no inventes.")


# ---------- Parte 5: nota de voz -> mail ----------
import math as _m


def p5s1(im, d, t):
    card(d, (80, 420, 1000, 760), fill=(37, 211, 102), r=40)
    d.ellipse((120, 500, 260, 640), fill=(255, 255, 255))
    d.polygon([(175, 535), (175, 605), (230, 570)], fill=(37, 211, 102))
    for i in range(26):
        h = 20 + 70 * abs(_m.sin(i * 0.9 + t * 6))
        x = 300 + i * 24
        d.rounded_rectangle((x, 570 - h / 2, x + 12, 570 + h / 2), 6, fill=(255, 255, 255))
    d.text((300, 660), "3:12", font=font("Bold", 48), fill=(255, 255, 255))
    p = prog(t, 1.4, 0.3)
    if p > 0:
        d.rounded_rectangle((200, 900, 880, 1020), 30, fill=mix(RED, p))
        ctext(d, 918, "3 MIN DE AUDIO", font("Black", 64), mix(WHITE, p), 200, 880)
        ctext(d, 1080, "↓", font("Black", 110), mix(YEL, p))
        d.rounded_rectangle((260, 1240, 820, 1360), 30, fill=mix(GREEN, p))
        ctext(d, 1258, "MAIL EN 10 s", font("Black", 64), mix(BG, p), 260, 820)
    stamp(d, t)


MAIL5 = ["Hola Laura:", "Te resumo lo que hablamos:", "1. La entrega pasa al jueves 10.", "2. Falta el OK de compras.",
         "3. Necesito 2 personas más.", "¿Me confirmás el punto 2 hoy?", "Gracias, Javi"]


def p5s3(im, d, t):
    card(d, (60, 330, 1020, 1300), fill=(255, 255, 255), outline=GREEN, r=24, width=4)
    d.text((110, 365), "Asunto: Entrega del proyecto", font=font("Black", 44), fill=(30, 40, 60))
    for i, ln in enumerate(MAIL5):
        p = prog(t, 0.15 + i * DURS[2] * 0.09, 0.2)
        if p > 0:
            f = font("Bold" if i in (0, 5) else "Medium", 44)
            d.text((110, 470 + i * 105), ln, font=f, fill=mix((40, 50, 70) if i != 5 else (200, 60, 40), p))


P5_PROMPT = ("Te paso una nota de voz. Convertila en un mail para [A QUIÉN], tono [FORMAL / CERCANO]: saludo, "
             "máximo 3 puntos y qué necesito que me respondan.")

# ---------- Parte 6: mail al inglés formal ----------
BAD6 = "Dear boss, I write you for say that the report is delay because we have many problems with the datas."


def p6s1(im, d, t):
    card(d, (60, 360, 1020, 1150), fill=(255, 255, 255), outline=(210, 215, 225), r=24)
    d.text((110, 395), "Para: CEO (Londres)", font=font("Bold", 42), fill=(30, 40, 60))
    f = font("Medium", 48)
    y = 500
    for ln in wrap(d, BAD6, f, 840):
        d.text((110, y), ln, font=f, fill=(40, 40, 40))
        w_ = d.textlength(ln, font=f)
        for x in range(110, int(110 + w_), 18):
            d.line((x, y + 62, x + 9, y + 68), fill=RED, width=3)
            d.line((x + 9, y + 68, x + 18, y + 62), fill=RED, width=3)
        y += 80
    p = prog(t, 1.5, 0.3)
    if p > 0:
        d.rounded_rectangle((250, 1220, 830, 1330), 30, fill=mix(RED, p))
        ctext(d, 1238, "Inglés de colegio", font("Black", 58), mix(WHITE, p), 250, 830)
    stamp(d, t)


GOOD6 = ("Dear Mr. Collins, I am writing to let you know that the report will be delayed until Thursday, "
         "as we are resolving some data issues. I will keep you updated. Kind regards, Javier")


def p6s3(im, d, t):
    card(d, (60, 330, 1020, 1300), fill=(255, 255, 255), outline=GREEN, r=24, width=4)
    d.text((110, 365), "Listo para mandar", font=font("Black", 50), fill=(30, 40, 60))
    n = int(len(GOOD6) * min(1.0, max(0.0, t / max(0.6, DURS[2] * 0.75))))
    f = font("Medium", 46)
    for i, ln in enumerate(wrap(d, GOOD6[:n], f, 840)):
        d.text((110, 470 + i * 66), ln, font=f, fill=(40, 50, 70))
    p = prog(t, DURS[2] * 0.8, 0.3)
    if p > 0:
        d.rounded_rectangle((250, 1340, 830, 1450), 30, fill=mix(GREEN, p))
        ctext(d, 1358, "Inglés formal ✓", font("Black", 56), mix(BG, p), 250, 830)


P6_PROMPT = ("Pasá este mail a inglés formal, listo para mandar: [TU TEXTO EN CASTELLANO]. Después explicame en "
             "castellano qué dice cada párrafo.")

# ---------- Parte 7: planificar la semana ----------
TASKS7 = ["Informe mensual", "Llamar a Gómez", "Presupuesto 2027", "Revisar contratos", "Mail a proveedores",
          "Reunión de equipo", "Capacitación", "Pagar facturas", "Actualizar web", "Encuesta clientes", "Inventario"]


def p7s1(im, d, t):
    n = int(min(22, 4 + t * 22))
    d.rounded_rectangle((300, 330, 780, 440), 40, fill=RED)
    ctext(d, 345, f"{n} PENDIENTES", font("Black", 56), WHITE, 300, 780)
    for i, task in enumerate(TASKS7):
        col, row = i % 2, i // 2
        x, y = 70 + col * 480, 490 + row * 120
        p = prog(t, i * 0.08, 0.15)
        if p > 0:
            d.rounded_rectangle((x, y, x + 450, y + 95), 16, fill=mix((255, 249, 196), p))
            d.text((x + 25, y + 26), task, font=font("Bold", 38), fill=mix((60, 50, 20), p))
    stamp(d, t)


DAYS7 = [("Lun", ["Pagar facturas", "Informe mensual"]), ("Mar", ["Llamar a Gómez", "Presupuesto 2027"]),
         ("Mié", ["Reunión de equipo", "Contratos"]), ("Jue", ["Proveedores", "Hueco libre"]),
         ("Vie", ["Web", "Cierre semana"])]


def p7s3(im, d, t):
    d.text((90, 330), "Tu semana", font=font("Black", 60), fill=WHITE)
    for i, (day, items) in enumerate(DAYS7):
        p = prog(t, 0.15 + i * DURS[2] * 0.12, 0.25)
        if p <= 0:
            continue
        y = 440 + i * 175
        d.rounded_rectangle((60, y, 220, y + 150), 20, fill=mix((40, 60, 100), p))
        ctext(d, y + 50, day, font("Black", 50), mix(WHITE, p), 60, 220)
        for j, it in enumerate(items):
            x = 240 + j * 390
            urgent = j == 0 and i < 2
            fill = (255, 220, 220) if urgent else ((220, 245, 225) if it == "Hueco libre" else (255, 255, 255))
            d.rounded_rectangle((x, y, x + 370, y + 150), 20, fill=mix(fill, p))
            for k, ln in enumerate(wrap(d, it, font("Bold", 38), 330)):
                d.text((x + 20, y + 30 + k * 48), ln, font=font("Bold", 38), fill=mix((40, 50, 70), p))


P7_PROMPT = ("Estas son mis tareas pendientes y mi agenda de la semana. Tengo [X] horas libres reales por día. "
             "Armá un plan día por día: lo urgente primero y bloques para lo importante.")

# ---------- Short suelto: "Pago 200 dólares de IA y lo anoto como sueldos" (26/11) ----------

def robot(d, cx, cy, s=1.0, a=1.0, color=(96, 165, 250)):
    """Robot-empleado simple (cabeza redondeada, ojos, antena). Propio, no copiado."""
    w, h = int(170 * s), int(140 * s)
    d.line((cx, cy - h // 2 - int(38 * s), cx, cy - h // 2), fill=mix(color, a), width=max(3, int(6 * s)))
    d.ellipse((cx - int(14 * s), cy - h // 2 - int(56 * s), cx + int(14 * s), cy - h // 2 - int(28 * s)), fill=mix(YEL, a))
    d.rounded_rectangle((cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2), int(36 * s), fill=mix(color, a))
    d.rounded_rectangle((cx - int(60 * s), cy - int(36 * s), cx + int(60 * s), cy + int(36 * s)), int(20 * s), fill=mix(BG, a))
    for ex in (-28, 28):
        d.ellipse((cx + int((ex - 12) * s), cy - int(12 * s), cx + int((ex + 12) * s), cy + int(12 * s)), fill=mix(GREEN, a))


def worker_card(d, t, y, name, hour, color):
    card(d, (60, y, 1020, y + 230), fill=CARD, outline=color, r=28, width=4)
    robot(d, 190, y + 125, 0.85, 1.0, color)
    d.text((320, y + 40), name, font=font("Black", 60), fill=WHITE)
    d.rounded_rectangle((320, y + 125, 560, y + 195), 20, fill=mix(color, 0.9))
    d.text((345, y + 133), hour, font=font("Black", 48), fill=BG)
    on = int(t * 2) % 2 == 0
    d.ellipse((900, y + 60, 940, y + 100), fill=GREEN if on else (40, 120, 70))
    d.text((808, y + 120), "activo", font=font("Bold", 38), fill=GREEN)


def v1(im, d, t):
    card(d, (80, 380, 1000, 1360), fill=(255, 255, 255), outline=(210, 215, 225), r=30)
    d.text((130, 420), "Gastos del mes", font=font("Black", 56), fill=(30, 40, 60))
    d.line((130, 510, 950, 510), fill=(225, 228, 235), width=3)
    d.text((130, 560), "IA (Claude y otras)", font=font("Bold", 46), fill=(40, 50, 70))
    d.text((130, 630), "US$ 200 / mes", font=font("Black", 84), fill=(30, 40, 60))
    d.text((130, 800), "Categoría:", font=font("Medium", 42), fill=(110, 120, 140))
    f = font("Black", 92)
    d.text((130, 870), "SOFTWARE", font=f, fill=(150, 155, 165))
    p = prog(t, DURS[0] * 0.45, 0.35)
    if p > 0:
        w_ = d.textlength("SOFTWARE", font=f)
        d.line((120, 930, 120 + (w_ + 20) * p, 930), fill=RED, width=14)
    p2 = prog(t, DURS[0] * 0.7, 0.3)
    if p2 > 0:
        d.rounded_rectangle((130, 1050, 700, 1200), 30, fill=mix((34, 160, 90), p2))
        ctext(d, 1070, "SUELDOS", font("Black", 96), mix(WHITE, p2), 130, 700)
        d.text((740, 1090), "x3", font=font("Black", 80), fill=mix((34, 160, 90), p2))
    stamp(d, t)


VIDS = [("Le pidió a Claude que acelere su wifi", "×429"), ("Repos para no pagar suscripciones", "×25")]


def v2(im, d, t):
    worker_card(d, t, 330, "RADAR", "03:47", (96, 165, 250))
    d.text((90, 620), "Videos que están explotando:", font=font("Bold", 44), fill=MUTED)
    for i, (title, x) in enumerate(VIDS):
        p = prog(t, 0.3 + i * DURS[1] * 0.18, 0.25)
        if p <= 0:
            continue
        y = 720 + i * 260
        card(d, (60, y, 1020, y + 190), fill=mix((255, 255, 255), p), outline=mix((210, 215, 225), p), r=22)
        d.rounded_rectangle((90, y + 30, 250, y + 160), 14, fill=mix((40, 50, 70), p))
        d.polygon([(150, y + 65), (150, y + 125), (200, y + 95)], fill=mix(WHITE, p))
        for j, ln in enumerate(wrap(d, title, font("Bold", 42), 470)):
            d.text((280, y + 40 + j * 52), ln, font=font("Bold", 42), fill=mix((30, 40, 60), p))
        d.rounded_rectangle((790, y + 55, 990, y + 135), 24, fill=mix(RED, p))
        ctext(d, y + 65, x, font("Black", 54), mix(WHITE, p), 790, 990)


NEWS = ["1. Lo nuevo de Claude", "2. Una herramienta gratis", "3. El dato del día"]


def v3(im, d, t):
    worker_card(d, t, 330, "NOVEDADES", "07:41", (245, 181, 68))
    card(d, (60, 620, 1020, 1130), fill=(255, 255, 255), outline=(210, 215, 225), r=24)
    d.text((110, 650), "Guion de hoy", font=font("Black", 50), fill=(30, 40, 60))
    reveal_lines(d, t, DURS[2], NEWS, 760, gap=110, f=font("Medium", 46))
    p = prog(t, DURS[2] * 0.65, 0.3)
    if p > 0:
        d.rounded_rectangle((180, 1180, 900, 1300), 30, fill=mix(GREEN, p))
        ctext(d, 1200, "Programado: 18:00 ✓", font("Black", 58), mix(BG, p), 180, 900)


DAYS = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]


def v4(im, d, t):
    worker_card(d, t, 330, "TURNO NOCHE", "23:13", (167, 139, 250))
    d.text((90, 620), "Calendario de publicaciones", font=font("Bold", 44), fill=MUTED)
    for i, day in enumerate(DAYS):
        col, row = i % 4, i // 4
        x, y = 60 + col * 245, 700 + row * 290
        p = prog(t, 0.2 + i * DURS[3] * 0.09, 0.2)
        card(d, (x, y, x + 225, y + 260), fill=(255, 255, 255), outline=(210, 215, 225), r=20)
        ctext(d, y + 20, day, font("Black", 48), (30, 40, 60), x, x + 225)
        if p > 0:
            d.rounded_rectangle((x + 25, y + 100, x + 200, y + 170), 16, fill=mix((34, 160, 90), p))
            ctext(d, y + 110, "19:00", font("Black", 42), mix(WHITE, p), x + 25, x + 200)
            ctext(d, y + 182, "✓ fijado", font("Bold", 34), mix((34, 160, 90), p), x, x + 225)


def v5(im, d, t):
    for i, c in enumerate([(96, 165, 250), (245, 181, 68), (167, 139, 250)]):
        robot(d, 230 + i * 310, 430, 0.8, 1.0, c)
    ctext(d, 560, "Yo solo apruebo ✓", font("Black", 66), GREEN)
    ctext(d, 720, "COMENTÁ", font("Black", 120), WHITE)
    pulse = 1 + 0.05 * abs(((t * 2) % 2) - 1)
    ctext(d, 860, "GUIA", font("Black", int(200 * pulse)), YEL)
    ctext(d, 1110, "y te mando 10 tareas", font("Bold", 56), WHITE)
    ctext(d, 1185, "que la IA te hace sola, gratis", font("Medium", 48), MUTED)
    by = 1290 + int(25 * abs(((t * 1.6) % 2) - 1))
    cx = W // 2
    d.polygon([(cx - 60, by), (cx + 60, by), (cx, by + 80)], fill=YEL)


# ---------- Parte 8: gráfico desde la planilla (27/11) ----------
SALES8 = [("Ene", 41), ("Feb", 38), ("Mar", 52), ("Abr", 47), ("May", 63), ("Jun", 58)]


def p8s1(im, d, t):
    n = int(min(300, 12 + t * 120))
    d.rounded_rectangle((250, 330, 830, 440), 40, fill=RED)
    ctext(d, 345, f"{n} FILAS", font("Black", 60), WHITE, 250, 830)
    x0, y0, rh = 90, 480, 52
    widths = [90, 200, 260, 250]
    heads = ["#", "Fecha", "Vendedor", "Monto"]
    names = ["Pérez", "Gómez", "Ruiz", "Sosa", "Díaz"]
    off = int(t * 9)
    x = x0
    for w, h in zip(widths, heads):
        d.rectangle((x, y0, x + w, y0 + rh), fill=(225, 230, 238), outline=(200, 205, 215))
        ctext(d, y0 + 10, h, font("ExtraBold", 30), (40, 50, 70), x, x + w)
        x += w
    for i in range(14):
        r_ = i + off + 2
        yy = y0 + (i + 1) * rh
        vals = [str(r_), f"{(r_ * 7) % 28 + 1:02d}/{(r_ // 50) % 6 + 1:02d}", names[r_ % 5], f"{(r_ * 3517) % 90 + 5}.{(r_ * 37) % 10}00"]
        x = x0
        for w, v in zip(widths, vals):
            d.rectangle((x, yy, x + w, yy + rh), fill=(255, 255, 255), outline=(215, 220, 228))
            ctext(d, yy + 10, v, font("Medium", 30), (40, 50, 70), x, x + w)
            x += w
    d.rounded_rectangle((300, 1290, 780, 1390), 30, fill=AMBER)
    ctext(d, 1308, "Reunión en 10 min", font("Black", 46), BG, 300, 780)
    stamp(d, t)


def p8s3(im, d, t):
    d.text((90, 330), "Ventas por mes", font=font("Black", 60), fill=WHITE)
    card(d, (70, 430, 1010, 1130), fill=(255, 255, 255), outline=(200, 205, 215), r=24)
    base, top = 1040, 520
    mx = max(v for _, v in SALES8)
    bw, gap = 110, 37
    for i, (m, v) in enumerate(SALES8):
        p = prog(t, 0.1 + i * DURS[2] * 0.06, 0.3)
        x = 130 + i * (bw + gap)
        h = int((base - top - 60) * v / mx * p)
        best = v == mx
        col = (34, 197, 94) if best else (96, 165, 250)
        if h > 0:
            d.rounded_rectangle((x, base - h, x + bw, base), 12, fill=col)
        ctext(d, base + 20, m, font("Bold", 34), (60, 70, 90), x, x + bw)
        if p >= 1:
            ctext(d, base - h - 50, str(v), font("ExtraBold", 34), (40, 50, 70), x, x + bw)
    pb = prog(t, DURS[2] * 0.5, 0.3)
    if pb > 0:
        d.rounded_rectangle((640, 450, 990, 515), 20, fill=mix((34, 197, 94), pb))
        ctext(d, 462, "★ Mejor mes: mayo", font("Black", 34), mix(WHITE, pb), 640, 990)
    pc = prog(t, DURS[2] * 0.62, 0.3)
    if pc > 0:
        card(d, (70, 1170, 1010, 1380), fill=mix(CARD, pc), outline=mix(AMBER, pc), r=22, width=3)
        d.text((110, 1195), "Para la diapositiva:", font=font("ExtraBold", 38), fill=mix(AMBER, pc))
        for k, ln in enumerate(wrap(d, "Mayo fue el mejor mes: +53 % contra enero.", font("Bold", 42), 860)):
            d.text((110, 1255 + k * 54), ln, font=font("Bold", 42), fill=mix(WHITE, pc))


P8_PROMPT = ("Te paso mi planilla de ventas (Excel). Armá un gráfico de barras de ventas por mes, marcá el mejor mes "
             "y decime en una frase qué conclusión tengo que contar en la reunión.")

# ---------- Parte 9: presupuesto desde la lista de precios (27/11) ----------
PRICES9 = [("Silla de oficina", "45.000"), ("Escritorio 120 cm", "98.000"), ("Lámpara LED", "12.500"), ("Archivero 3 cajones", "63.000"),
           ("Pizarra blanca", "21.000"), ("Perchero", "15.800"), ("Mesa de reunión", "210.000"), ("Biblioteca", "74.000"),
           ("Silla fija", "28.500"), ("Cesto", "4.200"), ("Alfombra", "36.000"), ("Cajonera", "52.000")]
QUOTE9 = [("Silla de oficina", 6, 45000), ("Escritorio 120 cm", 3, 98000), ("Lámpara LED", 6, 12500), ("Archivero 3 cajones", 2, 63000)]


def _m(v):
    return "$ " + f"{v:,}".replace(",", ".")


def p9s1(im, d, t):
    n = int(min(40, 3 + t * 14))
    d.rounded_rectangle((200, 330, 880, 440), 40, fill=RED)
    ctext(d, 345, f"{n} PRODUCTOS", font("Black", 60), WHITE, 200, 880)
    x0, y0, rh = 90, 480, 56
    widths = [80, 520, 300]
    heads = ["#", "Producto", "Precio"]
    off = int(t * 2.2)
    x = x0
    for w, h in zip(widths, heads):
        d.rectangle((x, y0, x + w, y0 + rh), fill=(225, 230, 238), outline=(200, 205, 215))
        ctext(d, y0 + 11, h, font("ExtraBold", 32), (40, 50, 70), x, x + w)
        x += w
    for i in range(10):
        k = (i + off) % len(PRICES9)
        yy = y0 + (i + 1) * rh
        vals = [str(i + off + 1), PRICES9[k][0], "$ " + PRICES9[k][1]]
        x = x0
        for j, (w, v) in enumerate(zip(widths, vals)):
            d.rectangle((x, yy, x + w, yy + rh), fill=(255, 255, 255), outline=(215, 220, 228))
            if j == 1:
                d.text((x + 24, yy + 11), v, font=font("Medium", 32), fill=(40, 50, 70))
            else:
                ctext(d, yy + 11, v, font("Medium", 32), (40, 50, 70), x, x + w)
            x += w
    d.rounded_rectangle((290, 1150, 790, 1250), 30, fill=AMBER)
    ctext(d, 1168, "Para mañana", font("Black", 50), BG, 290, 790)
    stamp(d, t)


def p9s3(im, d, t):
    d.text((90, 330), "Presupuesto", font=font("Black", 60), fill=WHITE)
    card(d, (60, 430, 1020, 1120), fill=(255, 255, 255), outline=(200, 205, 215), r=24)
    cols = [("Producto", 90, 480), ("Cant.", 480, 590), ("Precio", 590, 790), ("Subtotal", 790, 1000)]
    for name, a, b in cols:
        ctext(d, 460, name, font("ExtraBold", 32), (90, 100, 120), a, b) if name != "Producto" else d.text((a, 460), name, font=font("ExtraBold", 32), fill=(90, 100, 120))
    d.line((80, 515, 1000, 515), fill=(210, 215, 225), width=3)
    total = 0
    for i, (prod, q, pr) in enumerate(QUOTE9):
        p = prog(t, 0.15 + i * DURS[2] * 0.08, 0.3)
        if p <= 0:
            continue
        yy = 545 + i * 105
        c = mix((40, 50, 70), p)
        for ln_i, ln in enumerate(wrap(d, prod, font("Bold", 34), 380)):
            d.text((90, yy + ln_i * 42), ln, font=font("Bold", 34), fill=c)
        ctext(d, yy, str(q), font("Medium", 34), c, 480, 590)
        ctext(d, yy, _m(pr), font("Medium", 32), c, 590, 790)
        ctext(d, yy, _m(q * pr), font("Bold", 32), c, 790, 1000)
        total += q * pr
    pt = prog(t, 0.15 + 4 * DURS[2] * 0.08, 0.3)
    if pt > 0:
        d.rounded_rectangle((520, 990, 1000, 1090), 20, fill=mix((34, 197, 94), pt))
        ctext(d, 1012, "TOTAL " + _m(sum(q * p_ for _, q, p_ in QUOTE9)), font("Black", 44), mix(WHITE, pt), 520, 1000)
    pc = prog(t, DURS[2] * 0.62, 0.3)
    if pc > 0:
        card(d, (60, 1160, 1020, 1380), fill=mix(CARD, pc), outline=mix(AMBER, pc), r=22, width=3)
        d.text((100, 1185), "A confirmar:", font=font("ExtraBold", 38), fill=mix(AMBER, pc))
        d.text((100, 1245), "Monitor 27\" (no está en la lista)", font=font("Bold", 40), fill=mix(WHITE, pc))
        d.text((100, 1305), "Revisá las cuentas en tu planilla", font=font("Medium", 34), fill=mix(MUTED, pc))


P9_PROMPT = ("Te paso mi lista de precios y el pedido del cliente. Armá el presupuesto con producto, cantidad, precio y subtotal, "
             "y el total. Usá solo lo que está en la lista: si algo no está, no inventes, ponelo aparte en 'a confirmar'.")


# ---------- Short suelto: "Mi IA encontró un video 713 veces viral" (27/11) ----------

def r1(im, d, t):
    worker_card(d, t, 330, "RADAR", "03:47", (96, 165, 250))
    p = prog(t, 0.4, 0.35)
    card(d, (60, 620, 1020, 1330), fill=(255, 255, 255), outline=(210, 215, 225), r=30)
    d.text((110, 655), "Reporte de esta madrugada", font=font("Bold", 44), fill=(110, 120, 140))
    d.line((110, 730, 970, 730), fill=(225, 228, 235), width=3)
    d.text((110, 770), "1 video encontrado", font=font("Black", 56), fill=mix((30, 40, 60), p))
    n = int(469900 * prog(t, 0.6, DURS[0] * 0.45))
    d.text((110, 870), f"{n:,}".replace(",", ".") + " vistas", font=font("Black", 74), fill=mix((30, 40, 60), p))
    p2 = prog(t, DURS[0] * 0.55, 0.35)
    if p2 > 0:
        s = 1 + 0.25 * (1 - p2)
        f = font("Black", int(190 * s))
        d.rounded_rectangle((110, 1010, 970, 1290), 40, fill=mix(RED, p2))
        ctext(d, 1030, "×713", f, mix(WHITE, p2), 110, 970)
    stamp(d, t)


R2 = [("Video A", "×713", True), ("Video B", "×35", True), ("Video C", "×2,1", False), ("Video D", "×1,4", False), ("Video E", "×0,9", False)]


def r2(im, d, t):
    ctext(d, 330, "LOS CREADORES QUE SIGO", font("Black", 60), WHITE)
    d.rounded_rectangle((190, 425, 890, 520), 30, fill=YEL)
    ctext(d, 443, "Filtro: ≥ 3× su promedio", font("Black", 50), BG, 190, 890)
    for i, (name, x, ok) in enumerate(R2):
        p = prog(t, 0.2 + i * DURS[1] * 0.1, 0.25)
        if p <= 0:
            continue
        y = 570 + i * 160
        card(d, (60, y, 1020, y + 135), fill=mix((255, 255, 255), p), outline=mix((210, 215, 225), p), r=22)
        d.rounded_rectangle((90, y + 25, 200, y + 110), 14, fill=mix((40, 50, 70), p))
        d.polygon([(130, y + 45), (130, y + 90), (170, y + 67)], fill=mix(WHITE, p))
        d.text((230, y + 35), name, font=font("Bold", 50), fill=mix((30, 40, 60), p))
        d.text((560, y + 30), x, font=font("Black", 62), fill=mix(RED if ok else (150, 155, 165), p))
        pc = prog(t, DURS[1] * 0.6, 0.3)
        if ok and pc > 0:
            d.text((870, y + 25), "✓", font=font("Black", 76), fill=mix((34, 160, 90), pc))
        elif not ok and pc > 0:
            d.line((90, y + 68, 90 + 900 * pc, y + 68), fill=RED, width=10)


R3 = ["Gancho: la primera frase, literal", "Estructura: los 5 pasos del video", "Por qué pegó", "Idea para mi canal"]


def r3(im, d, t):
    ctext(d, 330, "LO BAJA Y LO TRANSCRIBE", font("Black", 60), WHITE)
    card(d, (60, 450, 1020, 1350), fill=(255, 255, 255), outline=(210, 215, 225), r=30)
    d.text((110, 490), "radar-virales.md", font=font("Black", 50), fill=(30, 40, 60))
    d.text((110, 560), "27/11 · 03:47", font=font("Medium", 40), fill=(110, 120, 140))
    d.line((110, 625, 970, 625), fill=(225, 228, 235), width=3)
    for i, txt in enumerate(R3):
        p = prog(t, 0.3 + i * DURS[2] * 0.17, 0.25)
        if p <= 0:
            continue
        y = 670 + i * 165
        head, _, rest = txt.partition(":")
        d.text((110, y), "## " + head, font=font("Black", 52), fill=mix((205, 110, 70), p))
        if rest:
            d.text((140, y + 68), rest.strip(), font=font("Medium", 40), fill=mix((60, 70, 90), p))
        else:
            d.rounded_rectangle((140, y + 80, 140 + int(620 * p), y + 105), 10, fill=mix((220, 225, 235), p))


def r4(im, d, t):
    worker_card(d, t, 330, "VIRAL DEL DÍA", "21:43", (245, 181, 68))
    steps = ["Agarra la mejor idea", "Escribe el guion", "Graba la voz y arma el video"]
    for i, s in enumerate(steps):
        p = prog(t, 0.2 + i * DURS[3] * 0.14, 0.25)
        if p <= 0:
            continue
        y = 630 + i * 110
        d.text((110, y), "✓", font=font("Black", 56), fill=mix(GREEN, p))
        d.text((190, y + 6), s, font=font("Bold", 50), fill=mix(WHITE, p))
    pr = prog(t, DURS[3] * 0.35, DURS[3] * 0.3)
    d.rounded_rectangle((110, 990, 970, 1060), 30, fill=CARD, outline=LINE, width=3)
    if pr > 0:
        d.rounded_rectangle((110, 990, 110 + int(860 * pr), 1060), 30, fill=AMBER)
    ctext(d, 1075, f"Render {int(pr * 100)}%", font("Bold", 42), MUTED)
    p2 = prog(t, DURS[3] * 0.72, 0.3)
    if p2 > 0:
        d.rounded_rectangle((180, 1170, 900, 1300), 34, fill=mix(GREEN, p2))
        ctext(d, 1195, "Yo solo apruebo ✓", font("Black", 62), mix(BG, p2), 180, 900)


def r5(im, d, t):
    for i, c in enumerate([(96, 165, 250), (245, 181, 68)]):
        robot(d, 390 + i * 300, 430, 0.8, 1.0, c)
    ctext(d, 600, "COMENTÁ", font("Black", 120), WHITE)
    pulse = 1 + 0.05 * abs(((t * 2) % 2) - 1)
    ctext(d, 740, "GUIA", font("Black", int(200 * pulse)), YEL)
    ctext(d, 990, "y te mando 10 tareas más", font("Bold", 56), WHITE)
    ctext(d, 1065, "que la IA te hace sola, gratis", font("Medium", 48), MUTED)
    by = 1200 + int(25 * abs(((t * 1.6) % 2) - 1))
    cx = W // 2
    d.polygon([(cx - 60, by), (cx + 60, by), (cx, by + 80)], fill=YEL)



PARTS = {
    "radar": [r1, r2, r3, r4, r5],
    9: [p9s1, chat_scene("Le pasás la lista", "Armame el presupuesto con este pedido: 6 sillas, 3 escritorios, 6 lámparas, 2 archiveros y un monitor.", "Adjunto: precios.xlsx"), p9s3, prompt_scene(P9_PROMPT), s5],
    "sueldos": [v1, v2, v3, v4, v5],
    8: [p8s1, chat_scene("Le pasás el Excel", "Armame un gráfico de ventas por mes para la reunión.", "Adjunto: ventas.xlsx"), p8s3, prompt_scene(P8_PROMPT), s5],
    1: [s1, s2, s3, s4, s5],
    2: [p2s1, chat_scene("Se los pegás a Claude", "Resumime estos 40 mails en 5 renglones: qué es urgente y a quién contesto primero.", "Adjunto: 40 mails"), p2s3, prompt_scene(P2_PROMPT), s5],
    3: [p3s1, chat_scene("Se lo pasás a Claude", "Ayudame a contestarle sin pelear. Puedo mandarlo el jueves y devolverle el envío.", "Adjunto: mail"), p3s3, prompt_scene(P3_PROMPT), s5],
    5: [p5s1, chat_scene("Le pasás el audio", "Convertí esta nota de voz en un mail para mi jefa, tono formal y corto.", "Audio: 3:12"), p5s3, prompt_scene(P5_PROMPT), s5],
    6: [p6s1, chat_scene("Lo escribís en castellano", "Pasalo a inglés formal: le aviso al CEO que el informe se atrasa hasta el jueves por problemas con los datos.", None), p6s3, prompt_scene(P6_PROMPT), s5],
    7: [p7s1, chat_scene("Le pegás la lista", "Estas son mis 22 tareas y mi agenda. Armame la semana: lo urgente primero.", "Adjunto: agenda.pdf"), p7s3, prompt_scene(P7_PROMPT), s5],
    4: [p4s1, chat_scene("Le mandás la foto", "Armame el acta de esta reunión con tareas, responsables y fechas.", "Foto: pizarrón.jpg"), p4s3, prompt_scene(P4_PROMPT), s5],
}
FNS = PARTS[PART]

if __name__ == "__main__":
    out = os.path.join(HERE, "scenes")
    os.makedirs(out, exist_ok=True)
    for k, (fn, dur) in enumerate(zip(FNS, DURS)):
        name = f"s{k + 1}"
        f = (lambda kk, ff: (lambda tt: frame(kk, tt, ff)))(k, fn)
        if sys.argv[2:] == ["frames"]:
            for j, tt in enumerate([0.3, dur * 0.5, dur - 0.05]):
                f(tt).save(os.path.join(out, f"{name}_{j}.jpg"), quality=80)
        else:
            r.render(name, f, dur, out)
    print("done")
