# Prompt de continuidade

Copie o bloco abaixo e cole como primeira mensagem de uma conversa **nova, dentro do mesmo projeto**.

---

```
Retomando o RPG da Guilda. Antes de qualquer coisa, leia nesta ordem:

1. H:\Claude 2\RPG-JJK\ESTADO-ATUAL.md — o sistema inteiro em uma página, as
   pendências ordenadas e como eu gosto de trabalhar
2. H:\Claude 2\RPG-JJK\CHANGELOG.md — o porquê de cada decisão. É a parte que
   não dá pra reconstruir sozinho, leia pelo menos até a v0.10
3. H:\Claude 2\RPG-JJK\02-esqueleto\arquitetura.md — o mapa do que existe e do
   que falta

Depois rode os dois validadores pra confirmar que nada quebrou:

  cd "/sessions/<sessao>/mnt/Claude 2/RPG-JJK/03-mecanica"
  python3 conferir-atributos.py
  python3 conferir-acao.py

Quatro coisas que valem saber de saída, porque foram aprendidas errando:

- Numa rolagem disputada, os dois lados precisam crescer no MESMO RITMO.
  Atributo investido cresce +3 na campanha; maestria cresce +3. Verificar
  invariância contra o nível NÃO basta — tudo que cresce numa campanha
  (atributo, proteção, equipamento) tem que entrar no teste.
- Antes de batizar qualquer coisa, cheque colisão de termo em duas direções:
  contra o manual do Fundamento e contra o resto do material do projeto. Já
  pegou três colisões reais (Grau, Leitura, Canalizador).
- Tensão de preço às vezes é lacuna de texto disfarçada. Antes de mexer no
  número, confira se a regra diz o que você acha que ela diz.
- Rode a conta antes de opinar. Metade dos achados deste projeto veio de
  calcular uma coisa que parecia óbvia.

A próxima peça é o quadro completo de perícias: 24 a 28 no total, com o
atributo de cada. Ela trava a criação de personagem, que é a peça seguinte.
Me mostre a proposta antes de escrever o documento.
```

---

## O que a conversa nova herda automaticamente

Por estar dentro do mesmo projeto, a conversa nova já vem com:

- **As instruções do projeto** ("Criação de um sistema de RPG do 0")
- **A pasta conectada** `H:\Claude 2`, com todos os arquivos
- **A memória** do projeto — o que a Guilda é, como você gosta de trabalhar
- **As quatro skills instaladas**, que são de conta e disparam sozinhas

## O que ela não herda

**O histórico da conversa.** É por isso que o prompt manda ler os três arquivos antes de agir: eles são o histórico, na forma que sobrevive.

O que se perde de verdade são as discussões que **não** viraram decisão — os caminhos descartados e o motivo. Se algum deles importar, anote antes de virar a página.
