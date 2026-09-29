# NOTAS — leva 2, agente A: quantas rodadas dura a luta, pela matemática de cada sistema

*28/09/2026. Notas ao longo do caminho. O resultado final vai em `RESULTADO-matematica.md`; o script em `conta-rodadas.py`.*

**Marcas.** `[C]` texto da regra citado · `[F]` fonte oficial secundária (SRD, errata, prévia) · `[I]` inferência, conta própria ou comunidade.

**Definições da conta (do pedido):**
- rodadas = vida do chefe ÷ (N × dano esperado de um personagem por rodada, já com a chance de acerto contra a defesa do chefe);
- pressão = dano esperado do chefe por rodada (com a chance de acerto dele) × rodadas ÷ (N × vida de um personagem);
- encontro padrão: mesma conta com vários inimigos do nível do grupo, quando o sistema dá um jeito limpo.

**Leva 1 já lida** (não refeita): orçamentos de XP do PF2e e do D&D 2024, espaços do Draw Steel, equivalências do 13th Age e as URLs estão em `../bestiario-leva-1/NOTAS-pesquisa-externa.md`.

## Marco 1 — Pathfinder 2e (Remaster), tabelas lidas no Archives of Nethys

Todas as tabelas abaixo foram lidas por `curl` no AoN em 28/09/2026 (fonte oficial aberta, licença da Paizo). Transcritas no `conta-rodadas.py`.

### Criatura (GM Core, cap. 2, "Building Creatures")
- `[C]` **Table 2–7: Hit Points** (GM Core p. 118), https://2e.aonprd.com/Rules.aspx?ID=2891 — colunas High / Moderate / Low, níveis −1 a 24. Uso o **meio da faixa Moderate** (ex.: nível 12 = 219–211 → 215).
  - Por que Moderate: "Give a creature HP in the moderate range unless its theme strongly suggests" outra.
- `[C]` **Table 2–5: Armor Class** (GM Core p. 117), https://2e.aonprd.com/Rules.aspx?ID=2888 — Extreme / High / Moderate / Low. Uso **High**.
  - Por que High: "Most creatures use high or moderate AC—high is comparable to what a PC fighter would have." Escolhi o chefe de luta corpo a corpo, o perfil "fighter" do texto.
- `[C]` **Table 2–9: Strike Attack Bonus** (GM Core p. 120), https://2e.aonprd.com/Rules.aspx?ID=2896 — uso **High**: "Use a high attack bonus for physically combative creatures—fighter types".
- `[C]` **Table 2–10: Strike Damage** (GM Core p. 120), https://2e.aonprd.com/Rules.aspx?ID=2897 — média entre parênteses; uso **High**: "A creature that's meant to be primarily a melee threat uses high damage". A tabela é "the damage a creature should deal with a single Strike".
- Valores usados (nível: PV moderado meio / CA high / ataque high / dano high por Strike), na íntegra no script.

### Orçamento (já na leva 1)
- `[C]` GM Core p. 75-76, https://2e.aonprd.com/Rules.aspx?ID=2716 e ID=2717/2719: trivial 40 (ajuste 10/PJ), baixa 60 (20), moderada 80 (20), severa 120 (30), extrema 160 (40); XP por criatura −4 = 10, −3 = 15, −2 = 20, −1 = 30, 0 = 40, +1 = 60, +2 = 80, +3 = 120, +4 = 160.
- Chefe sozinho: o maior nível que cabe no orçamento (convenção da leva 1). **"O sistema não faz"** quando o orçamento passa de 160 (a tabela acaba no +4) ou quando nada cabe (baixa com N = 1: orçamento 0).

### Personagem de referência: Guerreiro (Fighter, Player Core), conta própria `[I]` sobre regras `[C]`
- `[C]` Fighter, https://2e.aonprd.com/Classes.aspx?ID=35 — PV 10 + Con por nível; perito (expert) em armas marciais no 1; mestre no grupo escolhido no 5 (Weapon Mastery); lendário no 13 (Weapon Legend); Weapon Specialization no 7 (+3 se mestre, +4 se lendário); Greater Weapon Specialization no 15 (+6 mestre, +8 lendário); treinado em todas as armaduras, perito no 11, mestre no 17.
- `[C]` Automatic Bonus Progression (GM Core p. 83, Table 4-11), https://2e.aonprd.com/Rules.aspx?ID=2741 — ataque +1 no 2, +2 no 10, +3 no 16; dados de dano 2 no 4, 3 no 12, 4 no 19; CA +1 no 5, +2 no 11, +3 no 18; apex no 17. **Uso a ABP só como o calendário publicado de runas**, para não escolher calendário de item.
- `[C]` Atributo: "If an attribute modifier is already +4 or higher, it takes two boosts to increase it" (Player Core, https://2e.aonprd.com/Rules.aspx?ID=2110).
- **Suposições (sete, e nenhuma otimização de talento):**
  1. Guerreiro humano (PV de ancestralidade 8) com **espada grande (greatsword) d12** = 6,5 por dado;
  2. Força +4 no 1, +5 no 10, +6 no 17 (apex), +7 no 20; Con +2 no 1, +3 no 5, +4 no 10, +5 no 20;
  3. **2 Strikes por rodada**, o segundo com −5 de penalidade de ataque múltiplo; sem talento, sem Power Attack, sem flanco, sem condição;
  4. runas pelo calendário da ABP;
  5. armadura completa (full plate, +6 item, Des 0);
  6. crítico pela regra do PF2e (passar a CD por 10, 20 natural sobe um grau, 1 natural desce), dano dobrado;
  7. o chefe também faz **2 Strikes por rodada** (o segundo a −5), pela mesma convenção.
- Fórmulas: ataque = nível + proficiência (perito +4, mestre +6, lendário +8) + For + potência; dano por acerto = dados × 6,5 + For + especialização; CA = 10 + nível + proficiência de armadura (treinado +2, perito +4, mestre +6) + 6 + potência; PV = 8 + (10 + Con) × nível.
- Níveis de referência: **3, 10, 20** (no 3 a criatura −4 é nível −1, o piso da tabela; no 20 a +4 é nível 24, o teto).

### Encontro padrão (vários inimigos do nível do grupo) `[I]`
- Número de criaturas = orçamento ÷ 40 (criatura de nível 0 = 40 XP), fracionário.
- O grupo derruba uma de cada vez (foco); enquanto isso as vivas atacam. Dano inimigo total = dano de uma × (tempo para derrubar uma) × k(k+1)/2. É uma convenção, não regra.

### PF2e — primeiro resultado (script rodado, 28/09)
- Chefe sozinho, N = 4: trivial 0,8-1,6 rod · baixa 1,3-2,0 · moderada 1,9-2,8 · severa 3,0-3,3 · extrema 4,2-4,7 (níveis 3/10/20).
- Com N crescendo, o chefe sobe de nível mas as rodadas caem ou ficam: extrema N=1 3,1-6,5 → N=4 4,2-4,7; N=5 e N=6 "não faz" (orçamento > 160).
- O dano do chefe por rodada, em vidas de um personagem (vida/rod), cai com o nível: extrema N=4 = 0,95 no 3, 0,60 no 10, 0,41 no 20. A hipótese de 0,9 só aparece no começo.

## Marco 2 — D&D 2024 (SRD 5.2.1)

### Fonte dos blocos
- `[F]` Blocos do SRD 5.2 lidos pela API aberta do Open5e (transcrição de comunidade do SRD oficial, CC-BY): https://api.open5e.com/v2/creatures/?document__key=srd-2024 — 331 blocos.
- `[F]` Conferidos contra o PDF oficial do SRD 5.2.1 (https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf, p. 318): Adult Red Dragon AC 19, HP 256, Rend +14, 13 (1d10 + 8) + 5 (2d4), Legendary Action Uses 3, Pounce sem trava de uma vez por rodada — bate com o Open5e.
- `[C]` XP Budget per Character (SRD 5.2.1 p. 202), conferido no PDF: nível 3 = 150/225/400; nível 10 = 1.600/2.300/3.100; nível 17 = 4.500/7.200/11.700 (baixa/moderada/alta). Resto da tabela no script da leva 1.
- `[C]` "Running a Monster" (p. 255): o monstro usa ações lendárias "as often as it can".

### Como tirei vida, CA e dano por ND `[I]`
- Em vez de 3 a 5 blocos escolhidos à mão, **média de todos os blocos do SRD 5.2 naquele ND** (menos 3 sem ataque: Giant Fly, Seahorse, Shrieker Fungus). Escolher 3-5 "solos" à mão só é possível do ND 13 para cima, onde há lendários; abaixo disso não há solo no SRD.
- Onde o ND tem menos de 3 blocos (12, 19, 22, 24) ou nenhum (18), junto com os ND vizinhos, pesado pelo número de blocos `[I]`.
- **Dano por rodada** = os ataques do Multiattack (ou o melhor ataque, se não houver Multiattack) + as ações lendárias que fazem um ataque ("makes one X attack"), 3 usos por rodada quando a ação não tem trava de uma vez por rodada. **Não entra:** sopro e outras recargas, magia, efeito de área, teste de resistência. É a rotina de ataque, alvo único. *Isso subestima dragão e conjurador.*
- Acerto do monstro contra a CA do personagem: 20 natural sempre acerta e crita (dados dobrados), 1 natural erra.
- Tabela por ND (n, PV, CA, ataque médio, dano bruto/rodada se tudo acertar, extra de crítico), transcrita no script. Exemplos (ND 10+): Aboleth 150 PV/CA 17/60 por rodada; Young Red Dragon 178/18/48; Adult Red Dragon 256/19/108 (3 Rend + 3 Pounce); Balor 287/19/78; Ancient Red Dragon 507/22/174; Kraken 481/18/48 (só tentáculos).

### Personagem de referência: Guerreiro Campeão do SRD 5.2.1 `[I]` sobre regras `[C]`
- `[C]` Fighter (SRD 5.2.1, via Open5e /v2/classes/?document__key=srd-2024): PV 10 + Con no 1, 6 + Con depois; Extra Attack no 5, Two Extra Attacks no 11, Three no 20; Studied Attacks no 13 ("If you make an attack roll against a creature and miss, you have Advantage on your next attack roll against that creature"); Fighting Style no 1, "Defense is recommended".
- `[C]` Champion (única subclasse do SRD): Improved Critical no 3 (19-20), Superior Critical no 15 (18-20), Heroic Warrior no 10 (Heroic Inspiration no começo do turno, se não tiver).
- `[C]` Greatsword 2d6, Heavy, Two-Handed, mastery Graze: errou, causa o modificador do atributo.
- **Regra de escolha:** o que a classe dá sozinha entra; escolha que o texto recomenda (Defense) entra; escolha sem recomendação não entra (segundo estilo do nível 7, talentos). Action Surge e Second Wind não entram (recurso por descanso).
- **Suposições:** For +3 (1-3), +4 (4-5), +5 (6+); Con +2 fixo (o resto dos ASI vai para talento sem número); cota de malha 16 no 3 e armadura de placas 18 no 10 e no 17, +1 do Defense; sem item mágico (o DMG 2024 não pressupõe); Heroic Inspiration gasta para rolar de novo o primeiro ataque errado do turno.
- Níveis de referência: **3, 10, 17**. No 20 o orçamento alto com N ≥ 4 pede ND 25+, e o SRD não tem monstro entre o ND 24 e o 30 — lacuna do SRD, não do sistema.

### Chefe e encontro padrão
- Chefe sozinho: o maior ND cujo XP cabe em orçamento × N (a conta da leva 1).
- Encontro padrão `[I]`: orçamento ÷ XP de um monstro de ND = nível do grupo, fracionário, com foco. O próprio SRD diz que um monstro de ND = nível é "low-difficulty challenge for a party of four".

### D&D 2024 — primeiro resultado (script rodado, 28/09)
- Guerreiro: nível 3 = +5, 1 ataque, CA 17, 28 PV, 7,6 de dano por rodada contra ND 3; nível 10 = +9, 2 ataques, CA 19, 84 PV, 22,9 contra ND 10; nível 17 = +11, 3 ataques, CA 19, 140 PV, 36,9 contra ND 17.
- Chefe sozinho, N = 4: baixa 1,6-2,0 rod · moderada 2,1-2,3 · alta 2,3-2,9 (níveis 3/10/17).
- Com N crescendo as rodadas CAEM: alta N=1 3,6-5,7 → N=6 2,0-2,7. O ND sobe mais devagar que o dano somado do grupo.
- vida/rod do chefe alto, N=4: 0,48 (3), 0,80 (10), 0,89 (17). Aqui o 0,9 da hipótese aparece no meio e no fim da progressão.
- Encontro padrão (monstros de ND = nível): baixa ~1,8-2,1 rod, moderada ~2,7-3,1, alta ~4,2-4,9 — mais longo que o chefe sozinho na mesma dificuldade, porque o ND = nível tem CA mais baixa, mas mais PV somados por XP.

## Marco 3 — Draw Steel (MCDM), via Steel Compendium

Fonte: Steel Compendium, "independent product published under the DRAW STEEL Creator License" (texto do README), transcrição dos livros oficiais. Marco como `[C]` o texto de regra lido lá, com essa ressalva.
- Monster Basics: https://raw.githubusercontent.com/SteelCompendium/data-bestiary-md/main/Monsters/Chapters/Monster%20Basics.md
- Heróis: https://github.com/SteelCompendium/data-rules-md (Classes By Level/Fury, Abilities/Fury, Chapters/Kits.md, Chapters/Classes.md)
- Blocos: https://github.com/SteelCompendium/data-bestiary-json

### Monstro (fórmulas de criação, Monster Basics l. 1297-1382) `[C]`
- Vigor (Stamina) = (10 × nível + modificador de papel) × organização; Solo: papel +30, organização ×5 → **Solo = (10L + 30) × 5**.
- EV = (2 × nível + 4) × organização; Solo ×6.
- Dano = (4 + nível + mod. de dano) × modificador do tier (0,6 / 1,1 / 1,4), arredondado para cima; se for golpe, soma a maior característica. Solo: mod. de dano +2.
- Maior característica = 1 + escalão, +1 para solo (máx. +5). Escalão: 1-3 = 1º, 4-6 = 2º, 7-9 = 3º, 10 = 4º.
- "Elite, leader, and solo monsters have abilities that typically target two creatures".
- Instant Solo: "The creature can take two turns each round."
- **Conferido `[C]` contra os 22 solos do bestiário JSON:** o Vigor de todos bate com a fórmula (ex.: nível 1 = 200, 5 = 400, 10 = 650, 11 = 700; a Medusa tem 420 e o Kingfissure Worm, 420 contra 500). O dano da assinatura de alvo único ou duplo fica perto (nível 3 Chimera 9/13/16 = fórmula 9/13/16; nível 10 Lich 15/21/25 contra 15/23/28 — o livro avisa que a fórmula dá "a few points higher").
- Todos os 22 solos têm 2 turnos por rodada; o Ajax (nível 11) tem 3.

### Onde o solo cabe: "hero slots" (Monster Basics l. 662-681) `[C]`
- "One solo creature fills six hero slots plus one slot for each level the creature is higher than the heroes."
- Trivial: N − 2 espaços; fácil: N − 1; padrão: N (+1 se ninguém acima do nível); difícil: N + 2 (+1 se nem todos acima), solo até +1 nível; extremo: N + 4 "or more".
- Solo máximo +1 nível acima: "restrict them to no more than 1 level above the heroes' average level".
- **Resultado `[I]`:** trivial e fácil: nenhum N de 1 a 6 cabe. Padrão: N = 5 (solo de nível L, 6 = N + 1) e N = 6 (L). Difícil: N = 3 (L, 6 = N + 3), N = 4 (L, 6 = N + 2), N = 5 (L + 1, 7 = N + 2); N = 6 "não faz" (pediria L + 2). Extremo: N = 1 (L), N = 2 (L), N = 3 (L + 1); N ≥ 4 "não faz" (o solo +1 só enche 7 espaços, e o extremo pede N + 4 = 8 ou mais).
- Pela regra do EV (orçamento por ES, l. 590-600) a conta dá quase igual; muda uma célula no nível 1 (N = 6, difícil, solo +1 = 8 heróis de ES). Uso os espaços, que não dependem do nível.

### Herói de referência: Fúria (Fury) `[I]` sobre regras `[C]`
- `[C]` Fury Basics: Vigor 21 no 1, +9 por nível; Might 2 no 1, 3 no 4, 4 no 7, 5 no 10 (Characteristic Increase).
- `[C]` Ferocidade: "At the start of each of your turns during combat, you gain 1d3 ferocity"; 1d3 + 1 a partir do 7 (Greater Ferocity). Primordial Strike (nível 4): "spend 1 ferocity to gain 1 surge". Surge: "Each surge you spend deals extra damage equal to your highest characteristic score", até 3 por golpe.
- `[C]` Brutal Slam (assinatura): 3 + M / 6 + M / 9 + M. To the Uttermost End (5 de ferocidade): 7 + M / 11 + M / 16 + M.
- `[C]` Kit: bônus corpo a corpo fixo +X/+Y/+Z e Vigor por escalão. Uso +2/+2/+2 e +6 por escalão (Dual Wielder, Guisarmier e outros) `[I]`.
- `[C]` Rolagem: 2d10 + característica; ≤11 tier 1, 12-16 tier 2, 17+ tier 3; 19-20 natural sempre tier 3 e, em ação principal, crítico = ação principal extra. Não há defesa: o golpe sempre resolve num tier.
- **Suposições:** (1) Fúria com kit +2/+2/+2; (2) toda rodada usa a assinatura; (3) só a ferocidade garantida do começo do turno (média 2, ou 3 do nível 7), sem a do dano recebido; (4) no nível 1 a ferocidade vai para To the Uttermost End (uma a cada 2,5 turnos); do 4 em diante, toda ferocidade vira surge (+M por ponto, até 3); (5) o crítico dá 3% de ação extra, contado.
- Dano por turno: nível 1 ≈ assinatura + (2/5) × (diferença para a heroica); nível 5 = assinatura + 2 × 3; nível 10 = assinatura + 3 × 5.
- Vigor do herói: 21 + 9 × (L − 1) + 6 × escalão.

### Chefe: dano por rodada `[I]`
- 2 turnos × 1 ação principal × assinatura pela fórmula, em min(2, N) alvos. **Não entra:** ação de vilão (3 por luta, 1 por rodada), Malícia (N + nº da rodada por rodada; 5 compra uma ação principal extra), golpe livre. É um piso.

### Encontro padrão `[I]` sobre `[C]`
- Criaturas de pelotão (platoon, 1 espaço cada) do nível do grupo: trivial N − 2, fácil N − 1, padrão N + 1, difícil N + 3, extremo N + 4. Papel médio (+20 de Vigor, +0 de dano), 1 alvo, 1 turno.
- Níveis de referência: **1, 5, 10** (o jogo vai do 1 ao 10).

### Draw Steel — primeiro resultado (script rodado, 28/09)
- Fúria: nível 1 = 11,9 de dano por turno, Vigor 27; nível 5 = 17,5, Vigor 69; nível 10 = 29,8, Vigor 126.
- Solo sozinho: padrão N=5 3,4-4,6 rod, N=6 2,8-3,8; difícil N=3 5,6-7,6, N=4 4,2-5,7, N=5 (solo +1) 4,2-5,1; extremo N=1 16,8-22,8, N=2 8,4-11,4, N=3 7,0-8,6. Trivial e fácil: nenhum solo cabe de 1 a 6 heróis.
- vida/rod do solo (2 turnos, 2 alvos, só a assinatura): 1,59 no 1, 0,98 no 5, 0,76 no 10. A pressão passa de 1 em várias células. O herói do Draw Steel tem Recoveries (10 na Fúria), e pressão acima de 1 sobre o Vigor pede cura e não quer dizer morte.
- As rodadas caem com o N dentro de cada dificuldade (difícil: 5,6 → 4,2 → 4,2 no nível 1), porque o solo é o mesmo bloco e o dano do grupo cresce com o N.
- **O herói de referência só bate em um alvo.** No encontro de vários monstros o Draw Steel dá muita área ao herói, e a conta alonga essas lutas.

## Marco 4 — 13th Age (1ª edição, Archmage Engine SRD, OGL)

### Monstro `[F]` (SRD oficial aberto, site 13thagesrd.com, seções do Archmage Engine)
- Monster Creation, https://www.13thagesrd.com/monsters/monster-creation/ — "Baseline Stats for Normal Monsters", "Large or Double-Strength", "Huge or Triple-Strength", níveis 0-14: ataque, dano de golpe (Strike Damage), PV, CA. Transcritas no script. Ex.: nível 5 normal +10 / 18 / 72 PV / CA 21; enorme 54 / 216; nível 10 normal +15 / 58 / 216 / CA 26; enorme 174 / 648.
- O grande e o enorme repartem o dano em mais ataques ("Split damage up into smaller attacks"): uso o total da coluna por rodada, com um teste de acerto por ataque `[I]`.

### Batalha `[C]` (Running the Game, https://www.13thagesrd.com/running-the-game/)
- "For adventure tier, levels 1-4, start with one enemy creature of the party's level per PC"; champion (5-7) um nível acima; epic (8-10) dois acima.
- Monster Equivalents (adventurer; champion e epic deslocam 1 e 2 níveis): mesmo nível normal 1 / grande 2 / enorme 3; +1 = 1,5 / 3 / 4; +2 = 2 / 4 / 6; +3 = 3 / 6 / 8.
- **O SRD da 1ª edição tem uma dificuldade só** (a batalha justa, N equivalentes) e uma lista qualitativa de "Unfair Encounters". Não há trivial, difícil ou extremo em número. As outras linhas são "o sistema não faz".
- Chefe sozinho `[I]`: um monstro que valha N equivalentes, preferindo o menor desvio de nível: N=1 normal, N=2 grande, N=3 enorme, N=4 enorme +1, N=5 enorme +1 (vale 4: nada vale 5 exato), N=6 enorme +2 — tudo deslocado pelo escalão (+1 no champion, +2 no epic).
- Encontro padrão `[I]`: N monstros normais do nível que vale 1 no escalão.

### Personagem de referência: Guerreiro (Fighter, SRD) `[I]` sobre `[C]`
- `[C]` Fighter, https://www.13thagesrd.com/classes/fighter/ — PV (8 + Con) × 3/4/5/6/8/10/12/16/20/24 nos níveis 1-10; CA com armadura pesada 15 + modificador do meio de Con/Des/Sab + nível; ataque básico corpo a corpo "Strength + Level vs. AC", acerto "WEAPON + Strength damage", "Miss: Damage equal to your level"; espada grande/machado grande 1d10; bônus de dano do atributo ×1 (1-4), ×2 (5-7), ×3 (8-10); +1 em 3 atributos no 4, 7 e 10.
- `[C]` WEAPON = um dado da arma por nível do personagem (regra de dano do 13th Age).
- `[C]` Dado de escalada: só os PJs, +1 no ataque a partir da 2ª rodada, até +6 (já lido na leva 1).
- **Suposições:** Força +4 (1-6), +5 (7-10); Con +2; modificador do meio +1; um ataque básico por turno; sem manobra, talento, item mágico nem recuperação; 20 natural = crítico, dano dobrado.
- Níveis de referência: **1, 5, 10**.

### 13th Age — primeiro resultado (script rodado, 28/09)
- Guerreiro: nível 1 = +5, 9,5 no acerto, 1 no erro, CA 17, 30 PV; nível 5 = +9, 35,5, 5, CA 21, 80 PV; nível 10 = +15, 70, 10, CA 26, 240 PV.
- Chefe que vale N: 4,5 rod (nível 1), 4,2 (5), 7,6 (10) com N = 1; com N = 6, 4,3 / 4,0 / 7,1. **É o único sistema em que as rodadas ficam quase paradas com o N** (razão N=6/N=1 de 0,93 a 0,97), porque "vale N" é vida × N e dano × N, como na grade do Mizuki.
- A pressão também fica parada (nível 1: 0,41 · 0,41 · 0,41 · 0,50 · 0,33 · 0,47); o que cresce com o N é o vida/rod (0,09 → 0,65), porque o chefe bate por N.
- O nível 10 sai longo (7,6 rodadas) porque o guerreiro não tem item mágico nem manobra; a tabela de monstro do escalão épico cresce 1,25× por nível. Anotado como convenção, não como achado.

## Marco 5 — Fabula Ultima, Daggerheart, Lancer
- **Fabula Ultima:** o livro base é fechado (leva 1); o Campeão (N) é vida × N e turnos × N, e sem a tabela de dano/defesa por nível aberta não dá para fazer a conta. Pulado.
- **Daggerheart:** o SRD é aberto, mas não tem rodada (sem iniciativa, holofote por Medo) e a vida é em marcas por limiar de dano; "rodadas até derrubar" não tem definição limpa. Pulado.
- **Lancer:** capítulo de NPC fechado (leva 1). Pulado.

## Marco 6 — síntese (script com resumo, 28/09)
- Alinhamento `[I]`: PF2e trivial/baixa/moderada/severa/extrema e Draw Steel trivial/fácil/padrão/difícil/extremo = os cinco degraus, na ordem; D&D baixa/moderada/alta = Ameaça/Desastre/Catástrofe (a alta do DMG 2024 tem o mesmo risco que a severa do PF2e); 13th Age justa = Desastre.
- Mediana das rodadas do chefe sozinho com N = 4, juntando os sistemas: Capanga 1,5 · Ameaça 1,8 · Desastre 2,7 · Catástrofe 3,3 · Calamidade 4,7 (hipótese 2 · 2,5 · 3 · 4 · 5).
- Pressão em N = 4: a conta de hoje do Mizuki (0,9 de vida por rodada por 3 rodadas, 4 pessoas) dá 0,675; PF2e e D&D põem isso entre a severa/alta (0,28-0,65) e a extrema (0,49-1,01), não na moderada (0,20-0,48).

## Marco 7 — entrega (28/09)
- `RESULTADO-matematica.md` escrito a partir da saída do `conta-rodadas.py` (tabelas por sistema geradas pelas funções do script; as duas tabelas do resumo conferidas por diff contra a saída, valor a valor).
- `python3 conta-rodadas.py` roda e sai com código 0.
