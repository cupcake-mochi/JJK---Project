# RASCUNHO — Caminho, Trilhas e subtrilhas

**Isto é o método e o plano, não a peça.** Ela é a maior coisa que falta escrever — **quinze Trilhas, e ela toca 100% das fichas** —, e é a única da fila em que errar o formato antes de começar custa a peça inteira. Este documento existe para o formato ser decidido **antes**, e não no meio.

Escrito na **v0.54**, com o Mizuki fora. **Nenhuma Trilha é escrita aqui.** O que está aqui é: o que já está travado, o que a conta já responde, o problema de escala com número, e as perguntas na ordem em que uma trava a outra.

**Na v0.55 a Q1 e a Q4 fecharam** — sem multiclasse, e as entregas de nível alto cruzam Trilhas do mesmo Caminho. **Na v0.60 a Q2 fechou**, junto com o calendário e o fim da palavra `subtrilha`. **Na v0.61 fechou a Q3, que é a régua.** **Sobra a Q5** — o conteúdo, entrada por entrada, e agora ela tem contra o que ser medida.

> **Duas coisas deste documento estavam erradas e foram corrigidas na v0.60. Leia isto antes do §2.**
>
> **1. A tabela de progressão do §2.1 omitiu a escada de Classe.** Uma **Classe nova de feitiço** cai nos níveis **5, 9, 13, 17 e 21** — cinco dos catorze ímpares —, e ela é a maior entrega isolada do sistema. Os níveis que não entregam nada são **nove**, não catorze: `3 · 7 · 11 · 15 · 19 · 23 · 25 · 27 · 29`.
>
> **2. E por isso a recomendação de `2, 10, 18, 26` do §3 caiu pelo próprio argumento dela.** Aqueles são os **quatro níveis mais cheios do sistema**: o nv26 entrega quatro coisas ao mesmo tempo — Classe 7, maestria, dois feitiços e marco —, o nv10 e o nv18 entregam três. O §2.1 cita o D&D 2024 justamente por ele *"não empilhar presente no mesmo nível"*, e a recomendação empilhava em todos.
>
> *A Rotina do §2.2 também mudou: o `126` do nível 30 era leitura da coluna errada do manual, e o valor é `108`. O dono é o manual, e a checagem 4d do `conferir-manual.py` passou a conferir isso.*

---

## 1. O que chega pronto, e não se rediscute

**Os quinze nomes fecharam na v0.24** e o `conferir-nomes.py` falha se algum voltar. **Três por Caminho:**

| Caminho | Trilhas |
|---|---|
| **Bastião** | `Muro` · `Punho` · `Brasa` |
| **Vanguarda** | `Estocada` · `Batedor` · `Executor` |
| **Guia** | `Elo` · `Sutura` · `Perímetro` |
| **Emanador** | `Torrente` · `Repertório` · `Arremate` |
| **Evocador** | `Servo` · `Matilha` · `Coro` |

**E cinco travas duras, cada uma com dono:**

| trava | dono |
|---|---|
| **A Trilha vem no nível 2, e já rende ali.** Ela é identidade, como o Caminho | decisão da v0.27, aplicada na v0.34 |
| **O Caminho não dá dados de dano** — e a Trilha é o Caminho | peça 5 §4, desafiada e confirmada na v0.36 |
| **O que sobra para conceder:** posicionamento, alvo, duração, recuperação, troca do fixo do acerto por atributo, e **exceção estreita e paga na economia de ação** | peça 5 §4 |
| **Você e todas as suas invocações somados entregam uma Rotina** | peça 6 §4 |
| **Ataque extra: Bastião e Vanguarda pelo Caminho no nível 7; `Arremate` e `Coro` pela Trilha; o Guia por nenhuma rota** | peça 6 §3.1, com o nível corrigido na v0.61 |

**E três das quinze já estão construíveis**, porque o rascunho de Invocações fechou a máquina delas: `Servo` dá um corpo forte, `Matilha` dá os cinco, `Coro` dá a exceção de economia de ação — **e o que a Trilha concede não sai do orçamento da ficha.** *É a metade da Q6 que aquele documento entregou.*

## 2. O que a conta já responde, e não é pergunta

### 2.1 Existe um buraco de progressão, ele tem tamanho, e é onde a Trilha cabe

*O `ESTADO-ATUAL` lista a **tabela de progressão consolidada** como uma das três coisas que não existem — "o que você ganha em cada nível está espalhado por cinco documentos". Montei ela para saber onde a Trilha cabe, e o resultado decide a pergunta sozinho.*

| nível | maestria | feitiços | marco |
|---|---|---|---|
| 2 | 1 | 3 | — |
| 3 | 1 | 3 | — |
| 4 | 1 | **4** | — |
| 6 | 1 | **5** | **marco** · ataque extra do Bastião e da Vanguarda |
| 10 | **2** | **7** | **marco** |
| 14 | 2 | **9** | **marco** |
| 18 | **3** | **11** | **marco** |
| 22 | 3 | **13** | **marco** |
| 26 | **4** | **15** | **marco** |
| 30 | 4 | **17** | **marco** |

> **Catorze dos vinte e nove níveis não entregam absolutamente nada, e são todos os ímpares.** Os feitiços conhecidos (`2 + nível ÷ 2`) cobrem **todo nível par**; a maestria e os marcos caem em cima de níveis pares que já tinham feitiço.

**Isso não é defeito e vira a resposta:** o D&D 2024 padronizou a subclasse em **3, 6, 10 e 14** justamente para não empilhar presente no mesmo nível, e aqui a lacuna é maior e mais regular do que lá. **A Trilha tem onde cair sem competir com nada.**

### 2.2 A entrega TEM de ser escalonada, e não é escolha de densidade

A peça 14 §4 registra a dívida da Trilha da Vanguarda como *"de 6% a 9% da Rotina, e a fração quase não deriva"*. **A fração não deriva; o valor absoluto cresce dez vezes:**

| nível | Rotina | 6% | 9% | em pontos de arma |
|---|---|---|---|---|
| 2 | 13 | 0,8 | 1,2 | 2,4 a 3,5 |
| 10 | 45 | 2,7 | 4,0 | 8,2 a 12,3 |
| **30** | **108** | **6,5** | **9,7** | **19,6 a 29,5** |

> **Uma Trilha que entregue tudo no nível 2 paga a dívida naquele nível e vale `1,1%` da Rotina no nível 30.** É o mesmo formato de falha que o §2.1 do rascunho de ferramenta mediu no ponto de arma: **valor absoluto contra alvo que cresce.**

**Então "quantas entregas por Trilha" não é pergunta de gosto — o mínimo é mais de uma, e a conta é quem diz.** *O que continua sendo escolha é quantas a mais.*

### 2.3 O problema de escala é o maior risco da peça, e ele tem número

Quinze Trilhas multiplicam tudo. **Este é o custo real, medido contra o que este projeto já pagou:**

| entregas por Trilha | níveis | × 15 Trilhas | comparável a |
|---|---|---|---|
| 8 | 2 + os sete marcos | **120** | nada que este projeto já tenha escrito |
| 7 | 2, 8, 12, 16, 20, 24, 28 | **105** | idem |
| **4** | 2, 10, 18, 26 | **60** | peça 13 — 81 entradas, uma versão, com a régua escrita antes |
| 3 | 2, 12, 22 | **45** | entre a peça 11 e a peça 13 |
| 2 | 2, 16 | **30** | peça 11 — 10 entradas, uma versão |

**E o histórico de custo deste projeto, para calibrar:**

| peça | tamanho | custou |
|---|---|---|
| peça 11 — aptidões | 10 entradas compráveis | **uma versão** |
| catálogo de Invocações | 19 entradas | **duas versões** |
| peça 13 — Legados | 81 entradas | **uma versão** — *porque a régua veio primeiro* |
| peça 14 — Equipamento | 52 armas e 12 propriedades | **seis versões**, da v0.42 à v0.48 |

> **A peça 13 e a peça 14 são a lição inteira, e elas discordam de propósito.** Legados escreveu **81 entradas em uma versão** porque a **régua veio antes do catálogo** — e a ordem se pagou na hora: *"os quatro Legados que a régua reprovou eram do catálogo antigo"*. Equipamento gastou **seis versões** porque a régua foi sendo consertada com o catálogo já escrito, e cada conserto envelhecia o que existia.
>
> **Trilhas é maior que as duas.** Escrever entrada antes de a régua fechar é a rota de seis versões, com 60 a 120 entradas em vez de 52.

### 2.4 Duas das três perguntas abertas da peça 6 já têm o conserto nomeado

| pergunta da peça 6 §9 | onde a resposta já está |
|---|---|
| **Como `Torrente` cobra o segundo feitiço da rodada** | *"É o mesmo defeito da seção 4 — mais de uma ação por rodada —, e o conserto que funcionou lá provavelmente serve aqui"*. **E lá ele fechou:** na Q4 de Invocações o teto deixou de ser decreto e passou a **cair da economia de ação**. `Torrente` é a mesma máquina com feitiço no lugar de corpo |
| **O que `Elo`, `Sutura` e `Perímetro` valem contra o golpe por rodada que o Guia não tem** | a v0.36 já respondeu **metade**: *"Guia — **tudo** passa. Auxílio, estender, reposicionar e recuperar são literalmente a lista do permitido"*. O que falta é o **número**, e ele é `6%` a `9%` da Rotina pela peça 14 §4 — a mesma dívida da Vanguarda, no outro Caminho |
| **Quantas Trilhas um personagem acumula, e em que níveis** | **aberta de verdade.** É a Q1 abaixo |

## 3. As perguntas, na ordem em que uma trava a outra

**Q1 — FECHADA na v0.55.** *Decisão do Mizuki:* **Caminhos não se misturam — não existe multiclasse neste sistema.** Uma Trilha por ficha, e a pendência nº 3 do `ESTADO-ATUAL`, aberta desde a v0.22, fecha com ela. **Isso mata as 105 combinações** que eu tinha orçado como o maior risco de matriz da peça.

**Q2 — FECHADA na v0.60.** *Decisão do Mizuki, depois de a conta derrubar a recomendação antiga de `2, 10, 18, 26`.*

> **Entrega de Trilha nos níveis `2 · 11 · 19 · 27`. Entrega de Caminho nos níveis `7 · 15 · 23 · 29`.**
> **80 entradas** — `4 × 15` de Trilha mais `4 × 5` de Caminho — e **405 montagens legais**.

**Os dois degraus não são conceito novo:** a peça 6 §3.1 já escreve *"Bastião e Vanguarda ganham ataque extra no nível 6, **pelo Caminho**; Arremate e Coro ganham **pela Trilha**"*. O que a v0.60 fez foi transformar a distinção existente em calendário.

**E ela resolveu um empate que oito entregas de Trilha não resolviam.** Com seis entregas, todas de Trilha, é impossível ter as duas coisas boas ao mesmo tempo:

| calendário | maior vão da Trilha | pior seca, em missões |
|---|---|---|
| `2, 7, 11, 19, 25, 29` | **8** | 27 |
| `2, 7, 11, 15, 19, 25` | 6 | **37** |
| **misto — T `2,11,19,27` · C `7,15,23,29`** | **5** | **24** |

O misto entrega os dois **e** custa dez entradas a menos, com uma matriz de dominância **nove vezes menor** — porque um degrau de Caminho é igual para as três Trilhas dele e não multiplica nada.

> **A seca foi medida em missão e não em nível**, pela curva da peça 12, porque é a unidade que o jogador sente. Hoje o vão `nv26 → nv30` são **37 missões** sem nada que se escolha, e é o maior da campanha inteira — a seca deste sistema é **no topo**, e não no meio.

*Levantamento externo que decidiu o tamanho do vão:* o problema chama **dead level** no hobby. O D&D 3.5 o remendou com dois artigos de errata em 2007; o Pathfinder 2e o proíbe por princípio declarado; o 4e pagou o oposto, com ficha de nove páginas. **E o 5e de 2014 tinha vãos de 8 entre feitos de subclasse — Paladino `3·7·15·20`, Feiticeiro `1·6·14·18`, Bardo `3·6·14` — que a edição de 2024 tirou todos**, padronizando em `3, 6, 10, 14`.

**Q3 — FECHADA na v0.61. É a régua, e ela vem ANTES do catálogo.** A régua tem três eixos — **formato**, **quanto** e **o que não pode ser** —, e ela cabe em quatro linhas:

> **Formato:** a escada de Classes da peça 11 §4. A Classe declara a **janela**, e a janela fixa a magnitude.
> **Contador:** plano, e **`1×` por descanso curto**. Nunca um que cresça, e nunca um que cada mestre leia de um tamanho.
> **Preço:** **sete fatias de `1,27` ponto por rodada**, mais o **degrau do nível 7**, que vale o vão da peça 6 §3 e substitui uma fatia.
> **Denominador:** toda entrega é escrita como fração de coisa que já cresce. Número solto deriva `8,3×` e só cabe no nível 2.

### 3.1 O formato — a escada de Classes, e o que faz ela caber aqui

**A régua da peça 13 foi testada e reprovada.** O `Desliga` só apaga o que ninguém comprou, e isso é território de Origem — nada no permitido da peça 5 §4 desliga coisa. O `Ajusta` tem **um morador legal só**, trocar o fixo do acerto por atributo. Sobram 6 das 7 linhas no `Destranca`, e um formato que põe 6 de 7 no mesmo balde não separa nada: é etiqueta.

A escada de Classes passa no mesmo teste com folga, e por um motivo de forma — ela **corta a lista de travessa** em vez de particionar. Cada linha do permitido mora nas três, em tamanhos diferentes:

| linha do permitido (peça 5 §4) | Classe 1 | Classe 2 | Classe 3 |
|---|---|---|---|
| posicionamento | só quando você critica | 1× na Reação | +3 m sempre |
| alvo | só em alvo já marcado | retarget | seu Classe 0 sempre pega 2 |
| duração | só no seu turno | dobra | +1 rodada sempre |
| recuperação | só em quem está a 1,5 m | PE de volta | PE por rodada |
| troca do fixo por atributo | — | — | permanente (peça 6 §6) |
| exceção de ação | só com Classe 0 | conjura na Reação | — (a peça 5 §4 exige limite) |
| treino em arma | — | — | permanente, **e só no nível 2** |

**Moradores: `5 · 5 · 6`.** Contra os `6 · 1 · 0` da peça 13.

E ela porta sem adaptação porque a peça 11 §4 já diz exatamente o que ela é: ***"Ela não mede quanto — mede o quê."*** Um marco compra uma aptidão de qualquer Classe que o refino alcance; um degrau do calendário entrega uma coisa de qualquer Classe. Mesma estrutura, mesmo preço, formatos que não se substituem.

**Só que o que segura a Classe 3 lá não pode ser o que segura ela aqui.** Na peça 11 é o refino — *"uma Classe 1 no refino 10 não é a mesma coisa que no refino 2. Ela cresce junto com você"* —, e o refino está proibido na Trilha. O substituto sai da própria definição das três:

| Classe | janela | dispara em | magnitude quando dispara |
|---|---|---|---|
| **3** | permanente | 100% das rodadas | **1,27** |
| **2** | limitada, `1×` por descanso curto | ~27% | **4,70** |
| **1** | condicional, sem limite de uso | ~20% | **6,35** |

Mesma média, variância diferente: **uma Classe 1 entrega cinco vezes a porrada numa rodada de cinco.** É o mesmo mecanismo do *"Farejador não fica obsoleta"* da peça 11 §4, funcionando sem o refino.

### 3.2 O contador é plano, e é a lição nº 2 aparecendo num lugar novo

A magnitude de uma entrega é fração do que você já faz, então **ela já cresce** — 8,31× na campanha, que é o que a Rotina cresce. Se o contador também crescer, o degrau cresce duas vezes:

| contador | usos nv2 | usos nv30 | cresce | contra a Rotina |
|---|---|---|---|---|
| `1×` por cena | 1,0 | 1,0 | 1,00× | **não deriva** |
| `1×` por descanso curto | 1,0 | 1,0 | 1,00× | **não deriva** |
| PE, custo `1 × maior Classe` | 12,0 | 25,7 | 2,14× | deriva 2,1× **para cima** |
| PE, custo fixo em pontos | 6,0 | 90,0 | 15,00× | deriva 15,0× para cima |
| usos = maestria, por descanso | 1,0 | 4,0 | 4,00× | deriva 4,0× para cima |

*"Esse número já inclui o que eu estou somando nele?"* — a lição nº 2, na forma mais limpa que ela já apareceu neste projeto.

> **E é por isso que o padrão do 5e 2024 não serve aqui, apesar de ser o mais copiado do hobby.** *Usos iguais ao bônus de proficiência* funciona lá porque **a magnitude do feito é plana** — *"cause 1d6 a mais"* —, e o contador crescente é justamente o que faz ela acompanhar. Aqui a magnitude já é fração. Importar os dois juntos conta a mesma coisa duas vezes.

**E o degrau é `1×` por descanso curto — não `por cena`.** *Corrigido na v0.62, e a correção veio da resposta do Mizuki à dívida que a v0.61 tinha anotado.* A v0.61 escolheu `por cena` por consistência de idioma — é de longe o relógio mais usado do projeto, e **quem é dono dessa contagem é a peça 10 §5**, que a publica e tem validador recontando — e deixou registrado que a palavra não tinha definição em lugar nenhum. **A definição chegou, e ela desfaz a escolha:**

> **Quem conta é o mestre.** Uma cena pode ser uma sala, ou um segmento de salas, ou um combate.

*Isso agora está escrito, e é da peça 10 §5.* Medido pela metodologia da peça 13 §7:

| como o mestre lê | rolagens no período | usos por combate |
|---|---|---|
| a sala, ou o próprio combate | 4,7 | 1,00 |
| um segmento curto | 9,4 | 0,50 |
| o piso inteiro | 14,1 | 0,33 |

**Spread de `3,0×` — o mesmo com que a peça 13 §7 reprovou *"por sessão"* e *"por arco"***, escrevendo que ali *"o filtro do projeto — dois mestres que nunca conversaram chegam ao mesmo número? — está falhando, com número em cima"*.

**E os 71 usos da peça 13 continuam certos**, porque a trava de lá mede **largura antes de relógio**: *"por cena num gatilho de alcance 1 é seguro por construção, não por generosidade"*. Quando o gatilho é estreito, quem limita é a frequência do próprio gatilho. **A Classe 2 de Trilha é o caso contrário — o gatilho é combate, e o relógio é o único limitador.** Largura não salva ela, então ela leva o spread inteiro.

*E a troca não move número nenhum:* os dois são degraus vizinhos da escada — `4,7` contra `6,3` rolagens, `1,34×` —, e os dois dão **um uso por luta**. A magnitude continua `4,70`. O que muda é que o gatilho passa a ser *"a luta acabou"*, que a peça 10 §1 escolheu justamente porque **dois mestres arbitram igual**.

### 3.3 O preço — e o achado é que o calendário da Q2 já tinha resolvido a derivação

O §2.2 diz que entrega de valor absoluto morre contra alvo que cresce. **Isso vale para uma entrega. O número delas também cresce:**

| nv | entregas | entregas ÷ nv2 | Rotina ÷ nv2 | razão |
|---|---|---|---|---|
| 2 | 1 | 1,00 | 1,00 | 1,00 |
| **5 e 6** | **1** | **1,00** | **2,38** | **0,42** |
| 7 | 2 | 2,00 | 2,38 | 0,84 |
| 15 | 4 | 4,00 | 4,85 | 0,83 |
| 23 | 6 | 6,00 | 7,23 | 0,83 |
| **26** | **6** | **6,00** | **8,31** | **0,72** |
| 30 | 8 | 8,00 | 8,31 | 0,96 |

A Rotina cresce **8,31×** e o número de entregas cresce **8,00×**. Então uma entrega de valor **plano** fica em fração quase constante da Rotina do nível 7 ao 30 — espalhamento de `1,33×`. **O acúmulo repõe o crescimento**, e os únicos dois buracos são a Rotina subindo de degrau antes de a entrega seguinte chegar: **nv5–6 e nv26**.

**A fatia é `1,27` ponto por rodada, plana.** Ela sai de dividir o piso da peça 14 §4 no nível 30 — `10,14 ÷ 8` — e foi escolhida contra a alternativa de a primeira entrega ser maior:

| | oito iguais (`1,27`) | a do nv2 maior (`1,92` + `1,17`) |
|---|---|---|
| erro médio **pesado por missão** | **12,2%** | 13,2% |
| pior falta | −34% no nv5 | −16% no nv26 |
| pior excesso | +57% no nv2 | **+138% no nv2** |

*O erro foi pesado por missão e não por nível, pela curva da peça 12 — 145 missões do nv2 ao nv30 —, porque é a unidade que o jogador sente. É o mesmo critério que a Q2 usou para medir seca.* **Um ponto percentual de diferença não decide nada; o `+138%` no nível 2 decide.** E o argumento que fecha é do Mizuki: **no nível 2 o peso de identidade está na escolha entre as três Trilhas, não no tamanho do número.** Escolher `Muro` em vez de `Punho` já é a coisa.

> **O limite conhecido, escrito porque ele existe:** com oito fatias iguais, a Vanguarda fica **34% abaixo** do piso do escudo nos níveis 5 e 6 — **4 missões de 145** — e entre 13% e 19% abaixo no miolo. Isso não é defeito escondido; é o preço da fatia plana, e ele está aqui para ninguém redescobrir no playtest.

### 3.4 O degrau do nível 7, que é o único diferente dos oito

A peça 6 §3 mede a linha de base assim, e a leitura dela muda tudo:

> **Rotina 108 · conjurador 99 (−8%) · físico 106 (−2%), no nível 30.**

**Ninguém está acima.** O ataque extra não põe a Vanguarda na frente — ele tira ela de −8% e põe em −2%. É **correção de base, não bônus**, e por isso ele nunca coube como um degrau: ele vale de **3,2 a 5,5 fatias** e chega num nível em que você só tem duas.

| nv | Rotina | vão (físico − conjurador) | em % da Rotina | em fatias |
|---|---|---|---|---|
| 2 | 13 | 4 | 30,8% | 3,2 |
| 10 | 45 | 5 | 11,1% | 3,9 |
| 18 | 76 | 6 | 7,9% | 4,7 |
| 30 | 108 | 7 | 6,5% | 5,5 |

> **A regra: o degrau do nível 7 substitui uma fatia, e ele vale exatamente o vão.** Quem já tem rota para ataque extra — **Bastião e Vanguarda pelo Caminho, `Arremate` e `Coro` pela Trilha** — recebe **o ataque extra no lugar dele**. Quem não tem recebe o degrau grande.

E aí os cinco Caminhos empatam, com o resto do calendário inalterado:

| nv | Rotina | Vanguarda | Guia | `Arremate` | maior distância |
|---|---|---|---|---|---|
| 10 | 45 | 51,3 (+14%) | 51,3 (+14%) | 51,3 (+14%) | **0,0 pp** |
| 14 | 63 | 69,9 (+11%) | 69,4 (+10%) | 69,9 (+11%) | 0,8 pp |
| 18 | 76 | 81,8 (+8%) | 81,8 (+8%) | 81,8 (+8%) | **0,0 pp** |
| 22 | 94 | 100,1 (+7%) | 99,5 (+6%) | 100,1 (+7%) | 0,7 pp |
| 30 | 108 | 114,9 (+6%) | 114,9 (+6%) | 114,9 (+6%) | **0,0 pp** |

*As linhas de 0,7 e 0,8 pp são interpolação entre os quatro níveis que a peça 6 §3 publica; nos níveis publicados o empate é exato.*

**Isso fecha o problema de design nº 2, aberto desde a v0.24**, e fecha com o número que a peça 6 §3.1 pediu: *"o que Elo, Sutura e Perímetro entregam que valha um golpe por rodada?"* — **valem o vão, e o vão é o degrau do nível 7.**

**E o orçamento passa de `9,4%` para `14,7%` da Rotina no nível 30. Isso não é violação, e a distinção importa:** os `6%` a `9%` da peça 14 §4 são o **buraco do escudo**, que aquela peça registra como o que a Trilha **deve** — piso, não teto. Estourar ele em `1,57×` quer dizer que largar o escudo virou decisão fácil, que é literalmente o que ela pediu. **O teto de verdade é o `+18%` sustentado que a peça 6 §3.1 reprovou**, e a régua para em **`+6%`**, com dez pontos percentuais de folga.

*A saída que pagava o ataque extra em fatias foi medida e morreu: ela custa **6 das 8**, e Bastião e Vanguarda ficariam com seis níveis mortos — exatamente o que a Q2 saiu para matar.*

### 3.5 O denominador — o eixo que decide se uma entrega deriva

Toda entrega é fração de alguma coisa. **Se essa coisa não crescer no ritmo da Rotina, a entrega deriva**, e o autor da entrada não tem como perceber olhando só para ela:

| denominador | dono | cresce | contra a Rotina | deriva? |
|---|---|---|---|---|
| Integridade `20 + 8(nv−1)` | peça 1 | 9,00× | 1,08 | não |
| **o número de entregas** | a Q2 | 8,00× | 0,96 | não |
| Classe de feitiço | o manual | 7,00× | 0,84 | não |
| ~~refino passivo~~ | peça 11 §2 | 8,00× | 0,96 | **proibido, e não é por derivar** |
| espaços de feitiço | peça 11 §3 | 5,67× | 0,68 | sim, cai |
| maestria | peça 1 | 4,00× | 0,48 | sim, cai |
| atributo | peça 2 | 2,00× | 0,24 | sim, cai |
| **deslocamento `9 m` · dado de arma** | peças 3 e 14 | **1,00×** | **0,12** | **sim, cai 8,3×** |
| nível · PE máximo | peças 12 e 6 | 15,00× | 1,81 | sim, sobe |

**O refino é o melhor candidato que existe numericamente — 8,00× contra 8,31× — e continua proibido.** O que o reprova é outro eixo: a peça 11 §3 equilibra `Corpo · Refino · Leque` porque **nenhuma compra o que a outra compra**, e a Trilha é bem comum — 100% das fichas têm uma. Pendurar ela no refino põe um bem comum dentro de uma das três:

| nv | refino de quem escolhe | de quem não escolhe | a Trilha ficaria | de graça |
|---|---|---|---|---|
| 14 | 6 | 5 | 20,0% maior | +1,5% da Rotina |
| 22 | 9 | 7 | 28,6% maior | +2,3% |
| 30 | 10 | 8 | 25,0% maior | +2,3% |

*E na direção contrária é pior:* quem vai sempre de `Corpo` ou sempre de `Leque` termina com **zero aptidões** (peça 11 §3), e a Trilha é a única coisa que ainda escala para essas duas rotas. Pendurar ela no refino tira delas o último eixo — o contrário do que aquela seção desenhou.

**Q4 — FECHADA na v0.55, e ela devolve metade do que a Q1 tinha economizado.** *Decisão do Mizuki:* **as entregas de nível alto cruzam Trilhas do mesmo Caminho** — o Bastião pega uma do `Muro` e uma do `Punho`, e nunca uma do Guia.

> **A árvore, fechada — e são DUAS camadas, não três:**
> **`Caminho`** (5, exclusivo, escolhido na criação) → **`Trilha`** (3 por Caminho, escolhida no nv2).
> No nível **2** você pega a entrega da **sua** Trilha. Nos níveis **11, 19 e 27** você pega a de **qualquer** Trilha do seu Caminho.

> **A palavra `subtrilha` morreu na v0.60, e a mecânica ficou inteira.** *Decisão do Mizuki, e o motivo foi ele mesmo se perder lendo a árvore — que é o teste que importa.* `Caminho → Trilha → subtrilha` fazia parecer **três andares** quando são **dois com um empréstimo**: a coisa que você pega no nível 11 não é uma camada abaixo da Trilha, é a **mesma camada**, tirada de um vizinho do mesmo Caminho.

**O que isso custa está medido, e é o número que a régua tem de aguentar:** a matriz de dominância deixa de varrer as 15 Trilhas e passa a varrer **as combinações de subtrilha dentro de cada Caminho**. E a pergunta aberta desde a v0.24 muda de forma: *"o Guia contra a Vanguarda"* vira ***"esta combinação de Guia contra aquela combinação de Vanguarda"***. **A régua (Q3) tem de nascer sabendo disso** — ela não está precificando quinze coisas exclusivas, está precificando peças que se somam dentro do Caminho.

*A Q1 tirou as 105 combinações entre Caminhos; a Q4 devolveu as combinações dentro deles. O saldo é bom — cruzamento dentro de um Caminho é escolha de construção, e entre Caminhos era multiclasse —, mas não é zero, e a régua paga a diferença.*

**Q5 — O que cada Trilha entrega, entrada por entrada.** *Última de propósito.* É a passada de conteúdo, e ela só começa depois da Q3.

## 4. A ordem de ataque recomendada

**Não é por Caminho, e o motivo é dependência — o mesmo critério que ordenou a fila na v0.36.**

| # | bloco | por quê aqui |
|---|---|---|
| ~~1~~ | ~~**a régua** (Q1 a Q4)~~ | **fechada** — Q1 e Q4 na v0.55, Q2 na v0.60, **Q3 na v0.61**. Peça 13 contra peça 14: régua antes de catálogo é a diferença entre uma versão e seis |
| 2 | **Evocador** — `Servo` · `Matilha` · `Coro` | **as três já têm máquina**, e o rascunho de Invocações já escreveu o que cada uma concede. São o teste barato da régua contra coisa pronta |
| 3 | **Vanguarda** — `Estocada` · `Batedor` · `Executor` | **é a única com dívida numerada** — `6%` a `9%` da Rotina, peça 14 §4 — e com moeda já aprovada para pagá-la: *"acesso a arma é moeda que ela pode gastar"* (v0.45) |
| 4 | **Guia** — `Elo` · `Sutura` · `Perímetro` | fecha o problema de design nº 2, aberto desde a v0.24. A v0.36 já disse que **tudo passa**; falta o número |
| 5 | **Bastião** — `Muro` · `Punho` · `Brasa` | `Muro` encosta em **cobrir-se de energia** (peça 11 §6) e em escudo (peça 14 §4). *A v0.36 já mandou medir as duas juntas: "ou uma domina a outra, ou são a mesma peça com dois nomes"* |
| 6 | **Emanador** — `Torrente` · `Repertório` · `Arremate` | **`Torrente` é a mais perigosa das quinze** e por isso vai por último: ela é mais de uma ação por rodada, que é a coisa que quebra todo sistema d20. `Repertório` toca a peça 11 e `Arremate` toca a economia de ação |

**E duas coisas para medir antes de escrever, não depois** — as duas já estão registradas no `ESTADO-ATUAL` e nenhuma foi medida:

- **A reação de Redução de Dano do Bastião contra cobrir-se de energia**, que já dá RD de `1,5 × refino` por 2 PE.
- **Os *pontos de feitiço* do Emanador são moeda nova ao lado do PE**, e toda moeda nova passa pelo `conferir-orcamento.py` antes de ter número.

## 5. O que o validador vai precisar ter

- **A matriz de dominância entre as quinze**, e ela roda **por Caminho** e **entre Caminhos** — porque a pergunta do Guia contra a Vanguarda é entre Caminhos. *Com a Q1 e a Q4 fechadas, o tamanho está medido: **81 montagens por Caminho** e **405 no total**, que é `15 × 3³`.*
- ~~**Se a Q1 responder "mais de uma"**, a matriz varre as **105 combinações** de duas.~~ **Morta na v0.55:** não existe multiclasse, e a matriz nunca cruza Caminhos diferentes numa mesma ficha.
- **O orçamento de cada Trilha contra os `6%` a `9%` da Rotina**, lido da **peça 14 §4** e nunca de constante. *E ele é **piso**, não teto* — a régua da Q3 para em `14,7%` de propósito, e o teto que o validador confere é o **`+18%` sustentado que a peça 6 §3.1 reprovou**, lido daquela seção.
- **A fatia contra o número de degraus**, e as duas lidas de documento: `piso da peça 14 §4 no nv30 ÷ 8`. Perturbar o calendário da Q2 tem de mover a fatia.
- **O degrau do nível 7 contra o vão da peça 6 §3** — `físico − conjurador`, no nível —, e **nunca contra constante**. Contra-teste: um degrau do nv7 que valha uma fatia normal tem de reprovar, senão a checagem só confere que existe número.
- **Quem recebe o degrau grande do nv7 e quem recebe o ataque extra no lugar**, contado contra a peça 6 §3.1 — os dois conjuntos têm de ser complementares e cobrir as quinze Trilhas.
- **Nenhuma entrega com dado de dano**, e o contra-teste: perturbar a régua da peça 5 §4 tem de acender.
- **Nenhuma entrega que cresça com refino** — peça 11 §2. *E o contra-teste que dá valor a esta: o refino **cabe** na conta (8,00× contra os 8,31× da Rotina), então uma checagem que só media derivação sairia verde. Ela tem de reprovar pelo eixo da peça 11 §3.*
- **Todo contador de Classe 2 é plano, e é `por descanso curto`.** Perturbar um degrau para `usos = maestria` tem de acender, e a mensagem tem de dizer que o defeito é a magnitude já crescer. **E perturbar para `por cena` também tem de acender**, com a mensagem apontando a trava de largura da peça 13 §7 — o relógio é o único limitador aqui, então ele leva o spread de `3,0×` inteiro.
- **Todo relógio citado sai da escada da peça 10 §5**, lida daquele documento e nunca escrita aqui. *É a mesma checagem que a peça 13 §7 já faz no catálogo de Legados, e ela achou três relógios fora da escada lá.*
- **O quarto eixo do `Servo`**, quando ele existir: a matriz do `conferir-invocacoes.py` tem de passar a rodar com ele, e as duas entradas do `DOMINANCIA_PENDENTE_Q6` têm de **sumir da declaração**. Contra-teste: tirar o quarto eixo tem de fazer as duas voltarem.
- **O teto de uma Rotina somada**, para `Servo`, `Matilha`, `Coro` e `Torrente`, conferido **pela economia de ação** e não por decreto.
- **A tabela de progressão consolidada**, que esta peça vai finalmente poder fechar: o validador confere que **todo nível entrega alguma coisa de algum documento**, ou que os que não entregam sejam lista declarada.
- **Triagem de todo nome** que as quinze criarem — e é onde mais nome novo vai nascer no projeto inteiro.
- **A cota de ataque extra da peça 6 §3.1** conferida contra o catálogo: só `Arremate` e `Coro` o dão por Trilha, e **o Guia por nenhuma rota**.

## 6. O primeiro bloco da Q5 — o Evocador, e o que ele já achou na régua

*Escrito na v0.62.* O §4 manda começar pelo Evocador porque **as três já têm máquina** — a peça 15 fechou `Servo`, `Matilha` e `Coro` inteiras — e por isso ele é o **teste barato da régua contra coisa pronta**. Ele achou uma coisa antes de qualquer entrada ser escrita, e ela é de forma e não de número.

### 6.1 O Servo está dominado, e não é por magnitude

A peça 15 fecha declarando duas dominâncias pendentes, as duas apontando para o mesmo lugar: **`Matilha > Servo`** e **`Coro > Servo`**. O `conferir-invocacoes.py` as carrega no `DOMINANCIA_PENDENTE_Q6` e falha se aparecer uma terceira. **Rodando a matriz nos três eixos que aquele validador usa:**

| Trilha | saída | corpos | ação |
|---|---|---|---|
| `Servo` | 1 Rotina | 1 | comanda |
| `Matilha` | 1 Rotina | **5** | comanda |
| `Coro` | 1 Rotina | 1 | **ataca e comanda** |

**O `Servo` não tem nenhum eixo em que esteja na frente.** Ele empata em saída — o teto de uma Rotina é igual para as três, pela peça 6 §4 — e perde ou empata nos outros dois. *Não é preço errado: é ausência de eixo.*

**E não existe número que conserte isso dentro dos três.** Subir a saída dele fura o teto da peça 6 §4; dar corpo o transforma na `Matilha`; dar ação o transforma no `Coro`. **O conserto tem de ser um quarto eixo**, e a conta diz isso sozinha: qualquer eixo em que só o `Servo` esteja na frente **mata as duas dominâncias de uma vez**.

> **Isso é o que a Q6 estava esperando, e agora está dito com forma em vez de com nome.** A peça 15 escreveu *"quando a Q6 der esse número, o par tem de sumir da declaração"* — e a resposta não é um número, é uma **coluna nova na matriz**. O número vem depois dela.

### 6.2 E a régua tem um limite aqui, que é melhor achar agora

Os candidatos óbvios de quarto eixo — **orçamento de `Traço` e `Comando`**, alcance da amarra, vida do corpo — são todos da peça 15, e **a régua da Q3 não os preça em ponto de Rotina.** A peça 15 §3.6 já tinha escrito por quê:

> *"O ponto de arma é cerca de quatro vezes menor que o ponto de ficha, e isso não é conflito — são orçamentos de tamanhos diferentes. **O que não pode acontecer é as duas moedas caírem no mesmo saco.**"*

A fatia da Q3 é `1,27` **ponto de dano por rodada**. O ponto de orçamento de invocação compra `Traço` e `Comando`, que a peça 15 §3.7 **proíbe de tocar dado de dano**. Converter um no outro é exatamente o saco único que aquela seção proíbe.

**Então a régua não muda; o que ela exige é o que sempre exigiu — que o eixo seja fração de coisa que já cresce.** E o orçamento de invocação é: ele sai dos **sete marcos**, a mesma cadência de atributo, refino e feitiço.

| nv | orçamento (peça 15 §3.6) | quanto `+1` é | acumulado |
|---|---|---|---|
| 2 | 2 | **+50%** | 1,0× |
| 10 | 4 | +25% | 2,0× |
| 18 | 6 | +17% | 3,0× |
| 30 | 9 | +11% | 4,5× |

**Ele cresce `4,5×` contra os `8,31×` da Rotina — deriva `1,8×` para baixo.** É o mesmo tamanho da deriva dos espaços de feitiço (`0,68`), que o projeto já aceita. *Vai registrado, e não escondido: uma entrega do Evocador denominada em ponto de orçamento vale a metade, no fim da campanha, do que valia quando você a pegou.*

### 6.3 A escolha do Mizuki: os DOIS eixos, e a trava que ele nomeou

*Decisão da v0.63.* **Orçamento e vida**, com o argumento dele por cima:

> *"Normalmente é a única invocação da pessoa, então ela tem de ser o equivalente de todas as outras, **mas não passar muito delas**. Por ser o mais simples, ela não pode dar um ganho maior que os outros — um exige capturar muitas invocações para valer a pena e o outro exige ir para o combate corporal. Mas ao mesmo tempo ele não pode ser muito abaixo, **já que ao perder a invocação principal, acabou o kit da pessoa**."*

**A trava do fim tem tamanho, e ele é `5×`.** A regra de morte da peça 15 §3.5 lê a **vida máxima** para decidir morte em definitivo — e com `h` a do `Servo` era um quinto da da `Matilha`, para a **mesma Rotina entregue**:

| nv | vida do corpo (`h`) | pool da `Matilha` (`5h`) | rodadas de chefe concentrando |
|---|---|---|---|
| 2 | 6 | 30 | `Servo` **0,8** · `Matilha` 4,0 |
| 10 | 22 | 110 | 1,7 · 8,5 |
| 30 | 62 | 310 | 1,7 · 8,6 |

> **A concessão, fechada:** o corpo do `Servo` tem **`5 × h`** — o pool inteiro da `Matilha` num corpo só — e **o orçamento da ficha mais metade**, arredondando para baixo.

**A vida iguala e o orçamento diferencia**, e os dois papéis são diferentes de propósito:

| | por que este eixo |
|---|---|
| **vida `5h`** | fecha a trava do *"acabou o kit"*. Os dois passam a sair da luta pelo mesmo golpe, e apagar o `Servo` custa as mesmas `1,25` Rotina de área por alvo que apagar a `Matilha`. **Nenhuma exceção nova** — a regra do §3.5 continua valendo palavra por palavra |
| **orçamento `×1,5`** | é onde o `Servo` fica **na frente**, e é o eixo que mata as duas dominâncias. `2→3` no nv2, `9→13` no nv30 — 46% do que compraria o catálogo inteiro |

**E o *"não passar muito delas"* está medido:** a `Matilha` compra `9` no nv30 e **aplica os nove cinco vezes**, um por corpo. Em largura de utilidade ela continua na frente; o que o `Servo` compra é profundidade num corpo só.

*O `Coro` fica com `h`, e isso é a troca dele escrita:* ele é o único que **ataca e comanda**, e o único cujo corpo cair não acaba o kit — o dono continua batendo.

> **E a vida não entra por dominância, o que é o motivo de ela ter checagem própria.** Medido: **só o orçamento já zera a matriz.** Tirar o `5h` sairia **verde** na matriz e desfaria em silêncio a metade da Q6 que a matriz não mede. O `conferir-invocacoes.py` passou a conferir os dois separados, e o `DOMINANCIA_PENDENTE_Q6` foi a **conjunto vazio**.

## 7. O que esta peça destrava, e o que ela fecha

| | |
|---|---|
| **destrava** | nada — **ela é a última dependência da fila.** É a peça que os outros esperam, não a que espera |
| **fecha** | o problema de design **nº 2** (Guia contra Vanguarda, aberto desde a v0.24), a pendência **nº 3** e a **nº 4** do `ESTADO-ATUAL`, as três perguntas do §9 da peça 6, e a dívida de `6%` a `9%` da Rotina que a peça 14 §4 registrou |
| **toca** | **100% das fichas.** Nenhuma outra peça da fila faz isso |
