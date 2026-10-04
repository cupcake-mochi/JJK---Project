# Leitores externos e validação editorial — Projeto M

Pesquisa pública feita em 2 de outubro de 2026. Esta nota propõe critérios e testes; nenhum participante humano foi recrutado, contatado ou testado. Revisão por agente é inspeção editorial, não prova de compreensão humana nem playtest. O material da Caramelo é feedback qualitativo de uma leitora e deve permanecer identificado assim.

## O que a pesquisa sustenta

**Navegação precisa de organização, não apenas de menos entradas.** Uma discussão pública de setembro de 2025 reúne pedidos por referências internas clicáveis e marcadores detalhados. No mesmo fio, leitores reclamam tanto de livros de centenas de páginas com apenas alguns marcadores quanto de marcar cada página pelo número. Isso contradiz uma solução simplista de remover todos os atalhos internos: para o Projeto M, a hipótese mais promissora é agrupar partes, capítulos e destinos úteis de consulta, abrindo o painel com os ramos recolhidos. A profundidade exata deve ser testada no próprio livro. Fonte de experiência de leitores, sem representatividade estatística: [RANT: Publishers, please hyperlink your PDFs](https://www.reddit.com/r/rpg/comments/1n71ovo/rant_publishers_please_hyperlink_your_pdfs/).

**Aprender e consultar são duas tarefas reais do mesmo livro.** Em discussão de dezembro de 2025 sobre boa diagramação, há leitores que valorizam a combinação de leitura contínua agradável e recuperação rápida de uma regra durante a sessão. Essa é uma hipótese útil para avaliar a proposta: a abertura ensina e situa, enquanto títulos, índice, glossário e atalhos permitem voltar ao ponto certo. Não significa que todo leitor prefira a mesma ordem de capítulos. [What makes a TTRPG book to be considered having a Good Layout?](https://www.reddit.com/r/rpg/comments/1pbbcbj/what_makes_a_ttrpg_book_to_be_considered_having_a/).

**Mais arte não resolve sozinha o aspecto de livro cru.** Uma conversa de abril de 2026 apresenta leitores que apreciam ilustrações, mas rejeitam excesso de elementos competindo com o texto e pouco contraste. Para o Projeto M, a inferência é usar arte para estabelecer mundo, ação e identidade; demonstrar regras por diagramas quando isso ajuda; preservar áreas tranquilas de leitura. O fórum não prova superioridade de uma ou duas colunas, nem preferência universal por páginas discretas. [Page layouts in TTRPGs](https://www.reddit.com/r/rpg/comments/1sslr6d/page_layouts_in_ttrpgs/).

Esses relatos são amostras espontâneas de comunidades em inglês, sujeitas à seleção de quem comenta. Votos indicam reação naquele fórum; não estimam a opinião dos jogadores de RPG em geral nem a dos jogadores brasileiros do Projeto M. Servem para formular hipóteses e procurar problemas concretos, não para decretar um gosto correto.

## Referências primárias de acessibilidade

- **Vocabulário:** a W3C recomenda palavras comuns, retirada de termos vagos e explicação acessível de siglas e termos incomuns. Aplicação editorial proposta: privilegiar nome funcional em regras de uso frequente; quando o termo jujutsu for indispensável, defini-lo na primeira ocorrência e oferecer atalho ao glossário. Não extrapolar a orientação para uma proibição absoluta de termos ficcionais. [W3C — Use Clear Words](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o3p01-clear-words/).
- **Marcadores:** a técnica PDF2 apresenta uma visão hierárquica para localizar conteúdo e pede conferir os destinos. Aplicação: testar marcadores e sumário clicável no arquivo exportado, incluindo glossário e referência rápida. Ela não define quantidade máxima de marcadores nem limite obrigatório de níveis. [W3C — PDF2](https://www.w3.org/WAI/WCAG22/Techniques/pdf/PDF2).
- **Estrutura:** PDF9 trata de títulos semânticos reconhecidos por tecnologia assistiva. Reduzir o painel de marcadores não deve eliminar a estrutura semântica das subseções. Painel de navegação e marcação interna são camadas distintas. [W3C — PDF9](https://www.w3.org/WAI/WCAG22/Techniques/pdf/PDF9).
- **Ordem de leitura:** PDF3 destaca que documentos com colunas, caixas e imagens podem exportar uma sequência incorreta. É necessário verificar a leitura por tecnologia assistiva e a navegação por teclado, além de olhar a página. Extrair texto corretamente é evidência parcial, não certificação de acessibilidade. [W3C — PDF3](https://www.w3.org/WAI/WCAG22/Techniques/pdf/PDF3).

São técnicas e orientações, algumas suplementares, que ajudam a aplicar princípios de acessibilidade. Não autorizam declarar conformidade WCAG ou PDF/UA com base apenas nesses poucos testes.

## Protocolo proposto para leitores reais

### Preparação

Fazer rodadas curtas, começando por 6 participantes, com possibilidade de ampliar ou fazer novas rodadas conforme as dúvidas. O GOV.UK sugere geralmente 4–8 pessoas por rodada qualitativa e iteração entre rodadas. Esse tamanho é adequado para descobrir problemas, não para afirmar que certa porcentagem de toda a comunidade prefere uma solução. [GOV.UK — Plan user research for your service](https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service).

Distribuição inicial proposta, ajustável à comunidade disponível: 2 pessoas com pouca experiência em RPG; 2 experientes em RPG que nunca leram o Projeto M; 2 jogadores ou mestres do Projeto M. Cruzar esses perfis com familiaridade em Jujutsu Kaisen: incluir fãs e quem conhece pouco da obra. Registrar uso predominante de celular, tablet ou computador e necessidade de ampliação, leitura em voz alta ou outra adaptação. Não presumir que conhecer o anime equivale a conhecer as regras.

Preparar um piloto com abertura do mundo, começo da criação de personagem, um trecho de combate, uma habilidade e uma tabela. A comparação inicial usa trechos equivalentes da v0.331 e do piloto. Registrar versão, páginas e regras cobertas antes de testar. Alternar a ordem das versões entre participantes e usar tarefas equivalentes, mas não idênticas, para reduzir memorização. É uma comparação exploratória; não tratá-la como experimento estatístico.

As sessões propostas duram aproximadamente 30–45 minutos. Dar instruções neutras, pedir que a pessoa explique o que procura e observar sem revelar a resposta. Registrar qualquer ajuda do facilitador. Pedir consentimento antes de gravações. O método segue a orientação de observar tarefas concretas com usuários reais ou prováveis e enunciados que não entreguem o caminho da solução. [GOV.UK — Using moderated usability testing](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing).

### Tarefas sugeridas

| Tarefa | Enunciado para a pessoa | Evidência esperada |
|---|---|---|
| Entrar no mundo | Depois de ler a abertura, explique que tipo de personagem você pode interpretar e que tipo de situação ele vive. | Entende a proposta; distingue cenário, papel do grupo e formato de guilda; aponta o trecho que levou à interpretação. |
| Começar a ficha | Você vai jogar pela primeira vez. Mostre por onde começaria e quais escolhas faria antes de preencher os números. | Localiza o roteiro, identifica dependências, percebe o que ainda não precisa decidir. |
| Encontrar uma regra | Seu personagem quer proteger um aliado de um ataque. Encontre a regra aplicável nesta ficha e explique quando ela pode ser declarada. | Acha a habilidade, informa gatilho e reação/custo sem ajuda e sem criar etapa que não existe. |
| Resolver uma interação | Receba uma pequena situação de combate preparada com gabarito. Diga o que pode fazer, o custo e o resultado. | Separa localizar de compreender; permite detectar resposta rápida, mas errada. |
| Associar nomes | Antes de ler as descrições, diga o que esperaria de três nomes candidatos. Depois associe cada nome a uma descrição. | Detecta expectativas falsas, colisões entre nomes e necessidade de explicação. Não escolhe só o nome mais bonito. |
| Navegar no PDF | Partindo de uma página distante, encontre uma condição e depois retorne à habilidade que a aplicou. Use os recursos que quiser. | Observa marcadores, busca, links, retorno, rolagem e desorientação. |
| Ler página densa | Consulte uma tabela e identifique uma opção que cumpra uma restrição simples. | Verifica cabeçalhos, continuação de tabela, tamanho de fonte e espaço entre texto/arte. |
| Avaliar voz | Marque uma passagem envolvente e uma que pareça genérica, repetitiva ou trabalhosa. Explique a diferença. | Obtém frases e razões verificáveis; evita reduzir o julgamento a “parece IA”. |

O responsável editorial precisa preparar e validar os gabaritos usando a fonte mecânica vigente. O texto do enunciado não deve fornecer o nome da seção, se localizar a seção fizer parte do teste. Interações ainda em discussão não servem para medir clareza de uma regra supostamente fechada.

### Registro e decisão

Por tarefa, registrar: resultado correto/errado/parcial; conclusão sem ajuda/com ajuda/abandono; tempo até localizar e tempo até explicar; palavra buscada; caminho percorrido; primeiro equívoco; trecho que o causou; fala literal curta com consentimento. Tempo e número de ações são medidas úteis, mas o resultado é principalmente qualitativo. Uma tarefa controlada também não reproduz todas as dificuldades de uma sessão de jogo. [GOV.UK — Usability testing: qualitative studies](https://www.gov.uk/guidance/usability-testing-qualitative-studies).

Separar quatro classes de problema: **regra** (conteúdo inconclusivo), **texto** (a regra existe, mas foi entendida errado), **navegação** (não a encontra), **apresentação** (a encontra, mas a página dificulta ler). Registrar ainda tema e interesse, pois uma página pode ser clara e desinteressante. O leitor propõe uma solução; o editor investiga a causa antes de adotar a solução literalmente.

Critério editorial proposto: bloquear publicação do lote se houver regra materialmente alterada, texto cortado, link crítico errado ou interpretação incorreta recorrente causada pelo texto. Uma falha grave individual já pede investigação. Pequenos gostos tipográficos são comparados com leitura e busca reais. Após a correção, repetir as tarefas problemáticas com alguém que não aprendeu a resposta na rodada anterior, sempre que possível.

Relatar os resultados com contagens e contexto, como “2 dos 6 participantes interpretaram o custo como opcional”; não transformar isso em “33% dos jogadores não entendem”. Não fixar metas universais de segundos antes de medir a versão atual e definir a natureza da tarefa.

## Revisão contínua entre as rodadas

1. **Inspeção mecânica:** conferir gatilho, ação, custo, alvo, alcance, duração, frequência, exceção, crítico e interação com outras habilidades contra a versão aprovada.
2. **Inspeção de linguagem:** sujeito claro; efeito fácil de achar; termos definidos; frases que acrescentam informação; instrução separada de exemplo e ambientação; primeira ocorrência sem pressupor D&D ou familiaridade com anime.
3. **Inspeção de voz:** marcar contrastes artificiais do tipo “não é X, é Y”, paráfrases consecutivas, aberturas genéricas, conclusões que repetem o parágrafo, enumerações automáticas e vocabulário abstrato onde cabe uma cena ou ação. Contagem serve para triagem, seguida de leitura contextual; o padrão pode ser necessário em casos específicos.
4. **Inspeção visual:** renderizar, olhar abertura, páginas densas, habilidade que cruza coluna, tabela longa e última página de capítulo. Não deixar título sozinho, número de tabela sem legenda, custo separado de seu efeito ou cabeçalho perdido. Uma seção longa pode atravessar páginas se o fluxo e a continuação forem claros.
5. **Inspeção de navegação e acessibilidade:** destinos corretos, rótulos previsíveis, ramos recolhidos quando suportado, busca por termo antigo e novo durante migração, sequência semântica, contraste e ampliação.
6. **Validação humana:** manter resultados separados dos pareceres de agentes. A máquina pode apontar problemas; não declarar que “o jogador entende” sem observação de jogador.

“Parece IA” é uma avaliação estética da leitura, não um método de autenticar autoria. Não publicar uma porcentagem de texto “humanizado” ou um selo de ausência de IA. A pergunta útil é: qual trecho ficou vago, repetitivo, artificial, sem voz ou trabalhoso, e que mudança concreta melhorou sua leitura?

## Complemento metodológico — prioridade sobre receitas e listas

Este complemento incorpora a orientação posterior do usuário: as reclamações servem para identificar o problema; suas soluções sugeridas não precisam ser aplicadas literalmente. Uma edição eficaz começa pela função do trecho e pelo percurso do leitor. A lista de inspeção acima detecta riscos; cumprir seus itens não garante que o livro esteja agradável, claro ou completo.

### 1. Editar em etapas diferentes, com perguntas diferentes

O CIEP distingue edição estrutural, edição do texto e revisão de prova, esta última depois da diagramação. A sequência evita polir capítulos que ainda precisam mudar de lugar ou tentar resolver conteúdo ausente com ajustes de fonte. [CIEP — About proofreading and editing](https://www.ciep.uk/resource/about-proofreading-and-editing.html).

Aplicação proposta ao Projeto M:

- **Edição estrutural:** decidir quem lê, o que quer aprender e quais conhecimentos cada trecho pressupõe; identificar lacunas de mundo, escolhas de personagem e regras; separar conteúdo de jogador, mestre e equipe. Entrega: mapa de leitura, escopo de cada capítulo e lista de conteúdo a acrescentar, mover ou retirar.
- **Edição do texto:** depois do escopo, trabalhar voz, ordem dos parágrafos, exemplos, transições, nomes e precisão. Entrega: capítulos que funcionam em leitura contínua e regras que se recuperam em consulta, acompanhados do registro de alterações mecânicas proibidas ou deliberadas.
- **Projeto visual:** testar tipografia, cor, área de texto, imagens, tabelas, navegação e páginas típicas com conteúdo real; aplicar aos capítulos estabilizados. Uma prova visual antecipada ajuda a descobrir limitações, mas não congela todo o livro cedo demais.
- **Revisão de prova:** conferir o resultado já diagramado, incluindo páginas, títulos, linhas, tabelas, remissões, marcadores e o texto final. Se surgir uma mudança estrutural, voltar à etapa apropriada e gerar nova prova.

No fluxo editorial do CIEP, a edição do texto também considera público, tom, precisão e fluidez. Portanto ela vai além da correção ortográfica. [CIEP — The publishing workflow](https://www.ciep.uk/learn-and-develop/the-ciep-competency-framework/the-publishing-workflow.html).

### 2. Distinguir funções do texto sem fragmentar artificialmente o livro

O método Diátaxis separa aprendizado guiado e consulta de informação. O tutorial conduz uma experiência concreta e progressiva; o material de referência oferece descrições consistentes e previsíveis para quem já precisa de uma resposta. A adaptação ao RPG é nossa: o primeiro combate comentado ensina a jogar; a regra de ataque descreve o procedimento; a tabela rápida ajuda a usá-lo durante a sessão. Não é necessário criar quatro livros ou impor os nomes do método como capítulos. [Diátaxis — Tutorials](https://diataxis.fr/tutorials/), [Diátaxis — Reference](https://diataxis.fr/reference/).

A explicação tem lugar próprio: dar contexto e conectar ideias também é uma necessidade do leitor. Isso ampara reservar espaço para a vida num mundo com maldições, o que os personagens enfrentam e o papel do jujutsu em suas decisões, em vez de tratar ambientação como enfeite a eliminar. É adaptação metodológica, não alegação de que Diátaxis foi validado especificamente para este RPG. [Diátaxis — Explanation](https://diataxis.fr/explanation/).

Um exemplo primário do setor: a editora de Old-School Essentials declara organizar temas em páginas duplas para consulta rápida e combina esse objetivo com arte evocativa. É uma solução concreta a estudar, não prova de que todo assunto do Projeto M deve caber em duas páginas. Uma página dupla do impresso também perde sua simultaneidade em muitos celulares. [Necrotic Gnome — About Old-School Essentials](https://necroticgnome.com/pages/about-old-school-essentials).

### 3. Verificar compreensão por uso e paráfrase

A Nielsen Norman Group recomenda pedir à pessoa que explique o texto com suas próprias palavras e investigar o que um termo significa para ela. Repetir uma frase de memória ou ler em voz alta não prova compreensão. Adaptando ao jogo: após consultar uma habilidade, o participante descreve quando pode usá-la e resolve uma situação diferente do exemplo. Se erra, investigar se faltou informação, se o nome induziu uma expectativa errada ou se a redação tornou uma exceção invisível. [NN/g — How to Test Content with Users](https://www.nngroup.com/articles/testing-content-websites/).

A paráfrase não deve virar exame de eloquência nem teste de memória. Permitir apontar a regra e usar exemplos, desenhos ou explicação oral. Na etapa de consulta, o livro permanece aberto porque essa é a situação real da mesa. Não confundir dificuldade de verbalizar com incapacidade de jogar.

### 4. Tratar concisão e narrativa como decisões de função

Proposta editorial para este projeto, não regra universal das fontes:

- Cortar a segunda frase que apenas repete a primeira; preservar o lembrete que evita abrir outro capítulo no meio de uma escolha.
- Manter uma definição principal estável e permitir resumos curtos nos lugares de uso, sempre coerentes com ela. O problema é duplicação contraditória ou que interrompe o percurso, não toda repetição.
- Uma cena curta pode ensinar melhor do que quatro definições abstratas. Ela merece espaço quando apresenta o mundo, torna uma escolha imaginável ou demonstra uma regra.
- A regra precisa identificar o que fazer, mas a abertura de capítulo pode estabelecer lugar, perigo, desejo e possibilidades de personagem. Aplicar a mesma voz seca a ambos empobreceria o livro.
- Resolver nomes opacos sem apagar identidade: nome compreensível para função recorrente; vocabulário do cenário explicado quando necessário; variedade expressiva nas passagens narrativas, consistência nas palavras que acionam regras.
- Não usar índice de legibilidade, quantidade de palavras ou detector de IA como árbitro de qualidade. Fórmulas não verificam se um conceito foi introduzido na ordem certa, se um exemplo é fiel à mecânica ou se a ambientação provoca vontade de jogar.

O critério de êxito combina leitura, interesse, localização e execução. Um trecho pode passar numa checagem de gramática e fracassar em todos os quatro; outro pode ser mais longo e resolver melhor a necessidade do leitor.
