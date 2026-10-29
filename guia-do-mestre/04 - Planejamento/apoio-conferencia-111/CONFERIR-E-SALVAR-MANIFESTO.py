"""Conferir as entradas anteriores e acrescentar o lote 111 por união."""
from pathlib import Path
import hashlib,json
A=Path(__file__).resolve().parent
R=A.parents[1]
M=R/'04 - Planejamento/apoio-piloto/manifesto-entrega.json'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def main():
 assert (A/'conferencias.json').is_file(),'Concluir a conferência dirigida primeiro'
 old=json.loads((A/'antes/04 - Planejamento/apoio-piloto/manifesto-entrega.json').read_text())
 current=json.loads(M.read_text())
 config=json.loads((A/'arquivos-do-lote.json').read_text())
 allowed=set(config['controles']+config['extras'])
 assert set(old)<=set(current),'Não remover entradas antigas'
 changed=[];fail=[]
 for rel,expected in old.items():
  p=R/rel
  if not p.is_file():fail.append({'arquivo':rel,'problema':'ausente'});continue
  actual=sha(p)
  if actual!=expected:
   if rel in allowed:changed.append(rel)
   else:fail.append({'arquivo':rel,'problema':'alteração fora do lote'})
 assert not fail,fail
 assert set(config['controles'])<=set(changed),(config['controles'],changed)
 result={'registro':111,'entradas_anteriores':len(old),'entradas_anteriores_sem_alteracao':len(old)-len(changed),'arquivos_anteriores_atualizados':changed,'arquivos_ausentes_ou_alterados_fora_do_lote':fail,'metodo':'Conferência de todas as entradas anteriores; união restrita aos controles, arquivos de navegação e entrega 111.','limite':'Integridade documental; não aprendizagem ou equilíbrio.'}
 (A/'conferencia-do-manifesto.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 files=[R/rel for rel in config['controles']+config['extras']]+[R/'04 - Planejamento/111-conferencia-conjunta-das-consultas.md']
 files += [p for p in A.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
 updated=dict(current)
 for p in files:updated[str(p.relative_to(R))]=sha(p)
 assert set(old)<=set(updated)
 M.write_text(json.dumps(updated,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'entradas_anteriores':len(old),'entradas_finais':len(updated),'novas_entradas':len(set(updated)-set(old)),'arquivos_anteriores_atualizados':len(changed),'falhas':len(fail)},ensure_ascii=False))
if __name__=='__main__':main()
