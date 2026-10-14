"""Integração de Morrendo e revisão de compreensão, sobre a R49 preservada."""
from pathlib import Path
import json

B = Path(__file__).resolve().parent

def aplicar(textos):
    rows = json.loads((B / 'ALTERACOES-R49-para-R50.json').read_text())
    for row in rows:
        assert textos[row['bloco']] == row['antes'], row['bloco']
        textos[row['bloco']] = row['depois']
    # R45 recompõe esta classificação a cada carga. Acrescentar aqui, depois dela,
    # torna o estilo do novo subtópico persistente em qualquer regeneração.
    path = B / 'revisao-r45/CLASSIFICACAO.json'
    classification = json.loads(path.read_text())
    classification = [r for r in classification if (r['bloco'], r['titulo']) != ('dano--socorro', 'Resgates expressos')]
    row = dict(next(r for r in classification if (r['bloco'], r['titulo']) == ('dano--socorro', 'Estabilizar')))
    row.update(titulo='Resgates expressos', motivo='R50: novo subtópico de Socorro, com o tratamento B aprovado.')
    row.pop('pagina_r34', None)
    classification.append(row)
    path.write_text(json.dumps(classification, ensure_ascii=False, indent=2) + '\n')
    return rows
