# Legados — a régua de magnitude e o catálogo

**As duas metades fecharam.** A régua veio na v0.37, o catálogo na v0.38 — **oitenta e uma entradas, sete listas de Origem, mais o `Sem Técnica`.**

A peça 9 continua dona das Origens, dos traços e de qual lista você lê. **O que mora aqui é a régua de magnitude e o catálogo inteiro.**

> **A ficha leva dois Legados: um Destranca, obrigatório, e mais um de qualquer lista da sua Origem.**

O validador desta peça é o **`conferir-legados.py`**, e ele lê tudo que confere dos documentos donos — os quatro degraus da peça 10, as Origens da peça 9, e as contagens da própria pasta. Nunca do próprio código.

---

## 1. O defeito que esta régua existe para pegar

*Registrado na v0.24, e ele não é quantidade.*

Hoje são catorze Legados, dois por Origem, e a faixa entre eles vai de **Irmãos** — você sente quando outro Feto está por perto, zero em rolagem — a **Não Sou Gente**, que era imunidade a veneno, a doença e ao que ataca corpo humano. *O `Não Sou Gente` saiu do catálogo nesta mesma peça: ele virou Passiva paga com espaço de feitiço.*

A trava escrita na peça 9 é *"não produz dano e não escala com nível"*. **Ela não pega imunidade**, e vale entender por quê, porque o motivo decide o formato da régua.

Ela guarda os dois eixos que o resto do sistema usa: **dano**, que é o que um Caminho não pode conceder, e **crescimento contra nível**, que é a regra que governa tudo — numa rolagem disputada, os dois lados crescem no mesmo ritmo. Imunidade não é nenhum dos dois. Ela não produz dano e não cresce com nível. Ela é constante, e é enorme.

O eixo que falta é um terceiro, e o sistema nunca precisou dele antes: **quanto do jogo a coisa desliga.** Nada mais aqui tem permissão de desligar nada — feitiço resolve por Acerto ou Teste de Resistência, aptidão rola, Caminho não dá dado. **O Legado é o único lugar do sistema onde *"isso simplesmente não me acontece"* está na mesa.**

E tem uma frase no manual que ninguém tinha cruzado com este catálogo:

> **IMUNIDADE — Nenhuma Melhoria fura imunidade. Quem quiser isso monta uma Passiva de Regra Própria com o mestre, com limite de uma vez por cena.**

Ou seja: **imunidade é absoluta neste sistema**, e o preço de furar uma é uma Passiva feita à mão, negociada, limitada a uma vez por cena. O Legado que concede imunidade entrega **de graça, na criação, para uma Origem inteira**, aquilo cujo antídoto o manual cobra caro e ainda raciona.

*Isso é a lição nº 6 acontecendo pelo lado contrário.* Lá, a Passiva Casca cobrava por *"dano físico"* e a expressão não existia no manual. Aqui a palavra existe, tem regra dura pendurada nela, e o catálogo a usou sem olhar.

## 2. A máquina que já existe passa nos catorze

Antes de escrever régua nova, rodei a que já existe. O teste de dominância da peça 3 — *A domina B se os ganhos de A contêm os de B e os custos de A cabem nos de B* — nas sete listas de Origem:

> **Zero dominâncias estritas.** Nenhum Legado contém outro.

Isso não absolve o catálogo. Explica por que ninguém pegou o problema em catorze versões: **a máquina existente mede contenção, e o defeito registrado é distância.** São coisas diferentes, e a segunda passa inteira pela primeira.

E tem uma consequência que decide a forma. Tentei pôr os catorze numa coluna só e não fecha — *"+25 pp uma vez por sessão"*, *"imune a veneno"* e *"você consegue audiência"* não têm unidade comum. Uma régua que os ranqueasse na mesma escala estaria **inventando o denominador**, que é a lição nº 8 entrando por outra porta.

## 3. Por que ela não é escada de preço

As duas réguas de magnitude que o projeto já tem são escadas, e as duas têm um degrau porque têm o que comprar:

| régua | os degraus | o que os separa |
|---|---|---|
| Restrições (peça 3) | Leve · Média | quanto cada uma **devolve** de turno |
| Passivas e aptidões (peça 11) | Classe 1 · 2 · 3 | são **formatos** comprados com um marco |

**Legado não tem o que comprar.** Um na criação, nunca outro, igual para todo mundo — a peça 9 fecha isso com todas as letras, e o motivo está escrito: é a terceira economia de poder do sistema, então ela nasce com o teto mínimo.

Com preço único e escolha permanente, **uma escada seria régua sem moeda**: o degrau de cima é só melhor, e quem escolheu por sabor descobre no nível 20 que pegou o pequeno. É o mesmo cuidado da rota que nunca escolhe Refino — lá o projeto decidiu que *"o texto diz isso com todas as letras"* em vez de deixar alguém cair sem saber.

> **Então: um teto só, igual para os catorze e para os vinte e cinco — mas medido por formato, porque os formatos não se comparam entre si.**

## 4. Os três formatos

Todo Legado declara qual é. **Não são "grande" e "pequeno": são coisas diferentes**, no mesmo espírito das Classes do manual.

| formato | o que ele faz | exemplos de hoje |
|---|---|---|
| **Ajusta** | mexe num número de uma rolagem | Aprendi Apanhando · Não Sou Só Eu · Corpo Emprestado · Instinto Bruto |
| **Desliga** | uma coisa deixa de te acontecer | Máscara · Peso Real · Sangue que Não é Sangue · Ferro Velho |
| **Destranca** | nada muda de número, nada é desligado — abre acesso ou informação | O Sobrenome · A Voz de Dentro · O Que Ninguém Lembra · Irmãos |

> **⚠⚠ Esta tabela estava errada em três das doze entradas, e ficou assim da v0.39 até a v0.104.** *Ela citava `Treino de Berço` como `Ajusta` — ele virou `Destranca` na própria v0.39, para não colidir com o `Costume Antigo`. Citava `Corpo Emprestado` como `Desliga` — ele virou `Ajusta` na mesma versão, quando a trava do formato o reprovou. E citava `Não Sou Gente`, que **saiu do catálogo** e virou Passiva paga com espaço de feitiço.*
>
> **A causa é de método e vale mais que o conserto:** *a v0.39 escreveu a régua, converteu os Legados que ela reprovava, e não voltou nas tabelas em prosa que citavam aqueles Legados **como exemplo**.* **Nenhum validador alcançava esta tabela**, porque ela é ilustração e não regra — e ilustração errada na porta de entrada de uma peça é o que a mesa lê primeiro. *Desde a v0.104 o `conferir-legados.py` lê os doze nomes daqui e cobra cada um contra o formato que o catálogo dá a ele.*

*Os três nomes passaram pela triagem, e um morreu nela:* **Abre** está dentro de **Abre Ferida**, que é Melhoria do manual — a mesma morte da *Faísca* dentro de *Faísca em Cadeia*. **Destranca** ficou porque é a única palavra livre que cobre as duas coisas que o formato faz: o Sobrenome dá acesso e a Voz de Dentro dá informação, e destrancar é o que os dois têm em comum.

## 5. A trava de cada formato

### Ajusta — o relógio, e a largura do gatilho escolhe o degrau

Uma rerrolagem tem teto natural, e o projeto já mediu esse número duas vezes:

| chance base | com a rerrolagem | ganho |
|---|---|---|
| 30% | 51% | +21 pp |
| **50%** | **75%** | **+25 pp** |
| 70% | 91% | +21 pp |

**+25 pp no pico** — exatamente o que um degrau de exaustão tira e o que o degrau do meio do Limiar dá. Rerrolagem e vantagem valem a mesma coisa; isso está medido na seção do Limiar e continua valendo aqui.

O teto não é o problema. **O problema é quantas vezes ele acontece**, e aí entra a escada de relógios da peça 10:

| relógio | rolagens no período | ganho médio por rolagem |
|---|---|---|
| por cena | 4,7 | **+5,32 pp** |
| por descanso curto | 6,3 | +3,94 pp |
| por dia | 25,4 | +0,98 pp |
| por descanso longo | 50,9 | +0,49 pp |

*As rolagens por período saem das âncoras que já existem:* combate de 3,4 a 4,0 rodadas na peça 1, e três lutas de graça por dia na peça 10.

**A âncora de preço é a Melhoria Adianta.** A peça 3 mediu ela em **4 a 7 pontos percentuais** de efeito médio, por um **preço Médio** — preço de verdade, pago dentro do feitiço. Um Legado custa zero. O denominador dos dois não é idêntico, mas a ordem de grandeza é a mesma, e ela diz uma coisa desconfortável:

> **"Por cena" com gatilho largo entrega de graça o que uma Média entrega paga.**

Por isso a trava não é um relógio fixo. É o par:

> **Largura é contável: quantas coisas nomeadas o gatilho alcança.**
> **Até três** — um Teste de Resistência nomeado, uma perícia, duas situações escritas: pode ser **por cena**.
> **Uma categoria inteira** — qualquer perícia (23), qualquer Teste de Resistência (4), qualquer ofício (10): desce para **por dia**.

*A contagem não é preciosismo.* A primeira versão desta trava dizia só *"gatilho estreito ou largo"*, e isso é binário sem critério — dois mestres aprovando um Legado Próprio divergiriam em *"qualquer perícia física"*. **Contando, o corte separa o catálogo existente sem nenhuma discussão**, e o validador conta sozinho. É o conserto que a skill de design manda dar: troque *"o mestre decide quanto"* por faixa com critério.

**E tem uma coisa que a contagem revela:** quando o gatilho alcança **uma** perícia nomeada, o relógio quase não morde — quem limita é a frequência da própria perícia. Instinto Bruto vale até +20 pp quando dispara, mas só em Intuição, que sai ~1 vez em 20 rolagens; o efeito médio na ficha é **1,0 pp**, com ou sem relógio. *"Por cena" num gatilho de alcance 1 é seguro por construção, não por generosidade* — e é por isso que a trava mede largura antes de medir relógio.

#### Todo Ajusta tem relógio. Não existe Ajusta permanente.

> **Um Legado que mexe em número de rolagem declara um degrau da escada da peça 10. Sempre.**

Isto fecha um buraco que a revisão desta régua encontrou: **Treino de Berço** — *"treine mais uma perícia"* — é Ajusta e não tinha relógio nenhum, e a trava, como estava escrita, só falava de largura e degrau. O número dele nunca foi o problema: `+maestria` numa perícia vale **0,25 a 3,0 pp médios** na ficha, que é a faixa do "por dia". O problema era a **regra não ter caso** para a forma.

**Havia duas saídas e a escolhida foi a estreita.** A outra era escrever um terceiro caso — *Ajusta permanente, alcance 1, proibido de tocar acerto, CD, defesa, Teste de Resistência e dano*, reusando a cerca do refino da peça 11. Ela funcionava e custava uma regra a mais. **Proibir custa reescrever um Legado que estava certo, e ganha uma trava com uma linha só:** todo Ajusta tem degrau, e o validador confere procurando o degrau, sem precisar decidir se aquilo é permanente.

*O preço está registrado porque ele é real:* `Treino de Berço` dizia *"treine mais uma perícia"*, que é a mesma moeda que a Origem e o Caminho já distribuem e se lê sem explicação. Com a proibição ele vira uma peça com relógio, e *"treinei a vida inteira"* passa a ser dito como *"uma vez por cena"*.

É a mesma forma da régua das Restrições, que também não é uma escala e sim um par de conjuntos. E ela **ratifica quase tudo que já estava escrito** em vez de mandar reescrever — que foi exatamente o que aconteceu quando a régua das Restrições apareceu e dez das onze fecharam de primeira.

**O relógio sai da escada da peça 10, e só de lá.** Os quatro degraus são de tempo de ficção: por cena, por descanso curto, por dia, por descanso longo. Isso não é preferência — é o filtro multi-mestre, e a seção 7 mostra o estrago com número.

### Desliga — não encosta no dano, porque o dano já tem dois donos

Este é o formato que a trava velha não alcançava. A primeira versão desta seção dizia que ele *"não tem como ser precificado, porque o denominador está no Bestiário e o Bestiário não existe"*.

**Estava errado, e o erro era não ter procurado.** A escada existe, está no manual, e ela tem dois degraus:

| degrau | o que é | quem já cobra por ele | dá para furar? |
|---|---|---|---|
| **resistência** | o dano daquele tipo cai pela metade, antes de qualquer outra conta | a Passiva **Escama** — custa um espaço de feitiço conhecido | **sim.** *"Feitiços daquele tema ignoram resistência ao seu tipo de dano"* |
| **imunidade** | absoluto | nada no Fundamento concede | **não.** Só Passiva de Regra Própria, com o mestre, 1×/cena |

E o manual ainda fecha o degrau de baixo por dentro: *"Ela é sempre presa a um tipo — **não existe resistência a tudo**."*

Com isso a trava se escreve sozinha, e ela é mais simples do que a que eu tinha proposto:

> **Um Desliga apaga o que ninguém comprou, e enfraquece o que alguém comprou. Nunca imunidade.**
> **Dano não, de jeito nenhum** — imunidade é absoluta e o antídoto dela é uma Passiva feita à mão; resistência a `Escama` já cobra por um espaço de feitiço. *Este é o único absoluto da trava.*
> **Condição pode, com relógio.** *Desde a v0.104 cada condição tem **nível** — `Leve`, `Média` ou `Pesada` —, e o nível é o preço dela no manual.* **Apagar de graça o que alguém paga continua proibido; apagar uma vez, com relógio, é o enfraquecer.**
> **E o degrau do relógio sai do nível da condição**, não do gosto de quem escreve: `Leve` → **por cena** · `Média` → **por dia** · `Pesada` → **por descanso longo**.
> **O que ninguém comprou continua sendo o território largo dele:** o que o mundo faz com você fora do feitiço, sem relógio. Uma coisa nomeada, uma só.
> **E ele escreve o que custa em troca, no próprio texto.**

> ***Decisão do Mizuki na v0.104.*** *A trava anterior dizia só **"apaga o que ninguém comprou"**, e com ela as cinco vagas destravadas pela peça 19 não tinham como ser preenchidas — toda condição passou a ter preço.* **A relaxação é escrita em cima do que a própria peça 19 criou:** o nível é número, então ele pode escolher o degrau do relógio em vez de simplesmente barrar a porta.
>
> **A fronteira com o `Ajusta` não some, e é isto que segura a relaxação:** um `Desliga` de condição **apaga aquela vez**; um `Ajusta` de condição **põe um dado no meio**. *O `Corpo Emprestado` e o `Já Morri` continuam `Ajusta` porque é isso que eles fazem — vantagem no Teste de Resistência é mexer num número de uma rolagem.* **São dois jeitos diferentes de encostar na mesma condição, e agora os dois são legais.**

**A regra apareceu depois de os primeiros Desliga estarem escritos, e ela reprovou três deles.** *Desconfiado* apagava Enfeitiçado, *Corpo Emprestado* apagava Incapacitado e *Já Morri* apagava Amedrontado — as três eram **Condição Maior** e custavam **Pesada** no manual da época, e nada na trava anterior me impediu de escrever os três. A trava dizia só *"não encosta no dano"* e parava ali.

**Os três viraram Ajusta com vantagem no Teste de Resistência**, que é o conserto que a própria peça já previa: *trocar a negação por rerrolagem, e a condição deixa de ser absoluta.* Vantagem e rerrolagem valem os mesmos +25 pp no pico — o efeito para o jogador quase não muda, e o que muda é que **agora existe um dado no meio**, e o conjurador que pagou Pesada tem chance de o dinheiro dele valer alguma coisa.

*E é assim que se lê o que sobrou:* os Desliga que passam — não ser reconhecido pelo catálogo, dormir em qualquer lugar, aparecer como outro na percepção de energia, não ser localizado — **nenhum deles apaga coisa que saiu de uma tabela de preço.** Eles apagam o que o mundo faz com você de graça.

**Isso não é régua nova: é a régua do manual aplicada a um catálogo que nunca foi cruzado com ela.** E é o mesmo desfecho da régua das Restrições, onde dez das onze fecharam de primeira — aqui **dois dos quatro `Desliga` da época passam intactos**, e o que cai é exatamente o que estava registrado desde a v0.24:

| os quatro `Desliga` que existiam na v0.39 | o que ele apaga | passou? |
|---|---|---|
| **Corpo Emprestado** | incapacitação por ferimento — **condição** | **não** — virou `Ajusta` |
| **Sangue que Não é Sangue** | comer, dormir, respirar — necessidade | **sim** |
| **Peso Real** | ser enganado por ferramenta, barreira e véu — informação | **sim** |
| **Não Sou Gente** | veneno, doença e o que ataca corpo humano — **dano** | **não** — saiu do catálogo |

*Esta tabela é a primeira passada da régua, na v0.39, e fica como registro dela.* **Os `Desliga` de hoje são sete** — `Inédito` e `Chão Duro` no Latente, `Máscara` no Receptáculo, `Coleira` no Descendente, `Ferro Velho` no Corpo Amaldiçoado, `Sangue que Não é Sangue` no Feto e `Peso Real` na Restrição Celestial —, e nenhum deles apaga coisa que tenha preço em tabela.

A cláusula de troca também não é enfeite: **o catálogo já gravita para ela sozinho.** Não Sou Gente diz *"cura que funciona em humano também não"*; Sangue que Não é Sangue diz *"cria problemas que os outros não têm"*; Irmãos diz *"ele sente você"*. A régua só transforma o hábito em regra.

### Destranca — quem dispara é o jogador

O teto aqui já é zero, porque nada nele encosta em número. **O que falta neste formato é piso** — e o piso tem duas cláusulas, porque a segunda veio de fora e é mais exigente que a primeira.

> **1. Um Destranca precisa de um gatilho que o jogador consiga puxar.**
> **2. E ele tem que dizer alguma coisa sobre o mundo que só esse personagem pode dizer.**

#### A cláusula 1 tem dois casos, e o segundo estava sendo usado sem estar escrito

*Aberto na v0.38, quando a lista do Corpo Amaldiçoado bateu nisso — mas o exemplar mais velho é da primeira lista de todas.*

| tipo | o gatilho é | exemplos |
|---|---|---|
| **Destranca de ação** | uma coisa que o jogador **faz**, quando ele quer | O Sobrenome · A Voz de Dentro · O Que Ele Quer · O Jeito Errado |
| **Destranca de identidade** | **a própria escolha**, feita uma vez na criação | Sem Patente · De Antes de Você · as quatro configurações do Corpo Amaldiçoado |

**O `Sem Patente` do Latente é de identidade e passou na régua sem ninguém reparar** — *"você nunca entrou na instituição, e ela sabe disso"* não tem gatilho nenhum, e nunca precisou de um. A cláusula estava escrita para o primeiro tipo e aplicada aos dois.

**O que segura o segundo tipo é o teste dos 90%, e ele segura sozinho:** ninguém deixa em branco a linha que diz **o que ele é**. Um Destranca de identidade não corre o risco que a cláusula 1 existe para evitar — o do **Irmãos**, que é uma coisa que *acontece com você* e que você não alcança.

> **A diferença que decide: identidade o jogador escolheu; o Irmãos foi escolhido por ele.**

**E um Destranca de identidade não pendura tarefa.** Ele diz o que você é e para. *Escrever "aponte para uma coisa da cena e diga qual dos três teria sabido" é transformar identidade em dever de casa* — e a pior versão disso é obrigar o mundo a reagir, que é enredo tirado do mestre sem ele ter pedido.

**A segunda cláusula não é gosto meu: é o que separa os dois desfechos conhecidos deste formato.** Levantamento de como outros sistemas escrevem traço de origem escolhido uma vez:

| como é escrito | exemplo | o que acontece na mesa |
|---|---|---|
| traço narrativo solto | os Traços, Ideais, Vínculos e Falhas do D&D 5e | **fica em branco ~90% das vezes.** A edição de 2024 removeu os quatro |
| trocado por mecânica | a mesma edição trocou a *feature* de antecedente por um **talento de origem** | funciona — mas aí virou Ajusta ou Desliga, não Destranca |
| **reivindicação sobre o mundo** | o *One Unique Thing* do 13th Age | funciona **sem mecânica nenhuma**, porque é algo verdadeiro sobre aquele personagem *e só ele*, e deixa **o jogador definir algo do mundo** |
| narrativo preso a uma moeda | Blades in the Dark paga **XP** quando você expressa herança e antecedente | funciona porque o narrativo compra mecânica |

**A primeira linha é a forma exata do Irmãos**, e é a razão de ele ser o piso do catálogo: nem mecânica, nem reivindicação que o jogador faz. O **Sobrenome**, do lado oposto, passa nas duas cláusulas — o jogador dispara quando quer audiência, e a existência daquele nome na sociedade jujutsu é uma afirmação sobre o mundo.

> **O teste dos 90%, e ele vale para os três formatos:** se o jogador puder deixar essa linha da ficha em branco e nada mudar, ela **é** a linha que vai ficar em branco.

O contraexemplo mora no catálogo: **Irmãos só acende quando o mestre põe outro Feto na cena.** O jogador não tem alavanca nenhuma, e o efeito ainda é simétrico — ele te revela tanto quanto revela o outro. Não é magnitude alta demais; é magnitude que o dono da ficha não alcança. O **Sobrenome**, do lado oposto, dispara quando o jogador quer audiência: é ficção pura e é jogável.

**E relógio, aqui, só quando o mestre responde com verdade.** Destrancar ficção não precisa de contador — o Sobrenome é ilimitado de propósito, e *conseguir audiência não é o mesmo que ser bem recebido*. Mas *"pergunte uma coisa e o mestre responde com verdade"* arranca informação dura da mesa, e isso pede degrau da escada como qualquer outra coisa.

## 6. O Legado Próprio sai de graça

A régua serve de métrica para o Legado escrito pelo jogador **sem máquina nova**:

> **Declare qual dos três formatos ele é, e obedeça à trava daquele formato.**

O molde é o da Aptidão Própria — catálogo de exemplos, métrica para criar, aprovação do mestre.

**E a trava mais apertada de lá precisa ser escrita à mão, agora que a ficha leva dois.** A Aptidão Própria diz *"só pode ser pega uma vez na ficha inteira"*, e enquanto o Legado era um só isso vinha de graça. Com dois, não vem:

> **Um Legado Próprio por ficha. O outro sai do catálogo.**

Sem essa linha, a ficha inteira poderia ser escrita pelo jogador, e o catálogo — que é onde a régua está aplicada e conferida — viraria opcional.

## 7. O que a régua acha nos catorze de hoje

Rodada contra o catálogo existente, ela acende três coisas. **Nenhuma delas é dominância** — a seção 2 já mostrou que aquele teste passa.

**a) Três dos catorze usam relógio que a escada da peça 10 não tem.** Aprendi Apanhando e A Voz de Dentro dizem *"uma vez por sessão"*; O Que Ninguém Lembra diz *"uma vez por arco"*. A expressão *"por sessão"* aparece **zero vezes no manual**.

E aparece **uma vez em outra peça — para ser recusada.** A peça 12, tratando da conversão de mestragem: *"um bônus por marca, **não por sessão**. (…) ela não pode virar pagamento por mesa disfarçado."* **O projeto já tinha rejeitado esse relógio, pelo mesmo motivo, em outro lugar** — e ninguém voltou para olhar o catálogo de Legados.

Sessão e arco são **tempo de mesa**, não tempo de ficção. Num mundo de cinco a sete mestres com personagem persistente, cada um resolve de um jeito:

| como o mestre lê | rolagens no período | ganho médio |
|---|---|---|
| uma sessão = três num arco de missão | 17,1 | +1,47 pp |
| uma sessão = meia missão | 25,4 | +0,98 pp |
| uma sessão = uma missão inteira | 50,9 | +0,49 pp |

**Spread de 3,0× entre a leitura mais generosa e a mais dura**, na mesma ficha, no mesmo Legado. É o filtro do projeto — *dois mestres que nunca conversaram chegam ao mesmo número?* — falhando, com número em cima. A peça 10 já tinha escolhido gatilho de ficção pelo mesmo motivo: *"dá para descansar uma hora aqui?" é exatamente o tipo de pergunta que cada um responde diferente.*

**b) Metade do catálogo não tem relógio nenhum, e isso sozinho não é defeito.** Sete dos catorze estão sempre ligados — e Irmãos também está, e vale zero. Estar sempre ligado não diz nada sobre tamanho.

**O que diz é o cruzamento com o dano**, e ele acende exatamente uma vez: **Não Sou Gente**, pela tabela da seção 5. Os outros três Desliga apagam coisa que não é dano e passam inteiros. *Vale registrar que a conta que eu tinha feito antes — "a contagem de negações vai de 1 a 4" — media a coisa errada:* fatiar Não Sou Gente em quatro Legados de uma negação cada não conserta nada, porque cada fatia continua sendo imunidade a dano.

**c) Um Legado o jogador não consegue disparar** — Irmãos, pela seção 5.

## 8. Como se escolhe, e por que são dois

*Decidido depois da primeira leva de listas, e é a única coisa desta peça que muda a ficha.*

> **Toda ficha leva dois Legados: um Destranca, obrigatório, e mais um de qualquer lista.**

### O problema que isso resolve

**Quando uma opção de ficção disputa a mesma vaga que uma opção mecânica, a mecânica ganha.** Não é opinião — é o desfecho mais documentado deste tipo de lista. Os Traços, Ideais, Vínculos e Falhas do D&D 5e ficavam em branco cerca de 90% das vezes, e a edição de 2024 removeu os quatro.

Com **um** Legado e três formatos na mesma lista, o Destranca era a linha que ninguém escolhia — e as vinte entradas já escritas mostram isso de outro jeito: quem monta ficha para jogar pega o número.

### Por que "um Destranca" e não "dois de listas diferentes"

A versão óbvia da regra — *escolha dois, de listas diferentes* — **não conserta nada**, e piora o que não estava quebrado:

| | quem otimiza sai com | quem quer ficção sai com |
|---|---|---|
| um Legado, lista misturada *(como era)* | 1 mecânico | 1 de ficção, sentindo que abriu mão |
| **dois de listas diferentes** | **2 mecânicos, zero de ficção** | 1 + 1 |
| **um Destranca + um livre** | **1 mecânico** + 1 de ficção | 1 + 1 |

*Duas de listas diferentes* deixa pegar **Ajusta + Desliga**: o jogador que a regra existia para alcançar continua sem ficção nenhuma, e a economia mecânica **dobra**.

**Com o Destranca obrigatório, ela não dobra.** Quem otimiza sai com exatamente o que tinha antes — um Legado com número —, e todo mundo passa a carregar uma afirmação sobre o mundo. **Destranca é zero no dado por definição**, e é por isso que a trava cabe.

### Isto reabre uma decisão registrada, e o registro fica

A peça 9 diz, com todas as letras:

> *"Se em playtest o Legado parecer decoração, o conserto é dar mais opções por Origem, **não mais Legados por ficha**."*

E o motivo dela é bom: o Legado é a **terceira economia de poder** do sistema, e nasceu com o teto mínimo porque o `arquitetura.md` chama a segunda de *"o risco maior da estrutura inteira"*.

**O teto de poder continua em um.** O segundo Legado não tem número, não rola, não desliga nada — ele é a linha da ficha que diz quem é aquela pessoa. Mas a decisão está sendo reaberta, e quem ler a peça 9 vai encontrar o contrário escrito: **a mudança precisa chegar na peça 9, na peça 8, no gerador da ficha e nos dois validadores que conferem a ficha contra as peças.** Enquanto esta metade for rascunho, a regra antiga é a que vale.

### O tamanho de cada lista

| formato | por Origem | por quê |
|---|---|---|
| **Destranca** | **4** | é o que todo mundo leva agora, então precisa ser a escolha mais larga — e é o mais barato de escrever bem, porque não carrega número |
| **Ajusta** | **4** | onde mora a variedade numérica, e é ela que carrega o peso mecânico da lista |
| **Desliga** | **2** | **cota, com vaga reservada quando o alvo ainda não existe** |

Dez por Origem, **setenta no total**.

#### O Desliga é cota de dois, e a vaga que falta fica declarada

*Esta linha mudou depois das quatro primeiras listas, e a mudança tem preço registrado.* A régua dizia **"até 2, teto e não cota"**, e o Receptáculo e o Descendente fecharam em um por causa dela. O Mizuki decidiu o contrário: **toda Origem termina com dois Desliga.**

**O problema é que o alvo não está disponível para isso**, e a conta é dura:

**Depois que a trava virou *"só apaga o que ninguém comprou"*, eu enumerei o que sobrou de alvo legal no sistema inteiro:**

| alvo nomeado, sem preço | onde ele mora |
|---|---|
| reconhecer uma técnica pelo catálogo | peça 1, uso de Inteligência |
| ambiente propício contra lugar ruim | peça 10, seção 2 |
| ser sentido por Sentir Energia | peça 7, a perícia |
| ser localizado ou rastreado | ficção, sem tabela |
| comer, dormir, respirar | ficção |
| ser enganado por barreira, véu e ferramenta | ficção |
| os degraus de exaustão | peça 10, seção 4 |

**São sete no sistema inteiro, e seis já estão usados.** Dois por Origem em sete Origens são **catorze** — faltam **oito**, e existe **um** alvo livre. Três por Origem exigiria vinte e um.

*E o motivo de serem poucos é bom, não ruim:* **um Desliga precisa de coisa nomeada existindo antes dele**, e neste sistema quase tudo que acontece com você ou foi comprado por alguém — e aí tem dono — ou é arbitrado na ficção, e aí não há o que desligar. **O suprimento é estreito porque o resto está bem amarrado.**

> **Então a cota de dois se cumpre em duas etapas: o Desliga que tem alvo se escreve; o que não tem vira vaga declarada.**

**A vaga não é promessa vaga, e essa é a diferença inteira.** Ela obedece a três regras:

1. **Ela nomeia a peça de onde o alvo deve sair** — equipamento, invocação, Trilhas, ou a peça de dano e condições. Vaga que não diz o que está esperando é cheque em branco, e daqui a seis versões vira "acho que a gente ia escrever alguma coisa aqui".
2. **Ela aparece na lista da Origem**, na mesma tabela dos outros, marcada. Não em nota de rodapé — foi assim que a Trilha passou sete versões escrita e não aplicada.
3. **O validador confere que ela está marcada**, e não que a lista está cheia. Uma lista de nove com uma vaga declarada passa; uma lista de nove calada falha.

**Por que reservar em vez de preencher.** A alternativa é inventar oito alvos agora, e a régua já mostrou como isso termina: os três Desliga de condição — *Desconfiado*, *Corpo Emprestado* e *Já Morri* — foram escritos **porque a coluna pedia**, e cada um apagava uma condição que alguém compra no manual. Nenhuma trava me impediu, e quem pegou foi o Mizuki lendo. **Entrada que existe para fechar contagem é exatamente o defeito que esta régua nasceu para achar** — e ela não pode ser a coisa que a própria cota obriga.

*As peças que ainda não existem vão criar coisa nomeada nova, e é de lá que sai o Desliga que faltar.*

### A regra 1 tem um modo de falha que só apareceu quando a primeira peça chegou

*Achado na v0.49, quando Equipamento fechou na v0.48 e **nenhuma das quatro vagas que a nomeavam abriu**.*

A regra 1 manda a vaga nomear a peça de onde o alvo deve sair. **Ela não manda conferir se a peça nomeada é mesmo a que vai produzir o alvo** — e as quatro erraram, cada uma por um motivo diferente:

| vaga | dizia esperar | espera de verdade | por que errou |
|---|---|---|---|
| **Descendente** | equipamento | **ferramenta amaldiçoada** | a peça 14 declinou ferramenta por decisão: ela é tópico próprio, com graus e forja |
| **Restrição Celestial** | equipamento | **ferramenta amaldiçoada** | mesma coisa — e é a Origem que mais depende dela |
| **Reencarnado** | equipamento | **objeto amaldiçoado** | o `Enterrado` foi a pista falsa: *"você guardou uma coisa"* não é uma arma |
| **Corpo Amaldiçoado** | equipamento | **Técnica Marcial** | dependência de segunda mão: Técnica Marcial *estava* bloqueada por equipamento, e a vaga nomeou o bloqueio em vez do dono |

> **A distinção que desfaz três dos quatro erros é de canon, e o projeto vinha usando um nome só para duas coisas.** *Achado do Mizuki:* **"acredito que são mais como itens amaldiçoados, não necessitando exatamente ser armas."**
>
> | | o que é | quem depende dela aqui |
> |---|---|---|
> | **ferramenta amaldiçoada** (呪具) | **arma forjada** para canalizar energia, com graus. Até quem não é feiticeiro usa | `Armaria` do Descendente · Restrição Celestial |
> | **objeto amaldiçoado** (呪物) | **não é item imbuído: é a própria maldição presa em forma de objeto.** Resto de feiticeiro antigo, que encarna num receptáculo compatível | Receptáculo · Reencarnado |
>
> **A diferença é de intenção:** a ferramenta é feita para canalizar; o objeto **é** a coisa. *A definição de cada uma mora no `ESTADO-ATUAL`, na lista do que não existe, e vem para a peça dona quando ela for escrita — esta tabela é o argumento que reclassificou as vagas, não a definição.* *E a peça 9 já escrevia a dependência certa sem que ninguém tivesse ligado os pontos: o Kashimo "aceitou virar **objeto amaldiçoado** e encarnar num corpo que o Kenjaku preparou".*

**E aí aparece o buraco que isto destampou: `objeto amaldiçoado` não tem peça dona em lugar nenhum do projeto.** Duas Origens inteiras são construídas em cima dele — Receptáculo é comer um dedo, Reencarnado é *ter virado* um — e ele não está na fila, não está no `arquitetura.md` e não tem vaga na ordem de construção. **Ele estava escondido dentro da palavra "ferramenta".**

> **O conserto da regra 1, para a próxima peça que chegar:** *a vaga nomeia a peça que é **dona do alvo**, não a peça que estava na frente dela na fila.* Uma dívida que nomeia a peça errada é pior que uma dívida sem nome — a sem nome ninguém dá por fechada, e a com nome errado **fecha sozinha no dia em que a peça errada fecha.**

*Cinco por formato foram considerados e recusados pela conta:* dariam 105 entradas, e 35 Desliga não existem nem com as peças que faltam.

**O Descendente é a exceção, e ela é de propósito.** Ele leva **onze**, porque é a única Origem que contém coisas diferentes por dentro: os quatro Destranca dele são **arquétipos de clã**, mais um genérico para quem inventou o próprio. A peça 9 proíbe qualquer Origem de mexer em técnica, então um Legado de clã só pode entregar nome, acesso, conhecimento e ferramenta — que é **exatamente** o que Destranca é. O formato e a ficção se encontram ali sem precisar de exceção nenhuma.

## 9. O catálogo, Origem por Origem

Cada entrada declara **formato**, **largura** e **relógio**. As colunas não são enfeite: é por elas que o validador confere.

> **Quatro das sete listas estão escritas.** A decisão de alvo — **4 Destranca · 4 Ajusta · 2 Desliga** — veio depois da primeira leva, então as listas cresceram para dentro dela em vez de nascer nela. **O total de entradas escritas varia**, porque o Desliga sem alvo fica como vaga declarada em vez de ser inventado. A tabela no fim da seção tem a conta.

### Latente — *ninguém te deu nada e ninguém te ensinou*

**Destranca — escolha um destes, obrigatoriamente**

| Legado | relógio |
|---|---|
| **O Jeito Errado** | por dia |
| **O Professor Que Você Não Teve** | sem relógio |
| **A Testemunha** | sem relógio |
| **Sem Patente** | sem relógio |

> **O Jeito Errado** — escreva na ficha **o que você aprendeu errado antes de aprender certo**. Uma vez por dia, aponte alguém que esteja fazendo a mesma coisa errada e o mestre diz o que aquilo custa a essa pessoa.
>
> **O Professor Que Você Não Teve** — existe um feiticeiro que **podia** ter te ensinado e não ensinou. Escreva quem é e por que não. Essa pessoa está viva, sabe que você existe, e a escolha dela ainda está de pé.
>
> **A Testemunha** — alguém sem energia amaldiçoada **sabe o que você é**, e nunca contou pra ninguém. Escreva quem é e o que essa pessoa viu. Ela continua na vida dela, e continua sabendo.
>
> **Sem Patente** — você nunca entrou na instituição, e ela sabe disso. Patente não te obriga a nada: ordem de superior é conselho, e a hierarquia te trata como o que você é — alguém que não deve nada e a quem não se deve nada.

**Ajusta**

| Legado | alcança | relógio |
|---|---|---|
| **Aprendi Apanhando** | qualquer perícia (23) | por dia |
| **Instinto Bruto** | Intuição (1) | por cena |
| **Gambiarra** | qualquer ofício (10) | por dia |
| **Desconfiado** | uma condição nomeada (1) | por cena |

> **Aprendi Apanhando** — uma vez por dia, refaça um teste de perícia que você falhou. Você já errou isso antes.
>
> **Instinto Bruto** — uma vez por cena, role Sentir Energia no lugar de Intuição, se disser como o seu jeito de sentir resolve aquilo.
>
> **Gambiarra** — uma vez por dia, use um ofício que você não tem treinado como se tivesse. Você já resolveu isso com o que estava na mão.
>
> **Desconfiado** — uma vez por cena, role com **vantagem** o Teste de Resistência contra ficar **Enfeitiçado**. Ninguém nunca te deu nada de graça, e você aprendeu cedo que quem se aproxima quer alguma coisa.

**Desliga**

| Legado | apaga | relógio |
|---|---|---|
| **Inédito** | ser reconhecido pelo catálogo | sempre |
| **Chão Duro** | a diferença entre lugar propício e lugar ruim | sempre |

> **Inédito** — a sua técnica não está em registro nenhum: ninguém a reconhece pelo catálogo, e preparar-se contra ela exige ter te visto fazer. *Em troca, ninguém sabe te ajudar com ela pelo mesmo motivo — não existe quem tenha estudado o que você faz.*
>
> **Chão Duro** — para você, **qualquer lugar é ambiente propício**. Você aprendeu a dormir no chão, comer o que tinha e acordar inteiro. *Em troca, você não percebe quando os outros não estão aguentando — para você aquilo é terça-feira.*

*O **Desconfiado** nasceu nesta lista como Desliga e mudou de formato antes de a lista fechar — ele está entre os Ajusta acima. O motivo está na seção 5.*

**Os dois que já existiam mudaram, e os dois por ordem da régua.** *Aprendi Apanhando* dizia *"uma vez por sessão"* — relógio que não está na escada da peça 10 — e o gatilho dele é a categoria inteira das perícias, então desce para **por dia**. *Instinto Bruto* dizia *"Percepção ou Intuição"*, e contra Percepção ele estava **metade morto**: Sentir Energia e Percepção são as duas de Essência desde a v0.16, e trocar Essência por Essência não é troca. Sobrou Intuição, que é Inteligência — e aí é troca de verdade, de até +4 para quem conjura.

**A régua reprovou uma proposta minha antes de ela virar texto.** *Gambiarra* nasceu como *"uma vez por cena"*, porque é a que mais parece pequena da lista. Ela alcança **os onze ofícios**, que é categoria inteira, e a largura manda ir para por dia. Estreitar o gatilho para um ofício escolhido na criação também fecharia a conta — e mataria o sabor, porque improviso que você escolhe com antecedência não é improviso. **O relógio cedeu, o gatilho ficou.**

**Inédito é o Desliga da lista, e ele apaga exatamente uma coisa nomeada:** *"reconhecer uma técnica pelo catálogo"*, que a peça 1 atribui à Inteligência. Não é dano, não é resistência, não é imunidade — e a troca está escrita no próprio texto, como a trava do formato exige.

**O Jeito Errado passa nas duas cláusulas do Destranca.** O jogador puxa o gatilho, e a reivindicação sobre o mundo é a linha que ele escreve na ficha: *existe um jeito errado de aprender isso, e eu sei qual é porque foi o meu*. Nenhum outro personagem tem aquela linha. O relógio existe porque o mestre responde com verdade.

#### Dois Destranca saíram dos traços da própria Origem

A peça 9 dá ao Latente três traços: *o professor que você não teve* · *a primeira vez em que quase morreu* · *alguém comum que sabe o que você é*. **Dois deles viraram Legado sem precisar de nada novo** — eles já eram afirmação sobre o mundo, feita pelo jogador, com zero no dado. Era a definição de Destranca escrita antes de o formato existir.

*Isso encosta num alerta que fica registrado:* os traços da peça 9 são a mesma estrutura que o D&D 2024 removeu — Traços, Ideais e Vínculos, deixados em branco cerca de 90% das vezes. **Enquanto forem lista de sugestão, ninguém escolhe; virando Destranca, passam a ser escritos e usados.** Não foram todos, e não deve ser sempre — mas é a fonte mais barata de Destranca que este catálogo tem, e ela já está escrita em sete Origens.

#### O que a régua fez com as três direções de Desliga

Foram levantadas três e havia duas vagas. **A régua repartiu sozinha, e nenhuma precisou ser cortada:**

| direção | tem coisa nomeada para apagar? | onde foi parar |
|---|---|---|
| a condição **Enfeitiçado** não pega | sim — está na lista de condições do manual | **Desliga** |
| fome, frio e privação não te param | **não.** A peça 7 registra que *"aguentar dor e fome é leitura de Constituição em qualquer mesa"* — não existe regra | **Desliga**, depois de pendurar no **ambiente propício**, que é coisa nomeada da peça 10 |
| hierarquia não te alcança | **não.** A peça 9 diz que *"a patente é eixo social e narrativo"*, e nada obriga ninguém mecanicamente | **Destranca** — não havia o que desligar |

**A terceira é a que ensina.** *"Hierarquia não te alcança"* parece Desliga e não é: um Desliga precisa de alguma coisa nomeada para apagar, e quando não existe regra por baixo, o que sobra é uma afirmação sobre o mundo — que é Destranca. **A régua não recusou a ideia; ela disse em que prateleira ela mora.**

*E o Chão Duro é o exemplo do caminho contrário:* a ideia não tinha gancho, e ganhou um. Sem o ambiente propício ele seria ficção fingindo ser mecânica.

**Dominância dentro da lista: nenhuma.** As dez compram coisas diferentes, e os quatro Destranca não se cobrem — um é sobre o seu erro, um sobre quem não te ensinou, um sobre quem sabe de você, e um sobre onde você não está. **Quatro Destranca · quatro Ajusta · dois Desliga**, dez no total.

### Receptáculo — *você carrega alguma coisa, e ela ainda está aí*

**Destranca — escolha um destes, obrigatoriamente**

| Legado | relógio |
|---|---|
| **A Voz de Dentro** | por dia |
| **De Antes de Você** | sem relógio |
| **Alcunha** | sem relógio |
| **O Que Ele Quer** | por descanso longo |

> **A Voz de Dentro** — uma vez por dia, pergunte ao mestre uma coisa sobre uma maldição ou técnica presente na cena. Ele responde com verdade. O que está em você já viu aquilo.
>
> **De Antes de Você** — escolha **uma pessoa, um lugar ou um clã que conheceu o que te habita quando ele ainda andava sozinho**. Eles existem, e sabem o que você carrega. O que fazem com isso é outra conversa.
>
> **Alcunha** — escreva **como ele era chamado** quando andava sozinho. Quem é do meio e ouve esse nome sabe o que é, e reage antes de pensar. Você pode dizer o nome em voz alta quando quiser — e não tem como despronunciar.
>
> **O Que Ele Quer** — escreva na ficha **o que ele quer, e não é o que você quer**. Uma vez por descanso longo você pode **ceder**: entregue a ele uma coisa que ele queria, e ele te dá passagem para o que você precisava. O mestre narra os dois lados, e **o que você cedeu fica escrito na ficha e não sai de lá**.

**Ajusta**

| Legado | alcança | relógio |
|---|---|---|
| **Não Sou Só Eu** | TR Espírito, três situações (3) | por cena |
| **Costume Antigo** | uma perícia (1) | por cena |
| **Tranco** | TR Físico (1) | por cena |
| **Passagem** | qualquer rolagem | por dia |

> **Não Sou Só Eu** — uma vez por cena, refaça um Teste de Resistência de Espírito que você falhou contra ser controlado, dominado ou lido.
>
> **Costume Antigo** — escolha uma perícia na criação: o que está em você já sabia fazer aquilo. Uma vez por cena, role ela como se fosse treinada. Você lembra da sensação, não de ter aprendido.
>
> **Tranco** — uma vez por cena, refaça um Teste de Resistência **Físico** que você falhou. Ele não quer morrer neste corpo mais do que você.
>
> **Passagem** — uma vez por dia, você deixa ele assumir: refaça **qualquer rolagem**. Quando você volta, o mestre diz uma coisa que ele fez enquanto estava no comando, e você não estava lá para impedir.

**Desliga**

| Legado | apaga | relógio |
|---|---|---|
| **Máscara** | ser sentido pelo que você é | sempre |
| **Revezamento** | ficar `Impedido` | por descanso longo |

> **Revezamento** — prender você prende um dos dois: uma vez por descanso longo, você **não fica `Impedido`** — ele empurra, e o seu corpo vai junto porque não é só seu. *Em troca, quem estava olhando viu: naquele momento não era você que se mexia. O mestre diz o que as pessoas presentes passaram a achar de você, e elas agem de acordo.*


> **Máscara** — quem sente a sua energia amaldiçoada sente **a dele**. Você não aparece como o que é. *Em troca, o que essas pessoas concluem sobre você costuma ser bem pior do que a verdade — e elas agem de acordo.*

**A Voz de Dentro desceu de relógio, e não por gosto.** Ela dizia *"uma vez por sessão"* — que não é degrau da escada da peça 10 e vale três coisas diferentes conforme o mestre. Ela é Destranca em que **o mestre responde com verdade**, então a trava do formato pede relógio, e **por dia** é o degrau que a escada tem. *Não Sou Só Eu* já passava: um Teste de Resistência nomeado contra três situações escritas é alcance 3, e alcance até 3 pode ficar por cena.

**De Antes de Você é o Destranca que não leva relógio, e o contraste com a Voz de Dentro é a trava do formato inteira.** Na Voz de Dentro **o mestre responde**; aqui **o jogador declara**, e aquilo passa a ser verdade no mundo. É a segunda cláusula funcionando: a afirmação é sobre o mundo, ela é daquele personagem e de mais ninguém, e não tem o que racionar porque nada é arrancado da mesa.

**Máscara apaga uma coisa nomeada e não é dano:** o que a percepção de energia amaldiçoada encontra em você. Não reduz golpe, não dá resistência, não fura imunidade. E a troca está no próprio texto, como a trava exige — e ela é boa ficção em vez de castigo, porque quem te lê errado te trata como coisa pior.

**O par que quase colide, e fica anotado:** *Não Sou Só Eu* cobre *ser lido*, e *Máscara* também encosta em leitura. São conjuntos diferentes — uma rerrola um Teste de Resistência contra leitura de mente, a outra redireciona percepção de energia e não rola nada. **Nenhuma contém a outra pelo teste da peça 3**, mas se alguma das duas for reescrita, este é o par a reconferir.

#### O Que Ele Quer nasceu falhando o filtro multi-mestre, e o conserto foi mover o gatilho

A ideia era *"quando o que ele quer coincide com o que a cena precisa, ele coopera"* — e **quem decide a coincidência?** Dois mestres respondem diferente, e o filtro do projeto existe exatamente para isso.

**O conserto não mexeu no efeito: mexeu em quem puxa.** Agora **o jogador declara que está cedendo**, e o mestre só narra o que aquilo custou. A coincidência deixou de ser julgamento e virou decisão de quem tem a ficha — que é o mesmo formato da primeira cláusula do Destranca.

**E o preço fica escrito.** *"O que você cedeu não sai da ficha"* é a única coisa deste catálogo que se acumula entre missões, e é de propósito: o Receptáculo é a Origem em que a coisa dentro de você continua lá, e uma dívida que zera no descanso longo não diria isso.

#### Passagem é o gatilho mais largo do catálogo, e o relógio é o que segura

*"Refaça qualquer rolagem"* alcança mais que qualquer outro Ajusta escrito até aqui — o *Aprendi Apanhando* pega as 23 perícias, e este pega tudo, inclusive ataque e Teste de Resistência. **Pela trava, categoria inteira desce para por dia**, e é o relógio que faz a conta fechar: **+25 pp no pico, diluídos em 25,4 rolagens, dão +0,98 pp médios** — o mesmo do *Aprendi Apanhando*.

**A diferença não está na média, está em onde você gasta.** Uma rerrolagem que serve para tudo é guardada para a rolagem que decide a missão, e isso vale mais do que a média diz. **É o candidato número um a apertar se o playtest mostrar que ele resolve cena demais** — e o aperto óbvio já existe pronto: tirar ataque de fora do alcance.

#### Alcunha e De Antes de Você não são o mesmo Legado

Um nomeia **quem conheceu** a coisa; o outro nomeia **como a coisa se chamava**. O primeiro coloca uma pessoa no mundo, o segundo coloca uma palavra — e a palavra funciona mesmo onde ninguém daquela lista está presente. Nenhum conjunto contém o outro.

**Dominância na lista: nenhuma. Quatro Destranca · quatro Ajusta · dois Desliga escritos.**

*A vaga esperava a **peça de dano e condições**, que é onde o que acontece com a sua cabeça vai ganhar nome.* **Ela fechou na v0.104, e o alvo é o `Impedido`.** *A nota da vaga pedia "o que acontece com a sua cabeça", e a condição de cabeça que sobrava era o `Atordoado` — ele custa `Pesada` e apagá-lo uma vez por descanso longo seria a maior coisa do catálogo inteiro.* **O `Impedido` diz a mesma ficção pelo corpo:** prendem você, e a coisa dentro empurra. *O Receptáculo é a Origem em que outra coisa quer o seu corpo, e é ela que sai andando.*

### Descendente — *você é de uma das famílias, e elas cobram*

**Destranca — escolha um destes, obrigatoriamente.** *Os quatro primeiros são arquétipos de clã; o quinto é para quem inventou o próprio.*

| Legado | o clã que ele desenha | relógio |
|---|---|---|
| **O Sobrenome** | o clã do **nome** — *Gojo* | sem relógio |
| **Armaria** | o clã da **ferramenta** — *Zen'in* | sem relógio |
| **Arquivo** | o clã do **corpo** — *Kamo* | sem relógio |
| **Palavra Dada** | o clã da **voz** — *Inumaki* | sem relógio |
| **Treino de Berço** | qualquer clã, inclusive o seu | sem relógio |

> **O Sobrenome** — em qualquer lugar da sociedade jujutsu você consegue audiência com quem importa. Conseguir audiência não é o mesmo que ser bem recebido.
>
> **Armaria** — a sua família guarda ferramenta amaldiçoada, e você sabe onde. **Escreva qual peça é sua por direito e quem está com ela agora.** Ela existe, ela é sua, e ninguém devolveu.
>
> **Arquivo** — a sua família fez coisas com corpo que nunca foram publicadas. **Escreva uma delas.** Você cresceu sabendo, ninguém de fora sabe, e alguém lá dentro ainda acha que valeu a pena.
>
> **Palavra Dada** — na sua família não se desperdiça palavra, e o meio inteiro sabe disso. **Quando você promete alguma coisa, quem é do meio trata como vínculo** — e cobra, com o peso do seu sobrenome atrás.
>
> **Treino de Berço** — o seu clã ensina **uma coisa que não se aprende fora dele**. Escreva na ficha o que é. Quem quiser aquilo tem que passar pela sua família — ou por você.

**Ajusta**

| Legado | alcança | relógio |
|---|---|---|
| **Conversa de Jantar** | técnica de clã (1) | por cena |
| **Etiqueta** | uma situação nomeada (1) | por cena |
| **Repetição** | um TR nomeado (1) | por cena |
| **Biblioteca** | duas perícias (2) | por cena |

> **Conversa de Jantar** — uma vez por cena, contra uma **técnica de clã**, você sabe o que vem: vantagem no Teste de Resistência contra ela. Você cresceu ouvindo falar dessas técnicas à mesa, com nome e com defeito.
>
> **Etiqueta** — uma vez por cena, refaça um teste social que você falhou **diante de alguém de patente ou clã superior ao seu**. Você foi treinado para essa sala desde criança.
>
> **Repetição** — escolha **um Teste de Resistência na criação**: é contra aquilo que a sua família te drilou, todo dia, por anos. Uma vez por cena, role ele com vantagem.
>
> **Biblioteca** — uma vez por cena, refaça um teste de **História ou Ocultismo** que você falhou. A sua casa tinha os livros, e você foi obrigado a ler.

**Desliga**

| Legado | apaga | relógio |
|---|---|---|
| **Coleira** | ser localizado ou rastreado | sempre |
| **Cabo** | ficar `Desarmado` | por cena |

> **Cabo** — a sua mão conhece o cabo antes de a cabeça mandar: uma vez por cena, você **não fica `Desarmado`** — a ferramenta escorrega e volta. *Em troca, você não larga ela quando devia: quem revista acha, quem te vê armado te trata como armado, e você não atravessa lugar nenhum como civil.*


> **Coleira** — o seu clã te selou na infância: técnica nenhuma te localiza, te rastreia ou te encontra à distância. *Em troca, o selo é dos dois lados — a sua família sempre sabe onde você está, e nunca precisou perguntar.*
>
*A vaga espera **ferramenta amaldiçoada**, e é a mesma dependência que a **Armaria** já carrega: o Descendente é a Origem que guarda ferramenta — a `Armaria` diz literalmente *"o clã da ferramenta"* — e ferramenta amaldiçoada ainda não tem propriedade nomeada para desligar.*

> **Esta linha dizia "espera a peça de equipamento", e estava errada.** *Corrigido na v0.49, depois que Equipamento fechou e a vaga não abriu.* A peça 14 declinou ferramenta amaldiçoada por decisão — ela é **tópico próprio, com graus e forja** —, então esta vaga nunca esteve esperando aquela peça. **Uma dívida que nomeia a peça errada não é dívida marcada: é dívida escondida atrás de um nome plausível.**

**Treino de Berço mudou de formato, e a proibição do Ajusta permanente foi o motivo.** Ele era *"treine mais uma perícia"* — Ajusta sem relógio, que a régua acabou de proibir. A versão com relógio ficaria *"uma vez por cena, role tal perícia como se fosse treinada"*, que é **exatamente o Costume Antigo do Receptáculo, palavra por palavra**. Duas das cinco primeiras entradas escritas seriam a mesma mecânica com duas ficções.

Virando Destranca, ele fica melhor do que era: *"o meu clã ensina uma coisa que não se aprende fora dele"* é reivindicação sobre o mundo, é daquele personagem e de mais ninguém, e é mais Descendente que um bônus de perícia — porque a Origem inteira é sobre **o que a família tem e cobra**.

**Coleira é o Desliga da lista, e o nome carrega a troca.** Ela apaga uma coisa nomeada — ser localizado por técnica — e não encosta em dano. A troca está escrita e é a Origem inteira em uma linha: o selo que te esconde do mundo é o mesmo que entrega você para a sua família.

#### A lista foi reequilibrada, e o motivo vale registrar

**A primeira versão desta lista tinha três Destranca de cinco e um Ajusta só** — a Origem menos numérica do catálogo. Ela ficou assim por acidente de sequência, e não por decisão: *Treino de Berço* **virou** Destranca para fugir da colisão com o *Costume Antigo*, e a lista pendeu junto.

**Conversa de Jantar era o terceiro Destranca, e trocar ele de formato consertou duas coisas de uma vez.** A ficção não mudou uma vírgula — você cresceu ouvindo falar das técnicas de clã à mesa. O que mudou é que aquilo agora sai em número, e não em pergunta ao mestre.

E consertou também **o par repetido**, que era o segundo defeito: o Receptáculo tinha *A Voz de Dentro* (o mestre responde, com relógio) mais *De Antes de Você* (o jogador declara, sem relógio), e o Descendente estava montando a mesma configuração com *Conversa de Jantar* e *Treino de Berço*. **Não seria duplicata de mecânica** — o conteúdo é completamente diferente e nenhuma contém a outra —, mas é a mesma estrutura em duas Origens seguidas, e catálogo previsível não aparece em teste nenhum. *Continua marcado para as listas que faltam.*

#### Os quatro arquétipos, e por que nenhum deles cita a técnica

**A peça 9 proíbe qualquer Origem de abrir Família, fechar Família, dar Melhoria ou mudar Classe.** Então um Legado de clã **não pode** dar Limitless, Fala Amaldiçoada, Manipulação de Sangue nem Dez Sombras — e essa proibição, que parecia um obstáculo, é o que fez os quatro saírem bons.

O que sobra de um clã quando a técnica sai da conta é **o que a família tem, guarda, esconde e cobra** — nome, arsenal, arquivo e reputação. Quatro coisas diferentes, quatro Legados, e nenhum deles é *"você é forte porque é Gojo"*.

**E os canônicos são exemplo, não requisito.** Cada arquétipo diz *que tipo de clã é aquele*, e o jogador que inventou uma família escolhe o que combina — o texto é o mesmo. Um Zen'in pega **Armaria**; alguém que inventou uma casa de caçadores de ferramenta pega **Armaria** também, com a mesma frase. **Isso era o defeito que eu tinha levantado contra clãs nomeados** — *"Legado que só um Zen'in usa é opção morta pra todo mundo que não é"* — e ele desaparece quando o nome do clã vira exemplo entre parênteses.

*Um aviso de dependência:* **Armaria cita ferramenta amaldiçoada, e a peça de equipamento não existe.** Como Destranca é zero no dado, ela funciona hoje como ficção e acesso — mas quando a peça 2 da fila for escrita, esta entrada é a primeira a reler.

#### Repetição e Conversa de Jantar quase se cobrem, e não se cobrem

As duas dão **vantagem em Teste de Resistência**, e é o mesmo número. A diferença é o gatilho: uma dispara **contra técnica de clã**, seja qual for o TR; a outra dispara **num TR escolhido**, seja qual for a ameaça. **Os conjuntos se cruzam e nenhum contém o outro** — quem pega Repetição e escolhe Espírito não está protegido contra a técnica de clã que vai pelo Físico, e quem pega Conversa de Jantar não tem nada contra o veneno de uma maldição comum.

*Fica anotado como par a reconferir se alguma das duas for reescrita*, junto com o par *Máscara × Não Sou Só Eu* do Receptáculo.

**Dominância na lista: nenhuma. Cinco Destranca · quatro Ajusta · dois Desliga escritos**, onze escritos.

*A Origem que contém quatro famílias diferentes ia levar onze, e leva dez.* O quinto Destranca entrou como estava previsto — é o genérico, para clã inventado. O segundo Desliga **não tinha alvo**: nenhum sobrou depois da Coleira. Pela régua antiga a lista fechava aí; pela cota de dois ela fecha com a vaga marcada, esperando equipamento.

### Reencarnado — *você já foi outra pessoa, e o corpo em que você está não nasceu seu*

**Destranca — escolha um destes, obrigatoriamente**

| Legado | relógio |
|---|---|
| **O Que Ninguém Lembra** | por descanso longo |
| **Encomenda** | sem relógio |
| **Quem Morava Aqui** | sem relógio |
| **Enterrado** | sem relógio |

> **O Que Ninguém Lembra** — uma vez por descanso longo, você sabe um lugar, um nome ou uma técnica de antes do seu tempo, e isso responde uma dúvida que ninguém vivo responderia.
>
> **Encomenda** — **alguém pagou para você voltar.** Escreva quem foi e qual era a condição. Essa pessoa está viva, considera o acordo aberto, e o que ela acha que comprou não é necessariamente o que você acha que vendeu.
>
> **Quem Morava Aqui** — **este corpo teve uma vida.** Escreva de quem ele era e **uma pessoa que ainda está esperando essa pessoa voltar**. Ela não sabe. Ela continua esperando, e continua procurando.
>
> **Enterrado** — você guardou uma coisa antes de morrer, e nunca voltou para buscar. Escreva o que é e onde. **Continua lá**, se o lugar ainda existir — e faz tempo demais para alguém ter tido motivo de mexer.

**Ajusta**

| Legado | alcança | relógio |
|---|---|---|
| **Corpo Emprestado** | uma condição nomeada (1) | por cena |
| **Espasmo** | dois TR nomeados (2) | por cena |
| **Já Morri** | uma condição nomeada (1) | por cena |
| **Método Velho** | uma situação nomeada (1) | por cena |

>
> **Corpo Emprestado** — dor não te para como para os outros: uma vez por cena, role com **vantagem** o Teste de Resistência contra ficar **Incapacitado**. O corpo avisa os outros e não avisa você.
>
> **Espasmo** — uma vez por cena, refaça um Teste de Resistência **Físico ou de Vigor** que você falhou. O corpo fez uma coisa que você não mandou, e quem estava aqui antes ainda está nos músculos.
>
> **Já Morri** — uma vez por cena, role com **vantagem** o Teste de Resistência contra ficar **Amedrontado**. Você já esteve do outro lado e não achou grande coisa — e não mede risco como quem tem uma vida só.
>
> **Método Velho** — uma vez por cena, um teste que envolva **método antigo** — ritual, selo, barreira velha, escrita morta — sai como se você fosse treinado. Era assim que se fazia no seu tempo.

**O relógio do Que Ninguém Lembra desceu para o degrau mais raro da escada.** Ele dizia *"uma vez por arco"*, e arco é tempo de mesa — não está entre os quatro degraus da peça 10, e cada mestre mede um arco de um jeito. *Por descanso longo* é o degrau mais lento que existe, que é o que "por arco" tentava dizer.

**Corpo Emprestado parou de ser ambíguo, e o conserto veio de fora.** Ele dizia *"você nunca fica incapacitado só por estar ferido"* — e `Incapacitado` é **condição nomeada do manual**, na lista que um feitiço aplica. A qualificação *"só por estar ferido"* fazia dois mestres lerem duas coisas, porque **o sistema não tinha regra escrita para o que acontece quando a vida acaba**. Agora tem: a seção 5.5 da peça 1 diz que **`Inconsciente` não é a condição `Incapacitado`**, e as duas leituras deixaram de existir.

#### Esta lista perdeu os dois Desliga dela, e o motivo é a regra nova

**Os dois nasceram apagando condição** — *Corpo Emprestado* levava Incapacitado e *Já Morri* levava Amedrontado, as duas **Condição Maior** no manual da época. Quando a trava do Desliga passou a dizer *"só apaga o que ninguém comprou"*, os dois caíram junto com o *Desconfiado* do Latente.

**Os três viraram vantagem no Teste de Resistência**, e o efeito na mesa quase não muda: vantagem vale os mesmos +25 pp no pico que a negação valia em certeza. O que muda é que **entrou um dado no meio** — e quem pagou Pesada para aplicar a condição volta a ter chance.

*Registrado porque é achado de método, não de conteúdo:* eu escrevi **três** Desliga de condição em duas Origens sem nada me impedir, e a trava da época — *"não encosta no dano"* — passou nos três. **Foi o Mizuki que pegou, lendo o Desconfiado.** A régua só ficou capaz de pegar sozinha depois disso.

#### Os três Destranca novos, e o que cada um evita

**Os três saem dos traços da peça 9** — *o motivo pelo qual você aceitou voltar* · *alguém que te reconheceu de antes* · *a família do corpo que você está usando* —, que é a mesma fonte barata que o Latente usou. Mas **um dos três traços foi recusado, e a recusa é o achado**.

*"Alguém que te reconheceu de antes"* vira o Legado óbvio: uma pessoa viva sabe quem você era. **Ele não foi escrito**, porque o catálogo já tem duas entradas com essa forma exata:

| Origem | Legado | forma |
|---|---|---|
| Latente | **A Testemunha** | alguém sabe o que você é, e nunca contou |
| Receptáculo | **De Antes de Você** | alguém conheceu o que te habita quando ele andava sozinho |
| ~~Reencarnado~~ | ~~alguém te reconheceu de antes~~ | **a terceira em quatro Origens** |

*Este é o alerta que a lista do Descendente deixou marcado — "é a mesma estrutura em duas Origens seguidas, e catálogo previsível não aparece em teste nenhum" — acendendo pela primeira vez numa lista nova.* Não é duplicata de mecânica: as três são zero no dado e o conteúdo é diferente. É **previsibilidade**, e ela não aparece em validador nenhum.

**O conserto foi inverter.** *Quem Morava Aqui* usa a mesma matéria — uma pessoa, uma ligação com quem você foi — e vira do avesso: **ela não sabe, e é justamente por isso que ela está procurando.** As outras duas põem no mundo alguém que guarda um segredo seu; esta põe alguém que carrega um erro seu, e que você pode escolher desfazer ou não.

**Encomenda é o Kashimo**, que é o exemplo da própria peça 9: um acordo que alguém pagou, com condição escrita. A cláusula final — *o que ela acha que comprou não é o que você acha que vendeu* — existe para o Legado ter **duas alavancas**: o jogador pode ir cobrar, e o jogador pode declarar que o acordo foi lido errado. Sem ela vira dívida que só o mestre movimenta, que é o defeito do **Irmãos**.

**Enterrado é acesso puro**, no molde do *Sobrenome*: zero no dado, e o jogador puxa quando quer buscar. *E ele tem a mesma dependência que a **Armaria** do Descendente:* se o que está enterrado for ferramenta amaldiçoada, **a peça de equipamento decide o que isso vale** — hoje funciona como ficção e acesso, e esta entrada é das primeiras a reler quando a peça 2 da fila sair.

#### As duas vagas de Desliga, e por que só uma fechou

**Desliga**

| Legado | apaga | relógio |
|---|---|---|
| *— vaga reservada —* | **espera a peça de objeto amaldiçoado** | — |
| **Usado** | ficar `Derrubado` | por cena |

> **Usado** — este corpo já esteve em estado muito pior que este, e levantou: uma vez por cena, você **não fica `Derrubado`**. *Em troca, ele cobra depois — o mestre diz uma coisa pequena que o seu corpo passa a fazer errado até o fim da cena, e ela é sua e não dele.*


Sobrou **um** alvo legal no sistema inteiro pela enumeração da seção 8 — **os degraus de exaustão**, da peça 10 — e ele **não foi gasto aqui**. Dois motivos, e o segundo é o que decide:

- **Ele encosta no Chão Duro.** O Legado do Latente já faz *"qualquer lugar é ambiente propício"*, que é a outra ponta do mesmo relógio de desgaste. As duas juntas precisam ser medidas antes de qualquer uma virar texto.
- **Ele é mais Corpo Amaldiçoado que Reencarnado.** *"O corpo não cansa como o de gente"* é a Origem que literalmente não é gente. Reencarnado tem corpo humano — emprestado, mas humano.

> **Com a cota de dois, o alvo livre deixou de ser prêmio de quem chegou primeiro e virou decisão de encaixe.** Ele fica **reservado para o Corpo Amaldiçoado**, que é a lista seguinte — e a decisão custa alguma coisa lá, porque é a Origem que tem direito a ele pela ficção.

**As duas vagas do Reencarnado esperam peças diferentes, de propósito.** Uma é **objeto amaldiçoado**, e a peça 9 escreve a dependência sem rodeio: o Kashimo *"aceitou virar **objeto amaldiçoado** e encarnar num corpo que o Kenjaku preparou"*. **A Origem inteira é a mecânica de objeto amaldiçoado vista de dentro.** A outra é a peça de dano e condições: o corpo emprestado é a ficção que mais pede efeito nomeado, e três Ajusta desta lista já disputam esse território.

> **Esta vaga dizia "espera a peça de equipamento", e o *Enterrado* foi a pista falsa.** *Corrigido na v0.49.* Aquele Destranca diz *"você guardou uma coisa antes de morrer"* — e **a coisa não é necessariamente uma arma**, então ele nunca dependeu de equipamento. O que ele pede é objeto com regra, e objeto amaldiçoado **não tem peça dona em lugar nenhum do projeto**.

**A lista fecha em nove escritos: quatro Destranca · quatro Ajusta · um Desliga escrito e um reservado.** Dominância dentro da lista: nenhuma — os quatro Destranca compram um segredo de antes, um credor, uma pessoa enganada e um objeto parado, e nenhum contém outro.

### Corpo Amaldiçoado — *você não é uma pessoa; é uma coisa que alguém fez e que acordou*

> **A Origem mudou de natureza antes de a lista ser escrita, e isso é o que faz ela caber.** Até a v0.38 ela dividia balde com a Maki: *"não têm energia amaldiçoada, então não têm aptidão nem refino"*. **Cadáver de mutação abrupta produz a própria energia** — é o que a mutação concede, uns três meses depois de ele acordar. O que falta é **técnica**, não energia. Então ele é **misto: PE, aptidões e refino como qualquer feiticeiro, e Técnica Marcial no lugar do Fundamento.** As Bênçãos e a Lapidação ficam com a Maki, que é a única de energia zero.

**Destranca — escolha um destes, obrigatoriamente.** *Os quatro são **de identidade**: eles dizem de onde vem a sua força, e param aí. Nenhum tem relógio, e nenhum pede tarefa.* **É a configuração escolhida aqui que abre a sua lista de Ajusta.**

| Legado | o que ele desenha |
|---|---|
| **Ninhada** | três seres num corpo — o método que funciona |
| **Gêmeos** | dois, e dois não bastam |
| **Inteiro** | um só, e mesmo assim você acordou |
| **Manutenção** | consciência sua, energia de outro |

> **Ninhada** — três seres num corpo só, obrigados a se olharem. É o método que funciona, e funcionou em você. Escreva o que são os três.
>
> **Gêmeos** — foram **dois**, e dois não estabilizam. Vocês se revezam, e nenhum dos dois manda na hora da troca.
>
> **Inteiro** — um núcleo só, e mesmo assim você acordou. Pelo método conhecido isso não acontece.
>
> **Manutenção** — a consciência é sua; **a energia é de quem te fez, e ela acaba.** Escreva quem te abastece e o que ela cobra. Você decide quando ir.

**Ajusta — três por configuração, e você só alcança os da sua.** *É a única Origem com Ajusta gatilhado, e o motivo está abaixo.*

**Ninhada**

| Legado | alcança | relógio |
|---|---|---|
| **Rodízio** | três perícias nomeadas (3) | por cena |
| **Vigília** | Iniciativa (1) | por cena |
| **Desempate** | qualquer Teste de Resistência (4) | por dia |

> **Rodízio** — escolha **três perícias na criação, uma por ser**. Uma vez por cena, role uma delas como se fosse treinada. Cada um sabia fazer uma coisa, e vocês três continuam sabendo.
>
> **Vigília** — uma vez por cena, role **Iniciativa com vantagem**. Nunca estão os três dormindo ao mesmo tempo.
>
> **Desempate** — uma vez por dia, refaça um **Teste de Resistência** que você falhou. Dois cederam e o terceiro não, e é o terceiro que decide.

**Gêmeos**

| Legado | alcança | relógio |
|---|---|---|
| **Cabeça Trocada** | uma perícia nomeada (1) | por cena |
| **Nunca os Dois** | TR Intelecto (1) | por cena |
| **Palpite** | qualquer perícia não treinada | por dia |

> **Cabeça Trocada** — escolha **uma perícia e um atributo na criação**: é o jeito que a outra faz aquilo. Uma vez por cena, role essa perícia com esse atributo em vez do que ela pede.
>
> **Nunca os Dois** — uma vez por cena, refaça um **Teste de Resistência de Intelecto** que você falhou. Enquanto uma cede, a outra ainda está lá.
>
> **Palpite** — uma vez por dia, role com **vantagem** um teste de perícia em que você **não** é treinado. Ela chuta, e ela chuta bem — e você descobre junto com todo mundo.

**Inteiro**

| Legado | alcança | relógio |
|---|---|---|
| **Feito de Uma Peça** | TR Vigor (1) | por cena |
| **Teimosia** | uma situação nomeada (1) | por cena |
| **Peça Única** | uma perícia nomeada (1) | por cena |

> **Feito de Uma Peça** — uma vez por cena, refaça um **Teste de Resistência de Vigor** que você falhou. Não existe parte sua que ceda antes das outras.
>
> **Teimosia** — uma vez por cena, refaça um teste para **continuar fazendo uma coisa que você já começou** — segurar, agarrar, sustentar, não largar. Ninguém aí dentro discorda de você no meio.
>
> **Peça Única** — escolha **uma perícia treinada na criação**. Uma vez por cena, role com **vantagem**. Você faz uma coisa, e faz bem.

**Manutenção**

| Legado | alcança | relógio |
|---|---|---|
| **Ajuste Fino** | um ofício nomeado (1) | por cena |
| **Recarga** | duas perícias nomeadas (2) | por descanso curto |
| **Fiado** | qualquer rolagem | por dia |

> **Ajuste Fino** — escolha **um ofício na criação**: é o de quem te fez, e você viu por dentro como se faz. Uma vez por cena, role com **vantagem**.
>
> **Recarga** — escolha **duas perícias na criação**: são as que ela calibrou em você. Uma vez por descanso curto, role uma delas com **vantagem**.
>
> **Fiado** — uma vez por dia, refaça **qualquer rolagem** que você falhou: ela cobre a diferença de onde estiver. **Escreva na ficha o que você passou a dever, e isso não sai no descanso.**

#### O que separa as doze, e o teste que elas tinham que passar

**Cada configuração ficou com um território, e nenhum dos doze serve a duas.** Era o teste que eu tinha marcado antes de escrever, e ele é o que decide se o gatilho faz trabalho ou é enfeite:

| configuração | o que ela compra | a leitura |
|---|---|---|
| **Ninhada** | largura — três perícias, iniciativa, todos os TRs | três sabem mais que um |
| **Gêmeos** | o repertório que não é seu — atributo trocado, perícia não treinada, o TR que resiste enquanto o outro cede | a outra faz o que você não faz |
| **Inteiro** | profundidade — um TR, uma situação, **uma** perícia com vantagem | um faz melhor que três |
| **Manutenção** | o que outra pessoa pôs em você, e a conta | você é bom no que ela calibrou |

**O par que quase colidiu, e por que não colide:** *Rodízio* (Ninhada) e *Peça Única* (Inteiro) mexem os dois em perícia por cena. Um dá **três** perícias como se treinadas — largura sem profundidade; o outro dá **uma** treinada com vantagem — profundidade sem largura. **Nenhum contém o outro, e a oposição é literalmente a ficção das duas configurações.**

**A escada ganhou um degrau que estava parado.** *Recarga* é a primeira entrada do catálogo inteiro a usar **por descanso curto** — os quatro degraus da peça 10 existem desde a v0.23 e o catálogo só vinha usando cena, dia e descanso longo. O degrau serve a ficção do abastecimento sem inventar relógio nenhum.

**E o Fiado é o único Ajusta do catálogo que cobra.** Ele é *qualquer rolagem por dia*, que é o alcance do **Passagem** do Receptáculo — e paga a diferença com dívida escrita que não sai no descanso, no mesmo molde do *O Que Ele Quer*. Sem a cobrança ele seria o Passagem com outra ficção; com ela, é a coleira funcionando como coleira.

**Desliga**

| Legado | apaga | relógio |
|---|---|---|
| **Ferro Velho** | os degraus de exaustão | sempre |
| *— vaga reservada —* | **espera a peça de Técnica Marcial** | — |

> **Ferro Velho** — cansaço não é uma coisa que acontece com você: os degraus de exaustão não te alcançam. Você não dorme porque precisa, dorme porque combinaram que era hora. *Em troca, você também não sente quando está perto de quebrar — o seu corpo não avisa antes, ele só para.*

*A vaga espera **Técnica Marcial**, e a peça 9 já dizia isso na linha de criação desta Origem: **"Técnica Marcial — não existe ainda"**. Ela não usa ferramenta amaldiçoada e não é objeto amaldiçoado; o que ela não tem é a economia de poder que substitui o Fundamento nela.*

> **Esta vaga dizia "espera a peça de equipamento", e isso vinha de uma dependência de segunda mão.** *Corrigido na v0.49.* Técnica Marcial **estava** bloqueada por equipamento — e essa trava caiu na v0.48, quando a peça 14 fechou. **A vaga não esperava a peça que ela nomeava: esperava a peça que aquela destravava.** Agora ela nomeia a certa, e a certa é a próxima da fila.

#### As quatro configurações, e por que o Ajusta desta Origem é gatilhado

**O eixo não é quantos núcleos você tem: é de onde vem a sua energia e quem decide quando você age.** Três configurações têm energia própria — um, dois e três seres — e a quarta depende de terceiro. *São quatro histórias completamente diferentes com zero diferença no dado*, que é a definição do formato de identidade.

**E é justamente por serem zero no dado que o Ajusta precisou ser gatilhado.** Nas outras seis Origens o Destranca é uma escolha ao lado das outras; aqui ele é **o que você é**, e um catálogo de Ajusta livre faria a Ninhada e o Inteiro comprarem exatamente a mesma coisa. *Configuração sem consequência é sabor pendurado numa ficha* — e o teste dos 90% pega isso na segunda sessão.

**A conta do que o jogador alcança**, contra as outras Origens:

| | segundo Legado escolhido entre |
|---|---|
| as outras seis Origens | 4 Ajusta + 1 a 2 Desliga = **5 a 6** |
| Corpo Amaldiçoado | 3 Ajusta da sua configuração + 1 Desliga = **4** |

**Quatro contra cinco ou seis é estreito de propósito e não é buraco.** A ficha leva dois Legados, então basta que o segundo tenha escolha real — e o que se perde em largura se ganha em amarração: nenhum dos doze Ajusta desta Origem serve a duas configurações, então nenhum deles é genérico. *Dois foram o número proposto primeiro; três entrou porque linha única precisa de opção, e a diferença custa quatro entradas de catálogo e zero de regra.*

**O Desliga fica no nível da Origem, e isso não foi escolha — foi suprimento.** Um Desliga por configuração pediria **quatro alvos nomeados e sem dono**, e a enumeração da seção 8 tem **zero livres** depois que o *Ferro Velho* gastou os degraus de exaustão. Inventar quatro é escrever entrada para fechar contagem, que é o que reprovou o *Não Sou Gente* e os três Desliga de condição. **E o Ferro Velho serve as quatro de qualquer jeito:** ele é sobre ser corpo fabricado, não sobre contagem de núcleo.

**A configuração de núcleo pilotado ficou de fora, e o motivo é limpo:** um cadáver operado à distância não é personagem — o personagem é quem pilota, e quem pilota já tem Origem própria. É o **Kokichi Muta**, Restrição Celestial pelo ramo do corpo trocado pela técnica, e o Mechamaru é a ferramenta dele.

**O Inteiro é invenção declarada, e o texto dele para na hora certa.** O canon diz que três almas se observando é o caminho para consciência e energia próprias; um núcleo só que consegue as duas **quebra o método**. A primeira versão fazia o mundo reagir — *"quem estuda o assunto vai querer saber como"* — e isso é **enredo tirado do mestre sem ele ter pedido**. O Legado diz que você é a exceção; **o que o mundo faz com isso é da mesa, não da ficha.**

**Manutenção não desce ao número, e isso é de propósito.** Com a Origem passando a ter PE, era tentador fazer a dependência drenar PE — e aí ela deixaria de ser Destranca. **A coleira é ficção: quem te abastece existe, é alcançável, e cobra.** Se em playtest ela precisar morder em número, o conserto não é esticar este Legado, é escrever a coisa na camada de Técnica Marcial, onde preço tem casa.

*Ela é a única das quatro em que o jogador **escolhe se pôr** naquela situação em vez de só descrever o que é — e foi a única que sobreviveu à primeira leva sem reescrita.*

**Dominância entre os quatro: nenhuma, e ela nem se aplica.** Identidade não se domina: as quatro descrevem coisas mutuamente exclusivas, e nenhuma entrega número. **O teste que importa aqui é o outro** — se as três Ajusta de cada configuração não se copiarem entre configurações, o gatilho está fazendo trabalho; se copiarem, ele é enfeite. *Fica marcado para quando as doze estiverem escritas.*

### Feto — *você foi feito, não nascido*

> **A pesquisa desta lista mexeu na premissa da Origem, e o conserto veio do próprio canon.** A peça 9 abre com *"nem todo Feto é Pintura da Morte"* — e, pelo material, **não existe outra categoria de pessoa meio-humana e meio-maldição.** O que existe com esse nome é outra coisa: **cadáver amaldiçoado em estágio de útero**, uma maldição imatura que vira maldição inteira depois da metamorfose. O do centro de detenção é esse. **Não é gente, e não vira gente.**
>
> **Mas a frase está certa por um caminho melhor do que o que ela usava.** As nove Pinturas da Morte foram feitas pelo **mesmo autor**, e esse autor fez outras coisas em outros corpos — e uma delas **nasceu de gente, do jeito normal**. O irmão que o mais velho reconheceu não era Pintura da Morte nenhuma. **A irmandade é definida por quem te fez, não pelo que você é.**
>
> Isso vale para o catálogo inteiro: **a Origem é "alguém te fabricou de propósito", e Pintura da Morte é o exemplar famoso, não a definição.**

**Destranca — escolha um destes, obrigatoriamente.** *De identidade, os quatro.*

| Legado | o que ele desenha |
|---|---|
| **Irmãos** | a irmandade, e quem entra nela |
| **Numeração** | você foi contado, e existe registro |
| **Guardado** | você foi objeto antes de ser pessoa |
| **Devagar** | o seu corpo não usa o mesmo calendário |

> **Irmãos** — escreva **quantos vocês eram e o que aconteceu com eles**. Você reconhece um irmão quando encontra, e sabe quando um morre, esteja onde estiver. **Nem todos se parecem com você** — quem te fez fez outras coisas, em outros lugares, e algumas delas nasceram de gente.
>
> **Numeração** — você não é só um nome: **você é um número dentro do que alguém estava tentando**. Escreva qual é o seu e quantos eram no total. Quem sabe do assunto reconhece a série.
>
> **Guardado** — antes de acordar você foi **coisa**, e alguém te teve. Escreva **quem te guardou, onde, e por quanto tempo**. Essa pessoa, ou o que sobrou dela, ainda tem a ver com você.
>
> **Devagar** — o seu corpo não envelhece no calendário dos outros. Escreva **há quanto tempo você existe** e com que idade você parece. Quem te conheceu antes vai notar; você não.

**Ajusta**

| Legado | alcança | relógio |
|---|---|---|
| **Meio e Meio** | veneno e doença (1) | por cena |
| **Como Se Monta** | Medicina (1) | por cena |
| **Faro** | maldição (1) | por cena |
| **Paciência** | qualquer perícia | por dia |

> **Meio e Meio** — uma vez por cena, role com **vantagem** um Teste de Resistência contra **veneno ou doença**. Metade de você não é feita de carne, e essa metade não escuta.
>
> **Como Se Monta** — uma vez por cena, refaça um teste de **Medicina** que você falhou. Você sabe do que corpo é feito porque alguém montou o seu na sua frente.
>
> **Faro** — uma vez por cena, quando o que você procura é **maldição**, role **Sentir Energia no lugar de Investigação**. Você não deduz onde ela está; você sente, porque é parente.
>
> **Paciência** — uma vez por dia, refaça um teste de perícia feito **enquanto você esperava, vigiava ou estava escondido sem se mexer**. Você já passou mais tempo parado do que a maior parte das pessoas passa viva.

**Desliga**

| Legado | apaga | relógio |
|---|---|---|
| **Sangue que Não é Sangue** | comer, dormir, respirar | sempre |
| **Talhe** | ficar `Agarrado` | por cena |

> **Talhe** — você foi guardado antes de andar, e o corpo aprendeu a sair: uma vez por cena, você **não fica `Agarrado`**. *Em troca, você sai por onde couber — quem te agarrou escolhe se você larga uma coisa que estava na sua mão ou termina o movimento fora da posição em que queria estar.*


> **Sangue que Não é Sangue** — você não precisa comer, dormir nem respirar como um humano. Isso resolve problemas que param os outros. *Em troca, cria problemas que os outros não têm — e nenhum deles tem nome ainda, porque ninguém precisou nomear fome para gente que come.*

#### O Irmãos saiu do piso, e quem consertou foi o canon

**O defeito estava registrado desde a v0.24: o jogador não conseguia disparar.** *"Você sente quando outro Feto está por perto, e ele sente você"* só acende quando o **mestre** põe outro Feto na cena — e o efeito ainda era simétrico, revelando você tanto quanto revelava o outro. Era o exemplar do que a cláusula do Destranca existe para pegar.

**O conserto não foi inventar um gatilho: foi ler o que a irmandade é.** No material, o reconhecimento de irmão **não depende de o outro ser da mesma fabricação** — o mais velho reconheceu como irmão alguém nascido de gente, porque quem os fez foi o mesmo. Então:

> **O gatilho é o jogador apontar alguém e dizer que é irmão.** É afirmação sobre o mundo, é do dono da ficha, e é exatamente o que aconteceu na obra.

E a assimetria some junto: *você* reconhece, *você* sabe quando um morre. Não é radar de mão dupla que entrega a sua posição.

**A `Numeração` e o `Guardado` saíram dos traços da peça 9**, como no Latente — *os irmãos e o que aconteceu com eles* e *quem te fez, e onde essa pessoa está*. O `Devagar` saiu do terceiro, *o corpo que não envelhece igual*, e é o único dos quatro que não põe outra pessoa no mundo: ele põe **tempo**, que é a única coisa que esta Origem tem de sobra.

**Um nome morreu na triagem e o motivo é fino:** *Fora do Tempo* saiu `OCUPADO` porque carrega **Tempo**, que é Família do manual. *Sem Pressa* caiu junto — **Pressa** é Melhoria. Sobrou **Devagar**, que é a palavra que nenhum dos dois estava conseguindo dizer.

**E uma coisa que o catálogo não vai tocar:** as Pinturas da Morte manipulam sangue, e isso é **técnica de clã** — a peça 9 proíbe qualquer Origem de abrir, fechar ou conceder técnica. Sangue fica de fora dos quatro Ajusta, e é por isso que eles compram percepção, medicina e espera em vez de arma.

**Dominância na lista: nenhuma. Quatro Destranca · quatro Ajusta · dois Desliga escritos.**

### Restrição Celestial — *você trocou uma coisa por outra antes de nascer, e não foi você que assinou*

> **Esta é a única Origem com sub-escolha antes do Legado, e ela já existia — só não estava ligada à lista.** A peça 9 separa os dois ramos na criação: *corpo pela técnica* conjura com o Fundamento normal, *sem energia* vai para a Técnica Marcial e não tem PE, feitiço de Toque nem Sentir Energia. *O segundo se chamava `energia pelo corpo` até a v0.117.* **O ramo vem antes, e gateia Destranca e Ajusta.**
>
> E os dois Legados que já existiam **já eram um por ramo**, sem ninguém ter marcado: *Alcance Impossível* só faz sentido em quem opera de longe, *Peso Real* só em quem lê o mundo sem energia.

**Corpo pela técnica — Destranca** *(o corpo não funciona, e a energia é enorme)*

| Legado | o que ele desenha |
|---|---|
| **Nasci Assim** | o que o seu corpo não faz, e o que isso cobra todo dia |
| **O Substituto** | as pessoas conhecem uma coisa que não é você |
| **A Oferta** | você já pensou no preço de um corpo que funcione |
| **Nunca Estive Lá** | você conhece lugares onde o seu corpo nunca esteve |

> **Nasci Assim** — escreva **o que o seu corpo não faz e o que isso te cobra todo dia**: o que dói, o que falta, o que você não pode encarar. Não é segredo e não tem conserto conhecido.
>
> **O Substituto** — o meio jujutsu conhece você por **uma coisa que não é o seu corpo** — um nome, uma voz, uma casca. Escreva o que é. Quase ninguém sabe que existe outra pessoa do outro lado, e quem sabe conta nos dedos.
>
> **A Oferta** — você já pensou no que daria por um corpo que funcione, e **já chegou a um número**. Escreva qual é. Existe gente que vende esse tipo de coisa, e uma delas sabe que você existe.
>
> **Nunca Estive Lá** — a sua energia vai a lugares que você não vai. Escreva **um lugar que você conhece de cor e onde o seu corpo nunca pisou**, e o que você viu acontecer lá.

**Corpo pela técnica — Ajusta**

| Legado | alcança | relógio |
|---|---|---|
| **Antena** | Sentir Energia (1) | por cena |
| **Do Meu Canto** | uma situação nomeada (1) | por cena |
| **Insônia** | qualquer perícia | por dia |
| **Li Tudo** | duas perícias nomeadas (2) | por cena |

> **Antena** — uma vez por cena, refaça um teste de **Sentir Energia** que você falhou. O seu alcance não é normal, e você passou a vida usando ele no lugar dos olhos.
>
> **Do Meu Canto** — uma vez por cena, role com **vantagem** um teste feito **sem sair do lugar em que você está**. Você nunca precisou chegar perto para trabalhar.
>
> **Insônia** — uma vez por dia, refaça um teste de perícia feito **enquanto os outros dormiam**. Dor não tem horário, e você aproveitou as horas.
>
> **Li Tudo** — uma vez por cena, refaça um teste de **Ocultismo ou Investigação** que você falhou. Você teve tempo parado que ninguém mais teve.

**Energia pelo corpo — Destranca** *(sem energia nenhuma, e o corpo é sobre-humano)*

| Legado | o que ele desenha |
|---|---|
| **Descartado** | o clã que te jogou fora |
| **Dividido** | a sua restrição foi partida com outra pessoa |
| **Desde Criança** | a ferramenta que te acompanha desde sempre |
| **Aprendi a Ver** | você não nasceu enxergando maldição |

> **Descartado** — a sua família é do meio e te tratou como erro. Escreva **quem te descartou e o que fizeram você fazer enquanto esteve lá**. Eles continuam existindo, continuam achando que estavam certos, e você conhece a casa por dentro.
>
> **Dividido** — a sua restrição **não é sua sozinha**: ela foi partida com alguém que nasceu junto de você. Escreva quem é e onde essa pessoa está. Enquanto os dois lados existirem, nenhum dos dois está inteiro.
>
> **Desde Criança** — existe **uma ferramenta que anda com você desde antes de você escolher**. Escreva o que é e como veio parar na sua mão. Quem entende de ferramenta reconhece aquela.
>
> **Aprendi a Ver** — você **não nasceu enxergando maldição**, e a maior parte de quem te olha supõe que sim. Escreva **como você resolveu isso** — o que você usa, ou o que você treinou até substituir o que falta.

**Energia pelo corpo — Ajusta**

| Legado | alcança | relógio |
|---|---|---|
| **Sentido Treinado** | maldição (1) | por cena |
| **Couro** | TR Físico (1) | por cena |
| **Ninguém Viu** | Furtividade (1) | por cena |
| **No Braço** | qualquer perícia de Força ou Destreza | por dia |

> **Sentido Treinado** — uma vez por cena, role **Percepção no lugar de Sentir Energia**. Você não sente energia — você aprendeu a notar o que ela mexe.
>
> **Couro** — uma vez por cena, refaça um **Teste de Resistência Físico** que você falhou. O corpo é a única coisa que a troca te deu, e ele é absurdo.
>
> **Ninguém Viu** — uma vez por cena, refaça um teste de **Furtividade** que você falhou. Você não emite nada, e passou a vida aproveitando isso.
>
> **No Braço** — uma vez por dia, refaça um teste de perícia **de Força ou Destreza** que você falhou.

**Desliga — dos dois ramos**

| Legado | apaga | relógio |
|---|---|---|
| **Peso Real** | ser enganado por barreira, véu e ferramenta | sempre |
| **Assinado** | ficar `Cego` | por descanso longo |

> **Assinado** — você nunca leu o mundo pela energia, e o resto do corpo cobriu: uma vez por descanso longo, você **não fica `Cego`**. *Em troca, a troca não foi só essa. Escreva na ficha uma coisa comum que você nunca vai conseguir fazer — e ela não volta, em nível nenhum.*


> **Peso Real** — você percebe **ferramenta amaldiçoada, barreira e véu pelo tato e pelo peso, não pela energia**. O que engana feiticeiro não engana você. *Em troca, você percebe que tem alguma coisa ali e não o que é — o aviso vem sem nome.*

*A vaga espera **ferramenta amaldiçoada**, e esta é a Origem que mais depende dela: pelo ramo sem energia nenhuma, **ferramenta amaldiçoada é o único jeito de ferir maldição** — a peça 5 §3 escreve isso com todas as letras. O `Peso Real` já cita ferramenta no próprio texto.*

#### O que o levantamento trouxe, e o que ele matou

**Dois ganchos vieram do material e eu não teria inventado nenhum dos dois.**

O primeiro: **quem não tem energia não nasce enxergando maldição.** Os dois exemplares canônicos resolveram isso por caminhos diferentes — um treinou os sentidos até perceber pelo que a maldição mexe no mundo, a outra usou ferramenta para enxergar. **Isso vira o `Aprendi a Ver` e o `Sentido Treinado`**, e conserta uma suposição que o catálogo fazia de graça: que perceber maldição é padrão de todo personagem.

O segundo: **a restrição pode vir partida.** No material, dois nascidos juntos contam como um para efeito de jujutsu, e enquanto os dois lados existem nenhum dos dois está completo. É o `Dividido`, e é a única entrada do catálogo inteiro em que **o Legado descreve uma coisa que ainda não terminou de acontecer**.

**E o `Alcance Impossível` morreu.** *"Aja de um lugar em que o seu corpo não está"* é **técnica** — operar à distância é exatamente o que a técnica do exemplar canônico faz —, e a peça 9 proíbe Origem de conceder técnica. É o mesmo diagnóstico do `Núcleos` e do `Não Sou Gente`: **não é Legado, é kit de poder, e o dono aqui é o Fundamento.** O ramo do corpo fraco conjura normalmente, então alcance absurdo é Melhoria de feitiço.

O que sobrou dele virou duas coisas que **não** são técnica: o `Nunca Estive Lá`, que é o conhecimento sem o poder, e o `Do Meu Canto`, que é a vantagem de quem nunca precisou chegar perto.

**O `Peso Real` passou a valer nos dois ramos**, e ganhou a cláusula de troca que a régua exige e que ele não tinha: *o aviso vem sem nome*. Você sabe que tem coisa ali; não sabe o quê.

**Cinco nomes morreram na triagem nesta lista**, o recorde de uma leva só: *Alcance* (está dentro do próprio Legado que morreu, e é Família), *Longe* (Melhoria, e está dentro de *Muito Longe*), *Anos Parado* (**Parado** é Restrição), *Osso Duro* (**Osso** é Tema), *Sem Rastro* (**Rastro** é Melhoria). E *Marra* saiu `fraco`, a uma letra de **Marca**.

**Dominância: nenhuma, dentro de cada ramo.** E **entre ramos ela não se aplica** — ninguém escolhe entre os dois lados, o ramo já veio da criação.

### Sem Técnica — a sub-origem, e a única entrada que mora fora de uma lista

**Sem Técnica não é Legado de catálogo, e não pode ser.** Ela tem construção própria em cima — rota de criação, economia de poder, duas peças que ainda não existem —, e enfiar isso numa linha de lista seria fingir que cabe. **Mas ela também não pode ficar invisível na camada onde o jogador escolhe quem é.**

> **Então ela entra como uma entrada de Destranca que aponta para fora:** ela está disponível nas cinco Origens que aceitam a sub-origem, e o corpo dela é um ponteiro.

> **Sem Técnica** — você tem energia amaldiçoada e **a técnica não veio junto**. Não é defeito e não é falta: é outro caminho, e ele tem seção própria. **Escolhendo esta linha, o seu poder não sai do Fundamento** — sai de aptidão ou de escola de espada, e é lá que você monta o personagem.

**Escrita uma vez, e as cinco listas apontam para cá.** Cinco cópias do mesmo texto em cinco Origens é a lição nº 9 acontecendo dentro de um catálogo — e é o defeito que este projeto mais paga para evitar. **Um texto, um dono.**

**Quem pode pegar:** Latente · Receptáculo · Descendente · Reencarnado · Feto. **As duas especiais não** — Corpo Amaldiçoado e Restrição Celestial já vêm com uma troca própria embutida, e a peça 9 fecha isso.

**Nas cinco, ela é um quinto Destranca**, e a lista deles vai a cinco. É a mesma exceção que o Descendente já tem por outro motivo — lá são quatro arquétipos de clã, aqui é uma porta para fora.

#### O que a pesquisa mudou sobre o tamanho desta rota

*O `arquitetura.md` avisa que Sem Técnica precisa de "um sistema próprio, paralelo ao Fundamento". Pelo material, precisa de menos.*

| rota | o que ela é, de verdade |
|---|---|
| **Aptidão** | **Energia Reversa não é técnica inata** — é manipulação de energia amaldiçoada, e é exatamente por isso que alguém sem técnica consegue usar. O que é raro nela é curar **os outros** |
| **Estilo da Sombra** | **anti-domínio**, e a espada é o jeito mais comum de usar — não o requisito |

**As duas caem na camada de aptidão e ferramenta, e metade já está construída:** as quatro anti-domínio entraram na v0.29, e a `Energia Reversa` fechou na v0.78, na peça 11 §6. **O que falta de verdade é ferramenta amaldiçoada, que é a peça 2 da fila.**

> **A espada não é obrigatória, e o projeto já sabia disso antes de a prosa saber.** A peça 9 descreve o Estilo da Sombra como *"técnica de espada e corpo"*, e no material a técnica central dele **foi aprendida em um mês por alguém que não usa espada**. Mais: o exemplar canônico de grau 1 virou líder da escola e **derrubou as restrições dela**. A **seção 6.5 da peça 11 já trata o Domínio Simples como aptidão pura** — raio em volta de você, com os pés no chão, sem uma palavra sobre lâmina. *A mecânica estava certa e a prosa da peça 9 estava mais estreita que ela.*

#### E a rota precisa de sistema de criação próprio

*Decidido com o Mizuki na v0.38.* **Sem Técnica não pode ser "os outros menos o Fundamento".** Se a rota for só subtração, ela fica atrás de todo mundo e ninguém escolhe por vontade — escolhe por castigo.

> **O poder dela vem da manipulação criativa da energia amaldiçoada, montada em aptidões — e isso precisa de uma máquina de construção com a mesma dignidade que o Fundamento tem.**

Duas rotas dentro dela, e **as duas são de aptidão**: uma que vai fundo no que qualquer feiticeiro pode fazer com energia, e outra que vai fundo em anti-domínio e corpo. A peça de aptidões já carrega metade do vocabulário; o que falta é a **criação** — quantas, com que orçamento, e com o que se paga.

*Não é peça 13. Fica registrado aqui porque foi esta lista que fez a pergunta aparecer.*

#### Uma entrada do catálogo quebra, e é uma só

De oitenta entradas, **exatamente uma** pressupõe que você tem técnica:

> **Inédito** *(Latente, Desliga)* — *"a **sua técnica** não está em registro nenhum"*.

Quem não tem técnica não tem o que esconder. **Todo o resto funciona**, porque Sem Técnica tem energia amaldiçoada e tem Sentir Energia — o que falta é a técnica inata. Faro, Antena, Máscara e os outros continuam de pé.

**O conserto é uma linha no Inédito** dizendo que ele não está disponível para quem é Sem Técnica, e a checagem 8 do validador confere isso.

#### Duas coisas da peça 9 que precisam mudar junto

**A frase *"Sem Técnica não dá um segundo Legado"* perdeu o sentido.** Ela foi escrita quando a ficha levava **um** Legado. Com dois, a leitura certa é: **Sem Técnica não amplia a conta — ela ocupa uma das duas vagas, como Destranca.**

**E a raridade fica como está, por decisão declarada.** *No material, técnica inata compõe mais de 80% do repertório de um feiticeiro, e o exemplar canônico de grau 1 sem técnica é apontado como o único no nível dele.* **É raro lá e continua comum aqui**, porque a rota precisa ser escolhível sem virar exceção negociada com o mestre — e **quem escolhe é o jogador, nunca a mesa**. *O desvio fica escrito em vez de escondido, que é a diferença entre decisão e descuido.*

### 9.9 · O Não Sou Gente saiu do catálogo inteiro, e o nome foi com ele

*O último dos catorze antigos que a régua reprovava.* Ele dizia:

> ~~**Não Sou Gente** — veneno, doença e o que ataca corpo humano não te pegam. Cura que funciona em humano também não.~~

**A metade que é dano vira Passiva de Regra Própria, e leva o nome.** É o que o manual manda com todas as letras: *"nenhuma Melhoria fura imunidade; quem quiser isso monta uma Passiva de Regra Própria com o mestre, com limite de uma vez por cena"*. Passiva custa **espaço de feitiço conhecido**, que é a moeda certa — e a cláusula de cura que não funciona já era o preço embutido, agora pago no lugar certo.

**E a outra metade não virou Legado nenhum, porque ela já existe.** *"Você não é uma pessoa"* é **a primeira linha da Origem** na peça 9:

> *"Você não é uma pessoa. Você é uma coisa que alguém fez e que acordou."*

**Um Legado que afirma o que a Origem que o contém já afirma é a lição nº 9 em escala pequena** — duas cópias da mesma frase, e uma delas vai divergir. O Corpo Amaldiçoado inteiro é o Legado que essa metade seria.

*Isso fecha os quatro do catálogo antigo que a régua tinha marcado:* o **Não Sou Gente** muda de camada, o **Irmãos** ganhou gatilho do jogador, o **Instinto Bruto** perdeu a metade morta, e o **Alcance Impossível** saiu por ser técnica. **Nenhum dos quatro sobreviveu como estava, e nenhum foi apagado sem destino.**

---

**A conta dos formatos, com todas as sete Origens escritas:**

| Origem | Destranca | Ajusta | Desliga escrito | Desliga reservado | escritos |
|---|---|---|---|---|---|
| Latente | 4 | 4 | 2 | — | **10** |
| Receptáculo | 4 | 4 | 2 | — | **10** |
| Descendente | 5 | 4 | 2 | — | **11** |
| Reencarnado | 4 | 4 | 1 | 1 | **9** |
| Corpo Amaldiçoado | 4 | **12** | 1 | 1 | **17** |
| Feto | 4 | 4 | 2 | — | **10** |
| Restrição Celestial | **8** | **8** | 2 | — | **18** |
| | **33** | **40** | **12** | **2** | **85** |

**Mais o `Sem Técnica`** — uma entrada só, escrita fora das listas e compartilhada pelas cinco Origens que o aceitam. **Oitenta e seis no total.**

**Oitenta e cinco entradas escritas, e duas vagas de Desliga declaradas.** *Eram sete até a v0.104: as cinco que a peça 19 e a peça 16 tinham destravado foram preenchidas, e as duas que sobram esperam peça que ainda não existe — `objeto amaldiçoado` e `Técnica Marcial`.* As duas Origens com sub-escolha — Corpo Amaldiçoado e Restrição Celestial — respondem por **35 delas**, e nas duas o jogador alcança bem menos do que o catálogo tem.

| | o jogador escolhe o segundo Legado entre |
|---|---|
| Latente · Receptáculo · Descendente · Reencarnado · Feto | **4 a 6** |
| Corpo Amaldiçoado | 3 Ajusta da configuração + 1 Desliga = **4** |
| Restrição Celestial | 4 Ajusta do ramo + 1 Desliga = **5** |

*O Corpo Amaldiçoado fechou com **doze** Ajusta — três por configuração —, e o jogador alcança três. É a única Origem com Ajusta gatilhado, e a única que passa de dez entradas: dezessete escritas para quatro alcançáveis como segundo Legado.*

**As sete listas estão escritas.** O que falta para a metade 2 fechar: o **Não Sou Gente** virar Passiva, e as **duas** vagas de Desliga que sobraram, que dependem de peça que ainda não existe. *O validador dos Legados existe desde a v0.39; as outras cinco vagas fecharam na v0.104.*

**O alvo livre acabou.** O *Ferro Velho* gastou os degraus de exaustão, que era o último da enumeração da seção 8 — **daqui para a frente, todo Desliga novo depende de peça nova criar coisa nomeada.** Feto e Restrição Celestial têm um Desliga escrito cada no catálogo antigo e vão entrar já com uma vaga aberta.

**Só o Latente fecha a cota de Desliga hoje, e ele é o único que tinha dois alvos.** As outras três carregam vaga declarada — quatro no total, contra **um** alvo livre no sistema inteiro, que já está reservado para o Corpo Amaldiçoado. **A dívida de alvo é a conta desta régua, e ela é visível de propósito.**

O Descendente leva cinco Destranca porque contém quatro clãs por dentro; o resto varia porque **o suprimento de alvo é estreito por construção**, e não porque alguma lista foi escrita com menos cuidado. *Uma Origem que fechasse em dez por ter dez seria a única prova de que a régua não está sendo aplicada.*

> ~~**Quando equipamento fechar, a primeira coisa a fazer é voltar aqui**~~ — quatro vagas, e três delas esperavam essa peça ou a de dano e condições. **As duas peças existem: equipamento é a 14 desde a v0.48 e dano e condições é a 19 desde a v0.103, e ninguém voltou aqui em nenhuma das duas vezes.** *Decisão registrada não é decisão aplicada, duas vezes seguidas.*

*Faltam três listas: Feto, Corpo Amaldiçoado e Restrição Celestial.*

## 10. O que fica para a outra metade

O catálogo, e as decisões de sabor que vêm com ele:

- ~~**As três listas que faltam**~~ — **as sete fecharam na v0.38**, 81 entradas escritas.
- ~~**Os três relógios fora da escada**~~ — **descidos**: *Aprendi Apanhando* e *A Voz de Dentro* para por dia, *O Que Ninguém Lembra* para por descanso longo.
- ~~**O piso do Irmãos**~~ — **resolvido na lista do Feto**, pelo canon: a irmandade é definida por quem te fez, e o gatilho virou o jogador apontar alguém e dizer que é irmão.
- **Sobraram DUAS vagas de Desliga**, e as duas esperam peça que ainda não existe: uma espera `objeto amaldiçoado`, no Reencarnado, e a outra espera **Técnica Marcial**, no Corpo Amaldiçoado. *Eram sete.* **As cinco destravadas foram escritas na v0.104** — três que esperavam a peça 19 e duas que esperavam a peça 16 —, e todas as cinco só couberam porque a trava do `Desliga` foi relaxada na mesma versão: *ele passou a poder apagar condição uma vez, com o relógio saindo do nível dela.* *Reclassificadas na v0.49: as quatro que diziam "equipamento" nomeavam a peça errada, e nenhuma delas abriu quando aquela peça fechou.*

  > **⚠ E as outras DUAS já destravaram, e ninguém voltou.** *Elas esperavam `ferramenta amaldiçoada`, que virou a peça 16 na v0.59 — a `Armaria` do Descendente e a Restrição Celestial.* **A peça 16 §9 registra que destrava as duas; esta peça continuava dizendo que elas esperam.** *Achado na v0.100, e a linha da tabela de cada uma continua dizendo `espera a peça de ferramenta amaldiçoada` — escrever as duas é trabalho, não conserto de texto.*
- **O `Inédito` precisa da linha que o fecha para Sem Técnica** — é a única das 81 entradas que pressupõe técnica própria.
- ~~**A peça 9 precisa de três consertos que esta peça gerou:** a frase *"Sem Técnica não dá um segundo Legado"*, o §5 que ainda diz que Corpo Amaldiçoado não tem energia, e o `Alcance Impossível`, que é técnica e sai do catálogo.~~ **Os três foram aplicados na v0.39.** *Lá a Origem Sem Técnica diz hoje que ela **não amplia a conta de Legados** — é uma entrada de `Destranca` e ocupa uma das duas vagas —, o Corpo Amaldiçoado diz que **tem energia amaldiçoada**, e o `Alcance Impossível` não aparece em nenhuma lista daquela peça.*
- ~~**Não Sou Gente sai do dano**~~ — **resolvido na v0.38: o nome inteiro foi para a Passiva, e o Legado deixou de existir.** A seção 9.9 tem o porquê.
- ~~**O piso do Irmãos**~~ — **resolvido na lista do Feto.** O gatilho virou *o jogador apontar alguém e dizer que é irmão*, que é o que a irmandade faz no material: ela é definida por **quem te fez**, e alcança gente que não é da mesma fabricação.
- ~~**Instinto Bruto está metade morto** e a régua não conserta isso: *"use Sentir Energia no lugar de Percepção"* é trocar Essência por Essência desde a v0.16.~~ **Consertado na v0.39, nesta mesma peça.** *A metade morta saiu: a seção 9 publica ele como "role Sentir Energia no lugar de **Intuição**", que é Inteligência — e aí é troca de verdade, de até +4 para quem conjura.*
- ~~**O validador dos Legados**, que sai junto com a peça e não sete versões depois.~~ **Saiu junto: o `conferir-legados.py` entrou na v0.39, na mesma versão desta peça.** *A tabela abaixo é a especificação que ele foi escrito para cumprir, e fica como registro do que foi pedido.* As checagens que esta régua pede:

| # | o que ele confere | de onde ele lê o certo |
|---|---|---|
| 1 | todo Legado declara um dos três formatos | a tabela da seção 4 |
| 2 | todo relógio é degrau da escada de quatro | **a peça 10**, lida de lá — nunca escrito no código |
| 3 | a largura do gatilho casa com o degrau: estreito pode cena, largo desce para dia | a seção 5 |
| 4 | **nenhum Desliga encosta em dano** — nem a palavra imunidade, nem resistência | **o manual**, que é dono dos dois termos |
| 5 | todo Desliga escreve o que custa em troca | a seção 5 |
| 5b | **toda Origem soma dois Desliga entre escritos e reservados**, e **toda vaga nomeia a peça que ela espera** | a seção 8 |
| 6 | todo Destranca **de ação** tem gatilho que o jogador puxa; todo **de identidade** é escolha de criação e não pendura tarefa | a seção 5 |
| 7 | o teste de conjunto da peça 3 dentro de cada lista de Origem | **a peça 3** |
| 8 | dois Legados por ficha, N por Origem, e as Origens citadas existem | **a peça 9** |
| 9 | **o `Sem Técnica` aparece nas cinco Origens que o aceitam e em nenhuma das duas especiais**, e nenhuma entrada disponível para ele pressupõe técnica própria | **a peça 9** |

Com o limite de design declarado à parte da regra aplicada — lição nº 8 —, e **teste negativo em cada uma**, conferindo antes que a base passa, que é o que a v0.35 pagou para aprender.
