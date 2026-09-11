#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AS SEIS MALDICOES PRONTAS — e elas estao na escada MORTA.

Achado em 10/09, respondendo "o que falta?" depois que o catalogo fechou.

A peca 26 §8 registra `As maldicoes prontas` como **FECHADAS na v0.214** — seis
bichos do nivel 2 ao 6, com ficcao de folclore japones, no `bloco-de-inimigo.docx`.
Elas existem, estao geradas e tem validador proprio.

O problema nao e que faltam. E que a escada mudou DEPOIS delas.

  a escada de quando elas nasceram : Ronda · Dupla · Alcateia · Calamidade
  a escada viva (04-fase-1)        : Capanga · Ameaca · Desastre · Catastrofe · Calamidade

Este script le as duas pontas nos documentos DONOS e mede a distancia:

  §1  quais categorias as seis usam        — o `dados.js` do gerador-inimigo
  §2  quais categorias estao vivas         — a `TABELA.md` desta pasta
  §3  quantas das seis sobrevivem          — o cruzamento
  §4  o que mais no `dados.js` e da escada morta

⚠ Este script NAO escreve nada no `Claude 2`. Ele so LE.
⚠ E o `Calamidade` e armadilha: o nome sobrevive nas duas escadas e o SIGNIFICADO
   nao — na morta ela era o topo de quatro, na viva e o topo de cinco. Nome igual
   nao e categoria igual, e o §3 trata isso a parte.

Nenhum numero mora aqui dentro: cada ancora e lida do documento dono, e o script
morre se o dono mudar.
"""
import os
import re
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')

DADOS = 'sistema/05-material/gerador-inimigo/dados.js'   # dono das seis
PECA26 = 'sistema/03-mecanica/26-bestiario.md'           # dono da escada morta
TABELA = '04-fase-1/TABELA.md'                           # dono da escada viva

MORTA = ('Ronda', 'Dupla', 'Alcateia')
VIVA = ('Capanga', 'Ameaça', 'Desastre', 'Catástrofe', 'Calamidade')
AMBIGUA = ('Calamidade',)   # o nome sobrevive, o significado nao

falhas = []


def morre(msg):
    print(f'\n  ✗ ANCORA PERDIDA: {msg}')
    falhas.append(msg)


def ler(base, rel):
    caminho = os.path.join(base, rel)
    if not os.path.exists(caminho):
        morre(f'nao existe: {rel}')
        return ''
    with open(caminho, encoding='utf-8') as f:
        return f.read()


def as_seis():
    """Le nome + faixa + categoria de cada uma das prontas, no dono."""
    txt = ler(REPO, DADOS)
    if not txt:
        return []
    achadas = re.findall(
        r"\{\s*nome:\s*'([^']+)'\s*,\s*faixa:\s*'([^']+)'\s*,\s*categoria:\s*'([^']+)'",
        txt)
    if not achadas:
        morre('o `dados.js` mudou de forma — nao achei `{ nome, faixa, categoria }`')
    return achadas


def escada_viva():
    txt = ler(BEST, TABELA)
    achadas = {c for c in VIVA if re.search(rf'\b{c}\b', txt)}
    if not achadas:
        morre('a `TABELA.md` nao cita categoria nenhuma da escada viva')
    return achadas


def main():
    print('=' * 74)
    print('AS SEIS MALDICOES PRONTAS — em que escada elas estao')
    print('=' * 74)

    seis = as_seis()
    viva = escada_viva()

    print(f'\n§1 · AS PRONTAS, no `{DADOS}`')
    if not seis:
        print('  (nenhuma lida)')
    for nome, faixa, cat in seis:
        estado = 'VIVA' if cat in viva and cat not in AMBIGUA else (
            'AMBIGUA' if cat in AMBIGUA else 'MORTA')
        marca = {'VIVA': '✓', 'AMBIGUA': '~', 'MORTA': '✗'}[estado]
        print(f'  {marca} {nome:<14} nv {faixa:<8} categoria `{cat}` — {estado}')

    print(f'\n§2 · A ESCADA VIVA, na `{TABELA}`')
    print('  ' + ' · '.join(sorted(viva)))

    print('\n§3 · O CRUZAMENTO')
    usadas = {c for _n, _f, c in seis}
    mortas = usadas & set(MORTA)
    ambiguas = usadas & set(AMBIGUA)
    vivas_ok = usadas - mortas - ambiguas

    n_mortas = sum(1 for _n, _f, c in seis if c in mortas)
    n_amb = sum(1 for _n, _f, c in seis if c in ambiguas)
    n_ok = sum(1 for _n, _f, c in seis if c in vivas_ok)

    print(f'  categorias usadas pelas prontas : {", ".join(sorted(usadas)) or "—"}')
    print(f'  delas, MORTAS                   : {", ".join(sorted(mortas)) or "nenhuma"}')
    print(f'  delas, ambiguas (nome sobrevive): {", ".join(sorted(ambiguas)) or "nenhuma"}')
    print(f'\n  fichas em categoria VIVA        : {n_ok} de {len(seis)}')
    print(f'  fichas em categoria AMBIGUA     : {n_amb} de {len(seis)}')
    print(f'  fichas em categoria MORTA       : {n_mortas} de {len(seis)}')

    if seis and n_ok == 0:
        print('\n  ⟹ NENHUMA das prontas esta numa categoria da escada viva.')
        print('    Elas nao estao erradas por dentro — o gerador computa tudo do `dados.js`.')
        print('    Elas estao penduradas numa escada que o projeto substituiu depois delas.')
        print('    ⚠ E o `bloco-de-inimigo.docx` e material de LIVRO, nao rascunho.')

    print('\n§4 · O QUE MAIS NO `dados.js` E DA ESCADA MORTA')
    txt = ler(REPO, DADOS)
    for cat in MORTA:
        n = len(re.findall(rf'\b{cat}\b', txt))
        if n:
            print(f'  `{cat}` aparece {n}× no arquivo inteiro')
    quatro = re.search(r'As quatro categorias da peca 26', txt)
    print(f'  o comentario "As quatro categorias da peca 26" — '
          f'{"AINDA LA" if quatro else "sumiu"}')
    if quatro:
        print('    ⚠ a escada viva tem CINCO. O comentario e da versao de antes.')

    print('\n' + '=' * 74)
    if falhas:
        print(f'✗ {len(falhas)} ancora(s) perdida(s). O documento dono mudou — releia antes de usar.')
        for f in falhas:
            print(f'   · {f}')
        sys.exit(1)
    print('✓ todas as ancoras de pe.')


if __name__ == '__main__':
    main()
