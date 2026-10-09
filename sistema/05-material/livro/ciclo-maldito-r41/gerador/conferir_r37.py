"""Confere preservação, cobertura do registro, índice e percurso de leitura."""
from pathlib import Path
from collections import defaultdict,Counter
import json,re,hashlib,difflib
B=Path(__file__).resolve().parent;OLD=B.parent/'livro-diagramado-r36';R=B/'correcoes-pente-fino'
def read(p):return json.loads(p.read_text())
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a=read(OLD/'FONTES-E-VALIDACAO.json');m=read(B/'FONTES-E-VALIDACAO.json');changes=read(R/'ALTERACOES-TEXTO.json')
assert all(sha(OLD/f)==h for f,h in read(R/'BASE-R36-HASHES.json').items()),'Base R36 alterada'
old=(OLD/'LIVRO-COMPLETO.md').read_text();new=(B/'LIVRO-COMPLETO.md').read_text();expected=old
export=lambda s:re.sub(r'^(#{1,6}) ',lambda q:'#'*(len(q[1])+2)+' ',s,flags=re.M)
for c in changes:
 before=export(c['antes']);after=export(c['depois']);assert expected.count(before)==1,(c['id'],c['bloco'],'ocorrências no livro',expected.count(before))
 expected=expected.replace(before,after,1)
assert expected==new,'Há diferença não registrada no texto consolidado'
(R/'DIFERENCAS-TEXTO.patch').write_text(''.join(difflib.unified_diff(old.splitlines(keepends=True),new.splitlines(keepends=True),fromfile='R36/LIVRO-COMPLETO.md',tofile='R37/LIVRO-COMPLETO.md')))
for f in ['ESTUDO-DENSIDADE.json','ESTUDO-TABELAS.json','ESTUDO-SECAO.json','ESTUDO-CAPITULO.json','CREDITOS.json','CAPA-E-ABERTURAS.json','revisao-textual/ALTERACOES.json','revisao-de-regras/ALTERACOES-REGRAS.json']:
 assert (B/f).read_bytes()==(OLD/f).read_bytes(),f
assert a['fontes_locais_r30']==m['fontes_locais_r30']
assert a['imagens']==m['imagens']
for field in ['capas_e_aberturas','posicionamento_imagens']:
 strip=lambda rows:[{k:v for k,v in row.items() if k not in {'pagina','topo_texto_livre'}} for row in rows]
 assert strip(a[field])==strip(m[field]),field
source=lambda z:[e['bloco'] for e in z['eventos'] if not e['gerado']]
assert list(dict.fromkeys(source(a)))==list(dict.fromkeys(source(m))),'Ordem dos blocos mudou'
index=[]
for row in read(B/'revisao-de-estrutura/DESTINOS-INDICE.json'):
 title=row.get('titulo',row['termo']);target=next(e for e in m['eventos'] if e['bloco']==row['bloco'] and e['texto']==title and e['tipo'].startswith('h'))
 pos=m['ancoras'][row['alias']]
 assert pos['pagina']==target['pagina'],row
 assert abs(pos['x']-target['x'])<.01,row
 index.append({**row,'pagina':pos['pagina']})
save(R/'INDICE-CONFERIDO.json',index)
heads={'major','h1','h2','h3','marker'};orphans=[]
for i,e in enumerate(m['eventos']):
 if e['gerado'] or e['tipo'] not in heads:continue
 nxt=next((q for q in m['eventos'][i+1:] if not q['gerado']),None)
 if not nxt:continue
 if nxt['pagina']!=e['pagina'] or (e['largura']<300 and e['x']!=nxt['x']):orphans.append({'pagina':e['pagina'],'titulo':e['texto'],'proximo':nxt['texto']})
assert not orphans,orphans
by=defaultdict(list)
for e in m['eventos']:by[e['pagina']].append(e)
multi=[p for p,es in by.items() if len({e['faixa'] for e in es if e['modo']=='duas-colunas' and e['faixa']})>1]
assert not multi,multi
muro=[e for e in m['eventos'] if e['bloco']=='bastiao--bas-muro' and not e['gerado']]
start=next(i for i,e in enumerate(muro) if e['texto']=='Muro');end=next(i for i,e in enumerate(muro) if e['texto']=='Nível 11 — Guarda-Costas')
assert len({(e['pagina'],e['x']) for e in muro[start:end]})==1,'Muro separado de Alicerce'
# Toda alteração de composição é registrada por bloco, inclusive elementos gerados.
def groups(z):
 d=defaultdict(list)
 for e in z['eventos']:d[e['bloco'] or '__gerados__'].append(e)
 return d
before,after=groups(a),groups(m);rows=[]
for k in dict.fromkeys([*before,*after]):
 if before[k]!=after[k]:rows.append({'id':f'R37-D{len(rows)+1:03}','bloco':k,'antes':before[k],'depois':after[k],'motivo':'Correções autorizadas do pente fino: hierarquia, contextos, aberturas, encaixe de tabelas e continuidade; registro inclui a repaginação decorrente.'})
save(R/'ALTERACOES-DIAGRAMACAO.json',rows)
impl=['gerar_livro.py','ler_fontes.py','fluxo_continuo.py','revisao_r37.py','revisao-de-hierarquia/CLASSIFICACAO.json','DESTAQUES-CATALOGO.json'];patch=[];records=[]
for f in impl:
 p=OLD/f;q=B/f
 records.append({'arquivo':f,'sha256_antes':sha(p) if p.exists() else None,'sha256_depois':sha(q)})
 patch.extend(difflib.unified_diff(p.read_text().splitlines(keepends=True) if p.exists() else [],q.read_text().splitlines(keepends=True),fromfile='R36/'+f,tofile='R37/'+f))
save(R/'REGISTRO-IMPLEMENTACAO.json',records);(R/'IMPLEMENTACAO.patch').write_text(''.join(patch))
summary={'edicao':'R37','base':'R36','paginas_antes':a['paginas'],'paginas':m['paginas'],'sha256_pdf':sha(B/m['pdf']),'sha256_texto':sha(B/'LIVRO-COMPLETO.md'),'r36_preservada':True,'blocos_textuais_alterados':len(changes),'diferencas_textuais_nao_registradas':0,'registros_diagramacao':len(rows),'capas_artes_creditos_estilos_preservados':True,'titulos_isolados':orphans,'paginas_com_multiplos_pares_de_colunas':multi,'destinos_especificos_conferidos':len(index),'novos_destinos_corrigidos':13,'muro_e_primeira_habilidade_juntos':True,'pagina_muro':muro[start]['pagina'],'exemplos_com_contas_refeitas':0,'exemplos_reposicionados_ou_identificados':['Rodízio / Ninhada','Ajustar a Preparação','Recolher sob Ataque','Manifestação em Grupo'],'revisao_visual':'Registro separado após inspeção da prova final.'}
save(R/'CONFERENCIA.json',summary);print(json.dumps(summary,ensure_ascii=False))
