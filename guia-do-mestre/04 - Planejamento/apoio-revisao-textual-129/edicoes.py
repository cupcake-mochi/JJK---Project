"""Edições da primeira passagem do lote B5-02 (registro 129). Lidas por REVISAR.py."""
COPIA = 'Criar cópia e apontar as remissões para as cópias revistas vizinhas ou para as fontes ainda não revistas.'
CLARO = 'Clareza: frase direta, termo do Livro de Regras 1.0 ou ordem de leitura.'
PENTE = 'Pente fino da segunda leitura, na prova completa.'


def orig(*names):
    return [(f']({n})', f'](<../../{n}>)') for n in names]


def sib(*names):
    return [(f']({n})', f'](<{n}>)') for n in names]


LINKS = {
    's043': orig('44-registro-de-aquisicao-e-estado-de-entidade.md', '53-construir-e-evoluir-o-escriba.md', '29-avaliar-tecnicas-e-criacoes.md', '52-domar-o-amontoado.md',
                 '38-ficha-de-projeto-e-entrega.md', '39-atividades-e-tempo-entre-missoes.md', '54-transporte-e-continuidade-das-entidades.md')
            + sib('51-ritual-do-cao-de-sombra.md', '45-tempo-materiais-e-retomada-de-entidades.md', '46-reconstruir-transferir-e-herdar-entidades.md')
            + [('](<../04 - Planejamento/14-base-pequena-de-inimigos-r53.md>)', '](<../../../04 - Planejamento/14-base-pequena-de-inimigos-r53.md>)')],
    's045': orig('39-atividades-e-tempo-entre-missoes.md', '55-fabricar-e-evoluir-o-vigia-do-deposito.md', '44-registro-de-aquisicao-e-estado-de-entidade.md', '40-registro-de-dedicacao-por-ficha.md')
            + sib('43-aquisicao-e-projetos-de-entidades.md', '46-reconstruir-transferir-e-herdar-entidades.md'),
    's046': orig('44-registro-de-aquisicao-e-estado-de-entidade.md', '55-fabricar-e-evoluir-o-vigia-do-deposito.md')
            + sib('45-tempo-materiais-e-retomada-de-entidades.md', '43-aquisicao-e-projetos-de-entidades.md'),
    's051': [],
}
MULTI = {}

E = []
def e(caso, antes, depois, motivo=CLARO, passagem=1, tipo='clareza'):
    E.append((caso, passagem, tipo, motivo, antes, depois))

# ---------------------------------------------------------------- s043
e('s043', 'Esse resultado impede repetir o teste sobre a mesma maldição até ela falhar.',
  'Como o sucesso da maldição a exorciza, não é possível repetir o teste até ela falhar.',
  'Clareza: a frase anterior podia ser lida ao contrário; agora segue o Livro de Regras 1.0.')
e('s043', 'Corpos inativos não substituem trabalhadores treinados: falham em rolagens, não agem e não recebem tarefas.',
  'Corpos inativos não substituem trabalhadores treinados: falham nas rolagens, não agem e não recebem tarefas.')

# ---------------------------------------------------------------- s045
e('s045', 'Não exige uma descrição de cada hora ou postagem diária.', 'Não exige descrever cada hora nem cada dia de trabalho.',
  'Clareza: vale para mesa presencial e on-line, como nos lotes B4-01 e B5-01.')

# ---------------------------------------------------------------- s046
e('s046', 'Reconstruir uma Classe exige menos trabalho-base que criar outra entidade daquela Classe.',
  'Reconstruir para uma Classe exige menos trabalho-base que criar do zero outra entidade daquela Classe.')

# ---------------------------------------------------------------- s051
e('s051', 'Seu ataque desarmado normal tem **+4 para acertar e 1d4 + 3 de dano**, sem outro modificador. Ele escolhe esse ataque porque a prova exige derrotar o cão sem destruí-lo.',
  'Seu ataque desarmado normal tem **+4 para acertar e 1d4 + 3 + 1d4 de dano**: o segundo d4 é Canalizar Energia, que Kaito tem por possuir energia amaldiçoada e que acompanha todo golpe desarmado que acerta. Ele escolhe esse ataque porque a prova exige derrotar o cão sem destruí-lo. Ainda assim, o golpe chega a 11: contra um cão com 1 PV, deixaria excedente 10, acima da metade de 12, e o destruiria.',
  'Correção de regra, documentada: no Livro de Regras 1.0, quem tem energia amaldiçoada recebe Canalizar Energia gratuitamente, e Canalizar em Golpe soma 1d4 (Refino 1–2) a cada ataque desarmado que acerta. Kaito tem técnica, portanto energia. O exemplo dizia "sem outro modificador". A correção também avisa que o golpe máximo de 11 pode destruir o cão quase sem vida.',
  tipo='correcao_de_regra')
e('s051', 'O d4 mostra 3: **3 + 3 = 6 de dano**.', 'Os d4 mostram 1 e 2: **1 + 3 + 2 = 6 de dano**.',
  'Correção de regra, documentada: o mesmo total de 6, agora com o d4 de Canalizar; o resto do exemplo (6 PV, depois zero com excedente zero) não muda.',
  tipo='correcao_de_regra')
e('s051', 'Kaito pode desistir sem gastar ação enquanto estiver consciente e conseguir comunicar a decisão.',
  'Kaito pode desistir sem gastar ação, desde que esteja consciente e consiga comunicar a decisão.')
