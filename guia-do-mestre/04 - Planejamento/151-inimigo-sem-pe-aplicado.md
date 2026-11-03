# Inimigo sem PE aplicado ao Guia

Registro 151, 02/11/2026. Aplica a decisão do autor registrada no [150](<150-resultados-da-avaliacao-dos-encontros.md>): inimigos não contam PE. A proposta foi aprovada como está em 02/11. Ela usava o vocabulário da peça 26 §6.1 e a decisão de 09/09/2026 (`bestiario/04-fase-1/decisoes-fase-1.md` §8).

As fontes da edição 136 foram alteradas. O PDF e o HTML ainda são os do registro 147.

## A regra

Cada capacidade de inimigo leva um **rótulo de frequência**:

- **à vontade**, sem rótulo;
- **1× por rodada**;
- **1× por luta**;
- **Recarga (5–6)**: começa disponível; depois do uso, rola um d6 no começo de cada turno da criatura e recupera com 5 ou 6.

Para traduzir uma ficha, mantenha o número de usos grandes que a reserva permitia e escolha o rótulo mais próximo. Ao trazer um feitiço publicado, conserve efeito, Forma, Selo e requisitos e troque o preço em PE pelo rótulo.

**Os três pontos que dependiam de PE:**

1. **Estágio 2 de Integridade.** O acréscimo de 1 PE por Classe não tem efeito numa ficha sem PE. As demais penalidades continuam valendo, e os rótulos não mudam.
2. **Leitura de Reservas** contra inimigo informa "sem reserva gastável" (0/0 PE) e não revela rótulos.
3. **Doma.** A domada com técnica começa com a reserva própria vazia e a enche nos descansos. A divisão de custo entre invocador e domada não muda, porque é regra de entidade.

## Fichas

| Ficha | Antes | Agora |
|---|---|---|
| Amontoado | 6 PE; Impacto 3 PE | Impacto **Recarga (5–6)** |
| Vigia das farpas | 6 PE; Estalo 3 PE | Estalo **Recarga (5–6)** |
| Toru | 8 PE | Fenda **Recarga (5–6)**; Cobrir-se **1× por luta** |
| Sayo | 12 PE | Fio **à vontade**; Remendo **1× por luta**; Cobrir-se **1× por luta** |
| Daigo (Haru) | 26 PE | Fita Classe 4 **1× por luta**; Classe 2 **à vontade**, com aviso e intervalo; Cobrir-se **1× por luta** |
| Vigia do arquivo | 14 PE | Cobrir-se **1× por rodada** |
| Tessa | 26 PE | Remendo firme **1× por luta**; Orientar **à vontade**; Cobrir-se **1× por luta** |
| Rastejante, Carregador, Sineiro | 0 PE | sem mudança |

**Desvio da proposta: o Vigia do arquivo.** A proposta dava Cobrir-se 1× por luta a todos. O Vigia é um protetor dedicado e, com 14 PE, pagava até 7 Cobrir-se. Um uso por luta tiraria a função dele. Ficou **1× por rodada**.

## Arquivos alterados

Na edição 136:
- **Capítulo 1**: o Amontoado ganha o bloco da Recarga; na rodada 2 a recarga sai 5; a tabela final diz "sem reserva".
- **Capítulo 6**: seção 6.3 reescrita, com o título mantido para não quebrar links; campo da ficha; linha de Toru.
- **Casos**: 14, 52, 57, 59 (reescrito como "Rótulos, recarga e preparação"), 60, 74, 75, 76, 77, 100, 101, 102 e 104.
- **Consultas**: 58, campo de recursos iniciais; 61, pergunta sobre Integridade.
- **Índice de casos**: título do 59.

Ainda nesta pasta:
- banners em `LEIA-ME`, `01` e `98`;
- nota no `README`;
- remissão no 150.

## Números refeitos

Tudo está em `apoio-encontros-149`.

- **Caso 57** (`c57_recarga.py`):
  - trio cheio: queda de 20,36% para **14,36%**, Derrotado **0,22%**;
  - trio com metade da vida e 2 Sequelas: queda de 60,50% para **54,12%**, Derrotado de 24,40% para **17,70%**.
- **Caso 76** (`c76_quem_atacar.py`, conta exata): Toru usa Cobrir-se uma vez só e termina com 56 e depois 43 PV (antes 59 e 46). A chance de derrubar Toru vai de 4,5% para **5,5%**. Sayo continua em 23,9%.
- **Caso 102** (`c102_dupla.py`, 1 milhão de lutas por linha, semente 102): só muda a coluna de 3 mistos com cura, de 11,8% para **11,4%**. A reconstrução dá 11,9% para a versão antiga, dentro do arredondamento; as outras colunas reproduzem o caso.
- **Caso 104** (`c104_recarga.py`, mesmas sementes de `casos.py`, recurso `recarga56`):
  - quedas com vida cheia de 21% para **15%**;
  - escolher o mais ferido, de 48% para **42%**, quase o triplo da linha base;
  - socorro a 2 turnos, de 11%/25% para **8%/20%**;
  - a ordem do que mais pesa não mudou.

O bloco C12 (grade da peça 26) não usa o Amontoado e fica igual.

## Limites

- Os rótulos de Toru, Sayo, Daigo, Vigia e Tessa são experimentais e não passaram por mesa.
- Os modelos de simulação têm as mesmas limitações listadas no 150.
