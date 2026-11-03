"""Casos C02, C04, C05, C07, C11 e C12 do plano 149, rodados com motor_estendido.simulate2.
Base: trio do piloto no nível 2 (frente, conjurador, apoio), Insistir, sem Bloquear, sementes 149000+i.
Saída: mediana e p90 da rodada em que a ameaça cai, % com pelo menos uma queda, % com alguém Derrotado,
% de lutas que o grupo perde (ninguém de pé), turnos de PC perdidos no chão e PE que sobra. Margem: Wilson 95%."""
import sys, math, statistics, copy, json; from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from motor_estendido import simulate2, V
N=4000
def wilson(k,n,z=1.96):
    if n==0: return 0,0
    p=k/n; d=1+z*z/n; c=(p+z*z/(2*n))/d; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return 100*(c-h),100*(c+h)
def roda(rotulo,**kw):
    rs=[simulate2(seed=149000+i,**kw) for i in range(N)]
    fl=sorted(r['fim_luta'] for r in rs if r['outcome']!='sem_combatente_ativo') or [0]
    q=sum(r.get('quedas',0)>0 for r in rs); d=sum(r['derrotados']>0 for r in rs); p=sum(r['outcome']=='sem_combatente_ativo' for r in rs)
    c=sum(r['outcome']=='censurado' for r in rs)
    lo,hi=wilson(q,N); dlo,dhi=wilson(d,N)
    lin=dict(caso=rotulo,med=statistics.median(fl),p90=fl[int(.9*(len(fl)-1))],queda=100*q/N,queda_ic=(lo,hi),derrot=100*d/N,derrot_ic=(dlo,dhi),
             perde=100*p/N,censurado=100*c/N,sem_agir=statistics.mean(r['sem_agir'] for r in rs),pe_sobra=100*statistics.mean(r['pe_sobra'] for r in rs),
             magias=statistics.mean(r.get('magias_inimigo',0) for r in rs))
    print(f"{rotulo:<46} rod {lin['med']:>3}/{lin['p90']:<3} queda {lin['queda']:5.1f}% [{lo:4.1f}–{hi:4.1f}]  Derrot {lin['derrot']:5.2f}% [{dlo:4.2f}–{dhi:4.2f}]  perde {lin['perde']:5.2f}%  cens {lin['censurado']:.1f}%  chão {lin['sem_agir']:.2f}  PE sobra {lin['pe_sobra']:4.1f}%  magias-ini {lin['magias']:.2f}")
    return lin
OUT=[]
TRIO=('frente','conjurador','apoio')
GRUPOS={2:('frente','apoio'),3:TRIO,4:TRIO+('frente',),6:TRIO*2}
AM=V.ENEMIES['amontoado']
def am(pv=None,pe=None,acoes=1):
    e=copy.deepcopy(AM)
    if pv is not None: e['pv']=pv
    if pe is not None: e['pe']=pe
    e['acoes']=acoes; return e
