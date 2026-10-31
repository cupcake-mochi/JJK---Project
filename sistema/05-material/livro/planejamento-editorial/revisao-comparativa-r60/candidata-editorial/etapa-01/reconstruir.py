from pathlib import Path
import subprocess,sys,json
H=Path(__file__).resolve().parent
for name in ['gerar_livro.py','gerar_noturno_r57.py']:
 subprocess.run([sys.executable,str(H/'composicao'/name)],cwd=H/'composicao',check=True)
subprocess.run([sys.executable,str(H/'conferir.py')],cwd=H,check=True)
r=json.loads((H/'revisao/VALIDACAO.json').read_text())
if r['resultado']!='aprovado':
 raise SystemExit('A composição requer revisão; confira revisao/VALIDACAO.json.')
