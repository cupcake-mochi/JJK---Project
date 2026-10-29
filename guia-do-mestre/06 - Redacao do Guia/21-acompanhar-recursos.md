# Vida, energia e outros recursos

Antes de uma missão, confira como estão os personagens. Durante o jogo, registre custos, perdas e efeitos no momento em que ocorrem. Ao terminar a missão, confira o que cada personagem recupera pelas regras e o que ainda precisa de cuidado.

Use os campos abaixo para acompanhar o que cada personagem ainda tem. [Quedas e socorro](22-quedas-e-socorro.md) explica o que acontece ao chegar a zero de vida ou ficar Derrotado; [Retirada e recuperação](23-retirada-e-recuperacao.md) trata da saída do perigo e da retomada. O [registro de estado e socorro](24-registro-de-estado-e-socorro.md) reúne os campos de consulta.

## Máximo e valor atual

O **máximo** é o limite de uma reserva naquele momento. O **valor atual** é quanto resta dela. Vida, pontos de energia (PE) e Integridade precisam de registros separados.

**Exemplo:** uma personagem tem 23 de vida máxima e perde 5. Sua vida atual fica em **23 − 5 = 18**; o máximo continua 23. Uma regra que reduza o máximo deve ser registrada à parte, com sua duração ou condição para voltar ao normal.

| Registro | O que acompanhar |
|---|---|
| Vida | Máximo atual, saldo e vida temporária separada |
| Energia | Máximo, saldo e energia temporária separada |
| Integridade | Máximo, saldo e estágio da perda, quando aplicável |
| Condições e efeitos | Fonte, aplicação, prazo e forma de encerrar |
| Capacidades limitadas | Usos gastos e condição para recuperar |
| Equipamento | Itens, munição, consumíveis, carga e alterações relevantes |
| Sequelas, Cicatrizes e Exaustão | Quantidades e consequências conforme suas regras |

O nome de uma reserva não substitui o que a ficha permite fazer. No ramo Sem Energia de Restrição Celestial, os PE são Pontos de Esforço; gastá-los não cria energia amaldiçoada. Corpos e entidades podem ter exceções próprias. Confira a entrada correspondente antes de usar os mesmos campos para todos.

## Como descontar o dano

Confira o dano do efeito, os tipos, as defesas e as reduções permitidas. Depois aplique o resultado às reservas. Resistência, Redução de Dano e vida temporária entram em momentos diferentes da conta.

**Exemplo:** um golpe causa 21 de Fogo. Resistência reduz à metade: **21 ÷ 2 = 10,5**, arredondado para **11** de dano recebido. Uma redução aplicável retira 4: restam **7**. Com 3 de vida temporária, a personagem perde esses 3 e mais **4 de vida comum**. Se tinha 18 de vida, fica com 14.

Um dano reduzido a zero não retira vida nem cura. Um ataque que acertou continua sendo um acerto; efeitos que dependem de acertar e efeitos que dependem de causar dano precisam ser conferidos separadamente.

Dano de Alma usa sua regra própria. Cada ponto afeta vida e Integridade, a menos que uma regra diga o contrário. A metade por resistência ou TR não se aplica a esse dano; um efeito inteiramente evitado por um TR continua podendo causar zero. Vida temporária absorve a parcela que iria à vida, sem proteger a Integridade. Consulte [Dano na alma, Livro de Regras 1.0](</home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r53/LIVRO-COMPLETO.md#dano--alma>) para as reduções e demais condições.

## Vida e energia temporárias

Registre cada reserva temporária separada da comum. O teto normal é metade do máximo do recurso, arredondada para baixo, mínimo 1 quando esse máximo for positivo. Máximo zero não cria reserva temporária.

Reservas temporárias do mesmo recurso não se somam: compare o que resta com a quantidade recebida, limitada pelo teto, e conserve o maior. Elas são consumidas antes da reserva comum conforme a regra e normalmente terminam com a cena, salvo duração própria.

**Exemplo:** vida máxima 23 permite até **11 temporários**. Restam 3 e uma nova capacidade concede 9: o saldo passa a **9 temporários**, não 12. Receber vida temporária não recupera vida nem conta como tratamento para sair de Morrendo.

Se uma proteção for preparada imediatamente antes da situação em que será usada, confirme sua continuidade naquele momento, conforme o Livro de Regras 1.0. Isso pode conservar o saldo até a situação correspondente, sem repor pontos já gastos.

## Perder Integridade

**Integridade** é a reserva usada pelas regras de dano de Alma. Compare quanto foi perdido com seu máximo e aplique as penalidades de todos os estágios que a perda atingiu.

| Perda em relação ao máximo | Efeito do estágio |
|---|---|
| Menos de 1/4 | Sem penalidade de estágio |
| Pelo menos 1/4 | Desvantagem em testes de perícia |
| Pelo menos 1/2 | Deslocamento pela metade; feitiços custam +1 PE por Classe |
| Pelo menos 3/4 | Desvantagem em ataques e Testes de Resistência; Classe máxima de conjuração cai à metade, para baixo, mínimo 1 se já possuía Classe 1 |
| Toda a Integridade | Inconsciente e Derrotado |

Compare as frações exatas. Com máximo 26, perder 6 não alcança 1/4; perder 7 alcança. Recuperar Integridade pode reduzir o estágio, mas cura de vida não restaura essa reserva. Se a perda de toda a Integridade já encerrou a participação na cena, restaurá-la não reabre essa participação por si só.

Se vida e Integridade chegarem a zero na mesma ocorrência, resolva a derrota por Integridade. Insistir não permite agir com Integridade a zero. Para quem não possui essa reserva por regra própria, como um Corpo Amaldiçoado com Núcleo Dependente, use a exceção aplicável.

## Condições e durações

Registre o efeito e seu prazo ao aplicá-lo. Quando uma regra indicar uma rodada, confira de quem é o turno de referência e em que ponto termina. Condições com saídas diferentes seguem suas próprias regras.

Receber a mesma condição novamente não intensifica seus efeitos por padrão. Registre fontes e durações; a condição permanece enquanto houver uma aplicação válida. Remover uma delas pode não remover as demais.

**Exemplo:** uma personagem encerra Atordoado no fim do turno. Isso não devolve a Ação Padrão que perdeu naquele turno. Da mesma forma, sair de uma queda não devolve uma ação já gasta nem coloca o personagem automaticamente de pé.

Quando houver dúvida de duração, leia a capacidade antes de continuar uma tentativa que depende dela. Siga as orientações de dúvidas de regra em [Conduzir uma sessão](04-conduzir-uma-sessao.md) se a interpretação continuar aberta.

## Quando recuperar os usos

| Limite da capacidade | Quando recuperar o uso |
|---|---|
| Por cena | Quando aquela cena termina |
| Por descanso curto | Ao concluir o descanso curto |
| Por dia | Depois de dormir para começar um novo dia |
| Por descanso longo | Ao concluir esse descanso no fim da missão |

Uma habilidade que diga apenas “por descanso”, sem especificar qual, precisa ter essa descrição completada antes de entrar em jogo. Recuperar o uso não devolve os PE gastos na ativação anterior.

Uma cena termina quando a pressão daquele trecho acaba: inimigo vencido, grupo que escapou ou problema imediato resolvido. O mestre anuncia a mudança quando ela afetar recursos. Trocar de sala durante a mesma perseguição não cria outra cena por si só.

A sessão é o encontro real para jogar. Seu término não encerra automaticamente a missão nem todos os efeitos. Uma missão pode durar vários dias da história e várias sessões; dormir renova os usos por dia, enquanto os demais mantêm suas condições próprias.

## Registre para continuar depois

Ao encerrar ou interromper, confira alterações com os jogadores. Preserve valores atuais, máximos alterados, usos gastos, condições, equipamento, consequências e prazos em andamento. Separe o que foi observado da decisão provisória de regra adotada pela mesa.

Na guilda, use os registros compartilhados e informe os responsáveis pelas pendências. Em campanha fechada, as mesmas informações podem ficar nas notas do grupo. Anote o que será necessário para continuar, incluindo os efeitos que ainda estão ativos.

*Base: Dano e recuperação, Percepção de energia, Origens e Cena e usos de habilidades do Livro de Regras 1.0. O [registro de estado e socorro](24-registro-de-estado-e-socorro.md) organiza a consulta; os textos completos permanecem na referência de regras.*
