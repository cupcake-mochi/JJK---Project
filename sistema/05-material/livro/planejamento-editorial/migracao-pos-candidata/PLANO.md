# Plano de migração da candidata para as peças, validadores, geradores e fichas

Item 4 da fila pós-reconstrução, escrito em 04/10/2026. **Nada foi migrado.** Nenhuma peça de `sistema/03-mecanica`, nenhum validador, gerador ou ficha foi alterado por este plano.

## Quando começar

A migração só começa depois de duas coisas, nesta ordem:

1. **A candidata estabilizar.** Os achados da revisão de interfaces (`../revisao-interfaces/ACHADOS.md`) que pedem decisão do autor precisam estar respondidos, e o teste com leitores e jogadores (`../testes-com-leitores/`) precisa ter rodado pelo menos a primeira leva nos quatro grupos prioritários. Mudança que sair da mesa entra na candidata antes de entrar nas peças, senão a migração é feita duas vezes.
2. **O Mizuki decidir a publicação.** Hoje a candidata é separada da edição v0.331 distribuída aos jogadores. Migrar as peças antes dessa decisão faria as peças, que são a fonte dos validadores, descreverem uma regra que o livro distribuído não tem.

Se a decisão for não publicar a candidata inteira, este plano vale por unidade: migra-se só o que for aprovado, e o resto fica registrado como candidata.

## O tamanho do trabalho

Os 23 arquivos `ALTERACOES.json` das unidades somam **774 registros** de antes, depois e motivo. A triagem automática pelo campo de tipo de cada registro dá:

| Classe (triagem automática) | Registros |
|---|---:|
| Mecânica | 283 |
| Interface ou correção | 205 |
| Editorial | 177 |
| Preservação | 63 |
| Esclarecimento | 46 |

A triagem lê o rótulo que cada unidade usou, e as unidades usaram rótulos diferentes (`M`, `mecânica de fechamento`, `Esclarecimento com impacto mecânico`...). Ela serve para dimensionar e ordenar, **não confirma nada**. A própria `REVISAO-FINAL.md` avisa que esses registros incluem decisões editoriais e correções de interface e não devem ser contados como regras novas.

Registro por registro, com a classe e os donos prováveis na v0.331: `INVENTARIO-ALTERACOES.json`.

| Unidade | Registros | Mecânica (triagem) | Donos prováveis na v0.331 |
|---|---:|---:|---|
| Catálogo | 118 | 46 | peça 17, manual do Fundamento v7, `livro/manual/40` |
| Fundamento | 56 | 28 | peça 17, manual do Fundamento v7, `livro/manual/40` |
| Ritual e Pactos | 32 | 28 | peças 27 e 22, `livro/manual/46` e `65` |
| Poderes avançados | 33 | 20 | peça 11, rascunho da expansão sem barreira |
| Invocações em campo | 49 | 20 | peça 15, `invocacoes/`, `livro/manual/60` |
| Regras gerais | 38 | 18 | peças 01, 03, 04, 05 e 23 |
| Emanador | 29 | 18 | peça 06, `livro/manual/35` |
| Bastião | 26 | 14 | peças 06, 05 e 23 |
| Dano e recuperação | 32 | 13 | peça 01 §5.5, peças 19, 24 e 10 |
| Progressão | 36 | 13 | peças 12 e 18 |
| Aptidões e Refino | 32 | 13 | peça 11 |
| Rotas | 32 | 10 | peças 20 e 25 |
| Origens | 35 | 9 | peças 09 e 13 |
| Demais 10 unidades | 226 | 33 | ver o inventário |

A coluna de donos é um mapa por unidade, a confirmar entrada por entrada. Os Caminhos de Evocador e Incursor, por exemplo, nunca tiveram peça própria: na v0.331 eles moram no `livro/manual/35-caminhos-e-trilhas.md` e no `RASCUNHO-trilhas.md`.

## Divergências já confirmadas

Conferidas em 04/10/2026, lendo os arquivos. Cada linha diz onde a v0.331 ainda tem a forma antiga. "Ficha" é o retrato do repositório `Ficha---RPG-JJK` no GitHub, commit `8e4cc75` de 03/10/2026 (ver a seção das fichas).

### Vida a zero

A peça 01 §5.5 descreve o Aguentar com cura de 20% **de uma vez**, o Insistir acordando só com **metade da vida máxima original** (somando curas), um teto de dano acumulado a zero em metade da máxima, e cura própria sem Sequela. A candidata usa a mesma janela para as duas escolhas (3 rodadas menos as Sequelas), tratamento acumulado de 20% para as duas, cada dano à vida consumindo uma rodada, Sequela em toda saída da queda e Derrotado como estado próprio.

- Peças com Aguentar/Insistir: 01, 12, 15, 24 (Insistir também na 20).
- Validadores: `conferir-atributos.py`, `conferir-invocacoes.py`.
- Livro v0.331: `08-inicio-rapido`, `10-como-jogar`, `60-invocacoes` (Insistir também em `42-tecnica-marcial`).
- Ficha: "capitulo-16-invocacoes.md", "manual.txt"; Insistir também em "apps-script/Ficha.gs" e "ficha-v01/tecnica-do-livro.json".

### Nomes

| Antes | Candidata | Peças | Validadores | Geradores | Ficha (arquivos) |
|---|---|---|---|---|---|
| Incapacitado | Guarda Aberta | 01, 06, 11, 13, 19, 23 | `conferir-atributos`, `conferir-bloquear`, `conferir-dano` | `manual/gerador/partD.js` | 7, entre eles "catalogo-projeto-m.json" e "apps-script/Ficha.gs" |
| Classe Passiva (CP) | Categoria de Efeito (CE) | 03, 09, 11, 13, 16, 20, 25, `RASCUNHO-trilhas` | `conferir-aptidoes`, `conferir-expansao`, `conferir-manual`, `conferir-marcial`, `conferir-sem-tecnica` | nenhum | 13, entre eles "apps-script/Ficha.gs" e "ficha-v01/tecnica-do-livro.json" |
| Passiva Livre | Expressão da técnica | 08, 18, 20, 25 | `conferir-manual`, `custo-sem-barreira`, `v7.py` | `manual/gerador/partB.js` e `partE.js`, `gerador-ficha/ficha.js` | 15 |
| Aviso (duas entradas) | Identificar Feitiço e Leitura de Feitiços | 2 peças | nenhum | 2 arquivos do gerador do `.docx` | 15 |

Nenhum dos nomes novos aparece em peça, validador, gerador ou ficha. A troca de nome é a parte mais mecânica da migração e a que mais quebra coisa ao mesmo tempo: o `conferir-nomes.py` e o `conferir-manual.py` leem o `.docx`, e a ficha usa os nomes como chave de catálogo.

### Fluidez, Malabarista, munição e Volume

`Fluidez` aparece 88 vezes na candidata e em nenhuma peça nem validador. `Munição` aparece 27 vezes na candidata, em uma peça e em nenhum validador. `Volume` aparece 80 vezes na candidata, em duas peças e dois validadores. Isso não prova divergência de regra, só onde a regra **não tem conferência automática** hoje. Cada uma precisa de leitura lado a lado antes de virar tarefa.

### Edição distribuída

O repositório de entrega `JJK---PDF---RPG` está no recorte da **v0.330** (commit `36d4f15`, 30/09/2026), com o Manual da Guilda em 18 capítulos. A candidata tem 21. Isso é informação para a decisão de publicação, não tarefa desta migração.

### Decisões do autor de 04/10/2026

Quatro achados da revisão de interfaces foram decididos pelo Mizuki e aplicados na candidata (`../revisao-interfaces/CORRECOES-APLICADAS.md`, registros D01 a D03c e EQ25). A migração leva as quatro:

| Decisão | Na candidata | Onde a v0.331 diverge |
|---|---|---|
| Besta comporta um virote (capacidade 1); não funcionar com o ataque extra é a desvantagem dela | EQ25, sem mudar o texto | peça 14, tabela de capacidade, que dá 2 às bestas e proíbe 1. O Combate Irregular da Vanguarda passou a aumentar só Arma de Fogo (D04), então a besta fica em 1 também nele |
| Ofensiva em Movimento: o segundo ataque é corpo a corpo ou arremesso | INC-22 | `livro/manual/35-caminhos-e-trilhas.md`, Ofensiva em Movimento |
| A entidade ataca com a básica ofensiva de Classe 0 ou com uma arma empunhada; com arma, o atributo da arma no acerto, a CD sem mudar e desvantagem por falta de treino | R11-50, R12-32 | a peça 15 já registra a mesma regra da arma (decisão (a) e fechamento da v0.258); conferir só a redação |
| Corpo excedente volta sozinho quando a vaga se abre por perda ou por aumento do total; soltar um corpo de propósito não traz outro | R11-51, PRO37, FAB-REV-01 | o total de corpos mantidos não existe na v0.331; entra junto com o resto de Invocações |

Essas entradas foram acrescentadas aos `ALTERACOES.json` das unidades depois do inventário. O `INVENTARIO-ALTERACOES.json` continua contando os 774 registros de 03/10.

## Ordem proposta

Cada passo fecha com a bateria inteira verde (os 27 validadores de `03-mecanica`, `pac7.py`, `v7.py` e o `conferir-repositorio.py`, com `PULADA=0` conferido) e uma entrada no CHANGELOG. Um passo por versão, para a bateria apontar o culpado quando quebrar.

1. **Confirmar cada registro mecânico.** Ler o "depois" do inventário contra a peça dona e marcar `confirmada`, `ja_na_peca` ou `so_editorial` no `estado_migracao`. Começar pelas unidades com mais registros mecânicos (Catálogo, Fundamento, Ritual). Sem esse passo, a migração copia uma suposição.
2. **Nomes.** Trocar os quatro nomes nas peças, nos validadores e nos geradores, deixando os nomes antigos como alias no `conferir-nomes.py`, para a triagem continuar pegando quem reusar. Validador que procura o nome antigo no `.docx` precisa decidir junto se o `.docx` v7 ainda é fonte, porque ele não tem os nomes novos.
3. **Vida a zero.** Reescrever a peça 01 §5.5 a partir do capítulo de dano da candidata, e as remissões das peças 12, 15, 20 e 24. Antes, rodar o `conferir-atributos.py` numa cópia com a regra nova para ver quais checagens medem a regra antiga, e trocá-las por checagens da regra nova com teste negativo. Não apagar checagem para passar.
4. **Equipamento e munição** (peças 14, 16, 21), depois **Invocações** (peça 15, que conversa com `invocacoes/`), depois **Caminhos** (peça 06 e `RASCUNHO-trilhas`, que hoje não têm Fluidez nem Malabarista).
5. **Criação, Fundamento e Catálogo** (peças 08, 17, 18). É o maior volume e o que mais toca a ficha.
6. **Geradores.** `manual/gerador` (o `.docx` do Fundamento v7), `gerador-ficha` e `gerador-inimigo`. O gerador do livro antigo (`livro/build/`) só muda se a candidata não substituir o `livro/manual/`.
7. **Fichas**, por último e em outro ambiente (seção abaixo).

## Fichas pessoal e maldita

**O estado delas precisa ser consultado no ambiente onde elas estão sendo feitas.** São trabalho paralelo do Claude, com conversa e pacote próprios. Este plano não supõe que a reconstrução do livro as atualizou, e não supõe o contrário de nada que não foi visto.

O que foi visto aqui é só o retrato do GitHub: o repositório `Ficha---RPG-JJK`, commit `8e4cc75` de 03/10/2026, com a `FICHA`, a `FICHA AMALDIÇOADA` e a `FICHA PESSOAL` na planilha `ficha-v01`. Nesse retrato:

- nenhum arquivo usa Guarda Aberta, Categoria de Efeito ou Expressão da técnica;
- `Classe Passiva`, `Passiva Livre` e `Incapacitado` aparecem em 13, 15 e 7 arquivos, inclusive no "apps-script/Ficha.gs" e no catálogo;
- o próprio "PENDENCIAS.md" registra no B33 que o catálogo e o "manual.txt" estão na v0.263, atrás do sistema.

Antes de mexer na ficha, quem estiver no ambiente dela confirma o estado de lá (pode haver trabalho que não subiu), recebe a lista de divergências confirmadas e decide se a ficha acompanha a candidata ou a publicação distribuída.

## O que este plano não cobre

Ilustrações, acabamento artístico e repaginação ficam fora, por decisão do Mizuki. A migração também não decide a publicação, não toca a edição distribuída e não muda a candidata.
