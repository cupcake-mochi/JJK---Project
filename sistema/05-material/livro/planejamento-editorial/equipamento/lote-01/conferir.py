from pathlib import Path
from collections import Counter
from fractions import Fraction
from itertools import product
import json,hashlib,re,unicodedata
import pdfplumber
from pypdf import PdfReader
B=Path(__file__).resolve().parent;R=B.parents[5]
IS_EQ='equipamento' in B.parts
F='EQUIPAMENTO-EM-JOGO.md' if IS_EQ else 'MOVIMENTO-E-CARGA.md'
PDF='Projeto-M-Equipamento-em-Jogo-Proposta-01.pdf' if IS_EQ else 'Projeto-M-Movimento-e-Carga-Proposta-02.pdf'
N=6 if IS_EQ else 5
checks=[]
def ck(n,a,b):checks.append({'verificacao':n,'obtido':a,'esperado':b,'ok':a==b})
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def words(s):return re.findall(r'\w+',unicodedata.normalize('NFKC',s).casefold())
md=(B/F).read_text();meta=json.loads((B/'ESTRUTURA.json').read_text());chunks=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',md);sections={chunks[i]:chunks[i+2] for i in range(1,len(chunks),3)}
r=PdfReader(B/'output/pdf'/PDF)
ck('Quantidade de páginas e seções',[len(r.pages),len(sections)],[N,N]);ck('Sequência',list(sections),meta['ordem'])
ck('Títulos correspondem ao mapa',all(s.splitlines()[0]=='# '+meta['titulos'][k] for k,s in sections.items()),True)
top=[o for o in r.outline if not isinstance(o,list)]
ck('Entradas principais',len(top),2 if IS_EQ else 3)
ck('Grupos recolhidos',[o.get('/Count') for o in top if o.get('/Count')],[-3,-3] if IS_EQ else [-2,-2])
def flatten(nodes):
 for n in nodes:
  if isinstance(n,list):yield from flatten(n)
  else:yield n
ck('Destinos de marcadores válidos',all(0<=r.get_destination_page_number(o)<N for o in flatten(r.outline)),True)
ids={p.indirect_reference.idnum:i+1 for i,p in enumerate(r.pages)};geom=[]
with pdfplumber.open(B/'output/pdf'/PDF) as doc:
 for i,(p,(key,s)) in enumerate(zip(doc.pages,sections.items()),1):
  clean=re.sub(r'\[([^\]]+)\]\(#[^)]+\)',r'\1',s);t=p.extract_text(x_tolerance=1,y_tolerance=3)
  ck(f'p{i}: texto completo',dict(Counter(words(clean))-Counter(words(t))),{})
  cs=[c for c in p.chars if c['text'].strip()];body=[c for c in cs if 48<c['top']<785]
  ck(f'p{i}: texto dentro da página',all(0<=c['x0']<=c['x1']<=p.width and 0<=c['top']<=c['bottom']<=p.height for c in cs),True)
  ck(f'p{i}: corpo separado de rodapé',max(c['bottom'] for c in body)<785,True)
  embed=set()
  for f in r.pages[i-1]['/Resources']['/Font'].values():
   o=f.get_object();d=o.get('/FontDescriptor')
   if d and any(k in d.get_object() for k in ['/FontFile','/FontFile2','/FontFile3']):embed.add(str(o['/BaseFont']).lstrip('/'))
  ck(f'p{i}: fontes incorporadas',sorted({c['fontname'] for c in cs}-embed),[])
  ck(f'p{i}: sem imagem raster',len(p.images),0)
  refs=re.findall(r'\]\(#([^)]+)\)',s);ck(f'p{i}: remissões existentes',[x for x in refs if x not in meta['paginas']],[])
  targets=[]
  for ar in r.pages[i-1].get('/Annots',[]):
   a=ar.get_object()
   if a.get('/Subtype')=='/Link':
    d=a.get('/Dest');targets.append(ids.get(d[0].idnum) if d else None)
  ck(f'p{i}: links corretos',sorted(set(targets)),sorted({meta['paginas'][x] for x in refs}))
  for ref in set(refs):ck(f'p{i}: página citada {ref}',f"(p. {meta['paginas'][ref]})" in re.sub(r'\s+', ' ', t),True)
  geom.append({'pagina':i,'final_corpo':round(max(c['bottom'] for c in body),2)})
snap=json.loads((B/'evidencias/fontes-preservadas.json').read_text());ck('Fontes e versões anteriores preservadas',[n for n,h in snap.items() if sha(R/n)!=h],[])
inv=json.loads((R/'sistema/05-material/livro/planejamento-editorial/INVENTARIO-BASE.json').read_text());ck('Livro e exportações preservados',[x['arquivo'] for x in inv['fontes']+inv['artefatos_publicados'] if sha(R/x['arquivo'])!=x['sha256']],[])
rev=json.loads((B/'evidencias/REVISAO-EDITORIAL.json').read_text());ck('Revisão do texto atual',rev['sha256_texto'],sha(B/F));ck('Seções lidas',len(rev['secoes']),N)
v=json.loads((B/'evidencias/inspecao-visual.json').read_text());ck('Inspeção do PDF atual',v['sha256_pdf'],sha(B/'output/pdf'/PDF));ck('Todas páginas visualmente examinadas',[p['pagina'] for p in v['paginas']],list(range(1,N+1)))
ck('Inspeção sem defeitos',all(p['resultado']=='sem defeito visual observado' for p in v['paginas']),True)
# Documentary cases are editorial scenarios, not human playtesting.
ck('Casos documentais registrados',len(json.loads((B/'evidencias/casos-documentais.json').read_text())),34 if IS_EQ else 25)
if IS_EQ:
 # Exact distribution of the chosen d20; not the total reload rate (X also matters).
 probs={k:Fraction(sum(fn(a,b)<=2 for a,b in product(range(1,21),repeat=2)),400) for k,fn in [('vantagem',max),('desvantagem',min)]}
 ck('Gatilho normal10%',sum(d<=2 for d in range(1,21)),2);ck('Vantagem1%',str(probs['vantagem']),'1/100');ck('Desvantagem19%',str(probs['desvantagem']),'19/100')
 # State traces using the manuscript procedure, with expectations independent of resolver.
 def shots(cap,dice,bonus=1):
  loaded=True;count=0;done=0;reloaded=0
  for die in dice:
   if not loaded:
    if not bonus:break
    bonus-=1;loaded=True;count=0;reloaded+=1
   done+=1;count+=1
   if count>=cap or die<=2:loaded=False
  return [done,count,loaded,reloaded,bonus]
 for label,args,want in [
 ('Besta3ataques,1Bônus',(1,[12,13,14]),[2,1,False,1,0]),
 ('Pistola2ataques semBônus, primeiro1',(2,[1,18],0),[1,1,False,0,0]),
 ('Rifle terc2, ambosgatilhos',(3,[12,13,2,18]),[4,1,True,1,0]),
 ('Dois1seguidos demandam2recargas',(3,[1,1,18]),[2,1,False,1,0]),
 ('Rifle4disparos semnaturalbaixo',(3,[12,13,14,15]),[4,1,True,1,0]),
 ('Metralhadora5disparos',(4,[12]*5),[5,1,True,1,0])]:ck(label,shots(*args),want)
 # Every X and die: triggering shot resolves, then blocks; two triggers cannot duplicate reload.
 ck('80 casos de disparo no último espaço do ciclo',all(shots(x,[10]*(x-1)+[d],0)==[x,x,False,0,0] for x in range(1,5) for d in range(1,21)),True)
 # Free opportunity constrained for Malabarista; paid manipulation consumes whole Movement.
 def manip(actions,mal=False,moved=False):
  free=0;movement=0;done=0
  for a in actions:
   if a=='largar':done+=1;continue
   eligible=free==0 or (mal and free==1 and a in ['sacar','guardar','recolher'])
   if eligible:free+=1
   elif not moved and movement==0:movement=1
   else:break
   done+=1
  return [done,free,movement]
 for name,args,want in [('Troca comum',(['guardar','sacar'],),[2,1,1]),('Largar não acumula gratuidade',(['largar','sacar','recolher'],),[3,1,1]),('Andou antes da troca',(['guardar','sacar'],False,True),[1,1,0]),('Malabarista porta arma',(['porta','sacar'],True),[2,2,0]),('Malabarista arma porta',(['sacar','porta'],True),[2,1,1])]:ck(name,manip(*args),want)
 ck('Empate ocultação: comparação passiva e busca',[14>=10+4,15>=15],[True,True])
 ck('Leve preserva décimos',str(9*Fraction(1,10)),'9/10')
 # Independent convolution, then exact expectation of maximum of two damage pools.
 results=[]
 for count in [1,2,4]:
  dist=Counter({0:1})
  for _ in range(count):dist=Counter({s:sum(n for x,n in dist.items() for d in range(1,7) if x+d==s) for s in range(count*6+1)})
  dist=Counter({k:v for k,v in dist.items() if v})
  total=6**count;ev=Fraction(sum(max(a,b)*na*nb for a,na in dist.items() for b,nb in dist.items()),total**2)
  ck(f'Par{count}d6 distribuição',sum(dist.values()),total)
  ck(f'Par{count}d6 melhora média dentro do máximo',Fraction(7*count,2)<=ev<=6*count,True)
  results.append({'dados':f'{count}d6','media_normal':3.5*count,'media_Par':float(ev),'exata':str(ev),'aumento':float(ev)-3.5*count})
 ck('Par1d6 preserva caso original',results[0]['exata'],'161/36')
 source=(R/'sistema/05-material/livro/manual/50-equipamento.md').read_text().split('### Munição')[1].split('## Treino')[0]
 canon={}
 for l in source.splitlines():
  m=re.match(r'\| ([1-4]) \| (.+?) \|',l)
  if m:
   for name in m[2].split(' · '):canon[name]=int(m[1])
 proposed={'Besta':1,'Besta de Uma Mão':1,'Pistola':2,'Revólver':2,'Espingarda':2,'Rifle de Precisão':2,'Rifle':3,'Submetralhadora':3,'Metralhadora Pesada':4}
 ck('LimitesMunição correspondem ao dono',proposed,canon)
 (B/'evidencias/analise-numerica.json').write_text(json.dumps({'Par':results,'gatilho_natural':{'normal':.10,'vantagem':.01,'desvantagem':.19},'limite':'Não mede equilíbrio das Trilhas, valor da Bônus, suprimentos ou frequência total de recarga.'},ensure_ascii=False,indent=2)+'\n')
else:
 before=(R/'caminhos/05-Edicao-Integrada/06-Incursor-Caminho-e-Trilhas.md').read_text()
 after=(B/'sincronizacoes/INCURSOR-COMPLETO.md').read_text()
 expected=before.replace('criaturas de até uma categoria de tamanho maior que você. Esse limite','criaturas de qualquer tamanho. Esse limite').replace('- Movimento Acrobático permite atravessar espaços de criaturas de qualquer tamanho, mantendo a exigência de terminar em espaço livre com apoio.\n','')
 ck('Incursor completo contém apenas duas alterações aprovadas',after==expected,True)
 ck('Novo nível2 permite qualquer tamanho','criaturas de qualquer tamanho. Esse limite' in after,True)
 level30=after.split('### Nível 30')[1].split('### Trilha')[0]
 ck('Sem benefício de tamanho duplicado no30','qualquer tamanho' in level30,False)
 ck('30 mantém dobra e oportunidade',[s in level30 for s in ['Seu deslocamento dobra','não provocam ataques de oportunidade']],[True,True])
 ck('Matriz36pares, 16 impedidos pela geral',sum(abs(a-b)<2 for a,b in product(range(6),repeat=2)),16)
 ck('Distâncias de exemplo normal e difícil',[4.5,4.5*2,12/2],[4.5,9.,6.])
 ck('Níveis2,23,30 limite acrobático',[12/2,12,12*2],[6.,12,24])
 ck('Qualquer tamanho não concede7,5m no nível2',7.5<=12/2,False)
 ck('Mesmo percurso cabe no23',7.5<=12,True)
 ck('Carga exata no limite e além',[Fraction(45,10)+5*Fraction(1,10),Fraction(45,10)+6*Fraction(1,10)],[Fraction(5),Fraction(51,10)])
# Serialize expectations that use fractions as strings, and keep failures compact.
res={'data':'2026-10-03','ok':all(c['ok'] for c in checks),'verificacoes':len(checks),'sha256_pdf':sha(B/'output/pdf'/PDF),'sha256_texto':sha(B/F),'checks':checks,'geometria':geom,'limites':['Não substitui revisão independente, teste humano ou playtest.','Convenções novas identificadas em DECISOES.md.']}
(B/'CONFERENCIA.json').write_text(json.dumps(res,ensure_ascii=False,indent=2,default=str)+'\n')
print(json.dumps({'ok':res['ok'],'verificacoes':len(checks),'falhas':[c['verificacao'] for c in checks if not c['ok']]},ensure_ascii=False))
raise SystemExit(0 if res['ok'] else 1)
