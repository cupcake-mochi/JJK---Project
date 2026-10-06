# -*- coding: utf-8 -*-
"""Leitura do livro reconstruído, que é o dono do Fundamento desde a v0.337.

Até a v0.336 sete validadores abriam o manual do Fundamento v7 (`.docx`). No passo 5
da migração (PLANO.md em sistema/05-material/livro/planejamento-editorial/
migracao-pos-candidata) o `.docx` foi para o arquivo, e eles passaram a ler os
manuscritos das unidades do livro. Este arquivo só sabe ACHAR e PICOTAR o texto:
nenhum número de regra mora aqui.

Cada unidade é lida do lote que a consolidação usa (o `fontes.txt` da cadeia). Se o
lote mudar, troque o caminho aqui e em nenhum outro lugar.

Tudo que não acha o que procura levanta `LivroMudou`, para o validador falhar alto
em vez de conferir menos em silêncio.
"""
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
BASE = os.path.join(RAIZ, 'sistema', '05-material', 'livro', 'planejamento-editorial')

UNIDADES = {
    'abertura': 'abertura/lote-01/ABERTURA-E-CRIACAO.md',
    'regras-gerais': 'regras-gerais/lote-final/REGRAS-GERAIS.md',
    'dano': 'dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md',
    'origens': 'origens/lote-01/ORIGENS-E-LEGADOS.md',
    'pericias': 'pericias-e-oficios/lote-01/PERICIAS-E-OFICIOS.md',
    'equipamento': 'equipamento/lote-final/EQUIPAMENTO.md',
    'progressao': 'progressao/lote-01/PROGRESSAO.md',
    'fundamento': 'fundamento/lote-01/FUNDAMENTO.md',
    'catalogo': 'catalogo/lote-01/CATALOGO.md',
    'aptidoes': 'aptidoes/lote-01/APTIDOES-E-REFINO.md',
    'rotas': 'rotas/lote-01/ROTAS.md',
    'poderes': 'poderes-avancados/lote-01/PODERES-AVANCADOS.md',
    'ritual': 'ritual-e-pactos/lote-01/RITUAL-E-PACTOS.md',
    'consulta': 'consulta/lote-01/CONSULTA.md',
}


class LivroMudou(Exception):
    """O livro não tem mais a forma que o validador espera."""


def caminho(unidade):
    return os.path.join(BASE, UNIDADES[unidade])


def texto(unidade):
    with open(caminho(unidade), encoding='utf-8') as fh:
        return fh.read()


def limpa(cel):
    """Tira negrito, itálico, crase e espaço de uma célula ou título."""
    return re.sub(r'[*`_]', '', cel).strip()


def secao(txt, titulo, nivel=None):
    """O corpo da seção cujo título é `titulo` (comparado sem marcação), até o
    próximo título de nível igual ou maior. `nivel` = número de #; sem ele, aceita
    qualquer nível."""
    linhas = txt.split('\n')
    achou = None
    for i, l in enumerate(linhas):
        m = re.match(r'^(#+)\s+(.*)$', l)
        if m and limpa(m.group(2)) == titulo and (nivel is None or len(m.group(1)) == nivel):
            if achou is not None:
                raise LivroMudou(f'o título "{titulo}" aparece mais de uma vez')
            achou = (i, len(m.group(1)))
    if achou is None:
        raise LivroMudou(f'não achei o título "{titulo}"')
    i, n = achou
    fim = len(linhas)
    for j in range(i + 1, len(linhas)):
        m = re.match(r'^(#+)\s', linhas[j])
        if m and len(m.group(1)) <= n:
            fim = j
            break
    return '\n'.join(linhas[i + 1:fim])


def tabelas(txt):
    """Todas as tabelas markdown do texto, cada uma como lista de linhas (a
    primeira é o cabeçalho; a de traços sai). Células limpas de marcação."""
    saida, atual = [], []
    for l in txt.split('\n') + ['']:
        s = l.strip()
        if s.startswith('|'):
            cels = [limpa(c) for c in s.strip('|').split('|')]
            if not all(re.fullmatch(r':?-+:?', c) for c in cels if c):
                atual.append(cels)
        elif atual:
            saida.append(atual)
            atual = []
    return saida


def tabela(txt, *colunas):
    """A ÚNICA tabela cujo cabeçalho tem todas as `colunas`. Devolve uma lista de
    dicionários coluna -> célula."""
    achadas = [t for t in tabelas(txt) if all(c in t[0] for c in colunas)]
    if len(achadas) != 1:
        raise LivroMudou(f'esperava uma tabela com as colunas {list(colunas)} e achei {len(achadas)}')
    cab = achadas[0][0]
    return [dict(zip(cab, linha)) for linha in achadas[0][1:]]


def tabelas_com(txt, *colunas):
    """Todas as tabelas cujo cabeçalho tem as `colunas`, emendadas numa lista de
    dicionários (para tabelas partidas em duas, como a da Progressão)."""
    achadas = [t for t in tabelas(txt) if all(c in t[0] for c in colunas)]
    if not achadas:
        raise LivroMudou(f'não achei tabela com as colunas {list(colunas)}')
    saida = []
    for t in achadas:
        saida += [dict(zip(t[0], linha)) for linha in t[1:]]
    return saida


def paginas(txt):
    """As páginas do manuscrito, pela marca `<!-- page:id|Título -->`: lista de
    (id, título, corpo). O corpo vai até a próxima marca."""
    marcas = list(re.finditer(r'^<!-- page:([^|]+)\|([^>]*?) -->$', txt, re.M))
    if not marcas:
        raise LivroMudou('o manuscrito não tem marca de página')
    return [(m.group(1), m.group(2).strip(),
             txt[m.end():marcas[i + 1].start() if i + 1 < len(marcas) else len(txt)])
            for i, m in enumerate(marcas)]


def _entradas(corpo, nivel):
    """(título, primeira linha não vazia do corpo, corpo) de cada título de `nivel`."""
    partes = re.split(r'^(#{%d} .+)$' % nivel, corpo, flags=re.M)
    saida = []
    for i in range(1, len(partes), 2):
        tit = limpa(partes[i].lstrip('#'))
        corpo_i = re.split(r'^#{1,%d} ' % nivel, partes[i + 1], maxsplit=1, flags=re.M)[0]
        prim = next((l.strip() for l in corpo_i.split('\n') if l.strip()), '')
        saida.append((tit, prim, corpo_i))
    return saida


PRECO = r'(Leve|Média|Pesada)'


def catalogo():
    """As entradas do Catálogo do livro: nome -> dict com `tipo` (Melhoria,
    Restrição ou Talento), `preco` (Melhoria: Leve, Média ou Pesada; Restrição: a
    devolução; Talento: a Categoria de Efeito), `familia` (Melhoria) e `texto`.

    De onde vem cada campo, sem lista escrita aqui:
      - a Família é a página: a tabela "Melhorias por Família" liga cada Família à
        página que a abre (`cat-alcance`), e as páginas seguintes sem Família própria
        (`cat-movimento`) continuam a anterior, na ordem do livro;
      - a Melhoria é um título `##` cuja primeira frase é "Preço: X." ou cujo título
        traz o preço ("Impulso  -  Leve"); um título com duas ("Concentrada  -  Leve
        / Duradoura  -  Média") vira duas;
      - a Restrição é um título `##` das páginas `cat-restricoes-*` cuja primeira
        frase é "Devolução: X.";
      - o Talento é todo título `##` das páginas `cat-passivas-*`, mais a Regra
        Própria e o Talento Próprio, que são página inteira.
    """
    txt = texto('catalogo')
    pags = paginas(txt)
    fam_de = {}
    for linha in tabela(txt, 'Família', 'O que você encontra'):
        m = re.match(r'\[(.+?)\]\(#(cat-[a-z]+)\)', linha['Família'])
        if not m:
            raise LivroMudou(f'a linha "{linha["Família"]}" da tabela de Famílias não liga a uma página')
        fam_de[m.group(2)] = m.group(1)
    saida = {}

    def poe(nome, d):
        if nome in saida:
            raise LivroMudou(f'a entrada "{nome}" aparece duas vezes no Catálogo')
        saida[nome] = d

    fam = ultima_cat = None
    for pid, ptit, corpo in pags:
        if pid in fam_de:
            fam = fam_de[pid]
        if pid in ('cat-regra-propria', 'cat-passiva-propria'):
            poe(ptit, {'tipo': 'Talento', 'preco': None, 'texto': corpo})
        elif pid.startswith('cat-restricoes'):
            for tit, prim, c in _entradas(corpo, 2):
                m = re.match(r'\*\*Devolução: ([^*]+?)\.\*\*', prim)
                if m:
                    poe(tit, {'tipo': 'Restrição', 'preco': m.group(1), 'texto': c})
        elif pid.startswith('cat-passiva'):
            cat = re.search(r'Categoria (\d)', ptit)
            cat = cat.group(1) if cat else None
            if cat is None:
                # "Proteção e presença" continua a Categoria da página anterior
                cat = ultima_cat
            ultima_cat = cat
            for tit, prim, c in _entradas(corpo, 2):
                poe(tit, {'tipo': 'Talento', 'preco': cat, 'texto': c})
        elif pid == 'cat-proprio' or (fam and pid.startswith('cat-')):
            if pid == 'cat-proprio':
                m = re.match(r'\*\*Preço: ([^*]+?)\.?\*\*', next(l.strip() for l in corpo.split('\n') if l.strip() and not l.startswith('#')))
                poe(ptit, {'tipo': 'Melhoria', 'preco': m.group(1) if m else None, 'familia': None, 'texto': corpo})
                continue
            for tit, prim, c in _entradas(corpo, 2):
                partes = [p.strip() for p in tit.split(' / ')]
                com_preco = [re.fullmatch(r'(.+?)\s+-\s+' + PRECO, p) for p in partes]
                if all(com_preco):
                    for m in com_preco:
                        poe(m.group(1).strip(), {'tipo': 'Melhoria', 'preco': m.group(2), 'familia': fam, 'texto': c})
                    continue
                m = re.match(r'\*\*Preço: ([^*]+?)\.\*\*', prim)
                if m:
                    poe(tit, {'tipo': 'Melhoria', 'preco': m.group(1), 'familia': fam, 'texto': c})
    return saida


# Os dois títulos das seções de condição que não são condição. São os únicos que a
# extração pula; um título novo qualquer entra como condição, e quem compara com a
# peça 19 acende.
NAO_SAO_CONDICAO = {'Remoção', 'Testes de saída'}


def condicoes():
    """Nível -> nomes das condições, das três seções do capítulo de Dano."""
    txt = texto('dano')
    saida = {}
    for nivel, tit in (('Leve', 'Condições leves'), ('Média', 'Condições médias'),
                       ('Pesada', 'Condições pesadas')):
        corpo = secao(txt, tit, 1)
        saida[nivel] = [limpa(x) for x in re.findall(r'^## (.+)$', corpo, re.M)
                        if limpa(x) not in NAO_SAO_CONDICAO]
    return saida


def familias():
    return [r['Família'] for r in tabela(texto('fundamento'), 'Família', 'Aplicações')]


def formas():
    """As Formas, das tabelas do Fundamento com as colunas Forma e Custo."""
    achadas = [t for t in tabelas(texto('fundamento')) if t[0][:2] == ['Forma', 'Custo']]
    if not achadas:
        raise LivroMudou('não achei as tabelas de Forma do Fundamento')
    return [linha[0] for t in achadas for linha in t[1:]]
