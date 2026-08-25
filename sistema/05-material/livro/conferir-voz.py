#!/usr/bin/env python3
"""
Projeto - M · Manual da Guilda
Confere a voz do manual: título que não é nome de coisa, e texto que fala do livro.

Não olha número de regra — disso cuidam os validadores do repositório de sistema.
Aqui só entra o que a REGRA-DE-VOZ.md manda.

    python3 conferir-voz.py                  resumo por arquivo
    python3 conferir-voz.py --inventario     lista cada achado, com linha
    python3 conferir-voz.py --so 40          só os arquivos que casam com "40"
    python3 conferir-voz.py --estrito        sai 1 se achar qualquer coisa
"""
import glob
import os
import re
import sys

MANUAL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "manual")

# Título de capítulo (h1) não entra: 41 referências cruzadas apontam para ele pelo nome.
ARTIGO = re.compile(r"^(O|A|Os|As|Um|Uma|Uns|Umas)\s+\S", re.U)
PERGUNTA = re.compile(r"^(O que|Quem|Quando|Onde|Quanto|Quantos|Quantas|Como|Por que)\b|\?\s*$", re.U)
CONTAGEM = re.compile(
    r"\b(dois|duas|tr[êe]s|quatro|cinco|seis|sete|oito|nove|dez|onze|doze|treze|"
    r"catorze|quinze|dezesseis|dezessete|dezoito|dezenove|vinte|trinta|cinquenta|cento)\b",
    re.I,
)
VERBO = re.compile(
    # depois de "de/da/do" a palavra é substantivo: "ritmo de entrega", "linha de conta"
    r"(?<!\bde )(?<!\bda )(?<!\bdo )"
    r"\b(é|são|tem|têm|dá|dão|faz|fazem|cabe|muda|custa|vale|vem|vai|pode|fica|"
    r"cai|sobe|desce|volta|entrega|devolve|compra|cobre|mexe|existe|precisa|aparece|"
    r"chega|nasce|morre|passa|serve|conta|come|acumula|rola|carrega|escreve|cresce|"
    r"some|opera|começa|inclui|paga|sabe|percebe|usa|repetem|está)\b",
    re.I,
)
MOLDURA = re.compile(
    r"\beste (manual|livro|cap[íi]tulo)\b|\besta parte\b|\bdeste (manual|livro)\b|"
    r"\bo resto (do|deste) (livro|manual)\b|\bisto n[ãa]o [ée]\b|"
    r"\b[ée] o dono d[ao]\b|\bexiste por um motivo\b|\bpara ler inteiro\b|"
    r"\b[ée] de consulta\b|\bde consulta, n[ãa]o\b",
    re.I,
)
REVISAR = re.compile(
    r"vale (reparar|a pena|lembrar|notar|guardar)|repare (que|no|nisso|nesse)|"
    r"é a aposta|de propósito|e é por isso|no fundo|isso quer dizer|"
    r"o que importa|não à toa|é exatamente esse|nada mais, nada menos",
    re.I,
)
# Ponteiro por POSICAO. Duas formas, e a segunda entrou depois: ate a setima
# passada esta checagem so' via `a tabela` em linha de PROSA, e os onze ponteiros
# que o livro carregava escaparam pelos dois furos ao mesmo tempo — tres estavam
# dentro de linha de tabela (o laco fazia `continue` antes de chegar aqui) e oito
# escreviam `na tabela`, `pela tabela`, `nas tabelas` ou `o catalogo acima`, que
# a expressao nao alcancava. O gatilho agora e' a PALAVRA DE POSICAO ao lado da
# coisa apontada, e nao o artigo.
POSICAO = re.compile(
    r"(?i:\b(?:tabelas?|cat[áa]logos?|listas?|quadros?|r[ée]guas?)\b"
    r"[^.\n]{0,24}?\b(?:acima|abaixo|ao lado)\b)"
    r"|(?i:\blogo\s+(?:abaixo|acima|adiante|atr[áa]s)\b)"
    r"|(?i:\ba tabela\b)(?!\s+[`*A-ZÀ-Ü])"
)

# Os encaixes da REGRA-DE-VOZ.md: nome fixo, reusado no livro inteiro. Ficam
# de fora das checagens de título — "Como ler" começa com "Como" de propósito.
ENCAIXES = re.compile(
    r"^(Como ler( .+)?|Caracter[íi]sticas( d[aoe] .+)?|Limites|Custo|Dura[çc][ãa]o|"
    r"Alcance|Teto|Cat[áa]logo|Exemplo)$",
    re.I,
)

CODIGOS = {
    "ARTIGO": "título começa com artigo",
    "PERGUNTA": "título é pergunta",
    "FRASE": "título é frase, não nome",
    "CONTAGEM": "contagem por extenso no título",
    "MOLDURA": "o texto fala do próprio livro",
    "TABELA-SEM-NOME": "tabela sem {: .tab-titulo }",
    "TABELA-VAGA": "cita tabela sem nome próprio",
}


# Ordem em que o build numera os capítulos; a frente do livro não recebe número.
CAPITULOS = [
    "10-como-jogar.md", "11-o-turno.md", "12-pericias-e-oficios.md",
    "15-dano-e-condicoes.md", "70-descanso-e-recuperacao.md",
    "20-criacao-de-personagem.md", "25-origens.md", "35-caminhos-e-trilhas.md",
    "40-fundamento.md", "42-tecnica-marcial.md", "45-aptidoes-e-refino.md",
    "47-bencaos-e-lapidacao.md", "50-equipamento.md",
    "55-ferramenta-amaldicoada.md", "60-invocacoes.md", "65-pactos.md",
    "80-experiencia-e-progressao.md",
]


def entradas_do_glossario(manual, arquivo):
    """Entradas do glossário que apontam para este capítulo.

    Não é checagem — é lista de leitura. Mexeu numa definição do capítulo, releia
    estas entradas à mão: o glossário repete a definição em uma linha, e as duas
    divergem em silêncio. Foi assim que 'Rodada' ficou com dois valores.
    """
    if arquivo not in CAPITULOS:
        return []
    numero = CAPITULOS.index(arquivo) + 1
    caminho = os.path.join(manual, "07-glossario.md")
    if not os.path.exists(caminho):
        return []
    saida = []
    for linha in open(caminho, encoding="utf-8"):
        m = re.match(r"^\|([^|]*)\|([^|]*)\|\s*(\d+)\s*\|\s*$", linha)
        if m and int(m.group(3)) == numero:
            saida.append((m.group(1).strip(), m.group(2).strip()))
    return saida



# --- termo sem destino: a checagem que nasceu do caso do `colado`. -----------
#
# Termo entre crases e' promessa. Quem le entende "isto e' nome de coisa do
# sistema" e sai procurando onde a coisa e' explicada; se nao achar, para de
# confiar na crase e para de procurar. Uma leitora do playtest travou em
# `colado` com a definicao seis palavras adiante, na mesma frase — porque nada
# ali dizia que aquilo era uma definicao.
#
# Os DOIS lados sao lidos: os termos saem do texto do manual, e o destino sai do
# 07-glossario.md e das estreias em formato de definicao. Nenhuma lista de termo
# fica escrita aqui dentro.
#
# O corte e' o da REGRA-DE-VOZ.md: 5 usos, ou aparecer em 3 capitulos. Abaixo
# disso o termo e' local e a estreia no lugar basta.
CORTE_USOS, CORTE_CAPITULOS = 5, 3

# Trava de crescimento, e nao meta. O buraco nao precisa fechar de uma vez —
# precisa NAO CRESCER enquanto fecha. Medido na v0.108; baixe o numero conforme
# as entradas forem escritas, nunca suba.
TETO_SEM_DESTINO = 0      # fechado na v0.108: todo termo que passa o corte tem destino.
                          # Daqui em diante o teto e ZERO — termo novo sem entrada no
                          # vocabulario, ou sem estreia definida, falha o --estrito.

TERMO_CRASE = re.compile(r"`([^`\n]{2,40})`")
NOME_DE_COISA = re.compile(r"^[A-ZÁ-Ú][A-Za-zÁ-úá-ú \-]*$")
# Crase opcional: o catálogo de Perícias define no formato "**Termo** — texto",
# sem crase dentro do negrito (05 casos achados na v0.108, todo o catálogo de
# Perícias). Os dois formatos valem como estreia.
ESTREIA = re.compile(r"\*\*`?([^`*\n]{2,40})`?\*\*\s*[—–-]\s")
# O encaixe de habilidade de Trilha/Caminho: "Nível N: `Termo`." — 74 usos em
# 35-caminhos-e-trilhas.md, tão sistemático quanto os títulos de seção. Conta
# como destino pelo mesmo motivo que um título "###" conta.
ESTREIA_NIVEL = re.compile(r"N[íi]vel \d+:\s*`([^`\n]{2,40})`\.")
# Título de seção — o formato mais usado do livro (362 ocorrências). Faltou aqui
# na primeira versão da checagem, e o próprio `Cobrir-se de energia` provou o
# buraco: tinha `### Cobrir-se de energia` e ainda assim contava como órfão.
TITULO = re.compile(r"(?m)^#{2,6}\s+`?([^`\n]{2,40})`?\s*$")
# O rotulo de familia entre colchetes — "**`Leve`** [Nível]" — e o padrao que o
# PHB 2024 usa nas 41 entradas ambiguas do Glossario de Regras dele ("Cone [Área
# de Efeito]", "Surdo [Condição]"). Ele so rotula onde o nome sozinho confunde.
LINHA_GLOSSARIO = re.compile(r"^\|\s*\*\*`?([^`*|]{2,40})`?\*\*(?:\s*\[[^\]]+\])?\s*\|")


def termos_sem_destino(manual):
    """Termos que o livro usa de verdade e nao explica em lugar nenhum.

    Devolve (sem_destino, examinados). Destino vale de dois jeitos: entrada no
    vocabulario, ou estreia no formato de definicao da REGRA-DE-VOZ.
    """
    arquivos = sorted(f for f in os.listdir(manual) if f.endswith(".md"))
    textos = {f: open(os.path.join(manual, f), encoding="utf-8").read() for f in arquivos}

    destinos = set()
    for f, t in textos.items():
        for m in ESTREIA.findall(t):
            destinos.add(m.strip().lower())
        for m in ESTREIA_NIVEL.findall(t):
            destinos.add(m.strip().lower())
        for m in TITULO.findall(t):
            destinos.add(m.strip().lower())
        if f.startswith("07-"):
            for linha in t.split("\n"):
                m = LINHA_GLOSSARIO.match(linha)
                if m:
                    destinos.add(m.group(1).strip().lower())

    usos, capitulos = {}, {}
    for f, t in textos.items():
        if f.startswith("07-"):
            continue
        for m in TERMO_CRASE.findall(t):
            m = m.strip()
            if not NOME_DE_COISA.match(m) or len(m.split()) > 3:
                continue
            usos[m] = usos.get(m, 0) + 1
            capitulos.setdefault(m, set()).add(f)

    examinados = [t for t in usos
                  if usos[t] >= CORTE_USOS or len(capitulos[t]) >= CORTE_CAPITULOS]
    sem = sorted((t for t in examinados if t.lower() not in destinos),
                 key=lambda t: -usos[t])
    return [(t, usos[t], sorted(capitulos[t])) for t in sem], examinados


def confere(caminho):
    achados = []
    avisos = []
    linhas = open(caminho, encoding="utf-8").read().split("\n")
    for i, linha in enumerate(linhas, 1):
        cab = re.match(r"^(#+)\s+(.*)$", linha)
        if cab:
            nivel, texto = len(cab.group(1)), cab.group(2).strip()
            if nivel == 1:
                continue
            limpo = re.sub(r"[`*_]", "", texto)
            if ENCAIXES.match(limpo):
                continue
            if ARTIGO.match(limpo):
                achados.append((i, "ARTIGO", texto))
            if PERGUNTA.search(limpo):
                achados.append((i, "PERGUNTA", texto))
            elif " que " in limpo or VERBO.search(limpo) or ("," in limpo and " e " not in limpo):
                achados.append((i, "FRASE", texto))
            if CONTAGEM.search(limpo):
                achados.append((i, "CONTAGEM", texto))
            continue

        if re.match(r"^\|\s*:?-{2,}", linha):
            janela = linhas[max(0, i - 5):i - 1]
            if not any(".tab-titulo" in x for x in janela):
                achados.append((i, "TABELA-SEM-NOME", linhas[i - 2].strip()[:56]))
            continue
        # A checagem de POSICAO vem ANTES do continue das linhas de tabela: celula
        # de tabela tambem aponta, e era por aqui que tres dos onze passavam.
        if POSICAO.search(linha):
            achados.append((i, "TABELA-VAGA", linha.strip()[:76]))
        if linha.startswith("|"):
            continue

        if MOLDURA.search(linha):
            achados.append((i, "MOLDURA", linha.strip()[:76]))
        if REVISAR.search(linha):
            m = REVISAR.search(linha)
            ini = max(0, m.start() - 46)
            avisos.append((i, linha.strip()[ini:m.end() + 40]))
    return achados, avisos


def refs_quebradas(manual, arquivos):
    """Toda referência *Nome de Seção* tem que bater com um título que existe.

    O itálico quebra linha no fonte, então o texto é colado antes de procurar.
    """
    titulos = set()
    for arq in arquivos:
        for linha in open(os.path.join(manual, arq), encoding="utf-8"):
            cab = re.match(r"^#{2,}\s+(.*)$", linha)
            if cab:
                titulos.add(re.sub(r"[`*]", "", cab.group(1)).strip())
    quebradas = []
    for arq in arquivos:
        colado = re.sub(r"\s+", " ", open(os.path.join(manual, arq), encoding="utf-8").read())
        for m in re.finditer(r"(?:se[çc][ãa]o|em)\s+\*([^*]{4,60})\*", colado):
            alvo = m.group(1).strip()
            if alvo not in titulos and not alvo.startswith(("Como Jogar", "Criação", "Dano,")):
                quebradas.append((arq, alvo))
    return titulos, quebradas


# --------------------------------------------------------------------------
# v0.144: as marcas de "isto ainda nao existe". Esta familia foi contada cinco
# vezes por documentos diferentes e deu cinco numeros diferentes — 4, 5, 8, 7 —
# porque nenhuma contagem tinha validador. Aqui ela ganha um.
#
# O NUMERO NAO MORA AQUI: ele e' lido da REGRA-DE-VOZ.md, que declara junto a
# FRONTEIRA — o que conta como marca e o que nao conta (vaga declarada, variante
# de mesa, e o que mora nas pecas). Sem a fronteira escrita, a proxima contagem
# volta a divergir, que e' exatamente o que aconteceu ate aqui.
MARCAS_PENDENCIA = [
    ("sendo-escrito", re.compile(r"sendo escrit\w*", re.I)),
    ("pergunte-ao-mestre",
     re.compile(r"(?:acordo|combine|combinem)\s+com\s+o\s+(?:seu\s+)?mestre", re.I)),
    ("sem-regra",
     re.compile(r"ainda não (?:tem|têm) regra"
                r"|não (?:tem|têm) regra[^.]{0,30}escrita ainda"
                r"|não tem regra de \w+ escrita", re.I)),
]


def marcas_de_pendencia(manual):
    """As marcas do livro, e o numero que a REGRA-DE-VOZ declara."""
    achadas = []
    for caminho in sorted(glob.glob(os.path.join(manual, "*.md"))):
        nome = os.path.basename(caminho)
        with open(caminho, encoding="utf-8") as fh:
            for i, linha in enumerate(fh, 1):
                for forma, rx in MARCAS_PENDENCIA:
                    if rx.search(linha):
                        achadas.append((nome, i, forma, linha.strip()))
                        break
    teto = None
    regua = os.path.join(os.path.dirname(manual), "REGRA-DE-VOZ.md")
    if os.path.isfile(regua):
        with open(regua, encoding="utf-8") as fh:
            m = re.search(r"O livro carrega `(\d+)` marcas de regra que ainda não existe",
                          fh.read())
        if m:
            teto = int(m.group(1))
    return achadas, teto


# --------------------------------------------------------------------------
# v0.153: o rotulo em negrito longo demais para ser nome de efeito, dentro de
# entrada de catalogo. A v0.141 mediu 9 entradas e 12 rotulos e publicou o par
# sem escrever a definicao; a v0.149 e a v0.152 tentaram remedir e acharam
# outra coisa, porque cada uma inventou o proprio recorte.
#
# OS NUMEROS NAO MORAM AQUI: saem da REGRA-DE-VOZ.md, que declara junto a
# FRONTEIRA. E sao DOIS: o de rotulos e a divida, e o de entradas e' GUARDA —
# sem ele, renomear uma tabela faz o reconhecedor achar zero entrada, logo zero
# rotulo, e a checagem passa verde para sempre sem ter conferido nada.
# E o CORTE tambem sai da regua: ele e' valor de regra, e valor de regra dentro
# de validador e' a licao no 9 pela porta do codigo. Se a linha sumir da
# REGRA-DE-VOZ.md a checagem falha em voz alta em vez de cair num padrao.
ROTULO_ABRE = re.compile(r"^\s*(?:>\s*)*\*\*(.+?)\*\*")
CAMADA_1 = re.compile(r"\s*\*\*(.+?)\*\*\s*[—–-]")


def _limpo(t):
    return re.sub(r"\s+", " ", re.sub(r"[`*_]", "", t)).strip().lower()


def _palavras(t):
    t = re.sub(r"`[^`]*`", "X", re.sub(r"[*_]", "", t))
    return len([p for p in re.split(r"[\s—–]+", t) if re.search(r"\w", p)])


def _abre_paragrafo(linhas, i):
    if i == 0:
        return True
    ant = linhas[i - 1].rstrip()
    return ant == "" or re.fullmatch(r"\s*>\s*", ant) is not None


def _nomes_de_tabela(linhas):
    """Primeira coluna de toda tabela do capitulo — o catalogo que o LIVRO publica."""
    nomes = set()
    for linha in linhas:
        if not linha.startswith("|"):
            continue
        celulas = [c.strip() for c in linha.strip("|").split("|")]
        if not celulas or set(celulas[0]) <= set("-: "):
            continue
        n = _limpo(celulas[0])
        if n and len(n) < 40:
            nomes.add(n)
    return nomes


def _secoes_folha(linhas):
    """Seccoes ### e #### sem subseccao dentro.

    O corte fecha em QUALQUER cabecalho de nivel igual ou menor — inclusive `##`
    e `#`. Sem isso o corpo de uma `###` vaza pela `##` seguinte e vai ate a
    proxima `###`, e a checagem passa a cobrar de uma entrada o rotulo que mora
    tres seccoes adiante. Mesmo defeito de recorte que a v0.151 pagou.
    """
    marcas = []
    for i, linha in enumerate(linhas):
        m = re.match(r"^(#{1,6}) ", linha)
        if m:
            marcas.append((i, len(m.group(1)), linha[len(m.group(1)) + 1:].strip()))
    saida = []
    for k, (i, nivel, titulo) in enumerate(marcas):
        if nivel not in (3, 4):
            continue
        fim = len(linhas)
        for j in range(k + 1, len(marcas)):
            if marcas[j][1] <= nivel:
                fim = marcas[j][0]
                break
        folha = not any(marcas[j][0] < fim for j in range(k + 1, len(marcas)))
        if folha:
            saida.append((titulo, linhas[i + 1:fim], i + 1))
    return saida


def _abre_pela_camada_1(titulo, corpo):
    """A entrada abre dizendo o proprio nome: caixa `**Nome** — ancora`, ou
    ancora em prosa que nomeia ela (o formato das condicoes)."""
    t = _limpo(titulo)
    i = 0
    while i < len(corpo) and not corpo[i].strip():
        i += 1
    if i >= len(corpo):
        return False
    if corpo[i].lstrip().startswith(">"):
        m = CAMADA_1.match(re.sub(r"^\s*>\s?", "", corpo[i]))
        return bool(m and _limpo(m.group(1)) == t)
    return t in _limpo(corpo[i]) and not ROTULO_ABRE.match(corpo[i])


def _regua_do_rotulo(manual):
    """(corte, teto_rotulos, teto_entradas), tudo lido da REGRA-DE-VOZ.md."""
    regua = os.path.join(os.path.dirname(manual), "REGRA-DE-VOZ.md")
    if not os.path.isfile(regua):
        return None, None, None
    texto = open(regua, encoding="utf-8").read()
    m = re.search(r"negrito \*\*abrindo parágrafo\*\*, com mais de `(\d+)` palavras", texto)
    corte = int(m.group(1)) if m else None
    m = re.search(r"O livro carrega `(\d+)` rótulos longos demais, em `(\d+)` "
                  r"entradas de catálogo", texto)
    return corte, (int(m.group(1)) if m else None), (int(m.group(2)) if m else None)


def entradas_de_catalogo(manual):
    """Devolve (rotulos_longos, n_entradas, teto_rotulos, teto_entradas, corte)."""
    corte, teto_r, teto_e = _regua_do_rotulo(manual)
    if corte is None:
        return None, 0, teto_r, teto_e, None
    longos, n_entradas = [], 0
    for nome in CAPITULOS:
        caminho = os.path.join(manual, nome)
        if not os.path.isfile(caminho):
            continue
        linhas = open(caminho, encoding="utf-8").read().split("\n")
        nomes = _nomes_de_tabela(linhas)
        for titulo, corpo, off in _secoes_folha(linhas):
            if _limpo(titulo) not in nomes or not _abre_pela_camada_1(titulo, corpo):
                continue
            n_entradas += 1
            for k, linha in enumerate(corpo):
                if not _abre_paragrafo(corpo, k):
                    continue
                m = ROTULO_ABRE.match(linha)
                if m and _palavras(m.group(1)) > corte:
                    longos.append((nome, off + k + 1, titulo,
                                   _palavras(m.group(1)), m.group(1)))
    return longos, n_entradas, teto_r, teto_e, corte


def main():
    inventario = "--inventario" in sys.argv
    estrito = "--estrito" in sys.argv
    filtro = None
    if "--so" in sys.argv:
        filtro = sys.argv[sys.argv.index("--so") + 1]

    arquivos = sorted(f for f in os.listdir(MANUAL) if f.endswith(".md"))
    if filtro:
        arquivos = [f for f in arquivos if filtro in f]

    total = {}
    todos_avisos = []
    print(f"{'arquivo':32} " + " ".join(f"{c[:9]:>10}" for c in CODIGOS))
    for arq in arquivos:
        achados, avisos = confere(os.path.join(MANUAL, arq))
        por = {c: sum(1 for _, k, _ in achados if k == c) for c in CODIGOS}
        for c, n in por.items():
            total[c] = total.get(c, 0) + n
        marca = "" if any(por.values()) else "  limpo"
        print(f"{arq:32} " + " ".join(f"{por[c] or '.':>10}" for c in CODIGOS) + marca)
        todos_avisos.extend((arq, ln, txt) for ln, txt in avisos)
        if inventario and achados:
            for ln, cod, txt in achados:
                print(f"      {arq}:{ln:<5} {cod:<19} {txt}")
    print(f"{'TOTAL':32} " + " ".join(f"{total.get(c, 0):>10}" for c in CODIGOS))
    print()
    for c, desc in CODIGOS.items():
        print(f"  {c:<20} {desc}")
    soma = sum(total.values())
    print(f"\n  {soma} achados. h1 (título de capítulo) fica de fora por causa das referências cruzadas.")

    print(f"\n  {len(todos_avisos)} trecho(s) para triar à mão (o validador não julga:"
          " 'por que o mundo é assim' fica, 'por que o livro é assim' sai).")
    if inventario:
        for arq, ln, txt in todos_avisos:
            print(f"      TRIAR  {arq}:{ln:<5} …{txt}…")

    if filtro:
        for arq in arquivos:
            entradas = entradas_do_glossario(MANUAL, arq)
            if entradas:
                print(f"\n  glossário — {len(entradas)} entrada(s) definem termo deste capítulo."
                      " Releia à mão se mexeu em definição:")
                for termo, defin in entradas:
                    print(f"      {termo:28} {defin[:66]}")

    todos = sorted(f for f in os.listdir(MANUAL) if f.endswith(".md"))
    titulos, quebradas = refs_quebradas(MANUAL, todos)
    print(f"  {len(titulos)} títulos de seção; {len(quebradas)} referência(s) apontando para título que não existe.")
    for arq, alvo in quebradas:
        print(f"      REF-QUEBRADA  {arq} -> *{alvo}*")

    sem, examinados = termos_sem_destino(MANUAL)
    print(f"\n  {len(examinados)} termos passam o corte de {CORTE_USOS} usos ou {CORTE_CAPITULOS} capítulos;"
          f" {len(sem)} sem destino — nem entrada no vocabulário, nem estreia definida.")
    if inventario:
        for termo, n, caps in sem:
            print(f"      SEM-DESTINO  `{termo}`  {n}x em {len(caps)} cap: {', '.join(c[:2] for c in caps)}")
    elif sem:
        print("      (--inventario lista quais)")
    estourou = TETO_SEM_DESTINO is not None and len(sem) > TETO_SEM_DESTINO
    if estourou:
        print(f"      !! o teto é {TETO_SEM_DESTINO} e são {len(sem)} — entrou termo novo sem destino")

    marcas, teto_marcas = marcas_de_pendencia(MANUAL)
    print(f"\n  {len(marcas)} marca(s) de regra que ainda não existe; o dono diz {teto_marcas}.")
    for arq, n, forma, txt in marcas:
        print(f"      PENDENTE[{forma}]  {arq}:{n}  {txt[:70]}")
    marcas_estourou = teto_marcas is not None and len(marcas) != teto_marcas
    if marcas_estourou:
        print(f"      !! a REGRA-DE-VOZ.md declara {teto_marcas} e o livro tem "
              f"{len(marcas)} — ou entrou marca nova, ou uma foi fechada e o "
              f"número não desceu junto")

    longos, n_entradas, teto_rot, teto_ent, corte = entradas_de_catalogo(MANUAL)
    if corte is None:
        print("\n  !! a REGRA-DE-VOZ.md não declara o corte de palavras do rótulo —"
              " a checagem ROTULO-LONGO não tem régua para aplicar")
        rotulo_estourou, entrada_estourou = True, False
    else:
        print(f"\n  {n_entradas} entrada(s) de catálogo; {len(longos)} rótulo(s) em negrito"
              f" com mais de {corte} palavras. O dono diz {teto_rot} em {teto_ent}.")
        for arq, n, titulo, p, txt in longos:
            print(f"      ROTULO-LONGO  {arq}:{n}  ### {titulo}  ({p}p)  {txt[:56]}")
        rotulo_estourou = teto_rot is not None and len(longos) != teto_rot
        entrada_estourou = teto_ent is not None and n_entradas != teto_ent
    if rotulo_estourou and longos is not None:
        print(f"      !! a REGRA-DE-VOZ.md declara {teto_rot} rótulo(s) longo(s) e o livro"
              f" tem {len(longos)} — entrada de catálogo saiu das quatro camadas")
    if entrada_estourou:
        print(f"      !! a REGRA-DE-VOZ.md declara {teto_ent} entrada(s) de catálogo e o"
              f" reconhecedor achou {n_entradas} — ou entrou entrada nova, ou ele ficou"
              f" cego (tabela renomeada, camada 1 quebrada) e a contagem de rótulo não vale")

    if estrito and (soma or quebradas or estourou or marcas_estourou
                    or rotulo_estourou or entrada_estourou):
        sys.exit(1)


if __name__ == "__main__":
    main()
