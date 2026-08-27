# EXPERIÊNCIA E PROGRESSÃO

**Fase 4, décima segunda peça.** Como se sobe de nível numa guilda onde sete mestres postam missão e ninguém coordena calendário.

Versão v0.32 — 11/08/2026 · Validador: `conferir-xp.py`

Esta é a **trava nº 1 de mundo compartilhado** — *"XP tabelado, nunca marco narrativo"* —, e ela ficou aberta por trinta versões. Sem ela, cinco mestres dão progressão diferente, que é exatamente o problema que o sistema existe para resolver.

Ela também é a primeira peça deste projeto escrita a partir de **dado de gente real**: catorze opiniões da Guilda sobre quanto tempo a subida deve levar. O que não muda o fato de tudo aqui continuar sendo previsão até alguém jogar — mas a previsão agora tem de onde sair.

> **O levantamento inteiro está em `01-pesquisa/levantamento-ritmo-de-progressao.md`**, com as catorze respostas como vieram, a mediana medida e o glossário do *gap*. Quando o playtest contradisser algum número daqui, é lá que se confere o que foi perguntado e quem respondeu o quê.

---

## 1. A regra, em cinco linhas

> **Cada nível custa um número inteiro de missões, e ele sobe uma missão a cada três níveis.**
> **Uma missão padrão paga 100 XP, e paga o mesmo para todo mundo na mesa.**
> **Nenhuma missão faz você subir mais de um nível — o que sobra fica acumulado.**
> **Por semana, as duas primeiras missões pagam cheio; da terceira em diante o valor cai pela metade a cada uma.**
> **Do nível 20 para o 21 o XP não basta: é preciso um feito.**

O resto desta peça é o porquê de cada uma das cinco.

## 2. Por que o XP é fixo, e não escalado pelo desafio

É a decisão que mais separa este sistema de um de campanha fechada, e ela vem de uma propriedade que só uma guilda precisa.

**Numa guilda, mesa aberta junta níveis diferentes.** Um nível 8 e um nível 14 na mesma missão não é exceção: é terça-feira. E aí a pergunta é o que acontece com quem ficou para trás.

Dois personagens começam juntos. Um perde dez sessões — viagem, prova, sumiço. Depois disso jogam tudo junto:

| depois de | XP fixo | XP escalado pelo nível |
|---|---|---|
| 20 sessões | distância 4 níveis | distância 4 |
| 40 sessões | **2** | 4 |
| 60 sessões | 2 | 4 |
| 90 sessões | **1** | 0 |

**Com XP fixo a distância só encolhe**, e chega a zero em 160 sessões — depois do fim de uma campanha, o que na prática quer dizer que ela termina em um nível de folga. O motivo é aritmético e não precisa de regra nenhuma: cada nível custa mais que o anterior, então a mesma missão vale uma fatia menor para quem está na frente. Quem está atrás sobe mais rápido sem receber nada de especial.

**Com XP escalado ela trava**, e só fecha porque o nível 30 é teto. Enquanto ninguém encosta no teto, o abismo não se move.

E isso tem nome na Guilda: é o **gap** que o Kekka descreveu — *"final da mansão tiveram players literalmente bloqueados de ganhar gap de tão mutantes que eram"*. Um personagem que se descola tanto que não cabe mais em mesa nenhuma.

### O que os jogadores queriam não era isso

A proposta que apareceu no levantamento foi *"inimigo de grau mais alto dá mais XP, como em D&D"*. A intuição está certa — **missão difícil deve valer mais** —, mas endereçada ao alvo errado.

**Missão difícil já vale mais, pelo tamanho dela** (seção 4). O que não pode é o valor depender do *nível de quem recebe*, porque é isso que congela a distância entre as fichas.

### E "Grau dá mais XP" bate numa decisão de arquitetura

O `arquitetura.md` separou os dois eixos de propósito:

> *"Todo personagem começa Grau 4, e a patente sobe por **feito**."*
> *"O Yuta é Grau especial, Nível baixo: a instituição o classificou no topo."*

**Grau é reconhecimento; nível é poder.** Se o Grau passar a dar XP, ele vira nível com outro nome — e pior, vira espiral fechada: sobe de patente, sobe de nível mais rápido, ganha patente por feito, sobe de novo.

O Grau continua valendo muito. Ele só não vale **XP**.

## 3. A curva

> **Um nível custa um número inteiro de missões padrão, e o número sobe uma a cada três níveis.**

| níveis | custa | em XP |
|---|---|---|
| **2 a 4** | 1 missão | 100 |
| **5 a 7** | 2 missões | 200 |
| **8 a 10** | 3 | 300 |
| **11 a 13** | 4 | 400 |
| **14 a 16** | 5 | 500 |
| **17 a 19** | 6 | 600 |
| **20 a 22** | 7 | 700 |
| **23 a 25** | 8 | 800 |
| **26 a 28** | 9 | 900 |
| **29** | 10 | 1.000 |

**Custo inteiro é a lição do jogo organizado, e não invenção nossa.** Os dois maiores sistemas de campanha compartilhada do mundo convergem nisso:

| | como conta |
|---|---|
| **D&D Adventurers League** (~100 mil membros) | 4 checkpoints por nível até o 4, 8 dali em diante — e 1 checkpoint por hora jogada |
| **Pathfinder Society 2e** | 12 XP por nível, cenário paga 4: **três cenários por nível**, sempre |

O que os dois compram é a mesma coisa: **um jogador sabe de cabeça quanto falta.** *"Estou no nível 12, cada nível são quatro missões, joguei duas."* Sem tabela, sem conta.

**Uma versão anterior desta peça usava uma reta** — `100 + 30 × (nível − 2)` —, e ela produzia 1,3 missão no nível 3, 1,6 no 4, 2,8 no 8. Todo nível pedia conta, e nenhum caía redondo.

**Os primeiros níveis passam voando de propósito.** Do 2 ao 4 é uma missão cada — a ficha entra em jogo e ganha corpo antes de qualquer decisão pesada. Do 17 em diante são seis missões por nível, e a subida vira coisa de arco.

## 3.1. Nenhuma missão dá mais de um nível

> **Você sobe no máximo um nível por missão. O XP que sobrar fica acumulado e sai na próxima.**

**Este é o defeito que derrubou o XP na maior campanha compartilhada do mundo.** A Adventurers League abandonou experiência na temporada 8, em 2018, e o motivo está escrito: *"uma aventura de quatro horas levava um personagem novo do nível 1 ao 3 — mais rápido do que os designers pretendiam."*

Sem o teto, a nossa pior combinação entregaria **três níveis de uma vez**: um final de arco jogado por um personagem de nível 2. Não é injusto — o XP é o XP —, mas é decisão de ficha demais para uma sessão só. Ninguém digere três níveis de escolha de uma vez, e o que a pessoa monta apressada ela joga mal por semanas.

| no nível | curta | padrão | longa | final de arco |
|---|---|---|---|---|
| 2 | +50 | **1 nível** | 1 nível, +100 | 1 nível, +200 |
| 5 | +50 | +100 | **1 nível** | 1 nível, +100 |
| 8 | +50 | +100 | +200 | **1 nível** |
| 12 e acima | +50 | +100 | +200 | +300 |

**O excedente não some, e isso importa.** Quem levou um final de arco no nível 2 sobe um nível na hora e entra na missão seguinte com 200 XP no bolso — sobe de novo, e continua subindo até o acumulado acabar. O teto não tira nada: ele só espalha.

**E ele quase não atrasa nada.** Simulado com missão padrão, o personagem com teto e o sem teto estão no mesmo nível em 10, 20, 40, 60 e 80 missões — porque com missão padrão o teto nunca chega a morder. Ele é rede de segurança para o caso grande, não freio de mão.

## 4. O tamanho da missão

Uma curva só, e quem varia é a missão.

| tamanho | paga | o que é |
|---|---|---|
| **curta** | 50 | uma cena, um interrogatório, roleplay puro, uma escolta sem incidente |
| **padrão** | 100 | a missão de uma sessão: sai, resolve, volta |
| **longa** | 200 | duas ou mais sessões, ou uma sessão que virou noite |
| **final de arco** | 300 | o fecho de uma linha de missões, ou o que a mesa vai lembrar por meses |

**Quem declara o tamanho é quem posta a missão, e ele declara antes.** Isso não é detalhe de administração: é o que impede o tamanho de ser decidido depois em função de como a mesa correu.

**Missão de roleplay que qualquer Grau pode entrar é missão curta**, e ela paga. Uma guilda que só dá XP para quem mata perde metade do que faz uma guilda ser guilda.

### E é isso que faz a faixa lendária ser mais rápida em tempo

Do nível 20 em diante a Guilda roda final de arco e side story — missões grandes. A curva continua subindo, mas o pagamento sobe junto:

| faixa | XP total | tamanho típico | missões |
|---|---|---|---|
| 2 → 20 | 6.300 | padrão, com uma longa a cada quatro | ~59 |
| 20 → 30 | **8.200** | longa e final de arco | ~34 |

Dez níveis lendários custam **mais XP** que dezoito mundanos — 8.200 contra 6.300 — e mesmo assim levam **pouco mais da metade das missões**. Foi o que catorze pessoas pediram de jeitos diferentes, e ele sai sem nenhuma regra de exceção.

## 5. As duas primeiras da semana pagam cheio

> **Na sua semana, a primeira e a segunda missão pagam o valor cheio. A terceira paga metade, a quarta metade disso, e assim por diante. A contagem zera na virada da semana.**

| missão da semana | paga |
|---|---|
| 1ª e 2ª | 100% |
| 3ª | 50% |
| 4ª | 25% |
| 5ª | 12% |
| 6ª | 6% |

**Ninguém sai com zero, e isso é a razão de ser retorno decrescente em vez de teto.** Um teto duro produziria a mesa em que você jogou seis horas e não levou nada — e aí a regra vira motivo de briga em vez de ritmo.

**O que ele resolve.** O levantamento trouxe o sintoma pronto, do Mega: *"muita gente só mestra pelo XP e isso vira cúmulo."* Quando a terceira mesa da semana vale metade, moer mesa para de compensar sozinho — sem proibir nada e sem ninguém precisar fiscalizar.

**E ele é o que faz os três perfis existirem:**

| perfil | mesas/semana | equivalente | 2 → 20 | o alvo |
|---|---|---|---|---|
| joga pouco | 1 | 1,00 | **14,5 meses** | 14 |
| mediano | 1,5 | 1,50 | **9,7 meses** | 9 |
| joga muito | 4 | 2,75 | **5,3 meses** | 6,5 |

Os dois primeiros batem quase exato. **Sem o retorno decrescente, quem joga quatro vezes por semana chegaria ao nível 20 em 3,4 meses** — e aí acontece o que o Zeuk temia: *"30 nego lvl 16 em 4 meses"*.

**O terceiro fica um mês e pouco na frente do alvo, e isso é registrado e não consertado.** Puxar ele para trás exigiria dar cheio só na primeira missão da semana — e aí quem joga uma vez por semana perde metade do que ganha hoje, que é exatamente quem não se quer punir. Cinco meses e pouco continua dentro do que o Mahi e o Pedro pediram.

## 6. Mestrar não dá XP

> **Mestrar não paga XP. Paga na moeda que o sistema já tem separada: patente, contato, favor da instituição, acesso.**

É a decisão mais impopular desta peça e a que tem o argumento mais curto: **se mestrar paga XP, mestrar vira a rota ótima de subir de nível**, e a pessoa que mais dirige o mundo é a que menos joga nele. O Mega descreveu o estado final disso no server de hoje.

**A recompensa existe e ela é grande** — ela só mora no eixo social, que é onde o `arquitetura.md` já pôs o reconhecimento. Um mestre ativo constrói patente e rede, e as duas coisas abrem porta que nível nenhum abre.

*E existe uma conversão pontual depois de muitas mesas mestradas* — **um bônus por marca, não por sessão.** A forma dela ficou em aberto da v0.32 à v0.171, com a trava escrita antes da regra: ela não pode virar pagamento por mesa disfarçado. **Hoje ela é o §6.2.**

## 6.1 O salário — a quarta moeda, e a única com número

*Escrita na v0.171, quando a peça 14 §8 item 11 finalmente pediu ela.* **Das quatro que o §6 lista — patente, contato, favor, acesso —, três continuam discricionárias de propósito. Esta tem tabela.**

> **Feiticeiro recebe salário mensal da instituição, e o valor sai da patente.** *Não é pagamento por missão: é folha.*

| patente | por mês | por ano |
|---|---|---|
| **Grau 4** | `¥150.000` | `¥1,8 milhão` |
| **Grau 3** | `¥300.000` | `¥3,6 milhões` |
| **Grau 2** | `¥600.000` | `¥7,2 milhões` |
| **Grau 1** | `¥1.200.000` | `¥14,4 milhões` |
| **Especial** | `¥2.400.000` | `¥28,8 milhões` |

**O topo é canon e o resto é derivado.** *O Akutami respondeu, em entrevista, que o salário do Gojo é o de um ministro do gabinete japonês — e que feiticeiro recebe **salário mensal**, e não por missão.* **Um ministro ganha `¥29,61 milhões` por ano**, e a escada inteira sai daí: `29,61M ÷ 12 ÷ 2⁴` dá `¥154.219`, arredondado para `¥150.000`. *A única escolha desta tabela é esse arredondamento, e ele custa `−2,7%` no topo.*

> **⚠ O lastro é levantamento secundário, e fica declarado como tal.** *A fala do Akutami chega por reportagem sobre uma entrevista, e não por fonte primária lida.* **Se um dia aparecer o número direto da fonte, é a linha do topo que se move, e a base se recalcula sozinha.**

**E ela cruza com o Japão real sem precisar de conserto.** *Um recém-formado começa entre `¥200.000` e `¥250.000` por mês; um `Grau 4` fica pouco abaixo disso, que é o que ele é — estudante, com moradia da escola.* **Um `Grau 1` em `¥14,4 milhões` por ano é salário de executivo sênior**, e é a faixa que explica a Mei Mei ser rica trabalhando por dinheiro.

### O que ele NÃO é

**Ele não é o quarto eixo de progressão, e a trava é a mesma do §2.** *Se o salário comprasse poder, o Grau viraria nível com outro nome pela porta dos fundos.* **O que o dinheiro compra está na peça 14, e lá ele passa por uma prova: nenhuma compra torna legal uma montagem que já não fosse** — toda entrada de equipamento é travada por atributo e por treino antes de ter preço, e o preço só decide **quando** você a alcança, nunca **se**.

> **A folga é de propósito, e é grande.** *O loadout mundano mais caro que existe — `Revestimento` no topo, arma de assinatura de duas mãos, arma de uma mão e escudo `Torre` — custa `¥1,6 milhão`.* **A renda de uma campanha inteira, subindo de Grau no ritmo normal, é da ordem de `¥10,5 milhões`:** o mundano inteiro cabe em `15%` dela. *Os outros `85%` existem para o que ainda não foi escrito — ferramenta amaldiçoada comprada em vez de recebida, e fabricação.*

## 6.2 A conversão de mestragem — o único lugar em que mestrar vira número

*Escrita na v0.172, e o §6 a deixou em aberto na v0.32.* **A forma estava por escrever; a trava já estava pronta: um bônus por marca, não por sessão, e ela não pode virar pagamento por mesa disfarçado.**

> **A cada vinte mesas mestradas você recebe uma mensalidade extra do seu Grau.** *A marca fecha sozinha na vigésima, e paga na patente que você tinha naquele dia.*

**Nenhum dos dois números foi escolhido.** *O valor é a linha do §6.1 — a mesma mensalidade, sem moeda nova e sem tabela nova.* **E o `20` é uma divisão com dois donos:** o levantamento mede o mestre ativo em **duas a três mesas por mês**, e o §6.1 mede o catálogo mundano inteiro em **`15%`** da renda de uma campanha. **`3 ÷ 0,15 = 20`.**

**O que a divisão compra é a trava do §6, e ela sai exata:** *no ritmo mais pesado que a Guilda já relatou, a mestragem acrescenta `15%` à renda — a mesma fatia que o loadout mundano mais caro ocupa.* **Mestrar a campanha inteira paga um loadout completo, e nem um iene a mais.**

### 6.2.1 Por que ela não vira pagamento por mesa, e isso é aritmética

**A fração não depende do tamanho da campanha.** *Ganho e folha correm no mesmo relógio — a mestragem entrega `taxa ÷ 20` da folha, e só isso.* **Mestrar mais não descola a mestragem do salário: ela anda amarrada nele, em qualquer campanha e em qualquer patente.**

| quem mestra | mesas por mês | fecha uma marca em | acrescenta à renda |
|---|---|---|---|
| **pesado** — o teto relatado | `3` | `6,7` meses | **`15%`** |
| **ativo** — a fala do levantamento | `2` | `10` meses | `10%` |
| **ocasional** | `1` | `20` meses | `5%` |

*A coluna da direita é `taxa ÷ 20`, e é ela que responde à trava: a folha continua sendo a renda, e a marca é o bônus em cima.*

> **A marca é rara de propósito, e a régua de raro é a do próprio sistema.** *O §5 mede o perfil mediano em `9,7` meses até o nível 20; nessa janela um mestre pesado fecha `1,5` marca, contra os **quatro** marcos que a ficha atravessa nos níveis 6, 10, 14 e 18.* **Menos frequente que o marco, que é a coisa mais rara que uma ficha tem.**

**Quem mestra pouco não fecha marca nenhuma, e isso não é buraco.** *O §6 já diz onde mora a recompensa de mestrar — patente, contato, favor e acesso —, e nenhuma das quatro tem relógio.* **A marca é a conversão pontual que o §6 prometeu *"depois de muitas mesas mestradas"*, e vinte é muitas.**

### 6.2.2 Contar mesa mestrada não é o relógio que a peça 13 reprovou

**A peça 13 §7 recusou `uma vez por sessão` no catálogo de Legados, e citou justamente esta seção para recusar.** *O argumento continua de pé e não alcança a regra acima.*

**Lá o defeito é que *"uma sessão"* é leitura:** *três mestres leem a mesma palavra de três jeitos, e o spread entre a leitura mais generosa e a mais dura é `3,0×` na mesma ficha.* **Aqui não há o que ler.** *Uma mesa mestrada é uma missão postada e resolvida, e quem postou está no quadro — a contagem sai do registro da Guilda, e não da memória de ninguém.*

> **⚠ E não existe guardar marca.** *Ela fecha na vigésima mesa, no dia em que a vigésima acontece.* **Segurar mesa para fechar a marca depois de subir de patente não funciona, porque não existe o ato de fechar.** *O livro já escreve o mesmo cuidado do outro lado, em "guardar marco não guarda refino".*

## 7. O limiar do nível 20

> **Você chega ao nível 20 por XP. Você passa dele por feito.**

Chegando aos 6.300 de XP acumulado, o personagem para no nível 20 até a mesa reconhecer alguma coisa que ele fez. O XP continua acumulando e nada se perde — ele destrava de uma vez quando o feito acontece.

**De onde isso veio.** Foi pedido no levantamento, e o argumento não é de balanceamento:

> *"Eu colocaria algum tipo de requisito pra quebrar o padrão do lvl 20 e ir pro nível lendário. Seria mais demorado porém com alguma recompensa, pq daí iria tirar a ilusão do 'cheguei no lvl 20 pro 21 em 4 meses de mesa enquanto fulano de tal upou 7 níveis'."*

E ele encaixa numa coisa que o sistema já tinha: **a patente sobe por feito.** O limiar do 20 é o único lugar onde o eixo social e o eixo de poder se tocam — e se tocam uma vez só, na fronteira entre o mundano e o lendário.

**A trava que ele precisa.** *"O mestre decide o que é um feito"* não atravessa sete mesas. A lista precisa ser fechada, no molde do ambiente propício: **entradas escritas, e a palavra final do mestre em cima delas** — nunca do zero.

### 7.1 As oito, e a lista é fechada

*Escrita na v0.172.* **O mestre da mesa tem a palavra final sobre se uma delas aconteceu — e não sobre quais são.**

| | o feito | o que um segundo mestre lê para conferir |
|---|---|---|
| **1** | derrubar um `Chefe` de nível acima do seu | o manual traz `Chefe` e o nível do grupo na tabela de inimigo; o seu nível está na ficha |
| **2** | sair de pé de uma Expansão de Domínio completa | a completa resolve por acerto garantido, pela peça 11; *de pé* é não ter chegado a `0` |
| **3** | fechar um `final de arco` | o tamanho é declarado **antes** da mesa, pela seção 4 desta peça |
| **4** | pôr de pé alguém que estava a `0` de vida | `Aguentar` e `Insistir` são estados escritos, na peça 1 §5.5 |
| **5** | voltar do estágio 4 de dano de alma | os quatro estágios são tabela, na peça 24 §4 |
| **6** | cumprir uma `Promessa` até o fim, pagando a sua metade | os três termos ficam escritos quando ela fecha, na peça 22 §5.1 |
| **7** | trazer para a Guilda uma ferramenta de grau 1 ou especial | a escada de grau da ferramenta é a peça 16 §3, e a ficha registra qual |
| **8** | terminar a missão depois de outro personagem jogador chegar ao estágio 4 | o mesmo estágio da peça 24 §4, lido na ficha do outro e não na sua |

**Um feito basta, e ele destranca uma vez.** *Quem acumulou XP parado no 20 sobe de uma vez até o acumulado acabar, pela regra do §3.1 — o feito abre a porta, e não paga XP.*

### 7.2 O filtro que escolheu as oito já estava escrito, e é da peça 10

**Aquela peça separou lista fechada de lista de exemplo, e o critério dela serve inteiro aqui:** *o `ambiente propício` tem lista fechada porque **"esse lugar tem kit e comida?" é pergunta sobre o mundo** — a mesma resposta serve para qualquer mesa; e `isso foi uma luta?` fica aberto porque **é pergunta sobre a cena que aquele mestre acabou de dirigir**, e ninguém está em melhor posição de responder do que ele.*

**Toda entrada acima é do primeiro tipo.** *Cada uma cita um estado que a ficha ou o registro da missão carrega depois que a mesa acabou* — um nível, um `0` de vida, um estágio, um tamanho declarado antes, um grau escrito na ferramenta. **Nenhuma delas pergunta como a cena foi.**

> **É por isso que *"o mestre decide o que é um feito"* não atravessa sete mesas e esta lista atravessa.** *Sete mestres discordam sobre o que foi impressionante; nenhum deles discorda se o `Chefe` era de nível acima.*

### 7.3 Três das oito trocaram de forma, e vale dizer por quê

**As três reprovavam no filtro do §7.2 do jeito que foram propostas, e as três tinham conserto.**

- **`fechar um incidente que teria vazado` virou `fechar um final de arco`.** *O original é contrafactual — *teria* vazado —, e o sistema não tem Véu: `vazar` não aparece em peça nenhuma nem no livro.* **O tamanho da missão é o gancho mais duro que esta peça tem**, porque a seção 4 obriga a declaração *antes*, exatamente para o tamanho não ser decidido depois em função de como a mesa correu.
- **`escrever um Fundamento inédito` virou `voltar do estágio 4 de dano de alma`.** *Escrever Fundamento é decisão de criação e não feito de mesa — sai do Passo da peça 8, e não da missão.* **E `Inédito` já é o nome de um Legado do Latente**, na peça 13: a entrada colidiria com um termo em uso.
- **`a instituição te dever um favor` virou `trazer para a Guilda uma ferramenta de grau 1 ou especial`.** *`Favor da instituição` é uma das quatro moedas com que o §6 paga a mestragem* — usá-lo como feito fecharia laço entre as duas seções desta peça. **E o favor é estado narrado pelo mestre, sem nada na ficha para um segundo conferir.**

> **⚠ E a primeira entrada trocou `grau` por `nível`, porque não existe grau de maldição hoje.** *A escada `grau 4 a grau 1, mais o especial` existe para **ferramenta e objeto**, na peça 16 §3, e para **patente**, no §6.1 desta.* **Inimigo não tem grau em documento nenhum:** *a tabela do manual é `nível do grupo → vida e dano`, com as colunas `Chefe` e `Capanga`.* **Se o BESTIÁRIO der grau ao inimigo, esta entrada volta para a forma original, e o feito 1 é a linha que o obriga a decidir.**

> **⚠ O feito 7 é o mais frouxo dos oito, e o registro fica.** *Uma ferramenta especial aparecer é decisão do mestre — a peça 16 §3.2 escreve que ela `aparece uma vez por arco, e não duas na mesma mesa`.* **O que a lista exige é que o FATO seja conferível depois, e o grau fica escrito na ficha;** *mas ele é o único dos oito em que a porta é aberta por quem dirige, e não alcançada por quem joga.*

## 8. Falhar

> **Missão falhada paga metade ou nada, e quem decide é o mestre.**

Uma faixa e não um número, porque as duas pontas existem: uma missão perdida por azar de dado não é a mesma coisa que uma abandonada na metade.

**O piso da faixa é metade, e não zero, por um motivo de mesa** — seis horas de sessão que terminam em nada fazem a pessoa não voltar. E o teto é metade, e não cheio, porque senão o sucesso deixa de significar.

*Isto é discricionariedade assumida*, no mesmo molde do *"o mestre declara o que foi uma luta"* da peça 10. Vai para o playtest com a mesma pergunta: **dois mestres pagam parecido pela mesma falha?**

## 9. Como a Guilda opera isto

1. **O mestre posta a missão e declara o tamanho** — curta, padrão, longa, final de arco.
2. **A mesa acontece.**
3. **No fim, o mestre paga o valor declarado**, cheio no sucesso, metade ou nada na falha.
4. **O jogador anota na ficha**, e aplica o desconto da semana se já for a terceira missão.
5. **Chegou ao XP do próximo nível, sobe** — no máximo um nível, e o resto fica acumulado. Não precisa de aprovação, exceto no limiar do 20.

**Uma linha de missões paga por missão, e não no fim.** Quem entra no meio de uma linha recebe pelo que jogou — é o que permite mesa aberta funcionar.

**O desconto semanal é do jogador, não da mesa.** Numa missão com quatro pessoas, uma pode estar na primeira semana dela e outra na quarta. Cada um aplica o seu.

## 10. Em aberto

- ~~**A lista de feitos do limiar do nível 20.**~~ **Fechada na v0.172: são as oito do §7.1**, e o filtro que as escolheu é o da peça 10.
- ~~**A forma da conversão de mestragem** — um bônus por marca, sem virar pagamento por mesa.~~ **Fechada na v0.172: é o §6.2**, uma mensalidade do seu Grau a cada vinte mesas mestradas.
- **Se dois mestres pagam parecido pela mesma falha.** Marcado para o playtest.
- **Se a semana é o relógio certo** para o retorno decrescente, ou se ele devia acompanhar o descanso longo, como o resto do sistema.
- **Se o "joga muito" um mês e pouco na frente incomoda na prática.** Registrado, não consertado.
