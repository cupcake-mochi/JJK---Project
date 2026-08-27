#!/usr/bin/env python3
"""
Projeto - M · Manual da Guilda
Markdown → HTML semântico → PDF (WeasyPrint).

Pipeline conforme "Como o Manual foi diagramado":
  - nenhum estilo inline; tudo vem de manual.css
  - marcas.css (índice de borda) é gerado aqui, pro número real de capítulos
  - largura de coluna de tabela calculada por conteúdo
"""
import os
import re
import sys
import unicodedata

import markdown
from bs4 import BeautifulSoup
from weasyprint import HTML, CSS

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
MANUAL_DIR = os.path.join(ROOT, "manual")
OUT_HTML = os.path.join(BASE, "manual.html")   # intermediario, sobrescrito a cada build
# Tres diagramacoes, para comparar. A `A-atual` nao se gera: ela e' o snapshot
# do que estava publicado antes desta leva, guardado a mao.
#   (sem argumento) coluna unica, com o sumario em duas colunas
#   --duas          corpo em duas colunas, tabela de 4+ colunas em largura inteira
VARIANTE = "duas" if "--duas" in sys.argv else "unica"
OUT_PDF = os.path.join(ROOT, "Projeto-M-Manual-da-Guilda-C-duas-colunas.pdf"
                       if VARIANTE == "duas" else "Projeto-M-Manual-da-Guilda.pdf")
CSS_VARIANTE = os.path.join(BASE, "duas-colunas.css") if VARIANTE == "duas" else None
CSS_MAIN = os.path.join(BASE, "manual.css")
CSS_MARCAS = os.path.join(BASE, "marcas.css")

# (arquivo, título, kanji, parte) — a ordem aqui é a ordem do livro
CHAPTERS = [
    ("10-como-jogar.md",             "Como Jogar",              "基", "O jogo"),
    ("11-o-turno.md",                "O Turno",                 "回", None),
    ("12-pericias-e-oficios.md",     "Perícias e Ofícios",      "技", None),
    ("15-dano-e-condicoes.md",       "Dano, Condições e Cobertura", "傷", None),
    ("70-descanso-e-recuperacao.md", "Descanso e Recuperação",  "休", None),

    ("20-criacao-de-personagem.md",  "Criação de Personagem",   "創", "O personagem"),
    ("25-origens.md",                "Origens e Legados",       "源", None),
    ("35-caminhos-e-trilhas.md",     "Caminhos e Trilhas",      "道", None),
    ("40-fundamento.md",             "Fundamento",              "術", None),
    ("42-tecnica-marcial.md",        "Técnica Marcial",         "型", None),
    ("43-sem-tecnica.md",            "Sem Técnica",             "種", None),
    ("45-aptidoes-e-refino.md",      "Aptidões e Refino",       "練", None),
    ("47-bencaos-e-lapidacao.md",    "Bênçãos e Lapidação",     "恵", None),
    ("50-equipamento.md",            "Equipamento",             "具", None),
    ("55-ferramenta-amaldicoada.md", "Ferramenta Amaldiçoada",  "呪", None),
    ("60-invocacoes.md",             "Invocações",              "式", None),
    ("65-pactos.md",                 "Pactos",                  "縛", None),

    ("80-experiencia-e-progressao.md", "Experiência e Progressão", "成", "A campanha"),
]

# Frente do livro: não recebem número de capítulo.
FRONT = [
    ("05-introducao.md",    "Bem-vindo à Guilda",        "門"),
    ("07-glossario.md",     "O vocabulário do sistema",  "語"),
    ("08-inicio-rapido.md", "Antes da primeira sessão",  "始"),
]

# Índice remissivo. Cada termo ganha uma âncora na primeira vez que aparece em
# cada capítulo, e a página sai do target-counter, como no sumário.
INDEX_TERMS = [
    "Ação Bônus", "Ação Padrão", "Amarra", "Ampliar", "Aptidão", "Arredondamento",
    "Ataque de oportunidade", "Atributo", "Caminho", "CD", "Cicatriz", "Classe 0",
    "Classe Passiva", "Cobertura", "Concentração", "Condição", "Crítico",
    "Dano na alma", "Defesa", "Desgaste", "Desvantagem", "Espaço de feitiço",
    "Essência", "Estigma", "Exaustão", "Expansão de Domínio", "Família",
    "Ferramenta amaldiçoada", "Feitiço", "Forma", "Fundamento", "Grau",
    "Integridade", "Invocação", "Legado", "Liberação Máxima", "Maestria",
    "Marco", "Melhoria", "Ofício", "Origem", "Pacto", "Passiva", "Patente",
    "Perícia", "Pontos de energia", "Pontos de vida", "Proteção", "Reação",
    "Redução de Dano", "Refino", "Restrição", "Rodada", "Rotina", "Selo",
    "Sequela", "Teste de Resistência", "Técnica Máxima", "Teto", "Trilha",
    "Uso Livre", "Vantagem",
]

NOTES_HEADING = "## Notas de revisão"

SUBTITULO = "RPG de mesa de Jujutsu Kaisen"
ETIQUETA = "Manual da Guilda"
KANJI_CAPA = "呪"

NOTA_CAPA = (
    "Feito para um servidor de guilda: cinco a sete mestres, e um personagem "
    "que atravessa mesas sem trocar de ficha."
)


def slug(text):
    t = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    t = re.sub(r"[^\w\s-]", "", t).strip().lower()
    return re.sub(r"[\s_]+", "-", t)


def split_notes(md_text):
    """Separa corpo do capítulo da seção final 'Notas de revisão'."""
    idx = md_text.find(NOTES_HEADING)
    if idx == -1:
        return md_text, None
    return md_text[:idx].rstrip() + "\n", md_text[idx + len(NOTES_HEADING):].strip()


def larguras(rows, ncols):
    """Peso de coluna por conteúdo. Fórmula do documento de diagramação."""
    pesos = []
    for ci in range(ncols):
        vals = [len(r[ci]) for r in rows if ci < len(r) and r[ci] is not None]
        if not vals:
            vals = [3]
        mx, md = max(vals), sum(vals) / len(vals)
        base = 0.65 * mx + 0.35 * md
        # coluna que só carrega número fica estreita
        so_num = all(re.fullmatch(r"[\d\s.,+×/–—-]*", (r[ci] or "")) for r in rows if ci < len(r))
        if so_num:
            base = min(base, 9)
        pesos.append(max(base, 3) ** 0.78)
    total = sum(pesos)
    return [100 * p / total for p in pesos]


def trata_tabelas(soup):
    for table in soup.find_all("table"):
        head = table.find("thead")
        body = table.find("tbody")
        header_cells = [c.get_text(" ", strip=True) for c in head.find_all("th")] if head else []
        rows = []
        if body:
            for tr in body.find_all("tr"):
                rows.append([c.get_text(" ", strip=True) for c in tr.find_all(["td", "th"])])
        ncols = max([len(header_cells)] + [len(r) for r in rows]) if (header_cells or rows) else 0
        if ncols == 0:
            continue

        todas = ([header_cells] if header_cells else []) + rows
        ws = larguras(todas, ncols)

        cg = soup.new_tag("colgroup")
        for w in ws:
            col = soup.new_tag("col")
            col["style"] = f"width:{w:.2f}%"
            cg.append(col)
        table.insert(0, cg)

        classes = ["tab"]
        if ncols >= 7:
            classes.append("muito-larga")
        elif ncols >= 5:
            classes.append("larga")
        # Na diagramacao de duas colunas, tabela de quatro colunas ou mais nao
        # cabe numa coluna de 233pt: os valores curtos quebram em duas linhas
        # cada e a tabela deixa de ser consultavel. Ela sai do fluxo de colunas
        # e ocupa a largura inteira, que e' o que os manuais do hobby fazem com
        # a tabela de armas e a de progressao. O corte e' o NUMERO DE COLUNAS e
        # nao a largura em caracteres: celula de prosa quebra bem numa coluna
        # estreita, e ela e' quem domina qualquer medida por caractere.
        # Tabela de largura inteira: o corte e' GRADE, e nao numero de coluna
        # nem largura em caractere.
        #
        # `ncols >= 4` foi a primeira regra e produzia 40 tabelas — 40 furos no
        # fluxo de duas colunas, e cada furo deixa meia pagina vazia. Largura em
        # caractere tambem nao serve: ela conta celula de prosa como se nao
        # quebrasse, e marcaria 176 de 211.
        #
        # O que nao cabe numa coluna de 236pt e' a GRADE que se varre com o olho:
        # cinco colunas ou mais, ou quatro com corpo longo. Sao 26.
        if ncols >= 5 or (ncols == 4 and len(rows) >= 10):
            classes.append("plena")
            # E a que enche uma pagina sozinha comeca em pagina propria. Sem
            # isso o titulo dela (mesmo virado `<caption>`) fica no pe da coluna
            # anterior e o corpo vai para a pagina seguinte — medido no catalogo
            # de armas. Eram DUAS ate a v0.138 — o catalogo de 52 armas e a
            # tabela de progressao — e sao TRES desde a v0.139, quando o capitulo
            # 3 trocou a tabela de pericia por atributo por um catalogo unico de
            # 34 linhas. O corte de 20 linhas e' declarado aqui.
            #
            # E' isso que faz a diagramacao de duas colunas SUBIR de pagina numa
            # versao em que o livro perdeu palavra: cada uma destas comeca pagina.
            if len(rows) >= 20:
                classes.append("pagina-propria")

        # tabela sem cabeçalho útil e de duas colunas = ficha rótulo/valor
        cab_vazio = all(not h for h in header_cells)
        if ncols == 2 and cab_vazio:
            classes.append("ficha")
            if head:
                head.decompose()
            for tr in table.find_all("tr"):
                cels = tr.find_all("td")
                if cels:
                    cels[0]["class"] = cels[0].get("class", []) + ["rot"]
        table["class"] = classes

        # primeira coluna de tabela com cabeçalho = nome da entrada
        if not cab_vazio and body:
            for tr in body.find_all("tr"):
                cels = tr.find_all("td")
                if cels:
                    cels[0]["class"] = cels[0].get("class", []) + ["nome"]


def trata_destaques(soup):
    """blockquote do Markdown vira caixa de destaque.

    A caixa padrao e' `.destaque`: resumo de regra, o uso de longe mais comum.
    Um blockquote marcado com `{: .aviso }` no fonte vira `.aviso` — a caixa de
    borda, para o que o leitor precisa saber ANTES de aplicar a regra, e nao a
    regra em si. O attr_list poe a classe no proprio blockquote, e e' por isso
    que ela e' lida antes de o conteudo mudar de tag.
    """
    for bq in soup.find_all("blockquote"):
        # O attr_list nunca marca o blockquote: ele poe a classe no PRIMEIRO
        # <p> de dentro. Medido — as tres formas de escrever `{: .aviso }` no
        # fonte caem todas ali. Ler do blockquote devolvia sempre None.
        primeiro = bq.find("p")
        classes = (primeiro.get("class") or []) if primeiro else []
        eh_aviso = "aviso" in classes
        if eh_aviso:
            primeiro["class"] = [c for c in classes if c != "aviso"] or None
            if not primeiro["class"]:
                del primeiro["class"]
        aside = soup.new_tag("aside")
        aside["class"] = ["aviso"] if eh_aviso else ["destaque"]
        for child in list(bq.children):
            aside.append(child.extract())
        bq.replace_with(aside)


def tira_rotulo_repetido(soup):
    """Titulo de tabela que repete o titulo da secao logo acima sai.

    Sao 32 no livro — `#### Base por Classe` seguido de `**Base por Classe**`
    com `{: .tab-titulo }`. Impresso, o leitor le o mesmo rotulo duas vezes
    seguidas, e numa coluna estreita eles ficam colados.

    O corte e' no BUILD e nao no fonte: o `conferir-voz.py` exige que toda tabela
    tenha nome, e o nome continua la para o texto poder apontar para ela.
    """
    def chave(s):
        s = unicodedata.normalize("NFKD", s)
        s = "".join(c for c in s if not unicodedata.combining(c))
        return re.sub(r"[^a-z0-9]", "", s.lower())

    n = 0
    for p in list(soup.find_all("p")):
        if "tab-titulo" not in (p.get("class") or []):
            continue
        ant = p.find_previous_sibling()
        if ant is None or ant.name not in ("h2", "h3", "h4", "h5", "h6"):
            continue
        if chave(ant.get_text(" ", strip=True)) != chave(p.get_text(" ", strip=True)):
            continue
        p.decompose()
        n += 1
    return n


TITULOS_MOVIDOS = []


def segmenta_colunas(soup):
    """Parte o capitulo em blocos de duas colunas e blocos de largura inteira.

    O WeasyPrint 69 NAO implementa `column-span: all` — medido: um `h2` e uma
    tabela marcados com ele continuaram presos dentro da coluna da esquerda. Sem
    ele, a unica forma de uma tabela larga atravessar as duas colunas e' ela nao
    estar DENTRO do bloco de colunas.

    Entao a segmentacao e' feita aqui: sequencia de elementos estreitos vira um
    `<div class="c2">`, e cada tabela `.plena` (mais o titulo dela) fica solta
    entre eles, em largura inteira.
    """
    filhos = [c for c in soup.children if getattr(c, "name", None)]
    grupos, atual = [], []
    i = 0
    while i < len(filhos):
        el = filhos[i]
        plena = el.name == "table" and "plena" in (el.get("class") or [])
        # o titulo da tabela vai junto com ela
        titulo_de_plena = (
            "tab-titulo" in (el.get("class") or [])
            and i + 1 < len(filhos)
            and filhos[i + 1].name == "table"
            and "plena" in (filhos[i + 1].get("class") or [])
        )
        if plena or titulo_de_plena:
            # O TITULO DA SECAO VAI JUNTO COM A TABELA, e nao fica no fim da coluna.
            #
            # Achado do Mizuki lendo a pagina 137 da v0.145: o `### Maestria` ficava
            # sozinho no pe da coluna da direita, com a tabela dele solta abaixo em
            # largura inteira e um vao no meio. Nao e' quebra ruim — e' o titulo
            # ficando do lado errado da fronteira entre um bloco de duas colunas e um
            # bloco de largura inteira. Ele fecha o `c2`, e a tabela abre o `plena`.
            #
            # Como o titulo nao tem o que anunciar depois dele naquela coluna, ele sai
            # do `c2` e entra no bloco de largura inteira, colado na tabela que ele
            # nomeia. `break-after: avoid` nao resolve: ele amarra dentro do mesmo
            # fluxo, e aqui sao dois fluxos diferentes.
            cabecas = []
            while atual and atual[-1].name in ("h2", "h3", "h4"):
                cabecas.insert(0, atual.pop())
            for _c in cabecas:
                TITULOS_MOVIDOS.append(_c.get_text(" ", strip=True))
            if atual:
                grupos.append(("c2", atual))
                atual = []
            bloco = list(cabecas) + [el]
            if titulo_de_plena:
                bloco.append(filhos[i + 1])
                i += 1
            grupos.append(("plena", bloco))
            # O título da tabela larga vira `<caption>` dela. Solto, ele fica no
            # pé de uma coluna com a tabela na página seguinte: `break-after:
            # avoid` é largado pelo WeasyPrint quando o bloco seguinte tem de
            # quebrar de qualquer jeito, e uma tabela de 55 linhas sempre tem.
            # Dentro da tabela ele viaja junto, por construção.
            if titulo_de_plena:
                titulo, tabela = bloco[-2], bloco[-1]
                cap = soup.new_tag("caption")
                for filho in list(titulo.children):
                    cap.append(filho.extract())
                titulo.decompose()
                tabela.insert(0, cap)
                bloco[:] = list(cabecas) + [tabela]

            # E SE A TABELA COMECA EM PAGINA PROPRIA, QUEM PULA A PAGINA E O TITULO.
            #
            # Segunda metade do achado do Mizuki, e ela so apareceu olhando o PDF:
            # com o titulo colado na tabela, as tres tabelas que carregam
            # `pagina-propria` deixavam o titulo no pe da pagina anterior e pulavam
            # sozinhas — trocando o vao do meio da coluna por um titulo orfao no fim
            # da pagina, que e pior. O `break-before: page` tem de sair da tabela e
            # ir para o titulo, senao a quebra acontece ENTRE os dois.
            if cabecas:
                tab = bloco[-1]
                cls = tab.get("class") or []
                if "pagina-propria" in cls:
                    tab["class"] = [c for c in cls if c != "pagina-propria"]
                    h = cabecas[0]
                    h["class"] = (h.get("class") or []) + ["puxa-pagina"]
        else:
            atual.append(el)
        i += 1
    if atual:
        grupos.append(("c2", atual))

    for tipo, els in grupos:
        if tipo != "c2":
            continue
        caixa = soup.new_tag("div")
        caixa["class"] = ["c2"]
        els[0].insert_before(caixa)
        for e in els:
            caixa.append(e.extract())
    return sum(1 for tipo, _ in grupos if tipo == "plena")


def cola_chamada(soup):
    """Frase de chamada + caixa viram um bloco só, que não quebra no meio.

    O `break-after: avoid` de um título amarra ele ao elemento seguinte e para
    aí. O padrão que sobrava no livro era título + frase de chamada + caixa: os
    dois primeiros ficavam no pé de uma página e a caixa ia para a seguinte,
    deixando o leitor com *"Leia (ou narre) isto para o grupo:"* e nada para ler.

    `break-before: avoid` em TODA caixa foi medido e reprovou: são 253 caixas no
    livro, e a versão com ela ficou com as mesmas oito páginas curtas e nove
    páginas a mais. O alvo certo é o par, e ele se reconhece pelo texto — um
    parágrafo que termina em dois-pontos e é seguido de caixa. São oito no livro.
    """
    n = 0
    for aside in soup.find_all("aside"):
        ant = aside.find_previous_sibling()
        if ant is None or ant.name != "p":
            continue
        if not ant.get_text(" ", strip=True).endswith(":"):
            continue
        par = soup.new_tag("div")
        par["class"] = ["par"]
        ant.insert_before(par)
        par.append(ant.extract())
        par.append(aside.extract())
        n += 1
    return n


def quebras_em_citacao(md_text):
    """Dentro de uma citação, cada linha é uma linha.

    O Markdown junta linhas seguidas num parágrafo só, o que cola fórmula em
    fórmula dentro de uma caixa de destaque. Duas linhas de citação seguidas,
    as duas com conteúdo, ganham quebra dura (dois espaços no fim).
    """
    linhas = md_text.split("\n")
    for i in range(len(linhas) - 1):
        a, b = linhas[i].lstrip(), linhas[i + 1].lstrip()
        if not (a.startswith(">") and b.startswith(">")):
            continue
        if a.strip() == ">" or b.strip() == ">":
            continue
        if a.rstrip().endswith(("|", "  ")):   # tabela ou quebra já posta
            continue
        if b.lstrip(">").strip().startswith("|"):
            continue
        # ⚠ Quebra dura só onde ela CARREGA sentido — v0.126.
        #
        # A regra antiga quebrava entre quaisquer duas linhas de citação, e com
        # isso a diagramação passava a depender de onde o autor apertou Enter no
        # `.md`. Em coluna larga isso não aparecia, porque as linhas do fonte têm
        # ~90 caracteres e enchem a linha impressa. Numa coluna de 236pt a mesma
        # caixa saía picotada no meio da frase.
        #
        # O que precisa de quebra é linha de REGRA: fórmula, entrada com nome em
        # negrito na frente, linha curta. Prosa longa e sem marca reflui.
        nu = a.lstrip(">").strip()
        prosa_longa = (
            len(nu) > 58
            and "`" not in nu
            and not nu.startswith(("**", "1.", "2.", "3.", "-", "·"))
        )
        if prosa_longa:
            continue
        linhas[i] = linhas[i].rstrip() + "  "
    return "\n".join(linhas)


def md_para_html(md_text, prefixo_id, achados=None):
    html = markdown.markdown(
        quebras_em_citacao(md_text),
        extensions=["tables", "extra", "sane_lists", "attr_list"],
    )
    soup = BeautifulSoup(html, "html.parser")
    trata_destaques(soup)
    trata_tabelas(soup)
    tira_rotulo_repetido(soup)
    cola_chamada(soup)
    if VARIANTE == "duas":
        segmenta_colunas(soup)
    if achados is not None:
        marca_indice(soup, prefixo_id, achados)
    secoes = []
    vistos = set()
    for h2 in soup.find_all("h2"):
        txt = h2.get_text(" ", strip=True)
        sid = f"{prefixo_id}-{slug(txt)}"
        n = 2
        while sid in vistos:
            sid = f"{prefixo_id}-{slug(txt)}-{n}"
            n += 1
        vistos.add(sid)
        h2["id"] = sid
        secoes.append((txt, sid))
    return str(soup), secoes


def marca_indice(soup, cid, achados):
    """Põe uma âncora vazia na 1ª vez que cada termo aparece neste capítulo.

    Âncora vazia, e não um wrap: mexer no texto quebraria <code> e célula de
    tabela. O target-counter resolve a página da âncora igual resolve a do
    capítulo no sumário.
    """
    pendentes = {t: re.compile(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])", re.I)
                 for t in INDEX_TERMS}
    for no in list(soup.find_all(string=True)):
        if not pendentes:
            break
        if no.parent.name in ("script", "style"):
            continue
        texto = str(no)
        for termo, rx in list(pendentes.items()):
            m = rx.search(texto)
            if not m:
                continue
            aid = f"ix-{cid}-{slug(termo)}"
            ancora = soup.new_tag("span")
            ancora["class"] = ["ix-anc"]
            ancora["id"] = aid
            no.insert_before(ancora)
            achados.setdefault(termo, []).append(aid)
            del pendentes[termo]
            break   # uma âncora por nó de texto: não fragmenta o parágrafo


def gera_indice(achados):
    if not achados:
        return ""
    def chave(t):
        return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    linhas = ['<section class="indice"><h1 id="indice-remissivo">Índice remissivo</h1>',
              '<p class="ix-nota">O número é a página em que o termo aparece pela '
              'primeira vez naquele capítulo. Para o que cada um quer dizer, veja '
              '<em>O vocabulário do sistema</em>, no começo do livro.</p>',
              '<div class="ix-cols">']
    for termo in sorted(achados, key=chave):
        refs = " ".join(f'<a class="ix-p" href="#{a}"></a>' for a in achados[termo])
        linhas.append(f'<div class="ix-item"><span class="ix-t">{termo}</span> {refs}</div>')
    linhas.append("</div></section>")
    return "\n".join(linhas)


def bloco_capitulo(titulo, kanji, numero, corpo_html, cid, classe_marca=None):
    if numero is None:
        etiqueta = ""
    else:
        etiqueta = f'<span class="arab">Capítulo {numero}</span>'
    cls = "capitulo" + (f" {classe_marca}" if classe_marca else "")
    return f"""
<section class="{cls}">
  <header class="abertura">
    <span class="abertura-n"><span class="kanji">{kanji}</span>{etiqueta}</span>
    <h1 id="{cid}">{titulo}</h1>
  </header>
{corpo_html}
</section>
"""


def gera_marcas(n, margem_externa=32.0):
    """Índice de borda: uma tira por capítulo, escalonada na vertical.

    A tira mora dentro da caixa de margem, e o deslocamento dela é medido a
    partir da margem externa da página: com 32mm de margem e 9mm de tira, ela
    encosta na borda com 23mm. Na variante de duas colunas a margem cai para
    18mm, e o 23mm fixo jogava a tira para FORA da página — ela sumia.
    """
    ALTURA, TOPO, FUNDO = 14.0, 24.0, 258.0
    desloc = max(margem_externa - 9.0, 0.0)
    passo = (FUNDO - TOPO - ALTURA) / max(n - 1, 1)
    out = ["/* gerado por build.py — não editar à mão */\n"]
    comum = ('background: var(--selo); color: var(--washi); '
             'font-family: "Barlow Condensed", sans-serif; font-weight: 600; '
             'font-size: 11pt; text-align: center; vertical-align: middle; '
             f'height: {ALTURA}mm; width: 9mm;')
    for i in range(1, n + 1):
        mt = TOPO + (i - 1) * passo
        out.append(
            f'@page cap{i}:right {{ @right-top {{ content: "{i}"; {comum} '
            f'margin-top: {mt:.1f}mm; margin-left: {desloc:.0f}mm; }} }}\n'
            f'@page cap{i}:left  {{ @left-top  {{ content: "{i}"; {comum} '
            f'margin-top: {mt:.1f}mm; margin-right: {desloc:.0f}mm; }} }}\n'
            f'.cap-{i} {{ page: cap{i}; }}\n'
        )
    return "\n".join(out)


def main():
    partes = []
    sumario_dados = []
    notas = []

    # ---------- capa de arte ----------
    # A arte e pagina 1 e a capa tipografica virou pagina 2: ela carrega o
    # sumario de capitulos e a nota, e nada disso cabe numa imagem.
    # O caminho e relativo ao manual.html, que e' quem o WeasyPrint abre.
    #
    # O arquivo ja vem RECORTADO em proporcao A4 exata (1697x2400). A arte
    # original era 1792x2400, que e mais larga que A4 — e o `cover` cortava
    # pelos LADOS, comendo o rotulo de versao do canto inferior direito. Os
    # 95 px sairam todos da ESQUERDA, que la e couro vazio.
    CAPA = os.path.join(BASE, "..", "arte", "Capa-v0.1.jpg")
    if os.path.exists(CAPA):
        partes.append('\n<section class="capa-arte"></section>\n')
    else:
        print("  AVISO: arte/Capa-v0.1.jpg nao encontrada — saiu sem capa de arte.")

    # ---------- capa ----------
    itens_capa = "\n".join(f"<li>{t}</li>" for _, t, _, _ in CHAPTERS)
    partes.append(f"""
<section class="capa">
  <div class="capa-marca">{KANJI_CAPA}</div>
  <div class="capa-etiqueta">{ETIQUETA}</div>
  <h1 class="capa-titulo">Projeto&nbsp;M</h1>
  <div class="capa-sub">{SUBTITULO}</div>
  <ol class="capa-lista">{itens_capa}</ol>
  <div class="capa-nota">{NOTA_CAPA}</div>
</section>
""")

    # ---------- ficha técnica ----------
    partes.append("""
<section class="creditos">
  <h1>Ficha técnica</h1>
  <p><strong>Projeto M</strong> é um sistema de RPG de mesa ambientado no universo de
  Jujutsu Kaisen, feito para um servidor de guilda com cinco a sete mestres ativos e
  personagem persistente entre mesas. O filtro que decidiu quase toda regra deste livro
  foi um só: dois mestres que nunca conversaram chegam ao mesmo número?</p>

  <h2>Criação e regras</h2>
  <p>Mizuki</p>

  <h2>Licença e escopo</h2>
  <p>Material de fã, gratuito e sem fins comerciais. Jujutsu Kaisen e seus personagens
  pertencem à Shueisha, à MAPPA e a Gege Akutami. Este material não é afiliado a nenhum
  dos três, e existe só para dar mesa a quem quer jogar no universo deles.</p>
</section>
""")

    # ---------- frente do livro ----------
    achados = {}
    frentes = []
    for arquivo, titulo, kanji in FRONT:
        caminho = os.path.join(MANUAL_DIR, arquivo)
        if not os.path.exists(caminho):
            print(f"  AVISO: {arquivo} não encontrado — pulado.")
            continue
        with open(caminho, encoding="utf-8") as f:
            md = f.read()
        md = re.sub(r"^#\s+.*\n", "", md, count=1)
        cid = f"cap-{slug(titulo)}"
        html, secoes = md_para_html(md, cid, achados)
        frentes.append((titulo, kanji, html, cid))
        sumario_dados.append((None, titulo, cid, secoes, None))

    # ---------- capítulos ----------
    # As "Notas de revisão" que os capítulos carregam são recado de quem escreve o
    # sistema, não material de mesa: elas são descartadas aqui e não entram no PDF.
    corpos = []
    numero = 0
    for arquivo, titulo, kanji, parte in CHAPTERS:
        caminho = os.path.join(MANUAL_DIR, arquivo)
        if not os.path.exists(caminho):
            print(f"  AVISO: {arquivo} não encontrado — capítulo pulado.")
            continue
        numero += 1
        with open(caminho, encoding="utf-8") as f:
            bruto = f.read()
        corpo_md, notas_md = split_notes(bruto)
        corpo_md = re.sub(r"^#\s+.*\n", "", corpo_md, count=1)
        cid = f"cap-{slug(titulo)}"
        html, secoes = md_para_html(corpo_md, cid, achados)
        corpos.append((titulo, kanji, numero, html, cid, f"cap-{numero}"))
        sumario_dados.append((numero, titulo, cid, secoes, parte))
        if notas_md:
            notas.append(titulo)

    # ---------- sumário ----------
    linhas = ['<section class="sumario"><h1>Sumário</h1><div class="sum-corpo">']
    for item in sumario_dados:
        if len(item) == 4:
            numero, titulo, cid, secoes = item
            parte = None
        else:
            numero, titulo, cid, secoes, parte = item
        if parte:
            linhas.append(f'<div class="sum-parte">{parte}</div>')
        n_html = f'<span class="sum-n">{numero}</span>' if numero else '<span class="sum-n"></span>'
        linhas.append(f'<div class="sum-cap"><a href="#{cid}">{n_html}{titulo}</a></div>')
        for txt, sid in secoes:
            linhas.append(f'<div class="sum-sec"><a href="#{sid}">{txt}</a></div>')
    linhas.append('<div class="sum-cap"><a href="#indice-remissivo">'
                  '<span class="sum-n"></span>Índice remissivo</a></div>')
    linhas.append("</div></section>")
    partes.append("\n".join(linhas))

    # ---------- corpo ----------
    for titulo, kanji, html, cid in frentes:
        partes.append(bloco_capitulo(titulo, kanji, None, html, cid))
    for titulo, kanji, numero, html, cid, marca in corpos:
        partes.append(bloco_capitulo(titulo, kanji, numero, html, cid, marca))

    # ---------- índice remissivo ----------
    partes.append(gera_indice(achados))

    doc = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="utf-8"><title>Projeto M — Manual da Guilda</title></head>
<body>
{''.join(partes)}
</body>
</html>"""

    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(doc)
    with open(CSS_MARCAS, "w", encoding="utf-8") as f:
        f.write(gera_marcas(len(corpos), 18.0 if VARIANTE == "duas" else 32.0))

    print(f"HTML: {len(doc):,} caracteres, {len(corpos)} capítulos.")
    if TITULOS_MOVIDOS:
        print(f"  {len(TITULOS_MOVIDOS)} título(s) foram com a tabela larga em vez de "
              f"ficar no pé da coluna:")
        for _t in TITULOS_MOVIDOS:
            print(f"    · {_t}")
    if notas:
        print(f"  notas de revisão descartadas (não vão pro PDF): {', '.join(notas)}")
    folhas = [CSS(CSS_MAIN), CSS(CSS_MARCAS)]
    if CSS_VARIANTE:
        folhas.append(CSS(CSS_VARIANTE))
    HTML(OUT_HTML).write_pdf(OUT_PDF, stylesheets=folhas)
    print(f"PDF:  {OUT_PDF}")


if __name__ == "__main__":
    main()
