from pathlib import Path
import json,hashlib,shutil,difflib
B=Path(__file__).resolve().parents[1]; R=B/'revisao-r45'; OLD=B.with_name('livro-diagramado-r44')
def save(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def write(p,s): p.write_text(s.strip()+'\n')
proof=json.loads((R/'PAGINAS-PARA-PROVA.json').read_text())
findings=json.loads((R/'ACHADOS-E-CORRECOES.json').read_text())
for f in findings:
 if f['id'].startswith('V'): f['estado']='corrigido e reconferido na prova visual final de 388 páginas'
save(R/'ACHADOS-E-CORRECOES.json',findings)
save(R/'REVISAO-VISUAL.json',{'edicao':'R45','paginas_pdf':388,'pdf_sha256':hashlib.sha256((B/'output/pdf/Ciclo-Maldito-R45.pdf').read_bytes()).hexdigest(),'paginas_inspecionadas':proof,'metodo':'Renderização Poppler e inspeção efetiva das 18 folhas de contato da prova final; leitura dos textos finais separadamente. Autorrevisão.','escopo':'69 páginas selecionadas: capítulo de Origens completo, dependências afetadas, sumário, glossário e índice. Não é inspeção visual de todas as 388 páginas.','resultado':'Sem cortes, sobreposições ou títulos órfãos novos identificados na amostra final.','correcoes':['Menores do Latente acompanha a primeira opção','Abertura Zenin acompanha o primeiro componente da marcante','Saída Elevada acompanha a tabela de pontos','Marcante e menores em ordem no glossário','Novas entradas posicionadas na ordem alfabética do índice'],'limites':['Espaço branco antes de aberturas com arte e em finais de capítulo preservado.','A página final do índice tem poucas entradas; não houve compressão global do índice.','Não é certificação de acessibilidade nem teste de compreensão com leitores humanos.']})
sheet=json.loads((R/'FICHA-DIGITAL-R45.json').read_text())
sheet['ajustes_visuais_posteriores']=[{'updateDimensionProperties':{'range':{'sheetId':450013,'dimension':'COLUMNS','startIndex':1,'endIndex':8},'properties':{'pixelSize':60},'fields':'pixelSize'}},{'repeatCell':{'range':{'sheetId':450013,'startRowIndex':3,'endRowIndex':24,'startColumnIndex':1,'endColumnIndex':8},'cell':{'userEnteredFormat':{'horizontalAlignment':'LEFT'}},'fields':'userEnteredFormat.horizontalAlignment'}},{'repeatCell':{'range':{'sheetId':450013,'startRowIndex':25,'endRowIndex':28,'startColumnIndex':0,'endColumnIndex':8},'cell':{'userEnteredFormat':{'wrapStrategy':'WRAP','verticalAlignment':'MIDDLE'}},'fields':'userEnteredFormat.wrapStrategy,userEnteredFormat.verticalAlignment'}}]
sheet['limite']='Painel de registro e alerta do Híbrido implementados em cópia. Outras automações herdadas não foram convertidas integralmente para as novas Origens; conferir bônus manualmente.'
save(R/'FICHA-DIGITAL-R45.json',sheet)
write(R/'RELATORIO-TESTES-E-REVISAO.md','''# R45 — relatório de testes e revisão

13/10/2026. Integração das Origens v178 sobre a R44, preservada integralmente. As decisões adicionais I001 e I002 estão registradas literalmente. Não houve commit, push ou publicação do livro.

## Integrado

Sete núcleos, dois ramos alternativos de Restrição Celestial, base + uma marcante + duas menores elegíveis. Sem Técnica separado. 52 blocos no registro antes/depois: 38 de Origens (12 novos) e 14 dependências. Outros 459 blocos permanecem idênticos. Um modelo suplementar de ficha foi atualizado com registro próprio.

O mapa decisão → texto → ficha reúne 146 entradas/títulos, com referências documentais. As fontes selecionadas estão copiadas em fontes-de-decisao, com hashes. Histórico e justificativa não entram no texto do jogador. Exemplos finais e suas diferenças estão no mesmo registro de blocos.

## Testes executados

- 68 casos determinísticos em TESTES-CALCULOS.json: todos aprovados, com entradas, gabarito e resultado. Incluem recuperação, arredondamentos, faixas, limites e contagens.
- Duplas elegíveis enumeradas por perfil, preservando restrições e repetições específicas; não se tratam de simulações de combate.
- Quatro fichas comparadas nos níveis 2, 10, 18 e 26, sob premissas idênticas de Caminho/atributos explicitadas em FICHAS-COMPARADAS.json. Não representam todos os Caminhos e Trilhas.
- Seis sequências de consumo de recursos em TESTES-DE-CONSUMO.json: todas aprovadas. Cenários modelados, sem dados humanos de mesa.
- 19 cenários de leitura/interação em CENARIOS-DE-LEITURA.json, examinados em autorrevisão mecânica e editorial.
- 11 casos executados na cópia nativa da ficha: entrada/saída da faixa de 30%, mudança do máximo, vida zero, usos, turno, Ação Bônus, impedimento, PE e outra Origem. Todos aprovados; dados de ensaio removidos e fórmulas restauradas.
- confer_ir_livro (script conferir_livro.py --strict): 122.552 verificações, 2.502 links internos, 192 marcadores, 511 blocos, 388 páginas, zero problemas apontados.
- Comparação dos 2.637 arquivos fotografados da R44: nenhuma divergência. Cada diferença do livro consolidado corresponde ao registro antes/depois da R45.

## Leitura e prova visual

Autorrevisão do texto final, comparação com aprovações e correção de seis achados de redação/remissão. Prova final de 69 páginas renderizadas, incluindo as 32 páginas do capítulo de Origens (66–97), dependências, sumário e índice. Cinco achados de composição/ordenação foram corrigidos e reconferidos. Páginas e critérios em REVISAO-VISUAL.json; imagens em prova/.

A verificação automática abrange o PDF inteiro; a inspeção visual abrange as 69 páginas indicadas. Não houve playtest humano, leitor externo, segunda revisão independente ou certificação de acessibilidade. Os testes não demonstram equilíbrio definitivo.

## Ficha

Foi criada uma cópia da ficha acessível, sem alterar a original. A aba ORIGENS R45 recebe escolhas e um alerta de regeneração do Híbrido; a vida na aba FICHA também recebe destaque quando entra na faixa. O alerta separa limiar de vida das demais condições de uso. O painel foi inspecionado visualmente no navegador. As demais automações antigas permanecem e precisam de conferência manual: esta entrega não é uma conversão completa do motor da ficha.

## Exportações

PDF, LIVRO-COMPLETO.md, FICHAS-COMPLETAS-R45.md, fontes/camadas editáveis e registros. DOCX não integra o fluxo efetivo da base; não foi fabricada uma exportação alternativa. O ZIP conserva os insumos de geração e os relatórios pertinentes, sem duplicar os PDFs e provas históricas pesadas.
'''.replace('confer_ir_livro','Validação do PDF'))
write(R/'NOMENCLATURA.md','''# Nomenclatura R45

- Híbrido é o nome visível vigente. As antigas âncoras técnicas contendo feto foram preservadas para não quebrar remissões; não são apresentadas ao jogador.
- Legado de história designa vínculo ou detalhe narrativo sem benefício mecânico. As escolhas mecânicas são marcante e menores, conforme a montagem aprovada.
- Sem Técnica é opção separada, sem ocupar marcante ou menor, apenas para as Origens autorizadas. Não é uma oitava Origem.
- Restrição Celestial contém dois ramos alternativos: Sem Energia e Restrição corporal. Não somar os pacotes.
- Classe é a escala das aplicações/capacidades; Categoria de Efeito é a escala dos Talentos; grau e patente seguem o uso institucional/do equipamento. Não foram tratados como sinônimos.
- Ofício compatível é escolhido e registrado na criação do corpo/personagem. Mantido o reparo da R44 por decisão I002.
- Demais nomes aprovados foram preservados. IDs de decisões e justificativas ficam nos registros, fora do livro.
''')
write(R/'PENDENCIAS.md','''# Pendências e limites reais — R45

Não restou decisão bloqueante para integrar o núcleo aprovado. I001 resolveu aquisição/limites do CE4 e I002 confirmou o reparo da R44.

1. **Três referências de CE4:** Arquitetura Microscópica, Manifestação Colossal e Geografia Interior aparecem como conceitos para construção com o mestre. Não foram promovidos a regras os parâmetros candidatos sem aprovação. Rede Remota usa seu núcleo aprovado. Para publicar as três como entradas fechadas de catálogo, ainda seriam necessárias decisões próprias de funcionamento.
2. **Interfaces extraordinárias:** não se inferiram novas permissões de Prenúncio, sentidos/Katas, Máximas, pulsos ou eventos não abrangidos pelas aprovações. O funcionamento publicado fica no alcance aprovado; uma futura ampliação requer decisão do autor.
3. **Reserva Condensada:** quantidade, ocasião e máximo são definidos com o mestre por regra aprovada. Isso não é lacuna a preencher com um teto universal.
4. **Ficha digital:** painel e alerta implementados em cópia; bônus e demais automações herdadas não foram todos reprogramados. Conferir a ficha pela R45 e registrar as escolhas no painel. Conversão integral da automação é tarefa separada.
5. **Validação humana e balanceamento:** autorrevisão e testes determinísticos concluídos. Leitura com jogadores, revisão independente e playtest de mesa permanecem por fazer; não se afirma equilíbrio definitivo.
6. **Diagramação:** preservadas artes, fontes e identidade existentes. Espaços de finais de capítulo/aberturas e a sobra final do índice não receberam uma nova rodada de compactação global.
7. **DOCX:** não há exportação DOCX no fluxo efetivo da base. Foram entregues Markdown editável e PDF, além dos insumos do gerador.
''')
write(B/'LEIA-ME-R45.md','''# Ciclo Maldito — R45

Integração das Origens v178 sobre a R44, concluída em 13/10/2026. **388 páginas.** R44 preservada; sem commit ou push. Comece por este arquivo: os LEIA-ME de versões anteriores são históricos.

## Entrega

- output/pdf/Ciclo-Maldito-R45.pdf — livro final.
- LIVRO-COMPLETO.md — texto consolidado editável.
- FICHAS-COMPLETAS-R45.md — modelos suplementares atualizados.
- ALTERACOES-R44-para-R45.json — 52 blocos com antes/depois, motivo e decisões.
- revisao-r45/ — mapa de decisões, fontes, testes, autorrevisão, pendências e prova visual.
- revisao-r45/ALTERACOES-DE-GERADOR-R45.json — diferenças dos scripts em relação à R44, incluindo as correções locais de continuidade.
- MANIFESTO-R45.json — hashes dos arquivos incluídos no ZIP. O SHA-256 do ZIP acompanha a entrega em arquivo separado.

## Ficha digital

Cópia com painel ORIGENS R45 e alerta de 30% do Híbrido:
https://docs.google.com/spreadsheets/d/1II2r3Yex_7H5BV2SVaU80XXyvPSqX6DNwYGmoSdBoOc/edit

A ficha original não foi alterada. As outras automações herdadas não foram integralmente convertidas; os campos do painel são registro e controle, e os demais bônus devem ser conferidos pelo livro. O link histórico existente no livro foi preservado.

## Reprodução

Python com ReportLab, Pillow, pypdf e pdfplumber. Poppler é usado na prova visual. Execute na pasta desta edição:

```sh
python gerar_livro.py --strict
python conferir_livro.py --strict
python revisao-r45/testar_origens.py
python revisao-r45/testar_integracao.py
```

Fontes editoriais congeladas e camadas anteriores são dependências ativas, não arquivos descartáveis. revisao_r45.py aplica o registro antes/depois após a R44, com conferência do texto anterior. A redação de trabalho está em revisao-r45/texto-final/. Não editar somente o Markdown consolidado esperando que sobreviva à geração. Os scripts históricos de preparação são registros; não os executar em lote. gerar_fichas.py é histórico e não exporta estes modelos R45 atualizados.

A conferência integral dos hashes da R44 depende da pasta original irmã e serve como auditoria local; o ZIP não duplica a edição anterior. O pacote contém fontes e ativos necessários à geração, mas não duplica PDFs e imagens de provas antigas.

## Limites

Veja revisao-r45/PENDENCIAS.md. Testes e leitura editorial são autorrevisão, sem playtest ou certificação de equilíbrio. PDF e Markdown são as exportações efetivas desta base; não há DOCX ativo.
''')
changes=[]
for p in B.glob('*.py'):
 old=OLD/p.name
 before=old.read_text() if old.exists() else ''
 after=p.read_text()
 if before!=after: changes.append({'arquivo':p.name,'antes':before,'depois':after,'motivo':'Integração R45 e composição local das novas Origens; scripts históricos preservados quando idênticos.'})
save(R/'ALTERACOES-DE-GERADOR-R45.json',changes)
shutil.copyfile('/home/mizuki/.codex/attachments/7f9de2e5-5765-4264-96b6-9013591a0e6d/Texto colado.txt',R/'PEDIDO-DE-INTEGRACAO.txt')
print('Relatórios concluídos;',len(changes),'scripts alterados/novos registrados')
