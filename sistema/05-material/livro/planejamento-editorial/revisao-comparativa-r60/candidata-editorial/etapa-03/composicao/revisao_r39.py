from pathlib import Path
import json

B = Path(__file__).resolve().parent

def aplicar(textos):
    rows = json.loads((B / 'revisao-r39/ALTERACOES-TEXTO.json').read_text())
    for row in rows:
        assert textos[row['bloco']].strip() == row['antes'], row['bloco']
        textos[row['bloco']] = textos[row['bloco']].replace(row['antes'], row['depois'], 1)
    return rows
