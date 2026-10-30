"""Edições da primeira passagem do lote B4-01 (registro 127). Lidas por REVISAR.py."""
COPIA = 'Criar cópia e apontar as remissões para as cópias revistas vizinhas ou para as fontes ainda não revistas.'
CLARO = 'Clareza: frase direta, termo do Livro de Regras 1.0 ou ordem de leitura.'
PENTE = 'Pente fino da segunda leitura, na prova completa.'


def orig(*names):
    return [(f']({n})', f'](<../../{n}>)') for n in names]


def sib(*names):
    return [(f']({n})', f'](<{n}>)') for n in names]


LINKS = {
    's034': orig('38-ficha-de-projeto-e-entrega.md', '39-atividades-e-tempo-entre-missoes.md')
            + sib('85-trajetorias-ferramentas-e-improvisacao.md', '36-ferramentas-objetos-e-contencao.md', '96-fabricar-e-identificar-o-anel.md', '90-reparar-personagem-de-corpo-construido.md'),
    's036': orig('29-avaliar-tecnicas-e-criacoes.md') + sib('96-fabricar-e-identificar-o-anel.md', '98-objeto-selado-e-risco-de-ingestao.md'),
    's096': [],
    's097': sib('96-fabricar-e-identificar-o-anel.md'),
    's098': sib('96-fabricar-e-identificar-o-anel.md'),
    's099': orig('25-conferir-personagens.md'),
}
MULTI = {}

E = []
def e(caso, antes, depois, motivo=CLARO, passagem=1, tipo='clareza'):
    E.append((caso, passagem, tipo, motivo, antes, depois))

# ---------------------------------------------------------------- s034
e('s034', 'Os futuros treinamentos específicos terão seus próprios benefícios e manutenção quando forem desenvolvidos.',
  'Treinamentos específicos ainda não têm regras próprias aprovadas; não os presuma a partir de um projeto concluído.',
  'Clareza e decisão vigente: o texto prometia benefícios de treinamentos futuros; o Guia não apresenta pacote mecânico de treinamento.')
e('s034', 'Não conclua o serviço só porque a jogadora terminou sua postagem.', 'Não conclua o serviço só porque a jogadora encerrou sua participação naquele momento.',
  'Clareza: vale para mesa presencial e on-line.')
e('s034', 'Escolha o Ofício pelo trabalho necessário.', 'Escolha o Ofício pelo trabalho que precisa ser feito.')

# ---------------------------------------------------------------- s036
e('s036', 'Ferramenta e objeto amaldiçoado têm funções distintas no Livro de Regras 1.0: a primeira serve como equipamento; o segundo pode continuar produzindo perigo enquanto está guardado.',
  'No Livro de Regras 1.0, ferramenta e objeto amaldiçoado têm funções diferentes: a ferramenta serve como equipamento; o objeto pode continuar produzindo perigo mesmo guardado.')
e('s036', 'Use testes quando houver incerteza e consequência.', 'Peça testes quando houver incerteza e consequência.')

# ---------------------------------------------------------------- s096
e('s096', 'Use este caso para preparar a ficha de uma ferramenta, descobrir seu funcionamento e contratar sua fabricação.',
  'Use este caso para preparar a ficha de uma ferramenta, deixar o grupo descobrir seu funcionamento e contratar sua fabricação.')

# ---------------------------------------------------------------- s097
e('s097', 'Use estes casos para distinguir acesso ao cofre, propriedade de um item e resultado de uma negociação.',
  'Use estes casos para separar três coisas: acesso ao cofre, propriedade de um item e resultado de uma negociação.')

# ---------------------------------------------------------------- s098
e('s098', 'Elas não definem como forçar a ingestão numa criatura hostil nem substitui as regras de ataque e resistência para tentar isso.',
  'Elas não definem como forçar a ingestão numa criatura hostil nem substituem as regras de ataque e resistência para tentar isso.',
  'Correção de concordância: o sujeito é "as regras abaixo".')

# ---------------------------------------------------------------- s099
e('s099', 'Use este caso para conferir um feito do **Limiar**, a exigência especial para sair do nível 20, e depois registrar uma decisão de patente.',
  'Use este caso para conferir um feito do **Limiar**, exigido para sair do nível 20, e depois registrar uma decisão de patente.')
