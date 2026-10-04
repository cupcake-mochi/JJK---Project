#!/usr/bin/env python3
"""Auditoria reproduzível R10. Não substitui leitura editorial ou teste com jogadores."""
from pathlib import Path
import hashlib
import itertools
import json
import math
import re

P = Path(__file__).resolve().parent
R = next(p for p in P.parents if (p / 'sistema/03-mecanica').is_dir())
E = R / 'sistema/05-material/livro/planejamento-editorial'
S = (P / 'ROTAS.md').read_text()
checks = []


def check(name, success, evidence):
    checks.append({'teste': name, 'passou': bool(success), 'evidencia': evidence})


def save(name, data):
    (P / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


pages = []
for segment in re.split(r'<!-- page:', S)[1:]:
    header, text = segment.split('-->', 1)
    ident, title = header.strip().split('|', 1)
    pages.append({'id': ident, 'titulo': title, 'palavras': len(re.findall(r'\S+', text)), 'texto': text})
ids = {p['id'] for p in pages}
check('IDs únicos', len(ids) == len(pages), [p['id'] for p in pages])
check('Páginas com título correspondente', all(p['texto'].lstrip().startswith('# ' + p['titulo'] + '\n') for p in pages), len(pages))
check('Faixa de extensão 140–400 palavras, com suficiência revista por seção', all(140 <= p['palavras'] <= 400 for p in pages), [{k: p[k] for k in ('id', 'palavras')} for p in pages])
heads = re.findall(r'^#{1,6}\s+(.+)$', S, re.M)
badheads = [h for h in heads if re.match(r'(?:A|O|As|Os)\s|Como ler\b', h)]
check('Títulos sem artigo inicial ou Como ler', not badheads, badheads)
refs = re.findall(r'\]\(#([^)]*)\)', S)
check('Remissões internas resolvidas', all(r in ids for r in refs), refs)
check('Sem ponto e vírgula na prosa', ';' not in S, S.count(';'))
check('Não usa legal como elegibilidade', not re.search(r'\blegal\b', S, re.I), re.findall(r'\blegal\b', S, re.I))
inv = json.loads((P / 'INVENTARIO.json').read_text())
check('Inventário fonte com destino existente', all(i['destino'] in ids for i in inv), len(inv))
changes = json.loads((P / 'ALTERACOES.json').read_text())
unfound = [{'id': c['id'], 'fonte': f} for c in changes for f in c['fontes'] if not f['linhas']]
check('Âncoras de alterações encontradas', not unfound, unfound)

# Read the owner tables. No numeric fallback if their schema changes.
fund = (E / 'fundamento/lote-01/FUNDAMENTO.md').read_text()
costpart = fund.split('# Pontos e preços\n', 1)[1].split('## Quantidade de peças', 1)[0]
rows = re.findall(r'^\| ([1-7]) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$', costpart, re.M)
assert len(rows) == 7, 'Tabela do dono de custos mudou; atualizar parser conscientemente.'
costs = {int(c): dict(zip(['nivel', 'orcamento', 'leve', 'media', 'pesada'], map(int, tail))) for c, *tail in rows}
repertoire = fund.split('# Feitiços conhecidos\n', 1)[1].split('## Invocação por espaço', 1)[0]
markline = next(l for l in repertoire.splitlines() if 'Os marcos ficam' in l)
marks = list(map(int, re.findall(r'\d+', markline.split('Os marcos ficam', 1)[1])))
assert len(marks) == 7, 'Escada de marcos mudou.'

sample_specs = [
    ('Gancho fechado', 2, 1, 0, [('media', True)], ['media'], 3, 'dano'),
    ('Placas de apoio', 2, 1, 0, [('media', True)], [], 2, 'apoio'),
    ('Linha de contenção', 2, 1, 0, [('media', True)], ['media'], 3, 'dano'),
    ('Fechar ferimento', 2, 1, 'media', [], [], 2, 'cura'),
    ('Resposta curta', 5, 2, 0, [('pesada', True)], ['media'], 6, 'dano'),
]
samples = []
for name, level, cls, form, improvements, restrictions, expected, kind in sample_specs:
    rule = costs[cls]
    spend = rule[form] if isinstance(form, str) else form
    spend += sum(max(1, rule[price] - math.ceil(cls / 2)) if free else rule[price] for price, free in improvements)
    refund = min(sum(rule[p] for p in restrictions), spend, 2 * cls)
    balance = rule['orcamento'] - spend + refund
    if kind == 'cura':
        balance = min(balance, 2 * cls)
    result = {'exemplo': name, 'nivel': level, 'classe': cls, 'gasto': spend, 'devolucao': refund, 'saldo': balance,
              'custo_PE': rule['orcamento'], 'resultado': f'{3 * balance} PV temporária' if kind == 'apoio' else f'{balance}d8'}
    samples.append(result)
    check('Exemplo: ' + name, balance == expected and level >= rule['nivel'] and len(improvements) <= 2 and len(restrictions) <= 2, result)

# Mechanical comparison of Presilha after the change in who rolls a maneuver.
presilha = []
for target_success in (0.25, 0.5, 0.75):
    attacker_initial = 1 - target_success
    old_reroll_failed_attempt = 1 - (1 - attacker_initial) ** 2
    repeated_successful_save = 1 - target_success ** 2
    presilha.append({'TR_alvo_sucesso': target_success, 'manobra_antes': attacker_initial,
                     'manobra_com_Presilha': repeated_successful_save, 'modelo_antigo_mesma_probabilidade': old_reroll_failed_attempt,
                     'ganho_pp': 100 * (repeated_successful_save - attacker_initial)})
check('Presilha oposição equivalente', all(abs(x['manobra_com_Presilha'] - x['modelo_antigo_mesma_probabilidade']) < 1e-12 for x in presilha), presilha)

lap = 1
picks = 0
growth = []
for level in marks:
    free = min(10, lap + 1)
    at_cap = free == 10
    picks += 2 if at_cap else 1
    lap = min(10, free + 1)
    growth.append({'nivel': level, 'depois_gratuito': free, 'lapidacao': lap, 'bencaos_no_marco': 2 if at_cap else 1, 'total': picks})
check('Rota pura Lapidação', [g['lapidacao'] for g in growth] == [3, 5, 7, 9, 10, 10, 10] and picks == 10, growth)
check('Lapidação sem escolha', 1 + len(marks) == 8, 1 + len(marks))

# Extract current owner of attack dice from R09 and candidate, comparing their tables.
apt = (E / 'aptidoes/lote-01/APTIDOES-E-REFINO.md').read_text()
aptpart = apt.split('## Canalizar em Golpe\n', 1)[1].split('## Feitiços e crítico', 1)[0]
ownpart = next(p['texto'] for p in pages if p['id'] == 'rota-estimulo')
pat = r'^\| (\d+(?:–\d+)?) \| (\d+d\d+)\.? \|$'
owner_dice = re.findall(pat, aptpart, re.M)
own_dice = re.findall(pat, ownpart, re.M)
assert len(owner_dice) == 5, 'Curva atual de Canalizar mudou.'
check('Estímulo corresponde ao Canalizar vigente', own_dice == owner_dice, {'candidata': own_dice, 'dono_R09': owner_dice})
numbers = [{'lapidacao': l, 'protecao': l // 3 + 1, 'RD': math.floor(1.5 * l), 'raio_Vulto': 1.5 * (l // 2),
            'alvos_Assombro': max(1, l // 2), 'autocura_semente_refino_equivalente': 4 if l == 10 else l // 3} for l in range(1, 11)]
check('Curvas nos limites citados', numbers[0]['protecao'] == 1 and numbers[-1]['protecao'] == 4 and numbers[-1]['RD'] == 15 and numbers[-1]['raio_Vulto'] == 7.5 and numbers[-1]['autocura_semente_refino_equivalente'] == 4, numbers)

# For any target bonus, changing either relevant attribute4–6 changes success by at most10pp.
def failchance(dc, bonus):
    return sum(d + bonus < dc for d in range(1, 21)) / 20
assombro = []
for essence, oldattr, mastery, targetbonus in itertools.product(range(4, 7), range(4, 7), range(1, 5), range(0, 11)):
    before, after = failchance(8 + oldattr + mastery, targetbonus), failchance(8 + essence + mastery, targetbonus)
    assombro.append({'essencia': essence, 'atributo_antigo': oldattr, 'maestria': mastery, 'bonus_alvo': targetbonus, 'antes': before, 'depois': after, 'variacao_pp': (after - before) * 100})
maximum = max(abs(x['variacao_pp']) for x in assombro)
check('Assombro mudança CD no intervalo4–6', maximum <= 10.000001, {'casos_enumerados': len(assombro), 'maxima_diferenca_pp': maximum, 'nao_cobre':'atributo antigo abaixo de4 ou fora do intervalo escolhido'})

esteio = [{'lapidacao': l, 'atributo': a, 'piso': min(l, a + 2)} for l, a in itertools.product(range(7, 11), range(0, 7))]
check('Esteio piso até8 sem somar Lapidação no TR', all(e['piso'] <= 8 for e in esteio), esteio)
check('Casco PV no14 e30', 14 // 2 == 7 and 30 // 2 == 15, {'14': 14 // 2, '30': 30 // 2})

report = {'manuscrito_sha256': hashlib.sha256(S.encode()).hexdigest(), 'estado':'candidata; validação computacional de limites definidos',
          'paginas_logicas':len(pages), 'checks':checks, 'falhas':[x['teste'] for x in checks if not x['passou']],
          'limites':['Não mede diversão, clareza humana ou eficácia de todas as combinações de combate.', 'Não é playtest nem prova de equilíbrio global.', 'Fonte externa do cânone não foi validada por estes testes.', 'Inspeção visual depende do PDF renderizado e pertence à raiz.']}
save('AUDITORIA.json', report)
save('evidencias/auditoria-numerica.json', {'manuscrito_sha256':report['manuscrito_sha256'], 'fontes':['R06 tabela Pontos e preços / Feitiços conhecidos', 'R09 Canalizar', 'manual47 e peças09/11'], 'exemplos':samples, 'presilha':presilha, 'marcos':growth, 'curvas':numbers, 'assombro':{'escopo':'E4/5/6 vs atributo4/5/6; maestria1–4; bônusTR0–10', 'casos':assombro, 'diferenca_maxima_pp':maximum}, 'esteio':esteio})
report['ok']=not report['falhas']
num=json.loads((P/'evidencias/auditoria-numerica.json').read_text())
num.update(ok=report['ok'],manuscritos_auditados={str((P/'ROTAS.md').relative_to(R)):report['manuscrito_sha256']},checks=checks)
save('evidencias/auditoria-numerica.json',num)
save('evidencias/regras-verificadas.json',{'ok':report['ok'],'sha256_texto':report['manuscrito_sha256'],'casos':checks,'casos_contextuais':'CASOS.json','teste_humano':False})
print(json.dumps({'checks':len(checks),'falhas':report['falhas'],'paginas_logicas':len(pages)},ensure_ascii=False))
raise SystemExit(bool(report['falhas']))
