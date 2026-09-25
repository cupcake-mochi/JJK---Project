# RASCUNHO — fontes dos Caminhos e interações com Invocações

Leitura de 24/09/2026. Apoio técnico à primeira comparação de arquitetura; não altera regras, não certifica preços e não aprova o protótipo. Nenhum script dos Caminhos foi executado.

## Fonte que prevalece nesta etapa

A coleção `../RPG-JJK-Caminhos-Trilhas-e-Ideias/` foi localizada depois da informação adicional do autor. O ZIP correspondente também está na raiz do satélite. Foram lidos integralmente LEIA-ME, MANIFESTO, Estado-atual-e-pendencias e os quatro Markdown de `01-Caminhos-e-Trilhas/` (167, 502, 360 e 347 linhas). A ausência informada na primeira busca deixa de ser uma limitação desta entrega.

O LEIA-ME identifica a coleção como consolidação v0.4, copiada sem novas mudanças; o manifesto relaciona sua origem e hashes. O cabeçalho do Emanador conserva a versão própria v0.3, embora integre a coleção v0.4. A instrução atual de Mizuki manda preservar esta coleção. Ela prevalece sobre `bastiao-completo.md`, `vanguarda-completo.md`, `emanador-completo.md` e `guia-completo.md`, que também foram lidos integralmente, inclusive seus parâmetros, e são comparações históricas nesta etapa.

O estado local de Git observado foi `main`, HEAD `dff171d36148c7163fdebfdaf8ec95f343c03503`. O ramo e commit citados em CONTINUIDADE-caminhos.md são registro de outra rodada. As pastas `.agents` e `.codex` do satélite estão vazias. Foram lidas as referências pessoais em `/home/mizuki/CHAT-GPT/sources/mizuki-rpg-gamedev/SKILL.md` e `/home/mizuki/CHAT-GPT/sources/mizuki-copiloto-do-mestre/SKILL.md`; elas reforçam precisão de fontes e separação entre regras e conjecturas, sem transportar regras de F&M para o Projeto M.

## Diferenças efetivas entre a coleção e os arquivos da raiz

| Caminho | Coleção v0.4, referência desta etapa | Arquivo local da raiz, somente comparação |
| --- | --- | --- |
| Bastião | Olhos Em Mim, Muro, Punho e Combatente Amaldiçoado. Essencialmente preserva o kit e acrescenta redação operacional: Ainda de Pé exige cair à metade da vida; Inabalável não devolve ações/Reações de um inconsciente. | Consolida decisões de 17–21/09 com orçamento e notas extensas. O ZIP `bastiao-reforma` é de 17/09, mais antigo; nomes e preços corrigidos na raiz já o sucederam. |
| Vanguarda | Sequência e Estocada preservadas, com redação mais explícita; inclui Batedor com rotas Yumi/Besta/Arma de Fogo e Executor completos. | Diz que Batedor/Executor não possuem releitura vigente, pois registrava o descarte de propostas anteriores. Essa afirmação não descreve a coleção v0.4. |
| Emanador | Desdobramento Técnico, Expressões Familiares, Forma Fluida, Composição Técnica e Expressão Instintiva. Trilhas Condutor Armado, Ressonante e Catalisador. | Emissão Intensa/Deslocada/Dupla e Trilhas Prisma, Crivo e Vestígio: outro desenho inteiro. Não importar suas habilidades, preços ou a regra específica sobre emissões como se fossem v0.4. |
| Guia | Aberturas Avançar/Executar/Resguardar; Resposta Coordenada; Reajustar/Passar oportunidade; cadeia no 30. Trilhas Arquiteto, Analista e Socorrista. | Chamada com dado de dano, Ataque Extra e Trilhas Cartógrafo/Analista/Regente: outro desenho. A vedação local a feitiços e golpes desarmados em ataques concedidos NÃO vale para Resposta Coordenada v0.4. |

Estocada permanece intacta. Emanador continua com 6 PE por nível, sem atributo acrescentado ao PE máximo. As habilidades locais não servem de correção implícita da coleção.

`03-Notas/Estado-atual-e-pendencias.md` mantém abertas: prazo/abrangência de Oportunista; ordem, custo e arredondamento de Contra a Parede; conversões de dano/cura/Apoio em Forma Fluida. Não resolver essas lacunas ao escrever Invocações. A validação integrada em fatias está pendente expressamente.

## Interações que realmente pertencem à v0.4

As linhas abaixo se referem aos arquivos de `../RPG-JJK-Caminhos-Trilhas-e-Ideias/01-Caminhos-e-Trilhas/`.

### Guia — 04-Guia-Caminho-e-Trilhas.md

- **21–47:** Abrir Caminho custa Ação Bônus + 1 PE; aliado voluntário percebido a 18 m e capaz de perceber orientação. Avançar oferece 3 m sem outra ação no turno do aliado; fora dele exige sua Reação. Executar oferece vantagem a uma tentativa de ataque/perícia existente. Resguardar oferece vantagem a um TR, inclusive concentração contra a ameaça indicada.
- **55–72:** Resposta Coordenada exige Reação do Guia **e** do aliado, uma vez por rodada. Permite golpe com arma ou desarmado **ou** feitiço conhecido de Classe 0 que normalmente use Padrão, com custos e limite geral de conjurações. Golpe não é Ação Atacar nem etapa de Sequência. A resposta não desencadeia outra ação concedida. Não há exclusão expressa de invocações; sua elegibilidade precisa respeitar capacidade, percepção e vínculo.
- **90–120:** cada etapa de uma cadeia usa aliado e tipo diferentes. Passar a Oportunidade não renova Resposta Coordenada. No 30, até três aliados e duas respostas; a segunda dispensa só a Reação do Guia, e os respondedores precisam ser distintos. Novos corpos aumentam participantes disponíveis, mas não os limites escritos.
- **134–216:** obras do Arquiteto têm posição, vida, Defesa, duração e limite de quantidade, embora sejam construções sem rotina autônoma. Portanto **ter vida e ocupar espaço não basta para exigir ficha de invocação**. Obra não é beneficiário-aliado por isso. Muretas/Passarelas/Patamares são precedente de valor físico separado de ações. Criar básica com Abertura custa 2 PE ao todo; reparo 1/3/5 PE.
- **222–274:** previsão de Bloquear/mover/atacar/conjurar confirma a leitura apenas depois do acontecimento; não retroage. Apontar a Brecha custa 3 PE para repetir primeiro TR bem-sucedido do inimigo, sem Reação. Deve ser testado com ataque especial de entidade que imponha TR.
- **280–345:** Socorrista cura/remedeia criaturas aliadas sob condições explícitas. Emergência exige que o alvo continue vivo e possa recuperar vida. Uma invocação que dissipa ao chegar a zero pode não estar mais disponível: não presumir que esta cura recupera entidade já removida. É uma dependência real da futura regra de derrota.

### Emanador — 03-Emanador-Caminho-e-Trilhas.md

- **32–36, 44–76:** Desdobramento modifica feitiços conhecidos de Classe 1+, respeitando Fundamento, Famílias, restrições, teto e custos. Modulações não autorizam aplicar habilidades do usuário a qualquer efeito da criatura. Deve-se identificar quem conjura e de quem é o feitiço.
- **88–102, 130–140:** Afinidade reduz a primeira conjuração de feitiços escolhidos; Instintiva reduz Classe 1/2 escolhidos para 1 PE quando feitos na Padrão. Se manifestação vier a ser feitiço, precisa testar estes descontos; não converter custo geral de manifestação em feitiço incidentalmente.
- **159–182, 218–226:** Condutor Armado combina Padrão e Bônus, inicialmente arma/Classe 0; depois admite classes maiores ou dois ataques sem feitiço. Comando obrigatório por Bônus compete diretamente com a identidade da Trilha.
- **285–297:** Ressonante usa Reação para preservar um Eco quando falha. Uma reserva compartilhada de Reações cria uma escolha real entre isso e proteção/reação de invocação.
- **314–322:** Catalisador pode transformar Padrão em Bônus, preservando o limite do outro feitiço como Classe 0. A criatura não fornece uma segunda licença de conjurar na ficha do usuário; essa autoria precisa ser explícita.

### Vanguarda — 02-Vanguarda-Caminho-e-Trilhas.md

- **32–96:** a Sequência usa ataques próprios existentes; uma Condução ou Conclusão por turno próprio. Criatura não prepara a Sequência do usuário automaticamente. Derrubado, Agarrado, terreno difícil ou outra redução prévia produzidos por aliado podem cumprir requisitos de opções específicas.
- **150–196:** Compasso usa a Bônus após conjuração elegível; Bote/Ferrão seguem seus limites. Refluxo recebe metade do PE **realmente gasto** numa Condução, arredondado para baixo, mínimo 1 se houve gasto; gratuita gera zero. Temporária gasta antes do normal, usa maior reserva, tem teto de metade do PE máximo e prazo geral. Testar uso de energia temporária nos custos do novo sistema sem inventar proibição ou desconto.
- **219–227:** Yumi arma uma Conclusão usando ataque próprio e depois gasta Reação para soltá-la. Usar essa Reação noutra coisa descarta a flecha. É exceção escrita à resolução no turno; não autorização de receber etapas via criatura.
- **307, 341:** criatura com ação, alcance e capacidade apropriados pode ajudar a retirar virote; custa Bônus+TR ou Padrão sem teste. Utilidade de corpos não se limita a dano. Não transferir essa ação de graça para invocações inativas.
- **405–413:** Arma de Fogo usa Reação/Oportunidade para retirada e recarga; outro ponto de concorrência de reserva.
- **442–486:** Finta solicita Reação do inimigo para Antecipar; Dobrar a Aposta pode conceder contra-ataque dentro da mesma Reação já gasta. Retirar ou compartilhar Reações de invocações muda sua resposta defensiva à Finta; o fato deve aparecer nos testes.

### Bastião — 01-Bastiao-Caminho-e-Trilhas.md

- **34–54:** ativa área com Bônus, assume golpe acertado com Reação; o golpe transferido não permite novo Bloquear. Nem Um Arranhão compete pela mesma Reação. Duro de Matar só responde à falha de Bloquear normal.
- **64–99:** proteção de aliado, cobertura e preservação da área inconsciente não entregam Reações novas. Mais corpos podem se beneficiar fisicamente, mas não multiplicam interceptações.
- **114–157:** Trocação disputa Bônus e anexa soco à Reação de transferência; Minha Vez usa ação livre + 2 PE depois de Bloquear. Retaliação integra a mesma Reação; Embalo exige crítico do próprio ataque na Ação Atacar ou seu TR Físico. A criatura não gera esses gatilhos em nome do usuário.

## Revisão da candidata de teste recebida

**Candidata:** usuário e entidades compartilham uma Reação; Bloquear mantém a regra geral; Padrão+Bônus permite até dois corpos diferentes darem um golpe simples reduzido; alternativamente a Padrão comum pertence ao usuário ou a uma criatura; cada Movimento reposiciona até dois corpos; intenção persiste sem ação gratuita.

1. **Conflito decisivo com o Guia que seja invocador:** Resposta Coordenada exige duas Reações. Se Guia e sua criatura compartilham uma única reserva, não podem ambos pagar. Cobrar apenas uma alteraria silenciosamente o Guia. Alternativas transparentes: manter uma reserva e registrar que ele não pode Coordenar a própria criatura; ou comparar uma Reação pessoal + uma coletiva de invocações. A segunda sustenta essa interação, mas aumenta respostas disponíveis e deve ser medida. Um Guia externo pode convidar a entidade consumindo a reserva coletiva, com a própria Reação separada.
2. **Não há bloqueio geral no conjunto Padrão+Bônus**, mas ele não é neutro: compete com Estocada, Condutor Armado, Catalisador, Finta e Abrir Caminho. Dois golpes reduzidos devem ser comparados com os ataques/feitiço que a mesma ficha abandonou, sem adotar redução numérica final agora.
3. **Singular e usuário são dois corpos diferentes e podem agir em conjunto**, cada um com um golpe instrumental. Para testar a fantasia de a entidade lutar pelo usuário, compare essa participação conjunta com a Padrão integral da entidade e o usuário sem ofensiva. A singular não recebe os dois golpes em seu próprio corpo; isso é um limite da opção, não exclusão dessa composição.
4. **Padrão da criatura não transporta o Caminho do usuário.** Ela usa ações expressamente presentes na ficha provisória. Uso de feitiço depende de uma capacidade própria e autoria; não recebe Sequência, Compasso, Desdobramento ou poderes defensivos do usuário implicitamente.
5. **Movimento compartilhado limita reposicionamento, não valor físico estacionário.** Quatro corpos ainda oferecem quatro posições, bloqueios, alvos e sentidos. Atividades úteis extras como tirar virote, agarrar, vigiar por sentido especial ou proteger exigem permissão/custo definido. Continuidade ficcional deve permitir seguir a intenção sem transformar cada corpo em ação gratuita.
6. **Bloquear sem novo custo preserva o geral**, mas contar suas rolagens separadamente de Reações. Vários alvos atacáveis podem elevar o total quando a ofensiva inimiga também alcança vários corpos; redução de dano do ataque coletivo não elimina isso.
7. **Persistência de recursos na troca:** manifestar/substituir não renova a reserva de Reação, ações, movimento ou benefícios já consumidos da cadeia. Um corpo recém-chegado não oferece uma nova Reação se a reserva que pagaria já acabou.

### Ajuste escolhido para o protótipo B, ainda não aprovado

Depois da identificação do conflito, a candidata B passa a testar **uma Reação pessoal do usuário e uma Reação coletiva de suas invocações**, independentemente de haver uma, duas, três ou quatro entidades. Resposta Coordenada do próprio Guia paga uma Reação de cada reserva, preservando o custo da habilidade. Um Guia externo paga sua própria Reação e a entidade convidada paga a coletiva de seu conjunto.

Isso introduz **uma resposta adicional disponível ao conjunto**, benefício explícito a medir e precificar depois; a independência do número de corpos impede que três ou quatro entidades multipliquem essa entrega. Mesmo Todos no Mesmo Plano não permite duas respostas de duas invocações daquele conjunto na mesma rodada, pois a segunda dispensa apenas a Reação do Guia e a coletiva já foi gasta. Um outro aliado com sua própria Reação ainda pode realizar a segunda resposta normalmente.

Os testes negativos devem contrastar: reserva única para todos, que bloqueia Guia→própria invocação por falta do segundo pagamento; e reserva por corpo, que multiplica respostas. Bloquear continua por ataque conforme a regra geral e não consome nenhuma dessas Reações. Derrota, retirada, troca ou remanifestação não renovam a coletiva. O procedimento do protótipo precisa fixar sua renovação no ciclo do controlador para não criar renovações intermediárias pelos turnos das entidades.

Essa é uma escolha de **protótipo comparativo**, não decisão de Mizuki nem mudança de qualquer Caminho.
