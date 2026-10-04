from pathlib import Path
from fractions import Fraction
from math import ceil
import json
b=Path(__file__).resolve().parent.parent
def primeira(base,fixa):
 atual=base;usos=[]
 while True:
  custo=ceil(Fraction(base if fixa else atual,8))
  if atual-custo<1:break
  atual-=custo;usos.append(custo)
 return {'ativacoes':len(usos),'custos':usos,'maximo_final':atual}
comparacao=[{'referencia':m,'recalcular_em_cada_queda':primeira(m,False),'base_sem_perdas_por_insistir':primeira(m,True)} for m in [23,80,305]]
falhas=[];pares=0;parcelas=0
for base in range(1,401):
 for inicial in range(1,base+1):
  pares+=1;atual=inicial
  for denom in (8,4,2):
   custo=ceil(Fraction(base,denom));parcelas+=1
   if atual-custo<1:break
   anterior=atual;atual-=custo
   if not 1<=atual<anterior:falhas.append([base,inicial,denom])
  if not 1<=atual<=inicial:falhas.append([base,inicial,'final'])
assert pares==80200 and not falhas
# Referência80 e saldo10 impedem primeira parcela; saldo20 paga1ª e não paga2ª.
assert ceil(Fraction(80,8))==10
assert 10-10<1 and 20-10>=1 and 10-ceil(Fraction(80,4))<1
assert sum(ceil(Fraction(80,d)) for d in (8,4,2))==70
res={'pares_base_saldo':pares,'parcelas_examinadas':parcelas,'falhas':falhas,'comparacoes':comparacao,'escopo':'Modelo candidato de custos. Em ambos os comparadores há proteção contra máximo zero; só varia a referência. Supõe cura e nova queda depois de cada primeira parcela, sem medir chance, ações ou PE. Não é simulação de combate nem playtest.'}
(b/'evidencias/quedas-sucessivas.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(res,ensure_ascii=False,indent=2))
