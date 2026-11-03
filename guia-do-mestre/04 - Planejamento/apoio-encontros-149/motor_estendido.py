"""Motor estendido para os casos C02–C12. Usa as funções do motor do piloto (motor/validar_base.py) sem mudar nenhuma;
só a rotina simulate() foi reescrita aqui para aceitar:
  grupo      lista de ids de personagem (repetição permitida: 4 e 6 pessoas repetem os perfis em ordem)
  inimigos   lista de fichas (dict) ou ids da base
  alvo       'lista' (a do piloto: a primeira pessoa consciente da lista, que é a frente), 'ferido' (menor PV atual),
             'espalha' (sorteio entre conscientes)
  recurso    'pe' (como a ficha), 'sem_pe' (a magia sem custo, todo turno), 'recarga56' (sem custo, volta com 5–6 no d6 no
             começo do turno; começa carregada)
  atraso_socorro  turnos que quem cura gasta para chegar a quem caiu (C11)
  ficar_ate_o_fim  se True, a cena continua depois de o inimigo cair, até ninguém estar Morrendo (socorro e prazo)
Com os valores padrão, simulate2 reproduz o simulate() do piloto semente a semente (conferido em c01c)."""
import sys, copy, random; from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent/'motor'))
import validar_base as V
from validar_base import actor, conscious, strike, physical, stage, dice, heal, expire
PERFIS={p['id']:p for p in V.DATA['players']}
def simulate2(grupo=('frente','conjurador','apoio'), inimigos=('amontoado',), seed=0, mode='Insistir', blocked=False,
              initial=1, sequelas=0, alvo='lista', recurso='pe', atraso_socorro=0, ficar_ate_o_fim=False, max_rodadas=20):
    rng=random.Random(seed)
    pcs=[actor(PERFIS[g],True,initial,sequelas) for g in grupo]
    for i,p in enumerate(pcs): p['id_unico']=f"{p['id']}{i}"
    foes=[actor(V.ENEMIES[e] if isinstance(e,str) else e,False) for e in inimigos]
    for f in foes: f['carregada']=True
    actors=pcs+foes
    actors.sort(key=lambda x:(rng.randint(1,20)+x['atributos']['destreza'],x['atributos']['destreza'],x['pc']),reverse=True)
    length=len(actors); counts=V.Counter(); caminho={}
    sem_agir=V.Counter(); fim_luta=None
    def resultado(outcome,r):
        return dict(outcome=outcome,rounds=r,fim_luta=fim_luta or r,**counts,derrotados=sum(p['status']=='Derrotado' for p in pcs),
                    morrendo=sum(p['hp']==0 and p['status']!='Derrotado' for p in pcs),sem_agir=sum(sem_agir.values()),
                    pe_sobra=sum(p['energy'] for p in pcs)/sum(p['pe'] for p in pcs))
    for round_i in range(max_rodadas):
        for pos,x in enumerate(actors):
            tick=round_i*length+pos
            for p in pcs: expire(p,tick,length)
            vivos=[e for e in foes if conscious(e)]
            if not any(conscious(p) for p in pcs):
                return resultado('sem_combatente_ativo',round_i+1)
            if not vivos:
                if fim_luta is None: fim_luta=round_i+1
                if not ficar_ate_o_fim or not any(p['hp']==0 and p['status']!='Derrotado' and not p['stable'] for p in pcs):
                    return resultado('ameaca_neutralizada',round_i+1)
            x['reaction']=True
            if not conscious(x):
                if x['pc']: sem_agir[x['id_unico']]+=1
                continue
            if x['prone']: x['prone']=False
            if x['pc']:
                needing=[p for p in pcs if p['hp']==0 and p['status']!='Derrotado']
                if needing and x['cura'] and x['energy']>=x['cura']['custo']:
                    target=min(needing,key=lambda p:p['window'])
                    chave=(x['id_unico'],id(target))
                    if atraso_socorro and caminho.get(chave,0)<atraso_socorro:
                        caminho[chave]=caminho.get(chave,0)+1; continue
                    x['energy']-=x['cura']['custo'];counts['curas']+=1
                    counts['socorros_concluidos']+=heal(target,dice(rng,2,8)); continue
                other=[p for p in needing if p is not x and not p['stable']]
                if other and x['id']=='apoio':
                    target=min(other,key=lambda p:p['window'])
                    if target['status']=='Insistir': target.update(status='Aguentar',prone=True)
                    if not target['stable']:
                        counts['tentativas_estabilizar']+=1
                        if rng.randint(1,20)+x['medicina']>=14: target['stable']=True
                    continue
                if not vivos: continue
                target=vivos[0]
                if x['energy']>=x['magia']['custo']:
                    x['energy']-=x['magia']['custo']
                    spec=dict(attack=x['ataque'],dados=3,faces=8,fixo=0); distance=1.5 if x['id']=='frente' else 6
                else:
                    spec=physical(x); distance=1.5
                counts['acoes_pcs']+=1
                if x['status']=='Insistir': counts['acoes_insistindo']+=1
                strike(x,target,rng,spec,blocked,tick,length,mode,distance,counts)
            else:
                cs=[p for p in pcs if conscious(p)]
                if alvo=='lista': target=cs[0]
                elif alvo=='ferido': target=min(cs,key=lambda p:(p['hp'],cs.index(p)))
                else: target=rng.choice(cs)
                spell=x.get('magia')
                if recurso=='recarga56' and spell and not x['carregada'] and rng.randint(1,6)>=5: x['carregada']=True
                cost=(spell['custo']+(spell['classe'] if stage(x)>=2 else 0)) if spell else 0
                pode = spell and ((recurso=='pe' and x['energy']>=cost) or recurso=='sem_pe' or (recurso=='recarga56' and x['carregada']))
                if pode:
                    if recurso=='pe': x['energy']-=cost
                    if recurso=='recarga56': x['carregada']=False
                    counts['magias_inimigo']+=1
                    spec=dict(attack=x['atributos'][spell['atributo']]+1,dados=spell['dados'],faces=spell['faces'],fixo=spell.get('fixo',0))
                    distance=6 if spell['forma']=='Projétil' else 1.5
                else:
                    spec=physical(x); distance=1.5
                for _ in range(x.get('acoes',1)):
                    cs=[p for p in pcs if conscious(p)]
                    if not cs: break
                    if target not in cs: target=cs[0] if alvo=='lista' else (min(cs,key=lambda p:p['hp']) if alvo=='ferido' else rng.choice(cs))
                    strike(x,target,rng,spec,blocked,tick,length,mode,distance,counts)
            if not ficar_ate_o_fim and (not any(conscious(e) for e in foes) or not any(conscious(p) for p in pcs)):
                if fim_luta is None and not any(conscious(e) for e in foes): fim_luta=round_i+1
                return resultado('ameaca_neutralizada' if not any(conscious(e) for e in foes) else 'sem_combatente_ativo',round_i+1)
    return resultado('censurado',max_rodadas)
