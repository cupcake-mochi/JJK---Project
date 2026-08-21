# Prompt para a próxima conversa

Cole isto inteiro numa conversa nova. Renomeie o chat seguindo a sequência `RPG - JJK<n>` — pergunte a ele qual foi o último número, porque quem sabe é ele.

> ## ⚠ Este arquivo não sabe em que versão o projeto está, e é de propósito
>
> **Ele não carrega número, régua, pendência nem "o que aconteceu na última versão".** Tudo isso tem dono em outro documento, e cópia diverge do dono — é a lição nº 9 do `README.md`, e ela já matou uma cópia dentro do próprio `sistema/ESTADO-ATUAL.md` na v0.32: ele guardava a lista de lições, e ela tinha parado em cinco enquanto o README chegava a nove.
>
> **O que mora aqui é só o que não muda quando a versão vira:** que projeto é este, onde ficam as coisas, como escrever arquivo neste mount, como rodar validador, e como conversar com ele.
>
> **Se você achar um número de versão ou uma régua escrita neste arquivo, isso é bug.** Apague e ponha o ponteiro para o dono.

---

## O que é

Projeto de RPG da Guilda (Jujutsu Kaisen), chamado **Projeto - M**. Sistema de mesa para um server de guilda com vários mestres ativos e personagem persistente entre mesas.

O filtro que decide quase tudo: *dois mestres que nunca conversaram chegam ao mesmo número?*

A numeração pulou de `0.99` para `0.100` em vez de `1.00`, e foi decisão dele. `1.0` costuma querer dizer pronto para usar, e o playtest tem zero sessões.

## São dois repositórios, e a relação é de mão única

O de **trabalho** é a fonte. Peças, validadores, CHANGELOG, ESTADO-ATUAL e os DESENHO moram lá.

O de **entrega** é artefato: um recorte do material de mesa, para quem for escrever o PDF. Ele mora em `finalizado`, com `.git` próprio, ignorado pelo `.gitignore` da fonte.

**Nada na entrega é editado à mão, com uma exceção:** o `README.md` dela, que não existe na fonte. O resto é cópia byte a byte, e a checagem 7 do `conferir-repositorio.py` é a única coisa do projeto que atravessa os dois repositórios.

**A pasta local dele é sempre a mais atualizada das duas.** Para saber em que commit cada uma está, leia o `logs/HEAD` de dentro do `.git` como arquivo — a entrega já atrasou duas versões numa sessão só.

> ⚠ **Não peça para ele sincronizar o Project.** Ele não consegue fazer isso sem abrir outra conversa, e você não precisa: clone os dois repositórios e leia o commit mais novo direto. O "Sync now" só importa para chat que leia o Project em vez de clonar.

---

## Onde cada coisa é dona do seu número

Este índice substitui tudo que costumava ser copiado para cá. **Vá ao dono; não confie em resumo, nem no meu, nem no de outra sessão.**

| você quer saber | o dono é |
|---|---|
| em que versão o projeto está | a entrada do topo de `logs/CHANGELOG.md` |
| o que as últimas versões fizeram, e **por quê** | `logs/CHANGELOG.md`, de cima para baixo |
| as lições que custaram erro | `README.md`, seção *"Nove lições que custaram erro"* — fonte única, e ela cresce |
| o que está aberto, e a fila do que vem | `sistema/ESTADO-ATUAL.md`, nas seções de pendências, de problemas de design e a de retomada, no fim |
| qualquer régua ou número de balanço | a peça de `sistema/03-mecanica/` que é dona dele |
| quantas peças, validadores e checagens existem | o **código** — e a checagem 9 do `conferir-repositorio.py` confere os documentos contra ele |
| o que ainda não virou peça | os `DESENHO-*.md` e `LISTA-*.md` da raiz, e `sistema/03-mecanica/RASCUNHO-bloqueio.md` |
| como ele gosta de trabalhar | `sistema/ESTADO-ATUAL.md`, na seção do fim |
| onde ficam as skills de apoio | `sistema/skills/` |

**Se `sistema/02-esqueleto/arquitetura.md` contradisser uma peça de `sistema/03-mecanica/`, a peça vence.**

**Não leia de `sistema/99-arquivo/` para escrever peça nova.** É material morto, guardado com o motivo de ter morrido.

## Ordem de leitura

`README.md`, em especial as **"Nove lições que custaram erro"**. Depois `sistema/ESTADO-ATUAL.md` **inteiro** — ele é grande e o leitor trunca; se vier aviso de leitura parcial, continue do offset em vez de responder pela primeira página, porque a seção de retomada é a última. Depois `logs/CHANGELOG.md` de cima, quantas entradas couberem. Depois a peça que for mexer.

---

## ⚠⚠ O mount — leia isto antes de escrever qualquer arquivo

**O arquivo fantasma existe e reproduz.** Sintoma: `ls` e `stat` mostram tamanho e inode certos, e `open()` devolve ENOENT enquanto os vizinhos da mesma pasta abrem. Um validador que morre com `FileNotFoundError` num arquivo que existe é isto, e não bug de código. **O conteúdo no disco nunca esteve em risco.**

Ele é intermitente e ninguém sabe o que o dispara. Numa leva, 23 arquivos foram gravados sem um fantasma e depois 2 de 11 viraram — e outros dois da mesma pasta, na mesma chamada, passaram.

> **Escreva código pelo bash, com `cat > arquivo` e heredoc.** Arquivo que a ferramenta de escrita grava fica invisível para o `python3` com frequência. Para `.md` a ferramenta de escrita serve.
>
> **Depois de escrever, confira que o bash lê o arquivo de volta — antes de rodar validador, não depois.** Um validador que falha por arquivo sumido parece erro de conteúdo e custa uma rodada de investigação errada.
>
> ⚠ **Reescrever por cima nem sempre conserta.** O `README.md` afirmou o contrário da v0.28 até a v0.100. **O que conserta é escrever com OUTRO NOME e depois `mv` por cima** — o `mv` não precisa abrir o destino. Confira por md5 depois, dos dois lados.
>
> **Apagar não dá; mover dá.** Mande para `_to_delete/`, que o `.gitignore` segura, e peça para ele apagar a pasta a mão.

> ⚠⚠ **Grave no disco a cada bloco fechado, e não no fim.** Uma versão inteira já se perdeu assim: a conversa fez o trabalho todo dentro do container, bateu no limite de sessão antes de gravar, e o disco ficou uma versão atrás com o dono do projeto achando que estava tudo lá. **Um checkpoint parcial no disco vale mais que uma versão inteira num container que some.**

**Se a sua interface tiver container próprio**, o caminho que funciona é clonar os dois repositórios e trabalhar lá — `git`, `python3` e os validadores rodam sem drama. Para a checagem 7 rodar, ponha o clone da entrega dentro da fonte, numa pasta chamada `finalizado`. Confira o disco contra o clone por `md5sum` arquivo a arquivo antes de começar e depois de gravar; **a prova de que o trabalho chegou é o md5**, e é ele que acha o fantasma.

> Para escrever de volta em lote: um `.tar.gz` só, gravado em `_to_delete/`, extraído numa pasta de staging criada **dentro** do mount, e aí `mv -f` arquivo por arquivo. **`mv` de fora do mount para dentro falha** — atravessar sistema de arquivos vira copiar-e-apagar, e o mount não deixa sobrescrever. Dentro do mesmo sistema de arquivos passa.

> **Se a sua ferramenta abrir worktree dentro da pasta**, ele é uma cópia inteira do repositório dentro do repositório. O `conferir-repositorio.py` e o `.gitignore` já pulam `.claude` por causa disso, desde a v0.107 — se você criar cópia de trabalho em outro lugar da árvore, o validador vai ler ela como material e acusar cada ponteiro duas vezes.

---

## Os validadores

Cada peça tem um validador dono, e checagem nova vai no validador da peça que ela confere — nunca num arquivo novo. **Nada de valor fica escrito dentro do validador:** o número se lê do documento dono.

```bash
cd sistema/03-mecanica && for v in conferir-*.py; do python3 "$v"; done
cd ../..  && python3 conferir-repositorio.py
cd manual/matematica && for v in pac7.py v7.py; do python3 "$v"; done
```

O `conferir-nomes.py` leva uns 20 segundos, então ele não cabe junto de outro numa chamada curta.

> ⚠ **Alguns validadores leem o `.docx` do manual, e sem o `python-docx` eles PULAM checagem em vez de falhar** — saem verdes sem terem conferido nada, com código 0. Um deles pula tudo, no `except ImportError`, antes da primeira checagem.
>
> **Conte as PULADAs; um verde que pulou não prova nada.** Instale com `pip install python-docx --break-system-packages`.
>
> **Quantos são e quanto cada um pula: leia do CÓDIGO, não da saída.** Uma versão contou pela saída, escreveu um número errado em quatro documentos, e ele sobreviveu duas versões. Contar sintoma não é contar causa.

**Rode de `sistema/03-mecanica/`**, porque é o que o `subir.sh` faz e o que a documentação supõe. *O motivo antigo — "de outro lugar eles pulam em silêncio" — parou de reproduzir na v0.38; hoje todos resolvem o caminho por `__file__`.*

### Todo número novo ganha teste negativo

Perturbe o valor e prove que a checagem certa acende. Três regras, cada uma paga com uma versão perdida:

1. **Numa cópia isolada**, nunca nos arquivos reais.
2. **Confira que a base passa na cópia antes de perturbar.** Cópia mal montada faz todas as perturbações acenderem — vermelhos que parecem prova e não são.
3. **Confira por `diff` que a perturbação mudou o arquivo** antes de ler o resultado. `sed` que não bate produz um "não acendeu" falso.

**E separe a regra aplicada do limite de design.** Uma checagem que se mede contra a própria constante sai verde quando você perturba a constante — é a lição nº 8, e ela apareceu em três versões seguidas. Sempre que der, acrescente um contra-teste que prove que a checagem não é trivialmente verdadeira.

### Antes de batizar qualquer coisa

```bash
cd sistema/03-mecanica && python3 conferir-nomes.py --candidatos Nome Outro Terceiro
```

Ela pega substring e já matou mais de dez nomes que pareciam livres. **Não pega três coisas, e você tem que pegar:** colisão de *sentido* (o nome sai `LIVRE` e ainda briga com o que o sistema já faz com aquela palavra), colisão com o hobby (*move*, *vantagem*, *condição*, *crítico* carregam significado herdado — procure o termo em `sistema/01-pesquisa/` antes) e categoria (escrever substantivo mais adjetivo faz o validador ler o adjetivo como nome da categoria).

---

## ⚠ Não rode git na pasta dele

Sai com `loose object is corrupt` e **o repositório está inteiro** — é o mount. Pior: `git status` cria um `.git/index.lock` que o sandbox não consegue apagar, e um lock preso trava o `subir.sh`. Vale para tudo, inclusive `log` e `fsck`.

Para ver em que commit a pasta está, leia o `logs/HEAD` de dentro do `.git` como arquivo. Num clone dentro de container, o git funciona normalmente.

**O commit é sempre dele, nos dois repositórios.** Você lê, edita e valida; ele commita.

Ele tem duas contas de GitHub e troca com `gh auth switch --user cupcake-mochi`. Na fonte é `./subir.sh`, que roda todos os validadores e se recusa a commitar se algum falhar, usando a mensagem deixada pronta em `mensagem-de-commit.txt`. **A entrega precisa do comando completo com a mensagem já escrita** — ele não sabe o que pôr nela.

### Fechar versão

**A entrada do topo do `logs/CHANGELOG.md` é a dona da versão do projeto.** Subir o número no `README.md`, no `sistema/ESTADO-ATUAL.md` ou no `sistema/LEIA-ME.md` sem escrever a entrada **falha** o `conferir-repositorio.py`.

Peça nova ou validador novo **quebra a contagem** até os três documentos e a entrada do CHANGELOG subirem juntos. Mas o validador confere a contagem, **não a prosa** — as listas de comandos e as seções em texto passam por baixo dele. **Quando fechar peça, releia as listas à mão.**

Meia peça não é peça: trabalho em andamento vive como `RASCUNHO-*.md`, sem número na frente. Peça substituída vai para `sistema/99-arquivo/` com cabeçalho dizendo de onde saiu, o que a substituiu, em que versão, **por que morreu** e o que dela sobreviveu.

**E a entrega não se atualiza sozinha.** Quando uma peça, um desenho ou o manual mudam, a cópia em `finalizado` fica velha e a checagem 7 acusa. O `README.md` dela é escrito à mão e carrega a versão do recorte e a do manual.

**Antes de fechar, revisão cética — inclusive contra o que você mesmo acabou de escrever.** Metade dos achados grandes do CHANGELOG saiu daí.

---

## Como falar com ele

Diga em que estado está cada coisa que você mostrar: **FEITO**, **PRECISO DE VOCÊ** ou **SÓ PARA VOCÊ SABER**.

Uma ideia por parágrafo, frase curta. Nada de ponteiro de seção no meio da frase. Número sempre com a unidade por extenso. Termo do projeto vem com a tradução colada na primeira vez.

**Escolha de sabor é dele** — quantos itens numa lista, quais são, como se chamam, em que ordem aparecem. Traga as opções com o número e o trade-off de cada uma já calculados, e pergunte. Várias rodadas curtas, nunca uma proposta grande pronta. **Mas não pergunte o que a conta responde:** se dominância, deriva ou o filtro multi-mestre já decidem, rode a conta e apresente o resultado.

Mostre o resultado no chat, não só no arquivo — ele quer ler o que foi escrito sem abrir o documento. E antes de entrar numa peça, mostre o que ela tem hoje.

**Número vem de conta rodada, nunca de intuição.** Escreva o script, rode, mostre a tabela.

**Documento não pode ter cara de saída de IA.** Seções de tamanhos diferentes, sem simetria forçada, sem "além disso" e "em suma". Português informal, e nunca português de Portugal.

> **Quando ele disser que não entendeu, procure o defeito antes de reexplicar.** Nas vezes em que isso aconteceu ele estava certo, e reexplicar melhor teria enterrado o achado.

---

## As armadilhas que mais voltam

Elas moram no `README.md`, nas *"Nove lições que custaram erro"*, e é de lá que se lê. Esta é amostra, não lista:

- **"Esse número já inclui o que eu estou somando nele?"** É o erro mais teimoso do projeto.
- **Antes de aceitar um preço, veja se o termo que ele usa existe** — e se existe, vá ler a regra pendurada nele.
- **Tensão de preço às vezes é lacuna de texto disfarçada.**
- **Decisão registrada não é decisão aplicada.** Decisão que termina em "corrigir em três lugares" precisa de alguém conferindo os três.
- **Sintoma não diz onde consertar.** Registro de pendência costuma anotar onde a coisa apareceu e chutar a pasta — confirme lendo o texto real antes de procurar onde o bilhete manda.
- **Aviso que parou de reproduzir é dívida.** Um procedimento com motivo errado envelhece pior que um sem motivo nenhum.
- **Número sobre a ferramenta se lê da ferramenta**, e não da saída dela.
- **Pesquise antes de inventar.** Se a sua proposta vai afirmar o que outro sistema faz, qual o modo de falha documentado de alguma coisa ou o que o material original estabelece, procure antes de escrever.

---

**Links:** fonte em `https://github.com/cupcake-mochi/JJK---Project.git` · entrega em `https://github.com/cupcake-mochi/JJK---PDF---RPG.git`
