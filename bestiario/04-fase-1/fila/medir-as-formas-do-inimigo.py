#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AS FORMAS DE AREA DO INIMIGO — resolvidas so do lado do inimigo.

Pedido dele, 10/09/2026: "vamos resolver isso tudo pelo lado do inimigo,
depois eu tento pasar pro player".

O `MEDIDA-o-quadrado-e-o-retangulo.md` achou tres defeitos:
  1 · o `Cone` nao tem abertura definida  (cobertura varia 3,0x)
  2 · `Cone`, `Linha` e `Esfera` custam `Leve` e cobrem 20x de diferenca no d5
  3 · o `Anteparo` nao tem dimensao nenhuma

A saida que resolve os tres de uma vez: no lado do INIMIGO a area ja nao e
comprada com degrau — ela e DE GRACA e sai do NIVEL (item 15, fechado).
Entao o inimigo nao precisa de escada por forma. Ele precisa de UMA
COBERTURA por nivel, e as formas sao jeitos diferentes de gastar ela.

Nenhum numero nasce aqui: a cobertura por nivel e lida do `RASCUNHO-5`.
"""
import math
import os
import re
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')

BLOCO = '03-bloco/RASCUNHO-5-o-bloco-em-branco.md'
PARTC = 'manual/gerador/partC.js'
PARTD = 'manual/gerador/partD.js'

_cache = {}


def ler(rel, raiz=BEST):
    k = (rel, raiz)
    if k not in _cache:
        with open(os.path.join(raiz, rel), encoding='utf-8') as f:
            _cache[k] = f.read()
    return _cache[k]


def pega(rel, padrao, rotulo, raiz=BEST, flags=0):
    m = re.search(padrao, ler(rel, raiz), flags)
    if not m:
        print(f'\n  !! ANCORA PERDIDA: {rotulo}\n     nao casa em {rel}\n     padrao: {padrao}')
        sys.exit(1)
    return m


def n(s):
    return float(s.replace(',', '.'))


def bloco(t):
    print()
    print('=' * 96)
    print(t)
    print('=' * 96)


# ---------------------------------------------------------------- 0 · âncoras
bloco('0 · AS ÂNCORAS — a área natural do inimigo, já fechada')

FAIXAS = []
for m in re.finditer(r'\| `(\d+)`–`(\d+)` \| \*\*`([\d,]+) m`\*\* \| `(\d+)` quadrados \| '
                     r'`(\d+)` quadrados', ler(BLOCO)):
    FAIXAS.append({'de': int(m.group(1)), 'ate': int(m.group(2)), 'raio': n(m.group(3)),
                   'cobre': int(m.group(4)), 'larg': int(m.group(5))})
if len(FAIXAS) != 4:
    print(f'  !! esperava 4 faixas de nível na área natural, li {len(FAIXAS)}')
    sys.exit(1)
QUAD = 2 * FAIXAS[0]['raio'] / FAIXAS[0]['larg']
print(f'  RASCUNHO-5 · o quadrado da grade é {QUAD:g} m')
for f in FAIXAS:
    print(f"    nv {f['de']:>2}–{f['ate']:<2}  raio {f['raio']:>4g} m   "
          f"cobre {f['cobre']:>3} quadrados   largura {f['larg']} quadrados")

m = pega(BLOCO, r'DE GRAÇA, pelo mesmo motivo que o `tamanho`', 'RASCUNHO-5 — a área é de graça')
print('\n  ✅ e ela é DE GRAÇA — "o preço da área já foi fechado supondo que ela pega a mesa inteira"')
print('  ⟹ o inimigo NÃO precisa de escada por forma. Ele precisa de UMA cobertura por nível.')


# ------------------------------------------------- 1 · a abertura do Cone
bloco('1 · A ABERTURA DO CONE — e o campo NÃO é unânime')

ABERTURAS = {
    'D&D 2024': (1.000, 'a largura em qualquer ponto é igual à distância até a origem',
                 'triângulo — área = L²/2'),
    'PF2e': (math.pi / 2, 'um quarto de círculo na grade',
             'setor de 90° — área = πL²/4'),
}
print('  as duas definições publicadas, e elas dão áreas diferentes:\n')
for sis, (ab, txt, forma) in ABERTURAS.items():
    print(f'    {sis:<12} abertura {ab:.3f}   {forma}')
    print(f'    {"":<12} "{txt}"')
raz = ABERTURAS['PF2e'][0] / ABERTURAS['D&D 2024'][0]
print(f'\n  ⟹ o cone do PF2e é {raz:.2f}× o do D&D no mesmo comprimento. Não dá pra "seguir o campo":')
print('     tem de escolher UM, e o critério é qual dá pra DESENHAR contando quadrado.')
print()
print('     D&D  · "a largura é igual à distância" ⟹ a 4 quadrados de você, o cone tem 4 de largura.')
print('            Conta-se na grade, sem transferidor e sem template.')
print('     PF2e · quarto de círculo ⟹ precisa do diagrama publicado do livro.')
print('            A regra deles remete a uma FIGURA, não a uma frase.')
print()
print('  ### ⟹ recomendação: a do D&D (1,000). É a única que se desenha contando.')
AB = ABERTURAS['D&D 2024'][0]


# ------------------------------------- 2 · a tabela, em QUADRADO INTEIRO
bloco('2 · A TABELA DO INIMIGO — e o quadrado e a linha são A MESMA FORMA')

print("""
  O `Quadrado` e a `Linha` nao sao duas formas. Sao o mesmo RETANGULO com
  proporcoes diferentes: a linha e `A x 1`, o quadrado e `A x A`, e o cubo do
  D&D e o quadrado visto de cima. Uma regra cobre as tres.

  Entao o inimigo tem TRES formas, e nao cinco:
    Esfera     — um raio, do corpo dele ou de um ponto
    Cone       — um comprimento, sempre do corpo dele
    Retangulo  — `A x B` quadrados, e o quadrado e a linha sao casos dele
""")


def retangulos(N, tol=0.10):
    """Todos os A x B em quadrado INTEIRO que cobrem N com <= tol de erro."""
    saida = []
    for b in range(1, int(math.isqrt(N)) + 2):
        for a in range(b, 4 * N + 1):
            if abs(a * b - N) / N <= tol:
                saida.append((a, b))
    saida.sort(key=lambda ab: abs(ab[0] / ab[1] - 1))   # do mais quadrado ao mais fino
    return saida


print(f'    {"nível":<10}{"cobre":>7}{"Esfera":>16}{"Cone":>18}   Retângulo — os A × B que cabem')
TAB = []
for f in FAIXAS:
    N = f['cobre']
    lado_cone = round(math.sqrt(2 * N / AB))            # em QUADRADOS
    c_m = lado_cone * QUAD
    rets = retangulos(N)
    TAB.append({'faixa': f, 'cone_q': lado_cone, 'cone_m': c_m, 'rets': rets})
    txt = '  '.join(f'{a}×{b}' for a, b in rets[:5])
    print(f"    nv {f['de']:>2}–{f['ate']:<5}{N:>5}q   raio {f['raio']:>4g} m"
          f"{c_m:>12g} m ({lado_cone}q)   {txt}")

print('\n  conferindo o que cada uma cobre depois de virar quadrado inteiro\n')
print(f'    {"nível":<10}{"alvo":>6}{"Esfera":>9}{"Cone":>9}{"Retâng.":>10}{"  pior erro":>13}')
pior = 0.0
for t in TAB:
    f = t['faixa']
    N = f['cobre']
    ce = math.pi * f['raio'] ** 2 / QUAD ** 2
    cc = t['cone_q'] ** 2 * AB / 2
    a, b = t['rets'][0]
    cr = a * b
    erros = [abs(x - N) / N for x in (ce, cc, cr)]
    pior = max(pior, max(erros))
    print(f"    nv {f['de']:>2}–{f['ate']:<5}{N:>5}{ce:>9.0f}{cc:>9.0f}{cr:>10}"
          f"{100*max(erros):>12.1f}%")

print(f'\n  ⟹ o pior erro em 12 células é {100*pior:.1f}%.')
print(f'     Hoje, no lado do jogador: {800/40:.0f}× entre o `Cone` e a `Linha` NO MESMO DEGRAU.')

print("""
  ### ⟹ E o argumento de por que TEM de ser a mesma cobertura:
      no inimigo a area e DE GRACA (item 15). Se formas de graca cobrissem
      areas diferentes, o mestre escolheria sempre a maior, e a "escolha de
      forma" seria mentira. Cobertura igual e o que faz "de graca" ser honesto.
      *E e exatamente esse o defeito do lado do jogador: la as tres custam
      `Leve` e o `Cone` cobre 20x a `Linha` — entao o `Cone` domina.*
""")

# ---------------------------------------------- 3 · a parede / o Anteparo
bloco('3 · A PAREDE DO INIMIGO — o `Anteparo` sem dimensão')

m = pega(PARTD, r"\['Anteparo', '(\w+)', '([^']+)'\]", 'partD.js — o Anteparo', REPO)
print(f"  partD.js · `Anteparo` custa {m.group(1)} — \"{m.group(2)}\"")
print('  ⟹ tem vida e duração. NÃO tem comprimento, altura, nem onde é colocada.\n')

print('  o campo dá os três de graça:')
print('    D&D 2024 · Wall of Fire ....... 18 m × 6 m × 0,3 m')
print('    Draw Steel · "X wall" ......... X quadrados contíguos, cada um partilhando um LADO')
print()
print('  a saída que não inventa número: a parede é a LINHA, de pé.')
for t in TAB:
    f = t['faixa']
    # a parede tem de ter ALTURA que ninguem passe por cima: >= 2 quadrados (3 m)
    altas = [ab for ab in t['rets'] if ab[1] >= 2] or t['rets']
    a, b = max(altas, key=lambda ab: ab[0] / ab[1])
    print(f"    nv {f['de']:>2}–{f['ate']:<3} parede de {a} quadrados de comprimento "
          f"({a*QUAD:g} m) × {b} de altura ({b*QUAD:g} m) — {a*b} quadrados")
print('\n  ⟹ o `Anteparo` do inimigo não precisa de tabela própria: ele é a `Linha` da faixa,')
print('     colocada de pé em vez de deitada. Zero número novo.')


# ------------------------------------------------------- 4 · o footprint
bloco('4 · O FOOTPRINT DO CORPO — e ele é execução, não decisão')

# ja aplicado no RASCUNHO-5 — agora o script CONFERE em vez de propor
CAMPO = {'Médio': 1, 'Grande': 2, 'Imenso': 3, 'Colossal': 4}   # unanime em D&D, PF2e, Draw Steel
lidos = {}
for m in re.finditer(r'\| [^|]*\*\*`(Médio|Grande|Imenso|Colossal)`\*\* \| \*\*`(\d+)×(\d+)`\*\*', ler(BLOCO)):
    if m.group(2) != m.group(3):
        print(f'  !! o footprint do `{m.group(1)}` nao e quadrado: {m.group(2)}×{m.group(3)}')
        sys.exit(1)
    lidos[m.group(1)] = int(m.group(2))
if lidos != CAMPO:
    print(f'  !! o RASCUNHO-5 publica {lidos}, e o campo da {CAMPO}')
    sys.exit(1)
print('  RASCUNHO-5 · a tabela do Passo 3 ja publica o footprint, e ele CONFERE com o campo:\n')
for nome, lado in CAMPO.items():
    print(f'    {nome:<12}{lado}×{lado} quadrados = {lado*lado:>2}   '
          f'({lado*QUAD:g} m × {lado*QUAD:g} m)')
print(f'\n  ✅ {len(lidos)} de {len(CAMPO)} batem. Unanime em D&D 2024, PF2e e Draw Steel.')
print('  ⟹ e é DE GRAÇA pelo item 16 — o `tamanho` já não cobra nada.')

bloco('FIM')
