"""Conferência somente de leitura: executar na pasta extraída do Guia."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
manifest=json.loads((root/'04 - Planejamento/apoio-piloto/manifesto-entrega.json').read_text(encoding='utf-8-sig'))
errors=[]
for rel,expected in manifest.items():
 p=root/rel
 if not p.is_file():errors.append('Ausente: '+rel)
 elif hashlib.sha256(p.read_bytes()).hexdigest()!=expected:errors.append('Divergente: '+rel)
print(json.dumps({'arquivos_conferidos':len(manifest),'problemas':errors},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
