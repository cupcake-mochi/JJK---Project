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
POSICAO = re.compile(r"(?i:\ba tabela\b)(?!\s+[`*A-ZÀ-Ü])")

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
    "40-fundamento.md", "45-aptidoes-e-refino.md", "50-equipamento.md",
    "55-ferramenta-amaldicoada.md", "60-invocacoes.md",
    "80-experiencia-e-progressao.md", "90-apendice-bloquear.md",
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
        if linha.startswith("|"):
            continue

        if MOLDURA.search(linha):
            achados.append((i, "MOLDURA", linha.strip()[:76]))
        if REVISAR.search(linha):
            m = REVISAR.search(linha)
            ini = max(0, m.start() - 46)
            avisos.append((i, linha.strip()[ini:m.end() + 40]))
        if POSICAO.search(linha):
            achados.append((i, "TABELA-VAGA", linha.strip()[:76]))
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
    if estrito and (soma or quebradas):
        sys.exit(1)


if __name__ == "__main__":
    main()
