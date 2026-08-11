---
name: design-mecanicas-rpg
description: Projeta, critica e revisa mecânicas de RPG de mesa — resolução por dado, economia de recurso, progressão, condições, custo de poder e regras de combate. Use sempre que a conversa envolver criar ou mexer numa regra de RPG, avaliar se uma mecânica está equilibrada, decidir entre d20 e 2d6 e pool de dados, precificar uma vantagem ou desvantagem, montar progressão de personagem, ou julgar se uma habilidade proposta por jogador é justa. Use também quando o pedido não citar "mecânica" mas for isso na prática — "essa técnica tá forte demais?", "quanto devia custar essa habilidade?", "como faço o sistema não quebrar quando o personagem sobe de nível?", "posso deixar o jogador fazer X?". Serve tanto sistema novo quanto sistema já em uso.
---

# Design de mecânicas de RPG de mesa

Uma mecânica não é boa ou ruim sozinha. Ela é boa ou ruim **para uma mesa específica, com um número específico de mestres, produzindo uma sensação específica**. Este documento é o roteiro para descobrir isso antes de escrever a regra — e para não quebrar o que já funciona quando mexer nela.

## Antes de qualquer coisa: leia o contexto do projeto

Se existe documento de fundação, pitch, manual ou changelog no projeto, leia antes de propor. Sistemas em andamento carregam invariantes que não são óbvios de fora — um teto de dano, um fecho de orçamento, uma promessa de tom — e a mecânica mais elegante do mundo é inútil se quebrar um deles.

Se não existir contexto escrito, levante três coisas antes de propor qualquer número:

1. **Quantos mestres arbitram esse sistema?** Um mestre só permite regra que dependa de julgamento. Cinco ou mais exigem regra que dois estranhos apliquem igual.
2. **O que a mesa deve sentir?** Tensão, poder, impotência, esperteza. A mecânica é o meio; a sensação é o fim.
3. **O personagem persiste entre mesas ou morre no fim do arco?** Persistência entre mestres transforma progressão em problema de auditoria, não de sabor.

## As duas perguntas que resolvem a maioria dos impasses

Quando duas mecânicas parecem igualmente boas, uma delas costuma estar respondendo a outra pergunta. Duas lentes separam isso rápido.

**A quem essa mecânica serve?** Existe um vocabulário antigo — gamismo (vencer por decisão esperta), narrativismo (produzir história com peso), simulacionismo (manter o mundo coerente) — que envelheceu como teoria mas continua útil como triagem. A tese original de que cada mesa persegue uma só e que servir as três é erro foi bastante contestada, e o próprio autor a abandonou depois; não trate como lei. Use só para perceber que as duas propostas nem estavam competindo. O caso clássico: alguém defende uma regra por realismo enquanto o resto da mesa quer tensão. São objetivos diferentes, não opiniões conflitantes.

**De onde vem a sensação?** Você escreve mecânica; o jogador sente estética; entre as duas existe a dinâmica — o que de fato acontece na mesa quando gente usa a regra. A cadeia corre num sentido para quem projeta e no inverso para quem joga. Na prática isso vira uma disciplina simples: **declare a sensação antes de escrever a regra**. "Quero que o jogador hesite antes de gastar" é a sensação. A regra é o que faz a hesitação existir. Se você não consegue nomear a dinâmica que a regra cria, ainda não sabe o que está escrevendo.

## O teste de dominância

Este é o teste que mais pega problema real, e o mais fácil de esquecer.

**Duas opções que custam o mesmo precisam doer diferente. Se uma dói estritamente mais que a outra pelo mesmo preço, a mais barata é peso morto no catálogo.**

O caso canônico: uma desvantagem "você não se move neste turno" e outra "você gasta o turno inteiro", devolvendo as duas o mesmo tanto de orçamento. A segunda contém a primeira — tira o movimento *e* a ação bônus *e* a ação padrão. Ninguém escolhe a segunda por razão mecânica; ela só sobrevive por sabor. O conserto é subir o preço da que dói mais, ou dar a ela um upside que a outra não tem.

Como rodar o teste:

1. Liste as opções que competem pelo mesmo orçamento na mesma faixa de preço.
2. Para cada par, pergunte: **existe uma situação em que eu escolheria a A em vez da B?** Se não existe nenhuma, A está dominada.
3. Cuidado com o falso positivo: flexibilidade é valor. Uma opção que dói mais mas pode ser preparada num turno morto não está necessariamente dominada — ela troca dor por conveniência.
4. Quando encontrar dominância e não puder subir o preço porque o teto do sistema não permite, **dê upside em vez de preço**. Subir preço é a saída óbvia e nem sempre é a disponível.

O mesmo teste vale para vantagens: se uma habilidade cara é sempre pior que uma barata, ela nunca entra em ficha nenhuma.

## O teste do bônus automático

Segundo erro mais comum, e se disfarça bem.

**Um bônus que todo mundo tem, ou que qualquer montagem alcança sem esforço, não é bônus — é a linha de base com passos extras.**

Dois sintomas típicos:

- Uma vantagem concedida a todos os personagens por serem personagens. Não cria decisão; só infla o número base e some da conta na primeira revisão.
- Um gatilho de bônus que a montagem mais óbvia já satisfaz. Exemplo real: "se o dano final ficar até metade do teto, o efeito dura mais uma rodada" — quando a peça de controle mais barata sozinha já joga o dano exatamente em metade do teto. O bônus deixou de ser escolha e virou piso.

Como testar: **enumere as montagens legais e conte quantas ganham o bônus.** Perto de 100%, não é bônus. Perto de 0%, é decoração. O alvo saudável é um bônus que uma parte relevante das montagens alcança com esforço e uma parte pequena leva ao topo. A skill `balanceamento-simulacao` mostra como enumerar isso com código em vez de intuição.

## O filtro do multi-mestre

Quando o sistema roda em mais de uma mesa com mestres diferentes e o personagem circula entre elas, **arbitrabilidade vence elegância**. Toda regra passa por:

> Dois mestres que nunca conversaram sobre isso leem a mesma cena. Resolvem igual?

Se a resposta depende do estilo do mestre, a regra precisa de um dos três consertos:

- **Tabela.** Troque "o mestre decide quanto" por uma faixa com critério.
- **Gatilho de ficção.** Troque "o mestre pede um teste quando achar" por "quando acontece X, role". É a lição mais transferível das famílias PbtA e Forged in the Dark: a regra nasce colada a um evento da ficção que a mesa consegue apontar.
- **Pergunta de calibragem.** Quando a regra tem que ficar discricionária mesmo, dê ao mestre a pergunta certa e a régua da resposta. "Em quantas cenas por arco isso vai importar? Uma: barato. Metade: médio. Quase toda: caro. Na dúvida, caro." Isso não elimina o julgamento — padroniza a direção do erro, que é o que importa entre mesas.

Repare na última: **quando houver dúvida, erre sempre para o mesmo lado.** Vantagem customizada na dúvida sai cara; desvantagem customizada na dúvida devolve pouco. As duas erram contra o jogador, e por isso o sistema não infla com o tempo.

## Progressão: o teto vem antes da curva

Sistema com personagem persistente precisa de teto. Sem ele, um mestre não consegue escrever encontro sem ver a ficha exata, e a preparação vira negociação.

O teto pode morar em dois lugares:

- **No dado.** Pool de dados e escada de tamanho de dado saturam sozinhos: o primeiro dado adicional compra muito, o oitavo quase nada. O freio é matemático e invisível.
- **No orçamento.** Pontos por faixa, com um teto declarado. O freio é explícito e auditável.

O segundo é mais chato de escrever e melhor para muitos mestres, porque um mestre consegue conferir um orçamento e não consegue conferir uma intuição. Se o sistema for de orçamento, escreva o **contrato de invariantes** cedo — os números que precisam continuar verdadeiros depois de qualquer mudança — e trate quebra de invariante como bug, não como ajuste de sabor.

Sobre a curva do dado: **a escolha da curva e a política de bônus são uma decisão só.** Num d20 um +1 vale sempre 5 pontos percentuais. Numa curva de sino o mesmo +1 vale de 8 a 17, e vale mais no meio, que é onde quase todo teste cai. Ou seja: curva chata permite mestre improvisar bônus; curva de sino exige proibir bônus numérico improvisado e substituir por vantagem, rerrolagem ou mudança de posição. Escolher sino e deixar bônus solto entrega mesas com dificuldades diferentes sem ninguém perceber.

Números de referência em `references/matematica-de-dado.md`.

## O teste da premissa herdada

Antes de fechar a arquitetura, passe os olhos nesta lista e marque cada item como **escolhido** ou **herdado**:

- Pontos de vida como reservatório que esvazia
- Iniciativa por rodada com todo mundo agindo uma vez
- Seis atributos numéricos
- Nível inteiro que sobe de um em um
- Classe fixa escolhida na criação
- Rolagem de acerto separada da rolagem de dano
- Dano crescente como principal eixo de poder

Nenhum item é proibido. O problema não é usar — é usar sem ter percebido que decidiu. Sistemas que refinam D&D sem questionar as premissas dele têm nome na comunidade, e o nome não é elogioso; o termo original era afetuoso, mas a armadilha é real: entregar a estrutura de sempre com nomes novos e achar que inovou. Se o jogo tem uma premissa forte de ficção, cada item herdado é uma chance perdida de a mecânica dizer a mesma coisa que a ficção diz.

## O nome é parte do design

Uma peça bem desenhada com nome errado é lida errado na mesa, e o erro não aparece em teste nenhum — aparece meses depois, quando um jogador reclama que a regra "não faz o que diz". Duas checagens antes de batizar qualquer coisa:

**O termo já significa outra coisa no hobby?** Palavras como vulnerável, vantagem, resistência, condição, iniciativa, crítico e concentração carregam significado herdado de sistemas populares. "Vulnerável", por exemplo, para boa parte da mesa significa *tomar mais dano* — não "ficar mais fácil de acertar". Se a sua peça faz a segunda coisa e se chama assim, metade da mesa vai lê-la errado na primeira leitura e você gasta o resto da campanha corrigindo. Ou muda o nome, ou muda a mecânica para o que o nome já promete.

**O termo já significa outra coisa dentro do seu próprio sistema?** Mesma armadilha, um nível mais fundo. Acontece quando o sistema cresce por partes: uma palavra boa serve para o tamanho de uma habilidade e depois parece perfeita para a patente do personagem no mundo. As duas escolhas são boas isoladas; juntas, garantem confusão em toda mesa.

Nos dois casos, renomeie a mais nova ou a menos entranhada, e antes de a comunidade adotar — depois de adotado o custo multiplica. E repare: colisão raramente se resolve só trocando a palavra. Quase sempre existe uma distinção real por trás, e nomeá-la deixa o sistema melhor do que estava antes do erro.

## Quando propor uma mecânica nova

Entregue nesta ordem. A ordem importa porque os três primeiros itens matam a maioria das propostas antes de você gastar tempo nos números.

1. **A sensação.** Uma frase: o que o jogador deve sentir na hora de usar isso.
2. **O gatilho.** Quando essa regra entra em jogo, em linguagem de ficção.
3. **O que ela substitui ou complica.** Mecânica nova quase nunca é adição pura; ela compete com algo por espaço na cabeça da mesa.
4. **A regra**, no menor número de palavras que ainda a torne arbitrável por estranho.
5. **O caso padrão e uma exceção**, visualmente separados. Quem lê rápido precisa achar o caso padrão sem tropeçar na exceção.
6. **A conta**, quando houver: custo, teto, pior caso e melhor caso.
7. **O teste de dominância e o de bônus automático**, com o resultado escrito.
8. **O porquê**, curto. Vira o registro no changelog e é o que impede a decisão de ser desfeita por engano seis meses depois.

## Quando criticar uma mecânica existente

Não abra pela opinião. Abra pelo que dá para verificar.

- Rode o teste de dominância contra as vizinhas de preço.
- Rode o teste do bônus automático.
- Passe pelo filtro do multi-mestre.
- Confira contra os invariantes declarados do sistema, se houver.
- Só então diga se gosta ou não, e deixe claro que essa última parte é gosto.

Quando encontrar problema, proponha **o menor conserto que resolve**. Reescrever o subsistema inteiro é quase sempre a resposta errada — o custo real não é escrever, é revalidar tudo que dependia dele e reensinar a mesa.

## Aprovar habilidade proposta por jogador

Em sistemas com criação livre de poder, o mestre precisa de um roteiro curto ou vira negociação caso a caso:

1. **Cabe no contorno declarado da técnica ou do conceito?** Se a proposta exige esticar a definição escrita, o problema é a definição, não a proposta.
2. **Usa alguma categoria que esse personagem fechou?** Sistemas que dão identidade fechando portas precisam checar as portas.
3. **Está dentro dos limites numéricos da faixa?** Quantidade de peças, teto, devolução.
4. **Em quantas cenas isso importa?** Essa pergunta precifica quase tudo que é customizado.
5. **Dá para apontar o momento exato em que dispara?** Se dois jogadores discordariam, está mal escrita — reescreva antes de precificar.

E a regra que sustenta as outras cinco: **o mestre pode recusar mesmo quando a proposta passa em tudo.** Um checklist existe para tornar o "sim" barato, não para tornar o "não" impossível.

## Arquivos de apoio

- `references/matematica-de-dado.md` — curvas comparadas, o que vale um +1 em cada mecânica, saturação de pool, vantagem, e o que cada formato implica para progressão. Leia quando a decisão envolver escolha de dado ou precificação de bônus numérico.
- `references/vocabulario.md` — glossário curto dos termos usados aqui. Leia se algum termo não estiver claro.
