# O Sukuna, remontado no nível 30

*13/09/2026, v0.229 do repositório.* **Nenhum número nasce neste arquivo:** *todos saem de `montar-o-sukuna.py`, e a saída inteira está em `SAIDA-o-sukuna-nv30.txt`.* **O `O-SUKUNA-no-rascunho-5.md` continua como o teste de 10/09, no nível 20, e é lá que mora a comparação com a mesa de 07/09.**

## O que mudou desde o rascunho 5

| | rascunho 5 (nível 20) | agora (nível 30) | por quê |
|---|---|---|---|
| **nível** | `20` | **`30`** | ***decisão do Mizuki:*** *"sobe o sukuna pra Nv30"* — no `30` o refino da curva já é o do gate |
| **Integridade** | igual à vida | **metade da vida** | peça 24 §3.3, v0.228 |
| **o Santuário** | Intervenção sem preço, tratado como incompleta, raio `18 m` | **Expansão sem Barreiras**: raio `200 m`, `5` rodadas, Acerto garantido | peça 26 §6.4, v0.229 |
| **o encontro** | `8` pessoas | **`15,4` pessoas** | ***decisão do Mizuki:*** *"é esperado o encontro ficar maior nesse caso"* — nada no bloco é dividido |
| **os papéis** | `Guardião` · `Apoio` | `Baluarte` · `Reforço` | triagem de nome da v0.224; o script parou de rodar ali |

## A ficha, com o que a máquina deriva

> ### Sukuna, o Rei Amaldiçoado
>
> *Maldição Média · **Calamidade** · `Artilheiro` · nível 30*
>
> **Defesa** `20` · **Acerto** `+10` · **CD** `18` · **Refino** `10` *(proteção `+4`)*
>
> **Vida** `1620` · **Integridade** `810` · **Deslocamento** `9 m`
>
> **Destreza** `6` *(Iniciativa)* · **Essência** `6` · ⏳ *os outros três, com `4` pontos livres*
>
> **Físico** treinado · **Espírito** treinado · **Vigor** — · **Intelecto** —
>
> **Perícias** `Ocultismo` · ⏳ *as outras*
>
> **Ações**
>
> **Ações Múltiplas.** Ele age `6` vezes por rodada.
>
> **Desmembrar.** *Ataque de conjuração:* `+10` para acertar, um alvo. *Acerto:* `67 (6d10 + 34)` de dano cortante. Corta qualquer coisa, com ou sem energia amaldiçoada.
>
> **Clivar.** *Ataque de conjuração:* `+10` para acertar, alcance `1,5 m`, um alvo com energia amaldiçoada. *Acerto:* `54 (12d8)` de dano cortante, e o alvo fica `Impedido`. Não funciona em quem não tem energia amaldiçoada.
>
> **Teia de Aranha.** *Teste de Resistência Físico:* CD `18`, cada criatura numa `Esfera` de raio `9 m` a partir do chão que ele toca. *Falha:* `45 (10d8)` de dano de Concussão, e `Derrubado`. *Sucesso:* metade do dano, e não cai.
>
> **Intervenções**
>
> Três por luta, cada uma usada uma vez. Sai no máximo uma por rodada, logo depois do turno de outra criatura.
>
> **Santuário Malévolo.** Ele abre o domínio sem fechar barreira, num raio de `200 m`, e o centro fica onde ele está. Por `5` rodadas, `Desmembrar` e `Clivar` acertam sem rolagem e sem Teste de Resistência em quem estiver dentro, e `Clivar` dispensa o alcance. Quem sai do raio sai do Acerto. O domínio acaba pelo tempo, pela disputa com outro domínio, pela concentração ou com ele em `0` de vida.

*A `Esfera` de `9 m` é a área natural do nível `25` a `30`, na peça 26 §6.5.* **O `Artilheiro` ganha alcance e não tem célula**, *e o alcance do `Desmembrar` fica para o bloco de livro.*

## O que falta para o bloco de livro — escolha do Mizuki

| # | o que | o que a regra já diz |
|---|---|---|
| **1** | **os `4` pontos livres de atributo** | *as duas obrigadas comem `12` dos `16` pontos e `6` dos `7` marcos; no rascunho 5 os livres foram espalhados para nenhum atributo ficar em `0`* |
| **2** | **a `Técnica Reversa`** | *no rascunho 5 era cura de `70`, e nenhuma régua escrita dá esse número; a peça 26 §6.5 mede a cura do inimigo contra a vida dele, e ela empata em um terço* |
| **3** | **a `Chama Divina`** | *era "linha de `18 m`", e a `Linha` não existe mais entre as áreas de inimigo — são `Esfera`, `Cone` e `Retângulo`, com o `Cone` de `22,5 m` no nível `30`; repartida em `3`, ela entrega `135 (8d12 + 83)` por alvo, e só `39%` disso é dado, abaixo da metade que a peça 26 §4.4 pede* |
| **4** | **o voto da "barreira aberta"** | *ele pagava a fuga e ganhava o raio; desde a v0.226 isso é o degrau da Expansão sem Barreiras, e o pacto passaria a comprar o que a regra já dá* |
