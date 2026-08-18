# Prompt para a próxima conversa

Escrito no fim da v0.103, contra o estado real. Cole isto inteiro numa conversa nova.
Renomeie o chat para o próximo número da sua sequência. *O último que teve nome escrito foi o **RPG - JJK15**, na v0.92.*

---

Projeto de RPG da Guilda (Jujutsu Kaisen), chamado **Projeto - M**. Estamos na **v0.103**.

O número pulou de `0.99` para `0.100` e não para `1.00`, e foi decisão dele. `1.0` costuma querer dizer pronto para usar, e o playtest tem zero sessões.

**SÃO DOIS REPOSITÓRIOS, e a relação entre eles é de mão única.** O de TRABALHO é a fonte: `github.com/cupcake-mochi/JJK---Project`. Peças, validadores, CHANGELOG, ESTADO-ATUAL e os DESENHO moram lá. O de ENTREGA é artefato: `github.com/cupcake-mochi/JJK---PDF---RPG`, um recorte do material de mesa para o chat que vai escrever o PDF. **NADA NELE É EDITADO À MÃO**, com UMA exceção: o `README.md` dele, que não existe na fonte. Ele mora em `finalizado`, ignorado pelo `.gitignore` de lá e com `.git` próprio. **A PASTA LOCAL "Claude 2" É SEMPRE A MAIS ATUALIZADA** dos dois.

Os dois estavam na v0.103 no disco quando isto foi escrito, e o commit é dele. **Confira antes de começar:** leia o `logs/HEAD` de dentro do `.git` de cada um como arquivo. O recorte já atrasou duas versões numa sessão só.

> ⚠ **Não peça para ele sincronizar o Project.** Ele não consegue fazer isso sem abrir outra conversa, e você não precisa: clone os dois repositórios do GitHub e você lê o commit mais novo direto. O "Sync now" só importa para chat que leia o Project em vez de clonar.

---

## ⚠⚠ O MOUNT — leia isto antes de escrever qualquer arquivo

**O arquivo fantasma existe e reproduz.** Sintoma: `ls` e `stat` mostram tamanho e inode certos, e `open()` devolve ENOENT enquanto os vizinhos da mesma pasta abrem. Um validador que morre com `FileNotFoundError` num arquivo que existe é isto, e não bug de código.

Ele é intermitente e ninguém sabe o que o dispara. Na v0.101, 23 arquivos foram gravados sem um fantasma e depois 2 de 11 viraram — e outros dois da mesma pasta, na mesma chamada, passaram.

> ⚠ **REESCREVER POR CIMA NÃO CONSERTA.** O `README.md` disse o contrário da v0.28 até a v0.100, e é falso: a escrita nova também sai ENOENT. O `cat > arquivo` falha e o `cp` falha.
>
> **O que conserta é escrever com OUTRO NOME e depois `mv` por cima.** O `mv` não precisa abrir o destino. Confira por md5 depois, dos dois lados.
>
> E o `mv` também é o jeito de tirar arquivo da pasta, já que apagar não dá: mande para `_to_delete`, que o `.gitignore` segura, e peça para ele apagar a pasta a mão.

**O método que funcionou na v0.103, e é o que eu recomendo repetir:**

1. **Clone os dois repositórios do GitHub para dentro do container e trabalhe lá.** `git`, `python3` e os validadores rodam sem drama. Para a checagem 7 rodar, ponha o clone da entrega dentro da fonte, numa pasta chamada `finalizado`.
2. **Confira o disco contra o GitHub antes de começar, por `md5sum` arquivo a arquivo.** Dá para rodar o `md5sum` na máquina dele e comparar com o do container — ele lê a pasta inteira numa chamada só. Na v0.103 bateram os 154 arquivos versionados, e os três a mais no disco eram ignorados pelo git.
3. **Para escrever de volta:** mande o arquivo pelo painel e depois grave no caminho do disco, com `force`. Depois confira `md5sum` dos dois lados, arquivo a arquivo. **A prova de que o trabalho está certo é o md5**, e é ele que acha o fantasma. Se algum sumir, grave de novo com outro nome e `mv` por cima.
4. **Você não consegue apagar arquivo do mount, mas consegue MOVER**, e o `mv` é a ferramenta mais útil que você tem lá.

---

## Ordem de leitura

`README.md`, em especial **"Nove lições que custaram erro"** — fonte única. Depois `sistema/ESTADO-ATUAL.md` INTEIRO (ele trunca; continue do offset). Depois `logs/CHANGELOG.md` de cima — v0.103, v0.102 e v0.101 são as três últimas. Depois os três DESENHO: trilhas, caminhos e manhas.

## Os validadores

**São 22:** dezenove em `sistema/03-mecanica`, o `conferir-repositorio.py` da raiz, e o `pac7.py` e o `v7.py` de `manual/matematica`. O `conferir-nomes.py` leva 21 segundos, então ele não cabe junto de outro numa chamada curta.

```bash
cd sistema/03-mecanica && for v in conferir-*.py; do python3 "$v"; done
cd ../..  && python3 conferir-repositorio.py
cd manual/matematica && for v in pac7.py v7.py; do python3 "$v"; done
```

> ⚠ **CINCO validadores leem o `.docx` do manual**, e sem o `python-docx` eles pulam checagem. **A lista mudou na v0.103 sem a contagem mudar:** o `conferir-atributos.py` saiu dela quando as condições foram para a peça 19, e o `conferir-dano.py` entrou no lugar. **Os cinco de hoje são `conferir-dano.py`, `conferir-manual.py`, `conferir-nomes.py`, `conferir-pericias.py` e `conferir-progressao.py`**, e a tabela de quanto cada um pula está em TRÊS documentos — `README.md`, `sistema/ESTADO-ATUAL.md` e `sistema/LEIA-ME.md`.
>
> Os cinco dizem que pularam. O `subir.sh` também acusa: validador que pulou sai como `ok*` em amarelo, com o motivo do lado. Mesmo assim, **leia a saída em vez do código de retorno**.
>
> No container: `pip install python-docx --break-system-packages`.

E desde a v0.102 **a contagem de checagens de cada validador tem dono, e o dono é o CÓDIGO**. A checagem 9 conta os blocos numerados e confere contra todo documento que publica o número. Uma checagem = um bloco numerado; sub-bloco conta para o bloco pai.

## NÃO RODE GIT NA PASTA DELE

Sai com "loose object is corrupt" e o repositório está inteiro — é o mount. E `git status` cria um lock dentro do `.git` que trava o `subir.sh`. **Commit é sempre do Mizuki, nos dois repositórios.** Para ver em que commit a pasta está, leia o `logs/HEAD` de dentro do `.git` como arquivo.

No container, num clone do GitHub, o git funciona normalmente. Use isso.

Ele tem duas contas de GitHub e troca com `gh auth switch --user cupcake-mochi`. O da fonte é `jjk` e `./subir.sh`, com a mensagem deixada em `mensagem-de-commit.txt`. O da entrega precisa do comando COMPLETO com a mensagem pronta — ele não sabe o que escrever nela.

## COMO FALAR COM ELE

Diga em que estado está cada coisa que você mostrar: **FEITO**, **PRECISO DE VOCÊ** ou **SÓ PARA VOCÊ SABER**.

Uma ideia por parágrafo, frase curta. Nada de ponteiro de seção no meio da frase. Número sempre com a unidade por extenso. Termo do projeto vem com a tradução colada na primeira vez. Escolha de sabor é dele — traga as opções com o número e o trade-off já calculados. **Mas não pergunte o que a conta responde.**

Quando ele disser que não entendeu, procure o defeito antes de reexplicar. Nas duas últimas vezes ele estava certo, e reexplicar melhor teria enterrado os dois achados.

---

## ⚠⚠ A LIÇÃO DESTA LEVA

**Um número marcado como "não reconstrói" é dívida, e não curiosidade.**

O `Derrubado` do nível 11 do `Punho` passou da v0.74 até a v0.103 declarado como órfão, e o que ele era não era mistério: era o preço lendo a entrega errada. **Ele valia o `Derrubado` PERMANENTE, e o texto da entrega escreve dois portões que o preço não lia.**

Com os portões, aquela Trilha caiu de `6,09` para `4,94` de um orçamento de `5,00` — e o estouro de `22%` que estava aceito por decisão nunca foi escolha.

**E quando você mexer num número que outros citam como precedente, procure quem cita.** Quatro decisões de estouro apontavam para o `Punho`. Nenhum número delas se moveu; o que se moveu foi qual precedente elas citam.

## E A SEGUNDA, QUE É A LIÇÃO Nº 8 PELA QUARTA VEZ

**Uma checagem que se mede contra a própria constante sai verde na perturbação que importa.**

A checagem 4 do `conferir-dano.py` comparava o manual contra a lista escrita **dentro do próprio validador**, e não contra a peça. Renomear uma condição na peça saía verde. **Quem achou foi o arnês de perturbação, e não a revisão.**

E ele achou mais duas: uma checagem que procurava uma frase OU outra (meia porta é porta aberta), e duas perturbações mal miradas, que trocavam uma ocorrência de uma âncora que aparece duas vezes no mesmo arquivo. **O arnês ganhou um modo que troca todas.**

## E A TERCEIRA, QUE É DE VALIDADOR

**Uma checagem que só aceita uma resposta obriga o documento a mentir.**

A checagem 6 do `conferir-legados.py` exigia que toda vaga reservada dissesse *"espera a peça de X"*. Quando a peça nascia, a vaga continuava dizendo que esperava. **Ao ganhar o segundo caminho — "destravada pela peça N, e por escrever" — ela achou na hora as duas vagas que a peça 16 destravou na v0.59 e que estavam quarenta e quatro versões escritas como esperando.**

---

## O QUE AS TRÊS ÚLTIMAS VERSÕES FIZERAM

**v0.101** — três lugares diziam verde escondendo que não conferiram. O `subir.sh` jogava a saída do validador fora; dois validadores imprimiam `TUDO OK` sem ter aberto o manual. Os três consertados, e o parágrafo do mount do `README.md` estava dando a saída errada desde a v0.28.

**v0.102** — o quick-start foi abandonado, e a contagem de checagens ganhou dono. Nasceu a checagem 9, a única do projeto em que o dono do número é o código.

**v0.103** — a peça de dano e condições entrou, e é a peça 19. Vinte e seis lugares em oito documentos esperavam por ela. A régua não precisou ser inventada: o manual preça condição em dano desde sempre. Nasceu o `conferir-dano.py`, com dez checagens.

---

## RÉGUAS QUE VALEM HOJE

A fatia é `5,08` de dano por rodada. A Trilha leva `5` e o Caminho leva `3`. O degrau de Caminho é `2 · 7 · 15 · 30` e a entrega de Trilha é `2 · 11 · 19 · 27`, e o dono dos dois é a linha de orçamento do topo do desenho de caminhos.

O vão `físico − conjurador` é `9 · 10 · 11 · 12`, e é exatamente um golpe simples. `+1` no seu acerto vale `10,80` de dano por rodada. Vantagem e rerrolar valem os mesmos `25` pontos percentuais. Dano evitado converte 1 pra 1, e isso inclui PV temporário, resistência e redução.

Um marco compra `+1` de atributo, que são `2,13` fatias. Um Classe 0 causa `27` no nível 30. A Rotina é `floor(3,5 × Classe)` dados. Chefe faz `72` por rodada no nível 30 e capanga faz `38`. Uma luta dura `3,3` rodadas.

**A régua de condição existe desde a v0.103, e é a peça 19.** Uma `Condição Menor` do manual custa `Média`, que é `2/7` da Rotina; uma `Maior` custa `Pesada`, que é `3/7`. As três bandas — `1/7`, `2/7` e `3/7` — dão o nível de cada condição: `Leve`, `Média` ou `Pesada`. **Tirar uma custa `1` ponto de energia por nível.** O manual tem catorze condições, nove `Menor` e cinco `Maior`.

Espaços de feitiço conhecido = `2 + nível ÷ 2`, mais `1` por marco. Dono: a peça 18, desde a v0.99.

## RÉGUAS QUE NÃO EXISTEM

Gastar PE não tem preço. E "uma aptidão a mais" não tem régua — foi isso que matou o `Repertório`.

*A régua de condição saiu desta lista na v0.103.*

---

## O QUE FICA ABERTO, POR TAMANHO

Nada trava jogar. Uma ficha de nível 2 fecha, roda uma missão inteira e sobe de nível.

**Regra que falta**

* **As três Trilhas do Evocador** — `Servo`, `Matilha` e `Coro`. Paradas desde a v0.82, e **elas são a próxima peça, por decisão dele na v0.103**. Quando voltarem, o total de 89 entradas da peça 17 muda e a checagem 1 do `conferir-catalogo.py` acusa.
* **O manual cobra `Média` por dez condições que a conta preça em outro tier, e seis delas ele subvende.** `Cego`, `Impedido` e `Envenenado` valem `Pesada` e custam `Média`. Consertar é mexer na tabela de Melhoria do manual e regerar o `.docx`, e é decisão dele.
* **A `Cicatriz`**, e se a `Energia Reversa` limpa Sequela. As duas ficaram fora do escopo da v0.103.
* **A penalidade por empunhar arma sem treino ou sem requisito.** A peça 14 e a peça 16 apontam para a peça 19, que existe, e o item continua aberto lá dentro.

**Material que falta, e não é regra**

* **O PDF.** Ele está escrevendo direto, a partir do repositório de entrega. **A pergunta de se ele nasce jogável nas primeiras páginas saiu da lista do projeto na v0.103, por decisão dele** — é trabalho dele, e o que o repositório faz é mandar o material para a entrega.
* **Playtest.** A pasta de playtest está vazia desde a v0.1. Todo número do sistema é previsão.

**Pendência pequena**

* **Cinco das sete vagas de `Desliga` estão destravadas e nenhuma foi escrita.** Duas pela peça 16 na v0.59, três pela peça 19 na v0.103. Escrever é trabalho, não conserto de texto.
* A perícia livre da Origem — último lugar da criação em que um número depende de julgamento do mestre.
* Como a `Torrente` cobra o segundo feitiço da rodada, contra a regra de ouro nº 6.
* O ofício não passa no filtro multi-mestre. Conserto escrito: tabela com o atributo padrão de cada um.
* A curva de refino das três rotas ainda mora no esqueleto, que é documento de projeto e não peça. É a última fonte da progressão fora de uma peça, e o candidato natural é a peça 11.
* **Duas réguas de rolagem que não medem a mesma coisa.** `+1` no seu acerto vale `10,80`, que são `10%` da Rotina de `108`; `1` ponto percentual na rolagem de um aliado vale `0,230`, que é `1%` da ação de atacar de `23,00`. Você é modelado pela Rotina inteira e o aliado por dois golpes simples — `4,7` vezes de diferença. Mexer nisso repreçaria o `Guiar`, o `Estampido` e o `Ajudar` de uma vez.

**Peças que ainda nem entraram na fila**

Técnica Marcial e Estilo da Sombra (as duas destravam rotas de Origem), depois Objeto amaldiçoado, Dano de alma com Essência na Integridade, Pactos e Bestiário.

---

## ⚠ A PRIMEIRA COISA A FAZER, SE ELE NÃO PEDIR OUTRA

**As três Trilhas do Evocador — `Servo`, `Matilha` e `Coro`.** Decisão dele na v0.103, e ela acabou com as duas respostas que o projeto tinha para "o que vem agora": a peça 16 dizia que a Técnica Marcial era a seguinte, e ela foi corrigida.

As três são o sistema de invocação visto de dentro, e a peça 15 é a máquina. **O `Servo` tem um rascunho pronto** no rascunho de Trilhas, e a régua daquele documento fechou na v0.61 e foi reformulada na v0.68 — o preço saiu da entrega e foi para a Trilha inteira, e cada entrada declara a taxa de disparo.

> ⚠⚠ **E a primeira coisa a fazer DENTRO delas é ler o que já está escrito, não escrever régua.** O projeto foi inventar régua que o manual já publicava quatro vezes: na v0.80, na v0.86, na v0.92 e na v0.103. **Quando o manual disser "isso não é conta minha", procure quem pegou; quando ele não disser nada, procure a tabela antes de escrever uma.**

**A régua vem antes do catálogo.** É a única recomendação de método que o rascunho de Trilhas faz, e a diferença entre a peça 13 fechar em uma versão e a peça 14 gastar seis.

> **E a peça 15 deixou duas regras penduradas que essas três Trilhas vão encostar:** quando a vida cheia da invocação reinvocada volta, e o que acontece com a invocação quando o DONO cai. *Enquanto as duas não fecharem, nenhuma entrega de Trilha que mexa nelas tem contra o que ser medida.*

---

**Links:** `https://github.com/cupcake-mochi/JJK---Project.git` · `https://github.com/cupcake-mochi/JJK---PDF---RPG.git`
