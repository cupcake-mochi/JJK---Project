# ECONOMIA DE AÇÃO E INICIATIVA

**Fase 4, terceira peça.** O turno, os recursos que ele contém, iniciativa e o que o Fundamento vende sem ter definido.
Versão v0.11, corrigida na v0.17 e na v0.26 — 10/08/2026

---

## 1. Esta peça é diferente das outras

As duas anteriores desenhavam do zero. Esta **descobre** — a economia de ação já existe dentro do Fundamento, espalhada por dezesseis peças que vendem pedaços de turno. Ela só nunca foi escrita.

O que o manual já declara, no glossário: `Ação | Padrão · Bônus · Reação · Rodada inteira`. E o que ele usa sem definir:

| Usado por | O que nunca foi definido |
|---|---|
| Passo, Pressa, Peso Morto | **Deslocamento base.** Passo dá 6 m, Pressa dá +6 m, Peso Morto corta pela metade — de quanto? |
| Passo, Pressa | **Ataque de oportunidade.** As duas dizem "sem provocar". Provocar o quê? |
| Adianta | **Iniciativa.** A Melhoria dá +2 na CD se você conjurar antes de qualquer inimigo agir. |
| Fica, Mão Firme | **Concentração.** Uma exige, a outra protege de dano até 10. |
| Parado, Lento | **Movimento como recurso separado.** Parado tira o movimento e mantém a ação bônus. |

## 2. O teste da premissa herdada

Esta é a parte mais herdada do sistema inteiro, e vale dizer isso em voz alta em vez de fingir que foi escolha.

Ação padrão, ação bônus, reação, movimento e ataque de oportunidade são o esqueleto de turno do d20 moderno. O Fundamento foi escrito em cima dele, e dezesseis peças já têm preço calibrado nessa premissa — **trocar o esqueleto de turno agora significa reprecificar todas elas e revalidar os 35 feitiços prontos.**

A conclusão honesta: **mantemos, e por custo de retrabalho, não por mérito.** O que dá para fazer é escolher bem os detalhes que ainda estão abertos, e é o que o resto deste documento faz.

Duas premissas que **não** vamos herdar sem checar:

- **Ataque de oportunidade existe?** Sim, e ele passa no teste de finalidade: sem ele, sair de um corpo a corpo é grátis, e a Melhoria Passo perde a razão de existir. E em Jujutsu Kaisen dar as costas para um feiticeiro em alcance de toque *deveria* custar caro.
- **Iniciativa é rolada?** Sim, e por um motivo mecânico específico. Ver seção 5.

## 3. O turno

Um turno contém quatro recursos, e eles são independentes:

| Recurso | Quantos | O que faz |
|---|---|---|
| **Movimento** | até 9 m | pode ser dividido antes, durante e depois da ação |
| **Ação padrão** | uma | atacar, conjurar, a maioria das coisas |
| **Ação bônus** | uma | só o que a regra disser explicitamente que é ação bônus |
| **Reação** | uma, e ela volta no começo do seu turno | responde a um gatilho, e vale fora do seu turno |

**Rodada inteira** (o que o Fundamento chama de Ação Completa) não é um quinto recurso: é gastar movimento, ação padrão e ação bônus de uma vez.

**Deslocamento base: 9 metros.** O número não é arbitrário — ele conversa com o resto das distâncias do Fundamento. O alcance base de Projétil é 18 m, então um turno de movimento fecha metade da distância de um duelo. A escada de área começa em raio de 3 m, então sair de uma explosão custa um terço do seu movimento. E os +6 m de Passo e Pressa são acréscimos que importam sem dobrar nada.

**Ataque de oportunidade.** Quando alguém sai do seu alcance de corpo a corpo sem tomar cuidado, você pode gastar a sua Reação para atacar. É o que dá sentido a Passo e Pressa dizerem "sem provocar".

**Concentração.** Alguns efeitos exigem que você mantenha a atenção neles — a Melhoria **Fica**, um efeito que dura, uma condição que você segura. Você só concentra em um por vez, e ao tomar dano faz um **Teste de Resistência Vigor** contra CD 10 ou metade do dano, o que for maior. Falhou, o efeito cai.

*Corrigido na v0.26.* Este parágrafo dizia **Físico**, e o manual dizia *"teste de Constituição"* dentro da Restrição Carregar — dois documentos, dois testes, e este aqui ainda afirmava que era *"a mesma régua que Carregar já usa"*. A régua da CD era; o teste não. **Concentração é Vigor**, e o manual v7.6 deixou de nomear teste pelo atributo.

**E Carregar deixou de ser concentração.** Os dois seguram alguma coisa contra o dano, mas a diferença já estava escrita e ninguém tinha lido: em Concentração *"o efeito cai"* — você tinha, e perdeu; em Carregar *"perde o feitiço"* — ele ainda não tinha saído. Um mantém o que está no ar, o outro segura o que está por sair.

| | o que você segura | teste | falhar custa |
|---|---|---|---|
| **Concentração** | o efeito que já está no ar | **Vigor** | o efeito cai |
| **Carregar** | o feitiço que ainda não saiu | **Espírito** | o feitiço, e o que você pagou por ele |

A Passiva **Mão Firme** cobre os dois, e o manual v7.6 diz isso com todas as letras — *"não perde concentração nem carga por dano de 10 ou menos"* —, porque com a divisão o nome dela sozinho não alcançava mais o Carregar.

## 4. A régua de preço

O Fundamento vende pedaços de turno em onze Restrições, e nunca teve uma régua para justificar quanto cada uma devolve. Com os recursos definidos, ela existe:

> **Leve** — consome **um** recurso, ou meio recurso espalhado por dois turnos.
> **Média** — consome **o turno inteiro**, ou um recurso mais um risco real.

Conferindo o catálogo existente contra essa régua:

| Restrição | preço | o que consome | fecha? |
|---|---|---|---|
| Parado | Leve | movimento | sim |
| Gesto | Leve | mãos e voz | sim |
| Peso Morto | Leve | metade do movimento, dois turnos | sim |
| Frágil | Leve | risco de perder o efeito | sim |
| Tudo ou Nada | Leve | chance de zerar | sim |
| Lento | Média | movimento + bônus + padrão | sim |
| Corpo a Corpo | Média | a distância inteira, para sempre | sim |
| Sangra | Média | vida | sim |
| Recuo | Média | condição no corpo até o próximo turno | sim |
| Sem Volta | Média | o próximo turno inteiro, se errar | sim |
| Carregar | Média | ação padrão do turno anterior + risco de perder tudo | ver abaixo |

**Dez das onze fecham.** Rodando o teste de dominância por conjunto de recursos, nenhum par de mesmo preço contém o outro. O catálogo estava certo — só não tinha como provar.

### O caso Carregar, que a v7.3 deixou em aberto

O changelog da v7.3 registrou a tensão: *"Carregar (Média) fica na mesma faixa do Lento e dói mais, porque consome dois turnos e ainda arrisca perder o feitiço se você tomar dano."*

Com a régua na mão, a resposta é mais simples do que parecia, e não exige mexer em preço.

**Lento** consome três recursos, todos neste turno, sem risco. **Carregar** consome um recurso do turno anterior mais o risco. São conjuntos diferentes, em turnos diferentes — não há dominância de conjunto.

O problema é que **o texto do manual não diz se quem carrega pode se mover no turno de carga.** E é isso que decide:

- Se **pode se mover**, Carregar tem um upside que Lento não tem: você fica móvel enquanto prepara. Os dois valem Média por caminhos diferentes, e o par se resolve sozinho.
- Se **não pode**, Carregar vira Lento com espera e risco por cima, e aí está dominado de verdade.

**A decisão: quem usa Carregar mantém o movimento e a ação bônus no turno de carga.** Só a ação padrão vai embora. É a leitura mais natural do texto atual, é o que torna a peça distinta de Lento, e — o mais importante — **não muda nenhum dos 35 feitiços prontos**, porque nenhum deles usa Carregar.

Um item que estava aberto há duas versões se resolve escrevendo uma frase que já estava implícita. Vale registrar por quê: **tensão de preço às vezes é lacuna de texto disfarçada.** Antes de mexer no número, confira se a regra diz o que você acha que ela diz.

*E na v0.26 a mesma lição pegou o mesmo item de novo.* A Restrição continuava dizendo *"você gasta um turno **concentrado**"*, e era essa palavra — só ela — que fazia Carregar e Concentração parecerem a mesma regra com dois testes diferentes. Ela saiu, e o preço não precisou de nenhum ajuste: o par Lento contra Carregar continua fechando pelos conjuntos de recurso, como esta seção já tinha resolvido.

## 5. Iniciativa

> **Iniciativa = d20 + Destreza.** Maior age primeiro. Empate se resolve pela maior Destreza; persistindo, o jogador decide antes do inimigo.

A parte que exige explicação é por que **rolada** e não fixa.

Iniciativa fixa — a ordem simplesmente sendo a Destreza — é tentadora num sistema de cinco a sete mestres: uma rolagem a menos, ordem previsível, ficha auditável. Mas ela quebra uma peça que já existe.

**A Melhoria Adianta** dá +2 na CD se você conjurar antes de qualquer inimigo agir na rodada. Com iniciativa fixa, um conjurador de Destreza alta **sempre** age antes, e Adianta vira +2 permanente por 2 pontos. Isso é exatamente o teste do bônus automático falhando: um bônus que a montagem óbvia sempre alcança não é bônus, é a linha de base com um passo a mais.

Com iniciativa rolada, Adianta é uma aposta: você paga por algo que costuma acontecer e às vezes não. O preço passa a fazer sentido.

**A conta de quanto Adianta vale:**

| sua Destreza | Destreza do inimigo | você age antes | efeito médio de Adianta |
|---|---|---|---|
| 3 | 3 | 52% | 5,2 pp |
| 4 | 3 | 57% | 5,7 pp |
| 6 | 3 | 66% | 6,6 pp |
| 3 | 5 | 38% | 3,8 pp |

O +2 na CD vale 10 pontos percentuais quando dispara, e ele dispara na maioria das rodadas mas não em todas. O efeito médio fica entre 4 e 7 pontos percentuais, por um preço Médio — **abaixo do que uma Média costuma entregar**, e vale acompanhar no playtest. Com iniciativa fixa seriam 10 pp garantidos, e aí o preço estaria errado no outro sentido.

## 6. A regra que fecha o turno

O Fundamento já tem, e ela é a regra de ouro nº 6:

> **Feitiço em Ação Bônus ou Reação só permite mais um de Classe 0 no turno.**

*Desde a v0.20 o manual escreve Classe também — a citação acima é literal.*

É a trava que impede o turno duplo de feitiço grande. Ela só funciona porque ação bônus e ação padrão são recursos separados — o que só agora está escrito.

## 7. O que esta peça deixa em aberto

- **Se ação bônus deve existir mesmo.** Ela é a mais herdada das quatro, e a que mais custa em tempo de mesa: todo turno, todo jogador pergunta "tenho alguma coisa de ação bônus?". Duas peças do Fundamento dependem dela (Rápido e Parado). Vale medir no playtest quantos turnos realmente usam uma.
- **Quantas reações por rodada.** Uma é o padrão, e quatro coisas competem por ela: ataque de oportunidade, a Melhoria Reação e as Passivas Contramedida e Reforço. Competir é bom — vira escolha. Mas se na prática ninguém nunca tiver reação sobrando, as Passivas de reação ficam mortas.
- **O valor real de Adianta** (seção 5). Entre 4 e 7 pontos percentuais de efeito médio, abaixo do que uma Média costuma entregar.

*Resolvido e tirado daqui:* o ataque de oportunidade **é ataque físico, rolado como ataque comum e pago com a Reação** — e um conjurador faz um normalmente, com soco ou arma. Conjurar na Reação continua exigindo a Melhoria Reação. A conta está na peça 4, seção 6.
