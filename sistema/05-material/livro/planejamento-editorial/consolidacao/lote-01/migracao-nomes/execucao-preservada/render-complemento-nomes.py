from pathlib import Path
import subprocess,json,hashlib,concurrent.futures
P=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial');M=P/'consolidacao/lote-01/migracao-nomes';units=['aptidoes/lote-01','origens/lote-01'];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def render(n):
 b=P/n;conf=json.loads((b/'VALIDACAO.json').read_text());old=M/'qa-antes'/n/'output/pdf'/conf['pdf'];new=b/'output/pdf'/conf['pdf'];folder=Path('/tmp/qa-nomes')/n;records=[]
 if sha(old)==sha(new):return {'unidade':n,'sha256_antes':sha(old),'sha256_depois':sha(new),'paginas':conf['paginas'],'alteradas':[],'PDF_identico':True}
 for mode,pdf in [('antes',old),('depois',new)]:
  out=folder/mode;out.mkdir(parents=True,exist_ok=True);subprocess.run(['pdftoppm','-png','-r','100',str(pdf),str(out/'pagina')],check=True)
 a=sorted((folder/'antes').glob('*.png'));c=sorted((folder/'depois').glob('*.png'));assert len(a)==len(c)==conf['paginas']
 for i,(o,p) in enumerate(zip(a,c),1):records.append({'pagina':i,'igual':sha(o)==sha(p),'sha256_antes':sha(o),'sha256_depois':sha(p),'imagem':str(p)})
 r={'unidade':n,'sha256_antes':sha(old),'sha256_depois':sha(new),'paginas':conf['paginas'],'alteradas':[x['pagina'] for x in records if not x['igual']],'registros':records,'PDF_identico':False}
 (b/'evidencias/COMPARACAO-NOMES-PDF.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');return r
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(render,units))
old={r['unidade']:r for r in json.loads((M/'QA-PIXELS.json').read_text())};old.update({r['unidade']:r for r in results});results=list(old.values())
(M/'QA-PIXELS.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
for x in results:print(x['unidade'],x['alteradas'])
