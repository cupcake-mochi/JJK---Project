A montagem tem três passos, nesta ordem, e cada um lê uma tabela.

*Passo 1 · Categoria* diz quanto o inimigo aguenta, *Passo 2 · Papel* diz como ele luta, e
*Passo 3 · Tamanho* diz onde o corpo cabe e até onde o golpe alcança. Os números de cada nível estão
em *Tabelas de nível*, e a ação montada no Fundamento, em *Escrita de ação*.

# Passo 1 · Categoria

A categoria responde uma pergunta só: **quantos personagens este inimigo exige?**

O fator da categoria e o número de pessoas são a mesma coisa em duas unidades:
**`personagens = fator × 4`**. Um bicho de fator `1,92` exige `7,7` pessoas.

**Categorias**
{: .tab-titulo }

| categoria | quem ela pede | vida | dano | ações | corpos | tem `Intervenção`? |
|---|---|---|---|---|---|---|
| **`Capanga`** | — | dano do grupo ÷ 4 | `0,25` | `1` | `8`, em pool | não |
| **`Ameaça`** | `1` | `0,25` | `0,25` | `1` | `1` | não |
| **`Desastre`** | `4` — a mesa padrão | `1,00` | `1,00` | `3` | `1` | sim |
| **`Catástrofe`** | `6` — a mesa cheia | `1,50` | `1,50` | `5` | `1` | sim |
| **`Calamidade`** | `8` | `2,00` | `2,00` | `6` | `1` | sim |

O `Desastre` é a linha da tabela de inimigo do manual sem tocar em nada. As outras saem dela.

> Nas colunas de quem tem `Intervenção`, a `Vida e golpe por faixa` já traz o golpe multiplicado
> por `0,923`. Use o golpe como ele está.

## Teto de empilhamento

> No máximo `3` corpos do mesmo esquadrão atacam o mesmo alvo por rodada, e do segundo em
> diante o golpe sai pela metade.

Sem a trava, oito corpos entregam mais que a vida inteira de um personagem numa rodada. Com
ela, entregam menos da metade.

A trava não encolhe o esquadrão. Os oito continuam entregando tudo; eles só não concentram.

## Encontro misturado

Quando você põe capangas ao lado de um chefe inteiro, os fatores não se somam.

> **fator do encontro = fator do chefe + (capangas × `0,083`)**

A régua vale até quatro capangas somados a um chefe. Acima disso cada corpo passa a valer mais.

**Chefe acompanhado**
{: .tab-titulo }

| o chefe vem | ele fica com | o encontro exige |
|---|---|---|
| sozinho | `100%` da vida | `4,00` pessoas |
| com um apoio | `91,5%` | `4,33` |
| com dois | `83,0%` | `4,67` |
| em bando (três) | `74,5%` | `5,00` |

# Passo 2 · Papel

O papel diz como ele luta. Ele redistribui o que a categoria deu, e nunca acrescenta.

**Papéis**
{: .tab-titulo }

| papel | o que ele ganha | o que ele paga |
|---|---|---|
| **`Brutamontes`** | vida × `1,20` | Defesa −2 |
| **`Guardião`** | Defesa +2 | vida × `0,80` |
| **`Artilheiro`** | alcance, a taxa fixa | vida × `0,857` |
| **`Emboscador`** | vantagem em `1` ataque por rodada, toda rodada | vida × a linha da categoria |
| **`Controlador`** | `1` ação negada do grupo | dano × `0,667` |
| **`Apoio`** | o mesmo `1` para `1`, em outro bloco | dano |

O golpe não muda em nenhum papel.

## Pagamento do `Emboscador`

O pagamento dele muda com a categoria.

**Vida do `Emboscador`, por categoria**
{: .tab-titulo }

| categoria | vida × |
|---|---|
| `Capanga` e `Ameaça` | `0,677` |
| `Desastre` | `0,863` |
| `Catástrofe` | `0,913` |
| `Calamidade` | `0,927` |

> Use a linha da categoria do bicho, e não um número só desta tabela.

## Papel por categoria

O `Capanga` toma quatro papéis: `Artilheiro`, `Emboscador`, `Apoio` e `Controlador`. O
`Controlador` num esquadrão conta as oito ações do esquadrão, e não a de um corpo.

`Brutamontes` e `Guardião` ficam fora do `Capanga`. O `Brutamontes`, porque um `Capanga` que não cai
num golpe é uma `Ameaça`.

O `Emboscador` não sobe de `Grande`. O `Guardião` e o `Apoio` só se pagam com mais de um inimigo
no encontro.

# Passo 3 · Tamanho

O tamanho diz onde o corpo cabe e até onde o golpe alcança. Ele não cobra nada.

**Tamanho, grade e alcance**
{: .tab-titulo }

| tamanho | ocupa na grade | alcance | o golpe pega |
|---|---|---|---|
| `Minúsculo` · `Pequeno` · **`Médio`** | `1×1` *(1,5 × 1,5 m)* | `1,5 m` | só o alvo |
| **`Grande`** | `2×2` *(3 × 3 m)* | `3 m` | o alvo, e metade em `1` vizinho |
| **`Imenso`** | `3×3` *(4,5 × 4,5 m)* | `4,5 m` | o alvo, e metade em `1` vizinho |
| **`Colossal`** | `4×4` *(6 × 6 m)* | `6 m` | o alvo, e metade em `1` vizinho |

A escada do tamanho mora no alcance. Nos alvos ele é um degrau só: `Grande`, `Imenso` e
`Colossal` pegam o mesmo vizinho a metade.

> A Defesa não muda com o tamanho, e o tamanho não pede nada em troca.
>
> Um bicho de `Grande` para cima entrega perto de um quinto a mais que um `Médio` da mesma
> categoria, de graça. Conte com essa folga.

A coluna da grade limita o teto de empilhamento: um esquadrão de oito `Capanga` `Grande` ocupa
trinta e dois quadrados, e três deles não cabem em volta de uma pessoa sem que o mapa permita.

# Tabelas de nível

<!-- TABELAS -->

**Vida e golpe por faixa**
{: .tab-titulo }

| nível | `Capanga` (cada um) | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |
|---|---|---|---|---|---|
| **2–4** | 9 · 4 | 28 · 4 | 114 · 1d4 + 3 | 171 · 5 | 228 · 1d4 + 3 |
| **5–8** | 22 · 2d4 + 5 | 67 · 2d4 + 5 | 270 · 2d4 + 7 | 405 · 1d10 + 5 | 540 · 2d4 + 7 |
| **9–12** | 32 · 2d8 + 10 | 97 · 2d8 + 10 | 390 · 2d10 + 12 | 585 · 3d6 + 10 | 780 · 2d10 + 12 |
| **13–16** | 45 · 4d6 + 14 | 135 · 4d6 + 14 | 540 · 4d8 + 16 | 810 · 6d4 + 16 | 1080 · 5d6 + 17 |
| **17–20** | 55 · 4d8 + 19 | 165 · 4d8 + 19 | 660 · 5d8 + 23 | 990 · 8d4 + 21 | 1320 · 5d8 + 23 |
| **21–25** | 68 · 4d10 + 24 | 206 · 4d10 + 24 | 825 · 8d6 + 28 | 1237 · 4d12 + 25 | 1650 · 8d6 + 28 |
| **26–30** | 78 · 6d8 + 28 | 236 · 6d8 + 28 | 945 · 6d10 + 34 | 1417 · 7d8 + 29 | 1890 · 6d10 + 34 |

*Vida · golpe de uma ação. O golpe sai uma vez por ação, e o número de ações está na tabela do Passo 1. Em `Desastre`, `Catástrofe` e `Calamidade` o golpe já vem com o `0,923` da `Intervenção`.*

**Pool do esquadrão de `Capanga`**
{: .tab-titulo }

| nível | vida de um | pool dos oito |
|---|---|---|
| **2–4** | 9 | **72** |
| **5–8** | 22 | **176** |
| **9–12** | 32 | **256** |
| **13–16** | 45 | **360** |
| **17–20** | 55 | **440** |
| **21–25** | 68 | **544** |
| **26–30** | 78 | **624** |

**Defesa, acerto, CD e refino por marco**
{: .tab-titulo }

| nível | Defesa | acerto | CD | refino | proteção |
|---|---|---|---|---|---|
| **2–5** | 14 | +4 | 12 | 1 | +1 |
| **6–9** | 15 | +4 | 12 | 3 | +2 |
| **10–13** | 16 | +6 | 14 | 4 | +2 |
| **14–17** | 17 | +6 | 14 | 6 | +3 |
| **18–21** | 18 | +8 | 16 | 7 | +3 |
| **22–25** | 19 | +8 | 16 | 9 | +4 |
| **26–30** | 20 | +10 | 18 | 10 | +4 |

*Estas cinco valem para toda categoria. Elas sobem em marco de nível, e as duas escadas não coincidem.*

<!-- FIM TABELAS -->

# Exemplo

<!-- EXEMPLO -->

**Ubume**

*A mulher que aparece com uma criança no colo, e pede que você segure ela.*

Um grupo de nível 10 precisa dos quatro para derrubar isto, e quem monta quer um bicho que
aguenta apanhar. Isso são três escolhas, e cada uma tem uma linha de tabela.

**Passo 1 — a categoria.** Quatro pessoas é `Desastre`. A linha do nível 10 dá **vida `390`**, **`3` ações** e golpe **`23 (2d10 + 12)`**, que já traz o `0,923` da `Intervenção`.

**Passo 2 — o papel.** Ele apanha de frente, então `Brutamontes`: **vida `× 1,20`** e **Defesa `-2`**. A vida vai a `390 × 1,20` = **`468`**, e a Defesa de `16` para **`14`**.

**Passo 3 — o tamanho.** `Grande`: ocupa `2×2` na grade, alcança `3 m`, e o golpe pega o alvo mais metade em um vizinho. Não custa nada.

**Os atributos.** No nível 10 são `11` pontos. A Defesa da tabela pede Destreza `4`; a técnica dele declara Força, que é o que a ficção pede.


> ### Ubume
>
> *Maldição Grande · **Desastre** · **Brutamontes** · nível 10*
>
> **Defesa** `14` · **Acerto** `+6` · **CD** `14` · **Refino** `4` *(proteção `+2`)*
>
> **Vida** `468` · **Integridade** `468` · **Deslocamento** `9 m`
>
> **Ações**
>
> **Ações Múltiplas.** A Ubume faz três ataques de Garra, ou usa Choro e faz dois ataques de Garra.
>
> **Garra.** *Ataque corpo a corpo:* `+6` para acertar, alcance `3 m`, uma criatura. *Acerto:* `23 (2d10 + 12)` de dano Cortante, e metade desse dano em um vizinho do alvo.
>
> **Choro.** *Teste de Resistência Espírito:* CD `14`, cada criatura numa `Esfera` de raio `4,5 m` a partir do corpo dela. *Falha:* `23 (2d10 + 12)` de dano Psíquico. *Sucesso:* metade do dano.
>
> **Intervenções**
>
> Três por luta, cada uma usada uma vez. Sai no máximo uma por rodada, logo depois do turno de outra criatura. As três seguem o molde do capítulo 5.


O orçamento de uma ação dele é `23 ÷ 4,5` = **`5,1` pontos**, que bate com a linha do `Desastre` na `Orçamento de uma ação, por categoria`.

<!-- FIM EXEMPLO -->

# Escrita de ação

O orçamento de feitiço de uma ação é o golpe dela dividido por `4,5`. Com esse número em mãos,
você monta a ação no Fundamento, que é a mesma máquina que o jogador usa.

**Cada ação tem o orçamento dela.** Duas ações do mesmo bloco são duas montagens diferentes.

**Condição custa ponto.** Ponto gasto em condição é dado que não foi comprado, e a régua vale
dos dois lados da mesa.

**Área custa ponto.** Um feitiço em área tem menos dados para comprar condição, porque o Fundamento
cobra a área em ponto de feitiço.

Abaixo de `3` pontos a ação não monta feitiço. Ela bate, e o dano sai como a
`Vida e golpe por faixa` manda. Veja *Bloco seco*, no capítulo 5.

<!-- ORCAMENTO -->

**Orçamento de uma ação, por categoria**
{: .tab-titulo }

| nível | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |
|---|---|---|---|---|---|
| `2` | seco | seco | seco | seco | seco |
| `5` | seco | seco | seco | seco | seco |
| `10` | `4,2` | `4,2` | `5,1` | `4,6` | `5,1` |
| `15` | `6,2` | `6,2` | `7,6` | `6,9` | `7,7` |
| `20` | `8,2` | `8,2` | `10,1` | `9,1` | `10,1` |
| `25` | `10,2` | `10,2` | `12,4` | `11,3` | `12,4` |
| `30` | `12,2` | `12,2` | `14,9` | `13,4` | `14,9` |

*As colunas de quem tem `Intervenção` já levam o `0,923`.*

O que cabe na maior ação do sistema, a de `14,9` pontos:

**Condição na maior ação**
{: .tab-titulo }

| se ele comprar | custa | sobra para dado |
|---|---|---|
| uma condição `Leve` | `4` | `10,9` |
| uma condição `Média` | `7` | `7,9` |
| uma condição `Pesada` | `11` | `3,9` |

<!-- FIM ORCAMENTO -->

Uma ação de inimigo aguenta uma condição `Pesada`, e nesse caso ela vira quase só condição.