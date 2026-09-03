# Continuar o Projeto - M — o exemplo guiado de invocação

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` na raiz e me avisa.

## Confirme a pasta antes de qualquer coisa

```bash
cd "/media/mizuki/HD Externo II/Claude/Claude 2" && grep -c "^## Nove lições" README.md
```

Tem que dar `1`. Se der `0`, é a pasta errada — **pare.** Existe um clone velho na v0.27
dentro da home que tem a cara deste projeto.

**E não rode git do sandbox, nem `status`.** Para saber em que commit a pasta está, leia
`.git/logs/HEAD` como arquivo.

## Leia nesta ordem

1. `README.md` — as **nove lições que custaram erro**, e elas moram só lá
2. `sistema/ESTADO-ATUAL.md` — inteiro, incluindo a seção final *"Onde estamos, e o que
   falta"*. Ele trunca; se vier aviso de leitura parcial, continue do offset
3. `logs/CHANGELOG.md` — as entradas da **v0.201 à v0.206**
4. `sistema/05-material/livro/REGRA-DE-VOZ.md` — como o livro escreve

## Onde o projeto está

**v0.206, commitada.** Manual do Fundamento na **v7.25**. Vinte e seis peças de regra e
vinte e seis validadores em `sistema/03-mecanica/`, mais o `conferir-repositorio.py` e o
`conferir-voz.py`.

A peça 26 — o Bestiário — **não tem mais trabalho de régua em aberto.** As seis últimas
versões foram quase todas nela:

- **v0.201** — a pressão do chefe triplicou, medida contra o Guia do Mestre de 2014 e o
  chefe solo do Pathfinder 2e. Chefe do nível 30 em `219` de dano por rodada e `945` de
  vida; ele entrega 90% da vida de um personagem por rodada, a luta dura 3 rodadas, e ele
  derruba `2,70` pessoas se concentrar.
- **v0.202** — o Kokusen base parou de custar marco: é regra de mundo.
- **v0.203** — entrou a aptidão `Circulação`, e ficou medido que cura em combate é troca
  ruim nos dois lados da mesa.
- **v0.204** — a Expansão de Domínio de inimigo dobra quantos personagens ele exige.
- **v0.205** — o `§6.5`: o inimigo não ganhou catálogo de traços próprio, ganhou o **câmbio
  do catálogo do jogador**. Três portas: a técnica paga no orçamento de feitiço da ação
  (`golpe ÷ 4,5`, piso na `Classe 1`), a aptidão paga na cota de dano por rodada
  (`1` PE por rodada `= 5,14` de dano), e o que dá vida efetiva paga em degrau de
  categoria.
- **v0.206** — a coluna de capanga da `Classe 1` abriu, e para abrir a linha do nível 2 teve
  de ser consertada: ela publicava `115` de vida onde a regra da própria seção pede `114`, e
  um ponto punha o chefe vivo numa quarta rodada.

## O que vem em seguida — e é escolha minha, já feita

**O exemplo guiado de invocação, no capítulo 60 do livro.**

O `Fundamento` tem um exemplo guiado para feitiço e ele funciona: cinco passos numerados,
depois um feitiço montado do zero passo a passo, uma tabela de ficha pronta no fim, e uma
caixa de **erros comuns**. Está em `manual/gerador/partC.js`, e o feitiço é o `Corte
Medido`.

O capítulo 60 (`sistema/05-material/livro/manual/60-invocacoes.md`) tem **dezoito seções**,
com `Orçamento`, `Limites do orçamento`, `Catálogo`, `Traço`, `Comando` e nove `Montagens de
exemplo` — **e não tem o passo a passo.** Quem lê vê a máquina e vê o resultado pronto, e
não vê a conta acontecendo.

O que eu quero:

1. **Leia a peça 15** (`03-mecanica/15-invocacoes.md`) e o capítulo 60 antes de escrever
   qualquer coisa, e me mostre o que eles têm hoje.
2. **Ache os passos que a montagem realmente tem** — eles existem espalhados; não invente
   uma ordem nova.
3. **Traga a invocação que vai ser montada como exemplo, com opções**, e eu escolho. Ela
   não pode ser uma das nove montagens já publicadas.
4. **A caixa de erros comuns sai de coisa medida**, não de palpite: a peça 15 e o
   `conferir-invocacoes.py` já sabem o que reprova.

Isso mexe no **livro**, então os quatro builds rodam no fim, e eu quero o PDF de duas
colunas antes de commitar.

## Depois dele, a fila

- **Catálogo de maldições prontas.** A decisão da v0.161 é "máquina mais prontas", e a
  máquina está entregue desde a v0.198. Ele espera a minha lista, e antes disso eu quero o
  **piso de quantas** e **de onde tirar os exemplos** — os dois medidos, não chutados.
- **`04-playtest/` continua vazia. Zero sessões desde a v0.1**, e todo número do sistema
  ainda é previsão. É o maior item, e ele não está em lista nenhuma.

## Como trabalhar aqui

- **Número vem de conta rodada, nunca de intuição.** Se eu disser que algo está
  desbalanceado, meça antes de concordar — e me diga quando a conta me desmentir.
- **Antes de propor mecânica nova, pesquise** como outro sistema resolve o mesmo problema.
  Os PDFs estão em `PDFs - Sistemas Extras/PDF_Sistemas/` — 5e (PHB 2024, Guia do Mestre,
  Volo, Tasha), Pathfinder 2e, GURPS 4ed e 3D&T. Na v0.205 a pesquisa decidiu a **forma** da
  peça e não só o conteúdo, e eu tinha pedido isso.
- **Escolha de sabor é minha.** Traga as opções com o número e o trade-off de cada uma já
  calculados, e pergunte. **Mas não pergunte o que a conta responde** — e não me devolva
  decisão que já está fechada como se fosse nova, o que aconteceu na v0.205.
- **Todo número novo ganha validador com teste negativo.** Perturbe numa cópia isolada,
  confira que a base passa antes com `PULADA=0`, e confira com `diff` que a perturbação
  bateu. E ponha contra-teste coerente — **mirado no que a checagem mede**, senão ele acende
  outras quatro e não prova nada.
- **Nada de valor fica escrito dentro do validador:** leia o número do documento dono.
- **Nome se confere com `conferir-nomes.py --candidatos` ANTES de escrever**, não depois.
- **Código novo se escreve pelo bash**, com `cat > arquivo <<'EOF'`. Para `.md` a ferramenta
  serve. E confira lendo de volta.
- **Escreva no meu registro:** negrito abrindo com a regra e a razão logo depois, "você"
  falando com o leitor, frase encadeada por vírgula em vez de aforismo, parêntese para a
  exceção curta.
- **Antes de fechar versão, releia o que VOCÊ escreveu** procurando antítese, frase teatral,
  tabela inútil e texto desnecessário. Na v0.205 essa passada achou dois erros meus de
  conteúdo, não de estilo.
- **Fale comigo diferente de como escreve o documento.** Uma ideia por parágrafo, frase
  curta, sem `§3.4` no meio da frase. Se eu disser que não entendi, a resposta certa é MENOS
  detalhe, recomeçando de mais atrás — e procure o defeito na régua antes de reexplicar.

## A ordem de fechar versão

1. Entrada no `logs/CHANGELOG.md` — ele é o dono da versão
2. Bump em `README.md`, `sistema/ESTADO-ATUAL.md` e `sistema/LEIA-ME.md`
3. Os quatro builds de `sistema/05-material/livro/build/`, **depois da última edição**:
   `build.py`, `build.py --duas`, `build_docx.py`, `build_txt.py`
4. Os 26 validadores de `sistema/03-mecanica/`
5. `manual/matematica/pac7.py` e `v7.py`
6. `conferir-voz.py --estrito`, de dentro de `sistema/05-material/livro/`
7. `conferir-repositorio.py`, da raiz

Se mexeu no manual do Fundamento: `node make.js` em `manual/gerador/`, copiar o `.docx` para
`manual/`, e exportar o `.pdf` com `soffice --headless --convert-to pdf`.

O `conferir-repositorio.py` vai acusar `7.1` e `7.3` antes do commit — são o recorte da
entrega, e o `./subir.sh` conserta sozinho. O que não pode sobrar é qualquer outro.

**São TRÊS comandos do meu lado, não dois** — o `finalizado/` é repositório separado sem
script próprio:

```bash
jjk
./subir.sh
cd finalizado && git add -A && git commit -m "recorte da vX.Y" && git push; cd ..
```

## Quatro coisas que vão te confundir se ninguém avisar

**O `conferir-voz --estrito` sai `1` de propósito.** São dois títulos de seção que eu
renomeei — *"Como uma aptidão funciona"* e *"Como funciona uma Bênção"* — e a regra "título
é pergunta" só libera *"Como ler …"*. **Não conserte sem me perguntar.**

⚠ **E é por isso que ele esconde erro novo:** o código de saída já é `1`, então quem confere
pelo código não vê. Um `ROTULO-LONGO` vivo desde a v0.203 só apareceu na v0.205, e o
`subir.sh` **não roda** o `conferir-voz`. Leia a saída, não o código.

**O mount às vezes perde um arquivo que ele mesmo acabou de gravar.** O conserto é escrever
com outro nome e `mv` por cima, e conferir que o `python3` lê de volta. Está no `README`, na
seção *"Commitar"*.

**Grep no projeto não é triagem.** Nome se confere com o `conferir-nomes.py`, que enxerga o
vocabulário do manual — o grep nos `.md` não enxerga.
