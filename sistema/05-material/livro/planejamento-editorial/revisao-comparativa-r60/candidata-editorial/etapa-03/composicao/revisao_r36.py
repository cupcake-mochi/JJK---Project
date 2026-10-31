import json
from pathlib import Path
B=Path(__file__).resolve().parent
def aplicar(textos):
    substituicoes=json.loads((B/'revisao-do-pente-fino/SUBSTITUICOES.json').read_text())
    registros=[]
    for c in substituicoes:
        k=c['bloco']; antes=textos[k]
        n=antes.count(c['antes'])
        if n!=1: raise ValueError(f"{c['id']}: esperada uma ocorrência; encontradas {n}")
        depois=antes.replace(c['antes'],c['depois'],1)
        textos[k]=depois
        registros.append({**c,'antes':antes,'depois':depois})
    (B/'revisao-do-pente-fino/ALTERACOES.json').write_text(json.dumps(registros,ensure_ascii=False,indent=2)+'\n')
    p=B/'revisao-de-regras/ALTERACOES-REGRAS.json'
    regras=json.loads(p.read_text()); regras=[x for x in regras if x['id']!='R36-PF011']
    regras.extend(x for x in registros if x['altera_regras'])
    p.write_text(json.dumps(regras,ensure_ascii=False,indent=2)+'\n')
    return registros
