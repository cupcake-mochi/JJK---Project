---
name: balanceamento-simulacao
description: Valida números de RPG de mesa com código em vez de intuição — curva de probabilidade, teto de dano, taxa de sucesso, quão "swingy" é uma mecânica de dado, busca exaustiva de todas as montagens legais, matriz de dominância e teste de regressão contra exemplos já publicados. Use sempre que alguém quiser saber se um número de RPG fecha, se uma mudança de preço quebrou alguma coisa, qual a chance de sucesso de uma rolagem, quantas rodadas um combate dura, ou se existe uma combinação abusiva que ninguém percebeu. Use também quando o pedido for só "isso tá balanceado?" ou "esse feitiço tá forte demais?" — a resposta certa é rodar a conta, não opinar. Serve para checar antes de publicar uma versão nova de um manual. Nunca dispara para decidir a CD de um teste dentro de uma cena de sessão em andamento — isso é decisão de mestre em tempo real, não balanceamento de manual.
---

# Balanceamento por simulação

Intuição de designer erra em duas direções previsíveis: subestima o efeito de combinações e superestima o efeito de números isolados. Código não tem essa fraqueza. A regra desta skill é simples — **quando a pergunta tem resposta numérica, rode a conta antes de responder.**

## Ordem de trabalho

1. Escrever o contrato de invariantes
2. Modelar as regras em código
3. Rodar a busca exaustiva
4. Rodar a matriz de dominância
5. Rodar a regressão contra os exemplos publicados
6. Reportar em linguagem de designer, não de programador

Os passos 1 e 6 são os que mais mudam a qualidade do resultado, e são os dois que mais gente pula.

## 1. O contrato de invariantes

Antes de escrever uma linha de código, escreva a lista de números que **precisam continuar verdadeiros**. Ela vira o cabeçalho do script e o critério de aprovação.

Um contrato real, de um sistema de construção de feitiços por pontos:

```
Pontos = 3 × Classe          Teto = 4 × Classe
Devolução máxima = 2 × Classe   Liberação = + Classe em dados
Leve = metade da Classe · Média = Classe · Pesada = Classe e meia (arredonda pra cima)
Custo em PE = 3 × Classe
Pico do nível 20 = 90 de dano em feitiço montado.
Se mudar, alguma coisa quebrou.
```

O valor disso não é documentação. É que **quebra de invariante deixa de ser questão de gosto e vira bug**. Sem o contrato, toda revisão vira discussão; com ele, o script decide.

Escreva o contrato mesmo quando o sistema for de outra pessoa e você só estiver auditando. Se ele não estiver escrito em lugar nenhum, derivá-lo dos exemplos publicados costuma ser o primeiro achado útil da auditoria.

## 2. Modelar as regras

Traduza as regras para funções pequenas e conferíveis. Duas armadilhas:

**Arredondamento.** Regra de mesa quase sempre arredonda, e quase nunca diz para que lado. Descubra pelos exemplos publicados antes de assumir. Um `ceil` onde devia ser `floor` desloca a tabela inteira e você só percebe três seções depois.

**Efeitos embutidos.** Muitas peças carregam outra peça por dentro — uma forma de curto alcance que já vem com a desvantagem "corpo a corpo" embutida, e que portanto ocupa espaço no limite de desvantagens. Modelar sem isso produz montagens que parecem legais e não são.

## 3. Busca exaustiva

Esta é a técnica que mais rende, e é mais barata do que parece.

**Enumere todas as montagens legais e olhe os extremos.** Se o espaço for grande demais para enumerar montagem por montagem, enumere **perfis de custo** — quantas peças de cada faixa de preço, quantas desvantagens de cada faixa — em vez de peças nominais. O perfil é o que determina o número; o nome da peça só importa para as travas de combinação.

O que a busca precisa reportar:

- **O máximo alcançável** em cada faixa, e a montagem que o alcança.
- **Se o máximo bate exatamente no teto declarado.** Bater exatamente é bom sinal: significa que o teto é alcançável e que nada o ultrapassa. Ficar abaixo significa que o teto é decorativo. Passar significa bug.
- **Quantas montagens legais existem**, e quantas ganham cada bônus condicional. É assim que se detecta bônus automático: se 100% das montagens legais ganham, não é bônus.
- **Quais combinações precisam ser travadas.** Pares que devolvem o orçamento inteiro em troca de uma condição que quase nunca falha costumam aparecer aqui.

O script `scripts/busca-exaustiva.py` traz o esqueleto desse padrão, comentado, pronto para adaptar.

## 4. Matriz de dominância

Para cada par de opções na mesma faixa de preço, responda: **existe alguma situação em que eu escolheria a mais fraca?**

Automatizável em parte: se a opção A impõe um superconjunto das restrições de B pelo mesmo preço, A está dominada, e isso dá para checar por código quando as restrições estiverem modeladas como conjuntos de recursos consumidos (movimento, ação bônus, ação padrão, reação, mão livre, turno futuro).

A parte não automatizável é a flexibilidade: uma opção que dói mais mas pode ser preparada num turno morto tem valor que a matriz não enxerga. Reporte o par suspeito e deixe a decisão para quem conhece a mesa.

Quando encontrar dominância e o teto do sistema não permitir subir o preço da opção mais dolorosa, a saída é **dar upside a ela**, não achatar as duas.

**E a armadilha maior: a matriz só enxerga os eixos que ela tem coluna.** Se a decisão que você está conferindo tem duas metades — uma que a matriz mede e outra que não —, perturbar a metade invisível sai **verde**. E verde parece prova.

O caso que ensinou isso: uma opção estava dominada, e o conserto foi dar a ela orçamento maior **e** vida maior. Só o orçamento já zerava a matriz. Tirar a vida saía verde, desfazendo em silêncio a outra metade da decisão — a que dizia *"perder esse corpo acaba o kit do jogador"*.

Vira duas regras de trabalho:

- **Quando não existir número que conserte a dominância dentro dos eixos que você tem, o que falta é uma coluna, não um valor.** Se as opções empatam em tudo que a matriz mede, a matriz terminou e a resposta mora fora dela. Qualquer eixo novo em que só a dominada esteja na frente mata todas as dominâncias de uma vez, e o número vem depois de escolher o eixo.
- **Toda metade de decisão que a matriz não mede ganha checagem própria, separada** — com mensagem que nomeie o que ela está medindo, senão ela vira mais uma linha verde.

E os eixos da matriz se leem **da tabela do documento dono**, nunca de constante escrita dentro do script. Se a tabela sumir ou mudar de formato, o certo é o script falhar alto dizendo isso, e não cair para um valor de reserva.

## 5. Regressão

Todo exemplo que aparece no material publicado — feitiço pronto, tabela, exemplo guiado, número solto no meio de um parágrafo — precisa ser recalculado pelo script.

Isso é o que transforma o validador em rede de segurança de verdade. Uma mudança de preço numa peça repercute em qualquer exemplo que a use, e é humanamente impossível rastrear isso à mão num manual de dezenas de páginas. O script deve terminar com um veredito único e sem ambiguidade:

```
>>> TUDO OK — todos os exemplos e tabelas conferem.
```

ou a lista de divergências, cada uma dizendo o valor esperado, o valor encontrado e onde ele aparece no material.

Trate esse script como parte do material, não como ferramenta descartável. Ele roda antes de gerar qualquer versão nova.

## 6. Reportar

O consumidor do resultado é designer, não programador. O relatório precisa dizer:

- **O que mudou em jogo**, em termos de mesa: "esse feitiço passa de 22 para 27 de dano médio, e nenhum estoura o teto".
- **Quantos itens do material foram afetados**, nominalmente.
- **O que continua verdadeiro** — os invariantes que não se mexeram.
- **O que ficou em aberto.** Tensão que a mudança criou e não resolveu vale mais registrada do que escondida. Exemplo: "com A subindo para a faixa média, ela agora divide faixa com B, e B dói mais; não dá para subir B sem estourar o fecho, então a saída seria dar upside a B."

Números crus sem essa tradução não ajudam ninguém a decidir.

## Ferramentas

**Distribuição exata, sempre que der.** Simulação de Monte Carlo introduz ruído que se confunde com efeito real. Para dados, a distribuição exata é barata de calcular. `scripts/dados.py` traz as funções prontas: soma de dados arbitrários, "pelo menos N", pool contando sucessos, maior de N dados, vantagem, e o valor marginal de um bônus.

**`dice-calc`** (PyPI, Python puro, zero dependência) compila código do AnyDice direto para Python e roda local. Útil quando a mecânica já estiver escrita em sintaxe AnyDice ou quando quiser conferir contra a referência da comunidade:

```
pip install dice-calc --break-system-packages
```

```python
from dice_calc.parser import compile_anydice
from dice_calc import *
exec(compile_anydice('output 2d6 named "2d6"'))
```

**Monte Carlo só quando não houver saída** — combate completo com múltiplos atores, iniciativa e decisão adaptativa. Nesse caso, rode iterações suficientes para o intervalo de confiança ficar menor que o efeito que você quer detectar, e **reporte a incerteza junto do número**. Um resultado de 54,2% sem barra de erro é uma afirmação que o método não sustenta.

## Perguntas frequentes e como respondê-las

**"Isso está balanceado?"** — Traduza para: comparado com o quê, na mesma faixa de preço? Balanceamento é relação, não propriedade. Rode dominância contra as vizinhas e teto contra o contrato.

**"Isso está forte demais?"** — Calcule o máximo alcançável e compare com o teto declarado. Se não houver teto declarado, esse é o achado.

**"Quantas rodadas dura o combate?"** — `vida ÷ maior dano concentrado por rodada`, calculado em **cada faixa de nível**, não só no topo. Sistemas costumam ser mais letais no começo e ninguém percebe porque só testam o topo.

**"Vale a pena essa mudança de preço?"** — Rode a regressão antes e depois e conte quantos itens publicados mudam de resultado. O custo real de uma mudança de preço é o retrabalho que ela gera, e esse número é mensurável.

## Arquivos

- `scripts/dados.py` — distribuições exatas e valor marginal de bônus. Importe em vez de reescrever.
- `scripts/busca-exaustiva.py` — esqueleto comentado da busca por perfis de custo, com matriz de dominância e o formato de relatório final.
