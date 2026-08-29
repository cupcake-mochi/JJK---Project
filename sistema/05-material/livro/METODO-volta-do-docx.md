# Volta do .docx — como uma revisão feita no Word entra no markdown

O `METODO-passada-de-texto.md` é o método de **cortar texto por conta própria**, com o
`medir-voz.py` decidindo onde. Este aqui é o oposto: **alguém já decidiu, fora do
repositório, e o trabalho é trazer a decisão de volta sem perder nada e sem inventar nada.**

Ele nasceu da v0.176, quando o Mizuki leu as 251 páginas no Word e devolveu **205 edições em
21 arquivos**. Vale para qualquer documento gerado deste repositório que volte editado.

> **A diferença que manda no resto:** na passada de texto, número de regra **nunca** muda.
> Aqui ele muda, e é justamente o que o método precisa proteger.

---

## A primeira pergunta, antes de qualquer coisa

**O arquivo editado é saída, e a fonte é outra.** Antes de abrir o editado, escreva em que
arquivo cada pedaço dele nasce. Sem esse mapa, a edição volta para o lugar errado ou não
volta.

No caso deste livro o mapa tem dono: a lista `CHAPTERS` do `build/build_docx.py`. **Leia o
dono, não a memória** — a ordem do `.docx` não é a ordem alfabética dos arquivos, e a peça de
frente não tem número de capítulo.

---

## Os seis passos

### 1. Extrair os dois lados, e diferenciar

Extrair só o editado não serve para nada: o que interessa é o **delta**, e para ter delta
você precisa da saída antiga com o mesmo extrator.

```bash
cd sistema/05-material/livro/build
python3 docx2md.py ../Projeto-M-Manual-da-Guilda-REVISAO.docx /tmp/original.md
python3 docx2md.py <o-editado>.docx                            /tmp/revisado.md
diff -u /tmp/original.md /tmp/revisado.md > /tmp/diff-completo.txt
```

**Use o mesmo extrator nos dois lados.** Um `.docx` reserializado pelo Word difere do
gerado em coisas que não são edição — espaço, quebra de run, ordem de atributo. Passar os
dois pelo mesmo extrator apaga essa camada e deixa só o que a pessoa mexeu.

**Confira as marcas de revisão antes.** `.docx` é um zip:

```bash
unzip -o -q <o-editado>.docx -d /tmp/docx && ls /tmp/docx/word/comments.xml
grep -c "<w:ins \|<w:del " /tmp/docx/word/document.xml
```

Comentário mora no *word/comments.xml* de dentro do zip, e o `docx2md.py` **não lê**; alteração controlada mora
em `<w:ins>`/`<w:del>` e ele lê como se fosse texto final. Se algum dos dois existir,
pergunte antes de aplicar. *Cuidado com o falso positivo: `w:insideH` e `w:insideV` são borda
de tabela e casam com um `grep w:ins` descuidado.*

### 2. Contar antes de ler

```bash
grep -c "^@@" /tmp/diff-completo.txt
```

E depois quebrar o diff por capítulo, ancorando cada `@@` no `# Título` que veio antes dele.
**A contagem por capítulo é o que dimensiona o trabalho e o que ordena a leitura**: um
capítulo com 49 hunks pede outra estratégia que um com 2.

### 3. Ler o diff inteiro **antes** de tocar em qualquer arquivo

Não intercale leitura e edição. O diff tem dependência entre pedaços distantes — um degrau
renomeado no capítulo 8 aparece de novo no 12, um `Estigma` que muda de grau reaparece no
glossário. **Quem edita enquanto lê aplica a primeira ocorrência e não sabe que existem
mais três.**

O que se procura na leitura:

| o que | o que fazer com isso |
|---|---|
| **troca de palavra** | aplicar direto |
| **corte de parágrafo** | conferir se ele era o dono único de algum fato |
| **número que mudou** | anotar, e caçar todas as cópias antes de aplicar |
| **frase nova** | conferir se ela contradiz uma frase que ficou |
| **anglicismo, nome de arquivo, nota entre parênteses** | é rascunho vazando; decidir e reportar |

### 4. Aplicar por substituição exata, um arquivo por vez

Substituição de string exata, com **contagem obrigatória**: se o alvo não aparece exatamente
uma vez, pare e olhe.

```python
n = s.count(alvo)
if n != 1:
    print(f"!! {n} ocorrências: {alvo[:70]!r}")
s = s.replace(alvo, novo, 1)
```

Zero ocorrências quer dizer que a extração normalizou alguma coisa — crase, negrito, travessão
— e o alvo real está diferente. Duas quer dizer que o mesmo texto existe em dois lugares, e é
exatamente aí que mora a lição nº 9.

**Reescreva na sintaxe do markdown, não na do extrator.** O `docx2md.py` devolve
`**assim**` mas perde a crase de termo de sistema, o `> ` do bloco de regra e o
`{: .tab-titulo }` da tabela. Copiar o extraído literalmente destrói a diagramação sem que
nenhum validador acuse.

### 5. Guarda de número, arquivo a arquivo

```bash
python3 build/guard_numeros.py /tmp/antes/<arquivo>.md manual/<arquivo>.md
```

Igual à passada de texto — **cada diferença lida contra a linha que a carregava** — com uma
diferença de leitura:

- **Número que aparece** é acréscimo, e tem de bater com uma linha nova do diff.
- **Número que some** é o perigoso. Ou saiu junto com um bloco que a revisão apagou, ou é
  regra apagada sem querer.

Quando a saída fica longa, o atalho é comparar só as linhas que carregam dígito:

```bash
diff /tmp/antes/<arquivo>.md manual/<arquivo>.md | grep -E "^[<>].*[0-9]"
```

Isso põe lado a lado o antes e o depois de cada número, e a explicação sai sozinha.

### 6. Regerar os quatro, e conferir

```bash
cd build && python3 build.py && python3 build.py --duas
python3 build_docx.py && python3 build_txt.py
cd .. && python3 conferir-voz.py --estrito
cd ../../.. && python3 conferir-repositorio.py
cd sistema/03-mecanica && for v in conferir-*.py; do python3 $v; done
```

**Rode os quatro builds depois da última edição**, e não no meio. A checagem 7.5 do
`conferir-repositorio.py` compara a data da fonte com a dos artefatos, e uma correção
depois do build derruba ela.

---

## O que fazer quando o documento se contradiz

É o caso que separa este método do outro, e ele **vai** acontecer: quem edita em Word não vê
as outras cópias do número que acabou de mudar.

**A regra é: o documento é a fala final sobre a DECISÃO, e não sobre a COBERTURA dela.**

- Se a pessoa mudou um número em três lugares e recalculou um exemplo com ele, a decisão está
  tomada. Propague para as cópias que sobraram — elas são derivadas, não são uma segunda
  opinião. *Na v0.176 a `Fura` foi de `3 × Classe` para `2 × Classe` em três lugares, com o
  `15` do `Ponto Final` virando `10`; as outras quatro cópias eram aritmética da mesma regra.*
- Se duas frases discordam e **nenhuma** é derivada da outra, não escolha. Aplique as duas
  como estão e reporte a colisão com as duas citações. *Na v0.176: `não dá para trocar ação` e
  `Ação Padrão pode virar Ação Bônus` ficaram na mesma seção.*
- Se um número novo não fecha com a fórmula que está uma linha acima dele, aplique e reporte.
  *`1/3 do refino` com `refino 10` dá `3`, e a revisão escreveu `+4`.* **Perguntar rende:** os
  três casos da v0.176 voltaram como decisão consciente, e dois deles pediram conserto do
  texto que ficou — a frase antiga que dizia o contrário, e a fórmula que agora precisava
  declarar a exceção.

**Reporte cada cópia que você propagou, uma a uma, com o antes e o depois.** É o que permite
reverter sem reabrir o `.docx`.

---

## O que sai da conta, e por quê

Nem tudo que aparece no diff é edição de livro.

**Ruído de extração.** Palavra colada (`oucom`), `**` no meio de uma frase, linha em branco
que apareceu ou sumiu dentro de bloco de regra. O `build_docx.py` junta linhas e o
`docx2md.py` desjunta diferente. **Nada disso é edição** — se o único delta de um hunk é
espaço, pule.

**Tabela que o `.docx` nunca teve.** O `walk()` do `build_docx.py` percorre blockquote por
`find_all(["p"], recursive=False)`: uma tabela dentro de `>` **não chega no Word**. Ela some
dos dois lados do diff e parece intocada. *Antes de concluir que um bloco foi apagado,
confira se ele existia no extraído original.*

**Nota de trabalho.** Handle de pessoa entre parênteses numa célula, `(Em revisão - Não usar)`,
palavra em inglês no meio da frase. É rascunho vazando para a saída. Aplique, e reporte
separado — quem escreveu decide se fica.

---

## O que este método NÃO faz

**Não corta por conta própria.** Se o texto ficou pesado depois de aplicar, isso é assunto do
`METODO-passada-de-texto.md`, em outra versão.

**Não conserta a fonte.** Quando a revisão apaga do livro uma coisa que a peça de
`03-mecanica/` ainda escreve, o livro fica certo e a peça fica pendente. Isso é achado para
reportar, e não conserto para fazer no mesmo commit: a peça é dona da regra, e mexer nela é
decisão de design.

**Não mexe em validador para o texto passar.** Se uma checagem para de achar o que procurava
porque a frase que a carregava saiu, o número virou órfão — e quem decide se ele volta ao
texto ou se a checagem muda de alvo é quem escreveu, não quem aplicou. *Quando a decisão vier
e for tirar o lugar da lista, tire com o motivo escrito no código, e **rode o teste negativo
depois**: perturbe uma das publicações que sobraram e prove que a checagem ainda acende. Um
reconhecedor que ficou sem alvo passa verde para sempre — é a lição nº 8 aplicada ao
reconhecedor.*

---

## A conta final que vai no relatório

Sempre estes, medidos e não estimados:

- hunks aplicados, e em quantos arquivos
- palavras antes e depois (`cat manual/*.md | wc -w` dos dois lados)
- páginas antes e depois, nos dois PDFs (`pdfinfo`)
- toda mudança de **número de regra**, uma linha cada
- toda cópia propagada além do que o documento trazia
- todo validador que mudou de estado, com o que ele parou de conferir
