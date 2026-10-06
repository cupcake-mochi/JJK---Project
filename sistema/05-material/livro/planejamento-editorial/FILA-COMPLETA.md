# Fila — estado vigente em 06/10/2026 (v0.339)

A reconstrução do livro está concluída (tabela de unidades abaixo, de 03/10). **A fila que anda agora é a da migração da candidata para as peças**, descrita em `migracao-pos-candidata/PLANO.md` e resumida em `sistema/ESTADO-ATUAL.md`.

Livro principal desde a v0.339: **Ciclo Maldito R28a** (`05-material/livro/Ciclo-Maldito-Livro-de-Regras.pdf`, 498 páginas). A candidata, que já tem a D43 e a D44, é a fonte das peças.

**Feito:** passos 1, 2 e 4 (321 registros conferidos, renomes, equipamento/Invocações/Caminhos) e o passo 5 em duas partes (validadores leem o livro; `.docx` fora de fonte).

**Próximo, nesta ordem:**
1. Capítulo de Dano sem o Morrendo, incluindo o 15º tipo, `Força` (o livro tem 15 tipos; as peças 01 e 19 têm 14).
2. Passo 5b, um capítulo por versão: Ritual e Pactos (29 registros), Poderes avançados (21, com o `conferir-expansao` e o `partE.js`), Regras gerais (19), Origens (18), Rotas (14), Aptidões e Refino (13).
3. O R28a recebe a D43 e a D44 pelo gerador dele (lista em `R28a`, commit 3bb0626).
4. Passo 6: `gerador-ficha`, `gerador-inimigo` e as fichas pessoal e maldita.
5. Passo 3 (vida a zero): espera a revisão do Morrendo, que o Mizuki adiou. Os registros travados não migram até lá.

Pendência pequena: na candidata, o exemplo da Abre Ferida está depois da Firmeza, com a Sobrecarga no meio.

Teste com leitores (`testes-com-leitores/PLANO.md`) segue preparado, sem execução.

---

## Histórico: fila da reconstrução — concluída

Atualizada em03/10/2026. A candidata editorial completa está em `consolidacao/lote-01`. A publicação v0.331 não foi substituída.

| Unidade | Fonte editável | Estado |
|---|---|---|
| ab | `abertura/lote-01/ABERTURA-E-CRIACAO.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| geral | `regras-gerais/lote-final/REGRAS-GERAIS.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| dano | `dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| origens | `origens/lote-01/ORIGENS-E-LEGADOS.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| pericias | `pericias-e-oficios/lote-01/PERICIAS-E-OFICIOS.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| equip | `equipamento/lote-final/EQUIPAMENTO.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| progressao | `progressao/lote-01/PROGRESSAO.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| fundamento | `fundamento/lote-01/FUNDAMENTO.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| catalogo | `catalogo/lote-01/CATALOGO.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| aptidoes | `aptidoes/lote-01/APTIDOES-E-REFINO.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| rotas | `rotas/lote-01/ROTAS.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| poderes | `poderes-avancados/lote-01/PODERES-AVANCADOS.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| ritual | `ritual-e-pactos/lote-01/RITUAL-E-PACTOS.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| campo | `invocacoes/lote-01/INVOCACOES-EM-CAMPO.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| construcao | `invocacoes/lote-02/CONSTRUIR-INVOCACOES.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| fabricacao | `invocacoes/fabricacao/lote-01/FABRICACAO-DE-ENTIDADES.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| consulta | `consulta/lote-01/CONSULTA.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| bastiao | `caminhos/bastiao/lote-01/BASTIAO.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| vanguarda | `caminhos/vanguarda/lote-01/VANGUARDA.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| guia | `caminhos/guia/lote-01/GUIA.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| emanador | `caminhos/emanador/lote-01/EMANADOR.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| evocador | `caminhos/evocador/lote-01/EVOCADOR.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |
| incursor | `caminhos/incursor/lote-01/INCURSOR.md` | Revisada e integrada; V01–V15 e fechamento rastreados. |

A montagem, os nomes, as interfaces, a inspeção visual, o preflight e a documentação estão concluídos. PDF único e ZIP compõem a entrega.

A próxima fase é revisão do autor e testes com leitores/jogadores. Não faz parte de uma validação humana já realizada. Prioridades sugeridas: queda/socorro, uso de invocações, Fluidez/continuações e equipamento. Veja `consolidacao/lote-01/REVISAO-FINAL.md`.
