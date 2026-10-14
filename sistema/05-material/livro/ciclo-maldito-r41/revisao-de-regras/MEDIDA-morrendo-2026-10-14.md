# O Morrendo do R50, conferido — 14/10/2026

O Mizuki mandou o R50 e pediu: "Revisione também" e "Aplique as mudanças nos nossos validadores". Esta é a conferência dos números do Morrendo, por `morrendo_r50.py`, nesta pasta. Não é uma medida nova de balanceamento: a regra é a que ele fechou, e o que se confere aqui é se o livro faz a conta que a regra manda.

## A saída do script

```
1. OS EXEMPLOS DO LIVRO, REFEITOS
  [x] máximo 93, Classe 3 — Aguentar: a conta dá 24, o livro escreve 24
  [x] máximo 93, Classe 3 — primeiro Insistir: a conta dá 31, o livro escreve 31
  [x] máximo 93, Classe 3 — metade sem teto: a conta dá 47, o livro escreve 47
  [x] máximo 93, Classe 3 — segundo Insistir, com teto: a conta dá 45, o livro escreve 45
  [x] máximo 395, Classe 7 — Aguentar: a conta dá 99, o livro escreve 99
  [x] máximo 395, Classe 7 — terço sem teto: a conta dá 132, o livro escreve 132
  [x] máximo 395, Classe 7 — metade sem teto: a conta dá 198, o livro escreve 198
  [x] máximo 395, Classe 7 — os dois Insistir, com teto: a conta dá (105, 105), o livro escreve (105, 105)
  [x] Mei, máximo 23 — Aguentar: a conta dá 6, o livro escreve 6
  [x] Mei, máximo 23 — primeiro Insistir: a conta dá 8, o livro escreve 8
  [x] Mei — o que falta com 6 de tratamento: a conta dá 2, o livro escreve 2
  [x] dano posterior — o que falta com 18 de 31: a conta dá 13, o livro escreve 13
  [x] janela com 0, 1, 2 e 3 Sequelas: a conta dá [3, 2, 1, 0], o livro escreve [3, 2, 1, 0]
  >>> exemplos: TODOS CONFEREM

2. O TRATAMENTO NECESSÁRIO PELA VIDA BASE (Vanguarda e Guia: (8+Con)+(5+Con)(n-1); Evocador e Incursor: (6+Con)+(4+Con)(n-1))
   nível | Classe | teto | vida | Aguentar | 1º Insistir | 2º Insistir
       2 |      1 |   15 |   14 |        4 |    5        |    7   [4+Con, Con 2]
       2 |      1 |   15 |   25 |        7 |    9        |   13   [5+Con, Con 6]
       6 |      2 |   30 |   38 |       10 |   13        |   19   [4+Con, Con 2]
       6 |      2 |   30 |   69 |       18 |   23        |   30 (teto)   [5+Con, Con 6]
      10 |      3 |   45 |   62 |       16 |   21        |   31   [4+Con, Con 2]
      10 |      3 |   45 |  113 |       29 |   38        |   45 (teto)   [5+Con, Con 6]
      14 |      4 |   60 |   86 |       22 |   29        |   43   [4+Con, Con 2]
      14 |      4 |   60 |  157 |       40 |   53        |   60 (teto)   [5+Con, Con 6]
      18 |      5 |   75 |  110 |       28 |   37        |   55   [4+Con, Con 2]
      18 |      5 |   75 |  201 |       51 |   67        |   75 (teto)   [5+Con, Con 6]
      22 |      6 |   90 |  134 |       34 |   45        |   67   [4+Con, Con 2]
      22 |      6 |   90 |  245 |       62 |   82        |   90 (teto)   [5+Con, Con 6]
      26 |      7 |  105 |  158 |       40 |   53        |   79   [4+Con, Con 2]
      26 |      7 |  105 |  289 |       73 |   97        |  105 (teto)   [5+Con, Con 6]
      30 |      7 |  105 |  182 |       46 |   61        |   91   [4+Con, Con 2]
      30 |      7 |  105 |  333 |       84 |  105 (teto) |  105 (teto)   [5+Con, Con 6]
   em 420 combinações de nível, Caminho e Constituição 0 a 6: o teto corta o 1º Insistir em 5, o 2º em 160, e Aguentar pede mais que Insistir em 0

3. QUANTO O INSISTIR PEDE A MAIS QUE O AGUENTAR (em pontos de tratamento, e em % da vida máxima)
   nível  2, vida  19 (5+Con, Con 3): 1º Insistir +2 (10.5%) | 2º Insistir +5 (26.3%)
   nível 10, vida  83 (5+Con, Con 3): 1º Insistir +7 (8.4%) | 2º Insistir +21 (25.3%)
   nível 18, vida 147 (5+Con, Con 3): 1º Insistir +12 (8.2%) | 2º Insistir +37 (25.2%)
   nível 26, vida 211 (5+Con, Con 3): 1º Insistir +18 (8.5%) | 2º Insistir +52 (24.6%)

4. RECOMPOSIÇÃO: 5 x Classe antes, 3 x Classe agora, contra o tratamento do 1º Insistir (5+Con, Con 3)
   nível 10: cura 15 -> 9; o 1º Insistir pede 28; a Recomposição cobre 54% -> 32% dele
   nível 18: cura 25 -> 15; o 1º Insistir pede 49; a Recomposição cobre 51% -> 31% dele
   nível 26: cura 35 -> 21; o 1º Insistir pede 71; a Recomposição cobre 49% -> 30% dele

5. RECOMPOSIÇÃO A 4 x A MAIOR CLASSE (o que o Mizuki disse em 14/10 que era para ser), ao lado do 3 x do livro R50
   nível 10: Recomposição 9 (3 x) ou 12 (4 x); cobre 32% ou 43% do 1º Insistir (28); Energia Reversa no teto 13.5 = 1.50 vez o Talento a 3 x e 1.12 vez a 4 x
   nível 18: Recomposição 15 (3 x) ou 20 (4 x); cobre 31% ou 41% do 1º Insistir (49); Energia Reversa no teto 22.5 = 1.50 vez o Talento a 3 x e 1.12 vez a 4 x
   nível 26: Recomposição 21 (3 x) ou 28 (4 x); cobre 30% ou 39% do 1º Insistir (71); Energia Reversa no teto 31.5 = 1.50 vez o Talento a 3 x e 1.12 vez a 4 x
   nível 30: Recomposição 21 (3 x) ou 28 (4 x); cobre 26% ou 35% do 1º Insistir (81); Energia Reversa no teto 31.5 = 1.50 vez o Talento a 3 x e 1.12 vez a 4 x
```

## O que saiu daqui para os validadores

- O `conferir-atributos.py` refaz os três exemplos do livro e a tabela da peça 1 a cada rodada (checagem 9.8), e confere em todo Caminho que Aguentar nunca pede mais que Insistir (9.2).
- O contra-teste da 9.3 mostrou que `15 ×` a maior Classe é o menor teto que mantém essa ordem com a vida base: com `14 ×` ela já quebra.
- A `Recomposição` a `3 ×` a maior Classe deixou a `Energia Reversa` acima dela (`31,5` contra `21` no nível 30). A peça 11 declara a relação, e a pergunta está aberta para o Mizuki.
- Ao ver o `3 ×` no livro, ele disse que a `Recomposição` "era pra ser 4x classe" (item 197). A parte 5 da saída põe os dois lado a lado; a correção entra na próxima edição do livro.
