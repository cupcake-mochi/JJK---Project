# Medida das Origens do R46 — 13/10/2026

O Mizuki pediu: "Faça uma medida de balanceamento / as origens estão boas? legais? justas?". A conta é exata, por enumeração dos dados, sem sorteio, e está em `origens_medida.py`, nesta pasta. A régua é o teste de paridade do livro: CD 8 + atributo + Maestria contra d20 + atributo + Maestria, que pede 8 no dado.

## O que ele decidiu com a medida

- **Ataque sem Prenúncio:** muda a ordem do anúncio (item 194, aplicado no R47). "Apoio na realidade, pode ser".
- **Tentativa e Erro, do Latente:** fica como está. "latente fica".
- **Regeneração Orgânica, do Híbrido:** não mexe.

## A saída do script

```
==============================================================================
0. A RÉGUA: teste de paridade do livro (precisa de 8 no d20)
==============================================================================
  chance sem nada:  65.0%
  com vantagem, ou repetindo a falha:  87.8%  (ganho +22.8 pontos)
  somando Maestria 1:  70.0%  (ganho  +5.0)
  somando Maestria 2:  75.0%  (ganho +10.0)
  somando Maestria 3:  80.0%  (ganho +15.0)
  somando Maestria 4:  85.0%  (ganho +20.0)
  somando 1d4:  77.5%  (ganho +12.5)
     o d4 do Encarnado entra depois do dado: gasto só quando faltou de 1 a 4, ele salva  62.5% dessas falhas
  piso 10 (Certeza Momentânea) ou 10 fixo (Fundamento Incorporado): 100.0%  (ganho +35.0)

==============================================================================
1. LATENTE — Tentativa e Erro: PE poupados por uso, em média
==============================================================================
  nível  2 (Maestria 1, Classe 1, feitiço de 3 PE, variação 1): desperdício  40.0%, controle  40.0%, média +0.00 PE por uso =   0.0% do custo
  nível 10 (Maestria 2, Classe 3, feitiço de 9 PE, variação 2): desperdício  35.0%, controle  45.0%, média +0.20 PE por uso =   2.2% do custo
  nível 18 (Maestria 3, Classe 5, feitiço de 15 PE, variação 3): desperdício  30.0%, controle  50.0%, média +0.60 PE por uso =   4.0% do custo
  nível 26 (Maestria 4, Classe 7, feitiço de 21 PE, variação 4): desperdício  25.0%, controle  55.0%, média +1.20 PE por uso =   5.7% do custo
  níveis em que a média é zero: 1 a 9

==============================================================================
2. RECEPTÁCULO
==============================================================================
  nível  2: Coexistência dá 2 feitiços além dos 3 espaços (+66.7%); Conflito recupera 2 a 4 PE por dia = 16.7% a 40.0% do máximo
  nível 10: Coexistência dá 2 feitiços além dos 9 espaços (+22.2%); Conflito recupera 6 a 8 PE por dia = 10.0% a 16.0% do máximo
  nível 18: Coexistência dá 2 feitiços além dos 15 espaços (+13.3%); Conflito recupera 10 a 12 PE por dia = 9.3% a 13.3% do máximo
  nível 26: Coexistência dá 2 feitiços além dos 21 espaços (+9.5%); Conflito recupera 14 a 16 PE por dia = 9.0% a 12.3% do máximo

==============================================================================
3. DESCENDENTE — o que cada clã entrega por dia
==============================================================================
  Kamo, Execução Ensaiada: os dois dados guardados valem em média 15.5 e 10.5; passam na paridade  95.7% e  71.8%
     soma dos dois ganhos sobre o teste comum: +37.5 pontos por dia, e você escolhe onde gastar sabendo o valor
  nível  2: Zenin 1 vantagem(ns) em Atletismo/Acrobacia + 1 TR repetido + 1 Exaustão a menos | Kamo 2 dados guardados + 1 acerto(s) repetido(s) | Gojo 1 vantagem(ns) em feitiço da lista + 1 TR(s) repetido(s) com a Reação
  nível 10: Zenin 2 vantagem(ns) em Atletismo/Acrobacia + 1 TR repetido + 1 Exaustão a menos | Kamo 2 dados guardados + 2 acerto(s) repetido(s) | Gojo 2 vantagem(ns) em feitiço da lista + 2 TR(s) repetido(s) com a Reação
  nível 18: Zenin 3 vantagem(ns) em Atletismo/Acrobacia + 1 TR repetido + 1 Exaustão a menos | Kamo 2 dados guardados + 3 acerto(s) repetido(s) | Gojo 3 vantagem(ns) em feitiço da lista + 3 TR(s) repetido(s) com a Reação
  nível 26: Zenin 4 vantagem(ns) em Atletismo/Acrobacia + 1 TR repetido + 1 Exaustão a menos | Kamo 2 dados guardados + 4 acerto(s) repetido(s) | Gojo 4 vantagem(ns) em feitiço da lista + 4 TR(s) repetido(s) com a Reação
  repetir depois de errar gasta o uso só quando errou; declarar vantagem antes gasta sempre: por uso gasto, a repetição rende 2.9 vez(es) a vantagem declarada

==============================================================================
4. HÍBRIDO — Regeneração Orgânica contra a Energia Reversa do livro
==============================================================================
  nível  2: até 1 PE por uso, cura média  3.5; com Constituição 3 são 2 usos por cena =  7.0 PV por 2 PE; isso é 36.8% a 43.8% da vida máxima
  nível 10: até 3 PE por uso, cura média 10.5; com Constituição 3 são 2 usos por cena = 21.0 PV por 6 PE; isso é 25.3% a 29.2% da vida máxima
  nível 18: até 5 PE por uso, cura média 17.5; com Constituição 3 são 2 usos por cena = 35.0 PV por 10 PE; isso é 23.8% a 27.3% da vida máxima
  nível 26: até 7 PE por uso, cura média 24.5; com Constituição 3 são 2 usos por cena = 49.0 PV por 14 PE; isso é 23.2% a 26.6% da vida máxima
  por PE: Regeneração 3.5 PV (Ação Bônus, nível 1) | Energia Reversa como Bônus 2.5 PV | como Padrão 4.5 PV (as duas pedem nível 14 e Refino 7)

==============================================================================
5. CORPO AMALDIÇOADO — reparo no descanso curto
==============================================================================
  teste em paridade:  65.0% de recuperar metade da vida =  32.5% da vida máxima por descanso curto, em média
  com a repetição diária da Manutenção Precisa:  87.8% =  43.9% da vida máxima
  Reparo Autônomo (menor, 1 por dia, Ação Padrão):  65.0% de recuperar 30% =  19.5% da vida máxima

==============================================================================
6. SEM ENERGIA — Ataque sem Prenúncio (2 PE)
==============================================================================
  ataque que acerta a Defesa com 8+ (65.0%): contra Bloquear normal 64.8%, contra Bloquear com desvantagem 76.2%
  ataque que acerta a Defesa com 10+ (55.0%): contra Bloquear normal 55.0%, contra Bloquear com desvantagem 66.6%
  ataque que acerta a Defesa com 12+ (45.0%): contra Bloquear normal 45.0%, contra Bloquear com desvantagem 56.6%
  (sem contar Aparar e Brecha, que são o duplo 10 e o duplo 1)
  nível  2: os 2 PE são 20.0% a 16.7% do máximo |  nível 10: os 2 PE são 4.0% a 3.3% do máximo |  nível 18: os 2 PE são 2.2% a 1.9% do máximo |  nível 26: os 2 PE são 1.5% a 1.3% do máximo |

==============================================================================
7. RESTRIÇÃO CORPORAL — Saída Elevada
==============================================================================
  Classe 1: +1 ponto(s) sobre 3 = 33.3% a mais de montagem (em dano, +1d8 se o feitiço compra pelo menos 1 ponto(s) de Melhoria)
  Classe 2: +1 ponto(s) sobre 6 = 16.7% a mais de montagem (em dano, +1d8 se o feitiço compra pelo menos 1 ponto(s) de Melhoria)
  Classe 3: +1 ponto(s) sobre 9 = 11.1% a mais de montagem (em dano, +1d8 se o feitiço compra pelo menos 1 ponto(s) de Melhoria)
  Classe 4: +2 ponto(s) sobre 12 = 16.7% a mais de montagem (em dano, +2d8 se o feitiço compra pelo menos 2 ponto(s) de Melhoria)
  Classe 5: +2 ponto(s) sobre 15 = 13.3% a mais de montagem (em dano, +2d8 se o feitiço compra pelo menos 2 ponto(s) de Melhoria)
  Classe 6: +3 ponto(s) sobre 18 = 16.7% a mais de montagem (em dano, +3d8 se o feitiço compra pelo menos 3 ponto(s) de Melhoria)
  Classe 7: +3 ponto(s) sobre 21 = 14.3% a mais de montagem (em dano, +3d8 se o feitiço compra pelo menos 3 ponto(s) de Melhoria)
  o preço: Defesa 0, e o livro não tem erro automático no 1 natural. Um ataque que acertaria com 10+ (55.0%) passa a acertar 100.0% -> 1.82 vez(es) os acertos

==============================================================================
8. MENORES QUE AUMENTAM OS PE MÁXIMOS
==============================================================================
  nível  2, Essência 2: Reserva Excedente +4 PE (40.0% do máximo de 5 por nível) | Núcleo Dependente +2 PE (20.0%)
  nível 10, Essência 3: Reserva Excedente +6 PE (12.0% do máximo de 5 por nível) | Núcleo Dependente +5 PE (10.0%)
  nível 18, Essência 4: Reserva Excedente +8 PE (8.9% do máximo de 5 por nível) | Núcleo Dependente +12 PE (13.3%)
  nível 26, Essência 5: Reserva Excedente +10 PE (7.7% do máximo de 5 por nível) | Núcleo Dependente +17 PE (13.1%)
  nível 30, Essência 6: Reserva Excedente +12 PE (8.0% do máximo de 5 por nível) | Núcleo Dependente +27 PE (18.0%)

==============================================================================
9. PISO 10 uma vez por dia: Certeza Momentânea (Latente) x Fundamento Incorporado (Descendente)
==============================================================================
  precisa de  6: comum  75.0% | Certeza (menor que 10 vira 10) 100.0% | Fundamento (o dado é 10) 100.0%
  precisa de  8: comum  65.0% | Certeza (menor que 10 vira 10) 100.0% | Fundamento (o dado é 10) 100.0%
  precisa de 10: comum  55.0% | Certeza (menor que 10 vira 10) 100.0% | Fundamento (o dado é 10) 100.0%
  precisa de 11: comum  50.0% | Certeza (menor que 10 vira 10)  50.0% | Fundamento (o dado é 10)   0.0%
  precisa de 13: comum  40.0% | Certeza (menor que 10 vira 10)  40.0% | Fundamento (o dado é 10)   0.0%
  precisa de 15: comum  30.0% | Certeza (menor que 10 vira 10)  30.0% | Fundamento (o dado é 10)   0.0%
```

## O que a medida não cobre

Dano por rodada de cada Origem numa luta inteira, que pediria supor Caminho, atributos e o andamento da luta; o Talento de Categoria de Efeito 4 e a Reserva Condensada, que são combinados com o mestre e não têm número.
