from pathlib import Path
import hashlib, json, shutil

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def gitsha(b): return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
old = json.loads((ROOT/'04 - Planejamento/apoio-piloto/manifesto-entrega.json').read_text(encoding='utf-8-sig'))
check = {'arquivos': len(old), 'ausentes': [], 'divergentes': []}
for rel, expected in old.items():
    p = ROOT/rel
    if not p.is_file(): check['ausentes'].append(rel)
    elif sha(p) != expected: check['divergentes'].append(rel)
origin = json.loads((HERE/'origem-github.json').read_text(encoding='utf-8'))
remote = {'commit': origin['commit'], 'iguais': 0, 'apenas_fim_de_linha': [], 'divergentes': [], 'ausentes': []}
for rel, expected in origin['arquivos'].items():
    if rel in ('README.md', 'SALVAMENTO.json'): continue
    p = ROOT/rel
    if not p.is_file(): remote['ausentes'].append(rel); continue
    b=p.read_bytes()
    if gitsha(b)==expected: remote['iguais']+=1
    elif gitsha(b.replace(b'\r\n',b'\n'))==expected: remote['apenas_fim_de_linha'].append(rel)
    else: remote['divergentes'].append(rel)
targets = [
 '04 - Planejamento/01-plano-completo-do-guia.md',
 '04 - Planejamento/02-decisoes-para-conversar.md',
 '04 - Planejamento/19-roteiro-pre-1-e-modelos.md',
 '04 - Planejamento/apoio-piloto/RETOMADA.md',
 '04 - Planejamento/apoio-piloto/manifesto-entrega.json',
 '06 - Redacao do Guia/LEIA-ME.md',
 '06 - Redacao do Guia/REFERENCIAS.md',
 '06 - Redacao do Guia/60-montar-habilidades-de-inimigos.md',
 '06 - Redacao do Guia/61-ficha-de-habilidade-de-inimigo.md',
]
snapshot = HERE/'historico/antes-do-encontro'
assert not snapshot.exists(), 'Snapshot já existe: não sobrescrever.'
for rel in targets:
    dest=snapshot/rel
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(ROOT/rel,dest)
report={'data':'2026-10-23','pasta_producao':str(ROOT),'pasta_sem_git':True,'manifesto_anterior':check,'github':remote,'protegidos':{p:sha(ROOT/p) for p in old if (ROOT/p).is_file()},'snapshot':{p:sha(ROOT/p) for p in targets},'r53_sha256':sha(HERE/'fontes/LIVRO-COMPLETO-R53.md')}
(HERE/'estado-inicial.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'manifesto':check,'github':remote,'r53':report['r53_sha256']},ensure_ascii=False,indent=2))
