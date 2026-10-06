# O que falta no R28a

O R28a foi gerado antes de duas decisões: a **D43** (Condição, Prende e Cerca pedem TR mesmo num ataque) e a **D44** (a Execução Preparada passa de −1 para −2). As duas já estão na candidata (`planejamento-editorial/consolidacao/lote-01/LIVRO-COMPLETO.md`), que é de onde as peças e os validadores leem.

A lista saiu do diff da candidata nos commits `65afa3c` (D43) e `9f622a5` (D44). Cada trecho antigo foi procurado no texto do R28a, e as páginas são as do PDF. Em página de duas colunas, o parágrafo pode estar quebrado entre elas.

São 14 trechos em 9 páginas: um só da D44 e treze da D43, dos quais dois são parágrafos novos e não substituem nada.

## D44: um trecho

**p. 125, Vanguarda, nível 7.** Só o número muda.

- Antes: *imponha **−1** a um TR adicional da Conclusão.*
- Depois: *imponha **−2** a um TR adicional da Conclusão.*

## D43: treze trechos

### Regras gerais

**p. 59, Condições → Aplicação e duração.** Entra uma frase depois da primeira.

- Antes: *A habilidade informa como aplica a condição: por acerto, falha em TR ou outro gatilho. **Use a duração escrita no efeito.** (…)*
- Depois: *A habilidade informa como aplica a condição: por acerto, falha em TR ou outro gatilho. A Melhoria Condição sempre pede TR: num feitiço de ataque, o alvo acertado ainda faz o TR registrado e só recebe a condição se falhar. **Use a duração escrita no efeito.** (…)*

O resto do parágrafo não muda.

### O exemplo da Kaori

**p. 83, Peso nas Mãos, a ficha.**

- Antes: *(…) No acerto, causa **3d8 de Concussão** e aplica **Derrubado por uma rodada**. No erro, o PE e a ação continuam gastos.*
- Depois: *(…) No acerto, causa **3d8 de Concussão**, e o alvo faz **TR Físico contra CD 12**. Na falha, fica **Derrubado por uma rodada**. No erro, o PE e a ação continuam gastos.*

**p. 83, a conta logo abaixo.**

- Antes: *(…) e paga 1 por Condição: Derrubado. Sobram 3 dados. (…)*
- Depois: *(…) e paga 1 por Condição: Derrubado, com TR Físico registrado para ela. Sobram 3 dados. (…)*

**p. 85, fim do exemplo de combate.**

- Antes: *(…) Se a criatura sobrevivesse ao acerto, seria necessário aplicar Derrubado e sua duração. As decisões seguintes (…)*
- Depois: *(…) Se a criatura sobrevivesse ao acerto, faria o TR Físico contra CD 12 e, na falha, ficaria Derrubada por uma rodada. As decisões seguintes (…)*

### Fundamento

**p. 309, parágrafo novo.** Entra entre *"Num feitiço ofensivo resolvido por TR, falhar aplica dano (…) continua existindo mesmo depois da falha inicial."* e *"Na criação, você pode trocar ataque por TR, ou o contrário (…)"*:

> Num feitiço de ataque, o acerto não basta para Condição, Prende e Cerca: o alvo acertado faz o TR registrado para o Controle e só recebe essas peças se falhar. Veja Controle, no Catálogo.

**p. 312, tabela de objetivos de controle.** Muda a terceira coluna de duas linhas.

| Objetivo | Antes | Depois |
|---|---|---|
| Segurar uma criatura no lugar. | O alvo pode gastar uma ação permitida pela peça para tentar escapar. | **Entra na falha do TR, mesmo num ataque.** O alvo pode gastar uma ação permitida pela peça para tentar escapar. |
| Aplicar uma condição. | No máximo uma Pesada. Se for Pesada, o alvo repete TR no fim dos turnos para encerrá-la. | **Entra na falha do TR, mesmo num ataque.** No máximo uma Pesada. Se for Pesada, o alvo repete TR no fim dos turnos para encerrá-la. |

### Catálogo, Controle

**p. 334, parágrafo novo.** Entra logo abaixo do título **Controle** e antes de **Condição**:

> **Condição, Prende e Cerca sempre pedem TR.** Numa ficha resolvida por TR, entram na falha desse TR. Numa ficha de ataque, o acerto aplica o dano e as outras peças; depois, cada alvo acertado faz o TR registrado na ficha para o Controle e só recebe essas peças se falhar. Um TR por alvo resolve as três peças da mesma ficha. O erro não pede TR.

**p. 334, Condição, primeiro parágrafo.**

- Antes: *(…) Ela se aplica no acerto ou na falha do TR, dura **uma rodada** (…)*
- Depois: *(…) Ela se aplica **na falha do TR**, mesmo numa ficha de ataque, dura **uma rodada** (…)*

**p. 334, Condição, segundo parágrafo.** Sai um pedaço.

- Antes: *(…) encerrando aquela aplicação no sucesso, mesmo que tenha sido aplicada por ataque. Leves e Médias (…)*
- Depois: *(…) encerrando aquela aplicação no sucesso. Leves e Médias (…)*

**p. 334, Cerca.**

- Antes: ***Preço: Leve.** No acerto ou na falha do TR, o alvo não pode (…)*
- Depois: ***Preço: Leve.** Na falha do TR, mesmo numa ficha de ataque, o alvo não pode (…)*

**p. 335, Prende.**

- Antes: ***Preço: Média.** No acerto ou na falha do TR, o alvo não pode se deslocar (…)*
- Depois: ***Preço: Média.** Na falha do TR, mesmo numa ficha de ataque, o alvo não pode se deslocar (…)*

### O exemplo do Iori

**p. 380, a ficha.**

- Antes: *(…) No acerto, cause **3d8 de Cortante** e aplique Prende até o fim do próximo turno do alvo. Para as tentativas de saída, registre **TR Físico contra sua CD da Kata**.*
- Depois: *(…) No acerto, cause **3d8 de Cortante**, e o alvo faz **TR Físico contra sua CD da Kata**. Na falha, Prende vale até o fim do próximo turno dele. As tentativas de saída usam o mesmo TR.*

**p. 380, o parágrafo seguinte.**

- Antes: *(…) a CD é **12**. Prende permite gastar Padrão, Bônus ou Movimento para tentar o TR de saída, conforme o Catálogo.*
- Depois: *(…) a CD é **12**. O acerto sozinho não prende: Prende entra na falha do TR. Depois, permite gastar Padrão, Bônus ou Movimento para tentar o TR de saída, conforme o Catálogo.*

## Depois de gerar

Se os dois parágrafos novos empurrarem texto, as páginas seguintes mudam, e o sumário e o índice também. Me manda o PDF novo que eu refaço a conferência parágrafo por parágrafo contra a candidata. Se bater, ele substitui o `Ciclo-Maldito-Livro-de-Regras.pdf` e o aviso sai do README.

## Projetar Energia: decisão do Mizuki de 06/10/2026 (v0.340)

O R28a e a candidata dizem **`1d6` de Força por PE, de `1` PE até o refino inteiro**. O Mizuki decidiu outra coisa para o livro: **de `1` PE até metade do refino (para baixo, mínimo `1`), com `2d6` de Força por PE.** O resto da entrada fica como está (Ação Padrão, ataque de conjuração, alcance de `18 m` e `36 m`, sem Canalizar nem Kokusen). Quem corrige é a candidata (`sistema/05-material/livro/planejamento-editorial/aptidoes/lote-01/APTIDOES-E-REFINO.md`, a seção Projetar Energia e o exemplo da Mei) e, depois dela, o gerador do R28a.

**O que muda no texto:** a entrada Projetar Energia e o exemplo da Mei, que escolhia de `1` a `6` PE com Refino 6 e agora escolhe de `1` a `3`.
