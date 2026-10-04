#!/usr/bin/env python3
"""QA estrutural do livro reunido. Não certifica V14 nem balanço das regras."""
from pathlib import Path
from collections import Counter
import hashlib,json,re,unicodedata,sys
import pdfplumber
from pypdf import PdfReader
B=Path(__file__).resolve().parent;P=B.parents[1];E=B/'evidencias';pdf=B/'output/pdf/Projeto-M-Livro-Completo-Candidata.pdf';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=[]
def ck(n,a,b):checks.append({'teste':n,'obtido':a,'esperado':b,'ok':a==b})
def tokens(s):return re.findall(r'\w+',unicodedata.normalize('NFKC',s).casefold())
gen=json.loads((E/'GERACAO.json').read_text());mapping=json.loads((E/'MAPA-BLOCOS.json').read_text());pages=json.loads((E/'PAGINAS-DESTINOS.json').read_text());reader=PdfReader(pdf)
ck('PDF atual',sha(pdf),gen['sha256_pdf']);ck('Markdown atual',sha(B/'LIVRO-COMPLETO.md'),gen['sha256_manuscrito']);ck('Nenhuma omissão',gen['omitidos'],[]);ck('Nenhum bloco duplicado',gen['duplicados'],[]);ck('Blocos únicos',len({x['id_livro'] for x in mapping}),gen['blocos_esperados']);ck('Blocos mapeados',len(mapping),gen['blocos_esperados']);ck('Paginação convergiu',gen['passagens'][-1]['mapa_estavel'],True)
ck('Destinos correntes resolvidos',gen['destinos_pendentes'],0);ck('Fontes não mudaram durante execução',gen['fontes_mudaram_durante_geracao'],[]);ck('Mapa não mudou durante execução',gen['destinos_mudaram_durante_geracao'],False)
changed=[key for key,v in gen['fontes'].items() if sha(P/v['arquivo'])!=v['sha256_lido']];ck('Fontes continuam atuais',changed,[])
ck('Mapa de destinos continua atual',sha(P/'consulta/lote-01/evidencias/DESTINOS.json'),gen['destinos_sha256']);ck('Ordem continua atual',sha(B/'ORDEM.json'),gen['sha256_ordem']);ck('Gerador da prova',sha(B/'gerar_livro.py'),gen['sha256_gerador'])
for name,digest in gen['fontes_tipograficas'].items():ck('Fonte tipográfica '+name,sha((B/'fontes-tipograficas')/name),digest)
outline=[]
def walk(nodes,level=0):
 for item in nodes:
  if isinstance(item,list):walk(item,level+1)
  else:outline.append({'titulo':item.title,'nivel':level,'pagina':reader.get_destination_page_number(item)+1,'count':item.get('/Count')})
walk(reader.outline);ck('Cinco partes',sum(x['nivel']==0 for x in outline),5);ck('21 capítulos',sum(x['nivel']==1 for x in outline),21);ck('Seis Caminhos',sum(x['nivel']==2 for x in outline),6);ck('Nenhuma seção despejada no painel',len(outline),32);ck('Partes recolhidas',all(x['count']<0 for x in outline if x['nivel']==0),True);ck('Destinos do painel existentes',all(1<=x['pagina']<=len(reader.pages) for x in outline),True)
ids={p.indirect_reference.idnum:i+1 for i,p in enumerate(reader.pages)};texts=[];geometria=[];links=[];chars_count=0
with pdfplumber.open(pdf) as doc:
 for i,p in enumerate(doc.pages,1):
  text=p.extract_text(x_tolerance=1,y_tolerance=3) or '';texts.append(text);cs=[c for c in p.chars if c['text'].strip()];chars_count+=len(cs)
  ck(f'p{i}: texto pesquisável',len(text)>20,True)
  ck(f'p{i}: caracteres dentro da página',all(-.2<=c['x0']<=c['x1']<=p.width+.2 and -.2<=c['top']<=c['bottom']<=p.height+.2 for c in cs),True)
  body=[c for c in cs if 48<c['top']<785]
  ck(f'p{i}: corpo acima do rodapé',not body or max(c['bottom'] for c in body)<786,True)
  embedded=set()
  for fr in reader.pages[i-1]['/Resources']['/Font'].values():
   fo=fr.get_object();desc=fo.get('/FontDescriptor')
   if desc and any(k in desc.get_object() for k in ['/FontFile','/FontFile2','/FontFile3']):embedded.add(str(fo['/BaseFont']).lstrip('/'))
  ck(f'p{i}: fontes usadas incorporadas',sorted({c['fontname'] for c in cs}-embedded),[])
  ck(f'p{i}: sem raster artístico',len(p.images),0)
  for ar in reader.pages[i-1].get('/Annots',[]):
   a=ar.get_object();dest=a.get('/Dest')
   if a.get('/Subtype')=='/Link' and dest:
    target=ids.get(dest[0].idnum);links.append({'origem':i,'destino':target});ck(f'p{i}: destino de link {len(links)}',target is not None,True)
  geometria.append({'pagina':i,'caracteres':len(text),'fim_corpo':round(max([c['bottom'] for c in body],default=0),2)})
  if i%50==0:print(f'QA: {i}/{len(doc.pages)} páginas',flush=True)
# Text completeness by source block in its mapped interval, permitting repeated table headers.
md=(B/'LIVRO-COMPLETO.md').read_text();parts=re.split(r'<!-- fonte:([^>]+) -->\s*<a id="([^"]+)"></a>\s*',md);contents={}
for i in range(1,len(parts),3):
 source,key,text=parts[i:i+3];text=re.split(r'<!-- parte:|<a id="capitulo-',text)[0];contents[key]=text
# Comparação independente do conteúdo derivado contra a captura da fonte.
def block_text(s,gloss=False):
 s=re.sub(r'\[([^\]]+)\]\(#[^)]+\)',r'\1',s)
 if gloss:s=re.sub(r'\*\*Consulta:\*\*[^\n]*','',s)
 return tokens(s)
source_blocks={}
for doc,v in gen['fontes'].items():
 captured=E/'fontes-capturadas'/f'{doc}.md'
 ck('Captura confere '+doc,sha(captured),v['sha256_lido'])
 for a,title,body in re.findall(r'<!-- page:([^|]+)\|([^>]+) -->\s*(.*?)(?=<!-- page:|\Z)',captured.read_text(),re.S):source_blocks[doc+'--'+a.strip()]=body.strip()
ck('Inventário independente',sorted(source_blocks),sorted(m['id_livro'] for m in mapping))
for m in mapping:
 key=m['id_livro'];src=source_blocks[key]
 if m['cabecalho_inicial_unificado']:src='\n'.join(src.splitlines()[1:])
 # Novo texto de destino do glossário é somente remissão; o corpo deve permanecer igual.
 ck('Fonte preservada '+key,block_text(contents[key],key.startswith('consulta--consulta-glossario-')),block_text(src,key.startswith('consulta--consulta-glossario-')))
for ix,m in enumerate(mapping):
 key=m['id_livro'];source=contents[key];source=re.sub(r'\[([^\]]+)\]\(#[^)]+\)',r'\1',source);source=re.sub(r'<[^>]+>','',source)
 start=m['pagina'];end=mapping[ix+1]['pagina'] if ix+1<len(mapping) else len(reader.pages)
 actual='\n'.join(texts[start-1:end]);missing=Counter(tokens(source))-Counter(tokens(actual));ck('Bloco completo '+key,dict(missing),{})
# Tabela partida: nenhum pedaço com menos de duas linhas, e título com até quatro linhas não fica no pé longe da tabela.
INK=(0.145098,0.090196,0.152941);same=lambda c:c is not None and len(c)==3 and all(abs(x-y)<.01 for x,y in zip(c,INK))
def layout(p):
 rs=sorted([r for r in p.rects if r['height']>5],key=lambda r:r['top']);fr=[];used=set();words=p.extract_words()
 for i,r in enumerate(rs):
  if not same(r.get('non_stroking_color')) or i in used:continue
  n=0;end=r['bottom'];j=i+1
  while j<len(rs) and abs(rs[j]['top']-end)<=.6 and abs(rs[j]['x0']-r['x0'])<=.6 and abs(rs[j]['width']-r['width'])<=.6 and not same(rs[j].get('non_stroking_color')):used.add(j);n+=1;end=rs[j]['bottom'];j+=1
  fr.append({'topo':r['top'],'fim':end,'linhas':n,'cab':' '.join(w['text'] for w in words if w['top']>=r['top']-1 and w['bottom']<=r['bottom']+1 and w['x0']>=r['x0'])})
 lines={}
 for c in p.chars:
  if 45<c['top']<786:lines.setdefault(round(c['top']),[]).append(c)
 return fr,sorted(lines.items())
def heading(cs):return all('Barlow' in c['fontname'] for c in cs if c['text'].strip()) and max(c['size'] for c in cs)>=13.5
with pdfplumber.open(pdf) as doc:L=[layout(p) for p in doc.pages]
table_issues=[]
for i in range(len(L)-1):
 (fr,ln),(nf,nl)=L[i],L[i+1]
 if not nf:continue
 g=nf[0];before=[k for k,_ in nl if k<g['topo']-1]
 if before:continue
 cut=fr and fr[-1]['cab']==g['cab'] and not [k for k,_ in ln if k>fr[-1]['fim']+1]
 if cut:
  if fr[-1]['linhas']<2:table_issues.append(['linha órfã no pé',i+1,g['cab']])
  nxt=L[i+2] if i+2<len(L) else None
  goes_on=nxt and nxt[0] and nxt[0][0]['cab']==g['cab'] and not [k for k,_ in nl if k>g['fim']+1] and not [k for k,_ in nxt[1] if k<nxt[0][0]['topo']-1]
  if g['linhas']<2 and not goes_on:table_issues.append(['linha viúva no alto',i+2,g['cab']])
 else:
  top=max([f['fim'] for f in fr],default=0);hs=[n for n,(k,cs) in enumerate(ln) if heading(cs) and k>top]
  if hs and len(ln)-1-hs[-1]<=4:table_issues.append(['título longe da tabela',i+1,''.join(c['text'] for c in ln[hs[-1]][1]).strip()])
ck('Tabelas sem linha órfã ou viúva e com o título junto',table_issues,[])
lone=[]
for i,(fr,ln) in enumerate(L[:-1]):
 hs=[n for n,(k,cs) in enumerate(ln) if heading(cs)]
 if hs and len(ln)-1-hs[-1]<=1 and not [f for f in fr if f['topo']>ln[hs[-1]][0]]:lone.append([i+1,''.join(c['text'] for c in ln[hs[-1]][1]).strip()])
ck('Nenhum título com uma linha só no pé da página',lone,[])
# Front index links and page references are generated from this exact map.
ck('Todas âncoras de bloco possuem página',all(m['id_livro'] in pages and 1<=pages[m['id_livro']]<=len(reader.pages) for m in mapping),True)
result={'sha256_pdf':sha(pdf),'sha256_manuscrito':sha(B/'LIVRO-COMPLETO.md'),'ok':all(x['ok'] for x in checks),'verificacoes':len(checks),'paginas':len(reader.pages),'blocos':len(mapping),'links_internos':len(links),'caracteres_pdf':chars_count,'checks':checks,'falhas':[x for x in checks if not x['ok']],'painel':outline,'geometria':geometria,'limites':['Verificação estrutural não substitui abrir todas as páginas nem reavaliar regras.','Contagem de palavras por intervalo detecta omissões, mas não comprova ordem semântica ou ausência de redundância autoral.','Não foi executado playtest ou leitura humana.']}
(E/'QA-ESTRUTURAL.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');(E/'TEXTO-DO-PDF.txt').write_text('\n\f\n'.join(texts));print(json.dumps({k:v for k,v in result.items() if k not in ['checks','geometria','painel']},ensure_ascii=False),flush=True)
raise SystemExit(0 if result['ok'] else 1)
