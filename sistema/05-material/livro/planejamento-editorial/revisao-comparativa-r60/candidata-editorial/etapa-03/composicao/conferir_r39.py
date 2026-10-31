"""Confere somente os acertos autorizados da R39 e a integridade da R38."""
from pathlib import Path
from collections import defaultdict
import json, hashlib, re, difflib
from pypdf import PdfReader

B=Path(__file__).resolve().parent; O=B.parent/'livro-diagramado-r38'; R=B/'revisao-r39'
read=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=read(R/'ALTERACOES-TEXTO.json'); old=(O/'LIVRO-COMPLETO.md').read_text(); expected=old
for row in rows:
 def expand(s):return re.sub(r'^(#{1,6}) ',lambda m:'#'*(len(m[1])+2)+' ',s,flags=re.M)
 a,z=expand(row['antes']),expand(row['depois']);assert expected.count(a)==1
 expected=expected.replace(a,z,1)
new=(B/'LIVRO-COMPLETO.md').read_text();assert new==expected,'Diferença textual não autorizada'
base=read(R/'BASE-R38-HASHES.json');assert all(sha(O/name)==value for name,value in base.items()),'R38 alterada'
m=read(B/'FONTES-E-VALIDACAO.json');om=read(O/'FONTES-E-VALIDACAO.json')
assert sha(B/m['pdf'])==m['sha256_pdf']
excluded={r['bloco'] for r in rows}
def prose(d):return [(e['bloco'],e['tipo'],e['texto']) for e in d['eventos'] if not e['gerado'] and e['bloco'] not in excluded]
assert prose(m)==prose(om),'Conteúdo ou ordem mudou fora do bloco autorizado'
for name in ['ESTUDO-DENSIDADE.json','ESTUDO-TABELAS.json','ESTUDO-SECAO.json','ESTUDO-CAPITULO.json','CREDITOS.json','CAPA-E-ABERTURAS.json','fluxo_continuo.py','tabelas_destaques.py','densidade_editorial.py','titulos_capitulo.py','titulos_secao.py','titulos_intermediarios.py']:
 assert sha(B/name)==sha(O/name),name
assert m['fontes_locais_r30']==om['fontes_locais_r30'];assert m['imagens']==om['imagens']
def by_block(d):
 result=defaultdict(list)
 for e in d['eventos']:result[e['bloco'] or '__gerados__'].append(e)
 return result
prev,now=by_block(om),by_block(m);layout=[]
for key in dict.fromkeys([*prev,*now]):
 if prev[key]!=now[key]:layout.append({'id':f'R39-D{len(layout)+1:03}','bloco':key,'antes':prev[key],'depois':now[key],'motivo':'Recomposição causada exclusivamente pelos acertos de termo autorizados nas Bênçãos.'})
(R/'ALTERACOES-DIAGRAMACAO.json').write_text(json.dumps(layout,ensure_ascii=False,indent=2)+'\n')
pdf=PdfReader(B/m['pdf']);opdf=PdfReader(O/om['pdf']);assert len(pdf.pages)==len(opdf.pages)
different=[i+1 for i,(a,z) in enumerate(zip(opdf.pages,pdf.pages)) if a.get_contents().get_data()!=z.get_contents().get_data()]
parts=[e for e in m['eventos'] if not e['gerado']]
for i,e in enumerate(parts[:-1]):
 if e['tipo'] in {'h1','h2','h3','major','marker'}:
  q=parts[i+1];assert e['pagina']==q['pagina'];assert e['largura']>300 or q['largura']>300 or e['x']==q['x']
result={'paginas_r38':om['paginas'],'paginas_r39':m['paginas'],'blocos_textuais_alterados':len(rows),
 'texto_identico_fora_do_bloco_registrado':True,'r38_integralmente_preservada':True,
 'fontes_tamanhos_estilos_arte_creditos_preservados':True,'paginas_pdf_com_desenho_diferente':different,
 'paginas_com_desenho_identico':len(pdf.pages)-len(different),'registros_diagramacao':len(layout),
 'sha256_pdf':sha(B/m['pdf']),'sha256_texto':sha(B/'LIVRO-COMPLETO.md')}
(R/'CONFERENCIA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(R/'DIFERENCAS-TEXTO.patch').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='R38',tofile='R39')))
print(json.dumps(result,ensure_ascii=False))
