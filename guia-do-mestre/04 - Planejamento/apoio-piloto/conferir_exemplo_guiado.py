"""Confere o roteiro fixo do piloto; não é uma amostra de partida real."""
from pathlib import Path
from collections import Counter
from itertools import product
import json
import validar_base as v

HERE=Path(__file__).resolve().parent
# Crítico físico: dobra apenas o dado da arma; Canalizar não dobra.
class FixedDice:
    def __init__(self): self.values=iter([20,8,8,4])
    def randint(self,a,b):
        value=next(self.values)
        assert a<=value<=b
        return value
critical_attacker=v.actor(v.DATA['players'][0],True)
critical_target=v.actor(v.ENEMIES['amontoado'],False)
v.strike(critical_attacker,critical_target,FixedDice(),v.physical(critical_attacker),False,0,4,'Insistir',1.5,Counter())
assert critical_target['hp']==48-(8+8+3+4)
front=v.actor(v.DATA['players'][0],True)
enemy=v.actor(v.ENEMIES['amontoado'],False)
support_pe=10;caster_pe=12
events=[]
def save(label):
    events.append(dict(evento=label,frente_pv=front['hp'],frente_pe=front['energy'],
        estado=front['status'],sequelas=front['sequelas'],tratamento=front['treatment'],
        janela=front['window'] if front['status']=='Insistir' else None,amontoado_pv=enemy['hp'],amontoado_pe=enemy['energy'],
        apoio_pe=support_pe,conjuradora_pe=caster_pe))

# Ordem Amontoado, frente, apoio, conjuradora. Cada volta contém quatro pontos.
enemy['energy']-=3
v.hurt(front,sum([5,4,3,4,3,5]),0,4,'Insistir')
assert front['need']==8 and front['window']==3 and front['hp']==0
save('R1: crítico 24, primeiro Insistir')
front['energy']-=3;v.hurt(enemy,4+3+5,1,4,'Insistir')
support_pe-=3;v.heal(front,3+5)
assert front['hp']==8 and front['sequelas']==1
caster_pe-=3;v.hurt(enemy,6+3+5,3,4,'Insistir')
assert enemy['hp']==22
save('R1: socorro8, inimigo22')
enemy['energy']-=3
v.hurt(front,4+4+4,4,4,'Insistir')
assert front['need']==12 and front['window']==2
front['energy']-=3 # ataque 6+4 erra Defesa11
support_pe-=3;v.heal(front,4+3)
caster_pe-=3;v.hurt(enemy,4+3+4,7,4,'Insistir')
assert front['treatment']==7 and front['hp']==0 and enemy['hp']==11
save('R2: segunda queda, tratamento7, inimigo11')
v.expire(front,8,4)
assert front['window']==1
# Ramo alternativo: Pancada acertou em vez de errar; encerra participação.
alternative=v.copy.deepcopy(front)
v.hurt(alternative,4+3,8,4,'Insistir')
v.heal(alternative,5)
assert alternative['status']=='Derrotado' and alternative['hp']==12
# Ramo principal: ataque7+4 erra Defesa13; frente5+4 erra Defesa11.
support_pe-=3;v.heal(front,2+3)
assert front['hp']==12 and front['sequelas']==2
caster_pe-=3;v.hurt(enemy,3+5+4,11,4,'Insistir')
assert enemy['status']=='Derrotado' and enemy['hp']==0
assert (front['hp'],front['energy'],support_pe,caster_pe)==(12,2,1,3)
save('R3: socorro12 e inimigo derrotado')

distribution=Counter(sum(t) for t in product(range(1,9),repeat=2))
probs={str(threshold):sum(count for value,count in distribution.items() if value>=threshold)/64 for threshold in (6,8,12)}
result=dict(conferido=True,critico_fisico_com_canalizar_conferido=True,etapas=events,ramo_alternativo=dict(estado=alternative['status'],pv_depois_da_cura=alternative['hp']),chance_exata_2d8_atingir=probs)
(HERE/'resultado-exemplo-guiado.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False,indent=2))
