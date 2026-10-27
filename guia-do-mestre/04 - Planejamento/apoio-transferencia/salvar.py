from pathlib import Path
import hashlib,json,shutil,zipfile,uuid
H=Path(__file__).resolve().parent;R=H.parent.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(obj):return json.dumps(obj,ensure_ascii=False,indent=2)+'\n'
mp=R/'04 - Planejamento/apoio-piloto/manifesto-entrega.json'
manifest=json.loads(mp.read_text(encoding='utf-8-sig'))
assert all((R/p).is_file() and sha(R/p)==v for p,v in manifest.items()),'Manifesto mudou: conferir antes de salvar.'
snapshot=H/'historico/antes-da-transferencia';assert not snapshot.exists()
ret='04 - Planejamento/apoio-piloto/RETOMADA.md'
for rel in [ret,mp.relative_to(R).as_posix()]:
 d=snapshot/rel;d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(R/rel,d)
p=R/ret
p.write_text(p.read_text(encoding='utf-8')+'\n## Transferência — 23/10/2026\n\nMizuki pediu salvar o processo para passar ao Codex. A retomada consolidada está em `RETOMADA-CODEX-2026-10-23.md`, na raiz de produção, com estado atual, fontes, entregas66/67, limites, próxima tarefa e cuidados com os verificadores históricos. `CONFERIR-SALVAMENTO.py` confere o manifesto atual sem escrever arquivos. Pacote portátil inclui planejamento e manuscrito completos com históricos e R53; bibliografia externa não incluída. Salvamento local, sem alteração do GitHub. A próxima etapa segue sendo a comparação de confronto com objetivo e pressão ambiental (Astra extra alto; prosa Sol alto).\n',encoding='utf-8',newline='\n')
for rel in [ret,'RETOMADA-CODEX-2026-10-23.md','CONFERIR-SALVAMENTO.py',Path(__file__).relative_to(R).as_posix()]:manifest[rel]=sha(R/rel)
mp.write_text(dump(manifest),encoding='utf-8')
assert all(sha(R/p)==v for p,v in manifest.items())
paths=[R/'LEIA-ME.md',R/'RETOMADA-CODEX-2026-10-23.md',R/'CONFERIR-SALVAMENTO.py']
for folder in ['04 - Planejamento','06 - Redacao do Guia']:
 paths.extend(p for p in (R/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
inventory={p.relative_to(R).as_posix():sha(p) for p in sorted(paths)}
out=R.parent/'Salvamentos do Guia';out.mkdir(exist_ok=True)
package=out/('guia-do-mestre-2026-10-23-ate-secao64-'+uuid.uuid4().hex[:6]+'.zip')
meta={'data':'2026-10-23','estado':'plano57; pauta51; planejamento67; manuscrito64','manifesto_producao':len(manifest),'publicado_no_github':False,'exclusoes':['bibliografia externa','PDFs de pesquisa','outras pastas de pesquisa','__pycache__'],'arquivos':inventory}
with zipfile.ZipFile(package,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in sorted(paths):z.write(p,'guia-do-mestre/'+p.relative_to(R).as_posix())
 z.writestr('guia-do-mestre/SALVAMENTO-TRANSFERENCIA.json',dump(meta))
with zipfile.ZipFile(package) as z:
 assert z.testzip() is None
 for rel,expected in inventory.items():assert hashlib.sha256(z.read('guia-do-mestre/'+rel)).hexdigest()==expected,rel
receipt={'pacote':str(package),'sha256':sha(package),'arquivos_no_pacote':len(inventory)+1,'manifesto_producao':len(manifest),'conteudo_conferido':True,'publicado_no_github':False}
package.with_suffix('.json').write_text(dump(receipt),encoding='utf-8')
print(dump(receipt))
