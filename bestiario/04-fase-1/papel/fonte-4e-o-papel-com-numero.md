# Fonte — o `papel` com número, e quem cobra por ele

*10/09/2026. Pesquisa feita inline, sem agente: três agentes morreram no limite de sessão sem salvar nada, e repetir o gesto era o erro que o `LEIA-ME` avisa.*

> **A pergunta:** o `papel` do inimigo **adiciona** ou **redistribui**? E algum sistema publicado **cobra** por ele?

---

## 1 · O D&D 4e inventou o papel, e publicou a troca COM NÚMERO

**Esta é a tabela do DMG, `Monster Statistics by Role`:**

| papel | PV no nível `0` | PV por nível | bônus de CA |
|---|---|---|---|
| `Skirmisher` | `24` | `+5` | — |
| `Controller` | `24` | `+5` | — |
| **`Soldier`** | `24` | `+5` | **`+2`** |
| **`Brute`** | **`26`** | **`+7`** | **`−2`** |
| **`Artillery`** | **`21`** | **`+3`** | **`−2`** |
| `Lurker` | `21` | `+3` | — |

*Fonte: tabela reproduzida em busca sobre `"monster statistics by role"`; o original é o DMG 4e, por volta da p. 184. **A página canônica do D&D4 Wiki (`dnd4.fandom.com/wiki/Monster_role`) devolveu `HTTP 402` e não abriu** — a tabela acima vem de reprodução de terceiro, então marco o *wording* do livro como `NÃO CONFIRMADO` em fonte primária. **Os números, porém, batem com a medição independente do item 1.1.***

### 1.1 E existe medição independente dos blocos publicados, que confirma a direção

**Médias medidas em cima dos blocos do `Monster Manual` de 4e, por papel** *(valor menos o nível)*:

| papel | `CA − nível` | `Fort − nível` | `Ref − nível` | `Von − nível` |
|---|---|---|---|---|
| **`Soldier`** | **`16,11`** | `14,57` | `11,82` | `11,72` |
| `Skirmisher` | `14,40` | `12,36` | `12,34` | `10,61` |
| `Controller` | `14,49` | `12,65` | `11,54` | `12,30` |
| `Lurker` | `14,18` | `11,32` | `12,68` | `10,66` |
| `Artillery` | `13,78` | `11,89` | `12,09` | `11,11` |
| **`Brute`** | **`12,77`** | `13,63` | `10,22` | `10,06` |

*Fonte: thread `Lots of statistics from the Monster Manual`, EN World — https://www.enworld.org/threads/lots-of-statistics-from-the-monster-manual.229092/*

> **A medição reproduz a tabela:** `Soldier` no topo da CA, `Brute` no fundo, `3,34` pontos de
> distância entre os dois. **E o `Brute` compensa na Fortitude** (`13,63` contra `10,22` de Reflexos),
> que é o eixo do corpo a corpo.

---

## 2 · ⚠ A resposta que decide: **o 4e NÃO COBRA pelo papel**

> ### *"XP does not depend on monster 'class' (brute, soldier, lurker, etc.) — any creature of a particular level is worth the same XP as any other of the same level."*

**O XP de 4e é função do NÍVEL e do qualificador, e o papel não entra:**

| nível | `Standard` | `Elite` | `Solo` |
|---|---|---|---|
| `1` | `100` | `200` | `500` |
| `5` | `200` | `400` | `1.000` |
| `10` | `500` | `1.000` | `2.500` |

*E `Minion` vale `1/4`.* **`Elite` = `2×` porque ocupa o lugar de dois; `Solo` = `5×` porque ocupa o
lugar de cinco.**

*Fonte: threads `Monster XP Formula` e `Discussing 4e Subsystems: Elites, Solos, Minions, and Monster
XP`, EN World — https://www.enworld.org/threads/monster-xp-formula.220538/ ·
https://www.enworld.org/threads/discussing-4e-subsystems-elites-solos-minions-and-monster-xp.243712/*

> ### O 4e separa os dois eixos exatamente como a escada do Projeto-M separa.
> **O qualificador (`Minion` · `Elite` · `Solo`) é a `categoria` — e é ele que custa.**
> **O papel (`Brute` · `Artillery` · …) é o `papel` — e ele é de graça.**

---

## 3 · O Draw Steel faz o contrário, e isso derruba a premissa do arquivo do papel

**O `PAPEL-do-inimigo-base.md` cita o Draw Steel como precedente de *"redistribui, nunca adiciona"*. As fórmulas publicadas dizem o oposto.**

*Extraídas do livro em `01-pesquisa/dmg2024-e-draw-steel.md`, seção `Adjusting Monster Levels`:*

> `EV = ((2 × nível) + 4) × modificador de organização`
> `Stamina = ((10 × nível) + modificador de papel) × modificador de organização`
> `dano = (4 + nível + modificador de dano) × modificador de tier`

| papel | mod. de `Stamina` | mod. de dano |
|---|---|---|
| `Brute` | `+30` | `+1` |
| `Defender` | `+30` | `+0` |
| `Ambusher` | `+20` | `+1` |
| `Harrier` · `Mount` · `Support` | `+20` | `+0` |
| `Artillery` | `+10` | `+1` |
| `Controller` · `Hexer` | `+10` | `+0` |

> ### ⚠ O `EV` — que é o custo de encontro — **não lê o papel.**
> **Então um `Brute` e um `Artillery` de mesmo nível e mesma organização custam o mesmo `EV`, e o
> `Brute` leva `+20` de `Stamina` com o MESMO modificador de dano.**
> **Isso não é redistribuição: é bônus de graça, num eixo só.**

**A compensação do Draw Steel mora no TEXTO DA HABILIDADE — alcance, mobilidade, alvos —, não na
fórmula.** *E o próprio livro avisa que essas fórmulas existem **para entender** os blocos, não para
construir com elas.*

---

## 4 · E o Flee Mortals! — o antecessor do Draw Steel, em 5e — não publica número por papel

**`10` papéis**, e a definição de cada um é **tática e comportamental**:

| papel | o que o artigo diz |
|---|---|
| `Ambusher` | usa invisibilidade e furtividade pra ataque calculado |
| `Artillery` | combate à distância e fogo de cobertura |
| `Brute` | corpo a corpo forte com PV alto |
| `Controller` | debuff, charme, movimento forçado |
| `Leader` | blocos complexos, com villain actions |
| `Support` | fortalece aliados e chama reforço — mais simples que `Leader` |
| `Minion` · `Skirmisher` · `Soldier` · `Solo` | horda · corpo a corpo móvel · corpo a corpo de defesa alta · criatura única com lair/villain action |

> **O artigo oficial não diz que o papel muda CA, PV ou dano, e não fala de ND nem de custo de
> encontro.** *Ele trata papel como função tática.* **A frase dele: *"creature roles are simply an
> alternative to the core system"*.**

*Fonte: https://www.dndbeyond.com/posts/1729-creature-roles-how-flee-mortals-helps-you*

---

# O papel ADICIONA ou REDISTRIBUI? — sistema por sistema

| sistema | resposta | cobra? |
|---|---|---|
| **D&D 4e** | **REDISTRIBUI, e com número publicado.** `Brute` troca `2` de CA por `+2` PV/nível; `Artillery` troca `2` de PV/nível por alcance | **não cobra.** O XP é só nível + qualificador |
| **Draw Steel** | **ADICIONA.** O modificador de papel entra na `Stamina` e no dano, e o `EV` não lê nenhum dos dois | **não cobra** — e por isso o `Brute` é compra estritamente melhor que o `Artillery` |
| **Flee Mortals!** | **nem um nem outro: é etiqueta tática.** Nenhum número por papel | não cobra |

> ### A regra que o Mizuki escreveu — *"redistribui, nunca adiciona"* — é MAIS disciplinada que a do Draw Steel e é exatamente a do 4e.
> **O precedente existe, mas ele é o 4e, não o Draw Steel.** *E o 4e confirma a parte que importa: **o
> papel não cobra**, porque o custo já mora no outro eixo.*

---

## O que ficou `NÃO CONFIRMADO`

| item | por quê |
|---|---|
| o *wording* literal do DMG 4e na tabela `Monster Statistics by Role` | `dnd4.fandom.com` devolve **`HTTP 402`**; `forum.rpg.net` e `forums.giantitp.com` devolvem **`403`**. Os números vêm de reprodução de terceiro **e batem com a medição independente dos blocos** |
| **o dano por papel no 4e, com número** | achei só a descrição qualitativa — *"brutes deal big melee damage"*, *"artillery should be on the low side of damage for their CR or have a single ranged attack that deals a high amount"*. **A tabela numérica de dano por papel não abriu em fonte nenhuma** |
| a matemática do `MM3` / `Monster Vault` | o 4e repreçou PV e dano de monstro depois do DMG. **Não confirmei se as diferenças por papel sobreviveram** |
