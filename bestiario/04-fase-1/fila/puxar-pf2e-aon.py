import json, subprocess
import os
# ⚠ o corpus mora ao lado DESTE arquivo, e nao no diretorio de quem chama. Ate 11/09/2026
#   estes abriam por nome nu: rodados da raiz do Bestiario eles achavam (ou criavam) uma
#   copia de la, e foi assim que os seis corpora acabaram morando em duas casas.
AQUI = os.path.dirname(os.path.abspath(__file__))
C = lambda n: os.path.join(AQUI, n)

def es(body, path="/aon/_search"):
    p=subprocess.run(["curl","-s","-m","90","-H","Content-Type: application/json","-d",json.dumps(body),
                      "https://elasticsearch.aonprd.com"+path],capture_output=True,text=True)
    try: return json.loads(p.stdout)
    except Exception: print("ERRO:", p.stdout[:400]); raise
Q={"bool":{"must":[{"match_phrase":{"text":"again for 1d4 rounds"}},{"term":{"category":"creature"}}]}}
todas, after = [], None
while True:
    b={"size":200,"_source":["name","level","text","source","url"],"sort":[{"_doc":"asc"}],"query":Q}
    if after: b["search_after"]=after
    d=es(b); h=d['hits']['hits']
    if not h: break
    todas += [x['_source'] for x in h]; after=h[-1]['sort']
    print("  baixadas",len(todas),"/",d['hits']['total']['value'], flush=True)
    if len(h)<200: break
json.dump(todas, open(C('pf2e-recarga.json'),'w'))
print("SALVO",len(todas))
