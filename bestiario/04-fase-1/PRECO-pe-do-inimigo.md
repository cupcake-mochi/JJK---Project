> # ⚠ ESTE RELATÓRIO ESTÁ OBSOLETO
> **A recomendação central dele (`PE = 9 × Classe`) foi DESCARTADA em 09/09/2026.**
> O Mizuki decidiu que **o inimigo não conta PE** — o limite é rótulo de frequência.
> A decisão está em `decisoes-fase-1.md` §8. O estado atual está em `ESTADO-onde-paramos.md`.
>
> **Três afirmações dele foram refutadas por verificação de fonte** (`refutacao/prova-*.md`):
> o `2,0×` do PF2e é régua de **área** e não de golpe; o SRD 5.2 nunca deixa recurso pago ser
> comprado por **uma** ação; e a largura também é gratuita no topo da linha de 2025.
>
> *O que continua valendo aqui é o levantamento do campo e as contas de assimetria. Não leia a §6.*

# O preço da energia do inimigo

*09/09/2026. Pesquisa de campo em seis frentes (workflow `pe-do-inimigo`) mais os cálculos.*

> ⚠ **A fase de refutação adversarial não rodou** — ela morreu duas vezes no limite de sessão junto
> com os cálculos, que foram refeitos à mão. **Então estes modelos não passaram por céticos.**
> Trate a recomendação como bem medida e mal atacada.

---

## 1. Como o campo resolve isso

| sistema | o que dá ao inimigo | o que isso custa |
|---|---|---|
| **D&D 5e 2014** | **espaço de magia de verdade**, igual ao do jogador | o Arquimago tem `20` espaços e usa `3` numa luta de 3 rodadas. **`85%` do recurso nunca é gasto** |
| **D&D 5e 2024** | acabou com espaço de magia. Virou `À vontade` e `X/Dia` | o Arquimago 2025 tem `8` magias à vontade e **todas causam zero dano** |
| **D&D 4e** | à vontade / por encontro / recarga | o modo de falha ficou documentado: o chefe vira *"a drone of at-will powers until it finally falls"* |
| **Pathfinder 2e** | espaço de magia existe, mas o livro **manda não preencher** | e diz por quê, literal: *"damaging spells drop off in usefulness for a creature that's expected to last only a single fight"* |
| **Pathfinder 2e** (o único poço real) | Pontos de Foco: **`1` a `3`** | o jogador tem a mesma faixa — **para o dia inteiro** |
| **Draw Steel** | Malice, e ela é do **DIRETOR**, não do monstro. **Poço por encontro alimentado por renda** — *"You can save it up"*, e a sobra evapora no fim ⟵ *corrigido 09/09* | a crítica publicada é literal: *"very book-keepy"*, *"quite tedious"* |
| **13th Age** | nada de poço. A unidade nativa é **`por batalha`** | e o bônus crescente vai para os JOGADORES, não para o monstro |
| **Lancer** | recarga por dado e usos limitados | sem poço |

> **Nenhum dos sete dá ao inimigo o poço DO JOGADOR** — o que tem recuperação, escala por nível e tabela de custo por magia. ⟵ *corrigido 09/09: o Daggerheart, que não estava neste levantamento, dá ao adversário um poço de ENCONTRO (`Stress`, média `3,48`), pequeno e de dupla função.* Os quatro formatos que apareceram
> são: rótulo de frequência sem poço, poço minúsculo de uma luta, poço da mesa que cresce por rodada,
> e poço que reseta todo turno.

## 2. A assimetria, medida

**O jogador orça PE para `10,5` rodadas de luta por dia** — `3` lutas de `3,5` rodadas. **O inimigo vive `3`.**

| nv | Classe | feitiço custa | poço do jogador | PE por rodada de luta | feitiços que cabem em 3 rodadas |
|---|---|---|---|---|---|
| 2 | `1` | `3` | `8` a `12` | `0,8` a `1,1` | `0,8` a `1,1` |
| 10 | `3` | `9` | `40` a `60` | `3,8` a `5,7` | `1,3` a `1,9` |
| 20 | `5` | `15` | `80` a `120` | `7,6` a `11,4` | `1,5` a `2,3` |
| 30 | `7` | `21` | `120` a `180` | `11,4` a `17,1` | `1,6` a `2,4` |

**Mas o inimigo age mais vezes por rodada, e isso quase fecha a conta:**

| lado | ações por rodada | rodadas na vida | **ações totais** |
|---|---|---|---|
| jogador, um dia | `1` | `10,5` | **`10,5`** |
| `Desastre` | `3` | `3` | **`9`** |
| `Calamidade` | `6` | `3` | **`18`** |

> **Um `Desastre` faz `9` ações na vida; o jogador faz `10,5` no dia.** Quase igual. *A diferença é
> que o jogador espalha em três lutas e o inimigo concentra numa.*

## 3. E é por isso que um poço de dia não funciona no inimigo

A literatura de attrition é unânime: **o peso do gasto mora FORA do encontro** — na próxima luta,
na decisão de avançar ou recuar. **O inimigo não tem "fora do encontro".**

> *"Recurso alimentado por tempo, sem pressão de tempo, é efetivamente de graça."*

**O inimigo está sempre em nova.** Dar um poço de dia a ele é formalidade por construção — ele
sempre vai gastar tudo, porque não existe amanhã.

---

## 4. Os quatro modelos

### A — o custo do feitiço dentro do dano

**É o que o Guia do Mestre de 2014 faz, e o divisor é a duração da luta.** Texto exato, p. 278:

> *"If a monster's damage output varies from round to round, calculate its damage output each round
> for the first three rounds of combat, and take the average."*

Exemplo do próprio livro: `(90 + 37 + 37) ÷ 3 = 54`. **A luta padrão do Projeto-M tem 3 rodadas —
o divisor já está pronto.**

O que isso libera, no nível 30, se o feitiço troca UMA ação normal e vale o dobro dela:

| categoria | ações | golpe | feitiço a `2×` | a média da luta sobe | veredito |
|---|---|---|---|---|---|
| `Capanga` · `Ameaça` | `1` | `55` | `110` | `33,3%` | **não cabe** |
| `Desastre` | `3` | `73` | `146` | `11,1%` | cabe |
| `Catástrofe` | `5` | `66` | `131` | `6,7%` | cabe |
| `Calamidade` | `6` | `73` | `146` | `5,6%` | cabe |

> **Quanto mais ações o inimigo tem, mais barato é dar um golpe grande a ele** — porque a média
> dilui. *É o mesmo mecanismo que quebrou a `Dupla`, visto ao contrário.*

**Veredito: sobrevive, e é a espinha da recomendação.**

### B — a segunda tabela de dano (a sua ideia)

**O Pathfinder 2e tem literalmente isso.** A tabela `2-12: Area Damage` tem duas colunas lado a
lado, `Unlimited Use` e `Limited Use`. A razão medida:

| nível | 1 | 5 | 10 | 15 | 20 | 24 |
|---|---|---|---|---|---|---|
| limitado ÷ ilimitado | `1,40×` | `1,75×` | `1,95×` | `2,07×` | `2,24×` | `2,26×` |

**Não é "um pouco maior". É o dobro, e estabiliza em `2,0×` a partir do nível 11.**

E o Level Up (A5E) faz por câmbio explícito: *"For every two points of damage that a limited-use
ability exceeds the damage per turn budget, reduce the total damage dealt on other turns by one."*
**Câmbio de `2` para `1`, deliberadamente favorável à rajada.**

> ⚠ **Mas o número quebra no seu sistema.** Um golpe de `Desastre` a `2,0×` no nível 30 é `146`, que
> é **`60%` da vida de um personagem**. *Você já rejeitou a `Dupla` na mesa com `45%`.*

**Veredito: a mecânica existe no campo, mas na razão que o campo usa ela recria o problema que você
acabou de matar.**

### C — o poço de PE dimensionado para uma luta

Três derivações independentes, no nível 30 com feitiço de `21` PE:

| derivação | resultado |
|---|---|
| (a) proporcional às rodadas: poço do jogador × `3 ÷ 10,5` | `43` PE = `2,0` feitiços |
| (b) por ação: o `Desastre` conjura em `1/3` das `9` ações | `63` PE = `3,0` feitiços |
| (c) por peso: o poço que dá 2 a 3 feitiços | `42` a `63` PE |

> **As três caem entre `43` e `63` PE. Convergem em 2 a 3 feitiços por luta.**

**Veredito: os números fecham, mas sozinho ele tem o defeito do nova — o inimigo despeja tudo na
rodada 1.**

### D — renda por rodada, no molde do Malice

Draw Steel, com 4 heróis e zero Vitórias: rodada 1 = `5`, rodada 2 = `+6` (`11`), rodada 3 = `+7` (`18`).
**E as três features que o livro manda preparar custam `2-3` + `5` + `7-10` = `14` a `18`.**

> **O poço de três rodadas cobre exatamente as três features preparadas, uma vez cada.**

Portado: com renda crescente de `Classe ÷ 3` por rodada, o total dá `2` feitiços e **o pico cai na
rodada 3** — que é onde toda a pesquisa diz que ele deve cair.

**Veredito: resolve o nova, mas cobra o preço que a crítica do Draw Steel nomeia — o mestre rastreia
um número novo toda rodada, e você quer um bloco lido num relance.**

---

## 5. A convergência no TRÊS

| fonte | quantos usos grandes numa luta |
|---|---|
| **a sua `Intervenção`**, decidida antes desta pesquisa | **`3`** por luta, `1` por rodada |
| Draw Steel, Villain Actions | **`3`** por encontro, `1` por rodada, **custo zero** |
| Draw Steel, Malice numa luta de 3 rodadas | `18`, que é o custo das **`3`** features preparadas |
| Pathfinder 2e, Pontos de Foco de criatura | **`1` a `3`** |
| as três derivações do poço, feitas aqui | **`2` a `3`** feitiços |

**Cinco caminhos independentes no mesmo número.** *E um deles é você, que chegou lá sozinho.*

---

## 6. A RECOMENDAÇÃO

> ### O inimigo tem PE, e o poço é exatamente três feitiços da Classe dele.
> ### **PE = `9 × Classe`**

| nv | Classe | feitiço custa | **PE do inimigo** | quantos feitiços | fração do poço de um jogador |
|---|---|---|---|---|---|
| 2 | `1` | `3` | **`9`** | `3` | `90%` |
| 5 | `2` | `6` | **`18`** | `3` | `72%` |
| 10 | `3` | `9` | **`27`** | `3` | `54%` |
| 15 | `4` | `12` | **`36`** | `3` | `48%` |
| 20 | `5` | `15` | **`45`** | `3` | `45%` |
| 25 | `6` | `18` | **`54`** | `3` | `43%` |
| 30 | `7` | `21` | **`63`** | `3` | `42%` |

*Uma linha só no bloco, e ela não muda durante a luta a não ser descendo.*

### E a trava contra o nova você já construiu

O modo de falha é o chefe despejar tudo na rodada 1 e virar saco de pancada. **A `Intervenção` já
resolve: no máximo uma por rodada.**

Com três usos e uma por rodada, a luta de três rodadas gasta um por rodada, **e o pico cai na
rodada 3** — exatamente onde a pesquisa manda ele cair.

> **Não precisa de regra nova. O throttle é a `Intervenção`, que você desenhou antes de saber disso.**

### O que a camada paga compra: LARGURA, não número bruto

**A resposta do D&D 2024, medida nos blocos:**

*Arquimago 2025: `4` ataques à vontade = `108` de dano por rodada, **de graça**. As `8` magias à
vontade dele causam **zero dano**. O `Lightning Bolt` que custa carga dá `42` por alvo e só compensa
a partir de **três** alvos.*

> **A camada paga não é maior contra um alvo. Ela é mais larga.**

E no seu sistema isso é mais barato **e** mais seguro:

| feitiço do `Desastre` nv 30 | alvos | dano total | fatia da vida de cada pessoa |
|---|---|---|---|
| `73` em cada | `1` | `73` | `30%` |
| `73` em cada | `3` | **`219`** | `30%` |
| golpe a `2,0×` num alvo só | `1` | `146` | **`60%`** |

**Três alvos pelo golpe normal entregam `219` — mais que o dobro do golpe a `2×` — e ninguém leva
mais que `30%` da vida.** *É o caminho barato e o caminho seguro ao mesmo tempo.*

---

## 7. O que fica em aberto

**Da conta:**
- O `Capanga` e a `Ameaça` têm uma ação só, e o feitiço a `2×` estoura neles (`33%` de aumento na
  média). **Eles precisam de outra régua, ou não conjuram grande.**
- O poço é por corpo ou por esquadrão no `Capanga`? Oito corpos com `9` PE cada é outra coisa.
- A `Calamidade` dura `4` a `6` rodadas, não `3`. Com `3` Intervenções e `1` por rodada, ela passa
  duas ou três rodadas sem nenhuma. **Isso é bom (o pico fica no fim) ou é o chefe ocioso?**

**Só o Mizuki responde:**
- **A recomendação contraria em parte a sua decisão da v0.220?** Não — o inimigo tem PE, como você
  decidiu. Mas o poço é pequeno e amarrado à `Intervenção`, e não uma segunda economia livre.
- **Você quer a segunda tabela de dano mesmo assim?** Ela existe no campo, e o número dela recria o
  problema da `Dupla`. A alternativa medida é largura.

## 8. Uma pendência do repositório que apareceu no caminho

**A frase do §6.1 está travada por código.** O `manual/matematica/sobrecarga.py` lê a string literal
*"O inimigo não conta PE"* do arquivo da peça 26 e **falha se ela sumir**. Quando esta decisão for
aplicada no repositório, esse script quebra junto.

## Fontes

- Guia do Mestre 2014, p. 278 e 279 (o divisor de três rodadas; o passo 13)
- Manual dos Monstros 2025: blocos do Mago, Arquimago e Lich
- Pathfinder 2e, GM Core, *Building Creatures* — https://2e.aonprd.com
- Draw Steel: Monsters, *Monster Basics* — https://steelcompendium.io
- 13th Age SRD — https://www.13thagesrd.com
- Angry GM e Sly Flourish sobre o chefe que gasta tudo na abertura
- O levantamento completo, com todas as citações, está em `LEVANTAMENTO-pe.md`
