# Comunidade BR — segunda tentativa (21/10/2026)

> **Nota de 21/10/2026:** o Fabula Ultima em PT pela Jambô **existe e está confirmado** pelos próprios PDFs em `05 - Fabula Ultima (JRPG)`: créditos da Jambô, tradução de Marcel Reis, 1ª edição de nov/2025, ISBN 978-85-8365-158-1 no Livro Básico. Onde este relatório diz que não confirmou, vale esta nota.

Complementa a seção 2 do 04. Não repete o que já está lá. Orçamento: ~20 buscas/fetches.

## 0) Portas tentadas (o que abriu e o que não)
- `old.reddit.com/r/rpg_brasil/search.json` → **302 pro login** (Reddit agora exige login até no old.reddit pra .json).
- `www.reddit.com/.../search.json` → **403**.
- Pullpush (`api.pullpush.io`) → **429** de novo.
- WebSearch com `site:reddit.com/r/rpg_brasil` → **zero thread do Reddit** (o buscador não indexa o sub).
- Bluesky API pública (`public.api.bsky.app ... searchPosts`) → **403**.
- Conclusão: Reddit e Bluesky continuam fechados por esta via. Só com navegador logado.
- **Porta que funcionou: API REST do WordPress** (`/wp-json/wp/v2/posts?search=...`). Abriu no RPGista e no Joga o D20. Movimento RPG, Dados & Dragões e olddragon.com.br não respondem JSON (bloqueado ou não é WP). **Mundos Colidem morreu**: o domínio virou blog de finanças/SEO.

## 1) O que mestres e jogadores BR elogiam e criticam num mestre
- **Não achei fonte BR nova com opinião de comunidade** sobre isso. A busca por "mestre ruim / mau mestre" só devolveu coluna em inglês (RPG.net, Character Class #6, sobre railroading) e o código da MesaQuest.
- O que dá pra tirar, sem inventar: o **código da MesaQuest** (seção 4) é o retrato mais concreto do que o mercado BR cobra do mestre — avisar antes de cancelar, tratar a mesa com seriedade, não humilhar novato, usar ferramenta de segurança. É regra de plataforma, não pesquisa de opinião.
- Somado ao 04 (RPGista 2019, "mestre refém da regra"), o quadro BR continua com **duas fontes de opinião e nenhuma de volume**.

## 2) O que dizem dos guias de mestre (T20, OP, OD2, Fabula Ultima PT)
- **Tormenta 20 — Resenha do RPGista** (Moisés Mota com Vrikolaka, 03/02/2021, lida): cap. 6 tratado como útil pra veterano e iniciante, com "recursos para agilizar decisões"; elogia a regra de **aliados** (simples) e as **tabelas de entre aventuras**. Capítulo de ameaças: fichas de antagonista "bastante simplificadas"; monstros bem mais fortes que no Tormenta RPG antigo porque o livro sugere **no máximo dois encontros por dia** — o resenhista acha ok e lembra que o mestre pode ajustar. O próprio livro recomenda deixar **poderes gerais de fora no começo** pra não perder novato; alerta de **Métodos de Experiência** que podem ser excludentes entre jogadores. **Nenhuma crítica direta ao cap. 6.** Nos comentários, um leitor (Cainã Morellato, dez/2021) acha a regra de descanso arbitrária e burocrática; o resto do debate é sobre raças. Uma resenha, um site — **opinião isolada**, mas é a segunda fonte a chamar o cap. 6 de completo (a outra é o Rotina de Mestre, no 04).
  https://rpgista.com.br/2021/02/03/resenha-do-tormenta-20/
- **Ordem Paranormal — STATUS MUDOU: 2ª edição anunciada** por Cellbit na live "Segredos Revelados" (YouTube, 29/08/2026; matéria do Joga o D20 de 03/09/2026, lida). Jogo "completamente novo": atributo e perícia viram dado (d4–d12, atributo até d20), soma dos dois, DT padrão 7 no playtest. **A investigação foi refeita** — a matéria chama a da 1ª edição de "principal problema" (é o enquadramento do site; não achei a frase atribuída ao Cellbit): **Pontos de Interesse** listados pelo mestre na cena, ações Investigar/Examinar/Interagir, busca infrutífera custa **Pontos de Determinação**, Dano Mental em excesso mata. Playtest público (Ato I grátis; Ato II só pra assinante do Arquivos Secretos). Editora não escrita (o link leva à Jambô). Sem data e sem nada sobre livro do mestre. **Consequência pro catálogo:** o que o 04 descreve da investigação da OP (teste estendido, ficha de investigação) é da 1ª edição e vai ser substituído.
  https://jogaod20.com/2026/09/03/ordem-paranormal-rpg-2e/
- **Fabula Ultima em PT pela Jambô (2025): não confirmei que exista.** Duas buscas (PT e PT+2025) só trouxeram a edição em inglês (Need Games, 2023, ENNIE) e o Kickstarter da Celebration Edition (out/2025, BoLS). Não citar a edição brasileira no Guia sem conferir no site da Jambô.
  https://www.belloflostsouls.net/2025/10/rpg-fabula-ultimas-celebration-edition-kickstarter-is-gonna-break-1-million-easily.html
- Ordem Paranormal, dica de mestre: busca devolveu só lista de episódio (Cellbit creditado como Mestre no TheTVDB) e PDF pirata em domínio spam. Opinião de comunidade: **nada**.

## 3) Dicas de mestragem que circulam muito na comunidade BR
- **Sessão zero / mini sessão zero** aparece como a dica de segurança mais repetida no material BR. **Igor Téuri (Dados Críticos)**, "Ferramentas de Segurança para RPG" (itch.io, grátis/pague quanto quiser, lido): coletânea, parte original e parte tradução/adaptação (créditos a Sly Flourish e Mike Shea, Kienna Shaw e Lauren Bryant-Monk etc.); traz **checklist de mini sessão zero de 15 min** que ele usa ao jogar online com desconhecidos, formulário de consentimento (readaptado 2021) e **macros de Roll20** pras ferramentas. É o mesmo Dados Críticos do servidor de Discord da seção 4.
  https://igorteuri.itch.io/ferramentas-de-seguranca-para-rpg
- **Mês de Mentoria para Mestrar (MMM)** — atualização do que está no 04. Post "O fim do Mês de Mentoria para Mestrar" (03/01/2025, lido via API do Substack): o título era clickbait, o programa **não acabou**, virou **AMMM (Advanced Mês de Mentoria para Mestrar)** em 2025 e **mudou de plataforma de newsletter** (o Substack ficou parado). Coisas de mesa BR que o próprio texto aponta: nasceu inspirado no **New Gamemaster Month** gringo, mas agora vai até **24 de fevereiro** (o texto diz ser a data do RPG no calendário nacional — não conferi); a comunidade roda em **grupo de WhatsApp** (já teve Telegram e Discord), "enquanto os gringos só usam o Discord"; tem "Festivais na Taverna", guias voluntários e podcast; ninguém é pago. Alcance no Substack é baixo (2–7 reações por post), então é movimento de nicho, não "o que circula muito".
  https://mesdementoriaparamestrar.substack.com/p/o-fim-do-mes-de-mentoria-para-mestrar
- **Mestre Pug** (mestrepug.substack.com, 2025): dicas de mestre em formato de guia (prospecto de campanha, masmorra de 5 salas, combate, horror, "verdades", metagame). Alcance baixo (2–6 reações), cara de SEO; serve pra mostrar que a dica gringa (5 salas, Sly Flourish) é o que se traduz e recircula, **não** como voz da comunidade. https://mestrepug.substack.com/p/um-guia-para-criar-um-prospecto-de
- Guia genérico BR de sessão 0 (digitei.com, não lido, cara de SEO): https://digitei.com/?p=67209

## 4) Específico de mesa BR (horário, Discord, online, mesa grande, streaming)
- **Mesa paga existe como mercado organizado no Brasil: MesaQuest.** Código de conduta (Elisinha, 15/12/2025, lido): o mestre "está gerenciando um negócio" e tem de manter comunicação com os jogadores como tal; cancelar sessão/campanha/one-shot **sem avisar** é conduta inaceitável; proíbe cobrar por fora da plataforma; não pode criticar jogador por inexperiência; ferramentas de segurança obrigatórias, pausar ou sair da mesa é direito; as regras valem também no **Discord do mestre**; três marcas = banimento. Regra de plataforma, não opinião da comunidade.
  https://intercom.help/mesaquestrpg/pt-BR/articles/12731889-codigo-de-conduta-do-mesaquest
  Outra página da ajuda diz que lá se acham "mesas de mestres e influenciadores do Brasil inteiro" (só título, não lido): https://intercom.help/mesaquestrpg/pt-BR/articles/12918378-e-verdade-que-no-mesaquest-eu-encontro-mesas-de-mestres-e-influenciadores-do-brasil-inteiro
- Servidores BR de achar mesa no Discord: **Império – RPG** e **Dados Críticos** (canais separados de procurar/oferecer mesa + dúvida de regra). Só a página de descoberta do Discord, não entrei.
  https://discord.com/servers/imperio-rpg-1012065638556119050 · https://discord.com/servers/dados-criticos-728447419632844811
- Legião dos Heróis, "10 dicas para jogar RPG de mesa online" (não lido ainda): https://www.legiaodosherois.com.br/lista/10-dicas-jogar-rpg-mesa-online.html
- **Efeito Mercer / mestre de stream:** só achei fonte em inglês (Wargamer). No Brasil o equivalente seria a mesa do Cellbit (Ordem Paranormal), mas **nenhuma fonte BR** falando disso apareceu. https://www.wargamer.com/dnd/dungeon-masters-problem-actual-play
- Preço de mestre pago por sessão: **não achei** (busca contamina com RPG de fisioterapia).

## 5) Buracos que continuam
- **Leitura geral:** a comunidade BR de mestragem vive em Discord, WhatsApp, YouTube e Reddit — tudo fora do alcance de busca sem login. O que é indexável é resenha velha (RPGista), notícia (Joga o D20), regra de plataforma (MesaQuest) e newsletter de nicho (MMM, Mestre Pug). **Não dá pra afirmar "a comunidade BR acha X" com o que está aberto.**
- Fabula Ultima PT (Jambô 2025): não confirmado.
- Old Dragon 2: nada novo além do 04 (site não responde à API; não gastei busca).
- Preço de mestre pago no Brasil: não achado.
- Pra fechar de verdade: navegador logado no r/rpg_brasil (buscar "mestre", "Livro do Mestre T20", "mesa online", "mestre pago") ou o Discord Dados Críticos/Império.
- Pista não lida: RPGista, "Guia de Sobrevivência Social: como não ser expulso do grupo de RPG" (14/02/2026) — etiqueta de jogador, pode ter o espelho do que se cobra do mestre. https://rpgista.com.br/2026/02/14/como-nao-ser-expulso-grupo-rpg-etiqueta/
- Pista não lida: Joga o D20, "Heart chega ao Brasil" (20/10/2026) e "Assimilação: Rakin rompe com a New Order" (09/10/2026) — mercado, não mestragem.
- Reddit, Bluesky, fórum da Jambô: fechados.
