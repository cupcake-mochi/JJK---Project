from fractions import Fraction
from functools import lru_cache
import json
from pathlib import Path

@lru_cache(None)
def nd6(n):
    counts={0:1}
    for _ in range(n):
        new={}
        for t,c in counts.items():
            for d in range(1,7): new[t+d]=new.get(t+d,0)+c
        counts=new
    return {s:Fraction(c,6**n) for s,c in counts.items()}

def mix(a,b,p):
    out={}
    for s,x in a.items():out[s]=out.get(s,Fraction(0))+(1-p)*x
    for s,x in b.items():out[s]=out.get(s,Fraction(0))+p*x
    assert sum(out.values())==1
    return out

def dice_height(h,step,cap=None):
    if h<3:return 0
    n=int(Fraction(h)/step)
    return min(n,cap) if cap is not None else n

def dist(h,step,bonus=None,resist=False,cap=None):
    a=nd6(dice_height(h,step,cap))
    if bonus is not None:
        p=Fraction(sum(d+bonus>=14 for d in range(1,21)),20)
        a=mix(a,nd6(dice_height(max(0,h-3),step,cap)),p)
    if resist:
        out={}
        for s,x in a.items():
            k=(s+1)//2
            out[k]=out.get(k,Fraction(0))+x
        a=out
    return a

def convolve(a,b):
    out={}
    for s,x in a.items():
        for t,y in b.items():out[s+t]=out.get(s+t,Fraction(0))+x*y
    assert sum(out.values())==1
    return out

def stats(a,hp):
    risk=sum((x for s,x in a.items() if s>=hp),Fraction(0))
    mean=sum(s*x for s,x in a.items())
    return {'mean':float(mean),'p0':float(risk),'p0_exact':str(risk),'min':min(a),'max':max(a)}

heights=[3,4.5,6,9,12,18,30,45,60,90,120]
# Comparison retains CON=2 for each level; mastery/stat scenarios are stated, not required builds.
levels={2:{'inc_hp':14,'bast_hp':23,'bonus':4},11:{'inc_hp':68,'bast_hp':104,'bonus':7},30:{'inc_hp':182,'bast_hp':275,'bonus':10}}
result={'threshold':'H<3=0; otherwise floor(H/step), all H counted','rounding':'resistance ceil(damage/2)','single':[],'repeat_4_5':[],'caps':[]}
for step in [Fraction(3),Fraction(3,2)]:
 for level,v in levels.items():
  for h in heights:
   row={'step':float(step),'level':level,'height':h,'bonus':v['bonus']}
   for key,hp,resist in [('inc',v['inc_hp'],False),('bast',v['bast_hp'],False),('bast_res',v['bast_hp'],True)]:
    row[key+'_plain']=stats(dist(h,step,resist=resist),hp)
    row[key+'_acro']=stats(dist(h,step,bonus=v['bonus'],resist=resist),hp)
   result['single'].append(row)
  for key,hp,resist in [('inc',v['inc_hp'],False),('bast',v['bast_hp'],False),('bast_res',v['bast_hp'],True)]:
   for acro in [False,True]:
    one=dist(4.5,step,bonus=v['bonus'] if acro else None,resist=resist)
    total={0:Fraction(1)}
    for repeats in [1,2,3,4]:
     total=convolve(total,one)
     result['repeat_4_5'].append({'step':float(step),'level':level,'target':key,'acro':acro,'falls':repeats,**stats(total,hp)})
 for cap in [12,20,30]:
  for level,v in levels.items():
   for key,hp,resist in [('inc',v['inc_hp'],False),('bast',v['bast_hp'],False),('bast_res',v['bast_hp'],True)]:
    result['caps'].append({'step':float(step),'cap':cap,'height_at_cap':float(step*cap),'level':level,'target':key,**stats(dist(999,step,bonus=v['bonus'],resist=resist,cap=cap),hp)})
Path(__file__).with_name('sonda-resultados.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))

print('SINGLE Inc2 p0 sem/acro, Bastião2 resist sem/acro; médias Inc2 sem/acro')
for r in result['single']:
 if r['level']==2 and r['height'] in [3,4.5,6,9,12,18,30]:
  print(r['step'],r['height'],*[round(r[k]['p0']*100,5) for k in ['inc_plain','inc_acro','bast_res_plain','bast_res_acro']],*[round(r[k]['mean'],4) for k in ['inc_plain','inc_acro']])
print('ADVANCED Inc p0 sem/acro, Bastião resist sem/acro')
for r in result['single']:
 if r['level'] in [11,30] and r['height'] in [18,30,45,60,90,120]:
  print(r['step'],r['level'],r['height'],*[round(r[k]['p0']*100,7) for k in ['inc_plain','inc_acro','bast_res_plain','bast_res_acro']])
print('REPEATS NV2')
for r in result['repeat_4_5']:
 if r['level']==2:print(r['step'],r['target'],r['acro'],r['falls'],round(r['p0']*100,6),round(r['mean'],4))
print('CAPS Inc/Bast NV11/30 (step3 only; distribution identical at step1.5)')
for r in result['caps']:
 if r['step']==3 and r['level'] in [11,30]:print(r['cap'],r['level'],r['target'],round(r['p0']*100,8),round(r['mean'],4),r['max'])
