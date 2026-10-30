"""Criar as quatro cópias do lote B2-04 a partir dos originais e registrar cada alteração.

Os originais não são alterados. Cada troca precisa ocorrer exatamente uma vez no texto
corrente; o registro em alteracoes.json reproduz as cópias a partir das fontes.
"""
from pathlib import Path
import json

A = Path(__file__).resolve().parent
R = A.parents[1]
G = R / '06 - Redacao do Guia'
C = G / 'revisao-98/casos'
CFG = json.loads((A / 'arquivos-do-lote.json').read_text())
CASOS = {f['id']: f for f in CFG['casos']}

COPIA = 'Criar cópia e apontar as remissões para as cópias revistas vizinhas.'
CLARO = 'Clareza: frase direta, termo do Livro de Regras 1.0 ou ordem de leitura.'
PENTE = 'Pente fino da segunda leitura, na prova completa.'

# Remissões da cópia: as fontes ficam na pasta do Guia; as cópias ficam em revisao-98/casos.
LINKS = {
    's072': [
        ('](71-sineiro-do-recolhimento.md)', '](<71-sineiro-do-recolhimento.md>)'),
        ('](63-carregador-consulta-e-doma.md)', '](<63-carregador-consulta-e-doma.md>)'),
        ('](<../04 - Planejamento/73-pressao-e-sobrevivencia-do-sineiro.md>)', '](<../../../04 - Planejamento/73-pressao-e-sobrevivencia-do-sineiro.md>)'),
        ('](73-ensaio-guiado-do-sineiro.md)', '](<73-ensaio-guiado-do-sineiro.md>)'),
    ],
    's073': [
        ('](71-sineiro-do-recolhimento.md)', '](<71-sineiro-do-recolhimento.md>)'),
        ('](72-sineiro-consulta-e-doma.md)', '](<72-sineiro-consulta-e-doma.md>)'),
        ('](22-quedas-e-socorro.md)', '](<22-quedas-e-socorro.md>)'),
    ],
    's075': [
        ('](74-regua-inicial-de-inimigos.md)', '](<74-regua-inicial-de-inimigos.md>)'),
        ('](76-confronto-de-ren-e-sora.md)', '](<76-confronto-de-ren-e-sora.md>)'),
    ],
    's076': [
        ('](75-ren-e-sora-atacante-e-apoio.md)', '](<75-ren-e-sora-atacante-e-apoio.md>)'),
        ('](73-ensaio-guiado-do-sineiro.md)', '](<73-ensaio-guiado-do-sineiro.md#personagens-usados>)'),
    ],
}

# (caso, passagem, tipo, motivo, antes, depois)
E = []
def e(caso, antes, depois, motivo=CLARO, passagem=1, tipo='clareza'):
    E.append((caso, passagem, tipo, motivo, antes, depois))

# ---------------------------------------------------------------- s072
e('s072', '**Conversão experimental preparada para a ficha do [Sineiro do Recolhimento](<71-sineiro-do-recolhimento.md>).** Use esta seção para conferir a aquisição e apresentar ao jogador o resultado antes da tentativa.',
  '**Conversão experimental da ficha do [Sineiro do Recolhimento](<71-sineiro-do-recolhimento.md>).** Use esta seção para conferir a aquisição e mostrar ao jogador, antes da tentativa, o que ele vai receber.')
e('s072', 'O Sineiro domado continua capaz de agarrar, transportar e preparar um impacto. A versão adquirida usa a construção e os comandos de entidade do Livro de Regras 1.0. Ter enfrentado dois ataques ou uma preparação por Bônus não concede esses recursos ao personagem.',
  'O Sineiro domado continua capaz de agarrar, transportar e preparar um impacto, mas passa a usar a construção e os comandos de entidade do Livro de Regras 1.0. Os dois ataques e a preparação por Bônus da ficha do confronto não passam para quem o doma.',
  'Clareza: a frase anterior sugeria que enfrentar a ficha concederia recursos; agora diz o que não passa para a entidade.')
e('s072', 'Essas diferenças fazem parte da oferta de aquisição. Não prometa uma cópia da ficha inimiga e só depois anuncie os limites.',
  'Mostre essas diferenças junto com a oferta de aquisição. Não prometa uma cópia da ficha inimiga para anunciar os limites só depois.')
e('s072', 'Exige candidato de **nível 6 ou maior**. A rota deste exemplo é derrotar a maldição sem destruí-la e tentar fora de combate. Este exemplo não define um ponto para tentar a Doma antes da derrota.',
  'Quem tenta a Doma precisa ter **nível 6 ou maior**. Neste exemplo, o caminho é derrotar a maldição sem destruí-la e fazer a tentativa fora de combate. O exemplo não define um momento para tentar a Doma antes da derrota; essa tentativa depende de permissão do mestre.',
  'Clareza: "rota" também nomeia a fonte da CD; o caminho da aquisição e a permissão de tentativa antecipada ficam explícitos, conforme Domar uma maldição.')
e('s072', 'Confira destruição usando os **108 PV máximos da ficha do confronto**. Uma ocorrência de dano direto de pelo menos 108, ou um excedente além de zero **maior que 54**, destrói. Excedente igual a 54 não basta. Dano em área derrota, mas não destrói por si. A partir de 5 PV, dano direto 59 produz excedente 54; 60 produz 55 e destrói.',
  'Para saber se o golpe final destrói a maldição, use os **108 PV máximos da ficha do confronto**. Destrói uma ocorrência de dano direto de pelo menos 108, ou um dano que passe de zero por **mais de 54**. Passar por exatamente 54 não basta. Dano em área derrota, mas não destrói por si. **Exemplo:** com 5 PV restantes, dano direto 59 deixa excedente 54 e a Doma continua possível; 60 deixa 55 e destrói.')
e('s072', 'A maldição faz **um TR Espírito**, normalmente +1, contra a CD da rota do candidato: **falha doma; sucesso exorciza**. Igualar a CD é sucesso. Aplique suas condições atuais, incluindo desvantagem do estágio 3 de Integridade quando presente. Não repita o teste até obter o resultado desejado.',
  'A maldição faz **um TR Espírito**, normalmente +1, contra a CD de conjuração de quem a doma, pela rota dessa pessoa (técnica, Manejo ou Kata). **Se falhar, fica domada; se passar, é exorcizada.** Igualar a CD é sucesso da maldição. Aplique as condições atuais dela, incluindo a desvantagem do estágio 3 de Integridade, quando houver. Faça um único teste; não o repita até obter o resultado desejado.',
  'Clareza: CD nomeada como no Livro de Regras 1.0 (Submissão) e resultado escrito em frases completas.')
e('s072', 'É a básica própria de entidade, não os dois ataques desarmados da ficha inimiga; Toque não passa a ganhar crítico contra Guarda Aberta só por sua aparência de soco.',
  'É a básica própria de entidade, não os dois ataques desarmados da ficha inimiga. Por ser uma básica de Forma Toque, e não um ataque desarmado, não causa crítico automático contra Guarda Aberta, mesmo parecendo um soco.')
e('s072', 'Essa atuação não deixa outra básica para Pancada ou especial no mesmo ciclo. A coletiva de Reação não cria uma segunda básica.',
  'Essa atuação gasta a básica: no mesmo ciclo, não sobra outra para Pancada ou especial. A Reação coletiva não cria uma segunda básica.',
  'Clareza: termo "Reação coletiva", como no Livro de Regras 1.0.')
e('s072', 'Soma de itens próprios, corpo transportado em kg ÷ 12 e itens dele de até **9 Volume**.',
  'A soma dos itens próprios, do corpo transportado (kg ÷ 12) e dos itens da pessoa vai até **9 Volume**.')
e('s072', 'Na saída de campo, a pessoa e seus objetos ficam no mundo, na posição e no estado alcançados. A CE1 permanece proposta de transporte limitado; não inclui a eficiência permanente do chefe.',
  'Se a entidade sair de campo, a pessoa e seus objetos ficam no mundo, na posição e no estado em que estavam. Este talento CE1 continua uma proposta de transporte limitado; não inclui o arrasto mais barato da ficha do confronto.')
e('s072', 'Comando por Padrão do invocador e uma básica disponível da entidade. Ela precisa já estar conduzindo a pessoa conforme as regras do talento. Não pode gastar a mesma básica para agarrar e executar esta especial.',
  'O invocador comanda com sua Padrão, e a entidade gasta uma básica disponível. Ela precisa já estar conduzindo a pessoa pelo talento. A mesma básica não serve para agarrar e para executar esta especial.')
e('s072', 'Conserve os 9 Volume conjuntos, tamanho Médio ou menor e espaço para ambos. Agarrado na entidade impede seu deslocamento.',
  'Valem os mesmos limites: 9 Volume conjuntos, pessoa Média ou menor e espaço para os dois corpos. Se a própria entidade estiver Agarrada, não se desloca.')
e('s072', 'Não se aplica uma nova condição nem há novo TR para uma contenção que já foi obtida.',
  'A especial não aplica nova condição nem pede novo TR para uma contenção já obtida.')
e('s072', 'Não produzem dano, cura ou distância adicional.', 'Esses pontos não viram dano, cura ou distância adicional.')
e('s072', 'O preço próprio precisa ser acordado antes do uso. A comparação é Passo, que oferece 6 m sem oportunidades pelo preço Leve: esta proposta custa Médio por conduzir também uma pessoa, inclusive uma presa sob contenção anterior, e conserva oportunidades.',
  'Combine o preço próprio antes do uso. A referência é Passo, que oferece 6 m sem oportunidades pelo preço Leve. Esta proposta custa Médio porque leva também uma pessoa, inclusive uma presa já contida, e não evita oportunidades.')
e('s072', 'Se precisou Agarrar nesse ciclo, a especial deve aguardar outra oportunidade válida.',
  'Se precisou Agarrar nesse ciclo, a especial fica para um ciclo seguinte, com outra básica.',
  'Clareza: "oportunidade" podia ser lida como ataque de oportunidade.')
e('s072', '**Primeiro turno:** Padrão normal de comando do invocador, uma básica da entidade e 6 PE iniciam **Carregar**. Mostre a área e a carga. Ela conserva seu Movimento, mas mover-se também muda a futura origem da Aura. Cada ocorrência de dano nela exige seu TR Espírito,',
  '**Primeiro turno:** o comando com a Padrão do invocador, uma básica da entidade e 6 PE iniciam **Carregar**. Mostre a área e a carga. A entidade conserva seu Movimento, mas mover-se também muda o ponto de onde a Aura sairá. Cada ocorrência de dano nela exige um TR Espírito,')
e('s072', 'O agarrão mantido termina pela condição. Não bloqueia nem recebe acertos automáticos; ataques corpo a corpo com arma ou desarmados que acertem causam crítico. A exposição dura mais que a da ficha do confronto.',
  'Se estiver agarrando alguém, o agarrão termina pela condição. A entidade não pode Bloquear; os ataques contra ela ainda precisam acertar, mas ataques corpo a corpo com arma ou desarmados que acertem causam crítico. Essa exposição dura mais que a da ficha do confronto.',
  'Clareza: "não recebe acertos automáticos" podia ser lido como proteção; agora diz que o ataque ainda precisa acertar.')
e('s072', 'Das devoluções nominais 2 + 1, aproveita somente **1**, o gasto em Melhoria.',
  'Das devoluções nominais, 2 + 1, aproveita só **1**: o ponto gasto em Melhoria.')
e('s072', 'não mantém o uso corporal gratuito da ficha inimiga.', 'não conserva a preparação corporal sem custo da ficha do confronto.')
e('s072', 'Conserve os recursos atuais, limitados aos novos máximos; **zero continua zero**.',
  'A Doma não cura: conserve os recursos atuais, limitados aos novos máximos; **zero continua zero**.')
e('s072', 'religar custa **Bônus e 2 PE**, no lugar do corpo, e devolve **19/38 PV**, sem recuperar Integridade ou criar básica. Quando houver permissão de manifestação comum, a entrada de Classe máxima 2 custa **Bônus e 2 PE**, não oferece básica naquele ciclo e exige outra Bônus para a primeira tarefa. São ações diferentes, ainda que os custos coincidam neste nível.',
  'religar custa **Bônus e 4 PE**, o dobro do PE da entrada, no lugar do corpo, e devolve **19/38 PV**, sem recuperar Integridade ou criar básica. Quando houver permissão de manifestação comum, a entrada de Classe máxima 2 custa **Bônus e 2 PE**, não oferece básica naquele ciclo e exige outra Bônus para a primeira tarefa.',
  'Correção de regra, documentada: no Livro de Regras 1.0, religar usa o retorno, que custa o dobro do PE da entrada. A entrada do Sineiro, de nível 6, custa 2 PE (maior Classe permitida, 2); portanto religar custa 4 PE, não 2. A frase que dizia que os custos coincidiam foi retirada. O Carregador, de nível 2, continua certo com 1 e 2 PE.',
  tipo='correcao_de_regra')
e('s072', 'No começo do turno dele renovam-se Movimento e básica, além da coletiva de Reação compartilhada. Não tem Bônus independente.',
  'No começo do turno dele, a entidade recupera Movimento e básica, e o conjunto recupera a Reação coletiva. Não tem Bônus própria.',
  'Clareza: ordem e termos de Invocações em campo.')
e('s072', 'Uma ordem antecipada conserva seus custos e sua primeira oportunidade válida, sem criar básica ou transporte imediato.',
  'Uma ordem dada antes conserva seus custos e só se cumpre na primeira ocasião válida; não cria básica nem transporte imediato.')
e('s072', 'O exemplo preserva esta conversão; não é teste da versão domada.',
  'O exemplo usa a ficha do confronto e não testa a versão domada.')

# ---------------------------------------------------------------- s073
e('s073', 'Leia este exemplo para acompanhar **uma missão que termina sem derrotar o chefe**. Depois, consulte o segundo exemplo para ver como uma interrupção malsucedida pode levar ao socorro. A [ficha do Sineiro](<71-sineiro-do-recolhimento.md>) traz suas capacidades; a [consulta e Doma](<72-sineiro-consulta-e-doma.md>) continua separada.',
  'Este exemplo acompanha **uma missão que termina sem derrotar o chefe**. O segundo exemplo, mais adiante, mostra como uma interrupção malsucedida pode levar ao socorro. A [ficha do Sineiro](<71-sineiro-do-recolhimento.md>) traz suas capacidades; a [ficha após a Doma](<72-sineiro-consulta-e-doma.md>) fica à parte e não é usada aqui.',
  'Clareza: instrução direta e nome atual da consulta da Doma.')
e('s073', 'Essas informações podem ser descobertas antes do confronto.', 'O grupo pode descobrir essas informações antes do confronto.')
e('s073', 'Os alvos dos impactos deste exemplo estão claramente dentro da zona. A preparação interrompida não exige resolver casos na borda.',
  'Quem é atingido neste exemplo está claramente dentro da zona, e a preparação interrompida não exige decidir casos na borda.')
e('s073', 'Estes são perfis de personagens de nível 6,', 'Os três são perfis de personagens de nível 6,')
e('s073', 'Nas duas alternativas, as escolhas de técnica e de Caminho permanecem iguais.', 'Os dois exemplos usam as mesmas escolhas de técnica e de Caminho.')
e('s073', 'Ativa Olhos Em Mim com Bônus; a área de proteção acompanha Rina por 6 m. Assumir um ataque rolado contra um aliado nessa área gasta sua Reação, antes dos dados.',
  'Ativa Olhos Em Mim com Bônus: a área de proteção tem 6 m de raio e acompanha Rina. Para assumir um ataque rolado contra um aliado nessa área, ela gasta a Reação antes dos dados.')
e('s073', 'No próprio turno do beneficiário, não exige outra ação; fora dele, exige sua Reação.',
  'No próprio turno, o beneficiário usa a abertura sem outra ação; fora dele, gasta a própria Reação.',
  'Clareza: "sua Reação" podia ser lida como a de Akira.')
e('s073', 'Cada Reação volta no começo do turno de seu dono; começar uma nova rodada, sozinho, não devolve todas ao mesmo tempo.',
  'Cada Reação volta no começo do turno de seu dono; a passagem de rodada não devolve as Reações.')
e('s073', 'Usa a interação simples gratuita do turno para pegá-la e a larga ali, sem outra ação. Isso chama a atenção do guardião; não é uma regra geral de provocação. Com a Bônus, ativa Olhos Em Mim. Sua provocação inicial dá',
  'Pega a caixa com a interação simples gratuita do turno e a solta ali mesmo, sem gastar outra ação. Isso chama a atenção do guardião; não é uma regra geral de provocação. Com a Bônus, ativa Olhos Em Mim. A provocação inicial dessa ativação dá')
e('s073', 'Até o começo do próximo turno de Rina, seus ataques têm vantagem contra ela e desvantagem contra outros alvos, conforme Provocar.',
  'Até o começo do próximo turno de Rina, os ataques do Sineiro têm vantagem contra ela e desvantagem contra outros alvos, conforme Provocar.',
  'Clareza: "seus ataques" podia ser lido como os de Rina.')
e('s073', '**O Sineiro captura e conduz.**', '**O Sineiro captura e arrasta.**', 'Clareza: mesmo nome da capacidade revista, Arrastar a presa.')
e('s073', 'conduzindo Rina de C6 a C10. O trajeto e os corpos cabem. A Bônus prepara o sino; o mestre marca a zona de 3 m de raio. O impacto poderá ocorrer na Padrão do próximo turno do Sineiro. Rina está dentro dela.',
  'arrastando Rina de C6 a C10. Os dois corpos cabem no trajeto. Com a Bônus, começa a dobrar o sino: o mestre marca a zona de 3 m de raio, com Rina dentro, e avisa que o impacto poderá vir na Padrão do próximo turno do Sineiro.',
  'Clareza: ordem do aviso e termo da ficha revista.')
e('s073', 'O deslocamento cancela a preparação.', 'Mudar de posição interrompe a preparação.', 'Clareza: mesmo critério da ficha revista.')
e('s073', 'Não conjurou nem recebeu outra Padrão por terminar o objetivo material.', 'Pegar a caixa não lhe deu outra ação.')
e('s073', 'Anda de E10:F11 até D7:E8, 4,5 m: a célula de referência passa por D9, D8 e D7.',
  'Anda de E10:F11 até D7:E8, 4,5 m: o primeiro espaço da anotação passa por D9, D8 e D7.',
  'Clareza: "célula de referência" não tinha sido definida.')
e('s073', 'Com Bônus, o Sineiro prepara outro impacto.', 'Com a Bônus, o Sineiro começa outra preparação.')
e('s073', 'O dano não cancela a preparação.', 'O dano, sozinho, não interrompe a preparação.', 'Clareza: mesmo critério da ficha revista.')
e('s073', '### Rodada 3 — encerrar a oposição', '### Rodada 3 — todos saem', 'Clareza: o Sineiro continua ativo; o título diz o que acontece.')
e('s073', 'A preparação do Sineiro ficou sem alvos; ele pode desistir. Seu comportamento não inclui perseguir além da entrada.',
  'A preparação do Sineiro ficou sem alvos, e ele pode desistir dela. Pelo comportamento declarado, não persegue além da entrada.')
e('s073', 'Encerrar a oposição não recupera PE ou vida automaticamente.', 'Sair do confronto não recupera PE ou vida automaticamente.')
e('s073', 'Este exemplo gasta menos recursos ofensivos que a sequência de seis feitiços comparada no planejamento.',
  'Este exemplo gasta menos recursos ofensivos que a sequência de seis feitiços usada na [revisão numérica do Sineiro](<../../../04 - Planejamento/73-pressao-e-sobrevivencia-do-sineiro.md>).',
  'Clareza: a referência ao planejamento ganha destino.')
e('s073', 'Não transporte os gastos ou as posições finais do primeiro exemplo para cá.', 'Não use os gastos nem as posições finais do primeiro exemplo.')
e('s073', 'sem atravessar o Sineiro ou sair de seu alcance depois de entrar nele.',
  'sem atravessar o Sineiro; depois de entrar no alcance dele, não sai mais, por isso não provoca oportunidade.')
e('s073', 'Não tem outro impacto imediato nem pode armar outro sino enquanto estiver nessa condição.',
  'Não tem outro impacto imediato nem pode começar outra preparação enquanto estiver nessa condição.')
e('s073', 'Mantenha a contagem para resolver o socorro, mesmo com a equipe fora.',
  'Continue contando a iniciativa até resolver o socorro, mesmo com a equipe fora do recinto.')
e('s073', 'Essa alternativa exige outro percurso; reduzir o tratamento não concede gratuitamente a fuga do caso acima.',
  'Essa alternativa exige outro percurso: precisar de menos tratamento não traz junto a fuga do caso acima.')
e('s073', 'Não esconda essas mudanças dentro da mesma classificação de dificuldade.',
  'Não trate o encontro modificado como se tivesse a mesma dificuldade.')

# ---------------------------------------------------------------- s075
e('s075', 'Este exemplo aplica as [referências iniciais de valores](<74-regua-inicial-de-inimigos.md>):',
  'Este exemplo aplica as referências de [escolher os números de um inimigo](<74-regua-inicial-de-inimigos.md>):',
  'Clareza: nome atual da consulta revista.')
e('s075', 'Não são maldições disponíveis para Doma.', 'Como não são maldições, não podem ser domados.')
e('s075', 'As fichas podem escolher Defesa estática ou Bloquear antes de cada ataque rolado; Bloquear não impede áreas ou TRs.',
  'Antes de cada ataque rolado contra eles, escolhem entre a Defesa e Bloquear; Bloquear não protege contra áreas ou TRs.')
e('s075', 'O limite inicial é **4**, por Refino 2;', 'O limite inicial é **4**, o dobro do Refino 2;')
e('s075', 'Leitura de Reservas, quando aplicada validamente, revela os valores efetivos de PE; registre os gastos.',
  'Se alguém usar Leitura de Reservas de forma válida, veja os PE atuais; por isso, registre os gastos.')
e('s075', 'Uma oportunidade comum usa um ataque físico, não a manobra ou o feitiço.',
  'Um ataque de oportunidade usa um golpe comum, não uma manobra nem um feitiço.')
e('s075', '**Impulso sozinho não exige base Média.** A base é paga aqui pela vida temporária.',
  '**A base Leve existe por causa da vida temporária;** Impulso, sozinho, não exigiria uma base Média.',
  'Clareza: a frase anterior invertia a ordem da explicação.')
e('s075', 'A escolha da dupla é usar Remendo em si ou no parceiro **ainda ativo, com vida positiva e até metade da máxima**. Isso é escolha de comportamento, não uma limitação nova da cura geral.',
  'Pela conduta escolhida para a dupla, Sora usa Remendo em si ou no parceiro **ainda ativo, com vida positiva e até metade da máxima**. Essa é uma escolha de comportamento, não uma limitação nova da cura geral.')
e('s075', 'Cobrir-se conserva seu custo de aptidão.', 'Cobrir-se não é feitiço e conserva seu custo.')
e('s075', 'Não há Insistir ou janela de socorro de jogador concedidos a estas fichas. Remendo não oferece permissão para reabrir a participação de quem foi Derrotado.',
  'Estas fichas não recebem Insistir nem a janela de socorro dos personagens jogadores. Remendo não traz de volta à luta quem foi Derrotado.')

# ---------------------------------------------------------------- s076
e('s076', 'Os [perfis do exemplo anterior](<73-ensaio-guiado-do-sineiro.md#personagens-usados>)',
  'Os [perfis do ensaio do Sineiro](<73-ensaio-guiado-do-sineiro.md#personagens-usados>)',
  'Clareza: remissão nomeada e com destino na seção dos perfis.')
e('s076', 'Não recebe vantagem pela provocação; a área de proteção de Rina permanece ativa.',
  'Como resistiu, Ren não recebe vantagem contra Rina nem desvantagem contra os outros; a área de proteção dela continua ativa.',
  'Clareza: efeito do TR resistido, conforme Provocar.')
e('s076', 'Rina fica com **58 PV**. Ela conserva a Reação.', 'Rina fica com **58 PV** e conserva a Reação.')
e('s076', 'Com Bônus e **1 PE**, prepara **Executar** para Mei contra Sora.',
  'Com Bônus e **1 PE**, prepara **Executar** para Mei contra Sora: ela poderá fazer o próximo ataque contra Sora com vantagem.',
  'Clareza: diz o que Executar concede antes de ser usado.')
e('s076', 'Ter saído dos 9 m antes do turno não suprimiu toda a atuação de apoio; obrigou uma escolha de posição, e ela pôde tratar a si mesma.',
  'Ser empurrada para fora dos 9 m não anulou o apoio: obrigou Sora a se reposicionar, e ela ainda pôde tratar a si mesma.')
e('s076', 'a Reação disponível não permite pagar uma redução sem energia suficiente.',
  'ela ainda tem Reação, mas não tem PE para pagar Cobrir-se.')
e('s076', 'Ele continua alcançável por alguns ataques; cruzar a porta não impede que outra escolha fosse feita.',
  'Ele ainda estaria ao alcance de alguns ataques; cruzar a porta não o protege.')
e('s076', 'Seu transporte não acontece automaticamente.', 'Levá-la exige outra solução; não acontece automaticamente.')
e('s076', 'Se o primeiro ataque já derrotar o alvo, a segunda personagem pode redirecionar sua ação; o cálculo da derrota desse alvo não exige atacá-lo depois de cair.',
  'Se o primeiro ataque já derrotar o alvo, o segundo personagem pode escolher outra ação; a chance da tabela não depende de atacar quem já caiu.')

PASS2 = json.loads((A / 'pente-fino.json').read_text()) if (A / 'pente-fino.json').exists() else []
for x in PASS2:
    E.append((x['caso'], 2, x.get('tipo', 'pente_fino'), x.get('motivo', PENTE), x['antes'], x['depois']))


def main():
    log = []
    for cid, f in CASOS.items():
        src = (R / f['fonte_original']).read_text()
        text = src
        for a, b in LINKS[cid]:
            assert text.count(a) == 1, (cid, a)
            text = text.replace(a, b)
        log.append({'fonte': f['fonte_revisada'], 'passagem': 1, 'tipo': 'copia_e_remissoes', 'motivo': COPIA, 'antes': src, 'depois': text})
        for caso, passagem, tipo, motivo, a, b in E:
            if caso != cid:
                continue
            n = text.count(a)
            assert n == 1, (cid, n, a[:90])
            text = text.replace(a, b)
            log.append({'fonte': f['fonte_revisada'], 'passagem': passagem, 'tipo': tipo, 'motivo': motivo, 'antes': a, 'depois': b})
        (R / f['fonte_revisada']).write_text(text)
    (A / 'alteracoes.json').write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n')
    from collections import Counter
    print(len(log), dict(Counter((x['passagem'], x['tipo']) for x in log)))


if __name__ == '__main__':
    main()
