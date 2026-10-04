"""R05: regressão contra candidatas correntes e modelos exatos. Não é playtest."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from collections import Counter
import re,json,hashlib,math
B=Path(__file__).resolve().parent;P=next(p for p in B.parents if (p/'validacao-editorial').is_dir());R=next(p for p in B.parents if (p/'sistema/03-mecanica').is_dir())
S=B/'EQUIPAMENTO.md';s=S.read_text();h=hashlib.sha256(S.read_bytes()).hexdigest();E=B/'evidencias';E.mkdir(exist_ok=True)
checks=[]
def ck(n,a,e=True):checks.append(dict(caso=n,obtido=a,esperado=e,ok=a==e))
def dump(n,d):E.joinpath(n).write_text(json.dumps(d,ensure_ascii=False,indent=2,default=str)+'\n')
def rows(t):
 return [[x.strip() for x in l.strip('|').split('|')] for l in t.splitlines() if l.startswith('|') and not re.match(r'^\|[-:| ]+\|$',l)]
def weapons(t):return {re.sub(r' \(.*\)$','',r[0]):r for r in rows(t) if len(r)==7 and re.match(r'^\d+d\d+ ',r[2])}
w=weapons(s);base=weapons((B.parent/'lote-04-r4/ARMAS.md').read_text());src=json.loads((B/'FONTES.json').read_text());leve=set(src['armas_recebem_Leve']);dec=json.loads((B/'ALTERACOES.json').read_text())
ck('52 armas sem perda de linha',set(w),set(base));ck('Contagem de armas',len(w),52)
for name,row in w.items():
 expected=base[name].copy()
 if name in leve:expected[3]+=' · Leve'
 if name=='Revólver' and any(x['id']=='EQ22' for x in dec['decisoes']):expected[6]='150.000 / 300.000'
 ck('Colunas autorizadas: '+name,row,expected)
 ck('Volume preservado: '+name,row[5],base[name][5])
ck('Leve explícita:19',sum('Leve' in r[3].split(' · ') for r in w.values()),19)
eligible=[n for n,r in w.items() if 'Leve' in r[3].split(' · ') or 'Fineza' in r[3].split(' · ')]
ck('Leve ou Fineza:21',len(eligible),21);ck('Taco não é Leve', 'Taco' in eligible,False);ck('Katana/Rapieira preservadas',all(n in eligible for n in ['Katana','Rapieira']))
# Every unchanged table row remains, including 9 armor,9 ammo,13 supplies,9 prices,17 effects.
for f in src['fontes_correntes']:
 path=R/f['arquivo'];ck('Fonte preservada: '+path.name,hashlib.sha256(path.read_bytes()).hexdigest(),f['sha256'])
 if path.name in ['ARMAS.md','EQUIPAMENTO-EM-JOGO.md']:continue
 for row in rows(path.read_text()):ck('Tabela preservada: '+path.name+' / '+row[0],row in rows(s))
oldmagic=(B.parent/'lote-08/EQUIPAMENTO-AMALDICOADO.md').read_text();magic=json.loads((B.parent/'lote-08/CATALOGO.json').read_text())['itens']
for it in magic:
 def block(t):return t.split('## '+it['nome']+'\n',1)[1].split('\n## ',1)[0].split('<!-- page:',1)[0].strip()
 ck('Ficha especial completa: '+it['nome'],block(s),block(oldmagic))
ck('17 ferramentas',len(magic),17)
parts=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',s);pages={parts[i]:parts[i+2] for i in range(1,len(parts),3)}
ck('39 páginas lógicas',len(pages),39);ck('Âncoras únicas',len(pages),len(re.findall(r'<!-- page:',s)))
for dest in re.findall(r'\]\(#([^)]+)\)',s):ck('Destino local: '+dest,dest in pages)
for title in re.findall(r'^#{1,6} (.*)',s,re.M):ck('Título direto: '+title,not re.match(r'^(?:A|O|As|Os|Como ler)\b',title))
ck('Combate: múltiplos de1,5m',all(Q(x.replace(',','.'))/Q('1.5')==int(Q(x.replace(',','.'))/Q('1.5')) for x in re.findall(r'(\d+(?:,\d+)?) m\b',s)))
# Exact distribution of sum of NdS and maximum of TWO sums, not per-die advantage.
def distribution(n,d):
 c=Counter({0:1})
 for _ in range(n):
  out=Counter()
  for subtotal,count in c.items():
   for die in range(1,d+1):out[subtotal+die]+=count
  c=out
 return c
par=[]
for n,d in [(1,4),(1,6),(1,8),(1,10),(1,12),(2,6),(2,8),(2,10),(4,6),(4,8),(4,10)]:
 c=distribution(n,d);total=sum(c.values());mean=Q(sum(k*v for k,v in c.items()),total);mx=sum(Q(max(a,b)*ca*cb,total**2) for a,ca in c.items() for b,cb in c.items())
 par.append(dict(dados=f'{n}d{d}',normal=float(mean),par=float(mx),ganho=float(mx-mean)))
 ck(f'Par{n}d{d}: limites',mean<mx<n*d)
ck('Par1d6 média161/36',Q(str(next(x['par'] for x in par if x['dados']=='1d6'))).limit_denominator(),Q(161,36))
ck('Par2d6 não é2Par1d6',next(x['par'] for x in par if x['dados']=='2d6')<2*next(x['par'] for x in par if x['dados']=='1d6'))
ck('Par: maior soma, não por dado',max(sum([1,6]),sum([5,5])),10)
ck('Par crítico conjunto4d6',len([1,2,3,4]),4)
# Both a failed shot and a natural1/2 expend ammunition; reloading conserves total.
transitions=0
for cap in range(1,5):
 for loaded,reserve,ready,low,add in product(range(cap+1),range(13),[False,True],[False,True],range(cap+1)):
  before=loaded+reserve
  if loaded and ready:
   after=loaded-1;needs=(after==0 or low)
   ckname=None;assert after+reserve==before-1 and (needs or after>0);transitions+=1
  amount=min(add,reserve,cap-loaded);after=loaded+amount;stock=reserve-amount
  assert after+stock==before and 0<=after<=cap and stock>=0;transitions+=1
ck('Conservação em transições de munição',transitions>1000)
# Mandatory counters depend on weapon AND bearer, unlike wear/unwear.
class Counters:
 def __init__(self,n):self.n=n;self.items={};self.people={}
 def use(self,item,person):
  if self.items.get(item,0)>=self.n or self.people.get(person,0)>=self.n:return False
  self.items[item]=self.items.get(item,0)+1;self.people[person]=self.people.get(person,0)+1;return True
c=Counters(1)
for title,item,person,result in [('Uso inicial','a','Rina',True),('Outra cópia não renova pessoa','b','Rina',False),('Emprestar não renova objeto','a','Mei',False),('Outra cópia e pessoa','b','Mei',True)]:ck(title,c.use(item,person),result)
c.people.clear();ck('Descanso sem peça não renova peça',c.use('a','Rina'),False);c.items.clear();ck('Dois relógios recuperados',c.use('a','Rina'))
a=Counters(2);count=0
for turn in range(5):
 reaction=True
 for event in range(4):
  if reaction and a.use(str(event)+str(turn),'Rina'):count+=1;reaction=False
ck('20 gatilhos,20 cópias Avulsa:2 usos',count,2)
# hand slots, wearable slots, one garment and one shield. Covers Vestida during actual attack.
options=[(1,0,0,0),(2,0,0,0),(1,0,0,1),(0,1,0,1),(0,1,1,0),(0,1,1,0),(0,1,1,0),(0,1,0,0)]
def legal(c,float_cost=1):
 h,w,g,sh=[sum(x*o[i] for x,o in zip(c,options)) for i in range(4)];w+=c[3]*(float_cost-1)
 return h<=2 and w<=2 and g<=1 and sh<=1
valid=[c for c in product(range(3),repeat=8) if legal(c)]
ck('Máximo quatro efeitos em uso',max(sum(c) for c in valid),4)
ck('Escudo flutuante usa vaga',legal((2,0,0,1,1,0,0,1)),False)
ck('Arma2 +flutuante+roupa',legal((0,1,0,1,1,0,0,0)))
ck('Dois uniformes mágicos',legal((0,0,0,0,1,1,0,0)),False)
ck('Mutação vaga grátis permite5',max(sum(c) for c in product(range(3),repeat=8) if legal(c,0)),5)
# Numeric inventory copied from current tables, read live. Imported structural catalog is a baseline only.
nums=json.loads((B.parent/'lote-04-r4/ARMAS.json').read_text());byname={x['nome']:x for x in nums}
items={r[0]:r for r in rows(pages['eqi-itens']) if len(r)==4 and r[0] not in ['Item']}
def number(v):return Q(v.replace('¥','').replace('.','').replace(',','.').strip())
vol=lambda name:Q(w[name][5].replace(',','.'))
kit=['Mochila','Corda','Lanterna elétrica','Pilhas de reserva','Cantil']
kv=sum(number(items[n][3]) for n in kit);kp=sum(number(items[n][2]) for n in kit)
ck('Exploração Volume',kv,Q('1.3'));ck('Exploração preço',kp,13000)
ck('Kit Katana Volume',vol('Katana')+Q('.5')+Q('.3')+kv,Q('3.1'));ck('Kit Katana saldo',150000-48000-12000-kp,77000)
ck('Hankyū+aljava+Traje1',vol('Hankyū')+Q('.5')+Q('.3'),Q('1.8'))
ck('Pistola+duasreservas+Traje1',vol('Pistola')+Q('.4')+Q('.3'),Q('1.2'))
ck('Metralhadora comreservas/exploração',vol('Metralhadora Pesada')+1+Q('.3')+kv,Q('6.6'))
ck('Metralhadora não obrigaForça7',3>=3 and Q('6.6')<=5+3)
ck('Naginata Força0 carga cabe mas manejo falha',vol('Naginata')+Q('.3')<=5 and byname['Naginata']['forca']>0)
ck('Reposição3Rifles+lanterna+pilhas',3*1500+3000+500,8000);ck('Volume reposição',3*Q('.3')+Q('.2')+Q('.1'),Q('1.2'))
# Score all52*7armor*4shields*7STR*7DEX pairs with and without exploration.
armor=[(0,99,0,0),(1,99,0,.3),(2,99,0,1),(3,99,3,2),(4,0,3,2),(5,0,4,3),(6,0,6,4)];shields=[(0,99,0,0),(1,5,0,.5),(2,3,3,1),(3,1,5,2)]
loadcount=accepted=0;defenses=[]
for weapon,arm,shield,strength,dex,exploration in product(nums,armor,shields,range(7),range(7),[False,True]):
 loadcount+=1;v=Q(str(weapon['volume']))+Q(str(arm[3]))+Q(str(shield[3]))+(kv if exploration else 0)
 ok=strength>=max(weapon['forca'],arm[2],shield[2]) and weapon['maos']+(1 if shield[0] else 0)<=2 and v<=5+strength
 if ok:accepted+=1;defenses.append(10+min(dex,arm[1],shield[1])+arm[0]+shield[0])
ck('Matriz completa de carga',loadcount,52*7*4*7*7*2)
ck('Defesa Traje2+Médio Dex4',10+min(4,3)+2+2,17);ck('Defesa Revest3+Torre',10+0+6+3,19)
# Price decision does not change combat power; it changes initial acquisition margin.
for name,expected in [('Pistola',25000),('Revólver',0)]:
 creation=number(w[name][6].split('/')[0]);ck('Saldo inicial: '+name,150000-creation,expected)
ck('Prêmio de preço Revólver20%',number(w['Revólver'][6].split('/')[0])/number(w['Pistola'][6].split('/')[0]),Q(6,5))
ck('Alcance Revólver33%',Q(12,9),Q(4,3))
# Requirement loss does not remove armor/cap or restore passive; Contrapeso bypasses onlyown req.
ck('Força4→2 Revest2 suspenso mantém teto',10+min(4,0)+0,10)
ck('Força5→4 Torre suspensa mantém teto',10+min(4,1)+0,11)
ck('Contrapeso permite requisito mas não carga',bool(4>5+0),False)
ck('Corpo60kg Força0 fronteira',Q(60,12)<=5)
ck('Corpo61kg não cabeForça0',Q(61,12)<=5,False)
ck('Corpo60kg+itens1+portador2 requerForça3',Q(60,12)+1+2,8)
# Whole-round timing and pause. Time spent never creates partial benefits.
ck('Traje1min são10 rodadas',60//6,10);ck('Revest vestir10min100rodadas',600//6,100);ck('Revest retirar5min50rodadas',300//6,50)
ck('Pausa após4turnos conserva24seg',4*6,24);ck('Dois trabalhos4+6completamTraje',4*6+6*6,60)
# Recovery shared once, no ammo duplication by splitting participants.
for shots in range(41):ck('Recuperação projéteis '+str(shots),shots//2<=shots)
ck('Besta criação total20',1+19,20);ck('Pistola inicial6',2*3,6);ck('MG inicial12',4*3,12)
ck('Parcial com1tiro Volumeinteiro',Q('.2'),Q('.2'))
# Probabilities both straight and advantage: natural1/2 state comes from kept die.
jams={mode:Q(sum((max(a,b) if mode=='vantagem' else min(a,b))<=2 for a,b in product(range(1,21),repeat=2)),400) for mode in ['vantagem','desvantagem']}
ck('Recarga1/2 comvantagem',jams['vantagem'],Q(1,100));ck('Recarga1/2 desvantagem',jams['desvantagem'],Q(19,100))
ck('Recarga normal10%',Q(2,20),Q(1,10))
tr=[]
for n,delta in product(range(1,19),range(-10,11)):
 p=Q(sum(r+delta>=8 for r in range(1,21)),20);fail=Q(n*9,2);saved=Q((n//2)*9,2);normal=fail*(1-p)+saved*p
 tr.append(dict(dados=n,diferenca=delta,normal=float(normal),quebranto=float(saved),anatema=float(normal*(1-p))))
ck('TRigual65%',Q(sum(r>=8 for r in range(1,21)),20),Q(13,20))
ck('3d8 sucesso1d8',next(x['quebranto'] for x in tr if x['dados']==3 and x['diferenca']==0),4.5)
ck('3d8 médiaTR7.65',next(x['normal'] for x in tr if x['dados']==3 and x['diferenca']==0),7.65)
ck('Desgaste sequência preservada',[2,2,1,0],[3-1,3-1,3-2,3-3])
# Invariants attached to the current wording and adversarial removals.
phrases=['Não concede outro ataque','A arma e as mãos necessárias ficam ocupadas','livres de outros objetos ou tarefas','Ação Completa','6 segundos','a peça não está pronta para uso','termine de retirar o anterior','Seu teto de Destreza continua valendo','sem acrescentar nem consumir munição','cada nova manipulação simples exige uma Ação de Movimento inteira','se essa mão estiver livre','sem crítico','somente a Integridade','Cópias do mesmo efeito compartilham o limite por personagem','antes de começar a preparar o novo']
for phrase in phrases:
 ck('Contrato atual: '+phrase,phrase in s);ck('Mutação textual recusada: '+phrase,phrase in s.replace(phrase,'REMOVIDO'),False)
# Ownership: do not reproduce Assassin/Pugilist/other class mechanics.
ck('Não ensina classes em equipamento',not re.search(r'Golpe Cirúrgico|Recuperar Base|Rajada Marcial|Contra a Parede|Cadência Marcial',s))
propositions=dict(sha256_texto=h,armas=52,leves=sorted(leve),elegiveis=eligible,modelos_par=par,transicoes_municao=transitions,conjuntos_itens=3**8,conjuntos_permitidos=len(valid),matriz_carga=loadcount,perfis_utilizaveis=accepted,probabilidade_recarga=jams,defesas_TR=tr)
dump('MODELOS.json',propositions)
result=dict(ok=all(c['ok'] for c in checks),sha256_texto=h,verificacoes=len(checks),checks=checks,manuscritos_auditados={str(S.relative_to(R)):h},limites=['Modelos exatos sob hipóteses registradas, sem teste de jogadores.','Sem comparação universal de poder entre utilidades distintas.','Cisão mantém sua regra; a raiz reconcilia o dono Integridade.','Preço mede decisão de compra, não equilíbrio de dano depois que o dinheiro deixa de limitar.'])
dump('auditoria-numerica.json',result);dump('regras-verificadas.json',dict(ok=result['ok'],sha256_texto=h,casos=checks))
print(json.dumps(dict(ok=result['ok'],verificacoes=len(checks),transicoes=transitions,carga=loadcount,permitidos=accepted,falhas=[c for c in checks if not c['ok']]),ensure_ascii=False,default=str));raise SystemExit(not result['ok'])
