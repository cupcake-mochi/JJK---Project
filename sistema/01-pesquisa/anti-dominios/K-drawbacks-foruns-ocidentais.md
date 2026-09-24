# K — Drawbacks e queda dos anti-domínios nos fóruns ocidentais (agente 3)

STATUS: EM ANDAMENTO

Recorte: o que a comunidade de língua inglesa (Reddit, Fandom, VS Battles, sites de notícia) diz sobre **drawbacks, weaknesses, how it breaks, how long it lasts** das quatro técnicas — Cesta Oca de Vime (彌虚葛籠, Hollow Wicker Basket), Domínio Simples (簡易領域, Simple Domain), Pétala (落花の情, Falling Blossom Emotion) e Extensão de Domínio (領域展延, Domain Amplification). Não repete o debate já coberto no `D`; foca em custo e queda.

Legenda: **[C]** canon do mangá (cap./pág.) · **[F]** oficial fora do mangá · **[I]** inferência/teoria, com quem afirma e link · **[NÃO ACHEI]** com onde procurei.

As seis respostas de "como cai": (1) pressão do domínio · (2) ataque ao usuário · (3) esgotamento · (4) largada · (5) condição ou voto · (6) o domínio acabou antes.

---

## 0 · Método e caminho (o que funcionou nesta rodada)

- **Reddit:** o `api.pullpush.io` que o `D` usou **morreu para nós nesta rodada** — toda chamada, espaçada ou não, devolveu `429 Rate limit exceeded ... does not provide free scraping resources for agents`. **O que funcionou foi o reserva, o `arctic-shift.photon-reddit.com`**, com três rotas:
  - `api/posts/search?subreddit=<sub>&title=<palavra>&limit=100` (busca por título — funciona bem com palavra, engasga com número como "266");
  - `api/posts/search?subreddit=<sub>&after=<data>&before=<data>&limit=100` (lista por janela de data — foi assim que achei os fios oficiais de discussão de capítulo do r/Jujutsushi);
  - `api/comments/tree?link_id=<id>&limit=9999` (a árvore inteira de comentários do fio, com score).
  - Devolve `422 Timeout. Maybe slow down a bit` se apertar: esperar 30–60 s resolve.
- **Score:** diferente do PullPush do `D`, o Arctic Shift re-raspa o comentário depois (`retrieved_2nd_on`), então o score aqui **é um retrato mais tardio e vale como medida de concordância** — mas continua sendo retrato, não o valor de hoje. Eu cito o score entre colchetes: `[+306]`.
- **O sub que importa é o r/Jujutsushi** (o sub de mangá; tem fio oficial "Chapter N Links + Discussion" e fio de vazamento por capítulo). É onde a leitura do capítulo acontece na semana em que ele sai.
- **Fandom:** `api.php?action=parse&page=<Página>&prop=wikitext` nos quatro artigos, nas páginas de capítulo (85, 108, 109, 187, 226, 227, 232, 246, 247, 249, 266, 267) e em `Talk:Hajime_Kashimo`. Aba Discussões pela `wikia.php`.
- **Aviso de fonte:** tudo marcado **[I]** abaixo é leitura de fã. Quando o fã aponta **painel**, eu digo qual; quando é teoria, eu digo que é teoria.

---

## 1 · CESTA OCA DE VIME (Hollow Wicker Basket, 彌虚葛籠)

### 1.1 O drawback que o ocidente enxerga

**O consenso é um só, e é custo de mão, não de energia.** Mas o fio que mais importa (r/Jujutsushi `1b12ry0`, *"What is the point of Hollow Wicker Basket?"*, 27/02/2024, post com **+491** e 164 comentários) mostra que antes do cap. 266 o ocidente **nem sabia se o selo tinha que ser mantido**:

- OP: *"If you have to keep your hands in a sign..... Wouldn't you just be standing there until your opponent just charges and kills you? ... HWB seems useless to everyone not named Sukuna due to his four arms. Unless he is only keeping the Handsigns up to strengthen it?"* — a pergunta que o cap. 266 respondeu seis meses depois.
- **u/escaflow [+464]** (a mais votada): *"Maybe a perseverance battle? Enduring the sure hit until one of them runs out of CE"* — **teoria** de queda por (3) esgotamento de um dos dois. Sem painel.
- **u/Abdul-Wahab6 [+138]**, resposta direta: *"while you're enduring said surehit your opponent (barrier caster) isn't suffering same fate and can just come around to whoop your ass or **free your hands and the sure-hit just hits you**."* — **teoria** de queda por (2) ataque ao usuário, via as mãos. **Foi exatamente o que a obra fez depois** (Rika segurando braços no 251; socos do Yuji no 266).
- **u/Natsu_Happy_END02 [+296]**: *"the idea is to stall till the Domain falls down. And I kinda have the impression that it doesn't get destroyed by strong domains like SD so it can very much be permanently active."* — **teoria** de (6) o domínio acaba antes. ⚠ A parte *"não é destruída por domínio forte"* foi **desmentida pelo próprio cap. 266** (narração: Cesta e Domínio Simples têm saída fraca e só compram tempo).
- **u/andii74 [+41]**: *"HWB trades a user's combat ability (due to the hand sign) in a **binding vow** to push the durability far past what SD is capable of."* — **teoria**. Não há voto nenhum associado à Cesta na obra (ver `A`). É a mesma hipótese que o `D` §7.2 registrou do u/SaIamiShadow.

**Um drawback de 2026 que ninguém tinha escrito tão claro** — r/Jujutsufolk `1vxhbsd`, *"If you're not True Form Sukuna, Hollow Wicker Basket is absolute trash"*, 24/08/2026:
- **u/AndrewEophis [+5]**: *"Your anti-domain tech, even when you are focusing on it and nothing else, no reinforcement, no CT use, no RCT, is going to lose to a domain of a comparable opponent."* — **teoria de escala**, mas ela resume a narração do 266.
- **u/stopcopium [+1]**: *"even if it allows you to move, you still have to hold the handsigns up to reinforce it or it'll still let some of the surehit through."* — ⚠ **"deixa passar um pouco" não tem painel.** A obra fala em *ser sobrepujada* (`押し負ける`), não em vazar.
- **u/dahfer25 [+3]**: *"SD doesnt let you move, and HWB doesnt let you use your hands."* — o par de custos que o ocidente repete, e que o `H` já corrigiu (o "não move" do Domínio Simples é o voto da Miwa).

### 1.2 Selo mantido: obrigatório ou reforço? — **o ocidente leu o 266 como "reforço", e bem**

Na semana do 266, o fio oficial de vazamento do r/Jujutsushi (`1esjflu`, 15–18/08/2024, 646 comentários) virou a chave:

- **u/BodybuilderThis7045 [+20]**: *"Finally confirmation that **HWB doesn't require constant handsigns, but that it just bolsters it**. This is in line with some evidence — someone pointed out that **receipt guy's HWB was still up after letting down the handsigns** ... Of course, it's still a temporary measure for most — **it'll break down eventually even under ideal conditions**."* ("receipt guy" = Reggie Star.)
- **u/evan_the_babe [+16]**: *"hwb doesn't drop immediately if he stops using the hand signs, the signs just make it stronger and longer lasting, it's explained in this chapter."*
- **u/Salt-Punch [+14]**: *"Hollow Wicker Basket persists after you make the handsign. Sukuna just continues the handsigns to strengthen/keep revitalizing it."*
- Contra, e **negativado**: **u/andy_arc [−6]**: *"Holding the sign doesn't increase the output ... All it does is lower the cursed energy output required for HWB."* A comunidade rejeitou.
- No fio r/Jujutsufolk `1hpp3bm` (30/12/2024), *"Can someone break hollow wicker basket by stopping the hand signs of the user"*: **u/Jolyne_Best_JoJo [+3]**: *"It'll get overpowered quicker, but it wouldn't make hwb immediately disperse since 266 specifies keeping the handsign up after activation helps with the low output."*

**O que isso vale:** a leitura ocidental majoritária bate com o texto japonês que o `H` corrigiu (`発動後も掌印を結んだままにすることで出力を補い` — *"mantendo o selo mesmo depois de ativar, suplementa a saída"*). **A frase japonesa "mesmo depois de ativar" já implica que manter é opcional**, e o ocidente chegou nisso sozinho. **[C]** cap. 266 (texto) + **[I]** leitura "o selo é reforço, não interruptor" [+20/+16/+14].

**⚠ A prova do Reggie é painel alegado, não conferido por mim.** Três pessoas diferentes afirmam a mesma cena do cap. 171: **u/tomtadpole [+21]** (*"we saw it persist after Reggie unclasped his hands when he realised Megumi's domain was incomplete"*), **u/rahonan [+20]** (*"Reggie activates the sign, and then removes them, but HWB stays up"*), e o u/BodybuilderThis7045 acima. **[I] com painel apontado (cap. 171)**; o `I` registra que o 171 não mostra a Cesta caindo — as duas coisas batem: **ela fica de pé sem o selo e a obra não mostra quando some.**

**Uma afirmação de tempo sem painel:** **u/MrChainsawHog [+1]** (`1hpp3bm`): *"Sukuna ... could only maintain HWB for a couple of seconds against yuta without maintaining hand sign."* **[I] sem painel.** O `I` (cap. 251) diz que ao soltar o selo ele fica *"sem conseguir manter a Cesta"* (`「彌虚葛籠」が維持できていない`) e toma a Escada de Jacó — ou seja, "alguns segundos" é o fã preenchendo o tempo que a obra não dá.

### 1.3 O buraco do cap. 266 → 267, pelo lado ocidental

**A leitura ocidental da semana foi "o Yuji está quebrando a Cesta", e a comunidade viu a rachadura no painel.**

Fio oficial do 266 (r/Jujutsushi `1evbavp`, 18/08/2024) e de vazamento (`1esjflu`):
- **u/Johnnygoodguy [+79]**: *"Sukuna trying to retreat while Yuji **breaks down HWB** like a slasher villain trying to get through a door."*
- **u/Alder_Godric [+21]**: *"Sukuna is maintaining Hollow Wicker Basket for now so the domain can't affect him. Though **it started to break down** over the course of the chapter."*
- **u/tutubabarao [+4]**: *"in their clash of punches Sukuna's hollow basket **appears broken in the top left corner**"* — **painel apontado**, e é o mesmo que o `I` achou nos resumos japoneses (`一部割れてしまう描写`, *"desenhada rachando em um pedaço"*).
- **u/MadeJustToReply12 [+8]**, respondendo *"yuji's punches can break hollow wicker basket?"*: ***"Indirectly.*** *Yuji's attacks weakens Sukuna's output and control over Megumi's body."* — **esta é a leitura de mecanismo mais útil que achei**: o soco não racha a Cesta por contato; ele **derruba a saída do dono**, e a Cesta, que já é de saída fraca, perde a corrida. **[I]**, mas coerente com o texto japonês do 266 (o soco de alma que a reversa não cura).

A frase inglesa que circula para o pensamento do Sukuna: *"My Reverse Cursed Technique is pointless against the brat's attack! **Hollow Wicker Basket is going to fall apart!**"* — **"is going to"**, futuro, igual ao japonês `解ける` que o `I` levantou. **A tradução em inglês não inventou a queda**; quem arredondou para "destruída" foi o resumo.

**Onde o ocidente discordou (e é o mesmo ponto que o `I` deixou fora de quadro):**
- **u/Traditional-Heat2782 [+7]** (`1esjflu`): *"I don't get why sukuna wasn't immediately hit with yuji's sure hit as soon as he **stopped HWB to use domain**."* — lê que ele **soltou**.
- **u/andii74 [−13]**: *"cop out from Gege how Sukuna managed to cast his domain when **HWB broke down** without being hit"* — lê que ela **quebrou**. Negativado.
- **u/ruminaui [+1]**: *"I just reread the chapter, **he hasn't dropped the Hollow Wicker basket, two of his hands are still making the sign**."* — lê que ela **continuava**.
- No vazamento do 267 (r/Jujutsushi `1ey7oni`, 22/08/2024, 2.602 comentários): **u/luceafaruI [+7]**: *"this chapter proved that **you cannot do two handsigns at once**. To open malevolent shrine, sukuna **has undid the hwb handsign** even though he didn't need the extra hands."* — e ele mesmo, logo abaixo, se contradiz: *"Hwb was most likely still active and it will probably break after the black flash."* **u/No_Nefariousness3849 [+6]**: *"HWB is no longer active."* **u/MusterBait [+3]**: *"after getting hit with resonance and **releasing his HWB**"*.
- Fio oficial do 267 (`1f0ybf2`, 25/08/2024): **u/Chemical_Reason_2043 [+36]**: *"Yuji more than proved last week he can beat Sukuna hand-to-hand and **destroy HWB**."* **u/FatalWarrior [+1]**: *"HWB, which was only just about lasting as it was"*.

**Veredito do lado ocidental:** o ocidente **também não fechou** se ela caiu sozinha ou se ele soltou. A maioria votada leu "quebrando" no 266 (+79, +21) e "destruída" no 267 (+36), mas **ninguém aponta o painel da Cesta se desfazendo** — os que olham o painel falam em **rachadura** (+4) ou em **selo desfeito para o domínio** (+7). **Isso confirma o veredito do `I`: causa (2) ataque ao usuário, com o último instante — (1)/(2) terminando ou (4) largada para o selo do domínio — fora de quadro.** **[I]**, scores acima.

**E a teoria do "um selo de cada vez"** (u/luceafaruI [+7]): *não dá para manter dois selos de mão ao mesmo tempo*, por isso ele largou a Cesta no 251 (para o Desmantelar que corta o mundo) e no 267 (para o domínio). **[I]** sem texto da obra que diga isso; é inferência de duas cenas. Vale como hipótese, não como regra.

### 1.4 A boca (cap. 249) — o ocidente tem DUAS respostas, nenhuma com texto

A frase japonesa é `腕と口の半分を封じ` (*"selando metade dos braços e da boca"*) e **não fala em encantamento**. O ocidente preencheu de dois jeitos:

**Leitura A — "a Cesta exige cantar":**
- **A página `Chapter 249` da Fandom** escreve hoje: *"forcing him to constantly neutralize the sure-hit effect using Hollow Wicker Basket, thus occupying half of his arms and mouths **to form the hand signs and chant the incantations**."* **[I] da wiki** — o artigo da própria técnica (`Hollow_Wicker_Basket`) **não** fala em canto, só em *"half of his arms and mouths were occupied"*. Ou seja, a wiki se contradiz entre páginas.
- **u/darklordoft [+34]** (`1b12ry0`): *"wicker uses up your hand and **has you chanting**."*
- **u/xPapaGrim [+6]** (r/Jujutsushi, 20/02/2024): *"HWB requires both your hands **and mouth** to maintain it."*
- **u/hima657 [+14]**: *"or maybe Sukuna's own is built different and only lasted **because of constant chant**."*
- Homebrew que já transformou isso em regra: o sistema do `B` (*"You must also continuously chant to concentrate on this feat"*). **Isso vem desta leitura de fã.**

**Leitura B — "a boca está presa porque a Cesta tira dele o canto do Desmantelar que corta o mundo":**
- **u/handy303 [+2]** (r/Jujutsushi, 20/02/2024): *"Sukuna himself stated ... he **cannot cast World Slashing dismantle while having to cast Hollow wicker basket**. ... his bottom 2 arms and bottom mouth is busy casting Hollow Wicker Basket."*
- **u/pray4sex [+12]** (fio oficial do 249, `1aipr6b`): *"half his arms and mouths are occupied keeping yutas domains sure hit from hitting him ... so sukuna **can't use his strong dismantle, because he needs to use some hand signs and chants** to do so."*
- **u/Hworks [+10]** (fio do 251): a fala do Yuta no 251 é *"you need chants, handsigns, or both — and we won't let you do either!"*, enquanto ele **arranca a língua da boca da barriga** e corta a boca de cima.

**O que dá para afirmar:** as duas leituras ocidentais concordam que **a boca da barriga é a boca de canto do Sukuna**, e que a Cesta **a ocupa**. Nenhuma das duas mostra painel da boca da barriga **recitando algo para a Cesta**. **[NÃO ACHEI]** — em inglês — texto ou painel dizendo que a Cesta **tem** encantamento. Procurei: artigos `Hollow_Wicker_Basket` e `Chapter_249` da Fandom; fios oficiais dos caps. 249 e 250–251 no r/Jujutsushi; busca de comentários com "mouths" no r/Jujutsushi entre 31/01 e 25/02/2024 (Arctic Shift). **A frase "chant the incantations" da página do cap. 249 é o lugar de onde o homebrew tirou o "cantando" — e ela não tem painel próprio.**

### 1.5 Cap. 187 (Kashimo): ativou ou não — o ocidente se dividiu por causa da frase

- A frase inglesa, citada em `Talk:Hajime_Kashimo` na Fandom: *"The Domain apprised Kashimo of the rules of Idle Death Gamble **faster than he could give up on activating** Hollow Wicker Basket."* O editor da wiki concluiu só que *"he can use the anti domain technique"*. **[C] via tradução** — bate com o japonês do `I` (`発動を諦めるよりも速く`).
- A leitura ocidental **mais votada é outra, e está errada**: **u/insGpro [+110]** (`1b12ry0`): *"Kashimo **tried to cast HWB but was too slow**."* E **u/Whitehawk26 [+33]**: *"Info dump is less than 0.2 seconds and they have to be faster than that."* — **[ERRO]**: a frase fala em **desistir** mais devagar, não em **ativar** mais devagar. O "0,2 s" é número do Mahito (cap. 130) transplantado para o Hakari **[NÃO ACHEI]** número para o Hakari.
- **u/-Dartz- [+207]**: *"Its even worse against Hakari-type domains, he still gets the infinite CE shenanigans, the only thing you accomplish by using HWB against it is that you **waste CE** and look like a dumbass."* — é a única menção ocidental votada a **gasto de energia** da Cesta, e é **teoria**: a obra não diz que a Cesta gasta energia.
- **Resposta ao buraco:** a obra diz "desistir", e o ocidente, na média, lê "tentou e foi lento". **Para o Mizuki: a Cesta NÃO subiu no 187 (resposta 6-bis: nunca chegou a subir), e o que circula em inglês como "Kashimo foi lento demais" é erro de leitura.**

### 1.6 Custo de energia, tamanho, como se aprende — pelo lado ocidental

- **Energia:** **[NÃO ACHEI]** número ou painel. Só teoria: "perseverance battle... until one of them runs out of CE" [+464]; "you waste CE" [+207]; *"possible that HWB is cheaper/less taxing on the user"* (**u/Muted_Lurker2383 [+2]**, `1f0aghm`). Ninguém cita fonte.
- **Tamanho:** a wiki dá só *"Mid Range"* no infobox. **[NÃO ACHEI]** número em inglês.
- **Como se aprende:** o ocidente perguntou e não respondeu — r/Jujutsufolk `1qh8dpg`, *"How Does Kashimo Know Hollow Wicker Basket?"* (19/01/2026). A resposta que circula é histórica: r/Jujutsushi `vgmxf0` (20/06/2022, **+147**), *"Hollow Wicker Basket was apparently practiced for at least 600 years from the Heian era to 400 years ago"* — isto é: **era técnica comum de época**, sem escola. **[I]** inferência pelos três usuários (Sukuna, Heian; Kashimo e Reggie, 400 anos atrás). **[NÃO ACHEI]** cena de aprendizado.

### 1.7 Cesta Oca — como cai, cena por cena, no olho ocidental

| cena | queda (1–6) | o que o ocidente diz | marca |
|---|---|---|---|
| 171, Reggie | **incerto** | a Cesta fica de pé depois que ele solta o selo; ele apanha dos sapos e clones porque o domínio era incompleto | [I] +21/+20, painel apontado |
| 187, Kashimo | **nunca subiu** | "tentou e foi lento" [+110] é **erro**; a frase é "desistir de ativar" | [C] via tradução / [ERRO] do fórum |
| 249→251, Sukuna × Yuta | **(4) largada, forçada por (2)** | "Sukuna deactivated HWB for world cutting slash" (ver `D` §7.1); teoria do "um selo por vez" | [I] |
| 266→267, Sukuna × Yuji | **(2) ataque ao usuário**, fim fora de quadro | "breaks down HWB" [+79], rachadura no canto [+4], "Indirectly: weakens output" [+8]; soltou para o domínio [+7] × quebrou [+36] | [I] |
