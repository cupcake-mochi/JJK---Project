#!/usr/bin/env python3
"""Confere a peca 27 — Ritual.

O que ele NAO faz: adivinhar se uma Melhoria de ritual anula uma Restricao.
Isso e' semantica e script nenhum resolve. A checagem 5 pega o erro de
OMISSAO — a Melhoria que nao declarou nada —, que foi o erro real: as duas
travas que existem hoje so apareceram quando alguem foi obrigado a passar
as dezesseis pelas dezoito Restricoes, uma a uma.

Nenhum valor mora aqui: a escada sai da peca, o Teto e os pontos saem do
partA.js do manual, e as Restricoes saem do partD.js.

Roda sem argumento. Sai com codigo 1 se algo quebrar.
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))
PECA = os.path.join(AQUI, '27-ritual.md')
PARTA = os.path.join(RAIZ, 'manual', 'gerador', 'partA.js')
PARTD = os.path.join(RAIZ, 'manual', 'gerador', 'partD.js')
LIVRO = os.path.join(RAIZ, 'sistema', '05-material', 'livro', 'manual', '46-ritual.md')

FALHAS = []
def erro(m):
    FALHAS.append(m); print(f'  !! {m}')
def ok(m):
    print(f'  [x] {m}')
def bloco(t):
    print(); print('=' * 88); print(t); print('=' * 88)

txt = open(PECA, encoding='utf-8').read()
parta = open(PARTA, encoding='utf-8').read()
partd = open(PARTD, encoding='utf-8').read()
livro = open(LIVRO, encoding='utf-8').read() if os.path.isfile(LIVRO) else ''

print(f'Peca lida: {len(txt.splitlines())} linhas. Livro: {len(livro.splitlines())} linhas.')

# ---------------------------------------------------------------- 1
bloco('1. A ESCADA DE TEMPO — tres degraus, e os pontos crescem')
esc = re.findall(r'\|\s*\*\*(Ação Padrão|Ação Completa|`Recitação Prolongada`)\*\*\s*\|[^|]*\|\s*\*\*(\d+)\*\*\s*\|', txt)
if len(esc) != 3:
    erro(f'1: li {len(esc)} degrau(s) na escada de tempo e esperava 3')
else:
    pts = [int(p) for _, p in esc]
    print(f'  a escada publicada: {" · ".join(str(p) for p in pts)} pontos')
    if pts != sorted(pts) or len(set(pts)) != 3:
        erro(f'1: a escada {pts} nao cresce. Mais tempo tem de dar mais ponto, '
             'senao o degrau de cima nao existe')
    else:
        ok('os tres degraus crescem, e nenhum empata com outro')

# ---------------------------------------------------------------- 2
bloco('2. AS MELHORIAS — preco, e o mais caro cabe no maior degrau')
mel = re.findall(r'^\|\s*`(Ritual de [^`]+)`\s*\|([^|]+)\|\s*(\d+)\s*\|([^|]*)\|([^|]*)\|\s*$',
                 txt, re.M)
if not mel:
    erro('2: nao achei a tabela das Melhorias de ritual na peca')
else:
    precos = [int(p) for _, _, p, _, _ in mel]
    print(f'  {len(mel)} Melhoria(s), precos de {min(precos)} a {max(precos)} ponto(s)')
    teto = max(int(p) for _, p in esc) if len(esc) == 3 else 0
    if max(precos) > teto:
        erro(f'2: a Melhoria mais cara custa {max(precos)} e o maior degrau da {teto}: '
             'existe Melhoria que nenhum ritual alcanca')
    else:
        ok(f'a mais cara ({max(precos)}) cabe no maior degrau ({teto})')
    menor = min(int(p) for _, p in esc) if len(esc) == 3 else 0
    if min(precos) > menor:
        erro(f'2: a Melhoria mais barata custa {min(precos)} e o menor degrau da {menor}: '
             'o primeiro degrau nao compra nada')
    else:
        ok(f'a mais barata ({min(precos)}) cabe no menor degrau ({menor})')

# ---------------------------------------------------------------- 3
bloco('3. O VAO — ele tem de SER a Liberacao Maxima, derivada do manual')
mp = re.search(r"\*\*Pontos\*\* = (\d+) × Classe", parta)
mt = re.search(r"\*\*Teto de dano\*\* = (\d+) × Classe", parta)
ml = re.search(r"\*\*Liberação Máxima\*\* = \+ Classe", parta)
if not (mp and mt and ml):
    erro('3: nao li Pontos, Teto e Liberacao Maxima do partA.js')
else:
    fp, ft = int(mp.group(1)), int(mt.group(1))
    print(f'  do manual: Pontos = {fp} x Classe · Teto = {ft} x Classe · Liberacao = + Classe')
    ruins = [c for c in range(1, 8) if (ft * c - fp * c) != c]
    if ruins:
        erro(f'3: o vao (Teto - Pontos) nao e a Classe nas Classes {ruins}. '
             'A peca 27 §5 afirma que os dois sao a mesma coisa')
    else:
        ok(f'o vao e a Liberacao Maxima nas 7 Classes ({ft}x - {fp}x = 1x)')

# ---------------------------------------------------------------- 4
bloco('4. METADE DO VAO — o piso de 1 e obrigatorio, e a peca publica a linha')
lin = re.search(r'\|\s*metade do vão\s*\|([^\n]+)\|', txt)
if not lin:
    erro('4: nao achei a linha "metade do vao" na peca')
else:
    pub = [int(x) for x in re.findall(r'\d+', lin.group(1).replace('**', ''))]
    der = [max(1, c // 2) for c in range(1, 8)]
    print(f'  publicado: {pub}')
    print(f'  derivado (metade da Classe, piso 1): {der}')
    if pub != der:
        erro(f'4: a linha publicada {pub} nao bate com a derivada {der}')
    else:
        ok('a linha publicada e' + ' a metade do vao com piso de 1')
    if max(1, 1 // 2) == 1 and (1 // 2) == 0:
        ok('e o piso morde: sem ele a Classe 1 entregaria 0, e um ritual que da zero nao e ritual')

# ---------------------------------------------------------------- 5
bloco('5. A DECLARACAO DE RESTRICAO — toda Melhoria diz com quais ela nao entra')
print('  Esta e a checagem que pega erro de OMISSAO. Ela nao julga se a anulacao')
print('  e real: ela exige que alguem tenha OLHADO. As duas travas de hoje so')
print('  apareceram quando a passada completa foi obrigatoria.')
print()
_bloco_r = re.search(r"const restricoes = \[(.*?)\n\];", partd, re.S)
nomes_r = set(re.findall(r"^\s*\['([^']+)',\s*'[^']*',", _bloco_r.group(1), re.M)) if _bloco_r else set()
if not nomes_r:
    erro('5: nao li o catalogo de Restricoes do partD.js')
else:
    _fixas = sorted(n for n in nomes_r if n != 'Restrição Própria')
    print(f'  {len(_fixas)} Restricao(oes) fixas no catalogo do manual, mais a Restricao Propria —')
    print(f'  que e customizada e nao se declara antes: o conteudo dela so existe quando alguem escreve')
    sem_decl, citadas = [], []
    for nome, _, _, _, decl in mel:
        d = decl.strip()
        if not d:
            sem_decl.append(nome); continue
        if d.lower() == 'nenhuma':
            continue
        for r in re.findall(r'`([^`]+)`', d):
            citadas.append((nome, r))
    if sem_decl:
        erro(f'5: {len(sem_decl)} Melhoria(s) sem declaracao: {", ".join(sem_decl)}')
    else:
        ok(f'as {len(mel)} Melhorias declaram — inclusive as que declaram "nenhuma"')
    fantasma = [(m, r) for m, r in citadas if r not in nomes_r]
    if fantasma:
        for m, r in fantasma:
            erro(f'5: {m} trava contra `{r}`, e essa Restricao nao existe no manual')
    else:
        ok(f'as {len(citadas)} trava(s) citadas apontam para Restricao que existe')
    for m, r in citadas:
        print(f'      {m} nao entra com `{r}`')

# ---------------------------------------------------------------- 6
bloco('6. A MATRIZ FORMA x MELHORIA — as dez Formas aparecem')
formas = re.findall(r"\['(Projétil|Toque|Explosão|Aura|Cone|Linha|Cura|Apoio|Onda|Efeito)',",
                    open(os.path.join(RAIZ, 'manual', 'gerador', 'partC.js'), encoding='utf-8').read())
formas = list(dict.fromkeys(formas))
print(f'  {len(formas)} Forma(s) no manual: {", ".join(formas)}')
faltam = [f for f in formas if f not in txt]
if faltam:
    erro(f'6: a peca 27 nao nomeia {len(faltam)} Forma(s): {", ".join(faltam)}')
else:
    ok('a peca nomeia as dez Formas do manual')
if 'Efeito` NÃO ritualiza' in txt or 'Efeito** | não ritualiza' in txt or 'não ritualiza' in txt:
    ok('a peca declara qual Forma fica de fora, em vez de deixar o buraco calado')
else:
    erro('6: nenhuma Forma e declarada fora do ritual. Se todas entram, diga isso; '
         'se alguma nao entra, escreva qual e por que')

# ---------------------------------------------------------------- 7
bloco('7. A PECA E O LIVRO — as mesmas Melhorias dos dois lados')
if not livro:
    erro('7: nao achei o capitulo 46-ritual.md do livro')
else:
    no_livro = set(re.findall(r'\*\*(Ritual de [^*]+)\*\*', livro))
    na_peca = set(n for n, _, _, _, _ in mel)
    so_peca = na_peca - no_livro
    so_livro = no_livro - na_peca
    print(f'  peca: {len(na_peca)} Melhoria(s) · livro: {len(no_livro)}')
    if so_peca:
        erro(f'7: {len(so_peca)} so na peca: {", ".join(sorted(so_peca))}')
    if so_livro:
        erro(f'7: {len(so_livro)} so no livro: {", ".join(sorted(so_livro))}')
    if not so_peca and not so_livro:
        ok('as duas listas tem os mesmos nomes — a licao no 9 conferida')

print()
print('=' * 88)
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S):')
    for e in FALHAS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — a escada cresce, os precos cabem nos degraus, o vao e a')
print('    Liberacao Maxima, toda Melhoria declara Restricao, e a peca e o livro batem.')
