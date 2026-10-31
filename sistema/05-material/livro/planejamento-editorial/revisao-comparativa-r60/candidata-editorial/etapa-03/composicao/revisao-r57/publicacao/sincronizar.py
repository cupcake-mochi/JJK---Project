from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil,re
src=Path('/home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r57')
repo=Path('/home/mizuki/JJK-v0.341-para-subir');pub=Path('/home/mizuki/JJK---PDF---RPG')
book=repo/'sistema/05-material/livro';base=book/'ciclo-maldito-r41';rev=base/'revisao-de-regras/editorial-r57';rev.mkdir(exist_ok=True)
def read(p):return json.loads(p.read_text())
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def cp(a,b):b.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(a,b)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def replace(p,a,b):
 t=p.read_text();assert a in t,(p,a);p.write_text(t.replace(a,b))
assert sha(src/'output/pdf/Ciclo-Maldito-R57.pdf')=='40a405e0ac954b68cc31fe20192f36c94c52103613a58eec3c39f9919a3ce4bc'
assert sha(src/'output/pdf/Ciclo-Maldito-R57-Noturno-Vinho-e-Pessego.pdf')=='347be0ecc616088b27d468ff9bb5e570ac691ed9e888abd6f1a1d4d0dd4a56c8'
cp(src/'LIVRO-COMPLETO.md',base/'LIVRO-COMPLETO.md')
for n in range(54,58):
 cp(src/f'revisao-r{n}/BLOCOS-R{n}.json',rev/f'BLOCOS-R{n}.json')
 cp(src/f'ALTERACOES-R{n-1}-para-R{n}.json',base/f'revisao-de-regras/alteracoes/R{n-1}-para-R{n}.json')
for f in ['REVISAO-TEXTUAL.json','REVISAO-VISUAL.json','CONFERENCIA-TEXTUAL-ESTRUTURAL.json','ESPACOS-PRESERVADOS.json','ENTREGA.json']:
 cp(src/'revisao-r57'/f,rev/f)
cp(src/'evidencias/CONFERENCIA.json',rev/'CONFERENCIA-PDF.json')
cp(src/'revisao-r57/VALIDACAO-NOTURNO.json',rev/'VALIDACAO-NOTURNO.json')
cp(src/'LEIA-ME-R57.txt',rev/'LEIA-ME.txt')
write(rev/'FONTE-PUBLICADA.json',{'revisao':'R57','sha256_texto':sha(base/'LIVRO-COMPLETO.md'),'blocos':576,'cadeia_editorial':['R53-para-R54','R54-para-R55','R55-para-R56','R56-para-R57'],'composicao_local':str(src)})
meta=read(book/'EDICAO-ATUAL.json');meta.update({'revisao':'R57','paginas':415,'revisado_em':datetime.now(timezone.utc).isoformat()})
for key,name in [('claro','Ciclo-Maldito-R57.pdf'),('noturno','Ciclo-Maldito-R57-Noturno-Vinho-e-Pessego.pdf')]:
 p=src/'output/pdf'/name;meta[key]['sha256']=sha(p)
 for d in [book,pub/'livro']:cp(p,d/meta[key]['arquivo'])
for d in [book,pub/'livro']:write(d/'EDICAO-ATUAL.json',meta)
review={'revisao':'R57','paginas':415,'resultado':'aprovado','sha256_claro':meta['claro']['sha256'],'sha256_noturno':meta['noturno']['sha256'],'operacoes_editoriais_r57':42,'blocos_alterados_r57':34,'regras_alteradas_na_rodada':False,'texto':read(src/'revisao-r57/REVISAO-TEXTUAL.json'),'visual':read(src/'revisao-r57/REVISAO-VISUAL.json'),'conferencia_pdf':read(src/'evidencias/CONFERENCIA.json'),'noturno':{'verificacoes':len(read(src/'revisao-r57/VALIDACAO-NOTURNO.json')['verificacoes']),'resultado':'aprovado'},'espacos_preservados':read(src/'revisao-r57/ESPACOS-PRESERVADOS.json')}
for d in [book,pub/'livro']:write(d/'REVISAO-R57.json',review)
# Current documentation and compatibility readers.
replace(repo/'sistema/03-mecanica/livro.py','Leitura da edição atual, R53.','Leitura da edição atual, R57.')
replace(repo/'sistema/03-mecanica/conferir-fundamento.py',"revisao-de-regras/fundamento-r53/BLOCOS-R53.json","revisao-de-regras/editorial-r57/BLOCOS-R57.json")
replace(base/'LEIA-ME.md',base.joinpath('LEIA-ME.md').read_text(),'''# Fonte corrente R57\n\nLIVRO-COMPLETO.md é a edição R57, de 415 páginas, usada pelos validadores. A revisão acrescentou contexto a termos e referências antecipadas. As regras do Fundamento continuam com o modelo integrado na R53.\n\nOs snapshots R54 a R57, as evidências e a impressão digital atual ficam em revisao-de-regras/editorial-r57/. O antes e depois de cada rodada está em revisao-de-regras/alteracoes/. A integração R53 permanece preservada em fundamento-r53/. Os PDFs ficam na pasta acima, com seus hashes em EDICAO-ATUAL.json.\n\nA composição atual está na entrega local /home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r57/. As cadeias antigas de geração documentam versões anteriores.\n''')
replace(repo/'README.md','**Versão v0.366**','**Versão v0.367**')
replace(repo/'README.md','Ciclo Maldito R53, livro completo com 411 páginas','Ciclo Maldito R57, livro completo com 415 páginas')
p=repo/'README.md';t=p.read_text();mark='O texto final fica em';i=t.index(mark);t=t[:i]+'A R57 conclui as revisões editoriais de contexto e diagramação posteriores à R53. Os registros de R54 a R57 ficam em `sistema/05-material/livro/ciclo-maldito-r41/revisao-de-regras/editorial-r57/`, com o antes e depois de cada rodada em `alteracoes/`.\n\n'+t[i:];p.write_text(t)
replace(repo/'sistema/LEIA-ME.md','**v0.366.**','**v0.367.**')
replace(repo/'sistema/LEIA-ME.md','O livro atual é a R53,','O livro atual é a R57,')
p=repo/'sistema/ESTADO-ATUAL.md';p.write_text('''# Edição corrente R57\n\nOs dois PDFs e o texto dos validadores estão sincronizados na R57, com 415 páginas. As rodadas R54 a R57 revisaram apresentação, contexto e diagramação. A R57 contém 42 ajustes editoriais em 34 blocos, sem alterações de regra.\n\nA guarda de integridade valida a cadeia de alterações da R52 até a R57 e compara o texto final ao snapshot atual. Evidências em `05-material/livro/ciclo-maldito-r41/revisao-de-regras/editorial-r57/`. O modelo de montagem mantém o nome fundamento_r53 por compatibilidade e lê a edição corrente.\n\nO histórico abaixo registra o estado anterior.\n\n'''+p.read_text())
p=book/'ESTADO-revisao.md';p.write_text('# Revisão editorial R57 concluída\n\nTexto e PDFs atuais: R57, 415 páginas. Registros e evidências em ciclo-maldito-r41/revisao-de-regras/editorial-r57/. A integração mecânica R53 e os relatórios anteriores abaixo permanecem como histórico.\n\n'+p.read_text())
p=repo/'logs/CHANGELOG.md';t=p.read_text();i=t.index('## [0.366]');t=t[:i]+'''## [0.367] - 25/10/2026\n\n### Alterado\n\n- Publicação da R57, clara e noturna, com 415 páginas. Sincronizados PDFs, texto corrente, hashes e registros editoriais das rodadas R54 a R57.\n- A R57 acrescenta 42 esclarecimentos em 34 blocos para contextualizar nomes e mecânicas antes de sua explicação completa, sem alterar regras.\n- A guarda de integridade acompanha a cadeia de snapshots e registros até a R57. O recorte passa a conferir também o PDF noturno e os metadados da edição.\n- Revisão visual completa nas duas paletas, com uma passagem ampliada em 12 páginas. Espaços preservados e limites das verificações estão registrados.\n\n→ Continua em `sistema/ESTADO-ATUAL.md`, com a edição R57 e sua publicação.\n\n---\n\n'''+t[i:];p.write_text(t)
replace(pub/'README.md','**Livro atual: Ciclo Maldito R53**, em **21 capítulos e 411 páginas**','**Livro atual: Ciclo Maldito R57**, em **21 capítulos e 415 páginas**')
replace(pub/'README.md','**Recorte da v0.366.**','**Recorte da v0.367.**')
replace(pub/'README.md','As peças de apoio e os validadores locais acompanham as interfaces da R53.','As peças de apoio conservam a integração da R53; o texto corrente e os validadores locais acompanham a revisão editorial R57.')
# Include both PDFs and edition records in the existing single-owner export list.
replace(repo/'conferir-repositorio.py',"for f in ('Ciclo-Maldito-Livro-de-Regras.pdf',):","for f in ('Ciclo-Maldito-Livro-de-Regras.pdf', 'Ciclo-Maldito-Livro-de-Regras-Noturno.pdf',\n              'EDICAO-ATUAL.json', 'REVISAO-R57.json'):")
print('PDFs, fonte corrente, snapshots, registros e documentação sincronizados.')
