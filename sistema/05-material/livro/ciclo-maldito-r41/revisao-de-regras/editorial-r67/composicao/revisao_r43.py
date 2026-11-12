"""R43: Bloquear declarado antes da rolagem; Redirecionar usa só Defesa."""
from pathlib import Path
import json
B=Path(__file__).resolve().parent

def aplicar(textos):
    rows=json.loads((B/'ALTERACOES-R42-para-R43.json').read_text())
    for row in rows:
        assert textos[row['bloco']].strip()==row['antes'].strip(),row['bloco']
        textos[row['bloco']]=row['depois']
    return rows
