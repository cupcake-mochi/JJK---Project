# Anatomia comparada — como manuais publicados organizam o livro inteiro

Pesquisa direta em seis livros publicados, lidos em PDF (amostragem de sumário + capítulos representativos, não o livro inteiro). Cada achado cita o livro e a página — se um dia a recomendação parecer errada, é mais fácil checar a fonte do que checar a memória de quem escreveu isto.

**Os seis livros:**
- **D&D 5e 2024, Livro do Jogador (PHB)** — mainstream, regra core + catálogos, 397 págs.
- **D&D 5e, Guia do Mestre (DMG)** — o mesmo sistema, só a metade que o jogador não lê, 322 págs.
- **D&D 5e, Caldeirão de Tasha para Tudo** — suplemento com regra opcional, 162 págs.
- **D&D 5e, Guia do Volo para Monstros** — bestiário, catálogo de dezenas de entradas parecidas.
- **3D&T Alpha** (Marcelo Cassaro, Jambô) — sistema **brasileiro**, português nativo, não é tradução.
- **GURPS 4ª edição** — sistema genérico por **orçamento de pontos**, o parente mais próximo de um sistema como o RPG da Guilda.

Nenhum destes é ambientação de Jujutsu Kaisen nem sistema de orçamento de pontos idêntico ao seu — são referência de **método**, não de conteúdo. Adapte, não copie.

**Mais dois, de fonte secundária (busca e resenha, não leitura direta do PDF — sinalizado onde usados):**
- **Cairn RPG, 2ª edição** — sistema minimalista/OSR, licença CC-BY-SA, o exato oposto de escala dos seis acima.
- **Mausritter** — sistema minimalista/OSR, livro core de 48 páginas.

Os seis primeiros são todos produção grande — mesmo o 3D&T, mais modesto, tem 146 páginas e uma editora por trás. **Nenhum representa a escala real de um projeto pequeno, com um ou dois autores e manual gerado por script** — que é o caso mais comum de quem usa esta skill. Cairn e Mausritter fecham esse buraco: são a prova de que os padrões abaixo não são luxo de editora grande.

---

## 0. A separação jogador/mestre e o índice de referência sobrevivem em livro pequeno

Achado que resolve a maior dúvida em aberto desta pesquisa: será que "GM content separado" e "índice de referência no fim" são práticas que só cabem numa produção de centenas de páginas?

- **Cairn** resolve a separação jogador/mestre da forma mais extrema possível: **dois livretos físicos separados**, Player's Guide e Warden's Guide, cada um por volta de 24 páginas — a mesma decisão do D&D (PHB vs. DMG), só que num décimo do tamanho.
- **Mausritter**: um livro só, 48 páginas, mas com a mesma fronteira interna do GURPS — a seção do jogador é claramente os primeiros ~20, a do mestre vem depois. E ele fecha com **"uma referência de regras compreensiva"** no final — a mesma função da tabela de resumo de uma página que a `redacao-acessivel-rpg` já recomenda na posição 8 da estrutura de material completo.
- **Mausritter**, catálogo de monstro: stat block de **uma linha só** por criatura ("Rato: 3hp, FOR 9, DES 9, VON 9. Ataques: d6 espada ou d6 arco") — a densidade mínima possível, e ainda assim funcional.

**Conclusão prática:** a separação jogador/mestre e o índice de referência não são luxo de produção grande — são decisão de arquitetura que vale em qualquer escala, só muda o tamanho físico de cada lado. Não existe desculpa de "é pequeno demais pra separar" ou "é pequeno demais pra ter índice".

---

## 1. Quick-start / entrada do leitor novo

Nenhum dos seis livros usa uma caixa "quick-start" separada e isolada. O quick-start **é** o primeiro capítulo, e ele é sempre um **exemplo trabalhado**, nunca um resumo abstrato:

- **D&D PHB** (p.7): cena de mesa dramatizada, com falas nomeadas e um teste de dado real acontecendo ("Felipe (jogando um d20): Aff. Sete."). É o único trecho do livro com uma jogada "ao vivo" em texto corrido.
- **3D&T Alpha** (p.16-19): oito passos numerados que constroem uma ficha de personagem (Tasha) junto com o leitor, narrando as decisões em primeira pessoa do plural, terminando na ficha preenchida.
- **Ironsworn** (fonte: artigo especializado sobre design de manual de RPG, corroborado por busca — não lido em PDF): quick-start de 32 páginas logo na abertura, e o livro **diz explicitamente pra que serve cada capítulo** ("this chapter is for referencing, not for reading straight through").

**Padrão convergente:** o capítulo 1 constrói algo real (uma ficha, uma cena) em vez de descrever o sistema em abstrato. **Nuance:** 3D&T e Ironsworn dão um atalho explícito pra quem já manja de RPG pular o tutorial — vale considerar se o público do seu manual precisa disso.

## 2. Jargão e glossário

Dois mecanismos que convivem, não competem:

- **D&D PHB**: termo com Capitalização própria, usado no corpo desde a primeira menção sem parênteses — e um aviso explícito na p.7 avisando que existe um glossário no Apêndice C se o termo não ficou claro. O glossário final tem convenção documentada no próprio topo dele (como ler uma entrada do glossário).
- **GURPS** (p.7): termos-chave centrais (como "ponto", a moeda do sistema inteiro) ganham um **glossário-ponte de uma linha, antes até do Capítulo 1**, com referência cruzada de página — o leitor não precisa esperar chegar no capítulo técnico pra saber o que "ponto" quer dizer.
- **3D&T**: separa em dois glossários por natureza — um de vocabulário de **cultura** (termos otaku, p.10-12) resolvido de saída, e jargão **mecânico** definido no ponto de uso com remissão cruzada sempre que reaparece antes da explicação formal.

**Padrão convergente:** definir no corpo na primeira aparição + glossário à parte como rede de segurança (isso já é o que a `redacao-acessivel-rpg` recomenda). **Achado novo:** quando existe um conceito **central** que todo o resto depende (ponto no GURPS; aqui seria "refino" ou "Fundamento"), ele merece um glossário-ponte de uma linha **antes** do capítulo técnico — não só a definição no corpo, no meio do primeiro uso.

## 3. Formato de uma entrada de catálogo

- **D&D PHB**: cada TIPO de entrada (talento, magia, item) ensina o esquema de campos ANTES da lista — um bloco "Partes de um Talento" nomeando Categoria/Pré-requisito/Benefício/Repetível, na ordem exata que as entradas vão seguir.
- **GURPS**: ordem rígida e repetida em centenas de entradas — Nome → Custo isolado em linha própria → efeito em prosa → Ampliações Especiais → Limitações Especiais, sempre nessa ordem.
- **D&D DMG** (item mágico): Nome em caixa alta → linha de metadados em itálico (categoria/raridade) → prosa livre com propriedades em negrito inline quando o item tem múltiplos efeitos.
- **3D&T**: mais solto — Nome (custo) + parágrafo em 2ª pessoa que já mistura flavor e regra no mesmo texto, sem separar em campos.

**Padrão convergente:** ensinar a gramática da entrada **uma vez**, antes da primeira entrada real, nunca repetir os rótulos em toda entrada. **Divergência que importa:** a rigidez do formato escala com o quanto o sistema é matemático — GURPS (pontos) é rígido, 3D&T (mais narrativo) é solto. Um sistema de orçamento de pontos como o seu deveria puxar mais para o lado GURPS/D&D do que para o lado 3D&T.

## 4. Catálogo em escala — muitas entradas parecidas

Pesquisa feita especificamente no Guia do Volo (bestiário), porque nenhum dos outros cinco livros tem esse problema no mesmo tamanho.

- **Agrupamento**: não é alfabético puro — o livro organiza por **famílias** (Bruxas, Gigantes, Goblinóides...) com subagrupamento por subtipo dentro de cada família. A ordem alfabética/por-nível só aparece nos índices de apoio, não no corpo.
- **Índice duplo**: um índice alfabético logo após o sumário (nome → página) **e** um segundo índice, num apêndice, reindexando tudo por um eixo funcional diferente (nível de desafio, tipo, ambiente) — "permite pesquisar blocos estatísticos por classificação de desafio, tipo de criatura e ambiente."
- **Variante como base + delta**: uma entrada muito parecida com outra não é reescrita — o livro escreve a regra-base uma vez e a variante só lista **a diferença**, com ponteiro explícito de volta pra base ("tem as mesmas estatísticas de X, exceto que...").
- **Esqueleto de seção fixo repetido**: cada família de monstro segue a mesma ordem de subseções (comportamento → interpretação → subtipos → covil → tesouro → tabelas), então o leitor aprende a navegar uma família e já sabe navegar todas.
- **Separação tipográfica flavor/crunch**: citações de lore ficam em caixas visualmente isoladas, sinalizando "pulável" pra quem só quer o stat block.

**Padrão a aplicar direto:** um catálogo de 50+ entradas parecidas precisa de índice duplo (nome + eixo funcional) e da convenção "base + delta" pra variante, ou ele vira ilegível na mesa por puro volume — não é problema de prosa, é problema de navegação.

## 5. Regra opcional / variante

- **GURPS**: rótulo fixo "**Regra Opcional:**" antes do nome, indexado **desde o sumário** — o leitor escaneia o índice e decide com antecedência quais módulos vai usar, sem precisar abrir o capítulo.
- **Tasha's**: declaração única, uma vez, no topo do livro inteiro ("Tudo neste livro é opcional") — não repete o aviso capítulo a capítulo. Quando uma opção específica depende de outra regra opcional já existente, a dependência é declarada localmente, no ponto de uso ("se seu grupo usa X").
- **D&D DMG**: convenção tipográfica fixa "**VARIAÇÃO:**" isolando regra alternativa do procedimento padrão, sempre com um exemplo numérico mostrando a variação funcionando.

**Padrão convergente:** três mecanismos diferentes, mas a regra de fundo é a mesma — **rotular uma vez, no nível certo** (livro inteiro, capítulo, ou entrada pontual, dependendo da abrangência), nunca espalhar aviso frase a frase. Quanto maior o escopo do "opcional", mais alto na hierarquia do documento o aviso deve morar.

## 6. Separação jogador vs. mestre

- **D&D**: dois livros inteiros, fisicamente separados. O Guia do Mestre presume abertamente que o leitor já leu o do jogador ("o DMG assume que você conhece o básico... a tabela resume esse material") e nunca reexplica mecânica core, só reaproveita e cita a página de origem.
- **GURPS**: um volume só, mas com "Livro 1 — Personagens" / "Livro 2 — Campanhas" como fronteira interna clara, paginação contínua.
- **3D&T**: "O Mestre" é deliberadamente o **último** capítulo do livro — o sistema inteiro é escrito pensando primeiro no jogador novato.

**Padrão convergente:** conteúdo de mestre nunca se intercala frase a frase com regra de jogador — ele fica depois, numa fronteira clara (livro separado, parte separada, ou capítulo por último), com no máximo uma seção simétrica curta ("Sendo um Jogador" / "Sendo um Mestre") logo no capítulo 1 pra dar o contexto dos dois papéis.

## 7. Justificativa de design vs. regra

- **GURPS**: boxes nomeados e recorrentes ("Como o GURPS Funciona") param a regra pura e explicam a intenção de balanceamento por trás do número — sempre isolados da regra, nunca misturados no mesmo parágrafo.
- **D&D PHB**: mesmo princípio, num quadro dedicado ("Exceções Sobrepõem Regras Gerais") — a regra de arbitragem em si é separada visualmente do exemplo que a prova.

**Padrão convergente, e é o mesmo que a `redacao-acessivel-rpg` já corrigiu por feedback direto**: justificativa de design mora numa caixa própria, nomeada, nunca dentro do parágrafo que carrega a regra jogável. Os livros publicados confirmam que a correção estava certa — não foi só gosto de quem deu o feedback.

## 8. Densidade matemática (sistemas por orçamento de pontos)

Só o GURPS serve de referência direta aqui, e vale ler o achado com ressalva: **ele às vezes afunda mesmo**. A entrada de Compulsão cruza três variáveis numa tabela só pra uma desvantagem; a densidade cognitiva por página é real, o livro não esconde isso.

O que ele faz pra mitigar (e vale copiar), mesmo não sendo perfeito:
- **Empilhamento incremental**: cada conceito matemático (custo base → nível → ampliação % → limitação % → modificador) é ensinado isolado antes de aparecer combinado.
- **Regra → exceção → exemplo resolvido**, quase sempre nessa ordem, com o exemplo às vezes repetido como citação de destaque.
- **Cross-reference extensivo**: quase toda frase técnica termina em "v. pág. X", pra o leitor nunca precisar segurar duas fórmulas na cabeça ao mesmo tempo.

**Leitura honesta:** GURPS é o exemplo mais próximo do que este projeto precisa, e também é o exemplo mais claro de "onde a densidade vence o leitor". Vale estudar os dois lados — o que funciona e o ponto exato em que ele deixa de funcionar.

## 9. Registro de língua / voz nativa

Único achado que não vem de contraste entre livros, vem de um livro só: **3D&T é o único original em português desta lista**, e isso muda o que dá pra aprender dele que os outros não ensinam.

- Interpela o leitor com pergunta retórica e reage à própria pergunta.
- Expressões idiomáticas brasileiras genuínas dentro de texto técnico ("em casa de ferreiro, espeto de pau", "feito mula") — nenhuma tradução do inglês teria isso.
- Assinatura de autor com apelido no fim da abertura — tom de comunidade, não de compêndio impessoal.
- Usa vocabulário do próprio gênero (mangá/anime, "tsuzuku") como termo técnico de mesa, em vez de inventar um termo genérico.

**Padrão a aplicar direto**: quando o sistema tem tema próprio (aqui, Jujutsu Kaisen — energia amaldiçoada, técnica), reaproveitar o vocabulário do próprio tema em vez de emprestar vocabulário genérico de fantasia é exatamente o que 3D&T faz e os livros traduzidos do inglês não conseguem fazer. Esse achado já virou correção na `redacao-acessivel-rpg` a partir de feedback direto — aqui está a confirmação de que é prática real, não só gosto pessoal.

---

## Nota de honestidade sobre esta pesquisa

Cada livro foi amostrado — sumário completo + 2-3 capítulos representativos, não o livro inteiro. As citações são reais (página + trecho, quando o texto extraído permitiu), mas um achado "sempre X" aqui significa "visto consistentemente nas amostras lidas", não "confirmado em cada uma das centenas de páginas". Se uma recomendação daqui parecer errada na prática, o primeiro passo é reabrir a fonte citada, não descartar o achado.

Dois PDFs ficaram de fora por tamanho (Pathfinder 2e, 265 MB) ou cobertura parcial (Guia do Volo, só 24 páginas — não chegou nos stat blocks de fato, só na arquitetura de navegação). Se um dia a pesquisa precisar de mais fôlego em "sistema com matemática ainda mais exposta que GURPS" ou "layout de stat block completo", esses dois são os próximos a buscar.

**Cairn e Mausritter (seção 0) são fonte mais fraca que os outros seis**: vieram de busca web e resenha de terceiros, não de ler o PDF. A rede deste ambiente bloqueia acesso direto a `cairnrpg.com` e a hosts de PDF de RPG em geral, então não deu pra confirmar por leitura direta. Os achados citados (livretos separados no Cairn, ~48 páginas e stat block de uma linha no Mausritter) vieram de múltiplas fontes secundárias concordando entre si, o que dá alguma confiança — mas se algum dia importar precisão de página exata desses dois, vale conseguir o PDF de verdade primeiro.

**Fontes da seção 0:**
- [Cairn RPG — site oficial](https://cairnrpg.com/) — estrutura em Player's Guide / Warden's Guide, licença CC-BY-SA 4.0
- [Cairn RPG — Second Edition](https://cairnrpg.com/second-edition/) e [Warden's Guide](https://cairnrpg.com/second-edition/wardens-guide/)
- [Mausritter — Prismatic Wasteland, resenha do boxed set](https://www.prismaticwasteland.com/blog/mausritter-boxed-set-review)
- [Mausritter — Gaming Trend, resenha](https://gamingtrend.com/reviews/mausritter-rpg-boxed-set-review-small-box-near-infinite-potential/)
- [Mausritter — Some Notes on Mausritter, The Stochastic Game](https://ludovic.chabant.com/blog/2025/05/18/some-notes-on-mausritter/)
