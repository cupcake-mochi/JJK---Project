"""Contas e regras dirigidas do lote C-02 (registros de campanha), conferidas contra o Livro de Regras 1.0 (R53)."""
from pathlib import Path
import json, hashlib
A = Path(__file__).resolve().parent
R = A.parents[1]
primary = R / '04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
rule = primary.read_text()
C = R / '06 - Redacao do Guia/revisao-98/consultas'
checks = []
def ck(name, x, y):
    assert x == y, (name, x, y); checks.append({'conta': name, 'resultado': x, 'esperado': y})
def has(t, src=None):
    assert t in (rule if src is None else src), t

# s028 — Conselho Interior: uma vez por cena, repete teste falho, perícias compartilham o uso
has('**Requisito: Coexistência. Uma vez por cena**, após falhar em Intuição ou Ocultismo, repita o teste e aceite o segundo resultado. As duas perícias compartilham o uso.')
has('Conselho Interior permite, uma vez por cena, repetir um teste falho de Intuição ou Ocultismo e aceitar o segundo resultado; as duas perícias compartilham o uso.', (C / '28-ficha-de-convivencia.md').read_text())

# s032 — Restrição revista depois de três sessões de uso; a ficha traz três linhas
has('O mestre deve rever uma Restrição depois de três sessões em que o feitiço tenha sido usado.')
ck('Linhas do acompanhamento de Restrição', [l.split('|')[1].strip() for l in (C / '32-ficha-de-avaliacao-de-capacidade.md').read_text().splitlines() if l.startswith('| ') and l.split('|')[1].strip().isdigit()], ['1', '2', '3'])

# s032 — Toque Classe 1: devolução só compensa Melhorias; sem Melhorias, nada a aproveitar → 3d8, não 4d8
has('**Toque** tem custo zero e concede uma devolução Leve nas montagens comuns de Classes 1 a 7. Essa devolução compensa pontos pagos em Melhorias')
has('Aproveite no máximo o gasto em Melhorias e no máximo 2 × Classe.')
ck('Devolução aproveitada sem Melhorias (mín. entre devolução Leve 1, Melhorias 0 e 2 × Classe 2)', min(1, 0, 2 * 1), 0)
has('**Classe 1 · Ação Padrão · 3 PE · Toque, até 1,5 m.**')
has('Faça seu ataque de técnica contra a Defesa. No acerto, causa **3d8 de Concussão**')
# demonstração: atributo 3 + Maestria 1; dado 10 contra Defesa 14
has('Mei tem Destreza 3 e Maestria 1, somando **d20 + 4** no ataque de conjuração. Contra Defesa 14, um resultado 10 no dado totaliza 14 e acerta.')
ck('Ataque de conjuração: atributo 3 + Maestria 1', 3 + 1, 4)
ck('Dado 10 + 4 contra Defesa 14 acerta', 10 + 4 >= 14, True)
has('Ação Padrão, 3 PE, alcance 1,5 m, Selo e ataque de conjuração.', (C / '32-ficha-de-avaliacao-de-capacidade.md').read_text())

# s038 — Traje de Rina: Alfaiate, ¥3.000, 4 horas, sem teste; depois de 2 horas faltam 2
has('um reparo com Alfaiate exige tecido e fechos de **¥3.000**, ferramentas e **4 horas de trabalho**. É um serviço conhecido, sem risco relevante; não exige teste. Depois de 2 horas, ainda faltam **2 horas**.')
ck('Traje de Rina: 4 horas − 2 do primeiro intervalo', 4 - 2, 2)
ck('Traje de Rina: dois intervalos de 2 horas', 2 + 2, 4)
ficha = (C / '38-ficha-de-projeto-e-entrega.md').read_text()
for t in ['**Conhecimentos:** Alfaiate.', 'tecido e fechos de ¥3.000', '**Trabalho:** quatro horas.', '**Teste:** dispensado, por ser rotina sem risco relevante.']:
    has(t, ficha)

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(primary) == '7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
d = {'registro': 132, 'novos_parametros': False, 'conferencias': checks,
     'regras_primarias': {'fonte': str(primary.relative_to(R)), 'sha256': sha(primary),
                          'trechos_consultados': ['Conselho Interior', 'Revisão da Restrição', 'Toque, Aura e proximidade', 'Devolução aproveitada', 'Peso nas Mãos', 'Ataque de conjuração (Mei)', 'Reparo do Traje de Rina']},
     'limites': ['Fichas de acordos, descobertas e facção não têm contas nem regras mecânicas; foram conferidas só na leitura.']}
(A / 'contas-conferidas.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(len(checks), 'contas conferidas')
