"""Edições da primeira passagem do lote B3-02 (registro 126). Lidas por REVISAR.py."""
COPIA = 'Criar cópia e apontar as remissões para as cópias revistas vizinhas ou para as fontes ainda não revistas.'
CLARO = 'Clareza: frase direta, termo do Livro de Regras 1.0 ou ordem de leitura.'
PENTE = 'Pente fino da segunda leitura, na prova completa.'


def orig(*names):
    return [(f']({n})', f'](<../../{n}>)') for n in names]


def sib(*names):
    return [(f']({n})', f'](<{n}>)') for n in names]


LINKS = {
    's033': orig('29-avaliar-tecnicas-e-criacoes.md', '92-reserva-condensada-proposta-e-comparacao.md')
            + sib('93-ampliar-mesclas-e-trocar-formas.md', '94-compras-repetidas-e-restricoes.md', '95-efeitos-de-cena-e-cancelamento.md'),
    's093': [],
    's094': [],
    's095': orig('53-construir-e-evoluir-o-escriba.md') + sib('31-avaliar-poderes-avancados.md'),
}
MULTI = {}

E = []
def e(caso, antes, depois, motivo=CLARO, passagem=1, tipo='clareza'):
    E.append((caso, passagem, tipo, motivo, antes, depois))

# ---------------------------------------------------------------- s033
e('s033', 'Consulte estes casos quando a proposta envolver uma permissão particular da ficha.',
  'Consulte estes casos quando um jogador propuser algo que depende de uma permissão específica da ficha.')
e('s033', 'Para conferir Remodelar, use o exemplo do Livro de Regras 1.0:', 'Para conferir Remodelar, acompanhe o exemplo do Livro de Regras 1.0:')
e('s033', 'Refaça também o orçamento com as Restrições que continuam válidas e use o resultado menor quando essa conferência limitar mais a aplicação.',
  'Refaça também o orçamento com as Restrições que continuam válidas; se essa conferência der um resultado menor, use o menor.')
e('s033', 'O limite de distância é medido do criador, ao concluir, até o ponto mais distante da borda.',
  'A distância é medida do criador, no momento em que conclui a Cortina, até o ponto mais distante da borda.')
e('s033', '“Quando estiver me escondendo” é uma tarefa, e não atende a esse critério.', '“Quando estiver me escondendo” descreve uma tarefa, não uma situação física, e não atende a esse critério.')

# ---------------------------------------------------------------- s093
e('s093', 'Use esta consulta para conferir duas formas de alterar um feitiço:', 'Use esta consulta para conferir duas maneiras de alterar um feitiço:',
  'Clareza: "forma" também é termo de regra (Forma); a troca evita a ambiguidade.')
e('s093', 'A cura independe do dano: acontece mesmo se todos os adversários passarem no TR ou não houver inimigo válido.',
  'A cura não depende do dano: acontece mesmo se todos os adversários passarem no TR ou não houver inimigo válido.')

# ---------------------------------------------------------------- s094
e('s094', 'Esta consulta mostra como contar duas compras da mesma Melhoria e como registrar uma limitação que realmente possa impedir ou dificultar o uso.',
  'Esta consulta mostra como contar duas compras da mesma Melhoria e como registrar uma Restrição que de fato impeça ou dificulte o uso.')
e('s094', 'O nome unificado não transforma isso numa única Melhoria Leve.', 'Dar um nome só às duas compras não as transforma numa única Melhoria Leve.')

# ---------------------------------------------------------------- s095
e('s095', 'Tocar a superfície delimita a aplicação de utilidade deste exemplo.', 'Tocar a superfície define onde começa a aplicação de utilidade deste exemplo.')
e('s095', 'Este Efeito fora de combate não pode ser recriado como atalho para uma aplicação de combate.',
  'Rei não pode conjurar de novo este Efeito fora de combate durante a luta como atalho para uma aplicação de combate.')
