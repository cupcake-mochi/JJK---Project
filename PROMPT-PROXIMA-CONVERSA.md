# Prompt para a próxima conversa
Escrito no fim da v0.100, contra o estado real. Cole isto inteiro numa conversa nova.
Renomeie o chat para o próximo número da sua sequência. *O último que teve nome escrito foi o **RPG - JJK15**, na v0.92.*

---

Projeto de RPG da Guilda (Jujutsu Kaisen), chamado **Projeto - M**. Estamos na **v0.100**.

**O número pulou de `0.99` para `0.100` e não para `1.00`, e foi decisão dele.** *`1.0` costuma querer dizer pronto para usar, e o playtest tem zero sessões.*

**SÃO DOIS REPOSITÓRIOS, e a relação entre eles é de mão única.** O de TRABALHO é a fonte: `github.com/cupcake-mochi/JJK---Project`. Peças, validadores, CHANGELOG, ESTADO-ATUAL e os DESENHO moram lá. O de ENTREGA é artefato: `github.com/cupcake-mochi/JJK---PDF---RPG`, um recorte do material de mesa para o chat que vai escrever o PDF. **NADA NELE É EDITADO À MÃO, com UMA exceção: o `README.md` dele**, que não existe na fonte. Ele mora em `finalizado`, ignorado pelo `.gitignore` de lá e com `.git` próprio. **A PASTA LOCAL "Claude 2" É SEMPRE A MAIS ATUALIZADA dos dois.**

> **Os dois estavam na v0.100 no disco quando isto foi escrito, e o commit é dele.** *Confira antes de começar: leia o `logs/HEAD` de dentro do `.git` de cada um como arquivo. O recorte já atrasou duas versões numa sessão só.*

## ⚠ O MOUNT — e o aviso da v0.99 NÃO reproduziu na v0.100

**A v0.99 escreveu que escrever no mount dá ENOENT e que só a ponte do desktop atravessa. Na v0.100 nada disso aconteceu.** *Medido: 157 arquivos lidos por `md5sum`, 23 arquivos escritos, um arquivo movido, e o `conferir-repositorio.py` rodou inteiro na máquina dele.*

**Aviso que parou de reproduzir é dívida — mas não apague este ainda**, porque a v0.99 mediu o contrário e nada explica a diferença. *O que ficou de fora do teste: a ferramenta de escrita apontada direto para o mount. Isso continua sem medida, e é justamente o que a v0.34 acusou.*

**O método que funcionou, e é o que eu recomendo repetir:**

1. **Clone os dois repositórios do GitHub para dentro do container** e trabalhe lá. `git`, `python3` e os validadores rodam sem drama.
2. **Confira o disco contra o GitHub antes de começar**, por `md5sum` arquivo a arquivo. Dá para rodar o `md5sum` na máquina dele e comparar com o do container.
3. **Para escrever de volta:** mande o arquivo pelo painel e depois grave no caminho do disco, com `force`. **Depois confira `md5sum` dos dois lados, arquivo a arquivo.** *A prova de que o trabalho está certo é o md5.*
4. **Você não consegue apagar arquivo do mount, mas consegue MOVER.** *Mande o lixo para a pasta `_to_delete`, que é ignorada pelo git, e peça para ele apagar a pasta na mão.*

## Ordem de leitura

`README.md`, em especial **"Nove lições que custaram erro"** — fonte única. Depois `sistema/ESTADO-ATUAL.md` INTEIRO (ele trunca; continue do offset). Depois `logs/CHANGELOG.md` de cima — **v0.100, v0.99 e v0.98** são as três últimas. Depois os três `DESENHO`: trilhas, caminhos e manhas.

## Os validadores

São **21**: dezoito em `sistema/03-mecanica`, o `conferir-repositorio.py` da raiz, e o `pac7.py` e o `v7.py` de `manual/matematica`. **O `conferir-nomes.py` leva 21 segundos**, então ele não cabe junto de outro numa chamada curta.

```bash
cd sistema/03-mecanica && for v in conferir-*.py; do python3 "$v"; done
cd ../..  && python3 conferir-repositorio.py
cd manual/matematica && for v in pac7.py v7.py; do python3 "$v"; done
```

**⚠ CINCO validadores leem o `.docx` do manual, e sem o `python-docx` eles pulam checagem.** *Eram três até a v0.96; o `conferir-atributos` entrou na v0.97 e o `conferir-progressao` na v0.99.* **A tabela de quanto cada um pula está no `README` e no `ESTADO-ATUAL`, e a v0.100 corrigiu as duas.**

**E dois deles mentem no rodapé:** o `conferir-nomes` e o `conferir-pericias` imprimem `TUDO OK` estando cegos. **Confira `PULADA` lendo a saída, não o código de retorno.** *Pôr a pulada visível nos dois é item aberto desde a v0.97.*

*No container: `pip install python-docx --break-system-packages`.*

## NÃO RODE GIT NA PASTA DELE

Sai com "loose object is corrupt" e **o repositório está inteiro** — é o mount. E `git status` cria um lock dentro do `.git` que trava o `subir.sh`. **Commit é sempre do Mizuki, nos dois repositórios.** Para ver em que commit a pasta está, leia o `logs/HEAD` de dentro do `.git` como arquivo.

*No container, num clone do GitHub, o git funciona normalmente. Use isso.*

**Ele tem duas contas de GitHub e troca com `gh auth switch --user cupcake-mochi`.** O da fonte é `jjk` e `./subir.sh`, com a mensagem deixada em `mensagem-de-commit.txt`. **O da entrega precisa do comando COMPLETO com a mensagem pronta** — ele não sabe o que escrever nela.

## COMO FALAR COM ELE

**Diga em que estado está cada coisa que você mostrar: FEITO, PRECISO DE VOCÊ ou SÓ PARA VOCÊ SABER.**

Uma ideia por parágrafo, frase curta. Nada de ponteiro de seção no meio da frase. Número sempre com a unidade por extenso. Termo do projeto vem com a tradução colada na primeira vez. **Escolha de sabor é dele — traga as opções com o número e o trade-off já calculados. Mas não pergunte o que a conta responde.**

**Quando ele disser que não entendeu, procure o defeito antes de reexplicar.** *Nas duas últimas vezes ele estava certo, e reexplicar melhor teria enterrado os dois achados.*

---

# ⚠⚠ A LIÇÃO DESTA LEVA

**Uma peça pode se contradizer sozinha, e nada acusa.**

**A peça 11 pedia, na lista de pendências, as quatro anti-domínio que a seção 6.5 dela publica desde a v0.29.** *E a abertura da seção 6, no mesmo arquivo, já dizia que elas saíram naquela versão.* **A peça 13 fez o mesmo em três itens.**

*A leitura fácil era "lista velha aponta para fora e envelhece devagar". É pior:* **uma lista que ninguém lê não envelhece, ela para.** *Onze itens vivos pediam coisa que já existe, e o mais velho estava assim havia sessenta versões.*

# E A SEGUNDA, QUE É DE MÉTODO

**Um arnês que lê o código de retorno do script inteiro mente.**

*Perturbar uma peça também deixa a cópia dela na entrega velha, e isso acende a checagem 7.* **Duas perturbações da checagem 8 saíam "acende" sem a checagem 8 ter acusado nada.** *Com o veredito lido da checagem certa, duas das quatro sub-regras não acendiam.*

**Leia o veredito da checagem que você está testando, nunca o do programa.**

---

# O QUE AS TRÊS ÚLTIMAS VERSÕES FIZERAM

**v0.98 — a entrega estava certa nas cópias e errada em tudo que não é cópia.** *As 25 cópias batiam byte a byte e mesmo assim ela mandava abrir 19 arquivos que não estavam lá.* **Nasceu a checagem 7**, a única coisa do projeto que atravessa os dois repositórios.

**v0.99 — a tabela de progressão virou a peça 18.** *Ela não estava espalhada por cinco documentos: eram dez números em seis lugares, e um deles não tinha dono.* **Uma tabela só, trinta linhas, nove colunas.** *E o achado: a fórmula do tamanho da lista de feitiços estava escrita à mão dentro de dois validadores e em documento nenhum.*

**v0.100 — as listas "Em aberto" mentiam em onze lugares.** *Riscados os onze, mais cinco fora das peças, mais quatro pendências que continuavam abertas com o motivo escrito errado.* **Nasceu a checagem 8**, com quatro sub-regras e nove perturbações. *E a contagem de validadores que leem o manual saiu de três para cinco em dois documentos.*

---

# RÉGUAS QUE VALEM HOJE

A **fatia** é `5,08` de dano por rodada. A Trilha leva `5` e o Caminho leva `3`. **O degrau de Caminho é `2 · 7 · 15 · 30` e a entrega de Trilha é `2 · 11 · 19 · 27`**, e o dono dos dois é a linha de orçamento do topo do desenho de caminhos.

**O vão `físico − conjurador` é `9 · 10 · 11 · 12`**, e é exatamente um golpe simples. **`+1` no seu acerto vale `10,80` de dano por rodada.** **Vantagem e rerrolar valem os mesmos `25` pontos percentuais.** **Dano evitado converte 1 pra 1**, e isso inclui PV temporário, resistência e redução — *uma barreira com vida evita a própria vida.*

**Um marco compra `+1` de atributo, que são `2,13` fatias.** **Um Classe 0 causa `27` no nível 30.** A Rotina é `floor(3,5 × Classe)` dados. **Chefe faz `72` por rodada no nível 30 e capanga faz `38`. Uma luta dura `3,3` rodadas.**

**Tirar condição custa `1` PE por nível dela.** **O manual tem catorze condições**, nove Menores e cinco Maiores, e a seção 8.3 da peça 1 é a dona.

**Espaços de feitiço conhecido = `2 + nível ÷ 2`, mais `1` por marco. Dono: a peça 18**, desde a v0.99.

# RÉGUAS QUE NÃO EXISTEM

**Gastar PE não tem preço. Condição não tem conversão em fatia. E "uma aptidão a mais" não tem régua** — foi isso que matou o `Repertório`.

---

# O QUE FICA ABERTO, POR TAMANHO

**Nada trava jogar.** *Uma ficha de nível 2 fecha, roda uma missão inteira e sobe de nível.*

## Regra que falta

- **A peça de dano e condições.** ***19 lugares em 8 documentos esperam por ela** — é a maior dívida estrutural.* Carrega a **Cicatriz**, o **clash** e três vagas de `Desliga`.
- **As três Trilhas do Evocador** — `Servo`, `Matilha` e `Coro`. *Paradas desde a v0.82.* **Decisão dele: ficam por último.** *Quando voltarem, o total de 89 entradas da peça 17 muda e a checagem 1 acusa.*
- **A terceira taxa do `Batedor`:** em quantas rodadas o atirador fica parado. **Decide `2,12` fatias — e não é conta, é pergunta de mesa.**

## Material que falta, e não é regra

- **Quick-start jogável.** *Não existe.* **É o que impede alguém de sentar na mesa.** *A skill de redação acessível existe para essa travessia e nunca foi rodada contra o material.*
- **Playtest.** *A pasta de playtest está vazia desde a v0.1.* **Todo número do sistema é previsão.**

## Pendência pequena

- **Duas vagas de `Desliga` destravaram na v0.59 e ninguém voltou.** *Elas esperavam a ferramenta amaldiçoada — a `Armaria` do Descendente e a Restrição Celestial —, e a peça 16 registra que destrava as duas.* **Escrever as duas é trabalho, não conserto de texto.**
- **Quem é a próxima peça está escrito de dois jeitos.** *A fila do `ESTADO-ATUAL` diz Trilhas; a peça 16 diz que a Técnica Marcial é a peça seguinte.* **É pergunta para ele.**
- **Os dois validadores que dizem `TUDO OK` estando cegos.**
- **A perícia livre da Origem** — último lugar da criação em que um número depende de julgamento do mestre.
- **Como a `Torrente` cobra o segundo feitiço da rodada**, contra a regra de ouro no 6.
- **O ofício não passa no filtro multi-mestre.** *Conserto escrito: tabela com o atributo padrão de cada um.*
- **A curva de refino das três rotas ainda mora no esqueleto**, que é documento de projeto e não peça. *É a última fonte da progressão fora de uma peça, e o candidato natural é a peça 11.*

## Peças que ainda nem entraram na fila

**Técnica Marcial** e **Estilo da Sombra** (as duas destravam rotas de Origem), depois **Objeto amaldiçoado**, **Dano de alma com Essência na Integridade**, **Pactos** e **Bestiário**.

---

# ⚠ A PRIMEIRA COISA A FAZER, SE ELE NÃO PEDIR OUTRA

**A contagem de checagens de cada validador é número de dois donos, e ninguém confere.**

*A v0.100 achou duas erradas de passagem: o `conferir-equipamento` publicado como dez sendo onze, e o `conferir-catalogo` publicado como dez num lugar e nove em outro, sendo onze.* **Isso é a lição nº 9 num eixo que nenhuma checagem alcança**, e a conta é barata: contar os blocos numerados de cada validador e comparar com o que os documentos afirmam.

**Vale junto: pôr o `PULADA` visível no rodapé do `conferir-nomes` e do `conferir-pericias`.** *É o item mais velho da lista pequena, e ele existe desde a v0.97.*
