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

*Fica em aberto, e é decisão de mesa:* **uma conversão pontual depois de muitas mesas mestradas** — um bônus por marca, não por sessão. A forma disso não está escrita, e ela não pode virar pagamento por mesa disfarçado.

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

## 7. O limiar do nível 20

> **Você chega ao nível 20 por XP. Você passa dele por feito.**

Chegando aos 6.300 de XP acumulado, o personagem para no nível 20 até a mesa reconhecer alguma coisa que ele fez. O XP continua acumulando e nada se perde — ele destrava de uma vez quando o feito acontece.

**De onde isso veio.** Foi pedido no levantamento, e o argumento não é de balanceamento:

> *"Eu colocaria algum tipo de requisito pra quebrar o padrão do lvl 20 e ir pro nível lendário. Seria mais demorado porém com alguma recompensa, pq daí iria tirar a ilusão do 'cheguei no lvl 20 pro 21 em 4 meses de mesa enquanto fulano de tal upou 7 níveis'."*

E ele encaixa numa coisa que o sistema já tinha: **a patente sobe por feito.** O limiar do 20 é o único lugar onde o eixo social e o eixo de poder se tocam — e se tocam uma vez só, na fronteira entre o mundano e o lendário.

**A trava que ele precisa.** *"O mestre decide o que é um feito"* não atravessa sete mesas. A lista precisa ser fechada, no molde do ambiente propício: **entradas escritas, e a palavra final do mestre em cima delas** — nunca do zero.

> **A lista de feitos está em aberto.** Ela é escolha de sabor e de mundo, e vai para a próxima rodada de decisão.

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

- **A lista de feitos do limiar do nível 20.**
- **A forma da conversão de mestragem** — um bônus por marca, sem virar pagamento por mesa.
- **Se dois mestres pagam parecido pela mesma falha.** Marcado para o playtest.
- **Se a semana é o relógio certo** para o retorno decrescente, ou se ele devia acompanhar o descanso longo, como o resto do sistema.
- **Se o "joga muito" um mês e pouco na frente incomoda na prática.** Registrado, não consertado.
