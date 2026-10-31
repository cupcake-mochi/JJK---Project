from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import urllib.request,json,hashlib
out=Path(__file__).parent
expected=json.loads(Path('/home/mizuki/JJK---PDF---RPG/livro/EDICAO-ATUAL.json').read_text())
headers={'Cache-Control':'no-cache','User-Agent':'Ciclo-Maldito-Verificacao-R57'}
with urllib.request.urlopen(urllib.request.Request('https://ciclo-maldito.vercel.app/livro/EDICAO-ATUAL.json',headers=headers),timeout=40) as f:actual=json.load(f)
assert expected==actual,'Metadados diferentes'
def check(key):
 info=expected[key];h=hashlib.sha256();size=0
 with urllib.request.urlopen(urllib.request.Request(info['url'],headers=headers),timeout=120) as f:
  result={'url':info['url'],'url_final':f.geturl(),'status':f.status,'tipo':f.headers.get_content_type()}
  assert f.status==200 and result['tipo']=='application/pdf'
  while chunk:=f.read(1024*1024):h.update(chunk);size+=len(chunk)
 assert h.hexdigest()==info['sha256'],f'{key}: PDF divergente'
 result.update({'sha256':h.hexdigest(),'bytes':size});print(key,'idêntico ao aprovado',size,flush=True);return key,result
with ThreadPoolExecutor(max_workers=2) as pool:checks=dict(pool.map(check,['claro','noturno']))
report={'resultado':'aprovado','revisao':'R57','paginas':415,'metadados_identicos':True,'pdfs':checks,'verificado_em':datetime.now(timezone.utc).isoformat()}
(out/'VERIFICACAO-PUBLICADA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Publicação verificada integralmente.',flush=True)
