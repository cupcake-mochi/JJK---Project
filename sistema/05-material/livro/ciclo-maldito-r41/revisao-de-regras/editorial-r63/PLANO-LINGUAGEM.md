# Palavras raras no Livro de Regras

R63, decidida em 03/11/2026. Continua a passada de linguagem simples da R62. Nenhuma regra, número ou mecânica mudou: só a forma do texto. O autor aprovou a lista de trocas com antes e depois.

## O que entrou

A R62 deixou três frentes para a R63, e as três entraram:

- as palavras raras da tabela da R62, de *parcela* para baixo;
- "reserva", que ainda nomeava vida temporária, Integridade, Pontos de Vínculo e outras coisas;
- o nível "Ampliada" das obras do Arquiteto e a ordem do sumário no capítulo 10.

As palavras de alta frequência (*conceder*, *requisito* e outras) não entraram. Ficam para a R64.

## Decisões

1. **"Sobra de dano" é o nome do excedente das entidades** (`campo--inv-queda`): "cai com 22 de sobra", "Zere a sobra ao religar". A sobra continua sendo o que passa de zero; a conta não mudou.
2. **"Parcelas adicionais" virou "Partes adicionais"**, e "parcela" virou "parte" ou "cada tipo" no resto do texto. A âncora `#ritual--rit-parcelas` continua como estava.
3. **"Vinculado" e "elegível" viraram palavras comuns:** "ligado a", no lugar de "preso a", a sugestão do plano; e "permitida", "válido" ou "que conta", no lugar de "liberada". Cada frase usa a que faz sentido nela.
4. **Ficam sem troca:** "arma vinculada" (10 usos), "Retorno Vinculado", "Reserva Excedente", "Ritual de Excedente" e a frase "Excedente usa a cura". São nomes do jogo, não palavras soltas.
5. **"Reserva" sai de 68 usos e fica em 107.**
   - Vida temporária: **pontos separados** ou **vida temporária**.
   - Integridade: **um valor separado**.
   - Reação: **a Reação coletiva**, ou só "ela". A R62 já tinha decidido que a Reação não é uma reserva, e estes casos tinham ficado de fora.
   - Movimento: **metros** ou **movimento separado**.
   - PE: **os pontos** ou **a quantidade de PE**.
   - Pontos de Vínculo: **os pontos**.
   - Barreira: **um total de vida**.
6. **Os usos de "reserva" que ficam:** nomes próprios (38), munição (20), domada (20), guardar para depois (18), verbo comum (10) e a frase nova "a cura guardada por Reserva" (1). O total é 107 e não 106 porque "reservas de cura" virou essa frase, que cita o nome Reserva.
7. **"Ampliada" virou "Extensa"**, e "ampliá-la" virou "aumentá-la". Assim a obra do Arquiteto não usa a raiz do feitiço Ampliar. "Extensa" capitalizada só existe nesse nível. Em minúscula, a palavra aparece em dois usos comuns que não têm relação com a regra: "uma conversa extensa" e "uma sessão extensa".
8. **A "versão ampliada" do feitiço fica**, porque ela é o resultado de Ampliar. "Repertório Ampliado" também fica, porque é nome.
9. **O sumário do capítulo 10 segue a ordem das páginas.** "Conheça as Famílias" sobe de nível, e os Feitiços de Classe 0 (p. 257), que o plano da R62 não listava, entram na ordem certa.
10. **Só a palavra da lista mudou.** "Conceder" e "conservar" continuam até nas frases tocadas, para que cada rodada tenha uma conferência simples.
11. **As âncoras não mudaram**, nem os destinos de link. O Guia do Mestre as usa.
12. **O Guia do Mestre não foi tocado**, porque está em outra frente. O parágrafo para repassar está no fim deste arquivo.

## O que foi feito

**206 trocas em 133 blocos.** A lista completa, com antes e depois, está em `TROCAS-R63.md`, e o registro da cadeia em `../alteracoes/R62-para-R63.json`.

| Motivo | Trocas |
|---|---:|
| parcela | 50 |
| elegível | 26 |
| efetivamente | 13 |
| concessão | 13 |
| vinculado | 7 |
| pertinente | 6 |
| excedente | 5 |
| retroativo | 5 |
| sobra de dano | 3 |
| vencimento | 2 |
| Duas palavras raras na mesma frase | 9 |
| reserva: vida temporária | 28 |
| reserva: Integridade | 13 |
| reserva: movimento | 5 |
| reserva: PE | 5 |
| reserva: Pontos de Vínculo | 4 |
| reserva: Reação | 3 |
| reserva: barreira | 3 |
| Nível "Extensa" da obra | 6 |

**Números:** a contagem ficou igual à da R62. Âncoras e destinos de link também.

**Contagem depois da R63:**

| Termo | No texto |
|---|---:|
| parcela | 0 |
| elegível | 0 |
| efetivamente | 0 |
| concessão | 0 |
| pertinente | 0 |
| retroativo | 0 |
| vencimento | 0 |
| excedente | 3 |
| vinculado, vinculada | 11 |
| reserva e derivadas | 107 |
| Extensa (nível da obra) | 5 |
| sobra, sobras | 25 |

A contagem não distingue maiúscula de minúscula e não inclui âncoras, comentários nem destinos de link. Antes da R63, as raras somavam 170 usos visíveis. As contagens da tabela da R62 eram um pouco diferentes: `elegível` dava 17 sem o plural, e são 32 com ele; `parcela` dava 64 com âncora e links, e são 60 visíveis.

**Composição:** 425 páginas nas duas paletas, com as mesmas páginas por capítulo. O `conferir.py` passou nas 55 verificações. Contra a R62, 131 páginas mudaram, as mesmas nas duas paletas. O papel do título "Partes adicionais" e a ordem do sumário vêm de `gerar_livro.py`, e não do texto (`COMPOSICAO.md`).

**Revisão visual:** as 131 páginas na clara, em 17 folhas de contato. As páginas 3, 110, 342, 343 e 396 também foram vistas lado a lado com a R62, e a 3 também na noturna. Não apareceu título solto, coluna quebrada nem tabela estourada. O sinal automático da p. 3 é falso positivo: são entradas do sumário. Medições em `COLUNAS-R62-R63.json` e `COMPARACAO-R62.json`.

Seis âncoras mudaram de página, todas nas Bênçãos, e o Índice acompanhou: Casco foi de 340 para 341, Vulto de 341 para 342 e Campo de 342 para 343, cada uma com a sua âncora de índice.

## Guardas

As guardas novas de `conferir-fundamento.py` e `conferir.py` têm teste negativo, rodado numa cópia: palavra injetada no livro e no PDF, e sumário fora de ordem. A de `conferir-fundamento.py` também tem contra-teste no próprio validador.

- `conferir-fundamento.py` falha com palavra rara visível no livro: parcela, elegível, efetivamente, concessão, pertinente, retroativo, vencimento, "excedente" fora dos nomes do jogo, "reserva coletiva", "reserva de Reação" e "Ampliada" capitalizada. Comentário, âncora e destino de link não contam.
- `conferir.py` (composição) falha com palavra rara impressa nas duas paletas e com o sumário do capítulo 10 fora da ordem das páginas.
- `conferir-acao.py` e `conferir-fundamento.py` leem as frases novas ("Cada tiro válido de Rajada conta" e "menor parte").
- `testar-integridade.py` (dos dois lugares) reaplica `R62-para-R63.json`, e `conferir-repositorio.py` exige o `REVISAO-R63.json`.

## Fica para a R64

Palavras de alta frequência, contadas no texto da R63:

| Palavra | Ocorrências | Troca sugerida (lista do registro 152) |
|---|---:|---|
| conceder, concede… | 395 | dar, receber |
| requisito | 349 | exigência, o que precisa |
| conservar, conserva… | 341 | manter, continuar com |
| conforme | 163 | como diz, seguindo |
| registre… | 139 | anote |

Sugestão da R62, que continua valendo: fazer capítulo por capítulo, começando pelo 6, que tem 88 páginas. Cada rodada deve ter a mesma conferência de números, âncoras e links desta.

## Teste de leitura

O `editorial-r62/QUESTIONARIO-LEITURA.md` continua sem aplicação, e nenhuma resposta entrou nesta edição. O gabarito continua certo, porque nenhum número mudou. Se ele for aplicado agora, entregue o texto da R63.

## Para quem está mexendo no Guia

> O Livro de Regras saiu na R63 com mais uma passada de linguagem simples, sem mudar regra. O que importa para o Guia:
>
> 1. **O nível do meio da tabela Obras maiores agora é "Extensa"** (Básica, Extensa, Grande). "Ampliada" saiu, e "ampliá-la" virou "aumentá-la". O feitiço Ampliar e a "versão ampliada" dele continuam iguais.
> 2. **O excedente das entidades agora é "sobra de dano"**: "cai com 22 de sobra", "a sobra supera metade da vida máxima". A conta não mudou.
> 3. **"Parcelas adicionais" agora é "Partes adicionais"**, e "parcela" saiu do Livro. A âncora continua `#ritual--rit-parcelas`.
> 4. **"Reserva" não descreve mais a vida temporária, a Integridade, os PE, os Pontos de Vínculo, a vida da barreira nem o movimento.** A vida temporária são "pontos separados que absorvem dano antes da vida", e a Integridade é "um valor separado". "Reserva" continua nos nomes próprios, como Reserva Excedente, na munição e na domada.
> 5. **"Elegível", "efetivamente", "concessão", "pertinente", "retroativo" e "vencimento" saíram do Livro.** "Vinculado" ficou só nos nomes: arma vinculada e Retorno Vinculado.
> 6. **O que não mudou:** nenhum número, custo, gatilho ou âncora. Todo link do Guia para o Livro continua válido, mas o título que o leitor vê no destino pode ter mudado, como no item 3.
>
> Os casos do Guia não foram conferidos contra esses termos, porque o Guia está em outra frente. Vale procurar neles por "Ampliada", "excedente", "parcela", "elegível" e "reserva". A lista completa de trocas está em `editorial-r63/TROCAS-R63.md`, no repositório do sistema.
