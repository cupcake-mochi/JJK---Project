"""R42: item 186, Promessa fora do limite de vagas de pactos."""
from pathlib import Path
import json
B = Path(__file__).resolve().parent

def aplicar(textos):
    rows = json.loads((B / 'ALTERACOES-R41-para-R42.json').read_text())
    for row in rows:
        assert textos[row['bloco']].strip() == row['antes'].strip(), row['bloco']
        textos[row['bloco']] = row['depois']
    return rows
