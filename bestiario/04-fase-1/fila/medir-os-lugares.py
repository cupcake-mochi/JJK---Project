#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OS LUGARES — a medicao que abre o catalogo `04`.

O catalogo `04-os-lugares.md` pergunta "o que faz um lugar produzir maldicao".
Antes de pesquisar fora, a regra do projeto manda conferir o que ja esta em casa
— e desta vez o que estava em casa respondeu tres perguntas de uma vez.

Este script roda quatro contas, nenhuma com numero digitado a mao:

  §1  o campo DA ficha pro lugar?          — Draw Steel, `Dynamic Terrain`
  §2  o lugar CUSTA encontro?              — o campo `EV` das mesmas fichas
  §3  o lugar tem saida SEM luta?          — o bloco `Deactivate`
  §0b CANARIO — o `environments` do SRD    — o campo existe e vem VAZIO na coleta

E um quinto, que e do repositorio e nao do campo:

  §4  o nome da coisa no nosso sistema     — `Cortina` (peca 11) contra `veu`

⚠ §0b e canario, na familia do §0b do `medir-resistencia-imunidade.py`:
   `environments` e chave declarada nos `331` blocos do SRD 2024 e vem vazia em
   `331` deles. Isso e falha de COLETA, nao ausencia de mecanica — do mesmo jeito
   que a `Vulnerabilities Fire` da Mumia. NAO publique "o D&D nao classifica
   monstro por ambiente" a partir daqui.

Nenhum numero mora aqui dentro: cada ancora e lida do documento dono, e o script
morre se o dono mudar.
"""
import json
import os
import re
import sys

BEST = os.environ.get('JJK_BEST', '/media/mizuki/HD Externo II/Claude/Claude 2/bestiario')
REPO = os.environ.get('JJK_REPO', '/media/mizuki/HD Externo II/Claude/Claude 2')

DS = '04-fase-1/fila/dados-recarga-area/data-md-main/Bestiary/Monsters/Dynamic Terrain'
SRD24 = '04-fase-1/fila/srd-2024.json'
SRD14 = '04-fase-1/fila/srd-2014.json'

# donos no repositorio (LEITURA — este projeto nao escreve no Claude 2)
P11 = 'sistema/03-mecanica/11-aptidoes-e-refino.md'   # a `Cortina` e a `Barreira Simples`
P12 = 'sistema/03-mecanica/12-experiencia-e-progressao.md'  # "o sistema nao tem Veu"
P13 = 'sistema/03-mecanica/13-legados.md'             # "enganado por barreira, veu e ferramenta"

# donos no Bestiario
CAT01 = '07-catalogo/01-o-que-e-uma-maldicao.md'      # o §4 se chama "O veu"

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


# ---------------------------------------------------------------- §0b CANARIO
def canario_environments():
    print('\n§0b · CANARIO — o campo `environments` do SRD')
    print('     (mesma familia do canario da vulnerabilidade: campo declarado, coleta vazia)')
    for rotulo, rel in (('SRD 2024', SRD24), ('SRD 2014', SRD14)):
        caminho = os.path.join(BEST, rel)
        if not os.path.exists(caminho):
            morre(f'{rotulo}: {rel} sumiu')
            continue
        with open(caminho, encoding='utf-8') as f:
            blocos = json.load(f)
        tem_chave = sum(1 for m in blocos if 'environments' in m)
        preenchido = sum(1 for m in blocos if m.get('environments'))
        print(f'  {rotulo}: {len(blocos)} blocos · chave presente em {tem_chave} · '
              f'PREENCHIDA em {preenchido}')
        if tem_chave and not preenchido:
            print('    ⚠ chave declarada e vazia em 100% — e COLETA, nao ausencia.')
            print('    ⚠ toda contagem de ambiente no SRD deste projeto e PISO, nao valor.')
        elif preenchido:
            print('    🆕 a coleta MUDOU — o campo passou a vir preenchido. Refaca a leitura.')


# ------------------------------------------------------- §1·§2·§3 DRAW STEEL
def draw_steel_terreno():
    print('\n§1·§2·§3 · DRAW STEEL — o campo da ficha pro LUGAR?')
    raiz = os.path.join(BEST, DS)
    if not os.path.isdir(raiz):
        morre(f'a pasta `Dynamic Terrain` sumiu: {DS}')
        return

    familias = {}
    for dirpath, _dirnames, filenames in os.walk(raiz):
        for nome in sorted(filenames):
            if not nome.endswith('.md') or nome.startswith('_'):
                continue
            fam = os.path.basename(dirpath)
            familias.setdefault(fam, []).append(os.path.join(dirpath, nome))

    if not familias:
        morre('a pasta existe e nao tem ficha nenhuma dentro')
        return

    total = sum(len(v) for v in familias.values())
    com_ev = com_stamina = com_desativar = com_upgrade = com_ativar = 0
    evs = []

    for fam in sorted(familias):
        for caminho in familias[fam]:
            with open(caminho, encoding='utf-8') as f:
                txt = f.read()
            if re.search(r'\*\*EV:\*\*', txt):
                com_ev += 1
                m = re.search(r'\*\*EV:\*\*\s*(\d+)', txt)
                if m:
                    evs.append(int(m.group(1)))
            if re.search(r'\*\*Stamina:\*\*', txt):
                com_stamina += 1
            if re.search(r'\*\*Deactivate\*\*', txt):
                com_desativar += 1
            if re.search(r'\*\*Activate\*\*', txt):
                com_ativar += 1
            if re.search(r'\*\*Upgrade\*\*', txt):
                com_upgrade += 1

    print(f'  {total} fichas de terreno, em {len(familias)} familias:')
    for fam in sorted(familias):
        print(f'    {len(familias[fam]):3d}  {fam}')

    def pct(n):
        return f'{n} de {total} — {100.0 * n / total:.1f}%'

    print(f'\n  §1 tem ficha?          `Stamina`: {pct(com_stamina)}')
    print(f'  §2 custa encontro?     `EV`:      {pct(com_ev)}')
    if evs:
        evs.sort()
        meio = evs[len(evs) // 2] if len(evs) % 2 else (evs[len(evs) // 2 - 1] + evs[len(evs) // 2]) / 2
        print(f'     EV lido em {len(evs)}: min {min(evs)} · mediana {meio} · max {max(evs)}')
    print(f'  §3 tem saida sem luta? `Deactivate`: {pct(com_desativar)}')
    print(f'     e o gatilho:        `Activate`:   {pct(com_ativar)}')
    print(f'     e cresce por preco: `Upgrade`:    {pct(com_upgrade)}')

    if com_desativar == total:
        print('\n  ⟹ TODA ficha de lugar do Draw Steel traz como DESLIGAR ela.')
        print('    E o modelo `Volo\'s` em forma de statblock: o lugar tem saida que nao e dano.')


# ------------------------------------------------------------ §4 O NOSSO NOME
def o_nome_no_repositorio():
    print('\n§4 · O REPOSITORIO — como a coisa se chama do nosso lado')
    p11 = ler(REPO, P11)
    p12 = ler(REPO, P12)
    p13 = ler(REPO, P13)
    cat = ler(BEST, CAT01)

    cortina = len(re.findall(r'Cortina', p11))
    barreira = len(re.findall(r'Barreira Simples', p11))
    print(f'  peca 11: `Cortina` {cortina}× · `Barreira Simples` {barreira}×')
    if not cortina or not barreira:
        morre('a peca 11 deixou de citar `Cortina`/`Barreira Simples` — o dono mudou')

    # a frase da peca 12 que declara a ausencia
    m = re.search(r'o sistema n[ãa]o tem V[ée]u', p12)
    print(f'  peca 12: a frase "o sistema nao tem Veu" — {"ACHADA" if m else "SUMIU"}')
    if not m:
        morre('a peca 12 nao diz mais "o sistema nao tem Veu" — reconferir o §4 do catalogo 01')

    veu13 = len(re.findall(r'v[ée]u', p13, re.I))
    print(f'  peca 13: a palavra `veu` aparece {veu13}× (na lista "barreira, veu e ferramenta")')

    veu_cat = len(re.findall(r'v[ée]u', cat, re.I))
    print(f'  catalogo 01: a palavra `veu` aparece {veu_cat}× — o §4 se chama "O veu"')

    if m and veu13 and veu_cat:
        print('\n  ⚠ AS TRES CONVIVEM, e nao e contradicao — sao tres coisas:')
        print('    · a peca 11 tem a APTIDAO (`Cortina`), com regra, preco e relogio')
        print('    · a peca 13 usa `veu` como PALAVRA de ficcao, numa lista de coisas que enganam')
        print('    · a peca 12 nega o VEU-MASQUERADE (o "vazou/nao vazou" do mundo), e so ele')
        print('    ⟹ o catalogo `04` tem de usar `Cortina` quando aponta REGRA,')
        print('      e pode usar `veu` como palavra — nunca como mecanica com dono.')


# --------------------------------------------------- §5 QUEM ERGUE A CORTINA
def quem_ergue_a_cortina():
    """
    O catalogo `01` §4 publica, como PADRAO, que "o veu e como o servico costuma
    comecar". A peca 11 §6.6 diz em que NIVEL a `Cortina` entra na ficha — e as
    duas coisas nao batem do jeito que a leitura ingenua supoe.
    """
    print('\n§5 · QUEM ERGUE A CORTINA — o gate de nivel da peca 11 §6.6')
    p11 = ler(REPO, P11)

    # a linha da tabela de rotas, na secao da `Cortina`
    m = re.search(
        r'\|\s*sempre Refino\s*\|\s*n[íi]vel\s*(\d+)\s*\|\s*\*\*n[íi]vel\s*(\d+)\*\*\s*\|', p11)
    m2 = re.search(
        r'\|\s*meio a meio\s*\|\s*n[íi]vel\s*(\d+)\s*\|\s*\*\*n[íi]vel\s*(\d+)\*\*\s*\|', p11)
    m3 = re.search(
        r'\|\s*sempre Corpo · sempre Leque\s*\|\s*(\w+)\s*\|\s*\*\*(\w+)\*\*\s*\|', p11)

    if not (m and m2 and m3):
        morre('a tabela de rotas da `Cortina` mudou de forma na peca 11 §6.6')
        return

    bar_ref, cor_ref = int(m.group(1)), int(m.group(2))
    bar_mei, cor_mei = int(m2.group(1)), int(m2.group(2))
    bar_out, cor_out = m3.group(1), m3.group(2)

    print(f'  `Barreira Simples` abre: sempre Refino nv{bar_ref} · meio a meio nv{bar_mei} '
          f'· Corpo/Leque {bar_out}')
    print(f'  `Cortina`          abre: sempre Refino nv{cor_ref} · meio a meio nv{cor_mei} '
          f'· Corpo/Leque {cor_out}')

    # o que a Cortina cobre, na propria peca
    cobre = re.search(r'Ela cobre \*\*um lugar\*\* — ([^\n]+?)—', p11)
    if cobre:
        print(f'  e ela cobre: {cobre.group(1).strip()}')
    else:
        morre('a peca 11 nao descreve mais o que a `Cortina` cobre')

    # o tamanho declarado sem metro
    sem_metro = re.search(r'O tamanho dela n[ãa]o tem metro', p11)
    print(f'  o tamanho dela nao tem metro — {"DECLARADO" if sem_metro else "SUMIU"}')
    if not sem_metro:
        morre('a peca 11 perdeu a declaracao "o tamanho dela nao tem metro"')

    print(f'\n  ⟹ A `Cortina` e aptidao de **nv{cor_ref} no melhor caso** e **nv{cor_mei} na rota '
          f'meio a meio`,')
    print(f'    e DUAS rotas ({bar_out}) nao chegam nela em nivel nenhum.')
    print('    ⚠ Entao "o veu sobe" NAO e coisa que o grupo faz — na maior parte da campanha')
    print('      quem ergue e o apoio, e isso e PADRAO de ficcao, nao regra nova.')
    print('    ⚠ E o catalogo `01` §4 escreve o veu como abertura do servico sem dizer isso.')


# -------------------------------------------- §6 O PRECO DO COVIL NO D&D 2024
def o_preco_do_covil():
    """
    O agente `B` leu num site de terceiro que a `Lair Action` saiu no MM 2024 e
    que o bicho passou a ganhar uso extra de `Legendary Resistance` em casa.
    Isso e achado LIDO. Este § transforma a metade que da pra medir em MEDIDO:
    o proprio SRD esta em disco, e o bonus mora no NOME do traco.

    ⚠ O que este § NAO prova: que a `Lair Action` foi removida. Os dois jsons nao
    tem campo de acao de covil nenhum — nem vazio, NAO EXISTE. Isso e limite de
    coleta (§0b), entao a remocao continua sendo achado LIDO.
    """
    print('\n§6 · O PRECO DO COVIL — o `Legendary Resistance` em casa')
    linhas = {}
    for rotulo, rel in (('SRD 2024', SRD24), ('SRD 2014', SRD14)):
        caminho = os.path.join(BEST, rel)
        if not os.path.exists(caminho):
            morre(f'{rotulo}: {rel} sumiu')
            return
        with open(caminho, encoding='utf-8') as f:
            blocos = json.load(f)

        com_lr, com_extra, pares = set(), set(), set()
        for m in blocos:
            for t in (m.get('traits') or []) + (m.get('actions') or []):
                nome = t.get('name') or ''
                if 'Legendary Resistance' not in nome:
                    continue
                com_lr.add(m['name'])
                mm = re.search(r'\((\d+)/Day(?:, or (\d+)/Day in Lair)?\)', nome)
                if mm and mm.group(2):
                    com_extra.add(m['name'])
                    pares.add((int(mm.group(1)), int(mm.group(2))))
        linhas[rotulo] = (len(blocos), com_lr, com_extra, pares)
        print(f'  {rotulo}: {len(blocos)} blocos · com `Legendary Resistance` {len(com_lr)} '
              f'· ganham uso EXTRA em covil {len(com_extra)}')
        if pares:
            deltas = sorted({b - a for a, b in pares})
            print(f'    fora → dentro: {sorted(pares)} · o extra e sempre +{deltas} uso')

    n24, _lr24, ex24, par24 = linhas['SRD 2024']
    _n14, _lr14, ex14, _p14 = linhas['SRD 2014']

    if not ex24:
        morre('o SRD 2024 nao tem mais `Legendary Resistance ... in Lair` — a coleta ou o '
              'campo mudou')
        return
    if ex14:
        morre('o SRD 2014 passou a ter uso extra em covil — a leitura de experimento natural cai')
        return

    print(f'\n  ⟹ EXPERIMENTO NATURAL: `0` de {len(_lr14)} no 2014, '
          f'`{len(ex24)}` de {len(_lr24)} no 2024.')
    print('    O campo ADICIONOU preco de covil entre as edicoes — e pos ele DENTRO do bloco')
    print('    do bicho, como UM uso a mais, em vez de dar ficha propria ao lugar.')
    print('    ⚠ Isto e o CONTRARIO do desenho do Draw Steel (§1), e os dois sao de 2024-25.')


def main():
    print('=' * 74)
    print('OS LUGARES — a medicao que abre o catalogo 04')
    print('=' * 74)
    canario_environments()
    draw_steel_terreno()
    o_nome_no_repositorio()
    quem_ergue_a_cortina()
    o_preco_do_covil()
    print('\n' + '=' * 74)
    if falhas:
        print(f'✗ {len(falhas)} ancora(s) perdida(s). O documento dono mudou — releia antes de usar.')
        for f in falhas:
            print(f'   · {f}')
        sys.exit(1)
    print('✓ todas as ancoras de pe.')


if __name__ == '__main__':
    main()
