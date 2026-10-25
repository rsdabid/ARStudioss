# Example sound-design pass for the worked example. For a new video, rebuild EV (event list)
# so every whoosh/pop/tick lands on that edit's graphic events, and set DUR.
# usage: sfx_example.py OUT_WAV
import numpy as np, wave, sys
SR=48000; DUR=28.24; rng=np.random.default_rng(7)
L=np.zeros(int(SR*DUR)+SR); R=np.zeros_like(L)
def env(n,a,d): t=np.arange(n)/SR; return np.minimum(1,t/max(a,1e-4))*np.exp(-t/d)
def onepole_lp(x,fc):
    y=np.zeros_like(x); s=0.0; fc=np.broadcast_to(fc,x.shape)
    a=1-np.exp(-2*np.pi*fc/SR)
    for i in range(len(x)): s+=a[i]*(x[i]-s); y[i]=s
    return y
def whoosh(dur=0.4,f0=400,f1=5000,peak=0.6):
    n=int(SR*dur); x=rng.standard_normal(n); t=np.linspace(0,1,n)
    fc=f0*(f1/f0)**np.sin(np.pi*t*0.5+0.0)  # sweep up
    y=onepole_lp(x,fc); y=y-onepole_lp(y,150)
    e=np.sin(np.pi*np.clip(t/peak,0,1)*0.5)**2*np.where(t<peak,1,np.exp(-(t-peak)/(0.25*(1-peak)+1e-3)))
    y*=e; return y/np.abs(y).max(), np.linspace(-0.6,0.6,n)
def pop(f0=950,f1=320,d=0.06):
    n=int(SR*0.18); t=np.arange(n)/SR
    f=f1+(f0-f1)*np.exp(-t/0.02); ph=2*np.pi*np.cumsum(f)/SR
    y=np.sin(ph)*env(n,0.002,d); y[:96]+=rng.standard_normal(96)*np.linspace(0.6,0,96)
    return y/np.abs(y).max(), np.zeros(n)
def tick():
    n=int(SR*0.03); x=rng.standard_normal(n); y=x-onepole_lp(x,2500); y*=env(n,0.0005,0.004)
    return y/np.abs(y).max(), np.zeros(n)
def shimmer():
    n=int(SR*1.5); t=np.arange(n)/SR; y=np.zeros(n)
    for f in (4700,7050,9400,11600,14000):
        y+=np.sin(2*np.pi*f*(1+rng.uniform(-.002,.002))*t+rng.uniform(0,6))*(0.6+0.4*np.sin(2*np.pi*rng.uniform(5,9)*t))
    y*=env(n,0.03,0.45); return y/np.abs(y).max(), 0.3*np.sin(2*np.pi*1.3*t)
def impact():
    n=int(SR*0.7); t=np.arange(n)/SR
    y=np.sin(2*np.pi*(55+60*np.exp(-t/0.05))*t)*env(n,0.002,0.22)
    nz=rng.standard_normal(n); nz=onepole_lp(nz,np.full(n,1800.0))*env(n,0.001,0.05)
    y=y+0.8*nz/np.abs(nz).max(); return y/np.abs(y).max(), np.zeros(n)
def add(t,snd,g):
    y,pan=snd; i=int(t*SR); n=min(len(y),len(L)-i)
    L[i:i+n]+=y[:n]*g*np.sqrt(0.5*(1-pan[:n])); R[i:i+n]+=y[:n]*g*np.sqrt(0.5*(1+pan[:n]))
EV=[(0.00,whoosh(0.45,300,7000,0.35),0.30),(0.28,whoosh(0.40,500,6000,0.5),0.22),(4.72,whoosh(0.30,1200,9000,0.4),0.18),
    (5.88,whoosh(0.30,400,6000,0.5),0.18),(7.45,whoosh(0.5,300,3000,0.5),0.12),(12.52,whoosh(0.25,600,8000,0.5),0.18),
    (13.50,whoosh(0.25,600,8000,0.5),0.18),(16.38,whoosh(0.35,300,5000,0.5),0.18),(22.40,whoosh(0.35,300,6000,0.3),0.22),
    (24.50,whoosh(0.25,600,8000,0.5),0.18),(22.40,impact(),0.32),(24.55,shimmer(),0.07)]
for t in (1.94,2.96,3.86,7.30,9.64,15.28,18.66,20.46,24.38): EV.append((t,pop(700,250,0.05),0.16))
for t in (6.05,6.18,8.10,24.85,26.46,26.80,27.08): EV.append((t,pop(),0.20))
EV.append((25.20,pop(1500,900,0.05),0.18))
for t in [12.77,12.89,13.01]+[13.75+0.12*k for k in range(5)]+[16.38,17.34,18.08]: EV.append((t,tick(),0.14))
for t,s,g in EV: add(t,s,g)
out=np.stack([L,R],1)[:int(SR*DUR)]
w=wave.open(sys.argv[1],'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((np.clip(out,-1,1)*32767).astype(np.int16).tobytes()); w.close()
print('peak',np.abs(out).max())
