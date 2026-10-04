from pathlib import Path
import re,json,hashlib
B=Path(__file__).resolve().parent;R=B.parents[5];checks=[]
for path in sorted((B/'sincronizacoes').glob('*.md')):
 text=path.read_text();src=re.search(r'Fonte(?: principal)?: `([^`]+)`',text)[1];content=(R/src).read_text()
 recorded=re.search(r'SHA-256(?: da fonte)?: `([0-9a-f]+)`',text)[1]
 checks.append({'arquivo':path.name,'verificacao':'hash da fonte','ok':hashlib.sha256((R/src).read_bytes()).hexdigest()==recorded})
 before=re.findall(r'\*\*Antes\*\*\s+```markdown\n(.*?)\n```',text,re.S)
 for i,block in enumerate(before,1):
  n=content.count(block);checks.append({'arquivo':path.name,'verificacao':f'trecho anterior{i}','ocorrencias':n,'ok':n==1})
out={'ok':all(c['ok'] for c in checks),'checks':checks,'quantidade':len(checks),'escopo':'Âncoras e fonte principal dos cinco patches; conteúdo novo não é aplicado nem validado exaustivamente por esta busca.'}
(B/'evidencias/sincronizacoes-verificadas.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':out['ok'],'quantidade':len(checks),'falhas':[c for c in checks if not c['ok']]},ensure_ascii=False));raise SystemExit(0 if out['ok'] else 1)
