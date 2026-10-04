# Piloto editorial 2

Proposta de 02/10/2026, sobre as regras da v0.331. O livro publicado não foi substituído. Não há imagens geradas por IA.

## Para ler e revisar

- [Entrada, Kaori e Bastião — PDF, 10 páginas](output/pdf/Projeto-M-Piloto-Editorial-02.pdf).
- [Amostras técnicas — PDF, 11 páginas](output/pdf/Projeto-M-Amostras-Tecnicas-02.pdf): movimento, Malabarista, montagem, entidades, catálogo de perícias e conferência final.
- [Relatório e resultados dos validadores](RELATORIO.md): mudanças, comparação, tratamento dos achados e limites.
- [Organização e fila atualizadas](ORGANIZACAO-E-FILA.md): destino das regras comuns e decisões necessárias.
- [Auditoria das regras básicas](evidencias/regras-basicas.md) e [estudo de F&M](evidencias/comparacao-fm.md).

## Fontes editáveis

[PILOTO.md](PILOTO.md) e [LOTE-TECNICO.md](LOTE-TECNICO.md) geram os dois PDFs. Os HTMLs, estilos e diagramas acompanham o pacote. O catálogo longo continua em duas páginas, com um único marcador; não se evita toda quebra de página indiscriminadamente.

`gerar.py` produz os PDFs com Python, Markdown e WeasyPrint. `verificar.py` confere a entrega no repositório original, usando o inventário da v0.331 e fontes externas a esta pasta. Para usar os PDFs e ler os relatórios não é preciso executar nada. Reconstruir e repetir o cotejo integral exige acesso ao repositório e às dependências. O manifesto do ZIP verifica a integridade do pacote.

Os relatórios de revisão em `evidencias/` preservam os pareceres separados, inclusive ressalvas que foram corrigidas depois. A síntese atual está no relatório principal e na verificação final. A cópia `ORGANIZACAO-E-FILA.md` adapta apenas os links do adendo salvo no planejamento; a continuação do projeto usa esse adendo como fonte da fila.

As referências a capítulos publicados usam títulos ou a numeração da v0.331, nunca a renumeração provisória do plano. Os PDFs de outros sistemas e o livro completo do Projeto M ficam fora deste pacote.

## O que ainda não foi feito

Ainda não houve teste deste piloto com jogadores. A revisão por agentes, as contas e a inspeção visual foram realizadas e documentadas. Salto, queda, terreno difícil, ocultação/detecção, manobras gerais e Estudar possuem lacunas ou conflitos a decidir; os exemplos não criam soluções escondidas. A revisão integral de nomes e textos permanece na fila.
