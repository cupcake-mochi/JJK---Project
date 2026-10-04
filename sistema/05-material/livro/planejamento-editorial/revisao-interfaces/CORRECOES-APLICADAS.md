# Correções aplicadas — antes, depois e motivo

Correções feitas em 04/10/2026 a partir da revisão das interfaces (`ACHADOS.md`), em duas passadas.

- **Primeira passada (C01 a C14):** só o que diverge de um nome, custo ou remissão já aprovado em outro capítulo. Nenhuma inventa número, e todas alinham um capítulo com outro que já dizia a coisa certa. **Seis delas mudam o que acontece na mesa** para quem lia só o capítulo corrigido: C01, C07, C09, C10, C13 e C14. Cada uma traz uma linha "Muda na mesa". As outras treze são só texto.
- **Contra a `v0.331` dos jogadores, só a C14 muda regra.** As outras cinco devolvem o que a `v0.331` já dizia, por exemplo `manual/50-equipamento.md`, linha 230 (C07), `manual/60-invocacoes.md`, linha 523 (C10), e `manual/42-tecnica-marcial.md`, linha 52 (C09), ou só trocam o nome de um contador que não existia (C01). O "Muda na mesa" de cada uma compara com a candidata de antes desta revisão. A comparação com a `v0.331` é da thread "Mudanças de mecânica no livro".
- **Segunda passada (D01 a D03c e EQ25):** quatro regras que o Mizuki decidiu no mesmo dia. Essas mudam regra, e a decisão dele vai citada em cada uma.

O mesmo conteúdo, com o hash de cada fonte antes e depois, está em `CORRECOES-APLICADAS.json`. Caminhos relativos ao planejamento editorial.

## Como foi conferido

- **Fontes editadas:** só as declaradas em `../consolidacao/lote-01/ORDEM.json`. O `LIVRO-COMPLETO.md`, o PDF e as evidências da consolidação foram regerados pelo `gerar_livro.py --strict`, não editados à mão.
- **Estrutura:** depois da segunda passada, `conferir_livro.py` passou com 3497 checagens e 508 links internos. O PDF tem agora **384 páginas** (uma a mais, no fim de Invocações em campo), 21 capítulos e seis Caminhos.
- **PDF:** main `44dfa941…`, primeira passada `89f9057b…`, segunda passada `adda0770…`, depois da D04 `00a207c9…` (sha256 completo em `../consolidacao/lote-01/evidencias/GERACAO.json`).
- **Páginas da primeira passada:** a comparação por pixel com o PDF da `main` mudou 35 páginas: 10, 59, 87, 96, 97, 113, 116, 117, 152, 175 a 189, 214, 218, 257, 263, 281, 283, 284, 340, 360, 376 e 378. A faixa 175 a 189 é o capítulo de Equipamento: as trocas C04b, C07, C11 e C12 mudaram o comprimento de algumas linhas e o texto seguinte andou junto.
- **Páginas da segunda passada:** comparadas com o PDF da primeira passada, ignorando cabeçalho e rodapé para absorver a página a mais. Mudaram 34: 2 (sumário), 59 (C08d sem ponto e vírgula), 160 (D01), 216 (D03c), 320 a 335 (D02 e D03, com o texto de Invocações em campo andando até a página nova), 340, 342 a 344, 348, 351, 352, 355, 360 e 361 (D02b e números de página em Construir invocações) e 377 a 380 (números de página do índice). As demais são idênticas em pixel, só deslocadas uma página depois da 334.
- **Páginas da D04:** comparadas com o PDF da segunda passada, mudaram só as páginas 96 a 99, no fim da Vanguarda, porque a frase nova empurrou o texto. O livro continua com 384 páginas, e `conferir_livro.py` passou de novo com 3497 checagens e 508 links.
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
- **Cotejos de fontes concorrentes.** Três auditores travam quando um capítulo de que dependem muda sem cotejo registrado. Nos três, o diff foi lido e registrado com o hash anterior e o motivo:
  - Fabricação (`../invocacoes/fabricacao/lote-01/evidencias/fontes-concorrentes.json`): Perícias trocou três vezes "desta página" por "desta seção" no fechamento; Invocações em campo e Construir invocações mudaram por D02, D02b e D03.
  - Construir invocações (`../invocacoes/lote-02/evidencias/fontes-concorrentes-finais.json`): Fundamento e Catálogo, só remissões (fechamento e C08e).
  - Consulta (`../consulta/lote-01/evidencias/FONTES-CANDIDATAS.json`): 17 donos. A Consulta só reproduzia dois dos trechos mudados, Leve (C03) e o rótulo de capítulo do índice (C05), e os mapas `GLOSSARIO.json` e `INDICE.json` foram atualizados para eles.

Cinco capítulos que esta rodada **não** mexeu continuam vermelhos como na `main`: Aptidões, Fundamento, Origens, Perícias e Poderes avançados. A origem é a mesma dos cinco acima: o fechamento da integração mudou o texto, e o PDF da unidade, a revisão editorial e a auditoria de regras não acompanharam. Eles ficaram fora porque nenhuma correção passou por eles. Foram atualizados depois, pelo mesmo método e sem mudar o texto: ver `../publicacao-github/provas-cinco-capitulos-2026-10-04/LEIA-ME.md`.
