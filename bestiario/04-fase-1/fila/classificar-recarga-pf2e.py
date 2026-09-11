# -*- coding: utf-8 -*-
"""PATHFINDER 2e — o equivalente da Recarga e "can't use X again for 1d4 rounds".
⚠ O texto do AoN vem CONCATENADO (statblock inteiro num campo so), entao o recorte do bloco
da habilidade e' aproximado. Trato isso assim: janela dos DOIS lados do gatilho (a area do
sopro do dragao vem DEPOIS da frase de recarga), e conferencia a mao de tudo que nao for AREA.
Fonte: Archives of Nethys, elasticsearch.aonprd.com, category=creature."""
import json, re
import os
# ⚠ o corpus mora ao lado DESTE arquivo, e nao no diretorio de quem chama. Ate 11/09/2026
#   estes abriam por nome nu: rodados da raiz do Bestiario eles achavam (ou criavam) uma
#   copia de la, e foi assim que os seis corpora acabaram morando em duas casas.
AQUI = os.path.dirname(os.path.abspath(__file__))
C = lambda n: os.path.join(AQUI, n)

from collections import Counter
cs = json.load(open(C('pf2e-recarga.json')))
CUSTO = re.compile(r'(Single Action|Two Actions|Three Actions|Free Action|Reaction)\b')
GATILHO = re.compile(r"(can't|cannot)[^.]{0,130}again for 1d4 rounds")

habs, vistos = [], set()
for c in cs:
    t=(c.get('text') or '').replace('’',"'")
    for g in GATILHO.finditer(t):
        antes=t[:g.start()]; ms=list(CUSTO.finditer(antes))
        if not ms: continue
        ini=ms[-1].start()
        # a proxima habilidade comeca no proximo marcador de custo DEPOIS do gatilho
        prox=CUSTO.search(t, g.end())
        fim = prox.start() if prox else min(len(t), g.end()+700)
        bloco = t[ini:fim]
        nome_m = re.search(r"can't use ([A-Z][\w' \-]{2,40}?) again", g.group(0)) \
              or re.search(r"can't ([\w' \-]{2,40}?) again", g.group(0))
        nome = nome_m.group(1).strip() if nome_m else '(sem nome no texto)'
        k=(c['name'], nome, bloco[:80])
        if k in vistos: continue
        vistos.add(k)
        habs.append(dict(mon=c['name'], nv=c.get('level'), nome=nome, bloco=bloco))
print("habilidades com recarga '1d4 rounds':", len(habs), "| criaturas:", len(set(h['mon'] for h in habs)))
# dedup por (nome da criatura, nome da habilidade) -> reimpressao nao conta duas vezes
ded={}
for h in habs: ded.setdefault((h['mon'],h['nome']), h)
habs=list(ded.values())
print("apos dedup por (criatura, habilidade):", len(habs))

AREA=re.compile(r'\bcone\b|\bburst\b|\bemanation\b|-foot line|\bline\b|all creatures|each creature|'
                r'each enemy|in the area|every creature|all other|each other|aura\b|'
                r'creatures within|creatures in|\bcube\b|\bcylinder\b|creatures who|creatures that',re.I)
UM  =re.compile(r'a single foe|one creature|single creature|a creature within|one enemy|one target|'
                r'\bStrike\b|the target\b|one ally|an ally',re.I)
REACAO=re.compile(r'^(Reaction|Free Action)\b|Trigger ',re.I)
AUTO=re.compile(r'teleports to|becomes invisible|temporary Hit Points|Flies up to|assume a physical form|'
                r'crumbles into the ground|counteract|improves its result|possesses a|Requirements',re.I)
for h in habs:
    b=h['bloco']
    if AREA.search(b): h['cls']='AREA'
    elif not UM.search(b): h['cls']='???'
    elif REACAO.search(b) or AUTO.search(b): h['cls']='UNICO_NAO_GOLPE'
    else: h['cls']='UNICO_GOLPE'
c=Counter(h['cls'] for h in habs)
print("\n ",dict(c))
U=c['UNICO_GOLPE']+c['UNICO_NAO_GOLPE']; mira=c['AREA']+U
print(f">> AREA {c['AREA']} de {len(habs)} = {100*c['AREA']/len(habs):.1f}%")
print(f">> das que deu pra classificar: {c['AREA']} de {mira} = {100*c['AREA']/mira:.1f}% AREA")
print(f">> alvo unico total {U} = {100*U/mira:.1f}%   (GOLPE {c['UNICO_GOLPE']}, "
      f"nao-golpe/reacao/auto {c['UNICO_NAO_GOLPE']})")
print(f"\n--- ALVO UNICO que E GOLPE ({c['UNICO_GOLPE']}) ---")
for h in habs:
    if h['cls']=='UNICO_GOLPE': print(f"  nv{h['nv']:<4}{h['mon']:28s}| {h['nome'][:30]:30s}| {h['bloco'][:160]}")
print(f"\n--- ALVO UNICO que NAO e golpe ({c['UNICO_NAO_GOLPE']}) ---")
for h in habs:
    if h['cls']=='UNICO_NAO_GOLPE': print(f"  nv{h['nv']:<4}{h['mon']:26s}| {h['nome'][:28]:28s}| {h['bloco'][:110]}")
print(f"\n--- ??? ({c['???']}) ---")
for h in habs:
    if h['cls']=='???': print(f"  nv{h['nv']:<4}{h['mon']:28s}| {h['nome'][:30]:30s}| {h['bloco'][:150]}")
json.dump(habs, open(C('pf2e-habs2.json'),'w'))
