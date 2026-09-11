# -*- coding: utf-8 -*-
"""DRAW STEEL — a Villain Action e o equivalente da Recarga (relogio proprio: 1 por rodada,
na rodada 1, 2 e 3 do combate). Conta TODAS elas e pergunta: quantas tocam MAIS DE UMA criatura?
Fonte: SteelCompendium/data-md, tarball de main, Bestiary/Monsters/**/Statblocks/*.md"""
import re, glob, os, json
from collections import Counter

# ⚠ o caminho sai do arquivo, e nao do diretorio de quem chama: rodado de `fila/` o glob
#   relativo devolvia ZERO e o script morria num ZeroDivisionError la embaixo.
AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(AQUI, 'dados-recarga-area', 'data-md-main')
arqs = sorted(set(glob.glob(os.path.join(BASE, 'Bestiary/Monsters/**/*.md'), recursive=True)))
if not arqs:
    raise SystemExit('DONO SUMIU: nao achei statblock nenhum em %s' % BASE)
VA = re.compile(r'\*\*(.+?)\s*\(Villain Action (\d)\)\*\*')
ALVO = re.compile(r'🎯\s*\**([^*|]+)')
DIST = re.compile(r'📏\s*\**([^*|]+)')

vas, vistos = [], set()
for f in arqs:
    if '/Statblocks/' not in f and '/Retainers/' not in f: continue   # ignora Index e o agregado
    txt = open(f, encoding='utf-8').read()
    mon = os.path.basename(f)[:-3]
    for bloco in txt.split('<!-- -->'):
        m = VA.search(bloco)
        if not m: continue
        k = (mon, m.group(1).strip(), m.group(2))
        if k in vistos: continue
        vistos.add(k)
        vas.append(dict(mon=mon, nome=m.group(1).strip(), n=int(m.group(2)),
            alvo=(ALVO.search(bloco).group(1).strip() if ALVO.search(bloco) else ''),
            dist=(DIST.search(bloco).group(1).strip() if DIST.search(bloco) else ''),
            bloco=bloco.strip()))

# as 17 de alvo "Special", resolvidas A MAO lendo o Effect de cada uma
MAO = {
 ('Angulotl Daybringer','New Dawn'):('NENHUM','invoca 4 pollywogs'),
 ('Angulotl Daybringer','It Is Day'):('MAIS_DE_UM','cada inimigo do mapa inteiro'),
 ('Ashen Hoarder','Mobile Mine Field'):('MAIS_DE_UM','6 minas num cubo 10'),
 ('Aurumvas','Hostile Acquisition'):('NENHUM','mira 3 TESOUROS, nao criatura'),
 ('Gloom Dragon','Absence of All Light'):('MAIS_DE_UM','mapa inteiro, ilusoes'),
 ('Thorn Dragon','Malign Thicket'):('MAIS_DE_UM','cobre todas as superficies do mapa'),
 ('Dwarf Marauder','Test Your Metal!'):('NENHUM','cria 3 objetos'),
 ('Shadow Elf Eclipse','From the Shadows'):('NENHUM','invoca 1 + aliados ganham free strike'),
 ('Fire Giant Chief','Burning Legion'):('NENHUM','invoca 5 fireballers'),
 ('Gnoll Carnage','Call Up From the Abyss'):('NENHUM','invoca 4 hienas'),
 ('Goblin Monarch','Kill!'):('MAIS_DE_UM','cada inimigo do encontro'),
 ('Kingfissure Worm','Earth Breach'):('MAIS_DE_UM','cada criatura no caminho'),
 ('Kobold Centurion','Firetail Pilum'):('MAIS_DE_UM','cada criatura por onde passa'),
 ('Medusa','Stone Puppets'):('MAIS_DE_UM','cada estatua/criatura no burst 10'),
 ('Time Raider Tyrannis','Armageddon'):('MAIS_DE_UM','minas em cada quadrado do burst 5'),
 ('Voiceless Talker Evolutionist','Release the Thralls'):('NENHUM','invoca 8 lacaios'),
 ('Strategos Alkestis','Send in the Second Wave'):('NENHUM','invoca reforcos'),
}
MUITOS = re.compile(r'each |all |every |two |three |four |five |\d+ creatures|\d+ enemies', re.I)
FORMA  = re.compile(r'burst|cube|line|aura|wall|\d+\s*[x×]\s*\d+', re.I)
UM     = re.compile(r'^one (creature|enemy|ally|object|creature or object|target)\b', re.I)

for v in vas:
    k=(v['mon'],v['nome'])
    if k in MAO: v['cls'], v['nota'] = MAO[k]
    elif UM.match(v['alvo']):                 v['cls'],v['nota']='UM_SO', v['alvo']
    elif v['alvo'].lower()=='self' and not FORMA.search(v['dist']): v['cls'],v['nota']='NENHUM','so ele mesmo'
    elif MUITOS.search(v['alvo']) or FORMA.search(v['dist']):       v['cls'],v['nota']='MAIS_DE_UM', v['alvo']
    else: v['cls'],v['nota']='???', v['alvo']

c=Counter(v['cls'] for v in vas)
print(f"VILLAIN ACTIONS no Draw Steel: {len(vas)}, em {len(set(v['mon'] for v in vas))} criaturas")
print("nao classificadas:", c['???'])
for v in vas:
    if v['cls']=='???': print("  ???",v['mon'],'|',v['nome'],'| dist',repr(v['dist']),'alvo',repr(v['alvo']))
assert c['???']==0, "sobrou villain action sem classe — nao publique numero"
print(f"\n  MAIS DE UMA criatura : {c['MAIS_DE_UM']}")
print(f"  EXATAMENTE UMA       : {c['UM_SO']}")
print(f"  NENHUMA (self/invoca): {c['NENHUM']}")
print(f"  soma {sum(c.values())} == {len(vas)}")
mira = c['MAIS_DE_UM'] + c['UM_SO']
print(f"\n>> DAS QUE MIRAM ALGUEM: {c['MAIS_DE_UM']} de {mira} pegam MAIS DE UM = {100*c['MAIS_DE_UM']/mira:.1f}%")
print(f">>                       {c['UM_SO']} de {mira} pegam UM SO = {100*c['UM_SO']/mira:.1f}%")
print(f">> SOBRE O TOTAL de {len(vas)}: alvo unico = {100*c['UM_SO']/len(vas):.1f}%")
print("\n--- AS DE ALVO UNICO, todas ---")
for v in [x for x in vas if x['cls']=='UM_SO']:
    dano = re.findall(r'(\d+)\s+\w+ damage', v['bloco'])
    print(f"  {v['mon']:30s} | VA{v['n']} {v['nome']:28s} | {v['dist']:12s} | {v['alvo']:20s} | dano citado: {dano if dano else 'NENHUM'}")
json.dump(vas, open(os.path.join(AQUI, 'ds-vas2.json'), 'w'))
