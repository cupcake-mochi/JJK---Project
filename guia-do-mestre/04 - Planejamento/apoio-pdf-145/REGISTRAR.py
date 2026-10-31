"""Registrar a composição e a inspeção efetivamente realizadas no lote 145."""
from pathlib import Path
import json,hashlib,os
A=Path(__file__).resolve().parent;R=A.parents[1]
load=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
comp=load(A/'composicao.json');audit=load(A/'conferencia-do-pdf.json');render=load(A/'renderizacao.json')
assert comp['paginas']==audit['paginas']==render['paginas']==383
assert comp['sha256_pdf']==audit['sha256_pdf']==render['sha256_pdf']==sha(R/comp['pdf'])
assert not audit['falhas'] and not audit['diferencas_de_extracao_a_examinar']
expanded=[2,6,27,61,104,105,176,194,206,214,226,236,244,249,380,383]
visual={'registro':145,'pdf':comp['pdf'],'sha256_pdf':comp['sha256_pdf'],'paginas':383,'paginas_inspecionadas':list(range(1,384)),'paineis_inspecionados':render['painel'],'paginas_ampliadas':expanded,'renderizacao':'Todas as páginas em PNG a 97,2 dpi, reunidas em 43 painéis de até nove páginas; mapas e pontos selecionados também abertos como página inteira.','verificacao_independente':'Página 194 também renderizada com Poppler a 110 dpi e inspecionada.','criterios':['Fluxo de leitura da coluna esquerda para a direita','Hierarquia e vínculo dos títulos com o texto','Tabelas sem cortes ou sobreposições e com cabeçalhos repetidos','Mapas, distâncias e legendas legíveis','Parágrafos curtos inteiros, sem divisão para nivelar colunas','Espaços de modelos e finais de unidade diferenciados de falhas de fluxo','Margens, numeração, contraste e rodapé consistentes'],'passagens':[{'prova':1,'paginas':374,'resultado':'Diagnóstico: finais muito curtos, imagem de equipamento em faixa inadequada e abertura de unidade sem reserva suficiente.'},{'prova':2,'paginas':375,'resultado':'Reserva do primeiro parágrafo e imagem em coluna; conferir finais.'},{'prova':3,'paginas':384,'resultado':'Redistribuição de finais e bibliografia consolidada; páginas 1–81 inspecionadas. Imagem de equipamento ainda deixava vazio excessivo; sumário podia oferecer mais caminhos.'},{'prova':4,'paginas':383,'resultado':'Imagem transferida para a passagem de compras, na página 61; sumário com acesso às seções. Nova passagem visual por todas as 383 páginas e ampliações selecionadas.'}],'espacos_remanescentes':'Folhas imprimíveis começam em páginas próprias. Permanecem espaços de preenchimento, respiros de encerramento e diferenças de altura para conservar parágrafos e tabelas inteiros. Não se inseriram imagens apenas para ocupar vazios.','problemas_impeditivos_observados':[],'limite':'Inspeção visual pelo assistente; todas as páginas vistas em painéis, com ampliações selecionadas. Não representa leitura humana externa, inspeção de cada página em tamanho físico de impressão nem prova de equilíbrio.'}
save(A/'revisao-visual.json',visual)
config=load(R/'04 - Planejamento/apoio-leitura-144/arquivos-do-lote.json')
controls=config['controles']+['08 - Diagramacao do Guia/LEIA-ME.md']
report='04 - Planejamento/145-pdf-integrado-e-revisao-visual.md'
for rel in controls:
 p=R/rel;backup=A/'antes'/rel
 assert not backup.exists(),f'Já registrado: {rel}'
 backup.parent.mkdir(parents=True,exist_ok=True);backup.write_bytes(p.read_bytes())
 link=os.path.relpath(R/report,p.parent)
 banner=f'> **Fila vigente - registro 145, 30/10/2026:** PDF integrado atualizado, com **383 páginas**, composto a partir das 99 fontes revistas e inspecionado visualmente por inteiro em painéis, com ampliações selecionadas. [PDF, revisão e estado salvo](<{link}>). Tipografia do livro base, sumário e remissões clicáveis; texto, HTML e regras preservados. **Próximo: comparação editorial final, etapa 8; GPT-6 Astra, esforço extra alto, conforme o plano 98.** Ajustes decorrentes: GPT-6.1 Sol, esforço alto. Gerador do PDF em `apoio-pdf-145`; gerador HTML continua no registro 144. O PDF anterior de 357 páginas permanece intacto. Salvamento local; último GitHub: registro 141.\n\n'
 text=p.read_text().replace('**Fila vigente - registro 144,','**Fila histórica - registro 144,',1)
 first,rest=text.split('\n',1);text=first+'\n\n'+banner+rest.lstrip('\n')
 if rel=='06 - Redacao do Guia/revisao-98/LEIA-ME.md':
  text=text.replace('**Próxima tarefa:** composição do PDF completo com as fontes atuais e inspeção visual de cada página. Depois, comparação editorial final e entrega. **GPT-6.1 Sol, esforço alto.**','**Próxima tarefa:** comparação editorial final e entrega, etapa 8. **GPT-6 Astra, esforço extra alto**, conforme o plano 98; ajustes e consolidação com **GPT-6.1 Sol, esforço alto**. PDF integrado e inspeção visual concluídos no registro 145.')
 if rel=='08 - Diagramacao do Guia/LEIA-ME.md':
  # O restante é documentação histórica, não instrução vigente de reconstrução.
  text=first+'\n\n'+banner+'''Abra o [PDF integrado revisto](output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0-Revisado.pdf). A versão anterior permanece disponível no mesmo diretório, com o nome sem “Revisado”.

Para atualizar o PDF vigente, use [o gerador do registro 145](<../04 - Planejamento/apoio-pdf-145/GERAR-PDF.py>) e siga [as instruções de composição e conferência](<../04 - Planejamento/apoio-pdf-145/LEIA-ME.md>). Ele lê a edição integrada atual; o gerador antigo desta pasta monta uma versão histórica e não deve substituir a entrega revisada.

## Histórico da diagramação anterior

'''+backup.read_text().split('\n',1)[1].lstrip('\n').replace('**Atualização vigente — registro 93','**Atualização histórica — registro 93',1)
 p.write_text(text)
save(A/'arquivos-do-lote.json',{'registro':145,'base_manifesto':5458,'relatorio':report,'controles':controls,'fontes_alteradas':[],'html_alterados':[],'manuscrito_integrado':'06 - Redacao do Guia/edicao-integrada-136','edicao_html':'07 - Edicao de Leitura/edicao-integrada-136','pdf_novo':comp['pdf'],'gerador_pdf':'04 - Planejamento/apoio-pdf-145/GERAR-PDF.py','proxima_etapa':'8 - comparação editorial final','modelo_previsto_no_plano':'GPT-6 Astra, esforço extra alto; ajustes com GPT-6.1 Sol, esforço alto'})
p=A/'LEIA-ME.md';text=p.read_text();text=text[:text.index('## Estado da revisão')]+'''## Estado da revisão

Composição fechada em 383 páginas. Todas foram inspecionadas visualmente em 43 painéis, com ampliações selecionadas, incluindo os nove mapas. A página 194 também foi renderizada com Poppler e inspecionada. O hash da saída é o mesmo nos registros de composição, conferência, renderização e revisão visual.

- `revisao-visual.json`: cobertura efetiva, ampliações, correções das quatro provas e limites da inspeção.
- `conferencia-do-manifesto.json`: auditoria do estado anterior e união dos artefatos deste lote, produzida no fechamento.
- [Relatório e próxima etapa](../145-pdf-integrado-e-revisao-visual.md).

A próxima etapa é a comparação editorial final prevista na etapa 8 do plano 98: GPT-6 Astra, esforço extra alto; ajustes e consolidação com GPT-6.1 Sol, esforço alto. O salvamento deste lote é local; o último envio remoto continua sendo o registro 141.

## Reproduzir a saída

Recrie um ambiente Python com `requirements.txt` se o ambiente temporário não existir. Execute `GERAR-PDF.py`, depois `CONFERIR-PDF.py` e `RENDERIZAR.py`. Alterações de conteúdo devem acontecer primeiro nas fontes vigentes, seguidas da atualização HTML. O programa confere os hashes das entradas e exige atualizar a lista de fontes conscientemente quando o manuscrito mudar. Após qualquer nova saída, a revisão visual anterior não vale automaticamente: confira o novo fluxo e registre o novo hash.

Não execute `REGISTRAR.py` novamente sobre este fechamento. Não reaplique os preparadores anteriores sobre a edição integrada atual.
''';p.write_text(text)
print('Revisão, cópias anteriores e dez controles registrados.')
