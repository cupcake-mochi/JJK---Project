# Detecção comum de energia — auditoria mecânica

Leitura de 03/10/2026. Base integrada v0.331, candidata lote 03 revisão 2 e candidata lote 04. Nenhuma fonte do projeto foi alterada. Este parecer verifica dependências e propõe limites; não afirma que a futura regra foi aprovada ou testada em mesa.

Raiz das referências: `/media/mizuki/HD Externo II/Claude/Claude 2/`.

Abreviações usadas abaixo:

- **M**: `sistema/05-material/livro/manual/`.
- **P**: `sistema/03-mecanica/`.
- **L03**: `sistema/05-material/livro/planejamento-editorial/regras-comuns/lote-03/03-PERCEPCAO-E-FURTIVIDADE.md`.
- **L04**: `sistema/05-material/livro/planejamento-editorial/regras-comuns/lote-04/04-MANOBRAS-E-INFORMACAO.md`.

## 1. Conclusão

É viável acrescentar uma busca energética local, ativa e limitada. A opção mais controlável é **Ação Padrão, um lugar declarado, um teste de Sentir Energia e resultado de posição atual**, sem enxergar, sem revelar ficha e sem atravessar obstrução sólida para obter coordenadas. Isso precisa ser apresentado como regra nova: os donos atuais oferecem aplicações e exemplos, mas não publicam um procedimento comum completo de alcance, custo, oposição e precisão.

Separar isso de uma **pressão energética percebida na cena**, que avisa presença ou direção aproximada, acomoda a fantasia já prometida pelo livro. A pressão não deve ser uma segunda ação de varredura, um detector passivo obrigatório ou uma fonte de coordenadas por triangulação de testes repetidos.

Um alcance fixo para a **localização ativa** é preferível a depender inteiramente de “sinal acessível” em mesa com vários mestres. O número ainda é decisão de design. A pressão de cena pode permanecer sem raio universal, desde que o mestre a prepare como parte das condições da cena e não mude sua existência para favorecer um resultado. Alvos comparáveis precisam receber o mesmo tratamento.

Há duas decisões que não podem ficar implícitas: **Furtividade passa a contestar localização energética?** E **um sucesso apenas informa o espaço naquele instante ou acompanha movimento?** A primeira deve ser afirmada para impedir que todo feiticeiro anule o Assassino gratuitamente; para a segunda, recomendo informação atual, seguida pelas regras de sinais e último espaço conhecido, sem rastreamento autônomo.

## 2. Donos e benefícios a preservar

| Regra ou habilidade | Fonte exata | O que efetivamente entrega / limite encontrado |
|---|---|---|
| Teste de perícia | M12-pericias-e-oficios.md:21–29, 56, 70–71 | d20 + atributo, maestria se treinado; Furtividade usa Destreza; Sentir Energia e Percepção usam Essência. Treino não é requisito geral para tentar Sentir Energia. |
| Sentir Energia | M12:136, 154–160; P07-pericias-e-oficios.md:103, 111–117 | Perceber feiticeiro escondido, dimensão/intensidade de maldição e sinais de energia antes de conjurar; ler seu fluxo. Não publica alcance comum, coordenadas por parede, detecção infalível ou ficha completa. |
| Escolha de treino | P07:195 | Sentir Energia deliberadamente não é perícia fixa de Caminho: deve existir o feiticeiro que não é bom nela. Detector universal automático contraria essa escolha. |
| Furtividade vigente | M12:104 | Mover-se sem ser visto nem ouvido. Não há nessa definição um procedimento explícito de suprimir aura. A ponte com energia é decisão nova, não mera correção de redação. |
| Esconder candidato | L03:35–62 | Uma rolagem com bônus completo; CD passiva 10 + Percepção do observador; resultado guardado para buscas. Não acrescenta Sentir Energia como segunda defesa passiva. |
| Vasculhar candidato | L03:67–77 | Padrão, declarar lugar, uma rolagem contra resultados guardados acessíveis; localizar encerra ocultação para aquele observador. Repetição idêntica fora de combate precisa de nova abordagem/informação/consequência; CD inalcançável pede outra solução. |
| Energia ainda pendente | L03:79–87 | Retira o radar universal de 9 m da revisão anterior. Distingue detectar presença, localizar e enxergar. O alcance e o resultado da detecção comum permanecem em aberto. |
| Vulto | M47-bencaos-e-lapidacao.md:185–189; P11-aptidoes-e-refino.md:1095; L03:29, 83, 100 | Classe Passiva 2; visão às cegas por som e movimento, raio `1,5 m × metade da Lapidação`. A candidata reconhece percepção/ataque por esse sentido, sem leitura fina, visão por paredes ou dispensa de Selos especificamente oculares. |
| Rastro | M40-fundamento.md:769–780; reprodução em M60-invocacoes.md:364 | Melhoria Leve de Marca: posição do alvo por 1 hora no mesmo plano. Não depende de nova busca por cômodo e não se limita ao raio local de uma perícia. Não concede olhos. |
| Sem Ver | M40:595–606; M60:253 | Melhoria Pesada: conjurar contra alvo fora da linha de visão se souber onde está; respeita alcance normal. Localização comum não deve entregar a permissão de conjurar sem visão. |
| Escada de alcance | M40:520–526 | O último degrau “o que você enxergar” exige olho nu; câmera, luneta, espelho e visão emprestada não contam. Sentir Energia não estende esse degrau. |
| Faro — Legado | M25-origens.md:419–420; P13-legados.md:896 | Uma vez por cena, ao procurar maldição, substitui Investigação por Sentir Energia. Exemplo aponta o andar e evita vasculhar três andares. Não é autorização geral para todos usarem Sentir Energia em qualquer investigação. |
| Faro — Bênção | M47:167–173; P11:1125–1127 | Classe Passiva 1; segue rastros físicos de feiticeiro/maldição. Tocando vestígio, sabe superficialmente o que a técnica fez ali, sem detalhes nem autoria. P11 afirma que não revela a posição atual. |
| Sem Pegada | M47:175–181; P11:1129–1132 | Classe Passiva 1; elimina pegada, cheiro, marca e som de passo; nem Faro, cão ou técnica de rastreamento acham por onde passou. Não é bônus de Furtividade nem apaga testemunha. |
| Antena | M25:653–654; P13:959 | Uma vez por cena, rerrola Sentir Energia após falha. Exemplo integrado ocorre do outro lado de uma parede; a peça menciona alcance excepcional, mas não quantifica. Mecânica comprada é rerrolagem, não um raio publicado. |
| Sentido Treinado | M25:687–688; P13:993 | Uma vez por cena, Percepção substitui Sentir Energia, percebendo efeitos físicos como poeira movida. Não concede a perícia proibida nem torna a substituição permanente. |
| Presságio | M55-ferramenta-amaldicoada.md:139–153; P16-ferramenta-amaldicoada.md:224–227 | Estigma Classe 1, grau 3, sem nível mínimo: avisa que há maldição perto antes de ver. Não fornece raio numérico, identidade, número de inimigos ou espaço. Foi concebido também para quem não pode ter Sentir Energia. |
| Aferido | M55:151 | Ao tocar maldição, informa grau. Uma busca energética que informe automaticamente o grau de qualquer alvo à distância esvazia esse benefício. |
| Máscara | M25:205–208 | Quem sente a energia do receptáculo sente a da entidade; troca leitura/identidade, não ausência de energia. O exemplo de atravessar Cortina “sem acender nada” é mais amplo que a regra. |
| Restrição sem energia | M12:89; M25:604, 618, 667; P09-origens.md:199, 208 | Não pode ter Sentir Energia. O PE dessa rota é esforço, não emissão de energia. Não confundir essa Origem com um feiticeiro que gastou seus PE. |
| Equipamento do Sem Energia | M47:94–107 | Corpo passa por Barreira Simples/Cortina; item amaldiçoado emite e pode ser detectado/barrado. Equipamento não transforma o corpo em alvo legível pelo Acerto garantido. |
| Maldição do Inventário | M42-tecnica-marcial.md:139–151 | Item guardado para de emanar; por isso atravessa com o usuário. Tratar mochila, caixa comum ou corpo como bloqueador absoluto de emissão copiaria a vantagem dessa Passiva. Impedir a localização precisa por um obstáculo não é o mesmo que suprimir emissão; definir essa distinção evita que roupas, bainhas e bagagens comuns se tornem invisibilidade energética gratuita. |
| Peso Real | M25:703–704 | Percebe ferramenta, barreira e véu pelo tato/peso; recebe aviso sem identificação. A detecção básica não deve dar isso a quem não sente energia. |
| Sobrevivência | M12:126; P07:98 | Já segue rastros, inclusive resíduo de energia. A busca por uma presença atual não deve absorver toda perseguição ou substituir a perícia. |
| Aptidão Própria de vestígios | M45-aptidoes-e-refino.md:399–406 | Exemplo aprovado de Classe Passiva 1: saber se objeto foi tocado por energia nas últimas 24h. Um teste comum não deve conceder exatamente esse diagnóstico garantido por padrão. |
| Silencioso | M40:750; L03:112 | Usar o feitiço não revela a posição e não exige sinal; percepção do efeito não revela automaticamente a origem. Busca independente pode localizar. “Todo gasto de PE revela o conjurador” destruiria essa compra. |
| Invocações e informação | M60:79, 629–659 | Entidade tem sentidos próprios; intenção não revela alvo escondido; não há telepatia, sentidos compartilhados ou conhecimento automático. Comunicar uma localização não concede visão do invocador. |

## 3. Lacunas e tensões já existentes

### A. Alcance e paredes

M45:13–15 diz que energia vaza, que se fareja um feiticeiro a um quarteirão e que Refino alto controla o vazamento. É apresentação ficcional sem custo, CD, distância exata ou tabela de supressão. Não autoriza somar Refino em Furtividade nem declarar invisibilidade energética em Refino 10.

Antena e Faro oferecem exemplos de informação além de uma parede/andar. A candidata pode limitar **posição exata** sem proibir a **percepção ampla de energia**. É preciso registrar na futura tabela de integração que os exemplos antigos passarão a exemplificar presença/direção ou benefício específico, e não detecção universal de coordenadas. Proibir toda informação por parede, com qualquer habilidade, seria uma alteração maior.

### B. Furtividade contra energia

O texto integrado só menciona visão e audição; a candidata fala em disfarçar sinais, mas guarda CD somente contra Percepção. Uma regra de energia sem oposição adequada descobre automaticamente praticamente qualquer feiticeiro escondido. Uma regra que peça Furtividade **e** controle/refino cria dois obstáculos e enfraquece a especialização existente.

Recomendação candidata: manter **a mesma rolagem de Furtividade guardada** como CD da tentativa de localizar energia. Não criar passiva `10 + Sentir Energia` adicional para cada observador. Não somar Refino à CD, não cobrar outra ação para “esconder aura”, não interpretar sucesso como deixar de emitir para barreiras e efeitos que não usam esse teste.

Isso é uma escolha de design a declarar. A justificativa é manter uma disputa única de localizar a criatura, e não afirmar que Destreza remove energia do corpo.

### C. Barreira e detecção não são sinônimos

**Barreira Simples**, M45:338–346, bloqueia passagem e linha de efeito nos dois sentidos; tem raio 6 m. **Cortina**, M45:348–364, esconde o interior de quem não é feiticeiro e impõe condição de travessia. A tabela expressamente proíbe usar a Cortina para esconder o interior de feiticeiros.

Não há procedimento publicado que transforme toda barreira em detector com mapa ao vivo do interior. “A barreira lê energia para permitir passagem” não equivale a “seu criador sabe a posição de todos”. Também não há regra comum completa que diga se toda barreira bloqueia todo sinal energético.

Consequência para a candidata: obstáculos sólidos podem impedir localização precisa; **não escrever “toda barreira impede sentir energia”**. O efeito específico pode bloquear passagem, ocultar, mascarar ou impedir detecção, e deve produzir somente o que diz. Cortina comum não recebe ocultação energética contra feiticeiros por associação de nome.

### D. Máscara não é passe universal

O bloco formal substitui a assinatura percebida. O exemplo seguinte sugere atravessar Cortina sem alerta. Pela própria lista de Cortina, isso só é coerente quando a condição depende de uma assinatura/identidade que a Máscara realmente substitui. Uma barreira que barra qualquer energia continuaria encontrando energia; uma condição nominativa pode depender de como foi escrita.

A detecção básica não deve negar Máscara com um sucesso normal, nem transformar Máscara em ausência universal de assinatura. Registrar a ambiguidade do exemplo para correção explícita, sem redefinir todas as Cortinas nesta unidade.

### E. Sem Pegada e Rastro

“Técnica de rastreamento não acha por onde passou” pode ser lido de forma ampla. O objeto de Sem Pegada é o vestígio da passagem; Rastro é uma marca aplicada ao próprio alvo que informa sua posição. Não encontrei cláusula dizendo que Sem Pegada desfaz a marca Rastro.

Recomendação de leitura a explicitar: apagar vestígios não remove uma marca existente. Se o projeto quiser que Sem Pegada desligue Rastro também, será uma mudança de interação, não uma conclusão já garantida pelo texto. Não usar a nova busca comum para decidir isso silenciosamente.

### F. Sentido Treinado pode ficar sem função

Percepção já pode achar alguém por poeira, som e movimento. Se o único teste novo de energia exigir exatamente os mesmos sinais físicos, a substituição por cena tende a não acrescentar nada. Por outro lado, conceder gratuitamente leitura de aura a toda Percepção elimina o Legado.

A nova ação deve permitir informação **especificamente energética** para que Sentido Treinado abra acesso limitado a ela por indícios físicos. Seu exemplo sustenta o uso de sinais físicos; não sustenta atravessar parede sem qualquer consequência física acessível. Caso a cena só entregue uma pressão que exclusivamente a energia percebe, deixar claro se esse Legado pode traduzi-la em indício disponível; isso é uma escolha necessária de compatibilidade.

### G. Estudar continua diferente de encontrar

M11-o-turno.md:75–76 e 104–106 têm conflito antigo entre tabela, assunto e distância. L03/L04 resolvem por função: Vasculhar procura, Estudar compreende, Ler o Ambiente fala do lugar. L04:79 exige criatura/objeto enxergado; 88 afirma que localizar é necessário, mas não diz que basta.

Uma presença sentida por parede não dá autorização automática para Estudar sua técnica. A busca encontra ou indica; a análise exige os sinais observáveis e a ação apropriada. Se quiser permitir estudar uma manifestação energética percebida sem visão, registrar essa ampliação expressamente em L04; não mudar o sentido de “enxergar” para todas as habilidades.

## 4. Restrições simples recomendadas para a próxima candidata

1. **Duas saídas claras, sem novas condições na ficha.** Pressão de cena: existe energia relevante naquela direção/região. Busca local: espaço atual da fonte encontrada. Nenhuma equivale a visão.
2. **Busca dentro de um alcance fixo e em um lugar escolhido**, com Padrão em combate. O alcance limita distância; não permite atravessar qualquer quantidade de cômodos ou procurar toda a construção. “Mesmo cômodo” sozinho não basta: galpão enorme e corredor dobrado mostram o problema.
3. **Um teste e um bônus completo.** Use a regra normal da perícia e a mesma CD guardada de Furtividade para alvos escondidos; sem segunda passiva, sem bônus gratuito de Refino. Definir em separado a dificuldade de fontes discretas que não fizeram Furtividade.
4. **Informação suficiente para a ação, sem diagnóstico total.** Localização não informa automaticamente nome, aliado/inimigo, grau exato, PE restante, intenções, Fundamento, lista de melhorias, autoria do vestígio ou todos os portadores numa sala lotada.
5. **Obstrução impede coordenada, não prova ausência.** Falha, sinal mascarado, obstáculo ou fonte fora de alcance não permitem concluir “não há ninguém”. Uma eventual pressão percebida através de parede é aproximação, sem contagem nem espaço atacável.
6. **Sem repetição para triangular gratuitamente.** Avisos de pressão não formam um mapa métrico; várias posições e rerrolagens não convertem a informação ampla em posição exata à margem do procedimento. Antena permite refazer a tentativa permitida, não mudar sua modalidade ou seu alcance.
7. **Sem rastreamento autônomo.** O sucesso informa a posição de agora; o aviso a aliado também. Movimento posterior escondido, perda de acesso ao sinal e novo Esconder exigem aplicar as regras de ocultação/busca. Não entregar uma hora de acompanhamento como Rastro.
8. **Efeitos específicos conservam suas permissões.** Rastro, Vulto, Faro, Presságio, Máscara, Maldição do Inventário e sentidos de entidade não recebem o teto da perícia por acidente. Ao mesmo tempo, “sentido especial” não é autorização genérica para ignorar cobertura e exigências de visão.
9. **Pressão é informação preparada de cena.** Um efeito excepcional ou manifestação forte pode ser notado sem ação, quando evidente. Um inimigo ordinário não emite obrigatoriamente um aviso antes de toda emboscada. A ficha sem Sentir Energia não recebe o aviso energético comum automaticamente; Presságio e Sentido Treinado precisam continuar tendo trabalho.

## 5. Casos adversariais mínimos

| Caso | Resultado que a regra precisa sustentar |
|---|---|
| Feiticeiro oculto na fumaça, Furtividade 17, observador Sentir Energia +4 tira 13 | Se a nova modalidade permitir busca local nessa situação, total 17 localiza; não concede visão. O ataque comum continua com desvantagem por não enxergar, e Sem Ver continua necessário quando exigido. |
| Mesmo alvo, observador tira 12 | Total 16 falha; ação gasta. Não revela que a CD era 17 nem prova ausência de energia. Antena pode rerrolar conforme seu uso por cena. |
| Furtividade guardada 27 contra Sentir Energia +4 | Máximo normal 24: teste idêntico é insuficiente. Não acrescentar sucesso automático em 20 nem CD máxima 20 para acomodar a situação. Buscar pista, expor esconderijo ou usar efeito específico. |
| Incursor/Assassino consegue Esconder; todos os inimigos têm energia | Não sofre uma segunda rodada passiva de testes só por emitir energia. Localização ativa dos inimigos custa a ação definida. A oportunidade de abate continua verificável. |
| Alvo do outro lado de parede, dentro do raio numérico | Raio não basta para fornecer espaço exato. Pressão pode indicar presença/direção quando prevista; não habilita escolher alvo por coordenada. Antena pode repetir a leitura permitida, não remover parede. |
| Alvo do outro lado de uma porta aberta, com caminho livre; observador não o vê por escuridão | A candidata deve dizer se esse sinal é acessível para localização. Este caso diferencia “precisa ver” de “precisa ter acesso”: exigir visão tornaria a nova busca muito redundante. |
| Duas presenças por parede, uma arma deixada numa sala vazia e uma maldição | Aviso de energia não promete contagem, criatura viva, identidade ou hostilidade. Uma arma pode explicar um sinal sem revelar quem a carregava. |
| Usuário se desloca três vezes para triangular a pressão atrás de parede | Continua sem posição precisa se não cumpriu a busca válida ou um efeito específico. Evitar scanner grátis disfarçado de narrativa. |
| Malabarista recebe só “há algo naquele prédio” | Não possui alvo localizado para Ricochete. Com posição obtida legalmente, ainda precisa trajetória desobstruída, alcance e demais requisitos, conforme M35:2832–2844. |
| Assassino sente uma criatura sem enxergá-la | Não pode designar novo Alvo Estudado: M35:2455–2457 exige ver a até 18 m. A energia não reescreve o requisito. |
| Rastro já aplicado; alvo se afasta por salas e atravessa corredor escuro | Continua entregando a posição durante 1h/no mesmo plano conforme a Melhoria, sem buscas locais repetidas. Não permite lançar feitiço comum sem Sem Ver nem atravessar parede com ataque. |
| Vulto dentro/fora do próprio raio | Dentro, conserva visão às cegas; fora, não. A busca de energia não adquire seu tratamento favorável de Cego nem substitui o raio de Vulto. |
| Sem Energia com ferramenta amaldiçoada exposta / guardada no Inventário | A fonte detectável é a ferramenta exposta; o corpo não ganha aura. Inventário para a emissão conforme seu texto. Bolsa comum não ganha essa supressão por analogia. |
| Feiticeiro com PE atual zero / Corpo Amaldiçoado / personagem Sem Técnica | Zero PE não é Origem Sem Energia. Corpo Amaldiçoado tem energia (P09:181); Sem Técnica manipula energia (M43:21; P13:1088). Não classificar alvo apenas pelo nome da rota ou reserva atual. |
| Sem Pegada passando na frente de testemunha / deixando vestígio / já marcado por Rastro | Testemunha continua vendo; o vestígio físico descrito não aparece. Interação com marca deve ser declarada, não inventada a partir de “sem rastro”. |
| Faro Legado usado ao buscar maldição entre andares | A substituição de Investigação 1/cena continua superior à busca local comum naquela investigação; não é transformada em leitura do mesmo cômodo disponível a todos. |
| Faro Bênção toca vestígio; usuário comum tenta o mesmo | A Bênção recebe seu conhecimento superficial. A perícia comum não entrega por padrão o diagnóstico garantido, autoria e localização do conjurador. Sobrevivência ainda pode seguir resíduo conforme sua função. |
| Presságio avisa antes de a criatura aparecer | Aviso permanece disponível conforme o Estigma, sem exigir que seu portador tenha Sentir Energia ou gaste Padrão. Não fornece coordenadas. |
| Máscara diante de barreira que reage a energia / identidade específica | Energia continua presente; a identidade lida pode mudar. Não prometer que qualquer condição de Cortina falha. Corrigir o exemplo amplo na integração. |
| Cortina comum com feiticeiro fora e inimigo dentro | Não esconder de feiticeiro por regra genérica nova. Tampouco entregar ao dono da Cortina mapa de quem está dentro. Examinar a função específica da barreira. |
| Conjuração Silenciosa durante ocultação | Perceber o efeito não aponta automaticamente a fonte. Uma busca independente válida pode encontrá-la; gasto de PE não se torna revelação obrigatória. |
| Sentido Treinado num corredor com poeira perturbada / atrás de parede hermética sem indício | No primeiro, pode substituir a perícia 1/cena. No segundo, a candidata precisa explicitar o limite e não conceder visão energética permanente pelo Legado. |
| Entidade fareja alvo, invocador está do outro lado do obstáculo | Entidade sabe o que seus sentidos permitem; invocador só recebe o que foi comunicado. Informação recebida não concede visão, domínio dos sentidos ou alcance ilimitado do vínculo. |
| Pedido “quero saber qual feitiço ele lançará, sua CD e quanto PE tem” | Detectar não revela ficha nem futuro. Estudar pode obter uma informação sustentada pelos sinais; Aviso (M40:784) e previsões de Trilha conservam seus benefícios específicos. |

## 6. Decisões que precisam constar antes de considerar a candidata fechada

- Alcance local final, origem da medida e necessidade de lugar/percurso acessível. Nenhum número atual pode ser chamado de restauração do texto integrado.
- Se o limite de obstrução é para posição precisa, como recomendado, quais tipos de efeito ocultam também a pressão; Cortina não deve ganhar isso automaticamente.
- Confirmação explícita de que a Furtividade guardada contesta localização energética, preservando ação e teste únicos.
- Resultado para uma fonte discreta sem Furtividade: quando é evidente e quando usa CD da tarefa/efeito, sem inventar rolagem retroativa em todo objeto.
- Precisão suficiente para múltiplas fontes: localizar as acessíveis comparadas pela mesma busca não implica identificar/classificar tudo.
- Duração da informação e como novo deslocamento escondido/novo Esconder voltam a exigir busca.
- Compatibilidade de Sentido Treinado com a modalidade energética e com informações de pressão sem sinais físicos.
- Registro visível de revisão dos exemplos de Antena, Faro, Refino e Máscara. Se preservar as habilidades formais e apenas esclarecer seus exemplos, diga isso; não afirme que os exemplos antigos já continham o novo procedimento.

Essas escolhas bastam para a unidade. Não é necessário definir agora um catálogo de espessuras de parede, níveis de emissão por ponto de PE, dezenas de CDs ambientais, identificação universal de assinaturas ou uma nova reserva para sentir energia.

## 7. Limites da auditoria

Foram lidos os trechos integrados e candidatos indicados, incluindo as dependências adicionais encontradas. Não foram executados validadores históricos, renderizações ou testes de mesa; não foi revisado todo o catálogo de Fundamentos próprios. Os casos acima são critérios de aceitação e contraexemplos para a próxima minuta, não uma certificação de uma regra ainda inexistente.

## 8. Identificação das principais fontes lidas

SHA-256 ao concluir a leitura; servem para identificar estas versões, não para provar uma auditoria global.

- `sistema/05-material/livro/manual/12-pericias-e-oficios.md`: `62f41d5d4ca7abe451eac31264c6a7ead7f3993a8218cede144f2b79c28e98ca`
- `sistema/05-material/livro/manual/25-origens.md`: `dac3ae94462e81858c3d7758b938dd5de71870175f811ed1c3b8f341018ac59e`
- `sistema/05-material/livro/manual/40-fundamento.md`: `8ec6cd54f8fbb0cc7e98874a5242890a3b3392a792ec1cdef959abcec4b70d96`
- `sistema/05-material/livro/manual/42-tecnica-marcial.md`: `d3dcdd307d4542219d8f279a6f7f32da04ae4edc953872e312a4e410911042e5`
- `sistema/05-material/livro/manual/45-aptidoes-e-refino.md`: `8cde6375fbe213fb3ee23cd62ff3fb94660fa90b9c4bec5013dd2d4ef66e6be2`
- `sistema/05-material/livro/manual/47-bencaos-e-lapidacao.md`: `c400089ab383f8368f66801f4a6004092929a26c3dba2f76ea9af90c8bce446d`
- `sistema/05-material/livro/manual/55-ferramenta-amaldicoada.md`: `4e25e19f0c616769cfc93fd5f6a7d4eae1775e119aa10b5b3fe519366c6bd702`
- `sistema/05-material/livro/manual/60-invocacoes.md`: `4df82e672d063b4d4bfe3394d93bb75052ec3e07d44d90b83c0ea32f10439f82`
- `sistema/05-material/livro/planejamento-editorial/regras-comuns/lote-03/03-PERCEPCAO-E-FURTIVIDADE.md`: `55cb314a5bd0d420a3be0f8fcdb77ccbe27628604242573288a99a2a4e1ea02b`
- `sistema/05-material/livro/planejamento-editorial/regras-comuns/lote-04/04-MANOBRAS-E-INFORMACAO.md`: `1ea15259408bc967d24476b594f272b406f37b5a72d1585308b2a3558d7a7c80`
