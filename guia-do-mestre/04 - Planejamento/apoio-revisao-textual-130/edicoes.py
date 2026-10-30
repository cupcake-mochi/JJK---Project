"""Edições da primeira passagem do lote B5-03 (registro 130). Lidas por REVISAR.py."""
COPIA = 'Criar cópia e apontar as remissões para as cópias revistas vizinhas ou para as fontes ainda não revistas.'
CLARO = 'Clareza: frase direta, termo do Livro de Regras 1.0 ou ordem de leitura.'
PENTE = 'Pente fino da segunda leitura, na prova completa.'


def orig(*names):
    return [(f']({n})', f'](<../../{n}>)') for n in names]


def sib(*names):
    return [(f']({n})', f'](<{n}>)') for n in names]


LINKS = {
    's052': orig('03-as-batidas-no-anexo-consulta.md') + [('](<../04 - Planejamento/14-base-pequena-de-inimigos-r53.md>)', '](<../../../04 - Planejamento/14-base-pequena-de-inimigos-r53.md>)')],
    's053': [],
    's054': sib('52-domar-o-amontoado.md'),
    's055': [],
}
MULTI = {'s055': [('](45-tempo-materiais-e-retomada-de-entidades.md)', '](<45-tempo-materiais-e-retomada-de-entidades.md>)')]}

E = []
def e(caso, antes, depois, motivo=CLARO, passagem=1, tipo='clareza'):
    E.append((caso, passagem, tipo, motivo, antes, depois))

e('s055', 'Retome o projeto de [reconstrução](46-reconstruir-transferir-e-herdar-entidades.md):', 'Retome o projeto de [reconstrução](<46-reconstruir-transferir-e-herdar-entidades.md>):', COPIA, tipo='copia_e_remissoes')

# ---------------------------------------------------------------- s052
e('s052', 'e a [Três maldições para a missão]', 'e as [Três maldições para a missão]', 'Correção de concordância.')
e('s052', 'Apresente a Nara a ficha que poderá receber.', 'Mostre a Nara, antes da luta, a ficha que ela poderá receber.')

# ---------------------------------------------------------------- s053
e('s053', 'Esta seção mostra como criar uma ficha e acompanhá-la ao longo dos níveis.', 'Esta seção mostra como criar a ficha de uma entidade e acompanhá-la ao longo dos níveis.')

# ---------------------------------------------------------------- s054
e('s054', 'Ren, nível 2, possui uma técnica que cria animais de papel.',
  'Ren, nível 2, possui uma técnica que cria animais de papel. É um personagem deste exemplo, não o atacante de nível 6 da dupla Ren e Sora.',
  'Clareza: o mesmo nome aparece no inimigo de nível 6; a ressalva evita a leitura de contradição, como nos lotes anteriores.')

# ---------------------------------------------------------------- s055
e('s055', '**Exemplo para a pré-1.0.**', '**Exemplo experimental para a pré-1.0.**', 'Clareza: mesmo aviso dos outros exemplos de entidade.')
