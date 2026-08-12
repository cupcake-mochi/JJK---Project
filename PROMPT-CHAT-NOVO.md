# Prompts para os chats novos

Um chat por peça. **Antes de abrir qualquer um deles:** `./subir.sh` e depois
**"Sync now"** no Project — senão o chat novo lê o commit anterior e discute
número que já mudou.

Copie o bloco inteiro da peça que for fazer.

---

## 1 · Legados — o próximo

```
Retomando o RPG da Guilda. Leia `README.md`, `sistema/ESTADO-ATUAL.md` e o
`logs/CHANGELOG.md` de cima até a v0.32 — as sete últimas versões foram densas,
e as três da ponta são de método e não de regra.

Estamos na v0.36, manual na v7.8, doze peças e doze validadores em
`03-mecanica`. A ficha de personagem saiu na v0.35 e está em `05-material/`,
com o gerador dela. A fila das próximas quatro peças está escrita no
ESTADO-ATUAL, na seção "A fila decidida com o Mizuki na v0.36" — leia ela antes
de qualquer outra coisa, porque ela tem as colisões já levantadas.

A peça de agora é a **1: Legados**, e ela tem duas metades nesta ordem:
a régua de magnitude primeiro, o catálogo depois.

Hoje são catorze Legados, dois por Origem, na peça 9. O defeito registrado
deles não é quantidade — é magnitude: a faixa vai de "Irmãos" (sente outro Feto
por perto, zero em rolagem) a "Não Sou Gente" (imune a veneno, doença e ao que
ataca corpo humano). A trava escrita, "não produz dano e não escala com nível",
não pega imunidade. Eu quero uns cinco por Origem mais a opção de criar o
próprio — o que quase triplica a lista, então a régua tem que vir antes ou o
defeito triplica junto.

Rode os validadores antes de mexer em número, sempre de `sistema/03-mecanica/`
— de outro diretório três deles pulam checagem em silêncio.

Antes de batizar qualquer Legado novo, rode
`python3 conferir-nomes.py --candidatos <nomes>`. Ela já matou mais de dez
nomes que pareciam livres.

E leia as nove lições do README antes de escrever conta nova. A peça 9 é uma
das três que nunca teve validador, e é de peça sem validador que saíram os dois
erros da v0.34 — então esta sai com validador junto.

Me diga o que você acha da régua antes de escrever o catálogo.
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
