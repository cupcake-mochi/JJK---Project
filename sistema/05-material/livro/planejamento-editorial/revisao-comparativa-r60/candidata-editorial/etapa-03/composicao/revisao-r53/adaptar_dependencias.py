from pathlib import Path
import json,re,unicodedata,argparse
B=Path(__file__).resolve().parents[1];R=B/'revisao-r53'
args=argparse.ArgumentParser();args.add_argument('--forma-fluida',choices=['preservar-funcao','somente-forma']);opt=args.parse_args()
texts=json.loads((R/'TEXTOS-TRABALHO.json').read_text());old=json.loads((R/'BLOCOS-R52.json').read_text())
meta=json.loads((R/'META-NOVA.json').read_text());aliases=json.loads((R/'ALIASES.json').read_text());entries=json.loads((R/'ENTRADAS.json').read_text())
notes={}
def change(k,a,z,reason):
 assert a in texts[k],(k,a)
 texts[k]=texts[k].replace(a,z)
 notes.setdefault(k,[]).append(reason)

def replace_all(k,changes,reason):
 for a,z in changes:change(k,a,z,reason)

change('ab--ab-kaori','recebe 1 pela limitação de Corpo a Corpo da Forma Toque','recebe a devolução Leve de 1 ponto de Toque, sem ocupar vaga de Restrição','Toque concede devolução própria, sem a antiga Restrição embutida.')
change('rotas--rota-fisga','Corpo a Corpo já acompanha Toque e devolve 1 ponto, exatamente o gasto.','Toque devolve Leve, que vale 1 ponto nessa Classe, sem ocupar vaga de Restrição. A devolução recupera exatamente o gasto.','Preservar o exemplo com a devolução aprovada de Toque.')
change('rotas--rota-redoma','Corpo a Corpo devolve esse ponto.','Toque devolve esse ponto como devolução Leve, sem ocupar vaga de Restrição.','Atualizar o cálculo da proximidade sem mudar a ficha de Classe 1.')
replace_all('rotas--rota-espinho',[
 ('Corpo a Corpo devolve 2, até o gasto. O saldo fica **6 − 2 + 2 = 6**.','Toque devolve Leve, que vale 1 ponto na Classe 2, sem ocupar vaga de Restrição. O saldo fica **6 − 2 + 1 = 5**.'),('causa **6d8 de Força**','causa **5d8 de Força**')], 'Recalcular a reação de Classe 2 pela devolução Leve de Toque.')
replace_all('rotas--rota-bancada',[
 ('Nao monta **Apoio + Guarda**, de Classe 1. Apoio custa 0 pontos e Guarda custa 1.','Nao escolhe vida temporária como função e monta **Projétil + Guarda**, de Classe 1. Projétil custa 0 pontos e Guarda custa 1.'),
 ('Essa cura não se torna Energia Reversa pela escolha da Forma Cura.','Escolher a função de cura conserva os corpos e materiais que a Regra permite tratar.')], 'Separar função de vida temporária, Forma e peça de proteção, conservando os números do exemplo.')
replace_all('rotas--rota-sutura',[
 ('Caio monta **Cura**, Classe 1, sem Melhorias ou Restrições. A Forma custa 1 ponto.','Caio escolhe cura direta e a Forma **Projétil**, Classe 1, sem Melhorias ou Restrições. A base Média de cura custa 1 ponto e Projétil custa 0.'),
 ('dentro do limite da Forma.','dentro do teto da cura individual.'),
 ('utiliza a Forma Cura com seus próprios custos.','usa a função de cura com seus próprios custos e sua Forma registrada.')], 'Manter a cura individual aprovada, com função e entrega separadas.')
replace_all('rotas--rota-cura',[
 ('Um **Manejo com Forma Cura**','Um **Manejo com a função de cura direta**'),
 ('seguindo a Forma e sua Classe.','quando a Forma escolhida e sua Classe permitirem essa distância.'),
 ('Escolher Forma Cura não muda','Escolher a função de cura não muda'),
 ('Um Manejo de Forma Cura produzido por Energia Reversa','Um Manejo de cura individual produzido por Energia Reversa'),
 ('A Forma Cura e a aptidão conservam suas diferentes ações, custos e requisitos.','O Manejo de cura e a aptidão conservam suas próprias ações, custos e requisitos.')], 'Atualizar a interface da semente Energia Reversa com a função de cura.')
replace_all('aptidoes--apt-reversa',[('um feitiço da Forma Cura','um feitiço com função de cura individual')], 'Remissão à função de cura individual.')
replace_all('aptidoes--apt-energia-positiva',[
 ('um feitiço da **Forma Cura**','um feitiço com **função de cura individual**'),
 ('os dados que a Forma destinou à cura','os dados destinados à cura daquele alvo'),
 ('nem transforma automaticamente a Forma Onda em um ataque de área.','e continua sendo uma aplicação ofensiva contra uma única maldição; cura coletiva não se converte em dano de área por esta aptidão.')], 'Conservar a exceção ofensiva de Energia Reversa, sem ampliar a antiga permissão individual para a nova cura coletiva.')
replace_all('construcao--entidade-cao-habilidades',[
 ('Corpo a Corpo devolve somente esse ponto gasto.','A devolução Leve de Toque recupera somente esse ponto gasto, sem ocupar vaga de Restrição.')], 'Atualizar o exemplo do cão sem alterar o dano de Mordida precisa.')
replace_all('construcao--entidade-vigia-habilidades',[
 ('**Básica de Classe 0. Apoio + Impulso.** A base seria 2d6, mas esta Forma não causa dano. Impulso usa a única Melhoria Leve permitida. Um aliado disposto a até **4,5 m** recebe vantagem no próximo teste que fizer até o fim do próximo turno dele. O benefício termina depois desse teste e não modifica dano.',
  '**Básica de Classe 0. Projétil + Firmeza: perícia.** A base seria 2d6. Firmeza usa a única Melhoria Leve permitida e a aplicação abre mão dos dados restantes. Um aliado disposto a até **4,5 m** recebe vantagem no próximo teste de perícia que fizer até o começo do próximo turno de Bruna. O benefício termina depois desse teste e não modifica dano.'),
 ('**Especial de Classe 2. Apoio + Guarda + Empurrão.** Apoio custa 0.','**Especial de Classe 2. Vida temporária, com Projétil + Guarda + Empurrão.** Projétil custa 0.'),
 ('**Especial de Classe 1. Cura, sem Melhorias ou Restrições.** A Forma custa 1.','**Especial de Classe 1. Cura direta com Projétil, sem Melhorias ou Restrições.** A base Média custa 1 e Projétil custa 0.')], 'Adaptar a ficha do vigia às seis Formas; Orientação usa a categoria perícia de Firmeza e termina no começo do próximo turno da invocadora, conservando o prazo da Melhoria e a iniciativa compartilhada.')
replace_all('ritual--rit-beneficios',[
 ('Cura ou Apoio alcança um aliado adicional','Cura ou vida temporária individual alcança um aliado adicional')], 'A linha de Compartilhamento passa a nomear as funções permitidas.')
replace_all('ritual--rit-parcelas',[
 ('Só na aplicação benéfica de Cura ou Apoio,','Só na aplicação benéfica de cura ou vida temporária individual,'),
 ('Com Junto, a origem deve ser','Com Mais Um, a origem deve ser'),
 ('Compartilhamento não amplia uma Onda.','Compartilhamento não amplia uma aplicação de cura ou apoio coletivo em área.'),
 ('Apoio dividido em 6 e 3 de vida temporária','Vida temporária dividida por Mais Um em 6 e 3')], 'Preservar a cópia individual do Ritual, usando Mais Um e mantendo a exclusão de benefícios coletivos.')
replace_all('ritual--rit-limites',[
 ('Alcance e Corpo a Corpo','Alcance e Queima-Roupa'),
 ('Não combine. Toque e distância limitada conservam sua exigência.','Não combine. Toque conserva seu alcance; Queima-Roupa conserva o limite dos alvos de Projétil ou a origem da área, conforme sua entrada.')], 'Atualizar a incompatibilidade de Ritual de Alcance com a Restrição de proximidade.')
replace_all('emanador--ema-remodelar',[
 ('| Forma Apoio | 3 de vida temporária. |','| Vida temporária | 3 de vida temporária. |')], 'Nomear a função que paga a diferença de custo de Remodelar.')
change('emanador--ema-remodelar','Se não houver resultado suficiente para pagar a diferença, essa versão não pode ser usada.','Numa mescla, retire a diferença das parcelas de dano, cura ou vida temporária registradas, sem aumentar nenhuma delas nem transferir saldo entre funções. Se não houver resultado suficiente para pagar a diferença, essa versão não pode ser usada.','Preservar a distribuição das funções nas Remodelagens de mesclas.')
replace_all('emanador--ema-instintiva',[('Impulso, Dívida e outros custos independentes','Impulso, Sobrecusto e outros custos independentes')], 'Sobrecusto substitui Dívida no catálogo aprovado.')
replace_all('emanador--ema-modulacoes',[
 ('Acrescentar alvo e dividir os dados.','Acrescentar um destinatário elegível, seguindo a distribuição de Mais Um.')], 'Divisão usa Mais Um também nas aplicações sem dano, conforme o protótipo aprovado.')
replace_all('emanador--ema-manifestacao',[
 ('Toque e Aura não podem afastar sua aplicação mantendo Corpo a Corpo. Uma Forma que precise permanecer centrada em você conserva essa exigência.','Toque conserva sua distância ao alvo. Aura permanece centrada em você. Queima-Roupa conserva seus alvos a até 1,5 m em Projétil ou a origem da área em você, conforme a Forma escolhida.')], 'A origem concedida por Manifestação Condutora conserva as limitações aprovadas de Toque, Aura e Queima-Roupa.')
replace_all('evocador--ev-multiplas-conduzir',[
 ('Toque e Corpo a Corpo conservam seus requisitos em relação a ela.','Toque e Queima-Roupa conservam seus requisitos em relação à executora.')], 'Aplicar a Restrição de proximidade à executora da especial.')
change('origens--restricao-menores-corporais','A escolha não se limita a Apoio ou Efeito. Esses feitiços não viram espaços comuns para Talentos ou invocações.','Esses feitiços podem usar qualquer função compatível com a técnica e permitida na Classe 0. Eles não viram espaços comuns para Talentos ou invocações.','Atualizar apenas os nomes das funções da menor Prática Cotidiana; seu benefício permanece igual.')

# Forma Fluida aguarda a resposta do autor; as outras dependências avançam.
if opt.forma_fluida:
 k='emanador--ema-forma'
 change(k,'Recalcule as limitações da Forma, suas devoluções e seus limites de resultado. Ao trocar Toque ou Aura por uma Forma sem Corpo a Corpo, retire essa devolução. Não mantenha os pontos de uma exigência que deixou de existir.',
  'Recalcule os custos e limites da Forma e das funções, incluindo a base Média e as devoluções aproveitáveis. Toque concede devolução Leve sem ocupar vaga de Restrição; Aura não concede devolução. Uma troca que deixe uma Restrição incompatível exige retirar sua devolução e conferir a montagem novamente.','Aplicar os preços e a proximidade do capítulo aprovado.')
 change(k,'Se a troca mudar dano, cura ou apoio, compare o saldo útil em pontos antes de fazer a nova conversão. A versão não pode ganhar saldo pela troca e ainda respeita o teto da nova Forma. Melhorias e Restrições preservadas precisam funcionar com ela.',
  'A versão não pode ganhar saldo pela troca e respeita os tetos das funções resultantes. Melhorias e Restrições preservadas precisam funcionar com ela.','Separar funções e Forma no texto da habilidade.')
 change(k,'> **Exemplo.** Uma Aura de Classe 3, sem desconto, tem Fura: custo 2 + 3, com devolução 3 de Corpo a Corpo. Causa **7d8**. Trocá-la por Explosão mantém o preço da Forma, mas retira a devolução: a versão passa a **4d8**. O PE adicional de Remodelar continua sendo 2.',
  '> **Exemplo.** Uma Aura de Classe 3 com Fura, sem descontos ou Restrições, custa 2 + 3 pontos e causa **4d8**. Trocá-la por Explosão aumenta o custo da Forma de 2 para 3: a versão passa a **3d8**. O PE adicional de Remodelar continua sendo 2.','Recalcular o exemplo com Aura Leve, Explosão Média e sem a devolução antiga.')
 if opt.forma_fluida=='preservar-funcao':
  change(k,'Ao Remodelar, pode trocar a **Forma** em vez de uma Melhoria. Os pontos da Forma retirada ajudam a pagar a nova. A diferença positiva retira resultado pela regra de Remodelar.',
   'Ao Remodelar, pode trocar a **Forma** ou trocar uma função entre **dano, cura e vida temporária**, em vez de uma Melhoria. Na troca de função, somente os pontos reservados a ela mudam de destino; as outras parcelas permanecem. A nova função precisa ser permitida pelas Famílias e pela Regra. Recalcule a base e a Forma da aplicação; os pontos retirados ajudam a pagar os novos custos. A diferença positiva retira resultado pela regra de Remodelar.','Resposta do autor: conservar a troca de função que antes decorria de mudar a Forma.')
  change(k,'trocar Forma e Melhoria,','trocar Forma ou função e uma Melhoria,','Composição Técnica conserva o limite de duas alterações quando a função é a escolha de Forma Fluida.')
 else:
  change(k,'A diferença positiva retira resultado pela regra de Remodelar.','A diferença positiva retira resultado pela regra de Remodelar. As funções e a distribuição do saldo da ficha permanecem.','Resposta do autor: Forma Fluida troca somente a Forma.')

# Esclarecimento motivado pela dúvida do autor durante a integração.
change('fundamento--funcoes','O saldo determina a quantidade de dano, cura ou vida temporária que o feitiço pode produzir.', 'Escolha as funções quando montar a ficha do feitiço. A conjuração usa as funções registradas nessa ficha. O saldo determina a quantidade de dano, cura ou vida temporária que o feitiço pode produzir.', 'Explicitar o momento da escolha das funções, sem alterar a regra aprovada.')
change('rotas--rota-sem-tecnica','Talentos deste capítulo','Talentos do Catálogo de criação','A remissão acompanha a distribuição do protótipo entre os capítulos do livro.')

# Clareza das rotas, solicitada pelo autor durante a integração.
k='rotas--rotas'
eligibility=re.search(r'\| Rota \| Quem a usa \|.*?(?=\n\n)',texts[k],re.S)[0]
new_intro='''# Rotas de criação

Sem Técnica e Técnica Marcial usam o procedimento de Fundamento para criar suas aplicações. Você escreve o funcionamento do seu poder e prepara uma ficha para cada aplicação aprendida. A rota determina de onde esse funcionamento vem e os requisitos para executá-lo.

Na rota **Sem Técnica**, você desenvolve uma aptidão escolhida como **semente**. Suas aplicações preparadas se chamam **Manejos**. Na **Técnica Marcial**, você desenvolve um estilo ligado a armas ou a uma ferramenta amaldiçoada. Suas aplicações se chamam **Katas**.

Sua Origem indica as rotas disponíveis. Confira essa escolha em [Origens](#origens--origem-escolhas) antes de criar seu repertório.

'''+eligibility+'''

## Como montar Manejos e Katas

Use esta sequência depois de escolher sua rota. Consulte [Montar sua aplicação](#fundamento--fundamento) para as tabelas e as regras de cada escolha.

1. **Defina o funcionamento.** Na seção da rota, escolha a semente ou o equipamento e escreva a Descrição e a Regra. Registre também atributo, Selo e Expressão da técnica conforme aquela rota.
2. **Escolha as Famílias.** Use as mesmas escolhas de Famílias Livres e Fechadas de Fundamento. A Regra e os requisitos da rota também limitam as funções que você pode montar.
3. **Escolha a função e a Forma de cada aplicação.** Decida se aquele Manejo ou Kata causa dano, cura, protege ou produz outro efeito permitido. Escolha como alcança os alvos. Uma mescla registra suas funções e a distribuição dos pontos na ficha.
4. **Monte na Classe disponível.** Use a mesma tabela de pontos e PE, compre as Melhorias e escolha Restrições compatíveis. Aplique os descontos, devoluções e limites normais.
5. **Registre e resolva.** Anote ação, alcance, alvos, ataque ou TR, resultado e duração. Coloque a aplicação no seu repertório. Ao usá-la, cumpra o Selo e pague os custos dessa ficha.

Quando uma regra mencionar **feitiço**, ela também alcança Manejos e Katas, salvo uma exceção expressa. Seus limites de conjuração, condições e demais procedimentos seguem as regras comuns. A tabela mostra os nomes usados por cada rota.

| Regra comum | Técnica amaldiçoada | Sem Técnica | Técnica Marcial |
|---|---|---|---|
| Aplicação preparada | Feitiço. | Manejo. | Kata. |
| Liberação Máxima | Liberação Máxima. | Liberação Máxima. | Ruptura. |
| Técnica Máxima | Técnica Máxima. | Auge. | Ōgi. |

**PE** significa Pontos de Energia para quem possui energia amaldiçoada e Pontos de Esforço para quem não possui. O Caminho entrega a mesma quantidade e cada regra cobra o mesmo valor. Recuperar PE ou pagar uma Kata não faz surgir energia amaldiçoada num personagem que nasceu sem ela.

Uma Kata pode produzir um efeito sobrenatural por meio de um equipamento amaldiçoado. Isso não concede ao usuário sentidos de energia, aptidões ou outras capacidades ausentes de sua Origem. O personagem Sem Técnica conserva sua energia amaldiçoada e desenvolve as aplicações permitidas pela semente.

O Restringido **Sem Energia** usa Técnica Marcial, com Lapidação e Bênçãos, sem exigir Refino. O **Corpo Amaldiçoado** pode usar Técnica Marcial conservando sua energia, Refino e aptidões. A **Restrição corporal** segue o Fundamento comum e mantém seus benefícios de Origem, incluindo o Talento extra e Saída Elevada.

As próximas seções explicam as escolhas de cada rota. Para acompanhar uma primeira montagem completa, consulte [Fisga](#rotas--rota-fisga), de Técnica Marcial, ou [Redoma](#rotas--rota-redoma), de Sem Técnica. As habilidades das entidades usam orçamento, Famílias e regras próprios, em [Construir invocações](#construcao--entidades-criar).
'''
change(k,texts[k],new_intro.strip(),'Reescrever a apresentação das duas rotas com procedimento compartilhado, origem da Regra, nomes equivalentes e remissões para as primeiras fichas. Nenhuma aquisição, requisito ou custo foi alterado.')
meta[k]={'capitulo':13,'contexto':'Rotas de criação','origem':'Revisão de compreensão pedida pelo autor durante a integração','titulos':[{'titulo':'Rotas de criação','tipo':'h1','tratamento':None,'nivel_editorial':1},{'titulo':'Como montar Manejos e Katas','tipo':'h2','tratamento':'grupo','nivel_editorial':2}]}
aliases['rotas-link-montagem']={'bloco':k,'titulo':'Como montar Manejos e Katas'}
change('rotas--rota-sem-tecnica','4. Escolha as Famílias e monte seus Manejos.','4. Escolha suas Famílias Livres e Fechadas.\n5. Monte cada Manejo por [Como montar Manejos e Katas](#rotas-link-montagem): escolha funções e Forma, pague a montagem da Classe e registre a ficha. Seu repertório usa os espaços de feitiço conhecido de Fundamento.','Mostrar a montagem comum dentro do passo a passo de Sem Técnica.')
change('rotas--rota-sem-tecnica','Seu repertório nasce de uma **semente**: uma aptidão que você estudou e transformou em seu próprio estilo de combate ou apoio.','Seu repertório nasce de uma **semente**: uma aptidão que você estudou e transformou em seu próprio estilo de combate ou apoio. A partir dela, escreva uma Descrição e uma Regra pelos critérios de Fundamento. Cada aplicação preparada dessa Regra é um Manejo, montado com funções, Forma, Melhorias e Restrições.','Explicar como a aptidão dá origem à Regra e à ficha de cada Manejo.')
change('rotas--rota-marcial','Descreva primeiro o funcionamento desse estilo.','A Descrição e a Regra registram o funcionamento desse estilo pelos critérios de Fundamento. Cada aplicação preparada se chama Kata e recebe sua própria ficha de montagem.','Explicar o funcionamento do estilo antes de apresentar as Katas.')
change('rotas--rota-marcial','1. Escreva a **Descrição**, a **Regra** e a **Expressão da técnica** pelo procedimento de Fundamento.\n2. Escolha a rota de arma ou a rota de ferramenta. Essa escolha é permanente.\n3. Registre o equipamento que permite executar suas Katas e o atributo utilizado.\n4. Escolha as Famílias e monte seu repertório. Talentos e entidades usam os mesmos espaços disponíveis para Katas.','1. Escolha a rota de arma ou a rota de ferramenta. Essa escolha é permanente. As seções seguintes definem o equipamento recebido e o atributo das Katas.\n2. Escreva a **Descrição**, a **Regra** e a **Expressão da técnica** do estilo, considerando o equipamento escolhido. Use os critérios de Fundamento.\n3. Registre o equipamento que permite executar suas Katas e o atributo utilizado.\n4. Escolha suas Famílias Livres e Fechadas.\n5. Monte cada Kata por [Como montar Manejos e Katas](#rotas-link-montagem). Seu repertório usa os mesmos espaços de feitiço conhecido de Fundamento; Talentos e entidades também ocupam esses espaços.','Organizar a criação marcial a partir do equipamento e do procedimento comum.')
(R/'META-NOVA.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
(R/'ALIASES.json').write_text(json.dumps(aliases,ensure_ascii=False,indent=2)+'\n')

# Glossário: definições breves adequadas à nova montagem.
k='consulta--consulta-glossario-3'
change(k,'[Família](#fundamento--familias). Grupo de Melhorias. Acesso e descontos seguem a rota e a ficha em montagem.','[Família](#fundamento--familias). Grupo que determina o acesso a funções e Melhorias da técnica. Uma Família Livre concede desconto; uma Fechada impede as escolhas indicadas em suas regras.','Definir acesso, funções e descontos na consulta breve.')
change(k,'[Forma](#fundamento--formas). Peça inicial da aplicação, que define alvos, origem, alcance e resolução conforme sua entrada.','[Forma](#fundamento--formas). Define como o feitiço alcança seus alvos e qual área ocupa. A função determina o efeito produzido.','Distinguir entrega e efeito no glossário.')
change(k,'[Fundamento](#fundamento--fundamento).','[Função](#fundamento--funcoes). Efeito produzido pelo feitiço, como dano, cura ou proteção. Sua quantidade segue o saldo reservado ou a Melhoria escolhida.\n\n[Fundamento](#fundamento--fundamento).','Acrescentar a função ao vocabulário de consulta.')

# Índice: remover nomes retirados e oferecer cada entrada do novo catálogo.
# Ajuste solicitado pelo autor durante a integração: vida temporária individual
# passa a pagar uma base Leve. A base única das mesclas continua compartilhada.
change('fundamento--funcoes',
 '| Vida temporária individual | 0 |',
 '| Vida temporária individual | Leve |',
 'Decisão do autor: cobrar Leve pela função de vida temporária individual.')
change('fundamento--funcoes',
 '**Pague a base Média uma vez** quando a aplicação tiver cura direta ou oferecer coletivamente vida temporária, Guarda, Impulso ou Firmeza. Essas funções podem compartilhar essa base na mesma ficha. Guarda, Impulso e Firmeza individuais pagam apenas suas Melhorias, sem essa base adicional. Pague a Forma uma vez e cada Melhoria separadamente. Essa regra não reduz automaticamente o custo de outras capacidades próprias.',
 '**Pague uma única base para as funções.** Use Média quando a aplicação tiver cura direta ou oferecer coletivamente vida temporária, Guarda, Impulso ou Firmeza.\n\nNas demais aplicações com vida temporária individual, use Leve. Quando a ficha combinar funções, pague somente a maior base exigida por elas.\n\nGuarda, Impulso e Firmeza individuais pagam apenas suas Melhorias. Pague a Forma uma vez e cada Melhoria separadamente. A base não recebe desconto de Família nem pode ser recuperada por devoluções. Capacidades próprias conservam os custos aprovados em sua criação.',
 'Conservar a base compartilhada das mesclas, agora com Leve para vida temporária individual; a base Média cobre a menor quando ambas forem exigidas.')
change('fundamento--funcoes',
 '### Escolha o destino do saldo',
 '> **Vida temporária na Classe 1.** Um feitiço com Projétil e vida temporária individual, sem Melhorias ou Restrições, começa com 3 pontos. A base Leve custa 1: restam 2 pontos, que concedem **6 de vida temporária**. Toque também precisa pagar essa base; sua devolução só recupera pontos gastos em Melhorias.\n\n### Escolha o destino do saldo',
 'Exemplificar o novo custo e impedir recuperar a base com a devolução de Toque.')
change('fundamento--pontos',
 '**Base:** some o custo das funções e da Forma. A tabela seguinte explica quando existe uma base Média compartilhada.',
 '**Base:** pague a maior base exigida pelas funções e acrescente o custo da Forma. A tabela seguinte apresenta as bases Leve e Média e seu compartilhamento.',
 'Alinhar a ordem de cálculo à base única compartilhada das funções.')
replace_all('fundamento--aplicacoes',[
 ('Na Classe 2 e sem descontos, os custos são **0 + 1 + 2 = 3**, de um orçamento de 6.',
  'Na Classe 2 e sem descontos, a base Leve custa 1, Projétil custa 0, Impulso custa 1 e Pressa custa 2. O total é **1 + 0 + 1 + 2 = 4**, de um orçamento de 6.'),
 ('O saldo 3 concede **9 de vida temporária**.', 'O saldo 2 concede **6 de vida temporária**.')],
 'Recalcular o exemplo de fortalecimento pela base Leve de vida temporária individual.')
replace_all('rotas--rota-bancada',[
 ('Projétil custa 0 pontos e Guarda custa 1. Sem Restrições, restam **3 − 1 = 2 pontos**.',
  'A base Leve custa 1 ponto, Projétil custa 0 e Guarda custa 1. Sem Restrições, restam **3 − 1 − 1 = 1 ponto**.'),
 ('**6 pontos de vida temporária**','**3 pontos de vida temporária**')],
 'Recalcular Placas de apoio com a base Leve, conservando Guarda e a ausência de Restrições.')
change('emanador--ema-forma','incluindo a base Média e as devoluções aproveitáveis.','incluindo a base devida e as devoluções aproveitáveis.',
 'A troca de Forma confere também a base Leve de vida temporária individual, sem mudar a função.')
change('construcao--entidades-formas',
 'A base Média é compartilhada nos mesmos casos da montagem comum e deve ser paga integralmente, fora do limite de Melhorias.',
 'As funções usam as bases Leve e Média da montagem comum. Pague somente a maior base exigida pela ficha, integralmente e fora do limite de Melhorias.',
 'Estender o custo Leve de vida temporária individual à montagem das entidades, conservando a base única das mesclas.')
change('construcao--entidades-saldo',
 'Vida temporária individual converte cada ponto em 3, respeitando os limites gerais dessa reserva.',
 'Vida temporária individual paga base Leve e converte cada ponto reservado em 3, até **3 × (pontos da entidade − preço Leve)**, respeitando os limites gerais dessa reserva.',
 'Explicitar o teto decorrente da base Leve nas habilidades de entidade.')
change('construcao--entidade-vigia-habilidades',
 '**Especial de Classe 2. Vida temporária, com Projétil + Guarda + Empurrão.** Projétil custa 0. Guarda custa 2, e Empurrão custa 1. Essas Melhorias não pertencem a Amparo e não recebem seu desconto. Sobram **4 − 2 − 1 = 1 ponto**, convertido em **3 de vida temporária**.',
 '**Especial de Classe 2. Vida temporária, com Projétil + Guarda + Empurrão e a Restrição Parado.** A base Leve custa 1 e Projétil custa 0. Guarda custa 2, e Empurrão custa 1. Essas Melhorias não pertencem a Amparo e não recebem seu desconto. O vigia precisa conservar sua posição: não pode ter se deslocado voluntariamente no turno da aplicação nem fazê-lo depois dela nesse turno. Parado devolve 1 ponto gasto nas Melhorias. Sobram **4 − 1 − 2 − 1 + 1 = 1 ponto**, convertido em **3 de vida temporária**.',
 'Adaptar Tiras de resgate à base Leve: acrescentar Parado efetivamente cumprido pela entidade para preservar a montagem com proteção e movimento.')

index=[]
for key,value in texts.items():
 if key.startswith('consulta--consulta-indice-'):
  index.extend(re.findall(r'^\[([^\]]+)\]\(#([^)]+)\)$',value,re.M))
renames={'Apoio':('Vida temporária','fundamento--funcoes'),'Onda':('Cura e benefícios em área','fundamento--funcoes'),'Corpo a Corpo':('Queima-Roupa',entries['Queima-Roupa']),'Dívida':('Sobrecusto',entries['Sobrecusto'])}
retired={'Certeiro','Junto','Puxa','Adianta','Muito Longe','Muito Maior'}
all_index={}
for term,dest in index:
 if term in retired:continue
 term,dest=renames.get(term,(term,dest))
 all_index[term]=dest
for name,dest in entries.items():all_index[name]=dest
all_index.update({'Funções e saldo':'fundamento--funcoes','Mesclas de funções':'fundamento--mesclas','Toque e proximidade':'fundamento--formas','Melhorias: efeitos':'catalogo--cat-efeitos','Melhorias: modificadores':'catalogo--cat-modificadores'})
# Destinos antigos com títulos retirados passam ao destino preciso da entrada.
specific=json.loads((B/'revisao-de-estrutura/DESTINOS-INDICE.json').read_text())
lookup={x['alias']:x for x in specific}
for term,dest in list(all_index.items()):
 if dest in lookup:
  row=lookup[dest]
  if term in entries:all_index[term]=entries[term]
  elif row.get('bloco') not in texts and row.get('bloco') in aliases:all_index[term]=row['bloco']
all_index=sorted(all_index.items(),key=lambda z:unicodedata.normalize('NFKD',z[0]).encode('ascii','ignore').decode().casefold())
keys=sorted([k for k in texts if k.startswith('consulta--consulta-indice-')],key=lambda k:int(k.rsplit('-',1)[1]))
for i,key in enumerate(keys):
 start=round(i*len(all_index)/len(keys));end=round((i+1)*len(all_index)/len(keys));chunk=all_index[start:end]
 texts[key]='# Índice de assuntos\n\n'+'\n\n'.join(f'[{term}](#{dest})' for term,dest in chunk)
 notes[key]=['Índice atualizado para as entradas e os nomes do catálogo aprovado, sem alterar os demais assuntos.']

(R/'TEXTOS-TRABALHO.json').write_text(json.dumps(texts,ensure_ascii=False,indent=2)+'\n')
(R/'NOTAS-DEPENDENCIAS.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
(R/'DECISAO-FORMA-FLUIDA.json').write_text(json.dumps({'estado':'respondida' if opt.forma_fluida else 'aguardando autor','escolha':opt.forma_fluida},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'blocos_adaptados':len(notes),'forma_fluida':opt.forma_fluida or 'pendente','assuntos_indice':len(all_index)},ensure_ascii=False))
