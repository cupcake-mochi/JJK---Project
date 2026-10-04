# Projeto - M — candidata editorial completa

A reconstrução está reunida em um livro de 382 páginas, revisado em 04/10/2026 (as mudanças desde 03/10 estão em `../../revisao-interfaces/CORRECOES-APLICADAS.md`). A publicação v0.331 foi preservada. A entrega inclui o PDF, o manuscrito único para leitura, os capítulos editáveis, os registros de decisões e as validações.

Abra `output/pdf/Projeto-M-Livro-Completo-Candidata.pdf`. Leia `REVISAO-FINAL.md` para alterações e limites. `VALIDADORES.json` contém o fechamento dos15critérios, e `evidencias/FINAL-V14.json` registra a inspeção das páginas.

## Editar e gerar

Edite os capítulos indicados em `ORDEM.json`. Não edite `LIVRO-COMPLETO.md` como fonte principal: ele é recomposto pelo gerador. A pasta do pacote conserva a estrutura relativa necessária.

Com Python3 e os pacotes reportlab, pypdf e pdfplumber instalados, execute:

```bash
python gerar_livro.py --strict
python conferir_livro.py
```

As fontes tipográficas usadas estão em `fontes-tipograficas`. O gerador calcula as páginas do sumário e dos links até a paginação estabilizar. Alterar conteúdo exige repetir a conferência e inspecionar as páginas afetadas. A geração não deve marcar a revisão visual como aprovada por conta própria.

## Histórico e validações

Os relatórios dos capítulos guardam decisões, testes e provas anteriores. O PDF reunido é a versão vigente desta entrega. Uma prova individual antiga pode ter outra paginação ou uma remissão anterior; `FECHAMENTO-INTEGRACAO.json` de cada unidade registra esse limite. Não misture o PDF de uma prova antiga com o texto atual.

A avaliação por modelos e simulações não substitui leitura humana ou playtest. Livros de terceiros usados como referência não estão no ZIP. Nenhuma imagem de IA foi produzida.
