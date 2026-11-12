"""R47: item 194, anúncio de Ataque sem Prenúncio após a defesa escolhida."""
from pathlib import Path
import json
B=Path(__file__).resolve().parent
def aplicar(textos):
 rows=json.loads((B/'ALTERACOES-R46-para-R47.json').read_text())
 for row in rows:
  assert textos[row['bloco']]==row['antes'],row['bloco']
  textos[row['bloco']]=row['depois']
 return rows
