from pathlib import Path
import json
B=Path(__file__).resolve().parent
def aplicar(textos,meta):
 rows=json.loads((B/'revisao-r38/ALTERACOES-TEXTO.json').read_text())
 for row in rows:
  
  if textos[row['bloco']].strip()!=row['antes']:
   import difflib
   print(''.join(difflib.unified_diff(row['antes'].splitlines(True),textos[row['bloco']].strip().splitlines(True))))
   raise AssertionError(row['bloco'])
  # Preserve the existing surrounding whitespace exactly.
  textos[row['bloco']]=textos[row['bloco']].replace(row['antes'],row['depois'],1)
 cfg=meta['rotas--rota-combate']
 template=next(x for x in cfg['titulos'] if x['titulo']=='Antecipar')
 pos=next(i for i,x in enumerate(cfg['titulos']) if x['titulo']=='Campo')
 cfg['titulos'][pos:pos]=[{**template,'titulo':name} for name in ['Represália','Sangue Frio']]
 return rows
