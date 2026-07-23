import cv2, numpy as np, json
from PIL import Image
plate=Image.open('render/p5c2.webp').convert('RGB'); W,H=plate.size
bgr=cv2.cvtColor(np.array(plate),cv2.COLOR_RGB2BGR); gray=cv2.cvtColor(bgr,cv2.COLOR_BGR2GRAY)
# panel-4 lower-left wrist zone (below the card, which sits higher)
roi=np.zeros((H,W),np.uint8); roi[int(.81*H):int(.95*H),int(.55*W):int(.78*W)]=255
bright=((gray>150)&(roi>0)).astype(np.uint8)
bright=cv2.morphologyEx(bright,cv2.MORPH_CLOSE,np.ones((13,13),np.uint8))
bright=cv2.morphologyEx(bright,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
n,lab,stats,cent=cv2.connectedComponentsWithStats(bright,8)
dbg=bgr.copy(); best=None;ba=0
for i in range(1,n):
    x,y,w,h,area=stats[i]
    if area<0.003*W*H: continue
    asp=max(w,h)/max(1,min(w,h))
    if asp>2.6: continue
    cv2.rectangle(dbg,(x,y),(x+w,y+h),(0,255,0),2)
    if area>ba: ba=area; best=i
if best:
    comp=(lab==best).astype(np.uint8)
    cnts,_=cv2.findContours(comp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    (rx,ry),(rw,rh),ang=cv2.minAreaRect(max(cnts,key=cv2.contourArea))
    if rw<rh: ang+=90; rw,rh=rh,rw
    box=cv2.boxPoints(((rx,ry),(rw,rh) if rw>=rh else (rh,rw),ang)).astype(int)
    cv2.drawContours(dbg,[cv2.boxPoints(cv2.minAreaRect(max(cnts,key=cv2.contourArea))).astype(int)],0,(0,0,255),3)
    res=dict(cx=round(rx/W*100,1),cy=round(ry/H*100,1),w=round(rw/W*100,1),h=round(rh/W*100,1),ang=round(ang,1))
    json.dump(res,open('screen_geom.json','w')); print('SCREEN',res)
else: print('none')
cv2.imwrite('render/screen2_dbg.png',dbg)
