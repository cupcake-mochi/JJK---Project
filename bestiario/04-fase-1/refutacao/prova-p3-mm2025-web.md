# Prova `p3-mm2025-web` — o bloco do Arquimago 2024/2025

*Verificação de fonte primária. 09/09/2026.*

## Veredito: **PARCIAL** — as quatro afirmações estão certas, mas duas delas por sorte

| # | afirmação do relatório | veredito |
|---|---|---|
| **a** | não tem espaço de magia; usa `À vontade` / `X/Dia` | **CONFIRMADO** — e agora com prova negativa contável |
| **b** | ataque à vontade entrega ~`108` por rodada (4 ataques) | **CONFIRMADO**, número exato |
| **c** | TODAS as magias à vontade dele causam ZERO dano | **CONFIRMADO para o Arquimago.** A generalização para a linha de 2025 é **REFUTADA** — o Lich tem `Fireball` e `Lightning Bolt` À VONTADE |
| **d** | `Lightning Bolt` custa uso limitado, dá `42`/alvo, compensa a partir de 3 alvos | **CONFIRMADO** — mas o relatório escolheu a magia mais favorável ao argumento. O `Cone of Cold` dele empata em **2** |

---

## 0. A fonte deixou de ser inconferível

**O bloco de 2025 está em documento oficial da Wizards, de graça e sob CC-BY-4.0:** o **System
Reference Document 5.2**. Ele traz o Arquimago, o Mago e o Lich **no formato novo**, e bate palavra
por palavra com o D&D Beyond.

> *"The System Reference Document 5.2 ("SRD 5.2") is provided to you free of charge by Wizards of
> the Coast LLC ("Wizards") under the terms of the Creative Commons Attribution 4.0 International
> License ("CC-BY-4.0")."*
> — SRD 5.2, p. 1 · `SRD52-en.txt:2-3`

- **URL oficial:** https://www.dndbeyond.com/srd
- **PDF:** https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.pdf (5,7 MB)
- **Texto extraído, grep-ável, agora local:**
  `/tmp/claude-1000/-media-mizuki-HD-Externo-II-Claude-Bestiario/56c72db1-7acc-4db0-bba3-77aa84a51702/scratchpad/livros/SRD52-en.txt`
- Páginas: **Lich `301`, Mago `302`, Arquimago `302`** (sumário em `SRD52-en.txt:113,140,143`)

**Confirmação independente, três fontes que não se copiam:**
- D&D Beyond (site do próprio editor): https://www.dndbeyond.com/monsters/5194902-archmage
- aidedd.org: https://www.aidedd.org/monster/archmage · `/monster/mage` · `/monster/lich`
- SRD 5.2 (documento oficial)

**As três dão o mesmo bloco.** Única divergência achada, e é lixo: aidedd e SRD dizem `XP 8.000`,
D&D Beyond diz `XP 8.400`. Não afeta nada aqui.

> **Corrija a linha de fontes do relatório.** Ela diz *"Manual dos Monstros 2025: blocos do Mago,
> Arquimago e Lich"* sem URL. A citação certa é **SRD 5.2, p. 301-302**, que é oficial, gratuita e
> conferível — e que já está extraída em `livros/SRD52-en.txt`.

---

## 1. (a) Espaço de magia: CONFIRMADO, com prova negativa contável

**Citação literal do bloco** (`SRD52-en.txt:19700-19726`, SRD 5.2 p. 302):

> *"**Multiattack.** The archmage makes four Arcane Burst attacks.*
> ***Arcane Burst.** Melee or Ranged Attack Roll: +9, reach 5 ft. or range 150 ft. Hit: 27 (4d10 + 5)
> Force damage.*
> ***Spellcasting.** The archmage casts one of the following spells, using Intelligence as the
> spellcasting ability (spell save DC 17):*
> ***At Will:** Detect Magic, Detect Thoughts, Disguise Self, Invisibility, Light, Mage Armor
> (included in AC), Mage Hand, Prestidigitation*
> ***2/Day Each:** Fly, Lightning Bolt (level 7 version)*
> ***1/Day Each:** Cone of Cold (level 9 version), Mind Blank (cast before combat), Scrying, Teleport"*

Cabeçalho (`SRD52-en.txt:19740-19752`): **`AC 17` · `HP 170 (31d8 + 31)` · `CR 12`**, Bônus
`Misty Step (3/Day)`, Reação `Protective Magic (3/Day)`.

**A prova negativa, contada no arquivo:**

```
"spell slot" nos capítulos do jogador (linhas < 16000):  365 ocorrências
"spell slot" na seção de monstros   (linhas > 16000):      0 ocorrências
```

> **A expressão `spell slot` aparece `365` vezes no SRD 5.2 e NENHUMA delas dentro de um bloco de
> monstro.** Não é "quase não usa". É zero.

E o eixo do jogador continua intacto — **os espaços não foram abolidos, foram tirados só do
monstro.** É exatamente a assimetria que o relatório está medindo.

### O contraste com 2014, agora conferido nos livros locais

`MM2014-pt.txt:21253-21269` (Arquimago 2014):

> *"Conjuração. O arquimago é um conjurador de 18° nível. (...) 1° nível (4 espaços) (...) 2° nível
> (3 espaços) (...) 3° nível (3 espaços) (...) 4° nível (3 espaços) (...) 5° nível (3 espaços) (...)
> 6° nível (1 espaços) (...) 7° nível (1 espaços) (...) 8° nível (1 espaços) (...) 9° nível (1 espaços)"*

`4+3+3+3+3+1+1+1+1 = 20`. **Os `20` espaços do relatório: CONFIRMADO em fonte local.**
E a adaga (`MM2014-pt.txt:21277-21279`): *"Acerto: 4 (1d4 + 2) de dano perfurante."* — os `4` de dano
do relatório: CONFIRMADO.

**Achado extra que aperta o argumento:** três dos `20` espaços têm asterisco —

> *"*O arquimago conjura essas magias sobre si antes do combate."* — `MM2014-pt.txt:21273`

São `armadura arcana`, `pele de pedra` e `limpar a mente`. **O próprio bloco de 2014 já gastava
`3` dos `20` fora da luta**, porque dentro da luta não caberia. O `85%` nunca gasto do relatório é
uma conta certa (`3 ÷ 20 = 15%` gasto), e o bloco de 2014 admitia o problema por escrito.

**E o formato de 2025 manteve a gambiarra:** `Mind Blank (cast before combat)`. Dos `8` usos
limitados do Arquimago, **um é declarado como pré-luta**. Sobram `7` para a luta.

**Contagem de "cargas" nos três blocos, verificada:**

| bloco | 2/Dia | 1/Dia | usos limitados de magia | + Misty Step | + Protective Magic | total |
|---|---|---|---|---|---|---|
| Mago `CR 6` | 2 magias = `4` | 2 magias = `2` | **`6`** | `3` | `3` | `12` |
| Arquimago `CR 12` | 2 magias = `4` | 4 magias = `4` | **`8`** (7 em luta) | `3` | `3` | `14` |
| Lich `CR 21` | 3 magias = `6` | 4 magias = `4` | **`10`** | — | ilimitado | — |

Bate com o `LEVANTAMENTO-pe.md` linhas 986, 995 e 1004. **Nenhum erro de contagem.**

---

## 2. (b) Os `108` de dano: CONFIRMADO no número, com uma ressalva de método

`4 × 27 = 108`. E o `27` é o valor impresso: `4d10+5` → `4 × 5,5 + 5 = 27,0`. **Exato, sem
arredondamento.**

**Ressalva:** `108` é dano bruto supondo que os quatro ataques acertam. Isso está *certo* pelo método
do DMG 2014 que o relatório usa (o passo do "damage output" não desconta acerto), e o `42` do
`Lightning Bolt` também não desconta resistência — **então a comparação é internamente consistente.**
Mas a assimetria de risco não é: ataque que erra dá `0`, magia com resistência bem-sucedida ainda dá
metade.

Descontando (AC 17, `+9` acerta com 8+ = `65%`; CD 17 contra save `+4` falha `60%`, fator `0,80`):

| | bruto | esperado |
|---|---|---|
| Multiattack (4 ataques) | `108` | **`70,2`** |
| `Lightning Bolt` por alvo | `42` | **`33,6`** |
| `Cone of Cold` por alvo | `54` | **`43,2`** |

> **A conclusão do relatório sobrevive aos dois métodos.** Mas veja o item (d) — a margem é menor do
> que ele diz.

**De passagem, o salto de 2014 para 2025 no Arquimago:** vida `99 → 170` (`1,72×`), dano por rodada
`4 → 108` (**`27×`**). *O que a WotC fez não foi tirar o poço: foi mudar de lugar todo o dano do
monstro, do recurso para a linha gratuita.* Isso é o argumento central do relatório, e o número é
brutal.

---

## 3. (c) "Todas as magias à vontade causam zero dano" — CONFIRMADO no Arquimago, REFUTADO como regra da linha

**No Arquimago: verdade, e são `8` mesmo.** Detect Magic, Detect Thoughts, Disguise Self,
Invisibility, Light, Mage Armor, Mage Hand, Prestidigitation. **Nenhuma das oito causa dano.**
No Mago (`SRD52-en.txt:19725-19726`) a mesma coisa, com `5`: Detect Magic, Light, Mage Armor, Mage
Hand, Prestidigitation.

**Mas no Lich `CR 21` a regra desaba** (`SRD52-en.txt:19648-19657`, SRD 5.2 p. 301):

> *"**At Will:** Detect Magic, Detect Thoughts, Dispel Magic, **Fireball (level 5 version)**,
> Invisibility, **Lightning Bolt (level 5 version)**, Mage Hand, Prestidigitation*
> ***2/Day Each:** Animate Dead, Dimension Door, Plane Shift*
> ***1/Day Each:** Chain Lightning, Finger of Death, Power Word Kill, Scrying"*

`Fireball` nível 5 = `10d6` = **`35` de dano em área, À VONTADE, ilimitado, de graça.**

E não são só esses dois blocos — os dragões de 2025 também têm dano à vontade: `Acid Arrow`,
`Scorching Ray`, `Shatter`, `Mind Spike` (`SRD52-en.txt:16953, 17272, 19011`).

> **Correção obrigatória no relatório.** A frase da tabela do §1 — *"o Arquimago 2025 tem `8` magias
> à vontade e todas causam zero dano"* — está **certa**. Mas a conclusão do §6 —
> *"A camada paga não é maior contra um alvo. Ela é mais larga"* — é generalizada de um bloco só, e o
> bloco do topo da linha (`CR 21`) **entrega a largura de graça**.

### O Lich em números, e ele é um caso melhor pro seu argumento, não pior

| linha do Lich | custo | dano | contra a rodada grátis (`93`) |
|---|---|---|---|
| Multiattack `3 × Eldritch Burst 31` | **grátis** | `93` | `1,00×` |
| `Fireball`/`Lightning Bolt` nv 5, `35`/alvo | **grátis, à vontade** | 3 alvos = `105` | **`1,13×`** |
| Ação Lendária `Disrupt Life` `9d6` em Emanação de 6 m | **grátis, recarrega toda rodada** | `31,5` em todos | — |
| `1/Dia` `Chain Lightning` `10d8` = `45`/alvo, 4 alvos | **pago** | `180` | `1,94×` |
| `1/Dia` `Finger of Death` `7d8+30` | **pago** | `61,5` num alvo | **`0,66×`** |
| `1/Dia` `Power Word Kill` | **pago** | zero dano, mata ≤ 100 PV | — |

> **O `Finger of Death`, magia de `1/Dia` do monstro de `CR 21`, entrega `61,5` — MENOS que os `93`
> que ele faz de graça só batendo.** Gastar o recurso mais escasso do bloco num alvo único é um
> prejuízo medido de `34%`.

**E o `Chain Lightning` a `1,94×` a rodada grátis cai quase exatamente na razão do Pathfinder 2e**
(`1,95×` no nv 10, `2,0×` estabilizado). *Duas editoras que não se falam chegaram no mesmo `2,0×`
para uso limitado.* **Só que o D&D entrega esse `2,0×` como `4` alvos a `0,48×` cada, e não como um
alvo levando o dobro.** Isso é a sua tese do §6 provada por um segundo caminho — e é a munição contra
o Modelo B que faltava.

---

## 4. (d) O `Lightning Bolt` e os três alvos: CONFIRMADO, mas o relatório pegou a magia conveniente

`Lightning Bolt` nível 7 = `12d6` = `42,0`. **Confirmado.** (Base nível 3 = `8d6`, `+1d6` por nível
acima → nível 7 = `12d6`.)

**E ele custa a AÇÃO INTEIRA, não um ataque.** Isso importa e eu confirmei no texto de regra:

> *"On your turn, you can take one action."* — `SRD52-en.txt:11258`

`Multiattack` e `Spellcasting` são as duas na seção `Actions` do bloco, e o `Multiattack` do
Arquimago é seco: *"The archmage makes four Arcane Burst attacks."* **Sem cláusula de troca.**
Conjurar custa os `108`.

| | bruto | vs `108` | esperado | vs `70,2` |
|---|---|---|---|---|
| `Lightning Bolt` 1 alvo | `42` | `0,39×` | `33,6` | `0,48×` |
| `Lightning Bolt` 2 alvos | `84` | `0,78×` | `67,2` | **`0,96×`** |
| `Lightning Bolt` 3 alvos | `126` | `1,17×` | `100,8` | `1,44×` |
| **`Cone of Cold` 1 alvo** | `54` | `0,50×` | `43,2` | `0,62×` |
| **`Cone of Cold` 2 alvos** | `108` | **`1,00×` — empate exato** | `86,4` | **`1,23×`** |
| `Cone of Cold` 3 alvos | `162` | `1,50×` | `129,6` | `1,85×` |

**Break-even bruto: `108 ÷ 42 = 2,57` alvos → precisa de `3`.** A afirmação (d) está certa.

> **Mas:** o relatório citou o `Lightning Bolt` (`2/Dia`, o `42`) e não o `Cone of Cold` (`1/Dia`,
> nível 9, `54`), que é **a maior magia do bloco** e que **empata em exatamente `2` alvos** — e ganha
> em 2 alvos assim que você desconta acerto e resistência (`86,4` contra `70,2`).
> **A camada paga do Arquimago vira lucro entre `2` e `3` alvos, não a partir de `3`.**

E no **Mago `CR 6`** o limiar é mais baixo ainda: rodada grátis `3 × 16 = 48`; `Fireball` nível 4 =
`9d6` = `31,5`. **Break-even `1,57` → `2` alvos**, e a `2` alvos já é `1,27×`.

> **Não muda a recomendação, muda a frase.** O padrão medido nos três blocos é: **a camada paga
> empata em `2` alvos e lucra em `3`.** *É mais fraco do que "compensa a partir de três" faz parecer
> — e ainda assim é a favor de largura, porque em alvo único ela vale `0,39×` a `0,66×`.*

---

## 5. O achado que o relatório não tem, e que é presente pro Modelo A

**O formato de 2025 tem uma TERCEIRA marcha que o levantamento não registrou** — e ela é literalmente
o Modelo A do relatório ("o feitiço troca UMA ação normal"):

> *"**Multiattack.** The dragon makes three Rend attacks. **It can replace one attack with a use of
> Spellcasting to cast** Acid Arrow (level 3 version)."* — `SRD52-en.txt:16931-16934`

**Ela aparece `9` vezes no SRD 5.2**, e eu conferi as nove uma por uma
(`SRD52-en.txt:16933, 17003, 17104, 17172, 17690, 19001, 20647, 20713` — dragões, e um gigante):

| linha | magia trocada por 1 ataque | ela é...? |
|---|---|---|
| 16933 | `Acid Arrow` (nv 3) | **À vontade** |
| 17003 | `Acid Arrow` (nv 4) | **À vontade** |
| 17104 | `Shatter` | **À vontade** |
| 17172 | `Shatter` (nv 3) | **À vontade** |
| 17690 | `Fog Cloud` | **À vontade** |
| 19001 | `Mind Spike` (nv 3) | **À vontade** |
| 19002 | `Mind Spike` (nv 5) | **À vontade** |
| 20647 | `Scorching Ray` | **À vontade** |
| 20713 | `Scorching Ray` (nv 3) | **À vontade** |

> ### `9` de `9`. **A troca de UM ataque por magia só existe para magia À VONTADE. Nenhuma magia de
> `X/Dia` em nenhum bloco do SRD 5.2 pode ser comprada com um ataque — ela sempre custa a ação
> inteira.**

**A regra de design implícita, e ela é dura:**
- camada **grátis** → pode ser comprada por **1 ação de ataque** (a troca);
- camada **paga** → custa a **rodada inteira** de ataques.

### Por que isso é um problema pro Modelo A do relatório

O §4-A precifica o feitiço do inimigo como **valendo o dobro de UMA ação** de um monstro de 3 a 6
ações, e conclui que a média de 3 rodadas dilui o custo (`+11,1%` no `Desastre`). **Mas o D&D 2025
nunca faz isso com recurso pago.** Um `Desastre` que troca `1` das `3` ações por um feitiço de `146`
é *mais generoso* que qualquer bloco de 2025: lá, conjurar o grande custa as três.

**Traduzido pro Projeto-M, o precedente medido é:**

| | o que o 2025 faz | o que o relatório propõe |
|---|---|---|
| feitiço **grátis** (Classe 0) | pode substituir **1** das ações | — |
| feitiço **pago** (`3 × Classe` de PE) | custa **todas** as ações da rodada | custa **1** ação |

> **Isso não derruba a recomendação de `PE = 9 × Classe`.** Derruba a *conta de diluição* do Modelo A,
> que é o que o relatório chama de "a espinha da recomendação". Se o feitiço pago custar a rodada
> inteira do `Desastre` (as `3` ações), o orçamento dele é `219`, não `146` — **e aí o teto de `219`
> em `3` alvos a `73` cada, que o §6 já recomenda, deixa de ser uma escolha de gosto e passa a ser a
> conversão exata do preço.** *O caminho da largura fica ainda mais barato do que o relatório diz.*

---

## 6. Erros achados, com o valor certo

| onde | o relatório diz | o certo |
|---|---|---|
| §1, tabela | *"o Arquimago 2025 tem 8 magias à vontade e todas causam zero dano"* | ✅ certo — mas vale **só pro Arquimago**. O Lich tem `Fireball` e `Lightning Bolt` **à vontade** |
| §6 | *"`4` ataques à vontade = `108` de dano por rodada, de graça"* | ✅ `4 × 27 = 108`, exato. Ressalva: bruto, sem desconto de acerto (esperado `70,2`) |
| §6 | *"o `Lightning Bolt` que custa carga dá `42` por alvo e só compensa a partir de **três** alvos"* | ✅ `12d6 = 42` e break-even `2,57`. **Mas o `Cone of Cold` (nv 9, `1/Dia`, `54`) empata em `2`.** A frase certa: **empata em `2`, lucra em `3`** |
| Fontes | *"Manual dos Monstros 2025: blocos do Mago, Arquimago e Lich"*, sem URL | **SRD 5.2, p. 301-302** — oficial, CC-BY, https://www.dndbeyond.com/srd. Extraído em `livros/SRD52-en.txt` |
| §4-A | o feitiço pago troca **1** ação do monstro | **`0` de `9`** blocos do SRD 5.2 fazem isso com magia paga. A troca-por-1-ataque é exclusiva da camada **à vontade** |

**Nenhum número do relatório está aritmeticamente errado.** O que está errado é o alcance de duas
frases e a ausência de uma URL conferível.

---

## 7. Onde eu bati na parede

- **`kassoon.com`, `dnd-wiki.org` e o fórum `giantitp` devolveram 403.** Não precisei deles — o SRD
  oficial cobre tudo.
- **A definição de regra de `At Will` e `X/Day Each` eu NÃO achei em texto oficial.** O SRD 5.2 usa as
  notações nos blocos mas não as define; a página livre *"How to Use a Monster"*
  (https://www.dndbeyond.com/sources/dnd/br-2024/how-to-use-a-monster) define Ação Lendária mas **não**
  define as notações de frequência. **A definição formal fica NÃO ACHADA.** O que eu tenho é melhor
  que definição, para o efeito prático: `0` ocorrências de `spell slot` em bloco de monstro, e as
  notações usadas em centenas de blocos.
- **Não achei texto de designer da WotC explicando POR QUE tiraram os espaços.** Confirma o buraco nº 1
  do `LEVANTAMENTO-pe.md:1128`.
- O `Lightning Bolt` nível 7 = `12d6` é **derivado** da regra de escala da magia (base nv 3 = `8d6`,
  `+1d6`/nível), não impresso no bloco. Mesma coisa pro `Cone of Cold` nível 9 = `12d8` e pro
  `Fireball` nível 5 = `10d6`. A aritmética é minha, a regra de escala é do PHB.

## Contas (todas rodadas em `python3`)

```
Arcane Burst 4d10+5 = 4*5,5+5 = 27,0        Multiattack 4x = 108,0
Lightning Bolt nv7 = 12d6 = 12*3,5 = 42,0  break-even 108/42 = 2,57 alvos
Cone of Cold  nv9 = 12d8 = 12*4,5 = 54,0   break-even 108/54 = 2,00 alvos
Mago:  3d8+3 = 16,5 (bloco 16); 3x = 48    Fireball nv4 = 9d6 = 31,5; break-even 48/31,5 = 1,57
Lich:  4d12+5 = 31,0; 3x = 93,0            Fireball nv5 a vontade = 10d6 = 35,0; break-even 2,66
       Chain Lightning 10d8 = 45,0/alvo x4 = 180,0 = 1,94x de 93
       Finger of Death 7d8+30 = 61,5 = 0,66x de 93
       Disrupt Life 9d6 = 31,5, gratis, recarrega toda rodada
2014:  espacos 4+3+3+3+3+1+1+1+1 = 20; 3 usados = 15% gasto, 85% nunca gasto
       3 dos 20 sao pre-combate (asterisco) -> 17 em luta
       Adaga 1d4+2 = 4,5 (bloco 4)
Salto 2014->2025: PV 99->170 = 1,72x ; dano/rodada 4->108 = 27x
Desconto (AC 17 vs +9 = 65%; CD 17 vs save +4 = fator 0,80):
       Multiattack esperado 70,2 ; LB 33,6/alvo (2 alvos 67,2) ; CoC 43,2/alvo (2 alvos 86,4)
"spell slot" no SRD 5.2: 365 nos capitulos do jogador, 0 em bloco de monstro
"replace one attack with a use of Spellcasting": 9 ocorrencias, 9/9 apontam magia A VONTADE
```

## Fontes

- **SRD 5.2** (Wizards of the Coast, CC-BY-4.0), p. 301-302 — https://www.dndbeyond.com/srd ·
  PDF: https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.pdf ·
  texto local: `scratchpad/livros/SRD52-en.txt` (Lich `19625-19690`, Mago `19713-19739`,
  Arquimago `19695-19752`, ação por turno `11258`, cláusula de troca `16933 17003 17104 17172 17690
  19001 20647 20713`)
- D&D Beyond, Arquimago — https://www.dndbeyond.com/monsters/5194902-archmage
- aidedd — https://www.aidedd.org/monster/archmage · https://www.aidedd.org/monster/mage ·
  https://www.aidedd.org/monster/lich
- D&D 2024 Basic Rules, *How to Use a Monster* (só a Ação Lendária) —
  https://www.dndbeyond.com/sources/dnd/br-2024/how-to-use-a-monster
- Manual dos Monstros 2014 (PT), Arquimago — `livros/MM2014-pt.txt:21253-21279`
