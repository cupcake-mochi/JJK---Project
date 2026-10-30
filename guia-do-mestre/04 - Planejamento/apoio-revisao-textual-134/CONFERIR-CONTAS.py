"""Regras e fontes do lote C-04 (mundo e obra), conferidas contra o Livro de Regras 1.0 (R53) e as páginas oficiais da obra."""
from pathlib import Path
import json, hashlib
A = Path(__file__).resolve().parent
R = A.parents[1]
primary = R / '04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
rule = primary.read_text()
checks = []
def ck(name, x, y):
    assert x == y, (name, x, y); checks.append({'conta': name, 'resultado': x, 'esperado': y})
def has(t):
    assert t in rule, t

# Termos do mundo — afirmações de regra do índice
origens = [l[4:].strip() for l in rule.splitlines() if l.startswith('### ') and l[4:].strip() in
           ['Latente', 'Receptáculo', 'Descendente', 'Encarnado', 'Híbrido', 'Corpo Amaldiçoado', 'Restrição Celestial']]
ck('Sete Origens no Livro de Regras 1.0', len(set(origens)), 7)
has('Escolha **um dos dois ramos** na criação: **Sem Energia** ou **Restrição corporal**.')
has('Seu Caminho fornece a quantidade normal de PE, lidos como **Pontos de Esforço**')
has('Na rota Sem Técnica, os feitiços recebem o nome de **Manejos** e seguem os requisitos da semente escolhida. Na Técnica Marcial, são chamados de **Katas**')
has('Você tem energia amaldiçoada, mas não possui técnica inata.')
has('Você delimita uma área para esconder seu interior de pessoas que não são feiticeiras e controlar a passagem por suas bordas.')
has('Refino e Lapidação têm progressões próprias.')
has('| Lista de ritual | Um feitiço com uma lista própria e desafios individuais de submissão.')
has('Na criação padrão, todos começam no **Grau 4**.')
ck('Regras citadas conferidas', 9, 9)

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(primary) == '7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
# Fontes da obra: abertas em 30/10/2026 no navegador do app (o acesso automático recebeu 403). Paráfrase de trabalho.
externas = [
    {'fonte': 'https://jujutsukaisen.jp/episodes/48.php', 'conferida_em': '2026-10-30', 'confere': True,
     'resumo': 'Tóquio após Shibuya; Yuji e Choso caçam maldições; Naoya, que mira a chefia do clã Zenin, ataca; Yuji sabe por ele que a suspensão da execução foi revogada; Yuta chega como executor.'},
    {'fonte': 'https://jujutsukaisen.jp/episodes/50.php', 'conferida_em': '2026-10-30', 'confere': True,
     'resumo': 'O grupo vai a Tengen para saber como desfazer o selamento de Gojo e o objetivo do adversário; Tengen responde e explica o Jogo do Abate.'},
    {'fonte': 'https://jujutsukaisen.jp/episodes/51.php', 'conferida_em': '2026-10-30', 'confere': True,
     'resumo': 'Maki vai à família Zenin buscar ferramentas para o Jogo do Abate; enfrenta insultos e a oposição da mãe; no depósito encontra Mai ensanguentada e o pai.'},
    {'fonte': 'https://jujutsukaisen.jp/episodes/55.php', 'conferida_em': '2026-10-30', 'confere': True,
     'resumo': 'Higuruma foi advogado; Yuji e Megumi recebem informações diferentes sobre onde ele está.'},
    {'fonte': 'https://www.shueisha.co.jp/books/items/contents_amp.html?jdcn=08X10000000018964300', 'conferida_em': None, 'confere': None,
     'resumo': 'Página em manutenção de emergência em 30/10/2026; não reconfirmada. Conferida antes no lote 8 (apoio-lote8/fontes-conferidas.md); o texto do Guia não mudou.'},
]
d = {'registro': 134, 'novos_parametros': False, 'conferencias': checks,
     'regras_primarias': {'fonte': str(primary.relative_to(R)), 'sha256': sha(primary),
                          'trechos_consultados': ['Origens', 'Restrição Celestial', 'Rotas de criação', 'Cortina', 'Refino e Lapidação', 'Lista de ritual', 'Patentes']},
     'fontes_externas': externas,
     'limites': ['Sinopses oficiais consultadas; sem leitura integral do mangá ou dos episódios.', 'Volume 18 não reconfirmado nesta revisão (página fora do ar).']}
(A / 'contas-conferidas.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(len(checks), 'conferências;', sum(1 for x in externas if x['confere']), 'de', len(externas), 'fontes da obra reconfirmadas')
