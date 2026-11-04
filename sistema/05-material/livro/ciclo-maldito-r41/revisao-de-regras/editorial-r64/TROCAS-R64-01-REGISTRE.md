# R64 | Registre e registrem

Proposta para aprovação. 139 ocorrências em 138 trechos da R63 (8e7e83bb).

Fonte conferida: `LIVRO-COMPLETO.md` (SHA-256 `0e3cacedfa8368ae2b1542e3ba55ac3e3da532a4bf15550bc7dba490aae634bb`).

O antes e o depois mostram o trecho completo da fonte. Os números de linha são os da R63.
Em sete trechos, as duas listas propõem mudanças na mesma linha. Cada lista mostra sua troca isolada, e a aplicação conjunta foi simulada em memória.

## Títulos para aprovação

- **R64-R-067** · **Registre as consequências** → **Anote as consequências**
- **R64-R-072** · **Registre a ficha** → **Preencha a ficha**

As duas mudanças de título estão incluídas no total acima e também aparecem nos seus capítulos. Os rótulos de Requisito ficam como estão.

## 2. Regras gerais

### R64-R-001

`geral--turnos` · linha 271

**Antes**

~~~~text
Em empate, age primeiro quem tiver maior Destreza. Se ela também empatar entre jogador e inimigo, o jogador age primeiro. Entre personagens dos jogadores ainda empatados, os envolvidos escolhem a ordem; entre inimigos, o mestre escolhe. Registre a ordem uma vez para o combate. Uma habilidade que antecipe ou altere um turno segue suas próprias regras.
~~~~

**Depois**

~~~~text
Em empate, age primeiro quem tiver maior Destreza. Se ela também empatar entre jogador e inimigo, o jogador age primeiro. Entre personagens dos jogadores ainda empatados, os envolvidos escolhem a ordem; entre inimigos, o mestre escolhe. Anote a ordem uma vez para o combate. Uma habilidade que antecipe ou altere um turno segue suas próprias regras.
~~~~

### R64-R-002

`geral--voo` · linha 956

**Antes**

~~~~text
Use a Ação de Movimento e as demais permissões habituais para gastar seus metros de voo. Subir, avançar e descer voluntariamente consomem movimento. Registre a altura na escala de **1,5 m** quando ela afetar alcance, obstáculos ou uma possível queda.
~~~~

**Depois**

~~~~text
Use a Ação de Movimento e as demais permissões habituais para gastar seus metros de voo. Subir, avançar e descer voluntariamente consomem movimento. Anote a altura na escala de **1,5 m** quando ela afetar alcance, obstáculos ou uma possível queda.
~~~~

## 3. Dano e recuperação

### R64-R-003

`dano--condicoes` · linha 1486

**Antes**

~~~~text
Uma **condição** altera o que você consegue fazer enquanto durar. Registre seu nome, a fonte, o momento em que termina e os testes ou ações que permitem encerrá-la. As treze condições classificadas como Leves, Médias ou Pesadas têm efeitos próprios; uma condição não inclui outra só porque seus nomes parecem relacionados.
~~~~

**Depois**

~~~~text
Uma **condição** altera o que você consegue fazer enquanto durar. Anote seu nome, a fonte, o momento em que termina e os testes ou ações que permitem encerrá-la. As treze condições classificadas como Leves, Médias ou Pesadas têm efeitos próprios; uma condição não inclui outra só porque seus nomes parecem relacionados.
~~~~

### R64-R-004

`dano--condicoes` · linha 1504

**Antes**

~~~~text
Receber **a mesma condição** novamente não intensifica seus efeitos. Registre as fontes e durações separadamente; ela permanece enquanto pelo menos uma aplicação estiver ativa. Escapar de um agarrão não remove outro. Uma habilidade que remova a condição por inteiro segue sua própria permissão.
~~~~

**Depois**

~~~~text
Receber **a mesma condição** novamente não intensifica seus efeitos. Anote as fontes e durações separadamente; ela permanece enquanto pelo menos uma aplicação estiver ativa. Escapar de um agarrão não remove outro. Uma habilidade que remova a condição por inteiro segue sua própria permissão.
~~~~

### R64-R-005

`dano--pesadas` · linha 1628 · Também consta na outra lista

**Antes**

~~~~text
O TR mantém os modificadores aplicáveis enquanto a condição existir. Se Impedido exigir TR Físico para terminar, a tentativa tem desvantagem. Envenenado não prejudica um TR de Vigor por si. Registre na ficha do efeito **qual TR e qual CD** resolvem a saída, conforme as regras de [Condições](#dano--condicoes).
~~~~

**Depois**

~~~~text
O TR mantém os modificadores aplicáveis enquanto a condição existir. Se Impedido exigir TR Físico para terminar, a tentativa tem desvantagem. Envenenado não prejudica um TR de Vigor por si. Anote na ficha do efeito **qual TR e qual CD** resolvem a saída, conforme as regras de [Condições](#dano--condicoes).
~~~~

### R64-R-006

`dano--zero` · linha 1695

**Antes**

~~~~text
Anote a vida máxima que tinha ao cair, sem vida temporária. Esse é o **máximo de referência** até aquela queda terminar. Registre também o tratamento necessário, o tratamento já recebido e sua janela de socorro.
~~~~

**Depois**

~~~~text
Anote a vida máxima que tinha ao cair, sem vida temporária. Esse é o **máximo de referência** até aquela queda terminar. Anote também o tratamento necessário, o tratamento já recebido e sua janela de socorro.
~~~~

### R64-R-007

`dano--sequelas` · linha 1787 · Também consta na outra lista

**Antes**

~~~~text
Sair de uma queda por chegar a zero de vida deixa **uma Sequela**. Registre-a quando o socorro encerrar a queda, inclusive com cura própria, uma exceção ao tratamento necessário ou a recuperação segura depois de estabilizar. A Sequela nova afeta a próxima queda. Se ficar Derrotado, registre-a ao sair desse estado, conforme Derrota e morte.
~~~~

**Depois**

~~~~text
Sair de uma queda por chegar a zero de vida deixa **uma Sequela**. Marque-a quando o socorro encerrar a queda, inclusive com cura própria, uma exceção ao tratamento necessário ou a recuperação segura depois de estabilizar. A Sequela nova afeta a próxima queda. Se ficar Derrotado, marque-a ao sair desse estado, conforme Derrota e morte.
~~~~

### R64-R-008

`dano--sequelas` · linha 1796

**Antes**

~~~~text
Sequelas não penalizam ataques, perícias ou TRs. Elas são removidas no descanso longo: resolva primeiro a recuperação e registre a Sequela se ela encerrar a queda ou a derrota por vida a zero; depois, remova todas as Sequelas, inclusive essa. Cura comum não as remove. Receber mais cura quando já está acima de zero não acrescenta Sequela.
~~~~

**Depois**

~~~~text
Sequelas não penalizam ataques, perícias ou TRs. Elas são removidas no descanso longo: resolva primeiro a recuperação e marque a Sequela se ela encerrar a queda ou a derrota por vida a zero; depois, remova todas as Sequelas, inclusive essa. Cura comum não as remove. Receber mais cura quando já está acima de zero não acrescenta Sequela.
~~~~

### R64-R-009

`dano--sequelas` · linha 1802

**Antes**

~~~~text
Ferimentos graves podem deixar marcas duradouras. Depois da segunda queda na mesma missão, registre com o mestre se houve uma cicatriz e como ela ficou. Ela faz parte da aparência e da história do personagem.
~~~~

**Depois**

~~~~text
Ferimentos graves podem deixar marcas duradouras. Depois da segunda queda na mesma missão, anote com o mestre se houve uma cicatriz e como ela ficou. Ela faz parte da aparência e da história do personagem.
~~~~

### R64-R-010

`dano--descansos` · linha 1885

**Antes**

~~~~text
Resolva primeiro a recuperação. Se ela encerrar uma queda ou uma derrota por vida a zero, registre a Sequela correspondente; depois, remova todas as Sequelas, inclusive essa.
~~~~

**Depois**

~~~~text
Resolva primeiro a recuperação. Se ela encerrar uma queda ou uma derrota por vida a zero, marque a Sequela correspondente; depois, remova todas as Sequelas, inclusive essa.
~~~~

### R64-R-011

`dano--exaustao` · linha 1897

**Antes**

~~~~text
**Da quarta luta do dia em diante, cada luta acrescenta um degrau de Exaustão, até o máximo de três.** Registre o total ao terminar cada confronto. A primeira, a segunda e a terceira luta não acrescentam degraus por essa regra.
~~~~

**Depois**

~~~~text
**Da quarta luta do dia em diante, cada luta acrescenta um degrau de Exaustão, até o máximo de três.** Anote o total ao terminar cada confronto. A primeira, a segunda e a terceira luta não acrescentam degraus por essa regra.
~~~~

## 4. Criar um personagem

### R64-R-012

`ab--ab-criacao` · linha 1982

**Antes**

~~~~text
| 2. Origem | Escolha a Origem e duas menores permitidas; registre história, marcante e treinos. |
~~~~

**Depois**

~~~~text
| 2. Origem | Escolha a Origem e duas menores permitidas; anote história, marcante e treinos. |
~~~~

### R64-R-013

`ab--ab-criacao` · linha 1986

**Antes**

~~~~text
| 6. Ficha | Calcule os valores, confira escolhas e registre recursos. |
~~~~

**Depois**

~~~~text
| 6. Ficha | Calcule os valores, confira escolhas e anote recursos. |
~~~~

### R64-R-014

`ab--ab-origem` · linha 2004

**Antes**

~~~~text
Escolha **uma Origem** no capítulo de Origens. Leia sua entrada inteira e registre a base de treinos, um **traço** (detalhe importante da sua história), uma **marcante** (capacidade central da Origem) e **duas menores permitidas** (capacidades complementares de seu catálogo). Legados de história registram vínculos e acontecimentos, sem conceder benefícios mecânicos nem consumir essas escolhas. Sem Técnica é uma opção separada, disponível somente às Origens indicadas.
~~~~

**Depois**

~~~~text
Escolha **uma Origem** no capítulo de Origens. Leia sua entrada inteira e anote a base de treinos, um **traço** (detalhe importante da sua história), uma **marcante** (capacidade central da Origem) e **duas menores permitidas** (capacidades complementares de seu catálogo). Legados de história registram vínculos e acontecimentos, sem conceder benefícios mecânicos nem consumir essas escolhas. Sem Técnica é uma opção separada, disponível somente às Origens indicadas.
~~~~

### R64-R-015

`ab--ab-caminho` · linha 2043

**Antes**

~~~~text
Leia **Características** e **Progressão** no Caminho escolhido. Registre os treinos, a vida, os **pontos de energia (PE)** e as habilidades recebidas no seu nível. Depois faça o mesmo com a Trilha. As descrições completas permanecem nas respectivas entradas para consulta durante a sessão.
~~~~

**Depois**

~~~~text
Leia **Características** e **Progressão** no Caminho escolhido. Anote os treinos, a vida, os **pontos de energia (PE)** e as habilidades recebidas no seu nível. Depois faça o mesmo com a Trilha. As descrições completas permanecem nas respectivas entradas para consulta durante a sessão.
~~~~

### R64-R-016

`ab--ab-caminho` · linha 2055

**Antes**

~~~~text
Na criação de nível 1, registre as características iniciais do Caminho. Você recebe as habilidades e a primeira Trilha do nível 2 quando chegar a esse nível. Escolhê-las com antecedência não permite usá-las antes.
~~~~

**Depois**

~~~~text
Na criação de nível 1, anote as características iniciais do Caminho. Você recebe as habilidades e a primeira Trilha do nível 2 quando chegar a esse nível. Escolhê-las com antecedência não permite usá-las antes.
~~~~

### R64-R-017

`ab--ab-capacidades` · linha 2089

**Antes**

~~~~text
Registre os valores que usa com frequência e onde consultar as demais regras. Quando uma habilidade modificar outra, anote a alteração na ficha correspondente. Isso evita esquecer um custo ou somar o mesmo benefício duas vezes.
~~~~

**Depois**

~~~~text
Anote os valores que usa com frequência e onde consultar as demais regras. Quando uma habilidade modificar outra, anote a alteração na ficha correspondente. Isso evita esquecer um custo ou somar o mesmo benefício duas vezes.
~~~~

### R64-R-018

`ab--ab-equipamento` · linha 2099

**Antes**

~~~~text
Na criação padrão, você recebe **um Traje 1 e ¥150.000** para comprar os demais itens. O Traje é um uniforme leve que concede proteção à Defesa e favorece testes numa situação escolhida, como água e chuva. Registre a situação, o tipo de TR e as perícias beneficiados seguindo [Trajes](#equip--eqp-traje), em Equipamento. Use Equipamento inicial para montar o inventário e conferir acesso, preços de criação e fornecimento de munição.
~~~~

**Depois**

~~~~text
Na criação padrão, você recebe **um Traje 1 e ¥150.000** para comprar os demais itens. O Traje é um uniforme leve que concede proteção à Defesa e favorece testes numa situação escolhida, como água e chuva. Anote a situação, o tipo de TR e as perícias beneficiados seguindo [Trajes](#equip--eqp-traje), em Equipamento. Use Equipamento inicial para montar o inventário e conferir acesso, preços de criação e fornecimento de munição.
~~~~

### R64-R-019

`ab--ab-conferencia` · linha 2236

**Antes**

~~~~text
Ao terminar, registre as recompensas, os gastos e as consequências que persistem. Confira descanso e recuperação antes de restaurar recursos. Se jogar numa guilda, use o procedimento de registro da comunidade para que a próxima mesa receba a ficha atualizada.
~~~~

**Depois**

~~~~text
Ao terminar, anote as recompensas, os gastos e as consequências que persistem. Confira descanso e recuperação antes de restaurar recursos. Se jogar numa guilda, use o procedimento de registro da comunidade para que a próxima mesa receba a ficha atualizada.
~~~~

## 5. Origens

### R64-R-020

`origens--legados` · linha 2306

**Antes**

~~~~text
Algumas histórias permitem escolher capacidades específicas. **Manutenção**, por exemplo, dá acesso a duas menores do Corpo Amaldiçoado: registre a história e a capacidade que escolher. A história não gasta vaga; cada menor escolhida ocupa uma das duas vagas normais.
~~~~

**Depois**

~~~~text
Algumas histórias permitem escolher capacidades específicas. **Manutenção**, por exemplo, dá acesso a duas menores do Corpo Amaldiçoado: anote a história e a capacidade que escolher. A história não gasta vaga; cada menor escolhida ocupa uma das duas vagas normais.
~~~~

### R64-R-021

`origens--origem-latente` · linha 2324

**Antes**

~~~~text
**Legados de história:** talvez você ainda procure o professor que nunca conseguiu encontrar, confie seu segredo a alguém de fora do jujutsu ou tenha deixado um erro do aprendizado sem reparação. Registre quem participou disso e por que essa relação ainda importa. Seus ofícios podem vir do trabalho, da família ou dos recursos que usou para se virar.
~~~~

**Depois**

~~~~text
**Legados de história:** talvez você ainda procure o professor que nunca conseguiu encontrar, confie seu segredo a alguém de fora do jujutsu ou tenha deixado um erro do aprendizado sem reparação. Anote quem participou disso e por que essa relação ainda importa. Seus ofícios podem vir do trabalho, da família ou dos recursos que usou para se virar.
~~~~

### R64-R-022

`origens--origem-receptaculo` · linha 2398

**Antes**

~~~~text
**Legados de história:** o nome antigo do passageiro pode levar até alguém que o conheceu antes de você. Um desejo dele pode contrariar o seu, enquanto uma instituição acompanha o que acontece com vocês. Escolha o que faz parte dessa convivência e registre como se relacionam e o que sabem um do outro.
~~~~

**Depois**

~~~~text
**Legados de história:** o nome antigo do passageiro pode levar até alguém que o conheceu antes de você. Um desejo dele pode contrariar o seu, enquanto uma instituição acompanha o que acontece com vocês. Escolha o que faz parte dessa convivência e anote como se relacionam e o que sabem um do outro.
~~~~

### R64-R-023

`origens--receptaculo-excecoes` · linha 2482

**Antes**

~~~~text
A disputa entre hospedeiro e ocupante é conduzida pela história combinada na mesa. Não há rotina automática de testes, limite de vida ou PE, ou falha desta Origem que entregue o controle do personagem. O livro de mestres aprofundará essa relação. Registre os acordos e mudanças que acontecerem na campanha sem acrescentar poderes à ficha por conta própria.
~~~~

**Depois**

~~~~text
A disputa entre hospedeiro e ocupante é conduzida pela história combinada na mesa. Não há rotina automática de testes, limite de vida ou PE, ou falha desta Origem que entregue o controle do personagem. O livro de mestres aprofundará essa relação. Anote os acordos e mudanças que acontecerem na campanha sem acrescentar poderes à ficha por conta própria.
~~~~

### R64-R-024

`origens--descendente-gojo` · linha 2556

**Antes**

~~~~text
Escolha **feitiços ou Manejos conhecidos em quantidade total igual à Maestria** e registre a lista. **Maestria vezes por dia**, ao usar uma dessas capacidades, antes dos dados, escolha um benefício:
~~~~

**Depois**

~~~~text
Escolha **feitiços ou Manejos conhecidos em quantidade total igual à Maestria** e anote a lista. **Maestria vezes por dia**, ao usar uma dessas capacidades, antes dos dados, escolha um benefício:
~~~~

### R64-R-025

`origens--origem-corpo` · linha 2843

**Antes**

~~~~text
Na criação, escolha o **ofício compatível com seu corpo** e registre-o na ficha. Por exemplo: Entalhador para madeira, pedra ou osso; Forja para metal; Alfaiate para pano. A lista não é fechada. O ofício deve corresponder ao trabalho necessário para reparar sua estrutura, sem cobrar automaticamente todos os ofícios dos materiais presentes. Anotar o ofício compatível identifica o treino exigido de quem repara; para fazer seu próprio reparo, você também precisa adquirir esse treino pelas escolhas da ficha.
~~~~

**Depois**

~~~~text
Na criação, escolha o **ofício compatível com seu corpo** e anote-o na ficha. Por exemplo: Entalhador para madeira, pedra ou osso; Forja para metal; Alfaiate para pano. A lista não é fechada. O ofício deve corresponder ao trabalho necessário para reparar sua estrutura, sem cobrar automaticamente todos os ofícios dos materiais presentes. Anotar o ofício compatível identifica o treino exigido de quem repara; para fazer seu próprio reparo, você também precisa adquirir esse treino pelas escolhas da ficha.
~~~~

### R64-R-026

`origens--corpo-configuracoes` · linha 2857

**Antes**

~~~~text
**Inteiro.** Você despertou com um único núcleo. Registre o que sabe sobre a criação e o que ainda deseja descobrir.
~~~~

**Depois**

~~~~text
**Inteiro.** Você despertou com um único núcleo. Anote o que sabe sobre a criação e o que ainda deseja descobrir.
~~~~

### R64-R-027

`origens--corpo-ninhada-gemeos` · linha 2951

**Antes**

~~~~text
Registre **três perícias ou Ofícios**. Você mantém **treino em um deles por vez**. Durante um descanso curto ou longo, pode trocar uma vez o procedimento ativo; a mudança entra em vigor ao concluir o descanso, sem PE, teste ou material adicional apenas para selecioná-lo.
~~~~

**Depois**

~~~~text
Anote **três perícias ou Ofícios**. Você mantém **treino em um deles por vez**. Durante um descanso curto ou longo, pode trocar uma vez o procedimento ativo; a mudança entra em vigor ao concluir o descanso, sem PE, teste ou material adicional apenas para selecioná-lo.
~~~~

### R64-R-028

`origens--restricao-prenuncio` · linha 3053

**Antes**

~~~~text
Registre ataques comuns por **tipo ou perfil de arma**, não por exemplar. Outra cópia equivalente não renova a novidade. Ataques comuns desarmados formam um único perfil: trocar soco por chute não o torna inédito.
~~~~

**Depois**

~~~~text
Anote ataques comuns por **tipo ou perfil de arma**, não por exemplar. Outra cópia equivalente não renova a novidade. Ataques comuns desarmados formam um único perfil: trocar soco por chute não o torna inédito.
~~~~

### R64-R-029

`origens--restricao-corpo` · linha 3131

**Antes**

~~~~text
Registre as regras combinadas, os cuidados necessários e os meios de lidar com a condição. Os três corpos apresentados são alternativas completas, não penalidades acumuladas para comprar mais ganhos.
~~~~

**Depois**

~~~~text
Anote as regras combinadas, os cuidados necessários e os meios de lidar com a condição. Os três corpos apresentados são alternativas completas, não penalidades acumuladas para comprar mais ganhos.
~~~~

### R64-R-030

`origens--restricao-ce4` · linha 3153

**Antes**

~~~~text
As três ideias abaixo servem para criar o CE4 com o mestre. Registrem a operação e os limites antes de usá-lo; o conceito sozinho não fornece uma capacidade completa.
~~~~

**Depois**

~~~~text
As três ideias abaixo servem para criar o CE4 com o mestre. Anotem a operação e os limites antes de usá-lo; o conceito sozinho não fornece uma capacidade completa.
~~~~

### R64-R-031

`origens--restricao-menores-corporais` · linha 3245

**Antes**

~~~~text
Jogador e mestre definem **quanto pode ser guardado em cada ocasião, quando e em quais condições o armazenamento pode ocorrer e o máximo acumulável**. Registre esses limites e condições na ficha.
~~~~

**Depois**

~~~~text
Jogador e mestre definem **quanto pode ser guardado em cada ocasião, quando e em quais condições o armazenamento pode ocorrer e o máximo acumulável**. Anote esses limites e condições na ficha.
~~~~

### R64-R-032

`origens--legado-criar` · linha 3297

**Antes**

~~~~text
Você pode criar com o mestre menores compatíveis com sua Origem, usando as entradas publicadas como referência. A marcante segue as opções publicadas para sua Origem; a exceção é a criação prevista em **Criar sua Restrição**, no ramo **Restrição corporal**. Registrem o pacote antes da primeira sessão: **base, uma marcante e duas menores**. A personalização pode alcançar ambas as menores; não exige escolher uma opção pronta primeiro.
~~~~

**Depois**

~~~~text
Você pode criar com o mestre menores compatíveis com sua Origem, usando as entradas publicadas como referência. A marcante segue as opções publicadas para sua Origem; a exceção é a criação prevista em **Criar sua Restrição**, no ramo **Restrição corporal**. Anotem o pacote antes da primeira sessão: **base, uma marcante e duas menores**. A personalização pode alcançar ambas as menores; não exige escolher uma opção pronta primeiro.
~~~~

### R64-R-033

`origens--legados-exemplos` · linha 3331

**Antes**

~~~~text
Registre também os campos particulares: ofício de um corpo, competências da Reserva de Experiência, companheiro de Entendimento Tácito, limites do CE4 ou cuidados da Restrição. Use a regra completa de cada entrada para resolver o efeito.
~~~~

**Depois**

~~~~text
Anote também os campos particulares: ofício de um corpo, competências da Reserva de Experiência, companheiro de Entendimento Tácito, limites do CE4 ou cuidados da Restrição. Use a regra completa de cada entrada para resolver o efeito.
~~~~

## 6. Caminhos e Trilhas

### R64-R-034

`capitulo-6` · linha 3340

**Antes**

~~~~text
Leia primeiro a apresentação do Caminho e suas Características. A tabela de Progressão indica quando cada habilidade chega; as entradas seguintes explicam como usá-la. Depois escolha uma das Trilhas apresentadas para ele e registre os benefícios do seu nível. Os treinos da tabela e a aquisição do equipamento são conferidos separadamente.
~~~~

**Depois**

~~~~text
Leia primeiro a apresentação do Caminho e suas Características. A tabela de Progressão indica quando cada habilidade chega; as entradas seguintes explicam como usá-la. Depois escolha uma das Trilhas apresentadas para ele e anote os benefícios do seu nível. Os treinos da tabela e a aquisição do equipamento são conferidos separadamente.
~~~~

### R64-R-035

`vanguarda--van-base` · linha 3691

**Antes**

~~~~text
Registre os treinos na criação. As opções estão em **Perícias e Ofícios**.
~~~~

**Depois**

~~~~text
Anote os treinos na criação. As opções estão em **Perícias e Ofícios**.
~~~~

### R64-R-036

`emanador--ema-familiares` · linha 4909

**Antes**

~~~~text
Escolha **dois feitiços conhecidos de Classe 1 ou maior**. Registre para cada um uma versão alternativa feita por uma Remodelagem, com efeitos, dados e custos calculados.
~~~~

**Depois**

~~~~text
Escolha **dois feitiços conhecidos de Classe 1 ou maior**. Anote para cada um uma versão alternativa feita por uma Remodelagem, com efeitos, dados e custos calculados.
~~~~

### R64-R-037

`emanador--ema-eco` · linha 5163

**Antes**

~~~~text
Depois de resolver um feitiço de **Classe 1 ou maior com Desdobramento**, guarde uma alteração realmente feita: a Melhoria obtida por Remodelar ou a Modulação Forçada. Registre qual peça foi obtida e por qual dessas maneiras.
~~~~

**Depois**

~~~~text
Depois de resolver um feitiço de **Classe 1 ou maior com Desdobramento**, guarde uma alteração realmente feita: a Melhoria obtida por Remodelar ou a Modulação Forçada. Anote qual peça foi obtida e por qual dessas maneiras.
~~~~

### R64-R-038

`emanador--ema-acorde` · linha 5233

**Antes**

~~~~text
Registre para cada Eco a peça, se veio de Remodelagem ou Modulação, e o prazo. Duas cópias da mesma peça pela mesma maneira não ocupam dois lugares. Troca de Forma e troca de Melhoria continuam sujeitas aos limites de categoria do Eco.
~~~~

**Depois**

~~~~text
Anote para cada Eco a peça, se veio de Remodelagem ou Modulação, e o prazo. Duas cópias da mesma peça pela mesma maneira não ocupam dois lugares. Troca de Forma e troca de Melhoria continuam sujeitas aos limites de categoria do Eco.
~~~~

### R64-R-039

`evocador--ev-usos` · linha 5411

**Antes**

~~~~text
Os usos pertencem ao conjunto. Registre cada benefício quando ele for aproveitado.
~~~~

**Depois**

~~~~text
Os usos pertencem ao conjunto. Anote cada benefício quando ele for aproveitado.
~~~~

### R64-R-040

`evocador--ev-complementar` · linha 5594

**Antes**

~~~~text
Para receber os benefícios dos aprimoramentos, essa execução conta como uma básica. Registre o uso da habilidade no conjunto, separado das básicas individuais.
~~~~

**Depois**

~~~~text
Para receber os benefícios dos aprimoramentos, essa execução conta como uma básica. Anote o uso da habilidade no conjunto, separado das básicas individuais.
~~~~

### R64-R-041

`evocador--ev-principal` · linha 5682

**Antes**

~~~~text
Registre na ficha de cada possível principal os acréscimos da Trilha. Quando uma capacidade tiver versão comum e versão ampliada, anote ambas e use a correspondente à situação em campo. Efeitos já resolvidos seguem suas próprias durações.
~~~~

**Depois**

~~~~text
Anote na ficha de cada possível principal os acréscimos da Trilha. Quando uma capacidade tiver versão comum e versão ampliada, anote ambas e use a correspondente à situação em campo. Efeitos já resolvidos seguem suas próprias durações.
~~~~

### R64-R-042

`evocador--ev-principal-especial` · linha 5728

**Antes**

~~~~text
Registre seus efeitos, requisitos e custos. A básica continua sendo Classe 0, com a escala do nível da entidade. A especial respeita a maior Classe permitida por esse nível. Todo talento concedido por Repertório Ampliado é de **Categoria de Efeito 1**, inclusive nas escolhas dos níveis 16 e 24. Escolha entre os talentos permitidos para entidades em **Criar uma invocação**, cumprindo seus requisitos. As escolhas seguem os procedimentos normais de revisão da ficha.
~~~~

**Depois**

~~~~text
Anote seus efeitos, requisitos e custos. A básica continua sendo Classe 0, com a escala do nível da entidade. A especial respeita a maior Classe permitida por esse nível. Todo talento concedido por Repertório Ampliado é de **Categoria de Efeito 1**, inclusive nas escolhas dos níveis 16 e 24. Escolha entre os talentos permitidos para entidades em **Criar uma invocação**, cumprindo seus requisitos. As escolhas seguem os procedimentos normais de revisão da ficha.
~~~~

### R64-R-043

`evocador--ev-parceria` · linha 5908

**Antes**

~~~~text
Registre a escolha e as capacidades compatíveis com a definição da entidade. As quantidades normais de capacidades e talentos seguem o construtor.
~~~~

**Depois**

~~~~text
Anote a escolha e as capacidades compatíveis com a definição da entidade. As quantidades normais de capacidades e talentos seguem o construtor.
~~~~

### R64-R-044

`evocador--ev-parceria-aprimoramentos` · linha 5938

**Antes**

~~~~text
Resolva uma rolagem e o dano de seu ataque. Registre a básica da entidade como gasta e o uso ofensivo do aprimoramento no conjunto.
~~~~

**Depois**

~~~~text
Resolva uma rolagem e o dano de seu ataque. Marque a básica da entidade como gasta e o uso ofensivo do aprimoramento no conjunto.
~~~~

### R64-R-045

`evocador--ev-multiplas` · linha 6131

**Antes**

~~~~text
Registre a escolha e as capacidades que respeitem a definição da entidade.
~~~~

**Depois**

~~~~text
Anote a escolha e as capacidades que respeitem a definição da entidade.
~~~~

### R64-R-046

`evocador--ev-multiplas-duplas` · linha 6181

**Antes**

~~~~text
Cada dupla ocupa uma vaga do repertório. Suas entidades têm fichas separadas, com capacidades e recursos próprios. Reescrever um espaço ocupado ao subir de nível usa a revisão comum daquele espaço, incluindo a dupla ligada a ele. Registre os dois primeiros espaços beneficiados. Trocar as entidades desses espaços não concede novas duplas a vagas posteriores.
~~~~

**Depois**

~~~~text
Cada dupla ocupa uma vaga do repertório. Suas entidades têm fichas separadas, com capacidades e recursos próprios. Reescrever um espaço ocupado ao subir de nível usa a revisão comum daquele espaço, incluindo a dupla ligada a ele. Anote os dois primeiros espaços beneficiados. Trocar as entidades desses espaços não concede novas duplas a vagas posteriores.
~~~~

### R64-R-047

`evocador--ev-multiplas-repertorio` · linha 6340

**Antes**

~~~~text
Registre as escolhas na ficha. Ao entrar ou ser substituída, a invocação utiliza esse repertório registrado. A capacidade é executada com suas ações, PE, requisitos e limites próprios.
~~~~

**Depois**

~~~~text
Anote as escolhas na ficha. Ao entrar ou ser substituída, a invocação utiliza esse repertório registrado. A capacidade é executada com suas ações, PE, requisitos e limites próprios.
~~~~

## 7. Perícias e Ofícios

### R64-R-048

`pericias--fabricacao` · linha 7415

**Antes**

~~~~text
Registre os pontos abaixo antes de gastar dinheiro ou materiais.
~~~~

**Depois**

~~~~text
Anote os pontos abaixo antes de gastar dinheiro ou materiais.
~~~~

## 8. Equipamento

### R64-R-049

`equip--eqp-traje` · linha 7691

**Antes**

~~~~text
Ao escolher seu Traje, registre **uma situação** da tabela. Escolha também **um tipo de TR** entre Físico, Vigor, Intelecto e Espírito, e **um número de perícias igual à sua Maestria**.
~~~~

**Depois**

~~~~text
Ao escolher seu Traje, anote **uma situação** da tabela. Escolha também **um tipo de TR** entre Físico, Vigor, Intelecto e Espírito, e **um número de perícias igual à sua Maestria**.
~~~~

### R64-R-050

`equip--eqp-traje` · linha 7714

**Antes**

~~~~text
Na criação, você pode propor outra situação ao mestre. Ela deve ser uma condição física reconhecível e ocasional, com nome curto. Não pode ser apenas uma tarefa, como esconder-se, nem algo presente em quase toda cena. Registre a situação e a aparência do uniforme na ficha.
~~~~

**Depois**

~~~~text
Na criação, você pode propor outra situação ao mestre. Ela deve ser uma condição física reconhecível e ocasional, com nome curto. Não pode ser apenas uma tarefa, como esconder-se, nem algo presente em quase toda cena. Anote a situação e a aparência do uniforme na ficha.
~~~~

### R64-R-051

`equip--eqm-reserva` · linha 7873

**Antes**

~~~~text
Na criação do personagem, a compra de uma arma de fogo inclui **três cargas completas**: uma instalada e duas de reserva. A compra de um arco ou besta inclui **um conjunto de 20 projéteis** da tabela. Na besta, pode começar com um deles colocado e 19 no estojo. Registre esse estoque; ele pode acabar. Receber munição não aumenta seu limite de carga: escolha quanto levar e onde guardar o restante.
~~~~

**Depois**

~~~~text
Na criação do personagem, a compra de uma arma de fogo inclui **três cargas completas**: uma instalada e duas de reserva. A compra de um arco ou besta inclui **um conjunto de 20 projéteis** da tabela. Na besta, pode começar com um deles colocado e 19 no estojo. Anote esse estoque; ele pode acabar. Receber munição não aumenta seu limite de carga: escolha quanto levar e onde guardar o restante.
~~~~

### R64-R-052

`equip--eqc-dinheiro` · linha 8278

**Antes**

~~~~text
Nesta tabela, uma patente superior é a de maior posição na instituição: Grau 1 está acima de Grau 2, e Especial está acima de ambos. A autorização para armas de fogo deve ser combinada com o mestre ou com a organização da guilda antes da compra; registre seu alcance na ficha.
~~~~

**Depois**

~~~~text
Nesta tabela, uma patente superior é a de maior posição na instituição: Grau 1 está acima de Grau 2, e Especial está acima de ambos. A autorização para armas de fogo deve ser combinada com o mestre ou com a organização da guilda antes da compra; anote seu alcance na ficha.
~~~~

### R64-R-053

`equip--eqc-precos` · linha 8312

**Antes**

~~~~text
Você pode comprar uma proteção diferente. Registre também o destino do Traje recebido: se continuar levando-o, ele ocupa espaço mesmo guardado. Vestir uma peça sobre a outra não soma a proteção dos dois uniformes.
~~~~

**Depois**

~~~~text
Você pode comprar uma proteção diferente. Anote também o destino do Traje recebido: se continuar levando-o, ele ocupa espaço mesmo guardado. Vestir uma peça sobre a outra não soma a proteção dos dois uniformes.
~~~~

### R64-R-054

`equip--eqc-compras` · linha 8368

**Antes**

~~~~text
Ao passar um item para outra pessoa, retire-o do inventário de quem entregou e registre-o com quem recebeu. Transfira também seu estado e os suprimentos restantes. O mesmo objeto não pode constar como disponível para duas pessoas ao mesmo tempo.
~~~~

**Depois**

~~~~text
Ao passar um item para outra pessoa, retire-o do inventário de quem entregou e anote-o no inventário de quem recebeu. Transfira também seu estado e os suprimentos restantes. O mesmo objeto não pode constar como disponível para duas pessoas ao mesmo tempo.
~~~~

### R64-R-055

`equip--eqf-aquisicao` · linha 8479

**Antes**

~~~~text
Os preços do catálogo comum não incluem versões amaldiçoadas. Quando houver uma ferramenta à venda, o mestre informa o valor, as condições de aquisição e o que se sabe sobre ela. Uma peça emprestada continua pertencendo a quem a cedeu; registre as condições de devolução.
~~~~

**Depois**

~~~~text
Os preços do catálogo comum não incluem versões amaldiçoadas. Quando houver uma ferramenta à venda, o mestre informa o valor, as condições de aquisição e o que se sabe sobre ela. Uma peça emprestada continua pertencendo a quem a cedeu; anote as condições de devolução.
~~~~

### R64-R-056

`equip--eqf-aquisicao` · linha 8483

**Antes**

~~~~text
Ao entregar uma ferramenta conhecida, o mestre fornece sua ficha: base, grau, efeito, requisitos, Volume e usos. Se ela tiver Desgaste, registre as missões restantes e o que acontece quando acaba.
~~~~

**Depois**

~~~~text
Ao entregar uma ferramenta conhecida, o mestre fornece sua ficha: base, grau, efeito, requisitos, Volume e usos. Se ela tiver Desgaste, anote as missões restantes e o que acontece quando acaba.
~~~~

## 9. Progressão

### R64-R-057

`progressao--prog-limiar` · linha 8821

**Antes**

~~~~text
Para avançar do nível **20 para o 21**, reúna o XP necessário e registre **um dos sete feitos abaixo**, realizado entre os níveis **15 e 20**. Um feito reconhecido nessa faixa continua válido quando você chegar ao limiar.
~~~~

**Depois**

~~~~text
Para avançar do nível **20 para o 21**, reúna o XP necessário e anote **um dos sete feitos abaixo**, realizado entre os níveis **15 e 20**. Um feito reconhecido nessa faixa continua válido quando você chegar ao limiar.
~~~~

### R64-R-058

`progressao--prog-marcos` · linha 8917

**Antes**

~~~~text
O feitiço concedido é uma aplicação conhecida, não uma vaga livre para comprar Talento, Domínio ou invocação. O Talento respeita seu nível de acesso e não ocupa espaços. Cada Leque abre uma vaga própria para ele além do limite de **cinco Talentos pagos**. Registre a origem de cada ganho.
~~~~

**Depois**

~~~~text
O feitiço concedido é uma aplicação conhecida, não uma vaga livre para comprar Talento, Domínio ou invocação. O Talento respeita seu nível de acesso e não ocupa espaços. Cada Leque abre uma vaga própria para ele além do limite de **cinco Talentos pagos**. Anote a origem de cada ganho.
~~~~

### R64-R-059

`progressao--prog-repertorio` · linha 8939

**Antes**

~~~~text
Uma revisão das regras que invalide uma montagem permite corrigi-la gratuitamente, sem gastar essa revisão. Ajuste o que deixou de funcionar e registre o motivo. Isso não concede revisão livre de toda a ficha.
~~~~

**Depois**

~~~~text
Uma revisão das regras que invalide uma montagem permite corrigi-la gratuitamente, sem gastar essa revisão. Ajuste o que deixou de funcionar e anote o motivo. Isso não concede revisão livre de toda a ficha.
~~~~

### R64-R-060

`progressao--prog-atualizar` · linha 8949

**Antes**

~~~~text
1. Confira os valores comuns, aplique o marco quando houver e registre os benefícios do novo nível para a ficha atual.
~~~~

**Depois**

~~~~text
1. Confira os valores comuns, aplique o marco quando houver e anote os benefícios do novo nível para a ficha atual.
~~~~

### R64-R-061

`progressao--prog-trilhas` · linha 8987

**Antes**

~~~~text
Registre o que foi removido e o que entrou. Escolhas ou montagens que perderam uma permissão precisam ser ajustadas antes de voltar a ser usadas. Esse ajuste obrigatório não consome a revisão de um feitiço do nível, mas se limita às partes afetadas; não abre uma revisão geral das outras escolhas.
~~~~

**Depois**

~~~~text
Anote o que foi removido e o que entrou. Escolhas ou montagens que perderam uma permissão precisam ser ajustadas antes de voltar a ser usadas. Esse ajuste obrigatório não consome a revisão de um feitiço do nível, mas se limita às partes afetadas; não abre uma revisão geral das outras escolhas.
~~~~

### R64-R-062

`progressao--prog-capacidades` · linha 8997

**Antes**

~~~~text
Uma troca de Trilha pode retirar vagas adicionais ou a aquisição de duas entidades por espaço. Registre a nova capacidade e regularize a ficha antes de usá-la novamente. **Suspender uma escolha não apaga sua história nem permite alterná-la durante as missões.**
~~~~

**Depois**

~~~~text
Uma troca de Trilha pode retirar vagas adicionais ou a aquisição de duas entidades por espaço. Anote a nova capacidade e regularize a ficha antes de usá-la novamente. **Suspender uma escolha não apaga sua história nem permite alterná-la durante as missões.**
~~~~

### R64-R-063

`progressao--prog-capacidades` · linha 9013 · Também consta na outra lista

**Antes**

~~~~text
Registre a seleção. Um corpo suspenso volta ao seu controle quando uma vaga se abre porque um corpo controlado foi destruído ou porque seu total permitido aumentou, conforme **Invocações em campo**. Soltar um corpo de propósito, estar perto do suspenso ou voltar à cidade não permite alternar o grupo controlado.
~~~~

**Depois**

~~~~text
Anote a seleção. Um corpo suspenso volta ao seu controle quando uma vaga se abre porque um corpo controlado foi destruído ou porque seu total permitido aumentou, conforme **Invocações em campo**. Soltar um corpo de propósito, estar perto do suspenso ou voltar à cidade não permite alternar o grupo controlado.
~~~~

### R64-R-064

`progressao--prog-capacidades` · linha 9015

**Antes**

~~~~text
Também remova básicas, especiais, Talentos ou Famílias concedidas apenas pela Trilha anterior. Registre versões válidas das fichas afetadas. Entidades domadas ou fabricadas conservam sua aquisição própria; a troca de Trilha não as transforma em entidades por espaço nem aumenta seu nível.
~~~~

**Depois**

~~~~text
Também remova básicas, especiais, Talentos ou Famílias concedidas apenas pela Trilha anterior. Anote versões válidas das fichas afetadas. Entidades domadas ou fabricadas conservam sua aquisição própria; a troca de Trilha não as transforma em entidades por espaço nem aumenta seu nível.
~~~~

### R64-R-065

`progressao--prog-patentes` · linha 9029

**Antes**

~~~~text
Se a campanha usar remuneração, consulte **Recompensas da guilda**. Registre a patente vigente no fechamento indicado por aquele procedimento.
~~~~

**Depois**

~~~~text
Se a campanha usar remuneração, consulte **Recompensas da guilda**. Anote a patente vigente no fechamento indicado por aquele procedimento.
~~~~

## 10. Fundamento

### R64-R-066

`fundamento--fundamento` · linha 9069

**Antes**

~~~~text
Comece pela técnica inteira: o poder que ela manifesta, seu funcionamento e as possibilidades que você quer desenvolver. Registre essas escolhas com o mestre. O catálogo oferece opções prontas e procedimentos para propor capacidades próprias, com preço e limites definidos antes da sessão.
~~~~

**Depois**

~~~~text
Comece pela técnica inteira: o poder que ela manifesta, seu funcionamento e as possibilidades que você quer desenvolver. Anote essas escolhas com o mestre. O catálogo oferece opções prontas e procedimentos para propor capacidades próprias, com preço e limites definidos antes da sessão.
~~~~

### R64-R-067 · **Título para aprovação**

`fundamento--tecnica` · linha 9087

**Antes**

~~~~text
##### Registre as consequências
~~~~

**Depois**

~~~~text
##### Anote as consequências
~~~~

### R64-R-068

`fundamento-link-fios-de-tensao` · linha 9148

**Antes**

~~~~text
Escolha um ou dois tipos de dano compatíveis com a Descrição e registre quais são usados em cada feitiço. Se um feitiço causar mais de um tipo de dano, defina a distribuição durante sua criação e mantenha-a ao conjurar, inclusive depois de conhecer as resistências do alvo. Consulte o catálogo de Dano para a definição dos tipos. **Força** representa energia pura.
~~~~

**Depois**

~~~~text
Escolha um ou dois tipos de dano compatíveis com a Descrição e anote quais são usados em cada feitiço. Se um feitiço causar mais de um tipo de dano, defina a distribuição durante sua criação e mantenha-a ao conjurar, inclusive depois de conhecer as resistências do alvo. Consulte o catálogo de Dano para a definição dos tipos. **Força** representa energia pura.
~~~~

### R64-R-069

`fundamento-link-criar-regra-propria` · linha 9212

**Antes**

~~~~text
Comece por uma frase que a mesa consiga aplicar. Depois registre alcance, alvos, consequência e prazo quando forem necessários. A Regra Própria precisa cumprir estas condições:
~~~~

**Depois**

~~~~text
Comece por uma frase que a mesa consiga aplicar. Depois anote alcance, alvos, consequência e prazo quando forem necessários. A Regra Própria precisa cumprir estas condições:
~~~~

### R64-R-070

`fundamento-link-criar-regra-propria` · linha 9225

**Antes**

~~~~text
Os dois precisam entender e aceitar a aposta antes da disputa. Registrem um resultado que possa ser verificado e mantenham a disputa genuína, com o vencedor ainda por decidir. Empate consome a aposta da cena sem conceder vantagem. As ações disponíveis e os testes já resolvidos permanecem inalterados. Esta proposta original de **Categoria de Efeito 1** depende da aprovação da mesa.
~~~~

**Depois**

~~~~text
Os dois precisam entender e aceitar a aposta antes da disputa. Anotem um resultado que possa ser verificado e mantenham a disputa genuína, com o vencedor ainda por decidir. Empate consome a aposta da cena sem conceder vantagem. As ações disponíveis e os testes já resolvidos permanecem inalterados. Esta proposta original de **Categoria de Efeito 1** depende da aprovação da mesa.
~~~~

### R64-R-071

`fundamento-link-montar` · linha 9303

**Antes**

~~~~text
4. **Escolha a Forma e as peças.** Defina como os alvos serão alcançados e compre as Melhorias necessárias. Se desejar Restrições, registre exigências válidas e suas devoluções.
~~~~

**Depois**

~~~~text
4. **Escolha a Forma e as peças.** Defina como os alvos serão alcançados e compre as Melhorias necessárias. Se desejar Restrições, anote exigências válidas e suas devoluções.
~~~~

### R64-R-072 · **Título para aprovação**

`fundamento--primeiro` · linha 9354

**Antes**

~~~~text
##### Registre a ficha
~~~~

**Depois**

~~~~text
##### Preencha a ficha
~~~~

### R64-R-073

`fundamento--conjurar` · linha 9712

**Antes**

~~~~text
Durante a montagem, escolha com o mestre qual dos quatro TRs corresponde ao efeito e registre-o na ficha. Use esse mesmo TR nas conjurações, independentemente dos atributos conhecidos do inimigo.
~~~~

**Depois**

~~~~text
Durante a montagem, escolha com o mestre qual dos quatro TRs corresponde ao efeito e anote-o na ficha. Use esse mesmo TR nas conjurações, independentemente dos atributos conhecidos do inimigo.
~~~~

### R64-R-074

`fundamento--restricoes` · linha 9769

**Antes**

~~~~text
O mestre deve rever uma Restrição depois de três sessões em que o feitiço tenha sido usado. Substitua a exigência se ela nunca tiver dificultado o uso. Registre o requisito e sua consequência na ficha antes de conjurar e mantenha-os durante a resolução.
~~~~

**Depois**

~~~~text
O mestre deve rever uma Restrição depois de três sessões em que o feitiço tenha sido usado. Substitua a exigência se ela nunca tiver dificultado o uso. Anote o requisito e sua consequência na ficha antes de conjurar e mantenha-os durante a resolução.
~~~~

### R64-R-075

`fundamento--combinacoes` · linha 9783 · Também consta na outra lista

**Antes**

~~~~text
| Escolha as funções e destine a cada uma os pontos que sobram. Registre seus destinatários permitidos e sua resolução. | Escolha destinatários válidos e use as quantidades da ficha. Se houver Mais Um, reparta essas quantidades antes das rolagens, conforme a peça. |
~~~~

**Depois**

~~~~text
| Escolha as funções e destine a cada uma os pontos que sobram. Anote seus destinatários permitidos e sua resolução. | Escolha destinatários válidos e use as quantidades da ficha. Se houver Mais Um, reparta essas quantidades antes das rolagens, conforme a peça. |
~~~~

### R64-R-076

`fundamento--combinacoes` · linha 9784

**Antes**

~~~~text
| Registre o vínculo entre os efeitos e sua ordem de resolução. | Aplique essa ordem. Se uma criatura receber dano e benefício da mesma aplicação, resolva primeiro o dano. |
~~~~

**Depois**

~~~~text
| Anote o vínculo entre os efeitos e sua ordem de resolução. | Aplique essa ordem. Se uma criatura receber dano e benefício da mesma aplicação, resolva primeiro o dano. |
~~~~

### R64-R-077

`fundamento--mesclas` · linha 9825

**Antes**

~~~~text
**5. Registre a ficha**, incluindo o Selo da técnica:
~~~~

**Depois**

~~~~text
**5. Preencha a ficha**, incluindo o Selo da técnica:
~~~~

### R64-R-078

`fundamento--mesclas` · linha 9849

**Antes**

~~~~text
Registre o vínculo entre as partes na ficha, respeitando a peça comprada. Em Ferir e recuperar, um aliado válido e disposto recebe a cura mesmo se o ataque errar.
~~~~

**Depois**

~~~~text
Anote o vínculo entre as partes na ficha, respeitando a peça comprada. Em Ferir e recuperar, um aliado válido e disposto recebe a cura mesmo se o ataque errar.
~~~~

### R64-R-079

`fundamento--mesclas` · linha 9872

**Antes**

~~~~text
**Funções e distribuição:** destine dois pontos a **2d8 de dano** na área e um ponto para **1d8 de cura** no aliado. Registre o tipo de dano e o Teste de Resistência (TR) correspondente, com sua CD, a dificuldade que o alvo precisa alcançar no teste.
~~~~

**Depois**

~~~~text
**Funções e distribuição:** destine dois pontos a **2d8 de dano** na área e um ponto para **1d8 de cura** no aliado. Anote o tipo de dano e o Teste de Resistência (TR) correspondente, com sua CD, a dificuldade que o alvo precisa alcançar no teste.
~~~~

### R64-R-080

`fundamento--controle` · linha 9946

**Antes**

~~~~text
Depois de calcular os pontos que sobram de um feitiço comum de Classe 1 a 7 com Melhoria de Controle, registre uma das opções abaixo. Essa escolha define se ele conserva seu dano disponível ou abre mão de parte dele para reforçar o Controle.
~~~~

**Depois**

~~~~text
Depois de calcular os pontos que sobram de um feitiço comum de Classe 1 a 7 com Melhoria de Controle, anote uma das opções abaixo. Essa escolha define se ele conserva seu dano disponível ou abre mão de parte dele para reforçar o Controle.
~~~~

### R64-R-081

`fundamento--livre` · linha 10110

**Antes**

~~~~text
Use a descrição da técnica para propor soluções e registre os efeitos mecânicos necessários na ficha. Compre as capacidades que alterem a resolução da situação.
~~~~

**Depois**

~~~~text
Use a descrição da técnica para propor soluções e anote os efeitos mecânicos necessários na ficha. Compre as capacidades que alterem a resolução da situação.
~~~~

### R64-R-082

`fundamento--efeito` · linha 10140

**Antes**

~~~~text
Registre a origem e a extensão da aplicação, descrevendo a alteração que ela produz. Defina sua duração e o encerramento, inclusive o que acontece se um combate começar. Qualquer consequência sobre testes, ataques ou ações exige a capacidade correspondente e deve ser definida antes do uso.
~~~~

**Depois**

~~~~text
Anote a origem e a extensão da aplicação, descrevendo a alteração que ela produz. Defina sua duração e o encerramento, inclusive o que acontece se um combate começar. Qualquer consequência sobre testes, ataques ou ações exige a capacidade correspondente e deve ser definida antes do uso.
~~~~

### R64-R-083

`fundamento--ampliar` · linha 10176

**Antes**

~~~~text
Antes da sessão, registre uma linha para cada Classe em que pretende usar a mescla. Durante a conjuração, escolha uma dessas Classes e consulte os valores correspondentes. Todas as linhas pertencem ao mesmo feitiço e ocupam um único espaço. Preencha apenas as Classes que pretende usar.
~~~~

**Depois**

~~~~text
Antes da sessão, anote uma linha para cada Classe em que pretende usar a mescla. Durante a conjuração, escolha uma dessas Classes e consulte os valores correspondentes. Todas as linhas pertencem ao mesmo feitiço e ocupam um único espaço. Preencha apenas as Classes que pretende usar.
~~~~

### R64-R-084

`fundamento--ampliar` · linha 10181

**Antes**

~~~~text
4. Registre os resultados. Toda função variável precisa receber pelo menos um ponto; se isso não couber, essa versão da mescla é inválida. Os pontos a mais podem ficar sem uso.
~~~~

**Depois**

~~~~text
4. Anote os resultados. Toda função variável precisa receber pelo menos um ponto; se isso não couber, essa versão da mescla é inválida. Os pontos a mais podem ficar sem uso.
~~~~

### R64-R-085

`fundamento--ampliar` · linha 10185

**Antes**

~~~~text
Quando um feitiço tem uma única função variável, use os pontos que sobram normalmente; a tabela é opcional. Um feitiço sem pontos sobrando pode produzir os efeitos das Melhorias compradas, como Impulso. Registre dano ou cura somente quando houver pontos destinados a essas funções.
~~~~

**Depois**

~~~~text
Quando um feitiço tem uma única função variável, use os pontos que sobram normalmente; a tabela é opcional. Um feitiço sem pontos sobrando pode produzir os efeitos das Melhorias compradas, como Impulso. Anote dano ou cura somente quando houver pontos destinados a essas funções.
~~~~

### R64-R-086

`fundamento--ampliar` · linha 10195

**Antes**

~~~~text
A tabela mostra uma progressão de **Ferir e recuperar**, com base Média e Mais Um Leve, sem descontos ou Restrições. Você pode escolher outra distribuição para sua ficha, respeitando as funções e seus limites. Registre antes da sessão os valores de cada Classe que pretende usar.
~~~~

**Depois**

~~~~text
A tabela mostra uma progressão de **Ferir e recuperar**, com base Média e Mais Um Leve, sem descontos ou Restrições. Você pode escolher outra distribuição para sua ficha, respeitando as funções e seus limites. Anote antes da sessão os valores de cada Classe que pretende usar.
~~~~

### R64-R-087

`fundamento--proprio` · linha 10211

**Antes**

~~~~text
Registre os campos abaixo. Eles permitem comparar a proposta com peças existentes e resolver seu uso durante a sessão.
~~~~

**Depois**

~~~~text
Anote os campos abaixo. Eles permitem comparar a proposta com peças existentes e resolver seu uso durante a sessão.
~~~~

### R64-R-088

`fundamento--proprio` · linha 10229

**Antes**

~~~~text
Mestre e jogador escolhem a Família que melhor representa a função mecânica da proposta. Ela define o acesso e o desconto de Livre. Se nenhuma Família for adequada, registrem o preço integral, sem desconto de Família. A criação respeita as proibições das Famílias Fechadas.
~~~~

**Depois**

~~~~text
Mestre e jogador escolhem a Família que melhor representa a função mecânica da proposta. Ela define o acesso e o desconto de Livre. Se nenhuma Família for adequada, anotem o preço integral, sem desconto de Família. A criação respeita as proibições das Famílias Fechadas.
~~~~

### R64-R-089

`fundamento--proprio` · linha 10231

**Antes**

~~~~text
Quando a proposta reunir benefícios independentes, pague e conte cada um. O mestre pode autorizar uma redução específica de pontos ou de espaço após avaliar a proposta. Registre essa decisão junto dos efeitos que ela abrange.
~~~~

**Depois**

~~~~text
Quando a proposta reunir benefícios independentes, pague e conte cada um. O mestre pode autorizar uma redução específica de pontos ou de espaço após avaliar a proposta. Anote essa decisão junto dos efeitos que ela abrange.
~~~~

### R64-R-090

`fundamento--proprio` · linha 10251

**Antes**

~~~~text
**Repetir uma Melhoria própria depende de acordo com o mestre antes do uso.** Registrem quantas compras são permitidas, o preço de cada uma e o que cada repetição acrescenta. Cada compra paga e conta no limite normal, salvo exceção expressamente acordada.
~~~~

**Depois**

~~~~text
**Repetir uma Melhoria própria depende de acordo com o mestre antes do uso.** Anotem quantas compras são permitidas, o preço de cada uma e o que cada repetição acrescenta. Cada compra paga e conta no limite normal, salvo exceção expressamente acordada.
~~~~

### R64-R-091

`fundamento--maxima` · linha 10307

**Antes**

~~~~text
Escolha durante a criação se a Máxima causará dano, recuperará vida ou produzirá uma aplicação sem dano. Registre essa escolha e mantenha-a em todos os usos. Você recebe a Máxima pela progressão; ela fica fora dos espaços comuns e da troca por invocações.
~~~~

**Depois**

~~~~text
Escolha durante a criação se a Máxima causará dano, recuperará vida ou produzirá uma aplicação sem dano. Anote essa escolha e mantenha-a em todos os usos. Você recebe a Máxima pela progressão; ela fica fora dos espaços comuns e da troca por invocações.
~~~~

### R64-R-092

`fundamento--maxima` · linha 10325

**Antes**

~~~~text
Use os dados da faixa da Técnica Máxima. Na criação, registre dano ou cura e a Forma que entrega o resultado. A cura paga sua base Média; a aplicação coletiva paga também a Forma de área e exige Amparo e Área. Os dados de cura da Máxima não usam o teto comum. A cura coletiva alcança cada aliado válido na região.
~~~~

**Depois**

~~~~text
Use os dados da faixa da Técnica Máxima. Na criação, anote dano ou cura e a Forma que entrega o resultado. A cura paga sua base Média; a aplicação coletiva paga também a Forma de área e exige Amparo e Área. Os dados de cura da Máxima não usam o teto comum. A cura coletiva alcança cada aliado válido na região.
~~~~

## 11. Catálogo de criação

### R64-R-093

`catalogo--cat-catalogo` · linha 10512

**Antes**

~~~~text
Ao comprar, registre alvos, resolução e duração na ficha. Uma peça que aumenta alcance precisa ter um alvo ou origem cuja distância possa aumentar. Uma peça que amplia área precisa de uma região para ampliar. As permissões de Formas e Famílias continuam valendo.
~~~~

**Depois**

~~~~text
Ao comprar, anote alvos, resolução e duração na ficha. Uma peça que aumenta alcance precisa ter um alvo ou origem cuja distância possa aumentar. Uma peça que amplia área precisa de uma região para ampliar. As permissões de Formas e Famílias continuam valendo.
~~~~

### R64-R-094

`catalogo--melhoria-anteparo` · linha 10626

**Antes**

~~~~text
Cria uma **barreira fixa**, num ponto válido ao alcance do feitiço, com **10 × Classe PV** e duração de **1 minuto**. Seus painéis de 1,5 m usam a quantidade de quadrados da Linha básica da Classe, distribuídos numa superfície vertical contínua. Cada painel compartilha um lado com outro e a altura mínima é **3 m**. Registre o formato.
~~~~

**Depois**

~~~~text
Cria uma **barreira fixa**, num ponto válido ao alcance do feitiço, com **10 × Classe PV** e duração de **1 minuto**. Seus painéis de 1,5 m usam a quantidade de quadrados da Linha básica da Classe, distribuídos numa superfície vertical contínua. Cada painel compartilha um lado com outro e a altura mínima é **3 m**. Anote o formato.
~~~~

### R64-R-095

`catalogo--melhoria-escolher` · linha 10964

**Antes**

~~~~text
Ao criar a área, escolha as criaturas presentes que podem receber seus efeitos nocivos. Use uma única seleção para todas as partes nocivas iniciais. As demais criaturas ficam protegidas dessas partes e ainda podem receber os benefícios permitidos na ficha. Você precisa distinguir cada criatura selecionada por uma percepção válida. A Forma mantém seu formato e seus limites, sem acrescentar alvos ou benefícios. Com Fica, registre a lista de criaturas excluídas no disparo e mantenha-a durante a aplicação; outras criaturas que entrarem permanecem sujeitas ao efeito. A exclusão de Escolher não se aplica a Estilhaço.
~~~~

**Depois**

~~~~text
Ao criar a área, escolha as criaturas presentes que podem receber seus efeitos nocivos. Use uma única seleção para todas as partes nocivas iniciais. As demais criaturas ficam protegidas dessas partes e ainda podem receber os benefícios permitidos na ficha. Você precisa distinguir cada criatura selecionada por uma percepção válida. A Forma mantém seu formato e seus limites, sem acrescentar alvos ou benefícios. Com Fica, anote a lista de criaturas excluídas no disparo e mantenha-a durante a aplicação; outras criaturas que entrarem permanecem sujeitas ao efeito. A exclusão de Escolher não se aplica a Estilhaço.
~~~~

### R64-R-096

`catalogo--melhoria-reserva` · linha 11269

**Antes**

~~~~text
Role os dados de cura ao conjurar e registre o resultado como uma reserva no aliado. Ele recuperará essa vida na próxima vez, ainda nesta cena, em que passar de pelo menos metade da vida para abaixo dela. Aplique a cura guardada depois do dano que provocou essa queda, sem gastar ação. A criação da reserva mantém a vida atual do aliado.
~~~~

**Depois**

~~~~text
Role os dados de cura ao conjurar e anote o resultado como uma reserva no aliado. Ele recuperará essa vida na próxima vez, ainda nesta cena, em que passar de pelo menos metade da vida para abaixo dela. Aplique a cura guardada depois do dano que provocou essa queda, sem gastar ação. A criação da reserva mantém a vida atual do aliado.
~~~~

### R64-R-097

`catalogo--melhoria-efeito-proprio` · linha 11293

**Antes**

~~~~text
Registre o resultado, os alvos, a distância, a ação, a oposição e a duração. Indique o encerramento e uma situação em que o efeito não funciona. Compare com as peças de função mais próxima; o mestre define o preço e anota o motivo na ficha.
~~~~

**Depois**

~~~~text
Anote o resultado, os alvos, a distância, a ação, a oposição e a duração. Indique o encerramento e uma situação em que o efeito não funciona. Compare com as peças de função mais próxima; o mestre define o preço e anota o motivo na ficha.
~~~~

### R64-R-098

`catalogo--restricao-sobrecusto` · linha 11385

**Antes**

~~~~text
Registre o custo total na ficha. Num feitiço comum de Classe 3, são 9 PE normais + 6 adicionais = **15 PE**. Outras modalidades conservam seu próprio custo normal e somam o mesmo adicional pela Classe usada. Não concede devolução quando o adicional seria zero, nem permite Restrições em modalidades que as proíbem.
~~~~

**Depois**

~~~~text
Anote o custo total na ficha. Num feitiço comum de Classe 3, são 9 PE normais + 6 adicionais = **15 PE**. Outras modalidades conservam seu próprio custo normal e somam o mesmo adicional pela Classe usada. Não concede devolução quando o adicional seria zero, nem permite Restrições em modalidades que as proíbem.
~~~~

### R64-R-099

`catalogo--restricao-condicional` · linha 11445

**Antes**

~~~~text
**Devolução: Leve ou Média.** Escreva uma condição de cena ou de alvo que precisa existir para conjurar: estar no escuro, atacar alguém marcado por você ou estar perto de água corrente, por exemplo. Registre também seus limites; “perto de água” precisa dizer qual distância e o que conta como água corrente.
~~~~

**Depois**

~~~~text
**Devolução: Leve ou Média.** Escreva uma condição de cena ou de alvo que precisa existir para conjurar: estar no escuro, atacar alguém marcado por você ou estar perto de água corrente, por exemplo. Anote também seus limites; “perto de água” precisa dizer qual distância e o que conta como água corrente.
~~~~

### R64-R-100

`catalogo--restricao-condicional` · linha 11449

**Antes**

~~~~text
> **Exemplo: agir antes dos inimigos.** Registre que o feitiço só pode ser usado antes de qualquer inimigo agir na rodada. Ação ou Reação inimiga conta; apenas receber ataque ou fazer um TR não conta. Para uma aplicação adiada, a exigência precisa valer no pagamento e no disparo. Essa limitação não aumenta a CD por si só: use Precisão, se Mira estiver disponível, para comprar esse bônus. Avaliem a devolução pela dificuldade real na campanha; não a concedam apenas por dar um nome à exigência.
~~~~

**Depois**

~~~~text
> **Exemplo: agir antes dos inimigos.** Anote que o feitiço só pode ser usado antes de qualquer inimigo agir na rodada. Ação ou Reação inimiga conta; apenas receber ataque ou fazer um TR não conta. Para uma aplicação adiada, a exigência precisa valer no pagamento e no disparo. Essa limitação não aumenta a CD por si só: use Precisão, se Mira estiver disponível, para comprar esse bônus. Avaliem a devolução pela dificuldade real na campanha; não a concedam apenas por dar um nome à exigência.
~~~~

### R64-R-101

`catalogo--restricao-assinatura` · linha 11483

**Antes**

~~~~text
**Devolução: Leve.** O feitiço deixa uma **marca visível por 1 hora**, que mostra **quem fez o feitiço e onde você está**. Registre na ficha onde a marca aparece e como ela o identifica. A marca não pode ficar deliberadamente escondida na montagem.
~~~~

**Depois**

~~~~text
**Devolução: Leve.** O feitiço deixa uma **marca visível por 1 hora**, que mostra **quem fez o feitiço e onde você está**. Anote na ficha onde a marca aparece e como ela o identifica. A marca não pode ficar deliberadamente escondida na montagem.
~~~~

### R64-R-102

`catalogo--restricao-restricao-propria` · linha 11507

**Antes**

~~~~text
Se a proposta reunir duas dificuldades independentes, registre duas Restrições e respeite o limite. Se repetir o mesmo impedimento, conte a devolução uma vez. Ter duas consequências no mesmo instante não basta para torná-las iguais: Sangra e Barulho, por exemplo, cobram vida e exposição.
~~~~

**Depois**

~~~~text
Se a proposta reunir duas dificuldades independentes, anote duas Restrições e respeite o limite. Se repetir o mesmo impedimento, conte a devolução uma vez. Ter duas consequências no mesmo instante não basta para torná-las iguais: Sangra e Barulho, por exemplo, cobram vida e exposição.
~~~~

### R64-R-103

`catalogo--cat-passivas-3` · linha 11619

**Antes**

~~~~text
Registre quais aplicações pertencem ao tema. Afinidade não ignora coberturas **Boa ou Total**, imunidade, Redução de Dano ou uma passagem bloqueada, nem permite escolher um alvo que você não poderia escolher normalmente.
~~~~

**Depois**

~~~~text
Anote quais aplicações pertencem ao tema. Afinidade não ignora coberturas **Boa ou Total**, imunidade, Redução de Dano ou uma passagem bloqueada, nem permite escolher um alvo que você não poderia escolher normalmente.
~~~~

## 12. Aptidões e Refino

### R64-R-104

`aptidoes--apt-kokusen` · linha 11949

**Antes**

~~~~text
Cada teste de Kokusen que falhar acrescenta **+2 ao limite dos próximos testes de Kokusen**. Registre esse bônus. Ele só desaparece no descanso longo, inclusive se um Kokusen acontecer antes disso. Não altera a margem de crítico nem o acerto. Um limite de 100 ou mais garante o sucesso no d100.
~~~~

**Depois**

~~~~text
Cada teste de Kokusen que falhar acrescenta **+2 ao limite dos próximos testes de Kokusen**. Anote esse bônus. Ele só desaparece no descanso longo, inclusive se um Kokusen acontecer antes disso. Não altera a margem de crítico nem o acerto. Um limite de 100 ou mais garante o sucesso no d100.
~~~~

### R64-R-105

`aptidoes--apt-simples` · linha 12024

**Antes**

~~~~text
**Requisito: Refino 5, ou Refino 4 com o voto do iniciante. Categoria de Efeito 2.** Você precisa ter visto um Domínio Simples sendo usado ou ter aprendido com alguém. Registre essa origem do aprendizado.
~~~~

**Depois**

~~~~text
**Requisito: Refino 5, ou Refino 4 com o voto do iniciante. Categoria de Efeito 2.** Você precisa ter visto um Domínio Simples sendo usado ou ter aprendido com alguém. Anote essa origem do aprendizado.
~~~~

### R64-R-106

`aptidoes--apt-extensao` · linha 12117

**Antes**

~~~~text
**Requisitos: Refino 7 e nível 18. Categoria de Efeito 3.** Você precisa ter visto uma Extensão em uso, estudado seu funcionamento ou aprendido com alguém. Registre isso na ficha. **Corpo Amaldiçoado não pode adquirir esta aptidão.**
~~~~

**Depois**

~~~~text
**Requisitos: Refino 7 e nível 18. Categoria de Efeito 3.** Você precisa ter visto uma Extensão em uso, estudado seu funcionamento ou aprendido com alguém. Anote isso na ficha. **Corpo Amaldiçoado não pode adquirir esta aptidão.**
~~~~

### R64-R-107

`aptidoes--apt-cortina` · linha 12178

**Antes**

~~~~text
A preparação segue [Barreira Simples](#aptidoes--apt-barreira): **1 minuto**, sem custo em PE. Antes de começar, registre o lugar e suas bordas: um prédio, uma escola, uma quadra ou outro local contínuo. **Ao concluir, a distância de você até o ponto mais distante da borda não pode ultrapassar o teto do seu Refino.** O lugar e as bordas continuam definidos pela descrição; a medida limita a Cortina inteira, não cada trecho isolado.
~~~~

**Depois**

~~~~text
A preparação segue [Barreira Simples](#aptidoes--apt-barreira): **1 minuto**, sem custo em PE. Antes de começar, anote o lugar e suas bordas: um prédio, uma escola, uma quadra ou outro local contínuo. **Ao concluir, a distância de você até o ponto mais distante da borda não pode ultrapassar o teto do seu Refino.** O lugar e as bordas continuam definidos pela descrição; a medida limita a Cortina inteira, não cada trecho isolado.
~~~~

## 13. Rotas de criação

### R64-R-108

`rotas-link-montagem` · linha 12253 · Também consta na outra lista

**Antes**

~~~~text
1. **Defina o funcionamento.** Na seção da rota, escolha a semente ou o equipamento e escreva a Descrição e a Regra. Registre também atributo, Selo e Expressão da técnica conforme aquela rota.
~~~~

**Depois**

~~~~text
1. **Defina o funcionamento.** Na seção da rota, escolha a semente ou o equipamento e escreva a Descrição e a Regra. Anote também atributo, Selo e Expressão da técnica conforme aquela rota.
~~~~

### R64-R-109

`rotas-link-montagem` · linha 12257

**Antes**

~~~~text
5. **Registre e resolva.** Anote ação, alcance, alvos, ataque ou TR, resultado e duração. Coloque a aplicação no seu repertório. Ao usá-la, cumpra o Selo e pague os custos dessa ficha.
~~~~

**Depois**

~~~~text
5. **Anote e resolva.** Inclua ação, alcance, alvos, ataque ou TR, resultado e duração. Coloque a aplicação no seu repertório. Ao usá-la, cumpra o Selo e pague os custos dessa ficha.
~~~~

### R64-R-110

`rotas--rota-marcial` · linha 12285

**Antes**

~~~~text
3. Registre o equipamento que permite executar suas Katas e o atributo utilizado.
~~~~

**Depois**

~~~~text
3. Anote o equipamento que permite executar suas Katas e o atributo utilizado.
~~~~

### R64-R-111

`rotas--rota-ferramenta` · linha 12334

**Antes**

~~~~text
Você recebe **uma ferramenta amaldiçoada de grau 4**, criada com o mestre. Pode ser uma armadura, uma câmera, um instrumento ou outro objeto de apoio. Registre seu funcionamento, como é utilizado e qual atributo explica seu controle.
~~~~

**Depois**

~~~~text
Você recebe **uma ferramenta amaldiçoada de grau 4**, criada com o mestre. Pode ser uma armadura, uma câmera, um instrumento ou outro objeto de apoio. Anote seu funcionamento, como é utilizado e qual atributo explica seu controle.
~~~~

### R64-R-112

`rotas--rota-ferramenta` · linha 12344

**Antes**

~~~~text
Na criação, registre se seus ataques desarmados passam pelo objeto. Uma manopla, armadura, máscara ou bota pode permitir isso. Uma câmera, lanterna ou maleta apenas carregada não faz o mesmo.
~~~~

**Depois**

~~~~text
Na criação, anote se seus ataques desarmados passam pelo objeto. Uma manopla, armadura, máscara ou bota pode permitir isso. Uma câmera, lanterna ou maleta apenas carregada não faz o mesmo.
~~~~

### R64-R-113

`rotas--rota-sem-tecnica` · linha 12508

**Antes**

~~~~text
5. Monte cada Manejo por [Como montar Manejos e Katas](#rotas-link-montagem): escolha funções e Forma, pague a montagem da Classe e registre a ficha. Seu repertório usa os espaços de feitiço conhecido de Fundamento.
~~~~

**Depois**

~~~~text
5. Monte cada Manejo por [Como montar Manejos e Katas](#rotas-link-montagem): escolha funções e Forma, pague a montagem da Classe e preencha a ficha. Seu repertório usa os espaços de feitiço conhecido de Fundamento.
~~~~

### R64-R-114

`rotas--rota-propria` · linha 12931

**Antes**

~~~~text
Escreva primeiro uma frase que diga o que o corpo consegue fazer. Depois, registre gatilho, alcance, duração e limites necessários. A mesa deve conseguir decidir quando o efeito aconteceu sem discutir novamente a proposta a cada uso.
~~~~

**Depois**

~~~~text
Escreva primeiro uma frase que diga o que o corpo consegue fazer. Depois, anote gatilho, alcance, duração e limites necessários. A mesa deve conseguir decidir quando o efeito aconteceu sem discutir novamente a proposta a cada uso.
~~~~

## 14. Poderes avançados

### R64-R-115

`poderes--degraus` · linha 12976

**Antes**

~~~~text
Anote o degrau, a Regra da técnica, o **Acerto**, quando houver, e o **Efeito** do domínio. Registre também o tipo de dano, quando houver, os alvos, a resolução da Incompleta e qualquer limite necessário para executar essas duas capacidades.
~~~~

**Depois**

~~~~text
Anote o degrau, a Regra da técnica, o **Acerto**, quando houver, e o **Efeito** do domínio. Inclua também o tipo de dano, quando houver, os alvos, a resolução da Incompleta e qualquer limite necessário para executar essas duas capacidades.
~~~~

### R64-R-116

`poderes--acerto` · linha 13010

**Antes**

~~~~text
Monte o Acerto de dano como um feitiço pela régua de [Inescapável](#catalogo--melhoria-inescapavel), a Melhoria de dano automático: são **3 × sua maior Classe em pontos**, menos o preço Médio dessa Melhoria. Cada ponto restante vira 1d8 em cada criatura afetada. Registre um tipo de dano compatível com a técnica. O desconto de Família Livre vale normalmente. Use sua **maior Classe**, a Classe máxima permitida pelo seu nível, mesmo sem conhecer um feitiço dela. O Acerto é o feitiço inteiro e não aceita outra peça.
~~~~

**Depois**

~~~~text
Monte o Acerto de dano como um feitiço pela régua de [Inescapável](#catalogo--melhoria-inescapavel), a Melhoria de dano automático: são **3 × sua maior Classe em pontos**, menos o preço Médio dessa Melhoria. Cada ponto restante vira 1d8 em cada criatura afetada. Anote um tipo de dano compatível com a técnica. O desconto de Família Livre vale normalmente. Use sua **maior Classe**, a Classe máxima permitida pelo seu nível, mesmo sem conhecer um feitiço dela. O Acerto é o feitiço inteiro e não aceita outra peça.
~~~~

## 15. Ritual e Pactos

### R64-R-117

`ritual--pacto-permanente` · linha 13573

**Antes**

~~~~text
O pacto concede **uma mecânica única, decidida com o mestre**. Pode modificar o funcionamento de um feitiço, da energia, de uma aptidão ou de um Estilo. Registre a regra completa: o benefício muda como essa capacidade funciona, sem acrescentar diretamente um valor numérico.
~~~~

**Depois**

~~~~text
O pacto concede **uma mecânica única, decidida com o mestre**. Pode modificar o funcionamento de um feitiço, da energia, de uma aptidão ou de um Estilo. Anote a regra completa: o benefício muda como essa capacidade funciona, sem acrescentar diretamente um valor numérico.
~~~~

### R64-R-118

`ritual--pacto-temporario` · linha 13605

**Antes**

~~~~text
Você pode discutir modelos de pacto com o mestre antes da sessão. Registre gatilho, perda e ganho esperados. Quando a situação acontecer, o mestre confere se o preço ainda tem o mesmo valor. Isso reduz a negociação no meio do turno sem conceder aprovação automática a qualquer circunstância.
~~~~

**Depois**

~~~~text
Você pode discutir modelos de pacto com o mestre antes da sessão. Anote gatilho, perda e ganho esperados. Quando a situação acontecer, o mestre confere se o preço ainda tem o mesmo valor. Isso reduz a negociação no meio do turno sem conceder aprovação automática a qualquer circunstância.
~~~~

## 16. Invocações em campo

### R64-R-119

`campo--inv-fora` · linha 14263

**Antes**

~~~~text
O mesmo acompanhamento impede que ficar recolhida se torne um meio de recuperação sem custo. Registre vida, efeitos, usos e Movimento antes de retirar a miniatura. Se um efeito levar a entidade a zero enquanto estiver recolhida, aplique a queda e o retorno próprios, sem transportá-la de volta para o campo.
~~~~

**Depois**

~~~~text
O mesmo acompanhamento impede que ficar recolhida se torne um meio de recuperação sem custo. Anote vida, efeitos, usos e Movimento antes de retirar a miniatura. Se um efeito levar a entidade a zero enquanto estiver recolhida, aplique a queda e o retorno próprios, sem transportá-la de volta para o campo.
~~~~

### R64-R-120

`campo--inv-manutencao` · linha 14293

**Antes**

~~~~text
Registre na montagem o custo, a frequência e se o talento pode ser desligado. Essa indicação resolve quais efeitos cessam com a inconsciência e quais continuam tentando pagar.
~~~~

**Depois**

~~~~text
Anote na montagem o custo, a frequência e se o talento pode ser desligado. Essa indicação resolve quais efeitos cessam com a inconsciência e quais continuam tentando pagar.
~~~~

### R64-R-121

`campo--inv-carga` · linha 14323

**Antes**

~~~~text
Uma entidade segue as regras gerais de [Carga](#geral--carga), com limite normal de **5 + Força**, em Volume: o que ela veste, empunha ou leva conta nele. Transportar carga adicional ou personagens exige uma característica própria, compatível com a definição da entidade, que ocupe **um de seus talentos**. O armazenamento e os passageiros cabem na capacidade desse talento, de **5 + Força**. Para passageiros, registre quantidade, anatomia necessária e custo de Movimento na montagem; não há uma quantidade automática.
~~~~

**Depois**

~~~~text
Uma entidade segue as regras gerais de [Carga](#geral--carga), com limite normal de **5 + Força**, em Volume: o que ela veste, empunha ou leva conta nele. Transportar carga adicional ou personagens exige uma característica própria, compatível com a definição da entidade, que ocupe **um de seus talentos**. O armazenamento e os passageiros cabem na capacidade desse talento, de **5 + Força**. Para passageiros, anote quantidade, anatomia necessária e custo de Movimento na montagem; não há uma quantidade automática.
~~~~

## 17. Construir invocações

### R64-R-122

`construcao--entidades-criar` · linha 14350

**Antes**

~~~~text
1. **Aquisição e tipo.** Registre como a entidade foi obtida, sua origem, seu corpo e seu nível.
~~~~

**Depois**

~~~~text
1. **Aquisição e tipo.** Anote como a entidade foi obtida, sua origem, seu corpo e seu nível.
~~~~

### R64-R-123

`construcao--entidades-lista-criacao` · linha 14454

**Antes**

~~~~text
A técnica pode possuir **um feitiço com uma lista própria de entidades**. Registre esse feitiço em um espaço conhecido. A lista e o procedimento de submissão fazem parte de sua ficha e são definidos com o mestre antes do uso.
~~~~

**Depois**

~~~~text
A técnica pode possuir **um feitiço com uma lista própria de entidades**. Anote esse feitiço em um espaço conhecido. A lista e o procedimento de submissão fazem parte de sua ficha e são definidos com o mestre antes do uso.
~~~~

### R64-R-124

`construcao--entidades-lista-criacao` · linha 14466

**Antes**

~~~~text
Registre a Classe e a ficha da entidade. Ela acompanha o nível do invocador até o último nível da sua Classe; passar à Classe seguinte exige reconstruí-la. O reparo de um corpo existente segue [Cura e reparo](#campo--inv-reparo), em Invocações em campo.
~~~~

**Depois**

~~~~text
Anote a Classe e os dados da ficha da entidade. Ela acompanha o nível do invocador até o último nível da sua Classe; passar à Classe seguinte exige reconstruí-la. O reparo de um corpo existente segue [Cura e reparo](#campo--inv-reparo), em Invocações em campo.
~~~~

### R64-R-125

`construcao--entidades-definicao` · linha 14531

**Antes**

~~~~text
Anote tamanho, forma corporal, membros e sentidos comuns. Registre se ela fala, quais sinais compreende e como transmite uma descoberta. Uma aparência humana pode justificar mãos e voz. Um cão precisa de um meio compatível de segurar objetos e de se comunicar.
~~~~

**Depois**

~~~~text
Anote tamanho, forma corporal, membros e sentidos comuns. Indique se ela fala, quais sinais compreende e como transmite uma descoberta. Uma aparência humana pode justificar mãos e voz. Um cão precisa de um meio compatível de segurar objetos e de se comunicar.
~~~~

### R64-R-126

`construcao--entidades-definicao` · linha 14535

**Antes**

~~~~text
**Deslocamento terrestre-base: 9 m.** Voo, travessia de paredes ou outro modo extraordinário exige uma capacidade que o conceda e descreva seus limites. Desenhar asas não estabelece sozinho a velocidade, a sustentação ou as condições desse voo. Registre essas informações na capacidade correspondente.
~~~~

**Depois**

~~~~text
**Deslocamento terrestre-base: 9 m.** Voo, travessia de paredes ou outro modo extraordinário exige uma capacidade que o conceda e descreva seus limites. Desenhar asas não estabelece sozinho a velocidade, a sustentação ou as condições desse voo. Anote essas informações na capacidade correspondente.
~~~~

### R64-R-127

`construcao--entidades-vida-defesa` · linha 14601

**Antes**

~~~~text
Registre o equipamento usado, a proteção, os requisitos e a carga. Levar um objeto ao campo ou recolhê-lo junto com a criatura segue [Carga e equipamento](#campo--inv-carga), em Invocações em campo. A capacidade de equipar algo não transforma esse objeto em uma parte gratuita da entidade.
~~~~

**Depois**

~~~~text
Anote o equipamento usado, a proteção, os requisitos e a carga. Levar um objeto ao campo ou recolhê-lo junto com a criatura segue [Carga e equipamento](#campo--inv-carga), em Invocações em campo. A capacidade de equipar algo não transforma esse objeto em uma parte gratuita da entidade.
~~~~

### R64-R-128

`construcao--entidades-basicas` · linha 14679

**Antes**

~~~~text
Escolha uma Forma disponível e use as distâncias da Classe 0 em [Alcance e área](#construcao--entidades-medidas), deste capítulo. Para um ataque, registre tipo de dano e resolução. A mordida de um cão pode ser Toque. Um espinho lançado pode ser Projétil.
~~~~

**Depois**

~~~~text
Escolha uma Forma disponível e use as distâncias da Classe 0 em [Alcance e área](#construcao--entidades-medidas), deste capítulo. Para um ataque, anote tipo de dano e resolução. A mordida de um cão pode ser Toque. Um espinho lançado pode ser Projétil.
~~~~

### R64-R-129

`construcao--entidades-especiais` · linha 14719

**Antes**

~~~~text
5. **Registre o resultado.** Cada ponto restante pode virar 1d8 de dano. Cura e vida temporária usam as conversões e os tetos de suas funções. Efeitos comprados têm potência própria; sobras podem ficar sem uso.
~~~~

**Depois**

~~~~text
5. **Anote o resultado.** Cada ponto restante pode virar 1d8 de dano. Cura e vida temporária usam as conversões e os tetos de suas funções. Efeitos comprados têm potência própria; sobras podem ficar sem uso.
~~~~

### R64-R-130

`construcao--entidades-controle` · linha 14836

**Antes**

~~~~text
Uma especial comum usa o procedimento de [Controle](#fundamento--controle), em Montar sua aplicação: registre na criação a opção de dano limitado à Classe real em dados ou sem dano. Use a mesma tabela de efeitos compatíveis, CDs, duração, saídas e progressão. O orçamento e o desconto continuam sendo os da entidade. A básica e as aplicações máximas não recebem esse reforço comum.
~~~~

**Depois**

~~~~text
Uma especial comum usa o procedimento de [Controle](#fundamento--controle), em Montar sua aplicação: anote na criação a opção de dano limitado à Classe real em dados ou sem dano. Use a mesma tabela de efeitos compatíveis, CDs, duração, saídas e progressão. O orçamento e o desconto continuam sendo os da entidade. A básica e as aplicações máximas não recebem esse reforço comum.
~~~~

### R64-R-131

`construcao--entidades-controle` · linha 14848

**Antes**

~~~~text
Para uma proposta ausente do catálogo, use **Efeito Próprio** como peça da habilidade ou **Talento Próprio** como característica adquirida pela progressão de talentos. Registre um resultado verificável, alcance, alvos, resolução, duração e término. A proposta precisa respeitar as Famílias disponíveis e os limites de atuação da entidade.
~~~~

**Depois**

~~~~text
Para uma proposta ausente do catálogo, use **Efeito Próprio** como peça da habilidade ou **Talento Próprio** como característica adquirida pela progressão de talentos. Anote um resultado verificável, alcance, alvos, resolução, duração e término. A proposta precisa respeitar as Famílias disponíveis e os limites de atuação da entidade.
~~~~

### R64-R-132

`construcao--entidades-restricoes` · linha 14870 · Também consta na outra lista

**Antes**

~~~~text
Uma Restrição Própria precisa de situação concreta em que prejudique a entidade. Registre o texto e o motivo do preço. Depois de três sessões de uso, confira as exigências que nunca atrapalharam, conforme o procedimento do catálogo.
~~~~

**Depois**

~~~~text
Uma Restrição Própria precisa de situação concreta em que prejudique a entidade. Anote o texto e o motivo do preço. Depois de três sessões de uso, confira as exigências que nunca atrapalharam, conforme o procedimento do catálogo.
~~~~

### R64-R-133

`construcao--entidades-passiva-propria` · linha 14937 · Também consta na outra lista

**Antes**

~~~~text
Registre benefício, gatilho, alcance, requisitos, usos e término. Se houver ação, Reação ou PE, indique os recursos exigidos conforme [Invocações em campo](#campo--inv-campo). Um talento reativo não concede uma segunda Reação coletiva.
~~~~

**Depois**

~~~~text
Anote benefício, gatilho, alcance, requisitos, usos e término. Se houver ação, Reação ou PE, indique os recursos exigidos conforme [Invocações em campo](#campo--inv-campo). Um talento reativo não concede uma segunda Reação coletiva.
~~~~

### R64-R-134

`construcao--entidades-conferencia` · linha 15071

**Antes**

~~~~text
Depois da conferência, registre o texto acordado. Ajustes posteriores usam os procedimentos de evolução ou a revisão combinada com a mesa.
~~~~

**Depois**

~~~~text
Depois da conferência, anote o texto acordado. Ajustes posteriores usam os procedimentos de evolução ou a revisão combinada com a mesa.
~~~~

### R64-R-135

`fabricacao--fab-teste` · linha 15111

**Antes**

~~~~text
No sucesso, conclua a entidade com a ficha combinada e registre seu invocador. Na falha, ela ainda não funciona. Uma nova tentativa acontece quando o mestre permitir e tem vantagem.
~~~~

**Depois**

~~~~text
No sucesso, conclua a entidade com a ficha combinada e anote seu invocador. Na falha, ela ainda não funciona. Uma nova tentativa acontece quando o mestre permitir e tem vantagem.
~~~~

### R64-R-136

`fabricacao--fab-conclusao` · linha 15131

**Antes**

~~~~text
No sucesso, registre o novo invocador. A transferência conserva **Classe, ficha, vida atual e usos gastos**, além da queda e da carga do talismã. Depois dela, a entidade acompanha o nível do novo invocador dentro da Classe dela; atualize os valores que dependem dele. A transferência não recupera energia, não concede outra atuação no ciclo nem religa um corpo Desligado.
~~~~

**Depois**

~~~~text
No sucesso, anote o novo invocador. A transferência conserva **Classe, ficha, vida atual e usos gastos**, além da queda e da carga do talismã. Depois dela, a entidade acompanha o nível do novo invocador dentro da Classe dela; atualize os valores que dependem dele. A transferência não recupera energia, não concede outra atuação no ciclo nem religa um corpo Desligado.
~~~~

## 18. Mestrar

### R64-R-137

`consulta--consulta-missao` · linha 15159

**Antes**

~~~~text
Prepare as fichas dos perigos antes da sessão. Para uma maldição, registre os atributos e as capacidades que ela poderá usar. Use as referências de combate para resolver o encontro, sem conceder uma nova capacidade ao inimigo apenas para anular uma boa escolha dos jogadores.
~~~~

**Depois**

~~~~text
Prepare as fichas dos perigos antes da sessão. Para uma maldição, anote os atributos e as capacidades que ela poderá usar. Use as referências de combate para resolver o encontro, sem conceder uma nova capacidade ao inimigo apenas para anular uma boa escolha dos jogadores.
~~~~

### R64-R-138

`consulta--consulta-conduzir` · linha 15189

**Antes**

~~~~text
Procure a capacidade usada e o procedimento geral que ela modifica. Confira ação, alvo, alcance, resolução e prazo. Se a dúvida persistir, combine uma decisão para aquela sessão e registre o trecho que permitiu interpretações diferentes. A correção posterior deve ser comunicada a quem foi afetado.
~~~~

**Depois**

~~~~text
Procure a capacidade usada e o procedimento geral que ela modifica. Confira ação, alvo, alcance, resolução e prazo. Se a dúvida persistir, combine uma decisão para aquela sessão e anote o trecho que permitiu interpretações diferentes. A correção posterior deve ser comunicada a quem foi afetado.
~~~~
