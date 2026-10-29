# O Carregador e a saída que fecha

**Variante experimental para comparação.** Use a [ficha do Carregador e sua Doma](63-carregador-consulta-e-doma.md), sem alterar números, e as orientações para [combinar inimigos e perigos](65-comparar-confronto-e-pressao-ambiental.md). O objetivo continua sendo recuperar a caixa e sair com todos. A alteração é um portão automático na saída curta e um corredor de serviço permanentemente acessível.

O prazo, o mecanismo e o corredor são escolhas deste cenário. Este caso não combina o dano de queda da passarela com o Carregador. Não concede poder de chefe, PE ou ataque adicional à criatura.

## Prepare a versão que será usada

Para comparar, use primeiro este mapa com o motor desligado; depois examine o mesmo mapa com o fechamento ativo. A versão original da consulta [O Carregador e o corredor de entulho](62-o-carregador-e-o-corredor-de-entulho.md) continua disponível, com seu próprio espaço.

O grupo começa no pátio **A**, logo fora do limite da entrada. O Carregador está no ponto de trabalho **C**, junto da caixa. As rotas entre C e o recuo continuam exatamente como antes: direta de 18 m com 6 m difíceis, lateral de 24 m regulares. Nenhum dos trechos novos tem entulho, queda ou dano ambiental.

### Mapa da saída

O caminho curto de C até o pátio tem 6 m. O portão fica no meio, no ponto **G**, a 3 m de cada extremidade. O corredor de serviço contorna uma parede e liga os mesmos pontos por três trechos regulares de 6 m. A parada está em **P**, no primeiro canto a partir de C; **Q** é o outro canto.

```text
A: PÁTIO — 3 m — G: PORTÃO — 3 m — C: TRABALHO / CAIXA → rotas antigas → RECUO
   |                                  |
   6 m                                6 m
   |                                  |
   Q ———————— 6 m ———————— P: PARADA
```

Este é um esquema de percursos, não uma planta em escala. Paredes sólidas separam o atalho do corredor de serviço: não existe diagonal atravessando a parede. Todos os corredores novos têm **3 m de largura livre**, teto, piso firme e iluminação. Marque a faixa de segurança do portão, com 1,5 m de comprimento ao longo do caminho e os 3 m de largura do vão. Os 6 m do atalho já incluem essa faixa; não acrescente outro trecho à distância.

| Percurso | Andar | Arrastar pelo piso |
|---|---:|---:|
| C → A pelo portão aberto | 6 m | 12 m |
| C → P → Q → A pelo serviço | 18 m | 36 m |
| A → Q → P, para operar a parada | 12 m | Não é um percurso de resgate obrigatório. |
| C → P, para operar a parada | 6 m | 12 m, se houver transporte permitido. |

As paredes limitam visão e acesso. De C é possível ver P pelo trecho reto de 6 m; do pátio, a parede impede enxergar P através do interior. Quem está em A vê a placa com o percurso e pode seguir pelo serviço. A ficha do alvo e a Forma de um feitiço continuam determinando se uma aplicação pode alcançá-lo; distância de caminhada não é automaticamente alcance de uma conjuração através de parede.

O pátio A é a saída para os dois percursos. A preferência do Carregador por não perseguir além da entrada passa a usar esse mesmo limite nas duas rotas. Ele pode circular pelo serviço enquanto estiver dentro, com seu movimento normal. Não atravessa uma porta fechada, não conhece posições ocultas nem aciona o mecanismo com uma ação gratuita.

## Apresente a situação

Na versão ativa, **o temporizador defeituoso acaba de iniciar um ciclo de fechamento quando o grupo chega a A**. Apresente isso antes de qualquer avanço: o aviso sonoro, a contagem visível, o desenho do serviço e a parada identificada. O Carregador aponta para o pátio e para a caixa, como no encontro original.

Explique: “O portão pode fechar depois de três rodadas completas. A passagem de serviço continua aberta. O comando em P interrompe o motor. O sensor mantém o vão aberto enquanto sua faixa está ocupada.” Role iniciativa; todos começam nas posições indicadas e recebem seus turnos antes do primeiro avanço ambiental. Esta abertura é uma convenção do exemplo, não regra para ligar máquinas durante um combate já iniciado.

Não há agressão automática pelo relógio. O Carregador conserva seus gatilhos de oposição da consulta [O Carregador e o corredor de entulho](62-o-carregador-e-o-corredor-de-entulho.md). A equipe pode parar o motor antes de mexer na caixa, conversar ou retirar-se. Na versão com motor desligado, não inicie a contagem quando alguém conseguir uma solução rápida.

## Ficha do fechamento

Use um marcador de **0 a 3**. Com motor funcionando, aumente-o uma vez, até o máximo de 3, ao fim de cada rodada completa, depois dos turnos e efeitos de fim de turno. Não avance por participante, entidade ou Reação. Até o estado 2, todo o vão permanece transitável pelo custo normal.

| Estado | Sinal e resolução |
|---|---|
| 0, abertura | Aviso sonoro e três rodadas anunciadas. Portão aberto. |
| 1, fim da primeira rodada | Primeiro sinal luminoso; faltam dois avanços. |
| 2, fim da segunda rodada | Segundo sinal; avise que o próximo avanço tentará fechar o vão. |
| 3, a partir do fim da terceira | Se a faixa estiver livre, fecha. Se estiver ocupada, aguarda aberto no estado 3. |
| Motor parado antes de fechar | Mantém-se aberto no estado alcançado; a contagem não recomeça sozinha. |
| Motor parado depois de fechar | Permanece fechado. A passagem de serviço continua disponível. |

**Faixa ocupada:** qualquer criatura de corpo sólido ou um objeto de pelo menos **1 Volume**, colocado na faixa, impede o fechamento. Esse alcance do sensor é um fato deste dispositivo. Uma projeção sem corpo não ocupa a faixa; uma entidade de corpo sólido pode ocupá-la, cumprindo suas regras de presença e atuação. O aparelho não exige que o ocupante gaste uma ação por rodada apenas para permanecer ali.

No estado 3, faça outra verificação somente ao fim da rodada seguinte se o motor continuar funcionando. Quando a faixa estiver livre, fecha nessa fase. Não fecha no instante em que alguém sai. O sensor não empurra, esmaga, agarra, causa dano ou separa corpos contidos. Um agarrão que atravesse a faixa a mantém ocupada. Se o grupo deixar a caixa ali, seu 1 Volume também serve; ainda será preciso retirá-la para cumprir o objetivo.

Fechado, o portão bloqueia passagem e visão comum pelo vão nos dois sentidos. Não cria silêncio, apagamento de energia ou impedimento de toda capacidade sobrenatural. Consulte a regra usada para perceber, alcançar ou atravessar o obstáculo. O Carregador pode ser obrigado a usar o serviço tanto quanto os personagens.

A derrota da criatura não para a contagem. Parar o motor não remove a criatura. Se a iniciativa terminar com motor ativo, resolva o tempo ficcional restante e a ocupação da faixa; não congele o mundo pela mudança de descrição. O marcador não mede tempo de fala dos jogadores.

## Como agir sobre o portão

**Operar a parada em P:** ao alcance de 1,5 m, com uma mão disponível, use **Usar objeto, Ação Padrão**, sem teste. O comando exige puxar até travar, conforme a construção deste cenário. A posição P já oferece esse acesso. O motor para; não é necessário sustentar o comando nem pagar outro recurso. Uma capacidade que permita a manipulação remota conserva seus requisitos.

**Ocupar a faixa:** alcançar G e permanecer pode preservar a saída curta. A pessoa ainda pode agir, mas precisa considerar o alcance do Carregador, suas mãos e a posição da caixa. Um efeito que a remova só permite o fechamento na fase definida, depois de conferir todos os ocupantes. Não aplique dano ou uma cobrança de Força adicional para recuperar a pressão perdida.

**Romper o acionamento:** a pequena caixa de comando em P é um objeto de mão resistente, de madeira: **Defesa 14, 10 PV**, sem RD adicional. Um ataque capaz de danificá-la usa ações, alvo, visão, alcance e dano normais. A zero PV, o motor perde alimentação e para na posição atual. Destruir o comando depois de o portão fechar não o reabre. O comando não Bloqueia; efeitos destinados apenas a criaturas não o atingem.

**Abrir passagem pela destruição:** a folha metálica do portão é um objeto maior resistente: **Defesa 18, 40 PV**, sem RD adicional. Defina a folha como a parte atacada. A zero, perde sua função de bloqueio e libera o vão de 3 m; os restos permanecem presos lateralmente, sem dano adicional ou terreno difícil neste caso. O mecanismo deixa de conseguir fechá-lo. Esses resultados pertencem à construção declarada do cenário, não a todo portão do sistema.

Ataques contra esses objetos seguem o Livro de Regras 1.0, inclusive crítico, dano acumulado e adequação ao material. Os valores vêm das tabelas de objetos, com porte e material escolhidos para o exemplo. Não dão ao Carregador um novo ataque capaz de destruir tudo por descrição. Se alguém atingir outra parte da construção, informe alvo, consequência e regra antes do gasto; não atribua automaticamente o resultado de um dos dois alvos preparados.

Para a retirada imediata, basta usar o serviço ou uma passagem já liberada. Reabrir o portão intacto e reparar o conjunto depois da ocorrência exige preparar a tarefa pertinente; não é um teste obrigatório para conseguir sair deste encontro.

## Exemplos de escolhas

Os exemplos abaixo não são uma simulação completa. Começam nas posições e estados declarados, sem outra interferência, para expor custos.

**Parar antes de enfrentar.** Mei, com deslocamento de 9 m e mão livre, começa em A. Usa Movimento e Bônus convertida: 18 m. Percorre A → Q → P por 12 m e usa a Padrão na parada. Sobram 6 m; pode chegar a C se o trajeto continuar válido. Não conserva a Padrão para atacar ao chegar. Conforme a iniciativa, o Carregador pode agir antes ou depois dessa intervenção; parar o motor não lhe retira o turno.

**Escolher entre correr e sair protegida.** Uma personagem livre em C, sem excesso de carga, leva a caixa e pretende chegar a A. Com o portão aberto, um Movimento de 9 m paga os 6 m, preservando Bônus. Fechado, Movimento e Bônus convertida pagam os 18 m do serviço. Nos dois casos, a Padrão pode ser Desengajar se ainda estiver disponível. Se gastar essa mesma Padrão para atacar ou escapar de uma contenção, não ganha Desengajar junto.

**Retirar um aliado.** Mei tem Força 2, leva 1 Volume próprio e arrasta um aliado de 72 kg com 2 Volume de itens: carga conjunta **1 + 72 ÷ 12 + 2 = 9**, dentro do teto de arrasto 14. O aliado está disposto ou inconsciente, ao alcance em C; há mãos, apoio e passagem. Com duas ações de Movimento de 9 m e a Padrão reservada, percorre os 6 m do atalho por custo 12 num turno. Pelo serviço, são 36 m de movimento: dois turnos de 18. A Padrão pode proteger o próprio movimento por Desengajar em cada turno; a pessoa arrastada não provoca oportunidade por esse transporte. Se o aliado estiver agarrado pelo inimigo, essa conta não dispensa encerrar a contenção.

**Preparar antes do fechamento.** Uma pessoa em C pode gastar Padrão para preparar deslocamento ao ver o segundo sinal luminoso e ouvir o aviso sonoro, no fim da rodada 2. Se a preparação ainda estiver válida e a Reação disponível, move até seu deslocamento depois do sinal. Com 9 m, paga os 6 m até A pelo portão ainda aberto. O movimento continua podendo provocar oportunidade. Preparar “quando o portão já fechar” não faz a resposta acontecer antes do fechamento nem concede atravessar o metal.

**Ocupação que muda o resultado.** No terceiro avanço, Kaito permanece na faixa G: o portão aguarda aberto. Se o Carregador o agarrar e arrastar para fora na rodada seguinte, confira a carga e todo o trajeto. Outros ocupantes ainda podem impedir a passagem ao estado fechado. Se ao fim dessa rodada a faixa estiver livre e o motor ligado, o portão fecha. O Carregador não ganhou uma ação ambiental; foi sua ação comum que mudou uma condição do cenário.

A iniciativa altera a ordem das oportunidades. Não escreva uma sequência de resgate como se todos pudessem agir entre Agarrar e o arrasto do mesmo turno. Reações preparadas e permissões específicas seguem seus gatilhos; ações comuns esperam seu turno.

## Encerrar a missão

O portão fechado muda o caminho, sem encerrar a missão por decreto. Quem está dentro ainda tem serviço, parada, contenção e capacidades próprias para considerar. Quem está fora pode voltar pelo serviço. Alcance e visão entre as pessoas mudam com as paredes: não permita Socorro ou alvo de poder apenas porque a distância em linha reta parece pequena.

Siga as regras de queda a zero, atendimento e retirada da consulta [O Carregador e o corredor de entulho](62-o-carregador-e-o-corredor-de-entulho.md). Um ferido no recuo não aparece em C para usar o exemplo de transporte acima. Meça o trajeto real, pague o entulho e registre a janela de Socorro. O motor não causa dano recorrente; o risco adicional vem das decisões e do tempo de acesso.

A Doma conserva a ficha experimental da consulta [Carregador de sinos: ficha e Doma](63-carregador-consulta-e-doma.md), incluindo seu limite próprio de transporte. O portão é parte do cenário, não capacidade que a entidade passa a possuir. Uma domada não recebe a Bônus independente do inimigo para reproduzir o movimento que ele conseguia somar no turno.

| O que terminou | O que ainda pode faltar |
|---|---|
| Motor interrompido | Caixa, oposição, feridos e retirada. |
| Carregador derrotado ou acordo obtido | Fechamento, socorro e transporte da caixa. |
| Caixa no pátio | Companheiros no recuo ou no serviço. |
| Todos no pátio | Informar o estado da criatura, do motor e dos acessos antes de liberar trabalhadores. |

Registre portão aberto ou fechado, marcador, motor, PV dos objetos, ocupantes, caixa e portador, criatura, feridos e rotas ainda válidas. O encerramento não repara objetos, cura corpos ou renova recursos. A comparação com a versão sem contagem deve registrar o que mudou nas escolhas, e não apenas quem venceu.
