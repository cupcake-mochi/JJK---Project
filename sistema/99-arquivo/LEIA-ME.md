# Arquivo morto

Nada aqui é regra corrente. Tudo aqui foi substituído, ou já cumpriu o que tinha para cumprir.

**Existe por dois motivos.** O primeiro é que a decisão que substituiu uma peça só faz sentido se você conseguir ver o que ela substituiu. O segundo é prático: material superado espalhado pelas pastas vivas atrapalha busca, e o `CHANGELOG` fica poluído de coisa que ninguém vai consultar.

**Regra de uso:** se você está escrevendo peça nova, não leia daqui. Leia o `ESTADO-ATUAL.md` e o `CHANGELOG.md`. Isto aqui é para quando você quiser saber *por que* alguma coisa mudou e o changelog não bastar.

## O que tem em cada pasta

| pasta | o que é |
|---|---|
| `secoes-substituidas/` | trechos que foram tirados de dentro de peças vivas quando envelheceram. Cada arquivo diz de onde saiu, o que o substituiu e **por que morreu** |
| `construcao-das-skills/` | o benchmark das quatro skills de apoio, da v0.3: nove execuções, o script que gerou tudo e o visualizador. Mais o `feedback.json`, que é o retorno que virou a v0.4 |
| `ferramentas-de-decisao/` | o comparador de curvas, que abre no navegador. Ele calibrou seis mecânicas de resolução na mesma chance de sucesso e serviu para a escolha do d20 na v0.3. Decisão fechada, ferramenta aposentada |
| `PROMPT-DE-CONTINUIDADE.md` | o prompt de retomada que foi usado até a v0.14. O `ESTADO-ATUAL.md` faz esse trabalho melhor hoje |
| `PROMPT-CHAT-NOVO.md` | o **segundo** prompt de retomada, da v0.15 à v0.44. Morreu na v0.45 medido: **15 dos 16 blocos eram cópia**, e nenhum validador o alcançava. *Dois arquivos, o mesmo motivo, trinta versões de distância — leia o cabeçalho dele antes de escrever um terceiro* |
| `RASCUNHO-pactos.md` | o levantamento que virou a **peça 22** na v0.134 — as quatro formas, a fonte e a conta do orçamento. *Arquivado no dia em que a peça nasceu:* **rascunho vivo ao lado da peça que ele gerou é a segunda fonte da regra.** O cabeçalho dele lista as duas coisas que **não** sobreviveram como estavam |
| `RASCUNHO-bloqueio.md` | o levantamento que virou a **peça 23** na v0.143, quando o `Bloquear` deixou de ser opcional. *Mesmo motivo dos outros: rascunho vivo ao lado da peça é a segunda fonte* |
| `RASCUNHO-clash-de-expansoes.md` | aberto na v0.28 e arquivado na v0.173, e **é o primeiro que veio para cá sem ter virado peça** — o dono dele acabou sendo o manual, na v7.18. O cabeçalho traz a reprovação medida do modelo de push gradual |
| `RASCUNHO-ritmo-de-xp.md` | aberto e fechado em duas versões: v0.195 mediu o repreço da curva de XP, e a **v0.196** escreveu ele na peça 12 e no capítulo 80 — esticando a curva mais uma vez no caminho. *O cabeçalho lista as **quatro** coisas dele que não sobreviveram à conferência* — a tabela nível a nível tinha ruído, a do gatilho estava medida a uma faixa só, e dois números da prosa eram arredondamento recontado |
| `PROMPT-TRILHAS.md` | **o terceiro, e ele foi escrito catorze versões DEPOIS do aviso acima.** Feito na v0.59 para o chat de Trilhas; ficou aqui desde então **sem cabeçalho e sem entrada nesta tabela**, com cara de documento vivo. *Envelheceu igual aos outros dois: manda conferir a versão contra `v0.59`, ler o CHANGELOG até a v0.50 e afirma 19 validadores.* **Catalogado na v0.69, varrendo lixo.** |

## Como arquivar coisa nova

Quando uma peça for substituída, **não apague**. Mova para a subpasta certa e escreva no topo do arquivo:

- de onde saiu (arquivo e seção)
- o que a substituiu
- em que versão
- **por que morreu** — esta é a parte que importa e a única que não dá para reconstruir depois
- o que dela sobreviveu, e onde está agora

Se o trecho estava dentro de uma peça que continua viva, deixe na peça viva **um parágrafo curto** com o que sobreviveu e um ponteiro para cá. Não deixe a seção morta inteira com um aviso em cima: ela continua aparecendo em busca e continua ocupando a atenção de quem lê.
