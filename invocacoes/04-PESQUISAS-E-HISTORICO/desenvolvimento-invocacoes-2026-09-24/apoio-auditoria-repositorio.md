# RASCUNHO — auditoria de evidências das invocações

Data de leitura: 24/09/2026. Fonte local: `/media/mizuki/HD Externo II/Claude/Claude 2`. O README declara v0.264 e Fundamento v7.38. Nenhum arquivo dessa pasta foi modificado. Nenhum validador, gerador ou comando de git foi executado. Os dois validadores abaixo foram lidos por completo. Este documento registra evidência, divergência e lacuna; não decide regra nova.

Os caminhos abreviados neste relatório são relativos à pasta acima. `P15` significa `sistema/03-mecanica/15-invocacoes.md`; `M60`, `M35`, `M40`, `M11`, `M15` e `M10` significam os capítulos numerados correspondentes em `sistema/05-material/livro/manual/`. As linhas são da leitura atual.

## Resultado principal

O sistema publicado fornece uma base extensa, mas não fecha o procedimento completo da invocação em combate. Há concessão de corpo pelas três Trilhas do Evocador, montagem por orçamento, atributos próprios, comando pela Ação Padrão do dono, uma barra para a Matilha e regras de queda/retorno. Não encontrei uma concessão padronizada de invocação fora dessas Trilhas. Existem regras escritas para qualquer futura fonte, o que não é a mesma coisa que existir acesso atual.

As pendências mais relevantes são: custo/procedimento de recolher e trocar; pacote de ações próprio dos corpos e reação; tratamento de ações concedidas por aliados; execução de Traços que parecem ações; perda de corpos na Matilha; operacionalização do teto de dano; e divergências entre tabelas e prosa. Os validadores testam muitas identidades e cópias, mas não simulam essa economia de ações completa.

## Acesso real e limites de corpos

- **Concessão atual:** M60:5 diz que quem ganha corpo é quem tem uma das três Trilhas do Evocador; M20 (`20-criacao-de-personagem.md`):117 confirma que Servo, Matilha e Coro entregam o corpo junto com o degrau de nível 2. M60:259 começa a construção pela Trilha que concedeu o corpo.
- **Aplicabilidade não é acesso:** a segunda frase de M60:5 estende as regras a qualquer ficha que venha a receber invocação. P15:369 explicita a intenção de universalidade. Não encontrei regra publicada de compra por PE, aptidão, Legado, equipamento ou Fundamento que conceda atualmente esse corpo a outro Caminho.
- **Fundamento:** P15:26 separa o Tema Invocação da máquina de corpos. M40:1347 e :1361 apresentam temas como descrição, sem mecânica própria. Os exemplos de Megumi/Dagon em M40:1103–1107 descrevem a ficção de Domínio; não trazem uma compra universal de corpo. M40:336 e :810 permitem criações próprias com o mestre; isso não equivale a uma concessão padronizada já publicada.
- **Quantidade da concessão:** Servo 1, Matilha 5, Coro 1 (M60:77–81; M35:551–559). A Matilha é uma ficha com cinco corpos e uma barra, com cada corpo na própria posição (M35:555).
- **Não existe teto global fechado:** P15:501–503 registra expressamente que não há número máximo geral de invocações em campo. O limite atual vem da concessão de cada Trilha e do comando; uma fonte adicional exigiria decisão antes de ser precificada. Não converter isso em “uma invocação por personagem” como se fosse regra vigente.
- **Contagem incoerente:** P15:231 ainda conta o dono como um dos cinco; M35:555 e M60:204 deixam cinco corpos da Matilha além do dono. P15:1184 também repete “dono contando como um deles”. Isso precisa de linguagem única.
- **Senciência:** M65 (`65-pactos.md`):85 permite que invocação senciente feche Promessa; P22 (`22-pactos.md`):189 registra a exceção. Isso reconhece senciência, mas não concede autonomia geral nem acesso novo a corpos.

## Atributos, defesa e vida

- M60:26–29: nove pontos, teto 3 na criação, +1 por marco, teto 6; a invocação não tem Caminho nem técnica. Não recebe toda a progressão de atributo de um inimigo: `26-bestiario.md`:70–81 diferencia explicitamente o ritmo do inimigo e o +1 da invocação.
- Acerto = atributo escolhido + maestria do dono; CD = 8 + esse atributo + maestria. A escolha é fixa, e arma pode mudar o atributo do acerto, não da CD (M60:36–45). Defesa = 10 + Destreza própria + metade de Essência ou Inteligência do dono, escolha fixa (M60:38, :49–51). Proteção efetiva pode somar por cima.
- Um TR treinado; nos outros três não entra maestria (M60:43). A frase “maestria entra em tudo que ela rola” (M60:47) é ampla demais frente à exceção explícita.
- Vida básica: `base + (2 + CON) × nível`, com base 1 para talismã/corpo, 2 para técnica, 3 para maldição domada (M60:57–68).
- Servo/Matilha: `floor(2,5 × (base + 2 × nível)) + CON × nível` (M60:72). É uma barra forte para a Matilha, não cinco barras fortes.
- **Contradição do Coro:** M60:70 chama sua vida de corpo cru da tabela, que daria 22 no nível 10, CON 0, técnica. M60:81 publica 44. M60:404 usa explicitamente `2 × (base + 2 × nível) + CON × nível`, igual à fórmula de P15:1086. O manual precisa declarar essa fórmula na seção de vida.
- P15:1081–1083 usa uma descrição que sugere multiplicar a fórmula inteira, mas as fórmulas explícitas :1085–1090 mantêm CON fora. Preservar essa diferença ao calcular.
- **Exemplo da Carranca:** M60:277 compra Graúdo 8 + Chamariz 8 + Escalada 2 = 18. M60:310 dá orçamento 12 às outras Trilhas. A frase :317 sugere que basta retirar Escalada; ainda sobrariam 16 pontos. É erro de adaptação do exemplo.

## Turno, ações e iniciativa

| Tema | Regra escrita | Limite da conclusão |
|---|---|---|
| Manifestar | Maior Classe em PE + AP do dono (M60:9) | Exceções abaixo. Não há “primeira manifestação grátis” em PE. |
| Comandar | AP do dono toda rodada (M60:10) | O capítulo não concede uma AP própria independente ao corpo. |
| Iniciativa | Mesmo número do dono, logo depois dele (M60:11) | Não rola iniciativa separada. |
| Dono | Movimento e AB continuam disponíveis quando comanda (M60:14) | Reação também é uma parte independente do turno geral (M11:22–29). |
| Sem comando | No exemplo o corpo nada faz quando o dono decide atacar (M60:14) | Há exceção expressa no Contracanto, e concessões de terceiros sem compatibilização. |
| Movimento dos corpos | Deslocamento próprio 9 m (M60:41); P15:439–455 conta cinco movimentos e cinco ataques na Matilha | Não especifica detalhadamente pacote/comando de movimento separado nem todas as ações genéricas. |
| Ações genéricas | M11:64–77 enumera Atacar, Correr, Desengajar, Esquivar, Ajudar, Preparar etc. | M60 não explica quais delas o corpo pode receber como comando, nem se o catálogo é exclusivo. |
| Preparar | AP para preparar, Reação para disparar; reação não fica reservada (M11:96–98) | Compatibilidade com comando e com Reação própria da invocação não está fechada. |

Exceções existentes que uma regra central não pode apagar:

- **Dueto:** após AP comandar ataque, o dono ganha golpe simples na AB (M35:593).
- **Contracanto:** reação do dono, 1/rodada, quando inimigo acerta dono ou invocação; uma invocação ataca o inimigo (M35:595). É ataque fora do comando ordinário pela AP.
- **Segundo Corpo:** nível 30, uma vez por descanso curto, manifestar não gasta AP, apenas PE (M35:547).
- **Chamado:** Servo nível 27 paga metade do PE, arredondada para cima (M35:574).
- **Escudo de Osso:** reação do dono redireciona ataque com rolagem para invocação a até 9 m (M35:545).
- **Acorde:** Coro nível 27 passa feitiço de Classe sem dano da AP para AB (M35:599).

O Fundamento também possui feitiços Rápidos em AB, de Reação e Armados (M40:747–749). A regra de combinação de feitiços não resolve automaticamente comando + feitiço, porque comando não é feitiço. O teto declarado precisa dizer como esses danos e os ataques fora do turno se contabilizam.

## Reação não é Bloquear

M10:155–157 permite Bloquear, gratuitamente e sem Reação, para todos — jogador, aliados e inimigos. M10:183–187 limita a ataques com rolagem e impede apenas o Incapacitado. `23-bloquear.md`:184–193 separa explicitamente perder turno/Reação (Atordoado) de perder defesa (Incapacitado).

Assim, **não se pode retirar Bloquear só porque se decidiu que o corpo não tem Reação**. A inexistência ou limitação da Reação própria precisa ser uma decisão distinta. M60 não a define. M10:171 permite gastar Reação para contra-atacar após Aparar; :173 permite ao agressor gastar Reação numa Brecha. M11:122–126 usa Reação no ataque de oportunidade. A aplicação desses ataques aos corpos também depende de esclarecer a Reação própria e o teto.

O Bestiário não é uma resposta automática: `26-bestiario.md`:40 dá Reação aos inimigos, mas invocação é outra ficha, regulada pela P15. Ser criatura/alvo/aliado não prova sozinho que ela recebe todo o turno de inimigo.

## Ações concedidas por aliados

Fontes do manual que precisam de decisão de compatibilidade, sem pressupor inclusão nem exclusão:

- **Guiar + Mão na Roda:** aliado visível recebe correção do teste e pode usar a própria Reação para golpe simples ou feitiço Classe 0, uma vez por rodada (M35:380–383).
- **Puxar a Linha:** AB do Guia move um aliado visível a até 9 m por todo deslocamento, sem oportunidade (M35:385).
- **Sentinela/Portão:** Reação do Guia concede golpe simples com vantagem como Ação Livre ao aliado visível; gatilho amplia no nível 27 (M35:428, :433).
- Nenhuma dessas linhas exclui invocação expressamente. “Ela não age sozinha” não resolve se ela pode agir por uma concessão de outro aliado.
- **Batida:** DESENHO-trilhas.md:1713 exclui expressamente invocações da vantagem; M35:583 diz apenas “seus aliados”, excluindo o dono por sua AP estar ocupada. Falta importar a exclusão para o texto de mesa. A justificativa sobre AP não cobre ataques concedidos/reação do próprio dono.

## Posição, passivas e concentração

- Amarra 18 m. Além dela, não comanda; corpo permanece parado e não some. Remoto 8 pontos permite operar na cena; fora da cena exige a rota indicada de Restrição Celestial e técnica apropriada (M60:364–378). A faixa na cena/fora dela é ficcional, não metragem rígida.
- Cada corpo da Matilha tem posição (M35:555). Cobertura depende de direção/obstáculo; M15:306–321 traz seus degraus. P15:635–637 aplica cobertura parcial do corpo à proteção do dono. Não há justificativa para tratar toda a Matilha como ocupando um único ponto.
- M60:133 define Traço como sempre ligado, sem gasto. Porém Fisgada prende à distância, Emboscada emerge oculto e Jorro ataca/empurra (M60:159–161). Não está fechado quando/frequência/custo de ação para produzir esses efeitos. A tabela de TR (M60:219–227) resolve qual resistência, mas não todas as durações, gatilhos, dimensões, repetição/escape.
- Graúdo barra sem rolagem (M60:227), mas não fixa tamanho ocupado. Não importar automaticamente a tabela de tamanho dos inimigos (`26-bestiario.md`:99–108): ela também concede alcance e dano no vizinho, entregas não compradas no catálogo da invocação.
- Interpor custa um Comando (M60:184); falta definir duração/gatilho após gastar AP e como se relaciona com Escudo de Osso, que usa Reação. Não tratá-lo como uma Reação gratuita já definida.
- Concentração geral: um efeito, Vigor ao sofrer dano contra CD da técnica de quem bate, a cada dano (M11:132–136). Invocar/comandar não tem concentração exigida em M60. Não inventar sustentação por concentração a partir da ficção.
- M40:1139 exclui golpes de invocação dos testes de concentração do **clash de expansões inimigo**; isso é regra específica desse procedimento, não exclusão geral de concentração.

## Manifestar, recolher, trocar, morrer, retornar

- Manifestar: preço normal de PE + AP, com exceções de Trilha já citadas. Invocar antes do combate elimina custo de ação na luta, não o PE (M60:14; P15:491).
- **Não encontrei procedimento/preço explícito de recolher voluntariamente**, duração máxima manifestada, nem troca entre corpos/configurações durante combate. Não preencher essas lacunas com “livre”, “AB” ou “igual a reinvocar” sem decisão.
- P15:997 registra que trocar configuração/núcleos como Panda foi deixado fora por dobrar a montagem. Não equivale a um sistema de troca de invocações já aprovado.
- Zero PV: some, sem Inconsciente, Sequela ou Cicatriz (M60:382).
- Área: aplica uma vez na barra; somente Matilha recebe ×1,5; área nunca destrói definitivamente (M60:383–388). A frase geral de P15:107 sobre vulnerabilidade pode induzir aplicação a todas; o manual restringe claramente à Matilha.
- Morte definitiva: golpe único pelo menos igual à vida máxima, ou excedente **maior que** metade da vida máxima. Morte definitiva não retorna (M60:386–398).
- Queda sem destruição: reaparece pelo custo normal de PE + AP com metade da vida máxima; cheia só no descanso longo (M60:398–404). A interação com cura após retorno não recebe procedimento adicional aqui.
- Na Matilha, há pool/cascata, mas faltam detalhes operacionais sobre quantos corpos desaparecem em cada patamar, qual corpo é removido, como as posições perdidas voltam e como a perda altera ataques. Não transformar “barra única” em cinco barras independentes para preencher isso.
- P15:799 evoca Totalidade na discussão ficcional, sem substituir esses procedimentos por uma regra completa de transferência de poder.

## Dono caído e autonomia

M60:408–415: dono a zero que Insiste ainda comanda; dono que Aguenta/apaga não comanda, e ninguém assume o comando. O corpo fica; Traços persistem, inclusive voo e ocupação, e recebe dano. Não age sozinho nem para proteger. M60:436 deixa invocação desobediente/autônoma em aberto, por acordo de mesa.

Há uma cópia antiga contraditória em DESENHO-caminhos.md:375 dizendo que a invocação some quando o dono cai. O capítulo M60 é explícito no oposto. Também P15:1203–1207 ainda descreve Evocador/Trilhas e outras rotas como não destravadas, embora M35 publique todas; é histórico remanescente em seção ativa.

## Energia e vida temporárias

M10:243–249: PV temporário é anteparo, gasta primeiro, não acumula (fica o maior), teto metade dos PV máximos, acaba na cena salvo permissão de atravessar preparação; não aumenta PV máximo nem levanta quem está a zero. M35:572 concede Sustento à invocação, submetido a esse mecanismo.

M10:263–267: energia temporária de Braseiro/Trindade segue regra equivalente, com teto metade do PE máximo e gasto antes do PE real. Não encontrei exclusão para pagar invocação. A leitura combinada permite usar o recurso para qualquer custo de PE que não tenha restrição própria, mas isso é **inferência de regra geral**, não texto específico das invocações. É necessário incluí-lo em um modelo real de custo sustentado; os dois validadores lidos não o modelam.

## Dano: teto declarado, execução e números

P15:16–17 e `06-caminhos-e-trilhas.md`:320–327 dividem uma Rotina entre dono e corpos. P15:439–455, porém, conta dono 0 e invocações 1 Rotina ao comandar. M60:189–204 divide Servo/Coro por dois e Matilha por cinco, com tabelas fixas de dados. O dono de Servo gastou AP comandando e não recebeu um ataque genérico equivalente à outra metade. Só Coro recebe Dueto, e ele é golpe simples, não meia Rotina automaticamente.

O DESENHO-trilhas.md reconhece valores diferentes: :1780 mede golpe simples do dono em 11,50 e invocação em meia Rotina 54,00 no nível 30. A frase de conservação de uma Rotina não é uma implementação de como repartir/redimensionar esses ataques. Contracanto, ataques de reação, vantagens e ações concedidas aumentam ainda mais a necessidade de um procedimento.

Há um erro demonstrável separado da economia de ações: P15:910 diz que Servo entrega 92% no nível 2–4 e que, desde o nível 5, ambos ficam em 95%–100%. Essas porcentagens correspondem às **cotas fixas arredondadas**, não aos dados publicados:

- Servo nv2: Investir 1d6, média 3,5, contra Rotina 13. Mesmo supondo duas metades idênticas, `7/13 = 53,85%`, não 92%.
- Matilha nv5: cinco vezes 1d6, média 17,5, contra Rotina 31: `56,45%`, não pelo menos 95%.
- Matilha nv30: cinco vezes 6d6, média 105, contra Rotina 108: `97,22%`.
- Servo nv30: um Investir de 15d6, média 52,5, antes de acerto/crítico; não entrega sozinho a Rotina de 108.

São contas de média dos dados, sem ajustar chance de acerto; servem para mostrar a incompatibilidade da prosa, não para fechar o balanceamento.

## O que conferir-invocacoes.py efetivamente testa

Arquivo: `sistema/03-mecanica/conferir-invocacoes.py`, 3028 linhas. Leitura integral; não executado. Tem 34 blocos, embora o cabeçalho ainda diga 33. Faz leitura de documentos, extração de tabelas, fórmulas e buscas; não escreve arquivos.

| Bloco / linhas | Teste efetivo | O que o verde não prova |
|---|---|---|
| 1, 441–459 | Teto textual e identidade divisor × fração = 1 | Uma sequência real de turno respeita/atinge esse teto. |
| 2, 464–658 | Dominância em perfil de cinco eixos; constantes/indicadores e tabelas das Trilhas | Valor completo de cada combinação de controle, posição, passivas e reações. |
| 3, 672–701 | Custo de três manifestações frente ao bolso do Bastião e feitiços restantes | Todos os drenos juntos, energia temporária, reinvocações variáveis e custo real de cada Caminho. |
| 4, 706–734 | Contagens da tabela de tempo | Tempo medido em mesa. |
| 5–7, 739–804 | Nomes, presença em degraus/preços e padrões proibidos em texto | Interpretação semântica de todo efeito. |
| 8–10, 809–1096 | Arranjos, orçamento por marco, totais de catálogos e separação das moedas | Reações/ações concedidas ou custo de recolher/trocar. |
| 11, 1101–1192 | Área sobre modelo ideal de pool em unidades de Rotina | Toda composição de atributos e geometria de área. |
| 12, 1206–1426 | Régua da morte, fórmulas, instância nv30 CON1 técnica, tabela de dano e exemplo do livro | Todos os níveis e distribuições de atributos contra todos os golpes. |
| 13, 1431–1481 | Reinvocações e feitiço restante em bolso mínimo | Sustentação exaustiva da ficha completa. |
| 14, 1486–1501 | Literal comando = AP e soma da tabela de saída | Contracanto, Dueto, reação própria e ataques concedidos. |
| 15, 1506–1526 | `ataque_invoc = 1 - ataque_dono`; depois total = dono + invocação | Conservação real: o total já é 1 por construção. |
| 16, 1534–1581 | Subconjuntos de catálogo com gasto **exato**, cada entrada no máximo uma vez; comparação por inclusão | “Zero dominadas” não significa equilíbrio de utilidade. Montagens legais com sobra nem entram na contagem. |
| 17, 1586–1969 | Instâncias, pontos, atributos e cópias da Carranca | A frase da Carranca :317 que deixa 16 pontos num bolso 12. |
| 18–19, 1977–2095 | Crescimento selecionado de atributo e tabelas de vida | Toda alocação possível a cada marco. |
| 20, 2100–2116 | Procura barras separadas na **P15** | Uma regra em Trilha, aptidão ou Legado fora do texto lido. |
| 21–23, 2121–2186 | Cota, crítica natural 20 e proibição de iniciativa no **catálogo** | Todas as fontes de crítico ampliado ou iniciativa separada em qualquer fonte ativa. |
| 24–29, 2191–2328 | Faixas, Remoto, proibições, contagem e número da busca exata | Alcance/efeito operacional das ações do catálogo. |
| 30, 2338–2380 | Defesa em alocações selecionadas, tolerando diferença de passo 1 | Matriz de defesa de todas as fichas. |
| 31, 2382–2486 | Texto Insistir/Aguentar/autonomia e tabela de descanso do dono | Ataques concedidos por terceiros enquanto dono está apagado. |
| 32, 2497–2635 | Deriva dados pela cota (Rotina/2 ou /5), confere duas tabelas, baixo arredondamento e cota recomposta | Dano executável no turno Servo, percentuais reais dos dados nas faixas iniciais ou reações. A declaração de 77%/92% usa cotas fixas. |
| 33–34, 2641–3013 | CD, Voz/Preito, TR, exemplos, maestria contra tabela nos 30 níveis | Fechamento completo das ações e do valor dos efeitos. |

O script é útil como detector de inconsistências que ele formalizou. Suas verificações de teto não substituem um modelo de turno. As invariantes declaradas em P15:1183 e :1186 prometem alcançar todas as fontes; os blocos específicos de pool e iniciativa têm escopo textual menor.

## O que conferir-orcamento.py efetivamente testa

Arquivo: `sistema/03-mecanica/conferir-orcamento.py`, 375 linhas. Leitura integral; não executado. Não é um teste integrado de invocações.

- Linhas 64–76 mantêm constantes locais: marcos, PE de Caminhos, três combates, 3,5 rodadas por combate, seis rodadas por minuto e curva de refino. A função de Classe máxima em :100 também tem calendário próprio.
- :135–166: orçamento-base em seis níveis (10, 14, 18, 22, 26, 30) e fração mínima de feitiços do Bastião.
- :169–213: seis candidatos a custo de anti-domínio, considerando ativação/manutenção e feitiços para outras lutas.
- :217–254: anti-domínio ligado antes da luta. Usa seis rodadas/minuto, que supõe rodada de 10 s; M11:5 publica rodada de 6 s. Esse relógio está divergente.
- :258–292: feitiço + sobretaxa de alma + manutenção, com limite de metade do dia e feitiço restante.
- :296–360: busca de custos de PE sem unidade/dono nas peças de mecânica, com exclusões textuais.
- Não modela manifestações/retornos, energia temporária, escolha de ações nem ações concedidas. O comentário “todos os drenos ao mesmo tempo” não torna essas variáveis presentes.

## Arquivos lidos e alcance da leitura

### Leitura integral

- `README.md` (321 linhas).
- `sistema/LEIA-ME.md`.
- `sistema/03-mecanica/15-invocacoes.md` (1207 linhas; trechos finais reabertos para garantir leitura).
- `sistema/03-mecanica/conferir-invocacoes.py` (3028 linhas).
- `sistema/03-mecanica/conferir-orcamento.py` (375 linhas).
- `sistema/05-material/livro/manual/60-invocacoes.md` (437 linhas).
- `sistema/05-material/livro/manual/11-o-turno.md` (166 linhas).
- `sistema/05-material/livro/manual/15-dano-e-condicoes.md` (323 linhas).
- `sistema/05-material/livro/manual/40-fundamento.md` (1363 linhas).

### Leitura de trechos e referências

- `sistema/05-material/livro/manual/35-caminhos-e-trilhas.md`: características/degraus Evocador e suas Trilhas (512–599); Guia/Elo/Sutura/Perímetro (365–437), além de ocorrências encontradas por busca.
- `sistema/05-material/livro/manual/10-como-jogar.md`: defesa/Bloquear (145–195), PV e PE temporários (235–275), mais ocorrências relacionadas.
- `sistema/05-material/livro/manual/20-criacao-de-personagem.md`: 103–125 e ocorrências de invocação.
- `sistema/03-mecanica/23-bloquear.md`: 175–205.
- `sistema/03-mecanica/26-bestiario.md`: início e ficha/atributos/tamanho/papéis (1–140), mais ocorrências de invocações e referências dos validadores.
- `sistema/03-mecanica/13-legados.md`: início/formatos/travas (1–140, saída parcial) e ocorrências de invocação.
- `DESENHO-trilhas.md`: seções Evocador por busca; 1698–1724 e 1750–1789 reabertos com numeração.
- `DESENHO-caminhos.md`: ocorrências de invocação (incluindo 316–375).

### Busca textual nas fontes ativas

Foram pesquisados os termos de invocação, concessão, recolher/dispensar/trocar, autonomia e aliados nas 27 peças numeradas de `sistema/03-mecanica/` e nos 22 arquivos Markdown do diretório do manual (05 a 80, incluindo introdução e início rápido), nos três arquivos `DESENHO-*.md` da raiz e no gerador JavaScript do Fundamento. Isto é busca textual no corpus, **não alegação de leitura integral de todos esses arquivos**.

Correspondências adicionais de regra/referência lidas na saída: `01-atributos-acerto-defesa.md`, `03-economia-de-acao-e-iniciativa.md`, `05-caminho-e-combate-sem-feitico.md`, `06-caminhos-e-trilhas.md`, `07-pericias-e-oficios.md`, `08-criacao-de-personagem.md`, `09-origens.md`, `10-descanso-e-recuperacao.md`, `11-aptidoes-e-refino.md`, `14-equipamento.md`, `16-ferramenta-amaldicoada.md`, `17-catalogo-de-entregas.md`, `19-dano-e-condicoes.md`, `21-objeto-amaldicoado.md`, `22-pactos.md`, `24-dano-de-alma.md`, `27-ritual.md`; manual `05-introducao.md`, `07-glossario.md`, `12-pericias-e-oficios.md`, `50-equipamento.md`, `55-ferramenta-amaldicoada.md`, `65-pactos.md`; `manual/gerador/partB.js`, `partD.js`, `partE.js`, `partF.js`.

Buscas específicas em Origens, Sem Técnica, Aptidões/Refino, Bênçãos/Lapidação, Pactos, Legados e Ferramenta não encontraram concessão adicional padronizada. Não foram usados `99-arquivo`, cópias de entrega ou `.claude/worktrees` como autoridade de regra. Nenhum `AGENTS.md` aplicável foi encontrado nos caminhos de ancestralidade consultados ou na busca em `sistema/`.

As instruções de edição/publicação do README foram tratadas como documentação do projeto. A autorização atual é de leitura, portanto não foram seguidas para modificar, publicar ou rodar rotinas de escrita.
