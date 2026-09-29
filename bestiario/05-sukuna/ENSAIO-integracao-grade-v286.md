# Sukuna — ensaio de integração à grade atual

> Continuação: `SUKUNA-GRADE-ATUAL.md` contém a conta integrada; `RELATORIO-integracao-grade.md` registra a pendência operacional antes de fechar a ficha. Este ensaio preliminar permanece como histórico.

28/09/2026. Continuação do item 18 após o fechamento da resistência pontual. Este documento é diagnóstico e ensaio; não substitui a ficha histórica nem aprova regra nova.

## Base preservada

O arquivo O-SUKUNA-no-nivel-30.md registra nível 30, papel Artilheiro, tamanho Médio, Destreza 4, os demais atributos escolhidos, Quatro Braços, Rei das Maldições, Energia Reversa, Circulação, Regravação, Santuário e Chama Divina. O item 18 da fila determina Calamidade ×6 na grade nova. A antiga medida de 18,4 pessoas não é reaproveitada como N.

O script montar-o-sukuna.py ainda depende da fase 1: lê suas tabelas, multiplica a quantidade de pessoas pelo Santuário e pela Recarga e lê a Extensão anterior. Não basta trocar seu nível ou substituir constantes. A remontagem deve usar a célula atual e conservar o arquivo e as saídas antigos como histórico.

## Contas que já têm dono

Calculadas pelo conta.js do gerador de inimigos, com os dados conferidos pela peça 26 e pela tabela do manual:

| grandeza | resultado | limite |
|---|---|---|
| célula | Calamidade ×6, nível 30 | decisão da fila |
| duração de referência | 5 rodadas | antes de medir a execução concreta |
| ações por turno | 6 | não aumenta por conhecer mais capacidades |
| PV-base calculados | 2362,5 | antes de ajustes e arredondamento; a célula impressa mostra 2362 |
| golpe-base | 68, em 6d10 + 35 | antes dos custos de técnica ou aptidão |
| Artilheiro, multiplicador de PV | 1 / 1,1 | papel atual, não o antigo fator fixo |
| PV com somente Artilheiro | 2148 | ainda não é a vida final do Sukuna |
| Intervenção, divisor de PV | 1,025 | porta aberta na célula; não desconta golpe |
| referência da tabela | Defesa 20, acerto +10, CD 18, refino 10 | Destreza 4 produz Defesa 18 e exige o ajuste próprio |

Não foram empilhados todos os recursos nem escolhida uma ordem de arredondamento intermediário. A vida final, a cura e os braços ainda não estão publicados como ficha pronta.

## Referência de PV-base — decisão fechada

A peça 26 usa, para cura de ação, “a vida dele ÷ as rodadas ÷ N” e, para parte destrutível, “a vida dele ÷ as rodadas × 2 ÷ N”. As duas são apresentadas como equivalentes à saída de um personagem e ao dobro dela; a tabela das partes publica 157 PV no nível 30. Essa equivalência só permanece direta antes dos ajustes de vida. O script histórico do Sukuna usava a vida depois do papel para o braço, de modo que não é seguro trocar silenciosamente o significado de “vida”.

Exemplo isolado, sem Santuário, Recarga, Circulação ou desvio de Defesa:

| referência | cura por ação | PV por parte |
|---|---|---|
| PV-base da célula | 78 | 157 |
| PV depois de apenas Artilheiro | 71 | 143 |

Recomendação apresentada ao Mizuki: fixar PV-base como referência, preservando a tabela corrente e escrevendo a distinção. Alternativa: usar PV final, com recalculação após todos os ajustes e correção da equivalência publicada. **Decisão posterior de Mizuki: "Pode fechar PV-Base".** Usar PV-base antes dos ajustes, mantendo frações até o resultado final. A cura por ação fica em 78 e cada braço em 157 PV; os 71 e 143 permanecem apenas como comparação da alternativa rejeitada. A vida final do Sukuna ainda será calculada.

## Próxima etapa

Resolver as contas derivadas sem alterar o conjunto de capacidades escolhido. Atualizar a Extensão pelo texto vigente da peça 11 (inclusive anulação do Acerto, limite da técnica e dano acima dele), sem conservar a antiga promessa de ataque automaticamente acertar. Verificar os custos de aptidão nas rodadas ligadas, os limites de Intervenção, a Recarga e a vida final. Conferir o bloco com um ensaio reproduzível antes de substituí-lo para leitura. Não reabrir Caminhos nem Procedimentos de Campo.
