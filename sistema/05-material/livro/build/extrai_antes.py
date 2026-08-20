#!/usr/bin/env python3
"""
Recorta de Projeto-M-Manual-da-Guilda-TEXTO.md o capítulo que veio de um arquivo-fonte.

O TEXTO.md é gerado antes de uma passada de revisão, então ele serve de "antes"
para o guard_numeros.py quando o arquivo em manual/ já foi reescrito.

    python3 build/extrai_antes.py 10-como-jogar.md > /tmp/antes.md
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXTO = os.path.join(ROOT, "Projeto-M-Manual-da-Guilda-TEXTO.md")


def main():
    alvo = sys.argv[1]
    bruto = open(TEXTO, encoding="utf-8").read()
    marca = f"*fonte: `manual/{alvo}`*"
    ini = bruto.find(marca)
    if ini < 0:
        sys.exit(f"não achei {marca} em {TEXTO}")
    ini += len(marca)
    fim = bruto.find("\n# ", ini)
    trecho = bruto[ini:fim if fim > 0 else len(bruto)]
    sys.stdout.write(re.sub(r"\n---\s*$", "", trecho.strip()))


if __name__ == "__main__":
    main()
