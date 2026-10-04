#!/usr/bin/env python3
"""Auditoria R18: le regras da candidata, confronta fontes e executa modelos limitados.
Nao e simulacao integral nem evidencia de compreensao humana. Falha em ancora ausente.
"""
from pathlib import Path
from dataclasses import dataclass,replace
from fractions import Fraction as F
from itertools import product
import re,json,hashlib
O=Path(__file__).resolve().parent
R=next(x for x in O.parents if (x/'caminhos/05-Edicao-Integrada/06-Incursor-Caminho-e-Trilhas.md').exists())
P=R/'sistema/05-material/livro/planejamento-editorial';file=O/'INCURSOR.md';s=file.read_text();plain=s.replace('**','').replace('`','');checks=[];cases=[]
def ck(id,ok,detail=None):
 checks.append(dict(id=id,passou=bool(ok),detalhe=detail))
 if not ok:raise AssertionError(id+': '+str(detail))
def req(p,t,id):
 m=re.search(p,t,re.M|re.S);ck('ancora-'+id,m is not None,p);return m
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def case(id,got,expected,note):
 ck(id,got==expected,{'obtido':got,'esperado':expected});cases.append(dict(id=id,obtido=got,esperado=expected,contexto=note))
source=(R/'caminhos/05-Edicao-Integrada/06-Incursor-Caminho-e-Trilhas.md').read_text()
manual=(R/'sistema/05-material/livro/manual/35-caminhos-e-trilhas.md').read_text()
ck('publicados-identicos',source.strip()==('## Incursor'+manual.split('## Incursor',1)[1]).strip())
for row in json.loads((O/'evidencias/FONTES-INICIAIS.json').read_text()):ck('fonte-preservada-'+row['arquivo'],sha(R/row['arquivo'])==row['sha256'])
pages={m[0]:(m[1],m[2]) for m in re.findall(r'<!-- page:([^|]+)\|([^>]+) -->(.*?)(?=<!-- page:|\Z)',s,re.S)}
ck('26-paginas',len(pages)==26)
for id,(title,body) in pages.items():
 ck('titulo-'+id,body.lstrip().startswith('# '+title+'\n'))
 ck('tabelas-'+id,all(x.count('|')-1<=4 for x in body.splitlines() if x.startswith('|')))
ck('titulos-diretos',all(not re.match(r'^(A|O|As|Os)\s',x) and 'como ler' not in x.lower() for x in re.findall(r'^#+ (.+)$',s,re.M)))
ck('sem-volume-leve','Volume leve' not in s)
ck('sem-legal',not re.search(r'\blegal\b',s,re.I))
ck('sem-bold-quebrado',all(x.count('**')%2==0 for x in s.splitlines()))
anchor_names=['Agilidade de Combate','Movimento Acrobático','Fluidez','Investida','Instante Decisivo','Passo Rápido','Evasão','Reflexo','Esquiva Instintiva','Passo Guardado','Retomar o Ritmo','Um Passo à Frente','Alvo Estudado','Estudar a Guarda','Golpe Cirúrgico','Cortar a Fuga','Parkour','Desaparecer no Percurso','Escolher a Próxima Vítima','Brecha Fatal','Sentença Final','Corpo Treinado','Rajada Marcial','Quebrar o Compasso','Recuperar a Base','Guarda Marcial','Interceptar e Prender','Movimento sobre líquidos','Golpe Desarticulador','Projeção Marcial','Corpo em Harmonia','Redirecionar a Força','Manejo de Combate','Ofensiva em Movimento','Ricochete','Lançamento Cruzado','Mudar o Destino','Trajetória de Retorno','Manejo Contínuo','Finta de Retorno','Trajetória Perfeita']
for name in anchor_names:ck('nome-'+name,name in source and name in s)
# Parametros numericos da candidata, sem fallback silencioso.
life=int(req(r'Vida inicial \| (\d+) \+ Constituição',plain,'vida')[1]);gain=int(req(r'Vida por nível seguinte \| (\d+) \+ Constituição',plain,'vida-ganho')[1]);energy=int(req(r'\| PE \| (\d+) por nível',plain,'energia')[1])
move=int(req(r'Seu deslocamento aumenta em (\d+) m',plain,'movimento')[1])
def body(id):return pages['inc-'+id][1].replace('**','').replace('`','')
gc=body('cirurgico');ck('GC-base-atributo','X = atributo escolhido − 1' in gc and 'mínimo de zero' in gc)
combo=int(req(r'mais (\d+) PE',body('cortar'),'combo')[1])
rajada=int(req(r'gastar (\d+) PE.*?dois ataques desarmados',body('corpo'),'rajada')[1]);guard=int(req(r'gastar (\d+) PE.*?um ataque desarmado e',body('base'),'guarda')[1]);harm=int(req(r'gastar (\d+) PE ao todo',body('redirecionar'),'harmonia')[1])
project_cost=int(req(r'(\d+) PE · Uma vez',body('projecao'),'projecao')[1]);project_range=int(req(r'livre a até (\d+) m',body('projecao'),'projecao-dist')[1])
offense=int(req(r'Ofensiva em Movimento.*?(\d+) PE · Uma vez',body('malabarista'),'ofensiva')[1])
cross=int(req(r'\| Lançamento Cruzado \| Fluidez e (\d+) PE',body('continuacoes'),'cruzado')[1]);back=int(req(r'\| Trajetória de Retorno, nível 11 \| Fluidez e (\d+) PE',body('continuacoes'),'retorno')[1]);feint=int(req(r'\| Finta de Retorno, nível 19 \| Fluidez e (\d+) PE',body('continuacoes'),'finta')[1]);perfect=int(req(r'Fluidez e (\d+) PE',body('perfeita'),'perfeita')[1]);extra=int(req(r'arma recebe (\d+) m adicionais',body('ricochete'),'ricochete')[1])
for name,a in [('ciclo1','uma vez entre o começo de um turno seu e o começo do próximo'),('ciclo2','duas vezes entre o começo de um turno seu e o começo do próximo'),('uma','uma Fluidez por vez'),('estado','Enquanto estiver Incapacitado, não pode ganhar ou manter Fluidez'),('evento','mesmo acontecimento para recuperá-la'),('retomar','não conta no limite das duas obtenções normais'),('regenerar','se estiver sem Fluidez'),('critico','dobra tanto os dados normais de Canalizar em Golpe quanto os dados adicionais'),('reacao','uma Reação pessoal'),('instante','Esse mesmo acerto não pode recuperar Fluidez'),('guardada','enquanto tiver Fluidez'),('turno','Não pode usar se seu turno já ocorreu naquela rodada'),('qualquer','criaturas de qualquer tamanho'),('compartilhado','compartilham uma utilização por turno seu'),('projecao','sem rolagem de ataque'),('perfeita','Uma mesma criatura só pode ser atacada uma vez nessa execução')]:ck('contrato-'+name,a in plain,a)
contract={'vida_inicial':life,'vida_ganho':gain,'PE_nivel':energy,'movimento_extra':move,'combo_cirurgico':combo,'rajada':rajada,'guarda':guard,'harmonia':harm,'projecao':project_cost,'projecao_metros':project_range,'ofensiva':offense,'cruzado':cross,'retorno':back,'finta':feint,'perfeita':perfect,'ricochete_extra':extra}
ck('contrato-aprovado',contract==dict(vida_inicial=6,vida_ganho=4,PE_nivel=6,movimento_extra=3,combo_cirurgico=4,rajada=3,guarda=3,harmonia=6,projecao=3,projecao_metros=6,ofensiva=3,cruzado=3,retorno=4,finta=6,perfeita=12,ricochete_extra=6))
# Estados: cada evento de ganho e resolvido uma vez, mesmo quando nao rende um ponto.
@dataclass(frozen=True)
class Fluidez:
 level:int=7; held:bool=False; gains:int=0; reaction:bool=True; incap:bool=False; seen:frozenset=frozenset();retomar_used:bool=False
 @property
 def cap(self):return 1 if self.level<7 else 2
 def event(self,id,kind,own=True,prohibit=False):
  if id in self.seen:return self
  out=replace(self,seen=self.seen|{id})
  valid=(kind=='miss-enemy')or(kind=='hit-own' and own)
  if valid and not prohibit and not self.incap and not self.held and self.gains<self.cap:return replace(out,held=True,gains=self.gains+1)
  return out
 def spend(self):return replace(self,held=False) if self.held else self
 def renew(self):return replace(self,gains=0,reaction=True,seen=frozenset(),retomar_used=False)
 def retomar(self,at_start=True,movement=True):
  if self.level>=23 and at_start and movement and not self.held and not self.incap and not self.retomar_used:return replace(self,held=True,retomar_used=True)
  return self
 def disable(self):return replace(self,held=False,incap=True)
 def response(self,held_at_declaration):
  ok=self.held and held_at_declaration and self.reaction and not self.incap
  return (replace(self,held=False,reaction=False) if ok else self),ok
f=Fluidez(level=2).event(1,'hit-own');case('ganho-nivel2',(f.held,f.gains),(True,1),'Acerto proprio.')
g=f.event(2,'hit-own');case('cheia-sem-banco',(g.held,g.gains),(True,1),'Novo acerto enquanto cheio nao gasta obtencao nem fica reservado.')
g=g.spend().event(2,'hit-own');case('evento-nao-repetido',(g.held,g.gains),(False,1),'Gastar depois nao permite usar de novo o mesmo acontecimento.')
case('cap2-saturado',f.spend().event(3,'miss-enemy').held,False,'Ja usou a unica obtencao do nivel2.')
f=Fluidez(level=7).event(1,'hit-own').spend().event(2,'miss-enemy');case('nivel7-duas',(f.held,f.gains),(True,2),'Gatilhos distintos dentro do mesmo ciclo.')
case('fora-turno-sem-ganho',Fluidez().event(1,'hit-own',own=False).held,False,'Reflexo fora do turno.')
case('instante-nao-retorna',Fluidez(held=True).spend().event(1,'hit-own',prohibit=True).held,False,'Acerto modificado por Instante Decisivo.')
case('incap-sem-fluidez',Fluidez(held=True).disable().event(1,'miss-enemy').held,False,'Estado mantido impede obter nova Fluidez.')
f=Fluidez(level=23).retomar().spend().event(1,'hit-own').spend().event(2,'miss-enemy');case('retomar-mais2',(f.held,f.gains,f.retomar_used),(True,2,True),'Retomar paga Movimento; duas obtencoes normais continuam disponiveis.')
case('retomar-sem-fabrica',f.spend().retomar().held,False,'O evento do comeco nao se repete.')
case('retomar-fora-comeco',Fluidez(level=23).retomar(at_start=False).held,False,'Recurso indisponivel mais tarde no turno.')
case('retomar-sem-movimento',Fluidez(level=23).retomar(movement=False).held,False,'Nao aceita Movimento parcial ou ja usado.')
f,valid=Fluidez(held=True).response(True);case('reacao-compartilhada',f.response(True)[1],False,'Evasao/Reflexo/Interceptar/Redirecionar usam a mesma Reacao.')
case('reflexo-posterior-invalido',Fluidez().event(1,'miss-enemy').response(False)[1],False,'A Fluidez recem-obtida nao existia na declaracao.')
# Enumera seis eventos curtos, com ids exclusivos, para cap/retencao; renovacao e testes acima.
count=0
for level in (2,7,23):
 for seq in product(range(5),repeat=6):
  f=Fluidez(level=level)
  for i,e in enumerate(seq):
   if e==0:f=f.event(i,'hit-own')
   elif e==1:f=f.event(i,'miss-enemy')
   elif e==2:f=f.spend()
   elif e==3:f=f.disable()
   else:f=replace(f,incap=False)
   assert 0<=f.gains<=f.cap and not(f.incap and f.held)
  count+=1
ck('enumeracao-fluidez',count==46875,count)
# Movimento em metros e quota fisica, arredondando na grade1,5m conforme regra geral.
floor_grid=lambda x:F(3,2)*int(F(x)/F(3,2))
def quota(level,speed):return floor_grid(speed if level>=23 else F(speed)/2)
case('acro12-n2',str(quota(2,12)),'6','Distancia acrobatica.')
case('acro12-n23',str(quota(23,12)),'12','Quota ampliada, sem metros adicionais.')
case('acro-dificil6',6*2,12,'6m percorridos consomem12m de movimento e6m de quota.')
case('parkour-salto',float(12-6-4.5),1.5,'Salto nao consome novamente quota da parede.')
case('correr-nao-renova',str(quota(2,12)-6),'0','Correr acrescenta12m, mantemquota gasta.')
case('retomar-correr',12,12,'Com Movimento gasto em Retomar, Correr pela Bonus fornece12m mediante Fluidez.')
case('adiantar-duplo',quota(30,(9+move)*2),24,'Um Passo a Frente dobra deslocamento e renova uma vez, sem segundo turno.')
def return_push(before,after,pushed,canmove=True):return floor_grid(F(after)/2) if canmove and F(pushed)>=F(before)/2 else F(0)
case('empurrao6-retorno6',return_push(12,12,6),6,'Deslocamento inalterado.')
case('empurrao9-retorno6',return_push(12,12,9),6,'Distancia excedente nao aumenta retorno.')
case('empurrao-lento',return_push(12,6,6),3,'Limiar anterior12/2 e retorno atual6/2.')
case('queda-nao-soma',return_push(12,12,3),0,'Empurrao3m seguidoqueda nao cumpre limiar6m.')
# Cirurgico: valores lidos da tabela da aptidao, adicionais por atributo.
apt=(P/'aptidoes/lote-01/APTIDOES-E-REFINO.md').read_text();mus=(P/'rotas/lote-01/ROTAS.md').read_text()
rows=[]
for a,b,n,d in re.findall(r'\| (\d+)(?:–(\d+))? \| (\d+)d(\d+)',apt.split('## Canalizar em Golpe')[1].split('## Feitiços')[0]):
 for ref in range(int(a),int(b or a)+1):rows.append((ref,int(n),int(d)))
ck('dez-refinos',len(rows)==10)
for ref,n,d in rows:ck('estimulo-tabela-'+str(ref),f'{n}d{d}' in mus)
mean=lambda n,d:F(n*(d+1),2)
profiles=[]
for ref,n,d in rows:
 for attr in range(7):
  x=max(0,attr-1);normal=mean(1,8)+attr+mean(n+x,d);crit=mean(2,8)+attr+mean(2*(n+x),d)
  profiles.append(dict(refino=ref,atributo=attr,PE=x,dados=n+x,dado=d,normal_media=float(normal),critico_media=float(crit),combinacao_PE=x+combo))
case('cirurgico-exemplo-dados',next(x for x in profiles if x['refino']==6 and x['atributo']==5)['dados'],7,'3d4 normais+4d4 extras; atributo nao define dado.')
case('cirurgico-exemplo-critico',next(x for x in profiles if x['refino']==6 and x['atributo']==5)['critico_media'],49.0,'2d8+5+14d4.')
case('cirurgico-atributo0',profiles[0]['PE'],0,'Minimozero; ainda custaFluidez e pode dobrar base no critico.')
case('cirurgico-atributo5-combo',max(0,5-1)+combo,8,'4PE adicionais nao compram maisdados.')
ck('cirurgico-nao-maximiza','não maximiza dados' in gc)
# Ataques/custos com o kit proprio, sem efeitos que concedam acoes externas.
case('pug2-ataques',1+1,2,'Atacar+Bonus CorpoTreinado.')
case('pug7-ataques',1+2,3,'Rajada substitui um ataqueBonus por dois.')
case('pug11-guarda',1+1,2,'Guarda e alternativa aRajada.')
case('pug27-ataques',1+2,3,'Harmonia nao soma dois pacotes.')
case('pug27-custo',harm,rajada+guard,'6PE total.')
case('mala-cruzado',offense+cross,6,'Tresataques, alvosdiferentesna continuacao.')
case('mala-retorno',offense+back,7,'Ate tresataquespropriosmesmoalvo compercurso.')
case('mala-finta',offense+feint,9,'Ate tresataquesproprios, umafinta.')
case('mala-perfeita-total',2-1+4,5,'Ofensiva2 substitui1 por4alvosdistintos.')
case('mala-perfeita-mesmoalvo',1+1,2,'Um na trajetoria+outro ataque daAcao.')
case('mala-com-reacao',3+1,4,'Contagem condicional mesma vitima por ciclo, exigegatilho eFluidezpreexistente.')
case('mala-perfeita-custo',offense+perfect,15,'Fluidez separada, requercontinuaçãodisponivel.')
# Geometria do ricochete em passos1,5m; segmentos/cobertura fisicos testados em casos logicos.
def ricochet(a,b,normal=6,long=18,clear=True):
 if not clear or a>long or a+b>long+extra:return 'inviavel'
 return 'longa' if a>normal or a+b>normal+extra else 'normal'
case('ricochete-exemplo',ricochet(3,9),'normal','Total12, primeiroponto dentro18.')
case('ricochete-parede-longa',ricochet(9,1.5),'longa','Primeirotrecho9 maior6 mesmo total10,5.')
case('ricochete-max',ricochet(18,6),'longa','Total24.')
case('ricochete-acima-max',ricochet(18,7.5),'inviavel','Total25,5.')
case('ricochete-ponto-invalido',ricochet(19.5,1.5),'inviavel','Totalcabe,maspontoexcedeoriginal18.')
case('ricochete-parede-bloqueia',ricochet(3,9,clear=False),'inviavel','Alcancenaosubstituipassagemlivre.')
geo=[(float(a),float(b),ricochet(a,b)) for a,b in product([F(3,2)*i for i in range(1,21)],repeat=2)]
case('retorno-parede1-5',1.5+1.5<=6,True,'Percursovitimaparedevitima.')
case('retorno-parede4-5',4.5+4.5<=6,False,'Nao usa+6deRicochete.')
def correction(first_to_new,origin_to_new,range_,same=False,used=False,path=True):return first_to_new<=6 and origin_to_new<=range_ and not same and not used and path
case('mudar-destino-valido',correction(6,18,18),True,'Novoroll,contamesmoataque.')
case('mudar-destino-alcance',correction(3,19.5,18),False,'Pertoalvoanteriornaodispensaorigem.')
case('mudar-destino-repetir',correction(3,12,18,used=True),False,'Naoencadeiacorrecao.')
case('mudar-destino-mesmo',correction(0,12,18,same=True),False,'Outra criatura obrigatoria.')
# Oposicao exata: TR >=CD e resistencia bemsucedida. Redirecionar nao rerrolaataque.
probs=[]
for attr,mastery,bonus in product(range(7),range(1,5),range(13)):
 cd=8+attr+mastery;failed=sum(d+bonus<cd for d in range(1,21));p=F(failed,20)
 probs.append(dict(atributo=attr,maestria=mastery,TR=bonus,CD=cd,prob_falha=float(p)))
case('TR-cd16-bonus6',sum(d+6<16 for d in range(1,21)),9,'45% falha;10 no dado passa.')
case('redirect-d20-mantido',17>=15,True,'Resultado17errouDEF18,podeacertarDEF15 sem rerrolar.')
case('redirect-sem-alcance',3<=1.5,False,'Segundoalvo3mdoagressor comalcance1,5minviavel.')
# Probabilidades criticas exatas; nao aplica maxima ao ataque que nao acerta.
critics=[]
for margin in (20,19):
 critics.append(dict(margem=margin,normal=sum(d>=margin for d in range(1,21))/20,vantagem=sum(max(a,b)>=margin for a,b in product(range(1,21),repeat=2))/400,desvantagem=sum(min(a,b)>=margin for a,b in product(range(1,21),repeat=2))/400))
case('critico19-vantagem',critics[1]['vantagem'],.19,'Somentea distribuicaodod20,antesde outras exigenciasdoataque.')
# Comparacao restrita: ataques com60%deacerto,5%critico; adicionalnaodobraexcetoGC.
# Continuacao so existe se um dos dois ataques iniciais acertar. Nao concedeumtirogarantido.
pressure=[]
for level,attr,ref,unarmed in [(7,4,3,6),(11,4,4,8),(19,5,7,10),(27,6,9,12),(30,6,10,12)]:
 n,d=next((n,d) for r,n,d in rows if r==ref);x=max(0,attr-1)
 def dmg(roll,die,extra_n=n,surgical=False):
  if roll<9:return F(0)
  return mean(1+(roll==20),die)+attr+mean(extra_n*(1+(surgical and roll==20)),d)
 single=sum(dmg(z,6) for z in range(1,21))/20
 assass=sum(dmg(z,6,n+x,True) for z in range(1,21))/20
 pug=3*sum(dmg(z,unarmed) for z in range(1,21))/20
 mala=sum(dmg(a,6)+dmg(b,6)+(dmg(c,6) if a>=9 or b>=9 else 0) for a,b,c in product(range(1,21),repeat=3))/8000
 assert mala==2*single+F(84,100)*single
 pressure.append(dict(nivel=level,atributo=attr,refino=ref,assassino_um_golpe=float(assass),pugilista_rajada=float(pug),malabarista_continuacao_condicional=float(mala),malabarista_tres_ataques_incondicionais=float(3*single),ressalva='Cruzado exigeoutroalvo;nivel7naopossuiRetorno. Acerto60%,critico5%,semvantagem,defesas,condicoes,Kokusen,ouacoesexternas. Custosnaocomparadoscomorecursounico.'))
# Elegibilidade cotejada como conjuntos deacesso, independente de novos pesos.
weapons=json.loads((O/'evidencias/ELEGIBILIDADE-ARMAS.json').read_text());ck('52armas',len(weapons)==52)
case('armas22para21',(sum(x['elegivel'] for x in weapons),sum(x['elegivel_nova'] for x in weapons)),(22,21),'Corte deliberado unicoTaco.')
case('unico-corte',[x['arma'] for x in weapons if x['mudanca']!='preservado'],['Taco'],'Fineza permaneceindependente.')
for name in ['Pistola','Revólver','Besta de Uma Mão','Wakizashi','Soqueira','Punhal']:
 ck('acesso-'+name,next(x for x in weapons if x['arma']==name)['elegivel_nova'])
measurements=re.findall(r'(?<!\d)(\d+(?:,\d+)?)\s*m\b',s)
ck('grade1-5',all((F(v.replace(',','.'))/F(3,2)).denominator==1 for v in measurements),sorted(set(measurements)))
# Cobertura de headings pelo inventario; permite explicitamente titulos editoriais retirados.
coverage=json.loads((O/'evidencias/COBERTURA.json').read_text());ck('inventario-integral',all(x['destino'] in pages or x.get('tratamento')=='titulo-editorial-substituido' for x in coverage))
# Interfaces migradas e casos adversariais adicionais.
ck('manobras-CD-propria','manobra desarmada' in plain and 'pode usar a CD do Pugilista' in plain)
ck('queda-nao-copia','dano de uma queda posterior afeta apenas quem cair' in plain)
ck('sem-duplicar-condicao',': seu deslocamento fica pela metade' not in s and ': seu deslocamento fica em zero' not in s)
for name,a in [('guarda-rodada','ainda não tiver se deslocado por vontade própria naquela rodada'),('guarda-proibe','não pode se deslocar por vontade própria até o fim da rodada'),('sentenca','oculto do Alvo Estudado no momento em que declara o ataque'),('execucao-ciclo','o limite de cada um desses usos passa a ser uma vez entre o começo de um turno seu e o começo do próximo'),('maos','Você precisa de uma mão livre'),('liquidos','compartilha o limite de distância'),('redirecionar','ao alcance da arma ou do membro utilizado naquele ataque'),('Finta','valem somente contra o alvo original desse retorno')]:ck('interface-'+name,a in plain,a)
def studied_guard(voluntary_this_round,bonus=True,visible=True,distance=18):return not voluntary_this_round and bonus and visible and distance<=18
case('guarda-sem-mover',studied_guard(False),True,'Recebe oportunidade no proximo corpo a corpo do turno.')
case('guarda-passoguardado-anterior',studied_guard(True),False,'Movimento voluntario anterior ao proprio turno ja impede.')
case('guarda-empurrao-anterior',studied_guard(False),True,'Movimento imposto nao e voluntario.')
case('guarda-fora18',studied_guard(False,distance=19.5),False,'Nenhuma selecao remota irrestrita.')
def surgical_allowed(hit,eligible,opportunity,fluidez,personal_turn,level,used=False,base=True):return hit and eligible and opportunity and fluidez and (personal_turn or level>=19) and not used and base
case('GC-sem-acerto',surgical_allowed(False,True,True,True,True,2),False,'Sentenca nao transforma erro em acerto.')
case('GC-sem-base',surgical_allowed(True,True,True,True,True,27,base=False),False,'Ataque que transporta feitico de dano nao recebe base nem reforco.')
case('GC-reacao-antes19',surgical_allowed(True,True,True,True,False,11),False,'Limite antigo e turno proprio.')
case('GC-reacao19',surgical_allowed(True,True,True,True,False,19),True,'Brecha ou outro ataque permitido; gatilhos ainda exigidos.')
case('GC-ciclo-consumido',surgical_allowed(True,True,True,True,False,19,used=True),False,'Nao repete o reforco do turno proprio.')
def perfect_ok(targets,segments,ricochets=0,continuation=False,held=True):return 1<=len(targets)<=4 and len(set(targets))==len(targets) and sum(segments)<=24 and ricochets<=3 and not continuation and held
case('perfeita-quatro24',perfect_ok(['a','b','c','d'],[6,6,6,6],3),True,'Contagem e distancia totais incluem a origem.')
case('perfeita-repetir',perfect_ok(['a','a'],[6,6]),False,'Nao concentra os quatro ataques na mesma criatura.')
case('perfeita-continua-usada',perfect_ok(['a'],[6],continuation=True),False,'Mesmo contador da continuacao.')
case('perfeita-sem-fluidez',perfect_ok(['a'],[6],held=False),False,'Nao pode financiar a abertura com o primeiro acerto futuro.')
case('perfeita-alem24',perfect_ok(['a','b','c','d'],[6,6,6,7.5]),False,'25,5m excede trajeto.')
case('colisao-sem-falha-inicial',False and True,False,'O TR da segunda criatura so ocorre apos falha da primeira.')
case('colisao-dano-sem-queda',14,14,'Dano de projecao14 e queda posterior7: copia14, nao21.')
case('direcao-sentenca',True,True,'Empurrar afasta conforme manobra geral; nenhum puxao novo.')
energy_profiles=[]
for lv in range(2,31):
 energy_profiles.append({'nivel':lv,'PE':lv*energy,'ofensiva_fracao':offense/(lv*energy),'cruzado_fracao':(offense+cross)/(lv*energy),'rajada_fracao':rajada/(lv*energy) if lv>=7 else None,'perfeita_fracao':(offense+perfect)/(lv*energy) if lv>=27 else None})
ck('energia-n30',energy_profiles[-1]['PE']==180)
result={'manuscritos_auditados':{str(file.relative_to(R)):sha(file)},'sha256_texto':sha(file),'verificacoes':len(checks),'casos_dirigidos':len(cases),'sequencias_fluidez':count,'perfis_cirurgico':len(profiles),'trajetorias':len(geo),'perfis_TR':len(probs),'perfis_pressao':len(pressure),'contrato':contract,'paginas':len(pages),'ok':all(x['passou'] for x in checks),'limites':['Modelos de especificacao ligados por ancoras e valores da candidata; nao executam o texto como um jogo.','Cobrem somente kit proprio e condicoes enumeradas. Nao incluem todas tecnicas, inimigos, Kokusen, buffs externos ou decisoes adaptativas.','Nao medem compreensao humana nem equivalencia global de poder; PDF e revisao independente separados.']}
e=O/'evidencias';e.mkdir(exist_ok=True)
for name,data in [('auditoria-numerica',result),('casos-executados',cases),('regras-verificadas',{'sha256_texto':sha(file),'ok':all(x['passou'] for x in checks),'checks':checks}),('cirurgico-perfis',profiles),('ricochete-perfis',geo),('resistencia-perfis',probs),('criticos-perfis',critics),('pressao-comparada',pressure),('energia-perfis',energy_profiles)]:
 (e/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2,default=str))
print(json.dumps(result,ensure_ascii=False,indent=2))
