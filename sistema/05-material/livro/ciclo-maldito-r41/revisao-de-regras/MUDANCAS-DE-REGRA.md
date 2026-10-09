# Ciclo Maldito — mudanças de regra decididas pelo Mizuki em 07/10/2026

Este documento lista o que precisa mudar no texto do livro. Tudo aqui foi decidido pelo Mizuki, item a item. O que não está aqui fica como está.

## Como trabalhar com este documento

- **Base:** a pasta `entregas/livro-diagramado-r29`. Trabalhe numa cópia (`livro-diagramado-r30`) e deixe a R29 intacta.
- **Mude só o que está listado.** Não feche lacuna, não acrescente limite, não reequilibre número e não renomeie nada por conta própria. Se uma mudança daqui parecer pedir outra, não faça: anote na entrega e pergunte.
- **Mexa só na frase que carrega a regra.** O parágrafo em volta fica como está. A voz do livro é a que já existe.
- **Onde está escrito "volta ao v0.331"**, a regra é a do livro antigo. A redação continua sendo a do livro novo; o que volta é o conteúdo. A fonte é o livro antigo, copiado ao lado deste documento na entrega, em referencia/manual-v0.331/ (no repositório JJK---Project ele fica em `sistema/05-material/livro/manual/`).
- **Frases vetadas pelo autor:** "suas fichas" (use "seus feitiços" ou reescreva) e "não tem como recusar".
- **Registre cada mudança** num arquivo de entrega dentro da pasta nova (revisao-de-regras/ALTERACOES-REGRAS.json), como decisão do autor de 07/10/2026, citando o número deste documento. Não escreva no repositório JJK---Project: a sincronização com a candidata e com as peças fica com o Claude.
- **Entregue junto** uma lista de todos os blocos alterados, com o texto de antes e o de depois. O Claude vai comparar o texto novo com o da R29 bloco a bloco: qualquer diferença fora desta lista será tratada como erro.
- A seção C lista o que **não deve ser escrito ainda**.

**As seis dúvidas que o ChatGPT levantou em 07/10 foram respondidas pelo autor direto no chat. Se uma resposta do chat divergir deste documento, vale a do chat.**

Os números entre colchetes são os da lista de revisão do Mizuki. Os códigos entre parênteses são os registros dos `ALTERACOES.md`.

## A. Mudanças decididas

### Poderes avançados (Expansão de Domínio)

| Nº | O que muda | Como deve ficar |
|---|---|---|
| [1] (R08-04) | Acerto de dano | **Volta ao v0.331.** O Acerto de dano é montado como um feitiço pela régua do Inescapável: ele é o feitiço inteiro (3 × Classe em pontos, menos o preço Médio do Inescapável) e não aceita outra peça. O desconto de Família Livre vale como em qualquer feitiço. Sai o valor fixo de "2 × sua maior Classe em d8" e a frase que nega desconto de Família. Fonte: `40-fundamento.md`, seção *Acerto e Efeito*. |
| [2] (R08-05) | Aliados no Acerto | Fica como está (o Acerto alcança aliados). Acrescente uma frase: poupar alguém só é possível se o Efeito do domínio disser como. |
| [3] (R08-06) | Acerto da Incompleta | **Volta ao v0.331:** o Acerto da incompleta "resolve por rolagem, como um feitiço". Sai o procedimento novo (a ficha escolher entre ataque individual e TR Físico; a regra de ambiente resistida por TR de Espírito até o próximo Acerto). Na incompleta são três casos: **(1)** se o Acerto causa dano, ele rola como qualquer feitiço, e o dono escolhe na criação se é ataque contra a Defesa ou TR do alvo; **(2)** se o Acerto é uma regra de ambiente, quem está dentro faz um TR para resistir, como num feitiço; **(3)** se o domínio não tem Acerto, só Efeito (um reforço para o dono, ou um efeito que não atinge inimigos), nada rola. |
| [4] (R08-07) | Defesas contra o Acerto garantido | O Acerto garantido não causa crítico. Ele **ignora Redução de Dano, resistência e imunidade**. |
| [5] (R08-08) | Regra de ambiente e o dono | A regra de ambiente **não vale contra o dono**, salvo se a ficha do domínio disser que vale. O resto do parágrafo fica (o Efeito não concede segundo Acerto, peça grátis nem cura). |
| [8] (R08-14/15) | Barreira | A barreira tem uma única reserva de vida (50 × metade do refino), como já está. **Sai** a regra de atingir a borda por dentro com dano dividido por quatro: por dentro a barreira não quebra. O ataque por fora continua acertando sem rolagem e sem crítico. |
| [11] (R08-19) | Rescaldo | **Volta ao v0.331:** quando o domínio acaba, a técnica não responde pelo resto da cena, e sobram a Classe 0, o corpo e o que não é técnica. Saem os fechamentos novos (sustentação que cai, instantâneo que não se desfaz, prazos próprios). Fonte: `40-fundamento.md`, *Barreira e Rescaldo*. |
| [12] (R08-22) | Acerto ao perder a disputa | A regra fica. Não use a frase "não tem como recusar". |
| [13] (R08-24) | Manter a disputa | **Volta ao v0.331:** personagem de jogador testa a cada dano, sem limite; inimigo testa no máximo uma vez por jogador que o acertou na rodada, contra a maior CD entre eles; golpe de invocação não faz o inimigo testar. Sai "conserva o primeiro total". Fonte: `40-fundamento.md`, *Domínios sobrepostos*. |
| [14] (R08-31, FU-18) | Passar no TR | Em **todo feitiço** resolvido por TR, o sucesso reduz **o resultado do dano** pela metade, e não a quantidade de dados. Vale no Fundamento, no Catálogo, nas Formas, nos exemplos e no domínio. A Técnica Máxima continua em três quartos do dano. **Só muda quem passa no TR:** Fica, Salto, Estilhaço e Queima continuam em "metade dos dados". |
| [152] (R08-27) | Três ou mais barreiras | **Regra nova do autor (07/10), que substitui "caem todas".** (1) Três ou mais barreiras fechadas que se sobrepõem ficam **instáveis**. Basta se sobreporem: sai a exigência de uma região comum às três e a frase sobre barreiras que só se encostam em lugares separados. (2) **Elas não caem sozinhas.** Seguem a disputa normal, em pares, pelo procedimento de "Mais de um confronto", com dois ajustes enquanto houver três ou mais barreiras: a pergunta do refino não decide, e a disputa vai direto ao d12 e, se ele não separar, à corrida; na corrida, cada barreira cai com **uma falha de Vigor a menos** que o normal, mínimo 1. (3) Barreira instável **não impede a entrada** de quem vem de fora. (4) **Intruso:** se uma criatura que estava fora entrar na área disputada e tiver **nível igual ou maior que o do dono de maior nível presente**, todas as barreiras envolvidas caem na hora. Ninguém vence, ninguém recebe Acerto e todos os donos entram em Rescaldo. Um intruso de nível menor entra sem derrubar nada. (5) Quando restarem só duas barreiras, a instabilidade acaba e valem as regras de dois domínios, com o refino voltando a contar. Domínio aberto e Incompleta continuam fora da contagem de barreiras. Base na obra: capítulo 179, em que os três domínios só ruíram com a entrada do intruso. |
| [153] (R08-27) | Duas barreiras e uma aberta | **Volta ao v0.331:** as duas barreiras disputam entre si como sempre, e a sem barreiras ataca as duas por fora. Sai "O domínio aberto disputa com elas". |

### Invocações

| Nº | O que muda | Como deve ficar |
|---|---|---|
| [16] (R11-32) | Domínio da domada | O Acerto de dano do domínio da domada segue a mesma regra do jogador (item [1]), montado com os números dela. Sai "Classe em d8 fixo". |
| [17] (R11-10) | Comandar especial | Comandar uma especial **não ocupa** a conjuração do turno do invocador. |
| [19] (R11-19) | Especial com a Melhoria Reação | Custa **somente a Reação coletiva**. Sai a cobrança da Reação do invocador e da básica. |
| [20] (R11-44/45) | Atrasar e Carregar numa especial | A Restrição cobra **só da entidade**. Sai a Ação Completa do invocador e a proibição de movimento dele. O invocador continua pagando a Ação Padrão normal de comandar. |
| [21] (R11-12) | Capacidade reativa com PE | Sai a regra do mesmo pagador e a exigência da Reação coletiva. A Contramedida de entidade **continua custando 2 PE**, como a do jogador. |
| [23] (R11-26) | Talismã | **Sai** a frase "Se a próxima entrada for o retorno de uma entidade caída, abata somente o valor adiantado…". O caso não acontece: entrar gasta a carga, e o descanso longo recupera a caída. |
| [30] (R12-05) | Ficha convertida da domada | Fica. Acrescente: o mestre pode permitir que o jogador monte a conversão a partir da ficha da maldição. |
| [143] (R12-15) | Restrição em especial de entidade | Mesma regra do item [143] do Fundamento: a devolução não cobre a Forma. |

### Ritual e Pactos

| Nº | O que muda | Como deve ficar |
|---|---|---|
| [34–36] (RP-19/20/29) | O que um pacto permanente concede | **Volta ao v0.331.** Sai "aumento do PE máximo igual à sua maior Classe" e toda a explicação de 1 a 7 PE. Princípio do autor, que já estava no livro antigo: *pacto nunca traz valor numérico, e sim uma mecânica única, decidida com o mestre.* Um pacto pode afetar feitiço, energia, aptidão ou estilo, alterando como eles funcionam, sem mexer diretamente em número. **Pacto de energia** muda como a energia funciona ou devolve energia; quando houver quantidade, ela é uma **porcentagem da energia máxima, combinada com o mestre**, nunca um número fixo (o Overtime é o modelo). Não existe pacto por dano. **Pacto não concede Estilo; pode modificar um Estilo, como modifica um feitiço.** Fonte: `65-pactos.md`. |
| [37] (RP-21) | Limite de pactos | O limite de metade da Essência conta pacto **permanente, Promessa e pacto de restrição**. Pacto temporário não conta. A vaga fica ocupada **enquanto o pacto existir** e volta quando ele se perde, por qualquer motivo. |
| [39] (RP-18) | Consentimento e quebra | **Volta ao v0.331:** nenhuma forma de pacto se fecha sob ameaça; quebrar uma Promessa custa a energia amaldiçoada de quem quebra e pode custar a vida. Acrescente: a punição pode ser definida na criação do pacto. |
| [42] (RP-03) | Falhar o Ritual | **Volta ao v0.331 para o conjurador:** o feitiço sai sem Pontos de Ritual e com a Classe a menos em dados de dano. **O auxiliar perde a Classe do feitiço em PE.** |
| [47] (RP-09) | Ritual de Rerrolagem | **Volta ao v0.331** (rerrola os dados de dano que caírem no mínimo, até Classe + 1 deles), mantendo só a frase nova "fica o segundo resultado". |
| [50] (RP-17) | Ritual em dupla | **Sem limite de auxiliares.** Cada auxiliar gasta a **Ação Padrão** dele (era Ação Completa) e dá **+2** Pontos de Ritual (era +4). |

### Fundamento e Catálogo

| Nº | O que muda | Como deve ficar |
|---|---|---|
| [51] (FU-20) | Certeiro | **Volta ao v0.331:** sem rolagem de acerto; o alvo faz TR para metade. Na tabela de combinações do Ritual, **retire a linha "Meio Acerto e Certeiro"**: sem rolagem não há erro para o Meio Acerto aproveitar. |
| [53] (FU-31) | Fica | **Volta ao v0.331:** a área dura 1 minuto, e quem entra nela ou começa o turno nela leva metade dos dados. Mantenha só o limite novo de **uma aplicação por criatura por rodada**. |
| [56] (R07-A-06) | Empurrão | **Volta ao v0.331.** Sai o limite de um alvo por conjuração. |
| [57] (R07-A-07) | Troca | **Sai do Catálogo.** Vira Efeito Próprio, montado com o mestre. Retire também as remissões a ela. |
| [63] (FU-36/37) | Classe 0 | **Volta ao v0.331:** cabe uma Melhoria Leve e uma Restrição Leve, e a Restrição devolve o dado que a Melhoria tirou. **Vale também para a básica das entidades**, em Construir invocações. |
| [65] (FU-42) | Técnica Máxima | **Quebra Coisa volta a ser permitida.** As outras vedações ficam. |
| [66] e [149] (FU-38, A29) | Efeito Próprio e Aptidão Própria | Quem define o preço ou o tamanho é **o mestre**. A tabela de comparação fica como apoio, não como regra. |
| [67] | Duas Melhorias escritas como uma | **Volta ao v0.331:** o mestre pode aprovar por menos pontos ou menos espaço, por conta e risco. Fonte: `40-fundamento.md`, *Melhorias e Restrições por Classe*. |
| [70] (R07-A-19, R07-R-04) | De Novo | Preço **Pesada** (era Média). **Sem limite por cena:** uma rerrolagem **a cada uso do feitiço**. Depois de errar, você rola o ataque de novo e é obrigado a ficar com o novo resultado. Na Rajada, continua valendo para um tiro só. |
| [71] (R07-B-34) | Levanta | "Você só usa Levanta uma vez por cena", em qualquer feitiço seu, e ela alcança um aliado só. |
| [75] (R07-B-19/22) | Segura e Armado | **Voltam ao v0.331.** Fonte: `40-fundamento.md`, Família *Tempo*. |
| [79] (R07-C-18) | Assinatura | A marca mostra **quem fez e onde você está**. |
| [80] (R07-C-36/37) | Regra Própria e Talento Próprio | Ficam os campos. Deixe explícito que o jogador continua livre para criar com o mestre fora dos exemplos. |
| [85] (R07-A-04) | Perseguir | Fica restrito a alvo individual. Passa a **seguir teleporte dentro da cena**, desde que o alvo não termine atrás de cobertura. Perseguir só acompanha o alvo: não contorna obstáculo nem ignora cobertura (isso continua sendo da Melhoria Contorno). |
| [86] (R07-A-27) | Desarma o Feitiço | Na criação do feitiço, escreva o que ele cancela: efeito contínuo, barreira, item ou Selo. Se a Classe do alvo for igual ou menor que a do seu feitiço, ele cancela direto. Se for maior, role **d20 + atributo da técnica, sem maestria, contra a CD de quem criou**. Para o que não é feitiço, o mestre atribui uma Classe de 1 a 7 ou declara impossível. Domínio nunca. |
| [141] | Recarga da Técnica Máxima | **Uma vez por cena** por padrão. O mestre pode permitir usar de novo depois de 3 rodadas, sem contar a rodada do uso. |
| [143] (FU-11) | Devolução de Restrição | **Volta ao v0.331:** a devolução nunca passa do que você gastou em Melhorias. A Forma não entra nessa conta. Refaça os exemplos que dependiam disso. |

### Dano e recuperação

| Nº | O que muda | Como deve ficar |
|---|---|---|
| [94] (DR15) | Cicatriz | O jogador escolhe: a Cicatriz dá vantagem em Intimidação e desvantagem em Persuasão, ou não dá nenhum dos dois. |
| [96] (DR20, R10-32) | Insistir e Segundo Fôlego | Escolher Insistir custa **Ação Padrão**; Movimento e Ação Bônus continuam com o jogador. Segundo Fôlego dispensa **essa ação e o primeiro custo de vida máxima**. |

### Origens, Progressão e Criação

| Nº | O que muda | Como deve ficar |
|---|---|---|
| [113] (ORI17) | Sangue que Não é Sangue | **Volta ao v0.331.** Sai a necessidade corporal obrigatória para recuperar no descanso longo. Fonte: `25-origens.md`. |
| [115] (ORI04) | Legado personalizado | **Volta ao v0.331:** sem o limite de um. |
| [118] (PRO04) | XP guardado | **Volta ao v0.331:** depois do feito, o XP guardado vira quantos níveis ele pagar, de uma vez. |
| [119] (PRO18/33) | Subir de nível | Fica. Acrescente: com permissão do mestre na mesa, subir de nível pode recuperar tudo. |
| [120] (PRO20–23) | Troca de Trilha | Fica. Deixe muito claro que a troca substitui tudo o que a Trilha antiga dava. |
| [147] | Rolar a vida | **Volta como variante:** com permissão do mestre, role o dado do Caminho a cada nível em vez do valor fixo. Cada Caminho informa o dado. Fonte: `10-como-jogar.md`, *Pontos de vida*. |

### Equipamento (item novo, depois da entrega da R30)

| Nº | O que muda | Como deve ficar |
|---|---|---|
| [156] | Arma sem a Força exigida ("Treino e Força") | Sai "você não soma Destreza à Defesa". Fica: **desvantagem nos ataques com aquela arma** e **deslocamento pela metade enquanto a empunhar**. Essa desvantagem não se acumula com a da falta de treino. Carregar a arma guardada continua sem penalidade. A base deste item é a R30, não a R29. |
| [157] | Traje, Revestimento ou escudo sem a Força exigida ("Requisitos e carga", em Proteção) | Hoje a peça não pode ser preparada nem dá proteção. **Muda:** a peça pode ser vestida ou empunhada e **dá a proteção normal**, mas, enquanto estiver em uso, o personagem fica com **deslocamento pela metade e desvantagem em TR Físico**. Os demais requisitos e o teto de Destreza da peça continuam valendo. O parágrafo da Força que cai temporariamente acompanha: a peça segue funcionando, com essa penalidade, em vez de ter os benefícios suspensos. **Não criar treino de uniforme nem de escudo:** o livro não tem esse treino. |
| [158] | Carga acima do limite ("Carga", em Regras gerais) | Hoje, acima de 5 + Força, não se desloca. **Muda:** acima do limite, o personagem anda com a **mesma penalidade do [157]**: deslocamento pela metade e desvantagem em TR Físico. O teto continua sendo o **dobro do limite**, que já é o máximo que se levanta em "Erguer"; acima disso não sai do lugar. |
| [157]/[158] juntos | Não acumulam | As penalidades do [156], do [157] e do [158] **não se multiplicam**: o deslocamento cai pela metade uma vez só, e a desvantagem em TR Físico é uma só. |
| [171] | Efeito Insondável (Equipamento amaldiçoado, "Corrente Extensível") | Hoje o alcance ampliado é de 18 m. **Volta ao v0.331:** enquanto a ponta estiver escondida, o alcance é **na cena, na ordem de 100 metros** (um quarteirão). Troque só o número e a frase que o carrega. O resto do texto fica: obstáculos, cobertura e linha de efeito continuam valendo, e a ponta presa continua sendo a condição. |
| [160] | Reação de Cobrir-se de Energia (Aptidões, "Amortecer um golpe") e de Defesa sem Armadura (Rotas, "Resistir ao golpe") | Hoje a Reação deixa o personagem sem proteção de qualquer fonte, inclusive Traje, Revestimento e escudo. **Muda:** a Reação tira **só a proteção passiva** (a da aptidão ou a da Bênção) até o fim do próximo turno. **Traje, Revestimento e escudo continuam dando a proteção deles.** Quem usa a Reação vestindo uniforme paga só a Reação e os 2 PE. A redução de dano, o custo e o prazo não mudam. O exemplo de Cobrir-se (Refino 6) continua certo, porque o personagem dele está sem uniforme; diga isso no exemplo se precisar. |

## B. Decisões anteriores que a R29 ainda não tem

1. **D43** (05/10): Condição, Prende e Cerca sempre pedem TR, mesmo num feitiço de ataque. São treze trechos.
2. **D44** (06/10): a Execução Preparada da Vanguarda impõe −2, não −1.
3. **Projetar Energia** (06/10): de 1 PE até metade do refino (para baixo, mínimo 1), com 2d6 de Força por PE.

Os trechos exatos dos três estão em `R28a-o-que-falta.md`, na pasta do livro.

4. **T072 sai:** a alteração T072 de revisao-textual/ALTERACOES.json (o "saldo calculado" no Controle das entidades) acrescentou regra e deve ser retirada. As outras 73 ficam.

## C. Não escrever ainda

Estes itens foram decididos na direção, mas faltam os números. O Mizuki vai fechar cada um antes.

| Nº | Assunto | Direção dada |
|---|---|---|
| [24] | Reparo por quem tem Classe menor que a do corpo | Pode reparar, mas recupera menos, proporcional ao que alcança. |
| [33] | Fabricação de entidades | O capítulo de fabricação sai do livro. No lugar, uma menção de que criar entidades vai existir. O sistema entra na fila de trabalho. |
| [40] | Exemplos de pacto | Uma lista só, juntando os da obra e os próprios, balanceada antes de ir para o texto. |
| [46] | Melhorias de Ritual que repetem | Uma tabela dizendo quais repetem e quantas vezes. |
| [101] | Área da Cortina | Volta a ser narrativa e em metros, com faixas por refino; precisa cobrir uma escola inteira. |
| [15] | Domínios da obra | Ficam fora do livro; vão para um guia de criação futuro. |
| [151] | Câmbio dos pactos | Recolocar em uma linha a régua antiga ("promessa pequena, ganho pequeno; promessa que arrisca a vida, ganho enorme"). Aguardando o ok do autor. |
| — | Exemplo do Sukuna nos pactos | O autor quer o exemplo do corte que parte o mundo. A fonte ainda precisa ser conferida. |
| — | Morte e Integridade | Vão ser revistas inteiras. Por enquanto fica o texto atual, com os itens [94] e [96]. |

## D. O que não muda

Tudo o que não aparece nas seções A e B fica exatamente como está na R29, incluindo os itens da revisão que o autor mandou manter. Em caso de dúvida, não altere e pergunte.
