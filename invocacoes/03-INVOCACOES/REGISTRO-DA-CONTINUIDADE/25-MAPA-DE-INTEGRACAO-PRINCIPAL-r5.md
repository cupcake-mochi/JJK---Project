# Mapa de integração com o principal — depois da r5

Leitura de trechos atuais do projeto principal, sem edição ou execução dos validadores antigos. Base corrente da proposta: v0.3 CANDIDATA r5, até §45. Esta análise não cria §46.

## Divergências confirmadas

| Fonte no principal | Situação encontrada | Tratamento na integração futura |
|---|---|---|
| Livro, `60-invocacoes.md`, linhas 7–14 | Padrão a cada rodada e inatividade sem comando; atuação logo depois do dono. | Substituir pelos procedimentos aprovados de intenção persistente, atuação no turno conjunto e comando especial. Sem nova aprovação do mesmo desenho. |
| Livro, linhas 362–365 | Fora da amarra, criatura fica parada, sem agir. | Distinguir comunicação de autonomia; perda do canal não apaga tarefa válida. Alcance do vínculo continua pendente: não importar os números antigos. |
| Livro, linhas 406–417 | Inconsciência do dono proíbe a invocação de agir sozinha. | Aplicar autonomia e ordens recebidas, respeitada sustentação. Não inventar novos comandos durante inconsciência. |
| Mecânica 15, linhas 98–102 e 637–645 | Justificativa de equilíbrio depende da exclusão mútua entre ação do dono e da criatura. | Essa justificativa não valida a arquitetura atual. Não importar conclusões numéricas de equilíbrio para o desenho novo. |
| Validador `conferir-invocacoes.py`, trechos 1488–1501 e 2389–2481 | Confere a economia antiga e exige texto que recusa atuação autônoma. | Futuramente precisa mudar junto dos documentos donos, com autorização de integração ao principal. Não executar para apresentar aprovação da r5 nem alterar só para obter resultado verde. |
| Livro, linhas 380–404 | Queda mistura desaparecer a zero PV, destruição definitiva e retorno com vida parcial mediante custo. | O §22 aprovou equivalência campo/reserva, mas não importou esse pacote. Separar consequência imediata, destruição e recuperação antes de migrar este trecho. |

Os números e custos históricos permanecem referências, não escolhas desta análise. A r5 continua sem regra nova de Evocador, Trilha, catálogo, construtor ou orçamento.

## Próximo recorte autoral proposto, ainda não aprovado

**Caso:** uma invocação em campo, com uma especial preparada, chega a zero PV antes do gatilho. O §22 exige a mesma consequência quando recolhida, mas não escolhe a consequência de queda em campo.

**Recomendação nova:** a zero PV, a invocação deixa de atuar e sai do campo. Como há saída, suas ordens especiais pendentes e preparações se encerram, sem devolução de gastos. Isso não declara destruição definitiva nem autoriza retorno com vida restaurada. Queda não é, por si só, substituição: nenhuma transferência de básica é concedida automaticamente por este recorte.

**Alternativa:** permanece como corpo caído em campo; seria necessário definir aptidão, ocupação, dano adicional e interação com o corpo. Não importar automaticamente Insistir/Aguentar dos personagens.

Morte definitiva, condições de recuperação e retorno continuam questões separadas. Recomendar saída a zero PV não importa o limiar antigo de destruição, prazo ou custo. A escolha acima ainda depende de Mizuki.

## Evidência e limites

Arquivos lidos no principal: livro 60, mecânica 15 e trechos do validador. Hashes em `25-FONTES-PRINCIPAL-r5.json`. Isto é comparação documental direcionada, não auditoria completa do repositório nem teste novo. Os 212 testes continuam pertencendo à r5. Nenhum arquivo principal, manual ou Caminho foi editado; sem commit/push.
