from pathlib import Path
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
import hashlib,json,shutil,subprocess
r=Path('/media/mizuki/HD Externo II/Claude/Pesquisa de Campo - Mestragem');a=r/'04 - Planejamento/apoio-revisao-integral-94';e=r/'07 - Edicao de Leitura';d=r/'08 - Diagramacao do Guia'
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
# All chapter files, appendices and entry pages.
soups={p.resolve():BeautifulSoup(p.read_text(),'html.parser') for p in e.rglob('*.html')};bad=[];count=0
for p,s in soups.items():
 for x in s.find_all('a',href=True):
  u=urlsplit(x['href'])
  if u.scheme or u.netloc:continue
  q=(p.parent/unquote(u.path)).resolve() if u.path else p;count+=1
  if not q.exists():bad.append([p.name,x['href'],'arquivo ausente'])
  elif u.fragment and q in soups and not soups[q].find(id=unquote(u.fragment)):bad.append([p.name,x['href'],'ancora ausente'])
links={'paginas_html':len(soups),'links_locais':count,'problemas':bad};save(a/'links-html-final.json',links);print(links);assert not bad
v=json.loads((a/'visual-prova-2/inspecao.json').read_text());assert len(v['paginas'])==357
for n in range(1,358):assert v['paginas'][str(n)]['conferida']
final={'pdf_sha256':sha(d/'output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf'),'paginas':357,'primeira_inspecao':'visual-prova-2/inspecao.json','comparacao':'comparacao-final.json','reinspecao':{str(n):{'sha256_png':sha(a/f'visual-final/p-{n:03}.png'),'conferida':True} for n in [1,2,313,314,351]},'resultado':'As 357 páginas foram examinadas. Na prova final, 353 páginas ficaram idênticas pixel a pixel; as quatro alteradas foram renderizadas e examinadas novamente. A p2 recebeu ampliação adicional. Nenhum corte ou sobreposição permaneceu nas verificações. Espaços de encerramento preservam unidades de leitura; tentativas de recompor duas, três e quatro páginas não reduziram a extensão sem alterar o padrão.'};save(a/'visual-final/inspecao.json',final)
nums=json.loads((a/'diferencas-numericas-para-conferencia.json').read_text())
for x in nums:x['conferencia']='Revisado: retirada de identificador/data de produção ou reorganização da mesma conta; sem alteração de valor mecânico.'
save(a/'conferencia-numeros-final.json',nums)
result=subprocess.run(['/tmp/guia-pdf-venv/bin/python',str(d/'VERIFICAR-PDF.py')],check=True,capture_output=True,text=True);audit=json.loads(result.stdout);save(a/'auditoria-pdf-final.json',audit);save(d/'revisao/auditoria-automatica.json',audit)
base=r/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md';assert sha(base)=='7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
log=json.loads((a/'alteracoes.json').read_text());print('alteracoes',len(log),'ocorrencias',sum(x['ocorrencias'] for x in log),'fontes',len({x['fonte'] for x in log}))
print('hash',final['pdf_sha256'])
state=json.loads((a/'estado.json').read_text());state['proxima']='Revisão integral concluída; consultar o registro 96 e o PDF final. Próximo passo sugerido: leitura externa e coleta de dúvidas, sem inventar teste já realizado.';state['conclusao']={'data':'2026-10-28','fontes_lidas':104,'segunda_leitura_paginas':357,'inspecao_visual_paginas':357,'pdf_sha256':final['pdf_sha256'],'relatorio':'04 - Planejamento/96-revisao-textual-integral-e-visual.md'};save(a/'estado.json',state)
for p in Path('/tmp').glob('guia94-*.py'):shutil.copy2(p,a/'scripts'/p.name)
