# Changelog

Registro do que muda entre uma leva de material e a seguinte. Cada versão fecha quando o material daquela fase é revisado e aprovado.

Formato: `## [versão] — data` com as seções `Adicionado`, `Alterado`, `Removido` e `Decidido` (decisão de design que fecha uma pergunta em aberto).

---

## [0.41] — 2026-08-12

**Equipamento andou, e três coisas que já estavam escritas nela caíram.** Nenhuma peça nova e nenhum validador novo — continuam treze e treze. O que mudou foi o rascunho de Equipamento, de 160 para 487 linhas, e o `conferir-nomes.py`, que estava classificando colisão errado desde sempre.

### Achado — a conta do escudo comparava duas colunas em unidades diferentes

O §4 do rascunho derivou `escudo +1` pondo lado a lado *"+1 de proteção poupa X"* e *"duas mãos rende 2,0"*, e concluiu que a troca empatava no meio da campanha.

**A coluna do escudo estava certa.** `0,05 × CHEFE` é o valor de tirar 5 pontos percentuais da chance do inimigo, e o `CHEFE` do manual é dano **por acerto** — é assim que o `conferir-atributos.py:459` o usa, multiplicando por `0,5`.

**A coluna da arma não.** Os `+2` de dado são o ganho *quando você acerta*, num turno em que usa a arma. Por rodada vale `2,0 × 0,55 × quanto do tempo você dá golpe simples` — o `0,55` da peça 1 §6 mais o crítico da §5.2, e o teto de uso que o `conferir-orcamento.py` já mede. Refeita, a arma rende **0,66** e o escudo passa ela no **nv6**, não no nv16.

> **A unidade de um número se lê do uso, não do nome.** `CHEFE` parece dano por rodada e não é. Quem descobriu foi o validador que já usava o número certo.

### Achado — o escudo desligava cobrir-se, e isso o matava no primeiro marco

O §4 dizia *"o custo do escudo é a mão"*. A peça 11 §5 e §9 e a peça 8 dizem outra coisa, com todas as letras: **"uniforme, armadura e escudo desligam a proteção de energia"**.

| nv | refino | cobrir-se dá | escudo dá | o escudo vale |
|---|---|---|---|---|
| 2 | 1 | 1 | 1 | 0 |
| 6 | 3 | 2 | 1 | **−1** |
| 30 | 10 | 4 | 1 | **−3** |

Do refino 3 em diante pegar escudo **tira** Defesa. Refino 3 chega no nv6 em duas das três rotas. **A derivação inteira mediu contra um escudo que não entraria em ficha nenhuma.**

*É a armadilha de sempre, na direção menos vigiada: o preço usava um termo que existe, e ninguém tinha ido ler a regra pendurada nele.*

### Decidido — o escudo soma, e isso muda três documentos

A alternativa era manter o desligamento, e a conta mostrou que ela mata o item. Então **uniforme e armadura continuam desligando; o escudo passa a somar.**

> **A decisão está tomada e NÃO está aplicada, e isso é de propósito.** A frase mora em três lugares — peça 8 passo 7, peça 11 §5 e peça 11 §9 — e as três só mudam quando Equipamento fechar, junto com a outra dívida que a peça 11 já devia (*"você fica sem a proteção passiva"* virando *"você fica sem proteção"*). Mexer nas duas de uma vez evita tocar duas vezes na mesma peça fechada.
>
> **Fica registrado em quatro lugares porque decisão que termina em "corrigir em três documentos" é exatamente a que o projeto já perdeu sete versões:** aqui, no §7 do rascunho, na seção nova do `ESTADO-ATUAL`, e como checagem obrigatória do validador da peça, no item 9 do §8. *Se a próxima passada fechar a peça sem mexer nos três, o validador tem que falhar.*

**E abriu um buraco que precisou de conserto na mesma passada:** com o escudo somando, `cobrir-se refino 10 + escudo` dá Defesa **21** e fura o teto de 20 que o §3 tinha fixado. Foi a decisão que abriu, e é ela que fecha.

### Decidido — RD foi levantada, medida, e morta pelo critério e não pela conta

A conta apontava para ela: `RD fixa` é a única forma que fica na mesma escala do dado da arma — erra por fator constante (1,5×) em todo nível, contra o fator crescente da proteção (0,5× a 5,5×).

> **Decisão do Mizuki: não.** *"Dar RD nunca é solução, pode acabar vindo a virar mais um cálculo e ninguém quer isso."*

**Fica registrado porque a conta e o critério discordaram, e o critério ganhou.** A conta mede valor por rodada; ela não mede quanto uma subtração a mais custa em tempo de mesa. **Esse eixo não tem validador, e não vai ter.** Sem o registro, alguém reabre a ideia daqui a dez versões achando que ninguém tinha feito a conta.

### Decidido — a escada de escudos, e ela sai de duas linhas que já estavam escritas

A saída estava na própria peça, em dois lugares que ninguém tinha juntado: o §3 fechou dizendo que **as duas rotas topam em Defesa 20**, contando o escudo dentro disso, e o §2 já tinha adotado a régua do 3.x — ***"proteção e teto de Destreza são um orçamento só"***.

**O escudo maior não cresce por cima do teto: ele cresce comendo teto de Destreza**, igual ao Revestimento. E aí vira o prêmio da build de Força sozinho, sem regra nova, porque quem tem Destreza baixa não perde nada com o teto.

| degrau | proteção | teto de Destreza | requer Força | custa marco? |
|---|---|---|---|---|
| 1 | 1 | 5 | — | não |
| 2 | 2 | 3 | 3 | não — cabe na criação |
| 3 | 3 | 1 | **5** | **sim, 2 pontos** |

**O degrau 3 é o primeiro item do catálogo inteiro que cobra ponto de marco** — toda arma pede no máximo Força 3, que é o teto da criação. É o trabalho novo que a peça 1 pedia desde a v0.24, com *"Força tem uma perícia só"*.

Busca exaustiva de uniforme × escudo × Destreza: **nada passa de 20, e 20 é alcançado por duas rotas** — o teto não é decorativo. Nenhum dos três degraus é dominado, e o cruzamento entre o 1 e o 3 cai em **Destreza 3**, o mesmo ponto de Traje contra Revestimento. Uma régua, dois lugares.

### Registrado — e ela não conserta a arma de duas mãos, que é o que motivou tudo

| nv | o degrau 3 poupa | a Pesada rende | razão |
|---|---|---|---|
| 6 | 2,58 | 0,66 | 4× |
| 30 | 10,80 | 0,66 | **16×** |

Proteção escala, dado não. **Isso não tem conserto dentro desta peça, e provavelmente não deveria ter:** a régua do §5 diz que *"a arma dá acesso e restrição; o Caminho dá o que você faz com ela"*. Duas mãos é acesso à árvore que exige duas mãos, e é a Trilha da Vanguarda que dá razão para largar o escudo — por isso ela vem depois na fila da v0.36.

**O alvo fica registrado para quando aquela peça chegar: 6% a 9% da Rotina, e a fração quase não deriva.** Não pode ser pago em dado de dano.

### Achado — o item 1 de Equipamento fechou, e o argumento que ia salvá-lo era desnecessário

*"A Pesada paga dois pontos de Força a mais que a Uma mão pelo mesmo valor líquido"*, e o argumento registrado era que o requisito é **compartilhado com o Revestimento**.

**Ele nem precisa disso: o requisito é grátis.** A Pesada pede Força 3, e 3 é o teto da criação (peça 2 §2). **Nenhuma classe do catálogo custa ponto de atributo** — o requisito de arma resolve acesso, que é o que a peça 5 §1 já tinha concluído.

**E o furo do teste era um nível acima do que a linha dizia.** Não é só que a matriz não somava o total: é que ela roda **uma vez só**. Enquanto o escudo desligava cobrir-se, existiam duas populações com dominâncias opostas — ficha de uniforme e ficha de cobrir-se —, e rodada uma vez ela cancelava as duas e saía verde. O validador precisa rodar **uma vez por rota de proteção**.

### Achado — `Uma mão` está dominada pela `Versátil`, e nenhum par de dados conserta

Mesmo dado, mesma mão livre, uma propriedade a mais, e o ponto de Força a mais não custa nada. O §5 afirmava *"zero classes dominadas"* — verdade com o requisito valendo como custo, falso sem ele.

Testados `d8/d10`, `d8/d12` e `d6/d10` para a Versátil: **em nenhum largar o escudo compensa**, porque o ganho de dado é 0,33 a 0,66 contra os 2,01 do escudo no nv16. O par de dados só vira escolha de sabor depois que a forma do escudo fechar.

### Corrigido — a triagem de nomes classificava três coisas diferentes com a mesma palavra

*Este é o conserto que mais vai render, porque ele estava enviesando decisão de nome desde que a triagem existe.*

O `conferir-nomes.py` marcava `OCUPADO` tanto para colisão exata quanto para **substring dentro de um termo composto**. As duas não são a mesma coisa.

> **Critério do Mizuki:** *"não precisa ligar tanto para nomes conjuntos, como Melhoria 'rasga escudo' a 'lança negra'. Se preocupe mais quando o nome bater de frente com o nome de algo que é **realmente** aquilo."*

A saída agora separa:

| grau | significa | mata? |
|---|---|---|
| `OCUPADO` | o **nome inteiro** já é termo definido | sim |
| `DENTRO` | aparece **dentro de um termo composto** | **não** — vá ler o termo e pergunte se ele *é* aquilo |
| `fraco` | fica a uma letra | não, mas confunde em voz alta |

**O custo de errar isso já tinha sido pago e ninguém percebeu:** `Lança` morreu na triagem por estar dentro de **Lança Negra**, e a arma entrou na classe Haste como **Yari** — que é exatamente uma lança, com o nome em japonês. **O sistema contornou um nome que nunca esteve ocupado.**

Quatro voltaram: `Lança`, `Escudo`, `Faca` e `Lastro`. Continuam mortos, por nome inteiro ou por sentido: `Chicote`, `Guarda`, `Anteparo`, `Bloqueio`, `Proteção`, `Carapaça`. **O catálogo foi de 39 para 41 armas.**

*Três contra-testes:* `Escudo` e `Lança` passaram de `OCUPADO` para `DENTRO`; `Toque`, que é Forma no manual **e** aparece em composto, continua `OCUPADO`, o que prova a prioridade do grau duro; e perturbando a linha que classifica, `Escudo` cai para `LIVRE`, o que prova que é ela que decide.

### Decidido — `Alcance` e `Distância` ficam, com o motivo escrito

As duas saem `OCUPADO` de verdade — `Alcance` é Família **e** Melhoria no manual, `Distância` é Tema — e as duas estão em uso como propriedade de arma.

**A colisão é de camada, não de sentido:** no manual descrevem o que um *feitiço* faz; na tabela descrevem o que um *objeto* é. Nenhuma regra pendura efeito nos dois ao mesmo tempo. Entram no validador da peça como `ACEITA`, no formato que os rótulos de rascunho da peça 6 já usam.

### Adicionado — a seção de itens comuns, em três camadas

*Pedida pelo Mizuki. A moeda ficou de fora de propósito — "provavelmente vai ser com preço e fornecimento".*

**A regra que abre a seção sai da conta: item comum não produz número.** Um item de +1 vale **33% de tudo que um atributo cresce em 28 níveis**, e com 5 a 7 mestres isso compõe — se cada um entregar um por arco, na terceira mesa o jogador ganhou de graça a campanha inteira, sem passar por marco, XP ou validador. **É o filtro multi-mestre falhando pelo lado que ninguém vigia: não é arbitragem divergente, é acúmulo invisível.**

E os quatro eixos óbvios já têm dono: proteção bate no teto de Defesa, cura bate em três decisões, dado de dano bate na Rotina, PE bate no `conferir-orcamento`.

| camada | o que é | o limite, e de onde ele sai |
|---|---|---|
| **1 · Permissão** | move de *não rola* para *rola sem maestria* | passa na lição nº 1 porque não empilha, não deriva (a CD de perícia é fixa) e não entra em rolagem disputada. **Item abre a porta, treino atravessa bem** |
| **2 · Consumível** | gasta e some, então não compõe entre mesas | **um a dois por missão.** De três em diante ele cobre as três lutas de graça da peça 10 e vira a resposta padrão — é o teste do bônus automático aplicado a item |
| **3 · Espaço** | inventário em slots | **desligada**, com gatilho escrito: *se o playtest mostrar que o grupo leva tudo sem escolher, o espaço entra* |

*Levantamento externo por trás disso:* cinco sistemas com o modo de falha de cada um — o *Christmas tree* do 3.5, a lista que ninguém lê do 5e, o `load` discricionário do Blades, o Tetris do Torchbearer e a economia de crafting que o alquímico do PF2e exige por baixo.

**E a ficção ajuda menos do que parecia.** Procurando o que um feiticeiro de JJK carrega além de ferramenta amaldiçoada, **não achei lastro** — a obra tem ferramenta e objeto amaldiçoado, e quase nenhum item mundano com peso de cena. O que tem lastro já está escrito nos ofícios: Herbalismo, Caligrafia, Forja, Entalhador dizem **quem fabrica**; falta dizer **o que sai**.

### Corrigido — o README contava quinze validadores e o `subir.sh` roda dezesseis

Achado na primeira leitura desta sessão, e ele é da mesma família do resto: `quinze` era o número certo com **doze** peças. A v0.39 subiu para treze e essa linha ficou.

```
13 de 03-mecanica/  +  conferir-repositorio.py  +  pac7.py  +  v7.py  =  16
```

**E o `conferir-repositorio.py` não alcança essa frase.** Ele confere as três linhas que contam peças e validadores, e não a prosa que diz quantos o script roda. *Número sem dono, errado desde a v0.39.*

### Em aberto

- **As sete propriedades de arma sem texto** — e essa é a dependência dura: enquanto forem só nome na tabela, 15 dos 16 pares da matriz saem `INCONCLUSIVO`, `Haste` e `Tiro pesado` ficam a 0,60 de estarem dominadas pela `Pesada`, e **o validador da peça não pode ser escrito**.
- **O teto de Defesa 20 não tem dono declarado.** O §3 derivou dele e agora a escada de escudos se apoia nele. Derivação virou invariante sem ninguém decidir — a lição nº 9 entrando pela porta de trás. Ou a peça 1 adota, ou Equipamento declara que é dona.
- **Os nomes dos três degraus de escudo.** Livres: Broquel, Pavês, Rodela, Adarga, Tarja, Couraça, Guarda-Corpo.
- **A lista de itens comuns**, e a moeda.
- **As quatro vagas de Desliga da peça 13** que esperam esta peça.
- **A Cicatriz não tem mecânica, só nome.**
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.40] — 2026-08-12

**Nenhuma regra e nenhum número de jogo mudaram.** Passada de documentação, feita na migração de conta e antes de abrir a peça de Equipamento. Ela existe porque três coisas que a documentação afirmava tinham deixado de ser verdade — e uma delas ensinava a confiar num verde que não confere nada.

### Achado — o "4, 2 e 1" estava errado, e errado para o lado que engana

A v0.38 mediu quantas checagens cada validador pula sem `python-docx` e registrou **4, 2 e 1**. O `README`, o `ESTADO-ATUAL`, o `LEIA-ME` e o `PROMPT-CHAT-NOVO` repetiram. **Lido do código:**

| validador | documentado | é | de quantas |
|---|---|---|---|
| `conferir-nomes.py` | 4 | **3** (checagens 1, 3 e 4) | 5 |
| `conferir-manual.py` | **2** | **4 — todas** | 4 |
| `conferir-pericias.py` | 1 | 1 ✓ | 8 |

**O `conferir-manual.py` estava escrito como o que pula menos e é o único que não confere absolutamente nada:** ele dá `sys.exit(0)` dentro do `except ImportError`, antes da primeira checagem. Quem lesse "pula 2 de 4" ia supor que sobrou metade da cobertura. Sobra zero.

**A causa é de método, e é o que vale guardar:** o 4 do `conferir-nomes` é a contagem da palavra `PULADA` na saída — ele imprime uma linha de resumo e mais três marcadores inline, e a linha de resumo foi contada como se fosse uma quarta checagem. **O número foi tirado da saída do programa em vez do código.** O do `conferir-manual` não bate com nenhuma das duas leituras.

> **Contar sintoma não é contar causa.** A saída de um validador é feita para ser lida por gente no meio do trabalho, não para ser fonte de número que vai para documento. Quando o número for sobre o comportamento do validador, ele se lê do validador.

*Achado rodando o controle negativo com o import bloqueado — a mesma prática que a v0.28 pagou para aprender e que a v0.33 institucionalizou.* A checagem que ninguém tinha feito era a segunda metade dela: **conferir que o número que a gente escreveu sobre a pulada bate com a pulada.**

### Alterado — o `ESTADO-ATUAL` e o `README` estavam parados na v0.38

A v0.39 subiu as contagens (`treze peças e treze validadores`) e a entrada do CHANGELOG, e o `conferir-repositorio.py` passou — porque ele confere **a contagem escrita contra a pasta**, e ela estava certa. O que ele não confere é se as listas e as seções em prosa acompanharam. Não acompanharam:

| onde | dizia | é |
|---|---|---|
| `ESTADO-ATUAL`, cabeçalho | *"na v0.38"* | v0.40 |
| `ESTADO-ATUAL` e `README`, lista de comandos | doze validadores | **falta o `conferir-legados.py`** nas duas |
| `ESTADO-ATUAL` | *"o décimo primeiro é de outra natureza"* · *"os dois últimos precisam de `python-docx`"* | são **três** naturezas fora da regra, e **três** precisam da biblioteca — e não são os últimos |
| `ESTADO-ATUAL` e `LEIA-ME` | *"as seis skills"* | **sete** |
| `README`, a árvore | doze peças · doze validadores · seis skills | treze · treze · sete |
| `ESTADO-ATUAL`, problema de design nº 1 | o teto de magnitude do Legado, aberto | **fechado na v0.39** |
| `ESTADO-ATUAL`, a fila da v0.36 | Legados na frente, por escrever | fechada, e Equipamento é a próxima |
| `ESTADO-ATUAL`, Corpo Amaldiçoado | *"falta aplicar na peça 9 §5"* | aplicado na v0.39 |

**A peça de Legados ganhou seção nova no `ESTADO-ATUAL`**, no lugar do alerta que pedia a régua: os três formatos, os dois Legados por ficha com Destranca obrigatório, e a tabela do que ficou pendurado — **sete vagas de Desliga, quatro esperando equipamento e três esperando dano e condições**, mais a `Armaria` e o `Enterrado`, que citam ferramenta amaldiçoada e são as primeiras a reler quando a próxima peça sair.

### Alterado — a contagem de versões sem playtest saiu de todos os documentos

*A v0.38 deixou isto anotado em aberto e escreveu o conserto certo: **"é derivável da versão atual e não devia estar escrita à mão em lugar nenhum."*** Estava em cinco lugares com dois valores — `README` 35 e 32, `ESTADO-ATUAL` 35 e 32, `LEIA-ME` 35.

Virou **"zero sessões desde a v0.1"** nos três. É a mesma informação, não envelhece, e ninguém precisa lembrar de somar um a cada versão. O `README` também dizia *"38 versões de argumento"*, pelo mesmo motivo e com o mesmo conserto.

E de passagem: o `README` ainda dizia que **`04-playtest/` e `05-material/` estão as duas vazias.** A ficha saiu na v0.35 e o gerador dela está lá — vazia é só uma.

### Registrado — as cinco skills instaladas estavam todas atrás da pasta

A migração de conta obrigou a reinstalar as sete de `sistema/skills/`. **Duas não estavam instaladas** — `gasto-de-modelo` e `pesquisa-antes-de-propor` — e **as cinco que estavam divergiam da cópia do repositório, todas.**

A pior era a `rpg-da-guilda`: a versão instalada ainda mandava rodar de `03-mecanica/` *"porque de outro lugar eles pulam checagem em silêncio"* — **o aviso que a v0.38 saiu para aposentar.**

> **E a deriva inverteu de direção.** Na v0.37 o repositório é que estava atrás, e a conclusão registrada foi *"migrar pelo repositório levaria o gatilho velho"*. Desta vez foi o contrário, nas cinco. **Não existe lado confiável por natureza** — existe a data da última sincronização, e ela não está escrita em lugar nenhum. Continua sendo a camada que nenhum validador alcança.

### Em aberto

- **Equipamento**, a próxima peça — e a proteção primeiro, porque é a que já tem teto fixado por fora: `1` no nível 2 e `4` no refino 10, e uniforme desliga cobrir-se de energia.
- **As sete vagas de Desliga** e o **Não Sou Gente** virando Passiva.
- **A máquina de criação do Sem Técnica** — Aptidão e Estilo da Sombra.
- **A Cicatriz não tem mecânica, só nome.**
- **Uma checagem que conte skill**, que a v0.38 já tinha marcado como candidata e que esta versão acabou de justificar de novo.
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.39] — 2026-08-12

**A peça 13 fechou.** Legados sai de rascunho e vira peça numerada, com validador junto — **treze peças e treze validadores**. O catálogo tem **81 entradas** contra as catorze de antes, e as quatro que a régua tinha reprovado saíram todas, cada uma com destino escrito.

### Adicionado — `13-legados.md`, as sete listas de Origem

| Origem | Destranca | Ajusta | Desliga escrito | reservado |
|---|---|---|---|---|
| Latente | 4 | 4 | 2 | — |
| Receptáculo | 4 | 4 | 1 | 1 |
| Descendente | 5 | 4 | 1 | 1 |
| Reencarnado | 4 | 4 | 0 | 2 |
| Corpo Amaldiçoado | 4 | **12** | 1 | 1 |
| Feto | 4 | 4 | 1 | 1 |
| Restrição Celestial | **8** | **8** | 1 | 1 |
| | **33** | **40** | **7** | **7** |

Mais o **`Sem Técnica`**, escrito uma vez e compartilhado pelas cinco Origens que o aceitam. **Oitenta e uma.**

### Decidido — o Desliga virou cota de dois, com vaga declarada

*A régua dizia "até 2, teto e não cota", e o Receptáculo e o Descendente fecharam em um por causa disso.* O Mizuki decidiu o contrário: **toda Origem termina com dois Desliga.**

**A conta não fecha hoje, e é por isso que a vaga existe.** Dois por Origem em sete são catorze; a enumeração de alvos legais tem **sete no sistema inteiro, e o `Ferro Velho` gastou o último**. Então: **o Desliga que tem alvo se escreve, o que não tem vira vaga declarada** — e a vaga **nomeia a peça de onde o alvo deve sair**, aparece na tabela junto dos outros, e o validador confere que ela está marcada em vez de conferir que a lista está cheia.

> **Inventar oito alvos agora seria escrever entrada para fechar contagem — que é exatamente o defeito que esta régua nasceu para achar.** Os três Desliga de condição da v0.37 foram escritos porque a coluna pedia, e cada um apagava Condição Maior, que custa Pesada.

**Sete vagas abertas:** quatro esperam **equipamento**, três esperam **dano e condições**.

### Decidido — dois tipos de Destranca, e o mais velho já estava em uso

A cláusula dizia que **todo** Destranca precisa de gatilho que o jogador puxa. A lista do Corpo Amaldiçoado bateu nisso — as quatro configurações de núcleo são identidade, não ação —, e aí apareceu que **o `Sem Patente` do Latente já era assim desde a primeira lista** e passou sem ninguém reparar.

| tipo | o gatilho é |
|---|---|
| **de ação** | uma coisa que o jogador faz, quando quer |
| **de identidade** | a própria escolha, feita uma vez na criação |

**O que segura o segundo tipo é o teste dos 90%, sozinho:** ninguém deixa em branco a linha que diz o que ele é. E a diferença para o **Irmãos**, que a cláusula existia para pegar: *identidade o jogador escolheu; o Irmãos foi escolhido por ele.*

**E um Destranca de identidade não pendura tarefa.** A primeira leva do Corpo Amaldiçoado foi reprovada pelo Mizuki por isso — *"aponte e diga qual das três teria sabido"*, *"escreva três pessoas que só conhecem ela"*, e a pior: *"quem estuda o assunto vai querer saber como"*, que é **enredo tirado do mestre sem ele ter pedido**.

### Achado — o canon reescreveu duas Origens e matou um Legado

**Corpo Amaldiçoado tem energia amaldiçoada.** O `ESTADO-ATUAL` punha ele no mesmo balde da Maki — *"não têm energia, então não têm aptidão nem refino"*. **Cadáver de mutação abrupta produz a própria energia**, uns três meses depois de acordar; o que falta é **técnica**. Ele é misto: **PE, aptidões e refino normais, e Técnica Marcial no lugar do Fundamento.** As Bênçãos e a Lapidação ficam só com a Maki, que é a única de energia zero.

**E os três núcleos não são sabor: são a receita.** Três almas compatíveis num corpo, obrigadas a se observarem, é o que produz autoconsciência e energia própria. Mas **não é a única configuração possível** — cadáver operado por um feiticeiro e cadáver mantido pelo criador também existem. A lista virou quatro configurações — **Ninhada, Gêmeos, Inteiro, Manutenção** —, três com energia própria e uma dependente, e **cada uma gateia três Ajusta próprios**.

**O `Alcance Impossível` morreu.** *"Aja de um lugar em que o seu corpo não está"* é **técnica** — é o que a Manipulação de Fantoche faz —, e a peça 9 proíbe Origem de conceder técnica. Mesmo diagnóstico do `Núcleos` e do `Não Sou Gente`: **não é Legado, é kit de poder.** O que sobrou dele virou o `Nunca Estive Lá` e o `Do Meu Canto`, que são conhecimento e posição, não alcance.

**E o Mechamaru é o boneco.** A peça 9 atribuía a ele a pele que não aguenta sol e os membros que faltam — isso é do **Kokichi Muta**, a pessoa. Corrigido nos dois documentos.

### Achado — a irmandade do Feto é definida por quem te fez

*O `Irmãos` era o piso do catálogo desde a v0.24: o jogador não conseguia disparar, e o efeito era simétrico.* **O conserto não foi inventar gatilho — foi ler o que a irmandade é.** No material, o reconhecimento de irmão **não depende de o outro ser da mesma fabricação**: o mais velho reconheceu como irmão alguém nascido de gente, porque quem os fez foi o mesmo.

> **O gatilho virou o jogador apontar alguém e dizer que é irmão.**

E isso conserta a premissa da Origem junto: *"nem todo Feto é Pintura da Morte"* estava certo e apoiado em nada — **não existe outra categoria de pessoa meio-humana e meio-maldição.** O que existe com nome parecido é **maldição imatura em estágio de útero**, que não é gente e não vira gente. A Origem é *"alguém te fabricou de propósito"*, e Pintura da Morte é o exemplar famoso.

### Decidido — Sem Técnica entra como ponteiro, e precisa de máquina de criação

**Ela não cabe como entrada de catálogo** — tem construção própria em cima —, **e também não pode ficar invisível na camada onde o jogador escolhe quem é.** Entra como **uma entrada de `Destranca` que aponta para fora**, disponível nas cinco Origens que aceitam a sub-origem, **escrita uma vez e referenciada pelas cinco**. Cinco cópias do mesmo texto seria a lição nº 9 dentro de um catálogo.

**E a rota precisa de máquina de criação própria.** Se for só subtração — os outros menos o Fundamento —, ninguém escolhe por vontade: escolhe por castigo.

*O que ela não precisa é de uma economia nova.* **Energia Reversa não é técnica inata**, é manipulação de energia amaldiçoada — e é por isso que quem não tem técnica consegue usar. E o **Estilo da Sombra é anti-domínio, com a espada sendo o jeito mais comum e não o requisito**: a técnica central dele foi aprendida em um mês por quem não usa espada, e a **seção 6.5 da peça 11 já trata o Domínio Simples como aptidão pura**. *A mecânica do projeto estava certa e a prosa da peça 9 estava mais estreita que ela.*

**De 81 entradas, exatamente uma quebra com Sem Técnica:** o `Inédito`, que fala da *sua* técnica. Virou a checagem 9 do validador.

### Adicionado — `conferir-legados.py`, o décimo terceiro validador

Nove checagens, e **nada de valor escrito dentro dele**: os quatro degraus saem da **peça 10**, as Origens saem da **peça 9**, e as contagens saem da própria pasta. O único bloco na mão é o `LIMITES DE DESIGN`, declarado à parte da regra aplicada — lição nº 8. **Não lê o `.docx` e não precisa de `python-docx`**, então não existe caminho por onde ele saia verde tendo pulado checagem.

A checagem 9 é a que mais vai render: **ela recalcula a tabela de totais da peça e falha se o escrito não bater com o contado.** As contas do rascunho já tinham envelhecido duas vezes dentro do próprio arquivo.

**Nove perturbações conferidas, cada uma acendendo a checagem certa** — numa cópia isolada, com a base conferida verde antes e o `diff` conferido em cada uma. Duas não provaram nada na primeira rodada e as duas foram consertadas: um `sed` que não bateu, e a checagem 8, que **acendeu a checagem errada porque estava frouxa** — ela aceitava a palavra *"especiais"* em qualquer lugar da seção. Agora exige as cinco elegíveis nomeadas **e** as duas especiais excluídas.

**E o contra-teste:** renomear um degrau **dentro da peça 10** acende a checagem 2. É a prova de que ele lê do dono em vez de guardar a escada.

### Alterado — o que a peça 13 obrigou a mexer em volta

| arquivo | o que mudou |
|---|---|
| `09-origens.md` | dois Legados; as sete listas viraram ponteiro para a peça 13; Corpo Amaldiçoado ganhou energia; Kokichi no lugar de Mechamaru; Sem Técnica reescrito; a pendência *"se um Legado é pouco"* fechada |
| `08-criacao-de-personagem.md` | dois Legados nos dois lugares, e a Kaori ganhou o segundo |
| `gerador-ficha/ficha.js` e `make.js` | campo do segundo Legado na página 3 |

> **O `.docx` da ficha ficou para trás do código** e precisa ser regerado com `node make.js`. O `conferir-ficha.py` não acusa porque ele confere as constantes de nível 2, e nenhuma delas mudou.

### Em aberto

- **As sete vagas de Desliga**, quando equipamento e dano-e-condições saírem.
- **A máquina de criação do Sem Técnica** — Aptidão e Estilo da Sombra.
- **A Cicatriz não tem mecânica, só nome.**
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Equipamento**, que é a próxima peça da fila.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.38] — 2026-08-12

**Nenhuma regra e nenhum número mudaram.** Esta versão mexe só na camada de procedimento, e ela existe porque a migração de conta obrigou a reler o que a documentação afirma — e duas coisas que ela afirmava tinham deixado de ser verdade.

### Adicionado — a skill `pesquisa-antes-de-propor`

O Mizuki nomeou o defeito: *"toda vez que vou dar continuidade, a primeira coisa é ir no achismo ou com as informações que temos, e poucas vezes é feita busca real na internet, fóruns e afins, a não ser que eu peça."*

**E a instrução já existia.** A `rpg-da-guilda` diz *"pesquise antes de inventar"* — no item 8, sexto bullet de uma lista de sete. Ela nunca disparou.

> **Lembrete enterrado numa lista não é procedimento. Gatilho é.**

A skill nova troca o bullet por **sete casos em que a busca é obrigatória antes de entregar**: afirmar o que outro sistema faz, atribuir modo de falha documentado, afirmar canon, afirmar comportamento de ferramenta, adotar nome novo, dizer que *"ninguém resolve isso"*, e contornar duas vezes o mesmo defeito de ambiente.

**E ela traz a metade que ninguém escreve — o que *não* se pesquisa fora.** Número que um documento do projeto é dono se lê do dono; buscar fora cria a segunda fonte para o mesmo número, que é a lição nº 9 entrando por outra porta. Conta que dá para rodar se roda. Escolha de sabor é do Mizuki, e nenhuma fonte externa decide por ele.

*Escrita depois de rodar a própria receita:* o levantamento de onde procurar por domínio saiu de busca real, e a hierarquia de canon — obra original, depois material oficial complementar, e wiki de fã como **índice e não autoridade** — é a que a preferência de pesquisa dele já pedia, com a checagem de mudança de status junto.

### Achado — o aviso do diretório parou de reproduzir, e ninguém tinha voltado para olhar

O `README` e o `LEIA-ME` diziam, desde a v0.28, que os três validadores que leem o `.docx` o acham *"por caminho relativo à própria posição"* e que, rodados de outro lugar, **pulam checagem em silêncio**. A v0.33 mediu e registrou: **4, 1 e 1 puladas de `/tmp`.**

**Hoje é zero.** Medido nesta versão:

| | de `03-mecanica/` | de `/tmp` |
|---|---|---|
| `conferir-nomes.py` | 61 linhas, 0 pulada | **61 linhas, 0 pulada** |
| `conferir-manual.py` | 94 linhas, 0 pulada | **94 linhas, 0 pulada** |
| `conferir-pericias.py` | 120 linhas, 0 pulada | **120 linhas, 0 pulada** |

Os quatro validadores que abrem arquivo do manual resolvem por `os.path.dirname(os.path.abspath(__file__))`, e **nenhum `conferir-*.py` tem caminho relativo cru**. O conserto entrou em alguma refatoração e nunca foi registrado — então o aviso sobreviveu à causa dele.

**A instrução fica, o motivo muda.** Rodar de `03-mecanica/` continua sendo o certo, porque é o que o `subir.sh` faz e o que o resto da documentação supõe. O que saiu dos três documentos e da skill é a justificativa errada.

> **Aviso que parou de reproduzir é dívida, e é pior que aviso nenhum:** ele ensina a procurar o defeito no lugar em que ele não está mais. Entrou na lista de armadilhas recorrentes da `rpg-da-guilda`.

### Confirmado — a outra pulada é real, e essa fica

Bloqueando o import de `docx` de propósito, os três saem **verdes, com código 0**, e pulam:

| validador | checagens puladas sem `python-docx` |
|---|---|
| `conferir-nomes.py` | **4** |
| `conferir-manual.py` | **2** |
| `conferir-pericias.py` | **1** |

O `conferir-ficha.py` não entra: ele lê o `.docx` com `zipfile`, da biblioteca padrão, desde a v0.35 — não tem dependência para faltar. **`PULADA=0` continua sendo a checagem que vale antes de confiar num "OK".**

### Alterado — a contagem de skills estava parada em quatro

O `README` e o `LEIA-ME` diziam *"as quatro skills"* enquanto o `ESTADO-ATUAL` dizia cinco, desde que a `rpg-da-guilda` entrou na v0.37. **Três documentos, dois números.** Agora são **seis**, e os três dizem seis — divididas em **duas de procedimento** (`rpg-da-guilda`, `pesquisa-antes-de-propor`) e **quatro de assunto**.

*É a lição nº 9 na camada que o `conferir-repositorio.py` não alcança* — ele confere versão do projeto, versão do manual, peças e validadores, e não conta skill. Fica anotado como candidato a checagem, junto com a divergência entre a pasta e a skill instalada que a v0.37 achou.

### Registrado — três contas do `RASCUNHO-legados-regua.md` envelheceram dentro do próprio arquivo

Nada disso muda a régua, que continua fechada. São as contas de fechamento, que ficaram para trás quando a seção 8 decidiu **dez por Origem** depois das listas já estarem escritas:

| onde | diz | é |
|---|---|---|
| §9, abertura | *"primeira leva, com cinco entradas cada"* | Latente 10, Descendente 10 |
| §9, fecho do Latente | *"quatro Destranca · três Ajusta · três Desliga"* | **4 · 4 · 2** — o `Desconfiado` virou Ajusta e o fecho não acompanhou |
| §9, conta final | *"Ajusta 8 · Desliga 4 · Destranca 8"* | **16 · 4 · 14** |
| §10, primeiro item | *"cinco por Origem"* | dez, pela seção 8 |

**A entrada da v0.37 está certa** — ela registra `Latente (10), Receptáculo (9), Descendente (10) e Reencarnado (5)`, que é o que a pasta tem. Quem derivou foi o rascunho contra si mesmo. **Corrigir junto com a outra metade**, para não mexer duas vezes no mesmo arquivo.

### Em aberto

- **O catálogo dos Legados**, três Origens inteiras — Feto, Corpo Amaldiçoado e Restrição Celestial — e o que falta no Reencarnado, que tem 5 de 10 e um Destranca só. **As quatro contas de fechamento acima entram nesse mesmo passe.**
- **Não Sou Gente** é imunidade a dano e a régua reprova; a saída registrada é virar Passiva paga com espaço de feitiço. **Irmãos** é o piso do catálogo e precisa de gatilho do jogador.
- **O validador dos Legados**, que sai junto com a peça — e sobe peças e validadores de doze para treze nos três documentos de uma vez.
- **A Cicatriz não tem mecânica, só nome** — o conteúdo dela é da peça de dano e condições, que não existe.
- **A mudança de um para dois Legados** ainda não chegou na peça 8, na peça 9, no gerador da ficha nem nos dois validadores da ficha.
- **A contagem de versões sem playtest diverge em três lugares** — o `README` diz 32, o `ESTADO-ATUAL` diz 35 num ponto e 32 em outro, o `LEIA-ME` diz 35. É derivável da versão atual e não devia estar escrita à mão em lugar nenhum.
- **A lista de feitos do limiar do nível 20** e a conversão de mestragem.
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.37] — 2026-08-12

**A pergunta nº 5 do `pitch-de-design.md` fechou.** Ela estava aberta desde a v0.1: *"como o sistema trata morte? JJK é letal; server de guilda com personagem persistente normalmente não é."* Metade dela já tinha resposta e ninguém tinha reparado que era só metade.

### Decidido — o Caído, e o corte entre o que é do mestre e o que é do sistema

| | quem decide |
|---|---|
| **o registro** — a morte cola nesta mesa? | **o mestre**, na abertura. É a trava 6 do `arquitetura.md`, e ela fica como está |
| **a máquina de estado** — o que acontece a 0 de vida | **o sistema.** Zero ocorrências no projeto e no manual antes desta versão |

O corte não foi inventado: o próprio esqueleto justifica a trava 6 dizendo que *"o filtro existe para impedir discricionariedade **nos números**; na ficção é trabalho do mestre"*. **Cair a 0 é número** — muda se você continua com o personagem —, então o registro fica por mesa e a máquina de estado é igual em todas.

> **A 0 de vida você escolhe:** **Aguentar** (apaga, janela de 3 rodadas, cura de 1 te levanta) ou **Insistir** (fica de pé, e cada rodada custa **1/8, depois 1/4, depois 1/2** da vida máxima).
> **Quem levanta ganha uma Sequela**, que encurta a janela da próxima queda. **Na segunda queda vem uma Cicatriz**, permanente.
> **A janela acabou:** estágio 4 de dano de alma.

### Achado — o estado terminal já estava escrito, e era inalcançável

O manual tem quatro estágios de dano de alma, e o quarto diz ***"você não é mais você; o que sobra é decisão do mestre"***. **Isso é a trava 6 com outras palavras**, e ninguém nunca chegou nele: a peça 1 registra que a alma é maior que o corpo em quatro dos cinco Caminhos, então *"a pessoa cai antes"*. Ligar o fim da janela ao estágio 4 destravou a máquina que já existia, sem estado novo e sem contador novo.

### Por que fração da máxima, e não o dano que entra

A versão óbvia — o dano continuar entrando, só que na vida máxima — quebra, porque **vida máxima é justamente o eixo em que os Caminhos divergem 3,2×**:

| perfil | rodadas de pé, se o custo fosse o dano que entra |
|---|---|
| Evocador de Constituição 0 | 3,4 |
| Evocador de Constituição 3 | 5,9 |
| **Bastião de Constituição 6** | **11,0** |

Onze rodadas num combate de 3,7 é *"continue lutando, de graça"*. Cobrando **fração da própria máxima**, a janela fica em **três rodadas para os cinco Caminhos × três Constituições × oito níveis** — e o Bastião paga mais em número absoluto e a mesma fração de si mesmo. O total é 7/8: quem insiste termina a missão com um oitavo do corpo.

### Duas coisas que a conta recusou

**Teste de morte no d20**, no molde de três sucessos contra três falhas: simulado em **41% a 68% de morte por queda**, conforme a CD. Num server em que o mesmo personagem atravessa cinco a sete mesas, isso põe no dado a decisão que a trava 6 já deu para o mestre.

**Degrau de exaustão por queda** — regra caseira popular em outros sistemas, e aqui cabia, porque a peça 10 já tem a escada. Mas o degrau 3 é *desvantagem em ataque e Teste de Resistência*, e uma missão de quatro lutas com duas quedas bate o teto. **Isso é espiral de competência**, que a v0.8 consertou e a peça 10 limitou de propósito.

A distinção virou parte da peça, porque ela é o desenho inteiro:

> **Espiral de competência** — levanta pior, e as suas rolagens pioram. Proibida.
> **Espiral de letalidade** — levanta igual, mas a **próxima** queda está mais perto do fim.

### Registrado — o levantamento que sustentou o desenho

Seis sistemas, e o defeito que o Mizuki nomeou tem nome e literatura: **o vaivém de cair e ser levantado**. O D&D 5e é a origem — qualquer cura de 1 ponto te põe de pé e **não existe consequência nenhuma**. O conserto canônico é o `wounded` do Pathfinder 2e: cada vez que você levanta, a próxima queda **começa** mais perto da morte. O Draw Steel resolve por outro caminho — você não desmaia, continua agindo e se degrada —, e o Daggerheart e o Cairn cobram **cicatriz permanente**.

A causa apontada pela literatura é *"curar antes de zerar é economia de ação ruim"*. **Aqui é pior que no 5e**, por uma frase do manual: *"Cura sem limite de uso por descanso"*. O alvo certo não era proibir a cura — era fazer a **queda** custar alguma coisa que a cura não devolve.

### Adicionado — seis checagens no `conferir-atributos.py`

Elas foram para o validador **dono da peça 1**, e não para um arquivo novo: `conferir-repositorio.py` conta os `conferir-*.py` da pasta contra o número escrito em três documentos, e validador novo quebraria a contagem.

Nada fica escrito na mão — a janela, a escada de custo e a queda da Cicatriz são **lidas do texto da seção 5.5**, e o ritmo de combate vem da seção 8 da mesma peça. Os limites de design ficam declarados à parte, que é a lição nº 8.

**Oito perturbações conferidas**, e a quinta é a que vale registrar: ela saiu **"não acendeu"** e era mentira — o `sed` não bateu porque a linha começa com `> **Sequela` e o padrão ancorava em início de linha. **Vermelho e verde que não provam nada têm a mesma cara**, e a defesa é conferir o `diff` antes de ler o resultado, do mesmo jeito que a v0.35 aprendeu a conferir que a base passa antes de perturbar.

### Adicionado — a régua de magnitude dos Legados, em rascunho

`03-mecanica/RASCUNHO-legados-regua.md`. **Sem número no nome de propósito:** meia peça não é peça, e um arquivo com dois dígitos na frente quebraria a contagem. Ela vira a peça 13 quando o catálogo fechar.

O defeito registrado na v0.24 era magnitude, não quantidade, e **a máquina que o projeto já tinha passava nos catorze** — zero dominâncias estritas pelo teste da peça 3. Ela mede contenção, e o defeito é distância.

A régua não ranqueia: **três formatos, cada um travado nos próprios termos.** `Ajusta` mexe em número e sempre tem relógio da escada da peça 10, com a largura escolhendo o degrau. `Desliga` só apaga o que ninguém comprou. `Destranca` é zero no dado, e precisa de gatilho do jogador **e** de uma afirmação sobre o mundo que só aquele personagem faz.

### Achado — a lição nº 6 pelo avesso, duas vezes

**A primeira:** a régua ia dizer que Desliga *"não dá para precificar, porque o denominador está no Bestiário e o Bestiário não existe"*. Estava errado — eu não tinha procurado. O manual tem **IMUNIDADE** escrito: *"nenhuma Melhoria fura imunidade; quem quiser isso monta uma Passiva de Regra Própria, com limite de uma vez por cena"*, e tem **resistência** definida como metade do dano, *"sempre presa a um tipo"*, cobrada pela Passiva Escama. **A escada existia e o catálogo nunca foi cruzado com ela.**

**A segunda foi o Mizuki quem pegou**, lendo o Legado *Desconfiado*: apagar uma condição é o mesmo problema. O manual precifica **Condição Menor em Média** e **Condição Maior em Pesada** — o tier mais caro que existe. Eu tinha escrito **três** Desliga de condição em duas Origens, e a trava da época — *"não encosta no dano"* — passou nos três.

A trava virou:

> **Um Desliga só apaga o que ninguém comprou.** Dano não, condição não, nem o que qualquer Melhoria concede. Sobra o que o mundo faz com você fora do feitiço.

Os três viraram **vantagem no Teste de Resistência**: mesmo +25 pp no pico, e agora com um dado no meio, para quem pagou Pesada ter chance.

### Decidido — dois Legados por ficha, e um deles é obrigatoriamente Destranca

**O problema:** quando opção de ficção disputa a mesma vaga que opção mecânica, a mecânica ganha. Não é opinião — os Traços, Ideais, Vínculos e Falhas do D&D 5e ficavam em branco cerca de 90% das vezes, e a edição de 2024 removeu os quatro.

**A regra óbvia não conserta.** *Dois de listas diferentes* deixa pegar `Ajusta + Desliga`: quem otimiza continua sem ficção **e a economia mecânica dobra**. Com o Destranca obrigatório ela não dobra — quem otimiza sai com exatamente um Legado com número, e todo mundo passa a carregar uma afirmação sobre o mundo.

**Isto reabre uma linha da peça 9**, que diz *"o conserto é dar mais opções por Origem, não mais Legados por ficha"*. O teto **de poder** continua em um, porque Destranca é zero no dado — mas a mudança ainda precisa chegar na **peça 8, na peça 9, no `ficha.js` do gerador e nos dois validadores que conferem a ficha**. Enquanto for rascunho, a regra antiga é a que vale.

### Achado — o Desliga é teto e não cota, e o motivo é bom

Enumerados os alvos legais do sistema inteiro depois da trava nova: **são sete, e seis já estão usados.** Três por Origem exigiria vinte e um.

**Um Desliga precisa de coisa nomeada existindo antes dele** — e neste sistema quase tudo que acontece com você ou foi comprado por alguém, e aí tem dono, ou é arbitrado na ficção, e aí não há o que desligar. *O suprimento é estreito porque o resto está bem amarrado.* As peças que faltam — equipamento, invocação e Trilhas — é que vão criar alvo novo.

**Alvo por Origem: 4 Destranca · 4 Ajusta · até 2 Desliga.** Escritas: **Latente (10), Receptáculo (9), Descendente (10) e Reencarnado (5)**.

### Alterado — 24 KB saíram do `ESTADO-ATUAL` para a peça 11, e a mudança pegou um erro de seis versões

O documento tinha **63 KB** e truncava na leitura: a seção que o próprio prompt de retomada mandava ler primeiro caía do lado de fora do corte. **Quase 40% dele era o argumento de projeto da peça 11**, fechada desde a v0.27, numa seção ainda chamada *"a próxima peça"*.

*A primeira hipótese estava errada e foi medida:* só **10%** daquelas frases existiam na peça 11 ou aqui, então não era duplicação — era conteúdo único morando no lugar mais caro de ler. Sete das onze subseções foram para a **seção 10 da peça 11**; as outras quatro, que são da Expansão e do manual, ficaram.

**E aí o `conferir-orcamento.py` acendeu na hora.** O bloco movido dizia *"gastando PE"* sem quantidade, e o preço virou **2 PE na v0.30** — a cópia estava congelada seis versões atrás, e sobreviveu porque **nenhum validador varre o `ESTADO-ATUAL`**. Ela era duplicata da seção 6.1 inteira; virou ponteiro, e a peça 11 ficou 966 B menor do que se o bloco tivesse sido colado cru.

`ESTADO-ATUAL`: **61 KB → 49,8 KB.**

### Adicionado — a skill `rpg-da-guilda`, no repositório

`sistema/skills/rpg-da-guilda/`. Ela guarda **procedimento e nunca conteúdo** — ordem de leitura, de onde rodar os validadores e por quê, o que a triagem de nomes não pega, como escrever arquivo neste mount sem ele sumir, o arnês de perturbação e como fechar versão. **Zero números e zero lições copiadas:** ela aponta para o README, senão criaria a lição nº 9 dentro da ferramenta feita para evitá-la.

### Achado — a lição nº 9 acontecendo fora do repositório

A pasta `sistema/skills/` é cópia de trabalho das skills instaladas na conta, e o `ESTADO-ATUAL` sempre avisou que **editar lá não altera a instalada**. Conferindo as cinco na hora de preparar a migração de conta, **uma tinha divergido**: a descrição do `playtesting-rpg` no repositório era a versão antiga e mais longa, e a instalada tinha sido apertada depois.

**Descrição de skill não é enfeite — é ela que decide quando a skill dispara.** Migrar pelo repositório levaria o gatilho velho. Sincronizado.

*Fica registrado porque é o mesmo defeito de sempre num lugar novo:* duas cópias da mesma coisa, numa camada que o `conferir-repositorio.py` não alcança.

### Em aberto

- **O catálogo dos Legados**, três Origens inteiras — Feto, Corpo Amaldiçoado e Restrição Celestial — e o que falta em Receptáculo, Descendente e Reencarnado.
- **Não Sou Gente** é imunidade a dano e a régua reprova; a saída registrada é virar Passiva paga com espaço de feitiço. **Irmãos** é o piso do catálogo e precisa de gatilho do jogador.
- **O validador dos Legados**, que sai junto com a peça.
- **A Cicatriz não tem mecânica, só nome** — o conteúdo dela é da peça de dano e condições, que não existe.
- **A mudança de um para dois Legados** ainda não chegou na peça 8, na peça 9, no gerador da ficha nem nos dois validadores da ficha.
- **A lista de feitos do limiar do nível 20** e a conversão de mestragem.
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.36] — 2026-08-11

Sem regra nova e sem número novo: esta versão **fecha uma pergunta e ordena quatro peças**. Ela existe porque a pergunta ia voltar, e porque a ordem que parecia certa estava errada.

### Decidido — o Caminho continua sem dar dados de dano

O Mizuki levantou cinco árvores de habilidade, uma por Caminho, e **três delas pediam dado de dano**: a tabela de desarmado do Bastião no molde do monge, a mecânica por grupo de arma da Vanguarda, e o atributo somado ao dano do feitiço no Emanador.

A peça 5 §4 tem duas listas, e a segunda diz o contrário:

> **O que um Caminho não pode conceder:** dados de dano · aumento de Classe de feitiço · Melhoria de graça · cura

**A regra fica.** O motivo é o pilar 1, e já estava escrito: *"se o Caminho desse dano, dois personagens do mesmo Caminho começariam a se parecer, e a técnica que cada um escreveu perderia espaço."* Um sistema em que a identidade mora na técnica não pode ter o Caminho competindo com ela no eixo mais visível de todos.

**Três saídas foram levantadas e a escolha foi a mais estreita:** manter a regra e desenhar dentro dela, em vez de reabri-la com uma régua nova ou abrir exceção só para o dano físico. As duas alternativas custavam reprecificar as peças 5 e 6 e refazer a **paridade conjurador‑guerreiro** — que está calibrada de propósito em `d20 + 3` nos dois lados desde o nível 2, e que o `conferir-atributos.py` vigia.

**E metade do que o Emanador queria já existia, no eixo certo.** A peça 6 §5 concede *trocar o valor fixo de 2 do ataque de conjuração por Inteligência ou Essência*. Isso é **acerto**, não dano, e é neutro porque os dois lados crescem +3 na campanha. A proposta pedia a metade que não cabe; a que cabe estava escrita desde a v0.14.

### Decidido — a ordem das quatro, e ela mudou por dependência

A ordem levantada foi **Legados → Caminhos → Itens → Invocações**. A peça de Caminhos foi para o fim:

| | peça | destrava | depende de |
|---|---|---|---|
| 1 | **Legados** | — | nada |
| 2 | **Equipamento** | a Vanguarda, e a **Técnica Marcial** — duas das três rotas de Origem que não rodam | — |
| 3 | **Invocações** | o Evocador | — |
| 4 | **Caminho, Trilhas e subtrilhas** | o resto | **2 e 3** |

**Duas das cinco árvores não podem ser escritas antes.** A especialização de arma da Vanguarda precisa que arma exista; o benefício de invocação do Evocador precisa que invocação exista — e essa vem com a trava mais dura do projeto já escrita: *você e todas as suas invocações somados entregam uma Rotina*, porque *mais corpos agindo por rodada é a coisa que quebra todo sistema d20, sem exceção*.

**O Guia é o único que passa inteiro**, e não por sorte: *auxiliar, estender, reposicionar e recuperar* é literalmente a lista do que um Caminho **pode** conceder. Ele também fecha a pergunta aberta desde a v0.24 — *o que Elo, Sutura e Perímetro valem contra um golpe por rodada.*

### Registrado — a peça de Legados tem duas metades, e a ordem entre elas importa

O pedido foi **cinco Legados por Origem**, contra os dois de hoje — de catorze para vinte e cinco.

**O defeito registrado dos Legados não é quantidade, é magnitude.** A faixa entre os catorze vai de **Irmãos** (sente outro Feto por perto, zero em rolagem) a **Não Sou Gente** (imune a veneno, doença e ao que ataca corpo humano). A trava escrita — *"não produz dano e não escala com nível"* — **não pega imunidade**.

> **A régua de magnitude vem antes do catálogo.** Multiplicar a lista por quase três sem ela multiplica o defeito junto.

A expansão em si já estava endossada pela própria peça 9, que fecha com *"se o Legado parecer decoração, o conserto é dar mais opções por Origem, não mais Legados por ficha"*. O que muda é só que ela deixou de ser condicionada ao playtest.

### Registrado — as quatro peças caem onde não há validador

Peças **5, 6 e 9**. São três das quatro que nunca tiveram validador — e a quarta, a peça 8, ganhou o dela na v0.34 **depois** de passar sete versões com a Defesa errada e a Trilha faltando.

Não é coincidência: são as peças de catálogo e de prosa, as que não têm curva para conferir. Fica anotado para que cada uma das quatro saia **com validador junto**, e não sete versões depois.

### Em aberto

- **As quatro peças acima**, nessa ordem.
- **A quick-start de nível 2**, que sai depois delas — o sistema fica testável antes de ela existir, mas ninguém senta na mesa sem ela.
- **Os três feitiços da Kaori**, se o exemplo for para ficar completo.
- **A lista de feitos do limiar do nível 20** e a conversão de mestragem.
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.35] — 2026-08-11

**A ficha de personagem.** `05-material/` estava vazia desde a v0.1, e ela é o primeiro material deste projeto que não é argumento de design — é coisa que alguém preenche.

Três páginas, geradas por código no mesmo molde do manual, em duas versões: **em branco** e **preenchida com a Kaori**.

### A forma, e por que três páginas

O Mizuki pediu **Ficha · Técnica · Lore/referência**, e a divisão faz mais do que caber:

| página | o que carrega | com que frequência muda |
|---|---|---|
| **1 · Ficha** | identidade, atributos, os números derivados, os 4 TRs, as 23 perícias, os 10 ofícios | toda sessão |
| **2 · A técnica** | a Regra, descrição, Famílias, Selo, Passiva Livre, os 2 Classe 0 e os 3 feitiços | uma vez, na criação |
| **3 · Quem é essa pessoa** | aparência, história, o traço da Origem, o Legado, laços, instituição, pacto | devagar |

**A terceira é a que justifica o projeto inteiro.** O problema que este sistema existe para resolver é *o mesmo personagem passar por sete mesas e continuar sendo o mesmo personagem* — e o que faz alguém ser reconhecido numa mesa em que nunca jogou não é a Defesa: é o traço, o Legado, quem lhe deve favor e o que a instituição sabe. Nada nela rola dado.

*A peça 8 promete que a ficha "cabe numa página".* Não cabe: só perícias e ofícios são 33 linhas. A promessa foi medida e desmentida — as três páginas fecham **exatas**, nas duas versões, e isso foi verificado renderizando o `.docx` em PDF e contando.

### A tira de referência é curta de propósito

A página 3 traz sete linhas de consulta — o turno, arredondamento, crítico, os dois golpes, os dois descansos — e **nada além**. CDs, condições e exaustão ficam de fora e vão para a quick-start.

Não é economia de espaço: é a lição nº 9. Uma tabela de CD impressa na ficha e escrita na quick-start são duas cópias do mesmo número, e a ficha é a que ninguém volta para atualizar.

### Os feitiços da Kaori ficaram em branco

A peça 8 não lista os dela, e inventar três aqui seria **escolha de sabor**, que é do Mizuki. Quando forem escritos, entram no `make.js` e o `pac7.py` confere se a montagem fecha no orçamento da Classe 1.

### Adicionado — `conferir-ficha.py`, o décimo segundo validador

A ficha imprime catálogo: 23 perícias com atributo, 10 ofícios, 5 Caminhos com vida e PE, 15 Trilhas, e nove constantes do nível 2. **Cada um é uma cópia de uma peça**, e este projeto já sabe o que acontece com cópia sem dono — a v0.34 acabou de pagar sete versões por uma.

E aqui é pior que num `.md`: **ficha errada não fica num arquivo que ninguém abre. Ela vira personagem, em sete mesas ao mesmo tempo.**

Seis checagens, e o `gerador-ficha/dados.js` é **cópia declarada** — a autoridade é a peça, e o validador falha quando os dois discordam.

**Nove perturbações conferidas**, todas acendendo a checagem certa: perícia sumindo da ficha, ofício inventado, PE do Bastião mudando só na ficha, Trilha que a peça 6 não tem, refino indo a 4, XP divergindo da peça 12, o `.docx` sumindo, **a peça 7 ganhando perícia e a ficha não acompanhando** — que é o caso real — e o `.docx` publicado ficando para trás do código.

### Corrigido de método — uma checagem que não podia acender, e um arnês que acendeu pelo motivo errado

**Duas armadilhas da casa, nas duas direções, na mesma versão.**

A primeira: a checagem de *"o `.docx` publicado é mais novo que o gerador?"* comparava **mtime**, e ela **não acendeu** na perturbação — este mount carimba data de arquivo de um jeito que não dá para confiar. É a lição nº 8: checagem que não pode acender é pior que checagem nenhuma. Ela foi trocada por uma que lê o **conteúdo** — abre o `.docx` como zip (com `zipfile`, biblioteca padrão, sem dependência para faltar) e confere se o texto traz a proteção, a Integridade e o XP atuais. Assim reformulada, ela acende.

A segunda, pelo lado oposto: o primeiro arnês de perturbação montou a cópia com os diretórios chamados `03` e `05` em vez de `03-mecanica` e `05-material`. **As oito perturbações acenderam — todas porque o validador não achava os arquivos.** Oito vermelhos que não provavam nada, e que pareciam prova. É exatamente o que aconteceu na v0.28 rodando de `/tmp`, e a defesa é sempre a mesma: **conferir que a base passa antes de perturbar.**

### Em aberto

- **A quick-start de nível 2**, enxuta. É a última coisa entre o sistema e uma mesa de verdade.
- **Os três feitiços da Kaori**, se o exemplo for para ficar completo.
- **Um validador para as peças 5 e 9**, que continuam sem nenhum.
- **A lista de feitos do limiar do nível 20** e a conversão de mestragem.
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.34] — 2026-08-11

A varredura das doze peças, pedida antes de a ficha ser construída. **Dois erros, os dois com sete versões de idade, e os dois na faixa que a ficha ia usar.**

E o achado que vale mais que os dois: **as peças com validador estavam limpas.** Peças 1, 3, 4, 7, 10, 11 e 12, todas certas. Os dois erros estavam nas peças 6 e 8, que não tinham nenhum.

### Achado — a Defesa da ficha de nível 2 estava errada desde a v0.27

A v0.27 deu número a *cobrir-se de energia*: **`1/3 do refino + 1` de proteção**, grátis no refino 1, sem uniforme nem armadura. No refino 1 isso é **proteção 1**, e toda ficha de nível 2 tem.

A peça 8 é da v0.21. Ela dizia proteção **0**, em dois lugares, e a ficha de exemplo fechava `10 + 2 + 0 = 12`.

> **A Defesa de nível 2 é `10 + Destreza + 1`. A ficha da Kaori é 13.**

**E o mais revelador: a matemática de balanço já rodava supondo proteção 1.** A peça 1 mede o caso difícil contra *"alvo que também investiu em Destreza e tem proteção 1"*, e a checagem 1 do `conferir-atributos.py` roda com `protecao 1` desde sempre. Quem estava fora de sincronia era só a peça que publica a ficha — então o conserto é de texto, e nada foi rebalanceado.

*E ela deixa um recado para a peça de equipamento, mais forte do que o que já estava escrito:* como uniforme, armadura e escudo **desligam** a proteção de energia, a tabela de proteção não compete com 0 — ela compete com 1 no nível 2 e com 4 no refino 10.

### Achado — a decisão da Trilha ficou sete versões escrita e não aplicada

O `ESTADO-ATUAL` registra desde a v0.27:

> *"A Trilha é identidade, como o Caminho, e nasce com o personagem. **Corrigir na peça 6, na peça 8 e aqui.**"*

**Nenhum dos três foi corrigido.** A peça 6 continuava dizendo que *"as escolhas de nível compram Trilhas"*, a peça 8 listava *"não afeta o nível 2"* entre as pendências, e o `ESTADO-ATUAL` **se contradizia sozinho** — a seção da decisão dizia uma coisa e duas tabelas mais abaixo diziam a outra.

Aplicado agora nos três. A primeira Trilha vem na criação, junto do Caminho; as seguintes se acumulam com o nível, e quantas e quando continua sendo a peça de Trilhas.

> **E o que ela entrega ainda não tem número, e o texto diz isso.** Escolher a Trilha no nível 2 não custa nada e não tranca nada — ela é o nome e a frase de uma linha até a peça sair.

**A lição que sai daqui é nova, e não é a nº 9:** *decisão registrada não é decisão aplicada*. O CHANGELOG e o `ESTADO-ATUAL` são bons em guardar o **porquê**, e nada no projeto conferia se o **o quê** tinha chegado nos arquivos. Uma decisão que termina em *"corrigir em três lugares"* precisa de alguém conferindo os três.

### Adicionado — `conferir-criacao.py`, o décimo primeiro validador

**Ele confere instância, e os outros dez conferem regra.** Essa é a diferença inteira, e é o buraco por onde os dois erros passaram:

| | pergunta |
|---|---|
| os dez primeiros | *a fórmula deriva certo?* |
| **o décimo primeiro** | ***a ficha publicada obedece à fórmula?*** |

A peça 8 é a única que produz uma ficha inteira com número fechado. Ela soma o que sete outras peças decidiram — e envelhece toda vez que uma delas mexe num número, sem que nada acuse.

Sete checagens: a ficha de exemplo sai das fórmulas; o bloco de fórmulas do passo 7 bate com a peça 1; nenhuma peça afirma proteção 0; a criação entrega Trilha; a contagem de feitiços do nível 2 fecha; as duas rotas de perícia e ofício somam igual; e Caminho, Trilha e Origem citados na criação existem nas peças donas.

**Nenhum valor fica escrito dentro dele** — a proteção é lida da peça 11, a maestria e o refino da peça 8, os Caminhos da tabela do passo 3, o XP da peça 12. E ele não lê o `.docx`, então não tem por onde sair verde tendo pulado checagem.

**Oito perturbações conferidas**, numa cópia isolada, cada uma acendendo a checagem certa: a Defesa voltando para 12, a proteção 0 voltando ao texto, a Trilha saindo da criação, cobrir-se deixando de ser gratuita, os feitiços voltando para dois, os atributos somando 10, e a ficha usando uma Trilha que não existe. **A oitava é a que importa:** mudar a fórmula na **peça dona** — `1/3 do refino + 2` — acende o erro na ficha, o que prova que ele lê do dono em vez de guardar o número.

### Registrado — o sumiço de arquivo tem causa, e ela é acionável

Seis ocorrências em duas versões, e a v0.34 isolou o gatilho:

| quem grava | o bash lê de volta |
|---|---|
| o **bash** | **sempre** |
| a ferramenta de escrita do assistente | às vezes não — ENOENT com `ls` e `stat` certos |

O `conferir-criacao.py` nasceu invisível para o próprio `python3` e precisou ser reescrito pelo bash com `cat > arquivo <<'EOF'`. **Fica como procedimento: código novo se escreve pelo bash.** Para `.md` a ferramenta serve, e uma segunda escrita reconcilia quando o sumiço acontece — o `README.md` e o `LEIA-ME.md` caíram juntos três vezes e voltaram nas três.

O conteúdo nunca esteve em risco em nenhuma das seis.

### Em aberto

- **A ficha de personagem e a quick-start de nível 2**, que é o que esta varredura estava limpando o caminho para.
- **Um validador para as peças 5 e 9**, que continuam sem nenhum.
- **A lista de feitos do limiar do nível 20.**
- **A forma da conversão de mestragem.**
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.33] — 2026-08-11 · *manual v7.8 regerado*

A passada de validação e polimento que a rota previa depois da XP. **A matemática estava limpa e a prosa não** — e o pior achado não estava em documento interno nenhum: estava na capa do manual.

### Os treze passam, e passam de verdade

Rodados de `sistema/03-mecanica/`, com o controle negativo que a v0.28 pagou para aprender: os três que leem o `.docx` saem com **zero** `PULADA` do lugar certo e com **4, 1 e 1** rodados de `/tmp`. O verde é verde. Nenhum número precisou mudar nesta versão — é a primeira em cinco em que isso acontece.

### Achado — a capa do manual dizia "Versão 7.5"

> **`partA.js` nunca foi atualizado desde a v7.5. O `.docx` que a Guilda abre trazia 7.5 na capa enquanto o projeto inteiro dizia v7.8.**

Três versões do manual (v7.6, v7.7 e v7.8) e **sete versões do projeto** (da v0.26 à v0.32) mexeram no conteúdo e ninguém tocou na string da capa. Nenhum validador olhava para ela.

**E ela é a pior cópia possível para deixar derivar**, porque é a única que sai do repositório. Todo o resto da deriva desta versão é conversa entre quem trabalha no sistema; a capa é o que um jogador vê.

Consertado no gerador e **o manual foi regerado**. O diff é exatamente uma string: 363 parágrafos e 84 tabelas antes e depois. **O `.pdf` continua na v7.4**, como sempre — ele é exportado à mão.

### Achado — a deriva, medida

| documento | afirmava | é |
|---|---|---|
| **capa do `.docx`** (`partA.js`) | **Versão 7.5** | 7.8 |
| `manual/matematica/COMO-USAR.txt` | Fundamento v7.6 | 7.8 |
| `sistema/LEIA-ME.md` | **v0.27** · onze peças · **sete** validadores · manual v7.6 | v0.32 · doze · dez · v7.8 |
| `arquitetura.md` | manual v7.6 | v7.8 |
| `ESTADO-ATUAL` · seção do manual | v7.6, 328 parágrafos, 76 tabelas | v7.8, **363**, **84** |
| `ESTADO-ATUAL` · o material medido | 25.600 palavras em dez peças · 22.000 no CHANGELOG · 2.070 linhas em seis validadores | **34.200** em doze · **32.000** · **3.880** em dez |
| `ESTADO-ATUAL` · o que falta | tabela de XP *"nunca foi escrita"* | peça 12, fechada na v0.31–v0.32 |
| `ESTADO-ATUAL` · a fila | *"nunca foi escrita"* **e** *"fechada na v0.31 e v0.32"* | **o mesmo arquivo, duas respostas** |
| `ESTADO-ATUAL` · dezessete coisas | doze existem, XP entre as que faltam | **treze**, e faltam quatro |
| `ESTADO-ATUAL` · passo 6 de 6 | *"a próxima da lista original"* | fechado desde a v0.23 |
| `ESTADO-ATUAL` · playtest | zero sessões em **26** versões | 32 |
| `ESTADO-ATUAL` · lições | **cinco** | o README tem **nove** |
| `README` · o que não existe | a tabela de XP, trava nº 1 | existe |

**O `LEIA-ME.md` é o caso mais caro**, porque ele é o mapa da pasta: cinco versões parado, anunciando um sistema com onze peças e sete validadores para quem chega agora.

### Corrigido — a lista de lições tinha duas cópias, e elas divergiram

O `ESTADO-ATUAL` guardava a própria lista, parada em **cinco** enquanto o README chegava a **nove**. E a lição nº 2 da cópia ainda listava *"v0.16, v0.17, v0.19, v0.24 e v0.26"* quando o original já contava sete versões.

**É a lição nº 9 acontecendo dentro do documento que existe para avisar sobre ela.** A cópia saiu e virou ponteiro: as lições moram no README, e só lá.

### Adicionado — checagem 4 do `conferir-repositorio.py`

> **Todo número que mora em mais de um documento tem um dono declarado, e cada cópia é conferida contra ele.**

| número | dono | por quê |
|---|---|---|
| **versão do projeto** | a entrada do topo do `CHANGELOG` | é a única que não dá para escrever errado sem querer — ela só existe depois de a versão fechar |
| **versão do manual** | a primeira linha de `manual/gerador/COMO-USAR.txt` | o `.docx` é **saída**. Quando os dois discordam, quem está errado é a capa, e o conserto é regerar |
| **peças e validadores** | a pasta `03-mecanica/` | já era assim para o README desde a v0.28; agora vale para o `ESTADO-ATUAL` e o `LEIA-ME` também |

São **onze cópias** conferidas, e **nenhum dos valores fica escrito dentro do validador** — a armadilha que ele mesmo caiu na v0.28, quando guardava `sete`.

Ele também **não lê o `.docx` e não precisa de `python-docx`**, então não existe caminho por onde ele saia verde tendo pulado checagem. Isso foi de propósito: a checagem que nasceu para pegar a lição 9 não podia nascer com a lição 8 dentro.

**Cinco perturbações conferidas**, cada uma acendendo a checagem certa e nomeando o arquivo culpado: capa voltando para 7.5, `LEIA-ME` voltando para sete validadores, `ESTADO-ATUAL` voltando para onze peças, dono sem valor legível — e o caso que apareceu sozinho enquanto eu escrevia esta entrada: **subir a versão nos três documentos antes de registrar a entrada do CHANGELOG acende três erros.** Essa última é uma trava de graça que ninguém desenhou: não dá mais para anunciar versão que não foi registrada.

*Rodadas numa cópia isolada do repositório, e não nos arquivos reais* — perturbar em cima do original e restaurar depois é como se perde trabalho num mount que já engoliu arquivo quatro vezes.

### Registrado — o mount perdeu dois arquivos, e o README já sabia

Aconteceu **duas vezes** nesta versão: com o `README.md` e o `LEIA-ME.md` juntos, e depois com o próprio `conferir-repositorio.py`, sempre logo depois de uma escrita. Sintoma idêntico ao da v0.28 e da v0.29 — `ls` e `stat` com tamanho e inode certos, `open()` devolvendo **ENOENT**, vizinhos abrindo normalmente.

**Conteúdo íntegro no disco nas três vezes, e uma escrita nova reconciliou nas três.** Fica registrado porque agora são quatro ocorrências em seis versões: não é acidente, é o mount, e o procedimento do README funciona.

### Achado — o mesmo mount quebra o git inteiro, e não só o commit

O README dizia que o assistente não consegue **commitar**. Ele também não consegue **ler**: `git status`, `git log` e `git fsck` saem todos com `fatal: loose object <sha> is corrupt`.

**Não é o repositório.** Medido:

| | conta |
|---|---|
| objetos soltos em `.git/` | 241 |
| que o `ls` mostra com tamanho certo | **241** |
| que o `open()` consegue abrir | 175 |
| que devolvem **ENOENT** | **66** |
| arquivos de trabalho no mesmo estado | 1 (o `mensagem-de-commit.txt`, reconciliado) |

É a mesma falha de sempre, agora medida em escala e dentro do `.git/`. **Fora do sandbox o git funciona normalmente**, e o perigo aqui é de interpretação: quem lê "corrupt" e roda `git gc` para consertar está tentando consertar um repositório que não está quebrado.

**E rodar `git status` daqui cobra um preço:** ele cria um `.git/index.lock` que o mount depois não deixa apagar, e um lock preso trava o `./subir.sh`. Aconteceu nesta versão e foi limpo. Está no README, junto com a conclusão: **não rodar git do sandbox.**

### Em aberto

- **Ficha de personagem e quick-start.** `05-material/` continua vazia, e agora não tem mais nada na frente.
- **A lista de feitos do limiar do nível 20.**
- **A forma da conversão de mestragem.**
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**
- **O `.pdf`, na v7.4.** Quatro versões de manual atrás — e desta vez a capa do `.docx` mudou, então a diferença ficou visível.

---

## [0.32] — 2026-08-11

O Mizuki olhou a curva da v0.31 e disse duas coisas: que ela não fazia **progressão nível a nível**, e que subir três níveis numa missão *"não traz uma metodologia de jogo bom"*. Pediu pesquisa em fórum e em sistema de guilda de verdade.

**Ele estava certo, e o precedente é mais forte do que a intuição dele.**

### Achado — o defeito que derrubou o XP na maior campanha compartilhada do mundo

A **D&D Adventurers League**, com cerca de 100 mil membros, abandonou experiência na temporada 8, em 2018. O motivo documentado é literalmente o caso que o Mizuki descreveu:

> *"Uma aventura de quatro horas levava um personagem novo do nível 1 ao 3 — mais rápido do que os designers pretendiam."*

E o defeito espelho junto: *"jogadores ficavam presos no nível 4 por muito tempo, porque o XP era fixo por faixa e não ajustado ao nível."*

**A nossa curva tinha exatamente o primeiro.** Medido: um final de arco jogado por um personagem de nível 2 entregava **três níveis de uma vez**.

### Achado — os dois grandes sistemas de jogo organizado convergem numa coisa que a nossa curva não tinha

| | como conta |
|---|---|
| **Adventurers League** | 4 checkpoints por nível até o 4, 8 dali em diante · 1 checkpoint por hora |
| **Pathfinder Society 2e** | 12 XP por nível, cenário paga 4 — **três cenários por nível**, sempre |

**Os dois compram a mesma propriedade: o custo de um nível é um número inteiro pequeno de sessões, legível sem tabela.** *"Estou no nível 12, cada nível são quatro missões, joguei duas."*

A reta da v0.31 — `100 + 30 × (nível − 2)` — dava 1,3 missão no nível 3, 1,6 no 4, 2,8 no 8. **Só o nível 2 caía redondo.** Todo o resto pedia conta.

### Decidido — a curva vira degrau, e ele sobe a cada três níveis

> **Um nível custa um número inteiro de missões padrão, e o número sobe uma a cada três níveis.**

| níveis | custa | | níveis | custa |
|---|---|---|---|---|
| 2 a 4 | 1 missão | | 17 a 19 | 6 |
| 5 a 7 | 2 | | 20 a 22 | 7 |
| 8 a 10 | 3 | | 23 a 25 | 8 |
| 11 a 13 | 4 | | 26 a 28 | 9 |
| 14 a 16 | 5 | | 29 | 10 |

**Ela mantém as duas propriedades da v0.31 e ganha a terceira.** Continua crescendo — que é o que fecha o abismo entre quem jogou e quem sumiu, e é a razão do XP ser fixo. E agora é legível de cabeça.

*Por que não a curva plana da Pathfinder Society:* com custo plano **ninguém alcança ninguém**, porque todos sobem no mesmo ritmo para sempre. A PFS resolve isso com faixas de nível por cenário — mesa aberta de guilda não tem esse luxo. Perturbei o validador para plano e ele acende.

### Decidido — nenhuma missão dá mais de um nível

> **Você sobe no máximo um nível por missão. O XP que sobrar fica acumulado e sai na próxima.**

**O excedente não some**, e isso é o que faz o teto não tirar nada de ninguém — ele só espalha. Quem levou um final de arco no nível 2 sobe na hora e entra na missão seguinte com 200 XP no bolso.

**E ele quase não atrasa nada.** Simulado com missão padrão, com teto e sem teto dão o mesmo nível em 10, 20, 40, 60 e 80 missões — porque com missão padrão o teto nunca chega a morder. Ele é rede de segurança para o caso grande.

### Os números novos

| | v0.31 | v0.32 | alvo |
|---|---|---|---|
| 2 → 20 | 6.390 XP · 60 missões | 6.300 XP · 59 | 60 |
| 20 → 30 | 7.750 XP · 32 | **8.200 XP** · 34 | 32 |
| joga pouco | 13,9 meses | 14,5 | 14 |
| mediano | 9,3 | 9,7 | 9 |
| joga muito | 5,1 | 5,3 | 6,5 |

### Corrigido de método — a mesma cegueira pela terceira vez em três versões

A checagem do teto comparava o resultado contra `TETO_NIVEIS_POR_MISSAO` — a **própria constante que ela deveria vigiar**. Subir a constante subia a régua junto, e a perturbação saía verde.

É o terceiro exemplar da mesma espécie em três versões seguidas:

| versão | onde | o que a checagem não via |
|---|---|---|
| v0.28 | dominância das três rotas | o eixo dos feitiços, que era o da pergunta |
| v0.30 | upkeep das anti-domínio | a constante, porque `1.0` estava escrito na mão |
| **v0.32** | teto de níveis por missão | a própria constante, por auto-referência |

**O conserto é sempre o mesmo:** separar *a regra aplicada* do *limite de design*. Agora `MAXIMO_DE_DESIGN = 1` é declarado à parte, e a checagem falha se a regra passar dele **ou** se o resultado passar.

**Nove perturbações conferidas** no `conferir-xp.py`, três delas novas: teto removido, custo deixando de ser inteiro, e curva plana.

### Em aberto

- **A lista de feitos do limiar do nível 20.**
- **A forma da conversão de mestragem.**
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale.**
- **Nome do sistema.**

---

## [0.31] — 2026-08-11

**A tabela de XP.** A trava nº 1 de mundo compartilhado — *"XP tabelado, nunca marco narrativo"* — ficou aberta por trinta versões, e é a última coisa que separava o sistema de ser jogável de ponta a ponta.

E é a **primeira peça deste projeto escrita a partir de dado de gente real**: catorze opiniões da Guilda sobre quanto tempo a subida deve levar. **Décimo validador**, e ele confere uma coisa que nenhum outro confere — que a regra continua produzindo o *tempo* que as pessoas pediram.

### O levantamento, medido

Mediana de **10,25 meses** para o 2→20 e **4,1** para o 20→30, razão **0,45**. O Mizuki punha o mediano em 9 meses e a razão em 0,61 — um pouco mais rápido que o grupo, com o "joga pouco" dele batendo no teto de quase todo mundo.

**Todas as catorze concordaram numa coisa só:** a faixa lendária é mais curta em tempo, apesar de ter dez níveis contra dezoito.

### Decidido — XP fixo por missão, e a razão é uma propriedade de guilda

> **A missão paga o mesmo para todo mundo na mesa, independente do nível de quem recebe.**

Numa guilda, mesa aberta junta nível 8 com nível 14 — não é exceção, é terça-feira. Simulado: dois personagens começam juntos, um perde dez sessões, depois jogam tudo junto.

| depois de | XP fixo | XP escalado pelo nível |
|---|---|---|
| 20 sessões | 4 níveis | 4 |
| 40 | 2 | **4** |
| 90 | **1** | 0 |

**Com XP fixo a distância só encolhe**, e é aritmética pura: cada nível custa mais que o anterior, então a mesma missão vale uma fatia menor para quem está na frente. Ninguém recebe nada de especial — o atrasado só precisa de menos.

**Com XP escalado ela trava**, e só fecha quando alguém encosta no teto de nível. É o **gap** que o Kekka descreveu: *"tiveram players literalmente bloqueados de ganhar gap de tão mutantes que eram."*

### Decidido — "Grau dá mais XP" bate numa decisão de arquitetura

A proposta que apareceu no levantamento foi a de D&D: inimigo de grau mais alto paga mais. **A intuição está certa e o alvo está errado** — missão difícil já vale mais, pelo tamanho dela.

E se o **Grau** desse XP, ele quebraria uma separação que o `arquitetura.md` fez de propósito: *"todo personagem começa Grau 4, e a patente sobe por **feito**"*, *"o Yuta é Grau especial, Nível baixo"*. Grau é reconhecimento; nível é poder. Juntar os dois vira espiral fechada — sobe de patente, sobe de nível mais rápido, ganha patente por feito.

### A curva, e o tamanho da missão

> **XP para subir = `100 + 30 × (nível − 2)`** — 100 no nível 2, 640 no 20, 910 no 29.

Reta de propósito: um mestre confere de cabeça que *"o próximo custa trinta a mais"*. Exponencial daria o mesmo efeito e uma tabela consultada toda vez.

| missão | paga |
|---|---|
| curta / roleplay | 50 |
| padrão | 100 |
| longa | 200 |
| final de arco | 300 |

**Uma curva só, e quem varia é a missão** — e é isso que faz a faixa lendária ser mais rápida sem nenhuma regra de exceção:

| faixa | XP | missões |
|---|---|---|
| 2 → 20 (18 níveis) | 6.390 | ~60 |
| 20 → 30 (10 níveis) | **7.750** | **~32** |

Dez níveis lendários custam **mais XP** que dezoito mundanos e levam **metade das missões**, porque lá em cima a Guilda roda final de arco.

**E missão de roleplay paga.** Uma guilda que só dá XP para quem mata perde metade do que a faz ser guilda.

### Decidido — retorno decrescente, e não teto

> **As duas primeiras missões da semana pagam cheio. A terceira paga metade, a quarta metade disso, e assim por diante.**

100% · 100% · 50% · 25% · 12% · 6%.

**Ninguém sai com zero, e essa é a razão de ser decrescente.** A escolha entre teto duro e decrescente foi do Mizuki, e o argumento é de mesa e não de planilha: *"por mais que o foco deveria ser jogar e ter história, é garantido que reclamariam de acabar tendo XP zero."* Um teto produziria a sessão de seis horas que termina em nada.

**O que ele resolve** veio pronto do levantamento, do Mega: *"muita gente só mestra pelo XP e isso vira cúmulo."* Quando a terceira mesa da semana vale metade, moer mesa para de compensar sozinho, sem proibição e sem fiscal.

| perfil | mesas/semana | 2 → 20 | o alvo |
|---|---|---|---|
| joga pouco | 1 | 13,9 meses | 14 |
| mediano | 1,5 | 9,3 | 9 |
| joga muito | 4 | **5,1** | 6,5 |

**O terceiro fica um mês e meio na frente, e isso está registrado e não consertado.** Puxá-lo para trás exigiria dar cheio só na primeira missão da semana — e aí quem joga uma vez por semana perde metade, que é exatamente quem não se quer punir. Sem o decrescente ele chegaria em 3,5 meses.

### Decidido — mestrar não dá XP

> **Mestrar paga na moeda que o sistema já tem separada: patente, contato, favor, acesso.**

A decisão mais impopular da peça e a de argumento mais curto: se mestrar paga XP, mestrar vira a rota ótima de subir, e quem mais dirige o mundo é quem menos joga nele.

*Fica em aberto:* uma conversão pontual depois de muitas mesas mestradas — **um bônus por marca, nunca por sessão**.

### Decidido — o limiar do nível 20

> **Você chega ao 20 por XP. Você passa dele por feito.**

Pedido pelo Zeuk e pelo Soler, e o argumento não é de balanceamento: *"tirar a ilusão do 'cheguei no lvl 20 pro 21 em 4 meses enquanto fulano upou 7 níveis'."*

Ele encaixa numa coisa que o sistema já tinha — a patente sobe por feito — e é **o único lugar onde o eixo social e o de poder se tocam**, uma vez só, na fronteira do mundano com o lendário. O XP continua acumulando e nada se perde.

**A lista de feitos fica em aberto**, e ela precisa ser fechada no molde do ambiente propício: entradas escritas, palavra final do mestre em cima delas.

### Decidido — falhar paga metade ou nada, e o mestre escolhe

Faixa e não número, porque azar de dado não é a mesma coisa que abandono. **O piso é metade e não zero** — seis horas que terminam em nada fazem a pessoa não voltar; **o teto é metade e não cheio** — senão o sucesso deixa de significar. Discricionariedade assumida, no molde do *"o mestre declara o que foi uma luta"*.

### Adicionado — `conferir-xp.py`, o décimo validador

Cinco checagens, e uma delas é inédita no projeto: **ele confere que a regra ainda produz o tempo que a Guilda pediu**, com tolerância declarada por perfil. Se alguém mexer na curva ou no tamanho das missões, ele diz de quanto o alvo saiu.

**Seis perturbações conferidas**: curva plana, curva decrescente, decrescente virando teto duro, missão padrão dobrada, faixa lendária ficando mais longa que a mundana, e o decrescente frouxo demais.

**E ele pegou um critério errado meu antes de fechar:** eu exigi distância **zero** entre o atrasado e o líder em 120 sessões, e 120 sessões não alcançam o teto de nível. O invariante certo é a distância **encolher sempre e terminar pequena** — ela zera em 160 sessões, depois do fim de uma campanha, o que na prática quer dizer um nível de folga.

### Em aberto

- **A lista de feitos do limiar do nível 20.**
- **A forma da conversão de mestragem.**
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale**, e os seis números do push.
- **Nome do sistema.**
- E a fila mudou: com a XP escrita, **o que falta para alguém jogar é ficha e quick-start.**

---

## [0.30] — 2026-08-11 · *manual v7.8*

O Mizuki notou uma coisa e ela derrubou o método de três versões seguidas: **todo cálculo de custo em PE deste projeto mediu uma peça sozinha contra o bolso inteiro.** Uma ficha de verdade gasta tudo ao mesmo tempo.

**Nono validador**, e ele é o primeiro que responde *"cabe tudo junto?"*.

### Achado — o erro não era de conta, era de modelo

Quando a v0.29 escreveu *"1 × Classe por rodada cabe em 3 a 4 lutas"*, o personagem dessa conta segura uma postura defensiva e **não conjura nada**. Isso não é um personagem: é uma estátua. O mesmo vício está nas contas de PE da v0.28 e da v0.27.

**E ele era invisível para os onze validadores**, porque cada um mede uma peça contra a régua dela. Nenhum somava. É a maior das três cegueiras achadas nesta semana — as outras foram a checagem de dominância que não via o eixo dos feitiços e o `1.0` escrito na mão dentro do laço.

### Corrigido de método — e a correção corrigiu a correção

A primeira soma que eu apresentei dizia que segurar uma anti-dominío e conjurar custava **136% do dia** de um Bastião no nível 22, ou seja, era impossível. **Esse número também estava errado**, e pelo lado oposto: ele supunha conjurar **toda rodada**.

> **Conjurar toda rodada nunca coube, com ou sem upkeep.** O bolso só dá para conjurar em **38% a 48%** das rodadas do dia num Bastião, e 57% a 76% num Emanador.

O upkeep é 20% do custo de uma rodada; o feitiço é 80%. Eu culpei o upkeep por um estouro que já existia sem ele. **Segurar durante um domínio inteiro sempre coube: 1 a 1,7 feitiços, 21% a 34% do dia.**

E a economia já pressupõe essa folga de propósito — o resto das rodadas vai para Classe 0, golpe simples e projetar energia, que não custam nada. Isso não é aperto: é o desenho.

### Decidido — o preço das anti-domínio fica como estava

O Mizuki pediu para reduzir o upkeep pela metade e reavaliar. A reavaliação achou uma coisa que ninguém tinha visto: **são duas travas diferentes, e elas puxam para lados opostos.**

| | o que ela faz |
|---|---|
| **custo de ativar** | pune ligar sem precisar — é afundado, some se a luta não vem |
| **upkeep** | limita quanto tempo você segura — **quanto menor, mais tempo ligado** |

Baixar só o upkeep **alarga** a janela de pré-ligamento, que era exatamente o que ele queria fechar: de 2,4 para 4,9 min.

Seis candidatos foram medidos no somatório:

| | um domínio (nv22) | do dia | feitiços que sobram | pré-ligado |
|---|---|---|---|---|
| **A** `0×` ativar · `1×` upkeep | 30 | 34% | 3 | **2,4 min** |
| B `0×` · `0,5×` | 15 | 17% | 4 | 4,9 min |
| C `2×` · `0,5×` | 27 | 31% | 3 | 4,2 min |
| E `2×` · `0,75×` | 37 | 42% | **2** | 3,1 min |
| F `1×` · `1×` | 36 | 41% | **2** | 2,7 min |

**A e C passam nos três invariantes; E e F falham** — deixam dois feitiços para o resto do dia, e aí uma luta de domínio come o dia inteiro. A escolha ficou no **A**: nada muda, porque o somatório absolveu o preço que já estava lá.

### Achado — um preço sem número, desde a v0.27

> **Cobrir-se de energia, a Reação: `1,5 × refino` de Redução de Dano por 2 PE.**

Estava escrito só *"gastando PE"*. É a lição nº 6 pelo avesso: ali o termo existia e o **número** não. O `conferir-orcamento.py` procura essa forma agora, e a busca varreu as onze peças.

**E os 2 são fixos porque o limitador dela não é PE** — é a Reação, uma por rodada, e a proteção perdida por um turno. Medido contra o que um PE compra atacando, só o valor fixo mantém defender não sendo estritamente pior que atacar: `+0,0` no nível 14 e `+0,9` no 30, contra `−2,0` e `−4,1` se ela custasse `1 × Classe`.

### Adicionado — `conferir-orcamento.py`, o nono validador

Cinco checagens, e nenhuma delas existe em outro lugar: a linha de base cabe; um compromisso não pode calar o personagem pelo resto do dia; pré-ligar não pode compensar; o dano de alma empilha por baixo sem falir ninguém numa rodada; e **todo preço em PE tem número**.

**Seis perturbações conferidas**, todas rodadas de `03-mecanica/`: bolso pela metade, upkeep em `3×`, upkeep zerado, upkeep em `0,1×`, Integridade quadruplicada, e o preço sem número voltando para a peça 11.

**E ele deu dois falsos positivos antes de ficar de pé**, os dois registrados no código: `custa Pesada` casava com `custa PE` por falta de um `\b`, e a nota que *explica* o preço antigo citando *"gastando PE"* era acusada como se fosse regra. Citação não é regra.

### Alterado — a coluna de PE do manual ganhou uma caixa (v7.8)

O Mizuki pediu para refazer os cálculos dela agora que existem aptidões. **A conta estava certa** — ela é PE total dividido pelo custo, e bate em todas as seis linhas. O que faltava não era número: era dizer o que ela **não** conta.

Medido: segurar uma anti-domínio durante um domínio inimigo tira **uma** conjuração do dia, duas no nível 20. A tabela não precisou mudar.

> **A caixa nova diz que a coluna é um teto, e não um orçamento de dia** — e diz por quê, porque foi tratar teto como orçamento que produziu esta versão inteira.

### Em aberto

- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale**, e os seis números do push.
- **Tabela de XP**, a próxima da fila.
- **Nome do sistema.**

---

## [0.29] — 2026-08-11

As quatro anti-domínio, destravadas pela v7.7. A pesquisa na obra **inverteu uma decisão** que estava escrita em três documentos, e a inversão mudou quem é a resposta barata do sistema.

### Achado — nenhuma das quatro serve contra a Expansão incompleta, e isso é canon

> **Elas anulam acerto garantido. A incompleta não tem acerto garantido — o Acerto dela rola.**

O wiki da Cesta Oca de Vime é explícito: ela *"não neutraliza a técnica em si, o que a torna ineficaz contra domínios incompletos ou não-letais"*. E tem cena: o **Reggie ativou Cesta Oca dentro do Jardim de Sombras Quimérico do Megumi** — incompleto — e os shikigami tomaram forma e bateram nele do mesmo jeito. O Domínio Simples tem o mesmo limite.

Isso encaixa exato nos dois degraus da v7.7 e **não abre buraco nenhum**: contra a incompleta você se defende com Defesa e Teste de Resistência, como de tudo o mais. E é o que faz o terceiro espaço da completa comprar alguma coisa de verdade — ele troca um Acerto bloqueável por Defesa por um que só estas quatro alcançam.

### Corrigido — a Cesta Oca é a predecessora, e o projeto tinha invertido

O `ESTADO-ATUAL` dizia *"Domínio Simples sem gate — é o que se ensina"*, e punha a **Cesta Oca acima dele**. A obra diz o contrário: a Cesta Oca de Vime é a **técnica antiga que o Domínio Simples melhorou**. O Reggie usa ela porque é feiticeiro do passado, não porque é mais forte. Gatear a versão pior mais alto cobra mais caro pelo produto inferior.

> **Cesta Oca de Vime é Classe 1, sem gate. Domínio Simples subiu para Classe 2.**

**E isso trocou o dono da resposta barata.** O argumento *"o acerto garantido só é jogável porque a resposta é barata"* estava pendurado no Domínio Simples no nível 6. Com ele em Classe 2 (nv10 · 10 · 14), quem chega no nível 6 para as três rotas é a Cesta Oca — **e ela responde menos**, porque anula o Acerto e não o Efeito.

**O argumento continua de pé, e vale escrever por quê:** o que a peça 11 chamou de opressivo foi o acerto que nunca falha, não o Efeito. A resposta barata cobre o que precisava cobrir, e só isso.

### Decidido — o eixo que separa as quatro é liberdade, não força

Os quatro preços vêm da obra, e nenhum foi inventado:

| | protege | e cobra |
|---|---|---|
| **Cesta Oca de Vime** | só você, numa esfera | você segura o símbolo e **não faz mais nada** |
| **Domínio Simples** | um raio em volta | **os pés não saem do chão**, ou quebra |
| **Pétala** | o corpo, e **devolve o golpe** | concentração, e **não para ataque físico** |
| **Extensão de Domínio** | o corpo, e faz o **seu** ataque acertar | **nenhum feitiço enquanto estiver de pé** |

| | Classe · gate | abre em | refino escala | PE/rodada |
|---|---|---|---|---|
| Cesta Oca de Vime | 1 · sem gate | nv 6, três rotas | **nada** | **nenhum** |
| Domínio Simples | 2 · refino 4, nível 7 | nv 10 · 10 · 14 | raio `1,5 m + refino÷2` | `1 ×` Classe |
| Pétala | 2 · refino 4, nível 7 | nv 10 · 10 · 14 | `refino÷2` Acertos devolvidos | `1 ×` Classe |
| Extensão de Domínio | 3 · refino 7, nível 13 | nv 14 · 18 · 26 | duração `refino` rodadas | `1,5 ×` Classe |

### Decidido — o custo por rodada, e a conta escolheu sozinha

Medido no Bastião, que é o menor bolso do sistema, numa luta de 3,5 rodadas:

| custo/rodada | do dia, por luta | lutas que cabem |
|---|---|---|
| metade da Classe | 9% a 18% | 5 a 11 |
| **`1 × Classe`** | **20% a 26%** | **3 a 4** |
| `2 × Classe` | 41% a 52% | 1 a 2 |

**O `1 ×` fica exatamente do tamanho do orçamento de lutas do dia** — a exaustão dispara da quarta, então dá para segurar a defesa em toda luta de um dia normal e terminar seco quando o cansaço chegaria de qualquer jeito. `2 ×` deixa você se defender uma vez e acabou; metade cai para 9% no nível 20 e **evapora**.

**A Cesta Oca é de graça em PE porque já cobra o turno**, que é o recurso mais caro de uma luta. Evitar dois Acertos custa **57% dos seus turnos**: você sobrevive e não contribui. Resposta de sobrevivência, não de vitória — que é o que ela é na obra. Cobrar PE em cima seria cobrar duas vezes pela mesma escolha.

### Escritas, com o que cada número segura

**O raio do Domínio Simples** é `1,5 m + refino ÷ 2` — 2,5 m no refino 2, que é onde o canon está (~2,21 m), e 6,5 m no teto. **Ele nunca passa de um movimento (9 m)**, e essa é a trava: uma defesa que cercasse o inimigo seria outra peça. O Kusakabe puxando gente para dentro fica como coisa da Trilha dele.

**A Pétala devolve `refino ÷ 2` Acertos**, e a completa solta `1 + duração` — 3 a 6. **Sempre sobra um**, em toda faixa de refino. Se ela devolvesse tudo, o terceiro espaço da completa deixaria de comprar alguma coisa.

**A Extensão se auto-limita pelo PE.** Ela dura `refino` rodadas, o dobro de uma Expansão, mas segurar até o fim custa 75% a 92% do dia de um Bastião — e **no nível 26 custa 106%**, ou seja, ele fica sem PE na nona rodada de dez. A duração é teto, não promessa. Some com *"você não lança nada enquanto ela está de pé"*: quem tem feitiço bom paga o dobro por ela.

### Adicionado — checagem 10 no `conferir-expansao.py`

A resposta mais barata alcança as três rotas antes de a Expansão existir; o upkeep cabe no orçamento de lutas do dia sem evaporar; a Pétala nunca anula o Acerto inteiro; o raio nunca vira cerca; e a escada de PE não decresce com a Classe.

**Seis perturbações conferidas**, todas rodadas de `03-mecanica/`: Cesta Oca subindo para Classe 2, upkeep em `2 ×` e em `0,5 ×`, Pétala devolvendo o refino cheio, raio em `1,5 × refino`, e a Extensão ficando mais barata que o Domínio Simples.

### Corrigido de método — a checagem do upkeep não lia a constante

A primeira versão dela tinha `1.0` escrito na mão dentro do laço, em vez de ler o multiplicador da tabela. Uma perturbação na constante **não acendia nada** — o mesmo defeito que a checagem de dominância do `conferir-aptidoes.py` tinha na v0.28, na mesma semana. Agora ela lê da tabela, e a mensagem de erro reporta o valor real em vez de um número fixo.

**É a lição nº 7 pela segunda vez em duas versões:** um número que mora em dois lugares vai divergir — inclusive quando os dois lugares estão no mesmo arquivo.

### Em aberto

- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale**, e os seis números do push.
- **A aptidão que baixa a Expansão para Ação Bônus** — citada, não escrita.
- **Tabela de XP**, que é a próxima da fila.
- **Nome do sistema.**

---

## [0.28] — 2026-08-11 · *manual v7.7*

A Expansão de Domínio, que era a coisa que a v0.27 registrou como bloqueadora de quatro entradas do catálogo. Ela saiu — e o caminho até ela achou **dois documentos que discordavam sobre quantos feitiços um personagem tem**, um validador que guardava um número em vez de lê-lo, e uma checagem de dominância que não enxergava o eixo que ela precisava enxergar.

**Oitavo validador.** E três nomes morreram na triagem, um deles depois de já estar escrito nesta versão.

### Decidido — os gates, e o que a conta separou de verdade

O `ESTADO-ATUAL` registrava nível 10 / refino **3** e nível 14 / refino **5**. O CHANGELOG da v0.27 registrava refino **4** e **6**. Os dois estavam meio certos, e a curva do `arquitetura.md` 4.3 separou:

> **Incompleta: nível 10 e refino 4, por 2 espaços. Completa: nível 14 e refino 5, por 3 no total — e ela exige ter a incompleta.**

**No nível 10 as três rotas estão coladas** — refino 5, 4 e 3, sem buraco entre elas. Então **qualquer gate que barre o generalista pega o meio a meio com folga zero**. Isso não é escolha de número: é o formato da curva, e só dá para escolher quem raspa.

**No nível 14, refino 5 e refino 6 separam exatamente as mesmas rotas.** Os dois barram só o generalista. Eles diferem na direção em que quebram, e o validador mediu: com **5**, a curva caindo um ponto não move ninguém; com 6, ela tira a completa do meio a meio. O 5 é imune para o lado que dói.

**E "barrado" quer dizer atrasado.** O generalista chega à incompleta no 14 e à completa no 18 — quatro níveis atrás nos dois degraus. Ele paga em tempo o que não pagou em marco.

### Corrigido — o preço da completa nunca esteve em aberto

O `ESTADO-ATUAL` dizia *"a definir"*. Mas a própria seção do Leque dizia 3, e **as três tabelas de orçamento da peça 11 só fecham com 3** — conferidas as nove células. `2 + nível÷2 + marcos` dá 12/16/21/24, e as linhas de Passiva batem em 3/7/12/15 e 0/0/3/6.

E um número velho junto: *"dois feitiços são 33% da lista no nível 10"* foi calculado com a fórmula anterior à v0.27. Com nove espaços no nível 10, dois são **22%**.

### Achado — o manual e o projeto tinham calendários de feitiço diferentes

A v0.27 mandou *"o manual corrigir o treze na v7.7"*, tratando como um número. **Não era um número: era um calendário inteiro.**

| nv | manual (tabela 9) | projeto (peça 11) |
|---|---|---|
| 6 | 4 | 6 |
| 14 | 9 | 12 |
| 20 | **13** | **16** |
| 30 | 18 | 24 |

O manual dava 2 no nível 1, +1 em cada **ímpar**, e extras no 10 e no 20. O projeto dá `2 + nível ÷ 2` — que sobe nos **pares** — mais um por marco. **Cada documento era coerente consigo e nenhum era coerente com o outro**, e a distância crescia: +3 no nível 20, +6 no 30.

E os extras **se cruzavam no nível 10**: o manual dava um feitiço ali e o projeto também. Se os dois valessem juntos, o nível 10 contaria duas vezes — a lição nº 2 pela sétima versão seguida.

> **O manual parou de contar feitiço.** A tabela 9 ficou com o que é do Fundamento — Classe por nível, Liberação Máxima, quando cada Classe de Passiva abre — e a contagem tem um dono só. É o mesmo modelo de dono único que a v0.26 escreveu para as três tabelas compartilhadas.

**Efeito colateral achado na varredura:** a peça 8 ainda dizia *"dois feitiços conhecidos"* no nível 2, em três lugares, incluindo a lista de abertura. A fórmula dá **três** desde a v0.27, e ninguém tinha corrigido. A ficha da Kaori não lista feitiços, então foi conserto de texto e não de exemplo.

### Decidido — o que a Expansão custa para usar

| | incompleta | completa |
|---|---|---|
| abrir | `6 × maior Classe` | `8 × maior Classe` |
| desconto lá dentro | `1/3 do refino` | `metade do refino` |
| duração | `metade do refino` em rodadas, mínimo 1 | |
| barreira | não tem | `50 × metade do refino`, só por fora |

**A escada fecha:** feitiço do topo `3×` < Técnica Máxima `5×` < incompleta `6×` < completa `8×`. E a incompleta passar da Máxima responde uma pergunta de design que apareceu no caminho — *"a incompleta não é mais fácil de ter que uma Técnica Máxima?"*. Ela chega sete níveis antes, sim. Mas a Máxima é **dada** no nível 17 para toda ficha, de graça e sem gate, e a incompleta é **comprada**, por dois espaços de lista e um gate de refino que barra uma das três rotas. *"Mais fácil"* está certo no calendário e errado no preço.

**O desconto quase virou lucro, e isso foi por pouco.** A duração é também quantos feitiços saem lá dentro, então desconto × duração compete com o custo de abrir:

| abrir | desconto | nv14 | nv20 | nv30 |
|---|---|---|---|---|
| `6 × Classe` | refino cheio | +3 | **−6** | **−8** |
| `8 × Classe` | metade do refino | +23 | +24 | +31 |

Com `6 ×` e refino cheio, **o saldo fica negativo do nível 20 em diante** — você abre o domínio e termina com mais PE do que começou. As combinações escolhidas ficam entre +18 e +31 em todo nível, e a margem não encolhe.

**E o desconto precisa de piso.** Sem *"nenhum feitiço custa menos de 1 PE"*, o refino 10 zeraria as Classes baixas e o PE deixaria de existir como recurso dentro do domínio.

### Decidido — o Acerto acontece no relógio do portador

Três formatos foram levantados, e dois caem no mesmo problema: pôr o proc no turno dos alvos. **"Começo da rodada dos alvos" não é um momento definido neste sistema** — a iniciativa é `d20 + Destreza` por criatura, então não existe rodada coletiva de inimigos, e dois mestres resolveriam diferente. E "fim do turno dos alvos" deixa todo mundo agir antes de o domínio encostar, o que esvazia o acerto garantido que o terceiro espaço comprou.

> **O Acerto acontece quando você abre, e de novo no começo de cada turno seu.** Um relógio, o do portador.

**E a preocupação com a aptidão que baixa o custo para Ação Bônus já tinha resposta escrita.** A regra de ouro nº 6 — *"feitiço em Ação Bônus ou Reação só permite mais um de Classe 0 no turno"* — resolve sozinha o caso de sair o Acerto garantido mais um feitiço da ação padrão. É a lição do Carregar de novo: **a tensão era lacuna de texto, não de preço.** Bastou escrever que a Expansão conta como feitiço para aquela regra.

### Decidido — o Efeito é escrito com o mestre, e o Acerto tem duas réguas

O Efeito sai no molde da **Regra Própria**, porque nenhum domínio da obra cabe num orçamento de dados — pachinko, julgamento, enxurrada de informação.

E o Acerto ganhou a régua que faltava, sem inventar nada:

- **Acerto que é dano garantido** → a régua é a Melhoria **Inescapável**, que custa uma Média e proíbe o feitiço de ter qualquer outra peça.
- **Acerto que é regra sobre o ambiente** → os requisitos da Regra Própria.

*Uma versão desta análise dizia que o +1 espaço da completa estava subprecificado contra o Inescapável.* Estava mal formulada: comparava as duas como se o Acerto fosse sempre dano. O do Higuruma — *"ninguém no ambiente pode causar dano"* — não é rolagem de dano nenhuma. A comparação só vale para a família que é dano, e é exatamente essa que a régua do Inescapável cobre.

### Adicionado — o Rescaldo, e o nome que morreu depois de escrito

A técnica queima quando o domínio acaba, **de qualquer jeito** — desfeito por vontade, expirado ou estilhaçado. O compêndio não distingue os três, e por isso **isso é preço e não risco**: acontece em todo uso, e quem abriu já sabia.

*Uma versão desta versão propôs tornar o gatilho condicional só à quebra, para preservar a energia reversa no cérebro como resposta a algo que acontece às vezes. A obra decidiu contra, e o texto passou a dizer que é custo fixo.*

**O nome era `Queima de Técnica`, e a triagem matou.** `Queima` já é Melhoria do manual — *"metade dos dados de novo, no começo do próximo turno do alvo"* —, e dois Queimas na mesma mesa com um deles causando dano é a colisão que este projeto mata nome para evitar. `Empurrão` e `Estilhaço`, que apareciam na descrição do clash, **também estão ocupados**. Sobrou **Rescaldo**, que é o que fica depois de algo queimar.

### Adicionado — `conferir-expansao.py`, o oitavo validador

Nove checagens: os gates separam o que dizem, a ordem entre os degraus não inverte, barrado é atrasado e não trancado, o preço fecha com as tabelas publicadas, a resposta anti-domínio chega antes da ameaça, a fragilidade da curva medida nas **duas** direções, o desconto não paga a própria Expansão, o piso segura o custo de feitiço, e a barreira cai dentro da própria duração.

**Oito perturbações conferidas**, cada uma acendendo a checagem certa: gate que para de barrar, gate que barra demais, gate da completa mais frouxo que o da incompleta, preço em 4, preço igual ao da incompleta, incompleta descendo para o nível 6, curva do generalista subindo, e a linha passiva do marco sumindo.

### Corrigido — a checagem de dominância não via o eixo da pergunta

Ao validar se o Leque devia devolver dois feitiços em vez de um, a checagem 5 do `conferir-aptidoes.py` saiu **verde** com a rota pura indo de 31 para 38 espaços. O motivo: ela olhava atributo, aptidões e Passivas, e **não olhava refino nem feitiços** — justamente o eixo em que o Leque lidera.

Agora ela olha os cinco, confere a recíproca (nenhuma rota pode **liderar** em todos), e ganhou duas travas diretas: o Leque devolve exatamente um feitiço por escolha, e a rota de Leque não pode terminar com mais espaços a mais do que existem marcos. **Perturbação conferida:** o `+2` acende as duas.

**E a resposta à pergunta foi não.** A lista não está escassa contra a régua que existe: o manual pretendia treze no nível 20, e a rota de Leque já entrega **20**, +54%. O aperto que se sentia vem da Expansão, e é o preço dela funcionando — sem comprar Expansão a lista nunca fica curta.

### Corrigido — o `conferir-repositorio.py` guardava o número em vez de lê-lo

Ele falhou quando o oitavo validador entrou, porque tinha `sete` escrito no código. Agora ele **lê o número do README** e compara — o mesmo defeito que a checagem 4 do `conferir-manual.py` existe para pegar, dentro do próprio validador que existe para pegar defeitos assim.

Ele também pegou, na hora, o rascunho do clash tomando número de peça. Rascunho não é peça, e o arquivo foi renomeado.

### Corrigido de método — três perturbações minhas eram inválidas

Ao testar o `conferir-manual.py`, rodei as cópias perturbadas de `/tmp`. **De lá ele não acha o `.docx`, avisa e pula as quatro checagens** — então as três primeiras perturbações saíram verdes sem terem conferido nada. É exatamente o alerta que o README dá sobre o `python-docx`, aplicado a mim.

Refeita no lugar certo, a perturbação acendeu. E ela achou um segundo problema: o teste genérico de *"está definido"* aceita qualquer frase com a palavra **é**, e quase toda frase em português tem uma. Para termos importados isso não basta — cada um agora declara o próprio padrão de definição.

### Adicionado — `refino` é termo importado, e o manual tem que defini-lo

A Expansão pôs uma palavra do projeto dentro do manual, que é a direção contrária do problema que a v0.26 consertou. O `conferir-manual.py` ganhou uma lista de **importados do projeto**: cada um entra com o lugar onde o manual o define, e o validador falha se a definição sumir. O manual define refino numa caixa de uma linha e não usa a palavra em mais lugar nenhum.

### Registrado — o clash ficou de fora, e está engatilhado

Um modelo de **push gradual** foi levantado a partir da obra: sobreposição de áreas anula o acerto garantido dos dois lados, e começa um empurrão cuja velocidade vem da diferença de refino, com vantagem para quem tem Acerto inofensivo e para quem está com a barreira aberta.

**Ele substitui uma regra marcada como fechada** — a resolução por `1d10 + aptidões + metade do nível` — e **pede seis números que não existem**. A parte mais interessante dele é a que mais preocupa: *efeito inofensivo empurra melhor* recompensa escrever um Acerto fraco de propósito, e sem número ninguém sabe se compensa.

Foi para `03-mecanica/RASCUNHO-clash-de-expansoes.md`, com os seis números nomeados e a ordem de atacá-los. A v7.7 cita a regra que já estava decidida.

### Registrado de método — o mount perdeu um arquivo que ele mesmo gravou

Fechando a versão, o `conferir-repositorio.py` acusou que o `README.md` não existia. Ele existia: `ls` e `stat` devolviam tamanho e inode certos, e o nome não tinha caractere estranho — mas `open()` devolvia **ENOENT** para o `head`, para o Python e para o `git` igualmente, enquanto **os vizinhos na mesma pasta abriam normalmente**. As ferramentas de arquivo liam o conteúdo certo o tempo todo.

Ou seja: **o arquivo estava íntegro no disco, e quem não o enxergava era o mount FUSE do sandbox.** Nenhuma tentativa de reconciliar resolveu — `sync`, relistar o diretório, caminho absoluto, reentrar na pasta. **Reescrever o arquivo inteiro resolveu**, porque criou um objeto novo.

É primo do problema do `git commit` que o README já documentava, e agora está escrito ao lado dele. Fica registrado porque o sintoma engana: parece arquivo apagado, e é o oposto — o conteúdo nunca esteve em risco.

### Alterado — o README ganhou uma sétima lição

> **Um número que mora em dois documentos vai divergir.** Não é "se", é "quando" — e cada cópia precisa de um dono declarado ou de um validador que compare as duas.

Ela sai desta versão de dois lados ao mesmo tempo: o `conferir-repositorio.py` guardava `sete` no código, e o manual e o projeto contavam feitiço por calendários diferentes desde sempre. As duas são a mesma doença.

E o aviso sobre `python-docx` ganhou um par: **os três validadores que leem o `.docx` também pulam em silêncio se forem rodados de outro diretório.** Foi assim que três perturbações desta versão saíram verdes sem terem conferido nada.

### Em aberto

- **As quatro anti-domínio**, agora destravadas. É a próxima da fila.
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Qual modelo de clash vale**, e os seis números do push.
- **A aptidão que baixa a Expansão para Ação Bônus** — citada, não escrita.
- **Nome do sistema.**

---

## [0.27] — 2026-08-11

A peça de aptidões, que o `arquitetura.md` chama de *"o risco maior da estrutura inteira"*. Ela sai **com quatro das catorze entradas em branco**, e isso é decisão: elas contam o Acerto de uma Expansão de Domínio, e a Expansão só ganha regra na v7.7 do manual.

**Sétimo validador.** E a escolha de marco deixou de ter duas opções.

### Adicionado — `03-mecanica/11-aptidoes-e-refino.md` e `conferir-aptidoes.py`

Sete checagens, e sete perturbações conferidas: aptidão escalando eixo proibido, o divisor de cobrir-se deixando de dar +3, a Reação com saldo negativo, kokusen grande demais para ser só grito, gate de refino que não separa as rotas, Passiva grátis deixando de ocupar vaga, e a linha passiva do marco removida.

### Decidido — o refino é a métrica geral das aptidões, e a trava é outra

Até aqui o refino era um contador. Ele subia nos marcos, tinha teto 10 e destravava aptidão — e **entre um refino 3 e um refino 10, no mesmo nível, com as mesmas aptidões, nada mudava na ficha.** A intenção estava escrita no `arquitetura.md` desde a Fase 3 (*"o refino governa confiabilidade e custo"*) e nunca tinha virado número.

Agora ele é requisito **e** tamanho, e entra no texto de cada aptidão **como variável**, no molde que o manual já usa para `sua maior Classe`. Cada aptidão declara o próprio teto — nem toda uma usa o valor cheio.

**A trava proposta pelo `arquitetura.md` era *"aptidão não produz dano e não escala com nível"*, e ela foi escrita antes de existir régua.** Com a régua das Classes, a que importa é outra, e ela vem da regra que governa o sistema:

> **O refino cresce +7 a +9 numa campanha; atributo e maestria crescem +3.**
> **Então ele não pode aparecer de um lado de uma rolagem em que o outro lado não cresce no ritmo dele.**

Isso proíbe acerto, CD, defesa, Teste de Resistência e dano — os cinco têm do outro lado alguém que cresce +3. **E permite refino contra refino**, que é simétrico: o clash de expansões passa por isso e não deriva.

### Decidido — o marco ganhou um terceiro eixo, o Leque

> **Passivo:** +1 atributo, +1 refino e **+1 espaço de feitiço**.
> **Escolha:** **Corpo** (mais atributo) · **Refino** (mais refino e uma aptidão) · **Leque** (mais um feitiço, que só pode ser feitiço, e uma Passiva).

**O problema que ele resolve é real e era maior do que parecia.** Passiva custa espaço de feitiço, e a Expansão também. Sem rota que devolva espaço, três Passivas de Classe 2 mais a Expansão completa chegavam ao **nível 20 com dois feitiços** — e a montagem cheia que o manual permite, cinco Passivas de Classe 3 mais Expansão, pedia 18 espaços numa ficha que tinha 16. **O teto de "cinco Passivas pagas" do manual já era letra morta:** quem escrevesse cinco Classe 3 descobriria no meio da campanha que não cabia.

Com a linha passiva do marco, a montagem típica sai de dois feitiços no nível 20 para sete, e a mais pesada passa a caber **a partir do nível 22**.

**As três não precisam de trava, e o motivo é bonito.** Passiva e aptidão vivem na **mesma escada de Classe**, então `+1 feitiço e 1 Passiva` empata com `+1 refino e 1 aptidão`. O que sobra dos dois lados é `+1 feitiço` contra `+1 refino` — e **refino não vale nada para quem não tem aptidão**. Quem escolhe Leque não quer refino; quem escolhe refino não quer Passiva. Nenhuma compra o que a outra compra.

**O teto de Passivas sobe, e a grátis traz a própria vaga.** Cada escolha de Leque aumenta o máximo em um, e a Passiva concedida ocupa a vaga nova — então as **pagas continuam sendo cinco**. O teto não cresce; ele abre lugar.

*Uma primeira leitura desta regra somava as duas coisas e chegava a **dezenove** Passivas numa ficha. Estava errada, e é a mesma família da lição nº 2: o teto já incluía o que eu estava somando nele.*

### Corrigido — o manual e a peça 8 discordavam em dois feitiços

O manual: *"a conta fecha em treze feitiços conhecidos no nível 20"* e *"ganha uma nova a cada dois níveis"*. A peça 8: *"no nível 2 você tem dois feitiços conhecidos"*. Dois no nível 2 mais um a cada dois níveis dá **onze** no nível 20.

> **Feitiços conhecidos = `2 + (nível ÷ 2)`, arredondando para baixo — mais um por marco.**

Três no nível 2: dois de toda ficha, mais o do próprio nível 2. **A confusão vinha de a ficha nascer no nível 2** — o nível 1 é quem ainda está entrando no mundo jujutsu, civil ou com a técnica sem despertar. Doze no nível 20, e o manual corrige o treze na v7.7.

### Decidido — a Classe de aptidão mede formato, não tamanho

Se ela medisse tamanho, a escada colapsaria: um marco compra uma aptidão de qualquer Classe destravada, então do nível 13 em diante **toda escolha seria Classe 3** e o especialista terminaria com sete aptidões, cinco delas Classe 3, sem nunca ter olhado para uma Classe 1.

**A Passiva do manual não tem esse problema porque ela tem preço** — Classe 3 custa três espaços, então você troca uma por três Classe 1. A v0.25 herdou metade da régua: o gate e o tamanho do efeito, sem o preço que faz os três degraus competirem.

**O que resolve é o refino.** Com ele escalando o que a aptidão entrega, **uma Classe 1 no refino 10 não é a mesma coisa que no refino 2** — e aí a Classe volta a dizer o que o manual sempre disse que ela dizia: *pequeno e condicional · reativo com limite · permanente*. Não são mais e menos; são formatos.

### Decidido — o gate é por aptidão, e não pode ser só nível

Cada aptidão declara o próprio requisito: nenhum, só nível, só refino, ou os dois.

**Só nível não serve**, e a conta mostra: quem escolhe refino **uma vez, no nível 26**, compraria uma Classe 3 na hora — o mesmo acesso de quem investiu seis vezes. Com gate de refino, a Classe 3 abre no nível 14 para o especialista e no **26** para o generalista. Doze níveis, que é o tamanho que *"quase ninguém consegue"* pede.

**E guardar marco não guarda refino.** A rota que espera — atributo cedo, refino tarde — não domina, porque o refino passivo sobe sozinho: ela chega ao nível 22 com refino 5 e ainda precisa de outro marco para o 7. Troca quatro aptidões por quatro pontos de atributo.

### Escritas — as seis que têm número

**Cobrir-se de energia.** Proteção `1/3 do refino + 1` sem uniforme, e como Reação uma RD de `1,5 × refino` gastando PE, ao custo da proteção por um turno.

O **1/3 não é escolha de gosto: é o único divisor que cabe.** Ele cresce de 0 a 3 na campanha, exatamente como um atributo. Com o refino cheio o atacante cairia de 50% para **5%** de acerto no nível 22 — a deriva da v0.9 pelo lado defensivo.

E o **1,5 ×** é o que impede a Reação de virar armadilha. Com `1 × refino` ela fica **negativa do nível 22 em diante**: o custo de um turno sem proteção cresce com o golpe do chefe enquanto a RD trava no teto. Com 1,5 o saldo fica positivo do começo ao fim e **encolhe** em vez de virar.

*Recado para a peça de equipamento:* no refino 10 ela dá proteção 4, e um Vanguarda que largue o uniforme chega a Defesa 20 contra os 17 dele fardado. **Um uniforme precisa valer mais que 4.**

**Canalizar energia** não é escalada pelo refino — ela vive inteira no orçamento do Fundamento, e é o exemplo mais limpo de teto por aptidão.

**Projetar energia** entrega `dano = refino`, entre **8% e 12% da coluna Rotina** do nível 2 ao 30. É o único lugar do catálogo onde o refino toca dano, e ele **deriva para baixo**, porque a vida do inimigo cresce mais rápido que ele.

**Kokusen** a `2 × refino` no d100, com **+50% no impacto depois de tudo resolvido**. Teto de **1,8%** de dano por rodada no refino 10 — menos de um quinto do que um ponto de atributo compra. **Kokusen Melhorado** dá **vantagem no d100**, que ganha do `3 ×` em todo refino (36% contra 30% no teto), e a terceira sobe a base para `3 ×`.

**E o kokusen tem proteção contra azar.** No refino 1 a espera pelo primeiro seriam **47 sessões**, o que na prática é nunca. Cada d100 falhado empurra o próximo em +2, e o acumulado **zera no descanso longo** — o refino 1 cai para ~9 sessões e o refino 10 quase não se move. *Por cena não serviria:* o acúmulo só começa no segundo crítico da mesma cena, e dois críticos no mesmo combate acontecem em **4,4%** das vezes.

**A cascata mexe só na chance, e nunca na margem.** Dobrar a chance no refino 5 rende +0,9 ponto; fazer a margem cair para 19 rende **+10,9%**, dos quais **9,1 vêm do dado a mais** — a margem carrega o crítico inteiro junto. E sem teto, quatro degraus numa cena levariam o físico a **1,8× o dano base**.

### Adicionado — o Limiar

Vem do dossiê, seção 2: **gatilho de ficção antes da rolagem**, roubado do PbtA e do FitD. Mecânica separada, declarada pelo mestre, e o kokusen é só um dos lugares que a citam. *Faísca* morreu na triagem dentro de *Faísca em Cadeia* e *Impulso* é Melhoria do manual; **Limiar** está livre nos dois lados.

**O cardápio sai sem número, por decisão** — mas o tamanho fica registrado na peça, porque ele não é plano. Contra o alvo difícil, rerrolar e dar vantagem valem os **mesmos +25 pontos percentuais**; "acontece mesmo errando" e "sucesso garantido" valem **o dobro**. E as duas famílias correm em sentidos opostos: a vantagem é auto-regulada e dá 9 pp contra alvo fácil, enquanto o garantido vale **75 pp** contra CD alta — justamente quando alguém vai querer dar.

**Nota de método registrada e não resolvida:** o dossiê defende o gatilho de ficção *contra* a discricionariedade. Aqui a escolha foi a outra, e o `arquitetura.md` sustenta — *"discricionariedade na ficção é o trabalho do mestre e não atravessa mesas"*. Vai para o playtest junto da contagem de lutas, que é a mesma aposta.

### Registrado — o que ficou fora, e por quê

**Quatro das catorze estão bloqueadas.** Domínio Simples, Pétala, Cesta Oca de Vime e Extensão de Domínio contam o **Acerto** de uma Expansão, e a Expansão vai para o manual na v7.7. Escrever o preço delas agora seria precificar contra alvo que não existe — o erro que a v0.24 registrou no ataque extra.

**E o laço entre as duas é o que torna as duas possíveis.** A Expansão completa acerta **garantido**, e é isso que o terceiro espaço compra. Um acerto que nunca falha só é jogável porque a resposta é barata: os quatro anti-domínio são **aptidões de marco**, ao alcance de qualquer ficha que escolha o eixo do controle. Se fossem raros, o garantido seria opressivo. A decisão de pôr os quatro no catálogo foi tomada antes de a Expansão ter forma.

**A Expansão, decidida e não escrita:** incompleta custa **2 espaços**, nível 10 e refino 4; completa custa **+1** (três no total), nível 14 e refino 6, e **exige ter a incompleta** — o molde é o da Regra Própria do manual, que sobe de Classe *"pagando só a diferença de espaços"*. Nos dois gates o **meio a meio passa com folga zero**, e isso pede validador quando a peça existir.

### Registrado — as Bênçãos e a Lapidação

A Restrição Celestial pelo ramo da Maki e o Corpo Amaldiçoado não têm energia — sem PE, sem golpe canalizado, sem Sentir Energia — então não têm aptidão nem refino. Eles ganham **a mesma máquina com outra métrica**: as aptidões viram **Bênçãos** e o refino vira **Lapidação**. Andar em parede e em água, deslocar-se no ar, *fast steps*. Os dois nomes passaram pela triagem.

É a camada de aptidão da **Técnica Marcial**, e ela destrava duas das três rotas de Origem que não rodam hoje.

### Alterado

- `02-economia-de-atributos.md` ganhou aviso na seção 3: a escolha de marco tem três opções desde esta versão, e a análise de auto-equilíbrio dela foi feita com duas.

### Em aberto

- **As quatro anti-domínio**, e a peça da Expansão que as destrava.
- **Energia Reversa, Barreira Simples, Cortina** e a régua da Aptidão Própria.
- **Se alguém escolhe o Leque.** Se ninguém pegar, o aperto que ele resolve continua resolvido pela linha passiva, e aí ele sai.
- **Se doze Passivas pesam na mesa.** O manual escolheu cinco por peso, não por orçamento.
- **Nome do sistema.**

---

## [0.26] — 2026-08-10 · *manual v7.6*

Os quatro buracos de regra que a v0.24 registrou e ninguém tinha escrito. Um deles a conta respondeu sozinha, e ao ir atrás dele apareceram três problemas maiores do que os quatro: um órfão de vocabulário dentro do manual, duas regras que apontavam para Testes de Resistência diferentes sem ninguém ter notado, e a Casca — que morreu por três motivos, e nenhum era o que estava escrito no changelog anterior.

**Seis validadores agora.** O sexto olha a direção que faltava.

### Corrigido dentro da própria versão — o manual não é lei, e eu tinha escrito que era

Duas frases desta versão davam ao manual uma autoridade que ele não tem: *"a fórmula já estava no manual"* e *"não é escolha nossa"*. **Os limitadores, exemplos e tabelas do manual foram calibrados quando o sistema em volta era outro.** Eles servem de base para continuidade — e é bom que estas mudanças estejam acontecendo agora, com estrutura em pé —, mas não valem ao pé da letra.

Isso não muda nenhuma decisão desta versão. Muda o **motivo** de duas delas, e muda o que o validador novo afirma.

Levantando a exposição real, **dez decisões do projeto estão penduradas em três tabelas do manual** — e elas não são iguais entre si:

| tabela | dono | por quê |
|---|---|---|
| **PE** — *"quantas vezes você lança"* | **o projeto** | nada exige que o Emanador tenha 6. O que exige é que a coluna diga a verdade sobre a ficha. Mudou o 6? Regere a coluna |
| **Rotina** — dano por rodada por Classe | **o manual** | ela não é medida, é a **definição** de "quanto é normal". Não há verdade fora dela: o projeto compara tudo contra ela, inclusive ela mesma |
| **Inimigo** — chefe e capanga por nível | **o playtest** | é a única das três que afirma alguma coisa sobre o mundo: que um combate dura ~3,5 rodadas. A trava de vida inteira da peça 1 foi calibrada contra ela, e ninguém é dono dela até alguém jogar |

**Duas das três não correm risco de estar desatualizadas, porque não afirmam nada — elas *são* a régua.** A terceira corre, e é exatamente a que o playtest mede primeiro.

A checagem 4 do `conferir-manual.py` foi reescrita em cima disso. Ela deixou de dizer *"o projeto copiou daqui, então tem que bater"* e passou a dizer **"os dois lados divergiram, e aqui está quem decide"** — a mensagem de erro nomeia o dono e o custo de mexer. Divergência virou pedido de decisão, e não veredito.

### Achado — a fórmula do PE máximo, e o quanto o manual conta como argumento

O buraco dizia: *"o PE máximo nunca teve fórmula escrita — só a instância do nível 2 na peça 8, e não dá para inferir da vida, que usa `(nível − 1)` e soma atributo."*

> **PE máximo = PE por nível do Caminho × nível.** Sem atributo, sem valor inicial.

Sem atributo pelo motivo da peça 1, seção 9: um atributo na conta de PE viraria o atributo obrigatório de todo conjurador pela porta dos fundos. Sem valor inicial porque é o que faz esta ser a única reserva que passa pela origem — a vida tem inicial e soma atributo, a Integridade tem inicial.

**E o manual concorda.** A tabela dele mostra 6, 30, 54, 78, 102 e 120 nos níveis 1, 5, 9, 13, 17 e 20, todos `6 × nível` exatos. Concordar não é mandar, pela seção acima — o que a concordância compra é que **a coluna "quantas vezes você lança" continua dizendo a verdade sobre a ficha sem precisar ser refeita.**

### Decidido — arredondamento, e a frase que reconcilia os precedentes

Cai em fração em quatro lugares, e a **Vanguarda e o Guia caem na primeira parada da primeira sessão**: 25% de uma pool de 10 é 2,5.

> **Arredonde sempre para o lado que não te favorece.** O que você paga sobe, o que você ganha desce, e o que você ganha nunca fica abaixo de 1.

Não é escolha nossa. É o princípio que o manual declara na caixa *"na dúvida, para que lado errar"* — *"os dois erram pro mesmo lado: o que não infla o feitiço"* — aplicado a número em vez de a preço. E ele explica por que os dois precedentes que existiam não estavam brigando: o manual arredonda para cima no preço de Melhoria e no +50% da Liberação, que são coisas que você **paga**; o exemplo da peça 10 arredonda para baixo, e é recuperação.

**O piso de 1 não desfaz um zero escrito.** O degrau 3 de exaustão devolve *nada*, e nada é zero. O piso existe para a conta que produziu 0,4.

**E um caso que parecia exceção e não é.** A vida por nível do Caminho é a média do dado arredondada **para cima** — d12 vira 7, d8 vira 5, d6 vira 4 —, e isso é um ganho subindo. Ela não quebra a regra porque **não é conta de mesa**: é valor de tabela, decidido uma vez no desenho. A regra vale para o número que cai na mão de quem está jogando. O validador agora confere as duas coisas separadamente, para o dia em que alguém tentar "consertar" a tabela aplicando a regra nela.

**Efeito colateral registrado:** com o piso de 1, os degraus 1 e 2 de exaustão devolvem o mesmo PE enquanto a pool é pequena — separam no nível 3 em quatro Caminhos e no 4 no Bastião. Os outros dois eixos do degrau continuam diferentes desde o nível 2, então a escada nunca fica plana de verdade. O validador passou a exigir que a coluna seja **não crescente**, e não estritamente decrescente.

### Decidido — o que conta como uma luta

> **Quem conta é o mestre, e ele conta como em qualquer mesa: foi uma luta se pareceu uma luta.**

Não depende de ter rolado iniciativa, e não é só maldição — feiticeiro contra feiticeiro cansa igual. A peça traz exemplos, e eles são exemplos e não lista fechada.

**Isso é diferente do ambiente propício de propósito, e vale registrar o motivo.** Lá a lista é fechada e o mestre tem a palavra final em cima dela. Aqui não. *"Esse lugar tem kit e comida?"* é pergunta sobre o mundo, e a mesma resposta serve para qualquer mesa; *"isso foi uma luta?"* é pergunta sobre a cena que aquele mestre acabou de dirigir. Fica marcado para o playtest: **medir se dois mestres chegam ao mesmo número de degraus no mesmo tipo de missão.** Se não chegarem, a saída é a do ambiente propício — fechar a lista.

### Corrigido — a exaustão nunca esteve desordenada. O texto é que prometia errado

O achado da v0.24 dizia que *"a exaustão está ordenada por onde dói, não por quanto"*, e que o degrau 1 é maior do que o texto promete. A primeira metade estava certa e a segunda estava mal formulada.

Desvantagem é rolar 2d20 e pegar o menor: a chance `p` vira `p²`, e a perda `p − p²` é máxima exatamente em 50%, onde vale **25 pontos percentuais**. Como o degrau 1 e o degrau 3 são os dois desvantagem, os dois tiram **exatamente os mesmos 25 pp**. Não existe "degrau leve" numa escada em que dois dos três degraus usam a mesma mecânica.

| degrau | eixo | tamanho no pico | a falha custa |
|---|---|---|---|
| 1 | perícia e ofício | −25 pp | a cena anda |
| 2 | deslocamento, 9 m → 6 m | −33% de alcance | posição |
| 3 | ataque e Teste de Resistência | −25 pp | dano, e às vezes a vida |

**A escada é ordenada por consequência, e sempre foi.** Falhar em perícia move a cena, porque a peça 4 proíbe falha que trava; falhar em ataque perde a luta. O conserto não era mexer no número: era o texto parar de vender o degrau 1 como pequeno e passar a dizer que ele é do mesmo tamanho e cai em cima do que não mata. O `conferir-descanso.py` agora confere **magnitude**, e falha se alguém escrever um degrau de desvantagem como se fosse menor.

Para escala: um degrau de exaustão é **maior que treinar um Teste de Resistência** (10 pp), **maior que a maestria de uma campanha inteira** (20 pp) e **maior que sair de atributo 0 para 3** (15 pp).

### Decidido — exaustão e Integridade, pega o pior

As duas escadas nunca tinham sido postas uma do lado da outra. São quase a mesma escada:

| | exaustão (peça 10) | Integridade (manual) |
|---|---|---|
| degrau 1 | desvantagem em perícia e ofício | desvantagem em testes de perícia |
| degrau 2 | deslocamento cai para 6 m | deslocamento pela metade, e +1 PE por Classe |
| degrau 3 | desvantagem em ataque e TR | desvantagem em ataque e TR, e teto de Classe |

> **Quem está nas duas pega o pior, não soma.**

Isso não inventa nada — desvantagem não empilha com desvantagem em mesa nenhuma. A regra existe para escrever o que a mesa já faria, em vez de deixar a pergunta aparecer no meio de uma missão longa. O que só a Integridade tem (o +1 PE por Classe e o teto de Classe) não compete com nada e simplesmente acontece.

**E os 6 m contra os 4,5 m ficam diferentes de propósito:** a Integridade é dano de alma e deve doer mais. Se as duas dessem o mesmo corte, a alma estaria cobrando o preço do cansaço. O validador falha se a Integridade deixar de cortar mais.

### Adicionado — `conferir-manual.py`, o sexto validador, e a direção que faltava

O `conferir-nomes.py` olha **projeto → manual**: *"esse nome que eu batizei já significa alguma coisa lá?"*. Ninguém olhava o contrário. É por isso que o `Bônus de Treinamento` da Passiva Reforço sobreviveu até a v0.25 — e por isso que a Fraqueza sobreviveu até agora.

Quatro checagens: **vocabulário órfão** (palavra de outro sistema, tolerância zero), **teste nomeado pelo atributo** em vez do Teste de Resistência, **termo mecânico usado e nunca definido** (com os aceitos declarados com motivo, no padrão do `conferir-pericias.py`), e — a que ninguém teria escrito à mão — **os números que o projeto importou do manual**. A tabela de PE, a de inimigo e a coluna Rotina estão **copiadas** dentro das peças e dos outros validadores; se o manual for regerado e um deles mudar, o projeto passa a mentir em silêncio. Agora ele grita.

Testado nos dois sentidos: com o manual v7.6 limpo ele sai com código 0, e **seis perturbações** — Sabedoria de volta, teste nomeado pelo atributo, `dano físico` de volta, e um número mexido em cada uma das três tabelas importadas — acenderam cada uma a checagem certa. Somando com as extensões do `conferir-descanso` e do `conferir-atributos`, foram **dezesseis perturbações conferidas** nesta versão.

### Achado — a Restrição Fraqueza carregava dois órfãos numa linha só

> *"Depois de usar, você fica com desvantagem em Testes de Resistência de uma **Habilidade**, escolhida na montagem, até o fim da cena. Habilidade pouco testada na sua mesa: Leve. Constituição, Destreza ou **Sabedoria**: Média."*

**Habilidade** aqui são atributos. **Sabedoria** não existe — ela e o Carisma fundiram em Essência antes de a Fase 4 começar. E o defeito é pior do que vocabulário: o preço citava **atributo**, e os Testes de Resistência daqui são quatro, com o Físico usando Força **ou** Destreza. A tradução não era um para um, e um terço da regra de preço apontava para o nada.

Preço novo: **Vigor ou Intelecto, Leve. Físico ou Espírito, Média.**

### Achado — Concentração e Carregar apontavam para testes diferentes, e um dizia ser o outro

A peça 3 diz que Concentração é **Teste de Resistência Físico**. O manual diz que Carregar é **"teste de Constituição"**. E a peça 3 ainda afirmava, com todas as letras, que *"é a mesma régua que a Restrição Carregar já usa"*. A régua da CD era; o teste não.

Ao abrir os dois, apareceu que **eles não deviam ser a mesma regra**, e a diferença já estava escrita há versões sem ninguém ler: em Concentração *"o efeito cai"* — você tinha, e perdeu. Em Carregar *"perde o feitiço"* — ele ainda não tinha saído. O único fio que os fazia parecer iguais era a palavra **"concentrado"** dentro do texto do Carregar.

| | o que você segura | teste | falhar custa |
|---|---|---|---|
| **Concentração** | o efeito que já está no ar | **Vigor** | o efeito cai |
| **Carregar** | o feitiço que ainda não saiu | **Espírito** | o feitiço, e o que você pagou por ele |

A frequência foi conferida antes de mexer: Concentração é exigida pela Melhoria **Fica**, que **1 dos 35 feitiços prontos** usa, e por Carregar, que **nenhum** usa. Então pôr Concentração em Vigor quase não muda a frequência dele, e o argumento *"o TR Vigor quase não rola"* — que a peça 10 usa e que sustenta o Leve da Fraqueza nova — continua de pé.

A Passiva **Mão Firme** passou a dizer *"não perde concentração **nem carga**"*, explícito, porque com a divisão o nome dela sozinho não alcançava mais o Carregar.

É a terceira vez que a lição do Carregar se paga: **tensão de preço às vezes é lacuna de texto disfarçada.** A v0.11 resolveu o par Lento-contra-Carregar escrevendo uma frase; agora uma palavra dentro do mesmo item resolveu outro problema, e nenhum preço precisou mudar.

### Decidido — a Casca morreu, e por três motivos que não eram o que estava escrito

A v0.25 deixou pendente: *"a Passiva **Casca** cai na mesma regra e não foi mexida"*. Rodando a conta antes de decidir, o motivo escrito era o menos importante dos três:

**`dano físico` aparece uma vez no manual inteiro — dentro da própria Casca.** Não é categoria definida em lugar nenhum, e os tipos de dano do manual são livres (*"corte, fogo, peso, o que a Descrição pedir"*). Dois mestres leem diferente, e um deles dá RD contra tudo que é soco.

**RD corta o mesmo valor de cada golpe, e o manual dá dano por rodada.** Nunca quantos golpes. A Casca valia de **6% a 42%** conforme um número que não existe em lugar nenhum do material.

**E a Melhoria Fura ignora `3 × Classe` de RD.** Um ponto numa Classe 1 já apagava a Casca inteira, em qualquer nível. Contra quem comprou Fura ela era zero.

> A Passiva **Casca** foi deletada. No lugar dela entra a **Escama**: *escolha um tipo de dano que a sua Regra justifique; você tem resistência a ele.*

**A Escama não é uma Casca mais fraca — é outra aposta.** Resistência é metade, então ela vale **5 a 9 vezes mais** que a Casca quando o tipo bate, e **zero** quando não bate. O ponto de virada é **1 luta em 4**: acima disso ela é a melhor Passiva de Classe 3 da lista, abaixo é a pior.

**A trava que impede a otimização é a que estava na escolha desde o começo:** o tipo é preso à Regra, e a Regra é escrita na **criação**, antes de qualquer um saber o que a campanha vai mandar. O jogador aposta; ele não escolhe o tipo que o mestre mais usa, porque ainda não sabe qual é. E o julgamento que a palavra *"justifique"* introduz cai no mesmo momento em que a técnica já é aprovada — a trava nº 3 de mundo compartilhado obriga alguém que não é o dono a ler a Regra —, então ele não atravessa mesas.

O nome passou pelo `conferir-nomes.py --candidatos` junto com onze outros. **Berço** está dentro de *Treino de Berço* e **Familiar** fica a uma letra de *Família*; os dois morreram na triagem antes de entrar em qualquer arquivo.

E ela nasce com **dois counters que já existiam**: a Melhoria **Corrói** cancela resistência ao tipo, e a Passiva **Afinidade** ignora resistência ao tipo. A peça defensiva nova não precisou de contrapeso novo.

**A regra que matou as duas foi escrita onde a próxima pessoa vai procurar** — a lista *"o que nenhuma Passiva paga pode fazer"* do manual ganhou uma quinta linha: *"Redução de Dano passiva… Resistência a um tipo, sim — é o que a Escama faz. Desconto em tudo, não."*

### Decidido — "resistência" ganhou definição

Ela era usada **três vezes** no manual — Afinidade, Corrói, Purga Escarlate — e **nunca explicada**. Mesma família do `dano físico`, e trocar um termo indefinido por outro não seria conserto.

> **Resistência: o dano daquele tipo cai pela metade, antes de qualquer outra conta. Sempre presa a um tipo — não existe resistência a tudo.**

Metade é a única leitura que **não deriva**: sendo proporcional, ela vale o mesmo no nível 13 e no 30. As alternativas de valor fixo encolhem conforme o inimigo cresce, que foi exatamente o que aconteceu com a Casca — **−6,1% no nível 13 e −5,6% no 30**, com o número tendo *dobrado* no meio do caminho.

### Registrado — o Kokusen Melhorado tem preço e requisito

As duas pendências da v0.25 fecharam juntas, porque a segunda responde a primeira:

> **É aptidão, e custa um marco. O requisito é refino 5 e nível 14.**

O requisito deixa de ser sorte. Pelo mesmo motivo, ele deixa de ser a mesma coisa para duas fichas idênticas — o antigo *"ter tirado um kokusen"* travava o jogador por dezenove sessões no refino 1.

Refino 5 cai no nível 10 para quem sempre escolhe refino, no 14 para quem vai meio a meio e no 18 para o generalista; o nível 14 é o que faz as duas primeiras rotas convergirem no mesmo marco. **Um mínimo de nível abaixo de 10 não morderia** — o refino 5 já chega lá.

**E o preço continua ruim de propósito.** A ~2% de dano por rodada, ele vale **0,2× um ponto de atributo**, que compra +10%. Numa campanha com no máximo sete aptidões e mediana perto de três, ninguém que olhe o número escolhe. Escolhe quem escolhe pelo grito — que é exatamente o que a v0.25 registrou que ele é, e o texto dele precisa dizer isso para ninguém montar ficha em cima.

**E o efeito apareceu, no fim da versão:**

> **Kokusen: +50% no impacto, depois de todos os valores resolvidos.**

Ou seja, em cima do crítico que já dobrou os dados — um crítico entrega `2D`, um kokusen entrega `3D`. Com o efeito na mão, a conta da v0.25 sai diferente:

| refino | chance no d100 | dano por rodada | sessões até o primeiro |
|---|---|---|---|
| 1 | 5% | +0,5% | 19,5 |
| 3 | 15% | +1,4% | 6,8 |
| 5 | 25% | +2,3% | 4,3 |
| 10 | 50% | **+4,5%** | 2,4 |

O teto é **4,5%**, e não os *"menos de 4%"* que a v0.25 registrou — aquele número foi calculado antes de o efeito existir. **A conclusão não muda:** continua sendo um quinto do que um ponto de atributo compra, e continua sendo peça de grito e não de planilha. O que muda é que agora dá para escrever validador em cima.

### Corrigido de método — dois erros meus, na revisão cética

O primeiro: uma versão da seção 5.3 dizia que o PE *"cresce mais rápido que a vida"*. Não cresce — o passo do PE é 4 a 6 por nível e o da vida é 7 a 10 com Constituição típica. O que sobe é a **razão** entre os dois, de 0,75 para 0,85 num Emanador, porque a vida perde um nível na parte que escala. **É a lição da v0.19 pela quinta vez: o número certo contra a base errada.**

O segundo achou uma contradição de verdade. A primeira redação da regra de arredondamento citava *"a vida por nível do Caminho"* como precedente do manual de arredondar para cima. Ela não é do manual — é nossa — e, pior, ela é um **ganho subindo**, que é o oposto do que a regra nova manda. A regra só fecha porque vale para **conta de mesa** e não para valor de tabela, e essa frase precisava estar escrita.

### Registrado — a cascata de kokusen é realimentação, e ela precisa de teto antes de existir

A ideia é a da obra: *o segundo kokusen num intervalo curto é mais fácil que o primeiro.* Quatro jeitos de fazer isso foram levantados, e **eles não são da mesma família.** Medidos no refino 5, depois do primeiro kokusen da cena:

| escada | dano por golpe | contra a linha de base |
|---|---|---|
| nada muda (o de hoje) | 0,5625 | +2,3% |
| ajuda no d100, +25 pontos | 0,5750 | +4,5% |
| dobra a chance, 25% → 50% | 0,5750 | +4,5% |
| vantagem no d100 | 0,5719 | +4,0% |
| **margem de crítico cai para 19** | 0,6250 | **+13,6%** |
| **margem cai para 18** | 0,6875 | **+25,0%** |
| **vantagem no ataque** | 0,8719 | **+58,5%** |

**As três primeiras mexem só no kokusen, e o kokusen é pequeno** — dobrar a chance dele rende 2,3 pontos. As duas últimas mexem em coisas que já valem sozinhas: a margem de crítico carrega os 10% do próprio crítico, e **9,1% do +13,6% vêm do dado a mais, antes de o kokusen entrar**; vantagem no ataque sobe o acerto de 50% para 75%, o que já é meio jogo de dano a mais.

**E "mais fácil depois do primeiro" é uma espiral, com o sinal trocado.** É o mesmo desenho que a v0.8 e a v0.23 diagnosticaram na exaustão: kokusen facilita kokusen facilita kokusen. Sem teto, quatro degraus numa cena levam o físico a **1,8× o dano de base** — e a coluna Rotina não tem para onde correr, então a tabela de encontro para de valer no meio da luta.

As três travas que a estrutura já usa e que servem aqui: **teto de degraus** (a exaustão para em três), **relógio curto** (a escada zera quando a cena acaba, no molde do "por cena"), e **uma escada só** — mexer na margem *ou* na chance, nunca nas duas, porque juntas elas se multiplicam.

### Em aberto

- **Nome do sistema.**
- **Qual escada de kokusen, e com que teto e que relógio.** A conta está acima; a escolha é de sabor.
- **Se cinco mestres contam luta parecido.** Aberto de propósito, e é a única coisa da peça 10 sem lista fechada por baixo.
- **A pergunta maior continua aberta:** a peça de aptidões ou a ficha + quick-start jogável. Os quatro buracos saíram da frente, e o número mudou de lado — das dezessete coisas que uma ficha de nível 2 precisa, **doze existem**, e das cinco que faltam **nenhuma morde numa missão de nível 2**: proteção nasce em 0, Pactos é opcional, Trilhas e aptidões só valem do nível 6 em diante, e XP não é preciso para uma missão só. Das dez pendências que só a mesa responde, **as dez são de nível 2**.

---

## [0.25] — 2026-08-10 · *manual v7.5*

Levantamento antes de escrever a peça de aptidões. A conferida contra o manual achou seis colisões e dois defeitos dentro do próprio Fundamento, e as decisões do Mizuki fecharam quatro peças de regra que não existiam. **O manual foi regerado: v7.5.**

### Decidido — as aptidões herdam a régua das Passivas, e não uma nova

O manual já tem a escada que a segunda economia de poder precisava, e ninguém tinha olhado para ela:

| Classe | Custa | Libera no nível | O que cabe |
|---|---|---|---|
| Livre | nada | 1 | ficção pura: não rola dado, não muda número, não faz ninguém rolar |
| 1 | 1 espaço | 1 | efeito pequeno, condicional, ou de informação |
| 2 | 2 espaços | 7 | efeito reativo, com limite por cena ou por descanso |
| 3 | 3 espaços | 13 | permanente, muda como você joga |

Três degraus, com **gate de nível embutido**, já conferidos pelo `pac7.py`. O `arquitetura.md` pedia uma trava para as aptidões — *"não produz dano e não escala com nível"* — porque não tinha régua. Tem.

### Decidido — cura existe nas duas economias, e por isso os nomes tinham que mudar

A Passiva **Reversão** já era Energia Reversa: *"uma vez por descanso curto, gasta a ação e recupera 5 × a sua maior Classe"*. Se a aptidão desse cura de graça, ela mataria a Passiva na hora — a mesma dominância que a peça 4 usou para não deixar feitiço virar ataque de oportunidade.

**As duas ficam, porque são coisas diferentes.** A Passiva é a cura **inata**, que vem da técnica, no molde do toque de cura do paladino. A aptidão é a cura **aprendida**, que gasta PE e se usa com frequência, no molde do conjurador. Duas economias, dois preços, dois nomes:

> A Passiva **Reversão** virou **Recomposição**. A aptidão fica com **Energia Reversa**.

### Corrigido no manual — dois defeitos dentro do Fundamento

**O manual tinha um termo órfão de outro sistema.** A Passiva **Reforço** dizia *"reduz o dano em 3 × Bônus de Treinamento"* — número que não existe aqui, porque o nosso se chama **Maestria**. Uma ocorrência só, e o `pac7.py` não pegava porque ele confere números e não vocabulário. Mesma família do Grau, três versões depois.

**A Passiva foi deletada, e não corrigida**, por decisão de design: *não existe redução de dano passiva neste sistema.* Fica o aviso para a peça de aptidões, que ia querer exatamente isso.

> **Pendente:** a Passiva **Casca** (Classe 3) — *"Redução de Dano 2 contra dano físico, vira 4 no nível 15"* — cai na mesma regra e **não** foi mexida. Decidir antes de fechar a v7.6.

**Técnica Máxima não é Expansão de Domínio.** O manual dizia que *"numa técnica que é feita de domínio, o domínio **é** a sua Técnica Máxima"*. Não é: a Técnica Máxima é o topo da técnica inata, e o domínio é a mesma técnica estendida sobre o território em volta. Uma técnica de domínio continua tendo Técnica Máxima como qualquer outra.

E **Expansão não vai ser aptidão**: ela mora na criação de personagem, presa a um mínimo de refino e de nível, comprada trocando espaços de feitiço conhecido. É a primeira coisa no sistema que o refino destrava fora da lista de aptidões.

### Corrigido no manual — três nomes, porque a obra ganha do manual

As aptidões vêm da obra e não têm para onde fugir. Quem muda é o lado menos entranhado, que é a regra da v0.5 aplicada de novo:

| era | virou | por quê |
|---|---|---|
| **Tema** Barreira | **Bloqueio** | a aptidão **Barreira Simples** é nome da obra |
| **Melhoria** Barreira | **Anteparo** | três coisas mecânicas não podem chamar Barreira |
| **Passiva** Domínio | **Afinidade** | ela escolhe um tema da Regra e fura cobertura leve — não tem nada a ver com domínio, e as aptidões **Domínio Simples** e **Extensão de Domínio** são da obra |

**A prosa em minúscula fica.** *"Dano dobrado contra barreiras"*, *"cancela um efeito contínuo ou uma barreira"*, *"uma barreira que absorva antes da vida"* — essas três agora apontam **certo**, porque barreira passou a ser exatamente a coisa que a aptidão produz. O que saiu foram os dois termos definidos.

Mexeu também no feitiço pronto **Muralha** e em três lugares do `pac7.py`. Os dois validadores passam e a estrutura é 326 parágrafos e 76 tabelas — um parágrafo a mais que a v7.4, porque a linha do domínio virou duas.

**O `.pdf` continua na v7.4.** Ele é exportado à mão; o `.docx` e o `.zip` estão na v7.5.

### Adicionado — o crítico, que era usado e nunca tinha sido escrito

Zero ocorrências no material do projeto. O manual usa a palavra uma vez, na Melhoria **Estilhaço** (*"em crítico, ou quando o alvo erra o Teste de Resistência por 5 ou mais"*), sem definir. E a mecânica de Kokusen pendura inteira nele.

> **20 natural numa rolagem de acerto é crítico, e você dobra os dados** — os da arma se for arma, os da Classe se for feitiço ou golpe canalizado. Nada mais dobra.

Três consequências que caem da frase sem regra a mais: **só existe crítico onde existe rolagem de acerto**, então feitiço que resolve por Teste de Resistência nunca crita; **comprar Certeiro ou Inescapável custa o crítico**, o que vira escolha de montagem em vez de bug; e **o crítico vale exatos 10% de dano por rodada** contra o alvo difícil, em qualquer nível, porque a taxa de acerto não deriva.

O crítico **não estoura** o teto de `4 × Classe em dados`: o teto é sobre o que se monta, não sobre o que o dado produz.

### Registrado — o Kokusen é caça-níquel, e a conta diz o tamanho

A proposta é: crítico no corpo a corpo → role d100, tire `5 × refino` ou menos.

| refino | chance no d100 | por ataque | por combate | combates até o 1º | sessões |
|---|---|---|---|---|---|
| 1 | 5% | 0,25% | 1,7% | 58 | **19** |
| 3 | 15% | 0,75% | 5,1% | 19 | 6 |
| 5 | 25% | 1,25% | 8,4% | 12 | 4 |
| 10 | 50% | 2,50% | 16,2% | 6 | 2 |

**Raro é o ponto**, e isso está decidido. O que a conta acrescenta é o tamanho: mesmo no refino 10 o kokusen soma **menos de 4%** de dano por rodada — 1,5% no nível 6, 3,7% no 30. Ele existe pelo grito na mesa, não pela planilha, e o texto dele precisa dizer isso para ninguém montar ficha em cima.

**Dois problemas ficam abertos**, e os dois são do requisito e não da mecânica: *"ter tirado um kokusen"* trava o jogador por **sorte** — dezenove sessões no refino 1, e duas fichas idênticas com acesso diferente. E **Kokusen Melhorado** paga um marco inteiro por ~2% de dano, competindo com Energia Reversa, que salva vidas.

### Registrado — o curandeiro nasce frágil por construção

Energia Reversa pede Essência 4 e Inteligência 4. Com nove pontos e teto 3 na criação, começar 3 e 3 gasta **seis dos nove** — sobram 1, 1 e 1 para Força, Destreza e **Constituição**, que é a maior alavanca de sobrevivência do sistema. Quem só escolhe refino chega a 4 e 4 no nível 10, e a 5 no nível 14.

Não é defeito: é o custo aparecendo onde deve. Mas é o número a olhar quando alguém reclamar que o curandeiro morre primeiro.

### Em aberto

- **Nome do sistema.**
- **A Passiva Casca**, que é a redução de dano passiva que sobrou.
- **O requisito do Kokusen Melhorado**, que hoje depende de sorte.
- **Se Kokusen Melhorado vale um marco** por ~2% de dano.

---

## [0.24] — 2026-08-08

Revisão cética do material inteiro em três camadas, antes de abrir a peça de aptidões. Os quatro validadores passam. Achou onze erros de texto, três buracos de regra e seis colisões de nome — metade delas nunca vista, porque nenhum validador olhava para lá.

### Adicionado — `conferir-nomes.py`, o quinto validador

O `conferir-pericias.py` já fazia checagem de colisão, **com 33 nomes**: as 23 perícias e os 10 ofícios. O projeto batizou muito mais — 15 Trilhas, 5 Caminhos, 14 Legados, 8 Origens, os termos de sistema. Nada disso passava por lugar nenhum, e foi por isso que três colisões ficaram no material desde a v0.14.

Cinco checagens: colisão para fora (contra o `.docx`), colisão para dentro (contra o próprio projeto), colisão fraca por distância de uma letra, **categoria errada** e termo morto vivo. Mais um modo de triagem, `--candidatos`, para rodar antes de batizar qualquer coisa.

**A quarta é a que ninguém teria escrito à mão.** Ela confere que todo lugar do projeto que cita uma Família, uma Forma, uma Melhoria ou uma Restrição usa um nome que **existe naquela categoria do manual**. Foi ela que pegou a ficha da Kaori, que tem *"Famílias Livres: Peso e Prender"* — e Peso é **Tema**, não Família; Prender não é nada, é uma palavra dentro da descrição de Controle.

**As listas fechadas são extraídas do `.docx` toda vez**, não copiadas: 9 Famílias, 15 Formas, 67 Melhorias, 19 Restrições, 70 Temas, 50 feitiços prontos e os 3 Fundamentos prontos. Quando o manual for regerado, elas se atualizam sozinhas — e o validador falha se a extração devolver um número diferente de nove Famílias, porque aí ele estaria aprovando sem ter lido nada. As perícias e ofícios ele importa do `conferir-pericias.py`, para não existirem duas listas que possam divergir.

Testado nos dois sentidos: numa cópia com os onze problemas consertados ele sai com código 0, e sete perturbações — nome que é Tema exato, nome dentro de feitiço pronto, palavra já batizada, nome dentro de outro nome batizado, Família inexistente, termo morto capitalizado, e o caso de uma letra que deve só avisar — acenderam cada uma a checagem certa.

### Corrigido — três colisões de nome que ninguém tinha visto

| Trilha | com o quê |
|---|---|
| **Sombra** (Evocador) | é **Tema** do manual, grupo Sentidos — e está dentro de **Estilo da Sombra**, o subsistema que ainda vai ser escrito |
| **Enxame** (Evocador) | é **Tema** do manual, grupo Criação |
| **Ofício** (Vanguarda) | é a categoria de **ofício**, com 15 ocorrências só na peça 7 |

A do Ofício é a mais constrangedora: a v0.15 pegou exatamente essa palavra colidindo, resolveu do lado da perícia — *"por isso a lista usa Artesania"* — e deixou a Trilha com o nome.

E duas das três antigas eram piores do que estava registrado. **Régua** não aparece "10x em prosa": ela é **um dos três Fundamentos prontos do manual**, o exemplo que a seção 2 usa para montar o primeiro feitiço. Termo definido, mesma categoria de Herança e Semente. E **Alcance** colide duas vezes — a Família, e o Legado **Alcance Impossível** escrito na v0.22.

### Corrigido de método — a v0.22 errou a categoria do manual

A entrada da v0.22 que rejeita **Herança** diz que ela *"é um dos Selos do manual"*. Não é. A lista *Vínculo · Troca · Cópia · … · Herança · Ausência* é o grupo **Conceito** da tabela de **Temas**. Selo, no manual, é *"um gesto, um som, uma condição visível"* — bater palma, dizer o nome do feitiço. Semente também é Tema, não Selo.

A rejeição estava certa e o motivo estava errado, o que importa porque é o motivo que a próxima checagem vai consultar. É a mesma confusão que produziu "Peso e Prender" como Família: **Tema escrito onde vai Família.** Duas vezes, em versões diferentes, sem ninguém notar — agora o validador não deixa.

### Decidido — os nomes das Trilhas, fechados

Pendência aberta desde a v0.14. Os seis que colidiam saíram; os nove que passaram ficam.

| Caminho | Trilhas |
|---|---|
| **Bastião** | Muro · Punho · Brasa |
| **Vanguarda** | Estocada · **Batedor** · **Executor** |
| **Guia** | Elo · **Sutura** · **Perímetro** |
| **Emanador** | Torrente · Repertório · Arremate |
| **Evocador** | **Servo** · **Matilha** · Coro |

**O Executor mudou de conteúdo junto com o nome.** Ele era *"golpe pesado com arma, ritmo de trabalho, o molde do Nanami"*; virou o corpo a corpo puro. Isso arruma a Vanguarda inteira, que passa a responder a mesma pergunta — *como você alcança o inimigo* — de três jeitos que não se sobrepõem: Estocada com um pé em feitiço, Batedor sem encostar, Executor só encostando. O Nanami vira exemplo, e não molde.

**Sutura ganhou de Respiro por uma frase de regra viva.** A peça 10 diz *"se um respiro devolvesse vida, a coisa mais rara da obra viraria conveniência"* — e a Trilha é justamente a que devolve. O nome brigaria com o texto. Colisão que nenhum validador pega, porque "respiro" ali é prosa.

**Não foi find/replace, pelo mesmo motivo do Grau.** Três dos seis mudam de gênero — *a Régua* → *o Perímetro*, *a Sombra* → *o Servo*, *o Fôlego* → *a Sutura*. E havia duas armadilhas que uma substituição cega destruiria: as ocorrências de "ofício" na peça 7 são **a categoria**, e as de "Sombra" nas peças 8 e 9 são **Estilo da Sombra**. As duas ficam.

Duas sugestões morreram na triagem antes de entrar: **Alento** fica a uma letra de **Lento**, que é Restrição; **Rédea** fica a uma letra de **Rede**, que é feitiço pronto. Nenhuma das duas se pega no olho.

### Decidido — quem ganha ataque extra, e em que nível

**Buraco de regra, não erro de balanço.** Da v0.14 até aqui o ataque extra tinha conta, argumento e correção — e nunca teve dono. O único texto era *"os Caminhos físicos ganham e os meio-arcanos não"*, que é a mesma divisão em duas famílias que a v0.15 registra como tendo deixado o Guia sem número de PE. Ela não cobre os cinco Caminhos.

E o achado nº 2 da v0.20 — *"o Guia pode estar dominado pela Vanguarda"* — dependia inteiro de como essa divisão fosse resolvida. Não era achado fechado; era conclusão apoiada numa classificação que ninguém tinha escrito.

> **Bastião e Vanguarda ganham no nível 6, pelo Caminho.**
> **Arremate e Coro ganham pela Trilha.**
> **O Guia não ganha por nenhuma rota.**

**Num Caminho de técnica, ataque extra é trocar o Classe 0 pelo golpe simples, não somar.** Somando, o conjurador de perto fica com três ações e vai a +61% da Rotina no nível 2 e +22% no 10; trocando, ele cai exatamente na linha do físico, que a peça 6 já aprovou. E somar quebra o único argumento que aprova o ataque extra — *a Rotina já é feitiço mais Classe 0, então o extra do físico é o espelho*.

**O Coro não custa nada a mais**, e isso caiu de graça: a regra da v0.14 diz que o dono e todas as invocações somados entregam **uma** Rotina. É teto de saída, não de número de ações. Os dois golpes do dono e o da invocação continuam saindo do mesmo orçamento — as ações se redistribuem, o dano não sobe. A exceção de economia de ação que estava aberta no Coro já estava paga desde a v0.14, e ninguém tinha percebido.

**O Guia fica coerente ficando de fora.** Ele é o único Caminho que não oferece um segundo golpe; quem quiser lutar de Guia paga pela técnica, no orçamento do Fundamento, como todo mundo. O que era *"pode estar dominado"* vira uma pergunta fechada com número: **o que Elo, Sutura e Perímetro entregam que valha um golpe por rodada?**

### Corrigido — a ficha da Kaori tinha dois nomes que não existem

É a página que todo jogador novo vai copiar, e ela citava **três** categorias erradas de uma vez.

*Famílias Livres: **Peso e Prender***. Peso é **Tema** do manual e preço de Liberação Máxima; Prender não é categoria nenhuma — é uma palavra dentro da descrição de **Controle**. As três Fechadas dela (Amparo, Área, Auxiliares) estavam certas, o que é justamente o que fez ninguém desconfiar da linha. Viraram **Controle e Castigo**: Controle é literalmente *"derrubar, prender, calar, barreira, terreno"*, que é a palavra da Regra dela; Castigo é *"fazer o dano render mais"*, que é o "mais pesado". As duas dizem a mesma coisa que Peso e Prender diziam, com nomes que existem.

E o ofício livre dela era **Artesania**, que virou Entalhador na v0.16. Como é escolha livre, qualquer um dos dez servia; ficou **Caligrafia**, que conversa com ela ser Descendente de um ramo de clã que perdeu o nome.

### Corrigido — a tabela das três alavancas tinha um número da v0.18

A linha do Caminho dizia **+36% / +43% / +44%**, e nenhuma fórmula do projeto reproduzia isso. O **+36%** é o número da v0.18, de quando a faixa era "de 6 para 10 de vida por nível" — e ele sobreviveu à revisão da v0.20, que montou essa tabela **justamente para acertar as bases**. Medido igual às outras duas linhas: **+56% / +46% / +44%**.

**E o par que virou pergunta de playtest mistura bases.** *"Constituição compra +113% contra os +56% da Destreza"* compara Constituição de **0 a 6** com Destreza de **1 a 6**. Na mesma base é **+79% contra +56%** — a Constituição lidera por **1,4×**, não por 2×. A peça 1 já media certo na tabela e citava o 113% à parte; o ESTADO-ATUAL é que juntava os dois como se fossem comparáveis. Não mexemos em nenhum número de regra: só a comparação estava errada, e a diferença é entre "um atributo puxou" e "um atributo dominou".

É a quarta vez que o mesmo tipo de erro aparece — v0.16, contagem não era valor; v0.17, a referência óbvia não era a certa; v0.19, o número certo contra a base errada; agora, dois números certos comparados entre si em bases diferentes.

### Corrigido — nove documentos que tinham ficado para trás

| onde | o quê |
|---|---|
| peça 1 | parágrafo duplicado em "Constituição entra cheia", e o primeiro terminava em *"Indo do valor 1 ao 6:"* sem tabela nenhuma depois |
| peça 3 | *"três peças competem"* pela reação, listando quatro |
| peça 5 | *"Treino em três perícias"* — são duas fixas e quatro livres desde a v0.16 |
| peça 7 | cabeçalho parado na v0.16, com conteúdo da v0.17 e da v0.22 dentro |
| peça 7 | *"Quantos ofícios uma Origem deve dar. Hoje, nenhum"* — a seção 6 do mesmo arquivo dá um |
| peça 8 | *"O catálogo de Origens... a maior lacuna desta peça"*, que existe desde a v0.22 e é apontado duas vezes pela própria peça |
| `arquitetura.md` | dizia "manual v7.3", e o cabeçalho dizia "sincronizada na v0.15" com correção da v0.22 dentro |
| `ESTADO-ATUAL.md` | v7.3 e v7.4 no mesmo arquivo; rabo de tabela morta listando Descanso como pendente; "aplicar Grau → Classe no `.docx`", resolvido na v0.20 |
| `LEIA-ME.md` | parou na v0.20 — "sete peças, três validadores, ainda falta a criação de personagem" |

O *"Quantos ofícios uma Origem dá"* não virou só uma correção: virou pergunta melhor. **O extra da Origem não é escolha de igual para igual** — perícia sem treino você rola, ofício sem treino não. O ofício compra o acesso inteiro a uma coluna fechada; a perícia compra +maestria num teste que você já podia tentar, de +1 no nível 2 a +4 no 30. Medir se alguém escolhe a perícia.

E o **Sentir Energia** saiu da lista de problemas abertos do `ESTADO-ATUAL.md`: a v0.21 fechou como decisão registrada, e ele continuava listado como aberto três versões depois.

### Registrado — três buracos de regra, e um degrau maior do que o texto promete

Nenhum é erro de balanço; são coisas que o material **cita e nunca escreve**, e que dois mestres resolveriam diferente:

- **O PE máximo nunca teve fórmula.** Só a instância do nível 2 na peça 8 (`PE por nível × 2`). Não dá para inferir da vida, que usa `(nível − 1)` e soma atributo.
- **Arredondamento não existe.** "Metade do máximo" e "25% do máximo" caem em fração em cerca de 30% das fichas, e em todo Guia e Vanguarda de nível ímpar. O exemplo da peça 10 arredonda para baixo sem dizer.
- **"Da quarta luta do dia"** nunca define o que conta como luta.

E o **degrau 1 de exaustão** dá desvantagem, que vale **−25 pp no pico** — maior que treinar um Teste de Resistência (+10), maior que a maestria de uma campanha inteira (+20 no nível 30), maior que investir um atributo de 0 a 3 (+15). O texto o vende como o degrau leve. A escada por eixo continua boa; o que falta é o texto dizer o tamanho, e o `conferir-descanso.py` conferir magnitude e não só qual eixo cada degrau toca.

### Achado — o Legado tem teto de quantidade, não de magnitude

Um por ficha, e conferir isso leva um segundo. Mas a faixa entre os catorze é enorme: de **Irmãos** (sente outro Feto por perto, zero em rolagem) a **Não Sou Gente** (imune a veneno, doença e o que ataca corpo humano — apaga uma família de ameaça e boa parte do TR Vigor). A trava escrita, *"não produz dano e não escala com nível"*, não pega imunidade.

Três coisas específicas: **Instinto Bruto está metade morto**, porque "use Sentir Energia no lugar de Percepção" é trocar Essência por Essência desde a v0.16 — o Legado foi escrito na v0.22 pressupondo o quadro anterior. **O relógio não é o mesmo dentro do par** — Latente e Receptáculo oferecem 1×/cena contra 1×/sessão, Reencarnado oferece 1×/arco contra permanente, e pela escada da peça 10 isso é 2× e 5× de diferença numa escolha apresentada como par. E **Treino de Berço** é o único que mexe em número de ficha: ele abre a rota Descendente com **10 perícias, 43%**, fora da faixa de 30–42% que o validador cobra e fora do checklist do mestre, que só conhece "8 e 3 ou 9 e 2".

### Em aberto

- **Nome do sistema.** A última pendência de nome.
- Os quatro achados acima que pedem decisão: o teto de magnitude do Legado, o conserto do Instinto Bruto, as três linhas de regra que faltam, e o texto da exaustão.

---

## [0.23] — 2026-08-07

### Adicionado

- `03-mecanica/10-descanso-e-recuperacao.md` — o manual citava descanso **seis vezes** e nunca definia nenhum dos dois. Sem esta peça ninguém fechava a primeira sessão.
- `03-mecanica/conferir-descanso.py` — quarto validador. Confere que o piso fora da base é estável, que a exaustão não espirala, que nenhum degrau toca a rolagem de luta antes do último, e que os quatro relógios estão ordenados.

### Decidido — a ordem das peças veio de simular uma campanha, não de tamanho

A escolha de escrever descanso antes de Técnica Marcial saiu de perguntar **quando o jogo trava**, e não de qual peça é maior:

| quando | o que travava |
|---|---|
| **fim da sessão 1** | descanso |
| **sessão 2** | equipamento — `Defesa = 10 + Destreza + proteção`, e proteção não tem número |
| **nível 6**, o primeiro marco | aptidões — você escolhe refino e ganha uma, e elas não existem |
| **depois do nível 2** | Trilhas |

E as duas peças de criação que pareciam ser a próxima coisa **estão bloqueadas**: Técnica Marcial depende de **equipamento** (a Maki fere maldição só com ferramenta amaldiçoada, e o preço não existe) e Estilo da Sombra depende das **aptidões** (a rota da Shoko é literalmente "o poder vem de aptidão"). São a quarta e a quinta economia de poder, e a segunda ainda não tem teto escrito.

### Decidido — dois descansos, os dois de ficção

> **Curto — você parou entre uma luta e outra. Longo — a missão acabou.**

**Sem relógio de horas.** Numa Guilda com cinco a sete mestres, *"dá para descansar uma hora aqui?"* é exatamente o tipo de pergunta que cada um responde diferente. Gatilho de ficção, dois mestres arbitram igual.

### Decidido — ambiente propício é o eixo único

Quase tudo na peça depende de uma pergunta só: **o lugar tem recursos?** Talismã, kit, comida, alguém que sabe costurar um corte.

**Lista fechada de exemplos, e o mestre com a palavra final.** É o mesmo padrão dos traços de Origem: a lista existe para ele não decidir do zero, não para amarrá-lo.

| | curto | longo em lugar propício | longo fora |
|---|---|---|---|
| **PE** | 25% do máximo | cheio | **metade do máximo** |
| **Vida** | nada | cheia | **metade do máximo** |
| **Exaustão** | — | zera | não zera |
| **Integridade** | — | cheia | **cheia** |

**A Integridade é a única coisa que o ambiente não toca**, e o motivo é o mesmo da v0.17: a alma não é o corpo. Isso mantém a regra do manual literalmente intacta.

**O descanso curto não devolve vida**, e é decisão: em Jujutsu Kaisen quem conserta gente é a Energia Reversa e a Shoko. Se um respiro devolvesse vida, a coisa mais rara da obra viraria conveniência.

### Achado — "metade" tem uma leitura que colapsa

A regra diz **metade do seu máximo**, e a frase precisa dizer isso com todas as letras. A leitura alternativa — *metade do que você tem* — colapsa:

| Emanador nv10, pool 60, sempre fora da base | dia 1 | dia 2 | dia 3 | dia 4 |
|---|---|---|---|---|
| metade do **máximo** (a regra) | 30 | 30 | 30 | 30 |
| metade do **atual** (a leitura ruim) | 30 | 15 | 7 | 3 |

O validador confere que o piso é estável, e falha se a regra escorregar para a outra leitura.

### Decidido — exaustão, e o teto que impede a espiral

**Não existe no manual** — zero ocorrências de exaustão, cansaço ou fadiga. É peça nova, e ela existe porque **sem ela o descanso curto não tem limite**.

> **Da quarta luta do dia em diante, cada luta dá um degrau. Máximo de três.**

| degrau | o que pega | curto fora de lugar propício |
|---|---|---|
| 1 | desvantagem em perícia e ofício | 15% |
| 2 | deslocamento cai para 6 m | 5% |
| 3 | desvantagem em ataque e Teste de Resistência | nada |

**A ordem não é aleatória: o primeiro degrau pega fora de combate, o segundo pega posicionamento, e só o terceiro pega a rolagem de luta.** Quem está cansado começa a falhar no que não mata antes de falhar no que mata — e o validador **falha** se algum degrau anterior ao último tocar a rolagem.

**O teto de três existe porque a combinação escolhida é uma espiral.** Exaustão que não zera fora da base, somada a degraus crescentes, é o mesmo defeito que a v0.8 diagnosticou: quem está cansado erra mais, apanha mais, luta mais tempo e cansa mais. Sem teto, dez dias de campo dariam vinte degraus.

**E o mestre pode tirar um degrau quando a ficção pedir** — uma noite de sono de verdade, um dia parado. A válvula só anda para o lado do jogador: o mestre nunca adiciona degrau fora da regra.

### Decidido — os quatro relógios, e por que o manual tinha dois nomes

O manual usa **"por cena"**, **"por descanso"** e **"por dia"** sem nunca dizer como se ordenam. Agora dá:

**por cena → por descanso curto → por dia → por descanso longo**, do mais frequente ao menos.

**"Por dia" e "por descanso longo" não são a mesma coisa, e a diferença é o ponto.** Uma missão pode durar cinco dias: quem tem "uma vez por dia" recarrega cinco vezes, quem tem "uma vez por descanso longo" recarrega uma. É por isso que o manual dá "por dia" para a Passiva Segunda Natureza e "descanso longo" para a Integridade — a segunda é muito mais forte, e o relógio mais lento é o preço.

### O orçamento de missão

**PE é o que você tem para a missão inteira.** A coluna do manual — *"quantas vezes você lança o seu melhor feitiço"* — passa a significar **por missão**, e vira o piso em vez do teto:

| lutas no dia | PE acumulado |
|---|---|
| 3 | 1,50 × pool |
| 4 | 1,75 × pool — e a exaustão entra |

É também o que **faz o golpe simples e o Classe 0 existirem**: eles são o que sobra quando o combustível acaba, e num sistema onde o combustível volta cheio a cada respiro eles não teriam razão de ser.

### Em aberto

- **Se três lutas de graça é o número certo.** Se a maioria das sessões tem duas lutas, a exaustão nunca dispara e a peça vira decoração.
- **Se o descanso curto devia devolver alguma vida.** Se o grupo sem curandeiro travar entre lutas, o conserto barato é devolver só em ambiente propício.
- **O que acontece com quem passa semanas em campo.** O teto de três impede a espiral e também diz que dois meses no mato doem igual a três dias.

---

## [0.22] — 2026-08-07

### Adicionado

- `03-mecanica/09-origens.md` — o catálogo. Fecha a maior lacuna da criação de personagem, que era a única coisa no sistema em que um número dependia de julgamento do mestre.
- `conferir-pericias.py` ganhou as listas de Origem e duas checagens: as quatro perícias de cada uma existem no quadro, e nenhuma Origem tem a lista inteira já fixada por um Caminho — se tivesse, a escolha dela morreria.

### Decidido — três camadas, não uma lista

| | |
|---|---|
| **Cinco principais** | Latente · Receptáculo · Descendente · Reencarnado · Feto |
| **Sub-origem** | **Sem Técnica**, que se soma a qualquer uma das cinco |
| **Duas especiais** | **Corpo Amaldiçoado** e **Restrição Celestial** — não aceitam a sub-origem, porque são especiais |

O cruzamento é o que a estrutura compra: **Descendente Sem Técnica** é o caso da Miwa, nome de peso e nenhuma técnica de clã. Uma lista plana de oito perderia isso.

### Corrigido pelo cânone — duas categorias mudaram de nome antes de existirem

A checagem contra a obra pegou uma coisa que teria nascido errada.

**O Junpei tem técnica inata.** Escória da Lua, veneno. O que o Mahito fez foi *modificar o cérebro dele para que ela despertasse antes da hora* — o poder era dele, o acesso veio de fora. Ele estava classificado como "recebeu técnica de fonte externa" e **virou Latente**.

Com ele fora, a categoria mudou de recorte e de nome: **Maculado virou Receptáculo**, e passou a ser *"você carrega alguma coisa, e ela ainda está aí"* — Itadori com o Sukuna, Hana Kurusu com o Anjo.

E **Desperto virou Reencarnado**, o que deixou a fronteira entre as duas nítida. **É a distinção que o próprio mangá faz:** sobre a Hana Kurusu, o texto diz que *"ao contrário da maioria das encarnações, o Anjo vive simbioticamente dentro dela em vez de sobrescrever a consciência"*.

> **Receptáculo é simbiose — os dois estão lá. Reencarnado é sobrescrita — sobrou um.**

O resto do cânone conferiu: **Kashimo** aceitou virar objeto amaldiçoado e encarnar num corpo que o Kenjaku preparou; **Panda** é Cadáver Amaldiçoado de Mutação Abrupta feito pelo Yaga, com três núcleos; **Mechamaru** troca corpo inútil por energia enorme; **Maki e Toji** nasceram sem energia nenhuma e ganharam corpo sobre-humano.

### Decidido — a patente sai da Origem

**Todo personagem começa Grau 4**, venha de onde vier. A patente é eixo social e sobe por feito.

Isso contradizia três documentos, e os três foram corrigidos: a peça 8 dizia que a Origem dava a patente inicial, a peça 2 usava o Yuta como justificativa, e o `arquitetura.md` chamava a Origem de *"o lugar natural da patente inicial"*.

**O caso do Yuta continua existindo na ficção** — a instituição classifica quem ela quiser onde ela quiser. O que sai é a patente ser **produto da Origem na criação**, que criaria a origem que começa na frente. É o mesmo argumento que a v0.10 usou para tirar atributo da Origem.

### Decidido — o Legado, e o teto que ele nasce com

> **O nome saiu de "talento" numa checagem que pegou colisão antes de ela existir.**
>
> A ideia era chamar de **Herança**, para remeter à Origem. **Herança é um dos Selos do manual** — ela está na lista *Vínculo · Troca · Cópia · Contrato · Dívida · Sorte · Aposta · Julgamento · Regra · Registro · Valor · Verdade · Segredo · Herança · Ausência*. Termo definido, mesma armadilha do Grau.
>
> Testadas em seguida: **Marca** (8× no manual), **Sangue** (9×) e **Semente** (também Selo) colidem igual. **Legado** tem zero ocorrência no manual e zero no projeto, e diz a mesma coisa que Herança dizia. Quatro nomes conferidos antes de um entrar no material — foi mais barato que o Grau, que só foi pego depois de 76 tabelas escritas.

A Origem dá **um Legado**, escolhido entre dois. **Um só na ficha inteira: o sistema nunca concede outro.**

Legado é economia de poder nova, e o `arquitetura.md` já chama as aptidões de *"o risco maior da estrutura inteira"* por não terem teto escrito. **Então esta nasce com o teto embutido, e o teto é o menor possível** — toda ficha tem exatamente um, e conferir isso leva um segundo. Legado não produz dano e não escala com nível, pela mesma regra das aptidões.

### Decidido — o resto do que a Origem entrega

**Uma perícia da lista de quatro dela, uma perícia livre, e um extra que o jogador escolhe: um ofício livre ou mais uma perícia.** Mais um Teste de Resistência (qualquer um dos quatro) e um traço, do catálogo dela ou escrito com aprovação.

O extra opcional cria duas rotas, e **as duas cabem na faixa**:

| rota | perícias | ofícios |
|---|---|---|
| Origem pega o ofício | 8 de 23 = **35%** | 3 de 10 = 30% |
| Origem pega a perícia | 9 de 23 = **39%** | 2 de 10 = 20% |

### Registrado — seis das nove rotas já rodam

| rota | jogável |
|---|---|
| as cinco principais | **sim** — vão para o Fundamento, que existe e está validado |
| Restrição Celestial, ramo do Mechamaru | **sim** — Fundamento normal, com o corpo limitado escrito na ficha |
| qualquer uma **+ Sem Técnica** | não — precisa de **Aptidão** ou **Estilo da Sombra** |
| Corpo Amaldiçoado | não — precisa de **Técnica Marcial** |
| Restrição Celestial, ramo da Maki | não — precisa de **Técnica Marcial** |

As três que faltam dependem de um subsistema paralelo ao Fundamento, e ele é a próxima peça. Elas entram no catálogo assim mesmo porque **a Origem é decisão fechada; o que falta é a montagem**.

### Corrigido

- A lista do Reencarnado tinha **Táticas**, que foi removida do quadro na v0.16. Virou Investigação. O validador agora falha se uma Origem oferecer perícia que não existe.

### Decidido — a próxima peça são duas, não uma

**Técnica Marcial** e **Estilo da Sombra** vão ser sistemas separados, porque resolvem problemas diferentes:

| | quem | o problema |
|---|---|---|
| **Técnica Marcial** | Panda, Maki, Toji | **não tem energia amaldiçoada.** Sem PE, sem golpe canalizado, sem Sentir Energia. Paga com o corpo e com ferramenta amaldiçoada |
| **Estilo da Sombra** | Miwa, Kusakabe | **tem energia e não tem técnica.** Tem PE e não tem o que gastar nele. Paga com PE, como todo mundo |

Um motor único acharia os dois: o Panda troca de núcleo e a Miwa saca espada, e forçar isso num orçamento só apagaria a diferença. O custo aceito é balancear duas economias novas em vez de uma.

### Em aberto

- **Técnica Marcial e Estilo da Sombra**, que destravam três rotas.
- **A Aptidão como rota de criação** — a Shoko existe na obra e não na regra, e isso amarra com os degraus de refino, que também não foram escritos.
- **Se a perícia livre da Origem devia ser da lista também.** É o último lugar da criação em que um número depende de julgamento.
- **Se um Legado por ficha é pouco.** Se parecer decoração no playtest, o conserto é mais opções por Origem, não mais Legados por ficha.

---

## [0.21] — 2026-08-07

### Adicionado

- `03-mecanica/08-criacao-de-personagem.md` — **a peça em que tudo se encontra.** Não inventa regra: junta as sete anteriores e o manual do Fundamento na ordem em que a pessoa senta e preenche.
- `99-arquivo/` — pasta de material morto, com `LEIA-ME.md` próprio e três subpastas por assunto.

### Decidido — a ordem dos oito passos, e por que o passo 2 existe

> **Origem → a Regra em uma frase → Caminho → Atributos → a técnica inteira → Perícias e ofícios → os números → Pactos.**

O `arquitetura.md` já tinha levantado a tensão: escrever a técnica inteira leva tempo, mas **escolher o Caminho antes de saber o que a técnica faz ancora o jogador num papel de equipe antes de ele saber o que o personagem é**. Quem escolhe "eu sou o tanque" e só depois escreve a técnica tende a escrever uma técnica de tanque — o oposto do pilar 1.

A saída é partir a técnica em duas: a **Regra sai no passo 2**, em uma frase, e o resto fica para o passo 5. O jogador escolhe o Caminho já sabendo o que a técnica dele é, e ainda não gastou a parte longa.

### Decidido — Sentir Energia fica como está

O achado da v0.20 dizia que ela falha no teste do bônus automático: sendo a mais rolada da mesa, toda ficha eficaz gasta uma das quatro escolhas livres nela, então o Caminho entrega três livres e uma obrigatória.

**Aceito conscientemente, e o argumento é do Mizuki:** sempre vai existir perícia melhor que outra, e as pessoas escolhem por querer ser únicas, não só por eficiência — é para isso que a lista tem vinte e três opções. Deixa de ser problema aberto e passa a ser decisão registrada.

### A ficha de exemplo, conferida

A peça traz uma ficha inteira — a Kaori, Bastião de nível 2 — e cada número dela foi conferido contra as fórmulas: vida 23, Integridade 28, PE 8, Defesa 12, CD 13.

O que ela mostra sem precisar dizer: **ela acerta d20+3 com o soco e d20+3 com o feitiço.** Não é coincidência — é o `2 + maestria` da v0.9 calibrado exatamente para o conjurador empatar com o guerreiro do nível 2 ao 30.

### Registrado — o que a criação ainda contorna

Quatro coisas entram como provisórias, cada uma com a saída escrita no ponto do texto onde ela pesa, e não numa nota no fim:

- **Origens** — escrita livre com aprovação do mestre. É a única em que um número depende de julgamento, e a maior lacuna da peça.
- **Pactos** — só a trava e a promessa.
- **Equipamento** — a ficha nasce com proteção 0. Não trava a criação; trava a segunda sessão.
- **Trilhas** — não afetam o nível 2, afetam a primeira subida.

### Alterado — o arquivo morto saiu do caminho

Material superado espalhado pelas pastas vivas atrapalha busca e ocupa a atenção de quem lê. Agora tem lugar:

| pasta | o que foi para lá |
|---|---|
| `99-arquivo/secoes-substituidas/` | a lista de catorze perícias e o quadro de quatro Caminhos, **extraídos de dentro das peças 4 e 5** |
| `99-arquivo/construcao-das-skills/` | o benchmark das quatro skills, o `feedback.json` e o visualizador — 200 KB que ninguém consulta |
| `99-arquivo/ferramentas-de-decisao/` | o comparador de curvas, que escolheu o d20 na v0.3 e está aposentado desde então |
| `99-arquivo/` | o `PROMPT-DE-CONTINUIDADE.md`, que o `ESTADO-ATUAL.md` faz melhor |

**A mudança de método que vale registrar:** até aqui, seção superada ficava dentro da peça viva com um aviso em cima. Isso não resolve — ela continua aparecendo em busca e continua ocupando quem lê. **Agora ela sai inteira**, e na peça viva fica só um parágrafo com o que sobreviveu e um ponteiro. As peças 4 e 5 encolheram e ficaram mais fáceis de ler.

Cada arquivo arquivado carrega no topo: de onde saiu, o que o substituiu, em que versão, **por que morreu** e o que dele sobreviveu. A última linha é a que não dá para reconstruir depois.

**Aviso para quem ler as entradas antigas deste arquivo:** as versões da v0.2 à v0.4 citam caminhos que não existem mais — `workspace-skills/`, `03-mecanica/comparador-de-curvas.html`, `feedback.json` na raiz. Elas ficam como estão, porque descrevem o que era verdade na época. A tabela acima é o mapa de para onde cada coisa foi.

---

## [0.20] — 2026-08-06

Revisão cética do material inteiro antes de abrir a criação de personagem, em três camadas: automática, textual e de design. Os três validadores passam. Achou quatro erros de texto e três problemas de design que nenhum validador pegaria. E fechou a pendência mais antiga do projeto, aberta desde a v0.3.

### Aplicado — Grau virou Classe no manual do Fundamento

A colisão estava aberta desde a v0.3 e decidida desde a v0.6: **"grau" é o termo da obra para a patente do feiticeiro**, a Guilda fala assim há anos, e o manual usava a mesma palavra para o tamanho do feitiço. Agora o manual está na **v7.4** e usa Classe.

**Não foi find/replace, e essa é a parte que vale registrar.** *Grau* é masculino e *Classe* é feminino. Uma substituição cega produz "do Classe", "um Classe", "o seu maior Classe". Foram **243 linhas alteradas** nos nove arquivos de fonte, e **dez precisaram de concordância que nenhuma regra automática pega**:

- artigo e preposição — *do Grau* → *da Classe*, *num Grau* → *numa Classe*, *pelo Grau* → *pela Classe*
- markdown no meio — `um **Grau**` não casava com a regra de `um Grau`, e escapou na primeira passada
- **pronome** — *"Escolha o Grau… **Ele** define os pontos"* → *"Escolha a Classe… **Ela** define os pontos"*

O método que achou os três últimos foi um linter escrito para o caso: procurar artigo masculino colado em Classe, no texto **renderizado**, não na fonte. Ele acusou oito ocorrências, das quais **cinco eram falso positivo** — *"o mesmo número dos pontos dele"* e *"de que Classe ele era"* têm "ele" se referindo ao feitiço e ao personagem, não à Classe. Só leitura separa esses casos.

**Um efeito colateral que precisou de decisão:** o manual tinha uma frase em prosa — *"se a sua mesa tem uma classe que bate em vez de conjurar"* — que passaria a colidir com o termo novo. Virou *"um tipo de personagem que bate"*.

Conferido depois de gerar: **0 ocorrências de "Grau"** como palavra inteira, 198 de "Classe", `pac7.py` e `v7.py` passando, e a estrutura idêntica — 325 parágrafos e 76 tabelas nos dois. As treze aparições de "grau" que sobram no texto são todas **"degrau"**, palavra diferente.

O `.docx`, o `.pdf` e o `.zip` de fontes foram regenerados e instalados.

### Corrigido — erros de texto

- **Parágrafo duplicado na peça 1.** "Vida é a única alavanca que a trava do Caminho deixa aberta" aparecia duas vezes seguidas, como seção e como parágrafo, dizendo a mesma coisa. Resíduo de edição da v0.18.
- **Dois números contraditórios para a mesma coisa, na mesma seção.** A peça 1 dizia que Constituição compra +45% de sobrevivência no nível 10 numa tabela e **+113%** noutra, dez linhas abaixo. A primeira ficou parada na fórmula da v0.18. Pior: as duas usavam bases diferentes — uma media do valor 1 ao 6, a outra do 0 ao 6. **Agora as três alavancas aparecem numa tabela só, todas medidas de 1 a 6**, com o valor de 0 a 6 citado à parte.
- **A peça 1 ainda usava a escada de perícia CD 12/16/20**, que não existe. A oficial é 10/14/18/22/26, corrigida no validador desde a v0.17 mas não no texto.
- **Listas de "Em aberto" apontando para coisas já resolvidas** em cinco das sete peças — quantos TRs se treina, de onde vem o treino, o quadro de Caminhos, a lista de catorze perícias, se o ataque de oportunidade usa a rolagem comum. Cada uma virou uma linha de "resolvido e tirado daqui", com o ponteiro para onde a resposta mora.

### Achado — Sentir Energia falha no teste do bônus automático

A peça 7 declara: *"Sentir Energia não é fixa de ninguém, e isso é escolha. Livre para todos, ela vira decisão de ficha — e o feiticeiro ruim de sentir energia passa a caber."*

**Não vira.** Ela é a perícia mais rolada da mesa, com o dobro do peso da segunda colocada e o quádruplo das outras dezessete. Com quatro escolhas livres entre vinte e três opções e uma delas valendo por quatro, **toda montagem que se importe com eficácia pega**.

Na prática o Caminho dá **três livres e uma obrigatória**, não quatro livres. E o Itadori ruim de sentir energia só existe se o jogador escolher ser pior de propósito — o que é armadilha, não escolha.

Três saídas, nenhuma aplicada ainda: dar Sentir Energia de graça a todo feiticeiro e assumir que é o piso; fixá-la em alguns Caminhos e aceitar a vantagem; ou aceitar que são três livres e dizer isso no texto em vez de prometer quatro.

### Achado — o Guia pode estar dominado pela Vanguarda

| | vida/nível | PE/nível | ataque extra |
|---|---|---|---|
| Vanguarda | 5 | 5 | **sim** |
| Guia | 5 | 5 | não |

**Números idênticos, e a Vanguarda tem um recurso a mais.** É o único par do sistema em que dois Caminhos custam igual e um leva algo que o outro não leva.

O Guia só escapa se as Trilhas dele entregarem algo que valha um ataque por rodada. Hoje as Trilhas são três linhas de descrição sem número nenhum, então **não dá para saber** — não é erro provado, é buraco de verificação. Fica travado até a peça de Trilhas existir, e é a primeira coisa a conferir quando ela existir.

### Achado — o ofício não passa no filtro do multi-mestre

A regra diz que **o mestre escolhe o atributo que o ofício usa, na hora**. Forjar uma lâmina é Força ou Inteligência? Falsificar é Destreza ou Essência?

Dois mestres que nunca conversaram cobram atributos diferentes pelo mesmo ofício, e a diferença pode ser de cinco pontos na rolagem. É a segunda regra do sistema em que **um número depende de julgamento** — a outra é a Origem dando duas perícias livres, que já está marcada como provisória.

O conserto padrão do projeto se aplica: uma tabela pequena, com o atributo padrão de cada ofício e uma linha dizendo quando o mestre pode trocar.

### Registrado — quatro premissas herdadas que nunca foram marcadas

A peça 3 fez esse exercício para a economia de ação e concluiu, honestamente, *"mantemos por custo de retrabalho, não por mérito"*. Quatro outras nunca passaram por ele:

- **Vida por Caminho.** Entrou na v0.19 com argumento próprio — é a única alavanca que a trava do Caminho deixa aberta —, o que é melhor que herdar cego, mas não está escrito como herança do d20.
- **Vida como reservatório único que esvazia.** Nunca questionado. Em Jujutsu Kaisen o ferimento importa narrativamente, e um medidor só pode não ser o que a obra faz.
- **Nível inteiro subindo de um em um.** O sistema só usa marcos de quatro em quatro; os níveis entre marcos entregam apenas Classe de feitiço. Vale perguntar se o nível precisa existir na granularidade que tem.
- **Rolagem de acerto separada da de dano.** Herdada do Fundamento, que já é d20.

Nenhuma é problema. Mas o projeto tem por método marcar o que é escolha e o que é herança, e essas quatro estavam passando como escolha sem ter sido decididas.

---

## [0.19] — 2026-08-06

### Corrigido — a trava de vida da v0.18 conferia a coisa errada

A v0.18 checava que a **média dos dados de vida** desse 8, igual ao número do manual. Isso parece certo e não é.

**O 8 do manual é a vida total por nível, sem atributo nenhum** — ele foi escrito antes de existir Constituição na conta. Somar Constituição por cima não empata com ele: infla.

| | média dos dados | mais Constituição típica (3) | o manual supõe | desvio |
|---|---|---|---|---|
| v0.18 — 10/9/8/7/6 | 8,0 | 11,0 | 8 | **+38%** |
| v0.19 — 7/5/5/4/4 | 5,0 | **8,0** | 8 | **+0%** |

Na prática, a v0.18 dava ao grupo 38% de vida a mais do que a tabela de encontro supõe, e o combate durava **4,7 rodadas onde o manual promete 3,5**.

**A trava certa é: média dos dados + 3 de Constituição ≈ 8.** O validador foi reescrito para conferir isso, e agora também mede as rodadas para cair sob foco contra a tabela de chefe do manual, em vez de confiar numa média abstrata.

É a terceira vez seguida que o mesmo tipo de erro aparece — v0.16, contagem não era valor; v0.17, a referência óbvia não era a certa; agora, o número certo comparado contra a base errada. **A pergunta que faltou nas três: "esse número já inclui o que eu estou somando nele?"**

### Alterado — a vida por Caminho, com dado

| Caminho | dado | vida no nível 1 | por nível | PE por nível | soma |
|---|---|---|---|---|---|
| **Bastião** | d12 | 12 | 7 | 4 | 11 |
| **Vanguarda** | d8 | 8 | 5 | 5 | 10 |
| **Guia** | d8 | 8 | 5 | 5 | 10 |
| **Evocador** | d6 | 6 | 4 | 6 | 10 |
| **Emanador** | d6 | 6 | 4 | 6 | 10 |

> **No nível 1 você recebe a vida inicial do Caminho + Constituição.**
> **Em cada nível depois, a vida por nível do Caminho + Constituição de novo.**

**A vida inicial é o máximo do dado e a vida por nível é a metade dele arredondando para cima**, então quem quiser pode rolar o dado em vez de pegar o fixo. Uma versão anterior desta proposta tinha 6 por nível para os Caminhos de d8, o que não fecha — d8 dá 5. O validador agora falha se o fixo e o dado deixarem de ser equivalentes.

**A soma vida+PE ficou 11 no Bastião e 10 nos outros quatro.** É o número que faz a troca "couro contra combustível" ser sabor em vez de degrau de poder, e o validador falha se a diferença passar de 2.

### Alterado — PE em três degraus

**6 no Emanador e no Evocador. 5 na Vanguarda e no Guia. 4 no Bastião.**

Os dois do meio vivem entre bater e conjurar: o Guia estende efeito alheio e recupera, a Vanguarda alterna golpe canalizado com golpe simples. O **6 dos dois conjuradores puros não é escolha nossa** — o Fundamento tem uma tabela de "quantas vezes você lança o seu melhor feitiço" calculada em cima dele. O 4 e o 5 são números nossos.

### Resultado

Rodadas para cair sob foco, com Constituição 3, contra a tabela de chefe do manual:

| | nv 2 | nv 10 | nv 20 | nv 30 |
|---|---|---|---|---|
| Bastião | 4,2 | 4,0 | 4,2 | 4,2 |
| Vanguarda · Guia | 3,2 | 3,2 | 3,3 | 3,4 |
| Evocador · Emanador | 2,7 | 2,8 | 2,9 | 2,9 |
| **média do grupo** | 3,2 | 3,2 | 3,3 | 3,4 |

Plana do nível 2 ao 30 nos cinco, e a média em cima das 3,5 do manual. O mestre nunca precisa saber o nível para estimar quanto tempo alguém aguenta.

### Registrado — Constituição virou a maior alavanca de sobrevivência

| no nível 10, do menor valor ao maior | compra |
|---|---|
| Caminho, de 4 para 7 | +46% |
| Destreza, de 1 para 6 | +56% |
| **Constituição, de 0 para 6** | **+113%** |

Na v0.18 ela comprava +59%, na mesma faixa da Destreza. Dobrou por duas razões somadas: a vida por nível ficou menor, então cada ponto de Constituição pesa proporcionalmente mais; e ela passa a entrar **também no nível 1**, multiplicando por *nível* em vez de *(nível − 1)*.

Não quebra nada e as três continuam sendo escolhas, mas é o primeiro número do sistema em que um atributo está claramente na frente. **Pergunta de playtest: apareceu alguém com Constituição 0 ou 1?** Se não apareceu, ela virou obrigatória, e o conserto é uma linha — Constituição volta a entrar só do segundo nível em diante.

Pela mesma causa, o espalhamento subiu para **3,2×**: o Evocador de Constituição 0 tem 122 de vida no nível 30 e cai em 1,7 rodadas, contra 395 e 5,5 rodadas do Bastião de Constituição 6. O teto do validador subiu de 3,0× para 3,5× com o motivo escrito.

### Efeito colateral registrado — a alma virou a reserva maior

Com a vida do corpo menor, a Integridade (`20 + 8 × (nível − 1)`, inalterada) passou a ser **maior que a vida em quatro dos cinco Caminhos**. Quem não é Bastião cai pelo corpo antes de a alma acabar, então o **estágio 4 de dano de alma quase nunca dispara**.

O Bastião é o único que inverte: no nível 30 ele fica de pé com 53 de vida no medidor e a alma acabada. É exatamente o que o Mahito faz com quem é duro demais para morrer de porrada — mas hoje ele é o único que chega lá.

Isso muda quando a **Essência** entrar na Integridade, o que já está decidido e sai junto com a peça de dano de alma.

---

## [0.18] — 2026-08-06

### Decidido — cada Caminho tem a sua vida por nível

> **Pontos de vida = 20 + (a vida do seu Caminho + Constituição) × (nível − 1).**

| | Bastião | Vanguarda | Guia | Evocador | Emanador |
|---|---|---|---|---|---|
| vida por nível | 10 | 9 | 8 | 7 | 6 |
| PE por nível | 4 | 4 | 6 | 6 | 6 |

**O argumento não é "porque o d20 faz assim" — é que sem isso o Bastião não tem como ser tanque.**

A trava do Caminho, escrita na peça 5, proíbe ele de dar dados de dano, Classe de feitiço, Melhoria de graça e cura. Com a v0.17, o Bastião — *"o corpo como resposta: aguentar, encarar, prender"* — ainda não tinha **um único número** que o fizesse aguentar mais que um Emanador. A coisa que o tornaria duro seria a Constituição dele, que qualquer conjurador também pode pegar.

Vida é a única alavanca que a trava deixa aberta, e ela não está na lista do proibido: não é dano, não é Classe, não é Melhoria, não é cura. É o que transforma "aguentar" em mecânica em vez de sabor.

E ela **corre no sentido contrário do PE**, que já era assimétrico desde a v0.14: quem tem mais couro tem menos combustível. As duas assimetrias se pagam em vez de empilhar.

### A trava que a peça precisa: média 8

**A média dos cinco Caminhos tem que dar exatamente 8**, e isso não é estética. O manual calibra vida de chefe, dano de chefe e dano de capanga em cima de 8 por nível. Enquanto a média for 8, a tabela de encontro dele continua valendo para um grupo típico — e ela é a peça que faz cinco mestres prepararem igual. 10 + 9 + 8 + 7 + 6 = 40, sobre cinco, dá 8.

O `conferir-atributos.py` agora **falha** se a média sair de 8, se o espalhamento passar de 3×, ou se uma das três alavancas de sobrevivência dominar as outras duas.

### Os números que fecham

| no nível 10, do menor valor ao maior | compra de sobrevivência | custo |
|---|---|---|
| Caminho, de 6 para 10 | +36% | escolha única, na criação, sem volta |
| Constituição, de 0 para 6 | +59% | pontos de atributo |
| Destreza, de 1 para 6 | +56% | pontos de atributo, e devolve muito mais junto |

Espalhamento no nível 30: de **194** (Emanador de Constituição 0) a **484** (Bastião de Constituição 6), **2,5×**. Um pouco mais largo que o d20 clássico, onde a distância entre o conjurador frágil e o brutamontes fica perto de 2×.

Nenhuma das três domina, e a do Caminho é a única que **não tira ponto de lugar nenhum**.

### Integridade — o rumo agora está decidido, não só registrado

A Integridade continua plana em `20 + 8 × (nível − 1)`, sem Caminho e sem Constituição, e continua sendo exatamente a fórmula do manual — muda uma frase, não muda uma tabela.

**Mas ela não fica assim.** Decidido que a Integridade vai **escalar com Essência**, virando uma segunda vida de verdade em vez de um número plano. Entra junto com a peça de dano de alma, com o contexto que ela vai trazer.

Quando entrar, os dois eixos se cruzam em vez de empilhar: o Emanador de Essência alta fica com **alma grossa e corpo fino**, o exato oposto do Bastião. Hoje já dá para ver o embrião disso — no nível 30, a alma do Bastião acaba com 232 de vida ainda no medidor, e ele fica de pé sem ser mais ele. É a imagem que a obra usa o tempo todo.

### Corrigido de método

A v0.17 tinha escolhido `20 + (8 + Constituição) × (nível − 1)`, com o 8 igual para todo mundo, e **não perguntou se o 8 devia ser igual para todo mundo**. O número veio do manual, e o manual não conhece Caminhos — ele foi escrito antes de eles existirem.

É a mesma lição da v0.17 aplicada um nível acima: lá, a referência óbvia (a tabela do manual) não era a referência certa para o tamanho da Constituição. Aqui, ela também não era a referência certa para **quantas fórmulas de vida deveriam existir**.

---

## [0.17] — 2026-08-06

Revisão geral antes de começar a criação de personagem. Os três validadores passam, todas as fórmulas aparecem iguais em todo lugar, todas as referências cruzadas resolvem e nenhum termo carrega dois significados. Achou um buraco grande e três textos parados.

### Achado — Constituição não fazia nada

Três documentos diziam que Constituição governava pontos de vida. A peça 4 e a peça 7 usavam exatamente isso para justificar por que ela tem **zero perícias**: *"ela já governa vida e o TR Vigor, que é trabalho suficiente"*.

A única fórmula de vida que existia no projeto inteiro estava no manual do Fundamento, e é `20 + 8 × (nível − 1)` — **sem atributo nenhum**. Constituição entregava só o Teste de Resistência Vigor, e o argumento que tirou as perícias dela era um trabalho que ela não tinha.

É o mesmo padrão da v0.11, a tensão que era lacuna de texto disfarçada. Só que desta vez a lacuna estava na linha mais visível da ficha, e teria aparecido na primeira pessoa que fosse criar um personagem.

### Decidido — Constituição entra cheia

> **Pontos de vida = 20 + (8 + Constituição) × (nível − 1).**

**E o número que decide isso não é o do manual.** Comparar Constituição com uma tabela que não tem atributo nenhum faz qualquer valor parecer demais — foi assim que a primeira recomendação saiu "metade", e estava errada.

A comparação certa é com o outro atributo que **já** compra sobrevivência: Destreza, pela Defesa. Indo do valor 1 ao 6:

| nível | Destreza (faz errar mais) | Constituição cheia | razão |
|---|---|---|---|
| 2 | +63% | +17% | 0,72 |
| 10 | +56% | +45% | 0,93 |
| 22 | +50% | +50% | **1,00** |
| 30 | +45% | +52% | 1,04 |

As duas ficam na mesma faixa a campanha inteira, e cruzam por volta do nível 22. **Destreza protege mais cedo e Constituição protege mais tarde** — a Defesa não cresce com o nível, a vida cresce. É por isso que uma não domina a outra.

Pela metade, Constituição ficaria em +29% no nível 10: o atributo que faz uma coisa só, fazendo pior que o atributo que faz cinco. Destreza ainda compra ataque à distância, iniciativa e quatro perícias por cima.

### Decidido — a Integridade não leva Constituição

> **Integridade = 20 + 8 × (nível − 1).**

O manual diz *"Integridade = vida máxima"*. Com Constituição na vida, essa frase daria de graça a um corpo duro uma alma dura — e dano de alma é justamente o que ignora o corpo. O que o Mahito faz não passa pelo músculo.

**A escolha custa zero:** a fórmula acima é exatamente a que o manual já tem. Muda uma frase — *"Integridade = vida máxima"* vira *"a vida que todo mundo tem, antes da Constituição"* — e não muda nenhuma tabela. Os quatro estágios de dano de alma continuam valendo como estão.

Se a alma parecer frágil no playtest, o conserto natural é ela somar **Essência**, que já é o atributo do TR Espírito e o eixo da alma no sistema. Registrado, não aplicado.

### Alterado

- `conferir-atributos.py` ganhou dois invariantes novos: **Constituição compra sobrevivência na mesma faixa que a Destreza** (falha fora de 0,6× a 1,4×) e **Integridade não leva Constituição** (falha se sair da fórmula do manual, porque aí a tabela de estágios teria que ser refeita).

### Corrigido — três textos que tinham ficado para trás

- **A peça 1 ainda dizia "3,2 rodadas é o alvo, com 65% de acerto".** Os dois números estavam errados e não batiam nem entre si: o CHANGELOG da v0.8 registrava 60% e o validador entrega 50%. Virou previsão de **3,4 a 4,0 rodadas**, com a tabela das três taxas do lado, marcada como número a medir e não alvo fechado.
- **A peça 3 citava a regra de ouro nº 6 como "Grau 0"** enquanto o resto do material diz "Classe 0". Citação traduzida, com nota de que o `.docx` ainda não foi regenerado.
- A nota de substituição da peça 4 dizia "vinte perícias" e não avisava que Sentir Energia mudou de atributo na v0.16.

### O que a criação de personagem ainda não tem

Levantado de propósito antes de começar. Só um item travava, e ele foi resolvido acima.

| falta | trava? | por quê |
|---|---|---|
| Lista de Origens | não | a forma existe — patente, traço, duas perícias, um TR. Falta o catálogo, e o mestre aprova na leitura |
| Tabela de proteção | não | `Defesa = 10 + Destreza + proteção`, e dá para criar com proteção 0 |
| Tabela de armas | não | o golpe canalizado nem usa arma |
| Quantas Trilhas e quando | não | a ficha começa no nível 2 e Trilha vem depois |
| Regra de Pactos | não | camada 5, opcional na criação |

### Lição de método

**Quando um número não existe, o erro não é escolher mal — é escolher contra a referência errada.** A primeira recomendação de Constituição saiu conservadora porque comparou com a tabela do manual. A pergunta certa nunca foi "quanto de vida é demais", e sim "quanto de sobrevivência os outros atributos já compram".

Vale como par da lição da v0.16: lá, contagem não era valor; aqui, a referência óbvia não era a referência certa.

---

## [0.16] — 2026-08-06

### Alterado

- `03-mecanica/07-pericias-e-oficios.md` reescrita: **vinte e três perícias**, e o quadro mudou de eixo.
- `03-mecanica/01-atributos-acerto-defesa.md` — a tabela de atributos e o parágrafo da fusão de Essência, que diziam o contrário do que agora vale.
- `03-mecanica/conferir-pericias.py` — checagem nova de peso de mesa, e as colisões aceitas passaram a ser declaradas com motivo dentro do próprio validador.

### Decidido — Inteligência sabe, Essência percebe

**Sentir Energia e Percepção saíram de Inteligência e foram para Essência.** É a maior mudança da versão e ela reverte uma decisão da v0.8.

A v0.8 mandou a percepção para Inteligência com uma intenção boa: tirar de Inteligência o papel de atributo-depósito, dando a ela a coisa que mais importa em Jujutsu Kaisen. Com o quadro de perícias escrito, dá para medir o que aquilo produziu — e produziu o oposto:

| | perícias em Int | peso de mesa (Int / Ess) |
|---|---|---|
| v0.15 | 10 de 20 | **56% / 21%** |
| v0.16 | 11 de 23 | **39% / 39%** |

**Inteligência ficou com mais perícias e vale menos**, porque as duas que saíram são as duas mais roladas da mesa. Foi o que a conta mostrou e o que a contagem crua escondia: pedir "quantas perícias cada atributo tem" responde a pergunta errada. A pergunta certa é quanto do que se rola numa campanha depende dele.

E o argumento de ficção fecha com o número: **Essência não sabe nada, ela sente.** Sentir energia amaldiçoada é a sua energia reagindo à de outro — ressonância, não análise. Na obra quem sente melhor não é quem estudou mais; é o Gojo com os Seis Olhos, é o instinto do Todo.

**Percepção foi junto e essa parte não era opcional.** Com Sentir Energia em Essência e Percepção em Inteligência, a mesa teria dois tipos de perceber em dois atributos, e erraria qual rolar em toda cena de aproximação.

### Decidido — o resto do quadro

- **Táticas deixou de existir.** O trabalho dela já estava coberto duas vezes: **Ocultismo** reconhece o que você vê porque conhece o catálogo, **Sentir Energia** lê como a energia se move sem precisar saber o nome. O Nanami faz a primeira, o Todo faz a segunda.
- **Três perícias partidas em duas:** Ocultismo perdeu o lado sagrado para **Religião**, Sobrevivência perdeu o conhecimento para **Natureza**. Religião é o lado de onde o jujutsu veio antes de virar instituição.
- **Entraram Lidar com Animais e Provocar.** Provocar é o inverso de Intimidação: uma faz recuar, a outra faz avançar.
- **Hierarquia foi para Inteligência.** Saber quem deve o quê a quem é conhecimento, não leitura de sala.
- **Ofícios:** Primeiros Socorros saiu e entrou **Herbalismo**; Artesania virou **Entalhador**; Protocolo virou **Burocracia**.

### Decidido — o Caminho para de escolher o personagem

> **Duas perícias fixas e mais quatro à escolha livre, de qualquer lugar do quadro.**
> **Um ofício fixo e outro livre. A Origem continua dando duas perícias.**

Oito de vinte e três — **35%**, o mesmo alvo de sempre, alcançado por outro caminho. Antes eram cinco escolhidas dentro de uma lista de oito por Caminho.

As duas fixas continuam sendo a assinatura: dois Bastiões dividem Atletismo e Intimidação. As quatro livres são o que impede duas fichas do mesmo Caminho de serem a mesma pessoa.

**Sentir Energia não é fixa de nenhum Caminho, e isso é escolha.** Sendo a mais rolada da mesa, fixá-la em um Caminho daria àquele Caminho uma escolha livre a mais disfarçada. Livre para todos, ela vira decisão de ficha — e o feiticeiro ruim de sentir energia passa a caber, que é o Itadori do começo.

**O Evocador entalha.** O ofício fixo dele é Entalhador, e é o que dá razão de existir para o shikigami de madeira e para a boneca que anda.

### Colisão de "Provocar" — registrada e aceita

O manual usa *"sem provocar ataque de oportunidade"* em três lugares, e a peça 3 chega a perguntar *"provocar o quê?"*. Pela regra de checagem em duas direções, isso é colisão.

**Aceita mesmo assim:** a expressão é comum demais em qualquer mesa de d20 para confundir, e "provocar ataque de oportunidade" e "rolar Provocar" nunca aparecem no mesmo tipo de frase. O que muda é que a decisão fica escrita **dentro do validador**, com o motivo, junto de outras duas fracas — *Natureza* encosta na Passiva **Segunda Natureza**, e *História* aparece uma vez em prosa solta. O validador agora falha se aparecer uma colisão que **não** esteja nessa lista, o que separa "aceito" de "não percebido".

### Achado de método

**Contagem não é valor, e o validador estava medindo a coisa errada.** A versão anterior conferia quantas perícias cada atributo tinha e teria aprovado a v0.16 com Inteligência a 48% — número pior que os 50% da v0.15. Ponderando pela frequência com que cada perícia é rolada, a mesma mudança aparece como 56% caindo para 39%.

Vale para o resto do projeto: **antes de medir uma distribuição, perguntar se cada item pesa igual.** Quase nunca pesa.

### Em aberto

- Nome do sistema.
- Nomes definitivos das Trilhas, com as três colisões conhecidas (Régua, Alcance, Fôlego).
- As listas de perícia de cada Origem.
- **Intuição está em cima do muro.** "Ler a pessoa" tem cara de perceber, e ela ficou em Inteligência como dedução. Se em mesa as pessoas rolarem Percepção no lugar dela, muda de casa.
- **Provocar e Intimidação vão brigar na mesa?** A distinção é clara escrita e vaga em jogo.
- Quantas Trilhas um personagem acumula, e em que níveis.
- Como a Trilha Torrente cobra o segundo feitiço da rodada.
- Se a Trilha Coro deixa dono e invocação agirem no mesmo turno.
- Se a curva de dano deve cruzar a coluna Rotina.

---

## [0.15] — 2026-08-06

### Adicionado

- `03-mecanica/07-pericias-e-oficios.md` — o quadro completo. **Vinte perícias e dez ofícios.** Substitui as seções 3 e 4 da peça 4.
- `03-mecanica/conferir-pericias.py` — validador do quadro: contagem por atributo, nome repetido, tamanho das listas de Caminho, fração treinada, perícia órfã e colisão de termo nas duas direções. Passa.

### Decidido

- **Duas listas, não uma.** Perícia pertence a um atributo fixo; **ofício não pertence a atributo nenhum** — o atributo muda conforme o que você faz com ele. Forjar é Força, falsificar é Destreza, saber qual selo o papel pede é Inteligência, e é o mesmo ofício. É a proficiência de ferramenta do d20, e é o que permitiu recheá-la sem inflar a lista de perícias.
- **Perícia sem treino você tenta; ofício sem treino, não.** Qualquer um escala e falha. Ninguém forja por tentativa.
- **Sabedoria dissolvida dentro de Inteligência, como consequência da v0.8.** Ocultismo come arcano e religioso; Sobrevivência come natureza e rastrear; Percepção, Intuição e Medicina vêm inteiras de Sabedoria. As cinco novas de JJK são Sentir Energia, Tecnologia, Táticas, Hierarquia e Pontaria.
- **O Caminho lista oito perícias e três ofícios; você treina cinco e dois.** A Origem dá mais duas perícias. **Sete de vinte — 35%**, exatamente o alvo que a v0.14 calculou. Com a lista de catorze eram 64%, e "ser treinado" não significava nada.
- **Sentir Energia está nas cinco listas e não é de graça** — ocupa um dos cinco espaços. Um feiticeiro pode ser ruim de sentir energia, e o Itadori do começo é isso.
- **PE do Guia: 6.** A regra da v0.14 dizia "6 nos Caminhos de técnica, 4 nos físicos" e o Guia não era nem um nem outro — ficava sem número. A regra passa a nomear os cinco Caminhos em vez de dividir em duas famílias que não cobriam todos.

### Aceito com pergunta de playtest — Inteligência com metade do quadro

**Dez das vinte perícias moram em Inteligência.** Isso a torna o atributo mais valioso fora de combate por larga margem, e a peça 1 já tinha marcado o risco quando Sabedoria foi fundida nela.

Fica assim de propósito: em Jujutsu Kaisen, perceber e saber *é* metade do jogo, e o contrapeso está dentro do combate — Destreza carrega Defesa e iniciativa, Constituição carrega os pontos de vida, e ninguém zera esses dois. A pergunta de playtest é específica: **apareceu alguma ficha com Inteligência 0 ou 1?** Se em três meses nenhuma apareceu, o conserto é um teto de três perícias do mesmo atributo por Caminho.

**Força continua com uma perícia só, e a lista não conserta isso.** Nenhuma cabia sem enchimento: correr, escalar e carregar já são Atletismo, e aguentar dor e fome é leitura de Constituição em qualquer mesa. O segundo trabalho de Força tem que vir de fora do quadro.

### Corrigido — quinze achados de uma revisão cética do material inteiro

Três contradições diretas, em que duas peças diziam o oposto:

- **O golpe canalizado somava arma e Força na peça 5 e não somava na peça 6.** É a regra central do combatente físico escrita ao contrário em dois arquivos. A peça 6 está certa — somando, o físico fica 131% acima da Rotina no nível 2. Peça 5 corrigida, com a conta apontada.
- **Quantas perícias o Caminho dá:** três na peça 4, sete na peça 6. Resolvido pelo quadro novo.
- **A peça 5 ainda listava os Caminhos de rascunho**, incluindo *Leitura*, eliminada por colisão na v0.14. A peça 6 dizia substituir "a seção 4 da peça anterior", mas a peça 5 não tinha aviso nenhum — quem lesse na ordem saía com os nomes errados.

Números que não fechavam:

- **Peça 1:** *"trocar o 5 fixo por um atributo"* — o valor fixo é **2**. Resquício da v0.8, duas linhas abaixo do lugar onde o próprio documento diz 2.
- **Peça 1:** a fórmula de perícia estava sem a condicional de treino.
- **CHANGELOG v0.10:** *"bate no teto no nível 8 ou 12"* — os marcos são 6/10/14, e não existe nível 8 nem 12. Resquício de quando os marcos eram 4/8/12.
- **`conferir-atributos.py` testava CD 12, 16 e 20**, que não existem na escada oficial de 10/14/18/22/26. Trocado, e a tabela da peça 4 saiu confirmada linha por linha.

O `arquitetura.md`, que é o arquivo apontado para retomar o projeto, tinha ficado quatro versões para trás:

- A tabela de refino usava os marcos **4/8/12/16/20/24/28**, substituídos por 6/10/14/18/22/26/30 na v0.10 — a curva inteira saía errada, junto com "o especialista bate no teto no nível 20" e "desperdiça três escolhas".
- A escada da patente dizia **sete degraus**; a v0.7 decidiu **oito**, com o semi-especial.
- A tabela dos três eixos chamava o tamanho do feitiço de **Escala**, três linhas abaixo do texto que decide **Classe**. Nem *Escala* nem *Potência* sobreviveram.
- O problema 1 da seção 4.3 estava listado como aberto. A v0.10 resolveu, e **não pelo conserto que estava proposto lá** — quem resolveu foi o teto fixo de 6 no atributo, que inverte sozinho o valor relativo dos dois lados no meio da campanha. Os degraus de peso continuam valendo, mas como controle de acesso, não como conserto de balanço.

### Registrado — três coisas que a revisão achou e que ficam para depois

**A taxa de acerto aparece com três valores diferentes no material.** A peça 1 diz 65%, o CHANGELOG da v0.8 diz 60%, e o validador entrega **50%** — contra um alvo que também investiu em defesa, que é o caso difícil. O alvo de "3,2 rodadas" foi calculado em cima de 60%; a 50% a faixa real é **3,4 a 4,0 rodadas**. Fica como previsão a medir em vez de número a consertar: quem decide se o combate está arrastado é a mesa, não a planilha.

**A curva de dano cruza a coluna Rotina, e ninguém tinha comentado.** No nível 2 o conjurador está +38% e o físico +69% acima dela; no nível 30 estão 21% e 16% abaixo. A peça 6 reprovou +135% no nível 2 e aprovou +69% na linha seguinte sem tratar a diferença. Não é necessariamente errado — vida é baixa no nível 2 —, mas é decisão não tomada.

**Três nomes de Trilha colidem com o manual**, pela checagem nas duas direções: **Régua** é um dos três Fundamentos de exemplo do manual, **Alcance** é Família *e* Melhoria com catorze ocorrências, e **Fôlego** aparece no feitiço pronto Roubo de Fôlego. E **Ofício** ia colidir com a perícia de ofício — por isso a lista usa *Artesania*. Como os nomes de Trilha já eram todos provisórios, entra na pendência que já existia.

### Em aberto

- Nome do sistema.
- Nomes definitivos das Trilhas, agora com três colisões conhecidas a resolver.
- As listas de perícia de cada Origem. Hoje a Origem dá duas livres, com aprovação do mestre.
- Quantas Trilhas um personagem acumula, e em que níveis.
- Como a Trilha Torrente cobra o segundo feitiço da rodada, contra a regra de ouro nº 6.
- Se a Trilha Coro deixa dono e invocação agirem no mesmo turno.
- Se a curva de dano deve cruzar a Rotina ou acompanhar ela.

---

## [0.14] — 2026-08-06

### Adicionado

- `03-mecanica/06-caminhos-e-trilhas.md` — o quadro de cinco Caminhos com três Trilhas cada. Revisa e substitui a seção 4 da peça anterior.

### Decidido

- **Cinco Caminhos, com nomes conferidos contra o manual:** Bastião (corpo), Vanguarda (arma), Guia (o outro), Emanador (técnica), Evocador (invocações). Os rótulos de rascunho saíram — *Leitura* em particular já aparecia três vezes no Fundamento.
- **Sem multiclasse.** Um Caminho por personagem; as escolhas de nível compram Trilhas dentro dele. Acumular Trilhas do próprio Caminho é o que permite pegar Energia Reversa antes do refino liberar.
- **O Guia não compete em buff, debuff nem cura** — esses moram na técnica e na Forma de feitiço. Ele **alcança**: faz o efeito de outra pessoa durar mais, pegar mais gente ou chegar mais longe. Era o Caminho que não fechava, e é essa a saída.
- **Treinamento em equipamento** em três categorias: armas, proteção e escudo. Escudo é categoria própria porque ocupa uma mão — e mão ocupada **cancela a Restrição Gesto**, que exige as duas mãos livres. Vira decisão de ficha em vez de bug.

### Ataque extra — aprovado, com correção

A coluna Rotina do Fundamento **já é "feitiço + Classe 0"**: o conjurador sempre teve dois golpes por rodada. Então ataque extra no físico não é privilégio, é o espelho.

Mas o golpe canalizado **não pode somar arma nem Força** — ele *é* o feitiço. Com os dois somados e ataque extra por cima, o físico fica 135% acima da Rotina no nível 2 e 32% no nível 10. A regra em três linhas, espelhando a regra de ouro nº 6: golpe canalizado são os dados da Classe e nada mais; golpe simples é arma + Força; um canalizado por turno, e ataque extra é sempre golpe simples.

### Invocação — reprovada como estava, e o conserto

**Uma invocação que age sozinha dobra o dano por rodada; uma horda de três quadruplica** — 504 por rodada no nível 30 contra uma Rotina de 126. Nenhum preço em PE conserta, porque o problema não é recurso, é economia de ação.

**Conserto: você e todas as suas invocações somados entregam uma Rotina.** Com uma, cada um entrega metade; com três, um quarto. Isso entrega exatamente a fantasia pedida sem regra extra — Sombra tem um corpo forte, Enxame tem cinco fracos, e o invocador troca dano pessoal por presença de tabuleiro. É também a leitura correta da obra: as maldições do Geto individualmente são frágeis, o que assusta é o número.

### Energia — fixa pelo Caminho, sem atributo *(revisado)*

**PE por nível: 6 nos Caminhos de técnica, 4 nos físicos. Espírito não entra.**

Com teto de atributo em 6, não existe faixa útil: qualquer divisor grande o bastante para não criar imposto entrega **um ponto** na ficha inteira. Ou o atributo importa de verdade e vira obrigatório — o que a peça 1 evitou de propósito —, ou não importa e só ocupa espaço na cabeça de quem lê. A análise abaixo continua registrada porque o raciocínio vale para qualquer outra tentação de amarrar atributo a recurso.

### Energia — a análise que levou a isso

Duas objeções à proposta de `4 + Espírito/2` para conjurador:

**Cortar a base de 6 para 4 invalida a tabela de PE do manual**, que tem uma coluna inteira de "quantas vezes você lança o seu melhor feitiço" calculada em cima de 6 por nível.

**Espírito/2 dá +50% de PE entre Espírito 0 e 6** — o dobro de usos do melhor feitiço em vários níveis. É o atributo obrigatório pela porta dos fundos que a peça 1 evitou ao tirar atributo da conta do feitiço.

Proposta: conjurador `6 + Espírito/4`, físico `4 + Espírito/4`. Dá +17%, que é sabor e não imposto. O físico com dois terços do combustível é justo porque o golpe simples dele rende ~10 contra os ~4,5 do Classe 0 do conjurador — menos combustível, melhor motor de reserva.

### Múltiplos atributos por Caminho — aprovado, já estava previsto

O mecanismo já existia: o Caminho pode **trocar o valor fixo de 2 do ataque de conjuração por um atributo**. Emanador conjura com Inteligência ou Essência; Bastião canaliza com Força; Vanguarda com Destreza. A troca é neutra em balanço porque os dois crescem +3 na campanha, e não vira imposto porque é opcional.

### Perícias — a lista precisa crescer

Com catorze perícias e 7 do Caminho mais 2 da Origem, o personagem fica treinado em **64% de tudo que existe** e "ser treinado" para de significar algo. Proposta: expandir para 24 a 28, o que leva a fração a 35% e devolve espaço para o resto do grupo brilhar.

### Em aberto

- Nome do sistema.
- Nomes definitivos das Trilhas.
- O quadro completo de perícias (24 a 28) com o atributo de cada.
- Quantas Trilhas um personagem acumula, e em que níveis.
- Como a Trilha Torrente cobra o segundo feitiço da rodada, contra a regra de ouro nº 6.
- Se a Trilha Coro deixa dono e invocação agirem no mesmo turno.

---

## [0.13] — 2026-08-06

### Adicionado

- `03-mecanica/05-caminho-e-combate-sem-feitico.md` — o trabalho de Força, o Caminho e como alguém luta com o corpo num sistema onde o poder mora na técnica.

### Decidido

- **Força governa** ataque corpo a corpo, agarrar, quebrar, Atletismo, capacidade de carga e requisito de arma e proteção. Armas de dado maior e uniformes pesados exigem Força mínima.
- **Golpe canalizado = feitiço de Forma Toque, sem Melhoria e sem Restrição.** Mesma Classe, mesmo orçamento, mesmo custo em PE, e o golpe ainda soma arma e Força por cima.
- **A trava do Caminho:** ele não dá poder novo, muda o que o poder alcança. Mexe em posicionamento, alvo, duração e recuperação — nunca em dados de dano, Classe de feitiço, Melhoria de graça ou cura.
- **Uma Trilha de Caminho pode abrir exceção estreita e paga** na economia de ação — conjurar na Reação uma vez por cena, ou só com Classe baixa. Como recurso de um caminho específico, não direito universal.
- **Quatro Caminhos como esqueleto:** Linha de Frente (Força), Ponta de Lança (Destreza), Retaguarda (Essência), Leitura (Inteligência). O quadro definitivo é taste call.

### Achado — uma arma sozinha não cabe no jogo

O manual já avisava que o combatente físico precisa ficar na coluna Rotina. Rodando a conta, **uma arma entrega de 7% a 65% do que a coluna pede, e a diferença cresce com o nível** — 1,5× de lacuna no nível 2, 11× no nível 30. Não é escolha de dado: trocar d6 por d12 muda três pontos numa lacuna de cem. Falta uma ordem de grandeza inteira, e nenhum requisito de Força ou tabela de arma conserta isso.

O conserto é Canalizar Energia, e a forma dele caiu da conta em vez de ser inventada: os dados de energia que faltam para o golpe atingir a Rotina batem com os pontos que a Classe do nível concede, faixa por faixa. **O golpe canalizado é o feitiço vazio** — o que sobra de um feitiço quando se tira toda a customização e fica só o orçamento bruto. Por isso é aptidão básica de qualquer feiticeiro, e por isso ter técnica continua sendo melhor: a técnica compra Melhorias, o golpe não.

Isso explica de graça três coisas que estavam soltas: por que **Maki** precisa de ferramenta amaldiçoada (sem energia ela não canaliza, e a arma canaliza por ela); por que **socar é a saída quando o PE acaba** (é o equivalente físico do feitiço de Classe 0); e por que **o combatente físico não tem Liberação Máxima** (ele já vive no teto de dano num alvo o tempo todo).

### Registrado sobre requisito de arma

Requisito de Força resolve **acesso, não balanço**. Um dado maior rende cerca de +2 por golpe, o que empata o valor defensivo de +1 de Destreza por volta do nível 5 e fica para trás depois — sem contar iniciativa e três perícias. É bom que exista e dá a Força um trabalho real, mas não é ele que impede Destreza de dominar. Quem faz isso é o Caminho de Linha de Frente.

### Em aberto

- Nome do sistema.
- O quadro definitivo de Caminhos e quantas Trilhas cada um tem.
- A tabela de armas: dados, requisitos e se arma leve compensa de outra forma.
- Quanto custa uma ferramenta amaldiçoada que canaliza sozinha. Precisa ser cara o bastante para não virar padrão.
- Se o golpe canalizado tem teto próprio ou herda o do Fundamento.

---

## [0.12] — 2026-08-06

### Adicionado

- `03-mecanica/04-pericias-e-testes.md` — perícias, escada de dificuldade, de onde vem o treino, fail-forward e a regra do ataque de oportunidade.

### Decidido

- **Perícia = d20 + atributo + maestria se treinado; sem treino, só atributo.** Maestria é o que marca o treino.
- **Por que treino funciona diferente em perícia e em Teste de Resistência:** a oposição é diferente. A CD de perícia é fixa pela dificuldade e não cresce, então o treino pode crescer. A CD de TR cresce com o conjurador, então o treino tem que ser flat ou o não treinado despenca. É a mesma regra da peça 1 aplicada aos dois casos.
- **Escada de dificuldade em cinco degraus nomeados:** 10 rotina, 14 fácil, 18 média, 22 difícil, 26 quase impossível. CD 10 vira automático no fim da campanha de propósito — feiticeiro experiente não rola para arrombar porta comum.
- **Catorze perícias**, nenhuma amarrada a Constituição. **Sentir Energia** é a mais rolada da mesa e mora em Inteligência.
- **Inteligência não concede perícias extras**, ao contrário do costume d20. Ela já carrega percepção, conhecimento e um TR; dar perícias por Inteligência a empurraria de carregada para obrigatória.
- **Treino:** Origem dá duas perícias e um TR; Caminho dá três perícias e outro TR. Cinco perícias treinadas de catorze, e dois TRs de quatro.
- **Falha nunca é "não acontece nada".** Ela entrega custo, complicação ou informação indesejada. Não é só ritmo: é a norma que faz cinco mestres diferentes falharem do mesmo jeito. Corolário: se o mestre não consegue nomear o custo antes de pedir a rolagem, não pede.
- **Ajudar dá vantagem, um ajudante por teste. Teste de grupo passa com metade do grupo.**

### Resolvido — feitiço como ataque de oportunidade

**Ataque de oportunidade é ataque físico**, rolado como ataque comum e pago com a Reação. Conjurar na Reação continua exigindo a Melhoria Reação.

A razão é aritmética: a Melhoria Reação custa Pesada, o que é **metade do orçamento do feitiço** em toda Classe — 67% na Classe 1, 52% na Classe 7. Se qualquer feitiço pudesse virar ataque de oportunidade de graça, a Melhoria viraria peça morta na hora. Uma trilha de Caminho pode abrir exceção limitada, e aí é recurso pago por um caminho específico em vez de bônus universal.

### Confirmado

- **Ação bônus fica.** Existem técnicas que viram ação bônus e a peça Rápido depende disso. Medir uso real no playtest.
- **Uma reação por rodada.** Revisitar só se a competição entre ataque de oportunidade, Melhoria Reação e as Passivas de reação deixar as Passivas mortas.

### Em aberto

- Nome do sistema.
- Se Força precisa de um segundo trabalho: uma perícia é pouco.
- Se treino em perícia tem graus ou é binário. Binário por ora.
- Quais trilhas de Caminho abrem exceção de conjuração na reação, e sob que condição.

---

## [0.11] — 2026-08-06

### Adicionado

- `03-mecanica/03-economia-de-acao-e-iniciativa.md` — o turno, os recursos que ele contém, iniciativa e a régua de preço das Restrições.
- `03-mecanica/conferir-acao.py` — valida a régua, roda dominância por conjunto de recursos e calcula o valor real da Melhoria Adianta. Passa.

### Decidido

- **O turno tem quatro recursos independentes:** movimento (até 9 m, divisível), ação padrão, ação bônus e reação. "Rodada inteira" não é um quinto — é gastar movimento, padrão e bônus de uma vez.
- **Deslocamento base: 9 metros.** Conversa com as distâncias que o Fundamento já usa: fecha metade de um duelo de 18 m num turno, e sair de uma explosão de raio 3 m custa um terço do movimento.
- **Ataque de oportunidade existe.** Sem ele, sair de um corpo a corpo é grátis e a Melhoria Passo perde a razão de existir.
- **Concentração:** um efeito por vez; ao tomar dano, TR Físico contra CD 10 ou metade do dano, o que for maior. É a mesma régua que a Restrição Carregar já usava.
- **Iniciativa é rolada: d20 + Destreza.** Iniciativa fixa seria mais rápida e mais auditável, mas quebraria a Melhoria Adianta — com ordem fixa, quem tem Destreza alta age antes em 100% das rodadas e Adianta vira +2 permanente. É o teste do bônus automático falhando.
- **A régua de preço das Restrições, derivada dos recursos:** Leve consome um recurso, ou meio recurso por dois turnos. Média consome o turno inteiro, ou um recurso mais um risco real.

### Resolvido — a tensão Carregar × Lento, aberta desde a v7.3

O changelog do Fundamento registrou que Carregar dói mais que Lento pelo mesmo preço e não dava para subir sem estourar o fecho de devolução. Com os recursos definidos, não há dominância: Lento consome três recursos deste turno sem risco; Carregar consome um recurso do turno anterior mais o risco. São conjuntos diferentes.

O que faltava era o texto dizer se **quem carrega pode se mover no turno de carga**. Decidido que sim: só a ação padrão vai embora. É a leitura mais natural do texto atual, é o que torna a peça distinta de Lento, e não muda nenhum dos 35 feitiços prontos porque nenhum usa Carregar.

**A lição:** tensão de preço às vezes é lacuna de texto disfarçada. Antes de mexer no número, conferir se a regra diz o que se acha que ela diz.

### Verificado

As onze Restrições do catálogo cabem na régua, e o teste de dominância por conjunto de recursos não encontra nenhum par em que um contenha o outro. O catálogo estava certo — só não tinha como provar.

### Em aberto

- Nome do sistema.
- **Se ação bônus deve existir mesmo.** É a mais herdada das quatro e a que mais custa em tempo de mesa. Duas peças do Fundamento dependem dela. Medir no playtest quantos turnos usam uma.
- **Quantas reações por rodada.** Uma é o padrão, e quatro coisas competem por ela: ataque de oportunidade, a Melhoria Reação e as Passivas Contramedida e Reforço. Competir é bom, mas se ninguém nunca tiver reação sobrando, as Passivas de reação ficam mortas.
- **O valor de Adianta:** entre 4 e 7 pontos percentuais de efeito médio, abaixo do que uma Média costuma entregar.

---

## [0.10] — 2026-08-06

### Adicionado

- `03-mecanica/02-economia-de-atributos.md` — escala, criação, crescimento e teto dos atributos.

### Decidido

- **Escala 0 a 6, o número é o modificador.** A escada de 1 a 30 com o 10 valendo 0 foi descartada: o sistema inteiro já foi montado sem conversão, conversão custa caro com cinco a sete mestres, e a granularidade extra serve para bônus pequenos que este sistema não tem. O d20 clássico carrega essa escada por razão histórica — os modificadores foram inventados depois dos scores.
- **Criação: nove pontos entre os cinco atributos, nenhum acima de 3.** O arranjo padrão é 3·2·2·1·1. O teto de 3 não é arbitrário: é o que faz o atributo investido crescer exatamente +3 na campanha, o mesmo ritmo da maestria.
- **Crescimento:** a cada quatro níveis, passivo de +1 atributo e +1 refino, mais uma escolha entre outro ponto de atributo ou outro de refino com uma aptidão. Sete marcos, nos níveis **6, 10, 14, 18, 22, 26 e 30** — contados a partir do começo da ficha no nível 2, fechando exato no 30. A maestria sobe em três desses marcos (10, 18 e 26), um sim e um não, então nenhum marco fica vazio e nenhum acumula dois ganhos grandes.
- **Teto do atributo: 6, fixo.** Um teto que crescesse com o nível manteria o ponto de atributo sempre valioso e travaria a escolha em "atributo" a campanha inteira.
- **Origem não dá atributo.** Em JJK a origem é a fonte do poder, não o corpo — ser recipiente não dá Constituição, dá um passageiro. Amarrar número à origem criaria a origem ótima por build, que é empurrar a identidade para a camada errada num sistema cujo pilar é a técnica. A origem dá a patente inicial, um traço não numérico e o gancho de ficção.

### Achado

**A curva se auto-equilibra e a escolha não precisa de trava.** O atributo principal bate no teto no nível 10 ou 14; depois disso o ponto de atributo cai num secundário e vale menos, enquanto uma aptidão nova continua valendo o mesmo. O jogador tende a pegar atributo cedo e refino depois sem que nenhuma regra mande — o valor relativo dos dois lados muda sozinho com o tempo. Era o problema 1 da seção 4.3 do esqueleto, e ele se resolve pelo teto fixo em vez de por degraus de peso.

### Em aberto

- Nome do sistema.
- Quantos pontos de perícia, e se perícia é treinada ou tem graus.
- De onde vem o treino nos Testes de Resistência.
- Se Força precisa de um segundo trabalho.

---

## [0.9] — 2026-08-06

### Corrigido — um erro meu que a pergunta do Mizuki encontrou

**O validador da v0.8 tinha um ponto cego.** Ele testava se a chance mudava com o nível **mantendo os atributos fixos**. Isso verifica se o nível cancela, mas não se a **campanha** cancela: o defensor não fica com Destreza 3 para sempre, ele investe e chega a 6. O ataque de conjuração era um valor fixo mais maestria, e maestria crescia +7 enquanto o atributo do defensor crescia +3. A v0.8 derivava 15 a 20 pontos percentuais e passava no teste assim mesmo.

**A regra que ficou:** numa rolagem disputada, os dois lados precisam crescer no **mesmo ritmo**. Não basta os dois crescerem. Atributo investido cresce +3 numa campanha; maestria a cada 4 níveis crescia +7 — rápido demais para substituir um atributo.

### Alterado

- **Maestria sobe a cada oito níveis**, não quatro. De 1 a 4 ao longo da campanha, o mesmo ritmo de um atributo investido. Continua caindo nos marcos de quatro níveis, só que num sim, num não.
- **Maestria saiu da Defesa e do Teste de Resistência.** Ela fica no ataque de conjuração, na CD e nas perícias. Com isso, nenhum número aparece dos dois lados da mesma rolagem — que era exatamente a objeção levantada.
- **Ataques físicos usam atributo direto:** corpo a corpo soma Força, à distância soma Destreza. Sem maestria, porque o atributo já cresce dos dois lados e se anula sozinho.
- **Ataque de conjuração = 2 + maestria**, e o 2 não é gosto: é o número que faz o conjurador empatar com o guerreiro do nível 2 ao 30. Com 5 ele acertava 15 pontos percentuais a mais a campanha inteira, o que seria de graça — o dano dele já vem do orçamento do feitiço.
- **Habilidade de Caminho pode trocar o 2 fixo por um atributo**, e a troca é neutra em balanço porque os dois crescem igual. É por aí que nasce o feiticeiro que conjura pela Força, no molde do Todo.
- **Perícia = atributo + maestria**, e aqui a deriva para cima é o objetivo: +30 pontos percentuais ao longo da campanha. É o único lugar onde crescer é o ponto, porque o mundo não cresce junto — uma fechadura comum continua sendo uma fechadura comum.

### Resultado

Guerreiro, atirador e conjurador acertam **50%** contra um alvo que também investiu em defesa, em qualquer nível do 2 ao 30. Resistir dá 55% sem treino e 65% treinado, também sem deriva. Deriva medida: **zero** em tudo que não deve derivar.

### Lição de método

Verificar invariância contra o nível não basta. **Tudo que cresce numa campanha precisa entrar no teste** — atributo, proteção, equipamento. O validador foi reescrito para variar os atributos junto com o nível, e ganhou uma checagem nova: nenhum termo pode aparecer dos dois lados da mesma rolagem.

---

## [0.8] — 2026-08-06

### Alterado

- **Cinco atributos, não seis.** Sabedoria e Carisma fundiram em **Essência** — vontade, presença, o que você é por dentro e o que isso projeta. O que Sabedoria fazia de percepção migrou para **Inteligência**, que assim deixa de ser o atributo-depósito clássico e passa a carregar o que mais importa em Jujutsu Kaisen: perceber energia amaldiçoada.
- **"Passo" virou "Maestria".** Conferido: não aparece nenhuma vez no manual.
- **A ficha começa no nível 2**, já com um feitiço. Maestria começa em 1 e sobe a cada quatro níveis a partir do 6, fechando exata em 8 no nível 30. O nível 1 fica como opção de campanha — o personagem antes de ser feiticeiro, o Itadori antes do dedo.
- **CD unificada:** `8 + maestria + atributo relevante`, uma forma só para a ficha inteira. Para feitiço, o atributo dá lugar a um **valor fixo de 5**, que é o que impede o imposto de maximizar a estatística de conjuração.
- **Ritmo de combate: 3,2 rodadas é o alvo**, não um defeito a corrigir. O manual precisa passar a mostrar as duas colunas de letalidade, com a de 60% de acerto marcada como a de mesa.

### Corrigido pela conta, antes de virar regra

- **Maestria só para quem é treinado produzia a espiral do d20.** O não treinado caía de 55% para 20% de sucesso entre o nível 2 e o 30 — salvaguarda sem treino virava sentença, e o mestre passaria a precisar saber nível *e* treino do alvo para estimar qualquer coisa. Conserto: todo mundo soma maestria no TR e treinado ganha **+2 fixo em cima**. Mesma intenção, sem a espiral, e treinar passa a valer exatos 10 pontos percentuais para sempre.
- **Defesa sem maestria quebrava o outro lado.** Com o ataque crescendo contra um número parado, o acerto ia de 65% no nível 2 a **100% no nível 30** — nem o 1 natural erraria. Conserto: a defesa carrega maestria igual ao ataque.

### Resultado

Três números batem no mesmo lugar e não mudam com o nível: acertar alvo de Destreza 3 com proteção 1 dá **60%**, resistir com atributo 2 treinado dá **60%**, sem treino dá **50%**. `conferir-atributos.py` passa em todos os invariantes.

### Em aberto

- Nome do sistema.
- Quantos TRs cada personagem é treinado, e de onde vem esse treino — Origem, Caminho ou os dois.
- Se Força precisa de um segundo trabalho: é o único candidato a depósito que sobrou.
- Quanto Inteligência realmente pesa na mesa. Ficou a mais carregada das cinco.

---

## [0.7] — 2026-08-06

### Adicionado

- `03-mecanica/01-atributos-acerto-defesa.md` — a primeira peça de mecânica com número. Atributos, rolagem de acerto, defesa e Teste de Resistência.
- `03-mecanica/conferir-atributos.py` — validador dessas fórmulas, com contrato de invariantes. Roda antes de fechar qualquer versão que mexa nelas. Passa.

### Decidido

- **O nível entra dos dois lados da conta e se cancela.** Ataque e defesa crescem no mesmo passo; CD e resistência também. O que sobra é a diferença de atributo. Bounded accuracy deixa de ser disciplina a manter e vira consequência da fórmula, e um mestre nunca precisa saber o nível para saber a chance.
- **Passo = nível ÷ 4**, arredondando para baixo. Mesma cadência do refino e do atributo. É a única coisa que cresce com nível.
- **Seis atributos com os nomes clássicos:** Força, Destreza, Constituição, Inteligência, Sabedoria, Carisma. O número é o modificador direto, escala 0 a 6, sem valor separado e sem tabela de conversão. É escolha deliberada e não herança: compra custo de ensino zero, e o custo de seis números não expressarem o personagem não pesa porque a identidade mora na técnica. Todos os seis conferidos contra o manual — nenhum é termo definido lá.
- **Quatro Testes de Resistência, não seis**, para eliminar salvaguarda-depósito: Físico (Força **ou** Destreza, declarado na criação e travado), Vigor (Constituição), Intelecto (Inteligência), Espírito (Sabedoria **ou** Carisma, também travado).
- **Cada atributo tem um serviço fora do TR**, ou o não-escolhido de cada par vira lixo de ficha. Duas amarras são específicas de JJK e resolvem o problema clássico de Sabedoria e Carisma: **Sabedoria percebe energia amaldiçoada** e **Carisma negocia Pactos**.
- **O tipo de dano da técnica decide qual TR o feitiço força**, por padrão. Fogo, corte e peso pedem Físico; veneno pede Vigor; ilusão e voz pedem Intelecto; o que encosta em alma pede Espírito. Uma Melhoria pode trocar.
- **Dano na alma passa a forçar TR de Espírito**, e Integridade volta a ser só reserva.
- **Fórmulas:** bônus de conjuração = 3 + passo · CD = 10 + bônus · defesa = 10 + passo + Destreza + proteção · TR = d20 + atributo do TR + passo.
- **Defesa evita ser acertado; RD reduz o que passou.** Cobrir-se de energia é a fonte natural de RD, e é por isso que ela é aptidão básica de todo feiticeiro.
- **Patente com oito degraus**, incluindo semi-especial: grau 4, 3, semi-2, 2, semi-1, 1, semi-especial, especial. Semi-especial é extensão deliberada — pelo que se sabe não existe no cânone, e é o limbo dramático mais rico da escada.

### Achados sobre o manual existente

**O Fundamento diz "Teste de Resistência" dezoito vezes e especifica de qual apenas uma vez** — no dano de alma. As outras dezessete não dizem contra o quê se resiste. Com quatro TRs, a lacuna vira profundidade em vez de continuar aberta.

**"Teste de Resistência de Integridade" é ambíguo:** o manual manda rolar sem dizer o que se soma, e Integridade é uma reserva, não um modificador. Resolvido acima.

A tabela de letalidade do Fundamento supõe que **todo ataque acerta**: ela divide vida pelo pico de dano. Com taxa real de acerto de 60%, o combate leva de 2,8 a 3,3 rodadas em vez de 1,7 a 2,0. Não é erro de conta — a coluna mede o que diz medir —, é descasamento entre o que a tabela informa e o que o mestre decide com ela. Feitiços que resolvem por Teste de Resistência ficam mais perto da coluna original, porque neles o dano passa mesmo no sucesso do alvo.

### Em aberto

- Nome do sistema.
- O ritmo de combate desejado, à luz do achado acima.
- Se algum atributo deve entrar na conta do feitiço (hoje nenhum entra — é o que faz o nível cancelar).
- Se PE deve receber contribuição de atributo (hoje cresce só com nível).
- Se o generalista deve ter alguma aptidão garantida.
- Os degraus de peso das aptidões, amarrados ao refino atual.

---

## [0.6] — 2026-08-06

### Decidido

- **Tamanho do feitiço passa a se chamar Classe.** "Um feitiço de terceira classe". Soa como classificação burocrática, o que combina com uma sociedade jujutsu que registra e cataloga. Volume e Fluxo ficam registrados como alternativas.
- **O chassi passa a se chamar Caminho**, com Trilhas dentro. Consequência obrigatória da decisão acima: a mesma palavra não pode significar as duas coisas. Vocação e Estilo ficam como alternativas livres.
- **Progressão de Refino fechada:** passivo e escolha ao mesmo tempo, teto 10, começo em 1. A cada quatro níveis o personagem ganha refino e atributo de graça e escolhe onde recebe o bônus extra. Especialista chega ao teto no nível 20; generalista termina em 8 no nível 28.
- **Trava que faz o Refino fechar:** com o refino no teto, escolher refino ainda concede a aptidão. Sem ela, o especialista desperdiça três escolhas depois do nível 20.

### Nota de método

Ao checar colisão de nome contra o manual, separar **termo definido** de **prosa solta**. As palavras *caminho*, *papel*, *função* e *classe* aparecem no Fundamento uma ou duas vezes cada, sempre em frase corrida. Isso não é colisão — vira colisão quando a palavra carrega definição. Livres de qualquer uso: vocação, estilo, postura, trilha, perfil.

### Em aberto

- Nome do sistema.
- Se o generalista deve ter alguma aptidão garantida (hoje termina com zero).
- Os degraus de peso das aptidões, amarrados ao refino atual.
- Onde a Regra da técnica entra na ordem de criação.

---

## [0.5] — 2026-08-06

### Adicionado

- `02-esqueleto/arquitetura.md` — o esqueleto do sistema. Mapeia o que o Fundamento já resolve, os onze buracos em volta ordenados por carga, a estrutura de criação de personagem em cinco camadas e as travas de mundo compartilhado. Sem número nenhum, de propósito.

### Decidido

- **Três eixos separados:** Nível (poder mecânico, da ficha), Grau (patente social, da instituição) e o tamanho do feitiço. É o que permite o Yuta nascer no topo da patente sabendo pouco, e o Itadori ter poder sem reconhecimento.
- **A colisão do Grau se resolve renomeando o tamanho do feitiço, não a patente.** O Grau-tamanho está entranhado no manual; o grau-patente está entranhado na cabeça da Guilda há anos porque é o termo da obra. Dá para vencer um manual, não o vocabulário de uma comunidade. Nome provisório: **Potência**.
- **Patente com sete degraus**, incluindo os semi: Grau 4, 3, semi-2, 2, semi-1, 1, especial. Funciona porque a patente não carrega número mecânico — ela compra acesso, autoridade, obrigação e risco.
- **Estrutura do personagem em cinco camadas:** Origem, Chassi, Técnica, Refino e Aptidões, Pactos.
- **Trava do chassi:** ele não dá poder novo, muda o que o poder alcança. Mexe em posicionamento, alvo, duração e recuperação, nunca em número de dano. Escolhido na criação, com poucas escolhas de trilha depois.
- **Trava das aptidões:** não produzem dano e não escalam com nível. São binárias, e o refino governa confiabilidade e custo, não potência. É o que as mantém fora da economia do Fundamento.
- **Morte no modo não letal não vira regra.** O peso vem de consequência no mundo, arbitrada pelo mestre com apoio de perícia e rolagem mundana. Não fura o filtro do multi-mestre porque o filtro protege os números, não a ficção — consequência narrativa não é portátil entre mesas.

### Em aberto

- Nome do sistema.
- Nome definitivo do tamanho de feitiço (Potência é provisório; Volume e Fluxo são as alternativas registradas).
- Como equilibrar a escolha entre refino e atributo, hoje provavelmente dominada pelo refino.
- Se a escala de refino é 1–7 ou existe outra fonte de refino além do nível.
- Onde a Regra da técnica entra na ordem de criação.

---

## [0.4] — 2026-08-06

### Alterado

- `design-mecanicas-rpg` ganhou a seção **"O nome é parte do design"**: checagem de colisão de termo para fora do sistema (palavra que já significa outra coisa no hobby) e para dentro. Veio do retorno do Mizuki de que "Vulnerável", na maior parte das mesas, significa *tomar mais dano* e não *ficar mais fácil de acertar*.
- `redacao-acessivel-rpg` ganhou **"Presunção sobre o que você não viu"**: quando revisar um trecho exige presumir coisa sobre o resto do material, perguntar antes de reescrever; se tiver que seguir, marcar a presunção no ponto do texto onde ela pesa, não numa nota no fim. Veio do retorno de que declarar a presunção é melhor que escondê-la, mas os dois perdem para perguntar.
- A seção de colisão de termo da `redacao-acessivel-rpg` passou a cobrir também colisão externa.

### Corrigido

- Falso negativo na correção automática do `eval-3`: a asserção "diz quando parar de testar" exigia as expressões "parar de testar" ou "critério de saída", e a resposta dizia "o sinal de parar continua o mesmo de sempre: quando o retorno de uma rodada só repete o da anterior, para". A regex foi corrigida e a execução com skill passou de 6/7 para 7/7. A média com skill subiu de 92,2% para 95,8%.

---

## [0.3] — 2026-08-06

### Adicionado

- Quatro skills de apoio, escritas e instaladas na conta: `design-mecanicas-rpg`, `balanceamento-simulacao`, `playtesting-rpg` e `redacao-acessivel-rpg`. Cópia de trabalho em `skills/`, com os arquivos de apoio que a versão instalada traz embutidos.
- `workspace-skills/iteration-1/` — nove execuções de teste (quatro com skill, quatro linha de base morna, uma linha de base fria), com `eval_metadata.json`, `timing.json` e `grading.json` por execução, mais `benchmark.json`.
- `workspace-skills/revisao-iteracao-1.html` — visualizador de revisão, abre no navegador.
- `workspace-skills/montar-benchmark.py` — o script que gera tudo isso, com as ressalvas de método no cabeçalho.
- `ESTADO-ATUAL.md` — ponto de retomada do projeto.

### Decidido

- Mecânica de resolução: **d20**. O Fundamento já é arquitetura d20 (CD, Teste de Resistência, RD, vantagem) e o teto que o dossiê exigia já existe nele, no orçamento em vez de no dado.
- Recurso central: energia amaldiçoada como pool numérico.
- Progressão numérica contínua, com Nível separado de patente.
- Morte: misto letal / não letal, declarado por mesa.
- Guilda: 5 a 7 mestres ativos, 2 a 3 mesas por semana.

### Auditoria

- Verificado que nada da sessão interrompida ficou truncado: os 21 arquivos criados estão íntegros, os scripts rodam e as oito referências internas das skills resolvem.
- A execução que faltava (`eval-3` sem skill) foi rodada em duas condições distintas, morna e fria, para separar "skill contra Claude que leu o dossiê" de "skill contra nada".

### Em aberto

Nome do sistema. E uma colisão de termo a resolver: **Grau** significa tamanho de feitiço no Fundamento e também patente do feiticeiro em JJK. Renomear a patente antes de a comunidade adotar.

---

## [0.2] — 2026-08-05

### Adicionado

- Comparador de curvas (`03-mecanica/comparador-de-curvas.html`) — ferramenta interativa que calibra seis mecânicas na mesma chance de sucesso e compara o formato da curva de progressão. Abre no navegador, funciona offline exceto pela biblioteca de gráfico.
- Dossiê de metodologia (`01-pesquisa/dossie-de-metodologia.md`) — lentes de decisão, espaço de design, mundo compartilhado multi-mestre, matemática de dado calculada, metodologia de playtest, estrutura de manual e leitura de IP.
- Dez travas de arquitetura que a fase de esqueleto herda (seção 8 do dossiê).

### Alterado

- Pitch: nova pergunta em aberto sobre o tamanho real da Guilda (nº de mestres e jogadores ativos), porque a consistência entre mesas depende disso.

### Decidido

- Ferramenta de probabilidade: `dice-calc` (Python, roda local, compila código do AnyDice). Testado e funcionando.
- Ciclo de playtest: 5 pessoas × 3 rodadas, com correção entre rodadas, em blocos temáticos de duas semanas (formato copiado do playtest público do Pathfinder).
- Estrutura do material final: quick-start jogável na frente do livro, referência atrás — decisão de estrutura, não de diagramação.
- Progressão será tabelada ou por gatilho, nunca discricionária do mestre, e com teto (bounded accuracy) — requisito derivado do personagem persistente entre mestres.

### Revisado

- Dossiê passou por revisão independente: corrigidos um erro de célula na tabela de +1 em 2d6, arredondamento inconsistente na tabela de vantagem, rótulo ambíguo na tabela estilo Blades e a data/premiação do Fabula Ultima.

---

## [0.1] — 2026-08-05

### Adicionado

- Pitch de design (`00-fundacao/pitch-de-design.md`) — visão geral, três pilares, restrições duras e perguntas em aberto.
- Estrutura de pastas do projeto.

### Decidido

- Base ficcional: Jujutsu Kaisen, como material de fã gratuito. Sem venda, sem monetização.
- Contexto de jogo: server de Guilda com múltiplos mestres e mini-campanhas; personagem persistente entre mesas.
- Formato: roleplay por texto entre sessões, rolagem majoritariamente ao vivo.
- Tom shounen de ação; crunch equilibrado.
- Primeiro entregável é esqueleto estrutural, não regra jogável.

### Em aberto

Mecânica de resolução, recurso central, funcionamento do rank no server, molde de técnica inata, tratamento de morte e nome do sistema.
