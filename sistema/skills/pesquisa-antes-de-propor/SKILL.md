---
name: pesquisa-antes-de-propor
description: Obriga levantamento externo — web, fóruns, texto de regra de outros sistemas, documentação oficial de ferramenta, fonte primária de lore — antes de propor mecânica, número, nome, conserto de ferramenta ou afirmação sobre canon. Use sempre que a resposta fosse conter algo que você não calculou dos documentos do projeto: como outro sistema resolve o mesmo problema, qual o modo de falha documentado dele, o que uma biblioteca faz de verdade, o que o material original diz. Use também quando a pergunta parecer respondível de cabeça — é justamente aí que ela falha. Não use para número que um documento do projeto já é dono.
---

# Pesquisa antes de propor

O defeito é específico e não é preguiça: **quando o contexto é rico, "eu já tenho o suficiente" fica verdadeiro por dentro.** Um repositório com 100 mil palavras de argumento, changelog e peça de regra dá material para responder qualquer coisa com confiança — e a resposta sai coerente, bem escrita e ancorada em nada fora dela mesma.

Isso é diferente de errar. Uma proposta feita só do que está em contexto costuma estar **certa e pequena**: ela resolve o problema do jeito que o próprio projeto já resolve os outros, e nunca descobre que três sistemas publicados já bateram nessa parede e sabem exatamente por onde ela quebra.

Esta skill existe para tornar a busca **obrigatória em casos nomeados**, em vez de opcional. Lembrete não dispara; gatilho dispara.

---

## 1. O gatilho — o que obriga a busca

Antes de entregar, olhe o que você ia escrever. **Se contiver qualquer um destes, você não pode entregar sem ter procurado:**

1. **"Sistema X faz assim."** Qualquer afirmação sobre outro jogo — regra, preço, curva, condição. Inclui o que você "lembra" de D&D, PbtA, Blades, Pathfinder, Daggerheart, Cairn.
2. **"O modo de falha conhecido disso é…"** Se você está atribuindo um defeito documentado a uma mecânica, o documento existe ou não existe.
3. **Canon.** Qualquer afirmação sobre o material original — o que uma técnica faz, quem venceu o quê, o que a obra estabelece como regra do mundo.
4. **Comportamento de ferramenta.** O que uma biblioteca, um formato ou uma API faz. Nunca deduza de nome de função.
5. **Um nome que você vai adotar.** Além da triagem interna, o termo carrega significado herdado do hobby, e isso mora fora do repositório.
6. **"Ninguém resolve isso"** ou **"não tem jeito"**. Essa frase é quase sempre falsa e é a mais barata de derrubar com dez minutos de busca.
7. **Um problema de ambiente que já custou tempo duas vezes.** Se você contornou a mesma coisa duas vezes, pare de contornar e vá procurar a causa.

Um único item da lista já obriga. **E procure antes de escrever a proposta, não depois** — buscar depois vira caça a fonte que concorda com o que você já decidiu, que é o pior dos dois mundos.

## 2. O que NÃO obriga, e isso importa tanto quanto

**Número que um documento do projeto é dono não se pesquisa na internet.** Ele se lê do dono. Buscar fora um valor que o repositório já fixou cria uma segunda fonte para o mesmo número — que é exatamente o defeito que o projeto mais paga para evitar.

Também não obriga:

- Conta que você mesmo pode rodar. Dominância, deriva, teto, distribuição de dado: escreva o script.
- Escolha de sabor. Quantos itens, quais, como se chamam — isso é do dono do projeto, e nenhuma fonte externa decide por ele.
- O que a ficção do projeto já decidiu para si.

**A pesquisa entra onde o projeto não tem autoridade sobre a resposta.** Onde ele tem, a autoridade é dele.

## 3. Onde procurar, por domínio

Ordem importa: **texto de regra primeiro, discussão depois.** Fórum é bom para descobrir *que* existe um problema e péssimo para saber o que a regra diz.

### Mecânica de RPG — o que outro sistema faz

| fonte | serve para | não serve para |
|---|---|---|
| **Archives of Nethys** (`2e.aonprd.com`) | texto de regra integral e gratuito do Pathfinder 2e, condição por condição | outros sistemas |
| **SRDs oficiais** do sistema em questão | a redação exata, que é o que você precisa citar | intenção de design |
| **o arquivo do The Forge** (2001–2012) | teoria de design indie, e o histórico de por que várias ideias foram abandonadas. Virou livro acadêmico revisado, então dá para citar | regra de sistema comercial atual |
| **r/RPGdesign** e **r/RPGcreation** | designers discutindo o problema *antes* de resolver — é onde modo de falha aparece nomeado | autoridade sobre qualquer coisa |
| **RPGnet** (`forum.rpg.net`), **EN World**, **RPG PUB** | histórico longo de discussão de mesa; bom para achar a reclamação real dos jogadores | número |
| **BGDF** (`bgdf.com`) | teoria de mecânica em jogo de tabuleiro, que resolve economia de recurso melhor que o hobby de RPG | ficção |

### Matemática de dado

**AnyDice** para conferir contra a referência que a comunidade usa, e `dice-calc` para rodar local. As duas já estão descritas na skill de balanceamento — use a distribuição exata e deixe Monte Carlo para o que não fecha em fórmula.

### Canon e lore

**A hierarquia é essa, e ela é dura:**

1. **A obra original.** Capítulo, painel, fala. É a única coisa que decide.
2. **Material oficial complementar** — fanbook, guia de personagem, novel supervisionado pelo autor. Cobre recorte declarado e pode estar desatualizado em relação ao que veio depois.
3. **Wiki de fã.** **É índice, não autoridade.** Serve para achar em que capítulo a coisa aparece, e aí você vai ler o capítulo.

**E a checagem que quase todo mundo pula: a informação mudou de status depois?** Retcon, revelação posterior, correção do autor, errata. Uma afirmação verdadeira no capítulo 40 pode ter sido virada do avesso no 200. **Procure pelo termo exato antes de generalizar** — o nome específico é âncora literal, e buscar o conceito no lugar do nome é como se perde a revelação que mudou tudo.

### Ferramenta e ambiente

1. **Documentação oficial** da biblioteca ou do formato.
2. **O issue tracker do próprio projeto** — é onde bug conhecido mora, com o workaround que funciona e a versão em que ele entrou.
3. **Stack Overflow e afins**, por último e com data à vista. Resposta de 2015 sobre biblioteca que mudou de API em 2021 é a armadilha mais comum aqui.

## 4. Como julgar o que voltou

Três perguntas, nesta ordem:

**É a fonte ou alguém descrevendo a fonte?** Resumo de busca é fabricante de concordância: ele encontra alguém dizendo o que você perguntou. **Abra o texto e leia o mecanismo, não o resumo do mecanismo.** Se você não consegue citar como a regra funciona — a condição, o gatilho, o número —, você ainda não leu.

**Isso continua valendo?** Errata, edição nova, deprecação, retcon. Data e versão fazem parte do achado.

**Quantas fontes independentes?** Duas que se copiam contam como uma. Fórum citando fórum citando um post apagado é zero.

E o teste que fecha: **você consegue explicar por que o desenho é aquele, e não só o que ele é?** Copiar a forma sem o motivo é como se importa o defeito junto.

## 5. Como reportar

O resultado útil não é "achei isto". É um quadro comparativo com o preço de cada saída:

> **O problema, em uma frase.**
>
> | quem resolveu | como | o que custou / o que quebra |
> |---|---|---|
>
> **O que se aplica aqui, e o que não se aplica** — porque o sistema é multi-mestre, ou porque o personagem persiste, ou porque o teto é outro.
>
> **A recomendação, com o trade-off à vista.**

**Três a cinco sistemas basta.** Mais que isso vira catálogo e ninguém decide. E inclua pelo menos **um que resolveu diferente do que você vai propor** — sem isso o levantamento é ilustração da conclusão, não pesquisa.

**Cite a fonte com link.** Não para parecer rigoroso: para a decisão poder ser reaberta daqui a seis meses sem refazer a busca.

## 6. Quando parar de procurar, e quando perguntar

**Pare de procurar** quando a terceira fonte repete a segunda e nenhum modo de falha novo apareceu. Daí em diante o custo passa o retorno.

**Pergunte em vez de continuar** quando:

- a resposta depende de escolha de sabor — aí a busca terminou e a decisão é do dono do projeto;
- as fontes divergem e a divergência é sobre o que a mesa deve sentir, não sobre fato;
- a busca revelou que a pergunta estava errada. Isso acontece e é o melhor resultado possível: diga qual é a pergunta certa antes de responder a torta.

**E não fique tentando resolver sozinho o que já tem resposta pública.** Contornar duas vezes o mesmo defeito de ambiente custa mais caro que dez minutos procurando a causa — e o contorno some junto com a conversa, enquanto a causa fica registrada.

## 7. O erro que esta skill mais provavelmente vai cometer

**Pesquisar o que já estava decidido.** Chegar com quatro sistemas e um quadro comparativo sobre uma pergunta que o CHANGELOG fechou há dez versões é trabalho jogado fora, e pior: é convite para reabrir decisão boa.

A defesa é a ordem de leitura de sempre — **ler o projeto primeiro, procurar fora depois.** A busca serve o que o projeto ainda não decidiu, e o projeto guarda o que ele já decidiu e por quê.
