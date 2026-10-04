# Delta para revisão independente de Consulta

Antes: `148ebf0e59568ebf42626f53bc149875c3614d631a71e255fe1dfd8f8f36122a` (28 blocos). Depois: `a4d4b68bbed3c62efdc849ab32a08350694f6653bdeea08ec71874b5aada4980` (30 blocos).

O arquivo anterior foi reconstituído exatamente pelo diff preservado e confirmado pelo hash original; cópia em `historico/antes-prova-nomes-maxima/CONSULTA.md`. O diff completo está em `DELTA-DESDE-28-BLOCOS.diff`.

## Escopo

Há uma página nova de conteúdo: **Ficha de recuperação**. A outra página adicional é continuação do índice, devido aos nomes atuais e seus aliases. A redistribuição de linhas entre páginas de glossário/índice não é uma mudança de regra. Abaixo são apresentados somente os blocos de prosa alterados e as entradas diferentes, sem repetir o conteúdo já lido.

## Testes na mesa

```diff
--- antes
+++ depois
@@ -23,4 +23,4 @@
 **Conversões:** Padrão → Bônus → Movimento. Cada conversão gasta o recurso anterior. Ela não devolve usos nem altera requisitos de uma habilidade.
 
-Antes de passar a vez, confira efeitos com prazo no fim do turno e anote recursos gastos. **Consulta:** Testes; Turnos; Reações e concentração.
+Antes de passar a vez, confira efeitos com prazo no fim do turno e anote recursos gastos. **Consulta:** Testes; Turnos; Reações e ataques de oportunidade; Concentração.
 
```

## Ataques e efeitos

```diff
--- antes
+++ depois
@@ -26,4 +26,4 @@
 Use um marcador junto do participante a cujo turno o prazo se refere. Um efeito que termina no começo do turno não dura até o fim dele.
 
-Ao sofrer dano, siga Dano e Condições e Recuperação para os recursos atingidos, a queda e suas consequências. Efeitos sobre Integridade seguem o procedimento de alma. A ficha da capacidade continua sendo a referência para exceções.
+Ao sofrer dano, siga Dano e Recuperação para os recursos atingidos, a queda e suas consequências. Efeitos sobre Integridade seguem o procedimento de alma. A ficha da capacidade continua sendo a referência para exceções.
 
```

## Repertório e inventário

```diff
--- antes
+++ depois
@@ -16,5 +16,5 @@
 |---|---|---|
 | Feitiços, Manejos ou Katas | ______ | __________________________ |
-| Passivas pagas | ______ | __________________________ |
+| Talentos pagos | ______ | __________________________ |
 | Entidades por espaço e outras ocupações | ______ | __________________________ |
 | Total ocupado / disponível | ______ / ______ | __________________________ |
```

## Ficha de entidade

```diff
--- antes
+++ depois
@@ -25,4 +25,5 @@
 | Defesa e origem de cada parcela | ________________________________________ |
 | PV atuais / máximos | ______ / ______ |
+| Integridade atual / máxima, quando aplicável | ______ / ______ |
 | Reserva própria, se houver, atual / máxima | ______ / ______ |
 
```

## Ficha de capacidades da entidade

```diff
--- antes
+++ depois
@@ -8,10 +8,10 @@
 | Espaços de especiais ocupados / disponíveis | ______ / ______ |
 | Especiais conhecidas | ________________________________________ |
-| Passivas e Classe Passiva | ________________________________________ |
+| Talentos e Categoria de Efeito | ________________________________________ |
 | Trunfos adquiridos, quando permitidos | ________________________________________ |
 
 ## Capacidade
 
-**Nome e tipo:** ____________________ **Classe ou CP:** ______
+**Nome e tipo:** ____________________ **Classe ou CE:** ______
 
 | Montagem | Registro |
```

## Ficha de recuperação

# Ficha de recuperação

**Personagem:** ____________________ **Cena e data:** ____________________

| Reservas | Atual | Máximo |
|---|---|---|
| Vida | ______ | ______ |
| Integridade, quando aplicável | ______ | ______ |

**Estágio de Integridade:** ______ **Sequelas atuais:** ______

**Condições e outras causas de inconsciência:** __________________________________

## Queda em andamento

| Registro | Valor ou descrição |
|---|---|
| Causa e momento da queda | ________________________________________ |
| Máximo de referência da queda | ________________________________________ |
| Sequelas antes desta queda | ________________________________________ |
| Escolha: Aguentar ou Insistir | ________________________________________ |
| Janela inicial / restante | ______ / ______ |
| Ponto da iniciativa para a contagem | ________________________________________ |
| Tratamento necessário / acumulado | ______ / ______ |
| Estável? Momento e origem do socorro | ________________________________________ |
| Máximo perdido por Insistir | ________________________________________ |
| Custos já pagos / próximo pagamento | ________________________________________ |

## Atendimento e desfecho

| Momento e fonte | Cura válida ou outro atendimento | Consequência registrada |
|---|---|---|
| __________________ | __________________ | __________________ |
| __________________ | __________________ | __________________ |
| __________________ | __________________ | __________________ |

**Queda encerrada? Sequela registrada?** ________________________________________

**Derrotado? Causa e condição para sair desse estado:** ___________________________

**Descanso concluído e recursos recuperados:** __________________________________

Use uma folha para cada queda ou risque o registro anterior de forma identificável. Anote o tratamento separadamente da vida até cumprir o procedimento de Socorro. Uma reserva recuperada não significa, por si, que a pessoa acordou ou voltou à cena.

**Consulta:** Vida a zero; Insistir; Socorro; Sequelas e Cicatrizes; Derrota e morte; Inconsciente; Estágios de Integridade; Descansos.



## Registro de missão

```diff
--- antes
+++ depois
@@ -39,4 +39,4 @@
 **Conferência com os jogadores:** _______________________________________________
 
-Registre o destino de itens compartilhados para que duas fichas não recebam a mesma peça por engano. Uma pendência de interpretação deve acompanhar o registro, sem virar alteração permanente silenciosa. **Consulta:** Progressão; Recuperação.
+Registre o destino de itens compartilhados para que duas fichas não recebam a mesma peça por engano. Uma pendência de interpretação deve acompanhar o registro, sem virar alteração permanente silenciosa. **Consulta:** Progressão; Dano e Recuperação.
 
```

## Definições e remissões do glossário

### Ataque

**Antes:** Tentativa de atingir um alvo com rolagem de acerto. Um ataque concedido não equivale necessariamente à Ação Atacar completa. → `regras-basicas/lote-02/ATAQUES-E-DEFESA.md#ataques` (Ataques).

**Depois:** Tentativa de atingir um alvo com rolagem de acerto. Um ataque concedido não equivale necessariamente à Ação Atacar completa. → `regras-gerais/lote-final/REGRAS-GERAIS.md#ataques` (Ataques).
### Atributo

**Antes:** Valor da ficha usado por testes e capacidades. O próprio número anotado serve de modificador quando a regra o pede. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#atributos` (Atributos).

**Depois:** Valor da ficha usado por testes e capacidades. O próprio número anotado serve de modificador quando a regra o pede. → `regras-gerais/lote-final/REGRAS-GERAIS.md#atributos` (Atributos).
### Ação

**Antes:** Recurso usado para executar uma tarefa. Padrão, Bônus e Movimento têm usos distintos; a Reação responde a um gatilho. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#turnos` (Turnos).

**Depois:** Recurso usado para executar uma tarefa. Padrão, Bônus e Movimento têm usos distintos; a Reação responde a um gatilho. → `regras-gerais/lote-final/REGRAS-GERAIS.md#turnos` (Turnos).
### Ação Bônus

**Antes:** Recurso gasto em uma opção que declare esse custo. Não torna uma tarefa gratuita nem fornece uma habilidade por si. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#turnos` (Turnos).

**Depois:** Recurso gasto em uma opção que declare esse custo. Não torna uma tarefa gratuita nem fornece uma habilidade por si. → `regras-gerais/lote-final/REGRAS-GERAIS.md#turnos` (Turnos).
### Ação Completa

**Antes:** Custo que compromete Padrão, Bônus e Movimento do turno. Também aparece em textos anteriores como Rodada inteira. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#turnos` (Turnos).

**Depois:** Custo que compromete Padrão, Bônus e Movimento do turno. Também aparece em textos anteriores como Rodada inteira. → `regras-gerais/lote-final/REGRAS-GERAIS.md#turnos` (Turnos).
### Ação Padrão

**Antes:** Recurso usado por ações como Atacar, Conjurar e Ajudar, salvo custo próprio indicado na capacidade. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#acoes` (Ações).

**Depois:** Recurso usado por ações como Atacar, Conjurar e Ajudar, salvo custo próprio indicado na capacidade. → `regras-gerais/lote-final/REGRAS-GERAIS.md#acoes` (Ações).
### Ação de Movimento

**Antes:** Recurso que permite percorrer o deslocamento ou pagar uma tarefa com esse custo. Não é uma medida em metros. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#turnos` (Turnos).

**Depois:** Recurso que permite percorrer o deslocamento ou pagar uma tarefa com esse custo. Não é uma medida em metros. → `regras-gerais/lote-final/REGRAS-GERAIS.md#turnos` (Turnos).
### CD

**Antes:** Classe de Dificuldade: valor que uma rolagem precisa igualar ou superar. O procedimento define a CD ou explica como determiná-la. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#testes` (Testes).

**Depois:** Classe de Dificuldade: valor que uma rolagem precisa igualar ou superar. O procedimento define a CD ou explica como determiná-la. → `regras-gerais/lote-final/REGRAS-GERAIS.md#testes` (Testes).
### Carga

**Antes:** Conjunto de objetos transportados e sua ocupação, medida em Volume. → `regras-comuns/lote-06-r6/MOVIMENTO-E-CARGA.md#carga` (Carga).

**Depois:** Conjunto de objetos transportados e sua ocupação, medida em Volume. → `regras-gerais/lote-final/REGRAS-GERAIS.md#carga` (Carga).
### Categoria de Efeito

**Antes:** não consta como entrada independente.

**Depois:** Escala usada por Talentos, Aptidões e Bênçãos, abreviada CE. Cada entrada informa seus requisitos e sua aquisição. Não é a Classe de um feitiço. → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Talentos).
### Cena

**Antes:** Trecho de jogo organizado em torno de uma situação. Sua passagem depende do que ocorre na ficção, não de uma quantidade fixa de turnos. → `regras-basicas/lote-04/RECUPERACAO.md#usos` (Cena e usos de habilidades).

**Depois:** Trecho de jogo organizado em torno de uma situação. Sua passagem depende do que ocorre na ficção, não de uma quantidade fixa de turnos. → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#usos` (Cena e usos de habilidades).
### Classe Passiva

**Antes:** Escala de acesso e investimento de uma Passiva. Não é a Classe de um feitiço ativado. → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Passivas).

**Depois:** não consta como entrada independente.
### Concentração

**Antes:** Manutenção de um efeito que exige essa atenção. Seu procedimento define interrupção e testes; preparações como Carregar têm regras próprias. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#reacoes` (Reações e concentração).

**Depois:** Manutenção de um efeito que exige essa atenção. Seu procedimento define interrupção e testes; preparações como Carregar têm regras próprias. → `regras-gerais/lote-final/REGRAS-GERAIS.md#concentracao` (Concentração).
### Condição

**Antes:** Estado nomeado que altera capacidades ou ações. Sua entrada e a fonte que o aplicou definem consequências e término. → `regras-basicas/lote-03-r3/DANO-E-CONDICOES.md#condicoes` (Condições).

**Depois:** Estado nomeado que altera capacidades ou ações. Sua entrada e a fonte que o aplicou definem consequências e término. → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#condicoes` (Condições).
### Crítico

**Antes:** Acerto que recebe o tratamento especial de dados previsto em Combate. Nem todo dado adicional acompanha a duplicação. → `regras-basicas/lote-02/ATAQUES-E-DEFESA.md#critico` (Dano e crítico).

**Depois:** Acerto que recebe o tratamento especial de dados previsto em Combate. Nem todo dado adicional acompanha a duplicação. → `regras-gerais/lote-final/REGRAS-GERAIS.md#critico` (Dano e crítico).
### Defesa

**Antes:** Valor comparado à rolagem de ataque. Não é um Teste de Resistência nem redução de dano. → `regras-basicas/lote-02/ATAQUES-E-DEFESA.md#defesa` (Defesa e cobertura).

**Depois:** Valor comparado à rolagem de ataque. Não é um Teste de Resistência nem redução de dano. → `regras-gerais/lote-final/REGRAS-GERAIS.md#defesa` (Defesa e cobertura).
### Derrotado

**Antes:** não consta como entrada independente.

**Depois:** Estado que encerra a participação ativa na cena. Recuperar reservas não devolve essa participação; consulte o procedimento de saída. → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#derrota` (Derrota e morte).
### Deslocamento

**Antes:** Distância que o personagem pode percorrer com uma Ação de Movimento, antes dos custos do terreno e demais alterações. → `regras-comuns/consolidado-r1/REGRAS-COMUNS.md#movimento` (Movimento e terreno).

**Depois:** Distância que o personagem pode percorrer com uma Ação de Movimento, antes dos custos do terreno e demais alterações. → `regras-gerais/lote-final/REGRAS-GERAIS.md#movimento` (Movimento e terreno).
### Desvantagem

**Antes:** Rolagem de dois d20 que usa o menor. Seu encontro com vantagem segue Testes. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#pericias` (Perícias e ofícios).

**Depois:** Rolagem de dois d20 que usa o menor. Seu encontro com vantagem segue Testes. → `regras-gerais/lote-final/REGRAS-GERAIS.md#pericias` (Treino e modificadores).
### Estabilizar

**Antes:** não consta como entrada independente.

**Depois:** Socorro que interrompe a perda de tempo da janela de queda enquanto suas condições forem mantidas. Não recupera vida nem acorda o alvo. → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#socorro` (Socorro).
### Exaustão

**Antes:** Consequência ligada a esforço e recuperação, com procedimento próprio. Não é uma Condição comprável do catálogo. → `regras-basicas/lote-04/RECUPERACAO.md#exaustao` (Exaustão).

**Depois:** Consequência ligada a esforço e recuperação, com procedimento próprio. Não é uma Condição comprável do catálogo. → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#exaustao` (Exaustão).
### Expressão da técnica

**Antes:** não consta como entrada independente.

**Depois:** Manifestação de aparência ou expressão ligada ao conceito da técnica, dentro dos limites de sua entrada. → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Talentos).
### Ferramenta amaldiçoada

**Antes:** Equipamento que carrega energia própria. Seu grau e sua ficha definem se possui um efeito especial. → `equipamento/lote-08/EQUIPAMENTO-AMALDICOADO.md#equipamento` (Equipamento amaldiçoado).

**Depois:** Equipamento que carrega energia própria. Seu grau e sua ficha definem se possui um efeito especial. → `equipamento/lote-final/EQUIPAMENTO.md#eqf-equipamento` (Equipamento amaldiçoado).
### Gatilho

**Antes:** Evento necessário para uma resposta ou efeito. Possuir um recurso disponível não dispensa esse evento. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#reacoes` (Reações e concentração).

**Depois:** Evento necessário para uma resposta ou efeito. Possuir um recurso disponível não dispensa esse evento. → `regras-gerais/lote-final/REGRAS-GERAIS.md#oportunidade` (Reações e ataques de oportunidade).
### Grau

**Antes:** Termo usado na patente e na classificação de ferramentas. A ficha informa qual escala está sendo usada; uma não concede a outra. → `equipamento/lote-08/EQUIPAMENTO-AMALDICOADO.md#graus` (Graus das ferramentas).

**Depois:** Termo usado na patente e na classificação de ferramentas. A ficha informa qual escala está sendo usada; uma não concede a outra. → `equipamento/lote-final/EQUIPAMENTO.md#eqf-graus` (Graus das ferramentas).
### Inconsciente

**Antes:** não consta como entrada independente.

**Depois:** Estado de quem perdeu a consciência. A regra que o causou determina como sair dele. → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#inconsciente` (Inconsciente).
### Integridade

**Antes:** Recurso usado pelas regras de alma. Seus efeitos e recuperação têm procedimento próprio. → `regras-basicas/lote-03-r3/DANO-E-CONDICOES.md#alma` (Dano na alma).

**Depois:** Recurso usado pelas regras de alma. Seus efeitos e recuperação têm procedimento próprio. → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#integridade` (Estágios de Integridade).
### Maestria

**Antes:** Bônus ligado ao nível. Só entra nas rolagens e valores que indiquem seu uso. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#atributos` (Atributos).

**Depois:** Bônus ligado ao nível. Só entra nas rolagens e valores que indiquem seu uso. → `regras-gerais/lote-final/REGRAS-GERAIS.md#atributos` (Atributos).
### Morrendo

**Antes:** Situação tratada pelas regras de queda e recuperação. Consulte seu procedimento antes de aplicar custos, prazos ou saídas. → `regras-basicas/lote-04/RECUPERACAO.md#zero` (Vida a zero).

**Depois:** Situação tratada pelas regras de queda e recuperação. Consulte seu procedimento antes de aplicar custos, prazos ou saídas. → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#zero` (Vida a zero).
### Movimento imposto

**Antes:** Deslocamento provocado por outra criatura ou efeito. O procedimento de movimento o distingue do percurso voluntário. → `regras-comuns/consolidado-r1/REGRAS-COMUNS.md#quedas` (Quedas e movimento imposto).

**Depois:** Deslocamento provocado por outra criatura ou efeito. O procedimento de movimento o distingue do percurso voluntário. → `regras-gerais/lote-final/REGRAS-GERAIS.md#quedas` (Quedas e movimento imposto).
### PV

**Antes:** Pontos de vida. Registre o valor atual separado do máximo. Vida temporária é anotada à parte. → `regras-basicas/lote-03-r3/DANO-E-CONDICOES.md#dano` (Dano).

**Depois:** Pontos de vida. Registre o valor atual separado do máximo. Vida temporária é anotada à parte. → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#dano` (Dano).
### Passiva

**Antes:** Capacidade cujo funcionamento e investimento seguem sua Classe Passiva. Uma entrada reativa ainda pode exigir ação ou gatilho. → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Passivas).

**Depois:** não consta como entrada independente.
### Patente

**Antes:** Reconhecimento do personagem no meio jujutsu, expresso por Grau. Não substitui nível nem requisito de uma capacidade. → `progressao/lote-01/PROGRESSAO.md#prog-inicio` (Experiência e Progressão).

**Depois:** Reconhecimento do personagem no meio jujutsu, expresso por Grau. Não substitui nível nem requisito de uma capacidade. → `progressao/lote-01/PROGRESSAO.md#prog-patentes` (Patentes).
### Proteção

**Antes:** Parcela da Defesa fornecida por equipamento ou capacidade, com regras próprias de combinação. → `equipamento/lote-02-r3/PROTECAO.md#protecao` (Proteção).

**Depois:** Parcela da Defesa fornecida por equipamento ou capacidade, com regras próprias de combinação. → `equipamento/lote-final/EQUIPAMENTO.md#eqp-protecao` (Proteção).
### Reação

**Antes:** Recurso gasto em uma resposta permitida por um gatilho. Sua recuperação ocorre no começo do próprio turno. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#reacoes` (Reações e concentração).

**Depois:** Recurso gasto em uma resposta permitida por um gatilho. Sua recuperação ocorre no começo do próprio turno. → `regras-gerais/lote-final/REGRAS-GERAIS.md#oportunidade` (Reações e ataques de oportunidade).
### Redução de Dano

**Antes:** Valor descontado durante a resolução do dano quando sua fonte permitir. Não aumenta a Defesa. Abreviação: RD. → `regras-basicas/lote-03-r3/DANO-E-CONDICOES.md#reducao` (Redução de Dano).

**Depois:** Valor descontado durante a resolução do dano quando sua fonte permitir. Não aumenta a Defesa. Abreviação: RD. → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#reducao` (Redução de Dano).
### Rodada

**Antes:** Passagem da ordem de iniciativa do combate. Turno é o momento de atuação de um participante dentro dela. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#turnos` (Turnos).

**Depois:** Passagem da ordem de iniciativa do combate. Turno é o momento de atuação de um participante dentro dela. → `regras-gerais/lote-final/REGRAS-GERAIS.md#turnos` (Turnos).
### Selo

**Antes:** Ato ou requisito que acompanha a conjuração de uma técnica. A rota pode usar equipamento como seu Selo. → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Passivas).

**Depois:** Ato ou requisito que acompanha a conjuração de uma técnica. A rota pode usar equipamento como seu Selo. → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Talentos).
### Talento

**Antes:** não consta como entrada independente.

**Depois:** Capacidade adquirida cujo funcionamento e investimento seguem sua Categoria de Efeito. Uma entrada reativa ainda pode exigir ação ou gatilho. → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Talentos).
### Teste de Resistência

**Antes:** Rolagem de quem tenta evitar ou encerrar um efeito. A regra indica o atributo, a CD e o resultado de sucesso ou falha. Abreviação: TR. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#resistencia` (Testes de Resistência).

**Depois:** Rolagem de quem tenta evitar ou encerrar um efeito. A regra indica o atributo, a CD e o resultado de sucesso ou falha. Abreviação: TR. → `regras-gerais/lote-final/REGRAS-GERAIS.md#resistencia` (Testes de Resistência).
### Treino

**Antes:** Qualificação registrada para perícia, ofício, TR ou equipamento. Cada tipo explica o que o treino permite. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#pericias` (Perícias e ofícios).

**Depois:** Qualificação registrada para perícia, ofício, TR ou equipamento. Cada tipo explica o que o treino permite. → `regras-gerais/lote-final/REGRAS-GERAIS.md#pericias` (Treino e modificadores).
### Turno

**Antes:** Momento de atuação de um participante. Prazos como começo do seu próximo turno se referem ao participante indicado. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#turnos` (Turnos).

**Depois:** Momento de atuação de um participante. Prazos como começo do seu próximo turno se referem ao participante indicado. → `regras-gerais/lote-final/REGRAS-GERAIS.md#turnos` (Turnos).
### Vantagem

**Antes:** Rolagem de dois d20 que usa o maior. Várias fontes não acrescentam novos dados por si. → `regras-basicas/lote-01/TESTES-E-TURNOS.md#pericias` (Perícias e ofícios).

**Depois:** Rolagem de dois d20 que usa o maior. Várias fontes não acrescentam novos dados por si. → `regras-gerais/lote-final/REGRAS-GERAIS.md#pericias` (Treino e modificadores).
### Vida temporária

**Antes:** Reserva separada dos PV atuais e máximos, sujeita aos limites e ao prazo de Recuperação. → `regras-basicas/lote-04/RECUPERACAO.md#temporarios` (Vida e energia temporárias).

**Depois:** Reserva separada dos PV atuais e máximos, sujeita aos limites e ao prazo de Dano e Recuperação. → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#temporarios` (Vida e energia temporárias).
### Volume

**Antes:** Medida de carga usada pelo inventário. É distinta de uma propriedade de manejo da arma. → `regras-comuns/lote-06-r6/MOVIMENTO-E-CARGA.md#carga` (Carga).

**Depois:** Medida de carga usada pelo inventário. É distinta de uma propriedade de manejo da arma. → `regras-gerais/lote-final/REGRAS-GERAIS.md#carga` (Carga).

## Entradas de índice alteradas

### Aguentar

**Antes:** não consta como entrada independente.

**Depois:** Dano e Recuperação: Vida a zero → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#zero` (Vida a zero).
### Ajudar

**Antes:** Testes e turnos: Perícias e ofícios → `regras-basicas/lote-01/TESTES-E-TURNOS.md#pericias` (Perícias e ofícios).

**Depois:** Regras gerais: Ajudar → `regras-gerais/lote-final/REGRAS-GERAIS.md#ajudar` (Ajudar).
### Aviso (Melhoria; nome anterior)

**Antes:** não consta como entrada independente.

**Depois:** Catálogo: Marcas e recursos → `catalogo/lote-01/CATALOGO.md#cat-marca-recursos` (Marcas e recursos).
### Aviso (Talento; nome anterior)

**Antes:** não consta como entrada independente.

**Depois:** Catálogo: Talentos de Categoria 1 → `catalogo/lote-01/CATALOGO.md#cat-passivas-1` (Talentos de Categoria 1).
### CE

**Antes:** não consta como entrada independente.

**Depois:** Fundamento: Selo e Talentos. Categoria de Efeito. → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Talentos).
### CP (sigla anterior)

**Antes:** não consta como entrada independente.

**Depois:** Fundamento: Selo e Talentos. Categoria de Efeito; sigla atual: CE. → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Talentos).
### Categoria de Efeito

**Antes:** não consta como entrada independente.

**Depois:** Fundamento: Selo e Talentos → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Talentos).
### Classe Passiva

**Antes:** Fundamento: Selo e Passivas → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Passivas).

**Depois:** não consta como entrada independente.
### Classe Passiva (nome anterior)

**Antes:** não consta como entrada independente.

**Depois:** Fundamento: Selo e Talentos → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Talentos).
### Concentração

**Antes:** Testes e turnos: Reações e concentração → `regras-basicas/lote-01/TESTES-E-TURNOS.md#reacoes` (Reações e concentração).

**Depois:** Regras gerais: Concentração → `regras-gerais/lote-final/REGRAS-GERAIS.md#concentracao` (Concentração).
### Cura

**Antes:** Fundamento: Formas de amparo e Efeito → `fundamento/lote-01/FUNDAMENTO.md#amparoformas` (Formas de amparo e Efeito).

**Depois:** não consta como entrada independente.
### Cura (Forma)

**Antes:** não consta como entrada independente.

**Depois:** Fundamento: Formas de amparo e Efeito → `fundamento/lote-01/FUNDAMENTO.md#amparoformas` (Formas de amparo e Efeito).
### Cura (recuperação)

**Antes:** não consta como entrada independente.

**Depois:** Dano e Recuperação: Cura → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#cura` (Cura).
### Derrotado

**Antes:** não consta como entrada independente.

**Depois:** Dano e Recuperação: Derrota e morte → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#derrota` (Derrota e morte).
### Desvantagem

**Antes:** Testes e turnos: Perícias e ofícios → `regras-basicas/lote-01/TESTES-E-TURNOS.md#pericias` (Perícias e ofícios).

**Depois:** Regras gerais: Treino e modificadores → `regras-gerais/lote-final/REGRAS-GERAIS.md#pericias` (Treino e modificadores).
### Estabilizar

**Antes:** não consta como entrada independente.

**Depois:** Dano e Recuperação: Socorro → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#socorro` (Socorro).
### Estágios de Integridade

**Antes:** não consta como entrada independente.

**Depois:** Dano e Recuperação: Estágios de Integridade → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#integridade` (Estágios de Integridade).
### Expressão da técnica

**Antes:** não consta como entrada independente.

**Depois:** Fundamento: Selo e Talentos → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Talentos).
### Fluxo

**Antes:** Catálogo: Passivas de Classe 2 → `catalogo/lote-01/CATALOGO.md#cat-passivas-2-recursos` (Passivas de Classe 2).

**Depois:** Catálogo: Talentos de Categoria 2 → `catalogo/lote-01/CATALOGO.md#cat-passivas-2-recursos` (Talentos de Categoria 2).
### Gatilho

**Antes:** Testes e turnos: Reações e concentração → `regras-basicas/lote-01/TESTES-E-TURNOS.md#reacoes` (Reações e concentração).

**Depois:** Regras gerais: Reações e ataques de oportunidade → `regras-gerais/lote-final/REGRAS-GERAIS.md#oportunidade` (Reações e ataques de oportunidade).
### Grau (patente)

**Antes:** Progressão: Experiência e Progressão → `progressao/lote-01/PROGRESSAO.md#prog-inicio` (Experiência e Progressão).

**Depois:** Progressão: Patentes → `progressao/lote-01/PROGRESSAO.md#prog-patentes` (Patentes).
### Guarda Aberta

**Antes:** não consta como entrada independente.

**Depois:** Dano e Recuperação: Condições leves → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#leves` (Condições leves).
### Identificar Feitiço

**Antes:** não consta como entrada independente.

**Depois:** Catálogo: Marcas e recursos → `catalogo/lote-01/CATALOGO.md#cat-marca-recursos` (Marcas e recursos).
### Incapacitado

**Antes:** Dano e Condições: Condições leves → `regras-basicas/lote-03-r3/DANO-E-CONDICOES.md#leves` (Condições leves).

**Depois:** não consta como entrada independente.
### Incapacitado (nome anterior)

**Antes:** não consta como entrada independente.

**Depois:** Dano e Recuperação: Condições leves → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#leves` (Condições leves).
### Inconsciente

**Antes:** Recuperação: Vida a zero → `regras-basicas/lote-04/RECUPERACAO.md#zero` (Vida a zero).

**Depois:** Dano e Recuperação: Inconsciente → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#inconsciente` (Inconsciente).
### Insistir

**Antes:** não consta como entrada independente.

**Depois:** Dano e Recuperação: Insistir → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#insistir` (Insistir).
### Integridade

**Antes:** Dano e Condições: Dano na alma → `regras-basicas/lote-03-r3/DANO-E-CONDICOES.md#alma` (Dano na alma).

**Depois:** Dano e Recuperação: Estágios de Integridade → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#integridade` (Estágios de Integridade).
### Integridade máxima

**Antes:** não consta como entrada independente.

**Depois:** Dano e Recuperação: Dano na alma → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#alma` (Dano na alma).
### Leitura de Feitiços

**Antes:** não consta como entrada independente.

**Depois:** Catálogo: Talentos de Categoria 1 → `catalogo/lote-01/CATALOGO.md#cat-passivas-1` (Talentos de Categoria 1).
### Mão Firme

**Antes:** Catálogo: Passivas de Classe 1 → `catalogo/lote-01/CATALOGO.md#cat-passivas-1` (Passivas de Classe 1).

**Depois:** Catálogo: Talentos de Categoria 1 → `catalogo/lote-01/CATALOGO.md#cat-passivas-1` (Talentos de Categoria 1).
### Passiva

**Antes:** Fundamento: Selo e Passivas → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Passivas).

**Depois:** não consta como entrada independente.
### Passiva (nome anterior)

**Antes:** não consta como entrada independente.

**Depois:** Fundamento: Selo e Talentos → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Talentos).
### Passiva Livre (nome anterior)

**Antes:** não consta como entrada independente.

**Depois:** Fundamento: Selo e Talentos. Expressão da técnica. → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Talentos).
### Passiva Própria

**Antes:** Catálogo: Passiva Própria → `catalogo/lote-01/CATALOGO.md#cat-passiva-propria` (Passiva Própria).

**Depois:** não consta como entrada independente.
### Passiva Própria (nome anterior)

**Antes:** não consta como entrada independente.

**Depois:** Catálogo: Talento Próprio → `catalogo/lote-01/CATALOGO.md#cat-passiva-propria` (Talento Próprio).
### Patente

**Antes:** Progressão: Experiência e Progressão → `progressao/lote-01/PROGRESSAO.md#prog-inicio` (Experiência e Progressão).

**Depois:** Progressão: Patentes → `progressao/lote-01/PROGRESSAO.md#prog-patentes` (Patentes).
### Reação

**Antes:** Testes e turnos: Reações e concentração → `regras-basicas/lote-01/TESTES-E-TURNOS.md#reacoes` (Reações e concentração).

**Depois:** Regras gerais: Reações e ataques de oportunidade → `regras-gerais/lote-final/REGRAS-GERAIS.md#oportunidade` (Reações e ataques de oportunidade).
### Selo

**Antes:** Fundamento: Selo e Passivas → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Passivas).

**Depois:** Fundamento: Selo e Talentos → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Talentos).
### Sentir Energia

**Antes:** Energia e seus sinais → `regras-comuns/consolidado-r1/REGRAS-COMUNS.md#mundo` (Energia e seus sinais).

**Depois:** Regras gerais: Percepção de energia → `regras-gerais/lote-final/REGRAS-GERAIS.md#mundo` (Percepção de energia).
### Socorro

**Antes:** não consta como entrada independente.

**Depois:** Dano e Recuperação: Socorro → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md#socorro` (Socorro).
### Talento

**Antes:** não consta como entrada independente.

**Depois:** Fundamento: Selo e Talentos → `fundamento/lote-01/FUNDAMENTO.md#selo` (Selo e Talentos).
### Talento Próprio

**Antes:** não consta como entrada independente.

**Depois:** Catálogo: Talento Próprio → `catalogo/lote-01/CATALOGO.md#cat-passiva-propria` (Talento Próprio).
### Treino

**Antes:** Testes e turnos: Perícias e ofícios → `regras-basicas/lote-01/TESTES-E-TURNOS.md#pericias` (Perícias e ofícios).

**Depois:** Regras gerais: Treino e modificadores → `regras-gerais/lote-final/REGRAS-GERAIS.md#pericias` (Treino e modificadores).
### Vantagem

**Antes:** Testes e turnos: Perícias e ofícios → `regras-basicas/lote-01/TESTES-E-TURNOS.md#pericias` (Perícias e ofícios).

**Depois:** Regras gerais: Treino e modificadores → `regras-gerais/lote-final/REGRAS-GERAIS.md#pericias` (Treino e modificadores).
### Volumosa

**Antes:** Equipamento: Propriedades → `equipamento/lote-01-r5/EQUIPAMENTO-EM-JOGO.md#propriedades` (Propriedades).

**Depois:** Equipamento: Armas escondidas → `equipamento/lote-final/EQUIPAMENTO.md#eq-oculta` (Armas escondidas).

**Remissão conservada, dono consolidado:** `regras-basicas/lote-03-r3/DANO-E-CONDICOES.md` → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md`. Títulos iguais; âncoras conferidas pelo mapa. Entradas: Agarrado, Amedrontado, Atordoado, Calado, Cego, Condição, Dano na alma, Derrubado, Desarmado, Energia amaldiçoada pura (dano), Enfeitiçado, Envenenado, Força (dano), Impedido, Lento, PV, Pontos de vida, Redução de Dano, Surdo.

**Remissão conservada, dono consolidado:** `regras-comuns/consolidado-r1/REGRAS-COMUNS.md` → `regras-gerais/lote-final/REGRAS-GERAIS.md`. Títulos iguais; âncoras conferidas pelo mapa. Entradas: Agarrar, Deslocamento, Esconder, Estudar, Movimento imposto, Preparar, Quedas, Saltos, Vasculhar.

**Remissão conservada, dono consolidado:** `regras-basicas/lote-02/ATAQUES-E-DEFESA.md` → `regras-gerais/lote-final/REGRAS-GERAIS.md`. Títulos iguais; âncoras conferidas pelo mapa. Entradas: Aparar, Atacar, Ataque, Bloquear, Brecha, Cobertura, Crítico, Defesa.

**Remissão conservada, dono consolidado:** `regras-basicas/lote-01/TESTES-E-TURNOS.md` → `regras-gerais/lote-final/REGRAS-GERAIS.md`. Títulos iguais; âncoras conferidas pelo mapa. Entradas: Atributo, Ação, Ação Bônus, Ação Completa, Ação Padrão, Ação de Movimento, CD, Essência, Força (atributo), Maestria, Rodada, Rodada inteira, Teste, Teste de Resistência, Turno.

**Remissão conservada, dono consolidado:** `regras-comuns/lote-06-r6/MOVIMENTO-E-CARGA.md` → `regras-gerais/lote-final/REGRAS-GERAIS.md`. Títulos iguais; âncoras conferidas pelo mapa. Entradas: Carga, Volume.

**Remissão conservada, dono consolidado:** `regras-basicas/lote-04/RECUPERACAO.md` → `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md`. Títulos iguais; âncoras conferidas pelo mapa. Entradas: Cena, Cicatriz, Energia temporária, Exaustão, Morrendo, Sequela, Vida temporária.

**Remissão conservada, dono consolidado:** `equipamento/lote-08/EQUIPAMENTO-AMALDICOADO.md` → `equipamento/lote-final/EQUIPAMENTO.md`. Títulos iguais; âncoras conferidas pelo mapa. Entradas: Desgaste, Estigma, Ferramenta amaldiçoada, Grau.

**Remissão conservada, dono consolidado:** `equipamento/lote-01-r5/EQUIPAMENTO-EM-JOGO.md` → `equipamento/lote-final/EQUIPAMENTO.md`. Títulos iguais; âncoras conferidas pelo mapa. Entradas: Emaranha, Fineza, Inventário, Longo Alcance, Oculta, Par, Rompe, Talha, Versátil, Vestida.

**Remissão conservada, dono consolidado:** `equipamento/lote-03-r5/MUNICAO.md` → `equipamento/lote-final/EQUIPAMENTO.md`. Títulos iguais; âncoras conferidas pelo mapa. Entradas: Munição.

**Remissão conservada, dono consolidado:** `equipamento/lote-02-r3/PROTECAO.md` → `equipamento/lote-final/EQUIPAMENTO.md`. Títulos iguais; âncoras conferidas pelo mapa. Entradas: Proteção.

## Rótulos do índice

Retirado o número técnico e o intervalo de letra repetida. Títulos atuais: Índice: A; Índice: A–C; Índice: C–D; Índice: D–E; Índice: E–G; Índice: G–L; Índice: L–O; Índice: O–P; Índice: P–S; Índice: S–V; Índice: V–X. IDs internos preservados.

## Donos conferidos

Estados e ficha: Dano e Recuperação final `b4035a501c87ada84e73e5951cdf41639c850d644cfe4cb8812575d8a0bc1c43`. Patentes: `prog-patentes`. Regras comuns: `regras-gerais/lote-final/REGRAS-GERAIS.md`. Equipamento: mapa de âncoras de `equipamento/lote-final/FONTES.json`. Nomes atuais: pauta de `consolidacao/lote-01/migracao-nomes/MIGRACAO.json`. As três definições de estado não copiam números; a ficha apenas registra valores.

Auditoria atual:994 verificações,48 casos dirigidos; inclui existência e seleção de todos os destinos em ORDEM.json. Esses testes não substituem leitura humana nem confirmam balanceamento de regra nova; R23 não altera valores.
