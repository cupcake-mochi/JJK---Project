# -*- coding: utf-8 -*-
"""Gera o capítulo 8 — as seis maldições prontas, no molde de bloco do 5e.

v0.282, a grade da fase 2. Nenhum número é digitado à mão, e nenhum é calculado aqui: a conta
inteira mora no `conta.js` do gerador de inimigo, que imprime as seis prontas com `node conta.js
--json`. Este script só FORMATA o que o conta.js calculou — até a v0.281 ele portava a conta do
make.js para Python e conferia as duas, e duas contas do mesmo número são dois donos.

O que continua conferido aqui:
  · toda condição que o texto põe ("fica `X`") é uma das treze da peça 19;
  · a ação que monta técnica tem ao menos o piso da `Classe 1` do Fundamento em pontos.

⚠ O script só LÊ o `Claude 2`. Ele nunca escreve lá.
"""
import json
import math
import os
import re
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
LIVRO = os.path.dirname(BASE)
BEST = os.path.dirname(LIVRO)
REPO = os.environ.get('JJK_REPO', os.path.dirname(BEST))
GER = os.path.join(REPO, 'sistema/05-material/gerador-inimigo')
FUND = os.path.join(REPO, 'sistema/05-material/livro/manual/40-fundamento.md')
COND = os.path.join(REPO, 'sistema/03-mecanica/19-dano-e-condicoes.md')
CAP = os.path.join(LIVRO, 'capitulos', '80-seis-maldicoes.md')
MARCA, FIM = '<!-- FICHAS -->', '<!-- FIM FICHAS -->'
FEM = {'Minúsculo': 'Minúscula', 'Pequeno': 'Pequena', 'Médio': 'Média',
       'Grande': 'Grande', 'Imenso': 'Imensa', 'Colossal': 'Colossal'}
NUM = {1: 'um', 2: 'dois', 3: 'três', 4: 'quatro'}
ATRIB = ('Força', 'Destreza', 'Constituição', 'Inteligência', 'Essência')
TR_TODOS = ('Físico', 'Vigor', 'Intelecto', 'Espírito')
DESLOC = '9 m'


def morre(m):
    sys.exit('✗ ÂNCORA PERDIDA: ' + m)


def ler(p):
    if not os.path.exists(p):
        morre('não existe: %s' % p)
    return open(p, encoding='utf-8').read()


def media(e):
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e.strip())
    return int(m.group(1)) * (1 + int(m.group(2))) / 2 + int(m.group(3) or 0) if m else float(e)


def rot_nv(a, b):
    return 'nível %d' % a if a == b else 'nível %d a %d' % (a, b)


# ── as seis, calculadas pelo conta.js do gerador (a conta pura, sem o pacote `docx`)
r = subprocess.run(['node', 'conta.js', '--json'], cwd=GER, capture_output=True, text=True)
if r.returncode != 0:
    morre('o `node conta.js --json` falhou: %s' % (r.stderr.strip().splitlines() or ['sem saída'])[-1][:160])
SEIS = json.loads(r.stdout)
if len(SEIS) != 6:
    morre('o conta.js devolveu %d prontas, e o capítulo é de seis' % len(SEIS))

# ── as duas travas: condição do sistema, e o piso da técnica
CONDS = set(re.findall(r'^\| \*\*`([^`]+)`\*\* \| `(?:Leve|Média|Pesada)`', ler(COND), re.M))
if len(CONDS) < 13:
    morre('a lista de condições da peça 19 mudou de forma (li %d)' % len(CONDS))
m = re.search(r'### Classe 1 · (\d+) pontos', ler(FUND))
if not m:
    morre('a Classe 1 mudou de forma no Fundamento')
PISO_TEC = int(m.group(1))

out = []
for j in SEIS:
    nome = j['nome']
    textos = [t['texto'] for t in j['tracos'] + j['acoes'] + j['intervencoes']] + [j['acoes_multiplas'] or '']
    for t in textos:
        for c in re.findall(r'fica `([^`]+)`', t):
            if c not in CONDS:
                morre('`%s` usa a condição `%s`, que o sistema não tem' % (nome, c))
    if any('de dano de Fogo' in t and 'conjuração' in t for t in textos) and j['pontos'] < PISO_TEC:
        morre('`%s` monta técnica com %.1f pontos, abaixo do piso da Classe 1' % (nome, j['pontos']))
    lo, hi = j['lo'], j['hi']
    at = j['atributos']
    i_atk = j['iAtk']
    treinados = [t for t in TR_TODOS if t in j['trs']]
    if len(treinados) != 2:
        morre('`%s` não tem dois Testes de Resistência treinados' % nome)

    def celula(i):
        sobe = ['`%d` do nível %d' % (at[k][i], lo + k) for k in range(1, len(at)) if at[k][i] != at[k - 1][i]]
        marca = [x for x, ok in (('Iniciativa', i == 1), ('acerto e CD', i == i_atk)) if ok]
        return '**%s** `%d`%s%s' % (ATRIB[i], at[0][i], ' (%s)' % '; '.join(sobe) if sobe else '',
                                    ' *(%s)*' % ', '.join(marca) if marca else '')
    atr = ' · '.join(celula(i) for i in range(5))
    trs = ' · '.join('**%s** %s' % (t, 'treinado' if t in treinados else '—') for t in TR_TODOS)
    corpo = (' · %s corpos' % NUM[j['corpos']]) if j['corpos'] > 1 else ''
    pap = (' · %s' % j['papel']) if j['papel'] else ''
    mov = ''.join(' · **%s** `%s`' % (mv, DESLOC) for mv in j['movimentos'])
    out += ['## %s' % nome, '', '*%s*' % j['linha'], '', j['notas'], '',
            '> ### %s' % nome, '>',
            '> *Maldição %s · **%s ×%d**%s%s · nível %d a %d*' % (FEM[j['tamanho']], j['categoria'], j['n'], pap, corpo, lo, hi), '>']
    for a, b, v, prot in j['seg']:
        pre = '*%s* · ' % rot_nv(a, b) if len(j['seg']) > 1 else ''
        out += ['> %s**Defesa** `%d` · **Acerto** `+%d` · **CD** `%d` · **Refino** `%d` *(proteção `+%d`)*'
                % (pre, v[0], v[1], v[2], v[3], prot), '>']
    out += ['> **Vida** `%d` · **Integridade** `%d` · **Deslocamento** `%s`%s' % (j['vida'], j['vida'] // 2, DESLOC, mov), '>',
            '> %s' % atr, '>', '> %s' % trs, '>',
            '> **Resistências** — · **Imunidades** — · **Vulnerabilidades** — · **Perícias** —', '>',
            '> **Traços**', '>']
    for t in j['tracos']:
        out += ['> **%s.** %s' % (t['nome'], t['texto']), '>']
    out += ['> **Ações**', '>']
    if j['acoes_multiplas']:
        out += ['> **Ações Múltiplas.** %s' % j['acoes_multiplas'], '>']
    for a in j['acoes']:
        out += ['> **%s.** %s' % (a['nome'], a['texto']), '>']
    if j['intervencoes']:
        out += ['> **Intervenções**', '>',
                '> %s por luta, cada uma usada uma vez. Sai no máximo uma por rodada, logo depois '
                'do turno de outra criatura.' % NUM[len(j['intervencoes'])].capitalize(), '>']
        for k, iv in enumerate(j['intervencoes'], 1):
            out += ['> **%d. %s.** %s' % (k, iv['nome'], iv['texto']), '>']
    out.pop()
    out.append('')

cap = ler(CAP)
if MARCA not in cap or FIM not in cap:
    morre('as marcas das fichas sumiram do capítulo 8')
i, k = cap.index(MARCA), cap.index(FIM)
_novo = cap[:i] + MARCA + '\n\n' + '\n'.join(out) + '\n' + cap[k:]
if '--conferir' in sys.argv:
    sys.exit(0 if _novo == cap else '✗ DESATUALIZADO: o capítulo não é o que build/gerar-as-seis.py gera hoje — rode ele')
open(CAP, 'w', encoding='utf-8').write(_novo)
print('AS SEIS PRONTAS — formatadas do `conta.js --json`, na grade')
for j in SEIS:
    print('  %-11s %-9s ×%d  nv %-7s vida %-4d golpe %-10s %.2f pts' % (j['nome'], j['categoria'], j['n'], j['faixa'], j['vida'], j['golpe'], j['pontos']))
