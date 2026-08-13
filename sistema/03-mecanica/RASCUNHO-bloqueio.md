# RASCUNHO — Bloquear

**Não é peça.** Sem número na frente de propósito: meia peça não é peça, e um arquivo com dois dígitos quebraria a contagem do `conferir-repositorio.py`. Isto é uma regra opcional, e ela vai para o tópico de regras quando aquele tópico existir.

*Escrito na v0.43. Nada aqui mudou número de peça nenhuma — a Defesa continua sendo `10 + Destreza + proteção` e continua sendo o padrão.*

---

## 1. O pedido, e por que ele não é o que parece

A maioria dos jogadores quer **rolar para se defender**. É um pedido velho e comum, e a resposta padrão do hobby — *"role d20 + os modificadores da sua Defesa no lugar dos 10"* — está errada por um motivo que ninguém no hobby percebeu.

> **`E[d20] = 10,5`, e a base da Defesa é `10`.**

Rolar dá **+2,5 pontos percentuais de graça, em todo ataque, para todo mundo**. A house rule é praticada há décadas com um bônus escondido dentro dela, e a busca externa não achou uma única discussão do problema.

E isso reprova pelo critério da casa: *"enumere as montagens legais e conte quantas ganham o bônus. Perto de 100%, não é bônus."* Custando zero, ninguém nunca deixa de rolar. **Não é escolha; é a Defesa subindo meio ponto com uma rolagem colada nela.**

## 2. Três saídas que não servem, e o número de cada uma

*Registradas porque as três parecem óbvias, e alguém vai propor cada uma delas de novo.*

**Cobrar a Reação.** A Reação de cobrir-se já dá RD de `1,5 × refino` por 2 PE. O bloqueio evita `2,5% × golpe`. Ela perde de **8× a 12×** em todo nível — vira letra morta. *E a janela é estreita dos dois lados: de graça vira automático, com preço vira nunca. Não existe preço intermediário, porque a Reação é o único slot defensivo do sistema.*

**Risco no fracasso — dano extra se o bloqueio falhar.** O dano extra que **equilibra** é `5,26%` do golpe: **1,9 de dano no nível 14**. A proposta que estava na mesa era *"nível em dano"*, que é **de 7× a 8× maior** — e faz bloquear ficar de **28% a 35% pior**. Não é nerf, é deleção. *O buraco não tem ponte: qualquer penalidade grande o bastante para dar medo já mata a opção, porque a vantagem que ela precisa cancelar é 2,5pp e mais nada.*

**Penalidade cumulativa por bloqueio na rodada**, no molde do −20% do RuneQuest. Traduzida para d20, −1 por bloqueio extra: o primeiro vale +2,5pp e **o segundo já vale −2,5pp**. É *"uma vez por rodada"* com outro nome, e o pedido era justamente valer em ataques múltiplos.

## 3. A saída: o dado da defesa não precisa ser d20

O d20 é sempre melhor por um motivo só, e ele é aritmético. **Qualquer dado de média 10 é neutro por construção** — sem penalidade escrita, sem custo, sem teto por rodada, sem Reação:

| dado | média | desvio | acerta no parelho | vs estático |
|---|---|---|---|---|
| 1d20 | 10,50 | 5,77 | 47,5% | **+2,5pp** |
| **2d10−1** | **10,00** | 4,06 | **50,0%** | **0,0pp** |
| 2d8+1 | 10,00 | 3,24 | 50,0% | 0,0pp |
| 2d6+3 | 10,00 | 2,42 | 50,0% | 0,0pp |
| 4d4 | 10,00 | 2,24 | 50,0% | 0,0pp |

### Por que dois dados, e não um d20 ajustado

*Esta é a pergunta que o Mizuki fez, e a resposta é a razão de a coisa toda funcionar.*

**A média de um dado único sempre termina em `,5`**, porque é `(N+1)/2`. A base da Defesa é inteira. Então o buraco é de **meio ponto**, e não existe modificador inteiro que o feche: `d20` dá **+2,5pp** e `d20−1` dá **−2,5pp**, sem nada no meio.

**2d10 tem média 11 — inteira.** O `−1` fecha exato. É por isso que a família de dados neutros só aparece com dois dados ou mais.

*Varridas 11 × 9 = 99 combinações de modificador de Defesa contra bônus de ataque: todas idênticas ao estático, ao ponto flutuante.*

### E o `−1` não aparece na mesa

`2d10 − 1 + Destreza + proteção` é o mesmo que **`2d10 + (Defesa − 11)`**. A ficha é gerada por código, então ela imprime **`Defesa 17 · Bloquear 2d10+6`** e o jogador lê um número pronto. Na mesa vira *"role 2d10+6"*, que tem o mesmo atrito de *"role d20+7"*.

E a regra declara a própria neutralidade, o que resolve o *"nem pode parecer vantajoso"* sem pedir que ninguém confie numa planilha:

> **A média de 2d10 é 11. Você troca os 11 que a sua Defesa já supõe por dois dados. Na média, dá exatamente a sua Defesa.**

## 4. A regra

> **A sua Defesa é `10 + Destreza + proteção`, e ela é o padrão.**
>
> **Ao ser atacado, você pode Bloquear:** role **`2d10 + (sua Defesa − 11)`** e use esse valor no lugar da sua Defesa contra aquele ataque.
>
> **Duplo 10 — Aparar.** O ataque não acerta. Você pode gastar a sua **Reação** para atacar o agressor imediatamente, e esse ataque sai com **+3 de dano**.
> **Duplo 1 — Brecha.** O ataque acerta. O agressor pode gastar a **Reação dele** para atacar você de novo, imediatamente, sem bônus.
>
> **O Aparar não anula um 20 natural.** Crítico fura guarda.
> Bloquear não custa nada, não gasta a sua Reação, vale contra qualquer ataque com rolagem de acerto, **não vale em Teste de Resistência**, e é de todo mundo.

**O crítico não muda em nada.** O atacante continua rolando d20, então *"20 natural numa rolagem de acerto"* segue intocado — 5%, dobra os dados, zero texto novo. *Isso é vantagem desta rota sobre virar a rolagem para o jogador, que obrigaria a mudar a casa do crítico.*

*E a trava do 20 natural sai de graça:* com ela, o multiplicador vai de `0,5490` para **`0,5500` exato** — ela **paga** a neutralidade que faltava, em vez de custar.

### Os dois extremos, e por que os dois gastam Reação

*A ideia é do Mizuki e ela vem do For Honor: recompensar quem apara, punir quem não apara direito.* **Os dois lados pagam o próprio slot, e os dois podem recusar** — é isso que traz o peso do *"eu realmente bato?"*, e o inimigo pensa igual, porque Reação também é recurso dele.

**A régua do ataque de oportunidade já existe** (peça 3 §2: *"você pode gastar a sua Reação para atacar"*), então nenhum dos dois inventa mecânica.

> **O `Guarda Aberta` saiu `DENTRO` na triagem** — carrega a Melhoria `Guarda` dentro, e a Melhoria é sobre defesa, então era substring **e** sentido. **`Brecha` saiu `LIVRE`** nas duas direções, e nomeia o que aconteceu com você em vez de acusar você de ter vacilado num resultado que foi do dado.

### O invariante que segura tudo: o modificador é UM só

> **Bloquear usa exatamente o mesmo modificador da Defesa passiva. Nada pode aumentar um sem aumentar o outro.**

*Decisão do Mizuki, e ela é o que impede a mecânica de apodrecer com o tempo.*

A neutralidade inteira depende de `média(2d10) = 11` bater com a base `10` mais o mesmo modificador dos dois lados. **Se um escudo, uma aptidão, um Legado ou um item desse `+1 na Defesa` e não no Bloquear — ou o contrário —, o jogador passaria a escolher pelo número em vez de escolher pelo gosto**, e a regra viraria exatamente a coisa que ela existe para não ser.

E o buraco é grande: **+1 de diferença vale 2,5 pontos percentuais**, que é o tamanho do viés do d20 que esta peça inteira saiu para consertar. Um único item mal escrito desfaz tudo.

**Isso é checagem do validador, não confiança:** ele lê o modificador dos dois e falha se as duas expressões não forem a mesma. Não *"os dois somam 7"* — a **mesma expressão**, porque valores iguais hoje divergem amanhã, e isso é a lição nº 9.

### Por que +3, e não +6 ou +metade do nível

*A conta decidiu isto sozinha, e o critério é o que o Mizuki pediu: manter o peso da escolha.*

**Primeiro, onde a decisão existe.** A Reação só custa alguma coisa se **outro golpe vier na mesma rodada** — se você aparou o único golpe do turno, ela não tinha outro emprego. Medido contra os golpes por rodada do §4 de equipamento:

| cenário | AO rende | Reação custa | é decisão? |
|---|---|---|---|
| chefe sozinho, qualquer nível | 6,9 | **0,0** | não — sempre aceita |
| chefe + capanga, nv6 e nv14 | 5,8 a 6,9 | 3,0 a 6,0 | não — sempre aceita |
| **chefe + capanga, nv22 e nv30** | 6,9 | 9,0 a 12,0 | **sim, e pesa** |

**Segundo, o que o bônus compra e o que ele destrói:**

| bônus | seu AO no nv30 | líquido do pacote | a decisão do nv22 |
|---|---|---|---|
| **+3 fixo** | 8,53 | **0,43%** | **sobrevive** |
| +25% | 8,59 | 0,43% | sobrevive |
| +metade do nível | 15,13 | 0,25% | **morre** |
| +nível | 23,38 | 0,02% | **morre** |

**Fixo e percentual empatam, e o motivo é que o golpe simples quase não cresce:** o dado é fixo e a Força trava em 6, então o dano vai de 9,5 no nv2 a 12,5 no nv14 e para ali. `+25%` disso é **sempre 2,4 a 3,1** — o `+3` é literalmente o mesmo número, sem conta de porcentagem na mesa.

**O teto é +3,9 de dano cru, e quem manda é o nv22:** é lá que a Reação vale 9,0 contra os 6,88 do AO base, e a folga é 3,86. **`+3` cabe com 0,9 de margem; `+4` estoura e a decisão morre.**

*E `nível` passa o alvo por 2,3× no nv6 e 9,6× no nv30* — a distância **cresce**, porque o bônus escala e a base não. Lição nº 1 na forma mais direta: o adicional viraria o ataque, e o ataque viraria o resto.

> **A tabela expõe uma troca que vale registrar:** bônus maior deixa o **líquido** mais perto de zero (0,43% → 0,02%), porque compensa o golpe maior do inimigo — **e mata a decisão.** As duas coisas correm em sentidos opostos, e o critério que decidiu foi o do Mizuki: *"tem que custar Reação pra vir aquele peso de 'eu realmente bato?'"*

### O que o pacote custa, somado

| | líquido por golpe recebido, nv30 | em % do golpe |
|---|---|---|
| Bloquear puro, sem extremos | 0,000 | **0,00%** |
| **+ Aparar e Brecha, com +3** | −0,154 | **0,43%** |

**Menos de meio por cento**, e ele **cresce com o nível** — 0,15% no nv6 contra 0,43% no nv30, porque o seu golpe simples trava em 6,9 quando a Força chega a 6 e o do chefe continua subindo. *Isso é a lição nº 1 aparecendo pequena: fica registrado para ninguém se assustar, e para o validador vigiar se ela crescer.*

> **E o bônus fica só no Aparar, não nos dois lados.** Se ele valesse para o inimigo também, amplificaria a assimetria — o golpe dele é maior e levaria a mesma porcentagem, e o custo do pacote subiria de 0,43% para 1,17%. *A assimetria também é mais fiel à fonte: no For Honor o parry garante um golpe pesado, e a guarda aberta do oponente só dá uma abertura comum.* **Aparar é perícia recompensada; Brecha é você exposto.**

## 5. O que ela custa, e não é balanceamento

**Tempo de mesa, e é a objeção documentada número um** contra defesa ativa em qualquer sistema. Uma rolagem a mais por golpe recebido — cerca de 16 num combate de quatro rodadas com quatro personagens. Ela não some; ela só deixa de ser paga por um bônus escondido.

**A galera vai rolar sempre, e a conta diz por quê:**

| o que o jogador vê | chance |
|---|---|
| **Aparar** — história boa | 1,0% |
| **duplo 1** — história ruim | 1,0% |
| o dado mudou o resultado, sem extremo | 14,5% |
| nada aconteceu, rolou por rolar | **83,5%** |

Dois eventos de 1% que são os mais memoráveis da mecânica, e 83,5% de rolagens que não mudam nada. **Vão rolar por loteria, não por vantagem** — e isso foi decidido de olhos abertos: *"vai fazer a galera querer rolar mais que defender passivo? Vai, mas é um flavor que eu acho que vale a pena."*

**E é o primeiro dado não-d20 do sistema.** Isso é uma exceção real num jogo que rola d20 para tudo o mais, e o preço dela é de aprendizado, não de matemática.

## 6. O que medir no playtest — e é o oposto do que eles vão comentar

Com 2d10−1 o tráfego é **16,5%, dividido igual: 8,2% salvou e 8,2% traiu.**

> **Um em cada doze golpes vai passar porque você rolou, quando a sua CA teria segurado.**

Ninguém pede isso e ninguém espera isso, e é de lá que sai o *"na verdade eu odeio essa regra"* depois de duas sessões. **Pergunte no fim da sessão quantas vezes Bloquear custou caro, não quantas vezes salvou** — o 8,2% que eles vão elogiar não é o que decide se a regra fica.

## 7. Em aberto

1. **Condições que impedem Bloquear.** O Mizuki levantou como possibilidade — surpreendido, caído, agarrado, sem ver o agressor. Nenhuma escrita, e elas são o que dá variação sem mexer em número nenhum. *É a única peça do desenho que ainda não tem forma.*
2. **A ficha precisa imprimir a linha.** `Defesa 17 · Bloquear 2d10+6`, calculada pelo `gerador-ficha` — e é ela que faz o `−1` nunca aparecer na mesa.
3. **O inimigo precisa de Reação na ficha dele.** A Brecha só funciona se o mestre souber que o inimigo tem uma e se ela for gasta de verdade. Isso é contabilidade nova na ficha de inimigo, e ela segue o padrão do ambiente propício: **valor na tabela por nível, palavra final do mestre.**
4. **O validador.** Três checagens, e nenhuma delas confia em texto: **(a)** recalcular `média(2d10)` contra a base da Defesa e falhar se divergirem; **(b)** conferir que o modificador do Bloquear e o da Defesa passiva são **a mesma expressão**, não dois valores que hoje calham de dar igual; **(c)** recalcular o líquido do pacote de extremos e falhar se passar de **1% do golpe** em qualquer nível. *Se o dado mudar, se a base mudar, se algum item der bônus a um lado só, ou se o +3 subir, é ele quem acusa.*
5. **Onde ela mora.** Regra opcional, então o tópico de regras — não a peça 1, que é dona da fórmula e não deve ganhar variante dentro dela.
6. **Se o playtest disser que a decisão do nv22 nunca aparece na mesa**, o bônus de +3 pode subir sem custo, porque era ela que segurava o teto. *Decisão com gatilho, no molde da camada 3 do §6 de equipamento.*

## 8. Levantamento externo

- **A house rule do d20 existe e é comum** — *"em vez de usar base 10 para a CA, você rola um d20 e ele conta como a base da sua CA naquele ataque"*. **Ninguém notou o 10,5.**
- **O efeito de achatamento é conhecido**: *"rolar a defesa faz com que, para quem normalmente teria dificuldade de acertar, as chances aumentem; e onde alguém acertaria com facilidade, as chances de errar aumentem."*
- **Os sistemas que resolveram defesa ativa de verdade cobram de um orçamento, e nenhum mantém CA junto:** GURPS (aparar/bloquear uma vez por turno cada, de graça — e o próprio material admite que *"não existe consideração tática"* quando só vem um golpe), Mythras (pontos de ação: defender compete com atacar), RuneQuest (−20% cumulativo por aparada extra), Riddle of Steel (pool único dividido entre ataque e defesa).
- **A combinação CA estática + rolagem opcional grátis e neutra não apareceu em nenhuma busca.** Terreno não pisado, e é por isso que a resposta teve que ser derivada em vez de encontrada.
- **Ressalva metodológica, contra a métrica usada aqui:** *"a distribuição dos resultados — sucesso ou falha — é a mesma para circunstâncias equivalentes, e tem o mesmo desvio padrão."* Verdade. O **tráfego** não mede variância de resultado; mede quantas vezes o dado muda o resultado **em relação ao que a CA teria dado** — e isso o jogador percebe, porque ele conhece a própria CA e vê o ataque.
