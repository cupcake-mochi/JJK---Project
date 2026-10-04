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
md=(B/'TESTES-E-TURNOS.md').read_text();meta=json.loads((B/'ESTRUTURA.json').read_text())
a=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',md)
sections={a[i]:a[i+2] for i in range(1,len(a),3)}
pdf=B/'output/pdf/Projeto-M-Testes-e-Turnos-Proposta-01.pdf';r=PdfReader(pdf)
ck('Sete páginas e seções', [len(r.pages),len(sections)], [7,7])
ck('Ordem de leitura',list(sections),meta['ordem'])
ck('Subtítulos não repetem título da seção',[k for k,s in sections.items() if '## '+meta['titulos'][k]+'\n' in s],[])
ck('Todos os títulos coincidem com o mapa', [k for k,s in sections.items() if s.splitlines()[0]!='# '+meta['titulos'][k]],[])
top=[o for o in r.outline if not isinstance(o,list)]
ck('Duas entradas principais',len(top),2)
ck('Grupos iniciam recolhidos',[x.get('/Count') for x in top if x.get('/Count')],[-4,-3])
def flatten(nodes):
 for o in nodes:
  if isinstance(o,list):yield from flatten(o)
  else:yield o
out=list(flatten(r.outline));ck('Marcadores com destinos válidos',all(0<=r.get_destination_page_number(o)<7 for o in out),True)
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

ck('Atributo é modificador direto','O valor anotado já é o modificador' in md,True)
ck('Níveis e maestria',[(n,1+(n-2)//8) for n in [2,9,10,17,18,25,26,30]],[(2,1),(9,1),(10,2),(17,2),(18,3),(25,3),(26,4),(30,4)])
ck('Especialização', [m//2 for m in [2,3,4]],[1,1,2])
ck('Exemplo de perícia',[3+1,3,3+2],[4,3,5])
ck('Dificuldade do criador',[8+4+2,8+4+2+2],[14,16])
ck('Vantagem e bônus',max(6,17)+4,21)
ck('TR de Kaito',9+4+2,15)
ck('Grupo ímpar: mínimo de sucessos',(5+1)//2,3)
ck('Sem sucesso automático de20 em perícia',sum(d+4>=26 for d in range(1,21)),0)
ck('Seis CDs fixas',re.findall(r'^\| (?:Fácil|Média|Difícil|Muito difícil|Extrema|Quase impossível) \| (\d+) \|',md,re.M),['6','10','14','18','22','26'])
ck('Cinco ajustes, sem Extremo inventado','Não definido nesta escala.' in md,True)
ck('Reação não renova pela rodada','Ela não volta na passagem de uma rodada para outra.' in md,True)
ck('Conversão não remove limite','Converter ações não remove esse limite' in md,True)
ck('TR Físico fixo','TR Físico é feita na criação e permanece fixa' in md,True)
ck('Fonte de vantagem cancela desvantagem','mesmo que existam várias fontes de um dos lados' in md,True)
ck('Concentração Vigor, Carregar Espírito','TR de Vigor contra a CD' in md and '**TR de Espírito**' in md,True)
ck('Fonte com dano zerado não aciona gatilho','cada golpe que causar dano' in md,True)
rev=json.loads((B/'evidencias/REVISAO-EDITORIAL.json').read_text())
ck('Sete seções avaliadas editorialmente',sorted(x['id'] for x in rev['secoes']),sorted(sections))
ck('Revisão ligada ao texto',rev['sha256_texto'],sha(B/'TESTES-E-TURNOS.md'))
snap=json.loads((B/'evidencias/fontes-preservadas.json').read_text())
ck('Fontes e consolidado anterior preservados',[n for n,h in snap.items() if sha(ROOT/n)!=h],[])
base=ROOT/'sistema/05-material/livro/planejamento-editorial'
inv=json.loads((base/'INVENTARIO-BASE.json').read_text())
ck('Livro e exportações preservados',[x['arquivo'] for x in inv['fontes']+inv['artefatos_publicados'] if sha(ROOT/x['arquivo'])!=x['sha256']],[])
protected=json.loads((base/'regras-comuns/lote-03/evidencias/preservacao-base.json').read_text())
ck('137 arquivos protegidos',[n for n,h in protected.items() if sha(ROOT/n)!=h],[])
broken=[]
for p in B.rglob('*.md'):
 for href in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if re.match(r'^[a-z]+:',href) or href.startswith('#'):continue
  target=p.parent/href.split('#')[0]
  if target.name=='CONFERENCIA.json':continue
  if not target.exists():broken.append([str(p.relative_to(B)),href])
ck('Links do dossiê',broken,[])
res={'data':'2026-10-03','ok':all(x['ok'] for x in checks),'sha256_texto':sha(B/'TESTES-E-TURNOS.md'),'sha256_pdf':sha(pdf),'verificacoes':len(checks),'checks':checks,'geometria':geometry,'limites':['Não é teste humano ou prova de equilíbrio.','Revisão pelo autor, sem nova revisão independente.','Decisões candidatas e pendências identificadas em DECISOES.md.']}
(B/'CONFERENCIA.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':res['ok'],'verificacoes':len(checks),'falhas':[x for x in checks if not x['ok']]},ensure_ascii=False,indent=2))
raise SystemExit(0 if res['ok'] else 1)
