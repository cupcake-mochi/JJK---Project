# Prompt para a próxima conversa — passada de texto do livro

*Escrito na v0.128, para uma conversa nova com contexto limpo. Copie daqui para baixo.*

---

Retomando o **Projeto - M** (sistema de mesa de Jujutsu Kaisen), em
`/media/mizuki/HD Externo II/Claude/Claude 2/`.

Leia `README.md`, `sistema/ESTADO-ATUAL.md` inteiro e `logs/CHANGELOG.md` de cima — as
entradas **v0.124 a v0.127** são o que esta tarefa herda. Depois leia
`sistema/05-material/livro/REGRA-DE-VOZ.md` inteiro: ela é a régua desta tarefa.

Projeto na **v0.128**, 20 peças, 21 validadores, 203 checagens, tudo verde.

## Esta conversa tem UM foco, e ele é leitura de texto

**Não é tarefa de código.** A varredura mecânica já foi feita duas vezes e ela deixa passar
exatamente o que sobrou. **Leia o livro texto por texto, capítulo por capítulo.** Pode levar o
tempo que precisar — a conta de uso está zerada e a profundidade é o que se quer aqui.

### O que tem de sumir

**Frase de efeito.** Frase que funciona no papel e não entrega regra nenhuma. Três exemplos
que o Mizuki achou lendo o PDF, com o lugar exato:

| onde | a frase |
|---|---|
| `manual/35-caminhos-e-trilhas.md:198` | *"A Vanguarda é o feiticeiro que resolveu o problema da técnica cara comprando aço."* |
| `manual/42-tecnica-marcial.md:130` | *"Se a sua Origem for o Corpo Amaldiçoado, nada disto morde."* |
| `manual/25-origens.md:945` | *"Oito das nove rotas já rodam: seis pelo Fundamento e duas pela Técnica Marcial. A que falta é Sem Técnica, e ela espera uma máquina de criação própria. Nela, você pode escrever a ficção inteira e escolher os dois Legados hoje; o que falta é a montagem do poder."* |

**Os três são famílias diferentes, e vale separar:**

1. **Metáfora no lugar da regra** — *"comprando aço"*. O leitor quer saber o que a Vanguarda
   FAZ, e a frase gasta uma linha sendo espirituosa.
2. **Aviso escrito de trás para frente** — *"nada disto morde"*. A informação é boa; a
   embalagem é que é frase de efeito. Reescreva direto, não corte.
3. **Contabilidade do projeto vazando para o livro** — *"oito das nove rotas já rodam"*. O
   jogador não conta rota; ele quer saber se a Origem dele fecha ficha. **Esta família é a
   mesma que a v0.126 achou** (cinco linhas de *"texto único, compartilhado pelas cinco
   Origens"*), o que quer dizer que a passada anterior não pegou tudo.

**A régua de decisão já está escrita**, em duas seções da `REGRA-DE-VOZ.md`:
*"O livro não fala de si mesmo"* e *"Na dúvida, corta"*. A segunda diz literalmente: *se eu
parei para decidir se uma frase acrescenta, ela já está condenada.*

> **⚠ E a exceção também está lá, e ela é a única:** *não corte se a frase é a única dona de
> um número, de uma exceção ou de um caso que nenhuma outra linha cobre.* **Aí não é estilo,
> é perda de regra — e aí pergunte antes.**

### Onde ler, e quanto é

18 arquivos em `sistema/05-material/livro/manual/`, **79.711 palavras**. Do maior para o
menor: `40-fundamento` 15.4k · `25-origens` 10.7k · `35-caminhos-e-trilhas` 9.7k ·
`50-equipamento` 5.3k · `45-aptidoes-e-refino` 5.2k · `10-como-jogar` 3.4k ·
`60-invocacoes` 3.5k · `80-experiencia` 3.3k · `07-glossario` 3.2k · `15-dano-e-condicoes`
2.8k · `12-pericias-e-oficios` 2.7k · `20-criacao-de-personagem` 2.6k ·
`55-ferramenta-amaldicoada` 2.1k · `11-o-turno` 2.1k · `47-bencaos-e-lapidacao` 2.0k ·
`42-tecnica-marcial` 1.9k · `70-descanso` 1.5k · `08-inicio-rapido` 1.0k ·
`05-introducao` 0.7k · `90-apendice-bloquear` 0.7k.

**Edite sempre a fonte `.md`. Nunca o `.pdf`, o `.docx` nem o texto corrido** — os três são
gerados a partir dela.

## E uma coisa pequena de regra, que não é texto

**Duas Origens estão sem a lista de quatro perícias**, e o livro diz isso com todas as
letras em `manual/25-origens.md:627` e `:794`. *As outras cinco têm a lista na peça 9.*

***Decisão do Mizuki, e ela fecha a Restrição Celestial:***

| ramo | a lista de quatro sai de |
|---|---|
| **corpo pela técnica** | Inteligência e Essência, somadas |
| **sem energia** | Destreza e Força, somadas |

**Três coisas para conferir antes de escrever:**

- **O poço de Destreza + Força tem exatamente CINCO perícias** — `Atletismo`, `Acrobacia`,
  `Furtividade`, `Pontaria`, `Prestidigitação`. *Escolher quatro de cinco é apertado de
  propósito, e é o que a Origem é.* **O de Inteligência + Essência tem dezoito.**
- **Nenhuma outra Origem tem lista por RAMO** — as cinco escritas têm uma só. *Isto abre uma
  forma nova, e ela precisa entrar na peça 9 e no livro do mesmo jeito.*
- **O ramo sem energia não pode ter `Sentir Energia`** — a peça 9 §5 fecha isso. *Ela é de
  Essência, então o poço já a exclui, mas confira que nada no texto contradiz.*

> **⚠ O Corpo Amaldiçoado continua sem lista, e o Mizuki NÃO decidiu essa.** *Ele falou só
> dos dois ramos da Restrição Celestial.* **Traga a pergunta com as opções medidas e
> pergunte** — não invente a lista.

**A dona do número é a peça 9** (`sistema/03-mecanica/09-origens.md`), e o livro é cópia.
Escreva na peça primeiro, depois no livro. *O `conferir-pericias.py` confere as listas de
Origem contra o quadro de perícias.*

## Onde as coisas moram

| | |
|---|---|
| a fonte do livro | `sistema/05-material/livro/manual/*.md`, 18 arquivos |
| a régua de escrita | `sistema/05-material/livro/REGRA-DE-VOZ.md` |
| o validador do livro | `sistema/05-material/livro/conferir-voz.py` — **rode com `--estrito`**, senão ele sai `0` mesmo com achado |
| o que já foi cortado e por quê | `sistema/05-material/livro/REMOCOES-material-de-mestre.md` |
| o registro da revisão | `sistema/05-material/livro/ESTADO-revisao.md` |
| a trava de número | `sistema/05-material/livro/build/guard_numeros.py antes.md depois.md` |
| como regerar | `sistema/05-material/livro/README.md` |
| as peças de regra | `sistema/03-mecanica/`, 20 peças e 20 validadores |

**Repositórios:**
- projeto (tudo): `https://github.com/cupcake-mochi/JJK---Project.git`
- entrega do PDF: `https://github.com/cupcake-mochi/JJK---PDF---RPG.git` — mora em
  `finalizado/`, tem git próprio e **precisa do commit dela depois**

**Os manuais de referência**, que vêm em anexo nesta mensagem e servem de exemplo de como um
livro do hobby escreve:
- `/home/mizuki/Downloads/Player_Hand_Book_DnD_2024.pdf.zip`
- `/media/mizuki/HD Externo II/PDFs/PDF_Sistemas/dampd-5e---caldeirao-de-tasha-para-tudo.pdf.zip`
- `/media/mizuki/HD Externo II/PDFs/PDF_Sistemas/dd-5e-guia-do-mestre-biblioteca-elfica.pdf.zip`

*Descompacte e leia trecho de verdade antes de decidir forma.* **O PHB 2024 não usa bloco de
`Exemplo:` nenhuma vez em 397 páginas**, e o livro daqui usa — isso é decisão registrada, e
não descuido.

## Três diagramações no disco, e a escolha é do Mizuki

*Ainda em aberto.* `sistema/05-material/livro/` tem:

| arquivo | páginas |
|---|---|
| `Projeto-M-Manual-da-Guilda-A-atual.pdf` | 256 — snapshot, **não se regera** |
| `Projeto-M-Manual-da-Guilda.pdf` | 251 — coluna única |
| `Projeto-M-Manual-da-Guilda-C-duas-colunas.pdf` | 143 — `python3 build.py --duas` |

**Toda mudança de texto tem de sair nas duas que se regeram.** *Rode os dois builds.*

## Método, e ele não é negociável

- **Rode os validadores antes de mexer em número:** os 20 de `sistema/03-mecanica/`, o
  `conferir-repositorio.py` da raiz, os dois de `manual/matematica/`, e o
  `conferir-voz.py --estrito` do livro.
- **Mede o sucesso pelo CÓDIGO DE SAÍDA, nunca casando texto da saída.** *Os validadores
  reprovam em dois formatos — `>>> N PROBLEMA(S)` e `>>> FALHOU`.* **Um laço que procura só o
  primeiro sai verde sem ter conferido, e isso travou o commit da v0.122.**
- **Confira `PULADA = 0`.** Sem `python-docx` cinco validadores pulam em vez de falhar.
- **`guard_numeros.py` a cada arquivo mexido, e explique CADA diferença antes de aplicar.**
  *Numa passada de texto, o número de regra que muda é zero.*
- **Escolha de sabor é do Mizuki**, em rodadas curtas de pergunta, nunca proposta grande
  pronta. Traga as opções com o tamanho de cada uma já medido.
- **Documento não pode ter cara de saída de IA.** Português informal, nunca de Portugal.
- **Você não commita.** Deixe a mensagem em `mensagem-de-commit.txt` na raiz e em
  `finalizado/mensagem-de-commit.txt`, e avise; ele roda `jjk && ./subir.sh` e depois
  commita a entrega.

### Duas armadilhas que esta tarefa específica tem

> **⚠ Corte demais também é defeito.** *A v0.125 cortou dois capítulos ao molde da casa e a
> conta bateu porque cada diferença do `guard_numeros` foi lida contra a linha que a
> carregava.* **Se você cortar sem ler o que a frase segurava, some regra.**

> **⚠ A medida não acha esta classe de defeito, e isso já foi provado.** *Na v0.126 as duas
> réguas contáveis — prosa antes da primeira regra, e proporção de prosa solta — passaram
> nos dois capítulos que estavam errados.* **A `REGRA-DE-VOZ.md` declara isso: decidir se uma
> frase é fato mal-vestido ou enfeite está na lista do que fica fora do alcance do
> validador.** *Não tente derivar o corte de um número. Leia.*

## O que NÃO é desta tarefa

As três Trilhas do Evocador (`Servo`, `Matilha`, `Coro`) continuam paradas por decisão do
Mizuki. `Sem Técnica` tem criação própria e vem depois. O repreço do `Desarmado` é da peça 19.
E a escolha de qual diagramação fica é dele, não sua.
