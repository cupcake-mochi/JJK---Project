# Fonte D&D — a que preço o D&D vende "o alvo perde a Reação"

**Data:** 09/09/2026
**Escopo:** D&D 5e 2014 (PHB/SRD 5.1), D&D 5e 2024 (PHB/Basic Rules 2024 + MM 2024), e 4e como contraste.
**Pergunta que isto responde:** a metade "custa o dobro de energia" da Melhoria `Sobrecarga` morreu junto com o poço de recurso do inimigo. Em que preço o D&D vende os substitutos (negar Reação / cortar ações / travar ação fora do turno)?

**Método:** texto de regra primeiro. Tudo abaixo tem citação literal + URL. O que não tem citação literal está marcado `NÃO CONFIRMADO`.

**Bloqueios que encontrei (e segui em volta):**
- `https://5thsrd.org/combat/the_order_of_combat/` → **HTTP 403**. Peguei a regra de Surpresa pelas Basic Rules 2014 no D&D Beyond.
- `https://dnd4.fandom.com/wiki/Dazed` → **HTTP 402 Payment Required**. Peguei o texto de `Dazed` no espelho dyasdesigns.
- `media.wizards.com/.../SRD_CC_v5.2.1.pdf` → **404**. O SRD 5.2 oficial em PDF não abriu; usei as Basic Rules 2024 no D&D Beyond (texto oficial, gratuito) + `dnd2024.wikidot.com`.
- `dndbeyond.com/sources/dnd/br-2024/spell-descriptions` → a página é gigante e o fetch cortou na letra **D**. Peguei Shocking Grasp e Slow 2024 no `dnd2024.wikidot.com`.
- `dnd5e.wikidot.com/spell:mind-whip` e `/conditions` → **404** (slug errado). Corrigi pra `spell:tashas-mind-whip` e `5thsrd.org/rules/conditions/`.

---

## 1. Tabela — efeitos que negam Reação (ou a condição-base que nega)

| efeito | edição | nível / tier | texto literal | URL |
|---|---|---|---|---|
| **Shocking Grasp** | 2014 | **Truque (nível 0)** — Artífice/Feiticeiro/Mago | "On a hit, the target takes 1d8 lightning damage, and it can't take reactions until the start of its next turn." | https://api.open5e.com/v1/spells/shocking-grasp/ · https://dnd5e.wikidot.com/spell:shocking-grasp |
| **Shocking Grasp** | **2024** | **Truque (nível 0)** | "On a hit, the target takes 1d8 Lightning damage, and it can't make **Opportunity Attacks** until the start of its next turn." | http://dnd2024.wikidot.com/spell:shocking-grasp |
| **Arms of Hadar** | 2014 | **Magia de 1º nível** (Bruxo), AoE 10 ft, salva Força | "On a failed save, a target takes 2d6 necrotic damage and can't take reactions until its next turn. On a successful save, the creature takes half damage, but suffers no other effect." | https://dnd5e.wikidot.com/spell:arms-of-hadar |
| **Arms of Hadar** | **2024** | **Magia de 1º nível** (Bruxo) | "On a failed save, a target takes 2d6 Necrotic damage and **can't take Reactions** until the start of its next turn. On a successful save, a target takes half as much damage only." | http://dnd2024.wikidot.com/spell:arms-of-hadar |
| **Blood Curse of Binding** | 2014 (Blood Hunter, Matt Mercer) | **Feature de nível 1** (Blood Maledict), ação bônus | "On a failure, the cursed creature's speed is reduced to 0 and it can't use reactions until the end of your next turn." | https://dnd5e.wikidot.com/blood-hunter:blood-curse |
| **Channel Divinity: Turn Undead** | 2014 | **Clérigo nível 2** (só mortos-vivos) | "A turned creature must spend its turns trying to move as far away from you as it can... **It also can't take reactions.** For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving." | https://dnd5e.wikidot.com/cleric |
| **Channel Divinity: Turn Undead** | **2024** | **Clérigo nível 2** (só mortos-vivos) | "If the creature fails its save, it has the **Frightened and Incapacitated** conditions for 1 minute." (→ Incapacitated nega Reação) | http://dnd2024.wikidot.com/cleric |
| **Open Hand Technique** | 2014 | **Monge nível 3** (subclasse), de graça no Flurry of Blows | "It can't take reactions until the end of your next turn." | https://dnd5e.wikidot.com/monk:open-hand |
| **Open Hand Technique — Addle** | **2024** | **Monge nível 3** | "**Addle.** The target can't make **Opportunity Attacks** until the start of its next turn." | http://dnd2024.wikidot.com/monk:warrior-of-the-open-hand |
| **Tasha's Mind Whip** | 2014 (TCE) | **Magia de 2º nível**, salva Inteligência, 1 rodada | "On a failed save, the target takes 3d6 psychic damage, and **it can't take a reaction until the end of its next turn**. Moreover, on its next turn, it must choose whether it gets a move, an action, or a bonus action; it gets only one of the three. On a successful save, the target takes half as much damage and suffers none of the spell's other effects." | https://dnd5e.wikidot.com/spell:tashas-mind-whip |
| **Slow** | 2014 | **Magia de 3º nível**, concentração, até 6 alvos | "An affected target's speed is halved, it takes a -2 penalty to AC and dexterity saving throws, and **it can't use reactions**. On its turn, it can use either an action or a bonus action, not both. Regardless of the creature's abilities or magic items, it can't make more than one melee or ranged attack during its turn." | https://api.open5e.com/v1/spells/slow/ |
| **Slow** | **2024** | **Magia de 3º nível**, concentração, até 6 alvos | "An affected target's Speed is halved, it takes a −2 penalty to AC and Dexterity saving throws, and **it can't take Reactions**. On its turns, it can take either an action or a Bonus Action, not both, and it can make only one attack if it takes the Attack action." | http://dnd2024.wikidot.com/spell:slow |
| **Confusion** | **2024** | **Magia de 4º nível**, concentração, AoE 10 ft | "...or that target **can't take Bonus Actions or Reactions** and must roll 1d10 at the start of each of its turns to determine its behavior for that turn..." | http://dnd2024.wikidot.com/spell:confusion |
| **Menacing Aura** (Hollow Warden, Ranger) | 2024 (Ravenloft: The Horrors Within) | **Ranger nível 11** | "When a creature fails its saving throw against your Unnerving Aura, it also can't regain Hit Points or **take Reactions** until the start of your next turn." | http://dnd2024.wikidot.com/ranger:hollow-warden |
| **Incapacitated** (condição) | 2014 | condição-base | "An incapacitated creature **can't take actions or reactions**." | https://5thsrd.org/rules/conditions/ |
| **Incapacitated** (condição) | **2024** | condição-base (as outras referenciam ela) | "While you have the Incapacitated condition, you experience the following effects. ***Inactive.*** You **can't take any action, Bonus Action, or Reaction**. ***No Concentration.*** Your Concentration is broken. ***Speechless.*** You can't speak. ***Surprised.*** If you're Incapacitated when you roll Initiative, you have Disadvantage on the roll." | https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary |
| **Stunned** | 2014 / 2024 | condição derivada | 2014: "A stunned creature is incapacitated (see the condition), can't move, and can speak only falteringly." · 2024: "***Incapacitated.*** You have the Incapacitated condition." | https://5thsrd.org/rules/conditions/ · https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary |
| **Paralyzed** | 2014 / 2024 | condição derivada | 2014: "A paralyzed creature is incapacitated (see the condition) and can't move or speak." · 2024: "***Incapacitated.*** You have the Incapacitated condition." | mesmas URLs acima |
| **Unconscious** | 2014 / 2024 | condição derivada | 2014: "An unconscious creature is incapacitated (see the condition), can't move or speak, and is unaware of its surroundings." · 2024: "***Inert.*** You have the Incapacitated and Prone conditions." | mesmas URLs acima |
| **Surpresa** | 2014 | regra de combate | "If you're surprised, you can't move or take an action on your first turn of the combat, and **you can't take a reaction until that turn ends**." | https://www.dndbeyond.com/sources/dnd/basic-rules-2014/combat |
| **Tasha's Hideous Laughter** | 2024 | **Magia de 1º nível** (→ Incapacitated) | "On a failed save, it has the **Prone and Incapacitated** conditions for the duration." | http://dnd2024.wikidot.com/spell:tasha-s-hideous-laughter |
| **Hold Person** | 2024 | **Magia de 2º nível** (→ Paralyzed → Incapacitated) | "The target must succeed on a Wisdom saving throw or have the **Paralyzed** condition for the duration." | http://dnd2024.wikidot.com/spell:hold-person |
| **Hypnotic Pattern** | 2014 | **Magia de 3º nível** (→ Incapacitated) | "While charmed by this spell, the creature is **incapacitated** and has a speed of 0." | https://api.open5e.com/v1/spells/hypnotic-pattern/ |
| **Stunning Strike** | 2024 | **Monge nível 5**, 1 Focus Point, 1×/turno | "On a failed save, the target has the **Stunned** condition until the start of your next turn. On a successful save, the target's Speed is halved until the start of your next turn, and the next attack roll made against the target before then has Advantage." | http://dnd2024.wikidot.com/monk |
| **Hold Monster** | 2014 | **Magia de 5º nível** (→ Paralyzed) | "The target must make a saving throw of Wisdom or be **paralyzed** for the duration of the spell." | https://api.open5e.com/v1/spells/hold-monster/ |
| **Power Word Stun** | 2014 | **Magia de 8º nível** (→ Stunned, só ≤150 PV) | "If the target has 150 hit points or fewer, it is **stunned**. Otherwise, the spell has no effect." | https://api.open5e.com/v1/spells/power-word-stun/ |
| **Dazed** (contraste 4e) | 4e (PHB p.277, Rules Compendium p.229) | condição — aplicada já por poder de **encontro de nível 1** | "The creature doesn't get its normal complement of actions on its turn; it can take either a standard, a move, or a minor action. The creature can still take free actions. The creature **can't take immediate actions or opportunity actions**. The creature grants combat advantage. The creature can't flank." | https://www.dyasdesigns.com/dnd4e/static-site/glossary/glossary133-dazed.html |
| **Chill Strike** (4e, Mago) | 4e (PHB p.159) | **poder de encontro, nível 1** | "2d8 + Intelligence modifier cold damage, and the target is dazed until the end of your next turn." — `NÃO CONFIRMADO` (só resumo de busca; a página `dnd4.fandom.com/wiki/Chill_strike` não foi lida na íntegra) | https://dnd4.fandom.com/wiki/Chill_strike |

### Definição de Reação (2024), pra saber o que exatamente se perde
> "A Reaction is a special action taken in response to a trigger defined in the Reaction's description. You can take a Reaction on another creature's turn, and if you take it on your turn, you can do so even if you also take an action, a Bonus Action, or both. Once you take a Reaction, you can't take another one until the start of your next turn."
> — https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary

E o Ataque de Oportunidade **é** uma Reação (por isso "negar só AdO" é estritamente mais fraco que "negar Reação"):
> "To make the Opportunity Attack, **take a Reaction** to make one melee attack with a weapon or an Unarmed Strike against the provoking creature."
> — mesma URL

### O achado de preço mais importante: a nerfada de 2024
Comparando as duas colunas da tabela, a WotC **rebaixou** negação de Reação exatamente nos dois lugares onde ela era mais barata:

| | 2014 | 2024 |
|---|---|---|
| Shocking Grasp (truque) | nega **toda** Reação | nega **só Ataque de Oportunidade** |
| Open Hand / Addle (monge 3) | nega **toda** Reação | nega **só Ataque de Oportunidade** |
| Arms of Hadar (magia 1) | nega toda Reação | **nega toda Reação** (mantido) |
| Slow (magia 3) | nega toda Reação | **nega toda Reação** (mantido) |

Ou seja: em 2024 **não existe mais truque que negue Reação inteira**. O piso virou **magia de 1º nível** (Arms of Hadar, e aí AoE + salva Força + dano) ou **feature de classe de nível 2-3 com restrição de alvo** (Turn Undead, só mortos-vivos).

---

## 2. O que impede uma criatura de usar AÇÃO LENDÁRIA

**Existe regra geral, sim, nas duas edições — e é a mesma ideia: só `Incapacitated` (ou "incapaz de tomar ações") desliga.**

**2014 (SRD 5.1, Legendary Creatures):**
> "A legendary creature can take a certain number of special actions—called legendary actions—outside its turn. Only one legendary action option can be used at a time and only at the end of another creature's turn. A creature regains its spent legendary actions at the start of its turn. It can forgo using them, and **it can't use them while incapacitated or otherwise unable to take actions. If surprised, it can't use them until after its first turn in the combat.**"
> — https://5thsrd.org/gamemaster_rules/legendary_creatures/

**2024 (Basic Rules 2024, "How to Use a Monster"):**
> "A Legendary Action is an action that a monster can take immediately after another creature's turn."
> "**The monster can't take a Legendary Action if it has the Incapacitated condition or is otherwise unable to take actions.**"
> — https://www.dndbeyond.com/sources/dnd/br-2024/how-to-use-a-monster

**Mudou de 2014 pra 2024?** Só a redação. 2014 dizia "incapacitated or otherwise unable to take actions" + cláusula de surpresa; 2024 diz "has the Incapacitated condition or is otherwise unable to take actions" e **sumiu a cláusula de surpresa** (coerente: surpresa em 2024 virou desvantagem na iniciativa, e `Incapacitated` 2024 já embute "***Surprised.*** ...Disadvantage on the roll").

**Existe magia/habilidade de JOGADOR que tire especificamente a ação lendária?** **Não.** Nenhuma. A única porta é aplicar `Incapacitated` (ou uma condição que o contenha: Stunned, Paralyzed, Unconscious). Ou seja: o "preço" do D&D pra desligar a ação fora do turno do chefe **não é um efeito barato — é a condição mais caríssima do jogo**, o que na prática significa magia de 2º-5º nível com salva, concentração, e geralmente Legendary Resistance queimando ela.

**Consequência crítica pro seu design — "não pode usar Reação" ≠ "não pode usar Ação Lendária".** O texto de 2014 define ação lendária como "special actions... outside its turn" e a regra 2024 define Reação separadamente como resposta a um gatilho; são baldes diferentes. Logo o **Slow (3º nível) NÃO desliga ação lendária** — só Reação. Isso é consenso de fórum, não texto de regra explícito; marco como **derivado do texto** (as duas definições acima) e cito a discussão como secundária: https://www.dndbeyond.com/forums/dungeons-dragons-discussion/rules-game-mechanics/37925-how-does-the-slow-spell-effect-legendary-actions · https://www.enworld.org/threads/slow-vs-legendary-actions.688571/

---

## 3. Existe efeito de jogador que ataque o RECURSO do monstro?

**Resposta curta: NÃO. E em 2024 a WotC tirou ativamente o único caso que existia.** Isso é o achado mais útil do relatório.

### 3a. Espaço de magia — o D&D 2024 *removeu* o ataque ao recurso

**Counterspell 2014** (3º nível) queimava o espaço do inimigo, porque a magia falhava mas já tinha sido paga:
> "You attempt to interrupt a creature in the process of casting a spell. If the creature is casting a spell of 3rd level or lower, **its spell fails and has no effect.**"
> — https://api.open5e.com/v1/spells/counterspell/

**Counterspell 2024** (3º nível) mudou o endereço do dano: ele ataca a **AÇÃO**, e diz explicitamente que **NÃO** ataca o recurso:
> "On a failed save, the spell dissipates with no effect, and **the action, Bonus Action, or Reaction used to cast it is wasted. If that spell was cast with a spell slot, the slot isn't expended.**"
> — http://dnd2024.wikidot.com/spell:counterspell

Leia isso com atenção: a edição nova de D&D pegou o efeito mais famoso de "drenar recurso do inimigo" e **reescreveu ele como "drenar a ação do inimigo"**, com a frase literal de que o recurso fica intacto. É exatamente a mesma troca que você está fazendo na `Sobrecarga`.

### 3b. Monstro de 2024 não tem mais espaço de magia pra atacar
O MM 2024 abandonou espaço de magia em monstro e passou a usar **rótulo de frequência** — igual à decisão que você tomou. As notações oficiais são:
> "**Limited Usage — X/Day:** This notation means the stat block part can be used a certain number of times and that a monster must finish a Long Rest to regain expended uses."
> "**Limited Usage — Recharge X–Y:** This notation means a monster can use the stat block part once. At the start of each of the monster's turns, roll 1d6. If the roll is within the number range given in the notation, the monster regains the use of that part."
> — https://www.dndbeyond.com/sources/dnd/br-2024/how-to-use-a-monster

Confirmação secundária (não é texto de regra, é análise): "Spellcasting monsters no longer use spell slots; as of the 2024 materials, they have spells they can cast a certain number of times per day." — https://arcaneeye.com/mechanic-overview/how-spellcasting-monsters-work/

### 3c. Resistência Lendária — nada do lado do jogador
Texto do traço (2024 MM): "If the creature fails a saving throw, it can choose to succeed instead." — https://dnd-wiki.org/wiki/Creature_Trait_(5e24)/Legendary_Resistance (fonte terciária; **o texto oficial do MM 2024 não abriu em página pública** → marco o *wording* como `NÃO CONFIRMADO` em fonte primária, mas o conteúdo é pacífico).

**Procurei e não existe** nenhuma magia, feat, feature de classe ou item do jogador que: force gastar Resistência Lendária, reduza o número de usos, ou impeça recuperar. O que a comunidade discute são *houserules* (ex.: dar Exhaustion por uso), justamente porque o RAW não tem nada:
- https://www.hipstersanddragons.com/legendary-resistance-fixes-5e/
- https://tabletopbuilds.com/legendary-resistance/
- https://www.enworld.org/threads/a-better-model-for-legendary-resistance.705137/

A única "pressão" que o jogo admite é tática, não mecânica: forçar muitas salvas pra o chefe queimar os usos por conta própria.

### 3d. Recarga (`Recharge 5-6`) — nada, zero
**Não existe** efeito de jogador que trave, atrase ou force a rolagem de recarga. A recarga é rolada pelo monstro no começo do turno dele e nenhuma opção de PC toca nela. Fontes que descrevem a mecânica inteira sem nenhuma interação do jogador: https://www.dungeonsolvers.com/a-look-into-the-dd-5e-recharge-mechanic/ · https://grimpress.net/dissecting-dnd5e-reimagining-recharge/

### 3e. O que o D&D oferece no lugar (o "menu legítimo")
Tudo que o jogador tem contra o kit do monstro ataca **uso**, não **estoque**:
- **Counterspell** → gasta a ação (2024: e só a ação).
- **Silence / Antimagic Field / Dispel Magic** → impede ou desfaz o uso.
- **Incapacitated e família** → desliga ação, ação bônus, Reação e **ação lendária** de uma vez.
- **Slow / Mind Whip / Confusion** → racionam quantas ações saem por turno.

---

## 4. Bônus — como o 2024 preça `Incapacitated`

`Incapacitated` virou a **condição-base** que as outras importam (Stunned, Paralyzed, Unconscious todas dizem literalmente "You have the Incapacitated condition"). E **sim, ela nega Reação explicitamente** — em 2014 era "can't take actions or reactions"; em 2024 o texto ficou mais amplo:

> "***Inactive.*** You can't take any action, Bonus Action, or Reaction."
> — https://www.dndbeyond.com/sources/dnd/br-2024/rules-glossary

Preço dessa condição em 2024, pelo que eu achei:
- **1º nível:** Tasha's Hideous Laughter (1 alvo, concentração, salva Sab no fim de cada turno **e** a cada dano, com vantagem se foi dano).
- **2º nível:** Hold Person (só Humanoide, concentração, salva por turno) · Turn Undead (Clérigo 2, só mortos-vivos, quebra com qualquer dano).
- **3º nível:** Hypnotic Pattern (AoE, quebra com qualquer dano).
- **5º nível:** Monge — Stunning Strike (custa 1 Focus Point, 1×/turno, e dura só **até o início do seu próximo turno**).
- **8º nível:** Power Word Stun (e ainda com teto de 150 PV).

Padrão: `Incapacitated` **nunca** vem sem pelo menos duas travas (salva repetida + concentração, ou restrição de tipo de alvo, ou quebra com dano, ou duração de 1 rodada). É o oposto de barato.

---

## O que isto diz pro preço

1. **Negar Reação é barato, mas a edição nova decidiu que era barato demais:** em 2014 um **truque** (Shocking Grasp) e uma **feature de nível 3** (Open Hand) negavam Reação inteira, e em 2024 a WotC cortou as duas pra "só Ataque de Oportunidade" — deixando o piso de negação total de Reação em **magia de 1º nível** (Arms of Hadar) ou **feature de nível 2 com alvo restrito** (Turn Undead). Se a sua `Sobrecarga` é uma Melhoria comprável, "o alvo não pode usar Reação até o fim do próximo turno dele" cabe no preço de uma Melhoria barata e **tem precedente explícito em texto de regra oficial** — mas o preço honesto de 2024 seria ou durar só até o início do próximo turno do alvo, ou negar só a Reação ofensiva (tipo AdO), não toda.
2. **Cortar as ações por rodada é mais caro que negar Reação, mas não muito:** Tasha's Mind Whip vende o pacote completo que você quer — nega Reação **e** força o alvo a escolher entre mover, ação ou ação bônus — por **magia de 2º nível, salva de Inteligência, 1 rodada de duração e meio efeito se passar**. Esse é o molde mais próximo da sua `Sobrecarga` reescrita, e ele vem com três travas (salva, duração curtíssima, metade no sucesso).
3. **Travar a ação fora do turno (ação lendária) é o item mais caro da loja e não tem atalho:** nenhuma opção de jogador em nenhuma edição tira ação lendária diretamente; a única via é aplicar `Incapacitated`, e `Incapacitated` nunca é vendido sem duas ou três travas (concentração, salva repetida, quebra com dano, restrição de tipo). Se a sua `Sobrecarga` for mexer na ação especial fora do turno do inimigo, ela deixa de ser Melhoria barata e vira efeito de nível alto — ou então ela só **atrasa/rouba uma** dessas ações, não desliga a fonte.
4. **Atacar o recurso do inimigo não é um caminho que o D&D tenha aberto — é um caminho que ele fechou:** não existe nada que force Resistência Lendária, nada que impeça `Recarga 5-6`, e em 2024 o Counterspell foi reescrito pra dizer literalmente "the slot isn't expended", trocando dano-ao-recurso por dano-à-ação. Sua decisão de tirar o poço gastável do inimigo é a mesma decisão que a WotC tomou no MM 2024 (que virou `X/Day` e `Recharge X–Y`), então reescrever a `Sobrecarga` contra ação/Reação em vez de contra energia é seguir o rumo da edição mais nova, não se afastar dele.
5. **Conclusão de preço em uma linha:** negar Reação = tier truque/1º nível (barato, precedente sólido); negar Reação **+** racionar ações = tier 2º-3º nível com salva e duração de 1 rodada; tocar na ação fora do turno = tier `Incapacitated`, caro, só com várias travas.
