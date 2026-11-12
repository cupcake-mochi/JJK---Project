"""Auditoria de continuidade R33: texto invariável, registro completo e composição."""
from pathlib import Path
from collections import defaultdict,Counter
import hashlib,json
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
B=Path(__file__).resolve().parent;R=B/'revisao-de-continuidade';OLD=B.parent/'livro-diagramado-r32'
def read(p):return json.loads(p.read_text())
def save(p,data):p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=read(B/'FONTES-E-VALIDACAO.json');old=read(OLD/'FONTES-E-VALIDACAO.json')
assert (B/'LIVRO-COMPLETO.md').read_bytes()==(OLD/'LIVRO-COMPLETO.md').read_bytes(),'O texto mudou'
assert sha(B/m['pdf'])==m['sha256_pdf']
changed_base=[f for f,h in read(R/'BASE-R32-HASHES.json').items() if not (OLD/f).is_file() or sha(OLD/f)!=h]
assert not changed_base,changed_base
for f in ['ESTUDO-DENSIDADE.json','ESTUDO-TABELAS.json','ESTUDO-SECAO.json','revisao-de-regras/ALTERACOES-REGRAS.json','CREDITOS.json','CAPA-E-ABERTURAS.json']:
 assert (B/f).read_bytes()==(OLD/f).read_bytes(),f
# Compare the ordered source elements, not just their word counts.
def source(m):return [(e['bloco'],e['tipo'],e['texto']) for e in m['eventos'] if not e['gerado']]
assert source(m)==source(old),'Mudança na ordem ou no conteúdo dos elementos editoriais'
assert [{k:v for k,v in p.items() if k!='pagina'} for p in old['posicionamento_imagens']]==[{k:v for k,v in p.items() if k!='pagina'} for p in m['posicionamento_imagens']]
assert set(old['ancoras'])==set(m['ancoras'])
def layout_stats(manifest):
 by=defaultdict(list)
 for e in manifest['eventos']:by[e['pagina']].append(e)
 W,H=A4;area=(W-38*mm)*(H-59*mm);rows=[];multiple=[]
 for p in manifest['paginas_planejadas']:
  if p['tipo']!='content':continue
  es=by[p['pagina']];used=sum(e['largura']*e['altura'] for e in es)/area*100
  bands=set(e['faixa'] for e in es if e['modo']=='duas-colunas')
  if len(bands)>1:multiple.append(p['pagina'])
  rows.append({'pagina':p['pagina'],'capitulo':p['capitulo'],'ocupacao_estimada_percentual':round(used,1),'pares_de_colunas':len(bands)})
 return rows,multiple
rows,multiple=layout_stats(m);previous,oldmultiple=layout_stats(old)
assert not multiple,multiple
# Every recorded complete introduction must share a column with its first child.
events=m['eventos'];heads={'h1','h2','h3','major','marker'};checked=[];unresolved=[]
for a in read(R/'ABERTURAS.json'):
 if a['ligacao']!='abertura completa' or 'unidos' not in a['resultado']:continue
 parents=[i for i,e in enumerate(events) if e['bloco']==a['bloco'] and e['tipo'] in heads and e['texto']==a['titulo']]
 good=False
 for i in parents:
  matches=[e for e in events[i+1:] if e['bloco']==a['bloco_entrada'] and e['tipo'] in heads and e['texto']==a['primeira_entrada']]
  if not matches:continue
  e=events[i];f=matches[0]
  if e['pagina']==f['pagina'] and abs(e['x']-f['x'])<.01:good=True;break
 if good:checked.append(a)
 else:unresolved.append(a)
assert not unresolved,unresolved
# Log every changed block, including generated continuation labels and tables.
def grouped(manifest):
 by=defaultdict(list)
 for e in manifest['eventos']:by[e.get('bloco') or '__elementos_gerados__'].append(e)
 return by
before,after=grouped(old),grouped(m);changes=[]
for block in dict.fromkeys([*before,*after]):
 if before[block]==after[block]:continue
 changes.append({'id':f'D33-{len(changes)+1:03d}','bloco':block,'antes':before[block],'depois':after[block],
  'motivo':'Recomposição da R32 para leitura de toda a coluna esquerda antes da direita; ligação de aberturas à primeira entrada, ajuste de tabelas à coluna quando legíveis e distribuição das sobras de página. Conteúdo editorial e ordem preservados.'})
save(R/'ALTERACOES-DIAGRAMACAO.json',changes)
save(R/'ALTERACOES-TEXTO.json',[])
save(R/'OCUPACAO-COMPARADA.json',{'metodo':'Soma das áreas dos elementos diagramados dividida pela área útil. Indicador de triagem; não mede legibilidade nem substitui inspeção visual. Capas, artes, sumários e formulários excluídos.','R32':previous,'R33':rows})
summary={'base':'R32','edicao':'R33','etapa':'6C','paginas_antes':old['paginas'],'paginas_depois':m['paginas'],
 'sha256_pdf':m['sha256_pdf'],'sha256_texto':sha(B/'LIVRO-COMPLETO.md'),'texto_identico':True,'elementos_editoriais_identicos_em_ordem':len(source(m)),
 'r32_preservada':True,'estilos_aprovados_preservados':True,'imagens_e_recortes_preservados':True,'mesmas_ancoras':len(m['ancoras']),
 'paginas_com_multiplos_pares_de_colunas_antes':oldmultiple,'paginas_com_multiplos_pares_de_colunas_depois':multiple,
 'paginas_textuais_com_ocupacao_inferior_a_25_antes':[p['pagina'] for p in previous if p['ocupacao_estimada_percentual']<25],
 'paginas_textuais_com_ocupacao_inferior_a_25_depois':[p['pagina'] for p in rows if p['ocupacao_estimada_percentual']<25],
 'aberturas_completas_verificadas_na_mesma_coluna':len(checked),'blocos_com_recomposicao_registrada':len(changes),'alteracoes_textuais':0,'problemas':[]}
save(R/'CONFERENCIA.json',summary);print(json.dumps(summary,ensure_ascii=False))
