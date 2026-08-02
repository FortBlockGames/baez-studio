import json, numpy as np, cv2
from PIL import Image
plate=Image.open('render/p5c2.webp').convert('RGBA'); W,H=plate.size
L='render/logos_trim/'
def place(path,cx,cy,wpct,ang=0):
    lg=Image.open(path).convert('RGBA')
    tw=max(1,int(wpct/100*W)); sc=tw/lg.width; lg=lg.resize((tw,max(1,int(lg.height*sc))),Image.LANCZOS)
    if ang: lg=lg.rotate(ang,expand=True,resample=Image.BICUBIC)
    px=int(cx/100*W-lg.width/2); py=int(cy/100*H-lg.height/2)
    layer=Image.new('RGBA',(W,H),(0,0,0,0)); layer.alpha_composite(lg,(px,py)); plate.alpha_composite(layer)

# 1) banners
bn={'chickows':(11.9,40.0,7.8),'aquafeelya':(23.2,41.7,7.2),'vital-vibe':(34.0,44.4,6.8),
 'digi-u':(44.6,45.7,6.6),'dollar-holler':(55.4,45.7,6.6),'puf':(66.0,44.5,6.8),
 'log':(77.3,44.3,7.0),'sentioids':(88.9,42.8,7.8)}
for n,(cx,cy,wp) in bn.items(): place(L+n+'.png',cx,cy,round(wp*0.82,1))
# 2) wrist screen sigil (clean, NO glow box)
place(L+'log.png',66.0,86.0,7.0,ang=16)

# snapshot AFTER banners/screen, BEFORE cards -> used to restore foreground occluders (fingers/thumb)
orig=np.array(plate); gorig=np.array(plate.convert('L'))
g=json.load(open('cards_geom.json'))
def card_and_restore(card):
    place(L+'takeover-dark.png',card['cx'],card['cy'],round(card['w']*0.82,1),ang=-card['ang'])
    # bbox around card
    cx=card['cx']/100*W; cy=card['cy']/100*H; half=card['w']/100*W*0.75
    x0,x1=int(cx-half),int(cx+half); y0,y1=int(cy-half),int(cy+half)
    bb=np.zeros((H,W),bool); bb[max(0,y0):y1,max(0,x0):x1]=True
    # clean white card face = bright, largest connected component within bbox
    white=((gorig>216)&bb).astype(np.uint8)
    white=cv2.morphologyEx(white,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
    n,lab,st,ce=cv2.connectedComponentsWithStats(white,8)
    face=np.zeros((H,W),bool)
    if n>1:
        bi=1+int(np.argmax(st[1:,4])); face=cv2.dilate((lab==bi).astype(np.uint8),np.ones((3,3),np.uint8)).astype(bool)
    occ=bb & ~face                      # everything in bbox that isn't the card face = foreground (finger/thumb/bg)
    pa=np.array(plate); pa[occ]=orig[occ];
    return Image.fromarray(pa)
plate=card_and_restore(g['card1'])
plate=card_and_restore(g['card4'])
plate.convert('RGB').save('render/p5_baked.png'); print('baked (finger-occlusion + no glow)')
