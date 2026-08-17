Prompt para a próxima conversa
Escrito no fim da v0.84, contra o estado real. Cole isto inteiro numa conversa nova.
Renomeie este chat para: RPG - JJK13

Projeto de RPG da Guilda (Jujutsu Kaisen). Estamos na v0.84.

SÃO DOIS REPOSITÓRIOS AGORA, e a relação entre eles é de mão única.

O de TRABALHO é a fonte: github.com/cupcake-mochi/JJK---Project. Peças, validadores,
CHANGELOG, ESTADO-ATUAL e os DESENHO moram lá.

O de ENTREGA é artefato: github.com/cupcake-mochi/JJK---PDF---RPG. Ele é um recorte
do material de mesa, feito para o chat que vai escrever o PDF jogável. NADA NELE É
EDITADO À MÃO — correção descoberta lá se aplica na fonte e volta no recorte
seguinte. Ele mora dentro da pasta de trabalho, em finalizado/, ignorado pelo
.gitignore de lá e com .git próprio. Ele existe por um motivo medido: o repositório
de trabalho tem 2,2 MB de texto e 628 KB disso é o CHANGELOG, que para escrever texto
de mesa é ruído; a entrega tem 816 KB e nenhum byte de histórico.

A PASTA LOCAL "Claude 2" É SEMPRE A MAIS ATUALIZADA dos dois.

LEIA, NESTA ORDEM: README.md, em especial "Nove lições que custaram erro" — elas são
fonte única. Depois sistema/ESTADO-ATUAL.md INTEIRO (ele trunca; continue do offset).
Depois logs/CHANGELOG.md de cima — v0.84, v0.83 e v0.82 são as três últimas. Depois
DESENHO-trilhas.md, DESENHO-caminhos.md e DESENHO-manhas.md.

RODE OS VALIDADORES de dentro de sistema/03-mecanica/, depois conferir-repositorio.py
da raiz, depois pac7.py e v7.py de manual/matematica/. São 19. Me diga quantos
passaram e se algum imprimiu PULADA.

NÃO RODE GIT. Sai com "loose object is corrupt" e o repositório está inteiro — é o
mount. E git status cria um .git/index.lock que trava o ./subir.sh. Commit é sempre
meu, nos dois repositórios. Para ver o commit, leia .git/logs/HEAD como arquivo.

QUANDO FOR ME MOSTRAR QUALQUER COISA, diga em que estado ela está: FEITO (está no
disco, validador rodado, não preciso fazer nada), PRECISO DE VOCÊ (travado numa
decisão minha) ou SÓ PARA VOCÊ SABER (achado que você já resolveu ou vai resolver).
Mostrar problema com solução ao lado sem dizer qual dos três é me faz adivinhar.
E quando for falar do commit da entrega, me passe o comando COMPLETO com a mensagem
pronta — eu não sei o que escrever nela.

O QUE AS TRÊS ÚLTIMAS VERSÕES FIZERAM.

A v0.82 fechou a "dívida do físico", e ela NUNCA FOI DÍVIDA. Era uma frase que
ninguém tinha escrito. O ataque extra do nível 7 é um GOLPE SOLTO por rodada e não
exige a Ação de Atacar — ele acontece junto do que a Ação Padrão fez, inclusive
quando ela conjurou. Zero número se moveu. A alternativa reprova por dominância: com
o ataque extra preso à Ação de Atacar, dois golpes rendem 23 no nível 30 e um Classe
0 grátis rende 27, e o físico e o conjurador ficariam idênticos em 60,50 por rodada.
A checagem 4h do conferir-manual.py guarda a forma; a 4f guarda o número. Nessa
versão também entraram as TREZE MANHAS da Vanguarda, que fecham o nível 2 dela.

A v0.83 deu casa à lista de ações: ela é a peça 3 §3.1. As doze do 5e de 2024, lidas
na fonte — oito já existiam, entraram Influenciar (Essência é o Carisma daqui) e
Preparar, e o Search e o Study viraram Vasculhar e Estudar. O Ler o Ambiente fala do
LUGAR e nunca de criatura, e é essa linha que impede uma Ação Bônus de dominar duas
Ações Padrão. Agarrar e Derrubar viraram opção do Atacar. O Ajudar ganhou custo de
ação sete versões depois de ser escrito: é Ação Padrão.

A v0.84 escreveu as doze entregas do Guia em texto de mesa e batizou sete do
Emanador. Elo: Nó, Repasse, Partilha, Trança. Sutura: Agulha, Enxerto, Pulso,
Cerzido. Perímetro: Chão, Sentinela, Encalço, Portão. Explosivo: Pavio, Estopim,
Rompante, Ápice. Arremate: Empunhadura, Rebote, Crosta — e o nível 27 fica SEM NOME
de propósito, porque está vago com 1,26 fatia.

E ela consertou uma Trilha que entregava QUATRO VEZES o preço dela: o nível 27 da
Estocada tinha a tabela com dois gates (1,33 fatia) e o bloco de regra dizendo
"carrega SEMPRE um Classe 0" (5,31 fatias, mais que a Trilha inteira). A causa é
estrutural e continua de pé: NENHUM VALIDADOR ALCANÇA OS ARQUIVOS DESENHO-*.md.

A FILA, na ordem.

1. FALTAM 17 NOMES de entrega de Trilha: Estocada (4), Batedor (8) e cinco espalhadas
no Muro, no Punho e na Brasa. Todas já têm texto de regra — é nome e triagem, sem
buraco mecânico. De 48 entregas, 30 já têm nome.

2. A PEÇA 17, com as 81 entradas — 48 entregas de Trilha, 20 degraus de Caminho e as
13 Manhas — e o décimo sétimo validador. Ela é o que faz a checagem "tabela e bloco
de regra batem" ganhar dono. Decidido: catálogo ganha peça própria, que é o
precedente das peças 13, 14 e 15. A contagem sobe de dezesseis para dezessete peças e
validadores, e o README, o ESTADO-ATUAL e o LEIA-ME têm de subir juntos.

3. AS APTIDÕES E A TROCA DO MARCO. Do nível 22 em diante o refino topa em 10 e a
escolha "refino e uma aptidão" vira só a aptidão, enquanto Corpo e Leque valem cheio
— três marcos com um dos três eixos pela metade. A régua impossível de "uma aptidão a
mais" NÃO é a que falta: no marco a comparação é entre as três opções para o mesmo
jogador, e aí a aptidão e a Passiva se cancelam porque vivem na mesma escada. Sobra
+1 refino contra +1 atributo contra +1 feitiço, que é dominância e o projeto sabe
medir. Ressalva: a escada de Classe Passiva nunca teve os próprios exemplos preçados
— dois dos sete não sobrevivem.

O EVOCADOR ESTÁ PARADO e não morto. O §6 do RASCUNHO-trilhas.md tem cabeçalho de
parada. Ninguém vai jogar de Evocador no primeiro teste. O Servo está montado e fecha
em 5,07 contra 5,07 — falta só o gatilho do nível 27. Matilha e Coro não têm entrega
nenhuma escrita.

RÉGUAS QUE VALEM HOJE. A fatia é 5,08 de dano por rodada; a Trilha leva 5 e a banda é
4,50 a 5,00; o Caminho leva 3, em três degraus (2, 15, 30), e o nível 7 é de graça
porque vale o vão. O vão é 9 · 10 · 11 · 12 e é exatamente um golpe simples. +1 no
seu acerto vale 10,80 de dano por rodada, que é 10% da Rotina — é por isso que quase
nada que mexe no d20 cabe num degrau. Vantagem são 25 pontos percentuais. 1 ponto
percentual numa rolagem de ALIADO vale 0,230. Dano evitado converte 1 pra 1, e isso
inclui PV temporário, resistência e redução. Um Classe 0 causa 27 no nível 30 e um
Classe 2 num alvo causa os mesmos 27. A Rotina é floor(3,5 × Classe) dados. O manual
diz que um conjurador gasta PE em cerca de metade das rodadas. Chefe faz 72 de dano
por rodada no nível 30 e capanga faz 38. Uma luta dura 3,3 rodadas.

RÉGUAS QUE NÃO EXISTEM. Gastar PE não tem preço. Condição não tem conversão em fatia
— mas TIRAR condição tem preço desde a v0.84: 1 PE por nível dela, e condição sem
nível declarado conta como nível 1. E "uma aptidão a mais" não tem régua e não pode
ter: vale a Trilha inteira para quem nunca escolhe Refino e um sétimo para quem
sempre escolhe. Foi isso que matou a Trilha Repertório.

O QUE AINDA ESTÁ ERRADO NOS ARQUIVOS, e vale saber antes de publicar qualquer coisa.
A peça 6 §2 ainda lista o Repertório abandonado e nunca ouviu falar do Explosivo. O
§9 dela publica o calendário de Caminho velho, 7-15-23-29 em vez de 2-7-15-30. O
estado de 0 de vida vai virar Inconsciente e a troca não foi aplicada — ele é citado
nas peças 1, 13 e 15, e Caído virou a condição de quem foi derrubado. O .pdf do
manual está na v7.4 contra a v7.8 do .docx. São QUATRO aptidões abertas e não três: a
terceira de kokusen não tem nome e o gate é "a definir" enquanto ela é contada entre
as onze fechadas. E os metros de cada arma de projétil não existem, embora a
propriedade Longo Alcance já custe 1 ponto no orçamento das onze.

E FICA PENDURADO. A dominância do Explosivo sobre a Torrente é 1,20×, declarada.
Preparar é o quinto competidor pela Reação, num slot que a peça 3 §7 já desconfiava
com quatro. O Ler o Ambiente não tem preço — o teto de uma vez por cena é o que
segura ele. Duas ações bônus ainda é pouco. As de sempre: vagas de Desliga, Cicatriz,
clash, nome do sistema, tabela de inimigo parada, atribuição de versão sem validador.
