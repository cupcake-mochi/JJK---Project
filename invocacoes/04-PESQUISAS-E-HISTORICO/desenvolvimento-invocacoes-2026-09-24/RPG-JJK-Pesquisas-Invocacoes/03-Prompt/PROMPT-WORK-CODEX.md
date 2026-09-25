Vamos continuar o desenvolvimento do sistema RPG -JJK / Projeto M. Sou Mizuki. O foco desta etapa é reconstruir as regras de INVOCAÇÕES. O Caminho EVOCADOR e suas Trilhas serão desenvolvidos depois, sobre esse sistema.

Atue como parceiro de criação e revisão técnica: leia, compare, questione e teste. Não implemente uma ideia só porque ela aparece numa pesquisa. Não tente terminar o subsistema, o Caminho e as três Trilhas de uma vez.

# 1. Localize o projeto e leia antes de propor regras

Use o repositório aberto ou a pasta local selecionada neste ambiente. Confirme o caminho real. Se houver Git, informe branch, commit e alterações já presentes, sem modificá-las.

Localize a pasta extraída `RPG-JJK-Pesquisas-Invocacoes` e, quando disponível, a coleção `RPG-JJK-Caminhos-Trilhas-e-Ideias`. Não presuma que arquivos de outro chat estejam acessíveis aqui.

Leia as instruções do projeto, incluindo README, AGENTS e arquivos de orientação que existirem e se aplicarem à pasta trabalhada. Se as referências próprias `mizuki-copiloto-do-mestre` e `mizuki-rpg-gamedev` estiverem no ambiente autorizado, leia-as também.

Ordem de leitura:
1. `README.md` deste pacote de pesquisas.
2. `02-Base-de-Trabalho/01-Consolidacao-decisoes-e-pendencias.md`.
3. Os DOIS relatórios completos em `01-Pesquisas/`, incluindo suas referências.
4. `02-Base-de-Trabalho/02-Plano-de-reconstrucao.md`.
5. As regras do repositório e os quatro Caminhos consolidados.

No snapshot estudado, os principais arquivos do repositório eram:
- `sistema/03-mecanica/15-invocacoes.md`;
- `sistema/05-material/livro/manual/60-invocacoes.md`;
- `sistema/05-material/livro/manual/35-caminhos-e-trilhas.md`;
- `sistema/05-material/livro/manual/40-fundamento.md`;
- `sistema/05-material/livro/manual/11-o-turno.md`;
- `sistema/05-material/livro/manual/15-dano-e-condicoes.md`;
- `sistema/03-mecanica/19-dano-e-condicoes.md`;
- `sistema/03-mecanica/conferir-invocacoes.py`;
- `sistema/03-mecanica/conferir-orcamento.py`.

Confirme os caminhos e siga referências para atributos, maestria, progressão, energia amaldiçoada, concentração, criaturas e orçamento. Leia os scripts antes de executá-los. Um teste antigo passar não valida o novo sistema.

Se um arquivo mudou de lugar, procure-o no projeto. Se realmente faltar, diga qual é e avance no que puder ser fundamentado, sem inventar seu conteúdo.

# 2. O que vale como regra e como decisão

O repositório enviado às pesquisas ainda não continha a reconstrução recente de Bastião, Vanguarda, Emanador e Guia. A coleção `RPG-JJK-Caminhos-Trilhas-e-Ideias` contém essa consolidação v0.4.

Para esses quatro Caminhos, use a coleção como referência das decisões desta conversa. Para as regras gerais e o diagnóstico das invocações antigas, consulte o repositório. Se o ambiente trouxer uma versão posterior, apresente as diferenças antes de escolher qual usar.

Não altere Bastião, Vanguarda, Emanador ou Guia nesta etapa. Em especial, a sugestão de acrescentar energia ao nível 2 do Emanador NÃO foi adotada. Estocada permanece como está.

As pesquisas são material de investigação, não regras aprovadas. Quantidades de corpos, valores de Presença, custos de PE, percentuais de dano/vida, progressão automática e listas de origens apresentados nelas são hipóteses. Não os transforme em decisão minha.

A redação final de manual e o balanceamento integrado dos quatro Caminhos ainda possuem pendências registradas. Não considere seus preços em fatias certificados.

# 3. Decisões já tomadas

- Vamos reconstruir primeiro o subsistema geral de Invocações; depois o Evocador; por último suas Trilhas.
- Invocações serão completamente customizáveis. Exemplos prontos podem testar o sistema, mas não substituem o construtor.
- Acesso a uma invocação e especialização em invocações são coisas diferentes. A arquitetura deve comportar uma fonte de acesso fora do Evocador, sem entregar gratuitamente o Caminho inteiro.
- O Evocador antigo e as invocações antigas não precisam ser preservados. Aproveite uma ideia somente se ela funcionar na arquitetura nova.
- As três futuras Trilhas devem sustentar estas relações:
  * Singular: uma entidade forte protege e luta por você, como uma extensão importante do personagem.
  * Parceria: você luta junto de uma ou duas invocações.
  * Múltiplas: um pequeno conjunto de entidades diferentes é sua principal forma de lutar e agir; não uma horda de dezenas de fichas nem cópias iguais com uma vida compartilhada.
- Os números finais de entidades simultâneas ainda não foram escolhidos.
- A narrativa deve permitir intenções e ordens que continuam valendo, sem obrigar o jogador a repetir “ataque” a cada rodada só para a criatura parecer viva. A forma de limitar as ações ainda precisa ser comparada.

# 4. Problemas que precisamos resolver

Os problemas apontados inicialmente foram acesso praticamente preso ao Evocador, ausência de um limite geral convincente de criaturas em campo, pouca identidade do Caminho e construção superficial das invocações.

Verifique esses diagnósticos no conteúdo atual, inclusive a diferença entre “a regra diz que pode existir outra fonte” e “há uma fonte realmente escrita”. Investigue também:
- quantos corpos, ações, movimentos, Reações e usos de Bloquear entram em jogo;
- habilidades passivas, auras, cobertura, ocupação de espaços, sentidos e utilidade fora do combate;
- custo para manifestar, retirar, trocar e trazer de volta;
- autonomia, obediência, alcance das ordens e comportamento fora dele;
- formas de aquisição, customização, crescimento e perda;
- interação com feitiços, condições, energia temporária e ações concedidas por aliados.

Dividir o dano entre criaturas não resolve sozinho o valor dos corpos adicionais. Por outro lado, controlar invocações não deve consumir toda a diversão do personagem em ordens repetitivas.

# 5. O papel de Jujutsu Kaisen

O sistema precisa acomodar entidades ligadas a uma técnica, conjuntos conquistados, criaturas capturadas, seres criados, suportes físicos e vínculos particulares. Origem, forma de obtenção e vínculo não são necessariamente a mesma classificação.

Teste a arquitetura contra situações inspiradas em:
- um shikigami simples de alguém que não escolheu Evocador;
- uma entidade singular ligada ao personagem;
- um conjunto fixo de invocações conquistadas gradualmente;
- um repertório expansível de maldições capturadas;
- uma criatura criada ou um corpo amaldiçoado;
- um ser utilitário, uma manifestação de Domínio e um efeito com aparência de criatura.

Não copie personagens canônicos como fichas prontas. Distinga fato mostrado na obra, interpretação da pesquisa e proposta nossa.

A pesquisa canônica ainda precisa de confirmação nos detalhes que sustentarem uma regra. Não trate uma página geral de personagens como prova de toda mecânica específica. Verifique especialmente Rika antes/depois de JJK 0, as regras particulares de Dez Sombras, aquisição de shikigami sem técnica específica, crescimento de maldições capturadas e corpos amaldiçoados.

Quando precisar complementar, prefira mangá/material oficial e documentação dos sistemas. Comunidade serve para experiência de jogo, não para provar regras ou frequência estatística. Se uma fonte estiver inacessível, registre a limitação.

# 6. Primeira tarefa: presença, ações e autonomia

Comece por uma definição curta do que merece uma ficha de invocação. Depois compare duas ou três arquiteturas de funcionamento em campo.

Separe as perguntas:
- Repertório: quais entidades o personagem possui ou pode chamar?
- Preparação: é necessário escolher antes quais estarão disponíveis, ou isso seria uma camada dispensável?
- Capacidade em campo: que limite representa o poder sustentado?
- Quantidade de corpos: é necessário um teto separado para manter a mesa rápida?
- Ações: como personagem e invocações dividem as ações disponíveis?
- Autonomia: o que cada entidade pode continuar fazendo sem uma nova ordem?
- Manifestação: como entrar, sair, trocar e perder uma criatura afeta o combate?

Presença é um nome e um modelo candidatos, não uma moeda obrigatória. Compare-o com alternativas mais simples. Não crie vários contadores para responder à mesma pergunta.

Para cada arquitetura, descreva um turno comum, uma rodada com resposta inimiga e a perda de uma invocação. Compare personagem não-Evocador com uma entidade, singular, parceria e múltiplas com duas, três e quatro entidades como cenários experimentais — não como limites aprovados.

A autonomia ficcional não dá, por si só, ações ofensivas ilimitadas. A limitação de ações também não exige que os corpos fiquem narrativamente inertes. Resolva essa diferença de forma explícita.

# 7. O que vem depois da arquitetura em campo

Proponha uma sequência de trabalho para:
1. Construir a ficha e seus módulos: corpo, sentidos, deslocamento, papel, características, ações e capacidade especial.
2. Criar fontes de acesso e vínculos: aprender, receber, criar, conquistar, capturar ou depender de uma técnica/objeto.
3. Separar crescimento da entidade, domínio do vínculo e evolução do usuário. Não adote crescimento automático para toda criatura capturada sem explicar o que acontece com sua força anterior.
4. Definir derrota, dissipação, corpo destruído, retorno, reparo e perda permanente. Não universalize a herança de Dez Sombras.
5. Medir recursos, riscos, ações e efeitos, incluindo presença física e utilidade.
6. Só então desenvolver Evocador e suas três Trilhas.

Essas etapas podem exigir ajustes entre si. Não feche uma regra de morte ou custo de aquisição que dependa de um valor de criatura ainda desconhecido.

# 8. Entrega esperada agora

Produza:
- mapa dos arquivos lidos e das diferenças entre as fontes;
- diagnóstico confirmado, com caminho e seção ou linhas;
- comparação de duas ou três arquiteturas;
- recomendação justificada, sem fingir aprovação;
- menor protótipo de teste da arquitetura recomendada, separado das regras vigentes;
- plano de próximos passos e poucas decisões realmente dependentes de mim.

Se usar números para permitir um teste, identifique-os como provisórios e explique o que estão testando. Não feche o orçamento em fatias nem escreva o catálogo completo.

Os testes devem contar ações, rolagens, Reações, reposicionamento, alvos, gasto de energia e consequência de perder/trocar uma criatura. Compare também o valor de vida adicional, bloqueio de passagem, proteção e condições. Não conclua “equilibrado” apenas porque o dano médio ficou igual.

Registre somente verificações realmente executadas, com comando de reprodução, resultados e limitações. Tempo real de mesa e diversão exigem observação de pessoas; não invente essas medições.

# 9. Arquivos e escrita

Pode criar documentos novos de diagnóstico, plano, protótipo e testes numa pasta de desenvolvimento coerente com o projeto. Marque tudo como RASCUNHO/PROPOSTA e informe os caminhos criados.

Não substitua o manual atual, não reescreva os quatro Caminhos preservados, não apague arquivos e não faça commit ou push sem minha decisão. Preserve alterações locais existentes. Escolher uma recomendação para comparar não significa aprová-la.

Escreva em português do Brasil, com linguagem de manual de RPG: benefício primeiro, depois custo, momento de uso e condições necessárias. Prefira “alvo que possa atingir” a “alvo legal”. Explique os termos do sistema e separe o texto do jogador das notas de design e matemática.

Não recomece toda a pesquisa de mercado. Use os dois relatórios, complete somente as lacunas que afetarem decisões e comece pela leitura e pelo funcionamento em campo. Ao terminar essa primeira entrega, pare para minha avaliação antes de desenvolver o Evocador.
