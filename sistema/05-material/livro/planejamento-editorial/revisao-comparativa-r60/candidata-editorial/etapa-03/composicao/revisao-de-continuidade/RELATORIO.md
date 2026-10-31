# R33 — continuidade e colunas

A R33 tem **389 páginas**, contra 394 da R32. O ganho veio da recomposição: nenhum texto foi cortado ou reescrito, e as fontes aprovadas mantêm seus tamanhos.

## O que mudou

- Cada página admite um único par de colunas. A leitura segue a esquerda inteira, depois a direita. Títulos e tabelas de largura inteira podem vir acima ou abaixo desse par, seguindo a ordem do conteúdo.
- Aberturas curtas de famílias e seções acompanham o começo útil da primeira entrada. Foram verificadas 203 dessas ligações. Em 73 apresentações extensas, o trecho final acompanha a primeira subseção; o restante continua entre parágrafos, com indicação de contexto.
- Tabelas compactas podem ocupar uma coluna quando suas palavras e números cabem com a fonte aprovada. Tabelas largas continuam em largura inteira.
- A escolha das quebras considera o restante da sequência para reduzir sobras muito pequenas. Colunas muito desiguais recebem uma distribuição mais equilibrada quando a sequência permite.

## Casos conferidos

| Trecho | Páginas da R33 | Resultado |
|---|---:|---|
| Feto e Sem Técnica | 78–79 | Colunas reequilibradas; Sem Técnica começa com sua apresentação e o primeiro legado. |
| Batedor: Besta e Arma de Fogo | 104–106 | Continuação identificada; Arma de Fogo começa junto do acesso e de sua primeira regra. |
| Famílias de melhorias | 257–267 | Família e primeira melhoria permanecem juntas; preço fica abaixo do nome da melhoria. |
| Cobrir-se de Energia | 281 | Apresentação, tabela, reação e exemplo seguem em sequência na mesma coluna. |
| Extensão de Domínio | 288–289 | Apresentação e duração aparecem juntas; a continuação segue na página seguinte. |
| Defesa sem Armadura | 306–307 | Tabela e reação seguem a leitura de toda a esquerda antes da direita. |
| Invocações em campo e construção | 333–373 | Continuações entre parágrafos e tabelas recompostas, preservando a ordem das regras. |

## Conferência e registros

O LIVRO-COMPLETO.md é idêntico, byte a byte, ao da R32. Os 5.846 elementos editoriais aparecem na mesma ordem, com as mesmas 1.514 âncoras. A base R32 foi conferida contra seu registro de arquivos e permanece intacta. Regras e exemplos não foram refeitos nesta etapa.

O registro `ALTERACOES-DIAGRAMACAO.json` contém 495 grupos alterados, com a posição de cada elemento antes e depois, inclusive rótulos de continuação gerados. `ALTERACOES-TEXTO.json` está vazio. Os registros de alterações de regras e redação herdados continuam valendo.

A validação final realizou 100.476 verificações e conferiu 2.354 links internos, sem problemas detectados. Foi eliminada a ocorrência de múltiplos pares de colunas na mesma página, antes presente em oito páginas da R32.

As 389 páginas foram vistas em folhas de contato; 61 também foram examinadas ampliadas, incluindo todos os 16 últimos reequilíbrios. A relação exata e o PDF conferido estão em `REVISAO-VISUAL.json`. Essa amostra não equivale à inspeção ampliada integral da etapa 6D.

Ainda há espaços em branco, sobretudo em transições para tabelas largas e encerramentos de capítulo. Foram preservados para manter fontes legíveis e sequência de leitura. As páginas 97, 279, 291 e 363 ficam destacadas para avaliação na 6D. A medida de ocupação em `OCUPACAO-COMPARADA.json` é apenas um indicador de triagem, não uma medida de legibilidade.

Próxima etapa: **6D — revisão visual integral**, com **GPT-6 Astra, esforço alto**. Sem commit ou push.
