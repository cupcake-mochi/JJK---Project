from pathlib import Path
import subprocess,json,sys,concurrent.futures
r=Path('/home/mizuki/JJK-v0.341-para-subir');p=Path(__file__).resolve().parent;out=p/'validadores';out.mkdir(exist_ok=True)
py='/home/mizuki/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3'
jobs=[(f.name,[py,str(f)]) for f in sorted((r/'sistema/03-mecanica').glob('conferir-*.py'))]
jobs += [('repositorio',[py,str(r/'conferir-repositorio.py')]),('integridade-atual',[py,str(r/'sistema/05-material/livro/ciclo-maldito-r41/revisao-de-regras/editorial-r57/testar-integridade.py')]),('integridade-base',[py,str(r/'sistema/05-material/livro/ciclo-maldito-r41/revisao-de-regras/fundamento-r53/testar-integridade.py')])]
def run(job):
 name,cmd=job
 with (out/(name+'.log')).open('w') as f:z=subprocess.run(cmd,cwd=r,stdout=f,stderr=subprocess.STDOUT)
 print(name,z.returncode,flush=True);return {'validador':name,'codigo_saida':z.returncode}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:results=list(ex.map(run,jobs))
(p/'VALIDADORES.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
sys.exit(any(x['codigo_saida'] for x in results))

