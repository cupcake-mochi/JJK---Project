from pathlib import Path
import json,hashlib,shutil
P=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial');M=P/'consolidacao/lote-01/migracao-nomes';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
units=json.loads((M/'QA-UNIDADES.json').read_text());pixels={r['unidade']:r for r in json.loads((M/'QA-PIXELS.json').read_text())};out=[]
remarks={
'regras-gerais/lote-final':{11:'Guarda Aberta no texto de concentração; quadro de custos e parágrafos mantêm margens.',16:'Guarda Aberta na lista de limites de Bloquear; exemplo e quadro completos.',19:'Nome da condição no procedimento de travessia; tabela de tamanhos e nota íntegras.',34:'Nome da condição na liberação de contenção; parágrafos e exemplos legíveis.'},
'equipamento/lote-final':{21:'Guarda Aberta no último parágrafo de contenção; linha final permanece dentro do corpo da página, ambas as tabelas íntegras.'},
'aptidoes/lote-01':{3:'Cabeçalho Categoria de Efeito quebra em duas linhas, sem compressão ou sobreposição. Encarnado na linha Cesta legível.',7:'Categoria de Efeito 3 no requisito sem quebra prejudicial; tabela de cura preservada.',8:'Remissão Dano e recuperação cabe no parágrafo, sem interferir no exemplo.',9:'Categoria de Efeito 3 no requisito, tabela e exemplo claros.',10:'Categoria de Efeito 3 no requisito; quadro das marcas intacto.',11:'Remissão Dano e recuperação cabe na regra do dano; exemplo e duas aptidões completos.',13:'Encarnado e Categoria de Efeito 1 no requisito; exemplos e quadro da Cesta íntegros.',14:'Categoria de Efeito 2 no requisito; tabela, voto e permanência legíveis.',16:'Categoria de Efeito 2 no requisito; quadro e regras de queda/contra-ataque íntegros.',17:'Categorias mencionadas em neutralização; parágrafos, nota e espaços preservados.',20:'Categoria de Efeito no título de escala e Categoria 1/2 nos exemplos; a tabela ocupa a largura útil e não estoura células.'},
'caminhos/incursor/lote-01':{3:'Guarda Aberta na expiração de Fluidez, sem interferir nos usos listados.',16:'Guarda Aberta na retenção da captura; restante das habilidades permanece legível.'},
'origens/lote-01':{8:'Guarda Aberta e remissão Dano e recuperação legíveis; título, texto e exemplo completos.',12:'Corpo Emprestado usa Guarda Aberta, com quebra regular e sem invadir a margem.'}}
for n in units:
 b=P/n;e=b/'evidencias';conf=json.loads((b/'VALIDACAO.json').read_text());source=b/conf['manuscrito'];pdf=b/'output/pdf'/conf['pdf'];r=pixels[n];assert sha(pdf)==r['sha256_depois'];old=json.loads((M/'qa-antes'/n/'evidencias/inspecao-visual.json').read_text())
 if r['PDF_identico']:
  assert sha(pdf)==r['sha256_antes'];inspection=old
 else:
  rows=[]
  for item in r['registros']:
   i=item['pagina'];row=dict(old['paginas'][i-1]);row.update(sha256_png=item['sha256_depois'],pixels_iguais_rodada_anterior=item['igual'])
   if item['igual']:
    row['evidencia_preservacao']='Identidade de pixels com a página já inspecionada na prova anterior; não houve nova abertura nesta rodada.'
   else:
    assert i in remarks[n];row.update(resultado='sem defeito visual observado',observacoes=remarks[n][i],revisor='/root/compatibilidade',inspecao_realizada='PNG aberto individualmente na rodada de migração nominal, 2026-10-03')
   folder=b/'output/png';folder.mkdir(parents=True,exist_ok=True);dest=folder/f'pagina-{i:02}.png';shutil.copy2(item['imagem'],dest);row['imagem']=str(dest.relative_to(b));rows.append(row)
  inspection={'data':'2026-10-03','sha256_texto':sha(source),'sha256_pdf':sha(pdf),'metodo':'Todas as páginas alteradas pela migração e seus complementos foram abertas individualmente. As demais conservam a inspeção anterior por igualdade de pixels comprovada, sem alegar nova leitura visual.','prova_anterior':r['sha256_antes'],'comparacao':'evidencias/COMPARACAO-NOMES-PDF.json','paginas':rows,'limites':'Inspeção por modelo em PNG a 100 dpi, sem impressão física ou teste com leitores humanos.'}
  (e/'inspecao-visual.json').write_text(json.dumps(inspection,ensure_ascii=False,indent=2)+'\n')
 delta={'unidade':n,'sha256_texto':sha(source),'sha256_pdf':sha(pdf),'escopo':'Releitura contextual das linhas alteradas; a revisão integral anterior permanece em seus relatórios históricos.','invariantes':'IDs, numerais, alcance, custos, procedimentos e tabelas conservados. Nomes aprovados e concordância uniformizados.','historico':str((M/'qa-antes'/n).relative_to(P)),'auditoria_numerica':'Execuções novamente concluídas após os nomes; outputs locais vinculados à versão atual.','paginas_reabertas':r['alteradas'],'paginas_preservadas':conf['paginas']-len(r['alteradas']),'equivalencia_visual':'PDF bitwise idêntico' if r['PDF_identico'] else 'Hashes de pixels por página, COMPARACAO-NOMES-PDF.json','revisao_independente_delta':{'revisor':'/root','resultado':'Sem bloqueador nos diffs nominais completos de Regras gerais, Equipamento, Aptidões, Incursor e Origens, conforme confirmação direta do revisor; unidades de texto idêntico preservam o parecer anterior.','complemento':'aguardando confirmação localizada apenas em Aptidões/Origens' if n in ['aptidoes/lote-01','origens/lote-01'] else 'não aplicável'},'limites':['Sem novo cânone, redesign ou afirmação de equilíbrio final.','Leitura por modelo não equivale a teste com pessoas.','Adjetivos passivo/passiva comuns mantidos.']}
 (e/'REVISAO-NOMES.json').write_text(json.dumps(delta,ensure_ascii=False,indent=2)+'\n')
 v=json.loads((b/'VALIDADORES.json').read_text());v['sha256_texto']=sha(source);v['sha256_pdf']=sha(pdf);v['revalidacao_nomes']=delta
 for item in v['validadores']:
  item['delta_nomes']='evidencias/REVISAO-NOMES.json'
  if item['id']=='V14':item['limite_delta']=f"{len(r['alteradas'])} páginas abertas; {conf['paginas']-len(r['alteradas'])} preservadas por identidade da prova."
 (b/'VALIDADORES.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
 out.append({'unidade':n,'sha256_texto':sha(source),'sha256_pdf':sha(pdf),'paginas':conf['paginas'],'alteradas':r['alteradas']})
(M/'QA-FECHAMENTO.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
