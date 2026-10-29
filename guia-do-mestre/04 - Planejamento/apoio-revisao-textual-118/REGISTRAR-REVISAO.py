"""Registrar somente a inspeção visual efetivamente concluída."""
from pathlib import Path
import hashlib,json,collections
A=Path(__file__).resolve().parent;R=A.parents[1]
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,d):(A/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
meta=load(A/'amostra.json');changes=load(A/'alteracoes.json');previous=load(A/'imagens-inspecionadas-prova-5.json');assert len(meta['paginas'])==20
# As 20 imagens da prova 5 foram inspecionadas; só a página 4 difere após o último ajuste; a página 3 voltou à imagem já inspecionada.
for i in range(1,21):
 if i!=4:assert sha(A/f'pagina-{i:02}.png')==previous[str(i)],i
notes={
 1:'Travessia e salto: títulos, fala, custos e tabela legíveis; sem sobreposição.',
 2:'Duto e queda: regras de passagem e divisão do impacto; quadro de quatro colunas legível.',
 3:'Queda e ponte: parcelas, defesa e características da obra legíveis; abertura de Parkour junto da apresentação.',
 4:'Parkour: descrição do percurso junto da tabela, em largura inteira; requisito de aproximação reunido. Espaço de encerramento do conjunto.',
 5:'Ricochete: posições, duas faixas e escolha de Força explicadas; sem título isolado.',
 6:'Comparação das trajetórias: medidas e unidades na mesma linha; título e introdução acompanham a tabela. Corda e fechadura legíveis.',
 7:'Algemas e cabo: tabela de perfil legível, requisitos e conta preservados.',
 8:'Garrafa: quadro, desvantagens, crítico e alcance legíveis; exemplo de treino mantido inteiro.',
 9:'Socorro: definição e fórmula da janela inteiras; escolhas e cálculo do tratamento legíveis.',
 10:'Aguentar, Insistir, prazo e dano: cabeçalhos e tabela legíveis. Texto corrido pode continuar entre colunas.',
 11:'Tratamento e estabilidade: comparação do descanso e quadro de duas quedas legíveis, com título e introdução juntos.',
 12:'Sequelas e derrota: fechamento junto do início da retirada; distinção visual clara entre os dois textos.',
 13:'Transporte e derrota: conta de carga inteira e estados distintos; sem corte de tabela.',
 14:'Descansos: título junto do quadro curto e cuidados em largura inteira; exceções podem ser lidas sem coluna estreita. Espaço entre blocos reavaliável na integração.',
 15:'Exaustão e descanso longo: duas tabelas largas; comparação com Integridade mantida inteira.',
 16:'Recuperação, consequências e próxima missão: fechamento e fonte juntos; espaço de fim de conjunto.',
 17:'Passagem: resumo e informações conhecidas legíveis; próximo quadro preservado inteiro na página seguinte.',
 18:'Estado e socorro de Mei: tabelas legíveis; arredondamento por extenso e nota final sem sobra na página seguinte.',
 19:'Perigo, divergência e retomada: cenário e estado pessoal separados; sequência em tabela larga legível.',
 20:'Depois do socorro: saldos e dúvidas futuras legíveis; referência de recompensa no mesmo parágrafo e coluna. Espaço de encerramento.'}
visual={'registro':118,'pdf':meta['pdf'],'pdf_sha256':meta['pdf_sha256'],'passagens_textuais':[{'passagem':1,'escopo':'Leitura integral dos cinco originais; cópias/remissões e 49 ajustes editoriais.','registros':54},{'passagem':2,'escopo':'Leitura das 21 páginas da primeira prova; 16 ajustes mais dois refinamentos relidos após inspeção.','registros':18}],'paginas':[{'pagina':i,'imagem':str((A/f'pagina-{i:02}.png').relative_to(R)),'imagem_sha256':sha(A/f'pagina-{i:02}.png'),'inspecionada':True,'metodo':'Inspeção direta após o último ajuste' if i==4 else 'Inspeção direta da prova 5; imagem final idêntica','observacao':notes[i]} for i in range(1,21)],'limites':['Duas leituras completas e releitura dos ajustes; sem leitor humano independente.','Prova parcial; ainda há espaços de fim de conjunto e antes de quadros que devem permanecer inteiros.','Integração e revisão visual do livro completo continuam pendentes.']}
save('revisao-final.json',visual)
ranges={'s084':([1,4],[1,4]),'s085':([5,8],[5,8]),'s022':([9,12],[9,12]),'s023':([13,17],[12,16]),'s081':([18,21],[17,20])}
rows=[]
for f in meta['fontes']:
 c=collections.Counter(str(x['passagem']) for x in changes if x['fonte']==f['fonte']);a,b=ranges[f['fonte_id']]
 rows.append({'id':f['fonte_id'],'fonte_original':f['fonte_original'],'fonte_revisada':f['fonte'],'sha256_original':f['sha256_original'],'sha256_revisado':f['sha256'],'passagem_1':'Original lido integralmente; conferência dirigida das regras pertinentes.','passagem_2_paginas_da_prova_1':a,'paginas_na_prova_final':b,'registros_por_passagem':dict(c),'estado':'duas passagens locais; integração e conferência global pendentes'})
save('leitura-por-caso.json',{'registro':118,'casos':rows,'formulario_24':'Lido por inteiro para conferir cobertura dos estados; original preservado e revisão textual integral ainda pendente.'})
save('mapa-do-lote.json',{'registro':118,'lote':'B1-02','casos':[f['fonte_id'] for f in meta['fontes']],'prova_parcial':meta['pdf'],'paginas':20,'casos_revisto_total':10,'casos_pendentes':49,'lotes_pendentes':12,'consultas_complementares_pendentes':17,'etapa_6':'em andamento','proximo_lote':'B2-01','modelo_recomendado':'GPT-6.1 Sol','esforco_recomendado':'alto','integrado_anterior':'preservado; não substituído'})
print(json.dumps({'paginas_inspecionadas':20,'registros':len(changes),'casos':len(rows)},ensure_ascii=False))
