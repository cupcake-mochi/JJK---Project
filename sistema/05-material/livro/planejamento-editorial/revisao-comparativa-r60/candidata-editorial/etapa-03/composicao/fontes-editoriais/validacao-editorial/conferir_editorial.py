"""Bloqueio editorial de títulos e conteúdo fora de seu dono. Sem dependências externas."""
from pathlib import Path
import argparse,hashlib,html,json,re,sys,unicodedata
B=Path(__file__).resolve().parent;P=B.parent;R=B.parents[1]/'fontes-projeto'
def normal(s):
 return ' '.join(''.join(c for c in unicodedata.normalize('NFKD',s) if not unicodedata.combining(c)).split())
def visible(s):
 s=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',s)
 return html.unescape(re.sub(r'<[^>]*>|[*`_]','',s))
def paragraphs(text):
 return [normal(visible(p)).casefold() for p in re.split(r'\n\s*\n',text) if len(normal(visible(p)).split())>=24 and not p.lstrip().startswith(('#','|'))]

def title_headings(text):
 """Visible headings, preserving accents and source line numbers.

 E007 ignores quoted material, comments and code. This deliberately does not
 normalize accents: the preposition À is not the article A.
 """
 def blank(match):return re.sub(r'[^\n]', ' ', match.group())
 text=re.sub(r'<!--.*?-->',blank,text,flags=re.S)
 text=re.sub(r'<blockquote\b[^>]*>.*?</blockquote\s*>',blank,text,flags=re.I|re.S)
 text=re.sub(r'<(pre|code)\b[^>]*>.*?</\1\s*>',blank,text,flags=re.I|re.S)
 lines=text.splitlines();clean=[];fence=None
 for line in lines:
  if re.match(r'^ {0,3}>',line):clean.append('');continue
  if fence:
   if re.match(r'^ {0,3}'+re.escape(fence[0])+'{'+str(fence[1])+r',}\s*$',line):fence=None
   clean.append('');continue
  fm=re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$',line)
  if fm:
   fence=(fm[1][0],len(fm[1]));clean.append('');continue
  # Four leading spaces or a tab are an indented code block here.
  clean.append('' if line.startswith(('    ','\t')) else line)
 masked='\n'.join(clean);found=[];html_lines=set()
 for match in re.finditer(r'<h([1-6])\b[^>]*>(.*?)</h\1\s*>',masked,re.I|re.S):
  start=masked[:match.start()].count('\n')+1
  end=start+match.group().count('\n');html_lines.update(range(start,end+1))
  found.append({'linha':start,'titulo':' '.join(visible(match[2]).split()),'formato':'html'})
 for i,line in enumerate(clean):
  if i+1 in html_lines:continue
  atx=re.match(r'^ {0,3}#{1,6}(?:[ \t]+|$)(.*?)(?:[ \t]+#+[ \t]*)?$',line)
  if atx:
   found.append({'linha':i+1,'titulo':' '.join(visible(atx[1]).split()),'formato':'atx'})
  elif line.strip() and i+1<len(clean) and re.match(r'^ {0,3}(?:=+|-+)\s*$',clean[i+1]):
   if not re.match(r'^ {0,3}(?:[-+*]\s|\d+[.)]\s)',line):
    found.append({'linha':i+1,'titulo':' '.join(visible(line).split()),'formato':'setext'})
 return sorted(found,key=lambda item:item['linha'])

def scan_title_articles(text):
 issues=[]
 for heading in title_headings(text):
  title=heading['titulo']
  # Numeric section labels do not hide an initial article in the title itself.
  match=re.match(r'^(?P<prefixo>\d+(?:\.\d+)*[.)]?\s+(?:[—–-]\s*)?)?(?P<artigo>A|O|As|Os)(?=\s|$)',title,re.I)
  if match:
   issues.append({'codigo':'E007','linha':heading['linha'],'termo':match['artigo'],'titulo':title,'trecho':title,'formato':heading['formato'],'motivo':'Título começa com artigo definido A, O, As ou Os; usar um título direto, com revisão contextual.'})
 return issues

def foreign_name_matches(s, entry, domain, registry):
 """A complete name owned by this domain takes precedence over its shorter homonym."""
 term=normal(entry['termo']);flags=0 if entry.get('sensivel_a_caixa') else re.I
 matches=list(re.finditer(r'(?<!\w)'+re.escape(term)+r'(?!\w)',s,flags))
 if not matches:return []
 owned_spans=[]
 for own in registry:
  if domain not in own['donos']:continue
  full=normal(own['termo'])
  if len(full)<=len(term):continue
  own_flags=0 if own.get('sensivel_a_caixa') else re.I
  owned_spans.extend(m.span() for m in re.finditer(r'(?<!\w)'+re.escape(full)+r'(?!\w)',s,own_flags))
 return [m for m in matches if not any(a<=m.start() and m.end()<=b for a,b in owned_spans)]

def scan(text,domain,registry,blocks=()):
 issues=scan_title_articles(text);lines=text.splitlines();fence=None;prose=[]
 for i,line in enumerate(lines):
  stripped=line.lstrip()
  fm=re.match(r'(`{3,}|~{3,})',stripped)
  if fm:
   if fence is None:fence=fm[1][0]
   elif fm[1][0]==fence:fence=None
   continue
  if fence:continue
  if stripped.startswith('<!--'):continue
  raw=visible(line);s=normal(raw);prose.append((i+1,line,raw))
  heading=bool(re.match(r'^\s{0,3}#{1,6}(?:\s|$)',line) or re.search(r'<h[1-6][ >]',line,re.I) or (i+1<len(lines) and re.match(r'^\s*(?:={3,}|-{3,})\s*$',lines[i+1])))
  if heading and re.search(r'\bcomo\s+ler\b',s,re.I):
   issues.append({'codigo':'E001','linha':i+1,'termo':'Como ler','trecho':raw.strip(),'motivo':'Título explicativo proibido; usar o nome do assunto.'})
  for entry in registry:
   if domain in entry['donos']:continue
   term=normal(entry['termo'])
   if entry.get('somente_nome_marcado') and not (heading or re.search(r'(?:\*\*|`)' + re.escape(term) + r'(?:\*\*|`)',normal(line),re.I)):
    continue
   flags=0 if entry.get('sensivel_a_caixa') else re.I
   left=[];right=[]
   for j in range(i-1,max(-1,i-3),-1):
    part=normal(visible(lines[j]))
    if not part or lines[j].lstrip().startswith(('<!--','```','~~~','#')):break
    left.insert(0,part)
   for j in range(i+1,min(len(lines),i+3)):
    part=normal(visible(lines[j]))
    if not part or lines[j].lstrip().startswith(('<!--','```','~~~','#')):break
    right.append(part)
   prefix=' '.join(left);offset=len(prefix)+(1 if prefix else 0)
   context=' '.join(left+[s]+right)
   if any(offset<=m.start() and m.end()<=offset+len(s) for m in foreign_name_matches(context,entry,domain,registry)):
    issues.append({'codigo':'E002','linha':i+1,'termo':entry['termo'],'donos':entry['donos'],'trecho':raw.strip(),'motivo':'Nome específico fora de seu domínio editorial; explicação deve ficar com o dono.'})
 # A name wrapped across source lines remains the same editorial reference.
 for idx in range(len(prose)-1):
  window=prose[idx:idx+3]
  if not window[0][2].strip():continue
  adjacent=[window[0]]
  for row in window[1:]:
   if row[0]!=adjacent[-1][0]+1 or not row[2].strip():break
   adjacent.append(row)
  joined=normal(' '.join(x[2] for x in adjacent))
  for entry in registry:
   if domain in entry['donos'] or entry.get('somente_nome_marcado'):continue
   term=normal(entry['termo']);flags=0 if entry.get('sensivel_a_caixa') else re.I
   pattern=r'(?<!\w)'+re.escape(term)+r'(?!\w)'
   if foreign_name_matches(joined,entry,domain,registry) and not any(foreign_name_matches(normal(x[2]),entry,domain,registry) for x in adjacent):
    if not any(x.get('termo')==entry['termo'] and x.get('linha')==window[0][0] for x in issues):
     issues.append({'codigo':'E002','linha':window[0][0],'termo':entry['termo'],'donos':entry['donos'],'trecho':joined,'motivo':'Nome específico fora do domínio, dividido entre linhas.'})
 # 24-word sequence catches copied prose even when the ability name was removed.
 clean=normal(visible(text)).casefold();tokens=re.findall(r'\w+',clean);ngrams={' '.join(tokens[i:i+24]) for i in range(max(0,len(tokens)-23))}
 for owner,source,block in blocks:
  if domain==owner:continue
  ts=re.findall(r'\w+',block)
  hit=next((' '.join(ts[i:i+24]) for i in range(max(0,len(ts)-23)) if ' '.join(ts[i:i+24]) in ngrams),None)
  if hit:
   issues.append({'codigo':'E003','linha':None,'termo':'Trecho repetido','dono':owner,'fonte':source,'trecho':hit,'motivo':'Sequência de24 palavras de texto de habilidade repetida fora do dono.'})
 return issues

def scan_vocabulary(text):
 """Return contextual alerts, with no automatic rewrite or reading-level claim."""
 entries=json.loads((B/'VOCABULARIO.json').read_text())['termos'];issues=[];fence=None
 for number,line in enumerate(text.splitlines(),1):
  fm=re.match(r'^\s*(`{3,}|~{3,})',line)
  if fm:
   if fence is None:fence=fm[1][0]
   elif fence==fm[1][0]:fence=None
   continue
  if fence or line.lstrip().startswith('<!--'):continue
  plain=normal(visible(line))
  for entry in entries:
   if re.search(r'(?<!\w)'+re.escape(normal(entry['termo']))+r'(?!\w)',plain,re.I):
    issues.append({'codigo':'E005','linha':number,'termo':entry['termo'],'trecho':plain,'motivo':'Vocabulário potencialmente ambíguo ou pouco familiar; avaliar o sentido no contexto.','sugestao':entry['sugestao']})
 return issues

def configuration():
 reg=json.loads((B/'DONOS.json').read_text());docs=json.loads((B/'MANUSCRITOS.json').read_text())['documentos'];blocks=[]
 for src in reg['fontes_de_blocos']:
  p=R/src;owner=p.stem.split('-')[1].casefold()
  blocks.extend((owner,src,x) for x in paragraphs(p.read_text()))
 return reg['termos'],docs,blocks

def check_file(path,require_review=False):
 path=Path(path).resolve();reg,docs,blocks=configuration()
 entry=next((d for d in docs if (P/d['arquivo']).resolve()==path),None)
 if entry is None:return [{'codigo':'E000','linha':None,'motivo':'Manuscrito sem domínio no cadastro. Registrar antes de exportar.','arquivo':str(path)}]
 issues=scan(path.read_text(),entry['dominio'],reg,blocks)
 vocabulary=scan_vocabulary(path.read_text())
 try:
  wording=json.loads((path.parent/'evidencias/LOCALIZACAO-EDITORIAL.json').read_text())
  fresh=wording.get('sha256_texto')==hashlib.sha256(path.read_bytes()).hexdigest()
 except (OSError,json.JSONDecodeError):wording={};fresh=False
 # A requisito or incompatibilidade sometimes must name another chapter's
 # concept. Admit only a reviewed exact excerpt in the current manuscript.
 # This never waives copied prose (E003), headings or vocabulary review.
 issues=filter_location_references(issues,wording if fresh else {})
 exceptions=wording.get('excecoes_vocabulario',[]) if fresh else []
 for finding in vocabulary:
  justified=any(e.get('linha')==finding['linha'] and e.get('termo')==finding['termo'] and str(e.get('justificativa','')).strip() for e in exceptions)
  if not justified:issues.append(finding)
 if require_review and not (fresh and wording.get('vocabulario_revisto') is True):
  issues.append({'codigo':'E006','linha':None,'motivo':'Revisão contextual de vocabulário ausente ou desatualizada; avaliar também palavras fora do cadastro.'})
 if require_review:
  review=path.parent/'evidencias/LOCALIZACAO-EDITORIAL.json'
  try:
   data=json.loads(review.read_text());good=data['sha256_texto']==hashlib.sha256(path.read_bytes()).hexdigest() and data['titulos_revisto'] and data['sem_explicacao_alheia'] and data['revisor']
  except (OSError,KeyError,json.JSONDecodeError):good=False
  if not good:issues.append({'codigo':'E004','linha':None,'motivo':'Revisão contextual de títulos/localização ausente ou desatualizada. Não basta passar a busca de nomes.'})
 for x in issues:x['arquivo']=entry['arquivo']
 return issues

def filter_location_references(issues,wording):
 permitted={'requisito','incompatibilidade','remissao'}
 exceptions=wording.get('excecoes_localizacao',[])
 def justified(finding):
  if finding.get('codigo')!='E002':return False
  return any(e.get('termo')==finding.get('termo')
             and e.get('trecho')==finding.get('trecho')
             and e.get('papel') in permitted
             and str(e.get('justificativa','')).strip()
             and e.get('nao_reproduz_regra') is True for e in exceptions)
 return [f for f in issues if not justified(f)]

def assert_exportable(path):
 issues=check_file(path,require_review=True)
 if issues:raise RuntimeError('Exportação bloqueada pela revisão editorial:\n'+json.dumps(issues,ensure_ascii=False,indent=2))

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('arquivos',nargs='*');ap.add_argument('--exportacao',action='store_true');ap.add_argument('--saida');args=ap.parse_args()
 _,docs,_=configuration();paths=[Path(x) for x in args.arquivos] if args.arquivos else [P/d['arquivo'] for d in docs]
 issues=[]
 for path in paths:
  try:issues.extend(check_file(path,args.exportacao))
  except OSError as e:issues.append({'codigo':'E000','arquivo':str(path),'motivo':str(e)})
 result={'ok':not issues,'documentos':len(paths),'achados':len(issues),'itens':issues,'limites':'Nomes dependem do cadastro; cópia detectada por24 palavras; paráfrases exigem revisão contextual. O parecer exigido na exportação é evidência de leitura, não prova automática de compreensão.'}
 if args.saida:Path(args.saida).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(result if not args.saida else {k:v for k,v in result.items() if k!='itens'},ensure_ascii=False,indent=2))
 sys.exit(0 if result['ok'] else 1)
