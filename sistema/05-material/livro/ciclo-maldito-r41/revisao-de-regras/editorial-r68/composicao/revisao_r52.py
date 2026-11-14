"""Retificação das permissões de personalização das Origens, em 15/10/2026."""
from pathlib import Path
import json
B=Path(__file__).resolve().parent

def aplicar(textos):
    rows=json.loads((B/'ALTERACOES-R51-para-R52.json').read_text())
    for row in rows:
        assert textos[row['bloco']]==row['antes'],row['bloco']
        textos[row['bloco']]=row['depois']
    return rows
