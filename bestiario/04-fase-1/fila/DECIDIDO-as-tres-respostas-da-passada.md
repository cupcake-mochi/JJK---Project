# DECIDIDO — o golpe mora nas Ações, `Ações Múltiplas` é entrada, e a rota do orçamento

*11/09/2026, fim da tarde. As respostas do Mizuki às três perguntas que a passada de texto do livro deixou
(`08-livro/PASSADA-3-texto.md`, capítulos `50` e `60`, e os dois "conferir" do `30` e do `40`).*

---

> ## ✅ EXECUTADO em 11/09/2026, na sessão seguinte. As três saíram, e tudo regerou verde.
>
> | § | onde entrou |
> |---|---|
> | **`1`** | cap. `50` *(cabeçalho sem o golpe · como se nomeia o ataque · `Ações Múltiplas` conta na linha)* · cap. `90` *(a trava)* · `gerar-as-seis.py` e `gerar-exemplo.py` *(o cabeçalho das seis e da Ubume)* · `03-bloco/RASCUNHO-5` *(o molde, com a medição dos `7` sistemas)* · `Claude 2/…/make.js` *(o cabeçalho das prontas + a nota de nome na ficha em branco)* ⟹ **`bloco-de-inimigo.docx` e `.pdf` regerados** |
> | **`2`** | `ferramentas-claude-2/rota-b-26.py` — **um script que reabre os donos e reescreve os três lugares**: a tabela do §6.5 da peça `26`, a mesma tabela no cap. `60` do livro, e a conta da checagem `9.1`. *De quebra, a `Condição na maior ação` do cap. `60`, que subtraía de `15`* |
> | **`3`** | `07-catalogo/PESQUISA-03b-o-erro-da-morte-do-naoya.md` — **o laudo.** *O cap. `30` do livro e o `03` do catálogo corrigidos; o `40` conferiu e ficou; o `04` do catálogo trocou "plantado" por "deixado"* |
>
> **`29` validadores do `Claude 2` verdes · `conferir-voz.py` em `0` · os dois PDFs do livro regerados.**
> ⚠ *Nada foi commitado nem empurrado — a árvore do `Claude 2` está suja, esperando o martelo dele.*

---

## 1 · O golpe e as `Ações Múltiplas`

> ***Palavras dele:*** *"Golpe fica na parte de ações, normalmente com um nome pro golpe, como "Ataque de X
> (arma)" - "Ataque de Taco" "Ataque de Calda" e talz, ja o ações multiplas e sobre o ações multiplas, sim,
> fica logo acima dos ataques, como entrada, mas apenas caso tenha multiplos golpes"*

**A leitura:**

| | decidido |
|---|---|
| a célula `O golpe` | **sai do cabeçalho.** O golpe aparece em `Ações`, como ataque com nome |
| o nome do golpe | o formato normal é **`Ataque de ‹ arma ›`** — `Ataque de Taco`, `Ataque de Cauda` |
| `Ações Múltiplas` | **conta como entrada** da linha de entradas nomeadas, e fica logo acima dos ataques |
| quando existe | **só em quem tem mais de um golpe por rodada** — igual à regra de hoje |

⚠ **Perguntado na mesma hora** se as seis prontas trocavam os nomes de hoje pelo formato `Ataque de X`.

> ***Palavras dele:*** *"Ataque de X é um exemplo, pegue de outros sistemas o como eles formam e afins"*

### Como os sistemas nomeiam o ataque — medido

*Contado nos dados que o projeto já tem em disco, e conferido na web onde não tinha.*

| sistema | como nomeia | exemplos | onde o ataque fica |
|---|---|---|---|
| **D&D 2024**, SRD (`fila/srd-2024.json`) | a arma, a parte do corpo ou o próprio golpe — **`0` de `423` ações de ataque com "Attack" no nome**; `331` de uma palavra | `Bite` `81` · `Rend` `60` · `Claw` `29` · `Slam` · `Longbow` | nas Ações. *Multiattack:* "makes three Rend attacks" |
| **D&D 2014**, SRD (`fila/srd-2014.json`) | o mesmo — **`0` de `524`** | `Bite` `140` · `Claw` `54` · `Tail` `32` | nas Ações. *Multiattack:* "one with its bite and two with its claws" |
| **D&D 5e em português** (`Manual dos Monstros`, PDF em disco) | o mesmo | `Mordida` · `Garras` · `Pancada` · `Constrição` · `Maça Estrela` | nas Ações. *Ataques Múltiplos:* "realiza dois ataques de pancada" |
| **Pathfinder 2e em português** (`Livro Básico`, PDF em disco) | a arma ou a parte do corpo, minúscula, com os traços | `mandíbulas (acuidade)` · `garra (ágil)` · `casco` · `ferrão` | na linha `Corpo a Corpo` |
| **Tormenta20** ([wiki de ameaças](https://tsrd.fandom.com/pt-br/wiki/Amea%C3%A7as_T20)) | o mesmo, com a contagem na frente | `4 garras +26 … e mordida +26` | na linha `Corpo a Corpo` |
| **Draw Steel** (`fila/dados-recarga-area/`) | nome de habilidade, frase curta — **`3` de `2076` habilidades de golpe com "Attack"** | *(ver a saída)* | nas habilidades |
| **Daggerheart** ([SRD](https://daggerheartsrd.com/adversaries/jagged-knife-bandit/)) | a arma | `Daggers` | ⚠ **no cabeçalho**, na linha `ATK` — **o contrário do que o Mizuki decidiu** |

**Nenhum sistema medido põe "Ataque de" no nome.** O nome é a arma ou a parte do corpo (`Mordida`, `Garra`,
`Kanabō`), ou o golpe quando ele tem jeito próprio (`Pancada`, `Dilacerar`). **O "ataque de" aparece na
frase das `Ações Múltiplas`** — "faz três ataques de Kanabō" —, que é onde o exemplo dele ("Ataque de Taco")
se encaixa.

**⟹ As seis prontas já seguem o padrão, e nenhuma troca de nome:** `Pisada`, `Foice`, `Mordida`, `Língua`,
`Kanabō` e o `Fogo-de-Raposa` da `Kitsune`; e a `Garra` e o `Choro` da Ubume. *O `Stomp` e o `Tongue` do D&D
são os mesmos nomes da `Pisada` e da `Língua`.* **O que muda é o molde do capítulo 5, que passa a dizer
como se nomeia.**

**Onde mexe:** o capítulo 5 (o bloco em branco, *Linhas de defesa*, *Linha de entradas nomeadas*), o
cabeçalho das seis no capítulo 8 (`gerar-as-seis.py`), o cabeçalho da Ubume no capítulo 6
(`gerar-exemplo.py`), o `90` (a trava das entradas), o `03-bloco/RASCUNHO-5-o-bloco-em-branco.md`, e no
`Claude 2` o `make.js` do gerador de inimigo e o `bloco-de-inimigo.docx`.

## 2 · A rota do orçamento de uma ação

> ***Palavras dele:*** *"Siga a melhor rota validada"*

**A pergunta era:** o orçamento de feitiço de uma ação sai com o `0,923` **depois** da média do golpe cru
(peça 26 §6.5, checada pela `9.1` do `conferir-bestiario.py`), e o golpe impresso sai com o `0,923` **antes**
do dado (`make.js`). A diferença é `0,1` ponto em `3` células.

**Decisão:** medir as duas contas contra os donos — o texto da regra, a definição do golpe e o golpe que a
mesa lê — e seguir a que fecha com eles. **Medido em 11/09** — `fila/medir-a-rota-do-orcamento.py`, saída em `SAIDA-a-rota-do-orcamento.txt`. *Cada
número lido do dono: a tabela `Inimigos` do `partF.js`, as categorias e o `0,923` da peça 26, e a função
`dado()` do `make.js`.*

| | **conta A** — o fator depois da média do golpe cru | **conta B** — a média do golpe impresso |
|---|---|---|
| bate com a tabela publicada (peça 26 §6.5) | `35` de `35` | `26` de `35` |
| o que a peça 26 §6.5 escreve embaixo da tabela | — | *"O golpe entra aqui como a ficha imprime ele — a média do dado do §4.4"* |
| o que o comentário da checagem `9.1` diz | — | *"o golpe entra como a ficha imprime ele"* |
| volta: pontos × `4,5` contra a média do golpe impresso | erro de até `0,60` de dano, médio `0,194` | erro de até `0,20`, médio `0,108` — só o arredondamento de uma casa |
| a regra do capítulo 6 ("o golpe dividido por `4,5`") aplicada ao golpe que a mesa lê | só bate onde as duas contas coincidem | bate sempre |

**A rota validada é a B.** *A tabela e a checagem `9.1` fazem a conta A, e o texto da peça e o comentário
da própria checagem descrevem a B.* **Um mestre que aplica a regra ao golpe impresso chega na B.**

**As `9` células que mudam** (e não `3`, como o agente dos blocos tinha contado — só a primeira coincide):

| nível | categoria | publicado | a conta B |
|---|---|---|---|
| `10` | `Catástrofe` | `4,5` | `4,6` |
| `15` | `Calamidade` | `7,6` | `7,7` |
| `20` | `Catástrofe` | `9,0` | `9,1` |
| `25` | `Desastre` | `12,5` | `12,4` |
| `25` | `Catástrofe` | `11,2` | `11,3` |
| `25` | `Calamidade` | `12,5` | `12,4` |
| `30` | `Desastre` | `15,0` | `14,9` |
| `30` | `Catástrofe` | `13,5` | `13,4` |
| `30` | `Calamidade` | `15,0` | `14,9` |

⚠ **"A maior ação do sistema" vai de `15,0` para `14,9` pontos** — o `Desastre` e a `Calamidade` do nível 30.
*Os `62%` do teto do jogador (`24`) não mudam.*

## 3 · As duas frases de canon marcadas pra conferir

> ***Palavras dele:*** *"Pode pesquisas e colocar, eu coloquei algumas skills no ambiente que vão servir pra
> sua escrita, mantenha a metodologia nova que veio com a att do livro"*

**Decisão:** pesquisar na obra, com fonte registrada e as quatro perguntas de validação do catálogo
(inferência conferida · contra-exemplo · status que mudou depois · classificação), e pôr o resultado no
texto dos capítulos `3` e `4`, na régua da passada 3 (`GUIA-titulos-e-texto.md` + `REGRA-DE-VOZ.md`).

| capítulo | a frase |
|---|---|
| `30` | *"Na obra, os feiticeiros que morreram e não voltaram como maldição foram mortos com energia amaldiçoada."* |
| `40` | *"A prisão de menores, a ponte, a casa do garoto e a escola do primeiro capítulo são quatro lugares com o mesmo desenho: um dedo deixado ali, e o dedo atraindo as maldições."* |
