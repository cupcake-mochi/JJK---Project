# Composição da R68

Os PDFs desta edição saíram da mesma cadeia de geração da R67, rodada com o texto da R68. Nenhum ajuste de diagramação foi preciso.

Fonte: LIVRO-COMPLETO-R68.md. Alterações textuais: ../alteracoes/R67-para-R68.json, com 2 trocas em 2 blocos.

## Onde ela roda

Esta foi a primeira composição feita no Windows. A cadeia é uma cópia da pasta da R67 em D:\Projetos\CHAT-GPT\RPG -JJK\desenvolvimento-fundamentos\revisao-didatica-r57-v1\revisao-r68, a mesma árvore que no Linux fica em /home/mizuki/CHAT-GPT/RPG -JJK/.

Para rodar no Windows, mudaram três coisas, e nenhuma é do texto ou da diagramação:

- `densidade_editorial.py` lia Bree Serif, Barlow Condensed Bold e IBM Plex Mono Medium das pastas de fonte do Linux. Agora lê da pasta fontes-linux, ao lado do script. Os arquivos de fonte não estão no repositório.
- O Python é um ambiente virtual com as versões do Python do Codex: reportlab 4.4.9, pypdf 6.10.0 e Pillow 12.3.0, mais o pymupdf para o conferir.py.
- Rodar com `PYTHONUTF8=1`. Sem ele, o Python do Windows lê os `.md` e `.json` como cp1252 e o gerador quebra.

**A prova de que a cadeia é a mesma:** antes de trocar o texto, a R67 regerada no Windows saiu idêntica, byte a byte, aos dois PDFs publicados (`c6fef62b…` e `475a226f…`).

Os passos, de dentro de composicao/, são os da R67:

1. LIVRO-CANDIDATA.md, na pasta acima, recebe o texto da edição. O LIVRO-COMPLETO.md de dentro de composicao/ também.
2. gerar_livro.py gera o PDF claro, em uns 3 minutos.
3. gerar_noturno_r57.py deriva o noturno do claro, com a mesma paginação.
4. conferir.py, na pasta acima, roda as 65 verificações e a auditoria do Índice.

## O que foi conferido

- 65 de 65 verificações do conferir.py, em evidencias/VALIDACAO.json e evidencias/conferir.log.
- Os 453 verbetes do Índice com número impresso e link certos, em evidencias/AUDITORIA-PAGINAS-INDICE.json.
- A comparação página a página com a R67, por texto e por pixels, em evidencias/COMPARACAO-R67.json: só as páginas 268 e 395 mudaram, as mesmas nas duas paletas, e nenhuma das 1769 âncoras mudou de página.
- A revisão visual dessas páginas nas duas paletas, em evidencias/REVISAO-VISUAL.json. O link novo da página 268 leva à Técnica Máxima, na página 277.

Os scripts em composicao/ preservam a implementação desta rodada, incluindo o `densidade_editorial.py` com o caminho de fonte novo. Como na R67, não formam um pacote autônomo de geração: fontes, arte e componentes herdados ficam na cadeia local.
