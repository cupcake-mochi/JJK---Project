# DOSSIÊ DE METODOLOGIA

**Fase 1 — pesquisa.** O que a gente vai usar para desenhar o sistema, e o que cada coisa obriga no nosso caso específico.
Versão v0.1 — 05/08/2026

Este documento não é aula de teoria. Todo achado vem colado na sua consequência prática para um sistema de JJK rodando num server de guilda com vários mestres, marcada como **"o que isso obriga"**. Achado que não gerou consequência não entrou.

Duas ressalvas de leitura. Primeira: quando o texto diz "vários mestres", é porque o número real de mestres ativos da Guilda ainda não está registrado — está na lista de perguntas em aberto e muda algumas contas. Segunda: todos os percentuais da seção 4 foram calculados e depois reconferidos por recálculo independente.

---

## 1. Duas lentes de decisão

Não são regras, são jeitos de fazer a pergunta certa quando a gente travar entre duas opções de mecânica.

### GNS — para que serve a mesa?

Ron Edwards separou o que as pessoas procuram numa mesa em três agendas: **gamismo** (vencer, superar desafio por decisão esperta), **narrativismo** (produzir história com significado) e **simulacionismo** (manter o mundo coerente consigo mesmo). A tese forte dele — que cada mesa persegue uma só, e que tentar servir as três é erro clássico de design — envelheceu mal e levou pancada por duas décadas. O próprio Edwards depois abandonou o GNS em favor do Big Model.

O que sobrou de útil não é a taxonomia, é o hábito: quando duas mecânicas parecem igualmente boas, perguntar *qual agenda cada uma serve* costuma revelar que elas nem estavam competindo.

**O que isso obriga:** JJK shounen puxa forte para gamismo (a luta é um teste que se vence sendo esperto) com uma camada narrativista no custo. O simulacionismo é o nosso menor interesse — não precisamos que energia amaldiçoada tenha física consistente, precisamos que ela cobre um preço dramático. Quando aparecer a tentação de "mas realisticamente...", essa é a lente que corta.

### MDA — de onde vem a sensação?

Mechanics (as regras escritas) → Dynamics (o que acontece de fato na mesa quando gente usa as regras) → Aesthetics (a emoção que sai disso). O designer escreve da esquerda para a direita; o jogador sente da direita para a esquerda.

Há debate honesto sobre se MDA cabe em RPG de mesa, já que RPG não tem mecanismo travado como jogo digital — o mestre é uma camada de interpretação no meio. Mesmo assim o modelo funciona bem em jogos de aventura de mesa, e o valor prático é este: **você não escreve a emoção, você escreve a regra que a produz.**

**O que isso obriga:** a gente vai declarar a estética antes da mecânica. "Quero que o jogador hesite antes de gastar" é estética. A mecânica é o que faz a hesitação existir. Toda proposta de regra no esqueleto vai ter que responder: *qual dinâmica isso cria na mesa, e qual sensação sai dela?*

---

## 2. O espaço de design: onde a gente cai

### Fantasy Heartbreaker — a armadilha nomeada

Edwards cunhou o termo para os RPGs dos anos 90 feitos por fãs apaixonados de D&D que queriam consertar D&D — e que traziam junto, sem perceber, um monte de premissa que nunca questionaram: atributo rolado aleatoriamente, o quarteto guerreiro/mago/ladino/clérigo, o trio humano/elfo/anão. Ele elogia as inovações reais desses jogos (sistemas de magia mais versáteis que slot de feitiço, por exemplo) e lamenta o resto. Vale registrar que no artigo original o termo é afetuoso, não pejorativo — a comunidade é que o transformou em xingamento depois.

**O que isso obriga:** nosso risco não é fazer um heartbreaker de fantasia, é fazer um **heartbreaker de shounen**: pegar o esqueleto de D&D 5e, trocar slot de feitiço por energia amaldiçoada, classe por "tipo de feiticeiro", e achar que inovou. A lista de premissas a questionar explicitamente no esqueleto:

- Pontos de vida como reservatório que esvazia
- Iniciativa por rodada com todo mundo agindo uma vez
- Atributo numérico de 6 pilares (For/Des/Con/Int/Sab/Car)
- Nível como número inteiro que sobe de um em um
- Classe fixa escolhida na criação
- Rolagem de ataque separada da rolagem de dano

Nenhuma delas é proibida. Todas precisam ser **escolhidas**, não herdadas.

### PbtA e FitD — o que dá pra roubar

Powered by the Apocalypse organiza o jogo em *moves*: gatilhos de ficção que disparam mecânica ("quando você faz X, role"). Forged in the Dark nasceu do PbtA mas divergiu em pontos que importam para nós: quebra a rolagem em **posição** (quão exposto você está) e **efeito** (quanto você consegue), introduz uma economia de **estresse**, e coloca **downtime** na estrutura do jogo em vez de deixar como tempo morto. As duas famílias compartilham DNA mas jogam bem diferente na mesa.

**O que isso obriga:** três peças são candidatas fortes a entrar no esqueleto, independentemente do resto:

1. **Gatilho de ficção antes da rolagem.** "Quando você força energia amaldiçoada além do seu limite, role" é mais arbitrável por cinco mestres diferentes do que "o mestre decide se pede um teste".
2. **Posição e efeito separados.** Resolve o problema clássico de "eu passei no teste, mas o que eu consegui?" sem depender do estilo do mestre.
3. **Downtime estruturado.** A Guilda joga RP por texto entre sessões. Isso *já é* downtime — só falta ele ter regra. É a peça que amarra o chat assíncrono ao jogo ao vivo em vez de deixar os dois em mundos separados.

### Referência de tom: JRPG e anime já resolvidos

Fabula Ultima (Need Games; edição em inglês de 2022, ouro no ENNIE 2023 de Melhor Jogo) resolve poder por **tamanho de dado crescente**: d6 é fraqueza, d12 é maestria; o teste é um pool de dois atributos, e vínculos e história do personagem permitem rerrolar. BESM 4ª edição vai pelo caminho oposto, universalista, cobrindo do romance escolar ao mecha com a mesma mecânica.

**O que isso obriga:** escada de dado (d6→d8→d10→d12) é uma alternativa séria a bônus numérico, e tem uma propriedade útil para nós — o teto é natural e visível. Não dá para "acumular +17". Vale colocar na disputa quando a gente for decidir a mecânica de resolução.

---

## 3. O problema central: um personagem, cinco mestres

Esta é a parte da pesquisa que mais muda o projeto, e é a que o pitch já tinha marcado como terceiro pilar.

### West Marches: o modelo que já resolve isso

Vários jogadores e vários mestres compartilham um mundo só. Sessões são autocontidas, formadas por grupos que mudam a cada vez, saindo de uma base fixa. O que acontece numa sessão muda o mundo para as próximas.

O que a prática consolidada recomenda para múltiplos mestres:

- **XP em vez de marco narrativo.** Progressão vira algo mensurável e igual entre grupos. Marco ("subiu de nível quando a história pedir") é exatamente o que quebra quando cada mestre tem um senso de ritmo diferente.
- **Guia do mestre com a matemática exposta:** conta de encontro, tabela de recompensa por faixa, regra de downtime, regra de morte e retorno.
- **Ritmo de recompensa padronizado.** Todos os mestres soltam prêmio no mesmo passo, ou o jogador aprende a escolher a mesa que paga melhor.
- **Ficha aprovada antes de entrar em jogo**, com submissão alguns dias antes. Regra de criação combinada entre os mestres.
- **Registro do mundo** com datas, locais visitados, facções e status — atualizado na hora em que algo muda.
- **Cuidado social explícito:** panelinha, membro inativo, loot injusto e briga por agenda são problemas previstos, não acidentes. Sessões de mistura com grupo sorteado são um remédio conhecido.

### Organized play: o mesmo problema em escala industrial

Pathfinder Society e Adventurers League resolvem personagem portátil entre mesas do mundo inteiro. O personagem cresce e carrega as recompensas para a próxima aventura mesmo com jogadores e mestres diferentes a cada vez. O preço é rigidez: regra de criação fechada, recompensa tabelada e relatório obrigatório depois de cada sessão.

**O que isso obriga — e é a consequência mais pesada do dossiê:**

Um sistema para personagem persistente entre mestres **não pode ter progressão negociável**. Toda mecânica que dependa de "o mestre decide o quanto você ganha" precisa virar tabela, relógio ou gatilho. Isso não é burocracia por gosto — é a peça estrutural que impede um jogador de descobrir qual mesa dá mais e passar a só frequentar ela.

E tem uma decisão de arquitetura que sai direto daqui: **a progressão precisa ser bounded**. Se não houver teto, um mestre não consegue escrever encontro sem saber a build exata do personagem. Detalho no próximo bloco.

---

## 4. Matemática de dado

Rodei tudo com `dice-calc` (PyPI, pure Python, zero dependência, compila código do AnyDice direto para Python). Confirmei que instala e roda no ambiente — dá para testar qualquer mecânica sem sair daqui e sem abrir o anydice.com.

### Quanto vale um +1

| Mecânica | Fácil (base ~80%) | Médio (base ~45%) | Difícil (base ~26%) |
|---|---|---|---|
| d20 puro | +5,0 pp (CD 5) | +5,0 pp (CD 11) | +5,0 pp (CD 16) |
| 2d6 | +8,3 pp (alvo 5) | +16,7 pp (alvo 8) | +13,9 pp (alvo 9) |
| 3d6 | +6,9 pp (alvo 8) | +12,5 pp (alvo 11) | +11,6 pp (alvo 13) |

**A leitura que importa:** no d20, um +1 vale sempre 5 pontos percentuais, não importa a situação. No 2d6, o mesmo +1 vale de 8 a 17 pp — e vale **mais no meio da curva**, que é exatamente onde a maioria dos testes acontece.

**Consequência direta para a Guilda:** um bônus improvisado de mestre ("beleza, isso te dá +1") custa três vezes mais numa curva de sino do que num d20. Ou a gente escolhe curva chata e libera os mestres para improvisar bônus, ou escolhe curva de sino e **proíbe bônus numérico improvisado**, substituindo por vantagem, rerrolagem ou mudança de posição. Escolher sino e deixar bônus solto é a receita para cinco mesas com dificuldades diferentes.

### O que vale um dado a mais

**Pool contando sucessos (Nd6, cada 4+ conta):**

A última coluna compara sempre com **um dado a menos**, medida em "≥2 sucessos".

| dados | ≥1 sucesso | ≥2 sucessos | o que o dado a mais rendeu |
|---|---|---|---|
| 1 | 50,0% | — | — |
| 2 | 75,0% | 25,0% | +25,0 pp |
| 3 | 87,5% | 50,0% | +25,0 pp |
| 5 | 96,9% | 81,2% | +12,5 pp |
| 8 | 99,6% | 96,5% | +2,7 pp |

**Pool estilo Blades (Nd6, olha o maior — 6 é sucesso total, 4-5 parcial, 1-3 falha):**

As duas últimas colunas estão separadas para mostrar onde nasce o crítico, mas **sucesso total é a soma das duas** — no Blades, tirar um 6 já é sucesso e dois 6 dão um bônus em cima, não uma categoria concorrente. Com 4 dados, sucesso total é 51,8%, não 38,6%.

| dados | falha (maior 1-3) | parcial (maior 4-5) | total, um 6 só | total, dois ou mais 6 |
|---|---|---|---|---|
| 0 (pior de 2) | 75,0% | 22,2% | 2,8% | — |
| 1 | 50,0% | 33,3% | 16,7% | — |
| 2 | 25,0% | 44,4% | 27,8% | 2,8% |
| 3 | 12,5% | 45,4% | 34,7% | 7,4% |
| 4 | 6,2% | 42,0% | 38,6% | 13,2% |
| 5 | 3,1% | 37,1% | 40,2% | 19,6% |

**A leitura que importa:** pool tem **teto embutido**. Do 1º para o 2º dado o ganho é enorme; do 7º para o 8º é ruído. Isso significa que uma progressão baseada em dados **se auto-limita** sem precisar de regra dizendo "o máximo é X". Para personagem que atravessa uma dúzia de mini-campanhas, isso é ouro: o sistema não explode sozinho.

Repare também na coluna de crítico do modelo Blades: ela **cresce** conforme o poder sobe enquanto a falha desaba. Isso é literalmente a curva de sensação shounen — o feiticeiro veterano raramente falha, mas quando acerta, acerta espetacular. A escalada de poder aparece na *qualidade* do sucesso, não na chance de sucesso.

### Vantagem no d20, para comparação

| CD | puro | com vantagem | ganho |
|---|---|---|---|
| 10 | 55,0% | 79,8% | +24,8 pp |
| 11 | 50,0% | 75,0% | +25,0 pp |
| 12 | 45,0% | 69,8% | +24,8 pp |
| 16 | 25,0% | 43,8% | +18,8 pp |

O ganho é simétrico em torno de CD 11, onde tem o pico exato de 25 pp — CD 10 e CD 12 valem rigorosamente o mesmo. Vantagem vale mais ou menos um +5. É um bônus grande disfarçado de mecânica simples — o que é bom para arbitragem (não tem conta) e perigoso para balanceamento (empilha fácil).

### Bounded accuracy

A ideia por trás do D&D 5e: manter a distância entre bônus de ataque, CA e CD relativamente constante ao longo do jogo, evitando corrida armamentista de números. O teto ali é bônus de atributo +5 e proficiência +6, dando +11 no total. A vantagem é que monstro fraco continua relevante e o mestre consegue improvisar cena sem consultar tabela. Uma objeção que circula na comunidade — não é consenso, é discussão de fórum — é que bounded accuracy combina mal com a distribuição chata do d20, e funcionaria melhor sobre uma curva.

**O que isso obriga:** para nós, bounded accuracy não é preferência, é requisito de arquitetura. Sem teto de números, um mestre da Guilda não consegue escrever encontro para "um feiticeiro de grau 2" sem saber a build exata. Com teto, "grau 2" vira informação suficiente. Vale registrar junto a objeção acima: se ela procede, ela empurra contra o d20, que é justamente a base que mais tenta um projeto vindo de D&D.

---

## 5. Metodologia de playtest

### Os estágios

Adaptado da prática da Storybrewers Roleplaying, que separa em cinco:

| Estágio | Quem joga | Para que serve |
|---|---|---|
| **Grosseiro** | só você (e o codesigner) | ver se a ideia funciona em algum nível |
| **Interno** | amigos próximos, com jogo mínimo viável | achar o ponto fraco antes de expor |
| **Ampliado** | rede maior, mesa "não vergonhosa" | ver a regra em ação com quem não tem compromisso emocional |
| **Cego** | outra pessoa mestra, você não está lá | descobrir o que o texto não diz |
| **Final** | material completo | conferir antes de fechar a versão |

É normal voltar um estágio depois de avançar. Isso não é fracasso, é o ciclo funcionando.

### Kleenex test

Você observa alguém que nunca viu o jogo jogar, **sem explicar nada e sem guiar**. O nome vem de Will Wright (SimCity, The Sims): o testador é descartável no sentido de que só serve uma vez — depois que a pessoa aprendeu, ela nunca mais é ingênua.

A regra de ouro do playtest cego: **o designer não vem dentro da caixa.** Toda pergunta que o testador faz é informação, mesmo quando a resposta está escrita nas regras — se ele perguntou, o texto escondeu bem demais.

### Que dado coletar

Dois conjuntos, e os dois importam:

**Observação sua.** Em que momento a energia da mesa subiu e em que momento morreu? Quem ficou sem holofote? Qual foi a carga mental do mestre — ele estava jogando ou administrando planilha? Reflita dentro da mesma semana, ou você perde. Um roteiro útil é os quatro F: **Fatos** (o que aconteceu), **Sentimentos** (o que se sentiu), **Achados** (o como e o porquê), **Futuro** (o que muda por causa disso).

**Retorno direto.** Conversa logo depois da sessão vem colorida pela emoção da mesa — ótimo para medir tom, ruim para crítica dura. Formulário anônimo depois pega o que ninguém fala na sua cara — melhor para achar o trecho fraco. Use os dois, para coisas diferentes.

**Analise tendência, não caso isolado.** Um comentário solto se descarta; um padrão não se ignora. Quando o retorno fica no meio do caminho, transforme em pergunta em vez de pular para a solução: *o que fez essas pessoas dizerem que X não funciona?*

### Quantas rodadas

Vem da usabilidade, não do RPG, mas a matemática é a mesma: Jakob Nielsen mostrou que **5 testadores pegam cerca de 85% dos problemas**, e que **três rodadas de 5 valem mais que uma rodada de 15** — porque entre uma rodada e outra você conserta, e o conserto cria problema novo que precisa ser pego.

**O que isso obriga:** nosso ciclo de playtest é 5 pessoas, três vezes, com correção entre as rodadas. Não é "testa até ficar bom", é "testa, conserta, testa de novo, conserta, testa de novo". Depois disso o retorno de informação nova cai bastante e é hora de fechar a versão.

### O caso Pathfinder, e o que dá pra copiar

A Paizo rodou playtest público do Pathfinder de março de 2008 a fevereiro de 2009: três liberações alpha em PDF e uma beta em PDF e impresso, mais de 45 mil downloads e mais de 100 mil posts no fórum.

A parte replicável não é a escala, é **a estrutura**: de setembro de 2008 a fevereiro de 2009, o beta foi testado em **blocos de duas semanas, cada um focado em um aspecto do jogo ou um capítulo do livro**.

**O que isso obriga:** a Guilda tem vários mestres e várias mesas rodando em paralelo. Isso é infraestrutura de playtest distribuído já montada. Adotar o formato de bloco — "estas duas semanas todo mundo testa e comenta *só* o combate", depois "só a progressão" — transforma retorno espalhado em dado organizado por tema, que é exatamente o que permite priorizar o que mexer primeiro.

---

## 6. Como se ensina uma regra

Referência principal: os livros de Ironsworn (Shawn Tomkin, ouro no ENNIE 2019 de Melhor Jogo/Produto Gratuito), que aparecem com frequência nas conversas de design como referência de estrutura e navegabilidade.

O que eles fazem de diferente:

- **Um quick-start de 32 páginas na frente do livro.** O jogo se torna jogável antes da página 33.
- **O livro diz para que serve cada capítulo.** Frases como "este capítulo é para consulta, não para ler de cabo a rabo" dirigem a atenção em vez de deixar o leitor adivinhar.
- **Mostrar em vez de contar.** Diagramas, exemplos, ícones e fluxogramas fazem o trabalho pesado. O esforço de design foi para material visual que *ensina*, não para diagramação bonita.

**O que isso obriga:** a estrutura do nosso material está decidida por essa referência — quick-start jogável na frente, referência completa atrás, e cada seção declarando se é para ler ou para consultar. Isso vai virar requisito da skill de redação na Fase 6, não decisão de última hora na diagramação.

---

## 7. IP e licenciamento

Decisão já tomada no pitch: material de fã, gratuito, sem venda. O que a pesquisa acrescenta em termos práticos:

- **Mecânica não tem copyright; texto e marca têm.** Dá para estudar qualquer sistema e usar a ideia — o que não dá é copiar redação de regra ou usar nome registrado como se fosse seu. Referência é inspiração, não recorte.
- Jujutsu Kaisen não tem licença aberta equivalente à OGL ou à ORC. Não existe rota legal formal para um derivado comercial. Por isso "gratuito" não é modéstia, é a condição.
**O que isso obriga:** crédito visível à obra original e declaração de trabalho de fã sem vínculo, em todas as versões do material desde a v0.1 — não só na final. Distribuição sem cobrança em nenhuma etapa e sem financiamento coletivo. E uma consequência que costuma pegar de surpresa: se um dia a Guilda quiser publicar de verdade, o custo do reskin é proporcional a quanto termo de JJK está entranhado no texto de regra. Vale manter os termos do sistema separáveis dos termos da ficção mesmo agora, sem virar obsessão.

Não sou advogado e isso não é orientação jurídica — é a leitura de risco prático com que a comunidade de RPG opera.

---

## 8. O que a pesquisa obriga no esqueleto

Consolidando. Estas são as travas que a Fase 3 herda:

1. **Progressão não pode ser negociável.** Tabela, relógio ou gatilho — nunca "o mestre decide quanto".
2. **Progressão precisa ter teto.** Sem bounded accuracy, mestre nenhum consegue escrever encontro sem ver a ficha.
3. **A escolha da curva de dado e a política de bônus são uma decisão só.** Sino sem controle de modificador = cinco mesas com dificuldades diferentes.
4. **Duas famílias de mecânica têm teto natural e entram na Fase 4 como favoritas a bater:** pool de dados (o 8º dado quase não rende nada) e escada de tamanho de dado à la Fabula Ultima (não existe "acumular +17"). Entre as duas, o pool leva vantagem num ponto específico do nosso caso: a qualidade do sucesso escala enquanto a chance satura, que é a curva de sensação shounen. Nenhuma das duas está escolhida.
5. **Rolagem precisa de gatilho de ficção**, não de decisão discricionária do mestre.
6. **Downtime precisa de regra**, porque o RP por texto da Guilda já é downtime acontecendo sem sistema.
7. **A lista de premissas herdadas de D&D precisa ser questionada uma a uma e por escrito**, ou a gente entrega um heartbreaker de shounen sem perceber.
8. **O material nasce com quick-start na frente.** Isso é requisito de estrutura, não de diagramação.

   > **⚠ O FORMATO desta trava foi abandonado na v0.102, e a pergunta que sobrou FECHOU na v0.103.** *Decisão do Mizuki na v0.102: `"pode abandonar a ideia do quick start, eu tô fazendo o PDF direto"`.* **O que este item pede não é um arquivo separado — é que alguém consiga jogar antes de ler tudo.**
   >
   > ***Decisão do Mizuki na v0.103: a pergunta sai da lista do projeto.*** *`"vamos finalizando as informações e mandando pro outro repositório o necessário para fazer o PDF, eu já tô no processo de estudo sobre"`.* **Como o PDF carrega essa propriedade é trabalho dele, e não pendência do repositório** — o que o repositório faz é mandar o material para a entrega. **A pesquisa fica escrita como está: ela é o levantamento, e não a decisão.**
9. **O playtest é 5 pessoas × 3 rodadas, em blocos temáticos de duas semanas**, aproveitando as mesas paralelas da Guilda.
10. **Precisa existir um guia do mestre com a matemática exposta** — conta de encontro, ritmo de recompensa, regra de morte — ou a consistência entre mesas não sobrevive ao terceiro mestre.

---

## Fontes

**Frameworks de design**

- [GNS theory — Wikipedia](https://en.wikipedia.org/wiki/GNS_theory)
- [Ron Edwards (game designer) — Wikipedia](https://en.wikipedia.org/wiki/Ron_Edwards_(game_designer))
- [Simulationism Was Real: GNS Theory Twenty Years On — The RPG Gazette](https://therpggazette.wordpress.com/2026/05/12/simulationism-was-real-gns-theory-twenty-years-on/)
- [MDA framework — Wikipedia](https://en.wikipedia.org/wiki/MDA_framework)
- [MDA for Tabletop Adventure Games — Aboleth Overlords](https://aboleth-overlords.com/2024/04/17/mda-for-tabletop-adventure-games/)
- [Does the MDA Framework Apply to Tabletop RPGs? — Sam Sorensen](https://samsorensen.blot.im/does-the-mda-framework-apply-to-tabletop-rpgs)

**Espaço de design**

- [Fantasy heartbreaker — RPG Museum](https://rpgmuseum.fandom.com/wiki/Fantasy_heartbreaker)
- ["Fantasy Heartbreakers" by Ron Edwards: A Retrospective](https://wordsongames.bearblog.dev/fantasy-heartbreakers-by-ron-edwards-a-retrospective/)
- [Powered by the Apocalypse — Wikipedia](https://en.wikipedia.org/wiki/Powered_by_the_Apocalypse)
- [Forged in the Dark compared to Powered by the Apocalypse — RPG.net](https://forum.rpg.net/index.php?threads%2Fforged-in-the-dark-compared-to-powered-by-the-apocalypse.917759%2F=)
- [Fabula Ultima — Wikipedia](https://en.wikipedia.org/wiki/Fabula_Ultima)

**Mundo compartilhado e múltiplos mestres**

- [Running West Marches — Practical Guide](https://www.westmarches.games/guide/running-west-marches)
- [What is a West Marches Campaign?](https://www.westmarches.games/guide/what-is-west-marches)
- [Pathfinder Society — Organized Play, Paizo](https://paizo.com/pathfinderSociety)
- [D&D Adventurers League — Wikipedia](https://en.wikipedia.org/wiki/D%26D_Adventurers_League)

**Matemática de dado**

- [dice-calc — PyPI](https://pypi.org/project/dice-calc/)
- [AnyDice](https://anydice.com)
- [Understanding Bounded Accuracy — D&D Wiki](https://www.dandwiki.com/wiki/Understanding_Bounded_Accuracy_(5e_Guideline))
- [Explain Bounded Accuracy to Me — EN World](https://www.enworld.org/threads/explain-bounded-accuracy-to-me-as-if-i-was-five.703031/)

**Playtest**

- [Playtesting your Tabletop RPG — Storybrewers Roleplaying](https://storybrewersroleplaying.com/2019/11/25/playtesting-your-tabletop-rpg/)
- [Tissue Testing — Eastshade Studios](https://eastshade.com/tissue-testing/)
- [The 3 stages of playtesting: Internal, Local, and Blind — BackerKit](https://www.backerkit.com/blog/tabletop-games-crowdfunding-roadmap/playtest/the-3-stages-of-playtesting-internal-local-and-blind/)
- [Why You Only Need to Test with 5 Users — Nielsen Norman Group](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/)
- [Pathfinder RPG playtest — PathfinderWiki](https://pathfinderwiki.com/wiki/Pathfinder_RPG_playtest)

**Redação e estrutura de manual**

- [Your RPG rulebook should begin with a 32-page quick-start in the front](https://jacke.substack.com/p/your-rpg-rulebook-should-begin-with)
- [Ironsworn — Shawn Tomkin, itch.io](https://shawn-tomkin.itch.io/ironsworn)
