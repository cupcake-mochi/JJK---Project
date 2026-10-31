# Guia do Mestre — edição diagramada pré-1.0

> **Fila vigente - registro 147, 30/10/2026:** três ajustes editoriais concluídos: folhas curtas primeiro, falas e comentários distintos, avisos repetidos reduzidos. [PDF de 383 páginas, pacote de impressão e revisão](<../04 - Planejamento/147-ajustes-de-consulta-e-leitura.md>). Geradores HTML e PDF em `apoio-editorial-147`. Próximo: plano de avaliação da dificuldade dos encontros; GPT-6 Astra, esforço extra alto. Retorno da pré-1.0 pode ser incorporado desde já. Salvamento local; último GitHub: registro 141.

> **Fila histórica - registro 146, 30/10/2026:** comparação editorial da etapa 8 concluída, com [parecer, matriz das 20 competências e notas da edição](<../04 - Planejamento/146-comparacao-final-e-proximos-ajustes.md>). Primeira missão reunida, preparo mínimo e variedade demonstrados; equivalência geral ainda parcial. **Próximo: três ajustes editoriais — folhas curtas primeiro, distinção de falas e comentários, redução de avisos genéricos repetidos nas ideias; GPT-6.1 Sol, esforço alto.** Depois, conferir texto e PDF afetados e incorporar retorno da pré-1.0. Dificuldade geral dos encontros permanece em frente mecânica separada. PDF atual de 383 páginas, HTML e regras inalterados neste lote. Geradores: PDF 145; HTML 144. Salvamento local; último GitHub: registro 141.

> **Fila histórica - registro 145, 30/10/2026:** PDF integrado atualizado, com **383 páginas**, composto a partir das 99 fontes revistas e inspecionado visualmente por inteiro em painéis, com ampliações selecionadas. [PDF, revisão e estado salvo](<../04 - Planejamento/145-pdf-integrado-e-revisao-visual.md>). Tipografia do livro base, sumário e remissões clicáveis; texto, HTML e regras preservados. **Próximo: comparação editorial final, etapa 8; GPT-6 Astra, esforço extra alto, conforme o plano 98.** Ajustes decorrentes: GPT-6.1 Sol, esforço alto. Gerador do PDF em `apoio-pdf-145`; gerador HTML continua no registro 144. O PDF anterior de 357 páginas permanece intacto. Salvamento local; último GitHub: registro 141.

Abra o [PDF integrado revisto](output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0-Revisado.pdf). A versão anterior permanece disponível no mesmo diretório, com o nome sem “Revisado”.

Para atualizar o PDF vigente, use [o gerador do registro 145](<../04 - Planejamento/apoio-pdf-145/GERAR-PDF.py>) e siga [as instruções de composição e conferência](<../04 - Planejamento/apoio-pdf-145/LEIA-ME.md>). Ele lê a edição integrada atual; o gerador antigo desta pasta monta uma versão histórica e não deve substituir a entrega revisada.

## Histórico da diagramação anterior

**Atualização histórica — registro 93, 26/10/2026:** capítulo 1 revisado; PDF com 359 páginas, inspeção de todas as páginas após a repaginação. Próxima tarefa: capítulo 2, GPT-6.1 Sol, esforço alto. Consulte o [relatório da revisão](<../04 - Planejamento/93-revisao-editorial-do-capitulo-1.md>). As descrições anteriores registram a entrega 92.

Abra o [livro em PDF](output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf). Ele usa o padrão tipográfico da R53, com duas colunas, tabelas na largura útil, sumário, remissões e índice clicáveis. O aprofundamento da obra fica no apêndice D, sinalizado por conter revelações.

O [relatório de revisão crítica](<../04 - Planejamento/92-revisao-critica-e-edicao-diagramada.md>) informa as mudanças e os limites. Esta é uma edição para leitura e avaliação, não uma declaração de equilíbrio em mesa.

## Arquivos que acompanham o livro

- `MAPAS.py`: cinco diagramas vetoriais; revisar junto aos exemplos quando mudarem medidas ou posições.
- `fontes/`: fontes utilizadas e licenças.
- `imagens/`: capa e quatro referências selecionadas do acervo da R53; autoria e capítulo nas legendas.
- `revisao/selecao-visual.json`: opções comparadas e razões de escolha.
- `revisao/alteracoes-textuais.json`: alterações nas fontes editáveis.
- `revisao/composicao.json`: páginas, remissões, fontes e notas transferidas.
- `revisao/revisao-visual.json` e `revisao/pranchas/`: registro da revisão e provas reduzidas de todas as páginas.
- `revisao/preservacao-do-conteudo.json`: comparação por amostras textuais e controle de links.

## Atualização

Corrija primeiro as fontes numeradas em `06 - Redacao do Guia` ou o piloto correspondente em `04 - Planejamento`. Regere a edição HTML pelo programa da pasta07; depois execute `GERAR-PDF.py` desta pasta. O programa usa Python, ReportLab, BeautifulSoup e Pillow. Para os controles adicionais, use PyMuPDF e Poppler. As fontes locais evitam depender das fontes instaladas no computador.

A composição estabiliza automaticamente as remissões paginadas. Qualquer mudança pode deslocar páginas: gere novas imagens com Poppler e examine todas as páginas alteradas, inclusive a continuação do capítulo. Não considere a ausência de sobreposição como prova de boa leitura. Verifique a unidade de parágrafos, títulos, exemplos e tabelas; evite dividir um parágrafo curto apenas para nivelar duas colunas.

As provas em pranchas servem para conferir o conjunto. Para avaliar tamanho e leitura, amplie a página no PDF ou renderize uma imagem de página inteira. As fichas de registro são modelos impressos, sem campos eletrônicos interativos.

**Próxima tarefa:** incorporar retorno e revisar os pontos identificados — GPT-6.1 Sol, esforço alto. Contradições mecânicas amplas — GPT-6 Astra, esforço extra alto.
