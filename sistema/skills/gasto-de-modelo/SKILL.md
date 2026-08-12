---
name: gasto-de-modelo
description: Fecha a resposta com uma linha dizendo se a tarefa pedia o modelo em que ela foi aberta, ou um mais barato. Use em toda conversa de trabalho do Mizuki — leitura de arquivo, escrita de documento, decisão de design, depuração — classificando o que foi feito de verdade, não o que parecia difícil no começo. Não use em conversa curta, pergunta factual ou bate-papo.
---

# Gasto de modelo — o veredito de uma linha

O Mizuki abre quase tudo no modelo mais caro por receio de subdimensionar, e desconfia que está desperdiçando. **O desperdício real não está em pensar caro — está em ler caro.** Uma sessão típica dele é metade `cat`, `grep`, rodar validador e conferir número que já existe, e essa metade não distingue modelo nenhum.

Esta skill fecha a resposta com **uma linha**, no fim, dizendo o que a tarefa pedia.

## A classificação

Julgue **o que foi feito**, não o que parecia difícil quando a conversa abriu. Uma pergunta que soava complexa e terminou em três `grep` era tarefa de leitura.

| a tarefa foi | o que ela pede | sinal |
|---|---|---|
| **Leitura e execução** | o modelo mais barato | listar arquivo, rodar script pronto, extrair trecho, conferir se número bate, responder o que está escrito |
| **Escrita e revisão** | o do meio | redigir seção, catálogo, changelog, reescrever texto, revisar prosa contra critério |
| **Decisão e cruzamento** | o mais caro | régua nova, achar contradição entre documentos que ninguém cruzou, precificar mecânica, desenhar validador, revisão cética contra a própria proposta |

**A fronteira que mais engana é entre as duas últimas.** Escrever um catálogo aplicando régua já fechada é escrita. Descobrir que a régua reprova três entradas já escritas é decisão.

## A linha

No fim da resposta, sozinha, depois de tudo:

```
↳ Isso foi <categoria>. <Modelo> daria conta. / <Modelo> foi a escolha certa.
```

**Curta e sem justificativa.** Se a categoria mudou no meio — abriu como leitura e virou decisão —, diga isso em vez de escolher uma: *"abriu como leitura e virou decisão no meio; o caro se pagou."*

**E quando o modelo aberto foi o certo, diga.** Uma skill que só reclama vira ruído e ele para de ler.

## Preço: confira, não decore

Preço de modelo muda, e a razão entre eles muda junto. **Busque a tabela atual antes de citar valor** — não escreva número de memória aqui nem na resposta.

O que vale carregar é a forma, não os valores: a diferença entre as faixas é de **poucas vezes**, não de ordem de grandeza. Isso importa porque o receio dele é baseado na intuição contrária — e uma tarefa de decisão feita no modelo errado custa uma sessão inteira de retrabalho, que é mais caro que qualquer diferença de token.

## Quando não emitir a linha

- Conversa curta, pergunta factual, bate-papo.
- Quando a resposta já é ruim e a linha vira desculpa.
- Duas vezes seguidas com o mesmo veredito sem nada ter mudado — repetir a mesma linha três respostas seguidas transforma ela em rodapé, e rodapé ninguém lê.

## O limite desta skill, dito na cara

**Ela dispara por gatilho, não por relógio.** Vai falhar em algumas respostas, e não existe jeito de garantir que apareça em todas — isso foi acordado quando ela foi criada. Se a linha sumir por várias respostas seguidas num trabalho longo, o gatilho está fraco para aquele tipo de tarefa, e a descrição da skill é o que precisa mudar.
