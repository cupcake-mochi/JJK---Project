"""Ensaio restrito do piloto R53. Não calcula dificuldade universal nem substitui jogo.

Invariantes: dados lidos da base única; Integridade NPC = max(1, PV//2);
Bloquear = 2d10+Defesa-11, gratuito; 20 natural prevalece; reações renovam
no próprio turno; inimigo a zero sai; PC a zero segue escolha, tratamento,
janela por ponto de iniciativa, dano posterior e Sequelas. Cura insuficiente
não reinicia prazo; cura comum não reabre participação de Derrotado.
"""
from pathlib import Path
from collections import Counter
from itertools import product
import copy, hashlib, json, math, random, statistics

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / 'base-inimigos.json').read_text())
ENEMIES = {x['id']: x for x in DATA['enemies']}
TR_ATTR = {'vigor': 'constituicao', 'intelecto': 'inteligencia', 'espirito': 'essencia'}

def required(maxhp, mode, count=1, classe=1):
    return math.ceil(maxhp / 4) if mode == 'Aguentar' else min(math.ceil(maxhp / (3 if count == 1 else 2)), 15 * classe)

def actor(spec, pc, initial=1, sequelas=0):
    x = copy.deepcopy(spec)
    x.update(pc=pc, hp=max(1, math.floor(spec['pv'] * initial)), energy=spec['pe'],
             soul=20 + (spec['atributos']['essencia'] + 5) * (spec['nivel'] - 1) if pc else max(1, spec['pv']//2),
             status='ativo', reaction=True, sequelas=sequelas, insisting=0,
             treatment=0, window=0, due=None, stable=False, prone=False)
    x['soulmax'] = x['soul']
    return x

def conscious(x):
    return x['status'] in ('ativo', 'Insistir')

def defeated(x):
    x.update(status='Derrotado', prone=True, stable=False, due=None)

def hurt(x, value, tick, length, mode, soul=False):
    if value <= 0 or x['status'] == 'Derrotado':
        return False
    if soul:
        x['soul'] = max(0, x['soul'] - value)
        if x['soul'] == 0:
            x['hp'] = max(0, x['hp'] - value)
            defeated(x)
            return False
    if x['hp'] == 0:
        if x['stable']:
            x.update(stable=False, due=tick+length)
        x['window'] -= 1
        if x['window'] <= 0:
            defeated(x)
        return False
    x['hp'] = max(0, x['hp'] - value)
    if x['hp']:
        return False
    if not x['pc']:
        defeated(x)
        return False
    x.update(window=3-x['sequelas'], treatment=0, due=tick+length, stable=False)
    if x['window'] <= 0:
        defeated(x)
        return True
    if mode == 'Insistir':
        x['insisting'] += 1
    x['status'] = mode
    x['need'] = required(x['pv'], mode, x['insisting'])
    if mode == 'Aguentar':
        x['prone'] = True
    return True

def heal(x, amount):
    if x['status'] == 'Derrotado':
        x['hp'] = min(x['pv'], x['hp'] + amount)
        return False
    if x['hp'] > 0:
        x['hp'] = min(x['pv'], x['hp'] + amount)
        return False
    x['treatment'] += amount
    if x['treatment'] < x['need']:
        return False
    x.update(hp=min(x['pv'], x['treatment']), status='ativo', due=None, stable=False,
             sequelas=x['sequelas'] + 1)
    # Socorro não levanta automaticamente quem ficou no chão.
    return True

def expire(x, tick, length):
    if x['hp'] == 0 and x['status'] in ('Aguentar', 'Insistir') and not x['stable']:
        while x['due'] is not None and x['due'] <= tick:
            x['window'] -= 1
            if x['window'] <= 0:
                defeated(x)
            else:
                x['due'] += length

def dice(rng, count, sides):
    return sum(rng.randint(1, sides) for _ in range(count))

def stage(x):
    lost = x['soulmax'] - x['soul']
    return 4 if not x['soul'] else 3 if 4*lost >= 3*x['soulmax'] else 2 if 2*lost >= x['soulmax'] else 1 if 4*lost >= x['soulmax'] else 0

def strike(attacker, target, rng, spec, blocked, tick, length, mode, distance, counts, soul=False, extra=0):
    """Respostas usam ataque físico de alcance 1,5 m, nunca uma conjuração grátis."""
    # Apenas uma fonte de cada: vantagem e desvantagem se anulam.
    has_adv = target['prone'] and distance <= 1.5
    has_dis = (target['prone'] and distance > 1.5) or attacker['prone'] or stage(attacker) >= 3
    roll = rng.randint(1, 20)
    if has_adv != has_dis:
        second = rng.randint(1, 20)
        roll = max(roll, second) if has_adv else min(roll, second)
    parry = breach = False
    defense = target['defesa']
    if blocked and conscious(target):
        a, b = rng.randint(1, 10), rng.randint(1, 10)
        parry, breach = a == b == 10, a == b == 1
        defense = a+b+target['defesa']-11
    hit = roll == 20 or (not parry and (breach or roll + spec['attack'] >= defense))
    if hit:
        amount = dice(rng, spec['dados'] * (2 if roll == 20 else 1), spec['faces']) + spec['fixo'] + extra
        counts['quedas'] += hurt(target, amount, tick, length, mode, soul)
    if distance <= 1.5:
        if parry and not hit and target['reaction'] and conscious(target) and conscious(attacker):
            target['reaction'] = False
            strike(target, attacker, rng, physical(target), blocked, tick, length, mode, distance, counts, extra=3)
        elif breach and attacker['reaction'] and conscious(attacker) and conscious(target):
            attacker['reaction'] = False
            strike(attacker, target, rng, physical(attacker), blocked, tick, length, mode, distance, counts)

def physical(x):
    if x['pc']:
        return dict(attack=x['atributos']['forca']+1, dados=x['arma_dados'], faces=x['arma_faces'], fixo=x['arma_fixo'])
    b=x['basica']
    return dict(attack=x['atributos'][b['atributo']]+1, dados=b['dados'], faces=b['faces'], fixo=b['fixo'])

def simulate(enemy_ids, seed, mode='Insistir', blocked=False, size=3, initial=1, sequelas=0, soul=False):
    rng = random.Random(seed)
    # O perfil de dois personagens conserva frente e apoio.
    specs = DATA['players'] if size == 3 else [DATA['players'][0], DATA['players'][2]]
    pcs = [actor(x, True, initial, sequelas) for x in specs]
    foes = [actor(ENEMIES[e], False) for e in enemy_ids]
    actors = pcs+foes
    # Empates: maior Destreza, depois jogador; PCs empatados escolhem a ordem da lista.
    actors.sort(key=lambda x: (rng.randint(1,20)+x['atributos']['destreza'], x['atributos']['destreza'], x['pc']), reverse=True)
    length=len(actors)
    counts=Counter()
    for round_i in range(20):
        for pos,x in enumerate(actors):
            tick=round_i*length+pos
            for p in pcs:
                expire(p,tick,length)
            if not any(conscious(p) for p in pcs):
                return dict(outcome='sem_combatente_ativo', rounds=round_i+1, **counts, derrotados=sum(p['status']=='Derrotado' for p in pcs), morrendo=sum(p['hp']==0 and p['status']!='Derrotado' for p in pcs))
            if not any(conscious(e) for e in foes):
                return dict(outcome='ameaca_neutralizada', rounds=round_i+1, **counts, derrotados=sum(p['status']=='Derrotado' for p in pcs), morrendo=sum(p['hp']==0 and p['status']!='Derrotado' for p in pcs))
            if not conscious(x):
                continue
            x['reaction']=True
            if x['prone']:
                x['prone']=False  # gasta Movimento; todos já têm alcance neste modelo.
            if x['pc']:
                needing=[p for p in pcs if p['hp']==0 and p['status']!='Derrotado']
                if needing and x['cura'] and x['energy'] >= x['cura']['custo']:
                    target=min(needing,key=lambda p:p['window'])
                    x['energy']-=x['cura']['custo'];counts['curas']+=1
                    counts['socorros_concluidos']+=heal(target,dice(rng,2,8))
                    continue
                other_needing=[p for p in needing if p is not x]
                if other_needing and x['id']=='apoio':
                    target=min(other_needing,key=lambda p:p['window'])
                    if target['status']=='Insistir':
                        target.update(status='Aguentar',prone=True)
                    if not target['stable']:
                        counts['tentativas_estabilizar']+=1
                        if rng.randint(1,20)+x['medicina']>=14:
                            target['stable']=True
                    continue
                target=next(e for e in foes if conscious(e))
                if x['energy'] >= x['magia']['custo']:
                    x['energy']-=x['magia']['custo']
                    spec=dict(attack=x['ataque'],dados=3,faces=8,fixo=0)
                    distance=1.5 if x['id']=='frente' else 6
                else:
                    spec=physical(x);distance=1.5
                counts['acoes_pcs']+=1
                if x['status']=='Insistir': counts['acoes_insistindo']+=1
                strike(x,target,rng,spec,blocked,tick,length,mode,distance,counts,soul=soul and x['id']=='conjurador')
            else:
                # Prioriza frente consciente; troca quando ela Aguenta ou é Derrotada.
                target=next(p for p in pcs if conscious(p))
                spell=x['magia']
                cost=(spell['custo']+(spell['classe'] if stage(x)>=2 else 0)) if spell else 0
                if spell and x['energy']>=cost:
                    x['energy']-=cost
                    spec=dict(attack=x['atributos'][spell['atributo']]+1,dados=spell['dados'],faces=spell['faces'],fixo=0)
                    distance=6 if spell['forma']=='Projétil' else 1.5
                else:
                    spec=physical(x);distance=1.5
                strike(x,target,rng,spec,blocked,tick,length,mode,distance,counts)
            if not any(conscious(e) for e in foes) or not any(conscious(p) for p in pcs):
                return dict(outcome='ameaca_neutralizada' if not any(conscious(e) for e in foes) else 'sem_combatente_ativo',rounds=round_i+1,**counts,derrotados=sum(p['status']=='Derrotado' for p in pcs),morrendo=sum(p['hp']==0 and p['status']!='Derrotado' for p in pcs))
    return dict(outcome='censurado_20_rodadas',rounds=20,**counts,derrotados=sum(p['status']=='Derrotado' for p in pcs),morrendo=sum(p['hp']==0 and p['status']!='Derrotado' for p in pcs))

def exact_hit(attack, defense, blocked=False):
    hits=crits=0
    combinations=list(product(range(1,11),repeat=2)) if blocked else [(0,0)]
    for roll in range(1,21):
        for a,b in combinations:
            parry=blocked and a==b==10;breach=blocked and a==b==1
            d=a+b+defense-11 if blocked else defense
            hit=roll==20 or (not parry and (breach or roll+attack>=d))
            hits+=hit;crits+=roll==20
    total=20*len(combinations)
    return dict(acerto=hits/total,critico=crits/total)

def regressions():
    checks=[]
    def check(name, predicate):
        assert predicate,name
        checks.append(name)
    for e in DATA['enemies']:
        check(e['id']+' atributos',sum(e['atributos'].values())==9 and max(e['atributos'].values())<=3)
        check(e['id']+' Defesa',e['defesa']==10+e['atributos']['destreza'])
        check(e['id']+' dano desarmado',e['basica']['fixo']==e['atributos']['forca'] and e['basica']['faces']==4)
        check(e['id']+' perícias',len(e['pericias'])==4+e['atributos']['inteligencia']//2)
        if e['magia']:
            check(e['id']+' orçamento e PE',e['magia']['dados']==3 and e['magia']['custo']==3 and e['pe']==6)
    for p in DATA['players']:
        start,gain={'Bastião':(12,7),'Emanador':(6,4),'Guia':(8,5)}[p['caminho']]
        check(p['id']+' vida',p['pv']==start+gain+2*p['atributos']['constituicao'])
        check(p['id']+' Defesa',p['defesa']==11+p['atributos']['destreza'])
    check('Kaori: ataque 16 acerta Defesa 12; 14 de dano encerra inimigo 14',16>=12 and 4+5+5==14)
    check('Mei 23: Aguentar 6, primeiro Insistir 8',required(23,'Aguentar')==6 and required(23,'Insistir')==8)
    check('Exemplo 93/Classe3: 24,31,45', [required(93,'Aguentar',classe=3),required(93,'Insistir',classe=3),required(93,'Insistir',2,3)]==[24,31,45])
    check('Teto 395/Classe7: 99,105,105',[required(395,'Aguentar',classe=7),required(395,'Insistir',classe=7),required(395,'Insistir',2,7)]==[99,105,105])
    p=actor(DATA['players'][0],True)
    hurt(p,100,2,4,'Insistir')
    check('Excesso da queda não agrava janela',p['window']==3 and p['hp']==0 and p['status']=='Insistir')
    heal(p,3);expire(p,5,4)
    check('Cura insuficiente não renova janela',p['hp']==0 and p['treatment']==3 and p['due']==6)
    expire(p,6,4)
    check('Prazo no ponto de iniciativa',p['window']==2 and p['due']==10)
    hurt(p,2,7,4,'Insistir')
    check('Dano posterior conserva tratamento e reduz prazo',p['window']==1 and p['treatment']==3 and p['need']==8)
    heal(p,5)
    check('Socorro converte todo tratamento, dá Sequela, não subtrai requisito',p['hp']==8 and p['status']=='ativo' and p['sequelas']==1)
    hurt(p,100,8,4,'Insistir')
    check('Nova queda: janela2 e segundo Insistir12',p['window']==2 and p['need']==12 and p['insisting']==2)
    p['stable']=True;p['status']='Aguentar';expire(p,100,4)
    check('Estável suspende tempo',p['window']==2)
    hurt(p,1,101,4,'Insistir')
    check('Dano rompe estabilidade e marca novo ponto',not p['stable'] and p['window']==1 and p['due']==105)
    expire(p,105,4);heal(p,20)
    check('Cura não reabre Derrotado',p['status']=='Derrotado' and p['hp']>0)
    p=actor(DATA['players'][0],True,sequelas=3);hurt(p,100,0,4,'Insistir')
    check('Três Sequelas: derrota imediata',p['status']=='Derrotado')
    e=actor(ENEMIES['amontoado'],False);hurt(e,24,0,4,'Insistir',soul=True)
    check('Integridade NPC é metade da vida; Alma pode derrotar com PV restantes',e['soulmax']==24 and e['hp']==24 and e['status']=='Derrotado')
    check('Acerto estático +4 contra13',exact_hit(4,13)['acerto']==0.6)
    return checks

def run():
    checks=regressions()
    sample=10000
    configs=[('rastejante',['rastejante'],3,1,0,False),('amontoado',['amontoado'],3,1,0,False),('vigia',['vigia'],3,1,0,False),('dois_rastejantes',['rastejante','rastejante'],3,1,0,False),('amontoado_dupla',['amontoado'],2,1,0,False),('amontoado_desgastado',['amontoado'],3,0.5,2,False),('amontoado_e_rastejante',['amontoado','rastejante'],3,1,0,False),('amontoado_com_alma',['amontoado'],3,1,0,True)]
    results=[]
    for config in configs:
        name,ids,size,initial,sequelas,soul=config
        for mode in ('Aguentar','Insistir'):
            for blocked in (False,True):
                runs=[simulate(ids,730000+i,mode,blocked,size,initial,sequelas,soul) for i in range(sample)]
                wins=sum(x['outcome']=='ameaca_neutralizada' for x in runs)
                fraction=wins/sample
                # Wilson95 para a taxa de neutralização; média não significa garantia.
                z=1.96;center=(fraction+z*z/(2*sample))/(1+z*z/sample)
                margin=z*math.sqrt(fraction*(1-fraction)/sample+z*z/(4*sample*sample))/(1+z*z/sample)
                rounds=[x['rounds'] for x in runs]
                results.append(dict(caso=name,politica=mode,bloquear=blocked,n=sample,neutralizacao=fraction,ic95=[center-margin,center+margin],mediana_rodadas=statistics.median(rounds),p10_rodadas=sorted(rounds)[int(sample*.1)],p90_rodadas=sorted(rounds)[int(sample*.9)],alguma_queda=sum(x.get('quedas',0)>0 for x in runs)/sample,algum_derrotado=sum(x['derrotados']>0 for x in runs)/sample,morrendo_ao_encerrar=sum(x['morrendo']>0 for x in runs)/sample,acoes_insistindo_media=statistics.mean(x.get('acoes_insistindo',0) for x in runs),curas_media=statistics.mean(x.get('curas',0) for x in runs),censurados=sum(x['outcome']=='censurado_20_rodadas' for x in runs)))
    output=dict(base_sha256=hashlib.sha256((HERE/'base-inimigos.json').read_bytes()).hexdigest(),r53_sha256=hashlib.sha256(Path(DATA['referencia']).read_bytes()).hexdigest(),checagens=checks,acertos_exatos={str(d):{'estatica':exact_hit(4,d),'bloquear':exact_hit(4,d,True)} for d in (11,12,13)},resultados=results)
    (HERE/'resultado-validacao.json').write_text(json.dumps(output,ensure_ascii=False,indent=2))
    print(json.dumps({'checagens':len(checks),'ensaios':len(results)*sample,'casos':results[:8]},ensure_ascii=False,indent=2))

if __name__=='__main__':
    run()
