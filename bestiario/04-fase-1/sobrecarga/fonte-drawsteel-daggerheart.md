# Sobrecarga — o que Draw Steel, Daggerheart e Weird Wizard cobram pra negar a reação do inimigo

**Data:** 09/09/2026
**Pergunta:** a metade "custa o dobro de energia" da `Sobrecarga` morreu (inimigo não tem poço gastável). Preciso reescrever contra Reação, ações por rodada, ou a `Intervenção` (= Villain Action do Draw Steel). Quanto os três sistemas cobram por isso?

**Veredito curto:** negar a **reação comum** é BARATO nos três. Negar a **ação especial fora do turno** (Villain Action / fury token / end-of-round) é **impossível** no Draw Steel e, no Weird Wizard, só existe quando o bloco do monstro escreve a exceção na mão. Nenhum dos três vende isso como condição genérica.

---

## 1. DRAW STEEL — existe algo do herói que pare uma Villain Action?

### Resposta: NÃO. Zero. Em nenhum preço.

Como procurei (pra o "não existe" valer):

Clonei os dois repositórios oficiais de dados do Steel Compendium — que são o texto das regras transcrito, o mesmo que alimenta o site:
- https://github.com/SteelCompendium/data-rules-md (livro *Heroes*: classes, habilidades, features, kits, títulos, perks, tesouros, condições, capítulos)
- https://github.com/SteelCompendium/data-md (livro *Monsters*: bestiário + Monster Basics + capítulos do Director)

**4.242 arquivos .md.** Grep em tudo.

**Resultado:** o termo "villain action" aparece no lado do herói em **exatamente um lugar** — e não é um bloqueio, é um *lucro*:

> "- The first time the Director deals damage to a hero using a Villain action or an ability that costs Malice, you gain 2 drama."
> — *Melodrama*, Troubadour 4th-Level Feature
> https://github.com/SteelCompendium/data-rules-md/blob/main/Features/Troubadour/4th-Level%20Features/Melodrama.md

Fora disso, "villain action" só aparece dentro de statblocks de monstro (☠️) e no capítulo Monster Basics. **Nada impede, atrasa, rouba ou cancela.**

### Texto literal da Villain Action

> "A creature with villain actions always has three. Each villain action can be used only once per encounter, and no more than one villain action can be used per round. (This holds even if you have two or more creatures with villain actions in an encounter, though such an occurrence should be rare.)
>
> A creature can use a villain action at the end of any other creature's turn during combat. Villain actions are numbered and intended to be used in a specific order that creates a logical encounter flow and cinematic arc, but you can use them in any order you choose."
> — *Draw Steel: Monsters*, Monster Basics
> https://steelcompendium.io/v2/Browse/rule/monster/villain-action/
> (mesmo texto: https://github.com/SteelCompendium/data-md/blob/main/Bestiary/Monsters/Chapters/Monster%20Basics.md)

Confirmado: é idêntico à sua `Intervenção`. 3 por luta, cada uma uma vez, máximo 1 por rodada, no fim do turno de outra criatura.

### E o Malice? Dá pra impedir o vilão de gastar?

**Não.** Grep por "can't spend Malice / prevents Malice / lose Malice / reduce Malice" no corpus inteiro: **nenhuma regra de herói faz isso.**

O que existe são três padrões, e nenhum é negação:

**(a) TAXAR o gasto** — dói, mas acontece:

> "**Effect:** While suppressed, a target takes psychic damage equal to twice your Intuition score at the start of their turns, whenever they use a supernatural ability, or whenever they use an ability that costs Malice."
> — *Arcane Purge* (11 Discipline), Null 8th-Level
> https://github.com/SteelCompendium/data-rules-md/blob/main/Abilities/Null/8th-Level%20Features/Arcane%20Purge.md

> "**Effect:** While weakened this way, the target takes damage equal to your Intuition score whenever they use a supernatural ability that costs Malice."
> — *Arcane Disruptor* (5 Discipline), Null 1st-Level
> https://github.com/SteelCompendium/data-rules-md/blob/main/Abilities/Null/1st-Level%20Features/Arcane%20Disruptor.md

> "**Effect:** Until the end of the encounter or until you are dying, whenever a target uses an ability that costs Malice (see *Draw Steel: Monsters*), they take holy damage equal to three times your Presence score. A target judged by you takes an extra 2d6 holy damage."
> — *Edict of Perfect Order* (7 Wrath), Censor 3rd-Level, **maneuver, 2 aura, cada inimigo na área**
> https://github.com/SteelCompendium/data-rules-md/blob/main/Abilities/Censor/3rd-Level%20Features/Edict%20of%20Perfect%20Order.md

**(b) LUCRAR com o gasto:**

> "**Effect:** You gain 6 surges. Until the end of the encounter or until you are dying, whenever the Director spends Malice (see *Draw Steel: Monsters*), choose yourself or one ally within 10 squares. The chosen character gains 2 of their Heroic Resource."
> — *Counterstrategy* (11 Focus), Tactician 9th-Level
> https://github.com/SteelCompendium/data-rules-md/blob/main/Abilities/Tactician/9th-Level%20Features/Counterstrategy.md

> "The first time each combat round that the Director uses an ability that costs Malice (see *Draw Steel: Monsters*), you gain 1 discipline."
> — *Discipline in Combat*, Null 1st-Level (recurso de classe)
> https://github.com/SteelCompendium/data-rules-md/blob/main/Features/Null/1st-Level%20Features/Discipline%20in%20Combat.md

**(c) SEQUESTRAR uma habilidade** — o mais perto que chega, e não alcança Villain Action:

> "**Trigger:** The target dies. **Effect:** Before the target dies, you can look at their stat block and force them to use one ability that is a main action or a maneuver. If the ability costs a Heroic Resource or Malice, the creature can use it without any cost."
> — *Word of Final Redemption* (11 Piety), Conduit 9th-Level
> https://github.com/SteelCompendium/data-rules-md/blob/main/Abilities/Conduit/9th-Level%20Features/Word%20of%20Final%20Redemption.md

Note: "**one ability that is a main action or a maneuver**" — Villain Action está explicitamente fora.

### A prova mais forte: reduzir Malice é REGRA DA CASA, não regra do jogo

No capítulo "For the Director", na caixa de variantes opcionais:

> "You can always change the rules of the game to fit your campaign and taste! [...] **You could allow heroes to spend hero tokens to reduce the amount of Malice you have** (see *Draw Steel: Monsters*). You might decide that all heroes have a free +1 bonus to any characteristic of their choice at 1st level."
> — *Draw Steel: Heroes*, Chapters/For the Director
> https://github.com/SteelCompendium/data-rules-md/blob/main/Chapters/For%20the%20Director.md

Isso é ouro pro seu caso. Os designers **pensaram** em deixar o herói atacar o Malice e **jogaram isso pra fora do baseline**, na mesma lista de "se você quiser mudar o jogo". Ao lado de "crítico só no 20 natural". Ou seja: mexer na economia do Director não tem preço na escada — está fora da escada.

---

## 2. DRAW STEEL — condições que tiram ação, e Dazed

Draw Steel tem **10 condições**, fim. Lista completa do diretório:
`Bleeding, Dazed, Frightened, Grabbed, Prone, Restrained, Slowed, Taunted, Weakened` (+ `_Index`)
https://github.com/SteelCompendium/data-rules-md/tree/main/Conditions

### Dazed — sua suspeita estava CERTA. Texto literal:

> "**Dazed:** A creature who is dazed can do only one thing on their turn: use a main action, use a maneuver, or use a move action. A dazed creature also can't use triggered actions, free triggered actions, or free maneuvers."
> — *Draw Steel Rules Reference V1* (PDF oficial gratuito da MCDM), seção Conditions
> https://files.mcdmproductions.com/DrawSteel/DrawSteelRulesReferenceV1.pdf
> (idem: https://steelcompendium.io/v2/Browse/rule/combat/condition/)

### As outras quatro que você pediu:

> "**Slowed:** A creature who is slowed has speed 2 unless their speed is already lower, and they can't shift."

> "**Restrained:** A creature who is restrained has speed 0, can't use the Stand Up maneuver, and can't be force moved. A restrained creature takes a bane on ability rolls and on Might and Agility tests, and abilities used against them gain an edge."

> "**Weakened:** A creature who is weakened takes a bane on power rolls."

> "**Taunted:** A creature who is taunted has a double bane on ability rolls for any ability that doesn't target the creature who taunted them, as long as they have line of effect to that creature."
> — todas do mesmo PDF oficial: https://files.mcdmproductions.com/DrawSteel/DrawSteelRulesReferenceV1.pdf

**Só Dazed toca em ação.** Slowed, Restrained, Weakened e Taunted são todas movimento ou penalidade de rolagem. Nenhuma tira ação.

### A reação do Draw Steel = Triggered Action

> "**Triggered Action:** You can take one triggered action per round when the trigger happens. There is no limit to the number of free triggered actions you can take."
> — https://files.mcdmproductions.com/DrawSteel/DrawSteelRulesReferenceV1.pdf

> "You can use one triggered action per round, either on your turn or another creature's turn, but only when the action's trigger occurs."
> "A free triggered action follows the same rules as a triggered action, but it doesn't count against your limit of one triggered action per round."
> "**Any effect that prevents you from using triggered actions also prevents you from using free triggered actions.**"
> — https://steelcompendium.io/v2/Browse/rule/combat/triggered-action/

### ⚠️ Dazed NÃO para a Villain Action — e tem prova estrutural

Isto é **inferência do texto de regra**, não ruling oficial (procurei fórum/reddit, nada de oficial — marcar `NÃO CONFIRMADO` como ruling, mas o texto é bem claro):

1. Dazed restringe duas coisas: o que você faz **no seu turno**, e **triggered actions / free triggered actions / free maneuvers**. Villain Action não está em nenhuma das duas listas.
2. Villain Action não é um tipo de ação. No statblock, o campo de tipo de ação de uma Villain Action é literalmente `-`, enquanto uma triggered action diz `Triggered action`:

> `❗️ **Courtesy Call**` → `| **Ranged** | **Triggered action** |`
> `☠️ **Close In (Villain Action 1)**` → `| **Area** | **-** |`
> — *Orc Warleader*
> https://github.com/SteelCompendium/data-md/blob/main/Bestiary/Monsters/Monsters/Orcs/Statblocks/Orc%20Warleader.md

3. A legenda do statblock separa os dois explicitamente:

> "- ❗️ A **triggered action**
> - ☠️ A feature or ability specific to a leader or solo creature, such as **villain actions**"
> — Monster Basics
> https://github.com/SteelCompendium/data-md/blob/main/Bestiary/Monsters/Chapters/Monster%20Basics.md

4. **E a prova decisiva:** quando o designer quer que Dazed *não* alcance algo, ele escreve isso no bloco do monstro. Aparece em ~10 features de Malice:

> "The dragon takes an additional main action on their turn. **They can use this feature even if they are dazed.**"
> — *Gloom Dragon Malice* (e Crucible, Omen, Thorn, Meteor, Medusa, Shambling Mound...)
> https://github.com/SteelCompendium/data-md/blob/main/Bestiary/Monsters/Monsters/Dragons/Features/Gloom%20Dragon%20Malice.md

> "Whenever any demon is reduced to 0 Stamina within 10 squares of Aurumvas, the Director gains 1 Malice. **Aurumvas loses this trait while he is dazed.**"
> — *Aurumvas*
> https://github.com/SteelCompendium/data-md/blob/main/Bestiary/Monsters/Monsters/Demons/Statblocks/Aurumvas.md

Ou seja: Dazed **só alcança o que o texto dele diz** mais o que o bloco do monstro mandar alcançar. Nenhuma Villain Action em todo o bestiário tem cláusula de Dazed. Ela é imune por omissão.

### Malice — texto literal (pra referência)

> "At the start of combat, you gain Malice equal to the average number of Victories per hero. Then at the start of each combat round, you gain Malice equal to the number of heroes in the battle, plus the combat round number."
> "If a hero dies, they stop generating Malice for you. At the end of an encounter, any unused Malice is lost."
> "Monsters can spend Malice the way heroes spend their Heroic Resource, activating and enhancing their abilities."
> — https://steelcompendium.io/v2/Browse/rule/monster/malice/

### 🔑 O PREÇO de negar a triggered action no Draw Steel: BARATO

Levantei todas as habilidades de herói que aplicam `dazed` — **22** — e o custo delas:

| Nível | Habilidade | Custo |
|---|---|---|
| **1st** | Repent! (Censor) | **3 Wrath** |
| **1st** | Stunning Blow (Null) | **3 Discipline** |
| **1st** | Concussive Strike (Tactician) | **3 Focus** |
| **1st** | Hypnotic Overtones (Troubadour) | **3 Drama** |
| 2nd | Death... Death! / Phalanx-Breaker / Visceral Roar (Fury) | 5 Ferocity |
| 2nd | Applied Chronometrics / Overwhelm (Talent) | 5 Clarity |
| 3rd | Soul Burn (Talent) | 7 Clarity |
| 5th–9th | Phase Step, Realitas, Pillar of Holy Fire, etc. | 9–11 |

Quatro classes diferentes compram Dazed no **degrau mais baixo que existe (3 de recurso, 1º nível)**. Exemplo literal:

> "**Power Roll + Might:** ≤11: 3 + M damage; M < WEAK, dazed (save ends) / 12-16: 5 + M damage; M < AVERAGE, dazed (save ends) / 17+: 8 + M damage; M < STRONG, dazed (save ends)"
> — *Concussive Strike* (3 Focus), Tactician 1st-Level, **Melee 1 or ranged 5, one creature**
> https://github.com/SteelCompendium/data-rules-md/blob/main/Abilities/Tactician/1st-Level%20Features/Concussive%20Strike.md

E fica mais barato ainda. Tem **três** efeitos que negam triggered action direto, sem passar por Dazed:

> "**Effect:** A target can't use triggered actions while their speed is reduced this way."
> — *Slow* (5 Clarity), Talent 2nd-Level — **é MANEUVER, Ranged 10, TRÊS criaturas**
> https://github.com/SteelCompendium/data-rules-md/blob/main/Abilities/Talent/2nd-Level%20Features/Slow.md

> "Your ward slows time for your enemies. Whenever a creature deals damage to you, their speed is reduced by an amount equal to your Reason score and **they can't use triggered actions until the end of their next turn.**"
> — *Entropy Ward*, Talent 1st-Level — **passiva, nível 1, custo ZERO**
> https://github.com/SteelCompendium/data-rules-md/blob/main/Features/Talent/1st-Level%20Features/Entropy%20Ward.md

> "**Effect:** A target can't use triggered actions while their speed is reduced this way." (mesmo texto, via subclass feature)
> — 2nd Level Chronopathy Ability
> https://github.com/SteelCompendium/data-rules-md/blob/main/Features/Talent/2nd-Level%20Features/2nd%20Level%20Chronopathy%20Ability.md

**Leitura:** negar triggered action no Draw Steel é rider. Vem grudado de graça numa manobra de nível 2 que pega três alvos, ou numa passiva de nível 1. Não é o produto que se compra — é o brinde.

---

## 3. DAGGERHEART — adversário tem Reaction? O que dá pra fazer?

### Sim, e a Reaction é explicitamente fora do turno

> "• **Actions:** a special attack or other unique action that the adversary can perform when the spotlight is on them.
> • **Reactions:** special effects that take effect when their trigger occurs, **regardless of whether the spotlight is on the adversary.**
> • **Passives:** special abilities that remain in effect by default and require no resources or triggers to activate."
> — *Daggerheart SRD* (Darrington Press), Adversaries, p.70
> https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf
> (espelho HTML: https://daggerheartsrd.com/rules/adversaries/)

Exemplos de Reaction que consomem Stress (relevante pra você):

> "**Team-Up - Reaction:** When another adversary within Very Close range of this adversary deals X damage to a creature, you can **mark a Stress** to make a standard attack against that same creature. On a success, combine the damage."
> "**Heavy Hitter - Reaction:** When this adversary deals damage with a standard attack, you can **spend a Fear** to gain a +X bonus to the damage roll."
> — *Daggerheart SRD*, Example Adversary Features, p.71
> https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf

### O Stress do adversário funciona igual ao do PC

> "**DAMAGE THRESHOLDS, HIT POINTS, AND STRESS** — These systems function the same way they do for PCs."
> "Note: each adversaries stress is tracked individually. If a feature requires the GM to spend Stress to activate it, the Stress must come from the adversary whose feature is being activate."
> — *Daggerheart SRD*, p.70 (sic, erro de digitação no original)
> https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf

### 🔑 As DUAS regras que você pediu literais

**(1) Encher o Stress = Vulnerable + trava as features que custam Stress:**

> "When a character marks their last Stress, they become Vulnerable (see: Conditions) until they clear at least 1 Stress. When a character must mark 1 or more Stress but can't, they mark 1 HP instead. **A character can't use a move that requires them to mark Stress if all of their Stress is marked.**"
> — *Daggerheart SRD*, Stress
> https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf

**(2) Vulnerable:**

> "When a creature is Vulnerable, all rolls targeting them have advantage."
> — *Daggerheart SRD*, Conditions
> https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf

Isso é **o lever indireto**: você não nega a Reaction, você enche o tanque. Reaction que custa Stress (Team-Up, Rivalry, Overcharge...) morre sozinha quando o Stress enche. E ainda vira Vulnerable de brinde.

### Daggerheart só tem TRÊS condições padrão, e nenhuma tira ação

> "Daggerheart has three standard conditions:"
> "**HIDDEN** — While you're out of sight from all enemies and they don't otherwise know your location, you gain the Hidden condition. Any rolls against a Hidden creature have disadvantage."
> "**RESTRAINED** — Restrained characters can't move, but you can still take actions from their current position."
> "**VULNERABLE** — When a creature is Vulnerable, all rolls targeting them have advantage."
> — *Daggerheart SRD*, Conditions
> https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf

Repara: **nem Restrained tira ação.** "can't move, but you can still take actions". O baseline do Daggerheart não nega ação pra ninguém.

### Negar Reaction existe — mas como condição ESPECIAL em duas cartas

Grep no SRD inteiro por "can't use reactions": **2 hits.** As duas dizem a mesma frase, e as duas são cartas de domínio.

**A barata:**

> "Make a Spellcast Roll against all adversaries in front of you within Close range. Once per rest on a success, create an illusion of flashing colors and lights that temporarily Stuns targets you succeed against and forces them to mark a Stress. **While Stunned, they can't use reactions and can't take any other actions until they clear this condition.**"
> — **HYPNOTIC SHIMMER**, Level 3 Grace Spell, **Recall Cost: 1**
> https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf
> (confirmação de nome/nível: https://daggerheartsrd.com/abilities/grace/)

**A caríssima:**

> "Make a Spellcast Roll to unleash powerful rays of burning sunlight against all adversaries in front of you within Far range. On a success, spend any number of Hope and force that many targets you succeeded against to make a Reaction Roll (14). Targets who succeed take 3d20+3 magic damage. Targets who fail take 4d20+5 magic damage and are temporarily Stunned. **While Stunned, they can't use reactions and can't take any other actions until they clear this condition.**"
> — **STUNNING SUNLIGHT**, Level 8 Splendor Spell
> https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf
> (confirmação de nome/nível: https://daggerheartsrd.com/abilities/splendor/)

**Mas o "temporarily" é o freio de preço:**

> "The **temporary** tag denotes a condition or effect that the affected creature can clear by making a move against it. [...] When an affected adversary makes a move to clear a temporary condition or effect, the GM puts the spotlight on the adversary and describes how they do it; **this doesn't require a roll but it does use up that adversary's spotlight.**"
> — *Daggerheart SRD*, Temporary Tags & Special Conditions
> https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf

Traduzindo: o Stun do Daggerheart **não** é negação. É um imposto de um spotlight. O inimigo sempre pode pagar pra sair. Por isso Hypnotic Shimmer pode ser Level 3 / Recall 1 / área / todos os adversários na frente.

### Forçar Stress no adversário é BARATÍSSIMO

> "**Scary:** On a successful attack, the target must mark a Stress."
> — propriedade de arma (Improved Longbow etc.), *Daggerheart SRD*, Weapons
> https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf

> "**Ruthless Predator:** When you make a damage roll, you can mark a Stress to gain a +1 bonus to your Proficiency. Additionally, **when you deal Severe damage to an adversary, they must mark a Stress.**"
> — Ranger specialization feature, passiva, custo zero
> https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf

> "• **Water:** When you deal damage to an adversary within Melee range, all other adversaries within Very Close range must mark a Stress."
> — Druid/Elemental Aura, specialization feature
> https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf

> "While this spell is active, an adversary must mark a Stress when they target you with an attack."
> — Level 3 Splendor Ability, Recall Cost 2 (passiva de aura)
> https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf

Ou seja: marcar Stress de inimigo no Daggerheart é tag de arma. É o preço mais baixo que existe no sistema.

---

## 4. WEIRD WIZARD — Reactions e End-of-Round

### O statblock tem os dois, confirmado com texto oficial da Schwalb

> "**Rampage** At the end of the round, roll a d6. On a 4 or higher, the green gorger's attacks deal an extra 2d6 damage until the end of the next round."
> "**Aggressive** (reaction, when the green gorger sees an enemy and has no enemy in reach; 1/minute) The gorger gains a move and can use it immediately."
> — *Green Gorger*, post oficial da Schwalb Entertainment
> https://schwalbentertainment.com/2023/04/20/enemies-combat-weird-wizard/

> "**Extra Reaction** A dragon increases the number of reactions it can use during a round by one."
> — *Dragon*, mesmo post
> https://schwalbentertainment.com/2023/04/20/enemies-combat-weird-wizard/

### Reação: uma por rodada

> "You can use a reaction once each round to perform one of the following special activities."
> "Each combatant can act out of turn just once each round by using a reaction."
> — *Weird Wizard Quick Play* (produto oficial gratuito da Schwalb)
> mirror consultado: https://pdfcoffee.com/weird-wizard-quick-play-digitalv6-pdf-free.html
> original (exige login): https://www.drivethrurpg.com/product/447890/Weird-Wizard-Quick-Play

### 🔑 CINCO afflictions negam reação. Texto literal:

> "**Stunned** — You cannot use actions or reactions. Your Speed drops to 0 and you cannot benefit from increases to Speed until this affliction ends. You grant 2 boons on rolls against you, and you make attribute rolls with 2 banes."
>
> "**Unconscious** — You cannot use actions or reactions. Your Speed drops to 0 and you cannot benefit from increases to Speed. You receive no information from your senses. You grant 3 boons on rolls against you, and you automatically fail all attribute rolls."
>
> "**Prone** — You are lying on the ground. **You cannot use reactions.** You grant 1 boon on rolls made to attack you with melee weapons, but impose 1 bane on rolls made to attack you with ranged weapons. You can use your move only to crawl or stand up."
>
> "**Confused** — You become unable to make sense of what is happening around you. **You cannot use reactions** and you make Intellect and Will rolls with 1 bane."
>
> "**Blinded** — [...] **You cannot make use of reactions that rely on sight.** Finally, your Speed is halved."
>
> "**Deafened** — You cannot hear. **You cannot make use of reactions that rely on hearing** and are not subject to effects that depend on hearing."
> — texto das afflictions do sistema licenciado oficial de Foundry VTT (`lang/en.json`), idêntico ao livro
> https://github.com/Savantford/foundry-weirdwizard/blob/main/lang/en.json
> (Stunned e Prone conferem com o Quick Play: https://pdfcoffee.com/weird-wizard-quick-play-digitalv6-pdf-free.html)

### 🔑 O PREÇO no Weird Wizard: o mais barato dos três. É de GRAÇA.

**Prone nega reação.** E derrubar no chão é uma opção de ataque básica universal, sem custo de recurso, sem nível, disponível pra todo mundo:

> "**Knockdown** — Choose one creature in your reach whose size is no more than 2 higher than yours. Make an Agility roll against the target's choice of Strength or Agility [...] the target falls prone."
> "**Shove** — [...] If the result of your roll is 20 or higher, the target falls prone."
> — *Weird Wizard Quick Play*, opções de ataque
> https://pdfcoffee.com/weird-wizard-quick-play-digitalv6-pdf-free.html

Um Knockdown bem-sucedido apaga a reação do inimigo pela rodada. Custo: nada. É a coisa mais barata do jogo.

### ⚠️ MAS: o Weird Wizard prova o seu ponto sobre ação especial fora do turno

O dragão tem uma economia de ação fora do turno (fury tokens) que é o análogo mais próximo da sua `Intervenção`. E olha como os designers a protegeram:

> "**Dragon Fury** At the start of combat, the dragon gains 3 fury tokens and retains them until it spends them or the combat ends. Once per round, when the dragon gets a failure on an attribute roll or a luck roll, the dragon adds 1 token to its supply.
>
> At any point, the dragon can spend 1 fury token to immediately perform one of the following activities **provided the banshee is neither stunned nor unconscious.** It can perform each activity just once. When it has performed each, it regains the ability to perform them all."
> — *Dragon*, post oficial da Schwalb
> https://schwalbentertainment.com/2023/04/20/enemies-combat-weird-wizard/
> (o "banshee" é erro de copy-paste do livro — o template é reaproveitado entre criaturas solitárias)

Isso é o achado estrutural. A condição Stunned diz "cannot use actions or reactions" — e **mesmo assim** o bloco do dragão precisou escrever `provided [it] is neither stunned nor unconscious` na mão. Por quê? Porque gastar um fury token **não é nem "action" nem "reaction"** — é uma categoria própria. A regra genérica não alcança. Tiveram que comprar o alcance com texto explícito.

E o end-of-round (`Rampage`) não tem `(action)` nem `(reaction)` no rótulo. Então Stunned **não alcança o end-of-round** tampouco. Ninguém escreveu exceção pra ele.

---

## 5. PERGUNTA TRANSVERSAL — barato ou caro?

Separa em duas perguntas, porque a resposta é oposta:

### (A) Negar a REAÇÃO comum → **BARATO nos três sistemas**

| Sistema | Efeito mais barato que nega reação | Preço |
|---|---|---|
| **Weird Wizard** | `Prone`, via Knockdown/Shove | **ZERO** — opção de ataque universal, sem nível, sem recurso |
| **Draw Steel** | `Entropy Ward` (passiva nível 1) | **ZERO** — passiva de subclasse |
| **Draw Steel** | `Slow` — 3 alvos, Ranged 10 | **5 Clarity, nível 2, MANEUVER** (rider grudado) |
| **Draw Steel** | `Dazed` | **3 de recurso, nível 1**, em 4 classes diferentes |
| **Daggerheart** | `Hypnotic Shimmer` — área, todos os adversários na frente | **Level 3, Recall Cost 1**, 1×/rest |

Nenhum dos três cobra caro. Em dois deles é literalmente grátis.

### (B) Negar a AÇÃO ESPECIAL FORA DO TURNO (Villain Action / fury token / end-of-round) → **não tem preço, porque não está à venda**

| Sistema | Negar a ação especial fora do turno? |
|---|---|
| **Draw Steel** | **Impossível.** Zero regras em 4.242 arquivos. Villain Action não é tipo de ação (`-` no statblock), então Dazed não alcança. Nenhum statblock do bestiário tem cláusula de Dazed em Villain Action. Atacar o Malice também é impossível — só taxar ou lucrar; reduzir Malice está listado como **variante opcional** no "For the Director". |
| **Weird Wizard** | Só com **cláusula escrita no bloco do monstro** (`provided [it] is neither stunned nor unconscious`). A condição genérica não alcança. End-of-round não tem cláusula nenhuma e é intocável. |
| **Daggerheart** | A Reaction é fora do turno e **é** negável via Stunned, mas só como *special condition* escrita em carta específica, e sempre `temporary` — o inimigo gasta um spotlight e sai. Nunca é travamento duro. |

---

## O que isto diz pro preço

Negar a **reação** do inimigo é barato em todos os três sistemas — Prone faz isso de graça no Weird Wizard, uma passiva de nível 1 faz de graça no Draw Steel, e Dazed é comprado no degrau mais baixo que existe (3 de recurso, 1º nível, em quatro classes). Então se você reescrever a `Sobrecarga` contra a **Reação**, ela é um efeito de tier baixo e não justifica preço de Melhoria caro: no Draw Steel esse efeito vem como *rider* de brinde numa manobra de nível 2 que pega três alvos. Negar a **ação especial fora do turno** é o oposto: os três sistemas se recusam a vender isso como condição genérica — a Villain Action do Draw Steel é literalmente inalcançável (não é tipo de ação, e nenhuma das 22 habilidades que aplicam Dazed a toca), e o Weird Wizard só consegue bloquear os fury tokens porque o bloco do dragão escreveu a exceção na mão. O sinal mais claro de todos é a MCDM ter colocado "heroes spend hero tokens to reduce the amount of Malice" na caixa de **regras opcionais da casa**, ao lado de "crítico só no 20" — eles olharam pra economia do Director e decidiram que ela fica fora da escada de preço. Recomendação de preço: se a `Sobrecarga` negar só a **Reação** do inimigo, cobra pouco (é efeito de entrada); se ela encostar na **`Intervenção`**, ela deixou de ser Melhoria e virou capstone — e os três sistemas dizem que esse efeito deve ser escrito no bloco do inimigo, não numa melhoria genérica de feitiço.

---

## Sites bloqueados / não acessados

| Site | O que aconteceu |
|---|---|
| `stawl.app` (texto dos livros Draw Steel) | **HTTP 403.** Contornado com os repos oficiais do Steel Compendium no GitHub. |
| `daggerheart.org` | **HTTP 403.** Contornado com o SRD PDF oficial de daggerheart.com. |
| `schwalbentertainment.com` via fetch normal | **Parse error.** Contornado via curl direto — conteúdo obtido. |
| `steelcompendium.io/compendium/main/...` | Páginas renderizadas por JS, voltam só o menu. As rotas `/v2/Browse/...` funcionam, e os repos GitHub resolvem tudo. |
| `drivethrurpg.com` (Weird Wizard Quick Play oficial) | Exige login. Usei mirror de terceiro (`pdfcoffee`) e cruzei o texto das afflictions com o sistema oficial de Foundry VTT — **bateram idênticos**. |

## `NÃO CONFIRMADO`

- **Ruling oficial da MCDM de que Dazed não para Villain Action.** Procurei em steelcompendium.io, no PDF oficial de regras, nos repos de dados e em busca de fórum/reddit. Não achei ruling explícito. A conclusão é inferência do texto de regra (Villain Action não é tipo de ação; Dazed lista o que alcança; nenhum statblock dá a ela cláusula de Dazed, enquanto ~10 features de Malice *têm* cláusula de Dazed). O texto é claro, mas não há ruling publicado.
- **Recall Cost de `Stunning Sunlight`.** O nome e nível (Level 8 Splendor) estão confirmados; o recall cost não saiu limpo do PDF (colunas embaralhadas) nem do espelho HTML.
