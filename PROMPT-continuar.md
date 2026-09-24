# Prompt para continuar o Projeto - M em conversa nova

*Copie tudo abaixo da linha.*

---

Trabalhe em `/media/mizuki/HD Externo II/Claude/Claude 2/`, na pasta **principal**.

**Projeto - M** é um sistema de RPG de mesa no universo de Jujutsu Kaisen, para um server de guilda com vários mestres ativos e personagem persistente entre mesas. O filtro que decide quase tudo: **dois mestres que nunca se falaram chegam no mesmo número?**

**Esta conversa continua a rodada 3 da revisão dos quatro anti-domínio: a `Pétala`, depois a `Extensão de Domínio`, e só no fim a comparação das quatro.** A `Cesta Oca` foi decidida na v0.267 e o `Domínio Simples` na v0.268. O registro da pesquisa e das rodadas 1 e 2 está em `logs/SESSAO-2026-09-24-anti-dominios.md`; o da rodada 3 até aqui está na entrada da v0.268 do `logs/CHANGELOG.md`, com as palavras do Mizuki.

## Regras da pasta, antes de tudo

- **Você não commita.** Deixa a mensagem pronta em `mensagem-de-commit.txt` na raiz e manda os comandos ao Mizuki, um por bloco; ele roda o `./subir.sh`, que confere os 31 validadores, commita e sobe, e depois commita a entrega à mão. *Git de leitura (`status`, `log`, `diff`) funciona daqui.*
- **Se a sessão abrir numa worktree** (uma pasta dentro de .claude/worktrees), a ferramenta de edição não escreve na pasta principal e a sessão não sai dela. **Edite na worktree e entregue por patch:** `git add -N` nos arquivos novos, `git diff --binary HEAD | git apply` da worktree para a principal (teste antes com `git apply --check`), e `cp` da `mensagem-de-commit.txt`, que é ignorada pelo git. *Depois que o Mizuki commitar, alinhe a worktree com o `main` antes da versão seguinte.*
- **Confirme a pasta:** `grep -c "^## Nove lições" README.md` tem que dar `1`. Se der `0`, é a pasta errada — pare. Existe um clone velho na home com a cara deste projeto.

---

# A ordem de tarefas

## Leia nesta ordem

1. `sistema/ESTADO-ATUAL.md` — onde parou e o que vem em seguida. **Leia inteiro**, inclusive a fila no fim; ele trunca, e se vier aviso de leitura parcial, continue do offset
2. `README.md` — as **nove lições que custaram erro**, e elas moram só lá
3. `logs/CHANGELOG.md` — as entradas `0.265` a `0.268`: o **porquê** de cada uma
4. `logs/SESSAO-2026-09-24-anti-dominios.md` — o que a conversa da nuvem tinha e os arquivos não têm
5. `sistema/01-pesquisa/anti-dominios/H-resumo-das-quatro.md` — as quatro técnicas na obra, como cada uma cai, e as divergências contra a peça 11
6. `sistema/03-mecanica/11-aptidoes-e-refino.md` §6.5 — a regra das quatro, dona de tudo que a rodada vai mexer
7. `sistema/01-pesquisa/anti-dominios/conta-dominio-simples.py` — a conta do Simples, que é o molde da conta da Pétala

E rode a skill `rpg-da-guilda` antes de começar.

## Passo 1 — a Pétala

**Mesmo método das rodadas 2 e 3.** O que se mede é o que o Mizuki pediu: **como cai, quanto dura, o que dá, o que não dá, e o que custa.**

1. **Mostre, curto, o que a peça 11 diz hoje e o que a obra diz** — o `H` tem a obra, com a marca de evidência (`[C]` cânone, `[F]` oficial, `[I]` inferência). **Antes de oferecer agente, procure nos arquivos `A` a `N`**: na rodada do Simples, a pergunta "apura de novo" já estava respondida na verificação cega.
2. **Liste as perguntas de desenho, numeradas.** O Mizuki responde no formato "1 - … 2 - …".
3. **Meça antes de perguntar**, num script irmão na mesma pasta, com o mesmo contrato: **a regressão reproduz os números publicados antes de medir coisa nova**, probabilidade exata e não Monte Carlo, e âncora lida da peça dona. *O `conta-cesta-oca.py` já reproduz a Pétala de hoje (o `R3` dele: `refino ÷ 2`, e sempre sobra um).*
4. **Traga as opções com o número e o trade-off já calculados**, e o Mizuki decide. *Ele também propõe fórmula — foi a dele que ficou no Simples. Meça a dele nas leituras possíveis e diga qual leitura você aplicou.*
5. **Aplique como versão nova**, pela ordem de fechar versão lá embaixo.

**O que a rodada tem que encarar:**

- **Como cai:** a peça diz "cai se você perder a concentração", e a obra a mostra como **programa automático** (Kusakabe, 227) — o "concentração" nasce num artigo de fã de 2023, sem painel. **Na obra ela cai com soco comum do dono do domínio** (108, pelo anime e pelo efeito; o mangá não diz com palavras) **e é largada para abrir o domínio** (227). *A caixa de abertura do capítulo 45 do livro diz hoje "só a Pétala exige concentração" — é a regra da peça, e é ela que está em revisão.*
- **O que ela para:** o acerto garantido que **toca** — a frase *"contra um Acerto que é golpe de corpo, ela não faz nada"* cai pela definição `[I]` (nenhuma cena testa). Ela **intercepta**, não `中和`, e "não se opõe à saída do domínio" (227).
- **Quanto dura:** hoje, `refino ÷ 2` Acertos por cena e sempre sobra um — isso é desenho do sistema, e a obra não amarra. *O Simples agora cai por rodadas contra a Expansão, e a Cesta pelos golpes em quem segura; a Pétala se mede contra as duas.*
- **O que custa:** `1 × maior Classe` por rodada — *a seção "Por que o custo por rodada é `1 × maior Classe`" da peça 11 vale hoje só para ela.*
- **A divergência do livro, que espera esta rodada:** *a caixa da Pétala no capítulo 45 pede "ser Descendente, ou ter aprendido com alguém de algum clã" e refino 2* (a peça: refino 4 e nível 10, sem requisito). **Veio da revisão do Mizuki no Word da v0.176, como o requisito da Cesta e o do Simples** — *os dois ficaram, por decisão dele, e o §5 da peça 11 registra o "requisito de história", que não é gate. O refino 2 ou 4 com nível 10 não muda o marco de ninguém: meça, não suponha.*

## Passo 2 — a Extensão de Domínio

- **"Faz o seu ataque acertar independentemente da técnica do alvo"** é, quase palavra por palavra, a frase da wiki, não a do Fanbook. O Fanbook (p. 143) diz que ela **neutraliza** a técnica que toca e o acerto garantido da Expansão; **a obra nunca a pôs contra acerto de domínio.**
- **Ela é a única das quatro em que a atenuação tem cena:** técnica de saída alta passa em parte (o Vermelho mitigado, 232). A Cesta e o Simples protegem inteiro até cair.
- **"Nenhuma serve contra a incompleta"** vale para a Cesta e o Simples, pelo 171, e **não** para a Extensão. *E o capítulo 45 do livro diz "algumas delas servem contra a Expansão incompleta", contra a peça — é esta rodada que fecha a frase.*
- **É largada para usar a técnica** — isso a peça já tem. **Junto com a técnica reversa, a obra não amarra**, e é desenho.
- **O livro diverge da peça, também da v0.176:** *a caixa da Extensão diz nível 18 e a tabela do mesmo capítulo diz 14; e ela "anula os efeitos" da Expansão e "neutraliza técnicas ao toque".*

## Passo 3 — a comparação das quatro, só depois

**O Mizuki pediu para não comparar as quatro antes das três serem revistas.** Quando a Extensão fechar: a matriz lado a lado — quem cai por quê, quanto segura, o que custa, e se alguma ficou dominada. *Um ponto para olhar lá: o Simples barato em PE, cobrindo o raio e com as mãos livres, contra a Cesta de Classe 1 e sem PE.*

## Pendentes pequenos, fora da rodada

- **O balão do cap. 246 no vol. 28** — quem tiver o volume confere se o `薄める` virou `弱める`. *O dado que existe foi lido contornando a proteção do leitor da Shueisha e voltou a **não conferido**; não repita esse caminho.*
- **O repositório da ficha (`Claude 3`) tem o texto velho da Cesta e do Simples** até a próxima extração do livro.
- **A nota de pesquisa do bestiário que cita o raio de 2,21 m fica como está** — é nota de campo.

---

# O contexto que você precisa

## Onde o projeto está

**v0.268.** Manual do Fundamento na **v7.38**. **Vinte e sete peças de regra e vinte e sete validadores** em `sistema/03-mecanica/`, mais o `conferir-repositorio.py`, os dois de `manual/matematica/` e o `conferir-voz.py` — **31 validadores**. A ficha (`Claude 3`, o `Ficha---RPG-JJK`) não mudou.

**A v0.264 e a v0.265 foram pesquisa** (`sistema/01-pesquisa/anti-dominios/`, arquivos `A` a `N`). **A v0.266 foi a rodada 1** (as frases da peça 11 que atribuíam à obra o que ela não faz). **A v0.267 foi a rodada 2, a Cesta**, e **a v0.268, o começo da rodada 3, o Simples.**

## O que a pesquisa mudou, e você precisa saber antes de propor qualquer coisa

**A casca não é a variável — é a diferença de saída (`出力`) entre quem defende e quem abriu**, e o sistema tem a moeda para isso nos dois lados: o refino. **Nenhuma das quatro tem relógio próprio na obra: todas caem por fora.** **E o jeito de ceder muda de uma para outra:** a atenuação só tem cena na Extensão; a Cesta e o Simples protegem por inteiro até cair; a Pétala intercepta.

**Seis coisas a obra não amarra, e são desenho livre:** custo de energia, limite de tempo, Extensão junto com a técnica reversa, Cesta com encantamento próprio, quem usa a Pétala fora do Zenin e do Gojo, e como se aprende a Cesta.

## As duas que já fecharam

**A Cesta Oca (v0.267, e a queda na v0.268):** as duas mãos presas no símbolo; levanta com Reação quando uma Expansão abre ou Ação Bônus no turno; cai pelos golpes em quem segura (Vigor contra a CD de quem feriu, falhas até metade da Essência); **quando cai, a Expansão alcança na hora, e ela levanta de novo sem espera, gastando a ação**; PE zero; requisito de história (Reencarnado, ou treinado em `História`).

**O Domínio Simples (v0.268):** **aguenta metade da Essência (mínimo 1) mais uma rodada de Expansão, menos uma por ponto de refino que o dono dela tem acima do seu, no mínimo uma**; o Acerto de abrir não conta; golpe no dono não o derruba; quando cai, a Expansão alcança na hora quem ele protegia, e ele levanta de novo sem espera. **Lá dentro a Expansão não alcança ninguém**, e o que ela dá ao dono continua. **Os pés são o voto do iniciante** (refino 4; com refino 5 ele anda com você), o gate é refino 5 sem nível, e o PE são `2` fixos. **Contra refino 10 nenhum Simples segura até o fim.**

## Lições de método desta rodada

1. **Rode a fórmula em todos os valores antes de levar.** *A primeira saída só de refino arredondava a metade do dono para baixo, e refino igual e ímpar segurava a Expansão inteira; só apareceu varrendo de 4 a 10.*
2. **Número publicado sem script se reconstrói antes de ser usado.** *O `1,9` do rascunho da Expansão sem Barreiras era a média sem teto, `s ÷ (1 − s)`; com os 6 Acertos do refino 10 é `1,7`.*
3. **No modelo, cada ação gasta o slot de alguém.** *A primeira conta da Cesta sem recarga deixava ela subir de novo antes do segundo golpe da rodada, e subir de novo gasta a Ação Bônus do turno de quem segura.*
4. **Base vermelha na cópia do arnês invalida todo vermelho.** *A cópia sem os `.docx` fazia o `conferir-bestiario` reprovar na base; e uma perturbação pode acender pelo motivo errado — a do custo zero acendia por `ZeroDivisionError`. Leia a mensagem, não só o `rc`.*
5. **A 7.4 reprova quando a entrega commitada está duas versões atrás**, e aí a entrega commita **antes** do `subir.sh`. *Aconteceu com a v0.267, porque três versões fecharam na nuvem sem entrega.*

## A ordem de fechar versão

1. **A peça dona primeiro** — aqui, a peça 11 §6.5 —, e depois toda cópia dela: o capítulo 45 do livro (`sistema/05-material/livro/manual/45-aptidoes-e-refino.md`), a peça 25 e o capítulo 43 se tocar na semente, a peça 26 §6.5 se mexer em PE (a checagem 9.2 do `conferir-bestiario.py` lê o custo da tabela da peça 11), o bloco 10 do `conferir-expansao.py`, e a linha do item 6 no `ESTADO-ATUAL`. **Procure as cópias pelo sentido, não pela redação** — negrito no meio da frase já escondeu uma da busca.
2. **Nome novo se confere com `conferir-nomes.py --candidatos` antes de escrever.**
3. A nota da versão no `H` e, se a conta mudou, a regressão do script da pasta de pesquisa.
4. Entrada no `logs/CHANGELOG.md` — ele é o dono da versão, e a entrada termina com a linha que aponta para o `ESTADO-ATUAL`.
5. Bump em `README.md`, `sistema/ESTADO-ATUAL.md` e `sistema/LEIA-ME.md`, e este `PROMPT-continuar.md` atualizado.
6. Os quatro builds do livro, **depois da última edição**, de dentro de `sistema/05-material/livro/build/`: `python3 build.py`, `python3 build.py --duas`, `python3 build_docx.py` e `python3 build_txt.py`.
7. Os 31 validadores, com `PULADA` zero. *Numa worktree a entrega não existe e as 7.x pulam: emule o `subir.sh` numa cópia da pasta principal com a entrega, e meça a 7.2 pelo diff dela.*
8. `mensagem-de-commit.txt`, o PDF de duas colunas no chat, e o Mizuki roda o `./subir.sh` e a entrega.

## Como o Mizuki trabalha

- **Escolha de sabor é dele.** Traga as opções com o número e o trade-off já calculados, e pergunte. Rodadas curtas, nunca uma proposta grande pronta.
- **Não pergunte o que a conta responde.** Rode e mostre a tabela. **E não devolva como nova uma decisão que já está fechada.**
- **Número vem de conta rodada, nunca de intuição** — e a conta regride contra exemplo já publicado antes de medir coisa nova.
- **No chat: frase curta, uma ideia por parágrafo**, sem número de seção no meio da frase. O documento pode ser denso; a explicação não. Se ele disser que não entendeu, a resposta certa é menos detalhe, recomeçando de mais atrás.
- **Imagem de mangá em preto e branco: só se afirma o que se tem certeza.** Nada de supor. **E imagem não entra no repositório.**
- **⚠ Antes de puxar QUALQUER agente de pesquisa, pergunte e espere** — é regra dura, escrita no arquivo de instruções da pasta de trabalho (um nível acima deste repositório), e vale mais que o ultracode; o teto é 2 a 3 por vez. **Todo agente salva o próprio arquivo ao longo do caminho, com append a cada bloco, numa pasta do HD e não no `/tmp`.** **Agente não contorna proteção de acesso** (leitor embaralhado, paywall), **e quem coordena confere o arquivo do agente, não o relatório dele.**
