"""Conferir o fechamento e atualizar por união, preservando a base anterior ao registro 135."""
from pathlib import Path
import hashlib,json,subprocess,sys
from bs4 import BeautifulSoup
from urllib.parse import unquote,urlsplit

A=Path(__file__).resolve().parent;R=A.parents[1]
M=R/'04 - Planejamento/apoio-piloto/manifesto-entrega.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def main():
 base=load(A/'retomada/antes-do-fechamento/manifesto-entrega.json')
 current=load(M);assert len(base)==3914 and current==base,'Manifesto mudou desde o início do fechamento; comparar antes de prosseguir.'
 logs=[]
 for script in ['CONFERIR.py','LEVANTAR.py','CONCORDANCIA.py','AUDITAR-RETOMADA.py']:
  p=subprocess.run([sys.executable,str(A/script)],text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  logs.append('### '+script+'\n'+p.stdout)
  print(script, 'concluído' if p.returncode==0 else 'falhou',flush=True)
  assert p.returncode==0,p.stdout[-6000:]
 (A/'retomada/conferencia-final.txt').write_text('\n\n'.join(logs))
 audit=load(A/'retomada/auditoria-independente.json');conf=load(A/'conferencia.json');visual=load(A/'retomada/revisao-visual.json')
 assert not audit['falhas'] and not conf['falhas']
 assert conf['alteracoes']==283 and audit['registros_de_alteracao_reproduzidos']==283
 assert sha(R/visual['pdf'])==visual['pdf_sha256']
 assert len(visual['paginas'])==20 and not visual['palavras_fora_da_pagina']
 for page in visual['paginas']:assert page['inspecionada'] and sha(R/page['imagem'])==page['sha256']
 config=load(A/'arquivos-do-lote.json');allowed=set(config['controles']+config['fontes_revisadas']+config['extras'])
 assert set(audit['arquivos_anteriores_alterados'])==allowed,(len(audit['arquivos_anteriores_alterados']),len(allowed))
 # O índice novo tem de acompanhar as cópias atuais, não as provas antigas.
 data=load(A/'destinos-e-fontes.json');q=load(A/'fila-dos-casos.json')
 assert sum(len(v) for v in data['casos'].values())==59
 for rows in [q['casos'],q['outras_consultas_pendentes']]:
  for row in rows:assert row['consulta_atual']==row['fonte_revisada'] and sha(R/row['fonte_revisada'])==row['sha256_revisado']
 assert len(q['outras_consultas_pendentes'])==17 and q['casos_pendentes']==0 and q['consultas_pendentes']==0
 failures=[];links=0
 for path in [A/'casos-completos.html',A/'guia-de-consulta.html']:
  for tag in BeautifulSoup(path.read_text(),'html.parser').find_all('a',href=True):
   u=urlsplit(tag['href'])
   if u.scheme or not u.path:continue
   links+=1
   if not (path.parent/unquote(u.path)).resolve().is_file():failures.append((path.name,tag['href']))
 assert not failures,failures
 meta={'registro':135,'pdf':visual['pdf'],'pdf_sha256':visual['pdf_sha256'],'html':str((A/'prova-textual.html').relative_to(R)),'paginas':visual['paginas'],'trechos_visiveis':246,'arquivos_com_alteracao_visivel':43,'fontes_conferidas':94,'limite':'Prova comparativa. Fontes editáveis vigentes; diagramação e leitura do conjunto integrado ainda pendentes.'}
 (A/'amostra.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
 result={'registro':135,'entradas_anteriores':len(base),'arquivos_anteriores_atualizados':sorted(allowed),'novos_indices_links_conferidos':links,'originais_preservados':104,'falhas':[],'metodo':'Auditoria independente de todas as entradas anteriores, reprodução das alterações e inspeção das 20 páginas; atualização por união restrita aos controles, fontes declaradas e novos arquivos do registro 135.'}
 (A/'conferencia-do-manifesto.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 files=[R/p for p in allowed]+[R/config['relatorio']]+[p for p in A.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
 updated=dict(current)
 for p in files:updated[p.relative_to(R).as_posix()]=sha(p)
 assert set(base)<=set(updated)
 M.write_text(json.dumps(updated,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'entradas_anteriores':len(base),'entradas_finais':len(updated),'arquivos_anteriores_atualizados':len(allowed),'novas_entradas':len(set(updated)-set(base)),'falhas':0},ensure_ascii=False),flush=True)

if __name__=='__main__':main()
