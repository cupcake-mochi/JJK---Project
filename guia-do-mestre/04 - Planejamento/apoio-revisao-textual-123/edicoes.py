"""Edições da primeira passagem do lote B2-05 (registro 123). Lidas por REVISAR.py."""
COPIA = 'Criar cópia e apontar as remissões para as cópias revistas vizinhas.'
CLARO = 'Clareza: frase direta, termo do Livro de Regras 1.0 ou ordem de leitura.'
PENTE = 'Pente fino da segunda leitura, na prova completa.'

LINKS = {
    's101': [
        ('](100-comparar-inimigos-em-outras-faixas.md)', '](<100-comparar-inimigos-em-outras-faixas.md>)'),
        ('](102-o-arquivo-e-as-oportunidades-de-agir.md)', '](<102-o-arquivo-e-as-oportunidades-de-agir.md>)'),
    ],
    's102': [
        ('](101-haru-vigia-e-tessa.md)', '](<101-haru-vigia-e-tessa.md>)'),
        ('[consulta de números](100-comparar-inimigos-em-outras-faixas.md)', '[consulta de números](<100-comparar-inimigos-em-outras-faixas.md>)'),
        ('[Inimigos de níveis mais altos](100-comparar-inimigos-em-outras-faixas.md)', '[Inimigos de níveis mais altos](<100-comparar-inimigos-em-outras-faixas.md>)'),
    ],
    's079': [
        ('](78-preparar-perigos-ambientais.md)', '](<78-preparar-perigos-ambientais.md>)'),
        ('](58-ficha-de-inimigo-e-encontro.md)', '](<../../58-ficha-de-inimigo-e-encontro.md>)'),
        ('](73-ensaio-guiado-do-sineiro.md)', '](<73-ensaio-guiado-do-sineiro.md#personagens-usados>)'),
    ],
}

E = []
def e(caso, antes, depois, motivo=CLARO, passagem=1, tipo='clareza'):
    E.append((caso, passagem, tipo, motivo, antes, depois))

# ---------------------------------------------------------------- s101
e('s101', 'Leia com a [comparação entre níveis](<100-comparar-inimigos-em-outras-faixas.md>)', 'Leia com [Inimigos de níveis mais altos](<100-comparar-inimigos-em-outras-faixas.md>)', 'Clareza: nome atual da consulta revista.')
e('s101', 'Não são alvos de Doma.', 'Como não são maldições, não podem ser domados.')
e('s101', 'Antes de cada ataque rolado, pode escolher Defesa estática ou Bloquear. Bloquear não gasta Reação e não substitui um TR. Na comparação numérica isolada, foi escolhida Defesa estática; a ficha de mesa conserva as duas opções.',
  'Antes de cada ataque rolado contra si, escolhe entre a Defesa e Bloquear. Bloquear não gasta Reação e não substitui um TR. A comparação numérica do confronto usou sempre a Defesa; na mesa, as duas opções continuam valendo.')
e('s101', 'o limite inicial é **8**, por Refino 4. Cada teste de Kokusen fracassado acrescenta +2 até o descanso longo.',
  'o limite inicial é **8**, o dobro do Refino 4. Cada teste de Kokusen que falhar acrescenta +2 aos seguintes, até o descanso longo.')
e('s101', 'Leitura de Reservas consulta os PE efetivos. Não transforme os resumos de usos em cargas separadas.',
  'Leitura de Reservas revela os PE atuais. As contas de usos desta ficha são exemplos de gasto da mesma reserva, não cargas separadas.')
e('s101', 'Uma oportunidade continua sendo um único ataque físico.', 'Um ataque de oportunidade continua sendo um único golpe.')
e('s101', 'Na falha, recebe todo o dano e **Prende**: não pode se deslocar voluntariamente até o fim do próximo turno do alvo. No sucesso, recebe metade do dano, para cima, sem Prende.',
  'Quem falha recebe todo o dano e **Prende**: não pode se deslocar voluntariamente até o fim do próprio turno seguinte. Quem passa recebe metade do dano, para cima, sem Prende.',
  'Clareza: sujeito explícito; "próximo turno do alvo" dito do ponto de vista de quem é preso, como em Prende.')
e('s101', 'Todos os corpos alcançados são afetados, inclusive aliados; não existe Escolher.',
  'Todos os corpos na linha são afetados, inclusive aliados de Haru; a ficha não tem Escolher.')
e('s101', 'Prende conserva ataques, conjuração e demais ações.', 'Preso, o alvo ainda pode atacar, conjurar e usar as demais ações.')
e('s101', 'O intervalo e os PE não são duas reservas: o primeiro organiza as oportunidades de resposta; os segundos pagam as conjurações e a proteção.',
  'O intervalo e os PE cumprem funções diferentes: o intervalo dá ao grupo tempo de responder; os PE pagam as conjurações e a proteção.')
e('s101', 'Haru pode anunciar uma faixa sem gastar a Padrão que usou para atacar.', 'Anunciar a faixa não gasta ação: Haru pode atacar com a espada e anunciar no mesmo turno.')
e('s101', 'Guardar os 14 PE para reduções é uma escolha direta, não uma obrigação de inventar um gasto ofensivo só para esvaziar a reserva.',
  'Ele pode guardar os 14 PE para Cobrir-se; não é preciso inventar um gasto ofensivo só para esvaziar a reserva.')
e('s101', 'Dois Cobrir-se antes do segundo Remendo já mudam a conta.', 'Gastar dois Cobrir-se antes do segundo Remendo já impede esse Remendo.')
e('s101', '**+2**, **1d4 + 2d4 de Concussão**; crítico **2d4 + 2d4**, antes de Kokusen.',
  '**+2**, **1d6 + 2d4 de Concussão**; crítico **2d6 + 2d4**, antes de Kokusen.',
  'Correção de regra, documentada: no Livro de Regras 1.0, o dado desarmado é d4 com Maestria 1 e d6 com Maestria 2. Tessa tem Maestria 2 e Força 0; o golpe passa a 1d6 + 2d4 (Canalizar do Refino 4), crítico 2d6 + 2d4. A comparação numérica do confronto não usa esse golpe.',
  tipo='correcao_de_regra')
e('s101', 'Não há reforço ou bloqueio da saída criado depois dessa vitória.', 'O mestre não cria reforço nem bloqueio da saída depois dessa vitória.')

# ---------------------------------------------------------------- s102
e('s102', 'A análise amplia a [consulta de números](<100-comparar-inimigos-em-outras-faixas.md>), mas não estabelece',
  'A análise continua [Inimigos de níveis mais altos](<100-comparar-inimigos-em-outras-faixas.md>), mas não estabelece', 'Clareza: nome atual da consulta revista.')
e('s102', '| Painel do arquivo | Fixado na parede junto de C12; acessível de B12, C12 ou D12. Não ocupa essas células. |',
  '| Painel do arquivo | Fixado num suporte junto de C12, sem bloquear a área de passagem; acessível de B12, C12 ou D12. Não ocupa essas células. |',
  'Coerência do cenário, documentada: todas as colunas passam livres para a linha 13, então não há parede junto de C12. O painel fica num suporte, sem mudar acesso, células ou regras.',
  tipo='coerencia_do_cenario')
e('s102', 'Receber dano ou Prende não interrompe sozinho o trabalho.', 'Dano e Prende, sozinhos, não interrompem o trabalho.')
e('s102', 'Esses requisitos pertencem a este equipamento, visíveis antes da escolha.', 'Esses requisitos são deste equipamento e ficam visíveis antes da escolha.')
e('s102', 'Registre previamente os ajustes de outros tipos pelo material. Não há dano misteriosamente transferido à caixa.',
  'Se outro tipo de dano tiver ajuste pelo material, registre-o antes. O dano no fecho não passa para a caixa.')
e('s102', 'Sem autorização, aceitam uma proposta que permita acompanhar a entrega: identificar quem receberá os documentos e permitir que um guarda acompanhe a entrega.',
  'Sem autorização, aceitam uma proposta que identifique quem receberá os documentos e deixe um guarda acompanhar a entrega.')
e('s102', 'Não trate a prioridade de alvo da conta abaixo como movimento gratuito por outras criaturas.',
  'A prioridade de alvo da comparação abaixo não dá movimento gratuito a ninguém.')
e('s102', 'o relógio não inventa uma derrota irreversível.', 'não há prazo escondido que transforme isso em derrota irreversível.')
e('s102', 'Os ataques escolhem Defesa estática 14, sem cobertura, Bloquear ou Cobrir-se.',
  'Os ataques miram a Defesa 14 dos guardas, sem cobertura, Bloquear ou Cobrir-se. Por isso, os resultados diferem dos da consulta de níveis mais altos, que usa outra Defesa.',
  'Clareza: explica por que as porcentagens não coincidem com as da consulta revista.')
e('s102', 'Duro de Matar não se aplica; Nem Um Arranhão', 'Duro de Matar não se aplica, porque não há Bloquear; Nem Um Arranhão')
e('s102', 'Ele mostra um momento do confronto, independente das sequências sem resposta da tabela anterior. Mei é o Emanador 15 da referência,',
  'Ele mostra um momento do confronto, independente das sequências da comparação, que não incluem respostas dos guardas. Aqui, Mei é o Emanador 15 da referência, não a personagem dos exemplos de nível mais baixo,')
e('s102', 'Sua escolha de Defesa estática não entra num TR.', 'Contra um TR, a Defesa não conta.')
e('s102', 'Recebe quatro ataques legais de +6,', 'Recebe quatro ataques válidos de +6,')

# ---------------------------------------------------------------- s079
e('s079', 'Use com [Preparar perigos ambientais](<78-preparar-perigos-ambientais.md>)', 'Use com [Perigos do ambiente](<78-preparar-perigos-ambientais.md>)', 'Clareza: nome atual da consulta revista.')
e('s079', '**Origem das regras:**', '**De onde vêm as regras:**')
e('s079', 'Turnos adicionais e entidades não repetem a fase ambiental.', 'Turnos adicionais e entidades não fazem a fase ambiental acontecer de novo.')
e('s079', 'A condição não exige que o dano tenha ultrapassado as proteções.', 'A condição vem mesmo que as proteções zerem o dano.')
e('s079', 'Use os [perfis de Mei e Akira](<73-ensaio-guiado-do-sineiro.md#personagens-usados>).', 'Use os [perfis de Mei e Akira do ensaio do Sineiro](<73-ensaio-guiado-do-sineiro.md#personagens-usados>).')
e('s079', 'Se tivesse escolhido Aguentar, estaria Inconsciente: não receberia o mesmo trajeto gratuito; seria necessário preparar transporte ou atendimento no lugar.',
  'Se tivesse escolhido Aguentar, estaria Inconsciente: não poderia fazer o mesmo trajeto por conta própria, e seria necessário transportá-la ou atendê-la no lugar.')
