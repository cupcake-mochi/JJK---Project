# Fundamento: auditoria das rotas e da apresentação

Data: 03/10/2026. Auditoria de fontes e leitura técnica; não é teste com jogadores. Nenhum arquivo publicado ou candidato foi alterado por esta auditoria.

Raiz dos caminhos relativos: `/media/mizuki/HD Externo II/Claude/Claude 2`.

## Fontes de autoridade

O arquivo `invocacoes/05-Edicao-Integrada/60-invocacoes.md` e sua cópia `sistema/05-material/livro/manual/60-invocacoes.md` são idênticos: SHA-256 `4df82e672d063b4d4bfe3394d93bb75052ec3e07d44d90b83c0ea32f10439f82`. As linhas abaixo usam a cópia do manual.

`sistema/03-mecanica/15-invocacoes.md:3` manda usar a edição integrada; seu corpo histórico não serve para contrariar a regra atual. A antiga afirmação de que Fundamento não produz invocação (`:34`) está ultrapassada.

Os capítulos de criação ainda são os publicados em `manual/40-fundamento.md`, `42-tecnica-marcial.md` e `43-sem-tecnica.md`. Há contradições entre capítulo e peça mecânica; elas estão separadas dos fatos confirmados neste relatório. A instrução atual do usuário confirma expressamente que a troca deve valer nas três rotas, incluindo a Marcial.

## Troca de espaço por entidade: o que está escrito

| Questão | Regra atual e fonte |
|---|---|
| O que é trocado? | Um espaço da lista de feitiços conhecidos; não um uso diário nem PE (`60:43–45`). |
| Quantas entidades? | Uma por espaço na regra comum (`60:45`). |
| Nível inicial e evolução? | A entidade tem o nível do personagem e sobe junto com ele (`60:45,55`). |
| Quando refazer a troca? | Ao subir de nível (`60:45`). Se a entidade for destruída, a próxima subida permite refazer a troca; não ressuscita a antiga (`60:995`). |
| Que origem/corpo isso compra? | A origem chamada Técnica: shikigami ou corpo amaldiçoado (`60:5–11`). Não transforma automaticamente uma maldição domada ou um talismã criado em entidade evolutiva. |
| Precisa de Evocador? | Não. Criação de personagem declara que outros Caminhos podem usar o subsistema (`20-criacao-de-personagem.md:119`). O Caminho modifica a regra quando sua habilidade disser. |
| Custa PE para adquirir? | O espaço é o custo de aquisição descrito. PE da entrada não compra entidade (`60:43`). Não há taxa adicional de PE para reservar o espaço. |
| Custa PE para usar? | Sim. Entrada custa a Classe correspondente ao nível da entidade (`60:579–587`); especial custa `3 × Classe da especial` (`60:112`). Sem reserva própria, a especial sai toda do PE do dono (`60:709`). A referência na criação deve deixar esses custos no capítulo de Invocações. |
| A lista pode ter quantas? | Não há limite geral de repertório (`60:53`); cada entidade obtida por espaço exige seu espaço. Ter várias não amplia o teto comum de duas ativas (`60:15,53`). |
| E a lista de ritual? | Outra forma de aquisição: um feitiço de ritual traz uma lista, domada individualmente; as entidades evoluem com o personagem (`60:47`). Não são entidades gratuitas obtidas apenas por declarar que o feitiço é ritual. |
| Uma exceção numérica relevante | Múltiplas Invocações, nível 2: os dois primeiros espaços comprometidos dão duas entidades cada; posteriores seguem a proporção comum (`35-caminhos-e-trilhas.md:2148–2154`). Não repetir a habilidade em Fundamento; basta que a regra geral admita exceções expressas. |

### Quais espaços estão disponíveis

`40-fundamento.md:409–425` e `80-experiencia-e-progressao.md:242–293` dão a mesma lista: `2 + ⌊nível/2⌋ + marcos alcançados`, marcos 6, 10, 14, 18, 22, 26 e 30. Os espaços dos marcos pertencem à mesma lista, sem uma marca de uso exclusivo; portanto também podem ser comprometidos para entidades.

Classe 0 está fora dessa lista (`40:144–158,423`); Liberações Máximas também (`40:943–954`). A Passiva Livre não consome espaço e a Regra Própria começa gratuita (`40:296–302,348`). Nenhuma dessas permissões gratuitas cria um espaço disponível para conversão. Não deduzir novas entidades trocando uma capacidade que nunca ocupou a lista.

Os espaços das especiais de uma entidade (`60:133–145`) pertencem à ficha daquela entidade, não à lista do jogador. A aquisição descreve espaços da **sua lista**; não autoriza uma cadeia de entidades comprando outras entidades com as próprias especiais. Uma ressalva curta no dono de Aquisição resolverá eventual interpretação recursiva; não é necessário ensinar recursão ao leitor iniciante.

Exemplos de contabilidade verificáveis:

- Nível 2: três espaços comuns. Uma entidade + dois feitiços = três. Os dois Classe 0 permanecem separados.
- Nível 10: nove espaços comuns. Uma entidade + uma passiva de Classe Passiva 2 + seis feitiços = nove. Três Classe 0 e uma Liberação continuam fora da conta.
- Nível 30: 24 espaços comuns. Usar espaços de marco não muda a proporção comum de uma entidade por espaço.
- A exceção das duplas pertence à Trilha e não deve virar o exemplo introdutório de Fundamento.

### Aplicação às três rotas

| Rota | Evidência de equivalência | Tratamento recomendado |
|---|---|---|
| Fundamento | Usa diretamente feitiços conhecidos (`40:405–425`). | Incluir a entidade na contabilidade, com remissão a Aquisição. |
| Sem Técnica / Manejo | Tudo do Fundamento vale; feitiço em qualquer capítulo inclui Manejo (`43:11–19`). | Mostrar a mesma opção no ponto em que a lista de Manejos é apresentada. Não reexplicar ações de entidades. |
| Técnica Marcial / Kata | Tudo do Fundamento vale e feitiço em qualquer capítulo inclui Kata (`42:9–17`); Origem sem energia continua recebendo PE como Pontos de Esforço (`25-origens.md:592–606`). | A autorização atual do usuário inclui esta rota. Registrar a equivalência de aquisição e conservar custos; não converter o mero acesso à lista em energia amaldiçoada, aptidões ou poderes pessoais. |

**Lacuna de interface da rota sem energia:** o capítulo de Invocações usa origem “Técnica”, fala em energia paga pelo dono e não explica a apresentação de uma entidade adquirida por Kata. O texto da Origem, por sua vez, nega conjurar energia e preserva Katas como corpo/ferramenta. A instrução do usuário resolve **acesso**, mas a redação ainda precisa resolver **como a regra se apresenta**. Sugestão de decisão editorial/mecânica registrada: nesta troca, o recurso gasto continua sendo PE da rota, com os mesmos números e ações; a entidade deve estar ligada ao equipamento/estilo, e sua energia não concede energia própria ao personagem. Isso é uma convenção de Projeto M autorizada pela equivalência, não informação canônica da obra. Não declarar que qualquer pessoa sem energia manifesta shikigami por natureza.

**Outra lacuna pequena:** o capítulo permite refazer a troca na subida, mas não diz se isso disputa a reescrita de um feitiço por nível (`40:1218`) nem quantas trocas de entidade cabem no mesmo nível. Não afirmar “troque todas” ou “ganha uma troca extra” sem registrar decisão. Proposta conservadora: usar o mesmo evento de revisão de um espaço da lista; a primeira ocupação de um espaço novo é aquisição, não segunda reescrita. Se o autor preferir a troca independente, deve escrevê-la no dono da Aquisição.

## Remissões propostas

Texto central sugerido para a lista de criações conhecidas:

> **Invocações.** Você pode ocupar um espaço da sua lista com uma entidade, em vez de um feitiço. Ela tem seu nível e evolui com você. A troca também vale para espaços de Manejo e de Kata. Monte e use a entidade pelas regras de **Invocações — Aquisição**; reservar o espaço não paga os custos de manifestação e comando. Você pode refazer a troca ao subir de nível.

Ressalva adjacente à tabela de contabilidade, sem poluir cada remissão:

> Os espaços obtidos nos marcos fazem parte desta mesma lista. Classe 0 e outras capacidades gratuitas que ficam fora dela não fornecem espaços para essa troca.

Na rota Manejo:

> Um espaço de Manejo também pode ser ocupado por uma entidade, seguindo **Fundamento — Criações conhecidas** e **Invocações — Aquisição**.

Na rota Marcial:

> Um espaço de Kata também pode ser ocupado por uma entidade, seguindo **Fundamento — Criações conhecidas** e **Invocações — Aquisição**. Os custos continuam sendo pagos com o PE da sua rota.

A discussão de esforço/energia deve ficar no parágrafo geral de equivalência da rota Marcial, não repetida toda vez que a entidade usar uma habilidade. “Criações conhecidas” é proposta de título simples; se o termo for adotado, registrar sua relação com o campo antigo “espaços de feitiço” na ficha, para não criar outra moeda.

## Por que o capítulo atual sobrecarrega a primeira leitura

1. A abertura afirma que todo personagem nasce com uma única técnica (`40:5`), contrariando imediatamente duas rotas que só serão explicadas em capítulos posteriores (`42:3;43:3`). O iniciante pode achar que escolheu errado antes de começar.
2. Nas primeiras 180 linhas, o leitor recebe pontos, oito Classes, limites, acerto, CD, fórmulas, PE, Classe 0 e conversão de d8 para d6/d12. Só em `:182` começa a escrever sua ideia. A tabela de conversão interrompe a tarefa principal e é material de consulta, não requisito de criação.
3. Quase toda explicação inicial usa dano como resultado. O primeiro exemplo (`Lança Negra`) nem apresenta a ideia de técnica que justificou suas escolhas. O bom exemplo guiado da Régua aparece somente em `:438`.
4. O procedimento diz escolher Classe, Forma, Melhorias, sobras e nome (`:427–436`); não começa pelo que o jogador quer fazer na cena. Não pede explicitar alvo, duração, resultado de resistência, término e preço de uso. A ficha vazia (`:1327–1343`) também omite vários desses campos.
5. “Forma” oscila entre formato espacial, método de acerto, finalidade e permissão fora de combate: Projétil, Cura e Efeito são escolhas de naturezas diferentes. O leitor precisa de uma porta por intenção antes da tabela completa.
6. “Classe”, “nível”, “Classe Passiva”, “nível da condição” e “marco” aparecem próximos. Deve haver um quadro curto distinguindo apenas as escalas necessárias naquele passo, sem novo glossário gigante.
7. A seção da Técnica Máxima define o resultado como golpe de dano fixo (`:964`) e ambos os exemplos são ataques (`:994–996`). A única alternativa criativa fica numa linha remetendo a uma tabela anterior (`:988`), cuja escala “Máxima” usa exemplos enormes mas não ensina testes, oposição ou como encerrar o efeito (`:927`). Isso induz dano/cura sem provar que o usuário não é criativo.
8. Os exemplos prontos foram agrupados por Classe, não por problema que resolvem. Isso ajuda procurar números depois; não ensina um iniciante a montar proteção, movimento, controle, informação ou efeito de cenário.

## Ordem de ensino recomendada

1. **Sua técnica:** um parágrafo situa aplicações e três rotas. Mostrar uma ideia simples e três objetivos possíveis, sem prometer que todos já funcionam no nível inicial.
2. **Criações conhecidas:** separar três contas em um quadro: espaço guarda uma criação; pontos montam os efeitos; PE paga cada uso. Já mostrar a opção de entidade, sem abrir o construtor dela.
3. **Criar um feitiço:** começar pela frase “Quero [resultado] sobre [alvo], de [posição/distância]”. Depois Classe disponível, Forma compatível, efeitos necessários, duração, custos e restrições. Usar o catálogo como consulta conforme o objetivo, não exigir leitura linear das nove famílias antes da primeira ficha.
4. **Exemplo completo:** um único exemplo com números, ficha final e resolução em cena. O primeiro pode ser direto, com uma Melhoria, para tornar visível a conta inteira.
5. **Outras aplicações:** três exemplos curtos da mesma técnica, com finalidades distintas. Diferenciar descrição estética, efeito pago e improvisação pequena. Não usar três ataques de cores diferentes como demonstração de criatividade.
6. **Limites e combinações:** junto do passo em que importam, oferecer pares permitidos/proibidos e motivo de uma linha. A matriz inteira fica no catálogo; repetir o critério geral, não dezenas de exceções em prosa corrida.
7. **Usar feitiços:** ação, alcance, alvo válido, requisito, PE, rolagem/resistência, duração/término. Isto ensina jogar a ficha pronta antes de aprofundar criação avançada.
8. **Técnicas avançadas:** passivas, Liberação, Máxima e demais trunfos após o ciclo comum funcionar. Para Máxima: procedimento próprio e dois exemplos sem dano bruto, com contabilidade e saída/contrajogo definidos.
9. **Consulta:** progressão, catálogos, conversão opcional de dados e ficha em branco. Manter uma origem de números e remissões curtas.

Não é necessário empurrar todo o capítulo atual para um PDF só. O lote R06 pode conter procedimento, interfaces e exemplos essenciais; o catálogo R07 deve ser sincronizado antes de apresentar o conjunto como revisado integralmente. Se R06 corrige uma incompatibilidade, registrar a linha exata que R07 herdará, para evitar que texto curto e tabela longa discordem.

## Perguntas de iniciante para testar a candidata

- Tenho nível 2: com quantas criações começo e qual Classe posso montar?
- O espaço acaba quando lanço o feitiço? Pontos e PE são a mesma reserva?
- Quero uma entidade: o que deixo de conhecer e em qual capítulo faço a ficha?
- Posso usar o espaço do marco? Posso trocar um Classe 0? Minha Kata também permite isso?
- Minha técnica movimenta papel: como descrevo uma proteção sem receber defesa gratuita só pela narrativa?
- Quero impedir alguém de sair de uma sala: escolho Efeito, Controle, terreno, condição ou parede? Que parte exige resistência?
- Quero um feitiço sem dano em combate: qual Forma admite isso, e o que acontece aos pontos que sobram?
- Posso colocar Longe em Toque? Se não, que alteração de projeto preserva a ideia sem reter uma devolução indevida?
- Se uma Restrição já está na Forma ou no Selo, conto de novo? Ela ocupa um dos dois limites?
- Trocar acerto por TR é escolha na criação ou na hora do uso? Qual TR e quais consequências existem no sucesso?
- O alcance mede distância ao centro ou o tamanho da área? Posso aumentar um sem aumentar o outro?
- Qual é a duração, como interrompo o efeito, e quando o alvo testa de novo?
- Quando Ampliar muda números e quando estou criando um efeito diferente que pede outro espaço?
- Como faço uma Máxima de resgate/controle sem simplesmente escrever “cidade inteira até desfazer”?
- Na Máxima, Forma e Melhorias reduzem o dano fixo? Posso usar uma condição de ativação que não devolve pontos?
- Quando a ficha sobe de nível, o que muda sozinho e o que exige reescrita?

Um validador útil exige que o leitor responda essas perguntas somente com o texto candidato e suas remissões previstas. Pontuação numérica não substitui a leitura de um jogador real; registrar como ensaio de compreensão enquanto for revisão por modelos.

## Exemplos mínimos para a entrega

1. **Primeira criação no nível 2:** uma ideia, escolha de família, cálculo, ficha e uma utilização com resultado de acerto/TR. Incluir a contabilidade do repertório.
2. **Mesma ideia, outro objetivo:** proteção ou controle com duração definida, sem adquirir dano/condição grátis pela descrição. Mostrar o que foi comprado e o que é apenas aparência.
3. **Criação sem combate:** Uso Livre versus Efeito pago, com um limite de alvo hostil claramente resolvido. Não usar o exemplo de ocultar passos de graça para conceder teste gratuito de Furtividade.
4. **Invocação:** reservar um dos três espaços do nível 2 e apontar a ficha no capítulo dono. Não reproduzir ali o catálogo da entidade.
5. **Combinação inválida reparada:** Toque + Longe e retorno indevido de Corpo a Corpo; mostrar por que se troca para Projétil em vez de obter alcance mantendo devolução.
6. **Ampliar:** versão conhecida e uso numa Classe superior, sem trocar de finalidade. Uma conta antes/depois é suficiente.
7. **Técnica Máxima sem dano:** resultado concreto, orçamento, ação/PE, duração, quem é afetado, como resiste/escapa/encerra. A potência tem que sair da regra proposta, não de frase vaga.
8. **Máxima combinada:** dano ou outro resultado principal mais utilidade, mostrando se o orçamento limita a largura do efeito e por que. Evitar que os dois exemplos finais voltem a ser apenas dano maior.

## Outras divergências encontradas no percurso

| Local | Achado | Destino recomendado |
|---|---|---|
| `40:421` | Diz que só Passivas e Domínio dividem espaços; omite entidade e Domínio sem Barreiras de cinco espaços. | Corrigir contabilidade agora. |
| `80:281–293` | Progressão também omite entidade. | Remissão curta na futura revisão/integridade. |
| `43:74,142` versus `03-mecanica/25-sem-tecnica.md:185–187,284` | Capítulo impede cura de terceiros na rota Sem Técnica; peça registra correção desde v0.194: vedação é da aptidão, não dos Manejos com Forma Cura. | Registrar correção de sincronização; não reintroduzir bloqueio no Fundamento. |
| `42:33` versus `42:88–100` | Primeiro afirma não ter Selo; depois define equipamento como seu Selo. | Escrever substituição do requisito em vez de ausência absoluta. |
| `40:5` versus rotas | Toda pessoa com técnica inata contradiz opções sem ela. | Ajustar abertura. |
| `40:68` | Exemplo diz duas versões do “mesmo feitiço” escolhidas conforme defesa/TR; não informa espaços nem atributo do exemplo. | Exigir ficha de versões e decisão de quando escolher resolução. |
| `40:892,905` | Uso Livre “perceber é Livre” e “abafar passos” pode ser interpretado como sentidos especiais/benefício de Furtividade gratuitos. | Conferir contra Energia e Vestígios/Furtividade recentes; benefício mecânico exige fonte. |
| `40:927,988` | Máxima não ofensiva sugere domínio narrativo absoluto e duração indefinida sem mecanismo de resistência, custo persistente ou encerramento definido. | Tratar como problema mecânico e didático, não só trocar exemplos. |

## Comparação editorial com fontes primárias

Fontes consultadas em 03/10/2026. Comparação de estrutura e de procedimento; não transporte de regras nem cópia de redação.

### D&D 2024 — Spells

Fonte oficial: https://www.dndbeyond.com/sources/dnd/br-2024/spells

O capítulo separa obtenção de magias de seu lançamento e percorre os campos que aparecem nas descrições: nível, tempo, alcance, componentes, duração e efeitos. Ele distingue aprender/preparar de gastar recursos. Para Projeto M, isso apoia apresentar repertório, construção e uso em etapas próprias. **Não importar slots de lançamento de D&D:** aqui o espaço é conhecimento, enquanto PE paga o uso. A definição dos campos na ficha é mais útil à acessibilidade do que uma longa fórmula antes de mostrar uma ficha preenchida.

### Pathfinder Player Core — Spells

Texto do livro no repositório oficial de regras: https://2e.aonprd.com/Rules.aspx?ID=2221

As entradas separam alcance, área, alvos, defesas e duração; efeitos de altura superior dizem quais aspectos mudam. Isso sustenta uma ficha de Projeto M que não esconda alcance dentro do nome da Forma e que registre resultado de sucesso/falha. O método de catalogação não exige copiar sua economia de ações, graus de sucesso ou preparo. O título inglês “Reading Spells” **não** será adaptado como “Como ler”, conforme preferência explícita do usuário.

### Fate Core — Building Stunts

Texto oficial: https://fate-srd.com/fate-core/building-stunts

A criação começa por funções reconhecíveis: permitir uma ação diferente, conceder um benefício limitado ou criar uma exceção específica. Exemplos são tratados como modelos para novas construções; o texto testa situações de uso estreitas ou amplas demais. Para Projeto M, isso apoia iniciar por intenção e mostrar o ajuste entre ideia, efeito e limite antes de abrir o catálogo inteiro. Não importar seus bônus, pontos Fate ou permissões durante a sessão.

## Registro de motivos sugerido

Para cada alteração do candidato, registrar: ID estável; fonte e linha; problema observado; antes/depois resumido; tipo (clareza, sincronização, regra nova, balanceamento); motivo; mecânicas afetadas; teste de caso; pendências. “Mais claro” sozinho não é justificativa verificável. Exemplos: “evita devolver Corpo a Corpo depois de remover seu limite”, “distingue vaga de repertório e recurso gasto”, “reproduz correção já registrada que não chegou ao capítulo”.

A futura revisão de integridade deve incluir explicitamente a mudança de **Morrendo/morte** e suas dependências: cura, estabilização, recuperação, entidades e morte do invocador, dano de alma, poderes que levantam a zero, efeitos persistentes e gasto de recursos por personagem inconsciente. Não resolver esse subsistema em Fundamento por uma frase incidental.
