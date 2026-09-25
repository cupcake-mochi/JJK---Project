# Prompt para continuar o Projeto - M em conversa nova

*Copie tudo abaixo da linha.*

---

Trabalhe em `/media/mizuki/HD Externo II/Claude/Claude 2/`, na pasta **principal**.

**Projeto - M** é um sistema de RPG de mesa no universo de Jujutsu Kaisen, para um server de guilda com vários mestres ativos e personagem persistente entre mesas. O filtro que decide quase tudo: **dois mestres que nunca se falaram chegam no mesmo número?**

**A conversa anterior tinha três partes, e a primeira fechou na v0.270.** *O que falta, nesta ordem, e cada parte fecha a sua versão antes da seguinte:*

- ~~**A — os Caminhos novos no livro (v0.270).**~~ **FECHADA na v0.270.** *Antes de começar a B, leve ao Mizuki as decisões que ela deixou — o item 15 da fila do `ESTADO-ATUAL` e a seção 4 da entrada da v0.270 do `CHANGELOG`: a perícia fixa do Bastião, a frase dos Limites, quem cura outra pessoa com Energia Reversa, e as colisões de nome da triagem. Pergunte em rodadas curtas, com a palavra do jogo.*
- **B — a rodada 3 dos anti-domínio, continuando.** Primeiro a `Pétala`, depois a `Extensão de Domínio`, e só no fim a comparação das quatro.
- **C — as Invocações, no ponto exato em que pararam:** o que acontece quando uma invocação chega a zero PV.

**Ao começar cada parte, diga em uma linha o modelo e o esforço que você recomenda para ela.**

## Regras da pasta, antes de tudo

- **Você não commita.** Deixa a mensagem pronta em `mensagem-de-commit.txt` na raiz e manda os comandos ao Mizuki, um por bloco; ele roda o `./subir.sh`, que confere os 31 validadores, commita e sobe, e depois commita a entrega à mão. *Git de leitura (`status`, `log`, `diff`) funciona daqui.*
- **Se a sessão abrir numa worktree** (uma pasta dentro de `.claude/worktrees`), a ferramenta de edição não escreve na pasta principal e a sessão não sai dela. **Edite na worktree e entregue por patch:** `git add -N` nos arquivos novos, `git diff --binary <commit do main> | git apply` da worktree para a principal (teste antes com `git apply --check`), e `cp` da `mensagem-de-commit.txt`, que é ignorada pelo git. **Antes de editar, confira que a worktree está no mesmo commit do `main`**; se estiver atrás, peça ao Mizuki para alinhar, ou gere o patch contra o commit do `main` — o `git reset --hard` pede permissão e pode ser negado.
- **Confirme a pasta:** `grep -c "^## Nove lições" README.md` tem que dar `1`. Se der `0`, é a pasta errada — pare. Existe um clone velho na home com a cara deste projeto.
- **⚠ Antes de puxar QUALQUER agente — um, dois ou três —, pergunte e espere**, dizendo quantos, o que cada um faz e quanto custa. É regra dura do arquivo de instruções da pasta de trabalho (um nível acima deste repositório), e vale mais que o ultracode; o teto é 2 a 3 por vez, e cada agente salva o próprio arquivo no HD ao longo do caminho.

---

# A ordem de tarefas

## Passo 0 — onde está

1. **O `main` deve estar no commit da v0.270** ou mais novo, com a entrega no *recorte da v0.270*. Rode `git log -3` e `git status` na pasta principal antes de qualquer coisa. *Se houver commit mais novo, leia a entrada dele no `CHANGELOG` antes de seguir.*
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

### A Pétala, primeiro

- **Como cai:** a peça diz "cai se você perder a concentração", e a obra a mostra como **programa automático** (Kusakabe, 227) — o "concentração" nasce num artigo de fã de 2023, sem painel. **Na obra ela cai com soco comum do dono do domínio** (108, pelo anime e pelo efeito; o mangá não diz com palavras) **e é largada para abrir o domínio** (227). *A caixa de abertura do capítulo 45 diz hoje "só a Pétala exige concentração" — é a regra da peça, e é ela que está em revisão.*
- **O que ela para:** o acerto garantido que **toca** — a frase *"contra um Acerto que é golpe de corpo, ela não faz nada"* cai pela definição `[I]` (nenhuma cena testa). Ela **intercepta**, não `中和`, e "não se opõe à saída do domínio" (227).
- **Quanto dura:** hoje, `refino ÷ 2` Acertos por cena e sempre sobra um — desenho do sistema, e a obra não amarra. *O Simples agora cai por rodadas contra a Expansão, em Essência e com o teste do `Carregar`, e a Cesta pelos golpes em quem segura, com o mesmo teste; a Pétala se mede contra as duas.*
- **O que custa:** `1 × maior Classe` por rodada — *a seção "Por que o custo por rodada é `1 × maior Classe`" da peça 11 vale hoje só para ela.*
- **A divergência do livro:** *a caixa da Pétala no capítulo 45 pede "ser Descendente, ou ter aprendido com alguém de algum clã" e refino 2* (a peça: refino 4 e nível 10, sem requisito). **Veio da revisão do Mizuki no Word da v0.176, como o requisito da Cesta e o do Simples** — *os dois ficaram, por decisão dele, e o §5 da peça 11 registra o "requisito de história", que não é gate. O refino 2 ou 4 com nível 10 não muda o marco de ninguém: meça, não suponha.*

### Depois, a Extensão de Domínio

- **"Faz o seu ataque acertar independentemente da técnica do alvo"** é, quase palavra por palavra, a frase da wiki, não a do Fanbook. O Fanbook (p. 143) diz que ela **neutraliza** a técnica que toca e o acerto garantido da Expansão; **a obra nunca a pôs contra acerto de domínio.**
- **Ela é a única das quatro em que a atenuação tem cena:** técnica de saída alta passa em parte (o Vermelho mitigado, 232). A Cesta e o Simples protegem inteiro até cair.
- **"Nenhuma serve contra a incompleta"** vale para a Cesta e o Simples, pelo 171, e **não** para a Extensão. *E o capítulo 45 diz "algumas delas servem contra a Expansão incompleta", contra a peça — é esta rodada que fecha a frase.*
- **É largada para usar a técnica** — isso a peça já tem. **Junto com a técnica reversa, a obra não amarra**, e é desenho.
- **O livro diverge da peça, também da v0.176:** *a caixa da Extensão diz nível 18 e a tabela do mesmo capítulo diz 14; e ela "anula os efeitos" da Expansão e "neutraliza técnicas ao toque".*

### Só no fim, a comparação das quatro

**O Mizuki pediu para não comparar as quatro antes das três serem revistas.** Quando a Extensão fechar: a matriz lado a lado — quem cai por quê, quanto segura, o que custa, e se alguma ficou dominada. *Um ponto para olhar lá: o Simples barato em PE, cobrindo o raio e com as mãos livres, contra a Cesta de Classe 1 e sem PE.*

## Parte C — as Invocações, no ponto do zero PV

**Estado:** *o subsistema está na **v0.3 CANDIDATA, revisão 5, decisões até o §45**, com 212 verificações simbólicas aprovadas (178 anteriores e 34 novas), **sem prova de equilíbrio e sem playtest humano**.* **As decisões não precisam ser aprovadas de novo.**

**Onde ler:** *em `invocacoes/03-INVOCACOES/`:* **00-REGISTRO-E-PONTO-DE-RETOMADA.md**, **ATUAL-r5/01-PROCEDIMENTOS-DE-CAMPO-v0.3-CANDIDATA-r5.md** e **ATUAL-r5/03-PENDENCIAS-E-CONFLITOS.md**. *O REGISTRO-DA-CONTINUIDADE/ e as pesquisas servem para uma dúvida específica, não para leitura inteira.*

**O que vale sem discussão:**
- **Primeiro o subsistema de Invocações; o Evocador e as Trilhas dele vêm depois.**
- **Customização completa, e as fantasias de entidade singular, parceria e pequeno conjunto de entidades distintas, são diretrizes** — *não fichas nem limites numéricos aprovados.*
- **Energia própria das entidades e custo de substituição continuam pendentes.**
- **Não crie construtor, catálogo, preço, orçamento, `X`, alcance, PE, PV, dano ou progressão para preencher lacuna.**

**O ponto exato de parada:** *a próxima discussão era a consequência imediata de uma invocação chegar a zero PV.* **O §22 aprovou a equivalência entre campo e reserva, mas não escolheu entre dissipar, ficar inconsciente, ser destruída ou se recuperar.** *Foi recomendado que ela saia do campo a zero PV, encerrando ordens e preparações pela saída, sem devolução nem cura automática.* **O Mizuki ainda não aprovou essa recomendação:** *não crie o §46 nem aplique a proposta como regra.*

**Como retomar:** mostre o resultado das Partes A e B em poucas linhas, e depois **retome só esse ponto**, explicando por que a regra que existe não o resolve. *Não reabra questão aprovada.* **Uma decisão nova de verdade ganha número a partir do §46 só depois da aprovação do Mizuki.**

## Pendentes pequenos, fora das três partes

- **O balão do cap. 246 no vol. 28** — quem tiver o volume confere se o `薄める` virou `弱める`. *O dado que existe foi lido contornando a proteção do leitor da Shueisha e voltou a **não conferido**; não repita esse caminho.*
- **O repositório da ficha (`Claude 3`) tem o texto velho da Cesta e do Simples** até a próxima extração do livro — *e, depois da Parte A, os Caminhos velhos também.*
- **A nota de pesquisa do bestiário que cita o raio de 2,21 m fica como está** — é nota de campo.

---

# O contexto que você precisa

## Onde o projeto está

**v0.270.** Manual do Fundamento na **v7.38**. **Vinte e sete peças de regra e vinte e sete validadores** em `sistema/03-mecanica/`, mais o `conferir-repositorio.py`, os dois de `manual/matematica/` e o `conferir-voz.py` — **31 validadores**. O livro tem **18 capítulos**. A ficha (`Claude 3`, o `Ficha---RPG-JJK`) não mudou.

**A v0.264 e a v0.265 foram pesquisa** (`sistema/01-pesquisa/anti-dominios/`, arquivos `A` a `N`). **A v0.266 foi a rodada 1** (as frases da peça 11 que atribuíam à obra o que ela não faz). **A v0.267 foi a rodada 2, a Cesta**, e **a v0.268 e a v0.269, o começo da rodada 3, o Simples** — *a v0.269 trocou a regra de queda que a v0.268 tinha publicado.*

**Os Caminhos e as Invocações foram trabalhados fora desta pasta**, num chat que não a via, e voltaram por pacote na v0.270. *A coleção v0.4 dos Caminhos está no livro, em `caminhos/`; as Invocações estão na candidata r5, em `invocacoes/`, fora da edição jogável.*

## O que a pesquisa dos anti-domínio mudou

**A casca não é a variável — é a diferença de saída (`出力`) entre quem defende e quem abriu**, e o sistema tem a moeda para isso nos dois lados: o refino. *No Simples, por decisão do Mizuki, a moeda acabou sendo a Essência — a de quem segura contra a do dono —, e o refino ficou no raio e no gate.* **Nenhuma das quatro tem relógio próprio na obra: todas caem por fora.** **E o jeito de ceder muda de uma para outra:** a atenuação só tem cena na Extensão; a Cesta e o Simples protegem por inteiro até cair; a Pétala intercepta.

**Seis coisas a obra não amarra, e são desenho livre:** custo de energia, limite de tempo, Extensão junto com a técnica reversa, Cesta com encantamento próprio, quem usa a Pétala fora do Zenin e do Gojo, e como se aprende a Cesta.

## As duas anti-domínio que já fecharam

**A Cesta Oca (v0.267, a queda na v0.268, e o teste na v0.269):** as duas mãos presas no símbolo; levanta com Reação quando uma Expansão abre ou Ação Bônus no turno; cai pelos golpes em quem segura (**o teste do `Carregar`, Espírito contra a CD de quem feriu** — era Vigor até a v0.268 —, falhas até metade da Essência); **quando cai, a Expansão alcança na hora, e ela levanta de novo sem espera, gastando a Ação Bônus**; PE zero; requisito de história (Reencarnado, ou treinado em `História`).

**O Domínio Simples (v0.268, e a queda na v0.269):** **aguenta `3` rodadas de Expansão, `4` se a Essência de quem segura for maior que a do dono e `2` se for menor**; cada Acerto que ele segura gasta uma, a começar pelo de abrir, e pede **o teste do `Carregar`** — a falha tira uma rodada, nunca abaixo de metade da Essência; golpe no dono não o derruba; quando cai, a Expansão alcança na hora quem ele protegia, e **erguer de novo na mesma Expansão custa a Ação Padrão e aguenta metade** (mínimo 1). **Lá dentro a Expansão não alcança ninguém**, e o que ela dá ao dono continua. **Os pés são o voto do iniciante** (refino 4; com refino 5 ele anda com você), o gate é refino 5 sem nível, e o PE são `2` fixos. **Contra refino 10 nenhum Simples segura até o fim.** *O teste não tem nome próprio; se o Mizuki quiser um, os candidatos livres na triagem foram Sustentar, Tenacidade, Manter, Sustentação e Firmar.*

## Lições de método

1. **Rode a fórmula em todos os valores antes de levar.** *A primeira saída só de refino arredondava a metade do dono para baixo, e refino igual e ímpar segurava a Expansão inteira; só apareceu varrendo de 4 a 10.*
2. **Número publicado sem script se reconstrói antes de ser usado.** *O `1,9` do rascunho da Expansão sem Barreiras era a média sem teto, `s ÷ (1 − s)`; com os 6 Acertos do refino 10 é `1,7`.*
3. **No modelo, cada ação gasta o slot de alguém.** *A primeira conta da Cesta sem recarga deixava ela subir de novo antes do segundo golpe da rodada, e subir de novo gasta a Ação Bônus do turno de quem segura.*
4. **Base vermelha na cópia do arnês invalida todo vermelho.** *A cópia sem os `.docx` fazia o `conferir-bestiario` reprovar na base; e uma perturbação pode acender pelo motivo errado — a do custo zero acendia por `ZeroDivisionError`. Leia a mensagem, não só o `rc`.*
5. **A 7.4 reprova quando a entrega commitada está duas versões atrás**, e aí a entrega commita **antes** do `subir.sh`. *Aconteceu com a v0.267, porque três versões fecharam na nuvem sem entrega.*
6. **Pergunte com a palavra do jogo, não com a do modelo.** *"Subida" era palavra do script, e o Mizuki não entendeu; "erguer de novo" ele entendeu na hora. E exemplo concreto de cada saída antes da pergunta: foi vendo os exemplos que ele propôs a regra que ficou.*
7. **Antes de refazer uma versão, confira o `git log` da pasta principal.** *A v0.268 foi commitada e subiu enquanto a conversa ainda discutia a regra, e a regra final teve de virar a v0.269 em cima dela.*

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
