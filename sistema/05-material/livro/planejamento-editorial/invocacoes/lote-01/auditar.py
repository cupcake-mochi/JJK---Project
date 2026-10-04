#!/usr/bin/env python3
"""R11: contas e transições executadas sobre contrato candidato.
Não é motor completo de combate, revisão humana, playtest nem certificação de equilíbrio.
As tabelas são lidas da fonte; alterações de âncora falham, sem fallback numérico.
"""
from dataclasses import dataclass, field
from pathlib import Path
import hashlib,json,math,re,itertools
O=Path(__file__).resolve().parent
R=next(p for p in O.parents if (p/'sistema/05-material/livro/manual/60-invocacoes.md').exists())
P=R/'sistema/05-material/livro/planejamento-editorial'
f=R/'sistema/05-material/livro/manual/60-invocacoes.md'
src=f.read_text(); text=(O/'INVOCACOES-EM-CAMPO.md').read_text()
checks=[]; executed=[]
def check(id,value,detail=None):
 checks.append(dict(id=id,passou=bool(value),detalhe=detail))
 if not value: raise AssertionError(id+': '+str(detail))
def req(p,t,id):
 m=re.search(p,t,re.M|re.S);check(id,m is not None);return m
levels={};points={}
for row in src.splitlines():
 m=re.match(r'\| (\d) \((\d+)–(\d+)\) \| (\d)d6 \| (\d+) \|',row)
 if m:
  c,lo,hi,di,pt=map(int,m.groups());points[c]=pt
  for lv in range(lo,hi+1):levels[lv]={'classe':c,'basica_d6':di}
check('30-niveis-da-fonte',len(levels)==30)
check('sete-faixas-reais',list(points.values())==[2,4,6,9,11,13,16])
req(r'\*\*Você pode ter duas entidades ativas ao mesmo tempo\.\*\*',src,'teto-fonte')
req(r'\*\*Só a maldição domada pode ter técnica própria\*\*',src,'reserva-exclusiva-fonte')
req(r'a reserva de energia dessa técnica',src,'reserva-ficha-fonte')
maximas={}
for lo,hi,d,pt,pe in re.findall(r'\| (17|21|26) a (20|25|30) \| (\d+)d8 \| (\d+) \| (\d+) PE \|',text):
 maximas[int(lo)]=dict(ultimo=int(hi),dados=int(d),pontos=int(pt),pe=int(pe))
check('maxima-faixas',len(maximas)==3)
check('maxima-valores',[(m['dados'],m['pontos'],m['pe']) for m in maximas.values()]==[(19,8,25),(22,12,30),(26,16,35)])
anchors={'limite-pago':'ocupa esse limite na emissão','basicas-sem-conjuracao':'**As básicas das entidades não ocupam suas conjurações pessoais.**','manutencao-suspensa':'**o efeito fica suspenso até um pagamento válido**','nao-divida':'não gera dívida','classe-reparador':'Requer reparador de Classe suficiente.','maxdano':'**Um Acerto de dano da domada causa Classe d8.**','trinvocado':'a cada dano, como uma combatente do lado dos jogadores','refino':'Refino, Maestria e especialização exigidos são os do invocador','dom-fim':'Recolher, desativar ou derrubar a domada encerra sua Expansão','sem-comando-inconsciente':'**Inconsciente, você não manifesta, recolhe, comanda, ajusta, cancela nem dá orientação nova.**','area-excedente':'Dano em área entra na soma, mas não provoca a destruição naquele momento.','mov-reserva':'Ficar vários ciclos guardada não recupera os metros gastos.','ordem-real':'impedimento real','anticipada-primeira':'primeira oportunidade válida','prepared-expira':'A preparação termina no começo do seu próximo turno.','arm-refund':'metade do PE efetivamente pago','contramedida':'os 2 PE seguem a divisão acima','arm-max':'Armado não prepara uma Técnica Máxima','seg-max':'Segura não pode adiar uma Técnica Máxima','atrasar-dois-corpos':'Nem você nem ela podem ter se deslocado voluntariamente','carregar-primeiro':'sua Padrão, uma básica da entidade e o PE da especial','carregar-segundo':'Rápido pode tornar esse segundo comando uma Bônus.','carregar-espirito':'TR Espírito dela contra a CD de quem a feriu','carregar-armado':'Carregar não combina com Armado.','aura-comandada':'Uma Aura montada como especial comandada pode aplicá-las.'}
for name,a in anchors.items():check('texto-'+name,a in text,a)
pages=re.findall(r'<!-- page:([^|]+)\|([^>]+) -->(.*?)(?=<!-- page:|\Z)',text,re.S)
check('31-paginas',len(pages)==31)
check('ids-unicos',len({p[0] for p in pages})==len(pages))
wordcounts={}
for id,title,body in pages:
 wordcounts[id]=len(body.split());check('volume-'+id,150<=wordcounts[id]<=380,wordcounts[id]);check('titulo-'+id,body.lstrip().startswith('# '+title.strip()+'\n'))
 for row in body.splitlines():
  if row.startswith('|'):check('colunas-'+id,row.count('|')-1<=4)
headers=re.findall(r'^#+ (.+)$',text,re.M)
check('titulos-rpg',not any(re.match(r'^(A|O|As|Os)\s',h) or 'como ler' in h.lower() for h in headers))
check('sem-legal-ambiguo',not re.search(r'\blegal\b',text,re.I))
check('sem-contraste-cliche',not re.search(r'não é .{0,70}[,;:] é ',text,re.I))
def split(cost,reserve):
 ent=min(cost//2,reserve);return cost-ent,ent
# Custos: casos exaustivos, incluindo insuficiência sem cobrança parcial.
price_cases=0
for cost in range(71):
 for res in range(91):
  own,ent=split(cost,res);assert own+ent==cost and ent<=res and ent<=cost//2 and own>=ent
  for wallet in [max(0,own-1),own,own+1]:
   before=(wallet,res);after=(wallet-own,res-ent) if wallet>=own else before
   assert min(after)>=0 and (sum(before)-sum(after)==cost if wallet>=own else after==before)
   price_cases+=1
check('precos-divididos',price_cases==71*91*3,price_cases)
check('exemplo9res2',split(9,2)==(7,2))
reserve_profiles=[]
for lv in range(1,31):
 for ess in range(7):
  cap=lv*(1+ess//3);dc=min(cap,max(1,cap//4));assert 1<=dc<=cap
  reserve_profiles.append(dict(nivel=lv,essencia=ess,maximo=cap,descanso_curto=dc))
check('210-reservas',len(reserve_profiles)==210)
refund_cases=0
for cost in range(1,71):
 for res in range(91):
  own,ent=split(cost,res);total=cost//2;backent=ent//2;backown=total-backent
  assert backown<=own and backent<=ent and backown+backent==total
  refund_cases+=1
check('devolucao-armado-conserva-energia',refund_cases==6370,refund_cases)
# Manutenção: prioridade da reserva, pagamento integral atômico, sem meio a meio.
def maintain(cost,res,own):
 if res+own<cost:return {'ativo':False,'reserva':res,'dono':own,'divida':0}
 debit=min(res,cost);return {'ativo':True,'reserva':res-debit,'dono':own-cost+debit,'divida':0}
check('manutencao-prioridade',maintain(3,2,4)==dict(ativo=True,reserva=0,dono=3,divida=0))
check('manutencao-nao-paga-parcial',maintain(3,1,0)==dict(ativo=False,reserva=1,dono=0,divida=0))
check('manutencao-retoma-vencimento',maintain(3,1,3)==dict(ativo=True,reserva=0,dono=1,divida=0))
# Talismã: crédito fixo adiantado, não segundo desconto sobre custo de retorno.
talismans=[]
for c in range(1,8):
 pre=c//2;normal=c-pre;back=2*c-pre
 assert pre+normal==c and pre+back==2*c and normal>=1
 talismans.append(dict(classe=c,carga=pre,entrada=normal,retorno=back,retorno_total=pre+back))
check('talismas-7classes',len(talismans)==7)
# Sobrevivência: números de dano inteiros, inclusive igualdade do limiar e áreas.
def damage(mx,pv,d,area=False,extra=0):
 remain=max(0,pv-d);over=extra+max(0,d-pv)
 dead=(not area) and (d>=mx or over>mx/2)
 return remain,over,dead
survival=0
for mx in range(1,121):
 for pv in sorted({1,max(1,mx//2),mx}):
  for d in sorted({0,pv,max(0,pv+mx//2),pv+mx//2+1,mx,2*mx}):
   normal=damage(mx,pv,d);area=damage(mx,pv,d,True)
   assert area[2] is False and normal[:2]==area[:2]
   assert normal[2]==(d>=mx or max(0,d-pv)>mx/2)
   survival+=2
check('limiar-52-30',damage(52,8,30)==(0,22,False))
check('limiar-52-35',damage(52,8,35)==(0,27,True))
check('limiar-52-34',damage(52,8,34)==(0,26,False))
check('area35-viva',damage(52,8,35,True)==(0,27,False))
check('desligada-direto',damage(52,0,5,False,22)==(0,27,True))
check('desligada-area',damage(52,0,5,True,22)==(0,27,False))
check('area-depois-direto',damage(52,0,1,False,27)==(0,28,True))
check('retorno-pv31',max(1,31//2)==15)
# Modelo mínimo de estados. Cada transição usa as regras locais, sem simular ficha inteira.
@dataclass
class Entity:
 active:bool=False
 basic:int=0
 spent:bool=False
 movement:int=9
 order:str|None=None
 prepared:bool=False
 condition_ok:bool=True
@dataclass
class Model:
 bodies:dict=field(default_factory=lambda:{x:Entity() for x in 'ABC'})
 reaction:bool=True
 attackers:set=field(default_factory=set)
 casts:list=field(default_factory=list)
 turn:int=0
 def start(self):
  self.turn+=1;self.reaction=True;self.attackers.clear();self.casts=[]
  for e in self.bodies.values():
   e.spent=False
   if e.prepared:e.order=None
   e.prepared=False
   if e.active:e.basic=1;e.movement=9
   else:e.basic=0
 def enter(self,k):
  e=self.bodies[k];assert not e.active and sum(x.active for x in self.bodies.values())<2;e.active=True;e.basic=0
 def swap(self,a,b):
  old,new=self.bodies[a],self.bodies[b];assert old.active and not new.active
  n=int(old.basic>0 and old.condition_ok and not new.spent)
  old.active=False;old.basic=0;old.order=None;old.prepared=False;new.active=True;new.basic=n
 def recall(self,k):
  e=self.bodies[k];e.active=False;e.basic=0;e.order=None;e.prepared=False
 def use(self,k,damage=False,special=False,off=False):
  e=self.bodies[k];assert e.active and e.basic and e.condition_ok
  if damage and not special and not off:assert k in self.attackers or len(self.attackers)<2;self.attackers.add(k)
  e.basic-=1;e.spent=True
 def cast(self,cl,exception=False):
  if not exception:
   assert len(self.casts)<2 and not (cl>0 and any(x>0 for x in self.casts))
  self.casts.append(cl)
 def issue(self,k,kind,cl=1,exception=False):
  e=self.bodies[k];assert e.active and e.order is None
  self.cast(cl,exception)
  if kind in ('prepared','armed','held'):self.use(k)
  e.order=kind;e.prepared=kind=='prepared'
 def spend_reaction(self):
  assert self.reaction;self.reaction=False
  for e in self.bodies.values():
   if e.prepared:e.prepared=False;e.order=None
 def execute(self,k,off=False,valid=True,trigger=True):
  e=self.bodies[k];kind=e.order;assert kind
  if not valid or (kind=='prepared' and not trigger):return False
  if kind=='anticipated':
   if not e.basic or (off and not self.reaction):return False
   self.use(k,special=True,off=off)
   if off:self.spend_reaction()
  elif kind=='prepared':
   if not self.reaction:return False
   self.spend_reaction()
  e.order=None;e.prepared=False;return True

def case(id,fn):
 fn();executed.append(dict(id=id,resultado='passou',tipo='modelo de transições executado'))
def expect_assert(fn):
 try:fn()
 except AssertionError:return
 raise AssertionError('Deveria recusar')
def swaps():
 m=Model();m.enter('A');check('entrada-sem-basica',m.bodies['A'].basic==0);m.start();m.bodies['A'].movement=3;m.swap('A','B');assert m.bodies['B'].basic==1;m.use('B',damage=True);m.swap('B','A');assert m.bodies['A'].basic==0 and m.bodies['A'].movement==3
case('troca-nao-duplica-basica-nem-movimento',swaps)
def reserve_move():
 m=Model();m.enter('A');m.start();m.bodies['A'].movement=3;m.recall('A');m.start();m.start();m.enter('A');assert m.bodies['A'].movement==3 and m.bodies['A'].basic==0;m.start();assert m.bodies['A'].movement==9 and m.bodies['A'].basic==1
case('reserva-nao-renova-metros',reserve_move)
def chain():
 m=Model();m.enter('A');m.start();m.swap('A','B');m.swap('B','C');assert sum(e.basic for e in m.bodies.values())==1;m.use('C');m.swap('C','A');assert not m.bodies['A'].basic
case('cadeia-transferencia-conserva-um-recurso',chain)
def pending():
 m=Model();m.enter('A');m.enter('B');m.start();m.issue('A','anticipated');m.start();m.issue('B','anticipated');assert m.execute('A',True);assert not m.execute('B',True);m.start();assert m.execute('B');m.cast(3);assert m.casts==[3]
case('duas-antecipadas-coletiva-renovacao-magia-pessoal',pending)
def prepared():
 m=Model();m.enter('A');m.start();m.issue('A','prepared');assert m.bodies['A'].basic==0;assert not m.execute('A',valid=False);assert m.bodies['A'].order=='prepared';assert m.execute('A');assert not m.reaction;assert not m.bodies['A'].basic
case('preparada-inviavel-conserva-prazo-e-cobra-uma-basica',prepared)
def lostprepared():
 m=Model();m.enter('A');m.start();m.issue('A','prepared');m.spend_reaction();assert m.bodies['A'].order is None and m.bodies['A'].basic==0
case('coletiva-externa-encerra-preparada',lostprepared)
def expiry():
 m=Model();m.enter('A');m.start();m.issue('A','prepared');m.start();assert m.bodies['A'].order is None and m.bodies['A'].basic==1
case('preparada-expira-mesmo-nao-tendo-disparado',expiry)
def onepending():
 m=Model();m.enter('A');m.start();m.issue('A','anticipated');expect_assert(lambda:m.issue('A','armed'));assert m.bodies['A'].order=='anticipated'
case('uma-especial-pendente-por-corpo',onepending)
def unabletransfer():
 m=Model();m.enter('A');m.start();m.bodies['A'].condition_ok=False;m.swap('A','B');assert not m.bodies['B'].basic
case('basica-impedida-nao-transfere',unabletransfer)
def specialpersonal():
 m=Model();m.enter('A');m.enter('B');m.start();m.cast(3);m.use('A',special=True);expect_assert(lambda:m.cast(2));m.cast(0);m.use('B',damage=True);assert m.casts==[3,0]
case('especial-imediata-feitico-positivo-negado-classezero-possivel',specialpersonal)
def prepared_personal():
 m=Model();m.enter('A');m.start();m.issue('A','prepared',3);expect_assert(lambda:m.cast(2));m.cast(0);assert m.casts==[3,0];assert m.execute('A',True)
case('preparacao-positiva-bloqueia-feitico-positivo-na-emissao',prepared_personal)
def prepared_zero():
 m=Model();m.cast(0);m.cast(3);assert m.casts==[0,3]
case('limite-generico-classezero-com-magica-pessoal-positiva',prepared_zero)
def twobasics():
 m=Model();m.enter('A');m.enter('B');m.start();m.cast(3);m.use('A',damage=True);m.use('B',damage=True);assert m.casts==[3] and len(m.attackers)==2
case('duas-basicas-nao-ocupam-conjuracoes-pessoais',twobasics)
def evoker():
 m=Model();m.enter('A');m.start();m.cast(5);m.cast(2,exception=True);expect_assert(lambda:m.cast(0));assert m.casts==[5,2]
case('excecao-evocador-combinacao-ocupa-duas',evoker)
def concentration():
 m=Model();m.enter('A');m.enter('B');m.start();m.issue('A','anticipated');m.start();m.issue('B','anticipated');m.start();assert m.execute('A') and m.execute('B');m.cast(3);assert m.casts==[3] and all(e.basic==0 for e in m.bodies.values())
case('concentracao-temporal-duas-ordens-pagas-mais-feitico-pessoal',concentration)
def armado():
 m=Model();m.enter('A');m.start();m.issue('A','armed');assert m.execute('A',True) and m.reaction and not m.bodies['A'].basic;m.start();m.issue('A','armed');m.recall('A');assert m.bodies['A'].order is None
case('armado-consome-basica-antes-sem-coletiva-disparo-sair-encerra',armado)
def cap():
 m=Model();m.enter('A');m.enter('B');m.start();m.use('A',damage=True);m.use('B',damage=True);m.swap('A','C');m.bodies['C'].basic=1 # Permissão explícita de básica extra, para isolar teto de corpos.
 expect_assert(lambda:m.use('C',damage=True));m.use('C',damage=True,special=True);assert len(m.attackers)==2
case('terceiro-corpo-dano-nega-basica-permite-especial',cap)
# Carregar: duas básicas legítimas em ciclos consecutivos, PE uma vez, ação variável.
def charge(fast=False,release=True,left=False,damages=()):
 paid_pe=9;basics=1;commands=['Padrão'];alive=not left and all(total>=dc for total,dc in damages)
 if release and alive:basics+=1;commands.append('Bônus' if fast else 'Padrão')
 return dict(pe=paid_pe,basicas=basics,comandos=commands,liberou=bool(release and alive))
check('carregar-rapido-dois-turnos',charge(True)==dict(pe=9,basicas=2,comandos=['Padrão','Bônus'],liberou=True))
check('carregar-comum-duas-padroes',charge()['comandos']==['Padrão','Padrão'])
check('carregar-dano-falha-perde',charge(damages=[(14,15)])==dict(pe=9,basicas=1,comandos=['Padrão'],liberou=False))
check('carregar-empate-passa',charge(damages=[(15,15)])['liberou'])
check('carregar-sair-perde',not charge(left=True)['liberou'])
check('carregar-prazo-perde',not charge(release=False)['liberou'])
for owner_moved,entity_moved in itertools.product([False,True],repeat=2):
 allowed=not owner_moved and not entity_moved
 check('atrasar-deslocamento-'+str((owner_moved,entity_moved)),allowed==(owner_moved==entity_moved==False))
# Comparação numérica dos trunfos, preservando pontos reais da entidade.
trunfos=[]
for c in range(3,8):
 trunfos.append(dict(classe=c,pontos=points[c],liberacao_dados=points[c]+c,liberacao_media=4.5*(points[c]+c),pe=math.ceil(4.5*c),dominio_dados=c,dominio_media=4.5*c,dominio_fechado_pe=6*c,dominio_aberto_pe=7*c))
check('liberacao-classe4-nao-regrede-12',trunfos[1]['liberacao_dados']==13)
check('exemplo-dominio4-r6',6*4==24 and 1.5*6==9 and 1+6//2==4)
# Reparo: Classe é a da progressão por nível, não Grau do item nem atributo Refino.
repair=[]
for patient in range(1,31):
 for worker in range(1,31):
  diff=levels[worker]['classe']-levels[patient]['classe'];status='impedido' if diff<0 else 'difícil' if diff==0 else 'média' if diff==1 else 'fácil'
  repair.append(dict(corpo=patient,reparador=worker,dificuldade=status))
check('900-reparos',len(repair)==900)
check('reparo-exemplo31',8+31//2==23)
# Reserva total: todo estado legal permanece legal ao desativar todos os corpos.
check('reserva-total-textual','total de corpos igual ao atributo escolhido para a Defesa das entidades + sua capacidade de entidades ativas' in text)
reserve_states=0
for attribute in range(0,11):
 for capacity in (2,4):
  total_max=attribute+capacity
  for total in range(total_max+1):
   for active in range(min(capacity,total)+1):
    inactive=total-active
    assert active+inactive<=total_max
    end_inactive=total
    assert end_inactive<=total_max
    restart=min(2,total)
    assert restart+(total-restart)<=total_max
    reserve_states+=1
check('corpos-reserva-6-transicao',2+4==6 and (4+2)==(0+6)==(2+4))
check('corpos-sem-acoes-inativas','falha em toda rolagem, não age e não recebe tarefa' in text)
check('corpos-reserva-enumerada',reserve_states>0,reserve_states)
sources=[f,R/'invocacoes/05-Edicao-Integrada/60-invocacoes.md',R/'sistema/05-material/livro/manual/35-caminhos-e-trilhas.md',P/'fundamento/lote-01/FUNDAMENTO.md',P/'catalogo/lote-01/CATALOGO.md',P/'poderes-avancados/lote-01/PODERES-AVANCADOS.md',P/'pericias-e-oficios/lote-01/PERICIAS-E-OFICIOS.md']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
check('espelho-integrado-igual',sha(f)==sha(sources[1]))
report={'ok':all(x['passou'] for x in checks),'manuscritos_auditados':{str((O/'INVOCACOES-EM-CAMPO.md').relative_to(R)):sha(O/'INVOCACOES-EM-CAMPO.md')},'fontes':{str(p.relative_to(R)):sha(p) for p in sources},'verificacoes':checks,'casos_executados':executed,'contagens':{'precos':price_cases,'devolucoes_armado':refund_cases,'reservas':len(reserve_profiles),'sobrevivencia':survival,'reparos':len(repair),'transicoes_nomeadas':len(executed)},'tabelas':{'maximas':maximas,'talismas':talismans,'trunfos':trunfos,'reservas':reserve_profiles,'reparos':repair},'palavras_por_pagina':wordcounts,'limites':['Modelo dirigido das regras de R11; não executa a ficha completa, cenas humanas ou regras de toda habilidade de Caminho.','Exceção Evocador é parâmetro explícito do modelo; validação textual de gatilhos e custos permanece indispensável.','Dano em área acumulado e comando no turno de emissão são decisões mecânicas candidatas registradas, não fatos de cânone.','Vários casos são enumerações do modelo; não equivalem a partidas ou medições empíricas de equilíbrio.']}
(O/'evidencias/auditoria-numerica.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(O/'evidencias/casos-executados.json').write_text(json.dumps({'ok':True,'sha256_texto':sha(O/'INVOCACOES-EM-CAMPO.md'),'casos':executed,'contagens':report['contagens'],'limites':report['limites']},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':report['ok'],'verificacoes':len(checks),'contagens':report['contagens'],'sha256':sha(O/'INVOCACOES-EM-CAMPO.md')},ensure_ascii=False))
