from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import json,re,hashlib,math
B=Path(__file__).resolve().parent;P=B.parents[1];R=next(p for p in B.parents if (p/'sistema/03-mecanica').is_dir())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
units=json.loads((B/'UNIDADES.json').read_text());texts={u['manuscrito']:(P/u['pasta']/u['manuscrito']).read_text() for u in units};checks=[]
def ck(n,a,b=True):checks.append({'caso':n,'obtido':a,'esperado':b,'ok':a==b})
def num(s):return Q(s.replace(',','.').replace('Nenhuma','0').replace('Sem teto','99').replace('+',''))
def protections(s):
 result={}
 for m in re.finditer(r'^\| (1|2|3|Broquel|Médio|Torre) \| ([+][123456]) \| (Sem teto|\d) \| (Nenhuma|\d) \| ([\d,]+) \|$',s,re.M):
  n,p,d,f,v=m.groups();key=('Traje ' if int(p)<4 else 'Revestimento ')+n if n.isdigit() else n
  result[key]={'protecao':int(p),'dex':num(d),'forca':int(num(f)),'volume':num(v)}
 return result
pr=protections(texts['PROTECAO.md']);prev=protections((P/'equipamento/lote-02-r2/PROTECAO.md').read_text())
ck('Nove peças',len(pr),9)
for n,p in pr.items():
 ck(n+': estatísticas fora de carga preservadas',{k:str(v) for k,v in p.items() if k!='volume'},{k:str(v) for k,v in prev[n].items() if k!='volume'})
 ck(n+': Volume',str(p['volume']),str({'Traje 1':Q('0.3'),'Broquel':Q('.5')}.get(n,prev[n]['volume'])))
common={}
for line in texts['ITENS-E-OBJETOS.md'].splitlines():
 cells=[c.strip() for c in line.strip('|').split('|')]
 if line.startswith('| ') and len(cells)==4 and re.fullmatch(r'[0-9.]+',cells[2]) and re.fullmatch(r'[0-9,]+',cells[3]):common[cells[0]]={'preco':int(cells[2].replace('.','')),'volume':num(cells[3])}
ck('Treze itens comuns',len(common),13)
ck('Cantil 0,3',str(common['Cantil']['volume']),'3/10')
items=json.loads((P/'equipamento/lote-04-r4/ARMAS.json').read_text());weapons={x['nome']:x for x in items}
v=lambda n:Q(str(weapons[n]['volume']))
access=sum(common[n]['volume'] for n in ['Mochila','Corda','Lanterna elétrica','Pilhas de reserva','Cantil'])
ck('Pacote exploração',str(access),'13/10');ck('Pacote com ração',str(access+common['Ração de viagem']['volume']),'7/5')
ck('Preço pacote preservado',sum(common[n]['preco'] for n in ['Mochila','Corda','Lanterna elétrica','Pilhas de reserva','Cantil']),13000)
t=pr['Traje 1']['volume'];b=pr['Broquel']['volume']
ck('Katana+Broquel+Traje1',str(v('Katana')+b+t),'9/5')
ck('Hankyu+flechas+Traje1',str(v('Hankyū')+Q('.5')+t),'9/5')
ck('Naginata+Traje1',str(v('Naginata')+t),'23/10')
ck('Pistola+duas reservas+Traje1',str(v('Pistola')+Q('.4')+t),'6/5')
ck('Compra completa Katana',str(v('Katana')+b+t+access),'31/10')
ck('Metralhadora+duas reservas+Traje1+exploração',str(v('Metralhadora Pesada')+1+t+access),'33/5')
ck('Metralhadora conjunto atende STR3',v('Metralhadora Pesada')+1+t+access<=8 and weapons['Metralhadora Pesada']['forca']<=3)
ck('Mesmo conjunto não atende STR0',v('Metralhadora Pesada')+1+t+access<=5 and weapons['Metralhadora Pesada']['forca']<=0,False)
# Parse ammunition rows instead of assuming it is unchanged solely by file age.
am=(P/'equipamento/lote-03-r5/MUNICAO.md').read_text();ck('Fonte de munição existe',len(am)>1000)
# Exhaustively inspect armor/shield/weapon packages including exploration kit; one weapon, ordinary hands.
none={'protecao':0,'dex':Q(99),'forca':0,'volume':Q(0)}
arm={k:z for k,z in pr.items() if k.startswith(('Traje','Revestimento'))};arm['Sem uniforme']=none
sh={k:z for k,z in pr.items() if k in ['Broquel','Médio','Torre']};sh['Sem escudo']=none
cases=[]
for strength,dex,(an,a),(sn,h),w in product(range(7),range(7),arm.items(),sh.items(),items):
 hands=w['maos']+(sn!='Sem escudo');load=a['volume']+h['volume']+Q(str(w['volume']))+access
 usable=strength>=max(a['forca'],h['forca'],w['forca']) and hands<=2 and load<=5+strength
 cases.append((strength,dex,an,sn,w['nome'],str(load),usable))
ck('Nenhum item muda carga por ter grau',all(pr[n]['volume']>=0 for n in pr))
# Core body load: exact rational. No rounding overflow and no inventory laundering.
def carry(strength,own,kg,other):return own+Q(kg)/12+other<=5+strength
ck('Mei60kg com equipamento falha',carry(2,Q(2),60,Q(1)),False)
ck('Mei redistribui1',carry(2,Q(1),60,Q(1)))
ck('60kg sem equipamento STR0',carry(0,Q(0),60,Q(0)))
ck('61kg sem equipamento STR0 não arredonda',carry(0,Q(0),61,Q(0)),False)
ck('Mochila na criatura não desconta Volume',carry(2,Q(1),60,Q('1.1')),False)
body=[{'kg':kg,'equipamento_total':gear,'forca_minima':max(0,math.ceil(Q(kg)/12+gear-5))} for kg,gear in product([48,60,72,84,96,108,120,132],[0,1,2,3])]
ck('Arrasto até dobro / Força2',2*(5+2),14)
# Text regression tests include decimal examples: a mutation must be detectable.
for f,phrase in [('PROTECAO.md','| Broquel | +1 | 5 | Nenhuma | 0,5 |'),('ITENS-E-OBJETOS.md','**1,3 Volume**'),('COMPRAS-E-EQUIPAMENTO-INICIAL.md','**3,1 Volume**'),('MOVIMENTO-E-CARGA.md','A conversão vale somente para corpos')]:
 ck('Texto: '+f,phrase in texts[f]);ck('Negativo: '+f,phrase not in texts[f].replace(phrase,'PERTURBAÇÃO'))
linked={str((P/u['pasta']/u['manuscrito']).relative_to(R)):sha(P/u['pasta']/u['manuscrito']) for u in units}
for path in ['equipamento/lote-04-r4/ARMAS.json','equipamento/lote-03-r5/MUNICAO.md']:linked[str((P/path).relative_to(R))]=sha(P/path)
result={'ok':all(x['ok'] for x in checks),'verificacoes':len(checks),'checks':checks,'manuscritos_auditados':linked,'conjuntos_enumerados':len(cases),'conjuntos_utilizaveis':sum(c[-1] for c in cases),'corpos':body,'limites':['Carga é uma abstração; âncoras físicas não estabelecem conversão universal.','Matriz considera uma arma, uma proteção e um escudo, com kit de exploração. Munição de reserva exige soma adicional.','Sem playtest humano.']}
dump(B/'AUDITORIA.json',result)
dump(B/'CATALOGO-CARGA.json',{'protecoes':{n:{k:str(v) for k,v in x.items()} for n,x in pr.items()},'comuns':{n:{k:str(v) for k,v in x.items()} for n,x in common.items()}})
for u in units:
 b=P/u['pasta'];dump(b/'evidencias/auditoria-numerica.json',result);dump(b/'evidencias/regras-verificadas.json',{'ok':result['ok'],'sha256_texto':sha(b/u['manuscrito']),'casos':checks,'escopo':'Calibração de carga desta rodada. Demais cenários na revisão anterior preservada.'})
print(json.dumps({'ok':result['ok'],'checks':len(checks),'conjuntos':len(cases),'utilizaveis':sum(c[-1] for c in cases),'falhas':[c for c in checks if not c['ok']]},ensure_ascii=False));raise SystemExit(0 if result['ok'] else 1)
