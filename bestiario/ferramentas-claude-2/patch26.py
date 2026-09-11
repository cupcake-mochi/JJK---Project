import os, re, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
P = '/media/mizuki/HD Externo II/Claude/Claude 2/sistema/03-mecanica/26-bestiario.md'
T = open(P, encoding='utf-8').read()
ORIG = T

# o numero da nota do §4.5 sai do mesmo modelo do validador (nv30, capangas primeiro)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'proto_min.py')).read())

def troca(old, new):
    global T
    n = T.count(old)
    if n != 1:
        sys.exit(f'!! trecho aparece {n} vez(es): {old[:90]!r}')
    T = T.replace(old, new)

def entre(ini, fim, novo):
    global T
    a = T.find(ini)
    if a < 0 or T.count(ini) != 1: sys.exit(f'!! inicio nao unico/ausente: {ini[:80]!r}')
    b = T.find(fim, a + len(ini))
    if b < 0: sys.exit(f'!! fim ausente: {fim[:80]!r}')
    T = T[:a] + novo + T[b:]

# ---------------------------------------------------------------- §3
troca("| categoria | `Ronda` · `Dupla` · `Alcateia` · `Calamidade` | o §4 |",
      "| categoria | `Capanga` · `Ameaça` · `Desastre` · `Catástrofe` · `Calamidade` | o §4 |")
troca("| vida | a linha do manual vezes o fator da categoria | manual, a tabela `Inimigos` |",
      "| vida | a linha do manual vezes o fator da categoria; a do `Capanga` é o dano do grupo dividido por quatro | manual, a tabela `Inimigos` |")
troca("| dano por rodada | a linha do manual vezes o fator da categoria | manual, a tabela `Inimigos` |",
      "| dano por rodada | a linha do manual vezes o fator da categoria — e menos em quem carrega `Intervenção`, pelo §6.5 | manual, a tabela `Inimigos` |")
troca("| ações por rodada | personagens da categoria menos um, piso `1` | o §4.2 |",
      "| ações por rodada | declaradas pela categoria | o §4.2 |")
troca("| **resistência, vulnerabilidade e imunidade** | custam degrau de categoria, pelo §6.3 | peça 19 §4 |",
      "| **resistência, vulnerabilidade e imunidade** | multiplicam o fator da categoria, pelo §6.3 | peça 19 §4 |")

# ---------------------------------------------------------------- §4
entre("| categoria | personagens | fator sobre a linha do manual | ações |", "### 4.1 A ficha pronta de cada categoria", """| categoria | personagens | fator sobre a linha do manual | ações | `Intervenção` |
|---|---|---|---|---|
| **`Capanga`** | — | `× 0,25` | `1` | não |
| **`Ameaça`** | 1 | `× 0,25` | `1` | não |
| **`Desastre`** | 4 | `× 1,00` | `3` | sim |
| **`Catástrofe`** | 6 | `× 1,50` | `5` | sim |
| **`Calamidade`** | 8 | `× 2,00` | `6` | sim |

**O `Desastre` é a linha do manual sem tocar em nada.** *As outras saem dela, e nenhuma inventa número.* **E o fator e o número de pessoas são a mesma coisa em duas unidades: `personagens = fator × 4`.** *Um inimigo de fator `1,92` exige `7,7` pessoas, e isso se lê sem tabela.*

> **O `Capanga` é a exceção de uma coluna só.** *O fator dele vale para o dano; a vida não sai do fator, sai do dano do grupo dividido por quatro — é o que UM personagem derruba num golpe —, e ele vem em esquadrão de `8` corpos, com a vida num pool só.* **Por isso ele não tem número de personagens: o preço dele é o câmbio do §5.**
>
> **⚠ Esta escada foi refeita no projeto do Bestiário, em 08/09/2026, e substitui a de quatro degraus que esta peça publicou da v0.198 à v0.220.** *`Ronda` virou `Ameaça` e `Alcateia` virou `Desastre`, com os mesmos números; a `Calamidade` de seis pessoas virou `Catástrofe`, e a `Calamidade` de hoje exige oito.* **A `Dupla` morreu:** *ela levava o dobro do orçamento pela mesma porta, e o golpe dela era `1,60 ×` o topo da banda que as outras respeitam.*

""")

# ---------------------------------------------------------------- §4.1
entre("| categoria | nv 10 | nv 20 | nv 30 |", "### 4.2 As ações saem da frase do manual", """| categoria | nv 10 | nv 20 | nv 30 |
|---|---|---|---|
| `Capanga` | `32` vida · `19` dano | `55` · `37` | `78` · `55` |
| `Ameaça` | `97` vida · `19` dano | `165` · `37` | `236` · `55` |
| `Desastre` | `390` · `75` | `660` · `147` | `945` · `219` |
| `Catástrofe` | `585` · `112` | `990` · `220` | `1417` · `328` |
| `Calamidade` | `780` · `150` | `1320` · `294` | `1890` · `438` |

*A vida do `Capanga` é a de UM corpo; o esquadrão tem oito, num pool.*

> **⚠ O arredondamento é meio para BAIXO, e ele é declarado porque não é cosmético.** *Os fatores `0,25` e `1,50` põem **doze das sessenta e três células** desta escala exatamente em `,5`.* **Três lugares calculam isto — a peça, o validador e o gerador do bloco — e cada linguagem arredonda de um jeito:** *o `Math.round` do JavaScript sobe, o `round` do Python vai para o par.* **Sem a regra escrita, os três divergem, e o mestre lê o número em voz alta na mesa.**
>
> **⚠ E a vida do `Capanga` arredonda PARA BAIXO, por inteiro, que é outra regra.** *Um quarto de ponto de vida põe o esquadrão vivo numa rodada a mais, e a rodada a mais custa `11` pontos percentuais de encontro* — **é o mesmo defeito que o §5.1 registra no chefe do nível 2.**

""")

# ---------------------------------------------------------------- §4.2
entre("### 4.2 As ações saem da frase do manual", "### 4.5 A sub-categoria", """### 4.2 As ações são declaradas pela categoria

**O `Desastre` age três vezes, e isso sai da frase do manual:** *o chefe "perde a ação três vezes por rodada" contra um grupo de quatro — ele age uma vez enquanto eles agem quatro.* **As outras quatro categorias têm o número delas escrito na tabela do §4**, e ele não sai de fórmula: *`Capanga` e `Ameaça` agem uma vez, a `Catástrofe` cinco e a `Calamidade` seis.*

> **⚠ Até a v0.220 as ações saíam de `personagens − 1`, com piso `1`, e foi isso que quebrou a `Dupla`.** *A razão `pessoas ÷ (pessoas − 1)` explode embaixo — `2 ÷ 1`, `4 ÷ 3`, `6 ÷ 5` —, e a categoria de duas pessoas levava o dobro do orçamento pela mesma porta, numa ação só.* **Declarando, o defeito não tem por onde nascer.**

> **⚠ E o `Desastre` não pode descer de `3`, e isso não é desta peça.** *A peça 19 §2.2 preça quatro das treze condições dividindo pelas ações do chefe.* **Com `2` as quatro passam do teto do próprio tier**, e o piso está medido lá, com a checagem `12` daquele validador em cima.

""")

# ---------------------------------------------------------------- §4.5
r1, c1 = simula(S30, [(KV30, KD30)] + [(CV30 * 0.915, CD30 * 0.915)])
r2, c2 = simula(S30, [(KV30, KD30)] + [(CV30 * 0.92, CD30 * 0.92)])
p1, p2 = c1 / VG30 * 100, c2 / VG30 * 100
f1 = lambda x: f'{x:.1f}'.replace('.', ',')
entre("### 4.5 A sub-categoria — em quantos corpos o encontro se parte", "### 4.6 O chefe derruba alguém", f"""### 4.5 A sub-categoria — em quantos corpos o encontro se parte

***Ideia do Mizuki:*** *nem todo combate tem mais de um inimigo, e o mesmo encontro pode vir num corpo só ou repartido.* **A categoria diz o TAMANHO; a sub-categoria diz a FORMA.**

| sub-categoria | o chefe fica com | capangas | cobra do grupo |
|---|---|---|---|
| **`sozinho`** | `100%` | — | `67,6%` |
| **`com um apoio`** | `91,5%` | `1` | `67,5%` |
| **`com dois`** | `83,0%` | `2` | `67,4%` |
| **`bando`** | `74,5%` | `3` | `67,3%` |

**A fração não foi escolhida: ela é a que devolve o que o chefe sozinho cobra.** *O projeto do Bestiário varreu `201` frações do chefe em `29` níveis, com o `Capanga` da escada.* **Os três primeiros capangas tomam `8,5%` do chefe cada um — praticamente `1/12`.**

> **⚠ E o câmbio NÃO é linear além de três corpos.** *Do quarto ao sétimo capanga cada corpo passa a tomar de `11%` a `17%` do chefe — `≈ 1/6`* —, **porque um esquadrão cheio cobre os próprios buracos, e cada corpo passa a valer o dobro.** *A tabela para em três de propósito.*
>
> **⚠ As frações saem com uma casa decimal, e isso não é preciosismo.** *Com um capanga, o chefe a `91,5%` cobra `{f1(p1)}%` da vida do grupo em {r1} rodadas, e a `92%` cobra `{f1(p2)}%` em {r2}:* **meio ponto percentual atravessa a borda de uma rodada.**
>
> **⚠ A coluna da direita depende de em que ordem o grupo abate, e a ordem está declarada: os capangas primeiro.** *É o que a mesa faz sozinha — o capanga cai num golpe de um personagem.* **E ela é medida no nível 30, contra a vida do grupo da peça 1.**
>
> **⚠ A primeira forma desta tabela era do capanga da `Alcateia`** — *quatro corpos com um quarto da vida do chefe e um terço do dano, e as frações `100%` · `75%` · `50%` · `25%`.* **Aquele capanga morreu com a escada, e o câmbio `1/4` morreu junto.**

""")

# ---------------------------------------------------------------- §4.6
troca("**Um chefe de `Alcateia` concentrando os três golpes derruba um personagem na rodada `1,11`.**",
      "**Um `Desastre` concentrando os três golpes derruba um personagem na rodada `1,11`.**")
troca("**Numa luta de três rodadas ele derruba `2,70` pessoas se concentrar** — não o grupo inteiro, e mais de uma.",
      "**Numa luta de três rodadas ele derruba `2,70` pessoas se concentrar** — não o grupo inteiro, e mais de uma.\n\n> *Os números desta seção são do modelo sem `Intervenção`. Com ela, a luta de três rodadas entrega o mesmo total — é assim que o fator `0,923` do §6.5 foi calculado —, e as `2,70` pessoas continuam.*")

# ---------------------------------------------------------------- §4.4
entre("| categoria, no nível 26 a 30 | por rodada | ações | o golpe |", "### 4.3 ⚠ A categoria não é intercambiável", """| categoria, no nível 26 a 30 | por rodada | ações | o golpe |
|---|---|---|---|
| `Capanga` | `55` | `1` | `6d8 + 28` |
| `Ameaça` | `55` | `1` | `6d8 + 28` |
| `Desastre` | `219` | `3` | `8d8 + 37` |
| `Catástrofe` | `328` | `5` | `6d10 + 33` |
| `Calamidade` | `438` | `6` | `8d8 + 37` |

*O `Capanga` e a `Ameaça` batem o mesmo golpe, e o que separa os dois é a vida. O `Desastre` e a `Calamidade` também: a `Calamidade` tem o dobro do dano em o dobro de ações. Quem carrega `Intervenção` rola este golpe com o fator do §6.5.*

> **Menos ações quer dizer golpe maior**, *e é por isso que a `Catástrofe` bate menos que o `Desastre`: uma vez e meia o dano, em cinco ações em vez de três.*
>
> ~~**⚠⚠ E ele custa doze dados numa rolagem só, o que é caro em tempo de mesa.**~~ ***RESOLVIDO na v0.216, e não por decreto:*** **o dado deixou de ser sempre `d8`.** *Pedido do Mizuki — "não precisa sustentar pra sempre o `d8`, dá pra usar `d6`, `d4`, `d10`, `d12`, para ajudar nos cálculos".* **O maior punhado da tabela caiu de `12d8` para `8d12`** — *o da `Dupla`, que morreu com a escada; o maior de hoje é `8d8`.*
>
> **Medido nas vinte e sete células que rolavam dado na escada de então:** *a metade cai **exata** em `6` delas contra `0` do `d8` fixo, e o desvio médio não se move — `26,4%` para `25,0%`.* **O balanço é o mesmo; o que melhorou foi a aritmética e a mão.**
>
> **⚠ O teto de oito dados não é cosmético.** *Sem ele o otimizador troca `5d8 + 26` por `10d4 + 24`: fecha melhor na conta e é pior na mesa.*

""")

# ---------------------------------------------------------------- §4.3
entre("### 4.3 ⚠ A categoria não é intercambiável consigo mesma", "### 4.7 O que a CURA do grupo faz", """### 4.3 ⚠ A categoria não é intercambiável consigo mesma

**Quatro `Ameaça` não valem um `Desastre`: elas cobram `0,75 ×` a `0,77 ×` o que ele cobra**, e a razão é a mesma nas sete faixas.

*A causa é que elas morrem em fila e a saída delas despenca — quatro corpos de um quarto entregam tudo enquanto estão os quatro de pé, e depois entregam cada vez menos.* **Somar os fatores dá a linha inteira; jogar os quatro não dá o mesmo encontro.** *E vale no degrau de baixo: duas `Ameaça` cobram `25%` a menos que um corpo de fator `0,50`, pela mesma razão.*

> **É por isso que o `Capanga` não é uma `Ameaça`.** *A `Ameaça` é um quarto do chefe nos dois eixos — um quarto da vida e um quarto do dano —, e o `Capanga` é `1/12` da vida com um QUARTO do dano.* **É essa diferença de um eixo só que faz o câmbio do §5 fechar em oito, e a `Ameaça` parar em `0,76`.**
>
> *Os números são os da escada de antes, com o nome novo: a `Ameaça` tem a vida, o dano e as ações que a `Ronda` tinha, e o `Desastre` os da `Alcateia`.* **O modelo do Bestiário refez a conta na escada viva e devolveu o mesmo `0,75 ×` a `0,77 ×`.**

""")

# ---------------------------------------------------------------- §5 e §5.1
entre("## 5. O câmbio — um corpo grande vale quatro pequenos", "## 6. O que ele carrega além dos números", """## 5. O câmbio — um corpo grande vale oito pequenos

**O `Capanga` é a categoria que vem em bando, e o câmbio diz quantos corpos dele valem um chefe.** *Ele é o da escada: esquadrão de `8` corpos, vida num pool só, uma ação cada.*

> **Um `Desastre` vale oito capangas do mesmo nível.**

**As duas linhas do capanga são derivadas, e nenhuma sai da vida do chefe:**

> **Vida do capanga = o dano do grupo por rodada dividido por quatro, arredondado para baixo.** *É o que UM personagem derruba num golpe.*
> **Dano do capanga = o dano do chefe vezes o fator da categoria** — *o mesmo golpe da `Ameaça`.*

**Com isso o câmbio fecha na aritmética: o esquadrão entrega DOZE golpes de um quarto, e doze quartos são as três rodadas do chefe.** *O grupo derruba quatro corpos por rodada, então o esquadrão bate oito vezes na primeira e quatro na segunda — `8 + 4`. O chefe bate três vezes em cada uma de três rodadas.*

**No nível 30 o chefe cobra `657` de dano em `3` rodadas e o esquadrão cobra `660` em `2`.** *Nas sete faixas os dois ficam a menos de um golpe de capanga de distância.*

> **A simulação roda no validador, e é ela que prova a igualdade.** *Ela não escolhe o `8` — ela confere que o `8` é o número de corpos que devolve o chefe, nível a nível.*

> **⚠ E o trade-off que sobra não é de tamanho: é de FORMA.** *O esquadrão entrega oito golpes na primeira rodada e quatro na segunda; o chefe entrega três em cada uma de três.* **O enxame morde cedo e acaba cedo** — é o mesmo fenômeno que o multiplicador de encontro do 5e de 2014 existia para representar, e que a edição de 2024 apagou por imprecisão.
>
> **E ele precisa de uma trava para não concentrar:** *no máximo `3` corpos do mesmo esquadrão atacam o mesmo alvo por rodada, e do segundo em diante o golpe sai pela metade.* **Sem ela oito corpos entregam mais que a vida inteira de um personagem numa rodada; com ela, menos da metade.** *A trava não encolhe o esquadrão — os oito continuam entregando tudo, só não no mesmo alvo.*

> **⚠ O capanga que esta seção publicou da v0.201 à v0.220 era outro** — *quatro corpos, a vida do chefe dividida por quatro e o dano dividido por três, com a prova dos "nove golpes" (`3 × 3` contra `4 + 3 + 2`).* **Ele era o capanga da `Alcateia`, e morreu com ela.** *Estava certo por dentro; ele só não é o da escada viva. Ficar com um só foi decisão do Mizuki, em 10/09/2026.*

### 5.1 A linha do nível 2 estava um ponto fora, e um ponto era uma rodada

**A seção `Inimigos` do manual escreve a própria regra:** *o chefe sozinho tem cerca de **três vezes** o dano de rodada do grupo em vida, "e é isso que faz a luta contra ele durar três rodadas".* **Seis das sete linhas cumpriam isso exato; a do nível 2 publicava `115` contra os `114` que a regra pede.**

> **⚠⚠ E um ponto de vida custava uma rodada inteira do chefe.** *Com `115` a luta dura `3,03` rodadas, e rodada é inteira na mesa: o chefe age quatro vezes e o encontro cobra `89%` da vida do grupo, contra os `68%` que as outras seis cobram.* **No nível em que o personagem tem `19` de vida.**
>
> *A faixa virou `105 a 123`, com o meio em `114` e o espalhamento em `±7,9%` — dentro dos `±7,4%` a `±9,1%` das outras seis.* **Manual na `v7.25`.** *A checagem `5.2` do validador guarda isso.*

**É o mesmo defeito que a vida do `Capanga` teria sem arredondar para baixo:** *um quarto de ponto de vida põe o esquadrão vivo numa rodada a mais.* **Com o piso, o esquadrão do nível 2 tem `9` de vida por corpo — `38 ÷ 4` dá `9,5`, e fica `9`.**

> **⚠ E a conta que parece óbvia mata o grupo.** *O câmbio não é linear:* **do quarto ao sétimo capanga somado a um chefe inteiro, cada corpo passa a valer o dobro do primeiro**, porque o esquadrão cheio cobre os próprios buracos. *A régua do encontro misturado mora no §4.5 e para em três de propósito.*

""")

# ---------------------------------------------------------------- §6.3
troca("### 6.3 Resistência é vida escondida, e ela custa degrau de categoria",
      "### 6.3 Resistência é vida escondida, e ela multiplica o fator da categoria")
entre("**Um chefe de `Alcateia` imune a `Físicos`", "**O mecanismo é o do `Guia do Mestre` de 2014**", """**Um `Desastre` imune a `Físicos` vira uma luta de `7,50` rodadas**, contra as `3,00` que a categoria promete — *a vida efetiva dele é `2,50 ×` a publicada.* *A ficha diz uma coisa e a mesa joga outra, e com a linha da v0.201 a diferença deixou de ser uma luta mais longa e passou a ser uma luta que o grupo não termina de pé.*

**O fator da categoria é a moeda disso, e ele é contínuo.** *`fator novo = fator × o multiplicador da coisa` — e a leitura sai de graça, porque `personagens = fator × 4`.* **Um `Desastre` que resiste a `Físicos` fica em fator `1,43` e exige `5,7` personagens.**

> **Resistência ao grupo `Físicos` multiplica o fator da categoria por `1,43`.** *Aos `Elementais`, por `1,18`; aos `Especiais`, por `1,05`.*
> **Imunidade a `Físicos` multiplica o fator por `2,50`, e o resultado é um número de pessoas, não um nome.** *Aos `Elementais`, por `1,43`; aos `Especiais`, por `1,11`.*
> **A vulnerabilidade é `1,00×`: não cobra e não devolve.** *O dano daquele tipo dobra contra ele, e nada mais na ficha muda — nem o fator, nem a vida.*
> **Ser imune a uma condição que rouba ação do inimigo, ou que dá desvantagem nos ataques dele, multiplica o fator por `1,20`. Qualquer outra condição custa `1,00×`.**

> **⚠ Um `Desastre` imune a `Físicos` exige `10` personagens, não `4`.** *A edição viva do D&D publica isso zero vezes em `331` blocos — se você vender, saiba que está vendendo o item mais caro do livro.* **É aviso, e não trava.**

> **⚠ A coluna `vulnerabilidade` da tabela é conta de vida efetiva, e não preço.** *Ela diz quanto a luta encurta se o grupo inteiro bater naquele tipo, e a ficha não sabe o que o grupo carrega — por isso não cobra nem devolve.* **`4` de `4` sistemas medidos no Bestiário têm vulnerabilidade, e nenhum mexe no custo de encontro por ela.**
>
> *Até a v0.220 esta seção cobrava em "degrau de categoria". Na escada viva o degrau vai de `1,000 ×` a `4,000 ×`, e três dos quatro preços que ela cobrava não cabiam em degrau nenhum. **A moeda passou a ser o fator.***

""")

# ---------------------------------------------------------------- §6.4
troca("### 6.4 A Expansão de Domínio do inimigo — ela DOBRA a categoria",
      "### 6.4 A Expansão de Domínio do inimigo — ela multiplica o fator por `1,92`")
entre("**E a categoria mede exatamente a coisa que esse número move.**", "> **⚠⚠ E é por isso que o chefe da obra com domínio nunca é enfrentado por quatro.**", """**E a categoria mede exatamente a coisa que esse número move.** *Ela é "quantos personagens ele exige", e `personagens = fator × 4`.* **Então a regra sai em uma linha, sem arredondar nada:**

> **Uma Expansão de Domínio completa multiplica o fator do inimigo por `1,92`** — *e, com ele, quantos personagens ele exige.*

| categoria | exige | com Expansão completa |
|---|---|---|
| **`Ameaça`** | `1` | `1,9` |
| **`Desastre`** | `4` | `7,7` |
| **`Catástrofe`** | `6` | `11,5` |
| **`Calamidade`** | `8` | `15,4` |

**Nenhuma cai num degrau da escada, e isso não é impedimento: a categoria mede pessoas, e o número existe fora da escada do mesmo jeito.** *Os cinco nomes são rótulos num contínuo, e não os únicos pontos onde dá para parar.*

> *Até a v0.220 esta seção arredondava o `1,92` para `2` e dizia que a Expansão "dobra a categoria". Na escada viva "dobrar" só pousa numa categoria de verdade em um caso — do `Desastre` para a `Calamidade` —, e os preços em degrau erravam de `13%` a `40%`.* **A moeda passou a ser o fator.**

""")
troca("*Uma `Calamidade` com Expansão exige **doze** feiticeiros.*", "*Uma `Calamidade` com Expansão exige **`15,4`** feiticeiros.*")
troca("> **Quer manter o tamanho?** *Monte com a linha da categoria de baixo* — uma `Alcateia` com domínio construída com os `109` de dano por rodada da `Dupla` entrega os `109` inteiros, contra os `114` efetivos de uma `Alcateia` normal. **Só a `Dupla` e a `Alcateia` têm linha abaixo para isso.**",
      "> **Quer manter o tamanho?** *Divida o dano por rodada dele por `1,92`* — o domínio devolve o que foi tirado, e o encontro fica o da categoria. **Com o fator contínuo isso vale em qualquer categoria**, e não só nas que tinham degrau embaixo.")

# ---------------------------------------------------------------- §6.5
troca("| **o que dá vida efetiva** | um **degrau de categoria**, pelo §6.3 |",
      "| **o que dá vida efetiva** | **multiplica o fator** da categoria, pelo §6.3 |")
entre("| pontos por ação | `Ronda` | `Dupla` | `Alcateia` | `Calamidade` |", "**`seco` é o piso", """| pontos por ação | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |
|---|---|---|---|---|---|
| nível 2 | seco | seco | seco | seco | seco |
| nível 5 | seco | seco | seco | seco | seco |
| nível 10 | `4,2` | `4,2` | `5,1` | `4,5` | `5,1` |
| nível 15 | `6,2` | `6,2` | `7,6` | `6,9` | `7,6` |
| nível 20 | `8,2` | `8,2` | `10,1` | `9,0` | `10,1` |
| nível 25 | `10,2` | `10,2` | `12,5` | `11,2` | `12,5` |
| nível 30 | `12,2` | `12,2` | `15,0` | `13,5` | `15,0` |

*O golpe entra aqui como a ficha imprime ele — a média do dado do §4.4 —, e quem carrega `Intervenção` entra já com o fator dela.*

""")
troca("— *uma `Alcateia` de nível 5 bate `13,0` num golpe, que é dado e não é feitiço.*",
      "— *uma `Ameaça` de nível 5 bate `2d4 + 5`, dez de média, que é dado e não é feitiço.*")
entre("**A `Dupla` do nível 30 monta `24,2` pontos", "> **⚠ E é aqui que a condição do inimigo se resolve", """**A maior ação de inimigo do sistema é `15,0` pontos — o `Desastre` e a `Calamidade` do nível 30 —, e o teto do jogador naquele nível é `24`.** *Uma ação de inimigo é `62%` do maior feitiço que um personagem monta no mesmo nível, e ele compensa em quantidade: age três, cinco ou seis vezes por rodada, e o jogador age uma.* **Até a v0.220 o topo era a `Dupla`, com `24,2` pontos numa ação só — o degrau que levava o dobro do orçamento pela mesma porta.**

""")
troca("**O rebalanceamento que o Mizuki pediu está na razão entre as categorias, e ele é de quatro para um.** *A mesma aptidão pesa quatro vezes mais numa `Ronda` do que numa `Alcateia`, porque a cota da `Ronda` é um quarto.*",
      "**O rebalanceamento que o Mizuki pediu está na razão entre as categorias.** *A mesma aptidão pesa quase quatro vezes mais numa `Ameaça` do que num `Desastre`: a cota da `Ameaça` é um quarto, e a do `Desastre` leva o fator da `Intervenção`.*")
troca("| ligada a luta inteira, no nível 30 | da cota de uma `Ronda` | de uma `Alcateia` |",
      "| ligada a luta inteira, no nível 30 | da cota de uma `Ameaça` | de um `Desastre` |")
troca("| `Domínio Simples` e `Pétala` · `1 ×` maior Classe | `65%` | `16%` |",
      "| `Domínio Simples` e `Pétala` · `1 ×` maior Classe | `65%` | `18%` |")
troca("| `Extensão de Domínio` · `1,5 ×` maior Classe | `98%` | `25%` |",
      "| `Extensão de Domínio` · `1,5 ×` maior Classe | `98%` | `27%` |")
troca("**No nível 2 a `Extensão de Domínio` custa `193%` da cota de uma `Ronda`, e por isso uma maldição daquele nível que a carregue tem de ser pelo menos uma `Dupla`** — *lá ela cai para `96%`, e cabe.*",
      "**No nível 2 a `Extensão de Domínio` custa `193%` da cota de uma `Ameaça`, e por isso uma maldição daquele nível que a carregue tem de ser pelo menos um `Desastre`** — *lá ela cai para `49%`, e cabe.*")
troca("*`Domínio Simples` ligado uma rodada de três custa `12,0` de dano, que são `5,5%` da cota de uma `Alcateia` e `22%` da de uma `Ronda` — contra os `16%` e `65%` da tabela acima.*",
      "*`Domínio Simples` ligado uma rodada de três custa `12,0` de dano, que são `5,9%` da cota de um `Desastre` e `22%` da de uma `Ameaça` — contra os `18%` e `65%` da tabela acima.*")
entre("#### As que saem de graça, e o número que prova isso", "#### As duas trocas ruins, declaradas e não proibidas", """#### A que sai de graça, e o número que prova isso

**Esta não muda a cota — ela muda a FORMA em que ela chega: em que rodada.** *É o mesmo fenômeno que o §4.4 e o §4.5 já medem.*

> **Habilidade guardada, `1 ×` por luta.** *Ela entrega o dobro de uma rodada e deixa as outras menores: no nível 30 são `438` numa e `110` nas outras duas, e o total é `657` — o publicado.*

#### A `Intervenção` — a ação fora do turno, por cima, e o que ela custa

**De `Desastre` para cima o inimigo carrega três `Intervenções` por luta.** *Cada uma é usada uma vez só, no máximo uma por rodada, logo depois do turno de outra criatura.* **A primeira bate — um pouco menos que uma ação normal; a segunda e a terceira mudam o campo em vez de causar dano.** *`Capanga` e `Ameaça` não têm.*

> **Ela é ação EXTRA, por cima das do §4.2, e se paga no dano: o fator de dano de quem carrega `Intervenção` é multiplicado por `0,923`.**

***As duas ideias fixas são do Mizuki:*** *"Inimigo tem ações"* e *"Intervenções são ações extras em meio aos turnos dos alvos. Nenhum sistema come ação do turno para ter essas 'intervenções', e é por um motivo."* **O `0,923` saiu da forma que o campo constrói:** *medidas `9` villain actions em `3` criaturas `Solo` do Draw Steel, a primeira abre com dano e as outras duas mudam o campo — `0,75` de ação extra numa luta de três rodadas.* **Com ele, o total da luta volta ao da tabela, e as `2,70` pessoas do §4.6 continuam.**

> **⚠ Até a v0.220 esta peça dizia o contrário: "as ações fora do turno saem das que ele já tem, nunca por cima".** *A medida daquela versão — `0,94 ×` a `1,07 ×` sobre `81` durações de luta — media a ação fora do turno tirada da cota, e ela continua certa para aquela leitura.* **A leitura mudou, e com ela o preço.**

#### A área — uma ação por rodada, e a `Recarga` não conta

> **No máximo `1` das ações dele por rodada pode ser em área. Ação de `Recarga` não conta nessa cota.** *Vale em toda categoria, e não muda com o nível.*

**Com `1` ação em área, todo mundo leva perto de metade da vida e a luta continua sendo uma luta; com `2`, o alvo termina a luta com `0,3%` de vida.** *E o `2,70` do §4.6 não existe em área: concentrando, a queda é uma curva; em área, é um penhasco — ou ninguém cai, ou a mesa inteira.*

> **A `Recarga (5-6)` é o rótulo do d20: a ação sai uma vez e volta no começo do turno dele com `5` ou `6` no `d6`, e ela ocupa uma das ações dele — não vem por cima.** *Uma área em recarga dispara `1,67 ×` numa luta de três rodadas e vale `0,557` de uma à vontade, então ela já se paga sozinha.* **Cobrar a cota em cima seria cobrar duas vezes.**

*Até a v0.220 esta peça dizia que "área reparte a cota, e não multiplica ela", e que a recarga `5-6` não cabia aqui.* **As duas saíram em 10/09/2026, com a trava acima.**

""")
troca("*Ele gasta a rodada e abre mão de `219` de dano; ganha `H` de vida, que alonga a luta em `H ÷ 315` rodadas, e cada rodada a mais entrega `219`.* **Então `H` de cura vale `0,70 × H` de dano**",
      "*Ele gasta a rodada e abre mão de `202` de dano — os `219` da linha com o fator da `Intervenção`; ganha `H` de vida, que alonga a luta em `H ÷ 315` rodadas, e cada rodada a mais entrega `202`.* **Então `H` de cura vale `0,64 × H` de dano**")
troca("gastar a rodada em algo que não é dano rende `0,70 ×` do que aquilo vale.", "gastar a rodada em algo que não é dano rende `0,64 ×` do que aquilo vale.")

# ---------------------------------------------------------------- §7
troca("| **3** | **a categoria é cópia com dono.** Vida e dano de cada uma reconstroem da linha do manual vezes o fator, e o fator reconstrói do número de personagens |",
      "| **3** | **a categoria é cópia com dono.** Vida e dano de cada uma reconstroem da linha do manual vezes o fator, e o fator reconstrói do número de personagens. *Desde a v0.221 o `Capanga` entra por outra porta: a vida dele é o dano do grupo dividido por quatro, para baixo* |")
troca("| **4** | **as ações saem da frase do manual**, e a `Alcateia` bate com o piso que a peça 19 §2.2 publica. *Se aquele piso mudar, esta acende* |",
      "| **4** | **as ações são declaradas**, e a categoria de fator `1,00` bate com o piso que a peça 19 §2.2 publica. *Se aquele piso mudar, esta acende* |")
entre("| **5** | **o câmbio é medido, não guardado.**", "| **5.2** |", """| **5** | **o câmbio é medido, não guardado.** A simulação de fogo concentrado é rodada aqui dentro, com o `Capanga` derivado do dano do grupo e do dano do chefe, e o `8` publicado tem de ser o que ela devolve. *E o capanga que a tabela `Inimigos` do manual publica tem de ser esse mesmo — desde a v0.221, quando o capanga da `Alcateia` morreu* |
""")
troca("| **5.1** | **a coluna da sub-categoria reconta.** As quatro formas do §4.5 são simuladas com os capangas abatidos primeiro, e as porcentagens publicadas têm de ser o que a simulação devolve.",
      "| **5.1** | **a coluna da sub-categoria reconta.** As quatro formas do §4.5 são simuladas com os capangas abatidos primeiro, e as porcentagens publicadas têm de ser o que a simulação devolve — desde a v0.221 com uma casa decimal, e com o `Capanga` da escada.")
troca("e a peça tem de declarar em que moeda a resistência se paga. *Sem essa declaração ela é vida de graça, e a categoria passa a mentir sobre o encontro* |",
      "e a peça tem de declarar em que moeda a resistência se paga — desde a v0.221 o multiplicador do fator, e o declarado tem de ser o calculado. *Sem essa declaração ela é vida de graça, e a categoria passa a mentir sobre o encontro* |")
troca("A `9.1` reconstrói as `28` células do orçamento de feitiço do golpe dividido pelo que um ponto vale",
      "A `9.1` reconstrói as `35` células do orçamento de feitiço do golpe dividido pelo que um ponto vale, com o fator de quem carrega `Intervenção`")

# ---------------------------------------------------------------- §8
entre("- ~~**A Expansão de Domínio de inimigo.**~~", "- **O inimigo com Trilha.**", """- ~~**A Expansão de Domínio de inimigo.**~~ ***FECHADA na v0.204, e refeita na v0.221:*** **ela multiplica o fator por `1,92`**, porque o Acerto garantido multiplica a saída efetiva por `1,92 ×`. *A primeira forma cobrava em degrau de categoria e só cabia em duas das quatro categorias da escada de então; a moeda passou a ser o fator, e ela cabe em qualquer uma.*
""")

open(P, 'w', encoding='utf-8').write(T)
print('ok — peça 26 reescrita;', len(ORIG), '->', len(T), 'caracteres')
