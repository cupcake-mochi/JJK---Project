# O que dizem e o que se mediu da duração da luta (leva 2, agente B)

*28/09/2026. Cada linha tem a URL e a citação nas notas (`NOTAS-o-que-dizem.md`, nesta pasta), marco por marco. A matemática dos sistemas é do outro agente; aqui entra o que os livros e os designers dizem e o que alguém mediu.*

**Marcas.** `[C]` texto da regra citado · `[F]` fonte oficial secundária (SRD, errata, dados oficiais, fala de designer) · `[I]` inferência, comunidade ou conta minha. `[C via X]` é texto da regra que só li citado por terceiros.

**Arquivos de conta nesta pasta:** `conta-fireball-rodadas.py` → `fireball-combates.csv` → `analisa-fireball.py` (24.748 combates reais de 5e); `conta-critrole-rodadas.py` (328 encontros do Critical Role).

## 1. Sistema por sistema

| sistema | o que diz da duração | duração por dificuldade | efeito do tamanho do grupo | teto do moedor | fonte |
|---|---|---|---|---|---|
| **D&D 5e 2014** | O DMG mede o dano do monstro nas 3 primeiras rodadas ("the first three rounds of combat") `[C via fórum D&D Beyond]`. Não achei frase dizendo que o monstro DURA 3 rodadas; essa leitura é da comunidade `[I]`. Mearls, 2013: no playteste "most battles over in two or three rounds", e o público gostou `[F]`. Mearls, 2025: o jogo supõe ~20 rodadas por descanso longo, com lutas de 3-4 `[F]`. | O livro não liga dificuldade a rodadas. Modelo publicado de Tom Dunn sobre o orçamento de XP: **Fácil 2,1 · Média 3,0 · Difícil 3,7 · Mortal 4,5** `[I]`. | O livro não fala de rodadas por grupo. | O livro não tem. Comunidade: 5 rodadas é "long" e já se aproxima do moedor, e 6 ou mais é moedor (Zupancic) `[I]`. O problema real apontado por Mearls é o inverso: o chefe cai "in a round or even less" `[F]`. 92% dos mestres mexem no PV durante a luta `[I, enquete]`. | Marcos 3, 3b, 3c |
| **D&D 2024** | O SRD 5.2.1 não traz nenhum número de rodadas `[C]`. O DMG 2024 tirou a conta do ND e a criação de monstro do zero `[F]`. Pela medição do Blog of Holding, o PV do MM 2024 ficou como o de 2014 e o dano subiu ~50% `[I]`. | Baixa, moderada e alta, sem rodadas `[C]`. | A regra manda tirar criatura quando falta jogador `[C]`. | Ajuste em jogo: fazer criatura fugir (a luta fica mais fácil) ou chamar reforço `[C]`. | Marco 3c |
| **D&D 4e** | A meta era contada em acertos: "kill a typical monster with four successful attacks" `[C via Blog of Holding, Player's Strategy Guide]`. Relatos: heroico com 4-5 rodadas, paragon com 6-8 `[I]`. | Relatos: luta difícil com 7-8 rodadas; 4-5 níveis acima, ~10, "some taking 20 or more" `[I]`. | Não achei. | O solo tinha PV × 5 do nível 11 em diante, e o DMG2, p. 133 (2009), baixou para × 4 em todo nível `[C via EN World]`. O MM3 (2010) subiu o dano em ~40% `[I]`. Combates de 1-2 h nos níveis baixos e de 3 h ou mais nos altos `[I]`. **A premissa do pedido precisa de ajuste:** a redução de vida veio no DMG2, e o MM3 aumentou o dano. | Marco 4 |
| **Pathfinder 2e** | O GM Core não dá número de rodadas. Diz só "Remember how short the lifespan of a typical combat creature is" `[C]`. | Severa serve para o chefe final e extrema é luta parelha, sem rodadas `[C]`. | Soma inimigos, sem engordar um `[C, leva 1]`. | Não há mecanismo. Comunidade: "3-6" é o típico, com algumas lutas de 7-10 `[I]`. | Marco 6 |
| **Draw Steel** | "fights typically last 3 or fewer rounds" e "A fight that lasts 5 rounds is a *long* fight" `[C]`. | Para o chefe durar, o livro manda montar encontro **difícil** e dar ao líder ou solo ≥ 1/3 do orçamento `[C]`. As 3 ações de vilão, no máximo uma por rodada, supõem um chefe de 3 rodadas ou mais `[C/I]`. Nos encontros com relógio, o típico é 3 rodadas; 5 ou mais sobe **uma categoria de dificuldade**; 2 ou menos também sobe quando o objetivo é impedir a ação `[C]`. | Foi feito e testado para 3 a 6 heróis. Grupo de 3 ou menos sofre contra solo, e com 7 ou mais o solo não aguenta `[C]`. | "tedious slog". O livro traz objetivos, "Cut!", final dramático e fuga sem volta `[C]`. A Malícia cresce com o número da rodada `[C]`. | Marco 1 |
| **13th Age** | Não dá número. O dado de escalada entra na 2ª rodada e vai até +6 `[C]`. Tweet: "the battles never drag on" `[F]`. | Na 2E, o recurso do dia é de "four average fights, or three tough fights": a luta difícil gasta ≈ 1,33 × a média `[F]`. | A 2E pesa mais em grupo grande, sem número aberto `[F]`. | O dado de escalada; o monstro com CA +1; a fuga do grupo, que custa "campaign loss" `[C]`. | Marco 5 |
| **Fabula Ultima** | Regra opcional Blitz: o XP extra é "5 minus the number of rounds elapsed", e a luta que acaba na 6ª rodada não dá nada `[C]`. | O core é fechado. O relógio de vencer o conflito tem 10-12 seções `[C]`. O chefe tem fases, com troca de bloco `[C, bloco oficial]`. | Os turnos se alternam. O Campeão (N) vale N soldados `[C, leva 1]`. | O próprio Blitz, que zera o prêmio na 6ª rodada; a fuga do vilão por 1 Ponto Ultima; o Mestre declara o fim do conflito `[C]`. | Marco 7 |
| **Daggerheart** | Não tem rodada: "no explicit initiative mechanic" `[C]`. | "**-1** for an easier or shorter fight" e "**+2** for a harder or longer fight", no mesmo ajuste `[C]`. O Medo por cena é 2-4 na padrão, 4-8 na maior e 6-12 no clímax `[C]`. | O jogo é para 2-5 jogadores, com orçamento linear `[C]`. | "When a scene drags on, end it." Há contagens regressivas `[C]`. | Marco 2 |
| **Lancer** | As SITREPs têm relógio: Control, Holdout e Recon acabam na 6ª rodada, Escort e Gauntlet na 8ª, Extraction na 10ª. A Basic Combat não tem limite `[F, dados oficiais da Massif]`. | O capítulo do Mestre é fechado. | Comunidade: ≈ 1,5 ativação inimiga por jogador `[I, leva 1]`. | O relógio da SITREP fecha a luta em qualquer PV `[F/I]`. | Marco 8 |
| **ICON** | Nenhuma fonte aberta. | — | — | — | Marco 9 |

## 2. Só o que foi medido

| fonte | o que mede | amostra | resultado |
|---|---|---|---|
| **FIREBALL** (Avrae no Discord, 5e 2014, ago-nov/2022). A contagem é minha | a rodada em que o combate acabou | **15.283 combates** (filtro F3: ≥ 1 PJ, ≥ 1 monstro, ≥ 3 ações, encerrado, ≤ 30 rodadas) | média 4,11 · **mediana 3** · p75 5 · p90 8 · 1 rodada: 12% · 2: 25% · 3: 18% · 4: 13% · 5: 9% · ≥6: 22% |
| FIREBALL, só mesa ao vivo provável (≤ 6 h de relógio) | idem | 12.675 | média 3,76 · mediana 3 · p90 7 · ≥6: 18% |
| FIREBALL, monstro único contra 3+ PJs, no quartil de mais PV por PJ | idem | 225 (de 900) | média 4,38 · mediana 4 · ≥5: 36% · ≥8: 10% |
| **Critical Role** (planilhas do CritRoleStats). A conta é minha | rodadas por encontro | C1: 120 · C2: 138 · C3: 70 | medianas 4 / 3,5 / 3 · médias 4,89 / 4,14 / 3,41 · moda 3 nas três · ≥5 rodadas: 32% / 30% / 19%. As mais longas são de chefe ou de evento (C1: 18-20, fora a perseguição de 67; C2: 13-23; C3: até 10) |
| EN World, el-remmen | rodadas e tempo, na própria mesa | 4 lutas (+1) | 1,5 a 6 rodadas, e uma de 11 |
| Enquete EN World (2020) | "quantas rodadas dura a maioria" | 114 votos | 1-2: 4% · **3-4: 55%** · 5-6: 31% · 6+: 10% |
| Enquete D&D Beyond (2022) | a duração **preferida** de uma luta média a difícil | 41 votos, múltipla escolha | **4-5: 58,5%** · 3-4: 32% · 5-6: 22% |
| Enquetes Sly Flourish | a percepção | 1.165 e 1.321 | 29% acham a luta do 5e lenta; 92% dos mestres mexem no PV durante a luta |

**Tamanho do grupo, medido.** No FIREBALL, com a mesma proporção de monstros por PJ, o grupo maior lutou mais. De 2 PJs para 5-6 PJs, a média subiu de +0,9 a +1,4 rodada: 2,73 → 3,87 com até 0,5 monstro por PJ, 3,26 → 4,52 com 0,5-1, 4,46 → 5,39 com 1-2 e 5,73 → 7,14 com mais de 2. No Critical Role, com 5 a 8 jogadores, não há tendência limpa, porque as células são pequenas. `[I, medido]`

**A cauda cresce com a mediana (FIREBALL).**

| mediana | p75 | p90 |
|---|---|---|
| 3 | 4-5 | 6-7 |
| 4 | 5-6 | 7-9 |
| 5 | 7-8 | 9-13 |

A média fica de 0,3 a 1,2 acima da mediana. `[I, medido]`

**Viés.** O FIREBALL é Discord, com muito jogo por postagem e muito combate de 1 PJ, e não tem ND, nível nem dificuldade. O Critical Role é uma mesa só, de 6 a 8 jogadores, com um mestre que mexe no PV. Os dois são 5e. **Não achei dado medido de nenhum outro sistema.** Ficam fora desta seção o modelo do Tom Dunn, o Zupancic e o Sly Flourish, que são conta ou opinião. O dado do playteste de Mearls não tem amostra publicada.

## 3. O que isso diz da hipótese 2 · 2,5 · 3 · 4 · 5

- **A curva tem precedente quase exato.** O modelo de Tom Dunn sobre o orçamento de 2014 dá 2,1 · 3,0 · 3,7 · 4,5 do Fácil ao Mortal. O Daggerheart põe "mais difícil" e "mais longa" no mesmo ajuste. O Draw Steel usa 5 rodadas ou mais como o marco de "uma categoria mais difícil". Os livros e o modelo concordam que a luta mais difícil dura mais.
- **O Desastre em 3 bate com todas as fontes.** Batem o DMG 2014, o Draw Steel ("3 or fewer"), a mediana 3 do FIREBALL e a moda 3 do Critical Role.
- **O Capanga em 2 é o piso.** Bate com o Fácil 2,1 de Dunn e com o "quick" de Zupancic. O Draw Steel avisa que luta de menos de uma rodada deveria virar teste.
- **A Ameaça em 2,5 não se separa do 3 em nenhum dado.** O intervalo do meio (p25-p75) do FIREBALL vai de 2 a 5. O 2,5 serve como meta de conta, mas a mesa não vai perceber a diferença.
- **A Catástrofe em 4 bate** com o Difícil 3,7 de Dunn e com as enquetes: a mesa relata lutas de 3-4 rodadas e prefere 4-5.
- **A Calamidade em 5 fica na linha da luta longa, uma rodada abaixo do moedor.** Cinco rodadas é a marca da luta *longa* no Draw Steel e no Zupancic. As fontes põem o moedor em 6 ou mais: Zupancic, e o Fabula Ultima, que zera o prêmio na 6ª rodada. Os relatos do 4e põem o moedor em 7-8 ou mais. Seis rodadas já passaria, por duas fontes.
- **O risco da Calamidade está na cauda.** No FIREBALL, quando a luta típica é de 5 rodadas, 1 em 4 vai a 7-8 e 1 em 10 passa de 9. Os sistemas que aceitam luta longa cortam essa cauda com um mecanismo:
  - relógio, como nas SITREPs do Lancer (6-10) e nos objetivos do Draw Steel;
  - escalada por rodada, como o dado de escalada do 13th Age e a Malícia;
  - fase ou fuga do chefe, como no Fabula Ultima e no Sly Flourish;
  - prêmio que zera, como o Blitz.

  **Com 5 como média, a Calamidade pede um desses mecanismos.** Sem ele, a cauda entra no moedor. Lido como média, o 5 põe a luta típica (a mediana) em ~4, que é mais seguro.
- **A luta fica mais pesada por rodada em três sistemas.** O Medo por cena do Daggerheart sobe a cada degrau (2-4, 4-8, 6-12). No 13th Age 2E, a luta difícil gasta 1,33 × a média. No Draw Steel, a Malícia cresce a cada rodada. O contraponto vem do 5e: o chefe cai rápido porque o grupo gasta nele o recurso do dia (Mearls, 2025). A conta de quanto o peso encurta a luta é do outro agente.
- **O ×1 a ×6 pode não ter a mesma duração.** Os livros não dizem nada, porque os orçamentos são lineares. No FIREBALL, com a mesma proporção de inimigos, o grupo de 5-6 lutou ~1 rodada a mais que o de 2. É sinal fraco, com fatores misturados, mas indica que a ficha ×5-×6 tende a passar da rodada-alvo. Vale conferir no playteste.

**Recomendação:** manter 2 · 2,5 · 3 · 4 · 5, com o 5 lido como média. A Calamidade pede um mecanismo que corte a cauda: relógio, escalada, fase ou fuga. O próximo degrau não deve ir a 6.

## 4. Lacunas

- **Nenhum livro fechado deu número de rodadas-alvo na parte que é aberta.** Ficaram de fora o DMG 2014 (só vi o "três rodadas" do dano, citado por terceiros), o DMG 2024, o DMG 4e e o GM Core do PF2e. Não achei designer do D&D 2024 nem da Paizo com número. O vídeo do Seifter não foi assistido, e o dado do playteste de 2018 não é público.
- **13th Age:** os artigos da Pelgrane ("Speeding Combat" e "Secret Origins of the Escalation Die") respondem 403, com checagem de navegador, e não contornei. A tabela de montar luta da 2E está em livro fechado.
- **Fabula Ultima:** o capítulo de montar batalha é do core fechado. O post de Patreon do Galletto deu 403.
- **Lancer:** o capítulo do Mestre é fechado. **ICON:** nada aberto.
- **Daggerheart:** não tem rodada, por desenho, então a duração em rodadas não existe.
- **Dado medido:** só há do 5e. Não há log de PF2e, Draw Steel, Lancer nem Daggerheart. O FIREBALL não tem ND nem nível. Um passo possível é casar o nome do monstro com o ND do SRD, para ter a dificuldade real, mas muitos nomes são apelidos ("SH1").
- **4e:** o número exato do aumento de dano do MM3 veio da comunidade; não li texto oficial com ele.
