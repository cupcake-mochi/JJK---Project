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
| **as sete skills** | `sistema/skills/` | quatro de apoio a RPG, mais `rpg-da-guilda` (o procedimento deste repositório), `pesquisa-antes-de-propor` e `gasto-de-modelo`. **Skill é da conta, não do repositório** — precisam ser instaladas de novo na conta nova |
| **o Project do Claude**, se usar | fora daqui | recriar apontando para o mesmo GitHub, e clicar em *Sync now* |

**O que NÃO precisa viajar:** `_backup/` (é o estado pré-reorganização, e o `.gitignore` já o segura), `manual/gerador/node_modules/` (reinstala com `npm install docx`) e qualquer `__pycache__/`.

**O que a conta nova precisa instalar:** `python-docx`, com
`pip install python-docx --break-system-packages`. Sem ele, três validadores
**pulam** as checagens que leem o manual em vez de falhar — eles saem verdes
sem terem conferido nada.

### Como instalar as sete skills na conta nova

As sete moram em `sistema/skills/`, cada uma com o seu `SKILL.md`. Dois caminhos:

1. **Pelo arquivo `.skill`** — zipe cada pasta com extensão `.skill` e mande no chat; ele mostra um botão de instalar.
2. **Pelo repositório** — peça ao assistente da conta nova: *"leia `sistema/skills/` e instale as skills que estão lá"*. Ele lê os `SKILL.md` e salva cada uma.

**A `rpg-da-guilda` é a mais importante de todas**, porque ela guarda o
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

1. INSTALE AS SKILLS. Estão em `sistema/skills/`, sete pastas com SKILL.md.
   Leia cada uma e salve todas na conta. A `rpg-da-guilda` é a mais
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

4. RODE OS VALIDADORES de dentro de `sistema/03-mecanica/`, que é o que o
   `subir.sh` faz. Depois o `conferir-repositorio.py` da raiz. Me diga quantos
   passaram e se algum imprimiu PULADA — verde que pulou checagem não prova
   nada. Sem `python-docx`, três deles pulam e saem com código 0: o
   `conferir-nomes` pula 3 de 5, o `conferir-manual` pula 4 de 4 (todas, ele
   sai no `except ImportError`) e o `conferir-pericias` pula 1 de 8.

5. NÃO RODE GIT. Deste sandbox o git sai com "loose object is corrupt" e o
   repositório está inteiro — é o mount. Pior: `git status` cria um
   `.git/index.lock` que você não consegue apagar, e lock preso trava o
   `./subir.sh`. Commit é sempre meu.

ONDE O TRABALHO PAROU
EQUIPAMENTO está em andamento, e o estado dela mora em
`sistema/03-mecanica/RASCUNHO-equipamento.md`. LEIA ESSE ARQUIVO INTEIRO antes
de propor qualquer coisa — ele tem as decisões já tomadas com o número de cada
uma, o que foi rejeitado e por quê, e a lista do que falta. Não refaça nada que
está lá; a conta já rodou.

Fechado no rascunho: duas classes (Traje e Revestimento), três degraus, requisito
de Força 3/5/6 e SEM gate de nível, escudo +1 derivado, oito propriedades de arma
e oito classes de arma com 39 nomes, dominância zerada.

Em aberto, e é por aí que se retoma:
- A classe PESADA paga dois pontos de Força a mais que a Uma mão pelo mesmo valor
  líquido. O argumento que a salva — o requisito é compartilhado com o Revestimento —
  NÃO foi validado. Valide antes de escrever a peça.
- Munição não tem número. Versátil não tem os dois dados escritos.
- O validador da peça, com a checagem de dominância POR VALOR TOTAL, que é o furo
  que o teste atual tem.
- A peça 11 tem uma dívida decidida e não aplicada: trocar "você fica sem a
  proteção passiva" por "você fica sem proteção". Vai junto, na mesma versão.

A peça 13 (Legados) FECHOU na v0.39, com 81 entradas e sete vagas de Desliga
esperando peça nova — quatro delas esperam justamente equipamento. Quando
Equipamento fechar, a primeira coisa é voltar na peça 13.

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

## 1 · Legados — FECHADA na v0.39

A peça 13 está pronta: `sistema/03-mecanica/13-legados.md` + `conferir-legados.py`.
81 entradas, sete listas de Origem, mais o `Sem Técnica`. Não precisa de prompt.

O que ela deixou em aberto e que outra peça resolve:
- **As sete vagas de Desliga** — quatro esperam equipamento, três esperam a peça de
  dano e condições. O validador confere que cada vaga nomeia a peça que espera.
- **A máquina de criação do Sem Técnica** — Aptidão e Estilo da Sombra. A rota não
  pode ser "os outros menos o Fundamento", senão ninguém escolhe por vontade.
- **O `.docx` da ficha** ficou atrás do `ficha.js`, que ganhou o campo do segundo
  Legado. Regerar com `node make.js` em `05-material/gerador-ficha/`.

---

## 2 · Equipamento — EM ANDAMENTO desde a v0.41

```
Retomando o RPG da Guilda. Leia `README.md` (as nove lições), o
`sistema/ESTADO-ATUAL.md` inteiro e o `logs/CHANGELOG.md` de cima até a v0.36 —
em especial a **v0.41**, que é a passada mais recente desta peça.

O projeto está em **treze peças e treze validadores**. Esta vira a catorze, e a
contagem sobe no README, no ESTADO-ATUAL, no LEIA-ME e na entrada do CHANGELOG
ao mesmo tempo — senão o `conferir-repositorio.py` falha.

EQUIPAMENTO ESTÁ NO MEIO, e o estado dela mora em
`sistema/03-mecanica/RASCUNHO-equipamento.md`. **LEIA ESSE ARQUIVO INTEIRO
antes de propor qualquer coisa** — são 487 linhas, com as decisões já tomadas,
o que foi rejeitado e por quê, e a conta de cada número. Não refaça nada que
está lá; a conta já rodou, e três coisas que pareciam fechadas já caíram uma vez.

JÁ FECHADO — não reabra sem motivo novo:

- Duas classes de uniforme, `Traje` e `Revestimento`, três degraus, requisito
  de Força 3/5/6 e SEM gate de nível.
- Oito classes de arma, 41 nomes. O requisito de Força é **grátis**: nenhuma
  classe pede mais que 3, e 3 é o teto da criação. Ele resolve acesso, não
  balanço — que é o que a peça 5 §1 já dizia.
- **O escudo SOMA com cobrir-se.** Ele saiu da frase "uniforme, armadura e
  escudo desligam a proteção de energia" — e essa mudança precisa chegar na
  peça 8, na peça 11 §5 e na peça 11 §9. Ainda não chegou.
- A escada de escudos: proteção, requisito de Força e **teto de Destreza**,
  que é o que impede a dominância. Conferida por busca exaustiva contra o teto
  de Defesa 20.
- **RD foi levantada e morta**, e não pela conta — pelo critério do Mizuki:
  "dar RD nunca é solução, vira mais um cálculo e ninguém quer isso". Não
  proponha de novo.
- Itens comuns, em três camadas: permissão, consumível de cena, e espaço
  desligado com gatilho escrito. **A moeda ficou para depois**, e vai ser
  provavelmente preço e fornecimento.

A DEPENDÊNCIA DURA, e é por onde se retoma:

**As sete propriedades de arma são só nome na tabela.** `Alcance`, `Distância`,
`Par`, `Oculta`, `Arremesso`, `Versátil` e `Munição` não têm texto nenhum.
Enquanto forem, 15 dos 16 pares da matriz de dominância saem INCONCLUSIVO,
`Haste` e `Tiro pesado` ficam a 0,60 de estarem dominadas pela `Pesada`, e **o
validador da peça não pode ser escrito**. Isso destrava o resto.

O RESTO EM ABERTO:

- **O teto de Defesa 20 não tem dono declarado.** O §3 do rascunho derivou dele
  e a escada de escudos se apoia nele. Ou a peça 1 adota, ou esta peça declara
  que é dona — e isso decide de onde o validador lê.
- Os nomes dos três degraus de escudo. Livres na triagem: Broquel, Pavês,
  Rodela, Adarga, Tarja, Couraça, Guarda-Corpo. **A categoria continua se
  chamando Escudo** — decisão do Mizuki.
- A lista de itens comuns, e a moeda.
- `Uma mão` está dominada pela `Versátil`, e nenhum par de dados conserta
  enquanto o escudo for proteção.

O QUE A PEÇA 13 DEIXOU ESPERANDO — leia `03-mecanica/13-legados.md`:

- **Quatro vagas de Desliga** nomeiam esta peça: Descendente, Reencarnado,
  Restrição Celestial e Corpo Amaldiçoado. Um Desliga precisa de **coisa
  nomeada que já existe e que ninguém comprou** — então ferramenta amaldiçoada
  precisa ganhar propriedade nomeada para essas vagas fecharem.
- **Três Legados já citam ferramenta e são os primeiros a reler:** `Armaria`
  (Descendente), `Desde Criança` (Restrição Celestial) e `Enterrado`
  (Reencarnado).
- Ferramenta amaldiçoada **ficou fora desta peça** por decisão do Mizuki: ela
  entra em tópico próprio, com graus e forja.

E A TÉCNICA MARCIAL COBRE DOIS CASOS DIFERENTES, decidido na v0.39:

- **Corpo Amaldiçoado TEM energia amaldiçoada** — cadáver de mutação abrupta
  produz a própria. Ele tem PE, aptidões e refino normais; o que falta é
  técnica inata.
- **A Maki não tem nada** — energia zero, sem PE, sem golpe canalizado, sem
  Sentir Energia. Ela é a única que fica com as Bênçãos e a Lapidação.

PROCEDIMENTO:
- Rode os validadores antes de mexer em número, de `sistema/03-mecanica/` —
  é o que o `subir.sh` faz. Confira PULADA=0: sem `python-docx` três deles
  pulam e saem com código 0 — 3 de 5, 4 de 4 e 1 de 8, nessa ordem.
- Rode a triagem antes de batizar qualquer coisa:
  `python3 conferir-nomes.py --candidatos <nomes>`. **Ela mudou na v0.41** e
  agora separa `OCUPADO` (o nome inteiro já é termo) de `DENTRO` (o nome só
  aparece dentro de um termo composto). **DENTRO não mata** — vá ler o termo e
  pergunte se ele É aquilo. E ela continua sem pegar colisão de sentido nem
  vocabulário herdado do hobby, então confira as duas à mão.
- A peça sai **com validador junto**, com arnês de perturbação numa cópia
  isolada: conferir que a base passa antes de perturbar, e conferir o `diff`
  antes de ler o resultado.
- Me mostre no chat o que você escrever, e me mostre o que a peça já tem antes
  de entrar nela.
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
