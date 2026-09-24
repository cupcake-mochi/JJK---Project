# Prompt para continuar o Projeto - M em conversa nova

*Copie tudo abaixo da linha.*

---

Trabalhe em `/media/mizuki/HD Externo II/Claude/Claude 2/`.

**Projeto - M** é um sistema de RPG de mesa no universo de Jujutsu Kaisen, para um server de guilda com vários mestres ativos e personagem persistente entre mesas. O filtro que decide quase tudo: **dois mestres que nunca se falaram chegam no mesmo número?**

## Leia nesta ordem antes de mexer em qualquer coisa

1. `sistema/ESTADO-ATUAL.md` — onde parou e o que vem em seguida. **Leia inteiro**, inclusive a fila no fim
2. `README.md` — as **nove lições que custaram erro**, e elas moram só lá
3. `logs/CHANGELOG.md` — a entrada do topo carrega o **porquê**, que é a única parte que não dá para reconstruir lendo o resto
4. A peça de `sistema/03-mecanica/` que for mexer

E rode a skill `rpg-da-guilda` antes de começar: ela tem o procedimento — ordem de leitura, validadores, triagem de nome, arnês de perturbação e como fechar versão.

## Onde está o projeto agora

**v0.266, commitada no branch `claude/jjk-anti-dominios-research-59hjly` — ainda NÃO no `main`.** Manual do Fundamento na **v7.38**. **Vinte e sete peças de regra e vinte e sete validadores** em `sistema/03-mecanica/`, mais o `conferir-repositorio.py`, os dois de `manual/matematica/` e o `conferir-voz.py` — **31 validadores**. *A v0.265 e a v0.266 foram fechadas numa sessão na nuvem, sem a `finalizado/`: lá o `conferir-repositorio.py` reprovou só por não achar a pasta da entrega, e os outros 30 passaram.* **Rode o `subir.sh` na pasta de trabalho antes de confiar no verde.**

**⚠ Os três repositórios NÃO estão sincronizados:** a v0.264, a v0.265 e a v0.266 moram só naquele branch. Falta trazer para o `main`, para a pasta de trabalho e para o Project. A ficha (`Claude 3`, o `Ficha---RPG-JJK`) não mudou; a entrega (`finalizado/`) fica atrás nas peças 11 e 25 até o próximo `subir.sh`.

**A v0.264 e a v0.265 foram pesquisa, e NENHUM número do sistema se moveu.** A v0.264 levantou as quatro técnicas anti-domínio em `sistema/01-pesquisa/anti-dominios/` (arquivos `A` a `H`) e mediu a ideia 11. A v0.265 foi atrás de **drawback** e de **como cada uma cai** (`I` a `M`, com páginas do mangá lidas quadro a quadro) e passou o resumo por uma **verificação cega** (`N`).

## O que vem em seguida — a revisão dos quatro anti-domínio

**É o item 6 da fila, aberto desde a v0.226 por decisão do Mizuki.** A pesquisa está feita e conferida; falta a rodada de decisão. **Comece lendo `sistema/01-pesquisa/anti-dominios/H-resumo-das-quatro.md`** — ele resume as quatro, diz como cada uma cai, e fecha com as **catorze** divergências entre a peça 11 §6.5 e a fonte.

### O que a pesquisa mudou, e você precisa saber antes de propor qualquer coisa

**A premissa da revisão estava metade errada.** A seção `8.4` do `RASCUNHO-expansao-sem-barreira.md` diz que o domínio sem barreira "arranca o Domínio Simples em instantes". A obra mostra as duas pontas: sem casca **em potência plena** ele cai em segundos, mas sem casca e **incompleto** quatro Domínios Simples aguentaram quase 99 segundos, e dentro de domínio **fechado** o Sukuna pagou metade do corpo. **A casca não é a variável — é a diferença de saída (`出力`) entre quem defende e quem abriu.** A pergunta virou "o anti-domínio mede contra a FORÇA de quem abriu", e o sistema já tem a moeda para isso nos dois lados: o refino.

**Nenhuma das quatro tem relógio próprio na obra: todas caem por fora.** A `Cesta Oca` racha sob golpe no dono e é largada para o golpe grande; o `Domínio Simples` cai pela pressão do domínio — nunca por golpe no dono dentro de domínio — ou pelo voto do usuário; a `Pétala` cai com soco comum do dono do domínio (pelo anime e pelo efeito — o mangá não diz com palavras); a `Extensão` é largada para usar a técnica.

**⚠ E o jeito de ceder muda de uma para outra — isto corrige a v0.264.** A v0.264 leu `中和` como "subtração com piso" valendo para as quatro. **A verificação mostrou que a atenuação só tem cena na `Extensão`** (o Vermelho passa mitigado, cap. 232). **A `Cesta Oca` e o `Domínio Simples` protegem por inteiro até cair** — é limiar —, e a `Pétala` intercepta. *O "trocar o interruptor por relógio" do levantamento do hobby continua sendo uma opção de desenho; o que caiu foi a ideia de que a obra já faz isso nas quatro.*

**E seis coisas a obra não amarra:** custo de energia, limite de tempo, `Extensão` junto com a técnica reversa, `Cesta Oca` com encantamento próprio, quem usa a `Pétala` fora do Zenin e do Gojo, e como se aprende a `Cesta Oca`. **São desenho livre.**

### As catorze divergências, em duas metades

**A rodada 1 saiu na v0.266:** *as frases que a peça 11 atribuía à obra sem base — os preços "vêm da obra", o raio "da obra", a Trilha do Kusakabe, o "nunca tinha usado" e o "não para ataque físico" — foram corrigidas, sem mexer em regra.* **A rodada 2 começa pela `Cesta Oca`.**

**Conserto de fato** *(a fonte simplesmente diz outra coisa)*:
- o "os pés não saem do chão" é **voto da Miwa** e não da técnica — e a obra diz "do **ponto** onde foi ativado", não "do chão";
- o raio de `2,21 m` é dela também, com o voto;
- o Kusakabe **expande o raio em combate** com a própria aptidão, e não pela Trilha;
- a `Pétala` responde ao **acerto garantido que toca**, não a "ataque físico" — e a frase *"contra um Acerto que é golpe de corpo, ela não faz nada"* cai;
- e **seis frases que a peça atribui à obra e a obra desmente**: a `Cesta Oca` "não faz mais nada" e "não quebra"; a `Pétala` "cai se perder a concentração" e o Gojo "nunca tinha usado"; a `Extensão` "acerta independentemente da técnica do alvo" (frase da wiki, não do Fanbook); e "nenhuma serve contra a incompleta" valendo para a `Extensão`.

**Decisão de preço, e é do Mizuki**: como cada uma cede (limiar na `Cesta Oca` e no `Domínio Simples`, atenuação só na `Extensão`); o que a `Extensão` faz contra o Acerto de domínio (o Fanbook diz que neutraliza, e a obra não tem cena); o que separa `Domínio Simples` e `Cesta Oca`; e o custo da `Cesta Oca`, que na obra é **selo imposto** — o inimigo pode *querer* que você pague.

### Uma coisa que a revisão vai ter de encarar, e não é divergência

**A `Cesta Oca de Vime` é a peça mais frágil do sistema hoje:** Classe 1, sem gate, custo zero de PE, não quebra, e resolve sozinha o que as outras duas cobram caro para resolver. O que segura ela é só o turno gasto. **Mexer no preço das outras sem olhar para ela empurra todo mundo para ela.** *E a obra dá dois custos que a peça 11 não cobra: ela **racha** sob golpe no dono, e **veta o golpe grande** do próprio dono enquanto está de pé.*

## O resto da fila

**Mecânica:** ⑧ rever os inimigos e o "máximo" de cada um · ⑨ a `ficha pessoal` e a `ficha maldita`, que são trabalho do repositório da ficha e destravam o `Volume` e as dezesseis Melhorias de ritual · ⑪ o teto de atributo contra a rota `Corpo` — **medido na v0.264 e o parecer diz que as duas vertentes valem pouco pelo preço**, porque o atributo entra nos dois lados da rolagem e o espelho não se move.

**Design aberto:** a **remodelagem das invocações e do Evocador**, anunciada duas vezes e nunca começada, com três pontas — as quinze entradas de catálogo com texto diferente entre livro e peça, a `Voz` cuja troca no nível 7 não muda número nenhum, e a invocação que não obedece (Rika e Mahoraga).

**Livro:** dois pequenos — rebaixar título de exceção para negrito correndo (à mão) e a caixa de aviso lateral (pede CSS novo no `build/`).

## Como o Mizuki trabalha, em cinco linhas

- **Escolha de sabor é dele.** Traga as opções com o número e o trade-off já calculados, e pergunte. Rodadas curtas, nunca uma proposta grande pronta.
- **Não pergunte o que a conta responde.** Rode e mostre a tabela.
- **Número vem de conta rodada, nunca de intuição** — e a conta regride contra exemplo já publicado antes de medir coisa nova.
- **No chat: frase curta, uma ideia por parágrafo.** O documento pode ser denso; a explicação não.
- **⚠ Antes de puxar QUALQUER agente de pesquisa, pergunte e espere** — é regra dura, escrita no arquivo de instruções da pasta de trabalho (um nível acima deste repositório), e o teto é 2 a 3 por vez. **Todo agente salva o próprio arquivo ao longo do caminho, com append a cada bloco** — a rodada que escrevia só no fim morreu no `429` e perdeu tudo. **Agente não contorna proteção de acesso** (leitor embaralhado, paywall), **e quem coordena confere o arquivo do agente, não o relatório dele.**
