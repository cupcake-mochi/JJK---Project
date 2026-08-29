# O livro — Projeto M · Manual da Guilda

O texto final de mesa, pronto para imprimir. É onde o `README.md` da raiz falava do
quick-start abandonado na v0.102: *"o texto de mesa passa a ter um destino só, e é o
PDF"*. É esse PDF, escrito direto a partir desta pasta.

## O que tem

| | |
|---|---|
| `manual/*.md` | **a fonte.** 20 arquivos, um por capítulo (ou peça de frente), com dois dígitos e um nome na frente do `.md`. É aqui que se edita |
| `build/build.py` | markdown → HTML semântico → PDF, via WeasyPrint. Gera também o índice remissivo |
| `build/build_docx.py` | markdown → `.docx` de revisão, sem diagramação — para comentar |
| `build/build_txt.py` | markdown → texto corrido, um arquivo só — para Ctrl+F e diff |
| `build/manual.css`, `marcas.css` | a diagramação. `marcas.css` é gerado pelo `build.py`, não editar à mão |
| `build/duas-colunas.css` | a folha extra da diagramação de duas colunas, com a medida dos três manuais do hobby escrita no topo |
| `arte/Capa-v0.1.jpg` | **a capa de arte**, provisória. O `build.py` usa ela se existir, e avisa e segue sem ela se não existir. *Ela já vem recortada em proporção A4 exata — `1697×2400` —, e é pintada como **fundo do `@page`** e não como `<img>`: com `<img>` sobrava um fio branco de 1 a 2 px na direita, porque o `overflow` corta na borda da página e o que passa dela não chega ao canvas* |
| `Projeto-M-Manual-da-Guilda.pdf` | o livro compilado, em coluna única |
| `Projeto-M-Manual-da-Guilda-C-duas-colunas.pdf` | o mesmo conteúdo em duas colunas |
| `Projeto-M-Manual-da-Guilda-A-atual.pdf` | **snapshot**, guardado a mão na v0.126 para comparar. Não se regera |
| `Projeto-M-Manual-da-Guilda-REVISAO.docx` | mesmo conteúdo, sem diagramação |
| `Projeto-M-Manual-da-Guilda-TEXTO.md` | texto corrido, para revisão |
| `ESTADO-revisao.md` | o registro da revisão: números antes/depois, o que mudou e por quê |
| `METODO-volta-do-docx.md` | **como uma revisão feita no Word volta para o markdown.** O oposto da passada de texto: aqui número de regra muda, e o método existe para proteger isso |
| `REMOCOES-material-de-mestre.md` | o que saiu do livro do jogador, e onde cada coisa precisa voltar a existir (a maior parte aponta para um futuro livro do mestre, que não existe ainda) |

## Três diagramações, para comparar

*Decisão em aberto na v0.126 — o Mizuki pediu as três lado a lado.*

| | páginas | o que ela é |
|---|---|---|
| `-A-atual` | 256 | o que estava publicado antes desta leva. Snapshot, não se regera |
| *(sem sufixo)* | 239 | a mesma coisa, com as quebras de página consertadas e o sumário em duas colunas |
| `-C-duas-colunas` | 139 | corpo em duas colunas a 9,4pt com entrelinha 1,45, e grade de 5+ colunas em largura inteira |

**A geometria da C não é gosto: ela foi medida em três manuais do hobby.** *Guia do Mestre 5e em A4, Caldeirão de Tasha e PHB 2024* — 83%, 92% e 92% das páginas em duas colunas, com corpo entre 9,1 e 9,3pt. **A mancha copiada é a do Guia do Mestre**, que é o único dos três em A4.

> **⚠ O WeasyPrint 69 não implementa `column-span: all`.** *Medido: um `h2` e uma `table` marcados com ele continuaram presos dentro da coluna da esquerda.* **Por isso a tabela larga não escapa pelo CSS — ela é tirada do fluxo de colunas no `build.py`, em `segmenta_colunas`.** *Se um dia o WeasyPrint passar a implementar, aquela função vira uma linha de CSS.*

**Três coisas que a v0.127 mediu e que valem para qualquer mexida futura:**

- **`column-fill` é `balance`, e não `auto`.** *Com `auto` a coluna da esquerda enche antes de a direita começar, e todo bloco curto sai com a direita vazia.*
- **O corte de tabela larga é a GRADE, não o número de colunas nem a largura em caracteres.** *`ncols >= 4` marcava 40 tabelas e furava o fluxo 40 vezes; largura em caracteres marcaria 176, porque conta célula de prosa como se não quebrasse.*
- **Entrelinha de coluna estreita é 1,45 e não 1,62.** *O que sobrava de página quase vazia eram duas a sete linhas transbordando.*

## Como regerar

Precisa de `markdown`, `beautifulsoup4`, `weasyprint` e `python-docx` (`pip install` os
quatro). E das fontes do projeto instaladas no sistema — Barlow Condensed (Regular,
SemiBold, Bold), Spectral (Regular, Italic, SemiBold, SemiBold Italic), IBM Plex Mono
(Regular) e Noto Serif CJK (para os kanjis de abertura de capítulo). Sem elas o WeasyPrint
cai para uma fonte substituta e a diagramação sai errada, sem avisar.

```bash
cd build
python3 build.py            # PDF em coluna única
python3 build.py --duas     # PDF em duas colunas
python3 build_docx.py       # docx de revisão
python3 build_txt.py        # texto corrido
```

O `manual.html` é intermediário e as duas variantes sobrescrevem ele. Rodar as duas em
sequência é seguro; ler o `.html` depois só mostra a última.

## O que já mudou aqui, e o que ainda não

**Fechado nesta leva:** organização, referência cruzada, glossário, índice remissivo, corte
de material de mestre, e um quick-start jogável escrito direto no PDF — o molde que a v0.102
decidiu, agora com texto de verdade dentro dele.

**Ainda em aberto**, e registrado em `REMOCOES-material-de-mestre.md`:
- ~~o `PvP` cortado do capítulo 9 precisa de um lugar~~ **livro do mestre, decidido na v0.130**
- ~~treino de arma por Caminho foi escrito pela primeira vez aqui, e ainda não tem validador~~
  **foi para a peça 6 §8.0 na v0.130, com a checagem 12 do `conferir-equipamento.py` comparando
  a peça contra este livro**
- ~~duas divergências achadas no caminho, que são bug do sistema e não do livro: a regra 5
  das Regras de ouro do Fundamento, e a tabela de Classe Passiva 3 do capítulo de Aptidões~~
  **as duas fecharam na v0.107, do lado da fonte** — o texto do livro já estava certo
