from pathlib import Path
import json,uuid,base64,io,math,struct,gzip,zipfile,hashlib
import numpy as np
from PIL import Image,ImageDraw,ImageFont
R=Path(__file__).resolve().parents[1];R.mkdir(exist_ok=True)
def w(p,s):
 p=R/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
def j(p,v):w(p,json.dumps(v,ensure_ascii=False,indent=2))
M={}
def cube(arr,n,o,s,mat,bone='body'):arr.append(dict(name=n,origin=list(o),size=list(s),mat=mat,bone=bone))
# palette tiles: cloth, edge, metal, stone, skin, black, glow, red, ivory, glass
colors=['#253249','#445778','#a87a42','#787f8b','#d9bca0','#111823','#73d8dc','#a73248','#e8dfc9','#427f92']
# Concierge
A=[]
cube(A,'coat',( -4,8,-2.5),(8,14,5),0)
for x in [-4,-2,0,2]:cube(A,'coat_fold',(x,2,-2.7),(2,9,5.4),0)
for x in [-3.5,1]:cube(A,'boot',(x,0,-3),(2.5,4,5),5,'left_leg' if x<0 else 'right_leg')
cube(A,'collar',(-5,20,-3),(10,2,6),1)
cube(A,'head',(-3.5,22,-3.5),(7,7,7),8,'head')
cube(A,'beak',(-1,24,-7),(2,2,4),2,'head')
for x in [-2.5,1.5]:cube(A,'eye',(x,26,-3.8),(1,1,.4),6,'head')
cube(A,'hat_brim',(-5,28,-5),(10,1,10),5,'head');cube(A,'hat',(-3.5,29,-3.5),(7,4,7),0,'head');cube(A,'hat_band',(-3.7,29.5,-3.7),(7.4,1,7.4),7,'head')
for x,bo in [(-7,'left_arm'),(4,'right_arm')]:
 cube(A,'sleeve',(x,11,-2),(3,10,4),0,bo);cube(A,'cuff',(x-.2,10,-2.2),(3.4,2,4.4),2,bo);cube(A,'hand',(x+.5,8.5,-1.5),(2,2,3),8,bo)
for y in [11,14,17,20]:cube(A,'button',(-.5,y,-2.9),(1,1,.5),2)
cube(A,'belt',(-4.2,9,-2.7),(8.4,1,5.4),2);cube(A,'ticket',(5,8,-4),(3,3,.4),8,'right_arm')
M['konduktor']=A
# bell diver quadruped with tank and gridded face
A=[];cube(A,'shell',(-5,8,-4),(10,10,8),2);cube(A,'helmet',(-5,17,-5),(10,9,10),2,'head');cube(A,'helmet_top',(-4,26,-4),(8,1,8),1,'head');cube(A,'window',(-3.5,19,-5.2),(7,5,.5),9,'head')
for x in [-3.5,0,3]:cube(A,'window_bar',(x,19,-5.8),(.5,5,.5),2,'head')
for y in [19,23.5]:cube(A,'window_rim',(-4,y,-5.6),(8,.5,.5),8,'head')
for x in [-2,1]:cube(A,'eye',(x,21,-5.5),(1,1,.2),6,'head')
for x,z,bo in [(-8,-4,'left_leg'),(5,-4,'right_leg'),(-8,3,'back_left'),(5,3,'back_right')]:
 cube(A,'leg_upper',(x,5,z),(3,7,3),1,bo);cube(A,'knee',(x-.3,4,z-.3),(3.6,2,3.6),2,bo);cube(A,'foot',(x-.5,1,z-1),(4,4,5),5,bo)
for x in [-3,1]:cube(A,'air_tank',(x,8,4),(2.5,11,3),1)
for y in [10,16]:cube(A,'tank_band',(-4,y,4),(8,1,3),2)
cube(A,'chest_light',(-2,11,-4.3),(4,3,.5),6)
for x in [-4,3]:
 for y in [9,16]:cube(A,'rivet',(x,y,-4.3),(1,1,.5),8)
M['nurek_dzwonowy']=A
# marionette deer actress
A=[];cube(A,'dress',(-4,11,-2.5),(8,11,5),7)
for x in [-6,-4,-2,0,2,4]:cube(A,'skirt',(x,4,-4),(2,8,8),7 if x in [-6,0,4] else 0)
cube(A,'waist',(-4.2,11,-2.7),(8.4,1,5.4),2);cube(A,'neck',(-1,22,-1),(2,2,2),2,'head');cube(A,'mask',(-3,24,-3),(6,7,5),8,'head');cube(A,'snout',(-2,24,-5),(4,3,2),8,'head')
for x in [-2.5,1.5]:cube(A,'eye',(x,28,-3.4),(1,1,.4),5,'head')
for x in [-4,3]:
 cube(A,'antler',(x,30,-1),(1,6,1),2,'head');cube(A,'antler_branch',(x-1,33,-1),(3,1,1),2,'head')
for x,bo in [(-7,'left_arm'),(5,'right_arm')]:
 cube(A,'upper_arm',(x,16,-1),(2,6,2),8,bo);cube(A,'joint',(x-.3,15,-1.3),(2.6,2.6,2.6),2,bo);cube(A,'forearm',(x,9,-1),(2,6,2),8,bo);cube(A,'hand',(x-.2,7,-1.3),(2.4,2,2.6),5,bo)
for x,bo in [(-3,'left_leg'),(1,'right_leg')]:cube(A,'leg',(x,0,-1),(2,7,2),8,bo);cube(A,'shoe',(x-.2,0,-2),(2.4,2,4),5,bo)
for x in [-7,6]:cube(A,'string',(x,21,0),(.25,17,.25),8,'left_arm' if x<0 else 'right_arm')
cube(A,'control_bar',(-9,38,-1),(18,1,2),2)
M['aktorka_bez_roli']=A
# sibling explorer
A=[];cube(A,'torso',(-4,12,-2),(8,12,4),0);cube(A,'vest',(-4.2,14,-2.2),(8.4,8,4.4),1);cube(A,'belt',(-4.3,12,-2.3),(8.6,1,4.6),2)
for x,bo in [(-4,'left_leg'),(1,'right_leg')]:cube(A,'trousers',(x,3,-2),(3,9,4),0,bo);cube(A,'boot',(x-.2,0,-3),(3.4,4,5),5,bo)
cube(A,'head',(-4,24,-4),(8,8,8),4,'head');cube(A,'hair_top',(-4,31,-4),(8,2,8),5,'head');cube(A,'hair_back',(-4,25,3),(8,7,1),5,'head');cube(A,'hair_side',(-4.3,27,-3),(1,5,6),5,'head');cube(A,'fringe',(-4,30,-4.3),(5,2,.5),5,'head')
for x in [-2.5,1.5]:cube(A,'eye',(x,27,-4.15),(1,1,.2),6,'head')
cube(A,'scarf',(-4.5,22,-2.5),(9,2,5),7);cube(A,'scarf_tail',(2,15,-2.7),(2,8,.5),7)
for x,bo in [(-7,'left_arm'),(4,'right_arm')]:
 cube(A,'sleeve',(x,15,-2),(3,9,4),0,bo);cube(A,'cuff',(x,14,-2),(3,1,4),2,bo);cube(A,'hand',(x,12,-2),(3,2,4),4,bo)
cube(A,'bag',(-3,14,2.5),(6,7,3),2);cube(A,'buckle',(-.5,15,5.5),(1,2,.4),8)
M['ida']=A
# boss bell angel
A=[];cube(A,'torso',(-7,16,-4),(14,16,8),5);cube(A,'chest_frame',(-5,21,-4.6),(10,8,1),2);cube(A,'core',(-3,23,-5),(6,4,.5),6);cube(A,'neck',(-2,32,-2),(4,3,4),2,'head');cube(A,'head',(-4,35,-3),(8,8,6),8,'head');cube(A,'face_line',(-.5,36,-3.3),(1,6,.4),5,'head')
for x,bo in [(-6,'left_leg'),(2,'right_leg')]:cube(A,'shin',(x,0,-3),(4,16,6),5,bo);cube(A,'greave',(x-.3,2,-3.3),(4.6,9,6.6),2,bo)
for x,bo in [(-12,'left_arm'),(8,'right_arm')]:cube(A,'shoulder',(x-1,28,-4),(6,5,8),2,bo);cube(A,'arm',(x,15,-2),(4,14,4),5,bo);cube(A,'hand',(x-.5,11,-2.5),(5,4,5),8,bo)
for side,bo in [(-1,'wing_left'),(1,'wing_right')]:
 for k in range(6):
  x=(-12-k*3) if side<0 else (8+k*3);cube(A,'wing_blade',(x,19+k*2,3),(4,15-k,1.5),2 if k%2==0 else 8,bo)
for a in range(12):
 ang=a*math.tau/12;cube(A,'halo',(-1+12*math.cos(ang),40+12*math.sin(ang),3),(2,2,2),2,'halo')
M['aniol_minuty']=A
# surface construction details: tailored hems, armor rims, mechanical fittings
A=M['konduktor']
for x in [-3.8,3.5]:cube(A,'coat_seam',(x,3,-2.85),(.35,18,.35),1)
for x in [-3,-1,1,3]:cube(A,'hem_stitch',(x,2,-2.9),(.8,.35,.35),2)
for x in [-3,2]:cube(A,'lapel',(x,18,-2.9),(1.1,3,.5),1)
cube(A,'mask_brow',(-3.5,27.2,-3.9),(7,.6,.5),5,'head')
for x in [-2.5,1.5]:cube(A,'eye_frame',(x-.25,25.8,-3.9),(1.5,1.5,.2),2,'head');cube(A,'eye_inlay',(x,26,-4.15),(1,1,.2),6,'head')
cube(A,'hat_badge',(-.7,30,-3.9),(1.4,1.5,.35),2,'head');cube(A,'ticket_mark',(5.5,9,-4.3),(2,.4,.2),7,'right_arm')
for x,bo in [(-3.5,'left_leg'),(1,'right_leg')]:cube(A,'sole',(x-.15,0,-3.15),(2.8,.6,5.3),1,bo)
A=M['nurek_dzwonowy']
for q in A:
 if q['name']=='shell':q['mat']=7
 if q['name']=='air_tank':q['mat']=8
for x in [-5.2,4.7]:cube(A,'helmet_corner',(x,17,-5.4),(.5,9,.5),8,'head')
for y in [17,25.5]:cube(A,'helmet_edge',(-5.2,y,-5.4),(10.4,.5,.5),8,'head')
for x in [-4.5,3.7]:
 for y in [18,24]:cube(A,'helmet_bolt',(x,y,-5.7),(.7,.7,.3),5,'head')
for x in [-6,5]:
 cube(A,'side_port',(x,20,-2),(1,4,4),5,'head');cube(A,'side_port_trim',(x-.2,21,-1),(1.4,2,2),2,'head')
cube(A,'helmet_rim',(-5.4,17,-5.4),(10.8,.7,10.8),1,'head');cube(A,'top_vent',(-2.5,27,-2.5),(5,.7,5),5,'head')
for x in [-2.5,2]:cube(A,'top_vent_bar',(x,27.7,-2.5),(.5,.4,5),2,'head')
for y in [9,16.5]:cube(A,'chest_border',(-5.3,y,-4.5),(10.6,.6,.6),2)
for x in [-4.8,4.2]:cube(A,'chest_edge',(x,9,-4.5),(.6,8,.6),2)
for x,z,bo in [(-8,-4,'left_leg'),(5,-4,'right_leg'),(-8,3,'back_left'),(5,3,'back_right')]:
 cube(A,'shin_plate',(x-.2,2,z-.45),(3.4,3,.7),8,bo);cube(A,'shin_band',(x-.3,3,z-.65),(3.6,.7,1),2,bo);cube(A,'boot_sole',(x-.7,.5,z-1.2),(4.4,.7,5.4),1,bo);cube(A,'knee_bolt',(x+.8,4.6,z-.65),(1,1,.4),5,bo)
for x in [-3,1]:
 for y in [8,18.3]:cube(A,'tank_cap',(x-.2,y,3.8),(2.9,.7,3.4),2)
A=M['aktorka_bez_roli']
for x in [-6,-4,-2,0,2,4]:cube(A,'dress_hem',(x,4,-4.3),(2,.6,.5),2)
for x in [-3,2]:cube(A,'bodice_trim',(x,12,-2.9),(.5,9,.5),2)
for y in [15,18,20]:cube(A,'dress_button',(-.4,y,-3),(.8,.8,.4),8)
cube(A,'mask_forehead',(-2.5,30,-3.25),(5,.6,.35),2,'head');cube(A,'snout_nose',(-.6,25,-5.4),(1.2,.8,.5),5,'head')
for x in [-2.5,1.5]:cube(A,'eyebrow',(x-.1,29.2,-3.25),(1.2,.4,.35),2,'head')
for x,bo in [(-7,'left_arm'),(5,'right_arm')]:cube(A,'joint_pin',(x+.5,15.6,-1.7),(1,1,.5),5,bo)
A=M['ida']
for x in [-2.7,1.3]:cube(A,'eyebrow',(x,28.3,-4.3),(1.4,.3,.3),5,'head')
cube(A,'mouth',(-.7,25.5,-4.25),(1.4,.3,.25),7,'head')
for x in [-3.3,1]:
 cube(A,'vest_pocket',(x,15,-2.5),(2.4,3,.6),0);cube(A,'pocket_flap',(x,17,-2.8),(2.4,.6,.8),2)
cube(A,'vest_zip',(-.2,14,-2.6),(.4,8,.6),2);cube(A,'belt_buckle',(-1,12,-2.7),(2,1.3,.5),8)
for x,bo in [(-4,'left_leg'),(1,'right_leg')]:cube(A,'boot_sole',(x-.3,0,-3.2),(3.6,.6,5.4),1,bo);cube(A,'boot_strap',(x-.25,2.5,-3.2),(3.5,.7,.4),2,bo)
cube(A,'bag_flap',(-3.3,19,2.6),(6.6,2,3.2),1)
A=M['aniol_minuty']
for x in [-6,5.5]:cube(A,'torso_edge',(x,17,-4.4),(.5,14,.6),2)
for y in [17,30.5]:cube(A,'torso_band',(-6,y,-4.5),(12,.5,.6),2)
for x in [-4.5,3.5]:
 for y in [21.5,27.5]:cube(A,'core_rivet',(x,y,-5),(1,1,.5),8)
for x,bo in [(-6,'left_leg'),(2,'right_leg')]:
 cube(A,'knee_cap',(x-.5,12,-3.8),(5,3,1),8,bo);cube(A,'boot',(x-.5,0,-4),(5,2,8),5,bo);cube(A,'sole',(x-.7,0,-4.2),(5.4,.6,8.4),2,bo);cube(A,'greave_inlay',(x+1.5,3,-3.9),(1,7,.5),8,bo)
for x,bo in [(-12,'left_arm'),(8,'right_arm')]:
 cube(A,'shoulder_rim',(x-1,28,-4.5),(6,.6,9),8,bo);cube(A,'arm_inlay',(x+1.5,16,-2.5),(1,10,.6),2,bo)
for side,bo in [(-1,'wing_left'),(1,'wing_right')]:
 for k in range(6):
  x=(-12-k*3) if side<0 else (8+k*3);cube(A,'wing_ridge',(x,19+k*2,2.7),(1,15-k,.4),5,bo)

# generate textures, models and high quality exact geometry previews
for ident,arr in M.items():
 P=R/'02_MODELE'/ident;P.mkdir(parents=True,exist_ok=True)
 atlas=Image.new('RGB',(128,128),'#111823');d=ImageDraw.Draw(atlas)
 for mat,col in enumerate(colors):
  tx=(mat%4)*32;ty=(mat//4)*32;c=tuple(int(col[i:i+2],16) for i in (1,3,5))
  for y in range(32):
   for x in range(32):
    noise=((x*17+y*31+mat*13)%9)-4
    if mat in [2,3,8]:noise+=3 if (x+y)%11==0 else 0
    if mat in [0,1,7]:noise+=4 if x%7==0 else -1
    atlas.putpixel((tx+x,ty+y),tuple(max(0,min(255,v+noise)) for v in c))
  d.line((tx,ty,tx+31,ty),fill=tuple(min(255,v+20) for v in c));d.line((tx,ty,tx,ty+31),fill=tuple(min(255,v+14) for v in c))
 atlas.save(P/'tekstura_128.png');bio=io.BytesIO();atlas.save(bio,format='PNG')
 bones={};elements=[];bbgroups=[];boneids={bo:str(uuid.uuid4()) for bo in set(a['bone'] for a in arr)}
 pivots={'body':[0,16,0],'head':[0, {'konduktor':22,'nurek_dzwonowy':17,'aktorka_bez_roli':24,'ida':24,'aniol_minuty':35}[ident],0],'left_arm':[-5,22,0],'right_arm':[5,22,0],'left_leg':[-2,12,0],'right_leg':[2,12,0],'back_left':[-6,7,4],'back_right':[6,7,4],'wing_left':[-7,30,4],'wing_right':[7,30,4],'halo':[0,41,3]}
 for a in arr:
  tx=(a['mat']%4)*32;ty=(a['mat']//4)*32;uv={f:dict(uv=[tx+2,ty+2],uv_size=[24,24]) for f in ['north','south','east','west','up','down']}
  bc=dict(origin=a['origin'],size=a['size'],uv=uv);bones.setdefault(a['bone'],[]).append(bc)
  uid=str(uuid.uuid4());elements.append(dict(name=a['name'],uuid=uid,type='cube',origin=pivots.get(a['bone'],[0,0,0]),**{'from':a['origin'],'to':[a['origin'][k]+a['size'][k] for k in range(3)]},faces={f:dict(uv=[tx+2,ty+2,tx+26,ty+26],texture=0) for f in uv},bone=a['bone']))
 for bo in bones:bbgroups.append(dict(name=bo,uuid=boneids[bo],origin=pivots.get(bo,[0,0,0]),children=[e['uuid'] for e in elements if e['bone']==bo]))
 for e in elements:e.pop('bone')
 j(f'02_MODELE/{ident}/{ident}.bbmodel',dict(meta=dict(format_version='4.10',model_format='bedrock',box_uv=False),name=ident,model_identifier=ident,resolution=dict(width=128,height=128),elements=elements,outliner=[dict(name='root',uuid=str(uuid.uuid4()),origin=[0,0,0],children=bbgroups)],textures=[dict(name='tekstura_128.png',path='tekstura_128.png',id='0',uuid=str(uuid.uuid4()),source='data:image/png;base64,'+base64.b64encode(bio.getvalue()).decode(),width=128,height=128,uv_width=128,uv_height=128)]))
 j(f'02_MODELE/{ident}/{ident}.geo.json',{'format_version':'1.12.0','minecraft:geometry':[{'description':{'identifier':'geometry.'+ident,'texture_width':128,'texture_height':128,'visible_bounds_width':6,'visible_bounds_height':6,'visible_bounds_offset':[0,2,0]},'bones':[{'name':'root','pivot':[0,0,0]}]+[{'name':bo,'parent':'root','pivot':pivots.get(bo,[0,0,0]),'cubes':cs} for bo,cs in bones.items()]}]})
 anim={'format_version':'1.8.0','animations':{f'animation.{ident}.idle':{'loop':True,'animation_length':2,'bones':{'head':{'rotation':[0,'math.sin(query.anim_time * 90) * 3',0]}}},f'animation.{ident}.walk':{'loop':True,'animation_length':1,'bones':{'left_leg':{'rotation':['math.sin(query.anim_time * 360) * 22',0,0]},'right_leg':{'rotation':['-math.sin(query.anim_time * 360) * 22',0,0]},'left_arm':{'rotation':['-math.sin(query.anim_time * 360) * 15',0,0]},'right_arm':{'rotation':['math.sin(query.anim_time * 360) * 15',0,0]}}}}}
 if ident=='nurek_dzwonowy':
  anim['animations'][f'animation.{ident}.walk']['bones'].update({'back_left':{'rotation':['-math.sin(query.anim_time * 360) * 22',0,0]},'back_right':{'rotation':['math.sin(query.anim_time * 360) * 22',0,0]}})
 if ident=='aniol_minuty':
  anim['animations'][f'animation.{ident}.idle']['bones'].update({'wing_left':{'rotation':[0,'math.sin(query.anim_time * 90) * 5',0]},'wing_right':{'rotation':[0,'-math.sin(query.anim_time * 90) * 5',0]},'halo':{'rotation':[0,'query.anim_time * 10',0]}})
 for clip in anim['animations'].values():clip['bones']={k:v for k,v in clip['bones'].items() if k in bones}
 j(f'02_MODELE/{ident}/{ident}.animation.json',anim)
 # textured orthographic renderer with proper front visibility and painter depth
 def render(angle):
  a=math.radians(angle);b=math.radians(14);right=np.array([math.cos(a),0,math.sin(a)]);towards=np.array([math.sin(a)*math.cos(b),math.sin(b),-math.cos(a)*math.cos(b)]);up=np.cross(right,towards)
  verts=[];faces=[]
  for q in arr:
   x,y,z=q['origin'];sx,sy,sz=q['size'];vv=np.array([[x,y,z],[x+sx,y,z],[x+sx,y+sy,z],[x,y+sy,z],[x,y,z+sz],[x+sx,y,z+sz],[x+sx,y+sy,z+sz],[x,y+sy,z+sz]])
   for indices,norm in [([0,1,2,3],[0,0,-1]),([5,4,7,6],[0,0,1]),([4,0,3,7],[-1,0,0]),([1,5,6,2],[1,0,0]),([3,2,6,7],[0,1,0]),([4,5,1,0],[0,-1,0])]:
    if np.dot(norm,towards)>0:
     f=vv[indices];faces.append((float(np.mean(f@towards)),f,q['mat'],norm));verts.extend(f)
  vv=np.array(verts);xx=vv@right;yy=vv@up;scale=min(490/(xx.max()-xx.min()),570/(yy.max()-yy.min()));cx=(xx.max()+xx.min())/2;cy=(yy.max()+yy.min())/2
  img=np.zeros((640,560,3),dtype=np.uint8);img[:]=[19,26,39]
  light=np.array([-.3,.8,-.6]);light/=np.linalg.norm(light)
  tex=np.array(atlas)
  for depth,f,mat,norm in sorted(faces,key=lambda v:v[0]):
   pts=np.stack([280+(f@right-cx)*scale,320-(f@up-cy)*scale],axis=1);uv=np.array([[0,1],[1,1],[1,0],[0,0]],float)
   shade=.55+.45*max(0,np.dot(norm,light))
   for tri in [(0,1,2),(0,2,3)]:
    pp=pts[list(tri)];uvv=uv[list(tri)];lo=np.maximum(np.floor(pp.min(axis=0)).astype(int),[0,0]);hi=np.minimum(np.ceil(pp.max(axis=0)).astype(int),[559,639])
    if np.any(hi<lo):continue
    gx,gy=np.meshgrid(np.arange(lo[0],hi[0]+1),np.arange(lo[1],hi[1]+1));v0=pp[1]-pp[0];v1=pp[2]-pp[0];den=v0[0]*v1[1]-v1[0]*v0[1]
    if abs(den)<1e-8:continue
    vx=gx+.5-pp[0,0];vy=gy+.5-pp[0,1];u=(vx*v1[1]-v1[0]*vy)/den;v=(v0[0]*vy-vx*v0[1])/den;mask=(u>=0)&(v>=0)&(u+v<=1)
    uu=uvv[0]+u[...,None]*(uvv[1]-uvv[0])+v[...,None]*(uvv[2]-uvv[0]);tx=(mat%4)*32+2+np.clip((uu[...,0]*23).astype(int),0,23);ty=(mat//4)*32+2+np.clip((uu[...,1]*23).astype(int),0,23)
    img[gy[mask],gx[mask]]=(tex[ty[mask],tx[mask]]*shade).astype(np.uint8)
  return Image.fromarray(img)
 views=[render(0),render(35),render(-145)];sheet=Image.new('RGB',(1680,700),'#131a27')
 for k,v in enumerate(views):sheet.paste(v,(k*560,40))
 d=ImageDraw.Draw(sheet);d.text((24,12),ident.upper()+' | EXACT MODEL: FRONT / THREE-QUARTER / BACK',fill='#e8dfc9');sheet.save(P/'model_trzy_widoki.png');views[1].save(P/'model_render.png')
j('02_MODELE/GEOMETRIA_ZRODLOWA.json',M)
print('Models ready:',{k:len(v) for k,v in M.items()})
