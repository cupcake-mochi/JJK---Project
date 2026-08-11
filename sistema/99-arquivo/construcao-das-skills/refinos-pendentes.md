# Refinos pendentes nas skills

Vindos da revisão humana da iteração 1 (06/08/2026). Não aplicados ainda — entram na próxima vez que as skills forem reinstaladas.

## 1. Colisão com a convenção do hobby, não só com o próprio sistema

**Origem:** revisão do eval-0. "Vulnerável" na maior parte dos sistemas de RPG não significa "atacantes têm vantagem" — significa tomar dano dobrado ou acrescido. Nenhuma das duas execuções questionou o nome; as duas aceitaram a definição do enunciado e discutiram só o preço.

**O que muda:** `redacao-acessivel-rpg` hoje só caça colisão de termo **dentro** do material. Precisa caçar também colisão com o vocabulário estabelecido do hobby — palavras que já carregam significado em D&D, PbtA, Storyteller e afins. Um termo emprestado com significado trocado gera erro de mesa que nenhum glossário conserta, porque o jogador não vai consultar uma palavra que ele acha que já sabe.

`design-mecanicas-rpg` precisa da mesma checagem no momento de nomear uma mecânica nova: o nome promete o que o efeito entrega?

**Lista curta de termos minados:** vulnerável, vantagem, resistência, imunidade, condição, iniciativa, reação, concentração, crítico, nível, proficiência.

## 2. Perguntar antes de presumir

**Origem:** revisão do eval-2. A execução com skill presumiu informação sobre o resto do manual e declarou que presumiu; a sem skill presumiu e escondeu. Declarar é melhor que esconder, mas o certo era **perguntar antes**.

**O que muda:** `redacao-acessivel-rpg` precisa de uma instrução explícita — ao revisar material de outra pessoa, levantar as perguntas que mudam a revisão **antes** de reescrever, não depois. Só seguir sem perguntar quando a pergunta não altera o resultado.

## 3. Bias para brevidade e decisão

**Origem:** o revisor humano se perdeu no volume. As quatro execuções com skill somaram cerca de 6.500 palavras; a revisão inteira passou de 11 mil. Isso é erro de projeto do teste, mas também sinal sobre as skills: elas produzem resposta longa demais para consumo humano.

**O que muda:** as quatro precisam de uma instrução de saída — abrir pela conclusão, uma recomendação clara, e o raciocínio de apoio depois e mais curto. Análise completa não é o mesmo que análise longa. Onde couber, tabela em vez de prosa.

## 4. Correção de grader (já aplicada)

A asserção "diz quando parar de testar" dava falso negativo: exigia as expressões literais "parar de testar" ou "quando parar", e a resposta dizia "o sinal de parar continua o mesmo de sempre: quando o retorno de uma rodada só repete o da anterior, para". Corrigida em `montar-benchmark.py`; a execução com skill do eval-3 passou de 6/7 para 7/7, e a média com skill de 92,2% para 95,8%.

Lição para as próximas asserções: casar por **conceito**, com várias formulações, não por frase literal. Asserção frágil produz ruído que parece problema da skill.
