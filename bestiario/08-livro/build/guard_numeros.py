#!/usr/bin/env python3
"""
Projeto - M · Manual da Guilda
Trava de número para passada de texto: compara duas versões do mesmo arquivo e
mostra toda notação de dado, porcentagem, inteiro e numeral por extenso que mudou.

Diferença não é erro por si só — um título que perde "As duas" perde um numeral.
Mas cada diferença tem que ser explicada antes de aplicar a mudança.

    python3 build/guard_numeros.py antes.md depois.md
"""
import collections
import re
import sys

NUM = re.compile(r"\d+\s*[dD]\s*\d+|\d+[,.]\d+\s*%?|\d+\s*%|[+−-]?\d+")
EXTENSO = re.compile(
    r"\b(um|uma|dois|duas|tr[êe]s|quatro|cinco|seis|sete|oito|nove|dez|onze|doze|treze|"
    r"catorze|quinze|dezesseis|dezessete|dezoito|dezenove|vinte|trinta|quarenta|"
    r"cinquenta|cem|cento|d[úu]zia|meio|metade|dobro)\b",
    re.I,
)


def conta(caminho):
    texto = open(caminho, encoding="utf-8").read()
    numeros = collections.Counter(re.sub(r"\s+", "", t) for t in NUM.findall(texto))
    palavras = collections.Counter(p.lower() for p in EXTENSO.findall(texto))
    return numeros, palavras


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    a_num, a_pal = conta(sys.argv[1])
    b_num, b_pal = conta(sys.argv[2])

    total = 0
    for rotulo, antes, depois in (
        ("NOTAÇÃO E NÚMERO", a_num, b_num),
        ("NUMERAL POR EXTENSO", a_pal, b_pal),
    ):
        difs = sorted(
            (k, antes[k], depois[k])
            for k in set(antes) | set(depois)
            if antes[k] != depois[k]
        )
        total += len(difs)
        if not difs:
            print(f"{rotulo}: idêntico ({sum(antes.values())} ocorrências)")
            continue
        print(f"{rotulo}: {len(difs)} diferença(s)")
        for chave, x, y in difs:
            seta = "sumiu" if y < x else "apareceu"
            print(f"   {chave!r:16} antes={x:<4} depois={y:<4} {seta}")

    print()
    if total:
        print(f"  {total} diferença(s). Explique cada uma antes de aplicar.")
        sys.exit(1)
    print("  Nenhum número mudou.")


if __name__ == "__main__":
    main()
