# -*- coding: utf-8 -*-
"""Classifica TODA acao de Recarga do SRD 5.2 (open5e doc srd-2024) em area / alvo unico / sem alvo.
Duas passadas: rotulo A MAO (revisado item por item) e um detector por palavra-chave.
Se os dois discordarem em qualquer linha, o script GRITA. Numero nao sai de estimativa."""
import json, re, statistics
import os
# ⚠ o corpus mora ao lado DESTE arquivo, e nao no diretorio de quem chama. Ate 11/09/2026
#   estes abriam por nome nu: rodados da raiz do Bestiario eles achavam (ou criavam) uma
#   copia de la, e foi assim que os seis corpora acabaram morando em duas casas.
AQUI = os.path.dirname(os.path.abspath(__file__))
C = lambda n: os.path.join(AQUI, n)


d = json.load(open(C('srd-2024.json')))

# rotulo a mao, revisado nos 86 textos. chave = (monstro, acao)
MAO = {
 ('Air Elemental','Whirlwind'):'UNICO',
 ('Ape','Rock'):'UNICO',
 ('Ettercap','Web Strand'):'UNICO',
 ('Ghost','Possession'):'UNICO',
 ('Giant Spider','Web'):'UNICO',
 ('Incubus','Nightmare'):'UNICO',
 ('Minotaur of Baphomet','Gore'):'UNICO',
 ('Roc','Swoop'):'UNICO',
 ('Sea Hag','Death Glare'):'UNICO',
 ('Stone Giant','Deflect Missile'):'UNICO',
 ('Swarm of Ravens','Cacophony'):'UNICO',
 ('Vampire','Charm'):'UNICO',
 ('Blink Dog','Teleport (Recharge 4-6)'):'SEM_ALVO',
 ('Clay Golem','Hasten'):'SEM_ALVO',
 ('Frost Giant','War Cry'):'SEM_ALVO',
 ('Marilith','Teleport'):'SEM_ALVO',
}
# feitico conjurado cuja area nao aparece no texto do statblock -> conferido no texto do feitico
FEITICO_AREA = {
 ('Drider','Magic of the Spider Queen'):'Darkness (esfera 15 pes) / Faerie Fire (cubo 20) / Web (cubo 20)',
 ('Ice Devil','Ice Wall'):'Wall of Ice — parede, efeito de area',
 ('Pit Fiend','Hellfire Spellcasting'):'Fireball x2 (esfera 20 pes)',
 ('Stone Golem','Slow'):'Slow (cubo 40 pes, ate seis criaturas)',
}
FEITICO_UNICO = {('Vampire','Charm'):'Charm Person — uma criatura'}

MARCA_AREA = re.compile(r'each creature|each enemy|Cone|Line\b|Emanation|Sphere|Cylinder|Cube|'
                        r'each object|Each creature', re.I)
MARCA_UNICO = re.compile(r'\bone (creature|Humanoid|Medium|Large|Frightened|target)|'
                         r'Melee Attack Roll|Ranged Attack Roll', re.I)

rows = []
for m in d:
    for a in m['actions'] or []:
        ul = a.get('usage_limits') or {}
        if ul.get('type') not in ('RECHARGE','RECHARGE_ON_ROLL'):
            continue
        desc = (a['desc'] or '').replace('\n',' ')
        k = (m['name'], a['name'])
        # detector automatico
        if k in FEITICO_AREA:   auto = 'AREA'
        elif k in FEITICO_UNICO: auto = 'UNICO'
        elif MARCA_AREA.search(desc):  auto = 'AREA'
        elif MARCA_UNICO.search(desc): auto = 'UNICO'
        else: auto = 'SEM_ALVO'
        mao = MAO.get(k, 'AREA')
        rows.append(dict(mon=m['name'], cr=m['challenge_rating'], acao=a['name'],
                         tipo=a.get('action_type'), param=ul.get('param'),
                         desc=desc, auto=auto, mao=mao))

# --- os dois casos em que mao e detector discordam DE PROPOSITO, com o motivo escrito ---
AMBIGUO = {
 ('Frost Giant','War Cry'): "detector le 'one creature' e chuta UNICO. Mas o efeito e Temp HP + "
   "vantagem num ALIADO — nao mira inimigo. Fica SEM_ALVO (nao e golpe).",
 ('Roc','Swoop'): "detector nao acha frase de alvo e chuta SEM_ALVO. Mas ela solta UMA criatura "
   "agarrada — mira um inimigo so. Fica UNICO (movimento, sem rolagem de dano).",
}
# --- o grito de discordancia ---
disc = [r for r in rows if r['auto'] != r['mao'] and (r['mon'],r['acao']) not in AMBIGUO]
print("casos ambiguos resolvidos a mao, com motivo:", len(AMBIGUO))
for k,v in AMBIGUO.items(): print("  *", k[0],'-',k[1],'->',v)
print("TOTAL de rotulos de Recarga no SRD 5.2 (open5e srd-2024):", len(rows))
print("DISCORDANCIA entre mao e detector:", len(disc))
for r in disc:
    print("  !!", r['mon'],'|',r['acao'],'| mao',r['mao'],'auto',r['auto'],'|',r['desc'][:150])
assert not disc, "mao e detector discordam — nao publique numero"

def conta(pred, base=rows):
    return [r for r in base if pred(r)]

area  = conta(lambda r: r['mao']=='AREA')
unico = conta(lambda r: r['mao']=='UNICO')
sem   = conta(lambda r: r['mao']=='SEM_ALVO')
print(f"\nAREA {len(area)} | ALVO UNICO {len(unico)} | SEM ALVO (self/buff/movimento) {len(sem)}")
print(f"soma {len(area)+len(unico)+len(sem)} == {len(rows)}")

# so as que miram alguem
mira = area + unico
print(f"\nSO AS QUE MIRAM ALGUEM: {len(area)} de {len(mira)} sao AREA = {100*len(area)/len(mira):.1f}%")
print(f"                        {len(unico)} de {len(mira)} sao ALVO UNICO = {100*len(unico)/len(mira):.1f}%")

# recorte que interessa: a ACAO principal (a Recarga do Projeto-M come a Acao, nao a bonus)
for t in ['ACTION','BONUS_ACTION','REACTION']:
    b = conta(lambda r: r['tipo']==t)
    ba = conta(lambda r: r['mao']=='AREA', b); bu = conta(lambda r: r['mao']=='UNICO', b)
    bs = conta(lambda r: r['mao']=='SEM_ALVO', b)
    print(f"  {t:14s} n={len(b):3d}  area {len(ba):3d}  unico {len(bu):2d}  sem alvo {len(bs)}")
acoes = conta(lambda r: r['tipo']=='ACTION')
aa = conta(lambda r: r['mao']=='AREA', acoes)
print(f"\n>> SO A ACAO PRINCIPAL: {len(aa)} de {len(acoes)} sao AREA = {100*len(aa)/len(acoes):.1f}%")

# a janela de recarga
from collections import Counter
print("\njanela:", dict(Counter(f"{r['param']}-6" for r in rows)))

# CR: area vs unico
print(f"\nCR medio  AREA {statistics.mean(r['cr'] for r in area):.2f}  (mediana {statistics.median(r['cr'] for r in area):.2f})")
print(f"CR medio UNICO {statistics.mean(r['cr'] for r in unico):.2f}  (mediana {statistics.median(r['cr'] for r in unico):.2f})")
print(f"CR maximo  AREA {max(r['cr'] for r in area)}   CR maximo UNICO {max(r['cr'] for r in unico)}")

# dano: extrai o maior numero de dano medio citado no texto
def dano(desc):
    n = [int(x) for x in re.findall(r'(\d+) \(\d+d\d+(?:\s*\+\s*\d+)?\)', desc)]
    return max(n) if n else 0
print("\n--- AS 12 DE ALVO UNICO, uma por uma ---")
for r in sorted(unico, key=lambda r: -r['cr']):
    print(f"CR {r['cr']:<5} | {r['mon']:22s} | {r['acao']:20s} | {r['tipo']:12s} | rec {r['param']}-6 | dano {dano(r['desc'])}")
sem_dano = [r for r in unico if dano(r['desc'])==0]
print(f"\nDAS 12 DE ALVO UNICO, {len(sem_dano)} nao rolam dano nenhum:", ", ".join(r['mon']+' '+r['acao'] for r in sem_dano))
print(f"maior dano de uma Recarga de ALVO UNICO em todo o SRD 5.2: {max(dano(r['desc']) for r in unico)}")
print(f"maior dano de uma Recarga de AREA:                          {max(dano(r['desc']) for r in area)}")
top = max(area, key=lambda r: dano(r['desc']))
print("   (essa e", top['mon'], '-', top['acao'], ')')

json.dump(rows, open(C('classificado-srd2024.json'),'w'))
