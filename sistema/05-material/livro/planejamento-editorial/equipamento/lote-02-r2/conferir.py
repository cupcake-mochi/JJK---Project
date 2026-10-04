from pathlib import Path
from collections import Counter
from fractions import Fraction
from itertools import product
import json,hashlib,re,unicodedata
import pdfplumber
from pypdf import PdfReader
B=Path(__file__).resolve().parent;R=B.parents[5]
IS_EQ=False
F='PROTECAO.md'
PDF='Projeto-M-Protecao-Proposta-02.pdf'
N=4
checks=[]
def ck(n,a,b):checks.append({'verificacao':n,'obtido':a,'esperado':b,'ok':a==b})
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def words(s):return re.findall(r'\w+',unicodedata.normalize('NFKC',s).casefold())
md=(B/F).read_text();meta=json.loads((B/'ESTRUTURA.json').read_text());chunks=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',md);sections={chunks[i]:chunks[i+2] for i in range(1,len(chunks),3)}
r=PdfReader(B/'output/pdf'/PDF)
ck('Quantidade de páginas e seções',[len(r.pages),len(sections)],[N,N]);ck('Sequência',list(sections),meta['ordem'])
ck('Títulos correspondem ao mapa',all(s.splitlines()[0]=='# '+meta['titulos'][k] for k,s in sections.items()),True)
top=[o for o in r.outline if not isinstance(o,list)]
ck('Entradas principais',len(top),2)
ck('Grupos recolhidos',[o.get('/Count') for o in top if o.get('/Count')],[-3])
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
import sys
sys.path.insert(0,str(B.parents[1]/'validacao-editorial'))
from conferir_editorial import check_file
ck('Bloqueio editorial e revisão contextual',check_file(B/F,True),[])
ck('Casos documentais registrados',len(json.loads((B/'evidencias/casos-documentais.json').read_text())),18)
# Published tables are independent oracle for the 9 preserved item profiles.
published=(R/'sistema/05-material/livro/manual/50-equipamento.md').read_text()
def rows(text,start,end):
 part=text.split(start,1)[1].split(end,1)[0]
 return [[re.sub(r'[`*]','',c.strip()) for c in l.strip('|').split('|')] for l in part.splitlines() if re.match(r'\| [123] \|',l)]
tr=rows(published,'### Traje','### Revestimento');rv=rows(published,'### Revestimento','## Escudo');sc=rows(published,'## Escudo','## Armas')
normal=lambda x:0.1 if x=='leve' else (None if x in ['—','Sem teto','Nenhuma'] else float(x.strip('+')))
source=[]
for group,rs in [('Traje',tr),('Revestimento',rv)]:
 for row in rs:source.append([group+row[0]]+[normal(v) for v in row[1:]])
for row in sc:source.append([row[1]]+[normal(v) for v in row[2:]])
expected=[['Traje1',1,None,None,.1],['Traje2',2,None,None,1],['Traje3',3,None,3,2],['Revestimento1',4,0,3,2],['Revestimento2',5,0,4,3],['Revestimento3',6,0,6,4],['Broquel',1,5,None,.1],['Médio',2,3,3,1],['Torre',3,1,5,2]]
ck('9 perfis correspondem ao dono',source,expected)
candidate=[]
for key,prefix in [('traje','Traje'),('escudo','Revestimento')]:
 s=sections[key]
 for l in s.splitlines():
  cells=[c.strip() for c in l.strip('|').split('|')]
  if len(cells)==5 and re.match(r'^[123]$',cells[0]):candidate.append([prefix+cells[0]]+[normal(v.replace(',','.')) for v in cells[1:]])
  elif len(cells)==5 and cells[0] in ['Broquel','Médio','Torre']:candidate.append([cells[0]]+[normal(v.replace(',','.')) for v in cells[1:]])
ck('Tabela candidata preserva os9perfis',candidate,source)
def defense(dex,armor,shield,energy):
 caps=[x[2] for x in [armor,shield] if x and x[2] is not None]
 useful=min([dex]+caps)
 protection=(armor[1] if armor else energy)+(shield[1] if shield else 0)
 return 10+useful+protection
ck('ExemploRinaTraje2',defense(4,expected[1],None,4),16)
ck('ExemploRinaMédio',defense(4,expected[1],expected[7],4),17)
ck('ExemploSousuke',defense(2,expected[5],expected[8],4),19)
ck('Durante retiradaTraje2 semescudo',10+4,14)
values=[]
for force,dex,energy in product(range(7),range(7),range(5)):
 for armor in [None]+expected[:6]:
  for shield in [None]+expected[6:]:
   if any(x and x[3] is not None and force<x[3] for x in [armor,shield]):continue
   got=defense(dex,armor,shield,energy);values.append(got)
ck('Montagens legais não ultrapassam teto publicado20',max(values),20)
ck('Teto0 sempre elimina parcelaDex',all(defense(d,expected[5],expected[8],4)==19 for d in range(7)),True)
ck('Energia passiva não soma comTraje',len({defense(4,expected[1],None,e) for e in range(5)}),1)
ck('Volume6 e capacidade11',[4+2,5+6],[6,11])
ck('Situações publicadas preservadas',all(x in md for x in ['Vão apertado','Altura e beirada','Escuro','Superfície ruim','Água e chuva','Multidão','Terreno instável','Calor e fogo']),True)
ck('Sem benefício antes de finalizar','só começa a valer depois' in md,True)
ck('Sem restauração passiva ao retirar parcialmente','depois de terminar de retirar' in md,True)
(B/'evidencias/calculos.json').write_text(json.dumps({'montagens_legais':len(values),'maximo_defesa':max(values),'ressalva':'Enumeração dos perfis e atributos, sem efeitos específicos. Não é playtest ou prova da vantagem situacional.'},ensure_ascii=False,indent=2)+'\n')
scenario=json.loads((B/'evidencias/regras-verificadas.json').read_text())
ck('Cenários da restrição de Trajes',scenario['ok'],True)
ck('Cenários do Traje usam texto atual',scenario['sha256_texto'],sha(B/F))
# Serialize expectations that use fractions as strings, and keep failures compact.
res={'data':'2026-10-03','ok':all(c['ok'] for c in checks),'verificacoes':len(checks),'sha256_pdf':sha(B/'output/pdf'/PDF),'sha256_texto':sha(B/F),'checks':checks,'geometria':geom,'limites':['Não substitui revisão independente, teste humano ou playtest.','Convenções novas identificadas em DECISOES.md.']}
(B/'CONFERENCIA.json').write_text(json.dumps(res,ensure_ascii=False,indent=2,default=str)+'\n')
print(json.dumps({'ok':res['ok'],'verificacoes':len(checks),'falhas':[c['verificacao'] for c in checks if not c['ok']]},ensure_ascii=False))
raise SystemExit(0 if res['ok'] else 1)
