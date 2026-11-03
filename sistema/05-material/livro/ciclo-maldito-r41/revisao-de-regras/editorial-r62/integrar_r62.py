from pathlib import Path
import json,shutil,hashlib,datetime
H=Path(__file__).resolve().parent;S=Path('/home/mizuki/JJK-v0.341-para-subir');L=S/'sistema/05-material/livro';B=L/'ciclo-maldito-r41';E=B/'revisao-de-regras/editorial-r62'
D=Path('/home/mizuki/JJK---PDF---RPG')
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
validation=json.loads((H/'revisao/VALIDACAO.json').read_text());assert validation['resultado']=='aprovado'
comp=json.loads((H/'revisao/COMPARACAO-R61.json').read_text())
ops=json.loads((B/'revisao-de-regras/alteracoes/R61-para-R62.json').read_text())
assert (H/'LIVRO-CANDIDATA.md').read_bytes()==(B/'LIVRO-COMPLETO.md').read_bytes()
assert comp['paletas']['claro']['paginas_com_imagem_alterada']==comp['paletas']['noturno']['paginas_com_imagem_alterada']
assert comp['paletas']['claro']['paginas']==comp['paletas']['noturno']['paginas']==425
pdfs=['Ciclo-Maldito-Livro-de-Regras.pdf','Ciclo-Maldito-Livro-de-Regras-Noturno.pdf']
for f in pdfs:shutil.copy2(H/'composicao/output/pdf'/f,L/f)
meta=json.loads((L/'EDICAO-ATUAL.json').read_text());meta.update(revisao='R62',paginas=validation['paginas'],revisado_em=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).isoformat())
for p in ['claro','noturno']:meta[p]['sha256']=sha(L/meta[p]['arquivo'])
dump(L/'EDICAO-ATUAL.json',meta)
alteradas=comp['paletas']['claro']['paginas_com_imagem_alterada']
comp['revisao_visual']={'resultado':'aprovado',
 'escopo':f'Comparação raster das 425 páginas por paleta frente à R61: {len(alteradas)} páginas mudaram, as mesmas nas duas paletas. Em todas, fim de cada coluna e título no pé medidos contra a R61 (COLUNAS-R61-R62.json); páginas com coluna deslocada mais de 10% inspecionadas lado a lado com a R61; as 77 páginas alteradas revistas uma a uma em folha de contato da paleta clara; páginas 279 e 394 revistas também na noturna.',
 'paginas_alteradas':alteradas,
 'observacoes':'Mesmo número de páginas (425) e as mesmas 44 páginas de atenção da R61. Nenhum título solto no pé de coluna. Nas páginas 279 e 394 sobra mais branco no fim da página porque uma seção inteira passou para a seguinte; o branco somado de cada sequência não cresceu (276-280: 1,93 → 1,89 colunas; 394-398: 1,03 → 0,92). A revisão achou a fórmula da vida máxima separada da sua introdução na virada da página 243, e a composição passou a mantê-las juntas no começo da 244. Achou também "saldo" fora do texto, no cabeçalho corrido, nas etiquetas de continuação e no sumário (páginas 3, 260 e 261); a composição passou a usar "Funções e pontos que sobram" e o conferir.py ganhou a checagem de "saldo" impresso nas duas paletas. Clara e noturna têm as palavras nas mesmas posições em todas as páginas.'}
dump(L/'REVISAO-R62.json',{'revisao':'R62','base':'R61','resultado':'aprovado','paginas':validation['paginas'],'blocos_alterados':sorted({o['bloco'] for o in ops}),'trocas':len(ops),
 'descricao':'Linguagem simples, sem mudar regra: "saldo" saiu do livro (montagem: pontos que sobram; vida e PE: atuais; movimento: metros que restam; XP: guardado), "lugar propício" virou "ambiente propício", a montagem usa sempre "destinar", a Reação é escrita como algo gasto, a ação de obra do Arquiteto passou a "Aumentar" e os termos usados antes da definição ganharam explicação no primeiro uso (seis com aposto e link; a Intenção, numa célula de tabela, só com link). Glossário e Índice ganharam "Ambiente propício". Números, custos, gatilhos e âncoras preservados.',
 'conferencia_pdf':validation,'revisao_visual':comp,'sha256':{**{p:meta[p]['sha256'] for p in ['claro','noturno']},'texto':sha(B/'LIVRO-COMPLETO.md')}})
dump(E/'COMPARACAO-R61.json',comp);shutil.copy2(H/'revisao/VALIDACAO.json',E/'VALIDACAO-PDFS.json')
for f in ['conferir.py','comparar_r61.py','medir_colunas.py','DESTINOS-INDICE-REVISAO.json','TROCAS-R62.json','TROCAS-R62.md','trocas_r62.py','conferir_trocas.py','integrar_texto_r62.py','integrar_r62.py']:shutil.copy2(H/f,E/f)
shutil.copy2(H/'revisao/COLUNAS-R61-R62.json',E/'COLUNAS-R61-R62.json')
(E/'composicao').mkdir(exist_ok=True)
for f in ['gerar_livro.py','gerar_noturno_r57.py','ler_fontes.py','fluxo_continuo.py']:shutil.copy2(H/'composicao'/f,E/'composicao'/f)
(E/'COMPOSICAO.md').write_text(f'Scripts da composição R62 preservados como registro. Ambiente completo de geração: {H}/composicao. Os scripts dependem dos recursos e módulos desse ambiente; esta pasta não é um pacote autônomo de geração. A R61 permanece preservada em seu diretório e no histórico do Git.\n\nMudança de composição da R62: em gerar_livro.py, o contexto do bloco fundamento--funcoes (cabeçalho corrido e etiqueta de continuação) e a linha do sumário passaram de "Funções e saldo" para "Funções e pontos que sobram". Em fluxo_continuo.py, a regra R40 passou a manter a fórmula da vida máxima junto da introdução terminada em dois-pontos (revisão visual, página 243). O resto da composição é o da R61.\n')
fp=json.loads((E/'FONTE-PUBLICADA.json').read_text());assert fp['sha256_texto']==sha(B/'LIVRO-COMPLETO.md')
for dest in [D,S/'finalizado']:
 for f in pdfs+['EDICAO-ATUAL.json','REVISAO-R62.json']:shutil.copy2(L/f,dest/'livro'/f)
print(meta['revisao'],meta['paginas'],meta['claro']['sha256'][:16],meta['noturno']['sha256'][:16],len(ops),'trocas')
