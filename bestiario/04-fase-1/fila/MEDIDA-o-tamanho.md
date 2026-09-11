# O `tamanho` vira regra — a troca, medida

*10/09/2026. Conta em `medir-o-tamanho.py`, saída em `SAIDA-tamanho.txt`.*

> ***Decisão do Mizuki:*** *"vira regra, vamos seguir o molde de Draw Steel por enquanto… **mas
> lembrando q tamanho tem q ter uma troca**."*

---

> ## ✅ CORREÇÃO — 10/09/2026: **ele ABRIU.**
> **O `Rules/Draw Steel Heroes.md` está no dump de `dados-recarga-area/`**, e a seção `Size and Space`
> abre inteira. *A caixa abaixo ficou como registro do que se sabia antes.*
>
> **E o que ela dizia por dedução estava CERTO no essencial e ERRADO no tamanho do acerto:**
>
> | | |
> |---|---|
> | *"a troca é construída com os câmbios do Projeto-M, **não copiada do Draw Steel**"* | ✅ **certo — e mais do que se sabia.** *Lá o `size` **não tem troca nenhuma**: Stamina `1,000 ×`, EV `1,000 ×`, medido em `415` statblocks* |
> | o alcance por degrau | ✅ **confirmado no campo** — `size 2` = `Melee 2`, `size 4` = `Melee 3`, `size 5` = `Melee 4` |
> | pegar mais alvos | ✅ **também é do campo** — `43%` das ações de corpo a corpo de `size 2+` pegam `2+` alvos, contra `22%` de `size 1` |
> | ⚠ **o preço em Defesa** | **é invenção nossa.** *E o Draw Steel não tem estatística de defesa — ataque é power roll contra faixa* |
>
> **⟹ `fila/MEDIDA-o-tamanho-no-draw-steel.md`.**

## ⚠ O que NÃO foi confirmado

**A mecânica de `size` do Draw Steel mora no `Draw Steel: Heroes` cap. 10, e ela não abriu.** *O
`steelcompendium.io` renderiza em JS, o repositório de dados só tem o bestiário, e a busca web caiu
duas vezes.*

**O que ficou confirmado do molde deles é só a FORMA da notação:** `1S` · `1M` · `1L` · `2`, e maiores.
*Fonte: `raw.githubusercontent.com/SteelCompendium/data-md/main/Bestiary/Monsters/Chapters/Monster Basics.md`*

*Também confirmado de lá: mounts **"of size 2 and smaller are typically meant to carry a single
rider"** — então o tamanho deles governa capacidade de carga, além de quadrados e alcance.*

> **A troca abaixo é construída com os câmbios do Projeto-M, não copiada do Draw Steel.**

---

## 1 · A conta que decide tudo: **alcance sozinho não paga Defesa**

*Usando o mesmo `f` que o `Artilheiro` fechou. O raio de engajamento numa rodada é
`deslocamento + alcance`, e alcance maior encolhe o `f` na proporção do raio.*

| alcance | raio | `f` | multiplica o dano |
|---|---|---|---|
| **`1,5 m`** — o padrão | `10,5 m` | `0,333` | `1,0000×` |
| `3 m` — o passo das `Armas Longas` | `12 m` | `0,292` | **`1,0417×`** |
| `4,5 m` | `13,5 m` | `0,259` | `1,0741×` |
| `6 m` | `15 m` | `0,233` | `1,1000×` |

**E o custo de Defesa, do câmbio que o `papel` já construiu:**

| | |
|---|---|
| `+1` passo de alcance | **ganha `4,2%`** |
| `−1` de Defesa | **custa `9,1%`** |

> ### ⚠ `1` ponto de Defesa vale `2,2×` um passo de alcance.
> **Então *"cada degrau de tamanho dá `+1,5 m` e tira `1` de Defesa"* seria péssimo negócio:**
> *o bicho perderia `2,2×` o que ganha, e um `Colossal` seria estritamente pior que um `Médio`.*
> **Ninguém escolheria.**

---

## 2 · O que fecha: o tamanho compra **ALVOS**, e o formato o sistema já tem

**Alcance sozinho é pequeno demais pra sustentar seis degraus. Um bicho grande também acerta mais
gente — o golpe dele pega quem estiver no alcance.**

*E o formato já está publicado: o `Estilhaço` (`Leve`) diz **"metade dos dados respinga em quem
estiver do lado"**.*

### ⚠ ~~A escada, com a Defesa resolvida pra FECHAR cada degrau~~ — SUBSTITUÍDA em 10/09

> **A troca inteira abaixo foi aposentada** — `fila/DECIDIDO-o-tamanho.md`. *A Defesa não é moeda de
> tamanho em sistema nenhum, e a escada de alvos não existe no campo.* **Fica como registro do
> raciocínio.**

| tamanho | alcance | o golpe pega | ganho | **Defesa** | produto |
|---|---|---|---|---|---|
| **`Médio`** | `1,5 m` | só o alvo | `1,0000×` | `20` *(`+0`)* | **`1,000×`** |
| **`Grande`** | `3 m` | o alvo **+ metade em `1`** | `1,2153×` | `18` *(`−2`)* | **`1,013×`** |
| **`Imenso`** | `4,5 m` | o alvo **+ metade em `2`** | `1,4321×` | `16` *(`−4`)* | **`1,023×`** |
| **`Colossal`** | `6 m` | o alvo **+ metade em `3`** | `1,6500×` | `13` *(`−7`)* | **`0,971×`** |

> **Os quatro fecham entre `0,97×` e `1,02×`.**
>
> **E a escada de Defesa acelera de propósito — `−2`, `−4`, `−7`.** *Não é arbitrário: `1/x` é
> convexo, então **cada ponto de Defesa a menos custa mais que o anterior**. A mesma não-linearidade
> que apareceu na tabela do papel.*

### E o lado pequeno sai da conta

**`Minúsculo`, `Pequeno` e `Médio` ficam IGUAIS em número.**

*No campo, tamanho não muda a chance de acertar: **D&D 5e, PF2e e Draw Steel não dão Defesa por ser
pequeno** — isso é herança do 3.x.* **A diferença entre eles é ficção:** onde cabem, o que alcançam,
se passam despercebidos.

> *Se o lado pequeno ganhasse Defesa, ele ganharia sem pagar nada — porque já está no piso do
> alcance. A conta mostrou isso: `Minúsculo` dava `1,25×` e `Pequeno` `1,11×`, os dois de graça.*

---

## 3 · O custo real desta saída, e ele é de sabor

> ### Um `Colossal` fica com Defesa `13`. O personagem acerta ele em `85%`.

> ⚠⚠ **E o `13` é INCONSTRUÍVEL** — medido em 10/09, `fila/MEDIDA-o-tamanho-exercitado.md`.
> *A fórmula é `10 + Destreza + proteção` e o atributo tem piso `0`, então a menor Defesa que se
> constrói no nv30 é `14`.* **O `Colossal` é inconstruível em `29` de `29` níveis, e o `13` acima é o
> MELHOR caso** — esta tabela fechou a troca com Defesa base `20`, que é o topo do nível.

**Ele vira um saco de pancada que bate em todo mundo ao mesmo tempo.** *Isso é exatamente o que um
Colossal deveria ser na ficção — e é uma decisão de mesa, não de conta.*

**Se isso incomodar, o degrau do `Colossal` pode cortar `2` vizinhos em vez de `3`**, e aí ele fecha
com `−4` de Defesa em vez de `−7`.

---

## 4 · E uma consequência de desenho que caiu sozinha

**`Colossal Emboscador` deixa de fazer sentido.** *Um bicho de `6 m` de alcance que precisa se
esconder pra ganhar vantagem é contradição de ficção — e a regra agora tem como dizer isso sem
inventar nada:* **o `Emboscador` não sobe de `Grande`.**

*É o mesmo tipo de trava que o `Guardião` e o `Apoio` já carregam — eles só se pagam quando o
encontro tem mais de um inimigo.*
