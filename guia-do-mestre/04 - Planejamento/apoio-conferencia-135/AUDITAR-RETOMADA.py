from pathlib import Path
import json,hashlib,re,collections,unicodedata
from urllib.parse import unquote,urlsplit
from bs4 import BeautifulSoup
import markdown

R=Path(__file__).resolve().parents[2]
A=R/'04 - Planejamento/apoio-conferencia-135';S=R/'06 - Redacao do Guia/revisao-98';B=A/'retomada/antes-do-fechamento'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((B/'manifesto-entrega.json').read_text())
changes=json.loads((B/'fontes-alteradas-pelo-claude.json').read_text())
allowed={str((S/f).relative_to(R)) for f in changes}
control=json.loads((R/'04 - Planejamento/apoio-revisao-textual-134/arquivos-do-lote.json').read_text())['controles']
allowed.update(control)
allowed.update(json.loads((A/'arquivos-do-lote.json').read_text()).get('extras',[]))
fail=[];changed=[]
for i,(rel,h) in enumerate(base.items(),1):
 p=R/rel
 if not p.is_file():fail.append({'arquivo':rel,'erro':'ausente'});continue
 if sha(p)!=h:
  if rel in allowed:changed.append(rel)
  else:fail.append({'arquivo':rel,'erro':'alterado fora do escopo'})
 if i%800==0:print('manifesto conferido',i,'/',len(base),flush=True)
for f in changes:
 p=A/'antes'/f;rel=str((S/f).relative_to(R))
 if sha(p)!=base[rel]:fail.append({'arquivo':rel,'erro':'snapshot do Claude diverge da base anterior'})
log=json.loads((A/'alteracoes.json').read_text())
texts={p.relative_to(A/'antes').as_posix():p.read_text() for p in (A/'antes').rglob('*.md')}
link_target=re.compile(r'(\]\(<?[^)>]*>?\))')
for n,e in enumerate(log,1):
 f=e['arquivo'];old=e['antes'];new=e['depois']
 if e['motivo'].startswith('Nome: elenco'):
  parts=link_target.split(texts[f]);count=0
  for j in range(0,len(parts),2):
   parts[j],c=re.subn(r'(?<![\w-])'+re.escape(old)+r'(?![\w-])',new,parts[j]);count+=c
  if count!=e['vezes']:fail.append({'alteracao':n,'erro':'quantidade de nomes','encontrada':count})
  texts[f]=''.join(parts)
 else:
  if old not in texts[f]:fail.append({'alteracao':n,'erro':'trecho anterior ausente'})
  texts[f]=texts[f].replace(old,new,e.get('vezes',1))
for f,t in texts.items():
 if t!=(S/f).read_text():fail.append({'arquivo':f,'erro':'reprodução das alterações diverge'})
anchors={};count_links=0;local=collections.Counter();externos=0;absolute=[]
def ids(p):
 if p not in anchors:
  text=p.read_text()
  if p.suffix=='.md':text=markdown.markdown(text,extensions=['tables','toc'])
  anchors[p]={x['id'] for x in BeautifulSoup(text,'html.parser').find_all(id=True)}
 return anchors[p]
for f in texts:
 p=S/f
 soup=BeautifulSoup(markdown.markdown(p.read_text(),extensions=['tables','toc']),'html.parser')
 for tag in soup.find_all(['a','img']):
  target=tag.get('href') if tag.name=='a' else tag.get('src')
  if not target:continue
  count_links+=1;u=urlsplit(target)
  if u.scheme in ['http','https','mailto','data']:externos+=1;continue
  if u.scheme=='file' or u.path.startswith('/home/'):absolute.append({'arquivo':f,'destino':target})
  d=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
  if not d.is_file():fail.append({'arquivo':f,'erro':'link ausente','destino':target});continue
  if u.fragment and d.suffix in ['.md','.html'] and unquote(u.fragment) not in ids(d):
   fail.append({'arquivo':f,'erro':'âncora ausente','destino':target})
  try:d.relative_to(S.resolve());local['dentro_da_estrutura_revisada']+=1
  except ValueError:local['apoio_ou_fonte_fora_da_estrutura']+=1
for rel in absolute:fail.append({**rel,'erro':'caminho absoluto de computador no texto'})
struct=json.loads((R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json').read_text())
for f in struct['fontes']:
 p=R/f['fonte']
 if sha(p)!=base[f['fonte']]:fail.append({'arquivo':f['fonte'],'erro':'fonte original alterada'})
result={'registro':135,'manifesto_base_entradas':len(base),'entradas_conferidas':len(base),'arquivos_anteriores_alterados':changed,'arquivos_do_levantamento':len(texts),'arquivos_alterados_pelo_claude':len(changes),'registros_de_alteracao_reproduzidos':len(log),'originais_preservados':len(struct['fontes']),'links_e_imagens_conferidos':count_links,'links_externos_nao_reabertos':externos,'destinos_locais':dict(local),'caminhos_absolutos':absolute,'falhas':fail,'metodo':'Hash de cada entrada anterior; reprodução sequencial independente do histórico; links e âncoras conferidos no HTML gerado de cada fonte Markdown. Não substitui leitura semântica integral.'}
(A/'retomada/auditoria-independente.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='arquivos_anteriores_alterados'},ensure_ascii=False,indent=2),flush=True)
raise SystemExit(bool(fail))
