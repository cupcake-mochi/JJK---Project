# Fase 0 — as decisões, em ordem de tomada

*Todas do Mizuki, em 08/09/2026, salvo onde dito.*

## 1. O que o Bestiário é

**Duas coisas: o catálogo e a máquina. E as duas se encontram no BLOCO.**

O catálogo é uma pilha de blocos preenchidos; a máquina é como preencher um em branco.

## 2. O formato

**Stat block no molde do D&D.** Uma página de duas colunas, no máximo duas. Legível num relance, num segundo monitor. Bloco fixo em cima, tempero embaixo.

*Referência que ele mandou: o Aboleth do Manual dos Monstros de 2024.*

## 3. Os números do sistema ficam

**O problema é o esqueleto, não os valores.** Descartadas: inflar atributo de inimigo, e subir a Defesa do chefe.

> **O número base sai da tabela. O desvio sai de uma característica que tem CAUSA na ficção** — igual ao inimigo de D&D que tem `20` de CA porque veste armadura de placas.

## 4. `Intervenção`

A ação fora do turno. **Três por luta, cada uma uma vez, no máximo uma por rodada.** Não absorve a Reação: *Reação é resposta, Intervenção é iniciativa.*

*Documento próprio em `03-bloco/a-intervencao.md`.*

## 5. Fase de chefe

**Opcional, e vai pro fim do livro como adicional.** Não é peça central.

## 6. Tamanho

**Seis degraus, no padrão que ninguém erra:** `Minúsculo` · `Pequeno` · `Médio` · `Grande` · `Imenso` · `Colossal`.

> ⚠ **Isso é mecânica NOVA.** Não existe categoria de tamanho em lugar nenhum do sistema hoje. Falta decidir se ela é só sabor no cabeçalho ou se carrega regra.

## 7. Tipo

**Cinco, fechados:** `maldição` · `feiticeiro` · `restringido` · `civil` · `sem técnica`.

*E o tipo já carrega mecânica sem precisar de regra nova: a ferramenta amaldiçoada fere maldição e não fere humano.*

## 8. A categoria — cinco degraus, e o nome diz a GRAVIDADE

**A regra que conserta o problema antigo:** o nome diz **quão ruim é**; a tabela diz **quantas pessoas precisa**. O leitor nunca converte.

*O defeito que isso mata, nas palavras dele:* **"Dupla? são dois inimigos? Aaaa são para dois players — pra q esse processo todo? n é bom pro game design da coisa."**

| | categoria | o que é |
|---|---|---|
| 1 | **`Capanga`** | morre rápido, vem em grupo |
| 2 | **`Ameaça`** | um feiticeiro resolve |
| 3 | **`Desastre`** | o grupo resolve — a linha do manual sem tocar em nada |
| 4 | **`Catástrofe`** | exige mais que o grupo |
| 5 | **`Calamidade`** | o topo |

**Por que cinco, e não quatro ou seis** — pesquisa de campo:

| sistema | postos |
|---|---|
| D&D 4e | `4` — minion, standard, elite, solo |
| Lancer | `5` — Grunt, Elite, Veteran, Commander, Ultra |
| Draw Steel | `6` |
| 13th Age | ~`4` |
| Pathfinder 2e | `0` — só nível |

> **A comunidade do 4e reclamava de um buraco entre o `minion` e o `standard`, e propôs um posto novo pra preencher.** A `Ameaça` é exatamente esse posto. Cinco é o 4e com o buraco tapado, e um a menos que o Draw Steel — que é onde a reclamação de excesso começa.

**E `Capanga` virar degrau próprio mata uma seção inteira de complexidade:** o câmbio de "um chefe vale quatro capangas", a derivação, o validador em cima dela, e a frase contraditória que só funcionava numa das categorias. Ele passa a ser uma linha da tabela.

## 9. Sem eixo de papel

**Decisão dele:** não vai ter um segundo rótulo (bruto, artilharia, controlador) junto da categoria.

*A reclamação de excesso no Draw Steel é documentada — um mestre descreveu o combate como "there's just too much going on", e uma resenha diz que o sistema "agrava o problema do mestre em vez de simplificar".* **Sendo preciso: a reclamação mira a carga total — o Malice rastreado toda rodada, traços de facção, sistemas em cima de sistemas — e não os papéis isoladamente.**

**Mas a decisão se sustenta por outro motivo:** o papel já vai estar no bloco como habilidade em vez de rótulo. Um inimigo que empurra e agarra é um bruto sem a palavra escrita.

*O que se abre mão: o atalho de montagem. O mestre não vai poder pedir "uma artilharia e dois defensores" — ele vai ler as habilidades.*

## 10. O escopo do catálogo — pirâmide, em ondas

***Decisão do Mizuki:*** *"Pirâmide parece a melhor forma mesmo, depois a gente enche mais."*

**Pesado embaixo, fino em cima**, que é o que o D&D faz — e o motivo é medido, não estilo:

| faixa | blocos no Manual dos Monstros | fatia | blocos por degrau de ND |
|---|---|---|---|
| ND 0 a 1 | `129` | `36%` | **`32,2`** |
| ND 2 a 4 | `89` | `25%` | **`29,7`** |
| ND 5 a 10 | `78` | `22%` | `13,0` |
| ND 11 a 16 | `33` | `9%` | `5,5` |
| ND 17 a 30 | `25` | `7%` | **`1,8`** |

**Sessenta e um por cento do livro é ND 0 a 4.** Dezoito monstros de faixa baixa para cada um de faixa alta. *É onde a maioria das mesas vive, e é onde o mestre precisa de variedade para não repetir.*

> **E o catálogo é a única parte do projeto que serve incompleta.** A máquina precisa estar inteira ou não monta nada; o catálogo com dez inimigos já é útil, e cresce para sempre. **Por isso ele sai em ONDAS, e o número final não precisa ser decidido agora.**

## 11. Onde isso mora — híbrido

**A máquina vira peça no repositório** (argumento, números, validador). **O catálogo vira livro gerado.**

*É a estrutura que o repositório já tem de pé — peça 26 mais o `bloco-de-inimigo.docx` gerado pelo `gerador-inimigo/`, com validador comparando os dois.* **O que muda é que o `.docx` deixa de ser folha de construção e passa a ser o bestiário.**

**O motivo é o formato:** stat block precisa de diagramação, e diagramação não mora em markdown. O argumento e os números moram; a página não.

---

# FASE 0 — FECHADA em 08/09/2026

**O que morre junto:** as categorias `Ronda`, `Dupla`, `Alcateia`; o câmbio de "um chefe vale quatro capangas"; e a sub-categoria (`sozinho`, `com um apoio`, `com dois`, `bando`).

**O que passa para a Fase 1:** a tabela que preenche o bloco — vida, dano, Defesa, acerto e CD por nível e por categoria. E as duas pendências que continuam abertas: **o PE do inimigo** (decidido na v0.220 do repositório, nunca aplicado) e **se `tamanho` carrega regra ou é só sabor**.
