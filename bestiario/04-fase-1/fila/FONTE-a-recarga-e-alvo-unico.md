# A `Recarga` é de área ou de alvo único? — a CONTAGEM

*10/09/2026. **Quatro contagens**, cada uma com script e saída nesta pasta:
`classificar-recarga-area.py` (D&D 5.2) · `classificar-va-drawsteel.py` (Draw Steel) ·
`classificar-recarga-pf2e.py` (PF2e) · `somar-os-tres-sistemas.py` (o total).
**Os dados crus estão em `dados-recarga-area/`, e os quatro scripts rodam de lá** — ver
`dados-recarga-area/COMO-RODAR.md`. Rodei os quatro dessa pasta antes de fechar: passam.*

***A dúvida dele, literal:*** *"E na recarga, ter colocado como alvo unico n acho tao interessante ser
em um alvo so. Tira o peso de poder mudar o combate, talvez ate mate o player de forma q n fique legal,
tanto q **raramente se tem acoes de recarga em sistema com qual e de alvo unico eu acho, bom
confirmar**"*

---

# ✅ CONFIRMADO. E a margem é grande.

> ## `70` de `86` rótulos de Recarga do SRD 5.2 são de ÁREA.
> **`12` são de alvo único. `4` não miram ninguém** (teleporte, buff, movimento).
>
> ### Tirando as `4` que não miram ninguém: **`70` de `82` = `85,4%` são área.**
> ### E no recorte que é o nosso — só a **AÇÃO** principal: **`64` de `72` = `88,9%`.**

*A intuição dele estava certa. Não "eu acho" — `85,4%`.*

---

## STATUS DA MEDIÇÃO

| passo | estado |
|---|---|
| **D&D 5e SRD 5.2** — área vs alvo único | ✅ **`70` de `86` são área** |
| D&D 5e SRD 5.1 (2014) — contra-prova | ⚠ **NÃO CONFIRMADO** — parse do open5e perdeu rótulos, ver §2 |
| **Draw Steel** — a `Villain Action` | ✅ **`119` de `156` pegam mais de um** |
| **Pathfinder 2e** — `1d4 rounds` | ✅ **`595` de `663` são área** *(aproximada)* |
| **O motivo de desenho publicado** | ✅ **achado** — `"Spread the Damage Around"`, Draw Steel |
| DMG 2024 · Daggerheart · Angry GM · Sly Flourish | ⚠ **NÃO CONFIRMADO**, ver §6 |

**MEDIÇÃO FECHADA.** *Os quatro passos do pedido foram medidos.*

> ⚠ **Os dois scripts exatos (D&D e Draw Steel) têm `assert` que ESTOURA se sobrar item sem
> classificação, ou se o rótulo que eu fiz à mão discordar do detector por palavra-chave.**
> *Rodei os dois: passam. O do PF2e não tem `assert` de propósito — a classificação lá é aproximada,
> e o §4 diz por quê.*

---

# 1. D&D 5e, SRD 5.2 — a contagem inteira

**Fonte:** `api.open5e.com/v2/creatures/?document__key=srd-2024` — `331` criaturas, varridas uma por uma.
`86` ações trazem `usage_limits` do tipo `RECHARGE` ou `RECHARGE_ON_ROLL`.

### ⚠ Nota de conferência com a medição anterior deste projeto

*A medição antiga dizia `83` rótulos, `67` deles `5-6`. Minha contagem dá **`86` rótulos**, e **`67`
deles `5-6`** — o `67` bate exato. A diferença de `3` está no total, não na janela. Fico com `86`,
que é o que a varredura conta; e registro que os dois números discordam.*

**A janela de recarga, contada:** `67` são `5-6` · `14` são `6` · `5` são `4-6`.

## A tabela

| classe | quantas | de | % | fonte |
|---|---|---|---|---|
| **ÁREA** — cone, linha, esfera, cilindro, emanação, "each creature in" | **`70`** | `86` | `81,4%` | open5e `srd-2024` |
| **ALVO ÚNICO** — "one creature", ataque contra um alvo | **`12`** | `86` | `14,0%` | idem |
| **SEM ALVO** — teleporte, buff em aliado, movimento | **`4`** | `86` | `4,7%` | idem |

### O recorte que importa pro Projeto-M

*A nossa `Recarga` é a **Ação** pesada — não a bônus, não a reação. Nesse recorte:*

| tipo de ação | n | área | alvo único | sem alvo | fonte |
|---|---|---|---|---|---|
| **`ACTION`** ← **é o nosso caso** | `72` | **`64`** | `8` | `0` | open5e `srd-2024` |
| `BONUS_ACTION` | `13` | `6` | `3` | `4` | idem |
| `REACTION` | `1` | `0` | `1` | `0` | idem |

> ### `64` de `72` — `88,9%`. Quando a Recarga é a AÇÃO do turno, ela é área.

---

# 2. As `12` exceções, uma por uma — e elas têm um padrão feio

| CR | monstro | ação | tipo | janela | dano | fonte |
|---|---|---|---|---|---|---|
| `13` | Vampire | `Charm` | bônus | `5-6` | **`0`** | open5e `srd-2024` |
| `11` | Roc | `Swoop` | bônus | `5-6` | **`0`** | idem |
| `7` | Stone Giant | `Deflect Missile` | **reação** | `5-6` | `11` | idem |
| `5` | Air Elemental | `Whirlwind` | ação | `4-6` | `24` | idem |
| `4` | Ghost | `Possession` | ação | `6` | **`0`** | idem |
| `4` | Incubus | `Nightmare` | bônus | `6` | `18` | idem |
| `3` | Minotaur of Baphomet | `Gore` | ação | `5-6` | `18` | idem |
| `2` | Ettercap | `Web Strand` | ação | `5-6` | **`0`** | idem |
| `2` | Sea Hag | `Death Glare` | ação | `5-6` | `13` | idem |
| `1` | Giant Spider | `Web` | ação | `5-6` | **`0`** | idem |
| `0,5` | Ape | `Rock` | ação | `6` | `10` | idem |
| `0,25` | Swarm of Ravens | `Cacophony` | ação | `6` | **`0`** | idem |

## O que essas `12` têm em comum — três coisas, e as três respondem a pergunta dele

### ⓵ São de monstro FRACO

| | CR médio | CR mediano | CR máximo |
|---|---|---|---|
| as de **ÁREA** | **`10,08`** | `8,50` | **`30`** *(Tarrasque)* |
| as de **ALVO ÚNICO** | **`4,40`** | `3,50` | **`13`** *(Vampire)* |

> **`CR 13` é o teto de uma Recarga de alvo único em todo o SRD 5.2.** *Acima disso, `0`.
> Todo monstro de `CR 14+` que tem Recarga, tem em ÁREA. Sem exceção.*

### ⓶ Metade não rola dano NENHUM

**`6` das `12` não têm dado de dano:** `Ettercap Web Strand` · `Ghost Possession` ·
`Giant Spider Web` · `Roc Swoop` · `Swarm of Ravens Cacophony` · `Vampire Charm`.

> *São condição e reposicionamento: `Restrained`, `Deafened`, `Charmed`, possessão, soltar um agarrado.*
> **Não são golpão. São truque.**

### ⓷ E as que causam dano são MINÚSCULAS

| | maior dano | quem |
|---|---|---|
| **Recarga de ALVO ÚNICO** | **`24`** | `Air Elemental` — `Whirlwind` |
| **Recarga de ÁREA** | **`91`** | `Ancient Red Dragon` — `Fire Breath` |

> ### `3,8×`. O maior golpe de Recarga de alvo único que o D&D 5.2 publicou dá `24`.
> **O D&D não usa alvo único pra golpão. Ele usa alvo único pra CONDIÇÃO em monstro de CR baixo.**

*Só uma das `12` chega perto de "matar o player de um golpe": a `Death Glare` da `Sea Hag`
(`CR 2`) — *"if the target has 20 Hit Points or fewer, it drops to 0 Hit Points"*. **E ela pede
que o alvo já esteja `Frightened` e já esteja com `20` PV ou menos** — ou seja, o design colocou
DUAS travas antes de deixar o efeito matar. E é `CR 2`, contra personagem de nível `1-3`.*

---

# ⚠ A contra-prova no SRD 5.1 (2014): **NÃO CONFIRMADO**

*Puxei as `325` criaturas do `srd-2014` também. Achei `47` rótulos de recarga e **todos os `47`
são área** — todos sopro, cone ou linha. Mas **não publico esse `47 de 47` como contagem.*

**Motivo:** o parse do open5e para o `srd-2014` **perdeu rótulos.** Conferi à mão: no SRD 5.1
impresso a `Giant Spider` tem `Web (Recharge 5-6)` e o `Gorgon` tem `Petrifying Breath (Recharge 5-6)`
— **nos dois o campo `usage_limits` vem vazio.** O parse só pegou sopro de dragão.

> **Então o `47` é piso, não total.** *A contagem do `2014` fica **NÃO CONFIRMADA**. A do `2024` é a
> que vale, e ela é confiável justamente porque **pegou** as de alvo único (`Giant Spider Web`,
> `Ettercap Web Strand`, `Ape Rock` estão todas lá).*

### E um `87º` rótulo que fica de fora da conta, de propósito

*`Cloaker` — `Phantasms (Recharge after a Short or Long Rest)`. É recarga por **descanso**, não por
dado, então é outro relógio. E é auto-buff (`Mirror Image` nele mesmo), não mira ninguém. Se você
quiser incluir: `87` rótulos, `70` área, `12` alvo único, `5` sem alvo.*

---

# 3. Draw Steel — a `Villain Action` é o equivalente, e aqui a margem é BRUTAL

**Qual é o equivalente?** *O Draw Steel não tem "recharge". Ele tem **`Villain Action`** — e é o
mesmo desenho: **a ação pesada que o vilão solta uma vez, no seu relógio próprio** (`Villain Action 1`
na rodada 1, `2` na rodada 2, `3` na rodada 3), e ela **substitui** a ação normal dele.*

*Não é o custo de `Malice`, não é `once per encounter` — é a `Villain Action`. Ela é literalmente
"a ação pesada da rodada", que é a definição da nossa `Recarga`.*

**Fonte:** `SteelCompendium/data-md`, tarball de `main`, `Bestiary/Monsters/**/Statblocks/*.md`.
Varri **todos** os statblocks. Cada `Villain Action` traz campo estruturado de alcance (`📏`) e de
alvo (`🎯`) — dá pra contar sem interpretar.

## A contagem

> ## `156` Villain Actions, em `52` criaturas.

| classe | quantas | de | % | fonte |
|---|---|---|---|---|
| **pega MAIS DE UMA criatura** | **`119`** | `156` | `76,3%` | `data-md` `main` |
| **pega EXATAMENTE UMA** | **`6`** | `156` | **`3,8%`** | idem |
| **não pega ninguém** *(self, invoca lacaio, cria objeto)* | `31` | `156` | `19,9%` | idem |

> ### Das que miram alguém: **`119` de `125` = `95,2%` pegam mais de um.**
> ### Alvo único: **`6` de `125` = `4,8%`.**

*As `17` de alvo `"Special"` eu resolvi **uma por uma**, lendo o `Effect` de cada — a resolução de
cada uma está escrita no dicionário `MAO` do script, com o motivo. O script **estoura** se sobrar
qualquer uma sem classe.*

## E agora o achado que responde a pergunta dele por completo

### ⓵ Nenhuma das `6` de alvo único rola dano

| criatura | Villain Action | alvo | o que ela faz de verdade | dano |
|---|---|---|---|---|
| `Chorogaunt` | `Bully the Weak` | **um ALIADO** | *mata o próprio lacaio* pra buffar os outros | `0` |
| `Radenwight Maestro` | `Solo Act` | uma criatura | **BUFF** — meio dano, `+4`, velocidade dobrada | `0` |
| `Devil High Judge` | `Deceptive Stratagem` | **um aliado/charmado** | troca de lugar, aliados ganham free strike | `0` |
| `Goblin Monarch` | `Focus Fire` | um inimigo | *"each ally… can move toward the target"* | `0` |
| `War Dog Ground Commander` | `Make an Example of Them` | um inimigo | *"each ally… can make a free strike against the target"* | `0` |
| `Bredbeddle` | `Challenge` | um inimigo | **o alvo ESCOLHE aceitar**, e rola o próprio teste | `0` |

*fonte de todas: `data-md/main`, os blocos estão citados na saída do script*

> ### `0` de `156`. **O Draw Steel não tem UMA villain action que concentre dano grande num alvo só.**

### ⓶ E as `3` que miram um herói não batem nele — elas MARCAM ele pros lacaios

*`Goblin Monarch`, `War Dog Ground Commander` e `Bredbeddle` apontam um herói. Mas o dano vem
**dos lacaios**, repartido em vários ataques separados — não de um golpe do vilão.*

### ⓷ E a única que pode MATAR num golpe pede a permissão do jogador

*`Bredbeddle` — `Challenge`. O `≤11` é *"The target is beheaded"*. **Mas:** *"**If the target accepts
the challenge**, the bredbeddle shifts adjacent to the target, who makes a **Might test**"*.
O jogador **escolhe entrar**, e **rola o próprio dado**.*

> **Isso é exatamente o medo dele — "talvez até mate o player de forma que não fique legal" — e o
> Draw Steel resolveu do único jeito que fica legal: o jogador aceita e rola.**

---

# 5. ⭐ O MOTIVO DE DESENHO — sim, alguém publicou. E tem seção com título próprio.

**Ele perguntou:** *"existe conselho publicado dizendo pra NÃO concentrar o golpão num personagem só?
A ideia de 'não mate um jogador com um golpe que ele não viu vindo' tem nome ou fonte?"*

## ✅ Tem nome. E o nome é do Draw Steel: **"Spread the Damage Around"**.

*É uma seção do capítulo `Monster Basics`, na lista de conselhos pro Director rodar combate.*

> ### `#### Spread the Damage Around`
> *"In an encounter with a lot of creatures, it's tempting to **focus fire on a single hero**. This can
> be a good tactical move, but **it's not always fun for the players**. Many heroes have triggered
> actions they can use when they take damage, so **spreading the damage around** can give those heroes
> a chance to do a cool thing off turn."*

*fonte: `data-md/main`, `Bestiary/Monsters/Chapters/Monster Basics.md`, linha `1254`*

> **Ele não só disse que não concentre — disse o MOTIVO mecânico:** *o jogador tem reação, e a reação
> só acontece se o dano chegar nele. Concentrar dano num só **desliga a reação dos outros quatro.***

### E a mesma página proíbe explicitamente concentrar duas Villain Actions no mesmo alvo

> *"…just pay attention to the rules about villain actions and **avoid having both solos focus fire on
> the same character at the same time**."*
>
> *mesma fonte, linha `689`*

## E a segunda metade da pergunta dele — "não mate um jogador com um golpe que ele não viu vindo"

### ✅ Também tem seção com nome, no mesmo capítulo: **"Play Nice—Even If You Don't Play Fair"**

> *"It might be tempting to keep a flying monster far out of reach of the heroes, or **popping that
> third villain action at the start of combat**, or causing rocks to fall from the sky every turn. But
> **the less the heroes can do about any specific situation, the less involved your players will
> feel** in the game. Use any tricks you can think of to make combat exciting and challenge the
> players, but **make sure that challenges can always be overcome**."*
>
> *mesma fonte, linha ~`1268`*

**Repara no exemplo que ele escolheu:** *"popping that third villain action at the start of combat"*.
**A `Villain Action 3` é a `ult`** — *"a showstopper that the villain can use to deal a devastating blow
to the heroes"* (linha `220`). **E soltar a ult sem aviso está na lista do que NÃO fazer.**

> ### Isso é literalmente a frase do Mizuki, publicada: o golpão precisa ser visto vindo.

## E o Draw Steel escreve a progressão das três, o que é o desenho de "ver vindo"

| | o que é | fonte |
|---|---|---|
| `Villain Action 1` | **opener** — *"shows the heroes they're not battling a typical creature… **They're a taste of what's to come**"* | `Monster Basics` linha `216` |
| `Villain Action 2` | **crowd control** — *"helps the villain regain the upper hand… **even more powerful than an opener**"* | linha `218` |
| `Villain Action 3` | **a `ult`** — *"a showstopper… **devastating blow**"* | linha `220` |

> **A escada é o aviso.** *A `1` é "prova do que vem". A `3` é o golpão. O jogador viu as duas
> primeiras antes de levar a terceira — e é por isso que a `3` pode ser devastadora.*

## Terceira fonte, e ela dá NÚMERO: o `Overkill Attack` do Giffyglyph's Monster Maker

**Nome do conceito lá: `Overkill Attack`** — *"a huge, devastating, and almost certainly fatal attack
that a monster can unleash against the party"*, valendo **`4×` o dano de um ataque normal**.

**E a trava que ele impõe é ESPACIAL, não numérica:**

> *"Overkill attacks automatically hit anything within a target area."*
> *"**Make sure that it's possible for your players (at least, most of them) to get out of range of the
> attack in only one turn** — even if it means dashing."*
>
> *fonte: https://www.giffyglyph.com/monstermaker/grimoire/2.1.2/en/overkill_attacks.html*

> ### Um golpe de `4×` é permitido — **desde que seja em ÁREA, e desde que dê pra sair dela.**
> **Alvo único não tem "sair da área". É aí que a trava desaparece — e é exatamente o que ele
> percebeu sozinho.**

---

# 4. Pathfinder 2e — a população existe, é ENORME, e dá o mesmo resultado

**Qual é o equivalente?** *Não é o `Frequency once per day`. É a frase idiomática do PF2e:*

> ### *"It can't use `<habilidade>` again for **1d4 rounds**."*

*É recarga por dado, igual ao `5-6` do D&D — só que o relógio é `1d4` rodadas em vez de `1d6` por
rodada. **É o mesmo desenho.***

**Fonte:** `Archives of Nethys`, `elasticsearch.aonprd.com`, `category=creature`.
**`677` criaturas** contêm a frase. Extraí **`696` habilidades**, que viram **`663`** depois de tirar
reimpressão (mesma criatura + mesma habilidade em dois livros).

## A contagem

| classe | quantas | de | % | fonte |
|---|---|---|---|---|
| **ÁREA** | **`595`** | `663` | `89,7%` | AoN `category=creature` |
| **ALVO ÚNICO** — total | **`34`** | `663` | `5,1%` | idem |
| ↳ *que é golpe num alvo* | `18` | `663` | `2,7%` | idem |
| ↳ *que é reação / auto-buff / aliado* | `16` | `663` | `2,4%` | idem |
| **não classificado** *(quase tudo reação e auto-buff)* | `34` | `663` | `5,1%` | idem |

> ### Das `629` que deu pra classificar: **`595` são área = `94,6%`.**

### ⚠ Aviso de qualidade, e ele é real

*O texto do AoN vem **concatenado** — o statblock inteiro num campo só, sem separar habilidade de
habilidade. Meu recorte do bloco é **aproximado** (janela entre marcadores de custo de ação). Conferi
as `34` de alvo único e as `34` sem classe **à mão**, e achei erro: o `Breath Weapon` do `Ravener`
(nv `21`) caiu em "alvo único" e é sopro — quase certamente área.*

> **Então o `94,6%` do PF2e é bom pra confirmar a tendência, e NÃO é preciso no dígito.**
> *Os números do D&D 5.2 e do Draw Steel são precisos; este é aproximado. **Não use este pra calibrar
> nada** — use pra confirmar a direção.*

## ⭐ Mas o PF2e entrega uma coisa que os outros dois não entregam: o CONTRA-EXEMPLO, e ele vem com a solução

*O PF2e **tem** um golpão de recarga em alvo único que mata. Dois, na verdade — e são gêmeos:*

| | `Norn` — `Snip Thread` | `Tatterthread` — `Shadow Snip` |
|---|---|---|
| nível | `20` | `20` |
| alvo | **uma criatura** em `100` pés | **uma criatura** em `100` pés |
| dano | **`100`** void | **`100`** acid |
| se cair a `0` PV | *"the creature **dies immediately**"* | *"it melts… and **dies immediately**"* |
| e fica morto | *"can't be restored to life except by a **wish** ritual"* | *idem, `miracle`/`wish`* |

*fonte de ambos: AoN, `category=creature`*

### E agora repara nas TRÊS travas que o PF2e pôs em cima disso

| trava | o texto |
|---|---|
| ⓵ **usos por dia** | *"**Frequency three times per day**"* |
| ⓶ **recarga** | *"The norn **can't use Snip Thread again for 1d4 rounds**"* |
| ⓷ ⭐ **imunidade por alvo** | *"**Regardless of the outcome of their saving throw**, a creature targeted by Snip Thread then becomes **temporarily immune for 24 hours**"* |

> ## A trava ⓷ é a resposta de desenho, e ela é linda.
> **O PF2e deixa existir o golpe de recarga que mata um jogador só — mas ele NÃO PODE MIRAR O MESMO
> JOGADOR DUAS VEZES.** *Errou o save ou acertou, tanto faz: aquele personagem fica imune por `24h`.*
>
> ### Isso é "spread the damage around" **escrito como regra**, não como conselho.
> *Se o golpe é de alvo único, o sistema te obriga a espalhar ele pela mesa.*

**E é nível `20`** — o topo do jogo, onde o personagem tem PV pra sobreviver a `100` de dano num save
bem-sucedido.

---

# 6. Onde eu procurei e NÃO achei — dito com todas as letras

| onde | procurei o quê | resultado |
|---|---|---|
| **DMG 2024** (capítulo de combate / criar monstro) | conselho de espalhar dano, de não focar um personagem | **NÃO CONFIRMADO** — varri resenhas detalhadas, o resumo do Sly Flourish das seções notáveis, o compêndio do Roll20 e o fórum EN World. O que o DMG `2024` diz é sobre **dificuldade de encontro** (*"high-difficulty encounters could be lethal for one or more characters"*), **não** sobre em quem bater. Se está no livro impresso, não achei em fonte aberta. |
| **Daggerheart** | conselho de espalhar dano / avisar antes do golpão | **NÃO CONFIRMADO** — `daggerheart.org/gm/gm-guidance` devolve `403`. Abri o SRD (`daggerheartsrd.com`, `core-gm-mechanics`) e **não tem** conselho de mirar/espalhar. O que existe é o mecanismo — `Group Attack` gasta `Fear` pra atacar vários, e o `spotlight` deixa o GM variar em quem bate — **mas o texto não escreve o conselho.** |
| **The Angry GM** | conselho específico sobre alvo único do golpão | **NÃO CONFIRMADO** — a série de `boss fight` fala de `nova` e de fases, e critica a experiência de "usar a nova no alvo errado", mas do lado do **jogador**, não do monstro. Não achei a frase que ele pediu. |
| **Sly Flourish** / `alphastream.org` | idem | **NÃO CONFIRMADO** — abri o `alphastream.org` (*"How to Challenge Players? Just Add Damage!"*, que já tinha funcionado neste projeto). Ele fala de **aumentar dano total** com dado a mais, e **não** de como repartir esse dano. |

> **Então: o conselho publicado que ele procurava existe, mas está no `Draw Steel` e no
> `Giffyglyph's Monster Maker` — não no D&D oficial nem no Daggerheart.**

---

# 7. O quadro, os três sistemas juntos

*conta em `somar-os-tres-sistemas.py`, saída em `SAIDA-total-tres-sistemas.txt`*

| sistema | o que conta como "recarga" | total | **área** | **alvo único** | sem alvo | **% área** | precisão | fonte |
|---|---|---|---|---|---|---|---|---|
| **D&D 5e SRD 5.2** | `usage_limits` `RECHARGE` / `RECHARGE_ON_ROLL` | `86` | **`70`** | **`12`** | `4` | **`85,4%`** | exata | open5e `srd-2024` |
| **Draw Steel** | `Villain Action 1/2/3` | `156` | **`119`** | **`6`** | `31` | **`95,2%`** | exata | `SteelCompendium/data-md` `main` |
| **Pathfinder 2e** | *"can't use X again for 1d4 rounds"* | `663` | **`595`** | **`34`** | `34` | **`94,6%`** | aproximada | AoN `elasticsearch` |
| **TOTAL** | | **`905`** | **`784`** | **`52`** | `69` | **`93,8%`** | | |

*`% área` é sobre as que miram alguém (área + alvo único), sem contar as que não miram ninguém.*

> ## `784` de `836` = `93,8%`.
> ## **`1` em cada `16` ações de recarga é de alvo único.**

---

# ✅ A resposta pro Mizuki

**Você tá certo, e não é por pouco: de `836` ações de recarga que miram alguém, em três sistemas, `784` são em ÁREA — `93,8%`. Alvo único é `1` em cada `16`.**

**E as poucas de alvo único não são golpão: no D&D `5.2` o teto de dano de uma recarga em alvo único é `24` (contra `91` em área), `6` das `12` não rolam dano nenhum, e nenhum monstro de `CR 14+` tem recarga de alvo único. No Draw Steel são `6` de `156` e NENHUMA causa dano — elas marcam o herói pros lacaios baterem.**

**O motivo publicado existe e tem título de seção: `"Spread the Damage Around"`, no `Monster Basics` do Draw Steel — *"it's tempting to focus fire on a single hero… it's not always fun for the players"*, e o motivo mecânico é que dano concentrado desliga a reação dos outros jogadores.**

**E a sua outra frase — "que não mate o player de forma que não fique legal" — também tem seção: `"Play Nice—Even If You Don't Play Fair"`, que lista *"popping that third villain action at the start of combat"* como o que NÃO fazer, porque *"the less the heroes can do about any specific situation, the less involved your players will feel"*.**

**Quando um sistema deixa a recarga de alvo único matar (o `Snip Thread` da `Norn` no PF2e, `100` de dano e morte permanente), ele trava por regra: `3×` por dia, recarga `1d4`, e — o pulo do gato — o alvo fica **imune por `24h`**, ou seja, o golpe não pode mirar o mesmo jogador duas vezes.**
