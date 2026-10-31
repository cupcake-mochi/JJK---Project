# R48 — revisão visual e continuidade

Entregue em cópia da R47. A R47 permanece intacta. Nenhum commit ou push.

## Resultado

- **402 páginas**, contra 388 da R47 (+14).
- **Leitura a Dois inteira na página 80**: título, regra, exemplo e último parágrafo na mesma coluna. Na R47 o encerramento ficava separado nas páginas 75–76.
- Texto consolidado byte a byte idêntico à R47: 511 blocos preservados. Nenhuma regra, frase, tabela ou exemplo reescrito.
- Fontes, tamanhos, espaçamento tipográfico, arte e hierarquia aprovada preservados. Sumário, índice, referências de página e navegação foram regenerados para a nova paginação.
- O aumento de páginas decorre das restrições de continuidade. Esta rodada prioriza a leitura; não é uma rodada de redução de páginas.

## Correções de composição

1. O compositor passou a penalizar quebras que deixavam finais curtos de uma regra na página seguinte, sobretudo quando o próximo parágrafo cabia no espaço restante.
2. Aberturas de grupos e catálogos acompanham a primeira entrada e o início de sua regra, quando o conjunto cabe em uma coluna. Exemplos: Controle (p. 276), Talentos de Categoria 1 (p. 287) e Especiais com preparação prolongada (p. 356).
3. Nomes de equipamentos e seus metadados acompanham o primeiro parágrafo do efeito. Exemplos: Kunai Fiel e Corrente Extensível (p. 229).
4. Tabelas curtas ficam inteiras quando possível. O título e sua introdução acompanham pelo menos as primeiras linhas das tabelas maiores. Dificuldade (p. 14), Arma de Fogo (p. 216) e Combinações de Ritual (p. 341) deixaram de ter a introdução separada da tabela por uma página.
5. Conclusões breves depois de tabelas largas acompanham suas últimas linhas. Aptidão Própria termina na própria página de apresentação e exemplos (p. 304).
6. O exemplo final de vida e energia temporárias acompanha a regra demonstrada (p. 52). Sangue Frio fica inteiro na coluna direita da p. 322. No Arquiteto, o exemplo acompanha o parágrafo anterior, mesmo quando o conjunto precisa continuar na página seguinte (p. 131).
7. A distribuição antes de elementos de largura inteira considera o espaço necessário para evitar adiamentos desnecessários. A leitura continua pela coluna esquerda inteira e depois pela direita, dentro de cada faixa de colunas.

## Conferência realizada

Todas as composições das 402 páginas foram cobertas pela inspeção visual: 303 permaneceram idênticas às já inspecionadas no ensaio anterior, e 99 foram reinspecionadas depois dos ajustes finais. Os pontos críticos foram ampliados. Os painéis, imagens individuais e a relação entre composições estão em `revisao-r48/`.

Não identifiquei cortes de texto, sobreposições ou colisões com os rodapés na inspeção. A conferência automática terminou com **117635 verificações e zero problemas**, abrangendo conteúdo, extração real, geometria, 2555 links internos e 192 marcadores.

As tabelas longas continuam podendo atravessar páginas, com cabeçalho repetido. Entradas extensas também continuam entre colunas ou páginas. Essas continuações não são, por si, defeitos. Permanecem áreas brancas em aberturas e finais de capítulo e onde uma abertura útil precisa passar inteira; por exemplo, o final da tabela de progressão na p. 240 ainda deixa espaço livre. Não foi feita compactação de fonte ou alteração textual para eliminar esse espaço.

Os relatórios `QUEBRAS-BASE.json` e `QUEBRAS-FINAL.json` são triagens heurísticas, não contagens de erros confirmados. Incluem continuações legítimas e falsos positivos; não devem ser usados para afirmar que toda quebra apontada é inadequada.

## Registro e preservação

- `ALTERACOES-R47-para-R48.json`: lista vazia porque não houve alteração textual.
- `revisao-r48/ALTERACOES-GERADOR.json`: antes e depois completos dos dois arquivos do gerador alterados.
- `revisao-r48/POSICIONAMENTO-ANTES-DEPOIS.json`: posicionamento dos blocos na R47 e na R48, incluindo referências regeneradas.
- `revisao-r48/VALIDACAO.json`: comparação do texto, preservação dos 794 arquivos da R47 e integridade do PDF.
- `revisao-r48/REVISAO-VISUAL.json`: cobertura e método da revisão visual.
- SHA-256 do PDF: `13f710aa2193d4d3e83898d377d7cc323150d506acf678ce2e7882f132557a41`.

O rascunho anterior de polimento dos Legados, remissões e visão noturna permanece separado em `../rascunho-polimento-legados-sobre-r46-2026-10-13/`. Não foi incorporado nesta rodada de diagramação.
