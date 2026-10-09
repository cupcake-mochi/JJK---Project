#!/usr/bin/env python3
"""Confere a peca 27 — Ritual.

O que ele NAO faz: adivinhar se uma Melhoria de ritual anula uma Restricao.
Isso e' semantica e script nenhum resolve. A checagem 5 pega o erro de
OMISSAO — a Melhoria que nao declarou nada —, que foi o erro real: as duas
travas que existem hoje so apareceram quando alguem foi obrigado a passar
as dezesseis pelas dezoito Restricoes, uma a uma.

Nenhum valor mora aqui: a escada sai da peca, e o Teto, os pontos, as Restricoes e
as Formas saem do Fundamento e do Catalogo do livro reconstruido (ate a v0.337, do
gerador do manual do Fundamento v7: partA.js, partD.js e partC.js).

Roda sem argumento. Sai com codigo 1 se algo quebrar.
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))
PECA = os.path.join(AQUI, '27-ritual.md')
sys.path.insert(0, AQUI)
import livro as _livro
LIVRO = os.path.join(RAIZ, 'sistema', '05-material', 'livro', 'manual', '46-ritual.md')

FALHAS = []
def erro(m):
    FALHAS.append(m); print(f'  !! {m}')
def ok(m):
    print(f'  [x] {m}')
def bloco(t):
    print(); print('=' * 88); print(t); print('=' * 88)

txt = open(PECA, encoding='utf-8').read()
fund = _livro.limpa(_livro.texto('fundamento'))
CAT = _livro.catalogo()
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
bloco('3. O VAO — ele tem de SER a Liberacao Maxima, derivada do Fundamento')
mp = re.search(r"Os pontos e o PE são (\d+) × Classe", fund)
# v0.346: o R41 reescreveu a frase do teto ("a soma dos dados iniciais com esses
# acréscimos não pode passar de N × Classe em d8"); o numero e' o mesmo, e a checagem
# le o numero, entao o regex ficou so' com o miolo que as duas redacoes tem.
mt = re.search(r"não pode passar de (\d+) × Classe em d8", fund)
ml = re.search(r"Uma Liberação Máxima acrescenta a Classe", fund)
if not (mp and mt and ml):
    erro('3: nao li Pontos, Teto e Liberacao Maxima do Fundamento do livro')
else:
    fp, ft = int(mp.group(1)), int(mt.group(1))
    print(f'  do livro: Pontos = {fp} x Classe · Teto = {ft} x Classe · Liberacao = + Classe')
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
nomes_r = {n for n, d in CAT.items() if d['tipo'] == 'Restrição'}
if not nomes_r:
    erro('5: nao li as Restricoes do Catalogo do livro')
else:
    _fixas = sorted(n for n in nomes_r if n != 'Restrição Própria')
    print(f'  {len(_fixas)} Restricao(oes) fixas no Catalogo do livro, mais a Restricao Propria —')
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
            erro(f'5: {m} trava contra `{r}`, e essa Restricao nao existe no Catalogo do livro')
    else:
        ok(f'as {len(citadas)} trava(s) citadas apontam para Restricao que existe')
    for m, r in citadas:
        print(f'      {m} nao entra com `{r}`')

# ---------------------------------------------------------------- 6
bloco('6. A MATRIZ FORMA x MELHORIA — as dez Formas aparecem')
formas = list(dict.fromkeys(_livro.formas()))
print(f'  {len(formas)} Forma(s) no Fundamento do livro: {", ".join(formas)}')
faltam = [f for f in formas if f not in txt]
if faltam:
    erro(f'6: a peca 27 nao nomeia {len(faltam)} Forma(s): {", ".join(faltam)}')
else:
    ok(f'a peca nomeia as {len(formas)} Formas do Fundamento')
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

# 7.1 (v0.283): o acesso fecha o ritual para quem monta a tecnica em `Manejo` ou em `Kata`.
# Decisao do Mizuki: "N da pra fazer ritual em estilo nem tecnica marcial" — "estilo" e' como
# ele chama o `Manejo`. A linha tem de estar ESCRITA dos dois lados: desde a v0.276 os capitulos
# 42 e 43 mandam ler `Kata` e `Manejo` onde qualquer capitulo escreve feitico, e sem ela o
# capitulo 46 abre o ritual para as duas rotas pela letra. Aceita a rota pelo nome da tecnica
# ou pelo nome da rota, e cobra a negacao e as duas rotas na MESMA linha. Na peca so' vale a
# caixa (`> `): o paragrafo que explica repete as palavras, e ler ele faria a checagem passar
# sem a regra — o defeito que a v0.273 achou no conferir-expansao.
def _secao(texto, rx_titulo):
    m = re.search(rx_titulo, texto, re.M)
    if not m:
        return None
    fim = re.search(r'^## ', texto[m.end():], re.M)
    return texto[m.end(): m.end() + fim.start()] if fim else texto[m.end():]

_ROTA_M = re.compile(r'`Manejo`|Sem Técnica')
_ROTA_K = re.compile(r'`Kata`|Técnica Marcial')
_NEGA = re.compile(r'não (?:compra|compram|faz ritual|fazem ritual)\b')

_s7 = _secao(txt, r'^## 7\. O acesso[ \t]*$')
_sa = _secao(livro, r'^## Acesso[ \t]*$') if livro else None
_acesso = {'peca 27, a caixa do §7': None if _s7 is None else
               '\n'.join(l for l in _s7.split('\n') if l.startswith('> ')),
           'livro, cap. 46, o Acesso': _sa}
for onde, sec in _acesso.items():
    if sec is None:
        erro(f'7.1: nao achei {onde} — a secao mudou de titulo e esta checagem parou de conferir')
        continue
    fecha = [l for l in sec.split('\n') if _NEGA.search(l) and _ROTA_M.search(l) and _ROTA_K.search(l)]
    if fecha:
        ok(f'7.1: {onde} fecha o ritual para o `Manejo` e a `Kata`')
    else:
        erro(f'7.1: {onde} nao fecha o ritual para quem monta a tecnica em `Manejo` ou em `Kata` — '
             'desde a v0.276 os capitulos 42 e 43 mandam ler as duas onde o livro escreve feitico, '
             'e sem a linha o Sem Tecnica e a Tecnica Marcial fazem ritual pela letra')

# 7.2 (v0.350): a peca 27 e o capitulo de Ritual do R41. As checagens 7 e 7.1 leem o livro
# v0.331, que esta' congelado; esta le o livro final. Ela confere os numeros que os dois lados
# publicam (escada, precos, ritual auxiliado), refaz a tabela de chance da peca pela formula —
# as 21 celulas estavam 10 pontos abaixo ate' a v0.349 —, e cobra as frases das decisoes do
# Mizuki na revisao (itens 42, 47, 50 e 51). Na peca, texto ~~riscado~~ e' historico.
print()
print('  7.2 — a peca 27 e o capitulo de Ritual do R41')
_R41 = ' '.join(_livro.texto('ritual').split())
_viva = ' '.join(re.sub(r'~~.*?~~', '', txt, flags=re.S).split())

# a) a escada
_esc_r41 = [int(p) for p in re.findall(
    r'\| (?:Breve|Completo|Recitação Prolongada) \| [^|]+\| (\d+) \|', _R41)]
_esc_peca = [int(p) for _, p in esc]
print(f'      escada no R41: {_esc_r41} · na peca: {_esc_peca}')
if len(_esc_r41) != 3:
    erro(f'7.2: li {len(_esc_r41)} modalidade(s) na tabela do R41 e esperava 3')
elif _esc_r41 != _esc_peca:
    erro(f'7.2: a escada do R41 e\' {_esc_r41} e a da peca e\' {_esc_peca}')
else:
    ok('7.2a: a escada de pontos e\' a mesma no R41 e na peca')

# b) as Melhorias: nome e preco
_mel_r41 = {n: int(p) for n, p in re.findall(r'\| (Ritual de [^|]+?) \| [^|]+\| (\d+) \|', _R41)}
_mel_peca = {n: int(p) for n, _, p, _, _ in mel}
print(f'      Melhorias no R41: {len(_mel_r41)} · na peca: {len(_mel_peca)}')
if not _mel_r41:
    erro('7.2: nao li nenhuma Melhoria de Ritual nas tabelas do R41')
else:
    _so_r41 = sorted(set(_mel_r41) - set(_mel_peca))
    _so_peca = sorted(set(_mel_peca) - set(_mel_r41))
    _preco = sorted(n for n in set(_mel_r41) & set(_mel_peca) if _mel_r41[n] != _mel_peca[n])
    if _so_r41:
        erro(f'7.2: so no R41: {", ".join(_so_r41)}')
    if _so_peca:
        erro(f'7.2: so na peca: {", ".join(_so_peca)}')
    for n in _preco:
        erro(f'7.2: {n} custa {_mel_r41[n]} no R41 e {_mel_peca[n]} na peca')
    if not (_so_r41 or _so_peca or _preco):
        ok(f'7.2b: as {len(_mel_r41)} Melhorias tem o mesmo nome e o mesmo preco dos dois lados')

# c) o ritual auxiliado: acao e pontos, dos dois lados
_aux_r41 = re.search(r'Ele dedica sua \*\*(Ação [^*]+)\*\* no próprio turno e concede '
                     r'\*\*(\d+) Pontos de Ritual\*\*', _R41)
_aux_peca = re.search(r'Cada aliado que ajuda gasta a (Ação \w+) dele e dá `(\d+)` pontos de ritual', _viva)
if not _aux_r41:
    erro('7.2: nao li no R41 a acao e os pontos do auxiliar')
elif not _aux_peca:
    erro('7.2: nao li na caixa do §6 da peca a acao e os pontos do auxiliar')
else:
    print(f'      auxiliar no R41: {_aux_r41.group(1)}, {_aux_r41.group(2)} ponto(s) · '
          f'na peca: {_aux_peca.group(1)}, {_aux_peca.group(2)} ponto(s)')
    if (_aux_r41.group(1), _aux_r41.group(2)) != (_aux_peca.group(1), _aux_peca.group(2)):
        erro('7.2: a acao ou os pontos do auxiliar divergem entre o R41 e a peca')
    else:
        ok('7.2c: o auxiliar gasta a mesma acao e da os mesmos pontos no R41 e na peca')

# d) a tabela de chance, refeita pela formula da propria peca: d20 >= 8 + Classe - Destreza.
# Igualar a CD e' sucesso, e o R41 o escreve nas Regras gerais; a testemunha e' o exemplo do
# capitulo, que da' a Classe, a Destreza, o dado e a chance.
_geral = ' '.join(_livro.texto('regras-gerais').split())
if 'Igualar ou superar a CD é sucesso' not in _geral:
    erro('7.2: o R41 nao escreve mais "Igualar ou superar a CD e\' sucesso" — a conta da '
         'tabela de chance perdeu a regra de onde sai')
_cel = re.findall(r'^\|\s*passa, com Destreza (\d+)\s*\|([^\n]+)\|\s*$', txt, re.M)
if len(_cel) != 3:
    erro(f'7.2: li {len(_cel)} linha(s) na tabela de chance do §3.1 e esperava 3')
else:
    _ruins = []
    for _d, _resto in _cel:
        _pub = [int(x) for x in re.findall(r'(\d+)%', _resto)]
        _der = [max(0, min(20, 21 - (8 + c - int(_d)))) * 5 for c in range(1, 8)]
        print(f'      Destreza {_d}: publicado {_pub} · pela formula {_der}')
        if _pub != _der:
            _ruins.append(_d)
    if _ruins:
        erro(f'7.2: a tabela de chance do §3.1 nao sai da formula nas linhas de Destreza {_ruins}')
    else:
        ok('7.2d: as 21 celulas da tabela de chance saem da formula')
_ex = re.search(r'Inteligência (\d+), Destreza (\d+), maestria (\d+) e treino em Ocultismo\. '
                r'Seu feitiço é Classe (\d+)\. A CD é \*\*(\d+)\*\* e seu bônus é \*\*\+(\d+)\*\*\. '
                r'Ele precisa tirar (\d+) ou mais: \*\*(\d+)%\*\*', _R41)
if not _ex:
    erro('7.2: nao li o exemplo do teste no R41 — a testemunha da tabela de chance sumiu')
else:
    _i, _dx, _m, _c, _cd, _b, _dado, _pct = (int(x) for x in _ex.groups())
    _ok_ex = (_cd == 8 + _i + _m + _c - _dx and _b == _i + _m and _dado == _cd - _b
              and _pct == (21 - _dado) * 5)
    if not _ok_ex:
        erro(f'7.2: o exemplo do R41 (CD {_cd}, bonus +{_b}, {_dado} ou mais, {_pct}%) nao sai '
             'da formula da peca')
    else:
        ok(f'7.2d: o exemplo do R41 confere com a formula (Classe {_c}, Destreza {_dx}, '
           f'{_dado} ou mais, {_pct}%)')

# e) as frases das decisoes: no R41, e na peca.
_VALE72 = [
    ('42', 'sem Pontos de Ritual e com a Classe a menos em dados de dano'),
    ('42', 'A falha não cobra PE adicionais do conjurador'),
    ('42', '**cada auxiliar perde PE iguais à Classe**'),
    ('47', 'Rerrole os dados de dano que caírem no mínimo, até Classe + 1 deles'),
    ('47', 'fica o segundo resultado'),
    ('50', 'sem limite de auxiliares'),
]
_SAIU72 = [
    ('42', 'PE adicionais iguais à sua Classe'),
    ('42', 'conjurador e auxiliar pagam, cada um'),
    ('47', 'que tenham mostrado 1'),
    ('50', '**um único aliado**'),
    ('50', '4 Pontos de Ritual'),
    ('51', 'Meio Acerto e Certeiro'),
]
_PECA_DIZ72 = [
    ('42', 'O que ele custa são dados de dano, e não PE'),
    ('42', 'cada auxiliar perde a Classe do feitiço em PE'),
    ('47', 'Fica o segundo resultado'),
    ('50', 'Não há limite de auxiliares'),
]
_PECA_NAO72 = [
    ('50', 'gasta a Ação Completa dele e dá `4` pontos'),
    ('42', 'os dois pagam a correção'),
    ('48', 'o feitiço não pode ser desviado'),
]
_f1 = [(i, f) for i, f in _VALE72 if f not in _R41]
_f2 = [(i, f) for i, f in _SAIU72 if f in _R41]
_f3 = [(i, f) for i, f in _PECA_DIZ72 if f not in _viva]
_f4 = [(i, f) for i, f in _PECA_NAO72 if f in _viva]
for _i, _f in _f1:
    erro(f'7.2: o R41 nao traz a frase da decisao {_i}: "{_f}"')
for _i, _f in _f2:
    erro(f'7.2: o R41 voltou a trazer o que a decisao {_i} tirou: "{_f}"')
for _i, _f in _f3:
    erro(f'7.2: a peca 27 nao escreve a regra da decisao {_i}: "{_f}"')
for _i, _f in _f4:
    erro(f'7.2: a peca 27 ainda afirma, fora de riscado, o que o item {_i} trocou: "{_f}"')
if not (_f1 or _f2 or _f3 or _f4):
    ok(f'7.2e: {len(_VALE72)} frases das decisoes no R41, {len(_SAIU72)} da candidata fora dele, '
       f'{len(_PECA_DIZ72)} regras novas na peca e {len(_PECA_NAO72)} antigas so riscadas')

print()
print('=' * 88)
if FALHAS:
    print(f'>>> {len(FALHAS)} PROBLEMA(S):')
    for e in FALHAS:
        print('   -', e)
    sys.exit(1)
print('>>> TUDO OK — a escada cresce, os precos cabem nos degraus, o vao e a')
print('    Liberacao Maxima, toda Melhoria declara Restricao, e a peca e o livro batem.')
