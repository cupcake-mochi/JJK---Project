"""Fechar somente o registro 136; atualizar o manifesto por união após as conferências."""
from pathlib import Path
import json,hashlib,subprocess,sys
from bs4 import BeautifulSoup
from urllib.parse import urlsplit,unquote
A=Path(__file__).resolve().parent;R=A.parents[1]
M=R/'04 - Planejamento/apoio-piloto/manifesto-entrega.json'
load=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def main():
 base=load(A/'antes/manifesto-entrega.json');current=load(M);config=load(A/'arquivos-do-lote.json')
 assert len(base)==4104 and current==base,'O manifesto mudou; comparar antes de atualizar.'
 for name in ['CONFERIR-INTEGRACAO.py','CONFERIR-PDF.py']:
  p=subprocess.run([sys.executable,str(A/name)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  print(name,p.stdout[-2000:],flush=True);assert p.returncode==0,p.stdout
 v=load(A/'revisao-visual.json');assert len(v['paginas'])==7 and sha(R/v['pdf'])==v['pdf_sha256']
 for page in v['paginas']:assert page['inspecionada'] and sha(R/page['imagem'])==page['sha256']
 allowed=set(config['controles']);assert len(allowed)==9
 changed=[];fail=[]
 for i,(rel,digest) in enumerate(base.items(),1):
  p=R/rel
  if not p.is_file():fail.append('Ausente: '+rel)
  elif sha(p)!=digest:
   changed.append(rel)
   if rel not in allowed:fail.append('Alteração não declarada: '+rel)
  if i%1000==0:print('Entradas anteriores conferidas:',i,flush=True)
 assert set(changed)==allowed,(changed,allowed)
 # As 104 fontes do sumário anterior e todas as entradas originais deste lote ficam preservadas.
 original=load(R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json')['fontes'];assert len(original)==104
 for entry in original:
  if sha(R/entry['fonte'])!=entry['sha256']:fail.append('Fonte original mudou: '+entry['fonte'])
 origins=load(A/'fontes-reunidas.json')
 for entry in origins:
  if sha(R/entry['origem'])!=entry['sha256_origem']:fail.append('Origem mudou: '+entry['origem'])
 oldpdf=R/'08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf'
 assert sha(oldpdf)=='0050d7cf2426ce3eba555ab2010deaeb6d62e023a5dba67ec43f0495e79cbd3b'
 # Conferir os destinos locais do relatório e dos novos apontamentos de continuidade.
 report=R/config['relatorio'];import markdown
 for tag in BeautifulSoup(markdown.markdown(report.read_text(),extensions=['tables']),'html.parser').find_all('a',href=True):
  u=urlsplit(tag['href'])
  if not u.scheme and u.path and not (report.parent/unquote(u.path)).resolve().is_file():fail.append('Link do relatório: '+tag['href'])
 assert not fail,fail
 record={'registro':136,'entradas_anteriores':len(base),'originais_preservados':104,'fontes_de_entrada_preservadas':len(origins),'arquivos_anteriores_atualizados':sorted(changed),'pdf_anterior_preservado':True,'falhas':[],'metodo':'Auditoria de todas as entradas anteriores; atualização por união restrita aos nove controles e aos novos artefatos de integração. O guia de consulta antigo não é alterado.'}
 save(A/'conferencia-do-manifesto.json',record)
 newdirs=[A,R/config['manuscrito_integrado'],R/config['edicao_html']]
 files=[R/p for p in allowed]+[report]+[p for d in newdirs for p in d.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
 updated=dict(base)
 for p in files:updated[p.relative_to(R).as_posix()]=sha(p)
 assert set(base)<=set(updated)
 save(M,updated)
 print(json.dumps({'entradas_anteriores':len(base),'entradas_finais':len(updated),'arquivos_anteriores_atualizados':len(changed),'novas_entradas':len(set(updated)-set(base)),'falhas':0},ensure_ascii=False),flush=True)
if __name__=='__main__':main()
