# Ciclo Maldito R41

O livro principal do repositório desde a v0.341. O PDF fica uma pasta acima, em `Ciclo-Maldito-Livro-de-Regras.pdf` (373 páginas). Aqui fica o que o produz e o que explica as regras dele.

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
