# Retomada — a v0.168 fechou, e a v0.169 é o capítulo de mesa de `Sem Técnica`

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` e avisa. *A entrega, desde a v0.149, o `subir.sh` copia sozinho.*

> ## Estado no disco
>
> **A v0.168 está fechada e validada, e a `mensagem-de-commit.txt` da raiz é a dela.**
> *Os 25 validadores de `03-mecanica/`, os quatro de `manual/matematica/` e o `conferir-voz.py
> --estrito` saem `0` com `PULADA = 0`.* **O `conferir-repositorio.py` sai `1` por três coisas, e
> as três são da ENTREGA** — o passo 0 do `./subir.sh` resolve as três antes de rodar validador.

Leia primeiro, nesta ordem: `README.md` (a seção *"Nove lições que custaram erro"*),
`sistema/ESTADO-ATUAL.md` **inteiro**, o `logs/CHANGELOG.md` de cima até a v0.160, e então a
**peça 25** (`25-sem-tecnica.md`) e o **capítulo 25 do livro**, o `25-origens.md` da fonte.

---

## A v0.169 — o capítulo de mesa de `Sem Técnica`

**A regra existe e está escrita; o que falta é o texto longo.** *A v0.168 pôs no capítulo 25 o
mínimo para o livro parar de contradizer a peça: a seção `Criação` ganhou a semente e a tabela
`Sementes`, o `Efeito na ficha` passou a dizer que ela escreve Fundamento, e a marca de
pendência saiu.* **O que ela NÃO tem é o capítulo com a dignidade dos outros** — a peça 20 ganhou
o `42-tecnica-marcial.md` inteiro, e esta rota tem quatro parágrafos dentro do capítulo de Origens.

| a decidir | o que já está resolvido |
|---|---|
| **se ela vira capítulo próprio** ou fica dentro do 25 | a peça 20 virou capítulo próprio, e é o precedente |
| **o que entra do §5** — a Regra sair da semente | a peça 25 §5 tem os dois exemplos de frase |
| **os dois Fundamentos de exemplo** | `Redoma` e `Sutura Fria`, prontos no §9 da peça |

> **Se virar capítulo novo:** ele entra na lista de capítulos dos **três** arquivos que a
> checagem 10.1 do `conferir-repositorio.py` compara, e o `conferir-voz.py` cobra `{: .tab-titulo }`
> em toda tabela. **E o `guard_numeros.py antes.md depois.md` roda a cada arquivo**, com CADA
> diferença lida contra a linha que a carregava, mais os **quatro** builds.

## Depois dela

1. **O `BESTIÁRIO`** — os nove números com quatro donos que montar um inimigo pede.
   *Decisão da v0.161: é **máquina mais maldições prontas**, e não recolhimento puro.*
   **É o único item da fila da mecânica.**
2. **Duas dívidas que a v0.168 herdou e não pagou:**
   - **⚠⚠ `08-criacao-de-personagem.md` Passo 1 dá os ofícios ao dono errado.** *Ele diz que a
     **Origem** entrega "dois ofícios livres", e a peça 7 §6 é dona: o **Caminho** dá dois, a
     Origem dá um ou uma perícia. O total `8+3`/`9+2` só fecha pela leitura da 7.*
   - **⚠ A peça 11 §6 justifica *"o refino não escala a `Energia Reversa`"* citando uma §2 que a
     v0.158 substituiu.** *A decisão pode ficar; o argumento caiu há dez versões.* **A peça 25 §6
     já registra isso por escrito, então quem for pagar tem o diagnóstico pronto.**
3. **Uma dívida de contagem que sobrou no `sistema/LEIA-ME.md`:** *ele publica o livro em
   `230` páginas, e o build de hoje dá `245` e `142`.* **A contagem de rotas daquele arquivo foi
   consertada na v0.168; a de páginas não.**

> **`04-playtest/` continua vazia. Zero sessões desde a v0.1, e todo número do sistema é
> previsão.** *É o maior item aberto do projeto.*

---

## O que a v0.168 fechou, e vale saber

**`Sem Técnica` é a peça 25, e a nona rota de Origem roda.** *A máquina é o Fundamento inteiro,
no molde da peça 20 — dois renomes (`Manejo` e `Auge`) e uma subtração (sem Expansão de Domínio).*
**A semente é uma aptidão que vem aberta na criação, sem gate e sem gastar marco**, com três
portas: `Domínio Simples`, `Energia Reversa` e uma `Aptidão Própria`.

> **A banda `Classe Passiva 2 e 3` é DERIVADA e não escolhida.** *A escada de gate da peça 11 §5
> produz sozinha quanto cada altura antecipa — `4,0` / `9,3` / `17,3` níveis —, e só `CP 2` e `3`
> passam: `1,86×` contra `4,33×` da banda com a `CP 1`, num filtro de `3,00×`.*

**⚠⚠ Três coisas mudaram de RESPOSTA, e nenhuma delas era "corrigir".** *O `Inédito` parou de
quebrar — a peça 13 marcava desde a v0.39 que ele pressupõe técnica própria, e como a rota
escreve Fundamento ele funciona nela.* **O aviso de `Sem Técnica com o Emanador` perdeu o
assunto**, porque `Manejo` é feitiço. *E o ponteiro do `Inédito` nunca pousou: a checagem 8 do
`conferir-legados.py` confere as cinco Origens elegíveis, e a frase que prometia uma checagem em
cima daquela entrada atravessou cento e vinte e nove versões.*

**O primeiro contrato do projeto venceu, e a resposta foi não.** *A peça 22 §3.5 escreveu na
v0.134 que "quando o `Estilo da Sombra` for escrito, um estilo dele cabe no teto de um pacto".*
**Trinta e quatro versões depois: o menor `Manejo` vale `2,56` fatias contra `0,50` — `5,1×`, e
`37,0×` no Classe 7.** *Pacto não concede `Manejo`, e a linha `um estilo` do §3.3 dissolveu.*

> **⚠⚠ E DOIS validadores liam prosa como se fosse regra.** *A checagem 8 do
> `conferir-repositorio.py` joga fora as palavras vazias ao montar o slug, e `sem` é uma delas —
> o slug de `25-sem-tecnica.md` desabava para `{tecnica}`, e a peça 1, cujo item discute a
> Constituição, saía acusada de esperar a peça 25.* **A 10.6, no MESMO arquivo, já declarava esse
> defeito para título de uma palavra só.** *E a tabela de uma seção `destrava` é registro de
> entrega: a peça 25 se acusava, e a 20 e a 16 escapavam só porque escrevem `Origem` no singular.*
>
> **A checagem 5 do `conferir-orcamento.py` lia caracterização como preço** — *"uma ação que
> **gasta PE** na taxa cheia É o Fundamento" não cobra de coisa nenhuma.* **É o terceiro falso
> positivo documentado dela, e os três são o mesmo defeito de recorte.**

---

## ⚠⚠ Quatro lições que as duas últimas versões pagaram

> **1 · Prosa SOBRE a regra não é a regra.** *A v0.168 pegou isso TRÊS vezes dentro do
> `conferir-sem-tecnica.py` e mais DUAS em validadores velhos lendo a peça nova.* **É a mesma
> família da v0.151 e da v0.165, e ela reaparece toda vez que um extrator lê SEÇÃO onde devia ler
> LINHA DE REGRA.**
>
> **2 · Slug de uma palavra casa com o projeto inteiro.** *A `10.6` já sabia disso e escreveu; a
> `8`, no mesmo arquivo, não sabia.* **Guarda que existe num lugar não protege o vizinho.**
>
> **3 · Guarda que aceita o sinal em QUALQUER ponto da frase não separa nada.** *A primeira
> versão da guarda da checagem 5 procurava o verbo `é` na frase toda, e `é` está em toda frase
> daqui.* **O arnês pegou: a perturbação que tirava a identidade saía verde pelo motivo errado.**
>
> **4 · A triagem de nomes leva ~21 s e mata o seu exemplo.** *Rode
> `python3 conferir-nomes.py --candidatos Nome Outro` ANTES de batizar.*

## Método, e ele não é negociável

- **Rode os validadores ANTES de mexer em número:** os de `sistema/03-mecanica/`, o
  `conferir-repositorio.py` da raiz, os quatro de `manual/matematica/`, e o `conferir-voz.py
  --estrito` do livro. **Meça pelo CÓDIGO DE SAÍDA**, e confira **`PULADA = 0`**.
- **Todo número novo ganha validador com teste negativo**, em cópia isolada. *Confira que a base
  passa na cópia **e que a checagem nova RODOU** antes de perturbar.* **E confira que a
  PERTURBAÇÃO mudou o arquivo** — `sed` que não bate produz "não acendeu" falso.
- **Uma checagem que só sabe ler a decisão de hoje mede a decisão, não a relação.** *O
  contra-teste que vale reverte a decisão de forma COERENTE em TODOS os donos e sai verde.*
- **Nada de valor fica escrito dentro do validador.** Leia do documento dono. *A exceção é
  `limite de design`, que existe para ser comparado com a regra aplicada — é a lição nº 8, e o
  `PECAS_ESPERADAS` do `conferir-catalogo.py` é o exemplar.*
- **⚠ Marca dentro de célula de tabela quebra extrator de OUTRO validador.** Marca vai embaixo.
- **⚠ Tabela dentro de bloco de citação também quebra.** *Molde da casa: texto de abertura,
  tabela solta, e o corpo do Legado no `>` depois dela.*
- **Pesquise antes de inventar.** Os PDFs estão em `PDFs - Sistemas Extras/PDF_Sistemas/`.
- **Se mexer no livro:** `guard_numeros.py antes.md depois.md` a cada arquivo, com CADA
  diferença lida contra a linha que a carregava, e os **quatro** builds. *Mande o PDF de duas
  colunas antes de ele commitar.*
- **Se mexer no manual:** `node make.js`, `soffice --headless --convert-to pdf`, e **rode o
  controle antes de o build valer.**
- **Escolha de sabor é dele**, em rodadas curtas, com o número e o trade-off já calculados.
  **Mas não pergunte o que a conta responde.**
- **Documento não pode ter cara de saída de IA.** Português informal, nunca de Portugal.

## Onde as coisas moram

| | |
|---|---|
| as peças de regra | `sistema/03-mecanica/` — **25 peças e 25 validadores**, e os documentos dizem 25 |
| o catálogo de entregas | peça 17; os três `DESENHO-*.md` da raiz são os donos do preço |
| a fonte do livro | `sistema/05-material/livro/manual/`, 20 arquivos |
| a régua de escrita | `sistema/05-material/livro/REGRA-DE-VOZ.md` — **`3` marcas de pendência** |
| o gerador do manual | `manual/gerador/`, e o `COMO-USAR.txt` é o dono da versão dele |
| a entrega | `finalizado/`, git próprio. **O `subir.sh` copia; o commit é à mão** |

⚠ **Não rode git do sandbox.** Para ver onde a entrega está, leia `finalizado/.git/logs/HEAD`
como arquivo.
