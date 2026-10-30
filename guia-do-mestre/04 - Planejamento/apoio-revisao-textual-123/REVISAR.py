"""Criar as três cópias do lote B2-05 a partir dos originais e registrar cada alteração.

Os originais não são alterados. Cada troca precisa ocorrer exatamente uma vez no texto
corrente; o registro em alteracoes.json reproduz as cópias a partir das fontes.
"""
from pathlib import Path
import json

A = Path(__file__).resolve().parent
R = A.parents[1]
G = R / '06 - Redacao do Guia'
C = G / 'revisao-98/casos'
CFG = json.loads((A / 'arquivos-do-lote.json').read_text())
CASOS = {f['id']: f for f in CFG['casos']}

COPIA = 'Criar cópia e apontar as remissões para as cópias revistas vizinhas.'
CLARO = 'Clareza: frase direta, termo do Livro de Regras 1.0 ou ordem de leitura.'
PENTE = 'Pente fino da segunda leitura, na prova completa.'

import sys
sys.path.insert(0, str(A))
from edicoes import COPIA, CLARO, PENTE, LINKS, E
PASS2 = json.loads((A / 'pente-fino.json').read_text()) if (A / 'pente-fino.json').exists() else []
for x in PASS2:
    E.append((x['caso'], 2, x.get('tipo', 'pente_fino'), x.get('motivo', PENTE), x['antes'], x['depois']))


def main():
    log = []
    for cid, f in CASOS.items():
        src = (R / f['fonte_original']).read_text()
        text = src
        for a, b in LINKS[cid]:
            assert text.count(a) == 1, (cid, a)
            text = text.replace(a, b)
        log.append({'fonte': f['fonte_revisada'], 'passagem': 1, 'tipo': 'copia_e_remissoes', 'motivo': COPIA, 'antes': src, 'depois': text})
        for caso, passagem, tipo, motivo, a, b in E:
            if caso != cid:
                continue
            n = text.count(a)
            assert n == 1, (cid, n, a[:90])
            text = text.replace(a, b)
            log.append({'fonte': f['fonte_revisada'], 'passagem': passagem, 'tipo': tipo, 'motivo': motivo, 'antes': a, 'depois': b})
        (R / f['fonte_revisada']).write_text(text)
    (A / 'alteracoes.json').write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n')
    from collections import Counter
    print(len(log), dict(Counter((x['passagem'], x['tipo']) for x in log)))


if __name__ == '__main__':
    main()
