from pathlib import Path
import shutil, subprocess, json, difflib, tempfile
root=Path.cwd(); out=root/'bestiario/05-sukuna/validacao-grade';out.mkdir(exist_ok=True)
files=['bestiario/05-sukuna/montar-sukuna-grade.js','bestiario/05-sukuna/SAIDA-sukuna-grade.json','bestiario/05-sukuna/SUKUNA-GRADE-ATUAL.md','sistema/03-mecanica/26-bestiario.md','sistema/03-mecanica/11-aptidoes-e-refino.md','sistema/05-material/livro/manual/40-fundamento.md','sistema/05-material/gerador-inimigo/conta.js','sistema/05-material/gerador-inimigo/dados.js']
base=Path(tempfile.mkdtemp(prefix='sukuna-grade-'))
for f in files:
 p=base/f;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/f,p)
def run(args):return subprocess.run(['node',str(base/files[0]),*args],text=True,capture_output=True)
b=run(['--check']); assert b.returncode==0,b.stderr
results=[{'caso':'base isolada','passou':True}]
cases=[('gasto-sem-cota',files[0],'if(!saldos.length || total+1e-9<custo)','if(false)',True,False),('falha-apaga-saldo',files[0],'permitido:false,saldos:[...saldos]','permitido:false,saldos:[]',True,False),('PV-final-no-lugar-da-base',files[0],'Math.floor(base/L/n)','Math.floor(pv/L/n)',True,False),('PV-com-fator-invertido',files[0],'/fatores.dominio/','*fatores.dominio/',True,False),('preco-Classe-4-congelado',files[0],'x[2]<=budget).at(-1)','x[2]<=budget && x[0]<=4).at(-1)',True,False),('braco-antigo',files[2],'157 PV','180 PV',False,False),('intervencao-inteira',files[1],'"media": 51','"media": 68',False,False),('controle-fonte-coerente',files[-1],"315, 945, 226","319, 945, 226",True,True)]
for name,f,old,new,regen,expected in cases:
 for original in files:shutil.copy2(root/original,base/original)
 p=base/f;s=p.read_text()
 if name=='controle-fonte-coerente':
  # Anchored to the actual source formatting rather than assuming spaces.
  import re
  m=re.search(r'315\s*,\s*945\s*,\s*226',s);assert m;old=m.group();new=old.replace('315','319',1)
 assert old in s,name
 changed=s.replace(old,new,1);assert changed!=s;p.write_text(changed)
 (out/(name+'.diff')).write_text(''.join(difflib.unified_diff(s.splitlines(True),changed.splitlines(True),fromfile=f,tofile=f)))
 r=run([] if regen else ['--check'])
 if r.returncode==0 and regen:r=run(['--check'])
 (out/(name+'.log')).write_text(r.stdout+r.stderr)
 assert (r.returncode==0)==expected,(name,r.stdout,r.stderr)
 results.append({'caso':name,'esperado':'passar' if expected else 'falhar','observado':'passou' if r.returncode==0 else 'falhou','codigo':r.returncode})
for f in files:shutil.copy2(root/f,base/f)
r=run(['--check']);assert r.returncode==0
results.append({'caso':'restauracao','passou':True})
(out/'resultados.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')

if Path(__file__).resolve() != (out/'executar.py').resolve():
 shutil.copy2(__file__,out/'executar.py')
print(json.dumps(results,ensure_ascii=False,indent=2))
