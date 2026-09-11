#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Puxa do AoN os campos de TAMANHO das criaturas do PF2e — size, AC, HP e atributos.
Mesmo endpoint que o `puxar-pf2e-aon.py` ja usa."""
import json
import os
# ⚠ o corpus mora ao lado DESTE arquivo, e nao no diretorio de quem chama. Ate 11/09/2026
#   estes abriam por nome nu: rodados da raiz do Bestiario eles achavam (ou criavam) uma
#   copia de la, e foi assim que os seis corpora acabaram morando em duas casas.
AQUI = os.path.dirname(os.path.abspath(__file__))
C = lambda n: os.path.join(AQUI, n)

import subprocess


def es(body, path="/aon/_search"):
    p = subprocess.run(["curl", "-s", "-m", "90", "-H", "Content-Type: application/json",
                        "-d", json.dumps(body), "https://elasticsearch.aonprd.com" + path],
                       capture_output=True, text=True)
    try:
        return json.loads(p.stdout)
    except Exception:
        print("ERRO:", p.stdout[:400])
        raise


CAMPOS = ["name", "level", "size", "ac", "hp", "strength", "dexterity", "constitution",
          "intelligence", "wisdom", "charisma", "creature_family", "rarity", "type"]
Q = {"bool": {"must": [{"term": {"category": "creature"}}]}}
todas, after = [], None
while True:
    b = {"size": 500, "_source": CAMPOS, "sort": [{"_doc": "asc"}], "query": Q}
    if after:
        b["search_after"] = after
    d = es(b)
    h = d['hits']['hits']
    if not h:
        break
    todas += [x['_source'] for x in h]
    after = h[-1]['sort']
    print("  baixadas", len(todas), "/", d['hits']['total']['value'], flush=True)
    if len(h) < 500:
        break
json.dump(todas, open(C('pf2e-tamanho.json'), 'w'))
print("SALVO", len(todas))
