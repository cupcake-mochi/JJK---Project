# RPG da Guilda — sistema de mesa de Jujutsu Kaisen

Sistema de RPG de mesa feito do zero, ambientado no universo de Jujutsu Kaisen, para um server de guilda com **5 a 7 mestres ativos** e **personagem persistente entre mesas**. Material de fã, gratuito, sem fins comerciais.

**Versão v0.27** · manual do Fundamento na **v7.6** · **onze peças de regra** e **sete validadores passando**.

---

## O que este projeto é, em três frases

O problema que ele existe para resolver não é "fazer um RPG de JJK": é **o mesmo personagem passar por sete mesas diferentes e continuar sendo o mesmo personagem**. Por isso quase toda decisão aqui passa por um filtro — *dois mestres que nunca conversaram chegam ao mesmo número?* — e por isso o projeto tem mais validador que a maioria dos sistemas publicados.

O coração é o **Fundamento**: um subsistema fechado e já validado que resolve técnica, feitiço, Melhoria, Restrição, Liberação Máxima e dano de alma por orçamento de pontos. Ele mora em `manual/` e é gerado por código. Tudo em `sistema/` é o que existe **em volta** dele — atributos, Caminhos, perícias, criação de personagem, descanso, aptidões.

E o registro do **porquê** de cada decisão é tão importante quanto a regra: `logs/CHANGELOG.md` tem 27 versões de argumento, e é a única parte do projeto que não dá para reconstruir sozinho lendo o resto.

## Por onde começar, se você acabou de clonar isto

1. **`sistema/ESTADO-ATUAL.md`** — o sistema inteiro em uma página: o que existe, o que não existe (tem uma seção medida sobre isso), e onde o trabalho parou.
2. **`logs/CHANGELOG.md`** — de cima para baixo, a entrada do topo é a mais recente. Leia até pelo menos a v0.16.
3. **`sistema/02-esqueleto/arquitetura.md`** — o mapa. É o documento mais antigo: **se ele contradisser uma peça de `03-mecanica/`, a peça vence.**
4. As peças de **`sistema/03-mecanica/`**, na ordem numérica.

**Não leia de `sistema/99-arquivo/` para escrever peça nova.** É material morto, guardado com o motivo de cada morte escrito no topo.

## Como está organizado

```
.
├── README.md              você está aqui
├── logs/
│   ├── CHANGELOG.md                     o porquê de cada decisão, v0.1 a v0.27
│   └── CHANGELOG-manual-v6-para-v7.md   o changelog do manual, antes de ele entrar aqui
├── manual/
│   ├── Fundamento-MANUAL-v7.docx        v7.6 — o manual gerado
│   ├── Fundamento-MANUAL-v7.pdf         v7.4 — exportado à mão, por isso atrasado
│   ├── gerador/                         Node + docx. `node make.js` recria o .docx do zero
│   └── matematica/                      pac7.py e v7.py, os validadores do manual
└── sistema/
    ├── ESTADO-ATUAL.md                  o ponto de retomada
    ├── LEIA-ME.md                       o mapa das pastas
    ├── 00-fundacao/                     os três pilares e as restrições do projeto
    ├── 01-pesquisa/                     dossiê de metodologia — a seção 8 lista as dez travas
    ├── 02-esqueleto/                    arquitetura: subsistemas e como se encaixam
    ├── 03-mecanica/                     as onze peças de regra e os sete validadores
    ├── 04-playtest/                     vazia. Zero sessões em 27 versões
    ├── 05-material/                     vazia. Ficha e quick-start ainda não existem
    ├── 99-arquivo/                      material morto, com LEIA-ME próprio
    └── skills/                          cópia de trabalho das quatro skills de apoio
```

**`_backup/` não entra no repositório** — ele guarda o estado da pasta antes da reorganização, e o `.gitignore` o segura.

## Preparar a máquina

```bash
pip install python-docx --break-system-packages    # dois validadores leem o .docx
cd manual/gerador && npm install docx               # só se for regerar o manual
```

Sem `python-docx`, o `conferir-nomes.py`, o `conferir-manual.py` e o `conferir-pericias.py` **pulam** as checagens que leem o manual em vez de falhar — então eles saem verdes sem terem conferido nada. Instale antes de confiar num "OK".

## Rodar os validadores

**Antes de mexer em qualquer número.** Eles falham alto se algo quebrar.

```bash
cd sistema/03-mecanica
python3 conferir-atributos.py     # acerto, defesa, TR, perícia, vida, PE máximo, deriva
python3 conferir-acao.py          # régua das Restrições, dominância, Adianta
python3 conferir-pericias.py      # quadro de perícias, listas de Caminho e Origem, colisão
python3 conferir-descanso.py      # piso, exaustão, arredondamento, magnitude, empilhamento
python3 conferir-nomes.py         # todo nome batizado, projeto → manual
python3 conferir-manual.py        # vocabulário e números importados, manual → projeto
python3 conferir-aptidoes.py      # a trava do refino, as três rotas do marco, o kokusen
```

E os dois do manual, que conferem número em vez de vocabulário:

```bash
cd manual/matematica && python3 pac7.py && python3 v7.py
```

**Antes de batizar qualquer coisa**, rode a triagem. Ela passa o nome contra o vocabulário inteiro do manual e do projeto, nas duas direções:

```bash
cd sistema/03-mecanica
python3 conferir-nomes.py --candidatos Vulto Matilha Bigorna
```

Ela já matou mais de dez nomes que pareciam livres.

## Commitar

```bash
./subir.sh "o que mudou"
```

Ele roda **os dez validadores**, mostra o que mudou, commita e dá push — e **se recusa a commitar se algum falhar**. Um commit que registra regra quebrada é pior que nenhum commit: daqui a três versões ninguém sabe em qual commit ela entrou.

Se a mensagem for longa, o assistente deixa ela pronta em `mensagem-de-commit.txt` e você roda `./subir.sh` sem argumento — ele usa o arquivo e apaga depois.

> **O assistente não consegue commitar nesta pasta, e isso não tem conserto.** Ele lê, edita e roda os validadores normalmente, mas o `git commit` falha: o git finaliza cada objeto com *escreve temporário → `chmod` → `rename`*, e o mount pelo qual a pasta é exposta ao sandbox força permissão fixa e **rejeita o `chmod`** (`unable to set permission`). O objeto fica no disco pela metade — aparece no `ls` e não abre. Não é configuração do git; é como a pasta é montada. O commit é sempre seu.

## Regerar o manual

O `.docx` **não é editado à mão** — ele é gerado.

```bash
cd manual/gerador
npm install docx
node make.js
cp Fundamento-MANUAL-v7.docx ../Fundamento-MANUAL-v7.docx
```

`manual/gerador/COMO-USAR.txt` diz onde mexer em cada parte e traz o histórico de mudanças de cada versão do manual. **Rode `pac7.py` antes de gerar** se você mexeu em número, exemplo ou feitiço pronto.

O `.pdf` é exportado à mão e por isso vive atrasado — hoje ele está na v7.4 e o `.docx` na v7.6.

---

## Como o projeto trabalha

Isto não é preferência de estilo: é o que evitou os erros que estão registrados no CHANGELOG.

**Número vem de conta rodada, nunca de intuição.** Se dominância, deriva ou o filtro multi-mestre já decidem, a conta decide e ninguém pergunta. A pergunta é para onde a conta empata ou não se aplica.

**Escolha de sabor é do Mizuki** — quantos itens numa lista, quais são, como se chamam, em que ordem aparecem. Traga as opções com o número e o trade-off de cada uma já calculados, e pergunte. Várias rodadas de pergunta, nunca uma proposta grande pronta.

**Todo número novo ganha validador, com teste negativo conferido** — perturbar o valor e provar que a checagem certa acende.

**Peça substituída vai para `99-arquivo/`** com cabeçalho dizendo de onde saiu, o que a substituiu, em que versão, **por que morreu** e o que dela sobreviveu. A última linha é a que não dá para reconstruir depois.

**Antes de fechar versão, revisão cética** — inclusive contra o que você mesmo acabou de escrever. Metade dos achados grandes do CHANGELOG saiu daí.

**Documento não pode ter cara de saída de IA.** Seções de tamanhos diferentes, sem simetria forçada, sem "além disso" e "em suma". Português informal.

## Seis lições que custaram erro

1. **Numa rolagem disputada, os dois lados crescem no mesmo ritmo.** Verificar invariância contra o nível não basta — tudo que cresce numa campanha entra no teste. Foi o que pegou a maestria a cada quatro níveis (v0.9) e, com o dobro do tamanho, o refino na Defesa (v0.27).
2. **"Esse número já inclui o que eu estou somando nele?"** Errou em v0.16, v0.17, v0.19, v0.24, v0.26 e v0.27. É o erro mais teimoso do projeto.
3. **Contagem não é valor.** Meça peso de mesa, não quantidade — Inteligência já teve mais perícias que Essência e valia menos.
4. **Antes de batizar, cheque colisão nas duas direções.** Hoje isso é o `conferir-nomes.py`.
5. **Tensão de preço às vezes é lacuna de texto disfarçada.** Confira se a regra diz o que você acha que ela diz antes de mexer no número. Pagou duas vezes na mesma Restrição, em versões diferentes.
6. **Antes de aceitar um preço, veja se o termo que ele usa existe.** A Passiva Casca cobrava por *"dano físico"*, e a expressão aparecia **uma vez no manual inteiro — dentro dela mesma**. Hoje isso é o `conferir-manual.py`.

## O que existe, e o que não existe

**Dá para montar uma ficha de nível 2, jogar uma missão inteira e recuperar entre elas**, por seis das nove rotas de Origem — e sem nenhum buraco de regra que morda nessa faixa.

**O que não existe, e faz falta:** a tabela de XP (que é a trava nº 1 de mundo compartilhado), uma tabela de progressão consolidada, a ficha de personagem, o quick-start jogável, e o playtest. `04-playtest/` está vazia: **zero sessões em 27 versões, e todo número do sistema é previsão.**

A seção *"O que existe e o que não existe, medido"* do `ESTADO-ATUAL.md` tem a conta.

## Licença e escopo

Material de fã, sem fins comerciais, não afiliado à Shueisha, à MAPPA nem a Gege Akutami. Jujutsu Kaisen e seus personagens pertencem aos detentores originais. Este repositório é privado e existe para o trabalho da Guilda.
