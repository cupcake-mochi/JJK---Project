"""Compara os 'fatos numéricos' da R53 que o guia usa (sha 7311979b…) com a R60.
Fato numérico = dado (NdM±k), CD, custo em PE, distância em m, modificador ±N, multiplicador N×, fração N/M e porcentagem.
Uso: python3 -I r53-para-r60.py R53.md R60.md"""
import re,sys,collections,hashlib
pat=re.compile(r"\b\d+d\d+(?:\s*[+−-]\s*\d+)?|\bCD\s*\d+|\b\d+\s*PE\b|\b\d+(?:,\d+)?\s*m\b|[+−-]\d+\b|\b\d+\s*×|\b\d+/\d+\b|\d+%")
def fatos(p): return collections.Counter(m.group(0).replace(' ','') for m in pat.finditer(open(p,encoding='utf-8').read()))
for p in sys.argv[1:3]: print(p, hashlib.sha256(open(p,'rb').read()).hexdigest()[:16])
a,b=fatos(sys.argv[1]),fatos(sys.argv[2])
print("fatos da R53 que sumiram na R60:", dict(a-b) or "nenhum")
print("fatos que só a R60 tem (exemplos e âncoras novas):", sum((b-a).values()))
