# O livro — Projeto M · Manual da Guilda

O texto final de mesa, pronto para imprimir. É onde o `README.md` da raiz falava do
quick-start abandonado na v0.102: *"o texto de mesa passa a ter um destino só, e é o
PDF"*. É esse PDF, escrito direto a partir desta pasta.

## O que tem

| | |
|---|---|
| `manual/*.md` | **a fonte.** 18 arquivos, um por capítulo (ou peça de frente), com dois dígitos e um nome na frente do `.md`. É aqui que se edita |
| `build/build.py` | markdown → HTML semântico → PDF, via WeasyPrint. Gera também o índice remissivo |
| `build/build_docx.py` | markdown → `.docx` de revisão, sem diagramação — para comentar |
| `build/build_txt.py` | markdown → texto corrido, um arquivo só — para Ctrl+F e diff |
| `build/manual.css`, `marcas.css` | a diagramação. `marcas.css` é gerado pelo `build.py`, não editar à mão |
| `Projeto-M-Manual-da-Guilda.pdf` | o livro compilado |
| `Projeto-M-Manual-da-Guilda-REVISAO.docx` | mesmo conteúdo, sem diagramação |
| `Projeto-M-Manual-da-Guilda-TEXTO.md` | texto corrido, para revisão |
| `ESTADO-revisao.md` | o registro da revisão de organização: números antes/depois, o que mudou e por quê |
| `REMOCOES-material-de-mestre.md` | o que saiu do livro do jogador, e onde cada coisa precisa voltar a existir (a maior parte aponta para um futuro livro do mestre, que não existe ainda) |

## Como regerar

Precisa de `markdown`, `beautifulsoup4`, `weasyprint` e `python-docx` (`pip install` os
quatro). E das fontes do projeto instaladas no sistema — Barlow Condensed (Regular,
SemiBold, Bold), Spectral (Regular, Italic, SemiBold, SemiBold Italic), IBM Plex Mono
(Regular) e Noto Serif CJK (para os kanjis de abertura de capítulo). Sem elas o WeasyPrint
cai para uma fonte substituta e a diagramação sai errada, sem avisar.

```bash
cd build
python3 build.py         # PDF
python3 build_docx.py    # docx de revisão
python3 build_txt.py     # texto corrido
```

## O que já mudou aqui, e o que ainda não

**Fechado nesta leva:** organização, referência cruzada, glossário, índice remissivo, corte
de material de mestre, e um quick-start jogável escrito direto no PDF — o molde que a v0.102
decidiu, agora com texto de verdade dentro dele.

**Ainda em aberto**, e registrado em `REMOCOES-material-de-mestre.md`:
- o `PvP` cortado do capítulo 9 precisa de um lugar — apêndice opcional ou livro do mestre
- treino de arma por Caminho foi escrito pela primeira vez aqui, e ainda não tem validador
  nem existe em `sistema/03-mecanica/`
- ~~duas divergências achadas no caminho, que são bug do sistema e não do livro: a regra 5
  das Regras de ouro do Fundamento, e a tabela de Classe Passiva 3 do capítulo de Aptidões~~
  **as duas fecharam na v0.107, do lado da fonte** — o texto do livro já estava certo
