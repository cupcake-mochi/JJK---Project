# Como rodar as contas deste bloco de novo

> ## ⚠ MUDOU em 11/09/2026 — os `.json` NÃO moram mais aqui
> **Eles moram em `04-fase-1/fila/`, uma casa só, e os scripts resolvem o caminho contra o próprio
> arquivo deles.** *Rode de onde quiser.*
>
> *Antes, este arquivo mandava `cp ../classificar-*.py .` e rodar aqui dentro — e os scripts abriam
> por nome nu, então escreviam a saída no diretório de quem chamava.* **Foi assim que os seis corpora
> acabaram em TRÊS casas:** a raiz do `Bestiario/`, a `fila/` e esta pasta. *As três eram `md5`
> idêntico, e as cópias foram apagadas.*

**O que sobra aqui é só o corpus do Draw Steel** — `ds.tar.gz` e o `data-md-main/` que ele gera. Seis
scripts da fila leem essa pasta por caminho absoluto.

| arquivo | o que é | de onde veio |
|---|---|---|
| `ds.tar.gz` | o repositório do Draw Steel inteiro | `github.com/SteelCompendium/data-md`, tarball de `main` |
| `data-md-main/` | o que o `tar` gera dele | — |

*O tarball fica porque é o recibo: ele prova que o `data-md-main/` não foi editado à mão.*

**Os outros corpora, em `04-fase-1/fila/`:**

| arquivo | o que é | de onde veio |
|---|---|---|
| `srd-2024.json` | as `331` criaturas do SRD 5.2 | `api.open5e.com/v2/creatures/?document__key=srd-2024` — por `puxar-srd-open5e.py` |
| `srd-2014.json` | as `325` criaturas do SRD 5.1 | idem, `document__key=srd-2014` |
| `pf2e-recarga.json` | as `677` criaturas do PF2e com *"again for 1d4 rounds"* | `elasticsearch.aonprd.com/aon/_search` — por `puxar-pf2e-aon.py` |
| `pf2e-tamanho.json` | os tamanhos do PF2e | `puxar-pf2e-tamanho.py` |
| `classificado-srd2024.json` · `ds-vas2.json` · `pf2e-habs2.json` | **derivados** — saem dos três `classificar-*.py` abaixo | — |

## A ordem

```bash
cd "04-fase-1/fila"
tar xzf dados-recarga-area/ds.tar.gz -C dados-recarga-area/   # só se o data-md-main/ sumir
python3 classificar-recarga-area.py      # D&D 5.2    -> 70 de 86 area
python3 classificar-va-drawsteel.py      # Draw Steel -> 119 de 156 pegam mais de um
python3 classificar-recarga-pf2e.py      # PF2e       -> 595 de 663 area
python3 somar-os-tres-sistemas.py        # 784 de 836 = 93,8%
```

> **Os dois primeiros ESTOURAM (`assert`) se sobrar qualquer item sem classificação, ou se o rótulo
> feito à mão discordar do detector por palavra-chave.** *Se eles rodam até o fim, o número fechou.*
>
> *O do PF2e **não** estoura — lá a classificação é aproximada de propósito, e o próprio arquivo
> `FONTE-a-recarga-e-alvo-unico.md` diz por quê (§4).*
