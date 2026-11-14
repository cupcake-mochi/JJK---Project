"""R46: retirar indicação de continuação do título, preservando a regra."""
from pathlib import Path
import json
B=Path(__file__).resolve().parent
def aplicar(textos):
 rows=json.loads((B/'ALTERACOES-R45-para-R46.json').read_text())
 for row in rows:
  assert textos[row['bloco']]==row['antes'],row['bloco']
  textos[row['bloco']]=row['depois']
 return rows
