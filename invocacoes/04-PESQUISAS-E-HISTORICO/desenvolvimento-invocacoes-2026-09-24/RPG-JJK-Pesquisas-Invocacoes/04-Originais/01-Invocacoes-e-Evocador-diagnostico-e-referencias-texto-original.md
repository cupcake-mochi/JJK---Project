# Invocações e Evocador — onde o redesenho precisa começar

## Diagnóstico do que existe hoje

Depois de passar pelo repositório atual e comparar suas regras com sistemas que resolveram fantasias parecidas de maneiras muito diferentes, minha conclusão é bastante firme:

> **Não devemos começar reescrevendo o Evocador. Também não devemos começar criando uma lista nova de poderes para invocações.**
>
> **A primeira coisa a reconstruir é o sistema-base de Invocações, especialmente a relação entre repertório, quantidade em campo e quantidade de ações que essas invocações conseguem gerar.**

O Evocador atual não é a origem do problema; ele é, em boa parte, **uma consequência de um sistema de invocações que nunca definiu os seus próprios limites fundamentais**.

O próprio repositório contém sinais claros disso.

O manual diz que quem recebe uma invocação é quem possui uma das três Trilhas do Evocador, mas, na mesma explicação, afirma que as regras de invocação não dependem de ser Evocador e poderiam ser usadas por qualquer ficha que obtivesse uma invocação por outra fonte. O problema é que essa outra fonte praticamente não existe. Na prática, o subsistema foi escrito como universal e implementado como exclusivo. (`sistema/05-material/livro/manual/60-invocacoes.md`, linhas 3–5.)

Há outro ponto ainda mais importante: os documentos de desenvolvimento **já identificaram explicitamente que não existe um limite de invocações em campo**. Na época, isso foi deixado em aberto porque nenhuma opção concedia corpos adicionais fora das Trilhas. O texto diz que, se algum dia existisse outra fonte de invocações, esse limite passaria a ser necessário. Esse “algum dia” chegou justamente agora. (`sistema/03-mecanica/15-invocacoes.md`, linhas 501–503.)

Hoje, o sistema tenta se proteger de múltiplas criaturas por dois mecanismos: comandar custa uma Ação Padrão, e o dano da “Rotina” é repartido entre os corpos. (`sistema/05-material/livro/manual/60-invocacoes.md`, linhas 7–14 e 187–208.) Isso controla **parte do dano**, mas não controla adequadamente o valor de possuir mais corpos.

Três invocações podem ocupar três posições, bloquear três espaços, enxergar três lugares, carregar três coisas, ameaçar três regiões, receber ataques diferentes, explorar, cercar, interagir com objetos e combinar habilidades. Mesmo que dividam exatamente o mesmo dano, **três corpos não equivalem a um corpo**.

Esse é, para mim, o maior problema estrutural do sistema atual.

### O Matilha mostra exatamente onde o modelo quebrou

A Matilha atual diz representar cinco corpos, mas coloca os cinco na mesma ficha, na mesma barra de vida e numa lógica de dano repartido. (`sistema/05-material/livro/manual/60-invocacoes.md`, linhas 70–94.)

Isso resolve algumas contas, mas transforma a fantasia de “tenho várias invocações” em algo muito próximo de:

> **“Tenho uma criatura grande que visualmente está espalhada por cinco miniaturas.”**

Não é o que você quer para o terceiro estilo.

O conceito que você descreveu é muito mais interessante: **várias invocações verdadeiramente diferentes**, que podem possuir funções, personalidades, formas, habilidades e relações umas com as outras. Geto é uma referência muito melhor para isso do que uma “matilha” de cinco cópias mecanicamente idênticas.

Isso também mostra por que eu não tentaria consertar Matilha. **Ela está respondendo a uma pergunta que não queremos mais fazer.**

### O Evocador atual praticamente não possui uma mecânica central

O Caminho começa com Sintonia, que escolhe entre crítico melhor, mais vida ou CD maior; depois Coleira melhora treinamento e acerto; Escudo de Osso permite que a invocação receba um ataque por você; e Segundo Corpo facilita uma manifestação uma vez por descanso. (`sistema/05-material/livro/manual/35-caminhos-e-trilhas.md`, linhas 512–547.)

Isso é funcional como conjunto de bônus, mas não responde:

> **“O que eu faço, rodada após rodada, que faz de mim um Evocador?”**

Essa é justamente uma diferença importante em relação aos Caminhos que acabamos de reconstruir.

O Vanguarda tem sua Sequência. O Emanador altera suas aplicações. O Guia abre oportunidades. O Bastião trabalha em torno da sua presença e resistência.

O Evocador atual essencialmente diz:

> “Você possui uma criatura e ela ganha números melhores.”

É pouco para uma identidade de Caminho.

E há uma questão ainda mais profunda: **qualquer personagem deveria poder ter uma invocação; o Evocador deveria ser o especialista em invocar.**

Uma arma não precisa ser exclusiva da Vanguarda para a Vanguarda ser o especialista em armas. Um feitiço não precisa ser exclusivo do Emanador para o Emanador ser o especialista em manipular sua técnica.

Pela mesma lógica:

> **Uma invocação não deveria precisar ser exclusiva do Evocador para que o Evocador tenha uma identidade forte.**
>
> Na realidade, tornar invocações universais provavelmente deixa o Evocador mais definido, não menos.

Ele deixa de ser **“o Caminho que desbloqueia o subsistema”** e passa a ser **“o Caminho que domina esse subsistema”**.

Essa distinção aparece de maneira muito útil em Pathfinder 2e: um personagem que entra no arquétipo de Summoner pode obter um eidolon, mas sua ligação é deliberadamente mais limitada; ele não recebe ferramentas centrais de coordenação como as ações de tandem do Summoner completo. Ou seja, **acesso ao companheiro e domínio do companheiro são coisas diferentes**. citeturn21view1

Minha leitura do repositório, portanto, é:

| Questão | Situação atual |
|---|---|
| **Quem pode ter invocação?** | Na prática, somente Evocador. |
| **Quantas pode conhecer/possuir?** | Não existe uma estrutura geral. |
| **Quantas pode ter manifestadas?** | Não existe limite universal. |
| **Quantas podem agir?** | A Ação Padrão limita comandos, mas não presença. |
| **Quanto vale um corpo adicional?** | O dano tenta ser repartido; o restante do valor não é medido. |
| **O que diferencia a origem da invocação?** | Principalmente vida e descrição. |
| **O que o Evocador domina?** | Majoritariamente números da criatura. |
| **Como as três Trilhas diferem?** | Sobretudo pela quantidade de corpos e pelo modo de atacar. |
| **Como representar Geto, Megumi e uma criatura singular?** | O sistema atual força fantasias muito diferentes para dentro da mesma estrutura. |

Por isso concordo com a premissa mais forte da sua mensagem:

**vale mais reconstruir do que remendar.**

## O que outros sistemas descobriram sobre invocadores

Existe um padrão muito consistente nas referências pesquisadas:

> **O problema mais perigoso de um invocador não é o dano da criatura. É transformar um jogador em vários personagens completos ao mesmo tempo.**

Sistemas diferentes resolvem isso de formas diferentes, e essas soluções são extremamente úteis para nós.

### Pathfinder mostra dois extremos muito úteis

O Pathfinder original é uma excelente referência para **customização**.

O eidolon recebe uma reserva de Evolution Points e compra modificações como garras, mordida, escalada, voo, agarrão, empurrão, armadura natural e outras capacidades. Algumas possuem requisitos de forma ou nível. O sistema também separa esse orçamento de limites próprios para coisas especialmente perigosas, como quantidade de ataques naturais. citeturn20view2

Esse detalhe é importante.

O Pathfinder não parte da ideia:

> “Se tudo custa pontos, então pontos resolvem qualquer problema.”

Ele reconhece que existem eixos tão poderosos que **precisam de um limite próprio além do orçamento**.

Essa é uma lição que eu levaria diretamente para RPG-JJK.

Podemos ter uma invocação completamente customizável e, ao mesmo tempo, dizer que certas coisas possuem seus próprios limites:

**ações adicionais, quantidade de corpos, reações, efeitos de controle muito fortes, voo, ataques extras, autonomia, alcance remoto e talvez técnicas próprias** não precisam depender somente de “quanto custam em pontos”.

O Pathfinder 2e segue por outra direção e é provavelmente a melhor referência para a Trilha singular. O Summoner e o eidolon são duas criaturas no mapa, mas **dividem as ações do personagem e até a penalidade de ataques múltiplos**. A própria regra deixa explícito que o eidolon não é um minion comum: os dois coordenam a mesma economia de ações. citeturn21view0

Esse é um princípio extremamente poderoso:

> **Dois corpos não precisam significar dois turnos.**

É precisamente a distinção que nosso sistema ainda não fez.

O modelo não precisa ser copiado literalmente — eu não acho que RPG-JJK deva necessariamente compartilhar vida entre personagem e invocação, por exemplo —, mas a solução conceitual é excelente.

### D&D mostra o que acontece quando quantidade vira quantidade de ações

O antigo *Conjure Animals* podia criar uma, duas, quatro ou oito criaturas. Uma análise publicada pelo próprio D&D Beyond destaca exatamente o problema: as versões com mais criaturas tendiam a ser muito fortes por causa da economia de ações, geravam muitas tentativas por rodada e podiam prejudicar a experiência da mesa. citeturn21view2

Isso é especialmente relevante porque o problema não era só:

> “oito lobos causam dano demais.”

Era também:

> “oito lobos fazem coisas demais.”

Nas regras atuais de D&D, *Conjure Animals* foi redesenhado para representar um conjunto espectral como um único efeito, em vez de entregar ao jogador até oito fichas completas independentes. É uma solução bastante abstrata e provavelmente abstrata demais para o que queremos aqui, mas a mudança é um bom sinal da pressão que muitos corpos independentes exercem sobre um jogo de mesa. citeturn20view4turn21view2

**Eu não copiaria a solução moderna do D&D.** Você explicitamente quer que as invocações continuem sendo criaturas customizadas e, principalmente no estilo Geto, quer que elas sejam diferentes.

Mas copiaria o diagnóstico:

> **Não podemos permitir que “mais invocações” signifique automaticamente “mais turnos completos”.**

### Draw Steel abraça a fantasia de exército, mas constrói regras específicas para isso

A apresentação oficial do Summoner de *Draw Steel* é praticamente o extremo oposto de Pathfinder 2e: sua identidade é literalmente **“You Are The Armada”**. O personagem invoca minions para ocupar inimigos, apoiar aliados, segurar posições e preparar contra-ataques. citeturn21view4

O interessante é que o sistema não trata essa quantidade como algo gratuito em termos de complexidade. A documentação atual classifica o Summoner como uma **“master class”**, recomendada para pessoas que já conhecem o jogo. citeturn21view5

Ele também introduz regras próprias de quantidade, agrupamento e administração das criaturas; fora de combate, por exemplo, existe inclusive uma quantidade específica de minions permitida e tarefas simples como reconhecimento, entrega de mensagens e transporte são tratadas separadamente. citeturn21view6

A lição para nós não é “faça oito invocações”.

É:

> **Se uma Trilha vai realmente controlar várias unidades, ela precisa ter uma interface mecânica feita para controlar várias unidades.**

Não podemos pegar uma ficha projetada para uma criatura, multiplicá-la por quatro e esperar que o turno continue saudável.

Isso será crucial para a terceira Trilha.

### Girls' Frontline mostra que comandante não significa “mais ataques”

*Girls' Frontline* trabalha a fantasia de comandante por mobilização, formação, linha de frente, linha de trás, posicionamento e uso de várias equipes. citeturn21view7

*Girls' Frontline 2* dá ainda mais destaque ao campo: cobertura, terreno, mecanismos e personagens diferentes compondo a equipe do Comandante. citeturn21view8

É uma referência muito útil para o Evocador múltiplo porque mostra que:

> **A satisfação de comandar um grupo vem tanto de montar o grupo e escolher quem está onde quanto de mandar todo mundo atacar.**

Isso abre possibilidades muito melhores para a futura Trilha múltipla.

Ela pode ser satisfatória porque uma invocação segura posição, outra prepara uma condição, uma terceira explora uma abertura e outra é chamada para substituir uma que saiu.

Não precisamos dar quatro ataques independentes para o jogador sentir que possui quatro invocações.

### Diablo mostra que “build de invocador” não precisa significar uma única coisa

O Necromancer atual de *Diablo IV* continua explorando várias formas de expressar a fantasia: muitos esqueletos, comando de alvos, magos, guerreiros, golem grande e a possibilidade de sacrificar ou utilizar os minions de outras maneiras. A revisão de 2026 ampliou especialmente o lado de “general dos mortos”, incluindo comando direto e mais espaço para configurações especializadas. citeturn20view10

Um ARPG pode suportar quantidades muito maiores porque o computador resolve os corpos, movimentos e ataques em tempo real. Portanto, **28 esqueletos não é uma meta transferível para RPG-JJK**.

O que é transferível é outra coisa:

> **O jogador de invocador gosta de decidir que tipo de invocador está construindo.**

Grande criatura única, tropas menores, tanque, dano, utilidade, sacrifício, especialização, composição.

Isso reforça sua decisão de manter **três Trilhas que mudam a relação do personagem com suas criaturas**, em vez de fazer três variações numéricas da mesma invocação.

## O que a temática de Jujutsu Kaisen pede do sistema

Aqui está, para mim, a descoberta conceitual mais importante da pesquisa:

> **Jujutsu Kaisen não possui uma única fantasia de “invocador”.**
>
> Ele possui várias relações diferentes entre feiticeiro e entidade.

Por isso, um sistema em que toda invocação nasce do mesmo procedimento, obedece da mesma maneira, morre da mesma maneira e é utilizada da mesma forma tende inevitavelmente a achatar a obra.

Mesmo referências muito conhecidas ocupam extremos diferentes. Megumi é associado a vários shikigami com capacidades distintas; Geto trabalha com um repertório de espíritos amaldiçoados que controla; Rika representa uma relação muito mais próxima de uma presença singular extremamente importante ligada a Yuta. citeturn21view9turn20view12turn20view13

Não trataria essas referências como modelos que precisamos copiar regra por regra. Mas elas mostram que suas três Trilhas propostas **não são arbitrárias**. Elas refletem três fantasias realmente diferentes.

Eu resumiria as identidades assim:

| Trilha conceitual | Relação | Frase de identidade |
|---|---|---|
| **Singular** | Uma criatura muito importante assume grande parte do combate e da proteção. | **“Minha invocação luta por mim.”** |
| **Dueto** | Personagem e uma ou duas invocações formam combinações. | **“Eu luto com minhas invocações.”** |
| **Múltiplas** | O repertório de criaturas é a própria maneira de combater. | **“Eu luto através das minhas invocações.”** |

Essa divisão é **muito mais forte** que Servo / Matilha / Coro.

Não necessariamente precisamos descartar esses nomes — nomes vêm depois —, mas eu descartaria a arquitetura atual das Trilhas.

### A singular não deve ser apenas “a mesma invocação com mais pontos”

Isso é importante.

O Servo atual ganha orçamento maior, vida maior e efeitos que o deixam mais resistente. Isso produz uma criatura numericamente maior.

Mas a fantasia singular deveria mudar a **relação** entre personagem e entidade.

Ela pode, futuramente, desenvolver coisas como:

- maior autonomia;
- interceptar perigos;
- agir mesmo quando o Evocador está ocupado;
- compartilhar percepção ou posição;
- proteger o usuário sem precisar receber ordens constantes;
- transformar sua presença numa espécie de segundo corpo;
- receber uma parcela muito maior do orçamento de customização;
- aprofundar uma mesma criatura em vez de aumentar repertório.

Não estou propondo essas habilidades como regras agora. O importante é o critério:

> **Ela não é “o caminho com uma invocação porque só pode ter uma”. Ela escolhe investir tudo em uma relação.**

### A intermediária deve ser sobre combinação

Esta é provavelmente a que mais lembra o combate de Megumi como referência visual.

Ela não deveria ser simplesmente:

> “Você tem dois pets.”

O seu jogo deveria ser:

> **eu faço algo → minha invocação aproveita → ela me reposiciona → eu aproveito → troco qual criatura está ativa → combinamos efeitos.**

A diferença para a singular é que o personagem continua sendo uma peça ofensiva importante.

A diferença para a múltipla é que ele não está administrando um repertório como principal linguagem de combate.

O centro da Trilha é **coordenação entre corpos**.

### A múltipla precisa ser um repertório, não uma horda

Aqui eu faria uma distinção muito firme.

**Geto não deveria ser representado pela atual Matilha.**

O interessante nessa fantasia não é “cinco bichos iguais atacam juntos”.

É possuir **muitas respostas diferentes**.

Uma criatura voadora. Uma que imobiliza. Uma defensiva. Outra estranha, especializada em determinado efeito. Uma que é dispensável. Uma criatura rara que o jogador guardou porque gosta dela.

Esse conceito combina muito bem com a distinção entre **repertório** e **campo** que proponho adiante.

O personagem pode, por exemplo, possuir um repertório grande sem jamais colocar todas as criaturas simultaneamente no mapa.

É exatamente o tipo de separação que jogos de comandante fazem: *Girls' Frontline* distingue seu conjunto de personagens da formação que está efetivamente participando de uma operação. citeturn21view7turn21view8

Isso preserva a fantasia de:

> **“Eu coleciono/domino muitas criaturas.”**

sem exigir:

> **“Eu coloco quinze fichas na iniciativa.”**

Há ainda outro motivo para reconstruir o ciclo de vida das criaturas. O documento atual aplica uma regra geral de destruição permanente e a justifica a partir de shikigami que não retornam após serem destruídos. (`sistema/03-mecanica/15-invocacoes.md`, linhas 554–563.)

Isso pode funcionar para **uma determinada origem ou técnica**, mas é muito amplo para um subsistema que quer representar talismãs, corpos amaldiçoados, shikigami, maldições domadas e outras formas futuras de invocação.

O próprio documento de desenvolvimento reconhece que existem entidades como Rika e Mahoraga que não se encaixam perfeitamente na hipótese de “a invocação simplesmente obedece ao portador”. (`sistema/03-mecanica/15-invocacoes.md`, linhas 495–503.)

Portanto, futuramente, **origem, obediência, perda e recuperação provavelmente precisarão ser módulos distintos**.

Mas ainda não é aí que eu começaria.

## A arquitetura que falta às Invocações

Eu construiria o novo sistema em torno de **quatro valores diferentes**, em vez de perguntar apenas “quantas invocações você tem?”.

### Repertório

> **Quantas invocações diferentes você possui e pode escolher.**

Isso representa coleção, aprendizado, domesticação, construção ou vínculos.

É um recurso de **opções**, não de economia de ações.

Uma pessoa poderia conhecer uma criatura e outra possuir dez sem que isso significasse automaticamente que a segunda coloca dez corpos no combate.

Essa separação é essencial para uma futura fantasia semelhante à de Geto.

### Capacidade de Campo

> **Quanto do seu repertório pode estar manifestado ao mesmo tempo.**

Eu não faria isso simplesmente como:

> “máximo de três invocações.”

Minha recomendação é que as próprias invocações possuam algum tipo de **peso de manifestação**.

Nome provisório:

**Presença**, **Carga de Invocação**, **Peso de Vínculo** ou algo semelhante.

Uma entidade grande e extremamente poderosa poderia consumir uma parcela enorme dessa capacidade; criaturas menores consumiriam menos.

Conceitualmente:

> **Capacidade de Campo ≥ soma da Presença das invocações manifestadas.**

Sem valores ainda.

Isso resolve uma coisa importantíssima: **as três Trilhas podem utilizar o mesmo sistema**.

A singular investe quase toda sua capacidade numa criatura.

A intermediária distribui entre uma ou duas.

A múltipla consegue distribuir entre mais criaturas.

Não precisamos criar três subsistemas incompatíveis.

Também evitaria, pelo menos inicialmente, deixar essa capacidade crescer diretamente com cada ponto de Inteligência ou Essência. **Quantidade de corpos é um eixo poderoso demais para um único ponto de atributo eventualmente virar “ganhe outra criatura no mapa”.** É mais seguro que o crescimento principal venha de nível, Caminho e Trilha; o atributo pode participar de CD, características, alcance ou outras partes da invocação.

Essa é uma recomendação de design, não algo que os sistemas pesquisados imponham.

### Capacidade de Comando

> **Quantas coisas relevantes suas invocações conseguem fazer numa rodada.**

Esta é, possivelmente, **a regra mais importante de todo o redesenho**.

Quantidade em campo e quantidade de ações precisam ser números diferentes.

Imagine:

- quatro criaturas em campo;
- somente uma ou duas recebem ordens ofensivas relevantes naquele turno;
- as outras continuam ocupando posições e mantendo efeitos, mas não geram quatro rotinas completas.

Agora é possível ter visualmente uma coleção sem quebrar a economia de ações.

Pathfinder 2e resolve sua dupla compartilhando ações entre Summoner e eidolon. citeturn21view0

Draw Steel cria uma arquitetura própria para administrar grupos. citeturn21view4turn21view5

D&D fornece o contraexemplo de por que simplesmente multiplicar criaturas independentes é problemático. citeturn21view2

Nosso sistema não precisa copiar nenhum deles. Só precisa absorver o princípio:

> **corpos e ações são recursos diferentes.**

Isso também significa que eu aposentaria a atual regra de:

> “a Rotina é uma só e é dividida por todos os corpos”

como **regra principal de funcionamento para o jogador**.

Ela ainda pode ser extremamente útil **nos bastidores para validar dano**.

Mas é ruim como principal mecanismo do subsistema porque ela tenta solucionar três problemas diferentes — quantidade, ação e dano — usando apenas o dano.

Eu prefiro:

**a economia de ações controla quanto o grupo consegue fazer; depois calibramos quanto cada ação pode causar.**

Isso é mais robusto.

### Vínculo e autonomia

> **O que uma invocação consegue fazer sem uma ordem direta, e até onde a relação funciona.**

Hoje existe uma regra simples: até 18 m pode receber comando; fora disso fica parada até voltar ao alcance. (`sistema/05-material/livro/manual/60-invocacoes.md`, linhas 7–14.)

Isso é fácil de administrar, mas reduz bastante fantasias como batedores, mensageiros e criaturas independentes — apesar de o próprio capítulo dizer que, fora de combate, invocações podem vigiar, explorar, carregar e realizar tarefas. (`sistema/05-material/livro/manual/60-invocacoes.md`, linhas 16–18.)

No novo sistema, eu trataria **autonomia** como um eixo próprio.

Uma invocação pode talvez:

- seguir você automaticamente;
- defender-se;
- manter posição;
- executar uma ordem simples já recebida;
- possuir ou não iniciativa própria;
- receber comandos a determinada distância;
- continuar uma tarefa fora desse alcance;
- agir independentemente em casos especiais.

Novamente, ainda não precisamos decidir cada regra.

Mas precisamos **reservar um espaço mecânico para isso**, porque a singular, a intermediária e a múltipla provavelmente vão querer autonomia em graus diferentes.

### A estrutura completa

Assim, antes mesmo de definir dano ou vida, uma ficha de personagem poderia conceitualmente possuir:

| Valor | Pergunta respondida |
|---|---|
| **Repertório** | Quais invocações eu tenho? |
| **Capacidade de Campo** | Quais delas podem estar manifestadas juntas? |
| **Presença da Invocação** | Quanto espaço mecânico essa criatura ocupa? |
| **Capacidade de Comando** | Quantas delas podem produzir ações relevantes agora? |
| **Vínculo** | Até onde e de que forma consigo coordená-las? |
| **Autonomia** | O que elas fazem sem receber uma nova ordem? |

**Isso é o núcleo que está faltando hoje.**

E é também por isso que eu não começaria definindo “o Evocador começa com três invocações”.

Ainda não sabemos o que significa **ter** três invocações.

Conhecer três?

Poder escolher entre três?

Manifestar três?

Comandar três?

Atacar com três?

Essas são cinco coisas diferentes.

## O que vale salvar e o que eu reconstruiria

Você disse que somente duas coisas são obrigatórias: customização completa e as três fantasias de Trilha.

**Eu concordo que quase todo o resto pode voltar para a mesa de projeto.**

Ainda assim, há algumas ideias do sistema atual que considero boas o bastante para servirem como matéria-prima — não necessariamente como regras que devem sobreviver sem mudanças.

### A customização deve sobreviver, mas ser reconstruída

A divisão atual entre **Traços** e **Comandos** é conceitualmente boa.

> Traço = algo que a criatura é.  
> Comando = algo que ela faz quando recebe uma ordem.

Isso é uma gramática excelente para um sistema de construção. (`sistema/05-material/livro/manual/60-invocacoes.md`, linhas 131–138.)

Eu provavelmente preservaria **a ideia**, não o catálogo nem os preços atuais.

Também preservaria a existência de criação personalizada. Hoje o sistema já permite propor Traços e Comandos novos e usa os custos existentes como referência. (`sistema/05-material/livro/manual/60-invocacoes.md`, linhas 231–253.)

Isso combina diretamente com sua exigência de invocações completamente customizáveis.

Mas eu ampliaria o modelo para algo mais próximo de:

> **Origem → Corpo/Função → Traços → Ações/Comandos → particularidades.**

O Pathfinder original mostra uma boa razão para fazer isso: uma reserva de pontos é excelente para liberdade, mas modificações diferentes podem exigir formas, níveis e limites específicos. citeturn20view2

### Os quatro tipos atuais são muito rasos

Hoje:

- talismã / corpo amaldiçoado;
- técnica;
- maldição domada;

mudam principalmente a base de vida e a descrição da origem. (`sistema/05-material/livro/manual/60-invocacoes.md`, linhas 53–96.)

Para algo tão importante narrativamente, isso é pouco.

Eu não transformaria cada origem numa classe diferente de invocação, mas gostaria que futuramente **Origem respondesse questões de ficção e ciclo de vida**, como:

| Origem | Perguntas que pode responder |
|---|---|
| **Técnica / shikigami** | Como é formado? Pode ser reconstruído? Sua perda transfere algo? |
| **Maldição domada** | Como é adquirida? Ela é realmente obediente? Pode ser substituída? |
| **Talismã** | O que acontece com o objeto? Pode ser preparado novamente? |
| **Corpo amaldiçoado** | Precisa de um corpo físico? Pode ser consertado? |
| **Outras futuras** | Que regra distingue essa relação? |

Não estou recomendando essas respostas específicas ainda.

Estou recomendando que **“tipo” deixe de significar praticamente apenas “+1 de vida base”**.

### Vida e atributos precisam esperar

Eu não salvaria ainda o modelo atual de:

> nove pontos próprios, cinco atributos, atributo próprio de ataque e CD, Defesa derivada, vida derivada.

Ele pode acabar funcionando muito bem para uma criatura singular.

Mas imagine uma Trilha múltipla com quatro invocações distintas.

Agora o jogador administra:

- seus cinco atributos;
- cinco atributos de cada invocação;
- quatro Defesas;
- quatro vidas;
- quatro CDs;
- quatro listas de Traços;
- quatro posições;
- quatro conjuntos de condições.

Isso pode rapidamente transformar a classe numa planilha.

Draw Steel declarar seu Summoner como uma classe para jogadores experientes é um bom lembrete de que controlar várias entidades produz complexidade real, mesmo quando o sistema foi deliberadamente construído para isso. citeturn21view5

Portanto, **o grau de ficha própria que uma invocação merece deve ser decidido depois que soubermos quantas delas um personagem consegue administrar**.

Talvez uma criatura singular tenha uma ficha mais profunda e criaturas de Presença menor usem estatísticas mais derivadas.

Talvez todas usem a mesma arquitetura simplificada.

Ainda não escolheria.

### A morte permanente precisa ser redesenhada por último, não agora

A regra atual tenta criar peso narrativo por meio de destruição definitiva. É uma questão importante, mas ela depende de:

- quanto custa criar uma criatura;
- quantas você possui;
- quão customizada ela é;
- quão fácil é destruí-la;
- se ela veio da sua técnica ou foi domesticada;
- se existe substituição;
- se existe herança;
- qual Trilha você escolheu.

Se uma pessoa gastou uma sessão inteira construindo sua **única** invocação singular e um crítico aleatório pode apagar permanentemente a peça central da ficha, estamos lidando com uma experiência muito diferente de Geto perder uma maldição de um repertório enorme.

Portanto:

> **não devemos estabelecer uma regra universal de morte antes de definir o valor que cada invocação representa para o personagem.**

## Ordem de reconstrução

A pesquisa mudou um pouco a ordem que eu adotaria inicialmente. Eu reconstruiria o sistema nestas etapas.

| Etapa | O que resolvemos | Por que vem aqui |
|---|---|---|
| **Núcleo de presença e comando** | Repertório, Capacidade de Campo, Presença, ações, ordens, autonomia e manifestação. | Todo o resto depende de saber quantos corpos existem e quantos podem agir. |
| **Acesso universal** | Como um personagem que não é Evocador obtém uma invocação. | Se o subsistema é universal, precisamos conhecer a versão básica antes de construir o especialista. |
| **Construção da invocação** | Corpo, atributos, funções, Traços, Comandos, orçamento e limites especiais. | Agora conseguimos precificar uma habilidade sabendo se ela aparecerá em um, dois ou quatro corpos. |
| **Origem e ciclo de vida** | Técnica, talismã, corpo amaldiçoado, maldição domada, recuperação, perda, obediência. | Depende do valor da criatura e do investimento feito nela. |
| **Caminho Evocador** | Identidade base nos níveis do novo padrão de Caminhos. | Finalmente sabemos quais regras ele pode dominar. |
| **Trilhas** | Singular, Dueto e Múltiplas. | Elas passam a modificar um subsistema estável em vez de definir suas regras básicas. |
| **Balanceamento e apresentação** | dano, vida, PE, tempo de turno, fichas rápidas, exemplos. | Os números finais vêm quando sabemos o comportamento completo. |

### Eu não faria “acesso universal” como uma versão fraca do Evocador

Esse detalhe será importante quando chegarmos lá.

A regra universal deve entregar uma **invocação funcional**.

Depois o Evocador faz mais com ela.

Pathfinder 2e oferece um paralelo muito bom: seu arquétipo realmente concede um eidolon, mas não entrega ao personagem toda a eficiência e coordenação que definem o Summoner completo. citeturn21view1

Para RPG-JJK, isso poderia eventualmente significar que outro Caminho consegue:

> obter → customizar → manifestar → comandar uma invocação.

Enquanto o Evocador consegue coisas como:

> manter repertório maior → manifestar melhor → trocar melhor → coordenar melhor → aprofundar invocações → comandar de formas que outros personagens não conseguem.

Isso preserva perfeitamente a exclusividade de identidade sem criar exclusividade artificial de conteúdo.

### O Evocador base não deveria determinar a quantidade de corpos

Essa é outra decisão que eu tomaria desde já.

A base deveria trabalhar com conceitos que servem às três Trilhas:

**manifestação, repertório, comando, troca, vínculo e adaptação das invocações.**

Quem define a relação final com a capacidade é a Trilha.

Isso evita repetir o erro atual em que Servo, Matilha e Coro precisam carregar dentro delas as regras fundamentais de quantos corpos a pessoa possui.

E permite que a identidade do Caminho seja algo como:

> **Evocador — você domina vínculos e manifestações. Suas invocações não são apenas ferramentas que conhece; elas são a forma principal pela qual você impõe sua técnica ao campo.**

Ainda não considero essa frase final, mas conceitualmente estamos muito mais perto.

## Decisão desta rodada

Depois de comparar o repositório com Pathfinder, Draw Steel, D&D, Girls' Frontline, Diablo e as próprias fantasias de Jujutsu Kaisen, eu considero que já temos informação suficiente para escolher **o primeiro objeto do redesenho**.

> **A primeira coisa a refazer deve ser o capítulo universal de Invocações.**
>
> **E a primeira parte desse capítulo deve ser “quantidade e ação”, não atributos, dano ou catálogo de poderes.**

Mais especificamente, precisamos responder, nessa ordem:

| Pergunta | Conceito que responde |
|---|---|
| **Quantas invocações diferentes posso possuir?** | Repertório |
| **Quantas podem estar presentes juntas?** | Capacidade de Campo + Presença |
| **Quantas podem realmente agir de maneira relevante por rodada?** | Capacidade de Comando |
| **O que fazem quando não recebem uma ordem?** | Autonomia |
| **Até onde consigo coordená-las?** | Vínculo |
| **Quanto custa colocar, retirar ou trocar uma criatura?** | Manifestação |

**Somente depois disso devemos decidir como uma invocação é construída.**

Isso é importante porque o mesmo poder pode ter valores completamente diferentes dependendo da arquitetura.

“Quando esta criatura acerta, derruba o alvo” pode ser razoável quando existe **uma** criatura realizando uma tentativa por rodada.

Pode ser muito forte quando existem **quatro** criaturas fazendo quatro tentativas.

Pode voltar a ser razoável se quatro estiverem em campo, mas o personagem só puder dar **uma ordem ofensiva** naquele turno.

Sem Capacidade e Comando, **não existe preço confiável para nenhuma habilidade de invocação**.

### O modelo que eu usaria como ponto de partida

Ainda sem colocar números, nosso primeiro protótipo deveria ter esta forma:

> **O personagem possui um Repertório.**
>
> **Cada invocação possui uma Presença.**
>
> **Você possui uma Capacidade de Campo.**
>
> **Pode manter invocações cuja Presença total caiba nessa capacidade.**
>
> **Ter uma criatura em campo não significa que ela recebe uma ação completa.**
>
> **Ordens determinam quais invocações produzem efeitos relevantes naquele turno.**

A partir desse mesmo esqueleto conseguimos testar as três fantasias:

**Singular**

> Capacidade concentrada → uma criatura muito mais profunda → maior autonomia → protege e luta por você.

**Dueto**

> Capacidade dividida moderadamente → uma ou duas criaturas → alta interação entre suas ações e as delas → vocês lutam juntos.

**Múltiplas**

> Capacidade espalhada → várias criaturas diferentes → repertório e posicionamento ganham importância → suas ordens são sua principal forma de combater.

E isso produz uma conclusão que considero particularmente valiosa:

> **A diferença entre as três Trilhas não precisa ser “1, 2 ou 5 invocações”.**
>
> Ela pode ser **como cada uma transforma a mesma Capacidade em jogo.**

É uma fundação muito mais saudável.

### O que considero definitivamente descartado

Com o que vimos, eu não levaria para a nova versão como pressupostos:

**Matilha com cinco corpos e uma barra de vida; número de corpos definido diretamente pela Trilha; Rotina dividida como única defesa contra múltiplas criaturas; Ação Padrão por criatura como único sistema de comando; origens diferenciadas principalmente por vida; destruição permanente igual para todas as origens; e Evocador como único acesso normal ao subsistema.**

Algumas ideias dessas podem reaparecer em formas específicas. **Nenhuma deveria continuar sendo uma fundação.**

### O que considero definitivamente preservado

Duas coisas que você já escolheu ficam ainda mais fortes depois da pesquisa:

**Invocações continuam altamente customizáveis.**

O precedente de Pathfinder mostra que uma criatura modular pode ter enorme identidade sem depender de uma lista fixa de monstros, desde que os eixos perigosos tenham limites próprios. citeturn20view2

E:

**as três Trilhas continuam baseadas na relação entre Evocador e invocação.**

A melhor formulação que encontrei para servir de norte a todo o futuro redesenho é:

> **Uma luta por você.**
>
> **Uma luta com você.**
>
> **Várias são a maneira pela qual você luta.**

Essa divisão é simples, temática e, mais importante, produz **três economias de ação diferentes**. Por isso ela é suficientemente forte para sustentar Trilhas completas, e não apenas três versões da mesma ficha.

O ponto inicial do próximo documento, portanto, não é “Evocador nível 2”.

É:

> **Invocações — Repertório, Presença, Campo e Comando.**

Quando essa fundação estiver funcionando com **um personagem comum controlando uma invocação**, **um protótipo singular**, **um protótipo de dueto** e **um protótipo múltiplo**, teremos finalmente uma base sobre a qual vale a pena calcular vida, dano, PE, customização e, por último, reconstruir o Evocador.