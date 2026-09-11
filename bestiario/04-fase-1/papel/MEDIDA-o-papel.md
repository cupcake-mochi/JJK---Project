# O `papel` do inimigo — medido

*10/09/2026. Conta em `medir-o-papel.py`, saída completa em `SAIDA-da-medicao.txt`, fonte externa em
`fonte-4e-o-papel-com-numero.md`.*

> **A regra que estava escrita:** *"o papel REDISTRIBUI o orçamento que a categoria já deu, nunca
> ADICIONA"* — e o `PAPEL-do-inimigo-base.md` citava o **Draw Steel** como precedente.
> **Esta rodada dá a regra por boa e derruba o precedente.**

---

## 1 · O precedente é o **4e**, não o Draw Steel

### O Draw Steel faz o CONTRÁRIO do que o arquivo dizia

*Fórmulas do próprio livro, em `01-pesquisa/dmg2024-e-draw-steel.md`:*

> `EV = ((2 × nível) + 4) × modificador de organização`
> `Stamina = ((10 × nível) + modificador de papel) × modificador de organização`

**O `EV` — que é o custo de encontro — não lê o papel.** *Rodando nível `5`, `Platoon`:*

| papel | `Stamina` | dano | `EV` |
|---|---|---|---|
| `Brute` | **`80`** | `11,0` | `14` |
| `Ambusher` | `70` | `11,0` | `14` |
| **`Artillery`** | **`60`** | **`11,0`** | **`14`** |
| `Controller` | `60` | `9,9` | `14` |

> ### O `Brute` tem `1,33×` a Stamina do `Controller` e o MESMO custo.
> **E o `Brute` e o `Artillery` têm o mesmo modificador de dano — o `Brute` só leva `+20` de
> Stamina de graça.** *Isso não é redistribuição: é bônus. Importar direto traz de volta o defeito
> que matou a `Dupla` — dois donos no mesmo número.*

### O 4e publicou a troca COM NÚMERO, e ela funciona

*`Monster Statistics by Role`, DMG 4e:*

| papel | PV nv `0` | PV/nível | bônus de CA |
|---|---|---|---|
| `Soldier` | `24` | `+5` | **`+2`** |
| `Brute` | `26` | **`+7`** | **`−2`** |
| `Artillery` | `21` | `+3` | `−2` |

**Rodei a neutralidade: `PV efetivo` = `PV cru` ÷ chance de acerto.** *Nível `10`, em quatro âncoras
de acerto, porque a taxa base do 4e não está neste projeto:*

| acerto do PC contra a CA padrão | `Soldier` vs `Brute` | `Artillery` vs `Brute` |
|---|---|---|
| `50%` | `9,7%` de diferença | `58%` |
| `55%` | `6,0%` | `58%` |
| **`60%`** | **`3,1%`** | `58%` |
| `65%` | **`0,7%`** | `57%` |

> **O par `Brute` / `Soldier` fica dentro de `10%` em toda a faixa e aperta pra menos de `1%` no
> topo.** *O `Brute` compra PV cru com CA, e a durabilidade sai igual.* **É redistribuição de
> verdade.**
> **E o `Artillery` paga `42%` a `43%` da durabilidade em TODAS as âncoras** — esse número não se
> move. *O que ele compra com isso está no TEXTO da habilidade, não na tabela.*

### ⚠ E a pergunta que decide tudo: **o 4e não cobra pelo papel**

> *"XP does not depend on monster 'class' (brute, soldier, lurker, etc.) — any creature of a
> particular level is worth the same XP as any other of the same level."*

**O XP de 4e é nível + qualificador** (`Minion` `1/4` · `Elite` `2×` · `Solo` `5×`), *e o papel não
entra.*

> ### O 4e separa os dois eixos exatamente como a tua escada separa.
> **O qualificador é a `categoria`, e é ele que custa. O papel é o `papel`, e ele é de graça.**

---

## 2 · O invariante de neutralidade — e ele FECHOU EXATO

**Se o papel redistribui, alguma coisa tem de ficar constante. A conta diz qual:**

> `dano total na luta` = `dano por rodada` × `rodadas`, e `rodadas` = `vida ÷ dano do grupo`
> ### ⟹ o que o encontro custa é proporcional a **`vida × dano`**

**Se isso está certo, o produto tem de crescer com o QUADRADO das pessoas que a categoria pede.**
*Dobrar as pessoas dobra o dano delas E obriga o inimigo a durar o dobro.*

| categoria | pessoas | `vida × dano` | produto ÷ `Desastre` | `(pessoas ÷ 4)²` | |
|---|---|---|---|---|---|
| `Ameaça` | `1` | `12.980` | `0,06×` | `0,06×` | **ok** |
| `Desastre` | `4` | `206.955` | `1,00×` | `1,00×` | **ok** |
| `Catástrofe` | `6` | `464.776` | `2,25×` | `2,25×` | **ok** |
| `Calamidade` | `8` | `827.820` | `4,00×` | `4,00×` | **ok** |

> ### Quatro de quatro, sem erro nenhum.
> **A regra *"redistribui, nunca adiciona"* deixou de ser princípio e virou conta:** *um papel que
> faz `vida × m` e `dano ÷ m` não muda quantas pessoas o inimigo pede.*

---

## 3 · ⚠ Mas a banda do `o golpe` fecha o eixo do DANO pra cima

**A escada mede `o golpe` como fatia da vida de UM personagem, e publica a banda:**

> *"A banda inteira é de `21%` a `32%` — onze pontos. A do bestiário antigo era de `23%` a `45%`, e
> **o topo dela era a `Dupla`**."*

| categoria | fatia hoje | teto | **o dano pode subir** |
|---|---|---|---|
| `Ameaça` | `23%` | `32%` | `1,39×` |
| `Catástrofe` | `27%` | `32%` | `1,19×` |
| **`Desastre`** | **`30%`** | `32%` | **`1,07×`** |
| **`Calamidade`** | **`30%`** | `32%` | **`1,07×`** |

> **O `Desastre` — que é a mesa padrão — tem `7%` de espaço. Isso é nada.**
> **E o espaço é DIFERENTE em cada categoria**, então um `m` único não serve: um papel que sobe o
> dano quebraria a banda na categoria mais usada e caberia na menos usada.

**A direção de BAIXO cabe sempre**, porque o piso da banda é `21%` e descer o dano desce o golpe.

---

## 4 · O eixo que o 4e usa, e que a banda NÃO alcança: **`vida` contra `Defesa`**

**O 4e não troca PV por dano. Ele troca PV por CA — e esse eixo não toca no dano, então a banda do
`o golpe` não chega nele.**

*A Defesa do inimigo no nv30 é `20`, e o personagem acerta alvo difícil em `50%` (peça 1 §5.2). Um
ponto de Defesa move `5` pontos percentuais num `d20`.*

| Defesa | acerto do PC | vida efetiva | **a vida crua precisa ser** |
|---|---|---|---|
| `18` | `60%` | `1,67×` | **`× 1,20`** |
| `19` | `55%` | `1,82×` | `× 1,10` |
| **`20`** | **`50%`** | **`2,00×`** | **`× 1,00`** |
| `21` | `45%` | `2,22×` | `× 0,90` |
| `22` | `40%` | `2,50×` | **`× 0,80`** |

**Rodado num `Desastre` nv30:**

| papel | Defesa | vida | dano | `o golpe` | fatia | **vida efetiva** |
|---|---|---|---|---|---|---|
| ‹ sem papel › | `20` | `945` | `219` | `73` | `30%` | **`1890`** |
| **`Brutamontes`** | `18` | **`1134`** | `219` | `73` | `30%` | **`1890`** |
| **`Guardião`** | `22` | **`756`** | `219` | `73` | `30%` | **`1890`** |

> ### A vida efetiva fica IGUAL nos três, e `o golpe` não se move.
> **`−1` de Defesa pede `×1,10` de vida crua. `−2` pede `×1,20`. `+2` devolve `×0,80`.**
> *É o `Brute` do 4e traduzido, e o número sai de conta, não de gosto.*

---

## 5 · Os seis papéis, um a um

| papel | a troca | cabe? |
|---|---|---|
| **`Brutamontes`** | Defesa `↓`, vida `↑` | **cabe, com câmbio exato.** `−2` de Defesa por `×1,20` de vida |
| **`Guardião`** | Defesa `↑`, vida `↓` | **cabe, mesmo câmbio ao contrário.** E o que ele faz pelo aliado sai do `dano ↓`, ao câmbio `1 pra 1` de dano evitado |
| **`Controlador`** | dano `↓` → efeito | **cabe.** A peça 19 §2.2 já converte: `N` ações negadas por `M` pontos |
| **`Apoio`** | o próprio orçamento → o dos aliados | **cabe.** O mesmo `1 pra 1`, só que o destino é outro bloco |
| **`Artilheiro`** | vida `↓` → alcance `↑` | **cabe pela metade** — ver abaixo |
| **`Emboscador`** | pico `↑`, sustentado `↓` | **⚠ NÃO CABE do jeito que está escrito** — ver abaixo |

### ⚠ O `Emboscador` é o único que a banda REPROVA

*"Some, aparece e estoura um alvo sozinho" = concentrar o mesmo dano em menos ações. Medido num `Desastre` nv30:*

| ações | `o golpe` | fatia da vida de um PC | na banda? |
|---|---|---|---|
| `3` | `73,0` | `30%` | sim |
| **`2`** | `109,5` | **`45%`** | **NÃO** |
| `1` | `219,0` | **`90%`** | **NÃO** |

> ### `45%` é, ao ponto percentual, o número que matou a `Dupla`.
> **Então o `Emboscador` não pode concentrar dano.** *Ele troca no eixo de mobilidade e de esconder
> — que é exatamente onde o 4e põe o `Lurker`, e o `Lurker` do 4e paga em PV (`+3`/nível, o mais
> baixo da tabela), não em concentração de golpe.*

### ⚠ O `Artilheiro` esbarra num preço que o sistema não tem

**Alcance de ataque não tem câmbio publicado.** *O único câmbio de metro que o sistema tem é o de
**deslocamento** — `1 m` = `0,60` de dano por rodada, da peça 5 §4.*

**Usando ele como convenção:** sair de `1,5 m` pra `18 m` vale `9,90` de dano por rodada — **`4,5%`
da cota de um `Desastre`**, ou `3%` da vida dele numa luta de três rodadas.

> ### E aí está o problema: o 4e cobra `42%` da durabilidade pelo alcance, e o câmbio do teu sistema cobra `3%`.
> **Uma ordem de grandeza de diferença.** *E a causa é honesta: o `0,60` preça **mover**, não
> **alcançar**. São coisas diferentes, e o sistema só tem preço pra uma.*

---

## 6 · O `Líder` — o número existe, o problema é o nome

**Se a categoria ganhar um degrau, o invariante do §2 determina os números; só sobra escolher as ações.**

| pessoas | fator | vida | dano | ações | `o golpe` | fatia | na banda? |
|---|---|---|---|---|---|---|---|
| `2` | `0,50` | `472` | `110` | `1` | `109,5` | `45%` | **NÃO** |
| **`2`** | `0,50` | `472` | `110` | **`2`** | `54,8` | **`22%`** | **sim** |
| `3` | `0,75` | `709` | `164` | `2` | `82,1` | `34%` | **NÃO** |
| **`3`** | `0,75` | `709` | `164` | **`3`** | `54,8` | **`22%`** | **sim** |

> **O degrau é construível.** *Duas pessoas com `2` ações, ou três com `3`.*

### Mas o `Apoio` já é isso, e por outro eixo

**O papel `Apoio` já está definido como *"fortalece os outros — o próprio orçamento vira o dos
aliados"*.** *Um degrau de categoria chamado `Líder` que "melhora os outros" é a mesma ideia em dois
eixos.*

> **Dois nomes pra uma coisa é o defeito que a skill `redacao-acessivel-rpg` chama de *"uma coisa por nome"*.**
> **A saída limpa: a `categoria` é sobre TAMANHO — quantas pessoas —, e o que ele faz com os aliados
> é o PAPEL `Apoio` pendurado nela.** *`Desastre Apoio` já diz tudo, sem degrau novo.*

---

# O que a medida entrega pras quatro decisões

| # | pergunta | o que a conta diz |
|---|---|---|
| **3** | cabeçalho ou traço nomeado? | *a conta não decide, mas o teto decide:* **o bloco tem `6` entradas nomeadas e `3` já estão gastas nas `Intervenções`.** Traço nomeado gastaria uma das `3` que sobram. E o `RASCUNHO-4` fixou o critério: *traço nomeado é o que pode ser desligado ou roubado* — **e o papel não pode, porque ele já está nas células** |
| **4** | muda número ou é etiqueta? | **pode mudar, e o eixo que funciona é `vida ↔ Defesa`**, com câmbio exato. O eixo `vida ↔ dano` é neutro mas a banda fecha uma direção dele |
| **5** | a categoria ganha um `Líder`? | **o número existe** (`2` pessoas com `2` ações). **O nome é que colide com o papel `Apoio`** |
| **—** | *(nova)* o `Artilheiro` paga por alcance? | **o sistema não tem preço de alcance.** O único câmbio de metro que ele tem é de deslocamento, e ele é `14×` mais barato que o que o 4e cobra |
