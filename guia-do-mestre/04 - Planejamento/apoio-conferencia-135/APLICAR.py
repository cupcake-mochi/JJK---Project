"""Conferência do conjunto (registro 135): nomes do elenco fixo e remissões.

Trabalha nas cópias revistas de revisao-98 (capítulos, casos, consultas). Os originais não são tocados.
Na primeira execução guarda antes/; as execuções seguintes partem sempre de antes/, então o resultado é
reproduzível. Grava alteracoes.json com cada troca (arquivo, antes, depois, motivo)."""
from pathlib import Path
import json, os, re, shutil, sys

A = Path(__file__).resolve().parent; R = A.parents[1]; G = R / '06 - Redacao do Guia'; S = G / 'revisao-98'
ANTES = A / 'antes'
FILES = sorted([p for p in S.glob('*.md') if p.name != 'LEIA-ME.md'] + list((S / 'casos').glob('*.md'))
               + list((S / 'consultas').glob('*.md')))
rel = lambda p: str(p.relative_to(S))
if not ANTES.exists():
    for p in FILES:
        d = ANTES / rel(p); d.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(p, d)
txt = {rel(p): (ANTES / rel(p)).read_text() for p in FILES}
log = []

def sub(f, old, new, motivo, n=1):
    c = txt[f].count(old)
    if c != n: sys.exit(f'{f}: esperado {n}x, achado {c}x: {old[:80]!r}')
    txt[f] = txt[f].replace(old, new); log.append({'arquivo': f, 'antes': old, 'depois': new, 'vezes': n, 'motivo': motivo})

# ------------------------------------------------------------------ 1. avisos que deixam de ser necessários
AV = 'Nome: o aviso de que não é o mesmo personagem sai, porque o nome passou a ser único.'
sub('casos/33-casos-especificos-de-avaliacao.md', 'Haru, um personagem de exemplo e não o guarda do arquivo, tem', 'Haru tem', AV)
sub('casos/54-transporte-e-continuidade-das-entidades.md', ' É um personagem deste exemplo, não o atacante de nível 6 da dupla Ren e Sora.', '', AV)
sub('casos/50-promessa-do-arquivo.md', 'Akira, um feiticeiro deste exemplo e não o perfil de Guia dos confrontos, precisa', 'Akira precisa', AV)

# ------------------------------------------------------------------ 2. nomes (elenco fixo, proposta aprovada em 30/10)
DUPLA = ['06-inimigos-e-perigos.md', 'consultas/58-ficha-de-inimigo-e-encontro.md', 'casos/59-recursos-e-ritmo-dos-inimigos.md',
         'casos/68-ficha-e-comparacao-de-chefes.md', 'casos/74-regua-inicial-de-inimigos.md', 'casos/75-ren-e-sora-atacante-e-apoio.md',
         'casos/76-confronto-de-ren-e-sora.md', 'casos/77-ficha-preenchida-ren-e-sora.md', 'consultas/LEIA-ME.md']
GUARDA = ['casos/100-comparar-inimigos-em-outras-faixas.md', 'casos/101-haru-vigia-e-tessa.md',
          'casos/102-o-arquivo-e-as-oportunidades-de-agir.md', 'casos/59-recursos-e-ritmo-dos-inimigos.md', 'consultas/LEIA-ME.md']
NOMES = [('Ren', 'Toru', DUPLA), ('Sora', 'Sayo', DUPLA), ('Haru', 'Daigo', GUARDA),
         ('Sora', 'Gabi', ['05-criar-uma-campanha.md']), ('Sora', 'Hiro', ['casos/83-perceber-procurar-e-interpretar-sinais.md']),
         ('Akira', 'Kei', ['casos/50-promessa-do-arquivo.md', '09-pactos-e-entidades.md']),
         ('Mina', 'Noa', ['casos/84-percursos-apoios-e-quedas.md', 'casos/85-trajetorias-ferramentas-e-improvisacao.md']),
         ('Mina', 'Chie', ['casos/95-efeitos-de-cena-e-cancelamento.md']),
         ('Nara', 'Tainá', ['casos/52-domar-o-amontoado.md', 'casos/54-transporte-e-continuidade-das-entidades.md']),
         ('Nara', 'Sumi', ['casos/48-pacifismo-impraticavel-minuta.md']),
         ('Nara', 'Rosa', ['consultas/87-casos-da-obra-para-preparar-situacoes.md']),
         ('Emi', 'Yoko', ['02-o-mundo-dos-feiticeiros.md']),
         ('Emi', 'Paula', ['consultas/87-casos-da-obra-para-preparar-situacoes.md', 'consultas/88-indice-de-termos-do-mundo.md']),
         ('Davi', 'Bruno', ['casos/94-compras-repetidas-e-restricoes.md']),
         ('Rui', 'Beto', ['01-sua-primeira-missao.md']), ('Rui', 'Tiago', ['casos/90-reparar-personagem-de-corpo-construido.md']),
         ('Rui', 'Shin', ['casos/94-compras-repetidas-e-restricoes.md']),
         ('Ema', 'Mio', ['casos/84-percursos-apoios-e-quedas.md']),
         ('Lia', 'Itsuki', ['05-criar-uma-campanha.md']), ('Lia', 'Kana', ['casos/94-compras-repetidas-e-restricoes.md'])]
NOME = 'Nome: elenco fixo aprovado em 30/10; um nome, um papel (proposta-de-nomes.md).'
link_target = re.compile(r'(\]\(<?[^)>]*>?\))')
for velho, novo, fs in NOMES:
    for f in fs:
        # troca só no texto visível: os destinos de link (nomes de arquivo) ficam
        partes = link_target.split(txt[f]); n = 0
        for i in range(0, len(partes), 2):
            partes[i], k = re.subn(r'(?<![\w-])' + velho + r'(?![\w-])', novo, partes[i]); n += k
        if not n: sys.exit(f'{f}: {velho} não encontrado')
        txt[f] = ''.join(partes); log.append({'arquivo': f, 'antes': velho, 'depois': novo, 'vezes': n, 'motivo': NOME})

# ------------------------------------------------------------------ 3. remissões a originais já revistos
est = json.loads((R / '04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json').read_text())
revisto = {p.name: p for p in list((S / 'casos').glob('*.md')) + list((S / 'consultas').glob('*.md')) if p.name != 'LEIA-ME.md'}
CAP = {  # capítulo antigo -> (destino, título novo quando o texto do link é o título antigo)
    '25-conferir-personagens.md': ('07-personagens-e-tecnicas.md#71-conferir-a-ficha', {'Conferir personagens': 'Conferir a ficha'}),
    '26-vinculos-e-mudancas.md': ('05-criar-uma-campanha.md#52-vinculos-e-interesses-dos-personagens', {'Vínculos e mudanças': 'Vínculos e interesses dos personagens'}),
    '29-avaliar-tecnicas-e-criacoes.md': ('07-personagens-e-tecnicas.md#74-avaliar-uma-capacidade', {'Avaliar técnicas e criações': 'Avaliar uma capacidade'}),
    '39-atividades-e-tempo-entre-missoes.md': ('08-entre-missoes.md#82-tempo-para-as-atividades', {'Atividades e tempo entre missões': 'Tempo para as atividades', 'Tempo entre missões': 'Tempo para as atividades'}),
    '41-pactos-e-promessas.md': ('09-pactos-e-entidades.md', {'Pactos e Promessas': 'Pactos e entidades'}),
    '03-as-batidas-no-anexo-consulta.md': ('01-sua-primeira-missao.md#as-batidas-no-anexo-preparo-para-consulta', {}),
    '80-escolher-e-usar-as-ferramentas.md': ('consultas/LEIA-ME.md', {}),
    '37-recompensas-e-fechamento.md': ('08-entre-missoes.md#86-recompensas-e-progressao', {'Encerrar a missão e entregar recompensas': 'Recompensas e progressão'}),
}
FICAM = {'27-convivencia-do-receptaculo.md', '92-reserva-condensada-proposta-e-comparacao.md'}  # sem cópia revista: decisão pendente
FICAM_EM = {('08-entre-missoes.md', '37-recompensas-e-fechamento.md')}  # o capítulo apontaria para si mesmo
LNK = re.compile(r'\[([^\]]+)\]\(<?([^)>#]+\.md)(#[^)>]*)?>?\)')
def novo_link(f, m):
    texto, alvo, frag = m.group(1), m.group(2), m.group(3) or ''
    base = (S / f).parent; dest = (base / alvo).resolve()
    if dest.parent != G.resolve(): return None
    if dest.name in revisto:
        novo = os.path.relpath(revisto[dest.name], base); motivo = 'Remissão: aponta para a cópia revista.'
    elif dest.name in CAP and dest.name not in FICAM and (f, dest.name) not in FICAM_EM:
        d, titulos = CAP[dest.name]; novo = os.path.relpath(S / d.split('#')[0], base) + ('#' + d.split('#')[1] if '#' in d else '')
        texto = titulos.get(texto, texto); frag = ''; motivo = 'Remissão: aponta para a seção nova que recebeu o conteúdo (mapa do registro 99).'
    else:
        return None
    return f'[{texto}](<{novo}{frag}>)', motivo
for f in list(txt):
    def troca(m):
        r = novo_link(f, m)
        if not r: return m.group(0)
        log.append({'arquivo': f, 'antes': m.group(0), 'depois': r[0], 'vezes': 1, 'motivo': r[1]}); return r[0]
    txt[f] = LNK.sub(troca, txt[f])

# ------------------------------------------------------------------ 4. links para o computador e para arquivos de trabalho
ABS = 'Remissão: o Livro de Regras 1.0 é citado pelo nome da regra, sem caminho do computador.'
for f in list(txt):
    def tira(m):
        log.append({'arquivo': f, 'antes': m.group(0), 'depois': m.group(1), 'vezes': 1, 'motivo': ABS}); return m.group(1)
    txt[f] = re.sub(r'\[([^\]]+)\]\(</home/[^>]*>\)', tira, txt[f])
REG = 'Remissão: as regras são citadas pelo Livro de Regras 1.0, não por um arquivo de trabalho.'
def reg(f, frase_link, novo, motivo=REG):
    m = re.search(re.escape(frase_link[0]) + r'\[' + re.escape(frase_link[1]) + r'\]\(<[^>]*Planejamento[^>]*>\)' + re.escape(frase_link[2]), txt[f])
    if not m: sys.exit(f'{f}: não achei {frase_link}')
    sub(f, m.group(0), novo, motivo)
reg('04-na-mesa-de-jogo.md', ('As ', 'regras usadas aqui', ' ficam acessíveis para consulta.'), 'As regras usadas aqui estão no Livro de Regras 1.0.')
reg('06-inimigos-e-perigos.md', ('As ', 'regras usadas aqui', ' estão disponíveis para consulta.'), 'As regras usadas aqui estão no Livro de Regras 1.0.')
reg('07-personagens-e-tecnicas.md', ('com as ', 'regras usadas aqui', ' disponíveis para consulta.'), 'com o Livro de Regras 1.0 à mão.')
reg('08-entre-missoes.md', ('As ', 'regras usadas aqui', ' e os casos completos ficam disponíveis para consulta.'), 'As regras usadas aqui estão no Livro de Regras 1.0, e os casos completos ficam disponíveis para consulta.')
reg('09-pactos-e-entidades.md', ('As ', 'regras usadas aqui', ' ficam disponíveis para consulta.'), 'As regras usadas aqui estão no Livro de Regras 1.0.')
reg('10-jogar-em-guilda.md', ('As ', 'regras usadas aqui', ' ficam disponíveis para conferir os exemplos e a continuidade das fichas.'), 'As regras usadas aqui estão no Livro de Regras 1.0 e servem para conferir os exemplos e a continuidade das fichas.')
reg('10-jogar-em-guilda.md', ('', 'Folhas para a mesa', ''), '[Folhas para a mesa](<consultas/LEIA-ME.md>)', 'Remissão: aponta para o guia das folhas, no livro.')
PROC = 'Remissão: registro de trabalho não é leitura do livro; a frase conserva a informação.'
reg('casos/71-sineiro-do-recolhimento.md', ('A ', 'comparação com referências de nível 6', ' levou'), 'A comparação com referências de nível 6 levou', PROC)
reg('casos/72-sineiro-consulta-e-doma.md', ('**Revisão numérica do confronto:** ', 'registro 73', '. '), '', PROC)
reg('casos/73-ensaio-guiado-do-sineiro.md', ('na ', 'revisão numérica do Sineiro', '.'), 'na revisão numérica do Sineiro.', PROC)
reg('casos/77-ficha-preenchida-ren-e-sora.md', (' do percurso, documentadas no ', 'registro 76', '.'), ' do percurso.', PROC)

for f, t in txt.items(): (S / f).write_text(t)
(A / 'alteracoes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n')
from collections import Counter
print(Counter(e['motivo'].split(':')[0] + ': ' + e['motivo'].split(':')[1][:40] for e in log))
print('arquivos alterados:', sum(1 for f in txt if txt[f] != (ANTES / f).read_text()))
