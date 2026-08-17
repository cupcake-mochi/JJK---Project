# Prompt para a próxima conversa

*Escrito no fim da v0.81, contra o estado real. Cole isto inteiro numa conversa nova.*

---

Renomeie este chat para: RPG - JJK12
Projeto RPG da Guilda (JJK), pasta local "Claude 2". Estamos na v0.81.

LEIA, NESTA ORDEM: README.md, em especial "Nove lições que custaram erro" — elas são
fonte única. Depois sistema/ESTADO-ATUAL.md INTEIRO (ele trunca; continue do offset).
Depois logs/CHANGELOG.md de cima — v0.81 e v0.80 são as duas últimas, e a v0.81 é longa
de propósito. Depois DESENHO-trilhas.md e DESENHO-caminhos.md.

RODE OS VALIDADORES de dentro de sistema/03-mecanica/, depois conferir-repositorio.py da
raiz, depois pac7.py e v7.py de manual/matematica/. São 19. Me diga quantos passaram e se
algum imprimiu PULADA.

NÃO RODE GIT. Sai com "loose object is corrupt" e o repositório está inteiro — é o mount.
E git status cria um .git/index.lock que trava o ./subir.sh. Commit é sempre meu. Para ver
o commit, leia .git/logs/HEAD como arquivo.

O QUE A v0.81 FEZ, em quatro blocos.

UM — o teto da régua de Trilhas não existe, e isso está medido. Sem o "+18%" que morreu,
as outras quatro travas não reprovam em orçamento nenhum de 1× a 8×. Três candidatos a
teto novo foram testados e derrubados: dois têm dono no playtest, e o único que reconstrói
sem playtest só acende a 10,45× do orçamento atual. Contra-teste: o +18%, se estivesse
vivo, reprovaria a partir de 3×. Decisão minha: o teto fica DECLARADO como decisão de
design — 4×, que é 27,7% da ficha — em vez de vestido de conta.

DOIS — o Classe 0 fantasma de 4,50 tinha pegado mais coisa. A v0.80 corrigiu a tabela e
repreçou só o Arremate; cinco entregas de outras três Trilhas foram CALCULADAS a partir do
4,50 e nunca refeitas. Torrente 5,37 → 4,65, Estocada 4,58 → 5,02, Brasa 5,03 → faixa de
7,06 a 9,42 com estouro aceito. As três matrizes ficaram limpas.

TRÊS — o "golpe canalizado" NUNCA EXISTIU. Zero ocorrências no manual, 60 usos no projeto.
Era abreviação de "feitiço de Forma Toque", e a palavra "golpe" fez um feitiço parecer
ataque. Trocado por "feitiço de Toque" em 39 lugares, SEM MEXER EM NÚMERO.

QUATRO — o Emanador fechou. O Repertório foi abandonado e no lugar entrou o Explosivo,
em 5,57 de 5,00.

O PRIMEIRO ITEM SÃO AS TRÊS TRILHAS DO EVOCADOR — Servo, Matilha e Coro. Elas são o
sistema de invocação visto de dentro, e a peça 15 é a dona da máquina. O RASCUNHO-trilhas
§6 tem o levantamento inteiro delas, incluindo a régua da camada de vínculo que a v0.68
fechou, e o Servo já está montado no §6.10 como prova de método. Com elas as quinze fecham.

A DÍVIDA DO FÍSICO FECHOU NA v0.82, e ela nunca foi dívida. A peça 6 §3.1 sempre teve a
linha "feitiço de Toque + golpe simples" marcada como EXISTENTE na tabela dos três turnos —
faltava dizer de onde vinha o golpe. Vem do ataque extra do nível 7, que é um GOLPE SOLTO
por rodada e não exige a Ação de Atacar. Zero número se moveu: o vão continua 9-10-11-12, o
nível 7 continua de graça nos cinco Caminhos, o Arremate e o Resquício continuam iguais. A
alternativa reprova por dominância: com o ataque extra preso à Ação de Atacar, dois golpes
dão 23 no nível 30 contra 27 de um Classe 0 grátis, e o físico e o conjurador ficam
idênticos em 60,50 por rodada. A checagem 4h do conferir-manual.py guarda a forma com sete
perturbações; a 4f guarda o número.

RÉGUAS QUE VALEM HOJE. A fatia é 5,08 de dano por rodada, a Trilha leva 5 e a banda é 4,50
a 5,00; o Caminho leva 3. O vão publicado é 9 · 10 · 11 · 12 e é exatamente um golpe simples
— e é ele que a dívida acima ameaça. Um Classe 0 causa 27 no nível 30 (manual, 2d8 a 6d8
por faixa), e "ganha um Classe 0 por rodada" vale 5,31 fatias, que é mais que uma Trilha —
nenhuma entrega pode dar isso sem gate ou relógio. No nível 30 um Classe 0 e um Classe 2
num alvo causam OS DOIS 27. Dano evitado converte 1 pra 1. Rerrolar e dar vantagem valem os
mesmos +25 pontos percentuais. A Rotina é floor(3,5 × Classe) dados. O manual diz que um
conjurador gasta PE em cerca de metade das rodadas — essa taxa tem dono e é dele.

RÉGUAS QUE NÃO EXISTEM. Gastar PE não tem preço por construção — o câmbio de 5,14 saiu dos
próprios feitiços. `condição` não tem conversão em fatia. E "uma aptidão a mais" não tem
régua e NÃO PODE TER: ela vale a Trilha inteira para quem nunca escolhe Refino e um sétimo
para quem sempre escolhe. Foi isso que matou o Repertório.

DOIS ERROS DE MÉTODO QUE EU PEGUEI NA v0.81, e que vão voltar. Preço de entrega OPCIONAL se
mede como botão × TAXA, e não comparando pico com pico — foi assim que a Brasa apareceu
valendo zero. E deriva se mede a partir do nível em que a entrega CHEGA, não do nível 2 —
foi assim que "somar atributo no dano" apareceu reprovando quando passa com folga.

E FICA PENDURADO. A dominância do Explosivo sobre a Torrente é 1,20×, declarada. O nível 27
do Arremate está VAGO com 1,26 fatia. As duas decisões de nível 7 tomadas contra o vão
errado continuam marcadas e não desfeitas — o Guia em 11,50 contra 12, e a Coleira do
Evocador em 10,80. O nível 19 da Brasa é FAIXA e não número, e o que decide é o que o
jogador monta. A lista de ações não está em peça numerada — ela mora no fim do
DESENHO-caminhos.md e nove Trilhas apontam para ela. Nenhum validador lê a regra de ouro
nº 6. Atribuição de versão não tem validador. As de sempre: vagas de Desliga, Cicatriz,
clash, nome do sistema, refino que paga mal no marco, tabela de inimigo.

https://github.com/cupcake-mochi/JJK---Project.git
