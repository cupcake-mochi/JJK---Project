# APTIDÕES E DEGRAUS DE REFINO

**Fase 4, décima primeira peça.** O eixo do controle: o que o refino é, o que ele governa, e o que se compra com ele.
Versão v0.27 — 11/08/2026

O `arquitetura.md` chama esta camada de *"o risco maior da estrutura inteira"*, e o motivo está escrito lá: aptidões são uma **segunda economia de poder**, e ela nasceu sem teto. O Fundamento tem orçamento, teto e validador; Barreira Simples, Cortina, Domínio Simples e o resto acontecem em combate e não passam por nenhum deles.

Esta peça existe para dar teto a essa economia. Validador: `conferir-aptidoes.py`.

> **Quatro das catorze entradas do catálogo não estão aqui**, e a seção 7 explica por quê: elas contam o Acerto de uma Expansão de Domínio, e a Expansão só ganha regra na v7.7 do manual. Precificar contra um alvo que não existe é o erro que a v0.24 registrou no ataque extra.

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
> **Refino** — mais um de refino, e uma aptidão.
> **Leque** — mais um feitiço, que só pode ser feitiço, e uma Passiva.

**Por que o terceiro eixo existe.** Passiva custa espaço de feitiço conhecido, e a Expansão de Domínio também. Sem uma rota que devolva espaço, quem monta técnica funda fica sem lista: três Passivas de Classe 2 mais a Expansão completa chegavam ao **nível 20 com dois feitiços**, e a montagem cheia — cinco Passivas de Classe 3 mais Expansão — era **impossível em qualquer nível**. O teto de *"cinco Passivas pagas"* do manual já era letra morta.

A linha passiva do marco sozinha conserta isso:

| montagem | nv14 | nv20 | nv26 | nv30 |
|---|---|---|---|---|
| só feitiço | 12 | 16 | 21 | 24 |
| 3 Passivas Classe 2 | 6 | 10 | 15 | 18 |
| 3 Passivas Classe 2 + Expansão completa | 3 | **7** | 12 | 15 |
| 5 Passivas Classe 3 + Expansão completa | 0 | 0 | **3** | 6 |

### As três não se substituem, e é isso que as equilibra

`+1 feitiço e uma Passiva` empata com `+1 refino e uma aptidão` porque **Passiva e aptidão vivem na mesma escada de Classe** — as duas são efeito pequeno, reativo ou permanente, nas mesmas três alturas. O que sobra dos dois lados é `+1 feitiço` contra `+1 refino`.

E aí a conta fecha sozinha: **refino não vale nada para quem não tem aptidão.** Quem escolhe Leque sete vezes tem zero aptidões, então o refino dele é um número morto. Quem escolhe refino tem sete aptidões e nenhuma Passiva a mais para querer. Nenhuma das três precisa de trava porque nenhuma compra o que a outra compra.

No nível 30, as três rotas puras:

| rota | atributo | refino | aptidões | Passivas | feitiços a mais |
|---|---|---|---|---|---|
| sempre Corpo | **14** | 8 | 0 | 5 | 0 |
| sempre Refino | 7 | **10** | **7** | 5 | 0 |
| sempre Leque | 7 | 8 | 0 | **12** | **7** |

**O teto de Passivas sobe junto, e a grátis traz a própria vaga.** Cada escolha de Leque aumenta o máximo em um, e a Passiva concedida ocupa a vaga nova — então as **pagas continuam sendo cinco**, exatamente as cinco de sempre. O teto não cresce de verdade; ele abre lugar para o que a rota concede.

### Feitiços conhecidos

> **`2 + (nível ÷ 2)`, arredondando para baixo — mais um por marco.**

Três no nível 2: dois de toda ficha, mais o do próprio nível 2. Essa soma é o que confundia dois documentos: o manual dizia *"treze no nível 20"* e a peça 8 dizia *"dois no nível 2"*, e os dois não fechavam. A fórmula dá **doze no nível 20**, e o manual corrige o número na v7.7.

### Quem nunca escolhe Refino termina com zero aptidões

**E isso está escrito de propósito, aqui, para ninguém descobrir no nível 20.** A rota existe, ela é legítima, e o que ela troca é claro: **catorze pontos de atributo contra sete**. Quem foca corpo é o dobro de atributo de quem foca controle.

Ele também não fica sem nada. **Cobrir-se de energia e canalizar energia vêm de graça no refino 1**, e as duas crescem com o refino passivo, que chega a 8 sem escolha nenhuma. O que ele nunca vai ter é Energia Reversa nem Barreira Simples.

## 4. As Classes de aptidão

As aptidões herdam a escada das Passivas do manual. **Ela não mede quanto — mede o quê.**

| Classe | o que cabe |
|---|---|
| **1** | efeito pequeno, condicional, ou de informação |
| **2** | efeito reativo, com limite de uso por cena ou por descanso |
| **3** | permanente. Muda como você joga |

Uma Classe 3 não é "uma Classe 1 maior": é uma coisa de outro formato. **Farejador** — *"você sente se alguém conjurou num lugar nas últimas 24 horas"* — não fica obsoleta porque uma permanente existe; ela faz algo que nenhuma permanente faz.

**E o que impede a Classe 3 de comer as outras duas é o refino.** Um marco compra uma aptidão de qualquer Classe que o seu refino alcance, e se a Classe medisse tamanho, ninguém olharia para a Classe 1 depois de destravar a 3 — mesmo preço, efeito maior. Com o refino escalando o que a aptidão entrega, **uma Classe 1 no refino 10 não é a mesma coisa que no refino 2**. Ela cresce junto com você.

> **A aptidão não custa espaço de feitiço.** Essa é a moeda das Passivas e da Expansão de Domínio, e as duas economias ficam separadas de propósito: uma muda de preço sem obrigar a outra a ser refeita.

## 5. O gate, e por que ele não é só nível

**Cada aptidão declara o próprio requisito: nenhum, só nível, só refino, ou os dois.**

A régua herdada das Passivas gateia por **nível** — Classe 1 no 1, Classe 2 no 7, Classe 3 no 13. Sozinha, ela não serve aqui, e a conta mostra por quê: com gate só de nível, **quem escolhe refino uma vez, no nível 26, compra uma Classe 3 na hora** — o mesmo acesso de quem investiu seis vezes. A ficção do refino some.

Um gate de refino separa:

| gate | especialista | meio a meio | generalista |
|---|---|---|---|
| Classe 2 no refino 4 | nível 10 | nível 10 | nível 14 |
| Classe 3 no refino 7 | nível 14 | nível 18 | **nível 26** |

Doze níveis entre o especialista e o generalista, que é o tamanho que *"quase ninguém consegue"* pede.

**E guardar marco não guarda refino.** A rota que espera — atributo cedo, refino tarde — não domina, porque o refino passivo sobe sozinho e ela chega ao nível 22 com refino 5, ainda precisando de outro marco para alcançar o 7. Ela troca quatro aptidões por quatro pontos de atributo, e as três que sobram são Classe 3. É a mesma escolha por outro caminho, não um atalho.

## 6. O catálogo — as que têm número

### Cobrir-se de energia · grátis no refino 1

> **Sem uniforme, sem armadura e sem escudo, a sua proteção é `1/3 do refino + 1`.**
> **Como Reação, você concentra a energia no impacto:** Redução de Dano de `1,5 × refino` num golpe, gastando PE — e você fica sem a proteção passiva até o fim do seu próximo turno.

Ela existe para o feiticeiro que não tem corpo. Quem zerou Destreza sai de ser acertado 80% das vezes para 60% no nível 30; quem investiu em Destreza e veste uniforme continua nos 50%. **É piso, não teto.**

A Reação é o momento do Todo contra o Mahito, e o `1,5 ×` é o que a faz valer a campanha inteira. Com `1 × refino` ela viraria armadilha: o custo de ficar um turno sem proteção cresce junto com o golpe do chefe, e a RD trava no teto 10.

| nível | RD | golpe de chefe | custo esperado | saldo |
|---|---|---|---|---|
| 6 | 4 | 17 | 1,7 | **+2,3** |
| 14 | 10 | 36 | 5,3 | +4,7 |
| 22 | 15 | 54 | 10,8 | +4,2 |
| 30 | 15 | 72 | 14,4 | **+0,6** |

Positiva do começo ao fim, e o saldo **encolhe** em vez de virar — forte quando você não tem outra resposta, e só mais uma opção quando já tem. **E ela não é redução de dano passiva:** custa Reação, custa PE e custa a proteção de um turno. A regra que matou a Casca continua valendo.

*Um recado para a peça de equipamento:* no refino 10 ela dá proteção 4, e um Vanguarda que largue o uniforme chega a Defesa 20 contra os 17 dele fardado. **Um uniforme precisa valer mais que 4**, senão ele nasce morto.

### Canalizar energia · grátis no refino 1

Já está escrita na peça 5: *"um golpe canalizado é um feitiço de Forma Toque, sem Melhoria e sem Restrição. Mesma Classe, mesmo orçamento de pontos, mesmo custo em PE."*

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

### A terceira de kokusen

> **A base sobe para `3 × refino`.**

Trinta por cento no teto. É a única das três que mexe no número em vez do dado, e por isso é a que se lê de cara na hora de escolher.

**A cascata mexe só na chance do d100, e com teto.** Dobrar a chance no refino 5 rende **+0,9 ponto**; fazer a margem cair para 19 rende **+10,9%** — e **9,1 desses pontos vêm do dado a mais, antes de o kokusen entrar**. A margem carrega o crítico inteiro junto, e é por isso que ela está fora.

E "mais fácil depois do primeiro" sem teto é a espiral da exaustão com o sinal trocado: quem crita mais fácil crita mais, e crita mais fácil ainda. Sem teto, quatro degraus numa cena levariam o físico a **1,8× o dano base**, e aí a coluna Rotina para de valer no meio da luta.

## 7. As oito que faltam, e por que

**Quatro estão bloqueadas pela mesma coisa.** Domínio Simples, Pétala, Cesta Oca de Vime e Extensão de Domínio contam o **Acerto** de uma Expansão de Domínio — e a Expansão só ganha regra na **v7.7 do manual**. Escrever o preço delas agora seria precificar contra um alvo que não existe, que é o erro que a v0.24 registrou no ataque extra: conta, argumento e correção prontos, e nenhum dono escrito.

**E o laço entre as duas coisas é o que torna as duas possíveis.** A Expansão completa acerta **garantido** — é isso que o terceiro espaço compra. Um acerto que nunca falha só é jogável porque a resposta a ele é barata: os quatro anti-domínio são **aptidões de marco**, ao alcance de qualquer ficha que escolha o eixo do controle. Se fossem raros, o acerto garantido seria opressivo.

**Quatro faltam por número, e não por dependência:**

| aptidão | o que ela é | contra o que precisa ser medida |
|---|---|---|
| **Energia Reversa** | a cura aprendida, que gasta PE | a Passiva **Recomposição**, que é a cura inata: `5 × maior Classe`, uma vez por descanso curto |
| **Barreira Simples** | bloqueia passagem e linha de efeito | a Melhoria **Anteparo** do manual, que faz coisa parecida por orçamento |
| **Cortina** | o véu que esconde de quem não é feiticeiro | nada — ela não tem efeito de combate, e o teste dela é de cena |
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
- **O número de Energia Reversa, Barreira Simples e Cortina**, e a régua da Aptidão Própria.
- **Se o teto de doze Passivas pesa na mesa.** O manual escolheu cinco por peso, não por orçamento — cada Passiva é uma coisa que o mestre lembra sozinho. A rota de Leque pura chega a doze, e paga por isso com zero aptidões e metade do atributo.
- **Se alguém escolhe o Leque.** Ele é o eixo novo e o único que compra versatilidade em vez de poder. Se ninguém pegar, o aperto de espaços que ele resolve continua resolvido pela linha passiva — e aí ele sai.
- **Se o Limiar sem número na mesa produz mestres que entregam o dobro achando que entregaram o mesmo.**

*Resolvidos e escritos aqui:* o que o refino faz por si só, a trava dele, o terceiro eixo do marco, o teto de Passivas, a fórmula de feitiços conhecidos, e por que a Classe de aptidão mede formato e não tamanho.
