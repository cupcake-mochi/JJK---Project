# Campo a campo — o que falta e o que sobra na ficha

*09/09/2026. Comparação do `RASCUNHO-2-o-bloco-em-branco.md` contra um bloco concreto de cada um dos quatro sistemas.*

> ⚠ **Aviso de método.** Os livros em texto que o prompt aponta (`scratchpad/livros/`) **NÃO EXISTEM** — o diretório foi apagado. Tudo abaixo veio de fonte externa, buscada agora, com URL. O SRD 5.2.1 veio de um espelho em Markdown do texto CC-BY (`oldmanumby/dnd.srd.5.2.1`), não do PDF oficial.

---

## Os quatro blocos concretos

| sistema | bloco usado | fonte |
|---|---|---|
| **Draw Steel** | **Thorn Dragon**, Level 2 Solo, EV 48 | `steelcompendium.io/compendium/main-linked/Bestiary/Monsters/Draw Steel Monsters - Unlinked/` — **437 a 442 blocos** varridos por contagem de campo |
| **Daggerheart** | **Volcanic Dragon: Ashen Tyrant**, Tier 4 Solo | `raw.githubusercontent.com/seansbox/daggerheart-srd/main/adversaries/Volcanic Dragon Ashen Tyrant.md` — **129 adversários** no JSON do mesmo repo |
| **PF2e** | **Ancient Red Dragon**, Creature 19 | `2e.aonprd.com/Monsters.aspx?ID=138`, via `elasticsearch.aonprd.com` |
| **D&D 2024** | **Ancient Red Dragon**, CR 24 | `raw.githubusercontent.com/oldmanumby/dnd.srd.5.2.1/main/11_Monsters/Monsters_A-Z/Monsters_A.md:1243` — **237 blocos** varridos |

### Draw Steel — Thorn Dragon, os campos na ordem impressa

Citação literal do cabeçalho, na ordem em que sai:

> `Thorn Dragon` / `Dragon, Elemental` / `Level 2` / `Solo` / `EV 48` / `3 Size` / `8 Speed` / `250 Stamina` / `6 Stability` / `5 Free Strike` / `Poison 5 Immunity` / `Fly Movement` / `— With Captain` / `— Weakness` / `+2 Might` / `+3 Agility` / `−1 Reason` / `+1 Intuition` / `+2 Presence`

Depois: `Solo Monster` (traço), `Withering Wyrmscale Aura` (traço), `Virulent Breath (Signature Ability)`, `Spinous Tail Swing`, `Provoking Nettles`, `Investiture of Verdure (5 Malice)`, `Prickly Situation`, `Thorny Scales (1 Malice)`, `Briar Bindings (Villain Action 1)`, `Thorned Armor (Villain Action 2)`, `Malign Thicket (Villain Action 3)`, e um bloco separado `Thorn Dragon Malice (Malice Features)`.

**Contagem de campo nos ~437 blocos** (`grep -cx` sobre o texto extraído): `Size` 442 · `Stamina` 441 · `Speed` 438 · `Stability` 438 · `Free Strike` 438 · `Weakness` 437 · `Movement` 437 · `With Captain` 437 · `Immunity` 435 · `Might`/`Agility`/`Reason`/`Intuition`/`Presence` 437 cada. **Zero campo de poço de recurso — confirma o levantamento.**

### Daggerheart — o template oficial do adversário

Citação literal do arquivo de template (`.build/04_md/templates/adversaries.md`):

> `# {{ .name }}` / `**_Tier {{ .tier }} {{ .type }}._** _{{ .description }}_` / `- **Motives & Tactics:** {{ .motives_and_tactics }}` / `- **Difficulty:** {{ .difficulty }} | **Thresholds:** {{ .thresholds }} | **HP:** {{ .hp }} | **Stress:** {{ .stress }}` / `- **ATK:** {{ .atk }} | **{{ .attack }}:** {{ .range }} | {{ .damage }}` / `- **Experience:** {{ .experience }}` / `### FEATURES`

**São nove campos e nada mais.** O bloco mais compacto dos quatro.

### PF2e — Ancient Red Dragon, a ordem de construção oficial

O PF2e publica a **ordem dos campos como checklist de construção** (Gamemastery Guide pg. 56, `2e.aonprd.com/Rules.aspx?ID=995`), citação literal:

> `Alignment, Size, and Traits (page 58) Ability Modifiers (page 59) Perception and Senses (page 60) Languages (page 60) Skills (page 60) Items, if necessary (page 61) AC (page 61) Saving Throws (page 62) Hit Points (page 62) Immunities, Weaknesses, and Resistances (page 63) Speed (page 64) Strikes, including their damage (page 64) Spells, if necessary (page 65)`

### D&D 2024 — Ancient Red Dragon, os campos na ordem impressa

`Gargantuan Dragon (Chromatic), Chaotic Evil` · `AC 22` · `Initiative +14 (24)` · `HP 507 (26d20 + 234)` · `Speed 40 ft., Climb 40 ft., Fly 80 ft.` · tabela de 6 atributos com colunas `MOD` e `SAVE` · `Skills` · `Immunities` · `Senses` · `Languages` · `CR 24 (XP 62,000, or 75,000 in lair; PB +7)` · `## Traits` · `## Actions` · `## Legendary Actions`.

**Contagem nos 237 blocos:** `HP` 237 · `AC` 237 · `Speed` 236 · `CR` 204 · `Senses` 186 · `Languages` 159 · `Skills` 156 · `Immunities` 140 · `Resistances` 55 · `Gear` 41 · `Vulnerabilities` 15.

---

# 1. O que existe em 3 ou 4 sistemas e NÃO existe na sua ficha

## FALTA-1 · **O golpe, com o dano — 4 de 4.** É o buraco maior.

| sistema | como imprime |
|---|---|
| D&D 2024 | `***Rend.*** *Melee Attack Roll:* +17, reach 15 ft. *Hit:* 19 (2d8 + 10) Slashing damage plus 10 (3d6) Fire damage.` |
| PF2e | `**Melee** jaws +37 (Fire, Magical, reach 20 feet), **Damage** 4d10+17 piercing plus 3d6 fire` |
| Daggerheart | `**ATK:** +10 | **Claws and Teeth:** Close | 4d12+15 phy` |
| Draw Steel | `5 Free Strike`, mais cada habilidade com as três faixas de dano (`≤11: 8 damage / 12-16: 12 / 17+: 15`) |

**Necessário aqui, e não tem outro caminho.** É o único número da `TABELA.md` que não tem célula no seu bloco. Detalhe: dos nove números da linha da tabela, **oito já têm célula** (vida, ações, Defesa, acerto, CD, refino, proteção, e Iniciativa via Destreza). Sobram dois: `o golpe` e `dano/rod`.

**E o número não é novo, é o que a tabela já tem.** Confere: `Desastre` nv 20 = `dano/rod 147` ÷ `ações 3` = `49`; e `4d12 + 23` dá média `26 + 23 = 49`. **Então `o golpe` = `dano/rod ÷ ações`, e `dano/rod` é derivável de volta.** A célula tem que ser `o golpe`; `dano/rod` fica na tabela de construção, porque é orçamento, não coisa que o mestre rola.

> **Linha de trabalho:** uma célula nova no bloco, com o rótulo do golpe e a expressão de dado. Nenhum número inventado — sai da coluna `o golpe` da `TABELA.md`.

## FALTA-2 · **Rótulo de frequência na habilidade — 4 de 4.** (É a resposta da pergunta 4, detalhada lá embaixo.)

## FALTA-3 · **Tipo de movimento, não só a distância — 3 de 4.**

Seu campo é `Deslocamento —`, e a `TABELA.md` fixa `9 m` como constante. **Um número só não diz "voa".**

| sistema | como resolve |
|---|---|
| Draw Steel | **DOIS campos separados**: `8 Speed` (número) e `Fly Movement` (tipo). `Movement` em **437 de 437** blocos |
| D&D 2024 | tudo numa linha: `Speed 40 ft., Climb 40 ft., Fly 80 ft.` — `Speed` em **236 de 237** |
| PF2e | `**Speed** 60 feet, fly 180 feet` |
| Daggerheart | **não tem** — usa faixas de alcance e o adversário move `Close` de graça |

**Necessário, e é barato: é lista de etiqueta, não número.** Metade de um bestiário de JJK é maldição que voa, escala parede ou atravessa chão. Se `9 m` é constante para todo mundo, então a única informação que a célula `Deslocamento` carrega é o TIPO — e hoje ela carrega o número que nunca muda e omite o tipo que sempre muda.

> **Linha de trabalho:** `Deslocamento 9 m` vira `Deslocamento 9 m · ‹ voo / escalada / escavação / — ›`. Zero número novo.

## FALTA-4 · **Fraqueza / vulnerabilidade — 3 de 4.**

Sua linha é `**Resistências** — · **Imunidades** — · **Perícias** —`. **Falta o eixo para baixo.**

| sistema | campo |
|---|---|
| Draw Steel | `Weakness`, em **437 de 437** blocos (vazio no Thorn Dragon, mas o campo está lá sempre) |
| PF2e | `**Weaknesses** cold 20` |
| D&D 2024 | `Vulnerabilities`, em **15 de 237** — o campo existe, é raro |
| Daggerheart | não tem campo; faz por passiva |

**Necessário, e a decisão §7 das `decisoes-fase-1` já pagou por ele sem perceber.** A régua que você fechou diz que imunidade a grupo inteiro **só com porta de saída declarada**. A porta de saída *é* uma fraqueza. Hoje ela mora na prosa do traço; um campo dá a ela um lugar fixo, e o mestre vê num relance como o grupo ganha.

> **Linha de trabalho:** a linha vira `Resistências — · Imunidades — · Fraquezas — · Perícias —`. Sem número novo: a mecânica pode ser a espelhada da resistência (dobra em vez de cortar pela metade) ou pode ficar como rótulo qualitativo por enquanto.

## FALTA-5 · **Idiomas — 3 de 4.** Draw Steel (`Crucible Dragon Languages` é seção própria), PF2e (`**Languages** Abyssal, Common, Draconic…`), D&D 2024 (**159 de 237**). Daggerheart não tem.

**Aqui o seu sistema resolve por outro caminho — e resolve melhor.** No JJK, "fala ou não fala" é justamente o que separa `maldição` de grau baixo de maldição inteligente, e você já tem `tipo` e `grau` no cabeçalho carregando isso na ficção. **Não abre campo.** Só cuide de que a prosa do bestiário diga, porque `maldição de grau 4 que fala` é informação de mesa.

## FALTA-6 · **Sentidos — 2 de 4.** PF2e (`**Perception** +35; darkvision, scent (imprecise) 60 feet, smoke vision`) e D&D 2024 (**186 de 237**). Draw Steel e Daggerheart não têm campo.

**Não passa a barra de 3 de 4, mas passa a barra da ficção.** Maldição que "sente energia amaldiçoada" e feiticeiro com Visão Panorâmica são coisas que o sistema precisa dizer. **Não abre campo: cabe em `Traços`,** que é onde o Draw Steel e o Daggerheart põem exatamente isso (`Withering Wyrmscale Aura`, `Keen Senses`).

## FALTA-7 · **Preço de encontro para grupo MISTURADO — 3 de 4.**

Draw Steel tem `EV 48`; D&D 2024 tem `XP 62,000`; Daggerheart tem pontos de batalha (SRD: *"Spend 2 points for each Horde, Ranged, Skulk, or Standard adversary"*, e *"+1 if you don't include any Bruisers, Hordes, Leaders, or Solos"*).

**Sua `categoria` resolve o caso de UM inimigo, e resolve melhor que os três** — `Desastre` já *diz* "quatro pessoas", em vez de mandar o mestre converter XP. **Mas ela não sabe somar.** `1 Desastre + 4 Capangas` não tem preço.

**Isso não é falta do BLOCO, é falta do capítulo de montar encontro.** Não abra campo no bloco. Fica na fila. *E o número já existe implícito: `Desastre` = 1,00, `Catástrofe` = 1,50, `Calamidade` = 2,00, `Capanga` = 0,25 — a coluna de fator de vida da escada JÁ é uma moeda somável.*

## FALTA-8 · **O `tamanho` carregando regra — 3 de 4.** (Isso é a pendência 2 do rascunho e o item 5 da fila. Agora tem precedente.)

| sistema | o tamanho é |
|---|---|
| Draw Steel | `3 Size` — **número**, e ele governa quantos quadrados a criatura ocupa e o alcance |
| PF2e | `Huge` — **trait**, governa espaço e alcance |
| D&D 2024 | `Gargantuan` na linha de itálico — governa espaço |
| Daggerheart | **não existe** — o sistema não tem tamanho |

**3 de 4 fazem o tamanho carregar regra; 1 de 4 não tem o campo.** *Nenhum dos quatro tem o campo como puro sabor.* Ou vira regra, ou sai. Fica avisado, como você decidiu — mas a decisão binária está bem posta: **imprimir um campo que não faz nada é o único caso, nos quatro sistemas, que não tem precedente.**

---

# 2. O que a ficha tem e nenhum outro tem — e se se paga

| campo dele | quem mais tem | se paga? |
|---|---|---|
| **`Iniciativa`** | só D&D 2024 (`Initiative +14 (24)`) — 1 de 4 | **NÃO.** A `decisoes-fase-1.md` §2 fecha: *"a Iniciativa do inimigo **é a Destreza dele**"*. Então a célula `Iniciativa` e a célula `Destreza` do mesmo bloco carregam o mesmo número, duas linhas de distância. No D&D isso não é duplicata (lá é Dex + bônus). **Aqui é.** Corta a célula e deixa a regra `d20 + Destreza` no capítulo — ou corta a Destreza da tabela de atributos, o que for mais útil |
| **`Reação 1 por rodada`** | 0 de 4 imprimem uma constante assim | **NÃO.** É constante para todo inimigo (`TABELA.md`, linha de constantes). Nenhum dos quatro imprime "1 reação por rodada" em 237, 437 ou 129 blocos. Vai para o capítulo de combate uma vez, sai de todos os blocos |
| **`CD` única no cabeçalho** | quase ninguém — PF2e imprime `spell DC 42`, D&D põe a CD dentro de cada ação | **SIM.** Ela faz pelo lado da resistência o que o `Acerto` faz pelo lado do ataque: um número cobre tudo. É o mesmo movimento de simplificação que o Daggerheart faz com `Difficulty` (um número para *toda* rolagem contra o adversário). Fica |
| **`Refino` *(proteção)*** | 0 de 4. O mais perto é a passiva do Daggerheart `Armored Carapace: reduce it by X` | **PAGA PELA METADE.** Se `Refino` é estatística que o jogador também tem, a simetria justifica. Mas **a `proteção` é derivada do `refino`** e a `TABELA.md` prova: 1→+1, 3→+2, 4→+2, 6→+3, 7→+3, 9→+4, 10→+4. Uma das duas células é lookup salvo, não informação. Se o bloco vai apertar (e vai, ver §6), essa é a primeira a virar `Refino 7 (+3)` numa célula só — que é o que já está escrito, mas ocupando uma linha inteira de tabela |
| **`Integridade`** | 1 de 4 — o `Stress` do Daggerheart é a única segunda trilha, e é mecânica diferente | **SIM, e barato.** É derivada (metade da vida, `decisoes-fase-1` §3), mas é uma divisão que o mestre faria no meio da luta. O Daggerheart imprime `Thresholds: 29/55` pela mesma razão |
| **`grau`** ("não entra em conta nenhuma") | 0 de 4 têm campo puramente decorativo | **SIM — como índice, não como regra.** Grau é o vocabulário canônico do JJK e o leitor procura por ele. Mas **é o único campo decorativo que o bloco pode bancar.** Se o `tamanho` também ficar sem regra, aí são dois, e o bloco começa a parecer preenchimento |
| **`Ações — N` como cabeçalho de seção** | 2 de 4 têm o equivalente, e **os dois imprimem como TRAÇO NOMEADO, não como seção** | **Se paga, mas está no lugar errado.** Daggerheart: `**Relentless (4) - Passive:** The Ashen Tyrant can be spotlighted up to four times per GM turn.` Draw Steel: `Solo Turns: The dragon can take two turns each round. They can't take turns consecutively.` **Nomear tem uma consequência mecânica: outra regra pode se referir ao nome.** Como cabeçalho de seção, `Ações — 6` não pode ser desligado, roubado, nem citado por um traço |
| **`corpos 8` do `Capanga`** | Draw Steel tem a regra idêntica, mas **não imprime a contagem no bloco** | **SIM, porque você fixou o 8 e o Draw Steel não fixa.** Confirmação independente da sua decisão de pool, citação literal: *"Each squad of minions shares a Stamina pool, with initial Stamina equal to each individual minion's Stamina multiplied by the number of minions in the squad. For example, a goblin spinecleaver has 5 Stamina, so a squad of eight spinecleavers has a Stamina pool of 40."* — **oito corpos, pool, e o corpo cai em um golpe.** É exatamente a sua forma A. Mas note: **o Draw Steel imprime só a vida de UM.** A sua `TABELA.md` imprime as duas (`vida de um 79` / `pool dos 8 632`) — no bloco, imprima as duas, porque o mestre precisa do pool para rastrear e do individual para saber quando um cai |

---

# 3. Os números morando fora do bloco — isso funciona num livro?

**Resposta curta: a `TABELA.md` funciona, e funciona bem — como ferramenta de CONSTRUÇÃO. Ela não funciona como o bloco publicado.**

**Os quatro sistemas TODOS têm a sua `TABELA.md`.** Isso não é coincidência, é o método:

> **PF2e, Gamemastery Guide pg. 56** (`2e.aonprd.com/Rules.aspx?ID=995`), literal: *"Creatures aren't built the same way PCs are. The rules for building them are more flexible, and their statistics are based on **benchmark final numbers** rather than combining each individual modifier together. This is called **top-down design**."*

**E o índice do Archives of Nethys prova que cada criatura publicada é NOTA CONTRA essa tabela.** O Ancient Red Dragon, direto do índice:

| campo | valor impresso | faixa da tabela |
|---|---|---|
| `ac` | **45** | `ac_scale: High` |
| `hp` | **425** | `hp_scale: Moderate` |
| `strike_damage_average` | **37** | `strike_damage_scale: High` |
| `fortitude_save` | **35** | `fortitude_save_scale: High` |
| `spell_dc` | **42** | `spell_dc_scale: High` |

**A tabela existe, é publicada, e a criatura é medida contra ela — e o bloco imprime `45`, `425`, `4d10+17`. A tabela nunca aparece na mesa.**

O mesmo nos outros três:

| sistema | onde mora a tabela | o que o bloco imprime |
|---|---|---|
| **Draw Steel** | equação publicada: `Monster Stamina … ((10 x Level) + Role Modifier) x Organization Modifier`, e a `Organization Modifier Table` (`Minion x 0.5`, `Solo x 6`, `Solo (Stamina only) x 5`) | `250 Stamina`, `5 Free Strike` |
| **D&D 2024** | tabela de estatística por ND, no Guia do Mestre | `AC 22`, `HP 507 (26d20 + 234)`, `Hit: 19 (2d8 + 10)` |
| **Daggerheart** | Homebrew Kit v1.0 (PDF separado, `daggerheart.com/wp-content/uploads/2025/07/`) | `Difficulty: 18 | Thresholds: 29/55 | HP: 8 | Stress: 5` |
| **PF2e** | Gamemastery Guide pg. 56-69 | `AC 45`, `HP 425`, `Damage 4d10+17` |

> **4 de 4 têm a tabela. 4 de 4 imprimem o resultado dela no bloco. 0 de 4 mandam o mestre consultar a tabela durante a luta.**

**O que isso quer dizer para você, em uma frase:** a `TABELA.md` é o gerador, o bloco é a saída. **O bestiário publicado é composto de blocos PREENCHIDOS.** O que o `RASCUNHO-2` é hoje — bloco com todas as células em `—` mais uma tabela apartada — é o *kit de construção*, e ele deve existir e ser publicado (os quatro publicam o deles). Mas ele não é a página do bestiário.

> **Linha de trabalho:** parar de tratar a `TABELA.md` como "onde os números moram" e passar a tratá-la como "a máquina que preenche". A única coluna dela que **não** deve ganhar célula é `dano/rod` — é orçamento. `o golpe` **precisa** de célula (FALTA-1).

---

# 4. Sem PE — falta linha para o leitor entender o que limita o inimigo?

**Sim, falta. E a seção `Intervenções` NÃO basta sozinha, por uma razão só: ela limita as três jogadas grandes e não diz nada sobre o resto do bloco.**

Hoje, num `Calamidade` nível 30, o leitor lê `Ações — 6` e uma lista de opções, e **nada na página diz que qualquer daquelas opções tem limite.** As 3 Intervenções estão trancadas. Os traços e a lista de ações estão soltos.

## O que os quatro fazem — e nenhum usa um campo de poço

**Todos os quatro põem o limite NA HABILIDADE, não num campo de recurso.** Números medidos agora:

| sistema | o rótulo | contagem |
|---|---|---|
| **D&D 2024**, 237 blocos | `Recharge 5-6` | **67** |
| | `Recharge 6` | **11** |
| | `Recharge 4-6` | **5** |
| | `(N/Day)` e variantes de covil | **57** |
| | `At Will` | **46** |
| | `Legendary Action Uses: N` | **30** |
| | **`spell slot`** | **ZERO** |
| **Draw Steel**, ~437 blocos | `N Malice` inline na habilidade | **663** |
| | `Villain Action 1/2/3` | **156** |
| **PF2e** | `It can't use Breath Weapon again for 1d4 rounds`, e `Draconic Momentum: The dragon recharges its Breath Weapon whenever it scores a critical hit with a Strike` | recarga por gatilho |
| **Daggerheart**, 129 adversários | `Mark a Stress` / `Spend a Fear` inline | **98 de 129 gastam Stress como custo** |

> **`spell slot` aparece ZERO vezes em 237 blocos do SRD 5.2.1.** Isso fecha a prova do levantamento com contagem própria.

## ⚠ Quem DISCORDA — e é discordância dura

**O Daggerheart dá ao inimigo um poço, e dá em 129 de 129 blocos.** O campo `Stress` está no template oficial e **nenhum adversário fica sem**. Faixa: `1` a `10`. Os 20 `Solo` do SRD: `[3,3,3,3,3,3,4,4,5,5,5,5,5,5,5,6,6,6,8,10]` — mediana `5`.

E o SRD é explícito de que é poço do INIMIGO, não do mestre, citação literal:

> *"each adversaries stress is tracked individually. If a feature requires the GM to spend Stress to activate it, the Stress must come from the adversary whose feature is being activate."*

O `Ashen Tyrant` (Tier 4 Solo) tem `Stress: 5` e três features que cobram dele: `Cornered - Passive: **Mark a Stress** instead of spending a Fear to spotlight the Ashen Tyrant.` e `Desperate Rampage - Action: **Mark a Stress** to make an attack against all targets within Close range.`

### Mas a discordância não derruba a sua decisão — ela corrige a FRASE do levantamento

**O `Stress` do adversário do Daggerheart não tem recuperação dentro da luta.** É `1` a `10`, gasta e acabou. **Isso não é o poço do jogador; é uma cota por luta com outro nome** — que é exatamente o que a sua `Intervenção` (3 por luta) já é.

> **A conclusão que sobrevive não é *"nenhum sistema dá poço ao inimigo"*. É *"nenhum sistema dá ao inimigo o poço DO JOGADOR"*.** A sua régua — *"recurso finito precisa de um DEPOIS"* — está certa e é isso que ela está pegando: o que os quatro rejeitam é o poço com recuperação, com escala por nível e com uma tabela de custos por magia. Cota por luta, todos os quatro têm. **Você também tem: chama de `Intervenção`.**

*E vale registrar o argumento público a favor da sua escolha, do outro lado:* o elogio recorrente ao Fear do Daggerheart é que ele substitui *"a lot of the bookkeeping required to run enemies in 5e, with a single pool of fear that all enemies share rather than tracking individual spell slots or ability uses"* (`drolleries.substack.com/p/how-to-use-fear-in-daggerheart-and`). **O consenso dos quatro é: se existe poço, ele é do MESTRE e é compartilhado, nunca por inimigo e por nível.**

## A linha que falta: vocabulário de frequência, não um campo

**Não é uma linha nova no cabeçalho. São três ou quatro rótulos que o bloco pode pendurar em qualquer Traço ou Ação.**

| rótulo | de onde sai o número |
|---|---|
| **(sem rótulo) = à vontade** | é o padrão. O D&D só imprime `At Will` para magia, porque para ataque o silêncio já significa isso. **Zero número** |
| **`1× por rodada`** | **já está no seu bloco duas vezes** — `Reação 1 por rodada` e `Intervenção máx. 1 por rodada`. Zero número novo |
| **`1× por luta`** | **já está no seu bloco** — é a própria `Intervenção` (`cada uma uma vez só`). Zero número novo |
| **`Recarga (5-6)`** | **este é o único que pede número, e o número não é invenção: dos 83 rótulos de recarga nos 237 blocos do SRD 5.2.1, `5-6` é 67, `6` é 11, `4-6` é 5.** `5-6` é o padrão publicado; `6` aperta, `4-6` afrouxa. Três valores, todos com precedente contado |

> **Linha de trabalho:** uma caixa de meia página no capítulo do bestiário definindo os quatro rótulos, e a permissão de escrevê-los depois do nome de qualquer Traço ou Ação. **Nenhum campo novo no cabeçalho. Nenhum número inventado.**

**E uma segunda linha, essa sim de forma:** transformar `### Ações — N` em traço nomeado, do jeito que os dois sistemas que têm a mecânica fazem (`Relentless (4)`, `Solo Turns`). Motivo mecânico, não estético: **um traço nomeado pode ser referenciado, desligado ou roubado por outra regra; um cabeçalho de seção não pode.** E numa mesa de JJK — onde a coisa que o jogador mais quer é tirar uma ação do chefe — isso vai ser pedido.

---

# 5. Os cinco TIPOS — algum campo deveria mudar conforme o tipo?

## Primeiro, o desalinhamento de eixo, porque ele é a raiz da pergunta

**O seu `tipo` e o seu `categoria` são eixos diferentes, e nos quatro sistemas eles têm nomes trocados:**

| você chama | Daggerheart chama | Draw Steel chama | D&D/PF2e chamam |
|---|---|---|---|
| **`categoria`** (`Capanga`…`Calamidade`) | **`type`** (`Solo`, `Horde`, `Minion`, `Leader`, `Bruiser`…) | **`Organization`** (`Minion`, `Horde`, `Platoon`, `Elite`, `Leader`, `Solo`) | (não existe) |
| **`tipo`** (`maldição`, `feiticeiro`…) | (não existe — vai na descrição) | **keywords** (`Dragon, Elemental`) | **creature type** (`Dragon (Chromatic)`) |

**A sua `categoria` JÁ muda campos, e está certa.** É o que a escada faz: vida, dano e ações mudam por categoria. Isso bate com 2 de 4 (Daggerheart e Draw Steel) e com precedente forte:

- **Daggerheart, o `Horde` muda como o campo `HP` se LÊ.** No JSON dos 129 adversários, o campo `type` de um horda é literalmente `"Horde (3/HP)"` — a razão vem no rótulo do tipo. E a passiva é: `**Horde (X) - Passive:** When the Horde has marked half or more of their HP, their standard attack deals X damage instead.`
- **Draw Steel, a `Organization` muda como a `Stamina` se LÊ.** `Minion x 0.5` no cálculo, e a regra do pool que você já reproduziu por conta própria.

> **Existe precedente para o rótulo do topo mudar a LEITURA de uma célula.** Isso libera o desenho, se você quiser usar.

## Agora a resposta: o `tipo` deve mudar UMA coisa, e só uma

**A única mudança por `tipo` que tem precedente em 2 de 4 e que não custa número novo é o pacote padrão de resistência/imunidade.**

É literalmente o que o creature type do D&D e do PF2e faz — e **a sua própria decisão §7 já pagou por isso**: *"resistência a 1 ou 2 tipos → **nada**, é sabor"* e *"imunidade a 1 ou 2 tipos → custa pouco. É o que quase todo chefe tem"*. E a sua própria mineração dos 354 blocos de 2014 mostra o padrão: `17 a 30` de ND → **92% têm imunidade, e quase sempre UM tipo**.

**Concreto:** `maldição` chega com o pacote que uma maldição deve ter; `restringido`, `civil` e `sem técnica` chegam sem nenhum. Zero número novo — a régua já diz que 1 a 2 tipos é grátis.

## E há uma segunda, que é decisão sua e eu não posso fechar: `Integridade`

`Integridade` é `metade da vida` para todos (§3), e o propósito declarado é *"alimentar os efeitos que se medem contra a Integridade máxima"*. **Os cinco tipos não são iguais nesse eixo** — um `restringido` (a Restrição Celestial: corpo trocado por energia amaldiçoada zero) e um `civil` não são o mesmo alvo que uma `maldição`, que É energia amaldiçoada.

**Não vou afirmar canon aqui.** O que eu trago é: **o precedente para uma célula ler diferente por rótulo de tipo existe** (o `Horde (3/HP)` do Daggerheart), e **se algum campo seu vai usar esse precedente, é a `Integridade`.** É pergunta de desenho, não conta.

## E o que NÃO deve mudar por tipo — isso eu afirmo

**`Defesa`, `Acerto`, `CD`, `Vida`, `Deslocamento`, `Ações`.** Todos saem de `categoria` × `nível`. **Deixar o `tipo` mexer neles põe dois donos no mesmo número — é o defeito exato que quebrou a `Dupla`** (`a-escada-com-numero.md`: *"a razão `pessoas ÷ (pessoas − 1)` explodia embaixo"*). Se um `feiticeiro` precisa de `+2` de Defesa, o `o-principio-da-causa.md` já resolve: **ele ganha o `+2` por uma causa escrita na ficção, não por ser feiticeiro.**

**E há uma terceira coisa que o tipo muda, que não é campo — é como o golpe se CHAMA.** A decisão do "Classe 0 do inimigo" (o golpe tabelado narrado como a técnica dele) só faz sentido para `feiticeiro` e `maldição`. Para `civil`, `sem técnica` e `restringido`, o mesmo `4d12 + 23` é um soco, uma faca ou uma arma amaldiçoada. **Isso é uma linha de prosa na definição do campo `o golpe` (FALTA-1), não um campo novo.**

---

# 6. Onde o bloco estoura a página primeiro

**Na ordem em que vai doer.**

## Primeiro: a tabela de atributos. É o desperdício mais denso, e é o mais barato de consertar.

Sua tabela gasta **6 linhas × 4 colunas = 24 células para carregar 9 números.** Os quatro comparados põem os atributos numa linha ou duas:

| sistema | forma |
|---|---|
| PF2e | **uma linha de 6**: `**Str** +9  **Dex** +5  **Con** +8  **Int** +5  **Wis** +6  **Cha** +7` |
| Draw Steel | **uma linha de 5**: `+2 Might  +3 Agility  −1 Reason  +1 Intuition  +2 Presence` |
| D&D 2024 | **grade 3 × 2**, com `MOD` e `SAVE` na mesma célula do atributo |
| Daggerheart | **não tem atributo nenhum** |

**A causa do seu problema é estrutural e vale nomear:** você tem **5 atributos e 4 resistências**, e não são 1 para 1. É esse desencaixe que força as duas colunas e as seis linhas. A forma do D&D 2024 (`atributo | MOD | SAVE`) resolve quando é 1:1 — no seu caso não é, então a saída é a forma do PF2e/Draw Steel: **uma linha corrida de 5 atributos, e as 4 resistências numa segunda linha corrida.** De 6 linhas para 2.

## Segundo: a lista de `Ações`. É onde o bloco realmente arrebenta.

O rascunho diz, com ênfase: *"**Isso não limita quantas estão escritas no bloco** — ele escolhe `N` da lista abaixo, toda rodada."* **Num `Calamidade` com `Ações — 6`, isso é um convite escrito para o autor listar 8 a 10 opções.** Somando as **3 Intervenções obrigatórias** e os traços, dá 12 ou mais entradas nomeadas.

**Doze é o teto absoluto do D&D, atingido por três monstros em 234.** Medido nos 234 blocos do SRD 5.2.1 (traços + ações + ações lendárias, entradas nomeadas):

| medida | valor |
|---|---|
| **mediana de entradas nomeadas** | **4** |
| média | 4,6 |
| máximo | **12** — e só o `Tarrasque` (12), o `Mummy Lord` (12) e o `Vampire` (11) chegam a dois dígitos |
| mediana de palavras por bloco | **249** |
| média de palavras | 278 |
| maior bloco | **762 palavras** (`Vampire`) |

E no Daggerheart, medido nos 129:

| medida | valor |
|---|---|
| média de features, todos os tipos | **3,2** |
| média de features, só os 20 `Solo` | **5,4** |
| máximo em todo o SRD | **7** |
| maior bloco | `Volcanic Dragon: Molten Scourge`, 2356 caracteres ≈ 350 palavras |

> **Isso dá número para a pendência 4 do rascunho e o item 4 da fila (`o teto de traços`), e o número não é invenção — é a mediana e o teto publicados.**
>
> **Proposta com origem declarada:** teto de **6 entradas nomeadas** para um bloco normal e **8** para o chefe de fim de arco. Origem: mediana `4` do D&D 2024 (234 blocos), média `5,4` dos `Solo` do Daggerheart (20 blocos), teto `7` do Daggerheart. **E das suas 6, três já estão gastas** — as Intervenções são obrigatórias. **Sobram 3 para `Traços` + `Ações` num bloco normal, 5 no chefe.**

**Essa contagem também bate de frente com o texto do rascunho.** Se o teto de entradas é 6 e 3 são Intervenções, então `Ações — 6` **não pode** vir com uma lista de 8. A frase *"isso não limita quantas estão escritas"* é verdadeira em regra e falsa em página. **Precisa da segunda metade: "não limita, mas o bloco só tem espaço para N".**

## Terceiro: a mobília fixa, antes de você escrever uma palavra de conteúdo

Contando o que o `RASCUNHO-2` gasta com o bloco todo vazio: 1 linha de nome + 1 de cabeçalho em itálico + 5 linhas de tabela de estatística + 7 linhas de tabela de atributo + 1 linha de resistências + 4 cabeçalhos de seção + 3 linhas de Intervenção = **cerca de 22 linhas e 90 a 110 palavras de mobília com zero conteúdo.**

A mediana do D&D 2024 é **249 palavras para o bloco INTEIRO**. **Você já gastou 40% dela na moldura.** Cada célula constante que sai (`Reação 1 por rodada`, a `Iniciativa` duplicada, uma das duas metades de `Refino (proteção)`) é orçamento devolvido para traço.

## Quarto, e mais tarde: as Intervenções obrigatoriamente três.

3 Intervenções × 1 linha de nome + 1 a 3 linhas de efeito = **6 a 12 linhas fixas por bloco**, e um `Capanga` também paga isso. **O D&D não paga:** `Legendary Actions` aparece em 30 dos 237 blocos. O Draw Steel não paga: `Villain Action` aparece 156 vezes em ~437 blocos.

**Aqui a `a-intervencao.md` decidiu o contrário, por escolha declarada e boa** (*"a ação fora de tudo, quase todo mundo vai ter"*). Fica registrado o custo de página que essa escolha compra: **um `Capanga` de nível 2 vai ter um bloco quase tão comprido quanto um `Desastre`.** Se em algum momento a página apertar, a Intervenção nos degraus de baixo é a primeira coisa que os quatro sistemas cortariam.

---

# Resumo das linhas de trabalho

| # | o que fazer | número novo? |
|---|---|---|
| 1 | **célula `o golpe`** no bloco | não — coluna `o golpe` da `TABELA.md` |
| 2 | **`Deslocamento`** ganha o tipo de movimento | não — lista de etiqueta |
| 3 | **`Fraquezas`** entra na linha de resistências | não — a "porta de saída" da §7 já existe |
| 4 | **quatro rótulos de frequência** (`à vontade` · `1×/rodada` · `1×/luta` · `Recarga (5-6)`) | só `5-6`, e vem de 67 de 83 rótulos do SRD 5.2.1 |
| 5 | **`Ações — N` vira traço nomeado** | não |
| 6 | **cortar `Reação 1 por rodada`** de todos os blocos | não |
| 7 | **cortar a `Iniciativa` duplicada** (ou a `Destreza`) | não |
| 8 | **tabela de atributo de 6 linhas para 2** | não |
| 9 | **teto de 6 entradas nomeadas** (8 no chefe), 3 já gastas nas Intervenções | mediana `4` do D&D 2024 e média `5,4` do Daggerheart Solo |
| 10 | **`tipo` carrega só o pacote padrão de imunidade** | não — a §7 diz que 1 a 2 tipos é grátis |
| 11 | **`tamanho`: vira regra ou sai** | decisão, não conta — 0 de 4 imprimem campo sem regra |
| 12 | **preço de encontro misturado** (fila, não é do bloco) | a coluna de fator de vida já é moeda somável |
| 13 | **corrigir a frase do levantamento**: não é "nenhum sistema dá poço", é "nenhum dá o poço DO JOGADOR" | — |

---

## Anexo — arquivos de trabalho

Os textos extraídos ficaram em `/tmp/claude-1000/-media-mizuki-HD-Externo-II-Claude-Bestiario/56c72db1-7acc-4db0-bba3-77aa84a51702/scratchpad/`: `ds.txt` (Draw Steel, 1,18 MB), `srdmon.md` (237 blocos do SRD 5.2.1), `dhadv.json` (129 adversários do Daggerheart), `pf2.json` (Ancient Red Dragon do AoN), `dh1.md` (SRD do Daggerheart). **São temporários — se a sessão morrer, morrem com ela.**
