# Curva do Teste de Resistência: d20 x 3d6

## Resposta direta

Com os números que você passou, o d20 não faz os inimigos passarem sempre. A chance de resistência deles fica numa faixa saudável, entre 45% e 75%, dependendo do nível do conjurador e de ele ter comprado Precisão ou não. Não existe nenhum ponto da progressão em que o resultado vira "garantido" ou "impossível" para nenhum dos dois lados.

Trocar para 3d6 muda bastante, e não é uma troca neutra. Se você portar os mesmos números da fórmula sem ajustar nada, o problema que você está com medo de ter (inimigo resistindo sempre) piora justamente nos níveis baixos: a chance de resistência no nível 1 vai de 75% (d20) para 95% (3d6). Trocar o dado exige redesenhar a curva de números, não só trocar "d20" por "3d6" no texto da regra.

A conta completa está abaixo.

## Premissas usadas nesta análise

- "Metade do nível do conjurador" = nível dividido por 2, arredondado para baixo. Se você arredondar para cima, os números mudam no máximo 1 ponto em níveis ímpares — não muda nenhuma conclusão.
- Bônus de resistência do inimigo: você deu as pontas (+2 no nível 1, +8 no nível 20); como não tenho a progressão exata dos níveis do meio, interpolei de forma linear entre essas duas pontas. Isso não compromete a conclusão principal, que depende só das pontas — se a progressão real for "em degraus", pode ter pequenos solavancos no meio, mas a tendência geral (CD subindo mais rápido que a resistência) se mantém.
- Comparei conjurador de nível X contra inimigo "padrão" desse mesmo nível (encontro parelho). Se o inimigo for de nível diferente, é só recalcular trocando o bônus dele.
- Não assumi regra de "1 natural sempre falha / 20 natural sempre passa". Se seu sistema tiver isso, ela trava o d20 entre 5% e 95%; no 3d6 o efeito equivalente seria raríssimo (ver seção 5).

## 1. A conta no d20

A chance de o inimigo resistir é sempre:

chance = (21 − número necessário) / 20, onde número necessário = CD − bônus de resistência do inimigo.

O d20 é uma distribuição uniforme (cada face vale exatamente 5% de chance), então cada ponto de diferença entre CD e bônus vale sempre 5 pontos percentuais, não importa se é no nível 1 ou no nível 20.

## 2. A curva nível a nível (d20)

Sem Precisão:

| Nível | CD | Bônus do inimigo | Número necessário | Chance de resistir |
|---|---|---|---|---|
| 1 | 8 | +2 | 6 | 75% |
| 5 | 10 | +3 | 7 | 70% |
| 10 | 13 | +5 | 8 | 65% |
| 15 | 15 | +6 | 9 | 60% |
| 20 | 18 | +8 | 10 | 55% |

Com Precisão (CD +2):

| Nível | CD | Bônus do inimigo | Número necessário | Chance de resistir |
|---|---|---|---|---|
| 1 | 10 | +2 | 8 | 65% |
| 5 | 12 | +3 | 9 | 60% |
| 10 | 15 | +5 | 10 | 55% |
| 15 | 17 | +6 | 11 | 50% |
| 20 | 20 | +8 | 12 | 45% |

## 3. Por que isso não vira "sempre passa"

Duas coisas seguram a curva:

Primeiro, a CD cresce mais rápido que a resistência dos inimigos. A CD sobe 1 ponto a cada 2 níveis (metade do nível), então do nível 1 ao 20 ela sobe uns 10 pontos. O bônus de resistência dos inimigos sobe só 6 pontos no total (de +2 para +8) no mesmo intervalo. Essa diferença de ritmo abre uma vantagem de uns 4 pontos para o conjurador ao longo da progressão, o que tira 20 pontos percentuais da chance de resistência do inimigo (75% → 55% sem Precisão, 65% → 45% com Precisão). É uma escolha de design comum e razoável: o conjurador fica proporcionalmente mais preciso conforme sobe de nível, então a magia de área "amadurece" junto com o personagem.

Segundo, a Precisão tem impacto fixo e previsível. Como o d20 é linear, +2 na CD sempre vale exatamente 10 pontos percentuais a menos de chance de resistência do inimigo, seja no nível 1 ou no nível 20 (compare as duas tabelas: a diferença entre elas é sempre exatamente 10%). Isso é uma propriedade boa do d20 — o jogador sabe exatamente o que está comprando ao pegar Precisão, em qualquer nível.

No fim das contas, a faixa fica entre 45% e 75% de chance de resistência do inimigo, nunca perto de 0% nem de 100%. É uma curva bem comportada, sem degraus nem extremos.

## 4. Pontos de atenção (não são erros, são escolhas de design)

- Nível 1 sem Precisão, 75% de resistência, é o ponto mais fraco para o conjurador: a magia de área vai causar metade do dano na maioria das vezes bem cedo no jogo. Se isso incomodar na mesa, dá para subir a CD base (de 8 para 9) ou reduzir um pouco o bônus de resistência inicial dos inimigos.
- Nível 20 com Precisão, 45% de resistência, inverte o favorito: o inimigo passa a falhar mais do que acertar o teste. Isso parece ser exatamente o efeito que Precisão deveria ter (um upgrade que faz o inimigo sofrer mais), então provavelmente está certo — só vale confirmar que essa é a fantasia que você quer entregar para quem investe nela.
- Se a progressão real do bônus de resistência dos inimigos não for linear (por exemplo, se ela saltar de +2 para +4 já no nível 5), vale reconferir os níveis de transição: pode existir um nível específico em que o número necessário cai de repente e cria um degrau de dificuldade que os dados acima não capturam.

## 5. E se trocar para 3d6?

Aqui está o ponto central: 3d6 e d20 têm exatamente a mesma média (10,5), mas desvios-padrão bem diferentes:

- d20: desvio-padrão aproximadamente 5,77
- 3d6: desvio-padrão aproximadamente 2,96 (quase metade do d20)

Isso significa que o 3d6 é uma curva de sino apertada em volta de 10 e 11, enquanto o d20 é uma reta (cada valor de 1 a 20 tem exatamente a mesma chance de sair). Na prática, isso muda o peso de cada modificador dependendo de onde o número necessário cai:

- Se o número necessário está abaixo da média (menos de 10-11), no 3d6 fica muito mais fácil de bater do que no d20, porque a curva de sino empilha a maior parte da probabilidade logo acima da média.
- Se está acima da média, no 3d6 fica muito mais difícil de bater do que no d20, porque a probabilidade despenca rápido perto dos extremos (3 e 18).
- Só perto do meio (número necessário 10 ou 11) os dois dados dão resultados parecidos.

### Comparando com os mesmos números da sua fórmula

Sem Precisão:

| Nível | Número necessário | Chance de resistir (d20) | Chance de resistir (3d6) |
|---|---|---|---|
| 1 | 6 | 75% | 95% |
| 5 | 7 | 70% | 91% |
| 10 | 8 | 65% | 84% |
| 15 | 9 | 60% | 74% |
| 20 | 10 | 55% | 62,5% |

Com Precisão:

| Nível | Número necessário | Chance de resistir (d20) | Chance de resistir (3d6) |
|---|---|---|---|
| 1 | 8 | 65% | 84% |
| 5 | 9 | 60% | 74% |
| 10 | 10 | 55% | 62,5% |
| 15 | 11 | 50% | 50% |
| 20 | 12 | 45% | 37,5% |

Repare no padrão: como os números necessários da sua fórmula (6 a 12) ficam, na maioria dos casos, abaixo ou bem perto da média do 3d6 (10,5), portar a fórmula direto para 3d6 empurra a chance de resistência do inimigo para cima em quase todos os níveis — o oposto do que você quer se está preocupado com "inimigo passando sempre". O caso mais extremo é o nível 1 sem Precisão: 75% no d20 vira 95% no 3d6.

A exceção fica na ponta mais alta da progressão: no nível 15 com Precisão os dois dados empatam em 50% (o número necessário, 11, cai bem no meio da curva dos dois), e só no nível 20 com Precisão o 3d6 passa a favorecer mais o conjurador do que o d20 (37,5% contra 45% de chance de resistência), porque aí o número necessário (12) já passou da média e a curva de sino faz esse valor ficar raro de superar.

### Outro efeito colateral: extremos ficam raríssimos

Se seu sistema usa regra de "1 natural = falha automática" ou "20 natural = sucesso automático" em Testes de Resistência, esse tipo de efeito praticamente desaparece no 3d6: tirar o valor mínimo (3, ou seja, 1-1-1) ou o máximo (18, ou seja, 6-6-6) tem só 1 chance em 216 (aproximadamente 0,46%) cada, contra 5% no d20. Se seu sistema depende desse tipo de regra em Testes de Resistência, o 3d6 sozinho já muda esse comportamento, mesmo sem mexer em mais nada.

## 6. Se for migrar para 3d6 mesmo assim

Não dá para só trocar "role 1d20" por "role 3d6" no texto da regra e manter os mesmos números. Algumas ideias caso decida seguir por esse caminho:

- Redesenhe a fórmula pensando em 10-11 como o centro "cara ou coroa", em vez de pensar em "cada ponto vale 5%" — isso só é verdade perto do centro no 3d6; nas pontas vale muito menos.
- Considere encolher os modificadores. Como cada ponto pesa quase o dobro perto do meio no 3d6 (por causa do desvio-padrão menor), uma escala de "metade do nível" pode ficar exagerada. Muitos sistemas baseados em 3d6 (como GURPS) usam modificadores bem menores, tipicamente entre -4 e +4, exatamente por causa disso.
- Aceite que o jogo vai ficar mais "decisivo" nas pontas (quando um lado já está favorecido, o resultado vira quase garantido) e mais sensível no meio (qualquer +1 perto do 50/50 pesa muito mais do que pesava no d20). É uma mudança de sensação de jogo, não só de matemática.

## Resumo

- d20 com os números atuais: está bem calibrado. A chance de resistência do inimigo fica entre 45% e 75%, sem extremos, e Precisão vale sempre exatamente 10 pontos percentuais em qualquer nível.
- Não, os inimigos não vão passar sempre. O ponto mais generoso para eles é justamente nível 1 sem Precisão (75%), e mesmo assim está longe de "sempre".
- 3d6 muda muito, e não é uma troca neutra. Tem a mesma média do d20 (10,5), mas desvio-padrão quase pela metade. Com os números atuais da sua fórmula, a troca pioraria o problema que você teme nos níveis baixos (75% → 95% de resistência no nível 1) e só favoreceria mais o conjurador nos níveis mais altos com Precisão.
- Se for para 3d6, trate como um redesenho da curva de dificuldade, não como uma simples troca de dado.
