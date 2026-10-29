# Revisão textual integral e visual — registro 96

28 de outubro de 2026. Pedido de Mizuki: revisar todas as páginas para clareza e naturalidade; revisar novamente como pente-fino; só então conferir a apresentação visual. Este registro sucede os registros 93–95. A pasta de apoio conserva o nome provisório `apoio-revisao-integral-94`; não substitui o registro 94 sobre a capa.

## Resultado

O [PDF revisado](<../08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf>) tem **357 páginas**. A edição HTML e as fontes editáveis foram atualizadas. O texto público chama a referência de **Livro de Regras 1.0**; R53 permanece apenas como identificação técnica nos arquivos de pesquisa e no histórico. A referência mecânica foi preservada, sem migração de versão ou rebalanceamento.

## Duas passagens textuais

A primeira leitura cobriu as **104 fontes integradas**, incluindo os três exemplos antes mantidos na pasta de planejamento. Foram simplificados títulos, frases abstratas, orientações burocráticas e referências ao processo de produção. A segunda leitura percorreu **as 357 páginas da prova resultante**, do início aos créditos, com correções adicionais e registro por página. Os trechos alterados foram relidos no contexto.

O [registro de alterações](apoio-revisao-integral-94/alteracoes.json) contém **2.000 substituições documentadas, em 2.160 ocorrências**; esse número inclui nomes, títulos e substituições repetidas, não representa 2.000 erros mecânicos. A [segunda leitura](apoio-revisao-integral-94/segunda-leitura/manifesto.json) preserva os textos da prova, seus hashes e as notas. A cópia anterior está em `apoio-revisao-integral-94/antes/`.

Exemplos de direção editorial:

- A entrada passa a explicar o trabalho do mestre com ações concretas: preparar uma missão, apresentar o mundo e acompanhar escolhas.
- “O Guia explica sua aplicação e identifica as seções relevantes” dá lugar a “Este Guia mostra como usá-las em situações de jogo e onde consultá-las”.
- Os títulos apresentam o assunto ou a ação do leitor: “A sociedade jujutsu”, “Por onde começar”, “Regras, dicas e exemplos”, “Entre missões”.
- Notas como número de estudo, versão de protótipo e referências sem destino dentro do livro foram retiradas do texto de leitura ou substituídas por referências internas úteis. O histórico permanece no acervo.
- Termos que nomeiam regras, como Integridade, Restrição, Teste de Resistência e Classe de Dificuldade, permanecem identificáveis. Simplificar a explicação não muda o nome da regra.
- As contas de ataque passaram a mostrar corretamente `d20 +3 (Força 2 + Maestria 1)`, sem sugerir que o dado mais os bônus seja sempre igual ao bônus.

Títulos de subseções receberam hierarquia consistente no PDF. As âncoras antigas foram preservadas para manter remissões após a troca dos títulos.

## Revisão visual depois do texto

Todas as **357 páginas** foram renderizadas com Poppler e examinadas em pranchas de quatro páginas, com ampliações adicionais. A conferência considerou colunas, sequência de leitura, títulos, tabelas, mapas, imagens, legendas, margens e espaços vazios.

Foram corrigidos o item isolado no início da página 314 e a introdução do apêndice D: seus dois parágrafos agora usam a largura da página antes da imagem, evitando a leitura fragmentada em duas colunas curtas. A capa final respeita a escolha registrada por Mizuki no registro 95: sem título adicional à direita, sem selo de pré-1.0, preservando a marca original da imagem. A condição de pré-1.0 continua na abertura e nos rodapés internos.

Os encerramentos com mais espaço foram revistos, incluindo páginas 16–17, 169–170, 187–188, 234–235, 293–294, 300–301, 332–333 e 349–350. Foram testadas recomposições das últimas duas, três e quatro páginas, sem reduzir fontes ou espaçamento. Não houve redução de páginas com esse padrão. Os espaços remanescentes preservam tabelas, introduções e encerramentos; não foram preenchidos com texto artificial nem imagens sem função.

Após os ajustes finais, **353 páginas ficaram idênticas pixel a pixel** à prova visual integral. As páginas **1, 313, 314 e 351** mudaram, foram renderizadas novamente e examinadas ampliadas; a página 2 também recebeu nova ampliação. O conteúdo textual interno antes e depois desta última mudança de layout conserva exatamente as mesmas ocorrências de palavras. Evidências: [comparação das provas](apoio-revisao-integral-94/comparacao-final.json), [inspeção integral](apoio-revisao-integral-94/visual-prova-2/inspecao.json) e [inspeção final](apoio-revisao-integral-94/visual-final/inspecao.json).

Conservado o padrão do livro-base: A4, Spectral 10,25/13,2 pt, margens de 19 mm, intervalo de 7 mm entre colunas, títulos Barlow Condensed/Bree Serif. Os cinco mapas e as imagens já selecionadas continuam no documento.

## Conferências e limites

- **2.383 links no PDF**, sem destinos inválidos; verificador sem sobreposições, conteúdo fora da margem ou títulos separados do primeiro bloco.
- **1.030 links locais em 16 páginas HTML**, sem arquivo ou âncora ausente.
- **104 fontes** com hashes correspondentes ao mapa editorial.
- Nenhuma ocorrência de “R53”, “procedimentos” ou “Cotidianos diferentes na mesma ocorrência” no texto extraído do PDF.
- As 14 alterações registradas com diferenças na sequência de números foram examinadas: remoção de datas/identificadores de produção ou reorganização das mesmas contas. Não houve mudança de valor mecânico.
- A referência R53 mantém SHA-256 `7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d`.

A revisão editorial e visual está concluída. Ela não representa teste com leitores, sessão de mesa ou certificação de equilíbrio. Uma questão técnica foi anotada para avaliação separada: o exemplo de História da família Arata usa CD 16 (p. 181), enquanto a escala comum apresentada no Guia usa passos 6/10/14/18/22/26. O valor preexistente foi preservado; confirmar se é dificuldade específica do exemplo ou se deve ser alinhado à escala, sem tratar uma revisão de escrita como autorização para mudar a regra.

SHA-256 do PDF final: `0050d7cf2426ce3eba555ab2010deaeb6d62e023a5dba67ec43f0495e79cbd3b`.

## Continuidade

Próxima tarefa recomendada: recolher dúvidas de leitura usando esta pré-1.0 e fazer correções dirigidas, preservando este ponto de comparação. Leitores podem indicar página, passagem, o que entenderam e o que ficou incerto. É possível conferir a questão técnica acima em paralelo; não reabrir decisões já assentadas sobre dedicação, Pactos ou Reserva Condensada.

Para comparar sugestões e aplicar correções dirigidas, recomendo **GPT-6.1 Sol, esforço alto**. Para contradições mecânicas que exijam comparação ampla, **GPT-6 Astra, esforço extra alto**. É uma recomendação para este projeto, sem teste comparativo entre modelos; a [orientação oficial de seleção](https://developers.openai.com/api/docs/guides/model-selection), consultada nesta revisão, recomenda comparar resultados usando os mesmos critérios de qualidade. Nenhuma configuração foi alterada.

Esta entrega foi salva localmente. Não foi feito novo commit ou envio ao GitHub nesta tarefa.
