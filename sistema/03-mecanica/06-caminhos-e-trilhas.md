# CAMINHOS E TRILHAS

**Fase 4, sexta peça.** O quadro de Caminhos, as Trilhas, e o que cada um pode conceder sem quebrar a economia do Fundamento.
Versão v0.14, corrigida na v0.15, na v0.16 e na v0.24 — 08/08/2026

Esta peça revisa e substitui a seção 4 da peça anterior.

---

## 1. Os cinco Caminhos

Nomes conferidos contra o manual — nenhum é termo definido lá. *Linha de Frente*, *Ponta de Lança*, *Retaguarda* e *Leitura* eram rótulos de rascunho; **Leitura** em particular já aparecia três vezes no Fundamento e precisava sair.

| Caminho | O que ele é | Atributos naturais |
|---|---|---|
| **Bastião** | o corpo como resposta: aguentar, encarar, prender | Força, Constituição |
| **Vanguarda** | a arma como resposta: alcançar, cortar, acabar | Destreza, Força |
| **Guia** | o outro como resposta: estender, recuperar, reposicionar | Essência |
| **Emanador** | a técnica como resposta: mais feitiço, mais aptidão | Inteligência, Essência |
| **Evocador** | o que você trouxe como resposta: invocações | Inteligência, Essência |

### Uma colisão que a checagem pegou

*Canalizador* era a escolha para o Caminho de técnica e **não passa** — não pelo manual, onde a palavra está livre, mas pelo próprio material do projeto.

**Canalizar Energia é a aptidão do lutador físico**, e "golpe canalizado" é o nome da mecânica central dele. As duas palavras aparecem 31 vezes nos arquivos do projeto, todas descrevendo o que o **Bastião** e a **Vanguarda** fazem. Nomear o Caminho de técnica de Canalizador colocaria a palavra apontando para os dois lados ao mesmo tempo.

Renomear a mecânica sairia mais caro: *canalizar energia* é termo da própria obra e já estava na lista de aptidões. Então quem muda é o nome do Caminho. **Emanador** está livre no manual e em todo o material do projeto, e a distinção fica limpa: **canalizar** é empurrar energia por dentro do corpo e da arma; **emanar** é soltar energia para fora. Um é o Bastião e a Vanguarda; o outro é o Emanador.

**Sem multiclasse.** Um Caminho por personagem, e dentro dele **Trilhas**.

**A primeira Trilha vem na criação, junto do Caminho.** *Decidido na v0.27, aplicado na v0.34.* Ela é identidade, não recompensa — o Caminho diz o seu lugar na equipe e a Trilha diz quem você é dentro dele, e as duas coisas nascem com o personagem. Esta seção dizia que *"as escolhas de nível compram Trilhas"*, e isso vinha de contar a partir do nível 1 numa ficha que nasce no 2: é o mesmo engano que a v0.28 achou na contagem de feitiços.

**As Trilhas seguintes, essas sim, se acumulam com o nível** — é isso que permite o Guia pegar Energia Reversa antes da hora, ou o Bastião pegar um pé em feitiço. **Quantas, e em que níveis, é a peça de Trilhas**, junto com o que cada uma entrega com número.

## 2. As Trilhas

Três por Caminho. **Os nomes foram fechados na v0.24**, quando o `conferir-nomes.py` passou os quinze pela checagem nas duas direções e reprovou seis.

### Bastião

| Trilha | O que faz |
|---|---|
| **Muro** | tanque puro. O corpo é o escudo: absorve, redireciona, não sai do lugar |
| **Punho** | meio tanque, meio dano. Vários golpes médios, uma pitada de controle |
| **Brasa** | meio tanque, meio feitiço. Conjura pequeno e bate na sequência |

### Vanguarda

| Trilha | O que faz |
|---|---|
| **Estocada** | versátil com um pé em feitiço. O molde do Yuta |
| **Batedor** | distância: arco, arma de fogo, o que atinge longe |
| **Executor** | arma e corpo, sem meio-termo. É o guerreiro puro do quadro |

As três respondem a mesma pergunta — *como você alcança o inimigo* — de jeitos que não se sobrepõem: a Estocada com um pé em feitiço, o Batedor sem encostar, o Executor só encostando.

### Guia

| Trilha | O que faz |
|---|---|
| **Elo** | estende o que outro fez: duração, alcance, quantos alvos |
| **Sutura** | recuperação — PE, condição, Integridade. É aqui que Energia Reversa chega cedo |
| **Perímetro** | controla o campo: reposiciona aliado e inimigo, nega movimento |

O Guia era o que você não sabia preencher, e o motivo é bom: **buff e debuff moram na técnica, e cura é Forma de feitiço.** Sobra pouco se o Caminho tentar competir nesses eixos. A saída é ele não competir — ele **alcança**. Não cria o efeito; faz o efeito de outra pessoa durar mais, pegar mais gente ou chegar mais longe. E a Sutura resolve o caso concreto que você levantou: liberar a aptidão de Energia Reversa antes do refino permitir.

**O Guia é o único Caminho sem rota para ataque extra** (seção 3), e isso é decisão da v0.24: quem quiser lutar de Guia paga pela técnica, no orçamento do Fundamento, como todo mundo. O que as três Trilhas dele entregam em troca de um golpe por rodada é a pergunta que a peça de Trilhas precisa responder com número.

### Emanador

| Trilha | O que faz |
|---|---|
| **Torrente** | mais de um feitiço acima de Classe 0 por rodada, a um custo |
| **Repertório** | aptidões extras — nunca refino |
| **Arremate** | conjurador de perto: feitiço e golpe na mesma troca |

### Evocador

| Trilha | O que faz |
|---|---|
| **Servo** | uma invocação, forte. O molde do Megumi com o Mahoraga |
| **Matilha** | muitas invocações fracas. O molde do Geto |
| **Coro** | lutar junto delas: o seu golpe e o delas se encadeiam |

---

## 3. Ataque extra: passa, com uma correção

Você pediu que os Caminhos físicos ganhem ataque extra e os meio-arcanos não. **A conta aprova**, e por um motivo que vale registrar. *Quem ganha, e em que nível, está na seção 3.1 — isso ficou sem ser escrito da v0.14 até a v0.24.*

A coluna Rotina do Fundamento **já é "feitiço + Classe 0"**. O conjurador sempre teve dois golpes por rodada: um grande e um pequeno. Então o ataque extra do físico não é um privilégio — é o espelho do Classe 0.

| nível | Rotina | conjurador (Classe + C0) | físico (canalizado + golpe simples) |
|---|---|---|---|
| 2 | 13 | 18 | 22 |
| 10 | 45 | 45 | 50 |
| 18 | 81 | 72 | 78 |
| 30 | 126 | 99 | 106 |

**A correção:** o golpe canalizado **não soma arma nem Força**. Ele *é* o feitiço; arma e Força são o que você faz quando **não** canaliza. Se o canalizado somasse os dois e ainda houvesse ataque extra:

| nível | Rotina | canalizado + arma + Força, dois golpes | quanto passa |
|---|---|---|---|
| 2 | 13 | 30 | **+135%** |
| 10 | 45 | 60 | **+32%** |
| 18 | 81 | 88 | +9% |

Então a regra fica em três linhas, e ela espelha a regra de ouro nº 6 do Fundamento:

> **Golpe canalizado** = os dados da Classe, e nada mais. É o feitiço.
> **Golpe simples** = arma + Força. É o Classe 0 físico.
> **Um canalizado por turno.** Ataque extra é sempre golpe simples.

## 3.1 Quem ganha ataque extra, e em que nível

*Escrito na v0.24.* Da v0.14 até aqui, o ataque extra tinha conta, argumento e correção — e **nunca tinha dono**. O único texto era "os Caminhos físicos ganham e os meio-arcanos não", que é a mesma divisão em duas famílias que a seção 5 desta peça registra como tendo deixado o Guia sem número de PE. Ela não cobre os cinco Caminhos, e o achado da v0.20 sobre o Guia dependia inteiro de como ela fosse resolvida.

> **Bastião e Vanguarda ganham ataque extra no nível 6**, pelo Caminho.
> **Arremate e Coro ganham pela Trilha**, quando o personagem a compra.
> **O Guia não ganha por nenhuma rota.**

O nível 6 é o primeiro marco, e é onde o resto do sistema já entrega coisa.

**Num Caminho de técnica, ataque extra é trocar, não somar.** O Arremate e o Coro trocam o Classe 0 pelo golpe simples; eles não passam a ter três ataques. A diferença não é estética:

| nível | Rotina | somar o golpe (3 ações) | trocar o Classe 0 (2 ações) |
|---|---|---|---|
| 2 | 13 | 21 · **+61%** | 22 · +69% |
| 10 | 45 | 55 · **+22%** | 50 · +11% |
| 18 | 81 | 90 · **+11%** | 78 · −4% |
| 30 | 126 | 127 · +1% | 106 · −16% |

Trocando, o conjurador de perto cai exatamente na linha do físico, que esta seção já aprovou. Somando, ele vira a terceira ação por rodada — e a seção 4, logo abaixo, prova que ação a mais por rodada não tem conserto por preço. Pior: o **único** argumento que aprova o ataque extra é que a Rotina já é "feitiço + Classe 0". Somar quebra o espelho que o argumento usa.

**O Coro não custa nada a mais**, e isso cai de graça da regra da seção 4: o dono e todas as invocações somados entregam **uma** Rotina. É teto de saída, não de número de ações. Os dois golpes do dono e o da invocação continuam saindo do mesmo orçamento — as ações se redistribuem, o dano não sobe. A exceção de economia de ação que estava em aberto no Coro já estava paga.

**E o Guia fica coerente ficando de fora.** Ele é o único Caminho que não oferece um segundo golpe; quem quiser lutar de Guia paga pela técnica, no orçamento do Fundamento, como todo mundo. Isso troca o achado nº 2 da v0.20 — *"o Guia pode estar dominado pela Vanguarda"* — por uma pergunta fechada e mensurável: **o que Elo, Sutura e Perímetro entregam que valha um golpe por rodada?** A peça de Trilhas responde com número.

## 4. Invocação: não passa como está

Este é o risco maior do pacote inteiro, e ele não tem conserto por preço.

| nível | Rotina do dono | + 1 invocação que age | + 3 (horda) |
|---|---|---|---|
| 10 | 45 | 90 | 180 |
| 20 | ~99 | 198 | 396 |
| 30 | 126 | 252 | **504** |

**Uma invocação que age sozinha dobra o dano por rodada. Uma horda de três quadruplica.** Nenhum preço em PE conserta isso, porque o problema não é recurso — é **economia de ação**. Mais corpos agindo por rodada é a coisa que quebra todo sistema d20, sem exceção.

### O conserto: a invocação divide o seu orçamento

> **Você e todas as suas invocações somados entregam uma Rotina.**
> Com uma invocação, cada um entrega metade. Com três, cada um entrega um quarto.

Isso resolve tudo de uma vez e — o melhor — **entrega exatamente a fantasia que você descreveu**, sem regra extra:

- **Servo** tem uma invocação forte: metade da Rotina em cada, um corpo a mais no campo.
- **Matilha** tem muitos corpos fracos: um quinto da Rotina em cada, cinco corpos no campo.
- **Coro** encadeia: o dono e a invocação somam a mesma Rotina, mas de lugares diferentes.

O invocador troca **dano pessoal por presença de tabuleiro** — corpos que absorvem ataque, flanqueiam e bloqueiam caminho. Não é menos poderoso; é poderoso em outro eixo, que é o que o Caminho deveria fazer.

E é a leitura correta da obra: as maldições do Geto individualmente são frágeis. O que assusta é o número.

## 5. Energia: fixa pelo Caminho, sem atributo

> **PE por nível: 6 no Emanador e no Evocador. 5 na Vanguarda e no Guia. 4 no Bastião.**
> **E o PE máximo é esse número × o seu nível** — sem atributo e sem valor inicial (peça 1, seção 5.3).

*Revisado na v0.19.* Virou uma escada de três degraus, e ela tem uma contraparte: cada Caminho também tem a **sua própria vida por nível**, correndo no sentido contrário. A tabela completa está na peça 1, seção 5.1.

*A fórmula do máximo entrou na v0.26*, e está na peça 1, seção 5.3. A tabela de *"quantas vezes você lança o seu melhor feitiço"* do manual já é `6 × nível` nos seis pontos que mostra, então ela concorda — mas concordar não é a mesma coisa que mandar, e a seção 5.3 explica por quê.

| | Bastião | Vanguarda | Guia | Evocador | Emanador |
|---|---|---|---|---|---|
| vida por nível | 7 | 5 | 5 | 4 | 4 |
| PE por nível | 4 | 5 | 5 | 6 | 6 |
| **soma** | **11** | **10** | **10** | **10** | **10** |

**A soma é o número que importa.** Com ela praticamente igual nos cinco, a troca "couro contra combustível" é escolha de sabor e não degrau de poder — e o validador falha se a diferença passar de 2.

*Corrigido na v0.15, revisado na v0.19.* A regra original dizia "6 nos Caminhos de técnica, 4 nos físicos", e o **Guia não era nem um nem outro** — ficava sem número. A divisão em duas famílias não cobria os cinco Caminhos, então ela virou uma escada de três degraus com cada Caminho nomeado.

O Guia e a Vanguarda ficam no meio, em 5. Os dois vivem entre bater e conjurar: o Guia estende efeito alheio e recupera, a Vanguarda alterna golpe canalizado com golpe simples. Nenhum dos dois é conjurador puro nem lutador puro, e o 5 diz isso.

**O 6 do Emanador e do Evocador é o número mais caro de mexer**, porque o Fundamento tem uma tabela inteira de "quantas vezes você lança o seu melhor feitiço" calculada em cima dele. *Corrigido na v0.26:* isto não é o mesmo que "não é escolha nossa", que era como estava escrito. **É escolha nossa** — os limitadores do manual foram calibrados quando o sistema em volta era outro, e servem de continuidade, não de lei. Baixar o 6 é legal; o que não é legal é baixar sem regerar a coluna, porque aí a tabela do manual passa a mentir sobre a ficha. O 4 e o 5 são mais baratos porque não têm coluna pendurada neles.

Espírito **não entra na conta**, e o motivo é uma dicotomia que não tem meio-termo:

| fórmula | Espírito 0 | Espírito 6 | diferença | veredito |
|---|---|---|---|---|
| 6 + Espírito/2 | 6 | 9 | +50% | atributo obrigatório |
| 6 + Espírito/3 | 6 | 8 | +33% | ainda pesado |
| 6 + Espírito/4 | 6 | 7 | +17% | ruído — um ponto no teto |

Com teto de atributo em 6, qualquer divisor grande o bastante para não criar imposto entrega **um ponto** na ficha inteira. Ou o atributo importa de verdade e vira obrigatório — o que a peça 1 evitou de propósito ao tirar atributo da conta do feitiço —, ou ele não importa e não deveria estar na fórmula ocupando espaço na cabeça de quem lê. Não há faixa útil entre os dois.

**A base de 6 fica** porque o Fundamento tem uma tabela inteira de "quantas vezes você lança o seu melhor feitiço" calculada em cima dela. Baixar para 4 seria um corte de 33% que invalida aqueles números.

**O Bastião fica com 4**, e a assimetria é justa: **o golpe simples dele rende ~10 e o Classe 0 do conjurador rende ~4,5**. Menos combustível, melhor motor de reserva — e ele é quem tem mais couro para aguentar enquanto o combustível não volta.

## 6. Múltiplos atributos por Caminho: passa, e já estava previsto

Sua quarta observação está certa e o mecanismo já existe na lista do que um Caminho pode conceder: **trocar o valor fixo de 2 do ataque de conjuração por um atributo.**

- **Emanador** conjura com Inteligência ou Essência.
- **Bastião** canaliza com Força.
- **Vanguarda** canaliza com Destreza.

A troca é **neutra em balanço** porque os dois crescem +3 na campanha — foi exatamente isso que a peça 1 verificou. E ela não cria imposto porque é opcional: quem não quiser especializar fica no 2 fixo e não perde nada.

Para as **habilidades** de Trilha, não há restrição nenhuma: elas podem chavear em qualquer atributo que faça sentido. Nada nelas entra numa rolagem disputada onde o ritmo importa.

## 7. Perícias: a lista precisa crescer

> *Resolvido na v0.15, revisado na v0.16.* O quadro completo está em `07-pericias-e-oficios.md`: **vinte e três perícias e onze ofícios**, com o Caminho dando **duas perícias fixas mais quatro à escolha livre**, e um ofício fixo mais um livre. A análise abaixo é o que levou a isso e fica registrada. Note que **Sentir Energia mora em Essência** desde a v0.16, não em Inteligência.

Você quer 6 a 8 perícias por Caminho, e um sistema recheado. A lista de catorze não suporta isso:

| lista | treinadas (Caminho 7 + Origem 2) | fração |
|---|---|---|
| 14 perícias | 9 | **64%** — quase tudo |
| 26 perícias | 9 | 35% — sobra espaço para o grupo |

Com 64% treinado, "ser treinado" para de significar alguma coisa e o resto do grupo não tem em que brilhar.

**Proposta: expandir para 24 a 28 perícias**, cobrindo o que você quer de fora de combate — burocracia jujutsu, clãs e política, primeiros socorros, culinária, condução, ofícios, artes, línguas, sobrevivência urbana, rastreio, interrogatório. E aí 7 por Caminho fica confortável.

A lista definitiva sai junto com o quadro de perícias completo, que é peça própria.

## 8. Treinamento em equipamento

Confirmado que precisa existir. Três categorias, e cada Caminho concede as suas:

- **Armas:** simples, marciais, de fogo, ferramentas amaldiçoadas
- **Proteção:** leve, pesada (com requisito de Força e limite de Destreza na Defesa)
- **Escudo:** categoria própria, porque ele ocupa uma mão — e mão ocupada conversa com a Restrição **Gesto**, que já existe e exige as duas mãos livres

Esse último ponto é um achado pequeno mas real: **escudo e Gesto se cancelam.** Quem usa escudo não pode montar feitiço com a Restrição Gesto, e isso é uma decisão de ficha interessante em vez de um bug.

## 9. Em aberto

- **Quantas Trilhas um personagem acumula** ao longo da campanha, e em que níveis.
- **Como Torrente cobra o segundo feitiço da rodada.** Uma lista de pontos à parte é o modelo mais provável, e ela precisa ser precificada contra a regra de ouro nº 6. **É o mesmo defeito da seção 4** — mais de uma ação por rodada —, e o conserto que funcionou lá provavelmente serve aqui: *os feitiços que você lança numa rodada, somados, entregam uma Rotina*.
- **O que Elo, Sutura e Perímetro entregam** que valha o golpe por rodada que o Guia não tem (seção 3.1).

*Resolvidos e tirados daqui:* os **nomes das Trilhas**, fechados na v0.24 — as seis que colidiam viraram Batedor, Executor, Sutura, Perímetro, Servo e Matilha, e o `conferir-nomes.py` falha se alguma voltar. E **se o Coro deixa o dono e a invocação agirem no mesmo turno**: deixa, e não custa nada, porque o orçamento dividido da seção 4 é teto de saída e não de número de ações (seção 3.1).
