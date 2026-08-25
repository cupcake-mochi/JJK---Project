# Pente fino · o texto que entrou depois da última passada

*Leitura fechada em 25/08/2026, contra a v0.147. **Nada foi aplicado** — este arquivo é a
lista, e a aplicação é conversa separada.*

O recorte é o que o pedido dizia: **texto novo, sem passada.** A última leitura de verdade
foi a sexta, na v0.137. De lá para cá entraram **336 linhas** em 19 dos 20 arquivos de
`manual/`, e o grosso é da v0.147 — o `Criar o seu Legado`, a `Versado`, a caixa de Teste de
Resistência das Manhas, o dano na arma em dois capítulos —, mais o `Bloquear` que virou
capítulo na v0.143 e as sete Passivas escritas na v0.141.

**O que a medida disse antes de eu ler: nada.** `conferir-voz.py --estrito` volta em `0`
achados, `11` triagens, `7` marcas contra um dono que diz `7`, `89` termos com destino e
nenhum sem. Os 24 validadores de `03-mecanica/` passam com `PULADA = 0`, o
`conferir-repositorio.py` fecha as `251` checagens, e os dois de `manual/matematica/` também.
**Os dezesseis achados abaixo saíram todos de ler**, que é o que o `METODO-passada-de-texto.md`
avisa no passo 2 e que continua sendo verdade na sétima passada seguida.

---

## 1 · A trava nova do `Desliga` contradiz seis dos treze `Desliga` publicados

**É o achado grande desta leva, e ele é de regra e não de texto.**

O `Criar o seu Legado`, escrito na v0.147, manda usar as entradas publicadas como molde e
descreve a forma de cada grupo. No `Desliga` ele escreve uma trava que nunca tinha existido:

> **`Desliga`** — apaga uma coisa que aconteceria com você, sem rolagem, toda vez que a
> situação aparecer. **Ele só apaga o que ninguém comprou** — nunca anula uma habilidade, um
> feitiço ou um item de outra ficha.

**Seis dos treze `Desliga` do capítulo fazem exatamente isso.** Cinco deles são da forma
*"você não fica `<condição>`"*, e condição é a coisa mais comprada do sistema — existe uma
Melhoria `Condição` no Fundamento cujo preço é o nível dela.

| entrada | linha | o que ela apaga | quem compra isso |
|---|---|---|---|
| `Revezamento` | 193 | `Impedido` | Melhoria `Condição`, preço `Pesada` |
| `Cabo` | 257 | `Desarmado` | Melhoria `Condição` |
| `Coleira` | 254 | **"técnica nenhuma te localiza, te rastreia ou te encontra à distância"** | qualquer técnica de outra ficha |
| `Usado` | 321 | `Derrubado` | Melhoria `Condição`, preço `Leve` — **e é o que a Manha `Abalo` entrega** |
| `Talhe` | 383 | `Agarrado` | Melhoria `Condição` |
| `Assinado` | 630 | `Cego` | Melhoria `Condição`, preço `Pesada` |

E mais duas que ficam na fronteira: o `Peso Real` (*"o que engana feiticeiro não engana
você"* — barreira e véu são coisa que alguém montou) e a `Máscara`, que anula a leitura de
quem rolou `Sentir Energia`.

> **O `Usado` é o exemplar mais cru.** *A `Abalo` é a Manha da categoria `Massa`, escrita na
> tabela `Manhas` do capítulo 8: o alvo cai, condição `Derrubado`.* **Uma ficha com `Usado`
> apaga, uma vez por cena, a entrega que outra ficha comprou pagando a `Escola de Arma` no
> nível 2.** *A trava nova diz que isso não acontece. Acontece, e está publicado desde antes.*

**São três saídas possíveis, e a escolha é sua:**

1. **A trava está certa e o catálogo está errado** — aí seis entradas precisam de revisão de
   preço, o que é versão própria.
2. **A trava está errada** — o `Desliga` sempre apagou coisa comprada, e a frase certa é
   outra: *"ele nunca desliga a ficha de outra pessoa, só o que chega em você"*.
3. **A trava vale só para `Desliga` escrito pelo jogador** — e aí ela tem de dizer isso, porque
   o parágrafo logo acima manda usar as publicadas como molde, e o molde e o exemplo estão
   dizendo coisas opostas.

*A terceira é a mais barata e é a que eu apostaria, mas é escolha de sabor e a conta não
decide.*

---

## 2 · A peça 9 §5 ainda diz *"sem PE"*, e o livro está na frente dela

**Desta vez a divergência é ao contrário do de sempre: o livro está certo e a fonte está
atrás.**

O livro, em `25-origens.md:534`, escreve a linha da Restrição Celestial assim:

> *sem energia:* sem Fundamento, sem feitiço de Toque, sem Sentir Energia, **sem aptidão e sem
> refino**

e logo abaixo: *"O `PE` do seu Caminho continua chegando. Nesta rota ele se lê **Pontos de
Esforço**."*

**A peça 9 §5, na linha 200, ainda tem a versão de antes da v0.116:**

> *sem energia:* sem Fundamento, **sem PE**, sem feitiço de Toque, sem Sentir Energia

**E a própria peça 9 diz, duas vezes, que essa frase morreu.** A linha 260: *"Uma Origem que
diz 'sem PE' com todas as letras entra em contradição com os cinco"*. A linha 317: a pendência
está riscada, com **FECHADO na v0.116** do lado. A peça 6, na linha 313, escreve a regra que
saiu daquilo: *"a coluna `por nível` vem inteira, e ela continua se chamando `PE`"*.

> **A frase morta já se espalhou.** *A peça 16 cita ela duas vezes — nas linhas 201 e 305 —
> como se fosse a regra viva: "está na peça 9 §5, junto de `sem PE` e `sem feitiço de Toque`".*
> **Três lugares carregam hoje uma frase que uma quarta linha do mesmo arquivo declara
> aposentada há trinta e uma versões.**

*Nenhum validador podia pegar.* A checagem 10 do `conferir-repositorio.py` pergunta se o livro
publica o que as peças escrevem — **presença**, não **concordância**. Ela conta os 20 termos e
os 86 Legados e fica verde. Duas cópias da mesma linha dizendo coisas diferentes passam por
baixo dela inteiras.

---

## 3 · O `Custo` do `Bloquear` publica metade do número, e contradiz a abertura da própria seção

O capítulo 1 abre o `Bloquear` dizendo, com todas as letras, que a troca é neutra:

> **Na média dá exatamente a sua Defesa.** […] Você troca um número certo por dois dados, e
> **não ganha nem perde nada com a troca**.

Trinta linhas depois, a seção `Custo` diz:

> **Um em cada doze golpes vai passar porque você rolou, quando a sua Defesa parada teria
> segurado.** O `Aparar` e a `Brecha` saem em cerca de 1% das rolagens cada um, e são eles que
> você está comprando.

**O número está certo — eu enumerei as 2.000 combinações e ele dá `8,2%`, que é 1 em 12.**
O problema é que ele é **metade de um par simétrico**, e a metade que ficou de fora é a que
sustenta a frase da abertura:

| | taxa |
|---|---|
| o Bloquear **traiu** — passou o que a Defesa parada teria segurado | `8,2%` |
| o Bloquear **salvou** — segurou o que a Defesa parada teria deixado passar | `8,2%` |

*Medido aqui, e batendo com o dono:* a peça 23 §7.1 escreve **"o tráfego é `16,5%`, dividido
igual: `8,2%` salvou e `8,2%` traiu"**, e a checagem 3 do `conferir-bloquear.py` existe
justamente para falhar se os dois divergirem — *"a assimetria seria o viés que a peça existe
para não ter"*.

> **E a frase não foi escrita para o jogador.** *Ela é cópia literal da peça 23 §7.1, cujo
> título é `O que medir no playtest — e é o oposto do que eles vão comentar`, e cuja linha
> seguinte é uma instrução ao mestre: "Pergunte no fim da sessão quantas vezes Bloquear custou
> caro, não quantas vezes salvou".* **É material de mestre que atravessou para o livro do
> jogador levando o enquadramento junto** — a família do `REMOCOES-material-de-mestre.md`.

Do jeito que está, quem lê a seção `Custo` fecha o capítulo achando que `Bloquear` é prejuízo
líquido. **A mesma rolagem que trai um em doze salva um em doze, e é isso que faz a regra ser
o que a abertura promete.**

*E o segundo parágrafo do `Custo` — "o outro preço é tempo de mesa: uma rolagem a mais por
golpe recebido" — é argumento de design puro. Ele não muda nada do que o jogador faz na mesa,
e a passada anterior cortou coisa igual em cinco capítulos.*

---

## 4 · A caixa de Teste de Resistência das Manhas enumera treze de catorze

A caixa nova da v0.147 fecha assim:

> **As que não pedem** são as que mexem em você ou no seu próprio dado — `Talho`, `Raspão`,
> `Encaixe`, `Racho`, `Palmo`, `Zunido` e `Estampido`.

**Sete nomes.** Somados às seis que pedem, dá treze — que era o número certo até a `Versado`
entrar, na mesma versão, quarenta linhas abaixo.

A `Versado` dá `+1` no acerto para você mesmo: **pelo critério ela é do grupo que não pede**, e
pela enumeração ela não é de grupo nenhum. *É a enumeração fechada que o item novo quebrou, e
ela quebrou no mesmo commit que criou o item.*

> *O `METODO` chama essa família de **"a frase que virou mentira sem ninguém mexer nela"** e
> diz que regex nenhuma acha. Esta aqui é a variante mais barata dela: a frase virou mentira
> porque a lista ao lado cresceu.*

---

## 5 · A `Versado` é invisível de onde o leitor procura por ela

O degrau que entrega Manha é o nível 2 da Vanguarda, e ele diz:

> **Nível 2: `Escola de Arma`.** Escolha uma das treze categorias de arma. Com armas daquela
> categoria você usa a **Manha** dela. *As treze estão na seção seguinte.*

Quem lê isso vai para a seção, encontra a tabela `Manhas` com treze linhas, lê as duas caixas
de regra, e **não tem motivo nenhum para continuar**. A `Versado` mora num `####` depois de
tudo isso, e nada antes dela diz que ela existe.

**Ela também não aparece na tabela** — e nisso está certa: ela não tem categoria, porque é
justamente a que se leva no lugar da categoria. *O que falta é a linha que manda olhar.*

`Versado` aparece **três vezes no livro inteiro**, todas dentro da própria seção. Fica abaixo
do corte do vocabulário (`5` usos ou `3` capítulos), então nenhum validador reclama — e o
resultado prático é uma entrega publicada que só acha quem ler o capítulo inteiro de ponta a
ponta.

---

## 6 · A cláusula `Classe 0` da `Defesa sem Armadura` não pode acender

O dano na arma entrou em dois lugares na v0.147, e o de baixo é cópia adaptada do de cima. A
adaptação pegou a escala certa e deixou passar a exceção:

> **`45-aptidoes-e-refino.md:141`** — *"E se o seu ataque já estiver somando um feitiço de dano
> de `Classe 0` ou mais — **como no nível 2 da `Brasa`, que põe um `Classe 0` junto do
> soco** —, este dano não se soma por cima."*
>
> **`47-bencaos-e-lapidacao.md:102`** — *"E se o seu ataque já estiver somando um feitiço de
> dano de `Classe 0` ou mais, este dano não se soma por cima."*

**A `Defesa sem Armadura` é Bênção, e Bênção vale para uma rota só.** A linha 3 daquele mesmo
capítulo: *"Bênção e Lapidação valem para **uma** rota de criação: a Restrição Celestial pelo
ramo **sem energia**"*. E a linha do ramo, em `25-origens.md:534`: *"sem Fundamento, sem
feitiço de Toque"*.

**Quem tem essa Bênção não conjura.** A cláusula descreve uma situação que a única rota que a
alcança nunca vai viver.

> **E tem um segundo fundo, que é mais interessante que o primeiro.** *Se a cláusula está viva,
> é porque alguma coisa entrega feitiço a uma ficha sem Fundamento — e o candidato existe: a
> Trilha `Brasa` do Bastião, cujo `Fagulha` no nível 2 diz "você pode lançar um feitiço de
> **Classe 0** como ação bônus".* **Nada no livro impede uma Restrição Celestial sem energia de
> escolher Bastião e `Brasa`.** *Aí a cláusula acende — e o buraco não é de texto, é de sistema,
> e é bem maior: uma Trilha entregando feitiço para quem a Origem diz que não conjura.*

**As duas leituras pedem coisa diferente**, e vale decidir qual antes de mexer: ou a cláusula
sai do capítulo 12, ou o capítulo 8 ganha a linha que diz o que as Trilhas conjuradoras fazem
numa ficha sem energia.

---

## 7 · O `Criar o seu Legado` virou segundo dono das três seções `Como ler`, e as duas cópias já divergem

O capítulo de Origens agora explica os três formatos **duas vezes**: no `## Legados`, no
começo, e no `## Criar o seu Legado`, no fim. **As duas versões não dizem a mesma coisa, e elas
nasceram divergentes no mesmo commit.**

| | `Como ler um X` (começo) | `Criar o seu Legado` (fim) |
|---|---|---|
| `Destranca`, trava | *"nunca mexe em acerto, CD ou dano"* | *"não mexe em acerto, CD nem dano, **e nunca decide o que outra pessoa faz**"* |
| `Ajusta`, relógio | *"quanto mais largo o que ele alcança, mais raro o relógio"* | *"**ele carrega relógio sempre**, e quanto mais largo…"* |
| `Ajusta`, o exemplo estreito | *"um que pega **uma condição** só vale por cena"* | *"o que pega **uma situação** só vale por cena"* |
| `Desliga`, contagem | *"a maioria vale sempre, sem contagem"* | *(sumiu)* |
| `Desliga`, trava | *(não tem)* | *"**ele só apaga o que ninguém comprou**"* |

*É a lição nº 9 do `README` na forma mais pura que este projeto já registrou: **um número que
mora em dois documentos vai divergir** — só que aqui não precisou de "quando", divergiu na
escrita.*

> **Duas das cinco diferenças são melhorias de verdade**, e vale dizer: **o `Ajusta` carrega
> relógio sempre está CERTO** — eu conferi as `40` entradas publicadas e as `40` têm relógio.
> *A versão de cima é que era frouxa.* **A saída não é apagar a de baixo: é uma dona só, e ela
> tem de ser a versão boa.**

---

## 8 · O aviso do objeto de apoio está escrito de trás para frente

No capítulo 10, o aviso que entrou na v0.147:

> **⚠ Escolha com cuidado, porque ela cobra tarde.** O ataque extra que Bastião e Vanguarda
> ganham no nível 7 é um golpe simples, e ele sai na Ação de Atacar. Se o seu objeto é do tipo
> que você só carrega, esses dois Caminhos passam a valer bem menos na sua ficha.

**Duas linhas depois vem a isenção:**

> **O Corpo Amaldiçoado fere maldição com o golpe simples, seja qual for o objeto.**

São duas as rotas que montam poder na Técnica Marcial, e **o aviso só vale para uma delas**.
Escrito sem dizer para quem é, ele assusta metade dos leitores que o alcançam, e a metade
assustada só descobre que não era com ela no parágrafo seguinte.

*O `METODO` já nomeia essa família — **"aviso escrito de trás para frente"** — como uma das
três que as passadas anteriores acharam lendo.* **O conserto é de uma frase: nomear a rota
dentro do aviso, ou trocar os dois blocos de ordem.**

---

## 9 · `objeto de apoio` é usado na primeira caixa do capítulo 14 e definido 147 linhas depois

A caixa de abertura do capítulo, linha 3:

> Uma ferramenta amaldiçoada é uma arma do catálogo de Equipamento **(ou um objeto de apoio)**
> mais um `Estigma`.

O `Sintonizar`, escrito na v0.147, usa de novo na linha 21: *"são as suas mãos, mais dois
objetos de apoio"*. **A definição está na linha 150**, dentro do `## Teto de Estigma`:

> **Objeto de apoio** é a ferramenta que você carrega sem empunhar: um anel, um cordão, uma
> peça costurada no forro do casaco.

Nenhuma das duas primeiras aponta para lá. *E o capítulo 10 manda o leitor para cá justamente
atrás disso: "a categoria que o capítulo 14 abre ao lado do catálogo de armas".*

**É a família do `colado`** — o termo chega marcado como coisa conhecida e a definição está em
outro lugar sem ponteiro. *A diferença é que aqui ele não está entre crases, então o
`conferir-voz.py` não tem como ver.*

---

## 10 · O `Bocado` carrega um `Na obra:` que as outras seis Passivas não têm

As sete Passivas do capítulo 10 se escrevem todas na mesma forma de quatro camadas — nome com
travessão, âncora de quando vale, nome de cada efeito em negrito, e a Classe Passiva no fim.
**Uma delas tem um bloco a mais**, e ele fica fora da caixa:

> **Na obra:** o Toji guarda o arsenal inteiro numa maldição em forma de verme, comprime ela
> numa bola e engole.

O `**Na obra:**` é a forma da família **Origem** — ele aparece oito vezes no capítulo 7, uma
por Origem, e em lugar nenhum mais como bloco rotulado. *Aqui ele foi emprestado para uma
entrada de catálogo, e só para uma das sete.*

**São dois problemas de uma vez:** a forma migrou de família sem passar pela `REGRA-DE-VOZ`, e
a entrada ficou assimétrica em relação às seis irmãs. *Ou as sete ganham, ou esta perde — e
"na dúvida, corta" já resolveu isso mais de uma vez neste livro.*

---

## Os cinco menores

**A `Versado` abre pela regra, e as sete Passivas ao lado abrem pela âncora.** *`Calo` — "vale
sobre qualquer arma que você já empunhou uma vez". `Raiz` — "vale contra qualquer coisa que
tente tirar você do lugar".* **A `Versado` abre com o efeito e põe o `Quando.` depois**, que é
a ordem que a `REGRA-DE-VOZ` inverte de propósito: *a frase de âncora diz quando a regra vale,
e nunca o que ela faz.* É uma linha reescrita.

**O `Bocado` e a `Versado` mexem no mesmo botão, e nenhuma cita a outra.** *A regra base é do
capítulo 2: um saque de graça por turno, e trocar de arma é dois.* **O `Bocado` dá dois de
graça — o que já torna a troca gratuita — e a `Versado` vende exatamente "a troca vira um gesto
só".* Uma ficha pode ter as duas (o `Bocado` é Passiva de Técnica Marcial, a `Versado` é Manha
de Vanguarda, e os eixos são independentes), e nessa ficha a `Versado` fica valendo só o `+1`
no acerto, tendo custado a Manha inteira. *Não trava nada; só é bom saber antes de precificar.*

**A `Brecha` ficou de fora do vocabulário e o `Aparar` entrou.** *Os dois são os dois extremos
da mesma rolagem, apresentados na mesma caixa.* A `Brecha` tem 2 usos em 1 capítulo e fica
abaixo do corte de `5` usos ou `3` capítulos, então está formalmente certa — **mas quem
aprendeu que o vocabulário tem `Aparar` vai procurar `Brecha` lá e não achar.**

**Onze ponteiros por posição sobreviveram, e os onze escapam do `TABELA-VAGA`.** *Li o motivo
no código, não na saída:* são **dois** motivos e não um. Três deles estão dentro de linha de
tabela, e o `conferir-voz.py` faz `continue` em toda linha que começa com `|` **antes** de
chegar na checagem. Os outros oito escapam pela expressão: `POSICAO` procura `\ba tabela\b`,
então `na tabela abaixo`, `pela tabela abaixo`, `nas tabelas acima` e `o catálogo acima` nunca
casam. *A lista: `10-como-jogar:142`, `15-dano:53`, `15-dano:305`, `40-fundamento:372`,
`:693`, `:919`, `:943`, `50-equipamento:116`, `55-ferramenta:42`, `60-invocacoes:183`,
`:209`.* **O pior é o `40-fundamento:693`, que manda ler "a tabela logo abaixo" quando são
três tabelas abaixo.**

**Um erro de digitação, em `12-pericias-e-oficios.md:130`:** *"**Natureza** — planta, bicho,
clima, terreno. O que é venenoso, **que vale enche**, quando a chuva vem."* **A frase não
fecha.** Ela entrou na v0.139, na reescrita do capítulo, e passou sete versões.

---

## E uma coisa que não é do livro: o `conferir-bloquear.py` só roda em Python 3.12+

Rodando os 24 validadores, **23 passam e um não chega a executar**:

```
File "sistema/03-mecanica/conferir-bloquear.py", line 234
    f'{"todos sao a `Talha`" if _suspeitas else "nenhum e' de outra peca"}')
                                                                        ^
SyntaxError: unterminated string literal
```

A aspa simples de `e'` fecha a f-string por fora. **Isso é erro de sintaxe até o Python 3.11 e
deixou de ser no 3.12**, quando a PEP 701 passou a permitir reusar a aspa dentro da expressão.
*Na sua máquina roda — se não rodasse, o `subir.sh` não teria deixado a v0.143 fechar.*

**O que ele custa é portabilidade:** qualquer pessoa da Guilda com 3.11 não consegue rodar o
`subir.sh` nem conferir o `Bloquear`. Varri os outros 47 arquivos `.py` do repositório e este é
o único. *Conserto de um caractere:* trocar `e'` por `e` na frase, ou a aspa externa por `"`.

---

## O que eu conferi e voltou limpo

Vale registrar, senão a próxima leitura refaz.

- **As treze condições batem nos três lugares** — `15-dano` tem 13 entradas `####`, a tabela
  `Condições em uma linha` tem 13 linhas, e o vocabulário tem 13. `Impedido` está vivo nos três.
- **A tabela `Perícias e ofícios` fecha:** 34 linhas, 23 perícias e 11 ofícios, e a distribuição
  por atributo é a que o parágrafo abaixo dela publica — Inteligência 11, Essência 7, Destreza
  4, Força 1.
- **Os `40` `Ajusta` publicados têm relógio, os `40`.**
- **O `Bloquear` fecha na conta:** média de `2d10` é 11, `Aparar` e `Brecha` saem em 1% cada,
  e o `1 em 12` do `Custo` é o `8,2%` da peça 23 — o número está certo, o que falta é a
  outra metade.
- **A `Integridade` nova bate ponta a ponta:** `20 + (Essência + 5) × (nível − 1)` no capítulo 1
  dá o `25 + Essência` da criação e o `26` da Kaori no nível 2 e da ficha do início rápido.
- **Os onze `Estigma` são onze**, e o `Bojo` é mesmo o único que só serve para quem conjura.
- **O `Cisão` é mesmo o único *dano direto na alma* do livro**, como o capítulo 4 afirma.
- **Nenhum dos sete termos novos ficou sem destino** pelo corte de `5` usos ou `3` capítulos.

---

## A fila, se for para aplicar

*Ordem por custo, não por importância — os três primeiros grupos não mexem em número nenhum e
o `guard_numeros.py` sai idêntico.*

1. **Uma frase cada:** o typo da `Natureza`, a ordem do aviso do objeto de apoio (§8), a
   âncora da `Versado` (§ menores), o ponteiro para a `Versado` dentro da `Escola de Arma` (§5),
   e a `Versado` entrando na enumeração da caixa de Teste de Resistência (§4).
2. **Dona única para os três formatos de Legado** (§7), ficando com a versão boa de cada linha.
3. **A metade que falta no `Custo` do `Bloquear`** (§3), e o corte do parágrafo de tempo de mesa.
4. **Os onze ponteiros por posição** (§ menores) — e, junto, os dois furos do `TABELA-VAGA`,
   que são no validador e não no texto.
5. **A trava do `Desliga`** (§1) — precisa da sua decisão entre as três saídas antes de virar
   texto.
6. **A cláusula `Classe 0` do capítulo 12** (§6) — precisa que a pergunta da Trilha conjuradora
   numa ficha sem energia feche antes.
7. **O *"sem PE"* da peça 9 §5** (§2) e as duas citações dele na peça 16 — é a fonte que muda,
   não o livro, e é a única da lista que mexe em peça de regra.

> **O `conferir-bloquear.py` é independente de tudo isso** e pode ir sozinho, a qualquer
> momento.
