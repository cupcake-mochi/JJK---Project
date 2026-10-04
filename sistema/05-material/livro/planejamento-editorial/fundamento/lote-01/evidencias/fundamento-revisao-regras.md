# Revisão de regras — Fundamento candidato, segunda passagem

Data: 2026-10-03T16:25:40-03:00
Fonte: `/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial/fundamento/lote-01/FUNDAMENTO.md`
SHA-256: `30306aa5740e0fcd9906fc96a937b0823909bacfb98ed9b3c97fc3dd37739b60`
Linhas: 800


Auditoria somente de leitura. O arquivo estava sendo editado durante a revisão: as localizações abaixo são do snapshot indicado e precisam acompanhar o texto, não o número absoluto. Foram lidas as seções completas de conjuração, repetições, Classe 0, Liberação, Máxima e Passagem de Papel e comparadas suas interfaces com os candidatos de Regras Básicas e Regras Comuns. Não houve teste com jogadores. As contas não certificam equilíbrio final.

## Parecer

A candidata está muito mais operacional que a fonte publicada: distingue montagem e uso, mostra saldo e custo, cobra a resistência nas situações hostis e define término de efeitos. O núcleo normal/Liberação pode avançar após os ajustes localizados abaixo. Técnica Máxima depende do quadro de compatibilidade anunciado pelo autor; sem ele, o orçamento fixo de dano pode ser multiplicado por peças herdadas que não foram escritas para esse orçamento. Passagem de Papel é uma aplicação original verificável, sem alegação de ser capacidade canônica de Jujutsu Kaisen.

## Ajustes prioritários ainda abertos neste snapshot

### P1 — O orçamento fixo da Máxima ainda precisa limitar peças que multiplicam dano

**Local:** FUNDAMENTO.md:696–723. **Natureza:** decisão mecânica nova, já identificada pelo autor, não simples revisão de frase.

O texto separa 24/28/32d8 de 8/12/16 pontos, mas a chamada genérica às Melhorias ainda permite ler Salto, Queima, Estilhaço, Fica, Remate, Acúmulo e Inescapável como disponíveis. A Máxima básica já supera 4 × Classe nas três faixas; o teto dos feitiços comuns não resolve isso. Uma Máxima com 24d8 e Queima acrescentaria 12d8 sem perder dano-base; Fica repetiria esses dados por várias rodadas. Inescapável eliminaria as duas resistências sem reduzir o pacote, diferente da sua economia normal.

**Correção mínima sugerida:** quadro exclusivo da Máxima dizendo quais peças são vedadas, quais dividem o pacote fixo e quais operam normalmente. Se a decisão for pacote fixo sem repetições, registrar explicitamente que Salto, Queima, Estilhaço, Fica, Remate, Acúmulo e Inescapável não são opções desta montagem; Rajada/Mais Um/Junto repartem os dados, nunca copiam. Certeiro pode conservar seu efeito só se deliberadamente aceito: ele não acrescenta dados, mas aumenta dano esperado em ataque. Não usar a expressão genérica “sem dano adicional” como única trava, porque Fica repete dano e Inescapável muda resolução sem adicionar dados escritos.

### P1/P2 — Área + respingo/pulo ainda permite multiplicação sobreposta

**Local:** FUNDAMENTO.md:482–486; catálogo publicado `manual/40-fundamento.md:627,733`.

O teto de 4 × Classe é conferido uma vez sem multiplicar pelos alvos. Isso preserva áreas funcionais, mas não define quantos gatilhos Estilhaço e Salto produzem quando o efeito inicial alcança várias criaturas. Dois alvos da Explosão falhando por 5 poderiam lançar dois respingos sobre o mesmo terceiro alvo; com seis inimigos próximos, o dano por alvo cresce além do modelo de pacote isolado. Não há recursão, mas ainda há múltiplos gatilhos independentes.

**Correção conservadora para o núcleo:** cada uma dessas peças produz um pacote secundário por conjuração, a partir de um alvo inicial que satisfaça o gatilho; indicar como se escolhe esse alvo antes da resolução. Alternativa: reservar a combinação área + Salto/Estilhaço ao catálogo R07 e declará-la não coberta pelas montagens deste lote. É mudança mecânica/restrição de interpretação, portanto registrar motivo. Não afirmar que a frase “não gera sequência” já elimina essa sobreposição.

### P2 — Salto passa a ter rolagem de ataque, mas efeitos por ataque não devem entrar silenciosamente

**Local:** FUNDAMENTO.md:486; fonte de interface `sistema/03-mecanica/03-economia-de-acao-e-iniciativa.md:170`.

A candidata corretamente explica que o alvo secundário pode resistir. Porém, a fonte dona exclui expressamente Salto dos ataques que ativam Alvo de Caça. Tornar o salto “novo ataque” introduz gatilhos de acerto e crítico que a montagem anterior não tinha.

**Texto mínimo sugerido:** “Essa rolagem apenas resolve o dano do Salto; não ativa benefícios que dependam de realizar ou acertar outro ataque, nem reaplica as peças do feitiço.” Decidir se 20 natural amplia seu dano; a solução conservadora preserva pacote secundário não crítico. Se a intenção for conceder crítico, registrar a mudança e seu efeito sobre o orçamento, sem dizer que era inerente à regra anterior.

Repor no exemplo o alcance próprio de 9 m e o alvo mais próximo do catálogo, ou deixar claro que o exemplo remete a esses requisitos. Toque já foi corretamente limitado a ambos os alvos ao alcance do conjurador.

### P2 — Áreas com ataque precisam preservar críticos individuais

**Local:** FUNDAMENTO.md:337; `regras-basicas/lote-02/ATAQUES-E-DEFESA.md`, regra de crítico.

O parágrafo começa com área resolvida por ataque e logo exemplifica TR. A leitura por quantidade de dados já melhora muito a divisão, mas falta dizer que o 20 de um alvo não duplica o dano de todos.

**Correção editorial mínima:** começar com “Numa área...” e separar ataque/TR. “Resolva os ataques ou TRs individualmente. Role uma vez para cada quantidade de dados necessária; resultados iguais usam o mesmo total. Um crítico só aumenta o dano contra o alvo desse ataque.” O crítico continua dobrando apenas os dados que a regra de crítico autoriza; Salto, Alvo de Caça e demais adicionais não entram por proximidade textual.

### P2 — Preservar a decisão histórica sobre Acúmulo

**Local:** FUNDAMENTO.md:482; `sistema/ESTADO-ATUAL.md:1856`; `sistema/03-mecanica/03-economia-de-acao-e-iniciativa.md:211`.

O registro v0.259 contém decisão explícita do usuário aceitando Acúmulo ultrapassar o antigo teto no quarto uso consecutivo, porque exige continuidade contra o mesmo alvo e a luta tende a já terminar. Portanto, a nova definição de teto não deve apagar essa exceção por inferência. O texto atual não cita Acúmulo; uma futura interpretação “todo dado adicional soma ao teto” criaria nerf não registrado.

**Correção mínima:** distinguir dados adicionais da própria conjuração dos dados acumulados por usos anteriores. “Acúmulo conserva sua progressão entre usos; sua exceção ao teto e a combinação com multiplicadores serão conferidas no catálogo.” Se decidir mudar, registrar como mudança mecânica, com comparação por rodada, e não como mera correção de redundância.

## Passagem de Papel — operacional, com três esclarecimentos pequenos

**Locais:** FUNDAMENTO.md:744–767. **Natureza:** original de Projeto M; não é evidência de cânone.

A ficha define preparação física, distância, tamanho da abertura, ação, PE, concentração, término, bloqueio, contenção e falha de chegada. O Efeito Próprio Pesado custa 8/9/11 nas Classes 5/6/7 sem desconto de Família; cabe em 8/12/16. Não há ganho oculto de pontos por descartar os dados. O alcance urbano de 1.500 m é uma escolha candidata, não dado da obra.

1. **P2 — Visão da saída:** Conjurar exige enxergar alvo/origem; a ligação atravessa paredes entre endereços e requer apenas tocar a entrada. Inserir “Não precisa enxergar a outra marca” para a exceção não depender de adivinhação.
2. **P2 — Marcas excedentes:** “Fixar duas marcas” e “uma passagem por vez” não respondem se existem vinte marcas prontas espalhadas pela cidade. A frase final sugere um par fixo. Inserir “Registre o par durante a preparação; só esse par pode ser ligado neste uso”, ou, caso seja a intenção restrita, “Só pode manter duas marcas preparadas; fixar outra desfaz uma anterior à sua escolha.” Não inventar destruição retroativa de marcas sem registrar a escolha.
3. **P3 — Pessoas carregadas:** criatura disposta pode atravessar e leva o que carrega. Vale explicitar se uma pessoa inconsciente carregada acompanha, pois o exemplo promete retirada de pessoas. Isso deve seguir transporte/contenção gerais; o portal não deve dispensar o peso nem soltar uma criatura agarrada. Uma frase resolve; não é necessário criar subsistema de consentimento.

Família Fechada “Marca” e marcas de papel não são conflito mecânico: o segundo termo é suporte físico da capacidade própria. Ainda assim, a coincidência pode confundir iniciantes. Evitar usá-la como exemplo didático de uma Família Marca livre ou fechada; se houver troca no exemplo, não mudar as regras da Família por causa do nome comum.

## Correções verificadas nesta passagem

- Conjurar usa Classe original ou maior por Ampliar; não concede redução livre de Classe.
- Requisito de enxergar alvo/origem está expresso, com exceção como Sem Ver.
- O limite de conjurações agora acompanha Turnos: uma acima de Classe 0 e a outra Classe 0, mesmo com conversão de ações.
- O TR normal reduz quantidade de dados pela metade, para baixo; não confunde com metade do resultado rolado.
- Máxima usa três quartos do dano e segue arredondamento do dano recebido, para cima após as defesas aplicáveis.
- Controle preserva saldo anterior ao descarte voluntário; descartar dados gratuitamente não compra +2 CD.
- Só condições Pesadas recebem o teste de saída de fim de turno pela regra geral, além de eventuais saídas próprias.
- Travessia usa Classe 0 e Passo, descartando o dano restante; não compra por 6 PE um resultado que Classe 0 já fornecia.
- Efeito distingue espaços comuns Classes 1–7 da quantidade própria de Classe 0.
- Classe 0 de Apoio não recebe vida temporária inventada com Classe fictícia 1; mantém só sua Melhoria Leve aplicável.
- Troca de espaço por invocação distingue novo espaço e reescrita do nível; gratuita de progressão não se converte.
- Silencioso pode coexistir com Barulho, mas não cancela sua exposição mantendo o reembolso.
- Rajada/Mais Um/Junto repartem os dados; alvo ou tiro com zero dados não aplica gratuitamente os efeitos de um acerto.
- Liberação cobra a rodada inteira e não recebe devolução de Atrasar/Parado pelo mesmo impedimento.
- Fica está limitado e estacionário conforme abaixo.

## Fica: a decisão atual é aplicável, mas é uma mudança mecânica

**Texto conferido:** rodada da conjuração e cinco seguintes; termina no fim da última. Uma resolução por criatura por rodada, inclusive erro ou TR que evite dano. Aplicação inicial consome a oportunidade daquela criatura. Depois, resolução ao iniciar turno ou entrar. Área fixa, até se a Forma inicial for Aura. Metade dos dados iniciais nas aplicações seguintes, sem repetir outras peças.

A administração exige uma marca por criatura por rodada, não uma reserva de dano pela vida inteira de cada criatura. Isso é viável para área persistente. Não chama a persistência de “seis turnos seus”, nem permite seis aplicações extras após a inicial.

**Atenção histórica:** a fonte antiga dizia um minuto numa rodada de dez segundos, mas não tinha limite expresso de uma resolução por rodada. Portanto, seis não era máximo comprovado da versão antiga. O novo limite fecha também reentradas e movimentações repetidas; é uma mudança mecânica, não só conversão de unidade.

A candidata geral de Turnos usa seis segundos. Sem ajuste, um minuto pode alcançar dez rodadas em vez de seis. A opção de seis janelas globais em Fica evita ampliar essa exposição por mera troca do relógio. Isso não resolve automaticamente todos os buffs/debuffs de um minuto do sistema; Concentrada, Alvo de Caça, Marca etc. precisam constar do mapa de revisão R07. Não alterar todos para 36 segundos por extensão.

**Cenários ideais, sem acerto/TR, entrada repetida ou concentração perdida:**

| Dados iniciais | 1 aplicação | 6 janelas: inicial + 5 persistentes | 10 janelas: inicial + 9 persistentes | Aumento de 6 para 10 |
|---|---:|---:|---:|---:|
| 5d8 | 5d8 | 15d8 | 23d8 | 53,3% |
| 8d8 | 8d8 | 28d8 | 44d8 | 57,1% |

O percentual não é constante: depende do arredondamento dos dados. São limites de exposição normalizada, não dano esperado real nem demonstração de máximo histórico.

## Certeiro: verificação numérica delimitada

Arquivos reproduzíveis: `/tmp/fundamento-certeiro-modelo.py` e `/tmp/fundamento-certeiro-resultados.json`. Reexecutado nesta passagem: 63 comparações com orçamento e três com dados iguais. Preços lidos da tabela publicada de Classes, sete linhas verificadas. Enumeram-se exatamente os vinte resultados de ataque, com crítico no 20 natural e dado d8 de média 4,5.

Certeiro continua exigindo ataque, mantém crítico no acerto e, depois de todas as tentativas como De Novo, causa metade dos dados para baixo se o erro final foi contra alvo válido. O erro não aplica os outros efeitos nem é crítico. A peça não permite atacar sem visão/alcance/caminho.

**Classe 5, preço normal:** 15d8 comuns contra 10d8 com Certeiro após pagar Média 5. Sem bloqueios, vantagem ou defesa posterior:

| Chance de acerto | Ataque comum | Certeiro | TR normalizado: mesma chance de falha que o acerto |
|---|---:|---:|---:|
| 25% | 20,25 | 30,375 | 40,5 |
| 50% | 37,125 | 36 | 49,5 |
| 75% | 54 | 41,625 | 58,5 |

São médias de dano, não valores inteiros de uma rolagem. O ataque comum pode superar Certeiro quando acerta com frequência. Certeiro encontra utilidade contra Defesa alta sem depender de TR fraco. O comparador TR normaliza probabilidades apenas para isolar resolução/preço: ele não demonstra que um inimigo real terá Defesa e resistência correlacionadas. Desconto de Família e reembolso real mudam a comparação e estão nos 63 casos.

Limitações: Bloquear é escolhido depois de ver o ataque e não está simulado; não há vantagem, crítico ampliado, redutores, imunidades nem gatilhos adicionais. A mudança de Certeiro exige atualizar sua entrada duplicada em Invocações e qualquer interpretação antiga que diga que ele retira o ataque e elimina crítico. O modelo não atesta equilíbrio do novo pacote de Máxima.

## Encaminhamento R07 e integração futura

1. Catálogo unificado: inserir mudanças com preço, famílias, pré-requisitos, duração e resolução; espelhar em Invocações e heranças Marciais sem duplicação divergente.
2. Repetições: caso área + respingo/pulo; acúmulo entre usos; simultaneidade; crítico nos pacotes secundários; formas de custo zero e Classe 0.
3. Duração: mapear todos os minutos depois da mudança de dez para seis segundos. Fica foi tratado, o catálogo inteiro ainda não.
4. Cura: preservar teto comum de 2 × Classe e Onda 3 × Classe menos Pesada; Máxima é exceção expressa, não justificativa para burlar o teto normal com reembolso.
5. Não chamar resultados dos verificadores históricos de validação desta candidata: eles usam premissas antigas e não testam todas as novas interfaces. Os relatórios históricos de v7/pac7 foram preservados em /tmp para comparação, não como aprovação automática.
6. Registrar como mudanças mecânicas: Certeiro novo; gatilho de Salto com nova resistência; duração e resolução de Fica; escopo de teto por montagem em áreas; orçamento fixo e exclusões da Máxima; Efeito Próprio da passagem.

A revisão de morte/Integridade permanece fora deste lote, conforme solicitação do usuário; não usar exemplos daqui para preencher suas lacunas por inferência.
