# Ciclo Maldito R41, hoje na edição R49

**Desde a v0.362 o PDF é o do R49, com o mesmo texto do R47:** *o R48 e o R49 mudam só a diagramação (dois arquivos do gerador), e os registros `R47-para-R48.json` e `R48-para-R49.json` vêm vazios.* **Desde a v0.361 o texto desta pasta é o R47:** *o R46 com um bloco mudado, o do Ataque sem Prenúncio (item 194: o anúncio vem depois da escolha entre Defesa e Bloquear). O registro é `revisao-de-regras/alteracoes/R46-para-R47.json`.* **Na v0.360 foi o R46:** *o R44 com as Origens refeitas (R45, cinquenta e dois blocos, item 193: cada Origem dá uma marcante e duas menores) e com um título sem "(continuação)" (R46). Os registros são `revisao-de-regras/alteracoes/R44-para-R45.json` e `R45-para-R46.json`, e o que veio da integração das Origens está em `revisao-de-regras/origens-r45/`.* **Na v0.359 foi o R44:** *o R43 com vinte e cinco blocos mudados, dos itens 24, 33, 40, 46, 101, 151 e 188 a 192 (reparo, criação de entidades, pactos, Melhorias de Ritual e Cortina). O registro é `revisao-de-regras/alteracoes/R43-para-R44.json`.* **Da v0.357 à v0.358 foi o R43:** *o R42 com seis blocos mudados, todos do item 187 (Bloquear é escolhido antes da rolagem de acerto, e o novo alvo do `Redirecionar a Força` usa só a Defesa). O registro é `revisao-de-regras/alteracoes/R42-para-R43.json`.* **Da v0.354 à v0.356 foi o R42:** *o R41 com dois blocos mudados, os dois do item 186 (a `Promessa` não ocupa vaga de pacto, e quem tem Essência 0 ou 1 pode firmar uma). O registro é `revisao-de-regras/alteracoes/R41-para-R42.json`.* **A pasta guarda o nome da edição em que nasceu,** *e as peças, os validadores e os registros continuam chamando o livro de R41; tudo o que eles dizem do R41 vale para o R42, fora esses dois blocos.*

O livro principal do repositório desde a v0.341. O PDF fica uma pasta acima, em `Ciclo-Maldito-Livro-de-Regras.pdf` (397 páginas). Aqui fica o que o produz e o que explica as regras dele.

## O que tem aqui

- `LIVRO-COMPLETO.md`: o texto inteiro, na ordem do PDF, em 521 blocos. Cada bloco abre com uma âncora `<a id="capitulo--bloco"></a>`, e é por ela que os registros de alteração apontam um trecho.
- `fontes-editoriais/`: os manuscritos dos capítulos de onde o gerador parte. **Eles não são o texto final:** *as rodadas depois do R30 são aplicadas pelos scripts de revisão do gerador (`gerador/revisao_r41.py` e os anteriores) na hora de gerar, então uma regra pode estar no `LIVRO-COMPLETO.md` e não estar aqui (a `Represália`, por exemplo). Para ler regra, use o `LIVRO-COMPLETO.md`.*
- `gerador/`: os scripts que montam e conferem o PDF, com os arquivos de configuração pequenos. **Ele não roda só com o que está aqui:** a arte da capa e das aberturas, as referências ilustradas e as fontes tipográficas ficaram na pasta de entrega do Mizuki, fora do repositório, junto com as páginas renderizadas e as evidências de cada rodada.
- `revisao-de-regras/`: o porquê das regras.

## De onde ele veio

O R28a, que era o livro principal desde a v0.339, recebeu 74 retoques de redação e virou o R29. Em 07/10/2026 o Mizuki abriu a revisão do que a reconstrução tinha mudado na mecânica em relação ao livro v0.331: cada mudança ganhou um número, e ele respondeu por número se ela ficava ou voltava. O R30 aplicou as respostas. Do R31 ao R40 o livro mudou de diagramação (duas colunas, menos páginas, sumário em três páginas, a habilidade de Caminho com o nome no título e o nível em linha própria) e recebeu as correções de cada pente fino. O R38 trouxe duas Bênçãos novas, `Represália` e `Sangue Frio`, e o R39 e o R41 as acertaram.

## Os registros

- `revisao-de-regras/MUDANCAS-DE-REGRA.md` é a lista decidida, escrita para quem aplicava no livro. A seção A é o que mudou, a B o que já estava decidido antes e faltava no R29, e a C o que tem direção e ainda não tem número. **A seção C não está no livro.**
- `revisao-de-regras/DECISOES-MIZUKI.md` guarda as respostas dele na ordem em que vieram, com as palavras dele, e o que ficou em aberto.
- `revisao-de-regras/LISTA-v1-numerada.md` e `SEGUNDA-PASSADA.md` são as duas passadas de comparação com o livro v0.331 que deram os números.
- `revisao-de-regras/alteracoes/` tem um arquivo por rodada que mexeu em texto, com o bloco, o antes e o depois. Cada rodada foi conferida do mesmo jeito: todo bloco diferente entre duas versões tem de estar no registro, e o antes e o depois têm de bater com o livro.
- Os `PENTE-FINO-*.md` são as conferências de cada entrega, e o `MEDIDA-represalia-sangue-frio-2026-10-09.md` é a conta das duas Bênçãos novas. O `GUARDADO-orientacao-de-servidor-v0331.md` é texto do livro antigo que saiu e que ele pediu para guardar.

## Quem lê este livro

Desde a v0.346 os validadores de `sistema/03-mecanica/` leem o `LIVRO-COMPLETO.md` daqui, pelo `livro.py`, que remonta cada capítulo a partir das âncoras de bloco. Da v0.337 à v0.345 eles liam a candidata, em `planejamento-editorial/`, que não recebeu a revisão e fica guardada. **Mexer na forma deste arquivo (âncoras, níveis de título, a linha de preço das entradas do Catálogo) é mexer no que os validadores leem.** O plano da migração diz o que falta para as peças chegarem aqui.

As duas Bênçãos novas não passaram por mesa.
