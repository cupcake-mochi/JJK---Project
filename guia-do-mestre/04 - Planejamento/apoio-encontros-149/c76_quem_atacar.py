from fractions import Fraction as F
from functools import lru_cache
def dice(n,f):
    d={0:F(1)}
    for _ in range(n):
        nd={}
        for k,v in d.items():
            for i in range(1,f+1): nd[k+i]=nd.get(k+i,0)+v/f
        d=nd
    return d
def atk(n,f,bonus=5,defesa=13):
    out={0:F(0)}
    miss=F(sum(1 for r in range(1,20) if r+bonus<defesa),20)
    hit=F(sum(1 for r in range(1,20) if r+bonus>=defesa),20)
    out[0]=miss
    for k,v in dice(n,f).items(): out[k]=out.get(k,0)+v*hit
    for k,v in dice(2*n,f).items(): out[k]=out.get(k,0)+v/20
    return out
def kill(pv,red):
    a=atk(5,8); b=atk(6,8); p=F(0)
    for x,px in a.items():
        for y,py in b.items():
            # redução no primeiro dano positivo
            if x>0: tot=max(0,x-red)+y
            elif y>0: tot=max(0,y-red)
            else: tot=0
            if tot>=pv: p+=px*py
    return float(p)
print('Sayo 48 red3',kill(48,3)); print('Toru 67 red3',kill(67,3)); print('Toru 67 sem red',kill(67,0))
