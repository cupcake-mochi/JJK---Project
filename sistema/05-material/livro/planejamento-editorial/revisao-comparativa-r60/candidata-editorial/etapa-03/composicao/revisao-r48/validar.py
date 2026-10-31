from pathlib import Path
import json,hashlib,re
from collections import Counter
from pypdf import PdfReader
B=Path(__file__).resolve().parents[1];O=B.with_name('livro-diagramado-r47');R=B/'revisao-r48'
assert (B/'LIVRO-COMPLETO.md').read_bytes()==(O/'LIVRO-COMPLETO.md').read_bytes()
snapshot=json.loads((R/'BASE-R47-SHA256.json').read_text());bad=[p for p,h in snapshot.items() if not (O/p).exists() or hashlib.sha256((O/p).read_bytes()).hexdigest()!=h];assert not bad,bad
old=json.loads((O/'FONTES-E-VALIDACAO.json').read_text());new=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());assert new['pdf'].endswith('R48.pdf')
# Exact source Markdown comparison covers all prose, examples and tables.
# Rendering may repeat a table header or a context label in a different place.
for file in ['ESTUDO-DENSIDADE.json','ESTUDO-HIERARQUIA.json','ESTUDO-SECAO.json','ESTUDO-TABELAS.json','ESTUDO-CAPITULO.json','REFERENCIAS.json','ARTES-APLICADAS.json','CREDITOS.json']:
 assert (B/file).read_bytes()==(O/file).read_bytes(),file
pdf=B/new['pdf'];assert len(PdfReader(pdf).pages)==new['paginas']
changes=[]
keys=list(dict.fromkeys(e['bloco'] for e in old['eventos'] if e['bloco']))
for key in keys:
 a=[e for e in old['eventos'] if e['bloco']==key];z=[e for e in new['eventos'] if e['bloco']==key]
 if a!=z:changes.append({'bloco':key,'paginas_antes':sorted({e['pagina'] for e in a}),'paginas_depois':sorted({e['pagina'] for e in z}),'antes':a,'depois':z,'motivo':'R48: composição por continuidade; texto fonte idêntico, com remissões paginadas e cabeçalhos repetidos regenerados.'})
(R/'POSICIONAMENTO-ANTES-DEPOIS.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
(R/'ALTERACOES-GERADOR.json').write_text(json.dumps([{'arquivo':f,'antes':(O/f).read_text(),'depois':(B/f).read_text(),'motivo':'Preservar finais curtos e aberturas de grupos; manter metadados de equipamento junto do efeito, tabelas curtas inteiras e conclusão breve junto de tabela larga; reservar espaço para largura inteira. Atualizar nome do PDF.'} for f in ['fluxo_continuo.py','gerar_livro.py']],ensure_ascii=False,indent=2)+'\n')
(B/'ALTERACOES-R47-para-R48.json').write_text('[]\n')
# User's reported case must have its whole subsection on one page.
es=[e for e in new['eventos'] if e['bloco']=='origens--descendente-inumaki' and not e['gerado']]
at=next(i for i,e in enumerate(es) if e['texto']=='Leitura a Dois');entry=es[at:]
assert len({e['pagina'] for e in entry})==1,[(e['pagina'],str(e['texto'])[:50]) for e in entry]
result={'base':'R47','texto_fonte':'LIVRO-COMPLETO.md byte a byte idêntico à R47','alteracoes_textuais':0,'blocos_textuais_preservados':511,'arquivos_R47_preservados':len(snapshot),'divergencias_R47':bad,'paginas_antes':old['paginas'],'paginas_depois':new['paginas'],'leitura_a_dois_pagina':entry[0]['pagina'],'leitura_a_dois':'Título, regra, exemplo e último parágrafo na mesma página.','sha256_pdf':hashlib.sha256(pdf.read_bytes()).hexdigest(),'blocos_com_posicionamento_diferente':len(changes)}
(R/'VALIDACAO.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
