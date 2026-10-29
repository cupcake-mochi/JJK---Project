from revisar_guia94 import *
import markdown
from bs4 import BeautifulSoup
from collections import defaultdict,deque
entries=json.loads(LOG.read_text());rels=sorted({x['fonte'] for x in entries if x['fonte'].endswith('.md')});aliases={}
for rel in rels:
 p=A/'antes'/rel
 if not p.exists():continue
 before=p.read_text();after=(R/rel).read_text()
 oldheads=BeautifulSoup(markdown.markdown(before,extensions=['toc']),'html.parser').find_all(re.compile('^h[1-6]$'))[1:]
 newheads=BeautifulSoup(markdown.markdown(after,extensions=['toc']),'html.parser').find_all(re.compile('^h[1-6]$'))[1:]
 queues=defaultdict(deque)
 for h in newheads:queues[h.get_text()].append(h['id'])
 local={}
 for h in oldheads:
  changed=h.get_text()
  for e in entries:
   if e['fonte']!=rel:continue
   a,b=e['antes'],e['depois']
   if a.startswith('#') and b.startswith('#'):a=a.lstrip('# ').strip();b=b.lstrip('# ').strip()
   changed=changed.replace(a,b)
  if queues[changed]:
   cur=queues[changed].popleft()
   if cur!=h['id']:local[cur]=h['id']
  else:print('UNMATCHED',rel,h['id'],changed)
 if local:aliases[rel]=local
(R/'07 - Edicao de Leitura/titulos-estaveis.json').write_text(json.dumps(aliases,ensure_ascii=False,indent=2)+'\n')
# A repeated visible title must still have its own stable destination.
for rel in rels:
 text=(R/rel).read_text();pairs=[]
 for a,b in [('pareceres comparados','exemplos de avaliação'),('Pareceres comparados','Exemplos de avaliação'),('Tempo, materiais e retomada','Tempo e materiais para criar entidades')]:
  if '['+a+'](' in text:pairs.append(('['+a+'](', '['+b+']('))
 if pairs:edit(rel,pairs,'Referência com linguagem simples')
edit(source(87),[('conversar sobre o procedimento','explicar como fazer o pedido')])
