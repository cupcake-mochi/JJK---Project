# A FILA — o que falta, e o que já estava respondido

*10/09/2026. **Este arquivo é a fila. Os outros são o porquê.***

> ### 🆕🔴 ITEM `31` — a peça 15 calibra a morte do shikigami contra a `Dupla`
> **`fila/MEDIDA-a-peca-15.md` · conta em `fila/medir-a-peca-15.py`** *(o 28º)*.
>
> **Peça de REGRA VIVA, e ela não estava em lista nenhuma.** *O teto que ela mediu caiu `1,51×`, a
> conclusão dela quebra na metade (nada destrói um corpo forte num golpe único) e `2` de `4` linhas
> da tabela do corpo machucado mudam.* ⚠ **Não é do Bestiário resolver — a conta está entregue.**
>
> ### ⚠ E a minha varredura de hoje estava incompleta: `104` linhas em `9` arquivos, não `24` em `2`.
> *`4` arquivos fora de lista: `15-invocacoes.md` · `ESTADO-ATUAL.md` · `mesa-01-grupo-01.md` ·
> `COMO-USAR.txt`.*

> ### 🆕🔴 ITEM `30` — as `6` maldições PRONTAS, e ele é o único item ABERTO com martelo dentro
> **`fila/MEDIDA-o-remapeamento-das-seis.md` · conta em `fila/medir-a-dupla.py`** *(o 27º)*.
>
> | | |
> |---|---|
> | ✅ **`4` das `6` são execução pura** | `Betobeto`·`Hitotsume` ⟹ **`Ameaça`** · `Tsuchigumo`·`Oni` ⟹ **`Desastre`**. *`29`/`29` em vida, dano, ações e golpe — nenhum número se move* |
> | ~~`30a`~~ · a `Kamaitachi` | ✅ **MARTELADA: duas `Ameaça`.** *A ficção dela já era dois corpos. Custa `−25,0%`, que é o `0,75×` do §4.3* |
> | ~~`30b`~~ · a `Kitsune` | ✅ **MARTELADA: saída `F`, sobe pra `9 a 12` e vira `Ameaça`.** *`4,2` pontos contra os `4,2` publicados — `+0,5%`, e a característica dela não muda uma letra* |
> | ⏳ **`30c` · o repositório** | **`24` linhas varridas** — `13` no `dados.js`, `11` no `make.js`. ⚠ *não está na `MEXIDAS-no-repositorio.md`, e uma delas é CÓDIGO* |
>
> ### ❌ E ele derrubou uma leitura publicada: `Alcateia ⟹ Capanga` erra `12,00×`. É `⟹ Desastre`.
> ### ⚡ E a `Dupla` não ficou órfã: ela foi MORTA de propósito, e já estava escrito em dois arquivos.
> ### ✅ OS DOIS MARTELOS CAÍRAM em 10/09 (noite) — `fila/DECIDIDO-as-seis-prontas.md`.
> **Sobra só o `30c`, e é execução.** *`6` de `6` fichas dentro da banda, conferidas pelo `§10` do
> script, que LÊ a decisão do `DECIDIDO` e morre se ela mudar.*

> ### ⚠⚠ ATUALIZADO DE NOVO — o item `17` foi medido, e ele reabriu a BANDA
> **`fila/MEDIDA-o-capanga.md`.** *O topo `32%` da banda **é o `Capanga` calculado com um fator que a
> própria escada substituiu**. Com o fator vivo ninguém encosta em `32%` — o topo real é `27,7%`, e a
> banda medida em `29` níveis × `5` categorias é **`21,8%`–`27,7%`**.*
> **E o piso `20%` ficou órfão:** *ele existia por causa do corte de dano do `Controlador`, e a forma
> `B` tirou esse corte.* **Três martelos abertos, todos com a conta pronta — `§ OS TRÊS MARTELOS` no fim.**

> ⚠ **Atualizado em 10/09 depois do teste de ponta a ponta.** *O item `7` fechou, e ele trouxe `4` itens novos — `10` a `13` — mais um aviso, o `14`, e um item dele, o `15`.*
> **E na mesma sessão o `12` já fechou (contagem de `836` ações de recarga) e o `10` e o `11` viraram martelo dele, com a conta pronta.**

---

# ✅ PRIMEIRO: "como o mestre cria as ações do inimigo?" JÁ ESTÁ RESPONDIDO

***Pergunta do Mizuki, 10/09/2026:*** *"a gente tirou o gasto de PE do inimigo, mas n formulo. Como
vai ser pro inimigo criar as ações? se o mestre quer uma ação q dá condição? se o mestre quer uma ação
que ataca diferente de outra? e se for em área?"*

**As quatro estão respondidas na peça 26 §6.5, fechada na v0.205.** *E eu quase respondi que não
estavam.*

## A regra, em uma linha

> ### **O orçamento de feitiço de uma ação é o golpe dela dividido por `4,5`.**
> *E o Fundamento — a mesma máquina que o jogador usa — faz o resto.*

**`4,5` não é número novo:** *é o que a peça 19 §2.1 publica — "cada ponto que não vira Melhoria vira
`1d8`, que são `4,5` de dano".*

## As quatro perguntas, uma a uma

| a pergunta | a resposta, e onde ela está |
|---|---|
| **como cria a ação?** | **golpe ÷ `4,5` = os pontos daquela ação.** Daí o mestre monta no Fundamento, igual a um feitiço de jogador |
| **e se ela dá condição?** | *"Comprar condição dentro de um feitiço custa ponto, e **ponto gasto em condição é dado que não foi comprado**. A régua da peça 19 §2.2 vale dos dois lados da mesa desde a v0.201, então **o preço já está escrito lá**."* |
| **e se uma ação ataca diferente da outra?** | **cada ação tem o orçamento DELA** — o golpe dela ÷ `4,5`. Duas ações do mesmo bloco são duas montagens diferentes |
| **e se for em área?** | *"**área reparte a cota, e não multiplica ela**"* — e o próprio Fundamento já cobra por área em ponto de feitiço. *Foi o Mizuki que levantou isso: "um feitiço em área vai ter menos dados para poder comprar condição"* |

**E tem piso:** *`seco` — abaixo de `13,5` de dano (o custo de uma `Classe 1`) o inimigo **não monta
feitiço nenhum**: ele bate, e o golpe sai como o §4.4 manda.*

> ### ⟹ O inimigo não precisa de preço próprio, porque o Fundamento já cobra por área, por condição e por Melhoria — em ponto de feitiço.
> **Tirar o PE tirou o POÇO, não a máquina de montar.** *O ponto de feitiço continua sendo moeda de
> CONSTRUÇÃO; o que sumiu foi a moeda de MESA.*

---

# ⚠ MAS TRÊS COISAS QUE A GENTE DECIDIU MOVERAM O §6.5

## 1 · A tabela de pontos por ação está na escada VELHA

**O §6.5 publica `pontos por ação` para `Ronda` · `Dupla` · `Alcateia` · `Calamidade`.** *Essas
categorias morreram — a escada nova é `Capanga` · `Ameaça` · `Desastre` · `Catástrofe` ·
`Calamidade`.*

**É trabalho mecânico** — `golpe ÷ 4,5` para cada linha da `TABELA.md` —, **mas tem que ser refeito.**

## 2 · E a recalibração da `Intervenção` move a tabela DE NOVO

**Quem tem `Intervenção` levou `× 0,923` no dano.** *Então `o golpe` mudou, e `golpe ÷ 4,5` muda junto.*

*Exemplo: o `Desastre` nv30 tinha golpe `73,0` → `16,2` pontos. Com o `0,923` ele vai pra `67,4` →
**`15,0` pontos**.*

## 3 · ⚠⚠ E ESTA É UMA CONTRADIÇÃO DIRETA, não um ajuste

**O §6.5 escreve, sobre a ação fora do turno:**

> *"**a trava é uma só: as ações fora do turno saem das que ele já tem pelo §4.2, NUNCA POR CIMA.**"*

**E a gente decidiu o contrário em 10/09**, com as duas ideias que o Mizuki pôs como fixas:

> *`1` — Inimigo tem ações.*
> *`2` — **Intervenções são ações extras em meio aos turnos dos alvos. Nenhum sistema come ação do
> turno para ter essas "intervenções", e é por um motivo.***

| | o §6.5 | a decisão de 10/09 |
|---|---|---|
| a ação fora do turno | **sai das que ele já tem** | **é extra, por cima** |
| e ela se paga | de graça — *medida em `0,94×` a `1,07×` sobre `81` durações de luta* | com o **fator `× 0,923`** no dano de quem a tem |

> **As duas são coerentes por dentro. A nossa é mais nova e segue a ideia fixa do Mizuki.**
> **⟹ O §6.5 precisa perder aquela frase, e ganhar o `0,923` no lugar.**

---

# A FILA — **do mais CARO pro mais BARATO**

*Reordenada em 10/09/2026, a pedido dele. **Custo = quanto trabalho ela dá, não quanto ela importa.***

> **A numeração dos itens NÃO mudou** — o `15` continua sendo o `15`. *Só a ordem da lista mudou, senão
> as referências dos outros arquivos quebram.*

---

## 🔴 CARO — pede régua nova, ou mexe nos dois lados da mesa

| ordem | # | item | o que faz ela ser caro |
|---|---|---|---|
| ~~**1º**~~ | ~~`15`~~ | ✅✅ **FECHADO em 10/09 — o lado do jogador também** | ⚡ **O LADO DO INIMIGO FOI MEDIDO em 10/09 — `fila/DECIDIDO-o-arredondamento-e-a-area-do-inimigo.md` §2-3.** *E a medição inverte a intuição: a nossa base de `3 m` cobre **`13` quadrados**, quase o dobro da mediana `CR 0–1` do D&D (`4,5`) e acima da do Draw Steel (`9`).* ⚠ **O que está fora de escala é o TOPO:** *`15 m` cobre `314` quadrados contra `72` da mediana `CR 17+` do D&D.* ✅ **A área natural do inimigo fechou: `3 m` · `4,5 m` · `6 m` por CATEGORIA, e para no `6 m`** — *quatro pessoas espalhadas cabem num raio de `4,4 m`; área maior pega cenário, não gente.* ✅✅ **E O LADO DO JOGADOR FECHOU em 10/09 (noite), martelado por ele.** *As duas pontas da queixa original — "`3 m` é nada KKK" — foram respondidas por medição:* **`1`** `3 m` de raio cobre `13` quadrados, **quase o dobro da mediana `CR 0–1` do D&D** — não é pequeno, LÊ pequeno, porque é raio escrito em metro; **`2`** a saída `C` do item `23` conserta a leitura imprimindo a grade junto; **`3`** o espalhamento entre as formas mediu **`2,79×`, idêntico ao D&D 2024**. ⟹ *não havia o que consertar no tamanho — havia o que consertar na LEITURA dele* |
| **2º** | ~~`9`~~ | ✅✅ **FECHADO — martelo `B`: fica o `Capanga` da ESCADA.** `fila/DECIDIDO-o-capanga-unico.md`. *O projeto tinha **dois** `Capanga` com o mesmo nome — o da peça 26 (`4` corpos, `chefe÷4`) e o da escada (`8` corpos, `chefe÷12`), com razão estável de `3,00×` em vida.* **Fica o da escada** — o outro era o capanga da `Alcateia` morta. ✅ **A régua saiu:** `fator do encontro = fator do chefe + capangas × 0,083`, e a tabela nova do §4.5 é `100%` · `91,5%` · `83,0%` · `74,5%`. ⚠ **E o câmbio não é linear:** `1/12` por corpo até `3`, `≈1/6` de `4` a `7`. ⏳ **`5` mexidas na peça 26 — vão no mesmo commit dos itens `5`, `6` e `11`** |
| **3º** | ~~`5`~~ | ✅ **DECIDIDO em 10/09 — `fila/DECIDIDO-o-degrau.md`.** *Medido: o degrau vai de `1,000×` a `4,000×`, e **`3` dos `4` preços não cabem em degrau nenhum** — a imunidade a `Físicos` erra `40%`, a Expansão erra `21,9%`.* ⚠ **E duas frases publicadas do §6.4 são da escada MORTA.** ✅ **A moeda passa a ser o FATOR, que é contínuo** — `fator × o multiplicador`, e a leitura sai de graça porque `personagens = fator × 4`. **E o argumento já estava publicado no próprio §6.4:** *"a categoria mede pessoas, e o número existe fora da escada do mesmo jeito"*. ⚠ **`0` de `4` sistemas do campo têm degrau uniforme** *(espalham `1,93×` a `24,25×`)*. ⏳ **As `5` mexidas estão escritas — e são no REPOSITÓRIO, vão com o `6` e o `11`** |
| **4º** | ~~`11`~~ | ✅ **MARTELADO por ele em 10/09: `1` ação em área à vontade, e `Recarga` NÃO conta na cota** · `fila/DECIDIDO-o-aperto-e-a-area.md` §2. *Medido: com `2` ações em área o alvo termina a luta com `0,3%` de vida; com `1` ele leva `~50%`.* ⚠ **E o §4.6 foi conferido — `fila/CONFERIDO-o-4-6-contra-a-area.md`:** o `2,70` **não existe em área** (concentrar é curva, área é penhasco). *Validado fora: o Dragão Ancião é `CR 11` sem o sopro e `CR 28` com ele à vontade.* ⏳ **Sobra só a mexida no §6.5, no commit com o `5`, `6` e `9`** |

---

## 🟡 MÉDIO — trabalho mecânico grande, sem régua nova

| ordem | # | item | o que ela pede |
|---|---|---|---|
| **5º** | **`8`** | **as mexidas da `Sobrecarga` no repositório** | **três donos do texto e cinco dependências.** *A lista e a ordem que não trava o commit já estão escritas* — `sobrecarga/MEXIDAS-no-repositorio.md`. **É execução, não decisão** |
| **6º** | ~~`16`~~ | ✅ **FECHADO em 10/09 — saída `F`, o `tamanho` NÃO COBRA NADA** · `fila/DECIDIDO-o-tamanho.md`. *Ele mandou medir duas vezes em vez de escolher, e a medição derrubou a premissa: o preço em Defesa era invenção nossa.* **`AC` espalha `1,000×` em `4.791` criaturas do PF2e e `1,016×` em `331` do D&D; o Draw Steel não tem defesa.** ✅ **Já aplicado no `RASCUNHO-5` Passo `3` e nos scripts.** ⚠ *Sobra declarar os `≈18%` que ele põe fora da conta — e o `RASCUNHO-5` já declara* |
| **7º** | **`6`** | **tirar *"nunca por cima"* do §6.5** e corrigir o `0,70×` da cura pra `0,64×` | baixo em conta, **mas é mexida no repositório** — e ela **vai junto com o `11`**, porque as duas mexem no mesmo §6.5. *Fazer as duas de uma vez é um commit em vez de dois* |

---

## 🟢 BARATO — uma linha escrita, ou martelo dele com a conta já pronta

| ordem | # | item | por que é barato |
|---|---|---|---|
| **8º** | ~~`1`~~ | ✅ **FECHADO — linha própria, condicional, e ela é LIVRO-CAIXA.** *Na estreia pegou o Sukuna com `3` votos e Essência pra `2`; a obra resolveu — só `2` são permanentes, o terceiro é de estado (mão perdida) e o "depois de Desmembrar e Clivar" não é voto, é condição de ativação.* · `fila/DECIDIDO-o-pacto.md`. *Ela vai contra a forma do campo (`38%` dos blocos do D&D têm zero traços — lista variável já resolve opcional), e o argumento que ganhou é o do ORÇAMENTO: pacto custa `0,50` fatia e traço anônimo não faz ninguém conferir* | **é escolha, não conta:** vira `Traço`, ou linha que só aparece quando existe. ⚠ *E o Sukuna mostrou que ele é o **caso limite**: os votos vinculantes dele **são** a mecânica dele — `Chama Divina` só depois das outras duas, barreira aberta compra alcance, três condições no corte do mundo* |
| **9º** | ~~`2`~~ | ✅ **A PESQUISA FECHOU — `15` linhas novas, e as duas que quebravam o bloco foram MEDIDAS.** *`fila/PESQUISA-pendente-o-pacote-de-tipo.md` + `fila/MEDIDA-a-morte-e-a-imunidade.md`.* **A condição de morte é traço nomeado** *(`3,7%`–`5,3%` em `1.093` blocos, `0` de `3` sistemas dão célula)*; **a imunidade da `maldição` custa `1,00×`** *(`8` de `8` rotas de personagem já têm porta grátis)*; **o pacote inteiro vai pro capítulo** *(ele come até `150%` da linha de entradas nomeadas)*. ✅ **E as duas escolhas de sabor FECHARAM** — `fila/DECIDIDO-o-pacote-de-tipo.md`: os núcleos são **partição** com `N` padrão `1` *(traço `Núcleos (N)`, `1,00×`)*, e o `feiticeiro` que vira maldição é **LORE**. 🆕 **E ele abriu o lado de LORE do Bestiário — modelo Volo's Guide.** |
| | ~~`2a`~~ | ✅ a COLETA do repositório — `fila/MEDIDA-o-pacote-de-tipo.md`. *Os quatro exemplos dele **já estavam publicados** (peça 25 §4.4 · peça 9 §5 · peça 13 · peça 26 §6.2) — não era escrever, era COLETAR. E o `feiticeiro` fechou: **"tem técnica garantidamente"**, o humano do D&D.* ✅ **E o `corpo amaldiçoado` e o `shikigami` que ele lembrou TAMBÉM estavam lá** (peça 9 §5 · peça 15). **`6` de `7` tipos vieram do repositório — zero pesquisa externa** | **é lista dele.** *A direção já está dada em 10/09 — maldição toma Energia Reversa, restringido passa por barreira, civil e restringido não veem maldição sem item, sem técnica não tem técnica.* **Falta ele fechar, e `feiticeiro` está em branco** |
| **10º** | ~~`13`~~ | ✅ **FECHADO — parêntese de pré-requisito** · `fila/DECIDIDO-o-gatilho.md`. *Não é quinto rótulo: os três sistemas separam frequência de pré-requisito (`limited_to_form` · `Requirements` · `Trigger:`), e o bloco já tinha a forma no `(Ação Bônus)`* | *"só depois de `Desmembrar` e `Clivar`"* não é nenhum dos quatro rótulos. **É decisão: quinto rótulo, ou texto da ação?** *E o `ESTADO` já diz que `8` de `9` sistemas usam "rótulo de frequência **ou gatilho**" — o gatilho só ficou fora da nossa lista* |
| **11º** | ~~`14`~~ | ✅ **MARTELADO por ele em 10/09** — `fila/DECIDIDO-o-aperto-e-a-area.md` §1, texto v2 em `fila/RASCUNHO-a-linha-do-aperto-de-atributo.md`. *A concentração `1,92×` está DENTRO da banda do campo (`1,80×`–`1,98×`, `5.877` bichos), e **"é do nível alto" saiu** — no D&D 2024 ela DESCE.* 🆕 **E entrou a porta da `Destreza`:** a técnica declara qualquer um dos cinco (peça 1 §5), e se declarar `Destreza` as três derivadas leem o mesmo atributo — a cor vai de `3` pra `8` pontos |
| **12º** | ~~`10`~~ | ✅ **FECHADO por MEDIÇÃO em 10/09** — `fila/MEDIDA-o-controlador-no-esquadrao.md` e `DECIDIDO-o-capanga.md` §3. *Ele não escolheu: mandou medir contra o Draw Steel.* **Forma `B`, e o `Controlador` no esquadrão usa `ações = 8`** — ganha `1,125×`, paga `vida × 0,889`, a `3,1%` do `0,917×` que o `Controller` deles mede em `415` statblocks. **E a banda foi junto: `21%`–`28%`** |
| **13º** | ~~`17`~~ | ✅ **o `Capanga` foi MEDIDO** — `fila/MEDIDA-o-capanga.md` | *Era meia hora de regex, e as duas frases da fila estavam erradas: o fator `0,33` é da tabela MORTA da escada — a fechada e a `TABELA.md` implementam `0,25`, e **ele É uma `Ameaça` com outra vida**.* **`o golpe` dele está dentro da banda em `4` de `4` níveis.** ⚠ **Mas ele trouxe `3` martelos** — ver abaixo |

---

## 🆕 § DOIS ITENS NOVOS — achados montando as fichas de teste nv`7` (10/09)

*`06-playtest/FICHAS-teste-nv7-oni.md`. **Os dois saíram de rodar a máquina, não de ler documento.***

## ~~Item `20`~~ — ✅ **FECHADO, e ele CORRIGIU o que eu tinha publicado**

**`fila/DECIDIDO-o-emboscador-e-a-ameaca-seca.md` §1.** *Eu publiquei que o `Emboscador` num corpo de
`1` ação furava o invariante em `27,7%`.* ### **Não fura — o erro foi do meu script.**
*A `A-TABELA` §6 já tinha a tabela por categoria, e ela dá `1,476 × 0,677 = 0,999` num corpo de uma ação.*

**Mas dois buracos reais saíram, e os dois já estão consertados:**
`1` a tabela do §6 **não tinha linha de `Capanga`** *(ele tomou papel no mesmo dia, depois dela)* — **entrou**.
`2` o resumo do §4 e o `RASCUNHO-5` imprimiam **só o `0,863` do `Desastre`**, com um *"varia por
categoria"* em itálico — **os dois passaram a imprimir as quatro linhas.**

> **O `Emboscador` é o único dos seis cujo pagamento muda por categoria.** *Um número certo no lugar
> errado engana igual a um número errado.*

## ~~Item `21`~~ — ✅ **FECHADO: a `Ameaça` seca não é defeito, falta uma LINHA**

**`fila/DECIDIDO-o-emboscador-e-a-ameaca-seca.md` §2**, medido em `276` bichos de `CR 0–1` + `437` do
Draw Steel.

| | com `1` entrada ou menos |
|---|---|
| D&D 2024 `CR 0–1` | **`25,2%`** |
| Draw Steel nv`1–2` | **`30,4%`** |
| **Draw Steel, os `minions`** | ### **`45,7%`** |

**Um botão só é normal no nível baixo. E a mediana é `1` ação + `1` TRAÇO PASSIVO** — *`Pack Tactics`,
`Keen Smell`, `Amphibious`, `False Appearance`.* **Nenhum é habilidade de dano.**

> ### ⟹ O piso `seco` FICA. Entrou a linha "o bloco seco" no `RASCUNHO-5`.
> ⚠ *E o alerta "inimigo com um botão só" do `ESTADO` continua valendo — **no CHEFE**. A ficha que o
> campo reclama é `CR 12`.*

---

# § ~~ITEM `22`~~ — ✅ **FECHADO: não era folga, era ARREDONDAMENTO**

**`fila/DECIDIDO-o-arredondamento-e-a-area-do-inimigo.md` §1.** *Os `6,1%` moravam inteiros em `10`
níveis, e eram um quarto de ponto de vida:* **a `TABELA` publicava `69` onde a fórmula pede `68,75`, e
`79` onde ela pede `78,75`.** *Isso punha o esquadrão vivo numa rodada a mais — `79,2%` em vez de `67,9%`.*

> ### ⟹ A vida do `Capanga` arredonda PRA BAIXO. ✅ Já aplicado na `TABELA.md`, `10` linhas.
> *Média com o piso: `67,7%` contra o alvo `67,5%` — `+0,3%`.*
> ⚠ **Terceira vez que este defeito aparece** — a peça 26 §8 já registra o mesmo no chefe do nv`2`.

---

---

# ✅ E o que JÁ FECHOU — pra não reabrir

| # | item | onde |
|---|---|---|
| ~~`3`~~ | a tabela de `pontos por ação` refeita na escada nova | `fila/A-TABELA-pontos-por-acao.md`. *Achado: a escada nova topa em `15,0` pontos contra os `24,2` da `Dupla` morta* |
| ~~`4`~~ | a `Recarga (5-6)` — ela **ocupa** uma ação, não vem por cima | `fila/DECIDIDO-a-recarga.md`. *`k ≈ 1,0×` do turno cheio, e o ganho é ÁREA* |
| ~~`7`~~ | **refazer o Sukuna** — o teste de ponta a ponta | `05-sukuna/`. *A máquina preencheu o bloco sem inventar número, e achou `4` contradições* |
| ~~`12`~~ | a `Recarga` de alvo único | `fila/A-DECISAO-da-area-e-da-recarga.md` §12. **`784` de `836` são em área — `93,8%`** |
| ~~`18`~~ | as duas frases do `LEVANTAMENTO-pe.md` | virou caixa de correção no topo do arquivo |

---

## E o que NÃO está na fila, pra não voltar a perguntar

| | por quê |
|---|---|
| **como o inimigo monta ação, condição, área** | ✅ **respondido** — peça 26 §6.5, `golpe ÷ 4,5` e o Fundamento faz o resto |
| **o inimigo que se cura** | ✅ **respondido** — §6.5: empata em `315`, cura vale `0,70 × H` de dano. *Declarado e liberado, não proibido* |
| **a condição que o INIMIGO põe num personagem** | ✅ **respondido** — §6.5: empata quando `alvos × ações negadas = 4 × ações gastas`. *Em alvo único nenhuma compensa* |
| **`dano por rodada` como célula do bloco** | ❌ **não deve existir** — é `o golpe × ações`, e derivável não ganha célula |
| **`idiomas` e `sentidos` como campo** | ❌ **não abrem campo** — `FALTA-5` e `FALTA-6` do `campo-ficha.md`. O `tipo`/`grau` carrega o primeiro, `Traços` carrega o segundo |
| **a `fase` de chefe** | ❌ **fora do escopo**, por decisão dele. *Vida partida, ferramenta de mestre, fim do livro* |

---

# O detalhe do item `15` — o TAMANHO da área

***Palavras dele, 10/09/2026:*** *"Uma coisa q acho bom anotar pra fila, é questão de área, vamos olhar
isso depois, **3m é nada** KKK e isso tbm vale pra ficha de players, vamos ver depois, so deixe anotado."*

**O que está publicado hoje** *(`manual/gerador/partC.js`, "Base por Classe" e "Escadas")*:

| | base | a escada sobe |
|---|---|---|
| `Explosão` (a esfera) | **raio `3 m`**, num ponto a até `18 m` | `3 → 4,5 → 6 → 9 → 15 m` |
| `Cone` | `4,5 m` saindo de você | `4,5 → 9 → 18 → 30 → 60 m` |
| `Linha` | `18 × 1,5 m` | `4,5 → 9 → 18 → 30 → 60 m` |
| `Aura` | raio `3 m` centrada em você | *(esfera)* |

> **A escada sobe bem. O que é pequeno é a BASE da esfera — `3 m` de raio, que é um quadrado e meio.**
> *E o `Cone` de `4,5 m` na base é menos que o deslocamento de `9 m` de qualquer pessoa.*

⚠ **Não é item do Bestiário: é do Fundamento, e mexe nos dois lados da mesa.** *Anotado, não trabalhado.*

> ⚠ **E ele NÃO é o item `11`.** *O `11` é o PREÇO da área (`Leve` fixo contra "reparte a cota"); o `15`
> é o TAMANHO dela.* **Os dois se encontram quando o `11` fechar** — se área passar a ter trava de uso,
> aumentar o raio fica mais barato de conceder.


---

# § OS TRÊS MARTELOS QUE O ITEM `17` ABRIU

*Todos com a conta rodada em `fila/MEDIDA-o-capanga.md`. **Custo zero de conta: só falta escolher.***

## Martelo `A` — a banda

*E este é também a pergunta `3` do martelo do item `10`, agora com número.*

| # | a saída | o que ela custa |
|---|---|---|
| **`1`** | **a banda vira `21%`–`28%`** — o medido, arredondado | **mexe em número publicado pela segunda vez em um dia.** *Mas a decisão de `20%`–`32%` fechou com a justificativa "o piso passa a ser o `Controlador`", e a forma `B` matou essa premissa* |
| **`2`** | fica em **`20%`–`32%`** | não mexe em nada. *Custa `4,3` pontos de teto que ninguém alcança — **e a escada escreve que a banda foi feita pra vigiar o TOPO*** |
| **`3`** | só o **piso volta pra `21%`**, teto fica `32%` | meio termo: piso real, teto folgado de propósito pra caber crescimento futuro |

> **Recomendação: `1`.** *A banda é uma régua. Uma régua com `4,3` pontos de folga em cima não pega
> nada em cima, e é justamente em cima que ela foi feita pra pegar.*

## Martelo `B` — o `Capanga` toma papel?

*Medido no nv20, luta inteira com fogo concentrado.*

| # | a saída | o que ela custa |
|---|---|---|
| **`1`** | **só os quatro neutros** — `Artilheiro` · `Emboscador` · `Apoio` · `Controlador` *(por esquadrão)*. **`Brutamontes` e `Guardião` não** | uma lista de exceção por categoria. *E o motivo do `Brutamontes` não é o número: **um `Capanga` que não cai num golpe é uma `Ameaça`**, e a escada já diz isso* |
| **`2`** | **o `Capanga` não tem papel nenhum** | mais simples de escrever. *Custa o `Apoio` e o `Emboscador`, que são de graça e ficam bem num esquadrão* |
| **`3`** | **todos entram, e o mestre mede** | o molde "declarar e liberar". *Custa `+25%` de encontro escondido num degrau que a escada vendeu como `1,00×`* |

> **Recomendação: `1`.** *Ela é a única que não mente sobre o tamanho do encontro, e a exclusão do
> `Brutamontes` cai de graça da definição que já está publicada.*

## ~~Martelo `C`~~ — ✅ **FECHADO POR MEDIÇÃO: `ações = 8`, por esquadrão**

***Ele não escolheu: mandou medir*** — *"valide em comparação ao Draw Steel, foi de lá q pegamos a
ideia"*. **E a medição fechou sozinha:** `fila/MEDIDA-o-controlador-no-esquadrao.md`.

*O `Controller` do Draw Steel, normalizado por nível e organização em `415` statblocks, é `0,917×` a
coorte. A leitura por esquadrão paga `0,889×` — **`3,1%` de distância**. A por corpo paga `0,500×` —
`45,5%`, e nenhum dos onze papéis deles chega perto de metade.*

**⚠ E de quebra a tabela dos seis ganhou validação externa:** *`Artilheiro` `0,857` contra `0,833`,
`Brutamontes` `1,200` contra `1,250`.* **Três de cinco batem em menos de `4%`, por duas derivações
independentes.**

### A conta que fechou o martelo

| a leitura | ganha | paga vida | razão vs chefe |
|---|---|---|---|
| **por CORPO** — `ações = 1` | `2,000×` | `× 0,500` | **`0,67`** |
| **por ESQUADRÃO** — `8` corpos | `1,125×` | `× 0,889` | **`1,01`** |

> **Recomendação: por ESQUADRÃO.** *Quem age é o esquadrão. Negar `1` ação de um grupo que enfrenta
> `8` corpos vale pouco — e o preço tem de valer pouco também.* **A leitura por corpo cobra metade da
> vida por um ganho que o esquadrão não tem.**


---

# § ~~ITEM `19`~~ — ✅ **FECHADO: teto `3`, extras a METADE**

> **`fila/DECIDIDO-o-capanga.md` §2b · medição em `fila/MEDIDA-o-empilhamento.md`.**
>
> *Sem trava, `8` capangas entregavam `296` numa cabeça de `163` de vida — **`181%`**, e `272%` se
> fossem `Grande`.* **Com a trava: `74` = `45%`.**
>
> **O desconto foi medido em `115` minions do Draw Steel: `0,573`.** *Ficou em `0,50` porque é a
> fração que o `Estilhaço` e o `tamanho` já publicam — uma fração de respingo no bestiário, não duas.*
>
> ⚠ **E ela não re-preça nada:** *o enxame continua entregando tudo, só não concentra. A razão
> `1,01 ×` da escada não se move.* **Por isso foi barata.**

## O raciocínio original

*Achado em 10/09 medindo o `Controlador` contra o Draw Steel —
`fila/MEDIDA-o-controlador-no-esquadrao.md`.*

**O nosso `Capanga` não tem teto nenhum pra quantos corpos batem na mesma pessoa.** *No nv20 são
`8 × 37` = **`296` numa cabeça só**, contra `163` de vida.* **Uma pessoa morre duas vezes na primeira
rodada, e nada na regra impede.**

**E o Draw Steel tem a trava escrita:**

> *"Each target of a minion's signature ability is affected by only **one instance** of the ability.
> But when **two or three (at maximum)** of a squad's minions attack the same creature simultaneously,
> each additional minion causes the ability to deal extra damage equal to the minion's **free strike
> value**."*

**É a mesma família de argumento que a gente já mediu na área** — *"Spread the Damage Around"*,
`fila/A-DECISAO-da-area-e-da-recarga.md`.

| custo | 🟡 **MÉDIO** |
|---|---|
| **o que pede** | uma trava escrita + re-rodar a simulação do enxame com ela. *A simulação de hoje supõe que os `8` batem livres* |
| **onde mexe** | o capítulo do `Capanga`, e possivelmente o fator de dano dele |
| ⚠ **e ele cruza com o `9`** | o preço de encontro misturado (`1 Desastre + 4 Capangas`) **pressupõe** como o enxame distribui dano. *Fechar o `19` primeiro barateia o `9`* |


---

# § ~~O MARTELO DO ITEM `16`~~ — ✅ **FECHADO: saída `F`, o `tamanho` não cobra**

> **`fila/DECIDIDO-o-tamanho.md`.** *Ele mandou medir duas vezes em vez de escolher, e a
> medição derrubou a premissa: **o preço em Defesa era invenção nossa**. `AC` espalha
> `1,000 ×` em `4.791` criaturas do PF2e e `1,016 ×` em `331` do D&D; o Draw Steel não tem
> defesa.* **E "encolher o ganho" tem número: o campo ganha `1,181 ×` e é UM degrau, não
> escada — o nosso topo era `1,650 ×`.**

> ⚠ **Sobra declarar os `+18%`** que a `F` põe fora da conta, e ela **cruza com o item `19`**.

## O raciocínio, e as cinco saídas que a medição aposentou

*Conta em `fila/MEDIDA-o-tamanho-exercitado.md`. **Cinco saídas, todas com número.***

> ## ⚠⚠ E A VALIDAÇÃO CONTRA O DRAW STEEL DERRUBOU A PREMISSA — `fila/MEDIDA-o-tamanho-no-draw-steel.md`
> ***Ele mandou medir antes de escolher:*** *"sempre métrica antes de resposta em achismo."*
>
> **No Draw Steel o `size` NÃO TEM TROCA.** *Medido em `415` statblocks, normalizado por nível e
> organização: **Stamina `1,000 ×`, EV `1,000 ×`** — exato.* **E ele ainda DÁ stability.**
>
> **E lá o tamanho dá as duas coisas que o nosso dá:** *alcance (`size 2` = `Melee 2`, `size 5` =
> `Melee 4`) **e** alvos (`43%` das ações de `size 2+` pegam `2+` alvos, contra `22%` de `size 1`).*
>
> ### O preço em Defesa é invenção nossa. E o Draw Steel nem TEM defesa — ataque é power roll.
> **⟹ O `Colossal` não é inconstruível porque a conta errou. Ele é inconstruível porque a gente pôs
> preço num eixo que o campo entrega de graça, e o preço bateu num piso de fórmula.**
>
> ### 🆕 Isso abre a saída `F` — **o `tamanho` não cobra nada**
> *Contradiz a instrução dele ("tamanho tem q ter uma troca"), e tem um porém: **o nosso ganho é maior
> que o deles** — a gente dá metade do dano em até `3` vizinhos, sempre; eles dão "às vezes `2` alvos".*
> **A saída honesta da `F` seria encolher o ganho até o tamanho do deles, e aí não cobrar.**
>
> ### E a `2ª` pergunta — o atributo devolvido — também foi medida
> *A soma dos cinco atributos no Draw Steel é a MESMA em todo tamanho (`1,000 ×` normalizado). O que
> muda é a FORMA: Might sobe de `1` a `5`, Agility desce.* **No campo, tamanho redistribui atributo,
> não adiciona.** ⚠ *Mas lá nenhuma derivada lê atributo — a devolução de Destreza é artefato da
> nossa fórmula, e o campo não tem esse acoplamento pra opinar.*

| # | a saída | o que ela custa |
|---|---|---|
| **`A`** | o `Colossal` corta `2` vizinhos em vez de `3` | ele **vira o `Imenso`**, e o buraco do nv`2` ao nv`9` continua |
| **`B`** | piso de nível por degrau | **mata o `Colossal`** — ele não fecha em nível nenhum |
| **`C`** | o `tamanho` paga em **VIDA**, não em Defesa | fecha exato em `100%` dos níveis. **Custa a ficção** de "grande é mais fácil de acertar" |
| **`D`** | híbrido **por faixa** de nível | mantém ficção e invariante. *Custa `12` números em vez de `3`* |
| **`E`** ⭐ | híbrido **FIXO**: Defesa `−3` *(o maior que fecha nos `29`)*, resto em vida | **uma tabela, quatro linhas, todo nível.** *`Imenso` e `Colossal` empatam em Defesa e se separam em vida e alvos* |

> **Recomendação: `E`** — é a única que mantém a ficção **e** o invariante sem tabela por faixa. *E
> ela usa a moeda que o projeto inteiro já usa: o `tamanho` é o **único** eixo que paga em Defesa, e
> é o único que bateu num piso de fórmula.*

⚠ **E qualquer saída precisa preçar o achado `4` junto** — o ponto de atributo devolvido. *Senão o
`Colossal` continua barato por uma porta que ninguém fechou.*

---
---

# 🆕 A FILA NOVA — o que abriu em 10/09 (tarde), itens `23` a `29`

*A fila antiga acabou. **O que sobrou dela:** o `6` e o `8` (repositório, que eu não escrevo), o `15`
do lado do jogador (só anotado, por decisão dele) e o playtest (não rodou —
`06-playtest/ESTADO-o-playtest-nao-rodou.md`).*

## ✅✅ TODOS MARTELADOS por ele em 10/09 (tarde) — `23` · `24` · `25` · `26` FECHARAM

| # | item | o que ele bateu | onde |
|---|---|---|---|
| ~~`23`~~ | raio × diâmetro | **`C`** — fica raio, e imprime a grade junto | `DECIDIDO-raio-ou-diametro.md` |
| ~~`24`~~ | resistência · imunidade · vulnerabilidade | **`A`** a vulnerabilidade é `1,00×` *(e ele mandou medir: `3` de `3` sistemas fazem igual)* · **`B`** `Vulnerabilidades` · **`C`** condição vai na mesma célula `Imunidades` · **`D`** o `Físicos` fica vendável, com aviso | `DECIDIDO-a-resistencia-e-a-vulnerabilidade.md` |
| ~~`25`~~ | o preço da imunidade a condição | **PUBLICADO junto do `24C`** — `1,20×` / `1,00×` | `MEDIDA-a-imunidade-a-condicao.md` |
| ~~`26`~~ | as formas de área do INIMIGO | **aprovado EM BLOCO, cone do D&D (`1,000`)** | `DECIDIDO-as-formas-de-area-do-inimigo.md` |

> ### ⚡ O `24A`: `4` de `4` sistemas TÊM vulnerabilidade e `4` de `4` NÃO mexem no custo de encontro.
> ⚠⚠ **E ele me corrigiu com um print da Múmia do `MM'25`** — *eu tinha dito que o D&D 2024 apagou a
> mecânica, e o `0` era da COLETA: o meu `srd-2024.json` traz o campo vazio pra ela.* **Canário
> instalado.** ✅ **E a vida também não sobe** — a Múmia tem `58` contra `65` da mediana `CR 3`.
>
> | ~~`14`~~ | a linha do aperto de atributo | ✅ **MARTELADA** — `DECIDIDO-a-linha-do-aperto-de-atributo.md` |
> |---|---|---|

## ✅✅ `27` · `28` · `29` — MARTELADOS em 10/09, e o `29` me corrigiu

**`fila/DECIDIDO-o-cone-o-anteparo-e-o-espalhamento.md`.**

| # | fechou como |
|---|---|
| ~~`27`~~ | ✅ **a abertura é a do D&D — `53°`, "a largura é igual à distância".** *E o argumento dele fechou: o VTT não decide o ângulo, ele LÊ de uma configuração — o Foundry já vem com `53°` de fábrica* |
| ~~`28`~~ | ✅ **o `Anteparo` ocupa os quadrados da `Linha` da Classe**, contíguos por lado, altura `≥ 2`, colocado num ponto. *Zero número novo — é o `X wall` do Draw Steel* |
| ~~`29a`~~ | ### ❌ **NÃO repreçar** — *ele estava certo e eu estava errado* |
| ~~`29b`~~ | ✅ **quando o comprimento da `Linha` bate no topo, `Maior` sobe a LARGURA** (`1,5 → 3 → 4,5 m`) |

> ### ⚠⚠ O `29` — eu publiquei `20×` e a conta estava ERRADA
> *Comparei `Cone` e `Linha` no mesmo ÍNDICE de degrau, e eles não começam no mesmo degrau: o `Cone`
> nasce no `1` (`4,5 m`) e a `Linha` no `3` (`18 m`).* **Na base a `Linha` é MAIOR (`12` contra `4` q)
> E alcança `4,00×` mais longe.** *A troca que ele descreveu é real.*
>
> | espalhamento entre as formas | |
> |---|---|
> | D&D 2014 | `1,52×` |
> | **D&D 2024** | `2,79×` |
> | **Draw Steel** | ### **`13,44×`** |
> | **o nosso, na base** | ### **`2,79×` — idêntico ao D&D 2024** |
>
> **Sobrou um buraco estreito:** *nas `Classes 6`–`7` a `Linha` paga `3` degraus e recebe `1`, porque
> ela já nasce perto do topo.* **É desperdício, não desequilíbrio — e o `29b` resolve.**

> ## ⚡⚡ E ISSO FECHA O ITEM `15` SEM ABRIR ELE.
> **O que fazia o `15` ser caro era o `29a`.** *A medição matou o `29a`.* **As três mexidas que
> sobraram só ACRESCENTAM texto onde não havia número — nenhum feitiço pronto encolhe.**

## ✅ E o que EU já executei em 10/09 (tarde), sem precisar de martelo

| | o quê | por que não precisava |
|---|---|---|
| **o footprint do corpo** | `Médio` `1×1` · `Grande` `2×2` · `Imenso` `3×3` · `Colossal` `4×4` — **aplicado no `RASCUNHO-5`** | `3` de `3` sistemas dão o mesmo valor, e o `tamanho` já não cobra nada (item `16`) |
| **as `2` mexidas novas no §6.3** | a frase da vulnerabilidade e as `2` menções à `Alcateia` morta — **na `MEXIDAS-no-repositorio.md`** | é lista de execução, não decisão. *O commit passou de `7` pra `9` mexidas* |
| **parar o playtest** | `06-playtest/ESTADO-o-playtest-nao-rodou.md` | ele mandou |
