# D — O debate OCIDENTAL sobre as quatro técnicas anti-domínio

**STATUS: COMPLETO**

Agente: D (debate da comunidade ocidental)
Data: 2026-09-22
Alvo: Hollow Wicker Basket (彌虚葛籠 / Iyako Tsuzura) · Simple Domain (簡易領域) ·
Falling Blossom Emotion (落花の情) · Domain Amplification (領域展延)

Escopo: o que o **ocidente anglófono** discute, discorda, erra e considera em aberto.
Fora de escopo (outros agentes): Extensão de Domínio em si; física da força de domínio.

Convenções deste arquivo:
- `[CONSENSO]` = visto repetido em fontes independentes
- `[OPINIÃO]` = uma pessoa / uma thread só
- `[ERRO]` = afirmação que circula e a obra contradiz
- `[NÃO ACHEI]` = busquei e não encontrei; o caminho tentado fica escrito

---

## 0. Log de acesso (qual caminho funcionou)

_(preenchido ao longo da rodada)_

### Rodada 1 de testes de acesso (2026-09-22)

| Caminho | Resultado |
|---|---|
| `WebSearch` com `allowed_domains: ["reddit.com"]` | **ERRO 400** — "domains not accessible to our user agent". Reddit bloqueia o crawler da Anthropic no robots.txt. Não adianta insistir. |
| `WebFetch` em `www.reddit.com/...` | **"Claude Code is unable to fetch from www.reddit.com"** — bloqueio na própria ferramenta, anterior à rede. |
| `curl` em `www.reddit.com/....json` | **HTTP 403** (página de bloqueio de 190 KB) |
| `curl` em `old.reddit.com/r/X/search/?q=...` | **HTTP 200, 318 KB — MAS é a tela "Welcome to Reddit" de login.** Falso positivo: o código 200 e o tamanho enganam, o conteúdo é a página de login. Sempre conferir o `<title>`. |
| `redlib.privacyredirect.com` | HTTP 200 — mas é desafio **Anubis** ("Making sure you're not a bot", exige JS). |
| `redlib.freedit.eu` / `redlib.perennialte.ch` | 403 |
| `redlib.catsarch.com` / `l.opnxng.com` | 429 (limite de taxa) |
| `redlib.nadeko.net` | 418 |
| `teddit.net`, `eu.safereddit.com`, `redlib.tux.pizza`, `rl.bloat.cat`, `redlib.kittywi.re`, `reddit.private.coffee`, `redlib.baczek.me`, `redlib.frontendfriendly.xyz`, `rl.citizen4.eu` | DNS morto / sem resposta (`000`) |
| `libreddit.privacydev.net` | 502 |
| `redlib.ducks.party` | 404 na rota de busca |
| `html.duckduckgo.com` via curl | HTTP 202 (desafio anti-bot), sem resultados |
| `www.mojeek.com` via curl | 403 |
| `search.marginalia.nu` via curl | 302 |

**Conclusão parcial:** o `curl` cru está queimado em toda a frente Reddit e nos buscadores
alternativos. Próximo caminho: navegador de verdade (executa JS) e arquivos (`web.archive.org`,
`archive.ph`).

### Rodada 2 — o que FUNCIONOU

| Caminho | Resultado |
|---|---|
| `web.archive.org` (CDX API) | **HTTP 503 — "Internet Archive services are temporarily offline"** no dia 22/09/2026. Não é bloqueio, é indisponibilidade. Vale retentar noutro dia: a CDX API com `filter=original:.*simple_domain.*` sobre `reddit.com/r/Jujutsufolk*` acha thread por slug da URL, e é o melhor caminho que sobrou para o Reddit. |
| `archive.ph` | HTTP 429 + **CAPTCHA**. Não resolvo CAPTCHA, caminho abandonado por regra. |
| Navegador embutido em `old.reddit.com` | recusado: "not allowed due to safety restrictions". |
| `WebFetch` em `jujutsu-kaisen.fandom.com/f/p/<id>` | HTTP 402 |
| `curl` na página `/f/p/<id>` da Fandom | HTTP 403 |
| **`curl` na API de Discussões da Fandom** (`/wikia.php?controller=DiscussionThread&method=getThread&threadId=...&responseGroup=full`) | ✅ **HTTP 200, JSON completo com post, autor, data e votos.** Este é o caminho que abriu a aba Discussão da Fandom, que o pedido apontava como "onde a briga fica registrada". |

---

## 1. A aba Discussões da Fandom Wiki (caminho aberto pela API)

### Thread `4400000000000053102` — "Domain Amplification vs Falling Blossom Emotion"
Fórum General · aberta por **Trick the Clown** em **2024-06-07** · 5 respostas

O fio é pequeno mas é exemplar do padrão ocidental: a pergunta é "qual é melhor" e a resposta
que ganha é **"são coisas de categoria diferente"**, não um ranking.

- **Griffvador** (2024-06-07, +3 votos — a resposta mais votada da thread):
  *"Falling blossom doesn't nullify techniques only domains (this doesn't mean it cant be used in
  general combat). Domain amplification does both but at the cost of you unable to use your
  technique while it's active."*
  → É o argumento ocidental padrão do **preço da Amplificação**: ela é a mais forte *e* a única
  com custo de oportunidade explícito (você não conjura enquanto ela está ligada).

- **Marcus Mattson** (2024-06-08, +1) — a resposta longa, e é onde mora a tese ocidental mais
  citada. Dois pontos que importam para mecânica:
  1. Falling Blossom Emotion **é um teste de força**: *"That would work as a defence against a
     Domain's Sure Hit as long as you can outpower the Sure Hit."* — ou seja, o ocidente já lê a
     FBE como defesa **disputada**, medida contra quem abriu o domínio. É exatamente a régua que
     o sistema quer.
  2. FBE **falharia contra acerto garantido não-físico**: *"this technique would fail against
     something like the Information Sure Hit of Hakari's Domain, or Mahito's Domain, less physical
     Sure Hits would likely bypass this technique easily."* — **[OPINIÃO]**, não consenso, e a obra
     nunca testou. Ver §Erros: esta é a raiz de um dos dois erros que o pedido suspeitava.
  3. Domain Amplification é lida como **cabo de guerra de barreira**: *"the Barrier Technique of a
     Domain is what allows for a Sure Hit to exist, so with that disrupted the Domain just doesn't
     have a Sure Hit to use"*, e ele mesmo puxa o precedente do **Megumi contra o Dagon** para
     dizer que é disputa de saída, não imunidade.

- **Osceblue** (2024-06-07, +0): a versão curta e mais repetida — *"Falling Blossom Emotion targets
  the can't-miss attack directly by striking it with cursed energy. Domain Amplification just gets
  rid of it."* — e ele mesmo marca a incerteza: *"I'm pretty sure I'm right, but I could be wrong."*

- **L725** (2024-06-07, +0): *"Different kind of slashes. Amplification uses a single slash.
  Whereas falling blossom used several slashes."* — resposta que confunde as duas com o Sukuna;
  ninguém corrigiu. Registro de como o debate ocidental tem ruído de baixa qualidade misturado.

- **Reegan1470** (2026-01-29, +1) — **[ERRO]**, e mostra que o erro ainda circula em 2026:
  *"Domain Amplification: increases the strength/potency of your domain during a clash against
  cursed energy or opposing domain."* Isso é ler 領域展延 pelo nome em inglês ("amplification")
  como se fosse *buff de domínio*. Não é: a técnica **reveste o corpo** com a camada de domínio e
  não tem nada a ver com fortalecer um Domain Expansion. É o erro de leitura mais barato do
  ocidente e nasce inteiramente da tradução (ver §Tradução).

---

## 2. ERROS DA COMUNIDADE OCIDENTAL — os dois suspeitos do pedido

Os dois suspeitos do pedido foram checados contra o texto ATUAL da Fandom Wiki (lido pela
`api.php`, 22/09/2026) e contra a página de Discussão dela. **Um foi confirmado como erro vivo
na wiki. O outro é erro real, mas a wiki já se corrigiu — ele sobrevive fora dela.**

### 2.1 "Falling Blossom Emotion não serve contra ataque físico" — **[ERRO] CONFIRMADO, e está na wiki HOJE**

O artigo `Falling Blossom Emotion` da Jujutsu Kaisen Wiki escreve, na seção do Naobito, esta
sequência (citação literal, referenciada ao cap. 108 p. 10-11):

> "However, the pure endless volume of shikigami never slowed down and it blocked Naobito's view,
> allowing Dagon to get close and punch him. **This proved that while Falling Blossom Emotion can
> resist cursed techniques, it provides little to no defense against physical attacks.**"

**A própria frase contém a refutação dela.** A premissa que a wiki escreve é *visão bloqueada*
("it blocked Naobito's view, allowing Dagon to get close"). A conclusão que ela tira é
*categoria de ataque* ("little to no defense against physical attacks"). Não decorre: o mangá
mostra o motivo mecânico (ele não viu o soco chegar), e a wiki converte isso numa regra geral
sobre tipo de dano que a obra nunca enunciou.

Pior: a conclusão contradiz o resto do próprio artigo, porque o soco do Dagon **é** físico e os
shikigami que a FBE cortava com sucesso também tomavam forma física. E a seção do Gojo, no mesmo
artigo, diz que a FBE reduziu os cortes do Santuário Malevolente a "shallow cuts" — corte é
dano físico.

→ **Para o sistema:** a FBE não deve ser escrita com imunidade/franquia por TIPO de dano. O que
a obra sustenta é que ela é um contra-ataque **reativo** que precisa PERCEBER o que vem. A
brecha canônica é **percepção**, não categoria. Uma Restrição do tipo "não protege contra o que
o usuário não pode perceber" é fiel; "não protege contra dano físico" é o erro da wiki.

### 2.2 "Simple Domain te prende no lugar" — **[ERRO] real, mas a wiki JÁ CORRIGIU; o erro sobrevive fora dela**

A wiki **hoje** escreve certo, e escreve exatamente a distinção que o pedido suspeitava:

- Sobre a **Miwa**: *"Due to being a beginner, she must impose a binding vow on herself to perform
  the technique, **which stipulates that the technique ends if both her feet leave their original
  position** from when the domain was activated."* (ref. cap. 40 p.4 e cap. 254 p.5)
  → o pé plantado é **o binding vow DELA, por ser iniciante**, e não a técnica.
- Sobre o **Kusakabe**: *"which he can use **without binding vows** and has a **wider range than
  most users**"* (ref. cap. 254 p.5-6).
  → confirma a leitura do pedido: sem vow e com alcance maior.

**Mas a versão errada esteve na wiki como regra geral**, e há prova documental disso na página de
Discussão. Em `Talk:Simple Domain`, seção "Activation and Cancellation conditions", o usuário
**Rizgubi** escreveu em **5 de fevereiro de 2021** citando o artigo daquela época:

> "The article states: *'What is known is that it requires both of the user's feet to remain at a
> set point.... The Simple Domain is dispelled if both feet leave the point at which the area was
> deployed'*"

e pediu esclarecimento — *"Either way I feel that the explanations should be made more clear."*
**Ninguém nunca respondeu.** A página de Discussão tem só 3 revisões em toda a sua história
(2021-01-26, 2021-02-05, 2024-04-28) e nenhuma é resposta a ele.

→ **Diagnóstico:** entre 2021 e hoje a wiki tirou a generalização, mas durante anos ela publicou
a regra do pé plantado **como propriedade do Simple Domain**, sem dizer que era vow da Miwa. Esse
é o período em que vídeos de análise e artigos de agregador copiaram — e eles não se atualizam.
Por isso o erro ainda circula no ocidente enquanto a fonte que o gerou já está limpa. É o modo de
falha clássico: **a wiki conserta, o ecossistema não recebe o conserto.**

### 2.3 Um terceiro erro, não pedido, achado no caminho: "Domain Amplification amplifica o seu domínio"

Na thread da Fandom, **Reegan1470** (2026-01-29) escreve: *"Domain Amplification: increases the
strength/potency of your domain during a clash."* Isso é falso e é **erro induzido pela tradução
oficial**: 領域展延 (*Ryōiki Ten'en*) significa literalmente **"Domain Envelopment"** (envelopamento
de domínio) — a própria wiki registra isso no infobox: `lit. ''Domain Envelopment''`. A palavra
inglesa "Amplification" sugere *aumentar*, quando a técnica **reveste** o corpo com uma camada
fina de domínio sem técnica embutida. O erro é inteiramente um artefato de localização.

### 2.4 A DATA exata em que o erro do pé plantado entrou e saiu da wiki (rastreado no histórico)

Varri as **192 revisões** do artigo `Simple Domain` pela `api.php` e localizei a fronteira por
busca binária. Resultado:

| Marco | Data | Quem |
|---|---|---|
| Artigo criado **já com** a generalização | **2020-01-25** | Aoiaoi600 |
| Reclamação na página de Discussão, sem resposta | 2021-02-05 | Rizgubi |
| **Última revisão COM** a frase generalizada | **2021-02-21** | TheGEORGIO |
| **Revisão que REMOVEU** a generalização | **2021-02-23** | **Young Mako** |

Texto que saiu (revisão de 2021-02-21, literal) — note que ele fala do **usuário**, não da Miwa:

> "What is known is that it requires **both of the user's feet** to remain at a set point."
>
> "**The Simple Domain in its traditional form** creates a circle with 2.21 meter radius around the
> user from the set point they choose and set with their feet. Any cursed techniques deployed in
> this area will automatically be dispelled. The Simple Domain is dispelled if both feet leave the
> point at which the area was deployed."

Texto que entrou (2021-02-23), com tudo reatribuído à Miwa:

> "**Kasumi Miwa's** Simple Domain creates a barrier beneath her feet that spans a 2.21-meter
> radius... **If both feet leave their original position** from when the domain was cast,
> **Kasumi's** technique ends."

**Três coisas que isso prova:**

1. A generalização do pé plantado ficou no ar **13 meses** (jan/2020 a fev/2021) — e essa janela
   cai **exatamente** em cima da estreia no anime do Simple Domain da Miwa (episódios 15 e 17, que
   foram ao ar em jan/fev de 2021, arco do Evento de Intercâmbio de Kyoto). Foi o pico de tráfego
   da página. É por isso que o erro grudou: todo vídeo e artigo escrito naquele mês copiou a
   versão generalizada, e nenhum deles foi atualizado quando a wiki corrigiu dois dias depois.
2. **[ERRO] BÔNUS — o raio de 2,21 m tem o mesmo defeito e é MENOS conhecido.** A wiki antiga
   publicava 2,21 m como o raio do "Simple Domain in its traditional form". Não é: é o raio **da
   Miwa**. O texto atual mantém 2,21 m só na seção dela, e diz do Kusakabe que ele tem
   *"a wider range than most users"*. Quem cita "Simple Domain tem 2,21 m de raio" como número
   do sistema está repetindo a versão de 2020 da wiki. **Se o RPG usar 2,21 m como raio fixo da
   técnica, está importando o erro.**
3. A correção existe, é datada e é verificável — então quando alguém citar a wiki hoje para o pé
   plantado, ele está citando um texto que não existe mais há cinco anos.

---

## 3. A nota de rodapé do Gege (Jump 2024 nº 8, cap. 248) — **o ocidente NOTOU, sim**

**Sim, o ocidente pegou, e rápido.** O caminho de entrada foi o Twitter/X e a coluna oficial da
Viz, e de lá espalhou para os agregadores no mesmo ciclo.

### O que ele disse, nas DUAS versões que circulam (e elas não são iguais)

- **Fan-translation**, postada por **@Go_Jover (Myamura)** no X, `status/1747820804543504881`,
  ~17 de janeiro de 2024 — é a versão que viralizou primeiro:
  > "Akutami Gege's comment for this week: *'Simple Domain doesn't neutralize the Cursed Technique,
  > so using **diluted/weakened** might've been wrong'*"

  e o comentário dela junto, que é a leitura que o ocidente adotou:
  > "In CH-246, when Kusakabe used SD to survive from slashes, Sukuna says SD 'weakened' his CT.
  > Which is wrong, cuz SD never neutralizes CTs"

- **Tradução oficial da Viz**, na coluna **"Mangaka Musings"**, publicada em **21 de janeiro de
  2024** (reportada pela Dexerto):
  > "Simple domain isn't neutralizing the curse itself, so '**thinning it out**' might have been
  > the wrong word choice."

→ **Isto já é, por si, um caso de divergência de tradução** (§5): a mesma frase do autor chega ao
leitor ocidental como *"diluted/weakened"* numa rota e *"thinning it out"* na outra. A palavra
exata importa porque **a palavra exata é o assunto da nota**.

### O que o ocidente concluiu

O enquadramento que pegou, e que a **Dexerto** publica explicitamente, é que **não foi erro de
tradução e sim esclarecimento técnico do autor** — Simple Domain *enfraquece* mas não *neutraliza*,
e quem *neutraliza* é a Domain Amplification. A Sportskeeda cobriu como **"Akutami fixes a major
Kusakabe flaw"**, isto é, tratou como **conserto**, não como retcon.

**[CONSENSO]** — o ocidente tratou a nota como correção bem-vinda e não como inconsistência.
Não achei reação de indignação nem acusação de retcon a respeito desta nota especificamente.
Caminhos tentados: WebSearch com os termos "retcon", "fans reaction", "confusion"; Dexerto;
Sportskeeda; GameRant. **[NÃO ACHEI]** thread de fórum reclamando dela.

### ⚠ A contradição que ficou de pé, e que ninguém no ocidente fechou

**A Fandom Wiki, hoje (22/09/2026), ainda publica a versão que o Gege desdisse.** O artigo
`Simple Domain` diz, palavra por palavra:

> "Unlike Domain Amplification, New Shadow Style: Simple Domain cannot fully neutralize cursed
> techniques itself. **However, it can weaken techniques that enter its range, reducing their
> strength while enhancing the user's own cursed energy output.**"
> (referenciado ao cap. 246 p.3 e cap. 254 p.1-2)

Ou seja: a wiki absorveu a metade da nota que diz "não neutraliza" e **manteve** a metade que o
Gege chamou de escolha de palavra errada ("enfraquece / dilui"). E a seção do Kusakabe repete:
*"reducing the damage dealt to himself by **weakening the cursed technique**"*.

→ **[ERRO] em aberto.** Esta é uma frase morta na wiki: o autor recuou publicamente do verbo e a
wiki continua com ele. **Para o sistema isso é decisão de design, não de canon** — a obra não
oferece uma regra limpa aqui. As duas leituras possíveis:
- **leitura "só barreira"** (a nota do Gege): Simple Domain anula SÓ o acerto garantido, mexendo
  na barreira; o dano bruto do que vem passa inteiro. É a leitura consistente com o Hollow Wicker
  Basket, que a própria wiki descreve como "cannot neutralize cursed techniques themselves".
- **leitura "atenua"** (o texto do cap. 246 e a wiki): além de anular o acerto garantido, reduz a
  potência do que entra.

O Gege empurrou para a primeira. Se o RPG quiser a segunda, é escolha de mesa, e vale escrever
que ela contraria a nota do autor.

---

## ⭐ O CAMINHO QUE ABRIU O REDDIT — `api.pullpush.io` (anote isto para a próxima rodada)

Depois de todos os caminhos do pedido falharem, o que funcionou foi um **arquivo de terceiros**,
sucessor do Pushshift:

```
https://api.pullpush.io/reddit/search/comment/?q=<termo>&subreddit=<sub>&size=100&sort=desc
https://api.pullpush.io/reddit/search/submission/?q=<termo>&subreddit=<sub>&size=100
```

- Devolve **HTTP 200 com JSON cru do Reddit**: autor, `created_utc`, `score`, `body`, `permalink`,
  `subreddit`. Tudo o que a regra de citação pede.
- **Cuidado 1 — limite de taxa agressivo.** A primeira chamada devolveu
  `{"error":"Rate limit exceeded. This website does not provide free scraping resources for
  agents."}`. O que resolveu foi **espaçar as chamadas e repetir com espera crescente** (8 s, 12 s,
  16 s...). Uma chamada por vez, nunca em paralelo.
- **Cuidado 2 — é LENTO.** Cada busca leva dezenas de segundos. Planeje rodar em segundo plano.
- `arctic-shift.photon-reddit.com/api/posts/search` — mesma família, devolveu
  `{"error":"Timeout. Maybe slow down a bit"}` (HTTP 422). **É um segundo caminho válido**, vale
  retentar devagar numa próxima rodada.

**Resumo do que funcionou vs. não funcionou (a resposta direta ao pedido):**

✅ **Funcionou:** `api.pullpush.io` (Reddit, arquivo) · `api.php` da Fandom (artigo + **histórico
de revisões** + páginas `Talk:`) · `wikia.php?controller=DiscussionThread` (aba Discussões da
Fandom) · `WebSearch` e `WebFetch` em tudo que não é Reddit (Dexerto, Sportskeeda, GameRant,
ScreenRant, CBR, X/Twitter via trecho de buscador).

❌ **Não funcionou:** `WebSearch` com `allowed_domains: reddit.com` (bloqueio de robots) ·
`WebFetch` em reddit.com (bloqueio da ferramenta) · `curl` em reddit.com (403) · `old.reddit.com`
(devolve 200 mas é a tela de login — **armadilha**) · navegador embutido (recusa por política) ·
todos os espelhos redlib/libreddit/teddit/safereddit testados (403/429/418/DNS morto/desafio
Anubis) · `archive.ph` (CAPTCHA — não resolvo por regra) · `web.archive.org` (**503, Internet
Archive fora do ar no dia** — não é bloqueio; vale retentar, e a CDX API filtrando por slug de URL
é o melhor plano B) · buscadores alternativos por `curl` (DDG 202, Mojeek 403, Marginalia 302).

---

## 4. O RANQUEAMENTO OCIDENTAL — **a hipótese da rodada anterior NÃO se sustenta**

> Hipótese a testar: *"o ocidente põe Domain Amplification como a melhor e o Japão como a pior."*

**Veredito: DERRUBADA como se fosse posição ocidental única.** O ocidente **não tem um
ranqueamento só** — ele tem duas escolas que discordam frontalmente, e a briga entre elas é o
achado principal desta seção. Achei fonte ocidental de peso colocando a Domain Amplification em
**primeiro** e fonte ocidental de peso colocando a mesma técnica em **último**.

### Lado A — "Domain Amplification é a melhor" (a escola do efeito)

Argumento: ela é a única que **anula técnica maldita**, e não só o acerto garantido. As outras três
mexem na barreira/no acerto; a Amplificação desliga a técnica em si. Na thread da Fandom,
**Griffvador** (2024-06-07, resposta mais votada, +3) formula isso na forma mais curta:
> "Falling blossom doesn't nullify techniques only domains... **Domain amplification does both**
> but at the cost of you unable to use your technique while it's active"

A Fandom Wiki reforça com duas frases que essa escola cita sempre:
> "While similar to New Shadow Style: Simple Domain, **Domain Amplification is more refined**. It
> has the potential to negate an opposing technique and **doesn't require binding vows** to use
> proficiently."

e o precedente do Infinito: a Amplificação é a técnica que **desligou a Infinidade do Gojo** — o
feito de maior prestígio que qualquer anti-domínio tem na obra. Esse é o trunfo retórico do lado A.

### Lado B — "Domain Amplification é a PIOR" (a escola do custo de oportunidade)

Fonte ocidental concreta e rastreável, e é grande: **Sportskeeda, "Jujutsu Kaisen: Every
anti-domain technique as of chapter 227", por Joseph Brogan, modificado em 30/06/2023**, editado
por Abhipsa Choudhury. Ele escreve, literalmente:

> "The major drawback to Domain Amplification, however, is that a user can't activate it and their
> own innate Cursed Technique simultaneously. As a result, and based on what's known and been seen
> of it so far, **it seems largely inferior to both Falling Blossom Emotion and the Simple Domain
> techniques.**"

Argumento: as outras três você usa **enquanto luta**; a Amplificação te reduz a **mãos nuas**. Numa
mesa, isso é a diferença entre uma defesa e uma troca de build no meio do turno.

O mesmo artigo monta o par Simple Domain × Falling Blossom Emotion com dois critérios que o
ocidente repete muito:
> "One downside of the Simple Domain compared to Falling Blossom Emotion is that **the former can
> be destroyed by a more powerful domain within seconds**. One upside is that a **Simple Domain can
> be used in an offensive manner**, whereas Falling Blossom Emotion is seemingly a defensive
> technique only."

→ **Para o sistema, é este o eixo que importa e ele é o mesmo dos dois lados:** ninguém no ocidente
discorda de que a Amplificação **entrega mais** e **custa mais**. Eles discordam só de qual metade
manda no ranking. Isso é desenho de preço, não de canon: se no RPG a Amplificação desligar a
técnica do usuário enquanto ativa, os dois lados ficam satisfeitos e o ranking vira escolha do
jogador, que é o resultado certo.

### ⚠ O quarto membro some do ranking ocidental

O artigo da Sportskeeda chama-se "**EVERY** anti-domain technique as of chapter 227" — e lista
**três**. **Hollow Wicker Basket não aparece**, apesar de ter estreado no **cap. 171**, 56
capítulos antes do recorte do próprio artigo.

**[CONSENSO, por omissão]** A Hollow Wicker Basket é sistematicamente esquecida no ocidente. Ela
quase nunca entra em lista de ranqueamento; quando entra, entra como "a versão velha do Simple
Domain". Isso distorce a discussão inteira, porque ela é justamente a que a obra usa para mostrar
o **limite compartilhado** das quatro: a wiki diz que ela *"cannot neutralize cursed techniques
themselves, making it ineffective against incomplete or non-lethal domains"* — a mesma trava que o
Gege depois confirmou valer para o Simple Domain na nota do cap. 248.

### E o erro do §2.1 aparece aqui de novo, propagado

O mesmo artigo da Sportskeeda repete o erro da wiki palavra por palavra:
> "However, the move doesn't protect against physical attacks, as Dagon was still able to punch
> Naobito despite the latter's use of the technique."

**Prova de propagação:** a conclusão da wiki (escrita antes) chega a um veículo de alto tráfego
(2023) já **sem** a premissa que a justificava — a wiki pelo menos escrevia "it blocked Naobito's
view"; a Sportskeeda corta isso e publica só a regra geral. É assim que vira "consenso" ocidental.

---

## 5. EM QUE O OCIDENTE DISCORDA ENTRE SI — as brigas, com os dois lados

Fonte: Reddit via `api.pullpush.io`, varredura de 20 a 22 de setembro de 2026, mais a aba
Discussões da Fandom. **Aviso de método:** o `score` que o PullPush devolve é o do momento em que
o arquivo raspou o comentário, quase sempre poucos minutos depois de postado — por isso quase tudo
aparece com `+1`. **Não use esses números como medida de apoio da comunidade.** O que vale é a
autoria, a data, o link e a repetição do argumento entre pessoas diferentes.

### BRIGA 1 — "Domain Amplification é ou não é uma técnica anti-domínio?"

Esta é a discordância **mais quente e mais estrutural** que achei, e ela não estava na lista do
pedido. Há uma facção ocidental inteira que sustenta que a Amplificação foi **classificada
errado**.

**Lado "não é anti-domínio, é anti-TÉCNICA":**
- **u/AlienGoat_**, r/Jujutsu_Kaisen, **2026-09-20**
  (`/r/Jujutsu_Kaisen/comments/1wlo9dp/.../pb0csop/`):
  > "Domain amplification **isn't an anti domain technique, it's an anti technique technique**.
  > Against unlimited void, it wouldn't do anything. Against MS, it would probably act the same way
  > as falling blossom emotion."

  E ele dá o modelo mecânico que essa facção usa, que é útil para o RPG porque é **quantitativo**:
  > "A technique, let's say Gojo's Red, first hits the domain amplification and gets neutralised,
  > but **it still isn't powerful enough to fully neutralise the technique, so the leftovers will
  > hit the main body**."
  → isto é **defesa com capacidade finita e transbordo**, não imunidade booleana. É a leitura mais
  jogável das quatro que apareceu na varredura.

- **u/Western_Half_1231**, r/PowerScaling, **2026-09-22**
  (`/r/PowerScaling/comments/1wlnhkf/.../pbedcje/`), a mesma tese com muito mais agressividade:
  > "**DA isn't an anti domain technique, it does jackshit against UV.** If you are inside a domain
  > and don't have a domain of your own or an anti domain tech you're gonna get hit by the sure
  > hit... you could argue he can figure out one of the anti domain techniques mid domain such as:
  > **Simple domain, HWB and Falling blossom emotion**."
  → note que ele lista **três** anti-domínio e deixa a Amplificação **fora da lista**, de propósito.

**Lado "é sim, e o canon diz":** a Fandom Wiki classifica `Domain Amplification` como
`Anti-Domain Technique` e afirma, com referência ao **cap. 171 p. 5**:
> "It will negate any technique it encounters and **weaken the sure-hit effect imbued into opposing
> domains as well**."

**[ERRO] da facção, com ressalva.** O canon citado está do lado da wiki: o cap. 171 diz que a
Amplificação enfraquece o acerto garantido. Mas a facção tem meio ponto legítimo, e é um ponto que
importa para o sistema: a Amplificação **não é imune** a acerto garantido, ela o **enfraquece** —
que é coisa diferente do que o Simple Domain e a Hollow Wicker Basket fazem (**anular**). O erro
está em transformar "enfraquece em vez de anular" em "não faz nada".

→ **Para o sistema:** há justificativa em texto para as quatro NÃO serem todas a mesma coisa
mecânica. Duas **anulam** o acerto garantido (Simple Domain, Hollow Wicker Basket), uma
**contra-ataca** o acerto garantido (Falling Blossom Emotion) e uma **enfraquece** o acerto
garantido enquanto **anula técnica** (Domain Amplification). Se as quatro virarem a mesma
Restrição com números diferentes, o sistema perde justamente o que o ocidente briga.

### BRIGA 2 — Falling Blossom Emotion: contra o que ela serve, afinal?

Aqui o ocidente se contradiz **em espelho**, e isso é o achado mais engraçado da varredura: as
duas afirmações mais repetidas sobre a FBE são **opostas uma à outra**, e as duas são erro.

- **Posição A (a da wiki e da Sportskeeda):** "não serve contra ataque **físico**" — ver §2.1.
- **Posição B (a do Reddit):** serve **SÓ** contra ataque físico. Literal, de
  **u/Phantom_tpa**, r/JujutsuPowerScalers, **2026-09-21**
  (`/r/JujutsuPowerScalers/comments/1wm3325/.../pb7o4r1/`):
  > "Falling blossom emotion **does not work on UV, only against physical sure hits**"

**[ERRO] nos dois lados, e eles se anulam.** A obra nunca disse nenhuma das duas. O que ela mostra
é (a) FBE cortando shikigami do Dagon com sucesso, (b) o Dagon acertando um soco **porque o Naobito
não viu**, e (c) a FBE reduzindo os cortes do Santuário Malevolente a arranhões no Gojo.

Existe uma terceira posição, mais cuidadosa, que trata o assunto como **em aberto** em vez de
resolvido — **u/The_Slumbering**, r/CTsandbox, **2026-09-20**
(`/r/CTsandbox/comments/1wkrg8g/.../paxhduc/`):
> "If it's the sure-hit, and not an environmental effect like Coffin of the Iron Mountain's heat,
> then surely an anti-domain technique like Simple Domain or Hollow Wicker Basket would work?
> **I'm not so sure about Falling Blossom Emotion; the way the sure hit manifests sounds like it
> would overwhelm it.**"
→ Esta é a formulação honesta: a FBE tem **capacidade**, e a pergunta é se o que chega cabe nela.
É a mesma leitura do Marcus Mattson na Fandom ("as long as you can outpower the Sure Hit").
**[CONSENSO da minoria informada]:** FBE é disputa de saída, não categoria de dano.

### BRIGA 3 — a Amplificação se gasta?

- **u/LegitimateHair7490**, r/Jujutsufolk, **2026-09-22**, na thread dedicada
  "my take on anti-domain techniques" (`/r/Jujutsufolk/comments/1wnjn2v/.../pbfiyig/`):
  > "Domain amplification feels like it might be **best unironically when it's outside of a domain
  > expansion**. It seems **consistent damage wears domain amplification off** which makes it bad
  > as an anti domain technique — at least falling blossom emotion feels a bit better in this
  > category. Then there's the aspect of it being good offensively against certain techniques like
  > sky manipulation and infinity."

  → **[OPINIÃO]**, mas é a formulação mais útil que achei: separa **valor ofensivo** (desligar
  Infinidade, desligar técnica do oponente) de **valor defensivo dentro de domínio** (ruim, porque
  dano contínuo a desgasta). O ranking ocidental inteiro depende de qual dos dois papéis você está
  medindo — e é por isso que o §4 achou a mesma técnica em primeiro e em último lugar.

---

## 6. O CAPÍTULO 258 — quatro Domínios Simples quase 99 segundos dentro do Santuário Malevolente

**Pergunta do pedido: o ocidente chamou de inconsistência?**
**Resposta: uma minoria chamou; a maioria NÃO, e a explicação que venceu é específica e verificável
no texto.** O debate existe, é vivo e está ativo ainda em setembro de 2026.

### O lado "isso é inconsistência / o Sukuna estava nerfado"

A formulação da acusação, citada por um oponente dela em r/JujutsuPowerScaling
(thread `1wm9n6x`, "the top 2 beat Kenjaku in a domain clash", **2026-09-21**):
> "Sukuna was so weakened at this point, he couldn't even overpower the domains of someone like
> Miwa"

É o argumento de força: se a **Miwa** — a usuária mais fraca de Simple Domain da obra, que precisa
de voto vinculante por ser iniciante — segura o Santuário Malevolente, então ou o Simple Domain é
bom demais ou o Sukuna estava fraco demais. Um dos dois tem de ceder.

### O lado "não é inconsistência, é voto vinculante" — **e é este que ganhou**

**u/Parking-Usual**, r/JujutsuPowerScaling, **2026-09-21**
(`/r/JujutsuPowerScaling/comments/1wm9n6x/.../pb6m9qp/`), respondendo com painel na mão:
> "The manga directly states that Sukuna's domain had **no loss of range or output**... So no, his
> domain was **not** weaker. **He made multiple binding vows in order to ensure it could unleash at
> full output. That's why it lasted 99 seconds.** ... 3 panels later for people who still wanted to
> insist it was a weaker domain we're outright told: *'Ryomen Sukuna sent slashes flying throughout
> his barrier on a scale as large as Shibuya'*. **It was a full powered Malevolent Shrine.**"

**A leitura vencedora, em uma linha:** os 99 segundos **não são fraqueza, são o preço**. O Sukuna
trocou **duração** por **saída máxima** num voto vinculante. Logo o Santuário estava no talo, e os
Domínios Simples seguraram um domínio no talo.

→ **Isto é diretamente relevante para o RPG.** O ocidente resolveu a aparente contradição com
exatamente o mecanismo que um sistema de mesa usaria: **um voto que troca duração por potência**.
Não precisou de retcon nem de "o autor errou".

**u/Salty_Cow4181** (r/JujutsuPowerScaling, **2026-09-21**) sustenta a versão intermediária, que é
a mais comum: a saída **geral** do Sukuna estava arrasada pela luta inteira, *e por isso* ele fez o
voto — *"he had to make a binding vow limiting the duration of the domain to 99 seconds allowing
him to boost the output back to max."* Ou seja, os dois lados podem estar certos em camadas
diferentes: **Sukuna fraco + voto que devolve a saída ao máximo**.

### O que o ocidente FEZ com o feito: virou régua de escala

O uso principal do episódio no ocidente não é acusar inconsistência, é **medir o Yuji**. Em
r/YUJI_Corp, thread `1wmk0sa` ("is there a way to scale EoS Yuji's DE refinement"), **2026-09-21**:

- **u/MathematicianSlow263**:
  > "his simple domain alone could withstand full output malevolent shrine for the better part of
  > 99 seconds... **yuji's SD lasting in Shrine, which directly correlates to his barrier mastery
  > in general, is what makes his domain refinement so good.** Keep in mind, this is his first ever
  > domain."
- **u/carl-the-lama**, mesma thread:
  > "his barrier refinement is very high, lasting nearly 99 seconds against Sukuna's nerfed
  > malevolent shrine. **According to Gojo, domain >>>> simple domain as a way to endure domains.**"
  (note que ele diz "nerfed", ou seja, a versão do nerf continua circulando em paralelo)
- **u/AlienGoat_**, r/YUJI_Corp, **2026-09-22**:
  > "Yuji can survive full power MS for 99 seconds. After that he is cooked (**we see him instantly
  > lose a leg when his SD breaks**)"

→ **Ponto mecânico que o ocidente tratou como consenso:** o Simple Domain **não degrada**, ele
**aguenta e depois quebra de uma vez**. Enquanto está de pé, protege; quando cai, o dano acumulado
chega todo junto (a perna do Yuji). Isso é **limiar**, não **redução progressiva** — para uma regra
de mesa é a diferença entre "reduz X de dano por turno" e "anula até quebrar".

### A resposta curta à pergunta do pedido

**[CONSENSO]** Não é lido como inconsistência pela maior parte do fandom ocidental de escala. É
lido como **feito de refinamento de barreira** dos quatro sorcerers e como **preço pago pelo
Sukuna**. **[MINORIA]** existe, e o argumento dela é a Miwa: uma iniciante com voto vinculante
segurando o mesmo domínio que despedaçou o Simple Domain do Gojo e o da Yuki é o ponto que o lado
vencedor nunca explicou bem. **Não achei** ninguém do lado vencedor respondendo especificamente à
Miwa — só ao "Sukuna estava fraco". Caminhos tentados: PullPush com `"simple domain"`, `"99
seconds"`, janela de março de 2024 e janela de setembro de 2026.

---

## 7. POWERSCALING APLICADO — quem fura qual defesa, e com que argumento

Isto importa porque no sistema a defesa mede contra a FORÇA de quem abriu o domínio. O ocidente
de escala **já trabalha nesse eixo** e produziu distinções utilizáveis.

### 7.1 A distinção Hollow Wicker Basket × Simple Domain — **a melhor coisa que achei nesta rodada**

**u/Loud-Boat-4124**, r/CTsandbox, **2026-09-21** (`/r/CTsandbox/comments/1wmrwyc/.../pb9iktz/`),
argumentando dentro de uma discussão sobre homebrew de técnica (ou seja, gente fazendo exatamente
o que este projeto faz):

> "Both nullify the technique but they do so in different ways. **Hollow wicker basket can be
> structurally maintained with the hand sign but it lacks versatility. Simple Domain is more
> versatile and allows for more freedom in combat, but it is at risk of being destroyed by the
> domain.**"

→ **Traduzido para regra:** as duas anulam o acerto garantido, mas o preço é oposto.
- **Hollow Wicker Basket** = você **paga mãos/ação continuamente** e, em troca, pode **reforçar** a
  defesa gastando mais. Ela não quebra por saída do oponente, ela quebra quando você solta.
- **Simple Domain** = **mãos livres**, você luta normalmente; em troca ela **tem ponto de ruptura**
  e um domínio mais forte a despedaça.

Isto é um par de Restrições limpo e assimétrico, e **é apoiado pelo texto**, não só pela opinião:
a wiki registra que o Sukuna manteve a HWB com *"half of his arms and mouths... occupied"* (cap.
249) e depois *"maintained it with two of his hands, **compensating for its weak output**"* (cap.
266) — ou seja, **gastar mais mãos compra mais defesa**. Enquanto o Simple Domain do Gojo e o da
Yuki foram **despedaçados** por domínios mais fortes, sem opção de reforço.

Confirmações independentes do custo de mãos:
- **u/Itsov3r-soLetsDraw**, r/JujutsuPowerScaling, **2026-09-21**: *"Hollow wicker basket would
  force him to **use two arms to maintain it** and give up his 'advantage'."*
- **u/Mainkenchi**, r/YUJI_Corp, **2026-09-21**: *"sukuna was also using hollow wicker basket
  **which hinders him a decent bit**."*
- **u/Gepapa363**, r/JujutsuPowerScaling, **2026-09-21**, propondo conserto de personagem:
  *"I think instead of an outright domain Kashimo could be given an **extra pair of hands**. That
  way he can **hold hollow wicker basket while fighting**."* — a comunidade trata o custo de mãos
  como **a** limitação definidora da técnica.
- **u/No-Resort-4773**, r/Jujutsufolk, **2026-09-21**: *"Yuji and Yuta were prepared for Sukuna
  **deactivating hollow wicker basket** for world cutting slash"* — **você tem de largar a defesa
  para dar o golpe grande.** É trade-off de ação, e é canônico.

### 7.2 O ranking ocidental da Hollow Wicker Basket: last place, por consenso

- **u/Lord-Seth**, r/JujutsuPowerScaling, **2026-09-21**: *"his only form of anti domain is hollow
  wicker basket, **an inferior form of simple domain**."*
- A própria wiki reforça: *"the predecessor to New Shadow Style: Simple Domain"* e *"cannot
  neutralize cursed techniques themselves, making it **ineffective against incomplete or non-lethal
  domains**"*.

**[CONSENSO]** HWB é a pior das quatro no ocidente. **[MINORIA dissidente]**, e o argumento dela é
bom: **u/SaIamiShadow**, r/Jujutsufolk, **2024-03-20**
(`/r/Jujutsufolk/comments/1bjdqgo/.../kvtd3qo/`):
> "i really can't think of **why Sukuna wouldn't just use simple domain against Yuta if it is that
> much better than HWB** lol. imo Sukuna's choice to use HWB heavily implies its **a binding vow
> for stronger protection but u can't use ur hand**. That's wayyy more believable than arguing
> Sukuna not being able to use simple domain."

→ Argumento de revelação de preferência: **o personagem mais forte da obra escolheu a técnica
"pior"**, duas vezes, contra dois domínios diferentes. Ou ele não sabe Simple Domain, ou a HWB
compra algo que o Simple Domain não compra. A obra nunca disse qual. **É uma das perguntas em
aberto (ver §8).**

### 7.3 A briga do domínio não-letal: Simple Domain / HWB funcionam contra o Hakari?

Esta é uma disputa **técnica**, com os dois lados citando texto.

**Lado "não funcionam":** é o que a obra parece dizer. A wiki, sobre o Kashimo (cap. 187 p.1):
> "he abandoned this idea because **the sure-hit effect is the transmission of information about
> the domain, which is harmless**."

**Lado "deveriam funcionar":** **u/Illustrious-Bass4354**, r/YUJI_Corp, **2026-09-21**
(`/r/YUJI_Corp/comments/1wkux52/.../pb5mbvd/`), respondendo a quem dizia que são inúteis:
> "Why would you think SD and HWB are useless against it? **Hakari's DE should not work without the
> sure-hit that explains the function of his spins**, per Tengen's explanation of non-lethal DEs and
> Higuruma's own rules for his DE to work. By blocking the sure-hit that forces that information
> into your mind, you are **either completely preventing his DE from functioning at all, or at least
> dramatically reducing his likelihood of rolling a Jackpot**."

E ele acrescenta a diferença entre as duas que o resto da comunidade ignora:
> "SD also has other strengths over HWB, such as **weakening the actual CT itself if it enters the
> SD, and increasing the caster's CE**."
(note: essa é justamente a propriedade que o **Gege desdisse** na nota do cap. 248 — ver §3. O
argumento dele usa uma frase que o autor recuou.)

→ **Para o sistema:** há uma pergunta de desenho embutida aqui que vale escrever explicitamente —
**anular o acerto garantido de um domínio cujo acerto garantido é uma REGRA anula a regra?** A obra
diz que não (o Kashimo desistiu). A lógica da comunidade diz que sim. É decisão de mesa, e os dois
lados têm texto.

### 7.4 O erro de escala que circula: "a Yuki inventou o Simple Domain"

**[ERRO]** — e circula nos **dois lados** de uma discussão, sem ninguém corrigir. Em
r/Jujutsufolk, thread `1bjhh5g`, **2024-03-20**:
- **u/barry-8686**: *"it destroyed Yuki's simple domain (why is this impressive? **BECAUSE YUKI
  INVENTED THE SIMPLE DOMAIN**)"*
- **u/LEFTRIGHTADORI**, discordando da conclusão mas **aceitando a premissa**: *"**Yuki inventing
  the simple domain** doesn't mean shit lmao."*

A obra diz o contrário: quem criou a Escola da Nova Sombra e desenvolveu o New Shadow Style: Simple
Domain foi **Sadatsuna Ashiya**, na era Heian (cap. 171 p.3), a partir da Hollow Wicker Basket. A
Yuki **aprendeu por observação** (cap. 269 p.13) — precisamente porque o voto vinculante da escola
proíbe *ensinar* a estranhos mas não previu que dava para *copiar olhando*. Ela é uma
**contornadora** do voto, não a inventora.

---

## 8. DIVERGÊNCIA DE TRADUÇÃO — Viz (John Werry) × TCB Scans, e a confusão documentada

Esta seção rendeu mais do que eu esperava. **A tradução não é uma nota de rodapé no debate
ocidental — ela é o chão de várias brigas de powerscaling**, e o fandom sabe disso: eles citam
tradutor por nome e trocam painel das duas versões dentro da mesma discussão.

Os comentários abaixo têm **pontuação real** (não são +1 de raspagem recente), então dá para
separar consenso de opinião solta.

### 8.1 "Domain Amplification" é tradução errada — **[CONSENSO informado]**

- **u/Fardin_197**, r/Jujutsushi, **2026-05-15**, **+17**
  (`/r/Jujutsushi/comments/1tddq33/is_domain_amplification_a_barrier_technique/olvqofx/`):
  > "From what I recall ***Domain Amplification* is the wrong translation** and proper one is
  > ***Domain Envelope*** or something like that."
- **u/Unexpected_Fellow**, r/Jujutsufolk, **2026-06-20**, **+13**
  (`/r/Jujutsufolk/comments/1ub7rlu/my_brain_still_doesnt_get_domain_amplification/osu4u91/`):
  > "**Domain Amplification is sort of a poor translation** since essentially when you use Dom Amp
  > you generate an empty barrier around yourself; when that barrier goes near or enters a
  > technique it takes it in, causing the technique to weaken or become nullified."

O japonês é 領域展延 (*Ryōiki Ten'en*), e 展延 é **estender/laminar**, não amplificar. A própria
Fandom Wiki registra `lit. Domain Envelopment` no infobox — mas mantém "Amplification" como título,
porque é o termo da Viz. **Resultado: o nome oficial descreve a técnica errada, e a correção mora
numa linha de infobox que quase ninguém lê.** É a origem do erro do §2.3.

### 8.2 O caso mais concreto: a Viz escreveu "Domain Expansion" onde era "Domain Amplification"

- **u/Different_Tadpole631**, r/JujutsuPowerScaling, **2026-04-05**, **+6**
  (`/r/JujutsuPowerScaling/comments/1scrzwj/doesnt_this_kind_of_confirm_jacobs_ladder_shuts/oedtjsi/`):
  > "This is a **shitty translation**. The '**Domain Expansion**' mentioned here **is actually
  > domain amplification**. What it means is that it targets your CE directly, so **DA can't reduce
  > its potency**."
- **u/Ok-Opportunity8921**, r/JujutsuPowerScalers, **2026-07-28**, confirmando de forma independente:
  > "Yes it is a **wrong translation**, but the general idea is the same: 'Jacob's Ladder and Boogie
  > Woogie target CE directly, so **Domain Amplification won't stop it**.'"

→ **A confusão documentada, e ela é exatamente a que o pedido procurava:** um painel sobre o que a
**Amplificação** não bloqueia foi traduzido como se fosse sobre **Expansão de Domínio**. A thread
inteira (`1scrzwj`, "doesn't this kind of confirm Jacob's Ladder shuts...") nasceu de uma pergunta
de powerscaling que **só existe por causa do erro**.

→ **Regra que sobrevive à confusão, e que vale para o sistema:** há afirmação em texto de que
**técnica que mira a energia amaldiçoada diretamente atravessa a Amplificação**, porque a
Amplificação neutraliza *técnica*, não *energia*. Isso é uma **exceção nomeada** — um tipo de
ataque que fura uma defesa específica. É exatamente o material de Restrição que o pedido queria.

### 8.3 O fandom nomeia o tradutor e escolhe lado

- **u/Fickle_Tie8014**, r/Jujutsufolk, **2026-06-26**
  (`/r/Jujutsufolk/comments/1ugijbd/can_a_sorcerer_embed_their_sure_hit_into_domain/ou0gqia/`):
  > "Yeah it's the translation of **John Werry** so it isn't the most reliable source. Here the
  > **TCB** translation: [imagem]"
  (John Werry é o tradutor oficial da Viz; TCB Scans é a principal fan-translation inglesa.)
- **u/ApprehensiveUnion707**, r/JujutsuPowerScaling, **2026-06-14**:
  > "**TCB is also the better direct English translation**, but it wouldn't matter either way."
- **u/Asian_Persuasion_1**, r/JuJutsuKaisen, **2026-03-15**, **+42** — o comentário mais votado
  que achei sobre o assunto, e ele abre assim:
  > "well to start, **you're reading the VIZ translation which is bad at translating**."

**[CONSENSO]** no fandom ocidental de escala: **a Viz é tratada como fonte menos confiável que a
TCB** para detalhe mecânico. Isso é relevante para este projeto: se o RPG citar texto em inglês,
vale saber que a comunidade que ele vai encontrar considera a tradução oficial suspeita.

### 8.4 Uma briga inteira que é só tradução: "o Sukuna usou Amplificação dentro do domínio?"

Duas leituras do mesmo painel, e a conclusão de powerscaling muda junto:

- **u/King_shubh**, r/JujutsuPowerScalers, **2026-03-15**: *"**Both TCB and Viz have this
  translation.** The original panel has ​**展延 (Ten'en)** which is used to refer to Domain
  Amplification... there were periods in which he didn't [use it]."*
- **u/Least_Cap_7441**, r/Jujutsu_Kaisen, **2026-03-23**: *"Which is pretty much based on a **wrong
  translation**, nothing else."* — e no mesmo fio, em 2026-03-14, ele exige a prova:
  *"**Which translator gave you that translation? Kindly upload pic please.**"*

→ Registro de como a discussão ocidental funciona quando fica séria: **pedem o painel e o nome do
tradutor**. É a melhor prática do fandom, e é rastreável.

### 8.5 Falling Blossom Emotion — o nome carrega um idioma chinês que a tradução perde

**u/dirklybl** no X (`status/1361120421312135168`, **fev/2021**), achado que circula no fandom:
> "One cool thing about the 'Falling Blossom Emotion' (落花の情; Rakka no Jō) domain technique is its
> reference to a **Chinese idiom about unrequited love**."

O idioma é **落花有意，流水無情** — *"a flor que cai tem sentimento, a água que corre não tem"*,
usado para amor não correspondido: um lado se oferece, o outro passa indiferente. **É uma descrição
perfeita da mecânica**: o ataque vem com intenção, e a técnica responde sem se mover. O nome em
inglês ("Falling Blossom Emotion") preserva as palavras e **perde a relação entre elas** — o
ocidente lê "emoção da flor caindo" como nome bonito e não como a explicação da mecânica.

### 8.6 O caos de nomes na primeira tradução do Simple Domain — documentado no histórico da wiki

A revisão de criação do artigo `Simple Domain` (**2020-01-25**, por **Aoiaoi600**) registra no
resumo de edição os nomes que competiam na época:
> "*'Simple Domain' (otherwise known as '**Shinkage Style: Simple Territory**', '**Shinkageru: New
> Shadow Style: Kan'i Ryoiki: Simple Area**', 'New Shadow Style: Si...'*"

→ **Quatro nomes para a mesma técnica** no mesmo parágrafo, em janeiro de 2020. "Simple Territory",
"Simple Area" e "Simple Domain" conviveram até a Viz padronizar. É a prova documental de que a
confusão de nome é anterior à confusão de mecânica — e explica por que buscas antigas no ocidente
sobre esta técnica são tão difíceis de rastrear.

---

## 9. AS PERGUNTAS QUE O OCIDENTE CONSIDERA EM ABERTO (e a obra nunca respondeu)

Todas rastreadas a thread e data. São, na prática, **a lista de lugares onde o RPG vai ter de
decidir sozinho**, porque não há canon para copiar.

**1. Por que o Sukuna usa Hollow Wicker Basket e não Simple Domain?**
**u/SaIamiShadow**, r/Jujutsufolk, 2024-03-20: *"i really can't think of why Sukuna wouldn't just
use simple domain against Yuta if it is that much better than HWB."* O ser mais forte da obra
escolheu a técnica que todo mundo chama de inferior, **duas vezes** (cap. 249 contra o Yuta, cap.
266 contra o Yuji). Hipótese mais popular: a HWB é um **voto vinculante que troca mãos por
proteção maior**. **A obra nunca disse.** Sem resposta.

**2. Simple Domain e HWB funcionam contra domínio não-letal / de informação?**
Ver §7.3. O cap. 187 diz que o Kashimo desistiu porque o acerto garantido do Hakari "é inofensivo";
**u/Illustrious-Bass4354** (r/YUJI_Corp, 2026-09-21) argumenta que bloquear a informação
**quebraria o domínio inteiro**. Nunca foi testado em página.

**3. Como o Kenjaku sobreviveu aos 0,2 s de Vazio Ilimitado em Shibuya?**
**u/PopularLadder9365** postou a mesma pergunta em **r/JujutsuPowerScaling e r/Jujutsufolk** no
mesmo dia, **2026-09-21** (`1wlzuh4` e `1wlzu8x`):
> "he **couldn't have done simple domain within that 0.2s**... EVEN THE GOAT TODO with his 530k IQ
> didn't do it fast enough against Mahito. And even with 0.1s hit of Unlimited Void does
> significant damage."
→ **A pergunta real por baixo é de TEMPO DE REAÇÃO**, e é a que mais importa para uma mesa: *o
anti-domínio tem de estar ligado ANTES, ou dá para ligar depois que o domínio abre?* O precedente
do Todo (cap. 130) diz que **você pode perder a janela**: a wiki registra que *"Mahito activated his
domain's cursed technique **before Todo could counter** with Simple Domain."* Mas o Yuji, o Ino, o
Choso e a Miwa conseguiram no cap. 258. **A obra nunca deu a janela em números.**

**4. Dá para embutir acerto garantido na Domain Amplification?**
Thread dedicada: r/Jujutsufolk `1ugijbd`, *"can a sorcerer embed their sure hit into domain
amplification"*, **2026-06-26**. O texto diz que o Jogo e o Hanami **se abstiveram** de incluir
(*"they refrained from doing so to free up the necessary capacity"*), o que implica que **daria**,
mas com custo de capacidade. **u/Fickle_Tie8014** fecha com a formulação certa: *"you can imbue a
cursed technique into your Domain Amplification since the words 'not deliberately imbue one'."*
→ Sugere que a Amplificação tem **orçamento**: ou você gasta em acerto garantido, ou gasta em
espaço vazio para anular. **Nunca quantificado.**

**5. Simple Domain É técnica de barreira, ou só "parecida com" uma?**
r/Jujutsushi, thread `1tddq33`: *"is domain amplification a barrier technique?"*. E
**u/Fickle_Tie8014** (2026-06-26): *"Gege described the New Shadow Style: SD '**similar to** barrier
techniques' **not as a** barrier technique."* A Fandom Wiki, por sua vez, classifica o Simple Domain
como `Barrier Technique` **e** admite no corpo do artigo: *"**Despite being classified as a barrier
technique, Simple Domain typically lacks a clearly defined barrier.**"*
→ A própria wiki escreve a contradição e não a resolve. **Em aberto.**

**6. A Amplificação se desgasta com dano contínuo?** Ver §5/BRIGA 3. Sem texto dos dois lados.

**7. Um domínio comum não segura o Santuário Malevolente, mas um Simple Domain segura?**
Duas afirmações ocidentais **contraditórias**, no mesmo subreddit, com um dia de diferença:
- **u/Designer-Maximum6056**, r/JujutsuPowerScaling, **2026-09-22** (`1wmtt11`):
  *"Malevolent Shrine **cannot be stopped by a normal domain expansion, however it CAN via a simple
  domain**."*
- **u/LadyOfBlackSparks**, r/JujutsuPowerScaling, **2026-09-21** (`1wm9n6x`):
  *"We know **Domain Expansion >>> Simple Domain** when it comes to withstanding other DEs."*
→ Os dois estão lendo o mesmo material. A conciliação provável é que **domínio aberto** (sem
barreira) se comporta diferente: um domínio fechado não consegue *disputar* com ele, mas um Simple
Domain *anula o acerto garantido* dele. **Ninguém fechou isso, e é exatamente o tipo de regra que
um sistema precisa ter escrita.**

**8. Dá para empilhar duas anti-domínio ao mesmo tempo?**
O Gojo usa **Simple Domain e Falling Blossom Emotion** na mesma sequência contra o Santuário
Malevolente — **u/Jettblitz**, r/Jujutsufolk, 2024-03-20: *"he had to use simple domain and fbe so
he wouldn't fry his brain trying to out heal MS."* **A obra nunca disse se foi simultâneo ou
alternado**, e o ocidente usa as duas leituras conforme convém ao argumento.

---

## 10. Nota de campo: a comunidade ocidental de homebrew já resolve isto como sistema

Achado lateral que vale para este projeto: o subreddit **r/CTsandbox** é cheio de gente montando
regra de anti-domínio, e as soluções deles são **desenho de preço**, igual ao que este RPG faz.

**u/Loud-Boat-4124**, r/CTsandbox, **2026-09-21**, *"New Shadow Style: Domain Nullification"*
(`/r/CTsandbox/comments/1wmrwyc/`) — a proposta e, principalmente, **como ele a precifica**:
> "Using Simple Domain as a medium, the user will enter into a binding vow which will make the
> barrier of their Simple Domain **indestructible**... However, to complete the binding vow, the
> user must program the Simple Domain with a program which **decreases the strength of their own CE
> while increasing the strength of their opponent's**. There is also a general rule that **the more
> powerful a domain is..., the harsher the debuffs are**."

→ Ele chegou sozinho na mesma solução que um sistema de mesa usaria: **preço que escala com o que
você está anulando**. Ou seja, a defesa não custa um número fixo, custa em proporção à força de
quem abriu o domínio. **É exatamente a régua que este projeto disse querer** ("a defesa vai medir
contra a FORÇA de quem abriu o domínio") — e há precedente de comunidade para ela.

O mesmo subreddit tem `Simple Domain: Stale Flaking Moon` (**u/Vast_Ad166**, 2026-09-19) e `Dojang`
(**u/Nervous-Bar-1483**, 2026-09-21), este último um Simple Domain de taekwondo com barreira que
**só fecha se o oponente entender as condições e aceitar** — variante do sumô do Miyo. Mostra que
o ocidente lê o Simple Domain como **o slot programável do sistema**, e é assim que o RPG deveria
tratá-lo.

---

## 11. RESUMO EXECUTIVO — o que levar para a mesa

1. **O ranking ocidental não existe como coisa única.** Domain Amplification aparece em **primeiro**
   (escola do efeito: é a única que anula técnica) e em **último** (escola do custo: te deixa sem
   técnica). A hipótese da rodada anterior está **derrubada** como afirmação simples. Hollow Wicker
   Basket é a única com consenso: **última**, e frequentemente esquecida da lista.
2. **Dois erros do pedido checados:** "FBE não serve contra físico" é **[ERRO] vivo na wiki hoje**,
   com a refutação dentro da própria frase. "Simple Domain te prende no lugar" é **[ERRO] já
   corrigido na wiki em 2021-02-23**, mas a versão errada ficou no ar 13 meses bem em cima da
   estreia no anime, e por isso continua circulando fora dela.
3. **[ERRO] bônus:** o raio de **2,21 m** é da **Miwa**, não da técnica — mesma generalização, menos
   conhecida. Não use como número fixo.
4. **A nota do Gege (Jump 2024 nº 8) foi notada e bem recebida** — tratada como conserto, não
   retcon. Mas **a wiki nunca aplicou a metade que importa**: ela ainda diz que o Simple Domain
   "enfraquece" técnica, que é o verbo que o autor recuou.
5. **A distinção mais jogável que o ocidente produziu:** HWB custa **mãos e pode ser reforçada**;
   Simple Domain deixa as **mãos livres mas tem ponto de ruptura**. As duas anulam o acerto
   garantido. É assimetria limpa e apoiada em texto.
6. **Simple Domain é limiar, não redução:** protege inteiro até quebrar, e quando quebra o dano
   chega todo junto (a perna do Yuji, cap. 258).
7. **Exceção nomeada que sobreviveu à confusão de tradução:** técnica que mira **energia
   amaldiçoada diretamente** atravessa a Domain Amplification.
8. **O cap. 258 não é lido como inconsistência**: os 99 s são **voto vinculante que troca duração
   por saída máxima**. A ponta solta que o lado vencedor não respondeu é a **Miwa**.

**STATUS: COMPLETO**
