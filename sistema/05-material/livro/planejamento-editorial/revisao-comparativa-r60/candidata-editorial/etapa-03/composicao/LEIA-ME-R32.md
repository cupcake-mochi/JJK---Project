# Ciclo Maldito — R32, prova de texto

- Livro: `output/pdf/Ciclo-Maldito-R32-Prova-de-Texto.pdf` — 394 páginas.
- Texto integral: `LIVRO-COMPLETO.md`.
- Relatório: `revisao-de-compreensao/RELATORIO.md`.
- Todas as diferenças de texto R31 → R32: `revisao-de-regras/ALTERACOES-REGRAS.json`.
- Conferência dos itens já aplicados: `revisao-de-regras/CONFERENCIA-156-158-R32.json`.
- Dúvidas/preservações: `revisao-de-regras/DUVIDAS.md`.
- Pendências de composição: `revisao-visual/PENDENCIAS-CONTINUIDADE.json`.

A revisão de compreensão (6A) terminou e os estilos aprovados foram aplicados (6B). Esta é uma prova anterior à continuidade (6C) e à inspeção visual integral (6D). Os relatórios de edições antigas copiados junto da base são históricos; o relatório acima descreve o estado atual.

Para gerar, use Python com ReportLab, Pillow, pypdf e pdfplumber e execute `gerar_livro.py`. Confira com `conferir_r32.py` e `conferir_livro.py`. O texto final usa as fontes congeladas, a revisão textual anterior, as substituições da R32 e a estrutura da R31. Sem commit/push.
