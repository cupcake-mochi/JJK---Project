"""Retificação de Recomposição pelo autor, em 14/10/2026."""
from pathlib import Path
import json
B=Path(__file__).resolve().parent

def aplicar(textos):
    rows=json.loads((B/'ALTERACOES-R50-para-R51.json').read_text())
    for row in rows:
        assert textos[row['bloco']]==row['antes'],row['bloco']
        textos[row['bloco']]=row['depois']
    return rows
