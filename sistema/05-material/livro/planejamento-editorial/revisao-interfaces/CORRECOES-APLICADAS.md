# Correções aplicadas — antes, depois e motivo

Correções feitas em 04/10/2026 a partir da revisão das interfaces (`ACHADOS.md`), em quatro passadas.

- **Primeira passada (C01 a C14):** só o que diverge de um nome, custo ou remissão já aprovado em outro capítulo. Nenhuma inventa número, e todas alinham um capítulo com outro que já dizia a coisa certa. **Seis delas mudam o que acontece na mesa** para quem lia só o capítulo corrigido: C01, C07, C09, C10, C13 e C14. Cada uma traz uma linha "Muda na mesa". As outras treze são só texto.
- **Contra a `v0.331` dos jogadores, só a C14 muda regra.** As outras cinco devolvem o que a `v0.331` já dizia, por exemplo `manual/50-equipamento.md`, linha 230 (C07), `manual/60-invocacoes.md`, linha 523 (C10), e `manual/42-tecnica-marcial.md`, linha 52 (C09), ou só trocam o nome de um contador que não existia (C01). O "Muda na mesa" de cada uma compara com a candidata de antes desta revisão. A comparação com a `v0.331` é da thread "Mudanças de mecânica no livro".
- **Segunda passada (D01 a D03c e EQ25):** quatro regras que o Mizuki decidiu no mesmo dia. Essas mudam regra, e a decisão dele vai citada em cada uma.
- **Terceira e quarta passadas (D05 a D24):** mais decisões do Mizuki, os verbetes que faltavam no índice e a retirada das contas de projetista que ele pediu. Cada uma cita a decisão e diz o que muda na mesa.

O mesmo conteúdo, com o hash de cada fonte antes e depois, está em `CORRECOES-APLICADAS.json`. Caminhos relativos ao planejamento editorial.

## Como foi conferido

- **Fontes editadas:** só as declaradas em `../consolidacao/lote-01/ORDEM.json`. O `LIVRO-COMPLETO.md`, o PDF e as evidências da consolidação foram regerados pelo `gerar_livro.py --strict`, não editados à mão.
- **Estrutura:** depois da segunda passada, `conferir_livro.py` passou com 3497 checagens e 508 links internos. O PDF tem agora **384 páginas** (uma a mais, no fim de Invocações em campo), 21 capítulos e seis Caminhos.
- **PDF:** main `44dfa941…`, primeira passada `89f9057b…`, segunda passada `adda0770…`, depois da D04 `00a207c9…` (sha256 completo em `../consolidacao/lote-01/evidencias/GERACAO.json`).
- **Páginas da primeira passada:** a comparação por pixel com o PDF da `main` mudou 35 páginas: 10, 59, 87, 96, 97, 113, 116, 117, 152, 175 a 189, 214, 218, 257, 263, 281, 283, 284, 340, 360, 376 e 378. A faixa 175 a 189 é o capítulo de Equipamento: as trocas C04b, C07, C11 e C12 mudaram o comprimento de algumas linhas e o texto seguinte andou junto.
- **Páginas da segunda passada:** comparadas com o PDF da primeira passada, ignorando cabeçalho e rodapé para absorver a página a mais. Mudaram 34: 2 (sumário), 59 (C08d sem ponto e vírgula), 160 (D01), 216 (D03c), 320 a 335 (D02 e D03, com o texto de Invocações em campo andando até a página nova), 340, 342 a 344, 348, 351, 352, 355, 360 e 361 (D02b e números de página em Construir invocações) e 377 a 380 (números de página do índice). As demais são idênticas em pixel, só deslocadas uma página depois da 334.
- **Páginas da D04:** comparadas com o PDF da segunda passada, mudaram só as páginas 96 a 99, no fim da Vanguarda, porque a frase nova empurrou o texto. O livro continua com 384 páginas, e `conferir_livro.py` passou de novo com 3497 checagens e 508 links.
- **Terceira passada (D05 a D17):** o livro foi regerado com 382 páginas e 509 blocos (saiu a página Ritmo de campanha), PDF `633f85ae…`. `conferir_livro.py` passou com 3503 checagens e 526 links (os 18 verbetes novos do índice somam links). Comparado com o PDF da D04 pelo corpo da página, sem cabeçalho e rodapé: 186 páginas idênticas na mesma posição, 108 idênticas que só mudaram de posição ou de número no rodapé, e 88 com corpo diferente. Destas, 68 têm texto que andou (Dano 48 a 55, Vanguarda 96 a 98, Incursor 148, Equipamento 176 a 185 e 205, Progressão 211 a 218, Aptidões 265 a 276, Rotas 279 a 294 e índice 373 a 382) e 20 só mudaram números de página nas remissões. As 88 foram abertas: nenhum corte, sobreposição ou título solto. Registro em `../consolidacao/lote-01/evidencias/COMPARACAO-VISUAL-2026-10-04-decisoes.json`. O texto extraído do PDF não tem mais nenhum dos trechos retirados e tem cada "depois".
- **Gerador do livro e índice:** o gerador lê `consulta/lote-01/evidencias/DESTINOS.json`, uma segunda cópia do mapa do índice. Os 18 verbetes novos ficaram de fora dela na primeira tentativa, e o modo estrito parou com 18 destinos pendentes. A cópia foi sincronizada, e o auditor da Consulta passou a comparar as duas. Testes negativos desta passada em `evidencias/perturbacao-terceira-passada.txt`.
- **Quarta passada (D18 a D24):** livro regerado com 382 páginas e 509 blocos, PDF `bceea2d7…`. `conferir_livro.py` passou com 3503 checagens e 526 links. Comparado com o PDF da terceira passada: 374 páginas idênticas na mesma posição e 8 com corpo diferente (210, 217, 238, 239, 284, 303, 307 e 328). A 239 só recebeu texto que subiu da 238. As 8 foram abertas: nenhum corte, sobreposição ou título solto. Registro em `../consolidacao/lote-01/evidencias/COMPARACAO-VISUAL-2026-10-04-quarta.json`. O texto extraído do PDF não tem mais nenhum trecho retirado e tem cada "depois". Nos capítulos, mudaram 7 páginas de unidade, todas abertas. Testes negativos do auditor da Progressão em `evidencias/perturbacao-quarta-passada.txt`.
- **Cotejos da quarta passada:** Consulta, Fabricação e Construir invocações travam quando um capítulo de que dependem muda. Os diffs foram lidos e registrados (`FONTES-CANDIDATAS.json`, `fontes-concorrentes.json` e `fontes-concorrentes-finais.json`): nenhum desses capítulos reproduz os trechos retirados.
- **Inspeção:** todas as páginas mudadas nas duas passadas foram abertas uma a uma: nenhum corte de texto, sobreposição ou título órfão no pé da página. A página 334 fecha Invocações em campo com cerca de 40% de texto, o que é normal no fim de capítulo.
- **Texto do PDF:** os termos removidos ("Restringido", "Restrição Único", "Montagem de entidades", "até haver espaço") não aparecem mais, e cada "depois" abaixo aparece no texto extraído.
- **Links:** os destinos internos do PDF foram conferidos pelo `conferir_livro.py`; nenhum destino ficou pendente.
- **Validadores:** `testar_editorial.py`, o `conferir_editorial.py` e os validadores de cada unidade, nas seções do fim.
- **Prova visual completa (V14):** `../consolidacao/lote-01/evidencias/FINAL-V14.json` continua apontando para o PDF da `main`. A inspeção desta rodada cobriu só as páginas que mudaram.
- **Tudo isto é revisão por modelo.** Não é revisão humana nem playtest.

## As correções

### C01 · caminhos/emanador/lote-01/EMANADOR.md

Achados: G1-01, G4-08. Integridade é a reserva de alma das criaturas (Dano e recuperação). O estado de dano de um objeto é a Vida do objeto, em Equipamento.

**Muda na mesa:** dano na arma passa a seguir Danificar objetos, em Equipamento, e não as regras de alma.

- Antes: A arma continua sendo um item: munição, Integridade, propriedades e efeitos precisam ser registrados.
- Depois: A arma continua sendo um item: munição, Vida do objeto, propriedades e efeitos precisam ser registrados.

- Antes: Conserve Grau, Integridade e efeitos próprios compatíveis.
- Depois: Conserve Grau, Vida do objeto e efeitos próprios compatíveis.

- Antes: Cada uma mantém munição, Integridade e efeitos próprios separados.
- Depois: Cada uma mantém munição, Vida do objeto e efeitos próprios separados.

### C02 · caminhos/incursor/lote-01/INCURSOR.md

Achados: G3-01. "Restringido" não aparece em nenhuma outra fonte; Rotas, glossário e índice chamam esse personagem de Restrição Celestial sem energia.

- Antes: **Restringido.** Aplique o reforço
- Depois: **Restrição Celestial sem energia.** Aplique o reforço

### C03 · consulta/lote-01/CONSULTA.md

Achados: G3-08, G4-12. O índice já registra Leve como propriedade de arma, exigida por habilidades do Assassino; o glossário não acompanhou a sincronização R05.

- Antes: **Leve, Média e Pesada.** Nomes de faixas de preço e também de categorias de Condição. Consulte a tabela correspondente; pontos de montagem e PE não são a mesma conta. **Consulta:** Pontos e preços.
- Depois: **Leve, Média e Pesada.** Nomes de faixas de preço e também de categorias de Condição. Consulte a tabela correspondente; pontos de montagem e PE não são a mesma conta. Leve também é uma propriedade de arma, explicada em Propriedades, no capítulo Equipamento. **Consulta:** Pontos e preços.

### C04 · regras-gerais/lote-final/REGRAS-GERAIS.md

Achados: G2-01, G4-14. Sete capítulos usam Ação Completa (46 ocorrências) e o glossário e o índice mandam procurar esse nome em Turnos, onde só aparecia Rodada inteira. O glossário mantém Rodada inteira como nome anterior.

- Antes: Um custo de **Rodada inteira** consome Ação Padrão
- Depois: Um custo de **Ação Completa** consome Ação Padrão

### C04b · equipamento/lote-final/EQUIPAMENTO.md

Achados: G4-14. Mesmo motivo de C04.

- Antes: cada **Rodada inteira** dedicada a vestir
- Depois: cada **Ação Completa** dedicada a vestir

### C05 · consulta/lote-01/CONSULTA.md

Achados: G2-09. O capítulo se chama Construir invocações (ORDEM.json); Montagem de entidades não é título de nenhuma fonte.

- Antes: | Domar | Montagem de entidades: Domar uma maldição |
- Depois: | Domar | Construir invocações: Domar uma maldição |

- Antes: | Entidade | Montagem de entidades: Criar uma invocação |
- Depois: | Entidade | Construir invocações: Criar uma invocação |

- Antes: | Invocação | Montagem de entidades: Adquirir entidades |
- Depois: | Invocação | Construir invocações: Adquirir entidades |

### C06 · caminhos/vanguarda/lote-01/VANGUARDA.md

Achados: G4-02. Equipamento trocou o contador X pela capacidade (Ataques por carga) e pelo gatilho de esvaziar; a Vanguarda ainda usava X. Nas armas de fogo o número não muda.

**Caso da besta:** com a besta em capacidade 1 (EQ25), o Combate Irregular leva a besta a 2, e não a 3 como seria com a peça 14. Com 2, a besta voltaria a servir no ataque extra para esse personagem. O Mizuki decidiu que o aumento vale só para Arma de Fogo (D04, abaixo).

- Antes: O limite **X de disparos antes da recarga aumenta em um**.
- Depois: A **capacidade da arma** (os ataques por carga, em Munição) **aumenta em um**.

- Antes: Recupere **metade de X, arredondada para baixo**, sem ultrapassar o limite.
- Depois: Recupere **metade da capacidade, arredondada para baixo**, sem ultrapassar o limite.

- Antes: recuperando **uma unidade de munição**, até a capacidade X.
- Depois: recuperando **uma unidade de munição**, até a capacidade da arma.

- Antes: resolve a necessidade normal de recarga por X ou pelo gatilho natural.
- Depois: resolve a necessidade normal de recarga por esvaziar a arma ou pelo gatilho natural.

### C07 · equipamento/lote-final/EQUIPAMENTO.md

Achados: G4-03. Guia, Emanador, Evocador e a criação oferecem treino numa arma específica; lida ao pé da letra, a regra de Equipamento impunha desvantagem a esse treino.

**Muda na mesa:** quem tem treino só numa arma específica (opção da criação, do Guia, do Emanador e do Evocador) deixa de ter desvantagem com ela. Antes, ao pé da letra, tinha.

- Antes: **Sem treino na categoria**, você tem desvantagem nos ataques com aquela arma.
- Depois: **Sem treino na categoria ou naquela arma específica**, você tem desvantagem nos ataques com aquela arma.

### C08 · caminhos/vanguarda/lote-01/VANGUARDA.md

Achados: G4-04, G5-03, G5-04. Não existe seção Compras e equipamento inicial; a regra está em Equipamento inicial.

- Antes: Compre seu equipamento conforme **Compras e equipamento inicial**.
- Depois: Compre seu equipamento conforme **Equipamento inicial**, em Equipamento.

### C08b · progressao/lote-01/PROGRESSAO.md

Achados: G4-04. Mesmo motivo de C08.

- Antes: conforme **Compras e equipamento inicial**.
- Depois: conforme **Equipamento inicial**, em Equipamento.

### C08c · rotas/lote-01/ROTAS.md

Achados: G4-04, G5-03. Os destinos não existem; as seções são Sacar e guardar, Equipamento amaldiçoado e Talento Próprio.

- Antes: Sacar uma arma de reserva segue **Ações — Interagir com objetos**.
- Depois: Sacar uma arma de reserva segue **Sacar e guardar**, em Equipamento.

- Antes: Efeitos especiais de graus maiores seguem **Equipamentos amaldiçoados**.
- Depois: Efeitos especiais de graus maiores seguem **Equipamento amaldiçoado**.

- Antes: deve seguir **Catálogo de criação — Criar Talentos**,
- Depois: deve seguir **Catálogo de criação — Talento Próprio**,

### C08d · abertura/lote-01/ABERTURA-E-CRIACAO.md

Achados: G4-04. Carga é seção própria de Regras gerais; Equipamento já corrigiu a mesma remissão (EQ23).

- Antes: Modos diferentes de movimento, terreno e excesso de carga seguem Movimento.
- Depois: Modos diferentes de movimento e terreno seguem Movimento. Excesso de carga segue Carga, em Regras gerais.

Na primeira passada o depois usava ponto e vírgula. A Abertura tem uma regra própria contra ponto e vírgula, e o validador da unidade recusou; a segunda passada trocou por ponto.

### C08e · catalogo/lote-01/CATALOGO.md

Achados: G5-04. Criar um efeito e Descanso e recuperação não são títulos das fontes vigentes.

- Antes: estão em **Criar um efeito**, no Fundamento.
- Depois: estão em **Efeitos próprios**, no Fundamento.

- Antes: Recuperar os pontos segue **Descanso e recuperação**.
- Depois: Recuperar os pontos segue **Descansos**, em Dano e recuperação.

### C09 · rotas/lote-01/ROTAS.md

Achados: G4-05. Equipamento organiza armas em 13 categorias e 3 listas; "grupo" não é termo dele. A peça 20 diz "três das treze categorias de arma".

**Muda na mesa:** lendo "grupo" como as listas Simples, Marcial e Arma de Fogo, a rota dava treino em até 13 categorias. Agora são três categorias, a leitura mais estreita.

- Antes: selecione **três grupos de armas diferentes** entre os grupos de Equipamento. Você recebe uma arma de cada grupo, todas de **grau 4**, e fica treinado nos três grupos,
- Depois: selecione **três categorias de armas diferentes** entre as categorias de Equipamento. Você recebe uma arma de cada categoria, todas de **grau 4**, e fica treinado nas três categorias,

- Antes: qualquer **arma amaldiçoada de um desses grupos**,
- Depois: qualquer **arma amaldiçoada de uma dessas categorias**,

- Antes: Assim, é possível escolher um grupo de Força e outro de Destreza.
- Depois: Assim, é possível escolher uma categoria de Força e outra de Destreza.

- Antes: Começa com uma arma de grau 4 de cada grupo.
- Depois: Começa com uma arma de grau 4 de cada categoria.

- Antes: | Selo | Usar uma arma amaldiçoada de um dos três grupos. |
- Depois: | Selo | Usar uma arma amaldiçoada de uma das três categorias. |

### C10 · invocacoes/lote-02/CONSTRUIR-INVOCACOES.md

Achados: G4-09. Equipamento define teto de Destreza zero para Revestimentos; a fórmula da entidade somava a Destreza inteira.

**Muda na mesa:** a entidade de Revestimento perde a Destreza na Defesa, porque o teto dessa peça é 0. Antes somava a Destreza inteira.

- Antes: a Defesa usa **10 + Destreza da entidade + proteção do equipamento**.
- Depois: a Defesa usa **10 + Destreza da entidade permitida pelo teto da peça + proteção do equipamento**.

### C11 · equipamento/lote-final/EQUIPAMENTO.md

Achados: G4-15. No mesmo capítulo Rina tem Força 0, e o escudo Médio exige Força 3; pela regra de requisitos ela não receberia a proteção.

- Antes: Sua Defesa é 10 + 4 + 2 = **16**. Com um escudo Médio, recebe mais 2 de proteção, mas só pode contar 3 de Destreza: 10 + 3 + 2 + 2 = **17**.
- Depois: Sua Defesa é 10 + 4 + 2 = **16**. Com um Broquel, recebe mais 1 de proteção: 10 + 4 + 2 + 1 = **17**. Um escudo Médio exigiria Força 3; com ele, ela só poderia contar 3 de Destreza.

### C12 · equipamento/lote-final/EQUIPAMENTO.md

Achados: G4-13. Duas propriedades das tabelas de armas são explicadas fora da página Propriedades.

- Antes: | Propriedades | Benefícios e restrições, explicados em [Propriedades](#eq-propriedades). |
- Depois: | Propriedades | Benefícios e restrições, explicados em [Propriedades](#eq-propriedades); Volumosa e Embainhada estão em Armas escondidas. |

### C13 · caminhos/emanador/lote-01/EMANADOR.md

Achados: G5-01. Nenhuma fonte define Restrição Único; a Restrição de frequência do Catálogo é Uma Vez.

**Muda na mesa:** "Restrição Único" não existia, então na prática não havia limite. Agora vale o limite de frequência da Restrição Uma Vez, do Catálogo.

- Antes: como a Restrição Único.
- Depois: como a Restrição Uma Vez.

### C14 · progressao/lote-01/PROGRESSAO.md

Achados: G5-06. Fundamento diz que trocar função, Forma ou peças da Técnica Máxima usa a revisão ao subir de nível (FU-44), mas a lista de Progressão não a incluía.

**Muda na mesa:** a Técnica Máxima passa a poder ser revista ao subir de nível. Antes a lista da Progressão não deixava.

- Antes: Você pode reescrever **um feitiço conhecido**, incluindo uma Liberação Máxima, ou rever
- Depois: Você pode reescrever **um feitiço conhecido**, incluindo uma Liberação Máxima, a **Técnica Máxima**, ou rever

## Decisões do autor (segunda passada)

O Mizuki decidiu quatro achados em 04/10/2026, e depois o caso da besta com Combate Irregular (D04). A besta ficou como estava; as outras mudaram texto. O que a `v0.331` dos jogadores diz diferente está em `../migracao-pos-candidata/PLANO.md`, na seção das decisões.

### EQ25 · equipamento/lote-final (sem mudança de texto)

Achado: G4-01. Mizuki: "Volta pra 1, a parte negativa da besta é justamente não funcionar no ataque extra".

- Antes: capacidade 1 das bestas sem registro de decisão nesta unidade; a peça 14 da `v0.331` usa 2.
- Depois: capacidade 1 mantida. O registro foi para `equipamento/lote-final/ALTERACOES.md` (EQ25). A peça 14 muda na migração.

Efeito na Vanguarda: ver D04.

### D01 · caminhos/incursor/lote-01/INCURSOR.md

Achado: G3-07. Mizuki: "só especificar que o segundo ataque tem de ser uma arma de arremesso ou corpo a corpo".

- Antes: Pode combinar ataques corpo a corpo e arremessos, usar a mesma arma ou armas diferentes…
- Depois: O segundo ataque precisa ser corpo a corpo ou um arremesso, e nunca um disparo de arma de fogo ou de besta. Pode combinar ataques corpo a corpo e arremessos, usar a mesma arma ou armas diferentes…

### D02 e D02b · Invocações em campo e Construir invocações

Achado: G2-04. Mizuki: "Elas tem classe 0 e a possibilidade de terem armas reais". O acerto com arma segue o que a peça 15 já decidia: a arma muda o acerto e nunca a CD, e a entidade não tem treino em armas.

Acrescentado em **Invocações em campo**, logo depois da lista de ações da atuação básica:

> Para Atacar, num revide ou num ataque comum concedido, a entidade usa a **básica ofensiva de Classe 0** da ficha ou uma **arma que ela empunhe**. O acerto com arma está em **Construir invocações — Acerto e dificuldade**. Sem nenhuma das duas, ela não ataca.

Acrescentado em **Construir invocações**, depois de "A maestria é sempre a do invocador…":

> Com uma arma empunhada, o ataque usa o atributo que a arma pede no lugar do atributo de acerto. A CD das habilidades não muda. A entidade não tem treino em armas, então ataca com elas com desvantagem. O dano é o da arma, conforme **Equipamento**.

E, no fim de "Uma capacidade ofensiva precisa estar montada na ficha para que seja usada como ataque próprio.": "A outra forma de atacar é com uma arma empunhada, conforme **Acerto e dificuldade**."

### D03, D03b e D03c · corpos excedentes

Achado: G2-03. Mizuki escolheu "Volta com trava": o corpo excedente volta sozinho quando a vaga abre por perda (corpo destruído ou limite que sobe), e soltar um corpo de propósito não puxa outro de volta.

- Invocações em campo, antes: Corpos adicionais precisam ser deixados sem seu controle até haver espaço. Não desaparecem nem são destruídos por essa escolha.
- Depois: Corpos adicionais precisam ser deixados sem seu controle. Não desaparecem nem são destruídos por essa escolha. Um corpo deixado assim volta ao seu controle quando uma vaga se abre porque um corpo controlado foi destruído ou porque seu total permitido aumentou. Deixar um corpo sem controle de propósito não abre vaga para trazer outro de volta.
- Fabricação, antes: …permanece no mundo sem controle até haver espaço; fabricar ou receber outro não amplia esse limite.
- Depois: …permanece no mundo sem controle e volta conforme **Invocações em campo**; fabricar ou receber outro não amplia esse limite.
- Progressão, antes: Recuperar o controle de um corpo suspenso exige uma aquisição ou transferência de vínculo permitida, com os procedimentos de **Fabricação de entidades** e os limites de **Invocações em campo**. Estar perto dele ou voltar à cidade não permite alternar gratuitamente o grupo controlado.
- Depois: Um corpo suspenso volta ao seu controle quando uma vaga se abre porque um corpo controlado foi destruído ou porque seu total permitido aumentou, conforme **Invocações em campo**. Soltar um corpo de propósito, estar perto do suspenso ou voltar à cidade não permite alternar o grupo controlado.

### D04 · caminhos/vanguarda/lote-01/VANGUARDA.md

Achado: efeito da C06 sobre G4-01. Mizuki, no cartão: "Só arma de fogo".

- Antes: A **capacidade da arma** (os ataques por carga, em Munição) **aumenta em um**.
- Depois: A **capacidade da Arma de Fogo** (os ataques por carga, em Munição) **aumenta em um**. Bestas e outras armas de disparo não recebem esse aumento.

A outra parte do Combate Irregular (disparar sem a desvantagem por inimigo adjacente) não mudou. O auditor da Vanguarda ganhou uma checagem para essa frase, testada por perturbação: tirar a frase das bestas faz a checagem falhar.

Cada unidade tocada ganhou a entrada correspondente no seu `ALTERACOES` (INC-22, R11-50, R11-51, R12-32, FAB-REV-01, PRO37 e VG-REV-01), com antes, depois e motivo.

## Decisões do autor (terceira passada) e retiradas pedidas

Em 04/10/2026, o Mizuki respondeu às seis prioridades do quadro de achados e pediu para tirar do livro do jogador as contas de projetista. Cada unidade tocada ganhou a entrada no seu `ALTERACOES` (A33, DR33, PRO38 a PRO40, VG-REV-02, EQ26, EQ27, INC-23, INC-24, R10-33 a R10-35 e R23-31).

### D05 · dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md

Achado: G1-05. Mizuki: "Entra Antes".

- Antes: Ao chegar a **zero de vida**, você está **Morrendo**. Escolha imediatamente **Aguentar** ou **Insistir**.
- Depois: Ao chegar a **zero de vida**, você está **Morrendo**. Resolva primeiro as capacidades disparadas pela própria queda; em seguida, escolha **Aguentar** ou **Insistir**. Se uma dessas capacidades encerrar a queda, não há escolha.
- Muda na mesa: só duas capacidades disparam nesse momento. Com Ainda Há Tempo (Guia), o aliado levanta antes de escolher e não paga o 1/8 de vida máxima do Insistir. Com Ainda de Pé (Bastião), a cura entra como tratamento antes da escolha; se chegar a 20% do máximo de referência, ele levanta sem escolher.

### D06 · progressao/lote-01/PROGRESSAO.md

Achado: G1-07. Mizuki: "Remove da lista".

- Antes: registre **um dos oito feitos abaixo**…; linha "Terminar a missão depois de outro personagem jogador chegar ao estágio 4."
- Depois: registre **um dos sete feitos abaixo**…; a linha saiu. Como era a última, a "ferramenta do sétimo feito" continua certa.
- Muda na mesa: o limiar do nível 20 tem sete feitos possíveis.

### D07 · caminhos/vanguarda/lote-01/VANGUARDA.md

Achado: G4-07. Mizuki perguntou se a liberação narrativa tinha sido removida; não foi (Equipamento restrito: "Grau 2 ou autorização prévia", combinada com o mestre). Escolheu a opção B.

- Acrescentado em Batedor: Arma de Fogo: **Acesso.** Armas de fogo exigem Grau 2 ou autorização prévia, conforme Equipamento restrito. Sem esse acesso, confirme a autorização com o mestre antes de escolher esta rota.
- Muda na mesa: nenhuma regra nova. A frase diz quando a autorização é combinada.

### D08 · equipamento/lote-final/EQUIPAMENTO.md

Achado: G3-03. Mizuki: opção A.

- Acrescentado em Sacar e guardar: Duas capacidades que troquem essa manipulação gratuita por duas não se somam. Em cada turno, use uma delas, com as restrições dela.
- Muda na mesa: um Malabarista com Maldição do Inventário continua com duas manipulações gratuitas por turno, não três.

### D09 e D10 · caminhos/incursor/lote-01/INCURSOR.md

Achados: G3-04 e G3-05. Mizuki: opção A nos dois.

- D09, acrescentado em Fluidez: No combate, o primeiro intervalo vai do início do combate até o começo do seu primeiro turno, inclusive para Passo Guardado.
- D10, antes: Após rolar o d20, antes de finalizar o ataque, gaste Fluidez…
- D10, depois: Após rolar o d20 e antes de o alvo escolher entre a Defesa e Bloquear, gaste Fluidez…
- Muda na mesa: o Incursor pode ganhar Fluidez quando um inimigo erra antes do primeiro turno dele. O Instante Decisivo é declarado sem saber se o alvo vai bloquear.

### D11 · equipamento/lote-final/EQUIPAMENTO.md

Achado: G1-02. Mizuki: opção B, "Pq o dano do cisão é na alma, literalmente dano na alma".

- Antes: O dano dos ataques com esta arma atinge **somente a Integridade** do alvo, seguindo as regras de dano direto à alma.
- Depois: O dano dos ataques com esta arma é **dano de Alma** e atinge **somente a Integridade** do alvo, conforme Receber dano de Alma, em Dano na alma.
- Dano e recuperação não mudou: ele já conserva a exceção "atinge somente Integridade".
- Muda na mesa: resistência a Cortante não reduz o golpe à metade; imunidade a Alma o impede; criatura sem alma só é afetada se uma regra permitir.
- O auditor do Equipamento compara cada ferramenta especial com o lote-08. Ele passou a aplicar só esta troca decidida e exigir o resto idêntico.

### D12 · rotas/lote-01/ROTAS.md

Achado: G5-02. Mizuki: opção B.

- Retirado de Talentos marciais: "Calo — Livre" e seu parágrafo.
- Técnica Marcial, passo 1, antes: Escreva a **Descrição** e a **Regra** pelo procedimento de Fundamento.
- Depois: Escreva a **Descrição**, a **Regra** e a **Expressão da técnica** pelo procedimento de Fundamento.
- Muda na mesa: Calo deixa de existir. O personagem marcial tem a Expressão da técnica do Fundamento, que também não tem efeito mecânico. Sem Técnica não recebeu frase nova; fica para o Mizuki confirmar. Confirmado depois: D18.

### G5-10 · sem mudança

Mizuki: "Mantém". Os três sentidos de "Impulso" e a família "Expressão" ficam como estão, inclusive "Impulso Energético" na introdução do Catalisador.

### D13 · consulta/lote-01/CONSULTA.md

Achados: G2-09, G4-12 e G5-11, sem decisão de regra.

- O índice foi de 268 para 286 verbetes: Auge, Carregar (Restrição), Desligada, Discreta, Embainhada, Escudo, Manutenção (entidades), Ordens pendentes, Recarregar, Recolher, Regra Própria, Religar, Retorno, Revestimento, Sacar e guardar, Segura, Talismã e Traje.
- As 11 páginas foram recompostas pelo script que reproduz byte a byte o índice anterior, com 26 linhas cada. Continuam 11; os títulos de faixa mudaram de E em diante. O auditor da Consulta passou a esperar 286.

### D14 a D17 · retiradas pedidas pelo Mizuki

Pedido: "remova essas informações que são completamente desnecessárias para o jogador… mostrar o como vc termina, rotas, tempo".

- D14, Aptidões, Progressão de Refino: saiu a tabela "Nunca escolhe Refino / Sempre escolhe Refino" e a frase sobre a última coluna. A regra do marco ficou.
- D15, Progressão: saiu a página Ritmo de campanha, com a estimativa em meses. A Progressão vai de 14 para 13 páginas. O modelo de tempo continua no auditor da unidade, como conta de projeto.
- D16, Progressão, Ganhos de Leque: saiu "Escolher Leque em todos os sete marcos termina em sete aplicações adicionais e sete Talentos concedidos, além do repertório comum." O exemplo do nível 6 ficou.
- D17, Rotas, Lapidação: saiu "Quem escolhe Lapidação em todos os marcos… Quem nunca a escolhe termina em Lapidação 8…". A regra do teto ficou.
- Muda na mesa: nada. São projeções, não regras.

## Quarta passada: Sem Técnica e contas de projetista

Em 04/10/2026, o Mizuki confirmou que Sem Técnica também anota a Expressão da técnica e pediu para tirar as duas frases de bastidor da Progressão, "e qualquer coisa semelhante". Cada unidade tocada ganhou a entrada no seu `ALTERACOES` (R10-36, PRO41, PRO42, RP-33, R08-34, FU-57 e R11-52).

### D18 · rotas/lote-01/ROTAS.md

Fecha a pendência deixada pela D12. Mizuki: "Sim ele pode anotar".

- Sem Técnica, passo 3, antes: Defina sua Regra, atributo e Selo pelo procedimento de Fundamento.
- Depois: Defina sua Regra, atributo, Selo e **Expressão da técnica** pelo procedimento de Fundamento.
- Muda na mesa: o personagem Sem Técnica escreve uma Expressão da técnica, como a Técnica Marcial. Ela não tem efeito mecânico.
- Contra a `v0.331`: devolve o que ela já dizia. `livro/manual/43-sem-tecnica.md`, linha 103, dá a Passiva Livre de graça na Sem Técnica, e Passiva Livre é o nome antigo da Expressão da técnica.

### D19 a D24 · contas de projetista retiradas

Critério usado na varredura das 23 fontes: sai a frase que só mostra uma conta de projeto sobre a regra (total acumulado, tempo de campanha, média de dano, diferença de probabilidade) e não muda o que o jogador faz na mesa. Fica o que o jogador usa para decidir ou para seguir um exemplo.

- D19, Progressão, Subir de nível: saiu "Partindo do nível 2, chegar ao 20 exige 14.300 XP gastos. Do 20 ao 30, são mais 16.400, totalizando 30.700 XP. O feito do limiar e o limite de um avanço por missão continuam necessários." O limite de um avanço por missão continua no começo do capítulo, e o feito do limiar na página dele.
- D20, Progressão, Recompensa por mestrar: saiu "A frequência esperada desse bônus é X dividido pela média de missões mestradas por mês" e o exemplo "Com X igual a 12… uma marca leva cerca de quatro meses…". A regra da marca ficou.
- D21, Ritual, Treino e prática: saiu ": a diferença é de 10 pontos percentuais com maestria 2, 15 com maestria 3 e 20 com maestria 4…". Ficou "Sem treino, a maestria permanece na CD, mas não entra na rolagem."
- D22, Poderes avançados, exemplo da Galeria de Vidro: saiu "A média bruta é 108, distribuída no tempo e antes das defesas."
- D23, Fundamento, exemplo Fenda de Arrasto: saiu "Os 24d8 causam média de 108 de dano. Role os dados normalmente."
- D24, Invocações em campo, exemplo da Máxima da domada: "Uma Forma de cura usa 19d8, com média de 85,5 PV antes dos limites aplicáveis." virou "Uma Forma de cura usa 19d8."
- Ficaram, de propósito: a tabela de custo por nível e a frase que explica que ela não mostra XP acumulado (Progressão), o "65% de chance" do exemplo de Ritual (é o que o jogador pesa antes de tentar), os 77 PE do exemplo de Aptidões (custo que ele vai pagar), a média de 14d8 no exemplo da Sala de Trégua (explica por que o exemplo usa 63 fixo) e a coluna "Efeito esperado" dos graus de ferramenta (descreve o que cada grau entrega).
- Muda na mesa: nada. São contas, não regras.
- O auditor da Progressão conferia a presença de "14.300" no texto. Agora confere uma linha da tabela de custo (a curva continua conferida linha a linha) e acusa se o total ou o prazo voltarem.

## Quinta passada: os 18 achados restantes

Em 04/10/2026, o Mizuki respondeu às 18 decisões que faltavam, aceitando a sugestão em todas. Na 9, acrescentou que a permissão do mestre pode conceder o acesso. Na 12, lembrou que os feitiços do personagem continuam mais fortes que os das invocações: a decisão só alinha a leitura do teto em área. Cada unidade tocada ganhou a entrada no seu `ALTERACOES`.

### D25 a D31 · invocacoes/lote-01/INVOCACOES-EM-CAMPO.md e Evocador

- D25 (G1-03), Integridade a zero: a entidade com alma cai sem ser destruída, como a zero de vida. O retorno exige pelo menos 1 de Integridade, que volta pelo descanso longo ou por capacidade que a restaure. Os estágios de Integridade valem para ela: PE adicional e teto de Classe nas especiais que executa.
- D26 (G2-02), domada que não pode ser recolhida: segue o modo dos corpos amaldiçoados, ativa ou inativa no mundo, e conta no total de corpos mantidos.
- D27 (G2-05): recolher, desativar ou cair a zero encerra a concentração da entidade.
- D28 (G2-06): a substituta de uma troca pode ser uma entidade caída, pagando o retorno no lugar da entrada. "O retorno não fornece básica" virou "O retorno não cria uma básica própria. Feito numa troca, ainda permite receber a básica transferida."
- D29 (G2-07 e G4-10): a entidade segue o limite geral de carga de 5 + Força, contando o que veste, empunha ou leva. O talento de transporte libera armazenamento e passageiros dentro desse mesmo limite, e levar personagens continua exigindo o talento.
- D30 (G2-08): a entidade pode preparar um deslocamento, que usa o Movimento que ainda lhe resta e não concede metros novos.
- D31 (G2-10): "reserva" ficou só para o PE da domada. A entidade guardada é "recolhida" (Invocações em campo, três frases, e Evocador, Formação Renovada).
- Muda na mesa: entidade com alma pode cair por dano na alma e não volta no mesmo dia sem recuperar Integridade. Concentração de entidade não sobrevive à saída. Equipamento da entidade passa a contar na carga dela. As demais só escrevem o que faltava.

### D32 · poderes-avancados/lote-01/PODERES-AVANCADOS.md

G1-06. A lista de encerramento do domínio, com barreira e sem barreira, ganhou "fica Inconsciente ou Derrotado".
- Muda na mesa: quem cai por Integridade ou dorme por um efeito perde o domínio na hora.

### D33 · rotas/lote-01/ROTAS.md

G4-06, opção B, com a ressalva do Mizuki sobre a permissão do mestre.
- Rota de Armas, acrescentado: **Acesso.** Escolha qualquer arma da categoria que seu acesso permita. As armas recebidas seguem Equipamento restrito: Arma de Fogo exige Grau 2 ou autorização prévia do mestre. Uma arma de fogo recebida vem com a munição inicial de uma compra, conforme Munição inicial.
- Rota de Ferramenta, acrescentado: os números de Revestimento 2 ou 3 seguem o acesso de Equipamento restrito, salvo permissão do mestre.
- Muda na mesa: a Técnica Marcial começa com o mesmo acesso de qualquer personagem, e o mestre pode liberar antes.

### D34 · ritual-e-pactos/lote-01/RITUAL-E-PACTOS.md

G5-08. Na Técnica Máxima com Ritual completo, use a maior Classe como Classe do feitiço no teste, na penalidade de falha e nas Melhorias de Ritual.

### D35 · fundamento/lote-01/FUNDAMENTO.md

G5-09. No Classe 0, a exigência de Toque ou Aura não ocupa a vaga da Restrição Leve, como já valia para as entidades.

### D36 · invocacoes/lote-02/CONSTRUIR-INVOCACOES.md

G5-05. O teto de 4 × Classe das especiais segue o Fundamento (FU-27): some os dados da montagem uma vez, sem multiplicar pelo número de criaturas na área. As especiais continuam com as escalas próprias das entidades, abaixo das do personagem.

### D37 e D38 · dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md

- D37 (G5-07), Lento: distâncias concedidas por capacidades, como a de Passo, também caem pela metade.
- D38 (G1-04): "Inimigos e entidades seguem suas próprias regras de derrota" virou "Entidades seguem Invocações em campo. Um inimigo a zero de vida ou de Integridade é derrotado, e o mestre descreve o desfecho, como morte, fuga ou exorcismo, salvo uma regra da ficha dele."

### D39 e D40 · caminhos/incursor/lote-01/INCURSOR.md

- D39 (G3-02): Quebrar o Compasso só vale durante seu turno. Golpe Cirúrgico e Cortar a Fuga dizem "Antes do nível 19, só durante seu turno".
- D40 (G3-06): Trajetória Perfeita usa "arma de uma mão com Longo Alcance de arremesso" (o Punhal e as quatro da categoria Arremesso).

### D41 · Abertura e Consulta

G4-11. O passo 5 da criação, a seção Equipamento e valores e a Ficha pronta pedem a situação, o TR e as perícias do Traje. Na ficha de repertório, a coluna de posição virou "Posição e recursos" e entrou a linha "Traje — situação, TR e perícias". Para a ficha continuar numa página, o traço da linha "Vestido, empunhado ou guardado" ficou mais curto.

## Sexta passada: o nível 7 da Vanguarda

### D42 · caminhos/vanguarda/lote-01/VANGUARDA.md

Em 05/10/2026, o Mizuki notou que a Vanguarda era o único Caminho com uma habilidade só no nível 7. A Não Pega da peça 06 (o Evasion do 5e: num efeito de TR para metade, sucesso anula e falha vira metade) não tinha chegado à candidata. Ele achou a Não Pega forte e pediu uma ideia nova. Rerrolar TR também ficou de fora, porque repetiria a Não Cede do nível 15. O texto é dele: "Execução Preparada: 1× por Sequência, ao Concluir depois de duas ou mais Conduções, imponha −1 a um TR adicional da Conclusão."

- Tabela de progressão: "Ataque Extra" virou "Ataque Extra e Execução Preparada".
- Acrescentado, depois do Ataque Extra: **Nível 7: Execução Preparada.** Uma vez por Sequência, ao Concluir depois de **duas ou mais Conduções acertadas**, imponha **−1 a um TR adicional da Conclusão**.
- "Acertadas" vem da Conclusão Dupla do nível 30, que usa a mesma condição. O nome passou na triagem do `conferir-nomes.py` (LIVRE).
- Muda na mesa: a partir do nível 7, uma vez por Sequência, a Conclusão que vem depois de duas ou mais Conduções acertadas impõe −1 a mais um TR, além do que ela já impõe.
- Unidade: `VG-REV-03` e `VG-REV-04` no `ALTERACOES` da Vanguarda. A peça 06 ainda diz Não Pega; a migração está em `../migracao-pos-candidata/PLANO.md`.

## Validador editorial

| Situação | Achados do `conferir_editorial.py` nos manuscritos alterados |
|---|---|
| `main`, antes das correções | 5 (Incursor 2, Construir invocações 3) |
| Logo depois da primeira passada | 60 |
| Hoje, depois das duas passadas e das renovações abaixo | 0 |

Os achados novos não vinham do texto novo. Cada manuscrito tem um `LOCALIZACAO-EDITORIAL.json`, na pasta de evidências da unidade, com as citações de nomes de outros capítulos já revisadas, e essa revisão só vale para o hash exato do texto. Ao mudar uma palavra, o hash muda e as exceções já aprovadas voltam a acusar. Todas coincidem, em termo e trecho, com exceções já revisadas.

Em cada manuscrito alterado, os trechos trocados foram relidos: nomes, remissões ou a regra decidida pelo autor, sem regra de outro capítulo copiada e sem título mudado. A revisão foi renovada com o hash novo e um registro `revisao_delta_2026_10_04`, que diz o hash anterior, as correções e que é revisão por modelo.

Cinco deles (Incursor, Catálogo, Equipamento, Construir invocações e Regras gerais) **já estavam com a revisão desatualizada na `main`**. A revisão registrada era de uma versão anterior ao fechamento da integração, guardada em `../consolidacao/lote-01/evidencias/antes-fechamento-integracao/fontes/`. O diff entre essa versão e a `main` é só redação de remissão ("desta página" para "desta seção", links para âncoras), e foi relido nesta rodada junto com as correções. O registro de delta desses cinco diz isso e guarda o hash da revisão antiga.

## Validadores das unidades

Cada capítulo tem um `conferir.py` que compara o PDF da unidade com o manuscrito e exige revisão editorial, inspeção visual e auditoria de regras do hash atual. Todos os 13 capítulos que esta rodada mexeu estão verdes:

| Capítulo | Na `main` | Agora |
|---|---|---|
| Abertura | quebrado (caminhos absolutos do HD do Mizuki) | verde |
| Emanador, Vanguarda, Rotas, Progressão, Invocações em campo | verde | verde |
| Incursor, Catálogo, Equipamento, Construir invocações, Regras gerais | vermelho (revisão editorial desatualizada) | verde |
| Consulta | vermelho (donos mudados sem cotejo) | verde |
| Fabricação | quebrado (Perícias mudada sem cotejo) | verde |

O que foi feito em cada um:

- **PDF da unidade regerado** pelo `gerar_pdf.py` da unidade, só com o caminho da fonte tipográfica trocado em memória para a cópia do repositório. A regeração da `main` com esse mesmo método saiu idêntica em pixel ao PDF guardado.
- **Inspeção visual por delta**, o mesmo método que o projeto já usa: as páginas que mudaram foram abertas, e as outras reaproveitam a inspeção anterior só por igualdade de pixel. Cada unidade tem um `COMPARACAO-VISUAL-2026-10-04.json` na pasta de evidências (por exemplo `../caminhos/incursor/lote-01/evidencias/COMPARACAO-VISUAL-2026-10-04.json`) com o hash do PDF anterior, o atual e as páginas abertas.
- **Auditoria de regras reexecutada** (`auditar.py`), sem desligar checagem nenhuma. Onde ela já passava, a saída da `main` foi mantida com o hash novo e um registro de delta.

Ajustes nos auditores e nas evidências, cada um com o motivo:

- `../abertura/lote-01/auditar.py`, linha 22, e `../abertura/lote-01/evidencias/fontes-preservadas.json`: os caminhos eram absolutos, da pasta do HD do Mizuki, e o validador quebrava em qualquer outro computador. Passaram a ser relativos à raiz do repositório. Os hashes esperados são os mesmos.
- `../equipamento/lote-final/auditar.py`, linha 152: a checagem procurava a frase "Rodada inteira", que a correção C04b trocou por "Ação Completa". A checagem continua a mesma, com o termo novo.
- `../invocacoes/fabricacao/lote-01/auditar.py`, linha 114: a checagem "Corpo excedente não ganha controle" procurava "até haver espaço". Agora procura a remissão para Invocações em campo e "não amplia esse limite". Foi testada por perturbação: trocar "não amplia" faz a checagem falhar.
- **Auditores que mudavam a evidência só por rodar de novo (04/10/2026, depois da quarta passada).** Cada `auditar.py` dos 23 capítulos foi rodado três vezes numa cópia, com sementes de embaralhamento diferentes (`PYTHONHASHSEED` 0, 1 e 2). Dezoito deram sempre a evidência que está no repositório. Cinco não:
  - Abertura, Catálogo, Regras gerais e Construir invocações regravavam `regras-verificadas.json` sem o bloco `revisao_delta_2026_10_04`, que é a anotação da revisão escrita depois da auditoria. Agora o auditor conserva os blocos `revisao_delta` que já estão no arquivo.
  - Equipamento gravava conjuntos com `str()`, e a ordem dos nomes mudava a cada execução. Agora os conjuntos saem como lista ordenada. A evidência dele mudou uma vez, só nessa forma.
  - Depois do conserto, os cinco dão a mesma saída nas três sementes, igual à do repositório (o Equipamento, igual à nova forma). Registro em `evidencias/estabilidade-auditores-2026-10-04.txt`.
- **Cotejos de fontes concorrentes.** Três auditores travam quando um capítulo de que dependem muda sem cotejo registrado. Nos três, o diff foi lido e registrado com o hash anterior e o motivo:
  - Fabricação (`../invocacoes/fabricacao/lote-01/evidencias/fontes-concorrentes.json`): Perícias trocou três vezes "desta página" por "desta seção" no fechamento; Invocações em campo e Construir invocações mudaram por D02, D02b e D03.
  - Construir invocações (`../invocacoes/lote-02/evidencias/fontes-concorrentes-finais.json`): Fundamento e Catálogo, só remissões (fechamento e C08e).
  - Consulta (`../consulta/lote-01/evidencias/FONTES-CANDIDATAS.json`): 17 donos. A Consulta só reproduzia dois dos trechos mudados, Leve (C03) e o rótulo de capítulo do índice (C05), e os mapas `GLOSSARIO.json` e `INDICE.json` foram atualizados para eles.

Cinco capítulos que esta rodada **não** mexeu continuam vermelhos como na `main`: Aptidões, Fundamento, Origens, Perícias e Poderes avançados. A origem é a mesma dos cinco acima: o fechamento da integração mudou o texto, e o PDF da unidade, a revisão editorial e a auditoria de regras não acompanharam. Eles ficaram fora porque nenhuma correção passou por eles. Foram atualizados depois, pelo mesmo método e sem mudar o texto: ver `../publicacao-github/provas-cinco-capitulos-2026-10-04/LEIA-ME.md`.
