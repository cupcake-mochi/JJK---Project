# Passada de texto — como se mede, e como se lê o que a medida diz

O `medir-voz.py` produz oito números. Este arquivo é o que diz o que fazer com eles.

Os dois existem separados de propósito: **o script mede, e este documento julga.** Quem
mistura os dois acaba com um validador que decide corte sozinho, e corte de texto é a única
coisa deste projeto que nenhum validador consegue decidir — a `REGRA-DE-VOZ.md` já declara
isso na seção *Fora do alcance do validador*.

```bash
cd sistema/05-material/livro && python3 medir-voz.py
```

Os quatro manuais ficam em `PDFs - Sistemas Extras/PDF_Sistemas/`, fora do repositório, por
serem material comercial de terceiro. Sem eles o script sai e não mede meio corpus.

---

## O que uma passada de texto pode fazer

Cortar narrativa, enfeite, argumento de design e material de mestre. Reescrever regra que
está mal-vestida. Trocar ponteiro por posição — *"a tabela acima"* — por ponteiro por nome.

## O que ela nunca faz

**Mudar número de regra.** Nenhum. A cada arquivo mexido, antes de aplicar:

```bash
python3 build/guard_numeros.py manual/<antes>.md manual/<depois>.md
```

Diferença não é proibida — um título que perde `As duas` perde um numeral por extenso — mas
**cada diferença tem que ser lida contra a linha que a carregava**, e explicada, antes de a
mudança entrar. A v0.136 leu 104 diferenças assim, uma a uma. A v0.137 saiu com a notação
idêntica em cinco dos nove arquivos mexidos.

E ela também não corta a única dona de um fato. Comentário de efeito às vezes carrega uma
regra que não está escrita em mais lugar nenhum: na v0.136, três das dezesseis linhas
`Na mesa:` que saíram eram donas de quem decide alguma coisa, e as três viraram regra escrita
com todas as letras **antes** de a frase sair.

---

## As oito marcas, e como ler cada uma

A tabela abaixo diz o que a marca é e o que um número alto quer dizer. **Ela não traz os
valores** — os valores saem do script, e um número copiado para cá envelhece na versão
seguinte, que é a lição nº 9 do `README`.

| marca | o que ela conta | número alto quer dizer |
|---|---|---|
| prosa | frases sem número nenhum dentro | ou tem narrativa, ou tem regra escrita em frase curta. **A marca não separa as duas** |
| palavras por frase | mediana | frase longa cansa quem lê no meio da mesa |
| `você` | quantas frases falam com o leitor | quase nada — os quatro manuais variam de 8 a 404, então não existe faixa certa |
| `não é X, é Y` | antítese fechada | enfeite quase sempre. É a única das oito em que alto é sentença |
| `, e não` | antítese aberta | **quase sempre regra.** Ver abaixo |
| `em vez de` | contraste | nada. Já está na faixa deles |
| analogia `como se` / `como quem` | comparação | nada. Já está na faixa deles, e hoje **abaixo** dela |
| equação `é o/a X que` | definição por equivalência | frase de efeito onde cabia a regra direta |

### O `, e não` é a armadilha desta lista

Ele mede altíssimo e quase nunca é para cortar. A v0.137 leu as 47 ocorrências à mão e achou
que a maioria era regra: *"perde uma, e não todas"*, *"e não vira dado"*, *"e não se
empilham"*. **Cortar ali apaga regra.**

E tem um efeito que confunde: conforme a passada corta narrativa, esta marca **sobe**, porque
o denominador encolhe e as frases de regra ficam. Subiu entre a v0.137 e a v0.139 sem ninguém
escrever uma linha nova. Isso é sinal de que a passada funcionou, não de que ela falhou.

### A prosa não é o que o nome promete

*"Frase sem número"* conta como prosa toda regra escrita em sentença curta — *"Você não usa
Ação Bônus"*, *"Restrição paga Melhoria"*. Os capítulos de regra pura são feitos disso.

A v0.137 projetou que a prosa cairia para perto da do PHB e ela quase não se moveu, com a
narrativa toda cortada. **A medida honesta de uma passada é a contagem de palavras**, e não
essa. Esta marca serve para escolher onde olhar primeiro, e para nada mais.

---

## Número alto não é ordem de corte

É a regra que este documento existe para carregar, e ela custou três diagnósticos errados numa
tarefa só, na v0.137:

| a medida disse | o que era |
|---|---|
| equação altíssima | o regex casava `[ée]` e **pegava a conjunção "e"** |
| antítese `não é X, é Y` altíssima | o mesmo defeito. Com o verbo só, sobraram três no livro inteiro |
| antítese `, e não` altíssima | número certo, **fenômeno errado** — quase todas eram regra |

Os dois primeiros são o mesmo bug de expressão. O terceiro é pior, porque **o número estava
certo**: nenhuma revisão de regex teria achado ele. Só ler as 47 achou.

> **Antes de cortar numa marca, leia uma amostra dela.** Se a amostra for regra, a marca não
> é candidata a corte naquele capítulo — por mais alta que ela esteja.

E os quatro manuais ficam baixos em várias dessas marcas por **registro de tradução**, não por
serem mais enxutos. Comparar contra eles diz onde a gente destoa; não diz que destoar é defeito.

## Corpo pequeno mente

As marcas são taxa por mil frases. Num capítulo de 15 ou 20 frases — a introdução, o
vocabulário — **uma ocorrência só vira uma taxa de dois dígitos.**

*Medido na v0.139:* o vocabulário deu equação `66,7` e a introdução `47,6`, e as duas eram
uma ocorrência cada.

**Abaixo de umas 60 frases, leia a contagem crua e ignore a taxa.** O script imprime o número
de frases de cada corpus justamente para isso.

---

## O que já foi decidido, e não se recorta de novo

Estas quatro fecharam com medida ou com decisão do Mizuki. Reabrir custa versão e não rende.

**Analogia e `em vez de` ficam.** Medidas contra os quatro: nas duas o projeto já escreve como
eles escrevem. *E a v0.139 mediu a analogia **abaixo** do piso dos quatro — ela caiu de arrasto
nas passadas de ficção, sem ninguém mirar nela. Cortar mais ali deixa o livro mais seco que os
modelos dele.*

**As cinco marcas de "isto ainda está sendo escrito" ficam.** Decisão da v0.129: quando a frase
de estado carrega uma permissão ou um limite que o jogador precisa, ela fica. As que só contavam
o estado do projeto já saíram.

**Tabela-prévia sai, tabela de contraste fica.** Critério da v0.106. Prévia é quando todas as
colunas repetem o texto adjacente; contraste é quando a tabela põe os itens num eixo que a
prosa não alcança. *A v0.138 tirou 26 de Legado por esse critério, oito versões depois de ele
ser escrito.*

**Um Legado nunca diz o que o PNJ faz.** Ele diz o que existe no mundo por sua causa, o que
você sabe, ou onde você entra. Saiu de ler o antecedente do PHB 2024, que entrega atributos,
Talento, perícias, ferramenta e equipamento — e nenhuma característica social.

---

## Entrada de catálogo se escreve nas quatro camadas, e isso é obrigatório

*Decisão do Mizuki na v0.141.* A forma está na `REGRA-DE-VOZ.md` e ela deixou de ser "a forma
da família condição": vale para condição, Bênção, aptidão, Passiva, `Estigma`, Legado e entrega
de Trilha — **qualquer coisa que o leitor procura pelo nome e lê sozinha.**

O sintoma do que está fora é medível: **rótulo em negrito com mais de seis palavras.** Nessa
largura ele parou de ser *nome do efeito* e virou *a regra*, e o leitor perde o índice visual
que existe para ele achar a linha que quer sem ler a entrada inteira.

*Medido na v0.141: **nove entradas, doze rótulos**, e seis das nove no capítulo das Bênçãos.*

> **O `Bocado` foi o exemplar, e ele durou dezenove versões.** *Abria com metáfora — "o que você
> carrega passa a viver dentro de você" — e a regra que o jogador usa toda rodada, o saque a
> mais, estava no terceiro parágrafo sem nome nenhum.*

## Quando um bloco sai, a frase que anuncia ele sai junto

No mesmo commit. Três vezes em duas versões um corte deixou ponteiro pendurado:

- o `Como ler uma aptidão` prometendo descrições que tinham acabado de sair
- os três `Como ler` de Legado dizendo *"cada tabela de X traz…"* depois de as tabelas saírem
- o `Como ler uma Origem` prometendo *"cada um com a sua tabela"*

É barato de evitar e caro de achar depois: as três estavam gramaticalmente perfeitas.

**A família maior disso é a frase que virou mentira sem ninguém mexer nela.** A v0.129 achou
duas lendo, e nenhuma regex acha: elas falam de um estado do projeto que era verdade quando
foram escritas. Toda passada tem que perguntar, de cada afirmação sobre o sistema, se ela ainda
é verdade — não só se ela está bem escrita.

---

## O procedimento, na ordem

1. `python3 medir-voz.py` — escolhe onde olhar primeiro. Não decide corte.
2. **Ler o capítulo.** É a única etapa que acha alguma coisa. As três famílias que as passadas
   anteriores acharam — metáfora no lugar da regra, aviso escrito de trás para frente,
   contabilidade do projeto vazando para o livro — saíram todas de leitura, nenhuma de medida.
3. Todo script de recorte leva **`assert` de corpus não vazio e de contagem esperada antes de
   escrever**. Na v0.136 o filtro das linhas `Na mesa:` errou duas vezes antes de acertar, e o
   `assert` segurou as duas. Na v0.137 ele salvou três cortes que teriam apagado regra.
4. `guard_numeros.py` em **cada** arquivo mexido, com **cada** diferença explicada.
5. `conferir-voz.py --estrito` de volta em **0 achados**, e as triagens relidas — o validador
   não julga se é *"por que o mundo é assim"* (fica) ou *"por que o livro é assim"* (sai).
6. Os 22 validadores de `03-mecanica/`, o `conferir-repositorio.py` da raiz e os dois de
   `manual/matematica/` — todos com **PULADA = 0**.
7. Os três builds regerados: `build.py`, `build.py --duas`, `build_docx.py`.
8. Entrada nova no `CHANGELOG`, que é a dona da versão.

> **O passo 2 é o que rende, e é o que a medida convida a pular.** A v0.137 começou pelo
> código com o pedido sendo para ler, e gastou três diagnósticos errados antes de desistir da
> medida. O achado de playtest daquela versão — um leitor se perdendo no `Arquivo`, porque a
> regra estava na linha que o capítulo manda ler como não-regra — não tem marca que o pegue.

## Onde os números vivem

Neste arquivo, nenhum, fora os que estão datados por versão como leitura de um momento.

Os oito da medida saem do `medir-voz.py`, rodado na hora. A ordem dos capítulos sai de
`build/build.py`, na lista `CHAPTERS` — **ela não é a ordem alfabética dos nomes de arquivo**,
e confundir as duas põe o `Descanso e Recuperação` no capítulo 16 quando ele é o 5.

A régua de voz é a `REGRA-DE-VOZ.md`. O que é livro de jogador e o que é livro de mestre é a
`REMOCOES-material-de-mestre.md`. As nove lições que custaram erro são do `README.md` da raiz,
e só de lá.
