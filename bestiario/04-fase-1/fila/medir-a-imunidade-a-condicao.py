#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A REGUA da imunidade a CONDICAO no inimigo.

Aberta pelo martelo `C` do `MEDIDA-a-resistencia-e-a-vulnerabilidade.md`:
a peca 19 e a peca 26 nao precam imunidade a condicao em lugar nenhum, e o
campo imprime ela em 22,7% dos blocos do D&D 2024.

A tese: ela e a IRMA da resistencia a dano do §6.3.
  resistir a dano   -> o inimigo recebe menos -> vida efetiva sobe
  imune a condicao  -> o inimigo perde menos ACAO -> saida efetiva sobe
E as duas se pagam do mesmo jeito: multiplicando o fator da categoria.

Nenhum numero nasce aqui. Todas as ancoras sao lidas dos donos, e o script
morre se qualquer uma mudar.
"""
import os
import re
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')

# 11/09/2026: as tres liam `finalizado/regra/`, que e a COPIA do recorte. O dono e a
# fonte, e a copia so' e sincronizada no passo 0 do subir.sh — ela atrasa sozinha.
P19 = 'sistema/03-mecanica/19-dano-e-condicoes.md'
P26 = 'sistema/03-mecanica/26-bestiario.md'
P11 = 'sistema/03-mecanica/11-aptidoes-e-refino.md'
PARTD = 'manual/gerador/partD.js'

_cache = {}


def ler(rel, raiz=REPO):
    k = (rel, raiz)
    if k not in _cache:
        with open(os.path.join(raiz, rel), encoding='utf-8') as f:
            _cache[k] = f.read()
    return _cache[k]


def pega(rel, padrao, rotulo, raiz=REPO, flags=0):
    m = re.search(padrao, ler(rel, raiz), flags)
    if not m:
        print(f'\n  !! ANCORA PERDIDA: {rotulo}\n     nao casa em {rel}\n     padrao: {padrao}')
        sys.exit(1)
    return m


def bloco(t):
    print()
    print('=' * 96)
    print(t)
    print('=' * 96)


# ------------------------------------------------------------ 0 · as ancoras
bloco('0 · AS ÂNCORAS — todas lidas dos donos')

# A frase dos "nove golpes" do §5 morreu de proposito na v0.221, junto com a escada.
# Os dois numeros dela continuam publicados, em dois donos separados e melhores:
#   as acoes, na COLUNA da tabela da escada do §4 — numero, e nao prosa
#   as rodadas, na frase do §4.6 que mede quantas pessoas o chefe derruba
EXTENSO = {'duas': 2, 'três': 3, 'quatro': 4, 'cinco': 5, 'seis': 6}
m = pega(P26, r'\| \*\*`Desastre`\*\* \| \d+ \| `× [\d,]+` \| `(\d+)` \|',
         'peça 26 §4 — as ações do `Desastre` na tabela da escada')
ACOES = int(m.group(1))
m = pega(P26, r'Numa luta de (\w+) rodadas ele derruba `[\d,]+` pessoas se concentrar',
         'peça 26 §4.6 — de quantas rodadas é a luta')
RODADAS = EXTENSO.get(m.group(1))
if not RODADAS:
    sys.exit('  !! ANCORA PERDIDA: o §4.6 passou a dizer "%s" rodadas' % m.group(1))
GOLPES = ACOES * RODADAS
print(f'  peça 26 §4 · o chefe (um `Desastre`) age {ACOES}× por rodada, e o §4.6 põe a luta '
      f'em {RODADAS} rodadas '
      f'⟹ {GOLPES} golpes na luta')

m = pega(P26, r'o inimigo acerta `(\d+)%`', 'peça 26 §6.4 — o acerto do inimigo')
ACERTO = int(m.group(1)) / 100.0
print(f'  peça 26 §6.4 · o inimigo acerta {m.group(1)}% fora de domínio')

m = pega(P11, r'\| vantagem na rolagem \| \d+% \| \*\*\+(\d+) pp\*\* \|',
         'peça 11 — o valor de vantagem/desvantagem')
PP = int(m.group(1)) / 100.0
print(f'  peça 11 · vantagem/desvantagem vale ±{m.group(1)} pontos percentuais')

m = pega(P19, r'o `Lento` cobra (\w+), o `Calado` e o `Enfeitiçado` (\w+), o `Atordoado` ([\w ]+?) —,',
         'peça 19 §2.2 — quantas ações cada condição cobra')
PALAVRA = {'meia': 0.5, 'uma': 1.0, 'uma e meia': 1.5}
CUSTO_ACAO = {'Lento': PALAVRA[m.group(1)], 'Calado': PALAVRA[m.group(2)],
              'Enfeitiçado': PALAVRA[m.group(2)], 'Atordoado': PALAVRA[m.group(3)]}
print(f'  peça 19 §2.2 · ações cobradas — ' + ' · '.join(f'{k} {v:g}' for k, v in CUSTO_ACAO.items()))

# as treze condicoes e o nivel de cada uma, lidas da peca 19 §3
NIVEL = {}
tx19 = ler(P19)
sec = tx19[tx19.index('## 3. As treze condições'):tx19.index('### 3.4')]
for m in re.finditer(r'\| \*\*`([^`]+)`\*\* \| `(Leve|Média|Pesada)` \|', sec):
    NIVEL[m.group(1)] = m.group(2)
print(f'\n  peça 19 §3 · {len(NIVEL)} condições lidas: '
      + ' · '.join(f'{k}({v[0]})' for k, v in NIVEL.items()))
if len(NIVEL) < 13:
    print(f'  !! a peça declara TREZE e o script leu {len(NIVEL)}')
    sys.exit(1)

# ⚠ a DURACAO e publicada, e ela e UMA RODADA pra todas as treze
m = pega(PARTD, r'Aplica uma das treze condições\.[^\n]*?Dura (uma|duas|três) rodadas?\.',
         'partD.js — a duracao da Melhoria Condicao')
DUR = {'uma': 1, 'duas': 2, 'três': 3}[m.group(1)]
print(f'  partD.js · a Melhoria `Condição` dura {m.group(1)} rodada ⟹ DUR = {DUR}')
tr_pesada = 'Só as de nível `Pesada` dão Teste de Resistência no fim de cada turno' in tx19
print(f'  peça 19 §3.3 · e só as `Pesada` dão TR no fim de cada turno: '
      f'{"SIM" if tr_pesada else "NAO"}  ⟹ a `Pesada` pode acabar ANTES de {DUR} rodada, nunca depois')

# quem da desvantagem NAS ROLAGENS do alvo — lido do texto de cada condicao
DESV = {}
for m in re.finditer(r'\| \*\*`([^`]+)`\*\* \| `(?:Leve|Média|Pesada)` \| ([^|]+) \|', sec):
    nome, txt = m.group(1), m.group(2)
    if re.search(r'desvantagem (?:nos seus ataques|em ataque|nos seus)', txt):
        DESV[nome] = True
print(f'  peça 19 §3 · dão desvantagem nos ataques DELE: ' + ' · '.join(DESV) or '(nenhuma)')


# ------------------------------------------------------------------ 1 · a régua
bloco('1 · A RÉGUA — quanto cada condição TIRA do inimigo, e quanto a imunidade vale')

print(f'''
  O inimigo entrega {GOLPES} golpes na luta ({ACOES} ações × {RODADAS} rodadas).
  Uma condição dura {DUR} rodada (publicado), então ela apaga `a × {DUR}` desses {GOLPES}.
  Ser IMUNE devolve isso ⟹ fator × {GOLPES}/({GOLPES} − a×{DUR}).

  Uma condição de desvantagem não tira ação: ela derruba o acerto de
  {ACERTO*100:.0f}% para {(ACERTO-PP)*100:.0f}%, e o que sai naquela rodada vale
  {(ACERTO-PP)/ACERTO:.3f}× — o resto é ação perdida equivalente.
''')

FATOR_DESV = (ACERTO - PP) / ACERTO
linhas = []
for cond, niv in NIVEL.items():
    dur = DUR                                    # publicado: toda condicao dura 1 rodada
    if cond in CUSTO_ACAO:
        perdidas = CUSTO_ACAO[cond] * dur
        como = f'rouba {CUSTO_ACAO[cond]:g} ação × {dur} rodada' + ('s' if dur > 1 else '')
    elif cond in DESV:
        perdidas = ACOES * (1 - FATOR_DESV) * dur
        como = f'desvantagem × {dur} rodada' + ('s' if dur > 1 else '')
    else:
        perdidas = 0.0
        como = 'não toca ação nem acerto do inimigo'
    fator = GOLPES / (GOLPES - perdidas) if perdidas < GOLPES else float('inf')
    linhas.append((cond, niv, perdidas, fator, como))

linhas.sort(key=lambda x: -x[2])
print(f'    {"condição":<15}{"nível":<8}{"ações apagadas":>16}{"do total":>10}'
      f'{"imunidade vale":>16}   como')
for cond, niv, p, f, como in linhas:
    if p == 0:
        print(f'    {cond:<15}{niv:<8}{"—":>16}{"—":>10}{"1,00×":>16}   {como}')
    else:
        print(f'    {cond:<15}{niv:<8}{p:>16.2f}{100*p/GOLPES:>9.1f}%'
              f'{("× " + f"{f:.2f}").replace(".", ","):>16}   {como}')

# agrupado por nivel
bloco('2 · AGRUPANDO POR NÍVEL — a tabela que caberia no §6.3')
print(f'    {"nível":<10}{"condições":>11}{"a que mais tira":>32}{"imunidade a ELA vale":>22}')
for niv in ('Leve', 'Média', 'Pesada'):
    grp = [x for x in linhas if x[1] == niv]
    top = max(grp, key=lambda x: x[2])
    print(f'    {niv:<10}{len(grp):>11}{top[0]:>32}'
          f'{("× " + f"{top[3]:.2f}").replace(".", ","):>22}')

print(f'''
  ⟹ A LINHA QUE FALTA no §6.3, e ela sai pronta:

     "Ser imune a uma condição multiplica o fator da categoria pelo valor dela:
      as de nível `Leve` por {min(x[3] for x in linhas if x[1]=="Leve"):.2f} a {max(x[3] for x in linhas if x[1]=="Leve"):.2f},
      as `Média` por {max(x[3] for x in linhas if x[1]=="Média"):.2f},
      as `Pesada` por {max(x[3] for x in linhas if x[1]=="Pesada"):.2f}.
      Imunidade a condição que não tira ação nem acerto do inimigo custa 1,00×."
''')


# ------------------------------------------- 3 · a conferência contra o §6.3
bloco('3 · CONFERINDO CONTRA O §6.3 — as duas réguas têm de ter a mesma FORMA')

PRECO = {}
for grupo in ('Físicos', 'Elementais', 'Especiais'):
    m = pega(P26, r'\| `' + grupo + r'` \| `(\d+)%` \| \*{0,2}`([\d,]+)×`\*{0,2} \| '
             r'\*{0,2}`([\d,]+)×`\*{0,2} \|', f'peça 26 §6.3 — {grupo}')
    PRECO[grupo] = (int(m.group(1)) / 100.0,
                    float(m.group(2).replace(',', '.')),
                    float(m.group(3).replace(',', '.')))

print('  §6.3 · resistir/ser imune a DANO:   fator × 1 ÷ (1 − fatia que ele deixa de receber)')
print('  aqui  · ser imune a CONDIÇÃO:       fator × 1 ÷ (1 − fatia que ele deixa de perder)')
print()
for g, (w, r, i) in PRECO.items():
    print(f'    {g:<12} imune apaga {w*100:4.0f}% do dano recebido  ⟹  × {i:.2f}   '
          f'(1 ÷ (1 − {w:.2f}) = {1/(1-w):.2f})')
print()
maior = max(linhas, key=lambda x: x[2])
print(f'    {maior[0]:<12} imune apaga {100*maior[2]/GOLPES:4.1f}% das ações dele  ⟹  '
      f'× {maior[3]:.2f}   (1 ÷ (1 − {maior[2]/GOLPES:.3f}) = {1/(1-maior[2]/GOLPES):.2f})')

print('''
  ### ⟹ É A MESMA FÓRMULA. A régua da condição não é régua nova — é o §6.3
      aplicado no eixo da AÇÃO em vez do eixo do DANO.

  ⚠ E ela erra pro lado SEGURO, como a resistência e ao contrário da
    vulnerabilidade: se ninguém no grupo comprou aquela condição, o inimigo
    pagou por uma imunidade que não usou, e o encontro foi cobrado mais caro
    do que é. A mesa ganha.

  ⚠ E o que NÃO está contado aqui, de propósito:
    · a vantagem que `Cego`/`Derrubado`/`Impedido` dão a QUEM ATACA ele
      (isso mexe na vida efetiva, não na saída — é outro eixo, e conta duas
       vezes se entrar aqui)
    · o `Incapacitado`, que transforma acerto corpo a corpo em crítico
  ⟹ Os dois deixam a régua CONSERVADORA. Declarado, não esquecido.''')

bloco('FIM')
