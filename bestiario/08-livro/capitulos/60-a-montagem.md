A montagem tem três passos, nesta ordem, e cada um lê uma tabela.

*Passo 1 · Categoria e N* diz quanto o inimigo aguenta e quanto ele bate, *Passo 2 · Papel* diz
como ele luta, e *Passo 3 · Tamanho* diz onde o corpo cabe e até onde o golpe alcança. Os números de
cada nível estão em *Tabelas de nível*, e a ação montada no Fundamento, em *Escrita de ação*.

# Passo 1 · Categoria e N

A categoria é a dificuldade da luta. O N é para quantos personagens do nível ela é feita, do `×1` ao
`×6`.

<!-- DEGRAUS -->

**Categorias**
{: .tab-titulo }

| categoria | a luta | dura | o golpe | tem `Intervenção`? |
|---|---|---|---|---|
| **`Capanga`** | trivial | `2` rodadas | metade do golpe-base | não |
| **`Ameaça`** | baixa | `2,5` rodadas | `0,900` × o golpe-base | só no `×6` |
| **`Desastre`** | moderada — o chefe do manual | `3` rodadas | o golpe-base | do `×4` em diante |
| **`Catástrofe`** | severa | `4` rodadas | `1,125` × o golpe-base | do `×3` em diante |
| **`Calamidade`** | extrema | `5` rodadas | `1,200` × o golpe-base | do `×2` em diante |

<!-- FIM DEGRAUS -->

> **Vida = rodadas × N × a saída de um personagem.** Ele age N vezes por rodada. A saída de um
> personagem é o dano do grupo por rodada da tabela de inimigo do manual, dividido por quatro.
>
> O golpe não muda com o N. Um `Desastre ×6` bate o mesmo golpe de um `Desastre ×1`, seis vezes.

O `Desastre ×4` é a linha da tabela de inimigo do manual. Todas as outras células saem dela.

## `×1` e `×2`

O inimigo de uma ou duas ações perderia a luta inteira para uma condição que tira ação.

> **No `×1`, a condição que tira ação dá a ele um Teste de Resistência no começo do turno dele,
> sempre com a maestria.** Passou, ela sai antes de ele agir.
>
> **No `×2`, o mesmo Teste de Resistência, com desvantagem.**

As condições que tiram ação são o `Lento`, o `Calado`, o `Enfeitiçado` e o `Atordoado`. Ele continua
precisando falhar no teste para a condição pegar.

## Capanga

O `Capanga ×N` é um esquadrão de dois corpos por personagem, com a vida num pool só. Cada corpo cai
num golpe de um personagem e bate metade do golpe-base. O grupo derruba N corpos por rodada, e o
esquadrão dura duas rodadas contra qualquer N.

> Um `Desastre ×N` vale `3N` capangas do mesmo nível.

## Teto de empilhamento

> No máximo `3` corpos do mesmo esquadrão atacam o mesmo alvo por rodada, e do segundo em
> diante o golpe sai pela metade.

A trava não encolhe o esquadrão. Os corpos continuam entregando tudo; eles só não concentram.

## Chefe com capangas

Quando você põe capangas ao lado de um chefe, o chefe encolhe.

> **Cada capanga tira `1 ÷ (rodadas × N)` da vida e do golpe do chefe**, até metade do grupo em
> capangas. Na `Ameaça`, use a fração do `Desastre`.

<!-- CAPANGAS -->

**Chefe com capangas**
{: .tab-titulo }

| cada capanga tira | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |
|---|---|---|---|---|---|---|
| `Desastre` | `33,3%` | `16,7%` | `11,1%` | `8,3%` | `6,7%` | `5,6%` |
| `Catástrofe` | `25,0%` | `12,5%` | `8,3%` | `6,2%` | `5,0%` | `4,2%` |
| `Calamidade` | `20,0%` | `10,0%` | `6,7%` | `5,0%` | `4,0%` | `3,3%` |

<!-- FIM CAPANGAS -->

# Passo 2 · Papel

O papel diz como ele luta. Ele muda um número e paga na vida, e o golpe não muda.

**Papéis**
{: .tab-titulo }

| papel | o que ele ganha | o que ele paga |
|---|---|---|
| **`Brutamontes`** | vida × `1,20` | Defesa −2 |
| **`Baluarte`** | Defesa +2 | vida × `0,80` |
| **`Artilheiro`** | ataque com alcance de `18 m` | vida, pela categoria |
| **`Emboscador`** | vantagem em `1` ataque por rodada, toda rodada | vida, pelo N |
| **`Controlador`** | `1` ação negada do grupo | vida, pelo N |
| **`Reforço`** | o mesmo `1` para `1`, em outro bloco | vida, pelo N |

A Destreza não muda em nenhum papel: ela é a que a `Orçamento de atributo por marco` pede, no
capítulo 5. O `−2` do `Brutamontes` e o `+2` do `Baluarte` entram direto na Defesa.

## Pagamento do papel

O `Artilheiro` paga pela categoria: ele poupa a rodada de aproximação, e ela pesa mais na luta
curta. O `Emboscador`, o `Controlador` e o `Reforço` pagam pelo N: o preço deles é uma ação, e o
inimigo tem N.

<!-- PAGAMENTO -->

**Vida do `Artilheiro`, por categoria**
{: .tab-titulo }

| | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |
|---|---|---|---|---|---|
| a vida | `× 0,800` | `× 0,833` | `× 0,857` | `× 0,889` | `× 0,909` |

**Vida do papel, pelo N**
{: .tab-titulo }

| papel | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |
|---|---|---|---|---|---|---|
| `Emboscador` | `× 0,678` | `× 0,808` | `× 0,863` | `× 0,894` | `× 0,913` | `× 0,927` |
| `Controlador` e `Reforço` | `× 0,500` | `× 0,667` | `× 0,750` | `× 0,800` | `× 0,833` | `× 0,857` |
| o esquadrão do `Capanga`, `Emboscador` | `× 0,808` | `× 0,894` | `× 0,927` | `× 0,944` | `× 0,954` | `× 0,962` |
| o esquadrão do `Capanga`, `Controlador` e `Reforço` | `× 0,667` | `× 0,800` | `× 0,857` | `× 0,889` | `× 0,909` | `× 0,923` |

*O esquadrão do `Capanga` tem dois corpos por personagem, e age `2N` vezes.*

<!-- FIM PAGAMENTO -->

## Papel por categoria

O `Capanga` toma quatro papéis: `Artilheiro`, `Emboscador`, `Reforço` e `Controlador`, lidos pelo
esquadrão.

`Brutamontes` e `Baluarte` ficam fora do `Capanga`. Um corpo que não cai num golpe deixa de ser
`Capanga`.

O `Emboscador` não sobe de `Grande`. O `Reforço` só se paga com mais de um inimigo no encontro,
porque ele gasta o câmbio em outro bloco.

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
> célula, de graça. Conte com essa folga.

A coluna da grade limita o teto de empilhamento: um esquadrão de oito corpos `Grande` ocupa
trinta e dois quadrados, e três deles não cabem em volta de uma pessoa sem que o mapa permita.

# Tabelas de nível

<!-- TABELAS -->

**Vida por faixa · `Ameaça`**
{: .tab-titulo }

| nível | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |
|---|---|---|---|---|---|---|
| **2–4** | 24 | 47 | 71 | 95 | 119 | 142 |
| **5–8** | 56 | 112 | 169 | 225 | 281 | 337 |
| **9–12** | 81 | 162 | 244 | 325 | 406 | 487 |
| **13–16** | 112 | 225 | 337 | 450 | 562 | 675 |
| **17–20** | 137 | 275 | 412 | 550 | 687 | 825 |
| **21–25** | 172 | 344 | 516 | 687 | 859 | 1031 |
| **26–30** | 197 | 394 | 591 | 787 | 984 | 1181 |

**Vida por faixa · `Desastre`**
{: .tab-titulo }

| nível | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |
|---|---|---|---|---|---|---|
| **2–4** | 28 | 57 | 85 | 114 | 142 | 171 |
| **5–8** | 67 | 135 | 202 | 270 | 337 | 405 |
| **9–12** | 97 | 195 | 292 | 390 | 487 | 585 |
| **13–16** | 135 | 270 | 405 | 540 | 675 | 810 |
| **17–20** | 165 | 330 | 495 | 660 | 825 | 990 |
| **21–25** | 206 | 412 | 619 | 825 | 1031 | 1237 |
| **26–30** | 236 | 472 | 709 | 945 | 1181 | 1417 |

**Vida por faixa · `Catástrofe`**
{: .tab-titulo }

| nível | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |
|---|---|---|---|---|---|---|
| **2–4** | 38 | 76 | 114 | 152 | 190 | 228 |
| **5–8** | 90 | 180 | 270 | 360 | 450 | 540 |
| **9–12** | 130 | 260 | 390 | 520 | 650 | 780 |
| **13–16** | 180 | 360 | 540 | 720 | 900 | 1080 |
| **17–20** | 220 | 440 | 660 | 880 | 1100 | 1320 |
| **21–25** | 275 | 550 | 825 | 1100 | 1375 | 1650 |
| **26–30** | 315 | 630 | 945 | 1260 | 1575 | 1890 |

**Vida por faixa · `Calamidade`**
{: .tab-titulo }

| nível | `×1` | `×2` | `×3` | `×4` | `×5` | `×6` |
|---|---|---|---|---|---|---|
| **2–4** | 47 | 95 | 142 | 190 | 237 | 285 |
| **5–8** | 112 | 225 | 337 | 450 | 562 | 675 |
| **9–12** | 162 | 325 | 487 | 650 | 812 | 975 |
| **13–16** | 225 | 450 | 675 | 900 | 1125 | 1350 |
| **17–20** | 275 | 550 | 825 | 1100 | 1375 | 1650 |
| **21–25** | 344 | 687 | 1031 | 1375 | 1719 | 2062 |
| **26–30** | 394 | 787 | 1181 | 1575 | 1969 | 2362 |

**Golpe por faixa**
{: .tab-titulo }

| nível | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |
|---|---|---|---|---|---|
| **2–4** | 2 | 4 | 4 | 1d4 + 3 | 1d4 + 3 |
| **5–8** | 1d4 + 3 | 2d4 + 4 | 2d4 + 5 | 2d4 + 6 | 2d4 + 7 |
| **9–12** | 2d4 + 5 | 2d8 + 8 | 2d8 + 10 | 2d10 + 11 | 2d10 + 12 |
| **13–16** | 2d6 + 7 | 2d12 + 13 | 4d6 + 14 | 6d4 + 17 | 4d8 + 16 |
| **17–20** | 2d8 + 10 | 4d8 + 16 | 4d8 + 20 | 6d6 + 21 | 4d10 + 23 |
| **21–25** | 2d10 + 13 | 4d10 + 21 | 4d10 + 25 | 4d12 + 27 | 8d6 + 29 |
| **26–30** | 4d6 + 14 | 4d12 + 25 | 8d6 + 28 | 6d10 + 31 | 6d10 + 35 |

*O golpe de uma ação. Ele sai N vezes por rodada, e não muda com o N.*

**Capanga por faixa**
{: .tab-titulo }

| nível | vida de um corpo | o golpe dele |
|---|---|---|
| **2–4** | 9 | 2 |
| **5–8** | 22 | 1d4 + 3 |
| **9–12** | 32 | 2d4 + 5 |
| **13–16** | 45 | 2d6 + 7 |
| **17–20** | 55 | 2d8 + 10 |
| **21–25** | 68 | 2d10 + 13 |
| **26–30** | 78 | 4d6 + 14 |

*O esquadrão tem dois corpos por personagem, com a vida num pool só.*

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

*Estas cinco valem para toda célula. Elas sobem em marco de nível, e a vida e o golpe sobem em faixa de Classe.*

<!-- FIM TABELAS -->

# Exemplo

<!-- EXEMPLO -->

**Ubume**

*A mulher que aparece com uma criança no colo, e pede que você segure ela.*

Um grupo de quatro, de nível 10, vai enfrentar uma luta moderada, e quem monta quer um bicho que
aguenta apanhar. Isso são quatro escolhas, e cada uma tem uma linha de tabela.

**Passo 1 — a categoria e o N.** Luta moderada para quatro é `Desastre ×4`. A linha do nível 10 dá **vida `390`**, **`4` ações** e golpe **`19 (2d8 + 10)`**.

**Passo 2 — o papel.** Ele apanha de frente, então `Brutamontes`: **vida `× 1,20`** e **Defesa `-2`**. A vida vai a `390 × 1,20` = **`468`**, e a Defesa de `16` para **`14`**.

**Passo 3 — o tamanho.** `Grande`: ocupa `2×2` na grade, alcança `3 m`, e o golpe pega o alvo mais metade em um vizinho. Não custa nada.

**As `Intervenções`.** O `Desastre ×4` abre a porta, e as três se pagam na vida: `468 ÷ 1,0625` = **`440`**. O golpe não muda.

**Os atributos.** No nível 10 são `13` pontos. A Defesa da tabela pede Destreza `4`; a técnica dele declara Força, que é o que a ficção pede.


> ### Ubume
>
> *Maldição Grande · **Desastre ×4** · **Brutamontes** · nível 10*
>
> **Defesa** `14` · **Acerto** `+6` · **CD** `14` · **Refino** `4` *(proteção `+2`)*
>
> **Vida** `440` · **Integridade** `220` · **Deslocamento** `9 m`
>
> **Ações**
>
> **Ações Múltiplas.** A Ubume faz quatro ataques de Garra, ou usa Choro e faz três ataques de Garra.
>
> **Garra.** *Ataque corpo a corpo:* `+6` para acertar, alcance `3 m`, uma criatura. *Acerto:* `19 (2d8 + 10)` de dano Cortante, e metade desse dano em um vizinho do alvo.
>
> **Choro.** *Teste de Resistência Espírito:* CD `14`, cada criatura numa `Esfera` de raio `4,5 m` a partir do corpo dela. *Falha:* `19 (2d8 + 10)` de dano Psíquico. *Sucesso:* metade do dano.
>
> **Intervenções**
>
> Três por luta, cada uma usada uma vez. Sai no máximo uma por rodada, logo depois do turno de outra criatura. As três seguem o molde do capítulo 5.


O orçamento de uma ação dele é `19 ÷ 4,5` = **`4,2` pontos**, que bate com a linha do `Desastre` na `Orçamento de uma ação, por categoria`.

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
`Golpe por faixa` manda. Veja *Bloco seco*, no capítulo 5.

<!-- ORCAMENTO -->

**Orçamento de uma ação, por categoria**
{: .tab-titulo }

| nível | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |
|---|---|---|---|---|---|
| `2` | seco | seco | seco | seco | seco |
| `5` | seco | seco | seco | seco | seco |
| `10` | seco | `3,8` | `4,2` | `4,9` | `5,1` |
| `15` | `3,1` | `5,8` | `6,2` | `7,1` | `7,6` |
| `20` | `4,2` | `7,6` | `8,4` | `9,3` | `10,0` |
| `25` | `5,3` | `9,6` | `10,4` | `11,8` | `12,7` |
| `30` | `6,2` | `11,3` | `12,4` | `14,2` | `15,1` |

O que cabe na maior ação do sistema, a de `15,1` pontos:

**Condição na maior ação**
{: .tab-titulo }

| se ele comprar | custa | sobra para dado |
|---|---|---|
| uma condição `Leve` | `4` | `11,1` |
| uma condição `Média` | `7` | `8,1` |
| uma condição `Pesada` | `11` | `4,1` |

<!-- FIM ORCAMENTO -->

Uma ação de inimigo aguenta uma condição `Pesada`, e nesse caso ela vira quase só condição.