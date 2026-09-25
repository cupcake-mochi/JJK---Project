# Ficha do ensaio r5

## Escopo

Executar `python3 bancada_r5.py` nesta pasta. Usa somente a biblioteca padrão do Python. A saída é gravada em `execucao.json` e `resultados.json` nesta pasta; não modifica os scripts anteriores nem o projeto principal.

As 178 verificações herdadas executam contra as classes ampliadas da r5. Os arquivos `base_r1.py`, `bancada_r2.py` e `bancada_r4.py` foram copiados sem alteração. São somadas 34 verificações novas, R5-01 a R5-34. Os resultados registram estado anterior/posterior, expectativa e resultado obtido.

## Premissas

- Uma oportunidade básica por corpo é fixture de ensaio, não progressão aprovada.
- Trajeto da porta tem dois segmentos abstratos: antes → porta → cobertura. Não são metros, alcance ou velocidade final.
- O efeito que impede movimento é fornecido como fato de uma capacidade escrita. Não nasce automaticamente do dano. A cena fornece uma passagem legal e comunicação válida quando há recusa.
- Opções conhecidas, aptidão, coerência com intenção, custos disponíveis e usos limitados são fatos de entrada. Não se calculam perícias, PE, dano ou teste de Provocar.
- A opção limitada é uma capacidade hipotética, não uma nova regra de Ler o Ambiente. A bancada não implementa a restituição da ação quando não existe informação útil nem decide detalhes não definidos dessa exceção.
- Abertura válida e dispensa expressa são fatos da cena. O modelo testa consumo/janelas e consequências sobre a coletiva, não concessão, alcance, expiração pelo relógio do Guia ou todas as Trilhas.
- Trocas herdadas são eventos legais fornecidos externamente: não são gratuitas por estarem no roteiro.

## Cobertura nova

| Casos | O que verificam |
|---|---|
| R5-01–08 | Resposta na porta antes da cobertura; continuidade do saldo; impedimento escrito; falha; recusa e inviabilidade sem armazenamento. |
| R5-09–22 | Pagamento por básica; nenhuma ação extra; proibições; requisitos; capacidades ausentes; usos preservados; janela e compromisso da antecipada. |
| R5-23–34 | Avançar dentro/fora do turno; consumo da Abertura; Movimento não renovado; coletiva e perda de preparações; Guia; dispensa expressa e impedimentos. |

Os dez casos de intenção copiados são análise textual histórica, não novas verificações executáveis. Os dez cruzamentos do complemento foram conferência textual, não uma soma ao total executável.

## Limites

Não há simulador espacial geral, motor completo de habilidades, prioridade universal de gatilhos, teste humano ou medição de equilíbrio. Recusas não recebidas continuam cobertas pelo método herdado, mas a cena da porta exercita somente recusa legal recebida. Não atribuir ao trajeto de exemplo cobertura de todo conflito simultâneo.
