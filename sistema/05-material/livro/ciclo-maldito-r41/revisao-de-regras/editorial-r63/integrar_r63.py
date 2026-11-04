from pathlib import Path
import json,shutil,hashlib,datetime
H=Path(__file__).resolve().parent;S=Path('/home/mizuki/JJK-v0.341-para-subir');L=S/'sistema/05-material/livro';B=L/'ciclo-maldito-r41';E=B/'revisao-de-regras/editorial-r63'
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
validation=json.loads((H/'revisao/VALIDACAO.json').read_text());assert validation['resultado']=='aprovado'
comp=json.loads((H/'revisao/COMPARACAO-R62.json').read_text())
ops=json.loads((B/'revisao-de-regras/alteracoes/R62-para-R63.json').read_text())
assert (H/'LIVRO-CANDIDATA.md').read_bytes()==(B/'LIVRO-COMPLETO.md').read_bytes()
assert comp['paletas']['claro']['paginas_com_imagem_alterada']==comp['paletas']['noturno']['paginas_com_imagem_alterada']
assert comp['paletas']['claro']['paginas']==comp['paletas']['noturno']['paginas']==425
pdfs=['Ciclo-Maldito-Livro-de-Regras.pdf','Ciclo-Maldito-Livro-de-Regras-Noturno.pdf']
for f in pdfs:shutil.copy2(H/'composicao/output/pdf'/f,L/f)
meta=json.loads((L/'EDICAO-ATUAL.json').read_text());meta.update(revisao='R63',paginas=validation['paginas'],revisado_em=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).isoformat())
for p in ['claro','noturno']:meta[p]['sha256']=sha(L/meta[p]['arquivo'])
dump(L/'EDICAO-ATUAL.json',meta)
alteradas=comp['paletas']['claro']['paginas_com_imagem_alterada']
comp['revisao_visual']={'resultado':'aprovado',
 'escopo':f'Comparação raster das 425 páginas por paleta frente à R62: {len(alteradas)} páginas mudaram, as mesmas nas duas paletas. Em todas, fim de cada coluna e título no pé medidos contra a R62 (COLUNAS-R62-R63.json); páginas com coluna deslocada mais de 10% (110, 342, 343 e 396) e o sumário inspecionados lado a lado com a R62; as {len(alteradas)} páginas alteradas revistas uma a uma em folha de contato da paleta clara; página 3 revista também na noturna.',
 'paginas_alteradas':alteradas,
 'observacoes':'Mesmo número de páginas (425) e a mesma contagem de páginas de atenção (44). Seis âncoras mudaram de página, todas nas Bênçãos: Casco e Vulto de 340/341 para 341/342 e Campo de 342 para 343, e o Índice acompanhou. A medida marcou a página 3 por engano: lá as últimas linhas são as entradas do sumário, sem título solto. A página 110 ganhou texto no topo da primeira coluna; a 396 passou a tabela Área básica para a 397, com o título Alcance e área e a primeira tabela juntos. O sumário do capítulo 10 passou à ordem das páginas, inclusive Feitiços de Classe 0 (257), que o plano não listava, e Conheça as Famílias deixou de ser subitem de Montar sua aplicação. Clara e noturna têm as palavras nas mesmas posições em todas as páginas.'}
dump(L/'REVISAO-R63.json',{'revisao':'R63','base':'R62','resultado':'aprovado','paginas':validation['paginas'],'blocos_alterados':sorted({o['bloco'] for o in ops}),'trocas':len(ops),
 'descricao':'Linguagem simples, sem mudar regra: saíram parcela, elegível, efetivamente, concessão, pertinente, retroativo e vencimento; excedente virou o que passa do limite e, nas entidades, sobra de dano; vinculado virou ligado a, fora arma vinculada e Retorno Vinculado; "reserva" saiu de 68 usos em que nomeava outra coisa; o nível Ampliada das obras do Arquiteto virou Extensa. Sumário do capítulo 10 em ordem de página. Números, custos, gatilhos e âncoras preservados.',
 'conferencia_pdf':validation,'revisao_visual':comp,'sha256':{**{p:meta[p]['sha256'] for p in ['claro','noturno']},'texto':sha(B/'LIVRO-COMPLETO.md')}})
dump(E/'COMPARACAO-R62.json',comp);shutil.copy2(H/'revisao/VALIDACAO.json',E/'VALIDACAO-PDFS.json')
for f in ['conferir.py','comparar_r62.py','medir_colunas.py','DESTINOS-INDICE-REVISAO.json','TROCAS-R63.json','TROCAS-R63.md','trocas_r63.py','conferir_trocas.py','integrar_texto_r63.py','integrar_r63.py']:shutil.copy2(H/f,E/f)
shutil.copy2(H/'revisao/COLUNAS-R62-R63.json',E/'COLUNAS-R62-R63.json')
(E/'composicao').mkdir(exist_ok=True)
for f in ['gerar_livro.py','gerar_noturno_r57.py','ler_fontes.py','fluxo_continuo.py']:shutil.copy2(H/'composicao'/f,E/'composicao'/f)
(E/'COMPOSICAO.md').write_text(f'Scripts da composição R63 preservados como registro. Ambiente completo de geração: {H}/composicao. Os scripts dependem dos recursos e módulos desse ambiente; esta pasta não é um pacote autônomo de geração. A R62 permanece preservada em seu diretório e no histórico do Git.\n\nMudança de composição da R63: em gerar_livro.py, o sumário do capítulo 10 passou à ordem das páginas, Conheça as Famílias subiu de nível, e o papel do título de ritual--rit-parcelas acompanha o nome novo, Partes adicionais. O resto da composição é o da R62.\n\nPython usado na geração e na conferência: runtime do Codex em ~/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3, com PYTHONPATH em revisao-didatica-r57-v1/prototipos/etapa07/tmp/python para pymupdf e pypdf.\n')
fp=json.loads((E/'FONTE-PUBLICADA.json').read_text());assert fp['sha256_texto']==sha(B/'LIVRO-COMPLETO.md')
for f in pdfs+['EDICAO-ATUAL.json','REVISAO-R63.json']:shutil.copy2(L/f,S/'finalizado/livro'/f)
print(meta['revisao'],meta['paginas'],meta['claro']['sha256'][:16],meta['noturno']['sha256'][:16],len(ops),'trocas')
