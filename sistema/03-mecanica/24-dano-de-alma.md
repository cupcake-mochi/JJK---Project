# Dano de alma e Integridade

**Fase 4, vigésima quarta peça.** A segunda barra: de onde vem o tamanho dela, o que a esvazia, o que ela arrasta junto, os quatro estágios, e o que a enche de volta.

*Fechada na v0.145, com o `conferir-alma.py` em cima dela.*

**Esta peça não inventa a máquina — ela recolhe uma que já estava rodando.** *A Integridade está em toda ficha desde o nível 1, os quatro estágios estão publicados no manual desde a v7.0, e o tipo de dano `Alma` é um dos catorze da peça 19.* **O que não existia era dono da régua**, e por isso as cinco partes divergiram sem ninguém acusar.

> **Nada aqui é batismo.** *`Integridade`, `Alma` e `Espírito` já são termos do sistema — a triagem devolve os três como ocupados ou dentro de termo maior, e é isso que se quer.* **Uma peça que recolhe não deve nomear nada de novo.**

---

## 1. O problema: a máquina existia partida em cinco

*Levantado por varredura antes de qualquer proposta.*

| pedaço | dono, até a v0.144 |
|---|---|
| a fórmula `20 + 8 × (nível − 1)` | peça 1 §5.1 |
| os quatro estágios | **o manual**, na seção 11 — peça nenhuma |
| **o acoplamento com a vida** | **o manual** — e nenhum documento do projeto citava ele |
| o tipo de dano `Alma`, um dos catorze | peça 19 §4 |
| a recuperação | peça 10 §2 |

**Cinco donos, e o do meio é o que decide tudo** — *"cada ponto de dano na alma tira 1 de vida, 1 de Integridade e derruba a vida máxima em 1"*. **Nenhuma peça do projeto repetia essa linha, e duas peças foram escritas supondo o contrário dela.**

### 1.1 Três coisas quebradas, e as três estavam publicadas

> **⚠⚠ 1 · O manual mandava rolar um Teste de Resistência que não existe.** *Ele nomeava a própria Integridade como se ela fosse um dos Testes de Resistência, e o livro publicava isso no capítulo 15.* **Este sistema tem quatro — Físico, Vigor, Intelecto e Espírito — e a Integridade não é nenhum deles: ela é reserva, e reserva não é modificador.** *O `conferir-manual.py` não pegava porque ele casa `Teste de Resistência de <atributo>`, e `Integridade` é palavra conhecida daqui.*
>
> **A decisão que resolve isso é da v0.7, e ela já dizia as duas metades:** *o dano de alma força o TR de Espírito, e a Integridade volta a ser só reserva.* **Cento e trinta e sete versões registrada e nunca aplicada em lugar nenhum.**
>
> *O nome morto **não** é repetido aqui de propósito — um `grep` não distingue citação histórica de afirmação viva, e a checagem 6 varre o projeto inteiro atrás dele.* **É a convenção que a v0.143 pagou para escrever.**

> **⚠⚠ 2 · O `Cisão` e o capítulo 15 diziam coisas opostas, no mesmo PDF.** *A peça 16 §4 escreve que o golpe dele `causa dano de alma **no lugar do** dano de vida`, e o livro completa: "contra alvo de alma dura, você vai sentir falta do dano normal".* **Pela regra do manual isso nunca foi troca** — era o mesmo dano de vida, **mais** a Integridade, **mais** a vida máxima. *O argumento preçado daquela peça — "é troca, não escada" — estava montado na leitura que o manual nega.*

> **⚠ 3 · *"a alma é maior que o corpo em quatro dos cinco Caminhos"* era uma frase de Constituição 3.** *Ela está na peça 1, neste projeto e na lista de playtest do `ESTADO-ATUAL`.* **A variável não é o Caminho — é a Constituição:** com Con `0` o estágio 4 não dispara em Caminho nenhum, e com Con `6` ele dispara nos cinco a partir do nível 10.

---

## 2. A Integridade passa a ter Essência dentro

***A decisão é da v0.70 e estava esperando esta peça:*** *"a Integridade vai escalar com Essência, virando uma segunda vida de verdade em vez de um número plano"*.

> ### `Integridade = 20 + (Essência + 5) × (nível − 1)`

**O `8` do manual se abre em `5 + 3`, e o `3` não é escolha: é o meio da escala `0–6` da peça 2 §1** — a mesma Constituição de referência que a peça 1 §5.1 e o `conferir-atributos.py` já usam para medir vida. ***Com Essência 3 esta fórmula É a fórmula publicada, em todo nível, sem uma unidade de diferença.***

| | nv 2 | nv 10 | nv 20 | nv 30 |
|---|---|---|---|---|
| Essência 0 | 25 | 65 | 115 | **165** |
| Essência 1 | 26 | 74 | 134 | 194 |
| **Essência 3** *(= hoje)* | **28** | **92** | **172** | **252** |
| Essência 6 | 31 | 119 | 229 | **339** |

### 2.1 As outras três formas foram medidas e reprovaram

| forma | nv30, Ess `0 · 3 · 6` | estágio 4 dispara | veredito |
|---|---|---|---|
| **`20 + (Ess+5)(nv−1)`** | `165 · 252 · 339` | **33,3%** da grade | **fica** |
| `20 + (Ess+8)(nv−1)` | `252 · 339 · 426` | `10,7%` | **reprova** — só sobe, nunca desce, e mata o estágio 4 |
| `(20+Ess) + (Ess+5)(nv−1)` | `165 · 255 · 345` | `31,4%` | perde: não reproduz a fórmula publicada em nível nenhum |
| `20 + 8(nv−1) + 8×Ess` | `252 · 276 · 300` | `19,2%` | **reprova** — vale `2,7×` no nível 2 e `1,19×` no 30: domina cedo e some tarde |

*A grade é `5` Caminhos × Constituição `0–6` × Essência `0–6`, nos níveis 2, 10, 20 e 30 — `980` fichas.* **A escolhida move a taxa de disparo do estágio 4 em `0,3` ponto percentual contra a fórmula plana.** *Ela não muda **quanto** o estágio 4 acontece; ela muda **com quem**.*

### 2.2 O `20` fica plano, e isso é afirmação

**Toda ficha nasce com a mesma alma.** *A Constituição entra na vida em dois lugares — no inicial do Caminho e no por-nível —, e a Essência entra num só.* **A diferença é de propósito: a vida inicial tem Caminho dentro e a Integridade não tem, porque um Caminho é treino e ninguém treina a alma com que nasceu.** *O que a Essência muda é como ela **cresce**.*

> **⚠ E é isso que segura a simetria de preço.** *No nível 30, `+1` de Constituição vale `+30` de vida — `1` no inicial e `1` por nível.* **`+1` de Essência vale `+29` de Integridade.** *A diferença de um ponto na campanha inteira é o inicial que a alma não tem, e ela é menor que o arredondamento de qualquer conta desta pasta.*

### 2.3 O cruzamento que a peça 1 prometeu

| ficha, nv 30 | corpo | alma, hoje | alma, agora | quem acaba primeiro |
|---|---|---|---|---|
| **Bastião** Con 6 · Ess 0 | `395` | `252` | **`165`** | a alma, e muito antes |
| **Bastião** Con 2 · Ess 1 *(a ficha da peça 8)* | `275` | `252` | `194` | a alma |
| **Emanador** Con 3 · Ess 3 | `212` | `252` | `252` | o corpo |
| **Emanador** Con 0 · Ess 6 | `122` | `252` | **`339`** | o corpo, com a alma intacta |

**É a imagem certa nos dois extremos, e ela é do Mahito:** *quem é duro demais para morrer de porrada fica de pé sem ser mais ele; quem é de alma grossa morre inteiro, com a alma sem um arranhão.*

### 2.4 O preço, e ele é real

**O degrau 2 chega em metade da Integridade, e ele faz todo feitiço custar `+1` PE por Classe.** *É a checagem 4 do `conferir-orcamento.py`, a mais apertada do projeto.* **Com a fórmula nova, quanto dano de alma até lá, no nível 30:**

| | dano de alma até o degrau 2 | contra hoje | acertos de `Sete Palmos` |
|---|---|---|---|
| Essência 0 | `82` | **`−34,5%`** | `2,7` |
| Essência 3 | `126` | `0,0%` | `4,1` |
| Essência 6 | `170` | **`+34,5%`** | `5,5` |

***Quem paga é o conjurador de Essência baixa*** — e ele existe, porque a v0.117 pôs o atributo da técnica na criação: a ficha da peça 8 conjura com Força. **O ganho do outro lado é do mesmo tamanho, e essa simetria é o que faz a fórmula ser eixo em vez de imposto.**

> **⚠ E o `conferir-orcamento.py` NÃO lê esta fórmula, nem antes nem depois.** *A checagem 4 dele modela "você está no degrau 2" e mede o bolso a partir dali.* **O acoplamento é de desenho e não de validador**, e vale escrever isso porque o contrário estava sendo suposto: mexer aqui não faz aquela checagem acender, então é esta peça que tem de medir o efeito — e é a checagem 4 **daqui** que faz isso.

---

## 3. O acoplamento com a vida, e a exceção

### 3.1 A regra geral vem da obra, e não da conta

> **Cada ponto de dano de alma tira `1` de vida, `1` de Integridade e derruba a vida máxima em `1`**, até o próximo descanso longo.

*Esta linha é do manual e ela fica, com o dono passando para cá.* **O motivo dela é canon:** na obra a alma vem antes do corpo — é a tese do Mahito, confirmada contra o Nanami —, e remodelar a alma reconfigura o corpo pendurado nela. **Derrubar a vida máxima junto é o corpo seguindo a alma, escrito em número.**

> *É por isso que a régua não é "uma segunda barra de vida".* **A alma não é a reserva reserva: ela é a de cima.**

### 3.2 A exceção: o que atravessa o corpo

**Existe dano de alma que ignora o corpo, e a obra é explícita sobre ele.** *A Katana de Alma Partida atravessa dureza física e reforço de energia amaldiçoada e bate direto na alma* — é o que o `Cisão` da peça 16 §4 reproduz.

> **Dano de alma que ATRAVESSA tira Integridade, e mais nada.** *Não tira vida, não derruba a vida máxima.* **Só um efeito escreve isso hoje, e é o `Cisão`.** *Todo o resto é a regra geral do §3.1.*

**A distinção precisa estar escrita porque as duas se chamam a mesma coisa**, e foi por não estar que a peça 16 e o capítulo 15 do livro passaram treze versões dizendo o oposto um do outro. *O GURPS 4e escreve exatamente esta linha para os Pontos de Fadiga — alguns ataques causam dano em PF **"em vez, ou além"** de PV —, e ele escreve porque as duas leituras existem em qualquer sistema com segunda barra.*

> **⚠⚠ E a exceção ENFRAQUECE o `Cisão`, o que é o que faz ela caber sem repreço.** *Pela regra geral, ele tirava a barra menor das duas mais a vida máxima; pela exceção, ele tira só a alma.* **Medido nos quatro arquétipos do §2.3 e no chefe do nível 30: a exceção nunca é mais rápida que a leitura 1:1 — ela é igual ou pior.** *Contra o Emanador de Essência 6 ela é `2,8×` pior.*
>
> ***Nenhum preço publicado se move.*** **O `Classe 3` daquela entrada sempre foi escrito para esta leitura** — o *"é troca, não escada"* da peça 16 §4 só é verdade aqui. *Consertar o vocabulário não repreça: devolve o preço que já estava lá.*

### 3.3 Quem não tem Caminho fica com a linha original do manual

> **Integridade de quem não é personagem jogador = a vida máxima dele.**

***E isto não é número novo: é a linha que o manual sempre teve*** — *"Integridade = vida máxima"*. **A peça 1 substituiu ela para o personagem, e o motivo está escrito lá: com Caminho e Constituição na vida, um corpo duro ganharia de graça uma alma dura.** *Um inimigo não tem Caminho e não tem Constituição — a vida dele é uma linha da tabela do manual. Então o motivo da substituição não o alcança, e a regra original continua valendo para ele.*

**Sem esta linha, o `Cisão` fica sem alvo contra inimigo**, que é a mesma forma do item aberto da peça 23 §9 sobre a Reação na ficha de inimigo. *Com ela, o `Cisão` contra o chefe do nível 30 é exatamente `1,0×` a velocidade de bater normal — ele não é atalho de dano.*

> **O que ele ganha contra inimigo são as outras duas coisas, e as duas são canon:** *ele atravessa redução e resistência, e ele empurra o chefe pelos quatro estágios.* **O estágio 3 dá desvantagem nos ataques do chefe**, e isso vale muito mais numa luta de `3,7` rodadas do que os `12` de dano do golpe.

---

## 4. Os quatro estágios

*A tabela é do manual e o dono passa para cá. Nenhum número mudou.*

| Integridade perdida | estágio | o que pega |
|---|---|---|
| `1/4` | **1** | desvantagem em testes de perícia |
| `1/2` | **2** | deslocamento pela metade, e todo feitiço custa `+1` PE por Classe |
| `3/4` | **3** | desvantagem em ataques e Testes de Resistência, e você não conjura acima de metade da sua Classe máxima |
| toda | **4** | você não é mais você — o que sobra é decisão do mestre |

**O estágio 4 é também o fim da janela do `Aguentar`**, da peça 1 §5.5. *Aquela seção ligou o fim da janela aqui na v0.37 para não inventar estado novo, e a ligação continua.*

### 4.1 O Teste de Resistência é o de **Espírito**

> **Ao levar dano de alma você faz um Teste de Resistência de Espírito contra a CD do atacante.** *Na falha, você avança um estágio na hora, mesmo que a fração ainda não tenha fechado.*

***Isso aplica a decisão da v0.7***, e ela nunca tinha sido aplicada. **A rolagem que o manual nomeava com o nome da própria reserva sai do sistema inteiro** — ela era uma quinta que a peça 1 §4 nunca teve, e a checagem 6 varre o projeto atrás dela pelo nome morto.

**E não é escolha: o Espírito é Essência, que é o atributo que dimensiona a barra.** *Essa é a mesma forma que a Constituição já tem deste lado — ela dimensiona a vida e é o atributo do TR Vigor.* **A alma ganha a estrutura que o corpo já tinha, e não uma nova.**

> *O GURPS resolve igual, e é o parente estrutural mais próximo:* **a HT dimensiona os Pontos de Fadiga e a HT é o teste que se rola contra fadiga e doença.** *Um atributo dimensionando uma reserva e rolando por ela é a forma padrão, não acúmulo.*

---

## 5. A recuperação

| | descanso curto | descanso longo |
|---|---|---|
| **Integridade** | — | **cheia, e os estágios limpam** |
| **a vida máxima derrubada** | — | **volta junto** |

> **⚠ E esta é a única parte da máquina que NÃO muda de dono.** *A peça 10 é dona da tabela de descanso inteira — PE, vida, exaustão e Integridade na mesma grade —, e mover uma linha dela para cá criaria a segunda fonte que a lição nº 9 existe para evitar.* **A tabela acima é ponteiro, e a peça 10 §2 é quem manda.**

**A Integridade volta inteira em qualquer lugar**, e a peça 10 §2 já escreve o motivo: o ambiente propício socorre o corpo, e a alma não é o corpo.

**Cura comum não devolve o que a alma perdeu.** *Só o descanso longo, ou a Melhoria `Remenda` do manual, que é o que o `Alinhavo` usa.* ***E isso também é canon:*** *ferimento da Katana de Alma Partida não fecha com Energia Reversa a menos que o alvo enxergue os contornos da própria alma.* **O manual já estava certo aqui, e vale registrar que estava.**

---

## 6. O que esta peça NÃO faz

### 6.1 O `recuperar Integridade` da peça 5 continua reprovado

**A peça 5 §4 carregava, desde a v0.70, um bilhete prometendo que esta linha poderia voltar a valer quando a Essência entrasse na Integridade.** ***Medido: ela não volta***, e o bilhete foi corrigido nesta versão em vez de continuar prometendo.

*O motivo do veto era que o corpo acaba antes em `três das quatro` fichas, o que torna a entrega inútil para a maioria dos alvos.* **Com a Essência dentro, a alma é a barra menor em `33,3%` da grade contra `33,6%` antes** — a fração não se moveu. *O que mudou foi **quem** está nela: antes era quem investiu Constituição, por acidente; agora é quem não investiu Essência, de propósito.*

> **A entrega continua valendo `0,00` para dois terços dos alvos, e é isso que a reprova** — a mesma família que matou o `recuperar ferimento` e a Passiva `Casca`. **O bilhete da peça 5 foi corrigido para dizer isso**, em vez de continuar prometendo uma reabertura que a conta não sustenta.

### 6.2 Os onze `Estigma` continuam sem preço uns contra os outros

*A dívida é da v0.144 e não é desta peça.* **O `Cisão` não foi repreçado aqui, e o §3.2 mostra por quê: a mudança de vocabulário só o enfraquece.** *Preçar os onze exige um modelo que documento nenhum é dono, e enfiar esse modelo num validador seria a lição nº 8 pelo avesso.*

### 6.3 A Cicatriz continua sem mecânica

*A peça 1 §5.5 registra a dívida desde a v0.37, e ela esperava a peça de dano e condições — que chegou na v0.103 e não a fechou.* **Esta peça também não fecha, e o motivo é de recorte:** *a Cicatriz é consequência de cair a `0` de vida, e não de dano de alma.* **Ela é da peça 1, e o que faltava nunca foi a régua da alma.**

---

## 7. O que o validador confere

*Escrito antes do `conferir-alma.py`, no molde do §5 da peça 15.* **Nenhum valor mora dentro dele — todos são lidos do documento dono.**

| # | a checagem | o dono do número |
|---|---|---|
| **1** | a fórmula publicada aqui reproduz a fórmula plana **exatamente** em Essência `3`, em todo nível de 1 a 30 | esta peça §2 e a peça 1 §5.1 |
| **2** | o `3` de referência é o **meio da escala de atributo**, recalculado de `teto ÷ 2`, e não escrito | peça 2 §1 |
| **3** | `+1` de Essência e `+1` de Constituição valem a mesma coisa nas respectivas barras, dentro de `1` ponto na campanha | peça 6 §5 e esta peça §2 |
| **4** | a taxa de disparo do estágio 4 sobre a grade de `980` fichas **não cai** contra a fórmula plana | derivada |
| **5** | os quatro estágios daqui batem com os quatro do manual, linha a linha | **o manual**, seção 11 |
| **6** | o TR do dano de alma é um dos **quatro** que a peça 1 §4 declara, e `Integridade` não é nenhum deles | peça 1 §4 |
| **7** | **exatamente uma** entrada do projeto declara a exceção que atravessa o corpo, e ela é o `Cisão` | peça 16 §4 |
| **8** | a exceção nunca mata mais rápido que a regra geral, nos quatro arquétipos e no chefe | derivada |
| **9** | quem não tem Caminho usa `Integridade = vida máxima`, e a linha existe escrita | esta peça §3.3 |
| **10** | a Integridade da ficha de exemplo da peça 8 é a fórmula aplicada à Essência **daquela ficha** | peça 8 |
| **11** | a recuperação daqui e a da peça 10 §2 dizem a mesma coisa | peça 10 |

> **A checagem 4 é a que esta peça existe para ter.** *Ela é a única que mede a consequência da mudança em vez de conferir uma cópia* — se alguém mexer no `5` ou no `3`, a fórmula continua bem-formada e o estágio 4 some da campanha sem nenhuma outra checagem acusar.

---

## 8. Em aberto

**Três coisas, e nenhuma trava o playtest.**

1. **O inimigo não tem linha de Integridade na tabela do manual.** *O §3.3 resolve por derivação — é a vida máxima dele —, então nada fica indefinido.* **O que falta é a tabela imprimir a coluna**, no mesmo padrão do ambiente propício: valor sugerido por nível, palavra final do mestre. *Mesma forma do item aberto da peça 23 §9.*
2. **A Essência passa a fazer cinco trabalhos.** *Integridade, TR Espírito, sete perícias, Pactos, e é candidata a atributo da técnica.* **A Constituição faz dois.** *O `ESTADO-ATUAL` já marcava esse desequilíbrio para o playtest antes desta peça; ela põe o quinto, e o registro tem de dizer isso em vez de deixar a conta parecer neutra.*
3. **Quanto o estágio 3 vale contra um chefe.** *Desvantagem nos ataques dele numa luta de `3,7` rodadas é grande, e ninguém mediu.* **É o que decide se o `Cisão` está barato**, e ele encosta na dívida de preço dos onze `Estigma`.

---

## 9. Levantamento externo

*Quatro sistemas com segunda barra, lidos no texto de regra e não em resumo.*

| sistema | a barra | tamanho vem de | acoplamento com o corpo |
|---|---|---|---|
| **GURPS 4e**, p. 16 e 328 | Pontos de Fadiga | **um atributo (HT)** | *"alguns ataques causam dano em PF, **em vez, ou além**, de PV"*; a perda de PV só liga em `0 PF`, e aí é `1` PV por PF |
| **Call of Cthulhu 7e** | Sanity | POW, com **teto** `99 − Mythos` | nenhum — e o que cai de vez é o **teto**, não o valor |
| **D&D 5e, Guia do Mestre** *(opcional)* | Sanidade | **um sexto atributo**, com TR próprio | nenhum — loucura longa ou permanente corrói o próprio valor em `1` |
| **D&D 5e 2024** | Exaustão | nada: contador `0` a `6` | nenhum — pega teste de d20 e deslocamento, e mata em `6` |

**O GURPS é o parente estrutural, e ele decide duas coisas desta peça.** *A primeira é o §4.1: um atributo dimensiona a reserva **e** é o que se rola por ela, e lá isso é a forma padrão e não acúmulo.* **A segunda é o §3.2: ele escreve "em vez, ou além" com todas as letras**, porque as duas leituras existem em qualquer sistema com segunda barra e nenhuma delas é a óbvia.

**E os outros três resolveram DIFERENTE do que esta peça faz, o que é o motivo de estarem aqui.** *Nos três a segunda barra não toca o corpo em nada* — a consequência é loucura, condição ou morte, nunca dano. **Aqui ela toca, e a razão não é de sistema: é que na obra a alma vem antes do corpo.** *Copiar a forma dos três importaria um dano de alma que não é o da obra.*

> **⚠ E o que a Call of Cthulhu resolve e este sistema não é o TETO que cai.** *Lá, conhecer o Mythos derruba de vez o máximo de Sanidade.* **Aqui a vida máxima cai e volta no descanso longo, e a Cicatriz — que seria a candidata a perda permanente — continua sem mecânica.** *Se um dia alguém quiser perda que não volta, o desenho está lá e é barato de ler.*
