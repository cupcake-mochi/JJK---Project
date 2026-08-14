---
name: rpg-da-guilda
description: Procedimento de trabalho do repositório do RPG da Guilda (sistema de mesa de Jujutsu Kaisen) — ordem de leitura, validadores, triagem de nome, como escrever arquivo neste mount, arnês de perturbação e como fechar versão. Use em qualquer tarefa que mexa nesse repositório: escrever ou revisar peça de regra, mexer em número, criar validador, batizar coisa, ou retomar o trabalho em conversa nova.
---

# RPG da Guilda — procedimento do repositório

Sistema de RPG de mesa de Jujutsu Kaisen, para um server de guilda com vários mestres ativos e **personagem persistente entre mesas**. O filtro que decide quase tudo: *dois mestres que nunca conversaram chegam ao mesmo número?*

Esta skill guarda **procedimento**, nunca conteúdo. Números, lições e decisões moram nos arquivos do repositório e só lá — copiar qualquer um deles para cá cria a divergência que a lição nº 9 do projeto existe para evitar.

O repositório fica na pasta de trabalho do Mizuki (`Claude 2`), espelhando `https://github.com/cupcake-mochi/JJK---Project.git`.

---

## 1. Antes de qualquer coisa: ler, nesta ordem

1. `README.md` — em especial a seção **"Nove lições que custaram erro"**. Ela é a fonte única; não existe cópia dela em lugar nenhum, e ela cresce.
2. `sistema/ESTADO-ATUAL.md` — o ponto de retomada. **Leia inteiro**, incluindo a seção final *"Onde estamos, e o que falta"*. Ele é grande e o leitor pode truncar: se vier aviso de leitura parcial, continue a partir do offset em vez de responder pela primeira página.
3. `logs/CHANGELOG.md` — de cima para baixo. Ele carrega o **porquê** de cada decisão, que é a única parte do projeto que não dá para reconstruir lendo o resto.
4. A peça de `sistema/03-mecanica/` que for mexer.

**Não leia de `sistema/99-arquivo/` para escrever peça nova.** É material morto.

Se `02-esqueleto/arquitetura.md` contradisser uma peça de `03-mecanica/`, **a peça vence**.

## 2. Rodar os validadores antes de mexer em número

```bash
cd sistema/03-mecanica && for v in conferir-*.py; do python3 "$v"; done
cd ../..  && python3 conferir-repositorio.py
cd manual/matematica && for v in pac7.py v7.py; do python3 "$v"; done
```

**Os dois do `manual/matematica/` fazem parte da conta.** O `subir.sh` roda os três blocos; quem seguisse só os dois primeiros rodava menos validador do que o script que decide se o commit sobe.

**A armadilha que continua real: confira `PULADA=0`.** Sem `python-docx` instalado (`pip install python-docx --break-system-packages`) os três que leem o manual pulam em vez de falhar, e saem com código 0. **Um deles pula tudo:** o `conferir-manual` sai no `except ImportError` antes da primeira checagem.

*E quando for documentar quanto cada um pula, leia do código, não da saída.* A v0.38 contou pela saída, escreveu um número errado em quatro documentos, e a v0.40 achou. **Contar sintoma não é contar causa.** *O mesmo vale para descobrir quais são os três:* `grep docx` acha nove arquivos, e seis deles só têm a palavra em comentário.

**Rode de `sistema/03-mecanica/` mesmo assim**, porque é o que o `subir.sh` faz e o que o resto da documentação supõe. *Mas o motivo virou hábito na v0.38:* até a v0.37 a documentação dizia que rodar de outro lugar fazia validador pular checagem em silêncio — hoje todos resolvem o caminho por `__file__` e a saída de `/tmp` é idêntica.

Um verde que pulou checagem não prova nada. Conte as PULADAs, não confie no "OK". **E quando um aviso destes parar de reproduzir, conserte o aviso** — um que dá o motivo errado ensina a procurar o defeito no lugar em que ele não está mais.

## 3. Antes de batizar qualquer coisa, a triagem

```bash
cd sistema/03-mecanica
python3 conferir-nomes.py --candidatos Nome Outro Terceiro
```

Ela já matou mais de dez nomes que pareciam livres, e pega **substring** — um nome morre por estar dentro de um termo maior do manual.

**Ela não pega três coisas, e você tem que pegar:**

- **Colisão de sentido.** Um nome pode sair `LIVRE` e ainda colidir com o que o sistema já faz com aquela palavra.
- **Colisão com o hobby.** Termos como *move*, *vantagem*, *resistência*, *condição*, *crítico* carregam significado herdado de sistemas populares. O `01-pesquisa/` cita vários desses sistemas pelo nome — vale procurar o termo lá antes de adotá-lo.
- **Categoria.** Escrever `<substantivo> <adjetivo>` faz o validador ler o adjetivo como *nome* daquela categoria. Use a formulação que as peças já usam.

## 4. Escrever arquivo neste mount

O mount que expõe a pasta ao sandbox tem defeitos medidos e reproduzíveis:

- **Código novo se escreve pelo bash**, com `cat > arquivo <<'EOF'`. Arquivo que a ferramenta de escrita grava fica invisível para o `python3` com frequência.
- **Para `.md` a ferramenta de escrita serve.** Se um validador acusar arquivo sumido que você está vendo, qualquer escrita nova reconcilia o mount — e uma edição de uma linha basta. O conteúdo no disco nunca esteve em risco. *Sintoma:* `ls` e `stat` mostram tamanho e inode certos, e `open()` devolve ENOENT enquanto os vizinhos abrem.
- **Não rode git do sandbox** — nem `status`, nem `log`, nem `fsck`. Todos saem com `loose object is corrupt` e **o repositório está inteiro**; do lado do usuário funciona normalmente. Pior: `git status` cria um `.git/index.lock` que o sandbox não consegue apagar, e um lock preso trava o script de commit. *Para ver em que commit a pasta está sem rodar git, leia `.git/logs/HEAD` como arquivo* — é texto puro e não cria lock.
- **O commit é sempre do usuário.** Você lê, edita e valida; ele commita.

Depois de escrever, confira que o bash lê o arquivo de volta.

## 5. Arnês de perturbação — todo número novo ganha teste negativo

Perturbe o valor e prove que a checagem certa acende. Três regras, cada uma paga com uma versão perdida:

1. **Numa cópia isolada**, nunca nos arquivos reais.
2. **Confira que a base passa na cópia antes de perturbar.** Uma cópia mal montada faz *todas* as perturbações acenderem — vermelhos que parecem prova e não são.
3. **Confira que a perturbação mudou o arquivo** (`diff`) antes de ler o resultado. `sed` que não bate produz um "não acendeu" falso.

E, ao escrever a checagem: **separe a regra aplicada do limite de design.** Uma checagem que se mede contra a própria constante sai verde quando você perturba a constante. Esse erro apareceu três vezes em três versões.

Sempre que der, adicione um **contra-teste**: prove que a alternativa que você rejeitou produziria resultado diferente. Sem ele, uma checagem pode ser trivialmente verdadeira.

## 6. Onde a checagem mora

**Cada peça tem um validador dono.** Checagem nova vai no validador da peça que ela confere — não num arquivo novo.

Isso não é só arrumação: `conferir-repositorio.py` conta peças (`NN-nome.md`) e validadores (`conferir-*.py`) na pasta e compara com o número escrito no `README`, no `ESTADO-ATUAL` e no `LEIA-ME`. **Arquivo novo com dois dígitos na frente, ou `conferir-*.py` novo, quebra a contagem** até os três documentos e a entrada do CHANGELOG subirem juntos.

**Meia peça não é peça.** Trabalho em andamento vive como `RASCUNHO-*.md`, sem número na frente. Ele vira peça numerada quando fecha.

E **nada de valor fica escrito dentro do validador**: leia o número do documento dono.

## 7. Fechar versão

```bash
./subir.sh "o que mudou"       # roda todos os validadores e se recusa a commitar se algum falhar
```

- **A entrada do topo do `CHANGELOG` é a dona da versão do projeto.** Subir a versão no `README`, no `ESTADO-ATUAL` ou no `LEIA-ME` sem escrever a entrada **falha** o `conferir-repositorio.py`.
- **Antes de fechar, revisão cética — inclusive contra o que você mesmo acabou de escrever.** Metade dos achados grandes do CHANGELOG saiu daí. Procure ativamente o erro na sua própria proposta antes de entregá-la.
- **Peça substituída vai para `99-arquivo/`** com cabeçalho dizendo de onde saiu, o que a substituiu, em que versão, **por que morreu** e o que dela sobreviveu.
- Se o repositório é lido por um Project, **sincronizar depois do push**.

## 8. Como o Mizuki trabalha

- **Escolha de sabor é dele** — quantos itens numa lista, quais são, como se chamam, em que ordem aparecem. Traga as opções **com o número e o trade-off de cada uma já calculados**, e pergunte. Várias rodadas curtas, nunca uma proposta grande pronta.
- **Não pergunte o que a conta responde.** Se dominância, deriva ou o filtro multi-mestre já decidem, rode a conta e apresente o resultado.
- **Mostre o resultado no chat**, não só no arquivo. Ele quer ler o que foi escrito sem abrir o documento.
- **Antes de entrar numa peça ou numa Origem, mostre o que ela tem hoje** — ele quer discutir a partir do estado atual.
- **Número vem de conta rodada, nunca de intuição.** Escreva o script, rode, mostre a tabela.
- **Não escreva resumo em prosa por cima de tabela que o script já imprimiu.** Leia o número do script.
- **Pesquise antes de inventar.** Isso virou skill própria na v0.38 — a `pesquisa-antes-de-propor` —, justamente porque enterrado aqui neste bullet ele não disparava.
- **Documento não pode ter cara de saída de IA.** Seções de tamanhos diferentes, sem simetria forçada, sem "além disso" e "em suma". Português informal, e nunca português de Portugal.

## 9. Skills de apoio, todas no repositório

`pesquisa-antes-de-propor` · `design-mecanicas-rpg` · `balanceamento-simulacao` · `playtesting-rpg` · `redacao-acessivel-rpg` · `gasto-de-modelo`

Elas moram em `sistema/skills/`, com `SKILL.md` e pastas de apoio. A de design tem testes — dominância, bônus automático, filtro multi-mestre, colisão de nome — que **pegam coisa que nenhum validador do repositório pega**; vale rodar contra a própria proposta antes de entregar.

*O `sistema/LEIA-ME.md` também lista as sete*, separadas em duas de procedimento, quatro de assunto e uma sobre a conversa. **Nenhuma das duas listas é conferida por validador nenhum** — o `conferir-repositorio.py` só checa que a pasta `sistema/skills` existe e depois pula ela na varredura. Então, quando as duas discordarem, não escolha entre elas: **conte a pasta** (`ls sistema/skills/`) e conserte a que estiver atrás. Esta aqui já foi a que estava.

**Existe eval, e ele cobre quatro das sete.** `sistema/skills/evals/evals.json` traz quatro casos — um por skill de assunto, com `prompt` e `expected_output`. As três de fora são justamente as que não têm resposta certa isolada: as duas de procedimento e a da conversa.

**A `pesquisa-antes-de-propor` vem antes das outras quatro**, e ela nasceu porque a linha *"pesquise antes de inventar"* estava no item 8 desta skill e não disparava. Lembrete enterrado numa lista não é procedimento. Se a sua proposta vai afirmar o que outro sistema faz, qual o modo de falha documentado de alguma coisa, o que o material original estabelece ou como uma ferramenta se comporta — **procure antes de escrever, não depois.**

**A pasta `sistema/skills/` é cópia de trabalho: editar lá não altera a skill instalada.** As duas divergem sozinhas, e nenhum validador alcança essa camada. Ao mudar uma skill, mude nos dois lados.

## 10. Armadilhas recorrentes deste projeto

Antes de fechar qualquer coisa, passe por estas — cada uma já mordeu mais de uma vez:

- **"Esse número já inclui o que eu estou somando nele?"** É o erro mais teimoso do projeto.
- **Antes de aceitar um preço, veja se o termo que ele usa existe** — e se existe, vá ler a regra pendurada nele. Vale nas duas direções.
- **Confira o ponteiro de seção antes de citar.** A checagem 5 do `conferir-repositorio.py` pega isso hoje, e ela nasceu porque três documentos apontavam para uma seção que não existe.
- **Tensão de preço às vezes é lacuna de texto disfarçada.**
- **Decisão registrada não é decisão aplicada.** Decisão que termina em "corrigir em três lugares" precisa de alguém conferindo os três.
- **Contagem não é valor.** Meça peso de mesa, não quantidade.
- **Um preço se mede somado, nunca sozinho.**
- **Aviso que parou de reproduzir é dívida.** Um procedimento com motivo errado envelhece pior que um sem motivo nenhum.

A lista completa e atualizada é a seção *"Nove lições que custaram erro"* do `README.md`. Leia de lá; não confie nesta amostra.
