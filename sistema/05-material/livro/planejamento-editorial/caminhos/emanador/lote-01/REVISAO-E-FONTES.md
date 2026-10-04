# Revisão do Emanador

Autoria e autoauditoria de uma candidata isolada. A fonte integrada, os contratos v0.331 e os donos das interfaces foram lidos. Não foram alterados o manual publicado ou os arquivos de outra unidade. O manuscrito contém 19 páginas lógicas e 48 entradas inventariadas. Há 29 decisões rastreáveis em `ALTERACOES.json`; fechamentos de lacunas são identificados como mudanças candidatas, não atribuídos ao texto histórico.

## Critérios editoriais

A leitura foi dividida por procedimento: escolher, pagar, resolver e registrar. Os nomes da fonte foram preservados, salvo a correção ortográfica **Sobre Carregar Energia → Sobrecarregar Energia**. A ficha explica aquisição e progressão antes das escolhas. As tabelas de Modulações e Propriedades mantêm todas as opções sem reproduzir as descrições do catálogo.

Os exemplos cumprem uma função concreta: diferença de preço em dados, perda de devolução, custo da Classe ampliada ou prazo de um recurso. O leitor não precisa interpretar uma cena ficcional para descobrir a regra. O parecer por página identifica casos permitidos e impedidos e as interfaces pertinentes. Essa avaliação é editorial; não substitui leitura por um jogador estreante.

Como referência primária de organização, [D&D Basic Rules 2024 — Classes, Sorcerer e Metamagic](https://www.dndbeyond.com/sources/dnd/br-2024/character-classes) apresenta alterações por escolha, custo, momento e limites de combinação. Esse formato ajudou a separar as opções do Emanador. Não foram importados o valor dos recursos, a escala de dano ou permissões de alcance daquele sistema.

O capítulo não faz alegações sobre poderes canônicos de personagens de Jujutsu Kaisen. Vínculos, Ecos, Impulso e estas fórmulas são mecânicas autorais do Projeto M. Não há justificativa para apresentar seu balanceamento como fato da obra.

## Orçamento e alterações

O auditor cobre **35.553 cenários** de troca, variando Classe, resultado original, preço retirado, preço acrescentado e devoluções. O resultado nunca cresce pelo simples ato de Remodelar. Uma troca barata descarta a diferença; uma troca cara paga a diferença com resultado. O recálculo final pode exigir redução adicional, sem devolver os dados já pagos por uma devolução anteriormente desperdiçada.

Esse último procedimento é um fechamento conservador, não uma ordem expressa encontrada no original. Ele evita que a mesma troca produza dois resultados, dependendo de quando a mesa reaplica as Restrições. A comparação de preços conjuntos em Composição permite que duas trocas simultâneas se compensem dentro do mesmo Desdobramento, mas não carrega sobras para outra conjuração.

**Forçar** tem uma exceção real: o PE paga a Melhoria, sem descontar novamente os mesmos pontos dos dados. Seu limite continua uma Modulação e uma vaga acima do máximo. Transformar essa habilidade em PE mais perda de dados enfraqueceria a fonte sem necessidade. Ela continua sem liberar Família Fechada, peça incompatível, dano acima do teto ou uma obrigação de tempo ignorada.

Forma Fluida usa pontos úteis para comparar dano, cura e vida temporária. Isso impede converter nove pontos de Apoio, expressos como 27 PV temporários, em 27 dados. A nova Forma mantém sua conversão e seus tetos.

## Reduções de custo

Foram comparados **72 perfis** de Classe original, Classe ampliada e redução fixa. As fórmulas são alternativas completas:

| Situação | Conta | PE antes de acréscimos |
|---|---|---:|
| Classe 2 ampliada para 4, Afinidade | metade de 6 + diferença 6 | 9 |
| Mesma conjuração, Eco disponível | metade do custo normal 12 | 6 |
| Composição proibida | metade dos 9 já reduzidos | 5 |
| Classe 2 ampliada para 5, Instintiva | 1 + diferença 9 | 10 |
| Mesma conjuração, Eco disponível | metade de 15, para cima | 8 |
| Classe 2→4, Ritual −2 e Afinidade | metade de (6−2) + 6 | 8 |
| Classe 2→4, Ritual −2 e Eco | metade de (12−2) | 5 |

O personagem escolhe uma conta completa. Uma vantagem não obriga a pagar mais que outra alternativa disponível. Desdobramento, Impulso e custos independentes são acrescentados depois. Instintiva não zera sua base de 1 PE. Primeira/próxima conjuração consomem seus gatilhos mesmo quando o desconto escolhido é outro.

Essa resolução preserva a fórmula publicada de Afinidade ao Ampliar e as fórmulas dos donos Eco/Cobrança. A vedação de compor essas metades é uma decisão candidata aprovada para evitar descontos multiplicativos não delimitados. O fechamento global precisa sincronizar R07/R19, como registra `INTERFACES.json`.

## Confiabilidade e potência

A análise de **133 perfis probabilísticos** parametriza a chance de o alvo resistir, sem fingir um adversário médio único. Se essa chance é 50%, a chance de aplicar o efeito passa de **50% para 75%** com desvantagem em um TR. Se Sobrecarregar permite também Corrigir essa resistência pelo mesmo procedimento, passa a **93,75%**. Na Classe 4, a primeira opção cobra 2 PE extras; Corrigir acrescenta 4 somente quando a primeira resolução ainda resiste. Nesse perfil, o custo adicional médio da combinação é 3 PE.

Esses percentuais medem um resultado binário selecionado. Não são DPR, não incluem imunidades, resistências a condições, Bloquear ou o valor narrativo do efeito. Sobrecarregar é uma vez por cena e veda gerar Impulso até o fim do próximo turno; a combinação não fica disponível continuamente. O forte ganho de confiabilidade é preservado como entrega de nível 19, com o custo e o intervalo explicitados.

Aperfeiçoar um d8, repetindo cada 1 ou 2 uma única vez e mantendo o novo resultado, aumenta a média de **4,5 para 5,25**, ou **16,67%**. Nove dados passam de 40,5 para 47,25. Uma rolagem compartilhada leva esse ganho a cada alvo que usa o mesmo total, o que torna áreas uma aplicação vantajosa. O texto limita o benefício a uma rolagem previamente escolhida e não permite corrigir também o TR com a mesma escolha de Intensificar. Em Sobrecarregar, Intensificar continua sendo uma opção, não duas.

Ressonante compra flexibilidade e economia adicional, não outra conjuração. Seu registro conserva só a peça e o método, respeita a categoria antes de descontos e não se copia sozinho. Contraponto pode somar alterações, mas não duplica a Modulação Forçada. Acorde não permite quatro alterações e conserva prazos individuais. Não foi simulada a utilidade de toda combinação de peça e cenário, que depende dos catálogos e da aventura.

## Arma, ações e inventário

Cadência consome Padrão e Bônus, resolve uma parte de cada vez e não exige acerto na primeira. O ataque conserva Canalizar quando seus requisitos permitem, porque o feitiço é uma resolução separada. Essa remissão local evita confundir Cadência com um ataque que transporta dano de feitiço, sem reproduzir a aptidão.

Cadência Marcial escolhe dois ataques ou a alternância com feitiço. Cadência Expandida e Ritmo Convergente conferem a Classe efetiva após Ampliar. A origem remota de Manifestação mantém as exigências de Toque/Aura e de Formas centradas; não amplia gratuitamente a aplicação que recebeu devolução por permanecer próxima.

Forma Mutável conserva carga, tipo de munição, Integridade e estados de recarga. Precisa descarregar antes de assumir perfil incompatível ou pequeno demais. Se o vínculo termina depois de ter sido carregada com munição do perfil transformado, a carga é conservada e impede disparar até o ajuste normal. Não surge estoque, conserto, disparo pronto ou mercadoria permanente.

Sentido do Vínculo conserva **1 km** por decisão editorial explícita: é localização narrativa, não alcance de ataque ou área na grade. As medidas de combate permanecem múltiplos de 1,5 m. Saber uma direção não revela o espaço de chegada necessário a Passo da Arma.

## Estado da validação

O auditor reproduzível passou **92 verificações e 62 casos**, além dos cenários numéricos acima e cinco mutações que removem limites relevantes. Preservação das cinco fontes publicadas também foi conferida. Os casos incluem prazos de Ecos, consumo de Impulso, intervalo de Sobrecarga, proibição de geração por reaplicação e estoque na mudança de arma.

Maxima concluiu uma leitura independente da fonte e da candidata, com 35 verificações próprias e nenhum bloqueador concreto. A exportação do PDF, navegação, fontes e inspeção de páginas estão **pendentes**, atribuídas à raiz. O quadro `VALIDADORES.json` conserva esses estados por item e por página. Não há playtest, amostra de jogadores, comparação exaustiva entre os Caminhos ou alegação de equilíbrio definitivo.


## Prova revisada

A revisão independente por maxima foi concluída com 35 verificações próprias. O agente principal inspecionou todas as19 páginas da prova final. A conferência automática está em CONFERENCIA.json. Essas etapas substituem as pendências de PDF/visual desta versão, sem alegar playtest humano.
