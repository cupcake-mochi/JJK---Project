"""Revisão editorial rastreável; fontes aprovadas permanecem intactas."""
import json
from pathlib import Path
B=Path(__file__).resolve().parent

def aplicar(textos):
    changes=json.loads((B/'revisao-textual/ALTERACOES.json').read_text())
    for c in changes:
        k=c['bloco'];before=c['antes'];after=c['depois']
        if k not in textos:raise ValueError('Bloco ausente: '+k)
        n=textos[k].count(before)
        if n!=1:raise ValueError(f"{c['id']}: esperada uma ocorrência, encontradas {n}")
        textos[k]=textos[k].replace(before,after,1)
    return changes
