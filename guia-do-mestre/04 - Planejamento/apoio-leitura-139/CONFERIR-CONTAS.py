"""Reconferência independente de probabilidades selecionadas dos casos 74 e 76."""
from pathlib import Path
from functools import lru_cache
from collections import defaultdict
import json
A=Path(__file__).resolve().parent
@lru_cache(None)
def dice(n,sides):
 d={0:1.0}
 for _ in range(n):
  new=defaultdict(float)
  for a,p in d.items():
   for face in range(1,sides+1):new[a+face]+=p/sides
  d=dict(new)
 return d
def add(x,y):
 out=defaultdict(float)
 for a,p in x.items():
  for b,q in y.items():out[a+b]+=p*q
 return dict(out)
def attack(bonus,defense,normal,critical):
 hit=sum(1 for roll in range(2,20) if roll+bonus>=defense)/20
 out=defaultdict(float);out[0]=1-hit-.05
 for damage,p in normal.items():out[damage]+=hit*p
 for damage,p in critical.items():out[damage]+=.05*p
 assert abs(sum(out.values())-1)<1e-10
 return dict(out)
def shift(d,k):return {x+k:p for x,p in d.items()}
def spell(level,defense):
 bonus=4 if level==2 else 5;n=3 if level==2 else 6
 return attack(bonus,defense,dice(n,8),dice(n*2,8))
def sword(level,defense):
 bonus=4 if level==2 else 5;strength=3 if level==2 else 4
 return attack(bonus,defense,shift(add(dice(1,8),dice(1,4)),strength),shift(add(dice(2,8),dice(1,4)),strength))
def body(level,defense,alternative=False):
 bonus=4 if level==2 else 5;strength=3 if level==2 else 4
 n,sides=(1,8) if alternative else ((1,4) if level==2 else (2,6))
 return attack(bonus,defense,shift(dice(n,sides),strength),shift(dice(n*2,sides),strength))
def survive(d,hp):return sum(p for dmg,p in d.items() if dmg<hp)*100
rows=[]
expected={2:[[25.2,2.9,29.1,3.6],[43.4,7.1,50.1,9.4],[65.4,15.5,73.0,19.8]],6:[[34.6,3.8,55.5,9.7],[70.1,13.5,88.0,28.9],[96.5,44.2,99.5,70.3]]}
for level,hps in [(2,[16,24,32]),(6,[48,72,108])]:
 f=spell(level,13);s=sword(level,13);three=add(add(f,f),f);six=add(three,three);mixed=add(add(s,f),f);twomixed=add(mixed,mixed)
 for hp,ref in zip(hps,expected[level]):
  actual=[survive(d,hp) for d in [three,six,mixed,twomixed]]
  assert max(abs(x-y) for x,y in zip(actual,ref))<.051,(level,hp,actual,ref)
  rows.append({'nivel':level,'pv':hp,'calculado_percentual':actual,'publicado_percentual':ref})
means=[]
for level,alt,ref in [(2,False,3.43),(2,True,4.73),(6,False,7.50)]:
 d=body(level,13,alt);v=sum(x*p for x,p in d.items());assert abs(v-ref)<=.0050001
 means.append({'nivel':level,'alternativa':alt,'media_calculada':v,'media_publicada':ref})
drop=[]
for hp,ref1,ref2 in [(14,4.9,27.0),(7,50.3,67.3)]:
 values=[]
 for alt,ref in [(False,ref1),(True,ref2)]:
  d=body(2,13,alt);value=100-survive(add(d,d),hp);assert abs(value-ref)<.051,(hp,alt,value,ref);values.append(value)
 drop.append({'pv_iniciais':hp,'probabilidade_de_zero_percentual':values,'publicado_percentual':[ref1,ref2]})
# As duas conjurações atingem um mesmo alvo que reduz 3 do primeiro dano positivo.
five=attack(5,13,dice(5,8),dice(10,8));six=spell(6,13);joint=add(five,six);targets=[]
for name,hp,ref in [('Sayo',48,23.9),('Toru',67,4.5)]:
 actual=100-survive(joint,hp+3);assert abs(actual-ref)<.051,(name,actual,ref)
 targets.append({'alvo':name,'probabilidade_calculada_percentual':actual,'publicada_percentual':ref})
result={'registro':139,'metodo':'Distribuições discretas independentes; ataques contra Defesa estática, erro natural e crítico natural, dados de Canalizar não duplicados. Hipóteses restritas às tabelas citadas.','tolerancia_percentual':'0,051 ponto percentual para valores publicados com uma casa decimal.','sobrevivencia_caso_74':rows,'medias_corporais_caso_74':means,'duas_tentativas_caso_74':drop,'escolha_de_alvo_caso_76':targets,'falhas':[],'limite':'Não inclui oponente agindo, socorro, escolhas de mesa ou equilíbrio. Não reconfere todos os percentuais do livro nem substitui os estados dos confrontos.'}
(A/'contas-reconferidas.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Contas selecionadas dos casos 74 e 76 reproduzidas, sem divergências além do arredondamento publicado.')
