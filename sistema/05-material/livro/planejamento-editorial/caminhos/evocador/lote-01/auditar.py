"""R17: contratos textuais, casos de recursos e modelos exatos limitados.
Não mede diversão, tempo de mesa ou compreensão de leitores reais.
"""
from pathlib import Path
from fractions import Fraction
import hashlib,json,re,itertools
B=Path(__file__).resolve().parent
R=next(p for p in B.parents if (p/'sistema').is_dir())
s=(B/'EVOCADOR.md').read_text();checks=[];cases=[]
def check(name,yes,detail=None):checks.append(dict(nome=name,passou=bool(yes),detalhe=detail))
def case(name,got,want,why):cases.append(dict(nome=name,obtido=got,esperado=want,motivo=why,passou=got==want));check(name,got==want)
def reject(name,fn):
 try:fn();ok=False
 except ValueError:ok=True
 case(name,ok,True,'Requisito ou recurso ausente impede a operação.')
def maxclass(lvl):
 return next(c for end,c in [(4,1),(8,2),(12,3),(16,4),(20,5),(25,6),(30,7)] if lvl<=end)
def pvturn(points,conscious=True):return min(3,points+1) if conscious else points
def discount(cost,uses):return max(0,cost-1) if uses else cost
def efficiency(attr):return max(1,attr//2)
def repertoire(attr):return attr//2
class Bond:
 def __init__(self,points=0):self.points=points;self.used=set();self.offensive=False;self.move_owner={};self.extra_spent=0
 def use(self,name,cost,discounted=False,reaction=None):
  if name in self.used:raise ValueError('intervenção repetida')
  price=max(0,cost-int(discounted))
  if self.points<price:raise ValueError('pontos')
  if reaction is False:raise ValueError('reação')
  self.points-=price;self.used.add(name);return price
 def attack_adv(self):
  if self.offensive:raise ValueError('ofensivo usado')
  self.offensive=True
 def move(self,benefit,body,meters=0):
  if benefit in self.move_owner and self.move_owner[benefit]!=body:raise ValueError('benefício de movimento vinculado')
  if benefit=='precisao' and self.extra_spent+meters>3:raise ValueError('saldo extra')
  self.move_owner[benefit]=body
  if benefit=='precisao':self.extra_spent+=meters
 def swap(self):return self.points,self.offensive,dict(self.move_owner),self.extra_spent

def movement(speed,remaining):return min(speed/2,remaining)//1.5*1.5

def transfer(remaining,new_used=False,new_transmitted=False,maintains_single=True):
 if new_used or new_transmitted:return 0
 return remaining if maintains_single else min(remaining,1)

def combined(participants,normal=True,immediate=True,standard=True,bonus=True,move=True,used=False):
 if used or not normal or not immediate or not (standard and bonus and move):raise ValueError('combinação')
 if not participants or len(participants)>2:raise ValueError('participantes')
 for maximum,remaining in participants:
  if maximum<1 or remaining!=maximum:raise ValueError('básicas incompletas')
 return dict(especiais=2,basicas_gastas=sum(m for m,r in participants),acoes_dono=['Padrão','Bônus','Movimento'])

def conduct(spell_range,between,dist_owner_a,dist_owner_b,spare=True):
 if between>spell_range or dist_owner_a>18 or dist_owner_b>18 or not spare:raise ValueError('condução')
 return spell_range

def body_state(attribute,capacity,active,total,in_combat):
 active_cap=capacity if in_combat else 2
 if total>attribute+capacity or active>active_cap or active>total:raise ValueError('teto corpos')
 return dict(ativos=active,inativos=total-active,total=total,teto=attribute+capacity)

sources=json.loads((B/'FONTES.json').read_text())
for f in sources['publicadas']:
 p=R/f['arquivo'];check('fonte_preservada_'+f['id'],hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256'])
manual=(R/'sistema/05-material/livro/manual/35-caminhos-e-trilhas.md').read_text();integrated=(R/'caminhos/05-Edicao-Integrada/05-Evocador-Caminho-e-Trilhas.md').read_text()
check('manual_integrado_identicos',('## Evocador\n'+manual.split('## Evocador\n',1)[1].split('## Incursor\n',1)[0]).strip()==integrated.strip())
pages=re.split(r'<!-- page:',s)[1:];counts={p.split('|')[0]:len(p.split('-->',1)[1].split()) for p in pages}
check('33_paginas',len(pages)==33);check('180_400_palavras',all(180<=n<=400 for n in counts.values()),counts)
check('sem_titulo_como_ler',not re.search(r'^#+.*como ler',s,re.M|re.I));check('sem_artigo_inicial',not re.search(r'^#+\s+(?:A|O|As|Os)\s',s,re.M|re.I))
check('sem_legal',not re.search(r'\blegal(?:mente)?\b',s,re.I));check('sem_ponto_virgula',';' not in s)
measure=[float(x.replace(',','.')) for x in re.findall(r'(\d+(?:,\d+)?) m\b',s)];check('medidas_1_5',all(abs(x/1.5-round(x/1.5))<1e-8 for x in measure))
contracts={
 'reserva':'0 Pontos de Vínculo','teto':'máximo de **3**','ganho':'recebe **1 ponto**',
 'ofensivo':'um uso ofensivo por rodada','normal':'Liberação, Técnica Máxima e Expansão de Domínio são trunfos separados',
 'rerrolagem':'repita a rolagem inteira','uma_rerrolagem':'uma única repetição, considerando todas as fontes',
 'complementar':'Ação Bônus · Uma vez por rodada','combinacao_pe':'**4 PE**','eficiencia':'reduzir seu custo em **1 Ponto de Vínculo, até o mínimo de zero**',
 'combinada_antes':'antes da resolução e dos dados','especial_todas':'todas as suas básicas da rodada disponíveis',
 'principal_duas':'Duas básicas no seu turno','principal_uma':'exatamente uma invocação ativa','CP1':'Todo talento concedido por Repertório Ampliado é de **Categoria de Efeito 1**',
 'basica_C0':'A básica continua sendo Classe 0','ficha_apenas_permitidas':'talentos permitidos para entidades',
 'continuidade_metade':'metade da maior Classe permitida pelo nível da invocação, arredondada para baixo, com mínimo de 1',
 'reflexa':'Reação pessoal em vez dos Pontos de Vínculo','parceria_ataque':'um ataque seu com arma ou desarmado, com vantagem',
 'parceria_resposta':'sem atacar, executar especial ou participar de Golpe Acompanhado','cobrir':'a proteção dispensa o gasto e a disponibilidade dessa reserva de Reação',
 'multipla_quatro':'quatro invocações ativas','multipla_uma':'uma atuação básica que cause dano e uma especial comandada por rodada',
 'dupla':'dois primeiros espaços de feitiço conhecido','conceito':'conceito de técnica, Manejo ou Kata com entidades',
 'conduzir':'A segunda invocação precisa estar dentro do alcance da própria especial',
 'dois_principais':'um aprimoramento principal diferente a cada uma de até duas',
 'formacao':'ainda não tiver usado, investido ou transferido sua básica nessa rodada',
 'repertorio_attr':'metade do valor permanente do atributo escolhido, arredondada para baixo',
 'fora_corpos':'use capacidade de controle **4**, inclusive fora do combate'}
for k,v in contracts.items():check('contrato_'+k,v in s)
mutations=[('máximo de **3**','máximo de **6**'),('um uso ofensivo por rodada','um uso ofensivo por invocação'),('todas as suas básicas da rodada disponíveis','nenhuma básica disponível'),('**4 PE**','**0 PE**'),('dois primeiros espaços de feitiço conhecido','todos os espaços de feitiço conhecido'),('A básica continua sendo Classe 0','A básica tem Classe igual ao nível')]
for before,after in mutations:
 bad=s.replace(before,after);check('mutacao_'+before,bad!=s and not all(v in bad for v in contracts.values()))
# Counter state, exchange history, and negative cases.
case('abertura primeiro turno',pvturn(0),1,'Começa combate zero, ganha um na primeira abertura.')
case('inconsciente não ganha',pvturn(2,False),2,'Condição suspende ganho, sem apagar a reserva.')
case('teto não acumula quarto',pvturn(3),3,'Reserva máxima3.')
b=Bond(3);b.attack_adv();b.move('precisao','ave',1.5);before=b.swap();case('troca conserva usos',b.swap(),before,'Trocar beneficiária não reseta contadores.')
reject('segundo benefício ofensivo',b.attack_adv);reject('transferir movimento a outro corpo',lambda:b.move('precisao','cao',1.5));b.move('precisao','ave',1.5);reject('saldo extra acima3',lambda:b.move('precisao','ave',1.5))
case('corrigir custo especial',b.use('corrigir',1),1,'Custo1 independe da Classe da especial.')
reject('corrigir segunda vez',lambda:b.use('corrigir',1));case('mudar custo',b.use('mudar',2),2,'Dois pontos após corrigir gastam reserva3.')
reject('recolher sem pontos',lambda:b.use('recolher',2))
b=Bond(0);case('eficiente sem pontos',b.use('corrigir',1,True),0,'Uso diário reduz1 parazero. Limite da intervenção continua.')
reject('desconto não substitui coletiva',lambda:Bond(3).use('reposicionar',1,True,False))
for a,w in [(0,1),(1,1),(3,1),(4,2),(5,2),(6,3)]:case('eficiência atributo'+str(a),efficiency(a),w,'Metade para baixo,mínimo1.')
for a in range(7):case('repertório atributo'+str(a),repertoire(a),[0,0,1,1,2,2,3][a],'Valor permanente, sem mínimo1.')
for speed,rest,w in [(9,6,4.5),(9,3,3),(9,0,0),(12,9,6),(7.5,9,3)]:case('movimento '+str((speed,rest)),movement(speed,rest),w,'Metade da modalidade e saldo, arredondada à escala1,5m.')
for n in (0,1,2):case('troca principal saldo'+str(n),transfer(n),n,'Exatamente uma ativa antes/depois.')
case('corpo usado não renova',transfer(2,True),0,'Histórico do corpo impede duplicação.')
case('corpo transmissor não renova',transfer(2,False,True),0,'Saldo já transferido não reaparece.')
case('segunda ativa encerra adicional',transfer(2,False,False,False),1,'Permissão de duas depende de exatamenteuma.')
case('combinada principal',combined([(2,2)])['basicas_gastas'],2,'Uma principal pode executar duas especiais diferentes.')
case('combinada duas entidades',combined([(1,1),(1,1)])['basicas_gastas'],2,'Duas participantes gastam todas suasbásicas.')
for name,fn in [('basica gasta',lambda:combined([(2,1)])),('zero basicas',lambda:combined([(0,0)])),('sem bonus',lambda:combined([(1,1)],bonus=False)),('sem movimento',lambda:combined([(1,1)],move=False)),('trunfo',lambda:combined([(1,1)],normal=False)),('Carregar',lambda:combined([(1,1)],immediate=False)),('repeticao combate',lambda:combined([(1,1)],used=True))]:reject('combinada rejeita '+name,fn)
for level,w in [(19,2),(20,2),(21,3),(25,3),(26,3),(30,3)]:case('continuidade nivel'+str(level),maxclass(level)//2,w,'Limite pela Classe real, não nível/2.')
case('continuidade entidade nivel1',max(1,maxclass(1)//2),1,'Principal de nível baixo conserva mínimo1, mas precisa conhecer especiais diferentes.')
case('resposta entidade27',maxclass(27)-1,6,'Classe maior menos1.')
case('resposta pessoal27',(maxclass(27)+1)//2,4,'Metade para cima.')
case('manifestacao temporaria nivel11',min(5*maxclass(11),57//2),15,'57PV de entidade comCon2, teto28.')
case('vida apos protecao',57-max(0,20-15),52,'Exemplo numérico corrigido para ficha realizável.')
case('duplas dois espacos',2*2,4,'Dois espaços dão quatro entidades.')
case('duplas terceiro espaco',2*2+1,5,'Terceiro não recebe dupla.')
case('dois espacos nivel2 sobra',3-2,1,'Três espaços conhecidos no nível2.')
case('conducao9mais9',conduct(9,9,18,18),9,'Alcance novo9, percurso composto até18, com duplo requisito.')
for name,fn in [('apoiadora longe',lambda:conduct(9,10.5,18,18)),('fora comando',lambda:conduct(9,9,19.5,18)),('sem basica',lambda:conduct(9,9,18,18,False))]:reject('conduzir '+name,fn)
case('corpos2 total6 combate',body_state(2,4,4,6,True),dict(ativos=4,inativos=2,total=6,teto=6),'Capacidade4 da Trilha.')
case('corpos2 total6 fim',body_state(2,4,0,6,False),dict(ativos=0,inativos=6,total=6,teto=6),'Desativar não destrói nem transporta.')
case('corpos2 total6 fora',body_state(2,4,2,6,False),dict(ativos=2,inativos=4,total=6,teto=6),'Só duas ativas fora do combate.')
reject('corpos quarto fora',lambda:body_state(2,4,4,6,False));reject('corpos setimo',lambda:body_state(2,4,4,7,True))
case('principal exemplo PE',12-3,9,'Padrão+primeira básica; segunda básica grátis.')
case('principal exemplo acertos',[max(4,7)+6>=13,9+4>=13],[True,True],'Uma vantagem ofensiva e segundo ataque normal.')
case('parceria exemplo recurso',[pvturn(2)-1,movement(9,9),9-movement(9,9)],[2,4.5,4.5],'Abertura concede1, AbrirEspaço gasta1.')
# Exact probability models; all require reachable DC and independent d20 rolls.
models=[]
for threshold in range(2,21):
 p=Fraction(21-threshold,20);adv=1-(1-p)**2;dis=p*p
 reroll=1-(1-p)**2;adv_reroll=1-(1-adv)**2
 models.append(dict(d20_minimo=threshold,normal=float(p),vantagem=float(adv),desvantagem=float(dis),repeticao_falha=float(reroll),vantagem_e_repeticao_inteira=float(adv_reroll)))
check('probabilidades_limites',all(0<=x['desvantagem']<=x['normal']<=x['vantagem']<=x['vantagem_e_repeticao_inteira']<=1 for x in models))
case('vantagem repetida p50',float(1-(1-Fraction(3,4))**2),.9375,'Corrigir repete os dois dados, uma única tentativa, custo1.')
# Structural action envelope, not encounter DPS: damaging capacities may be multi-hit.
actions=[dict(trilha='Principal',nivel=2,basicas=2,especiais_no_comando=1,auxiliar=0),dict(trilha='Principal',nivel=19,basicas=2,especiais_no_comando=2,auxiliar=1),dict(trilha='Parceria',nivel=19,basicas_entidades=2,especial_e_feitico=2,ofensivo_aprimoramento=1),dict(trilha='Múltiplas',nivel=11,corpos=4,basica_com_dano=1,especial_comandada=1,apoios=2)]
check('limite_ofensivo_multiple',actions[-1]['basica_com_dano']==1 and actions[-1]['especial_comandada']==1)
report=dict(ok=all(x['passou'] for x in checks),manuscritos_auditados={str((B/'EVOCADOR.md').relative_to(R)):hashlib.sha256(s.encode()).hexdigest()},sha256_texto=hashlib.sha256(s.encode()).hexdigest(),aprovado=all(x['passou'] for x in checks),quantidades=dict(verificacoes=len(checks),casos=len(cases),perfis_probabilidade=len(models),mutacoes=len(mutations)),verificacoes=checks,casos=cases,palavras_paginas=counts,modelos_probabilidade=models,perfis_recursos=actions,limites=['Enumerações locais de regras e recursos, não playtest ou comparação de dano total entre todos os Caminhos.','Modelos de probabilidade não incluem imunidades, Bloquear, crítico, alcance, dano ou composição de encontro.','Ação ofensiva e quantidade de ataques não são sinônimos: a ficha de cada capacidade pode conter mais de uma rolagem.','Modelo de corpos inclui fechamento autorizado pelo coordenador; exige sincronização R11 antes de publicar.'])
(B/'evidencias').mkdir(exist_ok=True);(B/'evidencias/AUDITORIA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(aprovado=report['aprovado'],quantidades=report['quantidades'],falhas=[x for x in checks if not x['passou']]),ensure_ascii=False,indent=2))
raise SystemExit(0 if report['aprovado'] else 1)
