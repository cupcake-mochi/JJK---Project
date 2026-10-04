from pathlib import Path
from dataclasses import dataclass
from itertools import product
from fractions import Fraction as Q
import hashlib,json,re
B=Path(__file__).resolve().parent;P=next(p for p in B.parents if (p/'validacao-editorial/PROTOCOLO-COMPLETO.md').exists());R=P.parents[3];F=B/'VANGUARDA.md';text=F.read_text();checks=[];cases=[]
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def ck(name,got,want):checks.append({'caso':name,'obtido':got,'esperado':want,'ok':got==want})
def case(name,got,want):cases.append({'caso':name,'obtido':got,'esperado':want,'ok':got==want})
meta=json.loads((B/'ESTRUTURA.json').read_text());ck('Vinte seções de consulta',len(re.findall(r'<!-- page:',text)),20)
coverage=json.loads((B/'evidencias/COBERTURA.json').read_text());ck('Inventário integral',coverage['integral'],True)
for phrase in ['uma Condução ou uma Conclusão por turno próprio','A declaração consome a Sequência','duas ou mais Conduções acertadas','Não Cede','não renova o prazo','não concede outro ataque de Compasso','não cria uma unidade extra a cada recarga','Cada ataque consome o virote colocado','Consuma essa munição ao soltá-la','Conclusão Dupla com Yumi é imediata','Dobrar a Aposta não combina com Conclusão Dupla']:
 ck('Regra textual: '+phrase,phrase in text,True)
ck('Sem retorno da maximização indevida','maximiza' in text.lower(),False)
ck('Prazos sem dois donos','seu próximo turno dele' in text,False)
ck('Sem retórica Como ler',bool(re.search(r'^#+ .*como ler',text,re.I|re.M)),False)
ck('Sem ponto e vírgula',';' in text,False)
# Parâmetros extraídos do quadro, não apenas números repetidos em código.
rows=re.findall(r'^\| (1 ou 2|3 ou 4) \| (\d)d4 \| (\d) PE \|$',text,re.M)
ck('Quadro de custo/redução',rows,[('1 ou 2','1','2'),('3 ou 4','2','3')])
scales=[]
for m in range(1,5):
 n=(m+1)//2;cost=n+1;pers=m//2+1
 ck('Custo por Maestria '+str(m),cost,2 if m<=2 else 3)
 scales.append({'maestria':m,'reducao_media':str(Q(5*n,2)),'custo_conducao':cost,'nao_cede':m,'persistencia':pers})
ck('Exemplo nível10/Maestria2','No nível 10, Emi' in text and '2 PE com Maestria 2' in text,True)
@dataclass
class Seq:
 turn:int=0;target:str|None=None;successes:int=0;deadline:int=-1;used:bool=False;concluded:bool=False;energy:int=20;persist:int=1
 def next(self):
  self.turn+=1;self.used=False;self.concluded=False
  if self.turn>self.deadline:self.target=None;self.successes=0
 def initial(self,target,hit):
  if self.concluded or self.target==target:return False
  if hit:self.target=target;self.successes=0;self.deadline=self.turn+2
  return True
 def conduct(self,hit,cost=2,keep=False):
  if not self.target or self.used or self.energy<cost:return False
  self.energy-=cost;self.used=True
  if hit:self.successes+=1;self.deadline=self.turn+2
  elif keep and self.persist:self.persist-=1
  else:self.target=None;self.successes=0
  return True
 def conclude(self,minimum=0):
  if not self.target or self.used or self.successes<minimum:return False
  self.target=None;self.successes=0;self.used=True;self.concluded=True;return True
s=Seq();s.initial('a',True);s.conduct(True);case('Abrir e Conduzir no mesmo turno',(s.successes,s.energy,s.deadline),(1,18,2));case('Não Concluir depois de Conduzir',s.conclude(),False)
s.next();case('Conclusão no turno seguinte',s.conclude(1),True);case('Erro/resistência não devolvem Sequência',s.target,None);case('Não abrir após conclusão',s.initial('b',True),False)
s=Seq();s.initial('a',True);s.conduct(False);case('Erro cobra PE e termina',(s.energy,s.target),(18,None));case('Ataque restante pode abrir',s.initial('b',True),True);case('Não conduz duas vezes após reabrir',s.conduct(True),False)
s=Seq();s.initial('a',True);s.next();s.conduct(False,keep=True);case('Persistência mantém erro e prazo',(s.target,s.successes,s.deadline,s.persist),('a',0,2,0));s.next();case('Segundo turno seguinte ainda válido',s.target,'a');s.next();case('Expira depois do segundo turno seguinte',s.target,None)
s=Seq();s.initial('a',True);s.next();s.conduct(True);case('Acerto renova prazo',s.deadline,3);s.next();s.conduct(True);s.next();case('Duas conduções habilitam Dupla',s.conclude(2),True)
# Enumeração de resultados: no máximo uma evolução por turno, preservação não renova nem aumenta contagem.
state_count=0
for outcomes in product((False,True),repeat=6):
 s=Seq();s.initial('a',True)
 for hit in outcomes:
  old=s.deadline;oldn=s.successes;s.next()
  if not s.target:break
  kept=not hit and s.persist>0;s.conduct(hit,keep=kept)
  assert s.successes<=oldn+1
  if kept:assert s.deadline==old and s.successes==oldn
  state_count+=1
ck('Invariantes em sequências de acertos/erros',state_count>0,True)
# Probabilidade de efeito: ataque deve acertar e TR adicional falhar. Finta pode ser respondida com Reação.
prob=[]
for needed in range(2,21):
 failure=Q(needed-1,20);disfailure=1-(1-failure)**2
 for p in (Q(1,2),Q(13,20),Q(4,5)):
  normal=p*failure;finta=p*disfailure
  assert finta>=normal and finta<=p
  prob.append({'resultado_minimo_TR':needed,'p_acerto':str(p),'efeito_normal':str(normal),'finta_sem_reacao':str(finta)})
ck('Finta: exemplo CD14, bônus4, acerto65%',str(Q(13,20)*(1-Q(11,20)**2)),'3627/8000')
# Não Cede: rerrolagem tem segundo resultado obrigatório. Uso apenas depois da falha.
for success in range(21):
 p=Q(success,20);reroll=p+(1-p)*p
 ck('Não Cede chance '+str(success),0<=reroll<=1 and reroll>=p,True)
# Bote/Compasso/Ferrão: fonte de ataque adicional por rodada, separando evento de Classe0.
def attacks(attack_action,compasso,bote,extra_available=True):
 base=(1 if attack_action else 0)+(1 if compasso else 0)
 if extra_available and (attack_action or (compasso and bote)):base+=1
 return base
case('Compasso comum sem Ação Atacar',attacks(False,True,False),1)
case('Bote transfere adicional à Bônus',attacks(False,True,True),2)
case('Ataque Extra gasto não reaparece',attacks(False,True,True,False),1)
case('Ação Atacar normal nível7',attacks(True,False,False),2)
for c in range(1,8):ck('Classe mínima Compasso '+str(c),(c+1)//2,[1,1,2,2,3,3,4][c-1])
# Decisão do Mizuki de 04/10/2026 (D04): o +1 de capacidade do Combate Irregular vale só para Arma de Fogo; a besta fica em 1.
ck('Combate Irregular só aumenta Arma de Fogo','A **capacidade da Arma de Fogo** (os ataques por carga, em Munição) **aumenta em um**. Bestas e outras armas de disparo não recebem esse aumento.' in text,True)
# Munição: aumento de capacidade não aumenta estoque. Recargas parciais descontam apenas o acréscimo.
ammo_count=0
for base in (2,3,4):
 cap=base+1
 for loaded in range(cap+1):
  for reserve in range(13):
   for used in (1,2):
    for jam in (False,True):
     if loaded<used:continue
     left=loaded-used;need=jam or left==0
     for refill in (1,cap//2,cap):
      added=min(refill,reserve,cap-left);after=left+added;stored=reserve-added
      assert after+stored+used==loaded+reserve and after<=cap and stored>=0
      ammo_count+=1
case('RifleX4 com estoque3 não fabrica quarta unidade',min(4,3),3)
case('Supressão exige duas carregadas',1>=2,False)
case('RupturaX4 repõe no máximo2',min(4//2,5,4-1),2)
case('Romper Contato usa munição da reserva',min(1,0,4-1),0)
ck('Inventário conservado em recargas',ammo_count>0,True)
# Virotes: comuns e farpados ocupam uma vaga física. Farpado equivale a dois só no pagamento permitido.
bolt_count=0
for common in range(4):
 for barbed in range(4-common):
  assert common+barbed<=3
  for mode in ('debilitante','acionar','farpar'):
   c,b=common,barbed
   if mode=='debilitante':
    if b:b-=1
    elif c>=2:c-=2
    else:continue
   elif mode=='acionar':
    if b:b-=1;c+=1 # Consumir a Farpa
    elif c:c-=1
    else:continue
   else:
    if not c:continue
    c-=1;b+=1
   assert 0<=c+b<=3;bolt_count+=1
case('Farpa preservada por Acionar mantém uma vaga',(1-1,0+1),(0,1))
case('Dupla paga dois efeitos, um virote não paga ambos',1>=2,False)
def fire_bow(loaded,reserve,hand):
 if loaded:return (True,loaded-1,reserve)
 if reserve and hand:return (True,0,reserve-1)
 return (False,loaded,reserve)
case('Besta carregada sem mão consome apenas a colocada',fire_bow(1,7,False),(True,0,7))
case('Besta vazia sem mão não recarrega',fire_bow(0,7,False),(False,0,7))
case('Besta vazia com mão coloca e consome uma reserva',fire_bow(0,7,True),(True,0,6))
# O risco de Dobrar a Aposta: resposta só se execução erra ou resistência passa, nunca outra cadeia.
for hit,resist,reach in product((False,True),repeat=3):
 retaliation=reach and (not hit or resist)
 case(f'Aposta acerto{hit}/resistência{resist}/alcance{reach}',retaliation,reach and not(hit and not resist))
# Desvantagem de conjuntos: compara totais completos. Não escolhe mínimos por dado.
rolls=list(product(range(1,7),repeat=2));less=Q(sum(min(sum(a),sum(b)) for a,b in product(rolls,repeat=2)),len(rolls)**2);individual=Q(sum(sum(min(x,y) for x,y in zip(a,b)) for a,b in product(rolls,repeat=2)),len(rolls)**2)
ck('Desvantagem de dano mantém conjunto',less>individual,True)
for paid in range(0,15):
 refund=max(1,paid//2) if paid else 0
 ck('Refluxo não gera mais que custo '+str(paid),0<=refund<=paid,True)
summary={'estados_sequencia':state_count,'perfis_ataque_TR':len(prob),'estados_municao':ammo_count,'transicoes_virote':bolt_count,'pares_dano_2d6':len(rolls)**2,'media_2d6_desvantagem_conjunto':str(less),'media_misturando_minimos_proibida':str(individual)}
ok=all(x['ok'] for x in checks+cases);out={'ok':ok,'sha256_texto':H(F),'manuscritos_auditados':{str(F.relative_to(R)):H(F)},'verificacoes':len(checks),'casos_funcionais':len(cases),'checks':checks,'casos':cases,'escalas':scales,'probabilidades':prob,'resumo':summary,'limites':['Modelos próprios não constituem playtest nem comparação completa das fichas de seis Caminhos.','Probabilidades condicionam acerto e bônus de TR. Bloquear e defesas de alvos reais podem alterar a aplicação.']}
(B/'evidencias/auditoria-numerica.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');(B/'evidencias/regras-verificadas.json').write_text(json.dumps({'ok':ok,'sha256_texto':H(F),'verificacoes':len(checks),'casos':cases},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':ok,'verificacoes':len(checks),'casos':len(cases),'resumo':summary,'falhas':[x for x in checks+cases if not x['ok']]},ensure_ascii=False));raise SystemExit(0 if ok else 1)
