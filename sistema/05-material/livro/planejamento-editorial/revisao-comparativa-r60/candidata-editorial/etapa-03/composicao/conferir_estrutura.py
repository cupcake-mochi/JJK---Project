"""Validação R30 -> R31: texto registrado, mecânica preservada e geometria."""
from pathlib import Path
from collections import Counter,defaultdict
import hashlib,json,re,unicodedata,sys
from pypdf import PdfReader
import pdfplumber

B=Path(__file__).resolve().parent;R=B/'revisao-de-estrutura';OLD=B.parent/'livro-diagramado-r30'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());oldm=json.loads((OLD/'FONTES-E-VALIDACAO.json').read_text())
pdf=B/m['pdf'];reader=PdfReader(pdf);issues=[];checks=0
def check(ok,kind,detail=None):
 global checks
 checks+=1
 if not ok:issues.append({'tipo':kind,'detalhe':detail})
def clean(s):
 s=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',str(s));s=s.replace('–','-').replace('—','-').replace('−','-')
 return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',s).replace('*','').replace('`','')).strip()
def dense(s):return re.sub(r'\s+','',clean(s)).casefold()
hashes=json.loads((R/'BASE-R30-HASHES.json').read_text())
current={str(p.relative_to(OLD)):sha(p) for p in OLD.rglob('*') if p.is_file()}
check(current==hashes,'R30 integralmente preservada')
for folder in ['fontes-editoriais','referencias','capa','fontes-tipograficas']:
 for p in (OLD/folder).rglob('*'):
  if p.is_file():check(p.read_bytes()==(B/p.relative_to(OLD)).read_bytes(),'Arquivo de origem preservado',str(p.relative_to(OLD)))
for name in ['ORDEM.json','REFERENCIAS.json','ARTES-APLICADAS.json','CAPA-E-ABERTURAS.json','CREDITOS.json','GLOSSARIO-RESUMIDO.json','revisao-textual/ALTERACOES.json','revisao-de-regras/ALTERACOES-REGRAS.json']:
 check((OLD/name).read_bytes()==(B/name).read_bytes(),'Configuração ou histórico preservado',name)
transforms=json.loads((R/'TRANSFORMACOES-TEXTO.json').read_text());hier=json.loads((R/'HIERARQUIA.json').read_text())
def rule_paragraphs(text,key):
 result=[]; marker=hier[key].get('marcador')
 for line in text.splitlines():
  line=line.strip()
  if not line or line.startswith('#') or line=='---':continue
  if marker and line=='**'+marker+'**':continue
  if key=='incursor--inc-continuacoes' and line=='**Continuações**':continue
  if re.fullmatch(r'\*\*(Preço|Categoria de Efeito): [^*]+\*\*',line):continue
  if key.startswith('catalogo--'):
   line=re.sub(r'^\*\*Preço: .*?\.\*\*\s*','',line)
  result.append(clean(line))
 return result
for entry in transforms:
 check(Counter(rule_paragraphs(entry['antes'],entry['bloco']))==Counter(rule_paragraphs(entry['depois'],entry['bloco'])),
       'Parágrafos de regra, tabelas e exemplos integralmente preservados',entry['bloco'])
 if entry['bloco'].startswith('catalogo--'):
  def prices(text):
   values=[clean(s).rstrip('.') for s in re.findall(r'\*\*Preço: ([^*]+)\*\*',text)]
   for label in re.findall(r'^#{1,6} (.+)$',text,re.M):
    label=clean(label)
    if label=='Concentrada - Leve / Duradoura - Média':values.append('Concentrada - Leve; Duradoura - Média')
    else:
     found=re.fullmatch(r'.+?\s+-\s+(Leve|Média|Pesada)',label)
     if found:values.append(found[1])
   return Counter(values)
  check(prices(entry['antes'])==prices(entry['depois']),'Preços de Melhorias preservados',entry['bloco'])
 if entry['bloco'].startswith('rotas--'):
  def categories(text):
   return Counter(re.findall(r'Categoria de Efeito (\d+)',text)+re.findall(r'\*\*Categoria de Efeito: (\d+)\.',text))
  check(categories(entry['antes'])==categories(entry['depois']),'Categorias de Efeito preservadas',entry['bloco'])

pattern=r'<!-- fonte:([^\n]+) -->\n<a id="([^"]+)"></a>\n(.*?)(?=<!-- fonte:|<!-- parte:|<a id="capitulo-|\Z)'
old=(OLD/'LIVRO-COMPLETO.md').read_text();new=(B/'LIVRO-COMPLETO.md').read_text()
before=list(re.finditer(pattern,old,re.S));after=list(re.finditer(pattern,new,re.S))
check([a[2] for a in before]==[a[2] for a in after],'Mesmos 500 blocos e mesma ordem')
reasons={e['bloco']:e['motivo'] for e in transforms};records=[]
rebuilt=old
for a,b in reversed(list(zip(before,after))):
 if a[3]!=b[3]:
  check(a[2] in reasons,'Diferença de Markdown prevista',a[2])
  records.append({'bloco':a[2],'antes':a[3],'depois':b[3],'motivo':reasons.get(a[2],''),'altera_regras':False})
  rebuilt=rebuilt[:a.start(3)]+b[3]+rebuilt[a.end(3):]
records.reverse()
for i,e in enumerate(records,1):e['id']=f'E{i:03d}'
(R/'ALTERACOES-ESTRUTURA.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
check(rebuilt==new,'Reconstrução integral do Markdown pelo registro')
check(len(records)==len(transforms),'Todas as transformações registradas no texto consolidado',{'transformacoes':len(transforms),'blocos_md':len(records)})

events=defaultdict(list);old_events=defaultdict(list);by_page=defaultdict(list)
for e in m['eventos']:
 by_page[e['pagina']].append(e)
 if e['bloco'] in hier:events[e['bloco']].append(e)
for e in oldm['eventos']:
 if e['bloco'] in hier:old_events[e['bloco']].append(e)
pagetypes={p['pagina']:p['tipo'] for p in m['paginas_planejadas']}
for key,rows in events.items():
 source=[e for e in rows if not e['gerado']]
 for i,e in enumerate(source[:-1]):
  if (e['tipo'].startswith('h') or e['tipo'] in ['major','marker','cost']) and pagetypes[e['pagina']]=='content':
   f=source[i+1]
   check(e['pagina']==f['pagina'] and abs(e['x']-f['x'])<.01,'Título ou metadado acompanha a explicação',{'bloco':key,'titulo':e['texto'],'pagina':e['pagina']})
def word_tokens(s):
 return re.findall(r'\w+|[^\w\s]',clean(re.sub(r'^[#>•]+\s*','',str(s))).casefold())
for match in after:
 key=match[2];expected=[]
 for i,line in enumerate(match[3].splitlines()):
  line=line.strip()
  if not line or line=='---' or (i==0 and line.startswith('#')):continue
  if line.startswith('|'):
   if re.fullmatch(r'[\s|:\-]+',line):continue
   expected.extend(v.strip() for v in line.strip('|').split('|'))
  else:expected.append(re.sub(r'^- ','• ',line))
 actual=[]
 for e in events[key]:
  if e['gerado'] or e['tipo']=='esquema':continue
  actual.extend(v for row in e['texto'] for v in row) if e['tipo']=='table' else actual.append(e['texto'])
 missing=Counter(t for s in expected for t in word_tokens(s))-Counter(t for s in actual for t in word_tokens(s))
 check(not missing,'Conteúdo integral de cada bloco no plano',{'bloco':key,'faltam':dict(missing)})
 check(key in m['ancoras'],'Âncora de cada bloco preservada',key)
layout=[]
def coords(rows):
 return [{k:e.get(k) for k in ['pagina','tipo','texto','x','y','largura','altura','modo','faixa','gerado']} for e in rows]
for key in hier:
 a=coords(old_events[key]);b=coords(events[key])
 if a!=b:
  layout.append({'id':f'D{len(layout)+1:03d}','bloco':key,'paginas_antes':sorted({e['pagina'] for e in a}),
      'paginas_depois':sorted({e['pagina'] for e in b}),'antes':a,'depois':b,
      'motivo':'Colunas contínuas, papéis dos títulos, contexto de continuação e nova paginação; conforme HIERARQUIA.json.',
      'altera_regras':False})
(R/'ALTERACOES-DIAGRAMACAO.json').write_text(json.dumps(layout,ensure_ascii=False,indent=2)+'\n')
check(len(reader.pages)==m['paginas'],'Contagem de páginas')
check(sha(pdf)==m['sha256_pdf'],'PDF exato')
for e in m['eventos']:
 check(e['y']>=100 and e['y']+e['altura']<=789,'Conteúdo na área útil',{'pagina':e['pagina'],'bloco':e['bloco'],'tipo':e['tipo'],'y':e['y']})
 check(e['x']>=53 and e['x']+e['largura']<=542,'Margens do conteúdo',{'pagina':e['pagina'],'bloco':e['bloco']})
for page,rows in by_page.items():
 for i,e in enumerate(rows):
  for f in rows[i+1:]:
   dx=min(e['x']+e['largura'],f['x']+f['largura'])-max(e['x'],f['x'])
   dy=min(e['y']+e['altura'],f['y']+f['altura'])-max(e['y'],f['y'])
   check(dx<=.02 or dy<=.02,'Elementos sem sobreposição',{'pagina':page,'blocos':[e['bloco'],f['bloco']]})
 # No new pair of columns below another pair without a real wide element.
 bands=[]
 for e in rows:
  band=e.get('faixa')
  if band is not None and band not in bands:bands.append(band)
 for first,second in zip(bands,bands[1:]):
  a=[e for e in rows if e.get('faixa')==first];b=[e for e in rows if e.get('faixa')==second]
  if any(e['modo']=='duas-colunas' for e in a) and any(e['modo']=='duas-colunas' for e in b):
   check(False,'Retorno entre faixas de colunas sem separação larga',page)
pageids={p.indirect_reference.idnum:i+1 for i,p in enumerate(reader.pages)};links=0
for i,p in enumerate(reader.pages,1):
 for ref in p.get('/Annots',[]):
  a=ref.get_object();dest=a.get('/Dest')
  if a.get('/Subtype')=='/Link' and dest is not None:
   links+=1;check(hasattr(dest[0],'idnum') and dest[0].idnum in pageids,'Link interno válido',i)
outline=[]
def visit(items):
 for row in items:
  if isinstance(row,list):visit(row)
  else:outline.append(row)
visit(reader.outline)
check(len(outline)==len(m['marcadores'])==len(oldm['marcadores']),'Marcadores preservados')
for row in outline:
 page=reader.get_destination_page_number(row)+1
 check(any(x['titulo']==row.title and x['pagina']==page for x in m['marcadores'].values()),'Marcador na página correta',row.title)
destinations=json.loads((R/'DESTINOS-INDICE.json').read_text())
for row in destinations:
 pos=m['ancoras'].get(row['alias']);check(pos is not None,'Destino específico do índice',row)
 if pos:
  match=[e for e in events[row['bloco']] if e['texto']==row['termo'] and e['tipo'].startswith('h')]
  check(len(match)==1 and match[0]['pagina']==pos['pagina'],'Índice na página do título',row['termo'])
  row['pagina_r31']=pos['pagina']
(R/'DESTINOS-INDICE.json').write_text(json.dumps(destinations,ensure_ascii=False,indent=2)+'\n')

# Check the text actually painted by ReportLab, rather than only the layout plan.
texts=[p.extract_text() or '' for p in reader.pages]
for key,rows in events.items():
 extracted=dense(' '.join(texts[i-1] for i in sorted({e['pagina'] for e in rows})))
 for e in rows:
  if e['tipo']=='esquema':continue
  pieces=[v for row in e['texto'] for v in row] if e['tipo']=='table' else [e['texto']]
  for s in pieces:
   val=dense(s).lstrip('•>')
   if val:check(val in extracted,'Texto efetivamente presente no PDF',{'bloco':key,'pagina':e['pagina'],'texto':str(s)[:120]})
with pdfplumber.open(pdf) as pp:
 for i,p in enumerate(pp.pages,1):
  check(all(c['x0']>=-.2 and c['x1']<=p.width+.2 and c['top']>=-.2 and c['bottom']<=p.height+.2 for c in p.chars),'Glifos dentro da página',i)
  check(not any(c['text'] in ['\ufffd','■'] for c in p.chars),'Sem glifos faltantes',i)
for art in m['posicionamento_imagens']:
 for e in by_page[art['pagina']]:
  dx=min(art['x']+art['largura'],e['x']+e['largura'])-max(art['x'],e['x'])
  dy=min(art['y']+art['altura'],e['y']+e['altura'])-max(art['y'],e['y'])
  check(dx<=.02 or dy<=.02,'Arte separada do texto',{'pagina':art['pagina'],'imagem':art['imagem']})
check(len(m['capas_e_aberturas'])==len(oldm['capas_e_aberturas'])==22,'Mesmas capas e aberturas')
check({a['imagem'] for a in m['posicionamento_imagens']}=={a['imagem'] for a in oldm['posicionamento_imagens']},'Mesmas ilustrações existentes')
forbidden=['suas fichas','não tem como recusar']
for value in forbidden:check(value not in new.casefold(),'Expressão vedada ausente',value)
report={'checagens':checks,'problemas':issues,'r30_preservada':current==hashes,
 'paginas_r30':oldm['paginas'],'paginas_r31':m['paginas'],'blocos':len(hier),
 'blocos_texto_registrados':len(records),'blocos_diagramacao_registrados':len(layout),
 'remissoes_indice_especificas':len(destinations),'links_internos':links,
 'texto_mecanico_preservado':not any(e['tipo'].startswith('Parágrafos') for e in issues),
 'sha256_pdf':sha(pdf),'sha256_markdown':sha(B/'LIVRO-COMPLETO.md'),
 'escopo':'Registro integral das diferenças R30 -> R31, conservação dos parágrafos de regra, arquivos de origem, geometria, links e texto extraído. Revisão visual registrada separadamente.'}
(R/'VERIFICACAO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['problemas','escopo']},ensure_ascii=False,indent=2))
print('Problemas:',len(issues));print(json.dumps(issues[:15],ensure_ascii=False,indent=2))
sys.exit(bool(issues))
