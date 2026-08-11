# Matemática de dado — números de referência

Todos os valores abaixo são cálculo exato de distribuição, não simulação. Para recalcular ou testar variantes, use a skill `balanceamento-simulacao`.

## O que vale um +1

Ganho em pontos percentuais ao somar +1 ao resultado, medido em três faixas de dificuldade.

| Mecânica | Fácil (base ~80%) | Médio (base ~45%) | Difícil (base ~26%) |
|---|---|---|---|
| d20 puro | +5,0 pp (CD 5) | +5,0 pp (CD 11) | +5,0 pp (CD 16) |
| 2d6 | +8,3 pp (alvo 5) | +16,7 pp (alvo 8) | +13,9 pp (alvo 9) |
| 3d6 | +6,9 pp (alvo 8) | +12,5 pp (alvo 11) | +11,6 pp (alvo 13) |

**Consequência de design.** No d20 o valor de um bônus é constante e previsível, o que torna seguro deixar o mestre improvisar bônus. Numa curva de sino o mesmo +1 vale até três vezes mais, e vale mais justamente no meio, onde quase todo teste acontece — então curva de sino exige política restritiva de bônus numérico. Substitua bônus por vantagem, rerrolagem ou mudança de posição.

## Pool contando sucessos (Nd6, cada 4+ conta 1)

| dados | ≥1 sucesso | ≥2 sucessos | o dado a mais rendeu (em ≥2) |
|---|---|---|---|
| 1 | 50,0% | — | — |
| 2 | 75,0% | 25,0% | +25,0 pp |
| 3 | 87,5% | 50,0% | +25,0 pp |
| 4 | 93,8% | 68,8% | +18,8 pp |
| 5 | 96,9% | 81,2% | +12,5 pp |
| 6 | 98,4% | 89,1% | +7,8 pp |
| 7 | 99,2% | 93,8% | +4,7 pp |
| 8 | 99,6% | 96,5% | +2,7 pp |

**Consequência de design.** Pool tem teto embutido. Progressão baseada em quantidade de dados se auto-limita sem regra dizendo "o máximo é X" — o oitavo dado é ruído. Isso é valioso quando o personagem atravessa muitas campanhas e o sistema não pode explodir sozinho.

## Pool estilo Blades (Nd6, olha o maior)

6 é sucesso total, 4-5 é parcial, 1-3 é falha. Dois ou mais 6 dão um bônus em cima do sucesso — **crítico é subconjunto do sucesso total, não categoria concorrente**. Sucesso total real é a soma das duas últimas colunas.

| dados | falha | parcial | total, um 6 | total, dois ou mais 6 | total real |
|---|---|---|---|---|---|
| 0 (pior de 2) | 75,0% | 22,2% | 2,8% | — | 2,8% |
| 1 | 50,0% | 33,3% | 16,7% | — | 16,7% |
| 2 | 25,0% | 44,4% | 27,8% | 2,8% | 30,6% |
| 3 | 12,5% | 45,4% | 34,7% | 7,4% | 42,1% |
| 4 | 6,2% | 42,0% | 38,6% | 13,2% | 51,8% |
| 5 | 3,1% | 37,1% | 40,2% | 19,6% | 59,8% |

**Consequência de design.** Conforme o poder sobe, a falha desaba e o crítico cresce. É a curva de sensação de gênero heroico: o veterano raramente falha e, quando acerta, acerta espetacular. A escalada aparece na **qualidade** do sucesso, não na chance dele.

## Vantagem no d20 (maior de 2d20)

| CD | puro | com vantagem | ganho |
|---|---|---|---|
| 8 | 65,0% | 87,8% | +22,8 pp |
| 10 | 55,0% | 79,8% | +24,8 pp |
| 11 | 50,0% | 75,0% | +25,0 pp |
| 12 | 45,0% | 69,8% | +24,8 pp |
| 16 | 25,0% | 43,8% | +18,8 pp |

O ganho é simétrico em torno de CD 11, onde tem o pico exato de 25 pp. Vantagem vale mais ou menos um +5 — um bônus grande disfarçado de mecânica simples. Bom para arbitragem porque não tem conta; perigoso para balanceamento porque empilha fácil.

## Escada de tamanho de dado

Progressão trocando d6 por d8, d10, d12 em vez de somar bônus. Testada como soma de dois dados subindo em degraus (d6+d6 → d6+d8 → d8+d8 → d8+d10 → d10+d12) contra alvo fixo, a curva é **rasa**: a chance de sucesso quase não se mexe entre os degraus.

**Consequência de design.** Não é defeito, é escolha de onde o poder mora. Em sistemas que usam escada de dado, o crescimento do personagem aparece em dano e efeito, não em acertar mais. Se você adotar escada de dado esperando que o personagem passe a acertar mais, vai se decepcionar — e se adotar sabendo disso, ganha um teto natural e visível de graça, porque não existe "acumular +17".

## Bounded accuracy

A ideia: manter a distância entre bônus de ataque, defesa e dificuldade aproximadamente constante ao longo do jogo, evitando corrida armamentista. O teto de referência do D&D 5e é +5 de atributo e +6 de proficiência, dando +11 no total sem itens.

A vantagem é que ameaça fraca continua relevante e o mestre improvisa cena sem consultar tabela. Uma objeção que circula na comunidade, e que não é consenso, é que bounded accuracy combina mal com a distribuição chata do d20 e funcionaria melhor sobre uma curva.

**Para sistema multi-mestre, o teto não é preferência, é requisito.** Sem teto, um mestre não escreve encontro para "um personagem da faixa 2" sem ver a ficha exata. Com teto, "faixa 2" vira informação suficiente. O teto pode vir do dado ou do orçamento — o orçamento é mais auditável.

## Letalidade

Conta rápida para saber se o combate tem o ritmo desejado:

```
rodadas para cair sob foco = vida ÷ (maior dano concentrado num alvo por rodada)
```

Entre 1,5 e 2 rodadas o combate é rápido e mortal; acima de 3, vira desgaste. Rode essa conta em cada faixa de nível: sistemas costumam ficar mais letais no começo (vida baixa, dano já relevante) e o número precisa ser conferido em toda a escada, não só no topo.
