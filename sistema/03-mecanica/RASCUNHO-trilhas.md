# RASCUNHO — Caminho, Trilhas e subtrilhas

**Isto é o método e o plano, não a peça.** Ela é a maior coisa que falta escrever — **quinze Trilhas, e ela toca 100% das fichas** —, e é a única da fila em que errar o formato antes de começar custa a peça inteira. Este documento existe para o formato ser decidido **antes**, e não no meio.

Escrito na **v0.54**, com o Mizuki fora. **Nenhuma Trilha é escrita aqui.** O que está aqui é: o que já está travado, o que a conta já responde, o problema de escala com número, e as perguntas na ordem em que uma trava a outra.

**Na v0.55 a Q1 e a Q4 fecharam** — sem multiclasse, e as entregas de nível alto cruzam Trilhas do mesmo Caminho. **Na v0.60 a Q2 fechou**, junto com o calendário e o fim da palavra `subtrilha`. **Na v0.61 fechou a Q3, que é a régua** — e a **v0.65 reabriu e refez a Q4**: a Trilha virou fechada, sem empréstimo, com troca total nos níveis 11, 19 e 27. **Sobra a Q5** — o conteúdo, entrada por entrada, e agora ela tem contra o que ser medida.

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
| **Emanador** | `Torrente` · `Explosivo` · `Arremate` |
| **Evocador** | `Servo` · `Matilha` · `Coro` |

**E cinco travas duras, cada uma com dono:**

| trava | dono |
|---|---|
| **A Trilha vem no nível 2, e já rende ali.** Ela é identidade, como o Caminho | decisão da v0.27, aplicada na v0.34 |
| **O Caminho não dá dados de dano** — e a Trilha é o Caminho | peça 5 §4, desafiada e confirmada na v0.36 |
| **O que sobra para conceder:** posicionamento, alvo, duração, recuperação, troca do fixo do acerto por atributo, e **exceção estreita e paga na economia de ação** | peça 5 §4 |
| **Você e todas as suas invocações somados entregam uma Rotina** | peça 6 §4 |
| **Ataque extra: Bastião e Vanguarda pelo Caminho no nível 7; `Arremate` e `Coro` pela Trilha; o Guia por nenhuma rota** | peça 6 §3.1, com o nível corrigido na v0.61 |
| **A Trilha é fechada: as quatro entregas dela são todas dela.** Trocar de Trilha é troca **total**, e só nos níveis 11, 19 e 27 | Q4, refeita na v0.65 |

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

> **Entrega de Trilha nos níveis `2 · 11 · 19 · 27`. Entrega de Caminho nos níveis `2 · 7 · 15 · 30`.**

> **O calendário de Caminho mudou na v0.70 e a métrica só foi rodada na v0.71.** Ele era `7 · 15 · 23 · 29`, e o desenho dos cinco Caminhos o moveu sem que ninguém refizesse a conta de vão e seca que a Q2 usou para escolhê-lo. **Refeita: vão de `5` para `8` níveis, seca de `24` para `31` missões**, as duas por causa do degrau do nível 23 que saiu. *O modelo reproduz o `vão 5 · seca 24` publicado antes de comparar, que é o que faz a comparação valer.* **Decisão do Mizuki: o vão fica, e é preço aceito e não defeito.** *A Q2 continua de pé; o que caiu é a afirmação de que o calendário de Caminho não tinha se mexido.*
> **80 entradas** — `4 × 15` de Trilha mais `4 × 5` de Caminho. *As **405 montagens** que esta linha anunciava eram do empréstimo entre Trilhas; com a Q4 refeita na v0.65 elas são **15**, e o calendário não mudou.*

**Os dois degraus não são conceito novo:** a peça 6 §3.1 já escreve *"Bastião e Vanguarda ganham ataque extra no nível 6, **pelo Caminho**; Arremate e Coro ganham **pela Trilha**"*. O que a v0.60 fez foi transformar a distinção existente em calendário.

**E ela resolveu um empate que oito entregas de Trilha não resolviam.** Com seis entregas, todas de Trilha, é impossível ter as duas coisas boas ao mesmo tempo:

| calendário | maior vão da Trilha | pior seca, em missões |
|---|---|---|
| `2, 7, 11, 19, 25, 29` | **8** | 27 |
| `2, 7, 11, 15, 19, 25` | 6 | **37** |
| **misto — T `2,11,19,27` · C `7,15,23,29`** | **5** | **24** |

O misto entrega os dois **e** custa dez entradas a menos, com uma matriz de dominância **nove vezes menor** — porque um degrau de Caminho é igual para as três Trilhas dele e não multiplica nada. *E a Q4 da v0.65 derrubou o resto da multiplicação: hoje são 15 montagens.*

> **A seca foi medida em missão e não em nível**, pela curva da peça 12, porque é a unidade que o jogador sente. Hoje o vão `nv26 → nv30` são **37 missões** sem nada que se escolha, e é o maior da campanha inteira — a seca deste sistema é **no topo**, e não no meio.

*Levantamento externo que decidiu o tamanho do vão:* o problema chama **dead level** no hobby. O D&D 3.5 o remendou com dois artigos de errata em 2007; o Pathfinder 2e o proíbe por princípio declarado; o 4e pagou o oposto, com ficha de nove páginas. **E o 5e de 2014 tinha vãos de 8 entre feitos de subclasse — Paladino `3·7·15·20`, Feiticeiro `1·6·14·18`, Bardo `3·6·14` — que a edição de 2024 tirou todos**, padronizando em `3, 6, 10, 14`.

**Q3 — FECHADA na v0.61. É a régua, e ela vem ANTES do catálogo.** A régua tem três eixos — **formato**, **quanto** e **o que não pode ser** —, e ela cabe em quatro linhas:

> **Formato:** a escada de **Classe Passiva** da peça 11 §4. Ela declara a **janela**, e a janela fixa a magnitude.
> **Contador:** plano, e **`1×` por descanso curto**. Nunca um que cresça, e nunca um que cada mestre leia de um tamanho.
> **Preço:** **sete fatias de `1,27` ponto por rodada**, mais o **degrau do nível 7**, que vale o vão da peça 6 §3 e substitui uma fatia.
> **Denominador:** toda entrega é escrita como fração de coisa que já cresce. Número solto deriva `8,3×` e só cabe no nível 2.

### 3.1 O formato — a escada de Classe Passiva, e o que faz ela caber aqui

**A régua da peça 13 foi testada e reprovada.** O `Desliga` só apaga o que ninguém comprou, e isso é território de Origem — nada no permitido da peça 5 §4 desliga coisa. O `Ajusta` tem **um morador legal só**, trocar o fixo do acerto por atributo. Sobram 6 das 7 linhas no `Destranca`, e um formato que põe 6 de 7 no mesmo balde não separa nada: é etiqueta.

A escada de **Classe Passiva** passa no mesmo teste com folga, e por um motivo de forma — ela **corta a lista de travessa** em vez de particionar. Cada linha do permitido mora nas três, em tamanhos diferentes:

| linha do permitido (peça 5 §4) | Classe Passiva 1 | Classe Passiva 2 | Classe Passiva 3 |
|---|---|---|---|
| posicionamento | só quando você critica | 1× na Reação | +3 m sempre |
| alvo | só em alvo já marcado | retarget | seu Classe 0 sempre pega 2 |
| duração | só no seu turno | dobra | +1 rodada sempre |
| recuperação | só em quem está a 1,5 m | PE de volta | PE por rodada |
| troca do fixo por atributo | — | — | permanente (peça 6 §6) |
| exceção de ação | só com Classe 0 | conjura na Reação | — (a peça 5 §4 exige limite) |
| treino em arma | — | — | permanente, **e só no nível 2** |

**Moradores: `5 · 5 · 6`.** Contra os `6 · 1 · 0` da peça 13.

E ela porta sem adaptação porque a peça 11 §4 já diz exatamente o que ela é: ***"Ela não mede quanto — mede o quê."*** Um marco compra uma aptidão de qualquer Classe Passiva que o refino alcance; um degrau do calendário entrega uma coisa de qualquer Classe Passiva. Mesma estrutura, mesmo preço, formatos que não se substituem.

**Só que o que segura a Classe Passiva 3 lá não pode ser o que segura ela aqui.** Na peça 11 é o refino — *"uma Classe Passiva 1 no refino 10 não é a mesma coisa que no refino 2. Ela cresce junto com você"* —, e o refino está proibido na Trilha. O substituto sai da própria definição das três:

> **As três taxas abaixo são TRÊS PONTOS DE UM DIAL, e não os três valores possíveis.** *Registrado na v0.68:* a Trilha declara a taxa de cada entrada, porque os botões que o permitido oferece são grandes e indivisíveis — nenhuma das três divide `11,50` até `1,7`, e `15%` divide. **A escada continua medindo forma; a taxa é que mede quanto.**

| Classe Passiva | janela | dispara em | magnitude quando dispara |
|---|---|---|---|
| **3** | permanente | 100% das rodadas | **1,27** |
| **2** | limitada, `1×` por descanso curto | ~27% | **4,70** |
| **1** | condicional, sem limite de uso | ~20% | **6,35** |

Mesma média, variância diferente: **uma Classe Passiva 1 entrega cinco vezes a porrada numa rodada de cinco.** É o mesmo mecanismo do *"Farejador não fica obsoleta"* da peça 11 §4, funcionando sem o refino.

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

**E os 71 usos da peça 13 continuam certos**, porque a trava de lá mede **largura antes de relógio**: *"por cena num gatilho de alcance 1 é seguro por construção, não por generosidade"*. Quando o gatilho é estreito, quem limita é a frequência do próprio gatilho. **A Classe Passiva 2 de Trilha é o caso contrário — o gatilho é combate, e o relógio é o único limitador.** Largura não salva ela, então ela leva o spread inteiro.

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

> **LEIA O §3.4-B ANTES DESTA SEÇÃO.** *A v0.68 reformulou a Q3:* **a fatia continua sendo a unidade de conta e deixou de ser o preço de cada entrega.** O que esta seção mede — de onde a fatia sai, e que ela é plana — continua valendo inteiro. **O que caiu é a cobrança por entrega**, e com ela a pergunta *"oito iguais ou a do nv2 maior?"*, que deixou de existir quando a distribuição virou livre dentro do orçamento da Trilha.

> ## ⚠⚠ A FATIA É `5,08`, E O CAMINHO LEVA `3` FATIAS E A TRILHA LEVA `5`
>
> *Decidido na v0.73 e escrito aqui na v0.74. **Tudo abaixo desta caixa está em escala vencida** — o `1,27` da versão original e o `2,54` da caixa seguinte.*
>
> | | fatia | orçamento da Trilha | orçamento do Caminho |
> |---|---|---|---|
> | até a v0.71 | `1,27` | 7 fatias distribuídas | — |
> | v0.72 | `2,54` | — | — |
> | **v0.73 em diante** | **`5,08`** | **`5` fatias = `25,40` por rodada** | **`3` fatias**, mais o nível 7 de graça |
>
> **A camada de Caminho mais Trilha vira `27,7%` da ficha, e o físico termina em `+35,8%` da Rotina no nível 30.**
>
> **O que destravou o segundo dobro foi achar que a trava que segurava era circular.** A v0.72 reprovou `3×` e `4×` medindo contra o `+18%` da peça 6 §3.1 — **e foi a própria v0.72 que escreveu que aquele número não é teto de dano.** Ele é a medida de uma montagem de três ações que aquela seção recusa **pelo mecanismo**. Das cinco travas da v0.72, **quatro passam em `4×`; só a do `+18%` reprova, e ela reprova contra si mesma.**
>
> **O teto que não é circular é o pilar 1:** quanto da ficha pode ser Caminho e Trilha antes de a técnica deixar de ser a identidade. *Isso é decisão de design e não conta*, e a decisão do Mizuki foi `4×`, com o argumento dele: **"ficar constantemente nessa briga de onde pôr os pontos não vai salvar o projeto, só o limite ao ponto de não conseguirmos construir nada."**
>
> **A banda de escrita é `4,50` a `5,00` fatias por Trilha**, com sobra de propósito.
>
> > **E o acoplamento que ela paga NÃO foi aplicado, e o número que a v0.73 registrou estava errado.** Aquela versão escreveu *"a vida de chefe e de capanga sobe `36%`"*, e o `36` é o `+35,8% da Rotina` copiado com a base trocada — a base de antes era `98%` da Rotina, não `100%`. **Com a base certa dá `+38,3%`**, e isso é **teto e não valor**: ele supõe que as `8` fatias inteiras viram dano, e a matriz do Bastião mostra que o `Muro` põe `0,00` em dano. **Fica parada até as nove Trilhas que faltam serem preçadas**, porque só aí a média do grupo é computável. *O dono declarado daquela tabela é o playtest, e `04-playtest/` continua vazia.*
>
> ## ⚠ A FATIA DOBROU NA v0.72 — ela era `2,54`, e o motivo é um piso lido como teto
>
> **O `1,27` abaixo saiu de dividir *o piso* da peça 14 §4 por oito — e a régua passou quatro versões cobrando ele como se fosse teto.** A própria lista de armadilhas do projeto diz: *"Piso não é teto. Um número registrado como o que a peça **deve** é mínimo, e ler ele como máximo reprova a solução certa."*
>
> **E o `10,14` nunca foi "quanto uma Trilha vale".** É a conta da peça 14 de *quanto a Trilha da **Vanguarda** precisa entregar para alguém largar o escudo* — um buraco contábil de uma peça só, dividido por oito e aplicado às quinze Trilhas e aos cinco Caminhos, sem ninguém decidir isso.
>
> **A métrica que decidiu não é % da Rotina — é quanto a camada vale do que o personagem REALMENTE faz:**
>
> | | com `1,27` | com `2,54` |
> |---|---|---|
> | nível 2 | 10,4% | **18,8%** |
> | nível 18 | 6,1% | **11,5%** |
> | nível 30 | 7,7% | **14,4%** |
>
> *Com o valor velho, um Caminho inteiro mais uma Trilha inteira valiam **menos de um décimo da ficha**. Foi o Mizuki que apontou — "tá tudo muito irrelevante" —, e a conta deu razão a ele.*
>
> **As cinco travas conferidas:** o nível 30 fica em `+14,6%` contra o `+18%` que a peça 6 §3.1 reprova · a magnitude nunca vem de ação a mais por rodada · a camada não deriva como fração da saída (19% → 14%) · continua acima do piso da peça 14 · a fatia continua plana.
>
> **Contra-teste:** `3×` dá `+23%` e `4×` dá `+31%` — **as duas reprovam.** O teto prático é `21` de dano por rodada, que dá `+17,6%` e encosta no limite.
>
> **O orçamento pago passa de `8,89` para `17,8`** — sete fatias de `2,54`, mais o degrau do nível 7. *Toda conta de entrega escrita antes da v0.72 precisa ser refeita nesta escala, inclusive o `Servo` do §6.10 e o Bastião do `DESENHO-trilhas.md`.*

**A fatia era `1,27` ponto por rodada, plana.** Ela saía de dividir o piso da peça 14 §4 no nível 30 — `10,14 ÷ 8` — e foi escolhida contra a alternativa de a primeira entrega ser maior:

| | oito iguais (`1,27`) | a do nv2 maior (`1,92` + `1,17`) |
|---|---|---|
| erro médio **pesado por missão** | **12,2%** | 13,2% |
| pior falta | −34% no nv5 | −16% no nv26 |
| pior excesso | +57% no nv2 | **+138% no nv2** |

*O erro foi pesado por missão e não por nível, pela curva da peça 12 — 145 missões do nv2 ao nv30 —, porque é a unidade que o jogador sente. É o mesmo critério que a Q2 usou para medir seca.* **Um ponto percentual de diferença não decide nada; o `+138%` no nível 2 decide.** E o argumento que fecha é do Mizuki: **no nível 2 o peso de identidade está na escolha entre as três Trilhas, não no tamanho do número.** Escolher `Muro` em vez de `Punho` já é a coisa.

> **O limite conhecido, escrito porque ele existe:** com oito fatias iguais, a Vanguarda fica **34% abaixo** do piso do escudo nos níveis 5 e 6 — **4 missões de 145** — e entre 13% e 19% abaixo no miolo. Isso não é defeito escondido; é o preço da fatia plana, e ele está aqui para ninguém redescobrir no playtest.

> ## ✔ RESOLVIDO na v0.81 — o aviso da v0.80 virou conta
>
> A v0.80 deixou dois avisos aqui: o vão estava pequeno e o teto tinha morrido. **Os dois foram medidos, e o resultado é que o orçamento não se move.**
>
> **1. O vão foi corrigido, e ele não move o orçamento.** Ele era `4 · 5 · 6 · 7` e é `9 · 10 · 11 · 12` — exatamente um golpe simples. *A linha do conjurador da peça 6 §3 somava um Classe 0 de `4,50` que não existe no manual.*
>
> **Mas o ponto de chegada é o mesmo dos dois lados.** Pela leitura velha o conjurador estava em `99` e ganhava um degrau de `7`, chegando em `106`. Pela nova ele está em `94` e ganha um degrau de `12`, chegando em `106`. **O que mudou foi o tamanho do degrau de graça, não o orçamento pago** — e o degrau do nível 7 nunca saiu das fatias.
>
> **Consequência: a fatia continua `5,08`, o Caminho continua levando `3` e a Trilha `5`, e nenhuma das onze Trilhas fechadas se move.** *Conferido varrendo o repositório atrás de quem usa o vão como base de preço: são três lugares, e os três já estão tratados — os dois degraus de nível 7 marcados no `DESENHO-caminhos.md` e o nível 2 do `Arremate`, repreçado na v0.80.*
>
> **2. O teto morreu e NÃO tem substituto. Isso foi procurado, não suposto.**
>
> Sem o `+18%`, as outras quatro travas da v0.72 **não reprovam em orçamento nenhum** — medidas de `1×` a `8×`:
>
> | trava | o que ela faz sem o `+18%` |
> |---|---|
> | a magnitude nunca vem de ação a mais por rodada | é regra de **mecanismo**. Proíbe uma porta, não limita tamanho |
> | a camada não deriva como fração da saída | **melhora** quando o orçamento cresce: o espalhamento cai de `3,61×` para `1,81×` |
> | continua acima do piso da peça 14 | é **piso**. Crescer nunca viola |
> | a fatia continua plana | é propriedade de construção, não limite |
>
> > **Contra-teste, porque senão isto é trivialmente verdadeiro:** o `+18%`, se estivesse vivo, **reprovaria a partir de `3×`** — e reprova o orçamento de hoje, que está em `+35,7%`. **Existia teto, e era ele. Era o único.**
>
> **Três candidatos a teto novo foram testados e os três caíram:**
>
> | candidato | por que não serve |
> |---|---|
> | a coluna **dano do grupo por rodada** do manual | dono declarado: **o playtest**, e `04-playtest/` está vazia. Usar ela cria a segunda fonte sem dono |
> | a razão **chefe = 3 a 4× o dano do grupo** | é invariante de **relação**, não teto de nível — as duas colunas são da mesma tabela e sobem juntas |
> | a **duração de combate** de `3,3` a `4,0` rodadas | é a primeira dividida pela vida do chefe. Mesmo dono, mesmo defeito |
>
> **E o único que reconstrói sem passar pelo playtest nunca morde.** *"A técnica tem de continuar sendo a maioria do que a ficha faz"* é o pilar 1 escrito como conta, e ele não é circular — mede a camada contra a linha do físico, que tem dono fora desta régua. **Mas a camada só alcança metade da ficha em `10,45×`, que é `2,6` vezes o orçamento de hoje.** *Um teto que só reprova a dez vezes de onde estamos é a lição nº 8 por outra porta.*
>
> ## ⚠ ENTÃO O TETO É DECISÃO, E ELA É DO MIZUKI
>
> **Não existe número que segure este orçamento. O que segura é o pilar 1, e ele é escolha de design.** *A decisão está tomada desde a v0.73, com o argumento dele: **"ficar constantemente nessa briga de onde pôr os pontos não vai salvar o projeto, só o limite ao ponto de não conseguirmos construir nada."***
>
> > **O orçamento é `4×`, que é a fatia de `5,08` — `3` fatias de Caminho e `5` de Trilha. A camada vale `27,7%` do que o personagem faz no nível 30, e a técnica fica com os outros `72,3%`.**
>
> **Isto está escrito como decisão e não como conta de propósito**, porque escrever decisão vestida de conta é o que o `+18%` fazia. *A âncora externa que existe: no 5e a subclasse carrega de `10%` a `30%` do orçamento de classe mais subclasse, dependendo da classe. O denominador não é o mesmo daqui, então ela serve de ordem de grandeza e não de trava.*
>
> **O que fica pendurado, e é de playtest:** medindo com o modelo do manual, no orçamento de hoje **o chefe deixa de conseguir derrubar a ficha mais frágil concentrando fogo**. A virada acontece entre `2×` e `3×`. *Isso é teto e não valor — ele supõe que as `8` fatias inteiras viram dano, e a matriz do Bastião diz que não viram. **Mas é a primeira pergunta de mesa deste orçamento com número em cima.***

### 3.4 O degrau do nível 7, que é o único diferente dos oito

A peça 6 §3 mede a linha de base assim, e a leitura dela muda tudo:

> **Rotina 108 · conjurador 99 (−8%) · físico 106 (−2%), no nível 30.**

**Ninguém está acima.** O ataque extra não põe a Vanguarda na frente — ele tira ela de baixo da régua e encosta ela nela. É **correção de base, não bônus**, e por isso ele nunca coube como um degrau pago.

> **A linha de base foi corrigida na v0.80 e a tabela abaixo é a nova.** *A leitura acima — `conjurador 99 (−8%)` — era a que somava o Classe 0 fantasma. Hoje a peça 6 §3 publica **Rotina 108 · conjurador 94 · físico 106** no nível 30, e o vão é exatamente um golpe simples.*

| nv | Rotina | conjurador | físico | vão (físico − conjurador) | em % da Rotina | em fatias de `5,08` |
|---|---|---|---|---|---|---|
| 2 | 13 | 13 | 22 | **9** | 69,2% | 1,77 |
| 10 | 45 | 40 | 50 | **10** | 22,2% | 1,97 |
| 18 | 76 | 67 | 78 | **11** | 14,5% | 2,17 |
| 30 | 108 | 94 | 106 | **12** | 11,1% | **2,36** |

> **O vão vale hoje entre `1,77` e `2,36` fatias** — contra as `3` do Caminho inteiro. *Na escala velha ele valia de `3,2` a `5,5`, e era isso que o fazia não caber como um degrau de oito. **Com o preço morando na Trilha e não na entrega, ele é só uma entrega grande** — que é o que o §3.4-B abaixo já dizia.*

> **A regra: o degrau do nível 7 substitui uma fatia.** Quem já tem rota para ataque extra — **Bastião e Vanguarda pelo Caminho, `Arremate` e `Coro` pela Trilha** — recebe **o ataque extra mais uma segunda metade**. Quem não tem recebe o degrau grande, em `2,36`.

> **⚠⚠ A frase "ele vale exatamente o vão" morreu na v0.155, e o motivo é que o vão morreu como número.** *A v0.147 pôs o ataque extra de volta dentro da Ação de Atacar, e a Ação de Atacar não inclui o feitiço de Toque — então o físico passou a **escolher** entre atacar e conjurar, e `físico − conjurador` deixou de ser uma subtração.* **Medido: o ataque extra vale de `0,53` a `1,68` fatia conforme refino e Manha, contra os `2,36` que a tabela abaixo publica.**
>
> | nível 7 | ataque extra | + a metade nova | total |
> |---|---|---|---|
> | **Bastião** — `Ainda de Pé` | `0,83` | `1,10` | **`1,93`** |
> | **Vanguarda** — `Não Pega` | `0,92` | `1,18` | **`2,10`** |
> | Guia · Emanador · Evocador | — | — | `2,36` |
>
> **A conta inteira mora na peça 6 §3.1**, com a taxa derivada do bloco 1 do `conferir-orcamento.py` e a diferença de `−0,44` e `−0,26` declarada. *A tabela de vão logo acima fica como leitura da v0.80: ela continua descrevendo a linha de base, e não o preço do degrau.*

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

**E o orçamento passa de `9,4%` para `14,7%` da Rotina no nível 30. Isso não é violação, e a distinção importa:** os `6%` a `9%` da peça 14 §4 são o **buraco do escudo**, que aquela peça registra como o que a Trilha **deve** — piso, não teto. Estourar ele em `1,57×` quer dizer que largar o escudo virou decisão fácil, que é literalmente o que ela pediu.

> **A frase que fechava este parágrafo morreu na v0.81.** *Ela dizia: "o teto de verdade é o `+18%` sustentado que a peça 6 §3.1 reprovou, e a régua para em `+6%`".* **Aquele `+18%` não reconstrói de nada e a montagem que ele media deixou de ser proibida.** *E os dois números da frase estavam em escalas diferentes: o `+6%` é da escala de `1,27` por fatia, três dobros atrás do orçamento de hoje.* **O teto hoje é decisão declarada, e a caixa no topo desta seção diz qual é e por quê.**

*A saída que pagava o ataque extra em fatias foi medida e morreu: ela custa **6 das 8**, e Bastião e Vanguarda ficariam com seis níveis mortos — exatamente o que a Q2 saiu para matar.*

### 3.4-B A Q3 foi REFORMULADA na v0.68, e o que mudou é o método

*Não é ajuste de número: é onde o preço mora.* **A auditoria da escada mostrou que o método antigo não conseguia construir nem a primeira Trilha da fila**, e as duas metades do conserto são estas:

> **1. O preço mora na TRILHA, não na entrega.** As quatro entregas de uma Trilha somam o orçamento dela. Nada obriga as quatro a valerem a mesma coisa.
> **2. Cada entrada declara a TAXA DE DISPARO**, e a magnitude é o botão que o permitido já oferece. O que se confere é `botão × taxa`.

#### Por que o método antigo não fechava

Ele cobrava **uma fatia por entrega**, e os botões que a peça 5 §4 autoriza são **indivisíveis e grandes**:

| o botão | vale | em fatias |
|---|---|---|
| recuperação — `+1 PE` | `5,14` | **4,1** |
| alvo — o golpe simples pega 2 | `11,50` | **9,1** |
| exceção de ação — uma ação a mais | `108,00` | **85,2** |
| posicionamento — `+3 m` | `1,80` | 1,4 |

**Só posicionamento cabe direto.** A escada oferece três taxas — `100%`, `27%` e `20%` — e **nenhuma delas divide `11,50` até `1,7`**. Com a taxa declarada, `15%` divide.

> **É por isso que a escada não estava errada e mesmo assim não servia.** Ela mede **forma**, e diz isso de si mesma — *"ela não mede quanto, mede o quê"*. As três Classes são **três pontos de um dial contínuo**, e a Trilha precisa do dial inteiro. *A escada continua sendo a escada de aptidão, e continua valendo lá, onde o refino carrega a magnitude e o orçamento é de um marco.*

#### O que sobrevive da Q3 original, e é quase tudo

**O calendário da Q2, as travas de forma do §3.6, o degrau do nível 7 e a banda de orçamento não se movem.** O que muda:

| | antes | agora |
|---|---|---|
| onde o preço mora | em cada entrega | na **Trilha inteira** |
| como uma entrada é conferida | vale `1,27`? | `botão × taxa` bate com a fatia dela? |
| o que não é dano | não tinha como entrar | entra, e responde a **dominância e forma** |
| distribuição das quatro | oito iguais | livre, dentro do orçamento |

**E o degrau do nível 7 deixa de ser exceção.** O §3.4 o marca como *"o único diferente dos oito"* porque ele vale de `3,2` a `5,5` fatias e a régua antiga cobrava uma. Com o preço por Trilha ele é só uma entrega grande. *Uma régua que precisa de exceção para o caso mais importante estava medindo a coisa errada.*

#### O que isso custa, escrito porque existe

- **Perde-se a checagem por entrega**, que era gancho fácil de validador. No lugar entra uma por Trilha, mais difícil de escrever e mais próxima do que importa.
- **A taxa de disparo é um número novo por entrada**, e ela é estimativa de mesa. **Toda entrada tem de declarar a dela**, e o validador confere `botão × taxa` — nunca a taxa sozinha, que não tem contra o que ser conferida.
- **Entrega de utilidade — treino, sentido, comunicação — entra sem preço em dano**, porque não existe conversão e nunca vai existir. Ela responde a dominância e à trava de forma. *Isso é dívida declarada, não buraco.*

### 3.5 O denominador — o eixo que decide se uma entrega deriva

> **A PERGUNTA DESTA SEÇÃO ESTAVA ERRADA, e a v0.68 achou isso medindo.** Ela pergunta *"a entrega é fração de coisa que cresce?"* — e o §3.3 escolheu entrega **plana**, que por essa pergunta seria reprovada. **A pergunta certa é: "isso cresce DEPOIS de chegar?"** Uma entrega que continua crescendo sozinha depois de entrar na ficha soma duas vezes com o acúmulo do calendário, e é ela que esta seção existe para pegar. *A tabela abaixo continua útil como mapa de quanto cada denominador cresce; o que muda é o que a coluna "deriva?" quer dizer.*

Toda entrega é fração de alguma coisa. **Se essa coisa não crescer no ritmo da Rotina, a entrega deriva**, e o autor da entrada não tem como perceber olhando só para ela:

| denominador | dono | cresce | contra a Rotina | deriva? |
|---|---|---|---|---|
| Integridade `20 + (Ess+5)(nv−1)` | **peça 24** | `6,60×` a `10,94×` | `0,79` a `1,31` | **depende da Essência, desde a v0.145** — em Essência `3` é o `9,00×`/`1,08` de sempre |
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

**Q4 — REABERTA e REFEITA na v0.65. A Trilha é fechada, e o que existe é TROCA.**

*A v0.55 tinha decidido que as entregas de nível alto cruzam Trilhas do mesmo Caminho. O Mizuki derrubou isso na v0.65, e o argumento é dele:* ***"misturar assim é mais fácil do que misturar uma nv2 e outra de nv11 de trilhas diferentes... mas manter a forma de 405 rende em deixar pegar trilhas sem ter a base da trilha e fica estranho."***

> **A árvore, refeita — duas camadas, e a de baixo é fechada:**
> **`Caminho`** (5, exclusivo, escolhido na criação) → **`Trilha`** (3 por Caminho).
> **As quatro entregas de Trilha — `2 · 11 · 19 · 27` — são todas da sua Trilha.** Não existe pegar de outra.
> **Nos níveis `11`, `19` e `27` você pode TROCAR de Trilha, dentro do seu Caminho. A troca é total:** tudo o que você tinha vira o equivalente da Trilha nova.

**O levantamento externo achou três modelos, e não existe um quarto limpo:**

| sistema | como resolve |
|---|---|
| **D&D 5e** (2014 e 2024) | **trilha fechada.** Você pega as coisas da subclasse, na ordem dela. Não existe misturar, e **não existe regra nenhuma de trocar** — nas duas edições, é discricionariedade de mestre |
| **Pathfinder 2e** | **pool, mas com pré-requisito escrito em cada entrada** — *"prerequisites can be a specific class feature, or another feat"*. É assim que ele impede pegar o avançado sem o básico |
| **Pathfinder Society** (personagem entre mestres, o caso mais parecido com este) | **rebuild completo, uma vez só, com data para expirar.** Mudar de rumo lá é evento excepcional e central, não regra de nível |

> **Ou você escreve pré-requisito em cada entrada, ou você fecha a trilha.** Não existe meio-termo que fique limpo — e a forma de 405 era exatamente o meio-termo.

**E o próprio projeto já tinha o argumento a favor de fechar, na peça 5 §4:** *"se o Caminho desse dano, dois personagens do mesmo Caminho começariam a se parecer, e a coisa que os distingue — **a técnica que cada um escreveu** — perderia espaço."* **A Trilha nunca foi o motor de variedade.** A técnica é, e cada jogador escreve a dele do zero. *Quinze Trilhas fechadas não é pouco: é a quantidade certa para uma camada que não deve carregar a individualidade.*

**O que a mudança custa e o que ela devolve:**

| | antes (v0.55) | agora (v0.65) |
|---|---|---|
| montagens a conferir | **405** | **15** |
| pegar o avançado sem o básico | acontecia, e nada proibia | **impossível** |
| mudar de ideia | não existia | **troca total em 11, 19 ou 27** |
| pré-requisito escrito em cada entrada | seria obrigatório | **desnecessário** |

*A trava que a pergunta do Mizuki caçou continua valendo por outro motivo:* **nenhuma entrega pode depender de outra** — não mais porque você pode pegá-la solta, mas porque a troca é total e a Trilha nova precisa funcionar inteira a partir do nível em que você trocou.

> **A palavra `subtrilha` morreu na v0.60 e não volta.** São duas camadas, e agora sem empréstimo nenhum entre elas.


**Q5 — O que cada Trilha entrega, entrada por entrada.** *Última de propósito.* É a passada de conteúdo, e ela só começa depois da Q3.

### 3.6 Qual Classe Passiva em qual degrau — refeito na v0.65

*A v0.64 tinha travado a altura por nível, e ela caiu junto com o empréstimo.* **Os dois motivos daquela regra eram o empréstimo e o tamanho da matriz, e a Q4 refeita matou os dois** — não há mais o que emprestar, e as montagens caíram de 405 para 15. *Com Trilha fechada, o formato passa a ser justamente o que faz uma Trilha parecer diferente da outra.*

> **Cada Trilha escolhe o formato de cada degrau, com duas travas.**
> **1. O nível 2 é sempre `Classe Passiva 1` ou `3`** — condicional ou permanente. **Nunca uso limitado.**
> **2. Pelo menos uma das quatro entregas tem de ser algo que o jogador decide usar** — uso limitado por relógio, **ou condicional que ele ativa gastando um recurso do turno.**

> **A segunda trava foi reescrita na v0.73, e a metade nova é a do recurso de turno.** *Ela dizia "tem de ser `Classe Passiva 2`", que é o formato de relógio e só ele.*
>
> **O que fez mudar foi o `Punho` do Bastião.** Ele reprovava por **formato** e não por preço: as quatro entregas fechavam dentro do orçamento e a régua dava verde, e quem barrava era esta trava. Mas o `Engate` daquela Trilha **gasta a ação bônus** — e decidir gastar a ação bônus é uma escolha que acontece toda rodada, o que é **mais botão** do que um contador de descanso curto que dispara sozinho quando você lembra dele.
>
> **Contra-teste rodado, e ele é o que impede a trava de virar trivialmente verdadeira:** uma Trilha de terreno difícil, Defesa `+1`, resistência permanente e andar `+3 m` **continua reprovando**, porque nenhuma das quatro gasta recurso de turno. *E ela continua pegando o Champion, que é contra quem ela nasceu — lá nada gasta nada.*

**A primeira trava é do Mizuki, e o levantamento externo bate com ela.** *Ele escreveu: "o nv2 tem que dar a BASE para tudo funcionar, como algo passivo mesmo ou que proca às vezes".* A conta já dizia que o nível 2 não pode ser condicional-que-falha-muito — são **18 missões** com ela sozinha na ficha. O que faltava era o outro lado: **uso limitado no nível 2 é pior ainda**, porque a única coisa que a Trilha te dá vira um recurso para administrar antes de você ter qualquer outra coisa na ficha.

**A segunda trava veio de fora, e ela existe porque a preferência do Mizuki, levada ao extremo, tem nome no hobby.** Ele escreveu *"acho que tudo deveria ser entre sempre ligado e às vezes"* — e uma subclasse **só** de passiva e proc é literalmente o **Champion do D&D 5e**, que é o exemplar canônico de subclasse chata:

> *"Most of its features are passive… **this is a subclass that is absolutely desperate for some buttons to push**. The expanded crit range is genuinely useful, but it is a passive that requires no decisions… this simplicity makes the Champion an ideal character for **new players**, but **veterans will likely find it boring**."*

**E a última frase é a resposta inteira: passivo é certo no começo e errado no fim.** É exatamente o que o Mizuki desenhou sem saber — base passiva no nível 2, e o resto variando. A segunda trava só garante que o "resto" tenha pelo menos um botão.

#### E a preocupação com "uma vez por luta" tem número, e ela não se confirma

*Ele escreveu: "ter algo uma vez por luta é meio chato às vezes, tem dias que não vai ter mais de uma luta".* **A peça 10 §4 responde:** *"as três primeiras lutas do dia são de graça"*, e a exaustão começa na quarta. **O dia esperado deste sistema tem três a quatro lutas.**

| relógio | dispara por dia |
|---|---|
| `1×` por descanso curto — o degrau usado aqui | **3 a 4 vezes** |
| `1×` por dia | 1 vez |

**São três a quatro vezes mais.** *E o levantamento externo separa os dois pelo mesmo motivo:* o Stoddard escreve que *"não é um loop de jogo se o jogador só faz aquilo uma vez por dia"* e que *"uma vez por descanso curto está ok"*. **O formato que incomodava é o `por dia`, e este sistema não usa ele em Trilha.**

#### As duas pontas que a conta já tinha fechado, e que continuam

**O nível 2 não pode ser condicional-de-baixa-taxa**, e agora também não pode ser uso limitado — sobra permanente, ou condicional que dispara com frequência. **O nível 29 não pode ser condicional**: você o carrega por 10 missões, e coisa que se vê pouco tempo pede formato que aparece sempre.

*O que morreu nesta versão foi a sequência fixa `3 · 2 · 1 · 3 · 1 · 2 · 3`. Ela existia para as três Trilhas de um Caminho não competirem por confiabilidade, e sem empréstimo elas não competem mais.*

## 4. A ordem de ataque recomendada

**Não é por Caminho, e o motivo é dependência — o mesmo critério que ordenou a fila na v0.36.**

| # | bloco | por quê aqui |
|---|---|---|
| ~~1~~ | ~~**a régua** (Q1 a Q4)~~ | **fechada** — Q1 e Q4 na v0.55, Q2 na v0.60, **Q3 na v0.61**. Peça 13 contra peça 14: régua antes de catálogo é a diferença entre uma versão e seis |
| 2 | **Evocador** — `Servo` · `Matilha` · `Coro` | **as três já têm máquina**, e o rascunho de Invocações já escreveu o que cada uma concede. São o teste barato da régua contra coisa pronta |
| 3 | **Vanguarda** — `Estocada` · `Batedor` · `Executor` | **é a única com dívida numerada** — `6%` a `9%` da Rotina, peça 14 §4 — e com moeda já aprovada para pagá-la: *"acesso a arma é moeda que ela pode gastar"* (v0.45) |
| 4 | **Guia** — `Elo` · `Sutura` · `Perímetro` | fecha o problema de design nº 2, aberto desde a v0.24. A v0.36 já disse que **tudo passa**; falta o número |
| 5 | **Bastião** — `Muro` · `Punho` · `Brasa` | `Muro` encosta em **cobrir-se de energia** (peça 11 §6) e em escudo (peça 14 §4). *A v0.36 já mandou medir as duas juntas: "ou uma domina a outra, ou são a mesma peça com dois nomes"* |
| 6 | **Emanador** — `Torrente` · `Explosivo` · `Arremate` | **`Torrente` é a mais perigosa das quinze** e por isso vai por último: ela é mais de uma ação por rodada, que é a coisa que quebra todo sistema d20. `Explosivo` toca a peça 11 e `Arremate` toca a economia de ação |

**E duas coisas para medir antes de escrever, não depois** — e as quinze Trilhas fecharam na v0.164, então "antes" já passou:

- **A reação de Redução de Dano do Bastião contra cobrir-se de energia**, que já dá RD de `1,5 × refino` por 2 PE. ***Continua sem medida.*** *As três Trilhas do Bastião fecharam na v0.77 sem ela, e o que a medida pode mover hoje é preço de Caminho e de Trilha, não texto de mesa.*
- ~~**Os *pontos de feitiço* do Emanador são moeda nova ao lado do PE**, e toda moeda nova passa pelo `conferir-orcamento.py` antes de ter número.~~ ***SEM OBJETO desde a v0.131:*** **a `Torrente` cobra em PE**, no preço que o manual já dá para a Melhoria `Rápido`. *Não existe lista de pontos à parte, e a peça 6 §9 é a dona do fecho — ela nomeia esta linha.*

## 5. O que o validador vai precisar ter

- **A matriz de dominância entre as quinze**, e ela roda **por Caminho** e **entre Caminhos** — porque a pergunta do Guia contra a Vanguarda é entre Caminhos. *Com a Q4 refeita na v0.65 o tamanho caiu de **405 para 15**: a Trilha é fechada, então cada montagem É uma Trilha. A matriz compara pacote com pacote.*
- **A troca é total, e o validador confere que ela não deixa buraco:** trocar para qualquer Trilha em qualquer um dos três níveis tem de produzir uma ficha legal, com as quatro entregas daquela Trilha até o nível atual.
- **O nível 2 de toda Trilha é `Classe Passiva 1` ou `3`, nunca `2`**, e **toda Trilha tem pelo menos uma `Classe Passiva 2`** nas suas quatro. Contra-teste: uma Trilha só de permanente e condicional tem de reprovar, com a mensagem citando o Champion.
- ~~**Se a Q1 responder "mais de uma"**, a matriz varre as **105 combinações** de duas.~~ **Morta na v0.55:** não existe multiclasse, e a matriz nunca cruza Caminhos diferentes numa mesma ficha.
- **O orçamento de cada Trilha contra os `6%` a `9%` da Rotina**, lido da **peça 14 §4** e nunca de constante. *E ele é **piso**, não teto* — a régua da Q3 para em `14,7%` de propósito.

  > **O TETO NÃO TEM VALIDADOR, e isso é decisão e não esquecimento.** *Até a v0.80 esta linha mandava conferir contra o `+18%` da peça 6 §3.1, e aquele número morreu — ele não reconstrói de nada e a montagem que ele media deixou de ser proibida.* **A v0.81 procurou substituto em três candidatos e nenhum serve:** os que mordem têm dono no playtest, e o único que reconstrói sem playtest — *a técnica continua sendo a maioria da ficha* — só reprova a `10,45×`, dez vezes o orçamento de hoje.
  >
  > **Então o validador confere o PISO e declara que não confere teto.** *Escrever uma checagem de teto contra o pilar 1 seria vestir decisão de conta, que é exatamente o que o `+18%` fazia — e é a lição nº 8: uma checagem que se mede contra a própria constante sai verde na perturbação que importa.*
  >
  > **O que o validador PODE conferir, e vale a pena:** que o orçamento publicado bata com `fatia × fatias`, e que a fatia continue derivando do piso da peça 14. **Perturbar o multiplicador tem de acender ali**, mesmo sem teto.
- **A fatia contra o número de degraus**, e as duas lidas de documento: `piso da peça 14 §4 no nv30 ÷ 8`. Perturbar o calendário da Q2 tem de mover a fatia.
- ~~Contra-teste: um degrau do nv7 que valha uma fatia normal tem de reprovar.~~ **Morto na v0.68:** com o preço por Trilha o degrau do nv7 **deixou de ser exceção**, então um degrau do tamanho de uma fatia é legal e reprovar seria errado.
- **O degrau do nível 7 contra o vão da peça 6 §3** — `físico − conjurador`, no nível —, e **nunca contra constante**.
- **A SOMA das quatro entregas de cada Trilha contra o orçamento dela**, e não cada entrega contra a fatia. *Acrescentado na v0.68, quando a Q3 foi reformulada.* **Contra-teste: quatro entregas de tamanhos diferentes que somem certo têm de PASSAR** — senão a checagem está cobrando por entrega outra vez.
- **Toda entrada declara a taxa de disparo, e o que se confere é `botão × taxa`.** *Nunca a taxa sozinha*, que não tem contra o que ser conferida. **Entrada sem taxa declarada tem de reprovar.**
- **Entrada de utilidade — treino, sentido, comunicação — entra sem preço em dano e tem de ser declarada como tal.** Ela responde a dominância e às travas de forma. *Uma entrada que se declare utilidade e mexa em dano tem de reprovar.*
- **Quem recebe o degrau grande do nv7 e quem recebe o ataque extra no lugar**, contado contra a peça 6 §3.1 — os dois conjuntos têm de ser complementares e cobrir as quinze Trilhas.
- **Nenhuma entrega com dado de dano**, e o contra-teste: perturbar a régua da peça 5 §4 tem de acender.
- **Nenhuma entrega que cresça com refino** — peça 11 §2. *E o contra-teste que dá valor a esta: o refino **cabe** na conta (8,00× contra os 8,31× da Rotina), então uma checagem que só media derivação sairia verde. Ela tem de reprovar pelo eixo da peça 11 §3.*
- **Todo contador de Classe Passiva 2 é plano, e é `por descanso curto`.** Perturbar um degrau para `usos = maestria` tem de acender, e a mensagem tem de dizer que o defeito é a magnitude já crescer. **E perturbar para `por cena` também tem de acender**, com a mensagem apontando a trava de largura da peça 13 §7 — o relógio é o único limitador aqui, então ele leva o spread de `3,0×` inteiro.
- **Todo relógio citado sai da escada da peça 10 §5**, lida daquele documento e nunca escrita aqui. *É a mesma checagem que a peça 13 §7 já faz no catálogo de Legados, e ela achou três relógios fora da escada lá.*
- **O quarto eixo do `Servo`**, quando ele existir: a matriz do `conferir-invocacoes.py` tem de passar a rodar com ele, e as duas entradas do `DOMINANCIA_PENDENTE_Q6` têm de **sumir da declaração**. Contra-teste: tirar o quarto eixo tem de fazer as duas voltarem.
- **O teto de uma Rotina somada**, para `Servo`, `Matilha`, `Coro` e `Torrente`, conferido **pela economia de ação** e não por decreto.
- **A tabela de progressão consolidada**, que esta peça vai finalmente poder fechar: o validador confere que **todo nível entrega alguma coisa de algum documento**, ou que os que não entregam sejam lista declarada.
- **Triagem de todo nome** que as quinze criarem — e é onde mais nome novo vai nascer no projeto inteiro.
- **A cota de ataque extra da peça 6 §3.1** conferida contra o catálogo: só `Arremate` e `Coro` o dão por Trilha, e **o Guia por nenhuma rota**.

> ## ✔ FECHADO na v0.164 — as doze entregas do Evocador, e as quinze Trilhas com elas
>
> ***A decisão que segurava isto era da v0.82:*** *"evocador deixa realmente para outro dia, ninguém vai usar essa classe por enquanto."* **A premissa dela era a primeira mesa de teste não ter Evocador — e ela NÃO mudou.** *Decisão do Mizuki na v0.164: reabrir mesmo assim.* **A decisão da v0.82 fica registrada como superada por escolha, e não por fato.**
>
> **O que destravou de verdade foi a v0.163**, que fechou as duas regras que a peça 15 devia: *quando a vida cheia da invocação reinvocada volta* — descanso longo, derivado da peça 10 §3 — e *o que acontece com a invocação quando o dono cai* — ela fica parada e não pode ser comandada. **Enquanto as duas estavam abertas, nenhuma entrega que mexesse nelas tinha contra o que ser medida.**
>
> **As três estão no `DESENHO-trilhas.md`**, na seção *"O Evocador mecânico"*, com preço, texto de mesa e matriz. *`Servo` `7,32` · `Matilha` `5,05` · `Coro` `7,67`, de `5,00`, com os três estouros declarados.*
>
> ### ⚠⚠ E o que este cabeçalho publicou por trinta e duas versões estava numa escala morta
>
> **Ele dizia que o `Servo` "fecha em `5,07` contra um orçamento de `5,07`".** *Aquele `5,07` é `4 × 1,27`, e a fatia é `5,08` desde a **v0.73** — nove versões ANTES de este cabeçalho ser escrito.* **Na escala de hoje aquela montagem entregava `1,00` fatia de `5,00`: 20% do orçamento.**
>
> *A `LISTA-gatilhos-trilhas` já tinha achado isso na v0.77 e escrito, com todas as letras, que "o `Servo` publicado precisa ser **refeito** e não reajustado".* **O achado nunca voltou para cá nem para o §6.10.** *Um número, dois documentos, duas respostas — e quem estava certo era o que ninguém abre primeiro.*
>
> **E o segundo defeito não era de escala, e ninguém tinha visto:** *a peça 15 §3.4 escreve que o `Servo` e a `Matilha` **comandam e não atacam**.* **Então o nível 27 daquela montagem — "o SEU golpe simples pega 2 alvos" — só pagava na rodada em que o jogador abrisse mão da rodada inteira da invocação.** *E isso não é uma entrega: as quatro maiores linhas da régua de `DESENHO-trilhas.md` dependem de uma Ação Padrão que duas das três Trilhas gastam no `Comando`.*


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

**A trava do fim tem tamanho, e ele é `2,5×`.** *Até a v0.178 a regra de morte da peça 15 §3.5 lia a **vida máxima** para decidir morte em definitivo, e era ela que dava tamanho à trava; hoje a régua é escala fixa, e o que sustenta o corpo forte é durabilidade* — com `h` o `Servo` iria a zero levando **dois quintos** do dano que derruba a `Matilha`, para a **mesma Rotina entregue**:

| nv | vida do corpo (`h`) | corpo forte, `Servo` e `Matilha` | rodadas de chefe concentrando |
|---|---|---|---|
| 2 | 6 | 15 | corpo cru **2,0** · corpo forte 5,0 |
| 10 | 22 | 55 | 1,7 · 4,2 |
| 30 | 62 | 155 | 1,7 · 4,3 |

> **A concessão, fechada:** o corpo do `Servo` tem **`2,5 × h`** — o pool inteiro da `Matilha` num corpo só — e **o orçamento da ficha mais metade**, arredondando para baixo.

**A vida iguala e o orçamento diferencia**, e os dois papéis são diferentes de propósito:

| | por que este eixo |
|---|---|
| **vida `2,5h`** | fecha a trava do *"acabou o kit"*. Os dois passam a sair da luta pelo mesmo golpe, e apagar o `Servo` custa as mesmas `0,83` Rotina de área por alvo que apagar a `Matilha`. **Nenhuma exceção nova** — a regra do §3.5 continua valendo palavra por palavra |
| **orçamento `×1,5`** | é onde o `Servo` fica **na frente**, e é o eixo que mata as duas dominâncias. `8→12` no nv2, `36→54` no nv30 — 48% do que compraria o catálogo inteiro. *Os números são da escala da v0.67; eram `2→3` e `9→13` quando esta seção foi escrita* |

**E o *"não passar muito delas"* está medido:** a `Matilha` compra `9` no nv30 e **aplica os nove cinco vezes**, um por corpo. Em largura de utilidade ela continua na frente; o que o `Servo` compra é profundidade num corpo só.

*O `Coro` fica com `h`, e isso é a troca dele escrita:* ele é o único que **ataca e comanda**, e o único cujo corpo cair não acaba o kit — o dono continua batendo.

> **E a vida não entra por dominância, o que é o motivo de ela ter checagem própria.** Medido: **só o orçamento já zera a matriz.** Tirar o corpo forte sairia **verde** na matriz e desfaria em silêncio a metade da Q6 que a matriz não mede. O `conferir-invocacoes.py` passou a conferir os dois separados, e o `DOMINANCIA_PENDENTE_Q6` foi a **conjunto vazio**.

### 6.4 O formato das doze entradas, e as travas que a matriz achou — v0.66

*Decisões do Mizuki, com a conta rodada antes de cada uma.* A régua da Q3 deixa **38 sequências legais** por Trilha: as duas travas do §3.6 cortam o espaço de 81 para 38. **A média é idêntica nas 38, por construção** — `5,08` de dano por rodada no nível 30. *O que muda é a variância, e é por ela que as três escolhem diferente.*

| Trilha | jeito | forma | desvio | rodada morta | pico |
|---|---|---|---|---|---|
| **`Servo`** | sempre-ligado | três permanentes e um botão | `2,09` | 0% | `8,51` |
| **`Matilha`** | meio a meio | dois permanentes | `2,95` | 0% | `11,94` |
| **`Coro`** | meio a meio puxando pro condicional | **`1 · 2 · 3 · 3`** | `3,29` | 0% | `13,59` |

**Um permanente sozinho já zera a rodada morta**, e é essa a fronteira que separa as três de qualquer coisa pior: a pior sequência legal, `1 · 1 · 1 · 2`, deixa a Trilha sem fazer nada em **37% das rodadas**.

**O `Servo` é sempre-ligado porque a Q6 já tinha decidido isso com outro nome.** A vida do corpo forte existe para o corpo não cair; pôr variância de formato em cima de um corpo só recria pelo formato o *"acabou o kit"* que aquela decisão saiu para fechar.

**A `Matilha` fica no meio porque a variância dela já mora nos cinco corpos.** Ela aplica o orçamento cinco vezes e escolhe qual corpo faz o quê. Empilhar variância de formato em cima disso conta a mesma coisa duas vezes — lição nº 2, no lugar em que ela mais reincide.

**E o `Coro` puxa pro condicional porque o encadeamento é a ficção dele.** *Ordem escolhida pelo Mizuki:* **condicional no nível 2, botão no 11, permanentes no 19 e no 27.** O §3.6 permite condicional no nível 2 desde que ela **dispare com frequência**, e *"a invocação atacou"* dispara em quase toda rodada em que o `Coro` faz o que o `Coro` faz.

#### As três travas de escrita, e elas vêm da matriz e não da ficção

*Rodei a matriz de dominância subindo um eixo de cada vez em cada Trilha — quinze testes, nos cinco eixos que o `conferir-invocacoes.py` já usa mais os dois que a Q6 abriu.* **A base de hoje está limpa: zero dominância.** Três acendem:

| se uma entrega der… | para | acende |
|---|---|---|
| **ação** | `Matilha` | `Matilha > Coro` |
| **orçamento** | `Matilha` | `Matilha > Servo` |
| **ação** | `Servo` | `Servo > Coro` |

> **A `Matilha` não pode receber ação nem orçamento em nenhuma das quatro. O `Servo` não pode receber ação.**
> **O `Coro` está limpo nos cinco eixos** — ele tem mais espaço de escrita que os outros dois, e o motivo é que ele está atrás em vida.

**E os outros doze testes saem verdes, que é exatamente onde mora o perigo.** Dar um segundo corpo ao `Servo` **não acende nada** e mesmo assim borra a diferença dele para a `Matilha`. *A matriz não mede ficção* — é a lição do eixo errado da v0.63 reaparecendo na peça em que ela nasceu.

#### O orçamento de invocação não é a moeda das entregas, e a conta reprova antes da ficção

O orçamento cresce **`4,5×`** na campanha contra os `8,31×` da Rotina. Razão **`0,54`** — ela cai entre os espaços de feitiço (`0,68`) e a maestria (`0,48`) na tabela do §3.5. **Uma entrega escrita em ponto de orçamento vale metade no nível 30 do que valia quando você a pegou.**

*Levantamento externo, e ele bate com a conta:* o **Pathfinder 1e** monta o eidolon gastando um **bolo de pontos de evolução**, e o guia de referência da comunidade descreve o que sai disso — opções-armadilha (*"two evolution points for one secondary attack is a very poor investment"*), escolhas óbvias que todo mundo pega (*"flight is crucial, especially at high levels"*), e um **teto externo de número de ataques que precisou existir só para segurar o resto** (*"without this, eidolons would be fairly ridiculous"*). **O Pathfinder 2e trocou o bolo por tipo fixo mais talentos nomeados** — *"if you retrain this feat, the feat you replace it must also be an evolution feat"* —, com vida compartilhada e uma ação de agir junto uma vez por rodada, que é quase palavra por palavra o que o `Coro` já é aqui.

> **As doze entradas são nomeadas, nunca em branco.** O orçamento continua sendo a concessão fixa do `Servo`, e nenhuma das quatro entregas de nenhuma das três o move.

#### E nenhuma entrega do `Coro` pode supor corpo a corpo

A peça 14 §5 tem a categoria **`Arma de Fogo`** com sete armas, mais a propriedade `Longo Alcance`. *Uma ficha de `Coro` atirando ao lado de invocações que fecham a distância é legal hoje.* **Entrega escrita como *"quando você e a invocação estão adjacentes"* exclui uma montagem que o catálogo já permite** — e quem paga é o jogador que leu o catálogo e montou dentro dele.

#### O slot do golpe do `Coro` mudou, e a mudança mora na peça 6

*Decisão do Mizuki nesta versão:* **o golpe simples do `Coro` e do `Arremate` passa a ser Ação Bônus, com gate na Ação Padrão.** Ela não é entrega de Trilha — é a forma do ataque extra, que sempre foi da peça 6 §3.1, e está escrita lá.

### 6.5 A parede do Evocador: toda moeda dele é maior que uma fatia — v0.67

*Achado tentando escrever as quatro entregas do `Servo`, e ele derrubou três tentativas seguidas antes de aparecer inteiro.* **O problema não é qual entrega escolher. É que a máquina de Invocações não tem troco.**

| moeda do Evocador | % da Rotina | em fatias |
|---|---|---|
| **1 ponto de orçamento** (presença: meia Rotina) | `5,00%` | **4,3** |
| 1 ponto de orçamento (lido como saída: uma Rotina) | `10,00%` | 8,5 |
| invocar de graça, o dia todo | `9,00%` | 7,7 |
| a primeira invocação do dia de graça | `2,57%` | 2,2 |
| **a primeira invocação do dia pela metade** | `1,29%` | **1,1** |

> **E o número que fecha o argumento:** as **quatro** entregas de Trilha do `Servo` somam `4,69%` da Rotina. **Um ponto de orçamento vale `5,00%`.** *A Trilha inteira do Evocador vale, somada, cerca de um ponto — e um ponto é a menor coisa que a peça 15 sabe vender.*

**É por isso que as três tentativas morreram, e as três morreram do mesmo jeito:**

| tentativa | por que morreu |
|---|---|
| entrega em ponto de orçamento | **4,3 fatias** — a menor unidade já é quatro vezes uma entrega. *A deriva de `1,8×` que o §6.2 tinha achado era o problema menor* |
| desconto no custo de invocar | **7,7 fatias**, e não deriva — o problema é tamanho, não derivação |
| qualquer coisa presa em *"quando ela cai"* | **spread de `5,2×` por mestre** — a peça 15 §3.4 mede reinvocações de `0,8` a `4,2` por dia conforme quem mestra. *A peça 13 §7 já reprovou `3,0×` escrevendo que ali o filtro multi-mestre "está falhando, com número em cima"* |

#### Duas regras que a peça 15 deve, e as duas apareceram por tropeço

*Achadas porque o Mizuki não entendeu uma entrega que eu propus — e ele não entendeu porque **não havia o que entender**.*

1. **Quando a vida cheia da invocação reinvocada volta.** O §3.5 daquela peça registra a pergunta e diz que o candidato é o descanso longo, e que é sabor. **Enquanto ela não fechar, nenhuma entrega que mexa nesse relógio tem contra o que ser medida.**
2. **O que acontece com a invocação quando o DONO cai.** A peça fecha o lado vizinho — perder a invocação não tira dano do dono, ele volta a bater sozinho, e o que se perde é só presença — e **nunca escreveu este.**

> **Não dá para precificar uma entrega contra uma linha de base que não existe.** É a armadilha do preço que usa um termo que não existe, na direção em que ela é mais difícil de ver: o termo *parece* existir, porque a pergunta está escrita.

#### E uma linha do permitido que já era verdade

*Eu propus "o `Investir` da invocação usa o seu atributo no lugar do fixo".* **O acerto da invocação nunca teve valor fixo** — o §5 daquela peça exige que nenhuma linha da ficha cresça em ritmo diferente de `+3`, e o contra-teste dela é perturbar a maestria da peça 1 e ver o acerto da invocação andar junto. *A linha do permitido da peça 5 §4 fala do ataque de conjuração **do personagem**, não do golpe dela.*

#### A saída que a conta aponta, e ela é uma categoria que não existe

O orçamento vende **`Traço`** — *o que ela é* — e **`Comando`** — *o que ela faz quando comandada*. **Não existe nada que venda *"o que VOCÊ ganha por ela estar de pé"*.**

*Essa vaga é a única do Evocador que não tem moeda grande presa nela*, e ela é multi-mestre por construção: a invocação está de pé por padrão, e quanto tempo ela fica de pé não é escolha de quem mestra. **É onde as entregas de Trilha do Evocador cabem no tamanho de uma fatia.**

### 6.6 A saída escolhida: quebrar o ponto de orçamento em quatro — v0.67

*Decisão do Mizuki: **quebrar a moeda**.* A §6.5 mediu que um ponto de orçamento vale `4,3` fatias, então a unidade nova tem de ser **um quarto** dele. **Toda a peça 15 é multiplicada por 4**, e o conjunto de montagens legais sai idêntico — escala uniforme preserva o legal exato, então a busca exaustiva e as trinta checagens do `conferir-invocacoes.py` passam sem alteração.

| nível | orçamento hoje | escala nova | `Servo` hoje | `Servo` novo |
|---|---|---|---|---|
| 2 | 2 | **8** | 3 | **12** |
| 10 | 4 | 16 | 6 | 24 |
| 18 | 6 | 24 | 9 | 36 |
| 30 | 9 | **36** | 13 | **52** |

**Só escalar não basta, e a conta mata essa versão.** Com o item mais barato custando 4, a entrega de `+1` fica **morta** nos níveis 2, 11 e 19 — ela só vira coisa no 27, quando as quatro somam um ponto velho. *Isso fura a regra de formato do §3.6: uma permanente tem de valer alguma coisa na rodada em que chega.*

> **Então o degrau de 1 ponto se abre em entradas finas**, e a régua para isso já estava escrita: o §3.7 define o degrau como *"só mexe na própria invocação"* e lista quatro coisas — **como ela anda · o que ela comunica · o que ela percebe · que espaço ocupa.**

#### O teste que decidiu, e ele reprovou três propostas minhas

**Quebrar um degrau chapado só para baixo é aumento de orçamento disfarçado de tabela.** As seis entradas do degrau 1 somam `24` na escala nova, e qualquer sub-régua que some menos entrega orçamento que ninguém decidiu:

| sub-régua | soma | veredito |
|---|---|---|
| comunica 1 · anda 2 · espaço 3 · percebe 4 | 16 | **−33% de orçamento** |
| comunica 2 · anda 2 · espaço 3 · percebe 4 | 17 | −29% |
| percebe 2 · anda 3 · comunica 3 · espaço 4 | 17 | −29% |
| **anda 2 · comunica 3 · percebe 5 · espaço 7** | **24** | **neutra** |
| anda 3 · comunica 4 · percebe 4 · espaço 6 | 24 | neutra, mas empata dois degraus |

**E a ordem não foi escolhida: ela sai da régua do degrau 2**, que cobra `8` porque *"encosta em outra criatura ou no tabuleiro"*. Dentro do degrau 1 vale o mesmo eixo — quanto mais perto de encostar, mais caro. *O par que ancora isso já está escrito no §3.7:* `Miúdo` e `Graúdo` são par, e o que os separa **não é tamanho, é quem sofre** — um passa por um vão, o outro **barra passagem**, e barrar é o inimigo perdendo movimento.

> **`Miúdo` fica em `7`, a um passo do `Graúdo` em `8`.** A distância de um ponto é exatamente a distância que o texto daquela seção descreve.

#### O catálogo do degrau 1, na escala nova

| custo | entradas |
|---|---|
| **2** | `Escalada` · `Nado` — como ela anda, e só ela |
| **3** | `Fala` — o que ela comunica |
| **5** | `Faro` · `Vigia` — o que ela percebe, e o `Vigia` chega em você |
| **7** | `Miúdo` — que espaço ocupa, a um passo de mexer no tabuleiro |
| *8* | *o degrau 2 inteiro, sem mudança de sentido* |

**A prova de que a porta funciona**, contada por busca sobre o catálogo:

| nível | orçamento | a entrega | montagens sem ela | com ela |
|---|---|---|---|---|
| 2 | 8 | `+1` | 23 | **27** |
| 11 | 16 | `+2` | 188 | **306** |
| 19 | 24 | `+3` | 798 | **1.204** |
| 27 | 32 | `+4` | 2.170 | **3.206** |

**Cada entrega abre montagem nova em todo nível**, que é o que a regra de formato exige. *A entrega de Trilha do Evocador é `+1` ponto da escala nova, e ela vale `1,07` fatia — a régua fecha.*

> **A peça 15 subiu junto, na mesma versão.** O catálogo, a tabela de orçamento, as montagens dos shikigami e o `conferir-invocacoes.py` estão todos na escala nova, com arnês rodado. *Esta seção deixou de ser proposta no mesmo commit em que virou regra — que é o único jeito de a lição nº 9 não morder.*

### 6.7 A entrega muda de categoria: ela é da camada de VÍNCULO — v0.68

*Decisão do Mizuki, depois de levantamento externo que ele pediu.* **A entrega de Trilha do Evocador deixa de ser `+1` ponto de orçamento e passa a ser coisa nomeada da camada que o §6.5 achou** — *o que **você** ganha por ela estar de pé.*

**O que derrubou a saída do §6.6 foi uma contradição interna que o levantamento fez aparecer.** As duas frases são da mesma versão:

> **§6.4:** *"As doze entradas são nomeadas, nunca em branco. O orçamento continua sendo a concessão fixa do `Servo`, e nenhuma entrega o move."*
> **§6.6:** *"A entrega de Trilha do Evocador é `+1` ponto da escala nova."*

Se a entrega é um ponto, **as doze entradas são a mesma entrada doze vezes** — e a `Matilha`, que a matriz proíbe de receber orçamento, recebe orçamento nas quatro dela.

> **E a matriz não acusa isso, porque o eixo de orçamento dela é liga-desliga.** O `conferir-invocacoes.py` lê *"mais metade"* da tabela do §3.7 e marca `2` ou `1`; ele **não conta pontos**. Um `+1` para a `Matilha` passa verde por a matriz não saber contar, e não por estar tudo bem. *É a lição do eixo errado pela terceira versão seguida.*

#### O levantamento: ninguém entrega progressão em ponto de orçamento

| sistema | o que cada degrau de progressão entrega | o que custou |
|---|---|---|
| **Pathfinder 2e** Summoner | features **nomeadas**: `Shared Vigilance` · `Eidolon Symbiosis` · `Shared Reflexes` · `Twin Juggernauts` · `Shared Resolve` · `Instant Manifestation` | a customização virou trilha separada — *evolution feats*, que não são progressão de classe |
| **D&D 5e 2024** Beast Master | `Exceptional Training` (7) · `Bestial Fury` (11) · `Share Spells` (15) | tudo é **economia de ação e comando**, e quase nada disso é legal aqui |
| **Pathfinder 1e** Summoner | **o bolo de pontos cresce com o nível** — é a saída do §6.6 | opção-armadilha, obrigação de gastar tudo a cada nível, e a montagem de braços que fez a classe ser a mais reclamada da edição |

**O 1e é o sistema que resolveu igual, e é o cautionary tale. O 2e é a mesma editora desfazendo aquilo dez anos depois.**

#### E o formato que o 2e escolheu é literalmente a categoria do §6.5

Quatro das seis features nomeadas do Summoner do 2e — `Shared Vigilance`, `Shared Reflexes`, `Twin Juggernauts`, `Shared Resolve` — são **os dois lados ganhando de uma vez** por estarem ligados. *O levantamento não trouxe ideia nova: ele confirmou a que este documento já tinha apontado e chamado de "a categoria que não existe", e mostrou um sistema grande construindo a progressão inteira em cima dela.*

#### O que sobrevive do §6.6, e é quase tudo

**A moeda quebrada em quatro fica.** Ela nunca foi só para caber a entrega de Trilha: ela é o que deu granularidade ao catálogo da peça 15, e o degrau de 1 ponto aberto em `2 · 3 · 5 · 7` continua sendo a régua daquela peça. *O que morre é só a frase que fazia dela a entrega.*

#### O que a categoria nova ainda deve

- **Ela não encosta em nenhum dos cinco eixos da matriz** — não é saída, corpo, ação, orçamento nem vida. **É por isso que ela vale para as três Trilhas sem esbarrar na trava da `Matilha`** — e é por isso que ela vai precisar de checagem própria, porque a matriz vai sair verde de qualquer jeito.
- **O preço continua sendo a fatia da Q3:** `1,27` ponto de dano por rodada, que é `1,17%` da Rotina. Cada entrega tem de caber nela.
- **As doze entradas.** Agora elas têm categoria, régua e trava — falta o conteúdo.

### 6.9 A régua da camada de vínculo — v0.68

*Escrita antes de qualquer entrada, que é a recomendação de método que a peça 13 contra a peça 14 deixou.* **Ela fechou três coisas e matou uma linha do permitido.**

> **As contas desta seção continuam valendo; o enquadramento delas mudou no mesmo dia.** Ela foi escrita cobrando **uma fatia por entrega**, e o §3.4-B passou o preço para a Trilha inteira. **Onde estiver escrito "cabe" ou "estoura", leia "cabe numa entrega sozinha" ou "precisa de taxa que divida"** — nenhum dos números se moveu, e é a auditoria desta seção que levou à reformulação.

#### A fatia é plana, e o §3.3 e o §3.5 estavam medindo com réguas diferentes

O §3.3 diz que a entrega vale `1,27` de dano por rodada em todo nível, e que quem cresce é a **quantidade**. O §3.5 diz que toda entrega tem de ser **fração de coisa que cresce**, e reprova valor absoluto. **As duas não valem para a mesma entrega**: se ela é plana, ela não é fração de coisa que cresce; se ela é fração, oito delas somam sessenta e quatro vezes e não oito.

Rodado contra a dívida da peça 14 §4, que é o alvo em todo nível:

| nv | entregas | Rotina | alvo | plana | fração | por Classe |
|---|---|---|---|---|---|---|
| 6 | 1 | 31 | 1,92 | `1,27` **−34%** | `0,36` −81% | `0,82` −58% |
| 14 | 3 | 63 | 4,68 | `3,80` **−19%** | `2,23` −52% | `3,02` −36% |
| 22 | 5 | 94 | 7,41 | `6,34` **−14%** | `5,51` −26% | `5,92` −20% |
| 30 | 8 | 108 | 10,14 | `10,14` **+0%** | `10,14` +0% | `10,14` +0% |

> **A prova não é a plana ganhar — é ela reproduzir os erros que o §3.3 já tinha publicado.** Aquela seção escreve *"34% abaixo nos níveis 5 e 6"* e *"entre 13% e 19% abaixo no miolo"*, e a conta devolve `−34%`, `−19%` e `−14%`. **Mesmo modelo, mesmos números** — o que valida a leitura antes de valer a comparação.

*As três empatam no nível 30 porque é lá que a fatia foi definida. Descendo, a fração desaba: no nível 6 ela entrega um quinto do que a plana entrega.*

**Então a fatia é plana, e o §3.5 fica com a pergunta errada.** A pergunta certa dele nunca foi *"isso é fração de coisa que cresce?"* — é **"isso cresce depois de chegar?"**. Uma entrega que cresce sozinha depois de entrar na ficha soma duas vezes com o acúmulo, e é ela que o §3.5 existe para pegar.

#### O que cada família do permitido custa, medido

*A cadeia sai toda de documento: a peça 6 §4 diz que uma ação padrão a mais **dobra o dano por rodada**, então uma ação vale uma Rotina; a peça 15 §3.3 dá o `+10%` do acerto; e a luta dura `3,3` rodadas pelo §3.2.*

| família | janela | dano/rodada | em fatias | |
|---|---|---|---|---|
| acerto — `+1` no **seu** acerto | permanente | `5,40` | 4,3 | grande |
| **acerto — `+1`, preso no que ela faz (~20%)** | condicional | `1,08` | **0,9** | **cabe** |
| PE — `+1` por rodada | permanente | `5,14` | 4,1 | grande |
| **PE — `+1` por descanso curto** | 1× por luta | `1,54` | **1,2** | **cabe** |
| alvo — seu golpe simples pega 2 | permanente | `11,50` | 9,1 | grande |
| alvo — idem, 1× por luta | 1× por luta | `3,45` | 2,7 | grande |

> **É a parede do §6.5 outra vez, e ela nunca foi da moeda.** Tudo que é **permanente** e encosta na máquina do Evocador vale quatro fatias ou mais. **O que cabe é o que tem janela** — e isso casa de graça com o formato que o §6.4 já tinha fechado, porque o `Coro` puxa pro condicional e a `Matilha` fica no meio.

#### Duração SAI do permitido para efeito de Trilha

| o efeito dura | `+1` rodada é | em fatias |
|---|---|---|
| 2 rodadas | 50% | **43** |
| 5 rodadas | 20% | **17** |
| 8 rodadas | 12% | **11** |

**Não existe comprimento de efeito que faça `+1 rodada` caber.** No melhor caso ela ainda é **onze vezes** uma entrega.

*A conta supõe que o efeito estendido vale uma Rotina por rodada, que é o teto.* Um efeito que não seja dano vale menos — **e o projeto não tem conversão para nenhum deles**, então descer o número exigiria inventar um. **Decisão do Mizuki: duração sai da camada de vínculo e fica registrada aqui com o número**, para ninguém redescobrir. *Ela continua valendo para Caminho e para aptidão, que têm orçamento maior.*

#### Posicionamento entra, com uma previsão declarada e um problema de troco

**O número que falta é quantas rodadas o deslocamento extra decide alguma coisa, e ele só sai da mesa.** *Decisão do Mizuki: fica em `5%`, marcado como previsão* — que é o que o `ESTADO-ATUAL` já diz de todo número do sistema enquanto `04-playtest/` estiver vazia.

| entrega | dano/rodada | em fatias |
|---|---|---|
| `+1,5 m` sempre | `0,90` | **0,71** |
| `+3 m` sempre | `1,80` | **1,42** |
| `+6 m` sempre | `3,60` | 2,84 |

> **O metro exato de uma fatia é `2,11 m`, e ele não está na escala do projeto.** A escala inteira é `1,5 · 3 · 6 · 9 · 18 · 21 · 30`, então sobra ficar **29% abaixo** ou **42% acima**. *É a mesma falta de troco do §6.5, na terceira família em que ela aparece* — e aqui a saída é a janela, como nas outras: posicionamento condicional deixa a janela absorver o que a escala não divide.

#### O que sobra para as doze entradas

`acerto` · `alvo` · `recuperação` · `posicionamento` · `exceção de ação` — **e a última é ilegal para `Servo` e `Matilha`**, que não podem receber ação.

**E o achado que fecha esta seção: os exemplos da escada de Classe Passiva nunca tinham sido preçados.** Ela foi escrita como **forma** — o que separa permanente de reativo de condicional — e as células viraram exemplo sem ninguém converter em fatia. **Dois dos sete não sobrevivem ao contato:** *"+3 m sempre"* está `1,42×` grande e *"+1 rodada sempre"* está `11×`.

### 6.10 ~~O `Servo`, montado~~ — **VENCIDO. Refeito na v0.164** — v0.68

> ## ⚠⚠ TUDO ABAIXO ESTÁ NA ESCALA DE `1,27` POR FATIA, E ELA MORREU NA v0.73
>
> **Esta montagem entrega `1,00` fatia de `5,00` na escala de hoje** — 20% do orçamento —, e o nível 27 dela está pendurado num golpe que o dono do `Servo` não dá. *O `Servo` de verdade está no `DESENHO-trilhas.md`, na seção "O Evocador mecânico".*
>
> **A seção fica, e fica inteira, porque o MÉTODO dela sobreviveu**: a camada de vínculo, a taxa declarada por entrada, e a leitura de que o preço mora na Trilha. *O que morreu foram os quatro números.* **Número errado apagado é número que alguém redescobre** — mesmo molde das colunas velhas da `LISTA-gatilhos`.

*As quatro entregas somam `5,07` de dano por rodada, que é o orçamento de quatro fatias.*

| nv | Classe | família | a entrega | botão | taxa | sai em | fatias |
|---|---|---|---|---|---|---|---|
| **2** | 3 | treino | enquanto ela está de pé, **você é treinado** numa perícia ou num TR que ela tenha | utilidade | — | — | *sem preço em dano* |
| **11** | 2 | recuperação | `+1 PE`, **1× por descanso curto** | `5,14` | `30%` | `1,54` | 1,22 |
| **19** | 3 | posicionamento | `+3 m` de deslocamento enquanto ela está de pé | `1,80` | `100%` | `1,80` | 1,42 |
| **27** | 3 | alvo | o seu golpe simples pega **2 alvos**, com gatilho | `11,50` | `15%` | `1,72` | 1,36 |

> **Somam `5,07` contra um orçamento de `5,07`.** *A montagem não foi ajustada para fechar: as três taxas saem de onde as coisas acontecem — o descanso curto é uma vez a cada `3,3` rodadas de luta, o deslocamento é permanente, e o gatilho do nv27 é o que resta para o alvo caber.*

**O botão está no nível 11 e não no 27, e o motivo é o Champion.** O §3.6 traz a subclasse do 5e como o erro a evitar — *"desesperada por algum botão para apertar"* —, e o argumento inteiro é que **passivo é certo no começo e errado no fim**. Botão no 27 deixa a Trilha sem decisão nenhuma por dezessete níveis.

**E o `+3 m` estar 42% acima de uma fatia é a direção que ajuda:** o §3.3 mediu que a Trilha inteira roda de 14% a 34% **abaixo** do alvo da peça 14 no miolo da campanha.

~~**O que falta escrever nesta Trilha:** o gatilho do nível 27, que é o que fixa os `15%`.~~ **Não existe gatilho que produza `15%`, e a `LISTA-gatilhos` provou isso por subtração na v0.77:** *`5,07 − 1,56 − 1,80 = 1,71`, e `1,71 ÷ 11,50 = 14,9%`.* **A taxa saiu do que sobrou nas outras três, e não de gatilho nenhum.** *Com a lista de gatilhos fechada não existe mais `15%`: existem `100%`, `50%` e `30%`.*

## 7. O que esta peça destrava, e o que ela fecha

| | |
|---|---|
| **destrava** | nada — **ela é a última dependência da fila.** É a peça que os outros esperam, não a que espera |
| **fecha** | o problema de design **nº 2** (Guia contra Vanguarda, aberto desde a v0.24), a pendência **nº 3** e a **nº 4** do `ESTADO-ATUAL`, as três perguntas do §9 da peça 6, e a dívida de `6%` a `9%` da Rotina que a peça 14 §4 registrou |
| **toca** | **100% das fichas.** Nenhuma outra peça da fila faz isso |
