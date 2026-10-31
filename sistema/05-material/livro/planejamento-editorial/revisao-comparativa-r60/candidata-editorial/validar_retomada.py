from pathlib import Path
import hashlib,json,shutil,sys
H=Path(__file__).resolve().parent
S=H/'etapa-03'
e=json.loads((S/'ENTREGA.json').read_text())
for item in e['arquivos']:
    p=S/'output/pdf'/Path(item['arquivo']).name
    assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],p
    q=S/'composicao/output/pdf'/p.name
    q.parent.mkdir(parents=True,exist_ok=True)
    if not q.exists():shutil.copy2(p,q)
for n in ['VALIDACAO.json','VALIDACAO-ETAPA-03.json']:
    assert json.loads((S/'revisao'/n).read_text())['resultado']=='aprovado'
assert json.loads((H/'PLANEJAMENTO.json').read_text())['proxima_etapa']==4
print('PDFs e registros íntegros. Próxima etapa: 4, Diagramas.')
