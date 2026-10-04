# Fundamento — revisão, decisões e fontes

Data: 03/10/2026. Lote candidato de R06, com interfaces de R07 e R08. Fontes publicadas preservadas; as alterações propostas pertencem a este diretório e às suas sincronizações.

## Escopo e método

O trabalho partiu das dificuldades relatadas pelo usuário: a criação era percebida como uma sequência extensa de informações, as combinações não explicitavam seus limites e Técnica Máxima parecia servir apenas para dano e cura. Também faltava apresentar a troca de espaço conhecido por entidade nos três meios de criação.

As passagens relevantes do manual vigente, das peças mecânicas, da edição integrada de Invocações e das candidatas anteriores de regras básicas foram confrontadas. Em seguida, foram elaborados procedimento, exemplos e ficha; auditorias por modelos examinaram compatibilidade, progressão numérica, interfaces e leitura por um iniciante. Os apontamentos deram origem a revisões de texto e a decisões mecânicas identificadas abaixo.

**Não houve leitura integral de todos os livros enviados, consulta a leitores humanos nem playtest.** A comparação externa foi dirigida a capítulos e entradas pertinentes. Os modelos de cálculo conferem os cenários explicitamente representados, não todas as combinações possíveis de personagem, inimigo e ambiente.

O resultado de cada conferência precisa ser consultado nos arquivos finais de `evidencias`, vinculado ao hash correspondente. A conferência final aprovou 233 verificações do PDF de 29 páginas; todas as páginas foram inspecionadas visualmente. Relatórios exploratórios podem conter propostas rejeitadas e números anteriores; o manuscrito e os contratos finais da candidata definem o que foi adotado.

## Fontes internas e seus papéis

Os caminhos abaixo são relativos à raiz do projeto.

| Fonte | Uso nesta revisão |
|---|---|
| `sistema/05-material/livro/manual/40-fundamento.md` | Publicação de referência: repertório, montagem, Formas, catálogos, passivas e trunfos. Suas contradições não foram tratadas como novas decisões implícitas. |
| `sistema/05-material/livro/manual/42-tecnica-marcial.md` | Equivalência de Kata/feitiço, custos, equipamento e Ōgi. |
| `sistema/05-material/livro/manual/43-sem-tecnica.md` | Manejo, semente e Auge; confronto das passagens de cura com a peça mecânica. |
| `sistema/03-mecanica/25-sem-tecnica.md` | Correção registrada desde v0.194: a limitação inicial de cura de terceiros é da aptidão, não de todo Manejo com Forma Cura. |
| `invocacoes/05-Edicao-Integrada/60-invocacoes.md` e cópia no manual | Regra corrente de aquisição por espaço, nível/evolução da entidade, custos e repertório próprio. A igualdade das cópias foi conferida na auditoria de rotas. |
| `sistema/03-mecanica/15-invocacoes.md` | Somente identificação de sua condição histórica e do encaminhamento à edição integrada. O desenho antigo não foi usado para revogar a troca atual por espaço. |
| `sistema/05-material/livro/manual/35-caminhos-e-trilhas.md` | Exceções expressas de aquisição e economia de ações; não reproduzidas no texto geral do Fundamento. |
| `sistema/05-material/livro/manual/25-origens.md` | PE como esforço na rota sem energia e limites de acesso pessoal. |
| `sistema/05-material/livro/manual/80-experiencia-e-progressao.md` | Fórmula de espaços, marcos e progressão. |
| `sistema/05-material/livro/planejamento-editorial/regras-basicas/lote-01/TESTES-E-TURNOS.md` | Ações, Ação Completa, limite de conjuração, TR e concentração na redação candidata atual. |
| Candidatas correntes de Dano/Condições, Movimento, Energia/Vestígios e Recuperação | Interfaces de dano, oposição, deslocamento forçado, informação, cura e queda. Não transformam a revisão adiada de Morrendo em regra nova. |
| Modelos matemáticos anteriores de Fundamento, extraídos em `evidencias` | Comparação entre a intenção escrita e a execução efetivamente calculada, especialmente áreas, tetos e orçamento. Não certificam por si as novas regras. |

Os relatórios `evidencias/fundamento-compatibilidade.md`, `evidencias/fundamento-rotas-didatica.md`, `evidencias/fundamento-maxima.md` e `evidencias/fundamento-maxima-checklist-final.md` preservam localizações e argumentos detalhados. A leitura crítica da candidata, incorporada às evidências, deve ser interpretada como retrato da versão que examinou, não como declaração de que seus problemas continuam presentes após correções.

## Comparação com outros RPGs

Leitura dirigida de fontes primárias, sem copiar a redação ou importar automaticamente suas economias.

| Fonte consultada | Aplicação editorial |
|---|---|
| [D&D 2024 — Spells](https://www.dndbeyond.com/sources/dnd/br-2024/spells) | Separar obtenção e uso; registrar campos de execução. Os espaços de Projeto M continuam sendo repertório, não usos diários. |
| [Pathfinder Player Core — Spells](https://2e.aonprd.com/Rules.aspx?ID=2221) | Distinguir alcance, área, alvo, defesa e duração na ficha; identificar o que muda ao ampliar. |
| [Fate Core — Building Stunts](https://fate-srd.com/fate-core/building-stunts) | Partir de uma finalidade concreta e definir limites para uma capacidade própria. Não importar bônus ou pontos Fate. |
| [D&D 2024 — Forcecage](https://www.dndbeyond.com/spells/2618916-forcecage) | Referência dirigida de controle elevado com tamanho, duração e saídas declarados; não adotar sua potência por analogia. |
| [Pathfinder Player Core — Synaptic Pulse](https://2e.aonprd.com/Spells.aspx?ID=1710) | Referência dirigida de controle em área com oposição e resultados especificados. Não importar seus graus de sucesso. |

Também foram consultados [Descriptors, Mutants & Masterminds SRD](https://www.d20herosrd.com/6-powers/descriptors/) para distinguir descrição e efeito e [Collective Transposition, Player Core 2](https://2e.aonprd.com/Spells.aspx?ID=1978) para examinar seleção, consentimento e destinos do reposicionamento coletivo. A Retirada proposta usa percurso físico e números próprios; não converte teleporte daquele jogo.

Essas comparações ajudam a avaliar apresentação e completude. Não demonstram preferência estatística de leitores nem provam que uma opção de Projeto M está equilibrada porque se parece com uma opção de outro jogo.

## Verificação de cânone e limites de acesso

Foi localizado o [capítulo 134 de Jujutsu Kaisen na VIZ](https://www.viz.com/shonenjump/jujutsu-kaisen-chapter-134/chapter/21808), mas a leitura dos painéis exigia assinatura. **Os painéis não foram verificados nesta rodada.** A página de entrada não permite confirmar a mecânica de Uzumaki, sua extração ou todos os efeitos de uma Técnica Máxima.

A [errata oficial do fanbook](https://sp.shonenjump.com/j/notice/2021/03/04/210304_oshirase001.html) corrige a classificação da referência a Uzumaki. Ela **não valida uma lista de efeitos nem uma regra de criação**. Material comunitário pode localizar capítulos; não substitui o texto da obra para afirmar poderes.

Por isso, Fios de Tensão, Fio de Arrasto, Passagem de Papel e os demais exemplos do lote são **criações originais do Projeto M**. Níveis, pontos, PE, recarga, descontos, acesso pelas três rotas e procedimentos de oposição são regras do jogo. Não se afirma que todas as técnicas da obra seguem essa construção ou que os exemplos foram extraídos dela.

## Registro de decisões e motivos

O registro corrente está em [ALTERACOES.md](ALTERACOES.md) e na versão estruturada [ALTERACOES.json](ALTERACOES.json): **55 decisões**, cada uma com antes, candidata, motivo, natureza e destinos de sincronização. Vinte e oito foram classificadas como mudanças mecânicas ou fechamento de lacunas. Essa classificação inclui propostas conservadoras; não quer dizer que todas aumentem a força do personagem.

As decisões mais sensíveis são o orçamento da Máxima 8/12/16, as peças incompatíveis com seus dados fixos, a função nova de Certeiro, as seis janelas de Fica, os secundários únicos de Salto/Estilhaço, os tetos de cura e as lacunas de Classe 0. Acúmulo preserva a exceção histórica. Os efeitos próprios de passagem e retirada são propostas novas que precisam de mesa.

Os patches de [sincronização](sincronizacoes) preservam as âncoras anteriores. A [matriz](MATRIZ-AUDITADA.json) conserva as recomendações brutas dos auditores e acrescenta decisão atual, cobertura e estado. Das 54 linhas, 24 estão consolidadas, 5 parciais, 1 é interface preparada e 24 aguardam R07. Nenhuma recomendação pendente é uma permissão publicada.

## Revisão didática

A leitura crítica usou perguntas concretas: quantas criações existem no nível inicial; qual recurso é gasto ao lançar; como reservar entidade; quando ataque/TR é escolhido; qual medida aumentar; como montar sem dano; como ampliar e como atualizar a Máxima.

O primeiro exemplo completo foi recomendado para o início. Também foram apontados: remissões genéricas a “o catálogo”; exemplos cujas dimensões ou prazos não estavam na ficha; redação de Máxima que confundia ausência de dano com a Forma Efeito; progressão de orçamento sem instrução suficiente de reconstrução; e um exemplo de fio cuja imagem sugeria uma locomoção não concedida pela peça. Esses achados foram tratados: exemplo na página 3, medidas/prazos completos, Máxima de retirada em combate e progressão explícita. As contas e âncoras do texto final foram reexecutadas após as correções.

Os títulos devem continuar simples e localizáveis. Repetições que resolvem consultas diferentes — como a incompatibilidade de Toque/Longe junto da Forma e na matriz — podem permanecer. Avisos genéricos repetidos de que a descrição não concede poderes devem ser reduzidos quando a limitação específica já estiver clara.

## Validação numérica e seus limites

As evidências incluem cálculos de orçamentos/preços, descontos, progressão entre faixas, áreas, devoluções, cura e casos de repetição. As buscas de perfis examinam se uma composição cabe; **não provam que suas peças podem ser combinadas narrativamente ou que ela está equilibrada em campanha**.

A correção de orçamento da Máxima elimina regressões representadas no modelo. Ela também permite efeitos mais amplos nas faixas altas, como dano combinado a Controle. Exige análise de alvo, TR de saída, duração, concentração, quantidade de inimigos e disponibilidade de PE. Não afirmar que o dano-base inalterado equivale a força total inalterada.

Áreas e Fica devem ser avaliados em encontros com diferentes quantidades de alvos, permanência e contramedidas. Cura pede análise da reserva ao longo do dia, excesso desperdiçado, tamanho do grupo e interação com queda. Os exemplos mostram regras executáveis; não substituem essas comparações nem observação de mesa.

Resultados finais e cenário de cada ensaio: consultar `evidencias`. A inspeção final aponta o PDF e seu hash; uma tabela acrescentada à página 17 foi renderizada e reinspecionada, e as outras 28 páginas mantiveram pixels idênticos. Nenhuma imagem de IA foi usada; a comparação editorial não implica reaproveitamento de ilustrações de outros livros.

## Pendências e integração

**R07 — catálogo.** Consolidar preços, textos, famílias, repetição permitida, pré-requisitos e incompatibilidades de cada entrada. Publicar destinos de consulta verificáveis. Resolver pares ainda abertos, como fronteiras de Inescapável, encadeamentos, persistência e efeitos próprios. Sincronizar o catálogo comum duplicado em Invocações; não deixar o construtor pessoal e o de entidades ensinarem versões diferentes de uma peça compartilhada.

**R08 — poderes avançados.** Concluir Domínio e confrontos, comparar Máximas ofensivas, de cura e utilidade e testar Controle com duração. Uma aplicação fora de combate bem definida não encerra sozinha a revisão de proteção/controle sem dano durante combate. A progressão e as regras de reescrita da Máxima devem ter resposta única; as remissões de Auge, Ōgi e domada precisam acompanhar a decisão consolidada.

**Rotas.** Os cinco documentos em `sincronizacoes` são substituições revisáveis. A integração deve conferir as âncoras, as cópias e a fonte vigente, em vez de aplicar posições antigas de linha sem inspeção. Requisitos próprios de Origem e equipamentos permanecem no capítulo dono.

**Morrendo e Integridade.** O usuário pediu uma revisão de Integridade em conjunto com a futura revisão de morte. A dependência abrange dano de alma e seus estágios, ordem de redução de dano, Remenda, cura a zero, estabilização, Aguentar/Insistir, dano após queda, Sequelas/Cicatrizes, morte do invocador, efeitos persistentes e recursos gastos durante inconsciência. Esse trabalho permanece na fila; o presente lote não o substitui por uma frase de Fundamento.

**Testes humanos.** Depois de estabilizar catálogos e procedimentos, pedir a um iniciante que monte e use uma ficha sem auxílio oral, e a jogadores experientes que procurem combinações inválidas. Registrar dúvidas reais, tempo de consulta e decisões divergentes. Até que isso aconteça, os resultados são auditorias e ensaios por modelos, não evidência de aceitação pelos jogadores.

## Conferência final reproduzível

`auditar.py` aprovou 68 verificações de modelo/texto e 53 casos funcionais. Enumerou 39.032 estados de orçamento e 840 perfis de preço para a progressão da Máxima. Os 63 cenários de Certeiro com custos são comparações exatas de um ataque antes das defesas; não incluem Bloquear. Certeiro também funciona quando Bloquear/Aparar torna o ataque um erro final, interface que ainda exige comparação em combate completo.

`conferir.py` aprovou 233 verificações: texto presente em cada página, margens, fontes incorporadas, remissões, marcadores recolhidos, revisões vinculadas por hash e preservação das fontes/publicações. Os totais descrevem verificações distintas; não somar estados de busca e verificações como se fossem partidas observadas.

A bateria humana proposta está em [TESTE-DE-MESA.md](TESTE-DE-MESA.md). Ela permanece por executar.

A última leitura independente das cinco seções de Máxima não encontrou bloqueador restante. Ela detectou uma proibição indevida de Precisão+TR no modelo de teste; o modelo foi corrigido conforme a fonte e recebeu um caso positivo de regressão. O manuscrito já preservava essa aplicação. O relatório está em `evidencias/fundamento-maxima-ultima-leitura.md`.

## Atualização de 03/10 — acesso e catálogo

Invocação por espaço exige Descrição e Regra que prevejam criar, chamar ou controlar entidades; o requisito também aparece nas rotas de Manejo/Kata e nos patches. O exemplo positivo usa animais de papel, e o negativo uma técnica que apenas corta fios. FU-51 registra o pedido. FU-52 fecha Armado/Segura na Técnica Máxima, em continuidade com R07.

## Estado após catálogo R07

R07 está escrito em 30 páginas, com 106 entradas conferidas. A matriz atual está em `../../catalogo/lote-01/evidencias/MATRIZ-R06-R07.json`: 53 combinações consolidadas e uma interface com Condições. As contagens anteriores da matriz neste relatório documentam a etapa R06 antes desse fechamento. FU-51 a FU-55 registram requisito de invocações, Máxima adiada, Sem Volta/Vazio, títulos e novo exemplo de Passiva Livre. A candidata final tem 55 decisões, das quais 28 mecânicas/lacunas.
