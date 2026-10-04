# Revisão de Aptidões e Refino

Candidata R09 completa em vinte páginas lógicas, com quinze aptidões e o procedimento de Kokusen. O texto permanece separado do manual publicado. A exportação e a inspeção visual do PDF serão feitas pelo agente principal.

## Decisões principais

A revisão preserva as mudanças autorais da v0.176: Canalizar desde Refino 1, Projetar pago em d6 e Cortina com 40 vezes Refino de vida. A peça 11 e seus verificadores não incorporaram integralmente essas mudanças. Sua aprovação automática não demonstra que a versão antiga seja a vigente.

Canalizar em Golpe é o dano adicional de Canalizar Energia. Ele não entra no ataque que transporta um feitiço de dano; conjurar em outro momento não o apaga dos demais ataques. A exceção de crítico do Assassino continua funcionando. O capítulo não repete habilidades de Caminho ou Trilha.

Projetar usa Ação Padrão e o atributo de conjuração já registrado na ficha. Impor Essência criaria uma exigência nova: no cenário de Defesa 20 e maestria 4, Essência 0 produz 25% de acerto, contra 55% com o atributo habitual 6. A candidata não introduz essa penalidade.

A regra ofensiva de Forma Cura fica completa em Ferir maldições: exige Energia Reversa e ataque contra Defesa; só converte dados em dano contra maldições; conserva o custo e recebe o acréscimo publicado de 50%. Seu tipo é Energia Reversa, já existente em Dano e Condições. Não foi criado um tipo novo nem uma aptidão nova de cura externa.

## Resultados quantitativos

O script reproduzível em `evidencias/conferir_aptidoes_candidata.py` aprovou **74 verificações**, enumerou **2.187 sequências de marcos** e **1.792 sequências de resultados do Domínio Simples**. Oito perturbações deliberadas foram detectadas. O verificador editorial real, incluindo os blocos de prosa e as três remissões contextuais justificadas, passou sem achados.

A comparação inclui 58 perfis de Projetar e 290 perfis de Canalizar com um a cinco ataques. Os perfis anteriores ao nível 6 são identificados como sem acesso ordinário à compra de Projetar. Os múltiplos ataques são cenários de sensibilidade: não garantem que uma ficha possa realizá-los sem pagar os custos de sua Trilha.

Projetar não é a opção mais eficiente de dano por PE. Ele entrega média de 3,5 por PE, contra 4,5 de um Projétil vazio do Fundamento. No Refino 10, seu investimento máximo entrega 35 antes de acerto, contra 27 do Classe 0 no nível 30. O disparo pago compra independência de Selo, tipos e Famílias da técnica; seu preço relativo merece teste de mesa. A revisão não aumenta seu dano para esconder essa diferença, nem transforma o baixo resultado da versão antiga em justificativa para restaurá-la.

O raio do Domínio Simples foi convertido ao múltiplo de 1,5 m mais próximo. No Refino 4, 3,5 m vira 3 m: a área circular ideal cai cerca de 26,5%. No Refino 8, 5,5 m vira 6 m: sobe cerca de 19%. No Refino 10, 6,5 m vira 6 m: cai cerca de 14,8%. Isso é mudança mecânica registrada, não correção meramente gráfica. A quantidade de miniaturas cobertas depende do mapa e não foi inferida dessa área geométrica.

Barreira Simples e Cortina agora têm um único exemplar ativo por criador. No Refino 6, continuam com 30 e 240 PV, respectivamente; preparar dez cópias não cria uma reserva acumulada de 300 ou 2.400 PV. A Cortina tem limite territorial de 90 m até sua borda mais distante e não herda a vedação completa de ataques da Barreira Simples.

## Regressão publicada

Foram executados seis scripts existentes, sem alterar suas fontes. Quatro terminaram com sucesso. `conta-extensao.py` e `conta-as-quatro.py` pararam por âncora ausente do fator de Intervenção na peça 26. As saídas completas estão em `evidencias/*-PUBLICADO.txt` e o estado em `REGRESSAO-PUBLICADA.json`. Essas duas falhas não foram escondidas ou convertidas em aprovação da candidata.

O verificador antigo de aptidões passou mesmo usando Projetar gratuito e a escala anterior de Canalizar. A bateria nova cobre as regras candidatas. Os scripts antigos precisam ser sincronizados na integração, junto de seus donos, preservando as evidências históricas.

## Validações e limites

`REVISAO-POR-SECAO.json` registra a leitura contextual das vinte unidades: clareza, suficiência, títulos, vocabulário, voz, redundância, localização, regra, funcionalidade, compatibilidade, números, comparação com RPG e relação com a obra. `CASOS.json` reúne casos positivos e negativos. `INTERFACES.json` registra os contratos com os capítulos vizinhos.

A comparação com D&D foi metodológica e usa fontes primárias, documentadas em `pesquisa-editorial.md`. Os procedimentos numéricos são adaptações do Projeto M. A auditoria local de cânone foi consultada para evitar alegações indevidas; não se afirma uma leitura primária inédita de todos os capítulos do mangá.

Não houve playtest, teste de compreensão com pessoas ou prova de equilíbrio integral de todas as combinações de Caminhos. Os exemplos e os limites testados funcionam no modelo declarado. A validação visual permanece pendente até a exportação e leitura das páginas pelo agente principal.
