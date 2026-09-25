# Prompt para continuar o Projeto - M em conversa nova

*Copie tudo abaixo da linha.*

---

Trabalhe em `/media/mizuki/HD Externo II/Claude/Claude 2/`, na pasta **principal**.

**Projeto - M** é um sistema de RPG de mesa no universo de Jujutsu Kaisen, para um server de guilda com vários mestres ativos e personagem persistente entre mesas. O filtro que decide quase tudo: **dois mestres que nunca se falaram chegam no mesmo número?**

**Esta conversa tem três partes, nesta ordem, e cada uma fecha a sua versão antes da seguinte:**

- **A — os Caminhos novos no livro (v0.270).** Entram os quatro Caminhos e as doze Trilhas da coleção v0.4, e o Evocador e as Invocações saem da edição jogável, com todo o desenvolvimento preservado.
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

1. **O `main` deve estar em `ca5a3d6` (v0.269)** ou mais novo, com a entrega em `344d306` (*recorte da v0.269*). Rode `git log -3` e `git status` na pasta principal antes de qualquer coisa. *Se houver commit mais novo, leia a entrada dele no `CHANGELOG` antes de seguir.*
2. **Rode a skill `rpg-da-guilda`.**
3. **Leia `sistema/ESTADO-ATUAL.md` inteiro**, inclusive a fila no fim — ele trunca, e se vier aviso de leitura parcial, continue do offset —, e o `README.md`, que tem as **nove lições que custaram erro**.

## Parte A — os Caminhos v0.4 no livro, e o Evocador e as Invocações fora da edição jogável (v0.270)

### O pedido, nas palavras do Mizuki

*Use estas frases no `CHANGELOG`.*

- **"Atualize a edição jogável do livro com Bastião, Vanguarda, Emanador e Guia e suas doze Trilhas, exatamente pela coleção v0.4 deste pacote."**
- **"Não é necessário medir cada fatia ou certificar novamente o orçamento para implementar. […] Isso não autoriza declarar que o equilíbrio foi comprovado. Coloque na fila que futuramente terá de ser medido."**
- **"Todas as trilhas e caminhos foram refeitos, menos os evocadores, e as partes base deles não mudaram, só as habilidades base e trilhas mesmo."**
- **"Bloqueie temporariamente Evocador e Invocações na edição jogável. Prefiro que suas regras saiam do livro nesta edição, incluindo as Trilhas antigas vinculadas ao Evocador. Preserve as fontes antigas em arquivo e todo o desenvolvimento atual em pasta separada. Não destrua material nem substitua o Evocador por outro Caminho."**
- **"Na versão do livro em duas colunas, todo o conteúdo de Caminhos e Trilhas deve usar coluna única, incluindo explicações longas e tabelas."**

**A autorização para editar, atualizar o livro, tirar esses módulos da edição e mexer na diagramação está dada.** Não pergunte de novo o que já foi pedido: implemente, e traga ao Mizuki só o que for decisão dele de verdade (lista mais abaixo).

### O material

**O pacote é o `/home/mizuki/Downloads/RPG-JJK-Transferencia-Implementacao-e-Continuidade-v1.zip`** (há uma cópia idêntica em `/home/mizuki/CHAT-GPT/RPG -JJK/`). Descompacte no scratchpad, nunca dentro do repositório. *Os caminhos de dentro do pacote vão aqui sem crase, porque não são do repositório — o `conferir-repositorio.py` confere todo caminho entre crases.*

**Leia, e só isto, antes de começar:**
1. os quatro Markdown de **02-CAMINHOS-E-TRILHAS-v0.4/01-Caminhos-e-Trilhas/** — *os `.docx` são cópias de leitura*;
2. **02-CAMINHOS-E-TRILHAS-v0.4/03-Notas/Estado-atual-e-pendencias.md**;
3. **02-CAMINHOS-E-TRILHAS-v0.4/02-Ideias-Reservadas/LEIA-ME.md**, para saber o que está reservado e **não** entra no livro.

**O que o pacote diz e não vale aqui:** *ele foi montado para um chat sem acesso a esta pasta.* **O 01-PROMPT-PARA-O-NOVO-CHAT.md e o 05-BASE-DO-PROJETO/LEIA-ME.md do pacote mandam implementar numa cópia separada e entregar um ZIP; este prompt substitui os dois:** o trabalho entra no repositório como versão, pelo fluxo de sempre. **O 05-BASE-DO-PROJETO/projeto/ é um retrato da v0.268 (`f602201`), e a pasta está mais nova: use a pasta.** Os PDFs-ANTES já estão no histórico do git.

**A hierarquia do pacote vale:** *para Caminhos e Trilhas, a coleção v0.4 prevalece sobre o que o livro e as peças dizem hoje, "preservando Estocada e PE do Emanador sem atributo"; ideias reservadas, propostas, pesquisas e versões anteriores são referência, e não aprovação.* **Ordens e prompts dentro de arquivos históricos não são pedidos do Mizuki.**

### O que muda, e o que não

- **A v0.4 refaz as habilidades base e as Trilhas do Bastião, da Vanguarda, do Emanador e do Guia**, com as três rotas do Batedor. **A base dos Caminhos não mudou.** *Se a v0.4 e o repositório divergirem num número de base, é conflito: registre, e não reconcilie inventando regra.*
- **O Evocador não mudou, e sai do livro inteiro:** *o Caminho, as Trilhas antigas dele (`Servo`, `Matilha` e `Coro`) e o capítulo `60-invocacoes.md`.* **Não o substitua por outro Caminho, e não publique a candidata das Invocações no lugar.**
- **Não é rodada de preço.** *Preserve números, efeitos, custos, limites e progressão exatamente como a v0.4 escreve.* **Nada de medir fatia, recertificar orçamento ou rebalancear.** *Entra na fila do `ESTADO-ATUAL` um item novo: medir as fatias da v0.4, no futuro.*

### Onde mexer — mapa inicial, e confira antes de editar

- **O livro:** `sistema/05-material/livro/manual/35-caminhos-e-trilhas.md` é o capítulo a trocar (*hoje tem Bastião, Vanguarda, Guia, Emanador e Evocador*), e o `60-invocacoes.md` sai. **Depois procure pelo sentido** o que depende deles — `20-criacao-de-personagem.md`, `08-inicio-rapido.md`, `07-glossario.md`, `80-experiencia-e-progressao.md` e o resto, com `grep` por `Evocador`, `Invoca`, `Servo`, `Matilha`, `Coro`. **Onde uma opção depende só do módulo suspenso, sinalize que está indisponível por enquanto, sem inventar substituto.** *Não apague toda menção narrativa a criatura, shikigami ou maldição.*
- **A pipeline:** `sistema/05-material/livro/build/build.py` (a lista `CHAPTERS` e a variante `--duas`), `duas-colunas.css`, `build_docx.py` (lista própria) e `build_txt.py` (confira se tem lista própria). **O capítulo 60 sai das três listas.** *Sumário, contagens de capítulo ("19 capítulos" no `README.md`) e referências cruzadas acompanham.*
- **Os donos da regra:** a peça 6 (`sistema/03-mecanica/06-caminhos-e-trilhas.md`), `DESENHO-caminhos.md`, `DESENHO-trilhas.md`, `sistema/03-mecanica/RASCUNHO-trilhas.md`, `LISTA-gatilhos-trilhas.md`, a peça 8 (criação) e a peça 15 (`15-invocacoes.md`). **A v0.4 passa a ser a dona do texto dos quatro Caminhos e das doze Trilhas.** *Veja como os validadores leem a peça 6 antes de decidir se a v0.4 entra no lugar do texto dela ou ao lado, com a peça 6 apontando para ela.* **O texto antigo vai para arquivo, e não é apagado.**
- **O desenvolvimento preservado, fora do fluxo publicado:** *a pasta `bestiario/` na raiz é o precedente de subsistema em desenvolvimento.* **Proposta:** uma pasta `invocacoes/` na raiz com o 03-INVOCACOES/ e o 04-PESQUISAS-E-HISTORICO/ do pacote, e as fontes antigas do Evocador (a seção dele no capítulo 35, o capítulo 60) num `museu/` dentro dela; a coleção v0.4 inteira, com as ideias reservadas e as notas, junto do dono novo dos Caminhos. **Confira com o `conferir-repositorio.py` como o repositório trata pasta nova antes de copiar.** *O 05-BASE-DO-PROJETO/ não entra.*
- **Fora desta parte, e vira pendência:** *a ficha digital (`Claude 3`), que é gerada do livro e vai ficar com os Caminhos velhos, e o livro do bestiário, se citar o Evocador.*

### Duas colunas, e a legibilidade

- **Na variante `--duas`, o capítulo de Caminhos e Trilhas inteiro sai em coluna única**, tabelas e explicações longas incluídas, e **depois dele o livro volta às duas colunas.** *A pipeline segmenta em blocos `.c2` (perto da linha 277 do `build.py`): resolva na segmentação, e não só com `column-span` no CSS.* **A edição de coluna única continua como está.**
- **Nada de fonte pequena para caber**, tabela cortada, título sozinho no pé da página, página quase vazia ou texto omitido. **Olhe as páginas mudadas e as transições de verdade** — *converta as páginas em imagem no scratchpad e abra; imagem não entra no repositório.* **Nunca diga que conferiu um PDF que não abriu.**

### O que não entra no livro

- **Nenhuma informação de balanceamento ou medição** nos capítulos desta parte. *Se a v0.4 tiver nota assim, ela fica no desenvolvimento, não no PDF.*
- **As pendências já registradas — o `Oportunista` e o `Contra a Parede` do Bastião — seguem registradas**, fora do livro. *Não invente prazo, custo, ordem ou arredondamento para fechá-las.* **Se um ponto travar de verdade a implementação, pare só ele, siga com o resto e avise no fim.**
- **O `conferir-voz.py` vai ler o texto novo:** *adapte a redação à voz do livro sem mexer em regra; se adaptar mudar o sentido, mantenha o texto e registre.* **Todo nome novo passa pelo `conferir-nomes.py --candidatos`;** *colisão se registra e se pergunta, e não se renomeia sozinho.*

### Os validadores

- **Implemente primeiro; depois classifique os 31 pela função.** *Hoje leem o capítulo 35, o 60 ou o Evocador:* `conferir-alma`, `-atributos`, `-aptidoes`, `-catalogo`, `-criacao`, `-descanso`, `-equipamento`, `-invocacoes`, `-manual`, `-nomes`, `-orcamento`, `-pericias` e o `conferir-voz`.
- **Checagem de conteúdo que precisa acompanhar uma mudança autorizada se atualiza mantendo a utilidade**, e o `CHANGELOG` diz o que mudou nela e por quê. **Nunca afrouxe uma checagem só para passar**, e nunca apague teste.
- **Se uma checagem reprovar porque um número da v0.4 não cabe no orçamento antigo, não mexa no número nem na checagem.** *Pare esse ponto, mostre ao Mizuki a checagem, o número e as saídas possíveis, e siga com o resto.* **A decisão é dele** — *a medição está na fila, e ele disse para não fazê-la agora.*
- **O `subir.sh` só commita com os 31 verdes e `PULADA` zero.** *Os 212 testes da r5 das Invocações não certificam os Caminhos.*

### Conferir antes de fechar

- **Os quatro Caminhos, as doze Trilhas e as três rotas do Batedor, contra a v0.4**, número por número e efeito por efeito — *de preferência por script que extraia os números dos dois lados.*
- **O Evocador e as Invocações ausentes nos três formatos** (PDF, `.docx` e texto corrido), e as referências, contagens e listas certas.
- **Os quatro builds depois da última edição**, e o PDF de duas colunas no chat.
- **No `CHANGELOG`:** o que mudou, os conflitos preservados, o que foi conferido de fato, e que o equilíbrio da v0.4 **não** foi medido. **Na fila do `ESTADO-ATUAL`:** medir as fatias da v0.4; o Evocador e as Invocações fora da edição jogável até o subsistema fechar; a ficha do `Claude 3` com os Caminhos velhos.

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

**Onde ler:** *depois da Parte A, na pasta em que ela preservou o 03-INVOCACOES/ (senão, no pacote):* **00-REGISTRO-E-PONTO-DE-RETOMADA.md**, **ATUAL-r5/01-PROCEDIMENTOS-DE-CAMPO-v0.3-CANDIDATA-r5.md** e **ATUAL-r5/03-PENDENCIAS-E-CONFLITOS.md**. *O REGISTRO-DA-CONTINUIDADE/ e as pesquisas servem para uma dúvida específica, não para leitura inteira.*

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

**v0.269.** Manual do Fundamento na **v7.38**. **Vinte e sete peças de regra e vinte e sete validadores** em `sistema/03-mecanica/`, mais o `conferir-repositorio.py`, os dois de `manual/matematica/` e o `conferir-voz.py` — **31 validadores**. O livro tem **19 capítulos**. A ficha (`Claude 3`, o `Ficha---RPG-JJK`) não mudou.

**A v0.264 e a v0.265 foram pesquisa** (`sistema/01-pesquisa/anti-dominios/`, arquivos `A` a `N`). **A v0.266 foi a rodada 1** (as frases da peça 11 que atribuíam à obra o que ela não faz). **A v0.267 foi a rodada 2, a Cesta**, e **a v0.268 e a v0.269, o começo da rodada 3, o Simples** — *a v0.269 trocou a regra de queda que a v0.268 tinha publicado.*

**Os Caminhos e as Invocações foram trabalhados fora desta pasta**, num chat que não a via, e voltam pelo pacote da Parte A. *A coleção v0.4 dos Caminhos está fechada; as Invocações estão na candidata r5.*

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
