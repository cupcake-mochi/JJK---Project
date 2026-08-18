# CAMINHO E COMBATE SEM FEITIÇO

**Fase 4, quinta peça.** O chassi do personagem e como alguém luta com o corpo num sistema onde o poder mora na técnica.
Versão v0.13, corrigida na v0.15 e na v0.24 — 08/08/2026

As duas coisas andam juntas porque o Caminho é o lugar natural onde o combatente físico existe sem quebrar a economia do Fundamento.

> **Duas partes desta peça foram substituídas pela peça 6.** A seção 3 dizia que o feitiço de Toque soma arma e Força — está corrigido abaixo, e a conta que derruba isso está na peça 6, seção 3. O quadro de Caminhos da seção 4 era rascunho: os nomes definitivos são **Bastião · Vanguarda · Guia · Emanador · Evocador**. O resto da peça continua valendo.

---

## 1. O trabalho de Força

Força governa **ataque corpo a corpo, agarrar, quebrar, Atletismo, capacidade de carga e requisito de arma e de proteção**. Armas de dado maior e uniformes mais pesados exigem Força mínima; quem luta com Destreza fica nas armas leves.

> **Esta frase ficou sem implementação da v0.44 à v0.46, e ganhou uma na v0.47.** O requisito morava na *classe* de arma, e a classe deixou de ser o preço na v0.44 — o catálogo passou duas versões com **zero armas** carregando requisito escrito, e nenhum validador cruzava esta linha com ele. **Hoje o requisito é `Força 3` nos dois degraus de cima de cada escada de dado**: `d10` e `d12` no corpo a corpo, `2d8` e `2d10` no tiro. Mora em `14-equipamento.md` §5.5, e vem para cá quando aquela peça fechar.
>
> **A segunda metade da frase se cumpriu sozinha, e isso vale registrar.** As oito armas com `Fineza` — a rota de quem luta com Destreza — **param todas em `d8`**, então nenhuma delas encosta no requisito. *Ninguém impôs isso: caiu do orçamento, porque `Fineza` custa um ponto e o que sobra não paga dado grande.* A promessa e a régua chegaram no mesmo lugar por caminhos diferentes, que é o contra-teste que ela nunca tinha tido.
>
> **E o requisito continua não custando nada em ponto de atributo:** `Força 3` é o teto da criação (peça 2 §2). Ele resolve **acesso**, não preço — o que esta seção já concluía e agora tem catálogo para provar.

Isso é o modelo clássico do d20, e ele tem uma armadilha conhecida que vale medir antes de aceitar.

**Destreza faz mais coisas.** Ela dá ataque à distância, **Defesa**, **iniciativa**, quatro perícias e uma opção no Teste de Resistência Físico. Força dá ataque corpo a corpo, uma perícia, a mesma opção de TR e o acesso a equipamento. Para empatar, a arma pesada precisa devolver em dano o que Destreza entrega em defesa:

| nível | inimigo bate | quanto +1 de Destreza evita num combate de 3 rodadas |
|---|---|---|
| 5 | 15 por rodada | ~2 de dano |
| 10 | 26 por rodada | ~4 de dano |
| 15 | 38 por rodada | ~6 de dano |
| 20 | 49 por rodada | ~7 de dano |

Um dado de arma maior — 1d10 no lugar de 1d6 — rende cerca de **+2 por golpe**. Isso empata o valor defensivo por volta do nível 5 e fica para trás depois, sem contar iniciativa e as três perícias extras.

**Conclusão: requisito de arma resolve o acesso, não o balanço.** Ele dá a Força um trabalho real e é bom que exista, mas não é ele que impede Destreza de dominar. O que resolve está na seção 3, e não tem a ver com armas.

## 2. Uma arma sozinha não cabe no jogo

Este é o achado da peça, e ele muda o desenho.

O Fundamento tem uma coluna chamada **Rotina**: o dano por rodada que um personagem deveria estar entregando em cada faixa. E o manual já avisa, numa nota de rodapé, que *"se a sua mesa tem uma classe que bate em vez de conjurar, o dano dela por rodada precisa ficar na coluna Rotina"*.

Rodando a conta:

| nível | Rotina | arma 1d10 + Força | quanto falta |
|---|---|---|---|
| 2 | 13 | 8,5 | 1,5× |
| 10 | 45 | 9,5 | 4,7× |
| 20 | 76 | 10,5 | 7,2× |
| 30 | 108 | 11,5 | 9,4× |

**Uma arma entrega entre 11% e 65% do que a coluna pede, e a diferença cresce.** Não é escolha de dado: trocar d6 por d12 muda três pontos numa lacuna de cem. Falta uma ordem de grandeza inteira.

Nenhuma quantidade de requisito de Força, nenhuma tabela de arma e nenhum ajuste de dado conserta isso. O combatente físico precisa de outra coisa.

## 3. Canalizar Energia

> ## O "golpe canalizado" nunca existiu — v0.81
>
> *O termo `golpe canalizado` tem **zero** ocorrências no manual — junto com `canalizado`, `canaliza`, `Canalizar` e `golpeadora`.* **Ele era abreviação de *feitiço de Forma Toque*, e a palavra "golpe" fez um feitiço parecer um ataque.** Foi trocado por `feitiço de Toque` em 39 lugares, **sem mexer em número nenhum**.
>
> **A aptidão `canalizar energia` fica** — ela é termo da obra e a peça 11 a lista entre as doze que o material obriga. *O que ela faz é deixar você lançar a sua técnica como feitiço de Forma Toque.*
>
> ### A dívida que a v0.81 deixou aqui FECHOU na v0.82, e ela nunca foi dívida
>
> *Esta seção carregou por uma versão um aviso de `⚠⚠ LIMPAR ANTES DO PDF`: a peça 6 §3 publica o físico em `106` e a decisão daquela versão parecia implicar `94`.* **Ela não implicava.**
>
> **A peça 6 §3.1 sempre teve a linha `feitiço de Toque + golpe simples` marcada como EXISTENTE na tabela dos três turnos.** *O que faltava não era refazer conta — era dizer de onde o golpe vinha, e aquela seção já tinha escrito a resposta como "anotado, não decidido".*
>
> **De onde ele vem: do ataque extra do nível 7, que é um golpe solto por rodada e não exige a Ação de Atacar.** *Decidido na v0.82 e escrito na peça 6 §3.1, com validador em cima.*
>
> **A alternativa foi medida antes de ser descartada, senão isto seria gosto e não conta.** Com o ataque extra preso à Ação de Atacar, dois golpes rendem `23` no nível 30 e **um Classe 0 grátis rende `27`**. *A habilidade de nível 7 de dois Caminhos perderia para o botão que toda ficha já tem, ninguém usaria a Ação de Atacar, e o físico e o conjurador terminariam idênticos em `60,50` de dano por rodada.*
>
> ***O achado é do Mizuki, e ele veio de uma pergunta e não de uma conta:*** *"já é um ataque extra, é uma mecânica forte, não acho que precisa disso."* **Ele estava certo, e três mensagens de orçamento tinham sido construídas em cima da premissa errada.**
>
> **Nenhum número se moveu.** O vão continua `9 · 10 · 11 · 12`, o nível 7 continua de graça nos cinco Caminhos, e o `Arremate` e o `Resquício` continuam como estavam.

A obra já deu a resposta, e ela é uma das aptidões básicas que todo feiticeiro tem: **você empurra energia amaldiçoada pelo corpo e pela arma.** É por isso que um feiticeiro consegue ferir uma maldição e uma pessoa comum não.

A forma mecânica cai sozinha quando você olha os números:

> **Um feitiço de Toque é um feitiço de Forma Toque, sem Melhoria e sem Restrição.**
> Mesma Classe, mesmo orçamento de pontos, mesmo custo em PE. Os pontos viram dados de dano — **e nada mais entra**: o feitiço de Toque não soma arma nem Força.

**Corrigido na v0.15.** A primeira versão desta linha dizia que o golpe ainda somava arma e Força por cima. Não fecha: com os dois somados e ataque extra, o físico fica **131% acima da Rotina no nível 2**. Arma e Força são o que você faz quando **não** canaliza. A conta está na peça 6, seção 3.

Não foi uma escolha estética. Foi o que a conta apontou:

| nível | dados de energia que faltam para o golpe atingir a Rotina | pontos que a Classe do nível dá |
|---|---|---|
| 2 | 1 | 3 |
| 10 | 8 | 9 |
| 14 | 12 | 12 |
| 18 | 16 | 15 |

As duas colunas andam juntas porque são a mesma economia. O feitiço de Toque não é uma mecânica nova — é o **feitiço vazio**, o que sobra quando você tira toda a customização de um feitiço e fica só com o orçamento bruto.

E é exatamente por isso que ele é a aptidão básica de todo feiticeiro, e por que ter uma técnica continua sendo melhor: **a técnica compra Melhorias, o golpe não.** O mesmo orçamento, gasto no formato mais burro possível, entrega dano num alvo só e nada mais. Sem área, sem alcance, sem condição, sem escolher quem é atingido.

### O que isso explica de graça

**Maki.** Sem energia amaldiçoada, ela não canaliza — o golpe dela fica nos 8,5 da tabela acima, que é dano de pessoa comum. Ela só compete porque a **ferramenta amaldiçoada carrega a energia por ela**. O sistema explica a personagem sem precisar de regra especial: uma arma que canaliza sozinha é um item caríssimo, e é assim que ela deve ser precificada.

**Por que socar é a saída quando o PE acaba.** O golpe sem canalizar é o equivalente físico do feitiço de Classe 0: pequeno, grátis, sempre disponível.

**Por que o combatente físico não tem Liberação Máxima.** O manual já dizia isso e agora tem motivo: Liberação é o pico que rompe o teto de dano num alvo, e o feitiço de Toque já vive no teto de um alvo o tempo todo, sem gastar montagem.

## 4. O Caminho

O chassi. **Escolhido na criação**, com poucas escolhas de Trilha ao longo dos níveis.

### A trava

> **O Caminho não dá poder novo. Ele muda o que o seu poder alcança.**
> **A cerca são seis proibições. Fora delas quem decide não é a lista — é o preço, e onde não existe preço, o teto de maestria.**

O motivo da primeira é o pilar 1: a técnica é a identidade. Se o Caminho desse dano, dois personagens do mesmo Caminho começariam a se parecer, e a coisa que os distingue — a técnica que cada um escreveu — perderia espaço.

> **Esta seção era uma lista fechada de sete linhas até a v0.71, e ela tinha dois defeitos medidos.** A frase-trava enumerava **quatro** coisas enquanto a lista abaixo tinha **sete** — as duas nunca bateram. E o desenho dos cinco Caminhos usou **oito** entregas que nenhuma das sete autorizava, incluindo três que o próprio projeto já tinha aprovado. *Enumerar no topo é o que envelhece; a cerca não.*

### A cerca — seis coisas que um Caminho nunca dá

- **Dado de dano.** O dado do soco e o da arma são **equipamento**; o Caminho mexe no que se faz com eles.
- **Aumento de Classe de feitiço.**
- **Melhoria de graça.**
- **Cura**, que é Forma de feitiço — quem fechou a Família Amparo nunca vai curar, e nenhum Caminho contorna isso.
- **Redução de Dano passiva.** Resistência a um tipo, sim; desconto em tudo, não. *É a regra do manual que matou a Passiva Casca na v0.26, e ela nunca tinha sido escrita nesta peça — a v0.70 furou ela desenhando uma reação de RD para aliados antes de alguém notar.*
- **Refino dentro de uma rolagem** — acerto, CD, Defesa, Teste de Resistência ou dano. Ele cresce `+7` a `+9` na campanha contra os `+3` de quem está do outro lado, e não existe número que conserte isso. *Fora da rolagem ele continua valendo: custo, frequência, escopo e disputa contra outro refino são a peça 11 e não mudam aqui.* **A métrica do Caminho é a maestria**, que cresce `+3`.

### O que um Caminho concede — exemplos, com preço

**A tabela é exemplo e não fronteira.** Entrega que não está aqui é legal se passa da cerca e se o preço cabe no degrau. *Medido no nível 30, que é onde a fatia foi definida.* **A fatia é `5,08` de dano por rodada, e uma Trilha inteira leva `5` fatias** — a coluna abaixo foi reconvertida na v0.74, e ela estava na escala de `1,27` de quatro versões atrás.

| família | exemplo | janela | dano/rodada | fatias | da Trilha |
|---|---|---|---|---|---|
| **posicionamento** | mover-se `+1,5 m` | permanente | `0,90` | **0,18** | 4% |
| | mover-se `+3 m` | permanente | `1,80` | **0,35** | 7% |
| **alvo** | o golpe simples pega 2 | 1× por descanso curto | `3,45` | 0,68 | 14% |
| | idem | permanente | `11,50` | 2,26 | 45% |
| **defesa** | `+1` de Defesa | quando você acerta | `1,70` | **0,33** | 7% |
| | `+1` de Defesa | permanente | `3,39` | 0,67 | 13% |
| **recuperação** | recuperar `+1` PE | 1× por descanso curto | `1,54` | **0,30** | 6% |
| | recuperar `+1` PE | permanente | `5,14` | 1,01 | 20% |
| **acerto** | `+1` no acerto das suas invocações | permanente | `5,40` | 1,06 | 21% |
| | `+1` no **seu** acerto | permanente | `10,80` | 2,13 | 43% |
| | trocar o fixo do acerto por atributo | permanente | `21,55` | 4,24 | **85%** |
| **economia de ação** | uma ação padrão a mais | permanente | `108,00` | 21,26 | **425%** |
| **soco** | o soco no nível 30 — `d10 + Força 6` | permanente | `11,50` | 2,26 | 45% |
| | ... disparado por *"quando você acerta"*, com dois ataques | `75%` | `8,62` | 1,70 | 34% |

**Os dois destacados estão na tabela para serem vistos, não comprados** — do jeito que estão escritos, permanentes, os dois estouram ou raspam o orçamento inteiro de uma Trilha numa entrega só.

> ## ⚠ E a rota que reprovava a ação a mais SOZINHA deixou de reprovar — achado na v0.74
>
> **A v0.70 fechou o piso de taxa de `20%` com este argumento:** *"com ele, uma ação a mais passa a custar `17` fatias contra um orçamento de `4` e reprova sozinha — a trava que hoje é escrita à mão cai da conta."*
>
> **A fatia quadruplicou depois disso, e o preço em dano por rodada não mudou.**
>
> | | espremida no piso de 20% | em fatias | do orçamento da Trilha |
> |---|---|---|---|
> | uma ação a mais, na escala `1,27` | `21,60` | 17,01 | **425%** |
> | uma ação a mais, na escala `5,08` | `21,60` | **4,25** | **85% — cabe** |
> | trocar o fixo, na escala `1,27` | `4,31` | 3,39 | 85% |
> | trocar o fixo, na escala `5,08` | `4,31` | **0,85** | **17% — cabe folgado** |
>
> **As duas ficaram quatro vezes mais baratas em relação ao orçamento**, porque o orçamento quadruplicou e elas não. *Ninguém decidiu isso; foi efeito colateral de dobrar a fatia duas vezes em dois dias.*
>
> **A decisão não muda, e o que se perdeu foi a segunda rota até ela.** A proibição de ação a mais continua escrita em dois lugares — a **peça 6 §3.1** reprova pelo **mecanismo** (*"ação a mais por rodada não tem conserto por preço"*), e a caixa da fatia no `RASCUNHO-trilhas.md` §3 repete. **Mas ela voltou a ser trava escrita à mão, e o texto tem de dizer isso** em vez de continuar prometendo que o preço resolve.

*Exceção estreita e paga na economia de ação continua existindo — é o que deixa uma Trilha conjurar na Reação, ou o Bastião socar como ação bônus. Como recurso de um Caminho específico, nunca como direito universal. **O que não cabe é ação inteira a mais.** A Melhoria Reação continua valendo o que vale.*

> **E "estreita" tem três formas, não duas.** *A terceira entrou na v0.74, e ela veio do `Engate` do `Punho`, que usava uma forma que esta seção não listava.*
>
> 1. **uma vez por cena** — o relógio segura;
> 2. **só com feitiço de Classe baixa** — a magnitude segura;
> 3. **presa a uma rolagem que você já ia fazer, e gastando um recurso do turno** — *"quando você acerta um ataque, dê um golpe desarmado como ação bônus"*. **Duas coisas seguram ao mesmo tempo:** o gatilho dispara em `50%` a `75%` das rodadas conforme quantos ataques você tem, e a ação bônus é um slot que o turno só tem um.
>
> **A terceira é a mais interativa das três, e é por isso que ela merece existir**: decidir gastar a ação bônus acontece toda rodada, enquanto um contador de cena dispara sozinho quando o jogador lembra dele.

### O que mexe em rolagem e não tem conversão entra com teto de maestria

Três famílias são legais e o projeto **não sabe preçar**: `auxílio` (somar à rolagem de outra pessoa), `rerrolação` (refazer um teste falhado) e `utilidade` (treino em perícia e em Teste de Resistência). Falta a conversão de dano causado por outro, e falta saber quantos Testes de Resistência uma luta tem.

> **Enquanto faltar, o tamanho delas nunca passa da maestria.**

**Isso não é preço — é garantia de que a coisa não deriva.** Maestria é o único número do sistema que cresce com nível, e ela cresce `+3`, que é o mesmo ritmo de quem está do outro lado da rolagem. Um teto em maestria é o único envelope de crescimento que esta peça pode dar sem uma conversão em mãos.

**E `trocar feitiço conhecido` fica de fora do teto, porque não tem magnitude.** Trocar um feitiço da sua lista por outro já é o menor tamanho que existe — pôr teto de maestria ali faria a entrega **crescer**, não encolher.

> *Esta família chamou-se `repertório` por algumas horas na v0.71, e a triagem matou o nome: **`Repertório` era a Trilha do Emanador.*** **O nome ficou LIVRE na v0.88**, quando a Trilha foi abandonada e o `Explosivo` entrou no lugar — *o argumento abaixo continua de pé por conta própria, e a colisão que o gerou não existe mais.* Uma palavra fazendo o trabalho de duas é o defeito que a v0.64 pagou para consertar, e ele reapareceu na peça que existe para cercar. **A família fica sem nome curto de propósito** — o que ela faz cabe em três palavras.

> **Quanto treino o Caminho dá é da peça 7, e só de lá** — duas perícias fixas e quatro à escolha, mais um ofício fixo e um livre. *Esta seção guardava a própria cópia desses números até a v0.71; ela saiu porque um número que mora em dois documentos vai divergir, e o `conferir-pericias.py` já confere as listas contra a peça dona.*

### O que saiu do permitido, e por quê

*Registrado para ninguém redescobrir. Nenhuma das quatro é decisão de gosto: as três primeiras têm número.*

| linha | o que aconteceu |
|---|---|
| **estender duração** | morreu na **v0.68** — `+1` rodada custa de `11` a `43` fatias conforme o comprimento do efeito, e não existe efeito curto o bastante para ela caber. *Continua valendo para aptidão, que tem orçamento de um marco inteiro* |
| **recuperar ferimento** | reprovou na **v0.70** — vale `0,00` para quem não cai, e o Bastião do nível 30 aguenta `11,7` rodadas contra uma luta de `3,7`. O eixo que decide quanto ela vale é **em quem o mestre resolve bater**, que é a mesma família de defeito que matou a Casca |
| **recuperar Integridade** | reprovou na **v0.70** — dano de alma esvazia as duas barras ao mesmo tempo, e **o corpo acaba antes em três das quatro fichas**. *Quando a Essência entrar na Integridade, esta linha pode voltar a valer* |
| **recuperar condição** | **liberada na v0.103**: a peça 19 dá nível a cada condição, e tirar uma custa `1` ponto de energia por nível |

### Os papéis moram na peça 6

**Bastião · Vanguarda · Guia · Emanador · Evocador**, cinco em vez dos quatro que ficavam aqui. *O quadro de rascunho foi para `99-arquivo/secoes-substituidas/`.*

Duas coisas dele sobreviveram e valem independente dos nomes:

**Nenhum Caminho cura.** Ele faz o efeito de cura de outra pessoa alcançar mais gente, durar mais ou chegar mais longe — a cura continua sendo Forma de feitiço.

**O Caminho de corpo é onde Força passa a valer.** É ele que transforma "aguentar e ser encarado" em função de equipe. Na v0.19 isso ganhou número: o Bastião tem d12 de vida contra o d6 do Emanador.

## 5. Em aberto

- ~~**Quantas Trilhas por Caminho**, e em que níveis elas abrem.~~ **Fechada na v0.55, na v0.60 e na v0.65:** uma Trilha por ficha, entregas nos níveis `2 · 11 · 19 · 27`, e degrau de Caminho em `2 · 7 · 15 · 30`. *O dono dos dois calendários é o `DESENHO-caminhos.md` da raiz, e a peça 6 §9 registra a mesma resposta.*
- ~~**A tabela de armas.** Quais dados, quais requisitos de Força, e se arma leve tem alguma compensação além do requisito baixo.~~ **Fechada na v0.48, na peça 14:** as 52 armas com dado e propriedades, e o requisito de `Força 3` nos dois degraus de cima de cada escada — dezesseis de 52. *A compensação da arma leve não é o requisito baixo: é a `Fineza`, que troca Força por Destreza no acerto **e** no dano do corpo a corpo.*
- ~~**Quanto custa uma ferramenta amaldiçoada que canaliza sozinha.** É a peça que faz o personagem sem energia existir, e ela precisa ser cara o suficiente para não virar o padrão.~~ **Fechada na v0.59, na peça 16 — e a resposta desarma a pergunta em vez de responder o preço.** Ela entrega **ferir maldição**, que é binário, e não entrega dano: fechar a distância até a Rotina no nível 30 pediria 95 de dano por rodada, que é o Fundamento inteiro e não um item. *Como ela entrega porta e não dano, **ela não pode virar o padrão do feiticeiro** — que já tem essa porta de graça pelo feitiço de Toque.*
- **Se o feitiço de Toque tem teto próprio.** Hoje ele herda o do Fundamento, e vale conferir no validador junto com os 35 feitiços prontos.
