"""Integra os PDFs da R68, compostos no Windows em 14/11/2026, no molde do integrar_pdf_r67.py.

O texto da R68 já está no LIVRO-COMPLETO.md (integrar_r68.py). Aqui entram os dois PDFs,
o EDICAO-ATUAL.json, o REVISAO-R68.json, as evidências da composição e as versões dos
documentos. Roda uma vez e recusa rodar de novo.
"""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib, json, shutil
E = Path(__file__).resolve().parent
RAIZ = E.parents[5]
L = RAIZ/'sistema/05-material/livro'; B = L/'ciclo-maldito-r41'
P = Path(r'D:\Projetos\CHAT-GPT\RPG -JJK\desenvolvimento-fundamentos\revisao-didatica-r57-v1\revisao-r68')
def ler(p): return p.read_text(encoding='utf-8')
def gravar(p, t): p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(t.encode('utf-8'))
def rd(p): return json.loads(ler(p))
def dump(p, v): gravar(p, json.dumps(v, ensure_ascii=False, indent=2) + '\n')
def copy(a, b): b.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(a, b)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def editar(p, a, b):
    t = ler(p); assert t.count(a) == 1, (str(p), a, t.count(a)); gravar(p, t.replace(a, b, 1))

texto = B/'LIVRO-COMPLETO.md'
assert ler(texto) == ler(E/'LIVRO-COMPLETO-R68.md') == ler(P/'LIVRO-CANDIDATA.md'), 'fonte da composição não é a R68 corrente'
assert ler(P/'composicao/LIVRO-COMPLETO.md') == ler(texto)
val = rd(P/'revisao/VALIDACAO.json'); assert val['resultado'] == 'aprovado' and all(c['aprovado'] for c in val['verificacoes'])
aud = rd(P/'revisao/AUDITORIA-PAGINAS-INDICE.json'); assert aud['entradas'] == 453 and not aud['links_e_numeros_incorretos'] and not aud['aliases_sem_subtitulo']
cmp = rd(P/'r68/paginas/COMPARACAO.json'); visual = rd(P/'r68/REVISAO-VISUAL.json')
assert cmp['claro']['texto_mudou'] == cmp['noturno']['texto_mudou'] == visual['paginas']
assert not cmp['claro']['so_visual_mudou'] and not cmp['noturno']['so_visual_mudou']
meta = rd(L/'EDICAO-ATUAL.json'); assert meta['revisao'] == 'R67', 'já integrada'
ops = rd(B/'revisao-de-regras/alteracoes/R67-para-R68.json')

for f in (P/'composicao').glob('*.py'): copy(f, E/'composicao'/f.name)
for f in ['FONTES-E-VALIDACAO.json', 'GEOMETRIA-CANDIDATA.json']: copy(P/'composicao'/f, E/'composicao'/f)
for f in ['NAVEGACAO.json', 'SUMARIO-PAGINADO.json']: copy(P/'composicao/revisao-r45'/f, E/'composicao/revisao-r45'/f)
for f in ['conferir.py', 'DESTINOS-INDICE-REVISAO.json']: copy(P/f, E/f)
for f in ['VALIDACAO.json', 'AUDITORIA-PAGINAS-INDICE.json']: copy(P/'revisao'/f, E/'evidencias'/f)
copy(P/'r68/paginas/COMPARACAO.json', E/'evidencias/COMPARACAO-R67.json')
copy(P/'r68/REVISAO-VISUAL.json', E/'evidencias/REVISAO-VISUAL.json')
copy(P/'r68/conferir.log', E/'evidencias/conferir.log')

meta.update(revisao='R68', paginas=422, revisado_em=datetime.now(ZoneInfo('America/Sao_Paulo')).isoformat())
for pal in ['claro', 'noturno']:
    copy(P/'composicao/output/pdf'/meta[pal]['arquivo'], L/meta[pal]['arquivo']); meta[pal]['sha256'] = sha(L/meta[pal]['arquivo'])
dump(L/'EDICAO-ATUAL.json', meta)
dump(L/'REVISAO-R68.json', {
    'revisao': 'R68', 'base': 'R67', 'resultado': 'aprovado', 'paginas': 422,
    'blocos_alterados': sorted({o['bloco'] for o in ops}), 'trocas': len(ops),
    'descricao': 'Reforço de Controle da Técnica Máxima sem dano nas seções de Controle e de Controle das entidades, consequência da R67. Primeira composição no Windows.',
    'paginas_alteradas': visual['paginas'], 'ancoras_que_mudaram_de_pagina': visual['ancoras'],
    'conferencia_pdf': val['verificacoes'], 'auditoria_indice': aud, 'revisao_visual': visual,
    'sha256': {**{k: meta[k]['sha256'] for k in ['claro', 'noturno']}, 'texto': sha(texto)}})
f = rd(E/'FONTE-PUBLICADA.json'); f['pdf'] = 'composta em 14/11/2026: hashes em EDICAO-ATUAL.json'; f['composicao_local'] = str(P/'composicao'); dump(E/'FONTE-PUBLICADA.json', f)
editar(RAIZ/'conferir-repositorio.py', "'EDICAO-ATUAL.json', 'REVISAO-R67.json')", "'EDICAO-ATUAL.json', 'REVISAO-R68.json')")

resumo = ('A R68 corrige duas frases que ainda negavam o reforço de Controle à Técnica Máxima sem dano, que a R67 deu: '
          'a da seção de Controle, no Fundamento, e a do Controle das entidades, em Construir invocações, onde a Máxima da domada passa a recebê-lo como a pessoal. '
          'Classe 0, Liberação Máxima e a básica continuam sem ele. O achado veio de quem levava a regra para a ficha, em 14/11/2026. '
          'São 2 trocas em 2 blocos; mudaram só as páginas 268 e 395, as mesmas nas duas paletas, e nenhuma âncora mudou de página. '
          'O livro continua com 422 páginas. A composição passou nas 65 verificações, com os 453 verbetes do Índice conferidos, e a revisão visual passou pelas duas páginas nas duas paletas.')
windows = ('Foi a primeira composição no Windows: a cadeia do Linux, copiada para o HD interno, roda com as versões de biblioteca do Python do Codex e as fontes copiadas para junto do gerador. '
           'Antes de trocar o texto, a R67 regerada no Windows saiu idêntica, byte a byte, aos PDFs publicados nas duas paletas. O passo a passo está em `05-material/livro/ciclo-maldito-r41/revisao-de-regras/editorial-r68/COMPOSICAO.md`.')

p = RAIZ/'sistema/ESTADO-ATUAL.md'; t = ler(p)
velho = '# Edição corrente R67\n\n**Versão v0.378.**'
assert t.startswith(velho)
gravar(p, '# Edição corrente R68\n\n**Versão v0.379.**\n\n' + resumo + '\n\n' + windows +
       '\n\n**Publicação pendente.** Quem publica é o repositório `JJK---PDF---RPG`: os dois PDFs, o `EDICAO-ATUAL.json` e o `REVISAO-R68.json` vão para a pasta `livro/` dele. Depois do push, conferir o download das duas URLs públicas contra os hashes do `EDICAO-ATUAL.json` e registrar num PUBLICACAO.json na pasta da R68, como o da R67.'
       '\n\n**Ficha pendente.** A ficha digital ainda está na regra antiga da Máxima, e a Máxima sem dano dela precisa do reforço de Controle (`controle_sem_dano`).'
       '\n\nFonte, registros e validações em `05-material/livro/ciclo-maldito-r41/revisao-de-regras/editorial-r68/`. A cadeia de integridade cobre R52 a R68.\n\n'
       + t.replace(velho, '# Edição anterior R67\n\n*Versão v0.378.*', 1))

editar(RAIZ/'README.md', '**Versão v0.378**', '**Versão v0.379**')
editar(RAIZ/'README.md', '[Ciclo Maldito R67, livro completo com 422 páginas]', '[Ciclo Maldito R68, livro completo com 422 páginas]')
editar(RAIZ/'README.md', 'o registro fica em `sistema/05-material/livro/ciclo-maldito-r41/revisao-de-regras/editorial-r67/`.',
       'o registro fica em `sistema/05-material/livro/ciclo-maldito-r41/revisao-de-regras/editorial-r67/`. A R68 corrige as duas seções de Controle que ainda negavam o reforço à Máxima sem dano; o registro fica em `editorial-r68/`.')
editar(RAIZ/'sistema/LEIA-ME.md', '**v0.378.**', '**v0.379.**')
editar(RAIZ/'sistema/LEIA-ME.md', 'O livro atual é a R67 (a Técnica Máxima paga Forma e função nos dados)', 'O livro atual é a R68 (a Técnica Máxima paga Forma e função nos dados, e a sem dano recebe o reforço de Controle)')
lm = B/'LEIA-ME.md'; t = ler(lm); ini = t.index('# Fonte corrente R67')
gravar(lm, '# Fonte corrente R68\n\nLIVRO-COMPLETO.md é a edição R68, usada pelos validadores. É a R67 com duas frases corrigidas: as seções de Controle passam a dar o reforço à Técnica Máxima sem dano, pessoal e da domada. São 2 trocas em 2 blocos.\n\n'
       'O snapshot, as trocas e os scripts ficam em revisao-de-regras/editorial-r68/. O antes e depois está em revisao-de-regras/alteracoes/R67-para-R68.json. Os PDFs da R68 ficam na pasta acima, com hashes em EDICAO-ATUAL.json. A composição, a primeira feita no Windows, está descrita em revisao-de-regras/editorial-r68/COMPOSICAO.md.\n\n'
       + t[:ini] + t[ini:].replace('# Fonte corrente R67', '# Fonte R67', 1))

p = RAIZ/'logs/CHANGELOG.md'; t = ler(p); marca = '## [0.378] - 12/11/2026'; assert t.count(marca) == 1
entrada = ('## [0.379] - 14/11/2026\n\n### Alterado\n\n- ' + resumo +
  '\n- ' + windows +
  '\n- `conferir-fundamento.py`, seção 9: duas checagens novas (a seção de Controle e a de Controle das entidades dão o reforço à Máxima sem dano, e só negam a Classe 0, à Liberação e à básica) e dois contra-testes que voltam as frases antigas. Perturbado numa cópia isolada, cada frase antiga acende a checagem certa.'
  '\n- Ponteiros da fonte corrente, de R67 para R68, no `conferir-repositorio.py`, nos dois `testar-integridade.py`, no `conferir-fundamento.py` e no `livro.py`. `EDICAO-ATUAL.json` e os dois PDFs passam à R68; `REVISAO-R68.json` substitui o `REVISAO-R67.json`.'
  '\n\n→ Continua em `sistema/ESTADO-ATUAL.md`: publicar a R68 pelo `JJK---PDF---RPG` e conferir as URLs; levar a regra da Máxima para a ficha.\n\n')
gravar(p, t.replace(marca, entrada + marca, 1))
print('Integrados os PDFs da R68:', meta['claro']['sha256'][:12], meta['noturno']['sha256'][:12])
