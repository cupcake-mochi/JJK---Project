from pathlib import Path
import json,hashlib,sys
import pymupdf
R=Path('/media/mizuki/HD Externo II/Claude/Pesquisa de Campo - Mestragem');A=R/'04 - Planejamento/apoio-revisao-integral-94';D=R/'08 - Diagramacao do Guia';P=D/'output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf'
T=A/'segunda-leitura';T.mkdir(exist_ok=True)
if not (T/'manifesto.json').exists():
 doc=pymupdf.open(P);pages=[]
 for i,p in enumerate(doc,1):
  text=p.get_text();file=f'p{i:03}.txt';(T/file).write_text(text);pages.append({'pagina':i,'arquivo':file,'sha256':hashlib.sha256(text.encode()).hexdigest()})
 (T/'manifesto.json').write_text(json.dumps({'pdf_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'paginas':pages,'lidas':[],'correcoes':[]},ensure_ascii=False,indent=2)+'\n')
for n in range(int(sys.argv[1]),int(sys.argv[2])+1):print(f'\n===== PÁGINA {n} =====\n'+(T/f'p{n:03}.txt').read_text())
