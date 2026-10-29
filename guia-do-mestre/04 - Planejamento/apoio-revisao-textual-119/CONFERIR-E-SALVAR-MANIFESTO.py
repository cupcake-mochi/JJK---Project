"""Preservar o manifesto anterior e acrescentar o lote textual por união."""
from pathlib import Path
import hashlib,json
A=Path(__file__).resolve().parent;R=A.parents[1]
M=R/'04 - Planejamento/apoio-piloto/manifesto-entrega.json'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def main():
 conf=json.loads((A/'conferencias.json').read_text());visual=json.loads((A/'revisao-final.json').read_text());meta=json.loads((A/'amostra.json').read_text())
 assert conf['pdf_sha256']==visual['pdf_sha256']==meta['pdf_sha256']==sha(R/meta['pdf'])
 assert len(visual['paginas'])==len(meta['paginas']) and all(p['inspecionada'] for p in visual['paginas'])
 old=json.loads((A/'antes/04 - Planejamento/apoio-piloto/manifesto-entrega.json').read_text());current=json.loads(M.read_text());config=json.loads((A/'arquivos-do-lote.json').read_text())
 required=set(config['controles']+config['fontes_revisadas']);allowed=required|set(config['extras']);assert set(old)<=set(current)
 assert len(old)==2232,len(old)
 for page in visual['paginas']:
  assert sha(R/page['imagem'])==page['imagem_sha256'],page['imagem']
 changed=[];fail=[]
 for rel,expected in old.items():
  p=R/rel
  if not p.is_file():fail.append({'arquivo':rel,'problema':'ausente'});continue
  if sha(p)!=expected:
   if rel in allowed:changed.append(rel)
   else:fail.append({'arquivo':rel,'problema':'alteração fora do lote'})
 assert not fail,fail
 assert required<=set(changed)<=allowed,(changed,allowed)
 result={'registro':119,'entradas_anteriores':len(old),'entradas_anteriores_sem_alteracao':len(old)-len(changed),'arquivos_anteriores_atualizados':changed,'arquivos_ausentes_ou_alterados_fora_do_lote':fail,'metodo':'Todas as entradas anteriores conferidas; atualização por união restrita aos dez controles e arquivos novos do lote 119, incluindo cinco cópias revistas.','limite':'Integridade documental; não aprendizagem ou equilíbrio.'}
 (A/'conferencia-do-manifesto.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 files=[R/rel for rel in allowed]+[R/rel for rel in config['fontes_novas']]+[R/'04 - Planejamento/119-revisao-de-energia-habilidades-e-chefes.md']+[p for p in A.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
 updated=dict(current)
 for p in files:updated[str(p.relative_to(R))]=sha(p)
 assert set(old)<=set(updated)
 M.write_text(json.dumps(updated,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'entradas_anteriores':len(old),'entradas_finais':len(updated),'novas_entradas':len(set(updated)-set(old)),'arquivos_atualizados':len(changed),'falhas':len(fail)},ensure_ascii=False))
if __name__=='__main__':main()
