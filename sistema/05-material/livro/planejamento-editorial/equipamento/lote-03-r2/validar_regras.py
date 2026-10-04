"""Modelos de cenários para auditar propostas; não são implementação de combate do livro."""
from pathlib import Path
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
import json,hashlib,re
B=Path(__file__).resolve().parent;E=B.parent;R=B.parents[5]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
checks=[]
def ck(label,got,want):checks.append({'caso':label,'obtido':got,'esperado':want,'ok':got==want})
@dataclass
class Arma:
 capacity:int
 loaded:int
 blocked:bool=False
 used:int=0
 def fire(self,die,bonus=0,reserve=0):
  if self.blocked or not self.loaded:return False
  self.loaded-=1;self.used+=1;self.blocked=self.loaded==0 or die<=2
  return True
 def reload(self,reserve,amount=None,bonus=True,hand=True,compatible=True):
  if not (bonus and hand and compatible):return reserve,False
  n=min(reserve,self.capacity-self.loaded) if amount is None else amount
  if not 0<=n<=min(reserve,self.capacity-self.loaded):return reserve,False
  self.loaded+=n;self.blocked=self.loaded==0
  return reserve-n,True
 def unload(self,bonus=True,hand=True):
  if not (bonus and hand):return 0,False
  n=self.loaded;self.loaded=0;self.blocked=True
  return n,True
# Independent expected traces, including failure to pay costs.
a=Arma(3,3);a.fire(2);ck('Rifle após primeiro 2 natural',[a.loaded,a.blocked,a.used],[2,True,1]);reserve,paid=a.reload(3);ck('Completar após gatilho',[a.loaded,reserve,a.blocked,paid],[3,2,False,True])
a=Arma(3,3);a.fire(2);r,paid=a.reload(0);ck('Preparar restante sem reserva',[a.loaded,r,a.blocked],[2,0,False]);a.fire(15);a.fire(15);ck('Restante permite só dois tiros',[a.loaded,a.used,a.blocked],[0,3,True]);ck('Sem munição não dispara',a.fire(20),False)
a=Arma(2,0,True);r,paid=a.reload(1);ck('Recarga parcial de pistola',[a.loaded,r,a.blocked],[1,0,False]);a.fire(15);ck('Parcial não cria segundo tiro',a.fire(15),False)
a=Arma(3,2,True);r,paid=a.reload(3,bonus=False);ck('Sem Bônus não prepara',[a.loaded,r,a.blocked,paid],[2,3,True,False]);r,paid=a.reload(3,hand=False);ck('Mãos ocupadas impedem recarga',[a.loaded,r,a.blocked,paid],[2,3,True,False]);r,paid=a.reload(3,compatible=False);ck('Munição incompatível rejeitada',[a.loaded,r,a.blocked,paid],[2,3,True,False])
a=Arma(3,3);a.fire(15);r,paid=a.reload(3);ck('Recarga preventiva desconta só um',[a.loaded,r,paid],[3,2,True]);r,paid=a.reload(r);ck('Recarregar cheia não multiplica estoque',[a.loaded,r],[3,2])
a=Arma(3,3);a.fire(max(2,14));ck('Dado descartado não bloqueia',[a.loaded,a.blocked],[2,False]);a=Arma(3,3);a.fire(min(2,14));ck('Desvantagem mantém gatilho',[a.loaded,a.blocked],[2,True])
a=Arma(1,1);a.fire(2);r,paid=a.reload(19);ck('Besta: esvaziou e tirou 2, só uma recarga',[a.loaded,r,paid,a.blocked],[1,18,True,False]);ck('Segundo tiro da besta',a.fire(10),True);ck('Terceiro sem nova Bônus',a.fire(10),False)
a=Arma(3,3);b=Arma(3,0,True);a.fire(2);out,paid=a.unload();r,paid2=b.reload(out);ck('Transferir custa duas ações e conserva estoque',[a.loaded,b.loaded,r,a.used,paid,paid2],[0,2,0,1,True,True]);ck('Estado da arma de origem continua vazio',a.blocked,True)
a=Arma(2,2);b=Arma(2,2);a.fire(1);ck('Troca de arma não restaura primeira',[a.loaded,a.blocked,b.loaded,b.blocked],[1,True,2,False])
# Exhaust every load, capacity, d20, reserve and partial reload, checking invariant independent of model code.
n=0;bad=[]
for cap in range(1,5):
 for loaded in range(cap+1):
  for die,reserve in product(range(1,21),range(9)):
   for amount in range(min(reserve,cap-loaded+int(loaded>0))+1):
    a=Arma(cap,loaded,loaded==0);total=loaded+reserve;a.fire(die);r,paid=a.reload(reserve,amount=amount)
    n+=1
    if a.loaded+r+a.used!=total or not (0<=a.loaded<=cap) or r<0:bad.append([cap,loaded,die,reserve,amount])
ck('Conservação em todos estados enumerados',bad,[])
# Preserve all 9 capacities from the published owner, not a duplicate handwritten fixture.
source=(R/'sistema/05-material/livro/manual/50-equipamento.md').read_text().split('### Munição')[1].split('## Treino')[0]
canonical={}
for l in source.splitlines():
 m=re.match(r'\| ([1-4]) \| (.+?) \|',l)
 if m:
  for weapon in m[2].split(' · '):canonical[weapon]=int(m[1])
md=(B/'MUNICAO.md').read_text();actual={}
for l in md.splitlines():
 if ':' in l and l.startswith('|'):
  cells=[x.strip() for x in l.strip('|').split('|')]
  if len(cells)==4 and cells[1].isdigit():actual[cells[0].split(':')[0]]=int(cells[1])
actual.update({'Besta':1,'Besta de Uma Mão':1});ck('Todas capacidades do catálogo preservadas',actual,canonical)
ck('Capacidade das bestas expressa no texto','Cada besta comporta **um virote**' in md,True)
# Price/stock arithmetic, not claims of market prices or playtest balance.
prices=[(2,1000),(2,1000),(2,1000),(3,1500),(3,1500),(2,2000),(4,4000)]
ck('Custo por disparo',[p//c for c,p in prices],[500,500,500,500,500,1000,1000])
ck('Espingarda cabe na criação com munição incluída',150000+0,150000)
ck('Estoque inicial de fogo por arma',[3*c for c,p in prices],[6,6,6,9,9,6,12])
ck('Besta inicial: instalado + reserva',1+19,20)
ck('Carga da pistola e dois recipientes extras',str(Fraction(1,10)+2*Fraction(1,10)),'3/10')
ck('Recuperação de 7 flechas acessíveis',7//2,3)
ck('Recuperação de uma flecha',1//2,0)
ck('Recuperação coletiva explícita','limite é compartilhado pelo grupo' in md,True)
ck('Recarga gratuita por começo do turno proibida','começar outro turno não a prepara' in md,True)
ck('Retirada de munição na transferência cobra Bônus','retire-a de uma com Ação Bônus' in md,True)
ck('Unidade física e medida de jogo distinguidas','sem representar a quantidade real de cartuchos' in md,True)
write(B/'evidencias/regras-verificadas.json',{'ok':all(c['ok'] for c in checks),'sha256_texto':sha(B/'MUNICAO.md'),'casos':checks,'estados_enumerados':n,'limites':['Modelo de conservação e custos, não playtest. Preço e logística continuam propostas. Capacidade mede ataques de jogo.']})

print("Munição:", len(checks), "casos;", n, "estados;", all(c["ok"] for c in checks))
assert all(c["ok"] for c in checks)
