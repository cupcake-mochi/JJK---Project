# CAMINHOS E TRILHAS

**Fase 4, sexta peça.** O quadro de Caminhos, as Trilhas, e o que cada um pode conceder sem quebrar a economia do Fundamento.
Versão v0.14, corrigida na v0.15, na v0.16 e na v0.24 — 08/08/2026

Esta peça revisa e substitui a seção 4 da peça anterior.

---

## 1. Os cinco Caminhos

Nomes conferidos contra o manual — nenhum é termo definido lá. *Linha de Frente*, *Ponta de Lança*, *Retaguarda* e *Leitura* eram rótulos de rascunho; **Leitura** em particular já aparecia três vezes no Fundamento e precisava sair.

| Caminho | O que ele é | Atributos naturais |
|---|---|---|
| **Bastião** | o corpo como resposta: aguentar, encarar, prender | Força, Constituição |
| **Vanguarda** | a arma como resposta: alcançar, cortar, acabar | Destreza, Força |
| **Guia** | o outro como resposta: estender, recuperar, reposicionar | Essência |
| **Emanador** | a técnica como resposta: mais feitiço, mais aptidão | Inteligência, Essência |
| **Evocador** | o que você trouxe como resposta: invocações | Inteligência, Essência |

### Uma colisão que a checagem pegou

*Canalizador* era a escolha para o Caminho de técnica e **não passa** — não pelo manual, onde a palavra está livre, mas pelo próprio material do projeto.

**Canalizar Energia é a aptidão do lutador físico**, e ela descreve o que o **Bastião** e a **Vanguarda** fazem. Nomear o Caminho de técnica de Canalizador colocaria a palavra apontando para os dois lados ao mesmo tempo.

Renomear a aptidão sairia mais caro: *canalizar energia* é termo da própria obra e já estava na lista de aptidões. Então quem muda é o nome do Caminho. **Emanador** está livre no manual e em todo o material do projeto, e a distinção fica limpa: **canalizar** é empurrar energia por dentro do corpo e da arma; **emanar** é soltar energia para fora. Um é o Bastião e a Vanguarda; o outro é o Emanador.

> **Este bloco falava de "golpe canalizado" como *a mecânica central* do físico, e essa mecânica NÃO EXISTE — v0.81.** *O termo tem **zero** ocorrências no manual, junto com `canalizado`, `canaliza` e `Canalizar`.* **Ele era abreviação de *feitiço de Forma Toque*, e a palavra "golpe" fez um feitiço parecer um ataque** — que é o que confundiu a economia de ação do projeto inteiro.
>
> **A aptidão `canalizar energia` fica**, porque ela é da obra e a peça 11 a lista entre as doze que o material obriga. **O que morreu é o substantivo `golpe canalizado`.** *Trocado por `feitiço de Toque` em 39 lugares, em 11 arquivos, sem mexer em número nenhum.*

**Sem multiclasse.** Um Caminho por personagem, e dentro dele **Trilhas**.

**A primeira Trilha vem na criação, junto do Caminho.** *Decidido na v0.27, aplicado na v0.34.* Ela é identidade, não recompensa — o Caminho diz o seu lugar na equipe e a Trilha diz quem você é dentro dele, e as duas coisas nascem com o personagem. Esta seção dizia que *"as escolhas de nível compram Trilhas"*, e isso vinha de contar a partir do nível 1 numa ficha que nasce no 2: é o mesmo engano que a v0.28 achou na contagem de feitiços.

> **Esta linha dizia que "as Trilhas seguintes se acumulam com o nível", e isso morreu em duas etapas.** *Na v0.55:* **uma Trilha por ficha, e ponto** — não existe acumular. *Na v0.65:* **a Trilha é fechada** — as quatro entregas dela são todas dela, sem pegar emprestado das vizinhas.
>
> **O que existe no lugar é TROCA.** Nos níveis **11, 19 e 27** você pode trocar a sua Trilha por outra do mesmo Caminho, e **a troca é total**: tudo o que você tinha vira o equivalente da Trilha nova. Você é sempre exatamente uma Trilha, do nível 2 ao 30.
>
> *O motivo está no `RASCUNHO-trilhas.md` §3, e ele é curto: **ou cada entrada carrega pré-requisito escrito, como o Pathfinder 2e faz, ou a trilha é fechada, como o D&D 5e faz.** O meio-termo deixava você pegar o degrau avançado de uma Trilha sem nunca ter tido a base dela.*

## 2. As Trilhas

Três por Caminho. **Os nomes foram fechados na v0.24**, quando o `conferir-nomes.py` passou os quinze pela checagem nas duas direções e reprovou seis.

### Bastião

| Trilha | O que faz |
|---|---|
| **Muro** | tanque puro. O corpo é o escudo: absorve, redireciona, não sai do lugar |
| **Punho** | meio tanque, meio dano. Vários golpes médios, uma pitada de controle |
| **Brasa** | meio tanque, meio feitiço. Conjura pequeno e bate na sequência |

### Vanguarda

| Trilha | O que faz |
|---|---|
| **Estocada** | versátil com um pé em feitiço. O molde do Yuta |
| **Batedor** | distância: arco, arma de fogo, o que atinge longe |
| **Executor** | arma e corpo, sem meio-termo. É o guerreiro puro do quadro |

As três respondem a mesma pergunta — *como você alcança o inimigo* — de jeitos que não se sobrepõem: a Estocada com um pé em feitiço, o Batedor sem encostar, o Executor só encostando.

### Guia

| Trilha | O que faz |
|---|---|
| **Elo** | estende o que outro fez: duração, alcance, quantos alvos |
| **Sutura** | recuperação — PE, condição, Integridade. É aqui que Energia Reversa chega cedo |
| **Perímetro** | controla o campo: reposiciona aliado e inimigo, nega movimento |

O Guia era o que você não sabia preencher, e o motivo é bom: **buff e debuff moram na técnica, e cura é Forma de feitiço.** Sobra pouco se o Caminho tentar competir nesses eixos. A saída é ele não competir — ele **alcança**. Não cria o efeito; faz o efeito de outra pessoa durar mais, pegar mais gente ou chegar mais longe. E a Sutura resolve o caso concreto que você levantou: liberar a aptidão de Energia Reversa antes do refino permitir.

**O Guia é o único Caminho sem rota para ataque extra** (seção 3), e isso é decisão da v0.24: quem quiser lutar de Guia paga pela técnica, no orçamento do Fundamento, como todo mundo. O que as três Trilhas dele entregam em troca de um golpe por rodada é a pergunta que a peça de Trilhas precisa responder com número.

### Emanador

| Trilha | O que faz |
|---|---|
| **Torrente** | mais de um feitiço acima de Classe 0 por rodada, a um custo |
| **Explosivo** | um feitiço só na rodada, e ele sai maior |
| **Arremate** | conjurador de perto: feitiço e golpe na mesma troca |

### Evocador

| Trilha | O que faz |
|---|---|
| **Servo** | uma invocação, forte. O molde do Megumi com o Mahoraga |
| **Matilha** | muitas invocações fracas. O molde do Geto |
| **Coro** | lutar junto delas: o seu golpe e o delas se encadeiam |

---

## 3. Ataque extra: passa, com uma correção

Você pediu que os Caminhos físicos ganhem ataque extra e os meio-arcanos não. **A conta aprova**, e por um motivo que vale registrar. *Quem ganha, e em que nível, está na seção 3.1 — isso ficou sem ser escrito da v0.14 até a v0.24.*

A coluna Rotina do Fundamento é **o meio exato entre bater num alvo e espalhar o dano**. As duas colunas vizinhas dela, na mesma tabela do manual, são `3 × Classe` e `4 × Classe` em dados; a Rotina é `floor(3,5 × Classe)`. Ela fecha nas **sete** Classes sem nenhum parâmetro livre, e a checagem 4e do `conferir-manual.py` reconstrói ela em vez de guardar o número.

> **Esta seção dizia outra coisa da v0.14 até a v0.79, e a frase errada custou cinquenta e uma versões: *"a coluna Rotina já é feitiço + Classe 0"*.**
>
> Ela nunca foi. A leitura velha dá um número **diferente da Rotina nas sete Classes** — no Classe 7 ela pede `27d8` e a Rotina é `24d8`. E o estrago não ficou na explicação: foi ela que fez esta tabela somar um Classe 0 de `4,50` na linha do conjurador, **e `4,50` não existe em lugar nenhum do manual.**
>
> *O manual tem tabela própria para o dano de um Classe 0 — `2d8 · 3d8 · 4d8 · 5d8 · 6d8`, por faixa de nível —, e até a v0.79 nenhum documento do projeto e nenhum validador abriam ela. **Ela é a quarta tabela compartilhada com o manual, e era a única sem dono declarado.** Hoje o dono é o manual, como o da Rotina.*

**E um Classe 0 não cabe junto do feitiço grande.** Todo feitiço custa Ação Padrão. A única Melhoria que tira ele de lá é a `Rápido`, e ela custa o degrau **Pesada** — e o manual escreve que numa Classe 0 **só cabe Melhoria do degrau `Leve`**. Pôr `Rápido` no feitiço grande para os dois caberem no mesmo turno piora a rodada em todo nível do 10 em diante: no 30 ela sai de `94` para `72`. Ninguém faz.

**Então a linha do conjurador é o feitiço sozinho, e o ataque extra do físico não é o espelho de nada — ele é o que separa os dois.**

| nível | Rotina | conjurador (o feitiço sozinho) | físico (feitiço de Toque + golpe simples) |
|---|---|---|---|
| 2 | 13 | 13 | 22 |
| 10 | 45 | 40 | 50 |
| 18 | 76 | 67 | 78 |
| 30 | 108 | 94 | 106 |

**O vão entre as duas linhas é exatamente um golpe simples — `9 · 10 · 11 · 12`.** Não é coincidência nem calibragem: o físico *é* o conjurador mais um golpe, e nunca foi outra coisa. *A tabela publicava `4 · 5 · 6 · 7`, que é o golpe simples menos o Classe 0 fantasma, em todo nível.*

**A correção:** o feitiço de Toque **não soma arma nem Força**. Ele *é* o feitiço; arma e Força são o que você faz quando **não** canaliza. Se o feitiço de Toque somasse os dois e ainda houvesse ataque extra:

| nível | Rotina | feitiço de Toque + arma + Força, dois golpes | quanto passa |
|---|---|---|---|
| 2 | 13 | 30 | **+135%** |
| 10 | 45 | 60 | **+32%** |
| 18 | 76 | 88 | +16% |

Então a regra fica em três linhas, e ela espelha a regra de ouro nº 6 do Fundamento:

> **Feitiço de Toque** = os dados da Classe, e nada mais. É o feitiço.
> **Golpe simples** = arma + Força. É o Classe 0 físico.
> **Um feitiço de Toque por turno.** Ataque extra é sempre golpe simples.

## 3.1 Quem ganha ataque extra, e em que nível

*Escrito na v0.24.* Da v0.14 até aqui, o ataque extra tinha conta, argumento e correção — e **nunca tinha dono**. O único texto era "os Caminhos físicos ganham e os meio-arcanos não", que é a mesma divisão em duas famílias que a seção 5 desta peça registra como tendo deixado o Guia sem número de PE. Ela não cobre os cinco Caminhos, e o achado da v0.20 sobre o Guia dependia inteiro de como ela fosse resolvida.

> **Bastião e Vanguarda ganham ataque extra no nível 7**, pelo Caminho.
> **Arremate e Coro ganham pela Trilha**, quando o personagem a compra.
> **O Guia não ganha por nenhuma rota.**

> **Era o nível 6 até a v0.61, e o motivo escrito aqui era *"é o primeiro marco, e é onde o resto do sistema já entrega coisa"*. Esse motivo virou o argumento contrário.** A Q2 de Trilhas mediu o calendário do sistema inteiro e achou que o **nível 6 é um dos quatro mais cheios** — marco, feitiço e o ataque extra no mesmo lugar —, enquanto o **7 não entrega absolutamente nada**. E ela pôs os degraus de Caminho em **7 · 15 · 23 · 29**: com o ataque extra no 6, Bastião e Vanguarda ficavam com cinco degraus de Caminho e os outros três com quatro. **Mover fecha as duas coisas de uma vez** — um presente por nível, e quatro degraus de Caminho para os cinco.
>
> *O calendário que aquela Q2 escreveu foi **superado na v0.70**, quando o desenho dos cinco Caminhos o moveu para `2 · 7 · 15 · 30`. O que sobreviveu dela é o nível 7, que continua sendo degrau; o dono do calendário de hoje é o `DESENHO-caminhos.md`.*

**O ataque extra é o degrau de Caminho do nível 7 desses dois, e não um degrau a mais.** Quem não tem rota para ele — o Guia, e as Trilhas do Emanador e do Evocador que não são `Arremate` e `Coro` — recebe no lugar um degrau que vale exatamente o vão desta seção. *A régua está no `RASCUNHO-trilhas.md` §3.4.*

> **E "vale o vão" precisou de definição na v0.80, porque o degrau do Emanador não é um número somado toda rodada.** O `Resquício` só dispara quando a Ação Padrão foi um feitiço que não causa dano — então ele **levanta o chão da rodada de controle** em vez de subir o pico.
>
> **A leitura que vale é a MÉDIA por rodada, e não o pico.** Um degrau que dispara em parte das rodadas empata com o ataque extra quando `magnitude × taxa` dá o vão; ele não precisa empatar na rodada mais forte. *Escolha do Mizuki, e ela tem preço declarado: o Emanador termina `12` de dano por rodada atrás do físico na melhor rodada dele, e o que ele compra com isso é controlar sem perder o turno.*
>
> **A taxa é número de playtest.** Nenhuma medição existe de quantas rodadas um Emanador passa em controle, e ela decide o degrau inteiro.

**Num Caminho de técnica, o ataque extra chega na Ação Bônus, e ele é o degrau do vão.** O `Arremate` e o `Coro` põem um golpe simples ao lado do feitiço — `feitiço + golpe`, que é a mesma linha do físico. **A partir daí eles podem comprar um segundo golpe pela Trilha, e isso é permissão da v0.80.**

> **Esta seção proibia por nome até a v0.79: *"eles não passam a ter três ataques"*.** *E ela proibia com uma tabela que não reconstrói de nada — a coluna "somar o golpe" publicava `21 · 55 · 90 · 127`, e nenhuma combinação das peças publicadas produz esses quatro números.* **A proibição caiu junto com a linha de base do Classe 0**, porque ela era escrita como *"trocar o Classe 0 pelo golpe simples"* e não existe Classe 0 nenhum naquela rodada para trocar.

**A permissão, e o preço dela medido:**

> **O `Arremate` e o `Coro` podem ter três rolagens de ataque numa rodada** — dois golpes na Ação Padrão e o feitiço na Ação Bônus, ou o arranjo espelho. **A trava que continua valendo é a regra de ouro nº 6 do Fundamento e a da seção 3 acima: um feitiço de Toque por turno, e ataque extra é sempre golpe simples.**

*Decisão do Mizuki: **"o Emanador já tem pouca vida, ele ter dano é o mínimo."*** **E o motivo tem número:** com Constituição 3 no nível 30 o Emanador chega a `212` de vida, contra `243` da Vanguarda e `305` do Bastião — **87% e 70%.**

**O que a permissão custa, medido nível a nível, e não só no 30:**

| nv | Rotina | físico | `Arremate` com dois golpes | acima do físico |
|---|---|---|---|---|
| 11 | 45 | 50 | 60 | **+20%** |
| 18 | 76 | 78 | 89 | +14% |
| 22 | 94 | 92 | 104 | +12% |
| 30 | 108 | 106 | 118 | **+11%** |

> **⚠ O pior nível não é o 30, e é onde a conta anterior olhou.** O `DESENHO-trilhas.md` mediu `+10%` no nível 30 e fechou o argumento ali — **o nível 30 é o mais favorável dos quatro.** No nível 11, que é onde o ataque extra da Trilha chega, ele está em `+20%`.
>
> **A causa é de escala e não da Trilha:** o feitiço cresce de `13` para `94` na campanha e o golpe simples cresce de `9` para `12`. **Um golpe a mais é 22% da Rotina no nível 11 e 11% no nível 30** — ele encolhe sozinho.
>
> **Fica declarado e não consertado.** *O conserto barato, se o playtest reclamar, é mover o ataque extra do `Arremate` do nível 11 para o 19: o pior caso cai de `+20%` para `+14%` e a curva fica quase plana.*

> **A tabela que ficava aqui morreu na v0.80, e as duas notas presas nela também. Elas ficam registradas, porque as duas ensinam.**
>
> **A da v0.60:** a coluna Rotina desta peça vinha lendo `81` e `126`, que não são a coluna `Rotina` do manual — são `Feitiço num alvo` da Classe 6 e `Somando alvos` da Classe 7. *Número que veio da coluna errada da tabela certa passa por qualquer varredura que só pergunte se ele existe no manual.* **Hoje a checagem 4d do `conferir-manual.py` pega exatamente isso.**
>
> **A da v0.72:** o `+18%` daquela tabela **não era um teto de dano**, e foi lido como um. Ele era a medida de uma montagem específica, e o que a seção recusava era o **mecanismo**. *Piso lido como teto é o erro mais caro desta peça, e ele aconteceu duas vezes.*
>
> **E a v0.80 achou o terceiro andar do mesmo defeito: aqueles `+18%` nunca reconstruíram de nada.** O `127` do nível 30 aparecia **uma vez só no repositório inteiro**, sem script e sem validador. *Um teto que ninguém consegue recalcular não é teto — é número que sobreviveu por repetição.*

Com um golpe na Ação Bônus, o conjurador de perto cai exatamente na linha do físico, que esta seção já aprovou. **Com dois, ele passa dela — e a seção 4, logo abaixo, continua valendo para invocação: ação a mais por rodada não tem conserto por preço.** *A diferença entre os dois casos é que a invocação multiplica corpos e a Trilha compra um golpe dentro de uma ficha só, pagando por ele em fatia.*

**E o argumento que aprova o ataque extra é que ninguém está acima da régua.** O conjurador para em `94` e o físico em `106`, contra uma Rotina de `108`. O ataque extra **fecha o vão do físico até a régua** em vez de passar dela — e é por isso que ele é correção de base e não bônus.

> **Este argumento mudou na v0.80, junto com a linha de base da seção 3.** O que estava escrito aqui era *"o único argumento que aprova o ataque extra é que a Rotina já é feitiço + Classe 0"*, e aquela frase é falsa — a seção acima registra por quê. **A decisão sobrevive e o argumento ficou mais forte:** antes ela dependia de um espelho que não existia; agora ela depende de os dois estarem abaixo da régua, que é conta lida do manual.

**O Coro não custa nada a mais**, e isso cai de graça da regra da seção 4: o dono e todas as invocações somados entregam **uma** Rotina. É teto de saída, não de número de ações. Os golpes do dono e o da invocação continuam saindo do mesmo orçamento — as ações se redistribuem, o dano não sobe. A exceção de economia de ação que estava em aberto no Coro já estava paga.

> **E é por isso que a permissão da v0.80 chega no `Coro` de graça, e ela chega diferente.** *Decisão do Mizuki: o `Coro` herda.* **No `Arremate` a permissão custa `+11%` a `+20%` sobre o físico, porque cada golpe novo é dano novo. No `Coro` ela custa `0%` em dano**, porque o teto de uma Rotina somada já segura a saída — o que ela compra é **uma rolagem a mais**, e rolagem a mais é alcance, tipo de dano e alvo, que o teto não mede.
>
> **É a lição do eixo errado outra vez, e ela fica declarada em vez de consertada:** o teto da seção 4 só enxerga dano. *Quando as três Trilhas do Evocador forem preçadas, o que precisa de conta é a rolagem a mais e não o dano dela.*

**E o Guia fica coerente ficando de fora.** Ele é o único Caminho que não oferece um segundo golpe; quem quiser lutar de Guia paga pela técnica, no orçamento do Fundamento, como todo mundo. Isso troca o achado nº 2 da v0.20 — *"o Guia pode estar dominado pela Vanguarda"* — por uma pergunta fechada e mensurável: **o que Elo, Sutura e Perímetro entregam que valha um golpe por rodada?** A peça de Trilhas responde com número.

### Em que slot o golpe cai, e o gate que paga por ele — v0.66

*Decisão do Mizuki, e ela fecha um vão que estava aqui desde a v0.24:* **esta seção sempre disse *"2 ações"* e nunca disse quais.**

> **O golpe simples do `Arremate` e do `Coro` é uma Ação Bônus, e ele só existe se a Ação Padrão daquele turno foi gasta no que a Trilha é.**
> **`Coro`** — a padrão comandou, e a invocação atacou.
> **`Arremate`** — a padrão conjurou **ou atacou com a arma do grupo escolhido**.

> **A metade em negrito entrou na v0.80, e ela é a Trilha invertida.** *Decisão do Mizuki na v0.79: o `Arremate` bate na Padrão e conjura na Bônus, em vez do contrário.* **O gate sobrevive inteiro e só troca de sentido** — a Ação Padrão continua fazendo uma coisa só, e a escolha continua sendo por rodada. *O que ela não pode é ficar livre: uma Padrão solta faz a Trilha conjurar, golpear e ainda ter a Bônus.*

**O gate é a metade que importa, e sem ele a mudança vazava.** Mover o golpe para a Ação Bônus solta a Ação Padrão do `Coro`, e um `Coro` de padrão livre conjura, golpeia e comanda no mesmo turno. *O teto de uma Rotina da seção 4 continuaria segurando o **dano** e não seguraria o resto* — feitiço faz controle, alcance e condição, e o teto não mede nada disso. **É a lição do eixo errado: o teto só enxerga o eixo que ele tem.** Com o gate, a padrão só faz uma coisa, e a escolha volta a ser por rodada: **ou você conjura, ou você comanda e golpeia.**

**O que sai por rodada não muda** — feitiço mais golpe, como já era, e a tabela acima continua valendo. **O que muda é que o golpe passa a custar um slot que ele não custava**, porque ele morava no lugar do Classe 0 e o Classe 0 é grátis.

**E é aí que está o ganho, porque esse preço cresce sozinho.** A peça 14 §4 mediu os slots do turno e achou que **a Ação Bônus não cobra nada hoje**: no quadro dela, *passivo* e *ação bônus* empatam em `2,01`, e ela chama o slot de *"o mais vazio do turno"*. Aquela mesma seção escreve o conserto que ela não podia aplicar sozinha — *"um preço que cresce sozinho conforme o sistema enche o slot, que é o formato que a lição nº 1 pede"*. **Esta regra é a primeira coisa a encher o slot**, e o Bastião socando como Ação Bônus é a segunda.

> **Esta regra não tem validador dono, e isso é dívida.** Nenhum `conferir-*.py` lê a forma do ataque extra: o `conferir-manual.py` confere a coluna Rotina contra a qual ele foi aprovado, e o `conferir-orcamento.py` o cita numa linha de saída. **Nenhum dos dois falha se alguém trocar o slot ou apagar o gate.** Fica anotado como checagem que falta, junto da que conta skill.

### Canalizar e atacar são ações diferentes — v0.81

> **E ao escrever esta seção apareceu que a pergunta era outra: `golpe canalizado` NÃO EXISTE.** *Zero ocorrências no manual.* **A linha do físico desta peça estava escrita em cima do termo, e ele foi trocado por `feitiço de Toque` em 39 lugares sem mexer em número nenhum.** *A história completa está no topo do §3 da **peça 5**.* **A pergunta que sobrou — de que ação vem o golpe da linha do físico — fechou na v0.82, no bloco no fim desta seção.**

*A v0.80 registrou este buraco como **o mais caro que ela deixou aberto**: esta peça publica a rodada do físico como `feitiço de Toque + golpe simples` e **nunca disse em que ação isso acontece**. Ele decidia a `Brasa` por um fator de `2,6×`.*

> **Decisão do Mizuki: a Ação de Atacar NÃO inclui o feitiço de Toque.** *"Não tem como bater junto de um feitiço."* **Os dois não cabem no mesmo turno.**

| o turno, no nível 30 | dano | existe? |
|---|---|---|
| feitiço de Toque `94` + golpe simples `11,5` | 105,5 | **sim** — é a linha do físico da seção 3 |
| 2 golpes simples pela Ação de Atacar | 23 | **sim** |
| feitiço de Toque + golpe simples **+ feitiço na Ação Bônus** | 132,5 | **não** |

**A única exceção é a `Fornalha`, no nível 27 da `Brasa`** — e é justamente por ser exceção que ela é um degrau de nível 27.

> **O que isso destrava:** toda entrega de Trilha que se pendura em *"se você usou a ação de atacar"* **não dispara na rodada em que o personagem canaliza.** *É o que faz o nível 2 da `Brasa` ser preçado por taxa em vez de somado no pico.*
>
> ## O ataque extra EXIGE a Ação de Atacar — invertido na v0.147
>
> > **Você ganha um golpe simples por rodada. Ele exige a Ação de Atacar: acontece junto do que a sua Ação Padrão fez naquele turno, e só nesse caso — a não ser que uma habilidade diga o contrário.**
>
> ***Decisão do Mizuki na v0.147, e ela reverte a da v0.82.*** *O motivo é uma entrega publicada que valia zero:* **o `Bote`, nível 19 da `Estocada`, compra "usar o ataque extra na Ação Bônus quando o feitiço da Padrão for de condição" por `2,46` fatias.** *Com o golpe solto, aquilo já acontecia sozinho.* **Uma entrega preçada que não entrega nada é pior do que uma dominância declarada, e as duas estavam medidas.**
>
> **A cláusula final é a válvula, e ela é o que faz a forma nova funcionar:** *"a não ser que uma habilidade diga o contrário"*. **É por ela que o `Bote` volta a valer, e é onde qualquer Trilha futura compra a exceção em vez de recebê-la de graça.**
>
> ### ✔ O que esta inversão deixou aberto FECHOU na v0.155
>
> **O vão `físico − conjurador` do §3 foi construído sobre a forma antiga**, e é ele que pagava o degrau de nível 7 dos cinco Caminhos. *A tabela do fim desta seção é da v0.82 e fica como o que era verdade sob aquela forma — ela não descreve mais a regra.*
>
> ***O achado da v0.155: o vão parou de ser um número.*** *Na forma da v0.82 os dois faziam a mesma Ação Padrão e o físico tinha uma coisa a mais — subtração limpa. Na forma de hoje o físico **escolhe** entre atacar e conjurar, então `físico − conjurador` virou comparação entre duas decisões* — **e o resultado muda com o poço de PE do Caminho e com o que a ficha empilhou na arma.**
>
> | | vale | por quê |
> |---|---|---|
> | ataque extra, ficha nua | `0,53` | só arma, Força e crítico |
> | ataque extra, refino `8` + Manha | `0,92` | o `2º` golpe dobra a Manha e o dano na arma |
> | ataque extra, refino `10` + Manha | `1,95` | `4d6` de dano na arma em cada golpe |
>
> **A dispersão é `3,7×` dentro do mesmo Caminho, e ela não é da v0.147:** *o golpe sempre carregou o que estava empilhado nele.* **O que a v0.147 fez foi tirar o golpe da rodada de feitiço — e com isso encolher o degrau e INVERTER a forma dele**, que publicado crescia com o nível e derivado encolhe.
>
> > **⚠ A última linha era `1,68` e `3d6` até a v0.158, e a dispersão era `3,2×`.** *O que a moveu foi o refino `10` passar a dar um dado a mais — peça 11 §6.9, que é a dona do dano na arma desde aquela versão.* **O número anda por razão e não por reconta:** *o ataque extra é um golpe, e um golpe vale `golpe + dados extras`, então `(11,50 + 14,00) ÷ (11,50 + 10,50)` = `1,159`, e `1,68 × 1,159` dá `1,95`.*
> >
> > **As duas primeiras linhas NÃO se movem, e é isso que salva a tabela do degrau abaixo:** *o refino `8` não mudou, e é nele que o `1,93` do Bastião e o `2,10` da Vanguarda foram medidos.* **A dispersão daqui mede a entrega ao longo da campanha, contra uma ficha nua que só existe do nível 2 ao 9** — *a dominância entre duas fichas do MESMO nível 30 é `1,55×`, e ela está na peça 11 §6.9.*
>
> #### A taxa, e ela é derivada e não perguntada
>
> **O bloco 1 do `conferir-orcamento.py` já publicava o que faltava:** *`3` lutas × `3,5` rodadas = `10,5` rodadas de luta por dia, e o poço de PE diz quantas cabem.* **Bastião conjura `48%` das rodadas no nível 30, Vanguarda `67%`, Emanador `76%`** — e o resto, nas palavras do próprio validador, *"vai para Classe 0, golpe simples e projetar energia, que não custam PE"*. **É nessas que o ataque extra vive.**
>
> #### ***Decisão do Mizuki: o nível 7 ganha uma segunda metade, e ela não anda no ataque***
>
> **A compensação não pode ser dano.** *Qualquer coisa que ande junto do ataque herda a dispersão de `3,2×` e o problema volta.* **Ela tem de ser numa moeda que não sobe no ataque, e aí vale igual para toda montagem.**
>
> | | nível 7 | ataque extra | + a metade nova | total |
> |---|---|---|---|---|
> | **Bastião** | ataque extra + `Ainda de Pé` | `0,83` | `1,10` | **`1,93`** |
> | **Vanguarda** | ataque extra + `Não Pega` | `0,92` | `1,18` | **`2,10`** |
> | Guia · Emanador · Evocador | o degrau grande | — | — | `2,36` |
>
> **A `Ainda de Pé` é `1d8 + metade do nível` de cura, `1×` por cena, sem custo de ação.** *`1` de cura = `1` de dano evitado, pela régua da v0.76.* **O relógio não foi escolhido: `1×` por cena dá `1,10` e `2×` daria `2,19`, que estoura.**
>
> **A `Não Pega` é o `Evasion` do 5e** — sucesso anula, falha vira metade — **como Reação, e desligada pelo `Incapacitado`.** *Um efeito de TR-para-metade custa `16,20` esperados; ela derruba para `4,20`, evitando `12,00`.* ***Taxa declarada: `50%` das rodadas trazem um efeito qualificado*** — no molde da taxa do `Batedor` parado, escrita e não suposta.
>
> > **⚠ E o custo de ação foi escolhido por medida, não por sabor.** *A Reação do Bastião está tomada pelos três outros degraus dele, e a Ação Bônus está tomada pelas três Trilhas — a `Fagulha` põe um `Classe 0` de `27` ali toda rodada.* **Curar `19,5` gastando aquilo dá saldo `−7,5`, e a entrada viraria letra morta para `Punho` e `Brasa`.** *Por isso a `Ainda de Pé` não custa ação: é o único slot livre que o Bastião tem no nível 7.*
>
> #### A diferença que fica, e ela é declarada
>
> **Bastião `−0,43` e Vanguarda `−0,26` contra o degrau grande de `2,36`.** *Os dois ficam abaixo, e a distância entre eles é `0,18` — menor que qualquer Manha do catálogo.* **O resíduo é a Manha:** *a Vanguarda dobra uma no segundo golpe e o Bastião não tem nenhuma; em troca o Bastião passa `52%` das rodadas sem PE contra `33%` dela, e o ataque extra rende mais nele.* **As duas forças quase se cancelam.**
>
> ***Decisão do Mizuki: a diferença fica declarada em vez de o degrau grande descer para `2,05`.*** *`0,30` fatia é `6%` de uma Trilha, e cabe no que o projeto já aceita — a `Brasa` estoura entre `41%` e `88%` e ficou.*
>
> ### A leitura da v0.82, que a inversão aposentou
>
>
> | a rodada, no nível 30 | conjurador | físico | a diferença |
> |---|---|---|---|
> | gastando PE — o feitiço grande | `94,0` | `105,5` | **`11,5`** |
> | poupando PE — um Classe 0 | `27,0` | `38,5` | **`11,5`** |
>
> **A diferença é a mesma nas duas, e ela é exatamente um golpe simples** — que é o que a tabela do §3 publica como o vão, `9 · 10 · 11 · 12` por faixa de nível. *A conta reproduz uma coisa que não foi posta nela.*
>
> **E o custo da forma nova está medido, desde a v0.82:** com o ataque extra preso à Ação de Atacar, dois golpes rendem `23` e o Classe 0 que toda ficha tem de graça rende `27`. **A Ação de Atacar fica dominada pelo botão grátis.** *Aquela versão usou isso para recusar a forma; esta versão a escolhe sabendo o preço.*
>
> ***A decisão de pagar esse preço é do Mizuki, e o que ela compra é o `Bote` deixar de ser letra morta.***
>
> **E a v0.81 registrou no CHANGELOG a frase contrária** — *"o ataque extra sempre exige a Ação de Atacar, como no 5e"*. *Ela contradizia a tabela dos três turnos acima, que já marcava a linha do físico como existente. **Esta seção é a dona; o CHANGELOG registra o que se pensou naquele dia.***

## 4. Invocação: não passa como está

Este é o risco maior do pacote inteiro, e ele não tem conserto por preço.

| nível | Rotina do dono | + 1 invocação que age | + 3 (horda) |
|---|---|---|---|
| 10 | 45 | 90 | 180 |
| 20 | 76 | 152 | 304 |
| 30 | 108 | 216 | **432** |

**Uma invocação que age sozinha dobra o dano por rodada. Uma horda de três quadruplica.** Nenhum preço em PE conserta isso, porque o problema não é recurso — é **economia de ação**. Mais corpos agindo por rodada é a coisa que quebra todo sistema d20, sem exceção.

### O conserto: a invocação divide o seu orçamento

> **Você e todas as suas invocações somados entregam uma Rotina.**
> Com uma invocação, cada um entrega metade. Com três, cada um entrega um quarto.

Isso resolve tudo de uma vez e — o melhor — **entrega exatamente a fantasia que você descreveu**, sem regra extra:

- **Servo** tem uma invocação forte: metade da Rotina em cada, um corpo a mais no campo.
- **Matilha** tem muitos corpos fracos: um quinto da Rotina em cada, cinco corpos no campo.
- **Coro** encadeia: o dono e a invocação somam a mesma Rotina, mas de lugares diferentes.

O invocador troca **dano pessoal por presença de tabuleiro** — corpos que absorvem ataque, flanqueiam e bloqueiam caminho. Não é menos poderoso; é poderoso em outro eixo, que é o que o Caminho deveria fazer.

E é a leitura correta da obra: as maldições do Geto individualmente são frágeis. O que assusta é o número.

## 5. Energia: fixa pelo Caminho, sem atributo

> **PE por nível: 6 no Emanador e no Evocador. 5 na Vanguarda e no Guia. 4 no Bastião.**
> **E o PE máximo é esse número × o seu nível** — sem atributo e sem valor inicial (peça 1, seção 5.3).

*Revisado na v0.19.* Virou uma escada de três degraus, e ela tem uma contraparte: cada Caminho também tem a **sua própria vida por nível**, correndo no sentido contrário. A tabela completa está na peça 1, seção 5.1.

*A fórmula do máximo entrou na v0.26*, e está na peça 1, seção 5.3. A tabela de *"quantas vezes você lança o seu melhor feitiço"* do manual já é `6 × nível` nos seis pontos que mostra, então ela concorda — mas concordar não é a mesma coisa que mandar, e a seção 5.3 explica por quê.

| | Bastião | Vanguarda | Guia | Evocador | Emanador |
|---|---|---|---|---|---|
| vida por nível | 7 | 5 | 5 | 4 | 4 |
| PE por nível | 4 | 5 | 5 | 6 | 6 |
| **soma** | **11** | **10** | **10** | **10** | **10** |

**A soma é o número que importa.** Com ela praticamente igual nos cinco, a troca "couro contra combustível" é escolha de sabor e não degrau de poder — e o validador falha se a diferença passar de 2.

> **E é a soma que decide o que uma Origem sem energia amaldiçoada recebe daqui — v0.116.** *Esta peça não citava Origem nenhuma e a peça 9 não citava Caminho nenhum, então a combinação nunca tinha sido conferida:* **a Restrição Celestial pelo ramo da Maki diz *"sem PE"*, e os cinco Caminhos entregam PE.** *Com a coluna valendo zero, a soma cai para `7 · 5 · 5 · 4 · 4` — espalhamento `3`, e o validador acende.*
>
> **A regra que sai disso é da peça 9 §5, e ela não é gate:** *a coluna `por nível` vem inteira, e ela continua se chamando `PE`* — **`Pontos de Energia` para quem tem energia, `Pontos de Esforço` para quem não tem, e a sigla é a mesma.** *O tamanho é herdado desta tabela; **o que o PE compra** na rota sem energia é da Técnica Marcial.* *O argumento inteiro, com as três saídas que reprovaram, está na peça 9 §8.*
>
> **E a resposta chegou na v0.122, na peça 20: o `PE` compra a mesma coisa que compra no Fundamento** — pontos de montagem, na conta de `3 × Classe`. *Nenhum número desta tabela se moveu, e ela continua sendo a dona da coluna.*

*Corrigido na v0.15, revisado na v0.19.* A regra original dizia "6 nos Caminhos de técnica, 4 nos físicos", e o **Guia não era nem um nem outro** — ficava sem número. A divisão em duas famílias não cobria os cinco Caminhos, então ela virou uma escada de três degraus com cada Caminho nomeado.

O Guia e a Vanguarda ficam no meio, em 5. Os dois vivem entre bater e conjurar: o Guia estende efeito alheio e recupera, a Vanguarda alterna feitiço de Toque com golpe simples. Nenhum dos dois é conjurador puro nem lutador puro, e o 5 diz isso.

**O 6 do Emanador e do Evocador é o número mais caro de mexer**, porque o Fundamento tem uma tabela inteira de "quantas vezes você lança o seu melhor feitiço" calculada em cima dele. *Corrigido na v0.26:* isto não é o mesmo que "não é escolha nossa", que era como estava escrito. **É escolha nossa** — os limitadores do manual foram calibrados quando o sistema em volta era outro, e servem de continuidade, não de lei. Baixar o 6 é legal; o que não é legal é baixar sem regerar a coluna, porque aí a tabela do manual passa a mentir sobre a ficha. O 4 e o 5 são mais baratos porque não têm coluna pendurada neles.

Espírito **não entra na conta**, e o motivo é uma dicotomia que não tem meio-termo:

| fórmula | Espírito 0 | Espírito 6 | diferença | veredito |
|---|---|---|---|---|
| 6 + Espírito/2 | 6 | 9 | +50% | atributo obrigatório |
| 6 + Espírito/3 | 6 | 8 | +33% | ainda pesado |
| 6 + Espírito/4 | 6 | 7 | +17% | ruído — um ponto no teto |

Com teto de atributo em 6, qualquer divisor grande o bastante para não criar imposto entrega **um ponto** na ficha inteira. Ou o atributo importa de verdade e vira obrigatório — o que a peça 1 evitou de propósito ao tirar atributo da conta do feitiço —, ou ele não importa e não deveria estar na fórmula ocupando espaço na cabeça de quem lê. Não há faixa útil entre os dois.

**A base de 6 fica** porque o Fundamento tem uma tabela inteira de "quantas vezes você lança o seu melhor feitiço" calculada em cima dela. Baixar para 4 seria um corte de 33% que invalida aqueles números.

**O Bastião fica com 4**, e a assimetria se paga pela soma da tabela da seção 1: ele é o único dos cinco com **11** de vida mais energia por nível, contra `10` dos outros quatro. **Ele troca combustível por couro, e sai um ponto na frente da troca** — é o que faz escolher Bastião ser sabor e não degrau de poder.

> **O argumento que estava escrito aqui morreu na v0.81, e ele morreu invertido.** *Ele dizia: "o golpe simples dele rende ~10 e o Classe 0 do conjurador rende ~4,5 — menos combustível, melhor motor de reserva".* **O `~4,5` era o Classe 0 fantasma outra vez**, e desta vez ele sobreviveu à v0.80 porque a guarda daquela versão procurava a frase morta e não o número solto.
>
> **Com a tabela de dano do Classe 0 do manual na mão, o motor de reserva do conjurador é o MELHOR dos dois:**
>
> | nível | Classe 0 | golpe simples | quem rende mais |
> |---|---|---|---|
> | 2 | `2d8` = 9 | 9 | empate |
> | 10 | `3d8` = 13,5 | 10 | Classe 0 |
> | 30 | `6d8` = 27 | 12 | **Classe 0, em 2,25×** |
>
> *O `~10` batia com o golpe simples e o `~4,5` era o dano de um d8 — a régua de montar feitiço, não o dano de um Classe 0. A frase comparava uma linha certa contra uma errada.* **O número `4` não mudou; o que mudou é que ele parou de depender de um argumento que anda para trás.**

## 6. Múltiplos atributos por Caminho: passa, e já estava previsto

Sua quarta observação está certa e o mecanismo já existe na lista do que um Caminho pode conceder: **trocar o valor fixo de 2 do ataque de conjuração por um atributo.**

- **Emanador** conjura com Inteligência ou Essência.
- **Bastião** canaliza com Força.
- **Vanguarda** canaliza com Destreza.

> ⚠⚠ **A troca do `2` por um atributo MORREU na v0.117, e com ela o `2` — este parágrafo inteiro deixou de valer.**
>
> *Ele dizia que a troca era "neutra em balanço porque os dois crescem +3 na campanha, e foi exatamente isso que a peça 1 verificou".* **A peça 1 verificou que `2 + maestria` VALE um atributo investido — os dois eram o mesmo número em todo nível.** *A troca não substituía o termo inteiro: substituía só o `2`, que cresce `+0`. O resultado crescia `+6` contra `+3`.*
>
> **Hoje não existe `2` para trocar.** *O acerto de conjuração é `d20 + atributo da técnica + maestria` e a CD é `10 + atributo da técnica`, e o atributo é declarado na criação — qualquer um dos cinco.* **O que este Caminho concede não é mais "trocar o fixo": é o que sempre foi na prática — o Emanador aponta a técnica para Inteligência ou Essência, o Bastião para Força, a Vanguarda para Destreza.** *Isso deixou de ser habilidade e virou escolha de criação, na peça 1 §5.*

**O que sobrevive deste parágrafo é a segunda metade, e ela ficou mais verdadeira:** múltiplos atributos por Caminho passa, e não cria imposto — *quem não quiser especializar aponta a técnica para o atributo que já ia levar ao teto de qualquer jeito, e não perde nada.*


Para as **habilidades** de Trilha, não há restrição nenhuma: elas podem chavear em qualquer atributo que faça sentido. Nada nelas entra numa rolagem disputada onde o ritmo importa.

## 7. Perícias: a lista precisa crescer

> *Resolvido na v0.15, revisado na v0.16.* O quadro completo está em `07-pericias-e-oficios.md`: **vinte e três perícias e onze ofícios**, com o Caminho dando **duas perícias fixas mais quatro à escolha livre**, e dois ofícios livres. A análise abaixo é o que levou a isso e fica registrada. Note que **Sentir Energia mora em Essência** desde a v0.16, não em Inteligência.

Você quer 6 a 8 perícias por Caminho, e um sistema recheado. A lista de catorze não suporta isso:

| lista | treinadas (Caminho 7 + Origem 2) | fração |
|---|---|---|
| 14 perícias | 9 | **64%** — quase tudo |
| 26 perícias | 9 | 35% — sobra espaço para o grupo |

Com 64% treinado, "ser treinado" para de significar alguma coisa e o resto do grupo não tem em que brilhar.

**Proposta: expandir para 24 a 28 perícias**, cobrindo o que você quer de fora de combate — burocracia jujutsu, clãs e política, primeiros socorros, culinária, condução, ofícios, artes, línguas, sobrevivência urbana, rastreio, interrogatório. E aí 7 por Caminho fica confortável.

A lista definitiva sai junto com o quadro de perícias completo, que é peça própria.

## 8. Treinamento em equipamento

### 8.0 Qual Caminho treina o quê — fechado na v0.130

***Decisão do Mizuki.*** *Ela foi ditada na revisão do livro, na v0.106, e passou vinte e quatro versões existindo **só no PDF**, que é artefato.* **A peça 14 §5.4.1 já dizia que o eixo de acesso é o Caminho; qual Caminho pega o quê não estava escrito em peça nenhuma.**

| Caminho | treina | quais categorias |
|---|---|---|
| **Bastião** · **Vanguarda** | **as treze** | Simples, Marciais e Arma de Fogo |
| **Guia** · **Emanador** · **Evocador** | **duas** | `Arma de Fogo` e `Balestra` |

> **Para um conjurador empunhar o resto, a porta é a Trilha.** *É o que faz a `Empunhadura` do `Arremate`, no nível 2: ela concede um grupo de arma à escolha e ainda troca Força por Inteligência ou Essência naquele grupo.* **Um Emanador de espadão existe, e paga com a escolha de Trilha.**

**Duas coisas que esta linha decide, e as duas foram confirmadas pelo Mizuki na v0.130:**

- **O Guia fica no lado conjurador.** *Ele é `5` de vida e `5` de PE, meio a meio, e nenhuma das três Trilhas dele — `Elo`, `Sutura`, `Perímetro` — tem conteúdo de arma.*
- **"As treze" inclui `Arma de Fogo` para Bastião e Vanguarda.** *Com isso a rota `Arma de Fogo` do `Batedor` é **especialização** e não acesso, que é coerente com o texto dela: ela entrega `Ferrolho` e `Mirar`, e nunca treino.*

> **⚠ A `Balestra` é a única categoria Simples que um conjurador pega de graça.** *As outras seis da lista Simples — `Lâmina Curta`, `Porrete`, `Ceifa`, `Arremesso`, `Manopla`, `Massa` — ficam atrás da Trilha para os três.* **A divisão simples/marcial da peça 14 §5.4.1 continua sendo sobre identidade e não sobre poder**, e esta linha não mexe nela: ela diz quem alcança cada balde, e não quanto cada balde entrega.

*A penalidade de quem empunha sem treino é da peça 19 §6: desvantagem na rolagem de ataque, e `−3 m` de deslocamento se faltar o requisito de Força.*

### 8.1 O que ainda não tem número

Confirmado que precisa existir. Três categorias, e cada Caminho concede as suas:

- **Armas:** simples, marciais, de fogo, ferramentas amaldiçoadas
- **Proteção:** leve, pesada (com requisito de Força e limite de Destreza na Defesa)
- **Escudo:** categoria própria, porque ele ocupa uma mão — e mão ocupada conversa com a Restrição **Gesto**, que já existe e exige as duas mãos livres

> **Quais armas caem em qual balde foi decidido na v0.47, e mora em `14-equipamento.md` §5.4.1.** Simples: `Lâmina Curta` · `Porrete` · `Ceifa` · `Arremesso` · `Manopla` · `Massa` · `Balestra`. Marciais: `Lâmina Longa` · `Machado` · `Armas Longas` · `Flexível` · `Yumi`. `Arma de Fogo` é a de fogo, sozinha, e ferramenta amaldiçoada continua sem peça.
>
> **A divisão é acesso e nunca preço** — toda arma fecha no mesmo orçamento, e os dois baldes chegam ao mesmo teto de dado (`d8` numa mão, `d12` em duas). *Ela restringe qual identidade, não quanto poder*, que é o contrário do que a divisão faz no sistema de onde ela veio.
>
> **O que isto obriga a Trilha a saber:** a Trilha de corpo a corpo de um Caminho não-marcial **concede o treino marcial**, e é assim que o Emanador que quer lutar de espadão paga com a escolha de Trilha em vez de ganhar de graça. **Treino de arma não é dado de dano** — é acesso, que está na lista do que a seção 4 da peça 5 permite um Caminho conceder.
>
> *A proteção e o escudo continuam como esta seção os deixou; o que fechou foi só a linha das armas.*

Esse último ponto é um achado pequeno mas real: **escudo e Gesto se cancelam.** Quem usa escudo não pode montar feitiço com a Restrição Gesto, e isso é uma decisão de ficha interessante em vez de um bug.

## 9. Em aberto

- ~~**Quantas Trilhas um personagem acumula** ao longo da campanha, e em que níveis.~~ **Fechada na v0.55 e na v0.60:** uma Trilha por ficha, entregas nos níveis `2 · 11 · 19 · 27`, e degrau de Caminho em `2 · 7 · 15 · 30`. *O calendário de Caminho era `7 · 15 · 23 · 29` até a v0.70, e o dono dele é o `DESENHO-caminhos.md`.*
- ~~**Como Torrente cobra o segundo feitiço da rodada.**~~ ***FECHADA na v0.131, e as três coisas que a pendência afirmava reprovaram na medida.*** *Ela ficou aberta desde a v0.14.*

  > **Ela cobra em PE, no preço que o manual já dá para a Melhoria `Rápido`** — `Classe e meia`, arredondando para cima, que é a coluna `Pesada`. **Não existe lista de pontos à parte e não existe moeda nova.** *A pendência dizia que "uma lista de pontos à parte é o modelo mais provável", e o `RASCUNHO-trilhas.md` §4 mandava passar essa moeda pelo `conferir-orcamento.py` antes de ela ter número. Os dois ficam sem objeto.*

  **E o conserto da seção 4 NÃO serve, medido em três níveis.** *Aquela seção diz "você e todas as suas invocações somados entregam uma Rotina", e a pendência propunha copiar a frase trocando corpo por feitiço.*

  | nível | maior Classe | o feitiço sozinho | Rotina | folga para o segundo | o `Classe 0` que a regra de ouro nº 6 já permite |
  |---|---|---|---|---|---|
  | 11 | 3 | `40` | `45` | **`5`** | `18` |
  | 21 | 6 | `81` | `94` | **`13`** | `22` |
  | 30 | 7 | `94` | `108` | **`14`** | `27` |

  > **O teto proposto é mais apertado que a regra que ele existia para vigiar.** *Aplicá-lo tornaria ilegal o `Classe 0` que o Fundamento concede de graça, em todo nível do 5 em diante.* **A leitura alternativa — cada feitiço entrega metade da Rotina — dá a mesma folga de `14` e ainda exige cortar o feitiço grande de `94` para `54`**, coisa para a qual o sistema não tem mecanismo.

  **A razão é estrutural, e é ela que responde a pendência.** *A invocação põe um **corpo** a mais no campo, e corpo multiplica: um dobra a saída por rodada, três quadruplicam. Foi contra essa escada que o teto somado foi escrito.* **A `Torrente` não põe corpo nenhum** — ela usa a Ação Padrão e a Ação Bônus que a ficha já tem, e o número de feitiços por rodada **trava em dois, em todo nível, para sempre.** *Não existe escada para segurar.*

  > **O que ela é de verdade: a primeira coisa do sistema que faz a regra de ouro nº 6 trabalhar.** *A seção 3 desta peça já media que ninguém alcança o segundo feitiço pelo Fundamento — pôr `Rápido` no feitiço grande derruba a rodada de `94` para `72`.* **A regra estava escrita e era inalcançável; a Trilha é a porta.**

  ***E a medida cobrou preço: o `Acelerar` do nível 2 estava publicado em ZERO fatia.*** *Ele libera a Ação Padrão, e um `Classe 0` de `27` cabe nela — o que o `CHANGELOG` da v0.81 já preçava em `5,31` fatias por rodada, ou `2,87` à taxa de `54%` do relógio dela.* **A Trilha foi de `4,65` para `7,52` de `5,00`, com o estouro de `50%` aceito e declarado, no precedente da `Brasa`.** *A `Vazão` ganhou cláusula de piso na mesma versão, porque no nível 11 o teto dela ficava abaixo do `Classe 0`. A conta inteira está no `DESENHO-trilhas.md`.*
- ~~**O que Elo, Sutura e Perímetro entregam** que valha o golpe por rodada que o Guia não tem (seção 3.1).~~ **Respondida na v0.61, e a resposta é um número:** eles valem **o vão desta seção**, e ele chega como o degrau de Caminho do nível 7 — o mesmo lugar em que o Bastião e a Vanguarda recebem o ataque extra. *Com isso os cinco Caminhos empatam em `+6%` da Rotina no nível 30. A conta está no `RASCUNHO-trilhas.md` §3.4; **o que cada uma das três entrega em ficção continua sendo a Q5.***

*Resolvidos e tirados daqui:* os **nomes das Trilhas**, fechados na v0.24 — as seis que colidiam viraram Batedor, Executor, Sutura, Perímetro, Servo e Matilha, e o `conferir-nomes.py` falha se alguma voltar. E **se o Coro deixa o dono e a invocação agirem no mesmo turno**: deixa, e não custa nada, porque o orçamento dividido da seção 4 é teto de saída e não de número de ações (seção 3.1).
