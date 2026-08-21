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
OUT_HTML = os.path.join(BASE, "manual.html")
OUT_PDF = os.path.join(ROOT, "Projeto-M-Manual-da-Guilda.pdf")
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
    ("45-aptidoes-e-refino.md",      "Aptidões e Refino",       "練", None),
    ("50-equipamento.md",            "Equipamento",             "具", None),
    ("55-ferramenta-amaldicoada.md", "Ferramenta Amaldiçoada",  "呪", None),
    ("60-invocacoes.md",             "Invocações",              "式", None),

    ("80-experiencia-e-progressao.md", "Experiência e Progressão", "成", "A campanha"),
    ("90-apendice-bloquear.md",      "Apêndice · Bloquear",     "盾", None),
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


def gera_marcas(n):
    """Índice de borda: uma tira por capítulo, escalonada na vertical."""
    ALTURA, TOPO, FUNDO = 14.0, 24.0, 258.0
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
            f'margin-top: {mt:.1f}mm; margin-left: 23mm; }} }}\n'
            f'@page cap{i}:left  {{ @left-top  {{ content: "{i}"; {comum} '
            f'margin-top: {mt:.1f}mm; margin-right: 23mm; }} }}\n'
            f'.cap-{i} {{ page: cap{i}; }}\n'
        )
    return "\n".join(out)


def main():
    partes = []
    sumario_dados = []
    notas = []

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
    linhas = ['<section class="sumario"><h1>Sumário</h1>']
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
    linhas.append("</section>")
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
        f.write(gera_marcas(len(corpos)))

    print(f"HTML: {len(doc):,} caracteres, {len(corpos)} capítulos.")
    if notas:
        print(f"  notas de revisão descartadas (não vão pro PDF): {', '.join(notas)}")
    HTML(OUT_HTML).write_pdf(OUT_PDF, stylesheets=[CSS(CSS_MAIN), CSS(CSS_MARCAS)])
    print(f"PDF:  {OUT_PDF}")


if __name__ == "__main__":
    main()
