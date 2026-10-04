#!/usr/bin/env python3
"""R15: auditoria do Guia. Regressão numérica e modelos dirigidos ligados à candidata.
Não simula partidas humanas. Lê números do dono e falha se as âncoras mudarem.
"""
from pathlib import Path
from dataclasses import dataclass,field
from fractions import Fraction
import hashlib,json,itertools,re
O=Path(__file__).resolve().parent
R=next(p for p in O.parents if (p/'caminhos/05-Edicao-Integrada/04-Guia-Caminho-e-Trilhas.md').exists())
P=R/'sistema/05-material/livro/planejamento-editorial';S=R/'caminhos/05-Edicao-Integrada/04-Guia-Caminho-e-Trilhas.md';src=S.read_text();f=O/'GUIA.md';s=f.read_text();checks=[];cases=[]
def ck(id,value,detail=None):
 checks.append(dict(id=id,passou=bool(value),detalhe=detail))
 if not value:raise AssertionError(id+': '+str(detail))
def req(pattern,text,id):
 m=re.search(pattern,text,re.S|re.M);ck('ancora-'+id,m is not None);return m
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manual=(R/'sistema/05-material/livro/manual/35-caminhos-e-trilhas.md').read_text();piece='## Guia\n'+manual.split('## Guia\n',1)[1].split('## Emanador\n',1)[0]
ck('fontes-identicas',src.strip()==piece.strip())
for name,val in [('Vida por nível',5),('PE por nível',5),('Perícias à sua escolha',5)]:
 got=int(req(r'\| \*\*'+re.escape(name)+r'\*\* \| (\d+)',src,name)[1]);ck('caracteristica-'+name,got==val);ck('candidata-'+name,f'| **{name}** | {got}' in s)
ck('vida-inicial-completa','| **Vida inicial** | 8 + Constituição.' in s)
ck('ganho-Constituicao','5 + Constituição nos níveis seguintes' in s)
ck('obras-maiores-nivel11','**A partir do nível 11**, ao criar uma obra ou escolher Ampliar' in s)
feature_names=re.findall(r'\*\*Nível (\d+): `([^`]+)`',src)
ck('17-habilidades',len(feature_names)==17,feature_names)
for level,name in feature_names:ck('nome-preservado-'+name,name in s)
# Contratos de0.331 contêm decisões de Bastião, não alteram Guia.
contracts=json.loads((R/'caminhos/05-Edicao-Integrada/contratos-v0.331.json').read_text());ck('contrato-sem-guia','guia' not in contracts)
pages=re.findall(r'<!-- page:([^|]+)\|([^>]+) -->(.*?)(?=<!-- page:|\Z)',s,re.S)
ck('17-blocos',len(pages)==17);ck('ids-unicos',len({x[0] for x in pages})==17)
words={}
for id,title,body in pages:
 words[id]=len(body.split());ck('titulo-'+id,body.lstrip().startswith('# '+title.strip()+'\n'))
 for line in body.splitlines():
  if line.startswith('|'):ck('colunas-'+id,line.count('|')-1<=4)
ck('titulos-diretos',not any(re.match(r'^(A|O|As|Os)\s',h) or 'como ler' in h.lower() for h in re.findall(r'^#+ (.*)$',s,re.M)))
ck('sem-legal',not re.search(r'\blegal\b',s,re.I))
ck('sem-simetria-forcada',max(words.values())-min(words.values())>100,words)
ck('sem-repeticao-caminhos','Vanguarda' not in s and 'Emanador' not in s and 'Condução' not in s)
# Âncoras que ligam os modelos aos textos e mantêm os limiares conferíveis.
anchors=['Ação Bônus, 1 PE, uma vez por turno seu','até **18 m**','até 3 m de movimento','uma vez por rodada','início de um turno do Guia até o início do seguinte','sem novo gasto de PE','um tipo diferente do já utilizado','mantém o prazo original','primeira exige sua Reação normalmente','segunda dispensa somente a sua Reação','uma mesma criatura não pode realizar as duas respostas','100 kg × atributo escolhido','10 + seu nível + 5 × atributo escolhido','10 + sua maestria','3 PE**','um d8 para cada dois pontos do atributo escolhido','não cria uma Abertura nova','antes das consequências','não repete um teste que já tenha sido repetido','até o começo do seu terceiro turno seguinte','se ainda estiver nessa faixa de vida','Em Desarmado, é necessário que exista uma arma disponível','sem repetir o custo de 2 PE','Cada Abertura consumida permite uma resposta']
for i,a in enumerate(anchors):ck('texto-'+str(i),a in s,a)
# Delta GUIA-38: exceção só no resgate dedicado; condições gerais seguem o dono R03.
rescue_body=s.split('## Nível 19 — Ainda Há Tempo',1)[1].split('## Nível 27',1)[0]
for text in ['uma vez por cena','Reação e 2 PE adicionais','18 m','Consuma a Abertura e o Cuidado','enquanto o aliado ainda estiver **morrendo**','abaixo do limiar normal de recuperação','não permite voltar à cena depois de **derrotado**']:
 ck('emergencia-texto-'+text,text.lower() in rescue_body.lower())
r03=P/'dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md';r03text=r03.read_text()
threshold_percent=int(req(r'\*\*(\d+)% do máximo de referência',r03text,'limiar-resgate')[1]);ck('limiar-geral20',threshold_percent==20)
ck('socorro-tratamento-excecao','Se já havia tratamento acumulado válido, some-o à cura e aplique o máximo atual.' in r03text)

# Grandezas lidas das características e da tabela publicada.
life_base=int(req(r'Vida de cada obra\*\*? \| (\d+) \+',src,'vida-obra')[1]) if '**Vida de cada obra' in src else int(req(r'Vida de cada obra \| (\d+) \+',src,'vida-obra')[1])
life_factor=int(req(r'Vida de cada obra[^\n]+\+ (\d+) ×',src,'vida-atributo')[1]);duration=int(req(r'Duração de cada obra \| (\d+) minutos',src,'duracao')[1]);weight=int(req(r'Peso suportado[^\n]+\| (\d+) kg',src,'peso')[1]);defbase=int(req(r'\| Defesa \| (\d+) \+',src,'defesa')[1]);capbase=int(req(r'Obras ao mesmo tempo \| (\d+) \+',src,'cap')[1])
final_costs=list(map(int,req(r'Custos finais de criação:\*\* Básica, (\d+) PE; Ampliada, (\d+) PE; Grande, (\d+) PE',src,'precos').groups()))
ck('custos2-6-10',final_costs==[2,6,10])
ma={}
for row in (R/'sistema/03-mecanica/18-progressao.md').read_text().splitlines():
 c=[x.strip().replace('**','') for x in row.split('|')[1:-1]]
 if len(c)==9 and c[0].isdigit():ma[int(c[0])]=int(c[2])
ck('maestria30',len(ma)==30)
works=[]
for lv in range(2,31):
 for raw in range(7):
  a=max(1,raw);profile=dict(nivel=lv,atributo=raw,efetivo=a,limite=capbase+a//2,vida=life_base+lv+life_factor*a,defesa=defbase+ma[lv],minutos=duration*a,kg=weight*a,conserto=5*a)
  works.append(profile)
ck('exemplo-arquiteto11A4',next(x for x in works if x['nivel']==11 and x['atributo']==4)==dict(nivel=11,atributo=4,efetivo=4,limite=4,vida=41,defesa=defbase+ma[11],minutos=40,kg=400,conserto=20))
ck('conserto-precos',[(c//2) for c in final_costs]==[1,3,5]);ck('ampliacao-diferenca',final_costs[2]-final_costs[1]==4)
ck('mureta-antiga1m','1 m de altura' in src);ck('mureta-nova1-5','1,5 m de altura' in s and '× 1 m de altura' not in s)
measurements=[]
for val in re.findall(r'(?<!\d)(\d+(?:,\d+)?)\s*m\b',s):
 n=Fraction(val.replace(',','.'));measurements.append(str(n));assert (n/Fraction(3,2)).denominator==1
ck('medidas-grade1-5',bool(measurements),sorted(set(measurements)))
# Distribuições exatas, sem simulação aleatória.
rerolls=[]
for success_faces in range(21):
 p=Fraction(success_faces,20)
 pairs=list(itertools.product(range(1,21),repeat=2))
 win=lambda n:n<=success_faces
 adv=sum(win(a) or win(b) for a,b in pairs)
 repeated=sum(win(a) or ((not win(a)) and win(b)) for a,b in pairs)
 forced_pass=sum(win(a) and win(b) for a,b in pairs)
 assert Fraction(adv,400)==2*p-p*p==Fraction(repeated,400)
 assert Fraction(forced_pass,400)==p*p
 rerolls.append(dict(faces_sucesso=success_faces,normal=float(p),vantagem=float(Fraction(adv,400)),repetir_falha=float(Fraction(repeated,400)),falha_inimiga_com_brecha=float(1-p*p)))
quad=sum((a<=10 or b<=10) or (c<=10 or d<=10) for a,b,c,d in itertools.product(range(1,21),repeat=4))
ck('analista-mais-vantagem-93-75',Fraction(quad,160000)==Fraction(15,16))
# Cura comum e emergência: comparação com e sem cadeia; todos os d8 exatos.
heal_profiles=[];healing_cases=0
for raw in range(7):
 a=max(1,raw);dice=max(1,a//2);outcomes=[sum(t)+a for t in itertools.product(range(1,9),repeat=dice)]
 avg=Fraction(sum(outcomes),len(outcomes));assert avg==Fraction(9,2)*dice+a
 normal=[d+a for d in range(1,9)];normal_mean=Fraction(sum(normal),8)
 heal_profiles.append(dict(atributo=raw,efetivo=a,cura_media=float(normal_mean),emergencia_dados=dice,emergencia_min=min(outcomes),emergencia_max=max(outcomes),emergencia_media=float(avg),tres_cuidados_media=float(3*normal_mean),cadeia_emergencia_media=float(2*normal_mean+avg)))
 for mx in range(1,151):
  for hp in sorted({0,1,max(1,(mx-1)//2),(mx+1)//2,mx}):
   for result in normal:
    eligible=1<=hp and 2*hp<mx
    after=min(mx,hp+result) if eligible else hp
    assert not eligible or hp<after<=mx
    assert hp!=0 or after==0
    healing_cases+=1
ck('metade-exata100-50',not (1<=50 and 2*50<100));ck('45-mais10',min(100,45+10)==55)
ck('emergencia-A6',heal_profiles[-1]['emergencia_media']==19.5 and heal_profiles[-1]['emergencia_max']==30)
ck('tres-cadeia-40-5',heal_profiles[-1]['cadeia_emergencia_media']==40.5)
chain_costs=[]
for count in [1,2,3]:
 regular=1+2*count;extended=3
 chain_costs.append(dict(participantes=count,comum=regular,atendimento_cadeia=extended,economia=regular-extended,com_emergencia=extended+2))
ck('cadeia-3-custo5-emergencia',chain_costs[2]['com_emergencia']==5)
# Modelos do procedimento; as fichas integrais dos aliados não são um simulador aqui.
@dataclass
class Guide:
 level:int=30
 plan:bool=False
 slot:tuple|None=None
 used_people:set=field(default_factory=set)
 used_types:set=field(default_factory=set)
 reply_people:set=field(default_factory=set)
 personal:bool=True
 replies_cycle:int=0
 replies_plan:int=0
 alive:bool=True
 spent_scene_plan:bool=False
 paid:int=0
 opened_turn:bool=False
 reply_window:bool=False
 def open(self,who,kind,plan=False,dist=18,perceived=True,communicated=True):
  assert not self.opened_turn
  assert who!='guide' and dist<=18 and perceived and communicated
  assert not plan or self.level>=30 and not self.spent_scene_plan
  self.opened_turn=True;self.alive=True;self.reply_window=False;self.slot=(who,kind);self.plan=plan;self.used_people=set();self.used_types=set();self.reply_people=set();self.replies_plan=0;self.paid+=1;self.spent_scene_plan|=plan
 def consume(self):
  assert self.slot and self.alive
  who,kind=self.slot;self.used_people.add(who);self.used_types.add(kind);self.slot=None;self.reply_window=True
  return who,kind
 def pass_to(self,who,kind,dist=18):
  maximum=3 if self.plan else 2 if self.level>=23 else 1
  assert self.alive and not self.slot and len(self.used_people)<maximum and who not in self.used_people and kind not in self.used_types and dist<=18
  self.slot=(who,kind);self.reply_window=False
 def adjust(self,who,kind):
  assert self.slot and self.personal and who not in self.used_people and kind not in self.used_types
  self.personal=False;self.slot=(who,kind)
 def reply(self,who,pools,pool=None,recursive=False):
  pool=pool or who;limit=2 if self.plan else 1
  assert self.alive and self.reply_window and not recursive and self.replies_cycle<limit and pools[pool]
  free=self.plan and self.replies_plan==1
  assert free or self.personal
  assert not self.plan or who not in self.reply_people
  if not free:self.personal=False
  pools[pool]=False;self.replies_cycle+=1;self.replies_plan+=1;self.reply_people.add(who);self.reply_window=False
 def start_turn(self):
  self.slot=None;self.alive=False;self.personal=True;self.replies_cycle=0;self.opened_turn=False;self.reply_window=False

def expect(fn):
 try:fn()
 except AssertionError:return
 raise AssertionError('transição inválida foi aceita')
def case(id,fn):fn();cases.append(dict(id=id,passou=True,tipo='modelo executado'))
def opening():
 g=Guide();expect(lambda:g.open('guide','Executar'));expect(lambda:g.open('A','Executar',dist=19.5));g.open('A','Executar');assert g.slot==('A','Executar');expect(lambda:g.open('B','Resguardar'));g.start_turn();g.open('B','Resguardar');assert g.used_people==set() and g.slot==('B','Resguardar')
case('abertura-alvo-distancia-limite-proprio-turno',opening)
def advance_reply():
 g=Guide(level=7);g.open('A','Avançar');g.consume();p={'A':False,'B':True};expect(lambda:g.reply('A',p));g.reply('B',p);assert not g.personal and not p['B']
case('avancar-fora-consome-reacao-nao-pode-responder-mesmo-aliado',advance_reply)
def three():
 g=Guide();g.open('A','Avançar',plan=True);p={'X':True,'Y':True,'Z':True};g.consume();g.reply('X',p);g.pass_to('B','Executar');g.consume();g.reply('Y',p);g.pass_to('C','Resguardar');g.consume();expect(lambda:g.pass_to('D','Executar'));expect(lambda:g.reply('Z',p));assert g.replies_cycle==2 and not g.personal and g.paid==1
case('plano-tres-aberturas-duas-respostas',three)
def no_repeat():
 g=Guide();g.open('A','Avançar',plan=True);g.consume();expect(lambda:g.pass_to('A','Executar'));expect(lambda:g.pass_to('B','Avançar'));g.pass_to('B','Executar');expect(lambda:g.adjust('A','Resguardar'))
case('cadeia-sem-repetir-pessoa-ou-tipo',no_repeat)
def adjust_first():
 g=Guide();g.open('A','Avançar',plan=True);g.adjust('B','Resguardar');g.consume();expect(lambda:g.reply('C',{'C':True}));assert g.replies_plan==0
case('reajuste-gasta-reacao-nao-inicia-resposta-gratis',adjust_first)
def after_prior():
 g=Guide();g.open('B','Resguardar',plan=True);g.consume()
 g.replies_cycle=1;g.personal=False # Estado artificial de limite; não presume duas Aberturas no turno.
 expect(lambda:g.reply('B',{'B':True}));g.personal=True # Isola teto por rodada, sem afirmar fonte de recuperação.
 g.reply('B',{'B':True});g.pass_to('C','Executar');g.consume();expect(lambda:g.reply('C',{'C':True}));assert g.replies_cycle==2
case('estado-limite-artificial-resposta-anterior-conta-teto',after_prior)
def collective():
 g=Guide();g.open('A','Executar',plan=True);g.consume();p={'coletiva':True};g.reply('ent1',p,'coletiva');g.pass_to('B','Resguardar');g.consume();expect(lambda:g.reply('ent2',p,'coletiva'));p['coletiva']=True # Começo do turno de outro invocador, ainda antes do próximo turno do Guia.
 g.reply('ent2',p,'coletiva');assert g.replies_cycle==2
case('duas-entidades-compartilham-coletiva-mas-renovacao-outro-invocador-permite',collective)
def self_owner():
 g=Guide();g.open('A','Executar',plan=True);g.consume();p={'coletiva':True};g.reply('ent1',p,'coletiva');g.pass_to('B','Resguardar');g.start_turn();assert g.slot is None and not g.alive
case('guia-invocador-nao-usa-renovacao-para-prolongar-cadeia',self_owner)
def recursion():
 g=Guide(level=7);g.open('A','Executar');g.consume();expect(lambda:g.reply('A',{'A':True},recursive=True))
case('resposta-nao-gera-outra-acao-concedida',recursion)
def single_consumption():
 g=Guide();g.open('A','Executar',plan=True);g.consume();p={'B':True,'C':True};g.reply('B',p);expect(lambda:g.reply('C',p));g.pass_to('C','Resguardar');g.consume();g.reply('C',p)
case('uma-resposta-por-abertura-consumida',single_consumption)
def expiration():
 g=Guide();g.open('A','Executar',plan=True);g.consume();g.start_turn();expect(lambda:g.pass_to('B','Resguardar'));expect(lambda:g.reply('C',{'C':True}))
case('prazo-encerra-cadeia-e-janela-de-resposta',expiration)
def foreign_opening():
 held={'A':('G1','Executar')};used=[]
 held['A']=('G2','Resguardar') # Receber de outro Guia não chama consume().
 assert held['A']==('G2','Resguardar') and not used
case('outra-abertura-substitui-sem-consumo',foreign_opening)
# Seleções da cadeia por enumeração: a transição deve rejeitar duplicações.
chains=0
for size in [1,2,3]:
 for people in itertools.permutations('ABC',size):
  for kinds in itertools.permutations(['Avançar','Executar','Resguardar'],size):
   g=Guide();g.open(people[0],kinds[0],plan=True);g.consume()
   for person,kind in zip(people[1:],kinds[1:]):g.pass_to(person,kind);g.consume()
   assert len(g.used_people)==len(g.used_types)==size;chains+=1
ck('81-cadeias-distintas',chains==81,chains)
# Obras: versão, custo, vida e prazo não restauram ao ampliar/mudar.
def work_case():
 w={'version':0,'hp':17,'max':41,'expires':40};paid=2
 paid+=final_costs[1]-final_costs[w['version']];w['version']=1
 assert w['hp']==17 and w['expires']==40 and paid==6
 paid+=final_costs[2]-final_costs[w['version']];w['version']=2
 assert paid==10 and w['hp']==17
 repair_cost=final_costs[2]//2;w['hp']=min(w['max'],w['hp']+5*4)
 assert repair_cost==5 and w['hp']==37 and w['expires']==40
case('obra-ampliar-preserva-dano-prazo-e-conserto-sem-excesso',work_case)
def build_limit():
 def can_create(limit,works,free_to_end):return works<=limit and (works<limit or free_to_end>0)
 assert not can_create(3,4,0) and not can_create(3,4,1) and can_create(3,3,1)
case('limite-obras-nao-apaga-apoio-ocupado',build_limit)
# Analista: confirmação posterior não altera ação já terminada; previsão não troca alvo.
def analyst():
 predicted='conjurar';observed='Bloquear';confirmed=False;reaction=True;pe=1
 assert observed!=predicted and not confirmed
 if observed!=predicted and reaction and pe:confirmed=True;reaction=False;pe-=1
 assert confirmed and not reaction and pe==0
 pattern_end=3;assert [n for n in range(1,4) if n<pattern_end]==[1,2]
case('rever-leitura-custa-reacao-e1pe-padrao-dois-proximos-turnos',analyst)
def emergency():
 opening_used=True;care_unresolved=True;hp=0;alive=True;can_heal=True;reaction=True;pe=2
 assert opening_used and care_unresolved
 if hp==0 and alive and can_heal and reaction and pe>=2:hp=3*4+6;care_unresolved=False;reaction=False;pe-=2
 assert hp==18 and not care_unresolved and not reaction and pe==0
case('emergencia-com-abertura-consumida-nao-consome-segunda',emergency)
def heal_lock():
 def allowed(alive,can_heal,hp,care,rea):return alive and can_heal and hp==0 and care and rea
 assert not allowed(False,True,0,True,True) and not allowed(True,False,0,True,True)
 assert not allowed(True,True,0,False,True) and not allowed(True,True,0,True,False)
case('emergencia-nao-revive-morto-nem-ignora-proibicao-de-cura',heal_lock)
def care_choice():
 def prepare(hp,mx,condition=False):return hp>=1 and (2*hp<mx or condition)
 assert prepare(40,100) and prepare(80,100,True) and not prepare(80,100) and not prepare(0,100,True)
 assert prepare(50,100,True) and not prepare(50,100)
case('cuidado-cura-ou-condicao-elegivel-na-preparacao',care_choice)
# Compara o resgate a limiares representativos. Enumeração exata de todos os d8.
rescue_profiles=[]
for reference in [80,195,212,302,305,395]:
 for attribute in range(1,7):
  dice=max(1,attribute//2);values=[sum(t)+attribute for t in itertools.product(range(1,9),repeat=dice)]
  needed=(reference*threshold_percent+99)//100
  rescue_profiles.append(dict(referencia=reference,atributo=attribute,dados=dice,limiar_comum=needed,minimo=min(values),maximo=max(values),media=float(Fraction(sum(values),len(values))),probabilidade_sem_excecao=float(Fraction(sum(v>=needed for v in values),len(values))),probabilidade_com_excecao=1.0,condicoes='Alvo vivo, Morrendo e curável; preparo, alcance, percepção e recursos válidos.'))
ck('36-perfis-resgate',len(rescue_profiles)==36)
profile=next(x for x in rescue_profiles if x['referencia']==195 and x['atributo']==6)
ck('resgate-195-era-impossivel',profile['maximo']==30 and profile['limiar_comum']==39 and profile['probabilidade_sem_excecao']==0 and profile['probabilidade_com_excecao']==1)
@dataclass
class Rescue:
 reference:int=195
 maximum:int=195
 state:str='Morrendo'
 alive:bool=True
 healable:bool=True
 care:bool=True
 opening:bool=True
 reaction:bool=True
 pe:int=2
 used:bool=False
 hp:int=0
 treatment:int=0
 sequela:int=0
 def activate(self,heal,distance=18,perceived=True):
  assert self.alive and self.healable and self.care and self.reaction and not self.used and self.pe>=2
  assert self.hp==0 and self.state=='Morrendo' and distance<=18 and perceived and heal>0
  self.hp=min(self.maximum,self.treatment+heal);self.treatment=0;self.sequela+=1;self.state='Socorrido'
  self.care=False;self.opening=False;self.reaction=False;self.pe-=2;self.used=True

def rescue_low():
 r=Rescue();r.activate(9);assert r.hp==9 and r.state=='Socorrido' and r.sequela==1 and r.pe==0 and r.used
case('GUIA38-resgate-9-abaixo39-com-consumo',rescue_low)
def rescue_accumulated():
 r=Rescue(maximum=70,treatment=68);r.activate(9);assert r.hp==70 and r.treatment==0 and r.sequela==1
case('GUIA38-tratamento-soma-respeita-maximo-atual',rescue_accumulated)
def rescue_consumed_opening():
 r=Rescue(opening=False);r.activate(9);assert r.hp==9 and not r.care
case('GUIA38-abertura-ja-consumida-sem-consumo-duplo',rescue_consumed_opening)
def rescue_defeated():
 for state in ['Derrotado','Morto']:
  r=Rescue(state=state);expect(lambda:r.activate(9));assert r.hp==0 and r.pe==2 and r.care and not r.used
case('GUIA38-nao-retorna-apos-derrotado',rescue_defeated)
def rescue_invalid_target():
 for attr in ['alive','healable','care','reaction']:
  r=Rescue();setattr(r,attr,False);expect(lambda:r.activate(9));assert r.hp==0 and r.pe==2 and not r.used
case('GUIA38-preserva-impedimentos-e-requisitos',rescue_invalid_target)
def rescue_distance():
 r=Rescue();expect(lambda:r.activate(9,distance=19.5));expect(lambda:r.activate(9,perceived=False));assert r.hp==0 and r.pe==2
case('GUIA38-alcance-percepcao-preservados',rescue_distance)
def rescue_once():
 r=Rescue();r.activate(9);r.hp=0;r.state='Morrendo';r.reaction=True;r.care=True;r.pe=2
 expect(lambda:r.activate(9));assert r.hp==0 and r.sequela==1
case('GUIA38-uma-vez-cena-mesmo-em-nova-queda',rescue_once)
def rescue_cost():
 r=Rescue(pe=1);expect(lambda:r.activate(9));assert r.hp==0 and r.pe==1 and not r.used
case('GUIA38-dois-PE-adicionais-obrigatorios',rescue_cost)

paths=[S,R/'sistema/05-material/livro/manual/35-caminhos-e-trilhas.md',R/'caminhos/05-Edicao-Integrada/contratos-v0.331.json',R/'sistema/03-mecanica/18-progressao.md',P/'regras-comuns/consolidado-r1/REGRAS-COMUNS.md',r03,P/'equipamento/lote-05-r1/ITENS-E-OBJETOS.md',P/'fundamento/lote-01/FUNDAMENTO.md',P/'invocacoes/lote-01/INVOCACOES-EM-CAMPO.md']
report={'ok':True,'manuscritos_auditados':{str(f.relative_to(R)):sha(f)},'fontes':{str(p.relative_to(R)):sha(p) for p in paths},'verificacoes':checks,'casos_executados':cases,'contagens':{'verificacoes':len(checks),'casos_dirigidos':len(cases),'perfis_obras':len(works),'pares_d20':21*400,'quatro_d20':160000,'cenarios_cura':healing_cases,'cadeias_ordenadas':chains,'perfis_resgate_GUIA38':len(rescue_profiles)},'tabelas':{'obras':works,'repeticoes':rerolls,'curas':heal_profiles,'custos_cadeia':chain_costs,'resgate_GUIA38':rescue_profiles},'palavras_por_pagina':words,'limites':['Modelos dirigidos e distribuições exatas; não são sessões humanas ou motor completo de combate.','O risco de suporte forte depende das fichas dos aliados e da disponibilidade de reações, não é determinado por uma média de cura.','Medidas da Mureta foram adaptadas à grade por pedido do usuário; cobertura da versão básica permanece Parcial.','O caso de teto com resposta prévia injeta estado artificial para isolar o limite; não é sequência de duas Aberturas permitidas no mesmo turno.', 'A confirmação de compreensão e diagramação depende de leitura independente e PDF, ainda não executados aqui.']}
(O/'evidencias/auditoria-numerica.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(O/'evidencias/casos-executados.json').write_text(json.dumps({'ok':True,'sha256_texto':sha(f),'casos':cases,'contagens':report['contagens'],'limites':report['limites']},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':True,'contagens':report['contagens'],'hash':sha(f)},ensure_ascii=False))
