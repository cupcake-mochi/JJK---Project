"""Edições da primeira passagem do lote B3-01 (registro 125). Lidas por REVISAR.py."""
COPIA = 'Criar cópia e apontar as remissões para as cópias revistas vizinhas ou para as fontes ainda não revistas.'
CLARO = 'Clareza: frase direta, termo do Livro de Regras 1.0 ou ordem de leitura.'
PENTE = 'Pente fino da segunda leitura, na prova completa.'


def orig(*names):
    return [(f']({n})', f'](<../../{n}>)') for n in names]


def sib(*names):
    return [(f']({n})', f'](<{n}>)') for n in names]


LINKS = {
    's090': [],
    's091': orig('53-construir-e-evoluir-o-escriba.md'),
    's030': orig('95-efeitos-de-cena-e-cancelamento.md', '94-compras-repetidas-e-restricoes.md') + sib('89-vida-rolada-e-familia-propria.md'),
    's031': orig('29-avaliar-tecnicas-e-criacoes.md') + sib('22-quedas-e-socorro.md', '91-restricao-corporal-e-cuidados.md'),
}
MULTI = {}

E = []
def e(caso, antes, depois, motivo=CLARO, passagem=1, tipo='clareza'):
    E.append((caso, passagem, tipo, motivo, antes, depois))

# ---------------------------------------------------------------- s090
e('s090', 'O grupo consegue uma pausa segura.', 'O grupo consegue um descanso curto em segurança.',
  'Clareza: no Livro de Regras 1.0, Reparo do corpo acontece durante um descanso curto; "pausa segura" não dizia isso.')
e('s090', 'O atendimento ocupa o trabalho de Rui durante a pausa.', 'O atendimento ocupa o trabalho de Rui durante o descanso curto.', 'Clareza: mesmo termo do Livro de Regras 1.0.')
e('s090', 'Use a permissão específica de Reparo do corpo durante a pausa;', 'Use a permissão específica de Reparo do corpo durante o descanso curto;', 'Clareza: mesmo termo do Livro de Regras 1.0.')
e('s090', 'Compare essas Classes permitidas, não as capacidades que conhecem ou o grau do material.',
  'Compare as Classes permitidas pelos dois níveis, não as capacidades que eles conhecem nem o grau do material.')

# ---------------------------------------------------------------- s091
e('s091', 'Usar um atributo físico na conta de uma conjuração não basta para torná-la inviável.',
  'Usar Força ou Destreza na conta de uma conjuração não a faz falhar por si só.', 'Clareza: mesma formulação do Livro de Regras 1.0.')
e('s091', 'Ao criar outro CE4 ou outra condição, explique o que muda nas regras, como funciona e quais cuidados são necessários com esse mesmo nível de precisão.',
  'Ao criar outro CE4 ou outra condição, explique com a mesma precisão o que muda nas regras, como funciona e quais cuidados são necessários.')

# ---------------------------------------------------------------- s030
e('s030', 'Estes casos mostram como explicar uma avaliação.', 'Estes casos mostram como explicar ao jogador uma avaliação de poder.')
e('s030', 'Mesmo numa ficha de ataque, o alvo acertado faz o TR de Controle.', 'Mesmo numa ficha de ataque, o alvo acertado ainda faz o TR de Prende.',
  'Clareza: o TR é o da Melhoria Prende, da Família Controle.')
e('s030', 'Ela concede a rodada adicional e +2 na CD dos TRs de Prende.', 'Essa escolha concede a rodada adicional e +2 na CD dos TRs de Prende.')

# ---------------------------------------------------------------- s031
e('s031', 'Se Auxiliares já for Livre na técnica, Guarda custa **5 − 3 = 2**;', 'Se Auxiliares já for Livre na técnica, o desconto de metade da Classe, para cima, faz Guarda custar **5 − 3 = 2**;',
  'Clareza: diz de onde vem o desconto.')
e('s031', 'Separe três partes ao ler a proposta.', 'Ao ler a proposta, separe três partes.')
