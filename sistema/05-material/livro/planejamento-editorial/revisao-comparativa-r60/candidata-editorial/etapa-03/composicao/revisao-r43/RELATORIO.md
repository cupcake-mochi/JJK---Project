# Ciclo Maldito — R42 para R43

Revisão de 10/10/2026, em cópia nova da R42. O PDF continua com **373 páginas**.

## Regra aplicada

Bloquear é escolhido contra cada ataque **antes da rolagem de acerto do atacante**, sem conhecer seu resultado. A fórmula, a gratuidade, os custos e os resultados especiais não mudaram.

Redirecionar a Força conserva a rolagem original; o novo alvo usa apenas sua Defesa, sem Bloquear. Decisão explícita do autor: “Manter a rolagem original; novo alvo usa só Defesa”. As demais respostas continuam sujeitas às suas janelas próprias.

A sequência de Ataques, Olhos Em Mim, Instante Decisivo e a Consulta rápida foram adequadas ao novo momento. Instante Decisivo conserva seu gasto após o d20 e antes da resolução da defesa. Mudar o Destino não precisou ser alterado: faz uma nova rolagem, permitindo a escolha de Bloquear antes dela.

## Registro de alterações

Foram alterados seis blocos, todos registrados com antes e depois no arquivo `ALTERACOES-R42-para-R43.json`.

Três exemplos foram ajustados:

- Ataques: o inimigo de Sousuke conserva Defesa 17 antes da rolagem; o total 17 acerta, como antes.
- Bloquear: Rina escolhe antes da rolagem da maldição; ataque 18 e Bloquear 17/19 mantêm os mesmos resultados.
- Redirecionar a Força: o resultado original 17 supera a Defesa 15 do novo alvo, que não pode Bloquear.

Não foi inventado um número de item para o documento de decisões. O campo `item` identifica o assunto e a data desta decisão do autor.

## Preservação e diagramação

A comparação integral confirma que o texto é idêntico ao da R42 fora dos seis blocos registrados. Os 2.536 arquivos da R42 foram conferidos por SHA256: a base permanece intacta. A decisão anterior sobre Promessas foi preservada.

Arte, fontes, tamanhos, tabelas e estilos foram preservados. A recomposição automática mudou a posição de elementos nas páginas 21, 22, 23, 24, 88, 154, 165 e 366; está registrada em `RECOMPOSICOES-DO-PDF.json`.

Foram examinadas visualmente as páginas 20, 21, 22, 23, 24, 87, 88, 153, 154, 165 e 366. Não foram observados novos cortes, sobreposições ou problemas de ordem de leitura. A área branca herdada na metade inferior da página 165 não foi redesenhada nesta rodada de regra.

## Arquivos de suporte

O gerador da cópia R43 foi atualizado para aplicar a nova camada e identificar o PDF como R43. As referências dos três exemplos no catálogo de destaques foram atualizadas para casar com o texto, mantendo sua classificação visual. O conferidor geral libera os dados de cada página após verificá-la, reduzindo o uso de memória; não altera o conteúdo do PDF. Esses ajustes estão registrados em `ALTERACOES-DO-GERADOR.json` e `REFERENCIAS-DE-EXEMPLOS.json`.

Nenhuma cópia do repositório de regras em Claude 2 ou Claude 3 foi alterada. Sem commit nem push.

## Conferência final

A conferência geral concluiu **117,446 verificações**, sem apontamentos. Verificou os 500 blocos de texto, 2,432 links internos e 184 marcadores, além de margens, sobreposições, glifos, imagens e presença do conteúdo no PDF. A revisão visual é registrada separadamente.

SHA256 do PDF entregue: `8c936686336d38ad80863def9b575f3a8c8182d83d133fc9fbfc9e63af76b175`.
