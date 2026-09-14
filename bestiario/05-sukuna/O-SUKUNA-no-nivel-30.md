# O Sukuna, remontado no nível 30

*13 e 14/09/2026, da v0.229 à v0.233 do repositório.* **Nenhum número nasce neste arquivo:** *todos saem de `montar-o-sukuna.py`, e a saída inteira está em `SAIDA-o-sukuna-nv30.txt`.* **O `O-SUKUNA-no-rascunho-5.md` continua como o teste de 10/09, no nível 20, e é lá que mora a comparação com a mesa de 07/09.**

## O que mudou desde o rascunho 5

| | rascunho 5 (nível 20) | agora (nível 30) | por quê |
|---|---|---|---|
| **nível** | `20` | **`30`** | ***decisão do Mizuki:*** *"sobe o sukuna pra Nv30"* — no `30` o refino da curva já é o do gate |
| **Integridade** | igual à vida | **metade da vida** | peça 24 §3.3, v0.228 |
| **o Santuário** | Intervenção sem preço, tratado como incompleta, raio `18 m` | **Expansão sem Barreiras**: raio `200 m`, `5` rodadas, Acerto garantido | peça 26 §6.4, v0.229 |
| **a Chama Divina** | a rodada inteira repartida em `3` alvos, `90` cada | **`Recarga` pela regra nova: `2,5` golpes em cada alvo, `18d12 + 50`** | peça 26 §6.5, v0.230 |
| **o encontro** | `8` pessoas | **`21,0` pessoas** | `8 × 1,92` da Expansão `× 1,37` da `Recarga` |
| **os papéis** | `Guardião` · `Apoio` | `Baluarte` · `Reforço` | triagem de nome da v0.224; o script parou de rodar ali |
| **a Amplificação de Domínio** | anula toda técnica, sem custo | **a aptidão `Extensão de Domínio` da peça 11**, paga na cota | peça 26 §6.5, v0.231 |
| **os Quatro Braços** | braço destrutível, sem vida | **`180` de vida por braço** | o empate com duas rodadas pela frente, v0.231 |

## As quatro escolhas, fechadas em 14/09

| | a decisão | de onde sai o número |
|---|---|---|
| **os pontos livres** | **Força `3` · Constituição `4` · Inteligência `2`** — *na v0.233 são `9`: o orçamento meio a meio da v0.232 e o ponto de chefe na criação; na v0.230 eram `4`, e a escolha tinha sido Força `0`* | o script confere que fecham: `4` na criação e `5` em marco |
| **a `Técnica Reversa`** | **cura `90` no lugar de uma ação** — *"essa métrica já tinha sido calculada anteriormente, use ela de base"* | o empate da peça 26 §6.5: a vida `1620` ÷ a luta de `3` rodadas ÷ `6` ações |
| **a `Chama Divina`** | **Explosão de `3 m` que só mira um oponente fora do Santuário, e todo mundo nos `200 m` dentro** — *"é um dano em área que só pode ser usado em um alvo"* | a Forma do manual na `Classe 4`; o dano é o da `Recarga` |
| **o voto da barreira aberta** | **sai** | desde a v0.226 ele compraria o que o degrau já dá |

## A ficha

> ### Sukuna, o Rei Amaldiçoado
>
> *Maldição Média · **Calamidade** · `Artilheiro` · nível 30*
>
> **Defesa** `20` · **Acerto** `+10` · **CD** `18` · **Refino** `10` *(proteção `+4`)*
>
> **Vida** `1620` · **Integridade** `810` · **Deslocamento** `9 m`
>
> **Força** `3` · **Destreza** `6` *(Iniciativa)* · **Constituição** `4` · **Inteligência** `2` · **Essência** `6`
>
> **Físico** treinado · **Vigor** — · **Intelecto** — · **Espírito** treinado
>
> **Resistências** — · **Imunidades** — · **Vulnerabilidades** — · **Perícias** `Ocultismo` · `Intimidação` · `Percepção`
>
> **Traços**
>
> **Quatro Braços.** Ele conjura e ataca no mesmo turno: dois braços fazem o Selo enquanto dois lutam, e a boca do abdômen recita sem prender a respiração. Cada braço é um alvo com Defesa `20` e `180` de vida, e destruir um tira `1` das ações múltiplas dele.
>
> **Técnica Reversa.** No lugar de uma ação, ele cura `90` em si mesmo.
>
> **Ações**
>
> **Ações Múltiplas.** Ele faz seis ações, escolhendo entre `Desmembrar`, `Clivar` e `Teia de Aranha`, com no máximo uma `Teia de Aranha` por rodada.
>
> **Desmembrar.** *Ataque de conjuração:* `+10` para acertar, alcance `18 m`, um alvo. *Acerto:* `67 (6d10 + 34)` de dano Cortante. Corta qualquer coisa, com ou sem energia amaldiçoada.
>
> **Clivar.** *Ataque de conjuração:* `+10` para acertar, alcance `1,5 m`, um alvo com energia amaldiçoada. *Acerto:* `54 (12d8)` de dano Cortante, e o alvo fica `Impedido`. Não funciona em quem não tem energia amaldiçoada.
>
> **Teia de Aranha.** *Teste de Resistência Físico:* CD `18`, cada criatura numa `Esfera` de raio `3 m` a partir do chão que ele toca. *Falha:* `45 (10d8)` de dano de Concussão, e `Derrubado`. *Sucesso:* metade do dano, e não cai.
>
> **Chama Divina (Recarga 5-6) (depois de Desmembrar e Clivar).** Ela ocupa as ações múltiplas do turno. *Teste de Resistência Físico:* CD `18`. Fora do Santuário, uma `Esfera` de raio `3 m` num ponto a até `18 m`, e ele só a usa se houver um único oponente na área; dentro, cada criatura no raio do Santuário. *Falha:* `167 (18d12 + 50)` de dano de Fogo. *Sucesso:* metade do dano.
>
> **Intervenções**
>
> Três por luta, cada uma usada uma vez. Sai no máximo uma por rodada, logo depois do turno de outra criatura.
>
> **1. Desmembrar Dobrado.** Ele faz um `Desmembrar` fora do turno.
>
> **2. Santuário Malévolo.** Ele abre o domínio sem fechar barreira, num raio de `200 m`, e o centro fica onde ele está. Por `5` rodadas, `Desmembrar` e `Clivar` acertam sem rolagem e sem Teste de Resistência em quem estiver dentro, e `Clivar` dispensa o alcance. Quem sai do raio sai do Acerto. O domínio acaba pelo tempo, pela disputa com outro domínio, pela concentração ou com ele em `0` de vida.
>
> **3. Extensão de Domínio.** Ele se envolve numa camada fina de domínio sem técnica dentro, por até `10` rodadas. Ela anula o Acerto de uma Expansão, o ataque dele acerta independentemente da técnica do alvo, e o que encostar nela é anulado até `Classe 4`: uma Classe Passiva, uma Regra Própria ou um feitiço de Classe até `4`. Enquanto ela estiver de pé ele não usa a técnica, e as ações dele viram golpes de corpo. *Ataque corpo a corpo:* `+7` para acertar, alcance `1,5 m`, uma criatura. *Acerto:* `58 (8d6 + 30)` de dano de Concussão.

*O bloco não imprime linha de `Pacto`: o único voto que sobrou é o da `Chama Divina`, e ele mora na ação.*

## O que este bloco ainda não tem

- **A vida de braço é do Sukuna, e não regra da peça 26.** *O empate que deu `180` serve para qualquer inimigo com parte destrutível, e ninguém escreveu isso como regra.*
