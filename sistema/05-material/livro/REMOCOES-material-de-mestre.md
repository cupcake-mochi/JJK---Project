# O que saiu do PDF, e por quê

**Decisão do Mizuki:** o Manual da Guilda é livro de jogador. Argumento de design e
arbitragem de mestre saem dele. Este arquivo é o registro do que foi removido, o motivo,
e **onde a funcionalidade ainda vai precisar existir** — porque nada aqui deixou de ser
verdade sobre o sistema, só deixou de morar neste livro.

Nenhum número mudou em nenhuma das operações abaixo.

---

## Regra: o que é livro de jogador

O filtro aplicado, caso a caso:

| fica | sai |
|---|---|
| o que o jogador **consulta para jogar o turno dele** | o que prova que o número está balanceado |
| o que a **mesa decide junta** (ligar uma regra opcional) | como o número foi derivado |
| o gate que o jogador precisa **passar** | a projeção de quando ele passa, por rota de investimento |
| o efeito de uma condição | quanto aquela condição custou em fatia |

---

## 1 · Movido, não removido

Duas coisas estavam na seção errada e são **regra de jogador**. Não saíram do livro:
mudaram de capítulo.

### Os quatro estágios de dano na alma
**Estava:** cap. 9 *Fundamento* → `Para o mestre` → `Integridade e dano na alma`
**Foi para:** cap. 4 *Dano, Condições e Cobertura* → `Os quatro estágios de dano na alma`

O que acontece com o personagem conforme a alma dele cai é regra que o jogador aplica na
própria ficha. Estava enterrado na seção do mestre, num capítulo que não é dono do assunto.

> **Isso conserta um ponteiro quebrado.** O cap. 1 já dizia *"os quatro estágios moram no
> capítulo de dano"* e o cap. 4 não tinha a tabela. O ponteiro agora resolve.

### A tabela de Rotina por nível
**Estava:** cap. 9 *Fundamento* → `Para o mestre` → `A curva`, como uma coluna
**Foi para:** cap. 13 *Invocações*, na seção que a consome

`Rotina` é o teto de dano de um invocador somado às invocações dele — regra de jogador. O
capítulo 13 mandava o leitor procurar *"a tabela de Rotina do Fundamento"*, que não existia
com esse nome, e o termo não era definido em lugar nenhum. Agora a tabela está onde é usada.

---

## 2 · Removido do livro

### `Para o mestre` — cap. 9 *Fundamento* · 1.426 palavras

A seção inteira, menos os dois pedaços movidos acima.

| subseção | o que era | onde precisa voltar a existir |
|---|---|---|
| `Aprovar` | checklist de 8 caixas para o mestre aprovar feitiço novo | **Livro do mestre.** É a ferramenta central de arbitragem — sem ela o mestre não tem procedimento para dizer sim ou não |
| `O que depende de você` | como preçar `Efeito Próprio`, `Restrição Própria`, `Condicional`, `Regra Própria` | **Livro do mestre.** Sem isso, as peças "Próprias" ficam sem régua e cada mesa inventa a sua |
| `Dizer não` | as quatro respostas que resolvem 10 em 10 recusas | **Livro do mestre** |
| `Vida e letalidade` | vida de referência por nível e rodadas para cair sob foco | **Livro do mestre.** É régua de preparo de encontro |
| `Inimigos` | vida e dano de chefe e capanga, do nível 5 ao 30 | **Livro do mestre.** É a tabela mais usada na preparação de sessão |
| `PvP` | o corte de um terço no dano de feitiço em duelo | **Livro do mestre**, ou regra opcional no apêndice. É regra de verdade, não argumento |
| `A curva` | dano por faixa de nível, comparando Rotina, feitiço, Liberação e Técnica Máxima | **Repo-fonte.** É prova de balanceamento |

> ⚠ **`PvP` é o único item desta lista que é regra aplicável, não arbitragem.** Se a guilda
> joga PvP, ela precisa desse número em algum lugar. Decidir se ele volta como apêndice
> opcional (junto do `Bloquear`) ou se vai para o livro do mestre.

### `O orçamento` — cap. 11 *Equipamento* · 310 palavras

Como as 52 armas foram preçadas: o fundo de pontos por tipo, a escada de custo do dado, o
que cada propriedade custa, e a tabela de até onde o dado pode subir por número de
propriedades.

**Por que saiu:** o jogador escolhe do catálogo, ele não monta arma. A conta que prova que a
Katana fecha em 3 de 3 não muda nada no que ele rola.

**Onde precisa voltar:** **livro do mestre**, ou apêndice de homebrew. É a ferramenta de quem
for criar arma nova, e o próprio texto dizia *"se você for montar uma arma nova"*.

### Coluna `gasta` — cap. 11 *Equipamento* · 13 tabelas, 52 armas

Cada linha do catálogo trazia `3/3` ou `5/5`: quanto a arma gastou do orçamento dela.

**Por que saiu:** é o recibo da conta acima. Toda arma fecha exata por construção, então a
coluna diz a mesma coisa em todas as 52 linhas. Para o jogador é ruído numa tabela que ele
lê no meio da mesa.

**As 52 armas continuam todas lá**, com nome, mão, dado, propriedades e requisito de Força.

### Projeção de gates — cap. 10 *Aptidões e Refino* · ~180 palavras

A tabela de em que nível cada gate de refino abre para quem sempre investe, para quem
investe metade das vezes, e para quem nunca investe. Mais dois parágrafos justificando por
que o gate de Origem e o gate de outra aptidão são legais.

**Por que saiu:** é planejamento de curva, não requisito. **A tabela de formatos de gate
ficou** — ela é o que o jogador precisa para saber o que cada aptidão exige.

**Onde precisa voltar:** **repo-fonte**, como argumento de por que os gates estão onde estão.

### `Onde as três rotas puras chegam no nível 30` — cap. 14 · 123 palavras

Comparativo de atributo, refino, aptidões, Passivas e feitiços das três rotas de marco.

**Por que saiu:** é prova de que as três escolhas de marco são competitivas entre si — questão
de design, não de jogo. **O aviso que importa ficou:** *"quem nunca escolhe Refino termina a
campanha com zero aptidões"*, que é o que o jogador precisa saber antes de decidir.

### `Por que dois dados, e por que o −11` — cap. 15 · 183 palavras

A derivação de por que o `Bloquear` usa `2d10` e não `d20`, e de onde sai o `−11`.

**Por que saiu:** derivação matemática. **Ficou:** a regra, a seção
`Você não faz essa conta na mesa` (que é como a ficha imprime a linha), o exemplo, `O que ela
custa` com a tabela de probabilidade, e as duas travas. A mesa decide se liga a regra opcional
lendo o custo, não a derivação.

---

## 3 · Escrito novo: o que cada Caminho dá

Isto não é remoção, é o buraco que a remoção deixou visível.

**O problema:** os cinco Caminhos não declaravam nada do que concedem. Perícias fixas
estavam só no cap. 3, quantidade de ofício e Teste de Resistência só no cap. 6, e treino de
arma em lugar nenhum. Quem abria o Caminho para escolher o seu não conseguia saber o que
ele entrega.

**O que foi escrito:** um bloco `O que o <Caminho> dá` em cada um dos cinco, com vida por
nível, PE por nível, atributos naturais, perícias fixas, quantas perícias livres, quantos
ofícios, quantos Testes de Resistência, e o treino de arma.

### ⚠ O treino de arma por Caminho era um buraco de verdade

O cap. 11 afirmava *"cada Caminho concede os treinos dele"*, e **a tabela que diz quais nunca
existiu** — nem neste livro, nem em `sistema/03-mecanica/06-caminhos-e-trilhas.md`, nem em
`sistema/03-mecanica/14-equipamento.md` do repositório de trabalho. Os dois
arquivos-fonte estabelecem só o princípio: *"a Trilha de corpo a corpo de um Caminho
não-marcial concede o treino marcial"*.

**A regra foi ditada pelo Mizuki nesta revisão, e é decisão dele:**

| Caminho | treina |
|---|---|
| **Bastião** · **Vanguarda** | as treze categorias. Qualquer arma do catálogo |
| **Guia** · **Emanador** · **Evocador** | Arma de Fogo e Balestra, as duas que não pedem treino de verdade |

Para um conjurador empunhar o resto, a porta é a Trilha — como a `Empunhadura` do `Arremate`
(nível 2), que concede um grupo de arma e troca Força por Inteligência ou Essência nele.

> **Isto precisa voltar para o repositório de trabalho**, em
> `sistema/03-mecanica/06-caminhos-e-trilhas.md` ou `sistema/03-mecanica/14-equipamento.md`,
> e ganhar validador. Hoje ele existe só no PDF, que é artefato.

> **Duas inferências minhas, confira antes de fechar:**
> **1.** Pus o **Guia** no lado conjurador. Ele é 5 de vida e 5 de PE, "meio a meio", e nenhuma
> das três Trilhas dele (`Elo`, `Sutura`, `Perímetro`) tem conteúdo de arma — por isso caiu
> desse lado. Se ele devia treinar como corpo a corpo, é uma linha para trocar.
> **2.** Li *"todas as armas"* como incluindo **Arma de Fogo** para Bastião e Vanguarda. Isso
> faz a rota `Arma de Fogo` do `Batedor` virar especialização pura, e não acesso — o que é
> coerente com o texto dela, que só entrega `Ferrolho` e `Mirar`, nunca treino.

---

## 3b · Segunda passada: moeda de orçamento e tabelas-prévia

### As colunas `custa` e `devolve` — cap. 11 *Equipamento*

A tabela das doze propriedades tinha uma coluna `custa` (`Alcance` custa 1, `Versátil` custa 0)
e a das três restrições tinha `devolve`. **São a mesma moeda do orçamento que já tinha saído** —
ficaram órfãs na primeira passada.

**Por que saiu:** sem o orçamento, o jogador não tem onde gastar esse ponto. A propriedade já
vem impressa na linha da arma e ele nunca escolhe uma.

**Onde precisa voltar:** junto do `O orçamento`, no **livro do mestre** ou apêndice de homebrew.
As três peças (fundo por tipo, escada de dado, preço de propriedade) só funcionam juntas.

### 19 tabelas-prévia — cap. 8 *Caminhos e Trilhas*

Cada Caminho e cada Trilha abria com `| Nível | Degrau | Em uma linha |`, e logo abaixo vinha o
texto completo das mesmas entregas, já rotulado por nível.

**Por que saiu:** as três colunas repetiam o que estava cinco linhas abaixo. O nível está no
texto (*"Nível 2: `Corpo Duro`"*), o nome está no texto, e a glosa de uma linha é um resumo do
parágrafo seguinte.

**Nada foi perdido:** os 19 blocos de regra continuam inteiros, e o parágrafo em itálico que
fecha cada Caminho continua fazendo o trabalho de *"o que isso significa na mesa"*.

> **O critério aplicado, para reusar depois:** **tabela-prévia sai, tabela de contraste fica.**
> Prévia é quando todas as colunas repetem o texto adjacente. Contraste é quando a tabela põe
> os itens num eixo que a prosa não alcança — como as quatro anti-domínio do cap. 10
> (*protege / e cobra / PE por rodada*) ou os `Estigma` do cap. 12 (*quando age / relógio*).
> Essas ficaram.

Varredura no resto do livro: **nenhuma outra tabela-prévia**, e **nenhuma tabela duplicada**.
Sobraram 4 tabelas de duas linhas, todas contraste de dois itens. O livro foi de 240 para
**221 tabelas**.

---

## 4 · Contas

| capítulo | antes | depois | delta |
|---|---|---|---|
| 9 · Fundamento | 16.723 | 15.297 | −1.426 |
| 11 · Equipamento | 5.953 | 5.492 | −461 |
| 10 · Aptidões e Refino | 5.474 | 5.296 | −178 |
| 14 · Experiência e Progressão | 3.389 | 3.266 | −123 |
| 15 · Apêndice · Bloquear | 907 | 724 | −183 |
| 4 · Dano, Condições e Cobertura | 2.349 | +tabela de estágios | — |
| 8 · Caminhos e Trilhas | 10.187 | +5 blocos +treino | — |
| 13 · Invocações | 3.431 | +tabela de Rotina | — |

**Saíram ~2.400 palavras de material de mestre e argumento de design.**
**Entraram ~600 palavras de regra que faltava ou estava no lugar errado.**

---

## 5 · Antes de commitar

- [ ] Conferir as duas inferências sobre treino de arma (Guia, e Arma de Fogo para os marciais)
- [ ] Decidir onde o `PvP` vai morar — apêndice opcional ou livro do mestre
- [ ] Levar a regra de treino de arma por Caminho para o repo-fonte, com validador
- [ ] O `Para o mestre` do cap. 9 está preservado em `sistema/03-mecanica/11-aptidoes-e-refino.md`
      e `manual/Fundamento-MANUAL-v7.docx` do repositório de trabalho — conferir antes de considerar perdido
- [ ] As correções da rodada anterior (regra 5 das Regras de ouro ganhando *"Classe 3 ou
      mais"*, e a tabela de Classe Passiva 3 do cap. 10 que contradizia o cap. 9) são bugs do
      repo-fonte e valem voltar para lá
