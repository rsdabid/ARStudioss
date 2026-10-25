# Graphic asset builders (PIL -> float32 RGBA numpy, straight alpha, 0..1)
import numpy as np, cv2, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Fonts ship with the skill in assets/fonts (SIL Open Font License).
FD = os.environ.get('FONTDIR') or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'fonts')
CAP_FONT = os.path.join(FD, 'Unbounded-Black.woff')


def ui_font(weight, size):
    names = {'regular': 'Inter-Regular', 'medium': 'Inter-Medium', 'semibold': 'Inter-Medium', 'bold': 'Inter-Bold'}
    return ImageFont.truetype(os.path.join(FD, names[weight] + '.otf'), size)


K = 1.0


def _fin(im, w, h):
    return im.resize((max(1, int(round(w * K))), max(1, int(round(h * K)))), Image.LANCZOS)


def to_np(im):
    return np.asarray(im.convert('RGBA')).astype(np.float32) / 255.0


def hexrgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def vgrad(w, h, top, bot):
    t = np.linspace(0, 1, h)[:, None, None]
    a = np.array(top, np.float32)[None, None]; b = np.array(bot, np.float32)[None, None]
    return np.repeat((a * (1 - t) + b * t), w, axis=1)


def text_mask(text, size, shear=0.19, squash=0.92, font=CAP_FONT):
    ft = ImageFont.truetype(font, size)
    l, t, r, b = ft.getbbox(text)
    pad = int(size * 0.6)
    im = Image.new('L', (r - l + pad * 2, b - t + pad * 2), 0)
    ImageDraw.Draw(im).text((pad - l, pad - t), text, font=ft, fill=255)
    w, h = im.size
    im = im.transform((w, h), Image.AFFINE, (1, shear, -shear * h * 0.5, 0, 1, 0), Image.BICUBIC)
    im = im.resize((w, max(1, int(h * squash))), Image.LANCZOS)
    a = np.asarray(im).astype(np.float32) / 255
    ys, xs = np.where(a > 0.02)
    return a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]


def fit_size(text, maxw, maxsize, **kw):
    s = maxsize
    while s > 20:
        if text_mask(text, s, **kw).shape[1] <= maxw: return s
        s -= 4
    return s


PALETTE = {
    'blue':    ('#7FD6FF', '#0B7BFF', '#1E8CFF'),
    'green':   ('#E3FF5C', '#5FD11B', '#7BE52C'),
    'yellow':  ('#FFE15A', '#FF9A00', '#FFB300'),
    'red':     ('#FF7A5C', '#E8231B', '#FF3020'),
    'magenta': ('#FF8CF5', '#C02BFF', '#E040FF'),
    'white':   ('#FFFFFF', '#C9D0DA', '#FFFFFF'),
}


def caption(l1, l2, color, w2max=900, s2max=128):
    """Two-line caption: white line 1, coloured line 2; returns (rgba, glow_rgb)."""
    s2 = fit_size(l2, w2max, s2max)
    m2 = text_mask(l2, s2)
    s1 = min(fit_size(l1, 860, int(s2 * 0.80)), int(s2 * 0.80))
    m1 = text_mask(l1, s1)
    gap = -int(s2 * 0.02)
    pad = 70
    w = max(m1.shape[1], m2.shape[1]) + pad * 2
    h = m1.shape[0] + m2.shape[0] + gap + pad * 2
    A = np.zeros((h, w), np.float32); C = np.zeros((h, w, 3), np.float32)
    def put(m, top, ct, cb):
        x = (w - m.shape[1]) // 2 + (int(m.shape[0] * 0.08) if m is m1 else 0)
        g = vgrad(m.shape[1], m.shape[0], [c / 255 for c in hexrgb(ct)], [c / 255 for c in hexrgb(cb)])
        sl = (slice(top, top + m.shape[0]), slice(x, x + m.shape[1]))
        C[sl] = C[sl] * (1 - m[..., None]) + g * m[..., None]
        A[sl] = np.maximum(A[sl], m)
    t1 = pad; t2 = pad + m1.shape[0] + gap
    put(m2, t2, *PALETTE[color][:2]); put(m1, t1, *PALETTE['white'][:2])
    # inner bottom shading (subtle bevel look of the reference type)
    sh = np.clip(cv2.GaussianBlur(A, (0, 0), 3) - np.roll(cv2.GaussianBlur(A, (0, 0), 3), -4, axis=0), 0, 1)
    C = C * (1 - 0.35 * sh[..., None])
    glowc = np.array(hexrgb(PALETTE[color][2]), np.float32) / 255
    glow = cv2.GaussianBlur(A, (0, 0), 16) * 0.75
    shadow = np.clip(np.maximum(cv2.GaussianBlur(A, (0, 0), 12) * 1.4, cv2.GaussianBlur(A, (0, 0), 3) * 1.2), 0, 0.9)
    out = np.zeros((h, w, 4), np.float32)
    # layer: shadow (black) -> glow (colour) -> text
    base_a = shadow + glow * (1 - shadow)
    base_c = (glowc[None, None] * glow[..., None]) / np.maximum(base_a[..., None], 1e-4)
    out[..., :3] = C * A[..., None] + base_c * (1 - A[..., None])
    out[..., 3] = A + base_a * (1 - A)
    return out, glowc


def rounded(w, h, r, fill, outline=None, ow=0, scale=2):
    im = Image.new('RGBA', (w * scale, h * scale), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w * scale - 1, h * scale - 1), r * scale, fill=fill, outline=outline, width=ow * scale)
    return _fin(im, w, h)


def star(cx, cy, R, r):
    pts = []
    for i in range(10):
        a = -np.pi / 2 + i * np.pi / 5
        rr = R if i % 2 == 0 else r
        pts.append((cx + rr * np.cos(a), cy + rr * np.sin(a)))
    return pts


def star_pill(nfill, tagcol, border):
    w, h, S = 780, 110, 3
    im = Image.new('RGBA', ((w + 60) * S, (h + 60) * S), (0, 0, 0, 0))
    glow = Image.new('RGBA', im.size, (0, 0, 0, 0))
    ImageDraw.Draw(glow).rounded_rectangle((30 * S, 30 * S, (30 + w) * S, (30 + h) * S), h // 2 * S, outline=border + (255,), width=14 * S)
    glow = glow.filter(ImageFilter.GaussianBlur(14 * S))
    im.alpha_composite(glow)
    body = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(body)
    d.rounded_rectangle((30 * S, 30 * S, (30 + w) * S, (30 + h) * S), h // 2 * S, fill=(246, 248, 255, 255), outline=border + (255,), width=6 * S)
    im.alpha_composite(body)
    d = ImageDraw.Draw(im)
    for i in range(5):
        cx = (30 + 64 + i * 74) * S; cy = (30 + h / 2) * S
        filled = i < nfill
        d.polygon(star(cx, cy, 30 * S, 13 * S), fill=(255, 196, 40, 255) if filled else (226, 226, 232, 255),
                  outline=(214, 140, 10, 255) if filled else (205, 205, 214, 255))
    tw, th = 124, 50
    x0 = (30 + w - 26 - tw) * S; y0 = int((30 + h / 2 - th / 2) * S)
    d.rounded_rectangle((x0, y0, x0 + tw * S, y0 + th * S), th // 2 * S, fill=tagcol + (255,))
    f = ui_font('medium', 22 * S)
    d.text((x0 + tw * S / 2, y0 + th * S / 2), 'Best', font=f, fill=(255, 255, 255, 255) if tagcol[1] < 200 else (30, 60, 20, 255), anchor='mm')
    return to_np(_fin(im, w + 60, h + 60))


def magnifier():
    S = 3; R = 78
    im = Image.new('RGBA', (360 * S, 360 * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    cx, cy = 230 * S, 130 * S
    # handle (down-left)
    ang = np.deg2rad(135)
    p0 = (cx + (R + 4) * S * np.cos(ang), cy + (R + 4) * S * np.sin(ang))
    p1 = (cx + (R + 120) * S * np.cos(ang), cy + (R + 120) * S * np.sin(ang))
    d.line([p0, p1], fill=(40, 42, 48, 255), width=22 * S)
    d.line([p0, (cx + (R + 30) * S * np.cos(ang), cy + (R + 30) * S * np.sin(ang))], fill=(150, 150, 160, 255), width=26 * S)
    d.ellipse((cx - R * S, cy - R * S, cx + R * S, cy + R * S), fill=(235, 240, 250, 60), outline=(240, 240, 245, 255), width=7 * S)
    hl = Image.new('RGBA', im.size, (0, 0, 0, 0))
    ImageDraw.Draw(hl).arc((cx - (R - 18) * S, cy - (R - 18) * S, cx + (R - 18) * S, cy + (R - 18) * S), 200, 260, fill=(255, 255, 255, 170), width=8 * S)
    im.alpha_composite(hl.filter(ImageFilter.GaussianBlur(3 * S)))
    return to_np(_fin(im, 360, 360)), (230, 130), R


def badge(text='AD'):
    S = 3; w = 110
    im = Image.new('RGBA', (w * S, (w + 26) * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    c = w * S / 2
    d.polygon([(c - 16 * S, 88 * S), (c + 16 * S, 88 * S), (c, 120 * S)], fill=(255, 255, 255, 255))
    d.ellipse((6 * S, 6 * S, (w - 6) * S, (w - 6) * S), fill=(255, 255, 255, 255))
    inner = Image.new('RGBA', im.size, (0, 0, 0, 0)); di = ImageDraw.Draw(inner)
    g = vgrad(im.size[0], im.size[1], (0.62, 0.86, 1.0), (0.10, 0.45, 0.95))
    mask = Image.new('L', im.size, 0); ImageDraw.Draw(mask).ellipse((14 * S, 14 * S, (w - 14) * S, (w - 14) * S), fill=255)
    gi = Image.fromarray((np.dstack([g, np.ones(g.shape[:2])]) * 255).astype(np.uint8), 'RGBA')
    im.paste(gi, (0, 0), mask)
    d = ImageDraw.Draw(im)
    d.text((c, c), text, font=ui_font('bold', 34 * S), fill=(255, 255, 255, 255), anchor='mm')
    return to_np(_fin(im, w, w + 26))


def video_card(frame_bgr, w=250, h=440):
    """Portrait thumbnail card built from the user's own footage."""
    fh, fw = frame_bgr.shape[:2]
    tw = int(fw * 0.62); th = int(tw * h / w)
    y0 = 170; x0 = (fw - tw) // 2
    crop = frame_bgr[y0:y0 + th, x0:x0 + tw]
    crop = cv2.resize(crop, (w, h), interpolation=cv2.INTER_AREA)
    rgb = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(rgb).convert('RGBA')
    mask = Image.new('L', (w * 2, h * 2), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, w * 2 - 1, h * 2 - 1), 36, fill=255)
    im.putalpha(mask.resize((w, h), Image.LANCZOS))
    border = rounded(w, h, 18, None, (255, 255, 255, 140), 2)
    im.alpha_composite(border)
    return to_np(im)


def question_mark(size=190):
    m = text_mask('?', size, shear=0.12, squash=1.0)
    h, w = m.shape; pad = 30
    out = np.zeros((h + pad * 2, w + pad * 2, 4), np.float32)
    g = vgrad(w, h, (1.0, 0.45, 0.35), (0.80, 0.06, 0.05))
    # extruded 3D look: dark offset copy
    dark = np.zeros_like(out[..., 3]); dark[pad + 8:pad + 8 + h, pad + 6:pad + 6 + w] = m
    out[..., :3] = np.array([0.45, 0.02, 0.02]); out[..., 3] = dark
    sl = (slice(pad, pad + h), slice(pad, pad + w))
    out[sl][..., :3] = out[sl][..., :3] * (1 - m[..., None]) + g * m[..., None]
    out[sl][..., 3] = np.maximum(out[sl][..., 3], m)
    return out


def neon_question(size=520):
    m = text_mask('?', size, shear=0.1, squash=1.0)
    pad = 60
    a = np.pad(m, pad)
    edge = np.clip(cv2.dilate(a, np.ones((15, 15))) - cv2.erode(a, np.ones((15, 15))), 0, 1)
    core = cv2.GaussianBlur(edge, (0, 0), 1.5)
    glow = cv2.GaussianBlur(edge, (0, 0), 18)
    out = np.zeros(a.shape + (4,), np.float32)
    col = np.array([1.0, 0.18, 0.12])
    A = np.clip(core + glow * 1.4, 0, 1)
    out[..., :3] = col * (1 - core[..., None] * 0.55) + core[..., None] * 0.55
    out[..., 3] = A
    return out


def green_bar(text_len_frac=1.0, text='+ SALES', fill_frac=1.0):
    w, h = 560, 150; S = 3
    im = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w * S + 40, h * S), 10 * S, fill=(126, 226, 58, 255))
    n = max(0, int(round(len(text) * text_len_frac)))
    d.text((30 * S, 62 * S), text[:n], font=ui_font('medium', 56 * S), fill=(20, 50, 15, 255), anchor='lm')
    d.rounded_rectangle((30 * S, 112 * S, (w - 20) * S, 118 * S), 3 * S, fill=(90, 170, 40, 255))
    d.rounded_rectangle((30 * S, 112 * S, int((30 + (w - 50) * fill_frac) * S), 118 * S), 3 * S, fill=(40, 100, 25, 255))
    return to_np(_fin(im, w, h))


def dollar_icon():
    w = 120; S = 3
    im = Image.new('RGBA', (w * S, w * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w * S - 1, w * S - 1), 12 * S, fill=(26, 82, 30, 235))
    d.ellipse((24 * S, 24 * S, 96 * S, 96 * S), outline=(110, 240, 70, 255), width=6 * S)
    d.text((60 * S, 61 * S), '$', font=ui_font('bold', 50 * S), fill=(110, 240, 70, 255), anchor='mm')
    return to_np(_fin(im, w, w))


def check_badge():
    w = 64; S = 3
    im = Image.new('RGBA', (w * S, w * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w * S - 1, w * S - 1), 12 * S, fill=(70, 200, 60, 255))
    d.ellipse((14 * S, 14 * S, 50 * S, 50 * S), outline=(255, 255, 255, 255), width=3 * S)
    d.line([(23 * S, 33 * S), (29 * S, 39 * S), (41 * S, 26 * S)], fill=(255, 255, 255, 255), width=4 * S)
    return to_np(_fin(im, w, w))


def icon_tile(kind, bg):
    w = 96; S = 3
    im = Image.new('RGBA', (w * S, w * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w * S - 1, w * S - 1), 22 * S, fill=bg)
    if kind == 'calendar':
        d.rounded_rectangle((22 * S, 26 * S, 74 * S, 74 * S), 8 * S, fill=(255, 255, 255, 255), outline=(90, 70, 160, 255), width=3 * S)
        d.rectangle((22 * S, 26 * S, 74 * S, 40 * S), fill=(235, 70, 80, 255))
        d.line([(34 * S, 20 * S), (34 * S, 32 * S)], fill=(90, 70, 160, 255), width=4 * S)
        d.line([(62 * S, 20 * S), (62 * S, 32 * S)], fill=(90, 70, 160, 255), width=4 * S)
        d.text((48 * S, 58 * S), '20', font=ui_font('bold', 20 * S), fill=(60, 50, 110, 255), anchor='mm')
    else:  # phone handset
        d.ellipse((20 * S, 20 * S, 76 * S, 76 * S), fill=(255, 255, 255, 255))
        try:
            d.text((48 * S, 50 * S), '☎', font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 38 * S), fill=(40, 140, 60, 255), anchor='mm')
        except OSError:
            d.text((48 * S, 50 * S), 'CALL', font=ui_font('bold', 16 * S), fill=(40, 140, 60, 255), anchor='mm')
    return _fin(im, w, w)


def icons_card():
    w, h = 270, 130
    im = rounded(w, h, 22, (38, 38, 46, 205))
    im.alpha_composite(icon_tile('calendar', (214, 170, 245, 255)), (int(28 * K), int(17 * K)))
    im.alpha_composite(icon_tile('phone', (222, 230, 150, 255)), (int(146 * K), int(17 * K)))
    return to_np(im)


def bubble(big, pill=None, w=250, h=120, tail='left'):
    S = 3; H2 = h + 26
    im = Image.new('RGBA', (w * S, H2 * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w * S - 1, h * S - 1), 14 * S, fill=(255, 255, 255, 255))
    tx = 40 if tail == 'left' else w - 60
    d.polygon([((tx) * S, (h - 2) * S), ((tx + 30) * S, (h - 2) * S), ((tx + 6) * S, (h + 24) * S)], fill=(255, 255, 255, 255))
    d.text((20 * S, 38 * S), big, font=ui_font('bold', 40 * S), fill=(20, 20, 24, 255), anchor='lm')
    d.rounded_rectangle((20 * S, 70 * S, (w - 40) * S, 76 * S), 3 * S, fill=(200, 200, 206, 255))
    if pill:
        f = ui_font('medium', 17 * S)
        pw = int(d.textlength(pill, font=f) / S) + 22
        d.rounded_rectangle((20 * S, 86 * S, (20 + pw) * S, 108 * S), 6 * S, fill=(18, 18, 20, 255))
        d.text(((20 + pw / 2) * S, 97 * S), pill, font=f, fill=(255, 255, 255, 255), anchor='mm')
    else:
        d.rounded_rectangle((20 * S, 86 * S, (w - 90) * S, 92 * S), 3 * S, fill=(220, 220, 226, 255))
    return to_np(_fin(im, w, H2))


def dial_bg(R=230):
    S = 3; w = R + 140; h = 2 * R + 80
    im = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0))
    cx, cy = -30 * S, h * S // 2
    # filled radial blue disc
    yy, xx = np.mgrid[0:h * S, 0:w * S].astype(np.float32)
    rr = np.hypot(xx - cx, yy - cy) / (R * S)
    a = (0.12 + 0.42 * np.clip(1 - rr, 0, 1) ** 0.7) * (rr < 1) + np.exp(-((rr - 1) / 0.02) ** 2) * 0.35
    col = np.dstack([0.35 + 0.4 * (1 - rr), 0.62 + 0.25 * (1 - rr), np.ones_like(rr)])
    arr = np.dstack([np.clip(col, 0, 1), np.clip(a, 0, 1)])
    im = Image.fromarray((arr * 255).astype(np.uint8), 'RGBA')
    d = ImageDraw.Draw(im)
    r2 = (R - 30) * S
    d.arc((cx - r2, cy - r2, cx + r2, cy + r2), -70, 62, fill=(240, 246, 255, 255), width=4 * S)
    ang = np.deg2rad(62)
    px, py = cx + r2 * np.cos(ang), cy + r2 * np.sin(ang)
    d.ellipse((px - 9 * S, py - 9 * S, px + 9 * S, py + 9 * S), fill=(255, 255, 255, 255))
    return to_np(_fin(im, w, h)), (h // 2)


def dial_bar():
    w, h = 14, 84; S = 3
    im = Image.new('RGBA', ((w + 40) * S, (h + 40) * S), (0, 0, 0, 0))
    g = Image.new('RGBA', im.size, (0, 0, 0, 0))
    ImageDraw.Draw(g).rounded_rectangle((20 * S, 20 * S, (20 + w) * S, (20 + h) * S), 7 * S, fill=(30, 140, 255, 255))
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(8 * S)))
    ImageDraw.Draw(im).rounded_rectangle((20 * S, 20 * S, (20 + w) * S, (20 + h) * S), 7 * S, fill=(40, 150, 255, 255))
    return to_np(_fin(im, w + 40, h + 40))


def ui_text(text, size=46, weight='regular', color=(255, 255, 255)):
    f = ui_font(weight, size * 2)
    l, t, r, b = f.getbbox(text)
    im = Image.new('RGBA', (r - l + 40, b - t + 40), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((20 - l, 20 - t), text, font=f, fill=color + (255,))
    im = im.resize((im.size[0] // 2, im.size[1] // 2), Image.LANCZOS)
    return to_np(im)


def swoosh_points():
    # brush stroke sweeping left->right under line 2, rising at the end
    t = np.linspace(0, 1, 140)
    x = 150 + 780 * t
    y = 70 - 55 * np.sin(np.pi * np.clip(t * 0.9, 0, 1)) * (1 - t) + (-90 * t ** 3)
    wdt = 4 + 26 * np.sin(np.pi * t) ** 0.8
    return np.stack([x, y, wdt], 1)


def swoosh(progress):
    pts = swoosh_points()
    n = max(2, int(len(pts) * np.clip(progress, 0, 1)))
    S = 3; w, h = 1080, 260
    im = Image.new('L', (w * S, h * S), 0); d = ImageDraw.Draw(im)
    oy = 150
    for x, y, r in pts[:n]:
        d.ellipse(((x - r / 2) * S, (y + oy - r / 2) * S, (x + r / 2) * S, (y + oy + r / 2) * S), fill=255)
    a = np.asarray(_fin(im, w, h)).astype(np.float32) / 255
    out = np.zeros((h, w, 4), np.float32); out[..., :3] = 1.0; out[..., 3] = a
    glow = cv2.GaussianBlur(a, (0, 0), 6) * 0.5
    out[..., 3] = np.clip(a + glow * (1 - a), 0, 1)
    return out
