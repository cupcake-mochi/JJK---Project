from pathlib import Path
import hashlib,json,shutil
H=Path(__file__).resolve().parent
R=H.parent.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((R/'04 - Planejamento/apoio-piloto/manifesto-entrega.json').read_text(encoding='utf-8-sig'))
bad=[p for p,s in m.items() if not (R/p).is_file() or sha(R/p)!=s]
assert not bad,bad
targets=['04 - Planejamento/01-plano-completo-do-guia.md','04 - Planejamento/02-decisoes-para-conversar.md','04 - Planejamento/19-roteiro-pre-1-e-modelos.md','04 - Planejamento/apoio-piloto/RETOMADA.md','04 - Planejamento/apoio-piloto/manifesto-entrega.json','06 - Redacao do Guia/LEIA-ME.md','06 - Redacao do Guia/REFERENCIAS.md']
snapshot=H/'historico/antes-do-perigo'
assert not snapshot.exists()
for rel in targets:
 d=snapshot/rel;d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(R/rel,d)
report={'data':'2026-10-23','manifesto_inicial':m,'snapshot':{p:sha(R/p) for p in targets},'r53_sha256':sha(R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md')}
(H/'estado-inicial.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'{len(m)} arquivos íntegros; histórico preservado.')
