# Prompt para a próxima conversa
Escrito no fim da v0.92, contra o estado real. Cole isto inteiro numa conversa nova.
Renomeie o chat para: **RPG - JJK15**

---

Projeto de RPG da Guilda (Jujutsu Kaisen). Estamos na **v0.92**.

**SÃO DOIS REPOSITÓRIOS, e a relação entre eles é de mão única.** O de TRABALHO é a fonte: `github.com/cupcake-mochi/JJK---Project`. Peças, validadores, CHANGELOG, ESTADO-ATUAL e os DESENHO moram lá. O de ENTREGA é artefato: `github.com/cupcake-mochi/JJK---PDF---RPG`, um recorte do material de mesa para o chat que vai escrever o PDF. **NADA NELE É EDITADO À MÃO** — correção descoberta lá se aplica na fonte e volta no recorte seguinte. Ele mora em `finalizado/`, ignorado pelo `.gitignore` de lá e com `.git` próprio. **A PASTA LOCAL "Claude 2" É SEMPRE A MAIS ATUALIZADA dos dois.**

> **⚠ O recorte já atrasou duas versões numa sessão só.** Na v0.91 a fonte estava commitada e a entrega parada na v0.89, com os arquivos certos no disco e sem commit. **Confira os dois antes de começar:** leia `.git/logs/HEAD` e `finalizado/.git/logs/HEAD` como arquivo.

## O que mudou desde o prompt anterior, e vale saber

**O defeito de mount ACABOU.** *A v0.87 avisava que o `17-catalogo-de-entregas.md` sumia e que cinco validadores falhavam com `FileNotFoundError`.* **Na v0.88 a pasta foi alcançada pela ponte do desktop e todo arquivo abriu** — a peça 17, o `.docx` do manual, tudo. **Os vinte validadores rodaram de verdade em cinco versões seguidas, com `PULADA=0`.** *O aviso do `README` sobre o mount continua lá porque a via de acesso pode não ser a mesma que ele descreve — se ele não reproduzir de novo, apague.*

## Ordem de leitura

`README.md`, em especial **"Nove lições que custaram erro"** — fonte única. Depois `sistema/ESTADO-ATUAL.md` INTEIRO (ele trunca; continue do offset). Depois `logs/CHANGELOG.md` de cima — **v0.92, v0.91 e v0.90** são as três últimas. Depois `DESENHO-trilhas.md`, `DESENHO-caminhos.md` e `DESENHO-manhas.md`.

## Os validadores

São **20**: dezessete em `sistema/03-mecanica/`, o `conferir-repositorio.py` da raiz, e o `pac7.py` e o `v7.py` de `manual/matematica/`. **Confira `PULADA=0`** — sem `python-docx` três deles pulam checagem e saem verdes. **O `conferir-nomes.py` leva 21 segundos**, então ele não cabe junto de outro numa chamada de 45 segundos.

## NÃO RODE GIT

Sai com "loose object is corrupt" e **o repositório está inteiro** — é o mount. E `git status` cria um `.git/index.lock` que trava o `./subir.sh`. **Commit é sempre do Mizuki, nos dois repositórios.** Para ver o commit, leia `.git/logs/HEAD` como arquivo.

**Ele tem duas contas de GitHub e troca com `gh auth switch`.** Os commits do JJK precisam da `cupcake-mochi` ativa. **Quando for falar do commit da entrega, passe o comando COMPLETO com a mensagem pronta** — ele não sabe o que escrever nela. O da fonte é `jjk` e `./subir.sh`, com a mensagem deixada em `mensagem-de-commit.txt`.

## COMO FALAR COM ELE

**Diga em que estado está cada coisa que você mostrar: FEITO, PRECISO DE VOCÊ ou SÓ PARA VOCÊ SABER.**

Uma ideia por parágrafo, frase curta. Nada de `§3.4` no meio da frase. Número sempre com a unidade por extenso. Escolha de sabor é dele — traga as opções com o número e o trade-off já calculados. **Mas não pergunte o que a conta responde.**

---

# ⚠⚠ A LIÇÃO DESTA LEVA, E ELA APARECEU TRÊS VEZES

**O número que o projeto procura muitas vezes já tem dono, e o dono é o manual.**

| versão | o que "faltava" | onde estava |
|---|---|---|
| v0.80 | o dano de um Classe 0 | tabela própria no manual, que nenhum documento abria |
| v0.86 | a regra da ação `Mirar` | em lugar nenhum — treze menções concedendo, nenhuma definindo |
| **v0.92** | **a régua do `Efeito Próprio`** | **numa tabela de Melhorias do manual, com o desempate incluído** |

**Antes de escrever régua nova, abra o `.docx` e procure o termo exato.** *A v0.92 gastou sessenta versões de "falta a régua" para uma frase que estava publicada.*

# E A OUTRA, QUE É DE VALIDADOR

**Checagem escrita no braço para UM caso deixa os outros treze descobertos.** *Na v0.90 a comparação do gate do título contra o gate do catálogo existia só para a `Energia Reversa`; perturbando o gate de outra entrada, o validador saía verde.* **Generalize na hora de escrever, e ponha guarda de contagem** — se o número de pares cair, a checagem acusa em vez de conferir menos em silêncio.

---

# O QUE AS CINCO ÚLTIMAS VERSÕES FIZERAM

**v0.88 — quatro dívidas antigas, e a mais velha não era o que estava escrito.** *`Caído` virou `Inconsciente` no estado de 0 de vida; o `Abalo` das Manhas passou a aplicar o `Derrubado`, que é condição do manual e que a v0.74 já tinha adotado no `Punho` — a v0.82 reabriu a colisão por outra porta.* **E a causa era buraco de validador: a triagem era cega para as doze condições do manual, e ONZE voltavam `LIVRE`.** *O `Repertório` saiu da peça 6 e de mais seis lugares; a peça 6 parou de publicar o calendário de Caminho aposentado; `Quick Draw` virou `Descarga` e o sistema não tem mais nome em inglês.*

**v0.89 — a troca do marco.** *A escolha de `Refino` promete "mais um de refino, e uma aptidão" e entregava só a aptidão nos marcos 22, 26 e 30.* **A causa medida: a linha de graça do marco entrega `8` dos `10` de refino sozinha, então a metade "mais um de refino" só tem `2` pontos de espaço na campanha inteira.** ***Decisão do Mizuki: no teto, a escolha leva DUAS aptidões.*** **E a checagem 5.2 passou a medir MARCO A MARCO** — a 5 media o fim da campanha e saía verde com o meio quebrado.

**v0.90 — a terceira de kokusen virou `Kokusen Constante`.** *Ninguém tinha escrito se as três empilham; sem empilhar, a terceira é 17% pior que a `Melhorado` pelo mesmo marco.* ***Decisão: empilham*** — a base sobe para `3 × refino` e a vantagem rola em cima, `51%` no d100 no refino 10. **Gate `refino 5` sem gate de nível, derivado.** *E a trava do kokusen passou a medir a PILHA por marco em vez da entrada.*

**v0.91 — as duas barreiras, e o catálogo quase fechou.** ***"Se não vira uma vida extra paia"*** *— e a conta concorda: dano evitado converte `1` pra `1`, então uma barreira **evita a própria vida**.* **A rodada inteira não gateia; o que gateia é `1 minuto`, dez rodadas contra uma luta de `3,3`.** *`Barreira Simples`, sem gate, `5 × refino` de vida, raio `6 m`. `Cortina`, que **exige a `Barreira Simples`**, `20 × refino` de vida, uma condição sobre quem atravessa.* **E entrou o QUINTO formato de gate, que a v0.90 tinha recusado — a diferença ficou escrita: alternativa é pedágio, escada não é.**

**v0.92 — a `Aptidão Própria`, e o catálogo fechou.** *As catorze entradas têm regra, gate e validador.* **A régua era do manual; as três faixas de frequência caem exatamente nos três degraus da escada de Classe Passiva.** *Cinco requisitos, e o que faz ela sobreviver a sete mesas é a ficha carregar a RESPOSTA da pergunta de frequência e não só o texto.* **Na dúvida a proposta é RECUSADA** — é o único lugar do sistema em que "não sei" tem resposta escrita.

---

# RÉGUAS QUE VALEM HOJE

A **fatia** é `5,08` de dano por rodada. A Trilha leva `5` e a banda é `4,50` a `5,00`; o Caminho leva `3`, em três degraus (`2 · 15 · 30`), e o nível 7 é de graça porque vale o vão. **O vão é `9 · 10 · 11 · 12` e é exatamente um golpe simples.** **O degrau de Caminho é `2 · 7 · 15 · 30`, e o dono é o `DESENHO-caminhos.md`.**

**`+1` no seu acerto vale `10,80` de dano por rodada**, que é 10% da Rotina. **Vantagem são 25 pontos percentuais.** **Dano evitado converte 1 pra 1**, e isso inclui PV temporário, resistência e redução.

> **⚠ E o corolário disso, medido na v0.91: uma barreira com vida EVITA A PRÓPRIA VIDA.** *`vida ÷ 3,3 rodadas ÷ 5,08` dá as fatias.* **Duzentos de vida são `9,84` fatias contra uma Trilha de `5,00`.** *Toda vez que aparecer ponto de vida que não seja do personagem, rode essa conta primeiro.*

**Um marco compra `+1` de atributo, que são `+10%` de dano por rodada = `2,13` fatias.**

**Um Classe 0 causa `27` no nível 30, e um Classe 2 num alvo causa os mesmos `27`.** A Rotina é `floor(3,5 × Classe)` dados. **Chefe faz `72` por rodada no nível 30 e capanga faz `38`. Uma luta dura `3,3` rodadas, e o dia tem `13`.**

**Tirar condição custa `1` PE por nível dela.** **O manual tem doze condições**, sete Menores e cinco Maiores, e desde a v0.88 a triagem conhece as doze.

# RÉGUAS QUE NÃO EXISTEM

**Gastar PE não tem preço. Condição não tem conversão em fatia. Cobertura não existe como regra.** E **"uma aptidão a mais" não tem régua e não pode ter** — foi isso que matou o `Repertório`. *Na v0.89 ela apareceu de novo e foi aceita, com o motivo escrito: no marco quem recebe a aptidão a mais já escolheu esse eixo cinco vezes.*

---

# O QUE FICA ABERTO, POR TAMANHO

## O que impede alguém de sentar na mesa — e nada disso é regra

- **Quick-start jogável.** *Não existe. As dezessete peças são argumento de design, não texto de mesa.*
- **Tabela de progressão consolidada.** *O que se ganha em cada nível está espalhado por cinco documentos.*
- **Playtest.** *`04-playtest/` vazia, zero sessões desde a v0.1. **Todo número do sistema é previsão.***

## Regra que falta

- **A peça de dano e condições.** ***18 lugares em 8 documentos esperam por ela** — é a maior dívida estrutural do projeto.* Ela carrega a **Cicatriz**, a lista de condições com nível, o **clash** e as vagas de `Desliga`.
- **As três Trilhas do Evocador.** *Paradas desde a v0.82. O `Servo` está montado em `5,07` contra `5,07` e falta o gatilho do nível 27; ele está dominado pela `Matilha` e pelo `Coro` **por falta de eixo, não por sobra de número**.* **Quando as três voltarem, o total da peça 17 sai de 89 e a checagem 1 acusa.**
- **Cobertura**, e **os metros de cada arma de projétil** — a propriedade `Longo Alcance` já custa 1 ponto e nenhuma arma tem metro.

## Pendência pequena

- ~~Duas entregas com nome em minúscula.~~ **Fechadas na v0.93:** `Disparo Carregado` e `Acelerar`.
- ~~As quatro anti-domínio escrevem `Classe 1/2/3` solto.~~ **Fechado na v0.93, e eram TREZE lugares e não oito** — a contagem à mão pegou os títulos e a tabela, e deixou cinco de fora.
- ~~O `.pdf` do manual está na v7.4.~~ **Fechado na v0.93:** os dois na v7.8, e ele saiu do `soffice --headless` em vez do Word.
- **A terceira taxa do `Batedor`:** *em quantas rodadas o atirador fica parado.* **Decide `2,12` fatias — e não é conta, é pergunta de mesa.**
- ~~O nome do sistema.~~ **`Projeto - M`, na v0.94.**
