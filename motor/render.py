#!/usr/bin/env python3
"""Render the 'Comenta IA' reel scenes (1080x1920, 30 fps), one mp4 per scene."""
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
BG = (15, 27, 45)
CARD = (22, 38, 61)
LINE = (42, 59, 85)
WHITE = (255, 255, 255)
MUTED = (175, 192, 214)
AMBER = (245, 181, 68)
GREEN = (74, 222, 128)
RED = (248, 113, 113)
F = os.path.expanduser("~/Pictures/Javi Automates/Reels/motor/")
OUT = sys.argv[1] if len(sys.argv) > 1 else "scenes"
GUIDE_DIR = "/home/claude/guia"


def font(weight, size):
    return ImageFont.truetype(F + f"Inter-{weight}.otf", size)


def ease(x):
    x = max(0.0, min(1.0, x))
    return 1 - (1 - x) ** 3


def prog(t, start, dur):
    return ease((t - start) / dur)


def ctext(d, y, text, f, fill=WHITE, x=None):
    w = d.textlength(text, font=f)
    d.text(((W - w) / 2 if x is None else x, y), text, font=f, fill=fill)


def headline(d, t, text, color=AMBER, y=150):
    """Big hook text, visible from frame 0 with a quick pop."""
    p = prog(t, 0, 0.25)
    size = int(92 + 8 * (1 - p))
    f = font("Black", size)
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        ctext(d, y + i * (size + 12), ln, f, color)


def card(d, box, fill=CARD, outline=LINE, r=28, width=3):
    d.rounded_rectangle(box, r, fill=fill, outline=outline, width=width)


def label(d):
    f = font("Medium", 26)
    txt = "Voz generada con IA"
    w = d.textlength(txt, font=f)
    d.rounded_rectangle((W - w - 70, H - 120, W - 30, H - 66), 14, fill=(0, 0, 0))
    d.text((W - w - 50, H - 110), txt, font=f, fill=MUTED)


def brand(d):
    f = font("Bold", 30)
    ctext(d, 70, "JAVI AUTOMATES", f, MUTED)


# ---------- scenes ----------

def s1(t):
    """40 pages -> summary in 5 points (result visible at frame 0)."""
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    brand(d)
    headline(d, t, "40 PÁGINAS\n→ 10 SEGUNDOS")
    # document stack (left, small)
    shrink = prog(t, 0.0, 1.2)
    sx, sy = 90, 560
    for i in range(5, -1, -1):
        off = i * int(14 - 8 * shrink)
        card(d, (sx + off, sy + off, sx + 300 + off, sy + 400 + off), fill=(235, 240, 247), outline=(200, 210, 225), r=10)
    for k in range(9):
        d.rounded_rectangle((sx + 30, sy + 50 + k * 36, sx + 270 - (k % 3) * 40, sy + 62 + k * 36), 6, fill=(190, 200, 215))
    d.text((sx + 30, sy + 420 + 70), "contrato.pdf", font=font("SemiBold", 34), fill=WHITE)
    d.text((sx + 30, sy + 470 + 70), "40 páginas", font=font("Regular", 30), fill=MUTED)
    # arrow
    ax = 430
    d.polygon([(ax, 740), (ax + 60, 770), (ax, 800)], fill=AMBER)
    # summary card (right, big)
    cx0, cy0, cx1 = 520, 470, 1010
    card(d, (cx0, cy0, cx1, cy0 + 900), fill=CARD, outline=AMBER, r=30, width=4)
    d.text((cx0 + 36, cy0 + 34), "Resumen", font=font("ExtraBold", 46), fill=WHITE)
    d.text((cx0 + 36, cy0 + 96), "en 5 puntos", font=font("Medium", 32), fill=MUTED)
    items = ["Plazo: 24 meses", "Pago: día 10 de cada mes", "Aumento cada 6 meses", "Multa por rescisión", "Riesgo: letra chica pág. 31"]
    for i, it in enumerate(items):
        p = prog(t, 0.05 + i * 0.12, 0.35)
        y = cy0 + 190 + i * 136
        x = cx0 + 36 + int(40 * (1 - p))
        col = tuple(int(BG[j] + (c - BG[j]) * p) for j, c in enumerate(WHITE))
        dot = tuple(int(BG[j] + (c - BG[j]) * p) for j, c in enumerate(AMBER if i == 4 else GREEN))
        d.ellipse((x, y + 14, x + 22, y + 36), fill=dot)
        f = font("SemiBold", 36)
        lines, cur = [], ""
        for w_ in it.split():
            test = (cur + " " + w_).strip()
            if d.textlength(test, font=f) > 380 and cur:
                lines.append(cur)
                cur = w_
            else:
                cur = test
        lines.append(cur)
        for li, ln in enumerate(lines):
            d.text((x + 40, y + li * 46), ln, font=f, fill=col)
    # timer chip
    secs = min(10.0, t * 3.4)
    chip = f"{secs:4.1f} s"
    d.rounded_rectangle((cx0 + 300, cy0 + 40, cx0 + 460, cy0 + 100), 20, fill=AMBER)
    d.text((cx0 + 322, cy0 + 50), chip, font=font("Bold", 34), fill=BG)
    label(d)
    return im


def s2(t):
    """'Y hay más': grid of tasks flipping in."""
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    brand(d)
    headline(d, t, "Y HAY MÁS", WHITE, y=200)
    tasks = ["Mails", "Planillas", "Reuniones", "PDFs", "Presentaciones", "Clientes", "Presupuestos", "Manuales", "Recordatorios", "Formularios"]
    for i, name in enumerate(tasks):
        p = prog(t, 0.15 + i * 0.18, 0.4)
        col, row = i % 2, i // 2
        x0 = 90 + col * 470
        y0 = 450 + row * 250
        dy = int(60 * (1 - p))
        fill = tuple(int(BG[j] + (c - BG[j]) * p) for j, c in enumerate(CARD))
        out = tuple(int(BG[j] + (c - BG[j]) * p) for j, c in enumerate(AMBER if p > 0.99 else LINE))
        card(d, (x0, y0 + dy, x0 + 430, y0 + 200 + dy), fill=fill, outline=out, r=26)
        num = f"{i + 1:02d}"
        tc = tuple(int(BG[j] + (c - BG[j]) * p) for j, c in enumerate(AMBER))
        wc = tuple(int(BG[j] + (c - BG[j]) * p) for j, c in enumerate(WHITE))
        d.text((x0 + 34, y0 + 30 + dy), num, font=font("Black", 44), fill=tc)
        d.text((x0 + 34, y0 + 110 + dy), name, font=font("Bold", 40), fill=wc)
    label(d)
    return im


def before_after(t, title, before_fn, after_fn):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    brand(d)
    headline(d, t, title, AMBER, y=180)
    p = prog(t, 0.3 * SCENE_DUR, min(0.5, 0.3 * SCENE_DUR))
    # before card slides up and fades, after card slides in
    by = 420
    ay = 1300 - int(840 * p)
    before_fn(im, d, by, 1 - p)
    after_fn(im, d, ay, p)
    label(d)
    return im


def mix(c, a):
    return tuple(int(BG[j] + (c[j] - BG[j]) * a) for j in range(3))


def mail_before(im, d, y, a):
    card(d, (80, y, 1000, y + 560), fill=mix((245, 247, 250), a), outline=mix(RED, a), r=26, width=4)
    d.text((120, y + 40), "De: Martín (cliente)", font=font("SemiBold", 34), fill=mix((60, 70, 90), a))
    d.text((120, y + 100), "Asunto: ¡Esto es inaceptable!", font=font("ExtraBold", 40), fill=mix((180, 30, 30), a))
    body = ["Hace dos semanas que espero", "la factura corregida y nadie", "me responde. Si mañana no", "está, cancelo el servicio."]
    for i, ln in enumerate(body):
        d.text((120, y + 190 + i * 70), ln, font=font("Regular", 38), fill=mix((40, 50, 70), a))


def mail_after(im, d, y, a):
    card(d, (80, y, 1000, y + 640), fill=mix(CARD, a), outline=mix(GREEN, a), r=26, width=4)
    d.text((120, y + 40), "Respuesta lista ✓", font=font("ExtraBold", 40), fill=mix(GREEN, a))
    body = ["Hola Martín, tenés razón y", "te pido disculpas por la demora.", "Te mando la factura corregida", "hoy antes de las 18 h y te", "aviso apenas salga."]
    for i, ln in enumerate(body):
        d.text((120, y + 130 + i * 70), ln, font=font("Medium", 38), fill=mix(WHITE, a))
    d.rounded_rectangle((120, y + 520, 400, y + 600), 20, fill=mix(AMBER, a))
    d.text((170, y + 537), "Enviar", font=font("Bold", 38), fill=mix(BG, a) if a > 0.5 else BG)


def table(d, x, y, rows, widths, a, head_fill, cell_colors=None, rh=86):
    xs = [x]
    for w in widths:
        xs.append(xs[-1] + w)
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            fill = head_fill if r == 0 else (cell_colors.get((r, c), CARD) if cell_colors else CARD)
            d.rectangle((xs[c], y + r * rh, xs[c + 1], y + (r + 1) * rh), fill=mix(fill, a), outline=mix(LINE, a), width=2)
            f = font("Bold" if r == 0 else "Medium", 32)
            col = BG if r == 0 else WHITE
            if cell_colors and (r, c) in cell_colors and cell_colors[(r, c)] == AMBER:
                col = BG
            d.text((xs[c] + 18, y + r * rh + 24), val, font=f, fill=mix(col, a) if a > 0.05 else BG)


def sheet_before(im, d, y, a):
    rows = [["Cliente", "Fecha"], ["ana lopez", "3/11/26"], ["ANA LOPEZ", "2026-11-03"], ["Pedro Ruiz", "nov 5"], ["pedro ruiz", "05.11.2026"], ["Lucía Gómez", "—"]]
    red = {(2, 0): (90, 30, 40), (2, 1): (90, 30, 40), (4, 0): (90, 30, 40), (4, 1): (90, 30, 40), (5, 1): (90, 30, 40)}
    table(d, 110, y, rows, [460, 400], a, MUTED, red)


def sheet_after(im, d, y, a):
    rows = [["Cliente", "Fecha"], ["Ana López", "03/11/2026"], ["Pedro Ruiz", "05/11/2026"], ["Lucía Gómez", "FALTA DATO"]]
    cc = {(3, 1): AMBER}
    table(d, 110, y, rows, [460, 400], a, GREEN, cc)
    d.text((110, y + 4 * 86 + 30), "2 duplicados borrados ✓", font=font("SemiBold", 36), fill=mix(GREEN, a))


def notes_before(im, d, y, a):
    card(d, (80, y, 1000, y + 560), fill=mix((250, 240, 200), a), outline=mix((220, 200, 140), a), r=20, width=3)
    lines = ["- presupuesto nuevo?? hablar", "- Sofi ve lo del proveedor", "- lanzar web antes de fin de mes", "- alguien revisa contrato", "- reunión de nuevo el jueves?"]
    for i, ln in enumerate(lines):
        d.text((120, y + 50 + i * 95), ln, font=font("Medium", 38), fill=mix((70, 60, 30), a))


def notes_after(im, d, y, a):
    rows = [["Tarea", "Quién", "Para"], ["Proveedor", "Sofi", "18/11"], ["Lanzar web", "Equipo", "30/11"], ["Revisar contrato", "A DEFINIR", "A DEFINIR"]]
    cc = {(3, 1): AMBER, (3, 2): AMBER}
    table(d, 60, y, rows, [400, 270, 290], a, GREEN, cc)


def s3(t):
    return before_after(t, "MAILS DIFÍCILES ✓", mail_before, mail_after)


def s4(t):
    return before_after(t, "PLANILLAS ✓", sheet_before, sheet_after)


def s5(t):
    return before_after(t, "REUNIONES ✓", notes_before, notes_after)


_pages = {}


def page(n, h):
    key = (n, h)
    if key not in _pages:
        p = Image.open(f"{GUIDE_DIR}/pg-{n:02d}.png").convert("RGB")
        _pages[key] = p.resize((int(p.width * h / p.height), h), Image.LANCZOS)
    return _pages[key]


def s6(t):
    """Guide cover + pages fanning out."""
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    brand(d)
    headline(d, t, "GUÍA GRATIS\n10 TAREAS", AMBER, y=150)
    order = [5, 4, 3]
    for i, n in enumerate(order):
        p = prog(t, 0.4 + i * 0.35, 0.6)
        pg = page(n, 980)
        dx = int((i + 1) * 70 * p)
        x = (W - pg.width) // 2 + dx
        y = 520 + int(30 * (i + 1) * p)
        im.paste(pg, (x, y))
        d.rectangle((x, y, x + pg.width, y + pg.height), outline=LINE, width=3)
    cover = page(1, 1040)
    x = (W - cover.width) // 2 - 60
    im.paste(cover, (x, 480))
    d.rectangle((x, 480, x + cover.width, 480 + cover.height), outline=AMBER, width=5)
    f = font("Bold", 40)
    ctext(d, 1620, "Con el prompt listo para copiar", f, WHITE)
    label(d)
    return im


def s7(t):
    """CTA: comment IA."""
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    brand(d)
    pulse = 1 + 0.04 * abs(((t * 2) % 2) - 1)
    f = font("Black", int(150 * pulse))
    ctext(d, 420, "COMENTÁ", f, WHITE)
    f2 = font("Black", int(330 * pulse))
    ctext(d, 600, "\"IA\"", f2, AMBER)
    # comment bubble typing IA
    typed = "IA"[: max(0, min(2, int((t - 0.6) * 4)))]
    card(d, (120, 1130, 960, 1290), fill=(245, 247, 250), outline=(220, 225, 235), r=40)
    d.ellipse((150, 1160, 250, 1260), fill=(200, 208, 220))
    d.ellipse((182, 1178, 218, 1214), fill=(245, 247, 250))
    d.pieslice((165, 1215, 235, 1285), 180, 360, fill=(245, 247, 250))
    d.text((280, 1170), "Agregá un comentario…" if not typed else typed + ("|" if int(t * 3) % 2 else ""), font=font("SemiBold", 56 if typed else 44), fill=(40, 50, 70) if typed else (150, 160, 175))
    ctext(d, 1360, "y te la mando por mensaje", font("Bold", 52), WHITE)
    # arrow down bouncing
    by = 1500 + int(25 * abs(((t * 1.6) % 2) - 1))
    cx = W // 2
    d.rectangle((cx - 16, by, cx + 16, by + 120), fill=AMBER)
    d.polygon([(cx - 70, by + 110), (cx + 70, by + 110), (cx, by + 200)], fill=AMBER)
    label(d)
    return im


import json as _json
_D = _json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "durs.json")))
SCENES = list(zip(["s1", "s2", "s3", "s4", "s5", "s6", "s7"], [s1, s2, s3, s4, s5, s6, s7], _D))
SCENE_DUR = 5.0


def render(name, fn, dur, out_dir):
    global SCENE_DUR
    SCENE_DUR = dur
    tmp = os.path.join(out_dir, f"{name}.tmp.mp4")
    final = os.path.join(out_dir, f"{name}.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", tmp]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    n = int(round(dur * FPS))
    for i in range(n):
        p.stdin.write(fn(i / FPS).tobytes())
    p.stdin.close()
    if p.wait() == 0:
        os.replace(tmp, final)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    only = sys.argv[2:] if len(sys.argv) > 2 else None
    if only == ["frames"]:
        for name, fn, dur in SCENES:
            fn(min(dur - 0.1, 2.5) if name not in ("s3","s4","s5") else 0.8 if False else dur-0.1).save(os.path.join(OUT, f"{name}_frame.jpg"), quality=85)
    else:
        for name, fn, dur in SCENES:
            if only and name not in only:
                continue
            render(name, fn, dur, OUT)
            print("done", name)
