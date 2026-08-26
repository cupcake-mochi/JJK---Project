# EQUIPAMENTO

**Fase 4, décima quarta peça.** Proteção, escudo, as 52 armas, treino e o requisito de Força — o que se veste e o que se empunha, num sistema em que o poder mora na técnica.
Versão v0.1 — 13/08/2026, fechada na v0.48 do projeto

*Viveu como rascunho sem número da v0.40 à v0.47, e virou peça quando o `conferir-equipamento.py` passou a existir.* **O validador dela é o `conferir-equipamento.py`**, e o §8 continua listando o que ficou em aberto — cada item com o motivo pelo qual ele não bloqueia a peça.

*Estado na v0.47: proteção fechada, categorias fechadas, recarga fechada, e **as 52 armas com dado e propriedades** (§5.3). A régua ganhou **fundo `3/5`** e o **dado virou entrada** — a ficção diz o tamanho da arma e o número de vagas cai da conta. **A restrição devolve orçamento** (§5.0.4). **O efeito de crítico da categoria morreu** (§5.1.1). E as duas decisões de acesso fecharam: **a divisão simples/marcial** (§5.4.1) e **o requisito de Força** (§5.5), que reancorou no dado depois de dois versões órfão.*

*A **penalidade** por empunhar sem treino ou sem requisito (§8 item 15) **fechou na v0.104**, na peça 19 §6: sem treino é **desvantagem na rolagem de ataque**; sem o requisito de Força o **deslocamento cai `3 m`**. As duas somadas custam `33,8` vezes o que a arma inteira entrega — é porta fechada, e não preço.*  * **Os nomes dos degraus de escudo fecharam na v0.59** — `Broquel`, `Médio` e `Torre`.*

> **Esta linha listava mais duas coisas até a v0.59, e as duas já estavam feitas.** O **validador** entrou na **v0.48** e é o `conferir-equipamento.py`. E **os dois dados do `Yumi`** foram corrigidos **nesta mesma peça, 573 linhas abaixo desta linha** — `Daikyū` para `1d10` e `Hankyū` para `1d8`, os dois fechando exatos em `4 de 4` (§5.3 e §8 item 16). *O §8 item 9 desta peça nomeou esse defeito com todas as letras — "uma conclusão que sobrevive à premissa" — e o cabeçalho dela estava fazendo exatamente isso, com o próprio texto dela como desmentido.*

> **A pergunta que a `Fineza` abriu está respondida, e a resposta não foi nenhuma das duas que esta nota oferecia.** Ela era *"ou a régua ganha uma exceção escrita, ou as propriedades soltas viram classes próprias"* — e as duas supunham que a classe ainda era o preço. **Ela não era mais:** a escada de dados do §5.2 já tinha posto `2d8` e `3d6` dentro da mesma `Tiro leve`, e ninguém tinha escrito isso. O catálogo já praticava 9 pacotes com 8 classes.
>
> **Decisão do Mizuki na v0.44: a classe para de ser o preço.** Cada arma carrega o próprio, dentro de um orçamento fechado por categoria de mão. O levantamento externo, a regressão contra as classes publicadas e a simulação estão no §5.0 e no §5.1.1.

Peça 2 da fila decidida na v0.36. Destrava a Vanguarda, a Técnica Marcial e **quatro das sete vagas de Desliga** da peça 13.

---

## 1. O que travava, e por que a resposta óbvia não servia

`Defesa = 10 + Destreza + proteção`, e a peça 11 §9 deixou o recado: *"um uniforme precisa valer mais que proteção 4, senão ele nasce morto."*

**Esse recado é orientação, não invariante, e tratá-lo como invariante trava a peça.** Proteção 1 é o que está assado dentro dos 50% de acerto que a peça 1 §6 promete. Cada ponto acima disso custa 5 pontos percentuais:

| proteção | acerta, em todo nível | rodadas de combate |
|---|---|---|
| **1** | **50%** | **3,7** — a linha da peça 1 |
| 3 | 40% | 4,6 |
| 5 | 30% | 6,2 |

Passar de 4 para não nascer morto põe o acerto 20 pontos abaixo do que o sistema promete.

**E a colisão de verdade é a lição nº 1:** cobrir-se cresce `+2` no refino passivo e `+3` no especialista; armadura de número fixo cresce `0`. Um número chapado só pode estar certo num nível.

> **Decisão do Mizuki:** o uniforme **não precisa ganhar** de cobrir-se. Precisa *alcançar e ter chance de passar*. Quem investiu Destreza e refino chegar a Defesa 20 é build, não defeito.

## 2. Duas classes, e o corte é o do 4e

A peça 6 §8 já tinha escrito *"leve e pesada, com requisito de Força e limite de Destreza na Defesa"*, e o levantamento confirmou que ela estava certa.

**O modo de falha da classe do meio é documentado.** Na 5e a armadura média é *"the worst-of-both-worlds of the best light armor and the best heavy armor"*, e o conserto oficial é gastar um feat só para ela funcionar. A 4e foi para duas classes de propósito, com o corte exatamente aqui: *"light armors let you add the better of your Dex or Int modifiers to your AC. Heavy armors do not have any ability score adjustment."*

A matriz de dominância deste projeto tinha achado o mesmo por outro caminho: com três classes, a média come a pesada sempre que a Destreza passa de 2.

**A régua do 3.x, que o levantamento também confirmou:** *"armor bonus + Max Dex adds up to either +7 or +8"* — proteção e teto de Destreza são um orçamento só.

## 3. A escada — nomes escolhidos pelo Mizuki

**`Traje`** (leve) e **`Revestimento`** (pesada). Os dois saíram `LIVRE` na triagem e não aparecem no manual nenhuma vez.

| degrau | **Traje** proteção | teto de Destreza | requer Força | **Revestimento** proteção | teto de Destreza | requer Força |
|---|---|---|---|---|---|---|
| 1 | 1 | — | — | 4 | 0 | **3** |
| 2 | 2 | — | — | 5 | 0 | **4** |
| 3 | 3 | — | **3** | 6 | 0 | **6** |

### A coluna de Força era uma só, e isso estava errado

*Achado na v0.42.* Até aqui os dois lados dividiam `3 / 5 / 6`, e o efeito era o **Traje — a classe leve — pedindo Força 6 no topo**. Ninguém tinha somado o que isso custa: Força 6 são três pontos de atributo acima do teto da criação, cobrados de quem escolheu a classe que existe justamente para quem não tem Força.

**Refeito com o orçamento de atributo compartilhado**, que é o furo da primeira medição — ela dava Força alta e Destreza alta ao mesmo personagem sem descontar as duas do mesmo bolso:

| gate no topo do Traje | abre no | Destreza que sobra | Defesa | acerto |
|---|---|---|---|---|
| sem gate | nv2 | 3 | 16 | 40% — cedo demais |
| **Força 3** | **nv6** | 4 | 17 | **45%** |
| Força 5 | nv10 | 4 | 17 | 50% |
| Força 6 (o de antes) | nv10 | 3 | 16 | 55% |

**Força 3 pousa exatamente nos 45% que esta seção já tinha aprovado**, e 3 é o teto da criação — cabe no array `3·2·2·1·1` sem gastar marco nenhum. Os degraus 1 e 2 do Traje não pedem nada. O `5` e o `6` eram herança da coluna dividida, e sobrepreço puro.

No Revestimento a escada fica, com o degrau do meio pedindo menos que o pesado: **`3 / 4 / 6`**.

**Sem gate de nível.** O orçamento de atributo faz o trabalho sozinho, e as duas escadas caem em lugares diferentes: o topo do Traje abre no nv6 e o do Revestimento no nv10.

*O motivo de não haver gate de nível é do Mizuki, e é de mesa:* sistema de "Custo 1 a 4" travado por nível força o personagem parrudo a usar uniforme leve porque é o que ele pode pegar, e ninguém gosta disso. Orçamento de como conseguir o item entra depois, não como trava de nível.

**O cruzamento cai em Destreza 3, igual nos três degraus** — Revestimento ganha de 0 a 3, Traje ganha de 4 pra cima. Sem classe do meio, ninguém espremido. *A mudança da coluna de Força não move esse ponto:* o cruzamento é de proteção contra proteção, e Força só decide quando o degrau abre.

### As duas rotas NÃO topam no mesmo lugar — equipamento para em 19

*Esta seção afirmava o contrário até a v0.42, e a frase era: "no nv30 com Destreza 6, cobrir-se com refino 10 dá Defesa 20, e Traje degrau 3 + escudo dá 20".* **O segundo número é 19.**

A frase é anterior ao §4. Quando o escudo ganhou **teto de Destreza** — que entrou para impedir `cobrir-se + escudo` de furar o 20 —, ele derrubou a rota do uniforme junto, e ninguém voltou aqui. Busca exaustiva de 196 montagens (7 uniformes × 4 escudos × 7 Destrezas):

| rota | topa em | por quantas montagens |
|---|---|---|
| cobrir-se, refino 10 | **20** | 3 |
| Traje 3 + escudo degrau 1 | 19 | 3 |
| Revestimento 3 + escudo degrau 3 | 19 | 7 |

**Nada passa de 20, e só a rota sem equipamento o alcança.** Decisão do Mizuki: **fica em 19, e vira decisão em vez de sobra.** No nv30 isso põe o atacante investido em 40% de acerto e o combate em 4,6 rodadas, contra os 35% e 5,3 que o 20 daria. A rota livre fica sozinha no topo porque refino 10 custa duas escolhas de marco — quem paga, chega mais alto.

### O dono do teto: ninguém escreve o número

*Isto fecha o item 8 do §8, e a resposta não é nenhuma das duas que aquele item oferecia.*

O 20 não é escolha esperando dono. Ele é o que sobra depois que três documentos já decidiram:

```
Defesa            = 10 + Destreza + proteção      peça 1 §5
teto de atributo  = 6                             peça 2 §3
teto de refino    = 10                            peça 2 §3
cobrir-se         = 1/3 do refino + 1  →  4       peça 11 §5

10 + 6 + 4 = 20
```

**Zero parâmetros livres.** Escrever `20` na peça 1 criaria a segunda fonte de um número derivado, que é a lição nº 9; e um validador que se medisse contra esse 20 escrito sairia **verde** ao perturbá-lo, que é a lição nº 8 pela quarta vez. Equipamento também não pode ser dona: ela nem alcança o número.

> **O que esta peça é dona é do invariante, não do valor:** *nenhuma montagem de equipamento passa da Defesa que a rota sem equipamento alcança.* O validador lê os três donos, deriva o teto e roda a busca exaustiva. Se a peça 11 mexer em cobrir-se um dia, o teto anda sozinho e a escada é reconferida — em vez de envelhecer calada.

### O Traje é sob medida, e o benefício dele não é proteção

**A conta fechou a porta do eixo da proteção, e foram as duas decisões acima que fecharam.** Equipamento para em 19 e o Traje é a classe sem teto de Destreza, então `10 + 6 + proteção ≤ 19` obriga **proteção ≤ 3**. E cobrir-se chega a 3 sozinho, na linha passiva, sem gastar escolha nenhuma:

| nv | refino passivo | cobrir-se | Traje 3 | ganho |
|---|---|---|---|---|
| 2–6 | 1–2 | 1 | 3 | **+2** |
| 10–18 | 3–5 | 2 | 3 | +1 |
| 22–30 | 6–8 | 3 | 3 | **+0** |

Não existe número de proteção que salve o Traje no fim da campanha: a janela **fecha sozinha** conforme o refino sobe de graça. Ele é a classe do meio do 5e reencarnada — não contra o Revestimento, contra **cobrir-se**, que é a armadura leve deste sistema e não tinha sido reconhecida como tal.

> **Decisão do Mizuki: o Traje ganha um benefício fora da proteção, e ele é feito sob medida para o personagem.**

**A Reação de cobrir-se fica nos dois lados** — o §7 é explícito, quem está de uniforme não tira o colete no meio do golpe. Com ela preservada, a conta no nv30 vira:

| quem | proteção | o que o Traje custa |
|---|---|---|
| não gasta escolha em refino (a maioria) | 3 contra 3 | nada — o benefício é ganho limpo |
| leva o refino ao teto 10 | 4 contra 3 | 1 de Defesa, ou 5 pp de acerto do inimigo |

*Os dois casos são o "alcançar e ter chance de passar" do §1, que é o critério que a classe precisava cumprir e não cumpria.*

**A forma do benefício: vantagem, e ela dispara em situação.** Vantagem já tem preço medido na peça 11 — **+25 pp contra alvo difícil, +9 pp contra fácil** —, é auto-regulada (dá pouco quando você já ia acertar), **não empilha** pela peça 4 §5, e não imprime número nenhum na ficha. Isso a mantém do lado certo da regra que o §6 escreveu: *item comum não produz número.*

O tamanho de "pequeno", pela frequência de disparo:

| dispara em | vale (alvo difícil) | veredito |
|---|---|---|
| toda rolagem de Destreza | 25,0 pp | bônus fixo com fantasia |
| metade das cenas | 12,5 pp | grande demais |
| **~1 por missão** | **2,5 pp** | **é o alvo** |
| 1 por arco | 0,8 pp | decorativo |

**O Traje carrega uma situação, não uma por degrau.** Três disparos por missão batem exatamente na linha que o §6 já traçou para consumível — *"3 ou mais vira a resposta padrão"* —, e a régua vale igual aqui.

**A máquina que faz "o jogador cria" sem virar discricionariedade já existe na peça 13:** é o **Destranca de identidade**. O jogador escolhe de uma lista fechada, escreve o que aquilo *é*, e a escolha é o gatilho, feita uma vez. A peça 13 já provou que segura pelo teste dos 90%, e já escreveu a trava que importa — **um Destranca de identidade não pendura tarefa**: ele diz o que é e para.

Aplicado aqui: a **lista é fechada e igual para todo mestre**; o que é do jogador é qual situação ele pega e como o traje dele é.

**A régua que peneira uma situação**, e é ela que governa também a vaga aberta:

> 1. É **condição física que o mestre já descreveu na cena** — não julgamento sobre o que o personagem tentou.
> 2. **Não decide o que uma das quatro perícias de Destreza já decide.** Senão vira vantagem em Furtividade pela porta dos fundos.
> 3. **Não acontece toda cena.** O alvo é ~1 disparo por missão.

*Candidatas que passam nas três:* vão apertado · altura e beirada · escuro · superfície ruim · água e chuva · multidão · terreno instável · calor e fogo.

**E uma vaga aberta, para o jogador inventar a dele** — decisão do Mizuki, e é o que faz "sob medida" ser verdade em vez de enfeite. Ela passa pela mesma régua de três itens, o que a torna conferível por um segundo mestre em vez de aprovada por um.

### Quem fabrica: o Alfaiate

*Levantamento do canon:* existe **um alfaiate dedicado ao mundo jujutsu**, o material dos uniformes é resistente a energia amaldiçoada, e **estudantes podem encomendar uniforme sob medida à escola**. O "sob medida" não precisou ser inventado.

> **Ressalva de fonte:** isso saiu de wiki de fã, que pela régua do projeto vale como **índice e não autoridade**. Confirmar no mangá antes de virar texto de mesa.

**Decisão do Mizuki: entra um ofício, o `Alfaiate`** — e ele é a opção do jogador que quer fabricar em vez de encomendar, engatando na mecânica de criação que vem depois. Passou na triagem como `LIVRE`, junto de `Alfaiataria`, `Tecelagem` e `Vestuario`. **`Costura` morreu:** é feitiço pronto **e** Passiva no manual, colisão de nome inteiro nas duas.

**Aplicado na mesma versão, e a lista do que ele tocou fica registrada:** `README`, peça 4 (três vezes), peça 6, peça 7 (o título do §5, a entrada nova, a proporção do §7 e a tabela do §8), peça 8, peça 13, `ESTADO-ATUAL` (duas vezes), `conferir-pericias.py`, `conferir-ficha.py`, `conferir-nomes.py`, `05-material/gerador-ficha/dados.js` e `05-material/gerador-ficha/ficha.js` — e os dois `.docx` da ficha, regerados.

> **A passada achou um buraco que não era o que ela foi procurar.** O `conferir-pericias.py` **nunca abriu a peça 7**: o docstring dele prometia *"contagem por atributo bate com o documento"* e a lista estava escrita dentro do próprio validador. Eram **três cópias** dos ofícios — a peça, o validador e o `dados.js` — e só duas eram comparadas, porque o `conferir-ficha.py` cruza a peça com o `dados.js` e ninguém cruzava a terceira. **Lição nº 9 dentro de um validador**, e ela só apareceu porque a contagem `!= 10` explodiu por acidente.
>
> Consertado na raiz: o `conferir-pericias.py` agora **lê a lista da peça 7**, e a contagem declarada sai do **título do §5** — separada da lista aplicada, que é a lição nº 8. O `conferir-ficha.py` deixou de procurar `'## 5. Os dez ofícios'` literal e passou a aceitar `Os \w+ ofícios`, porque mudar o título quebrava ele **pelo motivo errado**: ele acusava "não consegui ler a lista" quando o problema era o número por extenso.
>
> *E o `dez ofícios` da peça 13 era o único que não é contagem:* ele precifica o Legado `Gambiarra` por *"alcança dez ofícios, que é categoria inteira"*. **O argumento é "categoria inteira", então onze não muda a conclusão** — foi atualização de texto, não reprecificação.
>
> **A proporção caiu de 20% para 18%** — dois treinados de onze em vez de dez. Não é deriva: a peça 7 diz que *"ofício é para ser raro"*, e onze opções com dois treinados é mais raro que dez com dois. A conta de criação não mudou.

## 4. O escudo — a derivação anterior caiu, e o que sobrou é maior

*A primeira versão desta seção derivou `+1` comparando o escudo com o que a arma de duas mãos entrega, e concluiu que ele empatava no meio da campanha. **Três coisas estavam erradas, e a terceira é a que importa.***

### O que a conta velha dizia

| nível | golpe de chefe | +1 de proteção poupa | duas mãos rende |
|---|---|---|---|
| 6 | 17 | 0,9 | 2,0 |
| 14 | 36 | 1,8 | 2,0 |
| 22 | 54 | 2,7 | 2,0 |
| 30 | 72 | 3,6 | 2,0 |

A coluna do escudo continua certa. `0,05 × golpe de chefe` é o valor de tirar 5 pontos percentuais da chance do inimigo, e o `CHEFE` do manual é dano **por acerto** — é assim que o `conferir-atributos.py` o usa, multiplicando por `0,5` para chegar em dano por rodada.

**A coluna da arma é que não estava na mesma unidade.** Os `+2` de dado são o ganho *quando você acerta*, e num turno em que você usa a arma. Por rodada de combate ela vale:

> `2,0 de dado × 0,55 de acerto × quanto do tempo você dá golpe simples`

O `0,55` é a peça 1 §6 mais os 10% do crítico da §5.2. E o "quanto do tempo" tem teto conhecido: o `conferir-orcamento.py` mede o Bastião conjurando em **38% a 48%** das rodadas, e feitiço de Toque não soma arma (peça 5 §3). Sobram no máximo 62%, divididos com Classe 0 e projetar energia.

Refeita, com uso em 60%, a arma rende **0,66 por rodada** e o escudo passa ela no **nv6** em vez de no nv16.

### O terceiro erro, e é o que derruba a seção

**O custo do escudo não era a mão.** A peça 11 §5 e §9 e a peça 8 dizem, com todas as letras, que *"uniforme, armadura e **escudo** desligam a proteção de energia"*. Quem pega escudo troca `1/3 do refino + 1` por `+1`:

| nv | refino | cobrir-se dá | escudo dá | o escudo vale |
|---|---|---|---|---|
| 2 | 1 | 1 | 1 | 0 |
| 6 | 3 | 2 | 1 | **−1** |
| 14 | 6 | 3 | 1 | **−2** |
| 22 | 9 | 4 | 1 | **−3** |
| 30 | 10 | 4 | 1 | **−3** |

Do refino 3 em diante — o **primeiro marco**, em duas das três rotas — pegar um escudo tira Defesa. Ninguém pega. A conta velha mediu contra um escudo que não entraria em ficha nenhuma.

> **Decisão do Mizuki: o escudo passa a somar com cobrir-se em vez de desligar.** Isso muda o texto em três lugares — peça 8, peça 11 §5 e peça 11 §9 — e vai junto com a dívida da seção 6.

### E aí aparece o problema de verdade, que é da lição nº 1

Com o escudo somando, ele volta a ser `+1` puro. Só que `+1` de proteção **não tem número legal neste sistema**:

| nível | a arma de duas mãos rende | proteção +1 vale | quantas vezes mais |
|---|---|---|---|
| 2 | 0,66 | 0,30 | 0,5× |
| 10 | 0,66 | 1,30 | 2,0× |
| 22 | 0,66 | 2,69 | 4,1× |
| 30 | 0,66 | 3,60 | **5,5×** |

Para empatar no meio da campanha o escudo teria de valer **+0,33 de proteção**, e proteção fracionária não existe. **O menor escudo possível já é três vezes o que a troca comporta.**

A causa é a mesma que a seção 1 usou contra a armadura de número fixo, aplicada um nível abaixo: **proteção muda a chance e por isso cresce com o dano do inimigo; o dado da arma é constante.** Um deles cresce 12× ao longo da campanha e o outro não sai do lugar. Não existe número que faça os dois se cruzarem em mais de um ponto.

*A seção 1 já tinha escrito isso — "um número chapado só pode estar certo num nível" — e aplicou só a uniforme contra cobrir-se. Vale igual para escudo contra arma.*

### A régua de quantos golpes caem em você

A conta acima supõe **um golpe por rodada em cima deste personagem**, e esse número não é chute: é o que o `conferir-atributos.py` já usa para a trava de vida inteira, calculando quantas rodadas alguém aguenta com `vida ÷ (dano_chefe × 0,5)` — ou seja, o chefe concentrando num alvo.

**Fica 1,0, e por um motivo de dono:** se esta peça adotar outro número, ela passa a discordar da peça 1 sobre a mesma suposição. O que muda com ele:

| cenário | golpes/rodada | o escudo +1 vale no nv14 |
|---|---|---|
| chefe + capanga em cima de você | 2,0 | 3,56 |
| **chefe concentra em você** | **1,0** | **1,78** |
| chefe alterna entre dois da linha | 0,5 | 0,89 |
| chefe sorteia no grupo de quatro | 0,25 | 0,45 |

Ainda é a variável que mais move o resultado, e ela continua sem medição de mesa.

### Escudo que precisa ser levantado — a ideia do Mizuki, medida

*Pedida na v0.40: "talvez a ideia de path não seja ruim, o de ter de ativar o escudo pra ele realmente valer, não dando defesa passiva".*

O modelo existe e é do Pathfinder 2e. O texto de regra: **`Raise a Shield`, uma ação — "you gain its listed circumstance bonus to AC. Your shield remains raised until the start of your next turn."** Ativa no seu turno e vale até o próximo. Lá ele vem com uma segunda trava que este sistema não tem: o escudo **quebra** quando você usa o Shield Block.

**A régua para precificar isso já existe aqui, e é a da peça 3 §4:** *"Leve — consome um recurso."* Um escudo que come um slot do turno é uma Leve, e não precisa de régua nova.

Medindo cada slot pelo quanto ele corta o tempo em que o escudo está de pé:

| o escudo ativa na | quantas rodadas ele vale | valor no nv16 | contra os 0,66 da arma |
|---|---|---|---|
| nada (passivo) | 100% | 2,01 | 3,0× |
| **ação bônus** | 100% | 2,01 | 3,0× |
| ação padrão | ~50% | 1,01 | 1,5× |
| reação | ~45% | 0,90 | 1,4× |

**A ação bônus não cobra nada hoje**, e é por isso que ela empata com o passivo na tabela. Ela é o slot mais vazio do turno — a peça 3 §2 admite que é *"a peça mais herdada"*, e *"alguém usa ação bônus?"* está na lista de playtest do `ESTADO-ATUAL` desde a v0.26.

*Mas ela não fica vazia.* O `ESTADO-ATUAL` já promete que a peça de Caminhos dá ao Bastião **socar como ação bônus**. Quando aquela peça sair, o escudo em ação bônus passa a valer metade — **um preço que cresce sozinho conforme o sistema enche o slot**, que é o formato que a lição nº 1 pede. O problema é que ele cresce *depois*, e hoje o escudo ainda nasce três vezes forte demais.

> **Ativar ajuda e não resolve.** Nenhum dos quatro modelos chega nos 0,66, porque o defeito não é *quando* o escudo vale — é que proteção escala com o inimigo e o dado não.

### RD foi levantada e morreu, e o motivo não é numérico

A conta apontava para ela: `RD fixa` é a única forma que fica na mesma escala do dado da arma — erra por fator constante (1,5×) em todo nível, contra o fator crescente da proteção (0,5× a 5,5×).

> **Decisão do Mizuki: não.** *"Dar RD nunca é solução, pode acabar vindo a virar mais um cálculo e ninguém quer isso."*

**Fica registrado porque a conta e o critério discordaram, e o critério ganhou.** A conta mede valor por rodada; ela não mede quanto uma subtração a mais custa em tempo de mesa. Esse é o eixo em que a RD perde, e não existe validador que o meça.

*E as duas dívidas que ela criaria eram reais de todo jeito:* a Reação de cobrir-se já dá RD de `1,5 × refino` e passaria qualquer escudo em todo nível, o que exigiria regra de empilhamento; e RD sem tipo é mais larga que a Passiva Escama, que é paga — a mesma tensão que matou a Casca.

### Então: proteção, com requisito de Força e teto de Destreza

*A saída estava escrita na própria peça e passou batido duas vezes.*

A seção 3 fechou dizendo que **as duas rotas topam em Defesa 20**, e contou o escudo dentro disso: *"Traje degrau 3 + escudo dá 20"*. E a seção 2 já tinha adotado a régua do 3.x — ***"proteção e teto de Destreza são um orçamento só"***.

**Junte as duas e o escudo maior tem lugar:** ele não cresce por cima do teto, ele cresce **comendo teto de Destreza**, do mesmo jeito que o Revestimento. E aí ele vira o prêmio da build de Força sozinho, sem regra nova — porque quem tem Destreza baixa não perde nada com o teto.

| degrau | nome | proteção | teto de Destreza | requisito de Força | custa marco? |
|---|---|---|---|---|---|
| 1 | **`Broquel`** | 1 | 5 | — | não |
| 2 | **`Médio`** | 2 | 3 | 3 | não — cabe na criação |
| 3 | **`Torre`** | 3 | 1 | **5** | **sim, 2 pontos** |

**Os três nomes fecharam na v0.59.** O `Broquel` histórico é de punho, 15 a 45 cm — por isso ele não pede Força e quase não come Destreza. E a `Torre` cobre o corpo e se planta no chão, o que é a Destreza travada em 1 e o ponto de marco. *A escada de nome é a mesma escada de número: quanto mais escudo, menos braço sobra.*

> **O do meio é `Médio`, e ele carrega duas colisões declaradas em vez de escondidas.** *Decisão do Mizuki, com as duas na mesa.*
>
> **A primeira a triagem pega:** `Médio` sai **fraco**, a uma letra de `Medo`, que é **Tema** no manual. Aceita — `Medo` é Tema de feitiço e `Médio` é degrau de escudo, e as duas palavras nunca aparecem na mesma linha de regra.
>
> **A segunda a triagem NÃO pega, e é o mesmo ponto cego que o §5.4.1 desta peça já registrou:** `Leve`, `Média` e `Pesada` são os **tiers de Restrição** da peça 3, e eles saem `LIVRE` porque tier de magnitude não está em lista nenhuma do manual. **`Médio` (escudo) e `Média` (Restrição) são a mesma palavra em gêneros diferentes**, do mesmo jeito que a classe de arma `Pesada` já colide com o tier `Pesada` desde que as duas existem. **É a segunda colisão aceita nesta peça, no mesmo eixo** — e por isso ela fica escrita aqui e não descoberta na mesa: *escudo `Médio` é objeto; Restrição `Média` é preço. Uma se empunha, a outra se paga.*

**O degrau 3 é o primeiro item do catálogo inteiro que cobra ponto de marco.** Toda arma pede no máximo Força 3, que é o teto da criação; ele pede 5. Isso dá à Força um trabalho que ela não tinha — e a peça 1 tem *"Força tem uma perícia só"* aberto desde a v0.24.

**Busca exaustiva de todas as combinações de uniforme × escudo × Destreza:**

| combinação | Destreza útil | proteção | Defesa |
|---|---|---|---|
| cobrir-se refino 10, sem escudo | 6 | 4 | **20** |
| cobrir-se refino 10 + degrau 1 | 5 | 5 | **20** |
| Traje 3 + degrau 1 | 5 | 4 | 19 |
| Revestimento 3 + degrau 3 | 0 | 9 | 19 |

**Nada passa de 20, e 20 é alcançado por duas rotas diferentes** — o teto não é decorativo. *E o teto de Destreza do degrau 1 não é enfeite: sem ele, `cobrir-se + escudo` dava **21** e furava o teto do §3. Foi a decisão de o escudo somar que abriu esse buraco, e é ela que precisa fechá-lo.*

**Nenhum dos três é dominado.** O cruzamento entre o degrau 1 e o degrau 3 cai em **Destreza 3** — o mesmo ponto em que Traje e Revestimento se cruzam na seção 3. Uma régua, dois lugares: quem aprende uma vez aplica nos dois.

| Destreza | degrau 1 | degrau 2 | degrau 3 | melhor |
|---|---|---|---|---|
| 0–1 | 15–16 | 16–17 | **17–18** | degrau 3 |
| 2–3 | 17–18 | **18–19** | 18 | degrau 2 |
| 4–6 | **19–20** | 19 | 18 | degrau 1 |

**A categoria se chama Escudo.** *Decisão do Mizuki:* os tipos podem ter nomes próprios, mas o guarda-chuva é a palavra que todo mundo já usa. Ela saiu `DENTRO` e não `OCUPADO` na triagem corrigida — estava só dentro de **Rasga Escudo**, e uma Melhoria que rasga escudos não *é* um escudo.

**Os três nomes foram escolhidos na v0.59: `Broquel` · `Médio` · `Torre`.** Mortos na triagem anterior: `Anteparo` é **Melhoria** e `Bloqueio` é **Tema**, os dois com o nome inteiro. Sobraram sem uso: `Pavês`, `Adarga`, `Rodela`, `Tarja`, `Couraça` e `Guarda-Corpo`.

### O que isso NÃO conserta, e é melhor dizer

O escudo com requisito resolve o que foi pedido — dá trabalho à Força, cabe no teto, três degraus sem dominância. **Ele não conserta a arma de duas mãos.**

| nv | o degrau 3 poupa | a Pesada rende | razão |
|---|---|---|---|
| 6 | 2,58 | 0,66 | 4× |
| 14 | 5,34 | 0,66 | 8× |
| 22 | 8,07 | 0,66 | 12× |
| 30 | 10,80 | 0,66 | **16×** |

Proteção escala, dado não. **Isso não tem conserto dentro desta peça** — e provavelmente não deveria ter. A régua da seção 5 diz que *"a arma dá acesso e restrição; o Caminho dá o que você faz com ela"*: **duas mãos é acesso à árvore que exige duas mãos**, e é a Trilha da Vanguarda que precisa dar razão para largar o escudo. Por isso aquela peça vem depois desta na fila da v0.36.

**O alvo fica registrado aqui, para quando ela chegar:**

| nv | o buraco | em fração da Rotina |
|---|---|---|
| 6 | 1,92 | 6,2% |
| 14 | 4,68 | 7,4% |
| 22 | 7,41 | 7,9% |
| 30 | 10,14 | 9,4% |

**De 6% a 9% da Rotina, e a fração quase não deriva** — é um alvo estável, que é o melhor tipo de alvo para passar adiante. E ele **não pode ser pago em dado de dano**: a peça 5 §4 proíbe e a v0.36 confirmou. Sai de posicionamento, alvo, duração ou exceção de ação.

### O que o escudo NÃO custa, e eu tinha escrito errado

`Gesto` é uma Restrição **Leve**, e Leve devolve `teto(Classe/2)`. **Mas Gesto é uma de treze Leve** — Parado, Tudo ou Nada, Uma Vez, Frágil, Barulho, Assinatura, Aquecer, Peso Morto, Condicional, Fraqueza e mais. Trocar Gesto por Parado devolve exatamente o mesmo. **Perder Gesto não custa quase nada.**

**A exceção é o Selo**, e ela é de graça: o manual define Selo como *"Gesto ou condição obrigatória pra conjurar, **igual pra todos os seus feitiços**"*. Quem escolheu Gesto como Selo e pega um escudo **desliga a técnica inteira**. Trava que se aplica sozinha, sem regra nova.

## 5. Armas — o preço mora na arma, e ele tem orçamento

*Reescrito na v0.44. A régua anterior era **"o preço mora na classe"**, e ela caiu por dois motivos: um que o Mizuki quis e um que já tinha acontecido sem ninguém ver.*

**O que ele quis:** *"a ideia é deixar cada arma sendo especial à sua forma — algumas iguais às outras e a mudança é só estética, ideal não, mas não tem problema. Cada arma ser mais única é o que dá prazer de escolher."*

**O que já tinha acontecido:** a escada de dados do §5.2 põe **dois dados diferentes dentro da mesma classe** — a Pistola rola `2d8` e a Submetralhadora rola `3d6`, e as duas são `Tiro leve`, que diz `d6`. Com zero arma nova, o catálogo já tinha **9 pacotes de preço para 8 classes**. A classe deixou de ser o preço na v0.42, e quem a tirou desse posto foi a decisão do 3d10.

> **A régua nova: a arma carrega o próprio preço, e ele fecha num orçamento.**

A classe some como preço. O que sobra dela é a **categoria**, que já existe e é o gancho da Vanguarda.

### 5.0 O orçamento, derivado das classes que já estavam escritas

**A unidade não foi escolhida, foi medida.** O §5.2 mediu o passo de dado em `0,33` por rodada e o `Par` em `0,32` — **um passo de dado e uma propriedade valem o mesmo neste sistema.** Então:

```
1 ponto  =  0,33 por rodada  =  um passo de dado  =  uma propriedade
dado     :  d4 = 0 · d6 = 1 · d8 = 2 · d10 = 3 · d12 = 4
```

Tratando as seis classes de corpo a corpo já publicadas como **dados de uma regressão**, e não como regra:

| classe publicada | dado | propriedades | mãos | gasto |
|---|---|---|---|---|
| Oculta | d4 | `Oculta` · `Longo Alcance` | 1 | **2** |
| Curta | d6 | `Par` | 1 | **2** |
| Uma mão | d8 | — | 1 | **2** |
| Versátil | d8 | `Versátil` | 1 | 3 |
| Haste | d10 | `Alcance` | 2 | **4** |
| Pesada | d12 | — | 2 | **4** |

> **O orçamento é `2` para uma mão e `4` para duas mãos.** Cinco das seis fecham exatas, e ninguém escolheu esses números — eles são o que o catálogo já praticava.

**E o contra-teste passou sozinho.** A sexta linha, a `Versátil`, gasta **3 num orçamento de 2** — estoura em exatamente **1 ponto**. Aquilo é a dominância que o §5 tinha achado e registrado como *"fraca, e não existe caso em que a `Uma mão` seja melhor"*, **sem conseguir dizer de que tamanho ela era.** A régua reencontrou o defeito de fora, e o dimensionou: `Uma mão` + 1 ponto.

### 5.0.1 A régua inteira, numa tabela

*Pedido do Mizuki: **"seguir a lógica do Pathfinder — precificar o que uma arma pode ter."*** Ela sai do orçamento sem regra nova nenhuma:

| propriedades **pagas** | **uma mão** (fundo 3) | **duas mãos** (fundo 5) |
|---|---|---|
| 0 | — | — |
| 1 | **d8** | **d12** |
| 2 | **d6** | **d10** |
| 3 | **d4** | **d8** |
| 4 | — | **d6** |
| 5 | — | **d4** |

> **A palavra `pagas` não é enfeite, e ela custou um achado.** Até a v0.45 esta coluna dizia só *"propriedades"* e supunha **1 ponto cada** — mas a `Versátil` foi a zero na v0.44 e a `Munição` é textura. Varridas as 54 combinações legais de corpo a corpo, a tabela discordava do orçamento em **15 delas, e todas as 15 tinham `Versátil` dentro**: a linha *"3 propriedades numa mão"* chamava de ilegal uma combinação que o orçamento aprova. **A régua nunca esteve errada; a tabela é que era um atalho que envelheceu.**

> **E o `0` sumiu de propósito.** Com o fundo `3/5`, uma arma sem propriedade nenhuma gastaria menos que o orçamento — que é dominância estrita. **Toda arma é obrigada a encher as vagas**, então identidade deixou de ser opcional e virou construção.

**É o mecanismo do PF2e — propriedade definidora limitando o dado —, só que aqui ele não precisa ser escrito à mão.** Lá a lista de tetos é decidida caso a caso (`Agile` d6, `Finesse` d6, `Reach` d10 e proíbe `Agile`); aqui a lista **é** o orçamento, e combinação abusiva fica ilegal por construção em vez de ser pega no teste.

*Contra-teste:* a tabela reproduz cinco das seis classes publicadas — `Oculta` d4+2 · `Curta` d6+1 · `Uma mão` d8+0 · `Haste` d10+1 · `Pesada` d12+0 — e reprova a sexta, que é a `Versátil`, pelo mesmo ponto de sempre.

**E o teto da `Fineza` cai sozinho dela.** `Fineza` custa 1 ponto, então numa mão sobra 1 para o dado: **d6**. Conferindo pelo outro lado, com o critério de que a rota de Destreza empata em Defesa 19 e precisa ficar atrás em dano: `Fineza` num **d12** daria `6,5 + Destreza 6 = 12,5`, que **empata com a `Pesada` nos dois eixos** — dominância. O orçamento corta três degraus antes disso. *É exatamente onde o PF2e põe o teto do `Finesse`, por um caminho diferente.*

### 5.0.2 Por que isso não vira a armadilha da longsword

A peça 5 já provou que **o dado não é alavanca**: trocar d6 por d12 move três pontos numa lacuna de cem contra a coluna Rotina. **Isso é o que torna o preço por arma barato aqui, e é o contrário do 5e**, onde o dado *é* a arma inteira e por isso duas armas com o mesmo dado são o mesmo item — o defeito que o próprio material do hobby descreve como *"um Guerreiro não tem razão real para escolher Machado de Batalha em vez de Martelo de Guerra ou Espada Longa."*

**Mas nenhum dos dois eixos é livre, e a direção entre eles inverteu na v0.45.** Escolhidas as mãos e o dado, **sobra um número de vagas só** — gastar menos que o orçamento é dominância estrita, então ninguém gasta. Quem entra é o dado; quem sai é a quantidade de propriedade. A tabela é a do §5.0.1, e ela é a única.

> **Esta subseção trazia aqui a tabela invertida da v0.44** — `0 propriedades → d8`, com o dado como *saída*. Ela ficou três seções abaixo da tabela nova contradizendo ela, e sobreviveu à v0.45 e à v0.46. **É o mesmo defeito que a v0.43 pagou para aprender: a prosa de um documento contra a tabela do próprio documento**, e agora tabela contra tabela. *Achado na passada da v0.47, lendo o §5.0.1 e o §5.0.2 na mesma sentada.*

**Quem carrega a variação continua sendo a propriedade, e propriedade não é escolha: é o que a arma é.** Uma naginata tem `Alcance` e ocupa as duas mãos; o que a régua decide é que, sendo `d10` em duas mãos, ela tem **duas** vagas para gastar — e a segunda é o que a separa da Yari, que tem o mesmo dado e o mesmo alcance.

Rodando a régua sobre as 41 armas de corpo a corpo, com as propriedades que a ficção de cada uma força:

| eixo | assinaturas | armas com gêmea |
|---|---|---|
| só o preço | **14** | 35 de 41 — **85%** |
| preço × categoria | **25** | 25 de 41 — **61%** |

**Gêmea continua permitida e de graça, como a v0.41 decidiu.** O que mudou é que ela deixou de ser rara: quatro facas pequenas terminando no mesmo número é exatamente o caso que já foi aceito, mas 61% não é "nenhuma arma é obrigada a ter".

### 5.0.3 O que o orçamento **não** consegue precificar: a mão

`Duas mãos` custa o escudo, e o escudo não tem um valor — ele tem uma curva:

| | escudo +1 vale | em pontos |
|---|---|---|
| nv2 | 0,30 | 0,9 |
| nv16 | 2,01 | 6,1 |
| nv30 | 3,60 | **10,9** |

**O mesmo item, 12× de diferença entre as pontas.** Nenhum número fixo fecha nos dois, e é por isso que `Duas mãos` **não é item de orçamento: é categoria de orçamento**, com número próprio (`4` contra `2`). É a mesma saída que o 3.x e o PF2e usam — lá os orçamentos de uma e duas mãos são tabelas separadas, e não uma propriedade precificada.

O que sobra fora da conta continua sendo o buraco registrado no §4: **6% a 9% da Rotina, que a Trilha da Vanguarda deve.** O orçamento não o fecha e não deve tentar.

### 5.0.4 A restrição devolve orçamento — a metade do §5 que faltava

*Fechado na v0.45, e ela é a peça que resolveu a identidade.*

> **A arma dá acesso e restrição.** É a frase que abre este §5 desde que ele existe, e **só o acesso tinha sido implementado.**

**A máquina já é da casa, e é do Fundamento:** `Leve` devolve `teto(Classe/2)` e `Média` devolve `Classe`. Aplicada uma camada abaixo:

> **Uma arma pode carregar um defeito de verdade e comprar uma propriedade com ele. Cada restrição devolve `1` ponto.**

| restrição | o que é |
|---|---|
| `Volumosa` | não dá para esconder, e atrapalha em espaço apertado |
| `Embainhada` | não se saca sozinha: precisa de tempo, ou de outra pessoa |
| `Comprida` | perde no corpo a corpo colado |

**Não virou resposta padrão, e a conta diz de quanto:** **3 das 41** usam (7%) — Odachi, Nodachi e Machado de Guerra, que são as três que a ficção já carregava de defeito. *A `Comprida` não achou dono nesta passada: o Bō virou `d10` e não precisou dela. Ou ela some, ou espera uma arma que a peça.*

**O limite é 1 restrição por arma.** O Fundamento aceita duas porque lá o orçamento é grande; aqui o orçamento inteiro de uma mão é `3`, e uma segunda restrição pagaria dois terços da arma com defeito — o que é a arma sendo definida pelo que ela não faz.

### 5.0.5 O tiro tem escada e fundo próprios — fechado na v0.47

*Aberto sem ninguém ver desde a v0.45: aquela versão pôs **fundo** no corpo a corpo e não voltou para as onze de tiro. O §5.3 afirmava "zero armas com vaga vazia", e isso valia para as 41.*

**A régua do corpo a corpo não serve para o tiro, e a conta diz por quê.** A fórmula do §5.2 desconta `2,5` (o piso, que é o `d4`) e `6,0` (a Força que o corpo a corpo soma). Aplicada à escada do tiro:

| dado | média | gasto pela fórmula |
|---|---|---|
| `1d10` | 5,5 | **0 — grampeado** |
| `2d6` | 7,0 | **0 — grampeado** |
| `2d8` | 9,0 | 0,5 |
| `2d10` | 11,0 | 2,5 |

**Dois defeitos, e o segundo é o que importa.** Os gastos são **fracionários**, então propriedade inteira nunca fecha o orçamento exato. E `1d10` e `2d6` custam **os dois zero**, porque a fórmula grampeia no piso — **a régua não consegue distinguir uma pistola de uma submetralhadora.** Não é que ninguém preencheu as vagas: é que a escada não tinha resolução no próprio fundo.

> **O conserto é o precedente do §5.0.3, um eixo ao lado.** Lá está escrito que *"`Duas mãos` não é item de orçamento: é **categoria** de orçamento, com número próprio"*. **A arma de tiro é a mesma coisa: o degrau da escada dela É a unidade.**
>
> ```
> 1d10 · 2d6 · 2d8 · 2d10   =   0 · 1 · 2 · 3
> fundo:  2 numa mão,  4 em duas
> ```

**O fundo do tiro fica em `2/4` e não sobe para `3/5`, e o motivo já estava escrito:** o §5.2 diz que *"o topo fica um ponto abaixo da `Pesada` porque ele paga o `Longo Alcance`"*. **A distância é o ponto que o tiro gasta e o corpo a corpo não** — é ela que compra o fundo mais baixo, e é por isso que ele não é punição.

**As duas do `Yumi` ficam nesta escada mesmo somando Destreza**, e fecham exatas em `4 de 4`. *A primeira versão desta seção as mandou para o fundo `5` do corpo a corpo, pela régua do §5.1.2 — e aí as duas passavam a ter vaga vazia. **O buraco era da proposta, não do catálogo**: a régua do §5.1.2 decide quem soma atributo, e o §5.0.5 decide qual escada precifica. São perguntas diferentes e não precisam da mesma resposta.*

### `Silenciosa` foi levantada, e o manual já tinha a resposta

*Ideia do Mizuki, para dar aos arcos o ponto que faltava:* **"uma propriedade que não tira o personagem de furtividade, exigindo um teste novo com penalidade, diferente das armas que revelam de imediato."**

**A máquina está certa, e o projeto concorda com ela em três lugares** — é a **camada 1 do §6**, *"move de não rola para rola"*, que é exatamente o que a `Oculta` já faz para o momento de **carregar** a arma. `Silenciosa` seria a mesma coisa para o momento de **usar**.

**Mas ela não entra, e são quatro motivos independentes:**

| | |
|---|---|
| **o nome está ocupado, e não é substring** | `Silencioso` é **Melhoria no manual**: *"Sem gesto, sem palavra. **Ninguém percebe que você conjurou.**"* Mesmo efeito, mesmo nome, uma camada acima |
| **a regra da qual ela isentaria não existe** | zero ocorrências de barulho quebrando furtividade nas treze peças. **É a Passiva Casca de novo** — preço por um termo que só existe dentro dele mesmo, lição nº 6 |
| **o eixo está errado** | o §5.0.2 diz que *"propriedade não é escolha: é o que a arma é"*. Então **toda arma sem `Silenciosa` faz barulho** — e isso põe o tantō e a soqueira fazendo mais barulho que um arco longo |
| **e os arcos não precisavam** | o buraco era da minha proposta, não do catálogo. No fundo `2/4` os dois fecham exatos |

> **A metade que sobrevive é a boa, e ela é uma linha em vez de uma propriedade.** Quem faz barulho não é *a arma*: é a **`Arma de Fogo`**, e categoria é onde este documento já põe *"o que a coisa é"*. Uma linha na categoria resolve o que uma propriedade em quarenta e cinco armas resolveria pior. **Fica no §8 item 19, esperando a peça que tiver regra de furtividade** — porque hoje ela seria preço sem regra pendurada.

### 5.0.6 O soco — a única entrada sem categoria e sem propriedade

*Decisão do Mizuki na v0.74, e ela nasceu do avesso: a Trilha do soco do Bastião estava sendo preçada contra `1d10 + Força`, que é a linha de comparação do §2 da **peça 5** e é outra arma. **O punho vazio não tinha dado escrito em documento nenhum.***

> **O soco não pertence a categoria nenhuma e não tem propriedade nenhuma. O dado dele sobe com a maestria.**
>
> | maestria | níveis | dado |
> |---|---|---|
> | 1 | 2 a 9 | **d4** |
> | 2 | 10 a 17 | **d6** |
> | 3 | 18 a 25 | **d8** |
> | 4 | 26 a 30 | **d10** |

**Ele soma Força**, como todo corpo a corpo pela régua do §5.1.2, e é **arma para todo efeito de regra** — crítico, ataque extra, requisito de treino. Não é arma para efeito de **catálogo**: ele não é uma das 52, não entra na divisão simples/marcial e não aparece no §5.3.

**E não é exceção: ele fecha exato na régua deste documento.** O fundo de uma mão é `3`, o dado custa `d4 = 0 · d6 = 1 · d8 = 2 · d10 = 3`, e zero propriedade custa zero.

| maestria | dado | gasta | fundo de uma mão | |
|---|---|---|---|---|
| 1 | d4 | 0 | 3 | `3` abaixo |
| 2 | d6 | 1 | 3 | `2` abaixo |
| 3 | d8 | 2 | 3 | `1` abaixo |
| **4** | **d10** | **3** | **3** | **exato** |

**O soco nasce dominado e chega à paridade no fim, e nunca passa dela.** Um personagem de nível 2 que soca está três pontos atrás de qualquer arma; um de nível 26 está no fundo cheio. *É por isso que o teto é `d10` e não `d12`: `d12` custa `4` e só existe em duas mãos, e o soco não tem uma segunda mão para vender.*

> **Zero propriedade é o que balanceia, e o §5.0 já dizia que isso não podia existir.** Aquela seção tirou a linha do `0` porque *"uma arma sem propriedade nenhuma gastaria menos que o orçamento — que é dominância estrita"*. **A saída não é abrir exceção: é que `0` propriedade tem um dado próprio, e ele é o `d10`.** A linha nunca esteve errada para as 52, porque nenhuma delas escolhe não ter identidade. O soco não escolhe — ele **é** a ausência dela.
>
> **E a conta que sai daí é a que vale para a mesa:** o soco no topo bate mais forte que qualquer arma de uma mão do catálogo, e não faz nada além de bater. A `Katana` troca dois pontos de dado por `Versátil` e `Fineza`; o `Machete` troca um por `Rompe`. **Quem soca abre mão de alcance, de `Par`, de `Oculta`, de `Talha` e de tudo o mais.**

**A Manopla continua viva, e é isso que prova que a régua está certa.** `Soqueira` e `Tekko` são `d4` com `Vestida`·`Oculta`·`Par`, e fecham `3/3` iguaizinho. **As duas entradas gastam o mesmo orçamento e compram coisas opostas** — o punho vazio compra dado, a manopla compra três propriedades. *Sem esta seção elas morreriam na maestria 2, porque arma vestida perdendo para não vestir nada é dominância estrita.*

**O requisito de Força não pega o soco.** O §5.5 lê o **dado impresso** e gateia `d10` e `d12` no corpo a corpo, então o soco entraria no requisito exatamente no nível 26. Ele fica **isento, por escrito**: o requisito existe para arma que você levanta, e não há como um personagem não alcançar o próprio punho. *É a mesma lógica que já isenta o passo do `Versátil`, que também não é dado impresso.*

> **O que esta seção mata em outro documento:** a primeira linha do `Corpo Duro` do Bastião — *"o seu ataque desarmado conta como arma, e você ataca desarmado sem empunhar nada"* — vira regra de todo feiticeiro e sai do Caminho. **O Caminho não pode dar dado de dano (peça 5 §4), e agora ele não precisa: o dado nunca foi dele.**

## 5.1 A categoria — o que a arma é

*Entrou na v0.42.* A classe é o pacote mecânico: dado, Força mínima, propriedades. **A categoria é o que a coisa é.** Ela existe por dois motivos, e nenhum dos dois é preço.

O primeiro é que ela resolve de onde vem o dano — foi ela que destravou a arma de tiro, que acertava com Destreza e causava dano com Força porque ninguém tinha cruzado a peça 1 §5 com a peça 6 §3. O segundo é que **ela é o gancho onde a Trilha da Vanguarda vai pendurar a especialização**, e sem ela aquela peça nasce sem ter em que especializar.

> **A categoria carregava uma coisa só: a fonte do dano.** *Reaberto na v0.44, e o motivo de reabrir é que a premissa caiu.* A trava original era: *"se ela carregasse número próprio, o valor de uma arma viraria `classe + categoria + propriedade` e a matriz teria de rodar sobre o produto dos três — que é a lição nº 7 pela porta de trás."*
>
> **Com a classe saindo do preço no §5, esse produto deixou de existir.** Sobrou `arma × categoria`, e a arma inteira agora fecha num orçamento em vez de ser comparada par a par. **A objeção era a matriz, e a matriz mudou de forma.**

### 5.1.1 O efeito de crítico MORREU na v0.45 — e o motivo é frequência

> **Achado do Mizuki:** *"ninguém lembra do efeito de crítico na hora de aplicar."* **A conta confirmou com folga.**

| | |
|---|---|
| dispara por rodada, por personagem | 3,0% |
| por combate, na **mesa inteira** de quatro | **0,44** |
| um jogador vê o efeito **da arma dele** a cada | **9 combates = 2,3 missões** |

**Num server de personagem persistente, cada jogador encontra a identidade da própria arma uma vez por arco** — e carrega 13 entradas de tabela na cabeça para isso, o que dá **29 entradas por disparo**. *Um efeito preso a todo acerto dispararia 11× mais, e é por isso que as Masteries do 5e 2024 ficam no acerto e são limitadas por classe.*

**E a causa embaixo era pior:** na régua da v0.44, a arma que a ficção põe no teto de dado — `d8` numa mão, `d12` em duas — tinha **zero vagas de propriedade**. Ter identidade *era* descer o dado, e na mesa ninguém desce o dado. **O efeito de crítico tinha nascido para contornar isso por fora: resolvia o problema certo pelo lado que não dispara.**

Com o fundo `3/5` do §5.0 e a restrição do §5.0.4, **as propriedades carregam a identidade sozinhas** — 39 assinaturas para 41 armas, contra as 14 que o preço sozinho dava. *A Vanguarda poder fazer coisa parecida com o que o efeito faria fica para a peça dela, e o buraco de 6% a 9% da Rotina que ela deve continua registrado no §4.*

*O texto abaixo é o argumento de v0.44 e fica como registro do que foi medido, para ninguém reabrir a ideia daqui a dez versões achando que não houve conta.*

### 5.1.1-a O argumento de v0.44, arquivado

*Decidido na v0.44. É o eixo de identidade, e ele existe porque o eixo de preço sozinho não entrega o que o Mizuki pediu.*

Um efeito preso ao **20 natural** dispara em **3,0% das rodadas** — 5% de crítico × 60% de golpe simples. Isso muda a escala de tudo:

| um erro de 3 de dano num efeito custa | |
|---|---|
| se ele dispara em **todo acerto** | **3,00 pontos** |
| se ele fica **preso ao crítico** | **0,27 ponto** |

> **O portão do crítico divide o erro por onze.** Um efeito de crítico pode valer até **11,0 no disparo** — quase o dado inteiro da `Pesada`, que é 12,5 — e ainda custar menos de um passo de dado.

**É a mesma máquina das catorze *critical specializations* do PF2e**, e lá elas não são de graça na arma: são destravadas por característica de classe no nível 5. Aqui o destravador óbvio é a **Trilha da Vanguarda**.

**Por que treze, na categoria, e não cinquenta e dois, na arma.** Balanceamento não decide — calibrando a taxa de erro nas oito Masteries do 5e 2024, das quais quatro saíram fora da banda, o espalhamento do melhor ao pior efeito é `0,89` ponto com treze e `1,22` com cinquenta e dois. **A diferença é 0,33, que é um passo de dado — a menor unidade que este projeto tem.** As duas rotas são seguras.

Quem decide são os outros três eixos:

| | treze, na categoria | cinquenta e dois, na arma |
|---|---|---|
| nomes na triagem | 13 | 52 |
| missões até a mesa conhecer o conjunto | **23** | 133 |
| a Vanguarda tem o que especializar | **sim, a categoria** | não — não há família para amplificar |

**A escolha continua liberada, mas não pelo motivo que estava escrito aqui.** O argumento era que o eixo de preço entregava a unicidade sozinho — e o §5.0.2 mostra que não entrega: ele produz **14 assinaturas para as 41 armas de corpo a corpo**, com 85% delas em par.

> **É a categoria que separa.** Com ela entrando na conta, as assinaturas vão de **14 para 25** e o par cai de **85% para 61%**. O efeito de crítico não é o eixo secundário de identidade — sem ele, quase todo o catálogo é gêmeo mecânico.

**Os treze efeitos ainda não estão escritos.** Cada um precisa passar na triagem, valer no máximo 11,0 no disparo, e — a armadilha documentada do PF2e — **não morrer contra alvo comum**: lá o sangramento da `Faca` não faz nada contra morto-vivo, e o derrubar do `Martelo` não faz nada em quem já está no chão.

### 5.1.2 A régua que decide quem soma atributo — escrita na v0.47

*A tabela abaixo existia desde a v0.42 como lista. **Ela tem uma regra por baixo, e ela é do Mizuki:***

> **A arma que exige alguma coisa do corpo de quem a segura soma atributo. A arma em que você só precisa mirar, não.**

**Isso não muda linha nenhuma da tabela — ela já obedecia.** O que muda é que a lista deixa de ser lista: um arco pede que você o puxe, um kunai pede que você o arremesse, uma besta pede que você aperte o gatilho de uma corda que **já** está tensionada, e uma arma de fogo pede menos ainda. *A régua também diz o que fazer com a arma número 53, que a lista não dizia.*

| fonte do dano | quem | por quê |
|---|---|---|
| **Força** | todo corpo a corpo, e `Arremesso` | o golpe e o arremesso saem do corpo |
| **Destreza** | corpo a corpo com **`Fineza`**, e **`Yumi`** | precisão que o corpo executa — e o arco se puxa |
| **nenhuma — só o dado, e o dado é maior** | **`Balestra`** e **`Arma de Fogo`** | a energia já está armazenada. Você mira |

> **E ela cobrou o preço na hora de ser escrita.** As duas armas do `Yumi` **estouravam o orçamento** — ver o §8 item 16 —, porque a escada do tiro da v0.44 foi construída só para as que não somam nada e desconta `6,0` de atributo de todas. **Corrigido nesta versão**, no §5.3: `Daikyū` desceu para `1d10` e `Hankyū` para `1d8`. *A régua não criou o defeito; ela tornou impossível não vê-lo.*

| categoria | armas |
|---|---|
| **Lâmina Curta** (5) | Tanto · Punhal · Canivete · Faca · Sai |
| **Lâmina Longa** (8) | Machete · Wakizashi · Rapieira · Katana · Espada Longa · Espadão · Odachi · Nodachi |
| **Massa** (5) | Maça · Marreta · Kanabō · Maul · Taco |
| **Porrete** (5) | Bastão · Bō · Cassetete · Tonfa · Nunchaku |
| **Manopla** (2) | Soqueira · Tekko |
| **Machado** (3) | Machado · Machado de Guerra · Machadinha |
| **Ceifa** (3) | Foice · Kama · Kusarigama |
| **Armas Longas** (3) | Naginata · Yari · Lança |
| **Flexível** (3) | Corrente · Chicote · Manriki |
| **Arremesso** (4) | Kunai · Shuriken · Tessen · Chakram |
| **Yumi** (2) | Hankyū *(arco curto)* · Daikyū *(arco longo)* |
| **Balestra** (2) | Besta · Besta de Uma Mão |
| **Arma de Fogo** (7) | Pistola · Revólver · Submetralhadora · Espingarda · Rifle · Rifle de Precisão · Metralhadora Pesada |

**O nome japonês vem com a tradução entre parênteses**, decisão do Mizuki — quem não conhece o termo não pode ficar travado numa linha de tabela. *E `Yumi` (弓) deixou de ser arma e virou categoria: é a palavra genérica para arco, e o que existe de fato são o `Hankyū` (半弓) e o `Daikyū` (大弓).* A grafia foi conferida: faltava o `n` e o macron nos dois.

*Renomeados nesta passada:* `Machado de Bombeiro` → **Machado de Guerra**; `Marreta de Obra` → **Maul**.

## 5.2 As propriedades

*O §8 item 7 dizia que eram sete sem texto, e que enquanto fossem, 15 dos 16 pares da matriz sairiam `INCONCLUSIVO`.* **Três delas eram a mesma coisa com três nomes.**

`Alcance`, `Distância` e `Arremesso` descreviam todas a mesma pergunta — *a que distância essa arma alcança?* — e a resposta é um número, não uma redação. Colapsaram em duas, **`Alcance`** para o braço e **`Longo Alcance`** para o projétil, as duas com valor em metros. `Distância` e `Arremesso` saem da lista de propriedades; `Arremesso` continua vivo como **categoria**.

| propriedade | o que é |
|---|---|
| **`Alcance`** | número em metros no corpo a corpo. Padrão 1,5 m; as `Armas Longas` chegam a 3 m |
| **`Longo Alcance`** | número em metros para projétil e arremesso |
| **`Duas mãos`** | ocupa as duas. É a única que já era mensurável, via o escudo que ela impede |
| **`Fineza`** | troca Força por Destreza no acerto **e** no dano do corpo a corpo |
| **`Par`** | **role dois dados de dano e fique com o melhor** |

> **`Fineza` não é só da Rapieira.** *Direção do Mizuki:* ela vai para as armas focadas em agilidade — **a `Lâmina Curta` inteira, boa parte do `Arremesso`, e o que mais for lâmina pequena**. A lista fecha junto da classe das doze armas novas, porque as duas respondem à mesma pergunta: *o preço mora na classe ou na arma?*
| **`Oculta`** | **move de *não rola* para *rola* esconder a arma.** Zero número em combate |
| **`Versátil`** | **nas duas mãos, o dado sobe um passo** — d6→d8, d8→d10, d10→d12 |
| **`Munição`** | **recarregar custa a sua ação**, e dispara por dois gatilhos ao mesmo tempo |

### As quatro propriedades novas da v0.45

*Cada uma com âncora conferida no repositório, e cada nome passado na triagem.*

| propriedade | custa | o que é | de onde ela pendura |
|---|---|---|---|
| **`Rompe`** | 1 | vantagem contra objeto e estrutura | *"Força governa agarrar, **quebrar**"* — peça 5 §1 |
| **`Emaranha`** | 1 | dá acesso a agarrar sem largar a arma | *"Força governa **agarrar**"* — peça 5 §1 |
| **`Vestida`** | 1 | não ocupa a mão | o §4 mede a mão livre, e `Selo`=`Gesto` depende dela |
| **`Talha`** | 1 | a arma é ruim de bloquear: **−1 no `Bloquear` de quem se defende** | peça 23 §3 |

**A `Talha` bate no `Bloquear` e não na proteção, e isso foi escolha com motivo.** *Ideia do Mizuki: "uma propriedade que dificulta justamente no bloqueio."* A versão anterior dela ignorava `1` de proteção — e proteção esbarra no teto de Defesa, que é **derivado de três donos** e não aceita item mexendo nele. **O `Bloquear` é rota que o defensor escolhe golpe a golpe**, então a propriedade cria uma decisão em vez de um desconto.

> ***A dívida desta propriedade FOI PAGA na v0.143, e ela ficou aberta noventa e oito versões.*** *Ela nasceu na v0.45 com um bilhete ao lado, escrito para não sumir:* **enquanto o `Bloquear` fosse escolha da mesa, toda mesa que o deixasse desligado tinha uma `Talha` valendo zero — e a arma tinha pagado `1` ponto por ela.**
>
> *O bilhete está aqui em discurso indireto de propósito. A checagem 6 procura as frases de opcionalidade **por texto**, e um `grep` não distingue citação histórica de afirmação viva — então frase morta não volta entre aspas.*
>
> **O `Bloquear` virou a peça 23 e deixou de ser opcional.** *As **nove** armas que carregam a propriedade passam a receber o que compraram, em toda mesa:* `Rapieira` · `Odachi` · `Maça` · `Marreta` · `Kanabō` · `Machado de Guerra` · `Foice` · `Yari` · `Rifle`.
>
> **⚠ E o bilhete velho contava `sete`.** *São nove desde alguma versão que ninguém acompanhou, e o capítulo 13 do livro já publicava `nove`.* **Contagem escrita em frase não tem dono** — hoje a checagem 6 do `conferir-bloquear.py` conta as armas do catálogo e compara com o número escrito aqui.
>
> **E a checagem 7 deste validador não morreu junto com a dívida: ela mudou de pergunta.** *Ela nasceu perguntando "alguma arma depende só de uma regra que a mesa pode desligar?", e essa pergunta acabou.* **A que fica é a que sempre importou por baixo dela:** *uma arma cuja identidade paga inteira é `−1` num número alheio é uma arma sem identidade própria.* **A `Maça` e o `Kanabō` continuam declaradas**, por decisão do Mizuki na v0.48 — elas **são** as armas anti-guarda.
>
> **E o invariante do Bloquear continua inteiro.** Ele diz que *o modificador do defensor é o mesmo nos dois lados*; a `Talha` é do **atacante** e não toca em modificador nenhum do defensor.

**Duas morreram na triagem, e uma por sentido.** `Quebra` saiu `DENTRO` de **Quebra Coisa**, que é Melhoria — e ali a colisão não é de substring, é de sentido: uma Melhoria que quebra coisa faz exatamente o que a propriedade faria. Virou `Rompe`. E `Trava` saiu `OCUPADO`, o que matou a ideia de prender a lâmina do oponente com o Sai — que morreria no mérito de qualquer jeito, porque **`desarmar` tem zero ocorrências no projeto inteiro**, e um preço que usa termo inexistente é a lição nº 6.

### `Oculta` — ela é a camada 1 do §6, e não precisou de régua nova

*"Item abre a porta, treino atravessa bem."* Uma arma `Oculta` move quem a carrega de **não rola** para **rola** na hora de passar por revista, entrar armado onde não se entra, ou sacar sem ninguém ver começar. Ela **não soma maestria, não concede treino e não repete rolagem** — isso é o que o marco compra.

**Ela não produz número nenhum em combate**, e é por isso que ela cabe: os quatro eixos que o §6 fechou — proteção, cura, dado de dano e PE — continuam intocados, e o quinto, bônus em rolagem, é justamente o que ela não faz.

### `Versátil` — custa **zero**, e a conta demorou três versões para dizer isso

*Decisão do Mizuki: o efeito continua sendo **um degrau na escada** — `d6 → d8 · d8 → d10 · d10 → d12`, +1,0 de média em todos, `0,33` por rodada. **O que muda na v0.44 é o preço: ela deixa de custar 1 ponto e passa a custar 0.***

**Por que zero.** O passo só rende se você largar o escudo — ou a mão livre. E o escudo não é um valor, é uma curva:

| nv | o passo rende | o escudo vale | vale largar? |
|---|---|---|---|
| **2** | 1,0 | 0,9 | **sim, por 0,1** |
| 6 | 1,0 | 2,7 | não |
| 16 | 1,0 | 6,1 | não |
| 30 | 1,0 | 10,9 | não |

**E aumentar o passo não conserta:** com dois passos ainda só ganha no nv2; com três — `d6 → d12` — ganha até o nv6 e para. *`Versátil` é o buraco da arma de duas mãos em miniatura, e o §4 já tinha escrito a sentença: **proteção escala, dado não.***

**Baixar o dado também não conserta, e a dominância só troca de lado.** Com `Versátil` a 1 ponto o dado teria de ser d6 — e aí `Uma mão` d8 ganha em todos os níveis, com escudo (2,9 contra 1,9 no nv2; 12,9 contra 11,9 no nv30) **e sem escudo também**, porque na rota de mão livre as duas têm a mão livre e a `Uma mão` tem 1 ponto a mais de dado. **Não existe dado no meio.**

> **A saída veio de um argumento do Mizuki, e ele tem âncora no §4:** *"ter uma mão LIVRE é uma vantagem — permite usar feitiço, pegar item, interagir, coisa que você não pode fazer com espada e escudo, já que vai ter que SOLTAR em vez de guardar."*
>
> **E a versão dura disso já estava escrita:** quem tem **`Selo` = `Gesto`** e pega um escudo **desliga a técnica inteira**. Para essa gente o escudo nunca esteve no menu, e a mão livre é obrigatória, não preferida.

**Com o preço em zero, tudo fecha:**

```
Versátil d8 = 2,0 de dado + 0 de propriedade = 2 de 2
Uma mão  d8 = 2,0 de dado + 0                = 2 de 2
```

**As duas viram a mesma arma, e a `Versátil` leva um texto a mais.** É a gêmea de graça que a v0.41 já tinha aprovado — *"não tem problema ter arma idêntica, tem vezes que a pessoa só quer um flavor diferente."*

> **E a dominância aberta desde a v0.41 fecha com tamanho.** O §5 registrava *"não existe caso em que a `Uma mão` seja melhor"* sem conseguir dizer de quanto era, e por isso ela ficou como `ACEITA` esperando forma. **A vantagem da `Versátil` sobre a `Uma mão` é 0,1 ponto, e só no nível 2.** *Uma dominância sem tamanho fica aberta para sempre; com tamanho, ela fecha.*

### `Munição` — dois gatilhos, e o teto não é o pente de verdade

*Decisão do Mizuki: os dois juntos.*

> **Recarregar é Ação Bônus.** Você recarrega quando tirar **1 ou 2 natural** no ataque, **ou** depois de **X ataques**, o que vier primeiro. O X é da arma.

> **Esta seção dizia as duas coisas ao mesmo tempo até a v0.44.** Ela abria com *"recarregar custa a sua ação"* e fechava com *"recarregar é Ação Bônus — decisão do Mizuki"*, **e a tabela de `54% / 46% / 14%` que ficava entre as duas tinha sido calculada com a primeira.** A decisão é a Ação Bônus; a tabela era da regra que ela substituiu, e saiu.

**O X não é a capacidade real, e o modelo velho errava num segundo ponto.** Ele supunha **2,2 ataques por combate** — um golpe simples por rodada. Mas a peça 6 §3.1 dá **ataque extra ao Bastião e à Vanguarda no nível 7**, e *"ataque extra é sempre golpe simples"*, que é exatamente o que a arma de tiro faz. Refeito com dois golpes por rodada:

| X | fração dos ataques que sai, **sem** ataque extra | **com** ataque extra |
|---|---|---|
| **1** | 100% | **64%** |
| 2 | 100% | 97% |
| 3 | 100% | 99% |
| 4 ou mais | 100% | 99% |

> **O `X = 1` apaga o ataque extra, e esse é o achado.** Com dois golpes por rodada você precisa de **duas recargas** e só tem **uma Ação Bônus** — então a recarga não atrasa o tiro, ela come o benefício de nível 7 de dois Caminhos inteiros. *Achado pelo Mizuki, olhando a faixa e dizendo que ela estava baixa demais.*

**E de 2 para cima a `Munição` custa entre 1 e 3 pontos percentuais.** Ela é **textura, não preço** — o que quer dizer que ela nunca poderia ter sido contada como contrapeso do dado, e a versão velha do §5.2 contava.

**O que o X decide, então, é ritmo:** de quanto em quanto tempo a arma força uma recarga.

| X | recargas num combate de 3,7 rodadas, **sem** extra | **com** extra | passa o combate sem recarregar |
|---|---|---|---|
| **2** | 1,8 | 3,8 | **0%** |
| **3** | 1,1 | 2,4 | **0%** |
| 4 | 0,8 | 1,9 | **22%** |
| 5 | 0,4 | 1,5 | **68%** |
| 6 | 0,4 | 1,3 | 68% |

**O critério do Mizuki é que nenhuma arma atravesse a briga sem recarregar**, e ele fecha em `2` e em `3` — só. De 4 em diante o teto solta, e em 5 ele já é indistinguível de não ter teto nenhum, porque o gatilho do dado natural assume sozinho. *A versão velha desta seção chamava o "4 ou mais" de enfeite: certa na conclusão, errada no número. A faixa útil acaba em **3**, e `—` sai da lista.*

### O X de cada arma

*Decisão do Mizuki, por ficção: **"pistola e revólver têm menos balas que rifle e submetralhadora, mas não menos que espingarda e rifle de precisão, que seriam as de maior dano."*** A faixa é `2 · 3 · 4`.

| X | armas | |
|---|---|---|
| **4** | Metralhadora Pesada | a única, por decisão |
| **3** | Rifle · Submetralhadora | as que sustentam o tiro |
| **2** | Pistola · Revólver · Espingarda · Rifle de Precisão · Besta · Besta de Uma Mão | |

> **A ordenação dele corta atravessado nos degraus de dado — Rifle e Espingarda são os dois `2d8` e levam X diferente.** Isso é a régua do §5 funcionando: com a classe fora do preço, o X mora na arma. **A régua velha não conseguiria escrever essa linha.**

**E o `X = 4` da Metralhadora Pesada foi conferido separado, porque ele é o único que fura o critério.** Ele deixa **22% dos combates** passarem sem recarga — mas só para quem **não tem ataque extra**:

| portador | vaza | janela |
|---|---|---|
| Vanguarda ou Bastião, **nv6+** | **0%** | nenhuma |
| Vanguarda ou Bastião, nv2–5 | 22% | quatro níveis |
| Guia · Evocador · Emanador | 22% | a campanha inteira |

**Uma metralhadora de cinta é arma de Vanguarda, e a Vanguarda ganha ataque extra no nv7 — praticamente onde o vazamento fecha.** *O nível era 6 até a v0.61, e a Q3 de Trilhas o moveu um degrau para cima; o vazamento continua sendo de 0,1 a 0,3 ponto e agora vaza um nível a mais.* E o que vaza custa **0,1 a 0,3 ponto**, porque recarregar em Ação Bônus já era quase de graça. **É textura, não balanço: registra-se em vez de consertar.** *Escrever exceção para 0,3 ponto é medir contagem em vez de peso, que é a lição nº 3.*

*As duas Bestas ficam em `2` por falta de lugar melhor: a ficção pediria `1` — uma besta carrega um virote —, e o `1` está proibido por apagar o ataque extra. **Fica marcado**, porque é o único ponto do catálogo em que a ficção e a régua discordam de frente.*

*Isso é o modo de falha que o levantamento externo descreve com todas as letras — **"um número que sobe e desce e nunca chega a zero, e nada de interessante sai dele"** —, e é por isso que ele é abstraído em vez de contado.* O gatilho do dado natural existe para o susto; o teto existe para o ritmo.

**Recarregar é Ação Bônus** — decisão do Mizuki. E isso tem uma consequência que precisa estar escrita: **em Ação Bônus a `Munição` custa zero.** A peça 3 §2 chama a Ação Bônus de *"a peça mais herdada do turno"*, e o §4 desta peça mediu o slot como vazio. Você recarrega gastando o que não estava usando.

> **Ela deixa de ser preço e vira textura, e isso muda no dia em que o slot encher.** O `ESTADO-ATUAL` já promete que a peça de Caminhos dá ao Bastião **socar como Ação Bônus**. Quando aquela peça sair, a `Munição` passa a cobrar de verdade — e o preço da arma de fogo sobe sozinho, sem ninguém mexer em número. É a mesma forma do escudo em Ação Bônus, medida no §4.

### O dado do tiro — 2d10 no topo, escada de dois dados

*Decisão do Mizuki na v0.44. **Era `3d10` no topo**, e o orçamento do §5.0 derrubou: aquele dado gastava 9,0 num orçamento de 4.*

| arma | dado | média | gasto | orçamento | sobra |
|---|---|---|---|---|---|
| Metralhadora Pesada · Rifle de Precisão | **2d10** | 11,0 | 3,5 | 4 | **0,5** |
| Rifle · Espingarda · Besta | 2d8 | 9,0 | 1,5 | 4 | 2,5 |
| Submetralhadora | 2d6 | 7,0 | 1,0 | 4 | 3,0 |
| Pistola · Revólver · Besta de Uma Mão | 1d10 | 5,5 | 1,0 | 2 | 1,0 |

**A fórmula, e ela é a mesma do §5.0 com um termo a mais.** O corpo a corpo soma Força e o orçamento não cobra por isso; a arma de tiro não soma nada. Então o dado dela se precifica descontando as duas coisas que o orçamento já dá de graça ao vizinho:

```
gasto do dado = média da arma − 2,5 (o piso, que é o d4) − 6,0 (a Força que o corpo a corpo soma)
                e nunca abaixo de zero
```

*Contra-teste, contra as duas classes de duas mãos já publicadas:* a `Pesada` (d12 + Força 6 = 12,5) sai **4,0 de 4**, e a `Haste` (d10 + Força 6, mais `Alcance`) sai **4,0 de 4**. **As duas fecham exatas**, o que prova que a fórmula do tiro é a mesma do corpo a corpo e não uma régua paralela.

**O topo fica um ponto abaixo da `Pesada` porque ele paga o `Longo Alcance`** — 11,0 contra 12,5. A distância deixa de ser de graça, que era o que o §5.2 dizia que ela era.

> **E o argumento antigo continua morto, pelo motivo certo.** Ele era *"não soma mod E tem munição, duas penalidades"*, e a v0.42 matou por dupla contagem — **corretamente**: o `16,5` já *é* o total sem atributo, e o dado grande é o que compensa. O que a v0.42 não viu é que **não somar atributo não é penalidade nenhuma: é independência de atributo**, e independência é o que torna a arma boa justamente para quem não investiu. Medido contra Força 0, o `3d10` estourava em **11 pontos ≈ 11% da Rotina** — mais do que os 6% a 9% que a Trilha da Vanguarda inteira deve. *Lição nº 7: um preço se mede somado, e aqui faltava somar quem segura a arma.*

> **As duas metades do argumento velho, e o que aconteceu com cada uma.** Ele era: *"ela não soma mod E tem munição, então tem duas penalidades."*
>
> A **`Munição`** vale zero, e a v0.44 mediu o quanto: recarregando em Ação Bônus com X ≥ 2, saem 97% a 99% dos ataques.
>
> O **`sem mod`** a v0.42 matou por dupla contagem, e estava certa — mas a v0.44 achou que ele é pior que neutro. *Ver o parágrafo acima: não é penalidade, é independência de atributo.*
>
> *E o que fica de pé daquela versão:* Força 6 e Destreza 6 custam **3 pontos cada**, os dois saindo do 3 da criação, e as duas carregam `Duas mãos`, então as duas largam o escudo. **O que a arma de fogo ganhava de graça era a distância — e agora ela paga por ela**, com o ponto de `Longo Alcance` que põe o topo em 11,0 contra os 12,5 da `Pesada`.

### `Uma mão` × `Versátil` — o argumento de v0.41, arquivado

> **Isto era uma comparação entre duas CLASSES, e as classes morreram como preço na v0.44.** Fica pelo motivo de sempre — para ninguém reabrir daqui a dez versões achando que não houve conta. *A pergunta que ele responde continua viva; o que mudou é a camada em que ela se responde, e a resposta nova está na matriz refeita, mais abaixo.*

*A dominância é fraca: com escudo empatam em 1,49; sem escudo a `Versátil` faz 1,82. Não existe caso em que a `Uma mão` seja melhor.*

> **Decisão do Mizuki: fica.** *"Vai ter vezes que vamos querer uma mão livre, por exemplo para pegar itens — e a `Uma mão` pode vir a ser usada em empunhadura dupla, uma mecânica que podemos trabalhar depois."*

**As duas razões são reais e nenhuma das duas tem número hoje**, e é honesto dizer isso: nada no sistema hoje cobra por ter as mãos ocupadas fora do escudo, e a empunhadura dupla não existe. **É valor a prazo** — a classe está reservada para uma mecânica que vem, não paga uma que já está aqui.

*O que sobrevive disto para o catálogo de hoje:* **a empunhadura dupla continua sem existir**, e ela é a única coisa que daria à mão livre um número próprio. Enquanto não existir, `Versátil` fica de graça e as três dominâncias que ela produz ficam `ACEITA`.

### `Par` — a conta fechou em cima do alvo

*O par medido era `Curta` contra `Uma mão`, que eram classes. **Refeito sobre arma na v0.47, e o resultado não se move** — o que era comparação entre pacotes virou comparação entre duas linhas do §5.3.*

A **Kama** (`d6`, `Par`·`Rompe`) contra o **Machete** (`d8`, `Rompe`). As duas de uma mão, as duas fechando em `3/3`: a Kama troca **um passo de dado** por `Par`, e nada mais muda entre elas. Então **`Par` precisa valer exatamente um passo, ou a Kama está dominada**:

| | valor |
|---|---|
| alvo — o passo `d6` contra `d8` | **0,33** por rodada |
| `Par` entrega, no `d6` | **0,32** |

Melhor de dois no `d6` dá 4,47 de média contra 3,50. **Erra por um centésimo, e não inventa mecânica**: é a mesma vantagem que a peça 11 já precifica e que a peça 4 §5 já garante que não empilha. E, principalmente, **não é ataque extra** — a trava da peça 6 §3 continua inteira, que é o que impede duas armas de virarem dois golpes.

*E a matriz confirma pelo lado de fora: a Kama não aparece entre as três dominadas.* **A régua que precificou `Par` em cima de classes continua certa quando medida em cima de armas** — que é o contra-teste que ninguém tinha rodado.

### As colisões aceitas, e por que cada uma fica

*Decisão do Mizuki: as três ficam.* **Aceita registrada é diferente de colisão não vista**, e a diferença é o registro.

| nome | colide com | por que fica |
|---|---|---|
| `Oculta` · `Versátil` | são **classe e propriedade** ao mesmo tempo | a classe se chama pela propriedade que a define. *"É intuitivo, e por costume ninguém confunde"* |
| `Pesada` | é classe de arma **e** o tier mais caro de Restrição | mesmo motivo, e a colisão já existia sem ninguém ter visto |
| `Alcance` · `Longo Alcance` | `Alcance` é Família e Melhoria no manual | colisão de camada: no manual descrevem o que um *feitiço* faz, aqui o que um *objeto* é |
| `Chicote` | é **feitiço pronto** no manual, nome inteiro | *"não tem problema ter comparação com o feitiço lá"* |

> **E o `ARMA DE FOGO` virou régua, não exceção.** O critério do Mizuki: *"fogo é uma palavra única, mas arma de fogo é um conjunto de palavras — mesmo que colida, não tem tanto problema."* Isso é um grau novo ao lado de `OCUPADO`, `DENTRO` e `fraco`: **um nome composto que contém termo ocupado não herda a colisão**, porque *Arma de Fogo* não é o Tema `Fogo`. Vale para categoria e para arma, e entra no `conferir-nomes.py`.

> **A triagem tem um quarto ponto cego, e ele apareceu aqui.** `Leve`, `Média` e `Pesada` são os **tiers de Restrição** — `Leve = teto(Classe/2)`, `Média = Classe`, Pesada é o mais caro —, e os três saem `LIVRE` porque a triagem compara contra as listas de Família, Forma, Melhoria e Tema, e **tier de magnitude não está em lista nenhuma**. A classe de arma `Pesada` colide com o tier `Pesada` desde que as duas existem. Fica aceita, e o ponto cego fica registrado.

### A matriz por valor total — refeita na v0.47, sobre arma e não sobre classe

*Esta subseção rodava sobre as **oito classes**, e a classe morreu como preço na v0.44. Ela sobreviveu três versões dizendo que o validador não podia ser escrito, por um motivo que já não existia. **O texto velho está arquivado no fim desta seção**; o que segue é a matriz sobre o catálogo real.*

**Ela roda agora, e roda inteira:** 41 armas de corpo a corpo, **1640 pares ordenados**, com o critério certo — *mesma mão, dado maior ou igual, propriedades em superconjunto, restrições em subconjunto, e algo estrito.*

| | |
|---|---|
| pares avaliados | **1640** |
| pares em que uma arma é estritamente melhor | **3** |
| propriedades em uso **sem texto de regra** | **zero — as doze têm** |

### As três dominâncias são a mesma, e ela já tinha nome

| a arma melhor | a arma pior | a diferença |
|---|---|---|
| Espada Longa (`d8`, `Versátil`·`Rompe`) | **Machete** (`d8`, `Rompe`) | `Versátil` |
| Espada Longa | **Machado** (`d8`, `Rompe`) | `Versátil` |
| Taco (`d8`, `Versátil`·`Oculta`) | **Wakizashi** (`d8`, `Oculta`) | `Versátil` |

**As três são `Versátil` a custo zero**, e é a dominância que a v0.41 achou entre classes e a v0.44 fechou **na camada da classe**, dizendo que `Versátil` e `Uma mão` *"viram a mesma arma, e a `Versátil` leva um texto a mais"*. **O que ninguém conferiu é que ela desce para a camada da arma**: uma arma que carrega `Versátil` é estritamente melhor que a arma idêntica que não carrega, porque o passo é de graça.

> **O tamanho é o mesmo que a v0.44 mediu: `0,1` ponto, e só no nível 2.** Do nv6 em diante o passo rende 1,0 contra os 2,7 do escudo, então **ninguém larga o escudo e as duas armas passam a ser idênticas na mesa.** Uma dominância que vale um décimo de ponto num único nível é gêmea com texto a mais, que é o que o Mizuki aprovou na v0.41: *"não tem problema ter arma idêntica, tem vezes que a pessoa só quer um flavor diferente."*
>
> **Mas o tamanho não é o achado, e chamar isso de "três exceções aceitas" seria contar sintoma.** `Versátil` a custo zero não é *barata*: ela é **não precificada**. Das 28 armas de uma mão, **4 levam e 24 recusam** — e **17 das que recusam têm o mesmo dado de uma que leva**, então o orçamento não impede nenhuma delas de pegar. **Quem impede é a ficção**, e só ela. Isso está no §8 item 17, porque é pergunta de desenho e não conta.
>
> **O que muda é o registro.** O §5.3 diz *"nenhuma arma tem dado maior **e** mais propriedade que outra da mesma mão"* — verdade literal, e ela não cobre o caso de **dado igual e mais propriedade**, que é onde as três moram. *A frase estava certa e media o eixo ao lado.*

### O requisito de Força não é custo, e isso continua valendo

Nenhuma arma do catálogo pede mais que **Força 3**, e 3 é o teto da criação (peça 2 §2). **Quem investe Força paga zero por qualquer arma**, então o requisito resolve **acesso** e não preço — que é o que a peça 5 §1 já tinha concluído e o que o §5.5 implementou. *O único item do catálogo inteiro que cobra ponto de marco continua sendo o escudo degrau 3, que pede Força 5.*

### O que sobra para o validador, agora que ele pode existir

*O bloqueio caiu junto com a matriz velha.* As checagens que esta subseção deixa prontas:

1. **A matriz de dominância roda sobre arma, não sobre classe** — 1640 pares, e o resultado esperado é **exatamente as três da `Versátil`**, nomeadas como `ACEITA`. Qualquer quarta é falha.
2. **Toda propriedade em uso tem texto** — hoje doze de doze. Uma propriedade nova sem texto quebra a matriz em silêncio, que é como esta seção envelheceu.
3. **A dominância roda uma vez por rota de proteção, e são DUAS** (cobrir-se · uniforme), pelo motivo do §8 item 1: rodada uma vez só, ela cancela populações opostas e sai verde.

   > **⚠ Eram três até a v0.118, e a terceira era `sem energia nenhuma`** — a Restrição Celestial pelo ramo da Maki, *"que não tem cobrir-se para desligar"*. **Ela deixou de existir como rota separada quando aquela Origem ganhou a `cobrir-se` portada**, na peça 11 §6.8: a proteção dela é `1/3 da Lapidação + 1`, a mesma função na mesma faixa `1`–`10`. *A rota colapsou na primeira, e o teto de Defesa não se moveu — porque é a mesma conta com outro nome de recurso.*

#### A matriz de classes, arquivada

*Este é o texto que morava aqui até a v0.47. Ele mediu o que dava para medir com a régua da época, e três das quatro afirmações dele já eram falsas quando foram lidas pela última vez — mas a conta que ele registra foi feita, e é por isso que ele fica.*

> *A primeira passada disse "zero classes dominadas". Ela media dado e propriedade; medindo o **total**, com o requisito de Força entrando como custo, aparecem duas coisas.*
>
> **A primeira: o requisito de Força não é custo nenhum.** Nenhuma classe pede mais que 3, e 3 é o teto da criação. *— continua verdade, e virou o §5.5.*
>
> **A segunda: `Uma mão` está dominada pela `Versátil`.** *— continua verdade, mas na camada da arma, e a v0.44 já a tinha dimensionado em 0,1 ponto.*
>
> **Sete das oito propriedades não têm texto nenhum.** *— falso desde a v0.45: são doze propriedades, todas com texto.*
>
> | pares suspeitos | veredito |
> |---|---|
> | 1 (`Uma mão` × `Versátil`) | **DOMINADA** |
> | 15 | `INCONCLUSIVO` |
>
> `Haste` e `Tiro pesado` perdem 0,60 por rodada para a `Pesada`. *— as três são classes, e classe não é mais preço. E o `0,60` já tinha sido corrigido para `0,33` na v0.42, no §8 item 7 deste mesmo documento, sem que esta linha soubesse.*
>
> **O item 9 do §8 não pode ser escrito antes disto.** *— **este era o bloqueio, e ele caiu na v0.44 sem ninguém desfazer o nó.** Três versões do rascunho carregaram a frase que dizia que o validador da peça era impossível, quando o motivo dela já tinha sido substituído. É a lição nº 9 na forma mais cara que ela tem: não uma cópia que diverge, mas uma **conclusão que sobrevive à premissa.***

### A régua que separa arma de Caminho

> **A arma dá acesso e restrição. O Caminho dá o que você faz com ela.**

O `ESTADO-ATUAL` diz que a árvore da Vanguarda é *"o que se faz com a arma: alcance, reposicionamento forçado, troca de alvo, exceção na economia de ação"*. **Nenhuma propriedade de arma concede manobra, reposicionamento nem exceção de ação** — senão a peça 4 da fila nasce sem ter o que dar. A naginata *tem* alcance (fato do objeto); a Vanguarda *estende* o alcance (ação).

### `Precisa` foi rejeitada na v0.41 e voltou como `Fineza` na v0.42 — e um dos dois argumentos caiu

*Reversão de decisão escrita, registrada aqui inteira para ninguém reabrir daqui a dez versões achando que não houve conta.*

**O argumento que caiu:** *"`Precisa` tira o primeiro trabalho da Força, que tem uma perícia só."* Ele era verdade quando foi escrito. **Depois desta peça, Força compra** o requisito de arma, o Traje degrau 3, o Revestimento 1/2/3, o escudo degrau 2 e 3, mais agarrar, quebrar e carga. O *segundo trabalho* que a peça 1 §9 pede desde a v0.24 **existe agora**, e não existia na v0.41.

**O argumento que ficou de pé, e agora tem número:** *"a diferença de dado inteira vale menos que a Defesa sozinha."*

| ficha | dano | por rodada | Defesa |
|---|---|---|---|
| Força 6 · Pesada + Revestimento 3 + escudo 3 | 12,5 | 4,12 | 19 |
| Destreza 6 · Lâmina Longa com `Fineza` + cobrir-se | 10,5 | 3,47 | **19** |

**As duas chegam a Defesa 19 por rotas diferentes, e o dano fica a `0,66` por rodada — 2% da Rotina.** Com equipamento no prato da Força, deixa de ser dominância e vira escolha de sabor. *O contrapeso não existia quando a decisão foi tomada; ele saiu desta mesma peça.*

> **Esta linha dizia `1,32 por rodada — 4% da Rotina`, e era o dobro. Corrigido na v0.44.** As duas colunas da tabela acima já traziam a resposta: `4,12 − 3,47 = 0,65`. O `1,32` sai de multiplicar a diferença de 2,0 de dano por **`0,66`** em vez de por **`0,33`** — e `0,66` é o número da linha vizinha desta mesma peça, *"a arma de duas mãos rende 0,66 por rodada"*.
>
> **A conclusão sobrevive e fica mais forte:** se 4% já tinha sido aceito como sabor, 2% é sabor com folga, e nada rebalanceia. *Mas é o quarto exemplar do defeito que a v0.43 pagou para aprender — **a prosa contradizendo a tabela do próprio documento** —, e o único jeito de pegar foi refazer a divisão.*

**O nome mudou duas vezes.** `Precisa` sai `fraco` na triagem — a uma letra de **Precisão**, que é Melhoria do manual. `Finez` foi a primeira escolha do Mizuki e ele mesmo trocou: **`Fineza`**, que é a palavra em português e sai `LIVRE`.

*O texto abaixo é o argumento original de v0.41, e fica porque a metade dele continua valendo:*

### O argumento de v0.41 contra Destreza no corpo a corpo

A peça 5 §1 já mediu: `+1` de Destreza evita 2 a 7 de dano num combate de três rodadas, e um dado maior rende `+2` por golpe. Mesmo com o menor dado do catálogo, a ficha de Destreza faria 5,5 de dano contra 8,5 da arma pesada — perde 3 e ganha Defesa, iniciativa e quatro perícias. **A diferença de dado inteira vale menos que a Defesa sozinha.**

E o agravante: a peça 1 §9 tem aberto *"se Força precisa de um segundo trabalho, ela tem uma perícia só"*. `Precisa` **tira o primeiro trabalho da Força** e piora a pergunta. Corpo a corpo é Força, ponto.

### Nomes que morreram na triagem

*A primeira passada matou sete. **Quatro voltaram na v0.40**, quando o critério de triagem foi corrigido — a tabela abaixo já está com a revisão.*

| nome | veredito | por quê |
|---|---|---|
| `Chicote` | **morto** | é feitiço pronto no manual, com o nome inteiro. E um chicote de energia **é** um chicote — colide de frente |
| `Guarda` | **morto** | é **Melhoria** no manual, nome inteiro |
| `Proteção` | **morto** | é o **termo da fórmula da Defesa**. Batizar a categoria com o nome do valor que ela produz é "uma coisa por nome", literal |
| `Carapaça` | **morto** | colide em sentido com a **Escama** e com a **Casca** que morreu |
| `Lança` | **volta** | estava só *dentro* de **Lança Negra**. Aquilo é um feitiço, não uma haste com ponta |
| `Escudo` | **volta** | estava só *dentro* de **Rasga Escudo**. Uma Melhoria que rasga escudos não **é** um escudo |
| `Faca` | **volta** | fica a uma letra de **Fica** (Melhoria), o que é aviso e não bloqueio |
| `Lastro` | **volta** | mesmo caso, contra **Rastro** |

### O critério que a triagem estava aplicando errado

*Corrigido na v0.40, e o conserto foi na ferramenta.*

> **Decisão do Mizuki:** *"não precisa ligar tanto para nomes conjuntos, como Melhoria 'rasga escudo' a 'lança negra'. Se preocupe mais quando o nome bater de frente com o nome de algo que é **realmente** aquilo."*

A triagem juntava três coisas diferentes numa palavra só. Agora ela separa:

| grau | o que significa | mata? |
|---|---|---|
| `OCUPADO` | o **nome inteiro** já é termo definido | sim |
| `DENTRO` | o nome aparece **dentro de um termo composto** | **não** — vá ler o termo e pergunte se ele *é* aquilo |
| `fraco` | fica a uma letra de um termo | não, mas confunde em voz alta |
| `LIVRE` | ninguém usa | — |

**O custo de errar isso é medível, e ele já tinha cobrado:** a `Lança` morreu por substring, e a arma entrou na classe Haste como **Yari** — que é exatamente uma lança, com o nome em japonês. O sistema contornou um nome que nunca esteve ocupado.

*Três contra-testes na mudança:* `Escudo` e `Lança` passaram de `OCUPADO` para `DENTRO`; `Anteparo`, `Bloqueio` e `Chicote` continuaram `OCUPADO`, porque são nome inteiro; e `Toque`, que é Forma no manual **e** aparece em composto, continua `OCUPADO` — o grau duro tem prioridade. Perturbando a linha que classifica, `Escudo` cai para `LIVRE`, o que prova que é ela que decide.

*Controle da triagem:* `Marca`, `Passo` e `Salto` foram passados de propósito e voltaram `OCUPADO` os três — prova de que a triagem estava mesmo rodando naquela passada.

### Duas propriedades em uso saem OCUPADO, e ninguém tinha passado elas

Rodando a triagem contra os oito nomes de propriedade da tabela acima:

| nome | resultado |
|---|---|
| `Par` · `Arremesso` · `Munição` · `Versátil` · `Oculta` | `LIVRE` |
| **`Alcance`** | `OCUPADO` — é **Família** e **Melhoria** no manual, com catorze ocorrências |
| **`Distância`** | `OCUPADO` — é **Tema** no manual |

As duas estão escritas na tabela de classes e não aparecem na lista de nomes mortos acima. **É colisão de sentido junto com a de substring, e nas duas o significado herdado briga com o novo:** a Melhoria `Alcance` estica o alcance de um *feitiço*, e a propriedade `Alcance` descreve o quanto uma naginata chega longe. Um mestre lendo os dois na mesma mesa mistura.

*A metade `Alcance Impossível` da colisão morreu com aquele Legado na v0.39. A metade do manual não morreu, e é a que pesa.*

> **Decisão do Mizuki: os dois ficam.** O motivo é o mesmo que a peça 6 usou para os rótulos de rascunho — **a colisão é de camada, não de sentido**. `Alcance` e `Distância` no manual descrevem o que um *feitiço* faz; na tabela de armas descrevem o que um *objeto* é. Nenhuma regra pendura efeito nos dois ao mesmo tempo, e trocar por sinônimo pior custaria mais clareza do que a colisão custa.
>
> **O que isso obriga:** as duas entram no validador desta peça como `ACEITA`, com o motivo escrito — no mesmo formato que os rótulos de rascunho da peça 6 e o aviso de cabeçalho do `arquitetura.md` já usam. Aceita registrada é diferente de colisão não vista, e a diferença é justamente o registro.


### 5.2.1 Alcance — as duas faixas, e a desvantagem por posição

*Escrita na v0.74, e ela paga uma dívida que estava escondida à vista.* **O §5.2 declara `Longo Alcance` como *"número em metros para projétil e arremesso"* — e nenhuma das onze armas de tiro tem metro escrito.** Pior: a propriedade **já custa 1 ponto** no orçamento, porque *"o topo fica um ponto abaixo da `Pesada` porque ele paga o `Longo Alcance`"*. **O catálogo inteiro pagou por uma regra que ninguém tinha escrito.**

> **Toda arma de projétil tem duas faixas.**
> **Faixa normal** — até o `Longo Alcance` da arma. Ataque normal.
> **Faixa longa** — até o número da direita na tabela do §5.2.2. **Desvantagem no ataque.**
> **Além da faixa longa, você não alcança.**
>
> **E existe uma terceira, do outro lado: `colado`.** Atacar com arma de projétil **estando adjacente a um inimigo** — qualquer inimigo, não só o alvo — é **desvantagem**, do mesmo jeito.

**As duas pontas são a mesma regra e o mesmo tamanho.** Desvantagem vale `−25` pontos percentuais contra alvo difícil, que é **metade do dano** — o número é da peça 11, e as peças 13 e 14 já o usavam. *Uma régua, dois lados: perto demais e longe demais custam igual.*

**O formato é o do hobby de propósito**, e o motivo é o filtro multi-mestre: *dois mestres que vieram de outro sistema chegam ao mesmo lugar sem ler nada.* É a mesma decisão que a lista de ações tomou ao seguir o padrão para a ação padrão.

> ~~**O que esta seção NÃO fecha: os metros de cada arma.**~~ **Fechados na v0.94, e estão no §5.2.2 logo abaixo.** *E eram **dezenove** armas e não as onze que esta nota contava — as oito de `Arremesso` também carregam `Longo Alcance`, e a própria declaração da propriedade diz "para projétil **e arremesso**".* **A contagem da dívida tinha lido só metade da frase que ela mesma citava.**
>
> **E a regra já tem três consumidores esperando por ela**, todos na Trilha `Batedor`: o `Yumi` ignora a desvantagem da faixa longa, a `Arma de Fogo` ignora a de estar colado, e a `Besta` não ignora nenhuma das duas — ela **empurra** o inimigo para fora do problema. *Três portas para a mesma pergunta de posição, que é o que faz as três serem escolhas diferentes em vez de três versões da mesma.*

### 5.2.2 Os metros de cada arma — importados do d20, e a fonte está declarada

*Decisão do Mizuki na v0.94: **seguir o d20 e converter, em vez de derivar número novo.*** **A conversão do projeto é `5 pés = 1,5 m`**, que é a mesma que põe o deslocamento padrão em `9 m`.

**O motivo de importar em vez de calcular é honesto e vale escrever: alcance de arma não tem preço neste sistema.** *A propriedade `Longo Alcance` custa `1` ponto para toda arma que a tem, e ela custa esse ponto por existir — não por quanto.* **Então o número não sai de conta nenhuma daqui; ele só precisa ser plausível, consistente entre as armas e igual em sete mesas.** *Uma tabela publicada e conhecida faz as três coisas de graça.*

**As onze de tiro:**

| arma | a que ela corresponde | faixa normal | faixa longa |
|---|---|---|---|
| **Hankyū** | arco curto — `80/320 pés` | **24 m** | 96 m |
| **Daikyū** | arco longo — `150/600 pés` | **45 m** | 180 m |
| **Besta de Uma Mão** | besta de mão — `30/120 pés` | **9 m** | 36 m |
| **Besta** | besta pesada — `100/400 pés` | **30 m** | 120 m |
| **Pistola** | pistola — `30/90 pés` | **9 m** | 27 m |
| **Revólver** | revólver — `40/120 pés` | **12 m** | 36 m |
| **Submetralhadora** | pistola automática — `50/150 pés` | **15 m** | 45 m |
| **Espingarda** | espingarda — `30/90 pés` | **9 m** | 27 m |
| **Rifle** | rifle automático — `80/240 pés` | **24 m** | 72 m |
| **Rifle de Precisão** | rifle de caça — `80/240 pés` | **24 m** | 72 m |
| **Metralhadora Pesada** | rifle automático — `80/240 pés` | **24 m** | 72 m |

**As oito de arremesso, todas na mesma faixa:**

| arma | faixa normal | faixa longa |
|---|---|---|
| **Punhal · Machadinha · Lança · Kunai · Shuriken · Tessen · Chakram · Kusarigama** | **6 m** | 18 m |

*A fonte dá `20/60 pés` para punhal, machadinha, martelo leve, lança, tridente e dardo — praticamente todo arremesso de mão.* **Uma faixa só para as oito, em vez de oito números que ninguém consegue lembrar na mesa.**

> **⚠ A faixa longa deixou de ser o dobro, e isso é mudança de regra.** *O §5.2.1 dizia "até o dobro disso" desde a v0.74 — e aquilo era régua provisória, escrita quando não havia catálogo nenhum para olhar.* **A fonte usa `4×` para arco e besta e `3×` para arma de fogo e arremesso**, e importar os números sem importar a proporção seria trazer metade da tabela. *Nada foi reprecificado: desvantagem continua valendo os mesmos `−25` pontos percentuais, e o `Longo Alcance` continua custando `1` ponto.*

> **Três armas empatam em `24 m` e o empate é da fonte, não descuido.** *O `Rifle`, o `Rifle de Precisão` e a `Metralhadora Pesada` correspondem todos a rifle de cano longo, e lá o rifle de caça e o automático têm o mesmo alcance e dados diferentes.* **O `Rifle de Precisão` se separa pelo dado — `2d10` contra `2d8` — e não pela distância.** *Se algum dia ele precisar alcançar mais que os outros dois, esse número vai ter de sair de fora da fonte, e aí ele vira decisão de design em vez de importação.*

> **A `Kusarigama` é a única sem correspondente**, porque uma foice presa a uma corrente não é arremesso solto. *Ela ficou com a faixa da família, e a ficção da corrente sugere menos.* **Fica declarado para quem reler não procurar defeito onde houve escolha.**

## 5.3 As 52 armas — dado e propriedades

*Fechado na v0.45.* **O dado é entrada e o número de vagas é saída**, então a pergunta de cada arma foi *o que essa coisa é* e o tamanho dela. Fundo `3` numa mão e `5` em duas.

| | assinaturas | armas com gêmea |
|---|---|---|
| v0.44, só o preço | 14 | 35 de 41 — **85%** |
| v0.44, preço × categoria | 25 | 25 de 41 — 61% |
| **v0.45, a régua com fundo** | **39** | **4 de 41 — 10%** |

**Zero armas estourando e zero com vaga vazia.** As duas gêmeas que sobraram são `Machete = Machado` e `Soqueira = Tekko` — pares que **são a mesma coisa na ficção**, e tekko é literalmente a soqueira japonesa. A régua acertou ao não separá-las.

> **Dominância, conferida:** dentro de cada mão todas gastam o orçamento cheio, então **dado maior sempre vem com menos propriedade ou com restrição paga**. Nenhuma arma tem dado maior *e* mais propriedade que outra da mesma mão.
>
> **E o eixo ao lado, que esta frase não cobria — medido na v0.47, nos 1640 pares.** *Dado **igual** e mais propriedade* acontece **três vezes**, e as três são `Versátil` a custo zero: **Espada Longa** passa Machete e Machado, **Taco** passa Wakizashi. Ficam `ACEITA`, com o tamanho que a v0.44 já tinha medido — `0,1` ponto, e só no nível 2, porque do nv6 em diante ninguém larga o escudo e as duas viram a mesma arma na mesa. *A frase acima estava certa e media o outro eixo; a matriz do §5.2 tem o par completo.*

> **Falta uma coluna, e ela é de texto e não de número: a descrição de cada arma.** *Decisão do Mizuki na v0.47.* Cada uma ganha um parágrafo narrativo com **as propriedades em negrito dentro do texto**, explicadas pela ficção em vez de por tabela — é lá que a condição que hoje é tácita fica escrita (*por que este cabo aceita a segunda mão e o do machete não*). **Não é regra nova: é o mesmo conteúdo, dito do jeito que se lê na mesa.**
>
> **Deliberadamente adiado**, porque este documento ainda é nota de design e 52 descrições são material. **Vai junto da passada de texto de mesa**, que a partir da v0.102 tem um destino só — o PDF — e é o primeiro lugar onde a skill `redacao-acessivel-rpg` tem serviço, já que ela nunca foi rodada contra nada. *Enquanto não existir, quem segura a condição é o validador, e ele só consegue acusar; não consegue explicar.*

> **Odachi e Nodachi ficam separados por DECISÃO DE DESIGN, e não por canon.** Três fontes especializadas dizem que os termos são intercambiáveis e que *"não há distinção formal em morfologia de lâmina"*. O que elas sustentam é o **porte nas costas com saque assistido**, e é dele que sai a `Embainhada`. *Fica escrito porque, sem isto, a próxima releitura procura uma fonte histórica que não existe.*

**Lâmina Curta**

| arma | mão | dado | propriedades | gasta |
|---|---|---|---|---|
| Tanto | 1 | **d6** | `Fineza` · `Oculta` | 3/3 |
| Punhal | 1 | **d6** | `Fineza` · `Longo Alcance` | 3/3 |
| Canivete | 1 | **d4** | `Fineza` · `Oculta` · `Rompe` | 3/3 |
| Faca | 1 | **d6** | `Fineza` · `Rompe` | 3/3 |
| Sai | 1 | **d6** | `Fineza` · `Par` | 3/3 |

**Lâmina Longa**

| arma | mão | dado | propriedades | gasta |
|---|---|---|---|---|
| Machete | 1 | **d8** | `Rompe` | 3/3 |
| Wakizashi | 1 | **d8** | `Oculta` | 3/3 |
| Rapieira | 1 | **d6** | `Fineza` · `Talha` | 3/3 |
| Katana | 1 | **d8** | `Versátil` · `Fineza` | 3/3 |
| Espada Longa | 1 | **d8** | `Versátil` · `Rompe` | 3/3 |
| Espadão | 2 | **d12** | `Alcance` | 5/5 |
| Odachi | 2 | **d12** | `Alcance` · `Talha` · `Embainhada` | 5/5 |
| Nodachi | 2 | **d12** | `Alcance` · `Rompe` · `Volumosa` | 5/5 |

**Massa**

| arma | mão | dado | propriedades | gasta |
|---|---|---|---|---|
| Maça | 1 | **d8** | `Talha` | 3/3 |
| Marreta | 2 | **d10** | `Rompe` · `Talha` | 5/5 |
| Kanabō | 2 | **d12** | `Talha` | 5/5 |
| Maul | 2 | **d12** | `Rompe` | 5/5 |
| Taco | 1 | **d8** | `Versátil` · `Oculta` | 3/3 |

**Porrete**

| arma | mão | dado | propriedades | gasta |
|---|---|---|---|---|
| Bastão | 1 | **d6** | `Versátil` · `Alcance` · `Rompe` | 3/3 |
| Bō | 2 | **d10** | `Alcance` · `Emaranha` | 5/5 |
| Cassetete | 1 | **d6** | `Oculta` · `Vestida` | 3/3 |
| Tonfa | 1 | **d6** | `Par` · `Vestida` | 3/3 |
| Nunchaku | 1 | **d6** | `Par` · `Emaranha` | 3/3 |

**Manopla**

| arma | mão | dado | propriedades | gasta |
|---|---|---|---|---|
| Soqueira | 1 | **d4** | `Vestida` · `Oculta` · `Par` | 3/3 |
| Tekko | 1 | **d4** | `Vestida` · `Par` · `Oculta` | 3/3 |

**Machado**

| arma | mão | dado | propriedades | gasta |
|---|---|---|---|---|
| Machado | 1 | **d8** | `Rompe` | 3/3 |
| Machado de Guerra | 2 | **d12** | `Rompe` · `Talha` · `Volumosa` | 5/5 |
| Machadinha | 1 | **d6** | `Longo Alcance` · `Rompe` | 3/3 |

**Ceifa**

| arma | mão | dado | propriedades | gasta |
|---|---|---|---|---|
| Foice | 2 | **d10** | `Emaranha` · `Talha` | 5/5 |
| Kama | 1 | **d6** | `Par` · `Rompe` | 3/3 |
| Kusarigama | 2 | **d8** | `Alcance` · `Emaranha` · `Longo Alcance` | 5/5 |

**Armas Longas**

| arma | mão | dado | propriedades | gasta |
|---|---|---|---|---|
| Naginata | 2 | **d10** | `Alcance` · `Rompe` | 5/5 |
| Yari | 2 | **d10** | `Alcance` · `Talha` | 5/5 |
| Lança | 1 | **d6** | `Alcance` · `Longo Alcance` | 3/3 |

**Flexível**

| arma | mão | dado | propriedades | gasta |
|---|---|---|---|---|
| Corrente | 2 | **d8** | `Alcance` · `Emaranha` · `Rompe` | 5/5 |
| Chicote | 1 | **d4** | `Alcance` · `Emaranha` · `Oculta` | 3/3 |
| Manriki | 1 | **d6** | `Emaranha` · `Oculta` | 3/3 |

**Arremesso**

| arma | mão | dado | propriedades | gasta |
|---|---|---|---|---|
| Kunai | 1 | **d6** | `Longo Alcance` · `Oculta` | 3/3 |
| Shuriken | 1 | **d4** | `Longo Alcance` · `Oculta` · `Par` | 3/3 |
| Tessen | 1 | **d4** | `Longo Alcance` · `Oculta` · `Vestida` | 3/3 |
| Chakram | 1 | **d4** | `Longo Alcance` · `Fineza` · `Oculta` | 3/3 |

**As de tiro** — escada da v0.44, com o `Yumi` refeito na v0.47.

> **As duas do `Yumi` desceram de dado, e o motivo é a régua do §5.1.2.** A escada do tiro foi construída para arma que **não soma atributo** — a fórmula desconta `6,0` de todas —, e o arco soma Destreza. Com o desconto indevido, o `Daikyū 2d8` fazia **15,0** contra os 12,5 do espadão de um Força 6, estourando o orçamento em **3,5**. **`1d10` fecha exato em `4 de 4`** e põe o arco em `11,5`, que é onde a rota de Destreza já está com a Katana — um ponto abaixo da Pesada, que é o desenho.
>
> **A saída bonita foi testada e reprovada:** dar `Volumosa` ao Daikyū (ele tem 2m e se carrega nas costas) devolveria 1 ponto e deixaria `1d12` fechar — e `1d12 + Destreza 6 = 12,5` **empata com a Pesada, à distância.** O §5.0.1 já tinha escrito essa sentença para a `Fineza`: *"empataria com a Pesada nos dois eixos — dominância."* **Empatar de longe é pior que empatar de perto.**
>
> **O `Hankyū` ficou em `1d8` e ganhou `Oculta`**, porque `1d8` sozinho deixaria vaga vazia e o fundo proíbe. *A âncora é de tamanho:* o **daikyū passa de 2 metros** e o **hankyū fica entre 45 e 160 cm**, e as fontes o descrevem como o arco de espaço apertado e de montaria. **Nenhum dos dois domina o outro** — o Daikyū tem dado maior, o Hankyū tem propriedade a mais.
>
> **E o `Yumi` não carrega `Munição`.** *Achado do Mizuki ao fechar esta passada:* **"munição elas precisam, mas não precisam recarregar."** Ele está certo, e a inconsistência já estava no documento: as duas do `Yumi` carregavam `Munição` no §5.3 e **nunca receberam X no §5.2** — a propriedade estava meia aplicada desde a v0.45.
>
> **`Munição` neste sistema não é *ter munição*: é o ciclo de recarga** — recarregar em Ação Bônus, disparado pelo `1–2` natural ou a cada X ataques. Uma besta se arma, um pente se troca; **uma flecha se encaixa como parte do disparo.** Não há recarga para modelar. *A flecha continua existindo como ficção e cai na camada 3 do §6, o inventário por espaço, que está desligada com gatilho escrito.*
>
> **Sair é de graça e o orçamento não se move**, porque `Munição` custa zero (§5.2, *"em Ação Bônus a `Munição` custa zero"*). Os dois continuam fechando `4 de 4`, e nenhuma dominância nova aparece.

> *Registrado de passagem:* a `Volumosa` junta *"não esconde"* e *"atrapalha em espaço apertado"* numa restrição só, e **não existe a propriedade positiva correspondente** — foi por isso que o Hankyū teve de pegar `Oculta`, que é a vizinha e não a exata. Se alguma arma futura precisar dizer *"funciona onde as outras não cabem"*, ela não tem palavra.

| arma | categoria | mão | dado | atributo | propriedades |
|---|---|---|---|---|---|
| Hankyū | Yumi | 2 | **1d8** | Destreza | `Longo Alcance` · `Oculta` |
| Daikyū | Yumi | 2 | **1d10** | Destreza | `Longo Alcance` |
| Besta de Uma Mão | Balestra | 1 | **1d10** | nenhuma | `Longo Alcance` · `Munição` · `Oculta` |
| Besta | Balestra | 2 | **2d8** | nenhuma | `Longo Alcance` · `Munição` · `Rompe` |
| Pistola | Arma de Fogo | 1 | **1d10** | nenhuma | `Longo Alcance` · `Munição` · `Oculta` |
| Revólver | Arma de Fogo | 1 | **1d10** | nenhuma | `Longo Alcance` · `Munição` · `Oculta` |
| Submetralhadora | Arma de Fogo | 2 | **2d6** | nenhuma | `Longo Alcance` · `Munição` · `Par` · `Oculta` |
| Espingarda | Arma de Fogo | 2 | **2d8** | nenhuma | `Longo Alcance` · `Munição` · `Rompe` |
| Rifle | Arma de Fogo | 2 | **2d8** | nenhuma | `Longo Alcance` · `Munição` · `Talha` |
| Rifle de Precisão | Arma de Fogo | 2 | **2d10** | nenhuma | `Longo Alcance` · `Munição` |
| Metralhadora Pesada | Arma de Fogo | 2 | **2d10** | nenhuma | `Longo Alcance` · `Munição` · `Rompe` · `Volumosa` |

## 5.4 Treino de arma — e por que aqui ele não vira castigo

*Decidido na v0.45.* **Decisão do Mizuki:** *"o Emanador e os outros Caminhos que não são marciais não devem conseguir pegar essas armas como espadão; só no caso de pegar a Trilha certa para combate corpo a corpo, que nela concederia treino nessas armas."*

Isso fecha a pergunta que o §8 item 14 abria, e não é ideia nova: **a peça 6 §8 já diz *"confirmado que precisa existir"*** e lista `simples · marciais · de fogo · ferramentas amaldiçoadas`, com **cada Caminho concedendo as suas**. O que faltava era saber se a régua nova tinha tornado a divisão inútil.

### A objeção era boa, e ela derruba metade da ideia

> *"Todas as armas têm seus valores iguais, já que todas se pagam — então talvez fazer a divisão seja meio inútil."*

**Certa na metade que importa: a divisão não pode ser preço.** No PF2e ela literalmente é — `Simple +1`, `Martial +4`, `Advanced +6` no orçamento de pontos da arma. Importar isso aqui seria cobrar duas vezes pela mesma coisa, porque toda arma já fecha em `3/5`.

### E é justamente por isso que ela funciona aqui, e não funciona no 5e

**O modo de falha do 5e é conhecido: lá a arma simples é *pior*.** O conjurador não é só restrito — ele é punido, fica com adaga e clava, e a lista de simples existe para ser ruim. Este projeto já rejeitou esse formato uma vez, quando decidiu que a rota Sem Técnica *"não pode ser os outros menos o Fundamento; se for só subtração, ninguém escolhe por vontade — escolhe por castigo."*

**Aqui não dá para punir nem se quiser, e a conta prova:**

| | uma mão (28 armas, todas `3/3`) | duas mãos (13 armas, todas `5/5`) |
|---|---|---|
| melhor dado do balde **simples** | `d8` — 4,5 | `d12` — 6,5 |
| melhor dado do balde **marcial** | `d8` — 4,5 | `d12` — 6,5 |

**Os dois baldes chegam ao mesmo teto**, porque toda arma gasta o orçamento cheio e dado maior sempre vem com menos propriedade ou com restrição paga. **A divisão restringe *qual* identidade, nunca *quanto* poder** — e isso é exatamente o contrário do que ela faz no sistema de onde ela veio.

### A divisão mora na categoria, não na arma

Mesma lógica que já decidiu o efeito de crítico: **treze nomes, não cinquenta e dois** — a mesa conhece um conjunto de treze em cerca de 23 missões, e um de 52 em 133.

*Testado com `Lâmina Curta · Massa · Porrete · Arremesso` no balde simples:* **19 armas simples contra 22 marciais**, e os dois baldes com dado de uma e de duas mãos. Ninguém fica sem opção de formato.

### 5.4.1 Qual categoria cai em qual balde — fechado na v0.47

*A pergunta foi devolvida para a conta, e a conta fechou junto com o desempate de ficção. O corte não foi escolhido: ele é o que sobra.*

**Quatro travas, todas medidas, e nenhuma delas é de gosto:**

| # | trava | mata |
|---|---|---|
| 1 | cada balde tem arma de uma e de duas mãos | 16 cortes |
| 2 | os dois baldes chegam ao mesmo teto, **nas duas economias de mão** | 240 |
| 3 | sob o requisito de Força, o simples ainda tem arma de duas mãos para quem tem Força < 3 | 192 |
| 4 | nenhum balde fica com menos de 3 das 10 categorias | 33 |

Dos **1024** cortes possíveis das dez categorias de corpo a corpo, **543 passam**. Trava demais para decidir sozinha — o que fecha é cruzar com a ficção.

> **A trava 2 é a que a v0.45 achou que era estrutural, e não é.** Aquela versão escreveu que *"punir é impossível por construção"* porque os dois baldes chegam ao mesmo teto. **Isso era propriedade do corte de teste, não da régua.** O `d8` de uma mão e o `d12` de duas moram nas **mesmas três categorias — `Lâmina Longa`, `Massa` e `Machado`** —, e qualquer corte que ponha as três do lado marcial deixa o simples **1,0 dado atrás nas duas mãos**. Que é exatamente o modo de falha do 5e que aquela decisão diz ser impossível.

**A trava 3 é nova, e ela nasceu do requisito de Força.** Com `Força 3` cobrindo `d10` e `d12`, sobram **duas** armas de duas mãos para quem não tem Força: o **Kusarigama** (`Ceifa`) e a **Corrente** (`Flexível`). Se nenhuma das duas categorias for simples, o Caminho não-marcial de Força baixa fica com **zero** arma de duas mãos — os dois gates se multiplicam em vez de somar. *Nenhum dos dois sozinho faz isso; foi preciso medir os dois juntos, que é a lição nº 7.*

**O desempate de ficção, lido da tabela oficial do 5e 2024** e não de memória:

| vai para simples, sem ambiguidade | vai para marcial, sem ambiguidade | o 5e corta por dentro |
|---|---|---|
| `Lâmina Curta` (dagger) · `Porrete` (club, quarterstaff) · `Ceifa` (sickle) · `Arremesso` (dart, javelin) | `Lâmina Longa` (longsword, rapier, greatsword) · `Flexível` (whip) | `Massa` · `Machado` · `Armas Longas` |

> **A `Manopla` não aparece na tabela do 5e — ele não tem essa arma.** A âncora vem do PF2e e é mais forte que a que faltou: **o gauntlet é arma simples** lá, do grupo `Brawling`, e carrega o traço **`free-hand`** — que é o texto de regra por trás da `Vestida` daqui. *A mesma fonte sustenta a propriedade e o balde.* **Entra no simples.**

**As três que ele corta por dentro são justamente onde mora o teto**, e é aí que a trava 2 morde: como `Lâmina Longa` é marcial sem discussão, **ou `Massa` ou `Machado` tem que ser simples.**

> **Entra `Massa`.** A âncora é específica e não é opinião: o **greatclub é arma simples no 5e**, e um kanabō *é* um greatclub. Do outro lado, **battleaxe e greataxe são marciais**, e o Machado de Guerra é um dos dois. Escolher `Machado` colocaria um machado de guerra no balde de quem não treinou, e ainda deixaria o simples com **4 armas de duas mãos** contra as **6** da rota da `Massa` — medido com o mesmo resto de balde nos dois lados.

**E `Armas Longas` fica no marcial, por um motivo que não é numérico** — a conta é indiferente, porque Naginata e Yari já caem no requisito de Força de qualquer jeito. Quem decide é o `ESTADO-ATUAL`: a árvore da Vanguarda é *"alcance, reposicionamento forçado, troca de alvo"*. **Alcance é a moeda dela**, então o alcance bom é o que o treino destrava. O balde simples não fica sem: `Bastão`, `Bō` e `Kusarigama` carregam `Alcance` lá dentro.

### O corte

> **Simples — 24 armas, 6 categorias:** `Lâmina Curta` · `Porrete` · `Ceifa` · `Arremesso` · `Manopla` · `Massa`
> **Marciais — 17 armas, 4 categorias:** `Lâmina Longa` · `Machado` · `Armas Longas` · `Flexível`

| | teto de uma mão | teto de duas mãos |
|---|---|---|
| simples | `d8` — 4,5 (Maça, Taco) | `d12` — 6,5 (Kanabō, Maul) |
| marcial | `d8` — 4,5 (Machete, Wakizashi, Katana) | `d12` — 6,5 (Espadão, Odachi, Nodachi) |

**Empatam nos dois, que é a trava 2 cumprida com a régua e não com sorte.** E a repartição de propriedade fica assimétrica de propósito: o marcial leva o alcance (8 armas contra 3) e o simples leva a ocultação e o par (`Par` e `Vestida` não existem do lado marcial). **A divisão restringe qual identidade, nunca quanto poder** — que era a promessa do §5.4, agora com o corte que a sustenta.

**As de projétil.** A peça 6 §8 nomeia quatro categorias de treino, e duas delas já têm dono: **`Arma de Fogo` é a "de fogo"**, sozinha, e **ferramenta amaldiçoada fica fora desta peça** (§8 item 2). Sobram `Yumi` e `Balestra`, e o 5e corta por dentro das duas — arco curto e besta leve são simples, arco longo e besta pesada são marciais. **Não dá para importar**, porque aqui a divisão mora na categoria.

> **`Balestra` é simples e `Yumi` é marcial**, e a âncora é histórica em vez de mecânica: a besta mudou a guerra medieval **por não exigir treino** — é o argumento inteiro dela —, enquanto o arco japonês é uma disciplina de anos. *Isso põe o balde simples em 26 armas e o marcial em 19, mais as 7 de fogo.*

### O que isso destrava — e é a razão de a Trilha vir depois desta peça

**A Trilha ganha o que conceder.** O `ESTADO-ATUAL` registra desde a v0.36 que *"a especialização de arma da Vanguarda precisa que arma exista"*, e o §4 desta peça deixou registrado que a Trilha da Vanguarda **deve de 6% a 9% da Rotina** e que *"não pode ser pago em dado de dano"*.

**Treino de arma não é dado de dano.** Ele é acesso — a lista do que a peça 5 §4 **permite** um Caminho conceder. Então a Trilha de corpo a corpo de um Caminho não-marcial concede o treino, e o Emanador que quiser lutar de espadão paga com a escolha de Trilha em vez de ganhar de graça.

### Os dois gates são eixos diferentes, e não se substituem

| gate | separa por | quem ele barra |
|---|---|---|
| **requisito de Força** (§8 item 13) | **atributo** | quem não investiu Força, em qualquer Caminho |
| **treino de arma** | **Caminho** | quem não é marcial, mesmo com Força 6 |

Um é sobre o corpo, o outro sobre o que você aprendeu. **Um Emanador de Força 6 passa no primeiro e para no segundo** — que é precisamente o caso que a decisão do Mizuki queria cobrir.

## 5.5 O requisito de Força — fechado na v0.47

*O requisito morava na classe, e a classe saiu do preço na v0.44. Ele passou duas versões órfão: das 41 armas do §5.3, zero tinham requisito escrito, e a promessa da peça 5 §1 — "armas de dado maior exigem Força mínima; quem luta com Destreza fica nas armas leves" — estava sem implementação.*

> **`Força 3` para os dois degraus de cima da escada de dado.** No corpo a corpo, `d10` e `d12` — **11 das 41**. No tiro, `2d8` e `2d10` — **5 das 11**. Dezesseis de 52.

**A mesma frase, duas escadas, zero parâmetro novo.** A escada do corpo a corpo é `d4 · d6 · d8 · d10 · d12` e a do tiro é `1d10 · 2d6 · 2d8 · 2d10` (§5.0.5); o requisito pega os dois degraus de cima de cada uma. Escapam as leves — Submetralhadora, Pistola, Revólver e Besta de Uma Mão — e pegam besta, espingarda, rifle, rifle de precisão e metralhadora pesada. **O corte de ficção sai sozinho da régua**, sem lista escrita à mão.

> **O `Yumi` não é gateado, e a primeira redação desta seção dizia que sim.** Ela contava `6 das 11` e nomeava *"arco longo"* — verdade enquanto o Daikyū era `2d8`, e **falso desde que ele desceu para `1d10` nesta mesma versão.** *Um número se moveu debaixo de uma frase, dentro da mesma passada.*
>
> **E o conserto revelou que a régua é mais estreita do que ela mesma dizia: o requisito nunca pega arma de Destreza.** As oito com `Fineza` param todas em `d8`; as duas do `Yumi` ficam em `1d8` e `1d10`, que são o fundo da escada do tiro. **O requisito de Força gateia exatamente quem não depende de Destreza** — o corpo a corpo que soma Força, e o tiro que não soma nada. *Isso não foi imposto em lugar nenhum: caiu do orçamento nas três famílias.*
>
> *O que fica em aberto é de ficção e não de conta:* um daikyū de dois metros **exige braço para ser puxado**, e foi esse o exemplo que abriu a decisão. Hoje ele não pede Força porque paga em Destreza. **Se isso incomodar na mesa, a saída não é exceção no gate** — é a peça de furtividade e condições resolvendo o que "puxar um arco de guerra" custa.

### Por que o tiro entra, e o que ele fecha

*Decisão do Mizuki: **"tem arma de longo alcance que vai necessitar de força pra carregar"**. A conta achou um segundo motivo, e ele é maior.*

O §5.2 registra que *"não somar atributo não é penalidade: é independência de atributo"*. **Sem requisito, essa independência vira a melhor arma do sistema para quem não investiu em nada:**

| ficha | melhor arma sem o requisito | com o requisito |
|---|---|---|
| Força 0 · Destreza 0 — o conjurador puro | **Rifle de Precisão, 11,0** | Hankyū, 7,0 |
| Força 3 · Destreza 0 | Rifle de Precisão, 11,0 | **igual — ele passa** |

**Um conjurador que não gastou um ponto de atributo fazia 11,0 de dano**, contra 6,5 do melhor corpo a corpo dele — e o requisito no corpo a corpo sozinho **não fecha isso**, porque a arma de fogo passa por fora. *É o buraco que o §5.2 nomeou e não trancou.*

### O requisito lê o dado impresso, e isso tem um vazamento medido

> **O requisito olha o dado escrito na linha da arma. O passo do `Versátil` não conta.**

Sem essa frase o requisito pega a **Katana**, que tem `Fineza` — quer dizer, cobraria Força de quem trocou Força por Destreza, que é o oposto do que a propriedade existe para fazer. **Com ela, três armas alcançam `d10` sem passar pelo gate:** Katana, Espada Longa e Taco, todas `d8` impresso com `Versátil`.

**O vazamento vale 1,0 dado**, e é o preço de não atropelar a rota de Destreza. *Medido: com o requisito lendo o dado impresso, a melhor arma de Força 0 · Destreza 0 é a Espada Longa em duas mãos, `d10` — exatamente o que um gate `Força 3` só para `d12` entregaria.* **Os dois gates dão a mesma arma ótima em toda ficha**, e é aí que eles deixam de ser equivalentes: o que o `d10` no gate compra não é dano, é **identidade**.

| para quem tem Força < 3 | gate em `d10` e `d12` | gate só em `d12` |
|---|---|---|
| armas abertas | 30 de 41 | 35 de 41 |
| de duas mãos | **2** | 7 |
| com `Talha` de duas mãos | **0 de 6** | 3 |
| com `Alcance` de duas mãos | 2 de 8 | 5 |

**A `Talha` some inteira das duas mãos, e é isso que o gate maior está comprando.** Quem não tem Força não pega arma pesada que atrapalha o bloqueio do outro — o que é o desenho, não um efeito colateral. *Contagem não é valor: o gate maior gateia 5 armas a mais e move zero de dano. O que ele move é o que dá para ser.*

**E o requisito continua sem custar ponto de atributo.** Força 3 é o teto da criação (peça 2 §2) e cabe no array `3·2·2·1·1`, então o requisito resolve **acesso** e não preço — que é a conclusão que o §8 item 1 já tinha fechado e que continua valendo com o requisito ancorado no dado em vez de na classe.

> **A penalidade fechou na v0.104**, na peça 19 §6, e as duas coisas ganharam a mesma resposta que este parágrafo pedia. *Marcado pelo Mizuki na decisão que criou este item.* **Sem treino é desvantagem na rolagem de ataque; sem o requisito de Força o deslocamento cai `3 m`.** *A desvantagem é grande — `54,00` de dano por rodada —, e é essa a intenção:* **as duas somadas custam `33,8` vezes o que a arma inteira entrega, então elas não são preço, são porta fechada.** *E o `3 m` não é escolha: são os `10` pés que o d20 de 2024 cobra de quem veste proteção sem a Força dela.*

---

## 6. Itens comuns

*Entrou na v0.40, a pedido do Mizuki. **A moeda fica para depois** — provavelmente preço e fornecimento. Esta seção decide o que um item pode fazer, não como se consegue.*

Hoje não existe nada: zero ocorrências de dinheiro, preço, consumível ou inventário no projeto inteiro. O que existe são **os ofícios**, que já dizem quem fabrica o quê — Herbalismo (*"planta que cura, planta que mata, chá, unguento"*), Forja, Caligrafia (*"talismã, papel de barreira"*), Entalhador (*"fazer o corpo que vai receber alguma coisa"*). **Falta dizer o que sai da fabricação.**

### Os quatro eixos óbvios já têm dono

| item que dá | bate contra |
|---|---|
| proteção | o teto de Defesa 20 da seção 3, que já está cheio |
| cura de vida | peça 5 §4, peça 10 §2 e peça 7 §5 — três decisões independentes |
| dado de dano | a coluna Rotina |
| PE | o `conferir-orcamento`, que mede os drenos somados |

E o quinto, que parece inofensivo e é o pior: **bônus em rolagem.**

```
crescimento de atributo investido, criação → nv30:   +3
um item de +1  =  33% de tudo que um atributo cresce em 28 níveis
```

Num sistema de **personagem persistente com 5 a 7 mestres**, isso compõe. Se cada mestre entregar um item de +1 por arco, **na terceira mesa o jogador ganhou de graça a campanha inteira de crescimento** — e o mestre seguinte não tem como saber, porque não passou por marco, por XP nem por validador. É o filtro multi-mestre falhando pelo lado que ninguém vigia: não é arbitragem divergente, é **acúmulo invisível**.

> **Então a regra que abre a seção: item comum não produz número.**

### O que o levantamento externo trouxe

Cinco sistemas, e o modo de falha de cada um:

| sistema | o item é | o que quebra |
|---|---|---|
| **D&D 3.5** | número, com `wealth by level` | *Christmas tree*: sem os itens o personagem não funciona. O item virou requisito |
| **D&D 5e** | lista grande em packs | ninguém lê. A postura da mesa vira *"se ele precisasse, teria trazido"* |
| **Blades in the Dark** | `load` + flashback, declarado **depois** | exige que o mestre aceite quase tudo — discricionariedade pura |
| **Torchbearer · Mausritter** | **espaço**. Item ocupa slot, tocha é relógio | vira Tetris, e desliga sozinho se sobrar slot |
| **PF2e alquímico** | consumível que não é poção — bomba, veneno, ferramenta | precisa de economia de crafting inteira embaixo |

*E a ficção ajuda menos do que eu esperava.* Procurando o que um feiticeiro de JJK carrega além de ferramenta amaldiçoada, **não achei lastro** — a obra tem ferramenta e objeto amaldiçoado, e quase nenhum item mundano com peso de cena. O que tem lastro (talismã, papel de barreira) já está escrito nos ofícios.

### As três camadas

*Decisão do Mizuki: as três, em camadas, com a terceira desligada até o playtest pedir.*

**Camada 1 — Permissão. O item abre a porta; ele não atravessa por você.**

A peça 7 já tem o eixo: *"perícia sem treino você tenta; ofício sem treino, não."* Um item de permissão move alguém de **não rola** para **rola sem maestria**.

| CD | sem o item | com ele, nv2 | nv30 |
|---|---|---|---|
| 10 · rotina | 0% | 70% | 80% |
| 14 · fácil | 0% | 50% | 65% |
| 18 · média | 0% | 30% | 45% |
| 22 · difícil | 0% | 10% | 25% |

O ganho é grande, e mesmo assim ele passa na lição nº 1 por três motivos: **não empilha** (dois pés de cabra não abrem melhor), **não deriva** — a CD de perícia é fixa, e a peça 4 §1 diz por quê: *"uma fechadura comum é a mesma fechadura no nível 2 e no 30"* — e **não entra em rolagem disputada**, porque não há ninguém do outro lado.

> **O limite, em uma frase: item abre a porta, treino atravessa bem.** Ele não soma maestria, não concede treino e não repete rolagem — isso é o que o marco compra.

**Camada 2 — Consumível de cena. Gasta e some, então não compõe entre mesas.**

O teto sai do ritmo de missão que a peça 10 já fixou — três lutas de graça antes da exaustão:

| consumíveis levados | fração das três lutas | veredito |
|---|---|---|
| 1 | 33% | decisão |
| 2 | 67% | aperta |
| 3 ou mais | 100% | **vira a resposta padrão** |

**De três em diante ele cobre a missão inteira e o jogador para de precisar do resto da ficha** — é o teste do bônus automático da skill de design, aplicado a item. O teto que cai da conta é **um a dois por missão**, e não por cena.

E o segundo limite é contra o PE, que também é *"da missão inteira"*: um consumível que faz o que um feitiço faria, mais barato, torna o PE decorativo naquela cena. Então ele faz **o que nenhum feitiço faz, ou o que o ofício faz mais devagar** — nunca dano, cura, proteção ou PE.

**Camada 3 — Espaço. Fica desligada, com o gatilho escrito.**

O modelo de slot só funciona se o espaço for escasso, e hoje não há o que carregar: sem as camadas 1 e 2 escritas, o inventário nasce vazio e o sistema desliga sozinho.

> **O gatilho:** *se o playtest mostrar que o grupo leva tudo que quer sem precisar escolher, o espaço entra. Até lá, carregar é ficção.*

Isso é diferente de deixar em aberto — é decisão com condição de disparo, no mesmo molde do *"três lutas de graça"* da peça 10.

## 7. A dívida que esta peça deve à peça 11

**O preço da Reação de cobrir-se tem de virar agnóstico de fonte.** Hoje ela cobra *"você fica sem **a proteção passiva**"* — e quem está de Revestimento não paga isso, porque não tira o colete no meio do golpe.

O tamanho, pelos números da própria peça 11:

| nível | RD | custo hoje | saldo hoje | saldo se o preço sumir |
|---|---|---|---|---|
| 6 | 4 | 1,7 | +2,3 | +4,0 |
| 14 | 10 | 5,3 | +4,7 | +10,0 |
| 22 | 15 | 10,8 | +4,2 | +15,0 |
| 30 | 15 | 14,4 | **+0,6** | **+15,0** |

A peça 11 escolheu o `1,5 ×` com critério escrito: *"o saldo **encolhe** em vez de virar"*. Sem o preço ele sobe e trava no teto — inverte o critério.

> **Conserto decidido:** trocar *"você fica sem a proteção passiva"* por *"você fica sem proteção"*, venha ela de onde vier. Uma palavra a menos.

**Vai junto com esta peça, na mesma versão** — decisão do Mizuki. E a linha *"sem uniforme, sem armadura e sem escudo"* muda junto, porque sob duas classes ela vira `Traje`, `Revestimento` e escudo.

### E a dívida cresceu: o escudo sai dessa lista

*Achado na v0.40, junto com a refeitura da seção 4.* A mesma frase aparece em mais dois lugares, e nos dois ela põe o **escudo** entre o que desliga cobrir-se:

| onde | o que diz hoje | o que passa a dizer |
|---|---|---|
| peça 11 §5 | *"Sem uniforme, sem armadura e sem escudo, a sua proteção é `1/3 do refino + 1`"* | sai o escudo |
| peça 11 §9 | *"uniforme, armadura e escudo **desligam** a proteção de energia"* | sai o escudo |
| peça 8, passo 7 | *"Sem uniforme, sem armadura e sem escudo…"* | sai o escudo |

**Uniforme e armadura continuam desligando; o escudo passa a somar.** O motivo está na seção 4 e é medido: com o desligamento, o escudo vira prejuízo já no primeiro marco, e nenhum número o salva enquanto ele estiver competindo com uma proteção que cresce.

*Isso também muda a frase da peça 11 §9 que virou orientação desta peça inteira — "um uniforme precisa valer mais que proteção 4". Ela continua valendo para uniforme. Para o escudo, deixa de fazer sentido: ele não substitui mais nada.*

**Três documentos, e nenhum validador cruza essa frase hoje.** Entra na lista de checagens do validador desta peça — é a armadilha do *"decisão registrada não é decisão aplicada"*, que já custou sete versões na Trilha.

## 8. Em aberto

1. ~~**A `Pesada` paga dois pontos de Força a mais que a `Uma mão` e entrega o mesmo valor líquido.**~~ **Fechado na v0.40, e o argumento que ia salvá-la caiu por ser desnecessário.** O requisito não é compartilhado com o Revestimento: ele é **grátis**, porque a Pesada pede Força 3 e 3 é o teto da criação. A dominância que existe é outra, e é dupla — **`Uma mão` está dominada pela `Versátil`** (seção 5), e **a `Pesada` perde para `Uma mão` + escudo do nv5 em diante** pela conta refeita da seção 4. As duas continuam abertas, mas nenhuma pelo motivo escrito aqui.

   > **E o furo do teste era um nível acima do que esta linha dizia.** Não é só que a matriz não somava o total: é que ela roda **uma vez só**. Enquanto o escudo desligava cobrir-se, existiam duas populações com dominâncias opostas — ficha de uniforme (escudo domina a Pesada) e ficha de cobrir-se (Pesada domina a Uma mão) — e rodada uma vez a matriz cancelava as duas e saía verde. Com o escudo somando, isso deixa de acontecer; **a exigência para o validador fica registrada de todo jeito**, porque uniforme e cobrir-se continuam sendo rotas de proteção diferentes.
2. ~~**Ferramenta amaldiçoada fica fora desta peça.** Decisão do Mizuki: canalizar energia já faz arma comum ferir maldição, e ferramenta amaldiçoada entra em tópico próprio, com graus e forja.~~ **A decisão fica de pé, e o tópico próprio virou a peça 16, na v0.59.** *Ela é uma das 52 armas desta peça mais um `Estigma`, e o fundo daqui continua sendo o chão dela.* **A `Armaria` do Descendente e o `Enterrado` do Reencarnado foram relidos na v0.49, e os dois não pedem a mesma coisa** — a Armaria é ferramenta amaldiçoada e o Enterrado é objeto amaldiçoado, que é outra peça.
3. ~~**As quatro vagas de Desliga da peça 13** que esperam equipamento.~~ **Voltamos na v0.49, e nenhuma das quatro abriu.** Elas nomeavam a peça errada: duas esperam `ferramenta amaldiçoada` — que esta peça declinou no item 2 acima —, uma espera `objeto amaldiçoado` e uma espera **Técnica Marcial**, tendo nomeado o que a bloqueava em vez do dono. **E esta peça produziu um alvo legal só**, o requisito de Força, que vale `1,0` de dado e zero para quem já tem Força 3. *A trava do Desliga proíbe encostar no que tem preço, e este documento precificou quase tudo que nomeou.* A conta está na peça 13.
4. ~~**Munição:** quantos tiros, e como recarrega.~~ **Fechado na v0.42** — dois gatilhos, recarga em Ação Bônus, X entre `1`, `2`, `3` e `—`. **Mas a régua do §5.0 acaba de reabrir a metade do slot**, e o item 12 abaixo tem a conta.

12. **A arma de fogo estoura o orçamento, e a v0.42 mediu contra a pessoa errada.** *Achado na v0.44, pela régua do §5.0.*

    | arma | gasta | orçamento | saldo |
    |---|---|---|---|
    | `2d8` — Pistola, Revólver, Besta de Uma Mão | 1,5 | 2 | ok |
    | `3d6` — Submetralhadora | 3,0 | 4 | ok |
    | `3d8` — Espingarda, Rifle, Besta | 6,0 | 4 | **−2** |
    | `3d10` — Rifle de Precisão, Metralhadora Pesada | 9,0 | 4 | **−5** |

    **E isso está medido contra Força 6**, que é o melhor caso para o corpo a corpo. Contra quem de fato escolhe uma arma que não soma atributo:

    | Força de quem segura | o `3d10` estoura em |
    |---|---|
    | 6 | 5 pontos ≈ 5% da Rotina |
    | 3 — o teto da criação | 8 |
    | **0** | **11 pontos ≈ 11% da Rotina** |

    > **A Trilha da Vanguarda inteira deve 6% a 9%. O `3d10` na mão de um Força 0 passa disso sozinho.**

    A v0.42 mediu **+4,3% da Rotina** e aceitou pelo tamanho — e o número bate exato com o meu contra Força 6. **O que faltou foi medir contra quem escolhe a arma**, que é a lição nº 7: *um preço se mede somado, nunca sozinho.* Aquela versão também derrubou o argumento de *"não soma mod E tem munição"* por dupla contagem, e estava certa nisso; o defeito é outro e é de população, não de contagem.

    **E a `Munição` devolve zero hoje**, porque o §5.2 escreve que recarregar é Ação Bônus e que *"em Ação Bônus a `Munição` custa zero"*. O contrapeso que o desenho supunha não existe.

    **As duas saídas levantadas, e por que uma delas nem existia:**

    | | o que acontece |
    |---|---|
    | ~~**A — `Munição` volta a custar a Ação Padrão**~~ | **A saída era falsa.** Ela foi montada em cima da tabela de `54% / 46% / 14%` do §5.2 — que estava calculada com a regra *"recarregar custa a sua ação"*, **substituída pela Ação Bônus na mesma seção e nunca apagada.** Eu li a metade morta. *É a lição nº 5 na direção mais chata: a tensão de preço era uma contradição de texto, e a conta em cima dela não valia nada.* |
    | **B — o dado do topo desce** | é a que sobrou, e é a que foi tomada |

    **Fechado na mesma versão, e nenhuma das duas saídas era suficiente sozinha.** O Mizuki perguntou se *"não ter MOD e precisar de Ação Bônus para recarregar"* já não pagava. Medido: **`sem MOD` devolve 0,0** (não é penalidade, é independência de atributo — e o `16,5` já era o total sem atributo, que é o que a v0.42 acertou) e **a Ação Bônus devolve 0,1 a 0,3** com X ≥ 2. **Somados, ~0,3 dos 5 pontos.**

    > **Decisão do Mizuki: o topo desce.** `2d10`, escada de dois dados, com `2d8`, `2d6` e `1d10`. Está no §5.2, com o contra-teste contra a `Pesada` e a `Haste`.

    **E o X da `Munição` fica em `2` ou `3`**, pelo critério dele de que nenhuma arma atravesse a briga sem recarregar. *Ele propôs `2 · 4 · 5`, e a simulação reprovou os dois de cima:* com `4`, 22% dos combates passam sem recarga para quem não tem ataque extra; com `5`, 68% — e o `5` já é indistinguível de não ter teto. **Falta só decidir qual arma leva `2` e qual leva `3`.**
5. ~~**`Versátil`: os dois dados não estão escritos.**~~ **Fechado na v0.44, e a pergunta estava mal posta.** Ela não tem *dois dados*: ela tem **um passo na escada** — `d6→d8 · d8→d10 · d10→d12` —, e o preço dela é **zero**, porque largar o escudo só compensa no nível 2 e por 0,1 ponto. *O que sobrou disso é a dominância que o passo de graça produz entre armas idênticas, medida na v0.47 e aceita: três pares, no §5.2.*
6. ~~**Os nomes dos degraus de escudo, e quantos são.**~~ **Fechado na v0.59:** são três — `Broquel`, `Médio` e `Torre` —, e a forma já tinha fechado antes (proteção, requisito de Força, teto de Destreza).
7. ~~**As sete propriedades sem texto.**~~ **Reduzidas a duas e meia na v0.42, e três delas eram a mesma coisa.** `Alcance`, `Distância` e `Arremesso` colapsaram em `Alcance` e `Longo Alcance`, as duas com número em metros em vez de redação. `Par` fechou em *"role dois dados de dano e fique com o melhor"*, 0,32 contra um alvo de 0,33. `Fineza` entrou. ~~**Falta `Oculta`, os dois dados da `Versátil` e o número da `Munição`.**~~ **Os três fecharam entre a v0.42 e a v0.44** — `Oculta` como camada 1 do §6, `Versátil` como passo de escada a custo zero, `Munição` com o X em `2 · 3 · 4`. **E hoje são doze propriedades, todas com texto**, conferido na matriz da v0.47.

   > **E o `0,60` daquela linha estava errado.** Com a fórmula que o §4 desta mesma peça fixou — `diferença de dado × 0,55 de acerto × 0,60 de uso` —, d10 contra d12 dá **0,33**. O `0,66` do §4 reproduz exato; o `0,60` do §5 só aparece se você tirar o fator de uso. **Duas fórmulas no mesmo documento**, e a segunda foi escrita sem o fator que a primeira tinha acabado de estabelecer.

   > **Mas o buraco de verdade não era o dado, e ele é 5× maior.** A peça 6 §3 é a única definição do golpe simples no projeto — *"arma + Força"* — e **não tem exceção para arma de tiro**. Como o acerto à distância soma Destreza (peça 1 §5), a arma de tiro acertava com um atributo e causava dano com o outro: **2,48 por rodada contra os 4,12 da Pesada, quando a matriz achava que a distância era 0,33.** É a lição nº 6 na direção de sempre — o preço usa um termo que existe, e ninguém foi ler a regra pendurada nele. *Resolvido pela categoria: `Yumi` soma Destreza, `Balestra` e `Arma de Fogo` não somam atributo nenhum e ganham dado maior.*
8. ~~**O teto de Defesa 20 não tem dono declarado.**~~ **Fechado na v0.42, e a resposta não era nenhuma das duas que esta linha oferecia.** O 20 é **derivado** de três números que já têm dono — `10` da peça 1 §5, o teto de atributo `6` e o teto de refino `10` da peça 2 §3, e a fórmula de cobrir-se da peça 11 §5. Zero parâmetros livres, então **ninguém escreve o número**: escrevê-lo em qualquer peça seria a lição nº 9, e medir uma checagem contra ele seria a nº 8. O que esta peça declara é o **invariante** — *nenhuma montagem de equipamento passa da Defesa que a rota sem equipamento alcança* —, e o validador deriva o teto dos três donos. Está no §3.

   > **E de passagem caiu a frase que sustentava o item:** o §3 dizia que as duas rotas topam em 20. Equipamento topa em **19**, e a diferença nasceu no §4, quando o escudo ganhou teto de Destreza. **Decisão do Mizuki: fica em 19**, agora como decisão e não como sobra.
9. ~~**O validador.**~~ **Ele entrou na v0.48, e é o `conferir-equipamento.py`.** *Quantos blocos ele tem é do código, e quem publica é a checagem 9 do `conferir-repositorio.py` — esta linha dizia `onze` desde a v0.48 e o código já estava em doze.* *A lista abaixo é a especificação que ele foi escrito para cumprir, e fica como registro do que foi pedido.* Checagens que ele precisa ter: a régua do orçamento por classe; dominância **por valor total e uma vez por rota de proteção** — *a especificação pedia **três**, com `sem energia nenhuma` separada; **desde a v0.118 são duas**, porque aquela Origem ganhou a `cobrir-se` portada na peça 11 §6.8 e a terceira rota colapsou na primeira. **O validador sempre implementou duas**, então nada nele mudou — o que estava errado era esta linha*; a escada de proteção contra a peça 11; o requisito de Força contra a peça 2 — incluindo que **nenhum requisito passe do teto de criação sem que isso seja decisão escrita**; que **o teto de Defesa seja derivado dos três donos e nunca lido de uma constante**, com a busca exaustiva provando que nenhuma montagem de equipamento passa da rota livre; que a lista de situações do Traje passe na régua de três itens do §3, **inclusive a vaga aberta**, e que o Traje conceda **uma** situação e não uma por degrau;

   > **A dominância do escudo muda de resposta conforme a rota, e isso é novo.** O §4 provou que nenhum degrau é dominado — degrau 1 melhor em Destreza 4–6, degrau 2 em 2–3, degrau 3 em 0–1. **Aquela tabela foi rodada só na rota de cobrir-se.** Na rota do Revestimento o teto de Destreza já é 0, então o teto do escudo não custa nada e ele vira proteção pura: **o degrau 3 domina o 1 e o 2, sempre.** E `Revestimento 3 + escudo 3` dá 19 com Destreza **zero** — o melhor resultado do sistema em cinco das sete Destrezas, e empate na sexta. Isso não derruba a escada; ela continua certa na rota em que foi medida. O que muda é que a peça tem de dizer que **o degrau 3 é a resposta do Revestimento e o degrau 1 a de cobrir-se**, em vez de vender três opções para todo mundo. *É o furo que este item já previa acontecendo antes de o validador existir.* a busca exaustiva de uniforme × escudo × Destreza contra o teto de Defesa; que a frase do desligamento não cite escudo nos três documentos; **que nenhum item comum produza número** e que o teto de consumível por missão bata com as lutas de graça da peça 10; e que todo nome do catálogo, **propriedade inclusive**, passe na triagem — com `Alcance` e `Distância` entrando como `ACEITA` e não como erro.
13. ~~**O requisito de Força ficou órfão, e é dívida da v0.45.**~~ **Fechado na v0.47, e ele reancorou no dado.** `Força 3` para os dois degraus de cima de cada escada — `d10` e `d12` no corpo a corpo, `2d8` e `2d10` no tiro, **dezesseis de 52**. Está no §5.5, com o vazamento do `Versátil` medido em 1,0 dado, o buraco da independência de atributo fechado, e o achado de que **o requisito nunca pega arma de Destreza** — nem `Fineza`, nem `Yumi`.

14. ~~**A divisão simples/marcial, e se ela ainda faz sentido.**~~ **Fechada na v0.47.** Simples: `Lâmina Curta` · `Porrete` · `Ceifa` · `Arremesso` · `Manopla` · `Massa` · `Balestra`. Marciais: `Lâmina Longa` · `Machado` · `Armas Longas` · `Flexível` · `Yumi`. `Arma de Fogo` é a terceira categoria de treino, sozinha. Está no §5.4.1, com a busca exaustiva dos 1024 cortes.

15. **A penalidade por pegar arma sem requisito ou sem treino.** *Marcada pelo Mizuki ao fechar o item 13.* Os dois gates dizem o que você **não** pega e não o que acontece se pegar. A resposta é a mesma para os dois e é da peça 19, **dano e condições** — escrita na v0.103, e este item continua aberto lá dentro: a saída óbvia do hobby é desvantagem na rolagem, e este projeto já mede desvantagem em **−25 pp contra alvo difícil** (peça 11) — grande demais para um item, então o número tem de sair de outro lugar. **Enquanto não existir, os dois gates são proibição e não penalidade**, e o texto tem de dizer isso.

16. ~~**As duas armas do `Yumi` estouram o orçamento.**~~ **Fechado na v0.47, e a decisão veio como régua e não como conserto.** *Decisão do Mizuki:* **"toda arma de longo alcance que exija fisicamente algo do portador soma atributo — diferente de bestas e armas de fogo, em que você só precisa mirar."** Isso virou o §5.1.2, e ele **deriva** a tabela de fonte de dano em vez de listá-la. O conserto que cai dela: `Daikyū` para `1d10` (fecha exato, 11,5 de dano) e `Hankyū` para `1d8` com `Oculta` (10,5). *A tentação do `1d12` com `Volumosa` foi medida e reprovada: empataria com a Pesada, à distância.* **O texto do achado fica abaixo, porque a conta foi feita.**

    *O achado original, arquivado:* Aquela fórmula desconta `6,0` — *"a Força que o corpo a corpo soma"* —, desconto que só está certo para arma que **não soma nada**. As nove de `Balestra` e `Arma de Fogo` reproduzem exatas contra a tabela publicada; o `Yumi` soma **Destreza** (§5.1) e leva o desconto do mesmo jeito.

    | arma | dado | com Destreza 6 | gasta | orçamento |
    |---|---|---|---|---|
    | Hankyū | `2d6` | 13,0 | 5,5 | 4 — **estoura 1,5** |
    | Daikyū | `2d8` | **15,0** | 7,5 | 4 — **estoura 3,5** |

    **O Daikyū passa a `Pesada` em 2,5 de dano** — 15,0 contra os 12,5 de um Força 6 com espadão —, e a rota de `Fineza`, que é a comparação certa, faz 10,5. *O §5.3 afirma "zero armas estourando o orçamento"; vale para as outras 50.*

    **As duas saídas, e as duas têm número:** ou o `Yumi` **para de somar Destreza** e vira a escada do tiro sem mexer em dado nenhum, ou ele **soma e desce o dado** — pela fórmula, duas mãos com `Longo Alcance` fecha em 4 com média 5,5, o que põe o Daikyū em `1d10` e obriga um degrau novo abaixo dele para o Hankyū. **É decisão de sabor com o custo já medido**, e ela mexe em duas linhas do §5.3.

19. **O barulho é da categoria, e ele espera a regra de furtividade.** *A metade que sobrevive da `Silenciosa` — ver §5.0.5.* Quem revela não é a arma, é a **`Arma de Fogo`**, e isso é uma linha na categoria em vez de uma propriedade em quarenta e cinco armas. **Não pode ser escrito hoje**, porque não existe regra dizendo que barulho quebra furtividade — seria preço sem regra pendurada, que é a lição nº 6. *Quando a peça de furtividade existir, a forma já está decidida: `Arma de Fogo` revela; o resto pede teste.* E o manual já mostra quanto vale a versão dele: `Silencioso` é Melhoria **Leve**.

18. ~~**O fundo da v0.45 nunca chegou nas armas de tiro, e são 7 dominâncias.**~~ **Fechado na v0.47, e o conserto não foi encher vaga: foi dar escada própria ao tiro.** A causa não era desleixo — a fórmula grampeava `1d10` e `2d6` no mesmo custo zero, então a régua não distinguia uma pistola de uma submetralhadora, e os gastos fracionários faziam propriedade inteira nunca fechar. **O degrau virou a unidade** (`0 · 1 · 2 · 3`) com fundo `2/4`, no precedente do §5.0.3. As sete vagas foram preenchidas com propriedade que já existia, e **as 7 dominâncias caíram por construção.** Está no §5.0.5 e no §5.3. *O achado original fica abaixo.*

    O §5.0 põe **fundo** no corpo a corpo — `3` numa mão, `5` em duas — e escreve que *"gastar menos que o orçamento é dominância estrita, então toda arma é obrigada a encher as vagas"*. **As 11 de tiro ficaram na régua da v0.44, sem fundo**, e ninguém voltou. O §5.3 diz *"zero armas estourando e zero com vaga vazia"*: **é verdade para as 41, e falso para 7 das 11.**

    | | |
    |---|---|
    | armas de tiro com **vaga vazia** | **7 de 11** (a maior é a Submetralhadora, sobrando `3,0` de `4`) |
    | **dominâncias estritas** no tiro | **7** |

    O `Rifle` (`2d8`, X=3) domina sozinho **três**: `Besta`, `Espingarda` e `Submetralhadora` — dado maior ou igual, recarrega menos, mesmas propriedades. `Rifle de Precisão` domina `Besta` e `Espingarda`. `Pistola` e `Revólver` dominam a `Besta de Uma Mão`.

    > **Isso não é o mesmo caso da `Versátil` do item 17.** Lá a dominância vale `0,1` ponto num único nível e é gêmea com texto a mais. **Aqui são armas estritamente piores sem nada em troca** — a Espingarda não faz uma coisa que o Rifle não faça, e recarrega mais. *Não dá para aceitar sete disso; dá para consertar, e o conserto é o mesmo que a v0.45 fez com as 41: encher as vagas com identidade.*

    **O espaço existe:** as propriedades que o tiro usa hoje são três (`Longo Alcance`, `Munição` a custo zero, `Oculta`) e a `Volumosa`. O catálogo tem doze. **`Rompe` numa arma que fura estrutura, `Par` num revólver de duas mãos, `Talha` numa espingarda** — nada disso precisa de propriedade nova.

    **É passada de catálogo, não de régua**, e ela bloqueia o validador da peça: sete dominâncias estritas fazem a matriz falhar, e uma matriz com sete exceções escritas não confere nada.

17. **`Versátil` é não precificada, e quem segura ela é a ficção.** *Achado na v0.47, rodando a matriz sobre arma.* O preço `0` foi bem argumentado na v0.44 e a conta continua de pé — **o que ninguém tinha olhado é a consequência.** Das 28 armas de uma mão, **4 carregam `Versátil` e 24 não**, e **17 das que não carregam têm o mesmo dado de uma que carrega**. Nenhuma delas é impedida pelo orçamento; todas são impedidas por *"machete não se empunha com duas mãos"*.

    **Isso não é defeito por si.** Ficção segurando uma propriedade é o mesmo mecanismo que faz a naginata ter `Alcance` — o §5.0.2 já diz que *"propriedade não é escolha: é o que a arma é"*. **O que é defeito é não estar escrito**, porque um mestre que aceite uma arma caseira com `Versátil` a mais não passa por trava nenhuma.

    **A saída de preço já estava reprovada:** a v0.44 testou `d8/d10`, `d8/d12` e `d6/d10` e em nenhum largar o escudo compensa. **Dar número a `Versátil` não conserta nada.**

    > **Decisão do Mizuki, e ela resolve os dois lados de uma vez.** *"Dá pra fazer uma descrição para cada uma das armas — por mais que já seja intuitivo — e nessa descrição colocar em negrito as propriedades no texto, explicando elas de forma narrativa."*
    >
    > **A condição de ficção deixa de ser tácita porque ela vira texto da arma.** Não é regra nova nem preço novo: é o parágrafo que diz o que a coisa *é*, com `Versátil` em negrito dentro dele explicando por que aquele cabo aceita a segunda mão e o do machete não. **A trava passa a ser o próprio texto** — quem for escrever uma arma caseira tem de escrever a frase, e a frase ou fecha ou não fecha.
    >
    > **E fazer isso agora é desperdício** — decisão dele, e ela está certa: as 52 descrições são texto de mesa, e este documento ainda é nota de design. **Fica declarado no §5.3 como coluna que vem**, para ser puxado na passada de material, junto do PDF e do resto do que a `redacao-acessivel-rpg` nunca viu.
    >
    > **Até lá o validador acusa**, que é a metade de graça: as quatro que carregam `Versátil` hoje entram como lista `ACEITA` e **uma quinta falha**, no mesmo molde que `Alcance` e `Distância` já usam.

10. **A lista de itens comuns.** A régua das três camadas fechou; os itens não. Quantos, quais e como se chamam é escolha de sabor, e cada um precisa passar pelo filtro *"não produz número"* e pela triagem.
11. **A moeda.** Adiada de propósito na v0.40 — *"provavelmente vai ser com preço e fornecimento"*. A única moeda que o projeto declara hoje é **patente, contato, favor, acesso** (peça 12 §6), e ela é discricionária: dois mestres liberam coisas diferentes pelo mesmo favor. Se ela virar a moeda de item, precisa de tabela, no molde do ambiente propício.

## 9. O que já foi conferido, e como

- **Regressão da régua das Restrições contra o manual:** 18 feitiços com Classe deduzida, **zero divergências**. `Leve = teto(Classe/2)`, `Média = Classe`.
- **Achado de caminho:** o `conferir-acao.py` **não abre o `.docx`** — a faixa de cada Restrição está escrita à mão dentro dele, e ele cobre **11 das 18** do manual. Ficam sem conferência: `Aquecer`, `Assinatura`, `Barulho`, `Condicional`, `Dívida`, `Fraqueza`, `Uma Vez`. Hoje não há erro; o que não há é trava. É a lição nº 9, e o conserto é uma checagem no validador dono.
- **A curva de refino do modelo reproduz sozinha o "refino 5, 4 e 3"** que a peça da Expansão usou no nv10 para escolher o gate — regressão contra número já publicado.

### A passada da v0.40

Quatro contas, e as três primeiras derrubaram texto que já estava escrito aqui.

- **Regressão contra a própria seção 4:** a coluna do escudo (`0,9 · 1,8 · 2,7 · 3,6` nos nv6/14/22/30) reproduz exata. É o que prova que o erro estava na *outra* coluna, e não na conta inteira.
- **A unidade do `CHEFE`** foi lida do uso, não do nome: `conferir-atributos.py:459` faz `dano_chefe(14) * 0.5`, e a linha 468 declara `ACERTO = 0.5`. Dano por acerto, não por rodada. Sem isso a arma sai 1,8× inflada.
- **Contra-testes**, quatro, todos acendendo: dado igual (d8×d8) domina em todo nível; escudo zerado inverte; a conta sem a taxa de acerto reproduz o `nv16` da versão velha desta seção; e a peça 11 promete *"1 no nv2 e 4 no refino 10"* — o modelo devolve 1 e 4.
- **Sensibilidade rodada em três eixos**, porque nenhum deles tem medição de mesa: uso do golpe simples (40% a 100%), golpes recebidos por rodada (0,25 a 2,0) e taxa de acerto (50% a 75%). **O veredito da seção 4 não vira em nenhum dos três** — a taxa de acerto move o ponto de virada só de nv5 para nv7.
- **Levantamento externo:** o texto de regra do `Raise a Shield` veio do Archives of Nethys, não de fórum. A régua que o hobby usa para esta troca é **proporcional** — *"um escudo corta 10–20% do dano recebido, então a arma de duas mãos deveria dar 10–20% mais dano"* —, e a deste sistema é absoluta. É a mesma lição nº 1 por outra porta.
