# A `Sobrecarga` — a metade morta, medida

*09/09/2026. Conta rodada em `medir-a-metade-morta.py`, saída completa em `SAIDA-da-medicao.txt`.*

> **O script não guarda número nenhum.** Cada âncora é lida do documento dono, no molde do
> `manual/matematica/sobrecarga.py`. Se uma sumir do dono, ele sai com erro em vez de sair com
> número velho.

---

## 1. A primeira coisa que a conta achou, e ela muda o conserto

**A metade morta não está morta só contra inimigo.** Ela está morta de um lado e quase morta do outro.

| "o feitiço dele custa o dobro de energia" | vale |
|---|---|
| contra **inimigo** | **`0,00`** — ele não conta PE (peça 26 §6.1) |
| contra **jogador, se ele paga** | `9,00` de dano por rodada |
| contra **jogador, se ele conjura Classe 0** | **`0,00`** — o dobro de zero é zero |
| **o ESPERADO contra jogador** | **`4,50`** |

**O `4,50` sai do próprio manual.** Ele escreve que o conjurador *"gasta PE em cerca de metade das
rodadas de luta do dia"* e chama o Classe 0 de *"o golpe de todo turno em que o PE precisa ser
poupado"*. **Metade das rodadas × `9,00` = `4,50`** — que é `6,2%` de UMA ação de chefe.

> ### ⚠ Então não é meia Melhoria quebrada. É uma metade que vale `6%` de uma ação dos dois lados da mesa.

**E isso muda o tamanho do conserto.** Pendurar uma cláusula *"contra inimigo, em vez disso…"* deixa
de pé, do lado do jogador, a frase que a **v0.217 já tirou da `Dívida` por dobrar zero** — e a
v0.219 registrou que a checagem 5 do `conferir-acao.py` proíbe essa frase de voltar na `Dívida` e
**não olha para esta**.

**Substituir a metade inteira é uma linha, não duas.** E fecha o buraco que o projeto já fechou uma vez.

---

## 2. A régua, e ela já estava escrita

A peça 19 §2.2 tem **duas perguntas separadas**, e a segunda é o teste:

> **1. O NÍVEL é quantas ações da rodada do alvo a coisa nega** — *meia ação é `Leve`, uma é `Média`, uma e meia é `Pesada`.*
> **2. O TESTE é de dominância** — *quanto ela nega ÷ o dano que aqueles pontos dariam*, contra o filtro de `3,00×`.

**As âncoras, lidas do dono:**

| âncora | valor | dono |
|---|---|---|
| chefe no nível 30 | `219` de dano por rodada, em `3` ações | `DESENHO-trilhas.md` |
| **UMA ação do chefe** | **`73,00`** | derivado: `219 ÷ 3` |
| 1 ponto de feitiço | `4,50` de dano | peça 19 §2.1 |
| preço na Classe 7 | `Leve` `4` · `Média` `7` · `Pesada` `11` pontos | peça 19 §2.1 |
| filtro de dominância | `3,00×` | peça 19 §2.2 |
| `−2` na CD | nega `5%` daquele feitiço, em qualquer taxa de TR | derivado do `d20` |

### A âncora que ninguém tinha escrito: quanto vale a `Reação` do inimigo

**Ela não existe como número em documento nenhum. Mas ela é derivável do `Atordoado` publicado, e fecha exata.**

O texto do `Atordoado` é *"você perde a Ação Padrão **e não usa reação**"*, e a célula seguinte diz
*"quem tem mais de uma Ação Padrão no turno perde **uma**, não todas"*. A tabela das treze publica
**`1,5` ações negadas** e **`109,50`** de dano.

> **`1,5 − 1,0` = `0,5`.** A `Reação` do inimigo é **meia ação** — `36,50` de dano por rodada.
> *Confere: `1,5 × 73,00` = `109,50`, que é o número publicado. O script aborta se o texto do
> `Atordoado` parar de dizer "não usa reação", porque aí a derivação perde o chão.*

---

## 3. As oito candidatas, medidas

*A Melhoria entrega as DUAS metades, então o total é `candidata + a CD 2 menor`. A CD vale `3,65` no
piso (1 ação pede TR) e `10,95` no teto (as 3 pedem). **A `AC` é a única exceção, e o §3.2 diz por quê.***

| cód | o que ela nega | ações | entrega | degrau pela regra 1 | dominância | passa o filtro? |
|---|---|---|---|---|---|---|
| **`R`** | **trava a `Reação` da próxima rodada** | `0,50` | **`36,50`** | **`Leve`** | `2,23×` → `2,64×` | **sim** |
| **`AC`** | **`−2` no ACERTO dele, na mesma janela** | `0,60` | **`43,80`** | **`Leve`** | `0,61×` → `2,43×` | **sim** |
| `A1` | tranca **uma ação** da próxima rodada | `1,00` | `73,00` | `Média` | `2,43×` → `2,67×` | sim |
| `A15` | tranca uma ação **e** a `Reação` | `1,50` | `109,50` | `Pesada` | `2,29×` → `2,43×` | sim |
| `I-0` | tranca a `Intervenção` — *leitura "sai da cota"* | `0,00` | **`0,00`** | — | `0,20×` → `0,61×` | sim |
| `I-1` | tranca a `Intervenção` — *leitura "é ação extra"* | `1,00` | `73,00` | `Média` | `2,43×` → `2,67×` | sim |
| `D2` | o golpe dele custa o **dobro de ação** | `1,00` | `73,00` | `Média` | `2,43×` → `2,67×` | sim |
| `RF` | **refino `−3`** (um degrau de proteção) | `0,00` | `3,45` | — | `0,39×` → `0,80×` | sim |

> **A `AC` não estava na tua lista.** *Ela entrou porque é o **espelho da metade que fica**: a
> `Sobrecarga` já dá `−2` na CD dele; dar `−2` no acerto também faz a Melhoria virar **uma ideia
> só** — `−2` nas duas rolagens de ataque dele. E o irmão publicado é exato: a `Precisão` vende
> `+2` em uma das duas por `Leve`.*

### Três delas não são candidatas: são condições que já existem

| | |
|---|---|
| **`A1`** | negar uma ação **é** o `Calado` e o `Enfeitiçado`, publicados em `Média` a `2,32×` |
| **`A15`** | negar ação + reação **é** o `Atordoado`, publicado em `Pesada` a `2,21×`, palavra por palavra |
| **`D2`** | *"custa o dobro de ação"* dá no mesmo: `1` ação a menos. É o `Calado` com outra ficção |

**Vender por Melhoria uma condição que o catálogo já vende é duplicar entrada, não consertar feitiço.**

### E duas não são alvo reproduzível

**O `refino` (`RF`) entrega `3,45` por degrau de proteção** — tamanho de `Desarmado`. *Mas o problema
não é o tamanho:* **cada aptidão lê o refino com teto próprio** (peça 11 §1: *"cada aptidão declara
o próprio teto — nem toda uma usa o valor cheio"*). Então o mesmo `−3 de refino` faz coisa
diferente em cada bloco, e **falha o filtro do projeto**: dois mestres que nunca conversaram não
chegam ao mesmo número.

*E ele é métrica estática, não poço. Drenar refino no meio da luta faz a `Defesa` impressa no bloco
ficar errada — é bookkeeping no lugar onde o projeto acabou de tirar bookkeeping.*

**O rótulo de frequência** (*"a `Recarga` não recarrega nesta rodada"*) tem o mesmo defeito por outro
caminho: o valor depende de **qual** habilidade aquele bloco pendurou no rótulo. Não tem número
único.

### 3.2 ⚠ A assimetria que a conta achou sem procurar: `2` pontos no acerto valem `4×` o que valem na CD

**São os mesmos dois pontos no mesmo `d20`, e eles não valem a mesma coisa.**

| os mesmos `−2` | negam | por quê |
|---|---|---|
| na **CD** dele | **`5%`** daquele golpe | Teste de Resistência bem-sucedido ainda entrega **metade** |
| no **acerto** dele | **`20%`** daquele golpe | golpe que erra entrega **zero** |

*`10` pontos percentuais ÷ `2` = `5` de um lado; `10` pontos percentuais ÷ `50%` de acerto base = `20%` do outro.*

> **E é por isso que a `AC` não se soma com a metade da CD.** *Um golpe ou **rola acerto** ou **pede
> Teste de Resistência** — nunca os dois.* **Então a Melhoria inteira nega `10,95 + 10,95k`, com `k`
> sendo quantas das ações dele rolam acerto:**

| `k` — ações dele que rolam acerto | nega | em `Leve` | em `Média` |
|---|---|---|---|
| `0` — tudo pede Teste de Resistência | `10,95` | `0,61×` | `0,35×` |
| **`1`** — **o bloco do Sukuna** | **`21,90`** | **`1,22×`** | `0,70×` |
| `2` | `32,85` | `1,83×` | `1,04×` |
| `3` — tudo rola acerto | `43,80` | `2,43×` | `1,39×` |

**O `k=1` não é hipótese: é o único bloco preenchido que o projeto tem.** *O Sukuna do
`03-bloco/RASCUNHO-1-o-bloco.md` tem `Corte` rolando acerto e `Desmantelar` e `Fuga` pedindo Teste
de Resistência.*

> ### E aqui está o argumento da `AC` que nenhuma outra candidata tem
> **A metade da CD, sozinha, é condicional também** — ela só morde ação que pede Teste de
> Resistência. *No bloco do Sukuna ela pega `2` das `3` ações e erra a terceira.*
> **Com o acerto junto, a Melhoria passa a pegar o inimigo qualquer que seja a mistura dele.**
> *A peça 26 §3 deriva `acerto` E `CD` para todo bloco — as duas rolagens estão sempre lá.*

*⚠ Fica registrado, porque apareceu no caminho e não é desta fila: a `Precisão` vende `+2 na rolagem
de acerto, ou +2 na CD` pelo mesmo `Leve`, e as duas metades dela diferem por `4×`. Não é preço
errado — um feitiço de ataque só pode pegar uma das duas —, mas quem conjura ataque leva `4×` mais
daquele `Leve` que quem conjura Teste de Resistência.*

---

## 4. ⚠ A `Intervenção` tem DUAS leituras, e o projeto não decidiu qual

**Esta é a descoberta que não era sobre a `Sobrecarga`.**

| leitura | o texto que sustenta | quanto a `Intervenção` ADICIONA |
|---|---|---|
| **sai da cota** | peça 26 §6.1: *"Tudo que ele faz sai do dano por rodada da ficha"* | **`0,00`** |
| **é ação extra** | `a-intervencao.md`: ela acontece **fora do turno**, logo é uma 4ª ação na rodada | **`73,00`** |

**As duas estão escritas, em documentos diferentes, e ninguém as encostou uma na outra.**

> **Se a leitura certa é "ação extra", o chefe faz `292` numa rodada em que intervém, e não `219`.**
> *Com `3` Intervenções numa luta de `3` rodadas — uma por rodada — isso é `+33%` de dano na luta
> inteira, por fora da escada.*

**Isso é um buraco no bestiário, não uma escolha desta Melhoria.** *Mas ele decide o preço de
`I-1`, então fica registrado aqui e vai pra fila.*

---

## 5. O bairro — e ele é o que decide o degrau

**A `Sobrecarga` não é uma Condição. Ela é uma `Auxiliar`.** A banda de `2,18×` a `2,67×` do §2.2 é
da família *Condição* — e **ninguém tinha medido a família dela.**

| `Auxiliar` | degrau | entrega | dominância |
|---|---|---|---|
| **`Trava`** | `Leve` | `36,50` | **`2,03×`** |
| `Guarda` | `Média` | `14,60` | `0,46×` |
| `Impulso` | `Leve` | `5,75` | `0,32×` |
| `Firmeza` | `Média` | `9,12` | `0,29×` |
| `Enfraquece` | `Média` | `7,50` | `0,24×` |
| `Abre Ferida` | `Leve` | `3,65` | `0,20×` |
| `Ecoa` | `Média` | `5,75` | `0,18×` |
| `Pressa` | `Média` | `3,60` | `0,11×` |

> **`Leve` publicada: `0,20×` a `2,03×`. `Média` publicada: `0,11×` a `0,46×`.**
> **A família `Auxiliar` é muito mais fraca que a família `Condição`** — e a `Média` mais forte dela
> entrega `0,46×`, menos de um quarto da `Média` mais fraca das condições.

### E o `Trava` é o irmão exato

> **O `Trava` dá desvantagem num golpe do alvo. Isso vale `36,50` — que é, ao centavo, o que a `Reação` do chefe vale.**
> **E o `Trava` é `Leve`, publicado.**

*Não é coincidência de conta: desvantagem tira metade de um golpe, e a `Reação` é meia ação. Duas
rotas diferentes para a mesma metade.*

---

## 6. O outro lado da mesa — e aqui a candidata `R` se separa das outras

*Um jogador tem `1` Ação Padrão, `1` Ação Bônus, `1` Reação e movimento (peça 3).*

| a mesma linha, contra um JOGADOR | vale |
|---|---|
| tranca a **`Reação`** dele | **`11,50`** — um ataque de oportunidade, um golpe simples |
| tranca a **Ação Padrão**, se ele ia atacar | `23,00` — dois golpes |
| tranca a **Ação Padrão**, se ele ia conjurar | **`108,00`** — a Rotina do nível 30 |

> ### Trancar a `Reação` é a única das três que cabe no MESMO degrau nos dois lados da mesa.
> `36,50` contra chefe e `11,50` contra jogador — e os dois são **meia ação do dono**, que é `Leve`
> pela regra 1.

**Trancar uma ação não cabe, e a conta mostra por quê:** contra o chefe tira `1/3` da rodada; contra
o jogador tira a rodada **inteira**. *É `Atordoado`, e `Atordoado` é `Pesada`.* **A mesma frase
produziria dois tamanhos diferentes dependendo de quem está do outro lado** — que é exatamente o
defeito que a metade morta já tem hoje, virado do avesso.

---

## 7. A mordida por categoria — o mesmo texto, cinco blocos

*Nível 30. A `Reação` é sempre **uma**, pela peça 3 — é constante pra todo inimigo do bestiário.*

| categoria | dano/rodada | ações | 1 ação | a `Reação` | **% da rodada dele** |
|---|---|---|---|---|---|
| `Ameaça` | `55` | `1` | `55,00` | `27,50` | **`50,0%`** |
| `Desastre` | `219` | `3` | `73,00` | `36,50` | `16,7%` |
| `Catástrofe` | `328` | `5` | `65,60` | `32,80` | `10,0%` |
| `Calamidade` | `438` | `6` | `73,00` | `36,50` | `8,3%` |
| `Capanga` (um corpo) | `55` — *`6d8 + 28`, médio* | `1` | `55,00` | `27,50` | `50,0%` |

**A mordida relativa cresce quando o inimigo tem menos ações — e isso não é defeito desta
Melhoria.** *É o que o §2.2 já publica para as quatro condições que cobram ação: "cada ação a menos
encarece as quatro na mesma proporção".* **O comportamento é o que o sistema já tem.**

---

## 8. E ela resolve uma divergência que estava aberta desde a v0.219

**O degrau da `Sobrecarga` tem dois donos e eles discordam:**

| dono | diz |
|---|---|
| `manual/gerador/partD.js` | **`Leve`** |
| o `.docx`, gerado do `partD.js` | **`Leve`** |
| `sistema/05-material/livro/manual/40-fundamento.md` | **`Pesada`** |

*É uma das vinte e cinco divergências que a v0.219 achou, e a única que é de DEGRAU.*

> **A escolha da metade nova decide qual lado ganha, sem ninguém ter que arbitrar:**
> **as duas finalistas — a `R` e a `AC` — caem em `Leve`, que é o lado de `2` dos `3` donos.**

*Se a escolha fosse `A15`, o degrau seria `Pesada` e o lado do livro ganharia. Mas `A15` é o
`Atordoado` palavra por palavra.*

---

## 9. O que a medida NÃO decide

### As duas finalistas, lado a lado

| | **`R` — trava a `Reação`** | **`AC` — `−2` no acerto** |
|---|---|---|
| **entrega contra chefe** | `36,50`, **invariante** | `10,95` a `43,80`, pela mistura do bloco |
| **no bloco do Sukuna** | `36,50` | `21,90` |
| **degrau pela regra 1** | `Leve` | `Leve` |
| **dominância em `Leve`** | `2,23×` → `2,64×` | `0,61×` → `2,43×` |
| **irmão publicado** | o `Trava`, `Leve`, **`36,50` ao centavo** | a `Precisão`, `Leve`, `±2` na mesma rolagem |
| **mesmo degrau contra jogador?** | **sim** — `11,50` é meia ação dele também | **sim** — todo mundo rola acerto |
| **morde 100% dos blocos?** | **sim** — a `Reação` é constante (peça 3) | **sim** — as duas rolagens sempre existem |
| **quantas ideias a Melhoria passa a ter** | **duas** — perde a reação, e `−2` na CD | **uma** — `−2` nas duas rolagens de ataque dele |
| **efeito novo na família `Auxiliar`?** | **sim** — nenhuma Melhoria hoje nega reação | **não** — é a `Precisão` ao contrário |
| **cabe no nome "Sobrecarga"?** | sim: ele está sobrecarregado, não consegue responder | mais fraco: "sobrecarga" não diz "erra mais" |

### E o degrau ainda é escolha, nas duas

| degrau | a `R` | a `AC` | o que isso significa |
|---|---|---|---|
| **`Leve`** | `2,23×` → `2,64×` | `0,61×` → `2,43×` | acima do `Trava` (`2,03×`), o teto atual da família |
| **`Média`** | `1,27×` → `1,51×` | `0,35×` → `1,39×` | acima de toda `Média` publicada (teto `0,46×`), abaixo de meia `Leve` |

**As quatro combinações passam o filtro de `3,00×`.** *`Leve` é fiel à regra 1 e ao degrau que 2 de 3
donos já imprimem; `Média` é fiel ao tamanho do resto da família.* **É decisão do Mizuki.**

### E existe uma terceira opção: as duas juntas

**A `Reação` é slot de ação e o `−2` é rolagem — elas não disputam nada entre si, então aqui somam.**

`0,50` ação (a `Reação`) + `0,60` ação (o `−2` no acerto) = **`1,10` ação negada, que é `Média` pela regra 1.**

| `k` | nega | em `Leve` | em `Média` | em `Pesada` |
|---|---|---|---|---|
| `0` | `47,45` | `2,64×` | `1,51×` | `0,96×` |
| **`1`** — *o Sukuna* | **`58,40`** | `3,24×` ⚠ | **`1,85×`** | `1,18×` |
| `2` | `69,35` | `3,85×` ⚠ | `2,20×` | `1,40×` |
| `3` | `80,30` | `4,46×` ⚠ | `2,55×` | `1,62×` |

> **Em `Média` a combinação cabe em todo `k`, com teto em `2,55×`.** *Em `Leve` ela estoura o filtro
> a partir de `k=1` — ou seja, já no primeiro bloco real.*

**⚠ O custo da combinação é a divergência:** ela é `Média`, e **nenhum** dos três donos escreve
`Média` hoje. *O gerador e o `.docx` dizem `Leve`, o livro diz `Pesada`.* **A divergência da v0.219
não se fecha — ela vira um terceiro valor.**
