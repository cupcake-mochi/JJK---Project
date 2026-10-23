# Dois protótipos: recursos e ritmo dos inimigos

23 de outubro de 2026. Continuação da [reavaliação 63](63-reservas-usos-e-ritmo-dos-inimigos.md). **Estudo de projeto, com variantes experimentais; nenhuma substitui o piloto ou define o construtor geral.** A coleção de ideias continua como fonte de consulta enquanto Claude trabalha nela. Esta entrega fica na pasta do Guia.

## Resultado para discussão

**PE não resolvem sozinhos a repetição dos melhores golpes.** No exemplo simples, seis PE e dois usos permitem as mesmas duas tentativas, enquanto o custo permanecer em três e nada alterar a reserva. Uma regra de intervalo modifica quando essas tentativas podem acontecer. Uma reserva compartilhada — de PE ou de usos — permite escolher entre capacidades concorrentes.

O que os PE acrescentam aqui é a possibilidade de **preços diferentes e alterações pequenas no saldo**, junto das interações já publicadas. Isso pode justificar seu controle numa única luta; não exige um inimigo que economize para outra missão. Também pode ser trabalho desnecessário quando nada disso influencia a cena.

**Recomendação revisada após o esclarecimento de Mizuki:** escolher o limite pela função da habilidade, sem tornar PE o padrão obrigatório dos especiais. Uso livre, recarga, intervalo, preparo, condições e reserva compartilhada são caminhos diferentes. Nenhum precisa aparecer em todas as fichas. Conservar uma informação de energia para as interações do mundo também não obriga toda habilidade a consumir essa reserva.

A pergunta anterior de preservar PE ou adaptar as interações foi prematura: deixou de fora esse caminho intermediário e misturou funcionamento com compatibilidade. Mizuki não a aprovou; esclareceu que seu maior receio é a reserva apenas incentivar gastar tudo imediatamente. Os protótipos iniciais R/U/I/M permanecem para comparação; as variantes N abaixo acrescentam capacidades sem gasto-base, mantendo energia existente. Nenhuma constitui decisão final.

## O receio de gastar tudo cedo

No protótipo simples, o inimigo não tem outro destino para PE. Com alvo disponível, usar Impacto imediatamente aproveita uma oportunidade que poderia perder ao ser derrotado. Diminuir a reserva o faz esgotar mais cedo; aumentá-la permite mais repetições. Nenhuma dessas mudanças, sozinha, cria uma razão para reservar energia.

Isso não torna ruim todo inimigo que começa com seu melhor golpe. Uma ameaça simples pode ter esse comportamento. O problema é cobrar acompanhamento de recurso esperando uma escolha que o repertório não oferece. Se a intenção for alternância ou uma chance de impedir o ataque, escrever esse funcionamento diretamente pode servir melhor.

**Recarga também não garante uma razão para esperar.** Usar cedo inicia mais cedo as oportunidades de recarregar. Nas [regras de D&D](https://www.dndbeyond.com/sources/dnd/br-2024/how-to-use-a-monster), a orientação de condução é usar capacidades fortes limitadas cedo e com frequência; a recarga controla o retorno. O [GM Core de Pathfinder 2e](https://2e.aonprd.com/Rules.aspx?ID=2874) distingue capacidades de uso livre e limitado, incluindo repetições não consecutivas. São exemplos de controles específicos, não de uma exigência para todo inimigo nem de valores transferíveis para este sistema.

Para produzir uma escolha de momento, a situação precisa mudar o valor da capacidade: um alvo pode sair de alcance, uma defesa pode salvar o inimigo, um preparo pode ser interrompido ou uma posição melhor pode justificar esperar. Para produzir somente espaçamento, um intervalo já pode cumprir o objetivo. Não exigir deliberação complexa de toda criatura.

## Método e limites

Os dois protótipos compartilham o corpo do Amontoado. O primeiro conserva seu repertório; o segundo acrescenta uma proteção experimental. Dentro de cada protótipo, só muda o controle de recursos ou repetição. **Não comparar a força do segundo com a do primeiro como se a proteção fosse gratuita ou já equilibrada.**

Uma **oportunidade** é um turno próprio no qual o inimigo pode agir e encontra alvo válido. As contas de disponibilidade usam janelas de um, três, cinco e oito turnos, sem derrota, erro, impedimento de Selo ou perda de alcance. Na comparação de proteção, existe no máximo uma ocasião válida para reagir por turno próprio. Essas janelas não são previsão de duração de combate.

Não houve simulação de encontro completo, leitura externa ou teste de mesa. As contas conferem sequências, escolhas possíveis e estados de recursos. O resultado não fixa dificuldade, vida, dano, quantidade de PE por nível ou duração desejada da luta.

## Ficha comum de ensaio

Fonte: [Amontoado do depósito, registro 14](14-base-pequena-de-inimigos-r53.md) e [dados da base](apoio-piloto/base-inimigos.json). A ficha abaixo permite conferir o que permanece constante. Os números já eram uma proposta local do piloto, não uma tabela universal aprovada.

| Campo | Valor conservado |
|---|---|
| Corpo | Maldição Média, com alma, dois braços, duas pernas e mãos funcionais |
| Nível e maestria | Nível 2; maestria 1 |
| Atributos | Força 3; Destreza 1; Constituição 3; Inteligência 1; Essência 1 |
| Vida e Integridade | 48 PV; 24 de Integridade |
| Defesa e Bloquear | Defesa 11; Bloquear 2d10, sem bônus |
| Movimento e iniciativa | 9 m; iniciativa +1 |
| Testes de resistência | Físico +4; Vigor +3; Intelecto +1; Espírito +1 |
| Perícias treinadas | Atletismo +4; Furtividade +2; Percepção +2; Intuição +2 |
| Percepção | Visão e audição comuns; Leitura CE 1, conforme ficha original; sem percepção automática de ocultos |
| Ações | Padrão, Movimento, Bônus e uma Reação; um ataque na Ação Atacar |
| Derrota | A zero de vida ou Integridade, fica derrotado; não recebe Insistir de personagem jogador |
| Proteções | Sem resistências, imunidades ou redução passiva de dano acrescentadas |

**Pancada.** Ação Padrão para Atacar; um ataque a até 1,5 m, d20 + 4 contra Defesa ou Bloquear. No acerto, 1d4 + 3 de Concussão; no crítico, 2d4 + 3. Sem custo de PE. As manobras básicas permitidas pela ficha usam CD 12 e substituem esse ataque, sem dano automático.

**Impacto concentrado.** Feitiço de Classe 1, Ação Padrão, Toque a até 1,5 m. Precisa enxergar o alvo, juntar as palmas e tocá-lo. Ataque d20 + 4; no acerto, 3d8 de Concussão; no crítico, 6d8. Não causa condição nem dano em área. O recurso é pago antes da rolagem e permanece gasto no erro. Na versão com energia, custa 3 PE. Fundamento Força, Livres Mira/Castigo e Fechadas Amparo/Tempo/Marca, conforme a ficha original; o ensaio não acrescenta outros feitiços.

O controle de usos abaixo substitui experimentalmente o pagamento desse feitiço. É uma mudança de regra, identificada na própria variante, não uma leitura literal da R53.

## Protótipo 1: uma capacidade especial

**Intenção:** impedir que retirem caixas do depósito. Mantém a conduta do piloto: reage a agressão ou desmontagem, prioriza o consciente mais próximo e usa o último agressor para desempatar; não ataca inconscientes e não persegue para fora do anexo. Nenhum controle abaixo concede novo deslocamento ou ataque.

| Variante | Texto de recurso ou repetição | O que o mestre acompanha além da ficha comum |
|---|---|---|
| R — Reserva | 6 PE; Impacto custa 3. Sem intervalo adicional. | Um saldo numérico. |
| U — Usos | Duas tentativas de Impacto disponíveis. Marque uma ao tentar, inclusive no erro. Não há saldo de PE nesta hipótese. | Duas marcas. A tradução de interações energéticas permanece pendente. |
| I — Intervalo | Impacto sem custo de PE e sem limite total, mas só pode voltar no começo do segundo turno próprio posterior ao uso. | O turno em que volta. A retirada do custo também altera a R53. |
| M — Combinação mínima | 6 PE, custo 3, com o mesmo intervalo da variante I. | Um saldo e o turno em que Impacto volta. Não acrescentar uma contagem separada de usos. |

**Intervalo, exemplo.** Usa no turno 1, fica indisponível durante o restante desse turno e todo o turno 2, volta no começo do turno 3. No turno 2, pode usar Pancada, uma manobra permitida ou outra ação normal. Perder a ação desse turno não adia o retorno. Não há rolagem de recarga.

Na variante com intervalo, o estalo das placas acompanha o golpe e elas voltam a se fechar no começo do turno de retorno. Esse sinal não atrasa o primeiro golpe nem concede uma ação gratuita. Para que a pausa seja informação útil, explique ao grupo a relação observável depois de ela ser reconhecida; não espere que o jogador adivinhe uma regra oculta. Se quiser preparação interrompível antes do golpe, será outro desenvolvimento, com seus próprios custos e momentos.

### Disponibilidade sem interferência

H representa Impacto; B representa Pancada. Política usada apenas nesta conta: escolher H sempre que estiver disponível. Todas as condições de alvo e ação estão atendidas.

| Variante | 1 turno | 3 turnos | 5 turnos | 8 turnos |
|---|---:|---:|---:|---:|
| R — 6 PE | 1 H | 2 H | 2 H | 2 H |
| U — dois usos | 1 H | 2 H | 2 H | 2 H |
| I — só intervalo | 1 H | 2 H | 3 H | 4 H |
| M — PE e intervalo | 1 H | 2 H | 2 H | 2 H |

Em cinco turnos, R/U produzem **H, H, B, B, B**; I produz **H, B, H, B, H**; M produz **H, B, H, B, B**. Se o confronto terminar depois do segundo turno, R/U puderam tentar dois Impactos; I/M, apenas um. A pausa pode alterar bastante uma luta curta, embora preserve o total de M numa janela maior.

O intervalo sozinho não preserva o orçamento de dois usos: prolongar a oposição pode trazer mais Impactos. A recarga aleatória, já examinada no registro 63, também não foi acrescentada como uma versão supostamente equivalente.

### Quando as duas marcas deixam de equivaler a seis PE

Com 24 de Integridade máxima, perder 12 alcança o estágio 2. Na R53, o custo do feitiço de Classe 1 sobe de 3 para **4 PE**, e o movimento fica em 4,5 m, além do efeito do estágio 1. O aumento se aplica a cada conjuração enquanto esse estágio estiver ativo.

- Se a perda acontecer **antes** do primeiro Impacto, seis PE permitem uma tentativa, deixando dois PE.
- Se acontecer **depois** de um Impacto pago a três, sobram três PE e não cabe outro de custo quatro.
- Duas marcas sem tradução permitiriam duas tentativas nos dois casos. Isso é uma diferença mecânica; não basta mudar o rótulo do campo.

Uma apresentação que preserva a R53 pode dizer **“6 PE; normalmente cabem dois Impactos de 3; no estágio 2, o custo é 4”**. O mestre pode usar marcas correspondentes a três PE enquanto os custos forem esses, conservando o saldo exato. Quando houver gasto diferente, passe ao número. As marcas são uma forma de registrar PE, sem um segundo limite de dois usos: uma recuperação válida pode permitir mais tentativas.

## Protótipo 2: ataque e proteção concorrentes

**Amontoado reforçado de ensaio.** Mesmo corpo e repertório, com a seguinte capacidade adicional, criada somente para a comparação. Não é uma aptidão publicada, não foi escolhida por Mizuki e não integra o Amontoado original.

**Trançar placas — proposta local.** Depois de determinar o dano de um ataque que o acertou, antes de descontá-lo, pode gastar **Reação e 2 PE** para reduzir esse dano em **4**, até zero. Protege somente a si mesmo, contra o dano desse ataque; não impede condições ou deslocamentos que dependam do acerto. Não protege de queda, dano contínuo ou feitiço resolvido por teste de resistência. A redução se aplica uma vez ao golpe inteiro, depois das resistências pertinentes. Se houver dano de Alma, a redução numérica aplicável entra antes de descontar vida e Integridade. Não altera Defesa ou Bloquear e não permanece para o ataque seguinte.

Trançar placas é uma capacidade própria deste ensaio, **não um feitiço**: o acréscimo por Classe do estágio 2 não altera seus dois PE. Exige uma Reação disponível; não funciona como uma defesa gratuita depois de gastar essa Reação com Aparar ou outra resposta. Não confere Cobrir-se de Energia, Refino, Canalizar em Golpe ou aptidões adicionais.

A R53 fundamenta o procedimento de Reação e Redução de Dano. O valor quatro e o preço dois são parâmetros deliberados para investigar custos distintos. Não se afirma que sejam um preço equilibrado. A reação publicada de Cobrir-se de Energia foi consultada, mas não importada pela metade: ela tem Refino e perda de proteção próprios.

| Variante | Regra do recurso |
|---|---|
| R — Reserva | Os mesmos 6 PE pagam Impacto, a 3, e Trançar placas, a 2. |
| U — Usos compartilhados | Duas ativações compartilhadas: gastar uma permite tentar Impacto **ou** usar Trançar placas. Cada capacidade conserva sua ação e seus requisitos. Substitui os dois pagamentos de PE; é uma adaptação experimental. |
| M — Reserva e intervalo | Mesmos 6 PE e preços de R; apenas Impacto recebe a pausa do protótipo 1. |

**A variante U também produz escolha.** Gastar uma ativação para se proteger reduz as disponíveis para Impacto. A diferença é que as duas capacidades passam a ter o mesmo preço em ativações. Duas cotas independentes, uma de ataques e outra de proteções, não preservariam essa disputa.

### Combinações possíveis

Em três ou mais turnos com oportunidades suficientes, sem alteração de Integridade ou recuperação, estas são as combinações máximas: não é possível acrescentar outra aplicação sem diminuir uma das quantidades. Não somar linhas da tabela.

| Escolha | R — 6 PE | U — duas ativações | M — 6 PE e intervalo |
|---|---|---|---|
| Priorizar ataque | 2 Impactos, nenhuma proteção | 2 Impactos, nenhuma proteção | 2 Impactos, separados pela pausa |
| Dividir a reserva | 1 Impacto e 1 proteção; sobra 1 PE | 1 Impacto e 1 proteção | 1 Impacto e 1 proteção; sobra 1 PE |
| Priorizar proteção | 3 proteções, nenhum Impacto | 2 proteções, nenhum Impacto | 3 proteções, nenhum Impacto |

Nos turnos sem Impacto ainda pode usar Pancada. Cada proteção exige um ataque recebido e uma Reação própria disponível. Três proteções não cabem numa única Reação, nem são três reduções sobre o mesmo golpe.

Com estágio 2 já ativo, R/M ainda permitem **um Impacto de quatro PE e uma proteção de dois**, ou **três proteções**. Dois Impactos não cabem. U, sem tradução, continuaria permitindo dois; preservar esse resultado seria uma mudança explícita da interação com Integridade.

### Duas decisões com o mesmo saldo

Depois do primeiro Impacto, restam três PE. Antes do próximo turno, um ataque acerta e causaria seis de dano comum, já calculados. Ele tem Reação disponível, Integridade acima do estágio 2 e nenhum outro dano ou ação neste recorte.

| Situação inicial | Se usar Trançar placas | Se guardar os três PE |
|---|---|---|
| Ainda tem 5 PV | Recebe 6 − 4 = 2; fica com 3 PV e 1 PE. Pode continuar vivo até seu próximo turno, se nada mais ocorrer, mas não paga outro Impacto. | Recebe 6; chega a zero e fica derrotado. Guardar PE não garante oportunidade de usá-los. |
| Ainda tem 20 PV | Fica com 18 PV e 1 PE. Compra quatro pontos de preservação, abrindo mão do próximo Impacto. | Fica com 14 PV e 3 PE. Conserva o próximo Impacto, se seus requisitos continuarem atendidos. |

O primeiro caso mostra uma proteção capaz de preservar participação; o segundo expõe uma escolha sem resposta universal. O objetivo do inimigo, o risco dos próximos ataques e a possibilidade de retirada importam. Não escrever “sempre gastar em defesa” como solução geral.

Para o grupo, forçar uma proteção pode abrir uma oportunidade ofensiva. Isso exige informação: observar a reação revela que a proteção existe, mas não revela automaticamente o saldo exato. Leitura de Reservas, quando usada com seus requisitos, pode fornecer esse saldo. O mestre não precisa entregar números por toda descrição visual.

## Integração das variantes iniciais com a R53

| Interação | Variantes com PE | Variantes que retiram PE |
|---|---|---|
| Leitura de Reservas | Informa saldo e máximo reais pelo procedimento publicado. | Informar “ativações restantes” ou “intensidade” seria outro resultado para a capacidade. Precisa de adaptação aprovada; não inventar um saldo no momento da leitura. |
| Integridade | Aplica o custo por Classe aos feitiços; não transforma toda capacidade em feitiço. | Definir uma tradução para cada economia adotada. Ignorar o aumento deixa uma diferença real. |
| Alteração de energia | Resolver a quantidade prevista pela capacidade efetivamente usada. | Dois usos não distinguem, por exemplo, 5 PE de 6. Uma correspondência aproximada mudará algumas possibilidades. |
| Manutenção | Só existe se uma capacidade da ficha a exigir; paga com saldo. Nenhum protótipo deste estudo possui manutenção. | Esta entrega não oferece conversão geral de manutenção. Não afirmar que as variantes já cobrem Domínios, barreiras ou técnicas sustentadas. |
| Doma | Usa a conversão própria da entidade, não herda automaticamente o orçamento de inimigo. | Ainda exige ficha e energia da entidade convertida. A variante experimental com Trançar placas não tem conversão pronta. |
| Retirada e reencontro | Conserva saldo e demais estados. | Conserva marcas; não ganha usos porque a cena mudou. |

**Exemplo condicional de alteração:** um efeito válido que retirasse dois PE de uma reserva de seis deixaria quatro; caberia um Impacto e sobraria um. Não existe neste estudo uma manobra genérica de “drenar dois PE”. O exemplo confere a necessidade de representar uma alteração pequena, se uma regra concreta a produzir.

Nos ensaios, nenhuma variante recebe recuperação. Recomeçar uma comparação independente com a ficha cheia é reiniciar o experimento, não uma regra de descanso. Na continuidade de uma mesma cena ou reencontro, conservar o estado. Para ensaiar retirada, manter a iniciativa: usar Impacto no turno 1, passar o turno 2 afastado e retornar no 3 permite que o intervalo termine, mas não devolve os três PE ou a ativação gastos. Uma recuperação posterior exigirá procedimento próprio antes de publicar essas variantes como fichas recorrentes completas.

## Variantes N: energia existente, especial sem gasto-base

Esta é a terceira direção que a pergunta anterior deixou de fora. **Ter energia não exige que toda aplicação custe PE.** Na R53, Canalizar Energia não cobra PE; Travessia por um fio é um exemplo de feitiço de Classe 0 com custo zero. Isso não autoriza tornar gratuito qualquer feitiço de outra Classe, nem prova que o Impacto esteja equilibrado sem seu custo.

Para examinar a diferença com o mínimo de outras mudanças, as duas variantes abaixo conservam a ficha simples com **6 PE atuais e máximos**, mas substituem experimentalmente o **custo-base do Impacto por zero e acrescentam um limite próprio**. Conservam Classe 1, Selo, ação, alcance, ataque e dano. É uma exceção nova de inimigo para este estudo; não uma montagem publicada, um desconto já aprovado ou uma alteração do Amontoado original. A mesma solução poderia ser inadequada a outro feitiço.

### N-R: retorno por recarga

O Impacto começa disponível. Depois de tentar, acertando ou errando, fica indisponível. No começo de cada turno próprio seguinte em que estiver indisponível, role um d6: **5 ou 6 o torna disponível**. O resultado não obriga a usá-lo naquele turno; se não usar, permanece disponível e dispensa novas rolagens até a próxima tentativa. Não acumula aplicações. A preparação habitual do Selo continua no instante da conjuração; não é um preparo interrompível com antecedência.

O custo-base é zero. Não há retorno por mudança de cena, nem reposição de PE pela recarga. Neste ensaio, não se acrescentam as regras de descanso de D&D; fora da iniciativa, conservar o estado até definir um procedimento próprio de continuidade. A comparação usa iniciativa contínua, inclusive no afastamento.

Com cinco oportunidades, uso imediato sempre que possível e sem interferência, pode tentar de **um a cinco Impactos**, com média **7/3, aproximadamente 2,33**. Pode voltar já no turno seguinte. A recarga substitui a contagem de gasto comum por uma marca de disponibilidade e possíveis rolagens, sem garantir pausa e sem preservar o total de dois usos.

### N-P: preparo que o grupo pode interromper

O Impacto começa sem preparo. Como **Ação Padrão**, o Amontoado firma as pernas e comprime as placas, produzindo um estalo audível. Fica preparado para tentar Impacto **a partir do começo do próximo turno próprio, até o fim desse turno**. Tentar consome o preparo, inclusive no erro. Sem tentar até o prazo, perde o preparo.

Este preparo é próprio do ensaio. **Não é a Restrição Carregar da R53 e não devolve pontos de montagem.** Carregar já oferece uma opção publicada: paga os PE no primeiro turno e exige TR Espírito ao sofrer dano durante a carga. N-P experimenta outra interrupção e cobra eventual PE apenas ao declarar o disparo, pelo custo vigente naquele instante, antes da rolagem. Não aplicar seu procedimento aos feitiços que possuem Carregar.

Mover-se voluntariamente, ser deslocado à força, ficar Derrubado, Inconsciente ou Derrotado encerra o preparo imediatamente. Receber dano, por si só, não o encerra. A declaração de preparo não impede essas consequências e não cria imunidade. Pode abrir mão do preparo para mover-se ou escolher outra ação normal. Um novo preparo exige outra Ação Padrão. Os dois braços continuam necessários para o Selo do Impacto.

**Exemplo.** Prepara no turno 1; depois os personagens agem. Se todos saírem do alcance de 1,5 m, ele não pode persegui-los conservando esse preparo. Se o deslocarem por uma capacidade válida, também terá de preparar novamente. Se ninguém impedir e houver alvo, pode tentar Impacto no turno 2. Não recebeu um turno extra: gastou sua Padrão anterior preparando.

Sem interferência, a sequência de cinco turnos é **preparar, Impacto, preparar, Impacto, preparar**: duas tentativas. Em oito turnos, cabem quatro. O mestre acompanha a existência e o vencimento do preparo; o grupo ganha uma possibilidade de resposta. Esse desenho pode ficar repetitivo ou permitir neutralização fácil; sua utilidade depende do espaço e do objetivo, e não foi validada em mesa.

O estado inicial sem preparo vale para este ensaio. Uma futura cena com preparo anterior precisa registrá-lo; não prometer uma janela de reação que o cenário já retirou. Estas variantes não se acumulam entre si nem com o intervalo de M.

### O que acontece com energia e Integridade

Nas variantes N, **Leitura de Reservas continua encontrando o saldo real**, que começa em 6/6 e permanece assim enquanto nada o altera. Isso não revela a recarga nem o preparo, e seis PE não significam seis usos ou determinada dificuldade. Não inventar uma reserva diferente na hora de responder à leitura.

O Impacto continua sendo de Classe 1. Portanto, no estágio 2 de Integridade seu preço é **0 + 1 = 1 PE por tentativa**. Uma perda válida de energia reduz o saldo normalmente; ela limita esse gasto quando ele existe. Com zero PE, não paga o acréscimo. Fora desse estágio, o custo-base zero não esvazia o saldo. O esgotamento não se transforma automaticamente em proibição de toda capacidade gratuita; a R53 distingue zero PE de uma rota sem energia.

Esse caso mostra uma forma de manter exatidão sem subtrair PE em cada uso comum. Também mostra uma consequência real: uma perda de PE influencia menos esse especial enquanto não houver custo. Precisamos avaliar isso, em vez de dizer que toda interação conserva o mesmo peso tático. Adotar uma habilidade corporal própria, em vez de feitiço, exigiria outra classificação e conferência das interações; não basta renomear Impacto para escapar dos custos.

Manutenção, recuperação fora da iniciativa, conversão por Doma e compatibilidade com alterações de feitiço não foram fechadas para N. São variantes controladas para comparar limites, não fichas prontas para circulação na guilda. Nenhuma concede especiais gratuitos às personagens.

## Trabalho de condução

As variantes R/U exigem uma reserva dinâmica; M acrescenta o retorno do golpe. Ter dois preços não cria dois saldos. Vida, Integridade, Reação, condições e posição continuam exigindo acompanhamento em todas elas. O intervalo não elimina esse trabalho.

U simplifica o pagamento e perde a diferença de preços; R conserva a diferença, mas exige subtração e atualização dos custos; M acrescenta uma pausa previsível e seu registro. O resumo de dois usos ajuda no caso normal de R, mas não permite apagar as informações necessárias quando a situação muda.

Não medimos segundos de condução nem preferência de mestres. A enumeração apenas identifica campos e mudanças de estado. Um formulário menor não prova uma experiência mais rápida, assim como um campo adicional não prova uma experiência pior.

Nas variantes N, a energia pode permanecer estática durante a cena comum. N-R troca subtrações por disponibilidade e rolagens; N-P exige lembrar preparo, prazo e interrupções. Portanto, retirar o gasto não elimina necessariamente o acompanhamento: muda o que ele permite fazer em jogo.

## Direção de trabalho após o esclarecimento

**Recomendo desenvolver limites por habilidade, com PE quando o gasto tiver uma função demonstrável.** Isso não exige adicionar recarga a todo inimigo, nem uma proteção energética artificial a toda ficha para justificar sua reserva. Um inimigo simples pode ter uma rotina simples. Um conjurador com opções concorrentes pode justificar preços e saldo. Um golpe que deve criar oportunidade de resposta pode justificar preparo.

| Resultado desejado | Primeiro caminho a examinar | Pergunta que pode fazê-lo falhar |
|---|---|---|
| Rotina sem administração extra | Uso livre, com efeito calibrado para repetição | A repetição transforma o efeito numa opção sempre superior às demais? |
| Limitar o total | Usos ou reserva finita | Gastar tudo cedo é adequado a essa criatura ou só esconde a ausência de escolhas? |
| Garantir pausa | Intervalo conhecido | A pausa produz oportunidade útil ou só um turno de espera sem função? |
| Retorno incerto | Recarga | A variação extrema é aceitável? O grupo foi levado a esperar uma pausa que não é garantida? |
| Permitir interferência | Preparo ou condição visível | Há tempo e meios reais de responder, sem uma solução única obrigatória? |
| Disputar ataque, defesa ou outra função | Reserva compartilhada, possivelmente PE | As alternativas são úteis em situações distintas ou uma sempre vence? |

A próxima proposta deverá distinguir **feitiço da R53 conservado**, **adaptação expressa para inimigo** e **habilidade própria**, com limites e interações identificados. Só então propor onde PE entram e quanto atribuir. Esta entrega não escolhe reservas por nível, aprova a reação de quatro pontos, decide custo-base zero ou conclui a atualização do Bestiário.

Não repetir agora a pergunta binária anterior. O esclarecimento de Mizuki orienta o problema; não aprova automaticamente uma solução. Enquanto os critérios são desenvolvidos, exemplos ambientais de C04 também podem avançar sem depender de uma economia universal de inimigos.

## Fontes e conferência

R53: Turnos, Ataques, Bloquear/Aparar, Redução de Dano, Dano na alma, Integridade, derrota dos inimigos, Leitura de Reservas, Cobrir-se de Energia, Canalizar Energia, zero PE, Travessia por um fio e Carregar. Amontoado: registro 14 e dados da base. Fundamento comparado externo: [registro 63](63-reservas-usos-e-ritmo-dos-inimigos.md), com URLs e escopo das consultas. As páginas de D&D e GM Core foram reabertas nesta etapa. Este estudo não acrescenta afirmações de cânone nem números de dano de outros jogos; d6 5–6 é referência experimental identificada.

Revisão de clareza e método:

| Antes, na discussão | Depois, nesta entrega | Problema corrigido |
|---|---|---|
| Escolher entre PE exatos e retirar a reserva. | Distinguir possuir energia, pagar a capacidade e controlar seu retorno. | A pergunta excluía habilidades sem gasto que coexistem com energia. |
| Recomendar PE primeiro pela integração. | Examinar a função do limite e depois conferir integração. | Compatibilidade recebia peso de prova de utilidade. |
| Usar “recarga” como alternativa suficiente a gastar cedo. | Mostrar que recarga organiza retorno e pode incentivar uso imediato. | Confundia repetição controlada com decisão de esperar. |
| Descrever somente uma ameaça com reserva. | Comparar rotinas completas e uma defesa concorrente, com custos e resultados visíveis. | Faltava mostrar a decisão no próprio combate. |

[Conferência reproduzível](apoio-prototipos-inimigos/comparar_recursos.py) e [resultados](apoio-prototipos-inimigos/resultados.json): disponibilidade por horizonte, combinações possíveis com e sem estágio 2, continuidade e casos de sobrevivência. Não modelam ataques dos jogadores, trajetórias de dano ou decisões de encontro completo. [Texto didático 59](<../06 - Redacao do Guia/59-recursos-e-ritmo-dos-inimigos.md>) apresenta as conclusões como critérios, sem inserir as variantes sem PE como regras prontas.

**Próxima tarefa:** desenvolver critérios de habilidades de inimigos e sua integração com a R53, escolhendo limites pela função antes das reservas por nível. **GPT-6 Astra, esforço extra alto**, para conferir interações; **GPT-6.1 Sol, alto**, para a prosa. Esforços são recomendações deste projeto, não mudança automática de modelo.
