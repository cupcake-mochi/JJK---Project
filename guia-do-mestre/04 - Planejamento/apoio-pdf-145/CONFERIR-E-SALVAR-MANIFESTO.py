"""Auditar todas as entradas anteriores e salvar o registro 145 por união."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
import json,hashlib,markdown
A=Path(__file__).resolve().parent;R=A.parents[1];M=R/'04 - Planejamento/apoio-piloto/manifesto-entrega.json'
load=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def main():
 base=load(A/'antes/manifesto-entrega.json');assert len(base)==5458
 assert load(M)==base,'O manifesto mudou. Comparar antes de salvar.'
 config=load(A/'arquivos-do-lote.json');comp=load(A/'composicao.json');audit=load(A/'conferencia-do-pdf.json');render=load(A/'renderizacao.json');visual=load(A/'revisao-visual.json')
 digest=sha(R/config['pdf_novo'])
 assert all(d['sha256_pdf']==digest and d['paginas']==383 for d in [comp,audit,render,visual])
 assert not audit['falhas'] and not audit['diferencas_de_extracao_a_examinar'] and not visual['problemas_impeditivos_observados']
 assert visual['paginas_inspecionadas']==list(range(1,384))
 assert len(visual['paineis_inspecionados'])==43
 assert [n for p in visual['paineis_inspecionados'] for n in p['paginas']]==list(range(1,384))
 assert audit['fontes_textuais_preservadas']==99
 for n in visual['paginas_inspecionadas']:assert (A/'revisao/paginas'/f'pagina-{n:03}.png').is_file()
 for panel in render['painel']:assert (A/panel['painel']).is_file()
 for row in load(R/'04 - Planejamento/apoio-leitura-144/cobertura-da-leitura-continua.json')['fontes']:assert sha(R/row['fonte'])==row['sha256_atual'],row['fonte']
 allowed=set(config['controles']);assert len(allowed)==10
 assert config['fontes_alteradas']==config['html_alterados']==[]
 def inspect(entry):
  rel,d=entry;p=R/rel
  if not p.is_file():return rel,'ausente',None
  actual=sha(p);return rel,'alterado' if actual!=d else 'igual',actual
 changed=[];fail=[];actuals={}
 with ThreadPoolExecutor(max_workers=4) as pool:
  for i,(rel,status,actual) in enumerate(pool.map(inspect,base.items()),1):
   actuals[rel]=actual
   if status=='ausente':fail.append('Ausente: '+rel)
   elif status=='alterado':
    changed.append(rel)
    if rel not in allowed:fail.append('Alteração não declarada: '+rel)
   if i%1000==0:print('Entradas anteriores conferidas:',i,flush=True)
 assert set(changed)==allowed,(changed,sorted(allowed-set(changed)))
 original=load(R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json')['fontes'];assert len(original)==104
 for row in original:
  if actuals.get(row['fonte'])!=row['sha256']:fail.append('Fonte original mudou: '+row['fonte'])
 assert actuals['08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf']=='0050d7cf2426ce3eba555ab2010deaeb6d62e023a5dba67ec43f0495e79cbd3b'
 report=R/config['relatorio']
 # O resultado do manifesto será escrito abaixo, antes do hash dos artefatos.
 forthcoming=A/'conferencia-do-manifesto.json'
 for p in [report,A/'LEIA-ME.md']+[R/x for x in allowed]:
  tags=BeautifulSoup(markdown.markdown(p.read_text(),extensions=['tables']),'html.parser').find_all('a',href=True)
  # Nos controles de histórico, conferir apenas o novo bloco vigente.
  if p not in [report,A/'LEIA-ME.md']:
   text=p.read_text().split('\n\n',2)[2].split('\n\n',1)[0]
   tags=BeautifulSoup(markdown.markdown(text),'html.parser').find_all('a',href=True)
  for tag in tags:
   u=urlsplit(tag['href'])
   if not u.scheme and u.path:
    dest=(p.parent/unquote(u.path)).resolve()
    if not dest.is_file() and dest!=forthcoming:fail.append('Link: '+str(p.relative_to(R))+' '+tag['href'])
 assert not fail,fail
 save(forthcoming,{'registro':145,'entradas_anteriores':len(base),'arquivos_anteriores_atualizados':sorted(changed),'originais_preservados':104,'fontes_textuais_preservadas':99,'paginas_html_preservadas':99,'pdf_anterior_preservado':True,'pdf_novo':comp['pdf'],'sha256_pdf':digest,'paginas':383,'controles_atualizados':10,'demais_arquivos_anteriores_preservados':len(base)-10,'falhas':[],'metodo':'Todas as entradas anteriores auditadas. Somente dez controles de continuidade alterados; união com novo PDF e artefatos da composição e inspeção visual.'})
 files=[R/x for x in allowed]+[report,R/config['pdf_novo']]+[p for p in A.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
 updated=dict(base)
 for p in files:updated[p.relative_to(R).as_posix()]=sha(p)
 assert set(base)<=set(updated)
 save(M,updated);assert load(M)==updated
 print(json.dumps({'entradas_anteriores':len(base),'entradas_finais':len(updated),'arquivos_anteriores_atualizados':len(changed),'novas_entradas':len(set(updated)-set(base)),'falhas':0},ensure_ascii=False),flush=True)
if __name__=='__main__':main()
