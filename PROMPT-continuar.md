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

**v0.264, commitada e no ar.** Manual do Fundamento na **v7.38**. **Vinte e sete peças de regra e vinte e sete validadores** em `sistema/03-mecanica/`, mais o `conferir-repositorio.py`, os dois de `manual/matematica/` e o `conferir-voz.py` — **31 validadores, e eles passam com `PULADAS=0`**.

Os três repositórios estão sincronizados: o sistema (`JJK---Project`), a entrega (`finalizado/`, que commita à mão) e a ficha (`Claude 3`, que é o `Ficha---RPG-JJK`).

**A v0.264 foi pesquisa de campo e NENHUM número do sistema se moveu.** Entraram `6.023` linhas em `sistema/01-pesquisa/anti-dominios/` sobre as quatro técnicas anti-domínio, mais o parecer medido da ideia 11.

## O que vem em seguida — a revisão dos quatro anti-domínio

**É o item 6 da fila, aberto desde a v0.226 por decisão do Mizuki.** A pesquisa está feita; falta a rodada de decisão. **Comece lendo `sistema/01-pesquisa/anti-dominios/H-resumo-das-quatro.md`** — ele resume as quatro e fecha com as oito divergências entre a peça 11 §6.5 e a fonte.

### O que a pesquisa mudou, e você precisa saber antes de propor qualquer coisa

**A premissa da revisão estava metade errada.** A seção `8.4` do `RASCUNHO-expansao-sem-barreira.md` diz que o domínio sem barreira "arranca o Domínio Simples em instantes". A obra mostra as duas pontas: sem casca **em potência plena** ele cai em segundos, mas sem casca e **incompleto** quatro Domínios Simples aguentaram quase 99 segundos, e dentro de domínio **fechado** o Sukuna pagou metade do corpo. **A casca não é a variável — é a diferença de saída (`出力`) entre quem defende e quem abriu.** A pergunta deixou de ser "o que fazer contra a Expansão sem Barreiras" e virou "o anti-domínio mede contra a FORÇA de quem abriu", e o sistema já tem a moeda para isso nos dois lados: o refino.

**E o mecanismo tem forma matemática, vinda da própria obra:** o termo que ela usa para o que a `Extensão de Domínio` faz é **neutralização química** — quantidade igual cancela, quantidade menor atenua. ***Não é interruptor: é subtração com piso.*** O levantamento do hobby de RPG chegou no mesmo lugar por outro caminho, com "trocar o interruptor por relógio".

### As oito divergências, em duas metades

**Quatro são conserto de fato** *(a fonte simplesmente diz outra coisa)*: o "os pés não saem do chão" é **voto da Miwa** e não da técnica; o raio de `2,21 m` é dela também, com o voto; o Kusakabe **expande o raio em combate** com a própria aptidão, e não pela Trilha; e a `Pétala` **responde ao que toca**, não a "ataque físico" — com isso a frase *"contra um Acerto que é golpe de corpo, ela não faz nada"* cai, porque Acerto corporal ainda é acerto garantido.

**Quatro são decisão de preço, e são do Mizuki**: se `中和` vira subtração com piso no sistema; se a `Extensão` passa a **diluir** o Acerto em vez de anular; se o `Domínio Simples` ganha o que a obra dá a ele (ele é **arrancável**, e a `Cesta Oca` é **sustentável**); e o que fazer com o custo da `Cesta Oca`, que na obra é **selo imposto** — o inimigo pode *querer* que você pague.

### Uma coisa que a revisão vai ter de encarar, e não é divergência

**A `Cesta Oca de Vime` é a peça mais frágil do sistema hoje:** Classe 1, sem gate, custo zero de PE, não quebra, e resolve sozinha o que as outras duas cobram caro para resolver. O que segura ela é só o turno gasto. **Mexer no preço das outras sem olhar para ela empurra todo mundo para ela.**

## O resto da fila

**Mecânica:** ⑧ rever os inimigos e o "máximo" de cada um · ⑨ a `ficha pessoal` e a `ficha maldita`, que são trabalho do repositório da ficha e destravam o `Volume` e as dezesseis Melhorias de ritual · ⑪ o teto de atributo contra a rota `Corpo` — **medido na v0.264 e o parecer diz que as duas vertentes valem pouco pelo preço**, porque o atributo entra nos dois lados da rolagem e o espelho não se move.

**Design aberto:** a **remodelagem das invocações e do Evocador**, anunciada duas vezes e nunca começada, com três pontas — as quinze entradas de catálogo com texto diferente entre livro e peça, a `Voz` cuja troca no nível 7 não muda número nenhum, e a invocação que não obedece (Rika e Mahoraga).

**Livro:** dois pequenos — rebaixar título de exceção para negrito correndo (à mão) e a caixa de aviso lateral (pede CSS novo no `build/`).

## Como o Mizuki trabalha, em cinco linhas

- **Escolha de sabor é dele.** Traga as opções com o número e o trade-off já calculados, e pergunte. Rodadas curtas, nunca uma proposta grande pronta.
- **Não pergunte o que a conta responde.** Rode e mostre a tabela.
- **Número vem de conta rodada, nunca de intuição** — e a conta regride contra exemplo já publicado antes de medir coisa nova.
- **No chat: frase curta, uma ideia por parágrafo.** O documento pode ser denso; a explicação não.
- **⚠ Antes de puxar QUALQUER agente de pesquisa, pergunte e espere** — é regra dura, escrita no arquivo de instruções da pasta de trabalho (um nível acima deste repositório), e o teto é 2 a 3 por vez. **Todo agente salva o próprio arquivo ao longo do caminho, com append a cada bloco** — a rodada que escrevia só no fim morreu no `429` e perdeu tudo.
