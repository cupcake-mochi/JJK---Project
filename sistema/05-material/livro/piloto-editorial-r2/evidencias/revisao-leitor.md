# Revisão independente de leitura — piloto editorial r2

2 de outubro de 2026. Leitura de `sistema/05-material/livro/piloto-editorial-r2/PILOTO.md` e `LOTE-TECNICO.md`, confrontada com as fontes pertinentes da v0.331. Sem edição do projeto. Esta revisão examina texto, pressupostos e operações; não substitui teste com leitores humanos nem inspeção visual do PDF. Os arquivos estavam sendo atualizados durante a leitura; os localizadores abaixo identificam também o trecho para facilitar a conferência.

## Parecer

Os exemplos principais permitem acompanhar o que o personagem decide, quais recursos paga e o saldo obtido. A situação preparada evita misturar a primeira conjuração com a proteção do Bastião; as duas resoluções de interceptação são alternativas explícitas. O Malabarista distingue ataque da ação, continuação, obtenção de Fluidez e arma disponível, sem criar ataques extras por acidente.

Não encontrei erro nas contas apresentadas: Kaori termina o primeiro exemplo com 18 de Vida e 5 PE; a interceptação deixa 15 ou 18 de Vida, conforme a alternativa; Haru gasta 6 PE e uma Fluidez por três ataques; o feitiço resulta em 3d8; Kaito conserva 6 PE com a básica ou fica com 3 ao comandar a especial. As escolhas finais propostas ao leitor têm resposta localizável: errar o feitiço deixa 5 PE e não gasta a Bônus; um aliado a 7 m fica fora da área de 6 m.

A amostra já serve para uma primeira avaliação humana de compreensão dessas tarefas delimitadas. Não permite alegar que uma pessoa terminou uma ficha ou aprendeu a resolver qualquer combate apenas com ela — o texto, corretamente, manda continuar a criação nas fontes completas.

## Ajustes relevantes

### 1. O saldo do turno usa um título que contradiz a disponibilidade indicada

**Local:** `PILOTO.md`, Uma rodada na ala oeste / quadro de resultado, linha 162: “Depois desse turno” seguido de “6 m restantes” e “Ação Bônus [...] disponíveis”.

O corpo do exemplo diz corretamente que os metros restantes podem ser usados **nesse turno**. O título, porém, situa o saldo depois dele. Para um iniciante, isso pode sugerir que o movimento ou a Bônus sobram para mais tarde.

**Correção sugerida:** “Neste ponto do turno” ou “Antes de encerrar o turno”. Preserve Vida/PE e a Reação, cuja disponibilidade tem outra janela. É correção de enquadramento temporal, sem alterar regra.

### 2. A apresentação geral das entidades omite um limite que impede uma extrapolação importante

**Local:** `LOTE-TECNICO.md`, Você e sua entidade / tabela de recursos, linha 189: cada entidade recebe uma básica; texto seguinte fala em orientar todas as entidades.

A regra é verdadeira, e o exemplo de um cão está correto. Mas a página tem voz de consulta geral e não menciona que **no máximo duas entidades atuam causando dano no turno do invocador, fora as especiais comandadas**. Um leitor que aplique o resumo a três ou mais corpos pode concluir que todos usam sua básica para morder. Esse limite consta de `manual/60-invocacoes.md`, Básica e limite de ataques, linha 673.

**Correção sugerida:** acrescentar uma frase curta com esse limite junto da básica ou uma remissão explícita ao limite de entidades causando dano. Não é necessário reproduzir ali todas as exceções; é necessário impedir que “cada uma tem básica” se torne “todas podem causar dano nesse turno”.

### 3. Bloquear é reproduzível na ficha pronta, mas sua origem fica opaca

**Local:** `PILOTO.md`, O ataque contra um aliado / tabela, linha 288: `2d10 + 2`.

A conta está correta para Defesa 13. Porém, o texto não explica de onde vem o +2. A ficha tem outros valores 2, então um leitor pode atribuí-lo à Destreza ou Constituição. Isso prejudica transferir o procedimento para a própria ficha. O manual fornece `2d10 + (Defesa − 11)` em `10-como-jogar.md`, Bloquear, linha 155.

**Correção sugerida:** uma explicação local curta: “O bônus é sua Defesa menos 11: 13 − 11 = 2.” Como o piloto usa números prontos, não é um impedimento para acompanhar o exemplo; torna-se necessário se a tarefa de avaliação pedir aplicar Bloquear a outra ficha. A escolha de interceptar antes do ataque está clara. Não encontrei fundamento para exigir também que a escolha de Bloquear ocorra antes do dado: o próprio exemplo da regra vigente admite vê-lo antes de bloquear.

### 4. O exemplo do cão ensina recursos, mas ainda não permite resolver sozinho o ataque

**Local:** `LOTE-TECNICO.md`, O cão guarda a porta, linhas 213–230.

Há acerto, alcance e dano do cão, mas a Defesa da maldição não é informada. O leitor consegue escolher entre básica e especial e fechar o saldo de ações/PE; não consegue rolar e decidir se acertou sem um dado adicional. O Malabarista delimita isso expressamente ao mandar considerar os ataques já acertados. O cão deixa essa delimitação menos evidente.

**Correção sugerida, conforme o objetivo:** fornecer a Defesa do alvo preparado se a intenção é uma tentativa jogável; ou dizer no começo que o recorte compara apenas o gasto de ações e energia, usando as defesas da ficha do inimigo para a resolução. Não precisa inventar outro combate completo. Uma atividade de teste humano sobre recursos pode manter o recorte atual, desde que não seja avaliada como tarefa de resolver o ataque inteiro.

## Pressupostos e lacunas: o que está bem delimitado

- O lote distingue Ação de Movimento e metros, explicita dividir o movimento e mostra que Desengajar não concede distância. A caminhada de Kaori de 3 m, com 6 restantes, está clara.
- Saltar, escalar, cair e esconder-se não receberam procedimentos emprestados de outro sistema. O catálogo de perícias explicita que nomear sua aplicação não fornece esses procedimentos. Não usar esse catálogo como evidência de que as lacunas gerais já foram resolvidas.
- Ricochete separa o primeiro trecho do percurso total, preserva a desvantagem se o primeiro já exceder a faixa normal e não promete retorno da arma. Mudar o Destino conserva a diferença entre correção e ataque adicional.
- A sequência de Haru começa sem Fluidez, ganha uma vez e não repõe o recurso pelos dois acertos posteriores. O exercício alternativo de Ricochete identifica corretamente a falta de recurso anterior à rolagem.
- A fonte completa do cão sustenta os valores prontos: `manual/60-invocacoes.md`, exemplo de montagem, linhas 539–545. O +6 da especial decorre de Precisão; não é necessário ensinar sua construção para o exercício de comandar, mas também não se deve generalizar que toda especial tenha +2 de acerto.
- Na montagem de Peso nas Mãos, a devolução paga a Melhoria em vez de exceder o orçamento. A técnica usar Força no acerto não acrescenta Força ou dano de soco ao feitiço. O texto evita essas confusões.

## Voz e uso da avaliação

A abertura parte de pessoas, lugar e objetivo concretos, e a exposição posterior explica o que o leitor acabou de acompanhar. As instruções estão predominantemente em voz direta, com custos e gatilhos reconhecíveis. Não encontrei repetição retórica relevante do tipo “não é X, é Y” usada como substituto de explicação; as negativas do lote em geral excluem interpretações mecânicas reais. Não recomendaria cortá-las por aparência estilística.

O trecho técnico de Mudar o Destino continua denso. Isso corresponde a uma habilidade com muitos vínculos de regra; não é evidência suficiente para reescrevê-la de novo antes de observar onde leitores de fato se perdem. Peça que encontrem um alvo permitido, indiquem de onde medem os 6 m e digam se gastam outro ataque. Observe o raciocínio e a localização da resposta, sem exigir repetir a redação do livro.

Nenhuma revisão textual por agente permite afirmar “iniciante compreendeu”. As evidências obtidas aqui são coerência do texto e possibilidade de reproduzir operações delimitadas. O próximo teste humano pode usar as perguntas já escritas e os saldos, evitando cobrar salto, furtividade ou manobras ainda sem base fechada.
