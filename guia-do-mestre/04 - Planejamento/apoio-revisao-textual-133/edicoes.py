"""Edições da primeira passagem do lote C-03 das consultas complementares (registro 133). Lidas por REVISAR.py.

As cópias ficam em revisao-98/consultas/. Remissões para capítulos antigos apontam para o capítulo novo
que recebeu o conteúdo, conforme o mapa de destinos do registro 99 (estrutura-e-fontes.json):
Atividades e tempo (s039) foi para Entre missões, 8.2; Pactos e Promessas (s041) para Pactos e entidades;
Criar inimigos (s056) para Inimigos e perigos. Os casos já têm cópias revistas em revisao-98/casos."""
COPIA = 'Criar cópia e apontar as remissões para os capítulos novos e cópias revistas, conforme o mapa de destinos do registro 99.'
CLARO = 'Clareza: frase direta, termo do Livro de Regras 1.0 ou ordem de leitura.'
PENTE = 'Pente fino da segunda leitura, na prova completa.'


def caso(*names):
    return [(f']({n})', f'](<../casos/{n}>)') for n in names]


def irma(*names):
    return [(f']({n})', f'](<{n}>)') for n in names]


LINKS = {
    's040': [('Consulte [Atividades e tempo entre missões](39-atividades-e-tempo-entre-missoes.md) para',
              'Consulte [Tempo para as atividades](<../08-entre-missoes.md>), no capítulo Entre missões, para')],
    's042': [('Use esta folha junto de [Pactos e Promessas](41-pactos-e-promessas.md).',
              'Use esta folha junto do capítulo [Pactos e entidades](<../09-pactos-e-entidades.md>).')]
            + caso('50-promessa-do-arquivo.md'),
    's044': caso('45-tempo-materiais-e-retomada-de-entidades.md', '46-reconstruir-transferir-e-herdar-entidades.md', '51-ritual-do-cao-de-sombra.md',
                 '52-domar-o-amontoado.md', '53-construir-e-evoluir-o-escriba.md', '54-transporte-e-continuidade-das-entidades.md',
                 '55-fabricar-e-evoluir-o-vigia-do-deposito.md'),
    's058': [('Ela acompanha o [método principal](56-preparar-inimigos-e-avaliar-encontros.md).',
              'Ela acompanha o capítulo [Inimigos e perigos](<../06-inimigos-e-perigos.md>).')]
            + caso('77-ficha-preenchida-ren-e-sora.md', '78-preparar-perigos-ambientais.md', '79-o-po-na-sala-de-conservacao.md', '68-ficha-e-comparacao-de-chefes.md')
            + irma('61-ficha-de-habilidade-de-inimigo.md', '24-registro-de-estado-e-socorro.md'),
    's061': irma('58-ficha-de-inimigo-e-encontro.md') + caso('60-montar-habilidades-de-inimigos.md', '62-o-carregador-e-o-corredor-de-entulho.md', '63-carregador-consulta-e-doma.md'),
}
MULTI = {}

E = []
def e(caso_, antes, depois, motivo=CLARO, passagem=1, tipo='clareza'):
    E.append((caso_, passagem, tipo, motivo, antes, depois))

# ---------------------------------------------------------------- s040
e('s040', 'O padrão recomendado é 28 horas novas a cada ciclo comum de sete dias, com saldo da concessão anterior válido apenas no ciclo seguinte.',
  'O padrão recomendado é 28 horas novas a cada ciclo comum de sete dias. O que sobrar das horas novas de um ciclo vale só no ciclo seguinte.',
  'Clareza: separa a concessão da validade do saldo.')
e('s040', 'Contando os dias 5, 6 e 7, recebe', 'Contando os dias 5, 6 e 7, a quatro horas por dia, recebe',
  'Clareza: mostra de onde vem o 4 da conta (28 horas em sete dias).')

# ---------------------------------------------------------------- s058
e('s058', '**Use esta ficha para preparar o encontro e registrar o resultado.**',
  '**Use esta ficha para preparar o encontro e, depois, registrar o resultado.**',
  'Clareza: ordem de uso — o bloco 6 é preenchido depois da aplicação.')

# ---------------------------------------------------------------- s061
e('s061', '**Aprofundamento opcional da ficha única.** Registre a capacidade no bloco 3 da [ficha de construção e encontro](<58-ficha-de-inimigo-e-encontro.md>).',
  '**Aprofundamento opcional da [ficha de inimigo e encontro](<58-ficha-de-inimigo-e-encontro.md>).** Registre a capacidade no bloco 3 dela.',
  'Clareza: a mesma ficha aparecia com dois nomes ("ficha única" e "ficha de construção e encontro"); fica o título dela.')
