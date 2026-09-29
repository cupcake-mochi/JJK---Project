# -*- coding: utf-8 -*-
"""Pergunta 4 do corte 3 (28/09/2026): quem tem Recarga paga no golpe, na vida ou em nada?

Mede nos 331 blocos do SRD 5.2 (D&D 2024), lidos pela API aberta do Open5e
(https://api.open5e.com/v2/creatures/?document__key=srd-2024, CC-BY; o arquivo baixado fica no HD,
agentes-2026-09-27/bestiario-leva-2/srd2024-criaturas.json). Compara, no MESMO ND, o monstro com
uma acao de Recarga e o monstro sem nenhuma: a vida, a CA e o dano da rotina de ataque (o Multiattack,
ou o melhor ataque sozinho), se tudo acerta. A Recarga, as magias e as acoes lendarias ficam fora da
rotina: a pergunta e se o golpe de quem tem Recarga e menor.
"""
import json, re, sys, os, math
ARQ = '/media/mizuki/HD Externo II/Claude/agentes-2026-09-27/bestiario-leva-2/srd2024-criaturas.json'
cs = json.load(open(ARQ, encoding='utf-8'))
NUM = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'a': 1, 'an': 1}

def media_ataque(a):
    t = a['attacks'][0]
    d = lambda n, tipo: (n or 0) * (int(tipo[1:]) + 1) / 2 if tipo else 0
    return d(t['damage_die_count'], t['damage_die_type']) + (t['damage_bonus'] or 0) + \
           d(t.get('extra_damage_die_count'), t.get('extra_damage_die_type')) + (t.get('extra_damage_bonus') or 0)

def rotina(c):
    """O dano por rodada da rotina de ataque, se tudo acerta; None se nao ha ataque."""
    ataques = {a['name'].lower(): media_ataque(a) for a in c['actions']
               if a['action_type'] == 'ACTION' and a['attacks'] and not a['usage_limits']}
    if not ataques: return None
    multi = [a for a in c['actions'] if a['name'].startswith('Multiattack')]
    if not multi: return max(ataques.values())
    txt = multi[0]['desc'].lower()
    total = 0; achou = False
    for m in re.finditer(r'\b(one|two|three|four|five|six|seven|eight|an?)\s+([a-z\' ]+?)\s+attacks?\b', txt):
        n = NUM[m.group(1)]; nome = m.group(2).strip()
        cand = [v for k, v in ataques.items() if k in nome or nome in k]
        if not cand:
            # "makes two attacks, using X or Y in any combination": o maior dos citados
            cit = [v for k, v in ataques.items() if k in txt]
            cand = cit or list(ataques.values())
        total += n * max(cand); achou = True
    return total if achou else max(ataques.values())

def tem_recarga(c):
    return any(a['action_type'] == 'ACTION' and a['usage_limits'] and a['usage_limits'].get('type') == 'RECHARGE_ON_ROLL'
               and re.search(r'damage', a['desc']) for a in c['actions'])

def so_ataques(c):
    """Sem Recarga, sem Spellcasting e sem outra acao de dano por Teste de Resistencia: so ataque."""
    for a in c['actions']:
        if a['action_type'] != 'ACTION': continue
        if a['name'].startswith('Spellcasting') or a['usage_limits']: return False
        if not a['attacks'] and re.search(r'saving throw', a['desc'], re.I) and re.search(r'damage', a['desc']): return False
    return True

linhas = []
for c in cs:
    r = rotina(c)
    if r is None: continue
    grupo = True if tem_recarga(c) else (False if so_ataques(c) else None)   # None: fica fora da comparacao
    if grupo is None: continue
    linhas.append((c['challenge_rating'], grupo, c['hit_points'], c['armor_class'], r, c['name']))

# regressao: o Adult Red Dragon conferido pelo agente A contra o PDF oficial (p. 318): tres Rend de 13 + 5
drag = [l for l in linhas if l[5] == 'Adult Red Dragon'][0]
ok = (drag[1], drag[2], drag[3], drag[4]) == (True, 256, 19, 3 * (13.5 + 5))
print(f'[{"x" if ok else "!"}] Adult Red Dragon: recarga={drag[1]} vida={drag[2]} CA={drag[3]} rotina={drag[4]}')
if not ok: sys.exit(1)

print('\n"sem" = so ataques: sem Recarga, sem Spellcasting e sem outra acao de dano por TR.')
print('ND   n com / sem   vida com/sem   CA com/sem   rotina com/sem')
razoes = {'vida': [], 'CA': [], 'rotina': []}
for nd in sorted({l[0] for l in linhas}):
    com = [l for l in linhas if l[0] == nd and l[1]]; sem = [l for l in linhas if l[0] == nd and not l[1]]
    if len(com) < 2 or len(sem) < 2: continue
    med = lambda g, i: sum(x[i] for x in g) / len(g)
    peso = min(len(com), len(sem))
    for nome, i in (('vida', 2), ('CA', 3), ('rotina', 4)):
        razoes[nome].append((med(com, i) / med(sem, i), peso, med(com, i) - med(sem, i)))
    print(f'{nd:>4}  {len(com):>3} / {len(sem):<3}   {med(com,2):>6.1f} / {med(sem,2):<6.1f} '
          f'{med(com,3):>5.1f} / {med(sem,3):<5.1f}  {med(com,4):>6.1f} / {med(sem,4):<6.1f}')
print('\nRazao media (com Recarga / sem), pesada pelo menor grupo de cada ND (geometrica):')
for nome, rs in razoes.items():
    w = sum(p for _, p, _ in rs)
    g = math.exp(sum(p * math.log(r) for r, p, _ in rs) / w)
    extra = f'  (diferenca media {sum(p * d for _, p, d in rs) / w:+.2f})' if nome == 'CA' else ''
    print(f'  {nome:<7} x{g:.3f}  em {len(rs)} NDs{extra}')
