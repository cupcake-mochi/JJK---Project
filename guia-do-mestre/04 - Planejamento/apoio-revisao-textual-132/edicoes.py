"""Edições da primeira passagem do lote C-02 das consultas complementares (registro 132). Lidas por REVISAR.py.

As cópias ficam em revisao-98/consultas/. Remissões para capítulos antigos apontam para o capítulo novo
que recebeu o conteúdo, conforme o mapa de destinos do registro 99 (estrutura-e-fontes.json):
A sessão zero (s007) e Facções (s017) foram para Criar uma campanha (5.1 e 5.4)."""
COPIA = 'Criar cópia e apontar as remissões para os capítulos novos e cópias revistas, conforme o mapa de destinos do registro 99.'
CLARO = 'Clareza: frase direta, termo do Livro de Regras 1.0 ou ordem de leitura.'
PENTE = 'Pente fino da segunda leitura, na prova completa.'


def caso(*names):
    return [(f']({n})', f'](<../casos/{n}>)') for n in names]


def irma(*names):
    return [(f']({n})', f'](<{n}>)') for n in names]


LINKS = {
    's008': [('Use [A sessão zero](07-preparar-o-grupo.md) para conduzir a conversa.',
              'Use [A sessão zero](<../05-criar-uma-campanha.md>), no capítulo Criar uma campanha, para conduzir a conversa.')],
    's012': irma('02-ficha-de-preparacao.md') + caso('83-perceber-procurar-e-interpretar-sinais.md'),
    's020': [('[Facções](17-faccoes-e-reacoes.md) explica', '[Facções](<../05-criar-uma-campanha.md>), no capítulo Criar uma campanha, explica')]
            + irma('16-linha-de-continuidade.md'),
    's028': irma('08-ficha-de-acordos-do-grupo.md'),
    's032': caso('30-pareceres-de-criacoes.md'),
    's038': caso('96-fabricar-e-identificar-o-anel.md'),
}
MULTI = {}

E = []
def e(caso_, antes, depois, motivo=CLARO, passagem=1, tipo='clareza'):
    E.append((caso_, passagem, tipo, motivo, antes, depois))

# ---------------------------------------------------------------- s008
e('s008', 'Preencha com os participantes antes do início e retome',
  'Preencha junto com os participantes antes da primeira sessão e retome',
  'Clareza: a ficha é preenchida em conjunto, antes da primeira sessão.')

# ---------------------------------------------------------------- s012
e('s012', 'Neste exemplo, o grupo conferiu os funcionários e conversou com Davi.',
  'Este exemplo usa a missão de [Sua primeira missão](<../01-sua-primeira-missao.md>). O grupo já conferiu os funcionários e conversou com Davi.',
  'Clareza: identifica de onde vem o exemplo do anexo.')
e('s012', 'Registrar o telefonema e a resposta quando ocorrerem; sua possibilidade não significa que o grupo já o realizou.',
  'Registre o telefonema e a resposta só quando acontecerem; poder ligar não significa que o grupo já ligou.')

# ---------------------------------------------------------------- s020
e('s020', 'Para um contato isolado, uma nota de pessoa na ficha de missão pode bastar.',
  'Para um contato isolado, uma nota em Pessoas, na [ficha de preparação](<02-ficha-de-preparacao.md>), pode bastar.',
  'Clareza: nomeia a ficha e o campo, que é a seção Pessoas da ficha de preparação.')
e('s020', 'Organização original para este exemplo;', 'Organização criada para este exemplo;',
  'Clareza: "original" podia ser lido como "da obra".')

# ---------------------------------------------------------------- s028
e('s028', 'Outros casos podem aproveitar os campos pertinentes, respeitando suas próprias Origens.',
  'Outras relações podem aproveitar os campos pertinentes, respeitando as regras de cada Origem.',
  'Clareza: "casos" se confundia com os casos do guia.')
e('s028', 'Conselho Interior permite a repetição prevista de Intuição ou Ocultismo, com uso compartilhado por cena.',
  'Conselho Interior permite, uma vez por cena, repetir um teste falho de Intuição ou Ocultismo e aceitar o segundo resultado; as duas perícias compartilham o uso.',
  'Clareza: mesma formulação do Livro de Regras 1.0 (Conselho Interior).')
