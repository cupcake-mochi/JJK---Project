# 15 — Invocações

**Fase 4, décima quinta peça.** O sistema de criação de invocação: iniciativa, o modelo da Matilha, a ficha, o custo, a morte, o retorno e o catálogo. O validador dono é o `conferir-invocacoes.py`, com as **trinta e duas** checagens do §5.
Versão v0.58 — 14/08/2026

> **O nome é decisão escrita, e não descuido.** `Invocação` sai **OCUPADO** na triagem: é **Tema** do manual, no grupo *Criação* do catálogo do apêndice. Tema não carrega mecânica — o próprio manual diz isso na abertura da Descrição —, então o choque é de vocabulário e não de regra. **O Tema e esta peça são coisas diferentes:** um é rótulo de sabor pendurado numa técnica, a outra é a máquina que põe um corpo no campo. O §4 tem a triagem inteira, com os dois nomes que saíram livres.

Aberta como rascunho na **v0.50**, quando a fila foi reordenada. A Q1 à Q5 fecharam entre a v0.51 e a v0.53; o catálogo foi escrito entrada por entrada na v0.53; a amarra ganhou número na v0.53 e as faixas de alcance na v0.55; a fórmula de vida ganhou o termo de tipo e o retorno fechou na v0.57. **Na v0.58 o validador entrou, e foi aí que ela deixou de ser meia peça.** *A Q6, que era da peça de Trilhas, **fechou na v0.63** — o número de cada concessão está na tabela do fim do §3.7, e as duas dominâncias que o validador declarava sumiram.*

---

## 1. O que já está decidido, e não se rediscute aqui

Três coisas chegam prontas. Elas não são ponto de partida para conversa — são o contorno dentro do qual a peça tem que caber.

> **Você e todas as suas invocações somados entregam uma Rotina.**
> Com uma invocação, cada um entrega metade. Com três, cada um entrega um quarto.

Isso é a **peça 6, seção 4**, e o argumento por trás dela está escrito lá com a tabela: uma invocação que age sozinha **dobra** o dano por rodada, três **quadruplicam**, e no nível 30 a horda chega a `432` contra uma Rotina de `108`. A peça 6 fecha dizendo que isso **não tem conserto por preço** — não é recurso, é economia de ação.

As outras duas:

- **O Coro não custa nada a mais** (peça 6 §3.1). O dono e a invocação agem no mesmo turno, e sai de graça porque o orçamento dividido é **teto de saída, não de número de ações**. Isso já foi decidido na v0.24 e conferido de novo na v0.34.
- **O Caminho não dá dados de dano** (peça 5 §4, reconfirmada). O que sobra para o Evocador conceder é posicionamento, alvo, duração, recuperação, troca do fixo do acerto por atributo, e exceção estreita e paga na economia de ação.

**E o Fundamento não produz invocação hoje.** Conferido no `.docx`, reconferido na v7.9: `Invocação` aparece **só como Tema**, no grupo *Criação* do catálogo do apêndice — e Tema não tem efeito mecânico (o manual diz isso na abertura da Descrição). Não existe Forma nem Melhoria que ponha um corpo que age no campo. Então não há duas portas para a mesma coisa, e a peça não corre o risco de contar o mesmo poder duas vezes — **que era a suspeita óbvia, e a checagem desmentiu.**

## 2. O que a pesquisa externa trouxe, e é aqui que aparece o buraco

Quatro levantamentos, e o achado que interessa não é sobre dano.

**PF2e, Summoner.** O eidolon não é um segundo personagem: existe uma ação chamada `Act Together` em que o número de ações gastas decide quantas cada um dos dois recebe, e o eidolon tem que ficar a até 30 m do dono. **É a mesma intuição da peça 6 §4 num eixo diferente** — lá se divide saída de dano, aqui se divide ação. Vale como confirmação de que o formato é o certo, não como coisa a importar.

**5e 2014, `conjure animals`.** O modo de falha mais documentado do hobby, e ele tem **duas metades**:

| metade | o que acontece | a peça 6 §4 cobre? |
|---|---|---|
| dano e economia de ação | oito lobos fazem mais que qualquer feitiço de mesmo círculo | **sim** |
| **tempo de mesa** | o combate para. Os outros jogadores esperam vendo oito lobos morderem, um de cada vez | **não** |

**5e 2024 trocou a família inteira por causa da segunda metade**, e o motivo publicado é operacional: mestre tendo que abrir ficha de monstro, ter miniatura para todos, e o combate travando. A saída deles foi **uma criatura só**, espectral, ocupando um tile, que **não se divide** e que **age na iniciativa do dono**.

**13th Age, mooks.** Quando o sistema quer horda de verdade, ele para de tratar corpo como corpo: o dano se contabiliza contra **o bando inteiro** e um mook tem um quinto da vida de um monstro normal, com o excedente cascateando para o próximo.

> **O buraco, dito direto: a regra da peça 6 §4 preça o dano da Matilha e não preça o tempo dela.** *"Um quinto da Rotina em cada, cinco corpos no campo"* é justamente a montagem que os dois sistemas acima tiveram que construir máquina especial para segurar. **Cinco fichas agindo por rodada custa o mesmo tempo de mesa quer cada uma faça 25 de dano ou 5.**
>
> E o projeto **já mede esse eixo** — a lista de playtest do `ESTADO-ATUAL` pergunta *"alguém usa ação bônus?"* com a justificativa *"é a peça mais herdada do turno e a que mais custa tempo de mesa"*. O eixo existe; ninguém tinha apontado ele para cá.

### E o que cada um faz com a iniciativa, lido do texto de regra

Levantado para fechar a Q1, e é a metade que o levantamento acima não tinha ido buscar. **Seis sistemas, texto citado e não lembrado:**

| sistema | o que o texto diz | onde a invocação age |
|---|---|---|
| 5e 2014, `conjure animals` | *"Roll initiative for the summoned creatures **as a group**"* | uma casa para o bando |
| 5e 2024, `Summon Beast` | *"**shares your Initiative count**, but it takes its turn immediately after yours"* | na casa do dono |
| 5e 2024, `conjure animals` | virou **emanação** — uma pack que você move com o **seu** movimento | nenhuma casa |
| PF2e, Summoner | *"you can use any of your actions **for yourself or your eidolon**"* | dentro do turno do dono |
| PF2e, companheiro animal | trait `minion`: *"gains 2 actions **during your turn**"* | dentro do turno do dono |
| 13th Age, mooks | um mob = **um** número de iniciativa; separar em mobs é separar números | uma casa para o mob |

**Zero de seis dão um número de iniciativa por corpo.** Nem o 5e 2014, que é o caso famoso de quebrar — ele já rolava uma iniciativa para o bando inteiro. **Quatro dos seis põem a invocação na casa do dono.**

## 3. As perguntas, na ordem em que uma trava a outra

**Q1 — FECHADA.**

> **A invocação compartilha o número de iniciativa do dono e age logo depois dele.** Não abre casa nova na ordem, com um corpo ou com cinco.

O argumento e as contas estão no §3.1. *Esta linha dizia **"só a Q6 continua aberta"** até a v0.63; ela fechou, e com ela a peça inteira.* A Q1 fechou sem criar dependência nova em nenhuma das outras — que era metade do trabalho dela.

**Q2 — FECHADA.**

> **A Matilha é uma ficha com cinco corpos.** Uma barra de vida só, e o dano que passa de um corpo **cascateia** para o seguinte. Os cinco corpos continuam no campo, com posição cada um.
>
> **A rodada dela se resolve em pool:** os cinco d20 saem de uma vez, conta-se os acertos, e **o dano dos que acertaram se soma**. Cada corpo declara o próprio alvo **antes** da rolagem.

Cinco corpos ficam — *decisão do Mizuki, ancorada na obra:* **"no próprio anime não se vê o Geto invocando muitas maldições simultaneamente"**. A peça 6 §4 não é tocada.

O argumento está no §3.2.

**Q3 — FECHADA.**

> **O ritmo é do dono e o valor é dela.** A maestria dele entra em toda rolagem dela; os atributos que fazem a conta são os dela, com o orçamento da peça 2.
> **Vida e deslocamento** = fórmula própria — a vida no molde da do Caminho, o deslocamento fixo em `9` metros.
> **Vida** = `base do tipo + (por nível do tipo + a Constituição dela) × nível do dono`.
> **A forma é orçamento de pontos**, no molde do Fundamento, **com três montagens prontas junto** — uma por Trilha.
> **A ficha tem duas camadas:** `Traço`, que é o que a invocação **é** — voa, carrega, rastreia —, e `Comando`, que é o que ela **faz** quando o dono gasta a ação padrão nela.
> **Ela tem os cinco atributos, e eles são dela** — nove pontos na criação com teto `3`, e `+1` por marco, como qualquer ficha. **O ritmo é do dono:** a maestria dele entra em toda rolagem dela.
> **O orçamento é `8` no nível 2 e sobe `+4` por marco, até `36` no 30.**
> **A amarra são 18 metros.** Além disso a invocação não pode ser comandada — e não some.
> **O catálogo tem 19 entradas compráveis**, mais o `Investir`, que custa 0 e toda invocação tem.

O argumento do princípio está no §3.3, o dos números no §3.6 e o do catálogo no §3.7.

**Q4 — FECHADA.**

> **Invocar custa `1 × a sua maior Classe` de PE e a sua ação padrão.**
> **Comandar a invocação, a cada rodada, custa a sua ação padrão.** Sobram movimento, ação bônus e reação.
> **Sem exceção de "a primeira é grátis"** — e a cena do Megumi com o lobo em campo antes da luta continua funcionando, porque fora de combate a ação não custa nada.

O argumento está no §3.4. **E o teto da peça 6 §4 deixou de precisar de policiamento:** com o comando custando a ação padrão, o dono e a invocação ficam mutuamente exclusivos na rodada, e a soma de uma Rotina **cai da economia de ação em vez de ser decreto.**

**Q5 — FECHADA.**

> **A invocação some no zero, sem estado intermediário.** Sem `Inconsciente`, sem Sequela, sem Cicatriz — ela não é personagem.
> **Área causa o dano uma vez no pool, e a invocação é vulnerável a ela: dobro.** Não é dano por corpo.
> **Ela morre em definitivo** — o talismã se desfaz, o corpo se perde, a invocação de técnica ou a maldição domada é exorcizada — **se o excedente passar de metade da régua, ou se um único golpe causar a régua inteira. A régua é `5 ×` a vida que a fórmula do tipo dá, e ela é a mesma para qualquer corpo.**

O argumento está no §3.5. *E o dilema que esta pergunta carregava desde a v0.50 dissolveu na Q4, sem ninguém precisar decidir nada.*

**Q6 — as três Trilhas com número. FECHADA na v0.63**, pela régua da Q3 de Trilhas.

> **O que a Trilha concede não sai do orçamento da ficha.** `Servo` dá um corpo forte, `Matilha` dá os cinco, `Coro` dá a exceção de economia de ação — atacar e comandar na mesma rodada. **O orçamento compra `Traço` e `Comando` por cima.**

**E o número de cada concessão está na tabela do §3.7**, no fim daquela seção: o `Servo` leva **o orçamento da ficha mais metade** e o **corpo forte** — o pool inteiro da `Matilha` num corpo só —, e as outras duas ficam como estavam. *O que destravou não foi um número: foi descobrir que o `Servo` estava dominado **por falta de eixo**, e que o conserto era uma coluna nova na matriz.*

## 3.1 A Q1, e por que ela fechou na casa do dono

Três saídas estavam na mesa. Uma morreu na conta, uma perdeu no placar, e a terceira é a que ficou.

| | como funciona | precedente |
|---|---|---|
| **A** | cada corpo rola a própria iniciativa | **0 de 6** |
| **A'** | o bando rola uma iniciativa, separada da do dono | 2 de 6 |
| **B** | tudo na casa do dono | **4 de 6** |

### O A morreu, e não foi por dano

A conta de iniciativa da peça 3 §5 (`d20 + Destreza`, empate pela maior Destreza, persistindo o jogador) reproduz a tabela do Adianta exata — 52,5 / 57,2 / 66,0 / 38,2 contra os 52 / 57 / 66 / 38 publicados. Rodada em cima dela, *"pelo menos um corpo meu age antes do inimigo"*:

| corpos | com casa por corpo | na casa do dono |
|---|---|---|
| 1 — sem invocação | 52,5% | 52,5% |
| 2 — Servo, Coro | 77,4% | 52,5% |
| 5 — **Matilha** | **97,6%** | 52,5% |

**Ele escala com o número de corpos, e ninguém pagou por isso.** É literalmente o teste que a **peça 3 §5** usou para rejeitar iniciativa fixa: *"um bônus que a montagem óbvia sempre alcança não é bônus, é a linha de base com um passo a mais"*. E cria dominância da Matilha sobre as outras duas Trilhas num eixo que a peça 6 §4 não preça.

> **O contra-teste é o que fecha.** A mesma conta rodada no **dano** — *"que fração do meu output da rodada cai antes de o inimigo agir"* — dá **52,5% nas três saídas, em todas as montagens.** A conta de dano empata. **É a confirmação numérica do buraco do §2:** a peça 6 §4 preça dano, e esta pergunta não é de dano.

Somando o filtro multi-mestre — casa por corpo obriga **seis** frases novas (a Destreza da invocação, quem entra no meio do combate, invocada depois do próprio turno age quando, empate entre corpos do mesmo dono, em que janela se mede a Rotina somada) contra **uma** —, o A sai sem precisar de escolha.

### E o A' perdeu por dois números

**A rodada perdida — 47,5%, exato.** `P(a casa do bando cair acima da casa do dono) = 190/400`. Se a invocação é conjurada em combate, em quase metade das lutas ela nasce depois da própria casa e só age na rodada seguinte. Num combate de 3,4 rodadas isso é **29% do tempo de vida dela**, perdido por uma rolagem que aconteceu antes de ela existir.

**A corrente do Coro.** A peça 6 §2 escreve o Coro como *"o seu golpe e o delas **se encadeiam**"*, e a §3.1 diz que Arremate e Coro **trocam** o Classe 0 pelo golpe simples. Com casa separada, inimigos agem no meio:

| inimigos | corrente quebrada | inimigos na janela |
|---|---|---|
| 2 | 43,5% | 0,57 |
| 4 | **58,7%** | 1,14 |
| 6 | 66,4% | 1,71 |

Na casa do dono, 0,0% e 0,00. **E o efeito é assimétrico entre as três Trilhas** — quebra o Coro e não encosta no Servo nem na Matilha, que não encadeiam nada. É o tipo de coisa que a matriz de dominância do §5 existe para pegar.

**E o argumento que mais pesou é estrutural.** A Q1 existe para destravar as outras cinco. **O A' cria duas dependências novas em vez de fechar:** precisa da Destreza da invocação (Q3) para rolar, e o tamanho da rodada perdida só se sabe depois de a Q4 dizer quando se invoca. A casa do dono não precisa de nenhuma das duas.

### O que o A' comprava, e por que não bastou

Duas coisas, e uma delas é minha e estava errada.

**A que vale:** dois momentos na rodada — as maldições agindo no ritmo delas em vez de como extensão do turno do dono. Isso é ficção boa, e foi levado a sério.

**E uma segunda correção, achada quando a Q4 chegou:** eu tinha escrito na conversa que *"pool compartilhado de ações morre por texto"*, citando a peça 6 §3.1. **A frase inteira diz o contrário:** *"É teto de saída, não de número de ações. Os dois golpes do dono e o da invocação continuam saindo do mesmo orçamento — **as ações se redistribuem**, o dano não sobe."* **"As ações se redistribuem" é exatamente pool compartilhado**, e é o que a Q4 acabou escolhendo. *Ler meia frase e concluir dela é o mesmo defeito de escrever resumo por cima de tabela.*

**A que não vale, e fica registrada porque o erro é meu:** eu tinha apresentado a *"janela de contra-jogo"* como ponto forte do A' — com casa separada, 1,14 inimigo por rodada age no meio dos meus corpos, contra zero na casa do dono. **Não é vantagem.** Todo personagem deste sistema age em bloco único no turno dele; nenhum inimigo age entre os dois golpes de um Bastião. **Zero janela é a norma, e quem é anomalia é o A'.** A janela que ele devolve não conserta nada, e o que ela custa é a corrente do Coro.

*E duas correções de número, da primeira passada para a segunda:* o precedente externo saiu como *"1 de 6 e 5 de 6"* e é **2 e 4** — o mob do 13th Age tinha caído no balde errado por eu ter contado mob como corpo; e a corrente do Coro saiu como *"54%"* e é **58,6%**, porque o placar levou um número escrito à mão em vez do que o script imprimiu. Nenhuma das duas muda a conclusão. **Contar sintoma não é contar causa, e número escrito à mão ao lado de script que roda é a mesma família.**

*E na revisão cética os três números da corrente saíram de simulação e foram refeitos por enumeração exata* — `43,5` · `58,7` · `66,4` no lugar de `43,4` · `58,6` · `66,6`. **Quando existe conta fechada, simulação é aproximação com cara de medida.**

## 3.2 A Q2, e por que ela fechou em uma ficha com cinco corpos

Quatro máquinas na mesa, e elas formam uma escada — do mais granular ao menos.

| | máquina | texto de regra |
|---|---|---|
| **M1** | cinco fichas — 5e 2014, `conjure animals` | oito bichos, ficha própria cada |
| **M2** | mook — 13th Age | *"a mook's hit point value is **one-fifth** that of a regular monster"*, com o excedente **cascateando** para o próximo. Mas *"mooks move and attack **individually**"* |
| **M3** | troop — PF2e | uma ficha, quatro segmentos; *"perde um segmento"* a 1/3 e 2/3 da vida; *"**instead of standard Strikes**, the troop has special actions"* — o bando ataca em emanação |
| — | emanação — 5e 2024, `conjure animals` | zero corpos, zero fichas: uma pack que se move com o movimento do dono |

### Duas coisas que a conta fechou antes de qualquer escolha

**Pool único implica cascata.** Para desperdiçar excedente é preciso saber em qual corpo o golpe bateu — e aí voltaram as cinco barras. **"Pool sem cascata" não existe: ele é o M1 com a soma escrita na margem.** Não era opção, e chegou a parecer uma.

**O M3 morre no swing.** Cortar para um ataque do bando faz a Matilha errar a rodada inteira em metade das vezes:

| | 5 ataques (M1, M2) | 1 ataque do bando (M3) |
|---|---|---|
| rodada em que a Matilha não causa nada | **3,1%** | **50%** — dezesseis vezes |
| CV do dano da rodada | 0,45 | **1,00** |

A peça 6 §4 escreve a identidade dela como *"as maldições do Geto individualmente são frágeis. **O que assusta é o número**"*. **Um dado só apaga exatamente isso**, e nenhum ganho de tempo de mesa paga.

### O que o M2 custa, e onde o preço aparece

O M1 e o M2 gastam **as mesmas 26 a 30 rolagens por combate** — a barra única é contabilidade, não tempo. O que ela troca é durabilidade, e a troca tem limiar:

| `D / h` | o golpe do inimigo faz | M1 aguenta | M2 aguenta |
|---|---|---|---|
| 0,50 | mata meio corpo | 10 golpes | 10 — **empatam** |
| 0,60 | | 10 | 8,3 — 83% |
| 0,75 | | 10 | 6,7 — 67% |
| 1,00 | mata exatamente um | 5 | 5 — **empatam** |
| 1,50 | mata um e meio | 5 | 3,3 — 67% |
| 2,00 | mata dois | 5 | 2,5 — **50%** |
| 3,00 | mata três | 5 | 1,7 — 33% |

> **A regra é uma frase, e não é a que eu tinha escrito aqui.** *A primeira redação dizia "abaixo de `D = h` os dois são idênticos", e ela é falsa: em `D = 0,75h` o M2 dura 67%.* **Os dois só empatam quando `h/D` é inteiro** — quando o golpe do inimigo divide a vida de um corpo exatamente. **O M1 arredonda o golpe para cima até fechar um corpo, e o M2 não; o arredondamento *é* o desperdício.** Acima de `D = h` o arredondamento vira `D/h`, e a distância cresce sem teto.
>
> *Achado na revisão cética, rodando a fórmula em vez de reler a frase. A tabela da versão anterior já tinha a linha de `0,75` dentro do script e eu escrevi o resumo por cima dela sem olhar — que é a mesma família do `0,60 contra 0,33` da v0.42: prosa contradizendo a tabela do próprio documento.*

*O preço não fica na Q2: ele reaparece na Q3, como vida a escrever.*

**O que o M2 compra:** uma barra em vez de cinco, e — o que pesa mais — **a Q3 escreve uma ficha com um contador de corpos, e ela serve para as três Trilhas.** Servo é a mesma ficha com um corpo; Coro também.

### O tempo de mesa não fechava na Q2, e fechou por fora

*Este é o achado da rodada.* O §2 levantou o buraco como *"cinco fichas agindo por rodada custam o mesmo tempo quer cada uma faça 25 de dano ou 5"*. **O M1 e o M2 empatam em rolagem.** Só o M3 cortava, e o M3 morreu.

| quem | rolagens por rodada | por combate |
|---|---|---|
| personagem comum | 1,5 | 5–6 |
| Bastião ou Vanguarda no nv6, dois golpes | 3,0 | 10–12 |
| Coro | 4,5 | 15–18 |
| **Matilha** | **7,5** | **26–30** |

**A Matilha custa 2,5× um personagem de nível 6.** *(Contei 6 atacantes na primeira passada e são 5 — o dono é um dos cinco corpos, pelo próprio §4. O número tinha saído 3,0×.)*

**A saída é de gesto e não de regra: rolar em pool.** Os cinco corpos são idênticos, então os cinco d20 saem juntos e conta-se os acertos; os danos idem. **Três gestos por rodada em vez de sete e meio — corte de 60%**, com média, variância e teto da Rotina idênticos, e o 20 natural continua visível. **Não muda um número; muda como a regra se joga.**

> **E o pool cobra uma coisa, que fica escrita porque é preço:** o alvo se declara **antes** de rolar. Não dá para ver o primeiro corpo derrubar e redirecionar o segundo.

### A forma do dano: soma dos acertos, e a conta escolheu

Duas formas estavam na mesa — *somar o dano dos acertos*, ou *cada acerto incrementar um golpe principal*. **Contra um alvo só as duas são aritmeticamente idênticas**, se a segunda crescer proporcional aos acertos. A diferença inteira é outra:

**Repartir alvo.** Cinco dados a 50%, alvo declarado antes:

| vida do alvo | acertos para derrubar | somando, repartido | um principal |
|---|---|---|---|
| 1/5 da Rotina | 1 | **2,50 mortes/rodada** | 0,97 |
| 2/5 | 2 | 0,81 | 0,81 |
| 3/5 | 3 | 0,50 | 0,50 |
| 5/5 | 5 | 0,03 | 0,03 |

**Contra capanga a soma mata 2,6× mais; contra chefe as duas empatam exatas.** A forma não muda o dano — muda **em quantos alvos ele cabe**.

**E o principal colapsa a Matilha no Servo.** Um pacote grande, um alvo por rodada, é o que o Servo já faz; a diferença entre as duas Trilhas viraria só quantos corpos absorvem golpe. O §5 manda rodar dominância entre as três, e essa seria a primeira a acender.

**O 20 natural fecha.** Em cinco d20, `P(pelo menos um 20) = 22,6%`.

| | ganho médio de crítico |
|---|---|
| somando — cada 20 dobra os dados do próprio corpo | **5% da Rotina** |
| um principal — se um 20 dobrar o pacote inteiro | **23% da Rotina** |

**A forma do principal herda um pico de 23% se ninguém escrever o que o 20 faz.** A soma não precisa de frase nenhuma: é a regra da peça 1 — *"Crítico = 20 natural, e dobra os dados"* — aplicada cinco vezes, sem exceção.

### Uma hipótese que eu levantei, medi e joguei fora

Achei que a **Redução de Dano** separasse as duas formas — cinco pacotes pequenos contra RD deveriam sofrer muito mais que um pacote grande. **Não sofrem.** A única RD do sistema é a Reação de cobrir-se de energia, na peça 11 §6 — *"Redução de Dano de `1,5 × refino` num golpe, por 2 PE"* —, uma por rodada, e ela **nunca passa da cota de um corpo**:

| nível | refino | RD | cota de um corpo |
|---|---|---|---|
| 2 | 1 | 1,5 | 2,6 |
| 10 | 3–5 | 4,5–7,5 | 9,0 |
| 18 | 5–9 | 7,5–13,5 | 16,2 |
| 30 | 8–10 | 12–15 | 25,2 |

Ela bloqueia `1,5 × refino` nas duas formas, idêntico. **Fica escrito porque uma hipótese medida e descartada é mais barata que a mesma hipótese ressuscitando daqui a três versões.**

*E uma correção de método, minha:* a primeira tabela de overkill que rodei dava **0% de desperdício em toda linha** para a forma somada — artefato de eu ter deixado o pacote que sobrava migrar de alvo de graça, o que o pool justamente proíbe. **Modelo generoso com a saída que eu já preferia é a pior espécie de verde.**

## 3.3 A Q3, e por que o princípio não era escolha binária

### O que a pesquisa achou, e o Mizuki tinha chegado sozinho

**Vida fixa não aparece em nenhum dos quatro sistemas levantados:**

| sistema | como a vida sai |
|---|---|
| 5e 2024, Bestial Spirit | `HP 20 (Air) ou 30 (Land/Water) + 5 por nível de magia acima de 2` — **base por tipo, mais escala** |
| **PF2e, companheiro animal** | *"ancestry Hit Points **from its type**, plus `6 + its Constitution modifier` **for each level you have**"*, com *"your companion's level is equal to yours"* |
| PF2e, Summoner | pool compartilhado com o dono |
| 13th Age, mook | um quinto de um monstro do nível |

**E o segundo é a fórmula que a peça 1 já escreve.** Lado a lado:

```
PF2e:       vida do tipo               + (6 + Con dela)                  × nível do dono
peça 1:   (inicial do Caminho + Con)   + (por nível do Caminho + Con)    × (nv − 1)
```

**É a mesma máquina.** Troque *"Caminho"* por *"tipo da invocação"* e o nível dela pelo do dono, e não sobra nada para inventar. *Isso não é economia de esforço: é a lição nº 9 pela porta da frente — uma fórmula, um dono, e o `conferir-atributos.py` já em cima dela.*

### A trava proíbe ritmo, não proíbe valor

Foi a pergunta do Mizuki que abriu isto: *"tem que ter algo que a ficha da invocação mude, senão por que teria Constituição nela?"*

| | nv2 | nv30 | cresce | acerto |
|---|---|---|---|---|
| atributo dela **3** — o teto da criação | 3 | 6 | **+3** | 55% |
| atributo dela **2** | 2 | 5 | **+3** | 50% |
| atributo dela **1** | 1 | 4 | **+3** | 45% |

**Os três crescem `+3`, e é o mesmo `+3` do atributo de um personagem.** *A peça 2 §2 escreve por que: o teto de `3` na criação existe para o atributo investido subir exatamente `+3` na campanha, no passo da maestria.* **Só ritmo diferente deriva**, e é por isso que refino está proibido ali — `+7` a `+9` põe o acerto em 70% a 80% no nível 30 — e um atributo com teto `3` na criação não está.

> **⚠ O teto de criação é `3` e não é escolha: `4` e `5` derivam.** *Medido — um atributo que começa em `4` só cresce `+2` até o teto de `6`, e a taxa dela cai de `60%` para `55%` na campanha; começando em `5` ela cai de `65%` para `55%`.* **Só o `3` fecha em zero**, e é o mesmo motivo pelo qual ele é o teto do personagem.

> **O princípio, e ele parte o que CRESCE do que VALE:**
>
> **O ritmo é do dono.** A maestria dele entra em toda rolagem dela, e é a única coisa que cresce sozinha.
> **O valor é dela.** Os cinco atributos são próprios, com o mesmo orçamento e o mesmo teto que a peça 2 dá a um personagem.
>
> **acerto** = `atributo dela + maestria do dono` · **Defesa** = `10 + Destreza dela + metade da Essência ou da Inteligência do dono`, escolhida na montagem · **Teste de Resistência** = `d20 + atributo dela + maestria do dono`, com **um** treinado.

### O que morreu, e morreu num número do projeto

**Vida compartilhada com o dono** — a saída do Summoner do PF2e, *"you both share a single pool of Hit Points"* — **não cabe aqui**:

| nível | PV do Evocador (Con 3) | Rotina do inimigo | rodadas até cair |
|---|---|---|---|
| 2 | 16 | 13 | **1,2** |
| 10 | 72 | 45 | 1,6 |
| 30 | 212 | 108 | 2,0 |

O Evocador é o Caminho de **menor vida do sistema**, empatado com o Emanador. Sozinho ele já aguenta 1,2 a 2,0 rodadas de foco; com cinco invocações bebendo da mesma barra, ele não fecha a primeira rodada em nível nenhum. **O PF2e pode compartilhar porque lá é classe de vida média e *um* eidolon.**

E o argumento que fecha não é o de vida: **pela peça 6 §4 o produto que a Matilha vende é corpo que absorve golpe.** Fazer esse corpo gastar a vida do dono é vender o produto cobrando nele mesmo.

### A taxa de câmbio, que é o que o orçamento vai gastar

| o ponto compra | efeito | em número |
|---|---|---|
| **+1 no acerto** | 50% → 55% | **+10% de dano saído** |
| **+1 na Defesa** | inimigo 50% → 45% | **+11% de vida efetiva** |
| −1 na Defesa | inimigo 50% → 55% | −9% de vida efetiva |

**Acerto e Defesa se pagam quase em paridade — `10%` contra `11%`.** Isso é propriedade do d20 em 50%, não escolha, e é o que deixa **um orçamento único comprar dos dois lados sem regra de conversão**.

**A Constituição não cabe nessa paridade**, e o tamanho depende da base por nível:

| nível | `h` (meia Rotina) | por nível | +1 de Con vale |
|---|---|---|---|
| 2 | 6,5 | 6,5 | +15% de vida |
| 10 | 22,5 | 2,5 | **+40%** |
| 30 | 54,0 | 1,9 | **+54%** |

De **1,4× a 4,9×** um ponto de Defesa. **Ou ela entra com preço próprio, ou a base por nível é grande o bastante para ela não dominar** — que é a mesma conta que a peça 1 fez no Caminho com *"a média dos dados mais 3 de Constituição ≈ 8"*.

### A forma: orçamento de pontos, com três montagens prontas

*Decisão do Mizuki.* O jogador constrói a invocação em **duas moedas separadas** — o arranjo de atributo da peça 2 e o orçamento de `Traço` e `Comando` desta peça —, **e a peça publica invocações já montadas**, que servem de exemplo e de atalho.

**A fila do `ESTADO-ATUAL` já pedia isso e ninguém tinha lido em voz alta:** ela não chama a peça de *"Invocações"*, chama de ***"Invocações — o sistema de criação"***. A peça estava escrita como máquina de construção desde a v0.36.

> **As três montagens prontas trazem uma dívida conhecida, e ela tem nome.** A peça 8 publica uma ficha de exemplo e **passou sete versões com a Defesa errada e a Trilha faltando** — foi por isso que o `conferir-criacao.py` nasceu na v0.34, para conferir **instância** e não regra. **Três montagens publicadas são três instâncias**, e elas envelhecem toda vez que a máquina mexer num preço. O validador desta peça tem de conferir as três contra o orçamento, não só o orçamento contra si mesmo.
>
> ***Escritas na v0.186, e a checagem entrou junto.*** *A promessa era da v0.53 e ficou 123 versões como aviso que não falhava — de propósito, porque escrever as três era escolha de sabor e não conserto.*

## 3.4 A Q4, e as duas réguas que eu tinha errado antes de a conta valer

### O piso não é o Evocador

*Decisão do Mizuki, e ela reancorou a peça inteira:* **invocação é coisa que qualquer Caminho pode vir a usar, não só o Evocador.** Então o preço tem de caber no piso — e o piso está escrito no comentário do `conferir-orcamento.py`:

> *"O Bastião é o **PISO** do sistema, e é por ele que toda checagem daqui é medida: se cabe nele, cabe em todo mundo."*

**4 PE por nível, não 6.** No **nível 2 o Bastião tem 8 PE e o feitiço custa 3 — dois feitiços no dia inteiro**, e é o nível em que toda ficha nasce.

### E o arredondamento do projeto colapsa metade da escada

A **peça 1 §5.4** é dona da regra, e o texto dela é este: *"Arredonde sempre para o lado que não te favorece. **O que você paga sobe.** O que você ganha desce."* Preço em PE é teto.

| preço | nv2 | nv10 | nv18 | nv30 |
|---|---|---|---|---|
| `0,5 × maior Classe` | **3 PE · 38%** | 6 PE · 15% | 9 PE · 12% | 12 PE · 10% |
| `1 × maior Classe` | **3 PE · 38%** | 9 PE · 22% | 15 PE · 21% | 21 PE · 18% |
| `1,5 ×` | **6 PE · 75%** | 15 PE · 38% | 24 PE · 33% | 33 PE · 28% |
| `2 ×` | **6 PE · 75%** | 18 PE · 45% | 30 PE · 42% | 42 PE · 35% |

> **No nível 2 a régua da maior Classe só tem dois degraus.** `teto(0,5 × Classe 1) = 1 = 1 × Classe 1`. **Meio preço é preço inteiro exatamente no nível em que toda ficha nasce.**

**`1,5 ×` e `2 ×` deixam o Bastião de nível 2 com zero feitiços no dia.** Saem por conta.

### Por que "nada" não cabia

A peça 6 §4 diz que o invocador *"troca dano pessoal por presença de tabuleiro"*. **Mas o teto é de uma Rotina somada, então o dano total não muda.** Não há troca — os corpos são acréscimo:

| nv | PV Bastião | PV Evocador | pool da Matilha | a mais na mesa de quatro |
|---|---|---|---|---|
| 2 | 25 | 16 | 32 | **+40%** |
| 10 | 105 | 72 | 112 | +32% |
| 30 | 305 | 212 | 315 | +30% |

**30% a 40% da vida da mesa inteira**, contra uma Trilha que a **peça 14 §4** orça assim: *"De 6% a 9% da Rotina, e a fração quase não deriva"*. Não é a mesma unidade; a ordem de grandeza responde sozinha.

### O `1 ×` escolhido, e o que ele custa de verdade

| nv | `1 ×` em PE | três lutas | % do dia | feitiços que custa |
|---|---|---|---|---|
| 2 | 1 | 3 | 38% | **1 de 2** |
| 10 | 3 | 9 | 22% | **1 de 4** |
| 18 | 5 | 15 | 21% | **1 de 4** |
| 30 | 7 | 21 | 18% | **1 de 5** |

**A fração encolhe de 38% para 18%, mas em feitiços ele cobra exatamente um em todo nível, do 2 ao 30.** *A coisa concreta que você perde não evapora.* E o formato já é aceito na casa: a Expansão incompleta é 22% da lista no nv10 e 8% no nv30, e está escrita como fechada.

E onde ele cai, ao lado do que já existe (% do dia do Bastião):

| | nv10 | nv30 |
|---|---|---|
| **invocar `1 ×`, três lutas** | **22%** | **18%** |
| um feitiço do topo, `3 ×` | 22% | 18% |
| Técnica Máxima, `5 ×`, uma vez | 38% | 29% |
| abrir Expansão, `6 ×`, uma vez | 45% | 35% |

*Esta linha era duas até a v0.174, quando a completa desceu de `8 ×` para `6 ×` e as duas passaram a abrir pelo mesmo PE.* **A completa custava `60%` e `47%` naquela tabela, e o retorno de mesa foi que ela estava cara demais.**

**Invocar três vezes no dia custa o mesmo que um feitiço do topo, e metade de abrir a Expansão uma vez.**

### A ação sozinha não segurava, e a conta confirma o argumento do Mizuki

*"Se o jogador se organizar é capaz dele nem gastar energia."*

| invocar gasta | perde da Rotina da luta |
|---|---|
| ação padrão, dentro da luta | 5,7% |
| qualquer uma, **antes** da luta | **0%** |

**Ação sozinha é preço que o jogador escolhe não pagar.** O PE carrega o peso; a ação governa o *quando*.

### Comandar custa a ação padrão, e o ganho não é o óbvio

| por rodada, Matilha de cinco corpos | ação da invocação livre | comandar custa a padrão |
|---|---|---|
| ataques que saem | 5 | 5 |
| movimentos que saem | 5 | 5 |
| dano total | 1 Rotina | 1 Rotina |
| ações do dono que sobram | 3 | **2** |

**Os dois põem a mesma coisa no campo.** Então isto **não** é o conserto do `conjure animals` de 2014 — *o que quebrava lá não era a ação do conjurador, era oito corpos sem teto de dano*, e esse teto já existe aqui.

**O ganho é outro:**

| | ação livre | comandar custa a padrão |
|---|---|---|
| dono entrega | 1/5 da Rotina | **0 — ele comandou** |
| invocações entregam | 4/5 | **1 Rotina inteira** |
| soma | 1 Rotina | 1 Rotina |
| **o que segura o teto** | uma frase da peça 6 | **a economia de ação** |

> **O teto deixa de ser divisão escrita e passa a cair da economia de ação sozinho.** Uma regra que cai da economia não precisa de ninguém policiando — **é o filtro multi-mestre passando de graça**, e é o oposto de tudo que precisou de validador aqui.

**E o Coro vira a exceção, com as palavras da peça 5 §4 — *"exceção estreita e paga na economia de ação"*:**

| Trilha | na peça 6 §2 | aqui |
|---|---|---|
| Servo | uma invocação, forte | comanda, não ataca |
| Matilha | muitas invocações fracas | comanda, não ataca |
| **Coro** | *"o seu golpe e o delas se encadeiam"* | **ataca e comanda** |

*As três passam a diferir na economia de ação, que é o eixo em que o §2 já as descrevia como diferentes — e a §3.1 já tinha pago pela exceção do Coro em 2024, quando escreveu que ela "não custa nada a mais".*

### A "primeira grátis" foi testada e reprovou

*O Mizuki levantou e pediu a validação: "precisamos validar o quanto isso vai ser benéfico/maléfico para o sistema."*

| como o mestre joga | dano na invocação por luta | reinvocações no dia | preço efetivo |
|---|---|---|---|
| espalha entre os cinco alvos | 0,70 Rotina | 0,8 | 84% |
| ela puxa o dobro | 1,17 | 1,4 | 140% |
| foca metade do tempo | 1,75 | 2,1 | 210% |
| foca nela | 3,50 | **4,2** | **420%** |

**O mesmo personagem, a mesma ficha, o mesmo dia: o preço varia cinco vezes conforme quem está mestrando.** *Um preço que só é cobrado quando o mestre decide cobrá-lo não é preço — é imposto variável.*

> **E uma correção do meio do caminho, porque a primeira leitura estava errada.** Eu escrevi que *"o mestre que foca está jogando certo"*. A conta de troca diz que não: derrubar o pool custa **2,5 Rotinas de dano** ao inimigo e nega **1 rodada** ao jogador — troca de `2,5 : 1` contra ele, e o dano que foi na invocação é dano que não foi num PJ, **que é literalmente o produto que a peça 6 §4 diz que o invocador compra**. O defeito de multi-mestre não é *"o mestre esperto cobra mais"*, é ***"o mestre inexperiente cobra mais, e ele não sabe"***. Continua sendo defeito — só não é o que eu tinha descrito.

**As duas saídas alternativas também morreram, e cada uma por um número:**

| saída | por que morreu |
|---|---|
| **teto de reinvocações por descanso** | contra o mestre que foca, o jogador passa **10,2 das 10,5 rodadas do dia sem o Caminho dele**. Troca imposto variável por desligamento, e desligar o Caminho de alguém por dois terços do dia é pior que cobrar caro |
| **"a primeira de cada luta não custa ação"** | devolve uma ação padrão por luta = **três Rotinas por dia**, e cobra o equivalente a **uma**. É desconto maior que o preço |

**E a metade que sobrevive não precisa de regra nenhuma.** A cena que o Mizuki citou — *"muitas vezes o próprio Megumi tinha o lobo em uso fora de combate"* — acontece sozinha: **fora de combate a ação não custa nada**, então quem invoca antes da luta paga o PE e entra em campo com a invocação de pé. Quem é pego sem ela paga o PE **e** a ação padrão da primeira rodada. *A assimetria que a ideia queria já estava lá.*

> **Duas atribuições erradas, achadas na revisão cética desta rodada e consertadas aqui.** Eu tinha citado a regra de arredondamento como sendo *texto* da peça 1 quando a frase que eu copiei é a do bloco de fórmulas do `ESTADO-ATUAL` — **a peça 1 §5.4 é a dona da regra, mas com outras palavras** —, e tinha atribuído o *"6% a 9% da Rotina"* ao `ESTADO-ATUAL` quando ele mora na **peça 14 §4**. *É a família daquela §9 da peça 5 que a v0.50 pegou e que nunca existiu: não é número errado, é ponteiro para o lugar errado — e ninguém que fosse conferir acharia.* **Escrito assim de propósito, sem a forma literal do ponteiro**, para não plantar no arquivo o mesmo fantasma que a v0.50 gastou uma versão arrancando.

### Os quatro tipos, e o buraco que eles fecham

*Levantados pelo Mizuki, do material:* **técnica · talismã · corpo amaldiçoado · maldição domada.** A Q3 fechou a fórmula de vida como `base do tipo + (por nível do tipo + Con dela) × nível do dono` **e deixou "tipo" sem lista.** Os quatro são essa lista, e eles são o que justifica a fórmula ter um termo de tipo em vez de um número só.

*E há um caso que o material impõe e a regra ainda não tem:* **Rika e Mahoraga agem fora do controle do portador.** Toda esta seção supõe que a invocação obedece; as duas são a exceção escrita na obra, e ela precisa de tratamento antes de a peça fechar.

> **⚠ Achado aberto na v0.178, e ele é do Mizuki lendo o livro: não existe teto escrito de quantas invocações cabem no campo.** *Nem aqui, nem no capítulo 16, nem em documento nenhum do projeto.* **O que segura hoje são duas coisas, e nenhuma delas é um número:** comandar custa a Ação Padrão, então você só comanda uma por rodada; e a cota da peça 6 §4 divide a saída por corpo, então cada corpo a mais encolhe todos os outros. *Quem entrega corpo é a Trilha — `Servo` um, `Matilha` cinco, `Coro` um —, e nenhuma delas entrega uma segunda.*
>
> ***Decisão do Mizuki na v0.178: fica registrado e não vira regra agora.*** **A pergunta que ele faz é a certa e ela precisa de conta antes de resposta:** *se um dia alguma coisa conceder uma invocação além da Trilha, o teto passa a fazer falta — e aí ele é preço, não texto.*

## 3.5 A Q5, que encolheu sozinha e sobrou com um problema de verdade

### O dilema do rascunho dissolveu, e o registro fica porque o motivo é útil

Esta pergunta foi escrita assim: *"se o dono recupera a Rotina inteira ao perder a invocação, matar a invocação **fortalece** o invocador [...] se não recupera, o Evocador vira o Caminho que pode ser desligado por um acerto de sorte. **Nenhuma das duas pontas serve.**"*

**Com o comando custando a ação padrão (Q4), as duas pontas somem:**

| situação | o dono faz | Rotina entregue |
|---|---|---|
| invocação de pé, luta em grupo | comanda: cinco corpos batem | **1** |
| invocação de pé, luta de chefe | ataca ele mesmo | **1** |
| **invocação caiu** | ataca ele mesmo | **1** |
| invocação caiu, ele reinvoca | invoca: não comanda | 0 nessa rodada |

**A Rotina é a mesma nas três primeiras.** Perder a invocação não tira dano do dono — ele volta a bater sozinho — **e também não devolve nada, porque ele nunca teve uma fração.** *Uma pergunta que parecia exigir escolha entre duas pontas ruins virou consequência de uma decisão tomada duas perguntas antes. Vale registrar: nem toda pendência precisa de decisão; algumas precisam de outra pendência fechar primeiro.*

O que se perde é **só presença** — os corpos, as posições, e a vida que absorvia golpe. E o custo de voltar já tem número: `1 × maior Classe` de PE **mais uma rodada sem comandar**, que vale 1 Rotina ou 28,6% da luta.

### O problema que sobrou era a área, e ele apagava a Matilha inteira

Com a vida em pool (Q2) e `h` em meia Rotina (Q3), **um efeito de área que causasse meia Rotina em cada corpo levava `5 × 0,5 = 2,5` Rotinas ao pool — que é o pool inteiro.** Um feitiço de rotina apagava a Matilha.

**O diagnóstico é preciso e não é uma exceção do sistema:** área já vale 4× contra quatro PJs agrupados; a Matilha é alvo agrupado, então vale 5×. **A diferença é que os corpos dela morrem para o que apenas machuca um PJ** — um PJ tem ~2 Rotinas de vida, um corpo tem meia.

> **A saída, decidida pelo Mizuki: a área causa o dano UMA VEZ no pool, e a invocação é vulnerável a ela.**

| como a área entra | no pool | % do pool | corpos que caem |
|---|---|---|---|
| por corpo — como era | 2,50 R | **200%** | **5,0 — apaga** |
| ×3 | 1,50 R | 120% | 5,0 — apaga |
| ×2 | 1,00 R | 80% | 4,0 |
| **×1,5 — vulnerável** | **0,75 R** | **60%** | **3,0** |
| uma vez, sem bônus | 0,50 R | 40% | 2,0 |

**O `×1,5` tira `3,0` dos cinco corpos com um feitiço de área de rotina.** Continua sendo a jogada certa contra a Matilha — contra golpe único o mesmo feitiço tiraria dois corpos, então a área vale metade a mais. ***Escolha do Mizuki na v0.178:*** *"que tal mudar a questão da Matilha ter vulnerabilidade e passar a ser um aumento de 50% em vez de 100%?"*

> **⚠ Eram `2,0` corpos até a v0.178, e o número subiu porque o pool desceu.** *A vida do corpo forte foi de `5 ×` para `2,5 ×` a fórmula, para tirar a Constituição de dentro do multiplicador, e o pool caiu de `2,50` para `1,25` Rotina junto.* **O `×1,5` é o escolhido, e ele foi remedido contra os três degraus com o pool novo**, mas a margem encolheu: o `×3` agora apaga a Matilha inteira, e antes ele deixava dois corpos de pé. *O `2,5 ×` chegou a ser recusado numa rodada anterior desta mesma versão, quando a vulnerabilidade ainda era `×2` e ele derrubava `4,0` dos cinco; **baixar a vulnerabilidade para `×1,5` na mesma leva devolveu a margem**, e o par acabou melhor que o `3 ×` com `×2` nas duas colunas.*

**Contra-teste — a área grande ainda resolve?**

| área por alvo | ×1,5 no pool | corpos que caem |
|---|---|---|
| 0,50 Rotina | 0,75 R | 3,0 |
| 0,75 | 1,12 | 4,5 |
| **0,83** | **1,25** | **5,0 — apaga** |

**Apagar a Matilha passa a exigir `0,83` Rotina de área por alvo** — um feitiço e dois terços de rotina, ou um feitiço grande de verdade. *A jogada continua existindo; ela custa caro. É o que separa contra-jogo de contra-jogo automático.*

### A morte em definitivo, e ela dispara onde a ficção dispara

*Decisão do Mizuki, e o argumento é canon:* na obra, shikigami destruído **não volta**.

> **Some no zero, sem estado intermediário.** Nada de `Inconsciente`, Sequela ou Cicatriz — a máquina da peça 1 §5.5 é de personagem, e a Q2 gastou a passagem inteira comprando que a invocação **não** fosse um.
> **A régua da morte é `5 ×` a vida que a fórmula do tipo dá**, e ela vale igual para qualquer corpo, seja ele um, cinco ou o do `Servo`.
> **Ela morre de vez se o excedente passar de metade da régua, ou se um único golpe causar a régua inteira.** O talismã se desfaz, o corpo se perde, a invocação de técnica ou a maldição domada é exorcizada.

| de onde vem o golpe | dano | passa de metade em negativo? | causa a régua inteira? |
|---|---|---|---|
| golpe único de inimigo (~meia Rotina) | 0,50 R | não | não |
| dois golpes na mesma rodada | 1,00 R | não | não |
| área de rotina, com ×1,5 | 0,75 R | não | não |
| **área grande, com ×1,5** | 1,88 R | **sim** | não |
| **Expansão de Domínio, acerto garantido** | 3,00 R | **sim** | **sim** |

**Nenhum golpe de rotina mata em definitivo.** Precisa de área grande ou de Expansão — *que são exatamente as coisas que na obra destroem shikigami de vez.* **A régua dispara onde a ficção dispara, e ninguém escreveu isso à mão: caiu dos dois números.**

> **⚠ A régua era a vida máxima DAQUELE corpo até a v0.178, e por isso ela encolhia junto com o corpo.** *Quando ela entrou, o `Servo` e a `Matilha` não sentiram: a vida máxima deles era exatamente `5 ×` a fórmula, que é a escala em que esta tabela sempre foi medida. **Na mesma versão o corpo forte desceu para `2,5 ×`, e aí a régua deixou de ser a vida máxima de alguém** — ela virou uma escala fixa, que é o que ela precisava ser desde sempre.* **Quem estava quebrado era o `Coro`:** o corpo dele vale `h`, então a régua dele valia `0,50 R` — e o golpe único de inimigo, que vale `0,50 R`, causava a vida máxima inteira. *As três primeiras linhas desta tabela matavam o corpo do `Coro` em definitivo, e a frase logo acima era verdadeira para `2,50 R` e falsa para `0,50 R`.*
>
> **É o achado da v0.63 de novo, na Trilha que ficou de fora dele.** *Lá o argumento foi escrito assim: "com `h` a vida máxima do `Servo` era um quinto da da `Matilha`, para a mesma Rotina entregue — pela regra de morte do §3.5 o `Servo` sai da luta por um golpe."* **O conserto de lá foi subir o corpo, e o de cá foi tirar a régua do corpo**, porque o `h` do `Coro` é a troca dele — ele é o único que ataca e comanda — e subir a vida apagaria a troca junto.
>
> **A conta de quanto isso pesava: `Con 1` já escapava em todo nível**, então o buraco caía inteiro na ficha de Constituição `0` — que é justamente o Evocador que põe corpo na frente em vez de aguentar golpe. *Achado do Mizuki lendo o livro, e a medida saiu pior que o palpite dele: não era vida baixa, era perda permanente da Trilha no primeiro acerto.*

### Reconseguir, fechado na v0.57 — e a resposta é que quase sempre não dá

*Decisão do Mizuki, e ela é mais dura do que o rascunho supunha.*

> **Se ela morreu em definitivo, acabou. Não se reconsegue.**
> **Se ela só chegou a zero** — sem excedente acima de metade da régua e sem um golpe que causasse a régua inteira —, **ela volta normalmente pelo preço da Q4, mas com metade da vida máxima.**

**A meia vida é o que faz a segunda invocação da luta doer sem desligar o Caminho de ninguém**, e ela cai numa conta que a Q5 já tinha rodado: o corpo vale **meia Rotina**, então o corpo que volta vale **um quarto**. Contra o pool da Matilha, reinvocar depois de cair devolve `1,25 → 0,62` Rotina de presença.

*E ela é a peça que faltava no argumento da Q4.* A conta da "primeira grátis" mostrou que o mestre que foca a invocação cobra **420%** do preço nominal, e o conserto foi não ter isenção. **A meia vida cobra o mestre que foca de novo, na direção certa:** ele derruba, o jogador reinvoca por PE e ação, e o corpo que volta cai na metade do tempo. *O preço agora é cobrado no recurso e na durabilidade, e não só no recurso.*

> ~~**Quando a vida cheia volta continua sem dono declarado.**~~ ***FECHADO na v0.163: ela volta no DESCANSO LONGO***, e a decisão não era de sabor — ela já estava tomada em outro lugar.

**A peça 10 §3 decidiu que o descanso curto NÃO devolve vida**, com o motivo escrito: *em Jujutsu Kaisen quem conserta gente é a Energia Reversa e a Shoko, e se um respiro devolvesse vida a cura deixava de ser assunto.* **A meia vida da invocação é vida.**

> **Pôr ela no respiro criaria uma segunda escada de recuperação de vida, para um tipo de corpo só** — *e o filtro multi-mestre reprova isso antes de qualquer conta: dois mestres passariam a carregar duas escadas na cabeça, uma para gente e outra para invocação.*
>
> **E o custo continua caindo onde a Q5 mediu.** *A meia vida foi desenhada como custo de **luta**, não de campanha.* **Com o descanso longo ele atravessa a missão inteira — que é o degrau em que *"a missão acaba"* já significa alguma coisa — e não vira penalidade permanente**, que era a terceira saída e a que este mesmo §3.5 já tinha recusado por medir o tipo de custo errado.

### O dono cai, e a invocação não vai junto

*Fechado na v0.163.* **A pergunta não estava escrita em lugar nenhum** — *nem aqui, nem no capítulo 60 do livro, nem na seção `Em aberto` dele* —, então nem a contagem de marcas do `conferir-voz.py` a enxergava.

**O dono chega a 0 de vida e escolhe uma das duas da peça 1 §5.5, e as duas caem diferente:**

| ele escolhe | a invocação |
|---|---|
| **`Insistir`** — fica de pé e age normalmente | **nada muda.** Ele tem Ação Padrão, então comanda como sempre |
| **`Aguentar`** — apaga, janela de `3` rodadas | **fica no tabuleiro, e não pode ser comandada** |

> **A invocação parada continua sendo um corpo.** *O `Traço` é o que ela **é**, e ele não depende de ninguém gastar ação: ela continua voando, continua ocupando o corredor, continua podendo ser atacada, com a vida que tinha.* **O que para é o `Comando` — o que ela **faz** —, e ele custa a Ação Padrão do dono, que um inconsciente não tem.**
>
> ***E isso entrega de graça uma coisa que já estava escrita em outra peça:*** *a peça 19 §5 lista **`uma criatura no caminho`** como exemplo de cobertura `Parcial`.* **Uma invocação de pé em cima do dono caído dá a ele `+2` de Defesa e `+2` no Teste de Resistência Físico pelas três rodadas da janela** — *sem uma linha de regra nova.* **E o inimigo ganha uma decisão de verdade: gastar ação matando o corpo, ou passar por ele e ir no dono.**

***A terceira saída — a invocação AGIR sozinha enquanto o dono está apagado — foi recusada pela conta, e não por gosto.***

**A trava da peça 6 §4 é `você e todas as suas invocações somados entregam uma Rotina`, e ela nunca precisou ser policiada:** *ela se sustenta sozinha porque o `Comando` come a Ação Padrão, o que torna o dono e a invocação **mutuamente exclusivos** na rodada.* **Está escrito no §3.4 desta peça:** *"o teto da peça 6 §4 deixou de precisar de policiamento"*.

> **Dono inconsciente não tem Ação Padrão para gastar.** *Uma invocação que agisse nessas três rodadas estaria agindo **de graça** — e a §1 desta peça já mediu esse caso exato:* **invocação que age sozinha DOBRA o dano por rodada.**
>
> **Então a exclusão mútua não é consequência da regra: é a regra.** *Se ela vale com o dono de pé, ela vale mais ainda quando ele não está* — **é o único momento da luta em que pôr a invocação para agir não custaria nada a ninguém.**

## 3.6 Os números da Q3 — `Traço`, `Comando`, e o orçamento

### As duas camadas, e o nome que a triagem deixou passar

*Levantado pelo Mizuki:* **uma invocação tem uma camada que diz o que ela é e outra que diz o que ela faz.** A primeira é voar, carregar, soltar o raio; a segunda é o ataque e a ação no turno — *"como numa ficha, mas muito mais fraco"*.

**`Passiva` estava ocupado**, e mais quatro caíram com ele na triagem:

| | |
|---|---|
| **OCUPADO** | `Passiva` (peça do Fundamento) · `Natureza` (já é perícia) · `Forma` (é Feitiço pronto **e** peça do Fundamento) · `Molde` (Tema) · `Instinto` (Passiva **e** Tema) |
| **LIVRE** | `Traço` · `Comando` · `Índole` · `Feitio` · `Dom` · `Sina` · `Manobra` · `Investida` · `Ato` |

> **`Traço` é o que ela é. `Comando` é o que ela faz.**

*E `Comando` é a mesma palavra da regra da Q4 — o dono gasta a ação padrão para **comandar**. O nome e a mecânica são a mesma coisa, o que é o oposto do problema que a lição nº 6 descreve.*

### A ficha dela, e o que ela tem igual ao personagem

*Frase do Mizuki que ancorou o desenho:* **"invocações raramente passam de força de seus portadores"**. *Ela não virou número — virou o lugar de onde os números saem: a invocação usa o orçamento de atributo do personagem, sem nada por cima.*

| a ficha dela | igual ao personagem? | dono do número |
|---|---|---|
| **9 pontos na criação**, teto `3` | **sim**, palavra por palavra | peça 2 §2 |
| **`+1` por marco**, teto `6` | **sim** | peça 2 §3 |
| **cinco atributos** | **sim** | peça 1 §4 |
| **um Teste de Resistência treinado** | não — o personagem treina **dois** | peça 8 |
| **deslocamento `9` metros, fixo** | é o base de qualquer ficha | peça 3 §2 |

**São seis arranjos legais na criação, exatamente os mesmos seis do personagem** — de `3·3·3·0·0` a `2·2·2·2·1`. *Com três atributos em vez de cinco o número cairia para **um**, `3·3·3`, e o arranjo deixaria de ser escolha; foi essa conta que trouxe Inteligência e Essência para a ficha dela.*

> **As duas que faltavam ganharam função com o Teste de Resistência próprio.** *Enquanto o TR era o número do dono, Inteligência e Essência não tinham onde entrar — e por isso a peça só usava três atributos.* **A peça 1 §4 escreve `TR = d20 + atributo do TR + maestria`**, então as cinco entram pela mesma porta.

**E o orçamento desta peça compra só capacidade.** Ele não encosta em acerto, Defesa nem vida — esses três já têm dono, e é o arranjo de atributo da peça 2. *Não existe operação que troque um pelo outro, e é isso que mantém as duas moedas separadas.*

### A amarra são 18 metros, e o número não é novo

*Buraco achado varrendo o arquivo, e ele estava aberto desde a v0.50: **não existia regra de distância entre o dono e a invocação em lugar nenhum.*** A única menção no rascunho inteiro era a nota do PF2e — *"o eidolon tem que ficar a até 30 m do dono"* —, e ela está marcada como *"vale como confirmação de que o formato é o certo, não como coisa a importar"*.

Com a Q4 fazendo **comandar custar a ação padrão**, *"de quão longe dá para comandar?"* passou a ser pergunta de mesa em toda rodada, sem resposta escrita. É exatamente o formato que o filtro multi-mestre reprova.

> **A invocação tem de ficar a até 18 metros do dono.** Além disso ela **não pode ser comandada**: fica onde está, sem agir, até voltar ao alcance.

**O 18 já tem dono e não é este documento:** é o **alcance base de Projétil**, do manual, e a peça 3 §3 usa ele como âncora ao explicar o deslocamento base — *"o alcance base de Projétil é 18 m, então um turno de movimento fecha metade da distância de um duelo"*. **Zero parâmetro novo**, e a conta que sai dele é legível na mesa: a invocação anda até **dois turnos de movimento** à frente do dono.

*Os 9 m foram medidos e reprovados:* com o deslocamento base como amarra, a invocação vive colada no dono, a Matilha de cinco corpos não abre leque nenhum, e o `Traço` de alcance vira compra obrigatória — que é o defeito que a régua de Equipamento chama de **propriedade morta**, uma vaga que toda montagem gasta do mesmo jeito.

**E o que acontece fora da amarra é escolha de desenho, não descuido.** Ela não some. Se sumisse, o inimigo que a empurrasse para além dos 18 m estaria **apagando o preço de invocar de graça** — `1 × maior Classe` de PE e uma ação padrão, com um empurrão. Ficar parada custa a rodada e devolve o corpo; sumir custaria o recurso inteiro.

### As três faixas, e por que nenhuma delas é um metro novo

*Decisão do Mizuki na v0.55, e ela resolve um problema que só apareceu quando o `Remoto` precisou de número:* **o projeto não tem nenhuma distância acima de 30 m escrita em lugar nenhum.** A escala inteira é `1,5 · 3 · 6 · 9 · 18 · 21 · 30`. Quarteirão e país estão os dois fora da escala de combate, e **medir em metro uma coisa que ninguém vai medir é precisão falsa.**

| faixa | o que é | quem alcança |
|---|---|---|
| **no combate** | os **18 m** da amarra | toda invocação |
| **na cena** | *(um quarteirão, na ordem de 100 m)* | o `Traço` **`Remoto`** |
| **fora da cena** | *(um país)* | o `Remoto`, **com gate** |

**A metragem entre parênteses é referência e não regra** — quem decide onde a cena acaba é o mestre, que já decide isso o tempo todo. *É o mesmo formato que a peça 10 usou para não ter relógio de horas: "gatilho de ficção — a luta acabou, a missão acabou — dois mestres arbitram igual".*

> **E o gate do país é o primeiro de todo o catálogo.** *Decisão do Mizuki:* alcance de país exige **Restrição Celestial pelo ramo do corpo limitado** e uma **técnica voltada a isso** — que é o Ultimate Mechamaru inteiro, sem regra especial nenhuma. **Nenhum outro `Traço` ou `Comando` tem requisito**, e é por isso que ele precisou de formato: a peça 11 §5 manda **cada aptidão declarar o gate dela**, e até a v0.57 os formatos permitidos lá eram três — *nenhum, só nível, só refino, ou os dois*. **O de Origem é um quarto formato, e ele foi escrito na peça 11 §5 na v0.58**, que é o documento dono dos formatos de gate. Esta peça aponta para lá em vez de repetir a definição.

> **E o quarto formato nasceu com trava.** A checagem 26 do `conferir-invocacoes.py` confere que **nenhuma outra entrada do catálogo tem requisito**. Se uma segunda aparecer, quer dizer que a régua de degrau do §3.7 parou de precificar sozinha — e isso tem de ser decisão e não descuido.

### O orçamento cresce, e crescer não deriva

*Decisão do Mizuki, contra a primeira leitura da conta — e a conta estava certa e incompleta.* Eu tinha registrado que *"o orçamento pode ser plano"*. **Ele pode; ele não precisa ser.** O que a trava proíbe é **magnitude em disputa**, e o que o orçamento compra é **largura**: três `Traço` não inflam o acerto, e o teto de uma Rotina já segura a saída. **É a mesma porta que a peça 11 §2 abre para o refino** — *escopo e frequência são eixos permitidos*.

E a cadência já existe: **os sete marcos**, que governam atributo, refino e feitiço.

| nível | marcos | orçamento | o que dá para montar |
|---|---|---|---|
| 2 | 0 | **8** | dois `Traço` baratos, ou um do degrau 2 — o Nue voa |
| 6 | 1 | 12 | três baratos, ou um do degrau 2 mais um barato |
| 10 | 2 | 16 | dois do degrau 2 |
| 18 | 4 | 24 | três |
| 26 | 6 | 32 | quatro |
| 30 | 7 | **36** | quatro e folga |

**Cada marco dá `4` pontos, e a base no nível 2 é `8`.** *O passo é `4` porque a v0.67 quebrou o ponto em quatro — o §6.6 do `RASCUNHO-trilhas.md` tem a conta, e o número mora aqui.*

**De 8 a 36, dois `Traço` baratos no começo e quatro do degrau 2 no fim, com zero escada nova.**

### Quanto vale um ponto, e as duas âncoras não são a mesma moeda

| âncora | 1 ponto vale |
|---|---|
| Equipamento §5 — 1 ponto de arma | `0,33` de dano por rodada |
| esta ficha — 1 ponto de atributo dela | **±10% do que a invocação entrega** |

**Os dois pontos não valem a mesma coisa, e desde a v0.180 eles não têm mais como se encontrar.** *Até ali existia uma razão publicada — `0,5×` no nível 2 e `4,1×` no nível 30 — e ela era medida **através da venda**: descer um ponto de acerto devolvia orçamento, e essa devolução era a ponte entre as duas moedas.* **Com a ficha própria a venda deixou de existir**, e com ela a ponte: o orçamento compra `Traço` e `Comando`, os atributos saem do orçamento da peça 2, e não há operação que troque um pelo outro.

> **Isso é mais forte que a razão que existia, e não mais fraco.** *Uma razão publicada prova que a conversão foi medida; a ausência de operação prova que ela não pode acontecer.* **O que o validador confere hoje é a ausência**: nenhuma taxa escrita, nenhuma entrada do catálogo preçada em moeda de arma, e a peça declarando que as duas não caem no mesmo saco.

**Então a separação não se sustenta mais em "são orçamentos de tamanhos diferentes"** — no pé da campanha o ponto de arma é o maior dos dois. Ela se sustenta em **o que cada um compra**: o de arma compra dado de dano, e o desta ficha é proibido de tocar em dado de dano. **O que não pode acontecer é as duas moedas caírem no mesmo saco**, e o validador guarda isso pelo que se compra, não pelo tamanho.

*E a escada do PF1e serve para calibrar o **formato**, não o valor:* movimento no chão custa 1, **voar custa 2**, sentido bom custa 3 a 4. **É a mesma forma da lista que a peça 5 §4 autoriza.**

### O catálogo sai do material, e sete dos oito entram sem forçar

*Lido em vez de lembrado, e a fonte confirma a regra da Q5 com essas palavras:* ***"Once destroyed, they cannot be summoned again."***

| shikigami | o que faz | na lista da peça 5 §4 | pontos |
|---|---|---|---|
| Cão Divino | caça e devora maldição, rastreia | sentido | 1 |
| **Nue** | voa, carrega uma pessoa, mergulha | posicionamento | **2** |
| Serpente | sai do chão e prende | alvo e posicionamento | 2 |
| Sapo | língua prende à distância | alvo, à distância | 2 |
| Elefante Máximo | jato de água que empurra | área e posicionamento | 2 |
| Coelho de Fuga | muitos corpos que distraem para o dono fugir | corpos e negação | 3 |
| **Cão Divino: Totalidade** | funde os dois num só | — | **0** |
| **Mahoraga** | adapta | fora de escala | **—** |

**Duas coisas caem sozinhas dessa tabela, e as duas são teste de que o resto está certo:**

**O `Cão Divino: Totalidade` custa zero**, porque ele não é capacidade nova — **é o que sobra quando um corpo morre em definitivo**, e a regra da Q5 já o produz. *Uma entrada de catálogo que o catálogo não precisa escrever é a melhor prova de que a regra debaixo está funcionando.*

**O Mahoraga não é capacidade nenhuma.** Ele e a **Rika** são a exceção escrita na obra — os dois agem fora do controle do portador —, e isso é **regra própria, não ponto de orçamento**. Fica marcado aqui e precisa de tratamento antes de a peça fechar.

### A fórmula de vida, com o termo de tipo preenchido

*Fechada na v0.57, e o termo estava vazio desde que a Q3 fechou — uma fórmula com termo vazio parece pronta e não é.*

**O alvo não era livre:** a Q2 fixou um corpo em **meia Rotina**, e a Q5 fixava então o pool da Matilha em `5h` — hoje ele é `2,5h`, e a mudança não move esta derivação, que sai da meia Rotina. Resolvendo os dois pontos ancorados — `h(2) = 6,5` e `h(30) = 54` — sai `por nível ≈ 1,7` e `base ≈ 3,1`. **Arredondando para número de mesa: base 2, por nível 2.**

> **O `h(30)` desta linha era `63` até a v0.60, e o número vinha de a peça 6 §3 estar lendo a coluna errada do manual.** Com a coluna `Rotina` de verdade, o alvo do nível 30 é `54`. **A fórmula não se moveu, e o motivo é a forma do alvo:** a Rotina é **escada por Classe**, não reta, e uma reta ajustada a uma escada passa por baixo no pé de cada degrau e por cima no topo. O `+15%` do nível 30 é o topo do degrau `26–30`, que é o **mais largo da tabela** — e ele é menor que o `+16%` do nível 8 e do nível 12, que esta peça já aceitava calada. *O ajuste sempre foi contra uma escada; o que estava errado era o último degrau dela.*

> **`vida = base do tipo + (2 + a Constituição dela) × nível do dono`**

*Ordem decidida pelo Mizuki:* **talismã e corpo amaldiçoado têm a mesma vida; a maldição domada tem mais, por ter sido domada; a técnica fica no meio** — ela não precisa ser domada, mas quem a perde perde da própria técnica, e não tem substituição.

| tipo | base | nv2 | nv10 | nv18 | nv30 |
|---|---|---|---|---|---|
| **talismã** · **corpo amaldiçoado** | **1** | 5 | 21 | 37 | 61 |
| **técnica** | **2** | 6 | 22 | 38 | 62 |
| **maldição domada** | **3** | 7 | 23 | 39 | 63 |
| *alvo — meia Rotina* | | *6,5* | *22,5* | *38,0* | *54,0* |

**Só a base varia, e o por-nível é igual nos quatro. É a mesma forma que o §3.3 usa no acerto:** base diferente é **linha de partida**, e linha de partida não deriva. Por-nível diferente faria os quatro tipos **derivarem um do outro** ao longo da campanha, que é a coisa que a trava proíbe.

**E o pool da Matilha continua na faixa que a Q4 mediu**, lido na mesma base do §3.4 e não numa base nova:

| nível | talismã e corpo | técnica | maldição domada | *o que o §3.4 registrou* |
|---|---|---|---|---|
| 2 | 31% | **38%** | 44% | *40%* |
| 10 | 30% | **31%** | 33% | *32%* |

**O tipo do meio cai em cima da referência**, e as duas pontas ficam dentro da faixa. *Nenhum tipo quebra a conta do custo.*

> **O preço de não derivar é que o tipo encolhe, e o número está aqui em vez de escondido.** Do mais fraco ao mais forte são **1,40×** no nível 2 — 31% de um corpo inteiro — e **1,03×** no nível 30, que é 3%. **O tipo pesa na criação e vira sabor no fim da campanha.** *Isso é propriedade do formato escolhido e não descuido: a alternativa é por-nível diferente, e ela troca "encolhe" por "deriva".*

### O que a Q3 devia, e o que sobrou

**O catálogo está escrito entrada por entrada no §3.7 — 19 compráveis, mais o `Investir` a 0.** Cresceu de 13 para 19 na passada dos três tipos que faltavam, com a triagem rodada em cada nome novo.

**Com a fórmula de vida preenchida, a Q3 fechou inteira.** *O que a peça ainda deve não é dela: é o validador.*

## 3.7 O catálogo — e ele achou um buraco entre o orçamento e a Trilha

### Os nomes passaram pela triagem, e dois morreram nela

**`Enxame` e `Sombra` saem OCUPADO — os dois são Tema no manual**, e `Enxame` era exatamente o nome óbvio para o Coelho de Fuga. `Toca` sai **DENTRO** de *"Toca a Alma"*, e `Golpe` sai **DENTRO** de *"Feitiço de Toque"*, que é termo do sistema. *Quatro nomes que pareciam livres, e a triagem pegou os quatro antes de qualquer um ser escrito.*

### `Traço` — o que a invocação é. Sempre ligado.

| ponto | `Traço` | o que faz | de onde veio |
|---|---|---|---|
| **5** | `Faro` | rastreia por cheiro e por energia | Cão Divino |
| **2** | `Escalada` | sobe parede e teto sem teste | — |
| **2** | `Nado` | move na água sem penalidade | — |
| **7** | `Miúdo` | ocupa espaço menor e passa por vão | Coelho de Fuga |
| **5** | `Vigia` | o que ela vê e ouve, **você** vê e ouve | Kogane · os shikigami de rato e de pássaro do Dhruv |
| **3** | `Fala` | ela fala, e dá para conversar com ela | Kogane · o Marmalade Boy · o Panda |
| **8** | `Voo` | voa | Nue |
| **8** | `Montaria` | carrega uma pessoa | Nue |
| **8** | `Fisgada` | prende à distância | Sapo |
| **8** | `Emboscada` | surge do chão, fora do alcance de ver | Serpente |
| **8** | `Jorro` | empurra em linha ou em área | Elefante Máximo |
| **8** | `Graúdo` | ocupa espaço maior e **barra passagem** | Elefante Máximo · a peça 6 §4 |
| **8** | `Remoto` | funciona **na cena**, além dos 18 m da amarra — e **fora da cena** com gate | Ultimate Mechamaru |

*A escada é a do PF1e no formato e não no valor: movimento no chão custa 1, **voar custa 2**. E as treze entradas caem todas dentro da lista que a peça 5 §4 autoriza — posicionamento, alvo, duração, recuperação. **Nenhuma toca dado de dano**, e não pode mesmo: o teto de uma Rotina já governa a saída.*

> **O `Graúdo` é o par do `Miúdo`, e o degrau diferente não é tamanho — é quem sofre.** Ocupar espaço está escrito no critério de **1 ponto** (*"que espaço ocupa"*), e é por isso que o `Miúdo` custa 1: ela passa por um vão, e isso não acontece com mais ninguém. **O `Graúdo` barra passagem**, e barrar é o inimigo perdendo movimento — encosta em outra criatura, degrau de 2. *É a mesma linha que separa `Escalada` de `Voo`, medida no outro eixo.*

### `Comando` — o que ela faz quando o dono gasta a ação padrão nela

| ponto | `Comando` | o que faz |
|---|---|---|
| **0** | `Investir` | o ataque. **Toda invocação tem**, e ele entrega a cota da Rotina |
| **4** | `Agarrar` | prende o alvo |
| **4** | `Arrastar` | move o alvo, ou se move levando ele |
| **4** | `Buscar` | pega um objeto, ou rastreia de forma ativa |
| **4** | `Cavar` | abre buraco, desenterra, revira o terreno |
| **8** | `Interpor` | se põe entre o dono e o golpe |
| **8** | `Chamariz` | o alvo tem de vir para cima dela | Coelho de Fuga |

*`Golpe` não pôde ser usado por estar dentro de `Feitiço de Toque`; `Investir` saiu LIVRE. O `Cavar` não é o `Emboscada`: um faz buraco no chão, o outro é ela **saindo** dele, e os dois funcionam sozinhos.*

#### O `Investir` em número, e ele nunca tinha sido multiplicado

***Achado do Mizuki na v0.178, perguntando o que o livro publicava:*** *a linha acima diz "a cota da Rotina" e o capítulo 16 do livro dizia só "o ataque".* **A fração estava decidida desde a v0.51 e o número nunca foi escrito em lugar nenhum** — nem aqui, nem no livro —, então `a minha invocação ataca` não resolvia na mesa. *Não é número novo: ele tem quatro donos e faltava a multiplicação.*

| de onde sai | dono |
|---|---|
| a Classe de cada nível | peça 18 §2 |
| a Rotina, `floor(3,5 × Classe)` dados de `d8` | peça 6 §3, lida do manual |
| a cota — dono e invocações somados entregam **uma** Rotina | peça 6 §4 |
| o arredondamento — o que se ganha desce | peça 1 §5.4 |

| nível | Classe | Rotina | uma invocação: cota | uma invocação: dado | corpo da `Matilha`: cota | corpo da `Matilha`: dado |
|---|---|---|---|---|---|---|
| 2–4 | 1 | 13 | 6 | `1d6` | 2 | `2` |
| 5–8 | 2 | 31 | 15 | `4d6` | 6 | `1d6` |
| 9–12 | 3 | 45 | 22 | `6d6` | 9 | `2d6` |
| 13–16 | 4 | 63 | 31 | `8d6` | 12 | `3d6` |
| 17–20 | 5 | 76 | 38 | `10d6` | 15 | `4d6` |
| 21–25 | 6 | 94 | 47 | `13d6` | 18 | `5d6` |
| 26–30 | 7 | **108** | 54 | **`15d6`** | 21 | **`6d6`** |

**A reconstrução foi conferida contra os quatro pontos que a peça 6 §3 publica** — `13`, `45`, `76` e `108` — e bate nos quatro. *`Uma invocação` cobre o `Servo` e o `Coro`; o `Coro` divide igual porque o que ele compra é economia de ação e não saída.*

> **O dado é `d6` e ele arredonda para BAIXO, e as duas metades dessa frase foram pagas.** ***Pedido do Mizuki:*** *"sobre os danos, não usa fixo, tenta usar dados também."* **Arredondar para o mais perto fura o teto de uma Rotina em três das sete faixas** — a `Matilha` chegava a `135%` no nível 2 —, *e o teto da peça 6 §4 é justamente o que não tem conserto por preço.* **Para baixo nada estoura**, e o preço é `1,9` de dano por rodada a menos numa invocação e `1,4` num corpo da `Matilha`, na média das sete faixas.

> **O corpo da `Matilha` não rola dado nos níveis `2` a `4`, e o motivo é aritmético:** *a cota dele ali é `2` de dano, e `2` é menor que a média de qualquer dado — o `d6` dá `3,5`, o `d4` dá `2,5`, e só o `d3` caberia.* **Abaixo do nível 5 ele causa `2` fixo**, e do 5 em diante rola. *O `d3` foi medido e recusado: ele cabe em tudo e erra menos, e não é dado de verdade — rola-se um `d6` e divide.*

> **⚠ Nos níveis `2` a `4` a `Matilha` entrega `77%` da Rotina e o `Servo` entrega `92%`, e isso fica.** *Um quinto de `13` é `2,6` e desce para `2`; cinco corpos somam `10`.* ***Decisão do Mizuki: aceitar e declarar*** — **o arredondamento é a regra da peça 1 e ela vale igual para todo mundo, e a `Matilha` compensa em corpos na faixa em que perde em dano.** *O vão fecha no nível 5 e não volta: da Classe 2 em diante as duas ficam entre `95%` e `100%`.* **Arredondar para cima ali estouraria o teto de uma Rotina em `115%`**, e a peça 6 §4 diz que esse teto não tem conserto por preço.

> **O `Chamariz` é a única entrada que existe porque um shikigami do material não fechava sem ela.** A peça 6 §4 descreve o produto do invocador como *"corpos que absorvem ataque, flanqueiam e bloqueiam caminho"* — e o Coelho de Fuga é *"muitos corpos que **distraem** para o dono fugir"*. Absorver e bloquear já tinham entrada; **distrair não tinha nenhuma.** Ele é **negar a ação de outro**, que é o degrau de 2 escrito.
>
> *E ele não pôde se chamar `Provocar`: o nome sai LIVRE na triagem e **colide em sentido** — `Provocar` é perícia de Essência (peça 7), e um `Comando` com o nome de uma perícia faz a mesa procurar uma rolagem que não existe. É o tipo de colisão que o `conferir-nomes.py` não pega.*

### Criar o seu — e a régua já estava implícita nas quatorze entradas

*Pedido do Mizuki: o jogador tem de poder criar `Traço` e `Comando`, com o catálogo servindo de base.* **O projeto já tem a regra para esse caso exato, escrita na peça 12:**

> *"'O mestre decide o que é um feito' **não atravessa sete mesas**. A lista precisa ser fechada, no molde do ambiente propício: **entradas escritas, e a palavra final do mestre em cima delas — nunca do zero.**"*

**Então o catálogo não é a lista do que existe: é a régua contra a qual o que não existe é medido.** E a régua sai das próprias entradas, sem precisar inventar critério novo:

| pontos | `Traço` — o que separa um degrau do outro |
|---|---|
| **2** | **como ela anda, e só ela.** `Escalada`, `Nado` |
| **3** | **o que ela comunica.** `Fala` |
| **5** | **o que ela percebe — e o `Vigia` chega em você.** `Faro`, `Vigia` |
| **7** | **que espaço ocupa, a um passo de mexer no tabuleiro.** `Miúdo` |
| **8** | **encosta em outra criatura ou no tabuleiro:** carrega, prende, empurra, barra, alcança além do alcance, aparece onde não dava. `Voo`, `Montaria`, `Fisgada`, `Emboscada`, `Jorro`, `Graúdo`, `Remoto` |

| pontos | `Comando` — o que separa um degrau do outro |
|---|---|
| **0** | **o ataque.** `Investir`, que toda invocação tem |
| **4** | **faz uma coisa com um alvo ou um objeto.** `Agarrar`, `Arrastar`, `Buscar`, `Cavar` |
| **8** | **protege o dono, ou nega a ação de outro.** `Interpor`, `Chamariz` |

*O `Voo` é o caso que mostra que a régua funciona: andar é 1 ponto, e voar é 2 — não porque voar seja "melhor", mas porque ele deixa de ser uma coisa que a invocação faz consigo mesma e passa a ser uma que ignora o tabuleiro inteiro. **É a mesma linha que separa `Escalada` de `Voo` no PF1e**, por outro caminho.*

### E três coisas que a criação não pode comprar a preço nenhum

**Elas não são caras — são ilegais**, e cada uma tem um dono que já disse por quê:

| não pode | por quê | dono |
|---|---|---|
| **dado de dano** | o teto de uma Rotina já governa a saída. Um `Traço` que dá `+1d6` não custa 3 pontos: ele não existe | peça 6 §4 |
| **qualquer coisa que cresça com refino** | refino cresce `+7` a `+9` contra `+3`, e isso é 70% de acerto no nível 30 | peça 11 §2 |
| **atributo** | os cinco já saem do arranjo dela, e comprar de novo é pagar duas vezes | §3.6 |

### Os outros três tipos, e o que eles pediram de verdade

*As catorze entradas da primeira passada saíram todas dos shikigami do Megumi, que é o tipo **técnica**. Faltava perguntar o que os outros três pedem — e a resposta foi bem menor do que o tamanho da pergunta.*

**A maldição domada não pede entrada nenhuma, e isso não é falha de levantamento.** O texto da fonte é *"the user can also extract the curse techniques of semi-grade 1 and above cursed spirits they absorb"* — a maldição domada **carrega a técnica dela**. Só que aqui isso se parte em dois, e os dois já têm dono:

| a técnica dela | onde ela cai |
|---|---|
| causa dano | **ilegal.** O teto de uma Rotina da peça 6 §4 governa a saída, e um `Traço` de dano não é caro, é inexistente |
| não causa dano | **é exatamente o que `Traço` e `Comando` são** |

O `Maximum: Uzumaki` — *"combines any number of cursed spirits in the user's possession into one and hits the target with a blast"* — cai na primeira linha. E *"a user can only absorb tamed cursed spirits after killing their master"* é **reconseguir**, que a Q5 já mandou para tempo de campanha. *Um tipo inteiro do material atravessando a máquina sem pedir nada é o melhor sinal de que a máquina está certa.*

**O talismã pede uma entrada e tem outra travada.** A fonte define talismã como *"paper tags with sutras written on them"*, cuja função principal é **selar** — *"halt the lifestream and preserve the existence of cursed objects while preventing them from doing any further damage"* — e que *"can serve as an intermediary to conjure shikigami"*.

> **Selar não dá para escrever agora, e o motivo tem nome.** O alvo do selo é `objeto amaldiçoado`, que a **v0.49** descobriu não ter peça dona nenhuma e a **v0.50** pôs em **último** na fila. Uma entrada de catálogo apontando para lá é a vaga de Desliga nomeando a peça errada, que é o defeito que aquelas duas versões gastaram inteiras para achar. *Fica marcado com o nome certo em vez de escrito com o alvo errado.*

O que sobra do talismã é o eixo dos shikigami que **não** são do Megumi — o rato e o pássaro do Dhruv, o Kogane, o Marmalade Boy do Masaki. Todos batedores, e todos **informando o dono**. O `Faro` rastreia, mas nada em lugar nenhum dizia que o dono recebe alguma coisa disso. **É o `Vigia`**, e junto com ele veio o `Fala`, que é o mesmo eixo um passo adiante.

**E o corpo amaldiçoado trouxe três coisas, das quais só uma virou entrada.** A fonte o define como *"a nonliving object that has been endowed with a curse, allowing it to gain self-control"*, com núcleos fazendo as vezes de coração.

| o que o tipo pede | veredito |
|---|---|
| *"programmed with predetermined commands or act autonomously"* | **ilegal.** Agir sem o dono gastar a ação padrão **é** a exceção do `Coro`, e a Q4 comprou o teto de uma Rotina justamente porque ele cai da economia de ação. Virar ponto de orçamento devolve o teto para o decreto — e a Q4 inteira foi paga para tirá-lo de lá |
| o Ultimate Mechamaru operado de longe | **entrada**, mas só depois de existir amarra. Virou o `Remoto`, e a amarra está no §3.6 |
| o Panda, *"has three cores. He can shift the cores in battle"* | **não existe.** *Decisão do Mizuki* |

> **Por que o núcleo do Panda ficou de fora, escrito para não voltar.** Trocar de configuração no meio da luta não cabe nos degraus que existem, porque ele não compra capacidade: **ele dobra a montagem inteira.** As saídas medidas eram um degrau de 12 pontos — que nasceria inalcançável até o nível 6, porque o orçamento do nível 2 é 8, e é degrau com um morador só — ou concessão de Trilha, que empurraria a decisão para uma peça que ainda não existe. **Corpo amaldiçoado fica sendo fórmula de vida própria e sabor, como os outros três.**

E uma que eu quase escrevi: um `Traço` de corpo duro, tipo *"ela aguenta mais porque é objeto e não carne"*. **Ele compra Defesa com ponto, e a Defesa dela já sai do arranjo de atributo da peça 2** — dois preços para a mesma coisa, que é a lição nº 2 na forma exata em que ela costuma aparecer aqui.

### Quanto isso custa no filtro multi-mestre, medido

| | divergência possível entre dois mestres |
|---|---|
| o mestre precifica do zero | **2 pontos — 20%** do que a invocação entrega |
| **a escada por efeito, com a palavra final em cima** | **1 ponto — 10%** |

**A escada corta a divergência pela metade e a põe numa faixa com tamanho conhecido**, porque 1 ponto já foi medido: `+10%` do que ela entrega, ou `+11%` de vida efetiva. *Não é zero — e não devia ser: o que a peça 12 diz é que a palavra final é do mestre, e o que a régua faz é impedir que ela seja dada do nada.*

> **E o validador tem uma checagem a mais por causa disso:** toda entrada do catálogo tem de cair no degrau que a régua manda. **Uma entrada publicada que não obedece à própria régua é o que ensina a mesa a ignorá-la** — e aí o `Traço` inventado no meio da sessão passa a ser precificado por imitação de uma exceção.

### E montar os shikigami do material achou o buraco

| shikigami | montagem | pontos | cabe no nível | arranjo `For · Des · Con · Int · Ess` |
|---|---|---|---|---|
| Cão Divino | `Faro` | 5 | **2** | `1 · 3 · 2 · 0 · 3` |
| **Nue** | `Voo` | 8 | **2** | `1 · 3 · 2 · 1 · 2` |
| Elefante Máximo | `Jorro` | 8 | **2** | `3 · 2 · 3 · 1 · 0` |
| Serpente | `Emboscada` + `Agarrar` | 12 | 6 | `3 · 3 · 2 · 1 · 0` |
| Sapo | `Fisgada` + `Agarrar` | 12 | 6 | `2 · 3 · 3 · 0 · 1` |
| Nue completo | `Voo` + `Montaria` | 16 | 10 | `3 · 3 · 2 · 0 · 1` |

**A coluna do arranjo entrou na v0.181, e o atributo principal de cada um sai da entrada que ele compra** — não de gosto. **Qual atributo cada entrada pede sai do §4 da peça 1**, e o mapa é este:

| entrada | atributo que ela pede | por quê, na peça 1 §4 |
|---|---|---|
| `Faro` | **Essência** | ela rastreia por cheiro **e por energia**, e perceber energia é Essência |
| `Voo` · `Emboscada` · `Fisgada` | **Destreza** | voar, sair de onde não se via e acertar à distância |
| `Jorro` · `Agarrar` · `Montaria` | **Força** | empurrar, prender e carregar são os três verbos de Força |

**O resto de cada linha é a ficção do bicho**, e é a parte que o Mizuki manda:

| shikigami | por que o resto caiu assim |
|---|---|
| Cão Divino | cão de caça: sente e corre, e não segura nada. Força `1` |
| Nue | criatura de vento, equilibrada — ela não é boa em nada além de estar no ar |
| Elefante Máximo | massa. Força e Constituição no topo, e o `Jorro` empurra pelo tamanho |
| Serpente | vem de baixo e prende: Força para segurar, Destreza para a emboscada |
| Sapo | fica parado e alcança. Destreza na língua, Constituição para aguentar parado |
| Nue completo | o mesmo Nue carregando gente — a Força sobe porque a `Montaria` cobra |

*Os seis somam `9` e nenhum passa de `3`, e os seis são arranjos distintos: com seis montagens e seis arranjos legais, dois iguais seriam desperdício de exemplo.*

**Três dos seis cabem no nível 2 e os outros chegam nos marcos** — que é a leitura certa do material, onde os shikigami aparecem ao longo da história em vez de todos de uma vez.

> **Mas o Coelho de Fuga não fechava, e ele expôs uma divisão que ninguém tinha escrito.** Ele é *"muitos corpos"*, e muitos corpos custariam 3 pontos — **impossível no nível 2, que é onde a Trilha é escolhida.** A peça 6 e o `ESTADO-ATUAL` dizem que *"a Trilha vem no nível 2, e já rende ali"*.
>
> **A saída não é baratear o preço, é reconhecer de quem é o corpo:**
>
> **O que a Trilha concede não sai do orçamento.** `Servo` dá um corpo forte, `Matilha` dá os cinco, `Coro` dá a exceção de economia de ação. **O orçamento compra `Traço` e `Comando` por cima disso.** O Coelho de Fuga é a Trilha `Matilha` mais `Miúdo` — **7 pontos, e sobra 1 no nível 2.**
>
> *Isso resolve o nível 2 e, de quebra, dá à Q6 a única coisa que ela ainda não tinha: **o que cada Trilha concede que o orçamento não pode comprar.** A pergunta que estava esperando a peça de Trilhas ganhou metade da resposta aqui.*

### E as três montagens por Trilha, que a peça devia desde a v0.53

*A promessa é da v0.53, a Q6 que a bloqueava fechou na v0.63, e ela ficou aberta como aviso até a v0.186.* **Elas são outra coisa das seis acima:** *aquelas são shikigami do material montados com o catálogo; estas são a montagem que a Trilha pede, no nível em que ela é escolhida.*

| montagem por Trilha | entradas | pontos | orçamento no nv2 | `For · Des · Con · Int · Ess` |
|---|---|---|---|---|
| **`Servo`** | `Agarrar` + `Interpor` | 12 | 12 | `3 · 1 · 3 · 1 · 1` |
| **`Matilha`** | `Agarrar` + `Arrastar` | 8 | 8 | `3 · 2 · 1 · 1 · 2` |
| **`Coro`** | `Fisgada` | 8 | 8 | `1 · 3 · 1 · 2 · 2` |

**As três gastam o orçamento inteiro do nível 2**, e o do `Servo` é o da ficha mais metade pela concessão dele — não é montagem mais cara, é bolso maior.

**Cada uma mostra a concessão da Trilha, e não só o orçamento.** *O `Interpor` do `Servo` só faz sentido num corpo que aguenta o golpe, e é justamente o que aquela Trilha entrega; a `Matilha` agarra e arrasta com cinco de uma vez, que é o **"o que assusta é o número"** da peça 6 §4; e a `Fisgada` do `Coro` prende à distância para o golpe do dono entrar atrás — o encadeamento que ele compra com a exceção de economia de ação.*

*O arranjo segue a régua das seis: o principal sai da entrada comprada — `Agarrar` pede Força e `Fisgada` pede Destreza —, e o resto é a ficção do bicho.*

### O que cada Trilha concede — a Q6 fechou na v0.63

*Ela era a única pergunta que esta peça deixou aberta, e ela nunca foi desta peça: `Servo`, `Matilha` e `Coro` são Trilhas.* **Fechou pela régua da Q3 de Trilhas**, e o achado que a destravou é de forma e não de número: o `Servo` estava dominado **por falta de eixo**. Ele empatava em saída — o teto de uma Rotina é igual para as três — e perdia ou empatava em corpos e em ação, então não existia número que o consertasse dentro dos três eixos. *Subir a saída fura a peça 6 §4; dar corpo o transforma na `Matilha`; dar ação o transforma no `Coro`.*

> **O que a Trilha concede não sai do orçamento da ficha.** O orçamento compra `Traço` e `Comando` por cima.

| Trilha | o que ela concede | orçamento do corpo | vida do corpo |
|---|---|---|---|
| **`Servo`** | um corpo forte | **o da ficha mais metade**, arredondando para baixo | **`2,5 ×` a fórmula do tipo** |
| **`Matilha`** | os cinco corpos | o da ficha | `2,5 ×` a fórmula do tipo, em pool com cascata |
| **`Coro`** | atacar e comandar na mesma rodada | o da ficha | `h`, a fórmula crua |

> **`vida do corpo forte = 2,5 × (base do tipo + 2 × nível) + Constituição × nível`**, arredondando para baixo

**A Constituição fica FORA do multiplicador, e isso é o conserto da v0.178.** *Enquanto ela morava dentro, um ponto de Constituição valia `5 × o nível` num corpo de invocação e `1 × o nível` numa ficha de personagem — **cinco vezes mais**, em todo nível, e nenhum documento tinha precificado isso.* ***Achado do Mizuki:*** *"se for com con 0, ele tá passando do bastião; eu diria que a vida deveria seguir algo semelhante a vanguarda."* **Com a Constituição fora, a razão para de crescer**, e o `2,5 ×` foi escolhido contra uma banda que o Mizuki descreveu: *"vida entre o Evocador e a Vanguarda — com Constituição alta alcançar uma Vanguarda de Con `3` a `4`, com Constituição baixa ficar perto de um Emanador de `0` a `2`."* **No nível 30 isso é um piso de `122` a `182` e um teto de `243` a `273`, e o corpo cai dentro dos dois:** `155` com Con `0` e `245` com Con `3`.

| tipo | nv2 | nv10 | nv18 | nv30 |
|---|---|---|---|---|
| `talismã` · `corpo amaldiçoado` | 12 | 52 | 92 | 152 |
| `técnica` | 15 | 55 | 95 | 155 |
| `maldição domada` | 17 | 57 | 97 | 157 |
| *Vanguarda, para comparar* | *13* | *53* | *93* | *153* |
| *Bastião, para comparar* | *19* | *75* | *131* | *215* |

*As colunas são com Constituição `0` nos dois lados, e as duas bases ímpares descem meio ponto pelo arredondamento da peça 1 §5.4.* **A Constituição sozinha não cabe na banda em nenhuma base:** *ela vale `30` por ponto no nível 30 e a banda tem `150` de largura, então seis pontos andam `180` e estouram o teto de qualquer jeito.* **Fica declarado: a ficha de Constituição `5` ou `6` leva uma invocação acima da banda**, e o conserto disso seria um teto de atributo que esta peça não tem.

**A vida do `Servo` é o pool inteiro da `Matilha`, e o motivo era a regra de morte do §3.5.** *Até a v0.178 ela dizia que a invocação morre de vez se um único golpe causar a vida máxima **dela** — e com `h` a vida máxima do `Servo` era **um quinto** da da `Matilha`, para a mesma Rotina entregue:*

| nv | corpo do `Coro` (`h`) | corpo forte, `Servo` e `Matilha` | rodadas de chefe concentrando |
|---|---|---|---|
| 2 | 6 | 15 | `Coro` 0,7 · corpo forte 1,8 |
| 10 | 22 | 55 | 0,6 · 1,5 |
| 30 | 62 | 155 | 0,6 · 1,4 |

> **⚠ A coluna da direita caiu para um terço na v0.201, e não foi o corpo que encolheu.** *O modelo é o da peça 14 §4 — vida dividida pelo chefe concentrando —, e a tabela de inimigo do manual triplicou o dano de rodada do chefe naquela versão.* **Nenhum corpo perdeu um ponto de vida; o que mudou foi contra quem eles são medidos.** *A razão entre o corpo do `Coro` e o corpo forte não se move — ela é `2,5×` antes e depois —, e é ela que o argumento abaixo usa.*

*Decisão do Mizuki, e o argumento é dele:* ***"normalmente é a única invocação da pessoa, então ela tem de ser o equivalente de todas as outras, mas não passar muito delas — e ao perder a invocação principal, acabou o kit."*** **Com o mesmo corpo forte nos dois, eles saem da luta pelo mesmo golpe**, e apagar o `Servo` custa a mesma área por alvo que o §3.5 mede para apagar a `Matilha` — `0,83` Rotina desde a v0.178, e `1,25` antes dela. *Nenhuma exceção nova: a regra de morte continuou valendo palavra por palavra, e o que mudou foi o número que ela lê.*

> **⚠ A v0.178 tirou a régua da morte de dentro do corpo, então este argumento parou de sustentar o corpo forte sozinho — e o corpo forte fica.** *O que ele sustenta hoje é a outra metade, que a matriz de dominância não mede: o `Servo` é a Trilha de **um corpo só**, e com `h` ele iria a zero levando dois quintos do dano que derruba a `Matilha`, entregando a mesma Rotina.* **Cair não é morrer, e mesmo assim custa a Trilha inteira por uma rodada, mais PE, mais o corpo voltando com metade da vida.** *A coluna de rodadas de chefe acima continua sendo a medida certa disso; o que mudou é o nome do que ela mede.*

**E o orçamento é onde o `Servo` fica na frente**, que é o eixo que mata as duas dominâncias:

| nv | orçamento da ficha | do `Servo` | do catálogo inteiro (112 pontos) |
|---|---|---|---|
| 2 | 8 | **12** | 11% |
| 10 | 16 | **24** | 21% |
| 18 | 24 | **36** | 32% |
| 30 | 36 | **54** | 48% |

**A `Matilha` compra menos e aplica cinco vezes**, um por corpo — então em largura de utilidade ela continua na frente, que é o *"não passar muito delas"* medido.

> **O arredondamento continua sendo o da peça 1 §5.4 — ganho desce —, e na escala nova ele não tem o que raspar.** Todo orçamento é múltiplo de `4`, então `mais metade` sempre fecha redondo. *Na escala velha ele mordia nos níveis 6, 14, 22 e 30, e ali o `Servo` levava meio ponto a menos; com a moeda quebrada em quatro esse meio ponto passou a caber, e no nível 30 ele vale `2` pontos.* **É a mesma paridade que a v0.67 registrou na busca exaustiva, aparecendo do outro lado:** a moeda fina fecha conta que a grossa arredondava. *A regra não mudou; o que mudou foi ela deixar de morder aqui.*

> **O `Coro` fica com `h`, e isso é a troca dele escrita.** Ele é o único dos três que **ataca e comanda**, e é o único cujo corpo cair não acaba o kit — o dono continua batendo. *Perder o corpo do `Coro` custa metade da Rotina; perder o do `Servo` custava a Trilha inteira, e é essa assimetria que o corpo forte fecha.*

## 4. O nome da peça precisa de triagem, e o óbvio está ocupado

Rodada a triagem antes de escrever qualquer coisa:

| candidato | veredito |
|---|---|
| `Invocação` · `Invocacao` | **OCUPADO** — é Tema no manual |
| `Vínculo` | **OCUPADO** — é Tema no manual |
| `Servo` · `Matilha` · `Coro` | **OCUPADO** — já são Trilhas do Evocador |
| `Coleira` · `Convocação` | LIVRE |

**Não é impeditivo, e é preciso saber por quê.** Tema do manual não carrega mecânica, então o choque é de vocabulário e não de regra — mas a lição nº 4 manda checar nas duas direções antes de batizar, e o `conferir-nomes.py` compara literal. **Decidido na v0.58: a peça se chama Invocações**, com a linha da abertura dizendo que o Tema e a peça são coisas diferentes. O que pesou foi custo de troca contra tamanho da colisão: o nome já está em **17 citações** no `ESTADO-ATUAL`, **61** no `CHANGELOG` e **13** na peça 6, e a v0.50 decidiu por escrito que histórico de CHANGELOG não se reescreve — trocar deixaria noventa e tantas linhas falando de uma peça com outro nome, para consertar um choque com um rótulo que não tem mecânica. **`Coleira` e `Convocação` ficam anotadas aqui**, livres, caso um dia façam falta.

## 5. O que o validador confere

**São trinta e duas checagens, e elas moram no `conferir-invocacoes.py`.** A lista abaixo é a especificação delas: cada item diz o que se confere, de qual documento o número é lido, e — onde faz sentido — qual perturbação tem de acender aquela checagem e só ela.

*Ela foi escrita antes do validador, e é por isso que ele coube numa versão só.* A peça 14 gastou três versões com uma frase dizendo que o validador dela não podia ser escrito, e a premissa daquela frase tinha morrido três versões antes.

> **O arnês de perturbação obedece às três regras:** cópia isolada, base conferida verde **antes** de perturbar, e `diff` provando que a perturbação bateu antes de alguém ler o resultado. **As trinta e duas acendem a checagem certa**, e três delas acendem um par ou um trio declarado — que é o que acontece quando duas checagens leem o **mesmo dono** e é mais honesto declarar do que fingir isolamento. Mais dois contra-testes que não podem acender nada, e não acendem.

- **O teto da Rotina somada**, derivado da peça 6 §4 e nunca lido de constante — a lição nº 8 na forma que já apareceu três vezes.
- **Dominância entre as três Trilhas**, com a matriz rodando por quantidade de corpos.
- **E a tabela de rodadas de chefe recomputada, célula por célula**, porque ela é o único lugar da peça que mede **durabilidade** e ela não tinha ninguém em cima. *As três colunas saem de dono externo: a base do tipo do §3.6, o multiplicador da tabela de concessão, e o dano de chefe do `conferir-atributos.py`, com o modelo da peça 14 — `vida ÷ (dano_chefe × 0,5)`.* **Perturbar qualquer célula, ou o multiplicador, tem de acender** — e o contra-teste é reescrever a prosa em volta sem a checagem se mexer, porque âncora de regra não pode morar em frase.
- **O somatório**, contra o `conferir-orcamento.py`: invocar não pode caber junto com conjurar e levar dano de alma se o bolso não fechar.
- **Tempo de mesa**, se a Q2 fechar em cinco fichas — e essa não é checagem de código, é pergunta de playtest com número esperado escrito antes da sessão.
- **Triagem de todo nome** que a peça criar.
- **A queda do dono** *(a 31, da v0.163)*: os dois estados de 0 de vida saem da peça 1 §5.5 e a seção tem de responder os dois; a recusa de a invocação agir sozinha se ancora no teto que a peça 6 §4 publica, e não numa frase escrita aqui; a vida cheia se mede contra a decisão da peça 10 §3 — *respiro não devolve vida* —, e não contra a palavra "descanso longo"; e o capítulo 60 do livro tem de publicar as quatro linhas, porque decisão escrita só na peça não chega ao jogador.
- **Toda entrada do catálogo cai no degrau que a régua da criação manda** — `Traço` de 1 ponto só mexe na própria invocação, `Traço` de 2 encosta em outra criatura ou no tabuleiro; `Comando` de 1 age sobre um alvo, `Comando` de 2 protege ou nega. **Entrada publicada que desobedece à própria régua ensina a mesa a ignorá-la.**
- **Nenhuma entrada, publicada ou criada, com dado de dano, com refino dentro, ou vendendo atributo.** As três são ilegais e não têm preço.
- **O arranjo de atributo lido da peça 2, e o teto de criação conferido contra o ritmo da maestria.** *Perturbar os nove pontos, o teto `3` ou o teto `6` — na peça 15 ou na peça 2 — tem de acender, e o contra-teste é o número de arranjos legais: com três atributos ele cai para um, e um arranjo não é escolha.*
- **O orçamento por nível derivado dos marcos da peça 2, nunca lido de constante**, e a busca exaustiva sobre todas as montagens legais em cada degrau.
- **E o resumo do topo desta peça é cópia do orçamento, então ele é comparado com a tabela dona** — base, passo e teto. *Acrescentado na v0.68: ele passou a v0.67 inteira publicando a escala velha e ninguém comparava as duas.* **Apagar a linha também tem de acender**, senão o conserto barato para uma divergência vira sumir com a cópia.
- **E a tabela do orçamento do `Servo` é DERIVADA, nunca publicada:** a ficha sai dos marcos, o `Servo` sai de `×1,5` com o arredondamento da peça 1 §5.4, e **a porcentagem é recontada contra o catálogo somado** em vez de lida. *Acrescentada na v0.68, quando aquela tabela apareceu com o cabeçalho numa escala e as duas colunas na outra.*
- **As duas moedas separadas:** ponto de arma (`0,33` de dano por rodada) e ponto de ficha (`±10%` do que a invocação entrega) não podem se converter uma na outra em lugar nenhum. *Desde a v0.180 a checagem confere a **ausência de operação** em vez de recalcular uma razão: a venda de deslocamento era a única ponte entre as duas, e ela morreu com a ficha própria.*
- **E o `±10%` recomputado da taxa de câmbio do §3.3**, que é o dono dele. *Aquela tabela publica o par de porcentagens e o efeito, e o efeito é aritmética do d20 em cima do par — um ponto move cinco pontos percentuais porque a face do dado vale `5%`.* **As três linhas se conferem sozinhas, sem constante nenhuma no validador**, e o `±10%` do §3.6 tem de bater com a linha do acerto. *Acrescentada na v0.185: até ali o número era lido, impresso, e nunca comparado com nada — perturbá-lo saía **verde**, e foi um controle do arnês que mostrou que a cegueira era anterior à passada de texto.*
- **O multiplicador de área lido do documento dono, nunca de constante**, e o teste negativo: perturbar o `×2` para `×5` tem de fazer a checagem acusar que um feitiço de rotina apaga a Matilha.
- **Os dois gatilhos de morte em definitivo, com o contra-teste que importa:** nenhum golpe de rotina pode disparar nenhum dos dois. Perturbar o dano de um golpe comum para cima tem de acender.
- **O preço de invocar contra o bolso do BASTIÃO, nunca do Evocador** — e o `conferir-orcamento.py` é quem já sabe medir isso. Perturbar o `1 ×` para `1,5 ×` tem de acender no nível 2, que é onde ele morde.
- **O teto de uma Rotina conferido pela economia de ação, e não pela divisão escrita** — se algum dia comandar deixar de custar a ação padrão, o teto volta a precisar de decreto e a checagem tem de acusar.
- **A exceção do Coro medida somada**: atacar e comandar na mesma rodada não pode passar de uma Rotina.
- **A busca exaustiva sobre todas as montagens legais do orçamento**, no molde do que o `conferir-equipamento.py` faz com as 196 montagens de proteção — dominância entre montagens, e nenhuma gastando menos que o orçamento cheio.
- **As montagens publicadas conferidas contra a máquina**, e não só a máquina contra si mesma. *A peça 8 é o precedente e ele custou sete versões.* **São duas tabelas e elas se conferem diferente:** as seis do material contra o catálogo e o nível em que cabem; **as três por Trilha contra o orçamento do nível 2**, com o do `Servo` derivado da concessão dela e nunca lido. *Nas duas, o arranjo soma nove, topa em `3`, tem o principal saindo da entrada comprada, e é distinto dentro da própria tabela — e o capítulo 16 publica os mesmos.*
- **Nenhuma linha da ficha pode crescer em ritmo diferente de `+3`.** Perturbar o ritmo de qualquer linha derivada tem de acender — e o contra-teste é perturbar a **maestria na peça 1** e ver o acerto da invocação andar junto, provando que a checagem não se mede contra a própria constante.
- **A fórmula de vida lida da peça 1, nunca de constante.**
- **A invariante da Q2: nenhuma regra pode dar corpo com barra de vida própria.** A Matilha é um pool; uma Trilha ou aptidão que devolva barras separadas desfaz a conta do limiar `D = h` do §3.2.
- **A cota por corpo lida da peça 6 §4, nunca de constante** — `1/n` com `n` = corpos no campo, o dono contando como um deles. Perturbar o `5` da peça 6 tem de acender aqui.
- **O ganho de crítico da Matilha**, que com cinco d20 é `22,6%` de chance e `5%` de Rotina em ganho médio. Se algum dia a forma virar pacote único, esse número salta para 23% e o validador tem de acusar.
- **A invariante da Q1: nada pode dar à invocação um número de iniciativa separado do dono.** Uma Trilha, uma aptidão ou um Legado que conceda isso reabre os 97,6% da tabela do §3.1 inteira. **É invariante de texto e não de número**, no molde do que Equipamento faz com o teto de Defesa: a peça é dona da regra, e o validador confere que ninguém a fura.
- **A amarra lida do dono do número, nunca de constante.** Os 18 m são o alcance base de Projétil, do manual; o `conferir-manual.py` já sabe cruzar número do manual com o projeto. **Perturbar o alcance de Projétil tem de fazer a amarra andar junto** — a lição nº 8, no eixo em que ela mais reincidiu aqui.
- **As duas faixas acima do combate não podem ganhar metro em lugar nenhum.** *"Na cena"* e *"fora da cena"* são gatilho de ficção, no molde do relógio da peça 10; a metragem entre parênteses é referência. **Perturbar uma delas para um número tem de acender**, porque um número ali vira teste de fita métrica na mesa.
- **O gate de Origem do `Remoto`, e ele é o único do catálogo.** A checagem confere que **nenhuma outra entrada tem requisito** — se uma segunda aparecer, a régua de degrau do §3.7 deixou de precificar sozinha e isso tem de ser decisão e não descuido.
- **Nenhuma entrada do catálogo pode vender linha que já tem outro dono.** Acerto, Defesa e vida saem do arranjo de atributo da peça 2, e um `Traço` que dê qualquer um dos três cobra duas vezes pela mesma coisa. **Perturbar uma entrada para dar `+1` de Defesa tem de acender.**
- **A contagem do catálogo, conferida contra o que o documento afirma.** Hoje são **19 compráveis** mais o `Investir` a 0 — 13 `Traço` e 6 `Comando`. *A peça 13 já pagou por isso: as contas do rascunho dela envelheceram duas vezes dentro do próprio arquivo antes de o validador existir.* A checagem recalcula e falha se o escrito não bater com o contado.
- **A busca exaustiva rodada por degrau de orçamento, e o número esperado escrito antes.** No nv30, com orçamento 36 e gasto exato, o catálogo entrega **5.429 montagens cheias**, todas com assinatura distinta, **zero dominadas**, e a maior delas usa **9 das 19 entradas — 47%**. *Antes da passada dos três tipos eram **1.126** montagens em 13 entradas, e a maior consumia **62%** do catálogo; e antes da escala da v0.67 eram **21.502**.*

> **A queda de `21.502` para `5.429` é da escala, e ela tem nome: paridade.** Com preços de `1` e `2`, quase todo subconjunto fechava o orçamento exato. Com `2 · 3 · 4 · 5 · 7 · 8` num orçamento par, **um número ímpar de itens de preço ímpar nunca fecha** — e por isso três em cada quatro montagens deixam troco. *O que a busca conta é gasto exato; o conjunto de montagens **legais** não caiu na mesma proporção.* **Isso é propriedade da moeda quebrada e não descuido** — e é o preço que a v0.67 aceitou para o degrau de 1 ponto ter granularidade. Se alguma entrada nova puxar esse consumo para cima outra vez, é sinal de que ela não acrescentou eixo, só volume.
- **A Defesa da invocação lida do §3.3, e o passo dela medido contra o da Defesa do alvo.** A metade da Essência ou da Inteligência do dono é o que faz as duas crescerem no mesmo ritmo; sem ela a invocação vira alvo grátis no fim da campanha. **O teto do atributo sai da peça 2 e nunca daqui**, e o contra-teste é tirar a metade e ver o passo cair — se ele não cair, a checagem estaria passando verde sem o mecanismo que ela existe para conferir.
- **O dano do `Investir` recomputado dos quatro donos, e conferido nas DUAS publicações** — a tabela do §3.7 e a do capítulo 16 do livro. *A média do dado não fica escrita: ela é derivada da própria âncora do nível 30 que a peça 6 §3 publica*, e a reconstrução tem de reproduzir os quatro pontos daquela peça antes de a tabela valer alguma coisa. **Perturbar a Classe na peça 18, o fator da Rotina na peça 6, a cota, uma célula de qualquer das duas tabelas, ou apagar uma delas, tem de acender.** *E ela confere duas coisas que nenhuma outra confere: que a soma de volta não passa do teto de uma Rotina, e que a perda de arredondamento da `Matilha` nos níveis 2 a 4 está **declarada** em vez de esquecida.*

## 6. O que esta peça destrava

| destrava | como |
|---|---|
| **O Evocador** | 1 dos 5 Caminhos. Hoje ele escolhe Trilha na criação e não recebe nada por ela |
| **3 das 15 Trilhas** | `Servo`, `Matilha` e `Coro` **são** o sistema de invocação visto de dentro. As outras doze já estão desbloqueadas desde que Equipamento fechou |
| **A peça de Trilhas** | é a última dependência dela. Com Invocações fechada, as quinze ficam escrevíveis de uma vez |

**O que ela não destrava:** rota de Origem nenhuma. As nove continuam 6 jogáveis e 3 paradas — isso é da corrente de `ferramenta amaldiçoada` → `Técnica Marcial`. *A primeira metade saiu na v0.59, e é a peça 16; **sobra a `Técnica Marcial`**, que é a peça seguinte na fila.*
