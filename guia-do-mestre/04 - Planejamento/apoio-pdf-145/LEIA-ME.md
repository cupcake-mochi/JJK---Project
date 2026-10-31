# Composição do PDF revisto

Registro 145. Trabalho sobre as 99 fontes fechadas no registro 144. O PDF anterior de 357 páginas permanece intacto. A nova composição fica em `08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0-Revisado.pdf`.

O gerador lê a edição integrada, mantém as fontes e as medidas do Livro de Regras 1.0 e integra o complemento do capítulo 3 sem duplicá-lo. As folhas ficam no apêndice A, os casos no B, os termos no C e o aprofundamento com revelações no D. As referências fecham o volume.

## Arquivos de trabalho

- `GERAR-PDF.py`: composição vigente; não executar o gerador antigo da pasta 08 sobre este texto.
- `CONFERIR-PDF.py`: extração independente, margens, sobreposições, ligações e preservação das fontes.
- `RENDERIZAR.py`: imagens de todas as páginas e painéis numerados para inspeção.
- `requirements.txt`: bibliotecas usadas; o ambiente de execução desta sessão fica em `/tmp/ciclo-guia-pdf-145` e pode ser recriado se necessário.
- `composicao.json`: ordem, destinos, geometria, entradas e hash da saída.
- `conferencia-do-pdf.json`: resultados da verificação automática.
- `renderizacao.json`: PDF correspondente às páginas renderizadas.
- `referencia-visual.json`: livro base efetivamente consultado e opções de imagem reavaliadas.
- `primeira-prova`, `segunda-prova` e `terceira-prova`: etapas anteriores desta composição.

## Estado da revisão

Composição fechada em 383 páginas. Todas foram inspecionadas visualmente em 43 painéis, com ampliações selecionadas, incluindo os nove mapas. A página 194 também foi renderizada com Poppler e inspecionada. O hash da saída é o mesmo nos registros de composição, conferência, renderização e revisão visual.

- `revisao-visual.json`: cobertura efetiva, ampliações, correções das quatro provas e limites da inspeção.
- `conferencia-do-manifesto.json`: auditoria do estado anterior e união dos artefatos deste lote, produzida no fechamento.
- [Relatório e próxima etapa](../145-pdf-integrado-e-revisao-visual.md).

A próxima etapa é a comparação editorial final prevista na etapa 8 do plano 98: GPT-6 Astra, esforço extra alto; ajustes e consolidação com GPT-6.1 Sol, esforço alto. O salvamento deste lote é local; o último envio remoto continua sendo o registro 141.

## Reproduzir a saída

Recrie um ambiente Python com `requirements.txt` se o ambiente temporário não existir. Execute `GERAR-PDF.py`, depois `CONFERIR-PDF.py` e `RENDERIZAR.py`. Alterações de conteúdo devem acontecer primeiro nas fontes vigentes, seguidas da atualização HTML. O programa confere os hashes das entradas e exige atualizar a lista de fontes conscientemente quando o manuscrito mudar. Após qualquer nova saída, a revisão visual anterior não vale automaticamente: confira o novo fluxo e registre o novo hash.

Não execute `REGISTRAR.py` novamente sobre este fechamento. Não reaplique os preparadores anteriores sobre a edição integrada atual.
