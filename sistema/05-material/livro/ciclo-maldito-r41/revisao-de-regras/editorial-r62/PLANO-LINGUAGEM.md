# Linguagem simples no Livro de Regras

R62, 03/11/2026. É a passada de linguagem simples do Livro, feita depois do piloto do Guia do Mestre (registro 152). Nenhuma regra, número ou mecânica mudou: só a forma do texto. As decisões saíram de uma sabatina com o autor (Q1 a Q20).

## O problema

O Livro tinha o mesmo defeito que o leitor apontou no Guia: palavras que soam complicadas, e não frases longas. A pior era **"saldo"**, com seis sentidos: pontos de montagem (o único definido no Glossário), vida e PE atuais, metros de movimento, básicas que passam na troca de invocação, XP acumulado e dinheiro. Isso quebra a regra "uma coisa por nome". Outros casos:

- "lugar propício" e "ambiente propício" para a mesma coisa;
- "Ampliar", que nomeava o feitiço (cap. 10) e a ação de obra do Arquiteto, Trilha do Guia (cap. 6);
- a Reação descrita como "reserva";
- termos usados antes de serem definidos.

## Decisões

1. **"Saldo" sai do texto inteiro.** Na montagem vira **pontos que sobram**, e a fórmula passa a ser *Pontos que sobram = 3 × Classe − base das funções − custo da Forma − Melhorias + devolução aproveitada*. Nos outros sentidos:
   - vida e PE: **vida atual** e **PE atuais**;
   - movimento: **metros que restam** e **3 m extras**;
   - básicas: **as básicas que a anterior ainda tinha**;
   - XP: **XP guardado**.
2. **Âncoras e chaves de código continuam com "saldo"** (`fundamento-link-saldo`, `construcao--entidades-saldo`). O leitor não as vê, e trocá-las quebraria links de fora.
3. **"Ambiente propício" é o único nome.** Ganhou entrada no Glossário e no Índice.
4. **Na montagem, o verbo é sempre "destinar".**
5. **A Reação é algo que se gasta**, nunca uma "reserva".
6. **A ação de obra do Arquiteto passa a se chamar "Aumentar"**, e a ação "Ampliar" fica só com o feitiço. A análise e a Q5 da sabatina chamaram essa obra de "do Emanador" por engano: ela é do Arquiteto (bloco `guia--guia-obra-uso`). O texto do livro não tinha esse erro.
7. **Termos usados antes da definição ganham explicação no primeiro uso.** A explicação é um aposto curto, tirado do Glossário, mais um link. Dos oito da lista, um era o próprio "saldo", que saiu. Seis ganharam aposto: Inconsciente, Vida temporária, Exaustão, Técnica Marcial, Manejo e Aptidão. A Intenção, que aparece numa célula de tabela, ganhou só o link.
8. **Palavras de cartório só saíram das frases que já seriam mexidas.** O resto fica para a R63.
9. **Sem piloto antes da publicação** (Q14). Em troca, revisão visual página por página no fim: espaços em branco, colunas e quebras, com o mesmo número de páginas nas duas paletas.
10. **O Guia do Mestre não foi tocado**, porque está sendo mexido em outra frente. O parágrafo para repassar está no fim deste arquivo.
11. **As peças de `03-mecanica/` não foram tocadas.**

## O que foi feito

**123 trocas em 60 blocos.** A lista completa, com antes e depois, está em `TROCAS-R62.md`, e o registro da cadeia em `../alteracoes/R61-para-R62.json`.

| Motivo | Trocas |
|---|---:|
| Montagem: pontos que sobram e "destinar" | 78 |
| Vida e PE atuais | 7 |
| Básicas na troca de invocação | 7 |
| Termo explicado no primeiro uso | 7 |
| Movimento | 6 |
| Glossário | 4 |
| Índice | 4 |
| Reação | 3 |
| Ambiente propício | 2 |
| Usos | 2 |
| XP guardado | 2 |
| Obra do Emanador | 1 |

**Números:** iguais aos de antes, com uma exceção. O exemplo do descanso longo ganhou a conta "a metade é 11" (metade de 23, arredondada para baixo).

**Contagem depois da R62:**

| Termo | No texto |
|---|---:|
| saldo | 0 |
| lugar propício | 0 |
| local propício | 0 |
| ambiente propício | 22 |
| pontos que sobram | 60 |
| vida atual | 10 |
| PE atuais | 7 |
| XP guardado | 5 |

A contagem não inclui âncoras, comentários nem destinos de link.

**Composição:** o cabeçalho corrido, as etiquetas de continuação e a linha do sumário de "Funções e saldo" vinham da configuração da composição, e não do texto. A revisão visual os achou, e eles passaram a dizer "Funções e pontos que sobram". A revisão também achou a fórmula da vida máxima separada da introdução na virada da página 243, e a regra R40 de `fluxo_continuo.py` passou a mantê-las juntas.

## Guardas

Cada guarda tem teste negativo, rodado numa cópia do repositório.

- `conferir-fundamento.py` falha com "saldo" visível no livro. Comentário, âncora e destino de link não contam. Também confere a fórmula com o nome novo.
- `conferir-nomes.py` trata "Saldo" capitalizado como nome aposentado nas peças, no ESTADO e no LEIA-ME.
- `conferir.py` (composição) falha com "saldo" impresso em qualquer página das duas paletas.

## Fica para a R63

Palavras de cartório fora das frases tocadas, contadas no texto da R62 (sem comentários):

| Palavra | Ocorrências | Troca sugerida (lista do registro 152) |
|---|---:|---|
| conceder, concede… | 395 | dar, receber |
| requisito | 349 | exigência, o que precisa |
| conservar, conserva… | 341 | manter, continuar com |
| conforme | 163 | como diz, seguindo |
| registre | 139 | anote |
| parcela | 64 | parte |
| excedente | 18 | o que sobra, o que passa do máximo |
| vinculado | 18 | preso a |
| elegível | 17 | liberada, que pode |
| efetivamente | 15 | de fato, ou cortar |
| concessão | 14 | reescrever a frase |
| pertinente | 6 | que faça sentido |
| retroativo | 5 | reescrever a frase |
| vencimento | 2 | quando expira |

Também ficam para a R63:

- **"Ampliada" e "ampliá-la" nas obras do Arquiteto** (5 usos de "Ampliada"). "Ampliada" é o nível do meio da tabela Obras maiores (Básica, Ampliada, Grande), que a Q5 não tratou. Não é a ação "Ampliar" do feitiço, mas usa a mesma raiz.
- **"reserva" e "reservado"** (cerca de 185 usos), que ainda nomeiam vida temporária, Integridade, Pontos de Vínculo e a reserva da domada. A Reação já saiu dessa lista na R62.
- **A ordem do sumário no capítulo 10.** Alguns itens aparecem fora da ordem das páginas: "Sua técnica" (249) depois de "Conheça as Famílias" (250), e "Selo e Talentos" (251) depois de "Famílias" (257). Isso já era assim na R61, e a R62 não mexeu.

Sugestão de ordem: começar pelas palavras raras da tabela (de *parcela* para baixo, cerca de 160 usos). Depois, as de alta frequência, capítulo por capítulo, começando pelo 6, que tem 88 páginas. Cada rodada deve ter a mesma conferência de números, âncoras e links desta.

## Teste de leitura

`QUESTIONARIO-LEITURA.md` traz 10 perguntas com gabarito, no molde do registro 152. Ainda não foi aplicado.

## Para quem está mexendo no Guia

> O Livro de Regras saiu na R62 com uma passada de linguagem simples, sem mudar regra. O que importa para o Guia:
>
> 1. **"Saldo" saiu do Livro.** Na montagem de técnica virou **pontos que sobram**. A fórmula agora é *Pontos que sobram = 3 × Classe − base das funções − custo da Forma − Melhorias + devolução aproveitada*. Nos outros sentidos:
>    - **vida atual** e **PE atuais**;
>    - **metros que restam** e **3 m extras** (movimento);
>    - **as básicas que a anterior ainda tinha** (troca de invocação);
>    - **XP guardado**.
>
>    O Guia pode usar os mesmos nomes. O cap. 7 e os casos 30, 31, 53, 94 e 99 são os que citam a montagem.
> 2. **"Ambiente propício" é o único nome.** "Lugar propício" e "local propício" saíram. O Livro tem verbete no Glossário e no Índice, e os casos 90 e 91 do Guia ainda usam os nomes antigos.
> 3. **Na montagem, o verbo é "destinar"** ("cada ponto destinado vira 1d8"), não "reservar".
> 4. **A ação de obra do Arquiteto se chama "Aumentar"**, e a ação "Ampliar" ficou só com o feitiço. O nível "Ampliada" da tabela Obras maiores não mudou.
> 5. **O que não mudou:** nenhum número, custo, gatilho ou título de seção que o Guia linke. As âncoras continuam as mesmas, inclusive `#fundamento-link-saldo`, e todo link do Guia para o Livro continua válido.
>
> A lista completa de trocas está em `editorial-r62/TROCAS-R62.md`, no repositório do sistema.
