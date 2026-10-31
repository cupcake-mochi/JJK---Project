from pathlib import Path
from collections import Counter,defaultdict
from pypdf import PdfReader
import pdfplumber,json,hashlib,runpy,re,sys
from identidade import nome_oficial
B=Path(__file__).resolve().parent
m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());s=json.loads((B/'evidencias/FICHAS-SEPARADAS.json').read_text());g=runpy.run_path(str(B/'ler_fontes.py'))
base=json.loads((B/'evidencias/BASE-POLIMENTO.json').read_text());errors=[];checks=0
def check(ok,label,detail=None):
 global checks
 checks+=1
 if not ok:errors.append({'tipo':label,'detalhe':detail})
def digest(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def source_elements(events,chapters=None):
 return [ {k:e[k] for k in ['bloco','tipo','texto','pagina','x','y','largura','altura','modo']} for e in events if (not chapters or e['capitulo'] in chapters)]
prior=json.loads((B/'evidencias/BASE-ARTES-R23.json').read_text())
def body_by_block(events):
 grouped=defaultdict(list)
 for e in events:
  if e['gerado'] or e['bloco'] is None or e['tipo'] in ['h1','major']:continue
  grouped[e['bloco']].append([e['tipo'], [[nome_oficial(v) for v in row] for row in e['texto']] if isinstance(e['texto'],list) else nome_oficial(e['texto'])])
 return dict(grouped)
check(body_by_block(m['eventos'])==body_by_block(prior['eventos']),'Todos os textos, números, tabelas e exemplos preservados na ordem, sem mudança de regras')
for name,original in prior['imagens']['imagens'].items():
 current=m['imagens']['imagens'].get(name,{})
 for field in ['arquivo','crop','sha256_arquivo','dimensoes_arquivo','largura_mm']:
  check(current.get(field)==original.get(field),'Imagem anterior preservada',{'imagem':name,'campo':field})
 original_pos=next(row for row in prior['posicionamento_imagens'] if row['imagem']==name)
 current_pos=next(row for row in m['posicionamento_imagens'] if row['imagem']==name)
 check(all(current_pos[field]==original_pos[field] for field in ['x','y','largura','altura','crop']),'Composição das imagens anteriores preservada',name)
check(len(m['posicionamento_imagens'])==23,'Quatorze imagens anteriores e nove novas')
check(m['creditos']['pagina']==m['paginas'],'Créditos após todo o livro')
check(m['creditos']['autor']=='Mizuki_sama','Nome informado pelo autor')
check(s['sha256_pdf']==hashlib.sha256((B/s['pdf']).read_bytes()).hexdigest(),'Caderno exato')
book=PdfReader(B/m['pdf']);supp=PdfReader(B/s['pdf']);check(len(supp.pages)==s['paginas'],'Páginas do caderno')
check(len(g['all_blocks'])+len(g['supplement_blocks'])==base['blocos'],'Todos os blocos preservados entre livro e caderno')
check(set(s['blocos'])==set(base['modelos']),'Modelos transferidos completos')
# Termos e destinos do glossário e do índice são conservados, sem verbetes partidos.
for kind,key in [('glossary','glossario'),('indexentry','indice')]:
 rows=[e for e in m['eventos'] if e['tipo']==kind]
 pairs=[]
 for e in rows:
  found=re.match(r'^\[([^\]]+)\]\(#([^)]+)\)',e['texto']);check(bool(found),'Verbetes com destino',e['texto'])
  if found:pairs.append(list(found.groups()))
 check(pairs==base[key],'Todos os termos e destinos preservados na ordem alfabética',key)
 check(all(e['modo']=='duas-colunas' for e in rows),'Consulta em duas colunas',key)
 # Verifica os números do índice no texto real da coluna onde cada entrada foi desenhada.
 if kind=='indexentry':
  with pdfplumber.open(B/m['pdf']) as pp:
   for e,(term,target) in zip(rows,pairs):
    p=pp.pages[e['pagina']-1];box=(e['x']+e['largura']-29,p.height-e['y']-e['altura']-.8,e['x']+e['largura']+.8,p.height-e['y']+.8)
    text=p.crop(box).extract_text() or ''
    check(str(m['ancoras'][target]['pagina'])==text.strip(),'Número do índice corresponde ao destino',{'termo':term,'numero':text})
for block in g['supplement_blocks']:
 rows=[e for e in s['eventos'] if e['bloco']==block.key];check(bool(rows),'Modelo presente',block.key)
 # Conteúdo do suplemento comparado ao modelo integral da versão anterior.
 def clean(t):
  t=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',str(t));return Counter(re.findall(r'\w+|[^\w\s]',t.replace('–','-').replace('—','-').replace('*','').replace('`','').casefold()))
 vals=[]
 for e in rows:
  if e['tipo']=='table':vals.extend(v for row in e['texto'] for v in row)
  else:vals.append(e['texto'])
 check(sum((clean(v) for v in vals),Counter())==clean(' '.join(word for word,count in base['modelos'][block.key].items() for _ in range(count))),'Modelo sem perda de palavras ou campos',block.key)
 texts=' '.join(supp.pages[p-1].extract_text() or '' for p in sorted({e['pagina'] for e in rows}))
 def dense(t):return re.sub(r'\s+','',re.sub(r'[*`]', '', str(t)).replace('–','-').replace('—','-'))
 for val in vals:check(dense(val) in dense(texts),'Texto do modelo desenhado',{'bloco':block.key,'texto':val[:80]})
# Campos e notas não se sobrepõem nem ultrapassam as margens.
by=defaultdict(list)
for e in s['eventos']:
 by[e['pagina']].append(e);check(e['y']>=53 and e['y']+e['altura']<=789 and e['x']>=53 and e['x']+e['largura']<=542,'Modelo dentro da área',e['pagina'])
for pn,rows in by.items():
 for i,a in enumerate(rows):
  for b in rows[i+1:]:
   x=min(a['x']+a['largura'],b['x']+b['largura'])-max(a['x'],b['x']);y=min(a['y']+a['altura'],b['y']+b['altura'])-max(a['y'],b['y']);check(x<=.02 or y<=.02,'Modelo sem sobreposição',pn)
with pdfplumber.open(B/s['pdf']) as pp:
 for pn,p in enumerate(pp.pages,1):
  check(all(c['x0']>=-.2 and c['x1']<=p.width+.2 and c['top']>=-.2 and c['bottom']<=p.height+.2 for c in p.chars),'Glifos do caderno dentro da página',pn)
  check(not any(c['text'] in ['\ufffd','■'] for c in p.chars),'Glifos do caderno completos',pn)
check(len(supp.outline)==len(g['supplement_blocks']),'Atalhos de todos os modelos')
fulltext='\n'.join(p.extract_text() for p in book.pages)
check('________________________________________' not in fulltext,'Modelos fora do livro')
for e in m['eventos']:
 if e['gerado'] and e['tipo'] in ['compactmajor','h3'] and e['capitulo']>=19:
  check(not re.match(r'^(Como ler\b|(?:A|O|As|Os)\s)',str(e['texto']),re.I),'Título de consulta direto',e['texto'])
report={'sha256_pdf':m['sha256_pdf'],'sha256_caderno':s['sha256_pdf'],'checagens':checks,'problemas':errors,'glossario':len(base['glossario']),'indice':len(base['indice']),'blocos_livro':len(g['all_blocks']),'blocos_caderno':len(g['supplement_blocks']),'escopo':'Preservação de todo o texto da R23, quatorze imagens anteriores, termos e destinos de consulta, números reais do índice, integridade do caderno e créditos finais. Sem novo playtest ou avaliação externa.'}
(B/'evidencias/CONFERENCIA-POLIMENTO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='problemas'},ensure_ascii=False));print('Problemas',len(errors));print(json.dumps(errors[:15],ensure_ascii=False,indent=2));sys.exit(bool(errors))
