# MEDIDA — quadrado e retângulo, e as DUAS coisas que a pergunta achou

***Pergunta dele, 10/09/2026:*** *"E se a gente adicionasse tamanhos no formato quadrado e retangular?
meio q a gente n boto mas é uma metrica padrão, acredito eu, tanto pra inimigo quanto pra player"*

**Conta em `medir-quadrado-e-retangulo.py`, saída em `SAIDA-quadrado-e-retangulo.txt`.**
*Toda âncora lida do `partC.js` e do `RASCUNHO-5`.*

> ### A pergunta lê de dois jeitos. Medi os dois, e **os dois têm resposta curta.**
> **E medindo apareceram DUAS coisas que ele não perguntou — e as duas são maiores que a pergunta.**

---

# § 1 · A RESPOSTA CURTA DAS DUAS LEITURAS

## Leitura `A` — a FORMA DA ÁREA

| forma | D&D 2024 | D&D 2014 | PF2e | Draw Steel |
|---|---|---|---|---|
| `Cone` | `40,4%` | `48,4%` | **`62,2%`** | ### **`0%`** |
| `Esfera` / `burst` | `13,5%` | `18,9%` | `10,0%` | **`56,9%`** |
| `Linha` | `17,7%` | `27,4%` | `17,1%` | `13,7%` |
| **`CUBO`** | `4,3%` | `4,2%` | `0,3%` | ### **`27,4%`** |
| `Emanação` | `22,7%` | `0%` | `10,3%` | `0,9%` *(aura)* |
| ### **`QUADRADO` como forma nomeada** | ### **`0`** | ### **`0`** | ### **`0`** | ### **`0`** |

> **O `Cubo` existe e é padrão — `2` de `4` sistemas usam de verdade.**
> **O `Quadrado` como FORMA não existe em lugar nenhum.** *"Square" nos três é a **unidade da grade**,
> não um formato de área. Um cubo visto de cima já É o quadrado.*

## ⚠ E o `Retângulo` já existe aqui — ele se chama `Linha`

**`partC.js`: `Linha`, `18 m por 1,5 m`.** *São dois números. É um retângulo de razão **`12:1`**.*

**O que o campo tem e a gente não é a LARGURA COMO PARÂMETRO:**

| | |
|---|---|
| **Draw Steel** — `241` linhas com largura declarada | `"A x B line"` — larguras `1`(`108`) · `2`(`67`) · `3`(`52`) · `4`(`14`) |
| **a razão mediana deles** | ### **`5:1`** |
| **a nossa** | **`12:1`, e ela é FIXA** — a escada sobe o comprimento e nunca a largura |

> ### ⟹ Não falta um `Retângulo`. Falta a largura da `Linha` poder se mexer.

## Leitura `B` — o CORPO NA GRADE

| sistema | tamanhos | o footprint é | retangular? |
|---|---|---|---|
| **D&D 2024** — `331` blocos | `5`, e é **uma palavra** | quadrado | **`0`** |
| **D&D 2014** — `325` | `6`, uma palavra | quadrado | **`0`** |
| **PF2e** — `4.791` criaturas | `6`, uma palavra | quadrado | **`0`** |
| **Draw Steel** — `1.286` statblocks | `8`, e é **um número** *(`1M` `696` · `2` `168` · `1S` `144` · `1L` `110` · `3` `81` · `4` `51`)* | quadrado | **`0`** |

**Varri `A por B` nos três procurando espaço de CORPO: `9` expressões achadas, `0` de corpo.**
*Todas as `9` são ÁREA — linha e muro.*

> ### ⟹ Footprint retangular não existe no campo. `0` de `3` sistemas, `5.400` criaturas.

## ⚠ MAS a leitura `B` acha um buraco de verdade, e ele é nosso

**A tabela do `tamanho` (`RASCUNHO-5` Passo `3`) diz o ALCANCE em metro e não diz quantos QUADRADOS
o corpo ocupa.**

*O `Grande` alcança `3 m`. Ele ocupa `1` quadrado ou `4`?* **A tabela não responde, e é a pergunta que
a mesa faz primeiro** — *o `Capanga` `Grande` do teto de empilhamento precisa saber onde ele cabe.*

| o campo responde assim | |
|---|---|
| **D&D · PF2e** | `Médio` `1` quadrado · `Grande` `2×2` · `Imenso` `3×3` · `Colossal` `4×4` |
| **Draw Steel** | o número **é** o lado: `size 2` = `2×2`, `size 3` = `3×3` |

> **Isto é execução, não decisão** — *`4` linhas na tabela do Passo `3`, e o campo é unânime no valor.*
> ⚠ **E é DE GRAÇA pelo mesmo motivo do item `16`:** *o `tamanho` já não cobra nada.*

---

# § 2 · 🔴🔴 A PRIMEIRA COISA QUE APARECEU — o `Cone` NÃO TEM LARGURA

**Varri o `partC.js`, o `partB.js`, o `partD.js`, o `partF.js` e as `26` peças.**

| a Forma | o que ela declara | basta? |
|---|---|---|
| `Explosão` / `Aura` | *"Esfera de raio `3 m`"* — **`1` número** | ✅ **sim.** Raio define círculo |
| `Linha` | *"`18 m` por `1,5 m`"* — **`2` números** | ✅ **sim** |
| ### `Cone` | ### *"`4,5 m` saindo de você"* — **`1` número** | ### ❌ **NÃO.** Um cone precisa de comprimento **e** abertura |

**E a abertura muda a cobertura em `3,0×`:**

| a hipótese | de onde ela vem | o `Cone` base cobre | no topo da escada |
|---|---|---|---|
| abertura `0,58` | cone de `60°` — PF 1e e vários VTT | `3` quadrados | `464` |
| **abertura `1,00`** | **D&D 2024** — *"a largura em qualquer ponto é igual à distância"* | `4` | `800` |
| abertura `1,73` | cone de `120°` | `8` | `1.384` |

> ### ⟹ Hoje duas mesas montam o mesmo feitiço e desenham áreas `3,0×` diferentes, e as duas estão certas — porque o manual não diz.

---

# § 3 · 🔴🔴 A SEGUNDA — `Cone` e `Linha` dividem UMA escada e UM preço, e no topo são `20×`

**As `4` Formas de área custam `Leve`. Todas. E a tabela de Escadas põe `Cone e Linha` na MESMA LINHA.**

*Cobertura em quadrados de `1,5 m`, com o `Cone` na hipótese do D&D (`1,00`):*

| degrau | `Esfera` | `Linha` | `Cone` | o maior ÷ o menor |
|---|---|---|---|---|
| `d1` | **`13`** | `3` | `4` | `4,2×` |
| `d2` | `28` | `6` | `18` | `4,7×` |
| `d3` | `50` | `12` | `72` | `6,0×` |
| `d4` | `113` | `20` | `200` | `10,0×` |
| ### `d5` | `314` | **`40`** | ### **`800`** | ### **`20,0×`** |

| | cresce de `d1` a `d5` |
|---|---|
| `Linha` | `13,3×` |
| `Esfera` | `25,0×` |
| ### `Cone` | ### **`177,8×`** |

> ### ⚠⚠ No `d5` o `Cone` e a `Linha` estão no MESMO degrau (`60 m`), pelo MESMO preço (`Leve`), e cobrem `800` contra `40` quadrados.
> **A `Linha` é a única das três que fica dentro da banda do campo no topo** *(o teto do Draw Steel é
> `100` quadrados; a mediana `CR 17+` do D&D é `72`).* **O `Cone` a `800` é `8,0×` o teto do campo,
> e a `Esfera` a `314` é `3,1×`.**
>
> *E isso confirma o que a `MEDIDA-raio-ou-diametro.md` §3 já tinha achado por outro caminho:*
> **"o que está fora de escala é o TOPO".** *Agora tem número, e o `Cone` é o pior.*

---

# § 4 · O ACHADO DE DESENHO — o Draw Steel não tem círculo NEM cone

**`1.371` declarações de área lidas. `0` cones. `0` esferas.**

**E o `burst` deles não é círculo:** *"o número `X` é o raio do burst… tem de estar a `X` **quadrados**
de você"*, e **diagonal custa `1`, sem Pitágoras** — *confirmado na regra e em resenha independente.*

> ### ⟹ Um `3 burst` alcança tudo a `3` quadrados em qualquer direção: é um QUADRADO `7×7`.
> **No sistema mais orientado a grade dos quatro, TODA forma é retângulo:** *`burst` (quadrado
> centrado em você) · `cube` (quadrado colocado à distância) · `line` (retângulo `A×B`) ·
> `aura` (quadrado que anda com você) · `wall` (quadrados contíguos à escolha).*
>
> **É o mesmo argumento da saída `C` do raio × diâmetro:** *o número impresso é o que você conta na
> grade.* **Eles não resolveram renomeando — resolveram tirando a geometria curva do jogo.**

---

# ⟹ § 5 · A RECOMENDAÇÃO, e ela inverte a ordem da pergunta

## `1` · O `Cubo` **entra** — mas é o TERCEIRO da fila, não o primeiro

**É forma padrão de verdade** *(`4,3%` no D&D, `27,4%` no Draw Steel)*, **e o ganho dele é exatamente
o que a `MEDIDA-raio-ou-diametro.md` disse que trava a mesa:** *ele encaixa na grade sem conta de
cabeça e sem quadrado pela metade.*

⚠ **Mas botar uma quarta forma numa tabela onde as três atuais não fecham entre si é empilhar.**

## `2` · O `Retângulo` **não entra** — a `Linha` vira `A × B`

**A largura passa a subir com a escada, como no Draw Steel.** *Isso não é forma nova: é um número que
já está impresso deixando de ser fixo.* **E resolve metade do `20×`** — *a `Linha` é a única das três
dentro da banda do campo, e ela só está lá porque é magra demais.*

## `3` · O footprint na tabela do `tamanho` **entra, e é de graça**

**`Médio` `1` quadrado · `Grande` `2×2` · `Imenso` `3×3` · `Colossal` `4×4`.**
*Unânime nos três sistemas, e o `tamanho` já não cobra nada.*

## ⚠⚠ `4` · MAS ANTES DOS TRÊS: a abertura do `Cone`, e o preço das três formas

> ### Estes dois não são "melhoria". São defeito publicado.
> **`4a`** — *o `Cone` precisa de abertura escrita.* **Recomendo `1,00`, a do D&D 2024** — *é a mais
> usada, ela deixa o cone base em `4` quadrados, e o texto sai em uma frase: "a largura do cone em
> qualquer ponto é igual à distância daquele ponto até você".*
> **`4b`** — *`Cone`, `Linha` e `Esfera` custam `Leve` e cobrem `20×` de diferença no topo.* **Ou os
> três saem da mesma escada, ou o preço deixa de ser um só.**

---

# § 6 · ⚠ E ISSO MEXE NOS DOIS LADOS DA MESA — ele estava certo nisso

**O inimigo usa estas mesmas Formas.** *A peça 26 §6.5: o orçamento de uma ação é `golpe ÷ 4,5`, e o
mestre monta no Fundamento — **o mesmo `partC.js`**.*

| | de quem é |
|---|---|
| a **área natural** do inimigo *(sopro, rugido)* | ✅ **já fechada** — raio por nível, `RASCUNHO-5` |
| a área que sai de **técnica**, no inimigo E no jogador | ⚠ **é o `partC.js`, e é este arquivo** |

> ⚠ **E por isso os quatro cruzam com o item `15`, que ele mandou só anotar.**
> *O `4a` e o `4b` são conserto de defeito e dão pra fazer sem reabrir o `15`.* **O `1` e o `2` são
> desenho novo no lado do jogador, e aí é o `15`.**

---

# § 7 · O QUE NÃO PRECISA DE MARTELO

| | por quê |
|---|---|
| **`Quadrado` como forma nomeada** | ❌ **não existe em `0` de `4` sistemas.** *"Square" é a unidade da grade. Um `Cubo` visto de cima já é o quadrado* |
| **footprint retangular de CORPO** | ❌ **`0` de `3` sistemas, `5.400` criaturas.** *As `9` expressões "A por B" achadas são todas ÁREA* |
| **`Retângulo` como forma nova** | ❌ **a `Linha` já é um** — `18 × 1,5 m`, razão `12:1` |

---
---

# § 8 · A SEGUNDA PERGUNTA — "a nossa `Linha` origina da gente"

***Ele, 10/09/2026:*** *"E o nosso linha origina da gente, a gente nunca pensou algo como linha sendo
colocada em um ponto, como parede de fogo do dnd"*

> ### A observação está certa. **A conclusão não — e o campo é quem diz.**

## `8a` · ⚠ PRIMEIRO, UMA CORREÇÃO NA PREMISSA: o Pathfinder NÃO tem cubo

**O PF2e tem QUATRO tipos de área, e o cubo não é um deles:** *`emanation` · `burst` · `cone` ·
`line`.* **Confirmado na regra publicada** *(Archives of Nethys / Roll20 Compendium)*, **e nos dados:
`2` menções a cubo em `663` habilidades de monstro — `0,3%`.**

| quem tem cubo de verdade | |
|---|---|
| **D&D 2024** | ✅ `4,3%` das menções de forma |
| **Draw Steel** | ✅ **`27,4%`** |
| **Pathfinder 2e** | ❌ **não tem** — `4` áreas, nenhuma cúbica |

> **⟹ O cubo é `2` de `3`, não `3` de `3`.** *Ainda é padrão — mas a validação que ele pediu contra o
> Pathfinder dá o contrário.*

## `8b` · ⚠⚠ E A ORIGEM: a gente JÁ BATE com os dois, exatamente

*Medido no texto de `220` áreas de monstro do D&D 2024 e `558` do PF2e.*

| forma | D&D 2024 — colocada num PONTO | PF2e — colocada num PONTO |
|---|---|---|
| `Cone` | ### **`0` de `57`** | ### **`0` de `368`** |
| `Linha` | ### **`0` de `25`** | ### **`0` de `101`** |
| **`Esfera` / `burst`** | **`8` de `11`** — `72,7%` | **é a definição:** *"parte de um canto de um quadrado **dentro do alcance**"* |
| `Emanação` | `0` de `32` — todas de você | `0` de `61` — todas de você |

> ### ⟹ Nos DOIS sistemas, `Cone` e `Linha` saem SEMPRE do conjurador. `0` de `551`.
> **Quem é colocada num ponto é a ESFERA — e é exatamente o que a nossa `Explosão` faz.**
>
> **A nossa tabela já é o desenho do campo, célula por célula:**
> `Explosão` = esfera **num ponto a até `18 m`** · `Aura` = esfera **em você** · `Cone` = de você ·
> `Linha` = de você.

## `8c` · ⟹ Então a "parede de fogo" NÃO é uma linha num ponto — e ela JÁ EXISTE aqui

**No D&D a `Wall of Fire` não é a forma `Line`.** *As seis áreas do D&D 2024 são `Cone` · `Cube` ·
`Cylinder` · `Emanation` · `Line` · `Sphere`.* **`Wall` não é uma delas** — parede é construção
própria, com duração e com corpo.

**E o nosso `partD.js` já tem as três peças, todas publicadas:**

| a peça | família | custa | o que faz |
|---|---|---|---|
| ### **`Anteparo`** | `Controle` | **`Média`** | ### *"Deixa uma **parede** ou escudo com `10 × Classe` de pontos de vida, por `1` minuto."* |
| **`Fica`** | `Área` | `Média` | *"A área continua ali por `1` minuto. Quem entrar ou começar o turno nela leva metade dos dados."* |
| **`Terreno`** | `Controle` | `Leve` | *"A área vira terreno difícil, ou fica obscurecida, por uma rodada."* |

> ## A `Parede de Fogo` do D&D, montada na nossa máquina hoje, sem regra nova:
> ### `Linha` + `Fica` (`Média`) — a área que fica queimando
> ### ou `Anteparo` (`Média`) + dano — a parede com vida que bloqueia
>
> **Ele não achou uma forma que falta. Ele achou uma montagem que ninguém tinha escrito.**

## `8d` · 🔴 MAS O `Anteparo` TEM O MESMO DEFEITO DO `Cone` — ele não tem dimensão

> *"Deixa uma **parede ou escudo** com `10 × Classe` de pontos de vida, por `1` minuto."*

**Não diz o comprimento. Não diz a altura. Não diz onde ela é colocada.**

| a peça | dimensões que ela declara | basta? |
|---|---|---|
| `Explosão` | raio | ✅ |
| `Linha` | comprimento **e** largura | ✅ |
| ⚠ `Cone` | só comprimento | ❌ |
| ⚠⚠ **`Anteparo`** | ### **nenhuma** | ❌ |

**E o campo dá os três números de graça:**

| | comprimento | altura | espessura |
|---|---|---|---|
| **D&D 2024 · `Wall of Fire`** | `18 m` | `6 m` | `0,3 m` |
| **Draw Steel · `X wall`** | `X` quadrados **contíguos, à escolha** — *cada um partilhando um LADO, não um canto* | empilháveis | `1` quadrado |

> **O Draw Steel resolve por um caminho que a gente já tem meia peça:** *o `Contorno` (`Leve`) já diz
> "a área faz curva, dobra esquinas".* **A parede deles é isso levado ao fim — quadrados contíguos
> desenhados um a um.**

## `8e` · E o preço da ORIGEM já está publicado — de trás pra frente

**A Restrição `Corpo a Corpo` devolve `Média`:** *"Projétil vira Toque. **`Explosão` vira `Aura`,
centrada em você.** `Cone` e `Linha` já saem de você, então não podem pegar esta."*

> ### Trocar "num ponto" por "em você" DEVOLVE `Média`. Então "num ponto" vale `Média`.
> **O número pra colocar qualquer coisa num ponto já existe — falta a linha que vende ele.**
>
> ⚠ **E o texto do `Corpo a Corpo` ADMITE a assimetria e para ali:** *"`Cone` e `Linha` já saem de
> você, então não podem pegar esta."* **A ida está escrita; a volta não.**
>
> ⚠⚠ *Mas cuidado com o `Média` cru:* **o `Corpo a Corpo` empacota DUAS coisas** — a queda de alcance
> (`18 m` → `1,5 m`) **e** a troca de origem. *Pro `Anteparo`, que já é colocado, a origem sozinha
> deve valer menos.* **Ancorar em `Média` é o teto, não o preço.**

---

# ⟹ § 9 · O QUE FAZER, na ordem — validado contra D&D e Pathfinder

| ordem | o quê | valida? | custo |
|---|---|---|---|
| **1º** 🔴 | **escrever a abertura do `Cone`** — *"a largura em qualquer ponto é igual à distância até você"* | ✅ **D&D 2024, palavra por palavra.** *PF2e: "o cone se alarga conforme avança"* | **uma frase** |
| **2º** 🔴 | **dar dimensão ao `Anteparo`** — comprimento, altura, e que ele é COLOCADO | ✅ **D&D `Wall of Fire`: `18 × 6 × 0,3 m`.** *E o `Anteparo` já tem vida e duração* | **uma linha** |
| **3º** 🔴 | **o preço das três formas** — `Leve` pra todas, e `20×` de cobertura no `d5` | ⚠ **o campo não valida nenhum dos três topos** — `800` quadrados é `8×` o teto do Draw Steel | **régua** |
| **4º** ✅ | **footprint na tabela do `tamanho`** — `2×2` · `3×3` · `4×4` | ✅ **`3` de `3` sistemas, unânime** | de graça |
| **5º** | **o `Cubo` entra** como quinta Forma de área | ⚠ **`2` de `3`** — D&D `4,3%`, Draw Steel `27,4%`, **PF2e não tem** | forma nova |
| **6º** | **a `Linha` vira `A × B`**, largura na escada | ✅ Draw Steel, `241` linhas, mediana `5:1` | número solto |

## ❌ E o que NÃO fazer, com o motivo medido

| | por quê |
|---|---|
| **`Linha` colocada num ponto** | ### **`0` de `551`** áreas de `Cone`/`Linha` no D&D e no PF2e são colocadas num ponto. *A "parede de fogo" não é uma linha: é `Anteparo`, e ele já existe* |
| **`Retângulo` como forma nova** | a `Linha` já é um — `18 × 1,5 m`, razão `12:1` |
| **`Quadrado` como forma nomeada** | `0` de `4` sistemas. *É o `Cubo` visto de cima* |
| **footprint retangular de corpo** | `0` de `3` sistemas, `5.400` criaturas |

> ### ⚠ Os TRÊS primeiros são conserto de defeito publicado, e dão pra fazer sem reabrir o item `15`.
> **Do `4º` pra baixo é desenho no lado do jogador — e aí É o item `15`.**
