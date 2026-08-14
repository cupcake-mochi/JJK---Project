# Prompt para o chat de Trilhas

*Escrito na v0.59, para o chat da peça 17 começar quente. Copiar o bloco abaixo inteiro.*

---

Este é o RPG da Guilda — sistema de mesa de Jujutsu Kaisen. Pasta Claude 2, no HD externo. Confira antes de escrever: `head -6 README.md` tem que dizer **v0.59** (ou maior), com **dezesseis peças e dezesseis validadores**, e `grep -c "Nove lições" README.md` tem que achar a seção. Se aparecer "Seis lições que custaram erro" ou "Versão v0.27", é o clone velho em JJK---Project dentro da home — pare e me avise, não tente consertar nada de lá.

Leia nesta ordem: `README.md` (as "Nove lições"), `sistema/ESTADO-ATUAL.md` INTEIRO (ele trunca — continue do offset; a tabela "Onde cada coisa está" ganhou validador na v0.59 e está completa), `logs/CHANGELOG.md` do topo até a **v0.50** (é onde a fila foi reordenada), e `sistema/03-mecanica/RASCUNHO-trilhas.md` inteiro, que é onde está a peça que vamos fechar. Leia também a **peça 6** (`06-caminhos-e-trilhas.md`), que é a dona dos Caminhos e é quem tem as três perguntas abertas que Trilhas herda.

Rode os 19 validadores: os dezesseis de `sistema/03-mecanica/` (conferir-atributos, conferir-acao, conferir-pericias, conferir-descanso, conferir-nomes, conferir-manual, conferir-aptidoes, conferir-expansao, conferir-orcamento, conferir-xp, conferir-equipamento, conferir-criacao, conferir-ficha, conferir-legados, conferir-invocacoes, conferir-ferramenta), o `conferir-repositorio.py` da raiz, e `pac7.py` + `v7.py` de `manual/matematica/`. Na v0.59 estava **19 de 19, zero PULADAS**. Se der PULADA é python-docx faltando (`pip install python-docx --break-system-packages`) — sem ele, conferir-nomes, conferir-manual e conferir-pericias pulam checagem em silêncio e saem verdes.

Não rode git. Não é só o commit que falha (o mount rejeita o chmod que o git faz ao finalizar objeto) — leitura também: status, log e fsck saem com "loose object is corrupt", e o repositório está inteiro, é o mount. Não rode git gc nem fsck --full. `git status` cria um lock que trava o subir.sh. Para saber em que commit a pasta está sem rodar git, leia `.git/logs/HEAD` como arquivo — é texto puro e não cria lock. Commit é sempre meu: deixe a mensagem pronta em `mensagem-de-commit.txt` e me avise — eu rodo `./subir.sh`, que confere os 19 validadores, commita e sobe sozinho, e não commita nada se algum falhar.

Código novo se escreve pelo bash com heredoc (`cat > arquivo <<'EOF'`), nunca pela ferramenta de escrita. Pra `.md` a ferramenta serve; se o mount comer um arquivo recém-escrito, uma segunda escrita reconcilia. E `rm` sai com "Operation not permitted" — peça a permissão de exclusão em vez de desistir.

**A TAREFA: a peça de Trilhas, que vira a peça 17.** É a maior coisa que falta escrever, **toca 100% das fichas**, e é a única da fila em que errar o formato antes de começar custa a peça inteira.

**O que já está decidido e não se rediscute:**

- **Q1, fechada na v0.55:** Caminhos não se misturam — **não existe multiclasse**. Uma Trilha por ficha. Isso matou as 105 combinações que eram o maior risco de matriz.
- **Q4, fechada na v0.55:** **as subtrilhas existem e cruzam Trilhas do mesmo Caminho** — o Bastião pega uma de `Muro` e uma de `Punho`, nunca uma do Guia.
- **As quinze já têm nome:** Bastião `Muro`·`Punho`·`Brasa` / Vanguarda `Estocada`·`Batedor`·`Executor` / Guia `Elo`·`Sutura`·`Perímetro` / Emanador `Torrente`·`Repertório`·`Arremate` / Evocador `Servo`·`Matilha`·`Coro`.
- **Três das quinze já são construíveis** porque a peça 15 fechou a máquina delas: `Servo` dá um corpo forte, `Matilha` dá os cinco, `Coro` dá a exceção de economia de ação — e **o que a Trilha concede não sai do orçamento da ficha**.

**A Q3 é a régua, e ela vem ANTES do catálogo.** É a única recomendação de método que o rascunho faz, e ela não é de sabor: a peça 13 fechou 81 entradas em **uma** versão porque a régua veio antes; a peça 14 gastou **seis** porque não veio. Não comece a escrever entrada nenhuma antes da régua fechar.

**O risco real é escala, e ele tem número:** quinze Trilhas × quantas entregas dá **30 a 120 entradas**. A Q2 (quantas entregas por Trilha, e em que níveis) é sua, e o rascunho já traz a recomendação de método com a conta: comece por **4** — níveis 2, 10, 18 e 26 —, que é a densidade do D&D 2024 ajustada para 29 níveis, cai em nível de marco e dá 60 entradas.

**O buraco onde a Trilha cabe está medido: catorze dos vinte e nove níveis não entregam nada hoje, e são todos os ímpares.** Os feitiços conhecidos (`2 + nível ÷ 2`) cobrem todo nível par, e maestria e marcos caem em cima de níveis que já tinham feitiço.

O **§5 do rascunho** lista o que o validador precisa ter — a matriz de dominância rodando por Caminho **e** entre Caminhos, o orçamento de cada Trilha contra os `6%` a `9%` da Rotina lidos da peça 14 §4, nenhuma entrega com dado de dano nem que cresça com refino, o teto de uma Rotina somada para `Servo`/`Matilha`/`Coro`/`Torrente` conferido pela economia de ação, a tabela de progressão consolidada, a triagem de todo nome novo, e a cota de ataque extra da peça 6 §3.1. **Não invente checagem: implemente aquelas.**

**Quando ela existir, quatro coisas sobem juntas ou o `conferir-repositorio.py` quebra a contagem:** o rascunho vira `17-trilhas.md` (e o rascunho é apagado, como a v0.58 e a v0.59 fizeram), o validador entra, o número de peças e validadores muda no README, no ESTADO-ATUAL e no LEIA-ME — **e o mapa "Onde cada coisa está" do ESTADO-ATUAL também, que ganhou a checagem 6 na v0.59 e falha se a peça ou o validador novo não aparecerem nele** — e entra a entrada nova no CHANGELOG.

**O arnês é obrigatório:** cópia isolada, base conferida verde ANTES de perturbar, `diff` provando que o sed bateu, e contra-teste mostrando que uma perturbação acende uma checagem só. *E copie o `.gitignore` junto se for perturbar o `conferir-repositorio.py` — sem ele a base sai vermelha e todo vermelho vira falso.*

**Nada de valor fica escrito dentro do validador** — leia o número do documento dono.

**Cinco armadilhas que já custaram correção:**

1. Número que descreve uma lista que mora em OUTRO documento envelhece a cada edição daquele documento. **Conte a lista, não guarde o total.**
2. Quando duas checagens leem o mesmo dono ou a mesma amarra, **declare o par explicitamente** em vez de fingir que são independentes.
3. **Confira ponteiro de seção antes de citar** — e cuidado com peça que tem `## 6.` e `## 6.5.`: "próxima seção" e "próximo número de seção" não são a mesma coisa.
4. **Uma peça que documenta o próprio validador contém o texto que o validador procura para reprovar.** Varra só as seções de regra, nunca a seção que descreve as checagens.
5. **Lista "o que falta" que ninguém revisita vence sozinha.** Antes de escrever qualquer uma, confira item por item se já não foi feito.

Escolha de sabor é minha, traga opções com número e trade-off já calculados e pergunte — mas não me pergunte o que a conta responde. Número vem de conta rodada. Pesquise antes de inventar, e cite texto de regra em vez de lembrar dele. Me mostre no chat o que você escreveu. Português informal, documento não pode ter cara de saída de IA.

Link: https://github.com/cupcake-mochi/JJK---Project.git
