# 18 · Progressão

**Fase 4, décima oitava peça.** O que o personagem ganha em cada nível, do 1 ao 30, numa tabela só.

**Esta peça quase não decide nada.** *Nove das dez colunas têm dono em outro documento, e o que ela faz é juntar as nove num lugar e pôr um validador que confere cada uma contra o dono.* **A décima nasce aqui, e ela nasce aqui porque não tinha dono nenhum** — é o tamanho da lista de feitiços, e está na seção 4.

---

## 1. O buraco que ela fecha, e ele era maior do que estava escrito

**O `ESTADO-ATUAL` dizia, desde a v0.32, que a progressão estava *"espalhada por cinco documentos"*.** *Contando número em vez de arquivo, são **dez**, em seis lugares.*

| o que se ganha | quem é dono hoje |
|---|---|
| maestria | peça 1 §2 |
| vida por nível | peça 1 §5.1 |
| PE por nível | peça 1 §5.3 |
| o marco, e o que ele entrega | peça 11 §3 |
| a curva de refino das três rotas | `03-mecanica/11-aptidoes-e-refino.md` §3 — *veio do `arquitetura.md` na v0.104* |
| degrau de Caminho | `DESENHO-caminhos.md` |
| entrega de Trilha | `DESENHO-caminhos.md`, na mesma linha de orçamento |
| Classe de feitiço, Classe de Passiva, Classe 0, Liberação e Técnica Máxima | manual, §9 |
| XP para subir | peça 12 §3 |
| **tamanho da lista de feitiços** | **ninguém, até esta peça** |

> **⚠⚠ A última linha é o achado, e ela é a lição nº 9 acontecendo com o número mais usado da ficha.** *A fórmula `2 + nível ÷ 2`, mais um por marco, estava escrita à mão dentro de DOIS validadores — o `conferir-aptidoes.py` e o `conferir-expansao.py` —, e em nenhum documento.* **O manual desistiu dela em v7.7, com todas as letras:** *"Quantos feitiços você conhece não é conta deste manual. O tamanho da lista vem do sistema em volta."* **E o sistema em volta não pegou.**

> *E é o inverso exato do defeito que o projeto já viu três vezes.* **Nas v0.80, v0.86 e v0.92 o projeto procurou régua que o manual já publicava.** *Aqui o manual mandou embora um número que ele carregava, e ninguém estava do outro lado para receber.*

---

## 2. A tabela

**Um personagem começa no nível 2.** *O nível 1 fica como opção de campanha — o personagem antes de ser feiticeiro.*

| nível | XP | maestria | espaços | refino | Classe | Passiva | Classe 0 | o que acontece |
|---|---|---|---|---|---|---|---|---|
| **1** | — | 1 | 2 | 1 | 1 | 1 | 2 | **Fundamento**, Passiva Livre, dois feitiços de Classe 0 |
| **2** | 100 | 1 | 3 | 1 | 1 | 1 | 2 | degrau de **Caminho** · entrega de **Trilha** |
| 3 | 100 | 1 | 3 | 1 | 1 | 1 | 2 | — |
| 4 | 100 | 1 | 4 | 1 | 1 | 1 | 2 | — |
| **5** | 200 | 1 | 4 | 1 | 2 | 1 | 3 | Classe 2 · mais um Classe 0 |
| **6** | 200 | 1 | 6 | 2 | 2 | 1 | 3 | **marco** |
| **7** | 200 | 1 | 6 | 2 | 2 | 2 | 3 | degrau de **Caminho** · libera Passiva de Classe 2 |
| 8 | 300 | 1 | 7 | 2 | 2 | 2 | 3 | — |
| **9** | 300 | 1 | 7 | 2 | 3 | 2 | 3 | Classe 3 |
| **10** | 300 | 2 | 9 | 3 | 3 | 2 | 3 | **marco** · **1ª Liberação Máxima** |
| **11** | 400 | 2 | 9 | 3 | 3 | 2 | 4 | entrega de **Trilha** · mais um Classe 0 |
| 12 | 400 | 2 | 10 | 3 | 3 | 2 | 4 | — |
| **13** | 400 | 2 | 10 | 3 | 4 | 3 | 4 | Classe 4 · libera Passiva de Classe 3 |
| **14** | 500 | 2 | 12 | 4 | 4 | 3 | 4 | **marco** |
| **15** | 500 | 2 | 12 | 4 | 4 | 3 | 4 | degrau de **Caminho** |
| 16 | 500 | 2 | 13 | 4 | 4 | 3 | 4 | — |
| **17** | 600 | 2 | 13 | 4 | 5 | 3 | 5 | Classe 5 · **Técnica Máxima** · mais um Classe 0 |
| **18** | 600 | 3 | 15 | 5 | 5 | 3 | 5 | **marco** |
| **19** | 600 | 3 | 15 | 5 | 5 | 3 | 5 | entrega de **Trilha** |
| **20** | 700 | 3 | 16 | 5 | 5 | 3 | 5 | **2ª Liberação Máxima** |
| **21** | 700 | 3 | 16 | 5 | 6 | 3 | 5 | Classe 6 |
| **22** | 700 | 3 | 18 | 6 | 6 | 3 | 5 | **marco** |
| 23 | 800 | 3 | 18 | 6 | 6 | 3 | 5 | — |
| 24 | 800 | 3 | 19 | 6 | 6 | 3 | 5 | — |
| 25 | 800 | 3 | 19 | 6 | 6 | 3 | 5 | — |
| **26** | 900 | 4 | 21 | 7 | 7 | 3 | 5 | **marco** · Classe 7 |
| **27** | 900 | 4 | 21 | 7 | 7 | 3 | 5 | entrega de **Trilha** |
| 28 | 900 | 4 | 22 | 7 | 7 | 3 | 5 | — |
| 29 | 1.000 | 4 | 22 | 7 | 7 | 3 | 5 | — |
| **30** | — | 4 | 24 | 8 | 7 | 3 | 5 | **marco** · degrau de **Caminho** · **3ª Liberação Máxima** |

**Nível em negrito é nível que entrega alguma coisa.** *São dezenove dos trinta; os onze restantes crescem em número e não em regra, e é assim de propósito.*

---

## 3. Como ler cada coluna

- **XP** é o que custa **sair** deste nível, e ele é o mesmo dentro de cada faixa de três níveis. *Uma missão padrão paga 100.* O nível 30 é o topo e não tem custo.
- **espaços** é o tamanho da sua lista de feitiços conhecidos. **Passiva é paga com espaço, e a Expansão de Domínio também; Liberação Máxima não ocupa.**
- **refino** é a **linha passiva** — o que todo mundo tem sem escolher nada. Quem escolhe Refino no marco tem mais que isso, e o teto é 10.
- **Classe** é a maior Classe de feitiço que você consegue montar. **Classe 0** é quantos feitiços grátis você carrega.
- **Passiva** é a maior Classe de Passiva que já abriu para você.

---

## 4. O tamanho da lista de feitiços — a única coisa que esta peça decide

> **Espaços de feitiço conhecido = `2 + nível ÷ 2`, arredondando para baixo, mais `1` por marco já alcançado.**

**No nível 2 são `3`. No nível 30 são `24`.**

*A parte de baixo — `2 + nível ÷ 2` — dá um feitiço novo a cada nível par, e é por isso que catorze dos vinte e nove níveis não entregam nada: são todos os ímpares, e a Trilha e o Caminho caem em cima de níveis pares que já tinham feitiço.*

**A parte de cima é a linha passiva do marco**, que existe porque Passiva e Expansão de Domínio comem espaço. *Sem ela, cinco Passivas de Classe 3 mais Expansão completa eram impossíveis em qualquer nível — dezoito espaços numa ficha de dezesseis.*

### Por que ela nasce aqui, e não em outro lugar

**O manual carregava essa contagem até a v7.6 e a devolveu na v7.7**, porque ela discordava do sistema em volta em três feitiços no nível 20 e seis no 30. *O texto dele hoje diz: "o tamanho da lista vem do sistema em volta, que é quem sabe quantos marcos você já passou".*

**E o sistema em volta não pegou.** *A fórmula foi parar dentro do `conferir-aptidoes.py` e do `conferir-expansao.py`, os dois com a mesma linha escrita à mão* — e a regra do projeto é que **nada de valor fica escrito dentro do validador**.

**Os dois passam a ler daqui.** *A tabela da peça 11 §3 que mede quanto espaço sobra para Passiva e Expansão reconstrói sem mexer em nada: `12` no nível 14, `16` no 20, `21` no 26 e `24` no 30.*

---

## 5. O que a tabela não mostra, e por quê

**Três coisas ficaram de fora, e nenhuma por esquecimento.**

| o que | por que | onde está |
|---|---|---|
| **Vida e PE** | dependem do **Caminho**, não do nível sozinho | peça 1 §5.1 e §5.3 |
| **A escolha do marco** | são três eixos e quem escolhe é o jogador | peça 11 §3 |
| **O que o degrau de Caminho e a entrega de Trilha entregam** | muda por Caminho e por Trilha — são 89 entradas | peça 17, que é o índice |

**Vida e PE cabem em duas linhas, e é por isso que elas não viram coluna:**

> **Vida:** no nível 1, a vida inicial do seu Caminho mais a sua Constituição. Em cada nível depois, a vida por nível do seu Caminho mais a Constituição de novo.
> **PE:** o PE por nível do seu Caminho vezes o seu nível.

*Uma coluna por Caminho seriam dez colunas a mais numa tabela que já tem nove, para publicar duas contas de uma linha.*

**E o atributo também fica fora**, pelo mesmo motivo do refino: a linha passiva dá `+1` por marco em cima dos nove pontos da criação, e a escolha dá mais. *Nove na criação, dezesseis de graça no nível 30, e até vinte e três para quem sempre escolhe Corpo.*

---

## 6. De onde vem cada coluna

*Nenhum valor da tabela acima foi escrito à mão. O `conferir-progressao.py` reconstrói as nove colunas a partir dos donos e compara linha a linha.*

| coluna | dono |
|---|---|
| **XP** | peça 12 §3 |
| **maestria** | peça 1 §2 |
| **espaços** | **esta peça, §4** |
| **refino** e o calendário de marcos | peça 11 §3 |
| **Classe**, **Passiva**, **Classe 0**, Liberação Máxima e Técnica Máxima | manual, §9 |
| degrau de **Caminho** e entrega de **Trilha** | `DESENHO-caminhos.md`, a linha de orçamento do topo |

> **O validador lê o manual, então ele PULA sem o `python-docx` — e diz que pulou.** *Sem a biblioteca, as colunas de Classe, Passiva e Classe 0 não são conferidas contra ninguém, e o rodapé imprime `OK, mas N checagem(ns) PULARAM` em vez de `TUDO OK`.*

---

## 7. Em aberto

- ~~**A curva de refino das três rotas mora no `arquitetura.md` §4.3.**~~ **Fechado na v0.104: ela foi para a peça 11 §3**, que já publicava a rota pura marco a marco e agora publica as três. *Com isso não sobrou nenhuma fonte de progressão fora de uma peça de regra.*
- **Esta peça é argumento de design como todas as outras, e a tabela dela é texto de mesa.** *Quando o PDF sair, a tabela vai aparecer lá também* — e aí ela vira número de dois donos, com esta peça sendo a fonte e o validador conferindo a cópia. **O quick-start era o destino previsto até a v0.102, quando ele foi abandonado.**
- **A coluna `XP` supõe missão padrão.** *A peça 12 §4 tem missão curta e longa, e a §5 tem o teto semanal; nenhuma das duas cabe numa coluna por nível.*
