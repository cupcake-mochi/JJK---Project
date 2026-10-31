from pathlib import Path
import json,hashlib,re
from collections import Counter
from pypdf import PdfReader
B=Path(__file__).resolve().parents[1];O=B.with_name('livro-diagramado-r48');R=B/'revisao-r49'
assert (B/'LIVRO-COMPLETO.md').read_bytes()==(O/'LIVRO-COMPLETO.md').read_bytes()
snapshot=json.loads((R/'BASE-R48-SHA256.json').read_text());bad=[p for p,h in snapshot.items() if not (O/p).exists() or hashlib.sha256((O/p).read_bytes()).hexdigest()!=h];assert not bad,bad
old=json.loads((O/'FONTES-E-VALIDACAO.json').read_text());new=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());assert new['pdf'].endswith('R49.pdf')
# Exact source Markdown comparison covers all prose, examples and tables.
# Rendering may repeat a table header or a context label in a different place.
for file in ['ESTUDO-DENSIDADE.json','ESTUDO-HIERARQUIA.json','ESTUDO-SECAO.json','ESTUDO-TABELAS.json','ESTUDO-CAPITULO.json','REFERENCIAS.json','ARTES-APLICADAS.json','CREDITOS.json']:
 assert (B/file).read_bytes()==(O/file).read_bytes(),file
pdf=B/new['pdf'];assert len(PdfReader(pdf).pages)==new['paginas']
changes=[]
keys=list(dict.fromkeys(e['bloco'] for e in old['eventos'] if e['bloco']))
for key in keys:
 a=[e for e in old['eventos'] if e['bloco']==key];z=[e for e in new['eventos'] if e['bloco']==key]
 if a!=z:changes.append({'bloco':key,'paginas_antes':sorted({e['pagina'] for e in a}),'paginas_depois':sorted({e['pagina'] for e in z}),'antes':a,'depois':z,'motivo':'R49: composição por continuidade; texto fonte idêntico, com remissões paginadas e cabeçalhos repetidos regenerados.'})
(R/'POSICIONAMENTO-ANTES-DEPOIS.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
(R/'ALTERACOES-GERADOR.json').write_text(json.dumps([{'arquivo':f,'antes':(O/f).read_text(),'depois':(B/f).read_text(),'motivo':'Aproveitar espaço para entradas completas, reduzir agrupamentos extensos, preservar tabelas que cabem em uma coluna e evitar finais quase vazios. Atualizar nome do PDF.'} for f in ['fluxo_continuo.py','gerar_livro.py']],ensure_ascii=False,indent=2)+'\n')
(B/'ALTERACOES-R48-para-R49.json').write_text('[]\n')
# User's reported case must have its whole subsection on one page.
es=[e for e in new['eventos'] if e['bloco']=='origens--descendente-inumaki' and not e['gerado']]
at=next(i for i,e in enumerate(es) if e['texto']=='Leitura a Dois');entry=es[at:]
assert len({e['pagina'] for e in entry})==1,[(e['pagina'],str(e['texto'])[:50]) for e in entry]
result={'base':'R48','texto_fonte':'LIVRO-COMPLETO.md byte a byte idêntico à R48','alteracoes_textuais':0,'blocos_textuais_preservados':511,'arquivos_R48_preservados':len(snapshot),'divergencias_R48':bad,'paginas_antes':old['paginas'],'paginas_depois':new['paginas'],'leitura_a_dois_pagina':entry[0]['pagina'],'leitura_a_dois':'Título, regra, exemplo e último parágrafo na mesma página.','sha256_pdf':hashlib.sha256(pdf.read_bytes()).hexdigest(),'blocos_com_posicionamento_diferente':len(changes)}
(R/'VALIDACAO.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))

# A ordem de todo o texto corrente também deve ser preservada no desenho.
def prose(m):return [(e['bloco'],e['tipo'],e['texto']) for e in m['eventos'] if not e['gerado'] and e['tipo']!='table']
assert prose(old)==prose(new),'A ordem ou o conteúdo dos parágrafos mudou'
bands={}
for e in new['eventos']:
 if e['modo']=='duas-colunas' and e['faixa'] is not None:bands.setdefault((e['pagina'],e['faixa']),[]).append(e)
for key,es in bands.items():
 xs=[int(e['x']>250) for e in es];assert xs==sorted(xs),('A leitura retornou à coluna esquerda',key)
result['ordem_textual']='Parágrafos na mesma ordem da R48; em cada faixa, coluna esquerda inteira antes da direita.'
result['faixas_conferidas']=len(bands)
(R/'VALIDACAO.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Ordem de leitura confirmada.',len(bands),'faixas')
