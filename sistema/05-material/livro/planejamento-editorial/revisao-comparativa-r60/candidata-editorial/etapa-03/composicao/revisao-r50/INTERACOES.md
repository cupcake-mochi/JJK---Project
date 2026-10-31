# Morrendo — conferência de interações na R50

Base de comparação: R49. Decisões: candidata consolidada v0.17, aprovada pelo autor. A conferência cruzou os trechos do livro com as 25 frentes do mapa de dependências. As alterações efetivas estão em `../ALTERACOES-R49-para-R50.json`; uma frente conferida não implica uma alteração.

| Frente | Resultado no livro |
|---|---|
| M01 — Entrada e janela | Vida a zero aplica Morrendo. A janela esgotada causa derrota antes de um resgate comum. Depois dos gatilhos da queda, escolhe-se Aguentar ou Insistir. Cura ordinária disparada nessa entrada acumula tratamento e é comparada à exigência depois da escolha. |
| M02 — Insistir | Sem custo de Ação Padrão, vida máxima ou rodada imediata. Primeiro uso na cena exige 1/3; seguintes, 1/2; teto direto de 15 × maior Classe. Conta uma escolha por queda. Passar a Aguentar não reduz o requisito nem renova prazo. |
| M03 — Cura e estabilização | Vida continua zero durante o acúmulo. Ao completar o requisito, todo o tratamento vira vida, sem descontar o requisito. Estabilidade suspende o tempo; novo dano quebra a estabilidade e consome uma rodada. |
| M04 — Sequelas, derrota e descanso | Uma Sequela na saída da queda; janelas 3/2/1/derrota imediata. Descanso longo resolve a recuperação, registra a Sequela da saída e só então remove todas. Cura após derrota não devolve participação na mesma cena. |
| M05 — Condições e remoção | Morrendo continua fora das condições compráveis. Limpa Fundo foi explicitamente adaptado: sua remoção genérica não encerra Morrendo. Limpa e tratamento de condições leves não ganham essa permissão. |
| M06 — Levanta | A entrada agora declara que encerra Morrendo abaixo do tratamento necessário. Conserva 5 × Classe, alvo aliado, uma vez por cena e impedimentos. Tratamento anterior soma; saída concede Sequela. |
| M07 — Socorrista | Ainda Há Tempo continua no gatilho de chegar a zero, exigindo Cuidado preparado, Reação e 2 PE adicionais. A entrada explicita a saída de Morrendo e a impossibilidade de superar Derrotado. Cuidado Preparado e Tratar e Retomar conservam seus alvos e condições. |
| M08 — Segundo Fôlego | CE2 e uma vez por descanso longo conservados. Troca a exigência de Insistir por 1/4 naquela queda. Conta como Insistir e não concede cura, turno ou prazo. |
| M09 — Prevenção | Passa Pra Mim, Costura e o pacto do braço mantêm o beneficiário com 1 PV antes de entrar em Morrendo. Não geram Sequela apenas por prevenir a queda. Regras próprias de cada fonte preservadas. |
| M10 — Autocura | Insistir permite usar a ação e a fonte disponíveis. Recomposição passa de 5C para 3C, como aprovado; mantém Padrão e uma vez por descanso curto. Ainda de Pé remete a Socorro: cura ordinária não ganha saída expressa. Energia Reversa conserva ação e PE. |
| M11 — Regeneração Orgânica | Continua exigindo pelo menos 1 PV e no máximo 30% da vida máxima. Como o tratamento não cria PV positivos parciais, não fica disponível durante Morrendo. Foi corrigida apenas uma negação ambígua na redação. |
| M12 — Corpo e reparo | Socorro conserva ofício compatível. Reparo Autônomo pode contribuir durante Insistir se houver consciência, treino, meios e ação; seus 30% não ganham saída expressa. Curas incompatíveis continuam sem efeito. O personagem não recebe o religamento pago de entidades. |
| M13 — Núcleo Dependente | Não foi criada Integridade para quem não a possui. Recuperar PE encerra sua inatividade energética, não Morrendo ou derrota. As restrições da inatividade continuam impedindo ações. |
| M14 — Integridade e Remenda | Integridade zero prevalece sobre a escolha de Insistir. Remenda recupera a reserva, mas não reabre a participação após derrota. Cura de vida não recupera Integridade. |
| M15 — Sem Cura e compatibilidade | Cura impedida ou incompatível não acumula tratamento. Estabilizar não é cura e continua possível; a recuperação posterior não ignora impedimentos. |
| M16 — Vida temporária | Não conta como tratamento nem encerra Morrendo. Absorve dano antes da vida; só dano restante que alcance a vida reduz a janela. A referência de máximo não inclui essa reserva. |
| M17 — Reserva, Junto e área | Reserva continua disparando cura ordinária depois do dano. Não ganha a permissão de Levanta. Junto e Compartilhamento não multiplicam o uso de resgate. O núcleo novo resolve o acúmulo quando o gatilho ocorre na queda. |
| M18 — Consciência e manutenção | Aguentar deixa Inconsciente; Insistir não. Outra causa de inconsciência não é removida. Concentração, ordens e ações seguem seus próprios requisitos; o tratamento não reinicia efeitos encerrados. |
| M19 — Domínios | O gatilho de encerramento a zero de vida permanece, mesmo que o dono escolha Insistir. Cura posterior não reabre automaticamente o domínio. |
| M20 — Entidades e inimigos | Nenhuma importação de Morrendo para entidades. Recolhimento, Desligada, destruição e retorno conservam seus procedimentos. Inimigos continuam com o desfecho próprio a zero, salvo regra da ficha. |
| M21 — Progressão | Subir de nível não é descanso, não remove Sequelas ou condições e mantém a zero quem precisa de socorro. A vida máxima de referência fica registrada na queda. O feito de levantar alguém continua exigindo um resgate efetivo pelo procedimento aplicável. |
| M22 — Medicina e Ofícios | Estabilizar informa alvo, alcance, Padrão, mão livre, meios, CD14, sucesso, falha e nova tentativa. Medicina não vira uma cura gratuita. Reparo de objetos não se aplica a personagens sem permissão. |
| M23 — Dano e transferência | Um golpe de tipos mistos conta uma ocorrência. Ataques distintos contam separadamente. Dano periódico e de queda seguem a mesma apuração após defesas. Zero dano e absorção total por vida temporária não agravam a janela. |
| M24 — Gatilhos por derrubar | Cobrança e Eco conservam seus gatilhos de reduzir a vida a zero. Tratamento parcial mantém a vida em zero; não cria novas quedas ou novos disparos desses efeitos. |
| M25 — Consulta e exemplos | Glossário e remissões usam a condição e o tratamento atuais. Refeitos os exemplos do dano posterior, da Mei com 23 PV e do Insistir com 93 PV; acrescentado o exemplo do teto com 395 PV. Índice e sumário foram regenerados. |

## Cenas conferidas por leitura do procedimento

- **Três Sequelas e Ainda Há Tempo:** a queda causa derrota imediata. A emergência não tem permissão pós-derrota; não contorna o limite. Uma capacidade futura que o autor escreva expressamente para depois da derrota será uma exceção específica.
- **Cura imediata ordinária de 24 com máximo 93/C3:** Aguentar exige 24 e encerra a queda; Insistir exige 31 e mantém 24 de tratamento, zero PV e a janela. Segundo Fôlego pode reduzir essa exigência para 24 quando anunciado na escolha.
- **Tratar e depois sofrer dano:** com requisito 31, tratamento 18 e janela 2, um golpe de 7 que atinja a vida deixa tratamento 18, requisito 31 e janela 1. Não exige 38 de cura nem reduz o tratamento a 11.
- **Tipos mistos e ataques múltiplos:** Cortante e Fogo de um mesmo golpe consomem uma rodada; dois ataques resolvidos separadamente podem consumir duas. A redução não depende do valor absoluto do dano positivo.
- **Estabilizar:** para o teste em alguém que Insiste, ele primeiro passa a Aguentar; a exigência da queda permanece. Dano quebra a estabilidade sem zerar o que já foi tratado. Uma nova estabilização não devolve rodadas.
- **Recuperação segura:** ao terminar o descanso curto estável, o 1 PV excepcional soma ao tratamento válido anterior, encerra Morrendo e concede uma Sequela. Sem Cura continua impedindo essa recuperação enquanto durar.
- **Descanso longo depois da terceira queda:** recupera as reservas conforme o ambiente, encerra a queda/derrota por vida, registra a Sequela correspondente e só então limpa todas. A personagem não começa a missão seguinte com a Sequela gerada por essa própria recuperação.
- **Derrota só por Integridade:** não produz Sequela de vida. Núcleo Dependente não precisa recuperar uma reserva que não possui. Nenhum dos casos ganha participação na mesma cena só porque uma reserva foi curada.

## Evidência e limites

Os 16 testes determinísticos da v0.14 foram executados novamente na integração. Eles conferem frações, teto, quedas sucessivas, persistência, contadores e recursos. As simulações extensas já realizadas estão preservadas no estudo; não foram repetidas como se fossem uma evidência nova. A conferência de regras acima é leitura cruzada, não execução de todas as capacidades num motor completo.

Nenhuma nova decisão de balanceamento foi tomada nesta integração. Aguentar e Segundo Fôlego continuam em 1/4 sem teto. Em máximos excepcionalmente altos, esse quarto pode superar o teto de Insistir; esse efeito do desenho aprovado já consta no estudo e não foi corrigido silenciosamente. Não houve teste com jogadores nesta rodada.
