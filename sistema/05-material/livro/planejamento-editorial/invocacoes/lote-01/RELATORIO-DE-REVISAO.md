# Parecer — Invocações em campo

Candidata de 31 páginas, com ação/PE, ciclo, tarefa, comunicação, básicas, especiais, preparações, Tempo, corpos, talismãs, trunfos, queda, reserva, manutenção, morte e carga. O capítulo publicado permaneceu intacto. Os procedimentos de montagem serão entregues em R12.

**Funcionalidade:** as transições modeladas preservam uma básica por corpo/ciclo, transferência sem cópia, reação coletiva única, prazo de Preparar e primeira oportunidade da antecipada. Ações pessoais não migram para entidades. Básicas Classe0 não gastam limite pessoal de conjuração; comando ocupa o turno de emissão. As exceções aprovadas do Evocador continuam válidas.

**Números:** `python3 auditar.py` reproduz pagamentos divididos, reservas, devoluções, talismãs, sobrevivência, reparos e trunfos a partir de tabelas e âncoras. O relatório discrimina verificações de texto, cenários numéricos e 17 modelos dirigidos. Esses totais não representam sessões de RPG.

**Balanço:** ações e preços de entrada, especial e trunfos foram preservados. A Liberação usa pontos 2/4/6/9/11/13/16+C, evitando reduzir inadvertidamente as faixas altas para 2C. Máxima mantém19/22/26 d8, com orçamentos8/12/16 já estabelecidos no R06. Domínio usa C d8 por decisão explícita de escala reduzida; a tabela de especiais não o produz por simples 2C−C nas faixas altas.

Riscos concretos para teste em mesa:

- Ordens pagas antes podem concentrar duas resoluções e uma conjuração pessoal num turno. O custo dos comandos foi pago antes; duas básicas serão gastas e cada corpo só sustenta uma especial pendente. Esse comportamento histórico foi mantido, testado e confirmado pelo root.
- Reação da Família Tempo custa pessoal+básica+coletiva, sendo menos atraente que a reação autônoma concedida por um poder específico. É fechamento conservador, não prova de equilíbrio.
- Armado permite dispensar coletiva porque compra uma Melhoria e paga tudo antes; sair de campo perde a aplicação e só devolve metade do PE. Estoque na reserva é vedado.
- Área não destrói, mas soma excedente a um corpo desligado; um dano direto posterior pode destruí-lo. É leitura conservada da fonte, explicitada para evitar surpresa.
- Suspender manutenção sem energia é novo procedimento. Não cria dívida, débito parcial ou morte; pode voltar no próximo vencimento. Precisa ser testado com uma passiva concreta.
- Reparo requer Classe de progressão suficiente, ferramentas e materiais. Não usa Grau de item ou Refino e não oferece criação automática de corpo/poder.

**Editorial:** títulos diretos por tarefa, sem Como ler e sem artigos iniciais. As 31 leituras contextuais ficam em REVISAO-EDITORIAL.json. Guia e domínios gerais foram retirados desta reprodução; remissões apontam os donos. Termos difíceis foram definidos quando indispensáveis. Textos são instrução de jogo, com exemplos originais, sem narrativa ornamental.

**Revisão de fechamento:** houve leitura independente, correção dos achados, geração da prova e inspeção visual das 31 páginas. As fórmulas foram conferidas novamente depois de remover marcas de Markdown que apareciam impressas. A conferência automática da prova fica em `CONFERENCIA.json`. Morrendo/morte/Integridade continuam na fila, e os gatilhos serão reavaliados na integração. Nenhum resultado automatizado equivale a validação humana, cânone ou garantia de equilíbrio.


**Conciliação final com R12:** Aura e Reação compradas como especial comandada mantêm acesso às condições pagas; a vedação é das respostas e auras autônomas. Atrasar comum custa Completa do invocador, básica da executora e imobilidade voluntária de ambos. Liberação conserva o Movimento da executora: a incompatibilidade com devoluções de Atrasar/Parado é expressa, sem conceder-lhe automaticamente a Restrição. Carregar paga Padrão+básica+PE no início e ação indicada+básica no turno seguinte; Rápido pode alterar a segunda ação. Foram adicionados casos de custos, prazo, dano, saída e imobilidade.


**Reserva total de corpos (R11-48):** conta corpos ativos e inativos juntos, usando atributo escolhido para Defesa mais a maior capacidade de ativação concedida. Conserva o maior total anterior e resolve o excesso involuntário ao encerrar combate. Mudanças de estado não geram corpos nem ampliam o teto ativo. Queda de capacidade por troca de Trilha exige seleção dos corpos mantidos, na regra de troca. A discussão independente e os cenários ficam em `REVISAO-INDEPENDENTE-RESERVA.json` e na auditoria atual.
