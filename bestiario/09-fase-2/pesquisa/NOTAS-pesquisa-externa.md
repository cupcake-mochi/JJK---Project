# NOTAS — pesquisa externa: inimigo × tamanho do grupo (leva 1)

*27/09/2026. Notas intermediárias. O resultado final vai em RESULTADO-pesquisa-externa.md.*

## Marco 0 — o que o projeto já tem (lido)

- `bestiario/01-pesquisa/dmg2024-e-draw-steel.md`: DMG 2024 — orçamento de XP POR PERSONAGEM (baixa/moderada/alta), sem multiplicador de encontro; "um único monstro é em geral desafio BAIXO para 4 PJs de nível = ND". Draw Steel — fórmulas EV/Stamina/dano; organização Minion ×0,125/×0,5, Horde, Platoon, Elite ×2, Leader ×2, Solo ×5 Stamina/×6 EV; Solo vale 6 heróis; villain actions 3/encontro; Malice = nº heróis + nº rodada; ES de um herói = 4 + 2×nível; Solo no máximo +1 nível acima.
  - Achado do projeto: dano POR GOLPE quase não muda entre postos (Solo ÷ Platoon 1,12–1,33); a força vem de vida, alvos e villain actions.
- `dnd-como-monta-inimigo.md`: DMG 2014 tabela por ND; calibra 3 rodadas; dano por rodada dividido livre.
- `o-capanga-contra-os-outros-sistemas.md`: capanga cai num golpe (4e, Lancer Grunt, DS minion, 13th Age mook); esquadrão de 8 bateu com DS.
- `LEVANTAMENTO-pe.md`: Lancer — NPC 1 Structure/1 Stress; Elite ×2 Structure/Stress, ×2 ativações; Ultra +3 Structure, +1-2 ativações; recomendação ativações inimigas ~1,5× nº de jogadores (fonte comunidade: owacsender substack). Fabula Ultima — Ultima Points de vilão 5/10/15 (Menor/Maior/Supremo) — fonte TV Tropes e blog; NÃO trata de Campeão. Draw Steel Solo = 2 turnos/rodada; ação principal extra = 5 Malice. 13th Age escalation die só PJ; mook = 1/5 de monstro normal.
- `LINKS-fontes-vivas.md`: steelcompendium /v2/ funciona; 2e.aonprd.com PF2e integral; daggerheart.org 403 (usar daggerheart.com SRD PDF); 5thsrd 403; dndbeyond br-2024 how-to-use-a-monster funciona.

## Sistema hoje (peça 26 §4, lida)
- Capanga (8 corpos pool, ×0,25 dano), Ameaça 1 (×0,25), Desastre 4 (×1,00, 3 ações), Catástrofe 6 (×1,50, 5 ações), Calamidade 8 (×2,00, 6 ações). personagens = fator × 4. A linha do manual é calibrada para 4.
- §4.2: ações declaradas, não por fórmula; antes era pessoas − 1 (piso 1), e isso quebrou a Dupla (2 ÷ 1).
- §4.3: 4 Ameaças cobram 0,75–0,77× um Desastre (não é intercambiável).
- §4.6: Desastre derruba 2,70 pessoas em 3 rodadas se concentrar; d20 2014 2,56–2,70, PF2e solo ~2,8.

## Pendências de pesquisa
(atualizado abaixo por sistema)

## Marco 1 — Fabula Ultima (FU)

Fontes abertas usadas (o core rulebook está fechado; no Demiplane Nexus as páginas "Core Rulebook" pedem login — NÃO contornei; AnyFlip/Scribd/pdfcoffee são cópias piratas — NÃO usei):
- [C] Press Start (grátis, Demiplane Nexus, página "Conflict"): https://app.demiplane.com/nexus/fabulaultima/rules/conflict
  - "the Player Characters' side and the enemy side alternate taking turns"; "Each turn allows for a single action."; "If one side outnumbers the other, keep alternating turns as long as possible, then let the side with the numerical advantage take the remaining turns towards the end of the round."
  - Iniciativa em grupo: DL = maior Initiative entre os adversários (página Initiative, Press Start).
- [C] Load Game (grátis, Demiplane "Villains"): https://app.demiplane.com/nexus/fabulaultima/rules/villains
  - Ultima Points por importância NARRATIVA: Minor 5 / Major 10 / Supreme 15. Usos: Escape (1), Invoke Trait reroll (1), Recovery (ação + 1 UP: tira status e recupera 50 MP). Não recarrega. Escalation (minor→major→supreme), 2 a 4 por campanha. Villain é eixo SEPARADO do rank ("Rank may vary" no bloco oficial).
  - Nada no texto dos UP depende do nº de PJs (o nº de PJs só entra no Fabula Point que CADA PJ ganha quando o vilão aparece).
- [F] Bônus oficial grátis da Need Games (Necromancer, 2022): https://www.needgames.it/wp-content/uploads/2022/11/Fabula-Ultima-Bonus-01-Necromancer.pdf
  - "LADY CARMILLA (Champion 3) Lv 30", HP 300, MP 160, Init 12; "BLOODCURDLING CARMILLA (Champion 4) Lv 30", HP 440, MP 120, Init 13; "Major Villain (10 Ultima Points); Rank may vary."
  - Rotina: "performs Shadow Barrage on her first and third turn, Spellbreak Claw on her second turn, and Bloodchill Wave on her fourth turn" → Champion 4 = 4 turnos por rodada [C do bloco].
  - Bloodchill Wave "can only be cast once per turn, and only during ... last turn of each round" — o chefe de vários turnos trava a habilidade grande num turno só.
  - Duas fases: ao chegar a 0 PV vira a forma Champion 4 (troca de bloco, não barra de vida única).
  - Conta de conferência [I, minha]: HP NPC = 2×nível + 5×Might (fórmula do Fultimator). Carmilla: 2×30 + 5×8 = 100; ×3 = 300 ✓. MP = nível + 5×WLP = 30 + 50 = 80; ×2 = 160 ✓.
- [I] Fultimator (ferramenta de comunidade, código aberto que implementa as regras do core): https://github.com/fultimator/fultimator/blob/main/src/libs/npcs.js
  - Ranks: Soldier, Elite, Champion(1) a Champion(6), Companion, Group Vehicle.
  - Elite: HP ×2, Init +2, +1 skill. Champion(N): HP ×N, MP ×2, Init +N, +N skills. N vai de 1 a 6 (teto 6 no seletor).
- [I] Resumo de buscador (fonte primária é o core, fechado): "Champion enemies can replace any number of normal enemies; they perform a number of turns per round equal to the number of normal enemies they replace, and their Hit Points are multiplied by that same number"; "Elite ... two turns per round, double Hit Points"(?); boss: "soldiers equal to the number of Player Characters plus one, or any equivalent combination of soldiers, champions, and elites"; exemplo de ordem de turno "3 PCs fight a Champion 4 ... PC, Champion 1, PC, Champion 2, PC, Champion 3, Champion 4" (bate com a regra [C] do Press Start sobre sobra de turnos).
  - ⚠ Elite "dois turnos": NÃO confirmado em fonte aberta. O Fultimator não codifica turnos. Declarar como lacuna/confirmação pendente.
- CONCLUSÃO FU: o "Campeão de rank N" que o Mizuki lembra EXISTE — Champion(1..6). Vale N soldados; multiplica PV por N e turnos por N (turnos: confirmado no bloco oficial Champion 4; regra geral só por fonte secundária). MP ×2 (não ×N), Init +N, skills +N. Dano por golpe NÃO multiplica (o ataque do bloco é o normal do nível). Defesas não multiplicam.
- [I] Fultimator, simulador de combate (src/routes/combat/combatSimulator.jsx, getTurnCount): soldier/champion1 = 1 turno; elite = 2; championN = N. Ultima: minor 5, major 10, supreme 15. → corrobora "Elite 2 turnos" e "Champion(N) N turnos" (comunidade, não o livro).
- Nota [I minha]: Bloodcurdling Carmilla MP 120 não fecha com MP ×2 (30 + 5×8 = 70, ×2 = 140). HP 440 = 4 × 110 (100 + 10 de skill de PV extra, provável). Não afeta a pergunta.

## Marco 2 — D&D 2024

Fonte aberta principal: SRD 5.2.1 (CC-BY-4.0, oficial): https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf — tem o "Combat Encounters" do DMG 2024 (Gameplay Toolbox), p. 202-203. Li por pdftotext em fluxo; não guardei o PDF.
- [C] p. 202, Low Difficulty: "As a rough guideline, a single monster generally presents a low-difficulty challenge for a party of four characters whose level equals the monster's Challenge Rating."
- [C] p. 202, Step 2: "Multiply the number in the table by the number of characters in the party to get your XP budget for the encounter." → o eixo do nº de jogadores é LINEAR (orçamento por personagem × N). Sem multiplicador de encontro, sem faixa declarada de tamanho de grupo. Exemplos do próprio SRD usam 4, 5 e 6 personagens (Ex. 3: seis de nível 15, 7.800 × 6 = 46.800).
- [C] p. 203, Adjustments: "A player's absence might warrant removing creatures from an encounter to keep it at the intended difficulty."
- [C] p. 203, Many Creatures: "If your encounter includes more than two creatures per character, include fragile creatures that can be defeated quickly." Troubleshooting: "Referencing more than two or three stat blocks for a single encounter can be daunting".
- [C] Glossário, "Challenge Rating" (p. 178-179): "summarizes the threat a monster poses to a group of four player characters." / "But circumstances and the number of player characters can significantly alter how threatening a monster is in actual play."
- [C] Legendary Actions (Monsters, p. ~257): "an action that a monster can take immediately after another creature's turn. Only one of these actions can be taken at a time"; "Legendary Action Uses: 3 (4 in Lair)... regains all expended uses at the start of each of its turns." Contagem no SRD 5.2.1: 27 blocos "3 (4 in Lair)", 3 blocos "3". Nenhum escala com nº de PJs. Legendary Resistance: 3/Day (2), 3/Day ou 4 em covil (15), 4/Day (2), 4/Day ou 5 em covil (12), 6/Day (1).
- [C] "Running a Monster" (p. 255): "make sure it uses them [Bonus Actions, Reactions, Legendary Actions] as often as it can."
- [F] D&D Beyond (post oficial): https://www.dndbeyond.com/posts/1901-creating-combat-encounters-using-the-new-dungeon — exemplo com 5 PJs nível 5: 750 × 5 = 3.750.
- [C] Roll20 prévia pública do DMG 2024 "Plan Encounters" confirma as mesmas frases.
- Eixo de força: ND (CR) do monstro + 3 dificuldades (baixa/moderada/alta). Não há rank de monstro (solo/elite) em 2024; o "chefe" é o monstro lendário (ações lendárias 3 + resistência lendária + covil).
- LACUNA: o que o DMG 2024 diz de grupo de 1-2 ou de 6+ fora do capítulo de encontro (o livro é fechado; o SRD não traz). A regra de multiplicador por tamanho de grupo do DMG 2014 (menos de 3 / 6 ou mais) não entrou no SRD 5.2.1 e não foi conferida aqui.
- CONTA [I minha] conta-dnd2024-um-monstro.py (nesta pasta): maior ND de UM monstro que cabe no orçamento, por N:
  - nível 10: N=1 → baixa ND 4, moderada ND 6, alta ND 7; N=2 → 7/8/10; N=4 → 10/12/14; N=6 → 12/15/17.
  - ND = nível consome do orçamento ALTO: N=1 1,64-1,90 (acima do alto); N=2 0,57-0,95; N=4 0,28-0,48; N=6 0,19-0,32 (níveis 5/10/15/20).
  - Ou seja: no D&D o tamanho do grupo move a FORÇA (o ND que você escolhe), e o bloco do monstro não muda com N.

## Marco 3 — Pathfinder 2e Remaster (AoN, integral e grátis via ORC/licença da Paizo)

- [C] GM Core p. 75-76, https://2e.aonprd.com/Rules.aspx?ID=2716 — Table 10-1: Trivial 40 ou menos (ajuste 10), Low 60 (20), Moderate 80 (20), Severe 120 (30), Extreme 160 (40). Table 10-2: nível do grupo -4 = 10 XP ("Low-threat lackey") ... 0 = 40 ("Any standard creature or low-threat boss"), +1 = 60, +2 = 80 ("Moderate- or severe-threat boss"), +3 = 120, +4 = 160 ("Extreme-threat solo boss"). Faixa: criaturas de -4 a +4.
  - "Different Party Sizes": "For each additional character in the party beyond the fourth, increase your XP budget by the amount shown in the Character Adjustment value"; "If you have fewer than four characters, use the same process in reverse"; "It's best to use the XP increase from more characters to add more enemies or hazards, and the XP decrease from fewer characters to subtract enemies and hazards, rather than making one enemy tougher or weaker."; "Encounters are typically more satisfying if the number of enemy creatures is fairly close to the number of player characters."; XP de recompensa não muda (sempre a de 4).
  - Quick Adventure Groups: Boss and Lackeys (120): 1 de +2 e 4 de -4; Boss and Lieutenant (120): 1 de +2 e 1 de nível; Elite Enemies (120): 3 de nível; Mated Pair (80); Troop (80); Mook Squad (60): 6 de -4.
  - Severe: "appropriate for important moments in your story, such as confronting a final boss"; Extreme: "likely to be an even match for the characters"; "Use an extreme encounter only if you're willing to take the chance the entire party will die."
- [C] GM Core p. 125 (Reactive Abilities), https://2e.aonprd.com/Rules.aspx?ID=2912: "A creature that's more likely to fight solo, on the other hand, might have a reaction to give it a way to continue to be dangerous amid an onslaught of attacks by the party." / "If you have a large number of creatures, skipping reactions can make the fight flow faster."
- [C] GM Core p. 123 (Action Economy), ID=2905: "Remember how short the lifespan of a typical combat creature is." / criaturas de nível alto "should get more abilities that improve their action economy".
- [C] Monster Core p. 6 (Elite Adjustments), ID=3264: +1 nível; +2 em CA, ataque, CD, salvaguardas, Percepção, perícias; +2 dano (+4 em habilidade limitada); PV +10 (nv ≤1), +15 (2-4), +20 (5-19), +30 (20+). Weak é o inverso. É o eixo de força "fino" (1 nível).
- [C] GM Core p. 20 (Group Composition), ID=908: grupos grandes e pequenos — para grupo pequeno, soluções do lado do JOGADOR (dois personagens por jogador, NPC de apoio, free archetype, tesouro extra), não do inimigo. Dual-Class PCs (ID=1328) "particularly small play group".
- [C] NPC Core p. 7 (Troops), ID=3364: "a 'creature' with the troop trait consists of multiple creatures working in tandem"; perde segmento a 2/3 e 1/3 dos PV (equivalente PF2e do esquadrão em pool).
- Economia de ação: toda criatura tem 3 ações + reação, independente de ser chefe. Não há ação lendária nem turno extra no núcleo. O chefe solo compensa com NÍVEL (+2 a +4 = números maiores, ≈ acerta mais e crita mais) e com reação.
- CONTA [I minha] conta-pf2e-um-monstro.py: nível da criatura única que cabe, por N (moderada / severa / extrema):
  - N=1: -2 / -1 / +0 (baixa: orçamento 0, nada cabe)
  - N=2: +0 / +1 / +2
  - N=3: +1 / +2 (sobra 10) / +3
  - N=4: +2 / +3 / +4
  - N=5: +2 (sobra 20) / +3 (sobra 30) / +4 (sobra 40)
  - N=6: +3 / +4 (sobra 20) / +4 (sobra 80 — a tabela acaba no +4; o resto TEM de virar mais criaturas)
  - Conclusão: o PF2e tem um TETO no chefe solo (+4); acima de 4 PJs o livro manda somar corpos, não engordar o chefe.

## Marco 4 — Draw Steel (texto de regra transcrito pelo Steel Compendium; Draw Steel: Monsters, cap. "Monster Basics")
Fonte: https://raw.githubusercontent.com/SteelCompendium/data-bestiary-md/main/Monsters/Chapters/Monster%20Basics.md (linhas citadas)
- [C] Organização (l. 222-256): Minion ("build encounters with them four at a time"), Horde ("about two to one"), Platoon ("one per hero"), Elite ("can usually stand up to two heroes of the same level"), Leader ("two or more heroes"), Solo ("can typically stand toe-to-toe with six heroes of the same level").
- [C] ES por herói = 4 + 2 × nível; ES do grupo = soma (tabela vai de 1 a 8 heróis). Retainer conta como herói. A cada 2 Vitórias médias, +1 herói.
- [C] Orçamento: trivial < ES − 1 herói; fácil < ES; padrão ES a ES + 1 herói; difícil até ES + 3 heróis; extremo acima.
- [C] Nível: criatura até +2 acima (+3 com 6+ Vitórias); "Solo creatures are an exception... restrict them to no more than 1 level above the heroes' average level".
- [C] Quick building (l. 662-681): hero slots = nº de heróis (+1 por 2 Vitórias). "Eight minions fill one hero slot. Two horde creatures fill one hero slot. One platoon creature fills one hero slot. One leader or elite creature fills two hero slots. One solo creature fills six hero slots plus one slot for each level the creature is higher than the heroes." Trivial −2 slots; fácil −1; padrão +0 (+1 se nenhum acima); difícil +2 (+1 se nem todos acima); extremo +4 ou mais.
- [C] Caixa "Parties Large and Small" (l. 685-691): "Draw Steel was made and tested with groups of mainly three to six heroes, including retainers"; 7+: "solo creatures don't quite live up to their name. So give the solo creatures some lackeys or a few more dynamic terrain objects"; dois solos: respeitar a regra de villain action e não concentrar os dois no mesmo herói; ≤3: "consider giving those heroes retainers to make up the difference. Parties that small can struggle against solo creatures and big groups of minions, given how much damage such foes have to spread around each turn."
- [C] Solo Creatures (l. 751): "Solo creatures can stand as an encounter all on their own for a group of four to six heroes."
- [C] Instant Solo (l. 756-775): EV ×3, Stamina ×2,5, "Solo Turns: The creature can take two turns each round. They can't take turns consecutively.", End Effect (10 de dano para encerrar efeito), "Solo Action (5 Malice): The creature takes an additional main action on their turn."
- [C] Villain actions (l. 210-220): "A creature with villain actions always has three. Each villain action can be used only once per encounter, and no more than one villain action can be used per round." Abertura / controle / "ult".
- [C] Malice (l. 337-339): início = média de Vitórias por herói; a cada rodada "Malice equal to the number of heroes in the battle, plus the combat round number"; herói morto para de gerar.
- [C] Star of the Show (l. 632): "set up a hard encounter and choose a leader or solo creature with an EV that is at least one-third of the encounter budget."
- [C] Initiative groups: "In a battle without a solo creature, you want about as many initiative groups as the number of heroes, plus or minus one or two."
- [C] Fórmulas (l. 1317-1380): Solo Stamina ×5, EV ×6; modificador de papel Solo +30, dano +2; "Elite, leader, and solo monsters have abilities that typically target two creatures or objects."
- [C] Retainers (cap. Retainers): "Each player can control only one retainer at a time." Retainer age no turno do mentor.
- CONTA [I minha] Solo de mesmo nível, em hero slots (6): N=1 → extremo; N=2 → extremo (difícil = 4, +1 = 5 < 6); N=3 → difícil (3+2+1 = 6); N=4 → difícil (6-7); N=5 → padrão (5+1 = 6); N=6 → padrão (6-7). Bate com "four to six heroes".
- CONTA [I minha] Malice que entra em 3 rodadas (sem Vitórias) = 3N + 6: N=1 → 9; 2 → 12; 3 → 15; 4 → 18; 5 → 21; 6 → 24. Em "Solo Action" de 5: 1,8 / 2,4 / 3,0 / 3,6 / 4,2 / 4,8 ações principais extras. → é o ÚNICO dos sete em que a economia de ação do chefe cresce SOZINHA com o nº de jogadores (pela renda de Malice), sem o mestre trocar de bloco.

## Marco 5 — Daggerheart (SRD 1.0, ver. 09/09/2025, licença DPCGL, grátis; texto via github.com/seansbox/daggerheart-srd, .build/01_pdf/DH-SRD-2025-09-09.md, que é o PDF oficial convertido)
- [C] Building Balanced Encounters (l. 3608-3624): "start with [(3 x the number of PCs in combat) + 2] Battle Points"; ajustes: −1 luta mais fácil/curta; −2 se 2+ Solos; −2 se +1d4 (ou +2) no dano de todos; +1 adversário de tier menor; +1 sem Bruiser/Horde/Leader/Solo; +2 luta mais difícil/longa. Custos: Minions 1 ponto "for each group of Minions equal to the size of the party"; Social/Support 1; Horde/Ranged/Skulk/Standard 2; Leader 3; Bruiser 4; Solo 5.
- [C] Tipos (l. 3514): "Solos: present a formidable challenge to a whole party, with or without support."
- [C] Relentless (X) (l. 3594): "This adversary can be spotlighted up to X times per GM turn. Spend Fear as usual to spotlight them."
- [C] Economia de ação: "there is no explicit initiative mechanic and characters don't have a set number of actions" (l. 1918). GM ganha Fear quando jogador rola com Fear; teto 12 (l. 2093, 3226); "You start a campaign with 1 Fear per PC in the party." (l. 3222); descanso longo: 1d4 + nº de PCs (l. 2285). "The GM can spend additional Fear to spotlight additional adversaries." (l. 2009).
- [C] Gasto de Fear por cena (l. 3240-3245): Standard 2-4; "Major: A large battle with a Solo or Leader adversary" 4-8; Climactic 6-12.
- [C] Benchmarks por tier (l. ~3630): ataque +1/+2/+3/+4; Difficulty 11/14/17/20; limiares 7/12, 10/20, 20/32, 25/45.
- [C] Blocos escalam por nº de PCs em alguns efeitos: "Endless Legions: spend a Fear to summon a number of Fallen Shock Troops equal to twice the number of PCs"; Demon "starts with a number of handfuls equal to the number of PCs"; ambiente "a number of Minor Treants equal to the number of PCs".
- MEDIDA [I minha] no JSON do SRD (129 adversários): PV mediano (slots) Standard 4/4/6/- ; Bruiser 6,5/7/7/8 ; Leader 6/6/7/8 ; Solo 8/9/10/8 (tiers 1-4). Solo ≈ 1,5-2,2× o Standard em PV. Relentless dos Solos: 2 a 4 (Hydra = nº de cabeças); alguns Solos sem Relentless.
- CONTA [I minha] Battle Points 3N+2: N=1 → 5 (um Solo = orçamento inteiro); N=2 → 8; N=3 → 11; N=4 → 14; N=5 → 17; N=6 → 20. Solo = 100% / 62% / 45% / 36% / 29% / 25% do orçamento. → no Daggerheart o Solo NÃO escala com N; o que escala é o que vem com ele. A economia de ação do Solo depende de Fear (que vem dos dados dos jogadores — mais jogadores rolando, mais Fear, [I]) e do Relentless (fixo no bloco).
- Faixa de grupo: não achei no SRD frase que declare "de X a Y jogadores". A fórmula aceita qualquer N.

## Marco 6 — 13th Age (1ª edição pelo SRD aberto; 2ª edição só pelo preview oficial grátis)
Fonte: 13th Age Archmage Engine SRD v3.0 (OGL), via https://www.13thagesrd.com (o site mistura material 3pp; usei só as seções do Archmage Engine).
- [C] Monster Rules (https://www.13thagesrd.com/monsters/monster-rules/): "Sizes are regular, large, and huge. Regular-sized monster can have double-strength (2x) and triple-strength (3x)." / "Large monsters generally have twice the hit points and deal roughly double the damage of a normal-sized monster. They also count as two monsters when you build a battle. Huge monsters have triple the hit points, deal triple damage, and count as three normal-sized monsters". Mook: dano rastreado no bando, excedente transborda; "A mook's hit point value is one-fifth that of a regular monster" (⚠ a tabela de criação dá 1/4: nível 5, 18 contra 72).
- [C] Building Battles (https://www.13thagesrd.com/running-the-game/): "For adventure tier, levels 1-4, start with one enemy creature of the party's level per PC. At champion tier, levels 5-7, start with one enemy creature per PC, with each creature being one level higher than the PCs. At epic tier, levels 8–10, the monsters should weigh in at two levels above the PCs if they appear in equal numbers."
  - Tabela Monster Equivalents (adventurer tier; champion e epic deslocam 1 e 2 níveis): 2 abaixo = normal 0,5 / mook 0,1 / large 1 / huge 1,5; 1 abaixo = 0,7 / 0,15 / 1,5 / 2; mesmo nível = 1 / 0,2 / 2 / 3; 1 acima = 1,5 / 0,3 / 3 / 4; 2 acima = 2 / 0,4 / 4 / 6; 3 acima = 3 / 0,6 / 6 / 8; 4 acima = 4 / 0,8 / 8 / (vazio no SRD).
  - Mooks: champion/epic 5 = 1 padrão; nível 1-2: 3 = 1; nível 3-4: até 4 = 1.
  - "Unfair Encounters": potent powers, nastier specials, weight of numbers, reinforcements, advantageous terrain.
- [C] Monster Creation (https://www.13thagesrd.com/monsters/monster-creation/): três tabelas-base (Normal, Large/Double-Strength, Huge/Triple-Strength) + Mooks. Medido [I minha]: Large = 2,00× dano e 2,00× PV do normal em todos os níveis 1-14 (nível 0: 2,25/2,05); Huge = 3,00×/3,00× em todos. "When it comes to large (or double-strength) or huge (or triple-strength) monsters, you don't have to put all their damage into one strike. Split damage up into smaller attacks or use conditional follow-up attacks." Subir 1 nível só num eixo: +6 ataque, ou +6 CA, ou dobrar PV, ou "Add a second attack or ongoing damage".
  - Valores (nível 5): normal 18 dano / 72 PV; large 36 / 144; huge 54 / 216; mook 9 dano / 18 PV. (nível 10): 58/216; 116/432; 174/648; 37/54.
- [C] Escalation die (combat-rules): só PJs (+1 por rodada a partir da 2ª, teto +6); exceção declarada pelos autores: dragões (LEVANTAMENTO-pe.md já tinha).
- Economia de ação: monstro tem 1 turno; o large/huge não ganha turno extra por regra — ganha ataques extras dentro do turno e ataques condicionais (acerto natural par etc.) [C: "Split damage up into smaller attacks or use conditional follow-up attacks"].
- [F] 13th Age 2E preview (Pelgrane, abr/2024, grátis): https://pelgranepress.com/wp-content/uploads/2024/05/13th_Age_2E_preview_updated.pdf — "Our new battle-building guidelines make life harder on large parties (in a good way), and that isn't reflected in earlier adventures' battle-building advice." Recursos de descanso longo: "four average fights, or three tough fights".
- [F] FAQ Pelgrane 24/11/2025: SRD ainda é o da 1E; 2E tem "new battlebuilding guidelines" (GMG p. 42); aventuras 1E "that include battle building tables for different numbers of players should be adjusted". → LACUNA: a tabela nova da 2E (GMG p. 42) é livro fechado; não li.
- Faixa de grupo: 1E soma por PJ (linear), sem faixa declarada que eu tenha achado no SRD.

## Marco 7 — Lancer (o capítulo de NPC e o do GM são livro FECHADO)
- [F] Massif Press, página do PDF grátis: https://massif-press.itch.io/corebook-pdf-free — a edição grátis "does not include NPC creation, the GM section, and setting info" (resumo do buscador; li só o título/descrição). → o núcleo de NPC (Elite, Ultra, Grunt, Veteran, Commander) e o balanceamento de encontro do livro NÃO são abertos. LACUNA declarada.
- [F/I] Lancer FAQ & Errata (compilação de comunidade com decisões do designer marcadas "word of Tom"): https://lancer-faq.netlify.app/
  - NPC padrão: "have only one Structure and are automatically destroyed without a Structure Damage check when they reach 0 HP"; "By default, NPCs only have one Stress"; templates como "Veteran or Ultra templates" dão mais Structure/Stress; Grunt: "any Heat from an external source will automatically destroy them".
  - "If an NPC takes more than one turn a round... they are still only able to use 1/round abilities once a round... However, NPCs with the Ultra template specifically refresh Reactions each time they take a turn due to their Shock and Awe feature, and can Overwatch unlimited times per round as due to their Reflex feature." [word of Tom] → confirma que existe NPC de vários turnos por rodada e que o Ultra reabre reação a cada turno.
- [I] owacsender (comunidade): https://owacsender.substack.com/p/the-gms-guide-to-building-lancer — "Elite: Adds +1 structure, +1 activation, +1 class optional."; "Ultra: Adds +3 structure, +1-2 activations (if you're at 5 players, it gets +2), +1-3 powerful Ultra optionals."; Elite e Ultra não se combinam no mesmo NPC; estrutura inimiga total "between 1.5-2x your player count"; ativações "around 1.5x your player count"; "throw the core book balancing rules out the window for the most part"; "Build for 3" e escalar para 4-5.
- [I] Train Lightning (comunidade): https://trainlightning.com/solstice-rain-combat-lineup/ — preferência do autor: "about 1.5 NPCs for each 1 PC in the fight at a time, with a maximum number of NPCs deployed equal to about 3 times the number of PCs".
- [I] resumo de buscador, fonte não identificada: "Ultras count as 4 characters, elites count as 2" — NÃO confirmado; não usar como regra.
- Síntese: no Lancer o "chefe" é um NPC de classe + template; o eixo de força é o TIER (1-3) e os templates; o eixo de grupo é o nº de ativações. A ideia de ativação ∝ nº de jogadores (≈1,5×) é da comunidade; a do Ultra ganhar a 2ª ativação extra com 5 jogadores também é da comunidade (não conferida no livro).

## Marco 8 — checagem de status (retcon) e complementos
- [C] Fabula Ultima v1.1 Changelog ITA (público, Need Games, ago/2026): https://www.needgames.it/wp-content/uploads/2026/08/Fabula-Ultima-v1.1-Changelog-ITA.pdf
  - "[maggiore] Pag. 295, Creare un Élite, Creare un Campione. Non si possono più assegnare Abilità di Classe a élite e campioni." → mudou o que o elite/campeão GANHA (não recebe mais Habilidade de Classe), não o multiplicador.
  - "[maggiore] Pag. 349, Acchiappadraghi. Solo una versione campione che rimpiazzi tre o più soldati può stringere..." → confirma a unidade do campeão: "rimpiazzare N soldati" (substituir N soldados).
  - "[minore] Pag. 301, Fasi Multiple. Sezione sostituita con 'Fasi e Forme'."; "[minore] Pag. 86 ... i PNG a 0 PV vengono rimossi dai conflitti"; "[minore] Pag. 103 ... 'raggruppare' più Cattivi per formare una squadra che conta come un singolo Cattivo."
  - "[maggiore] Pag. 83, Superiorità in Combattimento. Le regole per generare Punti Superiorità sono cambiate e le azioni aggiuntive possibili sono state limitate." → regra que eu NÃO consegui ler (livro fechado); pode tocar em ação extra. LACUNA.
  - Nenhuma entrada muda PV ×N, turnos ×N ou iniciativa do campeão (o changelog lista "os mais importantes", então ausência é evidência fraca).
  - ⚠ Os PDFs em /wp-content/uploads/woocommerce_uploads/ do site da Need Games são arquivos de PRODUTO (pagos/entregues por compra) que a API de mídia expõe. NÃO abri nenhum.
- [C] 13th Age SRD, Monster Creation: subir um nível inteiro em tudo = "+1 to attack, +1 to all defenses, multiply its damage output by 1.25, and multiply its hit points by 1.25". [I minha] 1,25 × 1,25 = 1,56 ≈ o 1,5 da tabela de equivalência (1 nível acima = 1,5 monstros) → a equivalência do 13th Age é ≈ produto PV × dano.
