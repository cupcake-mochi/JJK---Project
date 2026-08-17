# APTIDÕES E DEGRAUS DE REFINO

**Fase 4, décima primeira peça.** O eixo do controle: o que o refino é, o que ele governa, e o que se compra com ele.
Versão v0.27 — 11/08/2026

O `arquitetura.md` chama esta camada de *"o risco maior da estrutura inteira"*, e o motivo está escrito lá: aptidões são uma **segunda economia de poder**, e ela nasceu sem teto. O Fundamento tem orçamento, teto e validador; Barreira Simples, Cortina, Domínio Simples e o resto acontecem em combate e não passam por nenhum deles.

Esta peça existe para dar teto a essa economia. Validador: `conferir-aptidoes.py`.

> **Quatro entradas do catálogo ainda não estão aqui**, e a seção 7 explica por quê. As quatro anti-domínio saíram na v0.29, depois que a Expansão de Domínio ganhou regra no manual v7.7 — antes disso, precificá-las seria mirar num alvo que não existia.

---

## 1. O que o refino é

O eixo do **controle**, separado do eixo do **poder**. É a distinção que a obra faz o tempo todo: o Gojo diz que qualquer feiticeiro pode aprender Kokusen, e quase nenhum consegue. **Poder é quanto você tem; refino é quanto você não desperdiça.**

Até a v0.26 isso era só intenção. O refino existia como contador — subia nos marcos, tinha teto 10, e destravava aptidão. Entre um refino 3 e um refino 10, no mesmo nível, com as mesmas aptidões, **nada mudava na ficha**.

> **O refino é a métrica geral das aptidões.** Ele é o requisito para pegá-las, e é o número que diz o tamanho delas.

Ele entra no texto de uma aptidão **como variável**, no mesmo molde que o manual usa para `sua maior Classe`: *"a sua proteção é 1/3 do refino"*, *"Redução de Dano de 1,5 × refino"*, *"role d100 e tire 2 × refino ou menos"*. E **cada aptidão declara o próprio teto** — nem toda uma usa o valor cheio.

## 2. A trava, e o que ela permite

O refino sobe +1 por marco no passivo e +1 a mais quando você escolhe esse lado. Numa campanha inteira:

| o que cresce | do nível 2 ao 30 |
|---|---|
| atributo investido | 3 → 6, **+3** |
| maestria | 1 → 4, **+3** |
| refino, quem nunca escolhe | 1 → 8, **+7** |
| refino, quem sempre escolhe | 1 → 10, **+9** |

**O refino cresce duas a três vezes mais rápido que tudo o mais.** Isso não é defeito: ele é o eixo em que investir tem que aparecer. Mas ele proíbe uma coisa, e a proibição é a regra que governa o sistema desde a peça 1 — *numa rolagem disputada, os dois lados precisam crescer no mesmo ritmo*.

> **O refino não pode aparecer de um lado de uma rolagem em que o outro lado não cresce no ritmo dele.**

Isso elimina de saída **acerto, CD, defesa, Teste de Resistência e dano** — os cinco têm do outro lado alguém que cresce +3. É o erro que a v0.9 achou na maestria a cada quatro níveis, com o dobro do tamanho: um valor que sobe +9 contra um que sobe +3 leva o acerto de 50% a 5% no meio da campanha.

**E ela permite refino contra refino**, que é simétrico. É por isso que o clash de expansões pode ser decidido por ele: os dois lados crescem igual, e a chance não deriva.

O que sobra para o refino escalar:

| eixo | exemplo |
|---|---|
| **custo** | quanto PE a aptidão cobra |
| **frequência** | quantas vezes por cena, por descanso, por dia |
| **escopo** | alcance, duração, quantos alvos |
| **magnitude fora de disputa** | Redução de Dano, proteção, dano que não compete com feitiço |
| **disputa contra outro refino** | o clash de expansões |

### O caso que quase escapou

**Cobrir-se de energia dá proteção, e proteção entra na Defesa.** Se ela escalasse com o refino cheio, o atacante cairia de 50% para 5% de acerto no nível 22 — a mesma deriva, pelo lado defensivo. O `arquitetura.md` já tinha escrito a conclusão sem número: *"cobrir-se de energia dá uma defesa que não cresce"*.

A saída não foi tirar o refino dela: foi **dividir por três**. `1/3 do refino` cresce de 0 a 3 na campanha, que é exatamente o que um atributo cresce. É o único divisor que cabe — com 1/2 seriam +5.

## 3. O marco tem três eixos

*Esta seção substitui a escolha de duas opções da peça 2, seção 3.*

A cada quatro níveis — **6, 10, 14, 18, 22, 26 e 30**, sete marcos — o personagem recebe três coisas de graça e escolhe uma quarta.

> **Passivo:** +1 ponto de atributo, +1 de refino e **+1 espaço de feitiço**.
> **Escolha, uma das três:**
> **Corpo** — mais um ponto de atributo.
> **Refino** — mais um de refino, e uma aptidão. **Se o seu refino já estiver no teto, você leva `2` aptidões no lugar.**
> **Leque** — mais um feitiço, que só pode ser feitiço, e uma Passiva.

**Por que o terceiro eixo existe.** Passiva custa espaço de feitiço conhecido, e a Expansão de Domínio também. Sem uma rota que devolva espaço, quem monta técnica funda fica sem lista: três Passivas de Classe 2 mais a Expansão completa chegavam ao **nível 20 com dois feitiços**, e a montagem cheia — cinco Passivas de Classe 3 mais Expansão — era **impossível em qualquer nível**. O teto de *"cinco Passivas pagas"* do manual já era letra morta.

A linha passiva do marco sozinha conserta isso:

| montagem | nv14 | nv20 | nv26 | nv30 |
|---|---|---|---|---|
| só feitiço | 12 | 16 | 21 | 24 |
| 3 Passivas Classe 2 | 6 | 10 | 15 | 18 |
| 3 Passivas Classe 2 + Expansão completa | 3 | **7** | 12 | 15 |
| 5 Passivas Classe 3 + Expansão completa | 0 | 0 | **3** | 6 |

### O teto de refino chega antes do último marco, e a escolha não pode virar meia

**A linha de graça sozinha entrega 8 dos 10.** Sete marcos a `+1`, mais o refino 1 com que toda ficha começa: **quem nunca escolhe Refino termina a campanha com refino 8.**

**Então a metade *"mais um de refino"* da escolha só tem 2 pontos de espaço para caber, na campanha inteira** — e quem escolhe Refino nos sete marcos pagaria 15 e para em 10.

| marco | refino antes | depois | o que a ESCOLHA comprou |
|---|---|---|---|
| 6 | 1 | 3 | `+1` de refino e uma aptidão |
| 10 | 3 | 5 | `+1` de refino e uma aptidão |
| 14 | 5 | 7 | `+1` de refino e uma aptidão |
| 18 | 7 | 9 | `+1` de refino e uma aptidão |
| **22** | 9 | **10** | o refino da escolha **cai no teto** |
| **26** | 10 | **10** | idem |
| **30** | 10 | **10** | idem |

**Nos três últimos ela entregava metade do que promete.** *E os outros dois eixos não desperdiçam nada:* o Corpo ganha 14 pontos contra um teto somado de 30 nos cinco atributos, e o teto de Passivas do Leque sobe uma vaga por escolha, junto com a rota. **O refino era o único dos três cujo teto não acompanha quem o compra.**

> ***Decisão do Mizuki, na v0.89: no teto, a escolha de Refino leva DUAS aptidões.*** *Não é aptidão de graça — é a segunda metade da escolha trocando de moeda quando a primeira acaba.*

**A forma da comparação não muda, e é por isso que isto fecha.** Cortando o par aptidão/Passiva dos dois lados — eles vivem na mesma escada de Classe Passiva —, o marco sempre compara `+1` atributo contra **alguma coisa** contra `+1` feitiço. **Antes do teto essa alguma coisa é `+1` de refino; a partir dele é uma aptidão a mais.** *A escolha nunca fica com uma das mãos vazia.*

> **⚠ E o que isto NÃO tem é régua, declarado.** *"Uma aptidão a mais" não converte em fatia, e foi ela que matou o `Repertório` na v0.81.* **A diferença é quem recebe:** lá a Trilha era vendida para qualquer ficha, e o número tinha de valer para quem nunca pega aptidão nenhuma. **Aqui quem leva a segunda aptidão é, por definição, quem já escolheu esse eixo cinco vezes.** *A régua continua não existindo; o que muda é que esta comparação não depende dela.*

**A rota pura passa a precisar de 10 aptidões**, e o catálogo da seção 6 tem **12 que custam marco**. *Cabe, com duas de folga.* **E desde a v0.91 as doze estão escritas com número**, quando a `Barreira Simples` e a `Cortina` fecharam. **A rota pura passa a ter duas de folga, que é onde ela devia estar** — *escolher qual das doze deixar de fora é escolha, e não falta de cardápio.*

> **⚠ Só que a `Cortina` gasta DOIS marcos**, porque ela exige a `Barreira Simples`. *Uma rota pura que queira as duas usa `2` dos `10` picks para uma entrada só de catálogo.* **A folga de duas continua de pé, e ela some se alguém quiser as doze.**

### As três não se substituem, e é isso que as equilibra

`+1 feitiço e uma Passiva` empata com `+1 refino e uma aptidão` porque **Passiva e aptidão vivem na mesma escada de Classe Passiva** — as duas são efeito pequeno, reativo ou permanente, nas mesmas três alturas. O que sobra dos dois lados é `+1 feitiço` contra `+1 refino`.

E aí a conta fecha sozinha: **refino não vale nada para quem não tem aptidão.** Quem escolhe Leque sete vezes tem zero aptidões, então o refino dele é um número morto. Quem escolhe refino tem sete aptidões e nenhuma Passiva a mais para querer. Nenhuma das três precisa de trava porque nenhuma compra o que a outra compra.

No nível 30, as três rotas puras:

| rota | atributo | refino | aptidões | Passivas | feitiços a mais |
|---|---|---|---|---|---|
| sempre Corpo | **14** | 8 | 0 | 5 | 0 |
| sempre Refino | 7 | **10** | **10** | 5 | 0 |
| sempre Leque | 7 | 8 | 0 | **12** | **7** |

**O teto de Passivas sobe junto, e a grátis traz a própria vaga.** Cada escolha de Leque aumenta o máximo em um, e a Passiva concedida ocupa a vaga nova — então as **pagas continuam sendo cinco**, exatamente as cinco de sempre. O teto não cresce de verdade; ele abre lugar para o que a rota concede.

### Feitiços conhecidos

> **`2 + (nível ÷ 2)`, arredondando para baixo — mais um por marco.**

Três no nível 2: dois de toda ficha, mais o do próprio nível 2. Essa soma é o que confundia dois documentos: o manual dizia *"treze no nível 20"* e a peça 8 dizia *"dois no nível 2"*, e os dois não fechavam. A fórmula dá **doze no nível 20**, e o manual corrige o número na v7.7.

### Quem nunca escolhe Refino termina com zero aptidões

**E isso está escrito de propósito, aqui, para ninguém descobrir no nível 20.** A rota existe, ela é legítima, e o que ela troca é claro: **catorze pontos de atributo contra sete, e dez aptidões contra nenhuma**. Quem foca corpo é o dobro de atributo de quem foca controle.

Ele também não fica sem nada. **Cobrir-se de energia e canalizar energia vêm de graça no refino 1**, e as duas crescem com o refino passivo, que chega a 8 sem escolha nenhuma. O que ele nunca vai ter é Energia Reversa nem Barreira Simples.

## 4. As Classes Passivas — e o nome nunca vem sozinho

> **`Classe Passiva 1 · 2 · 3`. Sempre com as duas palavras, e nunca `Classe` solta.**

*Escrito na v0.64, e ele existe porque a palavra estava fazendo trabalho demais.* **O glossário do manual diz `Classe — o tamanho do feitiço, de 0 a 7`**, uma escala só. Só que ele também escreve *"cada Passiva tem uma Classe, **como um feitiço**"*, e a tabela de níveis dele diz *"7 — libera Passiva de Classe 2"*. **Então `Classe 2` já quer dizer duas coisas antes de esta peça abrir a boca**, e quando ela escrevia `Classe 2` querendo dizer *"reativo com limite"*, quem lia entendia *"feitiço de tamanho 2"*.

*Isso mordeu de verdade:* o Mizuki leu a régua de Trilha inteira e parou em *"Classe?, para mim Classe é feitiço"*. **Ele estava certo** — a leitura óbvia da palavra é a do glossário, e o eixo de formato vivia pegando ela emprestada sem devolver.

**O conserto é o idioma do próprio manual, não um termo novo.** Ele já escreve *"Passiva de Classe 2"* e *"Classe de Passiva"* quando precisa desambiguar; o projeto passa a fazer o mesmo, sempre. *`Feitio`, `Talhe`, `Lavra`, `Feição` e `Formato` saíram LIVRE na triagem e foram recusados de propósito — inventar palavra para o que o manual já sabe dizer é criar a segunda fonte que a lição nº 9 existe para evitar.*

As aptidões herdam a escada das Passivas do manual. **Ela não mede quanto — mede o quê.**

| Classe Passiva | o que cabe | as Passivas do manual naquela altura |
|---|---|---|
| **1** | efeito pequeno, condicional, ou de informação | `Leitura` · `Instinto` · `Raiz` · `Mão Firme` · `Farejador` · `Aviso` |
| **2** | efeito reativo, com limite de uso por cena ou por descanso | `Fluxo` · `Recomposição` · `Segunda Natureza` · `Eco` · `Costura` |
| **3** | permanente. Muda como você joga | — |

*A terceira coluna é a prova de que a leitura não foi inventada aqui:* as seis da Classe Passiva 1 são todas *"você sabe"* ou *"você não sofre"*, e as cinco da 2 são todas *"uma vez por X, acontece"*. **A escada estava na tabela do manual; o que faltava era alguém escrever o que ela separa.**

Uma Classe Passiva 3 não é "uma Classe Passiva 1 maior": é uma coisa de outro formato. **Farejador** — *"você sente se alguém conjurou num lugar nas últimas 24 horas"* — não fica obsoleta porque uma permanente existe; ela faz algo que nenhuma permanente faz.

**E o que impede a Classe Passiva 3 de comer as outras duas é o refino.** Um marco compra uma aptidão de qualquer Classe Passiva que o seu refino alcance, e se ela medisse tamanho, ninguém olharia para a 1 depois de destravar a 3 — mesmo preço, efeito maior. Com o refino escalando o que a aptidão entrega, **uma Classe Passiva 1 no refino 10 não é a mesma coisa que no refino 2**. Ela cresce junto com você.

> **E há uma diferença real entre a Passiva do manual e a aptidão daqui, que a palavra escondia:** na Passiva, a Classe Passiva **também cobra** — a 3 custa mais espaço de feitiço que a 1. Na aptidão **não cobra nada**: o marco compra uma de qualquer altura que o refino alcance, e o preço é o mesmo. *São duas economias, e é por isso que a seção abaixo diz que a aptidão não custa espaço de feitiço.*

> **A aptidão não custa espaço de feitiço.** Essa é a moeda das Passivas e da Expansão de Domínio, e as duas economias ficam separadas de propósito: uma muda de preço sem obrigar a outra a ser refeita.

## 5. O gate, e por que ele não é só nível

**Cada aptidão declara o próprio requisito: nenhum, só nível, só refino, ou os dois.** *E existem mais dois formatos, os dois escritos no fim desta seção: **só Origem**, desde a v0.58, e **exigir outra aptidão**, desde a v0.91.* **São cinco no total.**

A régua herdada das Passivas gateia por **nível** — Classe Passiva 1 no 1, a 2 no 7, a 3 no 13. Sozinha, ela não serve aqui, e a conta mostra por quê: com gate só de nível, **quem escolhe refino uma vez, no nível 26, compra uma Classe Passiva 3 na hora** — o mesmo acesso de quem investiu seis vezes. A ficção do refino some.

Um gate de refino separa:

| gate | especialista | meio a meio | generalista |
|---|---|---|---|
| Classe Passiva 2 no refino 4 | nível 10 | nível 10 | nível 14 |
| Classe Passiva 3 no refino 7 | nível 14 | nível 18 | **nível 26** |

Doze níveis entre o especialista e o generalista, que é o tamanho que *"quase ninguém consegue"* pede.

**E guardar marco não guarda refino.** A rota que espera — atributo cedo, refino tarde — não domina, porque o refino passivo sobe sozinho e ela chega ao nível 22 com refino 5, ainda precisando de outro marco para alcançar o 7. Ela troca quatro aptidões por quatro pontos de atributo, e as três que sobram são Classe Passiva 3. É a mesma escolha por outro caminho, não um atalho.

### O quarto formato: gate de Origem

*Escrito na v0.58, quando a peça 15 precisou de um e não tinha onde declará-lo.* Os três formatos acima gateiam por **coisa que se compra** — nível se ganha jogando, refino se ganha escolhendo no marco. Um gate de Origem não: ele pergunta **quem o personagem é**, e isso foi decidido na criação e não muda mais.

> **Um gate de Origem só é legal quando o efeito não faz sentido nenhum fora daquela Origem.** Não é para tornar caro; é para dizer que o resto da ficha não tem onde pendurar aquilo.

**Ele é raro de propósito, e o teste é o filtro multi-mestre.** Nível e refino dois mestres leem igual, porque estão escritos na ficha e crescem. Origem é um rótulo — se ela virar moeda de preço, a criação passa a ser escolhida por quais gates ela destrava, e a Origem deixa de ser ficção para virar árvore de talento. **Então ele não se usa para precificar: se o efeito couber num degrau da régua da peça que o publica, é ali que ele mora, e o gate não entra.**

### O quinto formato: gate de aptidão

*Escrito na v0.91, quando a `Cortina` pediu a `Barreira Simples`.* **Uma aptidão pode exigir que você já tenha outra.**

> **⚠ E este formato foi RECUSADO uma versão antes, então a diferença precisa estar escrita.** *Na v0.90 as três de kokusen passaram a empilhar, e fazer a `Kokusen Constante` exigir a `Kokusen Melhorado` foi recusado — porque as três são **alternativas**: cada uma serve sozinha, e o requisito obrigaria a comprar a de antes só para chegar na de depois.* **A `Cortina` é outra coisa: ela é a `Barreira Simples` maior.** *A obra diz isso — barreira é o básico, e cortina exige um nível de habilidade que muitos feiticeiros poderosos não têm.* **Um caso é escada; o outro seria pedágio.**

**A regra de quando ele é legal:** *a aptidão exigida tem de ser a mesma coisa em tamanho menor, e tem de servir sozinha.* **Se a de baixo só existir para destravar a de cima, é pedágio.**

*E o pedágio é exatamente o que a v0.65 derrubou* — uma pergunta de leitor do Mizuki, ***"por que não dá para pegar a de baixo em vez da de cima?"***, matou uma mecânica inteira. **O defeito não era a dependência: era ninguém ter escrito que ela podia existir.** *Agora está escrito.*

**E ele é o único dos cinco formatos que cobra MARCO.**

| formato | quem paga |
|---|---|
| nível | o tempo. Você joga e chega |
| refino | a linha passiva do marco, que sobe `+1` sem escolha nenhuma |
| Origem | a criação de personagem, uma vez |
| **aptidão** | **um marco.** É o recurso mais escasso da ficha |

*Uma ficha tem sete marcos na campanha inteira.* **Um gate de refino custa zero marcos — `refino 4` chega no nível 14 até para quem nunca escolhe Refino.** *Um gate de aptidão gasta um marco antes de a aptidão gateada abrir, e é por isso que ele não precisa de número em cima:* **o preço dele já é o mais caro que o marco tem.**

### E o exemplar único do gate de Origem

**O primeiro e único exemplar hoje é o `Remoto` da peça 15 §3.7**, na faixa *fora da cena*: alcance de país exige **Restrição Celestial pelo ramo do corpo limitado** e uma técnica voltada a isso, que é o Ultimate Mechamaru sem regra especial nenhuma. **O validador daquela peça confere que ele continua sendo o único** — um segundo gate no catálogo quer dizer que a régua de degrau parou de precificar sozinha.

## 6. O catálogo — as que têm número

### Cobrir-se de energia · grátis no refino 1

> **Sem Traje e sem Revestimento, a sua proteção é `1/3 do refino + 1`.** Escudo **soma** com ela.
> **Como Reação, você concentra a energia no impacto:** Redução de Dano de `1,5 × refino` num golpe, por **2 PE** — e você fica sem proteção até o fim do seu próximo turno.

> *Duas mudanças da v0.42, as duas vindas da peça de equipamento.* **O escudo saiu da lista do que desliga:** com o desligamento, ele virava prejuízo já no primeiro marco — no refino 3 você trocava proteção 2 por proteção 1 — e nenhum número o salvava enquanto competisse com uma proteção que cresce. **E o preço da Reação virou agnóstico de fonte:** ele dizia *"a proteção passiva"*, e quem estava fardado não pagava nada, porque não tira o colete no meio do golpe. Uma palavra a menos conserta os dois lados.

*Os 2 PE entraram na v0.30.* Até lá estava escrito só *"gastando PE"*, sem quantidade — um preço sem número, que é a lição nº 6 do README pelo avesso: o termo existia e o valor não. O `conferir-orcamento.py` procura essa forma agora.

**E o 2 é fixo, não escala — porque o limitador dela não é PE.** É a Reação, que você tem uma por rodada, e a proteção que você perde por um turno. Medindo contra o que um PE compra atacando (`Rotina ÷ custo do feitiço`), só o valor fixo mantém defender não sendo estritamente pior que atacar:

| preço da Reação | saldo no nv14 | no nv30 |
|---|---|---|
| **fixo 2 PE** | **+0,0** | **+0,9** |
| metade da Classe | +0,0 | −1,1 |
| metade do refino | −1,0 | −2,1 |
| `1 × Classe` | −2,0 | −4,1 |

Ela existe para o feiticeiro que não tem corpo. Quem zerou Destreza sai de ser acertado 80% das vezes para 60% no nível 30; quem investiu em Destreza e veste uniforme continua nos 50%. **É piso, não teto.**

A Reação é o momento do Todo contra o Mahito, e o `1,5 ×` é o que a faz valer a campanha inteira. Com `1 × refino` ela viraria armadilha: o custo de ficar um turno sem proteção cresce junto com o golpe do chefe, e a RD trava no teto 10.

| nível | RD | golpe de chefe | custo esperado | saldo |
|---|---|---|---|---|
| 6 | 4 | 17 | 1,7 | **+2,3** |
| 14 | 10 | 36 | 5,3 | +4,7 |
| 22 | 15 | 54 | 10,8 | +4,2 |
| 30 | 15 | 72 | 14,4 | **+0,6** |

Positiva do começo ao fim, e o saldo **encolhe** em vez de virar — forte quando você não tem outra resposta, e só mais uma opção quando já tem. **E ela não é redução de dano passiva:** custa Reação, custa 2 PE e custa a proteção de um turno. A regra que matou a Casca continua valendo.

*Um recado para a peça de equipamento:* no refino 10 ela dá proteção 4, e um Vanguarda que largue o uniforme chega a Defesa 20 contra os 17 dele fardado. **Um uniforme precisa valer mais que 4**, senão ele nasce morto.

### Canalizar energia · grátis no refino 1

Já está escrita na peça 5: *"um feitiço de Toque é um feitiço de Forma Toque, sem Melhoria e sem Restrição. Mesma Classe, mesmo orçamento de pontos, mesmo custo em PE."*

**O refino não a escala**, e é o exemplo mais limpo do teto por aptidão: ela vive inteira dentro do orçamento do Fundamento, e pôr refino nela seria dar poder de graça numa conta que já fecha.

### Projetar energia

> **Você dispara energia crua. O dano é `refino`, e ela não gasta PE.**

É o que sobra quando o combustível acaba, e o `arquitetura.md` já dizia o que ela não pode ser: *"o dano dela é fixo e baixo, e existe para quem ficou sem PE, não para competir com feitiço"*.

Com `dano = refino` ela fica entre **8% e 12% da coluna Rotina** do nível 2 ao 30 — sempre acima do Classe 0 depois do nível 10, e nunca perto de competir. **É o único lugar do catálogo onde o refino toca dano**, e ele deriva para **baixo**, porque a vida do inimigo cresce mais rápido que o refino. Errar para baixo é o lado seguro.

### Kokusen

> **Em crítico no corpo a corpo, role d100. `2 × refino` ou menos é kokusen: o dano leva +50% depois de todos os valores resolvidos.**

Em cima do crítico que já dobrou os dados — um crítico entrega `2D`, um kokusen entrega `3D`.

| refino | chance no d100 | dano por rodada | sessões até o primeiro |
|---|---|---|---|
| 1 | 2% | +0,2% | 47 |
| 5 | 10% | +0,9% | 9,5 |
| 10 | 20% | **+1,8%** | 4,7 |

**Ele existe pelo grito na mesa, não pela planilha, e o texto precisa dizer isso** — 1,8% no teto é menos de um quinto do que um ponto de atributo compra. Ninguém deve montar ficha em cima dele.

**E ele tem proteção contra azar.** No refino 1 a espera pelo primeiro seriam 47 sessões, o que na prática significa nunca. Cada d100 falhado empurra o próximo em **+2**, e o acumulado **zera no descanso longo**:

| | refino 1 | refino 5 | refino 10 |
|---|---|---|---|
| sem proteção | 47 sessões | 9,5 | 4,7 |
| com ela, zerando por missão | **~9** | 5,6 | 3,9 |

Ela socorre quem não investiu e quase não move quem investiu, que é a propriedade que se queria. E o relógio já existe: *por descanso longo* é o quarto da escada da peça 10, o mesmo da Integridade.

*Por que o relógio não é "por cena":* o acúmulo só começa a partir do **segundo crítico da mesma cena**, e dois críticos no mesmo combate acontecem em **4,4%** das vezes. Ele evaporaria antes de servir.

### Kokusen Melhorado · refino 5 e nível 14

> **Vantagem no d100.**

A vantagem ganha do `3 × refino` em **todo refino**, e a distância cresce: 36% contra 30% no teto. E ela não muda número nenhum na ficha — você rola dois d100 e pega o melhor.

O gate duplo tem folga do lado certo. Refino 5 cai no nível 10 para quem sempre escolhe refino, então **o nível 14 é a trava que morde**, e ela faz o especialista e o meio a meio convergirem no mesmo marco.

**O preço é ruim de propósito.** A ~2% de dano por rodada, ele vale um quinto do que um ponto de atributo compra, numa campanha com no máximo sete aptidões. Quem olha o número não escolhe; quem escolhe, escolhe pelo grito.

### Kokusen Constante · refino 5

> **A base sobe para `3 × refino`.**

Trinta por cento no teto. É a única das três que mexe no número em vez do dado, e por isso é a que se lê de cara na hora de escolher.

> ***As três empilham, e a ordem é essa:*** **a base é `3 × refino`, e a vantagem da `Kokusen Melhorado` rola em cima dela.** *Com as três na ficha, o d100 sai em `51%` no refino 10.* **Nenhuma delas exige a outra** — os quatro formatos de gate desta peça gateiam por nível, refino, os dois ou Origem, e nenhum deles é *"ter pego a de antes"*.

**Sozinha, ela perde para a `Kokusen Melhorado` em todo refino — e isso fica declarado, com a conta.**

| refino | só a `Melhorado` | só a `Constante` | as duas |
|---|---|---|---|
| 1 | 4,0% | 3,0% | 5,9% |
| 5 | 19,0% | 15,0% | 27,8% |
| **10** | **36,0%** | 30,0% | **51,0%** |

**A diferença é de forma e não de tamanho.** *Vantagem numa chance `p` dá `2p − p²`, e isso ganha de `1,5p` enquanto `p` estiver abaixo de `50%`.* **O teto do kokusen é `20%`, então a `Melhorado` ganha sempre.**

**O que a `Constante` compra em troca é o que esta seção já dizia dela: ela mora no número da ficha, e não na sorte do dado.** *E o gate é só de refino por causa disso:*

| gate | especialista | meio a meio | generalista |
|---|---|---|---|
| **`Kokusen Constante`** — refino 5 | **nível 10** | nível 14 | nível 18 |
| `Kokusen Melhorado` — refino 5 **e nível 14** | nível 14 | nível 14 | nível 18 |

**São quatro níveis em que ela é a única das duas disponíveis, e eles vão inteiros para quem investiu.** *É a mesma folga do lado certo que o gate duplo da `Melhorado` tem — só que virada para a outra ponta da campanha.*

**A cascata mexe só na chance do d100, e com teto.** Dobrar a chance no refino 5 rende **+0,9 ponto**; fazer a margem cair para 19 rende **+10,9%** — e **9,1 desses pontos vêm do dado a mais, antes de o kokusen entrar**. A margem carrega o crítico inteiro junto, e é por isso que ela está fora.

E "mais fácil depois do primeiro" sem teto é a espiral da exaustão com o sinal trocado: quem crita mais fácil crita mais, e crita mais fácil ainda. Sem teto, quatro degraus numa cena levariam o físico a **1,8× o dano base**, e aí a coluna Rotina para de valer no meio da luta.

### Energia Reversa · Classe Passiva 3 · refino 7 e nível 13

> **Ação padrão. Gaste até `maior Classe` de PE e recupere `1d8` de vida por PE gasto, em você.**

*Ela estava na lista das que faltavam desde a v0.27 e fechou na v0.77, quando a Trilha `Sutura` do Guia precisou dela para existir.*

**Nenhum número aqui é escolha minha, e vale mostrar de onde cada um sai.** A seção 7 já mandava medir esta aptidão contra a Passiva **`Recomposição`**, que é a cura inata: `5 × maior Classe`, uma vez por descanso curto — **`35` de cura no nível 30**. O projeto tem câmbio de PE, porque `+1` PE por rodada vale `5,14` de dano por rodada; e cura é **dano evitado**, que a régua converte `1` pra `1`. **Então um PE vale cerca de cinco de cura.** E o manual já cura em dado: *"cada ponto que sobra vira `1d8`"*, que é `4,5`.

| | quanto cura no nível 30 |
|---|---|
| a Passiva `Recomposição`, uma vez por descanso curto | `35` |
| **`Energia Reversa` no teto — `7d8`** | **`31,5`** |

**Mesma altura, e a diferença mora em outro eixo:** a Passiva é de graça e acontece uma vez; esta cobra PE e se repete. *E ela gasta a ação padrão — curar `31,5` numa rodada em que você tomaria `33,9` é empatar, e o empate é a intenção.*

**O gate não foi escolhido por simetria com a `Extensão de Domínio`, mesmo sendo o mesmo.** No material, energia reversa é gerada no **cérebro** e não no intestino como a comum, e o que a torna rara é sustentar **dois fluxos de energia ao mesmo tempo**. É a coisa que quase ninguém alcança — e a Classe Passiva 3 com refino 7 é exatamente a altura que a seção 5 reserva para isso: **o generalista só chega no nível 26.**

> **Ela cura VOCÊ, e isso não é economia de texto.** *Curar terceiro é o degrau raro do material*: o Gojo cura a si mesmo e não cura os outros, e a Shoko é nomeada como uma das poucas que conseguem. **Quem cura os outros é a Trilha `Sutura`**, e é ela que paga por isso — no nível 11 dela, e não no 2.

**O refino não escala esta aptidão, e o teto é a `maior Classe`.** *Pôr refino no tamanho da cura a faria derivar contra a vida do inimigo, que é o que a seção 2 proíbe.* A Classe já cresce com o nível, já é o eixo certo, e já é a variável que o manual usa para tudo que escala com tamanho de feitiço.

## 6.5. As quatro anti-domínio

*Escritas na v0.29, depois que a Expansão ganhou regra no manual v7.7.*

### A regra que vale para as quatro, e que precisa estar escrita

> **Elas anulam o Acerto de uma Expansão. Nenhuma delas serve contra a Expansão incompleta.**

Não é escolha nossa: é como a obra funciona, e tem cena provando. O Reggie ativou Cesta Oca de Vime dentro do Jardim de Sombras Quimérico do Megumi — que é incompleto — e não adiantou nada. Os shikigami tomaram forma e bateram nele como qualquer coisa bate em qualquer um.

**O motivo é mecânico e limpo.** Estas quatro anulam *acerto garantido*. A incompleta não tem acerto garantido: o Acerto dela **rola**. Contra ela você se defende com Defesa e com Teste de Resistência, como se defende de tudo o mais no jogo. Não existe buraco aqui — existe uma peça respondendo ao que ela responde, e nada além.

E é por isso que o terceiro espaço da Expansão compra alguma coisa de verdade: ele troca um Acerto que dá para bloquear com Defesa por um que só estas quatro alcançam.

### O que cada uma custa por fora, e por que elas são diferentes

O eixo que separa as quatro não é força — é **quanta liberdade você tem enquanto está protegido**. Os quatro preços vêm da obra:

| | protege | e cobra |
|---|---|---|
| **Cesta Oca de Vime** | só você, dentro de uma esfera | você segura o símbolo e **não faz mais nada** |
| **Domínio Simples** | um raio em volta de você | **os pés não saem do chão**, ou ela quebra |
| **Pétala** | o seu corpo, e **devolve o golpe** | exige concentração, e **não para ataque físico** |
| **Extensão de Domínio** | o seu corpo, e faz o **seu** ataque acertar | **nenhum feitiço enquanto ela estiver de pé** |

### As quatro, com número

| | Classe · gate | abre em | o refino escala | PE por rodada |
|---|---|---|---|---|
| **Cesta Oca de Vime** | 1 · sem gate | nv 6, nas três rotas | **nada** | **nenhum** |
| **Domínio Simples** | 2 · refino 4, nível 7 | nv 10 · 10 · 14 | o raio: `1,5 m + refino ÷ 2` | `1 × maior Classe` |
| **Pétala** | 2 · refino 4, nível 7 | nv 10 · 10 · 14 | quantos Acertos devolve: `refino ÷ 2` | `1 × maior Classe` |
| **Extensão de Domínio** | 3 · refino 7, nível 13 | nv 14 · 18 · 26 | a duração: `refino` rodadas | `1,5 × maior Classe` |

**Todas custam um marco, como qualquer aptidão. Nenhuma custa espaço de feitiço.**

### Cesta Oca de Vime · Classe 1, sem gate

> **Você faz o símbolo e uma esfera se fecha em volta de você. Enquanto você o segurar, o Acerto de uma Expansão não te alcança — e você não faz mais nada.**

Ela é a **predecessora** do Domínio Simples, e é pior de propósito: **anula o Acerto e mais nada.** O Efeito da Expansão continua acontecendo em cima de você, e o refino não a melhora em nada — é a segunda aptidão do catálogo que não usa o valor cheio, junto com canalizar energia.

**Em troca ela não quebra**, e é a única das quatro assim. Não tem duração, não tem teste, não tem PE: enquanto o símbolo estiver de pé, ela está de pé.

**E ela é de graça em PE porque já cobra o turno**, que é o recurso mais caro de uma luta. Cobrar as duas coisas seria cobrar duas vezes pela mesma escolha:

| rodadas segurando | dos seus turnos na luta | Acertos que você evita |
|---|---|---|
| 1 | 29% | 1 |
| 2 | **57%** | 2 |
| 3 | 86% | 3 |

Evitar dois Acertos custa mais da metade dos seus turnos: **você sobrevive e não contribui.** É resposta de sobrevivência, não de vitória — que é exatamente o que ela é na obra.

**É ela, e não o Domínio Simples, a resposta que chega no nível 6 para as três rotas.** Um marco de Refino, uma vez, e o acerto garantido deixa de ser sentença. Isso é o que torna a Expansão completa jogável, e é o menor preço que o sistema cobra por qualquer coisa.

### Domínio Simples · Classe 2, refino 4 e nível 7

> **Um domínio pequeno em volta de você, de raio `1,5 m + refino ÷ 2`. Dentro dele o Acerto de uma Expansão não acontece. Custa `1 × a sua maior Classe` de PE por rodada, e ela quebra se os seus pés saírem do chão.**

É o que se ensina, e o que a Miwa e o Kusakabe usam. A diferença para a Cesta Oca não é ser mais forte contra o Acerto — é **você poder lutar dentro dela**, e ela **cobrir quem estiver no raio**.

| refino | 1 | 2 | 4 | 6 | 8 | 10 |
|---|---|---|---|---|---|---|
| raio | 1,5 m | 2,5 m | 3,5 m | 4,5 m | 5,5 m | **6,5 m** |

O Domínio Simples da obra tem cerca de 2,21 m, e a fórmula bate nisso no refino 2. **Ela nunca passa de um movimento (9 m)**, e isso é a trava: uma defesa que cercasse o inimigo seria outra peça. O Kusakabe puxando gente para dentro é coisa da Trilha dele, não da aptidão.

### Pétala · Classe 2, refino 4 e nível 7

> **A energia cobre o seu corpo e devolve o golpe. Quando o Acerto de uma Expansão te alcança, ele é anulado no ponto de contato — `refino ÷ 2` vezes por cena. Custa `1 × a sua maior Classe` de PE por rodada, e ela cai se você perder a concentração.**

Ela não faz domínio nenhum: é a energia no corpo que reage. Segredo dos três clãs — Gojo, Zenin e Kamo —, e o Gojo disse que aprendeu criança e nunca tinha usado.

**Ela não cobre a Expansão inteira, e isso é de propósito.** A completa dispara o Acerto ao abrir e no começo de cada turno do portador:

| refino | Acertos que a Expansão solta | a Pétala devolve |
|---|---|---|
| 4 | 3 | 2 |
| 6 | 4 | 3 |
| 8 | 5 | 4 |
| 10 | **6** | **5** |

Sempre sobra um. Se ela devolvesse tudo, o terceiro espaço que a Expansão completa custou deixaria de comprar alguma coisa.

**E ela não para ataque físico** — o Dagon socou o Naobito com a Pétala de pé. Contra um Acerto que é golpe de corpo, ela não faz nada.

### Extensão de Domínio · Classe 3, refino 7 e nível 13

> **Você se envolve numa camada fina de domínio sem técnica dentro. Ela anula o Acerto de uma Expansão, anula qualquer técnica que encostar nela, e faz o seu ataque acertar independentemente da técnica do alvo. Dura `refino` rodadas, custa `1,5 × a sua maior Classe` de PE por rodada — e enquanto ela estiver de pé, você não usa a sua técnica.**

É a única das quatro que também é ataque, e a única Classe 3. É o que o Jogo e o Hanami usaram contra o Ilimitado do Gojo.

**O preço dela se equilibra sozinho, e é bonito de ver:** ela dura o dobro do que uma Expansão dura, mas o PE é o teto de verdade.

| nv | refino | duração | PE/rodada | segurar até o fim | do dia de um Bastião |
|---|---|---|---|---|---|
| 14 | 7 | 7 | 6 | 42 | 75% |
| 20 | 9 | 9 | 8 | 72 | 90% |
| 26 | 10 | 10 | 11 | 110 | **106%** |
| 30 | 10 | 10 | 11 | 110 | 92% |

**No nível 26 um Bastião não consegue segurar até o fim** — ele fica sem PE na nona rodada de dez. A duração é teto, não promessa, e quem tem pouco PE descobre isso antes de quem tem muito. Numa luta normal de 3,5 rodadas ela custa uns 32% do dia, que é o preço de verdade.

E some tudo isso com *"você não lança nada enquanto ela está de pé"*: quem tem feitiço bom paga o dobro por ela.

### Por que o custo por rodada é `1 × maior Classe`

A conta escolheu sozinha. Medido no Bastião, que é o piso de PE do sistema, numa luta de 3,5 rodadas:

| custo por rodada | do dia, por luta | lutas que cabem |
|---|---|---|
| metade da Classe | 9% a 18% | 5 a 11 |
| **`1 × Classe`** | **20% a 26%** | **3 a 4** |
| `2 × Classe` | 41% a 52% | 1 a 2 |

**O `1 ×` fica exatamente do tamanho do orçamento de lutas do dia.** A exaustão dispara da quarta luta, então dá para segurar a defesa em toda luta de um dia normal e terminar seco bem quando o cansaço chegaria de qualquer jeito. Tensão sem armadilha.

As outras duas quebram nas pontas: com `2 ×` você se defende uma vez e acabou o dia; com metade, o custo cai para 9% no nível 20 e **evapora**.

## 6.6. As duas barreiras — e o gate delas é um relógio

*Escritas na v0.91, e elas eram as duas últimas entradas do catálogo sem número.*

**As duas são ferramenta de preparação e não de luta, e isso não é sabor: é a única forma que a conta deixa.**

> **A régua do projeto diz que dano evitado converte `1` pra `1`.** *Uma barreira que o inimigo precisa quebrar consome nele exatamente a vida dela — então ela **evita a própria vida**.*
>
> | vida no teto | quanto ela evitaria | por rodada de luta | em fatias |
> |---|---|---|---|
> | `50`, a `Barreira Simples` | 50 de dano | 15,2 | **2,98** |
> | `200`, a `Cortina` | 200 de dano | 60,6 | **11,93** |
>
> **Uma Trilha inteira leva `5,00` fatias, e um marco compra `2,13`.** *Qualquer uma das duas, se coubesse numa luta, seria uma aptidão valendo mais que a Trilha que a ficha escolheu.*

**E gastar a rodada inteira levantando não gateia. Não chega perto.**

*Uma luta dura `3,3` rodadas: gastar uma inteira deixa `2,3` com a barreira de pé, que são `70%` da luta.* **E o câmbio fica a seu favor — uma rodada sua no nível 30 vale `108` de dano, e você a troca por uma barreira que absorve `200`.**

**O que gateia é levantar custar mais do que a luta inteira dura.** `1 minuto` são **dez rodadas** contra uma luta de `3,3`. **Aí ela não cabe, em mesa nenhuma, e nenhum mestre precisa julgar se alguém "está em combate"** — que é a pergunta que sete mesas respondem de sete jeitos.

*E o número já tem casa: `1 minuto` é a duração que o manual usa na Melhoria `Anteparo`.*

### Barreira Simples · sem gate

> **Um minuto para levantar.** Um domo de **raio `6 m`**, ancorado no lugar onde você o ergueu, que **bloqueia passagem e linha de efeito nos dois sentidos**.
>
> **Ele tem `5 × refino` de pontos de vida, e cai quando você fica `Inconsciente`.**

**A vida sai de comparação com o manual, e ela fica embaixo de propósito.** *A Melhoria `Anteparo` deixa uma parede com `10 × Classe` de vida — `70` no Classe 7, que é a maior parede que um feitiço monta.* **`5 × refino` dá `50` no teto: menos que a maior parede montada, e por um motivo.** *Aquela custa pontos de montagem dentro de um feitiço e sai numa ação; esta custa um marco e um minuto.* **A que sai rápido pode ser maior; a que é permanente na ficha não pode.**

**Ela é ancorada, e isso é o que a separa de um escudo.** *O domo fica onde foi erguido — você não o leva junto.* **Fechar um cômodo, uma porta, uma escada: é isso que ela faz.**

*Na obra, barreira comum é zona que protege um lugar, e não anteparo portátil.* **A ficção e a conta pediram a mesma coisa.**

### Cortina · exige a `Barreira Simples`

> **Um minuto para levantar.** Ela cobre **um lugar** — um prédio, uma escola, um quarteirão — e **esconde o que está dentro de quem não é feiticeiro**.
>
> **Você pendura uma condição sobre quem atravessa.**
>
> **Ela tem `20 × refino` de pontos de vida, e cai quando você fica `Inconsciente`.**

**O gate é ter a `Barreira Simples`, e nada mais.** *Sem gate de nível e sem gate de refino:* **o preço é o segundo marco**, e ele é mais caro que qualquer gate de refino, que a linha passiva paga sozinha.

| rota | a `Barreira Simples` abre | a `Cortina` abre |
|---|---|---|
| sempre Refino | nível 6 | **nível 10** |
| meio a meio | nível 10 | **nível 22** |
| sempre Corpo · sempre Leque | nunca | **nunca** |

***Quem nunca escolhe Refino duas vezes não levanta Cortina, e isso é da obra:*** *cortina exige um nível de habilidade que muitos feiticeiros poderosos não têm, e as condições delas chegam a ser encomendadas a quem sabe fazer.*

**A condição fala de QUEM ATRAVESSA, e de mais nada.** *É o recorte da obra — as condições de uma cortina tratam de energia amaldiçoada e de passagem.*

| a condição pode | a condição não pode |
|---|---|
| barrar uma pessoa específica | causar dano a quem entra |
| deixar entrar quem tem energia amaldiçoada, e mais ninguém | mover a cortina, ou fazer ela seguir você |
| impedir que quem está dentro saia | dar bônus a quem está dentro |
| deixar passar quem você nomeou na hora de levantar | esconder de quem é feiticeiro — o efeito base já é o contrário |

*O exemplar da obra é o feiticeiro que levantou uma cortina que deixava outros feiticeiros passarem e barrava só o Gojo.*

> **O tamanho dela não tem metro, e isso é decisão e não descuido.** *Ela é a única coisa do sistema cujo tamanho **nunca entra numa rolagem**: dois mestres discordarem se ela pega um quarteirão ou dois não muda número nenhum, porque nada dentro dela se mede em metros.* **Está escrito aqui justamente para ninguém tentar usá-la como medida de combate** — quem quiser fechar uma distância com energia usa a `Barreira Simples`, que tem raio.

## 7. A que falta, e por que

*As quatro anti-domínio saíram desta seção na v0.29 e estão na seção 6.5. **A `Energia Reversa` saiu na v0.78** e está na seção 6, medida contra a `Recomposição`.* **E a `Barreira Simples` e a `Cortina` saíram na v0.91** — estão na seção 6.6, com o relógio de um minuto que tira as duas do combate.

**Sobra uma, e ela falta por régua e não por número:**

| aptidão | o que ela é | contra o que precisa ser medida |
|---|---|---|
| **Aptidão Própria** | qualquer outra coisa, uma vez na ficha inteira | a régua do **Efeito Próprio**: *em quantas cenas por arco isso importa?* |

**A Aptidão Própria tem duas travas escritas.** Ela é **Classe 1 ou 2, nunca 3** — permanente é caro demais para sair de aprovação —, e **só pode ser pega uma vez na ficha inteira**, no mesmo molde do Legado. Ela é a energia densa do Hakari e o Punho Divergente do Itadori: a coisa que um feiticeiro construiu sozinho, que não é técnica e não está no catálogo.

## 8. O Limiar

Vem do dossiê, seção 2, roubado do PbtA e do FitD: **gatilho de ficção antes da rolagem**. Aqui ele é mecânica separada, e o kokusen é só um dos lugares que o citam.

> **Quando a ficção chega num ponto em que alguma coisa tem que ceder, o mestre abre um Limiar.**

Ele não faz nada sozinho — o que acontece é o mestre que decide, e a lista abaixo é exemplo e não menu fechado: a ficção anda sem número, você rerrola o que falhou, você tem vantagem, aquilo acontece mesmo se você errar, aquilo simplesmente acontece.

**Uma coisa que o mestre precisa saber antes de escolher, e que não vai no texto de mesa:** essas opções não são do mesmo tamanho. Contra o alvo difícil, rerrolar e dar vantagem valem os **mesmos +25 pontos percentuais**; "acontece mesmo errando" e "sucesso garantido" valem **o dobro**. E as duas famílias correm em sentidos opostos — a vantagem é auto-regulada e dá pouco quando você já ia acertar (9 pp contra alvo fácil), enquanto o garantido vale **mais** quanto mais difícil for a coisa (75 pp contra CD alta), que é justamente quando alguém vai querer dar.

**O que ele resolve no kokusen** é o caso que a proteção contra azar não pega: não a espera longa, mas o momento em que o personagem *precisa*.

### Uma nota de método, registrada e não resolvida

O dossiê defende o gatilho de ficção **contra** a discricionariedade: *"'quando você força energia amaldiçoada além do seu limite, role' é mais arbitrável por cinco mestres diferentes do que 'o mestre decide se pede um teste'"*. Aqui a escolha foi a outra.

O `arquitetura.md` sustenta: *"discricionariedade na ficção é o trabalho do mestre e não atravessa mesas"*. O Limiar acontece uma vez e não fica na ficha — o personagem sai da campanha do mestre A com a mesma ficha, independentemente de quantos Limiares ele abriu. **Está marcado para o playtest**, junto da contagem de lutas, que é a mesma aposta.

## 9. Em aberto

- **As quatro anti-domínio**, travadas até a Expansão existir no manual v7.7.
- **O número de Barreira Simples e Cortina**, e a régua da Aptidão Própria. *A `Energia Reversa` saiu desta linha na v0.78 e está na seção 6.*
- **Se o teto de doze Passivas pesa na mesa.** O manual escolheu cinco por peso, não por orçamento — cada Passiva é uma coisa que o mestre lembra sozinho. A rota de Leque pura chega a doze, e paga por isso com zero aptidões e metade do atributo.
- **Se alguém escolhe o Leque.** Ele é o eixo novo e o único que compra versatilidade em vez de poder. Se ninguém pegar, o aperto de espaços que ele resolve continua resolvido pela linha passiva — e aí ele sai.
- **Se o Limiar sem número na mesa produz mestres que entregam o dobro achando que entregaram o mesmo.**

*Resolvidos e escritos aqui:* o que o refino faz por si só, a trava dele, o terceiro eixo do marco, o teto de Passivas, a fórmula de feitiços conhecidos, e por que a Classe de aptidão mede formato e não tamanho.

---

## 10. O registro de decisão — de onde saiu cada número desta peça

*Movido do `ESTADO-ATUAL.md` nesta versão, inteiro e sem corte.* Ele morava lá porque foi escrito enquanto esta peça ainda era "a próxima"; a peça fechou na v0.27 e o argumento ficou para trás. **Um documento de retomada não é lugar de argumento de peça fechada** — ele é lido no começo de toda conversa, e tinha crescido a ponto de não caber numa leitura só.

Nada aqui foi reescrito. O que segue é o registro de projeto que sustenta os números das seções 1 a 9, e é onde procurar quando alguém perguntar *por que esse valor e não outro*.

### O que já está fechado, e não precisa ser reaberto

| | |
|---|---|
| **A régua** | as aptidões herdam as Classes das Passivas do manual — **Classe Passiva 1** é efeito pequeno, condicional ou de informação; a **2** é reativo, com limite por cena ou descanso; a **3** é permanente e muda como você joga. Não são "mais" e "menos": são **formatos** |
| **O gate** | cada aptidão declara o seu: **nenhum, só nível, só refino, ou os dois**. O Kokusen Melhorado é o primeiro escrito — refino 5 e nível 14 |
| **O preço** | um marco compra **uma aptidão**. Sem moeda nova, sem pontos |
| **O que impede a Classe 3 de comer as outras** | o refino. Uma Classe 1 no refino 10 não é a mesma coisa que no refino 2 — ela cresce junto com você |
| **O refino** | é **a métrica geral das aptidões**: requisito, tamanho e frequência. Entra no texto **como variável**, no molde do manual (*"3 × refino"*, *"refino usos por descanso"*), e **algumas aptidões declaram teto** — nem toda uma usa o valor cheio |
| **Já vem de graça no refino 1** | cobrir-se de energia e canalizar energia. As aptidões compradas *melhoram* o que já existe |
| **Kokusen Melhorado** | aptidão, refino 5 e nível 14. A escada da cascata mexe **só na chance do d100, com teto** — nunca na margem de crítico |
| **O tamanho do catálogo** | **doze a quinze**. Dez já são obrigatórias pela obra, então são poucas inventadas |
| **Quem nunca escolhe refino** | termina com **zero aptidões, e o texto diz isso com todas as letras** — 14 pontos de atributo contra 7, e as duas de graça crescendo com o refino passivo até 8. A rota existe e ninguém deve descobrir no nível 20 que caiu nela sem saber |
| **Aptidão Própria** | existe, e é **uma entrada do catálogo como qualquer outra** — com uma trava: **só pode ser pega uma vez na ficha inteira**, no mesmo molde do Legado. **Classe 1 ou 2, nunca 3.** Vem com catálogo de exemplos, uma métrica para criar e aprovação do mestre. É a energia densa do Hakari e o Punho Divergente do Itadori |

**As doze que a obra obriga:** cobrir-se de energia · canalizar energia · projetar energia · Barreira Simples · Cortina · Domínio Simples · Extensão de Domínio · Pétala · Cesta Oca de Vime · Energia Reversa · Kokusen · Kokusen Melhorado. As duas primeiras são as de graça do refino 1, então **dez são compráveis** antes de qualquer invenção.

**Os quatro anti-domínio ficam como quatro entradas separadas, todas aptidão, e a diferença entre elas é o requisito.** O `arquitetura.md` tinha diagnosticado que eles *"não pertencem ao mesmo degrau"* e proposto virar trilha; a decisão foi manter quatro peças e pôr a diferença no gate, que é a mesma coisa por um caminho mais barato de conferir — **uma rota só, e o validador olha um campo em vez de quatro.**

*Corrigido na v0.29:* esta seção dizia **"Domínio Simples sem gate — é o que se ensina"**. A pesquisa na obra inverteu isso. Quem é sem gate é a **Cesta Oca de Vime**, que é a **predecessora** que o Domínio Simples melhorou — antiga, mais limitada, e por isso a mais barata. O Domínio Simples subiu para Classe 2. Os detalhes estão na seção 6.5 da peça 11.

*Correção de conta:* uma versão desta análise dizia que quatro entradas separadas levariam o catálogo a **dezessete**. Estava errado — os quatro já estavam contados dentro das doze da obra. Com eles separados o catálogo fica em **catorze**, e a escolha não custou nada de faixa. Foi contagem dupla minha, e é a mesma família da lição *"esse número já inclui o que eu estou somando nele?"*.

### A trava do refino, corrigida

O `arquitetura.md` propôs *"aptidão não produz dano e não escala com nível"*, e isso foi escrito antes de existir régua. Com a régua das Classes, a trava que importa é outra, e ela vem da regra que governa tudo:

> **O refino cresce +7 a +9 numa campanha; atributo e maestria crescem +3.**
> **Então refino não pode aparecer de um lado de uma rolagem em que o outro lado não cresce no ritmo dele.**

Isso proíbe refino somando em acerto, CD, defesa, Teste de Resistência ou dano — os quatro têm do outro lado alguém que cresce +3. E **permite refino contra refino**, que é simétrico: o clash de expansões é exatamente esse caso, e ele passa.

O que sobra para o refino escalar: **custo em PE, frequência, alcance, duração, quantos alvos** — e disputa contra outro refino.

### As duas gratuitas — o registro, e uma duplicata que estava velha

**Este pedaço chegou aqui vazio de novidade, e o validador provou isso na hora.**

O texto que morava no `ESTADO-ATUAL` repetia a seção 6.1 inteira — a regra, o argumento do `1/3`, a tabela de saldo da Reação — só que **congelado antes da v0.30**: ele ainda dizia *"gastando PE"*, sem quantidade, quando o preço virou **2 PE** seis versões atrás. Nenhum validador varria o `ESTADO-ATUAL`, então a cópia velha sobreviveu; **no primeiro segundo dentro de uma peça, o `conferir-orcamento.py` acendeu nas duas frases.**

É a lição nº 9 com data: *um número que mora em dois documentos vai divergir* — e o exemplar mais barato de consertar, porque a cópia não tinha leitor.

> **A regra, o preço e as contas moram na seção 6.1.** Não há segunda cópia.

Sobraram dois pedaços que a seção 6.1 não tinha, e só eles ficam:

**O recado para a peça de equipamento.** Cobrir-se não é exclusiva do conjurador: um Vanguarda de refino alto que largue o uniforme chega a **Defesa 20**. Como **Traje e Revestimento desligam** a proteção de energia, a tabela de proteção não compete com 0 — ela compete com **1 no nível 2 e 4 no refino 10**.

> *A frase seguinte era "um uniforme precisa valer mais que proteção 4, senão ninguém veste", e a peça de equipamento a tratou como orientação e não como invariante — tratá-la como invariante travava a peça inteira.* **O uniforme não precisa ganhar de cobrir-se; precisa alcançar e ter chance de passar.** E **o escudo saiu desta lista na v0.42**: ele soma com cobrir-se em vez de desligar, porque desligando ele virava prejuízo já no primeiro marco.

**Canalizar energia** já está escrita na peça 5: *"um feitiço de Forma Toque, sem Melhoria e sem Restrição"*. **O refino não a escala** — ela vive no orçamento do Fundamento, e é o exemplo de aptidão que não usa o valor cheio.

### As três aptidões de kokusen

| | o que faz |
|---|---|
| **Kokusen** | em crítico no corpo a corpo, role d100: **2 × refino** ou menos é kokusen, e o dano leva **+50% depois de tudo resolvido** |
| **Kokusen Melhorado** | **vantagem no d100.** Refino 5 e nível 14. Ganha do `3 ×` em todo refino — 36% contra 30% no refino 10 |
| **`Kokusen Constante`** | sobe a base para **3 × refino**, e a vantagem da `Melhorado` rola em cima. Refino 5, sem gate de nível |

A 2 ×, o refino 10 soma **1,8% de dano por rodada** e leva ~5 sessões até o primeiro; no refino 1 são **47 sessões**, então ele praticamente não existe antes de você investir. **A cascata mexe só na chance do d100, com teto** — fazer a margem cair para 19 renderia +10,9%, dos quais **9,1 vêm do dado a mais** e não do kokusen.

**E o kokusen tem proteção contra azar, zerando por missão.** No refino 1 a espera pelo primeiro kokusen é de **47 sessões** — na prática, a maioria dos jogadores nunca veria um. Cada d100 falhado empurra o próximo em **+2**, e o acumulado zera no descanso longo:

| relógio | refino 1 | refino 5 | refino 10 |
|---|---|---|---|
| sem proteção nenhuma | 47 sessões | 9,5 | 4,7 |
| por cena | 41,2 | 9,3 | 4,7 |
| por dia | 19,9 | 7,6 | 4,3 |
| **por missão** | **~9 a 10** | 5,6 | 3,9 |

**Por missão entrega quase o efeito cheio e quase não move o refino 10** — o socorro vai inteiro para quem não investiu, que é a propriedade que se queria. E o relógio já existe: *por descanso longo* é o quarto da escada da peça 10, o mesmo da Integridade. Nenhum contador novo.

O motivo de "por cena" não servir: o acúmulo só começa a partir do **segundo crítico da mesma cena**, e dois críticos no mesmo combate acontecem em **4,4%** das vezes — ele evapora antes de servir.

Com as três de kokusen, o catálogo fica em **catorze entradas** — doze da obra mais a `Kokusen Constante` mais a Aptidão Própria —, dentro da faixa de doze a quinze.

### O Limiar — mecânica à parte, e o cardápio precisa dizer o tamanho

*Decidido depois da v0.26.* Vem do dossiê, seção 2: **gatilho de ficção antes da rolagem**, roubado do PbtA e do FitD. Aqui ele é **mecânica separada, e quem declara é o mestre** — um gancho com cardápio, e o kokusen é só um dos lugares que o citam.

**O nome passou pela triagem.** *Faísca* morreu dentro de *Faísca em Cadeia* e *Impulso* é Melhoria do manual. **Limiar** está livre nos dois lados.

**O cardápio tem duas alturas, e não uma.** Medido contra o alvo difícil, em que se acerta 50%:

| o que o mestre entrega | vira | ganho |
|---|---|---|
| a ficção anda, sem número | 50% | — |
| rerrolar a que falhou | 75% | **+25 pp** |
| vantagem na rolagem | 75% | **+25 pp** |
| acontece mesmo errando, com custo | 100% | **+50 pp** |
| sucesso garantido | 100% | **+50 pp** |

Rerrolar e vantagem valem **exatamente a mesma coisa**. Sucesso garantido vale **o dobro dos dois**. Se o cardápio for lista solta de sabores, o mestre entrega o dobro achando que entregou o mesmo — é o conserto que a exaustão levou na v0.26, aplicado antes de o erro existir.

E os dois **correm em sentidos opostos**: a vantagem é auto-regulada e dá pouco quando você já ia acertar (9 pp contra alvo fácil); o sucesso garantido vale **mais** quanto mais difícil a coisa for (75 pp contra CD alta) — que é justamente quando o mestre vai querer dar.

**Nota de método, registrada e não resolvida:** o dossiê defende o gatilho de ficção *contra* a discricionariedade — *"é mais arbitrável por cinco mestres do que 'o mestre decide se pede um teste'"*. A escolha aqui foi a outra, e o `arquitetura.md` a sustenta: *"discricionariedade na ficção é o trabalho do mestre e não atravessa mesas"*. O Limiar acontece uma vez e não fica na ficha. **Vai para o playtest junto com a contagem de lutas**, que é a mesma aposta.

### O catálogo fechado — catorze entradas, uma rota

| # | aptidão | gate | o refino escala |
|---|---|---|---|
| 1 | **Cobrir-se de energia** | grátis no refino 1 | proteção `1/3 + 1`, e a RD da Reação `1,5 ×` |
| 2 | **Canalizar energia** | grátis no refino 1 | **nada** — vive no orçamento do Fundamento |
| 3 | **Projetar energia** | — | o dano, entre 8% e 12% da Rotina |
| 4 | **Cesta Oca de Vime** | Classe 1, **sem gate** | **nada** — e não custa PE, porque já custa o turno |
| 5 | **Domínio Simples** | Classe 2 · refino 4, nível 7 | o raio: `1,5 m + refino ÷ 2` |
| 6 | **Pétala** | Classe 2 · refino 4, nível 7 | Acertos devolvidos: `refino ÷ 2` |
| 7 | **Extensão de Domínio** | Classe 3 · refino 7, nível 13 | a duração: `refino` rodadas |
| 8 | **Barreira Simples** | sem gate | a vida do domo: `5 ×` |
| 9 | **Cortina** | exige a `Barreira Simples` | a vida dela: `20 ×` |
| 10 | **Energia Reversa** | Classe Passiva 3 · refino 7, nível 13 | **nada** — o teto é `maior Classe`, e `1d8` de cura por PE |
| 11 | **Kokusen** | — | a chance no d100, `2 ×` |
| 12 | **Kokusen Melhorado** | refino 5, nível 14 | vantagem no d100 |
| 13 | **Kokusen Constante** | refino 5 | a chance, `3 ×` |
| 14 | **Aptidão Própria** | Classe 1 ou 2, **uma vez na ficha** | conforme o que for escrito |

**Todas custam um marco. Nenhuma custa espaço de feitiço** — essa é a moeda das Passivas e da Expansão de Domínio, que ficam do lado do manual.

### O que ainda não foi decidido

> **Destravado na v0.28.** A Expansão tem regra no manual v7.7, então as quatro anti-domínio — Domínio Simples, Pétala, Cesta Oca de Vime e Extensão de Domínio — já podem ser escritas com número. **É a próxima coisa da fila**, e o que elas medem agora existe: Acerto por rolagem na incompleta, Acerto que acontece na completa, barreira de `50 × metade do refino` e duração de `metade do refino` em rodadas.

- **O que cada uma das catorze faz, com número**, e o gate e o teto de refino das que estão marcadas acima.
- **O catálogo das Bênçãos**, e se ele espelha o das aptidões entrada por entrada ou tem lista própria.
- **Como o Acerto e o Efeito se precificam** — a expansão é comprada com espaço de feitiço, e nada diz ainda quanto de cada um cabe por espaço.
- **A métrica da Aptidão Própria.** O `arquitetura.md` sugere a mesma pergunta do Efeito Próprio — *"em quantas cenas por arco isso importa?"*, com o mesmo "na dúvida, erre para o lado que não infla".
- **O teto de cada aptidão**, já que nem toda uma usa o refino cheio — o clash de expansões usa, canalizar não.
- **Se o cardápio do Limiar lista as duas alturas separadas** ou deixa o mestre pesar.
- **Se o d100 falhado empurra o próximo.** A conta está feita: +2 por falha leva o refino 1 de 48 sessões para 8 e quase não move o refino 10 — o socorro vai para quem não investiu. Não foi decidido, e o Limiar pode cobrir o mesmo buraco por outro caminho.
