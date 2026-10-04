from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json
B=Path(__file__).resolve().parent
# Modelo da candidata: 20 natural acerta; duplo1 força acerto;
# duplo10 impede o acerto comum. Não inclui ataques de Reação.
def acerta(r,x,y,defesa,bonus):
 if r==20:return True
 if (x,y)==(10,10):return False
 if (x,y)==(1,1):return True
 return r+bonus>=x+y+defesa-11

def medir(D,A):
 casos=list(product(range(1,21),range(1,11),range(1,11)))
 fix=F(sum(r==20 or r+A>=D for r in range(1,21)),20)
 todos=F(sum(acerta(r,x,y,D,A) for r,x,y in casos),2000)
 seletivo=F(sum((r==20 or r+A>=D) and acerta(r,x,y,D,A) for r,x,y in casos),2000)
 # Cálculo separado pela distribuição triangular da soma de 2d10.
 condicionais=[]
 for r in range(1,21):
  if r==20:q=F(1)
  else:
   q=sum((F(10-abs(11-s),100) for s in range(2,21) if r+A>=s+D-11),F(0))
   if r+A>=20+D-11:q-=F(1,100)
   if r+A<2+D-11:q+=F(1,100)
  condicionais.append(q)
 assert todos==sum(condicionais,F(0))/20
 assert seletivo==sum((q for r,q in enumerate(condicionais,1) if r==20 or r+A>=D),F(0))/20
 assert seletivo<=fix
 return {'defesa':D,'bonus_ataque':A,'estatica_pct':float(fix*100),'bloquear_sempre_pct':float(todos*100),'bloquear_apenas_acertos_pct':float(seletivo*100),'fracao_seletiva':str(seletivo)}
rows=[medir(D,A) for D in range(10,26) for A in range(1,11)]
ref=next(r for r in rows if r['defesa']==17 and r['bonus_ataque']==6)
assert ref['estatica_pct']==50 and ref['bloquear_sempre_pct']==50.05 and ref['bloquear_apenas_acertos_pct']==41.75
assert acerta(20,10,10,25,1)
assert not acerta(19,10,10,17,6)
assert acerta(1,1,1,25,1)
assert acerta(11,7,4,17,6)
assert not acerta(12,8,5,17,6)
res={'modelo':'Chance de o ataque original acertar. Sem contra-ataques, dano, talentos, vantagem, desvantagem ou escolha para gerar recursos.','regras':['20 natural acerta','Duplo1 acerta independentemente do total','Duplo10 impede acerto, exceto20 natural','Escolha seletiva: manter Defesa se já seria erro; Bloquear se seria acerto'],'comparacoes':len(rows),'combinacoes_por_ficha':2000,'checagem_independente':'Distribuição triangular de 2d10 reproduz enumeração completa em todas as 160 fichas.','exemplo':ref,'matriz':rows,'limites':['Isso mede o ataque original, não o equilíbrio do combate.','Defesa26+ e bônus0 ou negativos não foram incluídos na matriz.','O modelo explicita a leitura de20 natural registrada em DECISOES.md.','O validador publicado não modela esta escolha condicional nem força Brecha fora do parelho.']}
(B/'evidencias/contas-bloquear.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'comparacoes':len(rows),'exemplo':ref},ensure_ascii=False))
