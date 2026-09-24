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

### 1.8 Adendo à Cesta: a peça que liga a boca ao Desmantelar (achada depois do 1.4)

A página `Chapter_255` da Fandom resume o cap. 255 assim: *"Originally, in order to expand Dismantle's target and unleash a slash capable of cutting the world, Sukuna needed only to form the **Enmaten** hand signs — the same used to activate Malevolent Shrine. However, after Gojo's unlimited Hollow Technique: Purple destroyed half of Sukuna's arms, he was rendered incapable of performing the technique. To compensate, Sukuna imposed a binding vow on the world-cutting Dismantle, **adding incantations** and requiring him to guide the slash with his hand."* **[C] via resumo da wiki**, cap. 255 — conferir no japonês.

**O que isso faz com o buraco da boca:** dá base de texto para a **Leitura B** do 1.4. Se o Desmantelar que corta o mundo passou a exigir **encantamento** (voto do cap. 255), então "selar metade dos braços **e da boca**" no 249 é o Sukuna dizendo que a Cesta **tira dele as peças do golpe grande** (o selo e a boca de canto). **Não prova que a Cesta tem encantamento** — prova que a boca é a moeda do Desmantelar. Continua **[NÃO ACHEI]** painel da Cesta sendo recitada. **[I]**, minha costura de duas fontes.

⚠ **Correção de fonte ao 1.3:** a frase inglesa *"Hollow Wicker Basket is going to fall apart!"* chegou a mim por trecho de buscador sobre o cap. 266; **não identifiquei se é da Viz ou da TCB**, e a busca da wiki não a encontrou. Vale como "circula em inglês", não como tradução oficial.

---

## 2 · DOMÍNIO SIMPLES (Simple Domain, 簡易領域)

### 2.1 O drawback que o ocidente enxerga

Dois custos dominam, e os dois já estão no `H`: **pode ser arrancado** e **"não pode sair do lugar"**. O que os fóruns acrescentam é **como** ele cai, com o painel na mão.

**Erro que continua vivo em 2026, agora fora da wiki:**
- **Aniviewer** (guia de 07/01/2026, sem autor): *"Both of her feet must often remain planted"* e trata o pé plantado como regra de iniciante (*"training wheel"*). **Fonte fraca**, mas aqui ela acerta a atribuição.
- **u/dahfer25 [+8]** (r/Jujutsufolk `1vxhbsd`, 24/08/2026): *"The one that doesn't allow you to move is simple domain, where you have to mantain the posture or it becomes like a hwb without handsigns, aka, **it gets destroyed in seconds**."* — **teoria**: "mover = cai em segundos" não tem painel; o painel do 206 mostra o contrário (ver 2.2).
- **u/KrispyKingTheProphet [−1]** e **u/stopcopium [+1]** no mesmo fio corrigem: *"SD can move, it's based on skill level. Miwa can't move, but Gojo and Kusakabe can move."* A correção existe e está **menos votada** que o erro.

### 2.2 Como ele cai — o que o ocidente leu nos painéis

**Cap. 206 (Yuki × Kenjaku) — o painel que derrubou o "não move":** r/Jujutsushi `zhvp9n` (10/12/2022, post **+189**): *"in chapter 206, Yuki used SD to defend against Kenny's DE and **she can run towards him to attack**; but her SD is still activated (though **it's slowly getting destroyed** by Kenny's DE)"*, com o painel linkado. Respostas: **u/Rafgaro [+230]**: *"Maybe it doesnt have the automatic attack in exchange for being able to move"*; **u/cranscape [+136]**: *"the extra limitations (feet staying in position) are a condition needed to give Miwa her offensive boost"*; **u/sentientrubberduck [+39]**: *"I always understood the 'if her feet move' part refer to the quickdraw slash, not the SD in general."* — **[I]**, mas o painel apontado (cap. 206) é o que a obra confirmou depois (cap. 254, Kusakabe sem voto). **Queda: (1) pressão do domínio, gradual ("slowly getting destroyed").** Duração: a wiki diz *"only bought her a few short seconds"* (cap. 206 p. 7, 9). **[C] via wiki.**

**Cap. 258/259 (Yuji dentro do Santuário) — a única vez que o ocidente PROPÔS queda por golpe no usuário, e a comunidade derrubou:**
- r/Jujutsushi `1clnn0o`, *"Y YUJI'S SIMPLE DOMAIN COLLAPSED"* (06/05/2024, post com score **0**, 40 comentários). O autor sustenta que o Domínio Simples do Yuji **não** foi arrancado pelo domínio: *"yuji's SD was not broken by MS like gojo's but rather it broke because yuji [couldn't] maintain the required conditions for his SD, that is; he lost his balance and couldn't maintain both feet on the ground. This happened because **sukuna used a manual attack** against yuji."* — isto é, **(2) ataque ao usuário → (5) voto quebrado**.
- **Derrubada, com painel:** **u/turnonforwhat25 [+258]**: *"You skipped a panel that's inconvenient for your argument: the one where it show's **Yuji's simple domain cracking and fracturing *before* he gets hit** in the body by a bunch of slashes."* E ele mesmo, **[+49]**, lê a sequência painel a painel: *(1) Yuji firme; (2) o Domínio Simples rachando; (3) o acerto garantido pega o corpo, com o pé no ar; (4) o pé esquerdo separado; (5) ele arremessado.* Conclusão: *"it simply broke under duress from external pressure."* **u/Aaroniero [+35]** concorda. **u/Abdul-Wahab6 [+41]**: *"Why would Sukuna [do a manual attack] if he's just going to stop his sure hit a second later to use Fuga?"*
- A wiki registra: *"Just before Malevolent Shrine collapses, Yuji's Simple Domain is **forcibly stripped away**, resulting in multiple slashes that sever his left foot."* **[C] via wiki**, cap. 258 p. 17.
- **Veredito ocidental: (1) pressão do domínio**, com o painel da **rachadura antes do golpe**. **[I] +258.**

⚠ **Isto muda um detalhe do `D`.** O `D` §6 registrou como consenso que o Domínio Simples *"não degrada, aguenta e depois quebra de uma vez"* (limiar). **Os fios que acham painel dizem outra coisa:** o 206 mostra a Yuki com ele **"slowly getting destroyed"** [+189], o 258 mostra o do Yuji **rachando antes** de o golpe entrar [+258], e o autor do `1clnn0o` resume: *"every time the simple domain is destroyed **gradually** ... as seen in yuki vs kenny and also gojo vs sukuna."* **O que está de pé nas duas leituras: enquanto não rompe, o acerto garantido não entra.** A diferença é só se a casca **mostra desgaste antes** (os painéis dizem que mostra) — **não** se ela **deixa passar dano parcial** (nenhum painel mostra isso).

**Cap. 226 (Gojo) — Domínio Simples junto com a técnica reversa:** a wiki diz: *"He activated Simple Domain **while simultaneously using reverse cursed technique** to heal himself. Gojo's barrier was **quickly destroyed** by Malevolent Shrine and he was struck by its sure-hit effect again. He conjured **another** Simple Domain shortly after and improvised healing his exhausted technique with reverse cursed technique rather than himself."* **[C] via wiki**, cap. 226 p. 9-14, 17. **Queda: (1).** **Detalhe que importa:** a obra mostra Domínio Simples **e** reversa ao mesmo tempo, e mostra que **dá para erguer de novo** logo depois de arrancado. **[NÃO ACHEI]** fio ocidental discutindo o custo de fazer as duas juntas.

**Cap. 130 (Todo × Mahito):** a wiki: *"Mahito activated his domain's cursed technique **before Todo could counter** with Simple Domain."* **[C] via wiki.** O ocidente usa isso como régua de **tempo de ativação** (ver `D` §9.3). Não é queda: **nunca chegou a proteger.**

### 2.3 "Algum Domínio Simples já caiu por golpe no usuário?" — a resposta dos fóruns

**Dentro de domínio: NÃO no que o ocidente leu.** Todo caso votado é (1) pressão (206, 226, 258) ou corrida perdida (130). A **única** proposta de (2) ataque ao usuário é o `1clnn0o`, e ela tem **score 0** contra **+258** do painel que a desmente.

**Fora de domínio: sim, e o ocidente registra dois casos** — mas nenhum é "anti-domínio caindo", é o **programa de contra-ataque** sendo vencido:
- **Cap. 40 (Miwa × Maki):** resumo da wiki: *"Maki casually breaks her cursed tool and throws it at Kasumi to **negate the effects of her Simple Domain**. Kasumi intercepts [the] projectiles but the latter is able to close the distance and **disarm** Kasumi."* **[C] via wiki.** Leitura ocidental: **u/UnadvisedGoose [+25]** (r/Jujutsushi `1c3yp2z`): *"Miwa ... must use a binding vow to keep her feet planted ... **which is why Maki is able to disrupt it**."* **Queda: (2) ataque ao usuário, explorando o programa automático** (isca arremessada) — o voto aparece como o **motivo de ela não poder recuar**, não como gatilho da queda. **[I] +25.**
- **Cap. 254 (Kusakabe × Sukuna):** resumo da wiki: *"The sustained assault eventually **shatters Kusakabe's katana**."* Depois disso ele luta a socos, restaura a lâmina com *Hazy Moon* e é cortado. **[C] via wiki.** O Domínio Simples dele era veículo do *Evening Moon* (contra-ataque de espada); **quebrar a espada desmonta o programa**. **[I]** — não achei fio ocidental tratando isso como "queda do Domínio Simples".

### 2.4 A nota do Gege (cap. 248) e a contradição que ficou de pé — o que os fóruns acrescentam ao `D`

- Fio r/Jujutsushi `1aj0311` (04/02/2024, post **+153**, 97 comentários), *"Has there been any updates about the whole thing with Kusakabe defending Sukuna's slashes with a simple domain?"*. OP: *"That was like the second or third time Gege has said weird contradictory statements about simple domain."*
  - **u/thacomicfan [+111]**: *"I'm pretty sure Gege corrected this in a comment or something. **The volume release will probably have the actual correct move**."*
  - **u/Zarathoustra1999 [+95]**: *"I think Gege is just being semantic and differentiating between 'technique' and 'technique's effect'. Because he doesn't say SD weakening techniques might be wrong. He's saying 'Simple Domain does not neutralize the technique itself, so expressing it as diluting/watering it down might have been wrong'."*
  - **u/Sm4shaz [+20]**: *"Simple domain reduces the technique's effectiveness/damage, domain amplification neutralises it."*
  - **u/luceafaruI [+31]**: *"We will see in the volume releases how the dialogue is changed."*
- **O que ninguém fechou no ocidente, e é o ponto novo:** **o cap. 254 veio DEPOIS da nota e repetiu o verbo.** O resumo da wiki do 254: *"Kusakabe increases his cursed energy output **while slightly weakening Sukuna's cursed techniques** within the Simple Domain."* E **u/travelerfromabroad [+2]** (r/Jujutsushi, 10/04/2024): *"Kusakabe talks about how even in his simple domain, he gets a boost while opponents and their attacks are weakened."* **[C] via wiki**, cap. 254 p. 1-2. **Se a revista do 254 fala em "enfraquecer levemente" seis capítulos depois da nota do 248, a nota não matou o conceito — ela trocou a palavra do 246** (a leitura do u/Zarathoustra1999 [+95] fica de pé: o que o Gege recuou foi **"diluir"** como **neutralização**, não o **efeito de reforço/enfraquecimento dentro do raio**).
- **Volume encadernado:** **[NÃO ACHEI]** registro ocidental de que o texto do 246 mudou no volume. Procurei: WebSearch ("volume 27 changes chapter 246 Kusakabe simple domain"); título "volume" no r/Jujutsushi (o Arctic Shift deu timeout duas vezes). **Fica em aberto: o ocidente esperou a mudança no volume e eu não achei ninguém confirmando que ela veio.** É pergunta para o agente japonês (comparação 本誌 × 単行本).

### 2.5 Custo de energia, duração, e o "domínio aberto"

- **Energia:** **[NÃO ACHEI]** número ou painel em inglês. O único dado de energia é o **inverso de custo**: no 254 o Domínio Simples **aumenta** a saída do dono (*"increases his cursed energy output"*). **[C] via wiki.**
- **Duração por cena, segundo a wiki inglesa:** Yuki **"a few short seconds"** (206); Gojo **"quickly destroyed"** (226); Yuji/Ino/Choso/Miwa **"almost 99 seconds"** (258). **Nenhum limite próprio da técnica aparece** — o tempo sempre é o do domínio que pressiona. **[C] via wiki.**
- **Por que os de 258 duraram tanto:** o `D` §6 já tem a briga ("voto de 99 s" × "Sukuna nerfado"). O `1clnn0o` acrescenta uma terceira hipótese: *"The domain that sukuna used in the last chapter was an **incomplete domain** ... this incompleteness is the reason y their SD's are holding"*, apoiada na fala do Yuji *"it's an incomplete domain. I can endure it"* (painel linkado). **[I]** — a obra diz que o Santuário do 258 não tinha perda de saída (ver `D`), então a hipótese tem contra-texto.

### 2.6 Domínio Simples — como cai, cena por cena, no olho ocidental

| cena | queda (1–6) | tempo | o que o ocidente diz | marca |
|---|---|---|---|---|
| 40, Miwa × Maki (fora de domínio) | **(2)** via isca no programa automático | — | "Maki is able to disrupt it" pelo voto | [I] +25 |
| 102, Ui Ui × Varíola | **(6)** | — | a Mei Mei resolve do lado de fora | [C] via wiki |
| 130, Todo × Mahito | **nunca protegeu** (perdeu a corrida) | 0,2 s do Mahito | régua de tempo de reação | [C] via wiki |
| 206, Yuki × Kenjaku | **(1)**, gradual | "a few short seconds" | "slowly getting destroyed" enquanto ela corre | [I] +189 / [C] via wiki |
| 226, Gojo × Sukuna | **(1)**, e ergue outro | "quickly destroyed" | junto com reversa | [C] via wiki |
| 254, Kusakabe × Sukuna (fora de domínio) | **(2)** — a espada do programa quebra | — | — | [C] via wiki |
| 258, Yuji × Santuário | **(1)**, racha antes do golpe | "almost 99 seconds" | proposta de (2)+(5) derrubada: +258 × 0 | [I] +258 |
| 258, Ino / Choso / Miwa | **(6)**, o domínio acabou antes | ~99 s | "only Yuji's broke" | [I] |

### 2.7 Adendo ao 2.2: o que a wiki diz do Domínio Simples do Gojo no 226 (detalhe de queda)

O resumo da página `Chapter_226` escreve: *"Gojo heals himself while protecting himself from the sure-hit effect at the same time but Choso comments that this effort will only buy him time. **After a brief physical exchange between the fighters, Gojo's simple domain is destroyed** and he's slashed by the domain again. Gojo immediately activates simple domain again ... this time, everyone notices that Gojo isn't healing himself. ... Gojo's simple domain is destroyed once again."* E o artigo `Simple_Domain`: *"Gojo's barrier was quickly destroyed **by Malevolent Shrine**."* **[C] via wiki.** A troca de socos aparece como **momento**, não como **causa**; a própria wiki atribui a quebra ao Santuário. **Queda (1), duas vezes seguidas, e ele ergue de novo nas duas.** Dado de mesa que ninguém no ocidente discute: **erguer de novo depois de arrancado é possível e rápido** — o custo que a cena mostra é que **na segunda vez ele parou de se curar** (a reversa foi para a técnica queimada).

---

## 3 · PÉTALA (Falling Blossom Emotion, 落花の情)

### 3.1 "Exige concentração" — **ACHEI A ORIGEM, e ela não tem base**

O `A` e o `F` marcaram "a Pétala exige concentração e o Naobito perdeu o foco" como leitura de fã sem base, vinda de "TikTok e resumos". **A cadeia é esta:**

1. **Fiction Horizon**, *"Jujutsu Kaisen: How Was Naobito Able To Resist Dagon's Domain? Falling Blossom Emotion Explained!"*, por **Arthur S. Poe**, **27/10/2023**: *"**Of course**, the technique requires concentration, so Dagon was ultimately able to hit Naobito when he lost focus and some of his energy."* — https://fictionhorizon.com/jujutsu-kaisen-how-was-naobito-able-to-resist-dagons-domain-falling-blossom-emotion-explained/ . **Sem painel, sem capítulo, e com "of course"** — é afirmação do redator.
2. **TikTok @znanimee**, vídeo `7295397263252229381` (o ID decodifica para **29/10/2023**, dois dias depois): *"However, this technique requires concentration, so Dagon eventually Managed to hit Naobito when he lost focus and A portion of his Energy."* — **cópia quase literal** do Fiction Horizon.
3. O homebrew de D&D do `B` (*"You must maintain concentration on Falling Blossom Emotion to keep it active"*) usa "concentration" como **termo de regra de D&D 5e** (a mecânica de manter magia), não como leitura do mangá.

**Veredito: DERRUBADO como canon.** A obra dá outro motivo para o soco (visão tapada, `F`), e a enciclopédia oficial (`F`/`I`) não fala em concentração. **O "exige concentração" nasceu num site de agregador em 27/10/2023 e se espalhou por cópia.** **[I] de fonte fraca, sem painel.** Procurei também: artigos `Falling_Blossom_Emotion`, `Naobito_Zenin`, `Chapter_108`, `Jujutsu_Sorcerers_vs._Dagon` da Fandom — **nenhum** fala em concentração.

### 3.2 Cap. 108 → 109: o "mais de um minuto" é do NANAMI no texto, e a wiki se contradiz

**Isto pode corrigir o `H`.** O `H` escreve: *"Aguenta saturação longa: o Naobito segurou mais de um minuto com 70% do enxame em cima. [C] cap. 108"*. Na Fandom há **duas versões incompatíveis**:

- **Página `Naobito_Zenin`:** *"Withstanding an endless stream of man-eating fish shikigami **for over a minute** and only losing a single arm."* (ref. cap. 109 p. 8-11) — **atribui o minuto ao Naobito.**
- **Página `Chapter_109`:** *"**Dagon is shocked Nanami managed to withstand Death Swarm for about a minute.** Suddenly, Naobito appears behind him ... Dagon ducks under the attack and is **equally surprised the old man survived as well**."*
- **Página `Jujutsu_Sorcerers_vs._Dagon`:** *"Dagon can't believe **Nanami** survived Death Swarm for about a minute and thoughts are interrupted when Naobito appears suddenly behind him. He's shocked that Naobito managed to survive Death Swarm's onslaught **as well**."*

**Leitura:** a fala do Dagon sobre "cerca de um minuto" é **sobre o Nanami** (que **não tem Pétala** e aguentou os 30%); o Naobito aguentou **o mesmo intervalo** (os dois foram engolidos juntos, 70/30, no cap. 108) e sobreviveu "também". **O tempo vale para os dois, mas a frase de canon é do Nanami.** **[C] via duas páginas da wiki contra uma** — ⚠ **conferir no japonês do cap. 109** (é trabalho do agente da obra). Se confirmar, o `H` precisa trocar "o Naobito segurou mais de um minuto" por "**o Naobito sobreviveu ao mesmo enxame que o Nanami aguentou por cerca de um minuto**, perdendo um braço".

**E o dado mais importante que essa comparação expõe: o Nanami, SEM anti-domínio nenhum, aguentou o mesmo minuto com 30% do enxame.** Isso **enfraquece** "aguenta saturação longa" como mérito da Pétala: o que a cena mede é **dano absorvido** (o Naobito com 70% perdeu um braço; o Nanami com 30% ficou de pé), não duração da técnica. **[I]**, minha leitura das duas páginas.

**O que acabou com a Pétala no 109:** nenhuma página da wiki mostra ela caindo. O que acaba é **o enxame**: o Megumi entra com o próprio domínio, e a página da batalha diz *"To **restore** Death Swarm Dagon ignores Maki and focuses on crushing Megumi and his domain"* — ou seja, **o acerto garantido do Dagon parou de valer** quando o Jardim de Sombras entrou (disputa de domínio). **Queda: (6), o acerto garantido acabou antes** — por um terceiro, não pelo dono. **[C] via wiki.** O braço foi perdido **antes**, no trecho em que o soco do Dagon o jogou para o alto com a visão tapada e o enxame continuou (cap. 108). **Causa do braço: (2) ataque ao usuário + saturação.** **[C] via wiki / [I] ligação causal.**

### 3.3 O drawback que o ocidente enxerga

O `D` já tem as duas posições espelhadas ("não serve contra físico" × "só serve contra físico") e a minoria informada ("é disputa de saída"). O que esta rodada acrescenta:

- **VS Battles Wiki, perfil do Gojo:** *"Normally, this technique can nullify a domain's attacks, however, **due to Sukuna's overwhelming pools and output of Cursed Energy it only weakened the damage** from Malevolent Shrine."* — https://vsbattles.fandom.com/wiki/Satoru_Gojo . **[I]** da comunidade de escala mais organizada: **a Pétala perde por saída**, e quando perde, **atenua** em vez de sumir. Aponta cena (cap. 227).
- **Página `Chapter_227` da Fandom:** *"Kusakabe explains how it works but **Choso adds that its output still isn't enough to rival a domain**. Shoko argues that **it'll buy Gojo enough time** to heal his exhausted technique."* **[C] via wiki** — a fala do Choso é a fonte do "saída fraca" da Pétala, **igual** à narração do 266 sobre Cesta e Domínio Simples.
- **Fandom Discussões**, fio `4400000000000062192` (*"Best anti-domain technique?"*), **Ineedalife6** (08/07/2025): *"Falling Blossom Emotion is sort of effective, however **it doesn't nullify anything but just reduce incoming damage**. It's also limited to the three great clans only."* **[I]** sem voto.
- **GameRant** (Harry Nugraha, **12/11/2024**): *"Provides no protection at all against physical attack."* — **[ERRO]**, o mesmo do `D` §2.1, ainda publicado. **Fonte fraca.** https://gamerant.com/jujutsu-kaisen-counters-domain-expansions/
- **DualShockers** (Omar Faruque, **13/10/2023**): a Pétala *"involve[s] a significant amount of cursed energy"*. **[I] sem fonte** — é a única menção ocidental a **custo de energia** da Pétala, e não aponta cena. **Fonte fraca.** https://www.dualshockers.com/jujutsu-kaisen-anti-domain-techniques/

**Consolidado:** o drawback que o ocidente **sustenta com cena** é um só — **saída**: ela atenua mas não iguala um domínio forte (227, fala do Choso + VSB). "Concentração" (3.1) e "não para físico" (`D` §2.1) **não têm painel**. "Gasta muita energia" **não tem painel**.

### 3.4 Como se aprende, e quem usa — o lado ocidental

- **Página `Falling_Blossom_Emotion`:** *"Satoru Gojo **learned how to use Falling Blossom Emotion as a child**, but stopped using it after mastering his domain."* (ref. cap. 227). **[C] via wiki.** É o **único** dado de aprendizado: **se aprende criança, dentro do clã** (o Gojo é do clã Gojo, uma das Três Famílias). **[NÃO ACHEI]** cena de ensino.
- **Usuários na wiki:** Naobito, Ogi (versão de espada, cap. 148) e Gojo. **Nenhum Kamo.** As páginas `Noritoshi_Kamo`, `Kamo_Clan`, `Zenin_Clan`, `Gojo_Clan` e `Sorcerer_Clan` da Fandom **não mencionam** a Pétala. **[NÃO ACHEI]** Kamo com Pétala.
- **VS Battles** põe a Pétala no perfil do **Jinichi Zenin** e, como *"Possibly"*, no do **Naoya Zenin**, citando só o cap. 108. **[I] da VSB** — é inferência por clã, **sem cena** dos dois usando. **Não use como canon.**
- **Kusakabe reconhece a técnica e ninguém mais no grupo** (cap. 227: *"Kusakabe is able to recognize Falling Blossom Emotion but **no one else seems to have ever even heard of the secret art**"*). **[C] via wiki** — isso **é** o drawback de acesso: **segredo de clã de verdade**, nem feiticeiro de grau especial fora das famílias conhece.

### 3.5 Pétala — como cai, cena por cena, no olho ocidental

| cena | queda (1–6) | tempo | o que o ocidente diz | marca |
|---|---|---|---|---|
| 108, Naobito × Dagon (início) | **não caiu** — o soco entrou **por fora dela** (visão tapada) | — | "não serve contra físico" é inferência da wiki (`D` §2.1); "perdeu a concentração" é do Fiction Horizon (3.1) | [C] via wiki / [ERRO] |
| 108→109, Naobito × Enxame da Morte | **(6)** — o acerto do Dagon parou quando o domínio do Megumi entrou | ~1 min (**dito do Nanami**; o Naobito sobreviveu "também") | custou **um braço** | [C] via wiki, ⚠ conferir |
| 148, Ogi × Maki | **não é queda de anti-domínio** — a Dragão-Osso absorve e devolve a energia | — | versão ofensiva com espada | [C] via wiki |
| 227, Gojo × Santuário | **(4) largada** — ele reabre o próprio domínio; ela serviu para **comprar tempo** | não dado | "output still isn't enough to rival a domain" (Choso); "only weakened the damage" (VSB) | [C] via wiki / [I] VSB |
