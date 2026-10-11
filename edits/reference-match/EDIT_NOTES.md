# Reference-match edit

Output: `final_edit.mp4`. It's 1080×1920 at 30 fps (the reference's format), H.264 video with AAC 48 kHz stereo audio, runs 28.23 s and plays at −13.3 LUFS (the reference plays at −12.6).

## Reference breakdown (what was replicated)

| Element | Reference | Applied to raw footage |
|---|---|---|
| Structure | One continuous take. No hard cuts; every "cut" is an animated zoom change. | Same. One take, with zoom keyframes changing on every caption. |
| Opening hook | Full-frame blue flash fading over ~0.35 s, a motion-blurred whip zoom-out (~1.7× → 1×), and the brand logo flying in from the bottom-left. | Same flash colour and timing, and a 2.1× → 1.36× whip zoom with zoom blur. The first caption uses the logo's fly-in (offset, scale, tilt, motion blur). |
| Camera | A quick punch-in (~0.2 s) or a smooth push on each new caption, then a slow drift out. | The same pattern. Zoom range is 1.22–1.45 because the raw take is framed wider than the reference. |
| Captions | Two-line keyword captions. Line 1 is white; line 2 is larger and coloured (blue, green, yellow, red, magenta) with a vertical gradient. Heavy extended italic type, a coloured glow plus colour spill on the subject, a dark shadow, and hands passing in front of the text. Entry is a scale-and-blur pop (~0.17 s); exit is a hard switch. | Same. The font is Unbounded Black slanted (the closest free match). The colour order follows the reference's sequence, and the subject's hands occlude the text via a person and skin mask. |
| UI graphics | Video cards fanning out; a magnifier sweeping the caption with a pin badge; two star-rating pills; a red flash with a 3D "?" and a neon "?"; a green "+%" bar with a "$" tile and a check badge; price chat bubbles above an icon card; a left-edge dial list with a wheel rotation. | Each one is rebuilt and mapped to the line of your script with the matching meaning (see the timeline below). |
| Grade | Dark, saturated blue room, with the bottom of the frame falling off to black and a natural subject. | Background is pushed to saturated blue via the person mask. The subject gets contrast, a highlight roll-off and slightly cool tones. Bottom gradient and vignette are added. |
| Audio | Voice only (no music bed found), with whooshes, pops, ticks, a high shimmer and an impact on the graphics. | Voice gets a high-pass, compression and loudness matching. The synthesized SFX are timed to each graphic event. |

## Timeline (raw script → reference technique)

| Time (s) | Words | Treatment (reference equivalent) |
|---|---|---|
| 0.00–1.94 | "An influencer video" | Blue flash + whip zoom + fly-in caption (logo intro) |
| 1.94–3.86 | "shouldn't stop working / after it's posted" | Blue captions (THE BEST / CONTENT AGENCY) |
| 3.86–5.88 | "with the right agreement and strategy" | Green caption + white swoosh (THAT HELPS / BUSINESS OWNERS) |
| 5.88–7.30 | "the strongest creator videos" | Video cards fan out (view-count cards) |
| 7.30–9.64 | "tested through paid ads" | Yellow caption + magnifier + pin badge (LOOKING FOR / FULL-TIME EDITORS) |
| 9.64–12.52 | "reach more potential customers" | Yellow caption (AND WE'RE / LOOKING FOR) |
| 12.52–15.28 | "which messages actually perform" | Star-rating pills (best of the best) |
| 15.28–16.38 | "This connection" | Magenta caption (IT / DEPENDS) |
| 16.38–18.66 | "creators, content and advertising" | Dial list rotating through 3 items (task / experience / skills) |
| 18.66–22.40 | "part of the system … my own brand" | Blue captions (WELL IT / DEPENDS) |
| 22.40–24.38 | "So if you want to turn creator content" | Red flash + 3D "?" + neon "?" (YOU MIGHT BE / WONDERING) |
| 24.38–26.46 | "into a stronger sales asset" | Green caption + green bar + "$" tile + check (HOW MUCH DO / WE PAY?) |
| 26.46–28.23 | "book a free 20 minute call with me" | Icon card + chat bubbles (the $500 / $2000 bubbles) |

## Limitations (not silently replaced)

- **Brand logo**: the reference opens on a "Media Key" logo. No logo asset was supplied and the raw script names no brand, so the logo's fly-in animation is used on the first caption instead.
- **Fabricated numbers avoided**: the reference shows view counts (1.2M/1M/2M), "+50%" and "$500/$2000". None of these exist in your footage, so:
  - the cards carry no numbers;
  - the bar reads "+ SALES";
  - the bubbles read "FREE" and "20 MIN · call with me", taken from your words.
- **Card thumbnails**: these come from your own take; no other creator videos were supplied.
- **Dial sub-lines**: the reference's small descriptions under each dial item were left out because your script has no text for them.
- **Lighting**: the reference's dark-shirt, blue-lit look comes partly from how it was shot. The grade gets close, but your white shirt stays brighter than the reference subject.
- **Sound effects**: synthesized (no SFX library or reference stems were available), so they match in timing and character, not in exact samples.
- **Pin badge**: the reference's pin badge shows another brand's avatar; it's replaced with a neutral "AD" badge.

## Rebuild

`scripts/` contains everything:

- `transcribe.py`: Whisper word timings
- `masks.py`: person segmentation
- `render.py` and `gfx.py`: grade, camera and graphics
- `sfx.py`: sound design

Fonts used: Unbounded (900) and Inter. Segmentation model: MediaPipe selfie segmentation.
