from pathlib import Path
exec(open(Path(__file__).with_name('tower_v2.py')).read().split('# Concierge')[0])
S=lambda s:struct.pack('>H',len(s.encode()))+s.encode()
def payload(t,v):
 if t==3:return struct.pack('>i',v)
 if t==8:return S(v)
 if t==9:
  typ,arr=v;return bytes([typ])+struct.pack('>i',len(arr))+b''.join(payload(typ,x) for x in arr)
 if t==10:return b''.join(bytes([typ])+S(k)+payload(typ,val) for k,(typ,val) in v.items())+b'\0'
 raise ValueError(t)
locs=['01_peron','02_ocean','03_teatr','04_ogrod','05_serce']
COL={'polished_deepslate':'#353d50','calcite':'#e1ded0','deepslate_tiles':'#273142','cut_copper':'#b8804d','waxed_oxidized_cut_copper':'#477f77','blackstone':'#242c3b','sea_lantern':'#c2e9e1','glass':'#76b9c9','water':'#367dba','dark_oak_planks':'#614235','red_wool':'#a63b51','white_wool':'#e8e0cd','cherry_leaves':'#d69eae','cherry_log':'#745461','moss_block':'#607956','quartz_block':'#e8e1d5','rail':'#b7a381','iron_bars':'#73808a','gold_block':'#d3ad5c','light_blue_stained_glass':'#6ea0c0','spruce_planks':'#95754d','copper_block':'#ba794c','amethyst_block':'#776496','chiseled_stone_bricks':'#86858c','stone_bricks':'#94939b','dark_oak_fence':'#60412d','quartz_stairs':'#e8e1d5'}
for idx,ident in enumerate(locs):
 B={}
 def put(x,y,z,b):
  if 0<=x<47 and 0<=z<47 and 0<=y<35:B[x,y,z]='minecraft:'+b
 def box(x0,y0,z0,x1,y1,z1,b):
  for x in range(x0,x1+1):
   for y in range(y0,y1+1):
    for z in range(z0,z1+1):put(x,y,z,b)
 def clear(x0,y0,z0,x1,y1,z1):
  for x in range(x0,x1+1):
   for y in range(y0,y1+1):
    for z in range(z0,z1+1):B.pop((x,y,z),None)
 # circular cutaway shell; back arches survive so interior renders readable
 for x in range(47):
  for z in range(47):
   r=math.hypot(x-23,z-23)
   if r<=22:
    put(x,0,z,'deepslate_tiles');put(x,1,z,'calcite' if (x//3+z//3)%2 else 'polished_deepslate')
   if 21<=r<=22:
    for y in range(2,23):put(x,y,z,'calcite' if y in [2,12,13,22] else 'stone_bricks')
   if 18<=r<=21:
    put(x,12,z,'dark_oak_planks');put(x,13,z,'dark_oak_fence' if r<18.8 else 'calcite')
 # columns, decorative ribs, windows
 for a in range(0,360,30):
  ang=math.radians(a);x=round(23+20*math.cos(ang));z=round(23+20*math.sin(ang))
  box(x-1,2,z-1,x+1,3,z+1,'chiseled_stone_bricks');box(x,4,z,x,21,z,'calcite');box(x-1,20,z-1,x+1,22,z+1,'cut_copper');put(x,18,z-1,'sea_lantern')
 for x in [13,23,33]:
  for y in range(6,11):
   for xx in range(x-2,x+3):put(xx,y,42,'light_blue_stained_glass')
 # two 3-block wide dry steps reach gallery
 for k in range(11):
  for xx in [7,8,9,37,38,39]:
   for yy in range(2,2+k):put(xx,yy,12+k,'calcite')
   put(xx,2+k,12+k,'quartz_stairs')
 # entrance arch and facade windows
 clear(20,2,0,26,7,3)
 for a in range(15,360,30):
  ang=math.radians(a)
  for da in [-3,0,3]:
   aa=ang+math.radians(da);xx=round(23+21.5*math.cos(aa));zz=round(23+21.5*math.sin(aa))
   for yy in list(range(6,11))+list(range(15,20)):put(xx,yy,zz,'light_blue_stained_glass')
  xx=round(23+21.5*math.cos(ang));zz=round(23+21.5*math.sin(ang));put(xx,11,zz,'cut_copper');put(xx,20,zz,'cut_copper')
 # carpet approach
 box(21,2,2,25,2,10,'red_wool')
 if idx==0:
  # railway and detailed carriage
  for z in range(7,37):put(17,2,z,'rail');put(29,2,z,'rail')
  for z in range(13,32):
   for x in range(16,21):put(x,3,z,'blackstone');put(x,9,z,'waxed_oxidized_cut_copper')
  box(16,4,13,20,8,31,'red_wool');clear(17,4,14,19,8,30)
  for z in range(15,30,3):
   box(16,6,z,16,7,z+1,'glass');box(20,6,z,20,7,z+1,'glass');put(18,8,z,'sea_lantern')
  clear(20,4,20,20,6,22);box(19,4,21,19,5,21,'red_wool')
  for z in [13,18,26,31]:box(15,2,z,16,3,z,'blackstone');box(20,2,z,21,3,z,'blackstone')
  for x,z in [(10,29),(34,15),(34,29)]:box(x,2,z,x+2,3,z+1,'spruce_planks');put(x+1,4,z,'gold_block')
  box(22,16,35,24,22,35,'cut_copper')
  for a in range(12):
   ang=a*math.tau/12;put(round(23+4*math.cos(ang)),round(19+4*math.sin(ang)),34,'gold_block')
  box(23,19,34,23,22,34,'blackstone');box(23,19,34,25,19,34,'blackstone')
 if idx==1:
  # deep water basin, dry border and clear glass walkways
  box(12,2,13,34,6,35,'water');box(11,2,12,11,7,36,'glass');box(35,2,12,35,7,36,'glass');box(11,2,12,35,7,12,'glass')
  for z in range(13,36):
   for x in [21,22,23,24,25]:put(x,7,z,'glass')
  for x,z in [(15,18),(31,18),(15,30),(31,30)]:
   box(x,2,z,x,5,z,'quartz_block');put(x,6,z,'sea_lantern')
  box(21,8,32,25,8,36,'quartz_block');box(22,9,34,24,10,35,'cut_copper')
  for x in range(18,29):put(x,18,23,'cut_copper')
  for z in range(18,29):put(23,18,z,'cut_copper')
  for x,z in [(18,23),(28,23),(23,18),(23,28)]:box(x,16,z,x,17,z,'sea_lantern')
 if idx==2:
  # stage house, seating and wings
  box(13,2,28,33,5,39,'dark_oak_planks');box(14,6,38,32,16,38,'red_wool');clear(19,6,38,27,13,38)
  for row,z in enumerate([12,16,20,24]):
   for x in list(range(12,21,2))+list(range(26,35,2)):
    box(x,2,z,x,3,z,'red_wool');put(x,4,z+1,'red_wool');put(x,2,z+1,'dark_oak_planks')
  box(19,6,30,26,10,35,'spruce_planks');clear(20,6,31,25,9,34);clear(22,6,30,23,8,30);box(18,11,29,27,11,36,'waxed_oxidized_cut_copper')
  for x in [15,31]:box(x,6,30,x,18,30,'iron_bars');put(x,18,30,'sea_lantern')
  box(21,19,33,25,21,33,'red_wool');box(22,18,33,24,22,33,'red_wool')
  for x,z in [(16,33),(30,33),(28,29)]:box(x,6,z,x,8,z,'white_wool');put(x,9,z,'calcite')
 if idx==3:
  # ornamental garden with deliberate foliage tiers
  for x in range(10,37):
   for z in range(10,37):
    if x in [16,30] or z in [15,31]:put(x,2,z,'water')
    elif 18<x<28 or 20<z<26:put(x,2,z,'quartz_block')
    else:put(x,2,z,'moss_block')
  for x,z in [(12,17),(34,17),(12,32),(34,32)]:
   box(x,3,z,x,10,z,'cherry_log')
   for y,rad in [(9,4),(10,4),(11,3),(12,2)]:
    for xx in range(x-rad,x+rad+1):
     for zz in range(z-rad,z+rad+1):
      if abs(xx-x)+abs(zz-z)<=rad+2:put(xx,y,zz,'cherry_leaves')
  for x,z in [(20,16),(26,16),(20,32),(26,32)]:
   box(x-1,3,z-1,x+1,3,z+1,'quartz_block');box(x,4,z,x,6,z,'chiseled_stone_bricks');put(x,5,z-1,'gold_block')
  for x in [19,27]:box(x,3,36,x,10,36,'quartz_block')
  box(19,10,36,27,11,36,'cut_copper');box(22,3,35,24,3,37,'amethyst_block')
 if idx==4:
  for x in range(10,37):
   for z in range(10,37):
    rr=math.hypot(x-23,z-23)
    if rr<12:put(x,2,z,'quartz_block' if int(rr)%3 else 'cut_copper')
  for y,rad in [(16,9),(19,12),(22,9)]:
   for a in range(160):
    ang=a*math.tau/160;put(round(23+rad*math.cos(ang)),y,round(23+rad*math.sin(ang)),'cut_copper')
  box(21,12,21,25,17,25,'sea_lantern');box(22,11,22,24,18,24,'glass')
  for x,z in [(12,23),(34,23),(23,34)]:box(x-1,3,z-1,x+1,6,z+1,'blackstone');put(x,7,z,'amethyst_block')
  for x,z in [(18,23),(28,23),(23,18),(23,28)]:box(x,3,z,x,14,z,'waxed_oxidized_cut_copper')
 # restore safe stairs after decoration and clear three-block headroom
 for k in range(11):
  for xx in [7,8,9,37,38,39]:
   put(xx,2+k,12+k,'quartz_stairs')
   clear(xx,3+k,12+k,xx,5+k,12+k)
 palette=sorted(set(B.values()));blocks=[{'pos':(9,(3,list(pos))),'state':(3,palette.index(b))} for pos,b in B.items()]
 data={'DataVersion':(3,4189),'size':(9,(3,[47,35,47])),'palette':(9,(10,[dict(Name=(8,b),**({'Properties':(10,{'facing':(8,'south'),'half':(8,'bottom'),'shape':(8,'straight'),'waterlogged':(8,'false')})} if b=='minecraft:quartz_stairs' else {})) for b in palette])),'blocks':(9,(10,blocks)),'entities':(9,(10,[]))}
 p=R/f'04_DATAPACK/wieza/data/wieza/structure/{ident}.nbt';p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(gzip.compress(b'\x0a\0\0'+payload(10,data)))
 j(f'03_MAPY/{ident}/bloki.json',{'size':[47,35,47],'palette':palette,'blocks':[{'pos':pos,'state':palette.index(b)} for pos,b in B.items()]})
 # exact cutaway image with visible faces and depth sorting
 img=Image.new('RGB',(1400,1100),'#111b2b');draw=ImageDraw.Draw(img)
 def pr(x,y,z):return (700+(x-23)*14+(z-23)*10,760-y*14-(z-23)*6+(x-23)*4)
 faces=[]
 V={pos:b for pos,b in B.items() if not (pos[2]<12 and pos[1]>2)}
 for (x,y,z),b in V.items():
  col=COL.get(b.split(':')[1],'#888888');rgb=tuple(int(col[k:k+2],16) for k in (1,3,5))
  for nb,verts,shade in [((x,y,z-1),[(x,y,z),(x+1,y,z),(x+1,y+1,z),(x,y+1,z)],.8),((x+1,y,z),[(x+1,y,z),(x+1,y,z+1),(x+1,y+1,z+1),(x+1,y+1,z)],.65),((x,y+1,z),[(x,y+1,z),(x+1,y+1,z),(x+1,y+1,z+1),(x,y+1,z+1)],1.12)]:
   if nb not in V:faces.append((sum(v[0]*.7+v[1]*.5-v[2]*.8 for v in verts)/4,verts,tuple(min(255,int(v*shade)) for v in rgb)))
 for dep,vs,c in sorted(faces,key=lambda a:a[0]):draw.polygon([pr(*v) for v in vs],fill=c)
 draw.text((30,25),ident.upper()+' | ACTUAL NBT STRUCTURE / CUTAWAY / 47 x 35 x 47',fill='white');p=R/f'03_MAPY/{ident}/rzeczywista_struktura.png';p.parent.mkdir(parents=True,exist_ok=True);img.save(p)
 print(ident,len(B),'blocks')
w('04_DATAPACK/wieza/pack.mcmeta',json.dumps({'pack':{'pack_format':61,'description':'Wieza: piec dekorowanych struktur demonstracyjnych 1.21.4'}}))
w('04_DATAPACK/wieza/data/wieza/function/build.mcfunction','\n'.join(f'place template wieza:{id} {k*64} 80 0' for k,id in enumerate(locs))+'\ntellraw @a {"text":"Ustawiono piec struktur demonstracyjnych. Brak fabularnych interakcji.","color":"gold"}\n')
