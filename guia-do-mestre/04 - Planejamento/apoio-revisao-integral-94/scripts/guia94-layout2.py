from pathlib import Path
import shutil
r=Path('/media/mizuki/HD Externo II/Claude/Pesquisa de Campo - Mestragem')
p=r/'08 - Diagramacao do Guia/GERAR-PDF.py'
a=r/'04 - Planejamento/apoio-revisao-integral-94'
shutil.copy2(p,a/'gerador-antes-layout-final.py')
s=p.read_text()
s=s.replace(' last:bool=True\n',' last:bool=True\n keep_next:bool=False\n')
s=s.replace("out.append(para(prefix+''.join(inline(c) for c in children),source=k))", "out.append(para(prefix+''.join(inline(c) for c in children),source=k))\n    if k=='s032' and 'Alcance da decisão:' in li.get_text():out[-1].keep_next=True")
s=s.replace("if item.kind in ['h1','h2','h3'] and len(q)>1:","if (item.kind in ['h1','h2','h3'] or item.keep_next) and len(q)>1:")
s=s.replace("shortlead=(pending and pending[-1].kind", "shortlead=(item.kind=='image' and item.source=='s087') or (pending and pending[-1].kind")
# Optimize a larger tail before balancing it. Recompose without artificial bottom
# margin and retain ordinary paragraph splitting; no font or spacing reduction.
a0=s.index(' saved=list(pages[-2:]);prefix=list(pages[:-2]);raw=')
a1=s.index(' TAIL_WHOLE=True',a0)
old=s[a0:a1]
new=''' original_pages=list(pages);original_y=y
 def reunite(raw):
  seq=[];i=0
  while i<len(raw):
   a=raw[i];j=i+1
   if a.original is not None and a.first:
    while j<len(raw) and raw[j].original is a.original:j+=1
    if raw[j-1].last:a=replace(a,f=a.original,original=None,first=True,last=True)
    else:j=i+1
   seq.append(a);i=j
  return seq
 for count in [4,3,2]:
  if len(original_pages)-start_index<count:continue
  prefix=list(original_pages[:-count]);seq=reunite([v.item for pp in original_pages[-count:] for v in pp.items])
  pages=list(prefix);BOTTOM=base;TAIL_WHOLE=False;newpage(ch,title)
  try:compose_items(seq,ch,title)
  except ValueError:continue
  if len(pages)<len(original_pages):return
 pages=original_pages;current=pages[-1];y=original_y
 saved=list(pages[-2:]);prefix=list(pages[:-2])
 seq=reunite([v.item for pp in saved for v in pp.items])
'''
s=s[:a0]+new+s[a1:]
p.write_text(s)
shutil.copy2(Path('/tmp/guia94-layout2.py'),a/'scripts/guia94-layout2.py')
