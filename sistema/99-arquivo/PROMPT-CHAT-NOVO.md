> **MATERIAL MORTO — arquivado na v0.45.**
>
> **De onde saiu:** a raiz do repositório, onde ele viveu da v0.15 à v0.44.
> **O que o substituiu:** nada, e é esse o ponto. O `README.md` ganhou a seção *"Retomar em conversa nova"* com a única coisa que era só dele — o teste da pasta certa, contra o clone parado na v0.27. O resto já morava em outro lugar.
> **Em que versão:** v0.45.
>
> **Por que morreu.** Medido bloco a bloco: **15 dos 16 blocos eram cópia**, e juntos criavam **32 cópias** de coisas que já tinham dono — a ordem de leitura (3 lugares), quanto cada validador pula (3), o *"não rode git"* (2), o *"como eu gosto de trabalhar"* (3), o estado do trabalho (2 a 3). **Um único bloco era dele.**
>
> E ele já tinha cobrado o preço disso duas vezes: a **v0.40** registra que ele repetiu o *"4, 2 e 1"* errado junto com os outros três documentos, e na **v0.45** ele descrevia a v0.44 — mandando ler uma tabela do §5.0.1 que tinha mudado e citando treze efeitos de crítico que já estavam mortos. **Nenhum validador o alcançava:** ele não aparece uma vez sequer no `conferir-repositorio.py`, e nenhum arquivo do repositório apontava para ele. Folha solta, sem dono e sem trava.
>
> **E o padrão já tinha acontecido.** O `PROMPT-DE-CONTINUIDADE.md`, nesta mesma pasta, é a primeira encarnação da mesma ideia — morto na v0.14 com a nota *"o `ESTADO-ATUAL.md` faz esse trabalho melhor hoje"*. **Este é o segundo, morrendo pelo mesmo motivo, trinta versões depois.** Se um terceiro aparecer, leia estas duas linhas antes de escrevê-lo.
>
> **O que dele sobreviveu:** o teste da pasta certa, hoje no `README.md`. E o hábito que o tornou desnecessário — **pedir um prompt de continuidade no fim de cada conversa**, escrito na hora contra o estado real, que é o único formato que não tem como envelhecer.

---

# Prompt para retomar o RPG da Guilda em conversa nova

*Atualizado ao fim da v0.44 — commitada e no GitHub. Copie daqui para baixo.*

---

Este é o **RPG da Guilda** — um sistema de RPG de mesa de Jujutsu Kaisen para um server de guilda com 5 a 7 mestres ativos e personagem persistente entre mesas. Você está pegando o projeto no meio de uma peça.

**Antes de escrever qualquer coisa, faça esta sequência inteira e me relate cada passo.**

## 0. CONFIRA QUE VOCÊ ABRIU A PASTA CERTA

A pasta de trabalho é a **Claude 2**, no HD externo. Existe **outro clone desta mesma coisa parado na v0.27** numa pasta JJK---Project dentro da minha home, e ele tem a cara do projeto inteiro — validadores, peças, changelog. Uma conversa já se perdeu meia hora lendo o clone velho e rodando sete validadores que passaram sem provar nada.

**O teste é uma linha, e leva dez segundos:**

```
head -6 README.md          # tem que dizer  Versão v0.44  (ou maior)
grep -c "Nove lições" README.md
```

Se o `README.md` disser *"Seis lições que custaram erro"* ou *"Versão v0.27"*, **você está na pasta errada. Pare e me avise** — não tente consertar nada de lá.

> **E se você tiver um Project do Claude com este repositório sincronizado, ele pode estar atrasado.** A sincronização é manual e eu esqueço dela. **Quando a busca do Project e os arquivos da pasta discordarem, a pasta vence** — ela é a fonte da verdade, e o Project é uma cópia com data. Se acontecer, me avise que eu clico em "Sync now": trabalhar com as duas ao mesmo tempo é a lição nº 9 acontecendo em cima do projeto inteiro.

## 1. LEIA, NESTA ORDEM

- `README.md`, em especial **"Nove lições que custaram erro"**. Elas são a fonte única e não têm cópia em lugar nenhum.
- `sistema/ESTADO-ATUAL.md` **INTEIRO**. Ele é grande e a leitura pode truncar — se vier aviso de leitura parcial, continue do offset em vez de responder pela primeira página.
- `logs/CHANGELOG.md` de cima até a **v0.33**. A entrada do topo é a mais recente, e ele carrega o **porquê** de cada decisão — é a única parte do projeto que não dá para reconstruir lendo o resto.

## 2. RODE OS VALIDADORES

De dentro de `sistema/03-mecanica/`, que é o que o `subir.sh` faz. Depois o `conferir-repositorio.py` da raiz, e os dois de `manual/matematica/` (`pac7.py` e `v7.py`). **Dezesseis no total.**

Me diga quantos passaram **e se algum imprimiu PULADA** — verde que pulou checagem não prova nada. Sem `python-docx`, três deles pulam e saem com código 0: `conferir-nomes` pula **3 de 5**, `conferir-manual` pula **4 de 4** (todas, ele sai no `except ImportError`) e `conferir-pericias` pula **1 de 8**. No fim da v0.44 o estado era **16 de 16, zero PULADAS**.

## 3. NÃO RODE GIT

Deste sandbox o git sai com *"loose object is corrupt"* e **o repositório está inteiro** — é o mount. Pior: `git status` cria um `.git/index.lock` que você não consegue apagar, e lock preso trava o `./subir.sh`. **Commit é sempre meu.**

Se precisar saber em que commit o repositório está, **leia os arquivos** — `.git/HEAD`, `.git/refs/heads/main`, `.git/refs/remotes/origin/main` e `.git/logs/HEAD` são texto puro, e ler não cria lock nenhum. `origin/main` diferente do `HEAD` quer dizer commit sem push.

Quando fechar alguma coisa, deixe a mensagem pronta em `mensagem-de-commit.txt` e me avise: eu rodo `./subir.sh` sem argumento. **E me lembre de clicar "Sync now" na fonte do GitHub do Project depois do push** — a sincronização é manual, e pular esse passo é o jeito mais fácil de o Project ficar discutindo regra que já mudou.

E o mount **às vezes some com um arquivo que ele mesmo acabou de gravar**. Sintoma: `ls` e `stat` mostram tamanho e inode certos, `open()` devolve ENOENT, os vizinhos abrem normalmente. Aconteceu duas vezes na v0.42 e duas na v0.44 — nesta última o `README.md` e o `ESTADO-ATUAL.md` caíram juntos, que é o par de sempre. O conteúdo nunca está em risco: **qualquer escrita nova reconcilia, e uma edição de uma linha basta.** Depois de escrever, confira que o bash lê o arquivo de volta.

---

# ONDE O TRABALHO PAROU

Duas frentes abertas, e elas são independentes.

## A. EQUIPAMENTO — a peça em andamento

O estado mora em `sistema/03-mecanica/RASCUNHO-equipamento.md`. **LEIA ESSE ARQUIVO INTEIRO** antes de propor qualquer coisa — ele tem as decisões já tomadas com o número de cada uma, o que foi rejeitado e por quê, e a lista do que falta. Não refaça nada que está lá; a conta já rodou.

### A régua de preço mudou na v0.44, e é o que você mais precisa saber

**O preço mora na ARMA, não na classe.** A classe sumiu como preço; o que sobrou dela é a **categoria**, que é o gancho da Vanguarda.

```
1 ponto = 0,33 por rodada = um passo de dado = uma propriedade
orçamento: 2 numa mão · 4 em duas mãos
```

E a régua inteira cabe numa tabela (§5.0.1), no molde do PF2e — só que aqui o teto de dado **é** o orçamento, então combinação abusiva fica ilegal por construção:

| propriedades | uma mão | duas mãos |
|---|---|---|
| 0 | d8 | d12 |
| 1 | d6 | d10 |
| 2 | d4 | d8 |
| 3 | — | d6 |

Ela saiu **por regressão contra as seis classes publicadas**, e cinco fecham exatas. **Não invente número novo para ela** — leia o §5.0 e o §5.0.1.

### E o dado NÃO é um eixo livre — é a correção que fechou a v0.44

Aquela tabela é uma **função**: escolhidas as mãos e o número de propriedades, sobra **um** dado legal, porque gastar menos que o orçamento é dominância estrita. **O dado é saída da conta, não entrada.** Ele não pode variar arma por arma.

Quem carrega a variação é a propriedade — e propriedade não é escolha, é o que a arma é. Uma naginata tem `Alcance` e ocupa as duas mãos, o que já a manda para o d10; a Yari e a Lança caem no mesmo lugar pelo mesmo motivo, sem ninguém ter decidido nada.

Rodado sobre as 41 armas de corpo a corpo:

| eixo | assinaturas | armas com gêmea |
|---|---|---|
| só o preço | **14** | 35 de 41 — **85%** |
| preço × categoria | **25** | 25 de 41 — **61%** |

> **Consequência de projeto:** a unicidade mora no **efeito de crítico da categoria**, não no dado. Sem ele, 85% do catálogo é gêmeo mecânico. Ele deixou de ser o eixo secundário de identidade e virou o principal.

*A v0.44 tinha escrito o contrário — "45 assinaturas legais para 52 armas, nenhuma arma é obrigada a ter gêmea". O número era `5 dados × 9 opções de propriedade`, e a régua não deixa o dado ser fator independente. O achado está registrado na subseção `Corrigido` daquela entrada.*

### Fechado

O teto de Defesa (derivado de peça 1 §5 + peça 2 §3 + peça 11 §5 — **ninguém escreve o número**; Equipamento é dona do invariante, e equipamento topa em **19**); duas classes de uniforme com escadas de Força separadas (`Traje` `— / — / 3`, `Revestimento` `3 / 4 / 6`); o Traje sob medida com vantagem situacional e vaga aberta; a escada de escudos; **treze categorias e 52 armas**; as oito propriedades; o ofício `Alfaiate`.

**E a v0.44 fechou:** a régua de preço acima · a escada do tiro (**`2d10`** no topo, dois dados: `2d10 · 2d8 · 2d6 · 1d10`) · o X da `Munição` (**`2 · 3 · 4`**, com a Metralhadora Pesada sozinha no 4) · a **`Versátil` a custo zero**, que fecha a dominância aberta desde a v0.41 · o **teto da `Fineza`** (d6 numa mão) · e o **§5.1 reaberto**, dando à categoria um **efeito de crítico**.

A dívida da peça 11 e da peça 8 foi **APLICADA** — o escudo soma com cobrir-se em vez de desligar, e o preço da Reação virou agnóstico de fonte. Três checagens no `conferir-criacao.py` guardam as duas.

### Em aberto, e é por aí que se retoma

1. **O dado e as propriedades de cada uma das 52 armas.** A régua existe; a atribuição não. **E ela é uma decisão sobre propriedades, não sobre dados** — o dado cai sozinho depois. A pergunta de cada arma é *o que essa coisa é*, e o que a ficção não forçar é escolha minha.
2. **Os treze efeitos de crítico**, um por categoria — e agora eles são o eixo principal de identidade, não o secundário. Cabe até **11,0 de valor no disparo** por menos de um passo de dado, porque o 20 natural dispara em 3% das rodadas. **A armadilha documentada do PF2e:** efeito que morre contra alvo comum — sangrar morto-vivo, derrubar quem já está no chão.
3. **O validador da peça**, que precisa rodar dominância por valor total e **uma vez por rota de proteção — e são TRÊS**: cobrir-se, uniforme, e sem energia nenhuma (Restrição Celestial pelo ramo da Maki).
4. **As quatro vagas de Desliga da peça 13**, que esperam esta peça desde a v0.39.

## B. BLOQUEAR — regra opcional, fechada em rascunho

`sistema/03-mecanica/RASCUNHO-bloqueio.md`, e agora com seção própria no `ESTADO-ATUAL`. Ela não entra em balanceamento até o tópico de regras opcionais existir, e não mudou número de peça nenhuma.

Sua Defesa é `10 + Destreza + proteção`, e ela é o padrão. Ao ser atacado, você pode **Bloquear**: role `2d10 + (sua Defesa − 11)`. **Duplo 10 — Aparar:** não acerta, e você pode gastar a Reação para contra-atacar, com **+3 de dano**. **Duplo 1 — Brecha:** acerta, e o agressor pode gastar a Reação dele para atacar de novo, sem bônus. O Aparar **não anula um 20 natural**. **Não vale em Teste de Resistência.**

**O achado que sustenta tudo:** a house rule do hobby (*"role d20 no lugar dos 10"*) dá **+2,5pp de graça** porque `E[d20] = 10,5`. Qualquer dado de média 10 é neutro por construção, e o d20 não tem conserto — a média de um dado único sempre termina em `,5`.

**E o invariante que a segura:** Bloquear usa **exatamente o mesmo modificador** da Defesa passiva, e nada pode aumentar um sem aumentar o outro. `+1` de diferença vale 2,5pp, que é o tamanho do viés que a regra saiu para consertar. **Isso vale para Equipamento**, que é a peça que mais mexe em Defesa.

**Em aberto:** as condições que impedem Bloquear (ficam para a peça de dano e condições), a linha na ficha (`Defesa 17 · Bloquear 2d10+6`), e a Reação na ficha de inimigo. **O validador dele NÃO pode ser arquivo novo** — as três checagens do §7 são sobre a fórmula da Defesa, que é da peça 1, então vão para o `conferir-atributos.py`. Validador novo quebraria a contagem de treze por treze.

---

# COMO EU GOSTO DE TRABALHAR

- **Escolha de sabor é minha:** quantos itens numa lista, quais são, como se chamam. Traga as opções **com número e trade-off já calculados**, e pergunte. Rodadas curtas, nunca uma proposta grande pronta.
- **Mas não me pergunte o que a conta responde.** Se dominância, deriva ou o filtro multi-mestre já decidem, rode a conta e me mostre o resultado.
- **Me mostre no chat o que você escreveu**, não só no arquivo.
- **Antes de entrar numa peça ou numa Origem, me mostre o que ela já tem.**
- **Número vem de conta rodada, nunca de intuição.** Escreva o script, rode, mostre a tabela.
- **Pesquise antes de inventar:** como outros sistemas resolvem o mesmo problema, e qual o modo de falha documentado de cada um.
- **Revisão cética antes de fechar**, inclusive contra o que você mesmo escreveu.
- **Português informal, nunca de Portugal.** Documento não pode ter cara de saída de IA: seções de tamanhos diferentes, sem simetria forçada.

## Três regras de método que custaram versão

**Não escreva conclusão dentro do script antes de ler a saída dele.** *A v0.43 pagou por isso:* três vezes a prosa de um script contradisse a tabela do próprio script, e uma vez foi aritmética pura (`36` no lugar de `72`), que inverteu o sinal. As quatro foram pegas por conta rodada, e **nenhuma por releitura**.

**E o mesmo defeito mora nos documentos, não só nos scripts.** *A v0.44 achou o quarto exemplar:* o §5 do rascunho de Equipamento dizia *"1,32 por rodada"* enquanto as duas colunas da tabela logo acima davam `4,12 − 3,47 = 0,65`. **Quando um documento traz uma tabela e uma conclusão, refaça a divisão.**

**Contar o espaço não é contar o uso.** *A v0.44 pagou esta no fim, contra o que ela mesma tinha acabado de escrever:* o *"45 assinaturas legais"* media quantas combinações a régua permite no abstrato, e a pergunta era quantas o catálogo de verdade produz. As duas respostas diferem por um fator de três, e a segunda é a que decide design. **Número sobre um catálogo se mede rodando sobre o catálogo.**

---

O repositório está em `https://github.com/cupcake-mochi/JJK---Project.git`. **Ele é público desde 13/08/2026** — era privado até ali, e a autenticação por HTTPS dava trabalho demais para o que o repositório é. Ainda assim, **leia da pasta e não da web**: a pasta é a fonte da verdade, e o GitHub só tem o que já foi commitado.

**Comece pelos quatro passos e me diga o que você entendeu do estado atual.**
