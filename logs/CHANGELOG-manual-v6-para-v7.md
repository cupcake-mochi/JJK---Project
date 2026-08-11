# O que mudou — v6 → v7

## Lento e Aquecer, reprecificados

**Lento passou de Leve para Média.** O argumento é de dominância: Parado tira só a ação de movimento, Lento é Ação Completa e tira movimento, ação bônus e ação padrão. Lento **contém** Parado. Com os dois devolvendo a mesma coisa, ninguém escolhia Lento por razão mecânica — dor estritamente maior pelo mesmo troco. Ele só sobrevivia por sabor.

Isso mexeu em seis feitiços prontos, todos pra cima, e nenhum estourou teto:

| Feitiço | Antes | Agora |
| :-- | :-: | :-: |
| Palma Trovejante (G2) | 4d8 = 18 | **5d8 = 22** |
| Lança Negra (G2) | 5d8 = 22 | **6d8 = 27** |
| Julgamento Vertical (G4) | 6d8 = 27 | **8d8 = 36** |
| Vala Comum (G5) | 7d8 = 31 | **9d8 = 40** |
| Fim de Turno (G5) | 10d8 = 45 | **12d8 = 54** |
| Sentença Final (Liberação G5) | 15d8 = 67 | **17d8 = 76** (teto da Liberação é 20d8) |

A Lança Negra virou um exemplo melhor do que era: com Lento devolvendo 2 e Fura custando 2, ela sai com o **dano cheio do Grau e a Fura de graça**. Como ela é o primeiro exemplo do manual, aproveitei pra explicitar ali a regra de ouro nº 1 — Restrição paga Melhoria — e a trava logo em seguida: 6 pontos continuam sendo o máximo de um Grau 2 contra um alvo, com ou sem Restrição.

A Rachadura ficou com o caso oposto e igualmente didático: o Lento devolveria 3, mas a Linha só custou 2, e o terceiro ponto some. Anotei isso na tabela.

**Aquecer passou de Média para Leve.** É a única das quatro Restrições de frequência cujo custo desaparece depois da rodada 1 — e o personagem tem outros feitiços e Grau 0 pra cobrir aquele turno. Comparada com Dívida (dobra o PE do próximo feitiço, dói toda vez) ou Uma Vez (some da cena inteira), ela era a melhor das quatro por larga margem devolvendo Média. Nenhum dos 35 prontos usa Aquecer, então o impacto foi zero.

O catálogo saiu equilibrado da troca: Lento subiu, Aquecer desceu, e a contagem de Leves e Médias ficou idêntica.

**Uma tensão que sobrou, pra você decidir depois:** com Lento em Média, **Carregar** (também Média) fica na mesma faixa — e Carregar dói mais, porque consome dois turnos e ainda arrisca perder o feitiço se você tomar dano. Não é dominância pura como era Lento/Parado (Carregar tem a flexibilidade de ser pré-carregado num turno morto), mas está apertado. Como Restrição não pode devolver Pesada sem estourar o fecho de 2 × Grau, a saída, se incomodar, seria dar um upside ao Carregar em vez de subir o preço.

## Restrição Própria

O catálogo tinha **Efeito Próprio** (Melhoria customizada, "o mestre decide o custo") mas nenhum equivalente do outro lado da moeda. Agora tem, no fim da seção 4, e ela herda tudo: escrita com o mestre antes da sessão e nunca no meio dela, vale só pro feitiço onde nasceu, conta no limite de duas Restrições, e obedece as travas de sempre (precisa ser apontável pela mesa, não pode cobrar o que a outra Restrição já cobra, não pode repetir o que o Selo já obriga). Se ela limita *quando* o feitiço sai, entra na trava de frequência junto com Uma Vez, Condicional, Aquecer e Dívida.

Duas decisões que precisei tomar, e o porquê:

**Ela devolve Leve ou Média, nunca Pesada.** Fui conferir o catálogo e descobri que *nenhuma* das 18 Restrições existentes devolve Pesada — e isso não é acaso. Duas Médias somam exatamente 2 × Grau, que é exatamente o teto de devolução, em todos os sete Graus. Uma Restrição Pesada estouraria esse fecho sozinha. O manual agora diz isso na abertura da seção 4, e o pac7.py ganhou a trava: se alguém tentar criar uma Restrição Pesada, o script acusa. Se a dor parece valer mais que uma Média, são duas Restrições disfarçadas de uma.

**Na dúvida, Leve.** A régua de preço é a mesma pergunta da Condicional, invertida: em quantas cenas isso vai realmente atrapalhar? Menos de uma a cada três = Leve; metade ou mais = Média; nunca atrapalha = não devolve nada e não vale como Restrição. E aí aparece uma simetria bonita que virou box no manual: Efeito Próprio na dúvida é **Pesada**, Restrição Própria na dúvida é **Leve**. Os dois erram pro mesmo lado — o que não infla o feitiço.

## Banca: a Técnica Máxima saiu

O jackpot era autocontraditório: custava 5 × maior Grau de PE (25 no nível 17, o custo mais alto do sistema) pra te dar três rodadas de feitiço sem PE. Você gastava energia pra economizar energia, e ainda ganhava cura por cima. Removido.

Efeito colateral bom, de consistência: os três Fundamentos prontos agora param todos no mesmo lugar — Descrição, Regra, Famílias, Selo e Passiva, que é exatamente o que se escreve na criação de personagem. Liberação Máxima e Técnica Máxima não pertenciam ali, porque só chegam nos níveis 10 e 17 e são escritas na hora. O manual agora diz isso explicitamente na abertura da página. O orçamento da Banca passou a morar inteiro na Regra Própria dela, que é onde a conta fecha de qualquer jeito.

## Sobre as referências a Jujutsu Kaisen

Varri o manual: **não existe nenhuma menção** a Hakari, Higuruma, ou a Banca e Sentença serem adaptações de alguém. Elas sempre foram apresentadas como Fundamentos originais de exemplo, então não havia nada a remover. A única referência a JJK no manual é a tabela **Selos de Jujutsu Kaisen** na seção 1 — que é uma lista de exemplos de *Selo* (Nobara, Todo, Inumaki, Megumi, Mahito, Choso, Nanami), não de Fundamento. Deixei como está, já que ela ensina o conceito de Selo por comparação e não afirma adaptação nenhuma. Se quiser que ela saia quando o grimório de técnicas adaptadas existir, é uma linha em `partB.js`.

## Controle: o degrau da metade saiu

O gatilho da v6 era "dano final até metade do teto: +1 rodada; até um quarto: também CD +2". O problema é que **Condição Menor sozinha dá exatamente 2 × Grau, que é exatamente metade do teto, em todos os sete Graus**. Condição Maior sozinha dá menos ainda. Ou seja: qualquer feitiço que comprasse Controle e não fizesse mais nada já ganhava a rodada extra de graça. O degrau não era escolha, era a linha de base — o mesmo defeito do Selo, num lugar diferente.

O gatilho novo:

  - **Dano final até um quarto do teto** (1 × Grau): os efeitos de Controle duram uma rodada a mais.
  - **Dano final zero** — o feitiço gastou o orçamento inteiro em Controle: além da rodada extra, a CD sobe +2.

Agora uma condição sozinha não ganha nada. Pra alcançar o primeiro degrau é preciso duas peças de Controle (ou uma Maior mais outra coisa cara), e pro segundo o feitiço precisa sair sem um único dado. Rodando todas as montagens legais de Controle no Grau 5: **45% não ganham nada, 48% pegam a rodada extra, 7% chegam no CD +2** — o bônus voltou a ser uma decisão de montagem, com um topo raro.

**Feitiços prontos que mudaram de resultado:**

| Feitiço | Dano | Antes | Agora |
| :-- | :-: | :-- | :-- |
| Palma Trovejante (G2) | 4d8 | Derrubado por duas rodadas | **uma rodada** |
| Domo de Gelo (G3) | 5d8 | terreno por duas rodadas | **uma rodada** |
| Vala Comum (G5) | 7d8 | Derrubados por duas rodadas | **uma rodada** |
| Prisão de Sombras (G4) | 4d8 | +1 rodada e CD +2 | **só +1 rodada** (4d8 = 1/4 exato do G4) |
| Rede (G3) | 0d8 | +1 rodada e CD +2 | **inalterada** — é o exemplo de dano zero |
| Muralha (G4) | 6d8 | +1 rodada | nada (o bônus nunca importou ali: Barreira já dura 1 minuto) |

Efeito colateral bom: a nota da tabela de **Ampliar** virou lição. A Palma Trovejante sai com metade do teto em todo Grau — a proporção é constante — então ela demonstra que Ampliar sobe o número sem mudar a natureza do feitiço: quem não alcançava o bônus continua sem alcançar.

## A escala do Grau, apresentada uma vez

O texto repetia "de 1 a 5" em dois lugares como se fosse a regra, e só o glossário dizia 0 a 7. Agora a seção de abertura tem uma tabela **A escala do Grau** com os três papéis (0 = o feitiço grátis que não se monta · 1 a 5 = os montados, níveis 1–20 · 6 e 7 = faixa lendária, 21–30), e daí em diante o corpo do manual só diz "o Grau". A tabela de Graus ganhou uma frase explicando a coluna Nível, e o passo 1 da montagem virou "escolha o Grau, até o maior que o seu nível liberou" — que é a regra real, já que ninguém escolhe Grau livremente.

## Selo sem bônus

O **+1 ponto no Grau 2+ saiu**. Todo Fundamento é obrigado a ter Selo, então o bônus era poder universal embutido: um número a mais pra todo mundo lembrar, zero decisão envolvida. E tinha um detalhe pior — **a matemática validada nunca contou com ele**. Nenhum dos 35 feitiços prontos usa o ponto do Selo, e a busca exaustiva do v6.py nunca modelou esse ponto extra. O texto prometia um orçamento que o modelo não cobria; remover alinhou os dois sem mexer em nenhum número conferido.

O que ficou do Selo: a identidade (a coisa que a mesa vê ou ouve toda conjuração) e a trava da seção 4 — **Restrição que o Selo já obriga não devolve ponto**. O manual agora diz isso com todas as letras: "o Selo não mexe em ponto nenhum: não custa, não devolve e não dá bônus."

**Isso fecha o item aberto "Selo com preço"** da rodada anterior.

## Técnica Máxima esclarecida

Regra igual, texto novo. O problema da v6 era jogar três números na mesa sem dizer o papel de cada um: 24d8 de dano, "8 pontos de Melhorias de graça" e 25 de PE — três valores que não conversam, e o leitor tentava derivar um do outro. A seção 7 agora separa num box ("Três números, três papéis"):

  - **O dano é fixo** por faixa (24/28/32d8). Não se compra dado, não se vende dado, Restrição não entra.
  - **Os pontos de montagem** (8/8/12) são um orçamento à parte que compra só Forma e Melhorias, **nos preços do seu maior Grau** (na faixa 17–20, preços de Grau 5: Leve 3 · Média 5 · Pesada 8). Projétil e Toque são de graça; as outras Formas custam do orçamento. Sobra se perde — não vira dado. Efeito que escala com Grau (Fura, por exemplo) usa o seu maior Grau.
  - **O PE tem fórmula própria**: a Técnica não tem Grau, então não custa 3 × Grau — custa **5 × o maior Grau** (25/30/35).

Os dois exemplos agora mostram a conta em vez de dizer "(grátis)": O Fim da Linha gasta Linha 3 + Muito Longe 5 = **8 dos 8 pontos**; Ponto Final gasta 5 e perde 3. O pac7.py confere essas montagens junto com o resto.

## Reescrita completa do manual

A pedido: escrita de manual de RPG, foco em compreensão. O que mudou na prática:

  - **Nova ordem de seções.** A Liberação Máxima saiu de dentro de "Montar um feitiço" e virou a seção 6, colada na Técnica Máxima (7). O sumário agora espelha as cinco peças da ficha: Fundamento (1) → feitiços (2–5) → Liberação (6) → Técnica Máxima (7). Regras de ouro, Progressão, Feitiços prontos e Mestre viraram 8–11.
  - **Exemplo guiado na seção 2.** O Corte Medido, primeiro feitiço da Régua, montado passo a passo com a conta aparecendo — inclusive o desconto de Família Livre funcionando (Fura de 2 por 1) e a ficha preenchida no final. É também a ponte com a seção 1: a Régua é criada lá, usada aqui.
  - **Voz de manual.** Parágrafos completos no padrão regra → explicação → exemplo. Os aforismos soltos viraram texto corrido (o único que sobreviveu, como resumo e não como regra inteira: "perceber é Livre, interferir é feitiço").
  - **Box de erros comuns** na seção 2 (devolução sem Melhoria pra pagar, Restrição "virando" dado, duas Restrições de frequência).
  - **Checklist de criação** abrindo a seção 1: as cinco coisas que se escrevem no nível 1.
  - Forma Efeito agora diz explicitamente o que os pontos fazem lá (compram Melhoria; sobra não vira nada — a escala vem do Grau).
  - O manual foi de 36 pra 42 páginas; a diferença é explicação e exemplo, não regra nova.

## Erros herdados da v6, corrigidos

  - **A tabela de Ampliar esquecia o Lento da Palma Trovejante.** Dizia 3d8/4d8/7d8 nos Graus 2/3/5; com a devolução do Lento entrando na conta (como entra no feitiço pronto), o certo é **4d8/6d8/10d8**. Em todos os três Graus o dano cai exatamente na metade do teto, então o bônus de Controle (+1 rodada de Derrubado) continua valendo — a tabela nova mostra a coluna do Lento.
  - **Fio Preso** dizia "por uma semana", contradizendo a regra da própria seção 5 (Fica sobe a duração um degrau). Agora: **até alguém desfazer**.
  - **"Cura não pode ser Forçada"** — Forçar morreu na v6 e a frase passou despercebida. Virou "não existe Liberação Máxima de cura".
  - **Regra explícita nova:** Melhoria que sobe mais degraus do que a escada tem **para no último degrau**. Era o que O Fim da Linha já assumia pra chegar nos 60 m (18 + três degraus estoura a escada de Linha); agora está escrito na seção 2.

## O que não mudou

A economia inteira: 3 × Grau de pontos, teto 4 ×, devolução 2 ×, preços Leve/Média/Pesada, PE, limites de Melhoria por Grau, as **montagens dos 35 feitiços prontos** (nenhum foi remontado — o que mudou em seis deles foi só a duração do efeito de Controle, consequência da regra nova), as 3 Liberações de exemplo, curvas de vida e letalidade, Integridade, PvP, inimigos. O pac7.py monta tudo isso de novo — mais os exemplos novos do texto — e fecha com "TUDO OK".

## Fontes

  - `gerador-do-manual/`: partA–F reorganizados pra espelhar a nova ordem (o COMO-USAR tem o mapa novo). Linha de tabela e caixa de destaque não racham mais entre páginas (cantSplit no helpers).
  - `matematica/`: v6.py → v7.py (economia idêntica, cabeçalho atualizado), pac6.py → pac7.py (agora confere também tutorial, Ampliar, Técnicas Máximas, PE das Liberações, tabela de cura e conversão d6/d12, e acusa erro se qualquer número sair da linha).

## Pra olhar no playtest

  - **Os 8 pontos de montagem da faixa 21–25 compram menos** que na 17–20, porque os preços sobem com o Grau 6 (Leve 3 / Média 6 / Pesada 9 — Média + Leve já não cabe). Se a intenção é a Técnica Máxima "encolher" de opções no meio da faixa lendária, está ok; se não, subir o orçamento pra 9 ou 10 nessa faixa resolve.
  - **Fica em Efeito no Grau 5** leva a duração pra "até alguém desfazer" (o degrau da linha Máxima). Ficou ótimo pro Fio Preso, mas é um salto grande por uma Média — vale observar se não vira padrão em todo Efeito de Grau 5.
  - **O CD +2 de Controle exige dano zero**, o que no Grau 1 é fácil (Condição Maior + uma Pesada já zera) e nos Graus altos pede 3 ou 4 peças. Se na mesa o degrau parecer inalcançável em Grau 4–5, a válvula é aceitar "dano até metade do Grau" no lugar de zero absoluto.
  - Continuam em aberto da rodada anterior: PE dos níveis 21–30, Técnica Golpeadora, Certeiro vs Inescapável, e o item 4 do Sui. ("Selo com preço" saiu da lista: resolvido pela remoção.)
