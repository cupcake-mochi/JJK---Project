# A aplicação da fase 2 — a lista de trabalho

*Aberta em 28/09/2026, quando o Mizuki liberou ("Gostei, otimas ideias, podemos seguir e aplicar"). O modelo está nos §3 a §11 de `decisoes-fase-2.md`; o mapa do que quebra é o §2 e o §3 da `pesquisa/RESULTADO-auditoria-interna.md`. Os validadores leem a peça 26 célula a célula, então o núcleo entra junto numa versão só.*

## O modelo, numa tela

| linha | a regra nova | antes |
|---|---|---|
| categoria | a dificuldade da luta: `Capanga · Ameaça · Desastre · Catástrofe · Calamidade` | quantas pessoas ele exige |
| N | quantas pessoas do nível a ficha enfrenta, de `×1` a `×6` | o fator × 4 |
| rodadas | `2 · 2,5 · 3 · 4 · 5` | 3 em toda categoria |
| vida | `rodadas × N × a saída de um personagem` (a saída do grupo do manual ÷ 4), meio para baixo | a linha × o fator |
| golpe | `a pressão do degrau × o golpe-base` (o dano do chefe do manual ÷ 4); a pressão é o orçamento do PF2e ÷ a duração | a rodada ÷ as ações |
| ações | `N` | `1 · 1 · 3 · 5 · 6` |
| Capanga `×N` | `2N` corpos de um golpe, meio golpe-base | 8 corpos, golpe da Ameaça |
| recurso e traço | se paga na vida (`vida ÷ o multiplicador`); o golpe não se move | multiplica o fator |
| `×1` e `×2` | TR no começo do turno contra condição que tira ação: com a maestria no `×1`, com desvantagem no `×2` | o piso de 3 ações |
| atributo | a ficha é a tabela por nível; o desvio da tabela se paga na vida (Defesa `10%` por ponto, acerto e CD `8,7%`) | a ficha de personagem sem Caminho |

## O que muda, e em que ordem

1. [x] `bestiario/09-fase-2/gerar-grade.py` — toda tabela da peça nova sai de conta, nenhuma à mão.
2. [x] peça 26 — reescrita; a de antes vai para `sistema/99-arquivo/`.
3. [x] `conferir-bestiario.py` — reescrito contra a peça nova.
4. [x] peça 19 §2.2 — ela aponta para a regra do `×1` e do `×2`; a régua de três ações e a checagem 12 do `conferir-dano.py` ficam, porque a conta do piso é o que justifica a regra. O chefe de referência dela (`219` em três ações, e o capanga de `73` do `DESENHO-trilhas`) foi para o item 19 da fila.
5. [x] os outros leitores da peça 26 (mexeram o `conferir-alma` e o `conferir-invocacoes`; os outros passaram sem mudança): `conferir-acao`, `-alma` (13c), `-aptidoes`, `-atributos` (a banda), `-invocacoes` (12b), `-bloquear`, `-expansao` (bloco 10), `-dano` (a linha do `Calado`).
6. [x] o manual (`partF.js`, a seção `Inimigos`): a coluna do capanga, os oito capangas e as três ações; `.docx` e `.pdf` refeitos.
7. [x] o gerador de inimigo (a conta foi para o `conta.js`) (`dados.js`, `make.js`) e o `conferir-ficha.py` 7a-7c; o `.docx` refeito.
8. [x] o livro de inimigos: os `gerar-*.py` (a `TABELA.md` fica, lida só para as derivadas); os capítulos 07, 50, 60, 70, 80 e 90 (sai a frase "exige oito"); as seis prontas; os PDFs.
9. [x] a peça 15 (a morte do shikigami pelo golpe) e a peça 1 (a banda do golpe de chefe). A peça 24 e o livro do jogador continuam certos; o Evocador da peça 1 foi para o item 19.
10. [ ] o Sukuna (`05-sukuna/`), refeito na grade — item 18 da fila.
11. [ ] as onze divergências da auditoria (§4.4) — item 19 da fila. *Quatro caíram com a v0.282 (1, 2, 5 e 6) e quatro fecharam na v0.284 (3, 4, 8 e 10); a 9 (resistência pontual) fechou na v0.286 e a 7 (Evocador na média) fechou na v0.285, e a 11 (o Sukuna) vai com o item 18.*
12. [x] ESTADO, CHANGELOG, arnês, emulação, mensagem — a v0.282.
