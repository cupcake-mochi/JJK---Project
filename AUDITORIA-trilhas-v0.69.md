# Auditoria da Q3 de Trilhas — pedida na v0.69

*Não é peça, não é rascunho e não mexe em nada. É o levantamento que responde às quatro perguntas do Mizuki, com a conta rodada duas vezes e o levantamento externo em fonte primária. Depois de decidido, o que sobrar disto vira entrada de CHANGELOG e o arquivo sai.*

**Base conferida antes de qualquer conta:** dezesseis validadores + `conferir-repositorio.py` + `pac7.py` e `v7.py`, todos verdes, `python-docx` instalado, **zero PULADAs**.

---

## O veredito, em uma linha

**O esqueleto está de pé e não se joga fora. O que não sustenta é o preço — a régua da Q3 reformulada não consegue reprovar nada, e é por isso que ela parece construir.**

---

## 1. A régua não tem poder de reprovar, e a prova é aritmética

A Q3 reformulada confere `botão × taxa` contra a fatia. O problema é que **a taxa é o grau de liberdade**, e ela é escolhida depois de você saber o alvo:

> dado um botão `b` e uma fatia alvo `f`, existe sempre `t = f/b`.
> A igualdade não é checagem — é a definição de `t`.

Rodado contra as oito famílias que o permitido da peça 5 §4 autoriza, com o valor medido no §6.9:

| botão | vale | taxa que fecha uma fatia | reprova? |
|---|---|---|---|
| exceção de ação — uma ação a mais | `108,00` | `1,17%` | não |
| duração — `+1` rodada num efeito de 5 | `21,60` | `5,87%` | não |
| troca do fixo por atributo | `21,55` | `5,88%` | não |
| alvo — o golpe simples pega 2 | `11,50` | `11,02%` | não |
| acerto — `+1` no seu acerto | `5,40` | `23,47%` | não |
| recuperação — `+1 PE` | `5,14` | `24,66%` | não |
| posicionamento — `+3 m` | `1,80` | `70,42%` | não |
| posicionamento — `+1,5 m` | `0,90` | `140,83%` | não |

**Zero de oito.** Inclusive a exceção de ação, que a matriz proíbe por escrito nas três Trilhas do Evocador — ela passa na régua de preço com `1,17%`, e quem a barra é uma trava escrita à mão do lado de fora.

**E o Servo prova isso de dentro.** O §6.10 usa `15%` no nível 27 e o §6.10 termina dizendo *"falta o gatilho do nível 27, que é o que fixa os 15%"*. **A taxa foi escolhida antes do gatilho existir** — não porque alguém trapaceou, mas porque é o único jeito de a conta fechar. É a lição nº 8 numa camada nova: a checagem se mede contra a constante que ela mesma produz.

> **Só duas taxas do projeto inteiro saem de documento:** `100%` (a definição de permanente, peça 11 §4) e `30%` (`1×` por descanso curto contra a luta de `3,3` rodadas do §3.2). **Todo o resto é livre.**

### O que o hobby cobra por essa mecânica, e o projeto não cobra

Ela não é nova: é a **Limitação** do GURPS — comprar um poder e descontar pelo quanto ele fica indisponível. O `Accessibility` (B110) é literalmente a taxa de disparo, com tabela de porcentagem de tempo. E o sistema que roda isso há quarenta anos carrega **duas travas que este projeto não tem**:

| trava do GURPS | o que ela faz | existe aqui? |
|---|---|---|
| **teto de `-80%` no total de limitações** | nenhum desconto passa disso — o piso efetivo de taxa é **20%** | **não** |
| o mestre recusa limitação que não limita de verdade | julgamento humano sobre a taxa declarada | **proibido** — é o filtro multi-mestre |

**Os `15%` do Servo são um desconto de `85%`. Em GURPS eles seriam ilegais por dois pontos percentuais.**

E o piso de `20%` **não é número estrangeiro**: é exatamente onde a escada de Classe Passiva do §3.1 já parava (`100%` · `27%` · `20%`). O método novo furou o próprio piso sem ninguém decidir isso.

**O que o piso compra, medido:** com `20%` mínimo, `uma ação a mais` passa a custar **`17,04` fatias** contra um orçamento de `4` — **ela reprova sozinha**, e a trava da matriz que hoje é escrita à mão passa a cair da conta. As outras sete continuam cabendo.

---

## 2. Uma das quatro entregas está saindo de graça

O `Servo` do §6.10 tem quatro entregas. A do nível 2 é utilidade e não tem preço. **As três pagas somam `5,07`, que é o orçamento de quatro fatias.**

| leitura | consequência |
|---|---|
| o orçamento é `4` fatias | **a entrega do nível 2 é grátis** |
| o orçamento é `3` fatias | **o `Servo` estoura em `+33%`** |

Não existe leitura em que os dois fechem. E como nenhum dos cinco eixos da matriz mede utilidade, **toda Trilha é estritamente melhor pondo utilidade num dos quatro slots** — isso é dominância, e ela sai verde.

### E o `nunca vai existir conversão` é falso justamente neste caso

O §3.4-B escreve que utilidade *"entra sem preço em dano, porque não existe conversão e nunca vai existir"*. A entrega do `Servo` é **ser treinado numa perícia ou num TR**, e o projeto tem número para isso:

| o que o treino dá | em pontos percentuais de d20 |
|---|---|
| TR treinado (`+2`) | **10 pp** |
| perícia treinada, nv2 (`+1` de maestria) | 5 pp |
| perícia treinada, nv30 (`+4`) | **20 pp** |

A peça 11 já preça desvantagem em `−25 pp` e a peça 14 preça a camada de permissão em taxa de sucesso. **Bônus em rolagem tem conversão neste projeto.** A frase vale para sentido e comunicação — não para esta.

---

## 3. A variância das três está errada, e o `Coro` colapsa no `Servo`

*Modelo reproduzido dos três desvios publicados no §6.4 antes de qualquer mudança, e depois refeito por Monte Carlo independente de 400 mil rodadas. Os quatro valores batem em duas casas.*

Os desvios do §6.4 tratam toda condicional como `20%`. O próprio §6.4 exige que a do `Coro` dispare em quase toda rodada — *"a invocação atacou"*. Como a régua trava a média em `1,27` por entrega, subir a taxa derruba a magnitude:

| taxa da condicional do nv2 | magnitude | desvio do `Coro` | pico |
|---|---|---|---|
| `20%` — como está publicado | `6,35` | **`3,29`** | `13,59` |
| `50%` | `2,54` | `2,44` | `9,78` |
| `80%` | `1,59` | `2,18` | `8,83` |
| **`90%`** | **`1,41`** | **`2,13`** | **`8,65`** |
| `100%` | `1,27` | `2,09` | `8,51` |

**A ordem das três se inverte:**

| | publicado | com a taxa que o §6.4 exige |
|---|---|---|
| menor variância | `Servo` `2,09` | `Servo` `2,09` |
| meio | `Matilha` `2,95` | **`Coro` `2,13`** |
| maior | `Coro` `3,29` | **`Matilha` `2,95`** |

**`Servo 2,09` contra `Coro 2,13` é 2% de diferença — não é diferença nenhuma.** Os picos também colam: `8,51` contra `8,65`. As três deviam se separar por variância, e duas viram a mesma coisa.

> **E o achado embaixo é estrutural, não de número.** Uma condicional que dispara em quase toda rodada **é uma permanente com passos a mais** — magnitude `1,41` contra `1,27`, desvio `0,42` contra `0`. A trava do §3.6 diz *"o nível 2 é Classe Passiva 1 ou 3, e se for 1 tem de disparar com frequência"*. **Aplicada, ela colapsa as duas opções que oferece.**

*O galho contrário é pior:* manter a magnitude em `6,35` e disparar a `90%` põe a Trilha `+88%` acima do orçamento.

---

## 4. O levantamento do 5e 2024 está errado, e é ele que sustenta o calendário

**Este é o achado que responde à pergunta do Mizuki sobre níveis diferentes por classe — e ele estava certo.**

O CHANGELOG da v0.60 e o §3 do rascunho escrevem:

> *"o 5e de 2014 tinha vãos de 8 entre feitos de subclasse — Paladino `3·7·15·20`, Feiticeiro `1·6·14·18`, Bardo `3·6·14` — que a edição de 2024 tirou todos, padronizando em `3, 6, 10, 14`, com o capstone do Paladino descendo do nível 20 para o 14."*

Conferido no texto das classes de 2024, uma por uma:

| classe, 2024 | níveis de subclasse | quantas | maior vão |
|---|---|---|---|
| Bárbaro | `3 · 6 · 10 · 14` | 4 | 4 |
| Ladino | `3 · 9 · 13 · 17` | 4 | 6 |
| **Paladino** | **`3 · 7 · 15 · 20`** | 4 | **8** |
| **Feiticeiro** | **`3 · 6 · 14 · 18`** | 4 | **8** |
| **Bardo** | **`3 · 6 · 14`** | **3** | **8** |
| **Clérigo** | **`3 · 6 · 17`** | **3** | **11** |

**Uma de seis está em `3·6·10·14`.** O Paladino de 2024 é idêntico ao de 2014 — o capstone não desceu, ele continua no nível 20. O Bardo é idêntico ao de 2014. O Feiticeiro só mudou o `1` para `3`, que é a regra nova de toda subclasse começar no 3.

**Das três classes que o projeto citou nominalmente como exemplo de vão de 8 corrigido, nenhuma foi corrigida.**

E duas classes entregam **três** features de subclasse em vez de quatro. O mecanismo está escrito na revisão do Clérigo: a feature de nível 8 saiu da subclasse **porque o benefício foi para a classe base** (`Blessed Strikes` no 7, `Divine Intervention` no 10).

> **A régua de verdade do 5e 2024 é: o total é da CLASSE. Quando a base entrega mais, a subclasse entrega menos — em quantidade e em nível.**

*Este projeto já pratica metade disso e nunca escreveu:* a peça 6 §3.1 diz que Bastião e Vanguarda ganham ataque extra **pelo Caminho** e `Arremate` e `Coro` **pela Trilha**. É a mesma mecânica. O que falta é o calendário acompanhar.

---

## 5. Por que as outras três peças fecharam e esta não

*Levantado contra o CHANGELOG e contra as próprias peças.*

| peça | tinha exemplar antes da régua? | qual |
|---|---|---|
| **13 — Legados** | **sim** | o catálogo antigo. *"os quatro Legados que a régua reprovou eram do catálogo antigo"* |
| **14 — Equipamento** | **sim** | *"tratando as seis classes publicadas como dados de uma regressão"* — cinco fecham exatas |
| **15 — Invocações** | **sim** | os seis shikigami do material. *"o `Chamariz` é a única entrada que existe porque um shikigami do material não fechava sem ela"* |
| **Trilhas** | **não** | quinze nomes |

Contado no repositório: fora do rascunho e do CHANGELOG, as doze Trilhas que não são do Evocador aparecem **de 0 a 7 vezes**, todas como menção de nome. `Servo`, `Matilha` e `Coro` aparecem 28, 46 e 36 — e são exatamente as três que o §4 mandou atacar primeiro *"porque as três já têm máquina"*.

> **O projeto já sabia que exemplar destrava, e usou isso uma vez sem generalizar.** A recomendação de método que o §4 herdou — *régua antes do catálogo* — é verdadeira e está sendo lida errada. Nas três peças que fecharam, a régua veio antes do catálogo **novo** e depois de exemplares **velhos**. Trilhas é a primeira que tenta fazer régua contra o vazio.

*E o exemplar não precisa ser balanceado. Ele precisa existir para a régua ter contra o que ser conferida — foi assim que o Coelho de Fuga criou uma entrada inteira da peça 15.*

---

## 6. Calendário por Caminho — a recomendação CAIU na segunda passada

*Pedido do Mizuki: "valide 2-3 vezes antes de me mandar, precisa ter certeza, não ser uma suposição". Ele estava certo em desconfiar — eu tinha recomendado por analogia com o 5e, sem rodar a conta.*

> **Primeiro o modelo teve de ser consertado.** A primeira versão dele media o vão só entre entregas de Trilha e devolvia `9` onde a Q2 publica `5`. A métrica certa é: **vão** = distância em níveis entre entregas de Trilha **e** de Caminho; **seca** = maior corrida em missões sem nada que se escolha, contando marcos junto. Refeito, ele reproduz `vão 5 · seca 24` **e os dois calendários de seis que a Q2 reprovou** (`vão 8 · seca 27` e `vão 6 · seca 37`). *Só depois disso a conta abaixo vale.*

**Três razões independentes, e cada uma sozinha já reprova.**

### a) Não melhora nada mensurável

| variação | vão | seca | contra hoje |
|---|---|---|---|
| **hoje** — `2·11·19·27` + `7·15·23·29` | **5** | **24** | — |
| um Caminho com **3** entregas de Trilha | 6 a 8 | 27 | **+1 a +3 de vão, +3 missões** |
| um Caminho com **5** entregas | 5 a 6 | 24 a 27 | **empata no melhor caso**, e custa 5 entradas a mais |

O mecanismo do Clérigo — menos entregas na subclasse — **piora as duas métricas aqui**, sem exceção.

### b) Não existe a assimetria que ele compensaria

No 5e o Clérigo perde a feature do nível 8 **porque a classe base ganhou duas**. Aqui os cinco Caminhos são empatados de propósito: a soma vida+PE é `11 · 10 · 10 · 10 · 10`, e a peça 6 §3 registra que *"a soma quase igual nos cinco é o que faz a troca ser sabor em vez de degrau de poder"*. **O degrau do nível 7 já fecha o que sobrava**, com `0,0 pp` de distância entre os cinco nos níveis publicados.

**Não há Caminho entregando mais na base. O calendário desigual não teria o que compensar — ele criaria a desigualdade em vez de corrigi-la.**

### c) O projeto já testou isso e rejeitou, na v0.61

A peça 6 §3.1, sobre mover o ataque extra do nível 6 para o 7:

> *"com o ataque extra no 6, Bastião e Vanguarda ficavam com **cinco degraus de Caminho** e os outros três com quatro. **Mover fecha as duas coisas de uma vez** — um presente por nível, e **quatro degraus de Caminho para os cinco**."*

**Calendário desigual por Caminho é exatamente o que aquela versão saiu para desfazer**, quatro versões atrás e com conta na mesa.

### E a "melhoria" que a busca achou também é falsa

Amostragem de 1,5 milhão de calendários legais achou um melhor **na seca**: `2·11·20·28` + `7·15·24·29` corta de `24` para `18` missões com o mesmo vão `5`. **Conferido contra o segundo critério da Q2, ele reprova:**

| | hoje | o "melhor" |
|---|---|---|
| entregas caindo em nível que já estava vazio | **8 de 8** | 5 de 8 |
| entregas empilhadas em nível que já entrega | **0** | **3** (20, 24, 28) |
| níveis que continuam sem nada | **2** (3 e 25) | **5** |

**O calendário de hoje é ótimo no critério que a Q2 declarou** — *"a Trilha tem onde cair sem competir com nada"* —, e ele acerta as oito. A busca otimizou uma métrica e quebrou a outra.

> **Veredito: o calendário não se mexe.** Nem por Caminho, nem deslocado. **O item errado do levantamento do 5e continua tendo de ser corrigido** — ele só nunca sustentou o calendário, que fechou por vão e por seca medidos, e esses estão certos.

### Mas o que o Mizuki sentiu existe, e tem outro nome

A intuição — *"as quinze sobem igual e por isso parecem iguais"* — está certa sobre o sintoma. O eixo é **formato**, não calendário, e a v0.65 já o libertou: *"com Trilha fechada, o formato passa a ser justamente o que faz uma Trilha parecer diferente da outra"*. É lá que a diferença mora, e é lá que a variância errada do §6.4 está atrapalhando.

---

## O que fica de pé da Q3, e é a maior parte

- **O calendário da Q2** (`2·11·19·27` e `7·15·23·29`) — a conta dele não depende de nada disto.
- **A Trilha fechada e a troca total da Q4.**
- **A fatia como unidade de conta**, `1,27` ponto de dano por rodada, e o fato de ela ser plana.
- **A escada de Classe Passiva como medida de FORMA** — ela mede o quê e não o quanto, e continua certa.
- **O degrau do nível 7**, e o empate dos cinco Caminhos em `+6%`.
- **As três travas da matriz** — `Matilha` sem ação nem orçamento, `Servo` sem ação, `Coro` sem corpo a corpo.
- **Duração fora do permitido**, com o número (`11` a `43` fatias) registrado.
- **A metade do §3.4-B que é o preço morar na Trilha.** Essa continua certa; o que não fecha é a segunda metade.

## O que não fica

- **A taxa livre por entrada**, do jeito que está.
- **A entrega de utilidade sem preço**, do jeito que está.
- **Os três desvios do §6.4**, e o formato `1 · 2 · 3 · 3` do `Coro` que saiu deles.
- **O item do levantamento sobre o 5e 2024**, no CHANGELOG da v0.60 e no §3 do rascunho.
- **A frase do §3.4-B sobre não existir conversão para utilidade**, que é falsa para bônus em rolagem.

*E o calendário fica — a seção 6 é a recomendação que eu mesmo derrubei.*

---

## 7. Quem escreve as quinze, e por que a minha objeção tinha saída

Minha objeção era: *se eu escrevo conhecendo a régua, o exemplar nasce contaminado e não serve de teste independente.* **Ela vale contra escrever a partir da régua. Não vale contra escrever a partir do material.**

As três peças que fecharam usaram exemplar **externo ao projeto**:

| peça | de onde veio o exemplar |
|---|---|
| 14 — Equipamento | as seis classes de arma **publicadas em outro sistema** |
| 15 — Invocações | os **shikigami do material do JJK** |
| 13 — Legados | o catálogo antigo, escrito **antes** da régua existir |

**As quinze Trilhas têm material.** Escrever cada uma como *"o que essa pessoa faz nas páginas"* — e só depois medir — é o mesmo método, e o exemplar continua sendo independente da régua porque não foi a régua que o produziu. *Foi assim que o Coelho de Fuga criou uma entrada inteira da peça 15: o exemplar não coube, e quem cedeu foi a régua.*

> **Então eu consigo, com uma condição: escrevo em ficção, a partir do material, sem olhar o orçamento.** Você revisa a ficção — que é a parte que é sua — e só depois eu preço. Se uma Trilha não couber, o achado é da régua e não da Trilha.

**E se você preferir escrever, os níveis são estes** *(não mudaram, e a seção 6 é a validação de que não mudam)*:

> **Cada Trilha entrega quatro coisas: nos níveis `2`, `11`, `19` e `27`.**
> **Cada Caminho entrega quatro coisas: nos níveis `7`, `15`, `23` e `29`** — iguais para as três Trilhas daquele Caminho.
>
> **O nível 2 é sempre permanente ou condicional-que-dispara-muito**, nunca uso limitado.
> **Pelo menos uma das quatro tem de ter botão** — algo que o jogador decide usar.
> **A do nível 7 é maior que as outras**: quem já tem ataque extra (Bastião, Vanguarda, `Arremate`, `Coro`) recebe o ataque extra ali; quem não tem recebe um degrau grande no lugar.

---

*Escrito na v0.69, com a base verde e os números rodados duas vezes — analítico e Monte Carlo para a variância, busca sobre as oito famílias para a régua, e fonte primária classe a classe para o 5e 2024.*
