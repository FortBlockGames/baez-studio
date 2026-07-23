# Row-band banner centering: place each crest at the banner's center AT THE LOGO HEIGHT
# (accounts for banner lean/taper), not the whole-banner centroid.
import numpy as np, json, sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB'); a=np.asarray(im).astype(float)
H,W,_=a.shape
r,g,b=a[:,:,0],a[:,:,1],a[:,:,2]
mx,mn=a.max(2),a.min(2); sat=mx-mn
d=(mx-mn); d[d==0]=1
hue=np.zeros((H,W))
mr=(mx==r); mg=(mx==g)&~mr; mb=(mx==b)&~mr&~mg
hue[mr]=(((g-b)/d)[mr]%6); hue[mg]=(((b-r)/d)[mg]+2); hue[mb]=(((r-g)/d)[mb]+4); hue*=60
band=np.zeros((H,W),bool); band[int(.33*H):int(.60*H),:]=True
def col_mask(hc,tol,smin=45): 
    dh=np.abs((hue-hc+180)%360-180); return band&(sat>smin)&(dh<tol)
masks={'chickows':col_mask(6,22),'dollar-holler':col_mask(48,16),'digi-u':col_mask(130,30),
 'vital-vibe':col_mask(172,22),'aquafeelya':col_mask(212,26),'puf':col_mask(268,30)}
# log (black banner): dark; sentioids (white): bright — via x-band column peak
def dark_mask(): return band&(mx<70)
def bright_mask(): return band&(mn>232)
def place(mask, xlo=0, xhi=100):
    m=mask.copy(); m[:, :int(xlo/100*W)]=False; m[:, int(xhi/100*W):]=False
    ys,xs=np.where(m)
    if len(xs)<300: return None
    # column histogram -> dominant banner x cluster
    hist=np.bincount(xs,minlength=W); hh=np.convolve(hist,np.ones(31)/31,'same')
    cxpx=int(np.argmax(hh)); sel=np.abs(xs-cxpx)<0.06*W
    ys2,xs2=ys[sel],xs[sel]
    py=float(np.median(ys2))                      # logo height = median y of the banner cluster
    rowsel=np.abs(ys2-py)<0.03*H                  # narrow row band at that height
    cx=float(xs2[rowsel].mean()) if rowsel.sum()>20 else float(xs2.mean())
    return [round(cx/W*100,1), round(py/H*100,1)]
out={}
for n,m in masks.items(): out[n]=place(m)
out['log']=place(dark_mask(),63,88)
out['sentioids']=place(bright_mask(),84,99)
json.dump(out, open('banner_coords.json','w'))
print(json.dumps(out))
