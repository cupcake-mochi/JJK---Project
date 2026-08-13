# RASCUNHO — Invocações

**Isto é o planejamento da peça, não a peça.** Levantamento engatilhado: o que já está travado, o que a pesquisa externa achou, e as perguntas na ordem em que uma trava a outra. Sem número no nome de propósito — meia peça não é peça, e um arquivo com dois dígitos na frente quebraria a contagem de catorze por catorze.

Escrito na **v0.50**, quando a fila foi reordenada. Ele vira a peça 15 quando fechar — e só aí ganha número no nome, junto com o validador dono dela e com a contagem subindo nos três documentos ao mesmo tempo.

---

## 1. O que já está decidido, e não se rediscute aqui

Três coisas chegam prontas. Elas não são ponto de partida para conversa — são o contorno dentro do qual a peça tem que caber.

> **Você e todas as suas invocações somados entregam uma Rotina.**
> Com uma invocação, cada um entrega metade. Com três, cada um entrega um quarto.

Isso é a **peça 6, seção 4**, e o argumento por trás dela está escrito lá com a tabela: uma invocação que age sozinha **dobra** o dano por rodada, três **quadruplicam**, e no nível 30 a horda chega a `504` contra uma Rotina de `126`. A peça 6 fecha dizendo que isso **não tem conserto por preço** — não é recurso, é economia de ação.

As outras duas:

- **O Coro não custa nada a mais** (peça 6 §3.1). O dono e a invocação agem no mesmo turno, e sai de graça porque o orçamento dividido é **teto de saída, não de número de ações**. Isso já foi decidido na v0.24 e conferido de novo na v0.34.
- **O Caminho não dá dados de dano** (peça 5 §4, reconfirmada). O que sobra para o Evocador conceder é posicionamento, alvo, duração, recuperação, troca do fixo do acerto por atributo, e exceção estreita e paga na economia de ação.

**E o Fundamento não produz invocação hoje.** Conferido no `.docx` da v7.8: `Invocação` aparece **só como Tema**, no grupo *Criação* do catálogo do apêndice — e Tema não tem efeito mecânico (o manual diz isso na abertura da Descrição). Não existe Forma nem Melhoria que ponha um corpo que age no campo. Então não há duas portas para a mesma coisa, e a peça não corre o risco de contar o mesmo poder duas vezes — **que era a suspeita óbvia, e a checagem desmentiu.**

## 2. O que a pesquisa externa trouxe, e é aqui que aparece o buraco

Quatro levantamentos, e o achado que interessa não é sobre dano.

**PF2e, Summoner.** O eidolon não é um segundo personagem: existe uma ação chamada `Act Together` em que o número de ações gastas decide quantas cada um dos dois recebe, e o eidolon tem que ficar a até 30 m do dono. **É a mesma intuição da peça 6 §4 num eixo diferente** — lá se divide saída de dano, aqui se divide ação. Vale como confirmação de que o formato é o certo, não como coisa a importar.

**5e 2014, `conjure animals`.** O modo de falha mais documentado do hobby, e ele tem **duas metades**:

| metade | o que acontece | a peça 6 §4 cobre? |
|---|---|---|
| dano e economia de ação | oito lobos fazem mais que qualquer feitiço de mesmo círculo | **sim** |
| **tempo de mesa** | o combate para. Os outros jogadores esperam vendo oito lobos morderem, um de cada vez | **não** |

**5e 2024 trocou a família inteira por causa da segunda metade**, e o motivo publicado é operacional: mestre tendo que abrir ficha de monstro, ter miniatura para todos, e o combate travando. A saída deles foi **uma criatura só**, espectral, ocupando um tile, que **não se divide** e que **age na iniciativa do dono**.

**13th Age, mooks.** Quando o sistema quer horda de verdade, ele para de tratar corpo como corpo: o dano se contabiliza contra **o bando inteiro** e um mook tem um quinto da vida de um monstro normal, com o excedente cascateando para o próximo.

> **O buraco, dito direto: a regra da peça 6 §4 preça o dano da Matilha e não preça o tempo dela.** *"Um quinto da Rotina em cada, cinco corpos no campo"* é justamente a montagem que os dois sistemas acima tiveram que construir máquina especial para segurar. **Cinco fichas agindo por rodada custa o mesmo tempo de mesa quer cada uma faça 25 de dano ou 5.**
>
> E o projeto **já mede esse eixo** — a lista de playtest do `ESTADO-ATUAL` pergunta *"alguém usa ação bônus?"* com a justificativa *"é a peça mais herdada do turno e a que mais custa tempo de mesa"*. O eixo existe; ninguém tinha apontado ele para cá.

## 3. As perguntas, na ordem em que uma trava a outra

**Q1 — a invocação tem iniciativa própria, ou age na do dono?**

Trava tudo o que vem depois, e é a única em que o sistema de fora já tem resposta testada. A iniciativa aqui é individual (`d20 + Destreza`), então sem uma frase explícita cada invocação abre uma casa nova na ordem. **É a decisão que compra ou gasta o tempo de mesa da Matilha**, e ela precisa vir antes de qualquer número.

**Q2 — a Matilha é cinco fichas ou uma ficha com cinco corpos?**

Depende da Q1. Se for cinco fichas, o custo de tempo é real e a Trilha precisa pagar por ele de algum jeito. Se for uma ficha só — no molde do mook, com vida somada e dano do bando —, a Matilha fica barata de rodar e a pergunta vira se ela ainda parece uma matilha na mesa. **Não decidir isso por gosto: as duas saídas têm precedente e as duas têm preço medido.**

**Q3 — de onde sai a ficha da invocação?**

Nada no projeto diz o que uma invocação **é**: quanta vida, que Defesa, que acerto. As candidatas óbvias são derivar do dono (nível, refino), derivar da tabela de inimigo do manual — que é a tabela cujo dono declarado é **o playtest**, e ninguém jogou —, ou escrever escada própria. **Cuidado com a lição nº 9 aqui:** se a ficha da invocação copiar número de outra peça, ela precisa de dono declarado ou de validador que compare os dois.

**Q4 — invocar custa o quê, e quando?**

PE, ação, espaço de feitiço conhecido, ou nada. O `conferir-orcamento.py` existe porque o bolso já é apertado, e o `ESTADO-ATUAL` avisa que **qualquer moeda nova passa por ele antes de ter número** — isso já foi escrito a respeito dos *pontos de feitiço* do Emanador e vale igual aqui.

**Q5 — a invocação morre como?**

E o que sobra do orçamento dividido quando ela morre. Se o dono recupera a Rotina inteira ao perder a invocação, matar a invocação **fortalece** o invocador, que é o inverso do que a ficção pede. Se não recupera, o Evocador vira o Caminho que pode ser desligado por um acerto de sorte. **Nenhuma das duas pontas serve, e o meio precisa de conta.**

**Q6 — as três Trilhas com número.**

`Servo`, `Matilha` e `Coro` já têm uma linha de descrição cada na peça 6 §2, e nada mais. Elas fecham **junto com a peça de Trilhas**, não aqui — mas a peça de Invocações tem que deixar as três construíveis, senão a peça de Trilhas trava de novo no mesmo lugar.

## 4. O nome da peça precisa de triagem, e o óbvio está ocupado

Rodada a triagem antes de escrever qualquer coisa:

| candidato | veredito |
|---|---|
| `Invocação` · `Invocacao` | **OCUPADO** — é Tema no manual |
| `Vínculo` | **OCUPADO** — é Tema no manual |
| `Servo` · `Matilha` · `Coro` | **OCUPADO** — já são Trilhas do Evocador |
| `Coleira` · `Convocação` | LIVRE |

**Não é impeditivo, e é preciso saber por quê.** Tema do manual não carrega mecânica, então o choque é de vocabulário e não de regra — mas a lição nº 4 manda checar nas duas direções antes de batizar, e o `conferir-nomes.py` compara literal. **Se a peça se chamar Invocações, isso tem que ser decisão escrita e não descuido**, com uma linha dizendo que o Tema e a peça são coisas diferentes. As duas livres estão anotadas aqui só para não se perderem; a escolha é do Mizuki.

## 5. O que o validador vai precisar ter

Anotado agora porque é mais barato do que descobrir depois — e porque a peça 14 gastou três versões com uma frase dizendo que o validador dela não podia ser escrito.

- **O teto da Rotina somada**, derivado da peça 6 §4 e nunca lido de constante — a lição nº 8 na forma que já apareceu três vezes.
- **Dominância entre as três Trilhas**, com a matriz rodando por quantidade de corpos.
- **O somatório**, contra o `conferir-orcamento.py`: invocar não pode caber junto com conjurar e levar dano de alma se o bolso não fechar.
- **Tempo de mesa**, se a Q2 fechar em cinco fichas — e essa não é checagem de código, é pergunta de playtest com número esperado escrito antes da sessão.
- **Triagem de todo nome** que a peça criar.

## 6. O que esta peça destrava

| destrava | como |
|---|---|
| **O Evocador** | 1 dos 5 Caminhos. Hoje ele escolhe Trilha na criação e não recebe nada por ela |
| **3 das 15 Trilhas** | `Servo`, `Matilha` e `Coro` **são** o sistema de invocação visto de dentro. As outras doze já estão desbloqueadas desde que Equipamento fechou |
| **A peça de Trilhas** | é a última dependência dela. Com Invocações fechada, as quinze ficam escrevíveis de uma vez |

**O que ela não destrava:** rota de Origem nenhuma. As nove continuam 6 jogáveis e 3 paradas — isso é da corrente de `ferramenta amaldiçoada` → `Técnica Marcial`, que é a peça seguinte na fila.
