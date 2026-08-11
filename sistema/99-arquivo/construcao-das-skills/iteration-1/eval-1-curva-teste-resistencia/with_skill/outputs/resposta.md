# Teste de Resistência de área — CD vs bônus de resistência, nível 1 a 20

Rodei os números em vez de estimar de cabeça (script anexo, `curva_teste_resistencia.py`, usa a distribuição exata de dado da skill de balanceamento, não Monte Carlo). Resposta direta primeiro, contas depois.

## Resposta curta

**No d20, os inimigos não vão passar sempre.** A chance deles resistirem (tomar só metade do dano) varia de **75% no nível 1** até **45% no nível 20 com Precisão comprada** — nunca trava perto de 0% nem de 100%. Mas tem uma deriva real: **o feitiço começa fraco e termina forte**. No nível 1 o inimigo resiste na maior parte das vezes (75%); no nível 20 ele passa a falhar na maior parte das vezes (45–55%). Isso não é bug, é consequência direta de você ter dado à CD um ritmo de crescimento (+0,5/nível) mais rápido que o do bônus de resistência que você mesmo definiu (+0,32/nível em média). Se isso é o que você quer — área ficando proporcionalmente mais confiável conforme o jogo avança — os números já fazem isso. Se você queria uma relação estável do nível 1 ao 20, falta bônus no topo (ver seção "em aberto").

**Trocar pra 3d6 muda muito, e muda de um jeito específico.** Não é só "a curva fica mais concentrada" — o efeito principal é que a melhoria Precisão (e qualquer outro +1 fixo na CD) deixa de valer sempre a mesma coisa. No d20 ela vale exatamente 10 pontos percentuais em qualquer nível. No 3d6 ela vale **11,6pp no nível 1 e 25pp no nível 20** — mais que o dobro, sem você ter mudado uma vírgula da regra. E como seus alvos de rolagem (CD menos bônus) ficam quase todos entre 6 e 12 — bem em cima da média de 3d6, que é 10,5 — o sistema inteiro passa a operar exatamente na região onde a curva de sino é mais sensível a qualquer ajuste de número.

## O contrato usado (e o que eu assumi)

Da sua descrição, tomei como fixo:

```
CD(nível) = 8 + metade do nível do conjurador  [+2 se comprou Precisão]
Bônus de resistência do inimigo = +2 no nível 1, +8 no nível 20
Resistiu → metade do dano · Falhou → dano cheio
```

Três coisas você não especificou e eu precisei assumir para rodar a conta. Nenhuma delas muda a conclusão (testei as alternativas, ver "Robustez" no fim), mas estão listadas porque são premissa minha, não fato do seu sistema:

1. **"Metade do nível" arredonda pra baixo** (nível 7 → +3, não +4). Testei com arredondamento pra cima também: a curva desloca 1 ponto em alguns níveis ímpares, a deriva geral não muda.
2. **O bônus de resistência cresce linearmente entre +2 e +8** ao longo dos 19 níveis intermediários, já que você só me deu as duas pontas. Testei arredondando pra cima, pra baixo e pro mais próximo — nos dois extremos (nível 1 e nível 20) todas batem exatamente com os seus números; no meio, a forma da curva balança um pouco, mas a tendência geral (queda) é a mesma nas três.
3. **Análise "no nível"**: conjurador nível L contra inimigo padrão do mesmo nível L, que é a leitura natural de "os inimigos têm bônus de +2 no nível 1 subindo pra +8 no nível 20" — lido como a régua de dificuldade padrão daquele nível. Casos fora da curva (chefe alto nível de área contra mob fraco, ou o inverso) comento à parte mais abaixo, porque o padrão muda de figura.
4. **Sem regra de "1 natural falha / 20 natural passa"** no teste, porque você não mencionou nenhuma. Se o seu sistema tiver isso, ela achata as pontas (nunca 0% nem 100% cravado) — não muda nada no miolo da tabela, que é onde está o problema real.

## O que acontece hoje, no d20

Chance do **inimigo passar** (resistir e tomar só metade do dano), nível a nível:

### Sem a melhoria Precisão

| Nível | Bônus resist. | CD | Alvo no dado | Chance de passar (d20) |
|---:|---:|---:|---:|---:|
| 1  | +2 | 8  | 6  | 75,0% |
| 2  | +2 | 9  | 7  | 70,0% |
| 4  | +3 | 10 | 7  | 70,0% |
| 6  | +4 | 11 | 7  | 70,0% |
| 8  | +4 | 12 | 8  | 65,0% |
| 10 | +5 | 13 | 8  | 65,0% |
| 12 | +5 | 14 | 9  | 60,0% |
| 14 | +6 | 15 | 9  | 60,0% |
| 16 | +7 | 16 | 9  | 60,0% |
| 18 | +7 | 17 | 10 | 55,0% |
| 20 | +8 | 18 | 10 | 55,0% |

### Com a melhoria Precisão

| Nível | Bônus resist. | CD | Alvo no dado | Chance de passar (d20) |
|---:|---:|---:|---:|---:|
| 1  | +2 | 10 | 8  | 65,0% |
| 2  | +2 | 11 | 9  | 60,0% |
| 4  | +3 | 12 | 9  | 60,0% |
| 6  | +4 | 13 | 9  | 60,0% |
| 8  | +4 | 14 | 10 | 55,0% |
| 10 | +5 | 15 | 10 | 55,0% |
| 12 | +5 | 16 | 11 | 50,0% |
| 14 | +6 | 17 | 11 | 50,0% |
| 16 | +7 | 18 | 11 | 50,0% |
| 18 | +7 | 19 | 12 | 45,0% |
| 20 | +8 | 20 | 12 | 45,0% |

(Tabela completa nível a nível, incluindo os ímpares, está na saída do script.)

**Leitura:** em nenhum ponto da progressão o inimigo passa "sempre" (nunca chega a 90%) nem falha "sempre" (nunca cai abaixo de 45%). O sistema está dentro de uma faixa saudável em qualquer nível isolado. O que existe é uma **deriva de 20 pontos percentuais** entre o nível 1 e o nível 20 (75%→55% sem Precisão, 65%→45% com Precisão) — o inimigo perde exatamente 20pp de chance de resistir ao longo de toda a progressão, com ou sem a melhoria. A melhoria Precisão, por sua vez, tem uma propriedade limpa no d20: **vale sempre 10 pontos percentuais, em qualquer nível**. Isso é assim porque no d20 cada +1 de CD vale exatamente 5pp, sempre — é a curva ser achatada (chance uniforme em cada face) que garante isso.

A causa da deriva é aritmética simples: sua CD sobe **meio ponto por nível** (10 pontos ao longo de 19 níveis, de +0 a +10 de bônus de nível). O bônus de resistência que você definiu sobe **cerca de 0,32 por nível** (6 pontos ao longo dos mesmos 19 níveis, de +2 a +8). A CD anda mais rápido que a resistência, e a diferença se acumula: por isso a área começa "fraca contra resistência" e termina "forte contra resistência".

## Isso é bom?

Depende do que você quer que aconteça entre o nível 1 e o nível 20, e isso é decisão sua, não teve como eu calcular:

- **Se a intenção é a área ficar proporcionalmente mais confiável conforme o jogo avança** (por exemplo, para compensar vida de monstro crescendo mais que o dano de alvo único, ou para dar identidade a essa escola de magia em níveis altos), os números atuais já fazem exatamente isso, de forma suave e sem estourar nenhum extremo. Não precisa mexer em nada.
- **Se a intenção era uma relação estável** — o inimigo típico resistindo com a mesma frequência no nível 1 e no nível 20 —, falta bônus de resistência no topo. Pra travar a chance de passar em 75% (o valor do nível 1) também no nível 20, o bônus de resistência no nível 20 precisaria ficar perto de **+11 ou +12**, não +8. Ou seja: seus dois números publicados (+2 e +8) *descrevem* uma deriva de 20pp; se você não quer a deriva, o número a mexer é o teto do bônus de resistência, não a fórmula da CD (mexer na fórmula da CD provavelmente derruba outras contas do sistema que dependem dela).

Nenhuma das duas é "errada" — mas hoje, do jeito que os dois números estão escritos, a deriva existe e provavelmente não foi escolhida de propósito (raramente é, é o tipo de coisa que só aparece quando alguém roda a tabela inteira, que é o que fiz aqui).

## E se trocar d20 por 3d6?

**Muda muito — mais do que "a curva fica mais concentrada".** O efeito que importa pra você é este: com a mesma fórmula de CD e o mesmo bônus de resistência, os alvos que o inimigo precisa tirar no dado (CD − bônus) ficam quase todos entre **6 e 12** ao longo da progressão inteira. Em 3d6 (intervalo 3–18, média 10,5), essa faixa cai bem em cima do miolo da curva de sino — exatamente onde ela é mais alta e mais inclinada. É a pior faixa possível pra trocar de dado sem reajustar os números.

### Mesma tabela, agora comparando os dois dados

| Nível | Alvo (sem Precisão) | Passa no d20 | Passa no 3d6 | Alvo (com Precisão) | Passa no d20 | Passa no 3d6 |
|---:|---:|---:|---:|---:|---:|---:|
| 1  | 6  | 75,0% | **95,4%** | 8  | 65,0% | **83,8%** |
| 8  | 8  | 65,0% | **83,8%** | 10 | 55,0% | **62,5%** |
| 12 | 9  | 60,0% | **74,1%** | 11 | 50,0% | **50,0%** |
| 18 | 10 | 55,0% | **62,5%** | 12 | 45,0% | **37,5%** |
| 20 | 10 | 55,0% | **62,5%** | 12 | 45,0% | **37,5%** |

Dois efeitos aparecem juntos:

**1. No nível 1, a área fica quase inútil.** 95,4% de chance do inimigo resistir (contra 75% no d20) é essencialmente "o feitiço quase nunca faz dano cheio" — o extremo que você estava preocupado que acontecesse no d20 acaba acontecendo no 3d6, só que embaixo, não em cima.

**2. No nível 20 com Precisão, a área fica bem mais forte que no d20.** 37,5% de chance de resistir (contra 45% no d20) significa que o inimigo toma dano cheio quase 2 em cada 3 vezes.

**3. A melhoria Precisão passa a valer mais conforme o personagem sobe de nível — sem nenhuma mudança de regra.** No d20 ela vale 10pp sempre. No 3d6:

| Nível | Precisão vale (d20) | Precisão vale (3d6) |
|---:|---:|---:|
| 1  | 10,0pp | 11,6pp |
| 8  | 10,0pp | 21,3pp |
| 12 | 10,0pp | 24,1pp |
| 20 | 10,0pp | 25,0pp |

A melhoria mais que dobra de valor entre o nível 1 e o nível 20, puramente porque o alvo necessário se aproxima da média da curva conforme o nível sobe. É a mesma melhoria, o mesmo custo, e um efeito real bem diferente dependendo de quando ela foi comprada.

**Por que isso acontece — o mecanismo, não só o sintoma:** o valor de +1 na CD, em pontos percentuais de falha do inimigo, é constante no d20 (5pp, em qualquer alvo) e varia forte no 3d6 conforme o alvo:

| Alvo necessário | +1 de CD vale (d20) | +1 de CD vale (3d6) |
|---:|---:|---:|
| 6  | 5,00pp | 2,78pp |
| 8  | 5,00pp | 6,94pp |
| 10 | 5,00pp | 11,57pp |
| 11 | 5,00pp | 12,50pp (pico) |
| 12 | 5,00pp | 12,50pp |
| 14 | 5,00pp | 9,72pp |

No d20, todo ponto de CD vale o mesmo, sempre — é por isso que Precisão é "só +10pp" em qualquer nível hoje. No 3d6, um ponto de CD vale até **4,5x mais** perto do meio da curva (alvo 11) do que na ponta (alvo 6). Como sua progressão de níveis empurra o alvo necessário de 6 pra 12 exatamente ao longo do jogo, você estaria literalmente caminhando na direção de máxima sensibilidade da curva conforme os personagens sobem de nível. Isso é o oposto do d20, onde não importa aonde você está na tabela — o efeito de qualquer bônus é sempre o mesmo.

Isso também aparece na variância bruta dos dados: o d20 tem desvio-padrão 5,77 (achatado, resultado individual muito mais imprevisível rodada a rodada) contra 2,96 do 3d6 (concentrado). Parece que 3d6 seria "menos aleatório" e mais fácil de prever — e é, rolagem a rolagem — mas o preço disso é que os *modificadores fixos* (CD, bônus de resistência, a própria Precisão) deixam de ter valor previsível: o mesmo +1 significa coisas muito diferentes dependendo de onde a partida em questão cai na curva.

**Nota lateral sobre confrontos fora do nível** (chefe de nível alto usando a área contra mob fraco, ou o inverso): a mesma lógica empurra os casos extremos pra ainda mais extremos no 3d6. Um chefe nível 20 (CD 18–20) de área contra um mob nível 1 (bônus +2) já resiste pouco no d20 (15–25%); no 3d6 isso desaba pra 0,5–4,6% — a área de chefe se torna quase impossível de resistir. No sentido inverso, conjurador nível 1 contra monstro nível 20 (bônus +8): o monstro já resistia quase sempre no d20 (95–100%) e no 3d6 fica cravado em 100% nos dois casos. Não chamaria isso de errado — provavelmente é o comportamento que você quer contra alvos muito fora de nível — mas é bom saber que 3d6 acentua esse efeito, não suaviza.

**Conclusão prática:** trocar o dado sem reajustar a fórmula da CD não é uma troca neutra. Se você migrar pra 3d6, os números de CD e bônus de resistência precisam ser redesenhados pensando na curva de sino (provavelmente com uma faixa de alvos mais estreita e deslocada, e com o crescimento por nível recalibrado), e não apenas copiados do sistema em d20.

## O que continua verdadeiro

- Em nenhum nível, com nenhum dos dois dados, o teste trava em 0% ou 100% dentro do uso normal (conjurador e inimigo do mesmo nível) — os dois pontos que você me deu (+2 no nível 1, +8 no nível 20) conferem exatamente com o modelo.
- No d20, a melhoria Precisão tem valor constante (10pp) em qualquer nível — essa é uma propriedade boa e vale preservar se você mantiver d20.
- A conclusão de que "a chance de passar cai com o nível" e de que "3d6 amplifica esse efeito" se mantém em todas as variações de arredondamento testadas (metade de nível pra cima/pra baixo, interpolação de bônus pra cima/pra baixo/mais próximo) — não é artefato da minha premissa de interpolação, é estrutural.

## O que fica em aberto

- **A deriva de 20pp entre nível 1 e nível 20 no d20 é intencional?** Se não for, o ajuste mais direto é levar o bônus de resistência no nível 20 pra perto de +11/+12 em vez de +8 (mantendo a CD como está), ou redistribuir o crescimento do bônus pra acompanhar +0,5/nível em vez de +0,32/nível.
- **Se migrar pra 3d6 continua na mesa**, os números de CD e resistência precisam de uma segunda rodada de calibração pensada pro 3d6 — não vale copiar a fórmula do d20 e só trocar o dado, porque o nível 1 vira quase-imune (95,4%) e o nível 20 com Precisão vira bem mais letal (37,5%) do que o equivalente em d20.
- Não testei aqui como essa curva interage com o dano médio do feitiço (quanto pesa, em dano esperado por rodada, passar de 55% pra 45% de resistência) — se você quiser, é só passar os números de dano do feitiço que eu rodo essa conta também.

## Nota metodológica

Script: `curva_teste_resistencia.py`, na mesma pasta desta resposta. Usa `soma()` e `p_ao_menos()` de `dados.py` (distribuição exata de 3d6 por enumeração, sem Monte Carlo) e replica a mesma lógica pro d20 em forma fechada. Roda sozinho (`python3 curva_teste_resistencia.py`) e imprime: o contrato, a varredura nível a nível para os dois dados e os dois estados de Precisão, o valor marginal da melhoria por nível, uma checagem de robustez contra 4 combinações de arredondamento, e a regressão contra os dois números que você publicou (+2 no nível 1, +8 no nível 20) — os dois batem exatamente.
