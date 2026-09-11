# Prova p2-mm2014-arquimago — o Arquimago, o Mago e o Lich do MM 5e 2014 (PT)

**Veredito: CONFIRMADO.** A frase do relatório (linha 15 de `PRECO-pe-do-inimigo.md`) —
*"o Arquimago tem `20` espaços e usa `3` numa luta de 3 rodadas. **`85%` do recurso nunca é gasto**"* —
está certa nos três números. Nenhuma correção necessária.

Uma ressalva de honestidade: 3 das 20 magias são marcadas com `*` = conjuradas **antes** do
combate. Se você contar essas como gastas, o desperdício cai de 85% para 70%. Os dois números
estão calculados abaixo; escolha qual publicar.

Fonte: `/tmp/claude-1000/-media-mizuki-HD-Externo-II-Claude-Bestiario/56c72db1-7acc-4db0-bba3-77aa84a51702/scratchpad/livros/MM2014-pt.txt`
(Apêndice B: Personagens do Mestre, p. 340–341, e p. 211 para o Lich).

---

## 1. ARQUIMAGO — bloco literal

Cabeçalho, linhas **21234–21241** e **21246–21257** (o OCR mistura as duas colunas da página;
as linhas abaixo estão limpas da coluna vizinha):

```
ARQUIMAGO
Humanoide Médio (qualquer raça), qualquer tendência
Classe de Armadura 12 (15 com armadura arcana)
Pontos de Vida 99 (18d8 + 18)
Deslocamento 9 m
FOR 10 (+0)  DES 14 (+2)  CON 12 (+1)  INT 20 (+5)  SAB 15 (+2)  CAR 16 (+3)
```

```
Nível de Desafio 12 (8.400 XP)
Conjuração. O arquimago é um conjurador de 18° nível. Sua
habilidade de conjuração é Inteligência (CD de resistência de
magia 17, +9 para atingir com ataques com magia).
```

### Os espaços de magia — citação literal, linhas 21259–21271

```
Truques (à vontade): mãos mágicas, luz, prestidigitação, raio de
   fogo, toque chocante
1° nível (4 espaços): armadura arcana*, detectar magia, escudo
   arcano, mísseis mágicos
2° nível (3 espaços): detectar pensamentos, identificação, névoa
   obscurecente
3° nível (3 espaços): contramágica, relâmpago, voo
4° nível (3 espaços): banimento, escudo de fogo, pele de pedra*
5° nível (3 espaços): cone de frio, muralha de energia, vidência
6° nível (1 espaços): globo de invulnerabilidade
7° nível (1 espaços): teletransporte
8° nível (1 espaços): limpar a mente*
9° nível (1 espaços): parar o tempo
```

Linha **21273**, a nota do asterisco:

```
*O arquimago conjura essas magias sobre si antes do combate.
```

Linhas **21274–21275**:

```
Resistência à Magia. O arquimago tem vantagem em testes de
resistência contra magias e outros efeitos mágicos.
```

### O ataque normal — citação literal, linhas 21276–21279

```
AÇÕES
Adaga. Ataque Corpo-a-Corpo ou à Distância com Arma: +6 para
atingir, alcance 1,5 m ou distância 6/18 m, um alvo. Acerto: 4 (1d4
+ 2) de dano perfurante.
```

**Não existe "Ataques Múltiplos" no bloco.** A seção `AÇÕES` tem uma entrada só — a Adaga — e
logo depois dela começa o texto de sabor (*"Arquimagos são poderosos (e geralmente bem velhos)
conjuradores..."*, linha 21281). Não há Reações e não há Ações Lendárias.

→ **Dano por rodada do ataque normal do Arquimago = 4.** (1d4+2: média real 4,5; o livro
imprime 4, arredondando pra baixo, como é o padrão da 5e.)

---

## 2. A conta

### Total de espaços

```
1°:4  2°:3  3°:3  4°:3  5°:3  6°:1  7°:1  8°:1  9°:1
4+3+3+3+3+1+1+1+1 = 20
```

**20 espaços. CONFIRMADO, exato.**

Comparação de paridade com o jogador: um mago PdJ de 18° nível na 5e 2014 tem
`4/3/3/3/3/1/1/1/1` = 20 espaços. **É o mesmo número, casa por casa.** O monstro herda o poço
do jogador inteiro — que é o achado central do levantamento ("monstro tem espaço de magia igual
ao do jogador"). Confirmado na fonte primária.

### Quanto ele gasta numa luta de 3 rodadas

```
1 feitiço por rodada x 3 rodadas = 3 espaços gastos
3 / 20 = 15,0% gasto
100% - 15% = 85,0% NUNCA é gasto
```

**"usa 3" CONFIRMADO. "85% nunca é gasto" CONFIRMADO, exato, não é arredondamento.**

### A ressalva do asterisco

3 magias têm `*`: `armadura arcana` (1° nível), `pele de pedra` (4° nível), `limpar a mente`
(8° nível). O livro diz que ele conjura essas **antes** do combate. Se você contar esses 3
espaços como gastos:

```
3 (pré-combate) + 3 (na luta) = 6 gastos
6 / 20 = 30,0% gasto  ->  70,0% nunca gasto
```

Os dois enquadramentos são defensáveis. O de 85% mede *o que a luta consome*; o de 70% mede
*o que a criatura consome no dia todo*. Para o argumento do bestiário (o poço é grande demais
para o horizonte da luta) o número honesto e mais difícil de contestar é **70%** — e ele já
ganha a discussão sozinho. Se publicar 85%, vale uma nota de pé dizendo que 3 espaços vão em
buffs pré-combate.

---

## 3. Por que 20 espaços é absurdo — o próprio DMG entrega a prova

O Guia do Mestre 2014 (PT), arquivo
`/tmp/claude-1000/-media-mizuki-HD-Externo-II-Claude-Bestiario/56c72db1-7acc-4db0-bba3-77aa84a51702/scratchpad/livros/DMG2014-pt.txt`,
**linhas 17240–17253**, define o orçamento do monstro num horizonte de três rodadas — literal:

```
   Se o dano causado pelo monstro variar de uma rodada
para a outra, calcule o dano causado por ele a cada
rodada para as três primeiras rodadas de combate e
pegue a média. Por exemplo, um dragão branco jovem
tem um hábito de ataques múltiplos (um ataque de
mordida e dois ataques de garra) que causam uma média
de 37 de dano por rodada, assim como sua arma de sopro
que causa 45 de dano, ou 90, se atingir dois alvos (e
provavelmente vai). Nas três primeiras rodadas de
combate, o dragão provavelmente irá usar sua arma de
sopro uma vez e seu hábito de ataques múltiplos duas,
então, a média de dano causada por ele nas três primeiras
rodadas seria (90 + 37 + 37) ÷ 3, ou 54 de dano
(arredondado para baixo).
```

Isto é o achado que fecha o caso: **o mesmo livro que constrói o monstro só olha 3 rodadas
para precificá-lo — e o Manual dos Monstros dá a ele um poço de 20 espaços dimensionado para
o dia de aventura inteiro de um PdJ.** A régua de construção e o tamanho do recurso não falam
a mesma língua. O desperdício de 85% não é um acidente de mesa; está assado no método.

### E o poço não é reserva, é o corpo do monstro

Tabela `ESTATÍSTICAS DE MONSTRO POR NÍVEL DE DESAFIO`, DMG2014-pt **linha 16951**, linha do ND 12:

```
 12      +4        17 236–250        +8        75–80    17
```

ND 12 pede **236–250 PV** e **75–80 de dano por rodada**. O Arquimago tem 99 PV e uma adaga.
Contas:

| o que ele faz | dano/rodada | % do orçamento ofensivo do ND 12 (77,5) |
|---|---|---|
| Adaga, o único ataque ilimitado do bloco | 4 | **5,2%** |
| Raio de fogo (truque, à vontade), 4d10 @ conj. 18° | 22 | 28,4% |
| Cone de frio (5° nível, espaço limitado), 8d8, 1 alvo | 36 | 46,5% |
| Cone de frio em 3 alvos | 108 | 139,4% |

(O DMG manda contar alvo múltiplo — é o que ele faz no exemplo do dragão branco, onde o sopro
vale 90 por atingir dois alvos.)

⚠ **Duas linhas dessa tabela são derivadas, não citadas.** O bloco do Arquimago **não imprime
dano de truque nem de magia** — só lista os nomes. Os `22` de raio de fogo (4d10) e os `36` de
cone de frio (8d8) vêm da escala de dano dessas magias no Livro do Jogador aplicada ao
conjurador de 18° nível declarado no bloco; **não achei esses números escritos no Manual dos
Monstros**. O único dano por rodada literalmente impresso no bloco do Arquimago é o **4** da
adaga. Se esse ponto for para o relatório, cite só o 4 como fato de fonte primária e marque os
outros dois como conta.

PV: 99 de 243 esperados = **41%** do PV do ND dele.

**Leitura:** o ataque ilimitado do Arquimago entrega 5% do que o nível de desafio dele exige.
Ele só alcança ND 12 gastando o poço em nukes de área. Ou seja, no D&D 2014 o espaço de magia
**não é um recurso opcional em cima de um corpo competente — é o corpo.** O monstro sem poço não
existe. E ainda assim 85% do poço nunca é gasto, porque a luta acaba antes.

Isso é exatamente o modo de falha que o Projeto-M não pode importar: se o PE do inimigo for
o que produz o dano dele, e a luta durar 3 rodadas, o poço precisa ter tamanho de 3 rodadas —
não tamanho de dia.

---

## 4. MAGO (traduzido como **ARCANO**) — bloco literal

⚠ **Nota de tradução:** nesta edição em português o *Mage* virou **ARCANO**, não "Mago". Grep
por "MAGO" não acha o bloco. Índice: o bloco fica na p. 340, Apêndice B.

Linhas **21181–21190** e **21197–21202**:

```
ARCANO
Humanoide Médio (qualquer raça), qualquer tendência
Classe de Armadura 12 (15 com armadura arcana)
Pontos de Vida 40 (9d8)
Deslocamento 9 m
FOR 9 (–1)  DES 14 (+2)  CON 11 (+0)  INT 17 (+3)  SAB 12 (+1)  CAR 11 (+0)
```

```
Nível de Desafio 6 (2.300 XP)
Conjuração. O arcano é um conjurador de 9° nível. Sua habilidade
de conjuração é Inteligência (CD de resistência de magia 14, +6
para atingir com ataques com magia). Ele possui as seguintes
magias de mago preparadas:
```

Espaços, linhas **21203–21210**:

```
Truques (à vontade): mãos mágicas, luz, prestidigitação, raio de
   fogo
1° nível (4 espaços): armadura arcana, detectar magia, escudo
   arcano, mísseis mágicos
2° nível (3 espaços): névoa obscurecente, sugestão
3° nível (3 espaços): bola de fogo, contramágica, voo
4° nível (3 espaços): invisibilidade maior, tempestade de gelo
5° nível (1 espaços): cone de frio
```

Ataque normal, linhas **21213–21216**:

```
AÇÕES
Adaga. Ataque Corpo-a-Corpo ou à Distância com Arma: +5 para
atingir, alcance 1,5 m ou distância 6/18 m, um alvo. Acerto: 4 (1d4
+ 2) de dano perfurante.
```

Conta:

```
4+3+3+3+1 = 14 espaços
3 gastos em 3 rodadas -> 3/14 = 21,4% gasto -> 78,6% nunca gasto
```

Paridade: mago PdJ de 9° nível na 5e 2014 = `4/3/3/3/1` = 14 espaços. **Idêntico.** Segunda
confirmação independente de que o bloco de monstro copia o poço do jogador.

---

## 5. LICH — bloco literal

Linhas **12964–12982** (o cabeçalho está deslocado no OCR de duas colunas: o nome aparece na
12964 e o corpo de regras vem antes, da 12921 em diante):

```
LICH
Morto-vivo Médio, qualquer tendência maligna
Classe de Armadura 17 (armadura natural)
Pontos de Vida 135 (18d8 + 54)
Deslocamento 9 m
FOR 11 (+0)  DES 16 (+3)  CON 16 (+3)  INT 20 (+5)  SAB 14 (+2)  CAR 16 (+3)
Nível de Desafio 21 (33.000 XP)
```

Linhas **12921–12924**:

```
Conjuração. O lich é um conjurador de 18° nível. Sua habilidade
de conjuração é Inteligência (CD de resistência de magia 20, +12
para atingir com ataques com magia). Ele possui as seguintes
magias de mago preparadas:
```

Espaços, linhas **12925–12937**:

```
Truques (à vontade): mãos mágicas, prestidigitação, raio de gelo
1° nível (4 espaços): detectar magia, escudo arcano, mísseis
   mágicos, onda trovejante
2° nível (3 espaços): detectar pensamentos, flecha ácida de Melf,
   invisibilidade, reflexos
3° nível (3 espaços): animar mortos, bola de fogo, contramágica,
   dissipar magia
4° nível (3 espaços): malogro, porta dimensional
5° nível (3 espaços): névoa mortal, vidência
6° nível (1 espaços): desintegrar, globo de invulnerabilidade
7° nível (1 espaços): dedo da morte, viagem planar
8° nível (1 espaços): dominar monstro, palavra de poder atordoar
9° nível (1 espaços): palavra de poder matar
```

Ataque normal, linhas **12947–12953**:

```
AÇÕES
Toque Paralisante. Ataque Corpo-a-Corpo com Magia: +12 para
atingir, alcance 1,5 m, uma criatura. Acerto: 10 (3d6) de dano de
frio. O alvo deve ser bem sucedido num teste de resistência de
Constituição CD 18 ou ficará paralisado por 1 minuto.
```

Conta:

```
4+3+3+3+3+1+1+1+1 = 20 espaços  (mesmo total do Arquimago)
3 gastos em 3 rodadas -> 15% gasto -> 85% nunca gasto
```

O Lich é ND **21** com o **mesmo poço de 20 espaços** do Arquimago, que é ND 12. O poço não
escala com a ameaça — ele escala com o *nível de conjurador*, que é 18 nos dois. Mais uma
evidência de que o espaço de magia no bloco de 2014 é um número herdado da ficha de jogador,
não um orçamento de encontro.

### Achado extra: as Ações Lendárias do Lich são o avô da Intervenção

Linhas **12954–12959**, literal:

```
AÇÕES LENDÁRIAS
O lich pode realizar 3 ações lendárias, escolhidas dentre as opções
abaixo. Apenas uma ação lendária pode ser usada por vez e
apenas no final do turno de outra criatura. O lich recupera as
ações lendárias gastas no começo do turno dele.
```

Opções (linhas 12960–12975): `Truque` (conjura um truque), `Toque Paralisante` (custa 2),
`Olhar Aterrorizante` (custa 2), `Romper Vida` (custa 3, 21 (6d6) necrótico em 6 m).

Isto casa quase palavra por palavra com a Intervenção já decidida: **3 por luta, no máximo 1
por vez, e só depois/no final do turno de outra criatura.** A diferença de desenho é que a do
Lich *recarrega toda rodada* (é renda por rodada, não 3 no total) e tem **preço em pontos**
(1, 2 ou 3 ações), enquanto a Intervenção do Projeto-M é 3 no total, uma vez cada, sem preço —
igual à Villain Action do Draw Steel. Vale citar o Lich como a fonte da forma ("fora do turno,
depois do turno de outro") e o Draw Steel como a fonte da economia ("3, uma vez cada, grátis").
O molde declarado no documento está correto, mas o ancestral em D&D existe e é este.

---

## 6. Resumo dos números verificados

| afirmação | fonte | veredito |
|---|---|---|
| Arquimago tem 20 espaços de magia | MM2014-pt L21259–21271 | **CONFIRMADO** (4+3+3+3+3+1+1+1+1) |
| Arquimago gasta 3 numa luta de 3 rodadas | 1/rodada x 3 | **CONFIRMADO** |
| 85% do recurso nunca é gasto | 3/20 = 15% | **CONFIRMADO**, exato |
| Arquimago tem espaço igual ao do jogador | mago PdJ 18° = 4/3/3/3/3/1/1/1/1 | **CONFIRMADO** |
| ataque normal do Arquimago | MM2014-pt L21276–21279 | Adaga, **4** de dano, sem Ataques Múltiplos |
| Mago ("Arcano") tem 14 espaços | MM2014-pt L21203–21210 | 14; 78,6% nunca gasto; = mago PdJ 9° |
| Lich tem 20 espaços, ND 21 | MM2014-pt L12925–12937 | 20; mesmo poço do ND 12 |

Ressalva única a registrar: **3 dos 20 espaços do Arquimago são buffs pré-combate marcados com
`*`.** Contando eles, o desperdício é 70%, não 85%. Nada mais no bloco contradiz o relatório.

**Correções necessárias no relatório: NENHUMA.**
