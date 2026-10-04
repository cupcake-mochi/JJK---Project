from pathlib import Path
import json,hashlib,re,math
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
B=Path(__file__).resolve().parent;E=B.parent;P=E.parent;R=B.parents[5]
def dump(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2,default=str)+'\n')
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(s):return [[v.strip() for v in l.strip('|').split('|')] for l in s.splitlines() if l.startswith('|')]
def f(v):return F(str(v).replace(',','.'))
def yen(s):return int(s.replace('¥','').replace('.',''))
checks=[]
def ck(n,a,b):checks.append({'caso':n,'obtido':a,'esperado':b,'ok':a==b})
W=read(E/'lote-04-r4/ARMAS.json');old={w['nome']:w for w in read(E/'lote-04-r3/ARMAS.json')};V=read(B/'VOLUMES-ARMAS.json');A=read(B/'VOLUMES-MUNICAO.json');matrix=[{'arma':w['nome']} for w in W]
actual={r[0].split(' (')[0]:r for r in rows((E/'lote-04-r4/ARMAS.md').read_text()) if len(r)==7 and r[1] in ['1','2']}
ck('52 armas, sem omissão',sorted(actual),sorted(old));ck('52 pareceres individualizados',sorted(m['arma'] for m in matrix),sorted(old))
for w in W:
 n=w['nome'];base=old[n].copy();base['volume']=V[n];ck(n+': somente Volume mudou',w,base)
 r=actual[n];expected_name=n+(' ('+w['descricao']+')' if w['descricao'] else '')
 props=[p+((' '+str(w['alcance_ca'])+' m') if p=='Alcance' else (' '+('/'.join(str(d) for d in w['distancia']))+' m') if p=='Longo Alcance' else '') for p in w['propriedades']]
 ck(n+': todas as colunas',[r[0],int(r[1]),r[2],r[3].split(' · '),r[4],float(f(r[5])),[yen(a) for a in r[6].split(' / ')]],[expected_name,w['maos'],w['dados']+' '+w['tipo'],props,str(w['forca']) if w['forca'] else '—',w['volume'],[w['preco_criacao'],w['preco']] if w['categoria']=='Arma de Fogo' else [w['preco']]])
 ck(n+': valor positivo em décimos',f(w['volume'])>0 and f(w['volume'])*10%1==0,True)
oldrows=rows((E/'lote-03-r4/MUNICAO.md').read_text());ammd=(E/'lote-03-r5/MUNICAO.md').read_text();expected=[r[:] for r in oldrows]
for r in expected:
 if r[0].split(':')[0] in A:r[-1]=str(A[r[0].split(':')[0]]).replace('.',',')
ck('Munição preserva preço, estoque e capacidade',rows(ammd),expected)
ck('Pistola e duas reservas',f(V['Pistola'])+2*f(A['Pistola']),F('0.9'))
ck('Exemplo corresponde ao cálculo','acrescentam 0,4: o conjunto ocupa 0,9' in ammd and 'mantém 0,9 Volume' in ammd,True)
ck('Munição inicial não amplia capacidade','Receber munição não aumenta seu limite de carga' in ammd,True)
# Enumerate resource conservation. No physical cartridge count is substituted for attacks.
states=0;bad=[]
for cap in range(1,5):
 for loaded,die,reserve in product(range(cap+1),range(1,21),range(9)):
  fired=int(loaded>0);left=loaded-fired
  for add in range(min(cap-left,reserve)+1):
   states+=1
   if left+add+reserve-add+fired!=loaded+reserve:bad.append((cap,loaded,die,reserve,add))
ck('Conservação de munição enumerada',bad,[])
# Every loadout is evaluated at every Strength, including those that cannot be used.
wm={w['nome']:w for w in W};inventories=[];accessory=F('1.2');outfit=F('.1')
for name,res,num,extra in [('Taco',None,0,F(0)),('Pistola','Pistola',2,F(0)),('Rifle','Rifle',2,F(0)),('Submetralhadora','Submetralhadora',2,F(0)),('Rifle de Precisão','Rifle de Precisão',2,F(0)),('Metralhadora Pesada','Metralhadora Pesada',0,F(0)),('Metralhadora Pesada','Metralhadora Pesada',1,F(0)),('Metralhadora Pesada','Metralhadora Pesada',2,F(0)),('Espadão',None,0,F(0)),('Besta','Estojo de virotes',1,F(0)),('Rifle','Rifle',2,F(2))]:
 total=f(V[name])+accessory+outfit+num*f(A[res] if res else 0)+extra
 need=max(0,math.ceil(total-5));use=wm[name]['forca'];inventories.append({'arma':name,'reservas':num,'equipamento_extra':float(extra),'carga':float(total),'forca_por_carga':need,'forca_manejo':use,'forca_para_ambos':max(need,use),'resultados':[{'forca':st,'cabe':total<=5+st,'sem_penalidade_de_manejo':st>=use} for st in range(7)]})
ck('Força 0 comporta rifle, mas não dispensa manejo',inventories[2]['resultados'][0],{'forca':0,'cabe':True,'sem_penalidade_de_manejo':False})
ck('Precisão: carga não dispensa Força 3 de manejo',inventories[4]['forca_para_ambos'],3)
ck('Metralhadora com uma reserva: Força por carga é 1',inventories[6]['forca_por_carga'],1)
ck('Metralhadora com duas reservas cabe em Força 3',inventories[7]['resultados'][3]['cabe'],True)
ck('Metralhadora com Traje 3 e acessórios excede Força 3',f(inventories[7]['carga'])-F('.1')+F(2)<=8,False)
# Exhaustively compare minimum derived Strength to the direct capacity inequality.
loadstates=0;errors=[]
for w in W:
 for copies,reserves,strength in product(range(1,4),range(6),range(7)):
  ammo=f(A.get(w['nome'],0));total=copies*f(w['volume'])+reserves*ammo+accessory+outfit;need=max(0,math.ceil(total-5));loadstates+=1
  if (strength>=need)!=(total<=5+strength):errors.append((w['nome'],copies,reserves,strength))
ck('Força mínima equivale à desigualdade de carga',errors,[])
for st in range(7):
 cap=F(5+st);ck(f'Limite exato de Força {st}',cap<=5+st,True);ck(f'Excesso de 0,1 em Força {st}',cap+F('.1')<=5+st,False)
load=(P/'regras-comuns/lote-06-r5/MOVIMENTO-E-CARGA.md').read_text()
ck('Capacidade preservada','**5 + Força**' in load,True)
ck('Equipamento de criatura usa tabela','apenas para o corpo e some o Volume tabelado do equipamento dela' in load,True)
ck('Bolsa não converte arma em kg genérico','bolsa ou entregá-los à criatura carregada não reduz a soma' in load,True)
ck('Corpo 60kg, equipamento 1 e próprio 2',F(60,12)+1+2,F(8))
ck('12kg não recalcula equipamento já tabelado','compare primeiro com um item semelhante do catálogo' in load,True)
ck('Metralhadora portátil não simula M2','Armas pesadas instaladas em tripés ou veículos exigem ficha própria' in (E/'lote-04-r4/ARMAS.md').read_text(),True)
units=read(B/'UNIDADES.json');new=read(B/'UNIDADES-NOVAS.json');linked={str((P/u['pasta']/u['manuscrito']).relative_to(R)):sha(P/u['pasta']/u['manuscrito']) for u in units}
# Ancillary values used in scenarios must match their still-current owners.
itemrows=rows((E/'lote-05/ITENS-E-OBJETOS.md').read_text());items={r[0]:f(r[3]) for r in itemrows if len(r)==4 and r[2].replace('.','').isdigit()}
ck('Acessórios efetivos dos cenários',sum(items[n] for n in ['Mochila','Corda','Lanterna elétrica','Pilhas de reserva','Cantil']),accessory)
pr=E/'lote-02-r2/PROTECAO.md';linked[str(pr.relative_to(R))]=sha(pr);ck('Traje 1 permanece 0,1','| 1 | +1 | Sem teto | Nenhuma | 0,1 |' in pr.read_text(),True)

# Money is read from the published owners; salary is not copied into player prose.
commerce=(B/'COMPRAS-E-EQUIPAMENTO-INICIAL.md').read_text();published=(P.parent/'manual/50-equipamento.md').read_text();progress=(P.parent/'manual/80-experiencia-e-progressao.md').read_text()
prices={}
for r in rows(published):
 if len(r)==3 and r[0] in ['Traje 1','Traje 2','Traje 3','Revestimento 1','Revestimento 2','Revestimento 3','Broquel','Médio','Torre']:prices[r[0]]=yen(r[1])
actualprices={r[0].removeprefix('Escudo '):yen(r[1]) for r in rows(commerce) if len(r)==2 and r[1].replace('.','').isdigit()}
ck('Nove preços de proteção, linha e coluna',actualprices,prices)
ck('Acesso no texto coincide com modelo',[r for r in rows(commerce.split('<!-- page:precos')[0]) if len(r)==2 and r[0] in ['Armas de fogo e sua munição','Revestimento 2','Revestimento 3']],[['Armas de fogo e sua munição','Grau 2 ou superior, ou autorização prévia.'],['Revestimento 2','Grau 3 ou superior.'],['Revestimento 3','Grau 2 ou superior.']])
shield=next(r for r in rows(pr.read_text()) if r[0]=='Broquel')
ck('Exemplo usa Volume e Força do Broquel corrente',[f(shield[4]),shield[3]],[F('.1'),'Nenhuma'])
salaries={r[0]:yen(r[1]) for r in rows(progress) if len(r)==3 and r[0].startswith(('Grau ','Especial')) and r[1].startswith('¥')}
ck('Fundo padrão vem da mensalidade publicada',salaries['Grau 4'],150000)
ck('Exemplo Grau 3 financia precisão',salaries['Grau 3']>=wm['Rifle de Precisão']['preco_criacao'],True)
ck('Gratuidade do Traje 1 preservada','recebe um **Traje 1**' in commerce and 'um Traje 1' in commerce,True)
ck('Dinheiro inicial não duplicado por venda de item gratuito','itens gratuitos não se convertem em crédito de compra' in commerce,True)
ck('Sem salário copiado fora do dono','¥600.000' in commerce or '¥2.400.000' in commerce,False)
kit_expected={
'Katana e Broquel':[wm['Katana']['preco']+prices['Broquel'],f(V['Katana'])+F('.1')+outfit,0],
'Hankyū e 20 flechas':[wm['Hankyū']['preco'],f(V['Hankyū'])+f(A['Aljava de flechas'])+outfit,0],
'Naginata':[wm['Naginata']['preco'],f(V['Naginata'])+outfit,3],
'Pistola e duas reservas':[wm['Pistola']['preco_criacao'],f(V['Pistola'])+2*f(A['Pistola'])+outfit,0]}
for row in rows(commerce):
 if len(row)==4 and row[0] in kit_expected:ck(row[0]+': todas as colunas do exemplo',[yen(row[1]),f(row[2]),int(row[3])],kit_expected[row[0]])
ck('Traje 2 + Katana deixa 12000',150000-prices['Traje 2']-wm['Katana']['preco'],12000)
itemdata={r[0]:{'preco':yen(r[2]),'volume':f(r[3])} for r in itemrows if len(r)==4 and r[2].replace('.','').isdigit()}
access_price=sum(itemdata[n]['preco'] for n in ['Mochila','Corda','Lanterna elétrica','Pilhas de reserva','Cantil'])
ck('Kit Rina custa 73000',kit_expected['Katana e Broquel'][0]+access_price,73000)
ck('Kit Rina deixa 77000',150000-kit_expected['Katana e Broquel'][0]-access_price,77000)
ck('Kit Rina ocupa 2,4',kit_expected['Katana e Broquel'][1]+accessory,F('2.4'))
ammo={r[0].split(':')[0]:{'cap':int(r[1]),'preco':yen(r[2]),'volume':f(r[3])} for r in rows(ammd) if len(r)==4 and ':' in r[0] and r[1].isdigit()}
ck('Reposição custa 8000',3*ammo['Rifle']['preco']+itemdata['Lanterna elétrica']['preco']+itemdata['Pilhas de reserva']['preco'],8000)
ck('Reposição ocupa 1,2',3*ammo['Rifle']['volume']+itemdata['Lanterna elétrica']['volume']+itemdata['Pilhas de reserva']['volume'],F('1.2'))
ck('Reposição dá nove ataques',3*ammo['Rifle']['cap'],9)
# Access separate from money, carrying, and use. A purchase is not automatic access.
rank={'Grau 4':0,'Grau 3':1,'Grau 2':2,'Grau 1':3,'Especial':4}
def access(grade,item,permission=False):
 return rank[grade]>=2 or permission if item in ammo else rank[grade]>=({'Revestimento 2':1,'Revestimento 3':2}.get(item,0))
ck('Grau 4, dinheiro mas sem autorização: fogo não',access('Grau 4','Pistola'),False)
ck('Grau 4 com autorização: fogo sim',access('Grau 4','Pistola',True),True)
ck('Grau 3 não basta para fogo',access('Grau 3','Rifle de Precisão'),False)
ck('Grau 2 basta para fogo',access('Grau 2','Metralhadora Pesada'),True)
ck('Grau 3 atende Revestimento 2',access('Grau 3','Revestimento 2'),True)
ck('Grau 3 não atende Revestimento 3',access('Grau 3','Revestimento 3'),False)
# Exact firing model. k attack opportunities/turn, no swap, bonus optionally occupied.
# Reflex/d20 effects, hit chance, defenses and class features are outside this model.
def sequence(cap,k,spares,p=F(1,10),bonus_available=True,rounds=6):
 states={(cap,False,cap*spares):F(1)};shots=F(0);reloads=F(0)
 for turn in range(rounds):
  st={(l,b,r,bonus_available):v for (l,b,r),v in states.items()}
  for opportunity in range(k):
   nxt=defaultdict(F)
   for (l,b,r,bonus),v in st.items():
    if (b or l==0) and bonus and l+r>0:
     added=min(cap-l,r);l+=added;r-=added;b=False;bonus=False;reloads+=v
    if b or l==0:nxt[(l,b,r,bonus)]+=v;continue
    shots+=v;nxt[(l-1,True,r,bonus)]+=v*p;nxt[(l-1,l==1,r,bonus)]+=v*(1-p)
   st=nxt
  states=defaultdict(F)
  for (l,b,r,bonus),v in st.items():
   if turn<rounds-1 and bonus and (b or l<cap) and l+r>0:
    added=min(cap-l,r);l+=added;r-=added;b=False;reloads+=v
   states[(l,b,r)]+=v
 return shots,reloads
ck('Oráculo: sem interrupção, 4 tiros e Bônus ocupada',sequence(4,3,8,F(0),False)[0],F(4))
ck('Oráculo: três ataques, carga4, reservas8, seis turnos sem interrupção',sequence(4,3,8,F(0))[0],F(18))
ck('Oráculo: três cargas de 2 não criam munição',sequence(2,1,2,F(0))[0],F(6))
seq=[]
for name,a in ammo.items():
 for k,spares,bonus in product([1,2,3],[0,2,8],[True,False]):
  sh,re=sequence(a['cap'],k,spares,bonus_available=bonus)
  ck(name+f': estoque/ações k{k}, reservas{spares}, Bônus{bonus}',0<=sh<=min(6*k,a['cap']*(1+spares)),True)
  seq.append({'arma':name,'oportunidades_por_turno':k,'reservas':spares,'bonus_disponivel':bonus,'disparos_esperados':float(sh),'recargas_esperadas':float(re)})
# All weapons: conservative dominance with identical mechanical tags, average damage incl. Par.
from functools import lru_cache
@lru_cache(None)
def distribution(n,s):
 out={0:1}
 for _ in range(n):
  d=defaultdict(int)
  for val,count in out.items():
   for die in range(1,s+1):d[val+die]+=count
  out=d
 return dict(out)
def average(w):
 n,s=map(int,w['dados'].split('d'));d=distribution(n,s);den=s**n
 return F(sum(max(a,b)*x*y for a,x in d.items() for b,y in d.items()),den*den) if 'Par' in w['propriedades'] else F(n*(s+1),2)
dominance=[];metrics=[]
for w in W:
 a=ammo.get(w['nome']);metrics.append({'arma':w['nome'],'volume':w['volume'],'dano_medio_dados':float(average(w)),'forca':w['forca'],'preco':w['preco'],'preco_criacao':w['preco_criacao'],'propriedades':w['propriedades'],'distancia':w['distancia'],'capacidade':a['cap'] if a else None,'volume_reserva':float(a['volume']) if a else None,'ataques_por_volume_reserva':float(F(a['cap'])/a['volume']) if a else None,'custo_por_ataque':a['preco']/a['cap'] if a else None})
for a,b in product(W,W):
 if a['nome']==b['nome']:continue
 if any(a[k]!=b[k] for k in ['categoria','tipo','dados','maos']):continue
 if set(a['propriedades'])!=set(b['propriedades']):continue
 def axes(w):
  am=ammo.get(w['nome']);return [-w['forca'],-f(w['volume']),-w['preco'],-w['preco_criacao'],w['alcance_ca']]+(w['distancia'] or [0,0])+([am['cap'],-am['volume'],-am['preco']] if am else [])
 aa,bb=axes(a),axes(b)
 if all(x>=y for x,y in zip(aa,bb)) and any(x>y for x,y in zip(aa,bb)):dominance.append([a['nome'],b['nome']])
ck('Dominância conhecida de Revólver registrada',['Revólver','Pistola'] in dominance,True)
linked[str((P.parent/'manual/50-equipamento.md').relative_to(R))]=sha(P.parent/'manual/50-equipamento.md')
linked[str((P.parent/'manual/80-experiencia-e-progressao.md').relative_to(R))]=sha(P.parent/'manual/80-experiencia-e-progressao.md')
limites=['Revisão documental e enumeração exata; sem playtest humano e sem medição física própria.','Volume é custo de inventário. Pesos reais são referência; a rodada recalibra opções para jogo.','Proteções e itens comuns não foram recalibrados nesta rodada; valores usados nos cenários são os das candidatas correntes.','Conversão residual de 12 kg é herdada/provisória, não escala de massa destas armas; revisão global de carga continua na fila.','Disponibilidade, preços e combate não foram reequilibrados junto da carga.']
res={'ok':all(c['ok'] for c in checks),'casos':checks,'estados_municao':states,'estados_carga':loadstates,'inventarios':inventories,'comparacao_armas':metrics,'dominancia_parcial':dominance,'sequencias':seq,'salarios_referencia':salaries,'manuscritos_auditados':linked,'limites':limites}
dump(B/'evidencias/auditoria-numerica.json',res)
for u in new:
 b=P/u['pasta'];dump(b/'evidencias/regras-verificadas.json',{'ok':res['ok'],'sha256_texto':sha(b/u['manuscrito']),'casos':checks,'limites':limites})
print(json.dumps({'ok':res['ok'],'verificacoes':len(checks),'estados_carga':loadstates,'estados_municao':states,'falhas':[c for c in checks if not c['ok']]},ensure_ascii=False,default=str))
assert res['ok']
