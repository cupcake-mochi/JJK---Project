# Retomada após pausa solicitada

O usuário pediu interrupção para mudar o esforço para Médio devido ao consumo. Não retomar automaticamente antes de nova instrução humana. Agentes maxima e rotas_didatica foram interrompidos; compatibilidade terminou. Não lançar novas revisões integrais redundantes.

## Estado salvo

- Livro reunido: `consolidacao/lote-01/output/pdf/Projeto-M-Livro-Completo-Candidata.pdf`, 383 páginas. SHA256 confirmado: `565e98135d44f9788cb6b4f65054916c094d1b6976ff5dbacd5f5f246ebc1c08`.
- Fonte editável: `consolidacao/lote-01/LIVRO-COMPLETO.md`. 23 fontes, 510 blocos. Prova ainda candidata, não entrega final.
- Conferência automatizada anterior: 3.485 verificações aprovadas; fechamento visual e documental ainda incompleto.
- Compatibilidade concluiu inspeção visual 56–136 e parecer transversal, salvos em `consolidacao/lote-01/evidencias/FINAL-V14-COMPATIBILIDADE.json` e `FINAL-TRANSVERSAL-COMPATIBILIDADE.md`.
- Rotas concluiu inspeção 218–315, salva em `FINAL-V14-ROTAS.json`. Encontrou remissões dependentes de paginação, listadas em `REMISSOES-RELATIVAS.json` (17 ocorrências a avaliar, três falhas confirmadas).
- Maxima estava inspecionando 137–217 e 355–383. Confirmar evidência persistida antes de considerar essa faixa concluída.
- Raiz viu mosaicos 01–12, páginas 1–48. Faltam mosaicos 13–24: 49–55 e 316–354, além de ampliações representativas. Mosaicos em `consolidacao/lote-01/output/mosaicos-root/`; mapa em `consolidacao/lote-01/evidencias/MOSAICOS-ROOT.json`.

## Ajustes concretos para uma única rodada

- P39: parágrafo final curto sozinho antes do capítulo seguinte.
- P110 e123: finais de habilidades isolados, páginas quase vazias.
- P158: Corpo em Harmonia e Nível27 separados do efeito.
- P188: Balestra e introdução separados da tabela.
- P203: Capa Perene e metadados separados da aplicação.
- P364: parágrafo final isolado de Entidades na mesa.
- P367: final da ficha da página366 transbordou; acomodar ficha em uma página.
- Remissões confirmadas: p249 “desta página” em Proteção e apoio inclui outra família; p274 “próxima página” em Voto do iniciante aponta para regra na mesma página; p297 idem para Acerto do domínio. Substituir por títulos/seções estáveis nos documentos donos, registrando o delta. Conferir demais ocorrências no JSON antes de alterar.

## Fechamento restante

1. Completar inspeção visual faltante e reunir achados já feitos, sem repetir leituras concluídas.
2. Corrigir apenas defeitos concretos, gerar uma nova prova e verificar o delta. Reutilizar evidências somente quando identidade ou ausência de impacto estiver comprovada.
3. Finalizar relatórios V01–V15 do livro inteiro e documentação dos 23 donos. Raiz ainda deve fechar manifestos de Dano, Rotas, Campo, Emanador, Evocador e Ritual; Dano também LEIA-ME e método. Perícias recebeu revisão independente real em `pericias-e-oficios/lote-01/evidencias/REVISAO-INDEPENDENTE-ROOT-FINAL.json`.
4. Atualizar fila e estado, produzir ZIP portátil com PDF, fonte editável, geradores e registros de decisões/validações. Não incluir livros de terceiros nem centenas de PNGs no pacote.
5. Entregar links e resumo das mudanças, preservando v0.331. Não declarar teste humano ou conclusão antes de finalizar essas etapas.

Referências adicionais: `consolidacao/lote-01/evidencias/V15-GLOBAL-LEVE.md`, `RESUMO-MUDANCAS-POR-TEMA.md`, `consolidacao/lote-01/migracao-nomes/QA-FECHAMENTO.md`, `FILA-COMPLETA.md` e `ESTADO-RODADA-AUTONOMA.md`. Registros antigos de pendência devem ser conciliados com evidências atuais, sem apagar histórico.
