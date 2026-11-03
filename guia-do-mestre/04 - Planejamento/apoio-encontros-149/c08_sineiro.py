"""C08 — o Sineiro do Recolhimento (caso 71) contra Rina, Mei e Akira (perfis de nível 6 do caso 73).
Modelo abstrato, sem grade: quem está 'na zona' é decidido pela política do grupo.
Sineiro: 108 PV, Def 11, Atacar = Agarrar (TR Físico CD 13) + Pancada (+5, 2d6+4); arrasta a presa e prepara (Bônus);
no turno seguinte, Impacto: TR Físico CD 13, 5d8 / metade para cima, em quem está na zona; depois Guarda Aberta até o
começo do próximo turno dele (acertos corpo a corpo viram crítico) e solta a presa. Interrompida, a preparação acaba sem
Guarda Aberta. Reação: uma Pancada de oportunidade.
Grupo: Rina (65 PV, 24 PE, espada +5 1d8+4 +1d4 Canalizar, TR Físico +5, Alicerce opcional = metade de Concussão),
Mei (44 PV, 36 PE, Arremesso de pressão +5, 5d8, 6 PE, Empurrão que interrompe ao acertar), Akira (51 PV, 30 PE,
Sutura 4d8 por 6 PE a 9 m; Resguardar com Bônus + 1 PE dá vantagem no TR de fuga).
Políticas: 'mei_perto' (como 'ignorar', mas Mei fica dentro da zona, como no segundo exemplo do caso 73), 'ignorar' (todos batem, Rina fica em corpo a corpo), 'sair' (presa tenta fugir e quem está perto sai da
zona quando há preparação), 'interromper' (Mei usa o Empurrão contra a preparação e Rina tenta Derrubar, CD 13).
Limites: sem posição real, sem Bloquear, sem Cobrir-se, Mei sem PE só espera, o Sineiro sempre agarra a Rina."""
import sys, math, random, statistics; from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent/'motor'))
import validar_base as V
def d(rng,n,f): return sum(rng.randint(1,f) for _ in range(n))
def pc(nome,pv,pe,forca,des,con,int_,ess,trf):
    x=V.actor(dict(id=nome,pv=pv,pe=pe,nivel=6,defesa=13,atributos=dict(forca=forca,destreza=des,constituicao=con,inteligencia=int_,essencia=ess)),True)
    x['trf']=trf; x['nome']=nome; return x
def luta(seed,politica='ignorar',alicerce=False,ini_mei=1.0,max_r=20):
    rng=random.Random(seed)
    rina=pc('Rina',65,24,4,2,3,1,1,5); mei=pc('Mei',44,36,0,2,3,4,2,3); akira=pc('Akira',51,30,0,2,3,2,4,2)
    mei['hp']=max(1,math.floor(44*ini_mei))
    pcs=[rina,mei,akira]
    s=V.actor(dict(id='sineiro',pv=108,pe=0,nivel=6,defesa=11,atributos=dict(forca=4,destreza=1,constituicao=3,inteligencia=1,essencia=1)),False)
    s.update(prep=False,aberta=False,presa=None,reacao=True)
    ordem=pcs+[s]; ordem.sort(key=lambda x:(rng.randint(1,20)+x['atributos']['destreza'],x['pc']),reverse=True)
    L=len(ordem); c=dict(impactos=0,atingidos=0,interrupcoes=0,fugas=0,quedas=0,curas=0)
    na_zona=lambda p: p is s['presa'] or (p is rina and politica in ('ignorar','mei_perto') and V.conscious(p)) or (p is rina and s['presa'] is rina) or (p is mei and politica=='mei_perto')
    def dano(p,v,tick,conc=True):
        if p is rina and alicerce and conc: v=math.ceil(v/2)
        c['quedas']+=V.hurt(p,v,tick,L,'Insistir')
    def pancada(alvo,tick):
        r=rng.randint(1,20)
        if r==20 or r+5>=alvo['defesa']: dano(alvo,d(rng,4 if r==20 else 2,6)+4,tick)
    for rod in range(max_r):
        for pos,x in enumerate(ordem):
            tick=rod*L+pos
            for p in pcs: V.expire(p,tick,L)
            if not V.conscious(s): return fim('vitoria',rod+1,pcs,c)
            if not any(V.conscious(p) for p in pcs): return fim('derrota',rod+1,pcs,c)
            if x is s:
                s['reacao']=True; s['aberta']=False
                if s['presa'] is not None and not V.conscious(s['presa']): s['presa']=None
                if s['prep']:
                    s['prep']=False; c['impactos']+=1
                    alvo_zona=[p for p in pcs if p['status']!='Derrotado' and na_zona(p)]
                    total=d(rng,5,8)
                    for p in alvo_zona:
                        c['atingidos']+=1
                        ok=rng.randint(1,20)+p['trf']>=13
                        dano(p,math.ceil(total/2) if ok else total,tick)
                    s['aberta']=True; s['presa']=None
                    continue
                vivos=[p for p in pcs if V.conscious(p)]
                alvo=rina if V.conscious(rina) else vivos[0]
                if s['presa'] is None:
                    if rng.randint(1,20)+alvo['trf']<13: s['presa']=alvo
                else: pancada(s['presa'],tick)
                pancada(s['presa'] or alvo,tick)
                s['prep']=True   # Bônus: dobrar o sino
                continue
            if not V.conscious(x): continue
            # PCs
            caidos=[p for p in pcs if p['hp']==0 and p['status']!='Derrotado']
            if x is akira:
                feridos=[p for p in pcs if V.conscious(p) and p['hp']<p['pv']/2]
                if (caidos or feridos) and akira['energy']>=6:
                    t=min(caidos,key=lambda p:p['window']) if caidos else min(feridos,key=lambda p:p['hp'])
                    akira['energy']-=6; c['curas']+=1; V.heal(t,d(rng,4,8))
                elif s['presa'] is not None and akira['energy']>=1 and politica!='ignorar':
                    akira['energy']-=1; s['resguardar']=True
                continue
            if x is mei:
                if mei['energy']>=6:
                    mei['energy']-=6; r=rng.randint(1,20)
                    if r==20 or r+5>=s['defesa']:
                        dano_s=d(rng,10 if r==20 else 5,8); c['quedas']+=V.hurt(s,dano_s,tick,L,'Insistir')
                        if s['prep'] and politica=='interromper': s['prep']=False; c['interrupcoes']+=1
                continue
            # Rina
            if s['prep'] and politica=='interromper':
                if rng.randint(1,20)+5<13: s['prep']=False; c['interrupcoes']+=1   # Derrubar: o Sineiro falha o TR Físico +5 contra CD 13
                continue
            if s['prep'] and politica=='sair' and s['presa'] is rina:
                adv=s.pop('resguardar',False)
                r=max(rng.randint(1,20),rng.randint(1,20)) if adv else rng.randint(1,20)
                if r+5>=13:
                    s['presa']=None; c['fugas']+=1
                    if s['reacao']: s['reacao']=False; pancada(rina,tick)
                continue
            r=rng.randint(1,20); crit=r==20 or s['aberta']
            if r==20 or r+5>=s['defesa']:
                c['quedas']+=V.hurt(s,d(rng,2 if crit else 1,8)+4+d(rng,1,4),tick,L,'Insistir')
    return fim('censurado',max_r,pcs,c)
def fim(res,r,pcs,c):
    return dict(res=res,rodadas=r,derrot=sum(p['status']=='Derrotado' for p in pcs),queda=c['quedas']>0 and any(True for _ in [0]),
                quedas_pc=sum(1 for p in pcs if p['sequelas']>0 or p['hp']==0 or p['status']=='Derrotado'),**c,
                pe=sum(p['energy'] for p in pcs))
if __name__=='__main__':
    N=4000
    def w(k,n,z=1.96):
        p=k/n; dd=1+z*z/n; cc=(p+z*z/(2*n))/dd; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/dd; return 100*(cc-h),100*(cc+h)
    for alic in (False,True):
        for ini in (1.0,18/44):
            for pol in ('ignorar','sair','interromper','mei_perto'):
                rs=[luta(1490800+i,pol,alic,ini) for i in range(N)]
                q=sum(r['quedas_pc']>0 for r in rs); dr=sum(r['derrot']>0 for r in rs); v=sum(r['res']=='vitoria' for r in rs)
                rod=sorted(r['rodadas'] for r in rs)
                print(f"Alicerce {'sim' if alic else 'não'} · Mei {'18/44' if ini<1 else 'cheia'} · {pol:<11} rod {statistics.median(rod)}/{rod[int(.9*N)]}  "
                      f"alguém cai {100*q/N:5.1f}% [{w(q,N)[0]:.1f}–{w(q,N)[1]:.1f}]  Derrotado {100*dr/N:5.2f}%  vence {100*v/N:5.1f}%  "
                      f"impactos {statistics.mean(r['impactos'] for r in rs):.2f}  atingidos {statistics.mean(r['atingidos'] for r in rs):.2f}  interrupções {statistics.mean(r['interrupcoes'] for r in rs):.2f}")
