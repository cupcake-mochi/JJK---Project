# Planejamento da organização do Manual da Guilda

Proposta editorial 3, de 02/10/2026. Base examinada: Projeto - M v0.331. O diagnóstico, o estudo dos livros e a pesquisa de métodos agora dão origem a um piloto delimitado, com preparação mecânica e primeira pauta de nomes.

**Atualização após o piloto 2:** o [adendo de regras comuns](ADENDO-REGRAS-COMUNS.md) amplia a cobertura de movimento, exploração e furtividade e passa a orientar a próxima etapa. A arquitetura abaixo é a proposta original de vinte capítulos; esse total não é mais uma meta fixa. As regras comuns que as Trilhas pressupõem precisam ser resolvidas antes da reescrita integral.

Este plano organiza a revisão do livro inteiro: sequência de leitura, localização das regras, nomes, redação, exemplos, imagens e publicação. O objetivo é que uma pessoa nova consiga começar e que uma pessoa em sessão encontre a regra sem depender de quem escreveu o sistema.

**Recomendação:** um livro principal de jogador com vinte capítulos, divididos em cinco partes, e referências no fim. A abertura apresenta o mundo e as possibilidades de personagem, conduz a uma primeira experiência de jogo e oferece caminhos de consulta. Manter o material de preparação e arbitragem do mestre em seu destino próprio. Rever os nomes estruturais antes da reescrita em escala e testar texto e diagramação juntos num piloto. Preservar as cores atuais do tema.

O [piloto editorial](PILOTO-EDITORIAL.md) está detalhado para execução. A [primeira rodada de nomes](NOMES-PRIMEIRA-RODADA.md) propõe alternativas para três conceitos, sem bloquear a amostra com os termos vigentes. O planejamento está pronto para discussão e execução por etapas. Os capítulos, as regras e os arquivos publicados da v0.331 não foram reorganizados nesta tarefa. Os títulos abaixo são títulos editoriais propostos; os nomes atuais das mecânicas continuam valendo.

## Método e resultado desejado

As observações do Mizuki e da Caramelo identificam dificuldades reais de leitura. Suas soluções sugeridas serão avaliadas pela função do trecho e pelo efeito no leitor. A exigência de preservar as cores do tema é uma restrição de produção; a quantidade de palavras, colunas, imagens e marcadores depende das provas.

O trabalho segue edição estrutural, revisão de texto e nomes, projeto visual e revisão da prova diagramada. O livro combina três necessidades: imaginar o mundo e o personagem; aprender a jogar; consultar durante a sessão. Um trecho pode cumprir mais de uma delas, mas precisa ter sua função principal clara. Cortar toda repetição, escrever todas as frases curtas ou impedir qualquer quebra de página não são critérios de qualidade.

O [diagnóstico de leitura](DIAGNOSTICO-DO-LEITOR.md) confronta as reclamações com a edição vigente. O [método e protocolo de leitores](METODO-E-TESTES-COM-LEITORES.md) fundamenta o fluxo em CIEP, Diátaxis, testes de conteúdo, observação de tarefas e orientações de acessibilidade. A adaptação desses métodos ao Projeto - M é uma decisão editorial; ainda não há teste humano do piloto. Os [livros de referência](ESTUDO-DOS-LIVROS.md) foram estudados por amostras identificadas, e a [auditoria do PDF](AUDITORIA-DO-PDF.md) registra os problemas de produção observados.

## Diagnóstico do material atual

O livro tem dezenove capítulos e três peças de abertura, distribuídos em 22 fontes Markdown. A contagem lexical dessas fontes dá aproximadamente 109 mil palavras. Ela inclui títulos, tabelas e números; serve para comparar o peso dos blocos, e não deve ser confundida com a contagem do Word ou do arquivo de texto exportado.

| Bloco atual | Palavras pela mesma contagem | Parcela do conjunto |
|---|---:|---:|
| Caminhos e Trilhas | 32.234 | 29,5% |
| Fundamento | 13.948 | 12,8% |
| Invocações | 16.371 | 15,0% |

Os três somam 57,2% do texto, antes de arredondar as parcelas. Essa concentração pede navegação interna, procedimentos curtos e catálogos bem localizados. O tamanho, sozinho, não prova redundância.

O inventário completo, com arquivos, títulos e hashes, acompanha este plano. São seis Caminhos e dezoito Trilhas na edição integrada. O estado das Origens ainda depende do trabalho em outro ambiente; não se deve transformar a enumeração atual em requisito imutável da próxima edição.

Os problemas estruturais observados foram:

- O glossário completo aparece antes da cena inicial. Ele ajuda na consulta, mas também põe um catálogo extenso na frente de quem quer começar.
- A criação só chega no capítulo 6, depois de regras detalhadas de dano, condições e descanso. É possível antecipar a escolha do personagem com uma explicação básica menor.
- Como Jogar concentra resolução geral, ataque, defesa, Bloquear, recursos, vida a zero e condições. Parte disso precisa continuar como apresentação; a regra completa pode ter destinos mais previsíveis.
- Fundamento reúne definição da técnica, procedimento de montagem, catálogo, poderes avançados, progressão e exemplos prontos. São tarefas diferentes dentro de um mesmo capítulo.
- Invocações apresenta grande parte da montagem e dos catálogos antes de explicar o ciclo completo da entidade em campo. Quem já tem uma entidade precisa atravessar material de construção para chegar ao uso.
- Os Caminhos têm apresentações de épocas diferentes. Há habilidades em caixas compartilhadas e outras em seções próprias, com critérios distintos para exemplos e exceções.
- Há termos que precisam ser confrontados por sentido, além de procurar palavras iguais: Classe, Classe Passiva, grau, patente, Refino, Lapidação e marcos, por exemplo.
- A documentação editorial também envelheceu: o README do livro ainda descreve vinte fontes, enquanto a pasta contém 22. Documentação de produção entra na revisão de consistência.
- A abertura mistura a quantidade de jogadores com a de mestres, enquanto a descrição do projeto fala em cinco a sete mestres ativos. É uma questão de apresentação a esclarecer, não um novo limite de grupo.

A revisão não começa eliminando toda repetição. Um lembrete local pode poupar várias consultas. O que precisa de controle é a repetição que reescreve uma regra inteira e acaba criando outra versão dela.

## Arquitetura recomendada

A ordem de publicação e a ordem de trabalho serão diferentes. O leitor recebe um caminho de entrada simples. A equipe revisa primeiro as regras das quais os demais capítulos dependem.

### Abertura

Capa, créditos e sumário dão acesso ao conteúdo. A apresentação precisa fazer o leitor imaginar uma vida nesse mundo: ameaças sobrenaturais no cotidiano, relações entre personagens, motivos para agir e situações que se transformam em missões. O texto estabelece o que se pode interpretar pelas regras vigentes, sem restringir toda ficha a um feiticeiro humano com técnica inata.

A entrada no mundo será uma sequência curta e concreta, ligada à primeira cena e às decisões de criação. Selecionar o que o iniciante precisa, sem antecipar uma enciclopédia da obra. Verificar fatos do cenário em fontes primárias, distinguir adaptações próprias e começar sem depender de grandes revelações do enredo. O formato de guilda ganha uma explicação principal legível: pessoas organizam sessões num servidor e personagens podem participar de mesas diferentes. Isso não cria uma instituição fictícia obrigatória.

A orientação de leitura fica aqui: começar pelo tutorial, criar personagem com o roteiro ou consultar uma regra conhecida. Cada percurso informa seus pré-requisitos. A abertura não pode mandar simultaneamente começar pela cena e ler outro capítulo antes de qualquer coisa.

Um quadro curto apresenta os termos indispensáveis para atravessar o começo: atributo, maestria, teste, CD, vida, PE, Origem, Caminho, Trilha e técnica. É uma seleção do glossário, mantida a partir das mesmas definições. O glossário completo vai para o fim.

O tutorial já existente continua dentro do livro. A decisão anterior de não produzir um quick-start separado é preservada.

### Parte I — Começar a jogar

| Capítulo proposto | Conteúdo e função |
|---|---|
| **1. Como jogar** | Conversa de mesa, primeira rolagem, atributos e maestria, vantagem, diferença entre ataque e TR, recursos em uma visão breve. A cena da Kaori entra como demonstração guiada. |
| **2. Criação de personagem** | Roteiro completo com a ficha à vista, decisões em ordem, caminhos de leitura para cada rota de poder e exemplo preenchido. Cada escolha termina dizendo o que anotar e onde buscar as opções. |

O capítulo 1 ensina o suficiente para entender uma cena. Ataques completos, Bloquear, queda e recuperação têm capítulos de consulta próprios mais adiante. O resumo inicial aponta para eles e não estabelece exceções próprias.

Na criação, a ordem efetiva de escolhas continua condicionada às regras: Origem, técnica, Caminho, atributos e demais etapas não serão trocados apenas para caber numa sequência visual bonita. O trabalho editorial pode apresentar decisões provisórias e retornos ao roteiro sem mudar quando elas se tornam válidas.

### Parte II — Construir e desenvolver o personagem

| Capítulo proposto | Conteúdo e função |
|---|---|
| **3. Origens e Legados** | Formas de origem, efeitos na ficha e Legados. Recebe a versão conciliada do trabalho externo. O formato final depende dessa entrega. |
| **4. Caminhos e Trilhas** | Comparação inicial dos seis Caminhos, regras comuns e seis seções independentes, cada uma com suas três Trilhas. |
| **5. Perícias e Ofícios** | Treino, atributo usado, testes, catálogo e aplicações já existentes em exploração e interação. |
| **6. Equipamento e ferramentas amaldiçoadas** | Compra e acesso, uso, treino, armas, proteção, carga e, em seção própria, ferramentas, objetos e Estigmas. |
| **7. Experiência e progressão** | Subir de nível, entregas, marcos, escolhas e registro entre mesas. Regras de personagem distinguem-se das recomendações administrativas para a guilda. |

O capítulo 4 continua sendo um capítulo lógico, mas cada Caminho deve abrir como uma unidade reconhecível, com marcador próprio no PDF e acesso pelo sumário. Internamente, pode ser montado a partir das seis fontes integradas. Não há razão para obrigar o leitor a percorrer as outras cinco classes.

A fusão de Equipamento e Ferramenta Amaldiçoada aproxima assuntos que se consultam juntos. Preserva uma fronteira visível entre equipamento comum, ferramenta e objeto amaldiçoado; não unifica conceitos nem torna os três intercambiáveis.

A progressão se aproxima da criação para permitir planejar e atualizar a ficha. As tabelas são as mesmas da edição vigente até existir decisão mecânica diferente.

### Parte III — Resolver as cenas

| Capítulo proposto | Conteúdo e função |
|---|---|
| **8. Turnos e combate** | Iniciativa, ações, deslocamento, ataques, Defesa, Bloquear, oportunidade, concentração e preparo, em ordem de resolução. |
| **9. Dano, condições e recuperação** | Aplicar dano, proteção e reduções conforme as regras, condições, cobertura, alma, vida a zero, morte, descanso e reparo. |

Os capítulos 8 e 9 são destinos de consulta. O capítulo 1 faz a apresentação e o 5 explica as perícias. Não é necessário inventar um sistema novo de exploração ou de cena social para preencher um capítulo.

Cobertura permanece definida uma vez, com um diagrama e referência no ponto em que modifica o ataque. Inconsciente, Incapacitado, Derrubado e os demais estados precisam de entradas que permitam reconhecer tanto seus efeitos quanto a duração e o término já previstos.

A fronteira entre os dois capítulos é o resultado: o 8 chega ao ataque ou teste resolvido; o 9 aplica suas consequências e mostra como recuperar. Exceções continuam junto da habilidade que as concede.

### Parte IV — Técnicas e poderes

| Capítulo proposto | Conteúdo e função |
|---|---|
| **10. Aptidões e Refino** | Recursos e poderes comuns de quem tem energia: obter, escolher, usar e consultar aptidões. |
| **11. Fundamento e criação de feitiços** | Descrição, Regra, Família, Selo, Passivas, orçamento e procedimento completo de montar e usar um feitiço. |
| **12. Formas, Melhorias e Restrições** | Catálogo da construção, com índices por nome e função e indicação dos requisitos relevantes. |
| **13. Liberação Máxima, Técnica Máxima e Domínio** | As três extensões avançadas, seus procedimentos e as interações entre Domínios. |
| **14. Técnica Marcial** | Acesso, transformações do procedimento comum, Kata, Ruptura, Ōgi, rotas de arma e ferramenta e exemplos. |
| **15. Sem Técnica** | Acesso, Semente, Manejo, Auge, limites e aplicação da construção comum. |
| **16. Bênçãos e Lapidação** | Desenvolvimento e catálogo da rota sem energia, com a ponte necessária para os conceitos compartilhados. |
| **17. Ritual** | Procedimento, testes, ganhos, falhas, acesso e ritual em dupla. |
| **18. Pactos** | Formas de pacto, custos, limites, criação e aplicação das trocas já aprovadas. |

Separar o Fundamento em três capítulos não cria três sistemas. O capítulo 11 ensina a construir; o 12 fornece as peças; o 13 trata dos recursos avançados. A ficha de feitiço e a conferência final devem continuar próximas do procedimento de montagem.

As rotas Marcial, Sem Técnica e sem energia precisam de um mapa curto: o que herdam, o que substituem e o que não acessam. Esse mapa deve ser extraído das regras atuais. Não transformar a organização por capítulos em novos pré-requisitos.

Aptidões precedem o construtor na ordem proposta por incluírem recursos comuns já usados pelos Caminhos. A definição breve de Classe Passiva aparece no ponto de uso e remete à escala completa. Se o piloto mostrar excesso de idas e voltas, a posição desse capítulo é o primeiro ajuste a testar; não será necessário redesenhar todo o sumário.

Exemplos prontos permanecem ao lado da máquina que demonstram: técnica e feitiço comuns no 11; Liberações e Técnicas Máximas no 13; exemplos de Kata no 14.

### Parte V — Invocações

| Capítulo proposto | Conteúdo e função |
|---|---|
| **19. Invocações em campo** | O que é uma entidade, aquisição em resumo, manifestação, ciclo, intenção, comando, ações, reação coletiva, movimento, energia, queda e saída. Um exemplo acompanha a sequência. |
| **20. Montagem de entidades** | Aquisição completa, domar, ficha, famílias, básicas, especiais, espaços, passivas, progressão, formas, melhorias, restrições e exemplo completo de montagem. |

A regra geral de Invocações pertence a estes capítulos. Evocador e suas Trilhas descrevem as mudanças específicas que concedem e apontam para o procedimento afetado.

O catálogo reduzido das entidades continua disponível junto de sua montagem. A semelhança com o Fundamento não autoriza apagar regras locais: os custos, limites e escalas diferem. Onde a semântica realmente for comum, a fonte de produção pode ser compartilhada; o resultado publicado deve continuar utilizável sem uma sequência excessiva de consultas.

### Referências finais

- **Glossário completo:** definição breve, categoria quando necessária e destino da regra completa.
- **Referência de mesa:** sequência de ataque, recursos do turno, condições, recuperação e ciclo de invocações.
- **Fichas e modelos:** personagem, feitiço e entidade, conciliados com o trabalho das fichas.
- **Índice remissivo:** destinos principais, referências úteis e nomes antigos que apontem para os novos durante a transição.

Os nomes antigos funcionam como entradas de busca, não como dois nomes oficiais concorrentes no corpo do livro. As referências rápidas são geradas ou conferidas contra suas fontes para não virar uma nova versão da regra.

## Caminhos de leitura

A estrutura não exige ler todos os catálogos em sequência. A abertura aponta três percursos: aprender a jogar, pelo capítulo 1 e depois 8 e 9; criar personagem, pelo 1 e pelo roteiro do 2, abrindo apenas os catálogos necessários; construir poderes, pelo procedimento do 11, pelas opções do 12 e pela rota correspondente.

O custo desta escolha é afastar o combate detalhado da abertura. A cena inicial precisa ser suficiente para começar, e o acesso aos capítulos 8 e 9 deve ser direto no sumário e nos marcadores. Essa é uma das coisas a testar no piloto.

## Fronteira do livro principal

O manual precisa conter tudo que um jogador necessita para construir e usar as opções publicadas. Pré-requisitos, preços, limites, falhas e exceções não podem desaparecer por serem difíceis de explicar.

A preparação de encontros, a calibração de inimigos, o processo de aprovação de conteúdo próprio, a fabricação detalhada de itens e a administração da guilda têm destinos de mestre já previstos no projeto. O bestiário permanece um material próprio. As regras de PvP seguem o destino de mestre decidido anteriormente.

Não abrir agora uma frente de escrita do livro do mestre para conseguir concluir a revisão do jogador. Registrar interfaces e reaproveitar o material já existente quando for executada aquela frente. As pendências do arquivo REMOCOES-material-de-mestre continuam rastreáveis.

Regras que afetam escolhas do jogador permanecem acessíveis a ele. A explicação de como os autores chegaram ao preço de uma arma pode ficar na documentação de design; o preço que ele paga e o efeito da arma precisam estar no manual.

## Revisão de nomes

A revisão ocorrerá em duas passagens.

**Primeiro, termos estruturais.** Conceitos repetidos por todo o sistema: categorias de poder, progressão, recursos, ações e condições. Mudá-los tarde multiplica o retrabalho. A ficha participa desta revisão porque é onde o jogador mais vê esses termos.

**Depois, nomes locais.** Habilidades, efeitos, Trilhas e entradas de catálogo, trabalhados junto de cada lote de texto. Incursor, Pugilista e Malabarista já estão aprovados. Reflexo e Sentença Final continuam na pauta; nenhum substituto foi escolhido neste plano.

Cada proposta deve apresentar o significado atual, o problema concreto, duas ou três alternativas e o custo da troca. Um nome evocativo pode continuar acompanhado por uma linha operacional clara. A meta não é dar nome técnico a todas as habilidades.

Os critérios são: permitir uma associação razoável com o efeito; diferenciar conceitos vizinhos; caber na ficha e na fala; combinar com a ficção do sistema; não colidir com outro nome ou com um uso muito estabelecido no hobby.

O registro de renomes terá identidade estável, nome antigo, nome proposto, decisão do Mizuki, origem da regra e superfícies afetadas. Trocas globais por busca e substituição só entram depois de separar usos homônimos. O termo Projeto - M, por exemplo, não muda por conveniência editorial.

A pauta inicial está em PAUTA-DE-DECISOES.md. Ela identifica o que investigar; não declara todos esses termos defeituosos.

## Revisão textual e formato das entradas

A regra de voz atual é o ponto de partida. As quatro camadas aprovadas para catálogo continuam: identificação, situação de uso, efeitos reconhecíveis e regra. A forma visual pode variar por família, desde que a localização das informações seja previsível.

| Família | O que o leitor precisa localizar |
|---|---|
| Regra de procedimento | Quando se aplica, sequência de resolução, resultado e exceções relevantes |
| Habilidade de Caminho ou Trilha | Nível, gatilho ou ativação, custo, alvo e alcance, efeito, duração, frequência e término, quando houver |
| Entrada de catálogo de montagem | Função, custo ou degrau, requisitos, escala e restrições de combinação |
| Condição | Efeitos separados, duração ou fonte da duração, meios previstos de terminar e interações indispensáveis |
| Equipamento | Categoria, treino, mãos, alcance, dano, propriedades, requisito, preço e carga, conforme o item |
| Exemplo | Situação, escolha, recursos disponíveis, resolução e estado final |

Não preencher campos ausentes com regras inventadas. Uma habilidade passiva não precisa de uma linha ornamental de custo. Uma condição cuja duração vem do efeito que a aplicou deve dizer isso, sem receber duração nova.

O padrão evita dois extremos: um parágrafo único que esconde custos e uma ficha repetitiva com dez rótulos para uma habilidade de duas linhas. Listas ficam para alternativas, etapas e efeitos independentes. Prosa explica a relação entre eles.

A revisão registra três espécies de alteração:

1. **Editorial:** muda clareza ou posição, mantendo a mesma resolução.
2. **Nomenclatura:** altera o termo, com correspondência aprovada.
3. **Mecânica:** muda possibilidade, preço, alvo, momento, duração, frequência, alcance, resultado ou exceção.

A terceira espécie segue em pauta própria até receber decisão. Trocar “pode” por “deve”, retirar “hostil” ou mudar “após o ataque” para “ao acertar” é alteração mecânica mesmo que nenhum algarismo mude.

Exemplos e ilustrações explicativas podem esclarecer a regra. Não serão usados como a única fonte de uma exceção. Quando uma frase aparentemente dispensável for dona de um fato, o fato é preservado na regra antes de cortar a frase.

Não estabelecer uma meta geral de eliminar 20% do livro, nem igualar o tamanho dos seis Caminhos. Cortes serão avaliados por perda de informação, facilidade de encontrar e compreensão.

## Exemplos e elementos visuais

**Exigência posterior do Mizuki: não usar imagens geradas por IA.** Ilustrações futuras devem ter origem confirmada. A prova inicial usa tipografia, tabelas, ficha anotada e diagrama de regras.

O livro precisa de imagens que mostrem o jogo e de ilustrações que convidem a jogá-lo. As duas funções entram no orçamento editorial.

| Elemento prioritário | O que precisa comunicar |
|---|---|
| Ficha anotada | Onde cada decisão de criação é registrada e onde o jogador encontra o número durante a sessão |
| Sequência de ataque | Declaração, respostas anteriores à rolagem, acerto, defesa escolhida e aplicação das consequências |
| Movimento e cobertura | Espaços, distâncias, ponto de apoio, linha de ataque e posições possíveis |
| Construção de feitiço | Orçamento, escolhas, gasto e resultado, com todas as contas do exemplo |
| Ciclo de invocação | O que pertence ao invocador, a cada entidade e à reação coletiva |
| Progressão | O que vem do nível, do marco, do Caminho e da Trilha |
| Ilustrações dos Caminhos | A fantasia de jogo de cada um, distinguindo postura, função e relação com a técnica |
| Aberturas de parte | O clima de ação e ocultismo contemporâneo do projeto |

Direção inicial proposta: ação e sobrenatural no cotidiano, áreas claras para leitura e silhuetas fáceis de distinguir. As cores atuais ficam preservadas por pedido expresso do Mizuki. A paleta Neve Saturado usa tinta `#251727`, selo `#2B1B2E`, selo fraco `#9A6F87`, acento `#BC2A6E`, acento claro `#ECC3D6`, fundo washi `#FDF0F6`, zebra `#FADDEA`, linha `#F8C7DC` e cinza `#847B86`. São valores lidos dos estilos atuais. A composição, tipografia, área de texto e aplicação dessas cores podem ser revistas. Combinações de pouco contraste devem ser corrigidas usando papéis adequados para cada cor.

Não usar arte de preenchimento para cumprir uma proporção fixa de imagem por página. O catálogo pode ser denso; uma abertura pode respirar. Uma cena que demonstre alcance ou parkour precisa corresponder às possibilidades escritas.

Os diagramas técnicos devem ter texto legível, legendas e identificação que funcionem sem depender apenas da cor. Ilustrações, fontes e créditos terão um inventário de produção. As figuras dos livros de referência servem para análise; os novos elementos do Projeto - M devem ter seus próprios arquivos e créditos.

### Piloto de diagramação

Começar com uma prova integrada da **abertura e primeira experiência de jogo**: apresentação do mundo, trecho do tutorial de Kaori, primeira decisão de criação, habilidade e tabela. É onde se testa se o livro convida, ensina e permite agir. Não diagramar apenas uma capa bonita ou uma página de texto fácil.

O capítulo proposto **Turnos e combate** continua como prova de procedimentos, tabelas, exceções e diagramas. Avaliar conteúdo real suficiente para representar essas situações, sem impor um número de páginas.

Antes de estender o padrão ao resto, acrescentar provas de três situações que esse capítulo não cobre bem: habilidade longa, catálogo com tabela larga e ficha de entidade. Bastião, Malabarista e a montagem de Invocações fornecem os casos.

Comparar a leitura em página inteira, em ampliação normal de tela e em impressão comum. Duas colunas são uma hipótese de partida para a prosa. Tabelas e diagramas podem ocupar largura inteira. Tamanho de fonte e largura de coluna são decididos pela prova, não pela meta de reduzir páginas.

O Word permanece apropriado para comentar e revisar texto. A diagramação final sai da fonte editorial e dos estilos do livro; não se mantém uma edição independente dentro do Word.

### Navegação e continuidade de página

O painel lateral atual tem 827 marcadores, com os 199 grupos que possuem filhos configurados abertos. Há seis níveis, gerados a partir de todos os títulos do HTML. O tratamento deve separar a estrutura semântica do texto da seleção de atalhos visíveis.

Proposta inicial: partes, capítulos e destinos de consulta úteis, com ramos recolhidos. Caminhos e Trilhas podem justificar um nível adicional; cada habilidade de nível, subtítulo repetido ou cabeçalho de exemplo não precisa virar marcador. Índices internos clicáveis, âncoras, busca e remissões continuam dando acesso às entradas. A quantidade final será consequência da seleção, não uma meta de redução arbitrária. O sumário impresso também precisa de seleção própria.

Proteger unidades de sentido: título com começo do texto, custo com efeito, rótulo com tabela e cabeçalho com dados. Permitir que seções longas continuem de forma orientada. A proibição de qualquer divisão pode gerar páginas vazias, deslocamento excessivo de caixas e fonte pequena. A capa pode usar espaço livre intencional; uma página com duas linhas remanescentes de orientação exige outra avaliação.

Conferir o PDF exportado: destinos, voltar ao ponto anterior, busca por nomes atuais e antigos, ordem de leitura e uso com ampliação. Não declarar acessibilidade certificada apenas porque o texto é selecionável. As provas devem incluir computador e o dispositivo que os leitores realmente usam.

## Etapas de execução

| Etapa | Trabalho | Saída que permite avançar |
|---|---|---|
| **0. Diagnóstico** | Inventário, leitura dirigida, comentários de leitores e auditoria dos PDFs | Concluído para este recorte; lacunas, amostras e limites registrados |
| **1. Direção e termos centrais** | Ajustar percurso e nomes; mapear interfaces com Origens e fichas | Escopo delimitado; termos vigentes ou renomes aprovados identificados; interfaces externas pendentes registradas |
| **2. Piloto integrado** | Trabalhar abertura, exemplo e regras representativas; diagramar e observar leitura e consulta | Texto e apresentação avaliados juntos, com diferenças mecânicas separadas |
| **3. Revisão por lotes** | Rever unidades completas na ordem de dependência, já com exportação e prova visual | Cada lote com texto, fontes, navegação, decisões e conferência |
| **4. Consolidação visual** | Estender os padrões às situações restantes, produzir arte e conciliar índices | Livro completo com identidade, hierarquia e referências coerentes |
| **5. Provas do conjunto** | Leitura transversal, tarefas humanas, inspeção das páginas e verificação técnica | Achados tratados; limites dos testes declarados |
| **6. Entrega** | Exportações finais, conferência cruzada e pacote | Edição identificada, correspondência de nomes e pendências remanescentes |

O piloto pode usar opções e termos já confirmados sem aguardar toda a entrega externa de Origens e fichas. Registrar as interfaces pendentes e conciliar as entregas antes de fechar os capítulos afetados.

O piloto visual acompanha o texto desde a primeira amostra estável. A arte pode avançar em paralelo aos lotes aprovados. Mudança de redação que altera uma quebra importante exige nova prova. A paginação definitiva vem depois da estabilização do conteúdo.

Não há estimativa honesta de dias antes do piloto: a quantidade de mudanças de nomes e a extensão da nova entrega de Origens ainda não estão fechadas. O avanço será medido por lotes aceitos, não por páginas redigidas.

## Trabalho com o Claude

O plano é utilizável em qualquer ambiente que consiga ler as fontes. O trabalho externo das fichas continua tendo sua própria frente. Na conciliação, comparar a versão das regras, os termos e as fórmulas, e registrar o que cada alteração afeta.

Para a revisão do livro, trabalhar com um responsável por lote e uma segunda leitura independente. O segundo revisor recebe a fonte vigente e a proposta; devolve achados localizados e alternativas, evitando reescrever simultaneamente o mesmo capítulo.

A escolha do responsável pode usar o piloto já recomendado: mesmas amostras escolhidas para a comparação, mesmas instruções, resultados avaliados sem identificar o modelo. Isso é uma avaliação do projeto, não prova geral de superioridade entre modelos. Não há motivo para repetir esse comparativo a cada capítulo depois de o fluxo funcionar.

Cada remessa deve dizer: base usada; unidade em revisão; alterações autorizadas; decisões pendentes; fontes; produto esperado; critérios de conferência. O roteiro operacional está em ROTEIRO-DE-EXECUCAO.md e aponta para as fontes, sem copiar todas as regras do projeto.

## Critérios para considerar a revisão concluída

- Todo conteúdo vigente tem destino conhecido; nenhuma regra desapareceu ao mover ou resumir uma seção.
- Nenhuma diferença mecânica entrou disfarçada de edição.
- Nomes aprovados aparecem de forma consistente no livro, ficha, gerador, fontes e índices; os antigos continuam encontráveis na transição.
- A abertura permite imaginar o mundo, os personagens e as situações de jogo, sem depender de conhecer o anime ou outro sistema.
- O caminho de uma primeira ficha e de uma primeira cena é testado com leitores sem explicação oral do autor; dificuldades são registradas e tratadas.
- Uma consulta encontra a regra completa e suas exceções relevantes sem depender de lembrança da conversa de design.
- Duas pessoas que mestram resolvem os casos de leitura de prova da mesma maneira. Divergências são investigadas, tratadas e novamente conferidas; um caso mecânico mantido em aberto permanece declarado como pendência, sem aprovação daquela prova.
- Referências internas, sumário e marcadores digitais apontam para os destinos corretos.
- As tabelas, exemplos e fichas batem com as fontes; os validadores aplicáveis passam sem checagens puladas.
- Cada variante de PDF entregue foi inspecionada visualmente, separadamente. Títulos, tabelas e caixas não têm corte, sobreposição ou separações que escondam informação necessária.
- O pacote identifica a edição, o histórico de nomes e qualquer pendência que permaneça.

As verificações automatizadas detectam certos defeitos; a leitura editorial e os testes de uso avaliam clareza, consulta, interesse e fidelidade. Não usar detectores de IA, nota de legibilidade ou contagem de palavras como certificado. O equilíbrio dos seis Caminhos continua sendo uma frente de matemática e mesa.

## Próxima unidade recomendada

**Execução iniciada:** a [primeira versão do piloto](../piloto-editorial-r1/LEIA-ME.md) já foi produzida. Revisar a proposta e a comparação de colunas antes do segundo lote. O escopo originalmente recomendado abaixo fica como referência de cobertura.

Produzir **a primeira versão do piloto**, conforme [PILOTO-EDITORIAL.md](PILOTO-EDITORIAL.md): sequência de entrada no mundo e no jogo, começo da criação, proteção do Bastião e prova visual. O [gabarito de Kaori](evidencias/preparacao-kaori.md) delimita o exemplo que já fecha e o que precisa ser preparado antes da redação. As demais amostras técnicas vêm na segunda entrega, antes de estender o padrão ao livro.

Discutir a [primeira rodada de nomes](NOMES-PRIMEIRA-RODADA.md) em paralelo. Usar nomes atuais com definições claras permite começar sem presumir aprovação dos candidatos. Se houver mudança no sumário, ajustar o mapa antes de mover arquivos; não é necessário refazer o diagnóstico.

## Referências do planejamento

O levantamento inicial de quatro livros está em [REFERENCIAS-E-DIAGNOSTICO.md](REFERENCIAS-E-DIAGNOSTICO.md). O estudo ampliado dos nove arquivos enviados está em [ESTUDO-DOS-LIVROS.md](ESTUDO-DOS-LIVROS.md), com páginas consultadas e limites. Métodos editoriais, relatos públicos e protocolo de teste estão em [METODO-E-TESTES-COM-LEITORES.md](METODO-E-TESTES-COM-LEITORES.md).
