# A ECONOMIA DE ATRIBUTOS

**Fase 4, segunda peça.** Escala, criação, crescimento e teto.
Versão v0.10, corrigida na v0.22 — 06/08/2026

Números calculados, não estimados. Validador: `conferir-atributos.py`.

---

## 1. A escala

**O número é o modificador. Escala de 0 a 6. Não existe valor separado, não existe tabela de conversão.**

A alternativa — 1 a 30 com o 10 valendo 0, no molde do d20 clássico — foi descartada por três motivos, e nenhum deles é gosto:

**O sistema inteiro já foi montado sem conversão.** Ataque é `d20 + Força`. Defesa é `10 + Destreza + proteção`. Colocar um score de 1 a 30 obrigaria a inserir uma tabela de conversão em cada uma dessas contas, sem mudar nenhum resultado.

**Conversão custa caro num sistema de vários mestres.** A propriedade que a Guilda mais precisa é o mestre bater o olho na ficha e saber a chance. Um número que precisa ser traduzido antes de entrar na conta é um passo a mais para errar, e cinco a sete pessoas errando de formas diferentes.

**A granularidade que a escada de 30 compra é granularidade que este sistema não quer.** Ela existe para permitir bônus pequenos — "+2 de Força" valendo meio modificador. Um sistema com bounded accuracy declarada e poucos modificadores não tem o que fazer com essa resolução extra. O d20 clássico carrega essa escada por razão histórica: os modificadores foram inventados depois dos scores, não antes.

Para referência de leitura na mesa:

| valor | o que significa |
|---|---|
| 0 | sem preparo nenhum |
| 1–2 | pessoa comum |
| 3 | bom, e é o teto da criação |
| 4–5 | notável entre feiticeiros |
| 6 | o topo humano |

## 2. Criação

**Nove pontos entre os cinco atributos. Nenhum acima de 3.**

O arranjo padrão que sai disso é **3 · 2 · 2 · 1 · 1**, e o jogador pode redistribuir como quiser dentro da regra. Nove pontos em cinco atributos com teto de 3 produz poucas combinações legais, e isso é proposital: a criação de personagem já tem a parte longa, que é escrever a técnica. Esta etapa precisa levar dois minutos.

O teto de 3 na criação não é arbitrário. Ele é o que faz o atributo investido crescer **exatamente +3** ao longo da campanha — o mesmo ritmo da maestria, que é o que a matemática de acerto e de Teste de Resistência depende para não derivar.

## 3. Crescimento

A cada quatro níveis a partir do começo da ficha — nos níveis **6, 10, 14, 18, 22, 26 e 30**, sete marcos ao todo. A escada fecha exata: o último marco cai no nível 30.

- **Passivo:** +1 ponto de atributo e +1 de refino.
- **Escolha:** mais um ponto de atributo, **ou** mais um de refino junto de uma aptidão.

> **⚠ Esta seção é CÓPIA, e o dono é a peça 11 §3.** *Ela está desatualizada desde a v0.26, e o conserto saiu com a peça de aptidões.* O marco ganhou um **terceiro eixo, o Leque** — a linha passiva passou a dar **+1 espaço de feitiço** junto do atributo e do refino, e a escolha virou uma de três: mais atributo, mais refino com uma aptidão, ou `+1 feitiço e uma Passiva`. As três fichas de exemplo abaixo e a análise de auto-equilíbrio da seção seguinte foram calculadas com duas opções e continuam válidas **para as duas que já existiam**. O levantamento do terceiro eixo, com a conta, está no `ESTADO-ATUAL.md`.

**Teto do atributo: 6.** Teto do refino: 10.

O orçamento total de crescimento é de 7 a 14 pontos de atributo, dependendo de quantas vezes o jogador escolhe esse lado.

### Três fichas ao longo da campanha

Partindo de 3/2/2/1/1:

| escolha | nível 14 | nível 22 | nível 30 |
|---|---|---|---|
| **sempre atributo** | 6·5·2·1·1 · ref 4 · 0 apt | 6·6·5·1·1 · ref 6 · 0 apt | 6·6·6·4·1 · ref 8 · 0 apt |
| **meio a meio** | 6·4·2·1·1 · ref 5 · 1 apt | 6·6·3·1·1 · ref 8 · 2 apt | 6·6·6·1·1 · ref 10 · 3 apt |
| **sempre refino** | 6·2·2·1·1 · ref 7 · 3 apt | 6·4·2·1·1 · ref 10 · **6 apt** | 6·6·2·1·1 · ref 10 · **10 apt** |

Repare que **os três chegam ao mesmo lugar no atributo principal** — 6 — e divergem em tudo o mais. Quem foca atributo termina largo: três ou quatro atributos altos. Quem foca refino termina estreito e fundo: dois atributos altos, refino no teto e dez aptidões.

### A curva se auto-equilibra

O atributo principal chega ao teto no **nível 10 ou 14**, dependendo do caminho. Depois disso, o ponto de atributo passa a cair num secundário — ainda útil, mas menos.

Isso resolve sozinho o problema que a escolha tinha: **ela não precisa ser equilibrada nos dois extremos da campanha, porque o valor relativo dos dois lados muda com o tempo.** No começo, atributo é claramente melhor: cada ponto vai direto no que você faz. Depois do teto, refino fica claramente melhor: aptidão nova contra +1 num atributo terciário.

Ou seja, o jogador tende a **pegar atributo cedo e refino depois** sem que nenhuma regra mande fazer isso. É a curva fazendo o trabalho no lugar de uma trava.

Isso também explica por que o teto do atributo não deve crescer com o nível. Um teto que sobe junto — 4 + maestria, por exemplo — manteria o ponto de atributo sempre valioso, e a escolha ficaria travada em "atributo" a campanha inteira. O teto fixo é o que cria a virada.

## 4. Origem não dá atributo

**Recomendação: origem não mexe em número nenhum.**

Em Jujutsu Kaisen, a origem é a **fonte do poder** — nasceu com, herdou de clã, foi recipiente, foi experimento. Nada disso deixa alguém mais forte ou mais rápido. Ser recipiente não te dá Constituição; te dá um passageiro.

Amarrar atributo à origem cria o problema clássico de raça em d20: a escolha vira otimização, e nasce a origem certa para cada build. Num sistema em que o pilar é *a técnica é a identidade*, ter a origem ditando o número seria empurrar a identidade para a camada errada.

O que a origem dá, então:

- **Uma perícia da lista dela e uma livre**, mais um ofício livre — ou outra perícia no lugar dele.
- **Um Teste de Resistência treinado.** O outro vem do Caminho.
- **Um traço não numérico.** Acesso, obrigação, um contato, uma marca no corpo, alguém atrás de você.
- **Um Legado**, um só na ficha inteira.
- **O gancho de ficção** que a técnica vai usar.

*Corrigido na v0.22.* Este documento dizia que a Origem também dava a **patente inicial**, e usava o Yuta como exemplo. Ela não dá: **todo personagem começa Grau 4**. A patente é eixo social e sobe por feito. O caso do Yuta continua existindo na ficção — a instituição classifica quem ela quiser onde ela quiser —, mas patente por Origem na criação criaria a origem que começa na frente, que é o mesmo problema que este documento evita ao não dar atributo. O catálogo está na peça 9.

Se em playtest a origem parecer leve demais, o conserto barato é dar **+1 num atributo à escolha do jogador** — o que preserva a origem como sabor e não cria origem ótima por build. O que não recomendo é +1 num atributo *específico* por origem.

## 5. O que este documento fecha

A premissa de que a peça anterior depende:

> Atributo investido: **3 na criação, 6 no teto — cresce +3.**
> Maestria: **1 no nível 2, 4 no nível 30 — cresce +3.**

Os dois batem. A matemática de acerto e de Teste de Resistência continua sem deriva.

E as duas escadas se encaixam: a maestria sobe nos marcos de **nível 10, 18 e 26** — um marco sim, um não, começando pelo segundo. O jogador nunca tem um marco vazio, e nunca tem dois ganhos grandes no mesmo.

| marco | nv 6 | nv 10 | nv 14 | nv 18 | nv 22 | nv 26 | nv 30 |
|---|---|---|---|---|---|---|---|
| atributo + refino + escolha | sim | sim | sim | sim | sim | sim | sim |
| maestria sobe | — | **sim** | — | **sim** | — | **sim** | — |

## 6. Em aberto

- **Se Força precisa de um segundo trabalho** para não virar depósito.
- **Se a criação deve permitir trocar pontos por uma desvantagem**, no molde de comprar um atributo negativo para subir outro. Fica de fora por ora: agrega pouco e custa clareza.
- **Se o teto de 3 na criação ainda aguenta**, agora que Constituição virou a maior alavanca de sobrevivência do sistema. Nove pontos com teto 3 fazem "3 em Constituição" ser barato demais de alcançar.

*Resolvidos e tirados daqui:* quantos pontos de perícia e como funciona o treino — **o Caminho dá duas fixas e quatro livres; a Origem dá uma da lista dela, uma livre e um extra à escolha; e o treino é binário** (peças 7 e 9). E o treino em Teste de Resistência: **um da Origem, um do Caminho**.
