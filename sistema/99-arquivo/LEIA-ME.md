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

## Como arquivar coisa nova

Quando uma peça for substituída, **não apague**. Mova para a subpasta certa e escreva no topo do arquivo:

- de onde saiu (arquivo e seção)
- o que a substituiu
- em que versão
- **por que morreu** — esta é a parte que importa e a única que não dá para reconstruir depois
- o que dela sobreviveu, e onde está agora

Se o trecho estava dentro de uma peça que continua viva, deixe na peça viva **um parágrafo curto** com o que sobreviveu e um ponteiro para cá. Não deixe a seção morta inteira com um aviso em cima: ela continua aparecendo em busca e continua ocupando a atenção de quem lê.
