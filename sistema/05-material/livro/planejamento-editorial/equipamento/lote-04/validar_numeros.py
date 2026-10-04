"""Auditoria documental e enumeração exata. Não representa playtest nem todas as classes."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter,defaultdict
from functools import lru_cache
import re,json,hashlib,runpy
B=Path(__file__).resolve().parent;E=B.parent;R=B.parents[5]
W=json.loads((B/'ARMAS.json').read_text());md=(B/'ARMAS.md').read_text()
source=(R/'sistema/05-material/livro/manual/50-equipamento.md').read_text()
checks=[]
def ck(n,a,b):checks.append({'caso':n,'obtido':a,'esperado':b,'ok':a==b})
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def cells(s):return [re.sub(r'[`*]','',c).strip() for c in s.strip('|').split('|')]
def money(s):return int(s.replace('¥','').replace('.','').strip())
def rows(s):return [cells(l) for l in s.splitlines() if l.startswith('|')]
base={};training=None
for c in rows(source.split('### Armas por treino')[1].split('### Lâmina Curta')[0]):
 if c[0].startswith('Treino '):training=c[0]
 if len(c)==7 and c[2] in ('1','2'):base[c[0]]=(c,training)
ck('52 identidades, sem duplicação',len(W),52);ck('Conjunto de armas',sorted(x['nome'] for x in W),sorted(base))
actual={c[0].split(' (')[0]:c for c in rows(md) if len(c)==7 and c[1] in ('1','2')}
ck('52 linhas no manuscrito',len(actual),52)
prices={};creation={}
for c in rows(source.split('### Preços')[1].split('### Carga')[0]):
 if len(c)==3 and re.fullmatch(r'[\d.]+',c[1]):
  for n in c[2].split(' · '):prices[n]=money(c[1])
 elif len(c)==2 and re.fullmatch(r'[\d.]+',c[1]):prices[c[0]]=money(c[1])
 elif len(c)==4 and re.fullmatch(r'[\d.]+',c[1]) and re.fullmatch(r'[\d.]+',c[2]):
  for n in c[0].split(' · '):creation[n]=money(c[1]);prices[n]=money(c[2])
ranges={c[0]:[int(c[1].split()[0]),int(c[2].split()[0])] for c in rows(source.split('**Armas de tiro**')[1].split('**Armas de arremesso**')[0]) if len(c)==3 and re.fullmatch(r'\d+ m',c[1])}
changed=[]
for w in W:
 n=w['nome'];c,t=base[n];a=actual[n];dice=c[3] if c[3][0].isdigit() else '1'+c[3]
 expected=[c[1],t,int(c[2]),dice,sorted(c[4].split(' · ')),0 if c[5]=='—' else int(c[5]),.1 if c[6]=='leve' else int(c[6]),prices[n],creation.get(n,prices[n])]
 ck(n+': colunas da base',[w[k] for k in ['categoria','treino','maos','dados']]+[sorted(w['propriedades'])]+[w[k] for k in ['forca','volume','preco','preco_criacao']],expected)
 props=[p+((' '+str(w['alcance_ca'])+' m') if p=='Alcance' else (' '+('/'.join(str(d) for d in w['distancia']))+' m') if p=='Longo Alcance' else '') for p in w['propriedades']]
 price=[money(v) for v in a[6].split(' / ')]
 ck(n+': tabela do leitor',[int(a[1]),a[2],a[3].split(' · '),a[4],float(a[5].replace(',','.')),price],[w['maos'],w['dados']+' '+w['tipo'],props,str(w['forca']) if w['forca'] else '—',w['volume'],[w['preco_criacao'],w['preco']] if n in creation else [w['preco']]])
 ck(n+': distância preservada',w['distancia'],ranges.get(n,[6,18] if 'Longo Alcance' in w['propriedades'] else None))
 ck(n+': tipo físico válido',w['tipo'] in ['Cortante','Concussão','Perfurante'],True)
 ck(n+': medidas múltiplas de 1,5',all(F(str(d))%F('1.5')==0 for d in [w['alcance_ca']]+(w['distancia'] or [])),True)
 if 'Alcance' in w['propriedades'] and w['categoria']!='Armas Longas':changed.append(n)
ck('Oito correções de alcance',len(changed),8)
ck('Treinos preservados',dict(Counter(w['treino'] for w in W)),dict(Counter(v[1] for v in base.values())))
@lru_cache(None)
def dist(n,s):
 d={0:1}
 for _ in range(n):
  new=defaultdict(int)
  for a,count in d.items():
   for i in range(1,s+1):new[a+i]+=count
  d=dict(new)
 return d

def mean(n,s,par=False):
 d=dist(n,s);den=s**n
 return F(sum(max(a,b)*x*y for a,x in d.items() for b,y in d.items()),den*den) if par else F(sum(a*x for a,x in d.items()),den)
ck('Oráculo d6',str(mean(1,6)),'7/2');ck('Oráculo Par d6',str(mean(1,6,True)),'161/36')
metrics=[]
for w in W:
 n,s=map(int,w['dados'].split('d'));p='Par' in w['propriedades'];normal=mean(n,s,p);crit=mean(n*2,s,p)
 attr=w['categoria'] not in ['Balestra','Arma de Fogo']
 metrics.append({'arma':w['nome'],'normal':float(normal),'critico':float(crit),'exato_normal':str(normal),'exato_critico':str(crit),'com_atributo_0_a_6':[float(normal+i) if attr else float(normal) for i in range(7)],'versatil_2_maos':float(mean(n,min(s+2,12),p)) if 'Versátil' in w['propriedades'] else None})
ck('Par multidados 2d6',str(mean(2,6,True)),'5425/648')
# Dominância conservadora: mesma categoria, tipo, dado, mãos e propriedades.
# Só declara comparação quando todos os demais eixos são iguais ou melhores.
dominance=[];duplicates=[]
for i,a in enumerate(W):
 for b in W[i+1:]:
  if (a['categoria'],a['tipo'],a['dados'],a['maos'],set(a['propriedades']))!=(b['categoria'],b['tipo'],b['dados'],b['maos'],set(b['propriedades'])):continue
  def axes(w):return [-w['forca'],-w['volume'],-w['preco'],-w['preco_criacao'],w['alcance_ca']]+(w['distancia'] or [0,0])
  aa,bb=axes(a),axes(b)
  if aa==bb:duplicates.append([a['nome'],b['nome']])
  elif all(x>=y for x,y in zip(aa,bb)):dominance.append([a['nome'],b['nome']])
  elif all(x<=y for x,y in zip(aa,bb)):dominance.append([b['nome'],a['nome']])
ck('Caso conhecido: revólver supera pistola no alcance',['Revólver','Pistola'] in dominance,True)
# Ammo rows: columns preserved except approved-for-discussion burden proposal.
oldrows=rows((E/'lote-03/MUNICAO.md').read_text());newrows=rows((E/'lote-03-r2/MUNICAO.md').read_text());expect=[r[:] for r in oldrows]
for r in expect:
 if r[0] in ('Aljava de flechas','Estojo de virotes'):r[-1]='0,2'
ck('Munição: somente dois Volumes alterados',newrows,expect)
ammo=[]
for c in newrows:
 if len(c)==4 and ':' in c[0] and c[1].isdigit():ammo.append({'arma':c[0].split(':')[0],'cap':int(c[1]),'preco':money(c[2]),'volume':float(c[3].replace(',','.'))})
# Six rounds, attack opportunities don't consume bonus; unlimited reserve, one weapon,
# loaded start, refill when blocked; unused bonus refills after round, if needed.
# Exact distribution of low-d20 event. No hit chance, movement or hand juggling modeled.
def sequence(cap,k,p,rounds=6):
 states={(cap,False):F(1)};shots=F(0);reloads=F(0)
 for turn in range(rounds):
  st={(l,b,True):v for (l,b),v in states.items()}
  for _ in range(k):
   nxt=defaultdict(F)
   for (l,b,bonus),v in st.items():
    if (b or l==0) and bonus:l,b,bonus=cap,False,False;reloads+=v
    if b or l==0:nxt[(l,b,bonus)]+=v;continue
    shots+=v;nxt[(l-1,True,bonus)]+=v*p;nxt[(l-1,l==1,bonus)]+=v*(1-p)
   st=nxt
  states=defaultdict(F)
  for (l,b,bonus),v in st.items():
   if turn<rounds-1 and bonus and (l<cap or b):l,b=cap,False;reloads+=v
   states[(l,b)]+=v
 return float(shots),float(reloads)
sequences=[]
for cap in range(1,5):
 for k in range(1,4):
  for label,p in [('vantagem',F(1,100)),('normal',F(1,10)),('desvantagem',F(19,100))]:
   sh,rel=sequence(cap,k,p);sequences.append({'capacidade':cap,'ataques_por_turno':k,'d20':label,'disparos_em_6_turnos':sh,'recargas_medias':rel})
ck('Sem panes: besta três oportunidades por turno',sequence(1,3,F(0))[0],7.0)
# Sensitivity: one point of burden reserved, empty container remains same burden.
sensitivity=[{'volume_por_recipiente':v,'recipientes_por_volume':int(F(1)/F(str(v))),'flechas_ou_virotes':20*int(F(1)/F(str(v))),'pistola_disparos_reserva':2*int(F(1)/F(str(v)))} for v in [.1,.2,.5,1]]
loads=[]
for strength in range(7):
 for n in ['Hankyū','Pistola','Rifle','Besta']:
  w=next(w for w in W if w['nome']==n)
  if strength<w['forca']:continue
  reserve=F('.2') if n in ['Hankyū','Besta','Pistola'] else F('.2')
  total=F(str(w['volume']))+F('.1')+reserve
  loads.append({'forca':strength,'arma':n,'traje_1':.1,'reserva_volume':float(reserve),'volume_conjunto':float(total),'capacidade':5+strength,'restante_para_outros_itens':float(5+strength-total)})
for a in ammo:
 a['custo_por_disparo']=a['preco']/a['cap'];a['disparos_reserva_por_volume']=a['cap']/a['volume'];a['estoque_inicial']=3*a['cap'];a['disparos_com_20000']=20000//a['preco']*a['cap']
ck('Pistola + traje + duas reservas',next(x['volume_conjunto'] for x in loads if x['arma']=='Pistola'),.4)
# Re-run old ammo conservation against current text, without touching historical folders.
runpy.run_path(str(E/'lote-03-r2/validar_regras.py'),run_name='__main__')
mun=json.loads((E/'lote-03-r2/evidencias/regras-verificadas.json').read_text());ck('Conservação e recarga anteriores permanecem válidas',mun['ok'],True)
old=(E/'lote-01-r3/EQUIPAMENTO-EM-JOGO.md').read_text();new=(E/'lote-01-r4/EQUIPAMENTO-EM-JOGO.md').read_text()
expected=old.replace('Use o alcance corpo a corpo indicado para a arma. Armas Longas alcançam 3 m; o padrão é 1,5 m.','O alcance corpo a corpo da arma é 3 m. Sem essa propriedade, o alcance comum é 1,5 m.')
ck('Equipamento: só Alcance alterado',new,expected)
eq={'ok':new==expected,'sha256_texto':sha(E/'lote-01-r4/EQUIPAMENTO-EM-JOGO.md'),'casos':[{'caso':'Delta único em Alcance','ok':new==expected}],'limites':['Demais regras herdadas do lote-01-r3; ganho de alcance pede mesa.']}
dump(E/'lote-01-r4/evidencias/regras-verificadas.json',eq)
result={'ok':all(c['ok'] for c in checks),'sha256_texto':sha(B/'ARMAS.md'),'casos':checks,'alcance_alterado':changed,'dados':metrics,'dominancia_parcial':dominance,'equivalentes':duplicates,'municao':ammo,'sensibilidade':sensitivity,'inventarios':loads,'sequencias':sequences,'limites':['Sem playtest humano. Distribuições exatas sob hipóteses registradas; não estimam dano final de classes. Tipos físicos são proposta nova. Dominância tem eixos restritos.']}
result['manuscritos_auditados']={str((E/unit/name).relative_to(R)):sha(E/unit/name) for unit,name in [('lote-04','ARMAS.md'),('lote-03-r2','MUNICAO.md'),('lote-01-r4','EQUIPAMENTO-EM-JOGO.md')]}
dump(B/'evidencias/regras-verificadas.json',result)
print(json.dumps({'ok':result['ok'],'verificacoes':len(checks),'falhas':[c for c in checks if not c['ok']],'alcance':changed,'dominancia':dominance,'equivalentes':duplicates},ensure_ascii=False))
assert result['ok']
