#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Os tres itens baratos da fila, medidos de uma vez.

  1. o PISO da banda do `o golpe` — o `Controlador` derruba pra 20% e o piso e 21%
  2. o TETO de entradas nomeadas — a proposta e 6 / 8, e falta bater o martelo
  3. o `tamanho` — vira regra ou sai

Nenhum numero mora aqui dentro. Tudo lido do dono.
"""
import os, re, sys

REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')

TABELA = '04-fase-1/TABELA.md'
ESCADA = '04-fase-1/a-escada-com-numero.md'
SUKUNA = '03-bloco/RASCUNHO-1-o-bloco.md'
RASC4 = '03-bloco/RASCUNHO-4-o-bloco-em-branco.md'
P26 = 'sistema/03-mecanica/26-bestiario.md'


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


def linha(t, c='='):
    print()
    print(c * 92)
    print(t)
    print(c * 92)


def media_dado(e):
    m = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?$', e.strip())
    return None if not m else int(m.group(1)) * (1 + int(m.group(2))) / 2 + int(m.group(3) or 0)


# ===========================================================================
linha('1. O PISO DA BANDA — o `Controlador` cai pra 20% e o piso publicado e 21%')
# ===========================================================================
mb = pega(ESCADA, r'A banda inteira é de `(\d+)%` a `(\d+)%`', 'a banda', BEST)
PISO, TETO = n(mb.group(1)) / 100, n(mb.group(2)) / 100
mD = pega(TABELA, r'## `Desastre`[\s\S]*?\n\| 30 \| `(\d+)` \| `(\d+)` \| `(\d+)` \| `([^`]+)` \|',
          'o Desastre nv30', BEST)
VIDA_D, DANO_D, ACOES_D, GOLPE_D = n(mD.group(1)), n(mD.group(2)), n(mD.group(3)), mD.group(4)
mf = pega(ESCADA, r'\| 30 \| `\d+%` \| `\d+%` \| `(\d+)%` \|', 'a fatia do Desastre', BEST)
FATIA_D = n(mf.group(1)) / 100
VIDA_PC = media_dado(GOLPE_D) / FATIA_D

print(f'  a banda publicada: {PISO:.0%} a {TETO:.0%}. A vida de um personagem no nv30: {VIDA_PC:.0f}.')
print()
print('  O que a banda EXISTE pra pegar, segundo a propria escada:')
print(f'    "A do bestiário antigo era de 23% a 45%, e O TOPO DELA ERA A `Dupla`."')
print('    >> A banda foi construida pra vigiar o TOPO. O piso e' + ' so onde a `Ameaça` senta.')
print()
print('  A metrica que o piso realmente afeta e a do §4.6 — quantos golpes pra derrubar alguem:')
print()
print(f'  {"fatia":>8}{"o golpe":>10}{"golpes pra derrubar 1 PC":>28}{"golpes na luta (3 rod)":>25}'
      f'{"derruba?":>11}')
print('  ' + '-' * 84)
for rot, corte in (('30% — sem papel', 1.0), ('22,5% — corte de 1/4', 0.75),
                   ('20% — corte de 1/3', 2 / 3), ('15% — corte de 1/2', 0.5)):
    golpe = media_dado(GOLPE_D) * corte
    fatia = golpe / VIDA_PC
    precisa = VIDA_PC / golpe
    tem = ACOES_D * 3
    print(f'  {fatia:>7.0%}{golpe:>10.1f}{precisa:>28.1f}{tem:>25.0f}'
          f'{"sim" if tem >= precisa else "NÃO":>11}')
print()
print(f'  >> Em TODAS as quatro o chefe ainda derruba alguem dentro da luta. O piso nao quebra')
print(f'     a metrica que ele poderia quebrar.')
print(f'  >> E o `Controlador` derrubar mais devagar E O PONTO DELE: ele troca dano por efeito.')
print()
print(f'  As duas saidas, com o numero de cada:')
print(f'    A — a banda vira {2/3*FATIA_D:.0%}–{TETO:.0%}. O `Controlador` corta 1/3, o invariante da')
print(f'        0,667x e ele paga vida x{1/(2/3):.2f}. E o piso passa a ser DELE, nao da `Ameaça`.')
print(f'    B — o `Controlador` corta 1/4 em vez de 1/3. `o golpe` fica em '
      f'{0.75*FATIA_D:.1%}, dentro')
print(f'        da banda de hoje. O invariante da 0,750x e ele paga vida x{1/0.75:.2f}.')


# ===========================================================================
linha('2. O TETO DE ENTRADAS NOMEADAS — contado no unico bloco preenchido que existe')
# ===========================================================================
TXT_S = ler(SUKUNA, BEST)
# uma entrada nomeada e' uma linha que abre com ***Nome.***
entradas = re.findall(r'^\*\*\*([^*]+?)\.?\*\*\*', TXT_S, re.M)
# em que secao cada uma cai
secoes, atual = {}, None
for ln in TXT_S.split('\n'):
    m = re.match(r'^#{2,3} (.+)$', ln)
    if m:
        atual = m.group(1).strip()
        secoes.setdefault(atual, [])
        continue
    m = re.match(r'^\*\*\*([^*]+?)\.?\*\*\*', ln)
    if m and atual:
        secoes[atual].append(m.group(1))
print('  O `Sukuna` do `RASCUNHO-1` — o unico bloco preenchido do projeto. Ele e `Calamidade`,')
print('  entao o teto proposto pra ele e o de CHEFE.')
print()
tot = 0
for s, its in secoes.items():
    if not its:
        continue
    tot += len(its)
    print(f'    {s:<42}{len(its):>3}   ' + ', '.join(f'`{i}`' for i in its))
print(f'    {"":<42}{"—":>3}')
print(f'    {"TOTAL como ele esta escrito hoje":<42}{tot:>3}')
print()
# como ele ficaria nas regras de hoje
mint = pega(RASC4, r'\*`(\d+)` por luta, cada uma \*\*uma vez só\*\*', 'as 3 Intervenções', BEST)
N_INT = int(mint.group(1))
mteto = pega(RASC4, r'Proposta: `(\d+)` entradas num bloco normal, `(\d+)` no chefe',
             'o teto proposto', BEST)
TETO_N, TETO_C = int(mteto.group(1)), int(mteto.group(2))

tracos = len(secoes.get('Traços', []))
acoes_reais = [i for i in secoes.get('Ações', []) if 'Ataque Múltiplo' not in i]
intervencoes = N_INT   # a regra de hoje sao 3, e o rascunho dele tinha 2
hoje = tracos + 1 + len(acoes_reais) + intervencoes   # +1 = o traço de ações
print(f'  E como ele ficaria nas REGRAS DE HOJE:')
print(f'    Traços                                  {tracos}')
print(f'    o traço de ações (substitui `Ataque Múltiplo`)   1')
print(f'    Ações                                   {len(acoes_reais)}   '
      + ', '.join(f'`{a}`' for a in acoes_reais))
print(f'    Intervenções (a regra são {N_INT})            {intervencoes}')
print(f'    {"":<40}—')
print(f'    TOTAL                                   {hoje}')
print()
print(f'  >> O teto proposto e {TETO_N} num bloco normal e {TETO_C} no chefe.')
print(f'  >> O `Sukuna` da {hoje}. **Ele estoura o teto de chefe em {hoje - TETO_C}.**')
print()
print(f'  ⚠ E isso nao e um Sukuna mal montado: {tracos} Traços e {len(acoes_reais)} Ações e o')
print(f'     minimo pra um chefe nao virar "o inimigo de um botao so" — que e o modo de falha')
print(f'     documentado que o `ESTADO-onde-paramos.md` ja registrou.')
print()
print(f'  As tres saidas:')
print(f'    A — o teto sobe pra {hoje} no chefe. O `Sukuna` cabe raspando.')
print(f'    B — as `Intervenções` saem da contagem. Elas sao {N_INT} FIXAS em todo bloco,')
print(f'        entao contar elas e contar constante. Sobrariam {hoje - intervencoes} de {TETO_C}.')
print(f'    C — o teto fica em {TETO_N}/{TETO_C} e o `Sukuna` perde uma entrada.')


# ===========================================================================
linha('3. O `tamanho` — vira regra ou sai')
# ===========================================================================
mt = pega(RASC4, r'\*\*`(\d+)` de `(\d+)` sistemas imprimem um campo de tamanho que não faz nada',
          'a medida do tamanho', BEST)
print(f'  A medida que ja estava feita: `{mt.group(1)}` de `{mt.group(2)}` sistemas imprimem um')
print(f'  campo de tamanho que nao faz nada.')
print()
print('    Draw Steel   usa NUMERO (`3 Size`), e ele governa quadrados e alcance')
print('    PF2e e D&D   usam TRAIT, e ele governa espaço ocupado, agarrar e cobertura')
print('    Daggerheart  NAO TEM o campo')
print()
print('  >> Campo decorativo e o unico caso SEM PRECEDENTE nos quatro.')
print()
print(f'  E o bloco ja banca UM decorativo: o `grau`. A peça 26 §2 fecha isso com todas as letras:')
mg = pega(P26, r'o grau fica na ficha da maldição como rótulo, e não entra em conta nenhuma',
          'o grau decorativo')
print(f'    "{mg.group(0)}"')
print()
print('  >> Entao a pergunta nao e "tamanho pode ser decorativo?" — e "o bloco banca DOIS')
print('     decorativos?". O `grau` se paga porque ele e a linguagem da obra (grau 1, especial).')
print('     O `tamanho` nao tem esse apoio: em JJK ninguem fala "maldicao Grande".')
