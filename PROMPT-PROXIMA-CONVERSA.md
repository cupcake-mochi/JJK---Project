# Continuar o Projeto - M — varrer a fila, e resolver o que ela esconde

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` na raiz e me avisa.

## Confirme a pasta antes de qualquer coisa

```bash
cd "/media/mizuki/HD Externo II/Claude/Claude 2" && grep -c "^## Nove lições" README.md
```

Tem que dar `1`. Se der `0`, é a pasta errada — **pare.** Existe um clone velho na v0.27
dentro da home que tem a cara deste projeto.

## Leia nesta ordem

1. `README.md`, a seção **"Nove lições que custaram erro"**
2. `logs/CHANGELOG.md`, as entradas **[0.187] até [0.182]** — são seis versões de uma
   conversa só, e elas explicam o padrão que a próxima precisa atacar
3. `sistema/ESTADO-ATUAL.md` **inteiro**, incluindo a seção final *"Onde estamos, e o que
   falta"*

## Onde o trabalho está

Estado limpo na **v0.187**, commitada. **26 validadores e 286 checagens** passando, PULADA
zero; o `conferir-repositorio.py` sai com zero problemas fora os dois do `finalizado/`,
que o passo 0 do `subir.sh` resolve.

As seis últimas versões saíram todas de uma conversa, e todas na mesma família de defeito:

- **v0.182** — a passada de texto da peça 15, pelo `METODO-passada-de-texto.md`. Doze
  lugares afirmando em tempo presente um mecanismo que morreu na v0.180
- **v0.183** — o corpo forte da invocação tinha **três** multiplicadores escritos na mesma
  peça, e a tabela de durabilidade misturava dois modelos entre as linhas
- **v0.184** — o `Casco` batizado duas vezes; a rota da `Sintonia` virou `Parrudo`
- **v0.185** — dois números sem checagem ganharam dono, e o do `Parrudo` não tinha dono
  nenhum: existia só no capítulo 35 do livro
- **v0.186** — as três montagens por Trilha, prometidas desde a v0.53
- **v0.187** — a vaga de `Desliga` do Corpo Amaldiçoado não esperava escrita, esperava
  **alvo**, e a peça 13 dizia as duas coisas na mesma seção

## O que eu quero nesta conversa

**Varrer a fila contra o estado real, e só depois escolher o que fazer.**

O motivo é medido: nesta leva, **três itens que a fila dava como abertos já estavam
fechados** — o aviso das montagens por Trilha, o `Casco`, e o custo de sacar arma, que a
peça 3 escreveu e a peça 20 continua listando como buraco em dois lugares.

O padrão é sempre o mesmo: **fechado numa peça e ainda aberto na peça vizinha.** Nenhum
validador alcança isso, porque a pendência mora em prosa de "Em aberto" e não em tabela.

Então:

1. **Confira item por item da fila abaixo contra o que as peças dizem hoje.** Não confie na
   lista; ela é justamente o que está sob suspeita.
2. **Conserte a contabilidade do que já fechou.**
3. **Traga o que sobrou, com o tamanho de cada um**, e eu escolho o que atacar.

E se der para escrever **uma checagem que impeça um item fechado de continuar aberto noutro
documento**, ela vale mais que qualquer item da lista. A v0.187 fez isso para um caso só.

## A fila, como ela está escrita hoje — e ela não é confiável

**Decisão tomada e não escrita**
- O **`Não Sou Gente`** virar Passiva paga com espaço de feitiço. Decisão da v0.39.

**Bloqueado, e dizendo por quê desde a v0.187**
- A vaga de `Desliga` do Corpo Amaldiçoado. Espera peça nova nomear coisa.

**Medida por rodar**
- A **reação de RD do Bastião encosta em cobrir-se de energia**. *"Ou uma delas domina a
  outra, ou são a mesma peça com dois nomes — medir as duas juntas."*
- Os **pontos de feitiço do Emanador** são moeda nova ao lado do PE.
- A **penalidade por empunhar sem treino ou sem requisito**, aberta dentro da peça 19.

**Sabor, esperando eu decidir**
- A **`Pétala`** como quarta porta.
- **`Energia Reversa` contra maldição** — na obra ela fere, aqui só cura.
- Catálogo de **Kata** e de **`Manejo`** — as duas peças entregam a máquina de propósito.

**Registrado e adiado por decisão minha**
- O **teto de quantas invocações cabem no campo** (peça 15, v0.178). Hoje a Trilha é a
  única porta que entrega corpo, e nenhuma entrega a segunda. *No dia em que outra coisa
  conceder uma invocação, o teto vira necessário — e aí ele é preço, não texto.*

**Já resolvido, e a fila não sabe**
- **Sacar arma.** A peça 3 tem a regra escrita; a peça 20 lista como aberto no §7 e no §11.

**O maior, que não está em lista nenhuma**
- `04-playtest/` continua vazia. **Zero sessões desde a v0.1.**

## Como eu quero que você trabalhe

- **Número vem de conta rodada, nunca de intuição.** Se eu disser que algo está
  desbalanceado, meça antes de concordar. E me diga quando a conta me desmentir.
- **Antes de propor mecânica nova, pesquise** como outro sistema resolve o mesmo problema,
  e procure o modo de falha documentado dele. Os PDFs estão em
  `PDFs - Sistemas Extras/PDF_Sistemas/`.
- **Traga as opções com o número e o trade-off já calculados, e pergunte.** Escolha de
  sabor é minha.
- **Todo número novo ganha validador com teste negativo:** perturbe o valor e prove que a
  checagem certa acende, restaure e confira. **E confira que a perturbação bateu** — nesta
  leva uma passou verde porque o `sed` não pegou todas as formas da frase, e a checagem
  estava certa.
- **Checagem não pode passar por ausência.** Se apagar a frase faz a checagem calar, o
  conserto barato para uma divergência vira sumir com a cópia.
- **Âncora de regra não mora em prosa.** Recorte de tabela termina onde a tabela termina.
  Uma checagem ancorada numa frase cai quando alguém reescreve a frase.
- **Aplicar a edição é a parte curta.** A longa é a cascata — peça → livro → validador.
  Pare no primeiro passo que virar design e pergunte.
- **Escreva no meu registro:** negrito abrindo com a regra e a razão logo depois, "você"
  falando com o leitor, frase encadeada por vírgula em vez de aforismo, parêntese para a
  exceção curta.
- **Fale comigo diferente de como escreve o documento.** Uma ideia por parágrafo, frase
  curta, sem `§3.4` no meio da frase. Se eu disser que não entendi, a resposta certa é
  MENOS detalhe, recomeçando de mais atrás.

## Fechar versão, quando a leva acabar

Entrada nova no topo do `logs/CHANGELOG.md`, que é o dono da versão, e subir o número no
`README.md`, no `sistema/ESTADO-ATUAL.md` e no `sistema/LEIA-ME.md`. Os quatro dizem
**v0.187** hoje.

Depois, nesta ordem:
- os quatro builds em `sistema/05-material/livro/build/` — `build.py`, `build.py --duas`,
  `build_docx.py`, `build_txt.py` — rodados **DEPOIS** da última edição
- os **25** validadores de `sistema/03-mecanica/`
- os dois de `manual/matematica/` (`pac7.py` e `v7.py`)
- `conferir-voz.py --estrito`, de dentro de `sistema/05-material/livro/`
- `conferir-repositorio.py`, da raiz

E deixe a `mensagem-de-commit.txt` pronta. **São TRÊS comandos do meu lado, não dois** — o
`finalizado/` é repositório separado sem script próprio:

```bash
jjk
./subir.sh
cd finalizado && git add -A && git commit -m "recorte da vX.Y" && git push; cd ..
```

**E se você mexer no livro, me manda o PDF de duas colunas antes de eu commitar.**

## Três coisas que vão te confundir se ninguém avisar

**O `conferir-voz --estrito` fica em 2 achados de propósito.** São dois títulos de seção
que eu renomeei — *"Como uma aptidão funciona"* e *"Como funciona uma Bênção"* — e a regra
"título é pergunta" só libera *"Como ler …"*. **Não conserte sem me perguntar.**

**O mount às vezes perde um arquivo que ele mesmo acabou de gravar.** O conserto é escrever
com outro nome e `mv` por cima, e conferir que o `python3` lê de volta. Está no README, na
seção *"Commitar"*. **E não rode git do sandbox.**

**Grep no projeto não é triagem.** Nesta leva eu afirmei que dois nomes estavam livres
depois de conferir por `grep` nos `.md` — e os dois colidiam com termo do manual, que só o
`conferir-nomes.py` enxerga. **Nome se confere com a triagem, sempre.**
