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


def traduz(txt):
    """Texto com o nome antigo -> o mesmo texto com o nome novo."""
    txt = _guarda_aberta(txt)
    for antigo, novo, _ in RENOMES[1:]:
        txt = re.sub(r'\b' + re.escape(antigo) + r'\b', novo, txt)
    return txt


def traduz_nome(nome, categoria=None):
    """Um nome solto de uma lista do manual. `categoria` resolve o `Aviso`."""
    if (categoria, nome) in POR_CATEGORIA:
        return POR_CATEGORIA[(categoria, nome)][0]
    for antigo, novo, _ in RENOMES:
        if nome == antigo:
            return novo
    return nome


def antigos():
    """Os nomes antigos que a triagem trata como termo morto. `Aviso` fica de fora:
    com maiúscula ele também é palavra comum no começo de frase."""
    return {a: n for a, n, _ in RENOMES}
