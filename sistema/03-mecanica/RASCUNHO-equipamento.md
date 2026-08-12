# RASCUNHO — Equipamento

**Não é peça.** Sem número na frente de propósito: meia peça não é peça, e um arquivo com dois dígitos quebraria a contagem do `conferir-repositorio.py`. Vira a peça 14 quando fechar, junto do validador dela — que ainda não existe e por isso não é citado pelo nome aqui.

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

| degrau | **Traje** proteção | teto de Destreza | **Revestimento** proteção | teto de Destreza | requisito de Força |
|---|---|---|---|---|---|
| 1 | 1 | — | 4 | 0 | **3** |
| 2 | 2 | — | 5 | 0 | **5** |
| 3 | 3 | — | 6 | 0 | **6** |

**Sem gate de nível.** O orçamento de atributo faz o trabalho sozinho: o teto da criação é 3, e Força 5 só chega no nv6, Força 6 no nv10. Medido:

| requisitos | degrau 3 abre no | acerto lá |
|---|---|---|
| 3 / 4 / 5 | nv6 | 40% — cedo demais |
| **3 / 5 / 6** | **nv10** | **45%** |

*O motivo de não haver gate de nível é do Mizuki, e é de mesa:* sistema de "Custo 1 a 4" travado por nível força o personagem parrudo a usar uniforme leve porque é o que ele pode pegar, e ninguém gosta disso. Orçamento de como conseguir o item entra depois, não como trava de nível.

**O cruzamento cai em Destreza 3, igual nos três degraus** — Revestimento ganha de 0 a 3, Traje ganha de 4 pra cima. Sem classe do meio, ninguém espremido.

**E as duas rotas topam no mesmo lugar:** no nv30 com Destreza 6, cobrir-se com refino 10 dá Defesa **20**, e Traje degrau 3 + escudo dá **20**. Uma paga com sete escolhas de marco; a outra com a mão ocupada. Isso caiu da régua, não foi calibrado.

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

## 5. Armas — o preço mora na classe

A peça 5 já provou que **o dado não é alavanca**: trocar d6 por d12 move três pontos numa lacuna de cem contra a coluna Rotina. Isso deixa o catálogo grande imune à armadilha clássica (*"o problema da longsword"*, opção-armadilha) — **porque a armadilha do hobby é sempre medida em dano.**

**A régua que fechou:** o preço é a **classe**, não a arma. O nome é sabor, e gêmea dentro da classe é de graça — decisão do Mizuki: *"não tem problema ter arma idêntica, tem vezes que a pessoa só quer um flavor diferente."*

| classe | Força mín | dado | propriedades | armas |
|---|---|---|---|---|
| **Oculta** | 0 | d4 | Oculta · Arremesso | Tanto, Punhal, Kunai, Shuriken, Tekko, Tessen, Canivete, **Faca** |
| **Curta** | 0 | d6 | Par | Sai, Tonfa, Nunchaku, Cassetete, Soqueira |
| **Uma mão** | 1 | d8 | — | Kama, Machete, Marreta, Machado, Taco, Wakizashi, Foice |
| **Versátil** | 2 | d8 | Versátil | Katana, Bastão, Espada Longa |
| **Haste** | 2 | d10 | Alcance · Duas mãos | Naginata, Corrente, Kusarigama, Yari, Bō, **Lança** |
| **Pesada** | 3 | d12 | Duas mãos | Odachi, Nodachi, Kanabō, Marreta de Obra, Machado de Bombeiro |
| **Tiro leve** | 1 | d6 | Distância · Munição · Oculta | Pistola, Revólver, Submetralhadora |
| **Tiro pesado** | 2 | d10 | Distância · Munição · Duas mãos | Espingarda, Rifle, Besta, Yumi |

**Oito classes, 41 armas** — eram 39 antes de `Lança` e `Faca` voltarem da triagem na v0.40.

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

### `Precisa` (Destreza no corpo a corpo) foi rejeitada, com conta

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
4. **Munição:** quantos tiros, e como recarrega. Nenhum número ainda.
5. **`Versátil`:** os dois dados não estão escritos, e a conta diz que **nenhum par resolve** — nem `d8/d10`, nem `d8/d12`, nem `d6/d10`. Largar o escudo nunca compensa enquanto o escudo for proteção. O par vira escolha de sabor depois que a forma do escudo fechar, não antes.
6. **Os nomes dos degraus de escudo, e quantos são.** A forma fechou — proteção, requisito de Força, teto de Destreza. Faltam os nomes e a contagem. Livres na triagem: **Broquel · Pavês · Rodela · Adarga · Tarja · Couraça · Guarda-Corpo**.
7. **As sete propriedades sem texto.** `Alcance`, `Distância`, `Par`, `Oculta`, `Arremesso`, `Versátil` e `Munição` são nome na tabela e nada mais. Enquanto forem, 15 dos 16 pares da matriz saem `INCONCLUSIVO` e `Haste` e `Tiro pesado` ficam a 0,60 de estarem dominadas pela `Pesada`.
8. **O teto de Defesa 20 não tem dono declarado.** A seção 3 derivou dele — *"caiu da régua, não foi calibrado"* — e agora a escada de escudos se apoia nele. Derivação virou invariante sem ninguém decidir, e isso é a lição nº 9 chegando pela porta de trás. **Ou a peça 1 adota o 20, ou esta peça declara que é dona dele.**
9. **O validador.** Checagens que ele precisa ter: a régua do orçamento por classe; dominância **por valor total e uma vez por rota de proteção**; a escada de proteção contra a peça 11; o requisito de Força contra a peça 2 — incluindo que **nenhum requisito passe do teto de criação sem que isso seja decisão escrita**; a busca exaustiva de uniforme × escudo × Destreza contra o teto de Defesa; que a frase do desligamento não cite escudo nos três documentos; **que nenhum item comum produza número** e que o teto de consumível por missão bata com as lutas de graça da peça 10; e que todo nome do catálogo, **propriedade inclusive**, passe na triagem — com `Alcance` e `Distância` entrando como `ACEITA` e não como erro.
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
