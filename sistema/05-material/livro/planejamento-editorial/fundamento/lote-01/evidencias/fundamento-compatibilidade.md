# Auditoria de compatibilidade — Fundamento

Data: 2026-10-03. Auditoria documental e numérica do assistente, sem teste com leitores ou jogadores. Nenhuma fonte publicada foi alterada. A candidata principal é responsabilidade do agente coordenador.

## Fontes e método

Raiz dos caminhos relativos: `/media/mizuki/HD Externo II/Claude/Claude 2`.

- `sistema/05-material/livro/manual/40-fundamento.md` (adiante **F**): fonte jogável publicada para o Fundamento.
- `manual/matematica/pac7.py` (adiante **P**): modelo que calcula as montagens prontas. Importante para distinguir intenção operacional de frases do manual.
- `manual/matematica/v7.py` (adiante **V**): economia e busca por perfis. Não é um verificador de pares nominais.
- `manual/matematica/validador-feiticos.py` (adiante **A**): versão anterior; usa três melhorias em todas as Classes e d6 em áreas. Não certifica a versão atual.
- `invocacoes/05-Edicao-Integrada/60-invocacoes.md` (adiante **I**): fonte vigente das entidades; a peça histórica `03-mecanica/15-invocacoes.md` remete a ela expressamente.
- `sistema/05-material/livro/manual/42-tecnica-marcial.md` (adiante **M**): equivalência de Kata, Ruptura e Ōgi.
- `sistema/05-material/livro/planejamento-editorial/regras-basicas/lote-03-r3/DANO-E-CONDICOES.md`: candidata atual de condições, usada como interface e não como publicação substituta.
- Skills lidas: pesquisa-antes-de-propor, redacao-acessivel-rpg e balanceamento-simulacao.

`pac7.py` e `v7.py` foram executados sem modificar seus arquivos. Saídas em `/tmp/fundamento-pac7-auditoria.txt` e `/tmp/fundamento-v7-auditoria.txt`. O primeiro imprime “TUDO OK”, mas os limites de cobertura abaixo impedem tomar isso por certificação de compatibilidade.

Classificação usada: **E** = correção editorial amparada por regra ou cálculo já claro; **I** = esclarecimento por inferência conservadora, que deve ser registrado; **M** = decisão mecânica para resolver fontes contraditórias ou lacuna. “Sem aplicação” significa que a peça não pode ser comprada nessa montagem como gasto artificial; não é uma proibição geral de imaginar aquele poder.

## Achados prioritários

### 1. A fórmula omite a Forma, e o texto de reembolso diverge dos exemplos

F:435–436 escreve `Pontos − Melhorias + Devolução` e limita a devolução ao preço das Melhorias. F:430 diz que Formas custam pontos. F:537–541 calcula Palma Trovejante com o preço do Cone e reembolsa Cone + Derrubado. F:1300 diz expressamente que Atrasar reembolsa a Linha de Rachadura, que não tem Melhoria. P:43–58 soma Forma e Melhorias e limita a devolução à soma.

**Recomendação E/M:** registrar `gasto = custo da Forma + custo das Melhorias`, depois `devolução aproveitada = menor entre devolução válida, 2 × Classe e gasto`. Dados de uma montagem comum de dano = `3 × Classe − gasto + devolução aproveitada`. Essa regra conserva os cálculos publicados; a correção da frase normativa é uma escolha entre fontes em conflito, não apenas ortografia. Uma soma negativa significa orçamento insuficiente, não um feitiço de controle gratuito.

**Não dar desconto de Família Livre à Forma.** F:234 concede o desconto às Melhorias; P:53 cobra Forma no preço normal e P:56 só usa desconto nas Melhorias. Famílias Fechadas continuam bloqueando Formas de sua Família (F:242).

### 2. Toque e Onda estão na linha errada da tabela de alcance

F:503 junta `Projétil e Toque` em 9/18/36 m, mas F:482 e 511 fixam Toque em 1,5 m. F:509 junta `Cura e Onda` em 9/18 m, mas F:489 define Onda autocentrada com raio 3 m. A cópia I:200 já separa Toque corretamente.

**Correção E:** uma linha por comportamento. Distinguir distância até o alvo/ponto de origem, posição fixa da origem e tamanho da área. Para Toque, o limite de 1,5 m permanece em qualquer Classe; sua Restrição embutida ocupa uma das duas vagas, mesmo quando não produz devolução aproveitável (P:54 e nota final P:261).

### 3. Longe não tem pré-requisito escrito

F:604–605 permite subir alcance sem dizer em quais Formas. O usuário autorizou explicitamente impedir o reembolso de contato junto do alcance aumentado.

**Correção M dirigida pelo usuário:** Toque não compra Longe nem Muito Longe. Para atingir de longe, monte Projétil e retire Corpo a Corpo. Não cobrar Corpo a Corpo de um poder que deixou de exigir contato.

**Cuidado com Cone e Linha:** F:995 e P:186–193 usam Muito Longe para aumentar o comprimento de Linha de 18 para 60 m. Proibir Longe em todas as Formas que saem do usuário quebraria esse exemplo. Há duas saídas coerentes: preservar a exceção de comprimento de Cone/Linha; ou reservar tamanho para Maior e migrar exemplos/custos. Para R06, recomendo preservar a exceção escrita e reservar a redundância de preço `Muito Longe Média` versus `Muito Maior Pesada` para R07. Não mover a origem do Cone/Linha para longe.

### 4. Atrasar é reembolso gratuito em Liberação Máxima

F:947 exige rodada inteira da Liberação. F:824 faz Atrasar pagar por essa mesma rodada inteira. F:954 admite Restrições sem excluir exigências já obrigatórias. Os exemplos Rachadura e Sentença Final compram Atrasar (F:1308–1309; P:140–145).

**Correção M:** exigência já imposta pela Forma, Selo, rota ou modalidade não devolve pontos novamente. Na Liberação, Atrasar e Parado não devolvem; Rápido e Reação não substituem a ação completa. A decisão conserva a exigência de Liberação e remove um benefício duplicado que o validador histórico aceitava. Os exemplos antigos são fonte histórica; os novos devem ser recalculados.

Sem outra Restrição efetiva, Rachadura de Classe 3 passa de 12d8 para 10d8 (`9 − 2 + 3`); Sentença Final Classe 5 passa de 17d8 para 12d8 (`15 − 3 − 5 + 5`). Ambas conservam PE e ação completa. Outra Restrição real poderia recuperar pontos, dentro dos limites.

### 5. O teto agregado escrito não existe no modelo que calcula áreas

F:107 e 1186 dizem que alvos e repetições somados não passam de 4C. P:b(), linhas 50–98, não recebe quantidade de alvos de área: compara apenas `dados + extra` com 4C. Os exemplos Fim de Turno e Vala Comum (F:1289–1291) entregam 12d8 e 11d8 por alvo na Classe 5. Dois alvos produzem 24d8 e 22d8, acima de 20. `Rede` é controle de 0d8: não é contraexemplo de dano.

O texto de Máxima é ainda mais explícito: 24d8 em tudo na Linha (F:995), mas não se deve usar Máxima para provar o problema dos feitiços normais, pois ela já é uma exceção de dados fixos.

**Recomendação adotável M:** preservar a aplicação integral de áreas por alvo. Trocar a promessa de teto agregado pela distinção entre dados comprados na montagem, divisão de dados e dados adicionais. Na candidata discutida com o coordenador: dados-base até 3C, ou 4C com Liberação; Rajada/Mais Um dividem a quantidade; pacotes adicionais de Queima/Salto/Estilhaço entram na avaliação de 4C sem multiplicar a base pelo número de alvos de uma área. Fica recebe exceção explícita de persistência. Isso é alteração do escopo normativo, apoiada na execução publicada, e requer avaliação comparativa de área em R07.

**Não afirmar** que todas as combinações de multiplicadores já estão balanceadas. Remate, Acúmulo, ataques externos que aproveitam marcas, número de alvos e duração são eixos diferentes; V:128–134 já reconhece parte dessa insuficiência.

### 6. Cura tem teto escrito, mas o reembolso genérico o ultrapassa

F:547 chama a tabela de Cura de teto por Classe. F:558–562 fixa Cura = 2C dados e Onda = 3C − Pesada. O cálculo genérico de P:56–58 permite reembolsar a Forma e chegar a 3C. Exemplo C5: Cura sem melhoria, Sangra (+5), dá `15 − 5 + 5 = 15d8`, embora o quadro diga 10d8. Onda C5, Gesto (+3) + Sangra (+5), dá 15d8 em cada aliado, embora o quadro diga 7d8.

**Recomendação M conservadora:** calcular normalmente e limitar o resultado final de Cura a 2C; Onda de cura a 3C − Pesada. Isso mantém todos os números da tabela e permite usar Restrições para financiar funções adicionais de Amparo. Na Onda de apoio, aplicar a mesma reserva máxima da Onda, convertida a 3 PV temporários por ponto, caso a candidata confirme essa interpretação. O excesso não se transforma em dano, energia nem pontos para outra ficha.

É mais claro que criar silenciosamente uma segunda regra de reembolso só para Amparo. Porém a interação com Liberação, Máxima e bônus de cura deve continuar seguindo exceções expressas, e a tabela histórica da Máxima não é coberta por esse teto de Classe.

### 7. Forma Efeito e Uso Livre permitem atalhos involuntários

F:886–906 exige Uso Livre sem mudar rolagens, mas oferece abafar passos e estabilizar a mão; alguns jogadores inferirão bônus de Furtividade/Pontaria. F:914–929 chama Efeito de automático fora de combate e inclui multidões/prédio dormindo/bairro de onde ninguém sai. Estar fora da iniciativa não remove a resistência de quem sofre um efeito hostil.

**Correção E/M:** exemplos de Uso Livre são pequenas manifestações ficcionais sem conceder bônus, invisibilidade, ocultação automática ou sucesso de perícia. Quando a intervenção muda uma disputa, use a regra aplicável ou construa uma aplicação paga. Forma Efeito pode resolver tarefas sem oposição, mas não aplica automaticamente condições, controle mental, confinamento, dano, alteração de memória ou informação disputada a criaturas resistentes. O feitiço precisa ter resistência/saída apropriada antes de entrar em jogo, independentemente de haver iniciativa. Uma abertura de combate não transforma um efeito de controle anteriormente automático em outra regra.

### 8. Disponibilidade não significa combinação funcional

F:810 permite Efeito Próprio fora de Família, mas o define como mecânica ausente do catálogo. Copiar Fura/Maior/Atordoado com nome novo para driblar Família Fechada contradiz esse requisito. Exige uma regra clara de montagem: toda peça deve alterar um campo aplicável, preservar seus próprios requisitos e não anular a desvantagem que está pagando por ela.

## Matriz de compatibilidade sugerida

Estas decisões devem ficar perto do procedimento e das entradas, não apenas num apêndice distante. “Permitido com limite” é importante: não rejeitar combinações só por serem criativas.

| ID | Combinação | Resultado recomendado | Motivo / fonte | Tipo |
|---|---|---|---|---|
| F01 | Toque + Longe/Muito Longe | Não combinar; trocar por Projétil, sem devolução de Corpo a Corpo | Contato fixo F:482,511; correção solicitada pelo usuário | M |
| F02 | Toque/Aura + Corpo a Corpo outra vez | Não contar duas vezes | Restrição já embutida, P:54; limite total de duas | E |
| F03 | Aura/Onda + Longe/Muito Longe | Sem aplicação para deslocar a origem; usar Maior para raio | Origem centrada no usuário, F:484,489 | I |
| F04 | Cone/Linha + Corpo a Corpo | Não combinar | Proibição explícita F:823 | E |
| F05 | Onda + Corpo a Corpo | Não devolve | Onda já é autocentrada e a conversão de F:823 só cita Projétil/Explosão | I |
| F06 | Explosão + Longe | Permitido: muda distância até o centro, não raio | Separação das escadas F:481–525 | I |
| F07 | Explosão/Aura/Onda + Maior | Permitido: sobe raio; não muda distância da origem | Escada Esfera F:523 e Maior F:621 | E/I |
| F08 | Cone/Linha + Longe/Muito Longe | Permitido para comprimento, sem mover origem; documentar exceção | Exemplo F:995; P:186–193 | E |
| F09 | Linha + Maior no comprimento máximo | Sobe largura 1,5→3→4,5 m; não reinicia comprimento | F:486 | E |
| F10 | Maior/Muito Maior + Projétil/Toque/Cura/Apoio sem área | Sem aplicação; uma área precisa de Forma adequada | Entrada pede tamanho de área F:621–622 | I |
| F11 | Mais Um + Toque | Permitido se todos os alvos forem alcançáveis a 1,5 m; divide dados | F:482,625; preservar exigência de contato | I |
| F12 | Salto + Toque | Não usar Salto para acertar o segundo alvo além de 1,5 m enquanto retém devolução de contato | Limite por alvo de Toque e não anular Restrição | I/M |
| F13 | Sem Ver + Toque | Permitido para alvo cuja posição conhece dentro de 1,5 m, sem parede; não aumenta alcance | F:606 e 482 | I |
| F14 | Sem Ver + cobertura total | Não atravessa obstáculo sólido por si | Saber posição não cria passagem; F:644 mantém total sem alvo | I |
| F15 | Contorno + cobertura total | Pode contornar por trajeto aberto dentro da geometria; não atravessa sólido | F:628 permite curva; exige distinção entre contornar e perfurar | I |
| F16 | Sem Cobertura + cobertura total | Não ignora | F:644 explícito | E |
| F17 | Inescapável + outra Melhoria ou Restrição, inclusive Corpo a Corpo de Toque/Aura | Não combinar | F:641; Restrição embutida é Restrição | E |
| F18 | Inescapável + Liberação Máxima | Não combinar | F:641 explícito | E |
| F19 | Inescapável + Forma paga/área | Lacuna: resolver expressamente em R07; candidato conservador só Projétil | “Mais nenhuma peça” não enumera Formas; só exemplo Projétil em F:1288 | M se restringir |
| F20 | Precisão + efeito inteiramente automático aliado | Sem aplicação, salvo existir outro teste comprado na mesma montagem | Bônus só existe em acerto/CD F:639 | I |
| F21 | Tudo ou Nada + efeito sem TR, ou TR que já elimina todo dano | Não devolve | F:830 troca metade por zero; não pode devolver sem piorar | E/I |
| F22 | De Novo + efeito que usa apenas TR | Sem aplicação | F:645 exige você errar a rolagem; não obriga inimigo a repetir TR | I |
| F23 | Rajada + troca para TR | Não conceder vários TRs/copiar dano automaticamente; Rajada opera com ataques individuais | F:626 exige cada tiro com rolagem de acerto; adaptação nova precisa projeto próprio | I |
| F24 | Salto + Salto / Estilhaço + Estilhaço / Queima gerando outra Queima | Não propagam recursivamente | F:627,730,733 só definem aplicação derivada, não nova conjuração | I |
| F25 | Condição Pesada + outra Condição Pesada | Não combinar | Uma por feitiço, F:657 | E |
| F26 | Condição + Amparo automático em aliado disposto | Permitido somente para benefício previsto; não cria imposição automática em hostil | F:488–489,788; alvo precisa ser elegível e aceitar o benefício | I |
| F27 | Junto + dano | Sem aplicação; usar Mais Um | Junto só cura/apoio, F:799 | E |
| F28 | Junto + Onda | Sem benefício adicional automático: Onda já pega todos os aliados; não gera segunda onda | F:489,799 | I |
| F29 | Reserva + cura imediata integral | Escolhe cura guardada, não duplica cura agora e depois | F:800 | I |
| F30 | Rápido + Reação | Não combinar | F:747–748 explícito | E |
| F31 | Rápido + Atrasar | Não combinar | F:747 explícito | E |
| F32 | Reação + Atrasar/Parado/Armado | Não combinar | F:748 explícito | E |
| F33 | Armado + Carregar | Não combinar | F:749 explícito | E |
| F34 | Armado + Rápido | Permitido: a preparação usa Bônus; o gatilho não cria uma segunda ação imediata | Nenhuma proibição; F:747,749. Mantém limites do turno que arma e da peça | I |
| F35 | Atrasar/Parado + Passo | Não recebe o movimento de Passo; não comprar como gasto funcional | Restrição proíbe mover no turno, Passo move antes/depois no mesmo turno | I |
| F36 | Silencioso + Gesto | Não combinar mantendo devolução: a melhoria remove o requisito da Restrição | F:750 vs826 | I |
| F37 | Silencioso + Barulho | Permitido; oculta gesto/palavra, mas o Barulho continua revelando origem | Barulho é efeito sonoro explícito F:835. Escrever precedência | I |
| F38 | Concentrada + Duradoura | Escolher uma para o mesmo efeito; não somar tempos | F:753–754 define alternativas | I |
| F39 | Concentrada/Duradoura + dano instantâneo | Sem aplicação; não repete dano | F:753 explícito | E |
| F40 | Concentrada/Duradoura + Fica/Anteparo | Não estende essas durações | F:753 exclui ambos, F:754 mesma coisa | E |
| F41 | Frágil + efeito instantâneo | Não devolve | F:834 exige algo durando | E |
| F42 | Atrasar + Parado | Só Atrasar pode devolver; Parado já incluído | F:824–825 e regra contra mesma cobrança F:872 | E/I |
| F43 | Duas de Uma Vez/Condicional/Aquecer/Dívida (ou Própria equivalente) | No máximo uma | F:870 explícito | E |
| F44 | Restrição equivalente ao Selo/rota exigida | Não devolve | F:250,874; estender à rota é inferência de custo já obrigatório | E/I |
| F45 | Remate + Aquecer/Condicional de vida ou duração | Não combinar | F:732 explícito | E |
| F46 | Sem Volta + cura/apoio inteiramente automático | Não devolve se a falha de acertar ninguém for impossível | F:839 exige risco de errar todos; alvo fora do alcance escolhido voluntariamente não legitima desconto | I |
| F47 | Liberação + Atrasar/Parado | Não devolvem | Rodada inteira já obrigatória F:947; corrige exemplos históricos | M |
| F48 | Liberação + Rápido/Reação | Não mudam ação completa; não comprar nesse perfil | Exigência fixa F:947 | I/M |
| F49 | Liberação + Toca a Alma | Não combinar | F:646 explícito | E |
| F50 | Liberação + Cura/Onda de cura | Não combinar | F:547,952 explícito | E |
| F51 | Liberação + Sem Volta, quando escolher Vazio | Não pagar duas vezes pela mesma proibição; rever a Restrição na montagem ou usar um preço realmente distinto | F:948 e839; preço da Liberação é escolhido no uso | I/M |
| F52 | Recuo + Limpa sobre o próprio conjurador | Não manter reembolso se o próprio feitiço limpa a condição que acabaria de causar | F:828,795; não anular a desvantagem comprada | I |
| F53 | Efeito Próprio repetindo função fechada ou aumento de dano conhecido | Não pode servir de nome alternativo para peça bloqueada | Só mecânica inexistente, F:810 | I |
| F54 | Efeito/uso fora de iniciativa + condição ou informação hostil | Não se torna automático só porque ainda não há iniciativa | Compatibilizar F:889,914 com procedimentos e resistência | M |

### Pares que não devem ser proibidos por associação superficial

- **Toque + Passo:** é uma aproximação ou saída de 6 m paga, continua exigindo o contato na resolução; não equivale a aumentar alcance. Fica incompatível se comprar Parado/Atrasar na mesma montagem.
- **Recuo Cego + Sem Ver:** Sem Ver não remove automaticamente a condição Cego nem suas desvantagens no restante do turno. Deve avaliar a dor que realmente sobra, não banir a dupla por nome.
- **Empurrão + Parede/Anteparo:** não inventar dano de colisão além das regras comuns. Mover alvo e criar obstáculo são funções compatíveis, mas a sequência precisa estar escrita; uma parede não pode nascer ocupando o corpo do alvo sem regra.
- **Atordoado + Prende:** condições distintas podem coexistir; o limite é uma Condição Pesada, não uma única peça de Controle.
- **Rápido + Parado:** o manual não proíbe. Usar Bônus sem movimento pode ser uma troca real. Não confundir com Reação + Parado, que está proibido expressamente.
- **Concentrada + dano e condição:** pode estender a condição; não o dano. O fato de haver dano não bloqueia a melhoria inteira.
- **Aura + Maior:** ampliar raio preserva o centro no usuário e a desvantagem; não remove Corpo a Corpo.

## Resolução mínima a escrever no núcleo

A ficha de uma aplicação deve definir separadamente: ação; alcance/origem; alvos/área; acerto ou TR; resultado de falha/sucesso; dano/cura; efeitos adicionais; duração; concentração; término/saída; custo e peças.

Trocar ataque por TR de graça não permite escolher a defesa mais fraca a cada uso. O exemplo F:68 diz que o personagem montou duas versões; são aplicações conhecidas separadas, salvo permissão específica. A forma de resolver e o atributo do TR ficam escritos antes da sessão.

**Lacuna a fechar em R07:** F:492 permite trocar ataque e TR livremente; F:640 cobra Certeiro por TR com metade. Para evitar que a troca gratuita duplique Certeiro, o esclarecimento conservador é: ataque erra = zero; TR de aplicação direta convertida = zero no sucesso; áreas mantêm metade indicada pela Forma; Certeiro muda a aplicação direta para TR com metade. Isso altera uma leitura possível e precisa estar registrado. Se a intenção for toda conversão para TR já dar metade, Certeiro está redundante e deve ser substituída, não mantida como preço fictício.

Ao resolver um pacote com dano e Controle, acerto aplica o efeito indicado e dano; TR bem-sucedido evita o Controle, com dano residual apenas quando a Forma/peça disser. Condição Pesada tem novo TR ao fim do turno para encerrar, mesmo se aplicada originalmente por acerto. Isso casa com a candidata de Condições:144–158 e evita “metade de uma condição”. Efeitos que criam estrutura, como Anteparo, não se multiplicam por cada alvo de uma área sem compra específica.

## Fica: execução simples e risco restante

Texto mínimo proposto, como decisão mecânica identificada:

> A área permanece por 1 minuto enquanto você mantém concentração. A aplicação inicial do feitiço conta como sua aplicação de dano naquela rodada para cada criatura atingida. Nas rodadas seguintes, uma criatura sofre metade dos dados quando entra na área ou começa o turno nela, o que ocorrer primeiro, no máximo uma vez por rodada. Use o TR do feitiço; passar reduz esse dano como indicado por sua Forma. Mover a área sobre a criatura não conta como ela entrar. Entrar e sair repetidamente não produz aplicações adicionais na mesma rodada.

A redação “nas rodadas seguintes” não deve impedir uma criatura nova de entrar e sofrer metade ainda na rodada da conjuração: a trava é por criatura. Melhor versão operacional: depois da resolução inicial, o primeiro gatilho elegível naquela rodada afeta apenas quem ainda não recebeu dano dessa conjuração na rodada. Concentrada/Duradoura não estendem Fica (F:753). Definir se Aura com Fica acompanha o conjurador é tarefa de R07; não pressupor mobilidade só pelo nome.

Por que isso não é teto vitalício: são até seis rodadas de persistência pela rodada de dez segundos do projeto. Um alvo que sofra dano inicial e nove pulsos na candidata pode receber muito mais de 4C. Mudar dez segundos para seis aumenta o dano potencial de persistência por minuto; não é só uma conversão de unidade. A alteração evita exploração de entradas sucessivas, mas não resolve equilíbrio entre feitiço instantâneo e persistente. Essa limitação deve constar do relatório da candidata.

## Interface com Invocações e outras criações

I:45 já diz: um espaço conhecido compra uma entidade no nível do personagem, que progride junto; a troca pode ser refeita ao subir de nível. F:421 só cita Passivas e Expansão, omissão de integração. M:11,17 define a equivalência do espaço de Kata. A autorização do usuário estende o apontamento às formas de criação, inclusive manejo/estilo marcial.

O núcleo deve apontar a troca uma vez e remeter ao procedimento dono para ficha/comando. Espaço de lista é custo de **conhecer/possuir**, não uma carga gasta ao invocar. Não cria ação ou turno adicional e não dispensa requisito narrativo/rota elegível. A regra de disponibilidade precisa distinguir corpo criado, entidade de técnica e outras aquisições; espaço não converte tudo em shikigami inato. O nome da entidade na rota marcial precisa de sua própria justificativa (constructo, parceiro etc.) e dos limites atuais da rota.

Sincronização obrigatória depois da aprovação: o catálogo comum está duplicado em I:176–452 e herdado por M:11. Não alterar só Fundamento e deixar duas redações de Longe, Fica, Corpo a Corpo ou orçamento convivendo. Na candidata, registrar a migração; não substituir de surpresa a publicação vigente.

## Bateria numérica e leitura dos resultados

Código: `/tmp/fundamento-auditoria-numerica.py`.
Resultados: `/tmp/fundamento-riscos-numericos.json`.

As sete linhas de preços vêm das colunas da tabela de F:96–103. São 56 casos de área, 56 de persistência, 56 de cura e cinco de Liberação. Cinco invariantes mecânicos simples passaram. A análise mede somas e máximos, não taxa de sucesso, letalidade completa, decisão tática ou diversão.

### Áreas com reembolso da Forma

Uma Explosão que recuperou o preço da Forma pode ter 3C dados por alvo. Todos abaixo falham no TR; são médias matemáticas sem RD, crítico ou bônus. PE continua 3C.

| Classe | Por alvo | 1 alvo | 2 alvos | 4 alvos | 6 alvos |
|---|---|---|---|---|---|
| 1 | 3d8 | 13,5 | 27 | 54 | 81 |
| 3 | 9d8 | 40,5 | 81 | 162 | 243 |
| 5 | 15d8 | 67,5 | 135 | 270 | 405 |
| 7 | 21d8 | 94,5 | 189 | 378 | 567 |

Isso não demonstra desbalanceamento sozinho: depende de agrupamento, fogo amigo, ação completa/restrição escolhida, saves e quantidade de inimigos. Demonstra que não se pode prometer um teto agregado de 4C e que o número de alvos precisa aparecer nos próximos testes.

### Fica cheio, um alvo exposto

Explosão + Fica pode recuperar ambos os preços com duas Restrições independentes que devolvam Média e Leve. Mantém uma Melhoria, uma Forma e duas Restrições. O alvo fica dentro e falha em todos os TRs. Média calculada sem arredondar o resultado do dado.

| Classe | 1 rodada | 3 rodadas | 6 rodadas | 10 rodadas (candidata de 6 s) |
|---|---|---|---|---|
| 1 | 3d8 = 13,5 | 5d8 = 22,5 | 8d8 = 36 | 12d8 = 54 |
| 3 | 9d8 = 40,5 | 17d8 = 76,5 | 29d8 = 130,5 | 45d8 = 202,5 |
| 5 | 15d8 = 67,5 | 29d8 = 130,5 | 50d8 = 225 | 78d8 = 351 |
| 7 | 21d8 = 94,5 | 41d8 = 184,5 | 71d8 = 319,5 | 111d8 = 499,5 |

Dez rodadas cabem em um minuto na candidata de Testes e Turnos (6 s por rodada). Se forem usados os dez segundos da publicação histórica, o limite correspondente é seis rodadas. O JSON contém ambos os rótulos. Para Classe 5, manter 15d8 iniciais e nove pulsos de 7d8 entrega 78d8 potenciais por alvo (351 de média); com seis rodadas eram 50d8 (225). A mudança de duração da rodada aumenta esse extremo em 56%. Concentração, permanência do alvo, saves e resistências reduzem o resultado real, mas não apagam a necessidade de calibrar esse eixo.

### Tetos de cura preservados

| Classe | Cura máxima proposta | Onda máxima proposta por aliado | Máximo que reembolso irrestrito produziria |
|---|---|---|---|
| 1 | 2d8 | 1d8 | 3d8 |
| 2 | 4d8 | 3d8 | 6d8 |
| 3 | 6d8 | 4d8 | 9d8 |
| 4 | 8d8 | 6d8 | 12d8 |
| 5 | 10d8 | 7d8 | 15d8 |
| 6 | 12d8 | 9d8 | 18d8 |
| 7 | 14d8 | 10d8 | 21d8 |

O teto específico evita que Restrições tornem Onda tão forte por aliado quanto dano cheio. Ainda falta testar cura ao longo do dia, acesso à Energia Reversa, tamanho de grupo e a futura revisão de Morrendo/Integridade. Não inventar um teto diário nesta rodada.

## O que resolver em R06 e o que pertence a R07

### R06, agora

1. Fluxo por intenção: decidir resultado, alvo e momento, depois escolher Classe e peças. Uma ficha final por exemplo, com pelo menos um exemplo de proteção/movimento/controle.
2. Fórmula com Forma, devolução real e gasto de energia separados de espaço conhecido.
3. Tabela de alcance separando origem, distância e tamanho; Toque explícito.
4. Restrição embutida conta; proibição de cancelar a própria Restrição; custos já obrigatórios não reembolsam.
5. Resolução fixada na montagem e efeitos no sucesso/fracasso do TR explícitos.
6. Dados-base versus dados derivados e área, sem garantia falsa de teto agregado.
7. Uso Livre e Efeito não dão vantagens ou afetam resistentes automaticamente.
8. Remissão de espaço por entidade para todas as rotas autorizadas.
9. Registro da necessidade de migrar catálogos de Invocações e Técnica Marcial quando a candidata for integrada.

### R07, catálogo e calibração

1. Entrada por entrada: o que pode receber cada peça, duração exata, dados aplicados por alvo e condições de saída.
2. Duplicação de Longe/Maior em comprimento e dominância dos preços Médio/Pesado.
3. Certeiro versus troca gratuita de resolução; Inescapável com Formas e Máxima.
4. Pacotes Queima/Salto/Estilhaço, multiplicadores de Remate, Acúmulo e Alvo de Caça; uma prova que não descarte antes as combinações que tentam ultrapassar o teto.
5. Fica: ataque/entrada/início, concentração, mobilidade da Aura, ação de empurrar para dentro, aliados e danos independentes.
6. Forma Efeito: escala sem “cidade inteira” virar imunidade a resistência. A tabela existente confunde quantidade, distância, duração e potência da imposição; não basta aumentar os números.
7. Cura/Onda/Apoio, Energia Reversa e geração de vida temporária; futura interface com Morrendo e Integridade.
8. Precedência de duração (efeito com uma condição breve e uma estrutura de um minuto); evitar fazer a parede desaparecer porque um bônus ofensivo do mesmo feitiço terminou.
9. Recuo, Sangra, Fraqueza e restrições que podem ser neutralizadas por imunidade, cura própria ou preço já pago; cada caso com custo real.

## Limitações dos validadores históricos

- **P lê suas próprias constantes, não o Markdown publicado.** Uma mudança no livro não provoca necessariamente falha.
- **P não multiplica por alvos de área**, não modela entradas em Fica e não verifica os pares acima.
- **P:161 e 195 contêm asserts tautológicos sobre Fura** (`3*2==6`, `3*5==15`) com rótulos que divergem do próprio manual, que usa 2C. São exemplos claros de verificador passar sem conferir a regra.
- **V:100 descarta resultados acima do teto antes de anunciar que ninguém o ultrapassa.** Isso certifica o filtro, não demonstra que a montagem produz um teto por si.
- **A é histórico:** máximo fixo de três melhorias, áreas d6, nomes antigos e ausência de custo de Forma no validador avulso. Não deve ser usado como teste final desta candidata.
- **P ainda imprime “Classe 0 não se monta”**, enquanto F:156 admite uma melhoria e uma restrição Leve. Mais uma divergência de versão, não prova de erro da Classe 0 atual.

## Invariantes para novos testes

1. Preços lidos da tabela dona, por linha e coluna; arredondamento para cima nos preços; desconto Livre só nas Melhorias e mínimo de 1.
2. Reembolso só existe se a desvantagem ainda valer; nunca supera o gasto aplicável nem 2C; embedded counted once.
3. Orçamento não negativo; Forma cobrada e não contada como Melhoria; Efeito Próprio contado.
4. Toque sempre 1,5 m; Aura/Onda permanecem autocentradas; aumentar área não aumenta distância de origem.
5. Ataque, TR e automático são caminhos distintos; nenhuma melhoria se compra se não alterar campo aplicável.
6. Seleção da resolução/TR não muda a cada conjuração de uma mesma ficha.
7. Uma conjuração produz uma aplicação de cada peça, salvo repetição explicitamente comprada; derivados não se propagam recursivamente.
8. Proibição de Rápido+Reação e demais pares explícitos; Liberação conserva ação completa; cura/alma não entram na Liberação.
9. Limites de Cura/Onda verificados depois de desconto e reembolso; não só no exemplo sem Restrição.
10. Simular áreas com 1, 2, 4, 6 alvos; duração até o limite válido; entrar/sair três vezes não triplica Fica.
11. Invocações e rotas marciais usam o mesmo contrato comum, preservando pontos/ações específicos próprios; não duplicar o dano básico ou o comando da entidade.
12. Uma mutação proposital (Toque com Longe; terceira Restrição embutida; cura 3C; Fica 11 rodadas numa duração única de 1 minuto) deve falhar por motivo próprio, mesmo se a soma de pontos ainda couber.

## Referências externas lidas

Estas fontes dão métodos, não preços para o Projeto M. Não foi feito levantamento de popularidade; não são opiniões de leitores.

| Sistema/fonte primária | O que ensina | Aplicação e limite |
|---|---|---|
| [D&D 2024, Spells](https://www.dndbeyond.com/sources/dnd/br-2024/spells), seções Range, Targets e Saving Throws | Separa distância, toque e usuário; ficha informa alvo e efeito de TR; exige caminho até o alvo | Boa estrutura para separar campos e prever resultado do teste. Não importar slots, unidades em pés ou limites de ações |
| [Pathfinder Player Core, Reach Spell](https://2e.aonprd.com/Feats.aspx?ID=4577), p.101 | Aumentar alcance de Toque é permitido quando uma habilidade expressamente transforma esse alcance | Contraexemplo importante: Toque + alcance não é logicamente impossível em todos os RPGs. No Projeto M, a rejeição decorre do reembolso de Corpo a Corpo e da decisão do usuário, não de uma lei do gênero |
| [Fate Core, Creating an Extra](https://fate-srd.com/fate-core/creating-extra), permissões e custos | Começa pelo que o poder faz; diferencia permissão ficcional de custo e associa efeitos a procedimentos de conflito | Serve para ensinar criatividade antes do catálogo e impedir que descrição sozinha compre benefício mecânico. Não importar a economia aberta de aspectos para o orçamento fechado do Projeto M |

A auditoria não acrescenta fatos sobre Jujutsu Kaisen. Exemplos da obra e alegações de lore devem ser validados pelo agente responsável por pesquisa canônica; aqui a fonte de números é o próprio sistema.


## Adendo — Classe 0

F:146–158 permite Forma, dano tabelado, uma Melhoria Leve e uma Restrição Leve, tirando um dado para pagar. O gerador histórico `manual/gerador/partA.js:169` só diz uma Melhoria por menos um dado, sem mencionar Restrição. I:110 repete a regra nova e explicita que uma básica de 1d6 cai para zero dados ao comprar a Leve. Não há fórmula de reembolso do dado para uma Restrição de Classe 0. Aplicar `3C` e `2C` literalmente dá zero, enquanto a melhoria custa um dado por exceção.

**Recomendação conservadora I/M:** manter o dano pela faixa de nível; uma Leve custa exatamente um dado e nenhum desconto o reduz; a Restrição Leve aceita pode limitar o uso, mas não devolve esse dado sem uma regra nova expressa. Registrar essa interpretação, pois não é unívoca nas fontes. Não transformar todas as escalas de Classe 0 em Classe 1: isso fortaleceria Fura, Anteparo e outros efeitos que hoje multiplicam por Classe.

**Apoio Classe 0:** está intencionalmente na tabela de alcance. O validador `sistema/03-mecanica/conferir-manual.py:1562–1565` afirma que Apoio pertence à coluna Classe 0 e distingue essa permissão da proibição de Cura/Onda. Contudo não existe quantidade definida de pontos convertíveis em vida temporária. Pela fórmula literal, `3 × 0 = 0`; portanto a forma não gera vida temporária por sobra. Não converter os seis dados de dano de nível alto em 18 PV temporários gratuitos. A candidata pode permitir que Apoio carregue a única Leve com efeito próprio (exemplo Impulso) e não conceda reserva de PV temporários. Essa formalização precisa ser explicitada, porque o custo em dado de uma forma sem dano é assimétrico, embora não entregue um pacote amplo.

**Toque e Aura Classe 0:** a Forma continua disponível, apesar de carregar Corpo a Corpo de faixa Média. É necessário dizer que a restrição embutida mantém a exigência de contato/origem própria, sem reembolso de pontos, e não deve impedir a escolha da Forma sob o limite especial de Leve da Classe 0. Contá-la como Restrição Média proibida eliminaria uma Forma que a própria tabela oferece. A candidata precisa escolher se ela ocupa a vaga da Restrição Leve; a saída conservadora é ocupar a vaga, sem conceder desconto.
