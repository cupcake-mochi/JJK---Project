"""Confere, sem modificar arquivos, o inventário desta cópia Git."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
meta=json.loads((root/'SALVAMENTO.json').read_text())
errors=[]
for rel,info in meta['arquivos'].items():
 p=root/rel
 if not p.is_file():errors.append('Ausente: '+rel)
 elif len(p.read_bytes())!=info['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=info['sha256']:errors.append('Divergente: '+rel)
print(json.dumps({'arquivos_conferidos':len(meta['arquivos']),'problemas':errors},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
