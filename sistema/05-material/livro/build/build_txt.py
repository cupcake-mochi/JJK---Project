#!/usr/bin/env python3
"""
Projeto - M · Manual da Guilda
Markdown -> um .md só, texto puro, na ordem do livro.

Serve para revisão de texto: dá para ler no editor, buscar com Ctrl+F,
comentar linha a linha e diferenciar contra a próxima versão. Nenhuma
diagramação, nenhum HTML.
"""
import glob
import hashlib
import os
import re

from build_docx import CHAPTERS, MANUAL_DIR, split_notes

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "Projeto-M-Manual-da-Guilda-TEXTO.md")

# Os capítulos numerados começam depois da frente do livro.
SEM_NUMERO = {"05-introducao.md", "07-glossario.md", "08-inicio-rapido.md"}


def main():
    partes = [
        "# Projeto M — Manual da Guilda\n",
        "*RPG de mesa de Jujutsu Kaisen. Texto corrido para revisão: "
        "sem diagramação, na mesma ordem do PDF.*\n",
        "*As seções “Notas de revisão” dos arquivos-fonte não entram aqui, "
        "igual não entram no PDF.*\n",
        "\n---\n",
    ]

    numero = 0
    notas = []
    for arquivo, titulo in CHAPTERS:
        caminho = os.path.join(MANUAL_DIR, arquivo)
        if not os.path.exists(caminho):
            print(f"  AVISO: {arquivo} não encontrado, pulando.")
            continue
        with open(caminho, encoding="utf-8") as f:
            bruto = f.read()
        corpo, notas_md = split_notes(bruto)
        corpo = re.sub(r"^#\s+.*\n", "", corpo, count=1).strip()
        # As linhas de atributo do attr_list (título de tabela) são só para o PDF.
        corpo = re.sub(r"^\{:[^}]*\}\s*$\n?", "", corpo, flags=re.M)

        if arquivo in SEM_NUMERO:
            cabecalho = f"# {titulo}"
        else:
            numero += 1
            cabecalho = f"# Capítulo {numero} · {titulo}"

        partes.append(f"\n{cabecalho}\n\n*fonte: `manual/{arquivo}`*\n\n{corpo}\n\n---\n")
        if notas_md:
            notas.append(titulo)

    texto = "\n".join(partes)
    medida = texto   # sem o rodape: a contagem publicada e do livro

    # IMPRESSAO DIGITAL DA FONTE, e ela existe por um defeito medido na v0.146.
    #
    # A v0.145 rodou os quatro builds, DEPOIS consertou um titulo em dois arquivos
    # da fonte, e nao rodou os builds de novo. Os PDFs e este arquivo foram para o
    # commit uma edicao atrasados, e nenhum validador acusou: a checagem 7.1 do
    # `conferir-repositorio.py` compara a copia da entrega contra a copia do projeto
    # — as duas envelhecem juntas — e nunca contra o `.md` que as gerou.
    #
    # Esta linha fecha isso pelo lado do conteudo, e nao pela data do arquivo: git
    # nao preserva mtime, entao um clone novo faria qualquer guarda por data mentir.
    # glob ordenado, e nao a lista CHAPTERS: assim os dois lados da guarda — este
    # e a checagem 7.5 do conferir-repositorio.py — nao precisam concordar sobre
    # nenhuma lista. Um arquivo novo em manual/ entra na conta sozinho.
    fonte = hashlib.sha1()
    for caminho in sorted(glob.glob(os.path.join(MANUAL_DIR, "*.md"))):
        with open(caminho, "rb") as f:
            fonte.update(f.read())
    texto += f"\n<!-- fonte: {fonte.hexdigest()} -->\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"texto: {OUT}")
    print(f"  {numero} capítulos numerados, {len(CHAPTERS) - numero} peças de frente.")
    print(f"  {len(medida.split()):,} palavras, {len(medida):,} caracteres.")
    if notas:
        print(f"  notas de revisão descartadas: {', '.join(notas)}")


if __name__ == "__main__":
    main()
