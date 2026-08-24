# Retomada — o que ficou aberto depois da v0.139

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree.

Leia primeiro, nesta ordem: `README.md` (a seção *"Nove lições que custaram erro"*),
`sistema/ESTADO-ATUAL.md` inteiro, e o `logs/CHANGELOG.md` de cima para baixo até a v0.136.
As entradas v0.136 a v0.139 são as quatro últimas passadas de texto e explicam quase tudo
que está aberto aqui. A v0.139 tem uma coisa a mais: ela mexeu em **regra**, e não só em texto.

---

## Onde o projeto está

**v0.139.**

| repositório | commit | |
|---|---|---|
| raiz · `JJK---Project` | `8ff2936` | era o da v0.138; a v0.139 está no disco, sem commit |
| `finalizado/` · `JJK---PDF---RPG` | `2f0264f` | idem — o recorte foi sincronizado, falta commitar |

22 peças de regra · 22 validadores · 232 checagens. Livro em 18 capítulos, **69.972 palavras**,
238 páginas em coluna única e 138 em duas colunas. `conferir-voz --estrito` em 0 achados e
10 triagens. Manual do Fundamento na **v7.12**, 49 páginas.

**As condições são TREZE desde a v0.139** — seis `Leve`, duas `Média`, cinco `Pesada`. Se você
achar `catorze` falando de condição em qualquer lugar fora de `logs/` e de `99-arquivo/`, é
sobra: o fecho da v0.139 varreu treze desses e nenhum validador alcança prosa.

---

## 1 · O `.git` local está com 649 MB, e dá para recuperar quase tudo

**O que aconteceu:** 572 MB de PDFs de sistemas de terceiros (PHB 2024, Tasha, Guia do Mestre,
GURPS, Pathfinder, Volo, 3D&T) tinham sido versionados por acidente. Eles **nunca chegaram ao
GitHub** — quatro commits ficaram presos em `HTTP 408` justamente por causa deles.

**O que já foi feito na v0.138:** a pasta entrou no `.gitignore`, saiu do índice, e um
`git filter-branch --index-filter` reescreveu os quatro commits pendentes tirando a pasta de
dentro deles. O push caiu de **520 MB para 7 MB** e passou.

**O que falta, e continua faltando:** o `filter-branch` guardou os commits antigos em
`refs/original/refs/heads/main` — a referência ainda existe, o `.git` ainda tem 649 MB, e
enquanto ela existir o `git gc` não recolhe nada.

O conserto, **e o Mizuki é quem roda** (não rode git do sandbox):

```bash
cd "/media/mizuki/HD Externo II/Claude/Claude 2" && git update-ref -d refs/original/refs/heads/main && git reflog expire --expire=now --all && git gc --prune=now --aggressive
```

⚠ **Isso é irreversível** — depois dele não dá mais para voltar aos commits com os PDFs dentro.
Confirme antes que os 8 PDFs continuam em `PDFs - Sistemas Extras/PDF_Sistemas/`, porque eles
são o corpus de medida e precisam ficar no disco.

---

## 2 · O pente fino agora cobriu 15 capítulos de 21, e faltam quatro mais o início rápido

**Passados a fundo até aqui:** 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 18, mais a introdução
e o vocabulário.

**NÃO passados linha a linha:** **2** (*O Turno*), **15** (*Invocações*), **16** (*Pactos*),
**17** (*Experiência e Progressão*), e o **início rápido**.

*A medida de prosa solta desses continua alta — o `11-o-turno.md` deu 42% —, e a leitura da
v0.139 confirmou o que a v0.138 só tinha suposto:* **quase tudo ali é regra escrita em frase
curta, e não narrativa.** A marca serve para escolher onde olhar, e nada mais; quem decide é
a leitura. O `METODO-passada-de-texto.md` do livro escreve isso por extenso.

> **O que a leitura acha e a medida não:** os dois achados grandes da v0.139 foram ponteiros
> para coisa que não existe — a *"Passiva `Reversão`"* no capítulo 5, e as Famílias Livres
> nomeadas errado no capítulo 10. **Nenhum regex pega frase gramaticalmente perfeita que fala
> de uma coisa que nunca foi escrita.**

---

## 3 · O que a v0.139 mexeu em REGRA, e o que isso reabre

**O `Petrificado` saiu, por decisão sua.** *A peça 19 registra a remoção, o motivo e o que
ficou no lugar do argumento que ele carregava.*

**A Restrição `Lento` virou `Atrasar`.** *O nome era duas regras ao mesmo tempo — a Restrição
de Ação Completa e a condição de deslocamento pela metade. A condição ficou com o nome.*

> **⚠ E o que NÃO se reabre:** a partição em três degraus. *A v0.139 tentou refazer o corte
> depois de o `Petrificado` sair, achou uma partição de `2,44×` contra os `4,26×` publicados,
> aplicou, rodou os validadores e desfez.* **A banda obriga a partição — o `Lento` e o
> `Incapacitado` cabem em `Leve` pela conta, e subir os dois para `Média` cobra caro do
> jogador.** *Está escrito na peça 19 §3.6 com o número; não refaça a busca.*

**Duas dívidas de preço continuam abertas e marcadas nos donos:** o `Desarmado`, que custa zero
para quem carrega arma reserva (peça 19 e peça 3 §3.2), e o par `Guiar`/`Estampido`/`Ajudar`,
que se repreçaria junto.

---

## 4 · A fila de mecânica, que não mudou nas quatro últimas versões

Imediatas, na ordem em que fazem falta:

| peça | o que ela resolve |
|---|---|
| **Itens iniciais por Caminho** | levantado na v0.135. A criação dá perícia, ofício, Trilha e técnica, e não diz com que equipamento o personagem sai de casa |
| **Itens menores** | levantado na v0.131. Consumível, talismã pronto, remédio, corda, o kit do `Herbalismo`. Nada tem preço nem lista |
| **Três Trilhas do Evocador** | `Servo`, `Matilha` e `Coro` dão o corpo da invocação, e as entregas dos níveis 2, 11, 19 e 27 não existem |

Depois delas: **Estilo da Sombra** e **Aptidão como rota** (as duas que fazem a `Sem Técnica`
fechar ficha — hoje é a única rota de Origem que não roda), **dano de alma com Essência na
Integridade** (decidido, nunca aplicado), **bestiário**, e a decisão de ligar ou não o
`Bloquear`, que continua em `03-mecanica/RASCUNHO-bloqueio.md`.

Duas vagas declaradas no livro: o **nível 27 do `Arremate`** e o **`Desliga` do Corpo Amaldiçoado**.

**E o que faz falta de verdade não está nesta lista:** `04-playtest/` continua vazia, zero
sessões desde a v0.1, e todo número do sistema é previsão.

---

## 5 · Decisões suas que valem como régua daqui para frente

**Um Legado nunca diz o que o PNJ faz.** Ele diz o que existe no mundo por sua causa, o que você
sabe, ou onde você entra. *Isso saiu de ler o PHB 2024 — o antecedente de lá entrega atributos,
um Talento, perícias, ferramenta e equipamento, e nenhuma característica social.*

**Toda entrada de Legado tem três partes fixas:** o que você escreve na ficha · **o que você
ganha, em voz direta** · o que isso limita. A linha `Na mesa:` diz em que cena aquilo aparece,
com um exemplo curto.

**Tabela-prévia sai, tabela de contraste fica.** Critério da v0.106.

**Analogia e `em vez de` NÃO se cortam.** Medido contra os quatro livros do hobby: nas duas o
projeto já escreve como eles escrevem. *E a v0.139 mediu a analogia **abaixo** do piso deles.*

**As cinco marcas de "isto ainda está sendo escrito" ficam.** Decisão da v0.129: quando a frase
de estado carrega uma permissão ou um limite que o jogador precisa, ela fica.

**Quando um bloco sai, a frase que anuncia ele sai junto, no mesmo commit.** *Aconteceu três
vezes em duas versões, e as três estavam gramaticalmente perfeitas.*

---

## Como fechar qualquer coisa aqui

- `guard_numeros.py` em **cada** arquivo mexido, com **cada** diferença explicada antes de aplicar
- `conferir-voz.py --estrito` de volta em 0 achados, e as triagens relidas
- os 22 validadores de `sistema/03-mecanica/`, o `conferir-repositorio.py` da raiz e os dois de
  `manual/matematica/` — todos com **PULADA = 0**, e o sucesso medido pelo **código de saída**
- os builds regerados: `build.py`, `build.py --duas`, `build_docx.py` e `build_txt.py`.
  *São os três do recorte mais o `Projeto-M-Manual-da-Guilda-TEXTO.md`, que é
  versionado e envelhece calado*
- **se mexeu no `manual/gerador/`**, o manual também: `node make.js`, `cp` para `manual/`, e
  `soffice --headless --convert-to pdf` — com o `pac7.py` rodado antes
- entrada nova no `CHANGELOG`, que é a dona da versão, e a versão subida nos cinco documentos
  (`README`, `ESTADO-ATUAL`, `LEIA-ME`, este arquivo, e o `README` de `finalizado/`)
- cópia para `finalizado/` do que mudou, e as **duas** mensagens de commit
- **você não commita:** deixa as mensagens prontas e avisa

> **⚠ Verde não é fim.** *Na v0.139 os 22 validadores passavam com `PULADA = 0` e treze lugares
> ainda diziam `catorze`, mais uma paginação publicada como `46` que é `49`.* **Contagem escrita
> em frase não tem dono no projeto** — a checagem 9 confere contagem de arquivo, não de prosa.
> **Quando fechar peça, releia as listas à mão.**

⚠ **Não rode git do sandbox.** Para ver onde o repositório está, leia os arquivos:
`.git/refs/heads/main` (local) e `.git/refs/remotes/origin/main` (remoto). São arquivos de texto
e não criam lock.
