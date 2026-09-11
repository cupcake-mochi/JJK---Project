# Prova p1-dmg2014 — Guia do Mestre 5e 2014 (PT), fonte primária

*Verificação das três afirmações que o `PRECO-pe-do-inimigo.md` faz sobre o DMG 2014.*

**Arquivo conferido:** `/tmp/claude-1000/-media-mizuki-HD-Externo-II-Claude-Bestiario/56c72db1-7acc-4db0-bba3-77aa84a51702/scratchpad/livros/DMG2014-pt.txt` (19.664 linhas)

**Veredito global: CONFIRMADO.** As três afirmações estão no livro, em português, com o texto que
o relatório usa. As correções são de **arredondamento** e de **uma palavra** (`só`) — nenhuma toca
a substância. **A paginação do relatório NÃO está errada** (ver ponto 0).

## 0. Paginação: o relatório está certo, este scan é que anda uma página à frente

O relatório e o `LEVANTAMENTO-pe.md` citam a **edição inglesa oficial**: três rodadas na **p. 278**,
passo 13 na **p. 278–279**, conjuração na **p. 279**. Este scan **PT numera uma página adiante** em
toda esta região:

| trecho | p. inglesa (relatório) | p. neste scan PT | linhas no PT |
|---|---|---|---|
| regra das três rodadas + `(90+37+37)÷3` | 278 | **279** | 17240–17253 |
| cabeçalho do PASSO 13 | 278–279 | **279** | 17240 (col. dir.) |
| parêntese *"não mudam realmente as estatísticas"* | 279 | **280** | 17282–17283 |
| *Conjuração Inata e Conjuração* | 279 | **280** | 17290–17299 |
| tabela `Características de Monstro` | 280–281 | **281–282** | 17354–17471 |
| tabela `Estatísticas de Monstro por ND` | 274 | **275** | 16929–16977 |

O deslocamento é **constante de +1** e fecha nos seis pontos, o que confirma as duas paginações ao
mesmo tempo. **Não mexa nas páginas do relatório.** Só saiba que, ao conferir neste `.txt`, é uma
página depois.

*(Como sei que os marcadores deste scan são rodapés e não cabeçalhos: o marcador `281` está na linha
17417 e o **cabeçalho de coluna da tabela se repete** na 17418. Cabeçalho repetido de tabela só
aparece no TOPO de uma página nova — logo o `281` é o pé da página anterior.)*

> ⚠ **Nota de leitura do scan:** o texto é OCR de duas colunas interleavadas — a mesma linha
> numérica carrega a coluna esquerda **e** a direita. Os marcadores de página são **rodapés**
> (provado no ponto 5 abaixo). Todas as citações abaixo foram extraídas por coluna
> (`cut -c1-64` / `cut -c65-`) e conferidas contra o dump cru.

---

## 1. A regra das TRÊS PRIMEIRAS RODADAS e o exemplo (90+37+37)÷3 — **CONFIRMADO**

**Onde:** linhas **17240–17253**, coluna esquerda. Passo 11 (Dano), subseção *Dano Geral Causado*.
Página **279** neste scan PT (entre o rodapé `278` da linha 17206 e o rodapé `279` da linha 17280)
= **p. 278 na edição inglesa**, que é a que o relatório cita. Ver ponto 0.

Texto **literal**, em português:

> **Se o dano causado pelo monstro variar de uma rodada para a outra, calcule o dano causado por
> ele a cada rodada para as três primeiras rodadas de combate e pegue a média.** Por exemplo, um
> dragão branco jovem tem um hábito de ataques múltiplos (um ataque de mordida e dois ataques de
> garra) que causam uma média de 37 de dano por rodada, assim como sua arma de sopro que causa 45
> de dano, ou 90, se atingir dois alvos (e provavelmente vai). Nas três primeiras rodadas de
> combate, o dragão provavelmente irá usar sua arma de sopro uma vez e seu hábito de ataques
> múltiplos duas, então, **a média de dano causada por ele nas três primeiras rodadas seria
> (90 + 37 + 37) ÷ 3, ou 54 de dano (arredondado para baixo).**

*(`DMG2014-pt.txt`, linhas 17240–17253, col. esq.)*

**A conta:**

```
(90 + 37 + 37) / 3 = 164 / 3 = 54,6666...  -> arredondado para baixo = 54   ✓
```

**⚠ Correção (arredondamento).** O relatório escreve `(90 + 37 + 37) ÷ 3 = 54`. A divisão dá
**54,67**; o `54` vem do arredondamento, e o livro diz **explicitamente** *"arredondado para
baixo"*. Se o Projeto-M herdar o divisor de 3, tem que herdar a direção do arredondamento junto —
senão a mesma média fecha em 55.

**A frase seguinte, que o relatório não usa e é relevante pra `Intervenção`** (linhas 17254–17262,
col. esq.):

> Quando estiver calculando o dano causado por um monstro, **conte também com características
> especiais fora de rodada que causem dano, como auras, reações, ações lendária ou ações de covil.**

*Isto é o DMG mandando pôr a ação-fora-do-turno DENTRO da cota de dano por rodada — exatamente o
que a `Intervenção` é. O livro dá o precedente literal.*

---

## 2. O PASSO 13, sobre traços, ações e reações especiais — **CONFIRMADO**

**Onde:** cabeçalho na linha **17240**, coluna **direita**; corpo em 17240–17249 (col. dir., p. 279)
continuando em 17281–17289 (col. esq., p. 280).

Texto **literal**:

> **PASSO 13. TRAÇOS ESPECIAIS, AÇÕES E REAÇÕES**
>
> Alguns traços especiais (como Resistência à Magia), ações especiais (como Invisibilidade
> Superior) e reações especiais (como Aparar) podem aprimorar a efetividade de combate de um
> monstro e, potencialmente, aumentar o nível de desafio dele.
>
> A tabela Características de Monstro lista diversas características que você pode copiar do Manual
> dos Monstros. **A tabela descreve como as características aumentam a Classe de Armadura, pontos
> de vida, bônus de ataque ou dano causado efetivos com os propósitos de determinar o nível de
> desafio dele. (As características não mudam realmente as estatísticas do monstro.)**
> Características que não tenham qualquer efeito no nível de desafio do monstro são descritas com
> um traço (–).
>
> Quando atribuir traços especiais, ações ou reações para um monstro, tenha em mente que nem todos
> os monstros precisam disso. **Quanto mais você adiciona, mais complexo (e difícil de conduzir) o
> monstro se torna.**

*(`DMG2014-pt.txt`, linhas 17240–17249 col. dir. + 17281–17289 col. esq.)*

> A última frase é o argumento do relatório sobre "um bloco lido num relance" **dito pelo próprio
> DMG**. Pode ser citada direto.

---

## 3. Conjuração só mexe no ND se supera o ataque normal ou mexe em CA/PV — **CONFIRMADO EM SUBSTÂNCIA, com uma ressalva de uma palavra**

**Onde:** linhas **17290–17299**, coluna esquerda. Página **280**. Ainda dentro do Passo 13.

Texto **literal**:

> **Conjuração Inata e Conjuração.** O impacto que os traços especiais Conjuração Inata e
> Conjuração tem no nível de desafio de um monstro depende das magias que o monstro pode conjurar.
> **Magias que causem mais dano que o hábito de ataque normal do monstro e magias que aumentem a CA
> ou pontos de vida do monstro precisam ser levadas em consideração para determinar o nível de
> desafio final do monstro.** Veja a seção "Traços Especiais" na introdução do Livro dos Monstros
> para mais informações sobre esses dois traços especiais.

*(`DMG2014-pt.txt`, linhas 17290–17299, col. esq.)*

**⚠ Correção 2 (a palavra `só`).** O livro **não** escreve "só". Ele escreve na afirmativa: essas
magias *"precisam ser levadas em consideração"*. A exclusividade (*"e as outras não contam"*) é
**leitura**, não citação. A leitura é razoável e sustentada por dois apoios indiretos:

1. Na tabela Características de Monstro, as linhas `Conjuração` (Lich) e `Conjuração Inata`
   (Djinni) **não têm efeito próprio** — só remetem ao passo 13
   (linhas **17383–17384**: *"Veja o passo 13 abaixo de 'Criando o Bloco de Estatísticas de um
   Monstro.'"*).
2. A tabela marca com traço (`–`) tudo que não afeta o ND, e o passo 13 diz que quem não afeta é
   descrito assim.

**Mas para uso em documento de regra: a palavra `só` é do relatório, não do DMG.** Escreva
"o DMG só manda contar" com essa consciência, ou reescreva como o livro escreveu.

---

## 4. A tabela de Características de Monstro — qual é, e onde está

**Título no scan:** `CARASCTERÍSTICAS DE MONSTRO` — **linha 17354** (o `S` extra é erro de OCR; o
corpo do texto no passo 13 e na linha 17554 escreve corretamente *"Características de Monstro"*).

**Extensão:** linhas **17354–17471**. Páginas **281–282** (rodapé `281` na linha 17417, rodapé `282`
na linha 17476). O cabeçalho de coluna se repete na linha 17418, no topo da p. 282.

**Três colunas:** `Nome` | `Exemplo de Monstro` | `Efeito no Nível de Desafio` (linhas 17355 e 17418).

**O que ela é, mecanicamente:** uma **tabela de câmbio**. Cada traço vira acréscimo em CA efetiva,
PV efetivos, bônus de ataque efetivo ou dano por rodada efetivo — e o livro avisa que
*"As características não mudam realmente as estatísticas do monstro"* (17282–17283). É contabilidade
de precificação, não regra de mesa. **É o molde exato do que o Projeto-M precisa para precificar PE.**

**Amostra literal das linhas que interessam para o preço de um recurso limitado:**

| linha | Nome | Exemplo | Efeito no Nível de Desafio (literal) |
|---|---|---|---|
| 17370–17371 | Arma de Sopro | Dragão negro ancião | *"Para determinar o dano efetivo produzido, considere que a arma de sopro atinge dois alvos e que cada alvo falha no teste de resistência."* |
| 17383 | Conjuração | Lich | *"Veja o passo 13 abaixo de 'Criando o Bloco de Estatísticas de um Monstro.'"* |
| 17384 | Conjuração Inata | Djinni | *"Veja o passo 13 abaixo de 'Criando o Bloco de Estatísticas de um Monstro.'"* |
| 17404–17405 | Explosão da Morte | Magmin | *"Aumenta o dano por rodada efetivo produzido pelo monstro, por 1 rodada, na quantidade descrita no traço e considere que ele afeta duas criaturas."* |
| 17410–17411 | Fortitude de Morto-Vivo | Zumbi | *"Aumenta os pontos de vida efetivos do monstro baseado no nível de desafio pretendido: 1–4, 7 pv; 5–10, 14 pv; 11–16, 21 pv; 17 ou mais, 28 pv"* |
| 17442 | Possessão | Fantasma | *"Dobra os pontos de vida efetivos do monstro."* |
| 17444–17445 | Presença Aterradora | Dragão negro ancião | *"Aumenta os pontos de vida efetivos do monstro em 25%, se o monstro foi feito para enfrentar personagens de 10° nível ou inferior."* |
| 17448–17449 | Regeneração | Troll | *"Aumenta os pontos de vida efetivos do monstro em 3 x o número de pontos de vida regenerado a cada rodada."* |
| 17453–17454 | **Resistência Lendária** | Dragão negro ancião | ver ponto 5 |
| 17467–17468 | Transferência de Dano | Mantor | *"Dobra os pontos de vida efetivos do monstro. Aumente o dano efetivo por rodada do monstro em um terço dos pontos de vida dele."* |

> **Padrão que aparece na tabela e importa aqui:** um traço que dura **1 rodada** é precificado como
> dano-por-rodada de **uma** rodada (`Explosão da Morte`, `Ataque Surpresa`, `Bote`, `Ferimento
> Enfurecedor`) — ou seja, o DMG **não** multiplica o burst pelas 3 rodadas; ele o joga na média,
> exatamente como o modelo A do relatório faz. **O modelo A não é interpretação: é o procedimento
> publicado.**
>
> E `Regeneração` mostra o câmbio inverso: um efeito **por rodada** é precificado como
> **3 ×** o valor por rodada. **3 é o mesmo divisor da regra das três rodadas** — o livro é
> internamente consistente e o número 3 é a duração de luta que ele assume em toda a máquina.

---

## 5. Resistência Lendária: a taxa de câmbio em pontos de vida efetivos

**Onde:** linhas **17453–17454**, tabela Características de Monstro, p. 281.

Texto **literal**:

> **Resistência Lendária** | Dragão negro ancião | **"Cada uso diário desse traço aumenta os pontos
> de vida efetivos do monstro baseado no nível de desafio pretendido: 1–4, 10 pv; 5–10, 20 pv; 11 ou
> mais, 30 pv."**

*(`DMG2014-pt.txt`, linhas 17453–17454)*

**A taxa, tabelada:**

| ND pretendido | pv efetivos **por uso** | 3 usos (o padrão dos blocos lendários) |
|---|---|---|
| 1–4 | `+10` | `30` |
| 5–10 | `+20` | `60` |
| 11 ou mais | `+30` | `90` |

**Contra a coluna PV da tabela por ND (linhas 16929–16977), quanto valem os 3 usos:**

```
ND 11: 221–235 pv (média 228)  ->  90 pv = 39,5% da vida
ND 17: 311–325 pv (média 318)  ->  90 pv = 28,3% da vida
ND 20: 356–400 pv (média 378)  ->  90 pv = 23,8% da vida
ND 24: 536–580 pv (média 558)  ->  90 pv = 16,1% da vida
ND 30: 806–850 pv (média 828)  ->  90 pv = 10,9% da vida
```

> **Leitura para o Projeto-M:** o DMG precifica um recurso de **3 usos** de defesa a **um valor
> plano** (`30 pv/uso` acima do ND 11), e esse valor plano **encolhe** como fração da vida conforme
> o ND sobe — de `39,5%` no ND 11 para `10,9%` no ND 30. **É o mesmo movimento que o relatório mede
> no PE do inimigo** (`90%` do poço do jogador no nv 2 caindo para `42%` no nv 30). O campo já
> aceita que a fração encolha; isso não é defeito do modelo `9 × Classe`.
>
> E de novo: **3 usos.** Resistência Lendária = 3, Ações Lendárias = 3/rodada, Villain Actions = 3,
> Intervenção = 3. O `3` do relatório tem mais um apoio.

---

## 6. Bônus: a tabela mãe, e a confirmação de que o monstro de 2014 tem espaço de magia de verdade

**`ESTATÍSTICAS DE MONSTRO POR NÍVEL DE DESAFIO`** — linha **16929**, página **275**. Colunas:
`ND` | `Bônus de Prof.` | `CA` | `PV` | `Bônus de Ataque` | `Dano/Rodada` | `CD de Resist.`
(linhas 16931–16932).

Linhas extremas, literais: `ND 0: +2, CA 13, 1–6 pv, +3, 0–1 dano, CD 13` (16933) e
`ND 30: +9, CA 19, 806–850 pv, +14, 303–320 dano, CD 23` (16977).

**⚠ Correção 3 (erro de OCR nesta tabela, não do relatório).** Duas faixas de PV vieram corrompidas
no scan e **não devem ser usadas**:
- linha 16964, `ND 21: "301–445"` → o correto é **401–445** (quebraria a monotonia com o ND 20, que
  termina em 400)
- linha 16969, `ND 26: "526–670"` → o correto é **626–670** (o ND 25 termina em 625)

**MM 2014, p. 10 — o monstro conjurador tem espaço de magia igual ao do jogador.** Confirma a
primeira linha da tabela do §1 do relatório. Arquivo
`/tmp/claude-1000/-media-mizuki-HD-Externo-II-Claude-Bestiario/56c72db1-7acc-4db0-bba3-77aa84a51702/scratchpad/livros/MM2014-pt.txt`,
linhas **518–522**:

> **CONJURAÇÃO**
> Um monstro com a característica de classe Conjuração **possui um determinado nível de conjurador e
> espaços de magia, os quais ele usa para conjurar suas magias de 1° nível e superiores (como
> explicado no Livro do Jogador).**

E linhas 533–537, o monstro pode fazer upcast como jogador:

> Um monstro pode conjurar uma magia da sua lista com um nível superior, se ele possuir espaços de
> magia para tal. Por exemplo, um drow arcano com a magia de 3° nível relâmpago pode conjura-la como
> uma magia de 5° nível usando um dos seus espaços de magia de 5° nível.

*(É esta a seção "Traços Especiais na introdução do Livro dos Monstros" a que o passo 13 remete.)*

---

## 7. Recálculo do modelo A do relatório, com o divisor 3 do DMG

Refiz a conta da tabela do §4-A (nível 30, feitiço = `2×` o golpe, trocando **uma** ação, média das
3 rodadas conforme p. 279):

```
Capanga/Ameaça  1 ação  base/rodada  55  rodada com feitiço 110  média3  73,33  aumento 33,33%
Desastre        3 ações base/rodada 219  rodada com feitiço 292  média3 243,33  aumento 11,11%
Catástrofe      5 ações base/rodada 330  rodada com feitiço 395  média3 351,67  aumento  6,57%
Calamidade      6 ações base/rodada 438  rodada com feitiço 511  média3 462,33  aumento  5,56%
```

**Três das quatro linhas do relatório batem exatamente** (`33,3%`, `11,1%`, `5,6%`).

**⚠ Correção 4 (nit).** A `Catástrofe` está como `6,7%` no relatório; com o feitiço de `131` que a
própria tabela dele traz, o valor é **`6,6%`** (`6,57%`). Os `6,7%` só aparecem se o feitiço for
`132` (= `2 × 66` sem arredondar). É ruído de arredondamento de 0,1 ponto, não erro de modelo.

---

## 8. Correções, consolidadas

| # | onde | o que está escrito | o certo |
|---|---|---|---|
| 1 | §4-A, *"Texto exato, p. 278"*; **Fontes**, *"p. 278 e 279"* | — | **NÃO é erro.** Bate com a edição inglesa. Só não bate com este scan PT, que numera +1. Ver ponto 0. |
| 2 | §4-A, o exemplo | `(90 + 37 + 37) ÷ 3 = 54` | `= 54,67`, e o livro diz **"ou 54 de dano (arredondado para baixo)"**. O arredondamento é regra, não conveniência — se o Projeto-M herdar o divisor, herda a direção. |
| 3 | §4-A, a citação | está em **inglês** (*"If a monster's damage output varies…"*) mas a fonte listada é o *Guia do Mestre 2014* | substância idêntica ao PT, palavra por palavra. O PT literal está no §1 acima; use um dos dois e marque qual. |
| 4 | `LEVANTAMENTO-pe.md` **linha 946**: *"O DMG 2014 diz explicitamente que conjuração **só** mexe no ND quando… Feitiço de utilidade é **de graça**."* | "explicitamente", "só", "de graça" | o DMG **não** escreve nenhuma das três. Escreve que essas magias *"precisam ser levadas em consideração"* — afirmativa, não exclusiva. A conclusão é leitura correta (e apoiada pelas linhas 17383–17384 da tabela), mas **não é citação**. Corrigir o "explicitamente". |
| 5 | §4-A, linha `Catástrofe` | `6,7%` | `6,6%` (`6,57%`) com o feitiço `131` da própria tabela. `6,7%` só com `132`. Nit de 0,1 ponto. |
| 6 | — (defeito do scan, não do relatório) | — | `DMG2014-pt.txt` linha 16964 `ND 21: 301–445` → **401–445**; linha 16969 `ND 26: 526–670` → **626–670**. Não citar esses dois números. |
| 7 | `LEVANTAMENTO-pe.md` **linha 918** | *"Resistência Lendária vale +10/+20/+30 PV efetivos por uso diário conforme a faixa de ND"* | **CONFIRMADO literal** na fonte primária PT (linhas 17453–17454). Faixas exatas: ND 1–4 / 5–10 / 11-ou-mais. |

## 9. Achados novos que servem à discussão do PE

1. **O DMG manda pôr ação-fora-do-turno na cota de dano por rodada** (linhas 17254–17262):
   *"conte também com características especiais fora de rodada que causem dano, como auras, reações,
   ações lendária ou ações de covil."* → precedente literal para a `Intervenção` entrar na cota, não
   por fora dela.
2. **O DMG precifica burst de 1 rodada como 1 rodada, e efeito-por-rodada como 3 ×.** Comparar
   `Explosão da Morte` (17404) com `Regeneração` (17448). **O divisor 3 e o multiplicador 3 são a
   mesma constante**: o livro assume luta de 3 rodadas em toda a máquina de preço. O modelo A do
   relatório é o procedimento publicado, não uma extrapolação.
3. **O DMG diz, ele mesmo, que traço demais estraga o monstro** (17287–17289):
   *"Quanto mais você adiciona, mais complexo (e difícil de conduzir) o monstro se torna."* → é a
   fonte primária para o argumento de "uma linha só no bloco".
4. **A Resistência Lendária mostra que o campo aceita fração de recurso encolhendo com o nível**
   (39,5% da vida no ND 11 → 10,9% no ND 30), o que desarma a objeção de que o `9 × Classe` "vale
   pouco no nível alto".
5. **O DMG 2014 é o único sistema do levantamento que dá poço do jogador ao monstro, e a tabela por
   ND mostra por quê ele pode**: ela orça `Dano/Rodada` por ND (ND 30 = `303–320`), e a conjuração
   entra ali só se **superar** o ataque normal. Ou seja: **mesmo em 2014, o espaço de magia não é uma
   economia paralela — ele é convertido em dano por rodada.** Isso é apoio forte, e novo, para a
   recomendação do relatório.
