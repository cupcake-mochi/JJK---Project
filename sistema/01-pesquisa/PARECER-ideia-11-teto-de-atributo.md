# Parecer · ideia 11 — o teto de atributo e o incentivo da rota `Corpo`

**Pedido do Mizuki em 22/09/2026: validar o quão interessante a ideia é, incluindo as duas
vertentes. NÃO aplicar.** Nada aqui foi para o repositório, e nenhum número do sistema se moveu.

A conta está em `conta-ideia-11.py`, ao lado deste arquivo. **Ela regride contra a tabela de três
fichas da peça 2 §3 antes de medir qualquer coisa** — as três versões anteriores dela, que ficaram
no scratchpad da sessão, tinham um erro de refino inicial que a regressão pegou.

---

## O que a ideia é

O item 11 da fila nasceu de uma frase dele em 20/09/2026, medindo a escada de CD:

> *"o teto é alcançado por darmos de graça, oq tira o incentivo em parte de pegar rota de corpo"*

**A premissa já tinha caído na medida da v0.261**, e o item registra isso: só o atributo
**principal** chega ao teto de graça. Os outros quatro só sobem se o jogador gastar a escolha do
marco — e é exatamente isso que a rota `Corpo` compra.

As duas vertentes que ficaram na fila, sem medida:

- **Vertente A** — a rota `Corpo` estoura o teto em `1`, um atributo por vez.
- **Vertente B** — o teto vira `5`, com o `6` travado atrás da rota `Corpo`.

E o aviso pendurado: **qualquer uma mexe no teto de Defesa `20`**, que a peça 14 §3 deriva do
teto de atributo.

## O método, antes de qualquer número

O simulador reproduz as **seis células** da tabela de três fichas da peça 2 §3 — atributo e
refino das três rotas no nível 30 — **antes** de medir qualquer coisa nova:

| rota | atributo no nv30 | refino |
|---|---|---|
| sempre atributo | `6·6·6·4·1` ✔ | `8` ✔ |
| meio a meio | `6·6·6·1·1` ✔ | `10` ✔ |
| sempre refino | `6·6·2·1·1` ✔ | `10` ✔ |

*A primeira versão dele começava o refino em `2` e dava `9` na rota Corpo contra os `8` publicados.
A regressão pegou, e é para isso que ela existe.*

---

## 1 · A rota `Corpo` já compra bastante, e ninguém tinha medido o quanto

| | Corpo | Refino |
|---|---|---|
| atributo no nv30 | `6·6·6·4·1` | `6·6·2·1·1` |
| refino | `8` | `10` |
| aptidões | `0` | `10` |

**Os dois primeiros atributos são IGUAIS nas duas rotas.** Então a rota `Corpo` **não compra
acerto e não compra Defesa** — ela compra o terceiro e o quarto atributo, que é onde Teste de
Resistência e perícia moram.

E ali ela compra muito: **`+4` no terceiro e `+3` no quarto**. No d20, enquanto não satura, isso é
**20 e 15 pontos percentuais** nos testes daqueles dois atributos.

> ***O que ela paga:*** *o refino no teto e as dez aptidões.* **A troca não é "quase nada contra
> muita coisa" — ela é larga dos dois lados.**

## 2 · ⚠⚠ O ESPELHO NÃO SE MOVE — e isso derruba as duas vertentes como ganho de poder

| regime | Corpo no nv30 | acerto | Defesa | **espelho** |
|---|---|---|---|---|
| **hoje** | `6·6·6·4·1` | `+10` | `19` | **60%** |
| **A · um atributo a 7** | `7·6·6·3·1` | `+11` | `20` | **60%** |
| **A · todos a 7** | `7·7·7·1·1` | `+11` | `20` | **60%** |
| **B · teto 5, o 6 atrás da Corpo** | `6·6·6·4·1` | `+10` | `19` | **60%** |

*Espelho = a rota `Corpo` atacando outra rota `Corpo`.*

**O atributo entra nos DOIS lados da rolagem** — no acerto de quem bate e na Defesa de quem
apanha, via Destreza. Subir o teto sobe os dois juntos, e a taxa não se move um ponto percentual.

É a **lição nº 1 do projeto**, e a peça 1 já escreve ela para este caso exato: *"os dois lados
crescem `+6`, e é por isso que fecha"* — a Defesa ganha `+3` de Destreza e `+3` de proteção, o
acerto ganha `+3` de atributo e `+3` de maestria.

## 3 · Onde o ganho aparece de verdade — e ele é contra UM número

O inimigo da peça 26 monta com **teto `6` fixo** e não tem rota `Corpo`. Defesa dele: `20`.

| regime | Corpo acerta | Refino acerta | separação |
|---|---|---|---|
| hoje | 55% | 55% | **+0%** |
| **A · um atributo a 7** | 60% | 55% | **+5%** |
| **A · todos a 7** | 60% | 55% | **+5%** |
| **B · teto 5, o 6 atrás da Corpo** | 55% | 50% | **+5%** |

**As três variantes entregam exatamente a mesma coisa: `+5` pontos percentuais de acerto para
quem pegou `Corpo`, contra o inimigo.** A vertente A sobe quem investe; a B baixa quem não
investe. O delta é idêntico.

> ***E esse ganho só existe porque o inimigo tem teto fixo.*** *Se a peça 26 subisse o teto do
> inimigo junto — que é o que ela faria, porque ela deriva do jogador —, a separação voltaria a
> zero.* **A ideia não recompensa a rota `Corpo`: ela desconta a Defesa do inimigo, por um caminho
> comprido.**

## 4 · O custo — oito lugares contra um

O teto de atributo é lido por:

| peça | o que ela faz com ele |
|---|---|
| **peça 2 §3** | é a **dona**: teto `6` e a curva que se auto-equilibra |
| peça 6 | o divisor de fatia usa *"teto de atributo em 6"* |
| peça 11 §6 | a Bênção declara que **não** move o teto de Defesa |
| **peça 14 §3** | o teto de Defesa `20` é **derivado** de `10` + teto de atributo + `cobrir(teto de refino)` |
| peça 15 | a invocação herda *"+1 por marco, teto 6"* |
| peça 19 | a comparação com o d20 usa *"atributo 6 + maestria 4 = +10"* |
| peça 22 | o validador de pactos **lê** o teto da peça 2 |
| peça 26 §3 | o inimigo monta com teto `6` |

**A peça 14 é a pior das oito, e pelo melhor motivo:** ela **deriva** o número em vez de copiar.
Mexer no teto de atributo move o teto de Defesa **sozinho**, sem ninguém decidir — e o `19` do
equipamento, que é decisão escrita, passa a estar dois pontos abaixo em vez de um.

Os mesmos `+5` pontos percentuais saem de **um** lugar: a rota `Corpo` dar `+1` de acerto direto,
ou a Defesa do inimigo cair `1` na peça 26. **Razão de 8 para 1.**

## 5 · Cada vertente contra o que o projeto já declarou

### A vertente A contradiz um argumento que a peça 2 §3 publica

> *"Isso também explica por que o teto do atributo não deve crescer com o nível. Um teto que sobe
> junto manteria o ponto de atributo sempre valioso, e a escolha ficaria travada em 'atributo' a
> campanha inteira.* **O teto fixo é o que cria a virada.***"*

A vertente A não sobe o teto com o nível — sobe com a **escolha** —, mas o efeito é o mesmo para
quem escolhe: **o principal nunca satura, então o ponto de atributo nunca perde valor**, e a
escolha de marco trava em `Corpo` para sempre. *É o modo de falha descrito, entrando pela porta
do lado.*

E a medida mostra o sintoma: na vertente A, a rota `Refino` **nunca alcança o teto** — ela fica
em `6` num sistema cujo teto é `7`.

### A vertente B contradiz uma decisão declarada como proposital

A peça 2 §3 escreve, sobre as três rotas: *"Repare que **os três chegam ao mesmo lugar no atributo
principal** — `6` — e divergem em tudo o mais."*

A vertente B existe justamente para quebrar isso. **Não é erro** — é uma decisão de design
diferente, e legítima. Mas ela é uma **reversão declarada**, não um ajuste, e a peça inteira foi
escrita em cima daquela frase.

E ela cobra um preço que a vertente A não cobra: **ela rebaixa o teto de todo mundo de `6` para
`5`**, o que desloca as oito peças para baixo em vez de para cima. O teto de Defesa cairia para
`19`, e o `19` do equipamento — que é decisão escrita — colidiria com a rota livre.

---

## Veredito

**Quão interessante a ideia é, medida:** *pouco, nas duas vertentes, pelo preço que ela cobra.*

| | vertente A | vertente B |
|---|---|---|
| muda o combate entre pares? | **não** — espelho fica em 60% | **não** — espelho fica em 60% |
| separa `Corpo` de `Refino`? | sim, `+5` pontos percentuais | sim, `+5` pontos percentuais |
| esse ganho é real ou é desconto na Defesa do inimigo? | **desconto** | **desconto** |
| quantos lugares toca | **8** | **8** |
| contradiz o que o projeto já escreveu? | sim, o argumento da virada | sim, a igualdade declarada do principal |
| custo extra | o `Refino` nunca alcança o teto | rebaixa o sistema inteiro |

**Entre as duas, a B é a mais defensável** — ela não mata a saturação, cria identidade de verdade
(o `6` vira exclusivo de quem investiu) e não quebra a lição nº 1 mais do que a A. *O preço dela
é ser uma reversão de decisão declarada e mexer para baixo em oito lugares.*

**A A é a mais perigosa**, porque ela parece pequena — *"só `+1`, e só para quem investe"* — e o
que ela faz é tirar o único freio que faz a escolha de marco virar para refino no meio da campanha.

## O que eu faria no lugar

**Nada, por enquanto — e o motivo é que a rota `Corpo` não está fraca.** Ela já compra `+4` e `+3`
em dois atributos, que é `20` e `15` pontos percentuais em Teste de Resistência e perícia. O que
faltava era isso estar **medido e escrito**, e não um incentivo novo.

Se depois do playtest ela parecer fraca mesmo, o conserto barato é o de **um** lugar: a rota
`Corpo` entregar `+1` de alguma coisa que **não** entre nos dois lados da rolagem. *Atributo entra
nos dois; dano por rodada, alcance e deslocamento não entram.*

## O que este parecer NÃO mediu

- **Quanto valem 10 aptidões contra 7 pontos de atributo.** É a comparação que decidiria se as
  rotas estão equilibradas hoje, e ela precisa entrar no catálogo da peça 11 aptidão por aptidão.
  *Sem isso, "a rota Corpo está fraca" continua sem resposta — o que este parecer mostra é que as
  duas vertentes não são o jeito de consertar, e não que não haja o que consertar.*
- **O terceiro eixo do marco, o `Leque`**, que entrou depois da tabela de três fichas. As três
  rotas medidas aqui são as duas antigas; a rota que gasta o marco em feitiço e Passiva não foi
  simulada.
- **O efeito no bestiário inteiro.** Medi contra a Defesa `20` de um inimigo de nível 30; a escada
  de categorias não foi rodada.
