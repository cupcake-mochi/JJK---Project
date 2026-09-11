import json, re
import os
# ⚠ o corpus mora ao lado DESTE arquivo, e nao no diretorio de quem chama. Ate 11/09/2026
#   estes abriam por nome nu: rodados da raiz do Bestiario eles achavam (ou criavam) uma
#   copia de la, e foi assim que os seis corpora acabaram morando em duas casas.
AQUI = os.path.dirname(os.path.abspath(__file__))
C = lambda n: os.path.join(AQUI, n)

d = json.load(open(C('srd-2024.json')))
rows = []
for m in d:
    for a in m['actions'] or []:
        ul = a.get('usage_limits') or {}
        if ul.get('type') in ('RECHARGE', 'RECHARGE_ON_ROLL'):
            rows.append((m['name'], m['challenge_rating'], a['name'], a.get('action_type'),
                         ul.get('param'), (a['desc'] or '').replace('\n',' ')))
print("TOTAL:", len(rows))
for i, r in enumerate(rows, 1):
    print(f"--- {i} | {r[0]} (CR {r[1]}) | {r[2]} | {r[3]} | recharge {r[4]}-6")
    print("   ", r[5][:420])
