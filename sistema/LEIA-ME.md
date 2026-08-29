# Projeto - M — pasta do projeto

Sistema de RPG de mesa em desenvolvimento, ambientado no universo de Jujutsu Kaisen, para um server de guilda com 5 a 7 mestres ativos e personagem persistente entre mesas. Material de fã, gratuito, sem fins comerciais.

## Onde está cada coisa

| Pasta | Conteúdo |
|---|---|
| `00-fundacao/` | Pitch de design e decisões que valem para o projeto inteiro |
| `01-pesquisa/` | Dossiê de metodologia, referências e análise do espaço de design |
| `02-esqueleto/` | Arquitetura do sistema: subsistemas, como se conectam, o que cada um resolve |
| `03-mecanica/` | As peças de regra, numeradas na ordem em que foram escritas, e os vinte e cinco validadores |
| `04-playtest/` | Roteiro de teste, formulários e retorno organizado por tema |
| `05-material/` | A **ficha de personagem** (e o gerador dela) e o **livro/**, o Manual da Guilda completo |
| `99-arquivo/` | **Material morto.** Nada aqui é regra corrente — ver o `LEIA-ME.md` de lá |
| `skills/` | Cópia de trabalho das sete skills de apoio |

**Sobre o `99-arquivo/`:** quando uma peça é substituída, ela não é apagada — vai para lá com um cabeçalho dizendo de onde saiu, o que a substituiu e **por que morreu**. Se você está escrevendo peça nova, não leia de lá.

## Ordem de leitura para quem chega agora

1. `ESTADO-ATUAL.md` — onde o projeto parou e o que vem em seguida
2. `00-fundacao/pitch-de-design.md` — o que este jogo é e o que ele não é
3. `01-pesquisa/dossie-de-metodologia.md` — a seção 8 é o resumo executivo: as dez travas que o sistema precisa respeitar
4. `../logs/CHANGELOG.md` — o que mudou e por quê

## As sete skills

Instaladas na conta e disponíveis em qualquer conversa, não só nesta pasta. **Duas são de procedimento, quatro são de assunto e uma é sobre a conversa:**

- **`rpg-da-guilda`** — o procedimento deste repositório: ordem de leitura, de onde rodar os validadores, o que a triagem de nomes não pega, como escrever arquivo neste mount, o arnês de perturbação, como fechar versão
- **`pesquisa-antes-de-propor`** — o gatilho que obriga levantamento externo antes de propor, onde procurar por domínio, como julgar fonte e o que **não** se pesquisa fora

- **`design-mecanicas-rpg`** — teste de dominância, bônus automático, filtro multi-mestre, aprovação de habilidade de jogador
- **`balanceamento-simulacao`** — contrato de invariantes, busca exaustiva, matriz de dominância, regressão
- **`playtesting-rpg`** — estágios de teste, casos-sonda para divergência entre mestres, formulários
- **`redacao-acessivel-rpg`** — jargão, colisão de termo, progressive disclosure, como não soar como texto de máquina

- **`gasto-de-modelo`** — fecha a resposta com uma linha dizendo se a tarefa pedia o modelo em que ela foi aberta

A pasta `skills/` guarda o `SKILL.md` de cada uma mais os arquivos de apoio. ~~**A versão instalada não traz as pastas de apoio.**~~ **Morreu na v0.93: elas estão lá, e batem byte por byte com as daqui** — os seis arquivos das quatro skills com pasta. *Esse aviso nasceu na v0.66, valeu enquanto valeu, e foi conferido de novo antes de sair.* **O que continua verdade é a outra metade: reinstalar sem as pastas recria o ponteiro pendurado, então toda reinstalação leva elas junto.** E mexer nos arquivos da pasta **não** altera a skill instalada. **As duas divergem sozinhas e nenhum validador alcança essa camada:** na v0.40, as cinco que estavam instaladas estavam todas atrás da pasta.

## Versão atual

**v0.176.** Fases 0 a 3 fechadas; a Fase 4 (mecânica) está em andamento com **vinte e cinco peças escritas e vinte e cinco validadores passando**. O manual do Fundamento está na **v7.19**, e ele é um subsistema fechado — a técnica e o feitiço já funcionam. O `.pdf` **está na mesma versão do `.docx`** desde a v0.93 — ele deixou de ser exportado a mão.

**Dá para montar uma ficha de nível 2, jogar uma missão inteira e recuperar entre elas, pelas nove rotas de Origem.** *Eram seis até a v0.122, oito de lá até a v0.168, e a nona é a peça 25.* Desde a v0.32 não sobrou peça de regra travando ninguém nessa faixa: das dezessete coisas que uma ficha de nível 2 precisa, **treze existem, e as quatro que faltam não mordem nessa faixa**. A ordem do resto está no `ESTADO-ATUAL.md`.

O que falta hoje não é regra, é **material**. A **ficha de personagem** saiu na v0.35 e está em `05-material/`, com o gerador dela. **O quick-start foi abandonado na v0.102**, por decisão do Mizuki — o texto de mesa iria direto para o PDF — **e o PDF saiu na v0.106**: `05-material/livro/`, com o quick-start escrito direto nele. *A paginação de hoje sai do build e não fica publicada aqui — as `230` desta linha eram as da v0.106, e elas envelheceram sozinhas por sessenta e três versões.* E `04-playtest/` continua vazia — **zero sessões desde a v0.1**.

**Cinco** leem o manual e precisam de `python-docx`: `conferir-dano.py`, `conferir-manual.py`, `conferir-nomes.py`, `conferir-pericias.py` e `conferir-progressao.py`. **Sem ele eles pulam as checagens que leem o `.docx`** em vez de falhar. Puladas por validador, lidas do código: **1 de 10** · **4 de 4** (todas — ele sai no `except ImportError` antes da primeira) · **3 de 5** · **1 de 8** · **1 de 8**. *O `conferir-atributos.py` estava nesta lista até a v0.102 e saiu dela: as condições mudaram para a peça 19, e com elas foi a única checagem dele que abria o `.docx`.* *Desde a v0.101 os cinco dizem no rodapé que pularam, e o `subir.sh` marca com `ok*` amarelo.*

> *Esta linha ficou parada em **três** até a v0.102 — o `README` e o `ESTADO-ATUAL` foram corrigidos na v0.100 e este arquivo não. **Três cópias, e a terceira envelheceu sozinha.***

*Até a v0.39 os três documentos diziam 4, 2 e 1. O número do `conferir-manual` era o mais perigoso dos três: ele estava escrito como o que pula menos e é o único que não confere nada.*

```
pip install python-docx --break-system-packages
cd sistema/03-mecanica && python3 conferir-nomes.py
```

**Rode de `03-mecanica/` mesmo assim.** *Até a v0.37 este arquivo dizia que rodar de outro lugar fazia os três pularem checagem — isso era verdade e deixou de ser:* hoje os três resolvem o caminho do `.docx` por `os.path.dirname(os.path.abspath(__file__))`, e de `/tmp` saem com saída idêntica e zero puladas. O hábito fica porque é o que o `subir.sh` faz e é o que o resto da documentação supõe; o que não fica é a justificativa errada.

Os quatro últimos não leem o manual e não precisam de nada: o `conferir-criacao.py` confere a ficha de exemplo da peça 8 contra as fórmulas das outras peças, o `conferir-ficha.py` confere a ficha de `05-material/` contra os catálogos delas, o `conferir-legados.py` recalcula a tabela de totais da peça 13 e falha se o escrito não bater com o contado, e o `conferir-invocacoes.py` faz as trinta e uma checagens da peça 15 sem guardar um número sequer dentro dele.

## A próxima peça

**Pactos** fechou na v0.134 e é a peça 22, em `03-mecanica/22-pactos.md`, com o `conferir-pactos.py` e catorze checagens. Ela é a **quinta camada de personagem** e a **quarta economia de poder**, e abre em quatro formas — permanente, temporário, `Promessa` e de restrição. **Só o permanente tem teto**, e ele é metade da Essência arredondando para baixo, sem piso. *O Passo 8 da peça 8 prometia essa régua desde a v0.21.*

**Catálogo de entregas** fechou na v0.85 e é a peça 17, em `03-mecanica/17-catalogo-de-entregas.md`, com o `conferir-catalogo.py` e quinze checagens. Ela é um índice das **102 entradas** — 68 entregas de Trilha, 20 degraus de Caminho e as 14 Manhas — e não guarda preço nem texto de mesa: os dois continuam nos três `DESENHO-*.md` da raiz. **O validador dela é o primeiro do projeto que lê aqueles arquivos**, e a checagem que ele existe para ter é a que pega bloco de regra contradizendo o gate da linha de preço.

**Ferramenta amaldiçoada** fechou na v0.59 e é a peça 16, em `03-mecanica/16-ferramenta-amaldicoada.md`, com o `conferir-ferramenta.py` e dezenove checagens. A máquina é da v0.55, o catálogo de `Estigma` da v0.56 e da v0.57 — **dez** entradas desde a v0.152, quando o `Bojo` foi arrancado. A escada de grau do antigo §6 virou **ritmo de entrega e não gate**, porque como gate ela anulava o gate herdado da peça 11 e deixava o `Desgaste` sem nada para comprar.

*Invocações saiu desta seção na v0.58*, quando virou a **peça 15** com o `conferir-invocacoes.py` em cima dela.

**A fila foi reordenada na v0.50**, quando as duas peças que a v0.49 destampou ganharam posição: **Invocações → ferramenta amaldiçoada → Trilhas → objeto amaldiçoado**. Só a terceira posição contra a segunda era escolha; o resto a conta fechou. `Servo`, `Matilha` e `Coro` **são** o sistema de invocação, então Invocações trava Trilhas; e `objeto amaldiçoado` foi para o fim porque **destrava zero ficha** — Receptáculo e Reencarnado já rodam hoje.

*Equipamento fechou na v0.48 como peça 14*, com o `conferir-equipamento.py` em cima dela. Ela destravou a Vanguarda e a **Técnica Marcial**.

**O que ela não destravou foram as vagas de Desliga da peça 13, e a v0.49 descobriu por quê:** as quatro nomeavam a peça errada. Duas esperavam **ferramenta amaldiçoada** (arma forjada, tópico próprio), uma esperava **objeto amaldiçoado** — que não tem peça dona em lugar nenhum — e uma esperava **Técnica Marcial**, tendo nomeado o que a bloqueava em vez do dono. *Reclassificadas; nenhuma preenchida, porque Equipamento produziu um alvo legal só e ele não vale a entrada.*
