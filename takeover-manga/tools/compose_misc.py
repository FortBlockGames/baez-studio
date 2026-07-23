import numpy as np, cv2
from PIL import Image
L='render/logos_trim/'
def paste(plate,path,cx,cy,wpct,mask=None):
    W,H=plate.size; lg=Image.open(path).convert('RGBA')
    tw=max(1,int(wpct/100*W)); sc=tw/lg.width; lg=lg.resize((tw,max(1,int(lg.height*sc))),Image.LANCZOS)
    px=int(cx/100*W-lg.width/2); py=int(cy/100*H-lg.height/2)
    layer=Image.new('RGBA',(W,H),(0,0,0,0)); layer.alpha_composite(lg,(px,py))
    if mask is not None:
        la=np.array(layer); la[...,3]=(la[...,3]*mask).astype(np.uint8); layer=Image.fromarray(la)
    plate.alpha_composite(layer); return plate

# COVER: TAKEOVER-white centered in the top black band
cov=Image.open('cover.webp').convert('RGBA'); W,H=cov.size
g=np.array(cov.convert('L')); rows=g.mean(1)
band=np.where(rows<45)[0]
if len(band): cy=(band.min()+band.max())/2/H*100
else: cy=4.0
cov=paste(cov,L+'takeover-white.png',50,cy,46)
cov.convert('RGB').save('render/cover_baked.png'); print('cover band cy=%.1f'%cy)

# PAGE 2: Vital Vibe logo on the teal hologram (detect teal, mask to it)
p2=Image.open('render/p2c2.webp').convert('RGBA'); W,H=p2.size
hsv=cv2.cvtColor(cv2.cvtColor(np.array(p2.convert('RGB')),cv2.COLOR_RGB2BGR),cv2.COLOR_BGR2HSV)
teal=((hsv[:,:,0]>78)&(hsv[:,:,0]<100)&(hsv[:,:,1]>80)&(hsv[:,:,2]>80)).astype(np.uint8)
teal=cv2.morphologyEx(teal,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
ys,xs=np.where(teal>0)
cx=xs.mean()/W*100; 
ytop=ys.min(); cyv=(ytop+0.32*(ys.max()-ytop))/H*100   # upper third of the cone (widest)
mask=teal.astype(bool)
p2=paste(p2,L+'vital-vibe.png',round(cx,1),round(cyv,1),13,mask=mask)
p2.convert('RGB').save('render/p2_baked.png'); print('P2 teal cx=%.1f cy=%.1f'%(cx,cyv))
