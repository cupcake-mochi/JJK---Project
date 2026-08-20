---
name: arquitetura-de-manual-rpg
description: Decide a estrutura de um manual de RPG de mesa inteiro antes da prosa entrar — ordem de capítulo, onde mora conteúdo de mestre, como rotular regra opcional, e como formatar um catálogo grande (talentos, itens, monstros, poderes) para ficar navegável. Toda recomendação vem de pesquisa direta em livros publicados (D&D, GURPS, 3D&T, Tasha's Cauldron, Volo's Guide), citados por nome e página, nunca de memória solta. Use sempre que for planejar a estrutura de um manual, capítulo ou suplemento do zero, decidir onde um catálogo grande deveria morar e como agrupar entradas, marcar regra opcional/variante, separar conteúdo de mestre do de jogador, ou perguntar "como sistemas publicados resolvem isso?". Use também para "por onde eu começo a escrever o manual?", "como organizo esse catálogo de 80 itens?", "isso devia ser capítulo separado?". Depois da estrutura decidida, a `redacao-acessivel-rpg` cuida da prosa. Nunca dispara para decidir número de regra ou mecânica — isso é `design-mecanicas-rpg`.
---

# Arquitetura de manual de RPG

Decisão de estrutura vem **antes** de decisão de frase. Um capítulo bem organizado com prosa mediana funciona; um capítulo bem escrito na ordem errada não. Esta skill decide a arquitetura — a `redacao-acessivel-rpg` decide a frase depois.

Toda recomendação aqui foi extraída de livros publicados de verdade, lidos e citados por página em `references/anatomia-comparada.md`. Se uma recomendação parecer estranha pro seu caso, abra a fonte antes de descartar — e se o seu caso não estiver coberto por nenhum dos livros pesquisados, isso é sinal para pesquisar mais (veja a skill `pesquisa-antes-de-propor`, se ela existir no seu projeto), não para inventar.

**Esta skill mira o manual completo, não um panfleto.** Se o objetivo é um PDF que vai ser publicado e compartilhado de verdade, o modelo principal são os seis livros de produção grande — D&D, GURPS, os suplementos —, não os dois minimalistas. Cairn e Mausritter (seção 0 da pesquisa) entram só como prova de que separação jogador/mestre e índice de referência não são luxo de editora grande: eles valem em qualquer escala, mas isso não é convite pra cortar escopo. "É só um projeto pequeno" não é motivo pra pular decisão de arquitetura — é motivo pra não ter equipe de diagramação fazendo isso por você, o que já está coberto nos achados que citam o gerador Node.

## Passo 0 — confira o número contra a fonte, sempre, antes de decidir qualquer estrutura

Toda decisão de arquitetura depende de contagem: quantas entradas tem o catálogo, quantas categorias, quantos formatos diferentes. **Antes de desenhar a estrutura em cima de um número, confira esse número no documento fonte — nunca confie no número que veio no pedido, nem no que parece óbvio.** Um pedido pode errar a contagem sem querer, e uma estrutura elegante desenhada em cima do número errado ainda está errada, só que de um jeito mais difícil de notar depois.

Isso já aconteceu de verdade: um teste desta skill recebeu um pedido que dizia "9 Origens" e produziu uma arquitetura inteira de "9 capítulos internos" sem checar — a fonte dizia, na terceira linha do documento, "sete listas de Origem, mais o Sem Técnica". A versão que não usou a skill nenhuma pegou o erro porque parou pra conferir antes de desenhar; a versão que usou a skill tinha o método certo e mesmo assim carregou o número errado do início ao fim. **Ter o método não substitui checar o fato.** Trate qualquer contagem — de entradas, categorias, subtipos — como algo a verificar por leitura direta da fonte, não como dado de entrada confiável.

## O que decidir, antes de escrever qualquer capítulo

Cinco perguntas, nesta ordem — cada uma trava a próxima, e todas presumem que o Passo 0 já foi feito:

### 1. Onde mora o conteúdo de mestre?

Nunca intercalado frase a frase com regra de jogador. As opções, da mais separada pra menos:
- **Livro/documento inteiro à parte** (D&D: Livro do Jogador vs. Guia do Mestre) — escolha isso se o material de mestre for grande o bastante pra ter vida própria, e se existir risco de spoiler (item mágico secreto, ficha de vilão) que o jogador não deveria ler.
- **Parte interna claramente demarcada, mesmo documento** (GURPS: "Livro 1 — Personagens" / "Livro 2 — Campanhas") — escolha isso se o material for menor ou se o projeto preferir um documento só.
- **Capítulo por último** (3D&T: "O Mestre" é o capítulo final) — a opção mais simples, funciona bem quando o material de mestre é pouco.

O que **não** fazer: espalhar "nota para o mestre" em caixas dentro do capítulo do jogador, seção após seção. No máximo uma seção simétrica curta ("Sendo Jogador" / "Sendo Mestre") no capítulo 1, pra dar contexto dos dois papéis — não substitui a separação de verdade.

**Isso não é luxo de produção grande.** Cairn (sistema minimalista, licença livre) faz a mesma separação com dois livretos de ~24 páginas cada; Mausritter faz a fronteira interna num livro de 48 páginas só. "É pequeno demais pra separar" não é motivo válido — veja a seção 0 de `references/anatomia-comparada.md`.

### 2. Existe um conceito central que tudo depende? Ele tem glossário-ponte?

Se o sistema tem uma "moeda" ou eixo que todo o resto usa (pontos no GURPS; aqui, possivelmente "refino" ou o eixo do Fundamento), ele precisa de uma definição de uma linha, com referência cruzada, **antes** do capítulo técnico que o explica de verdade — não só a definição embutida na primeira aparição dentro daquele capítulo. GURPS resolve isso num glossário-ponte na introdução (p.7), separado do glossário completo do fim.

### 3. Como uma entrada de catálogo é formatada, e isso escala com o quão matemático o sistema é?

Decida os campos fixos de CADA TIPO de entrada (uma técnica não tem os mesmos campos que um item; um Legado não tem os mesmos campos que uma arma) e escreva um bloco curto "Como Ler uma [Tipo]" antes da primeira entrada real da lista — nomeando os campos na ordem exata em que vão aparecer. Nunca repita os rótulos entrada por entrada; a ordem fixa já ensina.

A rigidez do formato deve escalar com quanto o sistema é matemático: um catálogo de orçamento de pontos pede tabela e ordem de campo fixa (GURPS, D&D); um catálogo mais narrativo tolera prosa solta que mistura flavor e regra (3D&T). Sistemas de orçamento de pontos — que é o caso mais comum de quem usa esta skill — devem puxar pro lado rígido.

### 4. O catálogo é grande (50+ entradas parecidas)? Ele precisa de índice duplo e convenção de variante.

Catálogo grande não é só "muitas entradas do mesmo formato" — é um problema de **navegação**, separado do problema de formato de entrada. Quando isso acontece:
- **Agrupe por categoria funcional**, não só alfabético (o Guia do Volo agrupa bestiário por família de monstro; um catálogo de técnicas poderia agrupar por escola/tipo).
- **Escreva um índice duplo**: uma lista rápida A-Z (nome → onde está) logo antes do catálogo, **e** uma segunda lista reindexando pelo eixo que o leitor realmente usa pra procurar na mesa (nível, custo, categoria — o que for equivalente ao "ND/tipo/ambiente" do bestiário).
- **Documente variante como base + delta**: se duas entradas são quase a mesma coisa, não reescreva a segunda inteira — escreva a diferença, com um ponteiro explícito de volta pra base ("mesma regra de X, exceto que...").
- **Repita o mesmo esqueleto de subseção em toda categoria** — depois que o leitor aprende a navegar uma categoria, ele já sabe navegar todas as outras.

### 5. Como uma regra opcional/variante é marcada, e em que nível da hierarquia?

O nível do aviso deve casar com o tamanho do escopo:
- **O livro inteiro é opcional** → uma declaração, uma vez, na abertura (Tasha's: "Tudo neste livro é opcional"). Não repita em cada capítulo.
- **Um sistema/capítulo inteiro é opcional dentro de um livro core** → rótulo indexado desde o **sumário**, não só no meio do texto (GURPS: "Regra Opcional:" aparece literalmente no índice).
- **Uma variação pontual dentro de uma regra** → convenção tipográfica fixa e repetida (D&D DMG: "VARIAÇÃO:"), sempre com um exemplo numérico mostrando a variação funcionando.

Quando uma opção depende de outra regra opcional já existir na mesa, a dependência fica **local**, no ponto exato de uso ("se seu grupo usa X..."), nunca só declarada lá no início do livro e esquecida.

## Depois da estrutura decidida

A prosa de cada seção — jargão, exemplo, voz, corte de texto de máquina — é trabalho da `redacao-acessivel-rpg`. Esta skill para na arquitetura; não escreva a frase final aqui.

Se a estrutura decidida aqui gerar uma dúvida que nenhum dos seis livros em `references/anatomia-comparada.md` responde, isso é sinal de pesquisar mais uma fonte, não de decidir no chute — sistemas publicados existem aos milhares, e a resposta provavelmente já foi resolvida por algum deles.

## Arquivos

- `references/anatomia-comparada.md` — os achados completos, por eixo de decisão, cada um citando o livro e a página de onde veio. Leia antes de aplicar qualquer recomendação num caso concreto, porque o arquivo tem a nuance e a ressalva que o resumo aqui não cobre.
