#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A tabela de PONTOS POR AÇÃO, refeita na escada nova.

O §6.5 da peca 26 publica ela na escada VELHA (`Ronda` · `Dupla` · `Alcateia` ·
`Calamidade`), e essas categorias morreram. E a recalibracao da `Intervenção`
(x 0,923) move o golpe de novo.

A regra e uma linha, e ela e do §6.5:

    o orcamento de feitico de uma acao e' `o golpe` dela dividido por `4,5`

E o piso tambem e' dele: abaixo de `3` pontos (a `Classe 1`, que sao 13,5 de dano)
o inimigo nao monta feitico nenhum — ele bate, e o golpe sai como o §4.4 manda.
"""
import os, re, sys

REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
P19 = 'sistema/03-mecanica/19-dano-e-condicoes.md'
P26 = 'sistema/03-mecanica/26-bestiario.md'
TABELA = '04-fase-1/TABELA.md'


def ler(rel, raiz=REPO):
    with open(os.path.join(raiz, rel), encoding='utf-8') as f:
        return f.read()


def n(s):
    return float(s.replace(',', '.'))


def pega(rel, padrao, rotulo, raiz=REPO):
    m = re.search(padrao, ler(rel, raiz))
    if not m:
        print(f'  !! ancora perdida: {rotulo} — nao casa em {rel}')
        sys.exit(1)
    return m


def media_dado(e):
    e = e.strip()
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e)
    if m:
        return int(m.group(1)) * (1 + int(m.group(2))) / 2 + int(m.group(3) or 0)
    return float(e) if re.match(r'^\d+$', e) else None


print('=' * 92)
print('AS ANCORAS')
print('=' * 92)
PONTO = n(pega(P19, r'cada ponto que não vira Melhoria vira `1d8` de dano — que são `([\d,]+)`',
               'o ponto de feitico').group(1))
regra = pega(P26, r'O orçamento de feitiço de uma ação é o golpe dela dividido por `([\d,]+)`',
             'a regra do §6.5')
if abs(n(regra.group(1)) - PONTO) > 0.01:
    print(f'  !! o §6.5 divide por {regra.group(1)} e a peca 19 diz que o ponto vale {PONTO}')
    sys.exit(1)
PISO_PONTOS = n(pega(P26, r'o menor feitiço do manual é a `Classe 1` e custa `(\d+)` pontos',
                     'o piso da Classe 1').group(1))
# 11/09/2026: o fator era digitado aqui dentro. Agora ele sai do dono — o §6.5 da
# propria peca 26 publica ele por extenso.
FATOR_INT = n(pega(P26, r'o fator de dano de quem carrega `Intervenção` é multiplicado '
                        r'por `([\d,]+)`', 'o fator da Intervenção, no §6.5').group(1))
COM_INT = {'Ameaça': False, 'Desastre': True, 'Catástrofe': True, 'Calamidade': True}

# ── o dado() do make.js, portado. Ele e' preciso aqui porque a ROTA do orcamento e'
#    a `B`: o fator entra ANTES de escolher o dado, e o que se divide por 4,5 e' a
#    media do golpe IMPRESSO. Ate 11/09 este script fazia a rota `A` — media do golpe
#    CRU vezes o fator — e dava 9 celulas diferentes do §6.5.
#    A medida esta em `fila/medir-a-rota-do-orcamento.py`.
MAKE = 'sistema/05-material/gerador-inimigo/make.js'
_mk = ler(MAKE)
_DADOS = [int(x) for x in pega(MAKE, r'const DADOS = \[([\d,\s]+)\]', 'o DADOS do make.js')
          .group(1).split(',')]
_PISO_D = int(pega(MAKE, r'if \(alvo < (\d+)\) return String\(arred\(alvo\)\)',
                   'o piso do dado no make.js').group(1))
_TETO_D = int(pega(MAKE, r'if \(n > (\d+)\) continue', 'o teto de dados no make.js').group(1))
if 'Math.round' not in _mk:
    print('  !! o make.js parou de usar Math.round — o meio-ponto deste port vem de la')
    sys.exit(1)

import math
arred = lambda x: math.ceil(x - 0.5)            # make.js: Math.ceil(x - 0.5)
jsr = lambda x: math.floor(x + 0.5)             # Math.round do JS: o meio SOBE


def dado(alvo):
    if alvo < _PISO_D:
        return str(arred(alvo))
    meta, bom = alvo / 2, None
    for d in _DADOS:
        med = (d + 1) / 2
        k = max(1, jsr(meta / med))
        if k > _TETO_D:
            continue
        fixo = alvo - k * med
        if fixo < 0:
            continue
        inteiro = 0 if abs(fixo - jsr(fixo)) < 1e-9 else 1
        er = abs(k * med - meta)
        if (bom is None or inteiro < bom[0] or (inteiro == bom[0] and er < bom[1] - 1e-9)
                or (inteiro == bom[0] and abs(er - bom[1]) < 1e-9 and k < bom[2])):
            bom = (inteiro, er, k, d, jsr(fixo))
    if bom is None:
        k = max(1, jsr(alvo / 9))
        r = arred(alvo - 4.5 * k)
        return '%dd8 + %d' % (k, r) if r > 0 else '%dd8' % k
    return ('%dd%d + %d' % bom[2:]) if bom[4] > 0 else '%dd%d' % (bom[2], bom[3])

print(f'  1 ponto de feitiço vale        {PONTO:.1f} de dano       peça 19 §2.1')
print(f'  a regra do §6.5                golpe ÷ {PONTO:.1f}')
print(f'  o piso                         {PISO_PONTOS:.0f} pontos = {PISO_PONTOS*PONTO:.1f} de dano '
      f'(a `Classe 1`)')
print(f'  o fator da `Intervenção`       × {FATOR_INT:.3f}, só pra quem tem     decisão de 10/09')

# le a TABELA nova
CATS, ROD, atual = {}, {}, None
for ln in ler(TABELA, BEST).split('\n'):
    m = re.match(r'## `([^`]+)`', ln)
    if m:
        atual = m.group(1)
        CATS.setdefault(atual, {})
        ROD.setdefault(atual, {})
        continue
    # nv | vida | dano/rod | acoes | o golpe — as duas colunas do meio sao o que a
    # rota `B` precisa: o fator entra no dano de RODADA, antes de escolher o dado.
    m = re.match(r'\| (\d+) \| `\d+` \| `(\d+)` \| `(\d+)` \| `([^`]+)` \|', ln)
    if m and atual:
        g = media_dado(m.group(4))
        if g is not None:
            CATS[atual][int(m.group(1))] = g
            ROD[atual][int(m.group(1))] = (int(m.group(2)), int(m.group(3)))
    # o Capanga tem outra forma: nv | vida de um | pool | golpe de um | ...
    m = re.match(r'\| (\d+) \| `\d+` \| \*\*`\d+`\*\* \| `([^`]+)` \|', ln)
    if m and atual == 'Capanga':
        g = media_dado(m.group(2))
        if g is not None:
            CATS[atual][int(m.group(1))] = g

ORDEM = ['Capanga', 'Ameaça', 'Desastre', 'Catástrofe', 'Calamidade']
faltando = [c for c in ORDEM if c not in CATS or not CATS[c]]
if faltando:
    print(f'  !! nao li o golpe de: {", ".join(faltando)}')
    sys.exit(1)



def impresso(c, nv):
    """O golpe como a FICHA imprime ele — a rota `B`, que e' a validada.

    Quem carrega `Intervenção` leva o fator no dano de RODADA e so' depois escolhe o
    dado; quem nao carrega imprime o golpe da propria TABELA."""
    if not COM_INT.get(c, False):
        return CATS[c][nv]
    rod, ac = ROD[c][nv]
    return media_dado(dado(arred(rod * FATOR_INT) / ac))


def pontos(c, nv):
    return impresso(c, nv) / PONTO


print()
print('=' * 92)
print('PONTOS POR ACAO — a escada nova, pelo golpe IMPRESSO (a rota `B`)')
print('=' * 92)
print(f'  `seco` = abaixo de {PISO_PONTOS:.0f} pontos. Ali ele NAO monta feitico: ele bate.')
print()
NIVEIS = [2, 5, 10, 15, 20, 25, 30]
print(f'  {"nível":<7}' + ''.join(f'{c:>14}' for c in ORDEM))
print('  ' + '-' * 77)
for nv in NIVEIS:
    ln = f'  {nv:<7}'
    for c in ORDEM:
        if nv not in CATS[c]:
            ln += f'{"—":>14}'
            continue
        pts = pontos(c, nv)
        ln += f'{("seco" if pts < PISO_PONTOS else f"{pts:.1f}"):>14}'
    print(ln)

print()
print('=' * 92)
print('A CONFERENCIA — esta conta bate com a tabela que o §6.5 PUBLICA?')
print('=' * 92)
# Ate 11/09 aqui morava uma comparacao com a escada VELHA, escrita a mao
# ("Ronda 12,2 · Dupla 24,2 · Alcateia 16,2 · Calamidade 14,6"). A v0.221 trocou a
# escada e a v0.222 trocou a rota do orcamento — entao o lugar dessa comparacao e' o
# museu, e o que este script faz agora e' CONFERIR contra o que esta publicado.
PUB, dentro = {}, False
for ln_ in ler(P26).split('\n'):
    if ln_.startswith('| pontos por ação |'):
        dentro = True
        continue
    if dentro:
        m = re.match(r'\| nível (\d+) \|(.+)\|\s*$', ln_)
        if not m:
            if ln_.startswith('|---'):
                continue
            dentro = False
            continue
        cels = [c.strip().strip('`') for c in m.group(2).split('|')]
        PUB[int(m.group(1))] = dict(zip(ORDEM, cels))
if len(PUB) != len(NIVEIS):
    print(f'  !! ancora perdida: a tabela do §6.5 mudou de forma (li {len(PUB)} linhas)')
    sys.exit(1)

print(f'  {"nível":<7}' + ''.join(f'{c:>26}' for c in ORDEM))
print('  ' + '-' * 137)
difere = []
for nv in NIVEIS:
    ln_ = f'  {nv:<7}'
    for c in ORDEM:
        pts = pontos(c, nv)
        meu = 'seco' if pts < PISO_PONTOS else f'{pts:.1f}'.replace('.', ',')
        pub = PUB[nv][c]
        bate = meu == pub
        if not bate:
            difere.append((nv, c, pub, meu))
        ln_ += f'{(meu if bate else f"{pub} -> {meu}  X"):>26}'
    print(ln_)
print()
if difere:
    print(f'  !! ANCORA PERDIDA: {len(difere)} celula(s) da conta nao batem com o §6.5 publicado:')
    for nv, c, pub, meu in difere:
        print(f'     nivel {nv:<3} {c:<12} a peca publica {pub:<6} e a conta da {meu}')
    print('     Um dos dois esta velho. A rota validada e a `B` — o golpe IMPRESSO —,')
    print('     e a medida dela esta em `fila/medir-a-rota-do-orcamento.py`.')
    sys.exit(1)
print(f'  ✓ as {len(NIVEIS) * len(ORDEM)} celulas batem com a tabela publicada no §6.5.')
print('    ⟹ o Bestiario e a peca 26 contam a mesma coisa. Enquanto este script passar,')
print('      a tabela do §6.5 nao saiu do lugar sem a conta saber.')
print()
rod30, ac30 = ROD['Desastre'][30]
print('  E o efeito do fator da `Intervenção` no `Desastre` nv30, pela rota `B`:')
print(f'    sem o fator   {rod30} de rodada / {ac30} acoes -> golpe {dado(rod30/ac30):<10}'
      f' media {media_dado(dado(rod30/ac30)):.1f}  ->  {media_dado(dado(rod30/ac30))/PONTO:.1f} pontos')
print(f'    com o fator   {arred(rod30*FATOR_INT)} de rodada / {ac30} acoes -> golpe '
      f'{dado(arred(rod30*FATOR_INT)/ac30):<10} media {impresso("Desastre", 30):.1f}'
      f'  ->  {pontos("Desastre", 30):.1f} pontos')

print()
print('=' * 92)
print('O QUE ESTA TABELA RESPONDE — a pergunta do Mizuki de 10/09')
print('=' * 92)
d = impresso('Desastre', 30)
pts = pontos('Desastre', 30)
print(f'  "como o mestre cria uma ação de um `Desastre` de nível 30?"')
print()
print(f'    o golpe dele e {d:.1f}  ->  {pts:.1f} pontos de feitiço naquela ação.')
print(f'    o mestre monta com {pts:.1f} pontos no Fundamento, igual a um feitiço de jogador.')
print()
print(f'  "e se ele quiser condição?"     tira ponto dos dados. A peça 19 §2.2 ja preca.')
print(f'  "e se for em área?"             o Fundamento ja cobra por area, em ponto.')
print(f'  "e uma ação diferente da outra?" cada uma tem o golpe DELA, e o orcamento DELA.')
