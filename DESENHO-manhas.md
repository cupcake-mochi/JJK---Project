# As treze Manhas — o nível 2 da Vanguarda

*Escritas na v0.82. **A régua veio antes do catálogo**, que é a recomendação de método que a peça 13 contra a peça 14 deixou.*

> **Escola de Arma (Vanguarda, nível 2).** Escolha uma das treze categorias de arma. Com armas daquela categoria você usa a **Manha** dela.

O `DESENHO-caminhos` abria esta linha desde a terceira passada e mandava o catálogo para depois — item 1 do *"o que sobrou aberto"*, marcado como **o maior trabalho que aquele desenho cria**. Sem ele, o nível 2 da Vanguarda apontava para uma lista que não existia, e um dos cinco Caminhos não rodava numa mesa de nível 2.

## O molde do 5e não transfere, e o motivo é estrutural

O desenho de Caminho dizia que o molde eram *"as oito propriedades de maestria do 5e de 2024"*. Rodadas contra a régua da peça 5 §4, **sete das oito reprovam**.

A causa não é preço: é que no 5e a rolagem do d20 é uma fatia pequena do que o personagem faz, e aqui não é. **`+1` no acerto vale `10,80` de dano por rodada, que é `10%` da Rotina.** Então vantagem — que são `25` pontos percentuais — vale `54,00`, e o degrau do nível 2 do Caminho é **uma fatia**, que são `5,08`.

| a maestria do 5e | permanente | em fatias | taxa que faria caber |
|---|---|---|---|
| `Vex` — vantagem no seu próximo ataque | `54,00` | **10,63** | 9% |
| `Nick` — o ataque extra dentro da Ação de Atacar | `21,60` | **4,25** | 24% |
| `Sap` — desvantagem no próximo ataque do alvo | `18,00` | **3,54** | 28% |
| `Cleave` — o golpe pega um segundo alvo | `11,50` | **2,26** | 44% |
| **`Graze` — o erro ainda causa o atributo** | `6,00` | **1,18** | **85% — cabe** |
| `+1` de Defesa | `3,39` | 0,67 | 150% — fraca |
| `Push` · `Slow` — empurrar ou tirar `3 m` | `1,80` | **0,35** | 282% — fraca |

**Uma das oito cai dentro do degrau sozinha.** As outras ou pedem trava grande, ou são fracas demais e precisariam ser o triplo do tamanho.

Isso não mata o formato — é o mesmo das Trilhas, onde a **janela** é que faz o preço fechar. O que muda é que **as treze são majoritariamente condicionais**, e não passivas como no 5e.

*O dano de inimigo foi lido da tabela do manual, não derivado: chefe faz `72` por rodada no nível 30 e capanga faz `38`.*

## Duas decisões do Mizuki que destravaram o catálogo

**Dano de valor FIXO é legal.** A cerca da peça 5 §4 proíbe *"dado de dano"*, e ninguém tinha escrito se valor fixo entrava junto — era o item 3 do *"o que a peça 5 precisa"*. **Fixo passa.** *Ela resolve de graça a mesma pendência na `Presa` do Evocador, que também é valor fixo.*

**Derrubar fica, e aplica a condição `Derrubado`.** *A régua de condição não existia quando isto foi escrito, e a entrada rodava com o efeito por extenso.* **Ela existe desde a v0.103, e é a peça 19** — o `Derrubado` é nível `Leve` lá, e vale `8,45` de dano por rodada permanente, que é exatamente o número derivado abaixo.

> **⚠ A colisão que isto abriu foi consertada na v0.88, e ela era REGRESSÃO.** *Esta entrada nasceu na v0.82 chamando a condição de `Caído`, que era o nome da máquina de estado de 0 de vida da peça 1 §5.5 — e a **v0.74 já tinha achado e fechado exatamente essa colisão no `Punho`**, adotando o `Derrubado` do manual. Oito versões depois ela voltou por outra porta.*
>
> **`Derrubado` é condição de nível `Leve` no manual**, com preço próprio e dois feitiços prontos usando ela — a `Palma Trovejante` e a `Vala Comum`. *Não é nome novo: é o nome que já existia.*
>
> **E o estado de 0 de vida virou `Inconsciente` na mesma versão**, aplicando a decisão do Mizuki que estava registrada aqui desde a v0.82 e nunca tinha sido aplicada.

## Como cada Manha foi preçada

Tudo no nível 30, que é onde a fatia foi definida. **A fatia é `5,08` de dano por rodada**, e o degrau do nível 2 do Caminho é **uma** delas.

As bases todas saem de documento dono:

| base | valor | dono |
|---|---|---|
| `+1` no seu acerto, permanente | `10,80` | peça 5 §4 |
| mover-se `+1,5 m`, permanente | `0,90` | peça 5 §4 |
| o golpe simples pega 2, permanente | `11,50` | peça 5 §4 |
| `+1` de Defesa, permanente | `3,39` | peça 5 §4 |
| `1` ponto percentual numa rolagem de **aliado** | `0,230` | `DESENHO-caminhos`, régua do Guia |
| dano do chefe por rodada, nv30 | `72` | manual, tabela de inimigo |

**E `derrubar` foi derivado das duas réguas que já existem, em vez de inventado.** *A peça 19 §2.2 reproduz esta conta linha por linha, e o `conferir-dano.py` falha se as duas divergirem:*

> vantagem para um aliado corpo a corpo — `25` pp × `0,230` = `5,75`
> o alvo gasta `4,5 m` levantando — `4,5` × `0,60` = `2,70`
> **total `8,45` de dano por rodada, que é `1,66` fatia permanente.** *Com trava de `60%` ele cai em `1,00`.*

## O catálogo

| categoria | Manha | o que faz | TR | trava | fatias |
|---|---|---|---|---|---|
| **Lâmina Curta** | `Talho` | `+1` no acerto do seu próximo ataque contra um alvo que levou dano seu neste turno | — | 75% | **0,80** |
| **Lâmina Longa** | `Raspão` | o ataque que **erra** ainda causa o seu atributo | — | — | **1,18** |
| **Massa** | `Abalo` | o alvo cai — condição `Derrubado` | **Físico** | 60% | **1,00** |
| **Porrete** | `Tranco` | desvantagem no próximo ataque do alvo | **Vigor** | 28% | **0,99** |
| **Manopla** | `Encaixe` | `+2` de Defesa até o seu próximo turno, se você acertou. Uma vez por rodada | — | 75% | **1,00** |
| **Machado** | `Racho` | o golpe pega um segundo alvo ao seu alcance | — | 44% | **1,00** |
| **Ceifa** | `Gancho` | o corte rasga: o alvo leva o seu atributo de novo no início do próximo turno dele | — | — | **1,18** |
| **Armas Longas** | `Espeto` | você empurra o alvo `4,5 m` | **Físico** | — | **0,53** |
| **Flexível** | `Laço` | o alvo perde metade do deslocamento do próximo turno | **Físico** | — | **0,53** |
| **Arremesso** | `Palmo` | `+1` no acerto do próximo arremesso contra o mesmo alvo | — | 50% | **1,06** |
| **Yumi** | `Zunido` | o tiro que **erra** ainda causa o seu atributo | — | — | **1,18** |
| **Balestra** | `Prego` | o alvo perde `9 m` do deslocamento do próximo turno | **Vigor** | — | **1,06** |
| **Arma de Fogo** | `Estampido` | todo aliado que enxerga tem `+1` no próximo ataque contra o alvo | — | — | **0,68** |
| *(no lugar da sua)* | `Versado` | guardar e sacar viram um gesto só, e `+1` no acerto com a arma nova | — | — | **não medida** |

> **Média `0,97` fatia. A menor é o `Espeto` e o `Laço` em `0,53`, a maior é o `Raspão`, o `Zunido` e o `Gancho` em `1,18`.**
> **Dominância entre a maior e a menor: `2,22×`** — o filtro do projeto reprova em `3,00×`. *Comparação: o `Guiar` do Guia vale `0,68` no mesmo degrau, e o `Absorver` do Bastião vale `1,60`. As treze cabem inteiras dentro do que os outros Caminhos já praticam.*

## A leva da v0.154 — cinco mexidas do Mizuki lendo o catálogo

*Nenhuma saiu de validador. As cinco vieram de ele ler as entradas e perguntar como cada uma acontece na mesa.*

| Manha | antes | agora | preço |
|---|---|---|---|
| `Talho` | `+1` contra alvo que levou dano seu **nesta luta** | `+1` no **próximo ataque** contra alvo que levou dano seu **neste turno** | `1,06` → **`0,80`** |
| `Encaixe` | sem limite | **uma vez por rodada** | `1,00` → `1,00` |
| `Gancho` | puxa o alvo `6 m` | **o corte rasga**: o alvo leva o seu atributo de novo no início do próximo turno dele | `0,71` → **`1,18`** |
| `Espeto` | empurra `6 m`, e ele não te acompanha | empurra **`4,5 m`** | `0,71` → **`0,53`** |
| `Laço` | perde o deslocamento **inteiro** | perde **metade** do deslocamento | `1,06` → **`0,53`** |

**O `Encaixe` era o único furo de regra da leva: ele não tinha limite e a Defesa empilhava.** *Com dois golpes na Ação de Atacar ele dava `+4`, e o preço de `1,00` sempre supôs `+2`.* **A entrada nomeia o limite agora, e o `+2` volta a ser o que estava preçado.**

> **⚠ O `3 m` que o Mizuki pediu para o `Espeto` reprovou, e por número.** *Ele dá `0,35` — que é exatamente a linha que a tabela do 5e acima já mede e recusa: `Push · Slow`, `0,35`, **fraca**.* **A banda iria a `3,33×` contra um filtro que reprova em `3,00×`.** *`4,5 m` entrega o encurtamento e mantém o filtro; e quem manda no piso da banda é o `Laço`, não o `Espeto`.*

### ⚠⚠ O `Gancho` não podia ser consertado por alcance, e o motivo é regra

***Achado do Mizuki:*** *"quase nunca ela vai ter alcance para puxar o alvo"*. **Ele está certo, e a causa é estrutural:** *puxar exige que o alvo esteja no seu alcance, e se ele já está, puxar não entrega nada.*

**A saída óbvia — dar `6 m` de alcance à Manha — reprova pela peça 14:** *`Alcance` é **propriedade de arma**, medida em metros, padrão `1,5 m`, e aquela peça escreve que "propriedade não é escolha: é o que a arma é".* **Uma Manha que concede alcance sobrescreveria uma propriedade de arma numa das treze categorias.**

> **E a ficção também não fechava, pelo mesmo lugar.** *A `Ceifa` é **Foice · Kama · Kusarigama**, e só o Kusarigama tem corrente.* **Dar `6 m` à categoria dá corrente à foice e à kama.**
>
> *O levantamento externo confirma a forma:* o 5e puxa a distância — `Thorn Whip` a `9 m`, `Lightning Lure` a `4,5 m` — **mas sempre como magia com alcance próprio**, nunca como propriedade pendurada no alcance corpo a corpo.

**A segunda saída — fechar a distância em vez de puxar — reprova por entregar zero.** *A peça 3 publica que a Ação de Movimento vale `9 m` e "pode ser dividida antes, durante e depois da ação".* **"Deslocar-se até `6 m` em direção ao alvo e atacar em sequência" é o turno base**, que todo personagem tem no nível 1. *É o defeito do `Bote`: entrada publicada e preçada que não entrega nada.*

***Decisão do Mizuki: o `Gancho` para de ser sobre mover.*** **Ele vira dano de valor fixo, que a seção *Duas decisões* acima já declarou legal** — e é o que uma foice faz. *Sem alcance, sem Teste de Resistência, no molde do `Raspão`.*

### ⚠⚠ E a leva destampou uma dívida: as Manhas foram preçadas supondo DOIS ataques

**O `Raspão` publica `6,00` de dano por rodada, e `6,00` só fecha com dois ataques:** *`2 × 50%` de erro `× 6` de atributo. Com um ataque dá `3,00`.*

> **Do nível 2 ao 6 a Vanguarda tem um ataque por rodada** — o ataque extra é o degrau de Caminho do nível **7**. **Então as quatro Manhas que escalam por ataque — `Talho`, `Raspão`, `Racho` e `Zunido` — entregam metade do preço publicado por cinco níveis.**

*Isso não é efeito desta leva: já era assim desde a v0.82, e nenhum documento escrevia.* **Fica registrado sem conserto**, porque consertar é escolher entre repreçar as quatro contra o nível 2 — e aí elas ficam grandes do 7 em diante — ou aceitar que o degrau do nível 2 da Vanguarda cresce sozinho no 7. *As duas mexem no orçamento da Vanguarda inteira, e isso é versão própria.*

## Os nomes, e os cinco que morreram na triagem

**Rodada nas duas direções, antes de qualquer um ser escrito.** Quatro candidatos caíram:

| morreu | por quê |
|---|---|
| `Fio` | dentro de `Fio Preso`, que é feitiço pronto do manual |
| `Volta` | dentro de `Sem Volta`, que é Restrição |
| `Sopro` | é feitiço pronto no manual |
| `Trava` | é Melhoria no manual |

**E um quinto morreu fora dela, por colisão de sentido — que é o que a triagem não pega.** `Ajuste` saiu `LIVRE` e foi recusado: `Ajusta` é um dos três formatos de Legado e aparece **42 vezes** na peça 13. Uma palavra fazendo o trabalho de duas é o defeito que a v0.64 pagou para consertar.

*`Manha` passou `LIVRE`, e ela é a palavra que o próprio desenho de Caminho já usava.*

## O que este bloco deixa em aberto

- ~~**A trava do `Abalo` é `60%` e ela precisa de gatilho escrito.**~~ **FECHADO na v0.147:** *o gatilho é o Teste de Resistência.* **Toda Manha que mexe no ALVO passou a pedir Teste de Resistência e a disparar uma vez por rodada** — decisão do Mizuki, e ela estava faltando desde que as treze entraram na v0.82.
- **⚠⚠ E isso abriu uma dívida de preço em QUATRO delas.** *O `Gancho`, o `Espeto`, o `Laço` e o `Prego` foram preçados com trava `—`, que quer dizer sem portão nenhum.* **Agora eles têm um, e os `0,71 · 0,71 · 1,06 · 1,06` publicados passam a valer mais do que a entrega entrega.** *Repreçar as treze é versão própria, no mesmo molde da dívida dos onze `Estigma` — e fazer meio dela deixaria o catálogo com dois modelos dentro.*
- **A `Versado` não tem fatia medida, e a forma dela diz onde ela cai.** *Ela entrega `+1` no acerto num relógio próprio, que é exatamente a forma do `Talho` e do `Palmo` — os dois preçados em `1,06` com trava de `50%`.* **Se a taxa de troca de arma na mesa for parecida, ela cai na mesma casa.** *Fica declarado como não medido em vez de escrito como se fosse.*
- **`Raspão` e `Zunido` são a mesma entrega em duas categorias.** *O 5e faz igual — `Graze` está no Greatsword e nas armas de haste —, mas fica declarado em vez de escondido.*
- **O `Estampido` é o único que preça rolagem de aliado**, e ele supõe três aliados na mesa. *Numa mesa de dois ele cai para `0,45` fatia.*
- **Nenhuma das treze foi medida contra as Trilhas da Vanguarda.** A matriz de dominância daquele Caminho fechou na v0.77 sem elas.
- **Elas não estão em peça numerada.** Como as Trilhas e os degraus de Caminho, moram em documento de raiz e não têm validador dono.