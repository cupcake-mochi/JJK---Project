# Gabarito de dependências do piloto de Kaori

Conferência restrita ao tutorial e às regras que ele aciona, em 02/10/2026, sobre a v0.331. Nenhuma regra, ficha, fonte do livro ou exportação foi alterada. Contas aritméticas executadas; não equivale a revisão integral de Bastião, Fundamento ou Origens.

## Fontes e precedência útil ao piloto

- `sistema/05-material/livro/manual/08-inicio-rapido.md`: **Kaori**, **Corredor da ala oeste**. É o exemplo a revisar; não serve como autoridade para arbitrar uma divergência.
- `sistema/05-material/livro/manual/20-criacao-de-personagem.md`: **Passo 4**, **Passo 5**, **Passo 7**, **Exemplo**. Há divergências localizadas abaixo; não copiar o capítulo como bloco já validado.
- `sistema/03-mecanica/08-criacao-de-personagem.md`: **Passo 1**, **Passo 5**, **Passo 6**, **Passo 7**, **Uma ficha inteira, do começo ao fim**. Guarda a declaração expressa de Força como atributo da técnica e o dono dos ofícios. Também contém comentários históricos obsoletos sobre Trilhas sem números; para as habilidades usar a edição integrada.
- `caminhos/05-Edicao-Integrada/01-Bastião-Caminho-e-Trilhas.md`: **Características do Bastião**, **Degraus do Bastião / Nível 2: Olhos Em Mim**, **Trilha: Muro / Nível 2: Alicerce**. Fonte das habilidades atuais do piloto.
- `sistema/05-material/livro/manual/40-fundamento.md`: **Classe do feitiço**, **Atributo da técnica**, **CD de feitiço**, **Números da montagem**, **Energia**, **Famílias**, **Selo**, **Criando feitiços / Passos / Formas**, **Controle / Condições**, **Restrições**. Fonte do orçamento e da execução de Peso nas Mãos.
- `sistema/05-material/livro/manual/11-o-turno.md`: **Iniciativa**, **Recursos do turno**, **Deslocamento**, **Ações de Ação Padrão**, **Ações de Ação Bônus**, **Ataque de oportunidade**.
- `sistema/05-material/livro/manual/10-como-jogar.md`: **Bloquear**, **Testes de Resistência**, **Arredondamento**, **Vida a 0**.
- `sistema/05-material/livro/manual/15-dano-e-condicoes.md`: **Condições / Derrubado**.
- `sistema/05-material/livro/manual/25-origens.md`: **Descendente / Efeito na ficha**, **Legados do Descendente / O Sobrenome / Biblioteca**. Usar como fotografia da Origem vigente, pendente de conciliação com o trabalho externo.
- `sistema/05-material/livro/manual/45-aptidoes-e-refino.md`: **Cobrir-se de energia**, **Canalizar energia**, confrontado com `sistema/03-mecanica/11-aptidoes-e-refino.md`, **§6.9 O dano na arma**.
- `sistema/05-material/livro/manual/50-equipamento.md`: **Soco**.
- `logs/CHANGELOG.md`: **v0.176 — 29/08/2026, §1 A revisão mexeu em REGRA**, especialmente linha 7740: decisão posterior do autor que antecipa o primeiro dado de Canalizar para Refino 1. Esta decisão resolve qual escada está vigente; a cópia antiga da peça 11 ainda precisa de sincronização.

## 1. Identidade e números sustentados

Kaori é Descendente, Bastião, Muro, nível 2 e Grau 4. Força é o atributo escolhido de sua técnica. Atributos: Força 3, Constituição 2, Destreza 2, Inteligência 1, Essência 1. TR Físico travado em Força; treinada em Físico e Vigor. Maestria 1 e Refino 1.

| Informação | Conta | Resultado |
|---|---|---:|
| Atributos | 3 + 2 + 2 + 1 + 1 | 9, nenhum acima de 3 |
| Vida | (12 + 2) + (7 + 2) | 23 |
| Integridade | 25 + 1 | 26 |
| PE | 4 × 2 | 8 |
| Defesa | 10 + 2 + proteção 1 | 13 |
| Bloquear, se escolhido | 2d10 + (13 − 11) | 2d10 + 2 |
| Iniciativa | d20 + Destreza | d20 + 2 |
| Ataque de conjuração | d20 + Força + maestria | d20 + 4 |
| Ataque desarmado, acerto | d20 + Força + maestria | d20 + 4 |
| CD de feitiço | 8 + Força + maestria | 12 |
| Provocar, pelo Bastião | d20 + Força + maestria | d20 + 4 |
| TR Físico treinado | d20 + Força + maestria | d20 + 4 |
| TR Vigor treinado | d20 + Constituição + maestria | d20 + 3 |
| TR Intelecto e Espírito, sem treino | d20 + respectivo atributo | d20 + 1 cada |
| Deslocamento base | criação nível 2 | 9 m |
| Limite da provocação inicial | piso(Força ÷ 2) + 1 | 2 inimigos |
| Espaços normais conhecidos | 2 + piso(nível ÷ 2) | 3 |
| Feitiços de Classe 0 | progressão inicial | 2, fora desses espaços |

A proteção 1 pode resultar do Traje de degrau 1 concedido na criação ou de Cobrir-se de energia sem Traje/Revestimento. **Não somar os dois.** A Defesa 13 está correta em ambos os casos, mas o piloto precisa dizer o que ela veste se for explicar a origem da proteção ou usar a Reação de Cobrir-se. Escudo ou compra adicional não estão declarados na mini-ficha; não os pressupor.

As nove perícias declaradas fecham: Atletismo e Provocar; Sentir Energia, Percepção, Sobrevivência, Intuição e Persuasão; Hierarquia e História. Forja e Herbalismo são os dois ofícios, da Origem. Não é necessário ensinar todas essas entradas na cena, mas uma ficha chamada completa deve incluí-las e atribuí-las corretamente.

## 2. Peso nas Mãos: composição que sustenta o resultado

A técnica usa a Regra “Tudo que eu prendo entre as minhas mãos fica mais pesado”. Famílias Livres: Controle e Castigo. Fechadas: Amparo, Área e Auxiliares. Selo: as duas mãos precisam se tocar antes da conjuração. A descrição do feitiço acrescenta o contato de ambas as mãos com o alvo.

| Componente | Regra aplicada | Valor |
|---|---|---:|
| Classe | Classe 1 está disponível no nível 2 | 1 |
| Orçamento | 3 × Classe | 3 pontos |
| Forma | Toque, um alvo a 1,5 m, rolagem de acerto | 0 de custo de Forma |
| Restrição embutida | Corpo a Corpo, devolução Média | +1 ponto |
| Melhoria | Condição: Derrubado, Leve, Família Controle | −1 ponto |
| Desconto da Família Livre | não reduz o preço abaixo de 1 | preço permanece 1 |
| Dados | 3 − 1 + 1 | 3d8 |
| PE da conjuração | 3 × Classe | 3 PE |
| Ação | Conjurar, sem Rápido, Reação ou Atrasar | Ação Padrão |
| Acerto | d20 + Força 3 + maestria 1 contra Defesa | d20 + 4 |
| Tipo | escrito no tutorial | Concussão |

A devolução do Toque paga a Melhoria; **não acrescenta um quarto dado**. Esse cálculo também está registrado em `sistema/05-material/livro/ESTADO-revisao.md`, **5 · Quick-start**, que explica a montagem histórica de Peso nas Mãos. A regra geral atual mantém esse orçamento legal.

Não somar Força aos 3d8 do feitiço, nem somar o soco, nem Canalizar em Golpe. Força já participa do acerto e da CD; a ficha é de um feitiço de Toque, não de um ataque de arma que ganha um feitiço grátis junto.

O Selo não custa ação própria nem concede pontos de Restrição. Não vender novamente o mesmo requisito como Gesto ou Restrição Própria. O procedimento normal da Ação Padrão já inclui cumprir o Selo.

**Derrubado:** a Condição Leve é aplicada no acerto e dura uma rodada, sem compra de Concentrada ou Duradoura. Não foi encontrada exigência de um TR adicional imediato para essa Condição Leve nessa montagem; não inserir um teste por costume de outro sistema. Enquanto durar, alvo rasteja com metade do deslocamento, ataca com desvantagem, recebe ataques com vantagem a até 1,5 m e com desvantagem de mais longe. O capítulo de condições distingue o levantar por Ação de Movimento “quando não for efeito de duração”. Se o piloto avançar ao turno seguinte do inimigo, deve tratar essa distinção explicitamente; não ensinar que levantar sempre cancela qualquer Derrubado de feitiço.

**Reserva:** conjurar uma vez, sem outro gasto, leva Kaori de 8 para 5 PE. O feitiço custa PE mesmo que não acerte; o texto de Energia cobra para conjurar, não só quando causa dano. A CD 12 não entra nessa resolução de ataque contra Defesa: pode constar na ficha, mas não substitui a rolagem de acerto.

## 3. Olhos Em Mim e Alicerce

**Olhos Em Mim:** Ação Bônus, área móvel de raio 6 m, até o fim da cena. Não há custo de PE declarado. Pode ser encerrada como ação livre no turno de Kaori.

Ao ativar, **uma vez por cena**, pode tentar Provocar até dois inimigos que já estejam dentro da área. Isso integra a ativação; não cobra outra Ação Bônus. Kaori usa Provocar com Força pelo Bastião, portanto rola d20 + 4. O alvo faz TR de Espírito; **não é automaticamente CD de feitiço 12**. Na falha do alvo, a regra de Provocar concede vantagem aos ataques dele contra Kaori e desvantagem contra outras criaturas, até o começo do próximo turno dela. A área dura mais que a provocação. Reabrir a área não renova automaticamente a provocação inicial.

**Assumir um golpe:** requer a área ativa, um aliado dentro dela e um ataque com rolagem declarado contra esse aliado. Kaori decide **antes da rolagem de acerto**, gasta Reação e vira alvo; usa Defesa 13 ou Bloquear 2d10 + 2. Bloquear não cobra outra Reação. A interceptação não exige mover Kaori e preserva o alcance já declarado contra o aliado. Protege um ataque, não toda uma ação com vários ataques. Um ataque originalmente contra a própria Kaori não é esse gatilho.

**Alicerce:** ao fim do último descanso longo, Kaori escolheu Cortante e Concussão. Enquanto Olhos Em Mim estiver ativo, recebe metade desses danos. Não gasta outra ação ou PE para “ligar Alicerce”: a proteção acompanha o estado de Olhos Em Mim. Não concede proteção contra todo dano físico; Perfurante não foi escolhido.

Exemplos aritméticos: um golpe Cortante total de 6 vira 3. Se usar total ímpar 5, a regra geral de arredondar contra quem recebe o benefício conduz a 3 de dano recebido. Para o primeiro exemplo didático, dano par evita acrescentar a regra de fração antes de ela ser ensinada.

## 4. Sequência da cena: o que já fecha e o que falta declarar

Esta é uma trilha de verificação, não nova versão redigida do tutorial.

1. **Iniciativa:** Kaori tira 11 + 2 = 13. A maldição tira 16 + 3 = 19 e age primeiro. A Destreza 3 da maldição só aparece na prosa; deve estar no bloco se o leitor puder repetir a cena com rolagens próprias.
2. **Primeiro golpe:** Olhos Em Mim ainda não está ativo, portanto Alicerce não reduz dano. O exemplo usa Defesa 13; escolher não Bloquear é permitido. Se o dano total for 5, Kaori vai a 18 de vida. Separar valor do dado e total: “sai 5” é ambíguo em `1d6 + 2`; d6 = 3 produz o total 5 preservado pelo exemplo.
3. **Turno de Kaori:** Ação Bônus e Ação Padrão são recursos independentes. Ela **pode ativar Olhos Em Mim e conjurar Peso nas Mãos no mesmo turno**. Não são opções mutuamente excludentes. Olhos Em Mim é habilidade do Caminho, não segundo feitiço; a regra geral de dois feitiços não cria impedimento aqui.
4. **Distância:** Peso nas Mãos exige alvo a até 1,5 m e mãos disponíveis para seu Selo/contato. A mini-cena diz que a maldição avança para atacar Kaori e depois que Kaori anda até ela, sem mapear a posição. Definir a posição inicial e o alcance do ataque inimigo é necessário para provar o movimento. Não supor um deslocamento arbitrário da maldição.
5. **Conjuração:** gastar a Padrão, cumprir o Selo e pagar 3 PE; reserva 8 → 5. Acerto já escrito: 12 + 4 = 16 contra Defesa 12. Dano já escrito: 3d8 total 14; Vida 14 → 0. Se quiser mostrar cada dado, 4 + 5 + 5 = 14 é uma decomposição ilustrativa possível, não dado registrado no arquivo original.
6. **Fim:** Kaori permanece com 18 de vida e 5 PE nesse ramo, sem outros gastos/ataques. Se a área foi ativada, está ativa até o fim da cena; a Reação permanece disponível se não foi usada. Não declarar cura ou recuperação automática no fim da luta.

**Lacuna impeditiva para resolver Provocar numericamente:** a Maldição Menor tem Vida 14, Defesa 12, ataque +3, dano 1d6 + 2 e Destreza 3 na prosa, mas **não declara Espírito nem treino/bônus do TR de Espírito**. Não é possível escrever um resultado auditável da provocação usando só o bloco publicado. É preciso completar o inimigo como tarefa de autoria do piloto e validar esse dado na fonte escolhida; não inventar uma CD ou interpretar +3 de ataque como TR.

**Lacuna para demonstrar a Reação de proteção:** a cena não fornece um aliado com posição e ataque dirigido a ele. Pode-se explicar a habilidade na ficha; demonstrá-la exige uma configuração de cena explícita. Não fingir que o ataque direto a Kaori prova Assumir um golpe.

**Se houver sobrevivência:** o caminho da maldição no turno seguinte depende de ela estar Derrubada, ter ou não sofrido Provocar e de quando termina cada efeito. Não simular esse ramo como se só existissem Vida e Defesa.

**Se houver recuo:** abandonar o alcance corpo a corpo pode provocar ataque de oportunidade; Desengajar custa Padrão. “Recuar e negociar” não é pacote gratuito publicado. Conversar/Influenciar depende da situação e da arbitragem; não prometer que a maldição pode sempre ser negociada ou que isso ignora as ações de combate.

## 5. Divergências e omissões a sanear antes de usar a amostra como gabarito

### A. Dano do soco e Canalizar: fontes divergem

- Tutorial, linha 50: soco `d4 + 3`.
- Equipamento, **Soco**: no nível 2/maestria 1, dado d4, soma Força; soco conta como arma para efeitos de regra.
- Aptidões do livro, **Canalizar energia**, linha 151: dá **1d4 extra no Refino 1**, 2d4 no 3, 3d4 no 6, 4d4 no 9. Seu exemplo, linha 159, aplica o extra ao soco.
- Peça `11-aptidoes-e-refino.md`, **§6.9, A escada**: Refino 1–2 dá **zero**, Refino 3 dá 1d4, 6 dá 2d4, 9 dá 3d4 e 10 dá 4d6.

**A busca localizada no histórico encontrou a decisão que resolve a precedência:** `logs/CHANGELOG.md`, **v0.176 — 29/08/2026**, seção **1 · A revisão mexeu em REGRA, e não só em texto**, linha 7740. O registro explica que o Mizuki devolveu uma revisão autoral do Word com mudanças mecânicas e lista expressamente: Canalizar energia e Estímulo Muscular passaram de **1d4 no Refino 3 para 1d4 já no Refino 1, chegando a 4d4 no 9**. É posterior à criação da §6.9 na v0.158. A busca pelas referências de Canalizar/dano na arma nas entradas posteriores não encontrou reversão desse degrau inicial.

Portanto o catálogo do livro acompanha a decisão posterior; **a tabela da peça 11 está desatualizada**. O dado próprio do soco continua d4 + 3; **um soco elegível com Canalizar no Refino 1 soma mais 1d4, total 2d4 + 3**. A mini-ficha só apresenta o dano básico e não distingue o total imbuído. A aplicação do piloto não deve atualizar um arquivo isolado: há propagação documental e proteção de validação a reconciliar. Essa correção não exige inventar uma nova regra nem pedir uma nova escolha do valor já decidido.

A abertura do capítulo de aptidões ainda fala em dano de refino apenas na rodada sem conjuração; o bloco local enfatiza apenas que não entra no mesmo ataque que já carrega feitiço. Para o ramo simples de uma Padrão de Peso nas Mãos, **não há soco adicional**, portanto não é necessário resolver agora todos os casos de interação para ensinar esse feitiço. Registrar a divergência antes de estender o piloto a reações e golpes mistos.

### B. Peso nas Mãos está legal, mas sua apresentação omite informação

Faltam 3 PE e atualização da reserva, componentes do orçamento e duração de Derrubado. O texto de Kaori se diz ligado a uma “ficha completa”, mas apresenta só este feitiço: os outros dois de Classe 1 e os dois de Classe 0 não estão definidos nessas duas seções. Uma mini-ficha suficiente para o ramo guiado não é ainda uma ficha completa para escolhas abertas.

### C. Olhos Em Mim omite limites no resumo

O tutorial não explicita “provocação inicial uma vez por cena”, o TR de Espírito, o efeito e a duração de Provocar. Preservar a distinção entre área persistente e provocação temporária. Não há erro no raio 6 m nem no limite de dois alvos. Alicerce está descrito de maneira compatível com a habilidade integrada.

### D. Dono dos ofícios está trocado no capítulo de criação

O capítulo 20, **Características do Caminho** e tabela **Treino na criação** (linhas 152–153), põe dois ofícios no Caminho e nenhum na Origem. A prosa imediatamente abaixo, a ficha de Kaori, a peça 08 e o Bastião integrado colocam os dois na Origem. O total permanece dois, por isso conferir só a soma não pega o erro. O piloto de primeira escolha não deve reproduzir a tabela divergente.

### E. A escolha de atributo da técnica foi omitida do roteiro publicado

O **Passo 5** do capítulo 20 começa pela Descrição e não oferece explicitamente a escolha/trava do atributo. A seção **Técnica** da Kaori nesse capítulo também não o declara; a tabela de acerto presume Força. A peça 08 **Passo 5** e sua ficha de Kaori declaram Força, e o próprio tutorial o escreve na mini-ficha. O gabarito precisa mostrar a escolha antes de derivar d20 + 4 e CD 12.

### F. Biblioteca foi resumida sem o gatilho de falha

Kaori no capítulo de criação descreve Biblioteca como refazer um teste de História ou Ocultismo uma vez por cena. O catálogo de Descendente especifica **um teste que você falhou**. Isso não interfere no ramo de combate atual, mas impede usar a ficha resumida como fonte suficiente se o piloto incluir investigação/conhecimento antes da porta.

### G. Escada de CD está divergente nos resumos

Fonte responsável: `sistema/03-mecanica/04-pericias-e-testes.md`, **§2.1 A escada fixa — para o que não tem nível**: seis degraus **6, 10, 14, 18, 22 e 26**. O glossário publica 10–26; a introdução da tabela de Como Jogar fala em cinco degraus apesar de seis linhas. Não redefine a CD 12 dos feitiços de Kaori: são funções distintas. Corrigir a referência antes de selecionar uma CD de investigação ou interação no piloto.

### H. Resultado de dado e total precisam ser separados

No ataque da maldição, “sai 17” pode significar o d20 ou a soma; ambos acertam Defesa 13. No dano, “sai 5” muda o resultado: d6 = 5 faria 7 de dano e Vida 16; total 5 faz Vida 18. Para conservar a conta publicada, explicitar d6 = 3, +2, total 5. Isso é clarificação do exemplo, não alteração do ataque inimigo.

## 6. Fronteira prática do piloto

É possível planejar com segurança o núcleo **iniciativa → ataque contra Defesa → Vida → Padrão de feitiço → PE → acerto → dano**, usando os números acima e sanando as omissões de apresentação.

Para publicar também um exemplo completo de **provocação**, falta o TR do inimigo. Para publicar **interceptação**, falta um aliado e posições. Para ensinar **soco**, propagar e conferir a decisão já encontrada de Canalizar (v0.176), distinguindo dano próprio de dano adicional. Para chamar a ficha de **completa**, definir o restante do repertório e equipamento e conciliar a Origem futura. Para criar um exemplo de **teste fora de combate**, usar a escada da fonte responsável e os gatilhos completos dos Legados.

O ramo principal pode permanecer em Peso nas Mãos e deixar soco e Provocar para quadros posteriores. Isso reduz a carga de ensino e não suspende nenhuma habilidade da personagem. Não são razões para paralisar o planejamento: são tarefas delimitadas de preparação da amostra. A narrativa e o layout podem ser desenhados ao redor desse núcleo; dados ainda ausentes devem ser identificados como pendentes, nunca apresentados como regras já publicadas.
