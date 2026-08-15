# O que ficou decidido nesta sessão, e ainda não subiu

*Nada disto está aplicado nos documentos do projeto. É a fila de escrita para quando você mandar salvar — cada linha diz onde ela vai morar e o que ela desfaz.*

---

## Decidido

### 1. Piso de taxa de `20%`, e a lista de gatilhos vira fechada

**Onde mora:** `RASCUNHO-trilhas.md` §3.4-B (a segunda metade do método) e §5 (duas checagens novas).
**O que desfaz:** os `15%` do `Servo` no §6.10.
**Fonte do número:** o teto de `-80%` de limitação do GURPS, e é onde a escada de Classe Passiva do §3.1 já parava.
**A lista está em `LISTA-gatilhos-trilhas.md`.**

### 2. A invocação some quando o DONO cai

**Onde mora:** peça 15 §3.5, que é a dona da morte e do retorno. Fecha a segunda das duas dívidas que a v0.67 achou por tropeço.
**O preço, medido depois da escolha:** vale de `0,34` a `1,14` fatia conforme quantas vezes o dono cai — até **28% do orçamento da Trilha**, e nenhum outro Caminho paga isso.
**Onde ela morde de verdade:** no `Insistir` da peça 1 §5.5. Quem apaga não perde nada a mais, porque já está apagado. Quem fica de pé pagando vida continua **sem o Caminho dele**, e reinvocar custa a ação padrão — ele paga a rodada inteira e não ataca.
**Fica como dívida declarada, com o número escrito.** *Não é buraco; é preço que alguém tem de ver antes de escolher `Insistir` de Evocador.*

### 3. A invocação volta na ação do dono, na MESMA rodada

**Onde mora:** peça 15 §3.4, junto do custo de reinvocar.
**Esta a conta decidiu, não é sabor.** Nunca existiu regra sobre quanto tempo ela fica fora — grep vazio no repositório inteiro. As duas leituras possíveis do texto atual dão:

| leitura | taxa de *"estar de pé"* | spread | |
|---|---|---|---|
| **volta na ação do dono, mesma rodada** | `60%` a `92%` | **`1,54×`** | passa |
| volta no turno seguinte | `20%` a `85%` | `4,24×` | **reprova** — o filtro do projeto para em `3,0×` |

*Com a decisão nº 2 somada, o spread vai a `2,89×` no cenário de o dono cair 1,5 vez por dia — ainda passa, e com pouca folga.*

### 4. O calendário NÃO muda

`2 · 11 · 19 · 27` de Trilha e `7 · 15 · 23 · 29` de Caminho, iguais para as quinze. **Validado em `AUDITORIA-trilhas-v0.69.md` §6**, por três rotas independentes. *A recomendação contrária era minha e caiu.*

---

## Medido, e ainda sem decisão

| achado | onde ele bate |
|---|---|
| **a régua reprova `0` de `8` famílias** hoje — a taxa é o grau de liberdade | §3.4-B |
| os **`15%` do `Servo` saem da subtração**: `5,07 − 1,56 − 1,80 = 1,71`, e `1,71 ÷ 11,50 = 14,9%` | §6.10 |
| com o piso, o `Servo` publicado **estoura em `12%`** | §6.10 |
| **três entregas pagas consomem `4` fatias** — a quarta sai de graça | §6.10 e §3.4-B |
| o **treino tem conversão**: `10` pontos percentuais num TR, `5` a `20` numa perícia | §3.4-B |
| **variância do `Coro` a `90%` cai para `2,13`** contra `2,09` do `Servo` — a ordem das três se inverte e duas colapsam | §6.4 |
| o **levantamento do 5e 2024 está errado** — 6 classes conferidas, 1 no calendário padrão, 2 com três entregas | CHANGELOG v0.60 e §3 |
| **só posicionamento é permanente e cabe** — a forma *"três permanentes e um botão"* do `Servo` não é construível | §6.4 |
| **três dos quatro alvos de `recuperar` nunca foram preçados** — ferimento, condição e Integridade. Só `PE` tem número | peça 5 §4 e §6.9 |

---

## O que trava o catálogo da camada de vínculo, e é a próxima conta

*Corrigindo o que eu disse antes:* a camada de vínculo **é** a categoria certa — isso a v0.68 já decidiu e continua de pé. **Mas ela não abre botão novo.** Ela obedece à mesma lista de sete linhas da peça 5 §4, e muda só a **condição**, não a magnitude.

**Então o que abre espaço para entrega permanente e pequena não é a categoria — é a linha `recuperar`, que tem quatro alvos e só um preço:**

> **`Recuperar — PE, ferimento, condição, Integridade`** *(peça 5 §4)*
> `PE` vale `5,14`. **`ferimento`, `condição` e `Integridade` nunca foram convertidos.**

`condição` depende da peça de **dano e condições**, que não está na fila — essa fica fora. **`ferimento` e `Integridade` dá para preçar**, e o projeto tem os donos: a vida por Caminho da peça 6, a tabela de inimigo do manual, e a Integridade plana `20 + 8(nv−1)` da peça 1.

*E há um aviso do próprio projeto em cima disso:* a peça 11 §6 escreve que a Reação de RD *"não é redução de dano passiva — a regra que matou a Casca continua valendo"*. **Preçar recuperação de ferimento vai esbarrar nessa regra**, e é melhor achar isso antes de escrever doze entradas em cima dela.

---

## A conta foi rodada, e ela derrubou a saída — e achou a causa raiz

**`recuperar ferimento` e `recuperar Integridade` reprovam os dois.** *Eu tinha apontado as duas como a saída; não são.*

### `recuperar ferimento` — vale zero para quem não cai

*O primeiro modelo que rodei estava errado: ele contava rodada de vida depois de a luta já ter acabado. Corrigido — o ganho trunca na duração da luta, `3,3` rodadas.*

Quanto vale *"recuperar 2 de vida por rodada"*, em dano por rodada, no nível 30:

| ficha | mestre espalha | puxa o dobro | foca metade | foca em você |
|---|---|---|---|---|
| Evocador Con 0 | `0,00` | `0,00` | **`3,27`** | `1,58` |
| Vanguarda Con 3 | `0,00` | `0,00` | `0,00` | `0,00` |
| Bastião Con 6 | `0,00` | `0,00` | `0,00` | `0,00` |

**O Bastião no nível 30 aguenta `21,9` rodadas contra uma luta de `3,3`. Ele nunca cai, e a entrega vale exatamente nada para ele.** O eixo que decide quanto ela vale é **em quem o mestre resolve bater** — e isso é a mesma família de defeito que matou a Casca, que valia *"6% a 42% conforme um número que não existe em lugar nenhum do material"*.

*E a comparação com a **Escama**, que foi aprovada com esse mesmo formato de tudo-ou-nada, separa as duas: a Escama é **aposta do jogador** — o tipo é preso à Regra, escrita na criação, antes de qualquer um saber o que a campanha vai mandar. Recuperar vida é **decisão do mestre**, tomada em jogo. O filtro do projeto reprova a segunda e aceita a primeira.*

### `recuperar Integridade` — quase ninguém chega lá

| nv | ficha | vida | Integridade | o que acaba primeiro |
|---|---|---|---|---|
| 30 | Evocador Con 0 | `122` | `252` | **o corpo** |
| 30 | Vanguarda Con 3 | `243` | `252` | **o corpo** |
| 30 | Bastião Con 6 | `395` | `252` | a alma |

*O `ESTADO-ATUAL` já marcava isso para playtest — "a alma é maior que o corpo em quatro dos cinco Caminhos, então quase todo mundo cai antes". Confirmado com número.* **Recuperar Integridade só vale para o Bastião de Constituição alta, que é justamente quem menos precisa.**

### E aí aparece a causa raiz de tudo

**Inventário completo do que a peça 5 §4 deixa uma Trilha vender:**

| linha do permitido | estado |
|---|---|
| treino em perícia / TR | **utilidade** — sem conversão em dano |
| mover · reposicionar · forçar reposicionamento | **viva** |
| escolher ou trocar alvo | **viva**, só com janela |
| recuperar **PE** | **viva** |
| trocar o fixo do acerto por atributo | viva, mas come 85% do orçamento numa entrega só |
| estender duração | **morta** na v0.68 — `11` a `43` fatias |
| recuperar **ferimento** | **reprova** — o eixo é quem o mestre foca |
| recuperar **Integridade** | **reprova** — o corpo cai antes |
| recuperar **condição** | **bloqueada** — peça de dano e condições, fora da fila |
| exceção de ação | **reprova** — `17` fatias contra um orçamento de `4` |

**Cruzando o que sobra com as taxas que a lista de gatilhos permite, saem seis entregas legais — e elas vêm de TRÊS tipos de efeito:**

| | vale |
|---|---|
| trocar alvo · `1×` por descanso curto | `2,75` fatias |
| recuperar PE · quando você acerta | `2,03` |
| **mover · permanente** | `1,42` |
| recuperar PE · `1×` por descanso curto | `1,23` |
| mover · quando você acerta | `0,71` |
| mover · `1×` por descanso curto | `0,43` |

> **São `60` entregas para escrever — quatro por Trilha, quinze Trilhas — e existem `3` tipos de efeito para escrevê-las.** *Mais treino, que é utilidade e não tem preço.*

**Isto é a causa raiz, e ela não é do método de preço nem do calendário.** A Q3 foi reformulada duas vezes, o `Servo` não fecha e as Trilhas *"parecem todas iguais"* — as três coisas saem daqui. **A sua intuição estava certa e o motivo é este: elas vão parecer iguais porque só existem três coisas para vender.**

---

## A média de dano recebido, derivada — e ela é peça nova de referência

*Pedida pelo Mizuki, porque eu estava supondo. **A tabela de inimigo existe no manual e ninguém tinha usado ela para isto** — é a tabela 76, com chefe e capanga, vida e dano, do nível 5 ao 30.*

**Ela é auto-consistente, e isso foi conferido antes de usar:** vida do chefe ÷ dano do grupo dá **`3,7` rodadas em todos os seis níveis**, sem exceção. O `ESTADO-ATUAL` diz que o combate deve levar `3,4` a `4,0`. **Confere.**

**E o encontro de capangas bate `2,8` a `4,4` vezes mais que o de chefe** — cinco a oito capangas equivalem a um chefe em vida, e somados eles causam muito mais dano por rodada.

> **A média de dano que um personagem recebe por rodada, num grupo de quatro, num encontro misto:**

| nível | só chefe | só capangas | **misto — usar esta** |
|---|---|---|---|
| 5 | `3,8` | `16,5` | **`10,1`** |
| 10 | `6,5` | `23,8` | **`15,1`** |
| 15 | `9,5` | `30,0` | **`19,8`** |
| 20 | `12,2` | `34,9` | **`23,6`** |
| 25 | `15,2` | `42,3` | **`28,8`** |
| 30 | `18,0` | `49,9` | **`33,9`** |

**Com ela, quantas rodadas cada ficha aguenta contra uma luta de `3,7`:**

| nv | Evocador Con 0 | Evocador Con 3 | Vanguarda Con 3 | Bastião Con 6 |
|---|---|---|---|---|
| 5 | **`2,2` — cai** | **`3,7` — no fio** | `4,3` | `6,9` |
| 15 | **`3,1` — cai** | `5,4` | `6,2` | `10,1` |
| 30 | **`3,6` — cai** | `6,3` | `7,2` | `11,7` |

*Correção do que eu tinha dito: o Bastião aguenta **`3,1×`** a luta, não `6×`. Eu estava usando o golpe de chefe cheio como se ele batesse no mesmo alvo toda rodada.* **A conclusão não muda: só o Evocador de Constituição 0 cai, e no nível 5 o de Constituição 3 fica no fio.**

### E a Integridade, com a regra que o manual tem escrita

*O Mizuki apontou que vida e Integridade são barras separadas de propósito e pediu para contar as duas separadas. **Ele está certo sobre o desenho, e o manual tem uma regra que muda a conclusão:***

> **"Cada ponto de dano na alma tira `1` de vida, `1` de Integridade e derruba a sua vida máxima em `1`, até o próximo descanso longo."**

**Dano de alma esvazia as duas barras ao mesmo tempo.** Então não é que a alma "quase nunca é usada" — é que **quem tem menos vida que Integridade morre pelo corpo antes de a alma acabar**, com o mesmo golpe:

| nv 30 | vida | Integridade | acaba primeiro |
|---|---|---|---|
| Evocador Con 0 | `122` | `252` | **a vida** |
| Evocador Con 3 | `212` | `252` | **a vida** |
| Vanguarda Con 3 | `243` | `252` | **a vida** |
| Bastião Con 6 | `395` | `252` | a Integridade |

**Três das quatro fichas, em todo nível.** *Recuperar Integridade só vale para quem já tem vida sobrando — que é quem menos precisa.*

> **Ressalva que é do próprio projeto:** a peça 1 §5.5 diz que *"a Integridade vai escalar com Essência, virando uma segunda vida de verdade"*. **Quando isso entrar, esta conta muda inteira, e a linha `recuperar Integridade` pode voltar a valer.** Fica registrado para não redescobrir.

---

## As três saídas, medidas

### A — as quinze se diferenciam por magnitude e taxa, sem tipo novo

Cruzando os três tipos vivos com as magnitudes e as taxas legais: **13 entregas, 45 montagens que fecham no orçamento.** Parece bastante. **Mas assinaturas de tipo distintas — que é o que o jogador enxerga — são cinco:**

`alvo + mover + mover` · `alvo + mover + PE` · `mover + mover + mover` · `mover + mover + PE` · `mover + PE + PE`

> **Quinze Trilhas para cinco assinaturas: três Trilhas por assinatura.** E `mover` aparece nas cinco.

**Custo:** nada muda em peça nenhuma, e a peça 5 fica intacta. **O preço:** as quinze vão se parecer, e a diferença entre elas vai morar na ficção e na magnitude, não no que elas fazem.

### B — abrir o que a peça 5 nunca proibiu

**A peça 5 tem uma incoerência interna, e ela nunca foi notada.** A frase-trava lista **quatro** coisas — *"um Caminho mexe em posicionamento, alvo, duração e recuperação"*. A lista logo abaixo tem **sete**. As duas não batem.

**E defesa não está em nenhuma das duas listas — nem no permitido, nem no proibido.** O proibido tem quatro itens: dados de dano, aumento de Classe, Melhoria de graça e cura. Defesa não é nenhum deles.

> **E o projeto já anda por cima dessa lacuna.** A peça 6 descreve o Bastião como *"o corpo como resposta: aguentar, encarar, prender"*, e a fila do rascunho manda medir *"a reação de Redução de Dano do Bastião"*. **Aguentar é defesa, e a peça 5 nunca autorizou.**

| o que abriria | vale, no nv30 | em fatias |
|---|---|---|
| acerto `+1` | `5,40` | `4,26` |
| Defesa `+1` (5 pontos percentuais de dano evitado) | `1,70` | `1,34` |
| Defesa `+2` | `3,39` | `2,67` |

**Defesa `+1` cai em `1,34` fatia, que é exatamente o tamanho de uma entrega.** *É o único molde novo que nasce no tamanho certo sem precisar de janela.*

> **O "se" que decide:** hoje o projeto **não tem conversão de dano evitado para dano causado**, e é a mesma conversão que faltou em `recuperar ferimento`. **A diferença é que defesa vale para todo mundo em toda rodada, e recuperar só vale para quem ia cair.** Defesa não tem o buraco do "só se você cair".

**Custo:** mexe na peça 5, que é fundação, e obriga a escrever a conversão de defesa. **O que devolve:** um quarto tipo, no tamanho certo, e a incoerência da peça 5 fecha de qualquer jeito.

### C — mais utilidade, menos número

| quantas utilidades | quantas pagas | tamanho de cada paga | moldes que cabem |
|---|---|---|---|
| 1 | 3 | `1,33` fatia | **3** |
| 2 | 2 | `2,00` | **2** |
| 3 | 1 | `4,00` | **0** |

> **Ela aperta em vez de aliviar.** Quanto mais utilidade a Trilha carrega, **maior cada entrega paga tem de ser** — e as grandes são justamente as que não cabem. Com três utilidades, nenhum molde do permitido serve.

**Custo:** nada muda. **O preço:** o repertório encolhe em vez de crescer, e a utilidade continua sem preço, o que é a dominância que a auditoria já achou.

---

## A fila, na ordem em que uma trava a outra

1. **Preçar `recuperar ferimento` e `recuperar Integridade`** — é a conta que destrava entrega permanente e pequena.
2. **Escrever o catálogo da camada de vínculo** — as doze entradas, com gatilho da lista e taxa acima do piso.
3. **Remontar as três formas** — o `Servo`, e depois a `Matilha` e o `Coro`, que nunca foram montados.
4. **O validador** — a spec do §5, agora com as duas checagens novas do piso e do gatilho.
