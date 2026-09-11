# A `Intervenção` — sai da cota ou é ação extra?

*10/09/2026. Conta em `medir-a-intervencao.py`, saída em `SAIDA-intervencao.txt`.*

> **As duas frases estão escritas, em documentos diferentes, e ninguém tinha encostado uma na outra:**
>
> *peça 26 §6.1:* **"Tudo que ele faz sai do dano por rodada da ficha"**
> *`a-intervencao.md`:* **"Ela acontece logo depois do turno de outra criatura"** — logo, é uma ação a mais na rodada

---

## 1 · O tamanho do buraco

*Numa luta de `3` rodadas, com no máximo `1` por rodada, ele dispara `3` Intervenções.*

| leitura | dano/rodada | dano na luta | vs a tabela |
|---|---|---|---|
| **A** — sai da cota | `219` | `657` | `1,00×` |
| **B** — é ação extra | `292` | `876` | **`1,33×`** |

> **A leitura `B` entrega `+33%` na luta inteira, por fora da escada.**
> *Pelo invariante `pessoas²` do papel, `1,333×` de dano pede `1,15×` de pessoas — um `Desastre`
> passaria a pedir **`4,6`** em vez de `4`.*

---

## 2 · ⚠ A leitura `A` tem um defeito de DRAMATURGIA, e ele é grave

**Se a Intervenção sai da cota, a rodada em que ele intervém tem `4` fatias em vez de `3`, com o mesmo total.**

| rodada | fatias | `o golpe` | fatia da vida de um PC |
|---|---|---|---|
| sem Intervenção | `3` | `73,0` | `30%` |
| **com Intervenção** | `4` | **`54,8`** | **`22%`** |

> ### Na rodada em que o chefe puxa a jogada grande, TODOS os golpes dele ficam MENORES.
> **A `Intervenção` foi desenhada pra ser *"o caba puxa um ATAQUE DO CRL"*.** *Nesta leitura ela é o
> contrário: ela **dilui** a rodada.*

---

## 3 · O campo já respondeu, e a resposta está escondida num descasamento

**O modificador de organização do Draw Steel é DUPLO, e o `Solo` é o único posto que descasa:**

| posto | `Stamina` | `EV` e dano | razão |
|---|---|---|---|
| `Minion` · `Horde` · `Platoon` · `Elite` · `Leader` | — | — | **`1,00×`** |
| **`Solo`** | **`× 5`** | **`× 6`** | **`1,20×`** |

> **O `Solo` custa `20%` a mais do que a Stamina dele sugere. E o que ele tem a mais é exatamente:**
> **as `3` villain actions** *(a nossa `Intervenção`)* **e** *"Solo Turns: The creature can take two
> turns each round"*.

> ### ⟹ O Draw Steel diz que a ação fora do turno é EXTRA, e que ela SE PAGA NO CUSTO.
> **Ele não dilui a rodada do `Solo` — ele cobra mais caro por ele.**
>
> *E os tamanhos batem: eles cobram `1,20×`, a nossa leitura `B` pede `1,33×`. Dois sistemas, dois
> desenhos, a mesma ordem de correção.*

---

## 4 · As saídas, com o número de cada

| saída | o que muda | custo |
|---|---|---|
| **A** — sai da cota | nada na escada | **dilui a rodada grande.** `o golpe` cai pra `22%` justo quando ele deveria brilhar |
| **B1** — extra, e a escada **recalibra** | o fator de dano do `Desastre` cai de `1,00` pra **`0,750`** — dano `164` em vez de `219`, e `o golpe` vai pra `22%` | **toda linha de toda categoria do `TABELA.md` muda** |
| **B2** — extra, e a categoria **pede mais gente** | o `Desastre` passa a pedir **`4,6`** pessoas | **quebra o "`4` = a mesa padrão"**, que é a âncora da escada inteira |
| **B3** — a Intervenção **não faz dano** | ela move, posiciona, aplica condição — adiciona `0,00` | **contradiz a ficção.** O `Domínio Encolhido` do Sukuna entrega `18` sem rolagem, e *"o golpe final"* que não causa dano não é o golpe final |
| **C** — ela **troca por uma ação** | ver abaixo | a `Intervenção` deixa de ser **de graça** |

---

## 5 · A saída `C`, que ninguém tinha olhado — e ela fecha exato

> ### Na rodada em que ele intervém, ele age `2` vezes no turno dele em vez de `3`, e a ação que sobrou acontece FORA do turno.

| | ações no turno | + Intervenção | total da rodada | `o golpe` | fatia |
|---|---|---|---|---|---|
| rodada normal | `3` | `0` | `219` | `73,0` | `30%` |
| **rodada com Intervenção** | **`2`** | **`1`** | **`219`** | **`73,0`** | **`30%`** |

| | |
|---|---|
| **o total da luta** | **`657`** — exatamente o da tabela. **Zero de correção** |
| **`o golpe`** | `73,0` (`30%`) em **toda** rodada. A banda não se move |
| **a dramaturgia** | **inverte em relação à `A`**: em vez de diluir a rodada, ele **guarda um golpe pro momento certo** |

### ⚠ O que ela custa, e a decisão que ela reabre

**A `Intervenção` deixa de ser de graça** — e ela foi desenhada de graça, no molde da Villain Action.

*E isso já foi decidido uma vez: a saída `B` do §8 das `decisoes-fase-1` morreu por exatamente esse
motivo — **"a Intervenção deixa de ser gratuita, e ela foi desenhada gratuita"**.*

> ### Mas tem uma diferença que vale olhar antes de descartar de novo.
> **Lá o custo era um POÇO — uma contagem nova no bloco.**
> **Aqui o custo é uma ação que ele já tinha.** *Não existe contador novo, não existe linha nova no
> bloco: é a mesma economia de ação que já está escrita.*

---

## 6 · E um documento desatualizado que apareceu no caminho

**O `RASCUNHO-1` do Sukuna carrega a versão VELHA da Intervenção:**

> *"Usos: `3` **por rodada**. Logo depois do turno de outra criatura, o Sukuna gasta um uso. **Os usos
> voltam no começo do turno dele**."*

*Isso é Ação Lendária do D&D, e não a decisão de 08/09* — **`3` por luta, cada uma uma vez, no máximo
`1` por rodada.** *O bloco precisa ser atualizado quando alguém mexer nele.*

---

# 7 · ⚠ FUI OLHAR COMO O DRAW STEEL FAZ, e a resposta deles não é conta

***Cobrança do Mizuki, 10/09/2026:*** *"N é só validar o como é feito no sistema q estamos nos
baseando e vendo o como eles lidam com essas questões? Acredito q as villain actions por exemplo, n
saem do custo da ficha, eles devem ter uma metodologia pra balancear isso tudo."*

**Ele estava certo nas duas pontas. Fui ler o `Draw Steel: Monsters`, e:**

## 7.1 As villain actions NÃO custam `EV` — confirmado

> *"A creature can use a villain action at the end of any other creature's turn during combat.
> Villain actions are numbered and intended to be used in a specific order that creates a logical
> encounter flow and cinematic arc, but you can use them in any order you choose."*

**Elas são embutidas no `Leader` e no `Solo`. Não há custo, nem em `EV`, nem em recurso.**

## 7.2 E — o achado que muda a pergunta — **não existe conta publicada de por quê**

**Procurei a explicação de como o `Solo` se equilibra tendo `3` villain actions grátis MAIS dois
turnos por rodada. Ela não existe no livro.**

*O que existe é uma âncora de RESULTADO:*

> *"A solo creature is an encounter all on their own… **A solo creature can typically stand
> toe-to-toe with six heroes of the same level.**"*

**E a fórmula de `EV` reproduz exatamente isso** — o `Solo` de nível `5` dá `EV 84`, e a força de
encontro de um herói de nível `5` é `14`. **`84 ÷ 14 = 6` heróis.** *Bate com a prosa, seis de seis.*

> ### ⟹ A metodologia deles é: **calibrar o TOTAL pelo resultado, e não itemizar as partes.**
> **Eles não somam "3 villain actions = tanto".** *Eles dizem "isto vale seis heróis", põem o número
> que vale seis heróis, e as villain actions ficam dentro dele sem nunca aparecerem numa linha.*

## 7.3 E a digital de onde isso foi pago está no descasamento

**O `Solo` é o ÚNICO posto em que os dois modificadores de organização discordam:**

| posto | `Stamina` | `EV` e dano | razão |
|---|---|---|---|
| `Minion` · `Horde` · `Platoon` · `Elite` · `Leader` | — | — | **`1,00×`** |
| **`Solo`** | **`× 5`** | **`× 6`** | **`1,20×`** |

> **Eles não escrevem que estão cobrando pelas villain actions. Mas o `Solo` custa `20%` a mais do
> que a Stamina dele sugere, e o que ele tem a mais é exatamente as villain actions e o turno duplo.**

---

## 7.4 O que isso muda na nossa decisão

**A pergunta *"a `Intervenção` sai da cota ou é extra?"* é uma pergunta de ITEMIZAÇÃO. O campo não
itemiza.**

*Eles fixam o resultado — **"aguenta seis heróis"** — e conferem na mesa.*

> ### E o Projeto-M tem a mesma âncora de resultado, já escrita: **"`Desastre` = a mesa padrão de `4`"**, e **`3,0` rodadas de duração**.

**Só que ele não pode usar a metodologia deles ainda, e o motivo é conhecido:** *a pasta
`04-playtest/` está vazia desde a v0.1, e a única mesa que existe — a de ND 20 — foi rodada **sem
ficha de inimigo**, improvisando. **Ela não testa a `Intervenção`.***

### ⟹ Então a escolha muda de critério

**Não é mais *"qual leitura é a certa?"* — é *"qual leitura é a mais BARATA DE DESFAZER quando uma
mesa finalmente medir?"***

| saída | custo de desfazer |
|---|---|
| **`C`** — troca por uma ação | **baixo.** Uma frase na regra da `Intervenção`. Nenhum número publicado se move |
| **`A`** — sai da cota | **baixo.** Também é uma frase, e nenhum número se move |
| **`B1`** — a escada recalibra | **alto.** Toda linha de toda categoria do `TABELA.md` mudaria, e voltaria a mudar |
| **`B2`** — a categoria pede mais gente | **alto.** A âncora de leitura da escada inteira se desloca — e é ela que o campo diz ser o único chão confiável |

> **As duas baratas são a `C` e a `A`, e entre elas a conta já separou:** *a `A` **dilui** a rodada
> grande (`o golpe` cai de `73` pra `54,8` justo quando o chefe deveria brilhar); a `C` mantém `o
> golpe` em `73` em toda rodada e faz ele **guardar** um golpe pro momento certo.*

---

# 8 · A SIMULAÇÃO — não itemizar, e conferir na mesa

***Decisão do Mizuki, 10/09/2026:*** *"Copiar metodologia: não itemizar. A gente faz os cálculos em
uma mesa e já considera que essas ações de intervenção vão pesar mais na mesa, **a gente apenas
calcula para não virar um TPK garantido rodada 1-2**. No fim do dia isso ainda é matemática pura, dá
pra validar sem um playtest."*

**Ele estava certo: dá. E o projeto já tinha a métrica pronta — e ela já vem validada contra dois
sistemas de fora.**

> *peça 26 §4.6:* **"Numa luta de três rodadas ele derruba `2,70` pessoas se concentrar"** — *e
> **"o d20 de 2014 derruba `2,56` a `2,70` numa luta de três rodadas, e o chefe solo do Pathfinder 2e
> derruba perto de `2,8`"**.*

## 8.1 O modelo reproduz as âncoras exatas — então ele é confiável

| conferência | |
|---|---|
| `219 × 3` = **`657`** | e a peça 26 §4.7 publica `657` |
| `78,75 × 4` atacantes `× 3` rodadas = **`945`** | e a vida do `Desastre` é `945`. **A linha do grupo mata ele em `3,0` rodadas, ao ponto** |

## 8.2 O resultado, no modelo sem atrito — o modelo da própria peça 26

| cenário | dano/rodada | na luta | **pessoas derrubadas** | na banda do campo? |
|---|---|---|---|---|
| **sem Intervenção** | `219` | `657` | **`2,70`** | **sim** |
| **com `3` Intervenções, de graça** | `292` | `876` | **`3,60`** | **NÃO** |
| **com `3`, trocando por uma ação** | `219` | `657` | **`2,70`** | **sim** |

> **De graça, ele derruba `3,60` de `4` pessoas — `+33%` sobre o alvo publicado, e `+0,80` acima do
> teto do campo.**

## 8.3 A pergunta do Mizuki, respondida: **não vira TPK na rodada 1-2**

| rodada | sem Intervenção | com `3` de graça |
|---|---|---|
| `1` | `0,90` caídas | `1,20` caídas |
| `2` | `1,80` | **`2,40`** |
| `3` | `2,70` | `3,60` |

> ### Nenhum cenário vira TPK na rodada `1` ou `2`. O pior derruba `2,40` de `4` na rodada `2`.
> **A barra que ele pôs está limpa.**

## 8.4 ⚠ Mas o modelo COM ATRITO acha uma coisa que a barra não pegava

*A peça 26 §4.6 registra o pior caso — **"com atrito e com o chefe concentrando e ganhando a
iniciativa, ele derruba os quatro em cinco rodadas"** — e a v0.205 decidiu que esse pior caso é
aceitável.*

**Rodando o mesmo pior caso com as `Intervenções` dentro:**

| cenário | o que acontece |
|---|---|
| **sem Intervenção** | o chefe cai na rodada `5`, com **`1` de `4` de pé** |
| **com `3` Intervenções, de graça** | **TPK na rodada `4`** — e o chefe sobra com `158` de vida |
| **com `3`, trocando por uma ação** | idêntico ao sem Intervenção: cai na rodada `5`, `1` de pé |

> ### As Intervenções de graça transformam o pior caso registrado — *"um sobrevivente"* — em **TPK**.
> *E não é TPK apertado: o chefe termina com `158` de vida ainda de pé.*

---

## 8.5 O que isso põe na mesa

| | |
|---|---|
| **pela barra que o Mizuki pôs** | ✅ **passa.** Não é TPK na rodada `1-2` em cenário nenhum |
| **pela métrica que o projeto já publicou e validou** | ❌ `3,60` contra alvo `2,70`, e `+0,80` acima do teto do campo |
| **pelo pior caso que a v0.205 já tinha aceitado** | ❌ vira TPK na rodada `4`, em vez de deixar um de pé na `5` |

> **As três leituras são verdadeiras ao mesmo tempo. A escolha é de qual barra vale.**

---

# 9 · ⚠ CORREÇÃO DE ENQUADRAMENTO — e ela é do Mizuki

***Ele, 10/09/2026:*** *"vc esta calculando as coisas dentro do nosso escopo como se ele fosse
imutável, podemos mexer nos inimigos já esperando esses valores... **Diminuir a banda de dano de todos
os inimigos, para que quando chegasse as opções de intervenções elas transformarem o combate em algo
mais letal mesmo**... tudo pode ser reajustado, **oq n podemos reajustar é a ideia**:*

> ### `1` — Inimigo tem ações.
> ### `2` — Intervenções são ações extras em meio aos turnos dos alvos. **Nenhum sistema come ação do turno para ter essas "intervenções", e é por um motivo.**

**As duas ficam FIXAS. E a `2` é factual:** *Draw Steel, Ação Lendária do D&D, `once per battle` do
13th Age, `End-of-Round Action` do Weird Wizard — **nenhum** consome a ação do turno.* **A saída `C`
do §5 morre por isso, e não por conta.**

## 9.1 E uma correção minha, sobre o peso do que eu disse

***Ele:*** *"mas esses registros é contanto q o inimigo pode falhar em testes? perder ações por
condições? errar ataques? players podem curar? ganhar agro?"*

**Ele está certo, e eu devo separar o que aguenta peso do que não aguenta:**

| o que eu disse | quanto peso ele aguenta |
|---|---|
| **`3,60` contra alvo `2,70` — `+33%`** | **aguenta.** O `2,70` saiu do MESMO modelo plano, e o d20 2014 e o PF2e — que validaram ele — **também são planos**. É comparação dentro de um modelo só |
| *"TPK na rodada `4`"* | **não aguenta o mesmo peso.** Aquilo empilha foco + iniciativa + atrito, e é exatamente onde cura, condição e agro mordem mais. **Eu dei peso demais àquela linha** |

---

# 10 · A RECALIBRAÇÃO — a Intervenção fica de graça, e a linha de dano desce

**Com a `Intervenção` extra e grátis, o total da luta vira `dano × rodadas + Intervenções × uma ação`.
Igualando ao total calibrado de hoje:**

> ### `fator` = `R ÷ (R + I/A)`

| categoria | tem Intervenção? | fator | dano novo | `o golpe` | fatia | na banda `20%`–`32%`? |
|---|---|---|---|---|---|---|
| `Ameaça` | **não** | `1,000` | `55,0` | `55,0` | `23%` | **sim** |
| **`Desastre`** | sim | **`0,750`** | **`164,2`** | `54,8` | `22%` | **sim** |
| **`Catástrofe`** | sim | **`0,882`** | **`289,4`** | `57,9` | `24%` | **sim** |
| **`Calamidade`** | sim | **`0,857`** | **`375,4`** | `62,6` | `26%` | **sim** |

## 10.1 ⚠ A `Ameaça` saía da banda — e o Draw Steel já resolvia isso

**Com Intervenções, a `Ameaça` dava fator `0,600` e `o golpe` em `14%`, contra um piso de `20%`.**
*Ela tem UMA ação, então uma Intervenção **dobra** a rodada dela.*

**E a frase do livro é literal:**

> *"Villain actions do not cost Encounter Value. They are **built-in abilities for leader and solo
> creatures**."*

> ### ⟹ Só os postos GRANDES têm. `Minion`, `Horde`, `Platoon` e `Elite` não têm.
> **Traduzido: `Intervenção` a partir do `Desastre`. `Capanga` e `Ameaça` não têm.**
>
> *O corte segue o campo, e não a conveniência da conta — e ele resolve a banda de quebra.*

## 10.2 A conferência: a métrica volta EXATAMENTE pro alvo

| categoria | total da luta | pessoas derrubadas | vs o alvo |
|---|---|---|---|
| `Ameaça` | `165` | `0,68` | **`1,00×`** |
| `Desastre` | `657` | **`2,70`** | **`1,00×`** |
| `Catástrofe` | `984` | `4,04` | **`1,00×`** |
| `Calamidade` | `1314` | `5,40` | **`1,00×`** |

> **Por construção o total volta ao de hoje — então a métrica de derrubadas volta ao número que a
> peça 26 §4.6 publica e que foi validado contra o d20 de 2014 e o PF2e.**

## 10.3 E o que isso COMPRA na mesa — que é o ponto da correção

| a rodada de um `Desastre` nv30 | hoje | recalibrado |
|---|---|---|
| **sem** Intervenção | `219` | **`164`** |
| **com** Intervenção | `219` | **`219`** |

> ### A rodada com Intervenção entrega `1,33×` a rodada sem. Hoje ela entrega `1,00×` — porque hoje não existe diferença nenhuma entre as duas.
>
> **Recalibrado, ele bate `25%` menos no básico, e a rodada da jogada devolve exatamente o número de
> hoje.** *O total não mudou. A **forma** mudou.*
>
> ***"elas transformarem o combate em algo mais letal mesmo"*** **é exatamente isso, e agora tem número.**

---

## 10.4 O que sobra decidir: o fator é um só, ou um por categoria?

**O fator não é uniforme — `0,750` · `0,882` · `0,857` — e o motivo é honesto:** *uma Intervenção pesa
`1/3` da rodada de um `Desastre` (`3` ações) e `1/6` da de uma `Calamidade` (`6` ações). **Quanto mais
ações a categoria tem, menos a Intervenção muda ela.***

**A alternativa é a Intervenção valer uma FRAÇÃO FIXA da rodada, igual pra toda categoria:**

| a Intervenção vale | fator | `Desastre`: dano | `o golpe` | fatia | na banda? |
|---|---|---|---|---|---|
| **`1/3` da rodada** | **`0,750`** | `164,2` | `54,8` | `22%` | **sim** |
| `1/4` da rodada | `0,800` | `175,2` | `58,4` | `24%` | **sim** |
| `1/2` da rodada | `0,667` | `146,0` | `48,7` | `20%` | **NÃO** — raspa o piso |

---

# 11 · ⚠⚠ FUI MEDIR NO DRAW STEEL, E A MEDIDA DERRUBA UMA SUPOSIÇÃO MINHA

***Pedido do Mizuki, 10/09/2026:*** *"Como outros sistemas fazem? principalmente drawn steel. **Sempre
q me perguntar algo que pode ser pesquisado e validado, pesquisa primeiro**, recomendo até salvar essa
informação nos documentos."*

**Medi `9` villain actions em `3` criaturas `Solo` do Draw Steel, contra a ação normal do mesmo bicho.
Tudo no `tier 2`, que é o resultado normal da rolagem.**

| criatura | nível | a ação normal | villain action `1` | `2` | `3` |
|---|---|---|---|---|---|
| **Thorn Dragon** | `2` | `Virulent Breath` **`9`** | `Briar Bindings` `9` — **`100%`** | `Thorned Armor` **`0`** | `Malign Thicket` **`0`** |
| **Ajax the Invincible** | `11` | `Blade of the Gol King` **`22`** | `Phoenix Wing King` `17` — **`77%`** | *tricks* **`0`** | *Awe of the Iron Crown* **`0`** |
| **Count Rhodar von Glauer** | `10` | `Spear of the Damned` **`18`** | `Red Tide` `13` — **`72%`** | `Sanguine Mist` `13` — `72%` | `Fires of Dracul` `16` — `89%` |

## Os três achados

| | |
|---|---|
| **1** | **NENHUMA villain action bate mais forte que uma ação normal do bicho.** O teto medido é **`100%`** |
| **2** | **`4` das `9` não causam dano nenhum.** Elas são controle, terreno, reposicionamento ou setup pro golpe seguinte |
| **3** | **Em `2` das `3` criaturas, são a `2` e a `3` que não causam dano.** *A `1` abre com dano; as outras duas **mudam o campo*** |

*Média `46%` · mediana `72%` · piso `0%` · teto `100%`.*

*Fonte: os statblocks oficiais no `SteelCompendium/data-md` — `Bestiary/Monsters/Monsters/Dragons/Statblocks/Thorn Dragon.md`, `.../Ajax the Invincible/...`, `.../Count Rhodar Von Glauer/...`*

---

## 11.1 E o que isso faz com a recalibração

| se a Intervenção valer | ações extras na luta | fator | dano novo | `o golpe` | fatia |
|---|---|---|---|---|---|
| **uma AÇÃO INTEIRA** — *o que eu supus* | `3,00` | `0,750` | `164` | `54,8` | `23%` |
| a **média medida** do Draw Steel (`46%`) | `1,37` | `0,868` | `190` | `63,4` | `26%` |
| **a FORMA do campo** — `1` com dano, `2` sem | **`0,75`** | **`0,923`** | **`202`** | `67,4` | `28%` |

> ### ⚠ O meu palpite era o cenário mais PESADO dos três — e o único que o campo não faz.
> **Eu ia propor cortar `25%` do dano de todo inimigo. A medida diz que o corte honesto é `8%`.**

## 11.2 E a pergunta que eu te fiz se responde sozinha

**Eu perguntei se a `Intervenção` vale *"uma ação dele"* ou *"uma fração fixa da rodada"*. A resposta
do campo não é nenhuma das duas — é uma FORMA:**

> ### A `Intervenção 1` bate, um pouco menos que uma ação normal.
> ### A `2` e a `3` **mudam o campo** em vez de causar dano.

**Isso resolve tudo de uma vez:**

| | |
|---|---|
| **o fator volta a ser quase `1`** | `0,923` — o dano de todo inimigo cai `8%`, e não `25%` |
| **a banda não é ameaçada** | `o golpe` fica em `28%`, dentro de `20%`–`32%` com folga |
| **e a dramaturgia melhora** | *"a 1ª é abertura, a 2ª é controle de área quando o grupo já cercou, a 3ª é o ultimate"* — o arco que a `a-intervencao.md` já tinha escrito **é o arco que o campo constrói**, e ele não depende de dano crescente |
| **e o `Domínio Encolhido` do Sukuna** | continua podendo causar dano: ele é a `Intervenção 1` dele, não a `3` |

---

# 12 · FECHADO — a forma do campo

***Decisão do Mizuki, 10/09/2026:*** *"vamos lá, perfeito — sabia q ia valer a pesquisa."*

> ### A `Intervenção 1` bate — um pouco menos que uma ação normal.
> ### A `2` e a `3` **mudam o campo** em vez de causar dano.
> ### E o fator de dano de quem tem `Intervenção` é **`0,923`**.

| o que fica | |
|---|---|
| a `Intervenção` é **extra e de graça** | as duas ideias fixas do Mizuki: *inimigo tem ações* · *nenhum sistema come ação do turno pra ter a ação fora do turno* |
| só de **`Desastre`** pra cima | *"built-in abilities for **leader and solo** creatures"* — Draw Steel |
| o dano de todo inimigo com Intervenção cai **`8%`** | e não `25%`, que era o que eu ia propor antes de medir |
| `o golpe` do `Desastre` vai pra **`28%`** da vida de um PC | dentro da banda `20%`–`32%`, com folga |
| a métrica de derrubadas volta pro alvo | `2,70`, validado contra d20 2014 e PF2e |
