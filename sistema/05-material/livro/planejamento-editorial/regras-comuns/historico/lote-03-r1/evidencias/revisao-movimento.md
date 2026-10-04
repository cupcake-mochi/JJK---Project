# Revisão focal — movimento, saltos e quedas

Leitura de 02/10/2026. Somente crítica; nenhum arquivo do projeto foi alterado.

**Documento examinado:** `sistema/05-material/livro/planejamento-editorial/regras-comuns/lote-02/02-SALTOS-E-QUEDAS.md`.

**SHA-256 da versão lida:** `cad3b5ca2e5b8041f34e7fb8865c1c66f99ace08776c2c70e1204c5fa29d2c02`.

## Parecer

A amostra já responde à direção de simplificar com uma base inspirada em D&D e adaptada à escala do Projeto M. A regra principal cabe em poucas consultas; todas as distâncias publicadas respeitam unidades de 1,5 m; o dano e seu teto são consistentes; a reação genérica para segurar bordas foi retirada. A separação entre travessia comum e os apoios especiais do Parkour está preservada. Restam dois esclarecimentos de resolução e a sincronização dos registros antes de fechar este lote.

## Ajustes necessários no manuscrito

### 1. Exigir expressamente os dois limites num salto combinado — linhas 58–64

A regra fornece alcances horizontal e vertical e escolhe o maior deles para cobrar movimento, mas não diz expressamente que ambos continuam limitando o mesmo salto. A regra de custo pode ser confundida com a autorização do percurso.

**Inserção curta sugerida:** “Se o salto avançar e subir, respeite os dois limites. O esforço adicional pode aumentar apenas um deles.”

**Caso que precisa ter resposta única:** Força 0, com impulso, permite 3 m na horizontal e 1,5 m na subida. Com esforço, pode tentar 4,5 m de avanço e 1,5 m de subida, ou 3 m de avanço e 3 m de subida. Não pode aumentar ambos para 4,5 m e 3 m com o mesmo teste. A cobrança pelo maior eixo é uma abstração coerente; não há necessidade de trocá-la por soma ou geometria.

### 2. Definir a falha quando esforço e terreno coexistem — linhas 66–68

O texto determina uma única rolagem contra a maior CD, mas depois distingue falha “apenas no esforço” de falha “causada pelo terreno”. Falta dizer como essa causa é identificada.

**Exemplo:** esforço CD 14 e obstáculo CD 18, resultado 15. A distância estendida foi atendida, mas o obstáculo não. Com resultado 12, ambos falharam. Hoje o leitor pode tanto recuar à distância normal quanto aplicar uma consequência ambiental incompatível com essa posição.

**Fechamento curto recomendado:** conservar uma única rolagem e comparar seu resultado às exigências presentes. Quando a CD ambiental falhar, aplicar a consequência anunciada para o obstáculo; quando ela for atendida e apenas o esforço falhar, usar o alcance normal do eixo escolhido. O mestre deve anunciar o que a falha ambiental faz ao percurso antes da tentativa. Isso não exige um teste por eixo nem por dificuldade.

Se a opção editorial for resolver toda tentativa combinada apenas contra a CD maior, a alternativa é declarar que a consequência anunciada cobre a tentativa inteira, inclusive onde o personagem fica. Nesse caso, remover a separação de causas que o procedimento não calcula. A primeira solução conserva melhor a promessa atual de que falhar somente no esforço atinge a distância normal.

## Conferências sem necessidade de correção

- **Unidades e contas:** a tabela horizontal está correta para `3 + 1,5 × Força`; o salto parado aplica metade e arredondamento inferior corretamente. A vertical usa 1,5 m ou 3 m; Força menor que 5 não ganha subida gratuita de 1,5 m parado, mas pode tentar o esforço. Isso não impede pequenos pulos no mesmo piso, como o texto já explica.
- **Custo:** o impulso custa seus metros; o salto custa o maior entre avanço e subida; Correr acrescenta movimento sem aumentar o alcance; a tentativa falha perde o movimento reservado. Os exemplos fecham: Rina gasta `3 + 4,5 = 7,5 m` de 9 m; o Assassino gasta `6 + 4,5 = 10,5 m` de 12 m. A reserva para o salto precisa incluir a distância que se tenta alcançar, e não somente a base; a leitura atual permite isso, sem exigir novo subsistema.
- **Parkour:** a exclusividade está corretamente circunscrita a terminar o **percurso acrobático** em borda/apoio especial, usar a vítima como apoio e substituir Atletismo por Acrobacia nos testes autorizados. Não se proíbe a escalada comum de outras personagens. A descida apoiada de 4,5 m continua diferente de cair livremente e continua apta a acionar a aproximação de abate.
- **Benefício da perícia:** o teste do esforço CD 14 dá utilidade concreta a Atletismo, e a substituição específica mantém Acrobacia relevante para o Assassino. Com bônus +4, o esforço passa em 55%; com +10, em 85%, antes de vantagens ou outros modificadores. A perícia melhora a confiabilidade da extensão; a distância-base é governada por Força. Isso corresponde à direção escolhida, não à proposta anterior de grandes extensões por uma escada de CDs.
- **Vítima como apoio:** a regra da Trilha continua disponível, com o salto alcançável e o movimento restante. Convém testar em mesa o caso de Assassino com Força baixa saltando para cima depois do ataque: se não houver o impulso imediatamente anterior exigido pela regra comum, alcançar apoio elevado em 1,5 m dependerá do esforço CD 14. É uma consequência real desta base, não uma contradição textual nem motivo para conceder impulso gratuito nesta revisão.
- **Quedas:** `1d6 por 3 m completos, até 20d6` produz exatamente a tabela. Quedas de 4,5/6/9/30 m causam 1d6/2d6/3d6/10d6. O limiar, o estado Derrubado condicionado a receber dano e o arredondamento do dano na água estão escritos. Concussão mantém a resistência do Bastião aplicável. Não é necessário adicionar a antiga mitigação universal por Acrobacia; ela foi abandonada nesta proposta.
- **Teto:** 20d6 tem máximo 120. Um Incursor de nível 30 com Constituição 2 tem 182 de Vida; portanto, queda nenhuma o leva de Vida cheia a zero somente por esse dano. Mesmo com Constituição 0, sua Vida cheia é 122. A resistência do Bastião reduz ainda mais o risco. Isso deve constar como consequência aceita da fantasia sobrenatural e do teto escolhido, sem afirmar que quedas conservam risco letal independente de nível. Não é um erro nas contas nem requer retirar o teto silenciosamente.
- **Movimento Acrobático:** o texto identifica a quota por ciclo como conciliação da amostra; não a apresenta como regra já publicada. Correr não renova a quota, movimento adicional a compartilha e o turno antecipado não cria duas renovações. Os saltos comuns não consomem novamente a quota por paredes. O exemplo de parede + salto funciona com a habilidade integrada.
- **Recargas:** o exemplo de atividade que consome a Ação de Movimento inteira é válido. A exceção existe no Vanguarda integrado, em `caminhos/05-Edicao-Integrada/02-Vanguarda-Caminho-e-Trilhas.md`, na recarga parcial de arma de fogo. A recarga comum ser Bônus não invalida “certas recargas”.

## Registro do lote ainda precisa acompanhar a amostra

`02-DECISOES.md`, na leitura realizada junto desta revisão, ainda descreve a proposta anterior: custo horizontal + subida, valores verticais de 0,5 m/1 m/2 m/2,5 m, dano fixo sem teto, mitigação universal por Acrobacia e reação geral de segurar borda. Também conserva os percentuais de saltos daquela tabela e a afirmação de proteção finita por Acrobacia.

Sincronizar esse documento e qualquer resumo que ainda trate esses candidatos como a escolha vigente antes de entregar o pacote. As comparações antigas podem continuar como histórico identificado; não podem contradizer o manuscrito dizendo que são o resultado atual. Esta constatação não afirma que os registros já estavam finalizados pelo editor.

## Fonte de compatibilidade

`caminhos/05-Edicao-Integrada/06-Incursor-Caminho-e-Trilhas.md`: Movimento Acrobático; Passo Guardado; Movimento Acrobático ampliado; Um Passo à Frente; Parkour, especialmente Apoios de infiltração, Aproximação de abate e A vítima como apoio. A revisão focal não repete uma auditoria de todo o Caminho nem certifica equilíbrio de todas as combinações.
