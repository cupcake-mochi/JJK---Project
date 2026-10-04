# Reavaliação adversarial — Percepção e Furtividade

02/10/2026. Análise de probabilidades, economia de ações e compatibilidade. Somente leitura; livro, classes e candidata não foram alterados.

**Candidata examinada:** `sistema/05-material/livro/planejamento-editorial/regras-comuns/lote-03/03-PERCEPCAO-E-FURTIVIDADE.md`. A análise principal refere-se à candidata anterior, SHA-256 `6b84a92c296d46bfc8ad5a41621e60a4e74921e35542019ce8ab51a11adb7765`. A revisão posterior já corrigida é comentada no adendo ao fim. **Contas completas:** `/tmp/reavaliacao04-furtividade-matematica.json`; reprodução: `/tmp/reavaliacao04-furtividade-contas.py`.

## Conclusão

**Trocar 8 por 10 não resolve a concessão de manutenção gratuita após atacar.** Nos confrontos com bônus semelhantes, o teste com desvantagem parece restritivo. Contra um observador menos investido, pode sustentar numerosos ataques ocultos sem pagar nova ação; em certos pares é automático, inclusive com desvantagem. A candidata ainda combina essa manutenção comum com a tentativa gratuita do Assassino 11, produzindo uma segunda chance no mesmo turno.

Recomendo **revelação pelo ataque como regra comum, sem teste gratuito de manutenção**, preservando tentativas de Esconder pelas ações e exceções que cada ficha já possui. Para a percepção passiva, **10 + bônus completo de Percepção** é um ponto inicial conservador e inteligível, mas não recebe um certificado de equilíbrio só porque gera 55% entre iguais. O custo de ação, os sentidos disponíveis, o terreno e a possibilidade de voltar a esconder-se são tão importantes quanto esse percentual.

A alternativa de preservar uma “posição incerta, mas não Oculto” cria outro estado e conflita com a definição atual de Oculto. Ela só faz sentido se for uma escolha deliberada de design com benefícios enumerados, e não uma maneira indireta de manter a mesma vantagem gratuita.

## Fontes e hipóteses

- `sistema/03-mecanica/01-atributos-acerto-defesa.md`, §§2, 3 e 5: atributos 0–6; maestria 1–4; CD de TR usa base 8, mas isso não demonstra automaticamente qual deve ser a CD de percepção passiva. O crítico por 20 natural é de **acerto**, não de toda perícia.
- `sistema/03-mecanica/04-pericias-e-testes.md`, §§1, 2.1 e 5: treino, especialização, escada de perícias e cancelamento entre vantagem e desvantagem. A tabela publica 0% em CD 26 com bônus +4 e 100% em tarefas fáceis com bônus suficiente; não há sucesso/falha universal de perícia em 20/1 natural nesta conta.
- `sistema/03-mecanica/11-aptidoes-e-refino.md`, §3: especialização comprada a partir do nível 10 soma metade da maestria outra vez. No teto isso adiciona +2.
- `caminhos/05-Edicao-Integrada/06-Incursor-Caminho-e-Trilhas.md`: Esconder por Bônus no nível 2; Desaparecer no Percurso no 11; Alvo Estudado, Golpe Cirúrgico, Fluidez e Sentença Final.
- `sistema/03-mecanica/14-equipamento.md`, §5.0.5 e §8 item 19: a intenção anterior era arma de fogo revelar e demais armas pedirem teste. Retirar a manutenção gratuita revisa essa intenção; deve ser registrado explicitamente, sem fingir que sempre foi assim. A autorização atual permite avaliar essa correção.
- Candidata, linhas 36–50: fórmula e CD; 56–62: persistência e ações; 69–77: busca; 98–119: vantagem, exposição, manutenção e Silencioso.

Os bônus escolhidos são possíveis: +4 pode ser Destreza 3 e maestria 1; +7, atributo 5 e maestria 2; +10, atributo 6 e maestria 4; +12, esse mesmo especialista. Não são uma progressão obrigatória nem uma estimativa da distribuição de fichas. Percepção +0 é um observador sem investimento; +10 é um muito competente sem especialização. O observador também pode especializar Percepção e chegar a +12: a especialização não é privilégio do furtivo.

**Omissão concreta da candidata:** a fórmula apresentada de Furtividade e a explicação de Percepção mencionam apenas atributo + maestria. A redação deve usar o bônus completo da perícia, incluindo especialização e modificadores aplicáveis. Não corrigir a análise limitando artificialmente Furtividade a +10.

As cadeias abaixo pressupõem esconderijo válido, acesso aos sinais e ausência de uma busca ou exposição adicional interrompendo a sequência. São testes de pressão em condições favoráveis, não uma previsão de todo combate. A manutenção atual não funciona quando o atacante termina claramente exposto.

## 1. As duas CDs na escala real

Cada célula informa **chance de Esconder normalmente / chance de manter com desvantagem depois de um ataque**.

### Base 8 + Percepção

| Furtividade | Percepção +0 | +4 | +8 | +10 |
|---|---:|---:|---:|---:|
| +4 | 85% / 72,25% | 65% / 42,25% | 45% / 20,25% | 35% / 12,25% |
| +7 | 100% / 100% | 80% / 64% | 60% / 36% | 50% / 25% |
| +10 | 100% / 100% | 95% / 90,25% | 75% / 56,25% | 65% / 42,25% |
| +12 | 100% / 100% | 100% / 100% | 85% / 72,25% | 75% / 56,25% |

### Base 10 + Percepção

| Furtividade | Percepção +0 | +4 | +8 | +10 |
|---|---:|---:|---:|---:|
| +4 | 75% / 56,25% | 55% / 30,25% | 35% / 12,25% | 25% / 6,25% |
| +7 | 90% / 81% | 70% / 49% | 50% / 25% | 40% / 16% |
| +10 | 100% / 100% | 85% / 72,25% | 65% / 42,25% | 55% / 30,25% |
| +12 | 100% / 100% | 95% / 90,25% | 75% / 56,25% | 65% / 42,25% |

Se `p` é a chance normal, desvantagem dá `p²`. O aumento de CD em 2 reduz a chance normal em 10 pontos percentuais na região não saturada. A redução na manutenção depende de onde o confronto está na escala; não é uma penalidade fixa e deixa de ajudar onde ambos os resultados são automáticos.

A base 8 favorece o personagem que está rolando: iguais passam em 65%. A base 10 deixa 55%. Nenhum desses valores é uma equivalência exata a uma disputa de dois d20: com bônus iguais, uma disputa produz 52,5% para quem vence os empates e 47,5% para quem perde. Uma CD fixa evita a segunda rolagem, mas escolhe um favorecimento; não há uma neutralidade matemática escondida em “usar o molde local”.

A regra de percepção passiva com ±5 também é uma convenção, não equivalência exata a rolar vantagem/desvantagem. Nos extremos seus efeitos se comprimem. Contexto que realmente justifique vantagem do vigia pode ajudar, mas não deve ser concedido sistematicamente pelo mestre para remendar uma manutenção automática forte demais.

## 2. As chances continuadas mudam a avaliação

Partindo **já oculto**, para declarar quatro ataques seguidos oculto bastam três manutenções: a revelação depois do quarto não altera seus benefícios retroativamente. Para continuar oculto **depois** dos quatro, é necessária a quarta manutenção.

| Confronto | Base | Manter após cada ataque | Declarar os quatro oculto | Ainda oculto após os quatro | Número médio de ataques até revelar, sem outras interrupções |
|---|---:|---:|---:|---:|---:|
| Bônus iguais | 8 | 42,25% | 7,54% | 3,19% | 1,73 |
| Bônus iguais | 10 | 30,25% | 2,77% | 0,84% | 1,43 |
| Furtividade +12 / Percepção +4 | 8 | 100% | 100% | 100% | O teste nunca revela |
| Furtividade +12 / Percepção +4 | 10 | 90,25% | 73,51% | 66,34% | 10,26 |
| Furtividade +12 / Percepção +10 | 8 | 56,25% | 17,80% | 10,01% | 2,29 |
| Furtividade +12 / Percepção +10 | 10 | 42,25% | 7,54% | 3,19% | 1,73 |

As probabilidades são condicionais à ocultação inicial. Se for preciso incluir a tentativa inicial, multiplique por sua chance de sucesso. A ameaça não é apenas “quatro ataques na rodada”; a mesma sequência pode atravessar rodadas enquanto o esconderijo continuar válido.

Investir em furtividade deve superar um vigia medíocre. **O problema adicional é transformar essa superioridade em dispensa de um custo recorrente de combate**, disponível a qualquer ficha, sem uma entrega específica de classe. Um especialista pode legitimamente esconder-se com facilidade e ainda revelar sua posição ao atacar.

Se uma vantagem válida cancelar a desvantagem da manutenção, a chance volta de `p²` para `p`. Entre iguais, a chance de ainda estar oculto depois de quatro ataques sobe de 3,19% para 17,85% com base 8, ou de 0,84% para 9,15% com base 10. Ajudar custa sua ação e uma ajuda não se estende automaticamente a todos os testes; não se deve tratá-la como vantagem permanente gratuita. Ainda assim, “com desvantagem” é uma penalidade cancelável pelas regras existentes, não um limite absoluto de frequência.

## 3. O que está sendo concedido além de uma porcentagem

### Ataques, informações e vantagem

A candidata relaciona vantagem a **ver sem ser visto**, não ao nome Oculto isoladamente. Esconder permite aplicar isso numa exposição cujo momento de revelação foi adiado até depois do ataque. A manutenção pode preservar essa oportunidade para os ataques seguintes na mesma posição, sem nova ação. Também conserva oportunidades de abate e o requisito de Sentença Final, quando os demais requisitos estiverem presentes.

Como ilustração de escala, um ataque que acerta normalmente em 55% passa a 79,75% com vantagem: ganho de 24,75 pontos percentuais. O 20 natural sobe de 5% para 9,75%. Isso não dobra a precisão, nem equivale diretamente ao mesmo ganho percentual de dano: a composição de dados, crítico e efeitos importa. No Golpe Cirúrgico, o crítico duplica os dados de Canalizar e do reforço, portanto essa melhoria de crítico interage com mais que o dado da arma.

Nem todo ataque feito oculto ganha uma vantagem adicional efetiva: o jogador pode já possuir vantagem, ou não enxergar o alvo. Nem retirar Oculto remove todo benefício de não ser visto: invisibilidade, escuridão e cobertura conservam seus efeitos próprios. A revisão deve manter essa distinção explícita.

### Ações e competição entre benefícios

- **Regra comum:** repetir Esconder custa Padrão. Manter-se de graça depois de atacar preserva essa Padrão para continuar atacando. Não é equivalente a “apenas um teste defensivo”.
- **Incursor 2:** repetir Esconder custa Bônus. A manutenção poupa a Bônus, que pode servir a outras ações e usos do kit. A gratuidade comum reduz o valor relativo da permissão do Caminho.
- **Assassino 11:** sua tentativa gratuita continua útil se a manutenção falhar; não fica literalmente inútil. Mas vira uma segunda tentativa no mesmo turno após um primeiro benefício gratuito que não foi comprado pela Trilha. Isso infla a confiabilidade e desloca a identidade de atacar, mover-se e desaparecer para uma rotina de manutenção antes de sequer usar a habilidade.

Se o Assassino começa oculto, ataca, conserva um esconderijo válido e pode cumprir Desaparecer no Percurso depois, a chance de terminar oculto é `q + (1−q)×p`, onde `q=p²` é a manutenção e `p` sua tentativa normal posterior:

| Confronto | Base | Com manutenção + tentativa legal da Trilha | Só tentativa da Trilha após revelação |
|---|---:|---:|---:|
| Bônus iguais | 8 | 79,79% | 65% |
| Bônus iguais | 10 | 68,61% | 55% |
| +12 contra +4 | 10 | 99,5125% | 95% |

**O perfil +12 contra +4 é um teste matemático de personagem especializado em nível alto com Desaparecer já disponível; +12 não foi tratado como bônus típico do próprio nível 11.** Isso pressupõe ataque e arma elegíveis, Alvo Estudado, movimento e posição de Esconder disponíveis. Uma segunda tentativa não é automaticamente legal só porque o personagem tem nível 11.

Num modelo ainda mais favorável de um ataque por turno, com essa tentativa posterior disponível em todos eles e nenhuma descoberta inimiga entre turnos, a fração estável de turnos que começam ocultos entre iguais seria 76,28% com base 8 e 63,67% com base 10; sem manutenção comum, seria 65% e 55%. É uma medida de pressão do modelo, não uma previsão de campanha.

Para a ficha comum que insistisse em sempre atacar oculto e pagasse Padrão para renovar após cada revelação, a manutenção reduz o número esperado de ações de Esconder necessárias por ataque de 1,54 para 0,89 entre iguais com base 8; com base 10, de 1,82 para 1,27. Essa conta idealizada pressupõe repetição legal de tentativas em esconderijos adequados. Demonstra a economia produzida pela regra; não cria autorização para repetir sem mudar a situação.

## 4. Busca ativa: números acima de 20 e tentativas sem saída

**CD acima de 20 não é, por si, impossível.** Percepção +10 alcança 30. A impossibilidade começa quando a CD guardada supera **20 + o bônus total do buscador**. Vantagem não amplia esse máximo; apenas aumenta a chance de atingir resultados já possíveis. Não se deve inventar sucesso automático no 20 para encobrir essa consequência.

Exemplo: Furtividade +12 pode guardar totais 13–32. Um observador +0 jamais alcança 21–32 só com seu d20. Entre os resultados iniciais dessa ficha, **60% são impossíveis para esse observador**; ambas as bases permitem a ocultação inicial automaticamente nesse confronto. Depois de uma manutenção com desvantagem, **36% dos resultados** ainda ficam acima de 20. A manutenção não garante resultados baixos.

Em Furtividade +12 contra Percepção +4 e base 10, **42,11% dos sucessos iniciais** geram CDs acima de 24, impossíveis para aquela busca. Depois de uma manutenção bem-sucedida, isso cai a 17,73%, mas não zera. São probabilidades condicionais ao teste ter passado, e não a todas as tentativas iniciais.

A ação de busca também não tem a mesma chance de 65% ou 55% usada para entrar em ocultação. Entre bônus iguais:

| Base | Sucesso médio da primeira busca depois de Esconder bem-sucedido | Depois de manutenção bem-sucedida |
|---|---:|---:|
| 8 | 35% | 45,77% |
| 10 | 30% | 39,09% |

Subir a CD inicial filtra fora os resultados baixos; portanto os esconderijos que sobrevivem ficam, em média, **mais difíceis de buscar**. É mais um motivo para não concluir “10 é equilibrado” pela primeira rolagem isolada.

O resultado guardado fica fixo. Três buscas não equivalem a três confrontos com um total de Furtividade novo. Contra Furtividade +12 e Percepção +0, depois da ocultação inicial, a primeira busca normal tem 9% de sucesso médio; até três buscas independentes contra o mesmo total têm 20,16%, não `1−0,91³`. Os casos impossíveis continuam impossíveis por quantas ações forem gastas. O JSON integra a distribuição fixa de totais, inclusive esses casos.

**Procedimento necessário:** uma busca falha não renova a CD de Furtividade. Um resultado inalcançável não justifica cobrar Padrões infinitas na esperança de um 20. O observador precisa de outra abordagem: mudar para uma posição que forneça visão livre, obter uma pista que denuncie o espaço, usar um sentido/efeito apropriado ou contar com outro observador capaz. Isso não concede visão através de obstáculos nem obriga a revelar a CD exata ao jogador. O mestre deve comunicar o limite perceptível da abordagem e evitar repetir uma tarefa impossível.

Um teto artificial 20 para toda CD de Furtividade reduziria o valor dos bônus investidos e permitiria achar especialistas com 20 natural sem fundamento anterior. **Não recomendo acrescentar esse teto como remendo.**

## 5. Resets e informação que precisam permanecer coerentes

1. **Quem localizou não esquece porque outro observador falhou.** O total guardado e a lista de observadores que conhecem a posição têm funções diferentes. Uma manutenção contra quem ainda não localizou não readquire ocultação contra quem já a perdeu.
2. **Vários observadores usam a mesma rolagem de Furtividade.** Contra três vigias com o mesmo bônus, a chance de esconder-se dos três não é `p³`; é `p`. Buscas ativas separadas só se tornam rolagens adicionais com as ações e sinais de cada um. Um aviso de posição compartilha a descoberta conforme a própria candidata.
3. **Furtividade guardada não renova por turno, iniciativa ou busca inimiga.** A candidata acerta ao dizer isso. Nova rolagem exige uma tentativa legal ou a exceção que a autorize.
4. **Manutenção troca a CD, mesmo se piorar.** Hoje cada ataque reabre essa distribuição. Não se pode manter o maior resultado entre o antigo e o novo. Isso cria uma nova checagem e registro após cada golpe, e pode reduzir uma defesa forte ou elevar uma fraca.
5. **Revelar a posição e depois esconder o corpo no mesmo local não são automaticamente a mesma coisa que apagar a posição conhecida.** O capítulo afirma que perder visão não faz esquecer o espaço, mas a manutenção permite continuar oculto após expor-se para atacar, sem exigir mudança de local nem ocultação da origem. A tensão é de ficção e de procedimento, além da conta.
6. **Não abrir rolagens para “pescar” CD alta.** Trocar de esconderijo e gastar a ação pode justificar uma nova tentativa; atacar objetos ou golpear o vazio não deveria ser um botão de renovar gratuitamente a defesa guardada. Remover a manutenção comum fecha esse atalho sem acrescentar um catálogo de alvos válidos.

## 6. Comparação das alternativas

| Alternativa | O que resolve | O que permanece ou precisa mudar |
|---|---|---|
| Manutenção atual, apenas CD 10 | Reduz taxas na região central. | Gratuidade recorrente, resultados automáticos, segunda tentativa do Assassino, registro por golpe e ficção da posição que deixa de ser conhecida. |
| Ataques revelam; nova ocultação só pelas ações/exceções | Fecha a gratuidade comum, valoriza Bônus do Incursor e Desaparecer no Percurso; um procedimento claro por ataque. | Rever a decisão anterior da peça 14; preservar exceções pagas como Silencioso; explicar que revelação não dá visão através de cobertura e não acompanha movimentos futuros. |
| Manutenção conserva posição incerta, mas não Oculto | Pode conservar parte da distinção entre arma ruidosa e discreta sem manter os requisitos específicos de Oculto. | Cria terceiro estado; contradiz a definição atual se ninguém localiza o corpo; deixa a vantagem de “ver sem ser visto” potencialmente ativa; exige especificar espaço de origem conhecido, ataque por adivinhação, busca, alvo de técnica e quando volta a valer Oculto. É maior, não menor, que o conserto anterior. |

**Escolha recomendada:** ataques revelam para quem puder perceber os sinais pertinentes, depois do ataque que começou validamente oculto; tentar Esconder novamente usa a ação ou a habilidade normal. Não significa revelar magicamente o atacante a todas as criaturas do mapa. Tampouco significa conceder ao observador visão, linha de efeito ou acompanhamento de todo movimento futuro.

Se a fantasia de tiro discreto ainda precisar de manutenção em combate, tratá-la depois como benefício delimitado, com uma fonte, custo e frequência próprios. A presente avaliação não cria essa habilidade nem recomenda inseri-la às pressas na regra comum.

## Alcance desta validação

Foram enumerados exatamente todos os resultados dos d20 normais e com desvantagem dos 32 pares pedidos, com comparações de vantagem do observador, distribuição de CDs guardadas, uma e três buscas, cadeias de ataques e renovação condicional. O JSON contém frações exatas; o texto arredonda somente a apresentação. Verificações independentes por enumeração de 400 pares confirmaram `q=p²` em todos os casos.

Esses números demonstram problemas estruturais e efeitos da correção. Não estabelecem uma taxa ideal universal, não substituem teste em mapas e não certificam todas as técnicas, sentidos e condições do livro. O principal teste posterior é uma cena com esconderijo de fato útil, oportunidade de aproximar-se ou buscar e ações concorrentes, usando uma ficha comum, Incursor 2 e Assassino 11 sob o mesmo terreno.


## Adendo — leitura da revisão 2 já corrigida

Versão lida após o parecer: SHA-256 `ac41bea4902f4da63d61eb3bfe67810722b36a4f9f93cb6b2bc6c24b4f34db2d`, mesmo caminho do manuscrito.

**Correções confirmadas:** a CD agora é 10 + o bônus completo de Percepção; a especialização entra nos dois lados; a manutenção comum após ataque foi removida; revelar a posição não remove os efeitos próprios da falta de visão; a tentativa do Incursor e a do Assassino voltam a ser as formas de recuperar a ocultação com seus custos/requisitos. O exemplo da Rina acompanha a mudança. O antigo radar comum de 9 m foi retirado explicitamente e permanece como lacuna de design.

Os percentuais da manutenção e das duas tentativas do parecer principal são **diagnóstico do modelo abandonado**, não problemas que continuam nessa revisão. A revisão resolve o principal risco encontrado.

**Ajuste de procedimento ainda recomendado:** a busca continua usando uma CD guardada que pode superar o máximo do buscador. Acrescentar uma orientação curta para não cobrar buscas idênticas repetidas contra um resultado inalcançável: é preciso mudar a abordagem ou obter um sinal que realmente revele a posição. A falta de sucesso automático no 20 é coerente com a escala publicada; não precisa ser alterada. Essa orientação evita que o leitor espere que gastar suficientes Padrões force a descoberta.

**Ponto editorial a vigiar:** a linha 110 descreve a exposição pela lateral com visão, alcance e passagem para obter vantagem; deve continuar sendo uma permissão para esse ataque oculto, sem ser interpretada como proibição geral de um atacante oculto tentar um ataque sem enxergar o alvo. A regra geral da linha 100 permite essa tentativa com desvantagem, salvo exigência específica de visão. Não identifiquei nessa leitura uma regressão numérica que exija refazer a solução.

O registro de decisões ainda carregava manutenção, radar de 9 m e descrição da candidata anterior durante essa leitura; deve acompanhar a revisão antes da entrega. Como a edição estava em andamento, não trato isso como alegação enganosa nem como falha já entregue.
