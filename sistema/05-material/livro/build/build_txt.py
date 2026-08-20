#!/usr/bin/env python3
"""
Projeto - M · Manual da Guilda
Markdown -> um .md só, texto puro, na ordem do livro.

Serve para revisão de texto: dá para ler no editor, buscar com Ctrl+F,
comentar linha a linha e diferenciar contra a próxima versão. Nenhuma
diagramação, nenhum HTML.
"""
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
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"texto: {OUT}")
    print(f"  {numero} capítulos numerados, {len(CHAPTERS) - numero} peças de frente.")
    print(f"  {len(texto.split()):,} palavras, {len(texto):,} caracteres.")
    if notas:
        print(f"  notas de revisão descartadas: {', '.join(notas)}")


if __name__ == "__main__":
    main()
