# Plano de testes e aceite da integração

**Plano a executar; não é relatório de testes realizados.** Os valores esperados precisam ser transcritos das regras aprovadas antes de rodar cada caso. Cálculos isolados do histórico não encerram a Etapa 6.

| Caso | Frente | Cobertura mínima | Fonte do gabarito |
|---|---|---|---|
| T01 | Estrutura e treinos | A047; listas próprias; uma marcante + duas menores elegíveis; sem duplicar treinos ou somar modalidades. | Base e montagens |
| T02 | Restrição sem energia | Ataque sem Prenúncio, custo, Estudar inicial, memória, mudança de perfil e Katas no alcance aprovado. | A028–A031 e montagem |
| T03 | Latente | Limiares 9/10/13/14, pior custo antes de declarar, custo final mínimo 1, descontos/acréscimos e intervalo entre turnos. | A037/A038 e Tentativa e Erro |
| T04 | Híbrido | PV 0, limiar 30% com arredondamento, acima/abaixo do limiar, cura acima dele, frequência e máximo de PE. | Regeneração v04 |
| T05 | Ficha Híbrido | Aviso visual ativa/desativa na faixa correta e não confunde elegibilidade com uso já gasto. | Requisito de integração da ficha |
| T06 | Corpo e reparo | Classe igual/inferior/superior, CD não cresce pela especialização, falha consome tentativa, repetição diária e 30% autônomo. | A052/A055/A062 |
| T07 | Corpo M1/M2 | Energia zero/inatividade/recuperação; sem Integridade, dano de Alma em vida e dano só em Integridade; condições e vulnerabilidades escolhidas. | Estado M1/M2 v06 |
| T08 | Receptáculo | Coexistência paga 6 PE; Conflito dano versus outros efeitos, resposta de medo e janela de imunidade; menores por modalidade. | Montagem e A070 |
| T09 | Encarnado | Reserva de Experiência após rolagem/antes consequência, usos compartilhados por descanso longo, perícias elegíveis e especialização no nível previsto. | A071–A076 |
| T10 | Descendente | Kukuru/Akashi, dados Kamo, feitiços/Manejos Gojo, duplas Inumaki, exclusivas, dinheiro próprio, cofre por grau. | Marcantes e catálogo A087 |
| T11 | CE4 | Uma escolha; técnica compatível; Rede Remota não multiplica ataques/sentidos; exemplos selecionados não recebem parâmetros não aprovados. | A088–A091 e pendências |
| T12 | Saída Elevada | Classes 1–7: 1/1/1/2/2/3/3 pontos; só Melhorias; tetos e custo-base preservados; sem Manejos/Máximas. | A092 |
| T13 | Penalidades | Defesa 0, sem Bloquear, condições corporais, luz, repouso e cura de cada pacote; efeitos no corpo versus intermediário. | A093–A096 |
| T14 | Oito menores corporais | Reserva com mestre; 2×Essência; 40% com cuidados; adicional ceil(base/2), um ataque/TR; PE temporários 2×Classe; busca 36 m; dois C0 de Formas válidas. | A097–A100 |
| T15 | Descansos e limites | Cena, rodada, dia, descanso curto e longo distinguíveis; não renovar longo por noite; mínimos e tetos sem geração indevida de recurso. | Regras gerais e concessões |
| T16 | Combinações e progressão | Duplas realmente elegíveis e exceções de repetição; fichas comparáveis em marcos relevantes; não pressupor mesma quantidade de combinações em todas as origens. | Montagens aprovadas e tabela de progressão |

## Registro dos resultados

Para cada caso: versão/hash das fontes, premissas, ficha e recursos, sequência de decisões, resultado esperado com referência, resultado obtido, divergência, correção e repetição. Separar cálculo determinístico, simulação, leitura de prova e sessão real. Um cenário narrado por agente não é playtest humano. Distribuições e recursos por cena/missão exigem premissas explícitas, não uma média inventada.

## Revisão da escrita

Revisão mecânica compara resolução com decisões; revisão editorial verifica leitura/consulta, termos, exemplos e contexto. Segunda leitura recebe a regra aprovada e o texto proposto. Registrar achados por localização, severidade, mudança sugerida, resolução e evidência de conferência. Se não houver revisor independente, registrar a ausência; não atribuir independência a uma autorrevisão.

## Conferência da integração

- Confirmar a base mais recente, registrar sua identidade e trabalhar numa cópia nova.
- Criar rastreio de cada entrada aprovada para arquivo/seção do livro e superfícies da ficha.
- Conferir que nenhuma regra sumiu, nenhuma candidata entrou por engano e nenhum legado antigo permaneceu como benefício cumulativo involuntário.
- Rodar validadores aplicáveis após inspecionar seu escopo, preservando scripts e sem efeitos de publicação; registrar falhas e checagens indisponíveis.
- Conferir números e palavras operacionais em diferenças antes/depois; não aceitar só igualdade de totais.
- Gerar as exportações que a base efetivamente oferece e revisar cada variante entregue.
- Inspecionar visualmente abertura, todas as páginas alteradas de Origens, tabelas longas e dependências com paginação afetada; conferir sumário, marcadores, links e ordem de leitura.
- Entregar fontes, PDF, DOCX quando aplicável, relatório, mapa de migração, alterações da ficha, pendências e hashes.

Critério de pronto: nenhuma diferença mecânica sem aprovação; pendências bloqueantes resolvidas ou claramente delimitadas fora da entrega publicável; resultados reproduzíveis registrados; prova visual e remissões conferidas. Não remover uma capacidade aprovada para fazer o critério passar: registrar o impedimento e preparar a decisão necessária.
