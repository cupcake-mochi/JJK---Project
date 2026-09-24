# Sessão de 24/09/2026 — a pesquisa dos anti-domínio, conferida, e as rodadas 1 e 2 da revisão

*Registro da conversa que fechou da v0.265 à v0.267, feita numa sessão na nuvem, no branch `claude/jjk-anti-dominios-research-59hjly`.* **É histórico datado, não dono de nada:** *a regra mora na peça 11, o porquê de cada versão mora no `CHANGELOG`, e a fila mora no `ESTADO-ATUAL`. Este arquivo guarda o que só a conversa tinha — o pedido, a ordem em que as coisas aconteceram, as palavras do Mizuki em cada decisão, e as lições de método.*

---

## 1 · O pedido

> *"eu gostaria que você fizesse uma pesquisa aprofundada em cada anti dominio, quais são seus 'drawbacks', tanto olhando na obra quanto em foruns, e também olhando o como eles 'caem', nenhum pode durar pra sempre né"*

As quatro: `Cesta Oca de Vime` (彌虚葛籠), `Domínio Simples` (簡易領域), `Pétala` (落花の情) e `Extensão de Domínio` (領域展延).

**Licença da rodada, decisão dele:** exatamente três agentes em paralelo; nenhum arquivo fora dos três deles; nada no `main`, sem merge e sem PR. **O "salvo" era o push:** cada agente rodava `/tmp/salvar.sh <arquivo> "<mensagem>"` a cada bloco, porque uma rodada anterior escrevia só no fim, caiu num `429` e perdeu tudo.

## 2 · O que aconteceu, em ordem

| etapa | o que foi | arquivo em `sistema/01-pesquisa/anti-dominios/` |
|---|---|---|
| três agentes em paralelo | a obra; os fóruns japoneses; os fóruns ocidentais | `I-queda-e-custo-na-obra.md` · `J-drawbacks-foruns-japoneses.md` · `K-drawbacks-foruns-ocidentais.md` |
| o `H` atualizado | a terceira rodada entrou no resumo, com uma seção "como cai" por técnica | `H-resumo-das-quatro.md` |
| uma frente curta | os cinco pontos que as três deixaram abertos | `L-cinco-pontos-em-aberto.md` |
| páginas do mangá | o Mizuki mandou os caps. 108, 171, 249, 258, 266 e 267; lidas quadro a quadro, **as imagens não entram no repositório** | `M-paginas-conferidas.md` |
| verificação cega | um agente conferiu `118` afirmações do `H` contra a fonte, sem aceitar a conclusão dos outros arquivos; `85` confirmadas, `26` corrigidas | `N-verificacao-do-H.md` |
| v0.265 | a pesquisa conferida entrou nos documentos de retomada; nenhum número se moveu | — |
| v0.266 | rodada 1: as frases da peça 11 que atribuíam à obra o que ela não faz | — |
| a conta da Cesta | modelo com regressão contra os números publicados | `conta-cesta-oca.py` |
| v0.267 | rodada 2: a `Cesta Oca` reescrita, e ela vira a base das outras três | — |

## 3 · O que a pesquisa concluiu, em cinco linhas

*O detalhe mora no `H`; isto é só o mapa.*

- **Nenhuma das quatro tem relógio próprio na obra: todas caem por fora.** *Esgotamento puro nunca aparece.*
- **A `Cesta Oca` racha com golpe no dono** (cap. 266, soco de alma) **e é largada para o golpe grande** (251); **a Expansão sozinha não a quebra.**
- **O `Domínio Simples` cai pela pressão do domínio** (206, 226, 258) **ou pelo voto do usuário** (Miwa, cap. 40) — **nunca por golpe no dono dentro de domínio.**
- **A `Pétala` cai com soco comum do dono do domínio** (108, pelo anime e pelo efeito) **e é largada para abrir o domínio** (227).
- **A `Extensão` é largada para usar a técnica; técnica de saída alta passa em parte** (232). **`中和` como atenuação só tem cena nela** — a `Cesta` e o `Simples` protegem inteiro até cair.

**Seis coisas a obra não amarra, e são desenho:** custo de energia, limite de tempo, `Extensão` junto com a técnica reversa, `Cesta` com encantamento próprio, `Kamo` usando a `Pétala`, e como se aprende a `Cesta`.

## 4 · As decisões do Mizuki, com as palavras dele

### Rodada 1 (v0.266) — as frases da peça 11

**"1 - Pode aplicar."** *Cinco frases que diziam "a obra faz X" sem base: os preços "vêm da obra", a `Cesta` "exatamente o que ela é na obra", o raio "da obra" (é o da Miwa), o Kusakabe "é coisa da Trilha dele" (nenhuma Trilha do sistema faz isso), o Gojo "nunca tinha usado" a `Pétala`, e "não para ataque físico".* **Nenhuma regra mexida.**

### Rodada 2 (v0.267) — a `Cesta Oca`

*Foram medidas a opção 2 (mãos presas no lugar do turno) e a 3 (ela cai).* **"a 3 é algo que precisamos medir de qualquer forma e é o motivo disso tudo, temos de analisar o como anti domínios caem, quanto tempo duram, o que dão, o que não dão e afins."**

| pergunta | a resposta dele |
|---|---|
| o que faz ela cair | **"Golpe no dono. Expansão não quebra a cesta se o alvo estiver mantendo o símbolo."** |
| com quantas falhas | **"Metade da Essência, como na corrida."** |
| o que ela cobra de pé | **"Mãos presas, já é o suficiente. Não faria sentido comer o turno inteiro."** *E:* **"não precisa comparar ainda, vamos usar a cesta de base."** |
| e se soltar o símbolo | **"Soltar permite que a cada acerto da expansão (caso tenha letal) reduza uma falha (max de 1 por rodada)."** |
| o Desarmado vale | **"Vale, mas um chute não é segurar uma arma, então ainda tem seu drawback."** |
| que ação levanta | **"Reação contra expansão, ou ação bônus no próprio turno."** |
| levantar de novo | **"dá pra levantar, as falhas zeradas, mas tem uma recarga de rodadas igual a metade da essência (min 1)"** — *com a alternativa dele de "só duas rodadas"; ficou a metade da Essência, que é o mesmo número das falhas.* |
| o requisito do livro | **"E os requisitos ficam."** *(ser Reencarnado, ou treinado em `História`)* |

**Aplicado sem pergunta, por já existir regra:** *o teste é Vigor contra a CD de quem te feriu, um por golpe (a concentração da v0.253); e a cláusula da corrida — o teste não ocupa a Concentração, e a Mão Firme não protege dele. O PE continua zero.*

## 5 · As lições de método desta sessão

1. **Técnica que deixou de ser desenhada não prova que caiu.** *O 249 p. 16 mostra o Sukuna lutando sem a esfera desenhada, entre a ativação e a fala de que continua usando a Cesta.* **O que prova queda é o efeito — o acerto alcançar o dono — ou o texto.**
2. **Quem coordena lê o arquivo do agente, não o relatório dele.** *Um "desacordo" sobre o cap. 254 era só a frase do relatório; o arquivo concordava com os outros dois.*
3. **Agente não contorna proteção de acesso.** *O `L` leu o balão do vol. 28 remontando as páginas embaralhadas do leitor da amostra da Shueisha; a verificação não repetiu, e o dado voltou a **não conferido**.*
4. **Cópia de frase se procura pelo sentido, não pela redação.** *A v0.266 corrigiu "não para ataque físico" na peça 11 e deixou passar a mesma coisa no livro, escrita "não vale contra ataque físico"; a v0.267 pegou.*
5. **Imagem em preto e branco: só se afirma o que se tem certeza** *(pedido do Mizuki).* *Duas leituras discordaram em três pontos das páginas, e a verificação resolveu pelos resumos japoneses.*

## 6 · O que ficou pendente

- **Trazer o branch para a pasta de trabalho e para o `main`** — *nada disso está no `main` ainda.*
- **Refazer o `.docx` e os dois PDFs do livro** *(só o texto corrido foi regenerado na nuvem; o PDF depende das fontes da pasta de trabalho)* **e rodar o `subir.sh`**, que copia as peças 11 e 25 para a entrega e confere os 31 com a `finalizado/` presente.
- **Sincronizar a entrega (`finalizado/`, que commita à mão) e o Project.**
- **Rodada 3:** o `Domínio Simples`, a `Pétala` e a `Extensão`, com a `Cesta` de base — *e só depois a comparação das quatro.*
- **Divergência livro × peça no `Domínio Simples`**, *que espera a rodada 3: o livro dá refino 3 (a peça, 4), o requisito "ter visto um sendo usado, ou ter aprendido com alguém", e diz que ele anula "os efeitos" da Expansão (a peça, só o Acerto).*
- **O balão do cap. 246 no vol. 28** — *quem tiver o volume confere se o 薄める virou 弱める.*
- *A nota de pesquisa do bestiário que cita o raio de 2,21 m fica como está: é nota de campo.*

**A ordem de tarefas da próxima conversa — trazer o branch, refazer o livro, e a rodada 3 começando pelo `Domínio Simples` — está no `PROMPT-continuar.md` da raiz.**

## 7 · Onde está cada coisa

| o quê | onde |
|---|---|
| a regra das quatro | `sistema/03-mecanica/11-aptidoes-e-refino.md` §6.5 |
| a mesma regra no livro | `sistema/05-material/livro/manual/45-aptidoes-e-refino.md` |
| o resumo da pesquisa, com as catorze divergências | `sistema/01-pesquisa/anti-dominios/H-resumo-das-quatro.md` |
| a verificação cega | `sistema/01-pesquisa/anti-dominios/N-verificacao-do-H.md` |
| as páginas lidas | `sistema/01-pesquisa/anti-dominios/M-paginas-conferidas.md` |
| a conta da Cesta | `sistema/01-pesquisa/anti-dominios/conta-cesta-oca.py` |
| as saídas medidas do `Domínio Simples` contra a Expansão sem Barreiras | `sistema/03-mecanica/RASCUNHO-expansao-sem-barreira.md` §8.4 |
| a conta da concentração na corrida, que a Cesta reusa | `manual/matematica/casca-sem-barreira.py` |
| o porquê de cada versão | `logs/CHANGELOG.md`, entradas `0.265` a `0.267` |
