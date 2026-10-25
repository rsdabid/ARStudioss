# Word-level timestamps for captions and timing.
# usage: python words.py RAW_VIDEO_OR_AUDIO [model]   ->  writes <name>.words.json
# Output format: [[start_s, end_s, "word"], ...]  (same as transcribe_onnx.py)
# Needs: pip install faster-whisper   (downloads the model on first run)
import sys, json, os
from faster_whisper import WhisperModel

src = sys.argv[1]
model = WhisperModel(sys.argv[2] if len(sys.argv) > 2 else 'small', device='auto', compute_type='int8')
segments, info = model.transcribe(src, word_timestamps=True, vad_filter=True)
words = [[round(w.start, 2), round(w.end, 2), w.word.strip()] for seg in segments for w in seg.words]
out = os.path.splitext(src)[0] + '.words.json'
json.dump(words, open(out, 'w'))
print('language:', info.language, '| words:', len(words), '| saved', out)
print(' '.join(f'[{s:.2f}]{t}' for s, e, t in words))
