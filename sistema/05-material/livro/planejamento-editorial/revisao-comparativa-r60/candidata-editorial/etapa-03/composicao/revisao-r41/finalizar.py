from pathlib import Path
import json
B=Path(__file__).resolve().parents[1];R=B/'revisao-r41'
def read(p):return json.loads(p.read_text())
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
c=read(R/'CONFERENCIA.json');g=read(B/'evidencias/CONFERENCIA.json');assert not c['problemas'] and not g['problemas'];assert c['sha256_pdf']==g['sha256_pdf']
pages=c['paginas_com_composicao_diferente'];assert pages==[132,139,140,147,148,294,297,298]
save(R/'REVISAO-VISUAL.json',{'sha256_pdf':c['sha256_pdf'],'paginas':[{'pagina':p,'imagem':f'paginas/pagina-{p:03d}.png','resultado':'Página renderizada e inspecionada ampliada; sem corte, sobreposição ou abertura isolada introduzidos nesta rodada.'} for p in pages],'demais_paginas':'365 páginas conservam os mesmos eventos de composição da R40. Capa, arte, fontes e tamanhos preservados.'})
report=f'''# R41 — Acertos no Evocador e nas Bênçãos

Entrega de 09/10/2026. Base: cópia independente da R40, preservada integralmente. Livro com **373 páginas**, sem mudança na contagem. Sem commit nem push.

## Aplicado

1. **Evocador, progressão do nível 7 (p. 132):** agora lista Dificultar a Resistência, Ajustar a Preparação, Recolher sob Ataque e Atuação Complementar. Nenhuma capacidade nova foi concedida.
2. **Nomes do Evocador (pp. 139 e 147):** títulos usam “Intervenções da Invocação Principal” e “Intervenções do Conjunto”, conforme as tabelas existentes. Os contextos de continuação acompanham a padronização.
3. **Represália (p. 297):** uso apenas fora do próprio turno; requisito Força 4 ou Destreza 4, também na tabela Escolhas disponíveis (p. 294). Mantidos CE 2, 1,5 m, resolução posterior ao gatilho, ausência de interrupção e a regra de que manter efeito ativo não oferece novo gatilho.
4. **Domínios (p. 297):** uma frase em cada Bênção exclui abertura/manutenção de Expansão de Domínio e Acerto de Expansão incompleta; feitiços conjurados dentro de um domínio continuam contando.
5. **Sangue Frio (p. 297):** repetição com um único d20, sem a vantagem da Bênção; CD e modificadores mantidos. Permanecem CE 3, Constituição 4, vantagem no TR inicial contra criatura a até 3 m, uma repetição por cena, resultado obrigatório e exigência de 3 m também na repetição.

## Registros e preservação

- Cinco blocos textuais registrados integralmente com antes/depois em `ALTERACOES-TEXTO.json` e na cópia equivalente `ALTERACOES-REGRAS.json`.
- Nove registros de recomposição em `ALTERACOES-DIAGRAMACAO.json`, incluindo alterações de contexto e deslocamentos decorrentes do texto.
- Nenhuma diferença textual fora desses cinco blocos. Todas as outras Bênçãos permanecem idênticas à R40.
- Nenhum exemplo precisou ser refeito. Os exemplos existentes e seus valores foram preservados.
- Todos os arquivos da R40 comparados com os hashes capturados antes da cópia; nenhuma alteração encontrada.

## Validação

A conferência geral completou **{g['checagens']} verificações**, sem problemas detectados, cobrindo conteúdo dos 500 blocos, extração real do PDF, fontes, margens, sobreposições, remissões e marcadores. Os 177 links das linhas do sumário também foram conferidos individualmente.

As páginas **132, 139, 140, 147, 148, 294, 297 e 298** foram renderizadas e inspecionadas ampliadas. As outras **365 páginas** mantêm os mesmos eventos de composição da R40. As duas Bênçãos estão completas na p. 297. A fonte, seu tamanho, a arte e os créditos foram preservados.

Não há dúvida pendente desta solicitação. Esta validação confirma a aplicação e a apresentação dos acertos; não é um teste de equilíbrio em mesa.

## Próxima etapa

Leitura e aceite do autor sobre a R41. Para eventuais ajustes pontuais de texto e diagramação: GPT-6.1 Sol, esforço alto, como recomendação editorial.
'''
(R/'RELATORIO.md').write_text(report)
(B/'LEIA-ME-R41.md').write_text('''# Ciclo Maldito — R41

Prova de 09/10/2026, com 373 páginas. R40 intacta. Sem commit nem push.

- PDF atual: `output/pdf/Ciclo-Maldito-R41.pdf`.
- Texto atual: `LIVRO-COMPLETO.md`.
- Relatório: `revisao-r41/RELATORIO.md`.
- Antes/depois dos cinco blocos: `revisao-r41/ALTERACOES-REGRAS.json` (equivalente a `ALTERACOES-TEXTO.json`).
- Validação: `revisao-r41/CONFERENCIA.json`, `revisao-r41/REVISAO-VISUAL.json` e `evidencias/CONFERENCIA.json`.

Os arquivos e PDFs de versões anteriores foram mantidos como histórico; a entrega atual é a R41.
''')
p=B.parent/'revisao-entendimento-r31-2026-10-08/FILA.md';s=p.read_text();a='8. Leitura e aceite do autor sobre a R40, especialmente a consulta por nível, o sumário e a continuidade das Trilhas.'
assert a in s
s=s.replace(a,'7G. Concluída na R41: progressão do Evocador no nível 7 completada, dois títulos alinhados às tabelas e acertos autorizados de Represália/Sangue Frio aplicados. Cinco blocos com antes/depois; nove registros de recomposição; oito páginas alteradas inspecionadas. 373 páginas, R40 intacta, demais Bênçãos idênticas e conferência geral sem problemas.\n8. Leitura e aceite do autor sobre a R41, especialmente as duas Bênçãos (p. 297) e os acertos do Evocador.')
s=s.replace('Entrega atual: `entregas/livro-diagramado-r40/LEIA-ME-R40.md`.','Entrega atual: `entregas/livro-diagramado-r41/LEIA-ME-R41.md`.')
s=s.replace('Para analisar os retornos, GPT-6 Astra, esforço alto.','Para ajustes pontuais de texto e diagramação, GPT-6.1 Sol, esforço alto; para retornos com conflitos de regras, GPT-6 Astra, esforço alto.')
p.write_text(s)
print('Relatórios e fila atualizados.')
