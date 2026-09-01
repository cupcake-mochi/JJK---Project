# 26 · Bestiário — a máquina de montar inimigo

*Fechada na v0.198. Ela estava no fim da fila desde a v0.36 com uma linha só — "sai da matemática de inimigo que o manual já tem" — e era o único item da fila da mecânica desde a v0.168.*

## 1. O que ela é, e o que ela não é

**Esta peça junta num lugar só os números que montar um inimigo pede.** Até aqui eles moravam em quatro donos — o manual, a peça 1, a peça 19 e o `ESTADO-ATUAL` —, e três dos que a mesa rola toda rodada não tinham dono nenhum: a Defesa do inimigo, o acerto dele e a CD dele.

**Ela é máquina, e não catálogo.** *Decisão do Mizuki na v0.161: o Bestiário sai como máquina mais maldições prontas, e não como recolhimento puro.* **As prontas ficam para a versão seguinte**, e o §8 diz o que falta nelas.

> **A ficha de inimigo é a ficha de personagem sem o Caminho.** *Decisão do Mizuki:* **o inimigo tem refino, tem Passiva, tem aptidão e às vezes tem técnica** — muita coisa que ele enfrenta na obra é feiticeiro, e feiticeiro se monta com as mesmas peças. *O que ele não tem é Caminho, Trilha e poço de PE, e o §6 diz por quê.*

**E a rota que só o inimigo tem é ser maldição.** *O jogador não escolhe isso, em nenhuma das nove rotas de Origem da peça 9.*

## 2. O grau é ficção, e a obra é quem manda nisso

***Decisão do Mizuki: o grau fica na ficha da maldição como rótulo, e não entra em conta nenhuma.*** **A métrica é o nível e a categoria do §4.**

O motivo é a peça 12 §2: *"Grau é reconhecimento; nível é poder"*. Se o grau da maldição parear com o grau do feiticeiro, e o grau do feiticeiro não diz nível, então dois mestres montam o mesmo encontro com fichas de níveis diferentes — que é o filtro que este projeto usa para tudo.

> **⚠ A intuição de parear grau com grau é da obra, e ela está certa lá.** *A escada existe para classificar quatro coisas — feiticeiro, maldição, objeto e ferramenta — e ela nasceu como regra de despacho: manda-se um feiticeiro do grau da maldição.* **O que não atravessa é a metade numérica**, porque aqui o grau é patente e a patente sobe por feito.
>
> **E a obra deixa uma fronteira que a ficha já carrega de graça.** *O que separa uma maldição de grau 2 de uma de semi-grau 1, na classificação da obra, é **saber usar técnica**.* **Isso não é número: é uma linha do §6 desta peça, e ela está na ficha quer o grau exista ou não.** *Então o rótulo tem onde se apoiar sem virar conta.*

## 3. A ficha, e cada linha tem dono

**Treze linhas. Nenhum número novo nasce aqui** — o que esta peça faz é dizer de onde cada um sai.

| linha | valor | dono |
|---|---|---|
| nível | o nível do grupo | o mestre declara antes da mesa |
| categoria | `Ronda` · `Dupla` · `Alcateia` · `Calamidade` | o §4 |
| vida | a linha do manual vezes o fator da categoria | manual, a tabela `Inimigos` |
| **Integridade** | igual à vida máxima | manual, a seção `Inimigos` |
| dano por rodada | a linha do manual vezes o fator da categoria | manual, a tabela `Inimigos` |
| ações por rodada | personagens da categoria menos um, piso `1` | o §4.2 |
| **Defesa** | `10 + Destreza + proteção` | peça 1 §5 |
| **acerto** | `atributo + maestria` | peça 1 §5 |
| **CD** | `8 + atributo + maestria` | peça 1 §5 |
| Reação | uma por rodada, volta no começo do turno dele | manual, a seção `Inimigos` |
| refino | a curva do `meio a meio` | peça 11 §3 |
| Testes de Resistência | dois treinados de quatro | peça 7 §6 |
| deslocamento | `9 m` | peça 3 §3 |

**As três em negrito não tinham dono em documento nenhum até esta peça**, e as três derivam sem escolha — elas não acrescentam número, elas dão nome ao que a peça 1 §6 e a peça 19 §2.5 já mediam do outro lado da mesa.

### 3.1 As três derivadas, nível a nível

**O inimigo carrega a mesma curva de atributo de quem investe** — `3` no nível 2 subindo a `6` no 26 —, e é isso que põe as três no lugar em que as outras peças já as mediam.

| nível do grupo | 5 | 10 | 15 | 20 | 25 | 30 |
|---|---|---|---|---|---|---|
| Defesa | `14` | `16` | `17` | `18` | `19` | `20` |
| acerto | `+4` | `+6` | `+6` | `+8` | `+8` | `+10` |
| CD | `12` | `14` | `14` | `16` | `16` | `18` |
| refino | `1` | `4` | `6` | `7` | `9` | `10` |

**Contra um personagem que investiu em defesa ele acerta `50%` a `55%`, e o Teste de Resistência treinado dele falha `35%`.** *São os mesmos números que a peça 1 §6 publica do lado do jogador, e é isso que prova a derivação: se ela estivesse errada, os dois lados da mesma rolagem discordariam.*

> **A proteção da Defesa anda junto com o refino, pela peça 11 §6** — `1/3 do refino + 1`. *Isso não é enfeite: sem ela a Defesa do inimigo congela e o acerto do personagem deriva `+15` pontos percentuais na campanha, que é o erro que a v0.117 consertou do lado do jogador.*

## 4. A categoria — quantos personagens ele exige

***Ideia do Mizuki, e o eixo é o dele:*** *quantos feiticeiros são precisos para enfrentar aquilo.* **A tabela de inimigo do manual já responde isso para um número — ela é calibrada para quatro —, e a categoria é aquela linha reescalada.**

| categoria | personagens | fator sobre a linha do manual | ações |
|---|---|---|---|
| **`Ronda`** | 1 | `× 0,25` | `1` |
| **`Dupla`** | 2 | `× 0,50` | `1` |
| **`Alcateia`** | 4 | `× 1,00` | `3` |
| **`Calamidade`** | 6 | `× 1,50` | `5` |

**A `Alcateia` é a linha do manual sem tocar em nada.** *As outras três saem dela, e nenhuma inventa número.*

### 4.1 A ficha pronta de cada categoria, nos três níveis que a tabela publica

| categoria | nv 10 | nv 20 | nv 30 |
|---|---|---|---|
| `Ronda` | `119` vida · `6` dano | `201` · `12` | `289` · `18` |
| `Dupla` | `238` · `13` | `402` · `24` | `578` · `36` |
| `Alcateia` | `475` · `26` | `805` · `49` | `1155` · `72` |
| `Calamidade` | `712` · `39` | `1208` · `74` | `1732` · `108` |

### 4.2 As ações saem da frase do manual, e não de escolha

**O manual escreve que o chefe *"perde a ação três vezes por rodada"* contra um grupo de quatro** — ele age uma vez enquanto eles agem quatro. **Então a compensação é `personagens − 1`, com piso `1`:** na `Ronda` ele age uma vez porque o outro lado também age uma vez, e na `Alcateia` ele age três.

> **⚠ E a `Alcateia` não pode descer de `3`, e isso não é desta peça.** *A peça 19 §2.2 preça quatro das treze condições dividindo pelas ações do chefe.* **Com `2` as quatro passam do teto do próprio tier**, e o piso está medido lá, com a checagem `12` daquele validador em cima.

## 5. O câmbio — um corpo grande vale quatro pequenos

**Dentro de uma categoria o mestre troca o corpo único por vários, e a troca é `1` para `4`.** *O capanga é a coluna que a tabela do manual já publica ao lado da do chefe.*

> **Um chefe de `Alcateia` vale quatro capangas do mesmo nível.**

**O `4` foi medido por simulação, com fogo concentrado e o excedente passando para o corpo seguinte.** *No nível 30 o chefe cobra `28%` da vida do grupo em quatro rodadas; quatro capangas cobram `33%` em três.*

**E ele reconstrói por um segundo caminho, que é o método do `Guia do Mestre` de 2014:** *lá o valor de um monstro é a média de um eixo defensivo, dos pontos de vida, com um ofensivo, do dano por rodada.* **Os dois eixos do capanga são `1/5,25` e `1/1,89` da linha do chefe, e a média deles é `1/3,15`** — o mesmo número que a simulação achou, por um caminho que não conversa com ela.

> **⚠ E o câmbio tem um trade-off declarado: o enxame é mais rápido e um pouco mais duro.** *Quatro corpos entregam tudo na primeira rodada e vão morrendo, então eles cobram mais cedo e a luta acaba antes.* **É o mesmo fenômeno que o multiplicador de encontro do 5e de 2014 existia para representar — e que a edição de 2024 apagou por imprecisão.**
>
> **⚠⚠ E a conta que parece óbvia mata o grupo.** *Multiplicar vida por dano e dividir dá `10` capangas por chefe.* **Dez capangas no nível 30 cobram `158%` da vida do grupo** — é a mesa inteira no chão. *Por isso o câmbio está escrito aqui em vez de deixado para quem quiser derivar.*

## 6. O que ele carrega além dos números

***Decisão do Mizuki:*** **o inimigo se monta com as mesmas peças que um personagem, menos o Caminho.** *Na obra a maior parte do que se enfrenta é feiticeiro, e feiticeiro tem técnica, tem aptidão e tem Passiva — se a ficha de inimigo não alcançar isso, metade dos antagonistas não cabe nela.*

| ele tem | de onde sai |
|---|---|
| refino | a curva do `meio a meio`, peça 11 §3 |
| aptidões e Passivas | o catálogo da peça 11, o mesmo que o jogador usa |
| técnica, com Fundamento | o manual, quando ele é feiticeiro ou maldição de técnica |
| Legado, ferramenta, objeto | as peças 13, 16 e 21, quando a ficção pedir |

| ele não tem | por quê |
|---|---|
| Caminho e Trilha | as duas entregam por marco de campanha, e o inimigo não sobe de nível |
| poço de PE | o §6.1 |
| Origem | a peça 9 é a máquina de criação de quem senta na mesa |

### 6.1 O inimigo não conta PE, e a cota de dano é o orçamento dele

**Tudo que ele faz sai do dano por rodada da ficha.** *Uma técnica que causa dano entrega aquela cota e não mais que ela; uma que não causa dano troca parte da cota por outra coisa.*

**O precedente é do `Guia do Mestre` de 2014, e ele é explícito:** *o que um monstro tem é dano por rodada, e como esse dano se divide em ataques é livre.* **Contar PE de inimigo criaria uma segunda economia que só o mestre opera**, e ela responderia diferente em duas mesas.

> **Isso é a regra de ouro nº 6 pelo outro lado.** *O personagem tem um teto de saída por rodada e paga em PE para chegar nele; o inimigo tem o mesmo teto escrito direto, sem a moeda no meio.*

### 6.2 E existe inimigo sem energia nenhuma

**Ele não tem refino, aptidão nem técnica, e a cota de dano vem do corpo.** *É a forma da Restrição Celestial pelo ramo da Maki, do lado de lá da mesa* — **e a ficha não muda de tamanho por causa disso:** a vida e o dano continuam saindo da categoria, porque a categoria mede o que o encontro custa, e não de onde ele tira força.

> **⚠ E aqui a fronteira da obra encosta na mecânica sem virar número.** *O que separa uma maldição de grau 2 de uma de semi-grau 1, na classificação da obra, é saber usar técnica.* **A ficha carrega essa linha na coluna `técnica`**, e o rótulo do §2 fica legível sem entrar em conta.

## 7. O que o `conferir-bestiario.py` confere

| # | o que ela confere |
|---|---|
| **1** | **as âncoras existem nos donos.** Cada número que a ficha usa aparece no documento que esta peça declara como dono, e a tabela do §3 é comparada com a lista do validador nos dois sentidos |
| **2** | **as três derivadas reconstroem.** A Defesa, o acerto e a CD saem das fórmulas da peça 1 §5, com a proteção andando junto do refino — e o resultado tem de bater com os `50%` a `55%` de acerto e os `35%` de falha que a peça 1 §6 publica |
| **3** | **a categoria é cópia com dono.** Vida e dano de cada uma reconstroem da linha do manual vezes o fator, e o fator reconstrói do número de personagens |
| **4** | **as ações saem da frase do manual**, e a `Alcateia` bate com o piso que a peça 19 §2.2 publica. *Se aquele piso mudar, esta acende* |
| **5** | **o câmbio é medido, não guardado.** A simulação de fogo concentrado é rodada aqui dentro, e o `4` publicado tem de ser o que ela devolve |
| **6** | **o grau não vira número.** Nenhuma linha desta peça pode pendurar valor no grau, e o `ESTADO-ATUAL` e a peça 12 continuam dizendo que inimigo não tem grau mecânico |
| **7** | **nenhum valor de regra guardado aqui dentro.** Todo número vem do dono, e a checagem falha se algum sobrar como constante |

### 7.1 As doze perturbações, em cópia isolada

*Com a base conferida verde e com `PULADA` zero antes de cada uma, com o `diff` comparado antes e depois, e com o veredito lido da checagem que estava sendo testada — nunca do código de retorno.*

| checagem | perturbação | esperado | deu |
|---|---|---|---|
| **1.1** | linha nova na ficha do §3 | acende | acende |
| **2** | a Defesa do nível 5 vira `15` no §3.1 | acende | acende |
| **2** | a curva do `meio a meio` muda na peça 11 | acende | acende |
| **2** | a peça 1 §6 perde a oscilação declarada | acende | acende |
| **3** | uma célula de vida do §4.1 vira `999` | acende | acende |
| **3** | o fator da `Dupla` vira `0,60` | acende | acende |
| **4** | a `Alcateia` publica `4` ações | acende | acende |
| **4** | a peça 19 baixa o piso das ações para `2` | acende | acende |
| **5** | a peça publica o câmbio em `cinco` | acende | acende |
| **6** | uma linha viva pendura número no grau | acende | acende |
| **2** | **contra-teste:** mexer em prosa sem mexer em número | fica verde | fica verde |
| **3** | **contra-teste:** a `Calamidade` vira `8` personagens, coerente nas duas tabelas | fica verde | fica verde |

> **O contra-teste da `3` é o que prova a checagem.** *Trocar a `Calamidade` para oito personagens muda o fator para `2,00`, as ações para `7` e as três células de ficha — e a checagem sai verde,* **porque ela mede a derivação e não os números publicados.**
>
> **⚠ E a terceira perturbação achou um defeito na checagem `2` antes de ela valer.** *A tabela da peça 1 §6 amostra os níveis de marco, que são os **picos** da curva de acerto — ela publica `55%` em todas as colunas.* **Medir a banda só por ela dava um ponto só, e o inimigo, amostrado em níveis que não são marco, caía fora dela sem nada estar errado.** *O vale não está na tabela: ele está declarado ao lado, como oscilação irredutível de `5pp`.* **Hoje a checagem lê os dois — o pico da tabela e a oscilação declarada — e a banda sai `50%` a `55%`.**

## 8. Em aberto

- **As maldições prontas.** *A decisão da v0.161 é máquina mais prontas, e esta versão entrega a máquina.* **Quantas, de que categorias e com que técnicas é escolha do Mizuki**, e o catálogo é a versão seguinte.
- **A Expansão de Domínio de inimigo.** *A obra dá domínio a maldição de grau alto, e o manual tem a máquina inteira.* **O que falta é o preço dela contra a cota de dano do §6.1** — ela não causa dano, então ela troca cota por Acerto garantido, e ninguém mediu quanto.
- **O inimigo com Trilha.** *Fica de fora por decisão, e o motivo está no §6* — mas um antagonista recorrente que sobe junto com o grupo é caso de mesa que vai aparecer.
- **A ficha impressa.** *A peça publica as linhas; o `05-material/` é quem transforma isso em bloco pronto para o mestre copiar.*
