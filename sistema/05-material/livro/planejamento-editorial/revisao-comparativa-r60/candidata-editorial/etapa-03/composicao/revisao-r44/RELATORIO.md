# R44 — regras decididas em 12/10/2026

Entregue sobre uma cópia da R43: **373 páginas**, 499 blocos editoriais. Foram aplicados os itens **24, 33, 40, 46, 101, 151, 188, 189, 190, 191 e 192**, incluindo os esclarecimentos do autor. Não restam dúvidas pendentes nesta rodada.

## Registro de texto

`../ALTERACOES-R43-para-R44.json` contém **25 entradas** com id, bloco, antes, depois, motivo e item: 22 blocos existentes modificados, dois removidos e um novo. A comparação integral do `LIVRO-COMPLETO.md` confirma texto idêntico à R43 fora desse registro. O registro usa o texto de cada bloco antes da transformação dos níveis de título para o Markdown consolidado, seguindo o formato das revisões anteriores.

As duas correções adicionais autorizadas no item 189 estão registradas em `construcao--entidades-tipos` e `construcao--entidades-progressao`. A criada acompanha o invocador até o teto de sua Classe, e a domada conserva o nível. Não foi localizada outra frase fora dessas duas que exigisse a mesma correção.

## Conteúdo aplicado

- Reparo por ofício compatível escolhido e registrado na criação; tabelas de recuperação com metade, um terço ou um quarto da vida máxima, conforme a comparação de Classes, sempre para baixo. O socorro mudou apenas o ofício utilizado.
- Criação de entidades condensada; mestre decide disponibilidade, tempo e materiais. Classe, evolução, reconstrução, transferência, herança e fontes de vantagem seguem as decisões do autor.
- Pactos: régua como referência para o mestre; nove exemplos; ganho temporário com preço permanente; Ação Bônus no próprio turno ou Reação fora dele, com gatilho percebido, após os dados e antes das consequências. Promessas exemplificadas sem tamanho de ganho.
- Ritual: dezesseis entradas com coluna Repete; cinco permitem duas compras, com os efeitos adicionais de Alcance, Tamanho e Rerrolagem explicitados.
- Cortina: alcance máximo por Refino, de 150 m, 300 m ou 400 m. Vida de 40 × Refino preservada.

## Exemplos

O exemplo da calígrafa foi ajustado para explicitar a Classe escolhida e o invocador: as CDs **12 e 14** e a aritmética foram preservadas. O exemplo antigo **Talismã de vigia** foi removido conforme solicitado. Foram escritos os **nove exemplos de pacto** fornecidos pelo autor. Rui, reparo do corpo com 31 PV máximos e 8 atuais, Haru, Kaito, Hana e Mei foram preservados.

## Navegação e geração

A seção passou a **Criação de entidades**. O índice foi atualizado em dois blocos do registro principal; o nome gerado no sumário e nos marcadores está registrado separadamente em `ALTERACOES-DE-NAVEGACAO.json`. Glossário e consulta rápida foram conferidos: não havia outra repetição contraditória a alterar.

Os arquivos de geração foram atualizados **somente na cópia R44**. `ALTERACOES-DE-GERACAO.json` e `.patch` registram as mudanças de código. As duas tabelas novas de quatro colunas têm proporções específicas para acomodar o conteúdo. Os exemplos curtos novos de pacto conservam a troca completa na mesma coluna, sem alterar seu texto. Fontes, tamanhos, estilos aprovados, arte e créditos foram preservados.

## Validação

- 329 verificações específicas desta revisão, sem problemas.
- 117918 verificações gerais, sem problemas; 2437 links internos e 184 marcadores conferidos.
- 49 páginas renderizadas e inspecionadas visualmente, incluindo todas as páginas de texto alterado, as recompostas e a navegação. A página 320 também foi examinada ampliada.
- Os 2564 arquivos da R43 mantêm seus hashes originais.
- PDF final: SHA-256 `e921594420eb60383a943bf87bc178b0e9d6e212b747f8bd1d65f772e47b750d`.

O espaço restante da página 321 corresponde ao fim de capítulo, após as quatro Promessas. Esta rodada não redesenhou o restante da diagramação nem realizou teste de mesa de balanceamento.

## Arquivos de entrega

- `../output/pdf/Ciclo-Maldito-R44.pdf`
- `../LIVRO-COMPLETO.md`
- `../ALTERACOES-R43-para-R44.json`
- `CONFERENCIA.json`, `REVISAO-VISUAL.json` e `../evidencias/CONFERENCIA.json`
- `DECISOES-DO-AUTOR.md`

Não houve commit nem push. Nenhum repositório de origem externo à pasta do livro foi sincronizado ou alterado.
