# ReelPilot render TEMPLATE. This is the worked example from a real client edit
# (see reference/example-edit-notes.md). For a new video, copy it into the
# project folder and change the parts marked  >>> EDIT PER VIDEO <<<  :
#   DUR, ZOOM, ANCHOR_SRC/DST, CAPS, BROLL, CARD stills, and the timed blocks in overlays().
# Raw footage must be 1080x1920 (scale it first with ffmpeg, see SKILL.md).
# usage: render_example.py RAW MASKS OUT_MP4 start_frame end_frame
#        render_example.py RAW MASKS --still t1,t2,... OUT_PNG   (contact sheet for checking)
import sys, os, subprocess, numpy as np, cv2
sys.path.insert(0, os.path.dirname(__file__))
import gfx

W, H, FPS = 1080, 1920, 30
RAW, MASKS = sys.argv[1], sys.argv[2]
DUR = 28.24   # >>> EDIT PER VIDEO <<< length of the edit in seconds
NF = int(DUR * FPS)

# ---------------------------------------------------------------- easing
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def e_out3(x): x = clamp(x); return 1 - (1 - x) ** 3
def e_inout(x): x = clamp(x); return 3 * x * x - 2 * x * x * x
def e_back(x, s=1.7):
    x = clamp(x); x -= 1; return x * x * ((s + 1) * x + s) + 1
def lin(x): return clamp(x)
EASE = {'out3': e_out3, 'inout': e_inout, 'lin': lin}

# ---------------------------------------------------------------- camera (zoom) keyframes  >>> EDIT PER VIDEO <<<
# (start, end, zoom_from, zoom_to, easing). Change zoom on every new caption, like the reference.
ZOOM = [(0.00, 0.50, 2.10, 1.36, 'out3'), (0.50, 1.94, 1.36, 1.22, 'inout'),
        (1.94, 2.94, 1.22, 1.40, 'inout'), (3.86, 4.06, 1.40, 1.30, 'out3'),
        (5.88, 7.30, 1.30, 1.28, 'lin'),
        (7.30, 7.50, 1.28, 1.40, 'out3'), (7.50, 9.64, 1.40, 1.33, 'lin'),
        (9.64, 9.84, 1.33, 1.43, 'out3'), (9.84, 12.52, 1.43, 1.37, 'lin'),
        (12.52, 12.72, 1.37, 1.26, 'out3'),
        (15.28, 15.48, 1.26, 1.40, 'out3'), (16.38, 18.66, 1.40, 1.32, 'inout'),
        (18.66, 18.86, 1.32, 1.43, 'out3'), (20.46, 20.66, 1.43, 1.30, 'out3'),
        (22.40, 22.60, 1.30, 1.45, 'out3'), (22.60, 24.38, 1.45, 1.38, 'lin'),
        (24.38, 24.58, 1.38, 1.30, 'out3'), (26.46, 28.30, 1.30, 1.25, 'lin')]

def zoom(t):
    z = ZOOM[0][2]
    for a, b, z0, z1, e in ZOOM:
        if t >= b: z = z1
        elif t >= a: return z0 + (z1 - z0) * EASE[e]((t - a) / (b - a))
    return z

ANCHOR_SRC = (540.0, 450.0)   # speaker's head in the raw frame
ANCHOR_DST = (540.0, 380.0)   # where the reference keeps the head on screen

def cam_matrix(z):
    return np.float32([[z, 0, ANCHOR_DST[0] - ANCHOR_SRC[0] * z], [0, z, ANCHOR_DST[1] - ANCHOR_SRC[1] * z]])

# ---------------------------------------------------------------- grade
def make_lut(contrast, expo, rgbmul, blue_lift):
    x = np.linspace(0, 1, 256)
    s = x ** 1.12
    s = np.clip((s - 0.5) * contrast + 0.5, 0, 1)
    s = np.where(s > 0.5, 0.5 + (s - 0.5) * 0.62, s) * expo   # roll off the bright shirt
    ch = [np.clip(s * m + (blue_lift * (1 - x) if i == 2 else 0), 0, 1) for i, m in enumerate(rgbmul)]
    return [(c * 255).astype(np.uint8) for c in ch]  # R,G,B

LUT_SUBJ = make_lut(1.28, 0.90, (0.92, 0.97, 1.06), 0.03)

yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
_grad = np.clip(1 - (yy / H - 0.52) / 0.40, 0, 1)
_grad = 0.10 + 0.90 * _grad ** 1.5
_vig = 1 - 0.38 * np.clip(((xx - W / 2) / (W * 0.62)) ** 2 + ((yy - H * 0.33) / (H * 0.80)) ** 2, 0, 1)
SCREEN_MASK = (_grad * _vig)[..., None].astype(np.float32)

def grade(rgb, m):
    subj = np.dstack([cv2.LUT(rgb[..., i], LUT_SUBJ[i]) for i in range(3)]).astype(np.float32) / 255
    lum = (0.3 * rgb[..., 0] + 0.59 * rgb[..., 1] + 0.11 * rgb[..., 2]).astype(np.float32) / 255
    lum = np.clip((lum - 0.12) * 1.25, 0, 1) ** 1.25
    bg = np.dstack([lum * 0.10 + 0.005, lum * 0.42 + 0.02, lum * 1.05 + 0.06])  # saturated blue room
    bg = 0.80 * bg + 0.20 * subj * np.array([0.5, 0.75, 1.1], np.float32)
    m3 = m[..., None]
    return subj * m3 + bg * (1 - m3)

# ---------------------------------------------------------------- compositing
def place(dst, rgba, cx, cy, alpha=1.0, scale=1.0, blur=0.0, mblur=0.0, rot=0.0, occl=None, sx=None):
    if alpha <= 0.003 or scale <= 0.01: return
    img = rgba
    if scale != 1.0 or (sx is not None and sx != 1.0):
        fx = scale * (sx if sx is not None else 1.0)
        img = cv2.resize(img, (max(1, int(img.shape[1] * fx)), max(1, int(img.shape[0] * scale))), interpolation=cv2.INTER_AREA if scale < 1 else cv2.INTER_CUBIC)
    if rot:
        h, w = img.shape[:2]; d = int(np.hypot(h, w)) + 4
        pad = np.zeros((d, d, 4), np.float32); y0, x0 = (d - h) // 2, (d - w) // 2; pad[y0:y0 + h, x0:x0 + w] = img
        M = cv2.getRotationMatrix2D((d / 2, d / 2), rot, 1.0); img = cv2.warpAffine(pad, M, (d, d), flags=cv2.INTER_LINEAR)
    if blur > 0.3 or mblur > 1:
        pm = img.copy(); pm[..., :3] *= pm[..., 3:4]
        p = int(max(blur * 3, abs(mblur)) + 4); pm = cv2.copyMakeBorder(pm, p, p, p, p, cv2.BORDER_CONSTANT)
        if blur > 0.3: pm = cv2.GaussianBlur(pm, (0, 0), blur)
        if mblur > 1:
            k = int(mblur) | 1; ker = np.zeros((k, k), np.float32); ker[k // 2, :] = 1.0 / k
            pm = cv2.filter2D(pm, -1, ker)
        img = pm; img[..., :3] /= np.maximum(img[..., 3:4], 1e-4)
    h, w = img.shape[:2]
    x0 = int(round(cx - w / 2)); y0 = int(round(cy - h / 2))
    ax0, ay0 = max(0, x0), max(0, y0); ax1, ay1 = min(W, x0 + w), min(H, y0 + h)
    if ax0 >= ax1 or ay0 >= ay1: return
    src = img[ay0 - y0:ay1 - y0, ax0 - x0:ax1 - x0]
    a = np.clip(src[..., 3:4], 0, 1) * alpha
    if occl is not None: a = a * (1 - occl[ay0:ay1, ax0:ax1, None])
    region = dst[ay0:ay1, ax0:ax1]
    region[:] = region * (1 - a) + np.clip(src[..., :3], 0, 1) * a

def screen_add(dst, field, color, k):
    if k <= 0: return
    g = field[..., None] * np.array(color, np.float32) * k
    dst[:] = 1 - (1 - dst) * (1 - g)

GLOW_FIELD = np.exp(-(((xx - 540) / 520) ** 2 + ((yy - 900) / 430) ** 2)).astype(np.float32)
FULL = np.ones((H, W), np.float32)

# ---------------------------------------------------------------- assets
CAP_Y = 890
# >>> EDIT PER VIDEO <<< captions come from the transcript words; colours follow the reference's order
CAPS = [  # start, end, line1, line2, colour, entry  (keyword captions, as in the reference)
    (0.30, 1.94, 'AN INFLUENCER', 'VIDEO', 'blue', 'fly'),
    (1.94, 2.96, "SHOULDN'T STOP", 'WORKING', 'blue', 'pop'),
    (2.96, 3.86, "AFTER IT'S", 'POSTED', 'blue', 'pop'),
    (3.86, 5.88, 'RIGHT AGREEMENT', '& STRATEGY', 'green', 'pop'),
    (7.30, 9.64, 'TESTED THROUGH', 'PAID ADS', 'yellow', 'pop'),
    (9.64, 12.52, 'REACH MORE', 'CUSTOMERS', 'yellow', 'pop'),
    (15.28, 16.38, 'THIS', 'CONNECTION', 'magenta', 'pop'),
    (18.66, 20.46, 'PART OF', 'THE SYSTEM', 'blue', 'pop'),
    (20.46, 22.40, 'INSIDE', 'MY OWN BRAND', 'blue', 'pop'),
    (22.40, 24.38, 'WANT TO TURN', 'CREATOR CONTENT', 'red', 'pop'),
    (24.38, 26.46, 'INTO A STRONGER', 'SALES ASSET', 'green', 'pop'),
]
CAP_IMG = [gfx.caption(c[2], c[3], c[4], w2max=950, s2max=150) for c in CAPS]

def raw_frame_at(t):
    cap = cv2.VideoCapture(RAW); cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000); ok, f = cap.read(); cap.release()
    return f

def graded_still(t, m_all):
    f = raw_frame_at(t)
    m = cv2.resize(m_all[int(t * FPS)].astype(np.float32) / 255, (W, H))
    g = grade(cv2.cvtColor(f, cv2.COLOR_BGR2RGB), m)
    return cv2.cvtColor((np.clip(g, 0, 1) * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)

MASKS_ALL = np.load(MASKS)
CARD_IMG = [gfx.video_card(graded_still(t, MASKS_ALL)) for t in (2.2, 11.0, 19.6)]

gfx.K = 1.2
PILL1 = [gfx.star_pill(n, (255, 160, 20), (255, 200, 60)) for n in range(6)]
PILL2 = [gfx.star_pill(n, (110, 215, 60), (170, 200, 255)) for n in range(6)]
gfx.K = 1.47; MAG, MAG_C, MAG_R = gfx.magnifier(); MAG_C = (MAG_C[0] * 1.47, MAG_C[1] * 1.47); MAG_R *= 1.47
gfx.K = 1.2; BADGE = gfx.badge('AD')
gfx.K = 1.1; GBAR = {}
gfx.K = 1.9; DOLLAR = gfx.dollar_icon()
gfx.K = 1.5; CHECK = gfx.check_badge()
gfx.K = 1.37; ICONS = gfx.icons_card()
gfx.K = 1.2; BUB1 = {n: gfx.bubble('FREE'[:n] if n else ' ') for n in range(5)}
gfx.K = 1.3; BUB2 = {n: gfx.bubble('20 MIN'[:n] if n else ' ', pill='call with me', w=300, h=135) for n in range(7)}
gfx.K = 1.0
DIAL, DIAL_CY = gfx.dial_bg(R=270)
DBAR = gfx.dial_bar()
DITEMS = [(16.38, gfx.ui_text('CREATORS', 50)), (17.34, gfx.ui_text('CONTENT', 50)), (18.08, gfx.ui_text('ADVERTISING', 50))]
QM = gfx.question_mark(200)
NEON = gfx.neon_question(560)

def gbar(textf, fillf):
    key = (round(textf, 2), round(fillf, 2))
    if key not in GBAR:
        gfx.K = 1.1; GBAR[key] = gfx.green_bar(textf, '+ SALES', fillf); gfx.K = 1.0
    return GBAR[key]

SWOOSH_CACHE = {}
def swoosh_img(p):
    k = round(p, 2)
    if k not in SWOOSH_CACHE: SWOOSH_CACHE[k] = gfx.swoosh(k)
    return SWOOSH_CACHE[k]

# ---------------------------------------------------------------- B-roll  >>> EDIT PER VIDEO <<<
# Clips from the project's broll/ folder. Each entry: (start, end, path, clip_in_seconds, mode)
#   mode 'full' = full-screen cutaway (captions stay on top); 'card' = rounded inset over the speaker.
# Leave empty when the user supplied no B-roll. Never invent footage.
BROLL = []
_BR_CAPS = {}

def broll_frame(path, t_clip):
    cap = _BR_CAPS.get(path)
    if cap is None: cap = _BR_CAPS[path] = cv2.VideoCapture(path)
    cap.set(cv2.CAP_PROP_POS_MSEC, max(0.0, t_clip) * 1000)
    ok, f = cap.read()
    if not ok: return None
    h, w = f.shape[:2]; s = max(W / w, H / h)          # cover-crop to 1080x1920
    f = cv2.resize(f, (int(w * s + 0.5), int(h * s + 0.5)), interpolation=cv2.INTER_AREA)
    y0 = (f.shape[0] - H) // 2; x0 = (f.shape[1] - W) // 2
    return cv2.cvtColor(f[y0:y0 + H, x0:x0 + W], cv2.COLOR_BGR2RGB).astype(np.float32) / 255

def apply_broll(fr, t):
    for a, b, path, cin, mode in BROLL:
        if not (a <= t < b): continue
        img = broll_frame(path, cin + (t - a))
        if img is None: continue
        u = t - a; p = e_out3(u / 0.20)
        z = 1.08 - 0.08 * p + 0.03 * (u / max(b - a, 1e-3))   # pop in, then slow push
        img = cv2.warpAffine(img, np.float32([[z, 0, W / 2 * (1 - z)], [0, z, H / 2 * (1 - z)]]), (W, H), borderMode=cv2.BORDER_REFLECT)
        if mode == 'full':
            fr[:] = fr * (1 - p) + img * SCREEN_MASK * p
        else:
            card = cv2.resize(img, (620, 1100), interpolation=cv2.INTER_AREA)
            rgba = np.dstack([card, np.ones(card.shape[:2], np.float32)])
            r = 40; mk = np.zeros(card.shape[:2], np.uint8)
            cv2.rectangle(mk, (r, 0), (620 - r, 1100), 255, -1); cv2.rectangle(mk, (0, r), (620, 1100 - r), 255, -1)
            for cx, cy in ((r, r), (620 - r, r), (r, 1100 - r), (620 - r, 1100 - r)): cv2.circle(mk, (cx, cy), r, 255, -1)
            rgba[..., 3] = mk / 255
            place(fr, rgba, 540, 960, alpha=clamp(u / 0.08), scale=0.85 + 0.15 * e_back(u / 0.25, 1.4))

# ---------------------------------------------------------------- per-frame overlay logic
def hand_occluder(raw_warp, m_warp):
    ycc = cv2.cvtColor(raw_warp, cv2.COLOR_BGR2YCrCb)
    skin = cv2.inRange(ycc, (40, 138, 80), (245, 178, 128)).astype(np.float32) / 255
    skin *= (m_warp > 0.45)
    skin[:640] = 0
    skin = cv2.morphologyEx(skin, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    skin = cv2.dilate(skin, np.ones((5, 5), np.uint8))
    return cv2.GaussianBlur(skin, (0, 0), 2.0)

def overlays(fr, t, occl):
    # caption + colour spill
    for i, (a, b, l1, l2, col, entry) in enumerate(CAPS):
        if not (a <= t < b): continue
        img, glowc = CAP_IMG[i]
        u = t - a
        if entry == 'fly':
            p = e_out3(u / 0.50)
            cx = 540 + (-380) * (1 - p); cy = CAP_Y + 420 * (1 - p)
            place(fr, img, cx, cy, alpha=clamp(u / 0.08), scale=1 + 1.3 * (1 - p), mblur=60 * (1 - p), rot=8 * (1 - p), occl=occl)
        else:
            p = u / 0.17
            place(fr, img, 540, CAP_Y, alpha=clamp(p * 1.6), scale=0.80 + 0.20 * e_back(p, 1.2), blur=7 * (1 - clamp(p)), occl=occl)
        screen_add(fr, GLOW_FIELD, glowc, 0.20 * clamp(u / 0.15))
        if col == 'red':
            screen_add(fr, FULL, glowc, 0.07)

    # swoosh under "AGREEMENT & STRATEGY"
    if 4.72 <= t < 5.88:
        place(fr, swoosh_img(e_out3((t - 4.72) / 0.35)), 540, CAP_Y + 30)

    # creator video cards (strongest creator videos)
    if 5.88 <= t < 7.30:
        u = t - 5.88
        for k, (dx, delay, sc) in enumerate([(-265, 0.17, 0.92), (265, 0.30, 0.92)]):
            p = e_out3((u - delay) / 0.22)
            if p > 0:
                place(fr, CARD_IMG[k * 2], 540 + dx * p, 960, alpha=clamp(p * 1.5) * 0.92, scale=sc * (0.85 + 0.15 * p))
        p = e_back(u / 0.20, 1.4)
        mid = CARD_IMG[1].copy()
        wash = clamp(1 - u / 0.25)
        mid[..., :3] = mid[..., :3] * (1 - wash) + wash
        place(fr, mid, 540, 960, alpha=clamp(u / 0.06), scale=0.6 + 0.4 * p, blur=6 * wash)

    # magnifier + badge (tested through paid ads)
    if 7.45 <= t < 9.64:
        u = t - 7.45
        p = e_inout(u / 0.95)
        lx = 1000 + (330 - 1000) * p + 30 * np.sin(u * 2.4) * clamp(u - 0.95)
        ly = 1035 + 20 * np.sin(np.pi * p) + 25 * np.cos(u * 2.0) * clamp(u - 0.95)
        r = int(MAG_R - 10)
        y0, y1, x0, x1 = int(ly - r), int(ly + r), int(lx - r), int(lx + r)
        if y0 >= 0 and x0 >= 0 and x1 <= W and y1 <= H:
            patch = fr[y0:y1, x0:x1].copy()
            big = cv2.resize(patch, None, fx=1.12, fy=1.12, interpolation=cv2.INTER_CUBIC)
            o = (big.shape[0] - patch.shape[0]) // 2
            big = big[o:o + patch.shape[0], o:o + patch.shape[1]]
            circ = (np.hypot(*np.mgrid[-r:r, -r:r]) < r).astype(np.float32)[..., None]
            fr[y0:y1, x0:x1] = big * circ + patch * (1 - circ)
        mh, mw = MAG.shape[:2]
        place(fr, MAG, lx + (mw / 2 - MAG_C[0]), ly + (mh / 2 - MAG_C[1]), alpha=clamp(u / 0.1))
    if 8.10 <= t < 9.64:
        u = t - 8.10
        place(fr, BADGE, 905, 760, scale=e_back(u / 0.25, 2.0), alpha=clamp(u / 0.08))

    # star rating pills (which messages actually perform)
    if 12.52 <= t < 15.28:
        u = t - 12.52
        p = e_out3(u / 0.22)
        n1 = int(clamp((u - 0.25) / 0.12, 0, 3)) if u > 0.25 else 0
        place(fr, PILL1[n1], 540 - 700 * (1 - p), 945, alpha=clamp(u / 0.05), mblur=70 * (1 - p))
        if t >= 13.50:
            v = t - 13.50; q = e_out3(v / 0.22)
            n2 = int(clamp((v - 0.25) / 0.12, 0, 5)) if v > 0.25 else 0
            place(fr, PILL2[n2], 540 - 700 * (1 - q), 1080, alpha=clamp(v / 0.05), mblur=70 * (1 - q))

    # dial / list (creators, content, advertising)
    if 16.38 <= t < 18.66:
        u = t - 16.38
        p = e_out3(u / 0.30)
        cy = 1040
        dh, dw = DIAL.shape[:2]
        # light cone from the dial
        cone = np.clip(1 - np.abs(yy[cy - 160:cy + 160, :] - cy) / (60 + xx[cy - 160:cy + 160, :] * 0.18), 0, 1) * np.clip(1 - xx[cy - 160:cy + 160, :] / 900, 0, 1)
        fr[cy - 160:cy + 160] = 1 - (1 - fr[cy - 160:cy + 160]) * (1 - cone[..., None] * np.array([0.35, 0.55, 0.85]) * 0.35 * p)
        place(fr, DIAL, dw / 2 - 260 * (1 - p), cy, alpha=p, rot=-30 * (1 - p))
        place(fr, DBAR, 285, cy - 8, alpha=p)
        for k, (ts, img) in enumerate(DITEMS):
            nxt = DITEMS[k + 1][0] if k + 1 < len(DITEMS) else 99
            if t < ts or t >= nxt + 0.25: continue
            ih, iw = img.shape[:2]
            if t < nxt:
                q = e_out3((t - ts) / 0.25) if k > 0 else p
                ang = 22 * (1 - q)
            else:
                q = e_out3((t - nxt) / 0.25); ang = -22 * q
            rad = np.deg2rad(ang); R = 430
            cx = -30 + R * np.cos(rad) + iw / 2 - 100; cyy = cy - 8 + R * np.sin(rad) * 1.0
            a = (q if t < nxt else 1 - q)
            place(fr, img, cx, cyy, alpha=a, rot=-ang)

    # red question marks
    if 22.40 <= t < 24.38:
        u = t - 22.40
        place(fr, QM, 120, 820, scale=e_back(u / 0.22, 1.6), rot=12, alpha=clamp(u / 0.06))
        p = e_out3((u - 0.1) / 0.30)
        if p > 0:
            flick = 0.85 + 0.15 * np.sin(u * 37)
            place(fr, NEON, 1080 + 40 - 60 * p, 1130, alpha=p * flick, rot=-8)

    # green bar, $ icon, check (stronger sales asset)
    if 24.50 <= t < 26.46:
        u = t - 24.50
        p = e_out3(u / 0.22)
        img = gbar(clamp((u - 0.15) / 0.30), clamp((u - 0.2) / 0.9))
        bh, bw = img.shape[:2]
        place(fr, img, 1080 - bw / 2 + 40 + 600 * (1 - p), 1205, mblur=60 * (1 - p))
    if 24.85 <= t < 26.46:
        u = t - 24.85
        place(fr, DOLLAR, 150, 1090, scale=e_back(u / 0.25, 1.8), alpha=clamp(u / 0.06))
    if 25.20 <= t < 26.46:
        u = t - 25.20
        place(fr, CHECK, 985, 760, scale=e_back(u / 0.25, 2.2), alpha=clamp(u / 0.06))

    # CTA bubbles
    if t >= 26.46:
        u = t - 26.46
        place(fr, ICONS, 540, 1228, scale=0.5 + 0.5 * e_back(u / 0.25, 1.6), alpha=clamp(u / 0.06))
        if t >= 26.80:
            v = t - 26.80
            place(fr, BUB1[int(clamp(v / 0.20) * 4)], 315, 1000, scale=0.7 + 0.3 * e_back(v / 0.22), alpha=clamp(v / 0.06), blur=5 * clamp(1 - v / 0.15))
        if t >= 27.08:
            v = t - 27.08
            place(fr, BUB2[int(clamp(v / 0.30) * 6)], 765, 965, scale=0.7 + 0.3 * e_back(v / 0.22), alpha=clamp(v / 0.06), blur=5 * clamp(1 - v / 0.15))

    # full-frame flashes
    if t < 0.42:
        a = 0.88 * (1 - e_out3(t / 0.42)) ** 0.9
        fr[:] = fr * (1 - a) + np.array([0.12, 0.40, 1.0], np.float32) * a
    if 22.40 <= t < 22.80:
        a = 0.80 * (1 - e_out3((t - 22.40) / 0.40))
        fr[:] = fr * (1 - a) + np.array([0.95, 0.12, 0.08], np.float32) * a

# ---------------------------------------------------------------- frame render
def render_frame(t, raw_bgr, m_small):
    m = cv2.resize(m_small.astype(np.float32) / 255, (W, H), interpolation=cv2.INTER_LINEAR)
    rgb = cv2.cvtColor(raw_bgr, cv2.COLOR_BGR2RGB)
    g = grade(rgb, m)
    z = zoom(t)
    if t < 0.5:   # whip zoom with zoom-blur
        zs = [zoom(max(0, t - k / 120)) for k in range(6)]
        acc = sum(cv2.warpAffine(g, cam_matrix(zz), (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT) for zz in zs) / len(zs)
        fr = acc
    else:
        fr = cv2.warpAffine(g, cam_matrix(z), (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
    fr = fr * SCREEN_MASK
    occl = None
    if False:  # hand occlusion disabled: captions always stay fully readable
        M = cam_matrix(z)
        occl = hand_occluder(cv2.warpAffine(raw_bgr, M, (W, H), flags=cv2.INTER_LINEAR), cv2.warpAffine(m, M, (W, H)))
    fr = np.clip(fr, 0, 1).astype(np.float32)
    apply_broll(fr, t)
    overlays(fr, t, occl)
    return (np.clip(fr, 0, 1) * 255 + 0.5).astype(np.uint8)

def raw_reader(start_frame):
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', RAW, '-vf', 'fps=30', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
    i = 0
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        if i >= start_frame: yield i, np.frombuffer(b, np.uint8).reshape(H, W, 3)
        i += 1

if __name__ == '__main__':
    if sys.argv[3] == '--still':
        ts = [float(x) for x in sys.argv[4].split(',')]
        outs = []
        for t in ts:
            i = int(round(t * FPS))
            fr = render_frame(i / FPS, raw_frame_at(i / FPS), MASKS_ALL[min(i, len(MASKS_ALL) - 1)])
            outs.append(cv2.resize(fr, (360, 640), interpolation=cv2.INTER_AREA))
        rows = [np.hstack(outs[k:k + 6] + [np.zeros_like(outs[0])] * (6 - len(outs[k:k + 6]))) for k in range(0, len(outs), 6)]
        cv2.imwrite(sys.argv[5], cv2.cvtColor(np.vstack(rows), cv2.COLOR_RGB2BGR))
        sys.exit()
    out = sys.argv[3]; s, e = int(sys.argv[4]), int(sys.argv[5])
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-preset', 'medium', '-crf', '14', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    for i, f in raw_reader(s):
        if i >= e or i >= NF: break
        enc.stdin.write(render_frame(i / FPS, f, MASKS_ALL[min(i, len(MASKS_ALL) - 1)]).tobytes())
    enc.stdin.close(); enc.wait()
