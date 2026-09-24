# Prompt para continuar o Projeto - M em conversa nova

*Copie tudo abaixo da linha.*

---

Trabalhe em `/media/mizuki/HD Externo II/Claude/Claude 2/`, na pasta **principal**, não em worktree.

**Projeto - M** é um sistema de RPG de mesa no universo de Jujutsu Kaisen, para um server de guilda com vários mestres ativos e personagem persistente entre mesas. O filtro que decide quase tudo: **dois mestres que nunca se falaram chegam no mesmo número?**

**Esta conversa continua a revisão dos quatro anti-domínio, na rodada 3.** A pesquisa e as rodadas 1 e 2 foram feitas numa sessão na nuvem, em 24/09/2026. O que ela decidiu está nos arquivos; o registro da conversa, com as palavras do Mizuki em cada decisão, está em `logs/SESSAO-2026-09-24-anti-dominios.md`.

## Regras da pasta, antes de tudo

- **Você não roda git**, nem `status`: o mount rejeita o que o git faz ao gravar. Para saber em que commit a pasta está, leia `.git/logs/HEAD` como arquivo.
- **Você não commita.** Deixa a mensagem pronta em `mensagem-de-commit.txt` na raiz e avisa o Mizuki; ele roda o `./subir.sh`, que confere os 31 validadores, commita e sobe.
- **Confirme a pasta:** `grep -c "^## Nove lições" README.md` tem que dar `1`. Se der `0`, é a pasta errada — pare. Existe um clone velho na home com a cara deste projeto.

---

# A ordem de tarefas

## Passo 0 — trazer a v0.267 para a pasta (o Mizuki roda)

**A v0.265, a v0.266 e a v0.267 estão só no branch `claude/jjk-anti-dominios-research-59hjly`, no GitHub.** O `main` não andou desde que o branch saiu dele (commit `ba1e0df`, a v0.264): o branch está 52 commits à frente e 0 atrás, então o caminho é um fast-forward, sem conflito possível.

**A decisão de levar para o `main` é do Mizuki.** Os comandos, do lado dele:

```bash
cd "/media/mizuki/HD Externo II/Claude/Claude 2"
git status --short
git fetch origin
git checkout main
git merge --ff-only origin/claude/jjk-anti-dominios-research-59hjly
git push
```

*O `git status --short` tem que vir vazio; se não vier, é trabalho local que ainda não subiu, e ele resolve antes. Se o `--ff-only` recusar, o `main` local tem commit que o GitHub não tem — pare e olhe, não force.*

**Confira do seu lado, lendo arquivo:** o `README.md` diz **Versão v0.267**, a última linha do `.git/logs/HEAD` mostra o merge que acabou de entrar, e `logs/SESSAO-2026-09-24-anti-dominios.md` existe.

## Leia nesta ordem, depois do Passo 0

1. `sistema/ESTADO-ATUAL.md` — onde parou e o que vem em seguida. **Leia inteiro**, inclusive a fila no fim; ele trunca, e se vier aviso de leitura parcial, continue do offset
2. `README.md` — as **nove lições que custaram erro**, e elas moram só lá
3. `logs/CHANGELOG.md` — as entradas `0.264` a `0.267`: o **porquê** de cada uma, que é a única parte que não dá para reconstruir lendo o resto
4. `logs/SESSAO-2026-09-24-anti-dominios.md` — o que a conversa da nuvem tinha e os arquivos não têm
5. `sistema/01-pesquisa/anti-dominios/H-resumo-das-quatro.md` — as quatro técnicas na obra, como cada uma cai, e as catorze divergências contra a peça 11
6. `sistema/03-mecanica/11-aptidoes-e-refino.md` §6.5 — a regra das quatro, dona de tudo que a rodada vai mexer

E rode a skill `rpg-da-guilda` antes de começar: ela tem o procedimento — ordem de leitura, validadores, triagem de nome, arnês de perturbação e como fechar versão.

## Passo 1 — refazer o livro e sincronizar a entrega

**A v0.267 mudou o capítulo 45 do livro, e na nuvem só o texto corrido foi regenerado** — o PDF depende das fontes e do WeasyPrint desta pasta. Então, antes de mexer em regra:

1. **Você** roda os quatro builds, de dentro de `sistema/05-material/livro/build/`: `python3 build.py`, `python3 build.py --duas`, `python3 build_docx.py` e `python3 build_txt.py`. *O texto corrido deve sair igual ao que já está no commit, salvo o hash; se sair diferente em outra coisa, olhe antes de seguir.*
2. **Você** roda os 31 validadores. Espere verde com `PULADA` zero, porque aqui a `finalizado/` existe; o `conferir-repositorio.py` pode acusar só a `7.1` e a `7.3`, que são o recorte da entrega atrás, e o `subir.sh` conserta sozinho. *Na nuvem ele reprovava também duas citações à pasta do livro dentro da entrega, no `ESTADO-ATUAL` e no `ESTADO-revisao`, só porque a entrega não existia lá; aqui elas devem resolver. Se não resolverem, é achado.*
3. **Você** deixa a mensagem em `mensagem-de-commit.txt`: o `.docx` e os dois PDFs do livro refeitos para a v0.267, sem mudança de regra.
4. **O Mizuki** roda os três comandos: o `./subir.sh`, que copia as peças 11 e 25, o PDF e o `.docx` para a entrega e sobe; depois a entrega, que commita à mão — `cd finalizado && git add -A && git commit -m "recorte da v0.267" && git push; cd ..`
5. **O Mizuki** atualiza o Project com os arquivos que mudaram.

## Passo 2 — rodada 3, começando pelo Domínio Simples

**A rodada 3 revisa o Domínio Simples, a Pétala e a Extensão, uma de cada vez e nessa ordem, com a Cesta Oca de base.** O que se mede em cada uma é o que o Mizuki pediu na rodada 2: **como cai, quanto dura, o que dá, o que não dá, e o que custa.**

### O método, que funcionou na rodada 2 e se repete aqui

1. **Mostre, curto, o que a peça 11 diz hoje e o que a obra diz** — o `H` tem a obra, com a marca de evidência de cada afirmação (`[C]` cânone, `[F]` oficial, `[I]` inferência).
2. **Liste as perguntas de desenho que a técnica abre**, numeradas. O Mizuki responde no formato "1 - … 2 - …".
3. **Meça antes de perguntar.** Estenda o `sistema/01-pesquisa/anti-dominios/conta-cesta-oca.py` ou escreva um script irmão na mesma pasta, com o mesmo contrato: **a regressão reproduz os números publicados antes de medir coisa nova** (o `R4` do script já reproduz o Domínio Simples de hoje, `30` PE e `324` evitados no nível 22, `35` e `378` no 26), probabilidade exata e não Monte Carlo, e âncora lida da peça dona — nada de número digitado quando existe dono.
4. **Traga as opções com o número e o trade-off já calculados**, e o Mizuki decide.
5. **Aplique como versão nova**, pela ordem de fechar versão lá embaixo.

### O Domínio Simples — o que a peça diz hoje

*Classe Passiva 2, refino 4 e nível 10. Raio de `1,5 m + refino ÷ 2`, que nunca passa de 9 m. Dentro dele o Acerto de uma Expansão não acontece. Custa `1 × a sua maior Classe` de PE por rodada, e quebra se os seus pés saírem do chão.* **Contra domínio nenhum ele cede** — é a pergunta que a seção 8.2 do `sistema/03-mecanica/RASCUNHO-expansao-sem-barreira.md` deixou aberta.

### O que a obra mostra (o detalhe está no `H`, seção 2)

- **Ele cai pela pressão do domínio** (206, 226; o 258 pela leitura do desenho, `[I]`) **ou pelo voto do usuário** (a Miwa, cap. 40, com o voto acionado em cena). **Nunca caiu por golpe no dono dentro de domínio.**
- **Protege inteiro até cair** — é limiar, não redução (`[I]`) —, e desgasta à vista antes de ceder.
- **Quanto dura depende da diferença de saída**, não da casca: sem casca e em potência plena ele cai em segundos; sem casca e incompleto, quatro Domínios Simples aguentaram perto de 99 s (258).
- **O dono luta dentro dele** — a técnica não desliga, e ele não queima a técnica. **Anda junto com a técnica reversa** (o Gojo cura segurando ele, 226). **Dá para erguer de novo logo depois de arrancado** (o Gojo fez duas vezes seguidas, 226).
- **"Os pés não saem do chão" é o voto da Miwa, não a técnica**, e a narração diz "os dois pés saírem **do ponto onde foi ativado**", não "do chão". O Kusakabe usa sem voto, com raio maior, e alarga o raio em combate (254) — **na v0.266 a peça ficou sem isso, de propósito**, porque a trava de 9 m separa defesa de cerco.
- *"Simples, mas domínio é domínio"* — pensamento do Kusakabe, cap. 254.

### As saídas já medidas (seção 8.4 do rascunho) — ponto de partida, não decisão

| saída | quanto ele segura contra a Expansão sem Barreiras de refino 10 |
|---|---|
| igual a hoje | os seis Acertos, sem ceder — contradiz a obra |
| **um teste a cada Acerto** contra a CD do dono da Expansão | `1,9` Acertos com bônus `+10`, `1,0` com `+7`, `0,2` com `+0` — é o formato da concentração na corrida |
| segura `refino ÷ 2` Acertos, mínimo 1 | espelha a Pétala; no refino alto quase não cede |

**Agora há uma quarta referência, que não existia quando isso foi medido: a Cesta Oca da v0.267.** Ela cai pelos **golpes em quem segura**, e o Simples, pela obra, cai pela **pressão da Expansão** — é o eixo natural para separar os dois. *A regressão do script novo precisa reproduzir o `1,9 / 1,0 / 0,2` antes de medir qualquer variante.*

### A divergência entre o livro e a peça, que espera esta rodada

**O capítulo 45 do livro dá ao Domínio Simples refino 3** (a peça, 4), **o requisito "ter visto um sendo usado, ou ter aprendido com alguém"** (a peça não tem requisito), **e diz que ele anula "os efeitos" da Expansão** (a peça, só o Acerto). *A peça é a dona; a decisão do Mizuki fecha as três de uma vez.* **Na Cesta o requisito do livro ficou, por decisão dele** ("E os requisitos ficam") — é um precedente, não uma regra.

## Passo 3 — a Pétala

**Mesmo método.** O que a rodada tem que encarar:

- **Como cai:** a peça diz "cai se você perder a concentração", e a obra a mostra como **programa automático** (Kusakabe, 227) — o "concentração" nasce num artigo de fã de 2023, sem painel. **Na obra ela cai com soco comum do dono do domínio** (108, pelo anime e pelo efeito; o mangá não diz com palavras) **e é largada para abrir o domínio** (227).
- **O que ela para:** o acerto garantido que **toca** — a frase *"contra um Acerto que é golpe de corpo, ela não faz nada"* cai pela definição `[I]` (nenhuma cena testa). Ela **intercepta**, não `中和`, e "não se opõe à saída do domínio" (227).
- **Quanto dura:** hoje, `refino ÷ 2` Acertos por cena e sempre sobra um — isso é desenho do sistema, e a obra não amarra.

## Passo 4 — a Extensão de Domínio

- **"Faz o seu ataque acertar independentemente da técnica do alvo"** é, quase palavra por palavra, a frase da wiki, não a do Fanbook. O Fanbook (p. 143) diz que ela **neutraliza** a técnica que toca e o acerto garantido da Expansão; **a obra nunca a pôs contra acerto de domínio.**
- **Ela é a única das quatro em que a atenuação tem cena:** técnica de saída alta passa em parte (o Vermelho mitigado, 232). A Cesta e o Simples protegem inteiro até cair.
- **"Nenhuma serve contra a incompleta"** vale para a Cesta e o Simples, pelo 171, e **não** para a Extensão — contra os shikigami de uma incompleta a obra não diz nada.
- **É largada para usar a técnica** — isso a peça já tem. **Junto com a técnica reversa, a obra não amarra**, e é desenho.

## Passo 5 — a comparação das quatro, só depois

**O Mizuki pediu para não comparar as quatro antes das três serem revistas.** Na rodada 2 a Cesta foi decidida sozinha, e as outras se medem contra ela. Quando as três fecharem, aí sim: a matriz lado a lado — quem cai por quê, quanto segura, o que custa, e se alguma ficou dominada.

## Pendentes pequenos, fora da rodada

- **O balão do cap. 246 no vol. 28** — quem tiver o volume confere se o `薄める` virou `弱める`. *O dado que existe foi lido contornando a proteção do leitor da Shueisha e voltou a **não conferido**; não repita esse caminho.*
- **A nota de pesquisa do bestiário que cita o raio de 2,21 m fica como está** — é nota de campo.

---

# O contexto que você precisa

## Onde o projeto está

**v0.267.** Manual do Fundamento na **v7.38**. **Vinte e sete peças de regra e vinte e sete validadores** em `sistema/03-mecanica/`, mais o `conferir-repositorio.py`, os dois de `manual/matematica/` e o `conferir-voz.py` — **31 validadores**. *Da v0.265 à v0.267 foram fechadas na nuvem, sem a `finalizado/`: lá 30 passaram e o `conferir-repositorio.py` reprovou só pelas citações à pasta da entrega.* **O verde de verdade é o `subir.sh` daqui.** A ficha (`Claude 3`, o `Ficha---RPG-JJK`) não mudou.

**A v0.264 e a v0.265 foram pesquisa, e nenhum número do sistema se moveu.** A v0.264 levantou as quatro técnicas em `sistema/01-pesquisa/anti-dominios/` (arquivos `A` a `H`). A v0.265 foi atrás de **drawback** e de **como cada uma cai** (`I` a `M`, com páginas do mangá lidas quadro a quadro) e passou o resumo por uma **verificação cega** de 118 afirmações (`N`): 85 confirmadas, 26 corrigidas.

**A v0.266 foi a rodada 1:** as frases da peça 11 que atribuíam à obra o que ela não faz — os preços "vêm da obra", o raio "da obra", a Trilha do Kusakabe, o "nunca tinha usado" e o "não para ataque físico" —, sem mexer em regra. **A v0.267 foi a rodada 2: a Cesta Oca reescrita.**

## O que a pesquisa mudou, e você precisa saber antes de propor qualquer coisa

**A premissa da revisão estava metade errada.** A seção 8.4 do rascunho da Expansão sem Barreiras diz que o domínio sem barreira "arranca o Domínio Simples em instantes". A obra mostra as duas pontas, e **a casca não é a variável — é a diferença de saída (`出力`) entre quem defende e quem abriu.** A pergunta virou "o anti-domínio mede contra a FORÇA de quem abriu", e o sistema já tem a moeda para isso nos dois lados: o refino.

**Nenhuma das quatro tem relógio próprio na obra: todas caem por fora.** Esgotamento puro nunca aparece.

**E o jeito de ceder muda de uma para outra.** A v0.264 leu `中和` como "subtração com piso" valendo para as quatro; **a verificação mostrou que a atenuação só tem cena na Extensão.** A Cesta e o Simples protegem por inteiro até cair — é limiar —, e a Pétala intercepta.

**Seis coisas a obra não amarra, e são desenho livre:** custo de energia, limite de tempo, Extensão junto com a técnica reversa, Cesta com encantamento próprio, quem usa a Pétala fora do Zenin e do Gojo, e como se aprende a Cesta.

## A Cesta Oca, que é a base da rodada 3

**Ela era a peça mais frágil do sistema** — Classe 1, sem gate, zero PE, e não quebrava; o que a segurava era só o turno gasto. **A v0.267 a reescreveu com as decisões do Mizuki:**

- **O preço são as duas mãos presas no símbolo.** Nada de arma, escudo, feitiço com Gesto ou Agarrar; andar e Desarmado, pode — *"um chute não é segurar uma arma, então ainda tem seu drawback"*.
- **Levanta com Reação quando uma Expansão abre, ou com Ação Bônus no próprio turno.**
- **Cai pelos golpes em quem segura:** um Teste de Resistência de Vigor por golpe contra a CD de quem feriu, com as falhas acumulando até **metade da Essência** (mínimo 1), como na corrida. O teste não ocupa a Concentração, e a Mão Firme não protege dele.
- **A Expansão não a quebra enquanto o símbolo está seguro.** Soltando, ela fica de pé, e cada Acerto letal conta uma falha, no máximo uma por rodada.
- **Depois de cair, levanta de novo com as falhas zeradas,** após uma recarga de metade da Essência em rodadas.
- **PE continua zero**, e o requisito do livro entrou na peça: ser Reencarnado, ou treinado em `História`.

**Medida, ela segura quase tudo cedo e cede tarde:** com um golpe por rodada, 3,0 de 3 Acertos no nível 14 e 5,6 de 6 no nível 26 para quem treina Vigor com Essência 6, e 1,2 a 1,3 para quem não treina. A tabela está na peça 11 §6.5, e sai do `conta-cesta-oca.py`, cuja regressão `R8` confere essa tabela.

## As catorze divergências

**A tabela inteira está no fim do `H`.** Depois das rodadas 1 e 2, o que ainda vale contra a peça é o que está nos Passos 2 a 4 acima: os pés e o raio do Simples, o "cai se perder a concentração" e o Acerto de golpe de corpo da Pétala, o "acerta independentemente" e o "nenhuma serve contra a incompleta" da Extensão, e como cada uma cede.

## O resto da fila, depois da revisão

**Mecânica:** ⑧ rever os inimigos e o "máximo" de cada um · ⑨ a `ficha pessoal` e a `ficha maldita`, que são trabalho do repositório da ficha e destravam o `Volume` e as dezesseis Melhorias de ritual · ⑪ o teto de atributo contra a rota `Corpo` — **medido na v0.264, e o parecer diz que as duas vertentes valem pouco pelo preço**.

**Design aberto:** a **remodelagem das invocações e do Evocador**, anunciada duas vezes e nunca começada.

**Livro:** dois pequenos — rebaixar título de exceção para negrito correndo (à mão) e a caixa de aviso lateral (pede CSS novo no `build/`).

## A ordem de fechar versão

1. **A peça dona primeiro** — aqui, a peça 11 §6.5 —, e depois toda cópia dela: o capítulo 45 do livro (`sistema/05-material/livro/manual/45-aptidoes-e-refino.md`), a peça 25 se tocar no Sem Técnica, a frase que o `conferir-expansao.py` imprime, e a linha do item 6 no `ESTADO-ATUAL`. **Procure as cópias pelo sentido, não pela redação** — a v0.266 deixou passar "não vale contra ataque físico" no livro porque a busca era por "não para ataque físico".
2. **Nome novo se confere com `conferir-nomes.py --candidatos` antes de escrever.**
3. A nota da versão no `H` e, se a conta mudou, a regressão do script da pasta de pesquisa.
4. Entrada no `logs/CHANGELOG.md` — ele é o dono da versão, e a entrada termina com a linha que aponta para o `ESTADO-ATUAL`.
5. Bump em `README.md`, `sistema/ESTADO-ATUAL.md` e `sistema/LEIA-ME.md`, e este `PROMPT-continuar.md` atualizado.
6. Os quatro builds do livro, **depois da última edição**.
7. Os 31 validadores, com `PULADA` zero.
8. `mensagem-de-commit.txt`, e o Mizuki roda o `./subir.sh` e a entrega.

## Como o Mizuki trabalha

- **Escolha de sabor é dele.** Traga as opções com o número e o trade-off já calculados, e pergunte. Rodadas curtas, nunca uma proposta grande pronta.
- **Não pergunte o que a conta responde.** Rode e mostre a tabela. **E não devolva como nova uma decisão que já está fechada.**
- **Número vem de conta rodada, nunca de intuição** — e a conta regride contra exemplo já publicado antes de medir coisa nova.
- **No chat: frase curta, uma ideia por parágrafo**, sem número de seção no meio da frase. O documento pode ser denso; a explicação não. Se ele disser que não entendeu, a resposta certa é menos detalhe, recomeçando de mais atrás.
- **Imagem de mangá em preto e branco: só se afirma o que se tem certeza.** Nada de supor. **E imagem não entra no repositório.**
- **⚠ Antes de puxar QUALQUER agente de pesquisa, pergunte e espere** — é regra dura, escrita no arquivo de instruções da pasta de trabalho (um nível acima deste repositório), e o teto é 2 a 3 por vez. **Todo agente salva o próprio arquivo ao longo do caminho, com append a cada bloco** — a rodada que escrevia só no fim morreu no `429` e perdeu tudo. **Agente não contorna proteção de acesso** (leitor embaralhado, paywall), **e quem coordena confere o arquivo do agente, não o relatório dele.**
