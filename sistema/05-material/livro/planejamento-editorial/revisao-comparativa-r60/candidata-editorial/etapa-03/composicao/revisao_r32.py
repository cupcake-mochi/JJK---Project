import json
from pathlib import Path
B=Path(__file__).resolve().parent
def aplicar(textos):
    changes=json.loads((B/'revisao-de-compreensao/SUBSTITUICOES.json').read_text())
    for c in changes:
        k=c['bloco'];before=c['antes'];after=c['depois']
        n=textos[k].count(before)
        if n!=1:raise ValueError(f"{c['id']}: esperada uma ocorrência, encontradas {n}: {k}")
        textos[k]=textos[k].replace(before,after,1)
    return changes
