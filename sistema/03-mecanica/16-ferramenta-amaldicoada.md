# Ferramenta amaldiçoada

**Fase 4, décima sexta peça.** A arma forjada para canalizar energia — o que ela é, o que ela dá, quando ela entra na ficha e por que ela não é uma arma com mais pontos.

*Fechada na v0.59. A máquina é da v0.55, o catálogo da v0.56 e da v0.57, e o `conferir-ferramenta.py` com dezesseis checagens entrou junto com esta peça. O rascunho que a produziu foi apagado ao virar peça — o argumento dele está nas entradas da v0.54 à v0.59 do `logs/CHANGELOG.md`, e este documento é o dono de tudo que está escrito aqui.*

Ela existe por uma dívida escrita em quatro documentos, não por vontade de ter itens mágicos. A peça 5 §3 diz que a Maki *"só compete porque a ferramenta amaldiçoada carrega a energia por ela"*; a peça 5 §5 deixou o preço dela em aberto; a peça 14 §8 mandou ela para tópico próprio; e a peça 13 §8 tem **duas vagas de Desliga** esperando o alvo que só esta peça cria.

---

## 1. O que ela é, em três linhas

> **Uma ferramenta amaldiçoada é uma das 52 armas da peça 14 — ou um objeto de apoio — mais UM `Estigma`.**
>
> **Ela fere maldição. Isso é binário: ou fere, ou não fere.**
>
> **Uma ferramenta que você não sintonizou é uma arma comum, e nada mais.**

A terceira linha é a que deixa esta peça existir sem furar Equipamento. A arma por baixo continua gastando o **fundo exato** que a peça 14 §5 cobra — `3` numa mão, `5` em duas —, e o `Estigma` é camada por cima, nunca ponto a mais. **O catálogo das 52 continua sendo o chão.**

E a primeira linha resolve a pendência da peça 5 sem inventar economia: ferir maldição é a porta que separa o feiticeiro da pessoa comum, e a ferramenta é o jeito que a obra dá para quem não tem energia atravessar essa porta.

## 2. Por que grau não pode ser "mais ponto de arma"

Esta seção não é justificativa: é a conta que escolheu o formato, e ela fecha nas duas pontas.

O ponto de arma tem valor **absoluto** — `0,33` de dano por rodada, pela régua da peça 14 §5 — e a Rotina da peça 6 §3 cresce. Então a mesma ferramenta encolhe sozinha:

| nível | Rotina | 1 ponto vale | **+5 pontos** — dobrar uma arma de duas mãos |
|---|---|---|---|
| 2 | 13 | 2,5% | **12,7%** |
| 10 | 45 | 0,7% | 3,7% |
| 18 | 76 | 0,4% | 2,2% |
| **30** | **108** | **0,3%** | **1,5%** |

> **No nível 30, dobrar o orçamento inteiro de uma arma de duas mãos vale `1,5%` da Rotina** — contra os **6% a 9%** que a peça 14 §4 diz que uma **Trilha inteira** vale.

A Lança Invertida do Céu não pode valer um sétimo de uma Trilha. *E o inverso morde igual:* no nível 2 os mesmos 5 pontos são **12,7%**, que é mais que uma Trilha inteira. **A régua de magnitude é grande demais embaixo e pequena demais em cima** — é o formato errado, não um número mal escolhido.

### 2.1 E ela não é o que faz o sem-energia competir em dano

*Esta é a que muda o desenho, e ela contradiz a leitura fácil da peça 5 §3.*

A arma comum **não escala**: o dado é fixo e o atributo topa em 6. A Rotina escala.

| nível | Rotina | melhor arma do sistema (`d12` + Força 6) | % da Rotina | o que falta |
|---|---|---|---|---|
| 2 | 13 | 12,5 | **96%** | 0,5 |
| 10 | 45 | 12,5 | 28% | 32,5 |
| 18 | 76 | 12,5 | 16% | 63,5 |
| **30** | **108** | **12,5** | **12%** | **95,5** |

> **Uma ferramenta que tivesse de fechar essa distância precisaria entregar 95 de dano por rodada no nível 30. Isso é o Fundamento inteiro, não é um item.**

Então a divisão de trabalho cai da conta:

| quem | o que entrega | formato |
|---|---|---|
| **ferramenta amaldiçoada** | **ferir maldição** | **binário** |
| **`Técnica Marcial`** | o dano por rodada da rota sem energia | magnitude, e ela é peça |

*A frase da peça 5 §3 está certa e é sobre a **porta**, não sobre o tamanho.* E isso desarma sozinho o medo da peça 5 §5 — *"cara o suficiente para não virar o padrão"*: se ela entrega porta e não dano, **ela não pode virar o padrão do feiticeiro**, que já tem a porta de graça pelo feitiço de Toque.

### 2.2 E o grau não pendura na patente

A ideia óbvia — *"feiticeiro de Grau 2 porta ferramenta de grau 2"* — bate de frente na peça 12 §2, que escreveu isto para rejeitar *"Grau dá mais XP"*:

> *"**Grau é reconhecimento; nível é poder.** Se o Grau passar a dar XP, ele vira nível com outro nome — e pior, vira **espiral fechada**."*

**Trocar "XP" por "ferramenta" não muda uma vírgula do argumento.** Sobe de patente → ferramenta melhor → mais poder → mais feito → sobe de patente.

> **Fica escrito, com todas as letras, porque a colisão é de expectativa e não de palavra:** *a sua patente não decide que ferramenta você pode portar, e a ferramenta que você porta não mexe na sua patente.* **São duas escadas de cinco casas com o mesmo nome, e elas não se tocam em lugar nenhum.**

O nome `Grau` fica. No material os dois **são** a mesma escada de propósito — a fonte diz que ferramenta e objeto amaldiçoado *"são ranqueados de forma idêntica, pela força da energia"* —, e trocar por outra palavra criaria um segundo vocabulário para uma coisa que a obra tem uma só.

## 3. A escada de grau, e o que cada degrau dá

**O grau não decide o tamanho do `Estigma`. Decide o formato dele.**

| grau | `Estigma` | gate | exemplar do material |
|---|---|---|---|
| **4** | **nenhum.** Ela fere maldição, e é só isso | **nenhum** | a katana da Kasumi, a semi-ferramenta |
| **3** | **Classe 1** — efeito pequeno, condicional ou de informação | **nenhum** | a espada do Toji, o machado da Mei Mei |
| **2** | **Classe 2** — reativo, com limite por cena ou descanso | **nível 7** | a Katana de Alma Partida |
| **1** | **Classe 3** — permanente, muda como você joga | **nível 13** | as forjadas de topo |
| **especial** | **Classe 3**, e ela é **única no mundo** | **nível 13** | Nuvem Divertida · Lança Invertida do Céu · Corrente de Mil Milhas |

**O grau 4 não é o degrau fraco: é o degrau que faz a peça existir.** Ferir maldição é a única coisa que a Maki e o Toji não conseguem sozinhos. *Um grau que não dá efeito nenhum é o mais importante da escada.*

As Classes são as da **peça 11 §4**, sem inventar nada, e a frase de lá vale aqui inteira: *não são "mais" e "menos", são formatos*.

### 3.1 O gate cai da peça 11, e a metade de refino fica de fora

Um `Estigma` de Classe 3 no nível 2 passaria por cima do gate que a peça 11 cobra de uma **aptidão da mesma Classe**. Então o gate é o dela, lido da **peça 11 §6**: a Cesta Oca de Vime (Classe 1) **não tem gate**; o Domínio Simples e a Pétala (Classe 2) pedem **nível 7**; a Extensão de Domínio (Classe 3) pede **nível 13**.

> **A metade de refino do gate NÃO entra, e isso é decisão.** A peça 11 cobra *nível e refino*. Cobrar refino aqui **trancaria a peça na cara de quem ela existe para atender** — a Restrição Celestial pelo ramo da Maki (peça 9 §5) não tem refino nenhum, porque não tem energia. *O gate herda o número e recusa o eixo.*

**Não existe gate de refino em lugar nenhum desta peça.** Não é esquecimento nem economia de texto: é invariante, e o validador falha se algum aparecer.

### 3.2 O que separa grau 1 de especial é escassez, e não mecânica

Os dois dão um `Estigma` de Classe 3. A diferença é de ficção: grau 1 se forja; **especial é uma só que existe**, com nome próprio. Nuvem Divertida, Lança Invertida do Céu e Corrente de Mil Milhas são objetos únicos, não categorias de produto.

**Isso é zero número novo**, e o que ele governa é a mão do mestre: uma especial aparece uma vez por arco, e não duas na mesma mesa.

## 4. `Desgaste` — a restrição que compra o gate

> **`Desgaste` — a ferramenta ignora o gate de nível do `Estigma` dela.**
> **Em troca ela se gasta: a cada missão em que o `Estigma` foi usado, ela desce um grau. No grau 4 ela é arma comum, e não volta.**

A máquina é da casa e já foi validada — é o §5.0.4 de Equipamento, onde `Volumosa`, `Embainhada` e `Comprida` devolvem 1 ponto, uma camada acima. **Restrição de verdade compra acesso.**

**E ele compra o GATE e nunca a Classe, de propósito.** Classe é **formato**, e a peça 11 §4 escreve isso com todas as letras; uma restrição que subisse a Classe estaria misturando formato com magnitude, que é o eixo que este projeto separa desde a v0.30. **O gate é número puro — nível 7, nível 13 —, e número é o que se compra.**

**O prazo tem tamanho medido:** a peça 12 §5 diz que um nível custa de **1 a 10 missões padrão**. Uma ferramenta de grau 1 com `Desgaste` dura **três missões** de uso antes de virar arma comum — perto de um nível inteiro de campanha na faixa baixa, e uma fração na alta.

*É a Corda Negra: trabalho de Lança Invertida na mão de quem não tem nível para isso, e ela não dura.*

## 5. O teto na ficha, e ele é de mão

> **A arma tem teto pelas mãos. O apoio tem teto de duas.**

| ficha do mesmo nível | `Estigmas` |
|---|---|
| mestre avaro — arma grau 4, sem apoio | **0** |
| caso normal — uma arma com `Estigma` | 1 |
| **teto declarado** — arma mais dois apoios | **3** |
| extremo — duas armas de uma mão mais dois apoios | 4 |

**A divergência inteira entre o mestre mais avaro e o mais generoso da Guilda é de um a três `Estigmas`.** Não existe a ficha com cinco ferramentas: as mãos não deixam do lado da arma, e o teto de dois fecha o outro. *Num server com cinco a sete mestres, quem entrega o item é a maior fonte de divergência que existe — e é por isso que o teto é de estrutura e não de bom senso.*

**E o tamanho disso tem moeda no projeto.** Um `Estigma` de Classe 3 é o mesmo formato de uma **aptidão** de Classe 3, e aptidão se compra com escolha de marco — que são **sete na campanha inteira**, pela peça 2 §3:

| `Estigmas` na ficha | do orçamento de escolha de marco |
|---|---|
| 1 | 14% |
| **3 — o teto declarado** | **43%** |
| 4 — o extremo | 57% |

## 6. O catálogo — onze `Estigma`

A régua é a das Classes da **peça 11 §4**, e o degrau de cada entrada foi derivado dela, não escolhido depois. **Nenhuma das onze dá dado de dano, nenhuma cresce com refino, nenhuma soma número numa rolagem disputada** — rodado entrada por entrada.

### Classe 1 · grau 3 — efeito pequeno, condicional ou de informação

| `Estigma` | o que faz | de onde veio |
|---|---|---|
| **`Fiel`** | ela volta para a sua mão no seu turno. **Não dá para te desarmar dela** | a espada-mão do Haruta, na versão pequena |
| **`Aferido`** | ao encostar numa maldição, **você sabe o grau dela** | a instituição classifica por grau, e ninguém sabe olhando |
| **`Presságio`** | ela avisa que há maldição perto, **antes de você ver** | — |
| **`Perene`** | ela não quebra, não enferruja e funciona onde arma comum não funciona | as forjadas antigas que atravessam eras |

> **O `Presságio` existe por causa de uma ficha específica, e vale escrever qual.** A Restrição Celestial pelo ramo da Maki não tem **Sentir Energia** — está na peça 9 §5, junto de *sem PE* e *sem feitiço de Toque*. **É a única perícia do sistema que uma Origem inteira não pode ter**, e a ferramenta é o jeito que a obra dá para ela compensar. *A entrada não foi desenhada e depois justificada: ela saiu do buraco.*

### Classe 2 · grau 2 — reativo, com limite de uso por cena ou por descanso

| `Estigma` | o que faz | de onde veio |
|---|---|---|
| **`Quebranto`** | **Reação:** anula um feitiço que ia te acertar. Uma vez por cena | a Corda Negra, *"perturba e cancela técnica alheia"* |
| **`Avulsa`** | **Reação:** a arma sai da sua mão e faz o ataque sozinha | a espada-mão do Haruta |
| **`Bojo`** | uma vez por descanso curto, ela **guarda um feitiço que você lançou e o devolve sem custo de PE** | o Osso de Dragão, *"acumula e ejeta energia"* |

*O `Bojo` cobra em **custo**, que é um dos eixos que a peça 11 §2 autoriza por escrito. Ele é o único dos onze que só serve a feiticeiro, e isso é aceito: **grau 4 é a entrada de quem não tem energia**, e o resto da escada não precisa ser neutro.*

### Classe 3 · grau 1 e especial — permanente, muda como você joga

| `Estigma` | o que faz | de onde veio |
|---|---|---|
| **`Anátema`** | **o contato anula técnica amaldiçoada** | a Lança Invertida do Céu |
| **`Cisão`** | o golpe dela **causa dano de alma no lugar do dano de vida** | a Katana de Alma Partida |
| **`Insondável`** | enquanto a ponta dela estiver escondida, o alcance dela é **na cena** | a Corrente de Mil Milhas |
| **`Contrapeso`** | ela **ignora o requisito de Força** da arma | a Nuvem Divertida, que qualquer um empunha |

> **O `Cisão` é Classe 3 e não Classe 2, e a obra é quem manda.** A Katana de Alma Partida não faz uma coisa uma vez por cena — **ela corta a alma, sempre**, e é isso que ela é.
>
> **E permanente aqui não é upgrade, o que é o que faz ele caber.** A Integridade é `20 + 8 × (nível − 1)` e não tem Caminho nem Constituição dentro. **Trocar dano de vida por dano de alma é pior contra quatro dos cinco Caminhos e melhor contra um** — é troca, não escada. *É literalmente o que "muda como você joga" quer dizer.*

*O `Insondável` usa as três faixas de alcance que a peça 15 fixou — **no combate · na cena · fora da cena** —, em vez de criar metragem própria. **Um número, um dono.***

*E o `Contrapeso` foi medido pelo motivo contrário:* ele vale `+2,0` de dano médio para quem tem Força 0 a 2, e **zero** para quem tem Força 3. **O gate de nível 13 é o que o segura:** no primeiro nível em que ele pode existir ele vale **3,5%** da Rotina, e cai para **1,6%** no nível 30. *Encolhe com o nível, que é o oposto de derivar.*

### A que foi arrancada, e por quê

**A `Vazadura`** ignorava a Redução de Dano do alvo, e saiu na v0.57 depois de escrita. *Ela tinha passado na conta* — a fração que ela anula anda só 3,3 pontos percentuais em vinte e oito níveis, então ela não derivava —, **e passar na conta não é o mesmo que ser uma boa regra.** A RD é o produto que a peça 11 §6 vende por 2 PE, e um item que a apaga é um item que responde a uma escolha de outro jogador com um "não".

*Fica registrado porque o método é o que sobrevive: a conta diz o que é legal, e ela não diz o que deve existir.* No lugar dela entrou o `Bojo`, e o catálogo continua com onze.

## 7. Quando ela entra na mesa — ritmo, e não gate

**Esta seção não cria requisito.** O único gate desta peça é o do §3.1, lido da peça 11 §6. O que está aqui é a régua de entrega, para o mestre não precisar adivinhar sozinho.

| grau | ritmo sugerido | por faixa, se a mesa preferir espalhar |
|---|---|---|
| 4 | nível **2** | 2 a 6 |
| 3 | nível **10** | 7 a 12 |
| 2 | nível **18** | 13 a 17 |
| 1 | nível **26** | 18 a 23 |
| especial | nível **30** | 24 a 29 |

A coluna do meio segue a cadência de marco da peça 2 §3 — um marco sim, um não —, e é a que o D&D ancora melhor: lá o lendário aparece no tier de níveis 11 a 16, que aqui daria por volta do 18.

> **Por que ritmo e não gate, já que os números existem.** *Decisão da v0.59.* Se esta tabela fosse gate duro, ela seria **estritamente mais dura que a do §3.1 em toda linha** — 18 contra 7, 26 contra 13 —, e duas coisas morreriam junto:
>
> - **o gate herdado da peça 11 nunca chegaria a valer**, e a checagem que confere que ele é lido de lá viraria trivialmente verdadeira: perturbar a Extensão de Domínio na peça 11 para 1, 8 ou 18 deixaria o gate do grau 1 parado em 26 nos três casos;
> - **o `Desgaste` viraria no-op**, porque ele apaga o gate do `Estigma` (7 e 13) e o da ferramenta (18 e 26) continuaria de pé. A Corda Negra deixaria de existir.
>
> E o §3.2 já tinha dito o que segura o topo, e não é número: **escassez.** Uma especial é única no mundo. *Um gate de nível para uma coisa que só existe uma vez é cinto em cima de suspensório.*

**Uma ferramenta por faixa de grau, entregue neste ritmo, dá cinco na campanha inteira** — mesma ordem de grandeza dos dois Legados por ficha e das sete escolhas de marco.

## 8. O que o validador confere

O `conferir-ferramenta.py` roda **dezesseis checagens**, e **nenhum valor fica escrito dentro dele**: teto, gate, fundo, Rotina e orçamento saem dos documentos donos. O único bloco com número na mão é o `LIMITES DE DESIGN`, declarado à parte da regra aplicada — que é a lição nº 8.

| # | o que ela confere | de onde ela lê | o teste negativo |
|---|---|---|---|
| 1 | a camada não fura o fundo de Equipamento | peça 14 §5 | dar um passo de dado a uma ferramenta acende |
| 2 | **um** `Estigma` por ferramenta, nunca dois | esta peça §1 | uma entrada com dois acende |
| 3 | o gate lido da peça 11 §6, nunca de constante | peça 11 §6 | perturbar a Extensão de Domínio faz o gate do grau 1 andar junto |
| 4 | nenhum gate de refino em lugar nenhum | esta peça, texto | pedir refino numa entrada acende |
| 5 | `Desgaste` compra o gate e nunca a Classe | esta peça §4 | subir Classe por `Desgaste` acende |
| 6 | o teto de `Estigmas` na ficha, com busca exaustiva | peça 14 §5 · peça 2 §3 | teto de apoio em 5 faz a ficha passar de 57% do orçamento de marco |
| 7 | cada grau declara **uma** Classe, e ela existe | peça 11 §4 | grau com Classe inexistente acende |
| 8 | nenhum grau dá dado de dano nem número que cresça com refino | esta peça §6 | um `d6` numa entrada acende |
| 9 | a escada de grau lida do documento dono | esta peça §3 | perturbar a escada acende |
| 10 | patente e grau não se tocam em lugar nenhum do texto | peça 12 §2 | ligar os dois acende |
| 11 | dominância entre graus, por rota de proteção | peça 14 §5 | um grau dominado acende |
| 12 | o somatório, contra o `conferir-orcamento.py` | o piso do bolso | efeito de grau que custe PE entra no bolso |
| 13 | a rota sem energia nenhuma, medida ponta a ponta | peça 9 §5 | a rota da Maki sem acesso acende |
| 14 | triagem de todo nome que a peça cria | o manual | nome colidindo acende |
| 15 | as duas vagas de Desliga da peça 13 §8 | peça 13 §8 | vaga sem alvo legal acende |
| 16 | ferramenta não sintonizada = arma comum, nos dois sentidos | esta peça §1 | efeito sem pagamento acende |

**A checagem 3 e a checagem 9 leem a mesma amarra por dois lados, e o par está declarado.** A 3 confere que o gate vem da peça 11; a 9 confere que a escada de grau vem daqui. Elas não são independentes: se a escada do §7 virasse gate, a 3 morreria e a 9 continuaria verde sozinha. *Declarar o par é o que impede a dupla de sair verde por motivos que se cancelam.*

**E o catálogo se conta, nunca se guarda.** O validador não sabe que são onze — ele conta as linhas das três tabelas do §6 e confere a soma contra o que o texto afirma. *Número que descreve uma lista que mora em outro documento envelhece a cada edição daquele documento, e este já desatualizou três vezes no projeto.*

## 9. O que ela destrava, e o que fica em aberto

| destrava | como |
|---|---|
| **`Técnica Marcial`** | ela precisa desta para a Maki e o Toji **ferirem maldição**. *Esta linha dizia "é a peça seguinte" e ela deu ao projeto duas respostas para "o que vem agora" — **corrigida na v0.103, por decisão do Mizuki: as próximas são as três Trilhas do Evocador***
| **2 das 9 rotas de Origem** | Corpo Amaldiçoado e Restrição Celestial ramo Maki — **6/9 → 8/9** |
| **2 das 7 vagas de Desliga** | a `Armaria` do Descendente e a Restrição Celestial, as duas na peça 13 §8 |

**O que ela não destrava:** Trilha nenhuma, e nenhuma peça de regra. *Ela é acesso, não economia nova.*

**Em aberto:**

- **Os nomes próprios das ferramentas do material**, se uma versão futura publicar um catálogo de itens além do catálogo de `Estigma`. Hoje a peça entrega a máquina e as onze entradas; a Nuvem Divertida e a Lança Invertida aparecem como exemplar, não como ficha.
- ~~**A penalidade por empunhar sem treino ou sem requisito.**~~ **Fechada na v0.104, na peça 19 §6.** *Sem treino é desvantagem na rolagem de ataque; sem o requisito de Força o deslocamento cai `3 m`.* **Ela vale para ferramenta amaldiçoada igual, porque a ferramenta usa a mesma tabela de arma da peça 14.**
- **O objeto amaldiçoado é outra peça**, e a fonte é explícita: *"com exceção de ferramentas amaldiçoadas e cadáveres amaldiçoados, itens que contêm energia amaldiçoada são chamados de objetos amaldiçoados"*. O cubo que prendeu o Gojo é objeto, não ferramenta. Ele fecha 1 vaga de Desliga e mais nada, e a v0.50 o pôs em último por isso.
