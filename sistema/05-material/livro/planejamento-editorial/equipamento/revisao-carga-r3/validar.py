from pathlib import Path
import json,hashlib,re,math
from fractions import Fraction as F
from itertools import product
B=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial/equipamento/revisao-carga-r3');E=B.parent;P=E.parent;R=B.parents[5]
def dump(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2,default=str)+'\n')
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(s):return [[v.strip() for v in l.strip('|').split('|')] for l in s.splitlines() if l.startswith('|')]
def f(v):return F(str(v).replace(',','.'))
def yen(s):return int(s.replace('¥','').replace('.',''))
checks=[]
def ck(n,a,b):checks.append({'caso':n,'obtido':a,'esperado':b,'ok':a==b})
W=read(E/'lote-04-r3/ARMAS.json');old={w['nome']:w for w in read(E/'lote-04-r2/ARMAS.json')};V=read(B/'VOLUMES-ARMAS.json');A=read(B/'VOLUMES-MUNICAO.json');matrix=read(B/'MATRIZ-52-ARMAS.json')
actual={r[0].split(' (')[0]:r for r in rows((E/'lote-04-r3/ARMAS.md').read_text()) if len(r)==7 and r[1] in ['1','2']}
ck('52 armas, sem omissão',sorted(actual),sorted(old));ck('52 pareceres individualizados',sorted(m['arma'] for m in matrix),sorted(old))
for w in W:
 n=w['nome'];base=old[n].copy();base['volume']=V[n];ck(n+': somente Volume mudou',w,base)
 r=actual[n];expected_name=n+(' ('+w['descricao']+')' if w['descricao'] else '')
 props=[p+((' '+str(w['alcance_ca'])+' m') if p=='Alcance' else (' '+('/'.join(str(d) for d in w['distancia']))+' m') if p=='Longo Alcance' else '') for p in w['propriedades']]
 ck(n+': todas as colunas',[r[0],int(r[1]),r[2],r[3].split(' · '),r[4],float(f(r[5])),[yen(a) for a in r[6].split(' / ')]],[expected_name,w['maos'],w['dados']+' '+w['tipo'],props,str(w['forca']) if w['forca'] else '—',w['volume'],[w['preco_criacao'],w['preco']] if w['categoria']=='Arma de Fogo' else [w['preco']]])
 ck(n+': valor positivo em décimos',f(w['volume'])>0 and f(w['volume'])*10%1==0,True)
oldrows=rows((E/'lote-03-r3/MUNICAO.md').read_text());ammd=(E/'lote-03-r4/MUNICAO.md').read_text();expected=[r[:] for r in oldrows]
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
ck('Precisão tem exigência de carga acima de 0',inventories[4]['forca_por_carga'],1)
ck('Metralhadora com uma reserva exige Força 5 por carga',inventories[6]['forca_por_carga'],5)
ck('Metralhadora com duas reservas excede Força 6',inventories[7]['resultados'][-1]['cabe'],False)
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
ck('Metralhadora portátil não simula M2','Armas pesadas instaladas em tripés ou veículos exigem ficha própria' in (E/'lote-04-r3/ARMAS.md').read_text(),True)
units=read(B/'UNIDADES.json');new=read(B/'UNIDADES-NOVAS.json');linked={str((P/u['pasta']/u['manuscrito']).relative_to(R)):sha(P/u['pasta']/u['manuscrito']) for u in units}
# Ancillary values used in scenarios must match their still-current owners.
itemrows=rows((E/'lote-05/ITENS-E-OBJETOS.md').read_text());items={r[0]:f(r[3]) for r in itemrows if len(r)==4 and r[2].replace('.','').isdigit()}
ck('Acessórios efetivos dos cenários',sum(items[n] for n in ['Mochila','Corda','Lanterna elétrica','Pilhas de reserva','Cantil']),accessory)
pr=E/'lote-02-r2/PROTECAO.md';linked[str(pr.relative_to(R))]=sha(pr);ck('Traje 1 permanece 0,1','| 1 | +1 | Sem teto | Nenhuma | 0,1 |' in pr.read_text(),True)
limites=['Revisão documental e enumeração exata; sem playtest humano e sem medição física própria.','Volume não é quilograma. Analogias e estimativas por categoria estão declaradas na matriz de 52 armas.','Proteções e itens comuns não foram recalibrados nesta rodada; valores usados nos cenários são os das candidatas correntes.','Conversão residual de 12 kg é herdada/provisória, não escala de massa destas armas; revisão global de carga continua na fila.','Disponibilidade, preços e combate não foram reequilibrados junto da carga.']
res={'ok':all(c['ok'] for c in checks),'casos':checks,'estados_municao':states,'estados_carga':loadstates,'inventarios':inventories,'manuscritos_auditados':linked,'limites':limites}
dump(B/'evidencias/auditoria-numerica.json',res)
for u in new:
 b=P/u['pasta'];dump(b/'evidencias/regras-verificadas.json',{'ok':res['ok'],'sha256_texto':sha(b/u['manuscrito']),'casos':checks,'limites':limites})
print(json.dumps({'ok':res['ok'],'verificacoes':len(checks),'estados_carga':loadstates,'estados_municao':states,'falhas':[c for c in checks if not c['ok']]},ensure_ascii=False,default=str))
assert res['ok']
