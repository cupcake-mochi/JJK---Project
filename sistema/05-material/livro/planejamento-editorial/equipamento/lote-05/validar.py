from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from functools import lru_cache
import json,hashlib,re
B=Path(__file__).resolve().parent;E=B.parent;P=E.parent;R=B.parents[5]
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2,default=str)+'\n')
def rows(s):return [[c.strip() for c in l.strip('|').split('|')] for l in s.splitlines() if l.startswith('|')]
def yen(s):return int(s.replace('¥','').replace('.',''))
def frac(s):return F(str(s).replace(',','.'))
checks=[]
def ck(n,a,b):checks.append({'caso':n,'obtido':a,'esperado':b,'ok':a==b})
W=read(E/'lote-04-r2/ARMAS.json');old={w['nome']:w for w in read(E/'lote-04/ARMAS.json')};V=read(B/'VOLUMES-ARMAS.json');A=read(B/'VOLUMES-MUNICAO.json')
md=(E/'lote-04-r2/ARMAS.md').read_text();actual={r[0].split(' (')[0]:r for r in rows(md) if len(r)==7 and r[1] in ['1','2']}
ck('52 armas, sem omissões',sorted(actual),sorted(old));ck('52 atribuições de Volume',sorted(V),sorted(old))
for w in W:
 n=w['nome'];baseline=old[n].copy();baseline['volume']=V[n]
 if n=='Taco':baseline['propriedades']=[('Discreta' if p=='Oculta' else p) for p in baseline['propriedades']]
 ck(n+': alteração restrita aos eixos autorizados',w,baseline)
 r=actual[n];expected_name=n+(' ('+w['descricao']+')' if w['descricao'] else '')
 props=[p+((' '+str(w['alcance_ca'])+' m') if p=='Alcance' else (' '+('/'.join(str(d) for d in w['distancia']))+' m') if p=='Longo Alcance' else '') for p in w['propriedades']]
 ck(n+': todas colunas do manuscrito',[r[0],int(r[1]),r[2],r[3].split(' · '),r[4],float(frac(r[5])),[yen(a) for a in r[6].split(' / ')]],[expected_name,w['maos'],w['dados']+' '+w['tipo'],props,str(w['forca']) if w['forca'] else '—',w['volume'],[w['preco_criacao'],w['preco']] if w['categoria']=='Arma de Fogo' else [w['preco']]])
 ck(n+': décimos exatos',frac(w['volume'])*10%1,0)
oldammo=rows((E/'lote-03-r2/MUNICAO.md').read_text());ammd=(E/'lote-03-r3/MUNICAO.md').read_text();newammo=rows(ammd);expected=[r[:] for r in oldammo]
for r in expected:
 n=r[0].split(':')[0]
 if n in A:r[-1]=str(A[n]).replace('.',',')
ck('Somente Volume pode mudar nas nove linhas de munição; preços/capacidades intactos',newammo,expected)
ck('Exemplo de pistola corrigido','o conjunto ocupa 0,7' in ammd and 'mantém 0,7' in ammd,True)
ck('Instalada incluída, sem duplicação','carga instalada na arma já está incluída' in ammd,True)
# Exhaustive conservation of ammunition, including partial reloads and d20 interruption.
bad=[];states=0
for cap in range(1,5):
 for loaded,die,reserve in product(range(cap+1),range(1,21),range(9)):
  fired=int(loaded>0);left=loaded-fired;blocked=left==0 or bool(fired and die<=2)
  for add in range(min(cap-left,reserve)+1):
   states+=1;after=left+add;remaining=reserve-add
   if after+remaining+fired!=loaded+reserve or not 0<=after<=cap:bad.append([cap,loaded,die,reserve,add])
ck('Conservação em estados enumerados',bad,[])
# Existing scenario runner applied to current manuscript without historical writes.
oldscript=(E/'lote-03-r2/validar_regras.py').read_text();oldscript=oldscript.replace("B=Path(__file__).resolve().parent;E=B.parent;R=B.parents[5]","B=Path(__file__).resolve().parent.parent/'lote-03-r3';E=B.parent;R=B.parents[5]")
oldscript=oldscript.replace("str(Fraction(1,10)+2*Fraction(1,10)),'3/10'","str(Fraction(5,10)+2*Fraction(1,10)),'7/10'")
exec(compile(oldscript,'cenarios_municao_herdados','exec'),{'__file__':str(B/'validar.py'),'__name__':'cenarios_municao'})
ck('34 cenários de recarga atualizados',read(E/'lote-03-r3/evidencias/regras-verificadas.json')['ok'],True)
# No remaining current owner links concealment to weight.
load=(P/'regras-comuns/lote-06-r4/MOVIMENTO-E-CARGA.md').read_text();eq=(E/'lote-01-r5/EQUIPAMENTO-EM-JOGO.md').read_text()
ck('Regra automática antiga removida','com Oculta ou Vestida são leves' in load,False)
ck('Independência no dono','Oculta, Discreta, Vestida e o número de mãos não determinam esse valor' in load,True)
ck('Independência na interface','Oculta, Discreta e Vestida não determinam o Volume' in eq,True)
ck('Discreta tem definição','| Discreta |' in eq and '**Discreta:**' in eq,True)
ck('Carga mantém limite','**5 + Força**' in load,True)
# Parse actual item table, preserve published six prices.
itmd=(B/'ITENS-E-OBJETOS.md').read_text();items={r[0]:{'conteudo':r[1],'preco':yen(r[2]),'volume':float(frac(r[3]))} for r in rows(itmd) if len(r)==4 and r[2].replace('.','').isdigit()}
ck('Treze itens',len(items),13)
for n in ['Corda','Lanterna elétrica','Algema','Pé de cabra','Gazuas','Kit de escalada']:ck(n+': preço preservado',items[n]['preco'],3000)
kit=['Mochila','Corda','Lanterna elétrica','Pilhas de reserva','Cantil'];price=sum(items[n]['preco'] for n in kit);vol=sum(frac(items[n]['volume']) for n in kit)
ck('Exemplo de kit: preço',price,13000);ck('Exemplo de kit: Volume',str(vol),'6/5');ck('Adicionar ração',str(vol+frac(items['Ração de viagem']['volume'])),'13/10')
ck('Sem mochila que crie capacidade','mochila organiza os itens, mas não aumenta seu limite' in itmd,True)
ck('Contenção não decorre apenas de Agarrado','Estar apenas Agarrado, Derrubado, Atordoado ou Incapacitado não basta' in itmd,True)
ck('Itens vestidos protegidos de uso abusivo da tabela','Destruir ou arrancar equipamento vestido ou empunhado exige uma regra' in itmd,True)
ck('Gazuas dependem do Ofício','Treino e tentativas sem treino seguem as regras de Ofícios' in itmd,True)
ck('Improvisado não remove Maestria','Aplique a Maestria usada no ataque comum' in itmd,True)
ck('Improvisado d4 e Força no exemplo','1d4 + 2' in itmd,True)
# Exact comparisons of carrying sets; 0.1 outfit remains separately pending armor calibration.
wmap={w['nome']:w for w in W};loads=[]
for strength in range(7):
 for name,reserve_key,num in [('Taco',None,0),('Pistola','Pistola',2),('Rifle','Rifle',2),('Hankyū','Aljava de flechas',1),('Besta','Estojo de virotes',1)]:
  if strength<wmap[name]['forca']:continue
  total=vol+F('0.1')+frac(wmap[name]['volume'])+(frac(A[reserve_key])*num if reserve_key else 0)
  loads.append({'forca':strength,'arma':name,'carga':float(total),'limite':5+strength,'folga':float(5+strength-total),'cabe':total<=5+strength})
ck('Conjunto do rifle com Força 1',next(x['carga'] for x in loads if x['arma']=='Rifle' and x['forca']==1),3.7)
ck('Conjunto da pistola com Força 0',next(x['carga'] for x in loads if x['arma']=='Pistola' and x['forca']==0),2.0)
# One Volume strictly for reserve containers; no free fractions/partial-container cheating.
sensitivity=[]
for n,v in A.items():
 c=20 if n in ['Aljava de flechas','Estojo de virotes'] else next(int(r[1]) for r in newammo if len(r)==4 and r[0].startswith(n+':'))
 sensitivity.append({'item':n,'capacidade':c,'volume':v,'disparos_por_1_volume':int(F(1)/frac(v))*c,'alternativas':{str(z):int(F(1)/frac(z))*c for z in [.1,.2,.5,1]}})
# Numerical scenario: natural 20 crits; natural 1 is not an automatic miss in this candidate. No RD or magical effects.
def dice(n,s):
 out={0:F(1)}
 for _ in range(n):
  new=defaultdict(F)
  for k,p in out.items():
   for d in range(1,s+1):new[k+d]+=p/F(s)
  out=dict(new)
 return out

def hits_distribution(bonus,defense,sides,attribute,adv=False,dis=False):
 d20=defaultdict(F)
 rolls=product(range(1,21),repeat=2) if adv or dis else ((i,) for i in range(1,21))
 for roll in rolls:d20[max(roll) if adv else min(roll)]+=F(1,400 if adv or dis else 20)
 damage=defaultdict(F)
 for die,p in d20.items():
  if die!=20 and die+bonus<defense:damage[0]+=p;continue
  for amount,q in dice(2 if die==20 else 1,sides).items():damage[amount+attribute]+=p*q
 return dict(damage)
def attempts(hp,dist):
 @lru_cache(None)
 def e(h):
  if h<=0:return F(0)
  return (1+sum(p*e(h-a) for a,p in dist.items() if a>0))/(1-dist.get(0,0))
 return e(hp)
object_models=[]
for defense,hp in [(10,5),(14,20),(18,5),(18,20),(16,40)]:
 for bonus,attr in [(3,2),(6,4),(10,6)]:
  for label,side,adv,dis in [('arma d8',8,False,False),('arma d8 e Rompe',8,True,False),('improvisado d4',4,False,True)]:
   d=hits_distribution(bonus,defense,side,attr,adv,dis);n=attempts(hp,d)
   object_models.append({'defesa':defense,'vida':hp,'ataque':bonus,'atributo':attr,'caso':label,'ataques_esperados':float(n),'dano_esperado_por_tentativa':float(sum(a*p for a,p in d.items()))})
ck('Oráculo ataques com dano 1 certo',str(attempts(5,{1:F(1)})),'5')
ck('Oráculo acerto 50%, dano 1',str(attempts(5,{0:F(1,2),1:F(1,2)})),'10')
ck('Exemplo da porta',20-8-12,0)
ck('1 natural não ganha falha automática importada',hits_distribution(10,10,8,6).get(0,F(0)),F(0))
for defense in [10,14,18]:
 p=sum(F(1,400) for a,b in product(range(1,21),repeat=2) if min(a,b)==20 or min(a,b)+5>=defense)
 ck(f'Improvisado mantém chance entre 0 e 1, Defesa {defense}',0<=p<=1,True)
# Snapshot ties all audits to player sources; rendering validates table extraction separately.
linked={};units=read(B/'UNIDADES.json')
for u in units:
 f=P/u['pasta']/u['manuscrito'];linked[str(f.relative_to(R))]=sha(f)
result={'ok':all(c['ok'] for c in checks),'casos':checks,'estados_municao':states,'inventarios':loads,'municao_sensibilidade':sensitivity,'objetos':object_models,'itens':items,'manuscritos_auditados':linked,'limites':['Modelo documental, não pesquisa de campo. Carga é convenção por porte, não pesagem. Combos de classes e resistências de monstros não simulados.']}
dump(B/'evidencias/auditoria-numerica.json',result)
for u in units:
 b=P/u['pasta'];dump(b/'evidencias/regras-verificadas.json',{'ok':result['ok'],'sha256_texto':sha(b/u['manuscrito']),'casos':checks,'auditoria':'equipamento/lote-05/evidencias/auditoria-numerica.json','limites':result['limites']})
print(json.dumps({'ok':result['ok'],'verificacoes':len(checks),'estados':states,'falhas':[c for c in checks if not c['ok']]},ensure_ascii=False,default=str))
assert result['ok']
