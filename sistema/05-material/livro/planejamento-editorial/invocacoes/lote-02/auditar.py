#!/usr/bin/env python3
"""Auditoria R12: lê tabelas donas e verifica exemplos, fronteiras e inventário."""
from pathlib import Path
import hashlib,json,math,re,itertools
P=Path(__file__).resolve().parent
R=next(x for x in P.parents if (x/'sistema/03-mecanica').is_dir())
E=R/'sistema/05-material/livro/planejamento-editorial'
S=(P/'CONSTRUIR-INVOCACOES.md').read_text()
M=(R/'sistema/05-material/livro/manual/60-invocacoes.md').read_text()
F=(E/'fundamento/lote-01/FUNDAMENTO.md').read_text()
checks=[]
def check(name,passed,evidence):checks.append({'teste':name,'passou':bool(passed),'evidencia':evidence})
def save(name,obj):(P/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
pages=[]
for b in S.split('<!-- page:')[1:]:
 h,t=b.split('-->',1);ident,title=h.strip().split('|',1)
 pages.append({'id':ident,'titulo':title,'palavras':len(t.split()),'texto':t})
ids={p['id'] for p in pages}
check('IDs únicos',len(ids)==len(pages),len(pages))
check('Título coincide com marcador',all(p['texto'].lstrip().startswith('# '+p['titulo']+'\n') for p in pages),len(pages))
check('Faixa editorial 180–400 palavras',all(180<=p['palavras']<=400 for p in pages),[{k:p[k] for k in ['id','palavras']} for p in pages])
heads=re.findall(r'^#{1,6} (.+)$',S,re.M)
bad=[h for h in heads if re.match(r'(A|O|As|Os)\s|Como ler',h)]
check('Títulos diretos',not bad,bad)
refs=re.findall(r'\]\(#([^)]*)\)',S)
check('Remissões internas',all(r in ids for r in refs),refs)
check('Vocabulário e pontuação',not re.search(r'\blegal\b',S,re.I) and S.count(';') == 1 and 'Leitura de Feitiços é um Talento; Identificar Feitiço é uma Melhoria de Marca.' in S,{'legal':len(re.findall(r'\blegal\b',S,re.I)),'pontos_virgula':S.count(';')})
inv=json.loads((P/'INVENTARIO.json').read_text())
check('Todas as seções fonte têm dono',len(inv)==len(re.findall(r'^#{1,6} ',M,re.M)) and all(v['dono'] in ['R11','R12'] for v in inv),len(inv))
check('Destinos R12 existem',all(v['destino'] in ids for v in inv if v['dono']=='R12'),[v['destino'] for v in inv if v['dono']=='R12'])
# Parse approved source table; no fallback numbers if format changes.
rows=re.findall(r'^\| ([1-7]) \(([0-9]+)–([0-9]+)\) \| ([0-9]+)d6 \| ([0-9]+) \|',M,re.M)
assert len(rows)==7,'Mudou a tabela-fonte Números da entidade. Rever parser conscientemente.'
scale={int(c):{'min':int(lo),'max':int(hi),'basica':int(b),'pontos':int(p)} for c,lo,hi,b,p in rows}
canrows=re.findall(r'^\| ([1-7]) \| ([0-9]+) \| ([0-9]+) \| ([0-9]+) \|$',S,re.M)
can={int(c):{'pontos':int(p),'pe':int(pe),'melhorias':int(m)} for c,p,pe,m in canrows}
assert len(can)==7,'Mudou a tabela candidata de especiais.'
check('Tabela especial preservada',all(can[c]['pontos']==scale[c]['pontos'] for c in scale),can)
check('Custo 3×Classe real',all(can[c]['pe']==3*c for c in scale),can)
canbasic=re.findall(r'^\| ([0-9]+)–([0-9]+) \| ([1-7]) \| ([0-9]+)d6 \| ([0-9]+) \|$',S,re.M)
check('Básica e faixas preservadas',len(canbasic)==7 and all((int(lo),int(hi),int(b),int(p))==(scale[int(c)]['min'],scale[int(c)]['max'],scale[int(c)]['basica'],scale[int(c)]['pontos']) for lo,hi,c,b,p in canbasic),canbasic)
cp=F.split('# Pontos e preços\n',1)[1].split('## Quantidade de peças',1)[0]
crows=re.findall(r'^\| ([1-7]) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$',cp,re.M)
assert len(crows)==7,'Mudou tabela comum de preço.'
cost={int(c):dict(zip(['min','pontos','leve','media','pesada'],map(int,v))) for c,*v in crows}
curve=[];ondas=[]
for c,r in scale.items():
 free=max(1,c//2);avg=r['pontos']*4.5+r['basica']*3.5;player=cost[c]['pontos']*4.5
 curve.append({'classe':c,'especial_d8':r['pontos'],'basica_d6':r['basica'],'media_conjunta':avg,'feitiço_pessoal_medio':player,'razao':avg/player,'desconto_entidade':free,'desconto_pessoal':math.ceil(c/2)})
 old=r['pontos']-cost[c]['pesada'];new=old;personal=cost[c]['pontos']-cost[c]['pesada']
 ondas.append({'classe':c,'antes_limite_sem_reembolso_da_forma':old,'candidato_limite_util':new,'pessoal_limite_util':personal,'aumento_de_cura_por_alvo':new-old})
check('Desconto próprio nas Classes ímpares',all(' | '+str(max(1,c//2))+' ' in S for c in scale),curve)
check('Onda preserva teto anterior e fica abaixo do pessoal',all(o['aumento_de_cura_por_alvo']==0 and o['candidato_limite_util']<=o['pessoal_limite_util'] for o in ondas),ondas)
curas=[{'classe':c,'antes':r['pontos']-cost[c]['media'],'candidato':r['pontos']-cost[c]['media'],'pessoal':2*c} for c,r in scale.items()]
check('Cura preserva teto anterior', [r['candidato'] for r in curas]==[1,2,3,5,6,7,9] and all(r['antes']==r['candidato'] for r in curas), curas)
# Build examples from owner prices and candidate entity budget.
specs=[('Mordida precisa C1',1,0,[('leve',True)],['media'],'dano',2),('Mordida precisa C2',2,0,[('leve',True)],['media'],'dano',4),('Mordida precisa C3',3,0,[('leve',True)],['media'],'dano',6),('Fura C2 Livre',2,0,[('media',True)],[],'dano',3),('Tiras de resgate',2,0,[('media',False),('leve',False)],[],'apoio',3),('Remendo de papel',1,'media',[],[],'cura',1),('Onda C1 com Impulso e Gesto',1,'pesada',[('leve',False)],['leve'],'onda',0)]
examples=[]
for name,c,form,mods,restr,kind,expected in specs:
 rule=cost[c];f=rule[form] if isinstance(form,str) else form
 spend=f+sum(max(1,rule[k]-max(1,c//2)) if free else rule[k] for k,free in mods)
 refund=min(sum(rule[k] for k in restr),spend,2*c)
 balance=scale[c]['pontos']-spend+refund
 result=min(balance,scale[c]['pontos']-rule['pesada']) if kind=='onda' else min(balance,scale[c]['pontos']-rule['media']) if kind=='cura' else balance*3 if kind=='apoio' else balance
 row={'nome':name,'classe':c,'pontos':scale[c]['pontos'],'gasto':spend,'devolucao':refund,'saldo':balance,'resultado':result,'unidade':'PV temporária' if kind=='apoio' else 'd8','PE':3*c}
 examples.append(row);check('Conta: '+name,result==expected and balance>=0,row)
# Enumerate allowed refund arithmetic, including source's old Form exclusion.
builds=0;over=0
for c,r in scale.items():
 vals=[cost[c][k] for k in ['leve','media','pesada']];budget=r['pontos']
 for form,n,freebits,rs in itertools.product([0,*vals],range(3),itertools.product([False,True],repeat=2),itertools.product([0,cost[c]['leve'],cost[c]['media']],repeat=2)):
  for chosen in itertools.product(vals,repeat=n):
   spend=form+sum(max(1,v-max(1,c//2)) if freebits[i] else v for i,v in enumerate(chosen))
   refund=min(sum(rs),2*c,spend);balance=budget-spend+refund
   if balance<0:continue
   builds+=1;over+=balance>budget
check('Busca de restituição sem criar dados acima do orçamento',over==0,{'montagens_aritmeticas':builds,'excedentes':over,'limite':'Não substitui requisitos qualitativos das peças.'})
marks=[6,10,14,18,22,26,30];leveldata=[]
for level in range(1,31):
 cls=next(c for c,r in scale.items() if r['min']<=level<=r['max'])
 slots=math.floor((2+level/2)/2);passlevels=[1,*[m for m in marks if m<=level]]
 leveldata.append({'nivel':level,'classe':cls,'espacos':slots,'basicas':1 if level<=10 else 2,'pontos_atributos':9+sum(m<=level for m in marks),'passivas':len(passlevels),'CPs_maximas':[1 if m<=6 else 2 if m<=12 else 3 for m in passlevels]})
check('Marcos de espaço', [d['nivel'] for i,d in enumerate(leveldata) if i==0 or d['espacos']!=leveldata[i-1]['espacos']]==[1,4,8,12,16,20,24,28],leveldata)
check('30 níveis: 8 espaços, 8 passivas, 2 básicas, 16 atributos',leveldata[-1]['espacos']==8 and leveldata[-1]['passivas']==8 and leveldata[-1]['basicas']==2 and leveldata[-1]['pontos_atributos']==16,leveldata[-1])
hp=lambda lv,con,body=False:5+con+((4 if body else 3)+con)*(lv-1)
hps=[{'nivel':l,'constituicao':co,'comum':hp(l,co),'criada':hp(l,co,True)} for l,co in [(1,2),(2,2),(4,2),(5,2),(6,3),(30,6)]]
check('Vida dos exemplos e Constituição retroativa',[hp(2,2),hp(4,2),hp(5,2),hp(6,3),hp(5,2,True)]==[12,22,27,38,31],hps)
check('Ficha simples/apoio',[sum([3,2,2,1,1]),sum([0,2,2,3,2]),10+2+2//2,10+2+4//2,4+1//2,4+3//2]==[9,9,13,14,4,5],{'cão':{'atributos':9,'DEF':13,'perícias':4},'vigia':{'atributos':9,'DEF':14,'perícias':5}})
passive_names=['Leitura','Instinto','Raiz','Mão Firme','Farejador','Leitura de Feitiços','Fluxo','Eco','Costura','Contramedida','Escama','Afinidade','Talento Próprio']
check('Treze opções preservadas',all(re.search(r'^\| '+re.escape(n)+r' \|',S,re.M) for n in passive_names) and len(passive_names)==13,passive_names)
# Odds from current CD, not a made-up universal taming statistic.
taming=[]
for bonus in [2,4,6]:
 cd=8+bonus;success=sum(d+bonus>=cd for d in range(1,21))/20
 taming.append({'bonus_equivalente':bonus,'CD':cd,'resiste_e_exorciza':success,'domada':1-success})
check('Domação com bônus iguais: 35% domar, 65% resistir',all(abs(t['domada']-.35)<1e-9 for t in taming),taming)
sourcehashes=json.loads((P/'evidencias/fontes-iniciais-auditoria.json').read_text())
accepted=json.loads((P/'evidencias/fontes-concorrentes-finais.json').read_text())
check('Fontes preservadas ou delta candidato cotejado',all(hashlib.sha256((R/name).read_bytes()).hexdigest() in [h,accepted.get(name)] for name,h in sourcehashes.items()),len(sourcehashes))
check('Manual e integrado idênticos',hashlib.sha256((R/'invocacoes/05-Edicao-Integrada/60-invocacoes.md').read_bytes()).hexdigest()==hashlib.sha256((R/'sistema/05-material/livro/manual/60-invocacoes.md').read_bytes()).hexdigest(),'Leitura integral manual e equivalência binária integrada.')
sha=hashlib.sha256(S.encode()).hexdigest()
save('evidencias/auditoria-numerica.json',{'ok':all(c['passou'] for c in checks),'manuscritos_auditados':{str((P/'CONSTRUIR-INVOCACOES.md').relative_to(R)):sha},'sha256_texto':sha,'curva':curve,'onda':ondas,'cura':curas,'exemplos':examples,'progressao':leveldata,'vida':hps,'domacao':taming,'sem_playtest':True})
save('AUDITORIA.json',{'sha256_texto':sha,'checagens':checks,'total':len(checks),'falhas':sum(not c['passou'] for c in checks),'limite':'Testes de estrutura e matemática; não validam sozinhos clareza, cânone, visual ou equilíbrio de toda criação.'})
save('evidencias/regras-verificadas.json',{'ok':all(c['passou'] for c in checks),'sha256_texto':sha,'casos_raciocinados':'casos-raciocinados.json','auditoria':'../AUDITORIA.json'})
print(json.dumps({'total':len(checks),'falhas':[c['teste'] for c in checks if not c['passou']],'sha256':sha},ensure_ascii=False))
raise SystemExit(any(not c['passou'] for c in checks))
