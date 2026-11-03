# Plano de avaliação da dificuldade dos encontros

Registro 149, 02/11/2026. Plano aprovado pelo autor com as decisões **A1** (a grade da peça 26 entra só como comparação), **B1** (medir na R60) e **C1** (medir os dois modelos de recurso do inimigo). Os resultados e o que foi aplicado ao livro estão no [registro 150](<150-resultados-da-avaliacao-dos-encontros.md>).

Base lida: capítulo 6 (`06-inimigos-e-perigos.md`) e os casos 22, 57, 65, 66, 73, 74, 76 e 100 da `edicao-integrada-136`, o parecer 146, as seções 5 a 7 do plano 98, a `RETOMADA-NUVEM-2026-10-31.txt` e, do lado do sistema, a peça 26 (`sistema/03-mecanica/26-bestiario.md`) e o `bestiario/09-fase-2/APLICACAO.md` da `main`.

---

## 1. O que já existe

**Os números de partida cobrem só os níveis 2 e 6.** Vida central de 24 e 72, ataque +4 e +5, Defesa 13, uma ação ofensiva na Padrão (caso 74). O próprio texto diz que são candidatos, que não se interpola o nível 3 a 5 e que não se multiplica para chegar ao 30.

**As contas medem conjuntos de ataques do grupo, e não rodadas.** O caso 74 calcula a chance de o inimigo continuar de pé depois de 3 ou 6 ataques de três perfis fixos (Bastião, Emanador e Guia), todos alcançando o alvo, sem o inimigo agir. O caso 100 repete isso nos níveis 10, 15, 20, 22, 26 e 30 e avisa que 26 e 30 deram o mesmo resultado porque os perfis usam os mesmos valores.

**Há uma única simulação com o inimigo agindo**, a do Amontoado (caso 57): mediana de 2 rodadas, queda de pelo menos uma pessoa em 20,36% das execuções com o grupo cheio e 60,50% com o grupo pela metade e duas Sequelas por pessoa. Ela usou fichas incompletas, escolhas fixadas antes e socorro simplificado.

**Os outros casos são ensaios guiados**, com resultados escolhidos para ensinar (Sineiro no 73, Toru e Sayo no 76, a saída que fecha no 66).

**Nenhuma mesa real usou essas fichas.** O sistema tem um registro de mesa (`sistema/04-playtest/mesa-01-grupo-01.md`), com outro material.

---

## 2. O que os exemplos ainda não respondem

1. **Tamanho do grupo.** Tudo foi medido com três personagens. Não existe conta para dois, quatro ou seis, e a guilda joga com grupos variados.
2. **Composição.** Os três perfis são Bastião, Emanador e Guia. Vanguarda, Incursor e Evocador não aparecem em nenhuma comparação, e um grupo sem cura ou sem proteção pode ter outro risco.
3. **Estado de entrada.** Só o caso 57 compara grupo cheio contra grupo ferido. Falta o segundo encontro do dia, sem descanso, com PE parcial.
4. **O inimigo agindo de verdade.** Com exceção do 57, nenhuma conta tem o inimigo atacando, controlando ou concentrando num alvo.
5. **Controle.** Ninguém mediu quanto tempo cada personagem passa sem agir por Agarrado, por queda ou por ter de gastar a Padrão escapando.
6. **Um corpo contra vários.** O caso 102 compara 200 PV num corpo com 120/80 em dois no nível 15. Não há a mesma comparação nos níveis baixos.
7. **Objetivo que não é matar.** Retirar a caixa ou o estojo encerra a missão, mas nenhuma medida conta quantas vezes o objetivo é cumprido nem a que custo.
8. **Socorro e retirada.** A janela de socorro existe nas regras e no caso 22, mas falta medir quantas vezes duas pessoas caem perto do mesmo turno, ou o socorrista está longe.
9. **Terreno e informação.** O caso 65 separa mapa original, motor desligado e fechamento ativo, mas sem resultado medido. Se o grupo reconhecer o sinal do Sineiro, a chance de interromper muda, e isso só aparece em mesa ou ensaio.
10. **Níveis altos com as capacidades reais.** Os conjuntos de 10 a 30 usam só ataque básico e feitiço. Duro de Matar, Passa Pra Mim, Chega Mais e Domínio ficam de fora.

---

## 3. Três decisões suas antes de começar

Cada uma muda o que vai ser medido. Trago a recomendação e o porquê.

### D-A. A régua de inimigos do sistema (peça 26) entra na comparação?

O guia exclui os números do "Bestiário antigo" desde a base do piloto. Só que a peça 26 da `main` é a régua viva do sistema: foi refeita na v0.282 como grade (categoria `Capanga · Ameaça · Desastre · Catástrofe · Calamidade`, de `×1` a `×6` pessoas, duração de 2 a 5 rodadas), tem validador, e o `bloco-de-inimigo.docx` publicado no `JJK---PDF---RPG` sai dela. Hoje a guilda tem duas réguas que não conversam.

| Opção | O que acontece |
|---|---|
| **A1. Entra só como ponto de comparação** *(recomendo)* | Um caso a mais (C12): os candidatos do guia e a grade da peça 26 enfrentam o mesmo grupo. Nada é importado. Se as duas discordarem, você fica sabendo quanto e onde. |
| A2. Fica de fora | O plano mede só o material do guia. A divergência continua existindo, sem número. |
| A3. Vira a base | O guia passa a usar a grade. Isso contraria a decisão registrada e precisa de revisão do capítulo 6. |

### D-B. Qual revisão do livro de regras?

O guia está preso à R53, de propósito. O livro está na R60. Pelo CHANGELOG, o que mexeu em regra no meio foi a R58 (Fundamento e Catálogo) e a R60 (Reação fora do turno não gasta o limite de feitiço). A R57 e a R59 dizem que não mudaram regra.

| Opção | O que acontece |
|---|---|
| **B1. Conferir a diferença da R53 para a R60 primeiro e medir na R60** *(recomendo)* | Um passo curto antes das contas. O resultado vale para o livro que a guilda usa hoje. |
| B2. Medir na R53 | Mais rápido. Os resultados podem ficar velhos se a R58 ou a R60 mexerem em algo que o encontro usa. |

### D-C. Inimigo gasta PE ou não?

A peça 26 §6.1 diz que o inimigo não conta PE: a frequência vem de rótulo e a cota de dano é o orçamento. O guia dá reserva de PE ao Amontoado (6), a Toru (8) e a Sayo (12). O registro do piloto já anotava essa tensão sem escolher.

| Opção | O que acontece |
|---|---|
| **C1. Medir os dois modelos no mesmo encontro** *(recomendo)* | O caso C07 compara Toru e Sayo com PE e com rótulo de frequência. A escolha continua sua, mas com o efeito na mão. |
| C2. Manter os dois, cada um no seu livro | Nada é medido. O mestre que lê os dois livros recebe duas instruções. |

---

## 4. Os casos de comparação

Treze casos, fechados. Cada um muda uma coisa só e mantém o resto igual ao caso de origem, como o capítulo 6.8 pede.

| # | O que varia | O que fica fixo | Origem | Tipo de evidência |
|---|---|---|---|---|
| C01 | Nada: reproduzir os números já publicados | tudo | casos 74 e 57 | conta exata e simulação |
| C02 | Tamanho do grupo: 2, 3, 4 e 6 personagens | Amontoado e Toru/Sayo, nível 2 | 57, 76 | simulação |
| C03 | Composição: trocar um perfil por Vanguarda e depois por Incursor | 3 personagens, nível 2 | 74 | simulação |
| C04 | Estado de entrada: cheio, metade, metade com 2 Sequelas, segundo encontro sem descanso | Amontoado, nível 2 | 57 | simulação |
| C05 | Um corpo contra dois: 32 PV contra 16 + 16 (nível 2), 200 contra 120/80 (nível 15) | vida total, Defesa, ataque | 74, 102 | simulação |
| C06 | Controle: Carregador agarrando contra Carregador só batendo | Carregador, corredor de entulho | 62, 63 | simulação |
| C07 | Recurso do inimigo: PE contra rótulo de frequência (só com D-C = C1) | Toru e Sayo | 75, 76 | simulação |
| C08 | Preparo anunciado: Sineiro com e sem tentativa de interromper | Sineiro, ordem Rina → Sineiro → Mei → Akira | 71, 73 | simulação e ensaio |
| C09 | Terreno: mapa original, motor desligado, fechamento ativo | Carregador | 65, 66 | simulação |
| C10 | Objetivo: lutar até o fim contra priorizar a retirada da caixa | Sineiro | 73 | simulação |
| C11 | Socorro: socorrista ao lado, a 2 turnos de distância, ausente | Amontoado, grupo pela metade | 22, 57 | simulação |
| C12 | Régua: candidatos do guia contra a grade da peça 26 (só com D-A = A1) | mesmo grupo, níveis 2 e 6 | 74, peça 26 | conta e simulação |
| C13 | Nível alto com capacidades de Caminho incluídas | Arquivo de Daigo, nível 15 | 100, 101, 102 | simulação |

**O C01 é o portão.** Se o simulador não reproduzir as probabilidades analíticas do caso 74 (por exemplo, 44,2% de o inimigo de 108 PV com Defesa 13 sobreviver a seis feitiços no nível 6), nenhum outro caso roda. Com a simulação do 57 a comparação é por faixa, porque ela usou fichas incompletas.

**O que fica de fora de propósito:** níveis 3 a 5, 7 a 14 e 16 a 30 sem ficha real, Domínio, Expansão e entidades como quarta ficha. Cada um desses precisaria de ficha completa antes de entrar.

---

## 5. O que medir

Dano médio e número de rodadas continuam na tabela, mas não decidem nada sozinhos. O caso 57 já mostrou por quê: duração igual, quedas três vezes maiores.

| Medida | Por que importa |
|---|---|
| Duração (mediana e o caso ruim, 90%) | Ritmo da sessão |
| Chance de pelo menos uma queda | Risco percebido pela mesa |
| Chance de duas quedas no mesmo intervalo de socorro | Onde o socorro deixa de dar conta |
| Socorro dentro do prazo | Se a regra de Morrendo funciona com o mapa e o grupo reais |
| Turnos sem agir, por personagem | Controle e queda tirando gente do jogo |
| PE e usos gastos pelo grupo | Quanto sobra para o próximo encontro |
| Objetivo cumprido, e a que custo | Missão que não termina em morte do inimigo |
| Retirada possível até o fim | Se existe saída de verdade |
| Turnos em que o inimigo usou a capacidade que define ele | Se a função da ficha aparece em jogo |

**O que só mesa ou ensaio mede:** se o grupo reconheceu o sinal, se teve mais de uma opção útil no turno, e quem ficou sem participar e por quê. São as perguntas do fim do capítulo 6.8.

---

## 6. Premissas da simulação

Toda saída traz estas premissas impressas junto do número:

- **Fichas completas**, montadas pela R53 ou pela R60 conforme D-B, com Kokusen e os efeitos de Caminho que o perfil tem no nível.
- **Política de escolha declarada, e mais de uma.** O inimigo roda com três políticas: focar quem está mais ferido, focar quem ameaça o objetivo, espalhar os golpes. O grupo roda com duas: atacar sempre e cumprir o objetivo assim que der. Resultado que muda muito de uma política para outra é marcado como dependente de decisão, e vira pergunta para mesa.
- **Mapa por faixas de distância**, com os custos de movimento dos casos 62, 65 e 66. Linha de visão e cobertura entram quando o caso já as define.
- **Queda e socorro pela regra do livro:** Aguentar, Insistir, Morrendo, prazo de atendimento. O programa não pode encerrar a luta só porque ninguém consciente consegue agir sem marcar quem está Morrendo e quem está Derrotado. Esse foi o limite registrado no 57.
- **Número de execuções** suficiente para a margem de cada porcentagem ficar abaixo de um ponto. A margem sai impressa.

**Os três tipos de evidência ficam separados em toda tabela:** conta exata, simulação com política declarada, ensaio com resultados escolhidos e mesa real. Nenhum resultado de simulação vira "dificuldade validada".

---

## 7. Mesas reais

**Três mesas curtas, uma por ficha de referência:** Amontoado (nível 2), Toru e Sayo (nível 2) e Sineiro (nível 6). O registro segue o capítulo 6.8: duração, recursos gastos, quedas, tempo sem agir, socorro, retirada, objetivo, e se o sinal foi entendido.

Nenhum jogador foi chamado. O assistente prepara a folha de registro e organiza o retorno, mas não inventa resultado.

A comparação entre mesa e simulação é o que fecha cada caso: onde a mesa ficar fora da faixa simulada, a premissa é revista, e não a ficha.

---

## 8. Limites atuais

- **Não existe escala geral validada** em nenhum nível. Os valores de 2 e 6 são candidatos.
- **Os perfis de 10 a 30 só têm ataque básico e feitiço.** Os níveis 26 e 30 empatam por limite da comparação.
- **Só um grupo, de três, foi medido**, sempre com os mesmos três Caminhos.
- **Só uma simulação teve o inimigo agindo**, com fichas incompletas.
- **Nenhuma mesa usou as fichas do guia.**
- **O guia está na R53**, e o livro na R60.
- **O sistema tem uma segunda régua de inimigo** (peça 26 e o bloco de inimigo publicado) que o guia não compara.
- **PE de inimigo tem dois modelos** nos dois livros.

---

## 9. Ordem e o que depende de você

1. Suas respostas para D-A, D-B e D-C.
2. Se D-B = B1: a conferência da R53 para a R60, só leitura, numa folha própria.
3. O simulador, com o C01 como portão. Fica numa pasta de apoio nova (`apoio-encontros-149/`), sem tocar nas fontes do guia.
4. C02 a C13, um resultado por caso, com as premissas na mesma tabela.
5. Folha de registro para as três mesas.
6. Nenhum número do guia muda nesta frente. Se algum caso mostrar que um valor precisa mudar, ele vem pra você com a comparação antes.

**Precisa do seu ok:** as três decisões, transformar este rascunho no registro 149 (mexe no 98, no manifesto e na fila) e qualquer alteração de número.
