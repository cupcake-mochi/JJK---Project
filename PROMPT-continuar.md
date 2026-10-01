# Prompt para continuar o Projeto - M em conversa nova

> **Continuidade de 29/09 — ordem mais recente de Mizuki:** o Git foi posto em dia — as v0.277 a v0.287 subiram num commit só, e a entrega como recorte da v0.287. O planejamento das Invocações virou o primeiro lote de desenvolvimento, que fica no HD, em `/media/mizuki/HD Externo II/Claude/invocacoes-pos46/`, e deu o §47 na v0.288 (o invocador apagado não derruba a sustentação), o §48 na v0.289 (quando ele morre, as entidades saem de campo), o §49 na v0.290 (cada entidade tem a própria ficha, e o limite é um teto de corpos), o §50 na v0.291 (uma básica por corpo por ciclo), o §51 na v0.292 (uma Bônus redireciona todas as entidades em campo, cada uma com a própria intenção de básica), o §52 na v0.293 (o limite de ataques por turno conta só a atuação com dano; a condição Média ou Pesada só vem de especial comandada), o §53 na v0.294 (a entidade só entra em campo no turno do invocador), o §54 na v0.295 (e só é recolhida no turno dele), o §55 na v0.296 (aparece colada no invocador, e na troca no lugar de quem sai), o §56 na v0.297 (a entrada e a troca custam a Ação Bônus), o §57 na v0.298 (o recolhimento também), o §58 na v0.299 (as manifestadas antes da luta começam em campo), o §59 na v0.300, fechado na v0.301 (a energia das especiais: do invocador, e da reserva própria de quem tem técnica, de 1 + ⅓ da Essência por nível, meio a meio) e o §60 na v0.302 (o conjunto rende até uma Rotina e meia por rodada, com preço), o §61 na v0.303 (a vida da entidade sai da fórmula de ficha, com 5 no nível 1 e 3 por nível, mais a Constituição), o §62 na v0.304 (sem supor Trilha, o teto de base é 2 entidades em campo), o §63 na v0.305 (o limite de base é 2, as duas atacam, e quem leva uma tem dano parelho com quem leva duas), o §64 na v0.306 (uma entidade completa até meia Rotina, e duas até dois terços), o §65 na v0.307 (a ficha da entidade é a da peça 15 antiga), o §66 na v0.308 (a Defesa com a metade do dono, e o traje no lugar), o §67 na v0.309 (cada entrada paga a Classe do nível da entidade em PE), o §68 na v0.310 (tudo que depende de nível segue o da entidade, até o do invocador), o §69 na v0.311 (a especial custa 3 × a Classe do nível da entidade, como um feitiço), o §70 na v0.312 (a manifestação dura até o fim da cena, e o fim do combate a encerra), o §71 na v0.313 (toda invocação exige uma troca para ser obtida, e o preço é a troca somada ao que já cobra), a correção dele e o §72 na v0.314 (o espaço dá a entidade no nível do invocador; a reserva recupera como o PE), o §73 na v0.315 (a morte definitiva, a volta com metade da vida, e a vaga da lista de ritual que se perde), o §74 na v0.316 (ficam `Desligada` o corpo amaldiçoado e a domada sem técnica). Em 29/09 o Mizuki mandou focar nas Invocações até terminar ("temos q terminar tudo de invocação"); a pergunta que espera o Mizuki é o que é um corpo `Desligada` — um objeto no campo que conta no teto e religa pela entrada, o mesmo sem contar no teto, ou o mesmo com a cura religando. Fichas de personagem ficam para depois.

*Copie tudo abaixo da linha.*

---

Trabalhe em `/media/mizuki/HD Externo II/Claude/Claude 2/`, na pasta **principal**.

**Projeto - M** é um sistema de RPG de mesa no universo de Jujutsu Kaisen, para um server de guilda com vários mestres ativos e personagem persistente entre mesas. O filtro que decide quase tudo: **dois mestres que nunca se falaram chegam no mesmo número?**

**A conversa anterior tinha três partes, e a primeira fechou na v0.270.** *O que falta, nesta ordem, e cada parte fecha a sua versão antes da seguinte:*

- ~~**A — os Caminhos novos no livro (v0.270).**~~ **FECHADA na v0.270**, *e as decisões que ela deixou fecharam na v0.271: a perícia fixa do Bastião é `Provocar`, a frase dos Limites voltou com o Socorrista como exceção, ninguém cura outra pessoa com Energia Reversa, e os renomes `Eco Amaldiçoado`, `Impulso Energético` e `Sobre Carregar Energia`, com o resto das colisões aprovado.*
- ~~**B — a rodada 3 dos anti-domínio.**~~ **FECHADA na v0.274:** *a `Pétala` na v0.272, a `Extensão de Domínio` na v0.273, e a comparação das quatro na v0.274 — nenhuma ficou dominada.*
- ~~**C — as Invocações, no ponto exato em que pararam.**~~ **FECHADA na v0.275:** *o §46 — a zero PV a invocação sai de campo, e a que o vínculo não deixa recolher fica `Desligada` — mora em `invocacoes/DECISOES-A-PARTIR-DO-46.md`.*
- ~~**Depois de C, a troca de nome no livro inteiro.**~~ **FECHADA na v0.276**, *com o `Calado` alinhado nas cinco cópias e o manual na v7.39. **A v0.283 fechou as duas pontas que ela deixou:** quem monta a técnica em `Manejo` ou em `Kata` não compra o Ritual, e a caixa da Extensão parou de dizer que a Técnica Marcial e as aptidões continuam.*
- **Agora, a fila grande do `sistema/ESTADO-ATUAL.md`**, *que o Mizuki deixou por último: "vamos continuar o 1, deixando a fila grande por ultimo". E ele pediu para emendar um item no outro sem perguntar — "sempre que finalizar pode ir automaticamente pro proximo" —, parando só em decisão dele e em commit.*

**Ao começar cada parte, diga em uma linha o modelo e o esforço que você recomenda para ela.**

## Regras da pasta, antes de tudo

- **Você não commita.** Deixa a mensagem pronta em `mensagem-de-commit.txt` na raiz e manda os comandos ao Mizuki, um por bloco; ele roda o `./subir.sh`, que confere os 31 validadores, commita e sobe, e depois commita a entrega à mão. *Git de leitura (`status`, `log`, `diff`) funciona daqui.*
- **Se a sessão abrir numa worktree** (uma pasta dentro de `.claude/worktrees`), a ferramenta de edição não escreve na pasta principal e a sessão não sai dela. **Edite na worktree e entregue por patch:** `git add -N` nos arquivos novos, `git diff --binary <commit do main> | git apply` da worktree para a principal (teste antes com `git apply --check`), e `cp` da `mensagem-de-commit.txt`, que é ignorada pelo git. **Antes de editar, confira que a worktree está no mesmo commit do `main`**; se estiver atrás, peça ao Mizuki para alinhar, ou gere o patch contra o commit do `main` — o `git reset --hard` pede permissão e pode ser negado.
- **Confirme a pasta:** `grep -c "^## Nove lições" README.md` tem que dar `1`. Se der `0`, é a pasta errada — pare. Existe um clone velho na home com a cara deste projeto.
- **⚠ Antes de puxar QUALQUER agente — um, dois ou três —, pergunte e espere**, dizendo quantos, o que cada um faz e quanto custa. É regra dura do arquivo de instruções da pasta de trabalho (um nível acima deste repositório), e vale mais que o ultracode; o teto é 2 a 3 por vez, e cada agente salva o próprio arquivo no HD ao longo do caminho.

---

# A ordem de tarefas

## Passo 0 — onde está

1. **Em 29/09/2026 o Git foi posto em dia:** as v0.277 a v0.287 subiram num commit só, com a entrega no *recorte da v0.287*, a v0.288 registrou o §47 das Invocações, a v0.289 o §48, a v0.290 o §49, a v0.291 o §50, a v0.292 o §51, a v0.293 o §52, a v0.294 o §53, a v0.295 o §54, a v0.296 o §55, a v0.297 o §56, a v0.298 o §57, a v0.299 o §58, a v0.300 o §59, a v0.301 o fechamento dele, a v0.302 o §60, a v0.303 o §61, a v0.304 o §62, a v0.305 o §63, a v0.306 o §64, a v0.307 o §65, a v0.308 o §66, a v0.309 o §67, a v0.310 o §68, a v0.311 o §69, a v0.312 o §70, a v0.313 o §71, a v0.314 a correção dele e o §72, , a v0.315 o §73 e a v0.316 o §74. **O `main` deve estar no commit da v0.316** ou mais novo, com a entrega no *recorte da v0.316*. *Se estiver abaixo, leia o `CHANGELOG` do disco antes de reaplicar qualquer coisa: o histórico das versões prontas mora na pasta agentes-2026-09-27 do HD.* **E rode `git worktree list` com um `git status` em cada worktree:** *versão pronta pode estar parada numa worktree sem ter subido. Em 28/09 a conversa nova leu o `main` na v0.275 e perguntou de novo o que a v0.276 e a v0.277 já tinham decidido, porque as sete versões estavam só na worktree `quirky-wiles`.* *A v0.272, a v0.273 e a v0.274 foram commitadas em 27/09, mas o push falhou: o GitHub CLI estava com a conta `Gustavo-MrTs` ativa, e não a `cupcake-mochi`. Se `git status` disser que o `main` está à frente do `origin`, o push ainda não saiu — lembre o Mizuki, porque trocar a conta é com ele.* Rode `git log -3` e `git status` na pasta principal antes de qualquer coisa. *Se houver commit mais novo, leia a entrada dele no `CHANGELOG` antes de seguir.*
2. **Rode a skill `rpg-da-guilda`.**
3. **Leia `sistema/ESTADO-ATUAL.md` inteiro**, inclusive a fila no fim — ele trunca, e se vier aviso de leitura parcial, continue do offset —, e o `README.md`, que tem as **nove lições que custaram erro**.

## Parte A — FECHADA na v0.270

**Os quatro Caminhos da coleção v0.4 estão no capítulo 8, e o Evocador e as Invocações saíram da edição jogável.** *A coleção mora em `caminhos/` e é a dona do texto; os `DESENHO-*.md` e a peça 17 ficaram como o registro com preço da coleção anterior; o desenvolvimento das Invocações e o texto que saiu do livro moram em `invocacoes/`.* **O equilíbrio da v0.4 não foi medido, e a medição está na fila (item 12).** *O que mudou, o que foi conferido e o que ficou para o Mizuki decidir estão na entrada da v0.270 do `CHANGELOG`.*

## Parte B — a rodada 3 dos anti-domínio, continuando

**Mesmo método das rodadas 2 e 3.** *O registro está em `logs/SESSAO-2026-09-24-anti-dominios.md` e nas entradas da v0.265 à v0.269 do `CHANGELOG`; a obra está no `sistema/01-pesquisa/anti-dominios/H-resumo-das-quatro.md`; a regra, na peça 11 §6.5; e o molde da conta é o `conta-dominio-simples.py`, na mesma pasta do `H`.* O que se mede é o que o Mizuki pediu: **como cai, quanto dura, o que dá, o que não dá, e o que custa.**

1. **Mostre, curto, o que a peça 11 diz hoje e o que a obra diz** — o `H` tem a obra, com a marca de evidência (`[C]` cânone, `[F]` oficial, `[I]` inferência). **Antes de oferecer agente, procure nos arquivos `A` a `N`.**
2. **Liste as perguntas de desenho, numeradas.** O Mizuki responde no formato "1 - … 2 - …".
3. **Meça antes de perguntar**, num script irmão na mesma pasta, com o mesmo contrato: **a regressão reproduz os números publicados antes de medir coisa nova**, probabilidade exata e não Monte Carlo, e âncora lida da peça dona. *O `conta-cesta-oca.py` já reproduz a Pétala de hoje (o `R3` dele).*
4. **Traga as opções com o número e o trade-off já calculados, com um exemplo concreto de cada uma**, e o Mizuki decide. *Ele também propõe fórmula — foi a dele que ficou no Simples. Meça a dele nas leituras possíveis e diga qual leitura você aplicou.*
5. **Aplique como versão nova**, pela ordem de fechar versão lá embaixo.

### ~~A Pétala, primeiro~~ — FECHADA na v0.272

**Ela rebate o que toca, e o dano do Acerto sai da Essência contra a do dono** (maior anula, igual leva `1/4`, menor leva metade); *o que a Expansão traz por contato e não é dano ela anula sempre; cai pelo teste do `Carregar` a cada golpe, de qualquer um, sem a queda na hora; com arma empunhada contra-ataca por `3` PE; `1` PE por rodada.* **E erguer a Cesta, o Simples ou a Pétala custa a maior Classe, toda vez.** *O porquê, as palavras dele e as leituras aplicadas estão na entrada da v0.272 do `CHANGELOG`; a pesquisa, no `O-petala-as-perguntas-da-rodada-3.md`; a conta, no `conta-petala.py`.*

### ~~A Extensão de Domínio~~ — FECHADA na v0.273

**Quem a usa fica imune a tudo o que a Expansão faz, em qualquer degrau**; *a técnica que encosta nela é anulada até `1/3 do refino + 1`, e acima disso você leva `3/4`; não cai por golpe; erguer paga a maior Classe; nível 18 com requisito de história; o Corpo Amaldiçoado não compra.* **Com ela de pé você não usa feitiço nem `Manejo`**; *a reversa e as aptidões continuam, "por enquanto", e desde a v0.283 a caixa não escreve o que continua.* *As palavras dele e as leituras estão na entrada da v0.273 do `CHANGELOG`; a pesquisa, no `P-extensao-o-que-ficou-aberto.md`; a conta, no `conta-extensao.py`.* **O que é leitura nossa não vai para o livro** *— "informação que o player n precisa".*

### ~~A comparação das quatro~~ — FECHADA na v0.274

**Nenhuma ficou dominada.** *A Cesta é a mais barata e a que mais segura sozinha com Essência `4` ou mais; o Simples não cai por golpe e cobre o grupo; a Pétala, com Essência maior que a do dono, não deixa passar nada; a Extensão nunca deixa, e é a única contra a incompleta.* **Quando a Cesta cai, ou o Simples cai pelo voto, o Acerto que alcança na hora é a mais** *— "chegando no começo do turno do inimigo vc vai receber novamente".* *A tabela está na peça 11 §6.5, em "As quatro lado a lado"; a conta, no `conta-as-quatro.py`; o arredondamento da Extensão no bestiário fechou junto.*

## ~~Parte C — as Invocações, no ponto do zero PV~~ — FECHADA na v0.275

**O §46 foi aprovado — "1 - A", "2 - A - Desligada" — e está em `invocacoes/DECISOES-A-PARTIR-DO-46.md`**, *ao lado do pacote, que continua como chegou. O que segue abaixo é o registro de como a parte foi aberta.*

**Estado:** *o subsistema está na **v0.3 CANDIDATA, revisão 5, decisões até o §45**, com 212 verificações simbólicas aprovadas (178 anteriores e 34 novas), **sem prova de equilíbrio e sem playtest humano**.* **As decisões não precisam ser aprovadas de novo.**

**Onde ler:** *em `invocacoes/03-INVOCACOES/`:* **00-REGISTRO-E-PONTO-DE-RETOMADA.md**, **ATUAL-r5/01-PROCEDIMENTOS-DE-CAMPO-v0.3-CANDIDATA-r5.md** e **ATUAL-r5/03-PENDENCIAS-E-CONFLITOS.md**. *O REGISTRO-DA-CONTINUIDADE/ e as pesquisas servem para uma dúvida específica, não para leitura inteira.*

**O que vale sem discussão:**
- **Primeiro o subsistema de Invocações; o Evocador e as Trilhas dele vêm depois.**
- **Customização completa, e as fantasias de entidade singular, parceria e pequeno conjunto de entidades distintas, são diretrizes** — *não fichas nem limites numéricos aprovados.*
- **Energia própria das entidades e custo de substituição continuam pendentes.**
- **Não crie construtor, catálogo, preço, orçamento, `X`, alcance, PE, PV, dano ou progressão para preencher lacuna.**

**O ponto exato de parada:** *a próxima discussão era a consequência imediata de uma invocação chegar a zero PV.* **O §22 aprovou a equivalência entre campo e reserva, mas não escolheu entre dissipar, ficar inconsciente, ser destruída ou se recuperar.** *Foi recomendado que ela saia do campo a zero PV, encerrando ordens e preparações pela saída, sem devolução nem cura automática.* **O Mizuki ainda não aprovou essa recomendação:** *não crie o §46 nem aplique a proposta como regra.*

**Como retomar:** mostre o resultado das Partes A e B em poucas linhas, e depois **retome só esse ponto**, explicando por que a regra que existe não o resolve. *Não reabra questão aprovada.* **Uma decisão nova de verdade ganha número a partir do §46 só depois da aprovação do Mizuki.**

## Depois da Parte C, na ordem dele

*"Depois vamos para a 2-3-4": as Invocações (fechadas na v0.275), os pendentes pequenos logo abaixo, e a troca de nome valendo no livro inteiro — e "deixando a fila grande por último".*

~~**A troca de nome no livro inteiro — DECIDIDA, falta aplicar.**~~ **APLICADA na v0.276**, *com o "leia também", a exceção do Restringido e o `Calado` da `Kata` ("Só se seguir os mesmos padrões, algumas ferramentas podem necessitar som"); o registro de antes fica abaixo.* *Hoje o capítulo 43 manda ler `Manejo` onde os capítulos 8 e 9 escrevem feitiço, e o 42 manda ler `Kata` nos mesmos dois; o resto do livro também escreve feitiço — a Cesta ("nada de feitiço com `Gesto`"), o teto da Extensão, o turno, dano e condições, o ritual, a experiência —, e pela letra nada disso alcança o Sem Técnica nem a Técnica Marcial.* **A decisão:** *"A" — a frase dos capítulos 42 e 43 passa a "onde o livro escreve feitiço, leia `Manejo`/`Kata`". E nas palavras dele: "antes o plano era impedir restringido e sem técnica de usar emanador, mas agora n tem o pq impedir".* **A peça 25 já diz que o `Manejo` "é o feitiço com outro nome"**, *então a versão alinha o livro com a peça. A checagem 13 do `conferir-sem-tecnica.py` lê a frase do capítulo 43, e a do capítulo 42, a mesma checagem no `conferir-marcial.py`.*

**A fila grande começou pelo item 12, e ele fechou na v0.281** *sem medir o resto — o Mizuki achou a conta inflada: "você está calculando cogitando muitas coisas, n precisa tanto". O piloto do Bastião e a leitura dos outros três Caminhos estão em `sistema/01-pesquisa/medicao-v04/`; a sobra do 12, o índice de entregas da v0.4, virou o item 17.* **O item 8 fechou na v0.282, como a fase 2 do bestiário:** *a escada de inimigos virou a grade de dificuldade por `×1` a `×6` pessoas, com as decisões e as contas em `bestiario/09-fase-2/`. As sobras dele são os itens 18 (o Sukuna na grade) e 19 (as onze divergências da auditoria).* **O item 19 recebeu a decisão sobre o Evocador em 28/09/2026:** "remove, porque não temos evocador". A v0.285 retira o Caminho suspenso da média que calibra o dano dos inimigos; a média agora usa Bastião, Vanguarda, Guia e Emanador. Não pergunte isso de novo. **Resistência pontual aprovada na v0.286:** até dois tipos fixos no total da criatura não descontam PV. Grupos completos continuam cobrados, mesmo escritos separadamente. Imunidades não recebem a isenção; três ou mais tipos mistos sem completar grupo seguem pendentes. Não reabra a decisão. No item 18, PV-base foi aprovado como referência de cura e partes destrutíveis, antes dos ajustes e mantendo frações até o resultado. Não reabrir essa escolha. Sukuna integrado na v0.287. A ordem recente é planejamento das Invocações para Claude antes das fichas; o índice v0.4 continua na fila.

## Pendentes pequenos, fora das três partes

- **O balão do cap. 246 no vol. 28** — quem tiver o volume confere se o `薄める` virou `弱める`. *O dado que existe foi lido contornando a proteção do leitor da Shueisha e voltou a **não conferido**; não repita esse caminho.*
- **O repositório da ficha (`Claude 3`) tem o texto velho das quatro anti-domínio** até a próxima extração do livro — *e, depois da Parte A, os Caminhos velhos também.*
- **A nota de pesquisa do bestiário que cita o raio de 2,21 m fica como está** — é nota de campo.

---

# O contexto que você precisa

## Onde o projeto está

**v0.287.** Manual do Fundamento na **v7.41**. **Vinte e sete peças de regra e vinte e sete validadores** em `sistema/03-mecanica/`, mais o `conferir-repositorio.py`, os dois de `manual/matematica/` e o `conferir-voz.py` — **31 validadores**. O livro tem **18 capítulos**. A ficha (`Claude 3`, o `Ficha---RPG-JJK`) não mudou.

**A v0.264 e a v0.265 foram pesquisa** (`sistema/01-pesquisa/anti-dominios/`, arquivos `A` a `N`). **A v0.266 foi a rodada 1** (as frases da peça 11 que atribuíam à obra o que ela não faz). **A v0.267 foi a rodada 2, a Cesta**, e **a v0.268 e a v0.269, o começo da rodada 3, o Simples** — *a v0.269 trocou a regra de queda que a v0.268 tinha publicado.*

**Os Caminhos e as Invocações foram trabalhados fora desta pasta**, num chat que não a via, e voltaram por pacote na v0.270. *A coleção v0.4 dos Caminhos está no livro, em `caminhos/`; as Invocações estão na candidata r5, em `invocacoes/`, fora da edição jogável.*

## O que a pesquisa dos anti-domínio mudou

**A casca não é a variável — é a diferença de saída (`出力`) entre quem defende e quem abriu**, e o sistema tem a moeda para isso nos dois lados: o refino. *No Simples, por decisão do Mizuki, a moeda acabou sendo a Essência — a de quem segura contra a do dono —, e o refino ficou no raio e no gate.* **Nenhuma das quatro tem relógio próprio na obra: todas caem por fora.** **E o jeito de ceder muda de uma para outra:** a atenuação só tem cena na Extensão; a Cesta e o Simples protegem por inteiro até cair; a Pétala intercepta.

**Seis coisas a obra não amarra, e são desenho livre:** custo de energia, limite de tempo, Extensão junto com a técnica reversa, Cesta com encantamento próprio, quem usa a Pétala fora do Zenin e do Gojo, e como se aprende a Cesta.

## As quatro que já fecharam

**Erguer qualquer uma das quatro custa a maior Classe em PE, toda vez (v0.272 e v0.273).**

**A Cesta Oca (v0.267, a queda na v0.268, e o teste na v0.269):** as duas mãos presas no símbolo; levanta com Reação quando uma Expansão abre ou Ação Bônus no turno; cai pelos golpes em quem segura (**o teste do `Carregar`, Espírito contra a CD de quem feriu** — era Vigor até a v0.268 —, falhas até metade da Essência); **quando cai, a Expansão alcança na hora, e ela levanta de novo sem espera, gastando a Ação Bônus**; PE zero; requisito de história (Reencarnado, ou treinado em `História`).

**O Domínio Simples (v0.268, e a queda na v0.269):** **aguenta `3` rodadas de Expansão, `4` se a Essência de quem segura for maior que a do dono e `2` se for menor**; cada Acerto que ele segura gasta uma, a começar pelo de abrir, e pede **o teste do `Carregar`** — a falha tira uma rodada, nunca abaixo de metade da Essência; golpe no dono não o derruba; quando cai, a Expansão alcança na hora quem ele protegia, e **erguer de novo na mesma Expansão custa a Ação Padrão e aguenta metade** (mínimo 1). **Lá dentro a Expansão não alcança ninguém**, e o que ela dá ao dono continua. **Os pés são o voto do iniciante** (refino 4; com refino 5 ele anda com você), o gate é refino 5 sem nível, e o PE são `2` fixos. **Contra refino 10 nenhum Simples segura até o fim.** *O teste não tem nome próprio; se o Mizuki quiser um, os candidatos livres na triagem foram Sustentar, Tenacidade, Manter, Sustentação e Firmar.*

**A Pétala (v0.272):** rebate o que toca, energia contra energia; **o dano do Acerto que toca sai da Essência de quem a usa contra a do dono — maior, nada; igual, `1/4`; menor, metade** —, e o que a Expansão traz por contato e não é dano ela anula sempre; levanta com Reação quando uma Expansão abre ou Ação Bônus no turno, e erguer de novo custa a Ação Bônus; **cai pelo teste do `Carregar` a cada golpe, de qualquer um, com metade da Essência em falhas, e sem a queda na hora**; com arma corpo a corpo empunhada, contra-ataca quem a acertou com um ataque de oportunidade com vantagem, por `3` PE (o soco não conta); `1` PE por rodada; contra a incompleta não faz nada; requisito de história (Descendente, ou ter aprendido com alguém de um clã) e refino 4.

**A Extensão de Domínio (v0.273):** imune a tudo o que a Expansão faz — o Acerto e o que ela faz com as pessoas e com o lugar —, completa, incompleta ou sem barreiras; a barreira continua prendendo e o que a Expansão dá ao dono continua com ele; a técnica que encosta é anulada até `1/3 do refino + 1`, e acima disso você leva `3/4`; levanta como as outras, `1,5 × maior Classe` por rodada, dura `refino` rodadas, e não cai por golpe; com ela de pé, nenhum feitiço nem `Manejo` (a reversa e as aptidões continuam, e a caixa não escreve isso desde a v0.283); a sua Expansão já aberta continua, e abrir uma nova a derruba; refino 7 e nível 18, requisito de história (ter visto, estudado ou aprendido com alguém); o Corpo Amaldiçoado não compra.

## Lições de método

1. **Rode a fórmula em todos os valores antes de levar.** *A primeira saída só de refino arredondava a metade do dono para baixo, e refino igual e ímpar segurava a Expansão inteira; só apareceu varrendo de 4 a 10.*
2. **Número publicado sem script se reconstrói antes de ser usado.** *O `1,9` do rascunho da Expansão sem Barreiras era a média sem teto, `s ÷ (1 − s)`; com os 6 Acertos do refino 10 é `1,7`.*
3. **No modelo, cada ação gasta o slot de alguém.** *A primeira conta da Cesta sem recarga deixava ela subir de novo antes do segundo golpe da rodada, e subir de novo gasta a Ação Bônus do turno de quem segura.*
4. **Base vermelha na cópia do arnês invalida todo vermelho.** *A cópia sem os `.docx` fazia o `conferir-bestiario` reprovar na base; e uma perturbação pode acender pelo motivo errado — a do custo zero acendia por `ZeroDivisionError`. Leia a mensagem, não só o `rc`.*
5. **A 7.4 reprova quando a entrega commitada está duas versões atrás**, e aí a entrega commita **antes** do `subir.sh`. *Aconteceu com a v0.267, porque três versões fecharam na nuvem sem entrega.*
6. **Pergunte com a palavra do jogo, não com a do modelo.** *"Subida" era palavra do script, e o Mizuki não entendeu; "erguer de novo" ele entendeu na hora. E exemplo concreto de cada saída antes da pergunta: foi vendo os exemplos que ele propôs a regra que ficou.*
7. **Antes de refazer uma versão, confira o `git log` da pasta principal.** *A v0.268 foi commitada e subiu enquanto a conversa ainda discutia a regra, e a regra final teve de virar a v0.269 em cima dela.*
8. **E na retomada, confira as worktrees, e não só o `main`.** *Versão pronta e não subida mora na worktree que a fez. Em 28/09 o `main` estava na v0.275 e a fila real, na v0.282; o prompt certo era o da worktree, e a pergunta repetida custou uma volta.*

## A ordem de fechar versão

1. **A peça dona primeiro, e depois toda cópia dela.** *Nos anti-domínio: a peça 11 §6.5, o capítulo 45 do livro, a peça 25 e o capítulo 43 se tocar na semente, a peça 26 §6.5 se mexer em PE (a 9.2 do `conferir-bestiario.py` lê o custo da tabela da peça 11), o bloco 10 do `conferir-expansao.py`, e a linha do item 6 no `ESTADO-ATUAL`.* **Procure as cópias pelo sentido, não pela redação** — negrito no meio da frase já escondeu uma da busca.
2. **Nome novo se confere com `conferir-nomes.py --candidatos` antes de escrever.**
3. A nota da versão no `H` e, se a conta mudou, a regressão do script da pasta de pesquisa.
4. Entrada no `logs/CHANGELOG.md` — ele é o dono da versão, e a entrada termina com a linha que aponta para o `ESTADO-ATUAL`.
5. Bump em `README.md`, `sistema/ESTADO-ATUAL.md` e `sistema/LEIA-ME.md`, e este `PROMPT-continuar.md` atualizado.
6. Os quatro builds do livro, **depois da última edição**, de dentro de `sistema/05-material/livro/build/`: `python3 build.py`, `python3 build.py --duas`, `python3 build_docx.py` e `python3 build_txt.py`.
7. Os 31 validadores, com `PULADA` zero. *Numa worktree a entrega não existe e as 7.x pulam: emule o `subir.sh` (os passos 0 e 1, cortando no "=== 2.") numa cópia da pasta principal com o patch aplicado, e meça a 7.2 pela lista branca dela.*
8. `mensagem-de-commit.txt`, o PDF de duas colunas no chat, e o Mizuki roda o `./subir.sh` e a entrega.

## Como o Mizuki trabalha

- **Escolha de sabor é dele.** Traga as opções com o número e o trade-off já calculados, e pergunte. Rodadas curtas, nunca uma proposta grande pronta.
- **Não pergunte o que a conta responde.** Rode e mostre a tabela. **E não devolva como nova uma decisão que já está fechada.**
- **Número vem de conta rodada, nunca de intuição** — e a conta regride contra exemplo já publicado antes de medir coisa nova.
- **No chat: frase curta, uma ideia por parágrafo**, sem número de seção no meio da frase. O documento pode ser denso; a explicação não. Se ele disser que não entendeu, a resposta certa é menos detalhe, recomeçando de mais atrás.
- **Imagem de mangá em preto e branco: só se afirma o que se tem certeza.** Nada de supor. **E imagem não entra no repositório.**
- **Agente não contorna proteção de acesso** (leitor embaralhado, paywall), **e quem coordena confere o arquivo do agente, não o relatório dele.**
