# Prova p4 — PF2e e Draw Steel, verificação de fonte primária

*09/09/2026. Alvo: `PRECO-pe-do-inimigo.md` §1, §4-B, §5. Tudo abaixo foi aberto na web nesta rodada.*

**Veredito: PARCIAL.** Os seis números da razão PF2e estão **todos exatos**. Toda a regra do Draw
Steel está **confirmada literalmente**, e o contraexemplo procurado **não existe** — a varredura
achou o contrário dele, escrito como regra. **Mas o §4-B leu a tabela errada:** a coluna `2,0×` é de
dano de **ÁREA**, e o PF2e tem uma regra separada, muito mais barata, para o golpe limitado de **alvo
único**. Isso muda o número que o relatório usou para rejeitar o modelo B.

---

## Fontes abertas

| fonte | como foi lida |
|---|---|
| PF2e GM Core, cap. 2 *Building Creatures* | https://2e.aonprd.com/Rules.aspx?ID=2874 — texto cru salvo em `/tmp/claude-1000/-media-mizuki-HD-Externo-II-Claude-Bestiario/56c72db1-7acc-4db0-bba3-77aa84a51702/scratchpad/pf2e-building.txt` (60.170 caracteres) |
| Draw Steel: Monsters, livro inteiro | https://steelcompendium.io/compendium/main-linked/Bestiary/Monsters/Draw%20Steel%20Monsters%20-%20Unlinked/ — mesmo texto via `github.com/SteelCompendium/data-bestiary-md`, arquivo `Monsters/Draw Steel Monsters - Unlinked.md`, 30.725 linhas / 1,57 MB, clonado em `…/scratchpad/ds/` |

> O `WebFetch` do steelcompendium.io devolve só a navegação (foi o que travou o levantamento
> original, nota 3 da Frente 4). O repositório `data-bestiary-md` é o **mesmo corpo de texto** que
> aquela URL serve, e é grep-ável. Por isso as citações do Draw Steel abaixo vêm com número de linha.

---

# PARTE 1 — PATHFINDER 2e

## 1.1 A tabela existe, e os seis números do relatório estão CORRETOS

`Table 2–12: Area Damage`, colunas `Unlimited Use` e `Limited Use`
(`pf2e-building.txt:585-586` — cabeçalho literal: `Level	Unlimited Use	Limited Use`).

Tabela inteira, como publicada (valor médio entre parênteses no original):

| nv | Unlimited | Limited | razão | nv | Unlimited | Limited | razão |
|---|---|---|---|---|---|---|---|
| −1 | 1d4 (`2`) | 1d6 (`4`) | `2,000` | 12 | 5d8 (`23`) | 13d6 (`46`) | `2,000` |
| 0 | 1d6 (`4`) | 1d10 (`6`) | `1,500` | 13 | 7d6 (`24`) | 14d6 (`49`) | `2,042` |
| **1** | 2d4 (`5`) | 2d6 (`7`) | **`1,400`** | 14 | 4d12 (`26`) | 15d6 (`53`) | `2,038` |
| 2 | 2d6 (`7`) | 3d6 (`11`) | `1,571` | **15** | 6d8 (`27`) | 16d6 (`56`) | **`2,074`** |
| 3 | 2d8 (`9`) | 4d6 (`14`) | `1,556` | 16 | 8d6 (`28`) | 17d6 (`60`) | `2,143` |
| 4 | 3d6 (`11`) | 5d6 (`18`) | `1,636` | 17 | 8d6 (`29`) | 18d6 (`63`) | `2,172` |
| **5** | 2d10 (`12`) | 6d6 (`21`) | **`1,750`** | 18 | 9d6 (`30`) | 19d6 (`67`) | `2,233` |
| 6 | 4d6 (`14`) | 7d6 (`25`) | `1,786` | 19 | 7d8 (`32`) | 20d6 (`70`) | `2,188` |
| 7 | 4d6 (`15`) | 8d6 (`28`) | `1,867` | **20** | 6d10 (`33`) | 21d6 (`74`) | **`2,242`** |
| 8 | 5d6 (`17`) | 9d6 (`32`) | `1,882` | 21 | 10d6 (`35`) | 22d6 (`77`) | `2,200` |
| 9 | 5d6 (`18`) | 10d6 (`35`) | `1,944` | 22 | 8d8 (`36`) | 23d6 (`81`) | `2,250` |
| **10** | 6d6 (`20`) | 11d6 (`39`) | **`1,950`** | 23 | 11d6 (`38`) | 24d6 (`84`) | `2,211` |
| 11 | 6d6 (`21`) | 12d6 (`42`) | `2,000` | **24** | 11d6 (`39`) | 25d6 (`88`) | **`2,256`** |

**Conferência dos seis números que o relatório publica:**

| nv | relatório | conta real | bate? |
|---|---|---|---|
| 1 | `1,40×` | `7 ÷ 5` = `1,400` | **SIM** |
| 5 | `1,75×` | `21 ÷ 12` = `1,750` | **SIM** |
| 10 | `1,95×` | `39 ÷ 20` = `1,950` | **SIM** |
| 15 | `2,07×` | `56 ÷ 27` = `2,074` | **SIM** |
| 20 | `2,24×` | `74 ÷ 33` = `2,242` | **SIM** |
| 24 | `2,26×` | `88 ÷ 39` = `2,256` | **SIM** |

**Seis de seis, exatos até a segunda casa. CONFIRMADO.**

## 1.2 Mas uma frase do §4-B está errada: ela NÃO estabiliza em 2,0×

O relatório escreve: *"É o dobro, e estabiliza em `2,0×` a partir do nível 11."*

A razão **cruza** `2,0` no nível 11 e **continua subindo** até `2,26`:

- média nv 11–24 = **`2,146`**, mínimo `2,000`, máximo `2,256`
- média nv 17–24 = **`2,219`**

**A própria tabela do relatório se contradiz** — ela mostra `2,24` no nv 20 e `2,26` no nv 24, que
não são `2,0`. **Correção: cruza `2,0×` no nível 11 e estabiliza perto de `2,2×` da metade da tabela
para cima.** É diferença pequena em valor, mas o relatório usa `2,0×` como o número de trabalho, e o
número de trabalho real é maior.

## 1.3 ⚠ O ACHADO QUE MUDA O §4-B: essa razão é de dano de ÁREA, não de golpe

O relatório aplica `2,0×` a **um golpe de alvo único** (`73 → 146`, "`60%` da vida de um personagem")
e rejeita o modelo B por causa disso. **O PF2e nunca manda fazer essa conta.** O texto que introduz a
tabela separa os dois casos, e manda usar tabelas diferentes. Literal, `pf2e-building.txt:583`:

> *"If a special action is a single action with only one target, you can often set damage using the
> Strike Damage table. If it uses more than 1 action or requires setup in some way, it might deal
> higher damage than is typical; often, you can just use the extreme column in these cases."*
>
> *"For abilities that deal damage in an area, use the Area Damage table. These numbers are based on
> a 2-action activity (e.g., most damaging spells). Single actions should deal much less damage. […]
> The table includes values for unlimited-use abilities (ones that can be used at will) and
> limited-use ones (which can be used once or, like dragon breath abilities, once or twice but not on
> consecutive turns)."*

E a regra do alvo único aparece de novo, explícita, na seção da tabela de golpe
(`pf2e-building.txt:457`):

> *"You can also use the extreme value for special attacks that the creature can use only a limited
> number of times or under circumstances that aren't likely to happen every round."*

**Ou seja: no PF2e, o preço do golpe limitado de alvo único é "sobe uma coluna para `Extreme`", não
"multiplica por 2".** `Table 2–10: Strike Damage` (`pf2e-building.txt:463`) tem quatro colunas —
`Extreme`, `High`, `Moderate`, `Low` — e **nenhuma divisão ilimitado/limitado**.

O prêmio real, medido na tabela:

| nv | Extreme | High | Moderate | ext ÷ high | ext ÷ mod |
|---|---|---|---|---|---|
| 1 | `8` | `6` | `5` | `1,333` | `1,600` |
| 5 | `20` | `16` | `13` | `1,250` | `1,538` |
| 10 | `33` | `26` | `22` | `1,269` | `1,500` |
| 15 | `45` | `36` | `30` | `1,250` | `1,500` |
| 20 | `58` | `44` | `37` | `1,318` | `1,568` |
| 24 | `68` | `52` | `44` | `1,308` | `1,545` |
| | | | **média** | **`1,288`** | **`1,542`** |

### O que isso faz com o número que matou o modelo B

`Desastre` nv 30, golpe `73`, vida de personagem `245`:

| régua | dano | fatia da vida |
|---|---|---|
| relatório, `2,00×` (tabela de **ÁREA**) | `146,0` | `59,6%` |
| PF2e alvo único, `1,288×` (`extreme ÷ high`) | **`94,0`** | **`38,4%`** |
| PF2e alvo único, `1,542×` (`extreme ÷ moderate`) | `112,6` | `45,9%` |

> **O relatório rejeita o modelo B com um número que o PF2e reserva para habilidade de área.** Na
> régua que o PF2e realmente usa para alvo único, o golpe limitado dá `94` = `38,4%` da vida —
> **abaixo dos `45%` que o Mizuki já rejeitou na mesa.** A rejeição do modelo B sobrevive contra a
> `Dupla`, mas ela foi feita contra a tabela errada, e a versão certa passa.

**E note para onde isso empurra:** a coluna `Limited Use` do PF2e só existe na tabela de **área**.
Quer dizer que **a resposta do PF2e para "habilidade limitada" já é largura**, exatamente a conclusão
do §6 do relatório (*"a camada paga não é maior contra um alvo. Ela é mais larga"*). **O §6 está
certo por um caminho que o §4-B não percebeu que tinha andado.**

## 1.4 Espaços de magia de criatura — texto literal, CONFIRMADO

A frase-chave (`pf2e-building.txt:500`), completa:

> *"When choosing spells, some won't be very useful if cast at an extremely low rank compared to the
> creature's level. **Most notably, damaging spells drop off in usefulness for a creature that's
> expected to last only a single fight.** A damaging spell 2 ranks below the highest rank a creature
> of that level can cast is still potentially useful, but beyond that, don't bother. Spells that have
> the incapacitation trait should be in the highest spell slot if you want the creature to
> potentially get their full effect against PCs."*

E o quanto de espaço existe, contra o quanto se preenche (`pf2e-building.txt:537-538`):

> *"For a creature that can cast as many spells as a PC spellcaster, the highest spell rank the
> creature can cast is half its level rounded up. It gets five cantrips. If the creature's level is
> odd, it gets two spell slots of the highest spell rank (plus three spell slots of each lower rank),
> or three spell slots of that rank (plus four spell slots of each lower level). If its level is
> even, it gets three spell slots of the highest spell rank (plus three spell slots of each lower
> rank), or four spell slots of that rank (plus four spell slots of each lower rank)."*
>
> *"**Because creatures tend to be "on stage" for only a short time, you usually don't need to fill
> every spell slot.** You can often fill just the top three ranks of spells, pick cantrips, and slot
> in a few thematic backup spells in the fourth rank down. For a recurring foe, you might give it a
> full complement of spells."*

**Nuance contra o §1 do relatório:** ele diz que *"o livro **manda não** preencher"*. O livro diz
*"you usually don't need to fill"* — **não precisa**, não *não pode* — e abre exceção para inimigo
recorrente (*"For a recurring foe, you might give it a full complement"*). A tese fica de pé; o verbo
está mais forte que a fonte. **Correção de redação, não de conteúdo.**

## 1.5 Pontos de Foco de criatura — texto literal, CONFIRMADO

`pf2e-building.txt:552`, parágrafo inteiro:

> *"Some creatures have focus spells, especially when those focus spells clearly fit a creature's
> theme. **Simply give the creature the focus spells you like and between 1 and 3 Focus Points** (you
> can also allow your creature to cast focus spells using spell slots). Use the same DC and spell
> attack modifier as any other spell. **A creature that has just 1 Focus Point is likely to cast a
> focus spell only once, unless it's a recurring enemy.** If the creature has plenty of spells
> already, you might want to skip focus spells altogether, as they aren't as strong as top-rank spell
> slots."*

`1 a 3` confirmado, e a admissão de que com `1` ponto a criatura conjura uma vez só também. **O §5 do
relatório está certo nesta linha.**

---

# PARTE 2 — DRAW STEEL

## 2.1 A fórmula do Malice — CONFIRMADA, literal

`Draw Steel Monsters - Unlinked.md:322` e `:337`:

> *"Just as every hero has a Heroic Resource determined by their class, so too do the heroes' foes
> need their own juice to fuel their strongest threats. **Malice is a resource gained and used by the
> Director.** You use Malice to let enemies in the game activate their most powerful abilities and
> throw surprises at the heroes during combat."*

> *"**At the start of combat, you gain Malice equal to the average number of Victories per hero. Then
> at the start of each combat round, you gain Malice equal to the number of heroes in the battle,
> plus the combat round number.** For instance, if five heroes with three Victories each are just
> starting their first combat round, you begin that combat with 9 Malice—3 for the average number of
> Victories, 5 for the number of heroes, and 1 for the first round of combat. At the start of the
> next round, provided all the heroes are still alive, you gain 7 Malice—5 for the number of heroes
> plus 2 for the second round. As long as none of the heroes is taken out of the fight, you gain 8
> Malice in the third round, 9 Malice in the fourth round, and so on."*

Conferência do exemplo do próprio livro (H=5, V=3): `3+5+1 = 9` ✓ · rodada 2 `+7` ✓ · rodada 3 `+8` ✓
· rodada 4 `+9` ✓. **A fórmula fecha com o exemplo.**

Conferência da conta que o relatório usa no §4-D (H=4, V=0):

| rodada | ganha | acumulado |
|---|---|---|
| 1 | `4+1` = `5` | `5` |
| 2 | `4+2` = `6` | **`11`** |
| 3 | `4+3` = `7` | **`18`** |
| 4 | `4+4` = `8` | `26` |
| 5 | `4+5` = `9` | `35` |

**`5 / 11 / 18` — exatamente o que o relatório publica. CONFIRMADO.**

E o custo das três features do quadro (`:372`, literal):

> *"**You often need to prepare only three Malice features for any given encounter, or four if you're
> running an encounter making use of multiple monster types or bands** (for example, orcs and
> goblins). Just pick a feature costing 2 to 3 Malice, a feature costing 5 Malice, and a feature
> costing 7 to 10 Malice and you should be covered."*

`2+5+7` = `14` · `3+5+10` = **`18`**. **O acumulado de 3 rodadas com 4 heróis é `18` = o teto exato
do custo das três features. A coincidência que o §5 alega é real.**

> ⚠ **Nuance contra o §5:** o livro diz *"only three […] **or four** if you're running an encounter
> making use of multiple monster types or bands"*. A convergência no `TRÊS` é verdadeira, mas o livro
> abre `quatro` para encontro misto. **Não derruba nada — o `Capanga` + `Desastre` do Projeto-M é
> justamente um encontro misto.** Vale saber que o campo prevê `4` nesse caso.

### E uma correção conceitual no §1: Malice É poço, alimentado por renda

O §1 classifica o Draw Steel como *"renda por rodada, não poço"*. O livro é explícito nas duas
pontas (`:339` e `:349`):

> *"If a hero dies, they stop generating Malice for you. **At the end of an encounter, any unused
> Malice is lost.**"*

> *"You won't be able to spend Malice on every single option a given encounter has to offer. It's
> totally up to you how you deploy Malice. You can spend it on smaller but still impactful features
> each combat round. **You can save it up and use it on a small number of extremely dramatic
> abilities.** You can spend it on the same feature that uses all available Malice each combat round
> and then forget about it until the next round."*

**Malice acumula e pode ser guardada — é um poço POR ENCONTRO, alimentado por renda crescente, que
evapora no fim.** A dicotomia "renda ou poço" do §1 não é do livro. Isso **importa para o modelo D**:
se o Mizuki portar só a renda e não a acumulação, ele perde a decisão que o Draw Steel considera o
miolo do recurso (guardar duas rodadas para comprar a coisa grande).

E existe vazão além do saldo (`:357`): *"**At the start of any monster's turn**, you can spend Malice
to activate **one** of the following features"* — uma Basic Malice por turno de monstro. As duas
básicas, literais (`:360`, `:365`):

> *"**Brutal Effectiveness (3 Malice)** — The monster digs into the enemy's weak spot. The next
> ability the monster uses with a potency has that potency increased by 1."*

> *"**Malicious Strike (5+ Malice)** — The monster pours all their animosity into their attack. Their
> next strike deals extra damage to one target equal to the monster's highest characteristic score.
> The extra damage increases by 1 for each additional Malice spent on this feature (to a maximum of
> three times the monster's highest characteristic). **This feature can't be used two rounds in a
> row, even by different monsters.**"*

## 2.2 Villain Actions: três, uma vez cada, uma por rodada — CONFIRMADO, literal

`Draw Steel Monsters - Unlinked.md:208-214`:

> *"#### Villain Actions"*
>
> *"The solo and leader creatures presented in this book are designed to be fought in climactic
> battles at the end of an adventure or campaign. Because of this, they have special abilities called
> villain actions."*
>
> *"**A creature with villain actions always has three. Each villain action can be used only once per
> encounter, and no more than one villain action can be used per round.** (This holds even if you
> have two or more creatures with villain actions in an encounter, though such an occurrence should
> be rare.)"*
>
> *"**A creature can use a villain action at the end of any other creature's turn during combat.**
> Villain actions are numbered and intended to be used in a specific order that creates a logical
> encounter flow and cinematic arc, but you can use them in any order you choose."*

**Cada palavra da `Intervenção` do Mizuki está aqui**, inclusive a parte de acontecer *depois do turno
de outra criatura*. E dois detalhes que ele ainda não tem escritos:

1. **O limite de `1 por rodada` é GLOBAL, não por criatura.** *"This holds even if you have two or
   more creatures with villain actions in an encounter."* — se o Projeto-M puser dois `Desastres` na
   mesma luta, o campo diz que o teto de uma Intervenção por rodada continua sendo **um só, na
   mesa**.
2. **Villain action só existe em `solo` e `leader`.** `:737` — *"Leader creatures have villain
   actions […] Creatures with the support role function much like leaders, but **they lack villain
   actions** and are less complex."* O `Capanga` e a `Ameaça` do Projeto-M, pelo molde declarado,
   **não deveriam ter Intervenção.**

O arco dos três (`:216-220`), que é o mesmo `1-2-3` do relatório:

> *"The first villain action is an **opener** […] They're a taste of what's to come."*
> *"The second villain action provides **crowd control** […] it's even more powerful than an opener."*
> *"The third and final villain action is an **ultimate move or "ult"**—a showstopper that the villain
> can use to deal a devastating blow to the heroes before the end of the battle."*

E o aviso contra o nova, que reforça o §6 do relatório (`:1266`):

> *"It might be tempting to keep a flying monster far out of reach of the heroes, or **popping that
> third villain action at the start of combat**, or causing rocks to fall from the sky every turn.
> But the less the heroes can do about any specific situation, the less involved your players will
> feel in the game."*

## 2.3 "Villain Actions não custam Malice" — CONFIRMADO, mas por medição, não por frase

**O livro nunca escreve a frase "villain actions cost no Malice".** O levantamento original tratou
isso como citação literal; **não é.** Então eu medi o livro inteiro.

**Medição 1 — nenhuma das 156 villain actions tem custo.** Extraí todos os títulos com
`(Villain Action N)` do livro: **156 títulos**. Nenhum contém `Malice`.

**Medição 2 — o controle prova que o formato de custo existe e é onipresente.** No mesmo livro,
**471 títulos de habilidade carregam custo explícito em Malice**, no formato `(N Malice)`:

| custo | ocorrências |
|---|---|
| `1 Malice` | `51` |
| `2 Malice` | `82` |
| `3 Malice` | `145` |
| `4 Malice` | `11` |
| `5 Malice` | `114` |
| `6 Malice` | `1` |
| `7 Malice` | `47` |
| `10 Malice` | `12` |
| **total** | **`463`** (+ variantes `N+`) |

> **O formato de preço existe, é usado 463 vezes, e as 156 villain actions são silêncio sistemático
> nele. Custo zero, medido.**

**Medição 3 — e há a frase quase-explícita.** Duas villain actions precisam dizer que **isentam** o
custo das habilidades que disparam, o que só faz sentido se a villain action em si for grátis
(`:4069`, quimera, Villain Action 3):

> *"**Effect:** The chimera uses Roar, then shifts up to their speed and can make a free strike
> against each enemy who comes adjacent to them during the shift. When the chimera ends this shift,
> they use Dragon's Eruption. **The use of these abilities as part of this villain action costs no
> Malice.**"*

Mesma construção em `:4060` (*"uses Dragon's Eruption and Roar **without spending Malice**"*),
`:3080`, `:16226`, `:19870`.

**Veredito: CONFIRMADO por medição + citação adjacente. Mas a tese deve ser escrita como "nenhuma das
156 villain actions do livro tem custo", e não como uma frase de regra que não existe.**

Contagem estrutural, de bônus — **sempre exatamente três, nunca quatro:**

| | ocorrências |
|---|---|
| `Villain Action 1)` | **`52`** |
| `Villain Action 2)` | **`52`** |
| `Villain Action 3)` | **`52`** |
| `Villain Action 4)` | **`0`** |

**52 criaturas, 52-52-52-0. O "always has three" não é só regra: é como o bestiário inteiro está
construído.**

## 2.4 O CONTRAEXEMPLO NÃO EXISTE — e a varredura achou o oposto dele

A tarefa pedia: alguma criatura cujo recurso seja um **poço próprio dela**? **Não. Zero.**

**Varredura 1 — todos os campos de statblock do bestiário.** Extraí por script o conjunto completo de
rótulos de campo dos **437 statblocks** do livro. A lista inteira é:

> `Stamina` · `Speed` · `Size` · `Stability` · `Free Strike` · `Immunity` / `Immunities` ·
> `Weakness` · `Movement` · `With Captain` · e as cinco características `Might` · `Agility` ·
> `Reason` · `Intuition` · `Presence`

**Nenhum campo de recurso, energia, mana, ponto ou poço. Em nenhum dos 437.**

O statblock mais pesado do livro, para deixar concreto — Ajax the Invincible, nível 11, `Solo`,
`EV 156`, `700` de Stamina (`:1601-1605`):

```
|   Human, Humanoid   |      -       |    Level 11     |      Solo       |      EV 156       |
|   **1L** Size       | **7** Speed  | **700** Stamina | **2** Stability | **11** Free Strike|
| **-** Immunities    | **Fly, hover** Movement |  -   | **-** With Captain | **-** Weakness |
|   **+5** Might      | **+4** Agility | **+5** Reason | **+5** Intuition | **+4** Presence  |
```

**Linha de recurso: não tem.** E a ação extra dele é comprada pelo **Diretor** (`:1582`):

> *"**Solo Action (5 Malice)** — Ajax takes an additional main action on his turn. He can use this
> feature even if he is dazed."*

Detalhe de desenho que vale para o Projeto-M: quando o chefe precisa pagar algo **do bolso dele**, o
Draw Steel cobra em **vida**, não em recurso (`:1610`):

> *"**End Effect:** At the end of each of his turns, Ajax can take 20 damage to end up to two effects
> on him that can be ended by a saving throw. This damage can't be reduced in any way."*

**Varredura 2 — vocabulário de poço.** Procurei `token`, `charge`, `stack`, `pool`, `reservoir`,
`essence`, `points`, `spend a`. Os únicos candidatos, todos descartados:

| candidato | linha | por que NÃO é contraexemplo |
|---|---|---|
| `rage points` | `26299` | é debuff **imposto ao herói**: *"their abilities can inflict rage points on **any enemy**"*. O monstro não gasta nada. |
| `Deathcount` | `7534` | contador **no alvo**, não no dragão |
| `Stamina pool` | `377` | é **vida compartilhada de esquadrão de minions**, não energia |
| `spend a Recovery` | `29870` etc. | `Recoveries` são de **herói e retainer** (aliado com nível). Nenhum inimigo tem campo de Recoveries |

**Varredura 3 — e aqui está o oposto do contraexemplo, escrito como regra.** Quando uma habilidade
geraria recurso pessoal, o Draw Steel **converte para Malice do Diretor**. Literal, `:28629`
(hierofante, ação livre `Solar Accretion`):

> *"**Effect:** **If the hierophant is a hero, they gain 3 of their Heroic Resource. If the hierophant
> is a Director-controlled creature, the Director gains 3 Malice.**"*

Mesmo desenho em `:5731` (Aurumvas): *"each time that hero gains any amount of their Heroic Resource,
**the Director gains 1 Malice**."*

> **O Draw Steel encontrou exatamente o caso que geraria um poço próprio de inimigo, e escreveu uma
> regra de câmbio para NÃO deixar isso acontecer.** A mesma criatura, como herói, tem recurso
> pessoal; como inimigo, o recurso vira Malice do Diretor. **É a tese central do relatório escrita
> pela fonte primária, e é mais forte do que o relatório alega.**

---

## Placar final

| afirmação do relatório | veredito |
|---|---|
| PF2e tem duas colunas `Unlimited Use` / `Limited Use` lado a lado | **CONFIRMADO** (`Table 2–12: Area Damage`) |
| as seis razões `1,40 / 1,75 / 1,95 / 2,07 / 2,24 / 2,26` | **CONFIRMADO, 6 de 6 exatos** |
| *"estabiliza em `2,0×` a partir do nível 11"* | **REFUTADO** — cruza `2,0` no nv 11 e sobe até `2,256`; média nv 11–24 = `2,146` |
| aplicar `2,0×` a **golpe de alvo único** (`73 → 146`, `60%` da vida) | **REFUTADO** — `2,0×` é régua de **ÁREA**. Alvo único no PF2e = coluna `Extreme` = `1,288×` (`ext÷high`) → `94` = `38,4%` da vida |
| *"damaging spells drop off in usefulness…"* | **CONFIRMADO, literal** (`:500`) |
| *"o livro manda NÃO preencher"* espaço de magia | **PARCIAL** — o livro diz *"you usually don't need to fill"*, e abre exceção para inimigo recorrente |
| Pontos de Foco de criatura = `1 a 3` | **CONFIRMADO, literal** (`:552`) |
| fórmula do Malice (herói + nº da rodada; Vitórias no início) | **CONFIRMADO, literal**, e fecha com o exemplo do livro |
| Malice de 3 rodadas com 4 heróis = `18` = custo das 3 features | **CONFIRMADO** (`5/11/18`; `3+5+10 = 18`) |
| *"Malice é renda por rodada, **não poço**"* | **PARCIAL** — é poço **por encontro** alimentado por renda: *"You can save it up"*, e sobra evapora no fim |
| Villain Actions: sempre `3`, `1×` cada, máx `1` por rodada | **CONFIRMADO, literal** (`:212`) + medido (`52/52/52/0`) |
| Villain Actions **não custam Malice** | **CONFIRMADO por medição** (0 de 156, contra 463 títulos que sim têm custo) — **mas a frase literal não existe no livro** |
| existe criatura com poço próprio? (contraexemplo) | **NÃO EXISTE.** 437 statblocks, zero campo de recurso. E `:28629` escreve o câmbio que impede o caso |

## O que muda no relatório

1. **§4-B tem que trocar a régua.** A razão `2,0×` é de área. Para o golpe limitado de alvo único o
   PF2e cobra `~1,29×` sobre `high` (ou `~1,54×` sobre `moderate`). No `Desastre` nv 30 isso é `94`
   de dano = `38,4%` da vida, **não** `146` = `60%`. **O modelo B não morre pelo motivo que o
   relatório dá.** Se ele for rejeitado, precisa de outro argumento.
2. **§4-B, corrigir a frase da estabilização:** cruza `2,0×` no nv 11, estabiliza perto de `2,2×`.
3. **§1, corrigir duas classificações:** o PF2e *"não precisa"* preencher (não *"manda não"*); a
   Malice *é* poço por encontro alimentado por renda (não *"renda, não poço"*) — e essa segunda
   correção **muda o modelo D**, porque a acumulação é a decisão que o Draw Steel considera o miolo.
4. **§5 ganha um degrau.** A convergência no `TRÊS` está confirmada em fonte primária e o bestiário
   inteiro obedece (`52/52/52/0`). Acrescentar que o livro admite `quatro` em encontro misto — que é
   o caso `Capanga` + `Desastre`.
5. **§6 ganha uma prova que ele não sabia que tinha.** A conclusão *"a camada paga é mais larga, não
   maior"* é a leitura correta do PF2e: a coluna `Limited Use` **só existe na tabela de área**.
6. **Dois detalhes novos para a `Intervenção`:** o teto de `1 por rodada` é **da mesa**, não da
   criatura; e no molde declarado, villain action existe só em `solo`/`leader` — o `Capanga` e a
   `Ameaça` não teriam.
7. **A tese central passa mais forte do que estava escrita.** Não é só que ninguém dá poço ao
   inimigo: o Draw Steel escreveu uma **regra de câmbio** para converter recurso pessoal em Malice do
   Diretor quando a criatura muda de lado.
