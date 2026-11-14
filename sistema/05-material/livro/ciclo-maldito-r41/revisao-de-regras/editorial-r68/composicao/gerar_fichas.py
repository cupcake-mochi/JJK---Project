from pathlib import Path
import json,hashlib
from pypdf import PdfReader
B=Path(__file__).resolve().parent
builder=(B/'gerar_livro.py').read_text().split('# Apresentação e sumário reunidos em uma única página, com duas colunas.')[0]
ns={'__file__':str(B/'gerar_livro.py'),'__name__':'modelos'}
exec(compile(builder,str(B/'gerar_livro.py'),'exec'),ns)
ns['enriched'].update(ns['g']['supplement_enriched'])
ns['BOTTOM']=19*ns['mm'];ns['TOP']=ns['H']-19*ns['mm'];ns['CAP']=ns['TOP']-ns['BOTTOM']
ch={'numero':0,'titulo':'Caderno de fichas','key':'caderno','parte':1}
for block in ns['g']['supplement_blocks']:
 parts=ns['parse'](block);before=len(ns['pages'])
 if ns['Unit'](parts).measure(ns['AW'])[0]<=ns['CAP']:
  page=ns['newpage'](ch,block.title,'form')
  ns['put'](page,ns['Unit'](parts),ns['M'],ns['TOP'],ns['AW'],'uma-coluna',info=block.key)
 else:ns['add_atoms'](ch,ns['atoms_for'](parts,block.title))
 for page in ns['pages'][before:]:page['kind']='form'
pdf=B/'output/pdf/Ciclo-Maldito-Caderno-de-Fichas-R27.pdf'
c=ns['Canvas'](str(pdf),pagesize=(ns['W'],ns['H']),pageCompression=1)
c.setTitle('Ciclo Maldito | Caderno de fichas');c.setAuthor('Mizuki_sama');c.showOutline()
for page in ns['pages']:
 c.setFillColor(ns['white']);c.rect(0,0,ns['W'],ns['H'],fill=1,stroke=0)
 c.setFont('Head',9);c.setFillColor(ns['ACC']);c.drawString(ns['M'],ns['H']-12*ns['mm'],'CICLO MALDITO')
 c.setFillColor(ns['MUTED']);c.drawRightString(ns['W']-ns['M'],ns['H']-12*ns['mm'],'CADERNO DE FICHAS')
 c.setStrokeColor(ns['RULE']);c.setLineWidth(.5);c.line(ns['M'],ns['H']-15*ns['mm'],ns['W']-ns['M'],ns['H']-15*ns['mm'])
 for key,(pn,x,y) in ns['positions'].items():
  if pn==page['numero']:
   c.bookmarkHorizontalAbsolute(key,y,x)
   block=ns['g']['supplement_blocks'];title=next((b.title for b in block if b.key==key),None)
   if title:c.addOutlineEntry(title,key,0,True)
 for part,f,x,y,w,h,mode in page['draws']:f.drawOn(c,x,y)
 c.setFont('Head',9);c.setFillColor(ns['MUTED']);c.drawString(ns['M'],14*ns['mm'],'CICLO MALDITO / CADERNO DE FICHAS')
 c.setFillColor(ns['ACC']);c.drawRightString(ns['W']-ns['M'],14*ns['mm'],str(page['numero']));c.showPage()
c.save()
manifest={'pdf':str(pdf.relative_to(B)),'sha256_pdf':hashlib.sha256(pdf.read_bytes()).hexdigest(),'paginas':len(ns['pages']),'eventos':ns['events'],'ancoras':{k:{'pagina':v[0]} for k,v in ns['positions'].items()},'blocos':list(ns['g']['supplement_enriched'])}
(B/'evidencias/FICHAS-SEPARADAS.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(B/'FICHAS-COMPLETAS.md').write_text('\n\n'.join(ns['g']['supplement_enriched'].values())+'\n')
print(pdf,len(ns['pages']),'páginas')
