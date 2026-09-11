#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RECALIBRAR a escada com a `Intervenção` DENTRO do orçamento.

Correcao de enquadramento do Mizuki, 10/09/2026:

  *"vc esta calculando as coisas dentro do nosso escopo como se ele fosse imutavel,
   podemos mexer nos inimigos ja esperando esses valores... Diminuir a banda de dano
   de todos os inimigos, para que quando chegasse as opcoes de intervencoes elas
   transformarem o combate em algo mais letal mesmo... tudo pode ser reajustado,
   oq n podemos reajustar e a IDEIA:
     1 - Inimigo tem acoes
     2 - Intervencoes sao acoes extras em meio aos turnos dos alvos. Nenhum sistema
         come acao do turno para ter essas 'intervencoes' e e por um motivo."*

Entao a `Intervenção` e' EXTRA e de graca, e quem se move e' a linha de dano.
A conta acha o fator novo que devolve o total calibrado.
"""
import os, re, sys, math

REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')

P26 = 'sistema/03-mecanica/26-bestiario.md'
TABELA = '04-fase-1/TABELA.md'
ESCADA = '04-fase-1/a-escada-com-numero.md'
N_INT = 3


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


# ===========================================================================
linha('AS ANCORAS')
# ===========================================================================
ALVO = n(pega(P26, r'ele derruba `([\d,]+)` pessoas se concentrar', 'o alvo').group(1))
POR_ATACANTE = n(pega(P26, r'um atacante que para de bater abre mão de `([\d,]+)`',
                      'o dano por atacante').group(1))
mb = pega(ESCADA, r'A banda inteira é de `(\d+)%` a `(\d+)%`', 'a banda', BEST)
# a banda ja foi movida pelo `Controlador`, em 10/09
PISO, TETO = 0.20, n(mb.group(2)) / 100

# a escada: categoria -> (pessoas, acoes) e a linha nv30
CATS = {}
atual = None
for ln in ler(TABELA, BEST).split('\n'):
    m = re.match(r'## `([^`]+)`', ln)
    if m:
        atual = m.group(1)
        continue
    m = re.match(r'\| 30 \| `(\d+)` \| `(\d+)` \| `(\d+)` \|', ln)
    if m and atual:
        CATS[atual] = dict(vida=n(m.group(1)), dano=n(m.group(2)), acoes=n(m.group(3)))

# quantas pessoas cada uma pede, e quantas rodadas ela dura contra ELAS
PEDE = {'Ameaça': 1, 'Desastre': 4, 'Catástrofe': 6, 'Calamidade': 8}
DUR = {}
for cat, pes in PEDE.items():
    if cat not in CATS:
        print(f'  !! nao li a linha nv30 de {cat}')
        sys.exit(1)
    DUR[cat] = CATS[cat]['vida'] / (POR_ATACANTE * pes)

mf = pega(ESCADA, r'\| 30 \| `\d+%` \| `\d+%` \| `(\d+)%` \|', 'a fatia', BEST)
VIDA_PC = (CATS['Desastre']['dano'] / CATS['Desastre']['acoes']) / (n(mf.group(1)) / 100)

print(f'  alvo publicado                 derruba {ALVO:.2f} pessoas          peça 26 §4.6')
print(f'  dano de um atacante            {POR_ATACANTE:.2f} por rodada        peça 26 §4.7')
print(f'  a vida de um personagem nv30   {VIDA_PC:.0f}')
print(f'  a banda do `o golpe`           {PISO:.0%}–{TETO:.0%}            (o piso mudou em 10/09)')
print()
print(f'  {"categoria":<14}{"pede":>6}{"vida":>8}{"dano":>7}{"ações":>7}{"rodadas contra ela":>20}'
      f'{"Intervenções que disparam":>27}')
print('  ' + '-' * 90)
for cat in PEDE:
    d = CATS[cat]
    disp = min(N_INT, math.floor(DUR[cat]))
    print(f'  {cat:<14}{PEDE[cat]:>6}{d["vida"]:>8.0f}{d["dano"]:>7.0f}{d["acoes"]:>7.0f}'
          f'{DUR[cat]:>20.1f}{disp:>27}')


# ===========================================================================
linha('1. O FATOR NOVO — e ele NAO e o mesmo em todas as categorias')
# ===========================================================================
# total novo = dano_novo x R + I x (dano_novo / A)  =  dano_velho x R
#  ->  fator = R / (R + I/A)
print('  Com a Intervenção de graça e por cima, o total da luta vira')
print('    dano × rodadas  +  Intervenções × uma ação')
print('  e "uma ação" é `dano ÷ ações`. Igualando ao total calibrado de hoje:')
print()
print('    fator = R ÷ (R + I/A)')
print()
print(f'  {"categoria":<14}{"R":>5}{"A":>4}{"I":>4}{"fator novo":>13}{"dano novo":>12}'
      f'{"o golpe":>10}{"fatia":>8}{"na banda?":>11}')
print('  ' + '-' * 82)
FATOR = {}
for cat in PEDE:
    d = CATS[cat]
    R, A = DUR[cat], d['acoes']
    I = min(N_INT, math.floor(R))
    fator = R / (R + I / A)
    FATOR[cat] = fator
    dano_novo = d['dano'] * fator
    golpe = dano_novo / A
    fr = golpe / VIDA_PC
    print(f'  {cat:<14}{R:>5.1f}{A:>4.0f}{I:>4}{fator:>13.3f}{dano_novo:>12.1f}'
          f'{golpe:>10.1f}{fr:>7.0%}{("sim" if PISO <= fr <= TETO else "NÃO"):>11}')
print()
print('  ⚠ O fator NAO e uniforme, e o motivo e' + ' honesto: uma Intervencao pesa 1/3 da rodada')
print('     de um `Desastre` (3 ações) e 1/6 da rodada de uma `Calamidade` (6 ações).')
print('     Quanto mais acoes a categoria tem, MENOS a Intervencao muda ela.')
print()
print('  ⚠⚠ E A `Ameaça` SAI DA BANDA: fator 0,600, `o golpe` em 14% contra um piso de 20%.')
print('     Ela tem UMA acao, entao uma Intervencao DOBRA a rodada dela.')
print()
print('  >> E o Draw Steel ja resolveu isso, e a frase e literal:')
print('     "Villain actions ... are built-in abilities for LEADER AND SOLO creatures."')
print('     >> So os postos GRANDES tem. Minion, Horde, Platoon e Elite NAO tem.')
print()
print('  Entao: `Intervenção` a partir do `Desastre`. `Capanga` e `Ameaça` nao tem.')
print()
print(f'  {"categoria":<14}{"tem Intervenção?":>18}{"fator":>9}{"dano novo":>12}{"o golpe":>10}'
      f'{"fatia":>8}{"na banda?":>11}')
print('  ' + '-' * 82)
COM_INT = {'Ameaça': False, 'Desastre': True, 'Catástrofe': True, 'Calamidade': True}
for cat in PEDE:
    d = CATS[cat]
    if not COM_INT[cat]:
        golpe = d['dano'] / d['acoes']
        fr = golpe / VIDA_PC
        FATOR[cat] = 1.0
        print(f'  {cat:<14}{"não":>18}{1.0:>9.3f}{d["dano"]:>12.1f}{golpe:>10.1f}{fr:>7.0%}'
              f'{("sim" if PISO <= fr <= TETO else "NÃO"):>11}')
        continue
    R, A = DUR[cat], d['acoes']
    I = min(N_INT, math.floor(R))
    fator = R / (R + I / A)
    FATOR[cat] = fator
    dano_novo = d['dano'] * fator
    golpe = dano_novo / A
    fr = golpe / VIDA_PC
    print(f'  {cat:<14}{"sim":>18}{fator:>9.3f}{dano_novo:>12.1f}{golpe:>10.1f}{fr:>7.0%}'
          f'{("sim" if PISO <= fr <= TETO else "NÃO"):>11}')
print()
print('  >> As quatro cabem na banda. E o corte segue o campo, nao a conveniencia.')


# ===========================================================================
linha('2. E SE A INTERVENCAO TIVER TAMANHO FIXO — o fator volta a ser um so')
# ===========================================================================
print('  A alternativa: a Intervenção não vale "uma ação dele", e sim uma FRAÇÃO FIXA da')
print('  rodada — igual pra toda categoria. Aí o fator é único e a escada fica limpa.')
print()
print(f'  {"a Intervenção vale":<26}{"fator":>9}{"Desastre: dano":>16}{"o golpe":>10}{"fatia":>8}'
      f'{"na banda?":>11}')
print('  ' + '-' * 80)
for rot, frac in (('1/3 da rodada', 1 / 3), ('1/4 da rodada', 0.25), ('1/2 da rodada', 0.5)):
    d = CATS['Desastre']
    R = DUR['Desastre']
    I = min(N_INT, math.floor(R))
    fator = R / (R + I * frac)
    dano_novo = d['dano'] * fator
    golpe = dano_novo / d['acoes']
    fr = golpe / VIDA_PC
    print(f'  {rot:<26}{fator:>9.3f}{dano_novo:>16.1f}{golpe:>10.1f}{fr:>7.0%}'
          f'{("sim" if PISO <= fr <= TETO else "NÃO"):>11}')
print()
print('  >> Com fracao fixa, TODA categoria usa o mesmo fator, e o `o golpe` de cada uma')
print('     cai na mesma proporcao. A escada continua sendo uma escada.')


# ===========================================================================
linha('3. A CONFERENCIA — a metrica de derrubadas volta pro alvo?')
# ===========================================================================
print(f'  O teste: com o fator novo E as Intervencoes disparando, quantas pessoas ele derruba')
print(f'  numa luta contra a mesa que ele pede? O alvo publicado e {ALVO:.2f}.')
print()
print(f'  {"categoria":<14}{"total da luta":>15}{"pessoas derrubadas":>21}{"vs o alvo":>12}')
print('  ' + '-' * 64)
for cat in PEDE:
    d = CATS[cat]
    R, A = DUR[cat], d['acoes']
    I = min(N_INT, math.floor(R)) if COM_INT[cat] else 0
    dano_novo = d['dano'] * FATOR[cat]
    total = dano_novo * R + I * (dano_novo / A)
    derruba = total / VIDA_PC
    velho = d['dano'] * R / VIDA_PC
    print(f'  {cat:<14}{total:>15.0f}{derruba:>21.2f}{derruba / velho:>11.2f}x')
print()
print('  >> Por construcao, o total volta ao de hoje — entao a metrica de derrubadas')
print('     volta EXATAMENTE pro numero que a peca 26 §4.6 publica e que foi validado')
print('     contra o d20 de 2014 e o PF2e.')


# ===========================================================================
linha('4. E O QUE MUDA NA MESA — que e o ponto da correcao do Mizuki')
# ===========================================================================
d = CATS['Desastre']
R, A = DUR['Desastre'], d['acoes']
dano_novo = d['dano'] * FATOR['Desastre']
print('  O total é o mesmo. O que muda é a FORMA dele na mesa:')
print()
print(f'  {"rodada":<28}{"hoje":>18}{"recalibrado":>18}{"diferença":>14}')
print('  ' + '-' * 78)
print(f'  {"rodada SEM Intervenção":<28}{d["dano"]:>18.0f}{dano_novo:>18.0f}'
      f'{dano_novo - d["dano"]:>+14.0f}')
print(f'  {"rodada COM Intervenção":<28}{d["dano"]:>18.0f}'
      f'{dano_novo + dano_novo / A:>18.0f}{dano_novo + dano_novo / A - d["dano"]:>+14.0f}')
print()
pico = (dano_novo + dano_novo / A) / dano_novo
print(f'  >> A rodada com Intervenção entrega {pico:.2f}x a rodada sem.')
print(f'  >> Hoje ela entrega 1,00x — porque hoje nao existe diferenca nenhuma entre as duas.')
print()
print(f'  ⚠⚠ E E ISSO QUE A CORRECAO DO MIZUKI COMPRA: hoje o chefe bate igual em toda rodada.')
print(f'     Recalibrado, ele bate {1 - FATOR["Desastre"]:.0%} MENOS no basico e {pico - 1:.0%} A MAIS')
print(f'     na rodada em que ele puxa a jogada. O total nao mudou — a FORMA mudou.')
print(f'     "elas transformarem o combate em algo mais letal mesmo" e' + ' exatamente isso.')
