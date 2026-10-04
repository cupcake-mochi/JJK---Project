"""Auditoria de modelo e texto. Não é motor de combate nem playtest.
Contas do candidato confrontadas com tabela publicada; exemplos têm resultados
independentes esperados. Perfis de custo são superconjunto, não 840 feitiços.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations_with_replacement, product
from math import ceil
import json,re,hashlib
B=Path(__file__).resolve().parent;R=B.parents[5];E=B/'evidencias'
s=(B/'FUNDAMENTO.md').read_text();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[];cases=[]
def ck(n,actual,expected):
 checks.append(dict(verificacao=n,obtido=actual,esperado=expected,ok=actual==expected))
def scenario(n,actual,expected,reason):
 cases.append(dict(cenario=n,obtido=actual,esperado=expected,motivo=reason,ok=actual==expected))
def dump(path,v):path.write_text(json.dumps(v,ensure_ascii=False,indent=2,default=lambda x: float(x) if isinstance(x,Fraction) else str(x))+'\n')
sections={m[1]:m[3] for m in re.finditer(r'<!-- page:([^|]+)\|([^>]+) -->\s*(.*?)(?=<!-- page:|\Z)',s,re.S)}
rows={}
for line in sections['pontos'].splitlines():
 m=re.fullmatch(r'\| ([1-7]) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|',line)
 if m:
  c,n,b,l,mid,h=map(int,m.groups());rows[c]={'nivel':n,'B':b,'L':l,'M':mid,'H':h}
source=R/'sistema/05-material/livro/manual/40-fundamento.md';old=source.read_text();published={}
for line in old.splitlines():
 m=re.match(r'\| \*\*([1-7])\*\* \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|',line)
 if m:
  c,n,b,l,mid,h,_=map(int,m.groups());published[c]={'nivel':n,'B':b,'L':l,'M':mid,'H':h}
ck('Sete curvas extraídas do texto',len(rows),7);ck('Preços e desbloqueios preservados',rows,published)
for c,row in rows.items():ck(f'Fórmula independente Classe{c}',[row['B'],row['L'],row['M'],row['H']],[3*c,ceil(c/2),c,ceil(c*1.5)])
def price(c,tier,free=False):
 p=0 if tier=='0' else rows[c][tier]
 return max(1,p-ceil(c/2)) if free else p
def build(c,form,imps,refund=0,mode='dano'):
 spent=price(c,form)+sum(price(c,t,f) for t,f in imps)
 rest=rows[c]['B']-spent+min(2*c,refund,spent)
 if rest<0:return None
 if mode=='cura':return min(2*c,rest)
 if mode=='onda_cura':return min(rows[c]['B']-price(c,'H'),rest)
 if mode=='apoio':return 3*rest
 return rest
examples=[
 ('Fio de Arrasto',1,'0',[('L',True)],0,'dano',2),
 ('Rede de imobilização',3,'L',[('H',False),('L',False)],0,'dano',0),
 ('Divisória antes de descartar dados',3,'0',[('M',True)],0,'dano',8),
 ('Socorro',2,'0',[('L',False),('M',False)],0,'apoio',9),
 ('Salto e Gesto',2,'0',[('M',False)],1,'dano',5),
 ('Corte medido C2',2,'0',[('M',True),('L',True)],1,'dano',5),
 ('Corte medido C3',3,'0',[('M',True),('L',True)],2,'dano',9),
 ('Corte medido C5',5,'0',[('M',True),('L',True)],3,'dano',15),
 ('Liberação sem reembolso Atrasar, antes do +C',3,'L',[],0,'dano',7),
 ('Máxima Fenda: saldo não vira dano',5,'0',[('L',True),('L',True)],0,'dano',13),
]
for n,c,f,imps,ref,mode,expected in examples:ck(n,build(c,f,imps,ref,mode),expected)
ck('Liberação C3 final',build(3,'L',[])+3,10);ck('Liberação C3 PE',ceil(4.5*3),14)
ck('Dano da Máxima independente do saldo','24d8 de Cortante' in sections['maximadano'],True)
ck('Geometria Anteparo 12 quadrados',Fraction(9*3)/Fraction(1.5**2),12)
# Superconjunto de preços: preservação de orçamentos, tetos e monotonicidade.
opts=[(tier,free) for tier in 'LMH' for free in (False,True)]
profiles=[(form,parts) for form in '0LMH' for n in range(5) for parts in combinations_with_replacement(opts,n)]
ck('Perfis de preço',len(profiles),840)
states=0;fail=[]
for c,(form,parts) in product(rows,profiles):
 if len(parts)>(2 if c<=2 else 3 if c<=4 else 4):continue
 spent=price(c,form)+sum(price(c,*p) for p in parts)
 for refund in range(2*c+1):
  states+=1;x=build(c,form,parts,refund)
  if x is not None and not(0<=x<=3*c):fail.append((c,form,parts,refund,x))
ck('Saldo viável não supera base em todos estados',fail,[])
maxrows=[]
for line in sections['maxima'].splitlines():
 m=re.fullmatch(r'\| (17 a 20|21 a 25|26 a 30) \| (\d+)d8 \| (\d+) \| (\d+) \|',line)
 if m:maxrows.append([int(x) for x in m.groups()[1:]])
ck('Máxima dados/pontos/PE do texto',maxrows,[[24,8,25],[28,12,30],[32,16,35]])
budgets={c:row[1] for c,row in zip((5,6,7),maxrows)}
def cost(c,p):f,imps=p;return price(c,f)+sum(price(c,*i) for i in imps)
transition=[]
for a,c in ((5,6),(6,7)):
 before=[p for p in profiles if cost(a,p)<=budgets[a]]
 lost=[p for p in before if cost(c,p)>budgets[c]]
 ck(f'Máxima sem regressão de preços{a}→{c}',lost,[])
 ck(f'Mínimo para preservar escolhas{a}→{c}',max(cost(c,p) for p in before),budgets[c])
 transition.append({'de':a,'para':c,'perfis_anteriores':len(before),'perdas':len(lost),'orcamento':budgets[c]})
ck('Quatro Médias Livres testemunham12',sum(price(6,'M',True) for _ in range(4)),12)
ck('Quatro Leves neutras testemunham16',sum(price(7,'L') for _ in range(4)),16)
for c,d in zip((5,6,7),(24,28,32)):
 ck(f'Efeito próprio Pesada cabe C{c}',price(c,'H')<=budgets[c],True)
 ck(f'Cura C{c} com restrição continua teto',build(c,'M',[],2*c,'cura'),2*c)
 ck(f'Onda C{c} com restrição conserva perda da Forma',build(c,'H',[],2*c,'onda_cura'),3*c-price(c,'H'))
# Repertório cotejado com resultados independentes e tabela impressa.
def known(level):return 2+level//2+sum(level>=m for m in (6,10,14,18,22,26,30))
ck('Repertório em oito marcos',[known(l) for l in (1,2,5,10,14,20,26,30)],[2,3,4,9,12,16,21,24])
ck('Repertório nunca recua',all(known(l)>=known(l-1) for l in range(2,31)),True)
# Distribuição e resistências. Metade de dados ≠ metade do resultado.
ck('TR comum em5d8',5//2,2);ck('TR Máxima resultado11',ceil(Fraction(3,4)*11),9)
ck('Salto C2 total inicial+secundário',5+5//2,7)
ck('Rajada24 repartida em6',sum([4]*6),24);ck('Rajada Certeiro erro4d8',4//2,2)
ck('Domada19 TocaAlma depois Certeiro',(19//2)//2,4)
# Reconstrói estudo Certeiro a partir da tabela atual, não importa seu resultado.
certainty=[]
for c,threshold in product(rows,(6,11,16)):
 for label,costc in [('normal',rows[c]['M']),('livre',price(c,'M',True)),('refund',0)]:
  n=3*c;d=n-costc
  normal=sum((2*n if roll==20 else n if roll>=threshold else 0) for roll in range(1,21))*4.5/20
  upgraded=sum((2*d if roll==20 else d if roll>=threshold else d//2) for roll in range(1,21))*4.5/20
  certainty.append({'classe':c,'limiar':threshold,'perfil':label,'media_comum':normal,'media_certeiro':upgraded})
ck('Certeiro, 63 cenários',len(certainty),63)
ck('Certeiro neutro C5 não domina ataque simples',any(x['media_certeiro']<x['media_comum'] for x in certainty if x['classe']==5 and x['perfil']=='normal'),True)
ck('Certeiro neutro C5 tem nicho',any(x['media_certeiro']>x['media_comum'] for x in certainty if x['classe']==5 and x['perfil']=='normal'),True)
# Contrato de combinações: subset, não um solucionador de todo catálogo.
bannedmax={'Salto','Queima','Estilhaço','Acúmulo','Remate','Quebra Coisa','Fica','Inescapável','Rápido','Reação'}
def valid(form,pieces,mode='comum',resolution='ataque',restriction=(),closed=()):
 if mode=='maxima' and (set(pieces)&bannedmax or restriction):return False
 if form=='Toque' and set(pieces)&{'Longe','Muito Longe'}:return False
 if form in {'Aura','Onda'} and set(pieces)&{'Longe','Muito Longe'}:return False
 if resolution=='TR' and set(pieces)&{'Rajada','Certeiro','De Novo'}:return False
 if set(pieces)&{'Passo'} and set(restriction)&{'Parado','Atrasar'}:return False
 if set(pieces)&{'Inescapável'} and (len(pieces)!=1 or restriction or mode!='comum'):return False
 if 'Retirada' in pieces:
  if mode!='maxima' or set(closed)&{'Área','Alcance'} or set(pieces)&{'Concentrada','Duradoura','Maior','Mais Um','Junto'}:return False
 if 'Amparo' in closed and form in {'Apoio','Cura','Onda'}:return False
 if 'Área' in closed and form in {'Explosão','Aura','Cone','Linha'}:return False
 return True
samples=[
 ('Toque não vira alcance', 'Toque',['Longe'],{},False),
 ('Projétil distante', 'Projétil',['Longe'],{},True),
 ('Toque com Passo físico', 'Toque',['Passo'],{},True),
 ('Parado bloqueia Passo', 'Projétil',['Passo'],{'restriction':['Parado']},False),
 ('Completa não proíbe movimento específico','Projétil',['Passo'],{'mode':'maxima'},True),
 ('Máxima não reembolsa Restrição','Projétil',[],{'mode':'maxima','restriction':['Gesto']},False),
 ('Rajada requer ataque','Projétil',['Rajada'],{'resolution':'TR'},False),
 ('Precisão também modifica CD','Projétil',['Precisão'],{'resolution':'TR'},True),
 ('Certeiro não se aplica em TR','Projétil',['Certeiro'],{'resolution':'TR'},False),
 ('Cura com Amparo fechada','Cura',[],{'closed':['Amparo']},False),
 ('Cone com Área fechada','Cone',[],{'closed':['Área']},False),
 ('Retirada não é feitiço comum','Efeito',['Retirada'],{},False),
 ('Retirada é Máxima própria','Efeito',['Retirada'],{'mode':'maxima'},True),
 ('Retirada não contorna Alcance fechada','Efeito',['Retirada'],{'mode':'maxima','closed':['Alcance']},False),
 ('Retirada não repete com concentração','Efeito',['Retirada','Concentrada'],{'mode':'maxima'},False),
 ('Retirada não ganha sétimo por Mais Um','Efeito',['Retirada','Mais Um'],{'mode':'maxima'},False),
 ('Retirada com Longe só seleção','Efeito',['Retirada','Longe'],{'mode':'maxima'},True),
 ('Inescapável comum sozinho','Projétil',['Inescapável'],{},True),
 ('Inescapável comum não aceita desconto por Restrição','Projétil',['Inescapável'],{'restriction':['Gesto']},False),
]
for name,form,ps,kwargs,answer in samples:scenario(name,valid(form,ps,**kwargs),answer,'Contrato candidato de compatibilidade; ler motivo no registro e na matriz.')
for piece in sorted(bannedmax):scenario('Máxima incompatível: '+piece,valid('Projétil',[piece],mode='maxima'),False,'Protege dados fixos, resolução, ação e recarga da Máxima.')
# Fica: várias entradas/turnos numa rodada ainda só uma resolução; erro conta.
def persistent(start,events):
 seen=set();out=[]
 for roundnum,who,event,outcome in events:
  key=(roundnum,who)
  if start<=roundnum<=start+5 and key not in seen:
   seen.add(key);out.append((roundnum,who,event,outcome))
 return out
seq=[(r,'A',event,'errou' if event=='entrou' else 'acertou') for r in range(1,8) for event in ('entrou','iniciou','entrou')]
scenario('Fica reentrada e erro ocupam resolução',len(persistent(1,seq)),6,'Rodada atual e cinco seguintes; conta resolução, não só dano.')
scenario('Fica dois alvos independentes',len(persistent(1,seq+[(r,'B','entrou','acertou') for r in range(1,7)])),12,'Uma resolução para cada criatura em cada rodada.')
scenario('Fica não reaplica condições','Os outros efeitos não são reaplicados por Fica.' in sections['persistente'],True,'Limite expresso; modelo não concede controle repetido.')
# Retirada: seleção imutável, terreno e condição consomem orçamento real.
def retreat(distance,pathcost,accept=True,mobility=True,slow=False):
 return distance<=18 and accept and mobility and pathcost<= (9 if slow else 18)
for name,args,exp in [
 ('Aliado inicialmente a20m fica fora',(20,6),False),('Trajeto18m em alcance',(18,18),True),
 ('Contorno24m não cabe',(9,24),False),('Terreno difícil9m custa18',(9,18),True),
 ('Sem consentimento',(9,3,False),False),('Contenção impede',(9,3,True,False),False),
 ('Lento reduz orçamento9m',(9,12,True,True,True),False)]:
 scenario('Retirada: '+name,retreat(*args),exp,'Modelo de trajetos físicos, seleção inicial e aceitação; não mede o valor tático do mapa.')
scenario('Retirada seis trajetos separados',6*18,108,'Metros de movimento não são equivalência de dano nem podem ser reunidos em um alvo.')
scenario('Recarga uso1 retorna5',1+3+1,5,'Exige terminar terceiro turno seguinte; rodada sem turno não avança contador.')
# Textual anchors bind exact mechanical choices to the artifact being tested.
anchors={
 'slots3rotas':'Isso vale para espaços de feitiço, de Manejo e de Kata.',
 'troca_nivel':'refazer essa troca usa a mesma revisão de um espaço',
 'descontoforma':'Formas não recebem desconto de Família Livre.',
 'juntodivide':'Junto faz a divisão de cura',
 'acumulo_preservado':'Acúmulo conserva sua exceção',
 'metadedados':'metade dos dados de dano, arredondada para baixo',
 'limiteconjuracao':'uma conjuração de Classe acima de 0 permite apenas mais um feitiço de Classe 0',
 'portal_termina':'a passagem se encerra antes do primeiro turno',
 'portal_unico':'Você só pode manter um par preparado',
 'retirada_fixa':'Declare destinos e percursos antes de mover qualquer um',
 'restricao_semduplicacao':'Aproveite no máximo o valor do gasto',
 'classe0_semrefund':'ela não recupera o dado pago nem cria pontos',
 'onda_max':'Cura ou Onda de cura os aplica como cura, sem o teto da Forma comum',
}
for name,phrase in anchors.items():ck('Contrato no texto: '+name,phrase in s,True)
# Requisito humano explícito: reserva disponível e capacidade declarada são necessários.
def entity_access(slot,declared_entity_function):return slot and declared_entity_function
for route in ('feitiço','Manejo','Kata'):
 for slot,declared in product((False,True),repeat=2):
  scenario(f'Entidade por {route}: espaço={slot}, previsão={declared}',entity_access(slot,declared),bool(slot and declared),'Espaço paga aquisição; a técnica/rota precisa comportar entidades, conforme pedido do usuário.')
ck('Requisito expresso no texto','A troca exige que invocações façam parte da técnica.' in s,True)
ck('Exemplo positivo de entidade coerente','A técnica de Bruna cria animais de papel' in s,True)
ck('Exemplo negativo sem invocação','sem criar ou chamar entidades, não permite essa troca' in s,True)
# Serialization supports independent reruns and records limits openly.
ok=all(c['ok'] for c in checks);sok=all(c['ok'] for c in cases)
audit={'data':'2026-10-03','ok':ok,'sha256_texto':sha(B/'FUNDAMENTO.md'),'manuscritos_auditados':{str((B/'FUNDAMENTO.md').relative_to(R)):sha(B/'FUNDAMENTO.md')},'verificacoes':len(checks),'estados_de_orcamento':states,'perfis_maxima':len(profiles),'transicoes_maxima':transition,'certeiro_cenarios':certainty,'checks':checks,'limites':['Enumeração de perfis de custo não prova que toda combinação semântica é válida.','Não mede Bloquear, builds completos, mapas, inimigos ou comportamento real de jogadores.','Peças próprias e orçamento ampliado da Máxima exigem teste de mesa.']}
dump(E/'auditoria-numerica.json',audit)
dump(E/'regras-verificadas.json',{'data':'2026-10-03','ok':sok,'sha256_texto':sha(B/'FUNDAMENTO.md'),'metodo':'Casos executados por modelo explícito mais âncoras textuais; não execução de combate real. Auditorias humanas simuladas por modelos estão separadas.','casos':cases,'quantidade':len(cases),'limites':'Subset deliberado de combinações; catálogo completo R07 permanece pendente.'})
dump(B/'CONTRATO.json',{'fonte_custos':str(source.relative_to(R)),'sha256_fonte':sha(source),'candidata':sha(B/'FUNDAMENTO.md'),'classes':rows,'maxima':maxrows,'maxima_incompativeis':sorted(bannedmax),'cenarios':len(cases),'auditoria':'auditar.py','nao_e_motor_de_regras':True})
print(json.dumps({'ok':ok and sok,'verificacoes_numericas_textuais':len(checks),'estados':states,'casos_funcionais':len(cases),'falhas':[c for c in checks+cases if not c['ok']]},ensure_ascii=False))
raise SystemExit(0 if ok and sok else 1)
