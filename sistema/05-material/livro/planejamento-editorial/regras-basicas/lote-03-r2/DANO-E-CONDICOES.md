<!-- page:dano|Dano -->
# Dano

Quando um ataque ou efeito causa dano, calcule quanto chega ao alvo e desconte esse valor dos pontos de vida dele. **Dano reduzido a zero não tira vida nem se transforma em cura.** A perda de vida não diminui seus bônus por si só; condições e outros efeitos podem impor penalidades.

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

Reduzir o dano a zero mantém o resultado do ataque. Uma condição aplicada **ao acertar** ainda pode entrar; um efeito que exija **causar dano** precisa de dano maior que zero. Resolva cada ataque separadamente. Ao chegar a zero de vida, consulte **Aguentar e Insistir**, nas regras de Recuperação.

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

**Força** é dano de energia concentrada que atinge o alvo como um impacto sobrenatural, como um projétil de energia sem elemento. Integra o grupo **Especiais**. Socos, quedas e impactos de objetos causam **Concussão** quando sua regra indicar esse tipo.

O tipo Força não usa automaticamente o atributo Força, não empurra o alvo e não ignora proteção ou resistência. Essas propriedades precisam estar no efeito.

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

## Cobrir-se de energia

Depois de determinar o dano de um golpe contra você e antes de descontá-lo, pode gastar **Reação e 2 PE** para reduzir **1,5 × seu refino**, arredondado para baixo. Ao fazer isso, você fica **sem proteção até o fim do seu próximo turno**. Atualize a Defesa e a base de Bloquear para os ataques seguintes; o acerto que já foi resolvido permanece como estava.

A perda afeta a proteção que você estiver usando, inclusive uniforme e escudo. Os demais componentes da Defesa permanecem. A Bênção equivalente usa Lapidação no lugar de refino e conserva os próprios requisitos.

> **Exemplo:** Rina tem Defesa 17: base 10, Destreza 3 e proteção 4. Com refino 3, paga Reação e 2 PE para reduzir **4** de um golpe que já acertou. Sua Defesa passa a **13**, e Bloquear a **2d10 + 2**, até o fim do próximo turno dela. A redução não permite recalcular aquele acerto com outra Defesa.

## Reduções do Bastião

**Duro de Matar** funciona sempre que seu Bloquear falhar. Some os **dois dados de Bloquear e sua Constituição**, sem incluir o modificador de Defesa. A habilidade não tem limite de uma vez por rodada.

**Casca Grossa** tem outro gatilho: um ataque assumido por Olhos Em Mim acertou você. Depois da resolução da Defesa ou de Bloquear, role **2d10 - 1 + Constituição** e reduza esse valor. Ela se soma às reduções aplicáveis, inclusive Duro de Matar quando Bloquear tiver falhado.

> **Exemplo:** um Muro com Constituição 3 assume um golpe e falha em Bloquear, cujos dados foram 7 e 4. Duro de Matar reduz **14**. Casca Grossa resulta em 6 e 5: **6 + 5 - 1 + 3 = 13**. Se o golpe causaria 40, restam **13 de dano**. Se Alicerce desse resistência ao tipo, os 40 cairiam primeiro para 20, e as duas reduções zerariam o dano.

Assumir um golpe já gasta sua Reação antes da rolagem. Se essa for a única Reação disponível, você não pode também pagar Cobrir-se de energia contra ele. Bloquear, Duro de Matar e Casca Grossa não exigem essa segunda Reação.

## Limites do efeito

Uma redução restrita a ataques não protege de uma queda por esse motivo. Uma regra que ignore parte da Redução de Dano não ignora também resistência ou vida temporária. Custos são pagos mesmo quando outras proteções acabam zerando o dano.

<!-- page:alma|Dano na alma -->
# Dano na alma

**Integridade** é o recurso do Projeto M que acompanha o dano de Alma. Anote seu máximo e valor atual separadamente da vida.

> **Integridade máxima do personagem = 20 + (Essência + 5) × (nível - 1).**

Inimigos e outras criaturas que não sejam personagens jogadores usam **metade da vida máxima, arredondada para baixo**, salvo regra específica de sua ficha.

## Receber dano de Alma

Cada ponto de dano de Alma desconta **1 de vida e 1 de Integridade**. Ele não reduz sua vida máxima. Um efeito que diga atingir **somente Integridade**, como Cisão, segue essa exceção.

Dano de Alma entra sem a redução pela metade própria do TR ou da resistência. Ao recebê-lo, faça **TR de Espírito contra a CD do atacante**, no máximo uma vez por rodada. O teste decide o avanço de estágio; passar nele não reduz o dano.

Teste no primeiro dano de Alma recebido na rodada. Os demais ainda descontam as reservas e podem ultrapassar os limites da tabela. Reduções numéricas aplicáveis ao golpe entram antes da perda das reservas. Vida temporária pode absorver a parte que iria à vida, sem impedir a perda de Integridade.

## Estágios

Compare a Integridade perdida com o máximo. Ao alcançar um limite da tabela, avance até aquele estágio, se ainda não o tiver atingido. Depois, uma falha no TR de Espírito acrescenta **um estágio**, até o máximo de 4.

| Integridade perdida | Estágio | Efeito |
|---|---|---|
| Pelo menos 1/4 | 1 | Desvantagem em testes de perícia. |
| Pelo menos 1/2 | 2 | Deslocamento pela metade; cada feitiço custa +1 PE por Classe. |
| Pelo menos 3/4 | 3 | Desvantagem em ataques e TRs; limite de conjuração cai à metade da Classe máxima, arredondada para baixo (mínimo 1 se já possuir Classe 1). |
| Toda | 4 | O personagem deixa de agir sob o controle normal do jogador; o mestre determina o desfecho. |

Os efeitos dos estágios anteriores continuam valendo. Mantenha o maior estágio atingido até que uma regra o remova. Para saber se alcançou uma fração, compare os valores exatos: com Integridade máxima 26, perder 6 ainda não alcança 1/4; perder 7 alcança.

> **Exemplo:** Kaori está no nível 2 e tem Essência 1: Integridade máxima **26**. Recebe 7 de Alma: perde 7 de vida, fica com 19 de Integridade e chega ao estágio 1. Passar no TR mantém esse estágio; falhar a leva ao estágio 2, sem retirar mais Integridade por essa falha.

## Recuperação

Cura comum devolve vida, sem restaurar Integridade. O descanso longo devolve toda a Integridade e limpa os estágios. **Remenda** recupera Integridade conforme sua descrição; recuperar pontos não remove, por si só, um estágio já atingido. Ao chegar a zero de vida, resolva também **Aguentar e Insistir**. O estágio 4 encerra a possibilidade de Aguentar.

<!-- page:condicoes|Condições -->
# Condições

Uma **condição** altera o que você consegue fazer enquanto durar. Registre seu nome, a fonte, o momento em que termina e os testes ou ações que permitem encerrá-la. Os treze nomes deste capítulo têm efeitos próprios; uma condição não inclui outra só porque seus nomes parecem relacionados.

## Aplicação e duração

A habilidade informa como aplica a condição: por acerto, falha em TR ou outro gatilho. **Use a duração escrita no efeito.** Uma condição criada pela Melhoria Condição dura uma rodada, salvo Concentrada, Duradoura ou outra regra específica. Quando o efeito disser apenas uma rodada, ele termina no começo do próximo turno de quem o aplicou.

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

**Inconsciente, Exaustão e Invisível** têm regras próprias. Inconsciente e Exaustão ficam em Recuperação; Invisível é um benefício tratado nas regras de Percepção. Eles não são opções compradas por esta lista de treze condições.

<!-- page:leves|Condições leves -->
# Condições leves

## Lento

Seu deslocamento cai pela metade e você não pode usar Ação Bônus. Converter outra ação em Bônus não permite usá-la enquanto essa proibição durar.

## Incapacitado

Você **não pode Bloquear**. Ataques corpo a corpo com arma ou desarmados **que acertarem você** são críticos. Ataques à distância e de conjuração não ganham crítico por essa condição; um feitiço de Toque continua sendo conjuração.

Você conserva suas ações e sua Defesa estática. O crítico segue a regra de dados dobrados e suas exceções expressas, como Golpe Cirúrgico. A condição não faz o ataque acertar automaticamente.

## Derrubado

Você está no chão. Só pode se deslocar rastejando, usando **metade do seu deslocamento**. A distância final segue a escala de 1,5 m de Movimento. Seus ataques têm desvantagem. Ataques contra você têm **vantagem a até 1,5 m** e **desvantagem de mais longe**.

Levantar de um Derrubado comum custa sua **Ação de Movimento inteira**. Uma habilidade pode permitir outro custo. Se um efeito mantiver você Derrubado por uma duração, precisa encerrar essa manutenção antes de levantar. Estar Agarrado não impede gastar a ação para levantar; você continua no mesmo espaço e agarrado.

## Agarrado

Seu deslocamento é **zero**. Você ainda pode atacar, conjurar e Bloquear, cumprindo os requisitos dessas ações. A contenção termina se quem o segura ficar Incapacitado, soltar você ou deixar de mantê-lo ao alcance.

Para escapar de um agarrão comum, gaste **Ação Padrão** e faça **TR Físico contra a CD da contenção**. No sucesso, ela termina. Feitiços e habilidades seguem suas saídas próprias. Consulte **Agarrado: escapar e arrastar**, nas regras comuns, para mão ocupada, arrasto e múltiplas contenções.

Ataques à distância contra alguém envolvido no agarrão usam a Defesa do alvo escolhido e a cobertura que a posição oferecer. O agarrão não troca o alvo aleatoriamente.

## Desarmado

A arma que você perdeu está no chão ou com outra criatura. Você pode recuperá-la, sacar uma reserva ou atacar desarmado, pagando os custos normais de cada opção. A condição não impede usar outra arma disponível.

## Surdo

Você não ouve e falha automaticamente em testes que precisem de audição. Recebe **-2 na iniciativa**. A penalidade entra quando rolar iniciativa; receber Surdo no meio do combate não muda retroativamente a ordem já registrada.

> **Exemplo:** um inimigo Incapacitado ainda pode atacar Rina. Se também ficar Atordoado, perde uma Ação Padrão e não usa Reações por causa de Atordoado; sua Defesa estática permanece, e Incapacitado continua impedindo Bloquear.

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
