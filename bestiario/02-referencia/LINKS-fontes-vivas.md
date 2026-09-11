# Links de fonte que FUNCIONAM

*Achados pelo Mizuki em 10/09/2026. **Salvar isto economiza a busca toda vez.***

---

## Draw Steel (MCDM) — a base que este projeto mais usa

| o quê | URL | serve pra |
|---|---|---|
| **Regras de jogador** (`Heroes`) | `https://steelcompendium.io/v2/Read/heroes/` | economia de ação, condições, tamanho, tudo do lado do PC |
| **Regras de inimigo** (`Bestiary`) | `https://steelcompendium.io/v2/Bestiary/` | ⚠ isto é a BUSCA de blocos, não o texto de regra |
| **o livro de inimigo, pra LER** | `https://steelcompendium.io/v2/Read/bestiary/` | o texto de regra: villain actions, organização, papel |

**Os slugs do leitor `/v2/Read/<slug>/`:** `draw-steel-heroes` · `bestiary` · `beastheart` · `summoner`.

> ⚠ **As rotas `/v2/` são as que funcionam.** *As páginas
> `steelcompendium.io/compendium/main/...` renderizam em JS e voltam só o menu.*

**E o repositório de dados, em markdown cru:**

| | |
|---|---|
| árvore de arquivos | `https://api.github.com/repos/SteelCompendium/data-md/git/trees/main?recursive=1` |
| um arquivo | `https://raw.githubusercontent.com/SteelCompendium/data-md/main/<caminho>` |
| ⚠ **só tem o Bestiário** | as regras de `Heroes` **não** estão nesse repo |

---

## O que costuma dar erro, pra não perder tempo de novo

| fonte | o que acontece |
|---|---|
| `dnd4.fandom.com` | **HTTP 402** |
| `forum.rpg.net` · `forums.giantitp.com` | **HTTP 403** |
| `5thsrd.org/combat/...` | **HTTP 403** |
| `stawl.app` · `daggerheart.org` | **HTTP 403** |
| `drivethrurpg.com` | exige login |
| a página de magias do `br-2024` no D&D Beyond | corta na letra `D` — muito grande |
| o SRD 5.2.1 em PDF na `media.wizards.com` | **404** |

---

## As que funcionaram bem

| fonte | serve pra |
|---|---|
| `2e.aonprd.com` | **PF2e integral e gratuito** — condições, feitiços, `Building Creatures` |
| `dnd2024.wikidot.com` · `dnd5e.wikidot.com` | D&D 2024 e 2014, texto de magia e de classe |
| `api.open5e.com/v1/spells/<nome>/` | SRD 5.1 em JSON, rápido |
| `dndbeyond.com/sources/dnd/br-2024/rules-glossary` | o glossário oficial de 2024 |
| `dndbeyond.com/sources/dnd/br-2024/how-to-use-a-monster` | ação lendária, rótulos de frequência |
| `daggerheart.com` (o SRD em PDF) | Daggerheart oficial |
| `alphastream.org` | crítica de desenho com conta feita — foi de lá que veio a *"Lurker Fallacy"* |
| `enworld.org` | histórico longo; foi de lá que saiu o XP do 4e e a medição por papel do MM |
