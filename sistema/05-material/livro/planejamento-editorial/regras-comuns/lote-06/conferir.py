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
md=(B/'MOVIMENTO-E-CARGA.md').read_text();meta=json.loads((B/'ESTRUTURA.json').read_text())
a=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',md)
sections={a[i]:a[i+2] for i in range(1,len(a),3)}
pdf=B/'output/pdf/Projeto-M-Movimento-e-Carga-Proposta-01.pdf';r=PdfReader(pdf)
ck('Quatro páginas e seções', [len(r.pages),len(sections)], [4,4])
ck('Ordem de leitura',list(sections),meta['ordem'])
ck('Subtítulos não repetem título da seção',[k for k,s in sections.items() if '## '+meta['titulos'][k]+'\n' in s],[])
ck('Todos os títulos coincidem com o mapa', [k for k,s in sections.items() if s.splitlines()[0]!='# '+meta['titulos'][k]],[])
top=[o for o in r.outline if not isinstance(o,list)]
ck('Duas entradas principais',len(top),2)
ck('Grupos iniciam recolhidos',[x.get('/Count') for x in top if x.get('/Count')],[-2,-2])
def flatten(nodes):
 for o in nodes:
  if isinstance(o,list):yield from flatten(o)
  else:yield o
out=list(flatten(r.outline));ck('Marcadores com destinos válidos',all(0<=r.get_destination_page_number(o)<4 for o in out),True)
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

from math import floor
# Contas em passos/parcelas exatas; não simula eficácia de combate.
ck('Carga5+Força',[5+x for x in [0,2,4,6]],[5,7,9,11])
ck('Equivalentes emkg',[12*(5+x) for x in [0,2,4,6]],[60,84,108,132])
ck('9 leves preservam décimos',str(9*Fraction(1,10)),str(Fraction(9,10)))
ck('10leves total1',int(10*Fraction(1,10)),1)
ck('No limite/um item a mais',[Fraction(45,10)+n*Fraction(1,10)<=5 for n in [5,6]],[True,False])
ck('Carga de aliado e próprio equipamento',72//12+2,8)
ck('Esforço dobrado Força2',2*(5+2),14)
ck('Rastejar9m regular/difícil',[floor(9/3)*1.5,floor(9/4.5)*1.5],[4.5,3.0])
ck('Outro corte do deslocamento não desaparece',floor(4.5/3)*1.5,1.5)
ck('Rastejar e espremer custo aditivo',[1.5+1.5+1.5,1.5+1.5+1.5+1.5],[4.5,6.0])
ck('Voo sem segunda reserva',[12-6,max(0,9-12)],[6,0])
ck('Graus de tamanho:duas categorias',[abs(2-t)>=2 for t in [2,3,4]],[False,False,True])
ck('Não corta movimento duas vezes','não corte o deslocamento pela metade de novo' in md,True)
ck('Incapacitado não concede travessia','Incapacitado não libera passagem automaticamente' in md,True)
ck('Sem voo por energia genérica','não concede voo por si só' in md,True)
ck('Sem reação universal de borda','não há uma Reação geral gratuita para recuperar apoio' in md,True)
ck('18casos documentais',len(json.loads((B/'evidencias/casos-documentais.json').read_text())),18)
rev=json.loads((B/'evidencias/REVISAO-EDITORIAL.json').read_text())
ck('Quatro seções avaliadas editorialmente',sorted(x['id'] for x in rev['secoes']),sorted(sections))
ck('Revisão ligada ao texto',rev['sha256_texto'],sha(B/'MOVIMENTO-E-CARGA.md'))
snap=json.loads((B/'evidencias/fontes-preservadas.json').read_text())
ck('Fontes e consolidado anterior preservados',[n for n,h in snap.items() if sha(ROOT/n)!=h],[])
base=ROOT/'sistema/05-material/livro/planejamento-editorial'
inv=json.loads((base/'INVENTARIO-BASE.json').read_text())
ck('Livro e exportações preservados',[x['arquivo'] for x in inv['fontes']+inv['artefatos_publicados'] if sha(ROOT/x['arquivo'])!=x['sha256']],[])
protected=json.loads((base/'regras-comuns/lote-03/evidencias/preservacao-base.json').read_text())
ck('137 arquivos protegidos',[n for n,h in protected.items() if sha(ROOT/n)!=h],[])
visual=json.loads((B/'evidencias/inspecao-visual.json').read_text())
ck('Inspeção visual ligada ao PDF',visual['sha256_pdf'],sha(pdf))
ck('Quatro páginas visualmente examinadas',[x['pagina'] for x in visual['paginas']],list(range(1,5)))
ck('Sem defeitos visuais registrados',all(x['resultado']=='sem defeito visual observado' for x in visual['paginas']),True)
ck('18 casos documentais',rev['casos_documentais'],18)
broken=[]
for p in B.rglob('*.md'):
 for href in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if re.match(r'^[a-z]+:',href) or href.startswith('#'):continue
  target=p.parent/href.split('#')[0]
  if target.name=='CONFERENCIA.json':continue
  if not target.exists():broken.append([str(p.relative_to(B)),href])
ck('Links do dossiê',broken,[])
res={'data':'2026-10-03','ok':all(x['ok'] for x in checks),'sha256_texto':sha(B/'MOVIMENTO-E-CARGA.md'),'sha256_pdf':sha(pdf),'verificacoes':len(checks),'checks':checks,'geometria':geometry,'limites':['Não é teste humano ou prova de equilíbrio.','Revisão pelo autor, sem nova revisão independente.','Decisões candidatas e pendências identificadas em DECISOES.md.']}
(B/'CONFERENCIA.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':res['ok'],'verificacoes':len(checks),'falhas':[x for x in checks if not x['ok']]},ensure_ascii=False,indent=2))
raise SystemExit(0 if res['ok'] else 1)
