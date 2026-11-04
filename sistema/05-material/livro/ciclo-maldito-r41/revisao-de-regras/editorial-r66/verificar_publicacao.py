from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import urllib.request,hashlib,json,concurrent.futures,subprocess
P=Path(__file__).resolve().parent
R=Path('/home/mizuki/JJK-v0.341-para-subir');Q=Path('/home/mizuki/JJK---PDF---RPG')
meta=json.loads((Q/'livro/EDICAO-ATUAL.json').read_text())
def fetch(pal):
 url=meta[pal]['url']
 request=urllib.request.Request(url,headers={'Cache-Control':'no-cache','User-Agent':'Ciclo-Maldito-publication-check'})
 with urllib.request.urlopen(request,timeout=45) as response:
  h=hashlib.sha256();size=0
  while chunk:=response.read(1024*1024):h.update(chunk);size+=len(chunk)
  result={'url':url,'url_final':response.url,'status':response.status,'tipo':response.headers.get('Content-Type'),'sha256':h.hexdigest(),'bytes':size}
  result['identico_ao_aprovado']=result['sha256']==meta[pal]['sha256']
  return pal,result
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:results=dict(ex.map(fetch,['claro','noturno']))
good=all(x['identico_ao_aprovado'] and x['status']==200 for x in results.values())
record={'estado':'publicada e verificada' if good else 'aguardando atualização pública','revisao':'R66','paginas':422,'commit_sistema':subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),'commit_pdf':subprocess.check_output(['git','rev-parse','HEAD'],cwd=Q,text=True).strip(),'verificado_em':datetime.now(ZoneInfo('America/Sao_Paulo')).isoformat(),'verificacao':'Download integral das duas URLs públicas e comparação SHA-256 com os PDFs aprovados ao fim da etapa 6.',**results}
(P/'PUBLICACAO.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False),flush=True)
raise SystemExit(0 if good else 1)

