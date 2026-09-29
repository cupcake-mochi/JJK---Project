# Quantas rodadas dura a luta — pela matemática de cada sistema (leva 2, agente A)

*28/09/2026. Arquivos nesta pasta: `NOTAS-matematica.md` (cada tabela transcrita, com URL e marca, e cada suposição), `conta-rodadas.py` (parte das tabelas transcritas e imprime tudo; `python3 conta-rodadas.py`, sai com código 0). Os números deste arquivo vêm da saída do script.*

**Marcas.** `[C]` texto da regra citado · `[F]` fonte oficial secundária (SRD, prévia) · `[I]` inferência ou conta própria. Toda linha de tabela abaixo é `[I]`: é conta minha sobre tabelas `[C]`/`[F]`. As URLs estão nas notas, marco por marco.

**Como ler.**
- *Rodadas* = vida do chefe ÷ (N × dano esperado de um personagem por rodada, com a chance de acerto contra a defesa do chefe).
- *Pressão* = dano esperado do chefe por rodada × rodadas ÷ (N × vida de um personagem).
- *vida/rod* = dano do chefe por rodada ÷ vida de um personagem. A conta de hoje do Mizuki usa 0,9.
  - A pressão implícita da conta de hoje (4 pessoas, 3 rodadas, 0,9 por rodada) é 0,9 × 3 ÷ 4 = **0,675**.
- Cada célula é a faixa entre os níveis de referência do sistema (começo, meio e fim).
- "não faz" quer dizer que o sistema não põe um chefe sozinho ali.

**O personagem de referência** é o guerreiro de cada sistema (a Fúria no Draw Steel), só com o que a classe dá sozinha (no D&D, também a subclasse Campeão, a única do SRD, e o estilo Defense, que o texto recomenda). Não entra talento escolhido, recurso por descanso nem item mágico. A exceção são as runas do PF2e, pelo calendário publicado da Automatic Bonus Progression. A lista de suposições de cada um está nas notas. Ele é o mais resistente do grupo, então a pressão sobre um conjurador seria maior.

## 1. Um sistema por vez

### Chefe sozinho (rodadas · pressão)

**Pathfinder 2e — chefe sozinho, níveis 3, 10 e 20 (rodadas · pressão; faixa entre os três níveis)**

| dificuldade | N=1 | N=2 | N=3 | N=4 | N=5 | N=6 |
|---|---|---|---|---|---|---|
| trivial | 0,3-2,9 · 0,02-0,23 | 0,5-2,2 · 0,03-0,14 | 0,6-1,7 · 0,04-0,10 | 0,8-1,6 · 0,06-0,10 | 0,6-1,3 · 0,04-0,06 | 0,9-1,3 · 0,05-0,07 |
| baixa | não faz | 0,5-2,2 · 0,03-0,14 | 1,0-2,2 · 0,10-0,18 | 1,3-2,0 · 0,11-0,15 | 1,5-2,2 · 0,13-0,18 | 1,3-1,8 · 0,09-0,13 |
| moderada | 1,0-4,3 · 0,10-0,55 | 1,5-3,3 · 0,23-0,41 | 1,7-2,6 · 0,20-0,27 | 1,9-2,8 · 0,20-0,29 | 1,5-2,2 · 0,13-0,18 | 2,0-2,2 · 0,12-0,26 |
| severa | 1,8-5,1 · 0,36-0,88 | 2,6-3,9 · 0,45-0,60 | 2,5-3,7 · 0,36-0,51 | 3,0-3,3 · 0,28-0,59 | 2,4-2,6 · 0,18-0,38 | não faz |
| extrema | 3,1-6,5 · 0,92-1,62 | 3,8-5,5 · 0,82-1,15 | 4,0-4,4 · 0,50-1,04 | 4,2-4,7 · 0,49-1,01 | não faz | não faz |

**D&D 2024 — chefe sozinho, níveis 3, 10 e 17**

| dificuldade | N=1 | N=2 | N=3 | N=4 | N=5 | N=6 |
|---|---|---|---|---|---|---|
| baixa | 2,5-3,4 · 0,29-0,65 | 1,8-2,8 · 0,15-0,46 | 1,8-2,1 · 0,17-0,35 | 1,6-2,0 · 0,10-0,27 | 1,6-1,7 · 0,14-0,22 | 1,4-1,6 · 0,09-0,21 |
| moderada | 3,6-5,3 · 0,60-1,42 | 2,7-3,1 · 0,38-0,78 | 2,1-2,6 · 0,17-0,47 | 2,1-2,3 · 0,21-0,48 | 1,8-2,1 · 0,20-0,31 | 1,5-1,9 · 0,14-0,29 |
| alta | 3,6-5,7 · 0,60-2,62 | 4,0-4,2 · 0,78-1,34 | 2,9-3,5 · 0,56-0,85 | 2,3-2,9 · 0,31-0,65 | 2,1-2,9 · 0,37-0,48 | 2,0-2,7 · 0,33-0,46 |

**Draw Steel — solo, níveis 1, 5 e 10**

| dificuldade | N=1 | N=2 | N=3 | N=4 | N=5 | N=6 |
|---|---|---|---|---|---|---|
| trivial | não faz | não faz | não faz | não faz | não faz | não faz |
| fácil | não faz | não faz | não faz | não faz | não faz | não faz |
| padrão | não faz | não faz | não faz | não faz | 3,4-4,6 · 0,67-1,06 | 2,8-3,8 · 0,46-0,74 |
| difícil | não faz | não faz | 5,6-7,6 · 1,85-2,96 | 4,2-5,7 · 1,04-1,66 | 4,2-5,1 · 0,75-1,46 | não faz |
| extremo | 16,8-22,8 · 8,33-13,31 | 8,4-11,4 · 4,16-6,66 | 7,0-8,6 · 2,08-4,04 | não faz | não faz | não faz |

**13th Age — chefe que vale N, níveis 1, 5 e 10**

| dificuldade | N=1 | N=2 | N=3 | N=4 | N=5 | N=6 |
|---|---|---|---|---|---|---|
| justa | 4,2-7,6 · 0,41-1,86 | 4,2-7,6 · 0,41-1,86 | 4,2-7,6 · 0,41-1,86 | 4,1-7,4 · 0,50-1,77 | 3,4-6,1 · 0,33-1,18 | 4,0-7,1 · 0,47-1,50 |

- **PF2e.** O chefe é o nível mais alto que cabe no orçamento de XP com o ajuste por personagem. PV moderado, CA, ataque e dano altos, pela tabela de criação do GM Core. Ele e o guerreiro dão 2 golpes por rodada. Na extrema com 5 ou 6 e na severa com 6, o orçamento passa do +4, onde a tabela acaba.
- **D&D 2024.** O chefe é o maior ND que cabe em orçamento × N. Vida, CA e dano são a média de todos os blocos do SRD 5.2 naquele ND, e ND com menos de 3 blocos junta com os vizinhos. O dano do monstro conta Multiattack e ações lendárias de ataque. Sopro, magia e área ficam fora, e isso subestima dragão e conjurador.
- **Draw Steel.** O solo vale 6 espaços, mais 1 por nível acima, e pode ficar no máximo 1 nível acima. Vigor e dano saem das fórmulas de criação, que batem com os 22 solos do bestiário. Com 1 a 6 heróis, o solo não cabe em trivial nem em fácil. O dano do solo é só a assinatura (2 turnos, 2 alvos), sem ação de vilão nem Malícia: é um piso. O herói tem 10 Recoveries, e por isso pressão acima de 1 ali pede cura, e não quer dizer morte.
- **13th Age.** O SRD tem uma dificuldade só, a batalha justa de N equivalentes. O chefe é o monstro que vale N: normal, grande ou enorme, subindo de nível. Com N = 5 não há um que valha 5, e uso o enorme que vale 4. O guerreiro soma o dado de escalada. O nível 10 sai longo porque não tem item mágico.

### Encontro padrão: vários inimigos do nível do grupo (rodadas · pressão) `[I]`

**Encontro padrão (vários inimigos do nível do grupo, com foco), rodadas · pressão, faixa entre os níveis**

| sistema e dificuldade | N=1 | N=2 | N=3 | N=4 | N=5 | N=6 |
|---|---|---|---|---|---|---|
| PF2e trivial | 0,8-1,6 · 0,14-0,25 | 0,8-1,6 · 0,09-0,15 | 0,8-1,6 · 0,07-0,12 | 0,8-1,6 · 0,06-0,10 | 0,8-1,6 · 0,05-0,09 | 0,8-1,6 · 0,05-0,08 |
| PF2e baixa | não faz | 0,8-1,6 · 0,09-0,15 | 1,0-2,2 · 0,10-0,18 | 1,1-2,4 · 0,11-0,19 | 1,2-2,6 · 0,11-0,19 | 1,3-2,7 · 0,11-0,20 |
| PF2e moderada | 1,5-3,3 · 0,34-0,61 | 1,5-3,3 · 0,23-0,41 | 1,5-3,3 · 0,19-0,34 | 1,5-3,3 · 0,17-0,30 | 1,5-3,3 · 0,16-0,28 | 1,5-3,3 · 0,15-0,27 |
| PF2e severa | 2,3-4,9 · 0,60-1,06 | 2,3-4,9 · 0,43-0,76 | 2,3-4,9 · 0,37-0,66 | 2,3-4,9 · 0,34-0,61 | 2,3-4,9 · 0,33-0,58 | 2,3-4,9 · 0,32-0,56 |
| PF2e extrema | 3,1-6,5 · 0,92-1,62 | 3,1-6,5 · 0,69-1,22 | 3,1-6,5 · 0,61-1,08 | 3,1-6,5 · 0,57-1,01 | 3,1-6,5 · 0,55-0,97 | 3,1-6,5 · 0,54-0,95 |
| D&D 2024 baixa | 1,8-2,1 · 0,44-0,67 | 1,8-2,1 · 0,26-0,40 | 1,8-2,1 · 0,20-0,31 | 1,8-2,1 · 0,17-0,27 | 1,8-2,1 · 0,15-0,24 | 1,8-2,1 · 0,14-0,22 |
| D&D 2024 moderada | 2,7-3,1 · 0,72-1,20 | 2,7-3,1 · 0,45-0,77 | 2,7-3,1 · 0,36-0,63 | 2,7-3,1 · 0,31-0,56 | 2,7-3,1 · 0,28-0,52 | 2,7-3,1 · 0,27-0,49 |
| D&D 2024 alta | 4,2-4,9 · 1,26-2,31 | 4,2-4,9 · 0,84-1,61 | 4,2-4,9 · 0,71-1,37 | 4,2-4,9 · 0,64-1,26 | 4,2-4,9 · 0,60-1,19 | 4,2-4,9 · 0,57-1,14 |
| Draw Steel trivial | não faz | não faz | 0,8-1,3 · 0,07-0,08 | 1,3-2,0 · 0,12-0,14 | 1,5-2,4 · 0,16-0,18 | 1,7-2,7 · 0,18-0,20 |
| Draw Steel fácil | não faz | 1,3-2,0 · 0,17-0,18 | 1,7-2,7 · 0,22-0,25 | 1,9-3,0 · 0,25-0,28 | 2,0-3,2 · 0,27-0,29 | 2,1-3,4 · 0,28-0,31 |
| Draw Steel padrão | 5,0-8,1 · 1,99-2,21 | 3,8-6,0 · 1,00-1,10 | 3,4-5,4 · 0,74-0,82 | 3,1-5,0 · 0,62-0,69 | 3,0-4,8 · 0,56-0,62 | 2,9-4,7 · 0,52-0,57 |
| Draw Steel difícil | 10,1-16,1 · 6,64-7,36 | 6,3-10,1 · 2,49-2,76 | 5,0-8,1 · 1,55-1,72 | 4,4-7,0 · 1,16-1,29 | 4,0-6,4 · 0,96-1,06 | 3,8-6,0 · 0,83-0,92 |
| Draw Steel extremo | 12,6-20,1 · 9,96-11,04 | 7,5-12,1 · 3,49-3,87 | 5,9-9,4 · 2,07-2,29 | 5,0-8,1 · 1,49-1,66 | 4,5-7,2 · 1,20-1,33 | 4,2-6,7 · 1,01-1,12 |
| 13th Age justa | 4,2-7,6 · 0,41-1,86 | 4,2-7,6 · 0,31-1,45 | 4,2-7,6 · 0,28-1,30 | 4,2-7,6 · 0,27-1,23 | 4,2-7,6 · 0,26-1,18 | 4,2-7,6 · 0,25-1,15 |

- O número de inimigos: no PF2e, orçamento ÷ 40 (criatura do nível do grupo); no D&D, orçamento ÷ XP de um monstro de ND = nível; no Draw Steel, criaturas de pelotão pelos espaços (N − 2, N − 1, N + 1, N + 3, N + 4); no 13th Age, N normais do nível que vale 1. O grupo derruba um de cada vez.
- No PF2e, no D&D e no 13th Age as rodadas não mudam com o N, porque o número de inimigos cresce junto com o N (a baixa do PF2e é a exceção: 20N − 20). O herói de referência só bate em um alvo, então as lutas de vários inimigos do Draw Steel saem compridas demais, já que lá o herói tem muita área.

## 2. As dificuldades nos cinco degraus

Alinhamento `[I]`: PF2e e Draw Steel têm cinco dificuldades e entram na ordem. O D&D 2024 tem três, e a alta ("could be lethal for one or more characters", SRD 5.2.1 p. 202) tem o risco da severa do PF2e: baixa, moderada e alta vão para Ameaça, Desastre e Catástrofe. A batalha justa do 13th Age é a luta comum do dia de aventura e vai para Desastre.

| degrau | hipótese | sistema (dificuldade) | N=1 | N=2 | N=3 | N=4 | N=5 | N=6 | vida/rod em N=4 | pressão em N=4 |
|---|---|---|---|---|---|---|---|---|---|---|
| Capanga | 2 | PF2e (trivial) | 0,3-2,9 | 0,5-2,2 | 0,6-1,7 | 0,8-1,6 | 0,6-1,3 | 0,9-1,3 | 0,20-0,30 | 0,06-0,10 |
| Capanga | 2 | Draw Steel (trivial) | — | — | — | — | — | — | — | — |
| Ameaça | 2,5 | PF2e (baixa) | — | 0,5-2,2 | 1,0-2,2 | 1,3-2,0 | 1,5-2,2 | 1,3-1,8 | 0,23-0,45 | 0,11-0,15 |
| Ameaça | 2,5 | D&D 2024 (baixa) | 2,5-3,4 | 1,8-2,8 | 1,8-2,1 | 1,6-2,0 | 1,6-1,7 | 1,4-1,6 | 0,25-0,60 | 0,10-0,27 |
| Ameaça | 2,5 | Draw Steel (fácil) | — | — | — | — | — | — | — | — |
| Desastre | 3 | PF2e (moderada) | 1,0-4,3 | 1,5-3,3 | 1,7-2,6 | 1,9-2,8 | 1,5-2,2 | 2,0-2,2 | 0,30-0,56 | 0,20-0,29 |
| Desastre | 3 | D&D 2024 (moderada) | 3,6-5,3 | 2,7-3,1 | 2,1-2,6 | 2,1-2,3 | 1,8-2,1 | 1,5-1,9 | 0,40-0,82 | 0,21-0,48 |
| Desastre | 3 | Draw Steel (padrão) | — | — | — | — | 3,4-4,6 | 2,8-3,8 | — | — |
| Desastre | 3 | 13th Age (justa) | 4,2-7,6 | 4,2-7,6 | 4,2-7,6 | 4,1-7,4 | 3,4-6,1 | 4,0-7,1 | 0,42-0,96 | 0,50-1,77 |
| Catástrofe | 4 | PF2e (severa) | 1,8-5,1 | 2,6-3,9 | 2,5-3,7 | 3,0-3,3 | 2,4-2,6 | — | 0,34-0,78 | 0,28-0,59 |
| Catástrofe | 4 | D&D 2024 (alta) | 3,6-5,7 | 4,0-4,2 | 2,9-3,5 | 2,3-2,9 | 2,1-2,9 | 2,0-2,7 | 0,48-0,89 | 0,31-0,65 |
| Catástrofe | 4 | Draw Steel (difícil) | — | — | 5,6-7,6 | 4,2-5,7 | 4,2-5,1 | — | 0,76-1,59 | 1,04-1,66 |
| Calamidade | 5 | PF2e (extrema) | 3,1-6,5 | 3,8-5,5 | 4,0-4,4 | 4,2-4,7 | — | — | 0,41-0,95 | 0,49-1,01 |
| Calamidade | 5 | Draw Steel (extremo) | 16,8-22,8 | 8,4-11,4 | 7,0-8,6 | — | — | — | — | — |

| degrau | hipótese | N = 4, todos os sistemas | mediana em N = 4 | N de 1 a 6, todos os sistemas | mediana de 1 a 6 |
|---|---|---|---|---|---|
| Capanga | 2 | 0,8-1,6 | 1,5 | 0,3-2,9 | 1,3 |
| Ameaça | 2,5 | 1,3-2,0 | 1,8 | 0,5-3,4 | 1,8 |
| Desastre | 3 | 1,9-7,4 | 2,7 | 1,0-7,6 | 3,0 |
| Catástrofe | 4 | 2,3-5,7 | 3,3 | 1,8-7,6 | 3,5 |
| Calamidade | 5 | 4,2-4,7 | 4,7 | 3,1-22,8 | 6,0 |

## 3. O que isso diz da hipótese 2 · 2,5 · 3 · 4 · 5

- **A ordem e o passo batem.** Com 4 personagens, a mediana dos sistemas é 1,5 · 1,8 · 2,7 · 3,3 · 4,7 rodadas. Cada degrau dura mais que o de baixo, e o salto maior fica entre a Catástrofe e a Calamidade, como na hipótese.
- **Desastre 3, Catástrofe 4 e Calamidade 5 caem dentro do que os sistemas medem.**
  - Desastre: PF2e 1,9-2,8, D&D 2,1-2,3, Draw Steel 2,8-4,6 (com 5 e 6 heróis) e 13th Age 4,1-7,4.
  - Catástrofe: PF2e 3,0-3,3, D&D 2,3-2,9 e Draw Steel 4,2-5,7.
  - Calamidade: o PF2e dá 4,2-4,7. É o único sistema que monta um chefe extremo para 4.
- **Capanga 2 e Ameaça 2,5 saem mais longos que qualquer chefe sozinho medido com 4 personagens.**
  - A trivial do PF2e dá 0,8-1,6. A baixa dá 1,3-2,0 no PF2e e 1,6-2,0 no D&D.
  - Nos encontros de vários inimigos, a Ameaça chega a 2,5 só no Draw Steel fácil (1,9-3,0 com 4).
- **A pressão da conta de hoje é a de um degrau mais alto.** A conta de hoje (0,9 da vida de um personagem por rodada, por 3 rodadas, com 4) dá 0,675. Com 4, PF2e e D&D dão:
  - moderada: 0,20-0,29 e 0,21-0,48;
  - severa/alta: 0,28-0,59 e 0,31-0,65;
  - extrema do PF2e: 0,49-1,01.

  No 13th Age e no Draw Steel, a batalha comum já passa de 0,5, mas lá o personagem tem Recoveries e a tabela de monstro conta com elas.
- **O 0,9 por rodada aparece nos sistemas em algumas células de cima:** no PF2e extremo no nível 3 (0,95), no D&D alto nos níveis 10 e 17 (0,80 e 0,89) e no Draw Steel difícil. Em todos, o número cai com o nível: no PF2e extremo, 0,95 no 3, 0,60 no 10 e 0,41 no 20.

## 4. O que muda com o N

- **Nos sistemas de orçamento (PF2e e D&D), a luta contra um chefe sozinho encurta quando o grupo cresce.** Com N = 6, as rodadas ficam entre 0,32 e 0,75 das de N = 1 no D&D, e entre 0,44 e 1,06 no PF2e dos níveis 10 e 20. Com 1 ou 2 personagens a luta fica longa e pesada: no D&D alto com N = 1, 3,6-5,7 rodadas e pressão 0,60-2,62.
  - O motivo é que o orçamento cresce linear com o N e o chefe sobe de nível ou de ND. A vida do chefe cresce mais devagar que o dano somado do grupo.
- **A exceção é o PF2e no nível 3.** Lá a luta alonga com o N (razão de 1,31 a 2,55), porque a criatura de nível alto tem CA que o guerreiro de nível 3 quase não acerta.
- **No Draw Steel o solo é o mesmo bloco para 3, 4, 5 ou 6.** As rodadas caem com o N: razão de 0,36 a 0,83. O livro diz o mesmo em texto: o solo é para 4 a 6 heróis, e grupos de 3 ou menos sofrem.
- **No 13th Age as rodadas quase não mudam com o N** (razão de 0,93 a 0,97). A pressão também fica parada. "Vale N" ali é vida × N e dano × N, como na grade do Mizuki, e o que cresce com o N é o dano do chefe sobre uma pessoa (vida/rod, de 0,09 a 0,65 no nível 1).
  - **Consequência para a grade:** se a vida do inimigo ×N for exatamente N vezes a de ×1, e cada personagem bater o mesmo, as rodadas não dependem do N. Uma duração por degrau serve de ×1 a ×6. Os sistemas de orçamento precisam de tabela por N porque não fazem isso.

## 5. Lacunas

- **PF2e:** acima do +4 "o sistema não faz" (extrema com 5 e 6, severa com 6); a baixa com 1 personagem tem orçamento 0. A escolha de PV moderado e CA, ataque e dano altos para o chefe é minha, pelo texto de cada tabela.
- **D&D 2024:** o SRD não tem monstro de ND 18 nem de 25 a 29, e por isso o fim da progressão foi o nível 17. A tabela de estatística por ND é de livro fechado, e a troquei pela média dos blocos do SRD. O dano do monstro não conta sopro, magia nem área. O 2024 não tem trivial nem extrema.
- **Draw Steel:** o dano do solo não conta ação de vilão nem Malícia, que cresce com o N (N + nº da rodada por rodada). O herói é um só (Fúria, alvo único), e a economia de ferocidade é minha (só o ganho garantido, gasto em surge do nível 4 em diante).
- **13th Age:** a regra de montagem da 2ª edição, que "pesa mais em grupo grande", é de livro fechado. Sem item mágico, o nível 10 alonga.
- **Fabula Ultima e Lancer:** o livro de regras de NPC é fechado, e ficaram fora.
- **Daggerheart:** o SRD é aberto, mas o jogo não tem rodada nem iniciativa. Ficou fora.
- **Nos quatro sistemas:** a conta não tem cura, condição, movimento nem foco do chefe num personagem. As rodadas são as de dano puro.
