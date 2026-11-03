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
for alvo in ('lista','ferido','espalha'):
    print(f"\n=== política do inimigo: {alvo} ===")
    print('-- C02 tamanho do grupo, Amontoado igual (48 PV)')
    for n,g in GRUPOS.items(): OUT.append(dict(alvo=alvo,bloco='C02',**roda(f"C02 grupo {n}, Amontoado 48",grupo=g,alvo=alvo)))
    print('-- C02b tamanho do grupo, vida do Amontoado × n/3 (como a grade faz)')
    for n,g in GRUPOS.items(): OUT.append(dict(alvo=alvo,bloco='C02b',**roda(f"C02b grupo {n}, Amontoado {round(48*n/3)}",grupo=g,inimigos=[am(pv=round(48*n/3))],alvo=alvo)))
    print('-- C04 estado de entrada (trio)')
    for ini,seq in ((1,0),(.75,0),(.5,0),(1,1),(.5,1),(.5,2)):
        OUT.append(dict(alvo=alvo,bloco='C04',**roda(f"C04 vida {ini:.0%}, Sequelas {seq}",inimigos=['amontoado'],initial=ini,sequelas=seq,alvo=alvo)))
    print('-- C05 um corpo contra dois (32 PV contra 16+16)')
    OUT.append(dict(alvo=alvo,bloco='C05',**roda("C05 um corpo 32 PV, 6 PE",inimigos=[am(32)],alvo=alvo)))
    OUT.append(dict(alvo=alvo,bloco='C05',**roda("C05 dois corpos 16+16, 6 PE cada",inimigos=[am(16),am(16)],alvo=alvo)))
    OUT.append(dict(alvo=alvo,bloco='C05',**roda("C05 dois corpos 16+16, 3 PE cada",inimigos=[am(16,3),am(16,3)],alvo=alvo)))
    print('-- C07 recurso do inimigo (Amontoado 48)')
    for rec in ('pe','sem_pe','recarga56'):
        OUT.append(dict(alvo=alvo,bloco='C07',**roda(f"C07 recurso {rec}",inimigos=['amontoado'],recurso=rec,alvo=alvo)))
    print('-- C11 distância do socorro (cena vai até ninguém estar Morrendo)')
    for at in (0,1,2):
        OUT.append(dict(alvo=alvo,bloco='C11',**roda(f"C11 atraso de {at} turno(s)",inimigos=['amontoado'],atraso_socorro=at,ficar_ate_o_fim=True,alvo=alvo)))
        OUT.append(dict(alvo=alvo,bloco='C11',**roda(f"C11 atraso {at}, dupla",grupo=GRUPOS[2],inimigos=['amontoado'],atraso_socorro=at,ficar_ate_o_fim=True,alvo=alvo)))
    print('-- C12 células da grade da peça 26 no nível 2 (Def 13 e +4 supostos; golpe fixo)')
    def celula(nome,pv,golpe,acoes):
        return dict(id=nome,nome=nome,nivel=2,atributos=dict(forca=3,destreza=1,constituicao=3,inteligencia=1,essencia=1),pv=pv,pe=0,defesa=13,
                    basica=dict(nome='Golpe',atributo='forca',dados=0,faces=1,fixo=golpe),magia=None,acoes=acoes)
    for nome,pv,g,a in (('Ameaça ×3',71,4,3),('Desastre ×3',85,4,3),('Desastre ×3 (Def 11)',85,4,3)):
        e=celula(nome,pv,g,a)
        if 'Def 11' in nome: e['defesa']=11
        OUT.append(dict(alvo=alvo,bloco='C12',**roda(f"C12 {nome}, {pv} PV, {a}×{g}",inimigos=[e],alvo=alvo,max_rodadas=30)))
json.dump(OUT,open(Path(__file__).with_name('casos-resultado.json'),'w'),ensure_ascii=False,indent=1)
