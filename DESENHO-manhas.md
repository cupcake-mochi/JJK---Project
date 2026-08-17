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

**Derrubar fica, e aplica a condição `Derrubado`.** A régua de condição não existe e vai vir com a peça de dano e condições; até lá a entrada roda com o efeito escrito por extenso.

> **⚠ A colisão que isto abriu foi consertada na v0.88, e ela era REGRESSÃO.** *Esta entrada nasceu na v0.82 chamando a condição de `Caído`, que era o nome da máquina de estado de 0 de vida da peça 1 §5.5 — e a **v0.74 já tinha achado e fechado exatamente essa colisão no `Punho`**, adotando o `Derrubado` do manual. Oito versões depois ela voltou por outra porta.*
>
> **`Derrubado` é `Condição Menor` no manual**, com tier de preço e dois feitiços prontos usando ela — a `Palma Trovejante` e a `Vala Comum`. *Não é nome novo: é o nome que já existia.*
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

**E `derrubar` foi derivado das duas réguas que já existem, em vez de inventado:**

> vantagem para um aliado corpo a corpo — `25` pp × `0,230` = `5,75`
> o alvo gasta `4,5 m` levantando — `4,5` × `0,60` = `2,70`
> **total `8,45` de dano por rodada, que é `1,66` fatia permanente.** *Com trava de `60%` ele cai em `1,00`.*

## O catálogo

| categoria | Manha | o que faz | trava | fatias |
|---|---|---|---|---|
| **Lâmina Curta** | `Talho` | `+1` no acerto contra alvo que já levou dano seu nesta luta | 50% | **1,06** |
| **Lâmina Longa** | `Raspão` | o ataque que **erra** ainda causa o seu atributo | — | **1,18** |
| **Massa** | `Abalo` | o alvo cai — condição `Derrubado` | 60% | **1,00** |
| **Porrete** | `Tranco` | desvantagem no próximo ataque do alvo | 28% | **0,99** |
| **Manopla** | `Encaixe` | `+2` de Defesa até o seu próximo turno, se você acertou | 75% | **1,00** |
| **Machado** | `Racho` | o golpe pega um segundo alvo ao seu alcance | 44% | **1,00** |
| **Ceifa** | `Gancho` | você puxa o alvo `6 m` para perto de você | — | **0,71** |
| **Armas Longas** | `Espeto` | você empurra o alvo `6 m` e ele não te acompanha | — | **0,71** |
| **Flexível** | `Laço` | o alvo perde o deslocamento inteiro do próximo turno | — | **1,06** |
| **Arremesso** | `Palmo` | `+1` no acerto do próximo arremesso contra o mesmo alvo | 50% | **1,06** |
| **Yumi** | `Zunido` | o tiro que **erra** ainda causa o seu atributo | — | **1,18** |
| **Balestra** | `Prego` | o alvo perde `9 m` do deslocamento do próximo turno | — | **1,06** |
| **Arma de Fogo** | `Estampido` | todo aliado que enxerga tem `+1` no próximo ataque contra o alvo | — | **0,68** |

> **Média `0,98` fatia. A menor é o `Estampido` em `0,68`, a maior é o `Raspão` e o `Zunido` em `1,18`.**
> **Dominância entre a maior e a menor: `1,74×`** — o filtro do projeto reprova em `3,00×`. *Comparação: o `Guiar` do Guia vale `0,68` no mesmo degrau, e o `Absorver` do Bastião vale `1,60`. As treze cabem inteiras dentro do que os outros Caminhos já praticam.*

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

- **A trava do `Abalo` é `60%` e ela precisa de gatilho escrito.** Hoje o número existe e a frase que o produz não — é o mesmo defeito do `15%` do `Servo`, que a `LISTA-gatilhos` existe em parte para não deixar repetir.
- **`Raspão` e `Zunido` são a mesma entrega em duas categorias.** *O 5e faz igual — `Graze` está no Greatsword e nas armas de haste —, mas fica declarado em vez de escondido.*
- **O `Estampido` é o único que preça rolagem de aliado**, e ele supõe três aliados na mesa. *Numa mesa de dois ele cai para `0,45` fatia.*
- **Nenhuma das treze foi medida contra as Trilhas da Vanguarda.** A matriz de dominância daquele Caminho fechou na v0.77 sem elas.
- **Elas não estão em peça numerada.** Como as Trilhas e os degraus de Caminho, moram em documento de raiz e não têm validador dono.
