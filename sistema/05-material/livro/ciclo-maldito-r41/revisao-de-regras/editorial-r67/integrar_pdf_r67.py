"""Integra os PDFs da R67, compostos em 12/11/2026, no molde do integrar_r66.py.

O texto da R67 já está no LIVRO-COMPLETO.md (integrar_r67.py e revisar_clareza_r67.py).
Aqui entram os dois PDFs, o EDICAO-ATUAL.json, o REVISAO-R67.json, as evidências da
composição e as versões dos documentos. Roda uma vez e recusa rodar de novo.
"""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib, json, shutil
E = Path(__file__).resolve().parent
RAIZ = E.parents[5]
L = RAIZ/'sistema/05-material/livro'; B = L/'ciclo-maldito-r41'
P = Path('/home/mizuki/CHAT-GPT/RPG -JJK/desenvolvimento-fundamentos/revisao-didatica-r57-v1/revisao-r67')
def ler(p): return p.read_text(encoding='utf-8')
def gravar(p, t): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(t, encoding='utf-8')
def rd(p): return json.loads(ler(p))
def dump(p, v): gravar(p, json.dumps(v, ensure_ascii=False, indent=2) + '\n')
def copy(a, b): b.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(a, b)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def editar(p, a, b):
    t = ler(p); assert t.count(a) == 1, (str(p), a, t.count(a)); gravar(p, t.replace(a, b, 1))

texto = B/'LIVRO-COMPLETO.md'
assert ler(texto) == ler(E/'LIVRO-COMPLETO-R67.md') == ler(P/'LIVRO-CANDIDATA.md'), 'fonte da composição não é a R67 corrente'
assert ler(P/'composicao/LIVRO-COMPLETO.md') == ler(texto)
val = rd(P/'revisao/VALIDACAO.json'); assert val['resultado'] == 'aprovado' and all(c['aprovado'] for c in val['verificacoes'])
aud = rd(P/'revisao/AUDITORIA-PAGINAS-INDICE.json'); assert aud['entradas'] == 453 and not aud['links_e_numeros_incorretos'] and not aud['aliases_sem_subtitulo']
cmp = rd(P/'r67/paginas/COMPARACAO.json'); visual = rd(P/'r67/REVISAO-VISUAL.json')
assert cmp['claro']['texto_mudou'] == cmp['noturno']['texto_mudou'] == visual['paginas']
meta = rd(L/'EDICAO-ATUAL.json'); assert meta['revisao'] == 'R66', 'já integrada'
ops = rd(B/'revisao-de-regras/alteracoes/R66-para-R67.json')

# Evidências da composição, como em editorial-r66/.
for f in (P/'composicao').glob('*.py'): copy(f, E/'composicao'/f.name)
for f in ['FONTES-E-VALIDACAO.json', 'GEOMETRIA-CANDIDATA.json']: copy(P/'composicao'/f, E/'composicao'/f)
for f in ['NAVEGACAO.json', 'SUMARIO-PAGINADO.json']: copy(P/'composicao/revisao-r45'/f, E/'composicao/revisao-r45'/f)
for f in ['conferir.py', 'DESTINOS-INDICE-REVISAO.json']: copy(P/f, E/f)
for f in ['VALIDACAO.json', 'AUDITORIA-PAGINAS-INDICE.json']: copy(P/'revisao'/f, E/'evidencias'/f)
copy(P/'r67/paginas/COMPARACAO.json', E/'evidencias/COMPARACAO-R66.json')
copy(P/'r67/REVISAO-VISUAL.json', E/'evidencias/REVISAO-VISUAL.json')
copy(P/'r67/conferir.log', E/'evidencias/conferir.log')

meta.update(revisao='R67', paginas=422, revisado_em=datetime.now(ZoneInfo('America/Sao_Paulo')).isoformat())
for pal in ['claro', 'noturno']:
    copy(P/'composicao/output/pdf'/meta[pal]['arquivo'], L/meta[pal]['arquivo']); meta[pal]['sha256'] = sha(L/meta[pal]['arquivo'])
dump(L/'EDICAO-ATUAL.json', meta)
dump(L/'REVISAO-R67.json', {
    'revisao': 'R67', 'base': 'R66', 'resultado': 'aprovado', 'paginas': 422,
    'blocos_alterados': sorted({o['bloco'] for o in ops}), 'trocas': len(ops),
    'descricao': 'Técnica Máxima com Forma e função pagas nos dados, decidida pelo autor em 12/11/2026; seis ajustes de clareza na composição, sem mudar regra.',
    'paginas_alteradas': visual['paginas'], 'ancoras_que_mudaram_de_pagina': visual['ancoras'],
    'conferencia_pdf': val['verificacoes'], 'auditoria_indice': aud, 'revisao_visual': visual,
    'sha256': {**{k: meta[k]['sha256'] for k in ['claro', 'noturno']}, 'texto': sha(texto)}})
f = rd(E/'FONTE-PUBLICADA.json'); f['pdf'] = 'composta em 12/11/2026: hashes em EDICAO-ATUAL.json'; f['composicao_local'] = str(P/'composicao'); dump(E/'FONTE-PUBLICADA.json', f)
editar(RAIZ/'conferir-repositorio.py', "'EDICAO-ATUAL.json', 'REVISAO-R66.json')", "'EDICAO-ATUAL.json', 'REVISAO-R67.json')")

resumo = ('A R67 está composta nas duas paletas, com 422 páginas, como a R66. Mudaram 11 páginas, as mesmas nas duas: '
          '276 a 281 (Técnica Máxima, Passagem de Papel e Retirada de Emergência), 376 e 377 (Técnica Máxima da domada), '
          '410 (Glossário), e o número da Técnica Máxima no Sumário (4) e no Índice (420), que passou de 278 para 277. '
          'A composição passou nas 65 verificações, com os 453 verbetes do Índice conferidos, e o texto é idêntico nas duas paletas. '
          'A revisão visual passou pelas 11 páginas nas duas paletas e não achou título solto, coluna quebrada nem tabela estourada.')
clareza = ('Antes da composição final, uma revisão de clareza ajustou seis trechos da R67, sem mudar número nem regra: '
           'a linha coletiva da tabela nova diz o valor de cada dado e que cada aliado recebe o total, sem dividir; '
           'a base do dano aparece como "Nenhuma", no lugar de "0"; o exemplo mostra a conta inteira (8 dados, 5 da base Média e 3 da Aura; sobram 16); '
           'o Efeito Próprio principal vai "até Pesada", como no resto do livro; e a vida temporária é encaminhada para a tabela, fora da Aplicação sem dano.')

p = RAIZ/'sistema/ESTADO-ATUAL.md'; t = ler(p)
velho = '# Edição corrente R67, só o texto\n\n**Versão v0.377.**'
assert t.startswith(velho)
gravar(p, '# Edição corrente R67\n\n**Versão v0.378.**\n\n' + resumo + '\n\n' + clareza +
       '\n\n**Publicação pendente.** A Vercel publica a partir do `main`: o merge publica. Depois dele, conferir o download das duas URLs públicas contra os hashes do `EDICAO-ATUAL.json` e registrar em `editorial-r67/PUBLICACAO.json`. A ficha digital ainda precisa da mesma mudança: as fórmulas da Máxima em `DADOS_R53` pagam a Forma com os pontos.'
       '\n\nFonte, registros e validações em `05-material/livro/ciclo-maldito-r41/revisao-de-regras/editorial-r67/`. A composição está descrita em `editorial-r67/COMPOSICAO.md`.\n\n'
       + t.replace(velho, '# Texto da R67\n\n*Versão v0.377.*', 1))

editar(RAIZ/'README.md', '**Versão v0.377**', '**Versão v0.378**')
editar(RAIZ/'README.md', '[Ciclo Maldito R66, livro completo com 422 páginas]', '[Ciclo Maldito R67, livro completo com 422 páginas]')
editar(RAIZ/'README.md', 'Os PDFs continuam os da R66 até a composição da R67. O texto já está no `LIVRO-COMPLETO.md`;', 'Os PDFs da R67 foram compostos na v0.378, com 422 páginas e seis ajustes de clareza sem mudança de regra;')
editar(RAIZ/'sistema/LEIA-ME.md', '**v0.377.**', '**v0.378.**')
editar(RAIZ/'sistema/LEIA-ME.md', 'O livro atual é a R66 no PDF e a R67 no texto (a Técnica Máxima paga Forma e função nos dados)', 'O livro atual é a R67 (a Técnica Máxima paga Forma e função nos dados)')
editar(B/'LEIA-ME.md', '**Os PDFs ainda são os da R66**, com hashes em EDICAO-ATUAL.json; a composição da R67 fica para outra rodada.', 'Os PDFs da R67 ficam na pasta acima, com hashes em EDICAO-ATUAL.json. A composição está descrita em revisao-de-regras/editorial-r67/COMPOSICAO.md.')

p = RAIZ/'logs/CHANGELOG.md'; t = ler(p); marca = '## [0.377] - 12/11/2026'; assert t.count(marca) == 1
entrada = ('## [0.378] - 12/11/2026\n\n### Alterado\n\n- ' + resumo +
  '\n- ' + clareza + ' As 17 trocas de `R66-para-R67.json` já trazem a redação final; o script é `editorial-r67/revisar_clareza_r67.py`.'
  '\n- `conferir-fundamento.py`: a checagem do exemplo da cura passou a ler os 5 dados da base Média do modelo de preço, e entraram duas checagens (a conta do exemplo coletivo e a linha coletiva da tabela) e um contra-teste. Perturbado numa cópia isolada, cada número novo acende a checagem certa.'
  '\n- `EDICAO-ATUAL.json` e os dois PDFs passam à R67; `REVISAO-R67.json` substitui o `REVISAO-R66.json` no `conferir-repositorio.py`. Composição e evidências em `editorial-r67/` (`COMPOSICAO.md`, `composicao/`, `evidencias/`).'
  '\n\n→ Continua em `sistema/ESTADO-ATUAL.md`: conferir a publicação da R67 na Vercel depois do merge e levar a regra para a ficha (`DADOS_R53`).\n\n')
gravar(p, t.replace(marca, entrada + marca, 1))
print('Integrados os PDFs da R67:', meta['claro']['sha256'][:12], meta['noturno']['sha256'][:12])
