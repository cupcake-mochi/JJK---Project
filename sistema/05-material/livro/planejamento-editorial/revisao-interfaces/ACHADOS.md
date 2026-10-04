# Revisão das interfaces de regras — achados

Item 2 da fila pós-reconstrução, feito em 04/10/2026 sobre a candidata de 03/10/2026.

**Esta é uma revisão por modelo, feita só lendo o texto.** Não é revisão humana, não é leitura de jogador e não é playtest. Ela aponta onde dois capítulos não fecham entre si; não mede se uma regra é boa em mesa.

Cinco grupos, cada um lido contra os capítulos que conversam com ele:

| Grupo | Assunto | Relatório completo |
|---|---|---|
| G1 | queda, Morrendo, Derrotado, socorro, Sequelas e Integridade | `grupos/G1.md` |
| G2 | ações e reservas das invocações | `grupos/G2.md` |
| G3 | Fluidez, continuações do Malabarista e gasto de Fluidez | `grupos/G3.md` |
| G4 | equipamento, carga e munições | `grupos/G4.md` |
| G5 | Fundamento, Catálogo, compatibilidades e Técnica Máxima | `grupos/G5.md` |

Cada relatório traz, por achado, os dois trechos que não fecham, o problema, uma correção sugerida e a confiança. No fim de cada um há a lista do que foi **conferido sem problema**, que é metade do valor da revisão: diz o que não precisa ser relido. As linhas citadas nos relatórios são as do texto **antes** das correções desta rodada.

## Resumo

51 achados. 17 corrigidos na primeira passada e 2 corrigidos em parte, todos do tipo "nome, custo ou remissão divergindo de uma regra já aprovada em outro capítulo". Seis dessas correções (C01, C07, C09, C10, C13 e C14) mudam o resultado na mesa para quem lia só o capítulo corrigido; `CORRECOES-APLICADAS.md` diz o que muda em cada uma. Contra a `v0.331` dos jogadores, só a C14 muda regra; as outras cinco devolvem o que ela já dizia. Na segunda passada, o Mizuki decidiu 4 (G2-03, G2-04, G3-07 e G4-01), e as decisões foram aplicadas. Os outros 28 ficaram como estavam, porque pedem uma decisão de regra, de nome ou de redação, ou porque falta escrever uma regra que nenhum capítulo tem.

O antes, o depois e o motivo de cada correção estão em `CORRECOES-APLICADAS.md`.

## O que precisa do Mizuki

Ordenado pelo peso em mesa. As quatro decisões de 04/10 (besta, pistola, ataque da entidade e corpos) já estão aplicadas e saíram desta lista, junto com a besta no Combate Irregular, que ficou só para Arma de Fogo (D04).

1. **G1-05 · Ordem da queda.** Ainda de Pé depois de Aguentar, e Ainda Há Tempo antes ou depois da escolha. Decide se a perda de 1/8 da vida máxima do Insistir acontece.
2. **G1-07 · Feito 8 do limiar.** Depois de DR13 ele só cobre dano de Alma e ficou fora do filtro de ameaça real. Escolher o alcance.
3. **G4-07 · Batedor: Arma de Fogo no nível 2.** A arma depende de uma autorização que a criação não dá. A Trilha concede ou o mestre confirma antes.
4. **G3-03, G3-04, G3-05 · Três ordens pequenas da Fluidez e do Malabarista.** Acúmulo de saques gratuitos, Fluidez antes do primeiro turno e momento do Instante Decisivo contra o Bloquear.
5. **G5-02 e G5-10 · Nomes.** "Calo — Livre" ficou com o rótulo antigo, e o Emanador reaproveita "Impulso" e a família "Expressão".
6. **G1-02 · Tipo do dano da Cisão.** Se continua com o tipo da arma ou vira dano de Alma.

Os casos de mesa que medem as lacunas abertas estão nos casos-sonda de `../testes-com-leitores/CASOS-SONDA.md`.

## Todos os achados

Situação: **corrigido** (com o código da correção), **decidido** (o autor escolheu, com o código da aplicação), **decisão** (regra, nome ou redação que é do autor), **lacuna** (falta escrever uma regra; o dono provável está na coluna), **remissão** (o destino precisa ser nomeado ou criado).

| Achado | Assunto | Tipo | Situação | Dono |
|---|---|---|---|---|
| G1-01 | "Integridade" usada como atributo de arma | inconsistência | corrigido (C01) | Emanador |
| G1-02 | Cisão remete a "dano direto à alma", que não existe | remissão | decisão (tipo do dano), depois remissão | Dano e recuperação |
| G1-03 | Entidade a Integridade zero sem desfecho | lacuna | lacuna; decidir com a revisão adiada de Morrendo | Invocações em campo |
| G1-04 | "Regras próprias de derrota" dos inimigos sem destino | remissão | remissão: nomear onde fica | Dano e recuperação |
| G1-05 | Ordem entre a escolha imediata e o que dispara na queda | lacuna | decisão pequena | Dano e recuperação, Bastião |
| G1-06 | Expansão de Domínio de dono Derrotado ou Inconsciente | lacuna | decisão | Poderes avançados |
| G1-07 | Feito 8 mudou de alcance com DR13 | decisão de regra | decisão | Progressão |
| G2-01 | "Ação Completa" sem definição no capítulo dono | inconsistência | corrigido (C04) | Regras gerais |
| G2-02 | Domada que não pode ser recolhida | lacuna | lacuna | Invocações em campo |
| G2-03 | Retomar corpos excedentes | decisão de regra | decidido e aplicado (D03, D03b, D03c): volta com trava | Invocações em campo, Fabricação, Progressão |
| G2-04 | Que ataque a entidade usa | decisão de regra | decidido e aplicado (D02, D02b): Classe 0 ou arma | Invocações em campo, Construir invocações |
| G2-05 | Concentração da entidade que sai de campo ou cai | lacuna | lacuna | Invocações em campo |
| G2-06 | Retorno de entidade caída numa troca | lacuna | lacuna | Invocações em campo |
| G2-07 | Limite de carga, passageiros e montaria da entidade | lacuna | lacuna (junto com G4-10) | Invocações em campo |
| G2-08 | Preparar um deslocamento com a entidade | lacuna | lacuna | Invocações em campo |
| G2-09 | Índice com rótulo de capítulo inexistente e verbetes faltando | remissão | rótulo corrigido (C05); verbetes pendentes | Consulta |
| G2-10 | "reserva" com dois sentidos | inconsistência | decisão de redação | Invocações em campo |
| G3-01 | "Restringido" não existe no livro | inconsistência | corrigido (C02) | Incursor |
| G3-02 | "Uma vez por turno seu" fora do turno | lacuna | decisão pequena | Incursor |
| G3-03 | Manejo de Combate com Maldição do Inventário | lacuna | decisão (somar ou não) | Equipamento |
| G3-04 | Fluidez e Passo Guardado antes do primeiro turno | lacuna | decisão pequena | Incursor |
| G3-05 | Instante Decisivo contra o Bloquear | lacuna | decisão pequena | Incursor |
| G3-06 | "Arma apropriada para arremesso" sem termo no Equipamento | remissão | decisão (qual termo) | Incursor |
| G3-07 | Ofensiva em Movimento com armas de fogo | decisão de regra | decidido e aplicado (D01): segundo ataque corpo a corpo ou arremesso | Incursor |
| G3-08 | Glossário: Leve sem a propriedade de arma | inconsistência | corrigido (C03) | Consulta |
| G4-01 | Besta com capacidade 1 contra a peça | decisão de regra | decidido: mantém 1, registrado em EQ25; a peça 14 muda na migração | Equipamento, peça 14 |
| G4-02 | Vanguarda usa um "X" que o Equipamento não define | inconsistência | corrigido (C06) | Vanguarda |
| G4-03 | Treino em arma específica não reconhecido | inconsistência | corrigido (C07) | Equipamento |
| G4-04 | Remissões para títulos inexistentes | remissão | corrigido (C08, C08b, C08c, C08d) | vários |
| G4-05 | "Grupos de armas" em vez de categorias | inconsistência | corrigido (C09) | Rotas |
| G4-06 | Armas de grau 4 da rota contra Equipamento inicial | lacuna | decisão | Equipamento, Rotas |
| G4-07 | Batedor: Arma de Fogo sem autorização na criação | lacuna | decisão | Vanguarda, Equipamento |
| G4-08 | Emanador registra "Integridade" de arma | inconsistência | corrigido (C01) | Emanador |
| G4-09 | Defesa de entidade com Revestimento soma Destreza | inconsistência | corrigido (C10) | Construir invocações |
| G4-10 | Carga de entidade sem talento de transporte | lacuna | lacuna (junto com G2-07) | Invocações em campo |
| G4-11 | Escolhas do Traje fora da criação e da ficha | lacuna | lacuna | Equipamento, Abertura, Consulta |
| G4-12 | Índice e glossário sem termos de equipamento | remissão | glossário corrigido (C03); verbetes do índice pendentes | Consulta |
| G4-13 | Volumosa e Embainhada fora da página de Propriedades | remissão | corrigido (C12) | Equipamento |
| G4-14 | "Rodada inteira" contra "Ação Completa" | inconsistência | corrigido (C04, C04b) | Regras gerais, Equipamento |
| G4-15 | Exemplo de Proteção com escudo que Rina não pode usar | inconsistência | corrigido (C11) | Equipamento |
| G5-01 | "Restrição Único" não existe | inconsistência | corrigido (C13) | Emanador |
| G5-02 | "Calo — Livre" com o nome antigo | inconsistência | decisão de nome | Fundamento, Rotas |
| G5-03 | Rotas remete a seções inexistentes | remissão | corrigido (C08c) | Rotas |
| G5-04 | Catálogo remete a títulos inexistentes | remissão | corrigido (C08e) | Catálogo |
| G5-05 | Teto de 4 × Classe "somando alvos" | inconsistência | decisão de redação: alinhar ao FU-27 | Construir invocações |
| G5-06 | Revisão ao subir de nível sem a Técnica Máxima | inconsistência | corrigido (C14) | Progressão |
| G5-07 | Lento sobre deslocamentos concedidos | lacuna | lacuna | Dano e recuperação (Condições) |
| G5-08 | Ritual sobre Técnica Máxima sem Classe | lacuna | decisão | Ritual e Pactos |
| G5-09 | Classe 0 com Toque ou Aura e a única Restrição Leve | lacuna | decisão | Fundamento |
| G5-10 | Emanador reaproveita nomes | decisão de regra | decisão de nome | Emanador |
| G5-11 | Índice sem Auge e Regra Própria | remissão | remissão: verbetes pendentes | Consulta |

## Por que alguns achados "claros" não foram corrigidos

O critério desta rodada foi corrigir sozinho só o que diverge de uma regra já aprovada em outro capítulo. Ficaram de fora:

- **G2-10** e **G5-05**: o texto é ambíguo, mas a correção é reescrever frases, e escolher a redação é do autor.
- **G5-02**: trocar o rótulo de Calo decide se ele ocupa espaço de Talento, o que é regra.
- **Verbetes novos no índice** (G2-09, G4-12, G5-11): é completude, e não divergência. Entram junto com a próxima rodada de Consulta.

## Situação do validador editorial

Os 13 capítulos que esta rodada mudou passam no `conferir_editorial.py` sem achado e no validador da própria unidade. Cinco deles (Incursor, Catálogo, Equipamento, Construir invocações e Regras gerais) já estavam vermelhos na `main`, com a revisão de localização feita sobre uma versão de antes do fechamento da integração. O diff dessa versão até a `main` é só redação de remissão, e foi relido junto com as correções. Consulta e Fabricação também estavam vermelhas na `main` e ganharam o cotejo das fontes que mudaram. Tudo com antes, depois e motivo em `CORRECOES-APLICADAS.md`.

Aptidões, Fundamento, Origens, Perícias e Poderes avançados continuavam vermelhos como na `main`, porque nenhuma correção passou por eles. Depois desta rodada, as provas deles foram atualizadas sem mudar o texto e os cinco saem verdes. Registro em `../publicacao-github/provas-cinco-capitulos-2026-10-04/LEIA-ME.md`.
