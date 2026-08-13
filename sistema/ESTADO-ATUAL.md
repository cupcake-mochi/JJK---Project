# Estado atual do projeto

Atualizado em 13/08/2026, na v0.52 (última peça fechada: **Equipamento, na v0.48** — ela é a peça 14 e tem o `conferir-equipamento.py` em cima dela; a regra opcional do **Bloquear** continua em `03-mecanica/RASCUNHO-bloqueio.md`, e **Invocações está com cinco das seis perguntas fechadas** em `03-mecanica/RASCUNHO-invocacoes.md`). Este arquivo existe para retomar o trabalho — inclusive em conversa nova — sem recontextualizar tudo. Leia ele inteiro antes de mexer em qualquer coisa: ele tem a seção *"Onde estamos, e o que falta"* no fim, que é o ponto de retomada.

**Versão v0.52.** Fases 0 a 3 fechadas; Fase 4 (mecânica) em andamento, **catorze peças escritas** e **catorze validadores**. Manual do Fundamento na **v7.8**, com a Expansão de Domínio escrita, e o catálogo de aptidões com **dez das catorze entradas fechadas**. **Dá para montar uma ficha de nível 2, jogar uma missão inteira e recuperar entre elas** — por seis das nove rotas de Origem, e agora sem nenhum buraco de regra que morda nessa faixa.

## Como retomar

Leia nesta ordem: este arquivo → `../logs/CHANGELOG.md` (de cima para baixo, a entrada do topo é a mais recente) → a peça de `03-mecanica/` que for mexer. O CHANGELOG carrega o **porquê** de cada decisão, que é o que não dá para reconstruir sozinho.

Antes de mexer em número, rode os validadores. Eles falham alto se algo quebrar.

```
cd 03-mecanica
python3 conferir-atributos.py     # acerto, defesa, TR, perícia, vida, PE máximo, deriva
python3 conferir-acao.py          # régua das Restrições, dominância, Adianta
python3 conferir-pericias.py      # quadro de perícias, listas de Caminho e Origem, colisão
python3 conferir-descanso.py      # piso, exaustão, arredondamento, magnitude, empilhamento
python3 conferir-nomes.py         # todo nome batizado, projeto → manual
python3 conferir-manual.py        # vocabulário e números importados, manual → projeto
python3 conferir-aptidoes.py      # a trava do refino, as três rotas do marco, o kokusen
python3 conferir-expansao.py      # os gates da Expansão, a ordem, o preço em espaços
python3 conferir-orcamento.py     # o somatório: todos os drenos de PE ao mesmo tempo
python3 conferir-xp.py           # a curva, o abismo que fecha, e os alvos da Guilda
python3 conferir-criacao.py      # a ficha de exemplo contra as fórmulas, e o que a criação cita
python3 conferir-ficha.py        # a ficha de 05-material contra os catálogos das peças
python3 conferir-legados.py      # os três formatos, a cota de Desliga, as vagas e os totais
```

**Três naturezas diferentes, e vale saber qual é qual.** Dez conferem **regra** — *a fórmula deriva certo?*. O `conferir-criacao.py` confere **instância** — *a ficha publicada na peça 8 obedece à fórmula?* —, e nasceu na v0.34 porque os dois erros daquela versão passaram por baixo de todos os outros: a peça 8 é a única que produz uma ficha inteira, e ela envelhece toda vez que outra peça mexe num número. O `conferir-ficha.py` confere **material**, que é a cópia que vira personagem em sete mesas. E o `conferir-legados.py`, o décimo terceiro, confere **catálogo**: ele recalcula a tabela de totais da peça 13 e falha se o escrito não bater com o contado.

O quinto tem um modo de triagem, para rodar **antes** de batizar qualquer coisa:

```
python3 conferir-nomes.py --candidatos Vulto Matilha Bigorna
```

**O sexto entrou na v0.26 e olha a direção que faltava.** O `conferir-nomes` pergunta *"esse nome que eu batizei já significa alguma coisa no manual?"*; o `conferir-manual` pergunta *"o manual usa alguma palavra que este sistema não tem?"*. Foi por não existir que o `Bônus de Treinamento` e o `Habilidade/Sabedoria` sobreviveram tanto tempo. Ele também confere que a **tabela de PE, a de inimigo e a coluna Rotina** — que estão copiadas dentro das peças e dos outros validadores — continuam batendo com o `.docx`.

**Três precisam de `python-docx`** — `conferir-nomes`, `conferir-manual` e `conferir-pericias` —; sem ele eles **pulam** as checagens que leem o manual, em vez de falhar, e saem com código 0. Quanto cada um perde, lido do código na v0.40: **3 de 5 · 4 de 4 · 1 de 8**.

> *Até a v0.39 esta linha dizia "os dois últimos" e "4, 2 e 1", e nenhuma das duas coisas era verdade.* São três, não dois, e eles não são os últimos da lista. E o `conferir-manual.py` estava escrito como o que pula menos quando é o único que **não confere absolutamente nada** sem a biblioteca: ele sai no `except ImportError` antes da primeira checagem. **Número documentado a partir da saída do programa, e não do código, envelhece assim.**

> **O que mudou na v0.38:** rodar de outro diretório **não** faz mais ninguém pular checagem. Os quatro que abrem arquivo do manual resolvem por `__file__`, e de `/tmp` a saída sai idêntica com zero puladas. O `README` e o `LEIA-ME` diziam o contrário desde a v0.28 e foram corrigidos. **Continue rodando de `03-mecanica/`** — o `subir.sh` faz assim —, mas o motivo agora é hábito e não defeito. **A pulada que sobrou é a do `python-docx`, e essa é real.**

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

**Vinte e três perícias e onze ofícios.** Perícia tem atributo fixo; ofício não — o atributo muda com o que você faz. O Caminho dá **duas perícias fixas + quatro livres** e **um ofício fixo + um livre**; a Origem dá mais duas perícias. Oito de vinte e três, 35%.

**Golpe canalizado** = os dados da Classe e nada mais (é o feitiço, e não soma arma nem Força). **Golpe simples** = arma + Força (é o Classe 0 físico). Um canalizado por turno; ataque extra é sempre simples.

**Invocações:** o invocador e todas as invocações somados entregam **uma** Rotina.

## Onde cada coisa está

| Arquivo | Conteúdo |
|---|---|
| `00-fundacao/pitch-de-design.md` | os três pilares e as restrições do projeto |
| `01-pesquisa/dossie-de-metodologia.md` | a seção 8 lista as dez travas de arquitetura |
| `02-esqueleto/arquitetura.md` | o que o Fundamento resolve e os buracos em volta |
| `03-mecanica/01-atributos-acerto-defesa.md` | de onde vem o número — e a **seção 5.5, o Caído**, que é a máquina de estado de 0 de vida |
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
| `03-mecanica/conferir-nomes.py` | o vocabulário do manual, extraído do `.docx`, contra todo nome que o projeto batizou |
| `03-mecanica/conferir-manual.py` | a direção contrária: o manual contra o vocabulário e os números do projeto |
| `03-mecanica/conferir-aptidoes.py` | a trava do refino, as três rotas do marco, o teto de Passivas e o kokusen |
| `03-mecanica/conferir-expansao.py` | os dois gates da Expansão, a ordem entre os degraus, o preço em espaços e a fragilidade da curva |
| `03-mecanica/conferir-orcamento.py` | o somatório: todos os drenos de PE ao mesmo tempo, e se todo preço tem número |
| `03-mecanica/conferir-xp.py` | a curva, o abismo que fecha, e se a regra ainda entrega o tempo que a Guilda pediu |
| `03-mecanica/conferir-criacao.py` | **a instância, não a regra**: a ficha de exemplo da peça 8 contra as fórmulas, a proteção da aptidão gratuita, a Trilha na criação e se o catálogo citado existe |
| `03-mecanica/conferir-ficha.py` | **o material contra a regra**: as 23 perícias, os 11 ofícios, os 5 Caminhos, as 15 Trilhas e as constantes do nível 2 que a ficha imprime, contra as peças donas |
| `05-material/gerador-ficha/` | o gerador da ficha (Node: `node make.js`), e os dois `.docx` que ele produz |
| `conferir-repositorio.py` | a árvore, as referências mortas, e os números que moram em mais de um documento |
| `99-arquivo/` | material morto, com LEIA-ME próprio. Não leia de lá para escrever peça nova |

**Duas peças foram parcialmente substituídas e trazem o aviso no topo:** as seções 3 e 4 da peça 4 saíram para a peça 7, e a seção 3 e o quadro de Caminhos da peça 5 saíram para a peça 6.

O manual do Fundamento **v7.8** (`manual/Fundamento-MANUAL-v7.docx`) é o subsistema de técnica e feitiço, já validado — 363 parágrafos e 84 tabelas. `manual/gerador/` traz o gerador (Node: `npm install docx && node make.js`) e `manual/matematica/` os validadores `pac7.py` e `v7.py`. **O `.pdf` continua na v7.4**, porque ele é exportado à mão.

**Quem é dono da versão do manual:** a primeira linha de `manual/gerador/COMO-USAR.txt`. Toda outra cópia — a capa em `partA.js`, este arquivo, o `README.md`, o `LEIA-ME.md` e o `arquitetura.md` — é cópia, e o `conferir-repositorio.py` falha se alguma divergir. *Ele nasceu na v0.33, depois de a capa do manual passar três versões dizendo 7.5.*

### O manual não é lei, e saber disso muda como se lê

*Registrado na v0.26.* Os limitadores, exemplos e tabelas do manual foram calibrados quando o sistema em volta era outro. **Servem de base para continuidade; não valem ao pé da letra.** Dez decisões do projeto estão penduradas em três tabelas dele, e as três não são iguais:

| tabela | dono | o que ela segura |
|---|---|---|
| **PE** — *"quantas vezes você lança"* | **o projeto** | o 6 do Emanador, a fórmula do PE máximo, o orçamento de missão. Mudou o 6? Regere a coluna |
| **Rotina** — dano por rodada por Classe | **o manual** | o golpe canalizado, o ataque extra, o conserto da invocação, os 10% do crítico. Ela é a **régua**, não uma medida: mudar a Rotina reprecifica os quatro de uma vez |
| **Inimigo** — chefe e capanga por nível | **o playtest** | a trava de vida inteira. É a única das três que afirma algo sobre o mundo — que um combate dura ~3,5 rodadas — e ninguém é dono dela até alguém jogar |

O `conferir-manual.py` falha se os dois lados divergirem, e a mensagem dele **nomeia o dono** em vez de acusar o projeto. Divergência ali é pedido de decisão.

## Pendências, da mais urgente à menos

1. **Nome do sistema.** Aberto desde a v0.1, e a única pendência de nome que sobrou.
2. **Se a perícia livre da Origem devia ser da lista também.** As listas existem desde a v0.22, mas a segunda perícia continua livre com aprovação — é o último lugar da criação em que um número depende de julgamento do mestre.
3. Quantas Trilhas um personagem acumula, e em que níveis.
4. **Como a Trilha Torrente cobra o segundo feitiço da rodada**, contra a regra de ouro nº 6. É o mesmo defeito da invocação — mais de uma ação por rodada — e o conserto que funcionou lá deve servir aqui.
5. **O que Elo, Sutura e Perímetro entregam** que valha o golpe por rodada que o Guia não tem.
6. **Se a curva de dano deve cruzar a coluna Rotina.** No nível 2 o conjurador está +38% e o físico +69% acima dela; no nível 30, 21% e 16% abaixo. Decisão não tomada, não erro.

### O Caído entrou na v0.37, e ele deixa uma dívida com nome

*A peça 1 ganhou a **seção 5.5**, e ela fecha a pergunta nº 5 do `pitch-de-design.md` — aberta desde a v0.1.* A 0 de vida você escolhe **Aguentar** (apaga, janela de 3 rodadas, cura de 1 te levanta) ou **Insistir** (fica de pé, cada rodada custa 1/8, 1/4 e 1/2 da vida máxima). Levantar dá uma **Sequela**, que encurta a janela da próxima queda; **na segunda queda vem uma Cicatriz**. O fim da janela é o **estágio 4 de dano de alma**, que o manual já escrevia e que ninguém alcançava. Seis checagens novas no `conferir-atributos.py`, com oito perturbações conferidas.

> **A dívida: uma Cicatriz não tem mecânica, só nome.** Hoje ela é o registro de que a coisa aconteceu — permanente, não sai no descanso, e nada mais. Isso foi deliberado, porque o conteúdo dela é da **peça de dano e condições**, que não existe: sem a lista fechada de condições, qualquer efeito que eu escrevesse ali seria número solto sem dono, e a lição nº 9 diz onde isso termina.
>
> **O que precisa ser resolvido quando aquela peça chegar:** o que uma Cicatriz faz, se ela tem teto por ficha, se some algum dia e por qual meio, e como ela conversa com a **Energia Reversa** — que é a candidata óbvia a apagá-la e continua sendo aptidão não escrita. Enquanto isso, ela é boa ficção e mecânica nenhuma, e **o texto da peça 1 diz isso com todas as letras** em vez de fingir que está fechado.
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

**As Bênçãos de Corpo, para quem não tem energia.** A Restrição Celestial pelo ramo da Maki não tem energia amaldiçoada — sem PE, sem golpe canalizado, sem Sentir Energia — então não tem aptidão nem refino. Ela ganha **a mesma máquina com outra métrica**: as aptidões se chamam **Bênçãos** e o refino se chama **Lapidação**.

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

**Metade já existe:** as quatro anti-domínio entraram na v0.29 e a **seção 6.5 da peça 11** já trata o Domínio Simples como aptidão pura, sem lâmina. A Energia Reversa está na lista de aptidões pendentes.

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
2. **O Guia pode estar dominado pela Vanguarda.** *Reformulado na v0.24.* Não era achado fechado: dependia de uma classificação que nunca tinha sido escrita — quem ganha ataque extra. Agora está escrito (peça 6, seção 3.1): **Bastião e Vanguarda pelo Caminho no nível 6; Arremate e Coro pela Trilha; o Guia por nenhuma rota.** O que sobra não é dominância, é uma pergunta com número: *o que Elo, Sutura e Perímetro entregam que valha um golpe por rodada?*
3. **O ofício não passa no filtro do multi-mestre.** "O mestre escolhe o atributo na hora" faz dois mestres cobrarem coisas diferentes pelo mesmo ofício, com até cinco pontos de diferença. Conserto: tabela com o atributo padrão de cada um.
4. **A escolha de refino no marco paga mal, e três marcos pagam zero.** *Achado pelo Mizuki na passada de Equipamento, e a conta confirmou pior do que o palpite.* O refino **passivo chega a 8** sem escolha nenhuma; sete escolhas de marco compram **+2**, e o teto 10 é alcançado no **nv22**. Do nv22 em diante a escolha *"refino e uma aptidão"* vira **só a aptidão**, enquanto *atributo* e *Leque* continuam valendo cheio — três marcos com um dos três eixos pela metade.

   | o que o +2 de refino compra | refino 8, de graça | refino 10, sete escolhas |
   |---|---|---|
   | proteção de cobrir-se | 3 | 4 |
   | RD da Reação | 12 | 15 |
   | desconto e duração do domínio | 4 | 5 |

   **A rota se paga pela quantidade de aptidões, não pela magnitude do refino** — e isso contradiz a frase que abre a peça 11, *"o refino é a métrica das aptidões"*. Como as aptidões usam o refino como variável, o valor de cada uma também quase não muda entre 8 e 10. *Não mexer sem decidir junto o que compensa os três marcos mortos: teto maior, escolha diferente depois do teto, ou o passivo parar antes de 8.*

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
| Aptidões e degraus de refino | só valem do nível 6 em diante |

**O que não existe, e faz falta para alguém jogar:**

> **As duas primeiras linhas da segunda tabela são vocabulário que ainda não tem peça, e por isso a definição delas mora aqui — provisoriamente.** *Quando cada peça for escrita, a definição vai para ela e esta linha vira ponteiro.* **Enquanto isso, este é o dono:** a peça 13 e a peça 14 citam as duas e apontam para cá em vez de repetir, que é a lição nº 9 sendo obedecida em vez de explicada.

| falta | tamanho do buraco |
|---|---|
| **Tabela de progressão consolidada** | o que você ganha em cada nível está espalhado por cinco documentos: marcos na peça 2, maestria na peça 1, refino no `arquitetura.md`, XP na peça 12, Classe e feitiço no manual |
| **Quick-start jogável** | decidido na v0.2 como a estrutura do material final. Não existe. As catorze peças são argumento de design, não texto de regra: ninguém senta na mesa com elas |
| **Playtest** | `04-playtest/` está vazia. Zero sessões desde a v0.1. **Todo número do sistema é previsão** |

*A **tabela de XP** saiu desta lista na v0.32.* Ela era a trava nº 1 de mundo compartilhado e ficou aberta trinta versões; hoje é a peça 12, com o `conferir-xp.py` em cima dela.

A skill `redacao-acessivel-rpg` existe exatamente para a travessia de "nota de design" para "texto de regra", e nunca foi rodada contra o material.

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
> A rota decidida com o Mizuki foi: v7.7 → anti-domínio → XP → **validação e polimento** → ficha e quick-start. *Os quatro primeiros saíram, o polimento foi a v0.33 e a **ficha saiu na v0.35** — `05-material/` não está mais vazia. Falta o quick-start.*

## A fila decidida com o Mizuki na v0.36

Quatro peças, e a ordem é de **dependência**, não de tamanho. A ordem que ele levantou era Legados → Caminhos → Itens → Invocações; a peça de Caminhos foi para o fim porque **duas das cinco árvores dependem das outras duas peças**.

| # | peça | destrava | depende de |
|---|---|---|---|
| ~~1~~ | ~~**Legados** — a régua de magnitude, e ~5 por Origem~~ | **fechada na v0.39** (peça 13): régua, catálogo de **81 entradas** e o `conferir-legados.py` | — |
| ~~2~~ | ~~**Equipamento** — armas, escudos, uniformes~~ | **fechada na v0.48** (peça 14): as 52 armas com orçamento fechado, proteção, escudo, treino e requisito de Força, mais o `conferir-equipamento.py` com dez checagens | — |
| 3 | **Invocações** — o sistema de criação | o Evocador | — |
| 4 | **Caminho, Trilhas e subtrilhas** — a árvore de cada um | o resto | **2 e 3** |

### A fila foi reordenada na v0.50, e as duas peças novas ganharam posição

*Decisão do Mizuki: "Invocações agora, ferramenta entre ela e a Trilha."* As duas que a v0.49 destampou entram assim:

| # | peça | por que aqui | move o contador? |
|---|---|---|---|
| 1 | **Invocações** | dependência dura de Trilhas | rotas 6/9 → 6/9 · vagas 0 de 7 |
| 2 | **Ferramenta amaldiçoada** | destrava `Técnica Marcial` | **rotas 6/9 → 8/9** · vagas 3 de 7 |
| 3 | **Trilhas** | fecha com as quinze de uma vez | toca **100% das fichas** |
| 4 | **Objeto amaldiçoado** | a conta o pôs por último | rotas 6/9 → 6/9 · **vagas 1 de 7** |

**Só a posição 3 contra 2 era escolha. As outras três a conta fechou sozinha:**

- **Invocações antes de Trilhas** não é preferência: `Servo`, `Matilha` e `Coro` **são** o sistema de invocação visto de dentro. As outras doze Trilhas já estão desbloqueadas desde que Equipamento fechou — era a Vanguarda que dependia dela.
- **Ferramenta antes de Técnica Marcial** está escrito na peça 5 §3: a Maki *"só compete porque a ferramenta amaldiçoada carrega a energia por ela"*. Técnica Marcial escrita antes produz rota que não fere maldição.
- **Objeto amaldiçoado por último**, e é o contrário do que a v0.49 fazia parecer. Ele foi o achado daquela versão, mas **Receptáculo e Reencarnado já rodam hoje** — os dois vão para o Fundamento. Ele fecha **1 vaga de Desliga e mais nada.** *Buraco de vocabulário real não é o mesmo que buraco que trava alguém.*

**O rascunho de Invocações está em `03-mecanica/RASCUNHO-invocacoes.md`**, com as seis perguntas em ordem de dependência, a triagem do nome e o que o validador vai precisar.

> **Cinco das seis fecharam na v0.51, e o argumento inteiro delas mora no rascunho — não aqui.** A Q1 (iniciativa) no §3.1, a Q2 (cinco fichas ou uma) no §3.2, a Q3 (a ficha) no §3.3 e no §3.6, a Q4 (o custo) no §3.4, a Q5 (a morte) no §3.5, e o catálogo no §3.7 — que na **v0.52** ganhou a **régua de criação**: o catálogo não é a lista do que existe, é a régua contra a qual o que não existe é medido, no molde que a peça 12 já mandava usar. **Só a Q6 continua aberta, e ela é da peça de Trilhas — com metade da resposta já escrita no §3.7.** *Este ponteiro existe para quem retomar não recomeçar: as decisões têm um dono só, e é lá.*
>
> **A máquina, em cinco linhas:** a invocação age **na casa do dono**; a Matilha é **uma ficha com cinco corpos**, pool com cascata, rodada resolvida **em pool**; a ficha é **derivada do dono mais um deslocamento que só desce**, com `Traço` e `Comando` comprados num orçamento de **2 a 9** pontos; invocar custa **`1 × maior Classe` e a ação padrão**, e **comandar custa a ação padrão**; ela **some no zero**, é **vulnerável a área** e **morre em definitivo** se o excedente passar de metade da vida máxima ou um golpe causar a vida máxima inteira.
>
> **E o teto de uma Rotina da peça 6 §4 deixou de precisar de decreto:** com comandar custando a ação padrão, o dono e a invocação ficam mutuamente exclusivos na rodada e a soma cai da economia de ação sozinha. **O Coro é a exceção**, que a peça 5 §4 já autoriza.
>
> **O que separa o rascunho da peça 15:** o catálogo de `Traço` e `Comando` escrito entrada por entrada, o tratamento de **Rika e Mahoraga** (que agem fora do controle do portador), **reconseguir a invocação morta**, e **o validador dono dela**, com as treze checagens que o §5 do rascunho lista. *O nome do arquivo fica sem escrever até ele existir — o `conferir-repositorio.py` acusa referência a arquivo que não existe, e acusou esta mesma frase ao fechar a versão.* **Ele achou um buraco na peça 6, e ele é de um eixo que ninguém tinha apontado para cá:** a regra da seção 4 preça o **dano** da Matilha e não preça o **tempo de mesa** dela. Cinco fichas agindo por rodada custam o mesmo tempo quer cada uma faça 25 de dano ou 5 — e foi por essa metade, não pela do dano, que o 5e 2024 trocou a família inteira de `conjure`. O eixo já existe aqui, na pergunta de playtest sobre ação bônus.

> **Equipamento é a próxima, e ela tem uma dívida marcada esperando.** A peça 13 fecha dizendo *"quando equipamento fechar, a primeira coisa a fazer é voltar aqui"* — quatro vagas de Desliga nomeiam essa peça como a que deve criar o alvo delas. As outras três esperam **dano e condições**, que não está na fila. *Decisão registrada não é decisão aplicada, e foi assim que a Trilha passou sete versões.*

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

**O que falta:** **o validador da peça**, que precisa rodar a dominância **uma vez por rota de proteção, e são três** — cobrir-se, uniforme, e **sem energia nenhuma** (a Restrição Celestial pelo ramo da Maki, que não tem cobrir-se para desligar); os **nomes dos degraus de escudo**; a **penalidade** por empunhar sem treino ou sem requisito, que é da peça de dano e condições; e **os dois dados do `Yumi`**, que a v0.47 flagrou estourando o orçamento — a fórmula de preço do tiro desconta a Força que o corpo a corpo soma, e o arco soma **Destreza** e leva o desconto do mesmo jeito.


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

**Em aberto:** as condições que impedem Bloquear — surpreendido, caído, agarrado —, que esperam a peça de **dano e condições**; a linha na ficha (`Defesa 17 · Bloquear 2d10+6`, que é o que faz o `−1` nunca aparecer na mesa); e a Reação na ficha de inimigo, sem a qual a Brecha não funciona.

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
| **Sete vagas de Desliga**, declaradas na tabela em vez de preenchidas | **duas** esperam ferramenta amaldiçoada · **três** esperam dano e condições · **uma** espera objeto amaldiçoado · **uma** espera Técnica Marcial. *Reclassificadas na v0.49 — as quatro que diziam equipamento nomeavam a peça errada* |
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

E uma coisa solta que não é peça: **o nome do sistema**.

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
