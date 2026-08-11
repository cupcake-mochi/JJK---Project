# Vulnerável: o preço tá certo?

**Resposta curta: quase. Parado e Gesto passam no teste de dominância um contra o outro — mas Vulnerável, do jeito que está escrita, não passa contra os dois pelo mesmo preço. Ela dói mais na cena comum do seu jogo (mais de um inimigo, que é a regra em luta shounen, não a exceção), e o motivo não é o desconto estar errado — é o alcance da regra estar maior que o das outras duas.**

Abaixo o porquê, rodando os testes na ordem que a gente usa pra criticar mecânica existente: dominância, bônus automático, filtro de multi-mestre, e só no fim uma opinião — marcada como opinião.

## O teste de dominância

As três competem pelo mesmo orçamento (todas devolvem metade do Grau, arredondado pra cima), então cabe perguntar, par a par: existe uma cena em que eu escolheria A no lugar de B?

**Parado vs. Gesto — passa.** Um conjurador que luta parado no mesmo lugar não se importa de pagar Parado; um lutador com as duas mãos ocupadas numa arma, ou numa cena de infiltração em que falar alto entrega a posição do grupo, não pode pagar Gesto de jeito nenhum. Cada uma dói mais numa configuração diferente de personagem e de cena, nenhuma contém a outra — é exatamente o tipo de "troca dor por dor" que o teste deixa passar. Vale um olho, não uma correção agora: as duas podem sair quase de graça pra uma build otimizada pra evitar exatamente aquele custo (o conjurador-torre que nunca precisa se mover; o desarmado que nunca precisa de silêncio). É um risco menor nas duas, secundário perto do que vem a seguir.

**Parado / Gesto vs. Vulnerável — não passa.** A diferença não é de intensidade, é de forma:

- Parado e Gesto custam algo **contido dentro do seu próprio turno**. O pior caso de cada uma é você não conseguir agir daquele jeito específico agora. O custo nunca sai da sua ação e vira problema decidido por outra pessoa.
- Vulnerável custa algo que **sai do seu turno e entra no dos inimigos**: "até o fim do seu próximo turno" cobre o resto da rodada atual, a rodada inteira do grupo inimigo, e ainda o seu próximo turno. E "ataques contra você" não é um ataque — é qualquer um que agir contra você nessa janela toda.

Isso faz o preço de Vulnerável deixar de ser fixo: ele escala com quantos inimigos o mestre pôs na cena, coisa que Parado e Gesto nunca fazem. Contra um oponente só, o custo pode ser pequeno. Contra a mobzada de quatro ou cinco que é padrão em combate shounen, você está multiplicando "vantagem" — que o próprio material de vocês já registra como valendo mais ou menos um +5 (um bônus grande disfarçado de mecânica simples) e como algo que **"empilha fácil"** (`references/matematica-de-dado.md`) — por cada criatura que ainda vai agir antes de você jogar de novo. Perder o movimento não faz isso: custa o mesmo não importa se tem um inimigo ou dez.

Rode o teste de novo com essa lente: existe uma cena em que eu prefiro pagar Vulnerável a pagar Parado, pelo mesmo reembolso? Só em cenas marginais — golpe de misericórdia sem mais ninguém por perto, inimigo fraco o bastante pra vantagem quase não mudar a chance dele de acertar. Existe a cena oposta, em que prefiro Parado? A maioria das lutas com mais de um oponente — ou seja, o normal do gênero que vocês escolheram. Quando a maioria das cenas empurra pra um lado e só a exceção pro outro, a opção mais arriscada na prática está perto de virar peso morto no catálogo: ninguém que entende o risco escolhe ela por razão mecânica, e quem escolhe sem entender leva um susto que as outras duas nunca dão.

## O teste do bônus automático

Não é bem esse o defeito aqui. Vulnerável não é um bônus de graça — ela quase sempre cobra alguma coisa em combate de verdade, o que por si só está certo. O problema é o espelho do automático: o **quanto** ela cobra não depende de nenhuma escolha do jogador (arma, build, se ele precisava se mover), depende só de quantos inimigos o mestre colocou na cena naquele dia. Isso empurra o problema direto pro próximo teste.

## O filtro do multi-mestre

Esse é o ponto mais forte contra a regra como está. O pitch do projeto fecha assim: quando houver dúvida entre "elegante" e "arbitrável por estranho", o projeto escolhe arbitrável. Parado e Gesto passam fácil nisso — dois mestres olhando a mesma cena concordam sobre se o personagem se moveu ou se as mãos estavam livres, sem depender de julgamento. Vulnerável também é uma regra clara, não discricionária, nesse sentido estrito. Mas o **custo real** que ela produz na mesa depende inteiramente de uma decisão que é do mestre, não do sistema: quantos inimigos ele decidiu colocar na cena e quantos deles agem antes do seu próximo turno. Duas mesas aplicando a regra exatamente como está escrita ainda assim entregam experiências bem diferentes pra quem pagou o mesmo preço — que é precisamente o tipo de inconsistência entre mesas que o server foi desenhado pra evitar.

Tem também uma borda que vale fechar por escrito, já que o projeto decidiu nunca deixar regra discricionária: o que acontece se o seu próximo turno for pulado — atordoado, incapacitado, isolado da cena? "Até o fim do seu próximo turno" fica sem resposta exatamente quando isso acontece. Vale escrever explicitamente que a janela fecha no primeiro turno que seria seu depois do atual, jogável ou não — senão um personagem incapacitado fica "vulnerável" indefinidamente por acidente de regra, e dois mestres vão resolver isso de dois jeitos diferentes.

## O conserto (o menor que resolve)

O problema não é o preço em si — metade do Grau, arredondado pra cima, continua fazendo sentido como reembolso. O problema é o alcance. A dominância desaparece se Vulnerável for limitada a **um** evento em vez de uma janela aberta pra qualquer atacante:

> **Vulnerável.** O próximo ataque contra você antes do fim do seu próximo turno tem vantagem.

Isso mantém a sensação que vocês querem — "abri a guarda, e isso pode custar caro daqui a pouco" — sem que o custo real multiplique pelo número de inimigos na cena. Continua valendo metade do Grau como as outras duas, porque agora o pior caso dela é do mesmo tamanho que o pior caso delas: um evento só e contido, não uma sequência que cresce junto com o encontro.

Se vocês preferem manter o alcance largo (vantagem contra qualquer ataque, na janela toda) porque a dramaticidade de "abrir a guarda de vez" vale mais que a simetria de preço, a saída é subir o preço só dela — mas isso sozinho não resolve a parte de multi-mestre, porque duas mesas ainda vão sentir custos bem diferentes dependendo de quantos inimigos apareceram naquele dia. Quem for por esse caminho devia somar um teto explícito ("no máximo dois ataques se beneficiam disso", por exemplo) ao preço mais alto, em vez de confiar só no número pra resolver um problema de variância.

## Uma opinião, marcada como opinião

Prefiro a versão de ataque único. Ela devolve a mesma sensação de risco — ficar exposto até conseguir agir de novo — sem que o custo real dependa de quantos inimigos o mestre daquela mesa especificamente gosta de colocar em cena. E fecha limpo com Parado e Gesto: as três voltam a ser opções que doem de formas diferentes pelo mesmo preço, que era o objetivo de ter três desvantagens em vez de uma só.
