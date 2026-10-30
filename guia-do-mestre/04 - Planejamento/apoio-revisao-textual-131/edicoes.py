"""Edições da primeira passagem do lote C-01 das consultas complementares (registro 131). Lidas por REVISAR.py.

As cópias ficam em revisao-98/consultas/. Remissões para capítulos antigos apontam para o capítulo novo
que recebeu o conteúdo, conforme o mapa de destinos do registro 99 (estrutura-e-fontes.json)."""
COPIA = 'Criar cópia e apontar as remissões para os capítulos novos e cópias revistas, conforme o mapa de destinos do registro 99.'
CLARO = 'Clareza: frase direta, termo do Livro de Regras 1.0 ou ordem de leitura.'
PENTE = 'Pente fino da segunda leitura, na prova completa.'


def caso(*names):
    return [(f']({n})', f'](<../casos/{n}>)') for n in names]


def irma(*names):
    return [(f']({n})', f'](<{n}>)') for n in names]


def orig(*names):
    return [(f']({n})', f'](<../../{n}>)') for n in names]


LINKS = {
    's002': [('O capítulo [Preparar uma missão](01-preparar-uma-missao.md) explica', 'O capítulo [Preparar aventuras](<../03-preparar-aventuras.md>) explica'),
             ('Há um [exemplo preenchido](03-as-batidas-no-anexo-consulta.md).', 'Há um exemplo preenchido em [Sua primeira missão](<../01-sua-primeira-missao.md>).'),
             ('[Registros para a campanha](80-escolher-e-usar-as-ferramentas.md) orienta', '[Escolher uma folha para a mesa](<LEIA-ME.md>) orienta')]
            + irma('24-registro-de-estado-e-socorro.md', '16-linha-de-continuidade.md'),
    's005': [('depois de ler [Conduzir uma sessão](04-conduzir-uma-sessao.md).', 'depois de ler [Na mesa de jogo](<../04-na-mesa-de-jogo.md>).'),
             ('[investigação em andamento](10-investigacao-em-andamento.md)', '[conduzir uma investigação](<../04-na-mesa-de-jogo.md>)'),
             ('[acompanhamento](21-acompanhar-recursos.md)', '[acompanhar recursos](<../04-na-mesa-de-jogo.md>)'),
]
            + caso('83-perceber-procurar-e-interpretar-sinais.md', '84-percursos-apoios-e-quedas.md', '85-trajetorias-ferramentas-e-improvisacao.md',
                   '82-testes-trabalho-em-grupo-e-iniciativa.md', '11-espaco-e-usos-criativos.md', '22-quedas-e-socorro.md', '23-retirada-e-recuperacao.md',
                   '81-passar-a-missao-entre-mestres.md')
            + irma('02-ficha-de-preparacao.md', '24-registro-de-estado-e-socorro.md', '16-linha-de-continuidade.md')
            + orig('12-registro-de-descobertas.md'),
    's024': [('[Acompanhar recursos](21-acompanhar-recursos.md)', '[Na mesa de jogo](<../04-na-mesa-de-jogo.md>)')]
            + caso('22-quedas-e-socorro.md', '23-retirada-e-recuperacao.md', '81-passar-a-missao-entre-mestres.md') + irma('16-linha-de-continuidade.md'),
    's016': [('[Escolher as ferramentas](80-escolher-e-usar-as-ferramentas.md) ajuda', '[Escolher uma folha para a mesa](<LEIA-ME.md>) ajuda')]
            + irma('24-registro-de-estado-e-socorro.md') + caso('81-passar-a-missao-entre-mestres.md'),
}
MULTI = {}

E = []
def e(caso_, antes, depois, motivo=CLARO, passagem=1, tipo='clareza'):
    E.append((caso_, passagem, tipo, motivo, antes, depois))

# ---------------------------------------------------------------- s002
e('s002', 'Use este modelo para consulta durante o jogo.', 'Use este modelo para preparar a missão e consultá-lo durante o jogo.',
  'Clareza: a ficha serve também ao preparo, não só ao jogo.')

# ---------------------------------------------------------------- s005
e('s005', 'Ler o Ambiente conserva ação e uso quando não há informação a oferecer.',
  'Ler o Ambiente não gasta a ação nem o uso quando não há nada a informar.', 'Clareza: mesma formulação do Livro de Regras 1.0.')
e('s005', 'Esforço e risco num salto usam uma rolagem contra a maior CD.', 'Num salto com esforço e risco, role uma vez contra a maior CD.')

# ---------------------------------------------------------------- s024
e('s024', 'Use como apoio à ficha durante a missão e na passagem entre mestres.', 'Use junto da ficha durante a missão e na passagem entre mestres.')

# ---------------------------------------------------------------- s016
e('s016', 'Registre mudanças reais e possibilidades futuras separadamente.', 'Registre separadamente as mudanças que já aconteceram e as possibilidades futuras.')
