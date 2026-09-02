# Bloquear

**Fase 4, vigésima terceira peça.** Rolar para se defender. O dado, por que ele não é o d20, os dois extremos, o invariante que segura tudo, e quem não pode usar.

*Fechada na v0.143, com o `conferir-bloquear.py` em cima dela. O desenho é da **v0.43** e não mudou uma linha — o que mudou foi o estatuto.*

**Ela nasceu como regra opcional e deixou de ser.** ***Decisão do Mizuki na v0.143:*** *"Bloqueio pode ligar, é uma mecânica que o jogador pode TOMAR, na hora que for receber um ataque, é uma mecânica real, não uma opcional."* **Bloquear é de todo mundo, vale em toda mesa, e não existe versão do sistema sem ele.**

> **A Defesa continua sendo `10 + Destreza + proteção`, e ela continua sendo o número parado da ficha.** *Peça 1 §5.* **Esta peça não muda número de peça nenhuma** — ela acrescenta uma segunda forma de usar o mesmo número, e a seção 5 é o que prova que as duas são a mesma coisa na média.

*A regra mora aqui e é publicada no **capítulo 1** do livro, colado na Defesa. **As duas coisas são de propósito**: o livro é organizado para quem lê pela primeira vez, e a peça é organizada por quem é dono de quê. Não junte esta peça na peça 1 — aquela é dona da fórmula, e uma peça dona de fórmula não deve carregar variante dentro dela.*

---

## 1. O pedido, e por que a resposta óbvia está errada

A maioria dos jogadores quer **rolar para se defender**. É um pedido velho e comum, e a resposta padrão do hobby — *"role d20 mais os modificadores da sua Defesa no lugar dos 10"* — está errada por um motivo aritmético.

> **`E[d20] = 10,5`, e a base da Defesa é `10`.**

Rolar dá **`+2,5` pontos percentuais de graça, em todo ataque, para todo mundo**. A house rule é praticada há décadas com um bônus escondido dentro dela.

E isso reprova pelo critério da casa: *"enumere as montagens legais e conte quantas ganham o bônus. Perto de 100%, não é bônus."* Custando zero, ninguém nunca deixa de rolar. **Não é escolha; é a Defesa subindo meio ponto com uma rolagem colada nela.**

### 1.1 Três saídas que não servem, e o número de cada uma

*Registradas porque as três parecem óbvias, e alguém vai propor cada uma delas de novo.*

**Cobrar a Reação.** A Reação de cobrir-se já dá Redução de Dano de `1,5 × refino` por `2` PE, pela peça 11 §6. O bloqueio evita `2,5%` do golpe. Ela perde de **`8×` a `12×`** em todo nível — vira letra morta. *E a janela é estreita dos dois lados: de graça vira automático, com preço vira nunca. Não existe preço intermediário, porque a Reação é o único espaço defensivo do sistema.*

**Risco no fracasso — dano extra se o bloqueio falhar.** O dano extra que **equilibra** é `5,26%` do golpe: `1,9` de dano no nível 14. A proposta que estava na mesa era *"nível em dano"*, que é de **`7×` a `8×`** maior, e faz bloquear ficar de `28%` a `35%` **pior**. A opção morre. *O buraco não tem ponte: qualquer penalidade grande o bastante para dar medo já mata a opção, porque a vantagem que ela precisa cancelar é `2,5` pontos percentuais e mais nada.*

**Penalidade cumulativa por bloqueio na rodada**, no molde do `−20%` do RuneQuest. Traduzida para d20, `−1` por bloqueio extra: o primeiro vale `+2,5pp` e **o segundo já vale `−2,5pp`**. É *"uma vez por rodada"* com outro nome, e o pedido era justamente valer em ataques múltiplos.

## 2. A saída: o dado da defesa não precisa ser d20

**Qualquer dado de média `10` é neutro por construção** — sem penalidade escrita, sem custo, sem teto por rodada, sem Reação:

| dado | média | desvio | acerta no parelho | contra o estático |
|---|---|---|---|---|
| `1d20` | `10,50` | `5,77` | `47,5%` | **`+2,5pp`** |
| **`2d10−1`** | **`10,00`** | `4,06` | **`50,0%`** | **`0,0pp`** |
| `2d8+1` | `10,00` | `3,24` | `50,0%` | `0,0pp` |
| `2d6+3` | `10,00` | `2,42` | `50,0%` | `0,0pp` |
| `4d4` | `10,00` | `2,24` | `50,0%` | `0,0pp` |

### 2.1 Por que dois dados, e não um d20 ajustado

**A média de um dado único sempre termina em `,5`**, porque é `(N+1)/2`. A base da Defesa é inteira. Então o buraco é de **meio ponto**, e não existe modificador inteiro que o feche: `d20` dá `+2,5pp` e `d20−1` dá `−2,5pp`, sem nada no meio.

**`2d10` tem média `11` — inteira.** O `−1` fecha exato. É por isso que a família de dados neutros só aparece com dois dados ou mais.

*Varridas `11 × 9 = 99` combinações de modificador de Defesa contra bônus de ataque: todas idênticas ao estático, ao ponto flutuante.*

### 2.2 E `2d10` na base `10` é a única configuração que fecha

***Medido no arnês da v0.143, e foi um contra-teste que reprovou.*** *A ideia era provar que a checagem 1 mede uma relação e não o `2d10` — mudando a base para `12`, o dado para `2d12` e o offset para `13`, tudo coerente, ela deveria ficar verde.* **Ela acendeu, e estava certa.**

| dado | média | faixa | base | deriva |
|---|---|---|---|---|
| **`2d10`** | `11` | `2` a `20` | `10` | **`+0,0000`** |
| `2d12` | `13` | `2` a `24` | `12` | `+0,0007` |
| `2d4` | `5` | `2` a `8` | `4` | `−0,0375` |

**A média certa não basta: a faixa do dado tem de caber na do `d20`.** *O `2d12` tem média `13`, que é exatamente `base + 1` — e enviesa mesmo assim, porque `21`, `22`, `23` e `24` são resultados que o `d20` não alcança de jeito nenhum.* **O `2d4` enviesa pelo lado contrário, por ser estreito demais.**

> ***Consequência de método:*** *a checagem 1 não pode ser enganada por mudança coerente, porque **não existe** segunda configuração coerente.* **O que prova que ela não é trivialmente verdadeira são as três perturbações independentes — dado, base e offset —, cada uma acendendo sozinha.** *Está registrado aqui para ninguém tentar o mesmo contra-teste de novo e concluir que a checagem está errada.*

### 2.3 E o `−1` não aparece na mesa

`2d10 − 1 + Destreza + proteção` é o mesmo que **`2d10 + (Defesa − 11)`**. A ficha é gerada por código, então ela imprime a linha pronta e o jogador lê um número:

> **`Defesa 17 · Bloquear 2d10+6`**

Na mesa vira *"role `2d10+6`"*, que tem o mesmo atrito de *"role `d20+7`"*. **A ficha é obrigada a imprimir as duas**, e a seção 8 é quem confere.

E a regra declara a própria neutralidade, o que resolve o *"nem pode parecer vantajoso"* sem pedir que ninguém confie numa planilha:

> **A média de `2d10` é `11`. Você troca os `11` que a sua Defesa já supõe por dois dados. Na média, dá exatamente a sua Defesa.**

## 3. A regra

> **Ao ser atacado, você pode Bloquear:** role **`2d10 + (a sua Defesa − 11)`** e use esse valor no lugar da sua Defesa contra aquele ataque.
>
> **Duplo 10 — Aparar.** O ataque não acerta. Você pode gastar a sua **Reação** para atacar o agressor imediatamente, e esse ataque sai com **`+3` de dano**.
> **Duplo 1 — Brecha.** O ataque acerta. O agressor pode gastar a **Reação dele** para atacar você de novo, imediatamente, sem bônus.
>
> **O Aparar não anula um `20` natural.** Crítico fura guarda.
> Bloquear não custa nada, não gasta a sua Reação, vale contra qualquer ataque com rolagem de acerto, **não vale em Teste de Resistência**, e é de todo mundo — jogador e inimigo.

**O crítico não muda em nada.** O atacante continua rolando `d20`, então *"`20` natural numa rolagem de acerto"* segue intocado: `5%`, dobra os dados, zero texto novo. *Isso é vantagem desta rota sobre virar a rolagem para o jogador, que obrigaria a mudar a casa do crítico.*

*E a trava do `20` natural sai de graça:* com ela, o multiplicador vai de `0,5490` para **`0,5500` exato** — ela **paga** a neutralidade que faltava, em vez de custar.

### 3.1 Os dois extremos, e por que os dois gastam Reação

*A ideia é do Mizuki e ela vem do For Honor: recompensar quem apara, punir quem não apara direito.* **Os dois lados pagam o próprio espaço, e os dois podem recusar** — é isso que traz o peso do *"eu realmente bato?"*, e o inimigo pensa igual, porque Reação também é recurso dele.

**A régua do ataque de oportunidade já existe** — peça 3 §2, *"você pode gastar a sua Reação para atacar"* —, então nenhum dos dois inventa mecânica.

### 3.2 Por que `+3`, e não `+6` nem metade do nível

**Primeiro, onde a decisão existe.** A Reação só custa alguma coisa se **outro golpe vier na mesma rodada** — se você aparou o único golpe do turno, ela não tinha outro emprego.

| cenário | o ataque de oportunidade rende | a Reação custa | é decisão? |
|---|---|---|---|
| chefe sozinho, qualquer nível | `6,9` | `0,0` | não — sempre aceita |
| chefe mais capanga, nível 6 e 14 | `5,8` a `6,9` | `3,0` a `6,0` | não — sempre aceita |
| **chefe mais capanga, nível 22 e 30** | `6,9` | `9,0` a `12,0` | **sim, e pesa** |

**Segundo, o que o bônus compra e o que ele destrói:**

| bônus | o seu ataque de oportunidade no nível 30 | líquido do pacote | a decisão do nível 22 |
|---|---|---|---|
| **`+3` fixo** | `8,53` | **`0,89%`** | **sobrevive** |
| `+25%` | `8,59` | `0,89%` | sobrevive |
| metade do nível | `15,13` | `0,80%` | **morre** |
| o nível inteiro | `23,38` | `0,70%` | **morre** |

**Fixo e percentual empatam, e o motivo é que o golpe simples quase não cresce:** o dado é fixo e a Força trava em `6`, então o dano vai de `9,5` no nível 2 a `12,5` no nível 14 e para ali. `+25%` disso é **sempre `2,4` a `3,1`** — o `+3` é o mesmo número, sem conta de porcentagem na mesa.

**Quem manda no teto é o nível 22:** é lá que a Reação vale `9,00` contra os `6,88` do ataque de oportunidade base, e a folga é `2,12` de dano esperado. *Um ponto de bônus só rende quando o contra-ataque acerta, então em dano cru ele vale `2,12 ÷ 0,55`:* **o teto do bônus é `3,85` de dano cru.** **`+3` cabe com `0,85` de margem; `+4` estoura por `0,15` e a decisão morre.**

> **⚠⚠ Estes dois números estavam errados no rascunho desde a v0.43, e a checagem 4 os pegou na primeira rodada.** *Aquele texto escrevia **"a folga é `3,86`"** logo depois de dizer `9,0` contra `6,88` — e `9,00 − 6,88` dá `2,12`.* **Ele estava chamando de "folga" duas grandezas diferentes:** *a subtração, que é `2,12` de dano esperado, e o teto do bônus, que é a mesma coisa dividida pela taxa de acerto e dá `3,85` de dano cru.* **A conclusão nunca esteve errada — `+3` continua sendo o maior que cabe.** *O que estava errado era a aritmética escrita ao lado dela, e ela sobreviveu cem versões porque ninguém tinha um validador que subtraísse.*
>
> **A tabela expõe uma troca que vale registrar:** bônus maior deixa o **líquido** mais perto de zero — `0,89%` para `0,70%` —, porque compensa o golpe maior do inimigo, **e mata a decisão.** *As duas coisas correm em sentidos opostos, e o critério que decidiu foi o do Mizuki:* **"tem que custar Reação pra vir aquele peso de 'eu realmente bato?'"**

**E o bônus fica só no Aparar, não nos dois lados.** Se ele valesse para o inimigo também, amplificaria a assimetria — o golpe dele é maior e levaria a mesma porcentagem, e o custo do pacote subiria de `0,43%` para `1,17%`. *A assimetria também é mais fiel à fonte: no For Honor o parry garante um golpe pesado, e a guarda aberta do oponente só dá uma abertura comum.* **Aparar é perícia recompensada; Brecha é você exposto.**

### 3.3 O que o pacote custa, somado

**Os dois extremos não têm a mesma chance, e a diferença é a própria trava do §3:**

| | chance | por quê |
|---|---|---|
| **Aparar** | `0,95%` | duplo `10`, **menos** o `20` natural, que fura a guarda |
| **Brecha** | `1,00%` | duplo `1`, e nada cancela ela |

| | líquido por golpe recebido, nível 30 | contra o golpe do chefe |
|---|---|---|
| Bloquear puro, sem os extremos | `0,000` | **`0,00%`** |
| **com Aparar e Brecha, a `+3`** | `−0,649` | **`0,89%` do golpe do chefe** |

**Menos de um por cento**, e ele **cresce com o nível**, porque o seu golpe simples trava em `6,9` quando a Força chega a `6` e o do chefe continua subindo. *Isso é a lição nº 1 aparecendo pequena: fica registrado para ninguém se assustar.* **A checagem 3 recalcula o líquido do nível 30 a partir dos donos e falha se ele passar de `1%` do golpe do chefe.**

> **⚠ O denominador está declarado, e até a v0.142 ele não estava.** *O rascunho publicava `0,43%` "do golpe", sem dizer de que golpe — e a conta só fecha com um `36` que não aparece em documento nenhum do projeto.* **Aqui o denominador é o golpe do chefe, `73,00`, que a peça 19 §2.2 publica como `219` de dano por rodada em `3` ações.**
>
> **⚠ Ele era `24,00` até a v0.200, e a v0.201 triplicou a linha de inimigo do manual.** *O líquido subiu junto — de `−0,159` para `−0,649` —, e o teto declarado de `1%` do golpe continua com folga: `0,89%`.* **Nenhuma peça do `Bloquear` foi repreçada; o que mudou foi o denominador.** *E a checagem 3 falha se a peça parar de declarar contra o quê a porcentagem é medida.*
>
> **E a mudança de `0,154` para `0,159`, na v0.142, foi a correção das duas chances acima:** *aquele número supunha `1%` dos dois lados, e o Aparar é `0,95%`.* **A direção não muda, o tamanho não muda de ordem, e o teto de `1%` continua com folga.**

### 3.4 A Reação do inimigo é a mesma de todo mundo, e agora ela está impressa

**A `Brecha` só existe se o inimigo tiver uma Reação e se ela for gasta de verdade.** *A regra sempre deu uma a ele — a peça 3 §3 escreve `uma, e ela volta no começo do seu turno` para o slot inteiro, e o §3 desta peça diz que Bloquear `é de todo mundo`.* **O que faltava não era o número: era o lugar de marcar.** *Fechado na v0.159, na seção `Inimigos` do manual, que é onde o mestre monta inimigo.*

> **Não é valor por nível, e isso não é escolha.** *A quantidade é a mesma do nível 2 ao 30 porque o slot é o mesmo* — **uma linha por nível repetindo `1` seis vezes seria coluna sem conteúdo.**

***E o chefe não ganha uma segunda por ter três ações.*** *A tentação existe: a peça 19 §2.1 modela o chefe em `3` ações por rodada, e pelo formato ele pareceria ter direito a três Reações.*

**Ela custaria caro:** *o ataque dela sai por cima dos `72` de dano por rodada que a tabela de inimigo do manual publica*, **e o dono daquela tabela é o playtest.**

**E ela compraria quase nada.** *O único gatilho com taxa medida é a `Brecha` — `1,00%` por rolagem de Bloquear, e o §9 prevê `16` rolagens por combate.* **Dá `0,16` disparo por combate.**

**Uma Reação por rodada nunca acaba contra `0,16` disparo por combate.** *A segunda compraria um caso que quase não acontece e pagaria com o número que preça as treze condições da peça 19.* **Então é uma, e ela é a mesma que a peça 3 dá a qualquer ficha.**

> *A checagem 8 mede isso como **relação**, e não como o `1`:* **ela lê a quantidade da peça 3 §3 e a do manual e falha se as duas divergirem.** *Trocar as duas juntas sai verde de propósito — é o contra-teste que prova que ela não está medindo a decisão de hoje.*

## 4. O invariante que segura tudo: o modificador é UM só

> **Bloquear usa exatamente o mesmo modificador da Defesa passiva. Nada pode aumentar um sem aumentar o outro.**

*Decisão do Mizuki, e ela é o que impede a mecânica de apodrecer com o tempo.*

A neutralidade inteira depende de `média(2d10) = 11` bater com a base `10` mais o mesmo modificador dos dois lados. **Se um escudo, uma aptidão, um Legado ou um item desse `+1` na Defesa e não no Bloquear — ou o contrário —, o jogador passaria a escolher pelo número em vez de escolher pelo gosto**, e a regra viraria exatamente a coisa que ela existe para não ser.

E o buraco é grande: **`+1` de diferença vale `2,5` pontos percentuais**, que é o tamanho do viés do d20 que esta peça inteira saiu para consertar. Um único item mal escrito desfaz tudo.

**Isso é checagem do validador, não confiança:** ele lê o modificador dos dois e falha se as duas expressões não forem a mesma. Não *"os dois somam `7`"* — a **mesma expressão**, porque valores iguais hoje divergem amanhã, e isso é a lição nº 9.

> **⚠ A única coisa do sistema que mexe num lado só é a propriedade de arma `Talha`, e ela não viola o invariante.** *Ela dá `−1` no Bloquear de quem se defende.* **O invariante fala do modificador do DEFENSOR; a `Talha` é do atacante e não toca em modificador nenhum do defensor.** *A seção 6 é dona dessa fronteira.*

## 5. Quem não pode Bloquear — e a resposta é derivada

**Só o `Incapacitado`.** *E ele já dizia isso, com todas as letras, desde a peça 19.*

**A pergunta ficou cem versões em aberto** — o rascunho listava *"surpreendido, caído, agarrado, sem ver o agressor"* como candidatos, e chamava isso de *"a única peça do desenho que ainda não tem forma"*. **Ela não precisava de forma: a peça 19 §3.4 já tinha decidido, por outro caminho.**

| condição | o eixo que ela ataca |
|---|---|
| **`Atordoado`** | tira **parte do turno** — uma Ação Padrão e a reação. Você continua se defendendo |
| **`Incapacitado`** | não tira turno nenhum: tira a **defesa**. Você age e não se protege |

***O `Incapacitado` é a condição cujo eixo É a defesa.*** **Deixar uma segunda condição desligar o Bloquear borra esse eixo** — e a decisão do Mizuki na v0.95, que separou `Atordoado` de `Incapacitado` justamente para as duas não se aninharem, seria desfeita por acidente.

**E a alternativa tem preço, que é o argumento definitivo.** *Pôr "você não pode Bloquear" no `Derrubado` ou no `Agarrado` acrescenta entrega a uma condição que já tem preço publicado na régua da peça 19* — `8,45` e `5,40` de dano por rodada. **Isso não é escrever uma regra: é repreçar duas condições, e a régua das treze não aceita entrega nova sem passar pela banda.**

> **A checagem 5 do validador confere que nenhuma outra das treze cita `Bloquear`.** *Ela existe porque a próxima pessoa que ler o rascunho antigo vai querer acrescentar a segunda, e o texto dela some sem ninguém acusar.*

### 5.1 E o preço do `Incapacitado` não se move

**A metade dele que dependia de regra opcional passa a valer sempre — e ela continua valendo praticamente zero.** *A peça 19 §2.2 é a dona do preço dela, e ele é inteiro a metade do crítico.*

**Medido por enumeração completa das `2.000` combinações, num chefe de nível 30:** a metade do Bloquear vale **`+0,02` de dano por rodada**, e o `Incapacitado` iria para `4,97`. *Abaixo da precisão que a régua carrega — o golpe simples que entra nela varia `3,0` entre o nível 2 e o 30.* **O número publicado fica em `4,95`.**

> **⚠⚠ Este número é da peça 19, e ele mora aqui como cópia — foi a v0.151 que descobriu isso do jeito caro.** *Aquela versão repreçou o `Incapacitado`, os 24 validadores saíram verdes, e esta peça continuou publicando o valor velho em dois lugares.* **Nenhuma checagem comparava as duas cópias.** *Hoje a sub-checagem `1.1` lê o valor da peça 19 e falha se esta peça publicar outro — lição nº 9, no número que esta peça existe para sustentar.*

***Mas o argumento embaixo dele muda, e essa é a parte que importa.*** *Até a v0.142 a peça 19 justificava o zero assim: "depende de uma regra opcional que nem toda mesa liga".* **Com o Bloquear ligado, o motivo verdadeiro aparece, e ele é mais forte:**

> **A metade do Bloquear vale zero porque o Bloquear é NEUTRO por construção, e não porque alguma mesa o desliga.**

*Tirar de alguém uma rolagem cuja média é exatamente o número que ela substitui não tira nada.* **O que sobra são os dois extremos de `1%`, e eles quase se cancelam.**

**A peça 19 passou a apontar para cá em vez de repetir a conta.** *Ela precisa saber que o Bloquear é neutro; ela não precisa saber a geometria dele.* **Quem prova a neutralidade é a checagem 1 desta peça** — e se um dia o dado mudar, o zero para de ser de graça e é aqui que acende.

## 6. A `Talha`, e a dívida que ela carregava

**A peça 14 §5.2 tem uma propriedade de arma que custa `1` ponto e só existe por causa desta peça:**

> **`Talha`** — a arma é ruim de bloquear: `−1` no Bloquear de quem se defende.

*Ela foi escrita na v0.45, e nasceu com uma dívida escrita ao lado, para não sumir:* **"Bloquear é regra opcional. Numa mesa que não a use, a `Talha` vale zero — e a arma pagou `1` ponto por ela."**

***A dívida está paga.*** **As nove armas que carregam `Talha` passam a receber o que compraram, em toda mesa.** *`Rapieira` · `Odachi` · `Maça` · `Marreta` · `Kanabō` · `Machado de Guerra` · `Foice` · `Yari` · `Rifle`.*

> **A checagem 7 do `conferir-equipamento.py` muda de pergunta, e não some.** *Ela nasceu perguntando **"alguma arma depende só de uma regra que a mesa pode desligar?"***, e essa pergunta deixou de ter sentido. **A pergunta que fica é a que sempre importou por baixo dela:** *nenhuma arma pode ter a `Talha` como única propriedade paga sem que isso seja decisão declarada* — porque uma arma cuja identidade inteira é `−1` num número alheio é uma arma sem identidade própria. *A `Maça` e o `Kanabō` continuam declarados, por decisão do Mizuki na v0.48: eles **são** as armas anti-guarda.*

## 7. O que ela custa, e não é balanceamento

**Tempo de mesa, e é a objeção documentada número um** contra defesa ativa em qualquer sistema. Uma rolagem a mais por golpe recebido — cerca de `16` num combate de quatro rodadas com quatro personagens. Ela não some; ela só deixa de ser paga por um bônus escondido.

**A galera vai rolar sempre, e a conta diz por quê:**

| o que o jogador vê | chance |
|---|---|
| **Aparar** — história boa | `0,95%` |
| **Brecha** — história ruim | `1,00%` |
| o dado mudou o resultado, sem extremo | `14,5%` |
| nada aconteceu, rolou por rolar | **`83,5%`** |

Dois eventos de cerca de `1%` que são os mais memoráveis da mecânica, e `83,5%` de rolagens que não mudam nada. **Vão rolar por loteria, não por vantagem** — e isso foi decidido de olhos abertos: *"vai fazer a galera querer rolar mais que defender passivo? Vai, mas é um flavor que eu acho que vale a pena."*

**E é o primeiro dado não-`d20` do sistema.** Isso é uma exceção real num jogo que rola `d20` para tudo o mais, e o preço dela é de aprendizado, não de matemática.

### 7.1 O que medir no playtest — e é o oposto do que eles vão comentar

Com `2d10−1` o tráfego é **`16,5%`, dividido igual: `8,2%` salvou e `8,2%` traiu.**

> **Um em cada doze golpes vai passar porque você rolou, quando a sua Defesa parada teria segurado.**

Ninguém pede isso e ninguém espera isso, e é de lá que sai o *"na verdade eu odeio essa regra"* depois de duas sessões. **Pergunte no fim da sessão quantas vezes Bloquear custou caro, não quantas vezes salvou** — o `8,2%` que eles vão elogiar não é o que decide se a regra fica.

## 8. O que o validador confere

*Escrito antes do `conferir-bloquear.py`, no molde que a peça 15 §5 usou.* **Nenhum valor mora dentro do validador: todo número é lido do documento dono.**

| # | a checagem | o dono do número |
|---|---|---|
| **1** | **a neutralidade**, por enumeração das `2.000` combinações: o multiplicador do Bloquear com a trava do `20` natural é **idêntico** ao da Defesa estática, e sem a trava ele é menor. *Falha se os dois divergirem em mais de `0,0005`* | **A sub-checagem `1.1`, da v0.151, compara as DUAS cópias do preço do `Incapacitado`:** *esta peça cita o número e a peça 19 é a dona dele.* **Ela nasceu porque as duas divergiram de verdade** — a v0.151 repreçou aquela condição, os 24 validadores saíram verdes, e esta peça continuou publicando o valor velho em dois lugares. *Ela não tem lista de formas de citar: pega todo `` `N,NN` `` perto da palavra, e tem guarda de contagem, porque parar de citar deixaria ela verde e calada* | esta peça §2 e §3 · peça 19 §2.2 |
| **2** | **o modificador é a MESMA expressão** dos dois lados — a Defesa da peça 1 §5 e o Bloquear do §3 desta peça reconstroem um do outro, e a diferença é exatamente `11`. *Não compara valores: compara a fórmula* | peça 1 §5 |
| **3** | **o líquido do pacote de extremos, no nível 30**, recalculado das chances enumeradas e do golpe do chefe: fica abaixo de `1%` **do golpe do chefe**, e a peça é obrigada a declarar esse denominador. *Junto vai o **tráfego**, e ele tem de ser simétrico — o que salvou e o que traiu são o mesmo número, e a assimetria seria o viés que a peça existe para não ter* | esta peça §3.3 e peça 19 §2.1 |
| **4** | **o `+3` do Aparar é o maior que cabe.** *Ela confere as duas grandezas separadas:* a **folga** do nível 22, que é uma subtração em dano esperado, e o **teto do bônus**, que é a folga dividida pela taxa de acerto e sai em dano cru. **Falha se `+4` couber, se `+3` não couber, ou se a peça publicar um dos dois com o valor do outro** | esta peça §3.2 |
| **5** | **nenhuma outra das treze condições cita `Bloquear`** — só o `Incapacitado`. *Ela lê a peça 19 §3, e não uma lista escrita aqui* | peça 19 §3 |
| **6** | **a `Talha` continua sendo a única propriedade de arma que encosta no Bloquear**, e ela é do atacante. *Falha se alguma propriedade nova mexer no modificador do defensor.* **Junto vão quatro sub-checagens que a v0.143 precisou:** *a `Talha` continua dizendo o que faz; nenhuma frase de opcionalidade sobreviveu na peça 14; a **contagem** de armas escrita lá bate com o catálogo; e a **lista nominal** delas também* | peça 14 §5.2 |
| **7** | **os `2d10` são o único dado não-`d20` do sistema.** *Varre as peças procurando notação de dado numa rolagem disputada e falha se aparecer uma segunda família* | as peças |
| **8** | **a Reação do inimigo é a mesma que a peça 3 dá a todo mundo, e o manual a imprime.** *Ela não guarda o `1`: lê a quantidade dos dois lados e compara.* **Junto vai a guarda de que a seção `Inimigos` do manual continua existindo** — sem ela, renomear a seção faz a checagem achar zero linha e passar verde para sempre | peça 3 §3 · **o manual**, a fonte da seção `Inimigos` |

> **A checagem 1 é a que a peça 19 consome.** *Ela publica o `Incapacitado` em `4,95` porque o Bloquear é neutro — se a neutralidade quebrar, o preço daquela condição fica errado e ninguém mais estaria olhando.* **É a única checagem deste projeto que existe para sustentar um número de outra peça.**

**E a ficha:** a checagem que confere que o gerador imprime `Defesa N · Bloquear 2d10+M`, com `M = N − 11`, mora no `conferir-ficha.py` — que é o validador dono da comparação entre a ficha e as peças. *Aqui mora a matemática; lá mora a impressão.*

## 9. Em aberto

> ~~**O inimigo precisa de Reação na ficha dele.**~~ ***FECHADO na v0.159***, e não como valor por nível: *o §3.4 conta o porquê.* **A `Brecha` vale contra inimigo agora, e a assimetria que este item registrava acabou.**

1. **Se o playtest disser que a decisão do nível 22 nunca aparece na mesa**, o `+3` do Aparar pode subir sem custo, porque era ela que segurava o teto. *Decisão com gatilho, no molde da camada 3 da peça 14 §8.*
2. **Quanto tempo de mesa a rolagem a mais custa de verdade.** *A conta prevê `16` rolagens por combate; ninguém mediu.* **É a primeira pergunta da lista de playtest desta peça**, e ela é de cronômetro, não de planilha.

## 10. Levantamento externo

- **A house rule do d20 existe e é comum** — *"em vez de usar base 10 para a CA, você rola um d20 e ele conta como a base da sua CA naquele ataque"*. **Ninguém notou o `10,5`.**
- **O efeito de achatamento é conhecido**: *"rolar a defesa faz com que, para quem normalmente teria dificuldade de acertar, as chances aumentem; e onde alguém acertaria com facilidade, as chances de errar aumentem."*
- **Os sistemas que resolveram defesa ativa de verdade cobram de algum orçamento, e nenhum mantém CA junto:** Mythras (pontos de ação: defender compete com atacar), RuneQuest (`−20%` cumulativo por aparada extra), Riddle of Steel (pool único dividido entre ataque e defesa), e o GURPS — que é o caso mais instrutivo e está detalhado abaixo.

> **⚠⚠ O rascunho descrevia o GURPS de memória de busca, e ele errava em três pontos.** *Lido no manual da 4ª edição de luxo, páginas 374 a 377, esta versão está conferida contra o texto.*
>
> | o que o rascunho dizia | o que o manual diz |
> |---|---|
> | *"aparar e bloquear uma vez por turno cada"* | **só o bloqueio.** *"Só é possível bloquear um ataque por turno."* **Aparar não tem teto: tem penalidade cumulativa de `−4`** por tentativa extra com a mesma arma ou mão, no mesmo turno |
> | *"de graça"* | **a defesa ativa é paga por MANOBRA.** Quem escolhe Ataque Total *"não tem direito a qualquer jogada de defesa ativa"*, e Defesa Total compra uma segunda tentativa |
> | *"o próprio material admite que não existe consideração tática"* | **essa frase não existe no manual.** *Procurada no capítulo de combate inteiro; foi publicada entre aspas sem dono* |
>
> **E as duas correções fortalecem a peça, em vez de enfraquecer.** *O `−4` cumulativo do Aparar é a mesma família do `−20%` do RuneQuest, então a saída que o §1.1 recusa tem **dois** precedentes documentados e não um.* **E "pago por manobra" é um quinto mecanismo que o rascunho não listava:** *no GURPS a defesa é grátis em recurso e cara em opção — você abre mão do ataque total.* **Este sistema não tem essa moeda**, porque a Ação Padrão não se divide em manobras, e é por isso que a resposta aqui teve de ser o dado e não o preço.
>
> **⚠ E o manual do GURPS entrega, de graça, o precedente do §2.3:** *"Os valores das defesas ativas devem ser calculados previamente e registrados na planilha de personagem."* **O maior sistema de combate detalhado do hobby resolve o atrito da conta imprimindo o número pronto na ficha** — que é exatamente o que a linha `Defesa 17 · Bloquear 2d10+6` faz aqui.
- **A combinação CA estática mais rolagem grátis e neutra não apareceu em nenhuma busca.** Terreno não pisado, e é por isso que a resposta teve que ser derivada em vez de encontrada.
- **Ressalva metodológica, contra a métrica usada aqui:** *"a distribuição dos resultados — sucesso ou falha — é a mesma para circunstâncias equivalentes, e tem o mesmo desvio padrão."* Verdade. O **tráfego** não mede variância de resultado; mede quantas vezes o dado muda o resultado **em relação ao que a Defesa parada teria dado** — e isso o jogador percebe, porque ele conhece a própria Defesa e vê o ataque.
