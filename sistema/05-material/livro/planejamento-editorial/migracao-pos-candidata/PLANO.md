# Plano de migração da candidata para as peças, validadores, geradores e fichas

Item 4 da fila pós-reconstrução, escrito em 04/10/2026. **Nada foi migrado.** Nenhuma peça de `sistema/03-mecanica`, nenhum validador, gerador ou ficha foi alterado por este plano.

## Quando começar

**Decisão de 05/10/2026: migrar.** O Mizuki autorizou a migração (*"e... podemos migrar"*) depois de fechar a revisão de interfaces e a sexta passada, sem esperar o teste com leitores. As duas condições abaixo ficam como o desenho original do plano; a primeira foi dispensada por ele, e a segunda é esta decisão. O que sair do teste com leitores, quando ele rodar, entra como mudança nova, pela candidata e depois pelas peças.

A migração só começa depois de duas coisas, nesta ordem:

1. **A candidata estabilizar.** Os achados da revisão de interfaces (`../revisao-interfaces/ACHADOS.md`) que pedem decisão do autor precisam estar respondidos, e o teste com leitores e jogadores (`../testes-com-leitores/`) precisa ter rodado pelo menos a primeira leva nos quatro grupos prioritários. Mudança que sair da mesa entra na candidata antes de entrar nas peças, senão a migração é feita duas vezes.
2. **O Mizuki decidir a publicação.** Hoje a candidata é separada da edição v0.331 distribuída aos jogadores. Migrar as peças antes dessa decisão faria as peças, que são a fonte dos validadores, descreverem uma regra que o livro distribuído não tem.

Se a decisão for não publicar a candidata inteira, este plano vale por unidade: migra-se só o que for aprovado, e o resto fica registrado como candidata.

## O tamanho do trabalho

Os 23 arquivos `ALTERACOES.json` das unidades somam **838 registros** de antes, depois e motivo (eram 774 em 04/10/2026; as passadas de decisão do autor acrescentaram 50, o inventário foi refeito em 05/10/2026, e a sétima passada, D43, acrescentou mais 14). A triagem automática pelo campo de tipo de cada registro dá:

| Classe (triagem automática) | Registros |
|---|---:|
| Mecânica | 299 |
| Interface ou correção | 207 |
| Editorial | 187 |
| Preservação | 63 |
| Esclarecimento | 46 |
| Decisão do autor | 36 |

*"Decisão do autor" é o rótulo das passadas de 04/10 e 05/10 sem a marca `M`. Quais delas mudam regra está nas tabelas de cada passada, abaixo.*

A triagem lê o rótulo que cada unidade usou, e as unidades usaram rótulos diferentes (`M`, `mecânica de fechamento`, `Esclarecimento com impacto mecânico`...). Ela serve para dimensionar e ordenar, **não confirma nada**. A própria `REVISAO-FINAL.md` avisa que esses registros incluem decisões editoriais e correções de interface e não devem ser contados como regras novas.

Registro por registro, com a classe e os donos prováveis na v0.331: `INVENTARIO-ALTERACOES.json`.

| Unidade | Registros | Mecânica (triagem) | Decisão do autor | Donos prováveis na v0.331 |
|---|---:|---:|---:|---|
| Catálogo | 123 | 51 | 0 | peça 17, manual do Fundamento v7, `livro/manual/40` |
| Fundamento | 61 | 32 | 0 | peça 17, manual do Fundamento v7, `livro/manual/40` |
| Ritual e Pactos | 34 | 28 | 1 | peças 27 e 22, `livro/manual/46` e `65` |
| Poderes avançados | 35 | 20 | 1 | peça 11, rascunho da expansão sem barreira |
| Invocações em campo | 59 | 22 | 7 | peça 15, `invocacoes/`, `livro/manual/60` |
| Regras gerais | 38 | 18 | 0 | peças 01, 03, 04, 05 e 23 |
| Emanador | 29 | 18 | 0 | peça 06, `livro/manual/35` |
| Bastião | 26 | 14 | 0 | peças 06, 05 e 23 |
| Dano e recuperação | 36 | 13 | 4 | peça 01 §5.5, peças 19, 24 e 10 |
| Progressão | 42 | 14 | 1 | peças 12 e 18 |
| Aptidões e Refino | 33 | 13 | 0 | peça 11 |
| Rotas | 39 | 10 | 6 | peças 20 e 25 |
| Origens | 35 | 9 | 0 | peças 09 e 13 |
| Demais 10 unidades | 248 | 37 | 16 | ver o inventário |

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
| Sobre Carregar Energia (Emanador, Trilha Catalisador) | Sobrecarregar Energia | 06 | `conferir-nomes`, `conferir-catalogo` | nenhum | a ficha já usa o nome novo |
| Passiva / Passivas (a categoria comprável) | Talento / Talentos | 20 peças, 281 ocorrências | 12 validadores, 182 ocorrências | `gerador-ficha/ficha.js` e o gerador do `.docx` | a ficha já usa o nome novo |
| Reencarnado (Origem) | Encarnado | 08, 09, 11, 13, 14, 21 | `conferir-nomes`, `conferir-objeto` | `gerador-ficha/dados.js` | a ficha já usa o nome novo |

*As três últimas linhas entraram depois da tabela original. `Passiva` → `Talento` é o NT05 da migração de nomes do livro (`consolidacao/lote-01/migracao-nomes/MAPA.json`), que a tabela de 04/10 deixou de fora, e `Reencarnado` → `Encarnado` é o registro ORI02. A quinta linha entrou na passada dos 76, em 05/10/2026 (registro EMA27, que a triagem automática marcou como correção ortográfica). A triagem do `conferir-nomes.py --candidatos` dá `Sobrecarregar Energia` como LIVRE.*

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

### Sétima passada de 05/10/2026

D43 (`../revisao-interfaces/CORRECOES-APLICADAS.md`): **Condição, Prende e Cerca pedem TR mesmo num feitiço de ataque.** O acerto aplica o dano; o alvo acertado faz o TR registrado para o Controle e só recebe essas peças se falhar. Puxa ficou de fora, por decisão do Mizuki: é deslocamento forçado, como o Empurrão.

| Decisão | Na candidata | Onde conferir na v0.331 |
|---|---|---|
| Condição, Prende e Cerca na falha do TR, mesmo em ataque; um TR por alvo para as três; a Pesada perde o "mesmo que tenha sido aplicada por ataque" | CAT-D43-01 a CAT-D43-05, FU-59 a FU-61 | `manual/gerador/partD.js` (linhas de Prende e Cerca e a da Condição), `livro/manual/40-fundamento.md` e a cópia em `60-invocacoes.md` |
| A Melhoria Condição sempre pede TR | DR36 | peça 19 e `livro/manual/15-dano-e-condicoes.md` |
| Kaori: Peso nas Mãos pede TR Físico contra CD 12 para o Derrubado | AB25 a AB27 | `livro/manual/08-inicio-rapido.md` |
| Iori: Gancho fechado pede TR Físico para Prende | R10-38, R10-39 | só na candidata; a regra vem do Catálogo |

**Os três donos do Fundamento mudam juntos** (`partD.js`, capítulo 40 e a cópia no 60), como o passo 1 já avisa. **A ficha também:** o "catalogo-projeto-m.json" e o "manual.txt" do `Ficha---RPG-JJK` saem do livro, e a ficha da Kaori tem o Peso nas Mãos.

**O preço não foi medido de novo.** Exigir TR num ataque deixa Condição, Prende e Cerca mais fracas na ficha de ataque do que eram, e iguais na ficha de TR. O preço de cada peça continua o mesmo. Se a migração quiser rever algum, o número sai de conta rodada, com a chance de falhar no TR multiplicando a de acertar, não de intuição.

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
6. **Fora do passo 1, pelo desenho dele:** os registros de interface (207), editoriais (187), de preservação (63) e de esclarecimento (46). Deles, 76 citam texto que existe na v0.331 (54 de interface, 12 editoriais e 10 de esclarecimento) e merecem uma passada curta antes do passo 2, para conferir que nenhum muda regra por baixo do rótulo. *Feita no mesmo dia: ver a seção seguinte.*

Os donos mais citados entre os que migram: capítulo 60 (95), capítulo 40 (91), capítulo 35 e peça 06 (60 cada), `partD.js` (51), peça 15 (47), `invocacoes/` (39) e peça 11 (38).

## Passada dos 76, feita em 05/10/2026

Os 76 registros de interface, editoriais e de esclarecimento que citam texto da v0.331 foram lidos um a um: o "antes" no dono e o "depois" na candidata (`LIVRO-COMPLETO.md`). Dois deles, a Queima e o Sugar, vinham sem o "depois" no inventário. Cada registro ganhou o mesmo bloco `conferencia_2026_10_05` do passo 1. Revisão por modelo, não humana.

| Natureza | Registros |
|---|---:|
| Fecha lacuna | 69 |
| Só texto (`so_editorial`) | 3 |
| Muda regra | 2 |
| Sincroniza donos | 1 |
| Travado pela revisão do Morrendo | 1 |

**Duas mudanças de regra estavam por baixo do rótulo de interface, as duas no Catálogo:**

- **Queima (R07-B-10).** A v0.331 dizia só "metade dos dados de novo". A candidata tira a Queima do erro com dano parcial e do TR bem-sucedido, usa os dados de antes do crítico e, em Rajada ou Mais Um, só os dados do alvo.
- **Sugar (R07-B-28).** O dano parcial de Certeiro e de TR bem-sucedido deixa de contar para a cura, e o teto de 5 × Classe vale para a conjuração inteira, somando os alvos.

**O resto que vale saber:**

- **A Remenda (R07-B-38) fica travada** com os 16 do passo 1. A revisão adiada do Morrendo e da Integridade (`../REVISAO-MORRENDO.md`) cita a Remenda pelo nome.
- **Um quinto nome para o passo 2:** `Sobre Carregar Energia` vira `Sobrecarregar Energia` (EMA27). Ele entrou na tabela de nomes, acima.
- **A Abre Ferida (R07-B-03) é uma leitura escolhida.** "−2 em um TR" passou a querer dizer "−2 em todo TR de um dos quatro tipos, escolhido na criação". Quem lia "uma rolagem" vê a peça ficar mais forte.
- **Um defeito editorial pequeno na candidata:** o exemplo da Abre Ferida ficou logo depois da Firmeza, com a Sobrecarga no meio. Fica para a próxima passada do livro.
- **GER36 não muda a mesa.** O capítulo 50 dizia que o uniforme desliga a proteção "de energia amaldiçoada", mas o 47 já desligava a Defesa sem Armadura da Bênção.

Depois da passada, o inventário fica assim:

| Estado | Registros |
|---|---:|
| `confirmada` (migra) | 363 |
| `travada_revisao_morrendo` | 17 |
| `confirmada_em_outro_registro` | 10 |
| `so_editorial` | 7 |
| `nao_confirmada` (interface, editorial, preservação e esclarecimento que não citam a v0.331) | 427 |

## Passo 4, feito em 05/10/2026 (v0.335)

**O inventário não cobria tudo o que a candidata mudou em equipamento.** *Ele lê os `ALTERACOES.json` das unidades do lote final, e várias regras entraram nas rodadas anteriores do mesmo capítulo (`equipamento/lote-02-r2` a `lote-08` e as duas `revisao-carga`), aprovadas com a candidata e sem registro no lote final.* **Por isso o passo 4 comparou o capítulo inteiro com as peças, e não só os 20 registros de equipamento.** *Revisão por modelo, não humana.*

**Peça 14:** *a propriedade `Leve` (19 armas) e a `Discreta` (o `Taco`); o `Volume` arma a arma, no lugar da régua das propriedades, e o do `Traje` `1` e do `Broquel`; as bestas com um virote (D, EQ25); a munição como estoque, com preço, `Volume`, recarga parcial e munição inicial; o Revólver a `¥150.000`; o benefício do `Traje` num TR e em perícias; o arrasto e o transporte em grupo; e o manejo — vestir, retirar, escudo, sacar, acesso, patente inicial.* **Duas divergências eram mais velhas que a candidata:** *a `Força 1` da `Espingarda` e do `Rifle` e a penalidade de metade do deslocamento sem a Força da arma vinham do livro desde a v0.176, e a peça 14 e a peça 19 nunca acompanharam.*

**Peça 16:** *o catálogo foi o da rodada `lote-08`, refeita a pedido do Mizuki ("poderes por grau, poucos benefícios numéricos"): dez `Estigma` mudaram de regra e sete entraram.* **O preço dos sete novos, do `Anátema` e do `Quebranto` não foi medido** — *fica no §9 da peça.*

**Peça 21:** *a candidata não mudou a máquina; pôs na mão do mestre a frequência, o alcance e a duração do selo, e as consequências de ingerir.*

**Peça 20:** *a rota de arma segue o Equipamento restrito (R10-37, D33).*

**Peça 15 (Invocações):** *ela se declara registro histórico desde a v0.331, e a candidata usa outra arquitetura.* **Os 40 registros (PRO37, 28 de `Invocações em campo`, 7 de `Construir invocações` e 4 de `Fabricação`) não foram escritos dentro dela;** *o cabeçalho passou a apontar o livro reconstruído como dono e a listar onde o texto antigo diz o contrário.* *(Os seis FU-xx que também citam a peça 15 são do Fundamento e vão no passo 5.)* **As contradições, com a linha da peça na v0.334:**

| registro | a peça 15 diz | a candidata diz |
|---|---|---|
| R11-07 | amarra de `18 m` (L99, L738, checagem em L1201) | a ordem chega pelos sentidos normais; sobrenatural é da ficha (CAMPO L97) |
| R11-19, R11-45 | comandar custa a ação padrão (L107, L110, L1188) | `Rápido` na Bônus, `Reação` na sua Reação, `Segura` paga agora (CAMPO L234–242, L263) |
| R11-26, R11-56 | retorno por `1 ×` maior Classe e Padrão (L530, L624) | duas vezes o PE da entrada e a Bônus (CAMPO L462) |
| R11-28, R11-49 | volta só no descanso longo; nada de vida no curto (L630–636) | reparo no descanso curto, CD `8 + atributo + Maestria + ajuste` (CAMPO L366–377) |
| R11-32, R11-34, R11-35, R12-05 | domada sem dano de técnica (L984, L988, L989, L991) | capacidades convertidas; Acerto do domínio em Classe `d8` (CAMPO L432–436, CONSTRUIR L144, L703) |
| R11-37 | some no zero (L114, L566) | Desligada, com o dano depois somando até destruir (CAMPO L466–470) |
| R11-48, R11-51, R11-54, PRO37 | sem teto de corpos (L509, L511); os quatro tipos iguais (L1011) | total mantido = atributo da Defesa + maior capacidade ativa; corpo e domada sem recolhimento ficam no mundo (CAMPO L343–353) |
| R11-50 | toda invocação tem o `Investir` (L100, L887, L964) | básica ofensiva de Classe 0 ou arma empunhada (CAMPO L114) |
| R12-32 | o dado da arma não soma (L715) | o dano é o da arma (CONSTRUIR L212) |

*E oito diferenças de arquitetura que sustentam várias linhas: o comando (a básica age pela tarefa sem ação do dono), o preço de invocar (Bônus e a maior Classe do nível da entidade), o nível (o da entidade, e não o do dono), a quantidade (duas entidades ativas, e não a Matilha de cinco), a ficha (básica, especial e Talentos por Categoria de Efeito, e não `Traço` e `Comando`), o dano (especiais em `d8` e no máximo duas entidades causando dano), a área (sem o `×1,5`) e o dono inconsciente (as entidades seguem com a tarefa).* **Os outros 22 registros são lacuna na peça ou já batem com ela (o deslocamento de `9 m`, R12-08), e não contradição** — *reserva, Concentração, Armado, manutenção, fabricação e transferência não existem no desenho antigo.*

**Peça 06 e Caminhos:** *o texto jogável dos seis Caminhos mora, na v0.331, na `caminhos/05-Edicao-Integrada/` e no capítulo 35 do livro, que ficam congelados; a peça 06 guarda a base (vida, PE, perícias, armas, TR) e a régua de preço, e o `RASCUNHO-trilhas` e os DESENHO da raiz se declaram registro da coleção anterior.* **Dos 60 registros confirmados dos Caminhos, 34 batem com a edição integrada, 6 são lacuna e 20 a contradizem:**

| registro | onde a edição integrada diz o contrário |
|---|---|
| BAS03, BAS04, BAS06, BAS11, BAS18, BAS26 | Bastião: L42 e L96 (Olhos Em Mim e o fim da área), L44 e L64 (o teste de Provocar vira CD), L46 e L48 (perceber o aliado; dano no erro), L86 (Alicerce é resistência, e não metade), L126 (o Arrastão e o uso da rodada), L54 (TR Físico de efeito ofensivo) |
| VG-08, VG-REV-01, VG-REV-03, VG-REV-04 | Vanguarda: L226 e L230 (desfazer a armação não destrói a flecha), L348 (o Combate Irregular só na Arma de Fogo), L35 e L128 (a Execução Preparada no nível 7) |
| R15-09, R15-18 | Guia: L76 e L140 (o ataque apoiado resolve antes da resposta), L172 e L205 (`1,5 m` de altura) |
| EMA15, EMA16 | Emanador: L202 (descarregar antes de mudar de perfil), L206 (perceber a arma e o espaço de chegada) |
| INC-05, INC-09, INC-22, INC-24, INC-25, INC-26 | Incursor: L65 (Guarda Aberta e Fluidez), L160, L263, L277 e L305 (`Leve` ou `Fineza`), L520 a L522 (o segundo ataque do Malabarista), L70 (a janela do Instante Decisivo), L176, L206 e L360 (só no seu turno antes do 19), L614 (`Longo Alcance` de arremesso) |

*As linhas são de `caminhos/05-Edicao-Integrada/0N-<Caminho>-Caminho-e-Trilhas.md`, e o capítulo 35 do livro v0.331 é espelho delas. Elas saem quando a candidata substituir o livro, que é a decisão de publicação.* **Na peça 06 mudaram três coisas:** *a troca de Trilha entre missões (PRO20), o nome das entregas da rota `Arma de Fogo` e a frase do Emanador (EMA07).*

**O achado do passo: a `Execução Preparada` vale muito menos que a `Não Pega`.** *Medida pela régua do degrau do nível 7 (`sistema/01-pesquisa/medicao-v0335/conta-execucao-preparada.py`, com regressão nos `1,18` da `Não Pega`), ela fica entre `0,00` e `0,12` fatia.* **O degrau da Vanguarda cai de `2,10` para no máximo `1,04`, contra `2,36` dos três Caminhos de degrau grande.** **Decisão do Mizuki na v0.336 (D44):** *"Coloca que é -2 no teste e segue assim, vale pouco mesmo, n tem problema".* **A `Execução Preparada` impõe `−2`, a tabela da peça 06 publica `0,23` (o teto) e a Vanguarda fica em `1,15`, `−1,21` contra o degrau grande, por decisão escrita.**

**Os validadores:** *o `conferir-equipamento.py` compara agora o `Volume` das 52 armas, a Força e o `Volume` das proteções com o capítulo de Equipamento da candidata, que passou a ser o dono desses números; o `conferir-ferramenta.py` conta dezessete `Estigma` e lê da peça quantos são de `Classe 2`; o `conferir-dano.py` cobra a penalidade nova.*

## Passo 5, primeira parte, feita em 06/10/2026 (v0.337)

**Os sete validadores que abriam o `.docx` passaram a ler o livro reconstruído.** *O leitor é o `sistema/03-mecanica/livro.py`: ele acha cada unidade no lote que a consolidação usa, picota título, tabela e página, e monta o Catálogo (nome, tipo, preço, Família) a partir das marcas de página do capítulo.* **Nenhum validador precisa mais do `python-docx`;** *rodando os 27 com a biblioteca bloqueada, todos saem com zero puladas, e a checagem `9.1` do `conferir-repositorio.py` passou a acusar quem voltar a abrir o `.docx`.* **O Catálogo do livro bate nome a nome com o do `.docx`:** *69 Melhorias, 19 Restrições e 18 Talentos, com os mesmos preços.* *Revisão por modelo, não humana.*

**O tamanho estava subestimado.** *Além dos sete que abriam o `.docx`, treze arquivos leem o `manual/gerador` direto (`partA` a `partF`): o `conferir-alma`, o `-atributos`, o `-bestiario`, o `-bloquear`, o `-dano`, o `-expansao`, o `-ficha`, o `-invocacoes`, o `-manual` e o `-ritual`, o `conferir-repositorio.py` e dois scripts de `manual/matematica`.* **Por isso o passo ficou em duas partes.** *Nesta, o `.docx` deixou de ser fonte. Na segunda, o gerador, o `.docx` e o `.pdf` vão para o arquivo, e antes disso três tabelas que só o gerador publica precisam de dono:*

| tabela do gerador | quem lê | o livro tem? |
|---|---|---|
| `Inimigos` (dano do grupo, chefe e capanga por nível) e a prosa dela (os `90%`, as três rodadas, o esquadrão) | `conferir-acao` (7), `-bestiario`, `-dano`, `-manual` (4a e 4b), `-alma`, `-bloquear`, `-invocacoes`, `-atributos` | não. *O livro do bestiário publica tabelas derivadas dela (vida por faixa, golpe por faixa), e não ela* |
| `A curva` (Rotina, feitiço num alvo, somando alvos, por Classe) | `conferir-acao` (9), `-manual` (4c a 4f) | não |
| `PE total` por nível do conjurador | `conferir-manual` (4a) | não. *O livro escreve `PE máximo = PE por nível do Caminho × nível`* |

*A proposta para a segunda parte é a peça que já se declara consumidora virar dona: a `Inimigos` na peça 26 (que cita "manual, a tabela `Inimigos`" como dona da vida e do golpe), a curva na peça 05 ou 06, e o PE total na peça 01. Até lá, as três leituras vão ao gerador, que era de onde o `.docx` saía.*

**O que o livro fechou ou mudou, achado na troca:**

- **O combo de Melhorias perdeu a exceção do mestre.** *O v7 deixava o mestre aprovar "por menos pontos ou menos espaço, por conta e risco, e o manual não recomenda"; o livro diz que reunir duas Melhorias sob um nome não reduz preço nem vaga, sem exceção.* **Nenhuma peça publicava a exceção**, *então nada mudou na mesa das peças; o capítulo 9 do livro v0.331 guarda o parágrafo antigo até ser trocado.*
- **A `Base por Classe` separou a `Onda`.** *No livro, a linha `Cura e Apoio` dá alcance de Classe 0 só ao `Apoio` (`4,5 m`), e a `Onda` tem linha própria, indisponível em Classe 0.* **A regra é a mesma do v0.166 (Classe 0 não cura);** *a comparação da tabela do capítulo 9 v0.331 com a do dono saiu do `conferir-manual` (8.1 c), porque acenderia pela mudança aprovada.*
- **A escada de frequência do `Efeito Próprio` saiu do livro.** *O v7 perguntava "em quantas cenas por arco" (uma: Leve; metade: Média; quase toda: Pesada); no livro o mestre define o preço comparando com as peças de função mais próxima, e o `Talento Próprio` usa a escada de Categoria.* **A escada sobrevive só na peça 11 §6.7, que a usa para a `Aptidão Própria`.** *O `conferir-manual` (4j) registra que ela não tem mais com quem ser comparada; a migração das Aptidões decide se a peça 11 segue o livro.*
- **O `inimigo fraco` virou `Capanga`.** *O `Peso da Presença` pega um inimigo da categoria `Capanga`, que o bestiário define. A isenção que o `conferir-manual` dava ao termo indefinido saiu.*
- **O livro não publica a contagem de Melhorias por extenso** *("Sessenta e nove Melhorias, em nove Famílias"), nem os 50 Feitiços prontos, os 70 Temas e os 3 Fundamentos prontos.* **A triagem do `conferir-nomes` perdeu essas três categorias**, *porque nome nenhum colide com o que o livro não publica.*

**Nas peças:** *peça 08, o passo do equipamento pede a situação, o TR e as perícias do `Traje` (AB24); peça 12, o oitavo feito saiu e a §9.1 lista as lacunas da Progressão que a candidata fechou; peça 18, o dono das colunas de Classe, Talento e Classe 0 é o livro, e o `conferir-progressao` confere seis colunas contra ele; peça 19, o `Lento` corta também as distâncias concedidas, como a do `Passo` (FU-26), e a distribuição dos tipos de dano se escolhe na criação (FU-09).* **Os outros registros do Fundamento e do Catálogo não têm peça dona:** *o dono era o `.docx`, e agora é o livro.* *O passo 1 atribuiu os 137 à peça 17, mas a peça 17 é o índice das entregas de Caminho e não tem regra do Fundamento: a atribuição estava errada, e o `.docx` era o único dono.* *Os que citam a peça 15 (FU-04, FU-13, FU-14, FU-27, FU-58 e os de Técnica Máxima) caem no cabeçalho dela, que já aponta o livro como dono.*

**Um achado fora do passo: o livro tem quinze tipos de dano, e as peças 01 e 19 têm catorze.** *A candidata acrescentou `Força` (energia pura) aos Especiais numa rodada anterior do capítulo de Dano, e o inventário do lote final não registrou; é o mesmo padrão do equipamento no passo 4.* **Não é Morrendo, então não espera a revisão dele,** *mas é do capítulo de Dano: entra quando esse capítulo for comparado inteiro com as peças.*

## Passo 5, segunda parte, feita em 06/10/2026 (v0.338)

**As tabelas de mestre do manual v7 ganharam dono em peça, sem mudar número.** *Eram a seção `Para o mestre` do manual, que o livro reconstruído não tem:*

| tabela | foi para | quem lê |
|---|---|---|
| `Inimigos` e a prosa dela (os `90%`, as três rodadas, o esquadrão, as linhas de Integridade e Reação) | peça 26 §3.0 | `conferir-acao` (7), `-alma`, `-atributos`, `-bestiario`, `-bloquear`, `-dano`, `-invocacoes`, `-manual` |
| `A curva` (Rotina, feitiço num alvo, somando alvos, Liberação, Técnica Máxima) | peça 05 §2.1 | `conferir-acao` (9), `-manual` (4c a 4f) |
| `PE total` por nível do conjurador de referência | peça 01 §5.3, que já publicava a cópia | `conferir-atributos`, `-manual` (4a) |
| a caixa `Vida` (`20 + 8 × (nível − 1)`) | peça 24 §2, como a curva em que os estágios foram calibrados | `conferir-alma` (1), `-atributos` |

**E as leituras do Fundamento que ainda iam ao gerador passaram para o livro:** *o `conferir-ritual` lê os pontos, o teto e a Liberação do Fundamento, as Restrições do Catálogo e as Formas; o `conferir-ficha` lê as Famílias e o alcance do Projétil; o `conferir-bestiario` lê os pontos por Classe, a escada de esfera e os gates da Expansão; o `conferir-dano` confere o `Calado` do livro no lugar do `partD.js`; e a checagem 12 do `conferir-repositorio` compara o degrau das 82 Melhorias e Restrições do livro v0.331 com o do livro reconstruído, que passou a ser o dono (o texto saiu da comparação, porque o livro reescreveu todas).* **Os estágios de Integridade passaram a ser conferidos contra o capítulo de Dano do livro, em fração e número;** *o efeito do estágio 4 mudou lá (Inconsciente e Derrotado) e espera a revisão do Morrendo.*

**O que saiu sem substituto, porque era cópia do manual:** *a caixa `Integridade` e o glossário do manual (o `conferir-alma` os comparava com a peça 24, que é a dona) e a `4b` do `conferir-manual` (o `.docx` contra o gerador).*

**O gerador ainda não foi para o arquivo, e o motivo é medido.** *Três coisas ainda o leem:*

- *o `conferir-expansao`, que confere a Expansão de Domínio contra o `partE.js`: trocar essa leitura é migrar o capítulo de Poderes avançados, que é um dos seis capítulos sem passo (abaixo);*
- *dois scripts de medição, `manual/matematica/casca-sem-barreira.py` e `sobrecarga.py`, que não estão na bateria e medem coisas dos Poderes e do Catálogo;*
- *os capítulos do Fundamento e do Catálogo do livro, que guardam o hash dos `part*.js` como fonte preservada; ao mover, eles ganham o cotejo de "arquivo movido, mesmo hash".*

**Então o gerador, o `.docx` e o `.pdf` vão para o arquivo junto com a migração dos Poderes avançados.** *O `conferir-repositorio.py` vai precisar de um mapa de "movidos para o arquivo" (no molde do `LOCAIS`): 33 citações em documentos e evidências apontam para `manual/gerador/`, e várias estão em arquivos presos por hash nos manifestos do livro, que não se reescrevem.*

## Passo 5b, primeiros três capítulos, feitos em 06/10/2026 (v0.340)

*Aptidões e Refino (peça 11), Rotas (peças 20, 25 e 11 §6.8) e Origens (peça 13). Comparação do capítulo inteiro com as peças, e não só dos registros do inventário. Revisão por modelo, não humana.*

**Aptidões.** *A comparação achou que os registros A06 (a escada do dano na arma) e A10 a A12 (o `Projetar`) eram regra, e o inventário os classificava como interface.* **A06:** *a escada do livro começa no refino `1`; a peça começava no `3`. Adotada por decisão do Mizuki, com as medidas dependentes refeitas (CHANGELOG da v0.340).* **A10 a A12:** *o `Projetar` pago, na forma que o Mizuki decidiu (`1` até metade do refino, `2d6` por PE); a candidata ainda diz `1d6` e o refino inteiro.* **A20, A25 e A27:** *raio do `Domínio Simples`, levantar a barreira em combate e a `Cortina` (`40 × refino`, `90 m`).* **Os outros registros confirmados** *(A08, A11, A15, A18, A22 a A24, A26, A28, A29) estão na peça 11 §6.10.*

**Rotas.** *Mudaram de regra o `Calo` (saiu, D12), o `Contragolpe`, a `Presilha`, o `Esteio`, o `Vulto`, o `Antecipar`, o `Assombro`, o `Casco`, o bônus de autocura de `+4` no refino `10` e o atributo da Kata, que era o item aberto da peça 20 §5 desde a v0.133 e fechou na regra do livro: o atributo da arma, no ataque e na CD.* **O `Segundo Fôlego` (R10-32) não migrou:** *espera o Morrendo.*

**Origens.** *Cinco Legados passaram de por cena para por descanso curto, o `Revezamento` apaga a `Guarda Aberta` (e a trava do relógio do `Desliga` virou piso de raridade), e o `Sangue que Não é Sangue` ganhou a necessidade corporal.*

**O que sobra destes três capítulos:** *os nomes dos três formatos de Legado (ORI01, `138` ocorrências na peça 13); o exemplo da `Abre Ferida` (candidata, junto da próxima reconstrução do PDF); e os registros editoriais e de preservação, que não mudam regra.* **A candidata e o R28a ainda têm o `Projetar` antigo** *(`R28a-o-que-falta.md`).*

## Capítulo de Dano sem o Morrendo, feito em 09/10/2026 (v0.347)

*Comparação das páginas do capítulo no R41 com as peças 19, 10 e 1, fora as de vida a zero. Revisão por modelo, não humana.*

**Dois números divergiam, e nenhum dos dois era da revisão do R41.** **Os tipos de dano:** *o livro tem quinze, com `Força`, desde uma rodada da candidata que o inventário não registrou; as peças 1 e 19 tinham catorze (achado no passo 5, v0.337).* **O degrau 2 da exaustão:** *o Mizuki o trocou de `6 m` para `4,5 m` na revisão do Word da v0.176, o livro v0.331 publicou, e a peça 10 e o validador dela ficaram no `6 m`, com um parágrafo defendendo a diferença para a Integridade.* **Os dois entraram nas peças, e os dois validadores passaram a ler o número da peça e a compará-lo com o R41.**

**O resto é lacuna fechada**, *e está na peça 19, na subseção da v0.347: a ordem de resolver um dano, o arredondamento do dano recebido, e o que o livro escreve a mais sobre nove condições.*

**Não migrou:** *`Inconsciente`, `Dano na alma`, os estágios de Integridade, `Vida a zero`, `Aguentar`, `Insistir`, `Socorro`, Sequelas e `Derrota e morte`.* **É o passo 3, que espera a revisão do Morrendo.**

## Os seis capítulos sem passo, achados em 06/10/2026

**A tabela de tamanho do topo lista seis capítulos que a ordem proposta não cobria:** *Ritual e Pactos (29 registros confirmados, peças 22 e 27), Poderes avançados (21, peça 11 e o rascunho da Expansão sem Barreiras), Regras gerais (19, peças 01, 03, 04, 05 e 23), Origens (18, peças 09 e 13), Rotas (14, peças 20 e 25) e Aptidões e Refino (13, peça 11).* **São 114 registros que nenhum passo migrava.** *Eles entram como passo 5b, um capítulo por versão, comparando o capítulo inteiro com as peças (o inventário não cobre as rodadas anteriores, como se viu no Equipamento e no tipo `Força` do Dano). Antes deles vai o capítulo de Dano sem o Morrendo.*

## Decisões do Mizuki de 05/10/2026, para os passos 2 e 3

**1. O manual do Fundamento em `.docx` (v7) é aposentado como fonte.** Resposta dele: *"A"*. O Fundamento passa a ter um dono só, o livro. Os validadores que hoje leem o `.docx` passam a ler o livro, e o `manual/gerador` vai para o arquivo.

O tamanho, medido antes de mexer: **sete validadores abrem o `.docx`**. São eles o `conferir-acao` (seis leituras, nas checagens da Dívida, dos vetos do Rápido e da Reação, da Concentração, da duração da Concentrada e da Duradoura e do Alvo de Caça), o `conferir-bestiario`, o `conferir-dano`, o `conferir-manual`, o `conferir-nomes`, o `conferir-pericias` e o `conferir-progressao`. O `conferir-repositorio.py` confere que o `.docx` e o `.pdf` existem.

**A troca de fonte vai no passo 5, e não no 2.** O Fundamento da candidata já tem as regras novas, e o Catálogo dela não usa tabelas: cada Melhoria virou um título com o custo ao lado. Se os validadores passassem a ler o livro no passo 2, comparariam as peças da v0.331 com as regras novas e falhariam por regra, não por nome. Então:

- **no passo 2**, o `.docx` continua sendo lido, congelado, e os validadores traduzem o nome antigo dele para o novo das peças por uma tabela de alias;
- **no passo 5**, quando as peças 08, 17 e 18 recebem as regras, os sete validadores passam a ler o livro, o alias sai, e o `manual/gerador`, o `.docx` e o `.pdf` vão para o arquivo com o cabeçalho de por que morreram;
- **o passo 6 encolhe:** o `.docx` não é mais regerado.

**2. O Morrendo fica na versão atual por enquanto.** Resposta dele: *"Deixe com a versão atual por enquanto, iremos ver depois"*. As peças ficam com a regra da v0.331 (peça 01 §5.5 e as remissões das peças 12, 15, 20 e 24), o livro fica com o texto da candidata, e o passo 3 só começa depois da revisão. Os 17 registros travados não migram. Os outros passos pulam o que for Aguentar, Insistir, socorro, Sequela de queda e Integridade.

## Ordem proposta

Cada passo fecha com a bateria inteira verde (os 27 validadores de `03-mecanica`, `pac7.py`, `v7.py` e o `conferir-repositorio.py`, com `PULADA=0` conferido) e uma entrada no CHANGELOG. Um passo por versão, para a bateria apontar o culpado quando quebrar.

1. **Confirmar cada registro mecânico.** Ler o "depois" do inventário contra a peça dona e marcar `confirmada`, `ja_na_peca` ou `so_editorial` no `estado_migracao`. Começar pelas unidades com mais registros mecânicos (Catálogo, Fundamento, Ritual). Sem esse passo, a migração copia uma suposição.
2. **Nomes.** *Feito: v0.332 e v0.333.* *Dividido em duas versões em 05/10/2026.* **A v0.332 fez os quatro pequenos** (`Guarda Aberta`, `Identificar Feitiço` e `Leitura de Feitiços`, `Sobrecarregar Energia`, `Encarnado`); **a v0.333 faz a família da `Passiva`** (`Talento`, `Categoria de Efeito`, `Expressão da técnica`). O livro v0.331 e as cópias da edição integrada ficam congelados junto com o `.docx`, porque o capítulo 60 está preso por hash à referência aprovada; o `sistema/03-mecanica/renomes.py` traduz o nome antigo quando um validador lê uma delas. Trocar os nomes nas peças, nos validadores e nos geradores, deixando os nomes antigos como alias no `conferir-nomes.py`, para a triagem continuar pegando quem reusar. *Decidido em 05/10/2026:* o `.docx` v7 sai de fonte, mas só no passo 5; até lá ele é lido congelado, com o nome antigo traduzido para o novo.
2b. **O nome do sistema: Ciclo Maldito.** *Feito: v0.334.* *Decisão do Mizuki em 05/10/2026, depois de mandar o livro final (R28a): o nome vale no repositório inteiro.* Uma versão própria, com a triagem do `conferir-nomes` e os validadores que leem o nome. Ficaram com o nome antigo os nomes de arquivo `Projeto-M-*`, o livro v0.331 congelado, o histórico e o bestiário, que troca na passada própria dele.
3. **Vida a zero.** *Adiado em 05/10/2026, até a revisão do Morrendo.* Reescrever a peça 01 §5.5 a partir do capítulo de dano da candidata, e as remissões das peças 12, 15, 20 e 24. Antes, rodar o `conferir-atributos.py` numa cópia com a regra nova para ver quais checagens medem a regra antiga, e trocá-las por checagens da regra nova com teste negativo. Não apagar checagem para passar.
4. **Equipamento e munição** (peças 14, 16, 21), *feito na v0.335, ver a seção do passo 4,* depois **Invocações** (peça 15, que conversa com `invocacoes/`), depois **Caminhos** (peça 06 e `RASCUNHO-trilhas`, que hoje não têm Fluidez nem Malabarista).
5. **Criação, Fundamento e Catálogo** (peças 08, 17, 18). É o maior volume e o que mais toca a ficha. *Primeira parte feita na v0.337 (ver a seção dela, acima): os validadores leem o livro. A segunda, na v0.338, deu dono às tabelas de mestre e tirou do gerador as leituras do Fundamento; o `manual/gerador`, o `.docx` e o `.pdf` vão para o arquivo com a migração dos Poderes avançados.*
5a. **O inventário da revisão do R41.** *Feito na v0.342: `INVENTARIO-REVISAO-R41.md`, ao lado deste plano.* Ele entrou antes do capítulo de Dano porque muda o que os capítulos seguintes têm de copiar, e deixou três frentes, nesta ordem: as regras novas e os desfeitos que já têm peça; a troca da fonte dos validadores, da candidata para o R41; e os capítulos que faltam do 5b, já lendo o R41.
5b. **Os seis capítulos sem passo** (ver a seção deles, acima): *um por versão. O de Dano sem o Morrendo foi feito na v0.347; faltam Regras gerais, Poderes avançados e Ritual e Pactos.*
6. **Geradores.** `gerador-ficha` e `gerador-inimigo`. O `manual/gerador` (o `.docx` do Fundamento v7) não é regerado: vai para o arquivo no passo 5. O gerador do livro antigo (`livro/build/`) só muda se a candidata não substituir o `livro/manual/`.
7. **Fichas**, por último e em outro ambiente (seção abaixo).

## O livro final passou a ser o R41 (v0.341, 09/10/2026)

**O que mudou no chão deste plano.** *Até a v0.340 a migração copiava a candidata para as peças, e o livro final (R28a) era a candidata com outra diagramação.* **Desde a v0.341 o livro final é o R41, e ele tem regra que a candidata não tem.** Entre 07 e 09/10 o Mizuki reviu, por número, o que a reconstrução tinha mudado na mecânica em relação ao livro v0.331. O resultado está em `../../ciclo-maldito-r41/revisao-de-regras/`.

As decisões caem em três casos, e cada um pede uma coisa diferente das peças:

- **Voltou ao valor da v0.331 e a peça nunca saiu dele.** Nada a fazer na peça; o registro do inventário daquela mudança deixa de ser `confirmada` e passa a não migrar.
- **Voltou ao valor da v0.331 e um passo já tinha migrado a mudança** (passos 4, 5 e 5b, v0.335 a v0.340). A peça e o validador dela voltam, com teste negativo.
- **Regra nova, que nem a v0.331 nem a candidata têm.** *Arma, uniforme, escudo e carga sem a Força pedida (itens 156 a 158), a Reação de `Cobrir-se de Energia` e de `Defesa sem Armadura` tirando só a proteção passiva (160) e as Bênçãos `Represália` e `Sangue Frio`.* Entram na peça dona como qualquer decisão.

**O passo 5a foi montar essa tabela antes de tocar em peça** (`INVENTARIO-REVISAO-R41.md`): uma linha por decisão, com a peça dona, o caso e o quanto cada linha foi conferida. Sem ela, os capítulos que faltam do passo 5b seriam copiados de uma candidata que o livro já desmentiu.

**A candidata fica guardada como está.** *Ela foi a fonte que os validadores liam pelo `03-mecanica/livro.py` da v0.337 à v0.345.* **Na v0.346 a fonte passou a ser o `LIVRO-COMPLETO.md` do R41,** *anunciada ao Mizuki como a versão seguinte e liberada por ele ("verifica e siga"). O inventário tinha medido o tamanho numa cópia isolada (22 dos 27 validadores passando sem mudança); na troca de verdade, quatro precisaram de ajuste.* **Daqui em diante, "migrar um capítulo" é comparar a peça com o R41, e não com a candidata.**

**Fora do livro e fora deste passo:** a seção C do `MUDANCAS-DE-REGRA.md` (direção dada, sem número) e as regras de XP de 01/10/2026 (Solo simples e Solo complexa, o multiplicador e o arredondamento em múltiplos de `12,5`), que a ficha já segue e o R41 ainda não.

## O livro final, Ciclo Maldito R28a

*Comparado em 05/10/2026, na v0.333.* O PDF do Mizuki (`Ciclo Maldito | Livro de regras`, 498 páginas, gerado pelo mesmo ReportLab da candidata) foi lido inteiro e comparado com o `LIVRO-COMPLETO.md` de antes da D43, em trechos de seis palavras para atravessar a diagramação em colunas. **3.787 dos 3.966 parágrafos da candidata estão inteiros nele, e os que não estão são lista quebrada pela diagramação, o glossário antigo (reescrito, mais curto), a seção Referências e adaptação e as folhas de ficha em branco.** O que ele tem a mais é apresentação: o nome, a página de consulta de cada capítulo, três esquemas (cobertura, percurso e a janela de queda), os créditos das imagens e o link da ficha digital. **Nenhuma regra difere, e a D43 não está nele** (a Kaori e o Iori ainda aplicam a condição no acerto). A candidata continua sendo a fonte das peças; o R28a precisa receber a D43 pelo gerador dele, que não está neste repositório.

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
