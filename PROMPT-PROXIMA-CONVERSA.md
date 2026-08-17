# Prompt para a próxima conversa

Escrito no fim da v0.87, contra o estado real. Cole isto inteiro numa conversa nova.
Renomeie o chat para: **RPG - JJK14**

---

Projeto de RPG da Guilda (Jujutsu Kaisen). Estamos na **v0.87**.

**SÃO DOIS REPOSITÓRIOS, e a relação entre eles é de mão única.** O de TRABALHO é a fonte: `github.com/cupcake-mochi/JJK---Project`. Peças, validadores, CHANGELOG, ESTADO-ATUAL e os DESENHO moram lá. O de ENTREGA é artefato: `github.com/cupcake-mochi/JJK---PDF---RPG`, um recorte do material de mesa para o chat que vai escrever o PDF. **NADA NELE É EDITADO À MÃO** — correção descoberta lá se aplica na fonte e volta no recorte seguinte. Ele mora em `finalizado/`, ignorado pelo `.gitignore` de lá e com `.git` próprio. **A PASTA LOCAL "Claude 2" É SEMPRE A MAIS ATUALIZADA dos dois.** Os dois estão commitados na v0.87.

## ⚠ LEIA ISTO ANTES DE RODAR QUALQUER COISA

**O mount perdeu o `sistema/03-mecanica/17-catalogo-de-entregas.md` na v0.87.** O `ls` e o `stat` mostram o arquivo com tamanho certo e o `open()` devolve ENOENT — é o defeito documentado no README, e **o conteúdo está íntegro no disco**. Do lado do Mizuki, fora do sandbox, ele abre normal.

**Consequência: cinco validadores falham no sandbox com `FileNotFoundError` nesse arquivo** — `conferir-catalogo`, `conferir-nomes`, `conferir-descanso`, `conferir-orcamento` e `conferir-repositorio`. **Não são falhas de regra.** Para verificar de verdade, monte a árvore num lugar limpo e traga a peça 17 do recorte, que é legível:

```bash
cd "/media/mizuki/HD Externo II/Claude/Claude 2"
rm -rf /tmp/verif && mkdir -p /tmp/verif
tar cf - --exclude='.git' --exclude='_backup' --exclude='_to_delete' --exclude='node_modules' \
   --exclude='sistema/03-mecanica/17-catalogo-de-entregas.md' . | (cd /tmp/verif && tar xf -)
cp finalizado/regra/17-catalogo-de-entregas.md /tmp/verif/sistema/03-mecanica/
```

**Se o arquivo voltar a abrir sozinho, apague este aviso.** Aviso que parou de reproduzir é dívida.

**E NÃO SONDE A PASTA COM ARQUIVO QUE VOCÊ NÃO CONSEGUE APAGAR.** Eu criei um arquivo de sonda com dois dígitos na frente para diagnosticar isso, e ele contou como peça na varredura, quebrando a contagem. O sandbox não apaga nada — só dá para mover para `_to_delete/`. *E o nome da sonda também não pode ser citado num documento: a checagem 5 do `conferir-repositorio.py` procura todo ponteiro de arquivo e falha quando ele não resolve.*

## Ordem de leitura

`README.md`, em especial **"Nove lições que custaram erro"** — fonte única. Depois `sistema/ESTADO-ATUAL.md` INTEIRO (ele trunca; continue do offset). Depois `logs/CHANGELOG.md` de cima — **v0.87, v0.86 e v0.85** são as três últimas. Depois `DESENHO-trilhas.md`, `DESENHO-caminhos.md` e `DESENHO-manhas.md`.

## Os validadores

São **20**: dezessete em `sistema/03-mecanica/`, o `conferir-repositorio.py` da raiz, e o `pac7.py` e o `v7.py` de `manual/matematica/`. **Confira `PULADA=0`** — sem `python-docx` três deles pulam checagem e saem verdes. **O `conferir-nomes.py` leva 21 segundos** desde a v0.87, porque ele varre 61 nomes contra mais arquivos.

## NÃO RODE GIT

Sai com "loose object is corrupt" e **o repositório está inteiro** — é o mount. E `git status` cria um `.git/index.lock` que trava o `./subir.sh`. **Commit é sempre do Mizuki, nos dois repositórios.** Para ver o commit, leia `.git/logs/HEAD` como arquivo.

**Ele tem duas contas de GitHub e troca com `gh auth switch`, que vai direto sem menu.** Os commits do JJK precisam da `cupcake-mochi` ativa. **Quando for falar do commit da entrega, passe o comando COMPLETO com a mensagem pronta** — ele não sabe o que escrever nela. O da fonte é `jjk` e `./subir.sh`, com a mensagem deixada em `mensagem-de-commit.txt`.

## COMO FALAR COM ELE

**Diga em que estado está cada coisa que você mostrar: FEITO, PRECISO DE VOCÊ ou SÓ PARA VOCÊ SABER.** Mostrar problema com solução ao lado sem dizer qual dos três é o faz adivinhar.

Uma ideia por parágrafo, frase curta. Nada de `§3.4` no meio da frase. Número sempre com a unidade por extenso. Escolha de sabor é dele — traga as opções com o número e o trade-off já calculados. **Mas não pergunte o que a conta responde.**

---

# O QUE FAZER NESTA CONVERSA

**Quatro dívidas antigas, todas mecânicas, numa versão só.** Nenhuma pede decisão de design — é aplicar coisa já decidida. Ele escolheu isto de propósito, para fechar uma versão barata antes de entrar na parte cara.

### 1. `Caído` vira `Inconsciente` no estado de 0 de vida

**A decisão é da v0.82 e nunca foi aplicada.** O motivo: `Caído` virou a condição de quem foi derrubado, que o `Abalo` das Manhas aplica. Duas coisas com o mesmo nome.

**Onde está, conferido na v0.87:**

| arquivo | linha | o que é |
|---|---|---|
| `01-atributos-acerto-defesa.md` | 274 | o título da seção **5.5**, que é a máquina de estado |
| `01-atributos-acerto-defesa.md` | 376 | *"Caído não é a condição Incapacitado"* |
| `13-legados.md` | 636 | a mesma frase, citando a peça 1 §5.5 |
| `15-invocacoes.md` | 106 e 548 | *"sem Caído, sem Sequela, sem Cicatriz"* |

**⚠ Cuidado, e é o ponto que decide o trabalho:** nem toda menção a `Caído` é o estado de 0 de vida. A condição de derrubado também se chama `Caído` e **essa fica** — ela aparece no `Abalo` das Manhas, no nível 11 do `Punho` e no nível 27 do `Muro`. **Separe as duas antes de trocar qualquer coisa.** Renomear a errada é pior que não renomear.

E o `conferir-atributos.py` tem seis checagens em cima da 5.5, então elas vão junto.

### 2. A peça 6 §2 ainda lista o `Repertório`

**Linha 83:** `| **Repertório** | aptidões extras — nunca refino |`. Ele foi **abandonado na v0.81** e substituído pelo **`Explosivo`**, e a palavra `Explosivo` **não aparece naquela peça nenhuma vez**.

**Ele sobreviveu em mais três lugares**, conferidos na v0.87: `sistema/05-material/gerador-ficha/dados.js`, `conferir-nomes.py` e `conferir-pericias.py`.

> **Uma consequência boa:** o `Repertório` está hoje na lista `TRILHAS` do `conferir-nomes.py`, então a triagem devolve o nome como `OCUPADO`. **Tirando ele de lá, o nome fica LIVRE de novo** — e a ficção dele é boa e pode voltar num Caminho que tenha coluna para ela.

### 3. O calendário velho de Caminho na peça 6

**O degrau de Caminho é `2 · 7 · 15 · 30` desde a v0.70.** A peça 6 ainda publica `7 · 15 · 23 · 29` em dois lugares, e **eles não são iguais**:

- **Linha 380, no §9:** apresentado como fato fechado — *"Fechada na v0.55 e na v0.60: (…) degrau de Caminho em `7 · 15 · 23 · 29`"*. **Este está errado e é o que precisa mudar.**
- **Linha 143:** dentro de bloco de citação que explica história — *"E ela pôs os degraus de Caminho em `7 · 15 · 23 · 29`"*, descrevendo o que a Q2 decidiu na época. **Este é registro legítimo**, e o conserto é marcá-lo como superado, não apagá-lo.

### 4. `Quick Draw` é o único nome em inglês do sistema

Nível 19 da rota `Arma de Fogo` do `Batedor`, **7 ocorrências** no `DESENHO-trilhas.md`. Todo o resto do projeto é português. **Rode a triagem antes de batizar** — e lembre que ela não pega colisão de sentido nem eco de nome aposentado.

---

# DEPOIS DESTAS, A GRANDE

**A troca do marco, e ela é o único problema de design que sobrou.** Do nível 22 em diante o refino topa em 10 e a escolha *"refino e uma aptidão"* vira só a aptidão, enquanto Corpo e Leque valem cheio — **três marcos com um dos três eixos pela metade.**

**A régua impossível de "uma aptidão a mais" NÃO é a que falta.** No marco a comparação é entre as três opções para o mesmo jogador, e aí a aptidão e a Passiva se cancelam porque vivem na mesma escada. Sobra `+1` refino contra `+1` atributo contra `+1` feitiço, que é dominância e o projeto sabe medir.

**Ressalva que morde: a escada de Classe Passiva nunca teve os próprios exemplos preçados — dois dos sete não sobrevivem.**

---

# O QUE A v0.87, A v0.86 E A v0.85 FIZERAM

**A v0.85 deu dono à contagem e criou a peça 17**, que é um índice das **89 entradas** — 56 entregas de Trilha, 20 degraus de Caminho e as 13 Manhas. **Ela não guarda preço nem texto de mesa**, só nome e ponteiro; os dois continuam nos `DESENHO-*.md`. **O `conferir-catalogo.py` é o primeiro validador que sai da pasta e lê aqueles arquivos** — até ali nenhum alcançava, e foi por isso que o nível 27 da `Estocada` passou três versões cobrando `1,33` fatia e entregando `5,31`.

**Decisão da contagem: rota de Trilha conta como entrada própria, menu dentro de degrau não conta.** O `Batedor` entra com 12; a `Pegada` e a `Sintonia` com 4 cada.

**A v0.86 escreveu a ação `Mirar`**, que era entregue em seis degraus do `Batedor` e não tinha regra em lugar nenhum. **Ação Bônus, vantagem no próximo tiro com arma de projétil, e só se você não se deslocou nesta rodada nem vai se deslocar.** ***Ela estoura o degrau em `5,3×` e o estouro é decisão do Mizuki***, declarado no molde do `Punho` e da `Brasa`. Com ela, as três rotas do `Batedor` vão para `5,95`–`6,09` contra um teto de `5,00` e **dominam a `Estocada` por `1,20×`**, declarado.

**A v0.87 fechou os 21 nomes que faltavam** e consertou os dois validadores que deixaram passar os últimos defeitos. **De 89 entradas, 88 têm nome** — a única sem é a vaga do `Arremate`, deliberada.

| Trilha | 2 | 11 | 19 | 27 |
|---|---|---|---|---|
| `Estocada` | `Compasso` | `Traçado` | `Bote` | `Ferrão` |
| `Muro` | `Alicerce` | `Aterro` | `Escora` | `Cúpula` |
| `Punho` | `Engate` | `Encontrão` | `Tropel` | `Arranco` |
| `Brasa` | `Fagulha` | `Braseiro` | `Labareda` | `Fornalha` |
| `Torrente` | `acelerar` | `Vazão` | `Cheia` | `Transbordo` |
| `Batedor`/`Yumi` | `carregar` | `Mirar` | `Pique` | `Dobro` |
| `Batedor`/`Besta` | `Manivela` | `Mirar` | `Repuxo` | `Dobro` |
| `Batedor`/`Fogo` | `Ferrolho` | `Mirar` | `Quick Draw` | `Dobro` |

**E ela achou dois defeitos que nenhum validador via.** O nível 19 da `Brasa` publicava `Classe 2` enquanto a tabela e o argumento cobravam `Classe 3`, e `Classe 4` do 21 — **segundo exemplar do defeito da `Estocada` em duas versões**. E `Mão Firme` colidia com uma **Passiva do manual** (*"você não perde concentração nem carga por dano de 10 ou menos"*); virou `Cheia`.

**Os dois consertos de validador:**

- **`conferir-catalogo.py` ganhou a checagem 9** — toda `Classe` que a linha de preço cobra tem de aparecer no bloco de regra. **Direção de mão única**, porque comparar os dois lados como conjunto dava sete vermelhos falsos: o bloco cita `Classe` em exemplo de custo, e exemplo não é promessa.
- **`conferir-nomes.py` passou a ler os nomes de entrega da própria peça 17** e a varrer os `DESENHO` da raiz. De 34 para 61 nomes. **`Rescaldo` entrou numa lista `NOMES_SEM_CATALOGO`, que é DÍVIDA declarada** — cada entrada ali é nome que vive solto na prosa e devia ter dono.

> **Um defeito que o conserto criou e que já foi consertado: `Nó` batia com a preposição *"no"***, porque a comparação tirava acento dos dois lados — 49 avisos falsos numa rodada. **Agora nome com acento se compara com acento.**

---

# RÉGUAS QUE VALEM HOJE

A **fatia** é `5,08` de dano por rodada. A Trilha leva `5` e a banda é `4,50` a `5,00`; o Caminho leva `3`, em três degraus (`2 · 15 · 30`), e o nível 7 é de graça porque vale o vão. **O vão é `9 · 10 · 11 · 12` e é exatamente um golpe simples.**

**`+1` no seu acerto vale `10,80` de dano por rodada**, que é 10% da Rotina — por isso quase nada que mexe no d20 cabe num degrau. **Vantagem são 25 pontos percentuais.** 1 ponto percentual numa rolagem de **aliado** vale `0,230`. **Dano evitado converte 1 pra 1**, e isso inclui PV temporário, resistência e redução.

**Um Classe 0 causa `27` no nível 30, e um Classe 2 num alvo causa os mesmos `27`.** A Rotina é `floor(3,5 × Classe)` dados. O manual diz que um conjurador gasta PE em cerca de metade das rodadas. **Chefe faz `72` por rodada no nível 30 e capanga faz `38`. Uma luta dura `3,3` rodadas, e o dia tem `13`.**

**Tirar condição custa `1` PE por nível dela**, e condição sem nível declarado conta como nível 1.

# RÉGUAS QUE NÃO EXISTEM

**Gastar PE não tem preço. Condição não tem conversão em fatia. Cobertura não existe como regra** — procurada nas dezessete peças, zero ocorrência. E **"uma aptidão a mais" não tem régua e não pode ter**: vale a Trilha inteira para quem nunca escolhe Refino e um sétimo para quem sempre escolhe. Foi isso que matou o `Repertório`.

# O QUE FICA PENDURADO

O Evocador está **parado e não morto** — o §6 do `RASCUNHO-trilhas.md` tem cabeçalho de parada, e o `Servo` está montado em `5,07` contra `5,07`, faltando o gatilho do nível 27. Quando as três voltarem, **o total da peça 17 sai de 89** e a checagem 1 acusa.

**São QUATRO aptidões abertas e não três** — a terceira de kokusen não tem nome e o gate é "a definir" enquanto ela é contada entre as onze fechadas. **Os metros de cada arma de projétil não existem**, embora a propriedade `Longo Alcance` já custe 1 ponto. **O `.pdf` do manual está na v7.4 contra a v7.8 do `.docx`.**

**Duas entregas têm nome em minúscula** — o `carregar` do `Yumi` e o `acelerar` da `Torrente`. **A dominância do `Explosivo` sobre a `Torrente` é `1,20×`, declarada.** `Preparar` é o quinto competidor pela Reação. **Duas ações bônus ainda é pouco.** As de sempre: vagas de `Desliga`, Cicatriz, clash, **nome do sistema**, tabela de inimigo parada, atribuição de versão sem validador.

**E a terceira taxa sem medida do `Batedor`: em quantas rodadas o atirador fica parado.** Ela sozinha decide `2,12` fatias — a 100% as rotas vão a `8,07`–`8,21` e a dominância sobe para `1,64×`. *Primeira coisa a olhar na mesa, junto com o estouro.*
