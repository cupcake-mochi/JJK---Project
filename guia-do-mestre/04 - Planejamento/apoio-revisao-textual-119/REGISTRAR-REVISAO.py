"""Registro das leituras e da inspeção visual concluída deste lote."""
from pathlib import Path
from collections import Counter
import json,hashlib
A=Path(__file__).resolve().parent;R=A.parents[1]
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,d):(A/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
m=load(A/'amostra.json');changes=load(A/'alteracoes.json');old=load(A/'imagens-inspecionadas-prova-3.json');assert len(m['paginas'])==17
last={10,11}
for i in range(1,18):
 if i not in last:assert sha(A/f'pagina-{i:02}.png')==old[str(i)],i
notes={
 1:'Abertura e escolha do limite: corpo, títulos e quadro largo legíveis.',
 2:'Preparo e reserva disputada: exemplos e custos legíveis; fluxo em duas colunas sem sobreposição.',
 3:'Fechamento de limites e começo de habilidades no mesmo fluxo; títulos e aviso experimental distintos.',
 4:'Conservar, adaptar ou criar: quadro, explicação dos tipos e custos legíveis.',
 5:'Custo dispensado e interações: tabela larga, linhas completas e nota sobre Contramedida em largura inteira.',
 6:'Três exemplos: subtítulos curtos, fórmula da CD inteira e requisitos completos; sem cabeçalho isolado.',
 7:'Números: abertura em largura inteira e quadro de funções; espaço antes da tabela seguinte preserva o quadro completo.',
 8:'Fórmulas e valores iniciais: tabelas legíveis; origem dos candidatos continua como texto corrido.',
 9:'Comparação entre Carregador e Sineiro inteira; precisão e sobrevivência com cabeçalhos e porcentagens legíveis.',
 10:'Remissão às outras faixas em largura inteira, reduzindo espaço lateral; dano, condições e frequência legíveis.',
 11:'Fechamento de números e início de outras faixas; perfis, atributos e hipótese de comparação legíveis.',
 12:'Tabelas de sete e seis colunas: números e rótulos legíveis, sem corte de linhas; conjuntos não apresentados como rodadas.',
 13:'Duro de Matar, apoio e Alma em blocos legíveis; consulta por faixa em largura inteira.',
 14:'Limites da comparação e começo de chefes no mesmo fluxo; título e introdução legíveis.',
 15:'Ajustes de confronto e ações fora do turno: dois quadros largos, sem linhas cortadas.',
 16:'Sinal, tempo de resposta e fases: exemplo de iniciativa inteiro; quadro de mudanças legível.',
 17:'Continuidade, derrota, partes e aliados: fechamento legível, com espaço final de conjunto.'}
save('revisao-final.json',{'registro':119,'pdf':m['pdf'],'pdf_sha256':m['pdf_sha256'],'passagens_textuais':[{'passagem':1,'registros':56,'escopo':'Leitura integral das cinco fontes; cinco cópias/remissões, 48 ajustes e três remissões ao método atual.'},{'passagem':2,'registros':20,'escopo':'Leitura das 18 páginas da primeira prova; 17 ajustes e três subtítulos relidos após inspeção.'}],'paginas':[{'pagina':i,'imagem':str((A/f'pagina-{i:02}.png').relative_to(R)),'imagem_sha256':sha(A/f'pagina-{i:02}.png'),'inspecionada':True,'metodo':'Inspeção direta após o último ajuste' if i in last else 'Inspeção direta da prova 3; imagem final idêntica','observacao':notes[i]} for i in range(1,18)],'limites':['Duas passagens completas e releitura dos refinamentos; sem leitor humano independente.','Espaços antes de quadros inteiros serão reavaliados na integração.','Não encerra a revisão visual global ou a comparação do livro completo.']})
ranges={'s059':([1,3],[1,3]),'s060':([3,6],[3,6]),'s074':([7,11],[7,11]),'s100':([11,14],[11,14]),'s067':([15,18],[14,17])};rows=[]
for f in m['fontes']:
 a,b=ranges[f['fonte_id']];counts=Counter(str(c['passagem']) for c in changes if c['fonte']==f['fonte'])
 rows.append({'id':f['fonte_id'],'fonte_original':f['fonte_original'],'fonte_revisada':f['fonte'],'sha256_original':f['sha256_original'],'sha256_revisado':f['sha256'],'passagem_1':'Original lido integralmente e regras pertinentes conferidas.','passagem_2_paginas_da_prova_1':a,'paginas_na_prova_final':b,'registros_por_passagem':dict(counts),'estado':'duas passagens locais; conferir o conjunto antes de integrar'})
save('leitura-por-caso.json',{'registro':119,'casos':rows,'limites':'Sem terceira leitura integral, teste humano ou nova simulação de combate.'})
save('mapa-do-lote.json',{'registro':119,'lote':'B2-01','casos':[f['fonte_id'] for f in m['fontes']],'pdf_parcial':m['pdf'],'paginas':17,'casos_revistos_total':15,'casos_pendentes':44,'lotes_pendentes':11,'consultas_complementares_pendentes':17,'etapa_6':'em andamento','proximo_lote':'B2-02','modelo_recomendado':'GPT-6.1 Sol','esforco_recomendado':'alto','edicao_integrada':'preservada; não substituída'})
print(json.dumps({'paginas_inspecionadas':17,'registros':len(changes),'casos':5},ensure_ascii=False))
