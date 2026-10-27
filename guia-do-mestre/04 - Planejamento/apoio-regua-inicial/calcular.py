"""Enumeração de recortes para régua inicial. Sem motor de combate ou sorteios.
Reutiliza distribuições conferidas em P73, sem modificar aquele apoio.
--salvar escreve apenas resultados.json nesta pasta, nunca o manifesto.
"""
import importlib.util,json,sys,math
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('p73',HERE.parent/'apoio-pressao-sineiro/calcular.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)

def check_dist(d):
    assert abs(sum(d.values())-1)<1e-8
    assert all(p>=0 for p in d.values())
    return d

def marginal(d):
    out=defaultdict(float)
    for (n,hit),p in d.items():out[n]+=p
    return check_dist(dict(out))

def plus(a,c):
    out=defaultdict(float)
    for x,p in a.items():
        for y,q in c.items():out[x+y]+=p*q
    return check_dist(dict(out))

@lru_cache(None)
def sword(level,defense,blocked):
    attr=3 if level==2 else 4;out=defaultdict(float)
    for (damage,hit),p in b.attack_dist(attr+1,defense,1,8,attr,blocked=blocked).items():
        if not hit:out[0]+=p
        else:
            for extra,q in b.dice(1,4).items():out[damage+extra]+=p*q
    return check_dist(dict(out))

@lru_cache(None)
def sequence(level,defense,blocked,mixed):
    attr=3 if level==2 else 4;n=3 if level==2 else 6
    spell=marginal(b.attack_dist(attr+1,defense,n,8,blocked=blocked));total={0:1};series=[]
    for i in range(6):
        total=plus(total,sword(level,defense,blocked) if mixed and i%3==0 else spell)
        series.append(total)
    return series

rows=[]
for level,hps in [(2,[16,24,32]),(6,[48,72,108])]:
    for defense in [11,13,15]:
        for blocked in [False,True]:
            for mixed in [False,True]:
                curve=sequence(level,defense,blocked,mixed)
                for hp in hps:
                    chances=[sum(p for damage,p in dist.items() if damage<hp) for dist in curve]
                    assert all(0<=v<=1+1e-8 for v in chances)
                    assert all(a+1e-8>=c for a,c in zip(chances,chances[1:]))
                    rows.append({'nivel':level,'PV':hp,'integridade':hp//2,'defesa':defense,'bloquear':blocked,'misto':mixed,'sobrevive_apos_declaracoes':chances})
accuracy=[]
for atk in [4,5]:
    for defense in [11,13,15,16]:
        for blocked in [False,True]:
            v=b.attacks(atk,defense,blocked);accuracy.append({'ataque':atk,'defesa':defense,'bloquear':blocked,'acerta':v.get('hit',0)+v.get('critical',0),'critico':v.get('critical',0)})
pressure=[]
for name,atk,n,sides,fixed,targets in [('Carregador',4,1,4,3,[23,14,17]),('Candidata_n2',4,1,8,3,[23,14,17]),('Pancada_Sineiro',5,2,6,4,[65,44,51])]:
    d=marginal(b.attack_dist(atk,13,n,sides,fixed));two=plus(d,d)
    for hp in targets:
        pressure.append({'aplicacao':name,'vida_maxima':hp,'media_por_declaracao':sum(x*p for x,p in d.items()),'zero_em_uma_cheio':sum(p for x,p in d.items() if x>=hp),'zero_em_duas_cheio':sum(p for x,p in two.items() if x>=hp),'vida_ferida':math.ceil(hp/2),'zero_em_duas_ferido':sum(p for x,p in two.items() if x>=math.ceil(hp/2))})
# Conferências cruzadas com resultados conhecidos e limites analíticos.
assert abs(sum(b.attacks(4,13)[k] for k in ['hit','critical'])-.6)<1e-12
assert abs(sum(b.attacks(5,13)[k] for k in ['hit','critical'])-.65)<1e-12
assert abs(b.mean(b.attack_dist(4,13,1,4,3))-3.425)<1e-12
assert abs(b.mean(b.attack_dist(5,13,2,6,4))-7.5)<1e-12
assert abs(sum(p for damage,p in sequence(6,11,False,False)[2].items() if damage<108)-b.pool_curve(108,False)[2]['sobrevive'])<1e-9
out={'metodo':'Enumeração de seis declarações no grupo, duas por personagem, com custos pagáveis. Sem oposição ativa ou duração de combate inferida.','sobrevivencia':rows,'acerto':accuracy,'pressao':pressure,'tr':{'CD12_vs_4_3_2':[b.fail(x,12) for x in [4,3,2]],'CD13_vs_5_3_2':[b.fail(x,13) for x in [5,3,2]]},'limites':['Sem críticos Kokusen, propriedades de arma, respostas de Caminho, reação de Aparar ou Brecha, cura, dano de Alma ou resistências.','Alcance, recursos e liberdade de agir são pressupostos; sem iniciativa, movimento, controle ou missão simulados.','Dois ataques são duas declarações legalmente disponíveis; a tabela não concede ataque extra a uma ficha.','Chegar a zero de PV de jogador não é morte ou derrota automática.']}
if '--salvar' in sys.argv:(HERE/'resultados.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('SOBREVIVÊNCIA: nível PV Def, três/seis conjurações; três/seis no recorte misto')
for level,hp in [(2,16),(2,24),(2,32),(6,48),(6,72),(6,108)]:
    for defense in [11,13,15]:
        picks=[x for x in rows if x['nivel']==level and x['PV']==hp and x['defesa']==defense and not x['bloquear']]
        print(level,hp,defense,[(x['misto'],*[round(100*x['sobrevive_apos_declaracoes'][i],2) for i in [2,5]]) for x in picks])
print('PRESSÃO',json.dumps(pressure,ensure_ascii=False))
print('CURVAS',len(rows))
