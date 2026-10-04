# Divisão do trabalho entre modelos

Não há um teste estatístico comparável deste Projeto - M que permita afirmar que uma marca escreve melhor ou encontra mais erros. Preço e desempenho neste projeto são medidas diferentes.

A documentação primária da Anthropic publica Fable 5.1 a US$10 por milhão de tokens de entrada e US$50 de saída; Opus 5.5 a US$4 e US$20. Com o mesmo volume sem cache, Fable custa 2,5 vezes Opus na API. Isso não converte diretamente em consumo de créditos ou limites da assinatura Pro. Fonte: [documentação de modelos da Anthropic](https://platform.claude.com/docs/en/models/overview), consultada em 02/10/2026.

## Divisão recomendada

| Trabalho | Uso sugerido | Motivo |
|---|---|---|
| Integração, correções aprovadas, coerência entre arquivos e verificações | Sol 6.1 com raciocínio alto | trabalho rastreável com resultados conferíveis |
| Fichas já em andamento | Claude Opus 5.5 | conserva o contexto e a continuidade daquele trabalho |
| Revisão editorial global após receber livros de referência | comparar Astra e Opus 5.5 em um piloto; usar o escolhido por capítulos e depois leitura transversal | a avaliação do material decide quem assume a primeira redação |
| Novas Trilhas e alternativas de identidade | Opus 5.5 e Astra em propostas independentes | comparar interesse de jogo e fechamento das regras antes de escolher uma versão |
| Segunda leitura de nomes e ambiguidades | Opus 5.5, recebendo fontes e critérios iguais | outro revisor pode detectar vícios da primeira leitura; não requer ser o modelo mais caro |
| Auditoria transversal difícil, com conflitos que sobreviveram à primeira revisão | Fable 5.1 em uma amostra antes de ampliar | a documentação o reserva para demandas difíceis; medir se o ganho paga o custo |

Evite dois ambientes escrevendo o mesmo capítulo ao mesmo tempo. Um prepara a versão proposta; o outro entrega observações ou um texto separado. A integração deve ter uma versão atual e uma lista explícita de decisões.

A divisão acima é uma sugestão inicial. Se a amostra favorecer outro modelo, ele deve assumir a redação principal; manter o contexto atual em um ambiente não é motivo para rejeitar um resultado melhor do outro.

## Como medir antes de gastar no livro inteiro

Compare os modelos com as mesmas 5 seções, fontes e instruções. Inclua criação de personagem, uma classe simples, uma classe com recursos, construção de feitiços e um procedimento de invocações. Avalie os resultados sem o nome do modelo à vista.

Conte ambiguidades reais encontradas, alterações de regra não autorizadas, regras ou custos esquecidos, trechos aceitos sem retrabalho e tempo/consumo efetivo. Para ambiguidades, registre precisão (achados válidos / achados totais) e cobertura (ambiguidades conhecidas encontradas / total conhecido); para reescrita, porcentagem de trechos aprovados. A amostra pequena serve para escolher o fluxo do projeto, não para provar superioridade geral. Não invente porcentagens sem realizar a comparação.
