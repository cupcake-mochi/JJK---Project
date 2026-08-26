# Projeto - M — sistema de mesa de Jujutsu Kaisen

**O sistema se chama `Projeto - M`**, batizado na v0.94 — era a pendência mais velha que existia aqui, aberta na v0.1. Sistema de RPG de mesa feito do zero, ambientado no universo de Jujutsu Kaisen, para um server de guilda com **5 a 7 mestres ativos** e **personagem persistente entre mesas**. Material de fã, gratuito, sem fins comerciais.

**Versão v0.161** · manual do Fundamento na **v7.15** · **vinte e quatro peças de regra** e **vinte e quatro validadores passando** · o Manual da Guilda em **17 capítulos**.

---

## O que este projeto é, em três frases

O problema que ele existe para resolver não é "fazer um RPG de JJK": é **o mesmo personagem passar por sete mesas diferentes e continuar sendo o mesmo personagem**. Por isso quase toda decisão aqui passa por um filtro — *dois mestres que nunca conversaram chegam ao mesmo número?* — e por isso o projeto tem mais validador que a maioria dos sistemas publicados.

O coração é o **Fundamento**: um subsistema fechado e já validado que resolve técnica, feitiço, Melhoria, Restrição, Liberação Máxima, Expansão de Domínio e dano de alma por orçamento de pontos. Ele mora em `manual/` e é gerado por código. Tudo em `sistema/` é o que existe **em volta** dele — atributos, Caminhos, perícias, criação de personagem, descanso, aptidões.

E o registro do **porquê** de cada decisão é tão importante quanto a regra: `logs/CHANGELOG.md` guarda o argumento de todas as versões desde a v0.1, e é a única parte do projeto que não dá para reconstruir sozinho lendo o resto.

## Por onde começar, se você acabou de clonar isto

1. **`sistema/ESTADO-ATUAL.md`** — o sistema inteiro em uma página: o que existe, o que não existe (tem uma seção medida sobre isso), e onde o trabalho parou.
2. **`logs/CHANGELOG.md`** — de cima para baixo, a entrada do topo é a mais recente. Leia até pelo menos a v0.16.
3. **`sistema/02-esqueleto/arquitetura.md`** — o mapa. É o documento mais antigo: **se ele contradisser uma peça de `03-mecanica/`, a peça vence.**
4. As peças de **`sistema/03-mecanica/`**, na ordem numérica.

**Não leia de `sistema/99-arquivo/` para escrever peça nova.** É material morto, guardado com o motivo de cada morte escrito no topo.

## Retomar em conversa nova

**Primeiro, confirme que você abriu a pasta certa — leva dez segundos e já custou meia hora uma vez.** Existe outro clone desta mesma coisa parado na **v0.27** numa pasta `JJK---Project` dentro da home, e ele tem a cara do projeto inteiro: validadores, peças, changelog. Uma conversa já se perdeu lendo o clone velho e rodando sete validadores que passaram sem provar nada.

```bash
grep -c "Nove lições" README.md        # tem que dar 1 ou mais
grep -c "Seis lições"  README.md       # tem que dar 0
```

Se aparecer *"Seis lições que custaram erro"* ou *"Versão v0.27"*, **é a pasta errada. Pare.**

> *Esta checagem já foi `head -6 README.md # tem que dizer Versão v0.57 ou maior`, e ela envelheceu sete versões seguidas — um teste escrito contra um número que sobe toda semana começa a mentir na semana seguinte.* **O que não envelhece é a lista de lições**, porque o clone velho parou nas seis e nunca vai ganhar a sétima.

Depois disso, a ordem de leitura é a da próxima seção, e os validadores são os da seção *"Rodar os validadores"*. **Não rode git daqui** — o porquê está em *"Commitar"*.

> **Não existe mais um arquivo de prompt de retomada, e isso é decisão da v0.45.** O `PROMPT-CHAT-NOVO.md` foi para `sistema/99-arquivo/`: medido bloco a bloco, **15 dos 16 eram cópia** de coisa que já tinha dono aqui, no `ESTADO-ATUAL` ou na skill — e ele já tinha divergido duas vezes, sem nenhum validador que o alcançasse. *Ele era a segunda encarnação da ideia: o `PROMPT-DE-CONTINUIDADE.md` morreu na v0.14 pelo mesmo motivo.*
>
> **O que funciona no lugar é o hábito que tornou os dois desnecessários: pedir um prompt de continuidade no fim de cada conversa**, escrito na hora contra o estado real. Um prompt escrito na hora não tem como envelhecer; um arquivo tem.

## Como está organizado

```
.
├── README.md              você está aqui
├── logs/
│   ├── CHANGELOG.md                     o porquê de cada decisão, da v0.1 até a versão atual
│   └── CHANGELOG-manual-v6-para-v7.md   o changelog do manual, antes de ele entrar aqui
├── manual/
│   ├── Fundamento-MANUAL-v7.docx        v7.15 — o manual gerado
│   ├── Fundamento-MANUAL-v7.pdf         v7.15 — o mesmo do .docx desde a v0.93
│   ├── gerador/                         Node + docx. `node make.js` recria o .docx do zero
│   └── matematica/                      pac7.py e v7.py, os validadores do manual
└── sistema/
    ├── ESTADO-ATUAL.md                  o ponto de retomada
    ├── LEIA-ME.md                       o mapa das pastas
    ├── 00-fundacao/                     os três pilares e as restrições do projeto
    ├── 01-pesquisa/                     dossiê de metodologia — a seção 8 lista as dez travas
    ├── 02-esqueleto/                    arquitetura: subsistemas e como se encaixam
    ├── 03-mecanica/                     as vinte e quatro peças de regra e os vinte e quatro validadores
    ├── 04-playtest/                     vazia. Zero sessões desde a v0.1
    ├── 05-material/                     a ficha (e o gerador dela) e o livro/, o Manual da Guilda completo
    ├── 99-arquivo/                      material morto, com LEIA-ME próprio
    └── skills/                          cópia de trabalho das sete skills de apoio
```

Um arquivo `RASCUNHO-*.md` em `03-mecanica/` é levantamento engatilhado, não peça — ele não leva número justamente por isso, e o `conferir-repositorio.py` falha se algum tomar. **Hoje são três:** `RASCUNHO-bloqueio.md` (a regra opcional de rolar a defesa, fechada em desenho na v0.43), `RASCUNHO-clash-de-expansoes.md` e o `RASCUNHO-trilhas.md`, que a **v0.54** abriu e que é a posição 1 da fila. *Eram cinco até a v0.58, quando o de Invocações virou a peça 15, e quatro até a v0.59, quando o de ferramenta amaldiçoada virou a peça 16 — que é o caminho que um rascunho existe para fazer, duas versões seguidas.* **O de Pactos fez o mesmo caminho na v0.134**, e foi para o `99-arquivo/` com o cabeçalho de sempre: **rascunho que virou peça e continua vivo ao lado dela é a segunda fonte da regra.**

**`_backup/` não entra no repositório** — ele guarda o estado da pasta antes da reorganização, e o `.gitignore` o segura.

## Preparar a máquina

```bash
pip install python-docx --break-system-packages    # cinco validadores leem o .docx
cd manual/gerador && npm install docx               # só se for regerar o manual
```

Sem `python-docx`, **cinco validadores pulam** as checagens que leem o manual em vez de falhar — então eles saem verdes sem terem conferido nada, com código 0. Instale antes de confiar num "OK".

**Quanto cada um perde**, lido do código e conferido bloqueando o import:

| validador | pula | de quantas | o rodapé avisa? |
|---|---|---|---|
| `conferir-dano.py` | 1 (as catorze contra o manual) | 10 | **sim** — `OK, mas 1 checagem(ns) PULARAM` |
| `conferir-manual.py` | **4 — todas.** Ele sai no `except ImportError` antes da primeira | 4 | avisa, e sai antes do rodapé |
| `conferir-nomes.py` | 3 (as checagens 1, 3 e 4) | 5 | sim, **desde a v0.101** |
| `conferir-pericias.py` | 1 (a que bate contra o Fundamento) | 8 | sim, **desde a v0.101** |
| `conferir-progressao.py` | 1 (a checagem 7) | 8 | **sim** |

> **⚠ Continuam CINCO, e um deles trocou na v0.103.** *As condições saíram da peça 1 para a peça 19, e com elas saiu a única checagem do `conferir-atributos.py` que abria o `.docx`.* **Ele deixou de ler o manual e o `conferir-dano.py` entrou no lugar dele.** *A contagem não se moveu, e a lista se moveu — que é exatamente o tipo de troca que passa despercebida quando o número está certo.*

> **Eram três até a v0.96.** *O `conferir-atributos` entrou na v0.97, quando o caminho de pulada dele foi consertado, e o `conferir-progressao` entrou na v0.99 junto com a peça 18.* **A contagem ficou parada em três nos dois documentos que a publicam — e este arquivo dizia "dois" no comentário do `pip` e "três" no parágrafo, com nove linhas de distância.** *Duas cópias, duas respostas, dentro do arquivo que publica a lição nº 9.*

> **Os cinco avisam, e dois deles só desde a v0.101.** *O `conferir-nomes` e o `conferir-pericias` imprimiam `TUDO OK` sem terem lido o manual, e isso ficou aberto da v0.97 até lá.* **Quem registra a pulada é cada checagem no ponto em que ela desiste**, então a contagem do rodapé é derivada e não escrita. *E o `subir.sh` também acusa: um validador que pulou sai como `ok*` em amarelo, com o motivo do lado.*

*A v0.38 registrou **4, 2 e 1**, e os três documentos repetiram. O 4 do `conferir-nomes` era a contagem da palavra `PULADA` na saída — ele imprime um aviso de resumo e mais três marcadores —, e o 2 do `conferir-manual` não bate com nada: ele **não confere nada** sem a biblioteca.* **É o que estava documentado como o que pula menos, e é o único que fica cego por inteiro.**

**Rode de `sistema/03-mecanica/`.** *E a razão mudou na v0.38, então vale saber qual é.* Até a v0.37 este arquivo dizia que rodar de outro lugar fazia os três pularem checagem em silêncio — verdade medida na v0.28, e a v0.33 chegou a contar **4, 1 e 1** puladas rodando de `/tmp`. **Hoje não reproduz mais:** os cinco validadores que abrem arquivo do manual resolvem o caminho por `os.path.dirname(os.path.abspath(__file__))`, e nenhum `conferir-*.py` tem caminho relativo cru. De `/tmp` a saída sai idêntica, byte por byte, com zero puladas.

O hábito continua, porque é o que o `subir.sh` faz e é o que o resto da documentação supõe. **O que não continua é a justificativa** — e um aviso que dá o motivo errado é pior que nenhum, porque ele ensina a procurar o defeito no lugar em que ele não está mais.

## Rodar os validadores

**Antes de mexer em qualquer número.** Eles falham alto se algo quebrar.

```bash
cd sistema/03-mecanica
python3 conferir-atributos.py     # acerto, defesa, TR, perícia, vida, PE máximo, deriva
python3 conferir-acao.py          # régua das Restrições, dominância, Adianta
python3 conferir-pericias.py      # quadro de perícias, listas de Caminho e Origem, colisão
python3 conferir-descanso.py      # piso, exaustão, arredondamento, magnitude, empilhamento
python3 conferir-nomes.py         # todo nome batizado, projeto → manual
python3 conferir-manual.py        # vocabulário e números importados, manual → projeto
python3 conferir-aptidoes.py      # a trava do refino, as três rotas do marco, o kokusen
python3 conferir-expansao.py      # os gates da Expansão, a ordem, o preço em espaços
python3 conferir-orcamento.py     # o somatório: todos os drenos de PE ao mesmo tempo
python3 conferir-xp.py           # a curva, o abismo que fecha, e os alvos da Guilda
python3 conferir-equipamento.py  # o fundo de cada arma, a dominancia, o teto de Defesa
python3 conferir-criacao.py      # a ficha de exemplo contra as fórmulas, e o que a criação cita
python3 conferir-ficha.py        # a ficha de 05-material contra os catálogos das peças
python3 conferir-legados.py      # os três formatos, a cota de Desliga, as vagas e os totais
python3 conferir-invocacoes.py   # o teto somado, o catálogo, a régua, a morte e o orçamento
python3 conferir-ferramenta.py   # o fundo, o gate herdado, a escada de grau, o teto na ficha
python3 conferir-catalogo.py     # o índice das 90 entradas contra os três DESENHO da raiz
python3 conferir-progressao.py   # as nove colunas da tabela de progressão contra os donos
python3 conferir-dano.py         # a régua de condição, as treze, os tipos de dano e a cobertura
python3 conferir-alma.py         # a Integridade com Essência, os quatro estágios, o TR e a exceção
```

**Os cinco últimos são de outra natureza, e vale saber por quê.** Os onze primeiros conferem **regra** — *a fórmula deriva certo?*.

*E o `conferir-equipamento.py` faltava nesta lista desde a v0.48, quando ele entrou* — o `subir.sh` sempre o rodou, porque ele varre a pasta por glob, mas quem seguisse o README à mão rodava um a menos. **Corrigido na v0.58, junto com a entrada do de Invocações.**

O `conferir-criacao.py` confere **instância** — *a ficha publicada na peça 8 obedece à fórmula?* —, e ele nasceu na v0.34 depois de aquela peça passar sete versões com a Defesa errada e a Trilha faltando, com os outros verdes o tempo todo.

O `conferir-ficha.py` confere **material**: as 23 perícias, os 11 ofícios, os 5 Caminhos, as 15 Trilhas e as constantes do nível 2 que a ficha de `05-material/` imprime, contra as peças donas. Ficha errada não fica num `.md` que ninguém abre — ela vira personagem, em sete mesas ao mesmo tempo.

O `conferir-legados.py` confere **catálogo**, e entrou na v0.39 junto com a peça 13. A checagem que mais rende é a que recalcula a tabela de totais da peça e falha se o escrito não bater com o contado — as contas do rascunho já tinham envelhecido duas vezes dentro do próprio arquivo antes de ele existir.

O `conferir-invocacoes.py` é o maior deles e faz as quatro coisas de uma vez, porque a peça 15 é máquina de construção: **regra** (o teto somado, o ritmo, os dois gatilhos de morte), **catálogo** (a régua de degrau contra as 19 entradas), **instância** (as montagens publicadas dos shikigami) e **busca exaustiva** (as 21.502 montagens que gastam o orçamento cheio no nível 30). Ele entrou na v0.58, com as trinta checagens que o §5 daquela peça vinha listando desde a v0.51.

O `conferir-catalogo.py` entrou na v0.85 e é o primeiro que **sai da pasta**: ele lê os três `DESENHO-*.md` da raiz, que até ali nenhum validador alcançava. A peça 17 é um índice das 90 entradas — 56 entregas de Trilha, 20 degraus de Caminho e as 14 Manhas — e ela não guarda preço nem texto de mesa, só nome e ponteiro. **A checagem que ela existe para ter é a sexta:** um bloco de regra não pode prometer permanência onde a linha de preço cobrou condição. *Foi essa contradição que deixou o nível 27 da `Estocada` valendo `5,31` fatias com preço de `1,33`, por três versões.*

E os dois do manual, que conferem número em vez de vocabulário:

```bash
cd manual/matematica && python3 pac7.py && python3 v7.py
```

**Antes de batizar qualquer coisa**, rode a triagem. Ela passa o nome contra o vocabulário inteiro do manual e do projeto, nas duas direções:

```bash
cd sistema/03-mecanica
python3 conferir-nomes.py --candidatos Vulto Matilha Bigorna
```

Ela já matou mais de dez nomes que pareciam livres — três só na v0.28, e um deles já estava escrito.

## Commitar

**O caminho de todo dia, e são duas linhas:**

```bash
jjk               # o atalho que entra nesta pasta
./subir.sh        # sem argumento: ele usa o mensagem-de-commit.txt e apaga depois
```

*É assim que o Mizuki commita.* O assistente deixa a mensagem pronta em **`mensagem-de-commit.txt`** e avisa; o `./subir.sh` sem argumento lê o arquivo, commita com ele e o apaga. **Mensagem curta também dá para passar direto:**

```bash
./subir.sh "v0.28 — tabela de XP"
```

Ele roda **todos os validadores** — os de `03-mecanica/`, o `conferir-repositorio.py` e os dois de `manual/matematica/` —, mostra o que mudou, commita e dá push, e **se recusa a commitar se algum falhar**. *Quantos são, exatamente, está na linha de versão no topo deste arquivo, e só lá — este parágrafo já disse "dezoito" e "quinze" enquanto eram dezenove e dezesseis, porque contagem copiada envelhece na versão seguinte (lição nº 9).*

### A entrega: o `subir.sh` copia, e você commita

**`finalizado/` é um repositório separado e não tem `subir.sh` próprio.** *O `.gitignore` dele
já segura o `mensagem-de-commit.txt`, então `add -A` é seguro.*

**Desde a v0.148 a cópia é do script.** *O passo `0. a entrega` roda antes dos validadores,
copia o que estiver velho, acerta a linha `Recorte da vX.Y.` do `README` da entrega, e **diz na
tela cada arquivo que mexeu**.* Se a entrega mudou, ele lembra o comando no fim — e o lembrete
está num `trap`, então ele aparece **também quando o script sai cedo**, que é quando dá para
esquecer.

```bash
cd finalizado && git add -A && git commit -m "recorte da vX.Y" && git push; cd ..
```

> **A versão da entrega sai do CONTEÚDO do último commit, e não do rótulo dele.** *Desde a v0.160 a checagem 7.4 lê a linha `**Recorte da vN.NN.**` do `README` da entrega **dentro daquele commit** — `git show HEAD:README.md` —, que é a mesma linha que o passo 0 mantém em dia.* **A mensagem continua sendo lida, e serve só para comparar: se ela discordar do conteúdo, sai um AVISO com os dois números.**
>
> **⚠⚠ Até a v0.159 ela lia a mensagem, e o buraco era dos dois lados.** *Uma entrega perfeitamente sincronizada reprovava se alguém copiasse a mensagem da vez passada — foi a v0.156, e custou três rodadas: o commit `cfcc885` levava conteúdo da v0.155 com a mensagem `recorte da v0.154`.* **E o lado pior nunca tinha aparecido: uma entrega DUAS versões atrasada passava batido se alguém escrevesse a mensagem certa por cima dela.** *Lição nº 9 na forma mais crua — o número existe no conteúdo e no rótulo, e nada comparava os dois.*
>
> ***O aviso não trava o commit, e isso é decisão.*** *Mensagem de commit já feito não se conserta sem reescrever história, e travar por causa dela seria travar contra o passado.* **Quem decide é o conteúdo; o rótulo só precisa parar de mentir na próxima vez.**
>
> **O `;` no lugar do último `&&` é de propósito:** *se o commit reclamar de `nothing to commit`, o `&& cd ..` não roda e você fica dentro de `finalizado/` sem perceber* — e aí o `./subir.sh` seguinte dá *"Arquivo ou diretório inexistente"*, porque a entrega não tem script próprio.
>
> **E a ordem, quando a entrega ficou para trás: rode o `./subir.sh` PRIMEIRO.** *O passo 0 sincroniza e suja a árvore da entrega; sem ele não há o que commitar.* **Ele para na 7.4, você commita a entrega, e roda o `subir.sh` de novo.**

> **A lista de arquivos não mora no `subir.sh`.** *Ela sai de `conferir-repositorio.py
> --recorte`, que é o mesmo lugar de onde a checagem 7.1 lê* — **uma lista, um dono**. E a
> versão sai de `--versao-recorte`, cujo dono é a entrada do topo do `CHANGELOG`. *Os dois modos
> imprimem e saem sem rodar checagem nenhuma, para a saída poder ser lida por script.*

> **A 7.1 não virou enfeite com isso.** *Ela continua pegando três coisas que a cópia não pega:
> quem editar a entrega direto, quem rodar o validador à mão, e a própria cópia falhando.*

> **A ordem normal é projeto primeiro, entrega depois** — o `subir.sh` roda a checagem 7.4
> antes de a entrega ser commitada, e por isso ela aceita a entrega estar **uma** versão
> atrás. **Se a entrega ficar DUAS atrás, a ordem inverte:** ela precisa ser commitada
> antes, senão o `subir.sh` do projeto se recusa a rodar. *Aconteceu na v0.146, porque o
> commit da entrega da v0.145 foi pulado.*

> **A entrega derivou QUATRO vezes por ser manual** — cinco versões na v0.121, duas na v0.135,
> uma pulada na v0.145, e duas peças mais os dois artefatos na v0.148. *Nas quatro o conserto foi
> o mesmo `cp` digitado de novo, e nas quatro alguém teve de lembrar.* **Foi a quarta que pagou
> o passo 0.**

Desde a v0.33 isso inclui uma trava a mais: **subir a versão no README, no `ESTADO-ATUAL` ou no `LEIA-ME` sem escrever a entrada do `CHANGELOG` falha o `conferir-repositorio.py`.** A entrada do topo do CHANGELOG é o dono da versão do projeto. Um commit que registra regra quebrada é pior que nenhum commit: daqui a três versões ninguém sabe em qual commit ela entrou.

> **O assistente não consegue commitar nesta pasta, e isso não tem conserto.** Ele lê, edita e roda os validadores normalmente, mas o `git commit` falha: o git finaliza cada objeto com *escreve temporário → `chmod` → `rename`*, e o mount pelo qual a pasta é exposta ao sandbox força permissão fixa e **rejeita o `chmod`** (`unable to set permission`). O objeto fica no disco pela metade — aparece no `ls` e não abre. Não é configuração do git; é como a pasta é montada. O commit é sempre seu.

> **E o assistente também não consegue *ler* o git daqui — nem `status`, nem `log`, nem `fsck`.** *Medido na v0.33.* Todos os três saem com `fatal: loose object <sha> is corrupt`, e **o repositório está inteiro**: dos 241 objetos soltos, o `ls` mostra os 241 com tamanho certo e o `open()` devolve ENOENT em **66 deles** — a mesma falha de mount descrita abaixo, aplicada ao `.git/`. Do seu lado, fora do sandbox, o git funciona normalmente. **Não trate esse "corrupt" como repositório quebrado**, e não rode `git gc` nem `git fsck --full` por causa dele.
>
> Um efeito colateral que morde: `git status` rodado do sandbox cria um `.git/index.lock` que ele **não consegue apagar** depois (`Operation not permitted`), e um lock preso trava o `./subir.sh`. Se o subir.sh reclamar de lock, apague o arquivo do seu lado — ele é vazio e descartável. **O jeito de evitar é não rodar git do sandbox.**

> **E o que dispara o sumiço tem nome, medido na v0.34: é a ferramenta de escrita, não o bash.** Arquivo que o **bash** grava, o bash lê de volta sempre. Arquivo que a ferramenta de escrita do assistente grava fica ENOENT para o bash com frequência — aconteceu seis vezes em duas versões, e o `README.md` e o `LEIA-ME.md` caíram juntos nas três últimas. **Consequência prática: validador e script novo se escrevem pelo bash**, com `cat > arquivo <<'EOF'`, senão eles nascem invisíveis para o próprio `python3`. Para `.md`, a ferramenta serve — só é preciso reconciliar com uma segunda escrita quando o sumiço acontecer.

> **O mesmo mount às vezes perde um arquivo que ele mesmo acabou de gravar.** Aconteceu com este README na v0.28: `stat` e `ls` mostravam tamanho e inode certos, e `open()` devolvia `ENOENT` — para o `head`, para o Python e para o `git` igualmente, enquanto os vizinhos na mesma pasta abriam normalmente. **O arquivo estava íntegro no disco**; quem não enxergava era o mount do sandbox. Aconteceu de novo na v0.29, com o `ESTADO-ATUAL.md`, e de novo na **v0.101**, em dois arquivos da raiz.
>
> **⚠ E a saída que este parágrafo dava até a v0.100 estava ERRADA.** *Ele dizia que "qualquer escrita nova reconcilia o mount, e uma edição de uma linha basta".* **Medido na v0.101: a escrita nova também sai ENOENT** — o `cat > arquivo` falha, o `cp` falha, e o arquivo continua fantasma.
>
> **O que reconcilia é escrever com OUTRO NOME e depois `mv` por cima.** *O `mv` não precisa abrir o destino, e o arquivo volta a existir com o conteúdo certo — conferido por md5 nos dois lados, nos dois arquivos.* **E o mesmo `mv` é o jeito de tirar arquivo da pasta**, já que apagar não dá: mande para `_to_delete/`, que o `.gitignore` segura, e apague a pasta a mão.

## O ciclo completo, quando o trabalho vem de um Project

O repositório é a fonte da verdade, e o Project do Claude lê dele. **A sincronização é manual**, então a ordem importa:

1. Trabalhar (aqui, no Cowork, ou onde for)
2. `./subir.sh "o que mudou"`
3. **No Project, clicar em "Sync now"** na fonte do GitHub

Pular o passo 3 é o jeito mais fácil de acabar com duas versões do projeto: o Project continua lendo o commit anterior e passa a discutir regra que já mudou. Se uma conversa começar a citar número que você sabe que não é mais o atual, sincronize antes de qualquer outra coisa.

## Regerar o manual

O `.docx` **não é editado à mão** — ele é gerado.

```bash
cd manual/gerador
npm install docx
node make.js
cp Fundamento-MANUAL-v7.docx ../Fundamento-MANUAL-v7.docx
```

`manual/gerador/COMO-USAR.txt` diz onde mexer em cada parte e traz o histórico de mudanças de cada versão do manual. **Rode `pac7.py` antes de gerar** se você mexeu em número, exemplo ou feitiço pronto.

O `.pdf` **está na v7.15, igual ao `.docx`**, desde a v0.93 — ele passou sete versões do manual atrasado porque era exportado a mão pelo Word. *Hoje sai de `soffice --headless --convert-to pdf`: 49 páginas.*

---

## Como o projeto trabalha

Isto não é preferência de estilo: é o que evitou os erros que estão registrados no CHANGELOG.

**Número vem de conta rodada, nunca de intuição.** Se dominância, deriva ou o filtro multi-mestre já decidem, a conta decide e ninguém pergunta. A pergunta é para onde a conta empata ou não se aplica.

**Escolha de sabor é do Mizuki** — quantos itens numa lista, quais são, como se chamam, em que ordem aparecem. Traga as opções com o número e o trade-off de cada uma já calculados, e pergunte. Várias rodadas de pergunta, nunca uma proposta grande pronta.

**Todo número novo ganha validador, com teste negativo conferido** — perturbar o valor e provar que a checagem certa acende. **E confira que a perturbação rodou de verdade:** uma que sai verde porque o validador pulou a checagem não provou nada.

**Peça substituída vai para `99-arquivo/`** com cabeçalho dizendo de onde saiu, o que a substituiu, em que versão, **por que morreu** e o que dela sobreviveu. A última linha é a que não dá para reconstruir depois.

**Antes de fechar versão, revisão cética** — inclusive contra o que você mesmo acabou de escrever. Metade dos achados grandes do CHANGELOG saiu daí.

**Documento não pode ter cara de saída de IA.** Seções de tamanhos diferentes, sem simetria forçada, sem "além disso" e "em suma". Português informal.

## Nove lições que custaram erro

1. **Numa rolagem disputada, os dois lados crescem no mesmo ritmo.** Verificar invariância contra o nível não basta — tudo que cresce numa campanha entra no teste. Foi o que pegou a maestria a cada quatro níveis (v0.9) e, com o dobro do tamanho, o refino na Defesa (v0.27).
2. **"Esse número já inclui o que eu estou somando nele?"** Errou em v0.16, v0.17, v0.19, v0.24, v0.26, v0.27 e v0.28. É o erro mais teimoso do projeto — na v0.28 foram dois calendários de feitiço que davam um extra no mesmo nível 10.
3. **Contagem não é valor.** Meça peso de mesa, não quantidade — Inteligência já teve mais perícias que Essência e valia menos.
4. **Antes de batizar, cheque colisão nas duas direções.** Hoje isso é o `conferir-nomes.py`.
5. **Tensão de preço às vezes é lacuna de texto disfarçada.** Confira se a regra diz o que você acha que ela diz antes de mexer no número. Pagou três vezes: duas na mesma Restrição, e uma na v0.28, quando a regra de ouro nº 6 já resolvia sozinha o caso que parecia pedir regra nova.
6. **Antes de aceitar um preço, veja se o termo que ele usa existe.** A Passiva Casca cobrava por *"dano físico"*, e a expressão aparecia **uma vez no manual inteiro — dentro dela mesma**. Hoje isso é o `conferir-manual.py`.
7. **Um preço se mede somado, nunca sozinho.** *Achado na v0.30, e ele derrubou três versões de método.* Toda conta de custo do projeto media uma peça contra o bolso inteiro — o que descreve um personagem que só faz aquilo. Uma ficha de verdade conjura, segura o que estiver segurando, e leva dano de alma que encarece feitiço, tudo ao mesmo tempo. E o erro contrário é igualmente fácil: a primeira correção supôs conjurar **toda rodada**, que nunca coube. Hoje isso é o `conferir-orcamento.py`.
8. **Uma checagem não pode se medir contra a própria constante.** *Três exemplares em três versões:* a dominância que não olhava o eixo dos feitiços (v0.28), o upkeep com `1.0` escrito na mão (v0.30), e o teto de níveis por missão comparado contra si mesmo (v0.32). Nos três, perturbar o número saía **verde**. O conserto é sempre separar *a regra aplicada* do *limite de design*, e checar as duas.
9. **Um número que mora em dois documentos vai divergir.** Não é "se", é "quando" — e cada cópia precisa de um dono declarado ou de um validador que compare as duas. O `conferir-repositorio.py` guardava `sete` no código e quebrou quando o oitavo validador entrou; o manual e o projeto contavam feitiço por calendários diferentes desde sempre. **Um número, um dono.** *E o exemplar mais caro apareceu na v0.33:* a **capa do manual** passou três versões dele e sete do projeto dizendo *"Versão 7.5"* — a única cópia que sai do repositório e vai para a mão de um jogador foi a última a ser conferida. Hoje a checagem 4 do `conferir-repositorio.py` confere onze cópias contra três donos.

## O que existe, e o que não existe

**Dá para montar uma ficha de nível 2, jogar uma missão inteira e recuperar entre elas**, por **oito das nove rotas de Origem** — e sem nenhum buraco de regra que morda nessa faixa. *Eram seis até a v0.122, quando a peça 20 destravou o Corpo Amaldiçoado e o ramo sem energia da Restrição Celestial.* **A nona é `Sem Técnica`, e ela tem criação própria — decisão do Mizuki.**

**O que não existe, e faz falta: o playtest.** `04-playtest/` continua vazia — **zero sessões desde a v0.1, e todo número do sistema é previsão.**

> *Esta frase tinha quatro itens e perdeu três.* **A pasta `05-material/` saiu na v0.35**, quando a ficha e o gerador dela entraram; **a tabela consolidada saiu na v0.99**, quando virou a peça 18; **e o quick-start saiu na v0.102, por decisão do Mizuki** — *"pode abandonar a ideia do quick start, eu tô fazendo o PDF direto"*.

> **O texto de mesa passa a ter um destino só: o PDF**, e ele se escreve a partir do repositório de entrega. *A skill `redacao-acessivel-rpg` continua sendo a travessia de "nota de design" para "texto de regra" — o que mudou é onde ela desemboca.*

> **E esse PDF existe agora, na v0.106.** `sistema/05-material/livro/` tem o Manual da Guilda inteiro — 230 páginas, com o quick-start escrito direto nele, no molde que a v0.103 previu: *"como o PDF carrega essa propriedade é trabalho dele"*.

A tabela de XP saiu dessa lista na v0.32 — ela era a trava nº 1 de mundo compartilhado, ficou aberta trinta versões, e hoje é a peça 12. **Com ela, o que falta para alguém sentar na mesa deixou de ser regra e passou a ser material.**

A seção *"O que existe e o que não existe, medido"* do `ESTADO-ATUAL.md` tem a conta.

## Licença e escopo

Material de fã, sem fins comerciais, não afiliado à Shueisha, à MAPPA nem a Gege Akutami. Jujutsu Kaisen e seus personagens pertencem aos detentores originais.

**O repositório é público desde a v0.44** — era privado até ali, e ficou público porque a autenticação por HTTPS custava mais atenção do que o sigilo valia. Ele existe para o trabalho da Guilda; qualquer um pode ler, ninguém precisa.
