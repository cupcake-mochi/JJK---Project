from pathlib import Path
import json,hashlib
from pypdf import PdfReader,PdfWriter
B=Path(__file__).resolve().parent;P=B.parents[1];units=json.loads((B/'UNIDADES.json').read_text());w=PdfWriter();mapping=[]
for u in units:
 b=P/u['pasta'];f=b/'output/pdf'/u['pdf'];r=PdfReader(f);meta=json.loads((b/'ESTRUTURA.json').read_text());start=len(w.pages)
 assert len(r.pages)==len(meta['ordem'])
 w.append(r,import_outline=False);parent=w.add_outline_item(u['titulo'],start,is_open=False)
 for k in meta['ordem']:w.add_outline_item(meta['titulos'][k],start+meta['paginas'][k]-1,parent=parent)
 w.set_page_label(start,len(w.pages)-1,style='/D',prefix=u['titulo']+' - ',start=1)
 mapping.append({**u,'inicio':start+1,'paginas':len(r.pages),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
w.add_metadata({'/Title':'Projeto M | Carga, proteção e compras | Revisão 5','/Author':'Projeto M','/Subject':'Candidata sobre base v0.331; páginas locais por bloco'})
w.page_mode='/UseOutlines';out=B/'output/pdf/Projeto-M-Carga-Protecao-e-Compras-Revisao-05.pdf';out.parent.mkdir(parents=True,exist_ok=True);w.write(out)
r=PdfReader(out);assert len(r.pages)==17
ids={p.indirect_reference.idnum:i for i,p in enumerate(r.pages)};checks=[]
for u in mapping:
 source=PdfReader(P/u['pasta']/'output/pdf'/u['pdf']);sids={p.indirect_reference.idnum:i for i,p in enumerate(source.pages)};start=u['inicio']-1
 def targets(page,idmap):
  return sorted(idmap[a.get_object()['/Dest'][0].idnum] for a in page.get('/Annots',[]) if a.get_object().get('/Subtype')=='/Link' and '/Dest' in a.get_object())
 for n,p in enumerate(source.pages):
  q=r.pages[start+n];checks.append(p.extract_text()==q.extract_text());checks.append([v+start for v in targets(p,sids)]==targets(q,ids))
assert all(checks)
assert len([x for x in r.outline if not isinstance(x,list)])==4
(B/'MAPA-PDF.json').write_text(json.dumps({'ok':True,'paginas':17,'verificacoes_texto_links':len(checks),'unidades':mapping,'sha256_pdf':hashlib.sha256(out.read_bytes()).hexdigest()},ensure_ascii=False,indent=2)+'\n')
print('17 páginas; textos e destinos de links conferidos nas cópias reabertas.')
