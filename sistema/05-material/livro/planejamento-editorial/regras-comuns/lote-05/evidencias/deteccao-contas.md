# Detecção — comparação matemática exata

Gerado por `deteccao-contas.py`, usando somente Python 3 e `fractions.Fraction`. Enumeração completa; nenhuma amostragem aleatória. Frações são exatas; percentuais são arredondados a até quatro casas. O JSON conserva numeradores, denominadores e a distribuição por CD.

## Premissas

O personagem primeiro usa Esconder: `d20 + Furtividade ≥ 10 + Percepção`. Só as faces que conseguiram esse sucesso entram na comparação de buscas. O total histórico de Furtividade obtido é a CD guardada; **não é uma CD passiva calculada pelo bônus de Furtividade**. Todas as faces restantes têm o mesmo peso condicionado. A busca tem sucesso com `d20 + Sentir Energia ≥ total guardado`, incluindo empates. Não há falha automática em 1 nem sucesso automático em 20.

Todos os casos supõem uma fonte de energia já alcançada pela busca candidata de 18 m, sem bloqueio ou interferência adicional. O cálculo compara testes; **não demonstra que 18 m seja o alcance adequado**. A regra calculada não acrescenta CD passiva de energia ao ato de Esconder.

Antena significa uma única rerrolagem após falhar, contra a **mesma CD**, consumindo o uso do Legado e mantendo o custo de uma Ação Padrão. Dois buscadores rolam separadamente contra essa mesma CD, com o mesmo bônus Sentir Energia indicado; a comparação principal considera duas Ações Padrão e pelo menos um sucesso. Não inclui dois usos de Antena nem mudanças de posição/alvo entre as tentativas.

## Depois que Esconder funcionou

| Furtividade / Percepção / Sentir | Chance inicial de Esconder | CDs guardadas possíveis, após sucesso | Uma busca | Busca + Antena | Dois buscadores iguais, 2 Padrões |
|---|---|---|---|---|---|
| +4 / +4 / +4 | 55% (11/20) | 14 a 24 | 30% (3/10) | 48,5% (97/200) | 48,5% (97/200) |
| +4 / +4 / +12 | 55% (11/20) | 14 a 24 | 70% (7/10) | 88,5% (177/200) | 88,5% (177/200) |
| +12 / +4 / +4 | 95% (19/20) | 14 a 32 | 17,3684% (33/190) | 28,0789% (1067/3800) | 28,0789% (1067/3800) |
| +12 / +4 / +12 | 95% (19/20) | 14 a 32 | 50% (1/2) | 67,5% (27/40) | 67,5% (27/40) |

A chance nas três últimas colunas é **condicionada ao sucesso inicial de Esconder**. Não é a chance de localizar alguém antes de saber se conseguiu se ocultar. Antena e duas buscas iguais têm a mesma probabilidade de ao menos um sucesso neste recorte; os custos e a disponibilidade são diferentes. Se o segundo buscador só agir depois de o primeiro falhar, o grupo pode economizar a segunda ação nos sucessos iniciais; esta tabela contabiliza a capacidade de investir até duas, sem avaliar esse valor tático.

As rolagens de busca são independentes **dada a CD guardada**, mas compartilham a mesma dificuldade histórica. Por isso calculamos `média[1 − (1 − p(CD))²]`, e não `1 − (1 − média[p(CD)])²`. Por exemplo, no caso +4/+4/+4, a chance média de uma busca é 30%, mas Antena dá **48,5%**, não 51%. Tirar a média antes de elevar ao quadrado superestimaria o benefício.

## Variante: um buscador de Percepção e outro de Sentir Energia

Esta comparação adicional só vale quando ambos têm sinais acessíveis para usar sua perícia. O custo considerado é de duas Ações Padrão. A tabela principal usa dois buscadores com o mesmo Sentir; não se deve confundir os dois cenários.

| Furtividade / Percepção / Sentir | Pelo menos um sucesso, condicionado a Esconder |
|---|---|
| +4 / +4 / +4 | 48,5% (97/200) |
| +4 / +4 / +12 | 76,5% (153/200) |
| +12 / +4 / +4 | 28,0789% (1067/3800) |
| +12 / +4 / +12 | 53,7632% (2043/3800) |

## Contrafactual: acrescentar uma segunda CD passiva

Este cenário é **uma alteração indevida da regra candidata**, incluída somente para medir seu efeito. O mesmo resultado de Esconder teria de alcançar as duas CDs, equivalendo a `max(10 + Percepção, 10 + Sentir Energia)`. Não se multiplicam duas probabilidades: existe um só dado de Esconder. A comparação abaixo é anterior a qualquer busca ativa; não mistura a distribuição nova com os resultados condicionados da primeira tabela.

| Furtividade / Percepção / Sentir | Só CD 10 + Percepção | Com segunda CD 10 + Sentir | Queda absoluta em pontos percentuais |
|---|---|---|---|
| +4 / +4 / +4 | 55% (11/20) | 55% (11/20) | 0 p.p. |
| +4 / +4 / +12 | 55% (11/20) | 15% (3/20) | 40 p.p. |
| +12 / +4 / +4 | 95% (19/20) | 95% (19/20) | 0 p.p. |
| +12 / +4 / +12 | 95% (19/20) | 55% (11/20) | 40 p.p. |

Nos dois exemplos com Sentir +12 e Percepção +4, a segunda passiva reduziria a chance inicial de Esconder em 40 pontos percentuais. Isso concederia influência sem gastar a Ação Padrão da busca. O número descreve estes casos, não prova que toda defesa passiva energética seria inviável em qualquer design.

## Referência simples: CD fixa 16

Aqui a CD já está fixada, portanto não existe a média sobre resultados históricos diferentes. A fórmula `1 − (1 − p)²` pode ser aplicada diretamente.

| Bônus da busca | Uma tentativa | Com uma rerrolagem de Antena | Dois buscadores iguais, 2 Padrões |
|---|---|---|---|
| +4 | 45% (9/20) | 69,75% (279/400) | 69,75% (279/400) |
| +6 | 55% (11/20) | 79,75% (319/400) | 79,75% (319/400) |

## Leitura limitada dos resultados

O bônus de Sentir aumenta a chance de uma busca ativa superar a Furtividade já conseguida. Antena amplia essa chance ao custo de seu uso; outro buscador exige outra ação. Os dados mostram esses efeitos exatos nos casos escolhidos, **sem concluir equilíbrio global**, validar alcance, valorar PE, simular múltiplos alvos ou medir o valor de atacar um inimigo localizado que ainda não pode ser visto.

A distribuição por CD está no JSON. O script confere a fórmula de duas tentativas contra enumeração dos 400 pares possíveis de d20 e também enumera conjuntamente o dado original de Esconder e os dois dados de busca. As verificações de CD fixa e de ausência de 1/20 automáticos estão no próprio script.

Reprodução: execute `python3 deteccao-contas.py` na pasta deste arquivo, ou passe o caminho completo do script. Os dois arquivos gerados são gravados ao lado dele; a minuta não é modificada.
