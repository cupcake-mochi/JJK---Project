# A abertura do catálogo `04` — o que já estava em casa

*10/09/2026. **Antes de pesquisar fora, conferir o repositório.** Deu certo pela quarta vez.*

> ### Conta rodada: `04-fase-1/fila/medir-os-lugares.py`
> **Quatro contas, nenhum número digitado à mão.** *Cada âncora sai do documento dono e o script morre
> se o dono mudar.* **Rodar de novo é conferir o estado.**

---

# ⚡ `1` · O CAMPO DÁ FICHA PRO LUGAR — e o Draw Steel dá inteira

**`35` fichas de terreno, em `6` famílias**, dentro da base que já estava em disco
*(`fila/dados-recarga-area/`, a mesma do `Capanga` e da área)*:

| família | quantas |
|---|---|
| `Environmental Hazards` | `7` |
| `Fieldworks` | `7` |
| `Mechanisms` | `8` |
| `Siege Engines` | `7` |
| `Power Fixtures` | `3` |
| `Supernatural Objects` | `3` |

## E as três colunas que interessam batem em `100%`

| | quantas das `35` |
|---|---|
| tem **vida** *(`Stamina`)* | ### **`35` de `35`** |
| **custa encontro** *(`EV`)* | ### **`35` de `35`** — *min `1` · mediana `3` · max `24`* |
| ### traz **como DESLIGAR** *(`Deactivate`)* | ### **`35` de `35`** |
| tem gatilho *(`Activate`)* | `22` de `35` — `62,9%` |
| cresce por preço *(`Upgrade`)* | `11` de `35` — `31,4%` |

> ## ⟹ Toda ficha de LUGAR do Draw Steel traz escrito como se livrar dela sem bater.
> **É o modelo `Volo's` em forma de statblock:** *o lugar tem uma saída que não é dano, e ela é
> obrigatória na ficha — não é enfeite de um ou outro.*
>
> *A `Lava` se apaga quadrado por quadrado. O `Black Obelisk` se desliga com um teste de `Reason`,
> e falhar no teste **liga** ele.* **Desligar é cena, e a cena tem risco.**

---

# ⚡ `2` · O D&D LIGA BICHO A LUGAR — mas por LISTA, não por ficha

**`322` de `325` blocos do SRD 2014 declaram ambiente.** *Mediana de `2` a `3` ambientes por bicho.*

| ambiente | blocos |
|---|---|
| `Forest or Jungle` | `151` |
| `Hills` | `113` |
| `Desert` | `110` |
| `Mountain` · `Grassland` | `105` cada |
| **`Urban`** | **`93`** |
| `Underworld` · **`Ruins`** | `83` cada |
| `Swamp` · `Caves` | `79` · `75` |
| **`Sewer`** · **`Temple`** · **`Tomb`** | `43` · `33` · `32` |

> ### ⟹ São DOIS desenhos diferentes, e os dois servem ao `04`:
> **o D&D diz "onde este bicho aparece"** *(rótulo no bloco do bicho)* · **o Draw Steel diz "o que
> este lugar FAZ"** *(bloco próprio, com preço)*.
>
> ⚠ *E o nosso Bestiário não tem nem um nem outro — a peça 26 monta o bicho e não fala de onde ele
> mora.* **Isso é observação, não pendência: o `04` é catálogo, e catálogo não cria regra.**

---

# ⚠⚠ `0b` · CANÁRIO — o `environments` do SRD 2024 vem VAZIO, e é COLETA

**A chave `environments` está declarada nos `331` blocos do SRD 2024 e vem preenchida em `0`.**
*No SRD 2014 vem preenchida em `322` de `325`.*

> ### Isto NÃO é "o D&D 2024 apagou o ambiente". É o mesmo furo da `Vulnerabilities Fire` da Múmia.
> **Toda contagem de ambiente em `D&D 2024` neste projeto é PISO, não valor.**
> *Canário instalado no `medir-os-lugares.py` §0b, na mesma família do §0b do
> `medir-resistencia-imunidade.py`.*
>
> ⚠ **Foi exatamente por aqui que ele me corrigiu em 10/09.** *Um `0` que sai de coleta parece achado
> e não é.* **A segunda vez não vai virar publicação.**

---

# ⚠ `3` · O NOME DA COISA — e o `04` precisa saber disso ANTES de escrever

*Grep nos donos, no repositório de leitura.*

| onde | o que tem |
|---|---|
| **peça 11** | a **APTIDÃO**: `Barreira Simples` `19×` e `Cortina` `15×` — *com regra, preço, gate e relógio de um minuto* |
| **peça 12** | a frase *"**o sistema não tem Véu**"* — *e ela nega uma coisa específica* |
| **peça 13** | a palavra `véu` `15×`, na lista *"enganado por barreira, véu e ferramenta"* |
| **catálogo `01`** | a palavra `véu` `7×`, e o §4 **se chama "O véu"** |

## As três convivem, e não é contradição — são três coisas

| | |
|---|---|
| a **`Cortina`** | é **mecânica com dono**: peça 11, §6.6 |
| o **`véu`** da peça 13 | é **palavra de ficção**, numa lista de coisas que enganam pela energia |
| o **`Véu` que a peça 12 nega** | é o **véu-masquerade** — o *"vazou / não vazou"* do mundo. *A peça 12 tirou um gancho de XP contrafactual por isso* |

> ### ⟹ REGRA DE ESCRITA PRO `04`, e ela sai de graça:
> **quando o `04` apontar `REGRA`, ele escreve `Cortina` e aponta pra peça 11.**
> *`véu` pode ficar como palavra do texto — nunca como mecânica com dono.*
>
> ⚠ **E isso é uma conferida no `01` §4**, que hoje intitula a seção *"O véu"*. *Não está errado —
> está marcado `PADRÃO` e descreve a Cortina da obra.* **Mas ele não aponta pra peça 11, e devia.**

---

# ⚡⚡ `4` · QUEM ERGUE A CORTINA — e a resposta muda a cena de abertura do serviço

*A peça 11 §6.6 tem a `Cortina` com regra fechada, e ninguém tinha cruzado ela com o catálogo.*

> ### A `Cortina` cobre **"um prédio, uma escola, um quarteirão"** — texto literal da peça 11.
> **A palavra `escola` já está lá.** *O `04` não precisa inventar o exemplo: ele já é o exemplo do
> documento dono.*

## Mas ela é aptidão CARA, e o gate está publicado

| rota | a `Barreira Simples` abre | a **`Cortina`** abre |
|---|---|---|
| sempre Refino | nv`6` | **nv`10`** |
| meio a meio | nv`10` | ### **nv`22`** |
| sempre Corpo · sempre Leque | nunca | ### **nunca** |

> ## ⟹ "O véu sobe" NÃO é coisa que o grupo faz. Na maior parte da campanha, quem ergue é o apoio.
> **Duas das rotas nunca levantam Cortina, em nível nenhum.** *E a rota do meio só chega no nv`22`.*
>
> ⚠ **E isso não é defeito — é a obra.** *A própria peça 11 escreve o porquê:* **"cortina exige um
> nível de habilidade que muitos feiticeiros poderosos não têm, e as condições delas chegam a ser
> encomendadas a quem sabe fazer."**

### O que isso dá pro `04`, e é `FERRAMENTA` boa

**Se o grupo não ergue o véu, alguém ergueu por eles — e essa pessoa é NPC com nome, agenda e
horário.** *O `01` §4 já oferecia "um custo de entrada: quem ergue não luta". Agora dá pra dizer
quem é.*

⚠ **E abre uma pergunta de mesa que não tem resposta publicada:** *o que acontece se o véu cair
no meio do serviço porque quem ergueu foi embora, ou morreu?* **A peça 11 só diz que ela cai
quando o dono fica `Inconsciente`.**

> ### ⚠ Correção pequena a fazer no `01` §4:
> **ele escreve o véu como abertura padrão do serviço e não diz que o grupo quase nunca é quem
> ergue.** *Não está errado — está incompleto, e a incompletude engana.*

---

# ⚡⚡⚡ `5` · O QUARTO EXPERIMENTO NATURAL — o D&D 2024 PASSOU a cobrar o covil

*Rodado depois da pesquisa. **O agente `B` leu num site de terceiro que o `MM 2024` mexeu no covil.**
Isso era achado LIDO — o SRD está em disco, e a metade que dá pra medir foi medida.*

| | com `Legendary Resistance` | ganham uso **EXTRA em covil** |
|---|---|---|
| **SRD 2014** | `23` de `325` | ### **`0`** |
| **SRD 2024** | `32` de `331` | ### **`27`** |

**O extra é sempre exatamente `+1` uso** — *`3/dia` vira `4/dia`, `4/dia` vira `5/dia`. Sem exceção
nas `27`.*

> ## ⟹ O campo ADICIONOU preço de covil entre uma edição e a seguinte.
> **E pôs o preço DENTRO do bloco do bicho, como um uso a mais — em vez de dar ficha ao lugar.**

## ⚠⚠ E aqui está a coisa mais interessante da rodada: os dois desenhos são de 2024–25 e vão pra lados opostos

| | quem tem ficha | onde mora o preço |
|---|---|---|
| **Draw Steel** *(`Dynamic Terrain`)* | ### **o LUGAR** | `EV` próprio, moeda do monstro |
| **D&D 2024** *(`in Lair`)* | ### **o MORADOR** | `+1` `Legendary Resistance`, dentro do bloco dele |

> ### **Os dois concordam que estar na casa dele é mais caro. Discordam de quem carrega a conta.**
> *Isso não é empate — é uma escolha de arquitetura, e ela tem consequência direta pro `04`.*

> ### ⚠ O que este § NÃO prova
> **Não prova que a `Lair Action` foi removida no `MM 2024`.** *Os dois jsons não têm campo de ação
> de covil nenhum — **nem vazio, não existe**.* **A remoção continua sendo achado LIDO**, e está
> marcada assim no `PESQUISA-04b` §5.

---

## O que esta medição NÃO responde

| | |
|---|---|
| **o que faz um lugar produzir maldição** | *é o miolo do `04`, e é pergunta de OBRA — não tem em casa* |
| escola e hospital, os dois exemplos dele | *idem* |
| se o `Volo's` dá seção de lugar, e como | *é pergunta de campo/comunidade* |

> **⟹ É daqui que sai a decisão sobre agente de pesquisa.** *As três de cima não têm resposta em
> disco; as quatro medidas acima já têm.*
