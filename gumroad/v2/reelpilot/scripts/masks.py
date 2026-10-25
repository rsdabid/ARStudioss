# Person mask for every output frame (30 fps), saved at 1/4 resolution as .npy.
# Needs MediaPipe selfie_segmenter.tflite (see SKILL.md). Input must be 1080x1920.
# usage: masks.py selfie_segmenter.tflite RAW_1080x1920.mp4 OUT_MASKS.npy
# Person-segmentation pre-pass: one mask per output frame (30fps), stored at 1/4 res.
import sys, subprocess, numpy as np, cv2
from ai_edge_litert.interpreter import Interpreter
model, src, out = sys.argv[1:4]
it=Interpreter(model_path=model); it.allocate_tensors()
I=it.get_input_details()[0]['index']; O=it.get_output_details()[0]['index']
W,H=1080,1920
p=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-vf','fps=30','-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
def seg(sq):
    x=cv2.resize(cv2.cvtColor(sq,cv2.COLOR_BGR2RGB),(256,256)).astype(np.float32)/255
    it.set_tensor(I,x[None]); it.invoke(); return cv2.resize(it.get_tensor(O)[0,...,0],(1080,1080))
masks=[]; prev=None
while True:
    b=p.stdout.read(W*H*3)
    if len(b)<W*H*3: break
    f=np.frombuffer(b,np.uint8).reshape(H,W,3)
    m=np.zeros((H,W),np.float32)
    a=seg(f[0:1080])
    m[0:1080]=a
    # below the hips: extend the hip-width column profile downward (legs stay within it)
    prof=a[1000:1080].max(0)
    m[1080:]=prof[None,:]*np.linspace(1,0.85,H-1080)[:,None]
    m=cv2.resize(m,(W//4,H//4),interpolation=cv2.INTER_AREA)
    prev=m if prev is None else 0.55*m+0.45*prev
    masks.append((np.clip(prev,0,1)*255).astype(np.uint8))
np.save(out,np.stack(masks)); print(len(masks))
