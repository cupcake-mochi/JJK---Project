# R32 — revisão de regras e compreensão

08/10/2026. Prova completa com 394 páginas. Base textual: R31 (498 páginas). A redução decorre dos tratamentos gráficos aprovados; nenhum capítulo ou regra foi cortado para reduzir páginas.

## O que foi aplicado

- Item 160 em Cobrir-se de Energia e Defesa sem Armadura: a Reação perde somente a proteção passiva. Traje, Revestimento e escudo conservam a proteção; custo, redução de dano e prazo permanecem.
- Item 171 em Corrente Extensível: alcance na cena, na ordem de 100 metros (um quarteirão), somente nos ataques feitos no próprio turno. Ponta presa, obstáculos, cobertura, linha de efeito e alcance fora do turno preservados.
- Item 115: retirada a limitação a um único Legado personalizado. A decisão já constava no documento, mas ainda não estava aplicada no texto da R31. A revisão anterior não havia detectado essa divergência.
- Itens 156, 157 e 158 conferidos sem reaplicação: os blocos correspondentes estão idênticos à R31. Penalidades, proteção normal e não multiplicação estão mantidas.

## Compreensão

Leitura integral dos 500 blocos em 63 partes (163.252 palavras no índice de leitura). Foram alterados 15 blocos de redação e 4 blocos de regras decididas, com 26 substituições pontuais. A revisão esclarece a escala de CD do criador, a conferência do teto de dano, a relação entre queda acidental e deliberada, sujeitos de ações e referências ambíguas. Não houve nova decisão de equilíbrio ou aplicação da seção C.

A explicação do teto separa saldo de pontos, dados iniciais e dano adicional; o teto continua em 4 × Classe, com as mesmas exceções. Em Remate, a remissão identifica o aumento de 25%. As imagens de conversa foram usadas como relatos de dificuldade de leitura, não como substituição das regras atuais.

## Exemplos tocados

- CD fixa e CD do criador: a explicação de Rina foi reescrita para separar as duas escalas e mostrar 8 + 4 + 2 e o ajuste +2. Todos os valores e resultados anteriores foram mantidos.
- Cobrir-se, Refino 6: ficou explícito que o personagem está sem Traje, Revestimento e escudo. A conta continua 17 − 9 = 8.
- Kaori: “Sobram 3 dados” passou a identificar o resultado como 3d8 de dano. A montagem e a conta não mudaram.

Nenhum exemplo precisou de recalcular números nesta rodada. O exemplo de Salto e as contas de transporte permaneceram iguais.

## Como comparar

`revisao-de-regras/ALTERACOES-REGRAS.json` é o registro integral R31 → R32: uma entrada por bloco alterado, com antes e depois completos. Os itens 115, 160 e 171 têm seus números; as entradas de redação usam `ENTENDIMENTO-2026-10-08`, que identifica a autorização editorial e não inventa um número do documento. `ALTERACOES-COMPREENSAO.json` repete apenas o subconjunto de redação.

O histórico cumulativo anterior R29 → R30 foi preservado em `revisao-de-regras/HISTORICO-ALTERACOES-R29-R30.json`. Os registros históricos da estrutura R31 permanecem na pasta própria. Para esta rodada, use `conferir_r32.py` e `conferir_livro.py`; os validadores anteriores continuam vinculados às bases antigas.

As fontes editoriais congeladas e as 73 revisões da R29 permanecem intactas, com T072 ausente. A camada `revisao_r32.py` aplica as 26 substituições antes da transformação estrutural da R31. PDF e LIVRO-COMPLETO.md leem o mesmo texto final; editar apenas o Markdown gerado não altera a fonte da próxima geração.

## Composição e verificações

Foram aplicados ao livro completo os tratamentos aprovados: famílias/entradas B+C, corpo 10,25 pt com entrelinha 13,2 pt, tabelas e exemplos B, títulos de seção C. A R32 tem 104 páginas a menos que a R31 (20,9%). A quantidade ainda pode mudar com a etapa de continuidade.

O registro reconstrói o Markdown da R32 a partir da R31 sem nenhuma diferença restante. A validação automática do PDF passou com 500 blocos, 2.370 links internos e 89 marcadores; não detectou perda de texto, sobreposição, glifo ausente ou conteúdo fora da página. R31, fontes, imagens, capa e créditos foram preservados.

Foram abertas e inspecionadas 28 páginas completas: todas as 27 que contêm blocos textuais alterados, mais a página 262. Nesta última, Controle já acompanha sua primeira Melhoria. Há pendências de composição em outras páginas, registradas em `revisao-visual/PENDENCIAS-CONTINUIDADE.json`.

## Fila

6A está concluída e 6B aplicada nesta prova. A próxima etapa é 6C: continuidade, colunas e vazios, incluindo título + introdução + primeira entrada subordinada. Depois vem 6D: inspeção visual de cada página ampliada, validação final e entrega da edição final. Esta prova não representa a conclusão da inspeção visual integral.

Sem commit ou push. Nenhum arquivo do repositório do sistema na unidade externa foi alterado.
