---
name: reelpilot
description: Edits raw talking-head footage into a ready-to-post vertical reel (Instagram Reels, TikTok, YouTube Shorts) that matches the style of a reference video - animated keyword subtitles, motion-graphic animations, zoom "cuts", colour grade, sound effects and the user's own B-roll. Use whenever the user wants a short-form video edited, wants their reel to look like another reel, mentions raw footage plus a reference video, asks for animated captions/subtitles or reel animations, or says "edit my reel" / "use ReelPilot".
---

# ReelPilot v2 - reference-matched short-form editing

You turn a raw talking-head take into a finished 1080x1920 reel that copies the
*techniques* of a reference reel the user likes. Everything is rendered with
Python + ffmpeg on the user's machine, frame by frame, so the result is an actual
video file, not a plan.

`reference/example-edit-notes.md` is a complete worked example (a real client
edit). Read it before your first edit: it shows the level of detail expected in
the reference breakdown, the timeline and the limitations list.

## 0. Inputs

Expect one project folder:

```
my-reel/
├── raw/          talking-head footage (one take, or pre-cut in CapCut)
├── reference/    ONE reel whose style should be copied
└── broll/        optional: the user's own B-roll clips
```

If something is missing, ask for it. Do not proceed without raw footage and a
reference. B-roll is optional; never invent or generate B-roll footage.

## 1. Setup (once per machine)

1. Check `ffmpeg -version` and `python3 --version` (3.9+). If ffmpeg is missing,
   tell the user how to install it (macOS: `brew install ffmpeg`; Windows:
   `winget install ffmpeg`).
2. `pip install -r <skill>/scripts/requirements.txt`
3. Person-mask model (used for the background grade and colour spill):
   download MediaPipe `selfie_segmenter.tflite` from
   `https://storage.googleapis.com/mediapipe-models/image_segmenter/selfie_segmenter/float16/latest/selfie_segmenter.tflite`
   into the project folder.
4. Work in a `work/` folder inside the project. Never overwrite the user's files.

If a download is blocked, say exactly which step failed. You can skip masks by
saving an all-ones mask array (`np.ones((frames, 480, 270), np.uint8) * 255`);
the grade then treats the whole frame as subject. Tell the user the background
grade is off.

## 2. Prepare the raw footage

```
ffmpeg -i raw/<file> -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30" -c:v libx264 -crf 14 -c:a aac work/raw.mp4
python <skill>/scripts/words.py work/raw.mp4          # -> work/raw.words.json
python <skill>/scripts/masks.py selfie_segmenter.tflite work/raw.mp4 work/masks.npy
```

Read the transcript back to the user if words look wrong (names, brands).

Cutting: if the take has long pauses or retakes, propose cuts from the word
timings (gaps > 0.6 s, repeated phrases), show the list, and apply them with
ffmpeg `select`/`aselect` or a concat list *before* masks and rendering. Cutting
can take a few rounds; if the take is messy, recommend the user pre-cuts it in
CapCut.

## 3. Break down the reference

Extract what makes the reference look the way it does:

```
ffprobe reference/<file>                                   # size, fps, duration
ffmpeg -i reference/<file> -vf "fps=4,scale=270:-1,tile=8x6" work/ref_sheet_%02d.png
ffmpeg -i reference/<file> -af ebur128 -f null -           # loudness
```

Look at the contact sheets and write a table with these rows: Structure (hard
cuts vs zoom changes), Opening hook, Camera moves, Captions (font feel, lines,
colours, entry/exit animation, position), UI graphics (list each one and when it
appears), Grade, Audio (music? SFX types?). Use the example notes' table as the
model.

## 4. Plan the timeline

Map every line of the user's script (from the word timings) to a reference
technique with the same *meaning*: a list in the script gets the list/dial
graphic, a question gets the question-mark hit, growth or results get the bar,
a call-to-action gets the bubbles, and so on. Place B-roll where the words
describe something the clip shows.

Show the user the plan as a table (time, words, treatment) and get a quick OK
before rendering.

## 5. Build the render script

Copy `scripts/render_example.py` into `work/render.py` (keep `gfx.py` importable
from the skill folder) and change only the blocks marked `>>> EDIT PER VIDEO <<<`:

- `DUR`: edit length.
- `ZOOM`: a punch-in (~0.2 s, `out3`) or smooth push on each new caption, then a
  slow drift. Keep the zoom between ~1.2 and 1.45 for a wide take.
- `ANCHOR_SRC` / `ANCHOR_DST`: the speaker's head position in the raw frame and
  where it should sit on screen.
- `CAPS`: 2-line keyword captions made from the transcript (line 1 short and
  white, line 2 the key word(s) in colour). Colours available: see
  `gfx.PALETTE`. Follow the reference's colour order.
- `BROLL`: `(start, end, path, clip_in, 'full'|'card')` for each user clip.
- `CARD_IMG` stills and the timed blocks in `overlays()`: re-time, remove or
  re-use the graphics to fit your plan. Available builders in `gfx.py`:
  `caption`, `video_card`, `star_pill`, `magnifier`, `badge`, `question_mark`,
  `neon_question`, `green_bar`, `dollar_icon`, `check_badge`, `icons_card`,
  `bubble`, `dial_bg`/`dial_bar`/`ui_text`, `swoosh`. New graphics follow the
  same pattern: PIL drawing at 2-3x scale, returned as float RGBA.
- The flashes at the end of `overlays()`: match the reference's hook.

## 6. Check stills, then render

```
python work/render.py work/raw.mp4 work/masks.npy --still 0.3,2,5,8,12,16,20,24 work/check.png
```

Look at the contact sheet yourself. Check: captions fully readable and inside
the frame, no graphic covering the face, B-roll appearing at the right moments.
Fix and re-check. Then render in chunks (faster to redo one part):

```
python work/render.py work/raw.mp4 work/masks.npy work/part1.mp4 0 300
python work/render.py work/raw.mp4 work/masks.npy work/part2.mp4 300 <total_frames>
```

and join them with the ffmpeg concat demuxer into `work/video.mp4`.

## 7. Sound

Copy `scripts/sfx_example.py`, rebuild its `EV` list so each whoosh, pop, tick,
shimmer or impact lands on a graphic event in your timeline, set `DUR`, and
render `work/sfx.wav`. Then mix:

```
ffmpeg -i work/video.mp4 -i work/raw.mp4 -i work/sfx.wav -filter_complex "[1:a]highpass=f=80,acompressor=threshold=-18dB:ratio=3:attack=5:release=80,loudnorm=I=-13:TP=-1:LRA=7[v];[v][2:a]amix=inputs=2:normalize=0[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest final_edit.mp4
```

If the reference has music, ask the user for a track; never pull music from the
internet.

## 8. Deliver

Save `final_edit.mp4` in the project folder plus `EDIT_NOTES.md` with: the
reference breakdown table, the timeline table, and a **Limitations** list.
Then tell the user in plain words what was done and what they might want changed.

## Rules

- **Never fabricate.** No invented view counts, percentages, prices, testimonials
  or brand logos. If the reference shows numbers the script doesn't contain,
  replace them with words from the script and list it under Limitations.
- **Readable captions win.** Captions sit on top of everything (hand occlusion is
  off by default); keep a strong shadow on bright clothing.
- **Don't copy other brands.** Replace logos/avatars from the reference with
  neutral elements or the user's own assets.
- **Revisions are normal.** When the user asks for a change ("bigger subtitles",
  "cut the pause at 0:12"), edit `work/render.py` and re-render only the affected
  chunk.
