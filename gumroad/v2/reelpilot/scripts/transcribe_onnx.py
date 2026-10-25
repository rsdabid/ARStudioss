# Optional: word timings with a local ONNX Whisper export (no internet at run time).
# Most users should use words.py (faster-whisper) instead.
# usage: transcribe_onnx.py MODEL_DIR audio16k.wav ...
import sys, json, wave, numpy as np, onnxruntime as ort
from transformers import WhisperFeatureExtractor, WhisperTokenizer
from scipy.ndimage import median_filter
D=sys.argv[1]
fe=WhisperFeatureExtractor.from_pretrained(D); tok=WhisperTokenizer.from_pretrained(D)
enc=ort.InferenceSession(D+'/onnx/encoder_model_quantized.onnx'); dec=ort.InferenceSession(D+'/onnx/decoder_model_merged_quantized.onnx')
outn=[o.name for o in dec.get_outputs()]
HEADS=[(5,3),(5,9),(8,0),(8,4),(8,7),(8,8),(9,0),(9,7),(9,9),(10,5)]
def dtw(x):
    N,M=x.shape; c=np.full((N+1,M+1),np.inf); c[0,0]=0; t=np.zeros((N+1,M+1),int)
    for j in range(1,M+1):
        for i in range(1,N+1):
            a=[c[i-1,j-1],c[i-1,j],c[i,j-1]]; k=int(np.argmin(a)); c[i,j]=x[i-1,j-1]+a[k]; t[i,j]=k
    i,j=N,M; path=[]
    while i>0 or j>0:
        path.append((i-1,j-1)); k=t[i,j]
        if i==0: j-=1
        elif j==0: i-=1
        elif k==0: i-=1;j-=1
        elif k==1: i-=1
        else: j-=1
    return np.array(path[::-1]).T
for f in sys.argv[2:]:
    w=wave.open(f); a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
    nfr=len(a)//160
    feats=fe(a,sampling_rate=16000,return_tensors='np').input_features
    hs=enc.run(['last_hidden_state'],{'input_features':feats})[0]
    sot=tok.convert_tokens_to_ids(['<|startoftranscript|>','<|en|>','<|transcribe|>','<|notimestamps|>'])
    eot=tok.eos_token_id
    past={}
    for l in range(12):
        for k in ['decoder.key','decoder.value','encoder.key','encoder.value']: past[f'past_key_values.{l}.{k}']=np.zeros((1,12,0,64),np.float32)
    ids=list(sot); inp=np.array([ids],np.int64); cache=False; atts=[]; out=[]
    for step in range(200):
        r=dict(zip(outn,dec.run(None,{'input_ids':inp,'encoder_hidden_states':hs,'use_cache_branch':np.array([cache]),**past})))
        nxt=int(np.argmax(r['logits'][0,-1]))
        atts.append(np.stack([r[f'cross_attentions.{l}'][0,h] for l,h in HEADS]))  # heads x t x 1500
        for k in list(past):
            nk=k.replace('past_key_values','present')
            if cache and 'encoder' in k: continue
            past[k]=r[nk]
        cache=True
        if nxt==eot: break
        out.append(nxt); inp=np.array([[nxt]],np.int64)
    W=np.concatenate(atts,axis=1)[:, :, :nfr//2]   # heads x (len(sot)+len(out)) x frames
    W=(W-W.mean(-2,keepdims=True))/ (W.std(-2,keepdims=True)+1e-9)
    W=median_filter(W,(1,1,7)); m=W.mean(0)[len(sot)-1:len(sot)-1+len(out)+1]
    ti,tj=dtw(-m)
    jumps=np.pad(np.diff(ti),(1,0),constant_values=1).astype(bool); times=tj[jumps]/50.0
    words=[]; 
    for k,t in enumerate(out):
        s=tok.decode([t]); st=float(times[k]); en=float(times[k+1]) if k+1<len(times) else st+0.2
        if s.startswith(' ') or not words: words.append([round(st,2),round(en,2),s.strip()])
        else: words[-1][1]=round(en,2); words[-1][2]+=s
    json.dump(words,open(f.replace('.wav','.words.json'),'w'))
    print('==',f); print(tok.decode(out)); print(' '.join(f'[{s:.2f}]{t}' for s,e,t in words))
