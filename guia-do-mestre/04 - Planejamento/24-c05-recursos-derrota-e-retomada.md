# C05 — recursos, derrota e retomada

21 de outubro de 2026. Continuação autorizada por Mizuki para o manuscrito pré-1.0. A etapa explica os procedimentos atuais de acompanhamento, queda, socorro, retirada e recuperação. Não introduz prazos novos, política de morte, regra de ressurreição ou mecânica de treinamento.

## Entregas

- [Acompanhar recursos e consequências](<../06 - Redacao do Guia/21-acompanhar-recursos.md>).
- [Quedas e socorro](<../06 - Redacao do Guia/22-quedas-e-socorro.md>).
- [Retirada e recuperação](<../06 - Redacao do Guia/23-retirada-e-recuperacao.md>).
- [Registro de estado e socorro](<../06 - Redacao do Guia/24-registro-de-estado-e-socorro.md>).

O índice e a folha de condução remetem ao conjunto. A linha de continuidade conserva o estado da missão; o novo registro acompanha o personagem e uma eventual queda. Eles cumprem funções diferentes.

## Fonte e método de conferência

A fonte é o texto editável da R53, com caminho e SHA256 preservados em `apoio-c05/fonte-r53.json`. Foram lidos Dano e recuperação, Vida a zero, Insistir, Socorro, Sequelas e Cicatrizes, Derrota e morte, Inconsciente, Descansos, Exaustão e Cena e usos de habilidades. Reações e oportunidades, Carga, Arrastar e transportar e exceções citadas de Origens também foram conferidos.

A ordem de apresentação parte do acompanhamento, passa pela queda e chega à recuperação. O texto distingue descrição de um procedimento publicado, exemplo aritmético e consequência ficcional. Não foi necessário escolher números novos nem importar mecanismos de outro sistema.

A redação foi revisada para explicitar: tratamento não é vida atual durante Morrendo; estabilidade não é cura; fim de sessão não é descanso; reserva positiva não reabre participação depois de Derrotado. Os procedimentos de inimigos e entidades permanecem distintos dos de personagens jogadores.

## Exemplos e casos de limite

| Caso | Regra ou resultado preservado |
|---|---|
| Dano 21 com resistência, redução 4 e 3 temporários | Metade para cima dá 11; depois 7; perda de 4 na vida comum |
| Temporários com máximo de vida 23 | Teto 11; nova fonte substitui pelo maior saldo, sem somar |
| Integridade máxima 26 | Perder 6 não alcança 1/4; perder 7 alcança |
| Zero de vida com três Sequelas | Derrota imediata; gatilho comum de queda não supera essa derrota sem permissão expressa |
| Zero simultâneo de vida e Integridade | Resolver a derrota por Integridade, sem Insistir |
| Máximo 93 e Classe 3 | Aguentar 24, primeiro Insistir 31, posteriores 45 pelo teto |
| Primeiro Insistir com máximo 23 | Tratamento 8; receber 5 + 4 encerra com 9 de vida, limitado pelo máximo atual |
| Personagem passa de Insistir a Aguentar | Conserva requisito, tratamento e janela; não pode voltar na mesma queda |
| Volta completa ao ponto da queda | Consome janela antes de ação futura naquele ponto; gatilhos específicos conservam seu momento |
| Dano posterior que alcança a vida | Consome janela sem apagar tratamento; excesso do golpe original não cobra outra rodada |
| Estabilização bem-sucedida | Para a contagem temporal, sem cura, despertar ou renovação de prazo |
| Estável com 18 de tratamento, requisito 31, fora do perigo | Após a pausa curta correspondente, saída especial converte 18 + 1 em 19 de vida, até o máximo atual, com Sequela |
| Cura depois de Derrotado | Pode recuperar vida, sem reabrir participação naquela cena |
| Recuperação depois da derrota ainda a zero de vida | Teste de Estabilizar na pausa é o atendimento específico desse procedimento; não abre nova janela |
| Descanso curto com máximo 10 PE e saldo 1 | Recupera 2, ficando com 3 |
| Curto fora de ambiente propício, máximo 8 PE | Recuperações 2, 1, 1 e 0 conforme degrau de Exaustão |
| Longo fora de ambiente propício, vida máxima 23 | Saldo 3 vai a 11; saldo 18 permanece 18 |
| Transporte de corpo de 60 kg | Corpo ocupa 5 de Volume; equipamentos continuam tabelados e entram à parte |

A estabilização com 18 de tratamento é um caso separado para explicar a saída excepcional. Não modifica as ações ou curas do piloto. Os máximos e Classes dos exemplos são referências parciais de cálculo, não personagens completos nem escalas novas de equilíbrio.

## Verificações executadas

`apoio-c05/conferir_exemplos.py` executou 46 conferências aritméticas e de limite. Inclui os três modos de tratamento para máximos 23, 93 e 395, tetos, arredondamentos, temporários, pausas, carga e comparação de movimento. Resultado em `apoio-c05/resultado-exemplos.json`.

O roteiro determinístico anterior foi reexecutado por `apoio-piloto/conferir_exemplo_guiado.py`. Foram novamente conferidas as duas quedas, a conversão de tratamento e o ramo com Derrotado. O JSON gerado foi comparado ao estado anterior, sem alterar seus resultados. A simulação ampla não foi repetida: as fichas, valores e modelo do piloto não mudaram.

Essas verificações são cálculo e conferência documental. Não são leitura por participantes nem teste de mesa. A verificação de integridade, links e fonte da etapa está em `apoio-c05/verificacao.json`.

## Consequências e decisões

D14 recebeu indicação da entrega baseada na R53. Captura, resgate, perda de objetivo e retirada aparecem como possibilidades que precisam decorrer dos acontecimentos e acordos; não se tornaram consequências automáticas ou políticas universais.

A redação preserva a escolha de campanha sobre morte permanente prevista pela base e sua definição antes da missão. O destino físico do personagem não pode ser trocado retroativamente para ajustar o drama. Também não foram criadas penalidades de Cicatriz ou perda permanente de capacidades por descrição.

No descanso longo, a ordem de recuperação e remoção de Sequelas foi mantida. A Exaustão tem seus gatilhos e margens publicados, sem novas cobranças por atividade cotidiana. Núcleo Dependente mantém a exceção de não possuir Integridade; entidades conservam seu procedimento próprio, que será aprofundado na frente correspondente.

## Cobertura e continuação

P16 recebe procedimento, demonstrações e ferramenta, com ligações a P08, P11, P18 e P19. O tratamento editorial inicial de C05 está disponível para integração e revisão; a conferência global dos 130 pontos ainda ocorrerá no manuscrito completo.

Próxima tarefa recomendada: C06 — conferência de personagens, vínculos e convivências. **GPT-6.1 Sol, esforço alto** para a redação e os exemplos. Se houver proposta de convivência além da base atual do Receptáculo, preparar a comparação com **GPT-6 Astra, esforço alto**, e levar a decisão necessária a Mizuki antes de adotar.

A R53, PDFs e relatórios de origem foram preservados. O estado anterior dos arquivos alterados está em `apoio-c05/historico/antes-da-redacao/`.
