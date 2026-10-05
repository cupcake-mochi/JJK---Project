# -*- coding: utf-8 -*-
"""Os nomes que o livro reconstruído trocou e que as peças já usam.

Migração da candidata para as peças, passo 2 (PLANO.md em
sistema/05-material/livro/planejamento-editorial/migracao-pos-candidata).

As peças desta pasta passam a usar o nome novo. Três fontes ficam CONGELADAS com o
nome antigo até o passo 5, quando o livro reconstruído substitui todas elas:

  - o livro v0.331 (sistema/05-material/livro/manual e o -TEXTO.md que sai dele);
  - as cópias da edição integrada (caminhos/ e invocacoes/05-Edicao-Integrada), que
    o conferir-invocacoes.py prende por hash à referência aprovada;
  - o manual do Fundamento v7 (.docx), que deixa de ser fonte no passo 5.

Quem lê uma delas e compara com uma peça passa o texto por `traduz()` antes. Este
arquivo é o único dono da tabela: um validador que guardasse a própria cópia dela
divergiria no primeiro renome novo (lição nº 9 do README).

De onde vem cada linha: NT01 a NT06 são o MAPA.json da migração de nomes da
candidata (consolidacao/lote-01/migracao-nomes); EMA27 e ORI02 são registros do
INVENTARIO-ALTERACOES.json da migração.

v0.333: a família da `Passiva` (NT04 a NT06). `Passiva Livre` vira `Expressão da
técnica`, `Classe Passiva` vira `Categoria de Efeito` (a sigla `CP`, `CE`), e
`Passiva` vira `Talento` (`Passiva Própria`, `Talento Próprio`). Só o nome com
maiúscula muda: `passiva` minúscula é adjetivo comum (*proteção passiva*) e fica.
`Talento` é masculino, e por isso o determinante antes dele troca de gênero.
"""
import re

# (antigo, novo, registro). Nome inteiro, com caixa. O gênero do nome novo decide o
# artigo: `Guarda Aberta` é feminino, e por isso a regra de artigo abaixo existe.
RENOMES = [
    ('Incapacitado', 'Guarda Aberta', 'NT01'),
    ('Sobre Carregar Energia', 'Sobrecarregar Energia', 'EMA27'),
    ('Reencarnado', 'Encarnado', 'ORI02'),
]

# `Aviso` era duas entradas do manual com o mesmo nome. O nome novo depende de qual.
POR_CATEGORIA = {
    ('Melhoria', 'Aviso'): ('Identificar Feitiço', 'NT02'),
    ('Passiva', 'Aviso'): ('Leitura de Feitiços', 'NT03'),
}

# `ficar Incapacitado` vira `ficar com a Guarda Aberta`, como na candidata (NT01).
_VERBOS = r'(?:fica|ficar|ficaria|ficou|ficando|está|estiver|esteja|estava|estar)'
# o artigo masculino que vinha antes do nome, e a forma feminina dele
_ARTIGO = {'o': 'a', 'O': 'A', 'do': 'da', 'Do': 'Da', 'pelo': 'pela', 'Pelo': 'Pela',
           'no': 'na', 'No': 'Na', 'ao': 'à', 'Ao': 'À', 'um': 'uma', 'Um': 'Uma'}
_MARCA = r'(\*\*`|`\*\*|\*\*|`|\*)?'


def _guarda_aberta(txt):
    txt = re.sub(r'\b(' + _VERBOS + r') ' + _MARCA + r'Incapacitado\b',
                 lambda m: f'{m[1]} com a {m[2] or ""}Guarda Aberta', txt)
    txt = re.sub(r'\b(' + '|'.join(_ARTIGO) + r') ' + _MARCA + r'Incapacitado\b',
                 lambda m: f'{_ARTIGO[m[1]]} {m[2] or ""}Guarda Aberta', txt)
    return re.sub(r'\bIncapacitado\b', 'Guarda Aberta', txt)


# v0.333: a família da `Passiva`. A ordem importa: os nomes compostos saem antes
# do `Passiva` sozinho, senão `Passiva Livre` viraria `Talento Livre`.
PASSIVA = [
    ('Passivas Livres', 'Expressões da técnica', 'NT04'),
    ('Passiva Livre', 'Expressão da técnica', 'NT04'),
    ('Classes Passivas', 'Categorias de Efeito', 'NT06'),
    ('Classe Passiva', 'Categoria de Efeito', 'NT06'),
    ('Passivas Próprias', 'Talentos Próprios', 'NT05'),
    ('Passiva Própria', 'Talento Próprio', 'NT05'),
    ('Passivas', 'Talentos', 'NT05'),
    ('Passiva', 'Talento', 'NT05'),
]
# o determinante feminino que vinha antes de `Passiva`, e o masculino de `Talento`
_DET_M = {'a': 'o', 'as': 'os', 'da': 'do', 'das': 'dos', 'na': 'no', 'nas': 'nos',
          'pela': 'pelo', 'pelas': 'pelos', 'à': 'ao', 'às': 'aos', 'uma': 'um',
          'umas': 'uns', 'numa': 'num', 'numas': 'nuns', 'dessa': 'desse',
          'dessas': 'desses', 'desta': 'deste', 'destas': 'destes', 'nessa': 'nesse',
          'nessas': 'nesses', 'nesta': 'neste', 'nestas': 'nestes', 'essa': 'esse',
          'essas': 'esses', 'esta': 'este', 'estas': 'estes', 'outra': 'outro',
          'outras': 'outros', 'nenhuma': 'nenhum', 'toda': 'todo', 'todas': 'todos',
          'sua': 'seu', 'suas': 'seus', 'mesma': 'mesmo', 'mesmas': 'mesmos',
          'primeira': 'primeiro', 'segunda': 'segundo', 'terceira': 'terceiro',
          'nova': 'novo', 'novas': 'novos', 'cada': 'cada', 'duas': 'dois',
          'quantas': 'quantos', 'quais': 'quais', 'algumas': 'alguns', 'alguma': 'algum',
          'aquela': 'aquele', 'aquelas': 'aqueles', 'naquela': 'naquele',
          'dela': 'dela', 'muitas': 'muitos', 'poucas': 'poucos', 'várias': 'vários'}
_MARCA_P = r'((?:\*\*|`|\*|\[)*)'


def _det(m):
    w = m[1]
    novo = _DET_M.get(w.lower(), w)
    if w[:1].isupper():
        novo = novo[:1].upper() + novo[1:]
    return novo


def _passiva(txt):
    for antigo, novo, _ in PASSIVA:
        masc = novo.startswith('Talento')
        if masc:
            dets = '|'.join(sorted(_DET_M, key=len, reverse=True))
            txt = re.sub(r'\b(' + dets + r')( ' + _MARCA_P + re.escape(antigo) + r'\b)',
                         lambda m: _det(m) + m[2], txt, flags=re.I)
        txt = re.sub(r'\b' + re.escape(antigo) + r'\b', novo, txt)
    # a sigla da Classe Passiva: `CP 1`, `CP1`, `CPs`
    txt = re.sub(r'\bCP(?=s?\b|\s?[0-9])', 'CE', txt)
    return txt


def traduz(txt):
    """Texto com o nome antigo -> o mesmo texto com o nome novo."""
    txt = _guarda_aberta(txt)
    for antigo, novo, _ in RENOMES[1:]:
        txt = re.sub(r'\b' + re.escape(antigo) + r'\b', novo, txt)
    return _passiva(txt)


def traduz_nome(nome, categoria=None):
    """Um nome solto de uma lista do manual. `categoria` resolve o `Aviso`."""
    if (categoria, nome) in POR_CATEGORIA:
        return POR_CATEGORIA[(categoria, nome)][0]
    for antigo, novo, _ in RENOMES + PASSIVA:
        if nome == antigo:
            return novo
    return nome


def antigos():
    """Os nomes antigos que a triagem trata como termo morto. `Aviso` fica de fora:
    com maiúscula ele também é palavra comum no começo de frase."""
    mortos = {a: n for a, n, _ in RENOMES}
    # v0.333: a família da `Passiva`. A triagem do conferir-nomes casa com caixa, e
    # `passiva` minúscula (adjetivo) não acende.
    mortos.update({a: n for a, n, _ in PASSIVA})
    return mortos
