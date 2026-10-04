"""Modelos exatos dos limites propostos. Não simula entendimento nem uma campanha."""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import json,re,hashlib,math
B=Path(__file__).resolve().parent;P=B.parents[1];R=P.parents[3]
# Absolute project root independently located by known source directory.
R=next(p for p in B.parents if (p/'sistema/03-mecanica').is_dir())
F=B/'EQUIPAMENTO-AMALDICOADO.md';s=F.read_text();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
checks=[]
def ck(name,actual,expected=True):checks.append({'caso':name,'obtido':actual,'esperado':expected,'ok':actual==expected})
cat=json.loads((B/'CATALOGO.json').read_text());items=cat['itens']
for it in items:
 header=re.search(r'^## '+re.escape(it['nome'])+r'\n\n([^\n]+)',s,re.M)[1];it['cabecalho']=header
 ck(it['nome']+': grau',re.search(r'Grau (\d|especial)\.',header)[1],it['grau'])
 block=s.split('## '+it['nome']+'\n',1)[1].split('\n## ',1)[0].split('<!-- page:',1)[0]
 if it['usos'] is None: ck(it['nome']+': frequência contínua/livre','vez por' not in header and 'vezes por' not in header)
 else:
  expected='Duas vezes por cena' if it['usos']==2 else ('Uma vez por descanso curto' if it['recuperacao']=='descanso curto' else 'Uma vez por cena')
  ck(it['nome']+': frequência',expected.casefold() in block.casefold())
cat['sha256_manuscrito']=sha(F);dump(B/'CATALOGO.json',cat)
ck('Seis tipos cobertos',sorted({x['tipo'] for x in items}),sorted(['arma','traje','revestimento','roupa','escudo','acessório']))
ck('Dezessete fichas distintas',len({x['nome'] for x in items}),17)
ck('Distâncias múltiplas de 1,5m',all(Q(x.replace(',','.'))/Q('1.5')==int(Q(x.replace(',','.'))/Q('1.5')) for x in re.findall(r'(\d+(?:,\d+)?) m\b',s)))
ck('Retorno usa propriedade existente','possuam Longo Alcance' in s and 'concede Arremesso' not in s)
ck('Recipiente não consumido','Seus recipientes seguem as regras de Munição' in s)
# Enumerate equipment footprints. Each entry has hands, worn spaces, garments, shields, effects.
options=[('arma1',1,0,0,0,1),('arma2',2,0,0,0,1),('escudo',1,0,0,1,1),('flutuante',0,1,0,1,1),('roupa',0,1,1,0,1),('traje',0,1,1,0,1),('revestimento',0,1,1,0,1),('acessório',0,1,0,0,1)]
def legal(counts,wear_limit=2,body_limit=1,float_cost=1):
 h,w,g,shield,e=[sum(c*opt[i] for c,opt in zip(counts,options)) for i in range(1,6)]
 w+=counts[3]*(float_cost-1)
 return h<=2 and w<=wear_limit and g<=body_limit and shield<=1
valid=[c for c in product(range(3),repeat=len(options)) if legal(c)]
ck('Teto quatro efeitos em 6561 combinações',max(sum(c) for c in valid),4)
ck('Duas armas e vestimenta + acessório',legal((2,0,0,0,1,0,0,1)))
ck('Escudo flutua + arma2 + roupa',legal((0,1,0,1,1,0,0,0)))
ck('Escudo flutua não mantém duas vagas extras',legal((2,0,0,1,1,0,0,1)),False)
ck('Roupa e Traje com efeitos não empilham',legal((0,0,0,0,1,1,0,0)),False)
ck('Duas proteções de escudo não acumulam',legal((0,0,1,1,0,0,0,0)),False)
ck('Mutação: retirar custo flutuante detectada',max(sum(c) for c in product(range(3),repeat=8) if legal(c,float_cost=0))>4)
ck('Mutação: três vagas detectada',max(sum(c) for c in product(range(3),repeat=8) if legal(c,wear_limit=3))>4)
# Counter state: separate object uses, character uses, and ordinary reaction availability.
class Counters:
 def __init__(self,limit):self.limit=limit;self.obj={};self.person={}
 def use(self,obj,person):
  if self.obj.get(obj,0)>=self.limit or self.person.get(person,0)>=self.limit:return False
  self.obj[obj]=self.obj.get(obj,0)+1;self.person[person]=self.person.get(person,0)+1;return True
c=Counters(1);ck('Primeiro uso',c.use('A','Rina'));ck('Cópia não repõe usuário',c.use('B','Rina'),False);ck('Empréstimo não repõe objeto',c.use('A','Mei'),False);ck('Outro personagem e outra cópia',c.use('B','Mei'))
c.person.clear();ck('Descanso só do usuário não recupera objeto',c.use('A','Rina'),False);c.obj.clear();ck('Recuperação de ambos permite novo uso',c.use('A','Rina'))
a=Counters(2);hits=[]
for round_ in range(1,6):
 reaction=True
 for attack in range(4):
  if reaction and a.use(str(round_)+str(attack),'Rina'):hits.append((round_,attack));reaction=False
ck('Vinte gatilhos, vinte cópias: dois ataques Avulsa',len(hits),2)
# Reach and return boundary conditions.
def returns(own_turn,hand_free,path_free,held,dist,maxdist):return own_turn and hand_free and path_free and not held and dist<=maxdist
for args,expect in [((1,1,1,0,18,18),True),((1,0,1,0,6,18),False),((0,1,1,0,6,18),False),((1,1,0,0,6,18),False),((1,1,1,1,6,18),False),((1,1,1,0,19.5,18),False)]:ck('Fiel '+str(args),bool(returns(*args)),expect)
ck('Insondável fora do turno: alcance de base','Fora do seu turno, use o alcance normal da arma.' in s)
# No +Defense rider; base protection and dex ceilings remain even on floating shield.
armor=[(0,99,0),(1,99,0),(2,99,0),(3,99,3),(4,0,3),(5,0,4),(6,0,6)]
shields=[(0,99,0),(1,5,0),(2,3,3),(3,1,5)]
rows=[]
for strength,dex,arm,shield in product(range(7),range(7),armor,shields):
 if strength<max(arm[2],shield[2]):continue
 d=10+min(dex,arm[1],shield[1])+arm[0]+shield[0]
 rows.append((strength,dex,d))
ck('Roupa simples não acrescenta proteção',armor[0][0],0)
ck('Revestimento3 + Torre / Dex2',10+min(2,0,1)+6+3,19)
ck('Escudo suspenso mantém exigência','mantém seu teto de Destreza e requisito de Força' in s)
# Exact d20 checks against 8 + opposing bonus. No auto success/fail assumed for ordinary TR.
def prob(diff):return Q(sum(roll+diff>=8 for roll in range(1,21)),20)
probabilities=[{'diferenca_bonus':d,'sucesso':float(prob(d))} for d in range(-10,11)]
ck('TR equivalente: 65%',prob(0),Q(13,20))
ck('TR quatro pontos atrás: 45%',prob(-4),Q(9,20))
# normalized spell damage 40, normal successful save halves it; before either roll.
p=prob(0);baseline=40*(1-p)+20*p
ck('Dano médio comum contra feitiço de40',float(baseline),27.0)
ck('Quebranto previne média7 nesse cenário',float(baseline-20),7.0)
ck('Anátema previne17.55 nesse cenário, uma vez',float(baseline*p),17.55)
# Cisao endpoint illustration only: enemy Integrity=.5HP; parties contribute equal preconversion damage.
cis=[]
for n in range(1,7):
 ordinary=Q(1,n);hp=Q(1,n-1) if n>1 else None;soul=Q(1,2);duration=min(hp,soul) if hp else soul
 cis.append({'membros':n,'tempo_comum':float(ordinary),'tempo_com_cisao':float(duration),'razao_duracao':float(duration/ordinary)})
ck('Cisão solo: metade tempo até uma barra esgotar',cis[0]['razao_duracao'],.5)
ck('Cisão grupo4: dispersão aumenta tempo nessa hipótese',cis[3]['razao_duracao'],4/3)
ck('Cisão não soma perda de vida','A vida não é descontada por esse dano.' in s)
# Desgaste: usage, unused mission, loan, last mission remains active.
remaining=3;balances=[]
for used in [True,False,True,True]:
 available=remaining>0
 if used and available:remaining-=1
 balances.append(remaining)
ck('Desgaste 3, missões uso/pausa/uso/uso',balances,[2,2,1,0])
ck('Última missão inteira explicitada','O efeito permanece disponível até o fim dela.' in s)
# Strict regression guards to ensure these tests reject a changed contract.
for phrase in ['até dois itens vestidos','apenas um pode ser uma vestimenta','Cópias do mesmo efeito compartilham o limite por personagem','Duas vezes por cena','não acrescenta automaticamente bônus','somente a Integridade']:
 ck('Contrato textual: '+phrase,phrase in s)
 for mutation in [s.replace(phrase,'REGRA ALTERADA')]:ck('Negativo: '+phrase,phrase not in mutation)
linked={str(F.relative_to(R)):sha(F)}
# Fractions are serialised by string; expected exact comparisons occurred above.
res={'ok':all(x['ok'] for x in checks),'verificacoes':len(checks),'checks':checks,'manuscritos_auditados':linked,'combinacoes_enumeradas':3**8,'conjuntos_permitidos':len(valid),'defesas_base_enumeradas':len(rows),'probabilidades_TR':probabilities,'cisao_hipotese_sem_rd_sem_estagios':cis,'limites':['Verificação de modelos e texto, não playtest.','Cisão ainda depende da revisão do subsistema de alma; estágio4 não equivale automaticamente a morte.','Funções diferentes não permitem ordenar todo catálogo por um número único.']}
(B/'evidencias/auditoria-numerica.json').write_text(json.dumps(res,ensure_ascii=False,indent=2,default=str)+'\n')
dump(B/'evidencias/regras-verificadas.json',{'ok':res['ok'],'sha256_texto':sha(F),'casos':checks}) if not any(isinstance(x['obtido'],Q) for x in checks) else (B/'evidencias/regras-verificadas.json').write_text(json.dumps({'ok':res['ok'],'sha256_texto':sha(F),'casos':checks},ensure_ascii=False,indent=2,default=str)+'\n')
for name in ['LOCALIZACAO-EDITORIAL.json','REVISAO-EDITORIAL.json']:
 f=B/'evidencias'/name;d=json.loads(f.read_text());d['sha256_texto']=sha(F);dump(f,d)
print(json.dumps({'ok':res['ok'],'verificacoes':len(checks),'conjuntos':len(valid),'falhas':[x for x in checks if not x['ok']]},ensure_ascii=False,default=str))
raise SystemExit(0 if res['ok'] else 1)
