from pathlib import Path
import re,json,hashlib
R=Path('/media/mizuki/HD Externo II/Claude/Pesquisa de Campo - Mestragem')
A=R/'04 - Planejamento/apoio-revisao-integral-94'
LOG=A/'alteracoes.json'
def edit(rel,pairs,reason='Clareza e linguagem direta'):
 pairs=[(old,new) for old,new in pairs if old!=new]
 p=R/rel;t=p.read_text();entries=json.loads(LOG.read_text()) if LOG.exists() else []
 missing=[old for old,new in pairs if old not in t and new not in t]
 assert not missing,(rel,missing)
 for old,new in pairs:
  if old not in t:continue
  count=t.count(old);t=t.replace(old,new);entries.append({'fonte':rel,'antes':old,'depois':new,'ocorrencias':count,'motivo':reason})
 p.write_text(t,encoding='utf-8');LOG.write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
def source(n):
 return str(next((R/'06 - Redacao do Guia').glob(f'{n:02}-*.md')).relative_to(R))
def headings(n,pairs):edit(source(n),[(a,b) for a,b in pairs],'Título curto e claro; âncoras antigas serão preservadas')
