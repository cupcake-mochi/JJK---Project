# ARQUITETURA DO SISTEMA

**Fase 3 — esqueleto.** O que existe, o que falta, e o que cada peça que falta precisa cumprir.
Versão v0.4, sincronizada na v0.15, na v0.22, na v0.24, na v0.25 e na v0.26 — 10/08/2026

> Este documento foi escrito antes da Fase 4 e ficou para trás em quatro pontos, todos corrigidos aqui: os marcos de progressão (eram 4/8/12…, hoje são 6/10/14…), a escada da patente (eram sete degraus, hoje oito), o nome do eixo de tamanho de feitiço (**Classe**, não *Escala* nem *Potência*) e o problema 1 da seção 4.3, que a v0.10 resolveu.

Este documento não tem número nenhum de propósito. Ele responde *que peças o sistema tem e como elas se encaixam*, não *quanto cada uma vale*. Número é Fase 4.

---

## 1. O que o Fundamento já resolve

O manual v7.20 é um subsistema fechado e validado. Ele cobre:

| Área | O que o Fundamento entrega |
|---|---|
| Identidade do personagem | Técnica inata escrita na criação: Descrição, Regra, Famílias, Selo, Passivas |
| Poder ativo | Feitiços montados por orçamento de pontos, com Melhorias e Restrições |
| Pico de poder | Liberação Máxima (nível 10) e Técnica Máxima (nível 17) |
| Economia de recurso | PE, com custo amarrado ao tamanho do feitiço |
| Dano e cura | Dados de dano, tipos, cura por Forma |
| Dano de alma | Integridade, com estágios e recuperação |
| Condições | Menores e Maiores, compradas como Melhoria |
| Arbitragem | Oito regras de ouro e um checklist de aprovação de oito perguntas |
| Preparo do mestre | Vida por nível, dano de inimigo por faixa, corte de PvP |

E ele traz o que quase nenhum sistema caseiro tem: **contrato de invariantes com validador**. `pac7.py` confere os 35 feitiços prontos e todos os exemplos do texto; `v7.py` roda a busca exaustiva. Isso não é acessório — é o que torna barato mexer no resto.

**O que isso significa para a arquitetura:** o Fundamento é o coração e não se toca sem motivo forte. Tudo que vier depois se encaixa em volta dele, respeitando os invariantes que ele já declarou.

---

## 2. A colisão do Grau, e os três eixos

O Fundamento usa **Grau** para o tamanho de um feitiço. Jujutsu Kaisen usa **grau** para a patente do feiticeiro. São dois significados para a mesma palavra dentro do mesmo material.

E a colisão não é simétrica. O Grau-tamanho está entranhado no *manual*: 76 tabelas, os scripts, o gerador. O grau-patente está entranhado na *cabeça de todo mundo* — a Guilda inteira já fala "grau especial" há anos porque é o termo da obra. Fighting entrenchment funciona contra um manual; não funciona contra o vocabulário de uma comunidade.

**Recomendação: renomear o Grau-tamanho, não a patente.** É a mudança mais cara em linhas de texto e a mais barata em atrito social, e o seu gerador com validador faz o retrabalho ser mecânico em vez de arriscado — muda o nome, roda `pac7.py`, gera o manual de novo.

**Decidido: Classe.** *"Um feitiço de classe 3"*, *"um feitiço de terceira classe"*. Sai fácil falado, e soa como classificação burocrática — o que combina com uma sociedade jujutsu que registra, cataloga e emite parecer sobre tudo.

Consequência obrigatória: **o chassi não pode se chamar classe.** Ver 4.2.

Duas alternativas ficam registradas caso Classe incomode depois: **Volume** (termo da própria obra, e neutro quanto ao que você faz com a energia) e **Fluxo** (duas sílabas, também vocabulário da obra). Enquanto o manual não for regenerado, trocar custa um find/replace e uma rodada do validador.

### 2.1 · Nota de método sobre colisão

Ao checar um nome candidato contra o manual, separe **termo definido** de **prosa solta**. As palavras *caminho*, *papel*, *função* e *classe* aparecem no Fundamento uma ou duas vezes cada, sempre em frase corrida — "eles não são todos iguais em papel", "se a sua mesa tem uma classe que bate em vez de conjurar". Isso não é colisão; vira colisão quando a palavra carrega definição. Uma reescrita de frase resolve.

Livres de qualquer uso no manual: **vocação**, **estilo**, **postura**, **trilha**, **perfil**.

Com isso o sistema passa a ter **três eixos separados**, e essa separação é a resposta ao que você levantou sobre o Yuta e o Itadori:

| Eixo | O que mede | Quem determina | Como se move |
|---|---|---|---|
| **Nível** | poder mecânico do personagem | a ficha | XP tabelado, igual em toda mesa |
| **Grau** (patente) | o que a instituição reconhece | a ficção, e os mestres | promoção, feito, política |
| **Classe** (ex-Grau) | tamanho de um feitiço | o Nível libera | automático, pelo Nível |

O Yuta é **Grau especial, Nível baixo**: a instituição o classificou no topo por causa do que ele carrega, e ele ainda não sabe usar. O Itadori é o contrário no começo — poder real, patente nenhuma, porque a instituição não o reconhece e prefere não reconhecer.

**O que a patente compra, já que não compra poder:** acesso (missão, arquivo, lugar), autoridade (mandar em quem tem patente menor), obrigação (o que você é convocado a fazer) e risco (que tipo de maldição mandam pra cima de você). É um eixo social, e é onde a Guilda inteira ganha textura sem inflar número nenhum.

---

## 3. Os buracos

Ordenados por carga: quanto o resto do sistema depende deles. Os quatro primeiros são estruturais — sem eles, o Fundamento não fecha, porque ele já *cita* coisas que ninguém definiu.

### Carga alta — o Fundamento já depende disso

**3.1 · De onde vem o número — RESOLVIDO na v0.9,** em `03-mecanica/01-atributos-acerto-defesa.md`. O Fundamento fala em "rolagem de acerto", "Teste de Resistência", "CD" e "defesa", e não diz de onde sai o bônus de nenhum. Precisa existir uma camada de atributo ou equivalente. A trava: qualquer que seja a forma, ela tem que respeitar bounded accuracy — se o bônus cresce sem teto, a matemática de inimigo do Fundamento quebra.

**3.2 · Economia de ação.** Ação padrão, ação bônus, reação e movimento aparecem em dezenas de Melhorias e Restrições. Nunca foram definidos. Isso é o esqueleto do turno e mexe em preço: o valor da Restrição "Parado" depende de quanto movimento vale.

**3.3 · Defesa e iniciativa.** "+2 de defesa" existe como Melhoria sem que defesa exista como número. Iniciativa nunca aparece.

**3.4 · O que se rola fora de combate.** Perícia, teste social, investigação. O Fundamento tem a Forma Efeito para feitiço fora de combate, mas nada para o personagem sem feitiço na mão.

### Carga média — o sistema roda sem, mas fica manco

**3.5 · O chassi.** Sua ideia: classe como capa, técnica como identidade. Ver seção 4.

**3.6 · Combate sem feitiço.** O Fundamento já antecipa isso numa nota — "se a sua mesa tem uma classe que bate em vez de conjurar, o dano dela precisa ficar na coluna Rotina, e ela não deve ter Liberação Máxima". A trava está escrita; falta a regra.

**3.7 · Criação de personagem, do começo ao fim.** Hoje existe a criação da *técnica*. Falta a ordem dos passos de tudo: o que se escolhe primeiro, o que a ficha pede, quanto tempo leva.

**3.8 · Descanso e recuperação.** "Descanso longo" devolve Integridade e é citado várias vezes. Nunca foi definido.

**3.9 · Progressão fora de feitiço.** A tabela de progressão dá Escala, feitiço conhecido e Passiva. Não dá mais nada. Se existir atributo e perícia, eles precisam de uma linha nessa tabela.

### Carga baixa — pode esperar sem risco

**3.10 · Equipamento e armas amaldiçoadas.** JJK tem, e é um eixo de poder paralelo ao da técnica. Perigoso justamente por isso: entra depois, com teto declarado, ou vira a segunda economia que ninguém balanceou.

**3.11 · Bestiário.** Sai da matemática de inimigo que o Fundamento já tem.

---

## 4. A estrutura do personagem

A ordem proposta, em cinco camadas:

**Origem** → **Chassi** → **Técnica** → **Refino e Aptidões** → **Pactos**

Cada camada responde uma pergunta diferente sobre o personagem, e é isso que faz a estrutura funcionar: nenhuma delas responde a mesma coisa duas vezes.

| Camada | A pergunta que ela responde |
|---|---|
| Origem | de onde vem o seu poder |
| Caminho | que lugar você ocupa numa equipe |
| Técnica | o que só você faz |
| Refino e Aptidões | quão bem você controla energia amaldiçoada |
| Pactos | o que você trocou por poder |

### 4.1 · Origem

De onde vem o poder: nasceu com, herdou de clã, foi recipiente, foi experimento, fez pacto antes de saber o que era. É a camada mais curta de escrever e a mais barata em regra.

*Corrigido na v0.22:* este parágrafo dizia que a Origem era **o lugar natural da patente inicial**, com o Yuta como exemplo. **Não é** — todo personagem começa Grau 4, e a patente sobe por feito. O caso do Yuta continua na ficção, porque a instituição classifica quem ela quiser; o que sai é a patente ser produto da Origem na criação, que criaria a origem que começa na frente. O catálogo de Origens está em `03-mecanica/09-origens.md`.

### 4.2 · Caminho

O chassi, com nome próprio. *Classe* está reservada para o tamanho do feitiço (seção 2), e a mesma palavra não pode significar duas coisas.

**Caminho**, com **Trilhas** dentro dele. Acomoda a estrutura de trilha sem inventar hierarquia nova, e não colide com nada no Fundamento. Alternativas livres, se incomodar: Vocação, Estilo.

Sua ideia — o Caminho como capa e a técnica como identidade, no formato de trilha e não de catálogo de talento por nível — está certa e conversa direto com o primeiro pilar. Mas ele precisa de uma trava, ou vira a segunda fonte de identidade e briga com a técnica.

A trava: **o Caminho não dá poder novo, ele muda o que o seu poder alcança.**

Um Caminho de linha de frente não ganha "mais dano". Ele ganha fazer inimigo olhar pra ele, e continuar de pé. Um Caminho de apoio não ganha cura — cura é Forma de feitiço, e quem tem Amparo fechado nunca vai curar. Ele ganha alcance sobre o efeito que já produz. O Caminho mexe em **posicionamento, alvo, duração e recuperação**, nunca em número de dano.

Assim dois personagens do mesmo Caminho com técnicas diferentes continuam sendo coisas completamente diferentes na mesa. E o Caminho vira o lugar natural para o **combatente sem técnica ofensiva** (3.6) existir sem quebrar a coluna Rotina, porque ele não compete no eixo de dano de feitiço.

Escolhido na criação, com poucas escolhas de Trilha ao longo dos níveis.

### 4.3 · Refino e Aptidões

O eixo do **controle**, separado do eixo do **poder**. É a distinção que a obra faz o tempo todo: o Gojo diz que qualquer feiticeiro pode aprender Kokusen, e quase nenhum consegue. Poder é quanto você tem; refino é quanto você não desperdiça.

Refino sobe a cada quatro níveis, junto de atributo, e naquele nível o jogador escolhe onde recebe o bônus: refino (sobe o nível de refino e ganha uma aptidão) ou atributo (recebe mais atributo além do passivo).

**Isso está certo na intenção e tem quatro problemas de estrutura.** Todos têm conserto barato.

**Problema 1 — RESOLVIDO na v0.10, e não pelo conserto proposto aqui.** O diagnóstico era: "uma aptidão + um degrau de refino" contra "um pouco mais de atributo" não é escolha equilibrada se as aptidões forem coisas como Energia Reversa. Ninguém escolheria atributo.

O que resolveu foi o **teto fixo de 6 no atributo**. O atributo principal chega ao teto no nível 10 ou 14; depois disso o ponto de atributo cai num secundário e vale menos, enquanto uma aptidão nova continua valendo o mesmo. O valor relativo dos dois lados se inverte sozinho no meio da campanha, sem que nenhuma regra mande. A conta está em `03-mecanica/02-economia-de-atributos.md`, seção 3.

Os dois consertos que estavam propostos aqui ficam registrados porque a ideia continua boa por outro motivo — **aptidões em degraus de peso**, com o degrau amarrado ao refino atual, é o que impede Energia Reversa de estar à venda no refino 2. Mas isso é controle de acesso, não conserto de balanço.

**Problema 2 — aptidões são uma segunda economia de poder, e ela não tem teto.** Este é o risco maior da estrutura inteira, e é o mesmo que eu marquei para equipamento na seção 3.10.

O Fundamento tem orçamento, teto e validador. Barreira Simples, Cortina, Domínio Simples, Cobrir-se de energia, Canalizar energia e Projetar energia são todas coisas que acontecem em combate — e nenhuma delas passa pelo orçamento do Fundamento. Se elas produzirem dano, ou escalarem com o nível, o sistema passa a ter duas fontes de poder e só uma foi balanceada.

A trava proposta: **aptidão não produz dano e não escala com nível.** Aptidão é binária — você consegue ou não consegue fazer aquilo — e o refino governa **confiabilidade e custo**, não potência. Projetar energia dispara energia crua; o dano dela é fixo e baixo, e existe para quem ficou sem PE, não para competir com feitiço. Cobrir-se de energia dá uma defesa que não cresce. Assim as aptidões vivem inteiras fora da economia do Fundamento e não precisam ser rebalanceadas toda vez que um preço mudar lá.

**Problema 3 — RESOLVIDO. A progressão é passiva e por escolha ao mesmo tempo.** A cada quatro níveis o personagem ganha refino e atributo de graça, e escolhe em qual dos dois recebe um bônus a mais. Escolher refino sobe outro degrau e concede uma aptidão; escolher atributo dá mais atributo.

Com teto 10 e começo em 1, a curva se desenha sozinha. Os marcos são os da v0.10 — **6, 10, 14, 18, 22, 26 e 30**, contados a partir da ficha que começa no nível 2.

> **A tabela das três rotas SAIU DAQUI na v0.104, e hoje ela mora na peça `03-mecanica/11-aptidoes-e-refino.md` §3.** *Ela era a última fonte de progressão do projeto fora de uma peça de regra, e este é documento de projeto: aqui a ideia nasce, lá ela mora e um validador alcança ela.* **Os gates da seção 5 daquela peça são esta curva lida em três colunas.**

**A trava que faz isso fechar:** quando o refino já está no teto, **escolher refino ainda concede a aptidão**. Sem essa linha, o especialista desperdiça duas escolhas depois do nível 22. Com ela, nada se perde e a decisão degrada sozinha para "aptidão ou atributo" no fim do jogo — que é uma comparação limpa.

**Uma consequência a decidir, não um defeito:** quem nunca escolhe refino termina com **zero aptidões**. Ele continua funcionando, porque Cobrir-se de energia e Canalizar energia vêm de graça no refino 1 (problema 4), mas nunca terá Barreira Simples nem Energia Reversa. Se a intenção for que todo feiticeiro tenha algumas, solte uma aptidão passiva em marcos de refino — 3 e 6, por exemplo — e deixe a escolha para as caras.

**Problema 4 — o que é básico não deveria custar slot.** Você mesmo classificou Cobrir-se de energia e Canalizar energia como mecânicas básicas de qualquer feiticeiro. Se são básicas, cobrar uma aptidão por elas é vender o que já devia vir junto. O desenho mais limpo: **todo feiticeiro recebe as duas no refino 1**, e as aptidões *melhoram* o que já existe. Isso libera os slots para o que é de fato especial e resolve o problema de o personagem novo parecer incompleto.

Duas notas menores. **Anti-Domínios são quatro coisas de tamanhos muito diferentes** — Pétala, Domínio Simples, Extensão de Domínio e Cesta Oca de Vime não pertencem ao mesmo degrau e não deveriam vir na mesma compra; é trilha, não item. E a **aptidão criada pelo jogador** (Energia Áspera do Hakari, Punho Divergente do Itadori) precisa da mesma pergunta de calibragem que o Fundamento usa para o Efeito Próprio: *em quantas cenas por arco isso importa?* — com a mesma regra de errar sempre para o mesmo lado.

### 4.4 · Pactos

A última camada estrutural, e a mais perigosa de escrever solta. Pacto em JJK é a mecânica que permite qualquer coisa desde que o preço seja real — é o Efeito Próprio do sistema inteiro, um nível acima.

A trava é a mesma que o Fundamento já usa para a Regra Própria: uma frase, verificável pela mesa, simétrica, sem dano direto, com limite. Sem isso, pacto vira a porta por onde todo desequilíbrio entra, e entra com autorização.

### 4.5 · A ordem, e o argumento contra ela

A ordem Origem → Chassi → Técnica → Refino → Pactos é boa para **ensinar**: as duas primeiras camadas são rápidas e dão andaime antes da parte difícil.

O argumento contrário, que vale considerar: a técnica é a identidade, e escolher o chassi antes ancora o jogador num papel de equipe antes de ele saber o que o personagem faz. Quem escolhe "eu sou o tanque" e depois escreve a técnica tende a escrever uma técnica de tanque — e o pilar 1 diz justamente que a técnica é que deveria mandar.

Um meio-termo que funciona: **escrever a Regra da técnica logo depois da Origem**, ainda na frase única, e deixar o resto da técnica para depois do chassi. Assim o jogador escolhe o chassi já sabendo o que a técnica dele é, mas ainda não gastou a parte longa da criação.

---

## 5. As travas de mundo compartilhado

Estas não são um subsistema — são regras que atravessam todos eles. Vieram da pesquisa da Fase 1 e valem para tudo que for escrito daqui pra frente.

1. **XP tabelado, nunca marco narrativo.** Marco quebra quando cada mestre tem senso de ritmo diferente.
2. **Recompensa no mesmo passo em toda mesa**, ou o jogador aprende qual mesa paga melhor.
3. **Ficha aprovada antes de entrar em jogo**, com a técnica lida por alguém que não seja o dono.
4. **Registro entre mesas**: o que aconteceu, quem estava, o que mudou no mundo.
5. **Guia do mestre com a matemática exposta** — conta de encontro, ritmo de recompensa, regra de morte. Sem isso a consistência não sobrevive ao terceiro mestre.
6. **Morte declarada por mesa, antes de começar.** Tem mesa de roleplay e tem mesa contra um Sukuna. O mestre declara o registro da mini-campanha na abertura.

**Sobre o peso do modo não letal — decidido:** não vira regra. O peso vem de consequência no mundo: a falha num teste faz você não notar o que era crucial, a decisão cobra dos NPCs e dos arredores, e isso é arbitragem de mestre apoiada em perícia e rolagem mundana. É punitivo sem ser letal.

Vale registrar por que isso **não** viola o filtro do multi-mestre, porque parece violar: o filtro existe para impedir discricionariedade **nos números** — quanto de XP, quanto de recompensa, quanto de poder. Discricionariedade **na ficção** é o trabalho do mestre e não atravessa mesas: o personagem sai da campanha do mestre A com a mesma ficha, independente de quantos NPCs ele decepcionou lá. Consequência narrativa não é portátil, e por isso não precisa ser padronizada.

O que isso obriga: o livro do mestre precisa ter essa seção escrita. Não como regra, como orientação — o que serve de consequência, como escalar sem virar castigo, e como não deixar a mesa não letal sem aposta nenhuma.

---

## 6. Ordem de construção proposta

Os quatro buracos de carga alta primeiro, porque o Fundamento já depende deles e porque eles definem os preços de tudo:

1. De onde vem o número (3.1) e defesa (3.3) — andam juntos
2. Economia de ação e iniciativa (3.2, 3.3)
3. Teste fora de combate (3.4)
4. Chassi (3.5) e combate sem feitiço (3.6)
5. Criação de personagem completa (3.7) — só depois que 1 a 4 existirem, porque ela é a soma deles
6. Descanso (3.8) e progressão fora de feitiço (3.9)

O resto entra quando fizer falta.

---

## 7. A escada da patente

Oito degraus, seguindo a obra e incluindo os semi. O semi-especial entrou na v0.7:

**Grau 4 · Grau 3 · Semi-grau 2 · Grau 2 · Semi-grau 1 · Grau 1 · Semi-especial · Grau especial**

Semi-especial é extensão deliberada — pelo que se sabe não existe no cânone, e é o limbo dramático mais rico da escada.

Oito é mais do que o normal para uma escada social, e aqui funciona justamente porque **a patente não carrega número mecânico**. Ela compra acesso, autoridade, obrigação e risco. Uma escada longa dá textura sem inflar nada — e os semi-graus são o degrau em que a instituição já reconheceu você mas ainda não te deu o que vem junto, que é um lugar dramático bom.

---

## 8. O que este documento não resolve

- ~~**O nome do sistema.**~~ **`Projeto - M`, decidido na v0.94.**
- **Se o generalista deve ter alguma aptidão garantida** (seção 4.3). Hoje ele termina com zero.
- **Os degraus de peso das aptidões**, amarrados ao refino atual. Não é mais conserto de balanço — o teto fixo resolveu isso na v0.10 —, mas continua sendo o controle de acesso que impede Energia Reversa no refino 2.
- **Onde a Regra da técnica entra na ordem de criação** (seção 4.5).
