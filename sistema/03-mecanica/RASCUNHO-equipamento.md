# RASCUNHO — Equipamento

**Não é peça.** Sem número na frente de propósito: meia peça não é peça, e um arquivo com dois dígitos quebraria a contagem do `conferir-repositorio.py`. Vira a peça 14 quando fechar, junto do validador dela — que ainda não existe e por isso não é citado pelo nome aqui.

*Estado na v0.44: proteção fechada, categorias fechadas, e a recarga fechada. **A régua do preço mudou** — o preço mora na arma, com orçamento, e a tabela inteira dela está no §5.0.1. Fecharam junto: a escada do tiro (`2d10` no topo), o X da `Munição` (`2 · 3 · 4`), a `Versátil` (custa zero) e o teto da `Fineza` (d6 numa mão). **Falta o dado e as propriedades de cada uma das 52, os treze efeitos de crítico, e o validador.***

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

O `0,55` é a peça 1 §6 mais os 10% do crítico da §5.2. E o "quanto do tempo" tem teto conhecido: o `conferir-orcamento.py` mede o Bastião conjurando em **38% a 48%** das rodadas, e golpe canalizado não soma arma (peça 5 §3). Sobram no máximo 62%, divididos com Classe 0 e projetar energia.

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

| degrau | proteção | teto de Destreza | requisito de Força | custa marco? |
|---|---|---|---|---|
| 1 | 1 | 5 | — | não |
| 2 | 2 | 3 | 3 | não — cabe na criação |
| 3 | 3 | 1 | **5** | **sim, 2 pontos** |

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

**Os nomes dos três degraus ainda não foram escolhidos.** Mortos na triagem: `Anteparo` é **Melhoria** e `Bloqueio` é **Tema**, os dois com o nome inteiro. Livres: **Broquel · Pavês · Rodela · Adarga · Tarja · Couraça · Guarda-Corpo**. Quantos degraus e quais nomes é escolha do Mizuki.

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

| propriedades | **uma mão** (orçamento 2) | **duas mãos** (orçamento 4) |
|---|---|---|
| 0 | **d8** | **d12** |
| 1 | **d6** | **d10** |
| 2 | **d4** | **d8** |
| 3 | — | **d6** |
| 4 | — | **d4** |

**É o mecanismo do PF2e — propriedade definidora limitando o dado —, só que aqui ele não precisa ser escrito à mão.** Lá a lista de tetos é decidida caso a caso (`Agile` d6, `Finesse` d6, `Reach` d10 e proíbe `Agile`); aqui a lista **é** o orçamento, e combinação abusiva fica ilegal por construção em vez de ser pega no teste.

*Contra-teste:* a tabela reproduz cinco das seis classes publicadas — `Oculta` d4+2 · `Curta` d6+1 · `Uma mão` d8+0 · `Haste` d10+1 · `Pesada` d12+0 — e reprova a sexta, que é a `Versátil`, pelo mesmo ponto de sempre.

**E o teto da `Fineza` cai sozinho dela.** `Fineza` custa 1 ponto, então numa mão sobra 1 para o dado: **d6**. Conferindo pelo outro lado, com o critério de que a rota de Destreza empata em Defesa 19 e precisa ficar atrás em dano: `Fineza` num **d12** daria `6,5 + Destreza 6 = 12,5`, que **empata com a `Pesada` nos dois eixos** — dominância. O orçamento corta três degraus antes disso. *É exatamente onde o PF2e põe o teto do `Finesse`, por um caminho diferente.*

### 5.0.2 Por que isso não vira a armadilha da longsword

A peça 5 já provou que **o dado não é alavanca**: trocar d6 por d12 move três pontos numa lacuna de cem contra a coluna Rotina. **Isso é o que torna o preço por arma barato aqui, e é o contrário do 5e**, onde o dado *é* a arma inteira e por isso duas armas com o mesmo dado são o mesmo item — o defeito que o próprio material do hobby descreve como *"um Guerreiro não tem razão real para escolher Machado de Batalha em vez de Martelo de Guerra ou Espada Longa."*

**Mas o dado não é um eixo livre, e é aqui que a primeira versão desta seção errou.** Sob a régua, escolhidas as mãos e o número de propriedades, **sobra um dado legal só** — gastar menos que o orçamento é dominância estrita, então ninguém gasta. O dado é **saída** da conta, não entrada:

| | 0 props | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **uma mão** | d8 | d6 | d4 | — | — |
| **duas mãos** | d12 | d10 | d8 | d6 | d4 |

**Quem carrega a variação é a propriedade, e propriedade não é escolha: é o que a arma é.** Uma naginata tem `Alcance` e ocupa as duas mãos, e isso já a manda para o d10 — a Yari e a Lança caem no mesmo lugar pelo mesmo motivo, sem ninguém ter decidido nada.

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

## 5.1 A categoria — o que a arma é

*Entrou na v0.42.* A classe é o pacote mecânico: dado, Força mínima, propriedades. **A categoria é o que a coisa é.** Ela existe por dois motivos, e nenhum dos dois é preço.

O primeiro é que ela resolve de onde vem o dano — foi ela que destravou a arma de tiro, que acertava com Destreza e causava dano com Força porque ninguém tinha cruzado a peça 1 §5 com a peça 6 §3. O segundo é que **ela é o gancho onde a Trilha da Vanguarda vai pendurar a especialização**, e sem ela aquela peça nasce sem ter em que especializar.

> **A categoria carregava uma coisa só: a fonte do dano.** *Reaberto na v0.44, e o motivo de reabrir é que a premissa caiu.* A trava original era: *"se ela carregasse número próprio, o valor de uma arma viraria `classe + categoria + propriedade` e a matriz teria de rodar sobre o produto dos três — que é a lição nº 7 pela porta de trás."*
>
> **Com a classe saindo do preço no §5, esse produto deixou de existir.** Sobrou `arma × categoria`, e a arma inteira agora fecha num orçamento em vez de ser comparada par a par. **A objeção era a matriz, e a matriz mudou de forma.**

### 5.1.1 A categoria ganha um efeito de crítico — e por que ele não entra no orçamento

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

| fonte do dano | quem |
|---|---|
| **Força** | todo corpo a corpo, e Arremesso |
| **Destreza** | corpo a corpo com **`Fineza`**, e **Yumi** |
| **nenhuma — só o dado, e o dado é maior** | **Balestra** e **Arma de Fogo** |

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

**O X não é a capacidade real, e o modelo velho errava num segundo ponto.** Ele supunha **2,2 ataques por combate** — um golpe simples por rodada. Mas a peça 6 §3.1 dá **ataque extra ao Bastião e à Vanguarda no nível 6**, e *"ataque extra é sempre golpe simples"*, que é exatamente o que a arma de tiro faz. Refeito com dois golpes por rodada:

| X | fração dos ataques que sai, **sem** ataque extra | **com** ataque extra |
|---|---|---|
| **1** | 100% | **64%** |
| 2 | 100% | 97% |
| 3 | 100% | 99% |
| 4 ou mais | 100% | 99% |

> **O `X = 1` apaga o ataque extra, e esse é o achado.** Com dois golpes por rodada você precisa de **duas recargas** e só tem **uma Ação Bônus** — então a recarga não atrasa o tiro, ela come o benefício de nível 6 de dois Caminhos inteiros. *Achado pelo Mizuki, olhando a faixa e dizendo que ela estava baixa demais.*

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

**Uma metralhadora de cinta é arma de Vanguarda, e a Vanguarda ganha ataque extra no nv6 — exatamente onde o vazamento fecha.** E o que vaza custa **0,1 a 0,3 ponto**, porque recarregar em Ação Bônus já era quase de graça. **É textura, não balanço: registra-se em vez de consertar.** *Escrever exceção para 0,3 ponto é medir contagem em vez de peso, que é a lição nº 3.*

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

### `Uma mão` × `Versátil` — aceita, e o motivo é melhor que o número

*A dominância é fraca: com escudo empatam em 1,49; sem escudo a `Versátil` faz 1,82. Não existe caso em que a `Uma mão` seja melhor.*

> **Decisão do Mizuki: fica.** *"Vai ter vezes que vamos querer uma mão livre, por exemplo para pegar itens — e a `Uma mão` pode vir a ser usada em empunhadura dupla, uma mecânica que podemos trabalhar depois."*

**As duas razões são reais e nenhuma das duas tem número hoje**, e é honesto dizer isso: nada no sistema hoje cobra por ter as mãos ocupadas fora do escudo, e a empunhadura dupla não existe. **É valor a prazo** — a classe está reservada para uma mecânica que vem, não paga uma que já está aqui. Entra como `ACEITA` com o motivo escrito, e **o validador confere que a diferença entre as duas continua sendo só a propriedade**, para ninguém alargar o buraco enquanto ele espera.

### `Par` — a conta fechou em cima do alvo

A `Curta` (d6, `Par`, Força 0) contra a `Uma mão` (d8, sem `Par`, Força 1). O requisito não custa nada — nenhuma classe passa do teto da criação —, então **`Par` precisa valer exatamente a diferença de dado, ou a `Curta` está dominada**:

| | valor |
|---|---|
| alvo — o buraco d6 contra d8 | **0,33** por rodada |
| `Par` entrega, no d6 | **0,32** |

Melhor de dois no d6 dá 4,47 de média contra 3,50. **Erra por um centésimo, e não inventa mecânica**: é a mesma vantagem que a peça 11 já precifica e que a peça 4 §5 já garante que não empilha. E, principalmente, **não é ataque extra** — a trava da peça 6 §3 continua inteira, que é o que impede duas armas de virarem dois golpes.

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

### A matriz por valor total, e o que ela achou

*A primeira passada disse "zero classes dominadas". Ela media dado e propriedade; medindo o **total**, com o requisito de Força entrando como custo, aparecem duas coisas.*

**A primeira: o requisito de Força não é custo nenhum.** Nenhuma classe pede mais que 3, e 3 é o teto da criação (peça 2 §2). Quem investe Força paga zero por qualquer arma do catálogo — o requisito resolve **acesso**, que é o que a peça 5 §1 já tinha concluído. Só o Revestimento degrau 2 e 3 cobra marco.

**A segunda: `Uma mão` está dominada pela `Versátil`.** Mesmo dado, mesma mão livre, uma propriedade a mais, e o ponto de Força a mais não custa nada. Não existe situação em que se escolha a primeira.

> **E os dois dados da Versátil não consertam.** Testados `d8/d10`, `d8/d12` e `d6/d10`: em nenhum deles largar o escudo compensa, porque o ganho de dado é de 0,33 a 0,66 por rodada contra os 2,01 do escudo no nv16. A Versátil vira *Uma mão com um texto a mais* — e continua dominando a Uma mão, que não tem o texto.

**Sete das oito propriedades não têm texto nenhum.** Só `Duas mãos` é mensurável, via o escudo que ela impede. Por isso a matriz sai assim:

| pares suspeitos | veredito |
|---|---|
| 1 (`Uma mão` × `Versátil`) | **DOMINADA** |
| 15 | `INCONCLUSIVO` — a diferença mora numa propriedade sem número |

`Haste` e `Tiro pesado` perdem 0,60 por rodada para a `Pesada` em todo nível e só se salvam por `Alcance` e por `Distância · Munição`. **Se essas propriedades não valerem 0,60, as duas estão dominadas** — e hoje ninguém sabe quanto elas valem.

> **O item 9 do §8 não pode ser escrito antes disto.** Um validador de dominância por valor total precisa de valor, e sete oitavos do catálogo ainda não têm.

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
2. **Ferramenta amaldiçoada fica fora desta peça.** Decisão do Mizuki: canalizar energia já faz arma comum ferir maldição, e ferramenta amaldiçoada entra em tópico próprio, com graus e forja. A peça 5 §9 tem a pendência nomeada; a `Armaria` do Descendente e o `Enterrado` do Reencarnado a citam e são as primeiras a reler.
3. **As quatro vagas de Desliga da peça 13** que esperam equipamento — Descendente, Reencarnado, Corpo Amaldiçoado e Restrição Celestial. A peça 13 fecha dizendo *"quando equipamento fechar, a primeira coisa a fazer é voltar aqui"*.
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
5. **`Versátil`:** os dois dados não estão escritos, e a conta diz que **nenhum par resolve** — nem `d8/d10`, nem `d8/d12`, nem `d6/d10`. Largar o escudo nunca compensa enquanto o escudo for proteção. O par vira escolha de sabor depois que a forma do escudo fechar, não antes.
6. **Os nomes dos degraus de escudo, e quantos são.** A forma fechou — proteção, requisito de Força, teto de Destreza. Faltam os nomes e a contagem. Livres na triagem: **Broquel · Pavês · Rodela · Adarga · Tarja · Couraça · Guarda-Corpo**.
7. ~~**As sete propriedades sem texto.**~~ **Reduzidas a duas e meia na v0.42, e três delas eram a mesma coisa.** `Alcance`, `Distância` e `Arremesso` colapsaram em `Alcance` e `Longo Alcance`, as duas com número em metros em vez de redação. `Par` fechou em *"role dois dados de dano e fique com o melhor"*, 0,32 contra um alvo de 0,33. `Fineza` entrou. **Falta `Oculta`, os dois dados da `Versátil` e o número da `Munição`.**

   > **E o `0,60` daquela linha estava errado.** Com a fórmula que o §4 desta mesma peça fixou — `diferença de dado × 0,55 de acerto × 0,60 de uso` —, d10 contra d12 dá **0,33**. O `0,66` do §4 reproduz exato; o `0,60` do §5 só aparece se você tirar o fator de uso. **Duas fórmulas no mesmo documento**, e a segunda foi escrita sem o fator que a primeira tinha acabado de estabelecer.

   > **Mas o buraco de verdade não era o dado, e ele é 5× maior.** A peça 6 §3 é a única definição do golpe simples no projeto — *"arma + Força"* — e **não tem exceção para arma de tiro**. Como o acerto à distância soma Destreza (peça 1 §5), a arma de tiro acertava com um atributo e causava dano com o outro: **2,48 por rodada contra os 4,12 da Pesada, quando a matriz achava que a distância era 0,33.** É a lição nº 6 na direção de sempre — o preço usa um termo que existe, e ninguém foi ler a regra pendurada nele. *Resolvido pela categoria: `Yumi` soma Destreza, `Balestra` e `Arma de Fogo` não somam atributo nenhum e ganham dado maior.*
8. ~~**O teto de Defesa 20 não tem dono declarado.**~~ **Fechado na v0.42, e a resposta não era nenhuma das duas que esta linha oferecia.** O 20 é **derivado** de três números que já têm dono — `10` da peça 1 §5, o teto de atributo `6` e o teto de refino `10` da peça 2 §3, e a fórmula de cobrir-se da peça 11 §5. Zero parâmetros livres, então **ninguém escreve o número**: escrevê-lo em qualquer peça seria a lição nº 9, e medir uma checagem contra ele seria a nº 8. O que esta peça declara é o **invariante** — *nenhuma montagem de equipamento passa da Defesa que a rota sem equipamento alcança* —, e o validador deriva o teto dos três donos. Está no §3.

   > **E de passagem caiu a frase que sustentava o item:** o §3 dizia que as duas rotas topam em 20. Equipamento topa em **19**, e a diferença nasceu no §4, quando o escudo ganhou teto de Destreza. **Decisão do Mizuki: fica em 19**, agora como decisão e não como sobra.
9. **O validador.** Checagens que ele precisa ter: a régua do orçamento por classe; dominância **por valor total e uma vez por rota de proteção — e são TRÊS rotas, não duas** (cobrir-se · uniforme · **sem energia nenhuma**, que é a Restrição Celestial pelo ramo da Maki e não tem cobrir-se para desligar); a escada de proteção contra a peça 11; o requisito de Força contra a peça 2 — incluindo que **nenhum requisito passe do teto de criação sem que isso seja decisão escrita**; que **o teto de Defesa seja derivado dos três donos e nunca lido de uma constante**, com a busca exaustiva provando que nenhuma montagem de equipamento passa da rota livre; que a lista de situações do Traje passe na régua de três itens do §3, **inclusive a vaga aberta**, e que o Traje conceda **uma** situação e não uma por degrau;

   > **A dominância do escudo muda de resposta conforme a rota, e isso é novo.** O §4 provou que nenhum degrau é dominado — degrau 1 melhor em Destreza 4–6, degrau 2 em 2–3, degrau 3 em 0–1. **Aquela tabela foi rodada só na rota de cobrir-se.** Na rota do Revestimento o teto de Destreza já é 0, então o teto do escudo não custa nada e ele vira proteção pura: **o degrau 3 domina o 1 e o 2, sempre.** E `Revestimento 3 + escudo 3` dá 19 com Destreza **zero** — o melhor resultado do sistema em cinco das sete Destrezas, e empate na sexta. Isso não derruba a escada; ela continua certa na rota em que foi medida. O que muda é que a peça tem de dizer que **o degrau 3 é a resposta do Revestimento e o degrau 1 a de cobrir-se**, em vez de vender três opções para todo mundo. *É o furo que este item já previa acontecendo antes de o validador existir.* a busca exaustiva de uniforme × escudo × Destreza contra o teto de Defesa; que a frase do desligamento não cite escudo nos três documentos; **que nenhum item comum produza número** e que o teto de consumível por missão bata com as lutas de graça da peça 10; e que todo nome do catálogo, **propriedade inclusive**, passe na triagem — com `Alcance` e `Distância` entrando como `ACEITA` e não como erro.
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
