"""Confere preservação, texto autorizado, linhas de tabelas e percurso de leitura."""
from pathlib import Path
from collections import defaultdict
import json,hashlib,re,difflib
B=Path(__file__).resolve().parent;O=B.parent/'livro-diagramado-r37';R=B/'revisao-r38'
read=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
changes=read(R/'ALTERACOES-TEXTO.json');original=(O/'LIVRO-COMPLETO.md').read_text();expected=original
for c in changes:
 def expand(t):return re.sub(r'^(#{1,6}) ',lambda m:'#'*(len(m[1])+2)+' ',t,flags=re.M)
 old,new=expand(c['antes']),expand(c['depois']);assert expected.count(old)==1,c['bloco'];expected=expected.replace(old,new,1)
actual=(B/'LIVRO-COMPLETO.md').read_text();assert actual==expected,'Diferença textual não registrada'
(R/'DIFERENCAS-TEXTO.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),actual.splitlines(True),fromfile='R37',tofile='R38')))
base=read(R/'BASE-R37-HASHES.json');assert all(sha(O/p)==v for p,v in base.items()),'R37 alterada'
m=read(B/'FONTES-E-VALIDACAO.json');oldm=read(O/'FONTES-E-VALIDACAO.json');assert sha(B/m['pdf'])==m['sha256_pdf']
for name in ['ESTUDO-DENSIDADE.json','ESTUDO-TABELAS.json','ESTUDO-SECAO.json','ESTUDO-CAPITULO.json','CREDITOS.json','CAPA-E-ABERTURAS.json','densidade_editorial.py','titulos_capitulo.py','titulos_secao.py','titulos_intermediarios.py']:
 assert sha(B/name)==sha(O/name),name
assert m['fontes_locais_r30']==oldm['fontes_locais_r30'];assert m['imagens']==oldm['imagens']
heads={'h1','h2','h3','major','marker'};source=[e for e in m['eventos'] if not e['gerado']];orphans=[]
for e,q in zip(source,source[1:]):
 if e['tipo'] in heads and (e['pagina']!=q['pagina'] or (e['largura']<300 and q['largura']<300 and e['x']!=q['x'])):orphans.append([e['pagina'],e['texto'],q['pagina'],q['texto']])
assert not orphans,orphans
by=defaultdict(list)
for e in m['eventos']:by[e['pagina']].append(e)
multi=[p for p,es in by.items() if len({e['faixa'] for e in es if e['modo']=='duas-colunas' and e['faixa']})>1];assert not multi,multi
bad_order=[]
for page,es in by.items():
 cols=[e for e in es if e['modo']=='duas-colunas' and e['faixa']]
 xs=[round(e['x']) for e in cols]
 if xs and any(xs[i]>xs[i+1] for i in range(len(xs)-1)):bad_order.append(page)
assert not bad_order,bad_order
source_tables={}
for match in re.finditer(r'<a id="([^\"]+--[^\"]+)"></a>\n(.*?)(?=\n<!-- fonte:|\n<a id="capitulo-|\Z)',actual,re.S):
 key,body=match.groups();rows=[]
 for l in body.splitlines():
  if l.startswith('|') and not re.fullmatch(r'[\s|:\-]+',l):rows.append([v.strip() for v in l.strip('|').split('|')])
 if rows:source_tables[key]=rows
repeated=0
for key,want in source_tables.items():
 tables=[e['texto'] for e in source if e['bloco']==key and e['tipo']=='table'];at=0;header=None
 for rows in tables:
  assert len(rows)>=2,(key,'cabeçalho sem linhas')
  for j,row in enumerate(rows):
   if at<len(want) and row==want[at]:at+=1
   elif j==0 and row==header:repeated+=1
   else:raise AssertionError(('Tabela mudou',key,at,row,want[at:at+1]))
  header=rows[0]
 assert at==len(want),(key,at,len(want))
double=[]
for a,b in zip(source,source[1:]):
 if a['tipo']==b['tipo']=='table' and a['bloco']==b['bloco'] and a['texto'][0]==b['texto'][0] and a['pagina']==b['pagina'] and a['x']==b['x']:double.append((a['pagina'],a['bloco']))
assert not double,double
# Every unchanged source paragraph/title appears in exactly the same order.
skip={r['bloco'] for r in changes}
def prose(man):return [(e['bloco'],e['tipo'],e['texto']) for e in man['eventos'] if not e['gerado'] and e['bloco'] not in skip and e['tipo']!='table']
assert prose(m)==prose(oldm),'Ordem ou redação de parágrafos não autorizada'
index=[]
for row in read(B/'revisao-de-estrutura/DESTINOS-INDICE.json'):
 title=row.get('titulo',row['termo']);e=next(e for e in m['eventos'] if e['bloco']==row['bloco'] and e['texto']==title and e['tipo'].startswith('h'));pos=m['ancoras'][row['alias']];assert pos['pagina']==e['pagina'] and abs(pos['x']-e['x'])<.01;index.append({**row,'pagina':pos['pagina']})
(R/'INDICE-CONFERIDO.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
def groups(man):
 r=defaultdict(list)
 for e in man['eventos']:r[e['bloco'] or '__gerados__'].append(e)
 return r
old,new=groups(oldm),groups(m);layout=[]
for k in dict.fromkeys([*old,*new]):
 if old[k]!=new[k]:layout.append({'id':f'R38-D{len(layout)+1:03}','bloco':k,'antes':old[k],'depois':new[k],'motivo':'Continuação entre parágrafos e linhas de tabela, cabeçalhos repetidos e equilíbrio das colunas; inclui a repaginação e as três alterações textuais autorizadas.'})
(R/'ALTERACOES-DIAGRAMACAO.json').write_text(json.dumps(layout,ensure_ascii=False,indent=2)+'\n')
result={'paginas':m['paginas'],'paginas_r37':oldm['paginas'],'sha256_pdf':sha(B/m['pdf']),'sha256_texto':sha(B/'LIVRO-COMPLETO.md'),'blocos_textuais_alterados':len(changes),'texto_identico_fora_das_tres_excecoes':True,'ordem_original_dos_paragrafos_preservada':True,'tabelas_linhas_preservadas':True,'cabecalhos_repetidos':repeated,'titulos_isolados':orphans,'paginas_com_multiplos_pares_de_colunas':multi,'retornos_da_direita_para_esquerda':bad_order,'cabecalhos_repetidos_sem_quebra':double,'r37_integralmente_preservada':True,'registros_diagramacao':len(layout)}
(R/'CONFERENCIA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(result)
