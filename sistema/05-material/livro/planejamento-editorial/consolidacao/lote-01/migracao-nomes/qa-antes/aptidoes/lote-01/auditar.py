from pathlib import Path
import runpy,json,hashlib
B=Path(__file__).resolve().parent;E=B/'evidencias';R=B.parents[5]
try:
 runpy.run_path(str(E/'conferir_aptidoes_candidata.py'),run_name='__main__')
except SystemExit as exc:
 if exc.code not in (None,0): raise
a=json.loads((E/'AUDITORIA-NUMERICA.json').read_text())
a['ok']=not a['falhas']
a['manuscritos_auditados']={str((B/'APTIDOES-E-REFINO.md').relative_to(R)):hashlib.sha256((B/'APTIDOES-E-REFINO.md').read_bytes()).hexdigest()}
(E/'auditoria-numerica.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
s={'ok':a['ok'],'sha256_texto':a['sha256_texto'],'casos':a['checks'],'casos_contextuais':'CASOS.json','limite':'Casos descritivos lidos não são apresentados como testes executados. Modelos e perturbações executados no script.'}
(E/'regras-verificadas.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':a['ok'],'checks':a['contagem_checks'],'falhas':a['falhas']},ensure_ascii=False))
