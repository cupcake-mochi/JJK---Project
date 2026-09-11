# O eixo do `tamanho`, exercitado — item `16`

*10/09/2026. Conta em `exercitar-o-tamanho.py`, saída em `SAIDA-o-tamanho-exercitado.txt`.*

> **O Sukuna é `Médio` — o único degrau que não carrega número.** *O
> `ACHADOS-o-teste-de-ponta-a-ponta` registrou isso no fecho: "`Grande`, `Imenso` e `Colossal`
> continuam sem bloco de exemplo".*
>
> **Rodei os quatro degraus nos `29` níveis, cruzando com a fórmula que constrói a Defesa.**
> ### E o `Colossal` não existe.

---

# O que a medição achou

| # | o achado | tamanho |
|---|---|---|
| **`1`** | ⚠⚠ **o `Colossal` é INCONSTRUÍVEL em `29` de `29` níveis** — a fórmula da Defesa não desce até onde a troca pede. *Nem no nv30* | **o maior** |
| **`2`** | o **`Imenso` é inconstruível em `8` de `29`** — nv`2` a nv`9` | **grande** |
| **`3`** | e por não pagar, ele **ganha de graça**: o `Colossal` paga `3` dos `7` pontos que deve na faixa de baixo | **grande** |
| **`4`** | 🆕 **o `tamanho` DEVOLVE ponto de atributo**, e isso não está em conta nenhuma. *E ele é a saída do achado `2` do teste do Sukuna* | **grande, e é bom** |

---

# `1` · A Defesa tem PISO de fórmula, e o `tamanho` pede abaixo dele

**A fórmula, peça 1 §5:** `Defesa = 10 + Destreza + proteção`

**E o atributo tem piso `0`** — *os nove pontos da criação se **compram**, e ninguém deve ponto pro
sistema.* **Então a menor Defesa construível é `10 + 0 + proteção`.**

| nv | proteção | Defesa base | **piso da fórmula** | o `Colossal` pede | fecha? |
|---|---|---|---|---|---|
| `2` | `1` | `14` | **`11`** | **`7`** | **NÃO** |
| `10` | `2` | `16` | **`12`** | `9` | **NÃO** |
| `20` | `3` | `18` | **`13`** | `11` | **NÃO** |
| `30` | `4` | `20` | **`14`** | **`13`** | **NÃO** |

> ### O `13` que a `MEDIDA-o-tamanho` publica é UM PONTO abaixo do que a fórmula constrói.
> *E ele é o **melhor** caso — a `MEDIDA` fechou a troca com Defesa base `20`, que é o nível `26` a
> `30`, o topo da tabela.*

**No nv2 o buraco é de `4` pontos.**

---

# `2` e `3` · Quantos ele deve, e quantos ele paga — **sem modelo nenhum**

*Esta conta não depende de como se preça um ponto de Defesa. Ela é a fórmula contra a tabela.*

| tamanho | deve | nv`2`–`9` | nv`10`–`17` | nv`18`–`25` | nv`26`–`30` |
|---|---|---|---|---|---|
| `Grande` | `2` | **`2` de `2`** | `2` de `2` | `2` de `2` | `2` de `2` |
| `Imenso` | `4` | ⚠ `3` de `4` | `4` de `4` | `4` de `4` | `4` de `4` |
| **`Colossal`** | `7` | ⚠⚠ **`3` de `7`** | `4` de `7` | `5` de `7` | ⚠ `6` de `7` |

> ### O `Colossal` paga menos da METADE na faixa de baixo, e nunca paga tudo em faixa nenhuma.
> **`Grande` é o único degrau que fecha em todo nível.**

---

# `4` · 🆕 E o `tamanho` devolve PONTO DE ATRIBUTO — que o produto não vê

**A Defesa lê a Destreza.** *Se a Defesa cai, a Destreza obrigada cai junto — e os pontos voltam pro
orçamento.*

**O achado `2` do teste do Sukuna dizia:** *"no nv20 as derivadas comem **todos** os `4` marcos, e
sobram `3` pontos de `13` pra cor."*

## No nv20:

| tamanho | Defesa | Destreza obrigada | **pontos devolvidos** | sobra pra cor |
|---|---|---|---|---|
| `Médio` | `18` | `5` | `+0` | `3` |
| `Grande` | `16` | `3` | **`+2`** | `5` |
| `Imenso` | `14` | `1` | **`+4`** | `7` |
| `Colossal` | `13` | `0` | **`+5`** | **`8`** |

> ### O `Colossal` quase TRIPLICA o orçamento de cor, e isso não está em conta nenhuma.
> *O produto do `tamanho` conta alcance, alvos e Defesa. **Não conta atributo.***

## E isso vira uma coisa boa

**O achado `2` do Sukuna era uma reclamação:** *"se o mestre quiser um chefe que resista a veneno E a
controle mental E seja forte, no nv20 ele não tem orçamento."*

> ### O `tamanho` É a saída, e ninguém tinha visto.
> **Um chefe `Imenso` ou `Colossal` tem orçamento de cor de verdade** — `7` ou `8` pontos em vez de
> `3`. *E isso casa com a ficção sem forçar nada: o bicho enorme é lento e burro de propósito, e o que
> sobra vira Constituição, Essência, resistência.*

**⚠ Mas é ganho não preçado.** *Enquanto ele não entrar na conta, o `Colossal` é mais barato do que a
tabela diz por DUAS portas — a Defesa que ele não paga e o atributo que ele recebe de volta.*

---

# AS SAÍDAS, com o número de cada uma

| # | a saída | o que ela custa |
|---|---|---|
| **`A`** | **o `Colossal` corta `2` vizinhos em vez de `3`** *(a própria `MEDIDA` ofereceu no §3)* | ele vira o ganho do `Imenso` e fecha com `−4`. **Mas `−4` só é construível de nv`10` pra cima** — sobra o buraco do nv`2` ao nv`9`. *E o `Colossal` deixa de ter degrau próprio: **ele VIRA o `Imenso`*** |
| **`B`** | **cada degrau ganha piso de nível** e só existe onde a Defesa fecha | `Grande` nv`2` · `Imenso` nv`10` · **`Colossal` NUNCA**. ***A saída `B` mata o `Colossal`*** |
| **`C`** | **o `tamanho` para de pagar em DEFESA e passa a pagar em VIDA**, como os seis papéis | fecha em `100%` dos níveis, exato: `Grande × 0,823` · `Imenso × 0,698` · `Colossal × 0,606`. **Custa a FICÇÃO** — um bicho de `6 m` deixa de ser mais fácil de acertar |
| **`D`** | **híbrido por faixa** — a Defesa cai o que a fórmula deixar, o resto vira vida | mantém a ficção **e** fecha. *Custa uma coluna por faixa de nível: `12` números em vez de `3`* |
| **`E`** | **híbrido FIXO** — a Defesa cai `−3` *(o maior corte que fecha em todos os `29`)*, o resto vira vida | **uma tabela só, quatro linhas, construível em todo nível.** *Custa: `Imenso` e `Colossal` ficam com a MESMA Defesa e se separam em vida e em alvos* |

## A saída `E`, com o número

| tamanho | deve | **Defesa** | falta | **`vida ×`** *(teto)* |
|---|---|---|---|---|
| `Médio` | `0` | `+0` | `0` | `1,000` |
| `Grande` | `2` | **`−2`** | `0` | `1,000` |
| `Imenso` | `4` | **`−3`** | `1` | **`≤ 0,909`** |
| `Colossal` | `7` | **`−3`** | `4` | **`≤ 0,683`** |

> ⚠ **O `vida ×` é TETO, não valor final.** *Ele sai do câmbio LINEAR, e a `MEDIDA-o-tamanho` preça
> Defesa em câmbio CONVEXO — "cada ponto custa mais que o anterior". **Como os pontos que faltam são
> os ÚLTIMOS, os mais caros, o convexo cobra mais que isso.***
>
> **O número final tem de ser rodado no câmbio convexo da `MEDIDA`, que este script não reconstrói.**

---

# ⟹ A recomendação, e o porquê

> ## `E`.

**Ela é a única que mantém as DUAS coisas que já estão publicadas:**

| | |
|---|---|
| **a ficção** | *"bicho grande é mais fácil de acertar"* — e ela sobrevive de `Médio` a `Grande`, que é onde a mesa mais sente |
| **o invariante** | fecha em todo nível, e sem tabela por faixa |

**E ela usa a moeda que o projeto inteiro já usa.** *O `Capanga` acabou de mostrar que vida é a moeda
dos seis papéis; o `tamanho` é o ÚNICO eixo que paga em Defesa, e é o único que bate num piso de
fórmula.* **Não é coincidência.**

> ⚠ **E qualquer saída que se escolha precisa preçar o achado `4` também** — o ponto de atributo
> devolvido. *Senão o `Colossal` continua barato por uma porta que ninguém fechou.*
