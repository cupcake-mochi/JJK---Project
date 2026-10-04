from pathlib import Path
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib,json,re,unicodedata
import pdfplumber
from pypdf import PdfReader
B=Path(__file__).resolve().parent;ROOT=B.parents[5]
checks=[]
def ck(name,got,want):checks.append(dict(verificacao=name,obtido=got,esperado=want,ok=got==want))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def words(s):return re.findall(r'\w+',unicodedata.normalize('NFKC',s).casefold())
md=(B/'RECUPERACAO.md').read_text();meta=json.loads((B/'ESTRUTURA.json').read_text())
a=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',md)
sections={a[i]:a[i+2] for i in range(1,len(a),3)}
pdf=B/'output/pdf/Projeto-M-Recuperacao-Proposta-01.pdf';r=PdfReader(pdf)
ck('Oito páginas e seções', [len(r.pages),len(sections)], [8,8])
ck('Ordem de leitura',list(sections),meta['ordem'])
ck('Subtítulos não repetem título da seção',[k for k,s in sections.items() if '## '+meta['titulos'][k]+'\n' in s],[])
ck('Todos os títulos coincidem com o mapa', [k for k,s in sections.items() if s.splitlines()[0]!='# '+meta['titulos'][k]],[])
top=[o for o in r.outline if not isinstance(o,list)]
ck('Duas entradas principais',len(top),2)
ck('Grupos iniciam recolhidos',[x.get('/Count') for x in top if x.get('/Count')],[-5,-3])
def flatten(nodes):
 for o in nodes:
  if isinstance(o,list):yield from flatten(o)
  else:yield o
out=list(flatten(r.outline));ck('Marcadores com destinos válidos',all(0<=r.get_destination_page_number(o)<8 for o in out),True)
geometry=[]
with pdfplumber.open(pdf) as doc:
 for n,(p,(key,chunk)) in enumerate(zip(doc.pages,sections.items()),1):
  clean=re.sub(r'\[([^\]]+)\]\(#[^)]+\)',r'\1',chunk)
  t=p.extract_text(x_tolerance=1,y_tolerance=3)
  ck(f'p{n}: sem palavras perdidas',dict(Counter(words(clean))-Counter(words(t))),{})
  chars=[c for c in p.chars if c['text'].strip()];body=[c for c in chars if 48<c['top']<785]
  ck(f'p{n}: limites físicos',all(0<=c['x0']<=c['x1']<=p.width and 0<=c['top']<=c['bottom']<=p.height for c in chars),True)
  ck(f'p{n}: rodapé separado',max(c['bottom'] for c in body)<785,True)
  used={c['fontname'] for c in chars};embedded=[]
  for f in r.pages[n-1]['/Resources']['/Font'].values():
   font=f.get_object();d=font.get('/FontDescriptor')
   if d and any(k in d.get_object() for k in ['/FontFile','/FontFile2','/FontFile3']):embedded.append(str(font['/BaseFont']).lstrip('/'))
  ck(f'p{n}: fontes incorporadas',sorted(used-set(embedded)),[])
  ck(f'p{n}: sem imagens raster',len(p.images),0)
  refs=re.findall(r'\]\(#([^)]+)\)',chunk)
  ck(f'p{n}: referências existentes', [x for x in refs if x not in meta['paginas']],[])
  page_ids={p.indirect_reference.idnum:i+1 for i,p in enumerate(r.pages)}
  destinations=[]
  for ref in r.pages[n-1].get('/Annots',[]):
   obj=ref.get_object()
   if obj.get('/Subtype')=='/Link':
    dest=obj.get('/Dest');destinations.append(page_ids.get(dest[0].idnum) if dest else None)
  ck(f'p{n}: links PDF para destinos esperados',sorted(set(destinations)),sorted(set(meta['paginas'][x] for x in refs)))
  for ref in set(refs):
   ck(f'p{n}: número da remissão {ref}',f"(p. {meta['paginas'][ref]})" in t,True)
  geometry.append({'pagina':n,'secao':key,'final_corpo':round(max(c['bottom'] for c in body),2),'links':destinations})

from math import ceil, floor
# Resoluções manuais confrontadas com modelo pequeno de recursos, não simulador de combate.
def ganho(maximo,pct):return 0 if maximo<=0 or pct==0 else max(1,floor(maximo*pct))
def curto(maximo,atual,grau=0,propicio=False):
 pct=Fraction(1,4) if propicio else [Fraction(1,4),Fraction(3,20),Fraction(1,20),Fraction(0)][grau]
 return min(maximo,atual+ganho(maximo,pct))
def longo_fora(maximo,atual):return min(maximo,max(atual,ganho(maximo,Fraction(1,2))))
def cura(maximo,atual,valor):return min(maximo,atual+valor)
def temp(maximo,saldo,novo):return min(ganho(maximo,Fraction(1,2)),max(saldo,novo))
def custos(ref):return [ceil(Fraction(ref,d)) for d in [8,4,2]]
ck('Cura sem ultrapassar máximo',cura(20,14,8),20)
ck('Cuidado respeita faixa inicial',[0<x<50 for x in [0,1,45,50,55]],[False,True,True,False,False])
ck('Temporários com teto',temp(23,0,15),11)
ck('Nova concessão compara saldo',temp(23,3,9),9)
ck('Concessão menor não apaga maior',temp(23,9,3),9)
ck('Dano exemplo',12-9,3)
ck('Energia temporária paga primeiro',[temp(8,0,6),2-(5-temp(8,0,6))],[4,1])
ck('Sem reserva do nada',temp(0,0,5),0)
ck('Aguentar20%ref23',ceil(Fraction(23,5)),5)
ck('Dano a zero ultrapassa, não iguala',[d>Fraction(40,2) for d in [19,20,21]],[False,False,True])
ck('Insistir ref80',custos(80),[10,20,40])
ck('Máximo após parcelas',[80-sum(custos(80)[:i]) for i in [1,2,3]],[70,50,10])
ck('Insistir ref23 arredonda cada custo',custos(23),[3,6,12])
ck('Cura acumulada após colapso',[25+15,ceil(Fraction(80,2)),min(10,25+15)],[40,40,10])
ck('Achado ref10 esgota máximo',10-sum(custos(10)),0)
ck('Achado ref5 não paga todas',5-sum(custos(5)),-1)
ck('Sequela encurta janela',[max(0,3-s) for s in range(5)],[3,2,1,0,0])
ck('Curto exemplo10PE',curto(10,1),3)
ck('Curto respeita máximo',curto(10,9),10)
ck('Exaustão max8',[curto(8,0,g) for g in range(4)],[2,1,1,0])
ck('Propício não perdePEpelaExaustão',[curto(8,0,g,True) for g in range(4)],[2,2,2,2])
ck('Longo piso23 preserva18',[longo_fora(23,x) for x in [3,11,18,23]],[11,11,18,23])
ck('Longo ref60 saldo8',longo_fora(60,8),30)
ck('Exaustão adotou4,5m','Deslocamento limitado a 4,5 m.' in md,True)
ck('Combinação Exaustão/Integridade',[min(4.5,x/2) for x in [9,6]],[4.5,3.0])
# Monotonia da recuperação entre degraus e preservação de saldo.
erros=[];casos=0
for m in range(201):
 for atual in {0,m//2,m}:
  v=[curto(m,atual,g) for g in range(4)];f=longo_fora(m,atual);casos+=1
  if v!=sorted(v,reverse=True) or any(not atual<=x<=m for x in v) or not atual<=f<=m:erros.append([m,atual])
ck('Grade201máximos: descanso não reduz saldo e exaustão não melhora recuperação',erros,[])
ck('Amostra inclui máximos0a200',casos,600)
riscos=[m for m in range(1,81) if sum(custos(m))>=m]
ck('Limiares problemáticos de Insistir abaixo81',riscos,[1,2,3,4,5,6,7,9,10,11,13,17])
(B/'evidencias/contas-recuperacao.json').write_text(json.dumps(dict(grade_descanso=casos,maximos_insistir_sem_sobra=riscos,limite='Modelo de procedimentos candidatos, não validação de equilíbrio; custo em máximo reduzido exige decisão.'),ensure_ascii=False,indent=2)+'\n')
ck('28 casos documentais com IDs distintos',len({x['id'] for x in json.loads((B/'evidencias/casos-documentais.json').read_text())}),28)
rev=json.loads((B/'evidencias/REVISAO-EDITORIAL.json').read_text())
ck('Oito seções avaliadas editorialmente',sorted(x['id'] for x in rev['secoes']),sorted(sections))
ck('Revisão ligada ao texto',rev['sha256_texto'],sha(B/'RECUPERACAO.md'))
snap=json.loads((B/'evidencias/fontes-preservadas.json').read_text())
ck('Fontes e consolidado anterior preservados',[n for n,h in snap.items() if sha(ROOT/n)!=h],[])
base=ROOT/'sistema/05-material/livro/planejamento-editorial'
inv=json.loads((base/'INVENTARIO-BASE.json').read_text())
ck('Livro e exportações preservados',[x['arquivo'] for x in inv['fontes']+inv['artefatos_publicados'] if sha(ROOT/x['arquivo'])!=x['sha256']],[])
protected=json.loads((base/'regras-comuns/lote-03/evidencias/preservacao-base.json').read_text())
ck('137 arquivos protegidos',[n for n,h in protected.items() if sha(ROOT/n)!=h],[])
visual=json.loads((B/'evidencias/inspecao-visual.json').read_text())
ck('Inspeção visual ligada ao PDF',visual['sha256_pdf'],sha(pdf))
ck('Oito páginas visualmente examinadas',[x['pagina'] for x in visual['paginas']],list(range(1,9)))
ck('Sem defeitos visuais registrados',all(x['resultado']=='sem defeito visual observado' for x in visual['paginas']),True)
ck('28 casos documentais',rev['casos_documentais'],28)
broken=[]
for p in B.rglob('*.md'):
 for href in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if re.match(r'^[a-z]+:',href) or href.startswith('#'):continue
  target=p.parent/href.split('#')[0]
  if target.name=='CONFERENCIA.json':continue
  if not target.exists():broken.append([str(p.relative_to(B)),href])
ck('Links do dossiê',broken,[])
res={'data':'2026-10-03','ok':all(x['ok'] for x in checks),'sha256_texto':sha(B/'RECUPERACAO.md'),'sha256_pdf':sha(pdf),'verificacoes':len(checks),'checks':checks,'geometria':geometry,'limites':['Não é teste humano ou prova de equilíbrio.','Revisão pelo autor, sem nova revisão independente.','Decisões candidatas e pendências identificadas em DECISOES.md.']}
(B/'CONFERENCIA.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':res['ok'],'verificacoes':len(checks),'falhas':[x for x in checks if not x['ok']]},ensure_ascii=False,indent=2))
raise SystemExit(0 if res['ok'] else 1)
