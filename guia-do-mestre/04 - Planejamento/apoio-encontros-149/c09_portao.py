"""C09 — o portão do depósito (caso 66) com o Carregador (caso 63) contra o trio de nível 2 do piloto.
Modelo em linha, sem grade: A (pátio) = 0 m, portão G = 3 m, C (caixa e Carregador) = 6 m, recuo = 24 m.
Com o portão fechado, de qualquer ponto ≥ 3 m até A são (x − 6) + 18 m pelo serviço, e quem está em A não vê além do portão.
Objetivo: Carregador neutralizado (0 PV ou fuga com 8 PV ou menos), caixa em A e todos que não foram Derrotados em A.
Carregador: 32 PV, Def 11, Agarrar TR Físico CD 12 no lugar do ataque, Pancada +4 1d4+3, Bônus vira Movimento;
arrastar custa o dobro; segura e arrasta para o recuo; uma Pancada de oportunidade por rodada.
Grupo: perfis do piloto; TR Físico +4 / +3 / +2; magia 3d8 por 3 PE a 18 m (frente: toque); cura 2d8 por 3 PE a 9 m.
Versões: 'desligado' (motor parado, sem contagem), 'ativo' (fecha no fim da rodada 3 se a faixa estiver livre, o grupo
ignora), 'parar' (o conjurador vai A → Q → P na rodada 1 e para o motor), 'ocupar' (o apoio fica na faixa G).
Limites: sem Bloquear, sem Desengajar, sem destruir portão ou comando, sem Derrubar/Empurrar, sem transporte de caído:
quem cai precisa ser socorrido e andar."""
import sys, math, random, statistics; from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent/'motor'))
import validar_base as V
PERF={p['id']:p for p in V.DATA['players']}; TRF={'frente':4,'conjurador':3,'apoio':2}
def d(rng,n,f): return sum(rng.randint(1,f) for _ in range(n))
def luta(seed,versao='desligado',max_r=15):
    rng=random.Random(seed)
    pcs=[V.actor(PERF[k],True) for k in ('frente','conjurador','apoio')]
    for p in pcs: p['x']=0.0; p['trf']=TRF[p['id']]
    cg=V.actor(dict(id='carregador',pv=32,pe=0,nivel=2,defesa=11,atributos=dict(forca=3,destreza=1,constituicao=2,inteligencia=1,essencia=1)),False)
    cg.update(x=6.0,presa=None,reacao=True,fora=False)
    st=dict(caixa=6.0,portador=None,cont=0,fechado=False,motor=versao!='desligado',servico=False)
    ordem=pcs+[cg]; ordem.sort(key=lambda a:(rng.randint(1,20)+a['atributos']['destreza'],a['pc']),reverse=True); L=len(ordem)
    c=dict(quedas=0)
    ativo=lambda: V.conscious(cg) and not cg['fora']
    def dist(a,b):   # a e b no mesmo lado: |a−b|; atravessar o portão fechado usa o serviço
        if st['fechado'] and (a<3)!=(b<3): return abs(max(a,b)-6)+18+min(a,b)
        return abs(a-b)
    def ve(a,b): return not (st['fechado'] and (a<3)!=(b<3))
    def andar(p,alvo,m):   # anda até m metros em direção a alvo; devolve metros gastos
        D=dist(p['x'],alvo)
        if D<=m: p['x']=alvo; return D
        if st['fechado'] and (p['x']<3)!=(alvo<3): st['servico']=True; p['servico_falta']=D-m; p['x']=p['x']  # ainda no serviço
        else: p['x']+=math.copysign(m,alvo-p['x'])
        return m
    def ataque(bonus,defesa): r=rng.randint(1,20); return (r==20 or r+bonus>=defesa), r==20
    def dano_pc(p,v,tick): c['quedas']+=V.hurt(p,v,tick,L,'Insistir')
    for rod in range(max_r):
        for pos,a in enumerate(ordem):
            tick=rod*L+pos
            for p in pcs: V.expire(p,tick,L)
            if not any(V.conscious(p) for p in pcs): return fim('grupo_caiu',rod+1,pcs,st,c)
            dentro=[p for p in pcs if p['status']!='Derrotado' and (p['x']>0 or (p['hp']==0 and not p['stable']))]
            if not ativo() and st['caixa']<=0 and not dentro: return fim('objetivo',rod+1,pcs,st,c)
            if a is cg:
                cg['reacao']=True
                if not ativo(): continue
                if cg['hp']<=8: cg['fora']=True; cg['presa']=None; continue
                if cg['presa'] is not None and (not V.conscious(cg['presa'])):
                    cg['presa']=None
                if cg['presa'] is not None:
                    v=cg['presa']; h,cr=ataque(4,v['defesa'])
                    if h: dano_pc(v,d(rng,2 if cr else 1,4)+3,tick)
                    passo=min(9,24-cg['x']); cg['x']+=passo; v['x']=cg['x']
                    continue
                alvos=[p for p in pcs if V.conscious(p) and p['x']>0 and ve(cg['x'],p['x']) and dist(cg['x'],p['x'])<=18]
                if not alvos: continue
                v=min(alvos,key=lambda p:(dist(cg['x'],p['x']),pcs.index(p)))
                gasto=dist(cg['x'],v['x']); cg['x']=v['x']
                if rng.randint(1,20)+v['trf']<12:
                    cg['presa']=v; passo=min((18-gasto)/2,24-cg['x']); cg['x']+=passo; v['x']=cg['x']
                continue
            p=a
            if not V.conscious(p): continue
            m=18.0
            # parar o motor
            if versao=='parar' and p['id']=='conjurador' and st['motor'] and not st['fechado']:
                p['x']=6.0; st['motor']=False; continue   # A → Q → P (12 m) e Padrão em P; P fica a 6 m de C
            if versao=='ocupar' and p['id']=='apoio' and st['motor'] and any(q['x']>3 for q in pcs if q is not p and q['status']!='Derrotado'):
                if p['x']!=3: andar(p,3,m)
                caidos=[q for q in pcs if q['hp']==0 and q['status']!='Derrotado' and not q['stable'] and dist(3,q['x'])<=9]
                if caidos and p['energy']>=3: p['energy']-=3; V.heal(min(caidos,key=lambda q:q['window']),d(rng,2,8))
                elif ativo() and p['energy']>=3 and ve(3,cg['x']) and dist(3,cg['x'])<=18:
                    p['energy']-=3; h,cr=ataque(4,cg['defesa'])
                    if h: V.hurt(cg,d(rng,6 if cr else 3,8),tick,L,'Insistir')
                continue
            if cg['presa'] is p:
                if rng.randint(1,20)+p['trf']>=12:
                    cg['presa']=None
                    if cg['reacao']: cg['reacao']=False; h,cr=ataque(4,p['defesa']); h and dano_pc(p,d(rng,2 if cr else 1,4)+3,tick)
                    andar(p,0,9)
                continue
            caidos=[q for q in pcs if q['hp']==0 and q['status']!='Derrotado' and not q['stable']]
            if p['cura'] and caidos and p['energy']>=3:
                t=min(caidos,key=lambda q:q['window']); D=dist(p['x'],t['x'])
                if D-9<=9:
                    if D>9: andar(p,t['x'],D-9)
                    p['energy']-=3; V.heal(t,d(rng,2,8)); continue
                andar(p,t['x'],m); continue
            if ativo():
                alc=p['magia']['alcance']
                if p['energy']>=p['magia']['custo'] and alc>1.5:
                    D=dist(p['x'],cg['x'])
                    if not ve(p['x'],cg['x']) or D>alc: andar(p,cg['x'],9); 
                    if ve(p['x'],cg['x']) and dist(p['x'],cg['x'])<=alc:
                        p['energy']-=3; h,cr=ataque(4,cg['defesa'])
                        if h: V.hurt(cg,d(rng,6 if cr else 3,8),tick,L,'Insistir')
                    continue
                gasto=andar(p,cg['x'],m)
                if p['x']==cg['x']:
                    if p['energy']>=3 and p['magia']['alcance']<=1.5: p['energy']-=3; h,cr=ataque(4,cg['defesa']); dn=d(rng,6 if cr else 3,8)
                    else: h,cr=ataque(p['atributos']['forca']+1,cg['defesa']); dn=d(rng,2 if cr else 1,p['arma_faces'])+p['arma_fixo']+d(rng,1,4)
                    if h: V.hurt(cg,dn,tick,L,'Insistir')
                continue
            # depois da oposição: caixa e saída
            if st['caixa']>0 and (st['portador'] in (None,p)):
                st['portador']=p
                if p['x']!=st['caixa']: m-=andar(p,st['caixa'],m)
                if p['x']==st['caixa'] and m>0: andar(p,0,m); st['caixa']=p['x']
                continue
            if st['portador'] is p: andar(p,0,m); st['caixa']=p['x']; continue
            andar(p,0,m)
        # fim da rodada: o portão
        if st['motor'] and not st['fechado']:
            st['cont']=min(3,st['cont']+1)
            if st['cont']>=3 and not any(q['x']==3 and q['status']!='Derrotado' for q in pcs) and not (3<=cg['x']<=3):
                if any(q['x']>3 for q in pcs if q['status']!='Derrotado') or st['caixa']>3: st['fechou_com_alguem']=True
                st['fechado']=True
        # quem estava no serviço: aplica o resto (simplificação: atravessa no fim da rodada seguinte)
        for q in pcs:
            if q.get('servico_falta') and V.conscious(q):
                q['servico_falta']=max(0,q['servico_falta']-18)
                if q['servico_falta']==0: q['x']=0.0 if q['x']>=3 else 6.0; q.pop('servico_falta')
                if st['portador'] is q: st['caixa']=q['x']
    return fim('censurado',max_r,pcs,st,c)
def fim(res,r,pcs,st,c):
    return dict(res=res,rod=r,derrot=sum(p['status']=='Derrotado' for p in pcs),caiu=any(p['sequelas']>0 or p['hp']==0 or p['status']=='Derrotado' for p in pcs),
                fechou=st['fechado'],fechou_com_alguem=st.get('fechou_com_alguem',False),servico=st['servico'])
if __name__=='__main__':
    N=4000
    for ver in ('desligado','ativo','parar','ocupar'):
        rs=[luta(1490900+i,ver) for i in range(N)]
        ok=sum(r['res']=='objetivo' for r in rs); rod=sorted(r['rod'] for r in rs if r['res']=='objetivo') or [0]
        print(f"{ver:<10} objetivo {100*ok/N:5.1f}%  rodadas {statistics.median(rod)}/{rod[int(.9*(len(rod)-1))]}  alguém cai {100*sum(r['caiu'] for r in rs)/N:5.1f}%  "
              f"Derrotado {100*sum(r['derrot']>0 for r in rs)/N:5.2f}%  portão fechou {100*sum(r['fechou'] for r in rs)/N:5.1f}%  "
              f"fechou com alguém dentro {100*sum(r['fechou_com_alguem'] for r in rs)/N:5.1f}%  usou o serviço {100*sum(r['servico'] for r in rs)/N:5.1f}%  "
              f"censurado {100*sum(r['res']=='censurado' for r in rs)/N:.1f}%")
