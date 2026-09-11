# Sobrecarga — precedente publicado: PF2e, 13th Age, LANCER/ICON

**Data:** 09/09/2026
**Pergunta:** quanto custa, em sistema publicado, negar meia ação / uma ação / a Reação do inimigo — e existe precedente de atacar recurso gastável de inimigo?

---

## 1. Pathfinder 2e (o mais importante)

### 1.1 A economia: 3 ações + 1 reação, e a reação é separada

> "At the start of each turn you take in an encounter, you regain 3 actions and 1 reaction to spend that round."
> — https://2e.aonprd.com/Rules.aspx?ID=2335 (Actions)

> "You gain 1 reaction per round. You can use a reaction on anyone's turn (including your own), but only when its trigger occurs."
> "If you don't use your reaction, you lose it at the start of your next turn, though you typically then gain a reaction at the start of that turn."
> "The GM determines whether you can use reactions before your first turn begins, depending on the situation in which the encounter happens. Once your first turn begins, you gain your actions and reaction."
> — https://2e.aonprd.com/Rules.aspx?ID=2432 (Reactions in Encounters)

> "Regain your 3 actions and 1 reaction. If you haven't spent your reaction from your last turn, you lose it—you can't 'save' actions or reactions from one turn to use during the next turn."
> — https://2e.aonprd.com/Rules.aspx?ID=2428 (Step 1: Start Your Turn)

### 1.2 **ACHADO CENTRAL: ação e reação são orçamentos separados**

> "Certain abilities, instead of or in addition to changing the number of actions you can use, say specifically that you can't use reactions."
> "The most restrictive form of reducing actions is when an effect states that you can't act: this means you can't use any actions, or even speak. When you can't act, you still regain your actions unless another effect (like the stunned condition) prevents it."
> — https://2e.aonprd.com/Rules.aspx?ID=393 (Gaining and Losing Actions)

Ou seja: `Slowed` **não encosta na reação**. Tirar reação exige cláusula explícita. São duas compras diferentes, não uma escala contínua.

### 1.3 Condições (texto literal)

| Condição | Texto literal | URL |
|---|---|---|
| `Slowed` | "You have fewer actions. Slowed always includes a value. When you regain your actions, reduce the number of actions regained by your slowed value. Because you regain actions at the start of your turn, you don't immediately lose actions if you become slowed during your turn." (Player Core pg. 446) | https://2e.aonprd.com/Conditions.aspx?ID=92 |
| `Stunned` | "You've become senseless. You can't act. Stunned usually includes a value, which indicates how many total actions you lose, possibly over multiple turns, from being stunned." + "Stunned overrides slowed. If the duration of your stunned condition ends while you are slowed, you count the actions lost to the stunned condition toward those lost to being slowed." | https://2e.aonprd.com/Conditions.aspx?ID=93 |
| `Quickened` | "You're able to act more quickly. You gain 1 additional action at the start of your turn each round. Many effects that make you quickened require you use this extra action only in certain ways." | https://2e.aonprd.com/Conditions.aspx?ID=89 |
| `Off-Guard` (ex-`Flat-Footed`) | "You're distracted or otherwise unable to focus your full attention on defense. You take a –2 circumstance penalty to AC." | https://2e.aonprd.com/Conditions.aspx?ID=58 |
| `Confused` ← **a condição que nega reação** | "You don't have your wits about you, and you attack wildly. You are off-guard, you don't treat anyone as your ally (though they might still treat you as theirs), and **you can't Delay, Ready, or use reactions**." | https://2e.aonprd.com/Conditions.aspx?ID=63 |
| `Paralyzed` | "You're frozen in place. You have the off-guard condition and can't act except to Recall Knowledge and use actions that require only your mind." | https://2e.aonprd.com/Conditions.aspx?ID=85 |
| `Unconscious` | "You're sleeping or have been knocked out. You can't act. You take a –4 status penalty to AC, Perception, and Reflex saves, and you have the blinded and off-guard conditions." | https://2e.aonprd.com/Conditions.aspx?ID=95 |
| `Prone` | "You're lying on the ground. You are off-guard and take a −2 circumstance penalty to attack rolls. The only move actions you can use while you're prone are Crawl and Stand." | https://2e.aonprd.com/Conditions.aspx?ID=88 |

**Quem nega reação no PF2e:** só `Confused` (cláusula explícita) e as condições de "can't act" (`Stunned`, `Paralyzed`, `Unconscious`, `Petrified`). `Slowed`, `Off-Guard`, `Clumsy`, `Frightened` — **nenhuma** toca a reação.

### 1.4 A pergunta-chave: qual o feitiço de nível mais BAIXO que aplica `Slowed 1`?

Busquei no índice completo de feitiços da AoN (endpoint Elasticsearch oficial do site: `https://elasticsearch.aonprd.com/aon/_search?q=slowed AND type:Spell AND level:[1 TO 2]`). Resposta em três camadas:

1. **Rank 2 é o mais baixo para `Slowed 1` direto, confiável, em alvo único:** `Laughing Fit` (rank 2, Player Core pg. 340) e o legacy `Hideous Laughter` (rank 2). Também rank 2: `Palm-Held Sun` e `Imp Sting` (slowed 1 por 1 rodada), `Blood Runs Cold`.
2. **Focus spells rank 1 já entregam `Slowed 1`** — mas em grau de sucesso ruim do alvo: `Dead Weight` (/Spells.aspx?ID=2896) "**Failure** The target is slowed 1 and off-guard. **Critical Failure** slowed 2 and off-guard"; `Mushroom Patch` (/Spells.aspx?ID=2442) crit fail "dazzled and slowed 1 for 1 round"; `Call of the Grave` (/Spells.aspx?ID=522) crit success "sickened 2 and slowed 1 as long as it's sickened"; `Scramble Body` (/Spells.aspx?ID=1904) idem.
3. **Rank 1 "de verdade" existe, mas com atraso:** `Goblin Pox` (rank 1, https://2e.aonprd.com/Spells.aspx?ID=1545) — a afflição só dá "Stage 2 sickened 1 and slowed 1 (1 round)". Slowed chega tarde, não na hora.

E o teto: `Slow` (rank 3, https://2e.aonprd.com/Spells.aspx?ID=1677) — "**Success** The target is slowed 1 for 1 round. **Failure** The target is slowed 1 for 1 minute. **Critical Failure** The target is slowed 2 for 1 minute."

→ **Uma ação negada por 1 rodada = rank 2. Uma ação negada pela luta inteira (1 minuto) = rank 3.**

### 1.5 **A prova de preço mais limpa que existe: `Laughing Fit`**

O mesmo feitiço vende reação e ação em graus de sucesso diferentes:

> **Critical Success** "The target is unaffected."
> **Success** "The target is plagued with uncontrollable laughter. **It can't use reactions.**"
> **Failure** "The target is **slowed 1 and can't use reactions**."
> **Critical Failure** "The target falls prone and **can't use actions or reactions for 1 round**. It then takes the effects of a failure."
> — https://2e.aonprd.com/Spells.aspx?ID=1583 (Laughing Fit, rank 2, Player Core pg. 340)

Leitura: **negar a reação é o prêmio de consolação** — um grau de sucesso ABAIXO de negar uma ação. Na mesma linha de preço, reação < ação.

### 1.6 O lado barato e o lado caro, pra calibrar tier

| Efeito | Custo | Texto |
|---|---|---|
| `Off-Guard` (−2 CA) | 1 ação, teste de perícia, à vontade, sem recurso | `Feint`: "Single Action. Attempt a Deception check. Success: The target is flat-footed against the next melee attack you attempt." https://2e.aonprd.com/Actions.aspx?ID=48 — ou **de graça** por flanqueamento |
| Tirar 1 ação **na prática** (ele gasta 1 pra Stand) | 1 ação, teste de perícia, à vontade | `Trip`: "Single Action. You try to knock a creature to the ground. Attempt an Athletics check against the target's Reflex DC. Success: The target falls and lands prone." https://2e.aonprd.com/Actions.aspx?ID=2382 |
| Idem (ele gasta 1 pra Escape) | 1 ação | `Grapple`: "Single Action. Attempt an Athletics check against the target's Fortitude DC. Success: Your target is grabbed until the end of your next turn." https://2e.aonprd.com/Actions.aspx?ID=35 |
| `Stunned 1` (1 ação sumida, sem jeito de encurtar) | **Talento de classe nível 2** + 2 Strikes de Flurry + save de Fort + trait Incapacitation | `Stunning Fist`/`Stunning Blows`: "...If either Strike hits and deals damage, the target must succeed at a Fortitude save against your class DC or be stunned 1 (or stunned 3 on a critical failure). This is an incapacitation effect." https://2e.aonprd.com/Feats.aspx?ID=442 |
| **+1 ação** (espelho do preço) | rank 3 | `Haste`: "It gains the quickened condition and can use the extra action each round for only Strike and Stride actions." https://2e.aonprd.com/Spells.aspx?ID=1553 |

**Imposto obrigatório sobre negação de ação:**

> "An ability with this trait can take a character completely out of the fight or even kill them, and it's harder to use on a more powerful character. If a spell has the incapacitation trait, any creature of more than twice the spell's level treats the result of their check to prevent being incapacitated by the spell as one degree of success better, or the result of any check the spellcaster made to incapacitate them as one degree of success worse."
> — https://2e.aonprd.com/Traits.aspx?ID=631 (Incapacitation)

Nota: `Slow` e `Laughing Fit` **não** têm Incapacitation (são "fewer actions", não "out of the fight"); `Stunning Fist` tem. O PF2e separa "tira 1 ação" de "tira o turno" com esse trait.

### 1.7 O que impede a reação de um MONSTRO

Não existe regra separada. Monstro roda a mesma economia:

> "Reactive Abilities: Free actions or reactions that are usually triggered when it's not the creature's turn are listed here."
> — https://2e.aonprd.com/Rules.aspx?ID=786 (Reading Creature Statistics)

Então o monstro perde a reação por: (a) já ter usado 1 nessa rodada; (b) decisão do GM antes do primeiro turno dele na cena (Rules 2432); (c) condição com cláusula explícita (`Confused`) ou de "can't act" (`Stunned`, `Paralyzed`, `Unconscious`). **`Slowed` não tira a reação do monstro.**

### 1.8 Recurso do monstro — existe, mas ninguém ataca

Monstro PF2e **tem** poço gastável:

> "Spontaneous spells list the number of spell slots after the spell rank."
> "If the creature has a focus spells, this entry lists the spells' rank, the Focus Points in the creature's focus pool, the DC, and those spells."
> — https://2e.aonprd.com/Rules.aspx?ID=786

**Mas não achei nenhum efeito de PC que drene slot, Focus Point ou carga de monstro.** O único ataque a recurso publicado é `Counterspell` (https://2e.aonprd.com/Feats.aspx?ID=4994) — e é troca 1:1: o PC gasta um slot igual pra queimar o do inimigo. Procurei em: índice de feitiços da AoN via Elasticsearch, lista de traits, Rules 786 (stat block), Rules 2228 (Focus Spells), busca web por "drain spell slots pathfinder 2e". **`NÃO EXISTE` (dentro do que varri): imposto de recurso sobre inimigo no PF2e.** Para efeito do seu sistema: o PF2e tem o recurso no monstro e mesmo assim **escolheu não deixar o jogador mexer nele** — taxa de ação é o único vetor.

---

## 2. 13th Age (1e / Archmage Engine SRD)

Fonte: SRD oficial licenciado — https://www.13thagesrd.com/combat-rules/ (tudo desta seção vem dessa URL, salvo indicação). PDF oficial Pelgrane: https://pelgranepress.com/files/13th_Age/13th_Age_System_Reference_Document.pdf

### 2.1 Economia de ação (vale igual pra monstro)

> "Each turn you can take one of each action, in any order." (standard, move, quick)
> "You can take any number of free actions on your turn, as allowed by the GM."
> **Interrupt action (= a "reação" do 13A):** "You can use one interrupt action when it's not your turn. You can't use another one until the end of your next turn."

Detalhe de preço embutido: a interrupt do 13A **recarrega mais devagar que a do PF2e** (só no fim do seu próximo turno). Gastar/negar ela vale mais aqui.

### 2.2 Condições (texto literal, mesma URL)

| Condição | Texto literal |
|---|---|
| `Dazed` | "You take a –4 penalty to attacks." |
| `Hampered` | "You can only make basic attacks. You can still move normally." |
| `Stunned` | "You suffer a –4 penalty to defenses and can't take any actions." |
| `Weakened` | "You take a –4 penalty to attacks and to defenses." |
| `Vulnerable` | "Attacks against you have their crit range expanded by 2 (normally 18+)." |
| `Stuck` | "You can't move, disengage, pop free, change your position, or let anyone else move you without teleporting." |
| `Helpless` | "While helpless, you take a –4 penalty to all defenses and you can be the target of a coup de grace." |
| `Confused` ← **o precedente que você quer** | "**You can't make opportunity attacks or use your limited powers.** Your next attack action will be a basic or at-will attack against any nearby ally, determined randomly." |

> Empilhamento: "You can only be affected by the same condition once at a time. The worst one affects you and the lesser effects are ignored."
> Saves: "There are three difficulty values for saves. If a save doesn't specify what type it is, it's a normal save: 11+. Easy: Roll 6+ on a d20 / Normal: Roll 11+ on a d20 / Hard: Roll 16+ on a d20."

**`Confused` do 13A é literalmente o pacote que você está tentando montar:** nega a reação (opportunity attack) **e** nega o recurso (limited powers) na mesma condição. E o preço dele está abaixo.

### 2.3 Escada de preço dentro de UMA classe (Wizard, SRD)

Aqui o eixo de preço do 13A não é só nível — é **tipo de recarga** (at-will < cyclic/1x por batalha < daily).

| Nível | Feitiço | Recarga | Efeito literal |
|---|---|---|---|
| 1º | `Color Spray` | "Cyclic (cast once per battle OR at-will when the escalation die is even)" | "...if the target has 10 hp or fewer after the damage, it is weakened until the end of your next turn" — nenhuma ação perdida |
| 1º | `Ray of Frost` (+ feat) | at-will | daza só em "natural even hit" contra alvo staggered |
| 3º | `Rebuke` | **Cyclic** | "the target is hampered (only makes basic attacks) until the end of your next turn" — **mantém as ações, perde as opções** |
| 3º | `Confusion` | **Daily** | "The target is confused (save ends)" — perde opportunity attack + limited powers |
| 3º | `Hold Monster` | **Daily**, hp cap 60 | "cannot move or use move actions (hard save ends, 16+)" — **um tipo de ação negado custa Daily + save difícil + teto de HP** |
| 3º | `Sleep` | **Daily** | "unconscious (hard save ends, 16+...)" |
| 5º | `Denial` | **Daily** | hampered em 1d4 inimigos |

Lista de níveis conferida em https://www.13thagesrd.com/classes/wizard/ (1st: Acid Arrow, Blur, Charm Person, Color Spray, Magic Missile, Ray of Frost, Shield, Shocking Grasp / 3rd: Confusion, Crescendo, Force Salvo, Hold Monster, Lightning Bolt, Rebuke, Sleep, Teleport Shield / 5th: Denial, Dimension Door, Fireball, Invisibility).

### 2.4 `Stunned` no 13A nunca é "acertou, tomou"

Varrendo 13thagesrd.com, stun de PC sempre vem como **rider de gatilho raro**: "Natural 18+: The target is also stunned until the end of your next turn" (wizard), "Natural 19+" (necromancer), "If both attack rolls hit, the target is stunned until the end of its next turn" (Paladin, Avenging Smite), "Natural Even Hit: ...if the target has 180 hp or fewer after the attack, it's stunned" (monk). Fonte: busca em site:13thagesrd.com — páginas de Wizard/Necromancer/Paladin/Monk.

### 2.5 Negar a triggered action do monstro — `NÃO CONFIRMADO` em 2e

Não achei SRD gratuito/integral de **13th Age 2e** (o 13thagesrd.com é o Archmage Engine/1e). A página oficial https://pelgranepress.com/13th-age-second-edition/ e o FAQ https://pelgranepress.com/2025/11/24/13th-age-faq-2/ confirmam que 2e reformatou poderes de monstro com cabeçalho `[Triggered action]` (exemplo que vi citado: "[Triggered action] Spirit guardian: When the spirit caller becomes staggered it gains +2 to all its defenses until it is next hit."), mas **não consegui texto de regra literal de 2e numa fonte livre — marque 2e como NÃO CONFIRMADO.** No 1e: não existe efeito genérico de PC do tipo "o monstro perde a triggered action"; os gatilhos do monstro dependem da rolagem dele, e a única negação geral é `Stunned` ("can't take any actions") ou `Confused` (só opportunity attacks). Um caso pontual 3pp: Swordmage — "If your roll equals or beats the natural attack roll, you negate the attack and the target is stunned until the end of its next turn" (https://www.13thagesrd.com/classes/3rd-party-classes/swordmage/).

---

## 3. LANCER (Massif Press)

Fonte primária usada: **dados oficiais da Massif Press** que alimentam o COMP/CON — https://raw.githubusercontent.com/massif-press/lancer-data/master/lib/statuses.json e `.../lib/actions.json`. Checagem cruzada: https://lancer.wiki.gg/wiki/Condition e https://lancer.wiki.gg/wiki/Tech_attack

### 3.1 Quem nega Reação — resposta direta

| Condição | Texto literal (statuses.json) | Nega reação? |
|---|---|---|
| `JAMMED` | "JAMMED characters can't: • use comms to talk to other characters; • make attacks, other than IMPROVISED ATTACK, GRAPPLE, and RAM; • **take reactions**, or take or benefit from tech actions." | **SIM** |
| `STUNNED` | "STUNNED mechs cannot OVERCHARGE, move, or take any actions – **including free actions and reactions**. Pilots can still MOUNT, DISMOUNT, or EJECT from STUNNED mechs, and can take actions normally. STUNNED mechs have a maximum of 5 EVASION, and automatically fail all HULL and AGILITY checks and saves." | **SIM** (tudo) |
| `SLOWED` | "The only movement SLOWED characters can make is their standard move, on their own turn – they can't BOOST or make any special moves granted by talents, systems, or weapons." | **NÃO** (é só movimento) |
| `IMPAIRED` | "IMPAIRED characters receive +1 difficulty on all attacks, saves, and skill checks." | NÃO |
| `IMMOBILIZED` | "IMMOBILIZED characters cannot make any voluntary movements, although involuntary movements are unaffected." | NÃO |
| `LOCK ON` | "Hostile characters can choose to consume a character's LOCK ON condition in exchange for +1 accuracy on their next attack against that character. LOCK ON is also required to use some talents and systems." | **NÃO** — Lock On é buff de acerto, não negação |
| `SHREDDED` | "SHREDDED characters don't benefit from ARMOR or RESISTANCE." | NÃO |
| `GRAPPLED` (status-like) | "A Grappling character is engaged and can't boost or take reactions." (https://lancer.wiki.gg/wiki/Status) | **SIM** |

→ Dos cinco que você listou, **só `JAMMED` e `STUNNED`** negam reação. `LOCK ON` e `SLOWED` não.

### 3.2 O preço: mesma ação, acesso diferente

A opção de invade **universal, que todo mech tem de graça**:

> `FRAGMENT SIGNAL` — "You feed false information, obscene messages, or phantom signals to your target's computing core. They become IMPAIRED and SLOWED until the end of their next turn."
> — actions.json; INVADE é **quick tech** ("Any tech attack which is a quick action is, by definition, a quick tech attack." / "On a success, your target takes heat 2 and you choose one of the invasion options available to you.") https://lancer.wiki.gg/wiki/Tech_attack

Já `JAMMED` exige sistema licenciado — e está no **tier mais baixo de licença (LL1)**:

> `Eject Power Cores` (HORUS Goblin, H0r_OS System Upgrade I) — "Your target becomes jammed until the end of their next turn as you temporarily disrupt their systems, ejecting ammo magazines and cooling rods. Characters adjacent to your target take energy 2."
> — https://lancer.wiki.gg/wiki/Tech_attack

Ou seja: **mesmo custo de ação (1 quick), a diferença é só acesso (licença LL1 vs grátis)**. Negar reação + ataques + tech no LANCER custa "um sistema de licença nível 1", não um recurso escasso.

### 3.3 LANCER e a pergunta do recurso

`OVERCHARGE` é do lado do jogador (o `STUNNED` cita "cannot OVERCHARGE" como algo de mech de PC). O ataque ao "recurso" do inimigo no LANCER **não é drenar poço, é ENCHER medidor**: todo tech attack bem-sucedido joga "heat 2" no alvo. `NÃO CONFIRMADO`: não consegui o texto literal de HEAT CAP de NPC nem de OVERCHARGE — `lancer.wiki.gg/wiki/Heat`, `/wiki/NPC` e `/wiki/Overcharge` deram **404**.

### 3.4 ICON (Massif Press) — `PARCIALMENTE CONFIRMADO`

O PDF do ICON 1.5 (43 MB, https://massif-press.itch.io/icon) não é buscável por fetch. O devlog oficial https://massif-press.itch.io/icon/devlog/542899/icon-15-playtest-released confirma só as mudanças macro: "Slow removed, changed to dazed (from old stalwart status)", "Stun has been changed", "Removed many saves to avoid statuses".

Texto de `STUNNED` do ICON que encontrei em post de discussão no itch (https://itch.io/post/9343438) — **atribuição de autor incerta, trate como indício, não como regra citável**:

> "You may only take 1 ACTION and no REACTIONS on your next turn, but do so as a SLOW TURN."

Se confere, é o dado mais direto de todos pro seu caso: o ICON **empacota** "perde 1 ação + perde a reação + age por último" dentro de **um único** status chamado stunned. Perder a reação nunca é o produto principal — é rider.

---

## 4. Tabela consolidada

| efeito | sistema | o que tira | nível / custo | texto literal | URL |
|---|---|---|---|---|---|
| `Off-Guard` | PF2e | nada de ação, só −2 CA | 1 ação + perícia, à vontade (ou grátis por flanco) | "Attempt a Deception check. Success: The target is flat-footed against the next melee attack you attempt." | https://2e.aonprd.com/Actions.aspx?ID=48 |
| `Prone` via Trip | PF2e | 1 ação **dele** (pra Stand) | 1 ação + Athletics, à vontade, sem recurso | "Attempt an Athletics check against the target's Reflex DC. Success: The target falls and lands prone." | https://2e.aonprd.com/Actions.aspx?ID=2382 |
| `Grabbed` via Grapple | PF2e | 1 ação dele (Escape) | 1 ação + Athletics | "Success: Your target is grabbed until the end of your next turn." | https://2e.aonprd.com/Actions.aspx?ID=35 |
| "can't use reactions" | PF2e | **só a reação** | **rank 2, grau de sucesso BAIXO** | "The target is plagued with uncontrollable laughter. It can't use reactions." | https://2e.aonprd.com/Spells.aspx?ID=1583 |
| `Slowed 1` + no reactions | PF2e | 1 ação **+** reação | **rank 2, grau de sucesso ALTO** | "The target is slowed 1 and can't use reactions." | https://2e.aonprd.com/Spells.aspx?ID=1583 |
| `Slowed 1` (focus) | PF2e | 1 ação | Focus 1 (1 Focus Point), em Failure | "Failure The target is slowed 1 and off-guard." | https://2e.aonprd.com/Spells.aspx?ID=2896 |
| `Slowed 1` (afflição) | PF2e | 1 ação, atrasada | rank 1, só no Stage 2 | "Stage 2 sickened 1 and slowed 1 (1 round)" | https://2e.aonprd.com/Spells.aspx?ID=1545 |
| `Slowed 1` 1 minuto / `Slowed 2` | PF2e | 1–2 ações pela luta | **rank 3** | "Failure The target is slowed 1 for 1 minute. Critical Failure The target is slowed 2 for 1 minute." | https://2e.aonprd.com/Spells.aspx?ID=1677 |
| `Stunned 1` | PF2e | 1 ação, sem contorno | **talento nv. 2 + 2 Strikes + save + Incapacitation** | "...be stunned 1 (or stunned 3 on a critical failure). This is an incapacitation effect." | https://2e.aonprd.com/Feats.aspx?ID=442 |
| `Quickened` (+1 ação) | PF2e | dá 1 ação | **rank 3** | "It gains the quickened condition and can use the extra action each round for only Strike and Stride actions." | https://2e.aonprd.com/Spells.aspx?ID=1553 |
| `Confused` | PF2e | reação + Ready/Delay + aliados | condição (de feitiços altos) | "you can't Delay, Ready, or use reactions" | https://2e.aonprd.com/Conditions.aspx?ID=63 |
| `Dazed` | 13A | nada de ação (−4 atk) | rider at-will / 1º nível | "You take a –4 penalty to attacks." | https://www.13thagesrd.com/combat-rules/ |
| `Hampered` | 13A | opções, **não** ações | **3º nível, Cyclic** (Rebuke) | "You can only make basic attacks. You can still move normally." / "the target is hampered ... until the end of your next turn" | https://www.13thagesrd.com/combat-rules/ · https://www.13thagesrd.com/classes/wizard/ |
| `Confused` | 13A | **opportunity attack + limited powers** | **3º nível, Daily, save ends** | "You can't make opportunity attacks or use your limited powers." | https://www.13thagesrd.com/combat-rules/ |
| "no move actions" | 13A | 1 tipo de ação | **3º nível, Daily, hard save 16+, cap 60 hp** | "cannot move or use move actions (hard save ends, 16+)" | https://www.13thagesrd.com/classes/wizard/ |
| `Stunned` | 13A | **tudo**, inclusive interrupt | rider de gatilho raro (Natural 18+/19+, dois acertos, cap de hp) | "You suffer a –4 penalty to defenses and can't take any actions." | https://www.13thagesrd.com/combat-rules/ |
| 1 interrupt / rodada | 13A | — (a régua) | — | "You can use one interrupt action when it's not your turn. You can't use another one until the end of your next turn." | https://www.13thagesrd.com/combat-rules/ |
| `FRAGMENT SIGNAL` | LANCER | movimento extra + −1 acerto | **1 quick action, universal, grátis** | "They become IMPAIRED and SLOWED until the end of their next turn." | https://lancer.wiki.gg/wiki/Tech_attack |
| `JAMMED` | LANCER | **reações** + ataques + tech + comms | **1 quick action, sistema licença LL1** | "take reactions, or take or benefit from tech actions" | https://raw.githubusercontent.com/massif-press/lancer-data/master/lib/statuses.json |
| `STUNNED` | LANCER | tudo (ações, free actions, reações, overcharge, movimento) | raro | "cannot OVERCHARGE, move, or take any actions – including free actions and reactions" | https://raw.githubusercontent.com/massif-press/lancer-data/master/lib/statuses.json |
| `LOCK ON` | LANCER | **nada** (é buff de acerto) | 1 quick action, universal | "in exchange for +1 accuracy on their next attack against that character" | https://raw.githubusercontent.com/massif-press/lancer-data/master/lib/statuses.json |
| `STUNNED` | ICON | 1 ação + reação + vai por último | `PARCIALMENTE CONFIRMADO` | "You may only take 1 ACTION and no REACTIONS on your next turn, but do so as a SLOW TURN." | https://itch.io/post/9343438 |

### Fontes que falharam / bloqueadas
- `lancer.wiki.gg/wiki/Heat`, `/wiki/NPC`, `/wiki/Overcharge` → **HTTP 404**
- `13thagesrd.com/combat-rules/saving-throws/` → **HTTP 404** (os saves estão na própria página `/combat-rules/`)
- ICON 1.5 PDF (43 MB, massif-press.itch.io/icon) → não fetchável; SRD aberto de ICON **não existe** que eu tenha achado
- **13th Age 2e**: nenhum SRD gratuito integral localizado. Tudo de 13A aqui é 1e / Archmage Engine.
- PF2e: **não achei** nenhum efeito de PC que drene slot/Focus Point/carga de monstro (varri índice de feitiços via Elasticsearch da AoN, traits, Rules 786, Rules 2228 e busca web). Único ataque a recurso: `Counterspell`, troca 1:1.

---

## 5. O que isto diz pro preço

1. **Negar reação é vendido BARATO, e os três sistemas concordam** — o `Laughing Fit` do PF2e (rank 2) entrega "can't use reactions" no grau de sucesso *Success* e só adiciona `slowed 1` no *Failure*, ou seja, a própria Paizo precificou reação **um degrau abaixo** de uma ação; no LANCER, `JAMMED` (que mata reação, ataque e tech) custa 1 quick action com um sistema de licença **LL1**, o tier mais baixo que existe; no ICON, perder a reação nunca é produto, vem empacotado como rider de `STUNNED`.
2. **Ação e reação são orçamentos separados, não frações da mesma coisa** — o PF2e escreve isso explicitamente ("Certain abilities... say specifically that you can't use reactions") e `Slowed` *não toca* a reação em nenhum grau; isso é um aviso direto contra a sua régua "reação ≈ meia ação": os precedentes não tratam reação como fração de ação, tratam como um segundo recurso, menor e mais barato.
3. **Uma ação inteira negada é caro e sempre vem com freio** — rank 2 pra 1 rodada e rank 3 pra 1 minuto no PF2e, com o trait `Incapacitation` podendo subir um grau de sucesso do alvo quando ele é mais forte; no 13A, negar *um tipo* de ação (`Hold Monster`) já custa Daily + hard save 16+ + teto de HP, e `Stunned` (tudo) nunca é resultado de acerto simples, é rider de Natural 18+/19+.
4. **O precedente exato do pacote que você quer existe e se chama `Confused` (13th Age):** "You can't make opportunity attacks **or use your limited powers**" — negar reação **e** negar recurso na mesma condição, precificado em **3º nível, Daily, save ends**. É o molde pra uma `Sobrecarga` que queira manter as duas metades.
5. **Sobre "custa o dobro de energia" contra inimigo: os sistemas publicados desistiram dessa metade** — o monstro do PF2e *tem* poço gastável (spell slots e Focus Points no stat block) e mesmo assim a Paizo **não publicou nenhum efeito de jogador que drene isso**; o LANCER resolveu indo no sentido oposto, medidor que **enche** (heat 2 em todo tech attack) em vez de poço que esvazia. Traduzindo pro seu caso: troque "custa o dobro de energia" por um custo que o inimigo **realmente paga em ação** (reação negada = tier `Leve`; uma ação = `Média`), ou invente um medidor que sobe — não um que desce.
