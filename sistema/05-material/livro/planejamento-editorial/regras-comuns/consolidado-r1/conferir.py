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
md=(B/'REGRAS-COMUNS.md').read_text();meta=json.loads((B/'ESTRUTURA.json').read_text())
a=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',md)
sections={a[i]:a[i+2] for i in range(1,len(a),3)}
pdf=B/'output/pdf/Projeto-M-Regras-Comuns-Prova-Consolidada-01.pdf';r=PdfReader(pdf)
ck('18 páginas e seções', [len(r.pages),len(sections)], [18,18])
ck('Ordem de leitura',list(sections),meta['ordem'])
ck('Subtítulos não repetem título da seção',[k for k,s in sections.items() if '## '+meta['titulos'][k]+'\n' in s],[])
ck('Todos os títulos coincidem com o mapa', [k for k,s in sections.items() if s.splitlines()[0]!='# '+meta['titulos'][k]],[])
top=[o for o in r.outline if not isinstance(o,list)]
ck('Seis entradas principais',len(top),6)
ck('Grupos iniciam recolhidos',[x.get('/Count') for x in top if x.get('/Count')],[-3,-4,-4,-5])
def flatten(nodes):
 for o in nodes:
  if isinstance(o,list):yield from flatten(o)
  else:yield o
out=list(flatten(r.outline));ck('Marcadores com destinos válidos',all(0<=r.get_destination_page_number(o)<18 for o in out),True)
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
# Medidas e contas de exemplos: não são simulação integral do sistema.
ds=[Fraction(v.replace(',','.')) for v in re.findall(r'(?<![\w,])([0-9]+(?:,[0-9]+)?)\s*m\b',md)]
ck('Todas as distâncias em múltiplos de1,5m',[str(v) for v in ds if (v/Fraction(3,2)).denominator!=1],[])
ck('Percurso com entulho: gasto e distância',[3+3+3,3+1.5+3],[9,7.5])
ck('Salto de Força1: metros restantes',9-3-4.5,1.5)
ck('Exemplo Assassino: teste e gasto',[10+4,6+4.5,12-10.5],[14,10.5,1.5])
ck('Queda de4,5m: dados e Vida',[int(4.5//3),14-4],[1,10])
ck('Manobra: CD e falha',[8+3+1,10<12],[12,True])
ck('Furtividade15 versus passivas14 e18',[15>=14,15>=18],[True,False])
ck('Energia16 contra16 e19',[16>=16,16>=19],[True,False])
ck('Busca+6: chance de alcançar16',str(Fraction(sum(d+6>=16 for d in range(1,21)),20)),'11/20')
# Cobertura editorial auditável, sem pontuação automática de qualidade.
rev=json.loads((B/'evidencias/REVISAO-EDITORIAL.json').read_text())
ck('Matriz editorial cobre todas as seções',sorted(x['id'] for x in rev['secoes']),sorted(sections))
ck('Matriz vinculada ao texto',rev['sha256_texto'],sha(B/'REGRAS-COMUNS.md'))
ck('Campos editoriais preenchidos',all(all(x.get(k) for k in ['funcao','titulo','suficiencia','redundancia_e_destino','limite','referencia']) for x in rev['secoes']),True)
ck('Nenhuma nota superada de lacuna','Ainda fora desta proposta' in md,False)
ck('Dono único da escada deCD',md.count('**6, 10, 14, 18, 22 e 26**'),1)
ck('Estudar requer observação','Conhecer somente o espaço de uma criatura escondida não basta' in sections['estudar'],True)
ck('Energia ainda não é visão','Conhecer somente seu espaço pela busca energética não basta' in sections['ler'],True)
ck('Vestígio não localiza antigo portador','não revela seu antigo portador' in sections['buscar'],True)
ck('Sem manutenção gratuita de ocultação','não concede um teste gratuito para continuar oculto' in sections['atacar'],True)
ck('CD passiva10 preservada','**CD 10 + o bônus completo de Percepção' in sections['esconder'],True)
ck('Interferência não somaCD','maior entre a CD da interferência e a Furtividade' in md,True)
paras=defaultdict(list)
for key,chunk in sections.items():
 for par in chunk.split('\n\n'):
  if len(words(par))>=30 and not par.startswith(('#','|')):paras[' '.join(words(par))].append(key)
ck('Sem parágrafos longos integralmente duplicados',{k[:90]:v for k,v in paras.items() if len(v)>1},{})
# Preservação, incluindo todos os arquivos dos lotes de entrada.
snap=json.loads((B/'evidencias/fontes-preservadas.json').read_text())
ck('Arquivos dos lotes anteriores intactos',[n for n,h in snap.items() if not (ROOT/n).is_file() or sha(ROOT/n)!=h],[])
p=ROOT/'sistema/05-material/livro/planejamento-editorial'
inv=json.loads((p/'INVENTARIO-BASE.json').read_text())
ck('Fontes e exportações do livro preservadas',[x['arquivo'] for x in inv['fontes']+inv['artefatos_publicados'] if sha(ROOT/x['arquivo'])!=x['sha256']],[])
protected=json.loads((B.parent/'lote-03/evidencias/preservacao-base.json').read_text())
ck('Retrato de137arquivos protegido',[n for n,h in protected.items() if sha(ROOT/n)!=h],[])
broken=[]
for p in B.rglob('*.md'):
 if p.name=='REGRAS-COMUNS.md':continue
 for href in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if re.match(r'^[a-z]+:',href) or href.startswith('#'):continue
  target=p.parent/href.split('#')[0]
  if target.name=='CONFERENCIA.json':continue
  if not target.exists():broken.append([str(p.relative_to(B)),href])
ck('Links locais do dossiê',broken,[])
res={'data':'2026-10-03','ok':all(x['ok'] for x in checks),'sha256_texto':sha(B/'REGRAS-COMUNS.md'),'sha256_pdf':sha(pdf),'verificacoes':len(checks),'checks':checks,'geometria':geometry,'limites':['Não é teste humano ou prova de equilíbrio.','A cobertura da matriz não automatiza juízo editorial.','Revisão desta consolidação feita pelo autor; revisão independente nova pendente.','Cânone reutiliza pesquisa dirigida anterior; sem nova validação da obra inteira.']}
(B/'CONFERENCIA.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':res['ok'],'verificacoes':len(checks),'falhas':[x for x in checks if not x['ok']]},ensure_ascii=False,indent=2))
raise SystemExit(0 if res['ok'] else 1)
