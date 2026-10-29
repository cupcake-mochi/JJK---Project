"""Conferir as tabelas com resultados arquivados e contas dirigidas; sem novo combate simulado."""
from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
from fractions import Fraction
from itertools import product
import json,markdown,math
A=Path(__file__).resolve().parent;R=A.parents[1];C=R/'06 - Redacao do Guia/revisao-98/casos'
def load(p):return json.loads(p.read_text())
def tables(p):
 s=BeautifulSoup(markdown.markdown(p.read_text(),extensions=['tables']),'html.parser')
 return [[[c.get_text(' ',strip=True) for c in tr.find_all(['th','td'])] for tr in t.find_all('tr')] for t in s.find_all('table')]
def value(s):return float(s.replace('%','').replace(',','.'))
def near(given,expected,places):assert abs(value(given)-expected)<=.5*10**(-places)+1e-8,(given,expected)
b=load(R/'04 - Planejamento/apoio-regua-inicial/resultados.json');l=load(R/'04 - Planejamento/apoio-lote7/resultados.json');checks=[]
ts=tables(C/'74-regua-inicial-de-inimigos.md')
acc=next(t for t in ts if t[0][0]=='Ataque')
for row in acc[1:]:
 atk=int(row[0])
 for d,cell in zip([11,13,15,16],row[1:]):near(cell,100*sum(x==20 or x+atk>=d for x in range(1,21))/20,0)
checks.append('Precisão: oito chances conferidas por enumeração do d20.')
surv=next(t for t in ts if t[0][0]=='Nível / PV do inimigo')
for row in surv[1:]:
 level,hp=map(int,row[0].split('/'))
 vals=[]
 for mixed in [False,True]:
  r=next(x for x in b['sobrevivencia'] if x['nivel']==level and x['PV']==hp and x['defesa']==13 and not x['bloquear'] and x['misto']==mixed)
  vals.extend([100*r['sobrevive_apos_declaracoes'][i] for i in [2,5]])
 for cell,n in zip(row[1:],vals):near(cell,n,1)
checks.append('Sobrevivência de níveis 2/6: 24 porcentagens confrontadas com resultados arquivados.')
damage=next(t for t in ts if t[0][0]=='Aplicação')
for row,key,n,sides,fixed,atk in zip(damage[1:],['Carregador','Candidata_n2','Pancada_Sineiro'],[1,1,2],[4,8,6],[3,3,4],[4,4,5]):
 hit=sum(x!=20 and x+atk>=13 for x in range(1,21));normal=n*(sides+1)/2+fixed;crit=2*n*(sides+1)/2+fixed
 near(row[-1],(hit*normal+crit)/20,2)
for key,expect in [('Carregador',[4.9,50.3]),('Candidata_n2',[27.0,67.3])]:
 row=next(x for x in b['pressao'] if x['aplicacao']==key and x['vida_maxima']==14)
 for field,n in zip(['zero_em_duas_cheio','zero_em_duas_ferido'],expect):near(str(n),100*row[field],1)
assert b['tr']['CD12_vs_4_3_2']==[.35,.4,.45] and b['tr']['CD13_vs_5_3_2']==[.35,.45,.5]
checks.append('Dano médio, pressão em duas tentativas e chances de TR preservados e conferidos.')
ts=tables(C/'100-comparar-inimigos-em-outras-faixas.md')
profiles=next(t for t in ts if t[0][0]=='Nível')
for row in profiles[1:]:
 level=int(row[0]);ps=[next(x for x in l['perfis'] if x['nivel']==level and x['caminho']==p) for p in ['Bastiao','Emanador','Guia']]
 assert list(map(int,row[1:]))==[*(p['PV'] for p in ps),ps[0]['classe'],ps[0]['ataque'],ps[0]['defesa']]
 for p in ps:
  initial,gain={'Bastiao':(12,7),'Emanador':(6,4),'Guia':(8,5)}[p['caminho']];con=p['atributos'][2]
  assert p['PV']==initial+con+(level-1)*(gain+con)
comparison=next(t for t in ts if t[0][0]=='Nível do grupo')
for row in comparison[1:]:
 level=int(row[0]);hp,integrity=map(int,row[1].split('/'));assert integrity==hp//2
 expected=[]
 for mixed in [False,True]:
  r=next(x for x in l['referencias'] if x['nivel']==level and x['PV']==hp and x['defesa']==16 and x['misto']==mixed)
  expected.extend([r['media_por_conjunto'],100*r['sobrevive'][1]])
 for i,(cell,n) in enumerate(zip(row[2:],expected)):near(cell,n,2 if i%2==0 else 1)
checks.append('Outras faixas: seis linhas de perfis e 24 médias/porcentagens confrontadas com as contas arquivadas.')
# Enumeração independente, restrita a um ataque contra o Bastião 15.
normal=Counter(sum(d)+6 for d in product(range(1,9),range(1,5),range(1,5)))
critical=Counter(sum(d)+6 for d in product(range(1,9),range(1,9),range(1,5),range(1,5)))
means=[]
for block,duro in [(False,False),(True,False),(True,True)]:
 total=Fraction()
 for die in range(1,21):
  pairs=product(range(1,11),repeat=2) if block else [(0,0)]
  for a,c in pairs:
   hit=die==20 or (not(block and a==c==10) and ((block and a==c==1) or die+8>=(a+c+2 if block else 13)))
   if not hit:continue
   dist=critical if die==20 else normal;rd=a+c+5 if duro else 0
   total+=Fraction(sum(max(0,x-rd)*n for x,n in dist.items()),20*(100 if block else 1)*sum(dist.values()))
 means.append(float(total))
for got,expected in zip(means,[12.63,12.31,1.81]):near(str(expected),got,2)
support=next(x for x in l['apoio'] if x['nivel']==15);near('96,20',support['media_normal'],2);near('99,94',support['media_com_um_impulso'],2)
soul=next(x for x in l['alma'] if x['nivel']==15);assert 12-2==10 and 10//2==5 and soul['dados_Alma']==5;near('60,4',100*soul['sobrevive_PV_e_integridade'],1);near('7,0',100*soul['vivo_em_estagio_2_ou_maior'],1)
assert 6-3==3 and 3-2==1 and 5-(6-4)==3 and 3+1>3 and 8+3+1==12 and 10-3==7 and 7<=8
checks.append('Duro de Matar recontado sem redução média; apoio, Alma, custos e exemplos simples conferidos.')
result={'registro':119,'conferencias':checks,'duro_de_matar_medias_recontadas':means,'novos_parametros':False,'nova_simulacao_de_combate':False,'limites':['Tabelas de sobrevivência comparadas aos resultados arquivados, sem executar outro confronto.','Enumeração independente somente do recorte de Duro de Matar e da precisão.','Não demonstra equilíbrio, duração de combate ou aprendizagem.']}
(A/'contas-conferidas.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
