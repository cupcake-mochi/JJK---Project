# Publicação no GitHub — 2026-10-03

Entrega preservada como candidata, separada do manual v0.331. PDF, 23 fontes e CRC do ZIP final foram conferidos na cópia de publicação. Os registros da revisão editorial final estão em ../consolidacao/lote-01/REVISAO-FINAL.md.

O verificador legado conferir-repositorio.py encontrou 166 problemas de referências na árvore ampliada. O relatório integral está em conferencia-repositorio.txt. Essa checagem geral não está aprovada e exige revisão própria dos ponteiros de planejamento e histórico; não se confunde com as 3492 checagens estruturais da candidata.

A publicação usou uma cópia limpa do repositório porque o Git do HD externo apresentou erro de leitura em .git/objects/40. Nenhum arquivo de trabalho foi removido. Imagens PNG de conferência e pacotes de continuidade antigos permanecem somente no ambiente local, conforme .gitignore.

Revisão de 04/10/2026: as referências foram examinadas uma a uma em `MANUTENCAO-REFERENCIAS-2026-10-04.md`. Num clone limpo eram 182, e não 166, porque 16 caminhos em /tmp só existiam na máquina que rodou a conferência. Dos 182, 14 eram defeitos reais e foram corrigidos; 131 eram limitação do verificador, que agora resolve caminhos relativos a pastas acima do documento; 37 apontam arquivos temporários ou locais fora do git e viraram aviso. O resultado novo está em `conferencia-repositorio-2026-10-04.txt`: 0 referências mortas e 37 avisos.
