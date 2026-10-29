# Validação dos relatórios 01 e 02

Feita em 21/10/2026. Checagem de fonte primária sempre que deu (post original, página oficial, texto do PDF já baixado, API Pullpush pra thread do Reddit). Nada foi baixado; os PDFs já existentes em `02 - PDFs baixados/` foram lidos com `pdfinfo`/`pdftotext`.

## Resumo

**112 itens checados: 83 confirmados · 21 a corrigir · 8 não confirmáveis ou não verificados.**
- Relatório 01: 72 itens → 49 confirmados, 17 a corrigir, 6 não confirmáveis.
- Relatório 02: 40 itens → 34 confirmados, 4 a corrigir, 2 não confirmáveis.

Na contagem, "confirmado com ressalva", "confirmado + atualizar" e "confirmado / enganoso" entram como confirmados: o fato bate, mas a linha pede ajuste de redação ou de status, e a lista de correções no fim já inclui esses ajustes. O item de Lines & Veils entrou como confirmado (o crédito a Ron Edwards), com o *Sex & Sorcery* em aberto.

**O que mais importa corrigir:**
1. **Electric Bastionland "comentário mais votado"** (01 l.142, 02 l.91) — errado. O mais votado da thread do r/rpg é o de **Apocalypse World (215 pontos)**. A frase "melhor tentativa de codificar os princípios OSR" é de um comentário com **15 pontos**; o comentário de EB mais votado tem 63 e diz só o nome do jogo.
2. **Fronts** (01 l.65) — são da **1ª edição** do Apocalypse World (2010). A 2ª (2016) trabalha com **mapa de ameaças + relógios de contagem**; a evidência é indireta, mas consistente (ver tabela).
3. **Five Room Dungeon** (01 l.73) — o próprio site do Johnn Four diz **2002–2003**, não "2002–2007"; o livro grátis só sai **assinando a newsletter**.
4. **Paizo "GM Pet Peeves"** (01 l.29) — a thread é sobre manias de **jogadores** que irritam o mestre; não fala de DMPC nem deus ex machina. Essas queixas vêm do EN World 2019 (de um usuário só, "Blue").
5. **X-Card** — a licença é **CC BY-SA 3.0** (o texto só dizia "CC").
6. **Lines & Veils** — crédito a Ron Edwards **confirmado no próprio TTRPG Safety Toolkit** (PDF baixado) e na página de sessão zero do Daggerheart. A origem no *Sex & Sorcery* continua **sem fonte primária**: só wiki/blog. E a data do livro diverge (2003 em Designers & Dragons, 2004 em catálogo); o blog da Roll20 diz "discutido por Ron Edwards em 2004".
7. **Links mortos ou trocados:** o conselho de Delta Green no arcdream.com (redireciona pra loja → 404), os princípios do Cairn em `/wip/2e/` (404; endereço novo abaixo), a prévia do Never Unprepared (o PDF saiu do ar; o rel. 02 já tinha visto, o 01 ainda lista como disponível), o link do Matt Colville (é um ensaio dele num livro da Monte Cook Games, não a série *Running the Game*).
8. **Mudança de status:** em 08/06/2026 o Sly Flourish anunciou o ***Rise of the Lazy Gamemaster*** (~160 p., agnóstico de sistema; não substitui o *Return*). As "community copies" do Apocalypse World estão **esgotadas** ("All copies claimed!"). O Delta Green Handler's Guide em capa dura está **esgotado** na loja da Arc Dream.

**Generalizações a cuidar (não são erro de fato, mas exageram a fonte):**
- Boa parte do "consenso EN World 2019" (arcos, momento de cada um, DMPC, deus ex machina, não reclamar do plano descarrilado) é **um post só**, do usuário Blue.
- "Por isso todo mundo insiste em sessão zero" (01 l.33) é **inferência do agente**; o comentário do Kobold Press (Ariaspinner, 2012) só fala em incompatibilidade de estilo.
- Enquete Sly 2017: as ~162 respostas vieram de um pedido dele no Twitter e no Facebook (09/05/2017). "Viciada" está certo. Lembrar que "knowledgeable" (3,7%) aparece separado de "rules" (2,5%).
- Pesquisa Sly 2016: a fonte se contradiz (4.046 dicas na seção de dicas, "4.153" na de clusters), e o maior grupo é **improvise (1.689 dicas)**, não "foco nos jogadores" (742). A lista do relatório não está em ordem de tamanho.

---

## Relatório 01 — `01-comunidade-o-que-faz-um-bom-mestre.md`

| Linha | Afirmação | Veredito | Valor correto / observação | Fonte |
|---|---|---|---|---|
| 18 | Enquete Sly 2017, ~162 respostas, 36,4 / 23,5 / 16,7 / 13 / 12,3 / 8,6 / 8,6 / 6,2 / 4,9; regra 2,5% | CONFIRMADO | Todos os números batem. Publicada em 19/06/2017; coleta pelo Twitter e pelo Facebook em 09/05/2017 | https://slyflourish.com/dm_traits_analysis.html |
| 19 | EN World "Research: What Makes a GM Great?", 2019, ~19 posts; improviso e leitura da mesa são o tema mais repetido | CORRIGIR (leve) | Data (09/06/2019, por Solanima) e contagem (19 posts, 2 páginas) certas. Na pág. 1 o tema mais enfatizado é **comunicação** (Man in the Funny Hat, Jacob Lewis); improviso e leitura da mesa vêm juntos, mas não são o "mais repetido" | https://www.enworld.org/threads/research-what-makes-a-gm-great.659927/ |
| 21 | Sly 2016: 6.600 respostas válidas, 4.046 dicas, 7 grupos, "player" 2.044× | CONFIRMADO | Números certos. Ressalvas: a própria fonte fala em "4.153 tips" na parte dos clusters, e o maior grupo é *improvise* (1.689) | https://slyflourish.com/2016_dm_survey_results.html |
| 22 | EN World 2019: arco por personagem, saber o que cada jogador quer, momento de cada um, inclusive em one-shot | CONFIRMADO / enganoso | Está lá, mas quase tudo num post só (Blue, pág. 2) | idem, page-2 |
| 23 | "O mestre que nunca levava a ação do jogador em conta", exemplo da emboscada | CONFIRMADO | Post #7 de Pentius, "The HATE Thread" (25/06/2011) | https://www.enworld.org/threads/the-hate-thread.307839/ |
| 24 | Entusiasmo visível | CONFIRMADO | Morrus (pág. 1) e Scottius (pág. 2) | EN World 2019 |
| 25 | "Mais de um post" diz que os melhores mestres quase não usavam voz nem adereço | CORRIGIR | **Um** post diz isso (ART!: "none of them did voices, had cool props…"). Outros (der_kluge, Jacob Lewis, Man in the Funny Hat) só dizem que voz e adereço não são essenciais | EN World 2019, pág. 1 e 2 |
| 28 | Railroad; links TV Tropes e RPG.net | NÃO CONFIRMÁVEL (link) | TV Tropes e RPG.net devolvem 403/redirecionam pra robô; o conteúdo não foi lido. A afirmação em si é senso comum | — |
| 29 | DMPC e deus ex machina — fonte "EN World 2019; Paizo GM Pet Peeves" | CORRIGIR | A thread da Paizo é sobre **manias de jogadores** (interromper o texto de caixa, faltar etc.); não cita DMPC nem deus ex machina. As duas queixas estão no EN World 2019 (Blue) | https://paizo.com/threads/rzs2qjya&page=3 |
| 30 | Reclamar do plano descarrilado; recusar a ideia esperta | CONFIRMADO | Blue, EN World 2019 | idem |
| 31 | Favoritismo; regra da casa pra mirar um jogador; "único item moral" | CONFIRMADO com ressalva | Thread "Are Bad DMs bad people?" (HarbinNick, 09/05/2014). Quem diz que só o favoritismo é problema moral é **um usuário** (David knott 242). "Regra da casa" não aparece: o exemplo do OP é um item amaldiçoado dado a um jogador | https://paizo.com/threads/rzs2r0g0 |
| 32 | Mestre solto demais perde coerência | CONFIRMADO | Michele, EN World 2019 | idem |
| 33 | Comentário do Kobold: manias odiadas = incompatibilidade de estilo → por isso todo mundo insiste em sessão zero | CONFIRMADO / enganoso | O comentário existe (Ariaspinner: "style mismatches"). O post é de 12/03/2012 (Jeremy L. C. Jones; as manias são do James Jacobs, a maioria sobre jogadores). A ligação com sessão zero **não está na fonte** | https://koboldpress.com/the-lost-gm-scrolls-james-jacobs-lists-his-pet-peeves/ |
| 36 | MesaQuest: sessão zero = cenário, regras, tom, limites, horário | CONFIRMADO | Também fala de criar personagem junto | intercom.help/mesaquestrpg (link ok) |
| 45 | Don't Prep Plots, Justin Alexander, 2009 | CONFIRMADO | 23/03/2009 | https://thealexandrian.net/wordpress/4147/… |
| 46 | Trama vs situação; preparar trama dá mais trabalho | CONFIRMADO | "a lot more difficult to prep plots than situations" | idem |
| 46 | "Depois ele esclareceu que trama = ação dos PJs predeterminada; o plano do vilão pode existir" | CORRIGIR (redação) | Não há esclarecimento com essas palavras. O ensaio já traz "Goal-Oriented Opponents" (o plano do vilão), nos comentários de 2015 ele define railroad como negar a escolha do jogador pra impor um desfecho, e o texto de 2015 (Tools, Not Contingencies) manda preparar os planos dos NPCs | idem + /37422/ (18/06/2015) |
| 47 | "Virou referência padrão em r/rpg e r/DMAcademy" | NÃO CONFIRMÁVEL | É opinião; o Reddit está bloqueado. É plausível, mas não foi medido | — |
| 50–51 | Três pistas: pelo menos três pistas por conclusão; perder, ignorar, interpretar errado; inverso | CONFIRMADO com ressalva | O autor diz a frase do "perder/ignorar/interpretar" **brincando** ("I'm kidding, of course"). O **inverso** ("se os PJs têm acesso a quaisquer três pistas, chegam a pelo menos uma conclusão") vem da série Node-Based Design, não do ensaio das três pistas. Data original: blog de **2008** (arquivo 20080509) | https://thealexandrian.net/creations/misc/three-clue-rule.html |
| 55–56 | Node-based, 2010 em diante; 4 nós e 9 pistas; "5-Node Mystery" | CONFIRMADO | "Four nodes and nine clues" está na pág. 2. O 5-Node Mystery é outro artigo | node-design2.html; https://thealexandrian.net/?p=37903 |
| 59–60 | 8 passos na ordem; segredos e pistas = "heart"; 1–2 frases; soltos do local | CONFIRMADO | Ordem e citações batem | https://slyflourish.com/eight_steps_2023.html |
| 63 | Data do livro e se é pago: não confirmado | CONFIRMADO (completar) | *Return of the Lazy Dungeon Master*: Kickstarter em fev/2018, ebook a US$ 8 na época, impresso em out/2018. **Novo:** *Rise of the Lazy Gamemaster* anunciado em 08/06/2026 (~160 p., agnóstico de sistema, "isn't a rewrite") | https://slyflourish.com/return_of_the_lazy_dm.html · https://slyflourish.com/announcing_rise_of_the_lazy_gamemaster.html |
| 65 | Fronts · Apocalypse World (Vincent e Meguey Baker) | CORRIGIR | Fronts são da **1ª ed. (2010)**. A 2ª ed. (Kickstarter 2016, Meguey entra como codesigner) usa **mapa de ameaças + relógios de contagem**. Evidência indireta: o *AW Extended Refbook* diz que "inclui as regras de fronts da 1ª ed., atualizadas pra 2ª". Confiança média | https://payhip.com/b/C4Vr · https://en.wikipedia.org/wiki/Apocalypse_World |
| 66 | Relógio: antes das 9h evitável; 9h–12h inevitável mas dá pra se preparar; 12h acontece; função = ameaças com vontade própria | CONFIRMADO | O post é sobre a 2ª ed. e cita a pág. 117 | https://daily-apocalypse.com/daily-apocalypse/85-threat-countdown-clocks (abre; dá 404 só com cliente sem navegador) |
| 70 | Relógios de Blades: 4/6/8 segmentos; complicação marca 1–3 | CONFIRMADO | — | https://roll20.net/compendium/BITD/Rules:Progress%20clocks |
| 73 | Five Room Dungeon, meados dos anos 2000 (2002–2007) | CORRIGIR | O site do autor diz **"in 2002-2003"** | https://www.roleplayingtips.com/5-room-dungeons/ |
| 74 | Cinco batidas | CONFIRMADO | Nomes exatos: Entrance and Guardian; Puzzle or Roleplaying Challenge; Trick or Setback; Climax, Big Battle or Conflict; Reward, Revelation, Plot Twist | idem |
| 75 | Livro com 87 exemplos, grátis no roleplayingtips.com | CORRIGIR (leve) | 317 p. e 87 exemplos; é grátis, mas **só assinando a newsletter** | idem |
| 77–79 | Angry GM: encontro = pergunta dramática sim/não; acabou a pergunta, acabou o encontro | CONFIRMADO | 23/07/2013; "ends when the dramatic question has been answered" | https://theangrygm.com/how-to-build-awesome-encounters/ |
| 82 | "Resenhas dizem" que as tags "deveriam estar na caixa de todo mestre" | CORRIGIR | É **uma** resenha, sobre o WWN: "The Tag System should be in every GM's toolkit" (Tenkar's Tavern, 17/04/2025). O link de 2022 citado não traz a frase | https://www.tenkarstavern.com/2025/04/free-osr-worlds-without-number-free.html |
| 82 | SWN apareceu várias vezes na thread como conselho de sandbox | CONFIRMADO | SWN e WWN aparecem em ~6 comentários (o maior, Arvail, com 115 pontos, compara a construção de mundo do WWN com a do DMG 5e) | Pullpush, thread xropuc |
| 87–88 | AW 2010 / 2ª ed. 2016; agenda; lista fechada de movimentos; "never speak its name" | CONFIRMADO | A resenha do Alexandrian (02/12/2011) traz "this is all he's allowed to do" e o princípio "Make your move, but never speak its name" | https://thealexandrian.net/wordpress/9584/… |
| 92 | "Diga sim ou role os dados", Dogs in the Vineyard, Vincent Baker, 2004 | CONFIRMADO | 2004, Lumpley Games; a forma do livro é "Roll dice or say yes" | Wikipedia (Dogs in the Vineyard) |
| 93 | Mouse Guard/BW: sem dado, negar com motivo, teste com risco | CONFIRMADO com ressalva | A fonte é uma thread de fórum, não o livro; "negar com motivo" não aparece como passo | forums.burningwheel.com/…/11908 |
| 97 | Quick Primer (Matt Finch, 2008, 13 p., grátis) | CONFIRMADO | 2008, Mythmere Games; resenhista: "13-page PDF" | Stargazer's World 2009; Internet Archive |
| 97 | Citação "Na maior parte do tempo você não usa uma regra, usa uma decisão" | NÃO CONFIRMÁVEL | Não achei a frase no Finch. Parece paráfrase de resenha ("old school games don't use rule most of the time…"). Trocar as aspas por paráfrase | busca exata sem resultado |
| 98 | Principia Apocrypha: Perry, Milton, Lumpkin; grátis; CC BY-NC-SA 4.0; tradução PT-BR no itch | CONFIRMADO | Os princípios são de Ben Milton e Steven Lumpkin, "organizados e corrigidos" por David Perry. Tradução de Antônio Marcelo e Marcus Mortati (Geração Xeroks). A licença está no PDF | PDF local + itch |
| 99 | Princípios do Warden no Cairn | CONFIRMADO | Information, Difficulty, Preparation, Narrative Focus, Danger (perigo telegrafado, armadilha à vista), Treasure, Choice, Die of Fate | https://cairnrpg.com/second-edition/players-guide/overview-and-principles/ |
| 100 | Link `cairnrpg.com/wip/2e/overview-and-principles/` | CORRIGIR | **404**. Endereço atual na linha acima | — |
| 100 | Link RPG.net da resenha do Finch | CORRIGIR (link) | Redireciona pra home do fórum (forum.rpg.net). Alternativa: Stargazer's World | https://stargazersworld.com/2009/07/30/reading-recommendation-quick-primer-for-old-school-gaming/ |
| 102 | Robin's Laws, Robin D. Laws, SJG, 32 p. | CONFIRMADO | 32 p. no impresso; **38 p. no PDF**. Indicado ao Origins 2002. US$ 13,95 impresso / US$ 8 PDF; ainda à venda | https://www.sjgames.com/robinslaws/ |
| 103 | "Mais conselho em 32 páginas que um DMG de 250" | NÃO CONFIRMÁVEL | Não está no link do Sly (13/07/2009), que só diz "this wonderful 32 page book". Tirar as aspas ou achar a fonte | slyflourish.com/four_tips_from_robins_laws.html |
| 103 | Crítica: tipologia fixa, de uma cultura de jogo específica | CONFIRMADO com ressalva | Michael Suileabhain-Wilson, 29/11/2003. A crítica é que taxonomia fixa exclui quem não se encaixa (ele não se reconhece nela). "Cultura de jogo específica" é leitura do agente | https://plausiblydeniable.com/the-trouble-with-taxonomy/ |
| 106 | Matt Colville, Running the Game, desde 2016 | CONFIRMADO | 1º episódio em 21/02/2016 | MCDM wiki; TheTVDB |
| 107–108 | "Às vezes dizer não é o certo"; jogador passivo precisa de pergunta — link Monte Cook | CORRIGIR (fonte) | O link é um **ensaio do Colville no livro *Your Best Game Ever*** (Monte Cook Games), não a série. Ele confirma a parte da pergunta ao jogador passivo; a do "dizer não" **não está lá** | montecookgames.com/matt-colvilles-essay-from-your-best-game-ever/ |
| 113 | Sessão zero no material oficial do Daggerheart | CONFIRMADO | Página oficial; cita X-Card (Stavropoulos), Lines and Veils (Ron Edwards), CATS (Patrick O'Leary) e o Core Rulebook p. 169 | https://www.daggerheart.com/sessionzero/ |
| 116 | Lines & Veils: crédito a Ron Edwards; origem no Sex & Sorcery (2003) não confirmada | CONFIRMADO (crédito) / NÃO CONFIRMÁVEL (livro) | O crédito está no próprio Safety Toolkit ("Linhas e Véus foi criado por Ron Edwards") e no Daggerheart. O *Sex & Sorcery* só aparece em fontes secundárias (RPG Museum wiki), a data do livro diverge (2003 / 2004) e o blog da Roll20 diz "discutido por Ron Edwards em 2004". Manter "não confirmado" | PDF do Toolkit PT-BR; blog.roll20.net |
| 118–119 | X-Card, John Stavropoulos, 2013, pensado pra jogar com estranhos; licença Creative Commons | CORRIGIR (precisar) | Tudo certo; a licença é **CC BY-SA 3.0 Unported** | doc original (PDF local); Wikipedia |
| 122–123 | Safety Toolkit: Kienna Shaw e Lauren Bryant-Monk; ENNIE 2020 de melhor produto gratuito; favoritar em vez de baixar | CONFIRMADO | ENNIE 2020 **ouro**, Best Free Game/Product. O guia atual é a v2.5 | Wikipedia (2020 ENnie Award winners); ttrpgsafetytoolkit.com |
| 127 | Never Unprepared, Engine Publishing, 2012, 128 p.; prévia grátis de 16 p. | CORRIGIR (link) | Data e páginas certas (anúncio de 30/05/2012; US$ 19,95 impresso + PDF, US$ 9,95 PDF). O **PDF da prévia saiu do ar** (redireciona pra /404page/); a página do post ainda abre | gnomestew.com (post de 2012) |
| 128 | So You Want to Be a Game Master, 2023, 544 p.; resenha "o livro que o hobby esperava" e 2/5 | CONFIRMADO | Page Street Publishing, 21/11/2023. Burn After Running (11/11/2023); Torchless 2/5 (09/02/2024) — as citações batem | links do relatório |
| 129 | How to Run Roleplaying Games (Stolze), link divnull | CORRIGIR | O link é o ***How to Play*** (do jogador). O do mestre está em https://gregstolze.itch.io/how-to-run-roleplaying-games. O erro já vinha do comentário do Reddit | rel. 02 l.25 |
| 135 | Thread r/rpg: 217 pontos, 132 comentários, set/2022 | CONFIRMADO | 30/09/2022, autor shadytradesman | Pullpush |
| 136 | r/RPGdesign "The best GM sections in RPGs", mar/2024 | CONFIRMADO | 12/03/2024 | Pullpush |
| 140 | AW: US$ 20 no itch; community copy grátis; mais citado | CONFIRMADO + atualizar | Preço certo. Comentário do topo: "Apocalypse World. Hands down." (215). **Community copies esgotadas** ("All copies claimed!") em 21/10/2026 | https://lumpley.itch.io/apocalypse-world |
| 141 | DW texto CC BY 3.0; direitos comprados em 2024 por Luke Crane e John Dimatos; 2ª ed. em desenvolvimento | CONFIRMADO | Vendido por Koebel e LaTorra; codesigners da 2ª: Spencer Moore e Helena Real | Wikipedia; Rascal News; dungeon-world.com |
| 142 | EB: "comentário mais votado da thread: melhor tentativa de codificar os princípios OSR" | CORRIGIR | O mais votado é o de AW (215). A frase é de b44l, com **15 pontos**. EB aparece em vários comentários (o maior, com 63, só diz o nome) | Pullpush |
| 142 | EB US$ 24; edição grátis com 10 carreiras | CONFIRMADO | "$24.00 USD or more"; a grátis é "name your own price" | itch |
| 142 | "O mestre é instruído a nunca preservar o status quo" | NÃO VERIFICADO | Não conferido (livro pago) | — |
| 143 | Blades: capítulo do mestre fora da SRD; Fine Blueprints grátis | CONFIRMADO | A SRD só tem uma seção curta "The Game Master" em Basics | bladesinthedark.com/basics |
| 144 | Mothership WOM: artigos de 2 p.; TOMBS; US$ 20; resenha 4/5 | CONFIRMADO | US$ 20 (impresso + PDF ou só PDF), ~60 p. A página da loja não cita o TOMBS, mas a Wikipedia e a resenha citam | tuesdayknightgames.com; Wikipedia |
| 145 | WWN Free Edition; SWN Revised grátis na DriveThru | CONFIRMADO | DTRPG 348809 e 230009 | Tenkar 2022; busca |
| 146 | 4e DMG 1 e 2: "o DMG 2 é o mais lembrado" | CORRIGIR | A thread cita **"DMG 1 & 2" juntos** (151 pontos); nada destaca o 2 | Pullpush |
| 147 | DG Handler's Guide: avisar que morte é provável; "coisas piores que a morte"; 5/5 RPG.net e EN World | CORRIGIR (fonte) | Os 5/5 estão na loja. Os conselhos vêm do **post "Advice for new Delta Green Handlers" (blog, dez/2017)**, não do livro, e esse **link morreu** (redireciona pra shop.arcdream.com → 404). O livro em capa dura está esgotado | busca; shop.arcdream.com |
| 147 | Need to Know: ENNIE ouro | CONFIRMADO | ENNIE **2016**, Best Free Game | Wikipedia (2016 ENnie) |
| 148 | CoC: "o único que ensina a usar as regras…"; 448 p.; Quick-Start ENNIE prata 2014 | CONFIRMADO | O comentário existe (Shotofentropy, 1 ponto: opinião isolada). 448 p. e US$ 54,95 (ficha da Chaosium). Prata 2014 em Best Free Product | Pullpush; Chaosium; Wikipedia |
| 149 | Night's Black Agents / Conspyramid citado em 2024 | NÃO VERIFICADO | A thread de 2024 tem 0 comentário no Pullpush; fica só o trecho de busca | — |
| 150 | PF2e "um respiro comparado ao 5e"; tabelas do GMG do PF1 | CONFIRMADO | "breath of fresh air" (14 pontos); GMG do PF1 (1 ponto) | Pullpush |
| 151 | DMG 2024: nota 7/10 na Wargamer | CONFIRMADO | — | https://www.wargamer.com/dnd/2024-dungeon-masters-guide-review |
| 152 | Cairn: grátis, CC BY-SA 4.0 | CONFIRMADO | O Warden's Guide é a v1.0.0, de março de 2026 | PDF local; site |
| 156 | Outros citados 1–2 vezes (ICRPG, Risus, Smallville/Leverage, Planescape, LotFP, Numenera, Conan, MotW, Fate) | CONFIRMADO | Todos aparecem. ICRPG tem 54 pontos: "I'd buy the system solely for the GM advice" | Pullpush |
| 174 | DG Need to Know: link exato não confirmado | CONFIRMADO (completar) | A página Start Here do delta-green.com aponta pro produto 175760 da DriveThru | https://www.delta-green.com/start-here/ |

---

## Relatório 02 — `02-catalogo-pdfs-e-guias.md`

| Linha | Afirmação | Veredito | Valor correto / observação | Fonte |
|---|---|---|---|---|
| 4 | 25 PDFs | CONFIRMADO | 25 arquivos; as contagens de página de todos batem com o `pdfinfo` | pasta local |
| 22 | Cairn 2e WG, 192 p., CC BY-SA 4.0 | CONFIRMADO | O link `yochaigal.itch.io/cairn-wardens-guide` agora redireciona pra **cairnpress.itch.io/cairn-wardens-guide** | PDF + curl |
| 24 | Stolze How to Run, 13 p., CC BY-ND, pague quanto quiser, zip | CONFIRMADO | O itch diz "Creative Commons Attribution/Non-derivative license" e não informa a versão | itch |
| 25 | How to Play, 10 p.; o link do rel. 01 é o de jogador | CONFIRMADO | — | PDF |
| 26 | Fine Blueprints, Michael Elliott, 12 p. | CONFIRMADO | — | PDF |
| 27 | Principia PT-BR 31 p., CC BY-NC-SA 4.0; site original fora | CONFIRMADO | principiaapocrypha.com **não resolve DNS** (provável domínio expirado) | PDF; curl |
| 29 | Ironsworn 270 p., CC BY-NC-SA 4.0, "Oracles in Guided Play" | CONFIRMADO | Capítulo na p. 166 | PDF |
| 30 | Daggerheart SRD 2.0, 224 p.; GM Guidance p. 85; Additional p. 183; DPCGL | CONFIRMADO | — | PDF |
| 31 | Homebrew Kit 26 p., DPCGL | CONFIRMADO | — | PDF |
| 32 | SRD 5.2.1, 364 p., CC BY 4.0, Gameplay Toolbox p. 192 | CONFIRMADO | — | PDF |
| 33 | CoC Quick-Start 48 p. | CONFIRMADO | — | PDF |
| 34 | EB Free 42 p.; o PDF diz que o guia de preparo está na completa | CONFIRMADO | "A complete guide to preparing and running the game" (p. 39) | PDF |
| 40 | X-Card 36 p.; licença "CC" | CORRIGIR (precisar) | **CC BY-SA 3.0 Unported** | PDF |
| 41 | Toolkit PT-BR v2.3, 4 p.; atual em inglês v2.5 | CONFIRMADO | — | PDF; site |
| 43 | CATS: autor "(arquivo da pasta Tools do toolkit)" | CORRIGIR | Cheatsheet v1.1 de **Tomer Gurantz**, baseado no **CATS Method de Patrick O'Leary** (2016) | PDF local |
| 49–51 | Sly: Workbook (5 p.), Cheat Sheet (2 p., 2013), 5e revisado (1 p.); links | CONFIRMADO | Cheat sheet de 20/05/2013; o 5e revisado é de 07/02/2022 e é onde está o link das folhas do Workbook | slyflourish.com |
| 52–54 | Old Dragon 2 — "Buró / Old Dragon" | CORRIGIR (leve) | O site oficial assina como **Old Dragon Editora** (Old Dragon Ltda.); "Buró" não aparece | olddragon.com.br/livros/lb1 |
| 55 | Daggerheart Campaign Frame Materials 7 p., 34 MB | CONFIRMADO | — | pasta local |
| 62 | Cairn 1e PT-BR (Rafa Arruda), 34 p., CC BY-SA | CONFIRMADO com ressalva | O PDF diz CC-BY-SA 4.0; a página do itch diz "Creative Commons Attribution v4.0" (sem SA). Vale o PDF. O itch avisa que existe uma "Edição Básica" mais nova | PDF; itch |
| 66 | Links da seção 2 com status 200 | CONFIRMADO com ressalva | Angry GM (406) e daggerheart.com (403) recusam cliente sem navegador, mas abrem normalmente | curl + WebFetch |
| 79 | Cairn 2e Guia do Guardião PT-BR "completo" | NÃO CONFIRMÁVEL | O índice está em PT-BR e CC BY-SA 4.0, mas alguns títulos aparecem em inglês ("Forest Seeds", "Pointcrawls"); não dá pra garantir que está completo | pt-br.cairnrpg.com |
| 90 | AW US$ 20; community copies | CONFIRMADO + atualizar | Community copies **esgotadas** em 21/10/2026 | itch |
| 91 | EB US$ 24; "(o relatório 01 dizia US$ 19)"; "comentário mais votado do r/rpg" | CORRIGIR | US$ 24 certo, mas o rel. 01 atual **já diz US$ 24**, então a nota está velha. "Mais votado" está errado (ver rel. 01 l.142) | itch; Pullpush |
| 92 | Mothership WOM ~US$ 20 | CONFIRMADO | US$ 20; o site respondeu hoje | tuesdayknightgames.com |
| 93 | DG Handler's Guide US$ 59,99 capa dura | CONFIRMADO + atualizar | Preço certo, mas **esgotado** ("sold out") | shop.arcdream.com |
| 94 | CoC Keeper Rulebook ~US$ 54,95 | CONFIRMADO | MSRP US$ 54,95 (ficha da Chaosium); a loja da Asmodee cobra US$ 54,99 e está esgotada | Chaosium sell sheet |
| 97 | Robin's Laws: preço não conferido | CONFIRMADO (completar) | US$ 13,95 impresso / US$ 8 PDF | sjgames.com/robinslaws |
| 98 | SYWTBAGM: "livrarias" | CONFIRMADO (completar) | Editora Page Street Publishing; ISBN 9781645679158 | livrarias |
| 99 | Never Unprepared: preço não conferido | CONFIRMADO (completar) | No lançamento (2012): US$ 19,95 impresso + PDF, US$ 9,95 PDF. Preço atual não conferido | gnomestew 2012 |
| 103 | T20 ~R$ 170; só o Introductory Kit grátis no Roll20, não baixa | CONFIRMADO | R$ 170,75 (Edição Jogo do Ano, capa dura, Magalu); preço de referência R$ 225. O kit é grátis, "can only be used with Roll20; cannot be downloaded" | marketplace.roll20.net/…/19562 |
| 110 | DG Need to Know, DTRPG 175760 | CONFIRMADO | — | delta-green.com/start-here |
| 111 | WWN Free 348809; Deluxe US$ 19,99; SRD CC0 473939 (Tenkar 2025) | CONFIRMADO | Post de 17/04/2025 | Tenkar's Tavern |
| 112 | SWN Revised Free 230009 | CONFIRMADO | — | busca |
| 113 | OD2 Livro I grátis, ~27 MB, capítulo pra mestres, "Resgatar" | CONFIRMADO | 27,4 MB | olddragon.com.br/livros/lb1 |
| 114 | Five Room Dungeons: 317 p., 87 exemplos, via newsletter | CONFIRMADO | — | roleplayingtips.com/5-room-dungeons/ |
| 117 | Toolkit v2.5 bloqueado pra download | NÃO CONFIRMÁVEL | Não testei (a regra era não baixar) | — |
| 118 | Prévia do Never Unprepared fora do ar | CONFIRMADO | Redireciona pra gnomestew.com/404page/ | curl |
| 119 | Quick Primer: Lula 404; existência confirmada por resenhas | CONFIRMADO + nota | Há cópia no Internet Archive (`archive.org/details/a-quick-primer-for-old-school-gaming`). Não é distribuição oficial do autor, então pela regra do catálogo fica só como nota | busca |
| 120 | Principia original fora | CONFIRMADO | Falha de DNS | curl |
| 124 | DG "The Fundamentals" no iCloud | CONFIRMADO | — | delta-green.com/start-here |

---

## Correções a aplicar

Relatório 01 (`01-comunidade-o-que-faz-um-bom-mestre.md`):

- **l.19** — "improviso e ler a reação da mesa é o tema mais repetido." → "comunicação, improviso e ler a reação da mesa são os temas mais repetidos."
- **l.25** — "Mais de um post no EN World diz que os melhores mestres que tiveram quase não usavam voz nem adereço." → "Um post no EN World (ART!) diz que os melhores mestres que teve quase não usavam voz nem adereço; outros dizem que ajuda, mas não é essencial."
- **l.29** — "(EN World 2019; Paizo \"GM Pet Peeves\") https://paizo.com/threads/rzs2qjya&page=3" → "(EN World 2019, um post do usuário Blue)"
- **l.31** — "Num fórum da Paizo é apontado como o único item que é problema \"moral\" e não de estilo." → "Na thread \"Are Bad DMs bad people?\" (Paizo, 2014), um usuário aponta o favoritismo como o único item que é problema \"moral\" e não de estilo."
- **l.33** — "→ por isso todo mundo insiste em sessão zero." → "(a ligação com a sessão zero é nossa, não do comentário)."
- **l.46** — "Depois ele esclareceu que \"trama\" aqui é *ação dos PJs predeterminada* — o plano do vilão pode e deve existir." → "O próprio ensaio manda preparar o objetivo do vilão (\"Goal-Oriented Opponents\"); nos comentários ele define railroad como negar a escolha do jogador pra impor um desfecho já decidido."
- **l.51** — "Inverso: se os PJs têm acesso a quaisquer três pistas, chegam a pelo menos uma conclusão." → "Inverso (da série Node-Based): se os PJs têm acesso a quaisquer três pistas, chegam a pelo menos uma conclusão."
- **l.63** — "(Data do livro e se é pago: não confirmei nesta busca — de memória, é pago.)" → "(*Return of the Lazy Dungeon Master*, 2018, pago. Em 08/06/2026 saiu o anúncio do *Rise of the Lazy Gamemaster*, ~160 p., agnóstico de sistema, que expande os 8 passos sem substituir o *Return*.)"
- **l.65** — "**Fronts e relógios de contagem** · Apocalypse World (Vincent e Meguey Baker), herdado por Dungeon World e Blades" → "**Fronts e relógios de contagem** · Apocalypse World 1ª ed. (2010; na 2ª ed., de 2016, os fronts dão lugar ao mapa de ameaças, e os relógios continuam), herdado por Dungeon World e Blades"
- **l.73** — "meados dos anos 2000 (as fontes divergem: 2002–2007)" → "2002–2003, segundo o site do autor"
- **l.75** — "Livro com o modelo e 87 exemplos, grátis no roleplayingtips.com (segundo …)." → "Livro com o modelo e 87 exemplos (317 p.), grátis no roleplayingtips.com pra quem assina a newsletter."
- **l.82** — "Resenhas dizem que o sistema de tags \"deveria estar na caixa de todo mestre\"." → "Uma resenha do Tenkar's Tavern (2025) diz que o sistema de tags \"deveria estar na caixa de todo mestre\"."
- **l.97** — "\"Na maior parte do tempo você não usa uma regra, usa uma decisão.\"" → "Na maior parte do tempo, o mestre decide pelo bom senso em vez de procurar uma regra (paráfrase)."
- **l.100** — "https://www.rpg.net/reviews/archive/16/16298.phtml" → "https://stargazersworld.com/2009/07/30/reading-recommendation-quick-primer-for-old-school-gaming/" e "https://cairnrpg.com/wip/2e/overview-and-principles/" → "https://cairnrpg.com/second-edition/players-guide/overview-and-principles/"
- **l.102** — "32 páginas" → "32 páginas (38 no PDF), 2002"
- **l.103** — "Elogiado como \"mais conselho em 32 páginas que um DMG de 250\";" → "Elogiado como denso pro tamanho;" e "criticado porque a tipologia é fixa e saiu de uma cultura de jogo específica" → "criticado porque a tipologia é fixa e deixa de fora quem não se encaixa nela"
- **l.107–108** — "Pontos citados: às vezes dizer \"não\" é o certo; jogador passivo geralmente só precisa de uma pergunta" → "Num ensaio dele no livro *Your Best Game Ever* (Monte Cook Games): jogador passivo geralmente só precisa de uma pergunta"
- **l.116** — "a origem no suplemento *Sex & Sorcery* (2003) **não confirmei**." → "crédito confirmado no próprio TTRPG Safety Toolkit. A origem no suplemento *Sex & Sorcery* (2003 ou 2004, as fontes divergem) aparece só em fonte secundária; **não confirmei** no livro."
- **l.119** — "Licença Creative Commons." → "Licença CC BY-SA 3.0."
- **l.123** — "ENNIE 2020 de melhor produto gratuito." → "ENNIE 2020 ouro de melhor jogo/produto gratuito."
- **l.127 e l.179** — "tem prévia grátis de 16 páginas" → "a prévia grátis de 16 páginas saiu do ar"
- **l.129 e l.178** — "https://thor.divnull.com/pub/essay/how-to-play-roleplaying-games-stolze.pdf" → "https://gregstolze.itch.io/how-to-run-roleplaying-games"
- **l.140** — "tem \"community copy\" grátis pra quem não pode pagar." → "tem \"community copy\" grátis pra quem não pode pagar (esgotadas em 21/10/2026)."
- **l.142** — "Comentário mais votado da thread do r/rpg: \"melhor tentativa de codificar os princípios OSR\"." → "Citado em vários comentários da thread do r/rpg; um deles: \"melhor tentativa de codificar os princípios OSR\"."
- **l.146** — "o DMG 2 é o mais lembrado." → "citados juntos (DMG 1 e 2)."
- **l.147** — "https://arcdream.com/home/2017/12/advice-for-new-delta-green-handlers/" → "(post do blog da Arc Dream, dez/2017, link morto; os conselhos são do post, não do livro)" e "**quickstart \"Need to Know\" grátis** (ENNIE ouro)" → "**quickstart \"Need to Know\" grátis** (ENNIE ouro 2016)"
- **l.174** — "site da Arc Dream (grátis; link exato não confirmado)" → "https://www.drivethrurpg.com/product/175760/Delta-Green-Need-to-Know (grátis, exige conta; apontado por delta-green.com/start-here)"

Relatório 02 (`02-catalogo-pdfs-e-guias.md`):

- **l.22** — "https://yochaigal.itch.io/cairn-wardens-guide" → "https://cairnpress.itch.io/cairn-wardens-guide"
- **l.40** — "| CC; export em PDF do Google Doc oficial |" → "| CC BY-SA 3.0; export em PDF do Google Doc oficial |"
- **l.43** — "| (arquivo da pasta Tools do toolkit) |" → "| Tomer Gurantz (cheatsheet v1.1), sobre o CATS Method de Patrick O'Leary (2016) |"
- **l.52** — "Buró / Old Dragon" → "Old Dragon Editora"
- **l.62** — "CC BY-SA (tradução linkada pelo site oficial do Cairn)" → "CC BY-SA 4.0 segundo o PDF (a página do itch diz CC BY 4.0; tradução linkada pelo site oficial do Cairn)"
- **l.79** — "Guia de mestre completo em português" → "Guia de mestre em português (alguns títulos ainda em inglês; não conferi se está completo)"
- **l.90** — "tem \"community copies\" grátis pra quem não pode pagar" → "tem \"community copies\" grátis pra quem não pode pagar (esgotadas em 21/10/2026)"
- **l.91** — "**US$ 24** no itch hoje (o relatório 01 dizia US$ 19)" → "**US$ 24** no itch hoje" e "Comentário mais votado do r/rpg: melhor codificação dos princípios OSR." → "Citado em vários comentários do r/rpg (um deles: melhor codificação dos princípios OSR)."
- **l.93** — "US$ 59,99 capa dura (loja da Arc Dream, conferido)" → "US$ 59,99 capa dura (loja da Arc Dream; esgotado em 21/10/2026)"
- **l.97** — "| preço não conferido | Steve Jackson Games |" → "| US$ 13,95 impresso / US$ 8 PDF | Steve Jackson Games |"
- **l.98** — "| preço não conferido | livrarias |" → "| preço não conferido | Page Street Publishing (livrarias) |"
- **l.119** — acrescentar: "Há cópia no Internet Archive (não oficial)."
