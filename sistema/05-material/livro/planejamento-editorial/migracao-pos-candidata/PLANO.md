# Plano de migração da candidata para as peças, validadores, geradores e fichas

Item 4 da fila pós-reconstrução, escrito em 04/10/2026. **Nada foi migrado.** Nenhuma peça de `sistema/03-mecanica`, nenhum validador, gerador ou ficha foi alterado por este plano.

## Quando começar

**Decisão de 05/10/2026: migrar.** O Mizuki autorizou a migração (*"e... podemos migrar"*) depois de fechar a revisão de interfaces e a sexta passada, sem esperar o teste com leitores. As duas condições abaixo ficam como o desenho original do plano; a primeira foi dispensada por ele, e a segunda é esta decisão. O que sair do teste com leitores, quando ele rodar, entra como mudança nova, pela candidata e depois pelas peças.

A migração só começa depois de duas coisas, nesta ordem:

1. **A candidata estabilizar.** Os achados da revisão de interfaces (`../revisao-interfaces/ACHADOS.md`) que pedem decisão do autor precisam estar respondidos, e o teste com leitores e jogadores (`../testes-com-leitores/`) precisa ter rodado pelo menos a primeira leva nos quatro grupos prioritários. Mudança que sair da mesa entra na candidata antes de entrar nas peças, senão a migração é feita duas vezes.
2. **O Mizuki decidir a publicação.** Hoje a candidata é separada da edição v0.331 distribuída aos jogadores. Migrar as peças antes dessa decisão faria as peças, que são a fonte dos validadores, descreverem uma regra que o livro distribuído não tem.

Se a decisão for não publicar a candidata inteira, este plano vale por unidade: migra-se só o que for aprovado, e o resto fica registrado como candidata.

## O tamanho do trabalho

Os 23 arquivos `ALTERACOES.json` das unidades somam **824 registros** de antes, depois e motivo (eram 774 em 04/10/2026; as passadas de decisão do autor acrescentaram 50, e o inventário foi refeito em 05/10/2026). A triagem automática pelo campo de tipo de cada registro dá:

| Classe (triagem automática) | Registros |
|---|---:|
| Mecânica | 291 |
| Interface ou correção | 207 |
| Editorial | 187 |
| Preservação | 63 |
| Esclarecimento | 46 |
| Decisão do autor | 30 |

*"Decisão do autor" é o rótulo das passadas de 04/10 e 05/10 sem a marca `M`. Quais delas mudam regra está nas tabelas de cada passada, abaixo.*

A triagem lê o rótulo que cada unidade usou, e as unidades usaram rótulos diferentes (`M`, `mecânica de fechamento`, `Esclarecimento com impacto mecânico`...). Ela serve para dimensionar e ordenar, **não confirma nada**. A própria `REVISAO-FINAL.md` avisa que esses registros incluem decisões editoriais e correções de interface e não devem ser contados como regras novas.

Registro por registro, com a classe e os donos prováveis na v0.331: `INVENTARIO-ALTERACOES.json`.

| Unidade | Registros | Mecânica (triagem) | Decisão do autor | Donos prováveis na v0.331 |
|---|---:|---:|---:|---|
| Catálogo | 118 | 46 | 0 | peça 17, manual do Fundamento v7, `livro/manual/40` |
| Fundamento | 58 | 29 | 0 | peça 17, manual do Fundamento v7, `livro/manual/40` |
| Ritual e Pactos | 34 | 28 | 1 | peças 27 e 22, `livro/manual/46` e `65` |
| Poderes avançados | 35 | 20 | 1 | peça 11, rascunho da expansão sem barreira |
| Invocações em campo | 59 | 22 | 7 | peça 15, `invocacoes/`, `livro/manual/60` |
| Regras gerais | 38 | 18 | 0 | peças 01, 03, 04, 05 e 23 |
| Emanador | 29 | 18 | 0 | peça 06, `livro/manual/35` |
| Bastião | 26 | 14 | 0 | peças 06, 05 e 23 |
| Dano e recuperação | 35 | 13 | 3 | peça 01 §5.5, peças 19, 24 e 10 |
| Progressão | 42 | 14 | 1 | peças 12 e 18 |
| Aptidões e Refino | 33 | 13 | 0 | peça 11 |
| Rotas | 37 | 10 | 4 | peças 20 e 25 |
| Origens | 35 | 9 | 0 | peças 09 e 13 |
| Demais 10 unidades | 245 | 37 | 13 | ver o inventário |

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

### Terceira passada de 04/10/2026

O Mizuki decidiu mais nove achados e pediu para tirar do livro do jogador as projeções de projetista (`../revisao-interfaces/CORRECOES-APLICADAS.md`, D05 a D17). Onde cada uma encosta na v0.331, a conferir entrada por entrada na migração:

| Decisão | Na candidata | Onde a v0.331 tem a forma antiga |
|---|---|---|
| Capacidades disparadas pela queda resolvem antes da escolha entre Aguentar e Insistir | DR33 | peça 01 §5.5 e `livro/manual/10-como-jogar.md` |
| Feito 8 do limiar retirado; ficam sete feitos | PRO38 | peça 12 (feito 8) e `livro/manual/80-experiencia-e-progressao.md` |
| Batedor: Arma de Fogo pede a autorização combinada antes da escolha da rota | VG-REV-02 | peça 14 §6.5 e `livro/manual/35-caminhos-e-trilhas.md` |
| Permissões que trocam a manipulação gratuita por duas não se somam | EQ26 | `livro/manual/35-caminhos-e-trilhas.md` (Malabarista) e o Talento Maldição do Inventário em `livro/manual/42-tecnica-marcial.md` |
| Fluidez e Passo Guardado contam o primeiro intervalo desde o início do combate; Instante Decisivo é declarado antes da escolha de Bloquear | INC-23, INC-24 | `livro/manual/35-caminhos-e-trilhas.md` e `RASCUNHO-trilhas.md` |
| Lâmina de Cisão causa dano de Alma que atinge só a Integridade | EQ27 | peças 16 e 24 §3.2, `livro/manual/15-dano-e-condicoes.md` e `livro/manual/55-ferramenta-amaldicoada.md` |
| Calo retirado; o personagem marcial registra a Expressão da técnica | R10-33, R10-34 | peça 20 e `livro/manual/42-tecnica-marcial.md` |
| Tabela de Refino "nunca/sempre", Ritmo de campanha, Leque e Lapidação "em todos os marcos" fora do livro do jogador | A33, PRO39, PRO40, R10-35 | as peças 11, 12 e 18 são documentos de projeto e podem manter as contas; `livro/manual/45-aptidoes-e-refino.md` e `livro/manual/80-experiencia-e-progressao.md` são do jogador e seguem a candidata |

Os nomes de G5-10 ficaram como estão, sem migração.

### Quarta passada de 04/10/2026

O Mizuki confirmou a Expressão da técnica na Sem Técnica e pediu para tirar as outras contas de projetista (`../revisao-interfaces/CORRECOES-APLICADAS.md`, D18 a D24):

| Decisão | Na candidata | Onde a v0.331 tem a forma antiga |
|---|---|---|
| Sem Técnica registra a Expressão da técnica | R10-36 | nenhum: `livro/manual/43-sem-tecnica.md`, linha 103, já dava a Passiva Livre de graça, que é o nome antigo da Expressão da técnica. A candidata volta a dizer isso |
| Total de XP até os níveis 20 e 30 fora do livro do jogador | PRO41 | `livro/manual/80-experiencia-e-progressao.md`, linha 38 (e a tabela de meses, linhas 94 a 122) |
| Prazo da marca de mestre fora do livro do jogador | PRO42 | `livro/manual/80-experiencia-e-progressao.md`, linha 174 |
| Diferença de probabilidade sem treino fora do Ritual | RP-33 | `livro/manual/46-ritual.md`, linha 45 ("uns 14 pontos percentuais") |
| Médias de dano e cura fora de três exemplos | R08-34, FU-57, R11-52 | exemplos da candidata; par direto na v0.331 não conferido |

As peças de `sistema/03-mecanica/` são documentos de projeto e podem manter essas contas. Os capítulos de `livro/manual/` são do jogador e seguem a candidata.

### Quinta passada de 04/10/2026

Os 18 achados restantes foram decididos (`../revisao-interfaces/CORRECOES-APLICADAS.md`, D25 a D41). Os que mudam regra e precisam chegar às peças e ao manual:

| Decisão | Na candidata | Onde conferir na v0.331 |
|---|---|---|
| Entidade com alma cai a Integridade zero e só volta com Integridade 1 ou mais | R11-53 | peça 15 e `livro/manual/60-invocacoes.md` |
| Domada sem recolhimento segue ativo/inativo e conta no total de corpos | R11-54 | peça 15 e `livro/manual/60-invocacoes.md` |
| Concentração da entidade termina ao recolher, desativar ou cair | R11-55 | peça 15 e `livro/manual/60-invocacoes.md` |
| Retorno pode ser feito numa troca, recebendo a básica transferida | R11-56, EV28 | `livro/manual/60-invocacoes.md` e `livro/manual/35-caminhos-e-trilhas.md` |
| Carga da entidade: 5 + Força com o que veste e empunha; talento dentro do limite | R11-57 | peça 15 e `livro/manual/60-invocacoes.md` |
| Entidade pode preparar deslocamento com o Movimento restante | R11-58 | `livro/manual/60-invocacoes.md` |
| Inconsciente ou Derrotado encerra a Expansão de Domínio | R08-35 | `livro/manual/40-fundamento.md` (Expansão) |
| Técnica Marcial segue Equipamento restrito, salvo permissão do mestre | R10-37 | peça 20 e `livro/manual/42-tecnica-marcial.md` |
| Ritual na Máxima usa a maior Classe | RP-34 | `livro/manual/46-ritual.md` |
| Classe 0 com Toque ou Aura não ocupa a Restrição Leve | FU-58 | `livro/manual/40-fundamento.md` |
| Teto de 4 × Classe das especiais sem somar alvos | R12-33 | `livro/manual/60-invocacoes.md` |
| Lento corta distâncias concedidas | DR34 | peça 01 e `livro/manual/15-dano-e-condicoes.md` |
| Quebrar o Compasso só no seu turno; Assassino só no seu turno antes do 19 | INC-25 | `livro/manual/35-caminhos-e-trilhas.md` |

Os demais (DR35, INC-26, R11-59, AB24 e R23-32) são texto e ficha, sem regra nova.

### Sexta passada de 05/10/2026

D42 (`../revisao-interfaces/CORRECOES-APLICADAS.md`): o nível 7 da Vanguarda ganhou a **Execução Preparada**, no lugar da Não Pega que a peça 06 previa e que não tinha chegado à candidata.

| Decisão | Na candidata | Onde conferir na v0.331 |
|---|---|---|
| Vanguarda 7: Ataque Extra e Execução Preparada (1× por Sequência, Conclusão depois de duas ou mais Conduções acertadas impõe −1 a um TR adicional) | VG-REV-03, VG-REV-04 | peça 06 (tabela do nível 7 e o texto da Não Pega) e `livro/manual/35-caminhos-e-trilhas.md` |

**O preço ainda não foi medido.** Na peça 06, o degrau do nível 7 da Vanguarda soma 2,10 de dano por rodada: 0,92 do ataque extra e 1,18 da Não Pega. A Execução Preparada troca a segunda parcela. Ao migrar, meça a parcela dela pela mesma régua e confira se o degrau continua abaixo do Guia, do Emanador e do Evocador (2,36).

## Passo 1, feito em 05/10/2026

Os 321 registros de mecânica e de decisão do autor foram conferidos um a um contra a v0.331. Cada um ganhou, no `INVENTARIO-ALTERACOES.json`, o bloco `conferencia_2026_10_05`: a natureza, os donos na v0.331 e uma linha do que muda. Revisão por modelo, não humana.

| Estado | Registros |
|---|---:|
| `confirmada` (migra) | 291 |
| `travada_revisao_morrendo` | 16 |
| `confirmada_em_outro_registro` (a mesma mudança entra por outro) | 10 |
| `so_editorial` (texto e ficha, sem regra) | 4 |

| Natureza | Registros |
|---|---:|
| Fecha lacuna: diz o que a v0.331 deixava em aberto | 166 |
| Muda regra: o resultado na mesa muda | 129 |
| Regra nova: procedimento que a v0.331 não tinha | 6 |
| Alinha donos: a peça já diz, o capítulo do livro não | 3 |
| Exemplo novo | 2 |
| Corrige erro: a tabela de chance do Ritual | 1 |

**O que o passo achou, e que muda a ordem dos próximos:**

1. **Só o Catálogo (89%) e as Origens (51%) editaram texto da v0.331.** Nas outras 21 unidades o texto de antes é um resumo ou um rascunho da própria candidata: os capítulos foram reescritos. Para o livro, migrar é trocar os capítulos do Manual da Guilda pelos da candidata. Para as peças, é levar as regras que mudam e as lacunas fechadas, que é o que o inventário agora separa.
2. **O texto do Fundamento mora em três donos na v0.331:** o gerador do manual do Fundamento (`manual/gerador/partD.js`, `partB.js` para as Passivas, `partE.js` para a Técnica Máxima e a Expansão), o capítulo 40 do Manual da Guilda e uma cópia das tabelas no capítulo 60. Em sete entradas o gerador já tem redação um pouco diferente do capítulo 40. É a lição nº 9: os três mudam juntos, ou um validador compara.
3. **16 registros esperam a revisão do Morrendo**, que o Mizuki adiou para tratar à parte, com a Integridade (`../REVISAO-MORRENDO.md`): 13 do capítulo de Dano e recuperação, o retorno do estágio 4 na Progressão (PRO36), a passiva de Insistir da Técnica Marcial (R10-32) e Ainda Há Tempo do Guia (GUIA-38). O passo 3 deste plano ("Vida a zero") depende dela.
4. **Donos que já divergiam na v0.331:** o capítulo 46 não tem Calado e Silencioso, que a peça 27 tem; o capítulo 65 ainda oferece Estilo no pacto permanente, que a peça 22 tirou na v0.168; a tabela de chance do Ritual está 10 pontos abaixo da fórmula na peça 27 e no capítulo 46.
5. **A Execução Preparada (D42) entra sem preço medido.** Ver a sexta passada, acima.
6. **Fora do passo 1, pelo desenho dele:** os registros de interface (207), editoriais (187), de preservação (63) e de esclarecimento (46). Deles, 76 citam texto que existe na v0.331 (54 de interface, 12 editoriais e 10 de esclarecimento) e merecem uma passada curta antes do passo 2, para conferir que nenhum muda regra por baixo do rótulo.

Os donos mais citados entre os que migram: capítulo 60 (95), capítulo 40 (91), capítulo 35 e peça 06 (60 cada), `partD.js` (51), peça 15 (47), `invocacoes/` (39) e peça 11 (38).

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

**Atualização de 05/10/2026: a ficha já acompanha a candidata.** No repositório `Ficha---RPG-JJK`, o "manual.txt" sai do "LIVRO-COMPLETO.md" desde 04/10/2026 (B33 e B36 do "PENDENCIAS.md" de lá): seis Caminhos, dezoito Trilhas, Talento no lugar de Passiva e as regras novas de Força, carga e XP. As cartas de Habilidades da seção 7 trazem o texto do livro (B37), com a Execução Preparada (D42). A ficha da invocação ficou para depois, por decisão do Mizuki. O que falta lá é montar no Sheets, que é passo do Mizuki. O retrato de 03/10 abaixo fica como histórico.

**O estado delas precisa ser consultado no ambiente onde elas estão sendo feitas.** São trabalho paralelo do Claude, com conversa e pacote próprios. Este plano não supõe que a reconstrução do livro as atualizou, e não supõe o contrário de nada que não foi visto.

O que foi visto aqui é só o retrato do GitHub: o repositório `Ficha---RPG-JJK`, commit `8e4cc75` de 03/10/2026, com a `FICHA`, a `FICHA AMALDIÇOADA` e a `FICHA PESSOAL` na planilha `ficha-v01`. Nesse retrato:

- nenhum arquivo usa Guarda Aberta, Categoria de Efeito ou Expressão da técnica;
- `Classe Passiva`, `Passiva Livre` e `Incapacitado` aparecem em 13, 15 e 7 arquivos, inclusive no "apps-script/Ficha.gs" e no catálogo;
- o próprio "PENDENCIAS.md" registra no B33 que o catálogo e o "manual.txt" estão na v0.263, atrás do sistema.

Antes de mexer na ficha, quem estiver no ambiente dela confirma o estado de lá (pode haver trabalho que não subiu), recebe a lista de divergências confirmadas e decide se a ficha acompanha a candidata ou a publicação distribuída.

## O que este plano não cobre

Ilustrações, acabamento artístico e repaginação ficam fora, por decisão do Mizuki. A migração também não decide a publicação, não toca a edição distribuída e não muda a candidata.
