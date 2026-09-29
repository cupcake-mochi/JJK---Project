# Integração do Sukuna — remontagem e débito corrente concluídos

28/09/2026. Item 1 da ordem mais recente de Mizuki. O item 3, planejamento das Invocações para Claude, vem depois do fechamento deste. A decisão sobre débito corrente foi aprovada por Mizuki: "Pode seguir recomendação. Agora vamos prós planejamentos".

## Entregas e alcance

`SUKUNA-GRADE-ATUAL.md` reúne a ficha derivada; `SAIDA-sukuna-grade.json` abre as contas; `montar-sukuna-grade.js` reproduz ambos. Rode `node bestiario/05-sukuna/montar-sukuna-grade.js --check` para conferir. O conferir-bestiario também executa essa conferência. A ficha histórica e seu script continuam preservados; o script antigo não é o gerador vigente.

A remontagem usa Calamidade ×6 e nível 30, como a fila determinava. Conserva atributos, papel, tamanho e capacidades escolhidas. Não é nova aprovação de design nem prova de equilíbrio. A montagem e o procedimento de débito estão fechados neste recorte; a dificuldade real do encontro ainda requer playtest.

## Números derivados

| Item | Resultado | Origem |
|---|---|---|
| PV-base | 2362,5 antes de arredondar | 5 rodadas × 6 pessoas × 315/4 |
| PV finais | 1111 | PV-base × 1,2 ÷ 1,1 ÷ 1,92 ÷ (67/60) ÷ (189/179) ÷ 1,025; arredondamento final do gerador |
| Integridade | 555 | metade dos PV finais, para baixo |
| Cura por ação | 78 | PV-base, decisão de Mizuki já fechada |
| Braço | 157 PV | dobro da saída individual, antes dos ajustes |
| Circulação | 25 (10d4) | teto próprio, não PV-base |
| Desmembrar | 68 (6d10 + 35) | golpe da célula |
| Clivar | 54 (12d8) | 68/4,5 − Pesada 8 + Toque 5; dados inteiros |
| Teia | 40 (9d8), média real 40,5 | 68/4,5 − Leve 3 − Leve 3; dados inteiros |
| Chama | 170 (18d12 + 53) | 2,5 golpes; d12 perto de dois terços |
| Primeira Intervenção | 51 (4d12 + 25) | 0,75 do golpe, não golpe inteiro |

**Classe 5 é consequência do orçamento, não promoção arbitrária.** O manual atual dá 15 pontos à Classe 5; 68/4,5 dá 15,111… e a peça 26 manda usar a maior Classe que cabe. O texto antigo da peça sobre 14,9 pontos caberem na Classe 4 continua verdadeiro, mas não descreve o novo Sukuna.

As fórmulas exatas da Recarga e da Circulação foram usadas antes do arredondamento de PV; os 1,12 e 1,06 publicados nas tabelas são apresentações arredondadas. O domínio usa o divisor explícito 1,92 da regra, não uma substituição silenciosa por 1/0,52.

**Atributos:** criação [2,2,1,2,3], na ordem Força/Destreza/Constituição/Inteligência/Essência; sete aumentos gratuitos e a escolha de atributo no 10; quatro pontos do Rei das Maldições. Energia Reversa no 18, Circulação na escolha com refino no 22, Regravação no 26 e Extensão no 30. Isso conserva os 22 pontos finais e atende ao gate atual da Extensão; não tenta comprar duas aptidões na escolha do 18. É uma demonstração de construção possível, não alteração da ficha de nível 30.

Extensão foi alinhada à peça 11: imunidade aos efeitos de Expansão, teto de contato 4, três quartos do dano acima dele, sem acerto automático próprio, sem feitiço/Manejo. Sua entrada específica de Intervenção foi conservada, sem conceder múltiplas Intervenções por rodada.

## Decisão de débito corrente — histórico do caso e fechamento

A peça 26 manda cobrar aptidões da cota **daquela rodada**, proíbe gastar acima dela e manda pagar ativação a cada uso. Não descreve a distribuição do débito quando o inimigo já agiu, perde ações por partes destruídas ou ativa uma defesa depois do turno. As antigas fichas só imprimiam o golpe reduzido de uma rodada inteira; isso não resolve os casos parciais.

Exemplo: seis golpes de 68 formam 408. Regravar custa 51,4. Antes de qualquer golpe, repartir o custo produz seis golpes de 59 pelo arredondamento do gerador. Mas se três golpes de 68 já saíram, não há como alterá-los: repartir a cobrança nas três ações restantes produz três golpes de 51. Usar a tabela de seis golpes nessa situação cobraria apenas parte do custo. Se todos já saíram, não existe cota restante para debitar.

**Decisão aprovada por Mizuki em 28/09/2026:** manter o débito na rodada corrente e cobrá-lo das ações ainda disponíveis, sem desfazer ações resolvidas nem criar dívida para a próxima rodada. Sem cota suficiente, a aptidão não pode ser ativada naquela janela. Para uma defesa fora do turno, isso exige ter deixado cota disponível; essa consequência foi apresentada ao autor e aceita, restringindo a reação tardia. O valor de cada ação pendente é recalculado com os preços de técnica que couberem no orçamento restante.

**Alternativa rejeitada:** permitir cobrar da próxima rodada quando a atual não comportar. Isso preserva a defesa depois de agir, mas altera a decisão vigente de pagar naquela rodada e cria dívida, inclusive na morte ou perda de ações antes do próximo turno. Não é recomendada sem redesenhar e testar esse débito.

O ensaio aplica a decisão aprovada a: ações parcialmente usadas; braços destruídos; Extensão acionada por Reação/Intervenção; repetição de ativação; e Regravação seguida de Chama. Esses são casos de teste da mesma política de cobrança, não cinco pedidos independentes de redesign. A amortização da ativação por cinco rodadas é a fórmula existente de montagem; a cobrança só pode alcançar ações ainda legalmente disponíveis, nunca ações já resolvidas. A cobrança não fornece janela nem conserva ações expiradas.

Não resolvemos essa lacuna transferindo custo para PV ou ignorando a Regravação. Tampouco removemos uma capacidade autoral só para fechar a ficha.

## Limites da validação

Os testes conferem reprodução, referência de PV, orçamento de técnica e consistência entre os arquivos derivados. Não simulam uma luta completa nem provam o empilhamento de domínio, Recarga, cura e partes contra todas as composições. O multiplicador de Circulação considera a sua própria fórmula de referência; a duração conjunta precisa de simulação de encontro e playtest; não é uma garantia produzida pelo ensaio contábil. Os casos de perturbação ficam em `validacao-grade/`.

O critério de fechamento deste recorte foi atendido: política aprovada, exemplos impressos e ensaio reproduzível. Item Sukuna concluído como integração técnica, sem certificação de equilíbrio; a próxima entrega é o planejamento das Invocações. Nenhum Caminho, Trilha, regra de Evocador ou Procedimento de Campo foi modificado.

**Resultado executado:** conferir-bestiario passou sem pular checagens. Cinco alterações incorretas foram detectadas em cópia isolada (PV final usado na cura; divisor de domínio invertido; Classe congelada em 4; braço antigo; Intervenção inteira). Base, restauração e alteração coerente da saída do personagem com regeneração passaram. Isso verifica a integração aritmética; o débito corrente foi integrado em complemento posterior, com doze casos executáveis na saída do gerador.

A conferência de repositório terminou com apenas a falha já conhecida 7.4: o último commit de finalizado é v0.276, enquanto o trabalho atual declara v0.286. As contagens foram alinhadas às onze checagens do Bestiário. Não foi feito commit para contornar esse resultado; não foi repetida a bateria completa de todos os validadores.

## Fechamento do débito

Os doze casos cobrem começo da rodada, três ações já usadas, cota esgotada, janela externa fornecida, saldo insuficiente, perda de braços antes/depois do débito, duas aptidões, reativação, Regravação seguida de Recarga e ausência de dívida futura. O modelo confere estado e custo, não cria legalidade de janela. A cota é orçamento da ação: errar, curar ou usar uma técnica com menos dano não devolve a parcela para pagar aptidão. Valores exatos são preservados até o arredondamento de cada golpe pela regra existente.

A ativação de Extensão mantém a amortização da peça 26 (maior Classe × câmbio ÷ rodadas). Nova ativação recebe outro débito dessa parcela; a manutenção não é isenta. Isso não cria reserva de PE, restituição ou cobrança de uso passado em rodada futura. Não mudamos o relógio geral das ações nem concedemos ações fora do turno.
