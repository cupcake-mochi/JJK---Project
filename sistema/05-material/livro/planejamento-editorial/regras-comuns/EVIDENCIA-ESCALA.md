# Critérios para movimento, salto e queda — análise independente

Base consultada: Projeto - M v0.331. Escopo: fontes internas, contas de escala e critérios para formular uma regra comum; nenhuma mudança aplicada, nenhum valor final proposto. Não foi executado git. A pesquisa externa fica com o autor da proposta.

Raiz dos caminhos: `/media/mizuki/HD Externo II/Claude/Claude 2/`.

## 1. O que a nova regra precisa preservar

A regra deve permitir que dois mestres resolvam o mesmo vão, parede e desnível com os mesmos requisitos básicos. A decisão do mestre continua importante para circunstâncias visíveis — piso solto, vento, ausência de apoio —, mas o jogador precisa saber o risco antes de gastar movimento ou saltar.

As fontes atuais já fixam elementos que limitam o desenho:

| Base vigente | Implicação para a proposta | Fonte |
|---|---|---|
| Atributo é o próprio modificador, de 0 a 6. Na criação, o atributo comum chega a 3. | Uma fórmula copiada que espera valores de Força como 10 ou 18 não se transfere diretamente. Força 0 também precisa de uma resposta jogável. | `sistema/03-mecanica/01-atributos-acerto-defesa.md`, §§2–3; `manual/20-criacao-de-personagem.md`, distribuição inicial. |
| Perícia = d20 + atributo, somando maestria se treinado; maestria 1 a 4. | O teste do especialista cresce aproximadamente de +4 a +10. Não cabe uma escala de distâncias/CDs que exija bônus de outro sistema. | `manual/10-como-jogar.md`, Perícias, Atributos e Maestria. |
| Escada fixa: CD 6, 10, 14, 18, 22 e 26. Portas, muros, rios e quedas usam essa escada. | O mesmo vão permanece igual quando o personagem sobe de nível. A CD de quem empurrou alguém não deve automaticamente substituir a dificuldade física de aterrissar no mesmo chão. | `sistema/03-mecanica/04-pericias-e-testes.md`, §§2.1–2.3. |
| Movimento básico 9 m; pode ser dividido. Correr acrescenta o próprio deslocamento. | Salto e escalada precisam dizer como descontam a distância. Um teste bem-sucedido não deve criar metros disponíveis. | `manual/11-o-turno.md`, Recursos, Deslocamento e Correr. |
| Atletismo/Força inclui saltar, escalar e nadar. Acrobacia/Destreza inclui equilíbrio e cair sem se machucar. | O procedimento comum pode separar alcançar de aterrissar. Dar livre escolha entre os dois em todos os saltos esvaziaria uma entrega do Assassino. | `manual/12-pericias-e-oficios.md`, Força e Destreza. |
| Incursor: +3 m, até metade do deslocamento em paredes/espaços de criaturas; exige apoio final e conserva riscos. | A regra comum precisa deixar valor para percorrer uma parede durante combate. | `caminhos/05-Edicao-Integrada/06-Incursor-Caminho-e-Trilhas.md`, Movimento Acrobático. |
| Assassino troca Atletismo por Acrobacia nos testes de Parkour; termina pendurado com uma mão ocupada; pode usar a vítima como apoio após acertar. | Uma regra nova não deve anular esses benefícios por exigir Força alta em uma etapa que precede o teste. Também não deve conceder essas permissões inteiras gratuitamente a todos. | Mesmo arquivo, Parkour, linhas 220–259. |
| Yumi de nível 2 recebe deslocamento de escalada igual ao normal. | A escalada comum precisa ser distinguível desse benefício. Isso pode envolver custo de movimento e condições para escalar, sem tornar toda parede um teste obrigatório. | `caminhos/05-Edicao-Integrada/02-Vanguarda-Caminho-e-Trilhas.md`, Soltura Preparada, linha 220. |
| Pugilista de nível 11 atravessa líquidos dentro do limite de Movimento Acrobático; termina com apoio. Nível 23 amplia o limite. | Uma corrida comum não pode atravessar água por mera descrição acrobática. A habilidade também não dá apoio permanente ou proteção contra o líquido. | Incursor integrado, Movimento sobre líquidos e Movimento Acrobático ampliado. |

O catálogo de equipamento menciona corda e kit de escalada, mas essa menção não fornece sozinha distância, velocidade, CD ou proteção numérica contra queda. A proposta deve dizer qual ajuda prática eles oferecem ou manter esse ponto claramente pendente.

## 2. Salto fixo ligado à Força e salto por teste

| Modelo | O que oferece | Risco de desenho | Condições para funcionar no Projeto |
|---|---|---|---|
| **Distância automática calculada pela Força** | Consulta rápida; torna a Força útil fora do ataque; permite planejar rotas sem várias rolagens. | Força 0 pode virar incapacidade de atravessar qualquer vão; um teto absoluto por Força pode prejudicar o Assassino de Destreza, apesar da troca de perícia. O treino e a maestria podem deixar de importar. | Definir piso funcional, diferença entre distância horizontal e altura, movimento gasto e tratamento de distâncias além da base. Se houver teste para superar a base, a troca do Parkour precisa continuar efetiva. |
| **CD por distância pretendida** | Permite que treino, atributo e nível melhorem alcance; a mesma tabela vale para todos os mestres; a troca Atletismo→Acrobacia atua diretamente. | Torna um salto curto uma loteria se tudo exigir teste; tabelas muito detalhadas atrasam a sessão; repetir tentativas sem custo garante sucesso quando nada acontece na falha. | Separar travessia segura de tentativa arriscada; poucas faixas, CD declarada antes da tentativa; consequência verificável e sem teste para situações triviais sem pressão. |
| **Base automática + teste para extensão ou circunstância adversa** | Permite rotina rápida e esforço excepcional; mantém tanto Força quanto perícia relevantes. | Pode cobrar duas vezes o atributo: distância máxima pela Força mais CD alta, tornando Acrobacia pouco útil. Pode ficar complexo se tiver simultaneamente multiplicador de corrida, altura, peso, velocidade e margem de sucesso. | Uma única pergunta por tentativa; extensão realmente acessível pelo teste; poucos modificadores públicos. O exemplo do Assassino com Força baixa deve ser testado antes da escolha de valores. |

A comparação favorece testar um modelo com travessias simples previsíveis e um teste apenas quando há uma questão real de alcance ou risco. Isso é um critério, não uma escolha de fórmula ou de metros.

### Escala real de probabilidades

Contagem dos vinte resultados do d20, usando sucesso por total igual ou superior à CD:

| Bônus total | CD 6 | CD 10 | CD 14 | CD 18 | CD 22 | CD 26 |
|---|---:|---:|---:|---:|---:|---:|
| +0 | 75% | 55% | 35% | 15% | 0% | 0% |
| +4 — atributo 3, treino/maestria 1 | 95% | 75% | 55% | 35% | 15% | 0% |
| +10 — atributo 6, treino/maestria 4 | 100% | 100% | 85% | 65% | 45% | 25% |

Uma dificuldade rotulada como “difícil”, CD 14, deixa o iniciante especialista com 55% de sucesso. Exigir dois sucessos desse tipo para uma única travessia — salto e aterrissagem no mesmo risco — reduz o sucesso completo para **30,25%**; três testes reduzem para **16,64%**. Mesmo três testes fáceis de 95% deixam **85,74%** de sucesso completo.

Portanto, declarar “teste para saltar, teste para alcançar a borda e teste para não cair” pode tornar o Parkour muito mais arriscado do que parece em cada frase. Dois testes só se justificam quando resolvem perigos independentes que o jogador consegue distinguir.

### Pontos que precisam de texto objetivo

- A distância escolhida é anunciada antes do d20. O resultado não concede livremente qualquer destino que o jogador imaginar depois.
- Salto horizontal, salto vertical e alcançar uma borda são situações diferentes. A fórmula deve esclarecer se mede pés, mãos ou destino de aterrissagem.
- Corrida preparatória, se existir, precisa de trajeto concreto e custo contado. “Já me movi em algum lugar” não deve valer automaticamente como impulso na direção desejada.
- É preciso ter movimento suficiente para a trajetória declarada, incluindo a aproximação que a regra cobrar. Correr permite dispor de mais movimento, mas só aumenta alcance de salto se a nova regra disser isso expressamente.
- Falha curta pode deixar o personagem na borda ou em queda, conforme a consequência escolhida para o procedimento. A regra deve determinar qual desses resultados acontece e se há uma tentativa adicional de se segurar; isso não pode surgir como salvamento gratuito variável por mestre.
- Se o teste muda a distância atingida, o procedimento deve evitar uma conta contínua de metros por ponto que torne cada d20 uma nova consulta. Poucas faixas ajudam mesas com vários mestres.

## 3. A interação mais sensível: parede, salto e abate

No nível 2, o Incursor comum tem **12 m de deslocamento** e pode usar até **6 m** por paredes/espaços de criaturas. O Assassino recebe oportunidade de abate ao percorrer **pelo menos metade do deslocamento por uma parede e depois saltar de um apoio**.

O caso mínimo de uma ficha comum já usa os **6 m de parede**. Ainda pode haver movimento total, porém o limite de parede está consumido. Se a nova regra somar qualquer salto a esse mesmo limite só porque o jogador usa Acrobacia, o gatilho se torna inviável nesse nível: não sobra trecho acrobático para o salto obrigatório.

A proposta precisa distinguir:

1. **Movimento total disponível**, de que saem parede e salto.
2. **Limite dos trechos especiais**, que a habilidade atual vincula a parede/travessia de criaturas e amplia para líquidos no Pugilista.
3. **Perícia do teste**, que não transforma por si só toda a trajetória em parede.

O salto deve ter seu custo e sua dificuldade normais sem consumir duas reservas pela simples troca de Atletismo por Acrobacia. A redação definitiva precisa tornar isso explícito, conferindo a compatibilidade com a habilidade aprovada.

A segunda aproximação do Assassino exige **descer 4,5 m de uma posição elevada com apoio**, usando Movimento Acrobático. Ela não concede imunidade a quedas. Uma descida guiada por apoios e uma queda livre de 4,5 m precisam de tratamentos identificáveis. Cobrar dano de queda por toda perda de altura faria até escadas, escalada descendente e o próprio gatilho de Parkour dependerem de sofrer dano.

Usar a vítima como apoio permite um salto específico depois do acerto, com movimento restante e sem oportunidade. Isso não concede movimento novo, teleporte, retorno automático a uma altura anterior ou cancelamento de toda a queda que ainda esteja ocorrendo. A nova regra deve definir quando um apoio realmente encerra uma queda, evitando reiniciar a contagem de altura ao tocar de leve cada parede ou inimigo.

## 4. Dano de queda: escala antes de dado e teto

### Linear por faixas de 3 m, com limite

Um modelo desse tipo pode ser escrito para análise como:

`dano médio bruto = média da unidade de dano × mínimo(unidades de altura efetiva, limite de unidades)`.

Os parâmetros ainda precisam ser escolhidos: primeira altura que causa dano; unidade de dano; frações de 3 m; limite; mitigação. Este documento não fixa nenhum deles.

Vantagens: uma variável física principal, cálculo simples, resultado que independe de quem é o mestre, previsão razoável de risco. Um teto também limita quantidade de dados.

Custos: os mesmos metros passam a representar uma fração menor da Vida nos níveis altos; acima do teto, alturas diferentes têm o mesmo dano; pequenos desníveis em torno de cada faixa podem mudar o resultado de modo abrupto. É preciso declarar o tratamento dos 4,5 m do Parkour, sem depender do arredondamento genérico para decidir a regra nova.

### Vida realmente disponível no sistema

Valores pela vida fixa, **Constituição 2 em cada comparação**, sem equipamento, resistência, vida temporária ou outros benefícios. Não representam uma build ótima ou progressão obrigatória de Constituição.

| Nível | Bastião | Vanguarda/Guia | Emanador/Evocador/Incursor |
|---|---:|---:|---:|
| 1 | 14 | 10 | 8 |
| 2 | 23 | 17 | 14 |
| 11 | 104 | 80 | 68 |
| 30 | 275 | 213 | 182 |

Fonte: `manual/10-como-jogar.md`, Vida e PE por Caminho, com `(Vida inicial + CON) + (Vida por nível + CON) × (nível−1)`.

Para enxergar apenas a sensibilidade do dado, suponha por um momento uma unidade por cada 3 m completos, sem altura gratuita, sem mitigação e antes de alcançar um teto. As alternativas abaixo são **sondas matemáticas, não propostas finais**:

| Altura exata | Se a unidade fosse d4 | Se fosse d6 | Se fosse d8 |
|---|---:|---:|---:|
| 3 m | média 2,5 | 3,5 | 4,5 |
| 6 m | média 5 | 7 | 9 |
| 12 m | média 10 | 14 | 18 |
| 30 m | média 25 | 35 | 45 |

Por exemplo, a sonda d6 faria uma queda de 12 m atingir, em média, a Vida inteira do Incursor de nível 2 dessa comparação e **7,69%** da Vida do mesmo Caminho no nível 30. Isso pode ser apropriado à escala sobrenatural desejada, mas precisa ser deliberado. Média de dano igual à Vida não significa chance de queda a zero de 100%, e chegar a zero tem regras próprias; não equivale automaticamente a morte.

Um teto fixo torna essa diferença mais forte. Para qualquer teto `C` de unidades e média `μ`, a fração média máxima da Vida é `C×μ / Vida máxima`, antes de reduções. Escolher `C` exige decidir se quedas extremas serão ameaça física relevante para um personagem avançado ou se a progressão tornará esse perigo secundário. Nenhuma das respostas vem pronta de outro sistema.

### Dano ou tolerância proporcionais ao salto

| Vínculo proposto | Benefício possível | Problema a testar |
|---|---|---|
| Descontar uma altura segura calculada pelo salto | Personagens atléticos aterrissam melhor; saltar até onde o próprio corpo alcança parece seguro. | Buffs de salto passam a reduzir dano de queda; se Correr aumenta o salto, correr poderia também tornar o corpo resistente à queda. Força baixa prejudica novamente o Assassino de Destreza. |
| Dano baseado na altura dividida pela capacidade de salto | Normaliza o risco para personagens físicos diferentes. | Introduz divisão, singularidade quando a capacidade é zero, dúvidas sobre salto horizontal/vertical e forte dependência de benefícios temporários. |
| Dano como parcela da Vida | Preserva ameaça ao longo dos níveis. | Faz dois corpos sofrerem números diferentes da mesma queda e pode reduzir o valor da Constituição/Caminho. Não decorre da regra atual e exige decisão ampla de identidade. |

A altura física da queda é uma base estável para consulta. Se atletismo alterar a tolerância, convém avaliar essa parcela separadamente; não ligar todos os parâmetros de dano à distância que o personagem salta naquele turno.

Também precisa ser definido de onde se mede a queda após um salto normal. Usar indiscriminadamente a descida desde o ápice pode fazer um salto vertical bem-sucedido causar dano ao próprio saltador ao retornar ao chão. “Altura perdida”, “trajetória percorrida” e “salto controlado” precisam de exemplos que eliminem essa diferença de interpretação.

### Interações que mudam o risco

- **Tipo de dano:** se a nova regra escolher Concussão, Alicerce poderá reduzir pela metade enquanto ativo para quem escolheu esse tipo. Isso é efeito da habilidade atual, salvo exceção expressa que seria uma decisão mecânica adicional.
- **Defesa não é Redução de Dano:** queda ambiental sem rolagem de ataque não passa por Bloquear. Não permitir automaticamente que o bônus de Defesa reduza a queda.
- **Cobrir-se de energia** fala em redução como Reação “num golpe”. Se for desejado que alcance queda ambiental, a compatibilidade precisa de definição expressa; não presumir extensão pela palavra impacto.
- **Vida temporária** é consumida antes da Vida real, conforme a regra geral. Ignorá-la exigiria exceção.
- **Chegar a zero** usa Aguentar/Insistir e consequências publicadas. Não acrescentar morte instantânea ou trauma permanente em uma nota de movimento sem tratar a mudança como decisão separada.
- **Queda forçada** pode ser consequência de um empurrão com teste próprio. Um segundo teste automático para anular todo o perigo pode baratear o empurrão; ausência total de resposta perto de um abismo também amplifica controle. Esses dois testes precisam resolver etapas diferentes, se ambos existirem.

## 5. Acrobacia para aterrissar: redução finita e procedimento curto

A descrição de Acrobacia já sustenta uma função de aterrissagem. Ela precisa coexistir com Atletismo para alcançar o destino e com a exceção do Parkour.

| Modelo de mitigação | Vantagem | Risco |
|---|---|---|
| Redução fixa de altura para quem atende a requisitos publicados | Pouco tempo de mesa; previsível para o jogador. | Se concedida a todos sem investimento, treino em Acrobacia não pesa; se muito ampla, apaga todo desnível relevante do cenário comum. |
| Um teste, que no sucesso desconta altura fixa | Treino/DEX influenciam; o limite de redução evita anular quedas arbitrariamente altas. | Cria uma rolagem adicional; CD crescente com altura pode produzir pouco benefício justamente quando importa. |
| Redução pela margem de sucesso | Especialista pode ter resultados graduais. | Mais contas, saltos de resultado, crescimento com maestria; torna o efeito muito mais difícil de calibrar e explicar. |
| Redução fracionária do dano | Escala com quedas grandes. | Pode manter proteção elevada até alturas extremas; somada a resistência exige regra clara de combinação. |

Para a alternativa “teste e redução fixa”, use na calibração uma altura reduzida limitada `R`, uma altura efetiva `H` e chance de sucesso `p`. O resultado nunca remove mais que `R`: sucesso deixa `máximo(0,H−R)`; falha deixa `H`. A redução média de altura é `p × mínimo(H,R)`. Zerar uma queda pequena em um sucesso é distinto de conceder imunidade a qualquer queda.

Requisitos a decidir explicitamente:

- O personagem precisa estar consciente e capaz de controlar o corpo? O que Agarrado, Impedido e uma carga incompatível impedem?
- A tentativa vale em queda involuntária, salto deliberado ou ambos? Quem é empurrado ainda pode amortecer sem desfazer o empurrão?
- Cobra Reação? Isso cria concorrência com Reflexo, Evasão e outras respostas do Incursor. Não inserir esse custo como detalhe neutro: ele muda o kit e precisa ser avaliado.
- Há apenas uma tentativa de amortecer por aterrissagem, mesmo que existam vários segmentos de queda?
- Uma tentativa de agarrar a borda já consumiu o recurso ou constitui outro risco? Evitar repetir testes ilimitados até passar.
- Uma queda evitada ou mitigada continua podendo deixar Derrubado? A condição e o dano devem ser decididos separadamente, sem imunidade implícita.

Evitar resolver o teste por “Acrobacia ou TR Físico, escolha o melhor” sem analisar o efeito sobre treinos e Legados. **Tranco** e **Couro** refazem TR Físico; **No Braço** refaz perícia de Força/Destreza. A escolha entre perícia e resistência determina quais benefícios funcionam e precisa ter uma razão consistente.

## 6. Oito casos que a proposta deve conseguir resolver

As distâncias abaixo são situações de teste. Elas não estabelecem alcance gratuito, CD ou dano final.

| Caso | Situação | O que precisa ficar decidível antes da rolagem | Critério de aprovação |
|---|---|---|---|
| **1. Vão comum entre duas lajes** | Personagens com Força 0, 3 e 6 enfrentam o mesmo vão de 1,5 m ou 3 m; primeiro sem pressão, depois perseguidos. | Se passa automaticamente; quando há teste; necessidade de impulso; movimento gasto; efeito da falha. | Força faz diferença sem transformar Força 0 em incapacidade de qualquer salto. Os dois mestres aplicam o mesmo procedimento. |
| **2. Janela e borda acima da cabeça** | Há espaço para saltar parado ou tomar impulso; a borda é alcançável com as mãos, mas não comporta os pés. | Diferença entre salto horizontal, vertical e alcançar; mãos necessárias; possibilidade de terminar pendurado. | A solução comum não entrega gratuitamente todo o benefício de Apoios de infiltração; a exceção do Assassino funciona de modo claro. |
| **3. Escalada e travessias especiais** | Parede comum com apoios, trecho liso e canal de água. Comparar personagem comum, Yumi nv2, Incursor e Pugilista nv11. | Velocidade/custo de escalada; quando apoios são indispensáveis; permissões especiais e apoio final. | Yumi conserva valor por escalar à velocidade normal; Incursor tem sua passagem por parede; Pugilista conserva travessia de líquidos. Acrobacia comum não vira escalada livre ou corrida sobre água. |
| **4. Parede seguida de abate** | Assassino nv2, deslocamento 12 m, percorre 6 m na parede e tenta saltar até um alvo a 3 m do apoio. | Saldo total de movimento; faixa exigida para o salto; teste de Acrobacia permitido; limite de parede separado. | O gatilho é viável com uma execução legal. O salto não é proibido só porque os 6 m de parede consumiram a metade acrobática. |
| **5. Descer, atacar e usar a vítima** | Assassino desce 4,5 m com apoio, ataca e tenta chegar a uma borda usando o corpo da vítima. Comparar com pular livremente da mesma altura. | Descida controlada versus queda; eventual dano e momento; movimento restante; destino válido; falha do salto; mãos ao terminar. | O Parkour conserva a oportunidade de abate e a saída sem oportunidade, sem ganhar imunidade ou movimento novo. O dano não decorre apenas de ter descido 4,5 m usando apoios. |
| **6. Empurrão na beira** | Cortar a Fuga pode empurrar até 3 m; o alvo está a 1,5 m de uma borda. Há uma plataforma inferior, ou queda longa sem apoio. | Quando sai do apoio; eventual tentativa de segurar; possível amortecimento; resolução de Derrubado/empurrão antes da queda. | Teste de defesa e mitigação, se ambos existirem, têm objetos distintos. Nenhum mestre concede tentativas infinitas; a consequência ambiental é previsível. |
| **7. Movimento fora do turno e falta de apoio** | Passo Guardado ou Passo Rápido permite sair de um perigo, mas o trajeto inclui vão ou termina sem piso. | Pode saltar com aquele movimento? O que ocorre quando os metros acabam no ar? Quando começa/resolve a queda? | Movimento adicional não vira voo ou suspensão entre turnos. As exigências de percurso e aterrissagem continuam valendo fora do turno. |
| **8. A mesma queda em quatro níveis** | Quedas de 3 m, 4,5 m, 12 m e grande altura são comparadas nos níveis 1, 2, 11 e 30, com Con2; repetir consciente, sem controle do corpo e com resistência aplicável. | Unidades e arredondamento; teto; elegibilidade da mitigação; tipo de dano; condições; resultado a zero. | A equipe conhece a fração de Vida perdida, a chance de redução e os resultados extremos. Sobrevivência avançada ou risco persistente são decisões deliberadas. |

Para fechar o teste, entregar a dois revisores apenas regra, fichas reduzidas e posição inicial. Pedir que anotem ações, metros, teste, consequência e saldo. Divergências revelam termos ainda abertos; médias de dano sozinhas não medem previsibilidade entre mestres.

## 7. Decisões mínimas antes da redação final

1. Definir a tarefa que cada teste resolve: alcançar, segurar ou amortecer; limitar duplicação do mesmo risco.
2. Escolher base automática, teste por faixa ou combinação; verificar Força 0 e Assassino de Destreza antes de calibrar extremos.
3. Definir contagem do movimento em salto, parede e escalada; separar limites das habilidades e deslocamento total.
4. Distinguir descida com apoio de queda livre, incluindo o gatilho de 4,5 m do Parkour.
5. Fixar os parâmetros de queda somente depois de medir Vida, resistência e mitigação nas faixas de nível.
6. Escrever falha, falta de movimento/apoio e momento da queda de forma que turnos não gerem suspensão involuntária ou testes infinitos.
7. Preservar casos simples curtos: uma consulta, no máximo o teste necessário, saldo de movimento explícito. Regras sobrenaturais específicas continuam especificadas nas habilidades.

Não foi encontrada nas fontes consultadas uma regra comum já fechada de metros de salto, dano por altura de queda ou amortecimento numérico. As referências existentes pressupõem essas regras; este relatório identifica os requisitos para completá-las e não preenche as lacunas como se os novos valores já estivessem aprovados.

### Recorte editorial confirmado no fechamento

É viável publicar nesta rodada uma **minuta consultável**, com movimento/terreno/escalada/natação, procedimento de salto e candidatos numéricos identificados como propostas. A análise de queda pode permanecer como requisitos, exemplos de escala e decisões abertas, sem uma fórmula jogável nova. Isso não exige resolver todo o balanceamento ambiental antes de revisar a clareza do procedimento.

Na parte de natação, preservar Atletismo como perícia responsável e distinguir água tranquila de correnteza/perigo. A eventual regra de custo de movimento não deve, sozinha, resolver afogamento, respiração ou travessia de líquido nocivo. Movimento sobre líquidos do Pugilista continua uma permissão distinta, sujeita a apoio final e contato com o líquido. Esses limites bastam para evitar que um parágrafo editorial prometa um subsistema ambiental completo.
