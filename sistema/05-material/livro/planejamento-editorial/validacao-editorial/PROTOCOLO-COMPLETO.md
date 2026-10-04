# Protocolo de revisão por unidade e do livro completo

Pedido reforçado pelo usuário em 03/10/2026: executar todos os validadores em cada item da fila e novamente no documento consolidado. Uma checagem sobre a versão antiga não valida o texto novo.

## Bateria obrigatória

| ID | Validador | Evidência exigida |
|---|---|---|
| V01 | Cobertura | Inventário de conteúdo da fonte e destino de todas as regras, exemplos e tabelas necessários. |
| V02 | Regras e fontes | Conferência com a versão vigente; divergências e precedência documentadas. |
| V03 | Funcionamento | Casos positivos, negativos e de limite, distinguindo execução de especificação. |
| V04 | Números | Contas reproduzíveis de custos, escalas, arredondamento, probabilidade e recursos aplicáveis. |
| V05 | Balanceamento | Comparação de alternativas e interfaces; riscos, hipóteses e limites do ensaio. |
| V06 | Compatibilidade | Relação com capítulos donos, exceções e cópias; nenhuma mudança silenciosa. |
| V07 | Títulos e vocabulário | Validador automático e leitura contextual. Títulos diretos; palavras familiares ou termos definidos. |
| V08 | Clareza e suficiência | Quem age, quando, custo, alvo, resolução, duração, saída e exemplo quando necessário. |
| V09 | Voz e redundância | Leitura contextual com livros de RPG como referência, especialmente D&D; reduzir frases vazias, contrastes retóricos e repetição. |
| V10 | Localização | Uma regra tem um dono; outras seções remetem ao dono e conservam apenas a exceção local. |
| V11 | Obra e referências | Afirmações sobre JJK verificadas em fonte adequada. Propostas originais identificadas; acesso insuficiente não vira confirmação. |
| V12 | Revisão independente | Segundo leitor por agente com escopo e hash; achados tratados ou encaminhados com motivo. |
| V13 | PDF e navegação | Texto completo, medidas, fontes incorporadas, remissões, marcadores e preservação de fontes. |
| V14 | Visual | Inspeção de todas as páginas renderizadas; mudança posterior requer reinspeção ou igualdade de pixels comprovada. |
| V15 | Rastreabilidade | Antes/depois/motivo, fontes, scripts, hash do texto/PDF e manifesto do lote. |

Cada unidade mantém `VALIDADORES.json`, vinculado ao manuscrito. Um critério sem aplicação recebe justificativa, não aprovação inventada. Dependências de outra unidade continuam em um registro de interfaces e são reavaliadas antes da consolidação.

## Limites

Leitura por agentes não equivale a leitura por jogadores. Modelos numéricos não equivalem a partidas nem medem diversão. Quando não houver participação humana, registrar explicitamente essa ausência e propor casos de mesa sem contá-los como executados.

Os validadores históricos verificam seus próprios donos. Não usá-los como evidência de que uma candidata diferente está correta apenas porque continuam passando na publicação antiga. Adaptar a conferência ao texto atual e conservar os casos de regressão pertinentes.

## Revisão final

No livro único, repetir a bateria completa. Acrescentar busca de nomes antigos/novos, remissões órfãs, definições contraditórias, números de progressão, aquisição pelas rotas, economia de ações, morte/Integridade, navegação e cobertura integral de páginas. Repetir os casos funcionais após alterações que mudem suas premissas.

As falhas devem ser corrigidas antes da entrega, ou explicitamente caracterizadas como limite que exige informação/mesa externa. O registro deve permitir reconstruir por que a decisão foi tomada.

## Referências indispensáveis entre capítulos

E002 pode aceitar uma referência exata registrada em `LOCALIZACAO-EDITORIAL.json`, com termo, trecho, papel (`requisito`, `incompatibilidade` ou `remissao`) e justificativa. O registro precisa declarar que não reproduz a regra e corresponder ao hash atual do manuscrito. Essa exceção permite indicar o dono ou o requisito necessário. Não libera cópia de habilidade, títulos proibidos ou outros erros: E003 e E007 continuam bloqueando a exportação.
