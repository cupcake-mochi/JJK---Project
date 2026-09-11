# Passada 3 — os seis blocos no molde do 5e

*10/09/2026 (noite). Log salvo conforme o trabalho anda. Se a sessão cair, o estado está aqui.*

**Estado (11/09, sessão 2): FECHADO.** Os três scripts rodam limpos (`gerar-as-seis.py`,
`gerar-tabelas.py`, `gerar-exemplo.py`). `conferir-voz.py`: 80 e 07 limpos; 50 e 60 só com os
títulos de antes, fora das minhas regiões (o `--estrito` sai 1 por eles). Guarda de número
explicada abaixo. `build.py` não foi rodado.

---

## Esquema do `seis-prontas.json`

> ⚠ **11/09/2026: o texto das seis mudou de dono.** O commit C do `Claude 2` copiou este JSON
> para as `PRONTAS` do `gerador-inimigo/dados.js`, campo a campo e sem diferença (o campo `acoes`
> se chama `acoes_nomeadas` lá). O `gerar-as-seis.py` passou a ler o `dados.js` pelo `node`, e o
> capítulo 8 saiu idêntico byte a byte. O JSON virou `seis-prontas.SUPERADO-11-09.json`. **Mexer
> no texto das seis agora é no `dados.js`** — este esquema continua valendo, com aquele nome de campo.

Um objeto por criatura, com a chave = nome (tem de casar com o §1 do DECIDIDO). **Só texto e
escolha; nenhum número de ficha.** Número entra por marcador, e o script enche.

| campo | tipo | o que é |
|---|---|---|
| `tamanho` | texto | `Minúsculo` … `Colossal`. Decide alcance e o vizinho do golpe (RASCUNHO-5) |
| `movimentos` | lista de texto | modos extras de deslocamento (`Escalada`, `Voo`…). Vazia na maioria |
| `linha` | texto | uma frase: o que é |
| `notas` | texto | um parágrafo: folclore, onde aparece, como luta |
| `corpos_na_mesa` | inteiro | quantas cópias do bloco vão à mesa. O script confere contra o DECIDIDO |
| `tracos` | lista de `{nome, texto}` | traços, no molde do 5e |
| `acoes_multiplas` | texto ou `null` | só em quem age mais de uma vez; chama os ataques pelo nome |
| `acoes` | lista de `{nome, texto}` | ataques e ações, na ordem do bloco |
| `intervencoes` | lista de `{nome, texto}` | exatamente três em `Desastre` para cima; vazia no resto |

**Marcadores** (o script morre em marcador desconhecido):

| marcador | sai de | exemplo impresso |
|---|---|---|
| `{acerto}` `{cd}` | TABELA, por marco; se a faixa cruza marco, o valor de cima vem entre parênteses | `` `+4` (`+6` no nível 10 a 12) `` |
| `{golpe}` | TABELA; em quem tem `Intervenção`, `dado(arred(dano/rod × 0,923) ÷ ações)` | `` `12 (2d4 + 7)` `` |
| `{alcance}` `{vizinho}` | tabela de tamanho do RASCUNHO-5 | `` `3 m` `` · `, e metade desse dano em um vizinho do alvo` |
| `{esfera}` `{cone}` `{retangulo}` | área natural por nível, RASCUNHO-5 | ``raio `3 m` `` · `` `7,5 m` `` · `` `4×3`, `6×2`, `7×2` ou `12×1` quadrados `` |
| `{deslocamento}` | RASCUNHO-5 | `` `9 m` `` |
| `{tecnica_dano}` `{tecnica_alcance}` | Fundamento: `⌊golpe ÷ 4,5⌋` d8, e o alcance do `Projétil` na Classe 1 | `` `18 (4d8)` `` · `` `18 m` `` |

**O que continua fora do JSON:** atributos e TR treinados (`arranjo`, `trs`) — o script lê do
`dados.js` pelo nome da ficha; faixa, categoria e corpos — do DECIDIDO.

**Travas do script:** Ações Múltiplas ⇔ age mais de uma vez; quem age 3 vezes tem ≥ 2 ataques com
nome e a Ações Múltiplas chama todos; `Intervenções` ⇔ categoria com Intervenção, e são 3; toda
condição escrita como ``fica `X` `` existe na peça 19; técnica abaixo do piso da Classe 1 mata; o
`dado()` portado tem de refazer os 58 golpes publicados de `Ameaça` e `Desastre`.

---

## Decisões até aqui (em aberto pro Mizuki onde está escrito)

### D1 · O golpe com `0,923` vira dado pela conta do `make.js`, e não pela média × 0,923

O `make.js` do Claude 2 calcula o golpe assim: `dado(arred(dano_por_rodada × fator) ÷ ações)`. O
porte fiel é esse pipeline inteiro, com o `0,923` entrando no fator — e não "média do golpe × 0,923",
que é o que o script antigo fazia para imprimir `5,1` e `12,0`.

**As duas contas dão dado diferente no Oni**, e por isso a escolha fica registrada:

| | Tsuchigumo (nv 2-4) | Oni (nv 5-8) |
|---|---|---|
| golpe cru da TABELA | `1d4 + 3` = 5,5 | `2d6 + 6` = 13,0 |
| antigo: média × 0,923 | `5,08` → `1d4 + 3` | `11,999` → **`1d10 + 6`** (11,5) |
| **novo: `make.js`** — `arred(dano/rod × 0,923) ÷ 3` | `arred(15,691)=16 ÷ 3 = 5,33` → `1d4 + 3` | `arred(35,997)=36 ÷ 3 = 12,0` → **`2d4 + 7`** (12,0) |

*(conta rodada no script; conferir na saída dele)*

### D2 · `Ações Múltiplas` sai dos Traços e vira a primeira entrada de Ações

Molde do `Ataques Múltiplos` (GUIA §2). Só em quem age mais de uma vez. Diz quais ataques e em que
combinação. **Pede mudança no 07 e no 50** — ver PEDIDOS.

### D3 · O segundo ataque dos dois `Desastre` é a área natural do capítulo 7

É o único jeito de ataque diferente que o livro declara de graça (*A área natural*: "A área é de
graça"). Alcance à distância **não** é de graça: é o que o `Artilheiro` compra
(`papel/A-TABELA-dos-seis-papeis.md` §2), e as seis não têm papel.

⚠ **PROPOSTA:** o livro não diz como a área natural resolve. Usei a regra de área do Fundamento
(Teste de Resistência contra a CD, golpe na falha, metade no sucesso). Ver PEDIDO pro cap. 70.

### D4 · Faixa que cruza marco imprime a linha de defesa por marco

Três fichas cruzam marco: Hitotsume e Oni (`nível 5` · `nível 6 a 8`) e Kitsune (`nível 9` ·
`nível 10 a 12`). Elas imprimem uma linha de Defesa/Acerto/CD/Refino por trecho. No texto do ataque,
`{acerto}` e `{cd}` imprimem o valor de baixo e, se mudar, o de cima entre parênteses: a Kitsune lê
`` `+4` (`+6` no nível 10 a 12) ``. **Isso corrige um erro do bloco antigo** (ver Achado 3).

### D6 · A média do golpe arredonda para baixo, como no 5e

Único caso de meio-ponto nas seis: a Tsuchigumo, `1d4 + 3` = 5,5 → imprime `5 (1d4 + 3)`. O alvo do
`make.js` para ela é `5,33`, então `5` casa com o 5e e com a conta.

### D7 · O cabeçalho continua com a célula `O golpe`

Ela repete o dano que já está nos ataques, mas o cap. 50 (fora da minha região) descreve a célula
em *As linhas de defesa*. Ficou; ver PEDIDO ao próximo passe.

### D8 · Tudo que a ficha diz de folclore

Betobeto (passos que seguem quem anda sozinho à noite; quem sai do caminho e pede que ele passe fica
em paz) · kamaitachi (trio de doninhas num redemoinho: derruba, corta, passa remédio) · tsuchigumo
(aranha gigante morta por Minamoto no Raikō) · hitotsume-kozō (menino careca de um olho, língua
comprida, só assusta) · kitsune (raposa que toma forma humana; kitsunebi) · oni (chifres, pele
vermelha ou azul, kanabō). Nada sobre a obra.

### D5 · Intervenção 1 é um ataque sem a metade no vizinho

`MEDIDA-a-intervencao.md` §12 fechou que a Intervenção 1 "bate — um pouco menos que uma ação
normal", e o `0,923` foi calculado com ela valendo `0,75` de uma ação. Um ataque de `Grande` sem a
metade no vizinho vale `1 ÷ 1,2153 = 0,82` de uma ação normal do mesmo bicho.

---

## Achados no caminho

1. **`Caído` não é condição do sistema.** A condição chama `Derrubado` (peça 19 §3.1). As duas
   Intervenções antigas usavam o nome errado.
2. **A Intervenção 2 antiga do Oni somava dano** ("o golpe passa a pegar dois vizinhos, até o fim
   da luta"). O capítulo 5 proíbe: a segunda e a terceira não somam dano.
3. **O bloco antigo imprimia a linha do nível de baixo para a faixa inteira.** Hitotsume e Oni
   saíam com Defesa `14` / Refino `1` no nível 6 a 8, e a TABELA dá `15` / `3`. A Kitsune saía com
   `+4` / CD `12` no nível 10 a 12, e a TABELA dá `+6` / `14`. O script antigo só conferia vida e
   golpe na faixa. Corrigido pela D4.
4. **TABELA × `make.js` divergem numa célula.** Catástrofe nv 2-4: alvo exato `5,00`; a TABELA
   publica `1d4 + 2` (o `round` do Python leva o `2,5` para o par) e o `make.js` dá `1d4 + 3`. O
   livro deixou de imprimir essa célula (a coluna da Catástrofe passou a trazer o golpe com o
   `0,923`, que dá `5` seco), mas a TABELA continua com ela. O `gerar-tabelas.py` lista o caso a
   cada rodada em vez de calar.
5. **O `make.js` não tem o `0,923` em lugar nenhum** (grep vazio). O `golpe()` dele recebe o fator
   da categoria, e a Intervenção não entra. Ver PEDIDOS.
6. **As frases vagas que o Mizuki citou moravam no `dados.js`** (`caracteristicas` e `notas`), e o
   bloco do `.docx` diz as mesmas. O JSON as substitui.

---

## As seis, antes → depois

| ficha | antes | depois |
|---|---|---|
| **Betobeto** | `Ações Múltiplas (1)`; "Golpe… O golpe é o orçamento inteiro dela" | traço *Passos no Escuro*; **Pisada** `4` Concussão |
| **Kamaitachi** | `Ações Múltiplas (1)`; "isso já é a categoria" | traço *Par* (ponha duas na mesa); **Foice** `4` Cortante |
| **Tsuchigumo** | `Ações Múltiplas (3)` com um golpe `5,1`; Intervenções com `Caído` e "perde o turno procurando" | Escalada `9 m`; *Escalada de Aranha*, *Andar na Teia*; Ações Múltiplas (3 Mordidas, ou Varrida + 2 Mordidas); **Mordida** `5 (1d4 + 3)` Perfurante + vizinho; **Varrida das Patas** Cone `7,5 m`, TR Físico CD `12`; Intervenções **Mordida** (sem vizinho) · **Teia** (terreno difícil) · **Subir** (escala `9 m` sem ataque de oportunidade) |
| **Hitotsume** | "O que assusta nela é aparecer…"; linha de defesa do nv 5 para 5-8 | traço *Mais Perto*; **Língua** `10 (2d4 + 5)` Concussão; defesa em duas linhas |
| **Kitsune** | "Técnica de `Classe 1`, escrita pelo mestre no orçamento de `4,2`"; `+4`/CD `12` para 9-12 | traço *Forma Humana*; **Mordida** `19 (2d8 + 10)`; **Fogo-de-Raposa** `18 (4d8)` Fogo, `18 m` (PROPOSTA); defesa em duas linhas, acerto `+4` (`+6` no 10 a 12) |
| **Oni** | `Ações Múltiplas (3)` com um golpe `12,0`; Intervenção 2 somava dano | traço *Faro*; Ações Múltiplas (3 Kanabō, ou Pancada + 2 Kanabō); **Kanabō** `12 (2d4 + 7)` Concussão + vizinho; **Pancada no Chão** Esfera raio `3 m`, TR Físico CD `12`; Intervenções **Kanabō** (sem vizinho) · **Arremesso** (jogado até `9 m`, `Derrubado`, sem dano) · **Parede Abaixo** (tira cobertura, terreno difícil) |

## Número de regra que mudou, e por quê

- **Golpe de quem carrega Intervenção** (D1): Tsuchigumo `5,1` → `5 (1d4 + 3)`; Oni `12,0` →
  `12 (2d4 + 7)`; Ubume `23,1` → `23 (2d10 + 12)`; na *Vida e golpe por faixa*, as colunas de
  Desastre, Catástrofe e Calamidade passam a sair com o fator, em dado.
- **Defesa/Acerto/CD/Refino por marco** (D4 / Achado 3): valores que a TABELA já dava e o bloco
  antigo omitia.
- **Técnica da Kitsune** `4d8`: PROPOSTA (P3).

**Guarda de número** (`guard_numeros.py .antes/X ../capitulos/X`):
- **80**: 34 diferenças, todas da reescrita — cada ataque imprime acerto, CD e alcance na própria
  linha (`+4`, `12`, `1,5`, `3`), a média antes do dado (`5`, `10`, `12`, `19`), dados novos
  (`1d4`, `2d4`, `4d8`), `5,1`/`12,0`/`4,2` somem, `7,5` (cone), `9` (deslocamento, escalada,
  arremesso), `7`/`6`/`12` (retângulo), linhas por marco (`+2`, `+6`, `15`, `16`, `3`), `18` (`4d8`
  e `18 m`). Extenso: "uma criatura" em cada ataque; "quatro/seis/três/duas" da abertura e do
  *Uso na campanha* reescritos. Nenhum número de regra além dos da lista acima.
- **50**: `1`/`2`/`3` da lista numerada das Intervenções e de "Passo 1"; `6` de "capítulo 6";
  extenso do exemplo de Ações Múltiplas ("três", "dois") e "metade do dano" no bloco em branco.
  Nenhum número de regra.
- **07**: três "uma" nas definições novas. Nenhum número de regra.
- **60**: 47 diferenças. As da *Vida e golpe por faixa* são as 21 células de `Desastre`,
  `Catástrofe` e `Calamidade`, que passam a sair com o `0,923` em dado (a Catástrofe nv 2-4 vira
  `5` seco: alvo `4,60`, abaixo do piso). As do exemplo são o Ubume: `23,1`/`25,0`/`2d12` somem;
  entram `23 (2d10 + 12)`, a Garra, o Choro (Esfera de raio `4,5 m`, CD `14`) e a Ações Múltiplas
  ("três", "dois"). A caixa do `0,923` perdeu o porquê e não mudou número.

---

## PROPOSTAS pro martelo do Mizuki

> ✅ **As cinco foram APROVADAS pelo Mizuki em 11/09/2026**, na sessão que executou a entrega no
> `Claude 2`. *Elas entram no `dados.js` no commit `C`.*

- **P1 (D3) · Área natural resolve como a do Fundamento:** TR contra a CD, golpe na falha, metade
  no sucesso. E a trava *"1 ação em área à vontade"* lida como "no máximo uma área por turno" — por
  isso as Ações Múltiplas dizem "Varrida + 2 Mordidas", e não "3 Varridas".
- **P2 (D5) · Intervenção 1 = ataque do bloco sem o vizinho** (`0,82` de uma ação de `Grande`).
  O cap. 50 diz só "um pouco mais fraco que numa ação normal", sem cravar o jeito.
- **P3 · Fogo-de-Raposa da Kitsune:** `Projétil` (Forma sem custo, `18 m` na Classe 1-5), `4`
  pontos em dado = `4d8` de Fogo; os `0,2` que sobram não compram nada. **Tensão:** o `Artilheiro`
  paga vida `× 0,857` pelo alcance, e aqui o alcance vem de graça pelo Fundamento. Se isso não
  valer, a saída é `Toque` (`1,5 m`, devolve `Média`) — conta não feita.
- **P4 · Os traços são inventados**, dentro do que o cap. 5 deixa (sentido, jeito de se mover,
  aparência, motivo do bando). O *Faro* do Oni tem efeito de luta (acha criatura ferida no mesmo
  cômodo) — conferir se ainda é "qualitativo".
- **P5 · Intervenções 2 e 3** aplicam `Derrubado`, terreno difícil e tiram cobertura sem custo,
  como as antigas faziam. O cap. 5 não diz se condição cabe nelas.

## PEDIDOS pro Claude 2 (para o `bloco-de-inimigo.docx` dizer o mesmo)

1. **`dados.js`:** `PRONTAS` recebe os campos do JSON (`tamanho`, `movimentos`, `linha`, `notas`,
   `corpos_na_mesa`, `tracos`, `acoes_multiplas`, `acoes`, `intervencoes`) e perde
   `caracteristicas`. `arranjo` e `trs` ficam com esse nome — o `gerar-as-seis.py` lê os dois por
   ele. As categorias e a faixa da Kitsune já estão no §4 do DECIDIDO.
2. **`make.js` · golpe:** em `Desastre` para cima, `golpe(dano, fator × 0,923, pes)`. Hoje o `0,923`
   não existe lá (Achado 5).
3. **`make.js` · marcadores:** encher os mesmos do JSON com as mesmas regras — média para baixo e
   dado entre parênteses; acerto/CD por marco; alcance e vizinho pelo tamanho; área natural pelo
   nível; `⌊golpe ÷ 4,5⌋d8` e o alcance do `Projétil` para a técnica.
4. **`make.js` · formato:** parar de imprimir `Ações Múltiplas (N)` como traço; imprimir só quando
   age mais de uma vez, como primeira entrada de Ações. Intervenções com preâmbulo e três opções
   numeradas com nome.
5. **Fora do Claude 2, para o dono da `TABELA.md`:** regenerar com meio-ponto para cima (Achado 4).

## PEDIDOS pro próximo passe do livro (capítulos que não são meus)

- **Cap. 60, *Orçamento de uma ação, por categoria*** (tabela estática, fora das minhas regiões):
  foi feita com média × `0,923`. Pela conta do `make.js`, três células andam `0,1` — Catástrofe
  nv 10 `4,5` → `4,6`, Catástrofe nv 15 `6,9` → `6,8`, Calamidade nv 20 `10,1` → `10,0` (conta
  rodada contra o `gerar-tabelas.py`). Melhor virar região gerada pelo mesmo script.
- **Cap. 70:** escrever como a área natural resolve (P1).
- **Cap. 50, *As linhas de defesa*:** decidir se a célula `O golpe` fica no cabeçalho (D7).
- **Cap. 50, *A linha de entradas nomeadas*:** dizer se `Ações Múltiplas` conta como entrada.
- **Cap. 50 e 60:** os títulos que o `conferir-voz.py` acusa (9 no 50, 13 no 60) estão fora das
  minhas regiões e continuam lá; o `--estrito` sai 1 por causa deles.
