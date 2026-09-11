# A `Sobrecarga` — **FECHADA**

*Decisão do Mizuki, 09/09/2026. Opção `A`, degrau `Leve`, Reação inteira.*

---

# O texto

> ## `Sobrecarga` · `Leve`
> ### *Até o fim do próximo turno do alvo, ele não usa Reação, e o feitiço dele sai com a CD `2` menor.*

**Mudou uma oração.** *"o feitiço dele custa o dobro de energia"* saiu; *"ele não usa Reação"* entrou.
**A metade da CD não se move.**

---

## O que a decisão fecha, em cinco linhas

| # | |
|---|---|
| **1** | **a metade morta morreu.** *"o dobro de energia"* valia `0,00` contra inimigo e `4,50` esperado contra jogador — `6,2%` de uma ação de chefe |
| **2** | **o degrau é `Leve`**, e isso **fecha a divergência aberta desde a v0.219** no lado de `2` dos `3` donos (o gerador e o `.docx` já diziam `Leve`; o livro dizia `Pesada`) |
| **3** | **a frase que a v0.217 tirou da `Dívida` sai daqui também.** *A checagem `5` do `conferir-acao.py` proíbe `"o dobro de energia"` de voltar na `Dívida` e não olhava pra cá* |
| **4** | **a `Intervenção` não foi tocada.** *Reação é resposta, Intervenção é iniciativa* — a separação continua inteira |
| **5** | **o `sobrecarga.py` caduca.** A seção `METADE 1` dele mede *"o dobro de energia"*, que deixou de existir |

---

# Por que a `Reação`, e não as outras seis

## 1 · É o único alvo que 100% do bestiário tem e que nenhuma outra peça já vende

| | |
|---|---|
| **zero** blocos têm PE | a peça 26 §6.1, e a decisão de 09/09 (`decisoes-fase-1.md` §8) |
| **todos** têm Reação | peça 3 §2: *"uma, e ela volta no começo do seu turno"*. **É constante — tanto que o `RASCUNHO-4` tirou a linha do bloco por ser constante** |
| **nenhuma** das `13` condições nega só a reação | o `Atordoado` nega ação **e** reação juntas, e é `Pesada` |
| **nenhuma** das `9` `Auxiliares` nega reação | medidas uma a uma em `MEDIDA-a-metade-morta.md` §5 |

## 2 · O preço já estava publicado no próprio sistema, ao centavo

**A âncora que faltava não precisou ser inventada: ela é derivável do `Atordoado`.**

> O texto do `Atordoado` é *"você perde a Ação Padrão **e não usa reação**"*, e quem tem mais de uma
> Ação Padrão *"perde **uma**, não todas"*. A tabela das treze publica **`1,5` ações negadas** e
> **`109,50`** de dano.
>
> ### `1,5 − 1,0` = `0,5`. **A `Reação` do inimigo vale meia ação — `36,50` de dano por rodada.**
> *Confere: `1,5 × 73,00` = `109,50`, que é o número impresso na peça 19.*

**E o irmão de preço bate ao centavo:**

| | entrega | degrau |
|---|---|---|
| o **`Trava`**, já publicado | **`36,50`** | **`Leve`** |
| a `Sobrecarga` nova, a metade da Reação | **`36,50`** | `Leve` |

*Não é coincidência de conta: **desvantagem tira metade de um golpe, e a Reação é meia ação.** Duas
rotas diferentes pra mesma metade.*

**A Melhoria inteira, somada:** `2,23×` → `2,64×` contra o filtro de `3,00×` da peça 19 §2.2. **Passa.**

## 3 · É o precedente externo mais forte de tudo que foi medido

*Cinco sistemas, texto de regra com URL nos três `fonte-*.md`.*

| sistema | o efeito | o preço |
|---|---|---|
| **D&D 5e 2014** | `Shocking Grasp` — *"it can't take reactions until the start of its next turn"* | **truque, nível `0`** |
| **Weird Wizard** | `Prone`, aplicado por `Knockdown` | **opção de ataque universal, custo zero** |
| **Draw Steel** | `Entropy Ward` | **passiva de nível `1`, de graça** |
| **Draw Steel** | `Dazed` | **`3` de recurso, nível `1`, em quatro classes** |
| **LANCER** | `JAMMED` — mata reação, ataque e tech | **`1` quick action, licença `LL1`** — o tier mais baixo |
| **PF2e** | `Laughing Fit` | **grau `Success`** — e `Failure` é que adiciona `slowed 1` |
| **Daggerheart** | `Hypnotic Shimmer` | nível `3`, `Recall 1` |

> ### O `Laughing Fit` é a prova mais limpa.
> *"**Success:** It can't use reactions. **Failure:** The target is slowed 1 and can't use reactions."*
> **A Paizo preçou "nega a reação" e "nega a reação MAIS uma ação" no mesmo feitiço, um grau de
> distância.** *Reação é mais barato que ação, e a diferença é exatamente um degrau.*

## 4 · E a troca tem validação literal do campo

**O `Counterspell` de 2024 é o efeito mais famoso de "drenar recurso do inimigo" que o D&D tinha. A WotC reescreveu ele pra drenar AÇÃO:**

> *"the action, Bonus Action, or Reaction used to cast it is wasted. **If that spell was cast with a
> spell slot, the slot isn't expended.**"*

**E o monstro de PF2e TEM poço gastável — spell slots e Focus Points impressos no bloco — e a Paizo
nunca publicou nada que drene isso.** *Só `Counterspell`, troca `1:1`.*

---

# A redação, resolvida

### A janela — e ela não precisa de regra nova

**A `Reação` *"volta no começo do seu turno"* (peça 3 §2).** Então *"até o fim do próximo turno do
alvo"* cobre:

| quando | o que acontece |
|---|---|
| da conjuração até o turno dele | ele não responde a nada |
| **no começo do turno dele** | a Reação **volta**, e cai na trava de novo |
| no fim do turno dele | a trava acaba, e a Reação volta de verdade |

**É a mesma janela do `Atordoado`, e é a janela que a `Sobrecarga` já tinha.** *Zero regra nova.*

### A colisão de nome — registrada, não fatal

**`Reação` tem dois significados no sistema, e isso é anterior a esta decisão:**

| onde | o que quer dizer |
|---|---|
| peça 3 §2 | o **slot de ação** |
| `partD.js` linha `136` e o livro linha `745` | uma **Melhoria `Pesada`** — *"Você conjura como Reação, a um gatilho que você declara"* |

> ***"Ele não usa Reação"* lê como o slot.** E um feitiço comprado com a Melhoria `Reação` cai junto,
> **porque ele gasta o slot** — que é coerente, e é o que o `Slow` do D&D faz.

*A skill `redacao-acessivel-rpg` é explícita sobre **uma coisa por nome**. O termo agora tem três
aparições, e vale amarrar no glossário: `Reação` = o slot; `Melhoria Reação` = sempre com a palavra
"Melhoria" na frente.*

### Na boca do mestre

> **"Sobrecarga. Até o fim do teu próximo turno, você não responde a nada — e o teu feitiço sai com `2` de CD a menos."**

*Ele está sobrecarregado: não sobra fôlego pra reagir. **Isso se narra em quatro palavras**, e é o
critério que o nome `Intervenção` passou.*

---

# O que NÃO entrou, e por quê — pra não voltar

| candidata | morreu porque |
|---|---|
| **tranca uma ação** | **é o `Calado` e o `Enfeitiçado`**, publicados em `Média` a `2,32×`. Vender por Melhoria o que o catálogo já vende é duplicar |
| **tranca ação + reação** | **é o `Atordoado`**, publicado em `Pesada`, palavra por palavra |
| **"o golpe custa o dobro de AÇÃO"** *(o câmbio do §6.1)* | dá no mesmo: `1` ação a menos. **É o `Calado` com outra ficção** — e contra inimigo de `1` ação tira a rodada inteira |
| **tranca a `Intervenção`** | **três sistemas recusam vender isso como efeito genérico** — ver abaixo |
| **`−2` no acerto dele** | **boa opção, e foi a vice.** Perdeu no sabor: *"Sobrecarga"* não diz *"ele erra mais"*. **A medida dela fica guardada** em `MEDIDA-a-metade-morta.md` §3.2 |
| **drena o `refino`** | entrega `3,45`. **Mas cada aptidão lê o refino com teto próprio** (peça 11 §1), então o mesmo `−3` faz coisa diferente em cada bloco — **falha o filtro dos dois mestres** |
| **"a `Recarga` não recarrega"** | o valor depende de **qual** habilidade aquele bloco pendurou no rótulo. Não tem número único |
| **um medidor que SOBE** *(a saída do LANCER)* | *"medidor que enche, não poço que esvazia"*. **É a porta que o campo aponta, e ela reabre a §8** — o molde Daggerheart foi visto e descartado em 09/09 |

### Por que a `Intervenção` morreu como alvo — e foi o campo, não a conta

| sistema | |
|---|---|
| **D&D, as duas edições** | **nenhuma** opção de jogador tira Ação Lendária. *2014: "it can't use them while incapacitated or otherwise unable to take actions"* · *2024: "The monster can't take a Legendary Action if it has the Incapacitated condition"*. **A única porta é a condição mais caríssima do jogo, e ela nunca vem sem duas ou três travas** |
| **Draw Steel** | a Villain Action é **inalcançável**: no bloco o campo de ação dela é literalmente `-`. **A prova:** ~`10` features de Malice escrevem *"They can use this feature even if they are dazed"* — **quando eles querem furar o `Dazed`, eles escrevem.** A Villain Action não tem cláusula: é imune por omissão |
| **Weird Wizard** | `Stunned` diz *"cannot use actions or reactions"* — **e o bloco do dragão AINDA escreveu na mão** *"provided [it] is neither stunned nor unconscious"* pros fury tokens. **A regra genérica não alcança a economia especial fora do turno** |
| **Draw Steel, o sinal mais claro** | reduzir Malice está na caixa de **variantes opcionais** — *"You could allow heroes to spend hero tokens to reduce the amount of Malice you have"* — **ao lado de "crítico só no 20 natural"** |

> ### **A ação fora do turno se governa no bloco do inimigo, não numa Melhoria genérica de feitiço.**
> *E isso é coerente com a decisão que já estava tomada: a `Intervenção` não se mexe.*

---

## E o que fica aberto — duas coisas, nenhuma desta Melhoria

| # | |
|---|---|
| **1** | ⚠ **a `Intervenção` tem DUAS leituras.** Pelo §6.1 ela *sai da cota* e adiciona `0,00`; mas ela age **fora do turno**, e aí é uma 4ª ação — o chefe faria `292` em vez de `219`, **`+33%` na luta inteira**. *As duas frases estão escritas em documentos diferentes. Vai pra fila: é buraco de bestiário* |
| **2** | a **`Precisão`** vende *"+2 na rolagem de acerto, **ou** +2 na CD"* pelo mesmo `Leve`, e **as duas metades dela diferem por `4×`** (`20%` contra `5%`). *Não é preço errado — um feitiço só pega uma das duas —, mas quem conjura ataque leva `4×` mais daquele `Leve`. Registrado, não é desta fila* |

---

## As mexidas no repositório

**Três donos do texto e cinco dependências.** *A lista completa, com a ordem que não trava o commit,
está em `MEXIDAS-no-repositorio.md`.*

> ⚠ **Nada disso foi mexido.** O repositório `Claude 2` é fonte de leitura aqui.
