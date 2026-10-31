from pathlib import Path
import json,re,hashlib
from pypdf import PdfReader
B=Path(__file__).resolve().parents[1]; O=B.with_name('livro-diagramado-r45');R=B/'revisao-r46'
a=(O/'LIVRO-COMPLETO.md').read_text();z=(B/'LIVRO-COMPLETO.md').read_text()
assert a.count(' (continuação)')==1
assert z==a.replace(' (continuação)',''), 'Mudança textual inesperada'
m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text()); old=json.loads((O/'FONTES-E-VALIDACAO.json').read_text());reader=PdfReader(B/m['pdf'])
hits=[]
for i,p in enumerate(reader.pages,1):
 if re.search(r'\(continuaç[ãa]o\)',p.extract_text() or '',re.I):hits.append(i)
assert not hits,hits
s=json.loads((R/'BASE-R45-SHA256.json').read_text())
bad=[f for f,h in s.items() if not (O/f).exists() or hashlib.sha256((O/f).read_bytes()).hexdigest()!=h]
assert not bad,bad
# Ignore only the authorized annotation, never prose or rule content.
def norm(x):
 if isinstance(x,str):return x.replace(' (continuação)','')
 if isinstance(x,list):return [norm(v) for v in x]
 return x
before=[(e['bloco'],e['tipo'],norm(e['texto']),e['gerado']) for e in old['eventos']]
after=[(e['bloco'],e['tipo'],norm(e['texto']),e['gerado']) for e in m['eventos']]
# Composition may insert fewer repeated context headings after line-height changes.
core_before=[v for v in before if not v[3]];core_after=[v for v in after if not v[3]]
assert core_before==core_after,'Diferença em elemento não gerado'
removed=sum(str(e['texto']).count('(continuação)') for e in old['eventos'])
result={'paginas':len(reader.pages),'rotulos_na_R45':removed,'rotulos_restantes':hits,'texto_MD':'Idêntico à R45 exceto a retirada do rótulo de um título','elementos_nao_gerados':'Idênticos após excluir o rótulo autorizado','R45_arquivos_preservados':len(s),'R45_divergencias':bad,'pdf_sha256':hashlib.sha256((B/m['pdf']).read_bytes()).hexdigest()}
(R/'VALIDACAO.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
