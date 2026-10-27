"""Enumeração finita de ataques e janelas ofensivas, não simulador de combate.

Não altera fichas, históricos ou manifesto. --salvar grava apenas resultados.json
nesta pasta. Os recursos e as ações declaradas são hipóteses, não política ótima.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path
import json, math, sys

HERE = Path(__file__).resolve().parent

@lru_cache(None)
def dice(n, sides):
    p = {0: 1.0}
    for _ in range(n):
        nxt = defaultdict(float)
        for a, pa in p.items():
            for b in range(1, sides+1): nxt[a+b] += pa/sides
        p = dict(nxt)
    return p

@lru_cache(None)
def attacks(bonus, defense, blocked=False, adv=0):
    """P(normal hit), P(critical), P(miss), P(parry trigger), P(breach trigger).
    Responses are NOT executed. Nat20 beats parry; breach forces hit, not crit.
    """
    rolls = [(i, 1/20) for i in range(1,21)] if not adv else [(max(a,b) if adv>0 else min(a,b),1/400) for a,b in product(range(1,21),repeat=2)]
    blocks = [(None,None,defense,1)] if not blocked else [(a,b,a+b+defense-11,.01) for a,b in product(range(1,11),repeat=2)]
    out = defaultdict(float)
    for d,p in rolls:
        for a,b,dc,q in blocks:
            w=p*q; parry=a==b==10; breach=a==b==1
            if d==20: out['critical']+=w
            elif parry: out['miss']+=w; out['parry_trigger']+=w
            elif breach or d+bonus>=dc: out['hit']+=w
            else: out['miss']+=w
            if breach: out['breach_trigger']+=w
    return dict(out)

@lru_cache(None)
def attack_dist(bonus, defense, n, sides, fixed=0, blocked=False, adv=0, exposed=False):
    rates=attacks(bonus,defense,blocked,adv); out=defaultdict(float)
    out[(0,False)]+=rates.get('miss',0)
    for critical,label in [(False,'hit'),(True,'critical')]:
        for damage,p in dice(n*(2 if critical or exposed else 1),sides).items():
            out[(damage+fixed,True)]+=p*rates.get(label,0)
    return dict(out)

def fail(bonus, cd, adv=0):
    if not adv: return sum(x+bonus<cd for x in range(1,21))/20
    return sum((max(a,b) if adv>0 else min(a,b))+bonus<cd for a,b in product(range(1,21),repeat=2))/400

def mean(dist): return sum(d*p for (d,_),p in dist.items())

def incoming(cd, tr, resistance=False, rd=0):
    out=defaultdict(float); f=fail(tr,cd)
    for d,p in dice(5,8).items():
        for failed,q in [(True,f),(False,1-f)]:
            factor=(1 if failed else .5)*(.5 if resistance else 1)
            out[max(0,math.ceil(d*factor)-rd)]+=p*q
    return dict(out)

@lru_cache(None)
def sword_dist(blocked=False):
    out=defaultdict(float)
    for (d,hit),p in attack_dist(5,11,1,8,4,blocked=blocked).items():
        if not hit:out[(0,False)]+=p;continue
        for extra,q in dice(1,4).items():out[(d+extra,True)]+=p*q
    return dict(out)

def pool_curve(hp, blocked, mixed=False):
    """Six paid Class2 attack spells; no incoming damage/control/retaliation.
    Damage is Concussion. No unverified grant of Soul damage at Class2.
    """
    states={(hp,hp//2):1.0}; rows=[]
    dist=attack_dist(5,11,6,8,blocked=blocked)
    for j in range(6):
        current=sword_dist(blocked) if mixed and j%3==0 else dist
        nxt=defaultdict(float)
        for (h,i),p in states.items():
            for (d,_),q in current.items():
                nh=h-d; ni=i
                if nh>0 and ni>0:nxt[(nh,ni)]+=p*q
        states=nxt
        rows.append({'declaracoes':j+1,'sobrevive':sum(states.values())})
    return rows

def window(hp, blocked, tactic):
    """B before boss; boss captures + one punch + windup; then E, G, B.
    Assumes valid ranges, retained resources and no PC action loss.
    Returns survival and survival with unbroken preparation, not hit chance.
    """
    states={(hp,False,False):1.0} # hp, canceled, open guard
    for j in range(4):
        nxt=defaultdict(float)
        for (h,canceled,open_guard),p in states.items():
            block_now=blocked and not open_guard
            if j==2 and tactic=='guarda_sem_dano':
                f=fail(1,15)
                options=[(0,True,True,f),(0,False,False,1-f)]
            elif j==2 and tactic=='guarda_com_dano':
                f=fail(1,13);options=[]
                for d,q in dice(5,8).items():
                    options.extend([(d,True,True,f*q),(math.ceil(d/2),False,False,(1-f)*q)])
            else:
                pushes=j==1 and tactic=='empurrao'
                options=[(d, pushes and hit, False,q) for (d,hit),q in attack_dist(5,11,5 if pushes else 6,8,blocked=block_now).items()]
            for damage,cancel,opened,q in options:
                if h-damage>0:nxt[(h-damage,canceled or cancel,open_guard or opened)]+=p*q
        states=nxt
    alive=sum(states.values()); ready=sum(p for (h,c,o),p in states.items() if not c)
    return {'sobrevive':alive,'sobrevive_com_preparo':ready}

def main():
    tests=[]
    def test(name,actual,expected,tol=1e-9):
        assert abs(actual-expected)<tol,(name,actual,expected)
        tests.append(name)
    test('Distribuição de 6d8 soma 1',sum(dice(6,8).values()),1)
    test('Média 6d8',sum(d*p for d,p in dice(6,8).items()),27)
    test('Ataque +5 contra Defesa11: acerto inclui crítico',sum(attacks(5,11).get(x,0) for x in ['hit','critical']),.75)
    test('20 natural contra Aparar',attacks(5,11,True)['critical'],.05)
    test('Duplo10 sem 20 natural oferece Aparar',attacks(5,11,True)['parry_trigger'],.0095)
    test('Duplo1 oferece Brecha',attacks(5,11,True)['breach_trigger'],.01)
    test('Caso anterior publicado +4 Defesa13 Bloquear',sum(attacks(4,13,True).get(x,0) for x in ['hit','critical']),.5985)
    test('TR +5 CD13 falha',fail(5,13),.35)
    test('TR +5 CD13 com vantagem falha',fail(5,13,1),.1225)
    test('TR +5 CD13 com desvantagem falha',fail(5,13,-1),.5775)
    test('TR Espírito +1 CD15 falha',fail(1,15),.65)
    test('Média impacto sem TR reduzido',sum(d*p for d,p in dice(5,8).items()),22.5)
    test('72PV sobrevivem sempre a um 6d8 sem crítico',sum(p for d,p in dice(6,8).items() if d<72),1)
    test('Primeira declaração contra 72 inclui crítico',pool_curve(72,False)[0]['sobrevive'],1-.05*sum(p for d,p in dice(12,8).items() if d>=72))
    for hp in [72,108,144]:
        for blocked in [False,True]:
            curve=pool_curve(hp,blocked)
            for a,b in zip(curve,curve[1:]):assert b['sobrevive']<=a['sobrevive']+1e-10
            for tactic in ['dano','empurrao','guarda_com_dano','guarda_sem_dano']:
                w=window(hp,blocked,tactic);assert -1e-10<=w['sobrevive_com_preparo']<=w['sobrevive']+1e-10<=1+1e-9
    test('Integridade108PV: quarto exige14 pontos perdidos',math.ceil(54/4),14)
    test('Integridade108PV: três quartos exigem41 perdidos',math.ceil(54*3/4),41)
    test('Destruição: 59 de dano a partir de5 não supera54',int(59>=108 or 59-5>54),0)
    test('Destruição: 60 de dano a partir de5 supera54',int(60>=108 or 60-5>54),1)
    profiles=[{'nome':'Bastião de referência','atributos':[4,2,3,1,1],'vida':65,'pe':24,'integridade':50,'tr_fisico':5},
              {'nome':'Emanador de referência','atributos':[0,2,3,4,2],'vida':44,'pe':36,'integridade':55,'tr_fisico':3},
              {'nome':'Guia de referência','atributos':[0,2,3,2,4],'vida':51,'pe':30,'integridade':65,'tr_fisico':2}]
    output={'metodo':'Enumeração finita e acumulação de distribuições; sem sorteio, sem combate completo. Probabilidades apresentadas com arredondamento.','testes':tests,'perfis':profiles,'ataques':[], 'impacto':[], 'controles':[], 'reservas':[], 'janela':[]}
    for defense in [11,13,16]:
        for blocked in [False,True]:
            rates=attacks(5,defense,blocked)
            output['ataques'].append({'defesa':defense,'bloquear':blocked,**rates,'media_pancada_2d6_mais4':mean(attack_dist(5,defense,2,6,4,blocked)),'media_feitico_6d8':mean(attack_dist(5,defense,6,8,blocked=blocked))})
    output['queda_se_sequencia_concluir']=[]
    punch=attack_dist(5,13,2,6,4)
    for profile in profiles:
        blast=incoming(13,profile['tr_fisico'])
        full=sum(p*q for (d,_),p in punch.items() for e,q in blast.items() if d+e>=profile['vida'])
        worn=sum(p*q for (d,_),p in punch.items() for e,q in blast.items() if d+e>=profile['vida']//2)
        output['queda_se_sequencia_concluir'].append({'perfil':profile['nome'],'pv_cheios':profile['vida'],'chance_zero_cheio':full,'pv_desgastado':profile['vida']//2,'chance_zero_desgastado':worn})
    output['ataque_com_abertura']=attacks(5,11,False,1)
    for tr in [2,3,5]:
        for resist in [False,True]:
            for rd in [0,3]:
                dist=incoming(13,tr,resist,rd)
                output['impacto'].append({'tr':tr,'resistencia':resist,'reducao':rd,'falha':fail(tr,13),'dano_medio':sum(d*p for d,p in dist.items()),'queda_a_partir_de_22pv':sum(p for d,p in dist.items() if d>=22)})
    for bonus,cd in [(5,13),(1,13),(1,15)]:
        for adv in [0,1,-1]:output['controles'].append({'bonus_tr':bonus,'cd':cd,'vantagem':adv,'falha':fail(bonus,cd,adv)})
    for hp in [72,108,144]:
        for blocked in [False,True]:
            for mixed in [False,True]:output['reservas'].append({'pv':hp,'integridade':hp//2,'bloquear':blocked,'uma_arma_e_dois_feiticos':mixed,'curva':pool_curve(hp,blocked,mixed)})
            for tactic in ['dano','empurrao','guarda_com_dano','guarda_sem_dano']:output['janela'].append({'pv':hp,'bloquear':blocked,'tatica':tactic,**window(hp,blocked,tactic)})
    # First critical only, no previously accumulated Kokusen bonuses.
    physical=defaultdict(float)
    for (weapon,hit),p in attack_dist(5,11,1,8,4,exposed=True).items():
        if not hit:physical[0]+=p;continue
        for extra,q in dice(1,4).items():physical[weapon+extra]+=p*q
    output['integridade']=[{'pv_maximo':h,'integridade_maxima':h//2,'perdas_para_estagios':[math.ceil((h//2)*q/4) for q in [1,2,3,4]]} for h in [72,108,144]]
    output['captura_e_fuga']=[{'tr_fisico':b,'chance_captura':fail(b,13),'chance_captura_e_fuga_fracassada':fail(b,13)**2} for b in [2,3,5]]
    output['espada_em_guarda_aberta_sem_kokusen']=sum(d*p for d,p in physical.items())
    output['limites']=['Revides de Aparar/Brecha não são executados; seus gatilhos são contabilizados separadamente.','Não há IA, deslocamento automático, iniciativa aleatória, socorro, morte, condição por desgaste dos jogadores ou simulação de sucesso da missão.','Salvas supõem que os personagens possam pagar e executar as ações; não equivalem a rodadas completas.','Guarda Aberta não transforma feitiço de Toque em crítico automático.','O recorte misto usa uma Espada Longa com Canalizar e dois feitiços; não executa Kokusen, respostas, Bônus ofensiva ou efeitos próprios de arma.','Alma aparece somente nos limiares de Integridade, sem conceder uma aplicação de 6d8 de Classe 2. Toca a Alma exige Classe 3 e precisa ser distinguido de eventual permissão própria.','Não certifica equilíbrio de Caminhos ou fichas completas.']
    if '--salvar' in sys.argv:(HERE/'resultados.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(output,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
