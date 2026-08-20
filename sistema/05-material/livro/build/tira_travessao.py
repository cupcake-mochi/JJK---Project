#!/usr/bin/env python3
"""Troca travessão de prosa por pontuação do dia a dia.

O dono do sistema pediu para evitar travessão: é correto na norma culta, mas
pouco usado na fala, e o excesso dá ar artificial ao texto.

Três coisas ficam intactas:
  - o cabeçalho de catálogo `**Nome** — descrição`, que é convenção estrutural;
  - o travessão sozinho numa célula de tabela, que quer dizer "vazio";
  - travessão dentro de bloco de código.
"""
import re
import sys

CABECALHO = re.compile(r"^(\s*>?\s*(?:[-*]\s*)?\*\*[^*]+\*\*)\s+—\s+")
CELULA_VAZIA = re.compile(r"\|\s*—\s*\|")


def escolhe(depois, ja_tem_dois_pontos):
    """Que pontuação entra no lugar do travessão."""
    d = depois.lstrip()
    if re.match(r"(e|mas|ou|porém|então|e não|nem)\s", d, re.I):
        return ", "
    if re.match(r"(que|porque|pois)\s", d, re.I):
        return ", "
    if ja_tem_dois_pontos:
        return ", "
    return ": "


def converte_linha(linha):
    if "—" not in linha:
        return linha, 0

    # célula de tabela com travessão sozinho: preserva
    if CELULA_VAZIA.search(linha):
        marcada = CELULA_VAZIA.sub(lambda m: m.group(0).replace("—", "\x00"), linha)
    else:
        marcada = linha

    # travessão colado em asterisco de ênfase (`*— vaga reservada —*`): preserva
    marcada = re.sub(r"\*—", "*\x00", marcada)
    marcada = re.sub(r"—\*", "\x00*", marcada)

    # cabeçalho de catálogo: preserva o primeiro travessão
    m = CABECALHO.match(marcada)
    if m:
        corte = m.end()
        cabeca, resto = marcada[:corte], marcada[corte:]
        cabeca = cabeca.replace("—", "\x00")
        marcada = cabeca + resto

    n = marcada.count("—")
    if n == 0:
        return marcada.replace("\x00", "—"), 0

    # par de travessões no mesmo trecho vira parênteses
    while marcada.count("—") >= 2:
        i = marcada.index("—")
        j = marcada.index("—", i + 1)
        meio = marcada[i + 1:j]
        # só vira parêntese se o miolo for curto o bastante pra ser um aparte
        if len(meio) < 90 and "." not in meio:
            marcada = (marcada[:i].rstrip() + " (" + meio.strip() + ") "
                       + marcada[j + 1:].lstrip())
        else:
            break

    # travessão solto restante vira pontuação corrente
    def troca(m):
        antes = marcada[:m.start()]
        depois = marcada[m.end():]
        return escolhe(depois, ":" in antes)

    while True:
        m = re.search(r"\s*—\s*", marcada)
        if not m:
            break
        marcada = marcada[:m.start()].rstrip() + troca(m) + marcada[m.end():].lstrip()

    marcada = re.sub(r"\s+([,.;:])", r"\1", marcada)
    marcada = re.sub(r"\(\s+", "(", marcada)
    marcada = re.sub(r"\s+\)", ")", marcada)
    marcada = re.sub(r"  +$", "", marcada)
    return marcada.replace("\x00", "—"), n


def main(paths):
    total = 0
    dentro_de_codigo = False
    for p in paths:
        linhas = open(p, encoding="utf-8").read().split("\n")
        saida, mudou = [], 0
        for linha in linhas:
            if linha.strip().startswith("```"):
                dentro_de_codigo = not dentro_de_codigo
            if dentro_de_codigo:
                saida.append(linha)
                continue
            nova, n = converte_linha(linha)
            saida.append(nova)
            mudou += n
        open(p, "w", encoding="utf-8").write("\n".join(saida))
        total += mudou
        print(f"  {p.split('/')[-1]:<34} {mudou}")
    print(f"total trocado: {total}")


if __name__ == "__main__":
    main(sys.argv[1:])
