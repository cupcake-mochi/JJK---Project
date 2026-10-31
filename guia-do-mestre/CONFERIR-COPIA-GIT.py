"""Conferência somente de leitura; raiz descoberta pela localização deste script."""
from pathlib import Path
import hashlib,json
r=Path(__file__).resolve().parent
MODE='copia'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
if MODE=='copia':
 meta=json.loads((r/'SALVAMENTO.json').read_text());entries=meta['arquivos']
else:
 meta=json.loads((r/'04 - Planejamento/apoio-piloto/manifesto-entrega.json').read_text());entries={k:{'sha256':v} for k,v in meta.items()}
errors=[]
for i,(rel,info) in enumerate(entries.items(),1):
 p=r/rel
 if not p.is_file():errors.append('Ausente: '+rel)
 elif ('bytes' in info and p.stat().st_size!=info['bytes']) or sha(p)!=info['sha256']:errors.append('Divergente: '+rel)
 if i%1000==0:print('Conferidos',i,'de',len(entries),flush=True)
print(json.dumps({'arquivos_conferidos':len(entries),'problemas':errors},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
