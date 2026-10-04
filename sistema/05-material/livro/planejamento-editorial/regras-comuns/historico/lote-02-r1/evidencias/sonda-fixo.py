import runpy,contextlib,io,json
from pathlib import Path
from fractions import Fraction
with contextlib.redirect_stdout(io.StringIO()): a=runpy.run_path(str(Path(__file__).with_name('sonda-calculo.py')))
mix,conv,stats=a['mix'],a['convolve'],a['stats']
levels=a['levels']
p=Path(__file__).with_name('sonda-resultados.json');out=json.loads(p.read_text())

def fixed(h,bonus=None,resist=False):
 def damage(z):return 0 if z<3 else 3*int(Fraction(z)/Fraction(3,2))
 dis={damage(h):Fraction(1)}
 if bonus is not None:
  success=Fraction(sum(d+bonus>=14 for d in range(1,21)),20)
  dis=mix(dis,{damage(max(0,h-3)):Fraction(1)},success)
 if resist:
  dis={(s+1)//2:x for s,x in dis.items()}
 return dis
out['fixed_single']=[];out['fixed_repeat']=[]
for level,v in levels.items():
 for h in [3,4.5,6,7.5,9,10.5,12,18,30,34.5,37.5,60,90,91.5,94.5,120]:
  row={'level':level,'height':h,'bonus':v['bonus']}
  for key,hp,resist in [('inc',v['inc_hp'],False),('bast',v['bast_hp'],False),('bast_res',v['bast_hp'],True)]:
   row[key+'_plain']=stats(fixed(h,resist=resist),hp)
   row[key+'_acro']=stats(fixed(h,bonus=v['bonus'],resist=resist),hp)
  out['fixed_single'].append(row)
 for key,hp,resist in [('inc',v['inc_hp'],False),('bast',v['bast_hp'],False),('bast_res',v['bast_hp'],True)]:
  for acro in [False,True]:
   one=fixed(4.5,v['bonus'] if acro else None,resist)
   total={0:Fraction(1)}
   for r in range(1,5):
    total=conv(total,one)
    out['fixed_repeat'].append({'level':level,'target':key,'acro':acro,'falls':r,**stats(total,hp)})
p.write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('FIXO Inc2 sem/acrobacia, Bastião resistente sem/acrobacia, médias Inc')
for r in out['fixed_single']:
 if r['level']==2 and r['height'] in [3,4.5,6,7.5,9,10.5,12,18,30,60]:
  print(r['height'],*[r[k]['p0']*100 for k in ['inc_plain','inc_acro','bast_res_plain','bast_res_acro']],*[r[k]['mean'] for k in ['inc_plain','inc_acro']])
print('FIXO repeats NV2')
for r in out['fixed_repeat']:
 if r['level']==2:print(r['target'],r['acro'],r['falls'],r['p0']*100,r['mean'])
print('FIXO advanced inc,bast-res p0 sem/acro')
for r in out['fixed_single']:
 if r['level']>2 and r['height'] in [30,34.5,37.5,60,90,91.5,94.5,120]:
  print(r['level'],r['height'],*[r[k]['p0']*100 for k in ['inc_plain','inc_acro','bast_res_plain','bast_res_acro']])
