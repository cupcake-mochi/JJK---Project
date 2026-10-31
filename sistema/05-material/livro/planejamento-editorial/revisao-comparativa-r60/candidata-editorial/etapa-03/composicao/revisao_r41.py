"""R41: acertos do autor no Evocador, Represália e Sangue Frio."""
from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=B/'revisao-r41'
NAMES={'Intervenções da principal':'Intervenções da Invocação Principal','Proteção do conjunto':'Intervenções do Conjunto'}
def rename(x):
 if isinstance(x,str):
  for a,b in NAMES.items():x=x.replace(a,b)
  return x
 if isinstance(x,list):return [rename(v) for v in x]
 if isinstance(x,dict):return {rename(k):rename(v) for k,v in x.items()}
 return x
def aplicar(textos,meta):
 rows=json.loads((R/'ALTERACOES-TEXTO.json').read_text())
 for row in rows:
  assert textos[row['bloco']].strip()==row['antes'].strip(),row['bloco']
  textos[row['bloco']]=row['depois']
 updated=rename(meta);meta.clear();meta.update(updated)
 (B/'revisao-de-estrutura/HIERARQUIA.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
 c=rename(json.loads((B/'revisao-r40/CLASSIFICACAO.json').read_text()))
 (R/'CLASSIFICACAO.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 return rows
