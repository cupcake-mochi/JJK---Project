from pathlib import Path
import json,hashlib
from pypdf import PdfReader,PdfWriter
B=Path(__file__).resolve().parent;P=B.parents[1]
units=json.loads((B/'UNIDADES.json').read_text());order=[3,2,0,1,4]
w=PdfWriter();mapping=[];readers=[]
for idx in order:
 u=units[idx];b=P/u['pasta'];c=json.loads((b/'CONFERENCIA.json').read_text());assert c['ok']
 f=b/'output/pdf'/u['pdf'];r=PdfReader(f);readers.append(PdfReader(f));start=len(w.pages);w.append(r,import_outline=False)
 label=u['titulo'].split(',')[0];parent=w.add_outline_item(label,start,is_open=False)
 meta=json.loads((b/'ESTRUTURA.json').read_text())
 for key in meta['ordem']:w.add_outline_item(meta['titulos'][key],start+meta['paginas'][key]-1,parent=parent)
 w.set_page_label(start,start+len(r.pages)-1,style='/D',prefix=label+' - ',start=1)
 mapping.append({'bloco':label,'pasta':u['pasta'],'pdf':u['pdf'],'inicio':start+1,'paginas':len(r.pages),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
w.add_metadata({'/Title':'Projeto - M | Carga e Equipamento | Revisão 2','/Author':'Projeto - M','/Subject':'Caderno de propostas; paginação local por bloco; base v0.331 preservada'})
w.page_mode='/UseOutlines';out=B/'output/pdf/Projeto-M-Carga-e-Equipamento-Revisao-02.pdf';w.write(out)
r=PdfReader(out);assert len(r.pages)==23
checks=[];offset=0
finalids={p.indirect_reference.idnum:i for i,p in enumerate(r.pages)}
for src in readers:
 ids={p.indirect_reference.idnum:i for i,p in enumerate(src.pages)}
 for i,p in enumerate(src.pages):
  q=r.pages[offset+i];assert p.extract_text()==q.extract_text()
  def targets(page,lookup):
   out=[]
   for ar in page.get('/Annots',[]):
    a=ar.get_object()
    if a.get('/Subtype')=='/Link':
     dest=a.get('/Dest');out.append(lookup.get(dest[0].idnum) if dest else None)
   return out
  old=targets(p,ids);new=targets(q,finalids);assert new==[offset+x for x in old]
  checks.append({'pagina':offset+i+1,'texto_identico':True,'destinos_validos':True})
 offset+=len(src.pages)
assert len([x for x in r.outline if not isinstance(x,list)])==5
assert all(x.get('/Count',0)<0 for x in r.outline if not isinstance(x,list))
(B/'evidencias/caderno-conferido.json').write_text(json.dumps({'ok':True,'sha256_pdf':hashlib.sha256(out.read_bytes()).hexdigest(),'paginas':23,'grupos_recolhidos':5,'blocos':mapping,'checks':checks},ensure_ascii=False,indent=2)+'\n')
print('Caderno: 23 páginas, 5 grupos recolhidos, textos e destinos conferidos.')
