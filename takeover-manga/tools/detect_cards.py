import cv2, numpy as np, json
from PIL import Image
plate=Image.open('render/p5c2.webp').convert('RGB'); W,H=plate.size
bgr=cv2.cvtColor(np.array(plate),cv2.COLOR_RGB2BGR); gray=cv2.cvtColor(bgr,cv2.COLOR_BGR2GRAY).astype(np.float32)
dbg=bgr.copy()
# local std (texture): cards/screens are SMOOTH; screentone background is noisy
m=cv2.blur(gray,(9,9)); sq=cv2.blur(gray*gray,(9,9)); std=cv2.sqrt(np.clip(sq-m*m,0,None))
def find(x0,x1,y0,y1,lo,hi,smooth=16,armin=.0025,armax=.03,asp=(1.15,2.1)):
    roi=np.zeros((H,W),np.uint8); roi[int(y0*H):int(y1*H),int(x0*W):int(x1*W)]=1
    th=(((gray>lo)&(gray<hi)&(std<smooth))&(roi>0)).astype(np.uint8)
    th=cv2.morphologyEx(th,cv2.MORPH_CLOSE,np.ones((7,7),np.uint8))
    th=cv2.morphologyEx(th,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
    cnts,_=cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    best=None;bs=0
    for c in cnts:
        a=cv2.contourArea(c)
        if a<armin*W*H or a>armax*W*H: continue
        (rx,ry),(rw,rh),ang=cv2.minAreaRect(c)
        if min(rw,rh)<5: continue
        r=max(rw,rh)/min(rw,rh)
        if not asp[0]<=r<=asp[1]: continue
        rectangularity=a/(rw*rh)
        if rectangularity<0.7: continue
        if a>bs: bs=a; best=((rx,ry),(rw,rh),ang)
    return best
def rec(rect,col,label):
    if not rect: print(label,'NOT FOUND'); return None
    box=cv2.boxPoints(rect).astype(int); cv2.drawContours(dbg,[box],0,col,3)
    (rx,ry),(rw,rh),ang=rect
    # normalize angle so longer side is 'width'
    if rw<rh: ang=ang+90; rw,rh=rh,rw
    d=dict(cx=round(rx/W*100,1),cy=round(ry/H*100,1),w=round(rw/W*100,1),h=round(rh/W*100,1),ang=round(ang,1))
    print(label,d); return d
out={}
out['card1']=rec(find(0.46,0.62,0.13,0.27,200,256,14,.0015,.012),(0,140,255),'card1')
out['card4']=rec(find(0.60,0.94,0.60,0.82,200,256,16,.004,.03),(0,140,255),'card4')
out['screen']=rec(find(0.56,0.80,0.80,0.97,120,215,18,.003,.03,(1.1,2.6)),(255,0,255),'screen')
json.dump(out,open('cards_geom.json','w'))
cv2.imwrite('render/p5_debug2.png',dbg)
