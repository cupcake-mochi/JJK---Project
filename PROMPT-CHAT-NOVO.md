# Prompts para os chats novos

Um chat por peça. **Antes de abrir qualquer um deles:** `./subir.sh` e depois
**"Sync now"** no Project — senão o chat novo lê o commit anterior e discute
número que já mudou.

Copie o bloco inteiro da peça que for fazer.

---

## 0 · Mudança de conta — o que levar, e o primeiro prompt

### O que precisa viajar

| o quê | onde está | observação |
|---|---|---|
| **o repositório inteiro** | esta pasta | 13 MB fora de `.git/` e `_backup/`. É a fonte da verdade — regras, validadores, manual, gerador e as skills |
| **o `.git/`** | esta pasta | leva junto se quiser o histórico. Se preferir começar limpo, um `git init` novo perde só o histórico de commit — **o `logs/CHANGELOG.md` é quem guarda o porquê**, e ele é arquivo comum |
| **as cinco skills** | `sistema/skills/` | quatro de apoio a RPG mais a `rpg-da-guilda`, que é o procedimento deste repositório. **Skill é da conta, não do repositório** — precisam ser instaladas de novo na conta nova |
| **o Project do Claude**, se usar | fora daqui | recriar apontando para o mesmo GitHub, e clicar em *Sync now* |

**O que NÃO precisa viajar:** `_backup/` (é o estado pré-reorganização, e o `.gitignore` já o segura), `manual/gerador/node_modules/` (reinstala com `npm install docx`) e qualquer `__pycache__/`.

**O que a conta nova precisa instalar:** `python-docx`, com
`pip install python-docx --break-system-packages`. Sem ele, três validadores
**pulam** as checagens que leem o manual em vez de falhar — eles saem verdes
sem terem conferido nada.

### Como instalar as cinco skills na conta nova

As cinco moram em `sistema/skills/`, cada uma com o seu `SKILL.md`. Dois caminhos:

1. **Pelo arquivo `.skill`** — zipe cada pasta com extensão `.skill` e mande no chat; ele mostra um botão de instalar.
2. **Pelo repositório** — peça ao assistente da conta nova: *"leia `sistema/skills/` e instale as cinco skills que estão lá"*. Ele lê os `SKILL.md` e salva cada uma.

**A `rpg-da-guilda` é a mais importante das cinco**, porque ela guarda o
procedimento que custou versão para aprender: de onde rodar os validadores, o
que a triagem de nomes não pega, como escrever arquivo neste mount sem o
arquivo sumir, e o arnês de perturbação. Sem ela, o chat novo redescobre tudo
isso do zero — e provavelmente errando primeiro.

### O primeiro prompt da conta nova

Cole isto inteiro no primeiro chat, com a pasta já conectada.

```
Este é o RPG da Guilda — um sistema de RPG de mesa de Jujutsu Kaisen para um
server de guilda com 5 a 7 mestres ativos e personagem persistente entre mesas.
Eu migrei o projeto de conta e você está pegando ele no meio de uma peça.
Antes de escrever qualquer coisa, faça esta sequência inteira e me relate cada passo.

1. INSTALE AS SKILLS. Estão em `sistema/skills/`, cinco pastas com SKILL.md.
   Leia cada uma e salve as cinco na conta. A `rpg-da-guilda` é a mais
   importante: ela é o procedimento deste repositório e existe para você não
   redescobrir errando o que já custou versão. Leia ela primeiro e siga.

2. PREPARE A MÁQUINA. `pip install python-docx --break-system-packages`.
   Sem isso três validadores PULAM as checagens que leem o manual em vez de
   falhar — eles saem verdes sem terem conferido nada.

3. LEIA, NESTA ORDEM:
   - `README.md`, em especial "Nove lições que custaram erro". Elas são a fonte
     única e não têm cópia em lugar nenhum.
   - `sistema/ESTADO-ATUAL.md` INTEIRO. Ele é grande e a leitura pode truncar —
     se vier aviso de leitura parcial, continue do offset em vez de responder
     pela primeira página.
   - `logs/CHANGELOG.md` de cima até a v0.33. A entrada do topo é a mais
     recente, e ele carrega o PORQUÊ de cada decisão — é a única parte do
     projeto que não dá para reconstruir lendo o resto.

4. RODE OS VALIDADORES, sempre de dentro de `sistema/03-mecanica/`. De outro
   diretório três deles pulam checagem em silêncio e saem verdes. Depois rode o
   `conferir-repositorio.py` da raiz. Me diga quantos passaram e se algum
   imprimiu PULADA — verde que pulou checagem não prova nada.

5. NÃO RODE GIT. Deste sandbox o git sai com "loose object is corrupt" e o
   repositório está inteiro — é o mount. Pior: `git status` cria um
   `.git/index.lock` que você não consegue apagar, e lock preso trava o
   `./subir.sh`. Commit é sempre meu.

ONDE O TRABALHO PAROU
A peça 13 (Legados) está no meio, em `sistema/03-mecanica/RASCUNHO-legados-regua.md`.
Ela tem duas metades: a régua de magnitude, fechada, e o catálogo, pela metade —
Latente, Receptáculo e Descendente prontos, Reencarnado incompleto, e Feto,
Corpo Amaldiçoado e Restrição Celestial não começados. O arquivo não leva número
no nome de propósito: meia peça não é peça, e arquivo com dois dígitos na frente
quebra a contagem do `conferir-repositorio.py`.

COMO EU GOSTO DE TRABALHAR
- Escolha de sabor é minha: quantos itens numa lista, quais são, como se chamam.
  Traga as opções com número e trade-off já calculados, e pergunte. Rodadas
  curtas, nunca uma proposta grande pronta.
- Mas não me pergunte o que a conta responde. Se dominância, deriva ou o filtro
  multi-mestre já decidem, rode a conta e me mostre o resultado.
- Me mostre no chat o que você escreveu, não só no arquivo.
- Antes de entrar numa peça ou numa Origem, me mostre o que ela já tem.
- Número vem de conta rodada, nunca de intuição. Escreva o script, rode, mostre
  a tabela.
- Pesquise antes de inventar: como outros sistemas resolvem o mesmo problema, e
  qual o modo de falha documentado de cada um.
- Revisão cética antes de fechar, inclusive contra o que você mesmo escreveu.
- Português informal, nunca de Portugal. Documento não pode ter cara de saída
  de IA: seções de tamanhos diferentes, sem simetria forçada.

Comece pelos cinco passos e me diga o que você entendeu do estado atual.
```

---

## 1 · Legados — em andamento, peça 13

```
Retomando o RPG da Guilda, na peça 13 — Legados. Ela está pela metade, em
`sistema/03-mecanica/RASCUNHO-legados-regua.md`.

Leia o `README.md` (as nove lições), o `sistema/ESTADO-ATUAL.md` inteiro, o
`logs/CHANGELOG.md` de cima até a v0.33, e o rascunho inteiro. A peça 9 continua
dona das Origens; o que mudou de casa é a régua e o catálogo.

**A régua está fechada.** Três formatos, e cada um tem trava própria:

- **Ajusta** mexe em número de rolagem. Sempre tem relógio da escada da peça 10,
  e a largura escolhe o degrau: até três coisas nomeadas pode ser por cena,
  categoria inteira desce para por dia. Não existe Ajusta permanente.
- **Desliga** só apaga o que ninguém comprou. Dano não, condição não — Condição
  Menor custa Média e Maior custa Pesada —, nem o que qualquer Melhoria concede.
  Sobra o que o mundo faz com você fora do feitiço. **É teto, não cota:** os
  alvos legais do sistema são sete, e seis já estão usados.
- **Destranca** é zero no dado, e tem duas cláusulas: o jogador puxa o gatilho,
  e ele afirma sobre o mundo alguma coisa que só aquele personagem afirma.
  Relógio só quando o mestre responde com verdade.

**A escolha é dois Legados: um Destranca obrigatório, e mais um de qualquer
lista.** Isso reabre uma linha da peça 9 que diz o contrário, e a mudança ainda
precisa chegar na peça 8, na peça 9, no `ficha.js` do gerador e nos dois
validadores que conferem a ficha. Enquanto o rascunho for rascunho, a regra
antiga é a que vale.

**Alvo por Origem:** 4 Destranca · 4 Ajusta · até 2 Desliga.

**Escritas: Latente (10), Receptáculo (9), Descendente (10) e Reencarnado (5).**
O Reencarnado está incompleto — faltam 3 Destranca e ele ficou com zero Desliga
depois que os dois dele foram reprovados por apagarem condição. Faltam inteiras:
**Feto, Corpo Amaldiçoado e Restrição Celestial.**

Duas coisas do catálogo antigo que ainda não foram tratadas:
- **Não Sou Gente** (Corpo Amaldiçoado) é imunidade a dano e a régua reprova.
  A saída registrada é a imunidade mudar de camada e virar Passiva paga com
  espaço de feitiço, e o Legado ficar com a metade que não é dano.
- **Irmãos** (Feto) é o piso do catálogo: o jogador não consegue disparar, e o
  efeito é simétrico. Precisa de gatilho do jogador ou de aposentadoria.

E a peça sai com **validador junto** — a peça 9 é uma das que nunca teve um, e é
de peça sem validador que saíram os dois erros da v0.34.

Antes de batizar qualquer Legado, rode
`python3 conferir-nomes.py --candidatos <nomes>` de `sistema/03-mecanica/`.
Ela já matou mais de dez nomes que pareciam livres — e não pega colisão de
sentido nem de vocabulário do hobby, então confira as duas à mão.

Me mostre no chat o que você escrever, e me mostre o que a Origem já tem antes
de entrar nela.
```

---

## 2 · Equipamento

```
Retomando o RPG da Guilda. Leia `README.md`, `sistema/ESTADO-ATUAL.md` e o
`logs/CHANGELOG.md` de cima até a v0.32. A fila está no ESTADO-ATUAL, na seção
"A fila decidida com o Mizuki na v0.36".

A peça de agora é a **2: Equipamento** — armas, escudos e armaduras/uniformes.
Pode ser D&D-like. Ela destrava duas coisas: a árvore da Vanguarda, e a
**Técnica Marcial**, que é o que falta para duas das três rotas de Origem que
não rodam hoje.

Duas travas já calculadas, e as duas apertam:

- `Defesa = 10 + Destreza + proteção`, e a ficha de nível 2 **já nasce com
  proteção 1** — cobrir-se de energia, aptidão gratuita do refino 1, que dá
  `1/3 do refino + 1`. No refino 10 ela dá 4.
- Uniforme, armadura e escudo **desligam** essa proteção. Então a peça 11 já
  registrou o recado: **um uniforme precisa valer mais que 4, senão ele nasce
  morto.** Isso não é sugestão, é o piso.

E o dado de arma é **equipamento, não Caminho** — a v0.36 confirmou que o
Caminho não dá dados de dano, e é por isso que o dano do soco e o da arma moram
aqui.

Rode os validadores antes de mexer em número, sempre de `sistema/03-mecanica/`.
Rode a triagem de nomes antes de batizar arma, material ou categoria.
Leia as nove lições do README antes de escrever conta nova, e a peça sai com
validador junto.
```

---

## 3 · Invocações

```
Retomando o RPG da Guilda. Leia `README.md`, `sistema/ESTADO-ATUAL.md` e o
`logs/CHANGELOG.md` de cima até a v0.32. A fila está no ESTADO-ATUAL, na seção
"A fila decidida com o Mizuki na v0.36".

A peça de agora é a **3: criação de invocações**. Ela destrava a árvore do
Evocador.

A trava é a mais dura do projeto e já está escrita, na peça 6 §4:

  "Você e todas as suas invocações somados entregam UMA Rotina."

O motivo está medido lá: uma invocação que age sozinha dobra o dano por rodada,
uma horda de três quadruplica, e nenhum preço em PE conserta isso — porque o
problema não é recurso, é economia de ação. Mais corpos agindo por rodada é a
coisa que quebra todo sistema d20, sem exceção.

Então a pergunta desta peça não é "quanto custa uma invocação": é **como se
divide uma Rotina entre corpos** sem que a divisão vire conta de mesa. As
Trilhas do Evocador já dizem os três formatos que o sistema quer suportar:
Servo (uma forte, o molde do Megumi), Matilha (muitas fracas, o molde do Geto)
e Coro (lutar junto delas).

Rode os validadores antes de mexer em número, sempre de `sistema/03-mecanica/`,
e o `conferir-orcamento.py` importa aqui mais que os outros — ele é quem
pergunta "cabe tudo junto?".
Leia as nove lições do README antes de escrever conta nova, e a peça sai com
validador junto.
```

---

## 4 · Caminho, Trilhas e subtrilhas

```
Retomando o RPG da Guilda. Leia `README.md`, `sistema/ESTADO-ATUAL.md` e o
`logs/CHANGELOG.md` de cima até a v0.32. A fila está no ESTADO-ATUAL, na seção
"A fila decidida com o Mizuki na v0.36" — leia ela inteira, porque ela tem
o que sobrevive de cada uma das cinco árvores e o que não.

A peça de agora é a **4: a árvore de habilidades de cada Caminho, as Trilhas e
as subtrilhas**. Ela é a última das quatro porque duas das cinco árvores
dependiam de equipamento e de invocações, que já saíram.

**A trava principal:** o Caminho **não dá dados de dano**, nem aumento de
Classe, nem Melhoria de graça, nem cura. Isso foi desafiado e confirmado na
v0.36, e o motivo é o pilar 1 — se o Caminho desse dano, dois personagens do
mesmo Caminho começariam a se parecer.

O que ele PODE conceder está na peça 5 §4: perícia e TR, mover e reposicionar,
trocar alvo de efeito que já existe, estender duração, recuperar (PE, ferimento,
condição, Integridade), trocar o fixo de 2 do acerto de conjuração por um
atributo, e abrir exceção estreita e paga na economia de ação.

Duas coisas para medir antes de escrever, não depois:
- a reação de RD que eu quero no Bastião encosta em cobrir-se de energia, que
  já dá RD de 1,5 × refino por 2 PE. Ou uma domina a outra, ou são a mesma peça
  com dois nomes.
- pontos de feitiço para o Emanador são moeda nova ao lado do PE. Passa pelo
  `conferir-orcamento.py` antes de ter número.

E a Trilha vem no nível 2, junto do Caminho — isso foi decidido na v0.27 e
aplicado na v0.34. Hoje as quinze são só nome e uma frase; esta peça é a que
lhes dá número.

Rode os validadores antes de mexer em número, sempre de `sistema/03-mecanica/`.
Rode a triagem de nomes antes de batizar subtrilha ou proeza.
Leia as nove lições do README antes de escrever conta nova.
```
