#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Os dois cambios que faltavam pro papel: ALCANCE e ESCONDER.

Decisao do Mizuki, 10/09/2026: *"a questao nunca e 'nao tem' e 'nao tem AINDA,
vale a pena fazer?'"*. Entao aqui eles sao CONSTRUIDOS, e cada degrau da
construcao diz de onde veio.

A disciplina: toda peca da derivacao e' ou (a) lida de um documento dono, ou
(b) uma EXTENSAO declarada de uma regra publicada, ou (c) um parametro de mesa
que nao sai de regra nenhuma — e esse ultimo aparece como FAIXA, nunca como
numero unico escondido.
"""
import os, re, sys

REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')
BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')

P01 = 'sistema/03-mecanica/01-atributos-acerto-defesa.md'
P03 = 'sistema/03-mecanica/03-economia-de-acao-e-iniciativa.md'
P14 = 'sistema/03-mecanica/14-equipamento.md'
P19 = 'sistema/03-mecanica/19-dano-e-condicoes.md'
P26 = 'sistema/03-mecanica/26-bestiario.md'
TABELA = '04-fase-1/TABELA.md'
ESCADA = '04-fase-1/a-escada-com-numero.md'


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
linha('AS ANCORAS — e cada uma diz se e REGRA, EXTENSAO ou PARAMETRO DE MESA')
# ===========================================================================

# --- (a) lidas de documento dono -------------------------------------------
DESLOC = n(pega(P14, r'põe o deslocamento padrão em `(\d+) m`', 'o deslocamento').group(1))
PP_DESVANTAGEM = n(pega(P14, r'Desvantagem vale `−(\d+)` pontos percentuais contra alvo difícil',
                        'a desvantagem em pp').group(1))
DESV_METADE = pega(P14, r'contra alvo difícil, que é \*\*metade do dano\*\*',
                   'desvantagem = metade do dano').group(0)
COLADO = pega(P14, r'Atacar com arma de projétil \*\*estando adjacente a um inimigo\*\*',
              'a regra do colado').group(0)
ALC_SEM_PRECO = pega(P14, r'alcance de arma não tem preço neste sistema', 'alcance sem preco').group(0)
ALC_POR_EXISTIR = pega(P14, r'ela custa esse ponto por existir — não por quanto',
                       'alcance por existir').group(0)
PONTO_ARMA = n(pega(P19, r'`1` ponto de arma \| `([\d,]+)`', 'o ponto de arma').group(1))
ACERTO_INI = pega(P26, r'ele acerta `(\d+)%` a `(\d+)%`', 'o acerto do inimigo')
ACERTO_BAIXO, ACERTO_ALTO = n(ACERTO_INI.group(1)) / 100, n(ACERTO_INI.group(2)) / 100
PP_VANT = n(pega(P19, r'vantagem e desvantagem \| `(\d+)` pontos percentuais',
                 'a vantagem em pp').group(1))

# a escada: quantas rodadas a luta dura, e a cota do Desastre
RODADAS = n(pega(ESCADA, r'\| `Desastre` \| `945` \| `[\d,]+` \| \*\*`([\d,]+)`\*\*',
                 'as rodadas do Desastre contra 4', BEST).group(1))
mD = pega(TABELA, r'## `Desastre`[\s\S]*?\n\| 30 \| `(\d+)` \| `(\d+)` \| `(\d+)` \|',
          'a linha do Desastre nv30', BEST)
VIDA_D, DANO_D, ACOES_D = n(mD.group(1)), n(mD.group(2)), n(mD.group(3))
UMA_ACAO = DANO_D / ACOES_D

print('  (a) LIDAS DO DONO — regra publicada')
print(f'      deslocamento padrão                {DESLOC:.0f} m                       peça 3 / 14')
print(f'      desvantagem                        −{PP_DESVANTAGEM:.0f} pp = METADE do dano     '
      f'peça 14 §5.2.1')
print(f'      vantagem                           +{PP_VANT:.0f} pp                      peça 19 §2.2')
print(f'      projétil COLADO                    desvantagem                peça 14 §5.2.1')
print(f'      1 ponto de arma                    {PONTO_ARMA:.2f} de dano por rodada   peça 19 §2.2')
print(f'      o inimigo acerta                   {ACERTO_BAIXO:.0%} a {ACERTO_ALTO:.0%}'
      f'                 peça 26 §3.1')
print(f'      a luta do Desastre contra 4        {RODADAS:.1f} rodadas               a escada')
print(f'      Desastre nv30                      vida {VIDA_D:.0f}, dano {DANO_D:.0f} em '
      f'{ACOES_D:.0f} ações')
print()
print('  E a POSIÇÃO DECLARADA do sistema sobre alcance, que é melhor que "não tem preço":')
print(f'      "{ALC_SEM_PRECO}"')
print(f'      "...ela custa esse ponto POR EXISTIR — NÃO POR QUANTO."')
print('      >> Então o câmbio certo é TAXA FIXA por ter alcance, e não preço por metro.')
print('         Isso já é decisão tomada do projeto, e ela sobrevive a esta construção.')


# ===========================================================================
linha('1. O CAMBIO DE ALCANCE — construido de duas regras publicadas')
# ===========================================================================
print('  A regra publicada preça POSIÇÃO, e ela é simétrica nos dois lados:')
print()
print(f'    o de corpo a corpo FORA do alcance   ->  não alcança: entrega ZERO')
print(f'    o de projétil COLADO                 ->  desvantagem: entrega METADE')
print()
print('  (b) A EXTENSÃO, declarada: a regra do §5.2.1 é escrita pra ARMA de projétil.')
print('      Estender ela pra técnica de inimigo à distância é o passo que esta construção')
print('      dá, e ele é explícito. Sem ele não existe câmbio nenhum.')
print()
print('  Com isso, quem luta de longe perde METADE quando está no lugar errado, e quem luta')
print('  de perto perde TUDO. A diferença entre os dois é o que o alcance vale:')
print()
print(f'    valor do alcance = f × (100% − 50%) × dano por rodada = f × 50%')
print()
print('  (c) O PARÂMETRO DE MESA: `f` é a fração dos ataques dele que acontecem fora da')
print('      zona preferida. Isso NÃO sai de regra nenhuma — é mapa. Então vai como faixa.')
print()
print(f'  {"f":<26}{"vale (dano/rodada)":>20}{"% da cota":>12}{"em vida, na luta":>20}'
      f'{"% da vida":>12}')
print('  ' + '-' * 90)
CAND = [('1/6 — meio turno de aproximação', 1 / 6),
        ('1/3 — UMA rodada de três', 1 / 3),
        ('1/2 — metade da luta', 1 / 2)]
for rot, f in CAND:
    val = f * 0.50 * DANO_D
    em_vida = val * RODADAS
    print(f'  {rot:<26}{val:>20.2f}{val / DANO_D:>11.1%}{em_vida:>20.0f}'
          f'{em_vida / VIDA_D:>11.1%}')
print()
F_PADRAO = 1 / 3
print(f'  >> O padrão defensável é `f = 1/3`, e ele sai da própria escada:')
print(f'     a luta do `Desastre` contra a mesa de quatro dura {RODADAS:.1f} rodadas, e a PRIMEIRA')
print(f'     é a rodada de aproximação. Uma de três.')
VAL_ALC = F_PADRAO * 0.50 * DANO_D
VIDA_ALC = VAL_ALC * RODADAS
print(f'  >> Então ALCANCE vale {VAL_ALC:.2f} de dano por rodada num `Desastre` nv30 —')
print(f'     {VAL_ALC / DANO_D:.1%} da cota dele, ou {VIDA_ALC:.0f} de vida '
      f'({VIDA_ALC / VIDA_D:.1%}) na luta inteira.')
print()
print(f'  ⚠ E ele é TAXA FIXA, não preço por metro — que é a decisão que a peça 14 §5.2.2 já')
print(f'     tinha tomado pro jogador. Um Artilheiro de 18 m e um de 30 m pagam o mesmo.')
print()
print(f'  E o contra-teste contra o campo: o `Artillery` do 4e paga 42% da durabilidade.')
print(f'  Este câmbio cobra {VIDA_ALC / VIDA_D:.0%}. Ainda é '
      f'{0.42 / (VIDA_ALC / VIDA_D):.1f}x mais barato que o 4e —')
print(f'  mas o câmbio de metro do deslocamento cobrava 3%, que era 14x mais barato.')
print(f'  A construção fechou {14 / (0.42 / (VIDA_ALC / VIDA_D)):.0f}x da distância.')


# ===========================================================================
linha('2. O CAMBIO DE ESCONDER — o eixo do `Emboscador`')
# ===========================================================================
print('  O `Emboscador` não pode concentrar dano: 2 ações joga `o golpe` em 45% da vida de')
print('  um personagem, que é o número que matou a `Dupla`. Então o eixo dele é VANTAGEM.')
print()
ACERTO_MED = (ACERTO_BAIXO + ACERTO_ALTO) / 2
com_vant = min(0.95, ACERTO_MED + PP_VANT / 100)
GANHO_VANT = com_vant / ACERTO_MED - 1
print(f'  o inimigo acerta {ACERTO_BAIXO:.0%} a {ACERTO_ALTO:.0%} (peça 26 §3.1), média '
      f'{ACERTO_MED:.0%}')
print(f'  vantagem dá +{PP_VANT:.0f} pp (peça 19 §2.2) -> ele passa a acertar {com_vant:.0%}')
print(f'  >> vantagem multiplica o dano daquele ataque por {com_vant / ACERTO_MED:.2f}, ou seja '
      f'+{GANHO_VANT:.0%}')
print()
print(f'  {"o que o Emboscador ganha":<40}{"vale (dano/rodada)":>20}{"% da cota":>12}'
      f'{"em vida":>12}')
print('  ' + '-' * 86)
OPC = [('vantagem no PRIMEIRO ataque da luta', GANHO_VANT * UMA_ACAO / RODADAS),
       ('vantagem em TODA a primeira rodada', GANHO_VANT * DANO_D / RODADAS),
       ('vantagem em todo ataque, a luta inteira', GANHO_VANT * DANO_D)]
for rot, val in OPC:
    print(f'  {rot:<40}{val:>20.2f}{val / DANO_D:>11.1%}{val * RODADAS:>12.0f}')
print()
print()
print('  ⚠⚠ MAS TODAS AS TRES DE CIMA TEM UM DEFEITO, E ELE TEM NOME PUBLICADO.')
print('     "The Lurker Fallacy" (alphastream.org, 2015) mede que um monstro cujo truque e')
print('     esconder-e-dar-o-golpao entrega MENOS dano total do que se ele so atacasse todo')
print('     turno: "it does more damage by not being a lurker!". Medido num Twig Blight do 4e.')
print('     E o conserto que o proprio 4e achou, em Monster Vault: Nentir Vale, e o `Joplin')
print('     the Sly`: "Attacking every round, bonuses when lurking" — ou seja, ganho TODA')
print('     rodada, e nao uma abertura so.')
print()
print('  >> Entao a forma certa nao e "na primeira rodada": e UM ATAQUE POR RODADA, sempre.')
print('     Mesmo preco total quando acoes = rodadas, mas espalhado — e o papel para de ser')
print('     um bicho que fica inutil depois do turno 1.')
print()
print(f'  {"categoria":<14}{"ações":>7}{"vantagem em 1 ataque/rodada":>30}{"multiplica o dano":>20}')
print('  ' + '-' * 72)
mcats = re.findall(r'## `(\w+)`[\s\S]*?\n\| 30 \| `(\d+)` \| `(\d+)` \| `(\d+)` \|', ler(TABELA, BEST))
MULT_EMB = {}
for cat, vd, dn, acs in mcats:
    acs = float(acs)
    ganho = GANHO_VANT / acs
    MULT_EMB[cat] = 1 + ganho
    print(f'  {cat:<14}{acs:>7.0f}{f"+{GANHO_VANT:.0%} em 1 de {acs:.0f}":>30}{1 + ganho:>19.3f}x')
print()
print('  ⚠ O ganho ENCOLHE nas categorias grandes, porque 1 ataque de 6 e menos que 1 de 3.')
print('     Entao o PAGAMENTO encolhe junto, e a tabela do papel passa a ter uma linha por')
print('     categoria em vez de um numero unico. Isso e custo de bookkeeping, e e real.')
print()
print(f'  >> A opção do meio — vantagem na primeira rodada inteira — vale '
      f'{GANHO_VANT * DANO_D / RODADAS:.2f} por rodada,')
print(f'     que é {GANHO_VANT * DANO_D / RODADAS / DANO_D:.0%} da cota. Em vida: '
      f'{GANHO_VANT * DANO_D:.0f} ({GANHO_VANT * DANO_D / VIDA_D:.0%} da vida dele).')
print(f'  >> A de cima — vantagem a luta inteira — vale {GANHO_VANT:.0%} da cota dele, que é')
print(f'     caro demais pra um papel de graça: seria {GANHO_VANT * DANO_D * RODADAS / VIDA_D:.0%}')
print(f'     da vida dele, e ele só tem 100%.')


# ===========================================================================
linha('3. A TABELA DE CAMBIO — tudo como MULTIPLICADOR sobre o invariante')
# ===========================================================================
# ⚠ A moeda NAO pode ser "dano por rodada" solto: vida e' estoque e dano e' fluxo,
# e somar os dois esconde a nao-linearidade da Defesa (1/x e' convexo, entao +1 e
# -1 de Defesa NAO valem o mesmo).
#
# A forma que fecha e' a do invariante do §2 da MEDIDA:
#
#     o que o encontro custa  ∝  vida EFETIVA x dano
#     e  vida efetiva = vida crua ÷ chance de o PC acertar
#
# Entao todo eixo entra como MULTIPLICADOR sobre esse produto, e um papel e' neutro
# quando o produto dos multiplicadores dele da 1,00.
ACERTO_PC = n(pega(P01, r'Contra o alvo difícil, em que se acerta (\d+)%',
                   'o acerto do PC').group(1)) / 100
mdef = pega(TABELA, r'## `Desastre`[\s\S]*?\n\| 30 \|(?: `[^`]+` \|){4} `(\d+)` \|',
            'a Defesa do Desastre nv30', BEST)
DEF_D = n(mdef.group(1))
PP_DEF = 1 / 20.0    # 1 ponto de Defesa num d20

print(f'  o invariante:  vida EFETIVA × dano,  com  vida efetiva = vida ÷ acerto do PC')
print(f'  o `Desastre` nv30: Defesa {DEF_D:.0f}, o PC acerta {ACERTO_PC:.0%}, '
      f'vida efetiva {VIDA_D / ACERTO_PC:.0f}')
print(f'  um papel e NEUTRO quando o produto dos multiplicadores dele da 1,00.')
print()


def mult_defesa(d):
    """quanto a vida EFETIVA se multiplica ao mover a Defesa em `d` pontos"""
    ac = min(0.95, max(0.05, ACERTO_PC - d * PP_DEF))
    return (VIDA_D / ac) / (VIDA_D / ACERTO_PC)


EIXOS = [
    ('Defesa  +1', mult_defesa(+1), 'vida efetiva', 'derivado — 5 pp num d20, peça 1 §5.2'),
    ('Defesa  +2', mult_defesa(+2), 'vida efetiva', 'derivado — idem'),
    ('Defesa  −1', mult_defesa(-1), 'vida efetiva', 'derivado — idem'),
    ('Defesa  −2', mult_defesa(-2), 'vida efetiva', 'derivado — idem'),
    ('vida crua  ×1,10', 1.10, 'vida efetiva', 'a própria célula'),
    ('vida crua  ×1,20', 1.20, 'vida efetiva', 'a própria célula'),
    ('vida crua  ×0,80', 0.80, 'vida efetiva', 'a própria célula'),
    ('1 ação a menos (de 3)', (ACOES_D - 1) / ACOES_D, 'dano', 'derivado — a escada'),
    ('ALCANCE (taxa fixa, f=1/3)', 1 + F_PADRAO * 0.50, 'dano',
     '🔨 CONSTRUÍDO — peça 14 §5.2.1 + extensão'),
    ('vantagem na 1ª rodada', 1 + GANHO_VANT / RODADAS, 'dano',
     '🔨 CONSTRUÍDO — peça 19 §2.2 + peça 26 §3.1'),
    ('vantagem a luta inteira', 1 + GANHO_VANT, 'dano', '🔨 CONSTRUÍDO — idem'),
]
print(f'  {"eixo":<28}{"multiplica":>12}{"em que":>15}   de onde vem')
print('  ' + '-' * 92)
for rot, mlt, onde, fonte in EIXOS:
    print(f'  {rot:<28}{mlt:>11.3f}x{onde:>15}   {fonte}')
print()
print('  ⚠ E a NAO-LINEARIDADE aparece aqui, e ela importa:')
print(f'     `Defesa +1` multiplica a vida efetiva por {mult_defesa(1):.3f}, e `Defesa −1` por '
      f'{mult_defesa(-1):.3f}.')
print(f'     {mult_defesa(1):.3f} x {mult_defesa(-1):.3f} = {mult_defesa(1) * mult_defesa(-1):.3f} — '
      f'NAO da 1,00.')
print(f'     Entao +1 e −1 de Defesa NAO sao o mesmo degrau, e um papel que troca Defesa')
print(f'     tem de usar o multiplicador do lado em que ele esta indo.')
print()

print('  OS SEIS PAPEIS, montados pra fechar em 1,00:')
print()
MONTAGEM = [
    ('Brutamontes', [('Defesa −2', mult_defesa(-2)), ('vida crua ×1,20', 1.20)]),
    ('Guardião', [('Defesa +2', mult_defesa(+2)), ('vida crua ×0,80', 0.80)]),
    ('Artilheiro', [('alcance (f=1/3)', 1 + F_PADRAO * 0.50), ('vida crua ×0,857', 1 / (1 + F_PADRAO * 0.50))]),
    ('Emboscador', [('vantagem na 1ª rodada', 1 + GANHO_VANT / RODADAS),
                    ('vida crua ×0,863', 1 / (1 + GANHO_VANT / RODADAS))]),
    ('Controlador', [('1 ação a menos', (ACOES_D - 1) / ACOES_D),
                     ('vida crua ×1,50', ACOES_D / (ACOES_D - 1))]),
]
for nome, pecas in MONTAGEM:
    prod = 1.0
    for _, m in pecas:
        prod *= m
    sinal = 'NEUTRO' if abs(prod - 1.0) < 0.005 else f'⚠ {prod:.3f}x'
    print(f'  {nome:<13}' + '   ·   '.join(f'{r} ({m:.3f}x)' for r, m in pecas))
    print(f'  {"":<13}produto = {prod:.3f}  ->  {sinal}')
print()
print('  >> O `Controlador` fecha trocando 1 ação por vida — mas o que ele QUER é efeito, e a')
print('     peça 19 §2.2 já preça efeito em ações negadas. Então ele troca 1 ação dele por')
print('     1 ação negada do grupo, e isso é 1 pra 1 sem conta nova.')
print('  >> O `Apoio` é o mesmo 1 pra 1, com o destino em outro bloco.')
print()
print(f'  ⚠ E A TRAVA QUE SOBRA: o `Artilheiro` e o `Emboscador` pagam em VIDA, nao em dano —')
print(f'     de proposito. Pagar em dano seria SUBIR o dano de outro, e a banda do `o golpe`')
print(f'     so da 1,07x de espaco num `Desastre`. Pagar em vida nao encosta na banda.')


# ===========================================================================
linha('4. O BLOCO PREENCHIDO — o `Desastre` nv30 com cada papel')
# ===========================================================================
# Nada aqui e' digitado a mao: cada celula sai dos multiplicadores do §3.
mfrac = pega(ESCADA, r'\| 30 \| `\d+%` \| `\d+%` \| `(\d+)%` \|', 'a fatia do Desastre nv30', BEST)
FATIA_D = n(mfrac.group(1)) / 100
VIDA_PC = (DANO_D / ACOES_D) / FATIA_D

# ⚠ A 6a coluna de cada linha e' o MULTIPLICADOR FORA DA FICHA: o ganho do `Artilheiro`
# e do `Emboscador` nao mora em celula nenhuma do bloco. Ele e' quanto do dano JA
# ESCRITO passa a chegar. Sem essa coluna o invariante da 0,857x e parece desequilibrado,
# quando na verdade a outra metade da troca esta fora da tabela.
BLOCOS = [
    #  nome            ΔDefesa  ×vida   dano                              ações        fora da ficha
    ('‹ sem papel ›', 0, 1.00, DANO_D, ACOES_D, 1.00),
    ('Brutamontes', -2, 1.20, DANO_D, ACOES_D, 1.00),
    ('Guardião', +2, 0.80, DANO_D, ACOES_D, 1.00),
    ('Artilheiro', 0, 1 / (1 + F_PADRAO * 0.50), DANO_D, ACOES_D, 1 + F_PADRAO * 0.50),
    ('Emboscador', 0, 1 / (1 + GANHO_VANT / RODADAS), DANO_D, ACOES_D, 1 + GANHO_VANT / RODADAS),
    ('Controlador', 0, ACOES_D / (ACOES_D - 1), DANO_D * (ACOES_D - 1) / ACOES_D, ACOES_D - 1, 1.00),
]
print(f'  A vida de um personagem no nv30, derivada de golpe ÷ fatia: {VIDA_PC:.0f}')
print()
print(f'  {"papel":<15}{"Defesa":>8}{"vida crua":>11}{"dano":>7}{"ações":>7}{"o golpe":>10}'
      f'{"fatia":>8}{"fora da ficha":>15}{"invariante":>12}')
print('  ' + '-' * 95)
base_inv = (VIDA_D / ACERTO_PC) * DANO_D
ok4 = True
for nome, dd, mv, dn, acs, fora in BLOCOS:
    vida = VIDA_D * mv
    ac = min(0.95, max(0.05, ACERTO_PC - dd * PP_DEF))
    golpe = dn / acs
    inv = (vida / ac) * dn * fora
    if abs(inv / base_inv - 1.0) > 0.005:
        ok4 = False
    print(f'  {nome:<15}{DEF_D + dd:>8.0f}{vida:>11.0f}{dn:>7.0f}{acs:>7.0f}{golpe:>10.0f}'
          f'{golpe / VIDA_PC:>7.0%}{fora:>14.3f}x{inv / base_inv:>11.3f}x')
print()
print(f'  >> A coluna `o golpe` NAO SE MOVE: {DANO_D / ACOES_D / VIDA_PC:.0%} em todos os seis.')
print(f'     E e isso que faz a tabela ser legal — a banda nunca entra no caminho, porque')
print(f'     NENHUM papel sobe o dano.')
if ok4:
    print(f'  >> E o invariante fica em 1,000x nos seis: o encontro nao mudou de tamanho.')
else:
    print(f'  !! o invariante NAO fecha em 1,000x em alguma linha — a montagem esta errada.')
    sys.exit(1)
print()
print(f'  ⚠⚠ E AQUI ESTA UM ACHADO DE LEGIBILIDADE, nao de balanceamento:')
print(f'     o `Artilheiro` e o `Emboscador` tem a coluna `fora da ficha` diferente de 1,00.')
print(f'     Quer dizer que o PAGAMENTO deles aparece no bloco (vida menor) e o GANHO NAO.')
print(f'     Quem le o bloco ve um `Desastre` com 810 de vida em vez de 945 e nada explicando.')
print(f'  >> E por isso que o papel TEM de estar no cabecalho — a palavra `Artilheiro` e a')
print(f'     unica coisa no bloco que diz pra onde os 135 de vida foram. Sem ela o bloco')
print(f'     parece um `Desastre` mal montado.')
print(f'  >> O `Brutamontes`, o `Guardião` e o `Controlador` nao tem esse problema: as duas')
print(f'     metades da troca deles aparecem em celula.')
