# Composição da R67

Os PDFs desta edição saíram da mesma cadeia de geração da R66, rodada com o texto da R67. Nenhum ajuste de diagramação foi preciso: as cores, a paleta noturna e as regras de página são as da R66.

Fonte: LIVRO-COMPLETO-R67.md. Alterações textuais: ../alteracoes/R66-para-R67.json, com 17 trocas em 5 blocos. As trocas já trazem os seis ajustes de clareza feitos na composição (revisar_clareza_r67.py), que não mudam número nem regra.

## Onde ela roda

A cadeia completa fica fora do repositório, em /home/mizuki/CHAT-GPT/RPG -JJK/desenvolvimento-fundamentos/revisao-didatica-r57-v1/revisao-r67. É uma cópia da pasta da R66 (revisao-integral-pos-r65), que ficou intocada com as provas aprovadas. O gerador grava arquivos dentro da própria pasta, por isso cada edição trabalha numa cópia.

Os passos, de dentro de composicao/:

1. LIVRO-CANDIDATA.md, na pasta acima, recebe o texto da edição.
2. gerar_livro.py gera o PDF claro.
3. gerar_noturno_r57.py deriva o noturno do claro, com a mesma paginação.
4. conferir.py, na pasta acima, roda as 65 verificações e a auditoria do Índice.

**O Python do sistema não tem o reportlab.** A geração roda com o Python que acompanha o Codex, em /home/mizuki/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3, que tem reportlab, pypdf e Pillow. O conferir.py precisa também do pymupdf, que esse Python não tem: ele roda num ambiente com os dois. Sem o reportlab, o gerador quebra na primeira linha e o noturno é recolorido a partir do claro antigo, com a mesma contagem de páginas. Confira a data e o tamanho do PDF claro antes de confiar no noturno.

## O que foi conferido

- 65 de 65 verificações do conferir.py, em evidencias/VALIDACAO.json e evidencias/conferir.log.
- Os 453 verbetes do Índice com número impresso e link certos, em evidencias/AUDITORIA-PAGINAS-INDICE.json.
- As páginas que mudaram contra a R66, em evidencias/COMPARACAO-R66.json: 11, as mesmas nas duas paletas.
- A revisão visual dessas páginas nas duas paletas, em evidencias/REVISAO-VISUAL.json.

Os scripts em composicao/ preservam a implementação desta rodada. Como na R66, não formam um pacote autônomo de geração: fontes, arte e componentes herdados ficam na cadeia local.
