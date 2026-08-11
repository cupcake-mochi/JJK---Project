# Casos-sonda: medir divergência entre mestres

Um caso-sonda é uma situação curta, propositalmente na fronteira da regra, mandada para cada mestre **separadamente**. O objetivo não é achar a resposta certa — é descobrir se os mestres chegam à mesma.

Custa quase nada (não precisa de sessão) e pega o modo de falha característico de sistema com vários mestres, que nenhum formulário de jogador enxerga: o jogador não sabe que a outra mesa resolveu diferente.

## Como escrever um bom caso-sonda

**Uma frase de situação, uma pergunta fechada.** Se precisar de parágrafo para montar o cenário, você está testando leitura, não arbitragem.

**Fique na fronteira, não no meio.** Um caso que a regra resolve claramente não mede nada. Um caso que a regra não cobre de jeito nenhum também não — só mede improviso. O ponto útil é onde a regra *parece* cobrir.

**Peça a decisão e a âncora.** "O que você decide, e em que trecho do material você se apoiou?" A âncora é metade do valor: dois mestres que decidem igual citando trechos diferentes revelam que a regra está espalhada demais.

**Não avise que é teste de consistência.** Mestre que sabe que está sendo comparado consulta mais do que consultaria numa mesa real.

**Três a cinco por leva.** Mais que isso vira dever de casa e a taxa de resposta despenca.

## Modelo de envio

> Cinco situações rápidas. Responde do jeito que você resolveria na sua mesa, no impulso — não precisa pesquisar. Depois de cada uma, escreve em que você se apoiou (pode ser "achei que fazia sentido").
>
> **1.** [situação em uma frase] — o que acontece?
> **2.** ...

## Exemplos de bom caso-sonda

Genéricos, para adaptar ao seu sistema:

- Um jogador quer usar uma habilidade de um jeito que a descrição não previu mas também não proíbe. Vale?
- Dois efeitos que duram "até o fim do próximo turno" foram aplicados em turnos diferentes. Quando cada um cai?
- Um personagem quer aceitar uma desvantagem que ele já teria de graça naquela cena. Ela devolve recurso?
- O alvo passa no teste que reduz o efeito pela metade, e o efeito não é numérico. O que "metade" significa?
- Um jogador propõe uma habilidade customizada que parece caber. Qual é o preço, e quem decide?

Repare no padrão: todos são casos em que **duas leituras razoáveis do material levam a decisões diferentes**. É isso que você está procurando.

## Ler o resultado

| O que aconteceu | O que significa | O conserto |
|---|---|---|
| Todos decidiram igual, mesma âncora | A regra está clara | nada |
| Todos decidiram igual, âncoras diferentes | Regra espalhada; funciona por acaso ou por cultura da comunidade | juntar num lugar só |
| Decisões diferentes | Regra ambígua | reescrever, não só esclarecer no Discord |
| Alguém não achou onde se apoiar | Lacuna, ou problema de navegação | conferir se a regra existe antes de escrever de novo |
| Todos decidiram igual e todos erraram | A regra existe e diz outra coisa | falha de redação: o texto não está sendo lido como escrito |

A última linha é a mais desconfortável e a mais útil. Quando todos os mestres convergem numa leitura que não é a que está escrita, a leitura deles costuma ser a intuitiva — e vale considerar mudar a regra em vez do costume.

## Frequência

Uma leva por versão, antes de fechar. E sempre depois de mexer numa regra que já tinha divergido antes — a correção precisa ser verificada, não presumida.
