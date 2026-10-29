# 14 — Análise de cobertura do Guia do Mestre pré-1.0

Feita em 28/10/2026, sem agente. Complementa a [comparação 97](<../04 - Planejamento/97-comparacao-critica-com-guias-de-mestre.md>), que olhou **como o livro ensina** (entrada, exemplos, inspiração). Esta olha **que assuntos ele cobre**.

## Método e limites
- **Nosso guia:** as 106 fontes de `06 - Redacao do Guia/` em 28/10, depois das revisões 112 a 117. Não usei o PDF, que é de 28/10 às 9h59 e está atrás das fontes.
- **Outros livros, 11 ao todo, todos no HD:**
  - DMG 2014 (PT) e DMG 2024;
  - Livro Básico do Pathfinder 2e;
  - Tasha;
  - GURPS 4e (PT);
  - Livro Básico do Fabula Ultima (PT);
  - SRD 2.0 do Daggerheart;
  - Warden's Guide do Cairn 2e;
  - Fate Core;
  - Livro I do Old Dragon 2;
  - Quick-Start do Call of Cthulhu.
- **Como contei:** listei 45 assuntos que guias de mestre costumam tratar e contei quantas vezes as palavras-chave de cada assunto aparecem em cada livro, em português e em inglês. Script e saída em `scratchpad/matriz.py` desta sessão. Todo zero do nosso guia foi conferido de novo com sinônimos do nosso vocabulário, porque o guia diz "pessoas" e não "NPC", por exemplo.
- **O que a contagem não mede:** qualidade. Ela mostra se o assunto aparece, não se é bem tratado. Número alto em livro grande (GURPS, PF2) pesa menos. O DMG 2024 tem OCR ruim e conta a menos.

## 1. O conteúdo atual
O guia tem 10 capítulos e 4 apêndices:

| Parte | Capítulos |
|---|---|
| Comece a mestrar | 1. Sua primeira missão · 2. O mundo dos feiticeiros · 3. Preparar aventuras · 4. Na mesa de jogo · 5. Criar uma campanha |
| Ferramentas | 6. Inimigos e perigos · 7. Personagens e técnicas · 8. Entre missões · 9. Pactos e entidades · 10. Jogar em guilda |
| Consulta | Apêndices A. Fichas · B. Exemplos completos · C. Termos · D. Inspirações da obra |

Os quatro caminhos de leitura estão no registro 99.

**Onde ele é forte.** Entre parênteses, quantas vezes as palavras-chave aparecem no nosso guia, em ~11 mil linhas:
- **Investigação e pistas** (155 de "investigação"/"pistas"). Bate o DMG 2014 (41) e só perde pro CoC, que é um jogo de investigação.
- **Quando rolar e dificuldade** (227). Está no nível do DMG.
- **Derrota, retirada e socorro** (167 de "derrota/rendição"; 128 de "retirada"). Só o Daggerheart tem mais.
- **Campanha, arcos e encerramento** (206). Facções (38), no nível do DMG 2014.
- **Pessoas do mundo e interpretação:** 384 "pessoas", 73 "interpreta", 26 de voz e jeito de falar.
- **Segurança e limites da mesa** (50, com o vocabulário próprio). Sessão zero (10) aparece mais que no DMG 2024 (6).
- **Guilda e vários mestres** (153 de "passagem/outro mestre") e **retorno depois da sessão** (62). Esses eram pontos fracos na pesquisa (P18 e P19) e o guia já cobre.
- **Mesa online** (20) e **regras opcionais** (38).

## 2. O que os outros livros cobrem
O que cada livro tem de marcante, pelos sumários e pela contagem:

| Livro | O que tem de marcante |
|---|---|
| DMG 2014 (PT) | "Conheça seus jogadores" (p. 6); "Regras da Mesa" e "O Papel dos Dados" (cap. 8); **Oficina do Mestre** (cap. 9: criar monstro, magia, item, opções de personagem e regras opcionais); tabelas aleatórias; masmorras e ambientes; estilos de fantasia |
| DMG 2024 | Sessão zero, preparo de sessão, exemplo de jogo, bastiões (base do grupo), glossário |
| Pathfinder 2e | Ferramentas de segurança, orçamento de ameaça, ajuste pro tamanho do grupo |
| Tasha | Sessão zero, patronos de grupo, enigmas, perigos ambientais, Ferramentas do Mestre (p. 137) |
| GURPS 4e | Como conduzir combate, tamanho do grupo, regras opcionais, campanhas |
| Fabula Ultima | Vilões e Pontos de Ultima, os "Pilares" do gênero (tom), itens raros, como montar batalha e NPC |
| Daggerheart | Holofote (é mecânica do jogo), derrota e morte com opções, "campaign frames" (pacote de cenário com regras próprias) |
| Cairn | Criação de mundo, facções, tabelas combináveis |
| Fate | Quando rolar, cenas, personagens do mestre |
| Old Dragon 2 | Armadilhas, XP, o capítulo "Mestrando" (p. 136) |
| Call of Cthulhu | Investigação e horror |

## 3. Comparação: o que ainda falta
Os números são as aparições no nosso guia, já com os sinônimos.

### Prioridade alta
| # | Assunto | No nosso guia | Quem faz bem | Material que já temos |
|---|---|---|---|---|
| 1 | **Tom e estilo da campanha.** Ajudar a mesa a escolher entre horror de mistério, ação de batalha e drama do cotidiano, e ajustar as regras e os inimigos a cada um | 4 aparições de "tom/estilo"; 1 de "proposta de jogo" | Fabula Ultima (os Pilares de cada Atlas), DMG 2014 (estilos de fantasia) | Mestragem 08 (Pilares do FU); Inimigos 19 (horror) |
| 2 | **Conduzir horror e medo.** Atmosfera, revelação aos poucos, maldição que só cai entendendo a regra. JJK é horror | 6 de "horror/medo"; 12 de "atmosfera/tensão" | Call of Cthulhu, Delta Green | Inimigos 19, inteiro |
| 3 | **Jogador difícil, ausente, calado ou que domina, e personagem novo entrando no meio da campanha.** Pesa mais numa guilda de mesa rotativa | 0 de "jogador difícil/ausente"; 2 de "personagem novo" (a participação em si tem 62) | Daggerheart (holofote), DMG 2024 | Mestragem 04 (holofote e jogador problema); Mestragem 11 (mesa aberta) |
| 4 | **Tamanho do grupo.** Escalar o encontro pra 2 ou pra 6 jogadores, e jogar com um jogador só | 1 aparição | Pathfinder 2e, GURPS | Nenhum relatório dedicado. **Exige conta no sistema, não pesquisa** |

### Prioridade média
| # | Assunto | No nosso guia | Quem faz bem | Material que já temos |
|---|---|---|---|---|
| 5 | **Regras da mesa.** Rolar escondido ou aberto, regra da casa, discussão de regra no meio da sessão ("decida agora, reveja depois") | 2 aparições | DMG 2014 (cap. 8), DMG 2024 | Mestragem 01 (princípios OSR) |
| 6 | **Tabelas roláveis de inspiração.** O registro 104 já trouxe listas de situações, pessoas, lugares e complicações, mas sem dado. A comparação 97 já pediu "um conjunto enxuto de inspiração" | 3 rolagens em tabela | DMG 2014, Cairn, WWN | Folhas do Old Dragon (rumores); Cairn |
| 7 | **O que cada jogador gosta.** Combate, drama, exploração, otimização, e como servir cada um | 5 aparições | DMG 2014 ("Conheça seus jogadores"), Robin's Laws | Mestragem 01 |

### Prioridade baixa
| # | Assunto | No nosso guia | Quem faz bem | Material que já temos |
|---|---|---|---|---|
| 8 | **Enigmas.** Barreira com condição, regra de maldição que funciona como charada | 0 | Tasha, DMG | Inimigos 19 (regra da maldição) |
| 9 | **Cansaço do mestre** | 2 | — | Mestragem 04 (artigo da Magpie sobre burnout) |

### Pra criação do sistema (Bestiário e Guia de criação)
A "Oficina do Mestre" do DMG 2014 (cap. 9) serve de mapa do que um livro de apoio à criação costuma ter. A comparação com o que já pesquisamos:

| Parte da Oficina | Pesquisa que temos | Falta |
|---|---|---|
| Criar monstro | Inimigos 05, 08, 11, 13 e 19 | — |
| Criar magia / técnica | Inimigos 07, 15, 16, 17 e 18, mais a lista "o que quebra uma técnica" | — |
| Criar item | Inimigos 06 e 03 | Itens **com vontade própria** (o DMG 2014 tem itens inteligentes na p. 215 e artefatos na p. 220). Combina com ferramenta amaldiçoada |
| Criar opção de personagem | Nada dedicado | **Lacuna.** Como os livros ensinam a criar Origem, Caminho ou classe nova sem quebrar as que já existem. O Homebrew Kit do Daggerheart, que já está baixado, trata disso e não foi analisado com esse foco |
| Regras opcionais / ajustes | Aparece espalhado | Ajustes da mesa (as "dials"), como "campaign frames" do Daggerheart e "Pilares" do Fabula Ultima: um pacote de regras que muda o tom da campanha. Conversa com o item 1 |

### O que eu não acrescentaria
Concordo com a comparação 97:
- não copiar a cosmologia do D&D;
- não criar um sistema de administração de facções;
- não pôr o catálogo de monstros no Guia, porque ele é do Bestiário.

Viagem e exploração aparecem pouco no nosso guia (14), mas as missões são urbanas, então não vejo lacuna aí.

## Resumo
- **O guia já cobre** o núcleo de um guia de mestre, e em investigação, derrota e guilda está acima da média dos livros comparados.
- **O que falta:**
  - tom e horror, que dependem do gênero de JJK;
  - o que fazer com jogadores difíceis e com o tamanho variável do grupo, que pesam na guilda;
  - regras da mesa e tabelas roláveis.
- **Pro Guia de criação:** o que falta é ensinar a criar opção de personagem e a montar "pacotes de tom" com regras próprias.
- **Pesquisa nova:** quase tudo já tem material nas duas pastas de pesquisa. A única pesquisa nova que vale é criar opção de personagem, a partir do Homebrew Kit do Daggerheart que já está no HD. O tamanho do grupo pede conta no sistema, não pesquisa.
