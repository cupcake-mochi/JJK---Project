# R65 | Parte 03 | Requisito no texto corrido

Propostas para o capítulo 6, Caminhos e Trilhas, sobre a edição publicada R64 (9ea841eb).

**65 trechos**. O lote revê 78 ocorrências e propõe trocar 67.

Fonte de referência (SHA-256) `8b69a31d4e253faac4dfdeafb4c72f57cc75f72e8517df46dfa6a73fe4bb82dd`.

O antes e o depois abaixo mostram cada troca desta parte isoladamente. A validação aplica as partes já prontas em sequência numa cópia.

Foram conferidos os números por bloco, as âncoras, os destinos dos links, os cabeçalhos de seção e os rótulos de Requisito. Os 28 validadores de mecânica passaram com esta parte e as anteriores na cópia.

## Usos que ficam

Os 10 rótulos de Requisito, Requisitos e Requisitos comuns seguem como aprovados. O título de seção Requisitos da aplicação também fica.

## R65-03-001

`bastiao--bas-defesa` · linha 3427

**Antes**

~~~~text
Você pode usar mesmo se já estava abaixo da metade antes do golpe. Perder apenas vida temporária não cumpre o gatilho. Se tiver chegado a zero, siga [Socorro](#dano--socorro), em Dano e recuperação. Enquanto estiver Morrendo, essa cura entra no tratamento acumulado; para encerrar a condição, você ainda precisa cumprir os requisitos do socorro.
~~~~

**Depois**

~~~~text
Você pode usar mesmo se já estava abaixo da metade antes do golpe. Perder apenas vida temporária não cumpre o gatilho. Se tiver chegado a zero, siga [Socorro](#dano--socorro), em Dano e recuperação. Enquanto estiver Morrendo, essa cura entra no tratamento acumulado; para encerrar a condição, você ainda precisa cumprir o que o socorro exige.
~~~~

## R65-03-002

`bastiao--bas-casca` · linha 3512

**Antes**

~~~~text
O acerto continua sendo um acerto mesmo que o dano chegue a zero. Efeitos que acompanhem o golpe usam seus próprios requisitos. Resistências são aplicadas antes das reduções, como explica Dano.
~~~~

**Depois**

~~~~text
O acerto continua sendo um acerto mesmo que o dano chegue a zero. Efeitos que acompanhem o golpe seguem suas próprias exigências. Resistências são aplicadas antes das reduções, como explica Dano.
~~~~

## R65-03-003

`bastiao--bas-combatente` · linha 3629

**Antes**

~~~~text
O feitiço conserva sua própria resolução, seus requisitos, alcance e alvos. O acerto que você recebeu não garante o acerto do feitiço. Um ataque interceptado que erre não permite Retaliação. Dano reduzido a zero não apaga o acerto.
~~~~

**Depois**

~~~~text
O feitiço conserva sua própria resolução, suas condições de uso, alcance e alvos. O acerto que você recebeu não garante o acerto do feitiço. Um ataque interceptado que erre não permite Retaliação. Dano reduzido a zero não apaga o acerto.
~~~~

## R65-03-004

`bastiao--bas-combatente` · linha 3639

**Antes**

~~~~text
O crítico de um ataque concedido somente por Reação ou Bônus não cumpre o primeiro gatilho. O segundo não exige que o TR venha de uma criatura dentro de Olhos Em Mim: essa área é requisito de Nem Um Arranhão, não de Embalo.
~~~~

**Depois**

~~~~text
O crítico de um ataque concedido somente por Reação ou Bônus não cumpre o primeiro gatilho. O segundo não exige que o TR venha de uma criatura dentro de Olhos Em Mim. Nem Um Arranhão exige essa área.
~~~~

## R65-03-005

`bastiao--bas-oportunista` · linha 3665

**Antes**

~~~~text
Resolva o ataque e depois o feitiço, **uma única vez na ação**, mesmo que o ataque tenha errado. O feitiço não gasta outra ação, mas cobra seus **PE normais** e conserva alcance, alvos, Selo, resolução e demais requisitos. Ele precisa permitir essa aplicação imediata; a habilidade não abrevia [Carregar](#catalogo--restricao-carregar), preparo que adia a liberação do feitiço para o turno seguinte, nem outros preparos.
~~~~

**Depois**

~~~~text
Resolva o ataque e depois o feitiço, **uma única vez na ação**, mesmo que o ataque tenha errado. O feitiço não gasta outra ação, mas cobra seus **PE normais** e conserva alcance, alvos, Selo, resolução e as demais condições de uso. Ele precisa permitir essa aplicação imediata; a habilidade não abrevia [Carregar](#catalogo--restricao-carregar), preparo que adia a liberação do feitiço para o turno seguinte, nem outros preparos.
~~~~

## R65-03-006

`vanguarda--van-conclusoes` · linha 3788

**Antes**

~~~~text
Escolha uma Conclusão compatível com a fonte do ataque e com seus requisitos. **A declaração consome a Sequência**, mesmo no erro ou na resistência. Concluir não custa PE adicional por si só.
~~~~

**Depois**

~~~~text
Escolha uma Conclusão compatível com a fonte do ataque, desde que cumpra as exigências da opção. **A declaração consome a Sequência**, mesmo no erro ou na resistência. Concluir não custa PE adicional por si só.
~~~~

## R65-03-007

`vanguarda--van-avanco` · linha 3850

**Antes**

~~~~text
Declare as duas antes dos dados, com todos os requisitos cumpridos. Um ataque ou feitiço resolve seu dano normal uma vez. Cada Conclusão tem seu TR, quando houver. Resolva os testes antes de aplicar os novos efeitos. Explorar o Desequilíbrio modifica apenas um teste que cumpra essas condições.
~~~~

**Depois**

~~~~text
Declare as duas antes dos dados, depois de cumprir todas as exigências. Um ataque ou feitiço resolve seu dano normal uma vez. Cada Conclusão tem seu TR, quando houver. Resolva os testes antes de aplicar os novos efeitos. Explorar o Desequilíbrio modifica apenas um teste que cumpra essas condições.
~~~~

## R65-03-008

`vanguarda--van-estocada` · linha 3873

**Antes**

~~~~text
Escolha **Essência ou Inteligência**. Some o valor atual desse atributo ao seu **PE máximo** e use-o no lugar de Força ou Destreza para o acerto e dano das armas de suas categorias escolhidas. Os requisitos de Força permanecem.
~~~~

**Depois**

~~~~text
Escolha **Essência ou Inteligência**. Some o valor atual desse atributo ao seu **PE máximo** e use-o no lugar de Força ou Destreza para o acerto e dano das armas de suas categorias escolhidas. As armas continuam exigindo a mesma Força.
~~~~

## R65-03-009

`vanguarda--van-feiticos` · linha 3905

**Antes**

~~~~text
Desorientar e os outros efeitos novos não prejudicam outro TR do mesmo lançamento. Em Conclusão Dupla, escolha duas opções deste catálogo e respeite todos os requisitos da Dupla.
~~~~

**Depois**

~~~~text
Desorientar e os outros efeitos novos não prejudicam outro TR do mesmo lançamento. Em Conclusão Dupla, escolha duas opções deste catálogo e cumpra todas as exigências da Dupla.
~~~~

## R65-03-010

`vanguarda--van-bote` · linha 3927

**Antes**

~~~~text
Declare Ferrão antes do ataque da arma. Se ela errar, o Classe 0 não é lançado. Se acertar, ele resolve sua própria rolagem e requisitos, inclusive alcance e crítico. Esse lançamento é uma exceção ao limite de conjurações no turno e não concede outro ataque de Compasso. Não é necessário que o alvo tenha falhado no TR adicional da Conclusão principal.
~~~~

**Depois**

~~~~text
Declare Ferrão antes do ataque da arma. Se ela errar, o Classe 0 não é lançado. Se acertar, resolva a rolagem do feitiço e siga suas regras de uso, incluindo alcance e crítico. Esse lançamento é uma exceção ao limite de conjurações no turno e não concede outro ataque de Compasso. Não é necessário que o alvo tenha falhado no TR adicional da Conclusão principal.
~~~~

## R65-03-011

`vanguarda--van-yumi` · linha 3939

**Antes**

~~~~text
As Conduções e Conclusões **comuns** são as do Caminho; as **próprias** são as da rota escolhida. Ambas usam o procedimento da Sequência e seus custos, salvo exceção escrita na entrada. Você pode usar as opções comuns quando cumprir seus requisitos.
~~~~

**Depois**

~~~~text
As Conduções e Conclusões **comuns** são as do Caminho; as **próprias** são as da rota escolhida. Ambas usam o procedimento da Sequência e seus custos, salvo exceção escrita na entrada. Você pode usar as opções comuns quando cumprir o que cada opção exige.
~~~~

## R65-03-012

`vanguarda--van-yumi` · linha 3970

**Antes**

~~~~text
A soltura é feita da sua posição real contra o mesmo alvo. Confira os requisitos da Conclusão na armação e, na soltura, aqueles que dependem da situação atual. Pague os custos adicionais do ataque na armação. Eles não retornam se a armação for desfeita. Separe uma flecha disponível, que não pode servir a outro disparo enquanto estiver armada. Consuma essa munição ao soltá-la. Desfazer a armação não destrói a flecha, mas não devolve o ataque comprometido ou a Sequência.
~~~~

**Depois**

~~~~text
A soltura é feita da sua posição real contra o mesmo alvo. Confira as exigências da Conclusão na armação e, na soltura, aqueles que dependem da situação atual. Pague os custos adicionais do ataque na armação. Eles não retornam se a armação for desfeita. Separe uma flecha disponível, que não pode servir a outro disparo enquanto estiver armada. Consuma essa munição ao soltá-la. Desfazer a armação não destrói a flecha, mas não devolve o ataque comprometido ou a Sequência.
~~~~

## R65-03-013

`vanguarda--van-executor` · linha 4235

**Antes**

~~~~text
**Ação Bônus, uma vez por turno próprio.** Com um ataque corpo a corpo disponível contra o alvo da Sequência, sem ter Conduzido ou Concluído naquele turno, anuncie uma **Conclusão corpo a corpo com TR cujos requisitos já foram cumpridos**. O alvo precisa perceber você.
~~~~

**Depois**

~~~~text
**Ação Bônus, uma vez por turno próprio.** Com um ataque corpo a corpo disponível contra o alvo da Sequência, sem ter Conduzido ou Concluído naquele turno, anuncie uma **Conclusão corpo a corpo com TR**, desde que já cumpra suas exigências. O alvo precisa perceber você.
~~~~

## R65-03-014

`vanguarda--van-executor` · linha 4265

**Antes**

~~~~text
Rasteira, Desarme e Quebrar o Ritmo permanecem disponíveis pelos requisitos comuns. Ponto Fraco não participa da Finta porque não exige TR.
~~~~

**Depois**

~~~~text
Rasteira, Desarme e Quebrar o Ritmo continuam disponíveis se você cumprir as exigências normais. Ponto Fraco não participa da Finta porque não exige TR.
~~~~

## R65-03-015

`vanguarda--van-executor-avanco` · linha 4275

**Antes**

~~~~text
Depois da resposta à Finta, pode escolher **outra Conclusão corpo a corpo com TR**, diferente e cujos requisitos já tenham sido cumpridos.
~~~~

**Depois**

~~~~text
Depois da resposta à Finta, pode escolher **outra Conclusão corpo a corpo com TR**, diferente, desde que já cumpra suas exigências.
~~~~

## R65-03-016

`vanguarda--van-executor-avanco` · linha 4295

**Antes**

~~~~text
**Uma vez por cena**, anuncie **duas Conclusões diferentes cujos requisitos já foram cumpridos** ao iniciar a Finta.
~~~~

**Depois**

~~~~text
**Uma vez por cena**, anuncie **duas Conclusões diferentes que você já possa usar** ao iniciar a Finta.
~~~~

## R65-03-017

`guia--guia-tratamento` · linha 4749

**Antes**

~~~~text
A escolha também vale quando o aliado abandona a Abertura para receber o socorro antes. Cura e retirada de condição continuam sendo alternativas do mesmo Cuidado. Para preparar o Cuidado, o aliado precisa poder receber cura ou ter uma condição tratável. Quando recebê-lo, escolha uma das opções cujos requisitos ele cumprir naquele momento. Quem está acima da metade da vida e sem condição tratável não recebe um Cuidado apenas para guardá-lo.
~~~~

**Depois**

~~~~text
A escolha também vale quando o aliado abandona a Abertura para receber o socorro antes. Cura e retirada de condição continuam sendo alternativas do mesmo Cuidado. Para preparar o Cuidado, o aliado precisa poder receber cura ou ter uma condição tratável. Quando recebê-lo, escolha uma das opções que ele possa receber naquele momento. Quem está acima da metade da vida e sem condição tratável não recebe um Cuidado apenas para guardá-lo.
~~~~

## R65-03-018

`emanador--ema-modulacoes` · linha 4899

**Antes**

~~~~text
Os requisitos de cada Melhoria permanecem. Sustentação não transforma um bônus para o próximo ataque em benefício para todos os ataques, e Preparação segue seu próprio momento de pagamento e disparo.
~~~~

**Depois**

~~~~text
Cada Melhoria continua com suas exigências. Sustentação não transforma um bônus para o próximo ataque em benefício para todos os ataques, e Preparação segue seu próprio momento de pagamento e disparo.
~~~~

## R65-03-019

`emanador--ema-instintiva` · linha 4971

**Antes**

~~~~text
A Expressão Familiar correspondente recebe o mesmo benefício quando usada como Padrão. Os limites da própria ficha, seus requisitos e as despesas adicionais continuam valendo.
~~~~

**Depois**

~~~~text
A Expressão Familiar correspondente recebe o mesmo benefício quando usada como Padrão. Os limites da própria ficha, suas condições de uso e as despesas adicionais continuam valendo.
~~~~

## R65-03-020

`emanador--ema-condutor` · linha 4998

**Antes**

~~~~text
Sua arma e seus feitiços dividem a mesma rotina. Você pode alternar os dois ou desenvolver o combate com a categoria escolhida. O vínculo acrescenta propriedades à arma sem dispensar seus requisitos de uso.
~~~~

**Depois**

~~~~text
Sua arma e seus feitiços dividem a mesma rotina. Você pode alternar os dois ou desenvolver o combate com a categoria escolhida. O vínculo acrescenta propriedades à arma sem dispensar o que ela exige para ser usada.
~~~~

## R65-03-021

`emanador--ema-condutor` · linha 5013

**Antes**

~~~~text
Escolha **uma categoria de armas** e receba treino com ela. Escolha **Essência ou Inteligência**: pode usar o atributo no acerto e dano com suas armas dessa categoria. Os requisitos de Força continuam valendo.
~~~~

**Depois**

~~~~text
Escolha **uma categoria de armas** e receba treino com ela. Escolha **Essência ou Inteligência**: pode usar o atributo no acerto e dano com suas armas dessa categoria. As armas continuam exigindo a mesma Força.
~~~~

## R65-03-022

`emanador--ema-condutor` · linha 5032

**Antes**

~~~~text
São duas resoluções separadas. O feitiço não é acrescentado ao dano da arma, e o ataque conserva Canalizar em Golpe quando seus requisitos permitirem.
~~~~

**Depois**

~~~~text
São duas resoluções separadas. O feitiço não é acrescentado ao dano da arma, e o ataque conserva Canalizar em Golpe quando você cumprir suas exigências.
~~~~

## R65-03-023

`emanador--ema-propriedades` · linha 5072

**Antes**

~~~~text
Somente uma arma comum ou de **Grau 4 ou 3** recebe esta Propriedade. Ao sacá-la ou manifestá-la, mude seu perfil para outra arma da mesma categoria, cujo requisito de Força você cumpra.
~~~~

**Depois**

~~~~text
Somente uma arma comum ou de **Grau 4 ou 3** recebe esta Propriedade. Ao sacá-la ou manifestá-la, mude seu perfil para outra arma da mesma categoria, que você tenha Força suficiente para usar.
~~~~

## R65-03-024 **Trecho conferido pelo validador de Fundamento**

`emanador--ema-manifestacao` · linha 5130

**Antes**

~~~~text
Confira visão, trajeto e requisitos ao resolver cada parte. O novo ponto não permite ignorar uma Restrição. Toque conserva sua distância ao alvo. Aura permanece centrada em você. Queima-Roupa conserva seus alvos a até 1,5 m em Projétil ou a origem da área em você, dependendo da Forma escolhida.
~~~~

**Depois**

~~~~text
Confira visão, trajeto e as exigências de uso ao resolver cada parte. O novo ponto não permite ignorar uma Restrição. Toque conserva sua distância ao alvo. Aura permanece centrada em você. Queima-Roupa conserva seus alvos a até 1,5 m em Projétil ou a origem da área em você, dependendo da Forma escolhida.
~~~~

## R65-03-025

`emanador--ema-contraponto` · linha 5223

**Antes**

~~~~text
Se Contraponto também produzir outro Eco, escolha qual guardar dentro da sua capacidade. Na capacidade de um, não conserve ambos. A conjuração pode usar uma peça Pesada pelo Desdobramento pago, desde que cumpra seus requisitos, mas não registrá-la como Eco.
~~~~

**Depois**

~~~~text
Se Contraponto também produzir outro Eco, escolha qual guardar dentro da sua capacidade. Na capacidade de um, não conserve ambos. A conjuração pode usar uma peça Pesada pelo Desdobramento pago, desde que cumpra o que a peça exige, mas não registrá-la como Eco.
~~~~

## R65-03-026

`evocador--ev-intervencoes` · linha 5480

**Antes**

~~~~text
**Requisitos comuns:** você está consciente e percebe a destinatária ativa a até **18 m**. Ela pode ser qualquer invocação sua que cumpra os requisitos da intervenção.
~~~~

**Depois**

~~~~text
**Requisitos comuns:** você está consciente e percebe a destinatária ativa a até **18 m**. Ela pode ser qualquer invocação sua que cumpra o que a intervenção exige.
~~~~

## R65-03-027

`evocador--ev-intervencoes` · linha 5484

**Antes**

~~~~text
Orientações de movimento, preparo e recolhimento precisam ser percebidas e compreendidas pela invocação. A capacidade original conserva seus custos, seus requisitos e suas durações.
~~~~

**Depois**

~~~~text
Orientações de movimento, preparo e recolhimento precisam ser percebidas e compreendidas pela invocação. A capacidade original conserva seus custos, suas condições de uso e suas durações.
~~~~

## R65-03-028

`evocador--ev-complementar` · linha 5582

**Antes**

~~~~text
Você precisa estar consciente e percebê-la. A invocação deve estar ativa, sem Atordoado, compreender sua orientação e cumprir os requisitos da ação e de sua intenção.
~~~~

**Depois**

~~~~text
Você precisa estar consciente e percebê-la. A invocação deve estar ativa, sem Atordoado, compreender sua orientação e cumprir o que a ação e sua intenção exigem.
~~~~

## R65-03-029

`evocador--ev-combinar` · linha 5624

**Antes**

~~~~text
Cada utilização de uma intervenção pode receber um desconto. Ela conserva seus requisitos, demais custos e limite de uso.
~~~~

**Depois**

~~~~text
Cada utilização de uma intervenção pode receber um desconto. Ela conserva suas exigências, os demais custos e o limite de uso.
~~~~

## R65-03-030

`evocador--ev-combinada` · linha 5649

**Antes**

~~~~text
Todas as participantes precisam estar ativas, ser percebidas por você a até 18 m, compreender o comando e estar com **todas as suas básicas da rodada disponíveis**. Uma básica gasta, investida ou perdida por condição impede essa participação. Ter zero básicas disponíveis não cumpre o requisito.
~~~~

**Depois**

~~~~text
Todas as participantes precisam estar ativas, ser percebidas por você a até 18 m, compreender o comando e estar com **todas as suas básicas da rodada disponíveis**. Uma básica gasta, investida ou perdida por condição impede essa participação. Com zero básicas disponíveis, a invocação também fica fora.
~~~~

## R65-03-031

`evocador--ev-combinada` · linha 5655

**Antes**

~~~~text
**Resolva em sequência.** Pague os PE da primeira especial e resolva-a completamente. Depois das respostas que ela provocar, a segunda começa imediatamente: escolha seus alvos, confira seus requisitos e pague os PE e demais custos dela. Cada capacidade conserva seu alcance e suas propriedades.
~~~~

**Depois**

~~~~text
**Resolva em sequência.** Pague os PE da primeira especial e resolva-a completamente. Depois das respostas que ela provocar, a segunda começa imediatamente: escolha seus alvos, confira o que ela exige e pague os PE e demais custos dela. Cada capacidade conserva seu alcance e suas propriedades.
~~~~

## R65-03-032

`evocador--ev-principal-especial` · linha 5712

**Antes**

~~~~text
Depois de resolver a especial, suas respostas e a orientação posterior, ela pode executar imediatamente **uma capacidade básica própria**, usando a segunda oportunidade. Cada capacidade conserva o alcance e os requisitos escritos em sua ficha.
~~~~

**Depois**

~~~~text
Depois de resolver a especial, suas respostas e a orientação posterior, ela pode executar imediatamente **uma capacidade básica própria**, usando a segunda oportunidade. Cada capacidade conserva o alcance e as exigências escritas em sua ficha.
~~~~

## R65-03-033

`evocador--ev-principal-especial` · linha 5728

**Antes**

~~~~text
Anote seus efeitos, requisitos e custos. A básica continua sendo Classe 0, com a escala do nível da entidade. A especial respeita a maior Classe permitida por esse nível. Todo talento concedido por Repertório Ampliado é de **Categoria de Efeito 1**, inclusive nas escolhas dos níveis 16 e 24. Escolha entre os talentos permitidos para entidades em **Criar uma invocação**, cumprindo seus requisitos. As escolhas seguem os procedimentos normais de revisão da ficha.
~~~~

**Depois**

~~~~text
Anote seus efeitos, condições de uso e custos. A básica continua sendo Classe 0, com a escala do nível da entidade. A especial respeita a maior Classe permitida por esse nível. Todo talento concedido por Repertório Ampliado é de **Categoria de Efeito 1**, inclusive nas escolhas dos níveis 16 e 24. Escolha entre os talentos permitidos para entidades em **Criar uma invocação**, cumprindo o que cada talento exige. As escolhas seguem os procedimentos normais de revisão da ficha.
~~~~

## R65-03-034

`evocador--ev-principal-reflexa` · linha 5849

**Antes**

~~~~text
Use a intervenção na sua janela, cumprindo seus requisitos e limites. O efeito e a duração permanecem iguais.
~~~~

**Depois**

~~~~text
Use a intervenção na sua janela, respeitando suas exigências e seus limites. O efeito e a duração permanecem iguais.
~~~~

## R65-03-035

`evocador--ev-parceria-complementar` · linha 5976

**Antes**

~~~~text
O lobo mantém Resposta ao Agressor. Ele usa a básica em Ajudar numa tentativa que possa apoiar pelas regras da ação. Depois, no turno inimigo, você é atingido. Se os requisitos ainda forem cumpridos, o lobo usa a coletiva para executar sua básica ofensiva contra o agressor. A ação de apoio anterior é compatível com essa resposta.
~~~~

**Depois**

~~~~text
O lobo mantém Resposta ao Agressor. Ele usa a básica em Ajudar numa tentativa que possa apoiar pelas regras da ação. Depois, no turno inimigo, você é atingido. Se as exigências ainda forem cumpridas, o lobo usa a coletiva para executar sua básica ofensiva contra o agressor. A ação de apoio anterior é compatível com essa resposta.
~~~~

## R65-03-036

`evocador--ev-parceria-intervencoes` · linha 5990

**Antes**

~~~~text
**Requisitos comuns:** você está consciente e percebe a invocação participante ativa a até **18 m**. Cada uso envolve você e **uma** invocação, que pode ser qualquer uma das suas ativas. A entidade precisa perceber o acontecimento ao qual responde e cumprir os requisitos de sua participação.
~~~~

**Depois**

~~~~text
**Requisitos comuns:** você está consciente e percebe a invocação participante ativa a até **18 m**. Cada uso envolve você e **uma** invocação, que pode ser qualquer uma das suas ativas. A entidade precisa perceber o acontecimento ao qual responde e cumprir as exigências para participar.
~~~~

## R65-03-037

`evocador--ev-parceria-cobrir` · linha 6029

**Antes**

~~~~text
*Exemplo: o lobo ajudou no seu turno e conserva Resposta ao Agressor. Você paga dois pontos para ele cobrir você. Se o ataque ainda acertar, o lobo pode responder pela Reação coletiva, cumprindo os requisitos do aprimoramento.*
~~~~

**Depois**

~~~~text
*Exemplo: o lobo ajudou no seu turno e conserva Resposta ao Agressor. Você paga dois pontos para ele cobrir você. Se o ataque ainda acertar, o lobo pode responder pela Reação coletiva, se cumprir o que o aprimoramento exige.*
~~~~

## R65-03-038

`evocador--ev-parceria-tecnicas` · linha 6047

**Antes**

~~~~text
Escolha a aplicação e seus alvos depois de resolver a especial e confira os requisitos a partir de sua própria posição. Pague os PE e demais custos normais. A invocação conserva os custos e o alcance da especial que executou.
~~~~

**Depois**

~~~~text
Escolha a aplicação e seus alvos depois de resolver a especial e confira as exigências a partir de sua própria posição. Pague os PE e demais custos normais. A invocação conserva os custos e o alcance da especial que executou.
~~~~

## R65-03-039

`evocador--ev-parceria-resposta` · linha 6078

**Antes**

~~~~text
Escolha uma capacidade conhecida que possa afetar o agressor. Confira a Classe de fato utilizada, inclusive após Ampliar, e os requisitos e alcance a partir de quem executa.
~~~~

**Depois**

~~~~text
Escolha uma capacidade conhecida que possa afetar o agressor. Confira a Classe de fato utilizada, inclusive após Ampliar, e use a posição de quem executa para conferir as exigências e o alcance.
~~~~

## R65-03-040

`evocador--ev-parceria-resposta` · linha 6088

**Antes**

~~~~text
**A invocação foi atingida.** No nível 27, sua maior Classe é 7: você pode responder com um feitiço de até **Classe 4**, usando sua Reação pessoal. A disponibilidade da coletiva não é requisito para essa resposta pessoal.
~~~~

**Depois**

~~~~text
**A invocação foi atingida.** No nível 27, sua maior Classe é 7: você pode responder com um feitiço de até **Classe 4**, usando sua Reação pessoal. Essa resposta pessoal pode ser usada mesmo com a coletiva indisponível.
~~~~

## R65-03-041 **Título interno do exemplo para aprovação**

`evocador--ev-parceria-resposta` · linha 6090

**Antes**

~~~~text
**Conservar recursos.** Cobrir o Parceiro por dois pontos preserva as Reações. Se o ataque ainda acertar e os requisitos continuarem satisfeitos, a dupla pode responder pela modalidade correspondente. O uso por combate pertence ao conjunto, mesmo que a beneficiária seja substituída.
~~~~

**Depois**

~~~~text
**Conservar recursos.** Cobrir o Parceiro por dois pontos preserva as Reações. Se o ataque ainda acertar e as exigências continuarem atendidas, a dupla pode responder pela modalidade correspondente. O uso por combate pertence ao conjunto, mesmo que a beneficiária seja substituída.
~~~~

## R65-03-042

`evocador--ev-multiplas-entrada` · linha 6151

**Antes**

~~~~text
Pague o PE de cada entrada ou retorno. Confira a posição e os requisitos de cada entidade.
~~~~

**Depois**

~~~~text
Pague o PE de cada entrada ou retorno. Confira a posição e o que cada entidade exige para entrar ou voltar.
~~~~

## R65-03-043

`evocador--ev-multiplas-entrada` · linha 6153

**Antes**

~~~~text
**Exemplo de Manifestação em Grupo.** A ave ainda tem sua básica, mas o cão já atacou. Você declara duas substituições: a serpente assume o lugar da ave, e o vigia assume o lugar do cão. Paga as duas entradas. Se a serpente cumprir os requisitos de transferência, recebe a básica da ave. O vigia entra sem básica. Cada substituta recebe a orientação da sua troca e conserva o histórico do próprio corpo.
~~~~

**Depois**

~~~~text
**Exemplo de Manifestação em Grupo.** A ave ainda tem sua básica, mas o cão já atacou. Você declara duas substituições: a serpente assume o lugar da ave, e o vigia assume o lugar do cão. Paga as duas entradas. Se a serpente cumprir as exigências da transferência, recebe a básica da ave. O vigia entra sem básica. Cada substituta recebe a orientação da sua troca e conserva o histórico do próprio corpo.
~~~~

## R65-03-044

`evocador--ev-multiplas-conduzir` · linha 6233

**Antes**

~~~~text
A executora usa sua ficha e cumpre os requisitos de percepção, trajeto, Forma e Restrições da capacidade. **Conduzir não dispensa contato nem afasta da executora uma Aura ou aplicação restrita ao próprio corpo.** Toque e Queima-Roupa conservam seus requisitos em relação à executora. Formas como Cone e Linha podem partir da apoiadora quando respeitarem todas as demais exigências. A executora paga sua básica. Você paga a Padrão do comando. Os PE e demais custos seguem o procedimento normal da especial.
~~~~

**Depois**

~~~~text
A executora usa sua ficha e cumpre as exigências de percepção, trajeto, Forma e Restrições da capacidade. **Conduzir não dispensa contato nem afasta da executora uma Aura ou aplicação restrita ao próprio corpo.** Toque e Queima-Roupa conservam as mesmas exigências para a executora. Formas como Cone e Linha podem partir da apoiadora quando respeitarem todas as demais exigências. A executora paga sua básica. Você paga a Padrão do comando. Os PE e demais custos seguem o procedimento normal da especial.
~~~~

## R65-03-045

`evocador--ev-multiplas-formacao` · linha 6303

**Antes**

~~~~text
Pague os **PE normais da entrada ou retorno**. Confira as condições, a posição de chegada e os requisitos dos tipos envolvidos pelo capítulo **Invocações em campo**.
~~~~

**Depois**

~~~~text
Pague os **PE normais da entrada ou retorno**. Confira as condições, a posição de chegada e as exigências dos tipos envolvidos no capítulo **Invocações em campo**.
~~~~

## R65-03-046

`evocador--ev-multiplas-formacao` · linha 6315

**Antes**

~~~~text
Você pode orientá-la com sua Bônus ou comandar uma especial pela Padrão quando cumprir os requisitos, aplicando a orientação posterior normal. As demais entradas feitas nesse turno seguem seus próprios procedimentos.
~~~~

**Depois**

~~~~text
Você pode orientá-la com sua Bônus ou comandar uma especial pela Padrão quando cumprir as exigências de uso, aplicando a orientação posterior normal. As demais entradas feitas nesse turno seguem seus próprios procedimentos.
~~~~

## R65-03-047

`evocador--ev-multiplas-repertorio` · linha 6329

**Antes**

~~~~text
Para cada escolha, acrescente à ficha **uma capacidade básica de Classe 0, uma especial normal ou um talento de Categoria de Efeito 1**. O talento precisa pertencer à lista permitida para entidades em **Criar uma invocação** e cumprir seus requisitos.
~~~~

**Depois**

~~~~text
Para cada escolha, acrescente à ficha **uma capacidade básica de Classe 0, uma especial normal ou um talento de Categoria de Efeito 1**. O talento precisa pertencer à lista permitida para entidades em **Criar uma invocação** e respeitar as exigências do talento.
~~~~

## R65-03-048

`evocador--ev-multiplas-repertorio` · linha 6340

**Antes**

~~~~text
Anote as escolhas na ficha. Ao entrar ou ser substituída, a invocação utiliza esse repertório registrado. A capacidade é executada com suas ações, PE, requisitos e limites próprios.
~~~~

**Depois**

~~~~text
Anote as escolhas na ficha. Ao entrar ou ser substituída, a invocação utiliza esse repertório registrado. A capacidade é executada com suas próprias ações, seus PE, suas exigências e seus limites.
~~~~

## R65-03-049

`incursor--inc-fluidez-avancada` · linha 6511

**Antes**

~~~~text
Quando o mesmo acontecimento permitir Passo Guardado e Reflexo, pode primeiro realizar o movimento e depois resolver o contra-ataque. Mantenha os requisitos de Reflexo: depois de um erro de ataque, o alvo continua sendo o inimigo que errou; depois de um TR Físico bem-sucedido, pode escolher uma criatura hostil ao seu alcance. O ataque ou efeito que provocou a resposta é resolvido antes de ambos.
~~~~

**Depois**

~~~~text
Quando o mesmo acontecimento permitir Passo Guardado e Reflexo, pode primeiro realizar o movimento e depois resolver o contra-ataque. Siga as condições de Reflexo: depois de um erro de ataque, o alvo continua sendo o inimigo que errou; depois de um TR Físico bem-sucedido, pode escolher uma criatura hostil ao seu alcance. O ataque ou efeito que provocou a resposta é resolvido antes de ambos.
~~~~

## R65-03-050

`incursor--inc-ritmo` · linha 6525

**Antes**

~~~~text
Passa a poder percorrer paredes e atravessar espaços de criaturas até o limite do **seu deslocamento completo**, mantendo os demais requisitos. Amplia a travessia permitida; não concede movimento adicional. O novo limite também vale para as modalidades acrescentadas ao Movimento Acrobático pela sua Trilha, como a travessia de líquidos do Pugilista.
~~~~

**Depois**

~~~~text
Passa a poder percorrer paredes e atravessar espaços de criaturas até o limite do **seu deslocamento completo**, respeitando as demais exigências. Amplia a travessia permitida; não concede movimento adicional. O novo limite também vale para as modalidades acrescentadas ao Movimento Acrobático pela sua Trilha, como a travessia de líquidos do Pugilista.
~~~~

## R65-03-051

`incursor--inc-ritmo` · linha 6542

**Antes**

~~~~text
Suas ações e os demais custos e requisitos das habilidades continuam funcionando normalmente.
~~~~

**Depois**

~~~~text
Suas ações e os demais custos e as exigências das habilidades continuam funcionando normalmente.
~~~~

## R65-03-052

`incursor--inc-assassino` · linha 6578

**Antes**

~~~~text
Armas com **Leve** ou **Fineza** estão identificadas no catálogo de Armas. O Volume e a propriedade Oculta não substituem esse requisito.
~~~~

**Depois**

~~~~text
Armas com **Leve** ou **Fineza** estão identificadas no catálogo de Armas. O Volume e a propriedade Oculta não substituem Leve ou Fineza.
~~~~

## R65-03-053

`incursor--inc-cortar` · linha 6646

**Antes**

~~~~text
Se você utilizou **Instante Decisivo naquele ataque**, pode aplicar **Golpe Cirúrgico sem gastar outra Fluidez**, desde que acerte e cumpra todos os requisitos da habilidade.
~~~~

**Depois**

~~~~text
Se você utilizou **Instante Decisivo naquele ataque**, pode aplicar **Golpe Cirúrgico sem gastar outra Fluidez**, desde que acerte e cumpra tudo o que a habilidade exige.
~~~~

## R65-03-054

`incursor--inc-parkour` · linha 6705

**Antes**

~~~~text
Durante seu turno, você pode escolher ou trocar seu **Alvo Estudado sem gastar uma ação**, uma vez por turno, mantendo os requisitos normais de alcance e visão.
~~~~

**Depois**

~~~~text
Durante seu turno, você pode escolher ou trocar seu **Alvo Estudado sem gastar uma ação**, uma vez por turno, respeitando as exigências normais de alcance e visão.
~~~~

## R65-03-055

`incursor--inc-brecha` · linha 6723

**Antes**

~~~~text
Você pode utilizar **Golpe Cirúrgico ou Cortar a Fuga nesse ataque**, desde que possua Fluidez e cumpra os requisitos normais, pagando seus respectivos custos.
~~~~

**Depois**

~~~~text
Você pode utilizar **Golpe Cirúrgico ou Cortar a Fuga nesse ataque**, desde que possua Fluidez e cumpra as exigências normais, pagando seus respectivos custos.
~~~~

## R65-03-056

`incursor--inc-corpo` · linha 6794

**Antes**

~~~~text
Canalizar ou Estímulo Muscular continua sendo acrescentado normalmente, seguindo seus requisitos e impedimentos.
~~~~

**Depois**

~~~~text
Canalizar ou Estímulo Muscular continua sendo acrescentado normalmente, se suas exigências forem cumpridas e nenhum impedimento se aplicar.
~~~~

## R65-03-057

`incursor--inc-base` · linha 6825

**Antes**

~~~~text
- **Enquanto estiver Agarrado por uma criatura:** ela realiza um **TR Físico contra a CD do Pugilista**. **Na falha, você escapa da contenção e pode deixar o agressor Agarrado por você, sem outro teste, desde que cumpra os requisitos normais para agarrá-lo.** No sucesso, ela mantém a contenção e a Fluidez permanece gasta.
~~~~

**Depois**

~~~~text
- **Enquanto estiver Agarrado por uma criatura:** ela realiza um **TR Físico contra a CD do Pugilista**. **Na falha, você escapa da contenção e pode deixar o agressor Agarrado por você, sem outro teste, desde que cumpra o que normalmente precisa para agarrá-lo.** No sucesso, ela mantém a contenção e a Fluidez permanece gasta.
~~~~

## R65-03-058

`incursor--inc-redirecionar` · linha 6932

**Antes**

~~~~text
Para utilizar a habilidade, cumpra os requisitos abaixo:
~~~~

**Depois**

~~~~text
Para usar a habilidade, cumpra as condições abaixo:
~~~~

## R65-03-059

`incursor--inc-malabarista` · linha 6975

**Antes**

~~~~text
Você pode usar **Força ou Destreza no acerto e no dano dos ataques corpo a corpo e de arremesso com armas de uma mão**, escolhendo a cada ataque. Os demais requisitos da arma continuam valendo.
~~~~

**Depois**

~~~~text
Você pode usar **Força ou Destreza no acerto e no dano dos ataques corpo a corpo e de arremesso com armas de uma mão**, escolhendo a cada ataque. As demais exigências da arma continuam valendo.
~~~~

## R65-03-060

`incursor--inc-malabarista` · linha 6987

**Antes**

~~~~text
O segundo ataque precisa ser corpo a corpo ou um arremesso, e nunca um disparo de arma de fogo ou de besta. Pode combinar ataques corpo a corpo e arremessos, usar a mesma arma ou armas diferentes e atacar a mesma criatura ou criaturas diferentes. Cada ataque é resolvido separadamente, com seu dano e seus requisitos normais. Adicionais de dano permanecem sujeitos às próprias regras.
~~~~

**Depois**

~~~~text
O segundo ataque precisa ser corpo a corpo ou um arremesso, e nunca um disparo de arma de fogo ou de besta. Pode combinar ataques corpo a corpo e arremessos, usar a mesma arma ou armas diferentes e atacar a mesma criatura ou criaturas diferentes. Cada ataque é resolvido separadamente, com seu dano e suas exigências normais. Adicionais de dano permanecem sujeitos às próprias regras.
~~~~

## R65-03-061

`incursor--inc-continuacoes` · linha 7028

**Antes**

~~~~text
[Mudar o Destino](#incursor--inc-destino), habilidade de nível 2, permite redirecionar um arremesso que errou contra outra criatura. Essa correção continua sendo parte do ataque corrigido. Depois da correção, considere o alvo final para os requisitos de uma continuação. Fluidez obtida por um acerto só pode ser aproveitada uma vez pelo mesmo acontecimento, segundo o Caminho.
~~~~

**Depois**

~~~~text
[Mudar o Destino](#incursor--inc-destino), habilidade de nível 2, permite redirecionar um arremesso que errou contra outra criatura. Essa correção continua sendo parte do ataque corrigido. Depois da correção, use o alvo final para conferir se pode fazer uma continuação. Fluidez obtida por um acerto só pode ser aproveitada uma vez pelo mesmo acontecimento, segundo o Caminho.
~~~~

## R65-03-062

`incursor--inc-destino` · linha 7054

**Antes**

~~~~text
Essa é uma correção da tentativa que errou: não consome outro ataque disponível, não repete a tentativa contra a mesma criatura e não permite outra correção se a nova rolagem também errar. Use a nova rolagem para determinar acerto e crítico, e resolva o dano normal da arma no acerto. Considere a correção como parte do mesmo ataque para gatilhos que contam ataques realizados; o erro contra o primeiro alvo permanece um erro. A correção tem suas próprias condições de vantagem, desvantagem e cobertura. Efeitos escolhidos antes da rolagem continuam sujeitos aos próprios requisitos contra o novo alvo; efeitos ligados ao resultado do primeiro d20 não são transferidos para o novo resultado.
~~~~

**Depois**

~~~~text
Essa é uma correção da tentativa que errou: não consome outro ataque disponível, não repete a tentativa contra a mesma criatura e não permite outra correção se a nova rolagem também errar. Use a nova rolagem para determinar acerto e crítico, e resolva o dano normal da arma no acerto. Considere a correção como parte do mesmo ataque para gatilhos que contam ataques realizados; o erro contra o primeiro alvo permanece um erro. A correção tem suas próprias condições de vantagem, desvantagem e cobertura. Efeitos escolhidos antes da rolagem continuam sujeitos às próprias exigências contra o novo alvo; efeitos ligados ao resultado do primeiro d20 não são transferidos para o novo resultado.
~~~~

## R65-03-063

`incursor--inc-finta` · linha 7094

**Antes**

~~~~text
Os 6 PE substituem o custo normal de 4 PE de Trajetória de Retorno. Esta execução consome a mesma utilização de Lançamento Cruzado e mantém o limite de uma continuação por turno, seus requisitos de arma, o ricochete em uma superfície sólida, o percurso livre de até 6 m e a nova rolagem de ataque. Não concede outra continuação naquele turno.
~~~~

**Depois**

~~~~text
Os 6 PE substituem o custo normal de 4 PE de Trajetória de Retorno. Esta execução consome a mesma utilização de Lançamento Cruzado e mantém o limite de uma continuação por turno, as exigências de arma, o ricochete em uma superfície sólida, o percurso livre de até 6 m e a nova rolagem de ataque. Não concede outra continuação naquele turno.
~~~~

## R65-03-064

`incursor--inc-finta` · linha 7112

**Antes**

~~~~text
O limite passa a ser **uma recuperação entre o começo de um turno seu e o começo do próximo**. Se já recuperou uma arma no seu turno, essa utilização não fica disponível novamente antes do próximo começo de turno. Mantém alcance de 6 m, caminho livre, mão disponível e demais requisitos de recuperação.
~~~~

**Depois**

~~~~text
O limite passa a ser **uma recuperação entre o começo de um turno seu e o começo do próximo**. Se já recuperou uma arma no seu turno, essa utilização não fica disponível novamente antes do próximo começo de turno. Mantém alcance de 6 m, caminho livre, mão disponível e demais exigências para recuperar a arma.
~~~~

## R65-03-065

`incursor--inc-perfeita` · linha 7137

**Antes**

~~~~text
Ganhos de Fluidez pelos acertos seguem os limites normais do Caminho, sem novas obtenções extras. Manejo Contínuo pode recuperar a arma depois do último ataque, se estiver disponível e a arma cumprir seus requisitos. A execução não garante retorno à mão.
~~~~

**Depois**

~~~~text
Ganhos de Fluidez pelos acertos seguem os limites normais do Caminho, sem novas obtenções extras. Manejo Contínuo pode recuperar a arma depois do último ataque, se estiver disponível e a arma atender às exigências da recuperação. A execução não garante retorno à mão.
~~~~
