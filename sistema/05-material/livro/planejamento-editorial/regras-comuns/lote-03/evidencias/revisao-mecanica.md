# Lote 03 — revisão mecânica independente

Revisei `sistema/05-material/livro/planejamento-editorial/regras-comuns/lote-03/03-PERCEPCAO-E-FURTIVIDADE.md`, versão lida em 02/10/2026, linhas 1–124. Conferi contra o manual e Caminhos integrados indicados em `/tmp/lote03-auditoria-percepcao.md`. Não alterei fontes e não usei Git. É revisão de texto e execução de casos, não playtest humano.

## Parecer

O procedimento principal é executável. Há ação, condição de entrada, teste, desempate, duração, CD guardada, busca ativa e saída de ocultação. A manutenção não concede Esconder gratuitamente a quem estava exposto. Os exemplos numéricos fecham. A ampliação de Vasculhar resolve a lacuna sem criar uma nova ação, e Sentir Energia 9 m está honestamente apresentado como proposta.

Recomendo corrigir os dois primeiros itens antes de fechar e acrescentar a definição curta do terceiro. O quarto é uma precisão útil, sem exigir outra regra. Não encontrei motivo para reabrir as classes nem criar mais recursos.

## Achados e menor correção

### 1. Silencioso pode perder a exceção pelo próprio efeito que acabou de produzir — prioridade alta

**Minuta: linha 118.** A oração “ou ser localizado pelo efeito produzido” pode permitir revelar automaticamente a origem de qualquer feitiço visível, mesmo com Silencioso. Um mestre lê que o disparo mostra de onde veio; outro aplica a exceção. A primeira leitura esvazia uma parte expressa da compra.

**Dono vigente:** `manual/40-fundamento.md:750`: usar Silencioso não revela a posição e não exige sinal; o texto conserva Selos de condição. Invocações repete a melhoria no catálogo atual.

**Caso:** o personagem oculto conjura um projétil Silencioso sem sair do esconderijo. O alvo percebe o projétil/impacto. A frase da minuta permite dizer que o efeito mostrou sua origem e retirar ocultação, apesar de “usar não revela”.

**Menor correção:** retirar esse exemplo de revelação automática. O efeito pode ser percebido sem revelar automaticamente o espaço do conjurador. Manter exposição do corpo, busca bem-sucedida e outras pistas independentes como causas normais. Se uma habilidade específica revela expressamente a origem, ela prevalece. Não é necessário tornar o feitiço invisível nem silencioso para todos os efeitos: apenas preservar a promessa de não revelar a posição pelo uso.

### 2. Visão às cegas precisa de uma ponte explícita para não virar detecção com penalidade permanente — prioridade média

**Minuta: linhas 10, 22, 97–101.** O texto admite um sentido apropriado, mas a vantagem/desvantagem depende literalmente de “enxergar”. Nenhum trecho explica como tratar a visão às cegas já existente.

**Dono vigente:** `manual/47-bencaos-e-lapidacao.md:185–189`, Vulto: percebe ao redor sem olhos abertos por som/movimento; o benefício é chamado **visão às cegas**, com raio próprio.

**Caso:** usuário de Vulto fecha os olhos dentro de seu raio. Uma leitura da minuta o localiza, mas impõe desvantagem por não enxergar, como se tivesse somente Sentir Energia. Outra aplica visão às cegas e permite combate sem essa penalidade. Esta diferença afeta a compra atual.

**Menor correção:** uma frase dizendo que um sentido descrito como visão às cegas substitui a visão para perceber e atacar dentro do alcance e limites próprios. Sentir Energia não recebe isso. Não conceder automaticamente leitura fina, visão através de parede nem dispensar um Selo que exija olhos/visão de maneira específica. A condição Cego continua com seu texto; a exceção vem do sentido especial, não de reescrevê-la globalmente.

### 3. Uma busca pode abranger vários ocultos, mas a quantidade de testes/resultados não está fixada — prioridade média

**Minuta: linhas 68–80.** Vasculhar declara lugar/setor, porém o procedimento passa para “uma criatura/uma presença”. Não diz se uma ação e rolagem podem encontrar todos os ocultos relevantes ou somente um. A mesma questão reaparece na detecção de energia através da parede.

**Caso:** na sala escolhida estão duas criaturas ocultas, com Furtividade 12 e 17. O investigador tira 15. Ele encontra apenas a de 12? Precisa declarar antecipadamente a criatura que nem sabe existir? O segundo teste consome outra ação? Para a energia sem ocultação, há duas presenças atuais no mesmo setor e dentro de 9 m: uma ação localiza uma ou ambas?

**Menor correção recomendada:** uma rolagem por ação contra cada resultado guardado das criaturas cujos sinais estejam acessíveis no lugar declarado; localizar as que a rolagem alcançar. Uma só busca, sem rerrolar para cada alvo. Presenças sem ocultação dentro das condições de detecção são identificadas ao concluir a ação. O limite de sentidos/setor e o alcance já impedem que isso procure o mapa inteiro. Se a intenção for apenas uma criatura por ação, escrever explicitamente; hoje há duas leituras operacionais.

### 4. Aviso do aliado deve transmitir posição daquele momento, não acompanhamento — precisão pequena

**Minuta: linha 76**, em conjunto com 10–14. O aviso que localiza para quem compreende é plausível, mas pode virar localização compartilhada indefinida se o exemplo for lido isoladamente.

**Caso:** A localiza o Assassino e avisa B. Depois, o Assassino muda de posição atrás da parede. B conserva a informação recebida, mas não adquire os sentidos de A nem passa a acompanhar todo movimento oculto.

**Menor correção:** acrescentar “naquele momento” ao aviso ou dizer que ele informa o último espaço conhecido. A regra de esconder novamente e a percepção própria continuam determinando o que acontece depois. Não exige telepatia, contadores nem ação nova.

## Casos que passaram

- **Exemplo Rina:** Furtividade 15 passa contra CD 12 do observador +4, falha contra CD 16 do observador +8. Busca 11 + 4 alcança 15. Conferência aritmética executada.
- **Novo observador:** Furtividade igual à CD de percepção permanece oculta; a linha 51 usa estritamente “menor”. Não contradiz o desempate da linha 47.
- **Bônus da percepção:** inclui Essência e maestria se treinado; vantagem/desvantagem está expressa na CD. A adaptação usa base 8 local e não inventa uma ficha separada de Atenção.
- **Incursor 2:** troca Padrão por Bônus para Esconder; não ganha Fluidez por isso. O procedimento não cobra outra ação oculta depois.
- **Assassino 11:** pode perder ocultação ao atacar, mover-se e Esconder sem ação pela habilidade. Um personagem comum nas mesmas condições não ganha esse teste gratuito.
- **Sentença Final:** o requisito é verificado na declaração, como na classe; revelação posterior não retira o crítico/execução já legitimados. Movimento visível anterior ao ataque pode retirar o requisito.
- **Lançamento Cruzado:** é outro ataque; a manutenção do primeiro ocorre antes dele. O novo alvo pode ter percepção diferente. A ocultação não é propagada à sequência inteira por uma única verificação final.
- **Mudar o Destino:** por ser correção do mesmo ataque, não acrescenta outro teste de manutenção. Continua reavaliando condições contra o novo alvo pela regra da trilha.
- **Trajetória Perfeita:** cada ataque tem verificação; a vantagem própria continua valendo se o atacante for descoberto. A regra comum não distribui a outros ataques a capacidade específica de impedir Bloquear.
- **Reflexo:** a minuta não introduz obrigação de ver para atacar. Um alvo localizado pode ser atacado com a penalidade comum por falta de visão. O simples erro de um agressor não concede localização automática.
- **Bloquear:** não há proibição nova para quem recebe ataque oculto. A defesa comum permanece disponível conforme o livro.
- **Sem Ver e Alvo Estudado:** posição por energia não satisfaz visão. A melhoria continua com função; o Assassino não pode escolher nova vítima através da parede só porque detectou presença.
- **Ricochete:** alvo localizado/percebido pode estar sem linha direta, mas o percurso continua exigindo passagem física; a nova regra não permite atravessar parede.
- **Faro de Origem:** a busca de presença atual não vira substituição irrestrita de Investigação para rastros antigos.
- **Ler o Ambiente:** permanece Bônus para informação do lugar; não é busca barata de criaturas.
- **Custos:** Vasculhar e Esconder Padrão, exceções de classe preservadas; falha na busca em combate consome a ação. Não encontrei geração gratuita de nova ação ou Fluidez.

## Limites da conferência

Não fiz balanceamento completo de alcance energético, vantagem ou duração da ocultação. O raio de 9 m e detecção por parede são decisões novas assumidas pela proposta; não eram números recuperáveis das fontes. Em bônus iguais, a comparação com base 8 dá 65% de sucesso para esconder; o teste de manutenção com desvantagem dá 42,25%. Esses dois valores foram calculados por enumeração do d20 e dos pares de d20: descrevem a regra proposta, não provam equilíbrio em mesa.

A opção de manter desvantagem quando ambos não se veem é explícita nas linhas 97–101 e evita o cancelamento automático pelo próprio procedimento. Condições específicas, inclusive Cego, continuam com seus textos; não trate isso como reprodução literal de D&D.
