"""Auditar o estado anterior e salvar o registro 142 por união."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
import json,hashlib,markdown
A=Path(__file__).resolve().parent;R=A.parents[1]
M=R/'04 - Planejamento/apoio-piloto/manifesto-entrega.json'
load=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def main():
 base=load(A/'antes/manifesto-entrega.json');assert len(base)==5062
 assert load(M)==base,'O manifesto mudou. Comparar antes de salvar.'
 c=load(A/'arquivos-do-lote.json');conf=load(A/'conferencia.json')
 assert not conf['falhas'] and conf['alteracoes_reproduzidas']==10 and conf['numeros_preservados']
 maths=load(A/'contas-conferidas.json');assert not maths['falhas']
 for row in maths['fontes']:assert sha(R/row['fonte'])==row['sha256'],row['fonte']
 allowed=set(c['controles']+c['fontes_alteradas']+c['html_alterados']);assert len(allowed)==15
 def inspect(item):
  rel,digest=item;p=R/rel
  if not p.is_file():return rel,'ausente',None
  actual=sha(p);return rel,'alterado' if actual!=digest else 'igual',actual
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
 for entry in original:
  if actuals.get(entry['fonte'])!=entry['sha256']:fail.append('Fonte original mudou: '+entry['fonte'])
 for row in load(A/'composicao.json')['ordem']:
  assert sha(R/row['fonte'])==row['sha256'],row['fonte']
 # Conferir também o que foi declarado como lido e seu estado final.
 for row in load(A/'leitura-realizada.json')['fontes_lidas']:
  assert sha(R/row['fonte'])==row['sha256'],row['fonte']
 assert actuals['08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf']=='0050d7cf2426ce3eba555ab2010deaeb6d62e023a5dba67ec43f0495e79cbd3b'
 report=R/c['relatorio']
 for tag in BeautifulSoup(markdown.markdown(report.read_text(),extensions=['tables']),'html.parser').find_all('a',href=True):
  u=urlsplit(tag['href'])
  if not u.scheme and u.path and not (report.parent/unquote(u.path)).resolve().is_file():fail.append('Link do relatório: '+tag['href'])
 assert not fail,fail
 result={'registro':142,'entradas_anteriores':len(base),'arquivos_anteriores_atualizados':sorted(changed),'originais_preservados':104,'demais_arquivos_anteriores_preservados':len(base)-len(changed),'fontes_alteradas':3,'paginas_html_alteradas':3,'controles_atualizados':9,'falhas':[],'metodo':'Todas as entradas anteriores auditadas. Apenas três fontes, três páginas de leitura e nove controles atualizados; união com os novos arquivos de leitura e seus estados anteriores.'}
 save(A/'conferencia-do-manifesto.json',result)
 files=[R/p for p in allowed]+[report]+[p for p in A.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
 updated=dict(base)
 for p in files:updated[p.relative_to(R).as_posix()]=sha(p)
 assert set(base)<=set(updated)
 save(M,updated)
 # Ler de volta o arquivo efetivamente salvo, sem repetir a leitura de milhares de artefatos.
 assert load(M)==updated
 print(json.dumps({'entradas_anteriores':len(base),'entradas_finais':len(updated),'arquivos_anteriores_atualizados':len(changed),'novas_entradas':len(set(updated)-set(base)),'falhas':0},ensure_ascii=False),flush=True)
if __name__=='__main__':main()
