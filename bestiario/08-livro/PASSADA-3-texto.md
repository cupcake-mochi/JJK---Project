# Passada 3 de texto — log

<!-- RESUMO: escrito no fim da passada, aqui no topo. -->

> ✅ **11/09/2026 — a passada 3 de texto FECHOU, inline.** `conferir-voz.py`: **`0` achados** em todos os
> capítulos e no `build.py` (eram `51`), `0` referência pendurada, `0` termo sem destino. Os três geradores
> rodaram depois e não mexeram em nada. **Nenhum número de regra mudou** — cada diferença do guard está
> explicada no capítulo dela, inclusive no `20` e no `30`, que tinham ficado sem registro.
>
> ## ✅✅ 11/09/2026, mais tarde — AS TRÊS PENDÊNCIAS DA PASSADA FECHARAM
> *Os dois pedidos de desenho do `50`, o achado de conta do `60` e as duas frases marcadas pra conferir.*
>
> | | o que fechou |
> |---|---|
> | **desenho do `50`** | **o golpe SAIU do cabeçalho** — ele mora no ataque, em `Ações`, com o alcance junto. **`Ações Múltiplas` passou a CONTAR na linha de entradas nomeadas.** *E o capítulo passou a dizer como se nomeia o ataque: a arma ou a parte do corpo, nunca "Ataque de".* **Medido em `7` sistemas** — `fila/DECIDIDO-as-tres-respostas-da-passada.md` §1 |
> | **conta do `60`** | **a rota `B` venceu** — o orçamento sai do golpe IMPRESSO. **`9` células andaram `0,1`, e não `3`.** *A maior ação do sistema foi de `15,0` pra `14,9` pontos; os `62%` do teto do jogador não mudaram.* Conta em `fila/medir-a-rota-do-orcamento.py`, patch em `ferramentas-claude-2/rota-b-26.py` |
> | **as duas frases de canon** | ❌ **a do `30` era ERRO DE FATO e foi corrigida:** *a Maki não matou o Naoya — foi a MÃE dela, com faca de cozinha, no cap. `152`.* ✅ **a do `40` conferiu e ficou como estava.** Laudo em `07-catalogo/PESQUISA-03b-o-erro-da-morte-do-naoya.md` |
>
> **Os `29` validadores do `Claude 2` seguem verdes, o `conferir-voz.py` segue em `0`, e os dois PDFs
> do livro mais o `bloco-de-inimigo` foram regerados.**

---

> **Três frases que viraram mentira foram corrigidas:** a "célula mais cara" (`50` e `07`), a "Área reparte a
> cota" (`60`) e o "golpe cru" (`90`). **Um achado ficou pro dono da regra** (as três células do orçamento, `60`),
> e **dois pedidos de desenho do `50` continuam com o Mizuki**.

---

## Régua

`GUIA-titulos-e-texto.md` (padrão de título, abertura e explicação de regra, tirado do Livro do
Jogador 2024, do Guia do Mestre 5e, do Caldeirão de Tasha e do DMG 2024) + `REGRA-DE-VOZ.md` e
`METODO-passada-de-texto.md` do `Claude 2` + as reclamações do Mizuki (2.1 títulos, 2.2 abertura e
justificativa, 2.4 enchimento).

Linha de base do `guard_numeros.py`: `build/.antes/` (não mexido).

---

## Ferramenta — `build/conferir-voz.py`

**O furo que deixou os títulos voltarem:** o validador pulava todo `#` (h1), porque no Manual da
Guilda o h1 é o título do capítulo. No Bestiário o título de capítulo mora no `build.py`, e o `#`
de dentro do arquivo é seção. Resultado: "Morreu do jeito errado", "A morte que alguém amaldiçoou",
"O bloco em branco", "A adjacência" e outros passaram limpos pela passada 2. Nome de tabela e as
listas `CHAPTERS`/`FRONT` também não eram lidos.

| mudança | por quê |
|---|---|
| h1 entra na checagem de título | no Bestiário `#` é seção |
| nome de tabela (`{: .tab-titulo }`) entra, marcado `[tabela]` | é citado pelo nome em outro capítulo (`O preço das três células`, `Os seis papéis`). A regra da vírgula não vale para tabela (`Formas, por nível` é nome) |
| títulos de capítulo e de parte do `build.py` entram, numa linha própria | é onde o título de capítulo mora |
| `Passo N ·` sai antes da checagem | `Passo 1 · A categoria` escondia o artigo |
| verbos novos na lista `VERBO`: vira, virou, morreu, amaldiçoou, matou, voltou, ficou, nasceu, sai, saiu, mora, responde, olhando | eram os verbos dos títulos-frase que escaparam |
| h1 conta como destino de termo e como alvo de referência `em *Título*` | mesmo motivo |
| `MOLDURA` na introdução (`05-abertura.md`) vai para a triagem e não conta | a `REGRA-DE-VOZ.md` dá à moldura de leitura um lugar só, a introdução. A passada 2 já tratava os `3` dali como autorizados; o validador é que não sabia |
| `ROTULO-LONGO` diz "não se aplica" quando nenhum arquivo do Manual da Guilda está na pasta | a checagem lê a lista `CAPITULOS` do Manual e a `REGRA-DE-VOZ.md` de lá. Aqui nenhum dos dois existe, e isso fazia o `--estrito` sair `1` **sempre**, com ou sem achado |

⚠ **Para o Mizuki validar:** as duas últimas linhas afrouxam o `--estrito`. As outras seis apertam.

### Linha de base, com o validador novo, antes de mexer em texto

**`77` achados** (o validador velho dava `3`, todos `MOLDURA` autorizada).

| arquivo | achados |
|---|---:|
| `10` | 3 |
| `20` | 2 |
| `30` | 8 |
| `40` | 13 |
| `50` | 9 |
| `60` | 10 |
| `70` | 10 |
| `80` | 2 — `Como usar as seis` (PERGUNTA, CONTAGEM). **Fora do meu escopo** |
| `90` | 6 |
| `build.py` | 15 |

**Títulos ruins que a regex não pega, e que a passada trata à mão:** "Morte de mão limpa"
(metáfora), "Grau e cabeça" (metáfora), "De dentro da arquitetura", "Portas de saída"
(metáfora), "Peso de cada atributo obrigado" (colide com `Peso` do vocabulário), "Fora do
combate", "Desligar e resolver" (verbos no infinitivo), "Como ler o cabeçalho" (encaixe da régua,
mas começa com "Como").

---

# Por capítulo

## `build.py` — títulos de capítulo e de parte

| antes | depois | por quê |
|---|---|---|
| Como usar este livro | **Introdução** | "Como…" e moldura. O Livro do Jogador 2024 e o Guia do Mestre abrem com *Introdução* |
| O vocabulário do livro | **Vocabulário** | artigo; "do livro" não acrescenta |
| O que é uma maldição | **Maldições** | pergunta |
| Os sete tipos | **Tipos de criatura** | artigo e contagem. **Não usei "Tipos de maldição"**, a sugestão do pedido: entre os sete estão `feiticeiro`, `civil` e `restringido`, que não são maldição, e o nome colidiria com a classificação da obra (espírito vingativo, doença…) do capítulo 1. *Tipos de criatura* é o nome que o D&D dá à mesma coisa |
| Gente que vira maldição | **Pessoas e maldições** | frase com verbo. Par de substantivos, a forma do *Dano e Cura* |
| Os lugares | **Lugares amaldiçoados** | artigo; "lugar amaldiçoado" é o termo que o capítulo usa |
| O bloco de inimigo | **Bloco de inimigo** | artigo |
| A montagem em três passos | **Criação de inimigos** | artigo e contagem. Forma do *Criação de Personagens* do Livro do Jogador 2024. "Montagem" ficou com a parte |
| Área, formas e frequência | **Área e frequência** | encurtado: forma é subseção de área. Bate com o arquivo e com o vocabulário |
| Seis maldições prontas | **Maldições prontas** | contagem — entra uma sétima e o título mente |
| Referência rápida | — | já era nome |
| parte "O catálogo" | **Catálogo** | artigo |
| parte "A máquina" | **Montagem** | artigo e metáfora |
| parte "As prontas" | **Fichas prontas** | artigo; "prontas" sozinho não diz o quê |

⚠ O capítulo 8 é do outro agente: só o título dele no `build.py` mudou.

## `05-abertura.md` — Introdução

**Título:** `Peso de cada coisa` → **`Marcas de peso`**. `Fora do escopo` e `Material de apoio` ficam.

| o que era | o que virou | tipo |
|---|---|---|
| "Este livro tem duas metades e elas servem a momentos diferentes da mesa." + um parágrafo por "metade" | dois parágrafos que dizem o que tem em cada parte, **com o número dos capítulos** | reescrita: a abertura agora roteia, como o *Criando um Monstro* do Guia do Mestre |
| "o que acontece quando ninguém saca uma arma" | cortado | drama |
| "sem que você invente um número sequer" | "sem inventar número: tudo sai de tabelas…" | reescrita |
| "**`PADRÃO` é a maior parte do catálogo.** Ele descreve…" (parágrafo à parte, rótulo-frase) | juntado à definição de `PADRÃO` | reescrita |
| "a peça do sistema que é dona dela" | "o lugar do sistema que é dono dela" | jargão interno ("peça" é arquivo do `Claude 2`) |
| "Quando este livro escreve `PADRÃO` ou `FERRAMENTA`, ele está dizendo que…" | "`PADRÃO` e `FERRAMENTA` marcam o que…" | moldura enxugada |
| "Grau de lugar não existe aqui, e a ausência é fiel à obra" | "Lugar não tem grau. Na obra, grau classifica…" | reescrita; o fato fica |
| "Um lugar amaldiçoado tem texto neste livro e não tem ficha." | "…é descrito em texto, no capítulo 4." | ponteiro |

**Guard:** `1` `4` `5` `7` `8` `9` apareceram — são os ponteiros de capítulo novos ("capítulos 1 a 4", "5 a 7", "capítulo 8", "o 9", "capítulo 4"). `metade` sumiu 2× (as "duas metades" viraram "duas partes"). `duas` 4→3 ("ler as duas na ordem" saiu). `um` 5→3 é artigo ("um número sequer", "Um lugar amaldiçoado"). **Nenhum número de regra.**

## `07-vocabulario.md` — Vocabulário

Os títulos já eram nome (é a página que o Mizuki elogiou). Três ajustes de texto:
- abertura: "neste livro" e "Esta é a lista" saíram;
- `REGRA`: "a peça dona" → "o lugar do sistema que é dono dela" (jargão);
- `civil`: "a fonte de tudo" → "a fonte das maldições" (vago). A mesma troca no capítulo 2.

⚠ **Conferir:** `Físicos` diz "Resistir a ele é a célula mais cara". Pela tabela do capítulo 5, resistir a `Físicos` custa `1,43` e a **imunidade** a `Físicos` custa `2,50`: a célula mais cara é a imunidade. O capítulo 5 repete a frase. Não mexi.

Linha 67 (`Ações Múltiplas (N)`) intocada. **Guard:** idêntico.

## `10-o-que-e-uma-maldicao.md` — Maldições

| título antes | depois | por quê |
|---|---|---|
| Grau e cabeça | **Grau e inteligência** | "cabeça" era metáfora |
| As cinco categorias | **Classificação da obra** | artigo e contagem; e "categoria" colide com `Categoria` do capítulo 6 |
| Como a mesa chega | **Serviço** | "Como…", frase |
| Fora do combate | **Comportamento** | nome da coisa |
| tabela *Categorias de maldição* | **Classificação de maldições** | colisão com `Categoria` |

Ficam: `Fatores`, `Invisibilidade`, `Vingativo imaginário`, `Útero amaldiçoado`, `Fixa e errante`, `Véu`, `Véu de terceiros`, `Estrutura de serviço`, `Coordenação`.

**Abertura.** Três parágrafos (a definição; "Ninguém invocou aquilo. Ninguém fez um pacto, desenhou um círculo…"; "Sedimento é uma boa palavra para isso porque…") viraram dois: a definição, com os mesmos fatos, e uma frase que diz o que as seções trazem.

| cortado | tipo |
|---|---|
| "Ninguém fez um pacto, desenhou um círculo ou pronunciou um nome." | drama (o fato "ninguém invoca" ficou) |
| "Sedimento é uma boa palavra para isso porque ela já carrega a parte que interessa…" | o livro comentando a própria palavra; o fato ("o lugar não fabrica a maldição") ficou |
| "acumulando como sedimento no fundo de um rio" | analogia de enfeite (acendia o `TRIAR` do "no fundo") |
| "Três delas são óbvias e a quarta decide." | vago → "O que decide é a convergência." |
| "pelo mesmo motivo que um rio grande carrega mais areia" | enchimento |
| "em três segundos" (caixa de improviso) | drama; a caixa virou instrução direta |
| "Este texto só aponta para ela." | moldura |
| "Uma sala com uma maldição dentro e uma sala vazia são a mesma sala para quem paga a conta de luz. A criatura não precisa se esconder de ninguém…" | drama; repetia a `REGRA` logo acima |
| "O que amadurece ela é a constância do medo." | repetia o rótulo |
| "Uma taxonomia que já nasce com exceção declarada serve para dar vocabulário à mesa, e para nada além disso." | repetia a abertura da seção |
| "inventar um valor aqui seria inventar" | enchimento |
| "A consequência se explica sozinha na mesa, sem que o mestre precise justificar nada." | enchimento |
| "É o mesmo desenho de grau da seção anterior, visto pelo lado do mapa." | o livro falando de si |
| "Ela não nasce neste livro." | moldura (o ponteiro ficou) |
| "Quem não quer molde joga fora e nada quebra." | repetia o que `FERRAMENTA` já diz |

**Reescrito:** "Uma maldição fraca funciona como acidente geográfico…" → "Trate uma maldição fraca como perigo do terreno… Trate uma forte como personagem…" (instrução direta) · rótulos-frase "**Medo constante amadurece rápido.**" → "**Medo constante.**" e "**Quanto mais forte, menos o endereço descreve.**" → "**Maldição forte.**" · "O perigo da errante mede-se em alcance" (ênclise de Portugal) → "o perigo passa a ser o alcance dela" · "**Nenhuma das duas.**" → "**Mesma origem.**" · "o par disso é a errante da seção acima" → ponteiro por nome, "em *Fixa e errante*" · "Um véu que é item é um véu que acaba." → "Um véu desses é item, e se gasta." · "uma cena antes da cena" → "uma cena antes da principal" · "Existe o outro tipo: a errante" → sem a palavra "tipo", que é termo do capítulo 2 · "Comportamento" ganhou uma linha de abertura.

**Canon:** nenhum fato sobre a obra mudou (Mahito, a reunião das quatro, Yuta/Gojo e o véu, cortina encomendada, escola e hospital, útero amaldiçoado).

⚠ **Conferir:**
- "O que decide é a convergência": o texto velho dizia "a quarta decide", e a convergência é o **terceiro** fator da lista. Li como a convergência porque a caixa de improviso usa só ela. Se a quarta era o tempo, a frase nova está errada.
- "É a única categoria em que a mesa vence falando" (vingativo imaginário), e no capítulo 3 "O espírito vingativo é o único […] que a mesa pode resolver em vez de matar". As duas dizem "único", e o espírito vingativo também se resolve conversando. Não mexi em nenhuma.
- "**Uma criatura em vários corpos.** O traço `Núcleos (N)` faz exatamente isso": pelo capítulo 5, `Núcleos (N)` reparte a vida de **um** corpo em núcleos. Não mexi.
- "categoria" no corpo e na coluna da tabela ainda nomeia as cinco da obra, e colide com `Categoria` (`Capanga`…`Calamidade`). Troquei só os títulos. Decidir se o corpo passa a dizer "família", como a abertura da seção já diz.

**Guard:** `cinco` 2→1 saiu do título (`As cinco categorias`). `três` 4→2: "Três delas são óbvias" e "em três segundos", cortados. `duas` 2→1: o rótulo "Nenhuma das duas". `um` e `uma` são artigo. **Nenhum número de regra.** Voz: limpo.

## `20-os-sete-tipos.md` — Tipos de criatura

*Registrado em 11/09 pela sessão que retomou: a passada 3 mexeu no arquivo e não chegou a escrever o log.
Cada linha abaixo foi lida no `diff` contra `build/.antes/`.*

**Título:** a tabela `Os sete tipos` → **Resumo dos tipos** (contagem no nome de tabela).

| o que era | o que virou | tipo |
|---|---|---|
| "Essa palavra é um ponteiro: ela vale por um pacote inteiro de regras que não cabe dentro da ficha, e o pacote mora aqui." | "Cada tipo vale por um pacote de regras que não cabe na ficha, e os pacotes estão aqui." | enxugado |
| "Sete tipos cobrem tudo que a mesa enfrenta" | "São sete tipos" | enchimento |
| "É a referência contra a qual os outros seis são escritos." | cortado | o livro falando de si |
| `civil`: "a fonte de tudo" | "a fonte das maldições" | vago — a mesma troca do vocabulário |
| "a mesa que percebe isso encontra uma conversa difícil esperando" | "Isso rende uma conversa difícil em cena." | drama |
| "a imunidade morde o mundo, e a mesa mal sente … emergência municipal" | "quem sente a imunidade é o mundo, e quase nada o grupo … emergência na cidade" | metáfora |
| "As quatro travas saem da mesma causa vista de quatro lados." | "As quatro travas têm a mesma causa" | enfeite |
| "E a segunda linha da regra é uma virada de cena pronta." | "**Vê sob ameaça de morte** serve de virada de cena" | ponteiro por posição → por nome. *O rótulo existe na regra do `civil`, conferido* |
| "Um corpo amaldiçoado consciente é três coisas se vigiando" | "três almas se vigiando" | vago |
| `Núcleos (N)` × as almas da obra, em três frases de imagem | "Não confunda as almas com o traço `Núcleos (N)` … na hora de aplicar use só o traço." | regra dita com todas as letras |

**Guard:** notação e número idênticos (`3` ocorrências). Extenso: `quatro` 2→1 ("vista de quatro lados", cortado) · `seis` 1→0 ("os outros seis", cortado) · `sete` 2→1 (o nome da tabela) · `um` 20→19 e `uma` 18→16 são artigo das frases reescritas. **Nenhum número de regra.**

## `30-gente-que-vira-maldicao.md` — Pessoas e maldições

*Mesmo registro: mexido pela passada 3, sem log.*

**Títulos:** `Morreu do jeito errado` → **Morte sem energia amaldiçoada** (frase) · `Morte de mão limpa` → **Ferramenta amaldiçoada** (metáfora) · `A morte que alguém amaldiçoou` → **Morte amaldiçoada** (frase) · `O que este livro não responde` → **Lacunas da obra** (pergunta e moldura) · a tabela `Os três estados` → **Estados da pessoa** (contagem). As linhas da tabela seguem os títulos novos.

| o que era | o que virou | tipo |
|---|---|---|
| a abertura: "de três maneiras, e a mesa costuma confundir duas delas. As três merecem nomes separados…" | as três maneiras ditas numa frase, e as seções anunciadas | abertura que roteia |
| "Procure um feiticeiro que morreu na obra e não voltou como coisa, e a busca explica o mundo inteiro em vez de furar a regra." | "Na obra, os feiticeiros que morreram e não voltaram como maldição foram mortos com energia amaldiçoada." | frase vaga que escondia regra — é o exemplo do `GUIA` |
| "Uma regra que dispara uma vez na obra inteira funciona como consequência narrada. Como tabela ela não tem o que preencher." | "A regra dispara uma vez na obra inteira, e funciona como consequência narrada." | enxugado |
| "matar de mão limpa" | "matar de mãos nuas" | metáfora |
| "Nada disso vira número aqui. Um número inventado … seria a única coisa neste livro que não veio de lugar nenhum." | "Nada disso vira número aqui." | o livro falando de si |
| "O grau dele não vinha dele. Vinha do que estava pendurado nele." (no fim da seção) | "O grau dele vinha da Rika, e não dele." (junto do fato) | drama |

⚠ **Conferir:** a frase nova sobre os feiticeiros que morreram é uma generalização sobre a obra que antes estava só implícita. *É leitura, e não medida* — vale conferir contra a obra antes de dar o capítulo por fechado.

⚠ **Conferir:** `Ferramenta amaldiçoada` como título de seção é o nome do termo do sistema. Aqui a seção trata justamente de ferramenta amaldiçoada contar como energia, então não é colisão de sentido.

**Guard:** notação e número idênticos (`4` ocorrências). Extenso: `duas` 2→1 ("confundir duas delas", cortado) · `três` 3→1 ("As três merecem nomes", cortado, e o nome da tabela) · `uma` 13→14 é artigo da abertura nova. **Nenhum número de regra.**

## `40-os-lugares.md` — Lugares amaldiçoados

*Passada inline, 11/09, na sessão que retomou. Voz antes: `13` achados.*

| título antes | depois | por quê |
|---|---|---|
| Os dois motores | **Acúmulo e contaminação** | artigo e contagem; par de substantivos com os dois nomes |
| tabela *Como o lugar ficou assim* | **Motores do lugar amaldiçoado** | "Como…" |
| A adjacência | **Adjacência** | artigo — é o exemplo do `GUIA` |
| A escola | **Escola** | artigo |
| De dentro da arquitetura | **Arquitetura** | locução no lugar de nome |
| O hospital | **Hospital** | artigo |
| O lugar quando ninguém está olhando | **Rotina do lugar** | artigo e frase |
| Como a mesa sai | **Saídas** | "Como…" — exemplo do `GUIA` |
| Desligar e resolver | **Exorcismo e resolução** | verbo no infinitivo |
| O lugar e quem mora nele | **Lugar e morador** | artigo e frase |
| O que este livro não responde | **Lacunas da obra** | pergunta e moldura; o mesmo encaixe do `30` |

Os rótulos `A escola comum`, `A escola de onde a coisa sai` e `A escola dos feiticeiros` perderam o artigo.

**Abertura:** passou a rotear pelas seções, com o nome de cada uma. Saíram "O que vem agora é o lugar como coisa que a mesa atravessa" (moldura) e "neste livro".

| cortado ou reescrito | tipo |
|---|---|
| "As duas convivem." | enchimento |
| "A prisão de menores prova a coisa pelo avesso… Se existe um lugar naquela obra que deveria gerar sozinho, é esse. E não foi ele: foi sabotagem." → uma frase com o mesmo fato | drama |
| "de maneira completamente diferente conforme a escolha, e nada mais precisa mudar" | enchimento |
| "Cemitério sozinho não fez. Prédio vazio sozinho não fez." | simetria forçada |
| "a ferramenta de improviso mais barata do capítulo" | o livro falando de si |
| "A mesma cena entrega um detalhe de mesa de graça" | enchimento |
| "se joga em fatia" → "por partes, como os andares desse prédio" | metáfora |
| "Vale a honestidade:" · "A escola foi o palco dela; o berço foi outro." | moldura · drama |
| "a profissão inteira mora no oposto do que ela caça. E o lugar mais perigoso do mundo…" | drama |
| "A tradição entrega uma promessa com endereço: esta escola tem sete…" | enchimento |
| "e essa liberdade é o que a torna útil" · "é problema seu" | justificativa · tom |
| "é 'encontrar sem lutar' em estado puro" | drama |
| "e é honesto dizer isso" · "A prova mais elegante disso" | moldura · drama |
| "e a licença já está dada pela própria frase de enciclopédia" | justificativa |
| "Não existe rolagem de ataque em lugar nenhum disso." | drama |
| "na cara dura" | tom |
| "e o mestre não precisou ser injusto com ninguém" · "o botão de dificuldade" | justificativa · metáfora |
| "a coisa mais estranha do prédio" | drama |
| "A obra deixou isto em branco… e não confirma nem nega… está marcada como tal" | redundância e moldura |
| "e é isso que separa lugar-inimigo de armadilha chata" | justificativa |
| "ensina a mesa a andar pela parede" → "a mesa aprende a evitá-lo" | metáfora |
| "e escolher entrar é o jogo" | drama |
| "A pergunta deste capítulo até aqui foi…" | moldura |
| "antes de qualquer coisa" · "e a ausência é fiel" | enchimento · enfeite |

⚠ **Conferir:**
- "um dedo plantado e o dedo chamando" virou "um dedo deixado ali, e o dedo atraindo as maldições". *"Plantado" diz que alguém pôs o dedo de propósito nos quatro lugares, e isso talvez não valha para todos* — na escola do primeiro capítulo o dedo estava guardado como selo, se a memória não falha. **Troquei por "deixado" pra não afirmar mais do que o texto sustenta. Conferir contra a obra.**
- "o lugar mais perigoso do mundo é o depósito de uma escola" virou "o depósito é o ponto mais perigoso da escola dos feiticeiros". *Tirei o exagero, e com ele o alcance da frase.*
- Em *Arquitetura*, a segunda frase virou instrução — "Descreva o lugar como de onde a coisa vem". *Mesma ideia, dita como o que o mestre faz.*

**Guard:** notação e número idênticos (`3` ocorrências). Extenso: `dois` 3→2 (o título *Os dois motores*) · `duas` 6→4 ("As duas convivem" e "nunca é a mesma duas vezes", cortados) · `sete` 3→2 ("esta escola tem sete", cortado; "sete é o número da promessa" fica) · `um` 28→22 e `uma` 17→11 são artigo das frases cortadas e reescritas. **Nenhum número de regra.** Voz: limpo, e `0` referência pendurada.

## `70-area-e-frequencia.md` — Área e frequência

*Passada inline, 11/09. Voz antes: `10` achados.*

| título antes | depois | por quê |
|---|---|---|
| Os rótulos de frequência | **Rótulos de frequência** | artigo |
| tabela *Os quatro rótulos* | **Frequência da ação** | artigo e contagem; e o `90` já tem uma tabela *Rótulos de frequência* |
| A área natural | **Área natural** | artigo |
| As três formas | **Formas de área** | artigo e contagem |
| tabela *As formas, por nível* | **Formas, por nível** | artigo |
| tabela *De onde cada uma sai* | **Origem de cada forma** | frase |
| tabela *A parede, por nível* | **Parede, por nível** | artigo |
| A trava de área | **Trava de área** | artigo |

**Abertura:** passou a rotear pelas seções. "e existem quatro" saiu — a tabela mostra.

| cortado ou reescrito | tipo |
|---|---|
| "É o jeito de dar um segundo uso sem prometer um segundo uso." → "Use quando a ação puder sair de novo, sem garantia." | enfeite → instrução |
| "O preço dela já foi fechado supondo que ela pega a mesa inteira, e o pior caso está pago." | justificativa de desenho |
| "Três metros de raio parece pouco… quase o dobro da área de um bicho de nível baixo do resto do hobby." | justificativa (comparação com outro sistema). A instrução de imprimir em quadrados ficou |
| "Formas de graça cobrindo áreas diferentes fariam o mestre escolher sempre a maior, e a escolha de forma seria mentira." | justificativa |
| "São três formas e não cinco… Uma regra cobre as três." | contagem e enfeite; as equivalências ficaram |
| "e sem ela duas mesas desenham áreas três vezes diferentes e as duas estão certas" | justificativa |
| "que é onde a categoria promete deixar ele" | justificativa |
| "Quem age é o esquadrão, e a cota é do esquadrão." → "A cota é do esquadrão, e não de cada corpo." | regra dita uma vez |
| "Quase toda ação de recarga do hobby é em área, e o motivo tem nome" | comparação com outro sistema; a consequência na mesa ficou |

**Duas mudanças de regra no texto, as duas alinhando o livro ao dono:**

- ➕ **como a área natural resolve** — *"Teste de Resistência contra a CD do inimigo: o golpe da ação na falha, e metade no sucesso."* **É a `P1`, aprovada pelo Mizuki em 11/09, e é o texto da peça 26 §6.5.** *Era o pedido do agente dos blocos pra este capítulo.*
- ✏️ **a trava:** *"`1` ação em área à vontade"* → *"no máximo `1` ação em área por rodada"*. **É a forma da peça 26 §6.5** (*"No máximo `1` das ações dele por rodada pode ser em área"*) e a leitura que a `P1` aprovou. *"À vontade" podia ser lido como "uma na luta".* O número não mudou.

**Guard:** notação e número idênticos (`110` ocorrências). Extenso: `cinco` 1→0 e `três` 6→1 ("três formas e não cinco", "Três metros", "três vezes diferentes", "cobre as três", todos cortados) · `quatro` 4→2 ("existem quatro" e o nome da tabela) · `treze` 1→0 e `dobro` 1→0 (a comparação com o hobby, cortada) · `duas` 6→3 ("duas contas", "duas mesas", "as duas estão certas", cortados) · `metade` 1→2 (a regra da `P1`, que entrou) · `um` 11→8 e `uma` 12→10 são artigo. **Nenhum número de regra.** Voz: limpo.

## `50-o-bloco.md` — Bloco de inimigo

*Passada inline, 11/09. Voz antes: `9` achados.* *A região `ATRIBUTOS` e o bloco em branco não foram tocados.*

| título antes | depois | por quê |
|---|---|---|
| O bloco em branco | **Bloco em branco** | artigo |
| As linhas de defesa | **Linhas de defesa** | artigo |
| Portas de saída | **Saídas do aperto** | metáfora — a passada de 10/09 já tinha listado |
| Peso de cada atributo obrigado | **Atributos obrigados** | colide com `Peso` do vocabulário |
| tabela *O que cada um carrega de graça* | **Carga de cada atributo** | artigo e pergunta |
| tabela *O preço das três células* | **Preço das células** | artigo e contagem — o `80` citava pelo nome, e foi junto |
| A linha de entradas nomeadas | **Linha de entradas nomeadas** | artigo |
| tabela *A linha recomendada* | **Linha recomendada** | artigo |
| O bloco seco | **Bloco seco** | artigo — o `60` citava, e foi junto |

`Como ler o cabeçalho` ficou: é o encaixe `Como ler` da `REGRA-DE-VOZ.md`.

| cortado ou reescrito | tipo |
|---|---|
| "A palavra é um ponteiro para o capítulo 2, e vale por um pacote inteiro" | metáfora |
| "Nada aqui é economia nova." | justificativa |
| "jogam completamente diferente" | enchimento |
| "Um chefe carrega a mesma concentração de atributo que um monstro de qualquer sistema de mesa" | comparação com outro sistema |
| "e esse é o preço da ficção" · "E é só isso." | drama |
| "e acabou. Ela é de graça para dar e de graça para tirar." | tom e simetria |
| "É ficção com retorno, e ela paga quem se preparou." | drama |
| "Ela continua vendável. Saiba o tamanho do que você está vendendo." | metáfora |
| "como uma luz que não tem interruptor" · "É aqui que mora a causa de todo número" | analogia · vago |
| "São três em todo bloco que as tem, e contar constante é contar nada." | justificativa |
| "A queixa de 'inimigo com um botão só' existe, e ela sempre foi sobre chefe." | justificativa |

**⚠ Uma frase FALSA, e de número:** *"Resistir a `Físicos` é a célula mais cara que existe."* **A tabela do próprio capítulo dá `1,43` para resistir e `2,50` para ser imune** — a mais cara é a imunidade, e a frase seguinte já falava de imunidade. **Virou "Ser imune a `Físicos` é a célula mais cara".** *O `07-vocabulario.md` repetia a frase e foi junto. A passada de 10/09 tinha visto e deixado.*

**A primeira `Intervenção` ganhou o jeito das prontas:** *"um pouco mais fraco que numa ação normal: nas maldições prontas, é o ataque sem a metade no vizinho"*. **É a `P2`, aprovada em 11/09.** *A frase geral fica, porque é a da peça 26 §6.5.*

**Os dois pedidos do agente dos blocos pra este capítulo continuam com o Mizuki**, porque são escolha de desenho e não de texto:
- a célula `O golpe` no cabeçalho repete o dano que já está nos ataques — **fica ou sai?**
- `Ações Múltiplas` **conta como entrada** na linha de `6`?

**Guard** (contra o arquivo de hoje, antes da passada): notação e número idênticos (`79` ocorrências). Extenso: `três` 12→10 (o nome da tabela, e "São três em todo bloco", cortado) · `metade` 1→2 (a `P2`) · `um` 32→28 e `uma` 19→18 são artigo. **Nenhum número de regra.**

## `60-a-montagem.md` — Criação de inimigos

*Passada inline, 11/09. Voz antes: `13` achados.* *As regiões geradas (`TABELAS` e `EXEMPLO`) não foram tocadas: os três geradores rodaram depois e o capítulo saiu idêntico.*

| título antes | depois | por quê |
|---|---|---|
| Passo 1 · A categoria | **Passo 1 · Categoria** | artigo |
| tabela *O chefe acompanhado* | **Chefe acompanhado** | artigo |
| Passo 2 · O papel | **Passo 2 · Papel** | artigo |
| tabela *Os seis papéis* | **Papéis** | artigo e contagem — o `80` e o `90` citavam, e foram juntos |
| tabela *O que o `Emboscador` paga* | **Vida do `Emboscador`, por categoria** | pergunta; *Pagamento do `Emboscador`* já é o nome da seção |
| Passo 3 · O tamanho | **Passo 3 · Tamanho** | artigo |
| As tabelas de nível | **Tabelas de nível** | artigo |
| Como o mestre escreve uma ação | **Escrita de ação** | "Como…" |
| tabela *O que quinze pontos compram* | **Condição na maior ação** | pergunta e contagem |

**Abertura:** passou a rotear pelos três passos, pelas tabelas e pela escrita de ação. Saíram "sem inventar número nenhum" e "até onde o braço dele chega".

| cortado ou reescrito | tipo |
|---|---|
| "e você lê isso sem tabela nenhuma" | enchimento |
| "porque um esquadrão cheio cobre os próprios buracos" | justificativa |
| "As frações saem com uma casa decimal e isso não é preciosismo: meio ponto percentual atravessa a borda de uma rodada e move o encontro em treze pontos." — o parágrafo inteiro | justificativa de desenho; ela mora na peça 26 §4.5 |
| "como quem troca de bolso o mesmo dinheiro" | analogia |
| "Os seis fecham em `1,000` e o golpe não se move em nenhum deles." → "O golpe não muda em nenhum papel." | calibragem; a instrução ficou |
| "O ganho dele é quase metade a mais num ataque, e um ataque vale mais num corpo de uma ação do que num de seis. O pagamento anda junto." → "O pagamento dele muda com a categoria." | justificativa |
| "Um número certo no lugar errado engana igual a um número errado." | drama |
| "e o motivo do primeiro não é o número" | justificativa — o motivo ficou, atribuído ao `Brutamontes` |
| "A folga está declarada aqui para você contar com ela." → "Conte com essa folga." | moldura |
| "morde o teto de empilhamento" → "limita" | metáfora |
| "É a mesma troca que o jogador faz." | justificativa |

**⚠ Uma frase de REGRA MORTA:** *"**Área reparte a cota.**"* **É literalmente a frase que o commit `A` tirou da peça 26 §6.5**, trocada por "no máximo `1` ação em área por rodada". **O rótulo virou "Área custa ponto"**, e o texto embaixo dele — *um feitiço em área tem menos dados para comprar condição, porque o Fundamento cobra a área em ponto de feitiço* — **continua verdade**, e é o que a decisão da v0.205 disse.

**⚠ Achado e NÃO consertado — é pergunta pro dono da regra, não pra passada de texto.** O agente dos blocos pediu trocar três células do *Orçamento de uma ação, por categoria* (`Catástrofe` nv 10 `4,5 → 4,6` e nv 15 `6,9 → 6,8`; `Calamidade` nv 20 `10,1 → 10,0`), porque o golpe impresso sai do `make.js` com o `0,923` antes do dado. **A tabela do livro bate célula a célula com a peça 26 §6.5, que a checagem `9.1` do `conferir-bestiario.py` valida.** *O repositório tem os dois jeitos de fazer a conta — o bloco com o fator antes do dado, o orçamento com o fator depois da média —, e a diferença é de `0,1` ponto em três células.* **Mexer aqui separaria o livro do dono.**

**Guard** (contra o arquivo de hoje): **notação** — `1` 20→21, `2` 10→11 e `3` 17→18 são os números dos passos que a abertura nova cita · `1,000` 1→0 é a frase de calibragem cortada. **Extenso** — `seis` 3→0 (o nome da tabela, "Os seis fecham", "num de seis") · `treze` 1→0 e `meio` 1→0 (o parágrafo das frações) · `quinze` 2→1 (o nome da tabela) · `metade` 10→9 ("quase metade a mais") · `um` 26→22 e `uma` 26→22 são artigo. **Nenhum número de regra.**

## `90-referencia.md` — Referência rápida

*Passada inline, 11/09. Voz antes: `6` achados.*

| título antes | depois | por quê |
|---|---|---|
| Montar um inimigo | **Montagem** | verbo no infinitivo; é o nome da parte |
| tabela *A montagem, em quatro linhas* | **Passos da montagem** | artigo e contagem |
| tabela *O que trava o inimigo* | **Travas do inimigo** | artigo e pergunta |
| tabela *O que cada célula multiplica no fator* | **Multiplicador de cada célula** | artigo e pergunta |
| Escrever uma ação | **Orçamento de ação** | verbo no infinitivo |

**⚠ Uma frase que virou MENTIRA sem ninguém mexer nela:** *"A `Vida e golpe por faixa` publica o golpe cru."* **Desde a passada 3 dos blocos, a tabela do capítulo 6 traz o golpe de `Desastre`, `Catástrofe` e `Calamidade` já com o `0,923`** — o próprio capítulo 6 diz "Use o golpe como ele está". *Quem seguisse a referência rápida multiplicaria duas vezes.* **Reescrita pra dizer o que a tabela faz.**

**A trava de área alinhada ao dono:** "ações em área, à vontade" → **"ações em área por rodada"**, igual ao capítulo 7 e à peça 26 §6.5. O `1` não mudou. *E a referência a `Os seis papéis` virou `Papéis`.*

**Guard** (contra o arquivo de hoje): notação e número idênticos (`29` ocorrências). Extenso: `quatro` 2→1 (o nome da tabela) · `seis` 1→0 (a referência) · `um` 2→1 e `uma` 7→6 (os dois títulos com verbo). **Nenhum número de regra.**

## `07` e `80` — uma correção e duas referências

- **`07-vocabulario.md`:** "Resistir a ele é a célula mais cara" → **"Ser imune a ele é a célula mais cara"**, pela tabela do capítulo 5 (ver `50`). **Guard: idêntico.**
- **`80-seis-maldicoes.md`**, fora da região das fichas: as referências a `Os seis papéis` e a `O preço das três células` seguiram os nomes novos. **Guard:** notação idêntica (`211`); `seis` 3→2 e `três` 6→5 são os dois nomes. *O gerador rodou depois e as fichas saíram idênticas.*

<!-- PRÓXIMO CAPÍTULO -->
