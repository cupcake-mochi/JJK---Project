"""Distribuições condicionais da dupla, não simulação de vitória.
--salvar grava somente resultados.json. Kokusen: primeiro teste possível,
Refino2, bônus acumulado0. Não reutilizar a média como política de uma luta.
"""
from pathlib import Path
from collections import defaultdict
import importlib.util,json,sys,math
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('p73',HERE.parent/'apoio-pressao-sineiro/calcular.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)

def physical(atk,defense,n,sides,fixed,adv=0,resistance=False):
    rates=b.attacks(atk,defense,False,adv);out=defaultdict(float);out[0]+=rates.get('miss',0)
    for critical,key in [(False,'hit'),(True,'critical')]:
        for base,p in b.dice(n*(2 if critical else 1),sides).items():
            for extra,q in b.dice(1,4).items():
                amount=base+extra+fixed
                if resistance:amount=math.ceil(amount/2)
                if critical:
                    out[amount]+=rates.get(key,0)*p*q*.96
                    out[math.ceil(amount*1.5)]+=rates.get(key,0)*p*q*.04
                else:out[amount]+=rates.get(key,0)*p*q
    assert abs(sum(out.values())-1)<1e-10
    return {'acerto':rates.get('hit',0)+rates.get('critical',0),'critico':rates.get('critical',0),'kokusen':rates.get('critical',0)*.04,'dano_medio':sum(d*p for d,p in out.items())}

joint=defaultdict(float)
for (d,_),p in b.attack_dist(5,13,5,8).items():
    for (e,_),q in b.attack_dist(5,13,6,8).items():joint[max(0,d+e-3)]+=p*q
# Cada acerto tem mínimo5/6: reduzir3 no primeiro positivo equivale aqui a
# descontar3 da soma. Sem caso de dano fracionário, resistência ou vida temporária.
assert abs(sum(joint.values())-1)<1e-9
focus=[]
for name,hp,maximum in [('Sora',48,48),('Ren',67,72)]:
    fallen=heal=boost=restored=0
    for damage,p in joint.items():
        remaining=max(0,hp-damage)
        if remaining==0:fallen+=p
        elif remaining<=maximum/2:
            heal+=p
            restored+=sum(min(maximum-remaining,d)*p*q for d,q in b.dice(4,8).items())
        else:boost+=p
    assert abs(fallen+heal+boost-1)<1e-9
    focus.append({'alvo':name,'vida_inicial':hp,'maximo':maximum,'derrotado_antes_de_nova_acao_de_Sora':fallen,'Sora_escolhe_cura_se_alvo_vivo':heal,'Sora_escolhe_Fio_se_alvo_vivo':boost,'cura_media_ponderada_incluindo_casos_sem_cura':restored})
rows=[]
for name,args in [('Ren',(5,1,8,4)),('Sora',(1,1,4,0))]:
    atk,n,sides,fixed=args
    for adv in [0,1]:
        rows.append({'nome':name,'vantagem':bool(adv),**physical(atk,13,n,sides,fixed,adv)})
        if name=='Ren':rows.append({'nome':'Ren contra Alicerce Cortante','vantagem':bool(adv),**physical(atk,13,n,sides,fixed,adv,True)})
assert abs(rows[0]['acerto']-.65)<1e-10
assert abs(physical(5,13,1,8,4,1)['acerto']-.8775)<1e-10
out={'metodo':'Enumeração condicionada a posição, ações, recursos e política declarados. Não calcula vitória do encontro.','ataques':rows,'foco':focus,'estado_comparado':'Depois de Ren agir na rodada1: Ren67PV/6PE, Sora48PV/9PE. Restam Mei5d8 e Akira6d8; ambos+5, alvoDef13 e uma redução3 por Reação/2PE.','limites':['Defesa estática, sem vantagem nos dois feitiços, sem novas ações/revides/Alma/curas antes de Sora2.','Primeiro teste de Kokusen possível nas referências de ataque físico; falhas anteriores exigem recalcular o limite.','Sora cura alvo vivo até metade da máxima; caso contrário oferece Fio. Nenhuma cura reabre o alvo derrotado.','Se Ren cair, Sora tenta retirada; não se concede buff a Ren derrotado.']}
if '--salvar' in sys.argv:(HERE/'resultados.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
