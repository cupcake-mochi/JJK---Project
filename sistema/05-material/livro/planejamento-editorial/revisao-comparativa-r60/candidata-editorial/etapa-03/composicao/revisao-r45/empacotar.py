from pathlib import Path
import json,hashlib,zipfile,shutil,tempfile
B=Path(__file__).resolve().parents[1]
DEST=B.parent/'Ciclo-Maldito-R45-Origens.zip'
assets={'fontes-editoriais','fontes-tipograficas','referencias','capa','componentes'}
text_ext={'.py','.json','.md','.txt','.csv','.toml','.yaml','.yml'}
selected=[]
for p in sorted(B.rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts: continue
 rel=p.relative_to(B)
 if rel.name=='MANIFESTO-R45.json':continue
 keep=(rel.parts[0] in assets or p.suffix.lower() in text_ext or str(rel)=='output/pdf/Ciclo-Maldito-R45.pdf' or str(rel).startswith('revisao-r45/prova/') or rel.name in {'CONFERENCIA-R45.log','GERACAO-R45.log'})
 if keep: selected.append(p)
manifest={'edicao':'R45','data':'2026-10-13','pdf_paginas':388,'metodo':'SHA-256 dos bytes; manifesto não inclui a si próprio. PDFs/provas antigas não são necessários à geração e foram omitidos.','arquivos':{str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in selected}}
(B/'MANIFESTO-R45.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n');selected.append(B/'MANIFESTO-R45.json')
with zipfile.ZipFile(DEST,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in selected:z.write(p,str(Path(B.name)/p.relative_to(B)))
with zipfile.ZipFile(DEST) as z:
 bad=z.testzip(); assert bad is None,bad
sha=hashlib.sha256(DEST.read_bytes()).hexdigest()
DEST.with_suffix('.zip.sha256').write_text(f'{sha}  {DEST.name}\n')
print(json.dumps({'zip':str(DEST),'arquivos':len(selected),'MB':round(DEST.stat().st_size/1e6,1),'sha256':sha},ensure_ascii=False))
