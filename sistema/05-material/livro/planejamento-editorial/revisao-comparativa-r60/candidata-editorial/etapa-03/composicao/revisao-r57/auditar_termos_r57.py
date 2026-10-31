from pathlib import Path
import re,json,unicodedata
B=Path('/home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r56')
d=json.loads((B/'revisao-r56/BLOCOS-R56.json').read_text());book=(B/'LIVRO-COMPLETO.md').read_text(); order=[k for k in re.findall(r'<a id="([^"]+)"></a>',book) if k in d];order=list(dict.fromkeys(order));plain=lambda s:re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',s).replace('*','')
full='\n\n'.join(d[k] for k in order)
heads=[]
for k in order:
 for m in re.finditer(r'^#{1,6} (.+)$',d[k],re.M):
  h=plain(m[1]);h=re.sub(r'^Nível \d+\s*[-–:]\s*','',h)
  if 4<=len(h)<=42 and not re.search(r'Exemplo|Como |Quando |Escolh|Confer|Progress|Caracter|Nível| e |:| / |\d',h):heads.append((h,k))
rows=[]
for h,k in heads:
 pat=re.compile(r'(?<!\w)'+re.escape(h)+r'(?!\w)',re.I)
 before=order[:order.index(k)]
 for bk in before:
  paragraphs=d[bk].split('\n\n')
  found=next((p for p in paragraphs if pat.search(plain(p)) and not p.startswith(('#','|'))),None)
  if found:
   rows.append({'termo':h,'primeiro':bk,'definicao':k,'contexto':found});break
Path('/tmp/r57-candidatos.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('blocks',len(order),'headings',len(heads),'forward candidates',len(rows))
for i,r in enumerate(rows): print(i,r['termo'],r['primeiro'],'=>',r['definicao'])
