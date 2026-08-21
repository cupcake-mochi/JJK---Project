# Estado atual do projeto

Atualizado em 21/08/2026, na v0.111 (última peça fechada: **Dano e condições**, ampliada na v0.104 com a penalidade de arma; antes dela, a **Progressão, na v0.99**; antes dela, o **Catálogo de entregas, na v0.85** — ela é a peça 17 e tem o `conferir-catalogo.py` em cima dela, com onze checagens; a regra opcional do **Bloquear** continua em `03-mecanica/RASCUNHO-bloqueio.md`). Este arquivo existe para retomar o trabalho — inclusive em conversa nova — sem recontextualizar tudo. Leia ele inteiro antes de mexer em qualquer coisa: ele tem a seção *"Onde estamos, e o que falta"* no fim, que é o ponto de retomada.

**Versão v0.111.** Fases 0 a 3 fechadas; Fase 4 (mecânica) em andamento, **dezenove peças escritas** e **dezenove validadores**.

**A v0.111 mediu o capítulo 9 antes de quebrar e descobriu que ele não precisa ser quebrado** — *o PHB tem dois capítulos acima de `35%` do livro, e o Fundamento é `21%`.* **Tirando os catálogos de consulta, ele tem `10.132` palavras de leitura corrida, praticamente iguais ao capítulo 7.** *O item saiu da fila como não-trabalho.* **E toda entrada do CHANGELOG passou a fechar com `→ Continua em`.**

**A v0.110 fechou a fila da revisão do livro.** *Três exemplos inline, três habilidades com efeitos separados em linha própria, e a confirmação de que o alvo previsto — 38 seções e 6 habilidades — era `3` e `3` na prática.* **Sétimo caso do mesmo erro de contagem, e o padrão está logo acima das pendências.**

**A v0.109 leu as 74 habilidades de Trilha e Caminho uma a uma e achou que `vida temporária` tinha três grafias** — *`Aprumo` e `Crosta` diziam "PV temporário", a Melhoria `Rasga Escudo` dizia "pontos de vida temporários"*, **e as três ficavam de fora da regra que a v0.108 tinha acabado de escrever.** *Unificadas. O `Aterro` também passou a dizer que não depende do `Alicerce`, informação que a fonte já tinha e a transposição perdeu.*

**A v0.108 escreveu a regra de `vida temporária`, que oito efeitos usavam e nenhum documento definia, e passou o livro por uma revisão de vocabulário medida contra o D&D 2024 e o GURPS 4e.** *A regra mora na peça 1 §5.1.1; a revisão do livro está registrada em `05-material/livro/ESTADO-revisao.md`.*

**A v0.107 fechou as duas divergências que a revisão do livro registrou na v0.106 e ninguém tinha investigado, e as duas moravam onde o bilhete não dizia.** *Ele chamou as duas de "bug do sistema, não do livro" e apontou para `03-mecanica/`.* **Uma está lá — a coluna de Passivas da peça 11 §4, errada em duas das três linhas. A outra estava no gerador do manual**, e consertar ela levou o Fundamento para a **v7.11**.

> **⚠⚠ A linha da Classe Passiva 3 daquela coluna dizia `—` — nenhuma Passiva permanente no manual — e o manual lista três.** *`Escama`, `Afinidade` e `Reserva Profunda`, e a `Escama` é da v0.26: a mesma que este documento discute na seção "Marcado para o playtest".* **A coluna existe como PROVA de que a escada de formato foi lida do manual; uma prova que contradiz o que ela cita prova o contrário.** *A linha da 2 também estava curta — cinco de sete.* **Ganhou a checagem `4k` do `conferir-manual.py`, com guarda e contra-teste, e a contagem de checagens não se moveu.**

> **E a regra de ouro nº 5 do Fundamento não estava em `03-mecanica/` nenhum.** *A dona é `manual/gerador/partE.js`, e a tabela publicava "Liberação Máxima custa a rodada inteira, e você só tem as que o nível deu" — **sem o piso de `Classe 3 ou mais`**, que o mesmo manual escreve em outros três lugares.* **Quem lesse só a tabela aprovaria uma Liberação Máxima de Classe 1** — e é a tabela que a seção diz que o checklist do mestre segue "exatamente".

**E o `conferir-ficha.py` voltou a conferir a checagem 3.** *A v0.105 tirou a coluna de ofício da tabela de Caminhos da peça 8 e o regex continuou pedindo seis colunas: ele não casava com nada, e o validador falhava com "nao consegui ler a tabela" — travando o `subir.sh` inteiro.* **O campo `oficio` dos `CAMINHOS` do `dados.js` saiu junto, porque nada no gerador lia ele.**

**A v0.104 é a versão das dez condições no degrau errado.** *A `Condição Menor` e a `Condição Maior` do manual viraram uma Melhoria só, chamada `Condição`, e o preço dela é o **nível** da condição escolhida.* **O espalhamento dentro de um degrau caiu de `17,00×` para `4,26×`, que é o piso de qualquer corte em três degraus** — a busca exaustiva diz que nenhum outro faz melhor, e o filtro do projeto reprova a partir de `3,00×`. *Manual na v7.10, com dois feitiços prontos mudando: `Palma Trovejante` `5d8 → 6d8` e `Vala Comum` `9d8 → 11d8`.*

**E ela pagou a dívida mais velha da peça 13: as cinco vagas de `Desliga` que estavam destravadas desde a v0.59 e a v0.103.** *O que as segurava não era trabalho — era a trava do formato, que proibia encostar em qualquer coisa com preço.* ***Decisão do Mizuki: a trava passou a "apaga o que ninguém comprou, e ENFRAQUECE o que alguém comprou — nunca imunidade"***, com o degrau do relógio saindo do nível da condição. **Sobraram duas vagas, e as duas esperam peça que não existe.**

**A penalidade de arma está escrita**, na peça 19 §6: sem treino, desvantagem na rolagem; sem o requisito de Força, `−3 m` de deslocamento. *As duas somadas custam `33,8` vezes o que a arma entrega — é porta fechada, não preço.* **Três documentos apontavam para ela.**

**A v0.103 escreveu a peça de dano e condições, e a régua que ela existia para ter não precisou ser inventada — ela estava na tabela de custo do manual.** *Vinte e seis lugares em oito documentos esperavam por ela, e metade dela já estava escrita: três seções da peça 1 declaradas, no próprio texto, como guarda provisória.* **Os catorze tipos de dano, a cobertura e as catorze condições mudaram de casa, e a peça 1 ficou com ponteiro.**

> **⚠⚠ E o achado: o `Punho` nunca estourou.** *Aquela Trilha estava publicada em `6,09` de um orçamento de `5,00`, com o estouro de `22%` aceito por decisão dele — e o próprio desenho marcava o `Derrubado` do nível 11 como "não reconstrói de lugar nenhum".* **Ele reconstrói: era o `Derrubado` PERMANENTE, e o texto da entrega escreve dois portões que o preço não lia.** *Com os dois — acertar (`75%`) e o alvo falhar o Teste de Resistência (`45%`) — o degrau vale `0,56` fatia e não `1,71`, e a Trilha fecha em `4,94`.* **Decisão dele: corrigir o preço e deixar assim.**

> **⚠ E quatro decisões de estouro citavam o `Punho` como precedente.** *O `Batedor` nas três rotas, a `Brasa`, a `Torrente` e o `Explosivo`.* **Nenhum número delas se moveu — o que se moveu foi qual precedente elas citam.** *O maior estouro aceito do projeto passa a ser a `Brasa`, entre `41%` e `88%`.*

> **A régua, em uma linha:** até a v0.103 o manual cobrava `Média` por qualquer uma das nove `Condição Menor` e `Pesada` por qualquer uma das cinco `Maior` — **e a conta diz que elas valem de `0,00` a `19,73` fatias, um espalhamento de `17` vezes contra um filtro de dominância que reprova a partir de `3,00`.** *Cada uma ganhou nível — `Leve`, `Média` ou `Pesada` —, e tirar uma custa `1` ponto de energia por nível.* **Na v0.104 as duas Melhorias viraram uma, chamada `Condição`, e o preço dela passou a ser o nível:** *dez das catorze estavam no degrau errado, e o espalhamento caiu de `17,00×` para `4,26×`, que é o piso de qualquer corte em três degraus.*

> **O número pulou de `0.99` para `0.100` e não para `1.00`.** ***Decisão do Mizuki:*** *`1.0` costuma querer dizer pronto para usar, e `04-playtest/` tem zero sessões, o quick-start não existe e faltam três Trilhas.* **O `1.0` fica reservado para quando alguém tiver jogado.**

**A v0.93 fechou três pendências pequenas, e a primeira era grande por dentro.** *As duas entregas em minúscula viraram `Disparo Carregado` e `Acelerar`; o `Classe` solto da peça 11 eram **treze** lugares e não os oito contados; e o `.pdf` do manual saiu da v7.4 para a v7.8 e parou de ser exportado a mão.* **⚠ E o achado: a minúscula do `carregar` não era descuido — `Carregar` sai `OCUPADO` na triagem, é Restrição no manual.** *A pendência ficou catorze versões descrita pelo sintoma, e o sintoma não diz o que precisa ser feito.*

**A v0.92 fechou a `Aptidão Própria`, e com ela o catálogo inteiro: as catorze entradas têm regra, gate e validador.** *Ela estava listada como "falta a régua do `Efeito Próprio`" desde a v0.3.* **⚠⚠ E a régua nunca precisou ser escrita — ela é do manual, está numa tabela de Melhorias, e ninguém tinha aberto:** *"Em quantas cenas por arco isso vai importar? Uma cena: Leve. Metade: Média. Quase toda: Pesada. **Na dúvida, Pesada.**"* **É o terceiro exemplar do mesmo defeito em doze versões** — o Classe 0 da v0.80 e a ação `Mirar` da v0.86 são os outros dois: *o projeto procurando um número que já tinha dono.*

> **E as três faixas caem exatamente nos três degraus da escada de Classe Passiva da §4:** *uma cena/Leve na Classe Passiva 1, metade/Média na 2, quase toda/Pesada na 3.* **A escada da peça mede FORMA e a do manual mede FREQUÊNCIA, e as duas caem nos mesmos três degraus** — condicional dispara pouco, reativo com limite dispara em parte, permanente dispara sempre. *Com isso a trava que já estava escrita ganhou número: `Classe Passiva 1 ou 2, nunca 3` quer dizer que uma `Aptidão Própria` importa em **no máximo metade das cenas** de um arco.*

> **Cinco requisitos, no molde da `Regra Própria` do manual, com um trocado.** *A simetria não veio — ela existe lá porque a `Regra Própria` **impõe uma regra ao mundo**, e uma `Aptidão Própria` só muda o que você faz.* **No lugar entrou "não é atalho": ela não repete uma das treze do catálogo com outro nome nem entrega uma que o seu gate não alcança.** *Sem isso, alguém escreve a `Energia Reversa` com outro nome e pula o gate de refino 7.*

> **O que faz ela sobreviver a sete mesas é uma linha: a ficha carrega a RESPOSTA da pergunta de frequência, e não só o texto.** *E o desempate do manual entra com o sinal a favor da mesa — na dúvida é Classe Passiva 3, e a `Aptidão Própria` não alcança a 3, então **a dúvida reprova a proposta**.* **É o único lugar do sistema em que "não sei" tem resposta escrita, e ela é "não".**

> **⚠ E a checagem do `por cena` da peça 10 acusou na primeira edição, pela segunda vez.** *Escrever a aptidão acrescentou três usos na pasta e a peça publicava `93`.* **De `93` para `96`** — a v0.83 tinha feito o mesmo caminho de `91` para `93`. *Lição nº 1 fazendo o trabalho dela duas vezes.*

**A v0.91 fechou o catálogo de aptidões: a `Barreira Simples` e a `Cortina` eram as duas últimas sem número, e estavam assim desde a v0.3.** ***O Mizuki chegou com o problema pelo nome antes de qualquer conta:*** *"se não vira uma vida extra paia"* — **e a conta concorda.** *Dano evitado converte `1` pra `1`, então uma barreira que o inimigo precisa quebrar **evita a própria vida**: `200` de vida seriam `9,84` fatias numa luta de `3,3` rodadas, contra uma Trilha inteira de `5,00`.*

> **⚠ E gastar a rodada inteira levantando NÃO gateia.** *Era a primeira ideia dele.* **Sobram `2,3` rodadas com a barreira de pé — `70%` da luta — e o câmbio fica a favor de quem levanta: uma rodada sua no nível 30 vale `108` de dano e você a troca por uma barreira que absorve `200`.** *O que gateia é `1 minuto`, que são dez rodadas contra `3,3`.* **E ele resolve de graça o problema multi-mestre: uma regra do tipo "não dá para levantar em combate" obriga sete mesas a decidirem o que é estar em combate.**

> **`Barreira Simples`, sem gate:** domo de raio `6 m`, ancorado no lugar, bloqueia passagem e linha de efeito, **`5 × refino` de vida** — abaixo dos `70` da maior parede que um feitiço monta, de propósito. **`Cortina`:** cobre um lugar, esconde de quem não é feiticeiro, carrega **uma condição sobre quem atravessa**, **`20 × refino` de vida**. *As duas caem quando você fica `Inconsciente`, que é da obra e encaixa no que a v0.88 renomeou.*

> **⚠⚠ E entrou o QUINTO formato de gate, que a v0.90 tinha recusado uma versão antes.** ***Decisão do Mizuki: a `Cortina` exige a `Barreira Simples`, e nada mais*** — *"só isso já força a gastar dois marcos aqui"*. **A diferença precisou ser escrita: no kokusen as três são alternativas e o requisito seria pedágio; aqui a `Cortina` é a `Barreira Simples` maior, e isso é escada.** *A regra: a aptidão exigida tem de ser a mesma coisa em tamanho menor e servir sozinha.* **E ele é o único dos cinco formatos que cobra MARCO** — nível o tempo paga, refino a linha passiva paga, Origem a criação paga.

> **O extrator de gate da v0.90 tinha um buraco que o formato novo abriu:** *`exige a Barreira Simples` não produzia token nenhum dos dois lados, e a comparação título-contra-catálogo passava **trivialmente**.* **Um formato de gate inteiro sem ninguém conferindo as duas cópias.** *Corrigido, com a guarda de contagem subindo de onze para treze.*

**A v0.90 fechou a terceira de kokusen, que virou a `Kokusen Constante`.** *Ela era contada entre as onze fechadas com o gate escrito como **a definir** e sem nome nenhum.* **E indo fechar ela apareceu um buraco: ninguém tinha escrito se as três de kokusen empilham** — procurado nas dezessete peças e nos três desenhos, zero ocorrências. ***Decisão do Mizuki: empilham.*** **A `Constante` sobe a base para `3 × refino` e a vantagem da `Melhorado` rola em cima dela — `51%` no d100 no refino 10, contra `36%` só com a `Melhorado`.** *Sem empilhar, a terceira seria `17%` pior pelo mesmo preço de um marco: entrada morta ocupando vaga.* **Nenhuma exige a outra**, porque criar um gate de *"ter pego a de antes"* seria o quinto formato — e foi uma pergunta de leitor dele, na v0.65, que derrubou uma mecânica inteira exatamente por isso.

> **O gate é `refino 5`, sem gate de nível, e ele é derivado.** *Assim ela abre no nível 10 para quem sempre escolhe Refino, e a `Melhorado` só no 14 — **quatro níveis em que ela é a única das duas disponíveis**.* **Sem isso ela nunca compensaria escolher:** quem pode pegar ela já pode pegar a `Melhorado`, que ganha em todo refino. *`Pleno` foi recusado fora da triagem, tendo saído `LIVRE`: ele entra no campo de `Liberação Máxima` e `Técnica Máxima`.*

> **⚠ E a trava do kokusen media a ENTRADA enquanto a peça fala da FICHA.** *Com as três empilhadas a ficha chega a `+4,64%` de dano por rodada — `0,46×` um ponto de atributo —, e a trava velha só olhava a base em `0,18×`.* **A comparação certa é POR MARCO: a pilha custa três marcos, e três marcos de `Corpo` comprariam `+30%` — `6,5×` mais.** *Continua sendo escolha pelo grito e não pela planilha.*

> **⚠ E a checagem do gate duplicado só olhava UMA das catorze entradas.** *O gate mora no título da seção e na linha do catálogo; a comparação estava escrita no braço para a `Energia Reversa`.* **Perturbando o gate da `Constante` no catálogo, o validador saía verde — treze das catorze não tinham ninguém comparando.** *Generalizada para as onze que têm seção própria, de mão única e com guarda de contagem.*

> **O catálogo passou de nove entradas escritas com número para dez, e a rota pura de Refino da v0.89 pede exatamente dez.** *Ela fecha sem folga nenhuma até `Barreira Simples` e `Cortina` entrarem.*

**A v0.89 fechou a troca do marco, que era o único problema de design que tinha sobrado.** *A escolha de `Refino` promete **"mais um de refino, e uma aptidão"** e entregava só a aptidão nos marcos 22, 26 e 30.* **A causa medida: a linha de graça do marco entrega `8` dos `10` de refino sozinha** — sete marcos a `+1` mais o refino 1 do começo —, **então a metade "mais um de refino" da escolha só tem `2` pontos de espaço para caber na campanha inteira.** *Quem escolhe `Refino` nos sete pagaria `15` e para em `10`.* ***Decisão do Mizuki: no teto, a escolha leva DUAS aptidões*** — a rota pura vai de `7` para `10`. **E os outros dois eixos não desperdiçam nada:** o `Corpo` ganha `14` pontos contra um teto somado de `30` nos cinco atributos, e o teto de Passivas do `Leque` sobe uma vaga por escolha.

> **A forma da comparação não muda, e é isso que fecha.** *Cortando o par aptidão/Passiva dos dois lados, o marco sempre compara `+1` atributo contra alguma coisa contra `+1` feitiço.* **Antes do teto essa alguma coisa é `+1` de refino; a partir dele é uma aptidão a mais.** *A régua de "uma aptidão a mais" continua não existindo — o que muda é que esta comparação não depende dela, porque quem leva a segunda já escolheu esse eixo cinco vezes.*

> **⚠⚠ E as duas alternativas foram medidas e reprovaram, com a conta escrita.** *Subir o teto de `10` para `15` acende **dois contratos** na hora: a proteção de `cobrir-se` passa a crescer `+33` contra `+3` de um atributo, e o kokusen sobe a `9,1%` de dano por rodada. Mais `31` fórmulas usando refino como variável em sete arquivos.* **Baixar o refino passivo move a tabela de gates inteira do §5.**

> **A checagem 5.2 é a segunda metade da 5 por outro eixo.** *A 5 mede o FIM da campanha e saía verde com o meio quebrado — nos totais a rota de `Refino` liderava o refino com `10` contra `8`.* **A 5.2 mede marco a marco, e as componentes são QUATRO e não cinco:** aptidão e Passiva entram na mesma, que é o que a peça 11 afirma. ***Contra-teste: rodando a regressão com as duas separadas, ela sai verde*** — é por isso que ninguém viu isto em dezessete versões.

> **E o Classe 0 fantasma sobreviveu num validador por ser só impresso.** *O `conferir-aptidoes.py` carregava `CLASSE_0 = 4.5`, o número que a v0.80 matou em todo o resto do projeto.* **A coluna dizia `35%` da Rotina no nível 2 quando é `69%`.** *Agora sai da tabela do manual, como cópia vigiada.* **Display errado ensina número errado do mesmo jeito.**

**A v0.88 fechou quatro dívidas antigas de uma vez, e a mais velha delas não era o que estava escrito.** *A troca de `Caído` por `Inconsciente` estava marcada desde a v0.82 como colisão entre o estado de 0 de vida e a condição de quem foi derrubado — e a condição de derrubado **já tinha nome no manual: `Derrubado`**, com tier de preço e dois feitiços prontos usando ela.* **O único lugar do projeto que a chamava de `Caído` era a Manha `Abalo`, e isso era REGRESSÃO:** a v0.74 já tinha achado e fechado exatamente essa colisão no `Punho`, e oito versões depois ela voltou por outra porta. **O `Abalo` passa a aplicar o `Derrubado`, e o estado de 0 de vida virou `Inconsciente` em onze lugares**, aplicando a decisão do Mizuki de três versões atrás. *Nenhum número se moveu.*

> **⚠⚠ E o que deixou isso acontecer é buraco de validador: a triagem era cega para as doze condições do manual.** *Elas moram dentro de uma frase de prosa — `"Aplica uma: …"` — e a extração do `conferir-nomes.py` lê primeira coluna de tabela.* **Onze das doze voltavam `LIVRE`**, e a única que não voltava era `Lento`, por acidente, porque ela também é Restrição. ***O exemplar mais constrangedor é o `Incapacitado`: ele saía `LIVRE` enquanto a peça 1 §5.5 gastava um bullet explicando que ele é condição nomeada do manual.*** **Agora as doze são lidas do `.docx`, com guarda de contagem.**

> **E a peça 6 parou de publicar duas coisas erradas.** *O `Repertório` — Trilha abandonada na v0.81 — ainda estava na §2, e ele sobreviveu em **sete** lugares e não em três: a peça, a **ficha do gerador**, dois validadores, o rascunho de Trilhas, a nota histórica da peça 5 que dava o motivo errado, e três pendências do desenho escritas como abertas.* **O nome ficou `LIVRE` de novo, de propósito.** *E o §9 publicava o calendário de Caminho `7 · 15 · 23 · 29` como fato fechado, dezoito versões depois de ele virar `2 · 7 · 15 · 30`.* **A citação histórica do §3.1 NÃO foi apagada — ganhou a linha que diz que foi superada.**

> **`Quick Draw` virou `Descarga`, e o sistema não tem mais nenhum nome em inglês.** *Decisão do Mizuki entre quatro candidatos que passaram na triagem; `Rajada` e `Estopim` morreram nela antes, e `Pente` morreu por sentido depois de sair `LIVRE`.* **A escada da rota `Arma de Fogo` fica `Ferrolho` · `Mirar` · `Descarga` · `Dobro`.**

> **Duas checagens novas, e dez perturbações conferidas em cópia isolada.** *A checagem 10 do `conferir-catalogo.py` compara toda cópia viva do calendário de Caminho contra o `DESENHO-caminhos.md`, que é o dono, **e em dois eixos**: uma pergunta se o valor bate, a outra se o valor morto sumiu. E ela tem guarda de contagem, porque checagem que para de conferir em silêncio é a lição nº 8 por outra porta.* **A triagem ganhou o veredito `MORTO`**, que não mata o candidato — o projeto reaproveita nome de propósito — mas impede reaproveitar sem saber.

**A v0.86 escreveu a ação `Mirar`, que era entregue em SEIS degraus do `Batedor` e não tinha regra em lugar nenhum.** *Ela atravessou da v0.74 à v0.85 assim — treze menções no desenho, todas concedendo, nenhuma definindo —, e quem achou foi o `conferir-catalogo.py` da versão anterior, indexando os degraus que a citam.* ***Decisão do Mizuki:*** **Ação Bônus, vantagem no próximo tiro com arma de projétil, e só se você não se deslocou nesta rodada nem vai se deslocar.** *É a forma do `Steady Aim` do Ladino do 5e; as duas outras formas comuns já estavam gastas aqui — consertar a penalidade de faixa de alcance é o nível 2 das três rotas, e mexer em cobertura não dá, porque **cobertura não existe como regra** neste sistema.*

> **⚠ Ela estoura o degrau em `5,3×`, e o estouro é decisão dele.** *Vantagem em um dos dois ataques vale `27,00` de dano na rodada; abrir mão do deslocamento de `9 m` devolve `5,40`; sobram **`4,25` fatias num degrau de `0,80`**.* **O gate de movimento corta `20%` do preço — não é decorativo, mas vantagem é o número mais caro do sistema.** ***"Você tá inflando demais essa habilidade, garanto para você"*** — *a mesma frase que segurou a `Brasa` na v0.81.* **Nenhum número publicado se moveu.**

> **E ele cria três dominâncias novas, declaradas.** *Com o atirador parado em metade das rodadas, as três rotas vão de `4,52`–`4,82` para **`5,95`–`6,09`** contra um teto de `5,00` — `+19%` a `+22%`, que é **exatamente o tamanho do `Punho`**.* **As três passam a dominar a `Estocada` por `1,19×` a `1,21×`**, mesmo tamanho da dominância `Explosivo` sobre `Torrente` que já estava aceita, e dentro do filtro de `3,00×`. *Ninguém domina o `Executor`, que é o único com coluna de defesa, e as três rotas não se dominam entre si.*

> **⚠ E entrou a TERCEIRA taxa sem medida do `Batedor`: em quantas rodadas o atirador fica parado.** *As outras duas já estavam declaradas — faixa longa e colado.* **Esta sozinha decide `2,12` fatias:** a `100%` as três rotas vão a `8,07`–`8,21` e a dominância sobe para `1,64×`.
>
> ***Decisão do Mizuki na v0.103: ela sai da fila de perguntas.*** *A taxa fica declarada onde ela mora — no desenho de Trilhas, junto das outras duas —, com o tamanho escrito, e não é pergunta que o projeto faça a ninguém.* **Quem responde é a mesa, e `04-playtest/` está vazia.**

**A v0.85 deu dono à contagem, e o primeiro validador do projeto passou a LER OS `DESENHO-*.md`.** *Até aqui nenhum alcançava aqueles três arquivos, e é por isso que o nível 27 da `Estocada` passou três versões com a tabela cobrando `1,33` fatia e o bloco de regra entregando `5,31`.* **A peça 17 é um índice: quantas entradas existem, como cada uma se chama, onde o texto dela mora — e nada mais.** *Ela não guarda preço e não guarda texto de mesa; os dois continuam sendo dos desenhos, que são os donos.* ***Decisão do Mizuki: rota de Trilha conta como entrada própria e menu dentro de degrau não conta*** — então o `Batedor` entra com `12` e a `Pegada` do `Executor` e a `Sintonia` do Evocador entram com `4` cada. **Com a regra escrita a contagem virou `89` e não `81`, e os nomes que faltam viraram `21` e não `17`.** *As quatro a mais estavam escondidas dentro de uma linha só do `Batedor`.*

> **A checagem 6 é a que a peça existe para ter:** um bloco de regra não pode prometer permanência onde a linha de preço cobrou condição. **Oito perturbações conferidas em cópia isolada**, com a base passando antes e o `diff` conferido em cada uma — e a que mais importa é a regressão da `Estocada`, que acende. *As checagens 5 e 6 se medem por eixos diferentes de propósito: apagar o bloco acende a 5, reescrever o bloco acende a 6.*

> **E o índice rendeu um buraco antes de existir: a ação `Mirar` não tem regra em lugar nenhum.** *Ela é entregue no nível 11 das três rotas do `Batedor` e estendida no 27 das três — seis degraus, entre `1,60` e `2,04` fatias cada.* **Nem a lista de ações da peça 3 §3.1 nem o desenho dizem o que ela faz ou que slot ela gasta.** *E a triagem devolve o nome como `fraco`: ele está a uma letra de `Mira`, que é Família no manual.* **É buraco de regra, e não de nome.**

**A v0.84 escreveu as doze entregas do Guia em texto de mesa e batizou mais sete do Emanador.** *O Guia era o único Caminho sem uma entrega jogável — as doze existiam só como linha da tabela de preço — e virou o único com os três completos.* **`Elo`: `Nó` · `Repasse` · `Partilha` · `Trança`. `Sutura`: `Agulha` · `Enxerto` · `Pulso` · `Cerzido`. `Perímetro`: `Chão` · `Sentinela` · `Encalço` · `Portão`.** ***Decisão do Mizuki: tirar condição custa `1` PE por nível dela*** — a regra preça pelo nível, então ela não depende da lista de condições que não existe, e a exaustão da peça 10 já tem três degraus numerados. **De 48 entregas de Trilha, `11` tinham nome e agora são `30`; faltam `17`.**

> **⚠⚠ E uma Trilha estava entregando `4×` o preço dela.** *O nível 27 da `Estocada` tinha a tabela com dois gates (`1,33` fatia) e o **bloco de regra** dizendo "carrega **sempre** um Classe 0" (`5,31` fatias — mais que a Trilha inteira).* **A v0.81 repreçou e consertou só a tabela, e a mesa lê o bloco.** *`Torrente`, `Brasa` e `Explosivo` foram varridas junto e as três batem.* **Nenhum validador alcança os `DESENHO-*.md`, e é por isso que ela passou três versões assim.**

**A v0.83 deu casa à lista de ações: ela é a peça 3 §3.1.** *Aquela peça tinha os quatro slots do turno e nenhuma ação nomeada, e o `Ajudar` morava na peça 4 §5 sem custo de ação declarado desde a v0.22.* **As doze do 5e de 2024 foram lidas na fonte** — oito já existiam aqui, entraram `Influenciar` (que cabe sem adaptação, porque **Essência é o Carisma deste sistema**) e `Preparar`, e o `Search` e o `Study` viraram `Vasculhar` e `Estudar`. ***Decisão do Mizuki: o `Ler o Ambiente` fala do LUGAR e nunca de criatura, e os outros dois falam da criatura*** — sem essa linha uma Ação Bônus dominava duas Ações Padrão. **`Agarrar` e `Derrubar` deixaram de ser ação própria e viraram opção do `Atacar`**, como no 2024, porque como ação própria elas ficavam mortas. **Cinco checagens novas no `conferir-acao.py`, com oito perturbações conferidas.**

**A v0.82 fechou a dívida de linha de base que a v0.81 marcou com `⚠⚠ LIMPAR ANTES DO PDF`, e ela NUNCA FOI DÍVIDA.** *Era uma frase que ninguém tinha escrito, e a própria peça 6 §3.1 já registrava a resposta como "anotado, não decidido".* **O ataque extra do nível 7 é um golpe SOLTO por rodada e não exige a Ação de Atacar** — ele acontece junto do que a Ação Padrão fez, inclusive quando ela conjurou. ***Achado do Mizuki, e por pergunta e não por conta:*** *"já é um ataque extra, é uma mecânica forte, não acho que precisa disso."* **Zero número se moveu:** o vão continua `9 · 10 · 11 · 12`, o nível 7 continua de graça nos cinco Caminhos, e o `Arremate` e o `Resquício` continuam como estavam.

> **A alternativa reprova por DOMINÂNCIA e não por orçamento**, e é isso que fecha o argumento. Com o ataque extra preso à Ação de Atacar, **dois golpes rendem `23` no nível 30 e um Classe 0 grátis rende `27`** — a entrega de nível 7 de dois Caminhos perderia para o botão que toda ficha já tem, ninguém usaria a Ação de Atacar, e o físico e o conjurador terminariam idênticos em `60,50` por rodada. **A checagem `4h` do `conferir-manual.py` guarda a FORMA, com sete perturbações; a `4f` guarda o número.**

**E as TREZE MANHAS entraram, fechando o nível 2 da Vanguarda** — o `DESENHO-manhas.md` na raiz. *A régua veio antes do catálogo e reprovou sete das oito propriedades de maestria do 5e de 2024: `+1` no acerto vale `10,80` de dano por rodada aqui, então vantagem vale `54,00` contra um degrau de uma fatia.* **As treze caem entre `0,68` e `1,18` fatia, dominância `1,74×`.** **O Evocador saiu da fila** — o §6 do `RASCUNHO-trilhas.md` tem cabeçalho de parada, e ele **não** foi para o `99-arquivo/` porque nada ali morreu.

**A v0.81 fechou os dois avisos que a v0.80 deixou na régua de Trilhas, e a resposta dos dois é "não muda nada, e agora dá para provar".** *O vão corrigido não move o preço de nenhuma das onze Trilhas fechadas — o ponto de chegada é o mesmo (`99 + 7` e `94 + 12` dão os mesmos `106`), e o que mudou foi o tamanho do degrau de graça.* **E o teto que morreu não tem substituto: as outras quatro travas não reprovam em orçamento nenhum de `1×` a `8×`, e os três candidatos testados ou têm dono no playtest ou só acendem a `10,45×`.** ***Decisão do Mizuki: o teto fica declarado como decisão de design — `4×`, que é `27,7%` da ficha para a camada — em vez de vestido de conta.*** *O `+18%`, como contra-teste, reprovaria a partir de `3×`: existia teto, era ele, e era o único.*

**E o Classe 0 fantasma tinha sobrado num lugar que a guarda da v0.80 não alcançava.** *A peça 6 §5 preçava um Classe 0 em `4,50` para justificar o PE do Bastião, e o argumento **inverte** com a tabela certa — um Classe 0 rende `27` no nível 30 contra `12` do golpe simples.* **A guarda daquela versão tinha um buraco de uma linha: ela lia `**negrito**` como nota histórica, porque negrito começa com `*`.** *Hoje `>` e `*` sozinho são história e `**` é afirmação viva, mais a checagem **4g**, que guarda o número morto e não só a frase morta — sete perturbações conferidas, e a base pegou uma cópia suja na primeira tentativa.*

> **Um achado de graça: o modelo de combate do manual reconstrói.** A coluna *dano do grupo por rodada* da tabela de inimigo é **`2,90 ×` a Rotina** nas seis linhas, e com isso o modelo reproduz os `3,7` e os `2,7` rodadas que a v0.73 publicou, com zero parâmetro livre. **Ele produz a primeira pergunta de mesa deste orçamento com número em cima:** no orçamento de hoje o chefe deixa de conseguir derrubar a ficha mais frágil concentrando fogo, e a virada é entre `2×` e `3×`.

**E indo consertar as pendências pequenas, a v0.81 achou que CINCO entregas publicadas foram calculadas a partir do Classe 0 fantasma.** *A v0.80 corrigiu a tabela e repreçou só o `Arremate`; as outras foram calculadas **a partir** do `4,50` e nunca refeitas.* **As três Trilhas foram repreçadas com o Mizuki: `Torrente` de `5,37` para `4,65`, `Estocada` de `4,58` para `5,02`, e `Brasa` de `5,03` para uma faixa de `7,06` a `9,42` — com o estouro aceito e declarado, no molde do `Punho`.** *As três matrizes continuam limpas.*

> **A regra nova que sai daí, e ela é do sistema:** um Classe 0 causa `27` no nível 30 e a fatia é `5,08`, então **"ganha um Classe 0 por rodada" vale `5,31` fatias contra um orçamento de Trilha de `5,00`.** *Nenhuma entrega pode conceder isso sem relógio ou gate.* **E no nível 30 um Classe 0 e um Classe 2 num alvo causam os dois `27`** — toda entrega que "sobe o Classe 0 para Classe 2" vale zero em dano onde a fatia mede.

**E o buraco de texto mais caro que a v0.80 deixou aberto FECHOU.** *Decisão do Mizuki: **a Ação de Atacar não inclui o feitiço de Toque** — canalizar e atacar são ações diferentes e não cabem no mesmo turno, e a `Fornalha` é a única exceção.* **Está escrito na peça 6 §3.1, com a tabela dos três turnos.** *Ele valia um fator de `2,6×` na `Brasa`, e a resposta veio da mesa e não da conta — que é exatamente o que a v0.80 previu.*

**A v0.80 é uma versão de conserto, e o conserto é de linha de base.** *O projeto preçava um feitiço de **Classe 0** em `4,50` de dano desde a v0.14, e esse número não existe no manual.* **O manual tem tabela própria para ele — `2d8 · 3d8 · 4d8 · 5d8 · 6d8` por faixa de nível, então `27` no nível 30 —, e nenhum documento do projeto e nenhum validador abriam ela.** *Ela era a **quarta** tabela compartilhada com o manual e a única sem dono declarado; hoje o dono é o manual.* **O estrago estava na coluna "conjurador" da peça 6 §3, que saía `5` pontos alta em todo nível**, e com ela o **vão `físico − conjurador`** — que paga o degrau do nível 7 dos cinco Caminhos. **O vão passou de `4 · 5 · 6 · 7` para `9 · 10 · 11 · 12`, e ele é exatamente um golpe simples.** *Efeito colateral bom: os cinco Caminhos passam a receber a mesma coisa no nível 7 — antes Bastião e Vanguarda ganhavam `11,50` e os outros três `7,00`.* **E a frase que explicava a Rotina — *"ela já é feitiço + Classe 0"* — é falsa: a Rotina é `floor(3,5 × Classe)` dados, o meio exato entre bater num alvo e espalhar, e ela fecha nas sete Classes.** *Duas checagens novas no `conferir-manual.py` (4e e 4f) com seis perturbações conferidas.*

**A permissão do `Arremate` foi APLICADA na v0.80** — a peça 6 §3.1 deixou de proibir três rolagens de ataque, com o motivo do Mizuki escrito e o número da vida junto (o Emanador tem `212` no nível 30 contra `243` da Vanguarda e `305` do Bastião). **O `Coro` herda, e nele custa `0%` em dano.** *E medindo nível a nível apareceu que o pior nível é o **11**, com `+20%` sobre o físico, e não o 30 com `+11%`.* **O nível 7 do Emanador foi refeito: a `Voz Grossa` morreu e virou o `Resquício`** — um Classe 0 na Ação Bônus quando a Padrão foi feitiço que não causa dano. *Ela morreu porque rebaixava o Classe 0 de `27` para `12`, e porque não existia na rodada em que o Emanador conjura.* **O `Arremate` repreçou para `3,74` de `5,00` e o nível 27 dele ficou VAGO, com `1,26` fatia.**

**DOZE Trilhas escritas de quinze, e o EMANADOR FECHOU na v0.81 — faltam só as três do Evocador.** *A terceira do Emanador é o **`Explosivo`**, em `5,57` de `5,00`: rerrolar `1` e `2` nos dados quando o feitiço for o único da rodada, somar o atributo no dano, gastar `a Classe` em PE por vantagem no ataque, e `+metade da Classe` em dados `1×` por cena.* **O `Repertório` foi ABANDONADO** — a ficção dele só se preçava por *"uma aptidão a mais"*, e essa régua não existe nem pode existir; e as duas colunas vazias do Caminho não aguentam uma Trilha inteira. ***Declarado: o `Explosivo` domina a `Torrente` por `1,20×`, e a causa é falta de coluna e não sobra de número.*** **A Vanguarda fechou na v0.76 e a matriz dela na v0.77; o GUIA fechou inteiro na v0.77** — Caminho preçado contra as três fatias e as três Trilhas em `4,78` · `4,51` · `4,74`, com matriz limpa. *A matriz da Vanguarda entra com **cinco** linhas e não três, porque as três rotas do `Batedor` são três fichas diferentes, e ela sai limpa: a única dominância é a `Arma de Fogo` sobre a `Estocada`, aceita e declarada desde a v0.75.* *E a régua de PV temporário fechou na v0.76: **`1` de PV temporário = `1` de dano evitado**, e o mesmo vale para resistência e redução — a conversão de PONTO do manual (`3` por ponto) é a moeda de montar feitiço e não serve para preçar entrega de Trilha.* **O soco tem dado, dono e validador desde a v0.74** — `d4 · d6 · d8 · d10` pela maestria, sem categoria e sem propriedade, na **peça 14 §5.0.6**; e os **catorze tipos de dano** estavam em guarda provisória na peça 1 até a peça de dano e condições existir — **desde a v0.103 eles são a seção 4 da peça 19**. **A régua de Trilhas mora no `03-mecanica/RASCUNHO-trilhas.md` §3, fechou na v0.61 e foi REFORMULADA na v0.68** — o preço saiu da entrega e foi para a Trilha inteira, e cada entrada passou a declarar a taxa de disparo. *A v0.62 fechou a dívida que ela destampou (**"cena" tem definição**, na peça 10 §5, com validador em cima), e a **v0.63 fechou a Q6 de Invocações** — a peça 15 não deve mais nada.* Manual do Fundamento na **v7.8**, com a Expansão de Domínio escrita, e o catálogo de aptidões **fechado, com as catorze entradas** — a **`Energia Reversa` fechou na v0.78**, na seção 6 daquela peça. **Dá para montar uma ficha de nível 2, jogar uma missão inteira e recuperar entre elas** — por seis das nove rotas de Origem, e agora sem nenhum buraco de regra que morda nessa faixa.

## Como retomar

Leia nesta ordem: este arquivo → `../logs/CHANGELOG.md` (de cima para baixo, a entrada do topo é a mais recente) → a peça de `03-mecanica/` que for mexer. O CHANGELOG carrega o **porquê** de cada decisão, que é o que não dá para reconstruir sozinho.

Antes de mexer em número, rode os validadores. Eles falham alto se algo quebrar.

```
cd 03-mecanica
python3 conferir-atributos.py     # acerto, defesa, TR, perícia, vida, PE máximo, deriva
python3 conferir-acao.py          # régua das Restrições, dominância, Adianta
python3 conferir-pericias.py      # quadro de perícias, listas de Caminho e Origem, colisão
python3 conferir-descanso.py      # piso, exaustão, arredondamento, magnitude, empilhamento, relógios
python3 conferir-nomes.py         # todo nome batizado, projeto → manual
python3 conferir-manual.py        # vocabulário e números importados, manual → projeto
python3 conferir-aptidoes.py      # a trava do refino, as três rotas do marco, o kokusen
python3 conferir-expansao.py      # os gates da Expansão, a ordem, o preço em espaços
python3 conferir-orcamento.py     # o somatório: todos os drenos de PE ao mesmo tempo
python3 conferir-xp.py           # a curva, o abismo que fecha, e os alvos da Guilda
python3 conferir-equipamento.py  # o fundo de cada arma, a dominancia, o teto de Defesa
python3 conferir-criacao.py      # a ficha de exemplo contra as fórmulas, e o que a criação cita
python3 conferir-ficha.py        # a ficha de 05-material contra os catálogos das peças
python3 conferir-legados.py      # os três formatos, a cota de Desliga, as vagas e os totais
python3 conferir-invocacoes.py   # o teto somado, o catálogo, a régua, a morte e o orçamento
python3 conferir-ferramenta.py   # o fundo, o gate herdado, a escada de grau, o teto na ficha
python3 conferir-catalogo.py     # o índice das 89 entradas contra os três DESENHO da raiz
python3 conferir-progressao.py   # as nove colunas da tabela de progressão contra os donos
python3 conferir-dano.py         # a régua de condição, as catorze, os tipos de dano e a cobertura
```

**Três naturezas diferentes, e vale saber qual é qual.** Onze conferem **regra** — *a fórmula deriva certo?*. *(O `conferir-equipamento.py` faltava nesta lista desde a v0.48 e entrou na v0.58 — o `subir.sh` sempre o rodou, porque varre por glob; quem rodasse à mão pelo documento rodava um a menos.)* O `conferir-criacao.py` confere **instância** — *a ficha publicada na peça 8 obedece à fórmula?* —, e nasceu na v0.34 porque os dois erros daquela versão passaram por baixo de todos os outros: a peça 8 é a única que produz uma ficha inteira, e ela envelhece toda vez que outra peça mexe num número. O `conferir-ficha.py` confere **material**, que é a cópia que vira personagem em sete mesas. E o `conferir-legados.py`, o décimo terceiro, confere **catálogo**: ele recalcula a tabela de totais da peça 13 e falha se o escrito não bater com o contado. O `conferir-invocacoes.py`, que entrou na v0.58, faz as quatro naturezas de uma vez — regra, catálogo, instância e **busca exaustiva** —, porque a peça 15 é máquina de construção e não lista.

O quinto tem um modo de triagem, para rodar **antes** de batizar qualquer coisa:

```
python3 conferir-nomes.py --candidatos Vulto Matilha Bigorna
```

**O sexto entrou na v0.26 e olha a direção que faltava.** O `conferir-nomes` pergunta *"esse nome que eu batizei já significa alguma coisa no manual?"*; o `conferir-manual` pergunta *"o manual usa alguma palavra que este sistema não tem?"*. Foi por não existir que o `Bônus de Treinamento` e o `Habilidade/Sabedoria` sobreviveram tanto tempo. Ele também confere que a **tabela de PE, a de inimigo e a coluna Rotina** — que estão copiadas dentro das peças e dos outros validadores — continuam batendo com o `.docx`.

**CINCO precisam de `python-docx`** — `conferir-dano`, `conferir-manual`, `conferir-nomes`, `conferir-pericias` e `conferir-progressao` —; sem ele eles **pulam** as checagens que leem o manual, em vez de falhar, e saem com código 0.

| validador | pula | de quantas | o rodapé avisa? |
|---|---|---|---|
| `conferir-dano` | 1 — as catorze contra o manual | 10 | **sim** — `OK, mas 1 checagem(ns) PULARAM` |
| `conferir-manual` | **4 — todas.** Sai no `except ImportError` antes da primeira | 4 | avisa, e sai antes do rodapé |
| `conferir-nomes` | 3 (as checagens 1, 3 e 4) | 5 | sim, **desde a v0.101** |
| `conferir-pericias` | 1 (a que bate contra o Fundamento) | 8 | sim, **desde a v0.101** |
| `conferir-progressao` | 1 (a checagem 7) | 8 | **sim** |

> **⚠ Eram três até a v0.96, e viraram cinco sem ninguém subir a contagem.** *O `conferir-atributos` entrou na v0.97, quando o caminho de pulada dele foi consertado, e o `conferir-progressao` entrou na v0.99 junto com a peça 18.* **Lido do código e conferido bloqueando o import.** *O `README` dizia três num parágrafo e **dois** no comentário do `pip install`, nove linhas acima — duas cópias, duas respostas, dentro do arquivo que publica a lição nº 9.*

> *Até a v0.39 esta linha dizia "os dois últimos" e "4, 2 e 1", e nenhuma das duas coisas era verdade.* São três, não dois, e eles não são os últimos da lista. E o `conferir-manual.py` estava escrito como o que pula menos quando é o único que **não confere absolutamente nada** sem a biblioteca: ele sai no `except ImportError` antes da primeira checagem. **Número documentado a partir da saída do programa, e não do código, envelhece assim.**

> **O que mudou na v0.38:** rodar de outro diretório **não** faz mais ninguém pular checagem. Os cinco que abrem arquivo do manual resolvem por `__file__`, e de `/tmp` a saída sai idêntica com zero puladas. O `README` e o `LEIA-ME` diziam o contrário desde a v0.28 e foram corrigidos. **Continue rodando de `03-mecanica/`** — o `subir.sh` faz assim —, mas o motivo agora é hábito e não defeito. **A pulada que sobrou é a do `python-docx`, e essa é real.**

## As sete skills, e onde elas moram

**Procedimento:** `rpg-da-guilda` · `pesquisa-antes-de-propor`
**Assunto:** `design-mecanicas-rpg` · `balanceamento-simulacao` · `playtesting-rpg` · `redacao-acessivel-rpg`
**Sobre a conversa:** `gasto-de-modelo` — o veredito de uma linha sobre que modelo a tarefa pedia

Estão na conta e disparam sozinhas. A **`rpg-da-guilda`** entrou na v0.37: ordem de leitura, de onde rodar os validadores, o que a triagem de nomes não pega, como escrever arquivo neste mount, o arnês de perturbação e como fechar versão.

A **`pesquisa-antes-de-propor`** entrou na v0.38, e ela existe por um defeito medido: *a linha "pesquise antes de inventar" já estava na `rpg-da-guilda`, enterrada num bullet de uma lista de oito, e não disparava.* Ela troca o lembrete por **gatilho** — sete casos em que a busca externa é obrigatória antes de entregar — e traz junto a metade que ninguém escreve: **o que não se pesquisa fora.** Número que um documento do projeto é dono se lê do dono; buscar fora cria a segunda fonte, que é a lição nº 9 entrando por outra porta.

As duas guardam **procedimento e nunca conteúdo** — apontam para o `README.md` em vez de copiar as lições.

**A pasta `sistema/skills/` é cópia de trabalho — editar lá não altera a skill instalada**, e as duas divergem sozinhas. **Ao mudar uma skill, mude nos dois lados** — nenhum validador alcança essa camada.

> **E na v0.40 a migração de conta provou que isso não é aviso teórico: as cinco que estavam instaladas divergiam, todas.** A `rpg-da-guilda` instalada ainda carregava o aviso que a v0.38 aposentou — *"rodados de outro lugar eles pulam checagem em silêncio"* —, que é justamente o motivo errado que aquela versão saiu para tirar de circulação.
>
> **E a deriva mudou de direção.** Na v0.37 o repositório é que estava atrás da instalada, e a conclusão registrada foi *"migrar pelo repositório levaria o gatilho velho"*. Desta vez foi o contrário, nas cinco. **Não existe um lado que seja confiável por natureza** — o que existe é a data da última vez que alguém sincronizou, e ela não está escrita em lugar nenhum.

> **E a v0.93 mediu a deriva se separando por CAMADA, o que nenhuma das anteriores tinha visto.** A instalada estava na frente **só na descrição** — seis das sete ganharam uma frase de fronteira mandando mesa e lore para a `mizuki-copiloto-do-mestre` —, e a pasta estava na frente **só no corpo**, em quatro das sete. *Nenhum dos dois lados estava velho por inteiro; cada um era dono de uma metade do arquivo.* **A regra do merge saiu disso e é mecânica: corpo da pasta, descrição da instalada.**
>
> **E a `rpg-da-guilda` da pasta carregava dois pontos cru no YAML da descrição** — `nesse repositório: escrever` —, que um parser estrito recusa. *A instalada já tinha o conserto, com vírgula e aspas.* **O carregador de verdade aceita os dois**, então era risco adormecido e não defeito vivo; ficou com aspas nas duas.

> **E a v0.66 viu os dois sentidos ao mesmo tempo.** A `rpg-da-guilda` instalada estava **39 linhas atrás da pasta** — sem o caminho de commit e sem a seção de como falar com o Mizuki, as duas fechadas com *"aplicada nos dois lados"* —, enquanto as de assunto estavam empatadas com a pasta e as duas atrás do CHANGELOG. **Não é uma direção de deriva; são duas, e elas convivem.**

**⚠ E um defeito que não é deriva — mas ele ACABOU na v0.93, e o parágrafo fica porque o motivo dele continua valendo.** *Medido de novo: as seis pastas de apoio estão instaladas e batem byte por byte com as da pasta de trabalho.* **O que segue abaixo é o que era verdade da v0.66 até a v0.92:** as quatro skills com pasta de apoio estavam instaladas só com o `SKILL.md`. A `design-mecanicas-rpg` manda ler `sistema/skills/design-mecanicas-rpg/references/matematica-de-dado.md`, a `balanceamento-simulacao` manda importar `sistema/skills/balanceamento-simulacao/scripts/dados.py`, a `playtesting-rpg` aponta para `sistema/skills/playtesting-rpg/assets/casos-sonda.md` e a `redacao-acessivel-rpg` para `sistema/skills/redacao-acessivel-rpg/references/checklist-de-revisao.md` — **e nenhuma dessas pastas existe do lado instalado.** *Medido na v0.66, contra as skills de sistema da mesma conta, que trazem as pastas delas normalmente.*

> **Ponteiro pendurado é pior que texto velho.** Texto velho dá conselho errado e dá para desconfiar dele; ponteiro pendurado manda abrir arquivo que não existe, e quem está seguindo a skill conclui que ela quebrou. **Toda reinstalação tem de levar as pastas junto** — o `LEIA-ME` dizia o contrário desde a v0.3 e foi corrigido.

## O sistema em uma página

**Base:** d20. Ficha começa no nível 2, teto lendário no 30.

**Maestria** = 1, +1 a cada oito níveis (chega a 4). É o único número que cresce com nível.

**Cinco atributos**, escala 0–6, o número é o modificador: Força, Destreza, Constituição, Inteligência, Essência. **Inteligência sabe; Essência percebe** — Sentir Energia e Percepção moram em Essência desde a v0.16.

**Quatro Testes de Resistência:** Físico (Força ou Destreza, travado na criação), Vigor (Constituição), Intelecto (Inteligência), Espírito (Essência).

```
Ataque corpo a corpo = d20 + Força
Ataque à distância   = d20 + Destreza
Ataque de conjuração = d20 + 2 + maestria
Defesa               = 10 + Destreza + proteção
Pontos de vida       = (inicial do Caminho + Con) + (por nível do Caminho + Con) × (nv − 1)
Pontos de energia    = PE por nível do Caminho × nível   (sem atributo, sem inicial)
Integridade          = 20 + 8 × (nível − 1)   (plana — sem Caminho, sem Constituição)
CD de feitiço        = 10 + 2 + maestria
Teste de Resistência = d20 + atributo do TR (+2 se treinado)
Perícia              = d20 + atributo + maestria (só se treinado)
Crítico              = 20 natural, e dobra os dados (só onde há rolagem de acerto)
Ofício               = d20 + o atributo que a situação pede + maestria (só se treinado)
Turno                = movimento 9 m + ação padrão + ação bônus + reação
Iniciativa           = d20 + Destreza
Arredondamento       = para o lado que não te favorece. Custo sobe, ganho desce,
                       e o que você ganha nunca fica abaixo de 1
```

| Caminho | dado | vida no nv 1 | vida por nível | PE por nível | soma |
|---|---|---|---|---|---|
| Bastião | d12 | 12 | 7 | 4 | 11 |
| Vanguarda | d8 | 8 | 5 | 5 | 10 |
| Guia | d8 | 8 | 5 | 5 | 10 |
| Evocador | d6 | 6 | 4 | 6 | 10 |
| Emanador | d6 | 6 | 4 | 6 | 10 |

**A trava da vida:** média dos dados **+ 3 de Constituição ≈ 8**, que é o que o manual supõe. Não é a média dos dados sozinha — esse foi o erro da v0.18. A soma vida+PE quase igual nos cinco é o que faz a troca ser sabor em vez de degrau de poder.

**A regra que governa tudo:** numa rolagem disputada, os dois lados precisam crescer no **mesmo ritmo**. Atributo investido cresce +3 na campanha; maestria cresce +3. Por isso nada deriva.

**Progressão:** marcos nos níveis 6, 10, 14, 18, 22, 26 e 30. Cada marco dá **+1 atributo, +1 refino e +1 espaço de feitiço** de graça, mais **uma escolha de três** — **Corpo** (outro atributo), **Refino** (outro refino e uma aptidão) ou **Leque** (outro feitiço e uma Passiva). Teto de atributo 6, de refino 10.

**O refino é a métrica das aptidões**, e ele entra no texto delas como variável. Ele cresce +7 a +9 na campanha, então **não pode aparecer contra quem cresce +3** — fora acerto, CD, defesa, TR e dano; dentro custo, frequência, escopo e disputa contra outro refino.

**Cinco camadas de personagem:** Origem → Caminho → Técnica → Refino e Aptidões → Pactos.

**Feitiços conhecidos** = `2 + (nível ÷ 2)`, mais um por marco. Três no nível 2, dezesseis no 20. **O manual não conta feitiço desde a v7.7** — essa contagem tem um dono só, e é este documento.

**Vinte e três perícias e onze ofícios.** Perícia tem atributo fixo; ofício não — o atributo muda com o que você faz. O Caminho dá **duas perícias fixas + quatro livres** e **dois ofícios livres**; a Origem dá mais duas perícias. Oito de vinte e três, 35%.

**Feitiço de Toque** = os dados da Classe e nada mais (é o feitiço, e não soma arma nem Força). **Golpe simples** = arma + Força (é o Classe 0 físico). Um feitiço de Toque por turno; ataque extra é sempre simples.

**Invocações:** o invocador e todas as invocações somados entregam **uma** Rotina. A máquina inteira é a **peça 15**; o teto é da peça 6 §4.

## Onde cada coisa está

| Arquivo | Conteúdo |
|---|---|
| `00-fundacao/pitch-de-design.md` | os três pilares e as restrições do projeto |
| `01-pesquisa/dossie-de-metodologia.md` | a seção 8 lista as dez travas de arquitetura |
| `02-esqueleto/arquitetura.md` | o que o Fundamento resolve e os buracos em volta |
| `03-mecanica/01-atributos-acerto-defesa.md` | de onde vem o número — e a **seção 5.5, o `Inconsciente`**, que é a máquina de estado de 0 de vida |
| `03-mecanica/02-economia-de-atributos.md` | escala, criação, crescimento, teto |
| `03-mecanica/03-economia-de-acao-e-iniciativa.md` | turno, iniciativa, régua das Restrições |
| `03-mecanica/04-pericias-e-testes.md` | dificuldade, fail-forward, ataque de oportunidade |
| `03-mecanica/05-caminho-e-combate-sem-feitico.md` | Força, e por que uma arma sozinha não cabe |
| `03-mecanica/06-caminhos-e-trilhas.md` | os cinco Caminhos e suas Trilhas |
| `03-mecanica/07-pericias-e-oficios.md` | o quadro completo e as listas de cada Caminho |
| `03-mecanica/08-criacao-de-personagem.md` | **os oito passos, e uma ficha inteira de exemplo** |
| `03-mecanica/09-origens.md` | as cinco Origens, a sub-origem e as duas especiais |
| `03-mecanica/10-descanso-e-recuperacao.md` | os dois descansos, ambiente propício, exaustão e os quatro relógios |
| `03-mecanica/11-aptidoes-e-refino.md` | o eixo do controle: o refino, o terceiro eixo do marco, o catálogo e o Limiar |
| `03-mecanica/12-experiencia-e-progressao.md` | a curva de XP em degraus, o teto de um nível por missão, o retorno decrescente e o limiar do nível 20 |
| `03-mecanica/13-legados.md` | **a régua de magnitude e o catálogo de 81 entradas**, nos três formatos (Destranca · Ajusta · Desliga), com a cota de Desliga e as vagas declaradas |
| `03-mecanica/14-equipamento.md` | proteção, escudo, **as 52 armas** com fundo `3/5`, treino, requisito de Força e a divisão simples/marcial |
| `03-mecanica/16-ferramenta-amaldicoada.md` | **a camada por cima da arma**: a escada de grau, o `Estigma`, o gate herdado da peça 11, o `Desgaste`, o teto na ficha e as onze entradas |
| `03-mecanica/conferir-ferramenta.py` | as **dezesseis** checagens da peça 16, e o par declarado entre a 3 e a 9 |
| `03-mecanica/15-invocacoes.md` | **o sistema de criação de invocação**: a casa de iniciativa, o pool da Matilha, a ficha derivada, o custo, a morte, o retorno e o catálogo de 19 entradas |
| `03-mecanica/conferir-atributos.py` | acerto, defesa, TR, perícia, vida, PE máximo e a deriva contra o nível |
| `03-mecanica/conferir-acao.py` | a régua das Restrições, a dominância entre elas e o `Adianta` |
| `03-mecanica/conferir-pericias.py` | o quadro de perícias, as listas de Caminho e de Origem, e a colisão |
| `03-mecanica/conferir-descanso.py` | o piso, a exaustão, o arredondamento, a magnitude, o empilhamento e — **desde a v0.62** — a **escada de relógios**: os quatro degraus têm gatilho escrito, o `por cena` tem definição própria, e os dois totais publicados são recontados da pasta em vez de guardados |
| `03-mecanica/conferir-legados.py` | **catálogo**: recalcula a tabela de totais da peça 13 e falha se o escrito não bater com o contado |
| `03-mecanica/conferir-equipamento.py` | o fundo de cada arma, a dominância **uma vez por rota de proteção — e são três**, e o teto de Defesa derivado dos três donos |
| `03-mecanica/conferir-nomes.py` | o vocabulário do manual, extraído do `.docx`, contra todo nome que o projeto batizou |
| `03-mecanica/conferir-manual.py` | a direção contrária: o manual contra o vocabulário e os números do projeto |
| `03-mecanica/conferir-aptidoes.py` | a trava do refino, as três rotas do marco, o teto de Passivas e o kokusen |
| `03-mecanica/conferir-expansao.py` | os dois gates da Expansão, a ordem entre os degraus, o preço em espaços e a fragilidade da curva |
| `03-mecanica/conferir-orcamento.py` | o somatório: todos os drenos de PE ao mesmo tempo, e se todo preço tem número |
| `03-mecanica/conferir-xp.py` | a curva, o abismo que fecha, e se a regra ainda entrega o tempo que a Guilda pediu |
| `03-mecanica/conferir-criacao.py` | **a instância, não a regra**: a ficha de exemplo da peça 8 contra as fórmulas, a proteção da aptidão gratuita, a Trilha na criação e se o catálogo citado existe |
| `03-mecanica/conferir-ficha.py` | **o material contra a regra**: as 23 perícias, os 11 ofícios, os 5 Caminhos, as 15 Trilhas e as constantes do nível 2 que a ficha imprime, contra as peças donas |
| `03-mecanica/conferir-invocacoes.py` | as **trinta** checagens da peça 15, sem um número guardado dentro dele — e a busca exaustiva das 21.502 montagens que gastam o orçamento cheio no nível 30 |
| `03-mecanica/17-catalogo-de-entregas.md` | **o índice das 89 entradas** — 56 entregas de Trilha, 20 degraus de Caminho e as 13 Manhas —, com a regra de contagem e o ponteiro de onde o texto de cada uma mora |
| `03-mecanica/conferir-catalogo.py` | as **onze** checagens da peça 17, e **o primeiro validador que sai da pasta**: ele lê os três `DESENHO-*.md` da raiz |
| `03-mecanica/18-progressao.md` | **a tabela de progressão** — o que se ganha em cada nível, do 1 ao 30, numa tabela só. Nove das dez colunas são cópia com dono declarado; a décima, o tamanho da lista de feitiços, nasce aqui |
| `03-mecanica/conferir-progressao.py` | as **oito** checagens da peça 18: cada coluna reconstruída a partir do dono, a fórmula dos espaços contra a tabela da peça 11, e a cópia de três fichas da peça 2 |
| `03-mecanica/19-dano-e-condicoes.md` | **a régua de condição** — quanto vale cada uma das catorze, em dano por rodada e em nível —, mais as catorze condições, os catorze tipos de dano e a cobertura, que vieram da peça 1 |
| `03-mecanica/conferir-dano.py` | as **onze** checagens da peça 19, e a nona sai da pasta: ela bate as duas entregas publicadas que aplicam condição contra a régua. *A décima primeira entrou na v0.104, com a penalidade de arma* |
| `05-material/gerador-ficha/` | o gerador da ficha (Node: `node make.js`), e os dois `.docx` que ele produz |
| `conferir-repositorio.py` | a árvore, as referências mortas, os números que moram em mais de um documento, os **ponteiros de seção** — todo `peça N §M` citado tem de apontar para seção que existe, desde a v0.54 —, o **mapa** desta tabela contra a pasta, a **entrega** contra a fonte, a **pendência morta** desde a v0.100 — nenhum item de "Em aberto" pode pedir coisa que já existe —, e, **desde a v0.102**, a **contagem de checagens de cada validador, lida do código** |
| `99-arquivo/` | material morto, com LEIA-ME próprio. Não leia de lá para escrever peça nova |

**Duas peças foram parcialmente substituídas e trazem o aviso no topo:** as seções 3 e 4 da peça 4 saíram para a peça 7, e a seção 3 e o quadro de Caminhos da peça 5 saíram para a peça 6.

O manual do Fundamento **v7.11** (`manual/Fundamento-MANUAL-v7.docx`) é o subsistema de técnica e feitiço, já validado — 366 parágrafos e 90 tabelas. `manual/gerador/` traz o gerador (Node: `npm install docx && node make.js`) e `manual/matematica/` os validadores `pac7.py` e `v7.py`. **O `.pdf` está na v7.11, exportado junto desde a v0.93**, e ele deixou de ser exportado a mão: sai do `soffice --headless`, com a mesma paginação de 46 páginas.

**Quem é dono da versão do manual:** a primeira linha de `manual/gerador/COMO-USAR.txt`. Toda outra cópia — a capa em `partA.js`, este arquivo, o `README.md`, o `LEIA-ME.md` e o `arquitetura.md` — é cópia, e o `conferir-repositorio.py` falha se alguma divergir. *Ele nasceu na v0.33, depois de a capa do manual passar três versões dizendo 7.5.*

### O manual não é lei, e saber disso muda como se lê

*Registrado na v0.26.* Os limitadores, exemplos e tabelas do manual foram calibrados quando o sistema em volta era outro. **Servem de base para continuidade; não valem ao pé da letra.** Dez decisões do projeto estão penduradas em quatro tabelas dele, e as quatro não são iguais:

| tabela | dono | o que ela segura |
|---|---|---|
| **PE** — *"quantas vezes você lança"* | **o projeto** | o 6 do Emanador, a fórmula do PE máximo, o orçamento de missão. Mudou o 6? Regere a coluna |
| **Rotina** — dano por rodada por Classe | **o manual** | o feitiço de Toque, o ataque extra, o conserto da invocação, os 10% do crítico. Ela é a **régua**, não uma medida: mudar a Rotina reprecifica os quatro de uma vez |
| **Classe 0** — dano por faixa de nível | **o manual** | a linha do conjurador da peça 6 §3, o vão que paga o degrau do nível 7 dos cinco Caminhos, o `Resquício`, e os degraus de Trilha que põem um Classe 0 num slot |
| **Inimigo** — chefe e capanga por nível | **o playtest** | a trava de vida inteira. É a única das quatro que afirma algo sobre o mundo — que um combate dura ~3,5 rodadas — e ninguém é dono dela até alguém jogar |

> **A do Classe 0 entrou na v0.80, e ela entrou porque estava faltando.** *As outras três estão listadas aqui desde a v0.26; essa nunca foi listada, nenhum documento do projeto citava ela, e nenhum validador abria ela.* **O projeto preçava um Classe 0 em `4,50` fixo — número que não existe no manual — enquanto a tabela dele diz `2d8 · 3d8 · 4d8 · 5d8 · 6d8` por faixa de nível.** *Cinquenta e uma versões, e o que a achou não foi validador nenhum: foi ir ler a regra pendurada num termo antes de aceitar o preço dele, que é a lição nº 6.*
>
> **A lição que sai daí e que não estava escrita: uma tabela compartilhada sem dono declarado não é "ainda não decidida" — é uma que vai divergir e ninguém vai notar.** *Vale varrer o manual atrás da quinta.*

O `conferir-manual.py` falha se os dois lados divergirem, e a mensagem dele **nomeia o dono** em vez de acusar o projeto. Divergência ali é pedido de decisão.

## Pendências, da mais urgente à menos

> **A fila do LIVRO não mora aqui.** *A passada de termos da v0.108 deixou quatro itens em
> ordem — gatilho e duração nas 74 habilidades, exemplo inline em ~38 seções, a terceira camada
> em seis blocos, e o que sobrou da passada de voz.* **Eles estão em
> `05-material/livro/ESTADO-revisao.md`, na seção *A fila, em ordem de quem retoma*.** *Aqui
> ficam só as pendências de mecânica.*
>
> ⚠ **E fica registrado um padrão que custou quatro diagnósticos naquela versão:** *medir o
> marcador em vez do fenômeno.* **Quatro contas sobre o livro deram números altos e todas
> estavam erradas** — o regex procurava `Exemplo:` e o texto escrevia `**Exemplo.**`; a conta
> de exemplos ignorava a exemplificação sem marcador; a de "22 seções enterram a tabela" só via
> um dos três formatos de regra, e o número real era zero. ***Quando um número sobre um
> documento deste projeto parecer alto demais, o primeiro suspeito é o filtro, não o
> documento.***


1. ~~**Nome do sistema.**~~ **`Projeto - M`, decidido na v0.94.** *Aberto desde a v0.1; era a pendência mais velha que o projeto tinha.*
2. **Se a perícia livre da Origem devia ser da lista também.** As listas existem desde a v0.22, mas a segunda perícia continua livre com aprovação — é o último lugar da criação em que um número depende de julgamento do mestre.
3. ~~Quantas Trilhas um personagem acumula, e em que níveis.~~ **Fechada na v0.55, na v0.60 e na v0.65:** uma por ficha, entregas em `2 · 11 · 19 · 27`. **A Trilha é fechada — não se pega emprestado das vizinhas —, e nos níveis 11, 19 e 27 dá para TROCAR de Trilha, com troca total.** **O degrau de Caminho mudou na v0.70 e é `2 · 7 · 15 · 30`** — três fatias nos níveis 2, 15 e 30, e o nível 7 de graça porque ele vale o vão `físico − conjurador` e é correção de base.

   > **O calendário novo custa vão e seca, e o preço está aceito e medido.** Contra o antigo `7 · 15 · 23 · 29`, o vão máximo entre entregas vai de **5 para 8 níveis** (entre o 19 e o 27) e a seca vai de **24 para 31 missões** (entre os marcos 22 e 26). *Quem carregava as duas métricas era o degrau do nível 23.* **Decisão do Mizuki na v0.71: fica, e o resto do sistema carrega o vão pelas camadas de cima.** O que se compra com ele é identidade de Caminho no nascimento, junto com a Trilha, e um capstone no 30 — o formato do Paladino de 2024, que a auditoria da v0.69 conferiu em `3 · 7 · 15 · 20`.
4. **Como a Trilha Torrente cobra o segundo feitiço da rodada**, contra a regra de ouro nº 6. É o mesmo defeito da invocação — mais de uma ação por rodada — e o conserto que funcionou lá deve servir aqui.
5. ~~**O que Elo, Sutura e Perímetro entregam** que valha o golpe por rodada que o Guia não tem.~~ **Fechada na v0.61, com número:** valem **o vão `físico − conjurador` da peça 6 §3**, e ele chega como o degrau de Caminho do nível 7 — o mesmo lugar em que Bastião e Vanguarda recebem o ataque extra. Os cinco Caminhos empatam em `+6%` da Rotina no nível 30. *A ficção de cada uma continua sendo a Q5 de Trilhas.*
6. ~~**Se a curva de dano deve cruzar a coluna Rotina.**~~ **FECHADA na v0.73: sim, ela cruza, e por decisão.** *Ficou aberta desde a v0.27.* No nível 2 o conjurador está +38% e o físico +69% acima da Rotina; no nível 30 o físico terminava **2% abaixo**. **Com o orçamento dobrado duas vezes — a fatia é `5,08`, o Caminho leva `3` fatias e a Trilha leva `5` —, ele termina em `+35,8%` acima**, e a camada de Caminho mais Trilha vale **`27,7%`** do que o personagem faz.

   > **A dívida acoplada, com o número corrigido na v0.74: a tabela de inimigo do manual NÃO subiu.** A v0.73 registrou `36%`, e aquele número é o `+35,8% da Rotina` copiado com a base trocada — a base de antes era `98%` da Rotina. **Com a base certa dá `+38,3%`, e mesmo isso é teto e não valor**, porque supõe que as `8` fatias inteiras viram dano. A matriz do Bastião diz que não viram: o `Muro` põe `0,00` em dano, e um grupo de `Muro` **estica** a luta. **Redevirar quando as nove Trilhas que faltam estiverem preçadas** — o dono daquela tabela é o playtest, e `04-playtest/` continua vazia.

   > **A trava que veio junto, e sem ela a decisão não vale:** a magnitude **nunca pode vir de uma ação a mais por rodada.** O `+18%` da peça 6 §3.1 não é um teto de dano — é a medida de uma montagem de **três ações** que aquela seção reprova, e o que ela recusa é o mecanismo. *Eu li aquele número como teto disponível antes de conferir, que foi o segundo piso-lido-como-teto da mesma sessão.*
   >
   > **Contra-teste rodado:** `3×` o orçamento dá `+23%` e `4×` dá `+31%`, e as duas reprovam. O teto prático é `21` de dano por rodada. *Os dois números do topo eram 21% e 16% até a v0.60, e eles saíam de a peça 6 §3 estar lendo a coluna errada do manual — com a `Rotina` de verdade o abismo do topo quase fecha sozinho, e o que sobra é meia dúzia de pontos percentuais.*

### O estado de 0 de vida entrou na v0.37, e na v0.88 ele virou `Inconsciente`

*A peça 1 ganhou a **seção 5.5**, e ela fecha a pergunta nº 5 do `pitch-de-design.md` — aberta desde a v0.1.* A 0 de vida você escolhe **Aguentar** (apaga, janela de 3 rodadas, cura de 1 te levanta) ou **Insistir** (fica de pé, cada rodada custa 1/8, 1/4 e 1/2 da vida máxima). Levantar dá uma **Sequela**, que encurta a janela da próxima queda; **na segunda queda vem uma Cicatriz**. O fim da janela é o **estágio 4 de dano de alma**, que o manual já escrevia e que ninguém alcançava. Seis checagens novas no `conferir-atributos.py`, com oito perturbações conferidas.

> **A dívida: uma Cicatriz não tem mecânica, só nome.** Hoje ela é o registro de que a coisa aconteceu — permanente, não sai no descanso, e nada mais. *Isso foi deliberado, porque o conteúdo dela é da **peça de dano e condições**, e ela não existia.* **Ela existe desde a v0.103 e é a peça 19 — e a Cicatriz continuou aberta**, porque o escopo daquela versão foi a régua de condição mais as três seções que mudaram de casa. *A lista fechada de condições existe agora, e com nível: o que falta é decidir o que a Cicatriz faz.*
>
> **O que precisa ser resolvido quando aquela peça chegar:** o que uma Cicatriz faz, se ela tem teto por ficha, se some algum dia e por qual meio, e como ela conversa com a **Energia Reversa** — que é a candidata óbvia a apagá-la, e que **existe desde a v0.78**, na peça 11 §6. *A pergunta não morreu junto: a aptidão agora tem número, e quem responde se ela limpa Sequela continua sendo a peça de dano e condições.* Enquanto isso, ela é boa ficção e mecânica nenhuma, e **o texto da peça 1 diz isso com todas as letras** em vez de fingir que está fechado.
>
> *Fica marcado aqui porque decisão registrada não é decisão aplicada — foi assim que a Trilha passou sete versões escrita e não corrigida em três documentos.*

*Resolvida na v0.20:* a colisão do Grau. O manual, o PDF e as fontes já usam **Classe** — 0 ocorrências de "Grau" no `.docx`, `pac7.py` e `v7.py` passando.

*Resolvidas na v0.24:* os **nomes das Trilhas** — os seis que colidiam viraram **Batedor · Executor · Sutura · Perímetro · Servo · Matilha**, e o `conferir-nomes.py` falha se algum voltar. E o **Coro**: dono e invocação agem no mesmo turno, e não custa nada, porque o orçamento dividido é teto de saída e não de número de ações.

*Resolvidos na v0.26:* os **quatro buracos de regra** da v0.24 — arredondamento, o que conta como luta, a fórmula do PE máximo e o texto da exaustão. Mais a **Passiva Casca**, que morreu e virou a **Escama**; o **requisito e o preço do Kokusen Melhorado** (aptidão, refino 5 e nível 14); a definição de **resistência**; e os dois órfãos que apareceram no caminho — a **Fraqueza** com Habilidade e Sabedoria, e o **Carregar** contra a **Concentração** apontando para testes diferentes.

## O marco ganhou um terceiro eixo: o Leque

*Decidido depois da v0.26, e ele muda a peça 2.* A escolha de marco era **atributo ou refino**. Agora são três, uma por eixo da ficha — **corpo, controle e técnica**.

> **Passivo, em todo marco:** +1 atributo, +1 refino e **+1 espaço de feitiço**, gastável onde você quiser.
> **A escolha, uma das três:** mais atributo · mais refino e uma aptidão · **Leque: +1 feitiço, que só pode ser feitiço, e uma Passiva de graça.**

**Por que ele existe.** Passiva custa espaço de feitiço conhecido, e a Expansão de Domínio também — 2 pela incompleta, 3 pela completa. Sem uma rota que devolva espaço, quem monta técnica funda fica sem lista: pela conta antiga, três Passivas de Classe 2 mais a Expansão completa chegavam ao **nível 20 com dois feitiços**, e cinco Passivas de Classe 3 mais Expansão eram **impossíveis em qualquer nível** — 18 espaços numa ficha de 16. **O teto de "cinco Passivas pagas" do manual já era letra morta.**

**A linha passiva do marco sozinha conserta isso**, sem dobrar a lista:

| montagem | nv14 | nv20 | nv26 | nv30 |
|---|---|---|---|---|
| só feitiço | 12 | 16 | 21 | 24 |
| 3 Passivas Classe 2 + Expansão completa | 3 | **7** | 12 | 15 |
| 5 Passivas Classe 3 + Expansão completa | 0 | 0 | **3** | 6 |

A montagem típica sai de dois feitiços no nível 20 para sete, e a mais pesada que existe — cinco Passivas de Classe 3 mais a Expansão completa, 18 espaços — passa a caber **a partir do nível 22**, em vez de nunca.

**E as três escolhas se auto-equilibram.** `+1 feitiço + 1 Passiva` empata com `+1 refino + 1 aptidão` porque Passiva e aptidão vivem na mesma escada de Classe; o que sobra dos dois lados é `+1 feitiço` contra `+1 refino` — e **refino não vale nada para quem não tem aptidão**. Quem escolhe Leque não quer refino, e quem escolhe refino não quer Passiva. As três compram coisas que não se substituem.

**O nome passou pela triagem, e dois candidatos morreram nela.** *Técnica* está dentro de **Sem Técnica** (a Origem) e de **Técnica Máxima** (o manual); *Repertório* já é Trilha do Emanador. **Leque** está livre nos dois lados — e é a palavra que o próprio Mizuki usou para descrever o que a rota compra.

**A fórmula dos feitiços, fixada:** `2 + (nível ÷ 2)`, arredondando para baixo. Isso dá **3 no nível 2** — dois de toda ficha mais o do próprio nível 2, que é o que confundia os dois documentos — e **12 no nível 20**. A prosa do manual diz treze; ela vira **doze, mais um por marco**, e entra na v7.7.

**O teto de Passivas: a grátis traz a própria vaga.** Cada escolha de Leque sobe o máximo em 1, e a Passiva concedida ocupa essa vaga nova. Então o teto vai de 5 a **12**, e as **pagas continuam sendo cinco** — exatamente as cinco que o manual sempre teve. O teto não cresce de verdade; ele só abre lugar para o que a rota concede.

E o que essa ficha paga por isso, no nível 30:

| rota | atributo | refino | aptidões | Passivas | feitiços a mais |
|---|---|---|---|---|---|
| sempre atributo | **14** | 8 | 0 | 5 | 0 |
| sempre refino | 7 | **10** | **7** | 5 | 0 |
| sempre Leque | 7 | 8 | 0 | **12** | **7** |
| meio a meio | 10 | 10 | 2 | 7 | 2 |

Doze Passivas e sete feitiços é o que a rota **compra** — zero aptidões, refino parado no 8 e metade dos pontos de atributo de quem foca corpo. Não é bônus por cima.

## Expansão de Domínio, clash e três decisões soltas

> **O argumento de projeto das aptidões e do refino saiu daqui nesta versão** e está na **seção 10 da peça 11**, inteiro. Ele descrevia uma peça que fechou na v0.27, e este documento é lido no começo de toda conversa — 24 KB de argumento de peça pronta faziam ele não caber numa leitura só. O que sobrou abaixo é o que **não** é da peça 11: a Expansão, que mora no manual, e três decisões que atravessam outras peças.

### O clash de expansões, fechado

> **Refino contra refino. Empatou, os dois rolam `1d10 + quantidade de aptidões + metade do nível`.**

**O refino resolve o clash onde domínio ainda não existe, e para de resolver onde ele acontece** — do nível 26 em diante o especialista e o meio a meio estão os dois no teto 10, e entre eles cai sempre no d10. Não é erro; é o que a regra faz, e o texto tem que dizer.

O d10 fica grande de propósito: a ameaça é calibrada contra o nível do grupo, então os dois lados chegam empatados e a diferença vem de foco e perda de foco. **Sete aptidões de vantagem ainda perdem 12% das vezes**, e dez níveis de distância valem meio dado.

**O inimigo carrega refino e aptidões na ficha dele**, como vida e dano. É onde a divergência entre mestres nasce, então a implementação deve seguir o padrão do ambiente propício: **valor sugerido pelo nível na tabela, e a palavra final do mestre em cima dele** — para ninguém preencher do zero. Com o chefe herdando a curva do meio a meio, o refino decide sozinho do nível 14 ao 22, e do 26 em diante o jogador especialista leva +3, que é 72%.

### Três decisões que saíram junto, e que não são da peça de aptidões

**A Trilha vem no nível 2, e já rende ali.** Três lugares do material diziam que ela *"não afeta o nível 2, afeta a primeira subida"* — e o motivo da confusão é o mesmo dos feitiços: **toda ficha nasce no nível 2**, e o nível 1 é quem ainda está entrando no mundo jujutsu, civil ou sem técnica desperta. A Trilha é identidade, como o Caminho, e nasce com o personagem.

> **Aplicado na v0.34, e ficou sete versões parado.** A decisão está escrita aqui desde a v0.27 e terminava em *"corrigir na peça 6, na peça 8 e aqui"* — e os três continuavam dizendo o contrário. Este documento chegou a se contradizer sozinho: esta seção dizia que a Trilha vem no 2, e duas tabelas mais abaixo diziam que ela não afeta o 2. **Decisão registrada não é decisão aplicada**, e nada no projeto conferia a diferença.

**A Expansão de Domínio tem duas peças: Acerto e Efeito.** O **Acerto** é o que a expansão garante que acontece; o **Efeito** é o que ela permite fazer lá dentro. A incompleta resolve o Acerto por rolagem; **a completa, com barreira, resolve por acerto garantido** — e isso já é palavra do manual, que resolve feitiço por *Acerto · Teste de Resistência · Automático*.

| | Acerto | Efeito |
|---|---|---|
| Megumi, incompleta | buffa todas as invocações | permite invocar todas elas |
| Hakari | todos recebem a informação da expansão | o pachinko, e a regeneração |
| Higuruma | ninguém no ambiente pode causar dano | o julgamento, e as punições |
| Gojo | a enxurrada de informação | tocar em outros para poupá-los |
| Sukuna | clivar e desmantelar acertam | alcança todos no ambiente |
| Yuta | os feitiços das espadas acertam | todas as técnicas copiadas, em forma de espada |
| Jogo | queima todos no ambiente | amplifica a técnica |
| Mahito | ninguém desvia do toque | alcança todos no ambiente |
| Dagon | os shikigami acertam | amplifica a técnica |

**E isso fecha um laço que ninguém tinha visto:** se a expansão completa sempre acerta, os **quatro anti-domínio serem aptidões baratas é o que a torna sobrevivível**. Se fossem raros, o acerto garantido seria opressivo. A decisão de pôr os quatro no catálogo por marco foi tomada antes de a expansão ter forma, e é a peça que faz as duas funcionarem juntas.

**As Bênçãos de Corpo, para quem não tem energia.** A Restrição Celestial pelo ramo da Maki não tem energia amaldiçoada — sem PE, sem feitiço de Toque, sem Sentir Energia — então não tem aptidão nem refino. Ela ganha **a mesma máquina com outra métrica**: as aptidões se chamam **Bênçãos** e o refino se chama **Lapidação**.

> **Corpo Amaldiçoado saiu deste balde na v0.38, e o motivo é canon.** A frase acima incluía os dois. Mas *cadáver amaldiçoado de mutação abrupta produz a própria energia* — é literalmente o que a mutação concede, cerca de três meses depois de ele acordar. **O que ele não tem é técnica, não energia.**
>
> Então ele é **misto**: PE, aptidões e refino como qualquer feiticeiro, e **Técnica Marcial** no lugar do Fundamento, porque não existe técnica inata para escrever. A Maki é a única sem energia nenhuma, e as Bênçãos são só dela.
>
> *Decidido com o Mizuki na v0.38 e **aplicado na peça 9 na v0.39**, junto com as outras mudanças que a peça 13 devia àquela peça.* A entrada de Corpo Amaldiçoado hoje diz *"você tem energia amaldiçoada: cadáver de mutação abrupta produz a própria, uns três meses depois de acordar"*, com PE, aptidões e refino normais e Técnica Marcial no lugar do Fundamento. Andar em parede e em água, deslocar-se no ar, *fast steps* — o físico no lugar do energético. Os dois nomes passaram pela triagem e estão livres nas duas direções.

Isso é a camada de aptidão da **Técnica Marcial**, que o material já descreve como *"paga com o corpo e com ferramenta amaldiçoada"* — e é o que destrava duas das três rotas de Origem que não rodam hoje.

### Sem Técnica precisa de máquina de criação própria, e ela é menor do que o esqueleto supôs

*Decidido na v0.38, e os dois lados vieram de levantamento.*

**O `arquitetura.md` diz que Sem Técnica precisa de "um sistema próprio, paralelo ao Fundamento". Pelo material, precisa de menos do que isso — e por outro motivo, de mais.**

| rota | o que ela é, no material |
|---|---|
| **Aptidão** | **Energia Reversa não é técnica inata** — é manipulação de energia amaldiçoada, e é por isso que quem não tem técnica consegue usar. O raro nela é curar **os outros** |
| **Estilo da Sombra** | **anti-domínio**, e a espada é o jeito mais comum, não o requisito. A técnica central foi aprendida em um mês por quem não usa espada, e o líder atual da escola derrubou as restrições dela |

**Metade já existe:** as quatro anti-domínio entraram na v0.29 e a **seção 6.5 da peça 11** já trata o Domínio Simples como aptidão pura, sem lâmina. **E a `Energia Reversa` saiu da lista de pendentes na v0.78** — ela está escrita na seção 6 daquela peça, com gate e teto.

> **Mas a rota não pode ser "os outros menos o Fundamento".** Se for só subtração, ela fica atrás de todo mundo e ninguém escolhe por vontade — escolhe por castigo. **Ela precisa de uma máquina de construção com a mesma dignidade que o Fundamento tem:** quantas aptidões, com que orçamento, e o que se paga por elas.

*A prosa da peça 9 chama o Estilo da Sombra de "técnica de espada e corpo", e isso ficou mais estreito que a própria mecânica do projeto. Corrigir quando a peça sair.*

### A Expansão de Domínio, escrita — manual v7.7

*Decidido depois da v0.26.* Ela **não é aptidão** e não mora nesta peça: mora no manual, no molde de uma Passiva, **comprada trocando espaços de feitiço conhecido**, com gate duplo de nível e refino, em dois degraus.

| degrau | preço | gate | quem passa no nível do gate |
|---|---|---|---|
| **incompleta** | 2 espaços | nível 10 e **refino 4** | especialista e meio a meio; generalista entra no 14 |
| **completa** | **3 no total** (+1 de upgrade) | nível 14 e **refino 5** | especialista e meio a meio; generalista entra no 18 |

*Fixados e validados. O `conferir-expansao.py` afirma os dois.* O `CHANGELOG` da v0.27 registrou refino 4 e **6**, e a versão anterior desta seção registrou refino 3 e 5 — os dois estavam meio certos, e a conta separou.

**No nível 10 as três rotas estão coladas — refino 5, 4 e 3, sem buraco entre elas.** Então qualquer gate que barre o generalista pega o meio a meio com folga zero. Isso não é escolha de número: é o formato da curva, e só dá para escolher **quem raspa**. O refino 4 barra o generalista e deixa o meio a meio na beirada; era isso ou não barrar ninguém.

**No nível 14, refino 5 e refino 6 separam exatamente as mesmas rotas** — só o generalista fica de fora nos dois. Eles diferem só na direção em que quebram, e o validador mediu: com **5**, a curva caindo um ponto **não move ninguém**; com 6, ela tira a completa do meio a meio. Com 5 o risco é a curva *subir* e o generalista entrar no 14 — e isso a checagem 1 acusa em voz alta. **O 5 é imune para o lado que dói e barulhento para o lado que não dói.**

**E "barrado" quer dizer atrasado, não trancado.** O generalista chega à incompleta no nível 14 e à completa no 18 — quatro níveis atrás do especialista nos dois degraus. Ele paga em tempo o que não pagou em marco, e o validador falha se alguma rota deixar de chegar.

**O preço sai do mesmo bolso das Passivas, e é aí que ele morde:**

| | nv10 | nv14 | nv22 | nv30 |
|---|---|---|---|---|
| espaços na lista | 9 | 12 | 18 | 24 |
| a incompleta é | 22% | 17% | 11% | 8% |
| a completa é | **33%** | 25% | 17% | 12% |

Quem pega a incompleta mais duas Passivas de Classe 2 gasta **dois terços da lista no nível 10** e exatamente metade no 14. *Correção:* a versão anterior desta seção dizia *"dois feitiços são 33% da lista no nível 10"* — aquilo foi calculado com a fórmula velha de feitiços conhecidos, antes de a v0.27 fixar `2 + (nível ÷ 2)` e a linha passiva do marco. Com nove espaços no nível 10, dois são 22%.

**A resposta é mais barata que a ameaça, e isso é o que faz o acerto garantido caber.** A **Cesta Oca de Vime** não tem gate nenhum: custa **uma escolha de marco, e a primeira acontece no nível 6** — quatro níveis antes de qualquer um poder comprar a incompleta. Não é preciso ser do eixo do controle; é preciso gastar uma escolha nele, uma vez na campanha inteira. **As duas rotas puras que nunca escolhem Refino terminam sem resposta anti-domínio nenhuma**, e isso é propriedade da rota, não defeito do gate.

*Corrigido na v0.29:* esta frase dizia **Domínio Simples**, e ele subiu para Classe 2 (nv10 · 10 · 14). A resposta do nível 6 é a Cesta Oca, e ela responde **menos** — anula o Acerto e não o Efeito. **O argumento continua de pé**, porque o que a peça 11 chamou de opressivo foi o acerto que nunca falha, e não o Efeito. A resposta barata cobre o que precisava cobrir, e só isso.

**E nenhuma das quatro serve contra a Expansão incompleta.** Ela não tem acerto garantido — o Acerto dela rola —, então você se defende dela com Defesa e Teste de Resistência como de tudo o mais. É canon: o Reggie usou Cesta Oca dentro do domínio incompleto do Megumi e levou porrada dos shikigami do mesmo jeito.

**O que custa para usar, fixado na v0.28:**

| | incompleta | completa |
|---|---|---|
| abrir | `6 × maior Classe` de PE | `8 × maior Classe` |
| desconto nos feitiços lá dentro | `1/3 do refino` | `metade do refino` |
| ação | a rodada inteira, nas duas | |
| duração | `metade do refino` em rodadas, mínimo 1 | |
| barreira | não tem | `50 × metade do refino`, só por fora |

**A escada de custo fecha:** feitiço do topo `3×` < Técnica Máxima `5×` < incompleta `6×` < completa `8×`. E a incompleta passar da Máxima é de propósito — a Máxima é **dada** no nível 17 para toda ficha, e a incompleta é **comprada** sete níveis antes, por dois espaços de lista e um gate que barra uma rota.

**O desconto quase virou lucro.** Duração é também quantos feitiços saem lá dentro, então desconto × duração compete com o custo de abrir. Com `6 × Classe` e desconto de refino cheio, o saldo fica **negativo do nível 20 em diante** — você abre o domínio e termina com mais PE. As combinações escolhidas ficam entre +18 e +31 em todo nível, e a margem não encolhe. **E o desconto precisa de piso:** sem *"nenhum feitiço custa menos de 1 PE"*, o refino alto zera as Classes baixas e o PE deixa de existir dentro do domínio.

**O Acerto acontece quando você abre, e de novo no começo de cada turno seu.** Um relógio só, o do portador — as alternativas punham o proc no turno dos alvos, e *"começo da rodada dos alvos"* não é momento definido num sistema de iniciativa individual. **E se algum dia o custo cair para Ação Bônus, a regra de ouro nº 6 já resolve sozinha:** *feitiço em Ação Bônus ou Reação só permite mais um de Classe 0 no turno*.

**O Rescaldo** — a técnica queima quando o domínio acaba, de qualquer jeito: desfeito por vontade, expirado ou estilhaçado. Isso é **preço e não risco**, porque acontece em todo uso. `Queima` morreu na triagem (é Melhoria do manual, e causa dano), e `Empurrão` e `Estilhaço` também estão ocupados.

**A barreira cai em ~2,4 rodadas** de saída cheia contra uma duração de 3 a 5 — dá para derrubar de fora dentro do próprio tempo, que é o que faz a decisão de atacar ou esperar existir. Por dentro não quebra. O mestre pode declarar exceção.

**O clash ficou de fora, e está engatilhado** em `03-mecanica/RASCUNHO-clash-de-expansoes.md`: o modelo de push gradual pede seis números novos e substitui uma regra marcada como fechada. A v7.7 cita a regra decidida.

**E há uma consequência de vocabulário:** se a Expansão entra no manual, **o manual passa a usar "refino"**, que é termo do projeto. É a direção contrária do problema que a v0.26 consertou, e é de propósito — mas o `conferir-manual.py` precisa saber, senão a próxima varredura vai tratar refino como palavra estranha.

## Problemas de design abertos

Nenhum validador pega estes — eles vieram de rodar os testes da skill de design contra o material.

1. ~~**O Legado tem teto de quantidade, não de magnitude.**~~ **Fechado na v0.39, pela peça 13.** *Ficou aberto da v0.24 até lá.* A régua é de **três formatos travados nos próprios termos**, e não escada de preço: `Ajusta` mexe em número e carrega relógio da escada da peça 10, com a largura do gatilho escolhendo o degrau; `Desliga` só apaga o que ninguém comprou; `Destranca` é zero no dado e precisa de gatilho do jogador. **Os quatro que a régua reprovou saíram, cada um com destino escrito:** o *Não Sou Gente* mudou de camada e virou Passiva paga com espaço de feitiço, o *Irmãos* ganhou gatilho do jogador, o *Instinto Bruto* perdeu a metade morta e ficou só contra Intuição — que é Inteligência, e aí é troca de verdade —, e o *Alcance Impossível* morreu por ser técnica, que a peça 9 proíbe Origem de conceder.
2. ~~**O Guia pode estar dominado pela Vanguarda.**~~ **FECHADO na v0.61, e ficou aberto da v0.20 até lá.** *Reformulado na v0.24*, quando a classificação que faltava foi escrita na peça 6 §3.1 — **Bastião e Vanguarda pelo Caminho; Arremate e Coro pela Trilha; o Guia por nenhuma rota** —, e a dominância virou uma pergunta com número: *o que Elo, Sutura e Perímetro entregam que valha um golpe por rodada?* **A Q3 de Trilhas respondeu: eles valem o vão, e o vão é o degrau de Caminho do nível 7.** O ataque extra saiu do nível 6 para o 7 na mesma versão, e a leitura que destravou tudo foi medir a base — **o conjurador está a −8% da Rotina e o físico a −2%: ninguém está acima, e o ataque extra é correção de base e não bônus.**
3. **O ofício não passa no filtro do multi-mestre.** "O mestre escolhe o atributo na hora" faz dois mestres cobrarem coisas diferentes pelo mesmo ofício, com até cinco pontos de diferença. Conserto: tabela com o atributo padrão de cada um.
4. ~~**A escolha de refino no marco paga mal, e três marcos pagam zero.**~~ **FECHADO na v0.89, e ficou escrito como aberto até a v0.98.** *Entrou na v0.41.* *Achado pelo Mizuki na passada de Equipamento, e a conta confirmou pior do que o palpite.* O refino **passivo chega a 8** sem escolha nenhuma; sete escolhas de marco compram **+2**, e o teto 10 é alcançado no **nv22**. Do nv22 em diante a escolha *"refino e uma aptidão"* vira **só a aptidão**, enquanto *atributo* e *Leque* continuam valendo cheio — três marcos com um dos três eixos pela metade.

   | o que o +2 de refino compra | refino 8, de graça | refino 10, sete escolhas |
   |---|---|---|
   | proteção de cobrir-se | 3 | 4 |
   | RD da Reação | 12 | 15 |
   | desconto e duração do domínio | 4 | 5 |

   **A rota se paga pela quantidade de aptidões, não pela magnitude do refino** — e isso contradiz a frase que abre a peça 11, *"o refino é a métrica das aptidões"*. Como as aptidões usam o refino como variável, o valor de cada uma também quase não muda entre 8 e 10.

   > **O conserto foi o terceiro dos três que estavam propostos aqui: escolha diferente depois do teto.** ***Decisão do Mizuki na v0.89: no teto, a escolha de Refino leva DUAS aptidões***, e a rota pura vai de `7` para `10`. **Está aplicado na peça 11 §3**, e a checagem 5.2 do `conferir-aptidoes.py` passou a medir marco a marco — a 5 media o fim da campanha e saía verde com o meio quebrado. *As outras duas alternativas foram medidas e reprovaram, com a conta escrita na entrada da v0.89 do CHANGELOG: subir o teto de `10` para `15` acende dois contratos, e baixar o refino passivo move a tabela de gates inteira.*
   >
   > **⚠ Este item ficou nove versões escrito como aberto depois de fechar**, contradizendo a linha de abertura deste mesmo arquivo, que desde a v0.89 diz que ele era *"o único problema de design que tinha sobrado"*. *Achado na v0.98, e é a lição de que decisão registrada não é decisão aplicada — desta vez aplicada à lista que registra as decisões.*

5. **"O mestre declara o que foi uma luta" é discricionariedade que vira número.** *Aceito de propósito na v0.26*, e é a única coisa da peça 10 sem lista fechada por baixo — a declaração muda quantos degraus de exaustão o grupo acumula, e isso muda quanto PE o respiro devolve. A aposta é que ninguém está em melhor posição de dizer se aquilo foi uma luta do que quem acabou de dirigir a cena. Se dois mestres divergirem no playtest, o conserto é o do ambiente propício: fechar a lista.

*Resolvidos na v0.26:* os **três buracos de regra** que estavam aqui — a fórmula do PE máximo (ela já estava no manual, na tabela de "quantas vezes você lança o seu melhor feitiço"), o arredondamento e o que conta como luta. E o **tamanho dos degraus de exaustão**: a escada nunca esteve desordenada, ela é ordenada por **consequência**, e o degrau 1 e o degrau 3 valem exatamente os mesmos −25 pp porque os dois são desvantagem. O que estava errado era o texto prometer "leve"; o `conferir-descanso.py` agora confere magnitude.

*Resolvido na v0.21:* **Sentir Energia**. O achado da v0.20 dizia que ela falha no teste do bônus automático, e a decisão foi aceitar conscientemente — sempre vai existir perícia melhor que outra, e as pessoas escolhem por querer ser únicas. Deixou de ser problema aberto e virou decisão registrada.

## Marcado para o playtest

- **A correção da v0.16 passou do ponto?** Essência agora carrega a perícia mais rolada da mesa, o TR Espírito e os Pactos — e vai carregar a Integridade também. O peso está empatado com Inteligência em 39% cada, mas empate na planilha não é empate na mesa.
- **Apareceu alguém com Constituição 0 ou 1?** Ela é a maior alavanca de sobrevivência do sistema — **+79% contra os +56% da Destreza**, os dois medidos de 1 a 6. *Corrigido na v0.24:* o par que estava escrito aqui era +113% contra +56%, e ele mistura bases — o 113% é de 0 a 6. Na mesma base a Constituição está na frente por 1,4×, não por 2×. Continua sendo a pergunta de playtest, com o tamanho certo. Se ninguém a zera, virou obrigatória, e o conserto é uma linha: ela volta a entrar só do segundo nível em diante.
- **O espalhamento de vida de 3,2× incomoda?** O Evocador de Constituição 0 cai em 1,7 rodadas no nível 30; o Bastião de Constituição 6 aguenta 5,5.
- **O estágio 4 de dano de alma dispara alguma vez?** Hoje a alma é maior que o corpo em quatro dos cinco Caminhos, então quase todo mundo cai antes. Muda quando a Essência entrar na Integridade.
- **Intuição está em cima do muro.** "Ler a pessoa" tem cara de perceber e ela ficou em Inteligência como dedução. Se rolarem Percepção no lugar dela, muda de casa.
- **Provocar e Intimidação vão brigar?** Uma faz recuar, a outra faz avançar. Claro escrito, vago em jogo.
- **Força tem uma perícia só**, e a lista não conserta. O conserto barato, se doer, é Força somar em pontos de vida.
- **A taxa de acerto real é 50%** contra alvo que investiu em defesa, e o combate deve levar 3,4 a 4,0 rodadas. Os textos antigos citam 60% e 65% e estão marcados como previsão, não como número fechado.
- **Alguém rola Pontaria?** Ela e o ataque à distância são as duas Destreza e as duas acertam alvo.
- **Alguém usa ação bônus?** É a peça mais herdada do turno e a que mais custa tempo de mesa.
- **Dois mestres contam o mesmo número de lutas?** *Entrou na v0.26.* A exaustão dispara da quarta, e quem conta é o mestre. Medir a mesma missão com dois mestres e comparar o número de degraus no fim do dia.
- **Alguém escolhe a Escama?** *Entrou na v0.26.* Ela vale 50% quando o tipo bate e zero quando não bate, e o ponto de virada é uma luta em quatro. Medir se as pessoas pegam — e, se pegarem, com que frequência o tipo delas aparece.

## O que existe e o que não existe, medido

Vale ter isso à mão, porque o material é grande e engana. *Medido na v0.33, e é retrato e não número fechado — reconte antes de citar.* **101.000 palavras** contando `sistema/` (fora o `99-arquivo/`), o CHANGELOG e o README, das quais **34.200** nas doze peças de mecânica e **32.000 no CHANGELOG** — quase um terço do projeto é o registro do porquê, e não o jogo. Mais **3.880 linhas** nos dez validadores de `03-mecanica/`, e 4.640 contando os treze.

**O que existe:** as regras, com conta, com validador e com o motivo de cada número.

**Uma ficha de nível 2 precisa de dezessete coisas. Treze existem, e as quatro que faltam não mordem nessa faixa** — *medido na v0.26, depois que os quatro buracos saíram, e recontado na v0.32, quando a tabela de XP saiu desta lista para a peça 12:*

| o que falta | por que não trava uma missão de nível 2 |
|---|---|
| ~~Tabela de proteção~~ | **fechada na v0.48**, na peça 14: Traje e Revestimento com três degraus cada, e escudo com três |
| Regra de Pactos | é opcional na criação |
| Trilhas com número | a Trilha é escolhida no nível 2, mas o que ela entrega chega depois |
| ~~Aptidões e degraus de refino~~ | **fechada na v0.27**, na peça 11 — e as quatro anti-domínio na v0.29. *Continuam valendo só do nível 6 em diante* |

**O que não existe, e faz falta para alguém jogar:**

> **As duas primeiras linhas da segunda tabela são vocabulário que ainda não tem peça, e por isso a definição delas mora aqui — provisoriamente.** *Quando cada peça for escrita, a definição vai para ela e esta linha vira ponteiro.* **Enquanto isso, este é o dono:** a peça 13 e a peça 14 citam as duas e apontam para cá em vez de repetir, que é a lição nº 9 sendo obedecida em vez de explicada.

| falta | tamanho do buraco |
|---|---|
| ~~**Tabela de progressão consolidada**~~ | **fechada na v0.99**, na peça 18: uma tabela só, trinta linhas, nove colunas. *Ela não estava espalhada por cinco documentos — eram dez números em seis lugares, e um deles não tinha dono nenhum.* **A curva de refino das três rotas continua no `arquitetura.md` §4.3**, e é a última fonte da progressão fora de uma peça |
| ~~**Quick-start jogável**~~ | **Abandonado como arquivo separado na v0.102**, e **fechado como texto na v0.106**: `sistema/05-material/livro/` tem o Manual da Guilda completo, 230 páginas, com o quick-start (*"Antes da primeira sessão"*) escrito direto no PDF — o molde que a v0.103 previu, *"como o PDF carrega essa propriedade é trabalho dele"* |
| **Playtest** | `04-playtest/` está vazia. Zero sessões desde a v0.1. **Todo número do sistema é previsão** |

*A **tabela de XP** saiu desta lista na v0.32.* Ela era a trava nº 1 de mundo compartilhado e ficou aberta trinta versões; hoje é a peça 12, com o `conferir-xp.py` em cima dela.

A skill `redacao-acessivel-rpg` existe exatamente para a travessia de "nota de design" para "texto de regra", e nunca foi rodada contra o material. **Com o quick-start fora, quem recebe essa travessia é o PDF.**

> **⚠ A pergunta que ficou aberta junto com aquela decisão FECHOU na v0.103.** *O dossiê de metodologia lista, como trava de arquitetura, que o material nasce com um quick-start na frente — e o argumento de lá não é sobre ter dois arquivos, é sobre **alguém conseguir jogar antes de ler tudo**.*
>
> ***Decisão do Mizuki: ela sai da lista do projeto.*** *"vamos finalizando as informações e mandando pro outro repositório o necessário para fazer o PDF, eu já tô no processo de estudo sobre".* **Como o PDF carrega essa propriedade é trabalho dele; o que o repositório faz é mandar o material para a entrega.**

**E as dez pendências que só a mesa responde são todas de nível 2** — Constituição virou obrigatória, alguém usa ação bônus, Intuição contra Percepção, se quatro perícias livres é escolha demais, se alguém rola Pontaria, se o extra da Origem é escolha de igual para igual, se a criação leva mesmo vinte a quarenta minutos, se um Legado por ficha é pouco, se três lutas de graça é o número certo, e se o descanso curto devia devolver alguma vida. **Nenhuma delas precisa das aptidões.**

## Onde estamos, e o que falta

A ordem de construção é a da seção 6 do `arquitetura.md`, e ela **acabou** — os seis passos estão fechados.

| # | peça | estado |
|---|---|---|
| 1 | De onde vem o número, e defesa | **fechado** (peças 1 e 2) |
| 2 | Economia de ação e iniciativa | **fechado** (peça 3) |
| 3 | Teste fora de combate | **fechado** (peças 4 e 7) |
| 4 | Caminho e combate sem feitiço | **fechado** (peças 5 e 6) |
| 5 | Criação de personagem | **fechado** (peça 8) |
| 6 | Descanso e progressão fora de feitiço | **fechado** (peças 10 e 12) — descanso na v0.23, progressão na v0.31 e v0.32 |

O que falta agora, na ordem em que travam umas às outras:

**A ordem foi decidida simulando uma campanha que começa amanhã**, e não por tamanho de peça. Cada linha é o momento em que o jogo trava:

| # | peça | quando ela trava o jogo |
|---|---|---|
| ~~1~~ | ~~Descanso e recuperação~~ | **fechada na v0.23** (peça 10) |
| ~~2~~ | ~~Aptidões e degraus de refino~~ | **fechada na v0.27** (peça 11), e as quatro anti-domínio na v0.29 |
| ~~3~~ | ~~Tabela de XP~~ | **fechada na v0.31 e v0.32** (peça 12) — era a trava nº 1 de mundo compartilhado |
| 4 | **Trilhas com número** | **depois do nível 2.** O Caminho para de significar alguma coisa. Resolve também a dúvida aberta do Guia contra a Vanguarda |
| ~~5~~ | ~~**Equipamento**~~ | **fechada na v0.48** (peça 14) — a proteção ganhou número, e o teto de Defesa ganhou dono derivado |

> **Mas a fila mudou de natureza na v0.32, e vale ler isto antes de pegar a próxima peça.**
>
> **Não existe mais peça de regra bloqueando alguém de jogar.** Uma missão de nível 2 roda inteira: cria, joga, recupera, sobe de nível. As duas acima travam a **segunda sessão** e a **primeira subida**, não a primeira mesa.
>
> O que falta para alguém sentar na mesa não é regra — é **material**: as peças são argumento de design e não texto de mesa. **`04-playtest/` está vazia desde a v0.1, e todo número do sistema continua sendo previsão.**
>
> A rota decidida com o Mizuki foi: v7.7 → anti-domínio → XP → **validação e polimento** → ficha e quick-start. *Os quatro primeiros saíram, o polimento foi a v0.33 e a **ficha saiu na v0.35** — `05-material/` não está mais vazia.* **O quick-start foi abandonado como arquivo na v0.102, e o último degrau desta rota virou o PDF — que saiu na v0.106, com o quick-start escrito direto nele.**

## A fila decidida com o Mizuki na v0.36

Quatro peças, e a ordem é de **dependência**, não de tamanho. A ordem que ele levantou era Legados → Caminhos → Itens → Invocações; a peça de Caminhos foi para o fim porque **duas das cinco árvores dependem das outras duas peças**.

| # | peça | destrava | depende de |
|---|---|---|---|
| ~~1~~ | ~~**Legados** — a régua de magnitude, e ~5 por Origem~~ | **fechada na v0.39** (peça 13): régua, catálogo de **81 entradas** e o `conferir-legados.py` | — |
| ~~2~~ | ~~**Equipamento** — armas, escudos, uniformes~~ | **fechada na v0.48** (peça 14): as 52 armas com orçamento fechado, proteção, escudo, treino e requisito de Força, mais o `conferir-equipamento.py` com onze checagens | — |
| ~~3~~ | ~~**Invocações** — o sistema de criação~~ | **fechada na v0.58** (peça 15), com o `conferir-invocacoes.py` e trinta checagens | — |
| 4 | **Caminho, Trilhas e subtrilhas** — a árvore de cada um | o resto | **2 e 3** |

### A fila foi reordenada na v0.50, e as duas peças novas ganharam posição

*Decisão do Mizuki: "Invocações agora, ferramenta entre ela e a Trilha."* As duas que a v0.49 destampou entram assim:

| # | peça | por que aqui | move o contador? |
|---|---|---|---|
| ~~1~~ | ~~**Invocações**~~ | **fechada na v0.58** (peça 15), com o `conferir-invocacoes.py` e trinta checagens | rotas 6/9 → 6/9 · vagas 0 de 7 |
| ~~2~~ | ~~**Ferramenta amaldiçoada**~~ | **fechada na v0.59** (peça 16): a máquina e o catálogo saíram na v0.55 e na v0.56, e o `conferir-ferramenta.py` tem **dezesseis** checagens | **rotas 6/9 → 8/9** · vagas 3 de 7 |
| 1 | **Trilhas** | fecha com as quinze de uma vez, e agora nada mais a trava | toca **100% das fichas** |
| 2 | **Objeto amaldiçoado** | a conta o pôs por último | rotas 6/9 → 6/9 · **vagas 1 de 7** |

> **✔ A DUAS RESPOSTAS ACABOU NA v0.103.** *Esta fila dizia `Trilhas`; a peça 16 §9 dizia que a `Técnica Marcial` **é a peça seguinte**.* ***Decisão do Mizuki: são as três Trilhas do Evocador** — `Servo`, `Matilha` e `Coro`.* **A peça 16 foi corrigida junto**, e ela deixou de nomear a Técnica Marcial como a seguinte.
>
> *As três estão paradas desde a v0.82, e ele mesmo tinha decidido que ficariam por último. Elas fecham as quinze Trilhas e tiram o Evocador de ser o único Caminho sem Trilha com número.* **Quando entrarem, o total de 89 entradas da peça 17 muda e a checagem 1 do `conferir-catalogo.py` acusa.**

> **As posições 2 e 3 ganharam rascunho na v0.54**, e os dois têm o mesmo formato do de Invocações — perguntas em ordem de dependência, com o que a conta já fecha separado do que é sabor.
>
> **E a v0.55 fechou a máquina de ferramenta e duas perguntas de Trilhas.** A ferramenta é **uma das 52 armas mais UM `Estigma`**, e o grau decide o **formato** dele — grau 4 não dá Estigma nenhum e só fere maldição, grau 3 dá Classe 1, grau 2 dá Classe 2 com gate de nível 7, grau 1 dá Classe 3 com gate de nível 13, e a especial é Classe 3 e **única no mundo**. **O gate é o da peça 11 §6 sem a metade de refino**, porque cobrar refino trancaria a peça na cara da Restrição Celestial que não tem energia. O **`Desgaste`** compra o gate e nunca a Classe, e a ficha topa em **três `Estigmas`**, que é 43% do orçamento de escolha de marco da campanha. *Falta o catálogo e o validador.* **Em Trilhas:** sem multiclasse (uma Trilha por ficha, o que fecha a pendência nº 3 desta lista) e **as subtrilhas cruzam Trilhas do mesmo Caminho**.
>
> **`03-mecanica/16-ferramenta-amaldicoada.md`** *(era rascunho até a v0.59)*. A conta fechou três coisas antes de qualquer pergunta: **grau não pode ser mais ponto de arma** (no nv30, dobrar o orçamento de uma arma de duas mãos vale `1,5%` da Rotina contra os `6%` a `9%` de uma Trilha inteira); **a ferramenta não é o que faz o sem-energia competir em dano** (a arma comum é 96% da Rotina no nv2 e 12% no nv30 — fechar isso pediria 95 de dano por rodada, que é o Fundamento e não um item), então **ela entrega ferir maldição, que é binário**, e o dano é da Técnica Marcial; e **grau como gate de patente está refutado pela peça 12**, porque *"Grau é reconhecimento; nível é poder"* e a espiral fechada é a mesma. *E o cubo que prendeu o Gojo é **objeto** amaldiçoado, não ferramenta — a fonte é explícita, e ele é da peça que a v0.50 pôs em último.*
>
> **`03-mecanica/RASCUNHO-trilhas.md`.** O achado que decide o formato: **catorze dos vinte e nove níveis não entregam nada hoje, e são todos os ímpares** — os feitiços conhecidos cobrem todo nível par, e maestria e marcos caem em cima de níveis que já tinham feitiço. **A Trilha tem onde cair sem competir com nada.** E o risco real da peça é escala: **quinze Trilhas × quantas entregas** dá de 30 a 120 entradas, contra as 81 que a peça 13 fechou em uma versão e as 52 armas que custaram **seis** à peça 14. *A diferença entre as duas foi a régua vir antes do catálogo, e é a única recomendação de método que aquele documento faz.*

**Só a posição 3 contra 2 era escolha. As outras três a conta fechou sozinha:**

- **Invocações antes de Trilhas** não é preferência: `Servo`, `Matilha` e `Coro` **são** o sistema de invocação visto de dentro. As outras doze Trilhas já estão desbloqueadas desde que Equipamento fechou — era a Vanguarda que dependia dela.
- **Ferramenta antes de Técnica Marcial** está escrito na peça 5 §3: a Maki *"só compete porque a ferramenta amaldiçoada carrega a energia por ela"*. Técnica Marcial escrita antes produz rota que não fere maldição.
- **Objeto amaldiçoado por último**, e é o contrário do que a v0.49 fazia parecer. Ele foi o achado daquela versão, mas **Receptáculo e Reencarnado já rodam hoje** — os dois vão para o Fundamento. Ele fecha **1 vaga de Desliga e mais nada.** *Buraco de vocabulário real não é o mesmo que buraco que trava alguém.*

**Invocações fechou na v0.58 e é a peça 15**, em `03-mecanica/15-invocacoes.md`, com o `conferir-invocacoes.py` em cima dela. O §5 daquela peça é a especificação das trinta checagens, e ele foi escrito **antes** do validador — que é por que ele coube numa versão só, contra as seis que a peça 14 gastou.

> **A peça fechou na v0.58, e o argumento inteiro mora nela — não aqui.** A Q1 (iniciativa) no §3.1, a Q2 (cinco fichas ou uma) no §3.2, a Q3 (a ficha) no §3.3 e no §3.6, a Q4 (o custo) no §3.4, a Q5 (a morte e o retorno) no §3.5, o catálogo e a régua de criação no §3.7, e a especificação das trinta checagens no §5. *Este ponteiro existe para quem retomar não recomeçar: as decisões têm um dono só, e é lá.*
>
> **A máquina, em seis linhas:** a invocação age **na casa do dono**; a Matilha é **uma ficha com cinco corpos**, pool com cascata, rodada resolvida **em pool**; a ficha é **derivada do dono mais um deslocamento que só desce**, com `Traço` e `Comando` comprados num orçamento de **2 a 9** pontos; invocar custa **`1 × maior Classe` e a ação padrão**, e **comandar custa a ação padrão**; ela **some no zero**, é **vulnerável a área** e **morre em definitivo** se o excedente passar de metade da vida máxima ou um golpe causar a vida máxima inteira — e quem só chegou a zero volta com **metade da vida**; e **a amarra são 18 metros**, lidos do alcance base de Projétil.
>
> **A Q6 fechou na v0.63**, e ela nunca foi desta peça: `Servo`, `Matilha` e `Coro` são Trilhas. **O `Servo` estava dominado por falta de eixo** — empatava em saída e perdia ou empatava em corpos e ação —, então não existia número que o consertasse dentro dos três. *O conserto era uma coluna nova na matriz.* **A concessão: o corpo do `Servo` leva `5 × h` de vida — o pool inteiro da `Matilha` num corpo só — e o orçamento da ficha mais metade.** A tabela está no fim do §3.7 daquela peça, e o `DOMINANCIA_PENDENTE_Q6` do validador foi a **conjunto vazio**.
>
> **A vida não entra por dominância, e por isso ela tem checagem própria.** Só o orçamento já zera a matriz; tirar o `5h` sairia **verde** e desfaria em silêncio a metade da pergunta que a matriz não mede — a de *"perder o corpo acaba o kit"*. *É a lição nº 8 por outra porta: uma checagem que se mede pelo eixo errado sai verde na perturbação que importa.*
>
> **O que a peça ainda deixa pendurado são duas regras, e as duas apareceram na v0.67 por tropeço:** **quando a vida cheia da invocação reinvocada volta** — o candidato natural é o descanso longo, e é sabor — e **o que acontece com a invocação quando o DONO cai**, que a peça nunca escreveu. *Enquanto as duas não fecharem, nenhuma entrega de Trilha que mexa nelas tem contra o que ser medida.*
>
> **E a v0.68 achou que a escala da v0.67 não tinha chegado inteira.** A venda de deslocamento ficou devolvendo `1` enquanto catálogo e orçamento iam para `×4`, **e a tabela do orçamento do `Servo` estava com o cabeçalho numa escala e as colunas na outra.** Ao todo foram seis linhas. **A devolução virou `4`**, a tabela do `Servo` passou a ser derivada, e as checagens 8, 9 e 10 ganharam a metade que faltava — o tamanho da devolução, o resumo do topo contra a tabela dona, a tabela do `Servo` contra os marcos, e a razão entre as duas moedas recalculada em vez de aceita.
>
> **E o arredondamento do `Servo` virou letra morta:** na escala nova todo orçamento é múltiplo de `4`, então *"mais metade"* sempre fecha redondo e ele ficou com `2` pontos a mais nos níveis 6, 14, 22 e 30. *A regra global da peça 1 continua valendo — ela só deixou de ter o que raspar aqui.*
>
> **E o buraco que ela achou na peça 6 continua aberto, porque é de playtest e não de conta:** a regra da seção 4 preça o **dano** da Matilha e não preça o **tempo de mesa** dela. Cinco corpos agindo por rodada custam o mesmo tempo quer cada um faça 25 de dano ou 5 — e foi por essa metade, não pela do dano, que o 5e 2024 trocou a família inteira de `conjure`. O conserto que a peça achou é de gesto e não de regra: **rolar em pool** corta de sete gestos e meio por rodada para três. **O número esperado está escrito no §3.2 antes da sessão** — a Matilha custa `2,5×` um personagem de nível 6 —, e a checagem 4 confere que ele continua batendo com a tabela dele mesmo.

> ~~**A dívida que a peça 13 marcou continua aberta, e agora ela é dupla.**~~ **Paga na v0.104.** *A peça 13 fechava dizendo "quando equipamento fechar, a primeira coisa a fazer é voltar aqui", e ninguém voltou nem quando a 14 fechou na v0.48 nem quando a 19 fechou na v0.103.* **As cinco vagas destravadas foram escritas**, e o que faltava não era trabalho: era a trava do `Desliga`, que proibia encostar em qualquer coisa com preço e por isso não deixava nenhuma delas nascer. *Decisão registrada não é decisão aplicada — e às vezes o que impede a aplicação é outra decisão.*

### Onde Equipamento parou, na v0.42

**Fechado:** duas classes de uniforme (`Traje` e `Revestimento`) com **escadas de Força separadas** — Traje `— / — / 3`, Revestimento `3 / 4 / 6`; a **escada de escudos** com proteção, requisito de Força e teto de Destreza; **treze categorias e 52 armas**; **as oito propriedades escritas**; o dado do tiro e a recarga; e a régua de **itens comuns** em três camadas, com a terceira desligada.

**O teto de Defesa ganhou dono, e não é o que o rascunho supunha.** O `20` é **derivado** de `10` (peça 1 §5) + teto de atributo `6` e teto de refino `10` (peça 2 §3) + a fórmula de cobrir-se (peça 11 §5) — zero parâmetros livres. **Ninguém escreve o número:** Equipamento é dona do **invariante** (*nenhuma montagem de equipamento passa da Defesa que a rota sem equipamento alcança*), e o validador deriva o teto dos três donos. **Equipamento topa em 19**, por decisão, e não em 20.

**Quatro coisas caíram nesta versão:** o §3 dizia que as duas rotas topam em 20 (dá 19, desde que o escudo ganhou teto de Destreza); o Traje era a classe do meio do 5e contra **cobrir-se**, que é a armadura leve deste sistema e ninguém tinha reconhecido; a peça 6 §3 **não tem exceção para arma de tiro**, o que fazia a arma acertar com Destreza e causar dano com Força — 5× o buraco que as propriedades deviam pagar; e o `0,60` do §5 não reproduz com a fórmula do §4, que dá `0,33`.

**A dívida da peça 11 e da peça 8 foi APLICADA:** o escudo **soma** com cobrir-se em vez de desligar, e o preço da Reação virou agnóstico de fonte. Três checagens novas no `conferir-criacao.py` guardam as duas.

### E o que a v0.44 fez com ela — a régua de preço mudou

**A pergunta *"o preço mora na classe ou na arma?"* foi respondida, e a resposta é a arma.** O motivo não foi de gosto: a escada de dados do §5.2 já punha **dois dados dentro da mesma classe** (Pistola `2d8` e Submetralhadora `3d6`, as duas em `Tiro leve`), então o catálogo praticava **9 pacotes de preço para 8 classes** desde a v0.42.

> **1 ponto = `0,33` por rodada = um passo de dado = uma propriedade.** Orçamento: **`2` numa mão, `4` em duas.**

Ele saiu por **regressão contra as seis classes publicadas**, e cinco fecham exatas. A sexta é a `Versátil`, que estourava em 1 — **a dominância que a v0.41 tinha achado e não sabia dimensionar.** A régua inteira cabe numa tabela de teto de dado por número de propriedades, no molde do PF2e, e o teto da `Fineza` (d6 numa mão) cai dela sozinho.

**Fecharam junto:** a escada do tiro (`3d10` → **`2d10`** no topo, porque o `3d10` gastava 9,0 num orçamento de 4 e estourava em 11 pontos na mão de um Força 0); o X da `Munição` em `2 · 3 · 4`, depois que o `X=1` foi flagrado **apagando o ataque extra**; e a `Versátil` a **custo zero**, que fecha a dominância de três versões com tamanho (0,1 ponto, só no nv2).

### A v0.45 inverteu a régua, e o efeito de crítico morreu

**O dado passou a ser ENTRADA e o número de vagas passou a ser SAÍDA** — a ficção diz o tamanho da arma e a conta diz quantas propriedades ela carrega. **Fundo `3` numa mão e `5` em duas**, e o teto de dado não se moveu. Como gastar menos que o orçamento é dominância estrita, **toda arma é obrigada a encher as vagas**: identidade deixou de ser opcional e virou construção.

**A restrição devolve `1` ponto** — `Volumosa`, `Embainhada`, `Comprida` —, que é a metade do *"a arma dá acesso e restrição"* que nunca tinha sido implementada. Usada por **3 das 41** (7%).

> **O efeito de crítico da categoria MORREU, e os treze nunca foram escritos.** *Achado do Mizuki:* **"ninguém lembra do efeito de crítico na hora de aplicar."** A conta confirmou — **0,44 disparo por combate na mesa inteira de quatro**, e um jogador vê o efeito da arma dele a cada 9 combates. E a causa embaixo era pior: na régua velha, a arma que a ficção põe no teto de dado tinha **zero vagas de propriedade**, então ter identidade *era* descer o dado. Com o fundo, as propriedades carregam a identidade sozinhas: **39 assinaturas para 41 armas**, contra as 14 que o preço sozinho dava.

**As 52 armas têm dado e propriedades** (§5.3), com zero estourando o orçamento e zero com vaga vazia. As duas gêmeas que sobraram são `Machete = Machado` e `Soqueira = Tekko`, que são a mesma coisa na ficção.

### A v0.47 fechou as duas decisões de acesso

**A divisão simples/marcial** (§5.4.1) e **o requisito de Força** (§5.5). As duas resolvem acesso por eixos diferentes — uma separa por **Caminho**, a outra por **atributo** —, e nenhuma pode ser preço: toda arma já fecha no mesmo fundo.

> **Simples — 24 armas:** `Lâmina Curta` · `Porrete` · `Ceifa` · `Arremesso` · `Manopla` · `Massa`, mais a `Balestra`.
> **Marciais — 17:** `Lâmina Longa` · `Machado` · `Armas Longas` · `Flexível`, mais o `Yumi`.
> **De fogo:** `Arma de Fogo`, sozinha. Ferramenta amaldiçoada fica fora desta peça.
>
> **Requisito `Força 3` nos dois degraus de cima de cada escada:** `d10` e `d12` no corpo a corpo (11 armas), `2d8` e `2d10` no tiro (6). Ele lê o **dado impresso** — o passo do `Versátil` não conta, senão ele pega a Katana, que tem `Fineza`.

**Busca exaustiva dos 1024 cortes possíveis: 543 passam nas quatro travas de conta**, e o que fecha é cruzar com a âncora do 5e 2024. **A trava que a v0.45 achou que era estrutural não é:** o `d8` de uma mão e o `d12` de duas moram nas mesmas três categorias — `Lâmina Longa`, `Massa` e `Machado` —, e qualquer corte que ponha as três no marcial deixa o balde simples **1,0 dado atrás nas duas mãos**, que é o modo de falha do 5e que aquela versão diz ser impossível.

**E os dois gates se multiplicam em vez de somar.** Sob o requisito de Força sobram **duas** armas de duas mãos sem requisito — Kusarigama e Corrente —, então uma das duas categorias delas tem de ser simples, ou o Caminho não-marcial de Força baixa fica **sem a economia de duas mãos inteira**. Nenhum dos dois gates faz isso sozinho.

**O gate no tiro fecha um buraco que o do corpo a corpo não alcança:** sem ele, um conjurador de Força 0 e Destreza 0 pega o Rifle de Precisão e faz **11,0 sem investir um ponto de atributo**, contra 6,5 do melhor corpo a corpo dele.

**O que falta:** a **penalidade** por empunhar sem treino ou sem requisito, que é da peça 19 — escrita na v0.103, com este item ainda aberto lá dentro. **Os nomes dos degraus de escudo fecharam na v0.59:** `Broquel` (punho, 15–45 cm), `Médio` e `Torre` (cobre o corpo, se planta no chão). *O `Médio` carrega duas colisões aceitas e declaradas na peça 14 — uma letra de `Medo` (Tema) e o gênero do tier de Restrição `Média`.*

> **Esta lista tinha mais dois itens até a v0.59, e os dois já estavam prontos.** O **`conferir-equipamento.py`** entrou na **v0.48**, com a dominância rodando uma vez por rota de proteção — cobrir-se, uniforme e sem energia nenhuma, as três. E **os dois dados do `Yumi`** foram corrigidos na **v0.47**, na mesma versão que flagrou: `Daikyū` para `1d10`, `Hankyū` para `1d8`, fechando exatos em `4 de 4`. *Vencido em dois documentos ao mesmo tempo, porque a lista foi copiada em vez de apontada.*


### Bloquear — a regra opcional que a v0.43 escreveu

Mora em `03-mecanica/RASCUNHO-bloqueio.md`, e **não mudou número de peça nenhuma**. A Defesa continua sendo `10 + Destreza + proteção`, e continua sendo o padrão. Ela é a segunda frente aberta hoje, independente de Equipamento, e só entra em balanceamento quando o tópico de regras opcionais existir.

> **Ao ser atacado, você pode Bloquear:** role `2d10 + (sua Defesa − 11)` no lugar da sua Defesa.
> **Duplo 10 — Aparar:** não acerta, e você pode gastar a Reação para contra-atacar com **+3 de dano**.
> **Duplo 1 — Brecha:** acerta, e o agressor pode gastar a Reação dele para atacar de novo, sem bônus.
> O Aparar **não anula um 20 natural**, e Bloquear **não vale em Teste de Resistência**.

**O achado que sustenta tudo.** A resposta padrão do hobby para *"quero rolar minha defesa"* é *role d20 no lugar dos 10 da CA* — e ela dá **+2,5 pontos percentuais de graça, em todo ataque, para todo mundo**, porque `E[d20] = 10,5` e a base da Defesa é `10`. Oito buscas externas não acharam uma única discussão do problema. **Qualquer dado de média 10 é neutro por construção**, e o d20 não tem conserto: a média de um dado único sempre termina em `,5`, então o buraco é de meio ponto e nenhum modificador inteiro o fecha.

**O invariante, e ele é a peça frágil:**

> **Bloquear usa exatamente o mesmo modificador da Defesa passiva. Nada pode aumentar um sem aumentar o outro.**

`+1` de diferença vale 2,5pp — o tamanho exato do viés que a regra saiu para consertar. Um escudo, uma aptidão, um Legado ou um item que suba um lado só desfaz a mecânica inteira. **Isso vale para Equipamento**, que é a peça em andamento e a que mais mexe em Defesa.

**Em aberto:** as condições que impedem Bloquear — surpreendido, caído, agarrado. *A peça 19 nomeia duas das três — `Derrubado` e `Agarrado` —, e a terceira não existe como condição neste sistema;* a linha na ficha (`Defesa 17 · Bloquear 2d10+6`, que é o que faz o `−1` nunca aparecer na mesa); e a Reação na ficha de inimigo, sem a qual a Brecha não funciona.

**E o validador dela não pode ser arquivo novo.** As três checagens do §7 do rascunho são todas sobre a fórmula da Defesa, que é da **peça 1** — então elas vão para o `conferir-atributos.py`, do mesmo jeito que o Caído foi na v0.37. Um `conferir-*.py` novo quebraria a contagem de treze por treze, e Bloquear não é peça.

### Decidido — o Caminho continua sem dar dados de dano

*A regra da peça 5 §4 foi desafiada e confirmada.* Três das cinco árvores propostas pediam dado de dano — a tabela de desarmado do Bastião, a mecânica de arma da Vanguarda e o atributo somado no dano do Emanador. **A regra fica, e as árvores se desenham dentro dela.**

O motivo é o pilar 1, e está escrito na peça 5: *"se o Caminho desse dano, dois personagens do mesmo Caminho começariam a se parecer, e a técnica que cada um escreveu perderia espaço."* O que sobra para o Caminho conceder é a lista permitida — posicionamento, alvo, duração, recuperação, troca do fixo do acerto por atributo, e exceção estreita e paga na economia de ação.

### O que sobrevive de cada proposta, e o que não

| Caminho | o que passa | o que não passa, e por quê |
|---|---|---|
| **Guia** | **tudo.** Auxílio, estender, reposicionar e recuperar são literalmente a lista do permitido. E fecha a pergunta aberta desde a v0.24: *o que Elo, Sutura e Perímetro valem contra um golpe por rodada* | — |
| **Bastião** | socar como ação bônus (*"exceção estreita e paga na economia de ação"*); agarrar, prender e forçar reposicionamento | **a tabela de desarmado tipo monge** é dado de dano. O dado do soco é **equipamento**, e o Caminho mexe no que se faz com ele |
| **Vanguarda** | o que se **faz** com a arma: alcance, reposicionamento forçado, troca de alvo, exceção na economia de ação. Proezas passivas, se não forem dado | **o dado de cada arma é equipamento**, não Caminho. Por isso ela vem depois da peça 2 |
| **Emanador** | **metade já existe:** a peça 6 §5 concede *trocar o fixo de 2 do acerto de conjuração por Inteligência ou Essência*. Isso é acerto, e é neutro porque os dois lados crescem +3 | **somar atributo no dano do feitiço.** Ele quebra a paridade conjurador‑guerreiro, que está calibrada em `d20 + 3` nos dois desde o nível 2 |
| **Evocador** | benefício que não seja ação nem dano | depende da peça 3. E a trava é dura: *você e todas as suas invocações somados entregam **uma** Rotina* — mais corpos agindo por rodada é o que quebra todo sistema d20 |

**Duas coisas para medir antes de escrever, não depois:**

- **A reação de RD do Bastião encosta em cobrir-se de energia**, que já dá RD de `1,5 × refino` por 2 PE. Ou uma delas domina a outra, ou são a mesma peça com dois nomes. Medir as duas juntas.
- **Os *pontos de feitiço* do Emanador são moeda nova ao lado do PE.** O `conferir-orcamento.py` existe porque o bolso já é apertado — qualquer moeda nova passa por ele antes de ter número.

### A peça de Legados fechou — o que ela deixou pendurado

*A régua veio primeiro e o catálogo depois, e a ordem se pagou: os quatro Legados que a régua reprovou eram do catálogo antigo.* São **81 entradas** nas sete Origens, mais o `Sem Técnica` — escrito uma vez e referenciado pelas cinco Origens que o aceitam, porque cinco cópias do mesmo texto seria a lição nº 9 dentro de um catálogo.

**A ficha leva dois Legados, e um deles é obrigatoriamente Destranca.** A regra óbvia — *dois de listas diferentes* — não conserta: ela deixa pegar `Ajusta + Desliga`, e aí quem otimiza continua sem ficção **e a economia mecânica dobra**. Com o Destranca obrigatório ela não dobra.

**O que ficou pendurado, e é o que Equipamento vai encontrar:**

| pendência | espera |
|---|---|
| ~~**Sete vagas de Desliga**~~ **DUAS**, declaradas na tabela em vez de preenchidas | **as cinco destravadas fecharam na v0.104** — `Cabo`, `Assinado`, `Revezamento`, `Talhe` e `Usado`, cada uma apagando uma condição nomeada uma vez, com o relógio saindo do nível dela. *Só couberam porque a trava do `Desliga` foi relaxada na mesma versão.* **As duas que sobram esperam peça que não existe:** uma espera objeto amaldiçoado e a outra espera Técnica Marcial |
| A **Armaria** do Descendente e o **Enterrado** do Reencarnado | relidos na v0.49, e **os dois não pedem a mesma coisa**: a Armaria é `ferramenta amaldiçoada` (arma forjada, com graus) e o Enterrado é `objeto amaldiçoado` (a maldição em forma de objeto) |
| O **Não Sou Gente** virar Passiva paga com espaço de feitiço | a decisão está tomada, a Passiva não está escrita |
| A **máquina de criação do Sem Técnica** | Aptidão e Estilo da Sombra |

> **O alvo livre acabou, e é por isso que as vagas existem.** A enumeração de alvos legais do sistema inteiro tem sete, e o `Ferro Velho` gastou o último. Inventar oito alvos para fechar a cota seria escrever entrada para fechar contagem — que é exatamente o defeito que essa régua nasceu para achar. **Peça nova é o que cria alvo novo.**
>
> **E a v0.49 mediu isso pela primeira vez com uma peça pronta na mão: Equipamento fechou e produziu UM alvo legal.** A trava do Desliga proíbe encostar no que tem preço, e a peça 14 **precificou quase tudo que nomeou** — propriedade, restrição, teto de Destreza, treino. Sobrou o **requisito de Força**, que ninguém compra — e ele vale `1,0` de dado, e vale zero para quem já tem Força 3. *A régua funcionando como desenhada, numa direção que ninguém previu: peça nova cria alvo novo, mas peça bem precificada cria pouquíssimo.*

### E um padrão que vale saber antes de começar

**As quatro peças caem quase todas em 5, 6 e 9 — que são as que não têm validador.** A peça 8 ganhou o dela na v0.34, depois de sete versões com a Defesa errada. As outras três continuam descobertas, e é de lá que saíram os dois erros daquela versão.

**Depois dessas quatro**, e não antes:

| peça | por que só depois |
|---|---|
| **Técnica Marcial** | ~~bloqueada por equipamento~~ — **destravada na v0.48**, e é a peça que a vaga de Desliga do Corpo Amaldiçoado espera. *O que ela ainda precisa é de ferramenta amaldiçoada para a Maki e o Toji ferirem maldição* |
| **Estilo da Sombra** | está **bloqueado pelas aptidões** — a rota da Shoko é literalmente "o poder vem de aptidão" |

As duas são economias de poder novas, e construir a quarta e a quinta antes de a segunda ter teto escrito é o erro que o esqueleto já avisou.

**E depois de todas essas**, na ordem em que fazem falta:

| peça | o que ela resolve |
|---|---|
| **Objeto amaldiçoado** | **a maldição presa em forma de objeto** — não é item imbuído de energia: *é* a coisa. Resto de feiticeiro antigo, que encarna quando um receptáculo compatível o consome. *Entrou na lista na v0.49, escondido dentro da palavra "ferramenta".* **Duas Origens inteiras são construídas em cima dele** — Receptáculo é comer um dedo, Reencarnado é ter virado um |
| **Ferramenta amaldiçoada** | **arma forjada para canalizar energia**, com graus, que até quem não é feiticeiro consegue usar. Prometida desde a peça 5 §5 e declinada pela peça 14 §8 item 2, que a mandou para tópico próprio *"com graus e forja"*. **É o único jeito de ferir maldição sem energia própria** — a Maki e o Toji |
| **Dano de alma, com Essência na Integridade** | já decidido, não aplicado |
| **Pactos** | a camada mais perigosa de escrever solta |
| **Bestiário** | sai da matemática de inimigo que o manual já tem |

~~E uma coisa solta que não é peça: o nome do sistema.~~ **Batizado na v0.94: `Projeto - M`.** *Era a pendência mais velha do projeto — aberta na v0.1 e fechada 93 versões depois.*

**As nove rotas de Origem, e quais já rodam:**

| rota | jogável hoje |
|---|---|
| Latente · Receptáculo · Descendente · Reencarnado · Feto | **sim** — vão para o Fundamento |
| Restrição Celestial, ramo do Kokichi Muta | **sim** — Fundamento, com o corpo limitado na ficha |
| qualquer uma **+ Sem Técnica** | não — falta Aptidão ou Estilo da Sombra |
| Corpo Amaldiçoado | não — falta Técnica Marcial |
| Restrição Celestial, ramo da Maki | não — falta Técnica Marcial |

**E três coisas que a criação ainda contorna**, cada uma com a saída escrita no ponto do texto onde ela pesa:

| falta | como se contorna |
|---|---|
| Regra de Pactos | pacto na criação só com aprovação do mestre e preço escrito na ficha |
| ~~Tabela de proteção~~ | **fechada na v0.48**, na peça 14. A ficha continua nascendo com a proteção 1 de cobrir-se; o que mudou é que agora existe o que vestir por cima, e o escudo **soma** em vez de desligar |
| Trilhas com número | a Trilha é escolhida na criação, junto do Caminho. O que ela entrega é a peça de Trilhas |

## Como o Mizuki gosta de trabalhar

**Perguntar antes de decidir.** Escolha de sabor — quantos itens numa lista, quais são, como se chamam, em que ordem aparecem — é dele, e ele quer decidir junto em vez de aprovar depois de pronto. Trazer as opções com o número e o trade-off de cada uma já calculados.

**Mas não perguntar o que a conta responde.** Se dominância, deriva ou o filtro multi-mestre já decidem, rodar a conta e apresentar o resultado. A pergunta é para onde a conta empata ou não se aplica.

Fase por fase, com o plano à vista antes de executar. Número vem de conta rodada, não de intuição. Documento não pode ter cara de saída de IA. Antes de fechar versão, revisão cética — inclusive contra o que eu mesmo escrevi. Material superado vai para o `99-arquivo/`, não fica com aviso em cima.

**As lições que custaram erro moram no `README.md`, e só lá.** São nove, e a seção se chama *"Nove lições que custaram erro"*.

*Até a v0.32 este arquivo guardava a própria cópia da lista.* Ela tinha parado em cinco enquanto o README chegava a nove, e a lição nº 2 daqui ainda listava *"v0.16, v0.17, v0.19, v0.24 e v0.26"* quando o README já contava sete versões. Duas cópias, duas respostas — que é a lição nº 9 acontecendo dentro do documento que existe para avisar sobre ela. Uma lista, um dono.

As três que a semana da v0.28 à v0.32 acrescentou, e que valem ler antes de escrever conta nova: **um preço se mede somado, nunca sozinho** (nº 7); **uma checagem não pode se medir contra a própria constante** (nº 8, que apareceu três vezes em três versões); e **um número que mora em dois documentos vai divergir** (nº 9).
