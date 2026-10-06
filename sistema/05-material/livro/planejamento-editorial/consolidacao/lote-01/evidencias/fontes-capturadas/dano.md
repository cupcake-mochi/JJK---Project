<!-- page:dano|Dano -->
# Dano

Quando um ataque ou efeito causa dano, calcule quanto chega ao alvo e desconte esse valor dos pontos de vida dele. **Dano reduzido a zero não tira vida nem se transforma em cura.** A perda de vida não diminui seus bônus por si só. Condições e outros efeitos podem impor penalidades.

## Resolução

1. **Determine o dano do efeito.** Role os dados e some os modificadores aplicáveis, incluindo o crítico quando houver. Se um TR mudar o dano, siga o texto do efeito: metade dos dados e metade do resultado são procedimentos diferentes.
2. **Aplique as defesas contra o tipo.** Confira imunidade, resistência e vulnerabilidade. Num golpe com mais de um tipo, mantenha as parcelas separadas nesta etapa.
3. **Aplique as reduções permitidas.** Desconte a Redução de Dano aplicável, sem deixar o resultado abaixo de zero. Uma redução contra o golpe inteiro é usada uma vez, não uma vez por tipo de dano.
4. **Desconte das reservas.** Gaste primeiro a vida temporária, se houver; o restante sai da vida. Um efeito que ignore vida temporária segue sua própria regra. [Dano na alma](#alma) também afeta Integridade.

Um TR bem-sucedido só reduz ou anula o que a regra disser. Nas Formas de área do Fundamento que mandam receber metade dos dados, reduza a quantidade de dados antes de rolar. O dano de Alma tem uma regra própria.

## Resistência, vulnerabilidade e imunidade

| Defesa ou fraqueza | Efeito sobre o dano do tipo indicado |
|---|---|
| Resistência | Recebe metade. Duas fontes da mesma resistência continuam reduzindo apenas à metade. |
| Vulnerabilidade | Recebe o dobro. Duas fontes da mesma vulnerabilidade não dobram novamente. |
| Imunidade | Não recebe dano desse tipo. |

Com resistência e vulnerabilidade ao mesmo tipo, os multiplicadores se anulam antes do arredondamento. Imunidade prevalece. Uma regra que ignore resistência não ignora imunidade por esse motivo.

**Arredonde o dano fracionário recebido para cima**, depois dos multiplicadores aplicáveis à parcela. A Redução de Dano pode zerar o que sobrar. Este arredondamento não cria dano onde um efeito já determinou zero.

> **Exemplo:** Rina receberia 21 de Fogo e tem resistência a esse tipo. Metade é 10,5, arredondada para **11**. Uma habilidade permite reduzir 4 desse golpe: restam **7**. Ela tem 3 de vida temporária, que se esgotam, e perde **4 de vida**.

## Acerto e dano

Reduzir o dano a zero mantém o resultado do ataque. Uma condição aplicada **ao acertar** ainda pode entrar; um efeito que exija **causar dano** precisa de dano maior que zero. Resolva cada ataque separadamente. Ao chegar a zero de vida, siga **Vida a zero**.

<!-- page:tipos|Tipos de dano -->
# Tipos de dano

Cada fonte informa o tipo do dano que causa. Esse nome determina quais resistências, imunidades, vulnerabilidades e habilidades se aplicam. O sistema usa **quinze tipos**, reunidos em três grupos.

| Grupo | Tipos |
|---|---|
| Físicos | Cortante, Perfurante e Concussão. |
| Elementais | Fogo, Frio, Elétrico, Ácido, Trovejante e Veneno. |
| Especiais | Radiante, Necrótico, Psíquico, Energia Reversa, Força e Alma. |

Resistência a **Fogo** protege apenas desse tipo. Resistência a **Elementais** alcança todos os seis tipos do grupo. Use exatamente o que a habilidade concedeu; pertencer ao mesmo grupo não torna dois tipos iguais.

## Força

**Força** é o tipo usado para **energia amaldiçoada pura**, projetada como um impacto ou disparo, sem outro tipo indicado pelo efeito. Ele pertence ao grupo **Especiais**.

Soco, queda e impacto de objeto usam Concussão conforme sua regra. Revestir uma arma com energia não muda sozinho o tipo de seu dano. Uma técnica que cause Fogo continua usando Fogo, mesmo alimentada por energia amaldiçoada.

O tipo Força não exige o atributo Força, não empurra o alvo e não ignora redução ou resistência. “Energético” pode descrever a aparência do efeito; não é um segundo tipo de dano.

## Efeitos adicionais

O tipo de dano não aplica uma condição nem outro efeito por conta própria. **Veneno** é um tipo de dano; **Envenenado** é uma condição. Uma fonte pode causar um deles ou os dois, conforme sua descrição.

Da mesma forma, dano de Fogo não continua queimando nos turnos seguintes sem uma regra que diga isso. Frio não aplica Lento automaticamente, Concussão não empurra por si e Necrótico não impede cura por seu nome. Danificar equipamento, incendiar objetos e aplicar condições exigem os procedimentos ou efeitos correspondentes.

> **Exemplo:** um feitiço causa 8 de Veneno e aplica Envenenado ao acertar. Imunidade ao dano de Veneno zera os 8, mas não concede imunidade à condição. Se o efeito exigisse causar dano para envenenar, o dano zerado impediria esse gatilho.

## Tema e nome do feitiço

O Tema descreve a técnica; o tipo de dano é uma informação da regra. Uma técnica de Tema Fogo só causa Fogo quando o efeito indicar esse tipo. O nome de um feitiço também não substitui sua descrição.

**Alma** afeta uma reserva adicional, a Integridade, conforme a [regra de dano na alma](#alma). **Energia Reversa** permanece um tipo de dano distinto de Alma e de Radiante; a aptidão ou o feitiço que o usar informa seus alvos e efeitos. Esses nomes não concedem novas permissões de conjuração.

## Golpes com vários tipos

Se um golpe causar 10 de Cortante e 8 de Fogo, resistência a Fogo reduz apenas os 8. O dano passa a ser 10 + 4 = **14**, antes de uma redução aplicável ao golpe inteiro. Resistência a Cortante e a Físicos não divide os mesmos 10 duas vezes.

<!-- page:reducao|Redução de Dano -->
# Redução de Dano

**Redução de Dano** desconta uma quantidade do dano recebido. Seu texto informa a quais golpes se aplica, seu custo e seu momento de uso. Resolva o acerto ou o TR antes de aplicar uma redução que atue sobre o dano; ela não refaz a Defesa nem desfaz a rolagem já concluída.

Resistência é aplicada antes da redução. Se houver parcelas de tipos diferentes, resolva suas resistências e vulnerabilidades primeiro. Desconte uma redução limitada a um tipo apenas dessa parcela; depois some o restante e aplique a redução que proteja do golpe inteiro. Não use o mesmo benefício nas duas etapas.

A habilidade que concede uma redução informa sua ação, seu custo e suas restrições. Confira essa descrição antes de descontar o valor. Se a ativação mudar sua Defesa, a mudança vale para os ataques seguintes e não refaz um acerto já resolvido.

> **Exemplo:** um golpe causa 30 de Fogo. A vítima tem resistência a Fogo e uma redução de 6 aplicável àquele golpe. Recebe metade de 30, que é 15, e depois desconta 6. Perde 9 de vida, ou gasta primeiro sua vida temporária.

## Limites do efeito

Uma redução restrita a ataques não protege de uma queda por esse motivo. Uma regra que ignore parte da Redução de Dano não ignora também resistência ou vida temporária. Custos são pagos mesmo quando outras proteções acabam zerando o dano.

<!-- page:alma|Dano na alma -->
# Dano na alma

**Integridade** acompanha o dano de Alma. Anote seu máximo e valor atual separadamente da vida.

> **Integridade máxima do personagem = 20 + (Essência + 5) × (nível − 1).**

Criaturas que não sejam personagens jogadores usam metade da vida máxima, arredondada para baixo, com mínimo 1 quando a vida máxima for positiva, salvo uma regra própria de sua ficha. Uma criatura sem alma só recebe dano de Alma se alguma regra permitir.

## Receber dano de Alma

Cada ponto desconta **1 de vida e 1 de Integridade**. Um efeito que diga atingir somente Integridade conserva essa exceção. Vida temporária absorve a parte que iria à vida, mas não protege Integridade.

Dano de Alma não recebe a redução pela metade própria do TR ou de resistência. Reduções numéricas aplicáveis ao golpe entram antes de descontar as reservas. Imunidade expressa a Alma continua impedindo esse dano. Um efeito que seja inteiramente evitado por um TR bem-sucedido não causa dano por essa regra.

Anote as perdas e compare a Integridade atual com os limites de **Estágios de Integridade**. Não há um teste adicional para avançar estágio além dessa perda.

> **Exemplo:** um golpe de 8 de Alma atinge Rina. Uma redução aplicável diminui o golpe para 5. Ela possui 3 de vida temporária. Perde esses 3, mais 2 de vida e 5 de Integridade.

<!-- page:integridade|Estágios de Integridade -->
# Estágios de Integridade

O estágio depende de quanto falta para sua Integridade máxima. Use o estágio mais alto cujo limite tenha sido atingido. Os efeitos dos anteriores continuam valendo.

| Integridade perdida | Estágio | Efeito |
|---|---|---|
| Menos de 1/4 | 0 | Nenhuma penalidade. |
| Pelo menos 1/4 | 1 | Desvantagem em testes de perícia. |
| Pelo menos 1/2 | 2 | Deslocamento pela metade. Cada feitiço custa +1 PE por Classe. |
| Pelo menos 3/4 | 3 | Desvantagem em ataques e TRs. Classe máxima de conjuração cai à metade, para baixo, com mínimo 1 se já possuir Classe 1. |
| Toda | 4 | Você fica Inconsciente e Derrotado, conforme **Derrota e morte**. |

Compare frações exatas. Com Integridade máxima 26, perder 6 ainda não chega a 1/4. Perder 7 alcança estágio 1. Corrija as distâncias reduzidas para a escala de 1,5 m pelas regras de Movimento.

## Recuperar Integridade

Cura de vida não recupera Integridade. Uma capacidade que restaure essa reserva e o descanso longo seguem seus próprios valores. **Ao recuperar Integridade, recalcule o estágio.** A recuperação pode retirar penalidades dos estágios que você deixou.

Chegar ao estágio 4 encerra sua participação naquela cena, mesmo que alguém restaure pontos logo depois. A recuperação permite o socorro e a recuperação posterior, conforme Derrota e morte. Ela não restaura um personagem morto nem desfaz uma consequência permanente.

> **Exemplo:** Kaori tem máximo 26. Está com 12 de Integridade e perdeu 14, por isso está no estágio 2. Recuperar 5 a deixa com 17. Faltam 9 para o máximo, menos da metade, e seu estágio cai para 1. Recuperar mais 3 a deixaria com 20, no estágio 0.

Vida e Integridade são acompanhadas separadamente. Se a mesma ocorrência zerar as duas, resolva a derrota por Integridade. Escolher Insistir não permite agir com Integridade a zero.

<!-- page:condicoes|Condições -->
# Condições

Uma **condição** altera o que você consegue fazer enquanto durar. Registre seu nome, a fonte, o momento em que termina e os testes ou ações que permitem encerrá-la. As treze condições classificadas como Leves, Médias ou Pesadas têm efeitos próprios; uma condição não inclui outra só porque seus nomes parecem relacionados.

## Aplicação e duração

A habilidade informa como aplica a condição: por acerto, falha em TR ou outro gatilho. A Melhoria Condição sempre pede TR: num feitiço de ataque, o alvo acertado ainda faz o TR registrado e só recebe a condição se falhar. **Use a duração escrita no efeito.** Uma condição criada pela Melhoria Condição dura uma rodada, salvo Concentrada, Duradoura ou outra regra específica. Quando o efeito disser apenas uma rodada, ele termina no começo do próximo turno de quem o aplicou.

Uma manobra pode ter outra forma de término. O agarrão comum dura enquanto a contenção for mantida; ser derrubado não faz você se levantar sozinho quando a rodada muda.

## Mais de uma condição

Condições diferentes podem coexistir: aplique os efeitos de cada uma. Vantagens e desvantagens continuam seguindo a regra de cancelamento, sem rolar dados extras por cada fonte.

Receber **a mesma condição** novamente não intensifica seus efeitos. Registre as fontes e durações separadamente; ela permanece enquanto pelo menos uma aplicação estiver ativa. Escapar de um agarrão não remove outro. Uma habilidade que remova a condição por inteiro segue sua própria permissão.

## Encerrar uma condição

Uma condição termina pela duração, por uma forma de saída da própria regra ou por uma habilidade que a remova. **As condições Pesadas permitem TR no fim de cada turno do alvo**, sem gastar ação; no sucesso, encerre aquela aplicação. Use o TR e a CD indicados pelo efeito. Se ele ainda não os definir, esses campos precisam ser preenchidos antes de entrar em jogo, inclusive em efeitos aplicados por acerto.

Condições Leves e Médias não concedem esse teste repetido por padrão. Uma habilidade pode conceder outra tentativa, com seu próprio custo.

| Nível | PE para remover, quando uma habilidade permitir |
|---|---|
| Leve | 1 PE. |
| Média | 2 PE. |
| Pesada | 3 PE. |

Ter os PE não basta: você precisa de uma habilidade que remova condições e respeitar o teto e a quantidade permitidos por ela. Esse custo em PE é diferente dos pontos usados para comprar a Melhoria Condição na montagem de um feitiço.

> **Exemplo:** Mei pode remover uma condição com teto de 2 PE por uso. Pode gastar 2 PE para tirar Calado, mas não pode tirar Cego, que exige 3. Pagar três usos separados de 1 PE não transforma essa habilidade em uma remoção de condição Pesada.

**Inconsciente, Morrendo, Derrotado, Exaustão e Invisível** têm regras próprias. Invisível é tratado em Visão e percepção. Os demais são descritos neste capítulo. Nenhum deles pode ser comprado como uma das treze condições desta lista.

<!-- page:leves|Condições leves -->
# Condições leves

## Lento

Seu deslocamento cai pela metade e você não pode usar Ação Bônus. Distâncias concedidas por capacidades, como a de Passo, também caem pela metade. Converter outra ação em Bônus não permite usá-la enquanto essa proibição durar.

## Guarda Aberta

Você **não pode Bloquear**. Ataques corpo a corpo com arma ou desarmados **que acertarem você** são críticos. Ataques à distância e de conjuração não ganham crítico por essa condição; um feitiço de Toque continua sendo conjuração.

Você conserva suas ações e sua Defesa estática. O crítico segue a regra de dados dobrados e as exceções expressas da fonte de dano. A condição não faz o ataque acertar automaticamente.

## Derrubado

Você está no chão. Só pode se deslocar rastejando. Cada trecho de 1,5 m custa 1,5 m adicional, conforme Movimento. Não reduza também sua reserva de deslocamento por essa condição. Seus ataques têm desvantagem. Ataques contra você têm **vantagem a até 1,5 m** e **desvantagem de mais longe**.

Levantar de um Derrubado comum custa sua **Ação de Movimento inteira**. Uma habilidade pode permitir outro custo. Se um efeito mantiver você Derrubado por uma duração, precisa encerrar essa manutenção antes de levantar. Estar Agarrado não impede gastar a ação para levantar; você continua no mesmo espaço e agarrado.

## Agarrado

Seu deslocamento é **zero**. Você ainda pode atacar, conjurar e Bloquear, cumprindo os requisitos dessas ações. A contenção termina se quem o segura ficar com a Guarda Aberta ou Inconsciente, soltar você ou deixar de mantê-lo ao alcance.

Para encerrar um agarrão comum, consulte **Escapar de uma contenção**, nas regras de combate. O procedimento também explica múltiplas contenções. O movimento de quem segura outra criatura é tratado em **Arrastar e transportar**. Feitiços e habilidades seguem suas saídas próprias.

Ataques à distância contra alguém envolvido no agarrão usam a Defesa do alvo escolhido e a cobertura que a posição oferecer. O agarrão não troca o alvo aleatoriamente.

## Desarmado

A arma que você perdeu está no chão ou com outra criatura. Você pode recuperá-la, sacar uma reserva ou atacar desarmado, pagando os custos normais de cada opção. A condição não impede usar outra arma disponível.

## Surdo

Você não ouve e falha automaticamente em testes que precisem de audição. Recebe **-2 na iniciativa**. A penalidade entra quando rolar iniciativa; receber Surdo no meio do combate não muda retroativamente a ordem já registrada.

> **Exemplo:** um inimigo com a Guarda Aberta ainda pode atacar Rina. Se também ficar Atordoado, perde uma Ação Padrão e não usa Reações por causa de Atordoado; sua Defesa estática permanece, e Guarda Aberta continua impedindo Bloquear.

<!-- page:medias|Condições médias -->
# Condições médias

## Calado

Você não consegue usar uma conjuração ou habilidade que **exija voz**. Isso inclui falar como parte do Selo, uma Restrição que exija fala ou outro requisito sonoro que dependa da sua voz.

Um gesto silencioso ou um Selo de condição continua possível se não depender de fala. A Kata segue a mesma exigência: uma execução que dependa de voz ou do uso sonoro impedido pela condição não pode sair. Confira o requisito escrito na técnica, na Kata ou na ferramenta; o nome da condição não dispensa essa leitura.

> **Exemplo:** Kaori precisa dizer o nome do feitiço como Selo e está Calada. Não consegue conjurá-lo. Mei tem um Selo que exige tocar a própria pulseira e nenhum requisito de voz: Calado não impede essa conjuração.

Calado não faz você perder a Ação Padrão, o movimento ou a Reação. Uma habilidade que não dependa da execução impedida continua disponível. Um inimigo sem habilidades que usem voz pode sofrer a condição sem perder seus ataques por causa dela.

## Enfeitiçado

Você **não pode atacar quem o enfeitiçou nem escolher essa criatura como alvo de um efeito nocivo**. Ela tem vantagem em testes sociais contra você.

A condição termina quando você recebe um ataque ou efeito ofensivo. Um ataque contra você encerra a condição mesmo se errar; o gatilho não exige que você sofra dano.

Estar Enfeitiçado não transfere o controle do personagem para outra pessoa. Você conserva suas decisões e ações dentro dessas restrições. A vantagem social também não transforma toda ordem em uma obrigação.

> **Exemplo:** Rina está Enfeitiçada por uma inimiga. Não pode atacá-la, mas pode se afastar ou ajudar um aliado conforme as ações disponíveis. Um capanga ataca Rina e erra: Enfeitiçado termina pelo ataque recebido, embora ela não tenha perdido vida.

## Remoção

Estas condições não concedem TR no fim do turno por padrão. Use a duração, as saídas do efeito ou uma habilidade de remoção. Quando a remoção cobrar por nível, uma condição Média custa **2 PE**, respeitando o teto e os demais custos da habilidade.

Se o efeito que aplica Enfeitiçado também causar dano, resolva esse ataque e seu dano antes de aplicar a condição. Um ataque ou efeito ofensivo posterior encerra a condição normalmente.

<!-- page:pesadas|Condições pesadas -->
# Condições pesadas

No fim de cada turno seu, faça o **TR indicado pelo efeito** para encerrar cada aplicação de condição Pesada que ainda estiver ativa. A tentativa não custa ação. Uma condição pode dificultar o próprio teste enquanto estiver valendo.

## Impedido

Seu deslocamento é **zero**. Seus ataques e TRs Físicos têm desvantagem; ataques contra você têm vantagem. A condição não retira, por si só, suas ações ou Bloquear.

## Cego

Você não enxerga e falha automaticamente em testes que exijam visão. Seus ataques têm desvantagem contra alvos que não consiga perceber por um sentido equivalente. Quem ataca você tem vantagem por sua cegueira **se conseguir enxergá-lo**.

Visão às cegas pode substituir a visão para ataques dentro dos limites que a concedem. Ela não permite ler nem cumpre um requisito que exija especificamente usar os olhos. **Sentir Energia localiza conforme sua regra, mas não substitui visão para retirar essa desvantagem.**

Quando duas criaturas não conseguem se enxergar, ambas atacam com desvantagem pela falta de visão. Outras fontes de vantagem e desvantagem continuam seguindo o cancelamento normal.

## Amedrontado

Enquanto enxergar a fonte do medo, você tem desvantagem em ataques e testes. Você não pode se aproximar dela voluntariamente, mesmo quando ela estiver fora de vista. Um efeito que o mova à força não é uma aproximação voluntária.

## Envenenado

Seus ataques e testes de perícia têm desvantagem. A condição não causa dano de Veneno por conta própria nem impõe desvantagem a todos os TRs.

## Atordoado

Você perde **uma Ação Padrão por turno** e não pode usar Reações enquanto a condição durar. Se tiver mais de uma Ação Padrão, perde apenas uma. Ação Bônus e Ação de Movimento continuam disponíveis, salvo outra restrição.

Atordoado não reduz sua Defesa nem impede Bloquear. A ação perdida não pode ser convertida em outra, e a condição não desfaz uma ação já concluída antes de ser aplicada.

> **Exemplo:** Rina começa o turno Atordoada. Ainda pode se mover e usar uma Bônus permitida, mas não usa sua Padrão. Fora do turno, continua podendo Bloquear, mas não pagar o revide de Aparar. No fim do turno, passa no TR e encerra a condição; isso não devolve a Padrão perdida daquele turno.

## Testes de saída

O TR mantém os modificadores aplicáveis enquanto a condição existir. Se Impedido exigir TR Físico para terminar, a tentativa tem desvantagem. Envenenado não prejudica um TR de Vigor por si. Registre na ficha do efeito **qual TR e qual CD** resolvem a saída, conforme as regras de [Condições](#condicoes).

<!-- page:cura|Cura -->
# Cura

Quando uma capacidade recupera vida, some o valor à vida atual, até o máximo que você tem naquele momento. O excesso é perdido. Uma redução de vida máxima limita a cura até ser removida.

> **Exemplo:** Rina tem 14 de vida, de um máximo de 20. Recebe 8 de cura e fica com 20. Os 2 excedentes não viram vida temporária.

## Receber tratamento

Use ação, custo, alcance, alvo e frequência da fonte. Uma capacidade que só atenda alguém com pelo menos 1 de vida não socorre quem está a zero. Remover uma condição não recupera vida, salvo quando a descrição também conceder cura.

**Sem Cura** impede receber cura enquanto durar. Uma cura tentada durante esse prazo não fica guardada para depois. Ela também não conta para o tratamento necessário a alguém com vida a zero.

A fonte deve ser compatível com o corpo que recebe o tratamento. Confira em Origens as necessidades de personagens com corpo construído e outras exceções. Um procedimento de reparo de objetos não trata uma criatura sem permissão expressa.

## Vida e Integridade

As duas reservas são recuperadas separadamente. Cura de vida não devolve Integridade. Recuperar Integridade não devolve vida. Uma capacidade que atenda ambas precisa dizer isso em sua descrição.

Para socorrer quem está a zero de vida, siga **Socorro**. Um efeito que ignore o limiar normal de recuperação continua sujeito a seus alvos, sua frequência e aos impedimentos de cura.

<!-- page:temporarios|Vida e energia temporárias -->
# Vida e energia temporárias

Algumas capacidades concedem uma reserva temporária. Anote-a separadamente da reserva comum. Ela é consumida primeiro e normalmente desaparece no fim da cena.

| Reserva | Limite e uso |
|---|---|
| Vida temporária | Até metade da vida máxima. Absorve dano antes da vida comum. |
| Energia temporária | Até metade dos PE máximos. É gasta antes dos PE comuns. |

Arredonde as metades para baixo, com mínimo 1 quando o máximo for positivo. Máximo zero não cria reserva temporária.

## Receber outra fonte

Reservas temporárias do mesmo recurso **não se somam**. Compare o que resta com a nova concessão, já limitada pelo teto, e fique com o maior valor. Vida e energia são recursos diferentes.

> **Exemplo:** Mei tem vida máxima 23 e recebe 15 de vida temporária. Seu teto é 11, então anota 11. Depois perde 8 e fica com 3. Uma nova concessão de 9 a deixa com 9 temporários. Se sofrer 12 de dano, perde os 9 temporários e 3 de vida.

O que restar desaparece ao terminar a cena, salvo duração própria. Uma proteção preparada imediatamente antes da situação para a qual será usada pode acompanhar essa situação. O mestre confirma essa continuidade quando a preparação for feita. Conservar a reserva não repõe pontos gastos.

## Limites

Vida temporária não aumenta a máxima e não é cura. Recebê-la a zero de vida não faz você acordar, não encerra Insistir e não conta como tratamento. Ela pode absorver dano posterior conforme sua regra normal.

Energia temporária paga custos de PE permitidos, mas não aumenta seus PE máximos. O descanso recupera PE comuns. Não refaz uma reserva temporária concedida por uma capacidade.

> **Exemplo:** Rina tem 8 PE máximos, 2 PE comuns e recebe 6 temporários. O teto deixa 4 temporários. Ao gastar 5 PE, usa esses 4 e mais 1 comum. Termina com 1 PE comum.

<!-- page:zero|Vida a zero -->
# Vida a zero

Ao chegar a **zero de vida**, você está **Morrendo**. Resolva primeiro as capacidades disparadas pela própria queda; em seguida, escolha **Aguentar** ou **Insistir**. Se uma dessas capacidades encerrar a queda, não há escolha. Estas regras são para personagens jogadores. Entidades seguem Invocações em campo. Um inimigo a zero de vida ou de Integridade é derrotado, e o mestre descreve o desfecho, como morte, fuga ou exorcismo, salvo uma regra da ficha dele.

| Escolha | Consequência |
|---|---|
| Aguentar | Você fica Inconsciente e espera socorro. Não perde vida máxima por essa escolha. |
| Insistir | Você permanece capaz de agir, pagando vida máxima enquanto estiver a zero. |

Anote a vida máxima que tinha ao cair, sem vida temporária. Esse será o **máximo de referência** até aquela queda terminar. Registre também sua janela de socorro e, se receber cura, o tratamento acumulado.

## Janela de socorro

A janela começa com **3 rodadas, menos 1 por Sequela que você já tenha**. As duas escolhas usam essa mesma janela. Se o resultado for zero, você fica Derrotado imediatamente, conforme **Derrota e morte**.

Marque o ponto da iniciativa em que caiu. Cada volta completa até esse ponto consome uma rodada da janela. A janela não concede turnos extras e não muda a iniciativa. Quando chegar a zero, você fica Derrotado.

Se a queda ocorrer fora de combate, organize turnos pelas regras de Iniciativa para resolver o socorro. Marque o começo dessa primeira rodada como ponto da queda. A primeira volta completa consome uma rodada da janela; uma tentativa de atendimento segue seus custos normais.

Cada ocorrência de dano que alcance sua vida enquanto estiver a zero consome mais **uma rodada da janela**, depois das defesas e da vida temporária. Um mesmo golpe com vários tipos de dano conta uma vez. Ataques distintos contam separadamente. Dano reduzido a zero não consome uma rodada.

O golpe que levou sua vida a zero inicia a queda. Seu excesso não consome outra rodada. Reduzir vida máxima como custo não é dano.

> **Exemplo:** Mei cai sem Sequelas, logo depois do turno de um inimigo. Tem três rodadas. Depois de uma volta completa da iniciativa, restam duas. Um ataque posterior causa dano à vida dela e consome outra. Resta uma rodada para socorrê-la.

## Aguentar

Você fica Inconsciente. Pode receber cura ou ser estabilizado conforme **Socorro**. A escolha conserva sua vida máxima, mas você não age para se proteger ou tratar os próprios ferimentos.

Escolher Aguentar não permite mudar para Insistir mais tarde naquela queda. Se já estava Inconsciente antes de perder o último ponto de vida, você Aguenta. Insistir não remove uma condição que já o impedia de agir.

<!-- page:insistir|Insistir -->
# Insistir

Ao escolher Insistir, você continua a zero de vida e conserva as ações, os recursos e as respostas que ainda puder usar. A escolha não devolve uma ação já gasta nem encerra condições. Pague vida máxima para permanecer agindo:

| Momento | Custo de vida máxima | Referência 80 |
|---|---|---|
| Ao escolher Insistir | 1/8 da referência. | Paga 10. Máximo atual 70. |
| Após uma volta completa, se ainda houver janela | 1/4 da referência. | Paga 20. Máximo atual 50. |
| Após outra volta completa, se ainda houver janela | 1/2 da referência. | Paga 40. Máximo atual 10. |

Arredonde cada custo para cima. Use sempre o máximo de referência da queda, mesmo depois de reduzi-lo. Primeiro desconte a rodada da janela. Só pague o próximo custo se ainda houver tempo e você continuar Insistindo.

A perda permanece até o descanso longo. Não é dano e não pode ser paga com vida temporária, reduzida por resistência ou anulada por uma redução de dano.

**A vida máxima precisa continuar em pelo menos 1.** Se não puder pagar o próximo custo, você passa a Aguentar, com a janela que ainda tiver. Pode fazer essa mudança antes, por escolha própria, sem ação. A perda já paga permanece. A mudança não reinicia a janela nem o tratamento.

## Socorro durante Insistir

Você precisa do mesmo tratamento de quem escolheu Aguentar, conforme Socorro. Recuperar apenas 1 de vida não encerra essa queda, salvo uma exceção expressa ao limiar. Você pode tratar a si mesmo enquanto conseguir agir e cumprir os requisitos da fonte.

Quando a janela termina, você fica Derrotado. Não recebe uma segunda janela por desabar. Dano à vida enquanto Insiste também consome rodadas dessa janela.

> **Exemplo:** Kaito cai com máximo 80 e uma Sequela. A janela é de duas rodadas. Paga 10 para Insistir e fica com máximo 70. Após uma volta completa, resta uma rodada. Paga 20 e seu máximo cai para 50. Se não receber socorro até a próxima volta, fica Derrotado. Não chega a pagar a terceira fração.

<!-- page:socorro|Socorro -->
# Socorro

Uma pessoa Morrendo pode ser curada ou estabilizada antes de sua janela acabar. Vida temporária não conta como tratamento.

## Cura

Acumule a cura válida recebida enquanto a pessoa estiver a zero. Ela volta a agir quando o total alcançar **20% do máximo de referência**, arredondado para cima. As curas podem vir de várias fontes e rodadas, inclusive durante Insistir.

Até alcançar esse total, a vida continua a zero. Anote o tratamento separadamente. Ao alcançar o limiar, converta o tratamento acumulado em vida, até o máximo atual. A contagem da queda termina e a pessoa recebe uma Sequela. O tratamento excedente ao máximo é perdido.

Calcule a cura pelo efeito usado, antes do limite da vida máxima reduzida. Uma fonte impedida ou incompatível não entra no total. Uma capacidade que exija um alvo acima de zero continua sem poder ser usada para esse socorro.

> **Exemplo:** Mei caiu com referência 23. Precisa de 5 de tratamento. Recebe 3 de cura e continua a zero. Outra cura de 3 completa 6. Ela volta com 6 de vida e uma Sequela. As curas anteriores não foram desperdiçadas.

Uma regra que permita levantar abaixo do limiar usa seu próprio valor de cura. Ela encerra a queda e concede a Sequela normalmente. Se já havia tratamento acumulado válido, some-o à cura e aplique o máximo atual. Nenhuma dessas fontes ressuscita alguém morto ou permite voltar à mesma cena depois de Derrotado, salvo permissão que diga isso expressamente.

## Estabilizar

Uma criatura a até **1,5 m**, com acesso físico ao alvo, pode gastar **Ação Padrão**, com uma mão livre e meios adequados de atendimento, para fazer **Medicina CD 14**. Para um corpo construído, use Entalhador ou Forja em lugar de Medicina. O alvo precisa estar Inconsciente e Morrendo. Quem Insiste pode escolher Aguentar antes do tratamento.

No sucesso, a pessoa fica **estável**. A janela para de diminuir pelo tempo enquanto ela não sofrer novo dano à vida. Não recupera vida, não acorda e conserva o tratamento acumulado e o tempo restante. Uma falha apenas gasta a ação. Outra tentativa é possível enquanto houver tempo.

Dano positivo à vida encerra a estabilidade e consome uma rodada da janela. Retome a contagem naquele ponto da iniciativa. A estabilização seguinte pode deter o tempo de novo, sem repor a rodada perdida.

Depois de sair do perigo, uma pessoa estável que conclua um descanso curto recupera **1 de vida** e recebe a Sequela da queda. Essa recuperação é uma exceção ao limiar de socorro. Não ocorre se houver um impedimento de cura. Também pode receber cura suficiente para voltar antes da pausa.

<!-- page:sequelas|Sequelas e Cicatrizes -->
# Sequelas e Cicatrizes

Sair de uma queda por chegar a zero de vida deixa **uma Sequela**. Registre-a quando o socorro encerrar a queda, inclusive com cura própria ou uma exceção ao limiar. A Sequela nova afeta a próxima queda. Se ficar Derrotado, registre-a ao sair desse estado, conforme Derrota e morte.

| Sequelas antes de cair | Janela de Aguentar ou Insistir |
|---|---|
| 0 | 3 rodadas. |
| 1 | 2 rodadas. |
| 2 | 1 rodada. |
| 3 ou mais | Fica Derrotado imediatamente. |

Sequelas não penalizam ataques, perícias ou TRs. Elas são removidas no descanso longo. Cura comum não as remove. Receber mais cura quando já está acima de zero não acrescenta Sequela.

> **Exemplo:** Mei cai e recebe socorro. Fica com uma Sequela. Se cair novamente antes do descanso longo, terá duas rodadas de janela, seja para Aguentar, seja para Insistir.

## Cicatrizes

Ferimentos graves podem deixar marcas duradouras. Depois da segunda queda na mesma missão, registre com o mestre se houve uma cicatriz e como ela ficou. Ela faz parte da aparência e da história do personagem.

Cicatrizes não concedem vantagem em toda Intimidação nem desvantagem em toda Persuasão. Uma reação específica depende da pessoa e da situação. Não há um modificador automático por receber tratamento de outra pessoa ou por usar cura própria.

A recuperação da vida não apaga uma cicatriz já estabelecida. Mudar uma marca permanente depende de uma possibilidade da história e de uma regra ou procedimento capaz de fazê-lo.

<!-- page:derrota|Derrota e morte -->
# Derrota e morte

Você fica **Derrotado** quando sua janela de socorro termina ou sua Integridade chega a zero. Sua participação ativa naquela cena termina. Você fica Inconsciente e precisa ser retirado do perigo.

Na regra de campanha padrão, derrota não causa morte automática. O mestre resolve o destino conforme os acontecimentos: resgate, captura, perda do objetivo ou outra consequência da missão. Ela não concede imunidade a perigos nem obriga inimigos a ignorar seu corpo.

## Missões com morte permanente

A campanha pode adotar morte ao esgotar a janela de socorro ou chegar a zero de Integridade. Essa regra precisa estar definida antes da missão. Use o mesmo critério para todos os personagens participantes. Não transforme uma derrota em morte retroativamente por preferência de quem está mestrando.

A morte também pode decorrer de uma consequência física que impeça qualquer socorro, estabelecida na cena. Não é uma redução comum de vida a zero. O mestre deve apresentar o risco antes de uma decisão que o personagem possa tomar.

## Recuperação depois da derrota

Se o personagem estiver vivo, converta o tratamento acumulado em vida, até seu máximo atual. Depois disso, a cura recupera vida normalmente, sem exigir o limiar de 20%. O personagem continua Derrotado: recuperar reservas não devolve sua participação naquela cena nem abre outra janela de socorro.

Depois de sair do perigo, pode recuperar a consciência ao concluir um descanso curto com atendimento, desde que tenha pelo menos **1 de vida e 1 de Integridade**. Se ainda estiver a zero de vida, use o teste de Estabilizar durante a pausa. No sucesso, recupera 1 de vida ao concluí-la. Uma nova pausa permite outra tentativa. Esse atendimento não restaura Integridade.

Ao sair da derrota, recebe uma Sequela se essa queda envolveu vida a zero. Conte apenas uma, mesmo que tenha recebido mais dano enquanto estava Derrotado. A derrota apenas por Integridade não gera essa Sequela.

Uma derrota por Integridade exige uma fonte que a recupere ou o descanso longo. **Concluir um descanso longo também encerra a inconsciência causada pela derrota**, desde que as duas reservas voltem a pelo menos 1. Aplique a recuperação desse descanso, incluindo a remoção das Sequelas. Outras causas de inconsciência conservam suas saídas próprias.

Um personagem morto não recupera vida por cura comum, descanso, estabilização ou remoção de condição. Voltar à vida exige uma regra expressa da campanha. Também não se transforma automaticamente numa maldição.

<!-- page:inconsciente|Inconsciente -->
# Inconsciente

Enquanto estiver Inconsciente, você não percebe o que ocorre à sua volta, não age, não se move por vontade própria, não usa Reações e não escolhe Bloquear. Concentrações e contenções que dependam de sua atuação terminam.

Se estiver de pé sem apoio que o sustente, cai e fica Derrubado. Sua Defesa estática permanece. Ataques contra você seguem sua posição e as demais condições presentes. A inconsciência não concede um crítico automático por si só.

Faça os TRs exigidos por efeitos com os modificadores aplicáveis, mesmo sem poder agir. Falha automaticamente num teste cuja tarefa dependa de uma ação consciente, como observar uma passagem ou sustentar uma conversa.

## Recuperar a consciência

A causa determina a saída. Vida a zero usa Socorro. Derrota exige o atendimento e a pausa definidos em Derrota e morte. Uma capacidade que faça alguém dormir indica como acordar.

Estar Inconsciente com vida acima de zero não inicia sozinho uma janela de Morrendo. Receber cura não encerra toda causa de inconsciência. Use a saída da regra que a provocou.
<!-- page:descansos|Descansos -->
# Descansos

O Ciclo Maldito usa dois tipos de descanso, definidos pela situação da missão. Não é necessário contar uma quantidade fixa de horas.

**Descanso curto:** uma pausa segura entre confrontos. Você parou e não está sendo perseguido naquele momento. **Descanso longo:** a missão terminou e você pôde parar de trabalhar.

O mestre confirma quando o descanso acontece e se o lugar é propício. Uma pausa contínua conta como um descanso; anunciar a mesma pausa várias vezes não repete a recuperação.

## Ambiente propício

Um lugar propício oferece abrigo, suprimentos e meios de atendimento. Exemplos incluem a escola, um posto oficial equipado, um hospital, a casa de um clã que recebe o grupo ou um veículo de apoio com kit.

Confira as condições reais: a escola sob ataque pode não oferecer descanso seguro; outro abrigo pode ter os recursos necessários. Sempre que possível, o mestre apresenta essas opções antes da missão para o grupo planejar o retorno.

## Descanso curto

Recupere **25% dos PE máximos**, sem ultrapassar o máximo. Vida e Integridade não voltam por esse descanso sozinho. Habilidades que curem ou permitam reparos durante a pausa continuam funcionando conforme suas regras.

Arredonde a recuperação para baixo, mínimo 1 quando a fração for positiva. Fora de ambiente propício, use a porcentagem do seu degrau de [Exaustão](#exaustao). Um resultado que diga **nada** continua sendo zero.

> **Exemplo:** Rina tem máximo 10 PE e está com 1. Sem Exaustão, recupera **2 PE** no descanso curto, ficando com 3. Sua vida não muda. Se tivesse 9 PE, recuperaria apenas 1, por já alcançar o máximo.

## Descanso longo

| Recurso | Em ambiente propício | Fora dele |
|---|---|---|
| Vida e PE | Voltam ao máximo. | Ficam, no mínimo, na metade do máximo. |
| Integridade | Volta ao máximo; estágios são limpos. | Volta ao máximo; estágios são limpos. |
| Exaustão | É removida. | Permanece. |
| Sequelas e máximo perdido por Insistir | Sequelas são removidas; máximo é restaurado. | Sequelas são removidas; máximo é restaurado. |

Restaure o máximo perdido por Insistir antes de calcular a vida recuperada. Fora de lugar propício, a metade é o mínimo em que a reserva fica após o descanso. Não se soma ao saldo nem reduz uma reserva que já esteja acima desse valor. Arredonde a metade para baixo, com mínimo 1 quando o máximo for positivo.

> **Exemplo:** ao terminar a missão fora da base, Mei tem máximo 23 de vida e saldo 3. Vai a **11**, metade arredondada para baixo. Se já tivesse 18, conservaria 18. Um personagem com máximo 60 PE e saldo 8 vai a **30 PE**.

Dormir durante uma missão ainda em andamento renova usos **por dia**; não equivale automaticamente ao descanso longo descrito aqui.

<!-- page:exaustao|Exaustão -->
# Exaustão

**Da quarta luta do dia em diante, cada luta acrescenta um degrau de Exaustão, até o máximo de três.** Registre o total ao terminar cada confronto. A primeira, a segunda e a terceira luta não acrescentam degraus por essa regra.

O mestre identifica o que contou como luta. Um combate com oposição, uma fuga que exigiu recursos ou uma contenção sob ataque podem contar. Um treino ou uma ameaça encerrada sem esforço relevante normalmente não contam. A decisão não depende apenas de ter rolado iniciativa.

## Efeitos

Os efeitos dos degraus anteriores continuam valendo. A última coluna vale para descanso curto **fora de ambiente propício**.

| Degrau | Efeito | Recuperação de PE |
|---|---|---|
| 0 | Nenhuma penalidade. | 25% do máximo. |
| 1 | Desvantagem em perícias e ofícios. | 15% do máximo. |
| 2 | Deslocamento limitado a 4,5 m. | 5% do máximo. |
| 3 | Desvantagem em ataques e TRs. | Nada. |

Em ambiente propício, o descanso curto devolve **25% em qualquer degrau**. Ele não remove a Exaustão por isso. O limite de 4,5 m não aumenta um deslocamento que já esteja menor ou zerado.

> **Exemplo:** com máximo 8 PE, Rina recupera 2, 1, 1 ou zero em uma pausa fora da base, conforme esteja nos degraus 0, 1, 2 ou 3. Nos degraus 1 e 2, o valor coincide pelo arredondamento e pelo mínimo de 1; as penalidades continuam diferentes.

## Recuperação

Descanso longo em ambiente propício remove toda a Exaustão. Fora dele, ela permanece. O mestre também pode retirar um degrau quando a situação justificar, como após uma noite de recuperação adequada; não acrescenta degraus fora dos gatilhos da regra.

Recomeçar a contagem de lutas de um novo dia não remove os degraus que você já tinha.

## Exaustão e Integridade

Quando ambas impõem a mesma penalidade, use a pior, sem multiplicar esses cortes entre si. Desvantagem continua sem se acumular. Para movimento, compare o limite da Exaustão com metade do deslocamento pela Integridade e use o menor; ajuste o resultado à escala de 1,5 m.

> **Exemplo:** com deslocamento 9 m, Exaustão 2 limita a 4,5 m; Integridade no estágio 2 também resulta em 4,5 m. A combinação mantém **4,5 m**. Com deslocamento 6 m, a metade da Integridade é 3 m, então usa **3 m**.

As consequências que só uma das duas impõe permanecem: o custo adicional de PE e o teto de Classe são da Integridade. Recuperar PE não remove essas penalidades.

<!-- page:usos|Cena e usos de habilidades -->
# Cena e usos de habilidades

O texto de uma habilidade informa quando seus usos voltam. Marque cada uso gasto na ficha e apague a marca quando cumprir a recuperação indicada. Recuperar um uso não devolve os PE pagos anteriormente.

| Limite | Quando o uso volta |
|---|---|
| Por cena | Quando aquela cena termina. |
| Por descanso curto | Ao concluir esse descanso. |
| Por dia | Depois de dormir para começar um novo dia. |
| Por descanso longo | Ao concluir esse descanso, no fim da missão. |

Siga o nome completo do limite. Uma habilidade que recarrega apenas em descanso longo não volta por fazer uma pausa curta. Se disser só “por descanso”, sem especificar qual, a descrição precisa ser completada antes de entrar em jogo.

## Cena

Uma **cena** é um trecho de jogo com uma situação em andamento. Pode abranger uma sala, várias salas ou um combate. Ela termina quando a pressão daquele trecho acaba: o inimigo foi vencido, o grupo escapou ou o problema imediato foi resolvido. O mestre anuncia a mudança quando ela afetar recursos.

Mudar de cômodo durante a mesma perseguição não cria, por si só, outra cena. Da mesma forma, terminar uma luta não garante uma pausa segura se ainda houver perseguidores próximos.

> **Exemplo:** uma capacidade pode atender cada aliado uma vez por cena. Trocar de usuário não permite repeti-la no mesmo alvo se o limite for por alvo. A descrição precisa informar a quem pertence o limite.

## Missões longas

Uma missão pode atravessar vários dias. Dormir renova os usos por dia; o descanso longo depende de encerrar a missão e poder parar. Não renove todas as habilidades só porque a mesa terminou a sessão.

> **Exemplo:** em uma missão de três dias, Rina pode renovar uma habilidade por dia após cada noite de sono. Uma habilidade por descanso longo permanece gasta até o descanso de encerramento da missão. Se uma pausa segura no segundo dia contar como descanso curto, apenas os usos com essa recuperação voltam por causa dela.

## Conferência da ficha

Ao concluir um descanso, atualize vida, PE e Integridade; confira máximos reduzidos, estágios, Sequelas e Exaustão; depois renove os usos correspondentes. Cicatrizes permanecem. Vida e energia temporárias seguem a duração de suas fontes e o fim da cena, não uma recuperação automática pelo descanso.

Consequências permanentes continuam registradas. A recuperação das reservas não desfaz uma morte ou restaura automaticamente uma entidade destruída.
