"""R44: decisões do autor em 12/10/2026; camada exata sobre a R43."""
from pathlib import Path
import json,re,copy
B=Path(__file__).resolve().parent;R=B/'revisao-r44'
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def aplicar(textos,blocos,capitulos,meta):
 rows=json.loads((B/'ALTERACOES-R43-para-R44.json').read_text())
 for row in rows:
  k=row['bloco'];a=row['antes'];z=row['depois']
  assert textos.get(k,'').strip()==a.strip(),k
  if not z:
   del textos[k];del blocos[k];meta.pop(k,None)
   for ch in capitulos:
    for grupo in ch['grupos']:grupo['blocks']=[b for b in grupo['blocks'] if b.key!=k]
   continue
  textos[k]=z
  if not a:
   doc,anchor=k.split('--',1);title=re.sub(r'^#+ ','',z.splitlines()[0])
   block=type(next(iter(blocos.values())))(doc,anchor,title,z)
   blocos[k]=block
   for ch in capitulos:
    for grupo in ch['grupos']:
     if any(b.key=='ritual--pacto-restricao' for b in grupo['blocks']):
      i=next(i for i,b in enumerate(grupo['blocks']) if b.key=='ritual--pacto-restricao');grupo['blocks'].insert(i+1,block)
   meta[k]={'bloco':k,'capitulo':15,'titulo_original':title,'papel':'procedimento ou entrada','contexto':'Pactos','parent':None,'marcador':None,'sem_titulo_inicial':False}
  cfg=meta[k];headings=[]
  for m in re.finditer(r'^(#{1,6}) (.+)$',z,re.M):
   headings.append({'titulo':m[2],'nivel':len(m[1]),'papel':'subtópico' if len(m[1])>=3 else 'seção' if len(m[1])==1 else 'procedimento ou entrada'})
  cfg['titulos']=headings;cfg['nivel_primeiro']=headings[0]['nivel'] if headings else 0
  if k.startswith('fabricacao--'):cfg['contexto']='Criação de entidades'
  if headings:cfg['titulo_original']=headings[0]['titulo']
 save(B/'revisao-de-estrutura/HIERARQUIA.json',meta)
 # Os novos títulos usam os mesmos tratamentos aprovados nas revisões anteriores.
 existing=json.loads((B/'revisao-r41/CLASSIFICACAO.json').read_text())
 changed={r['bloco'] for r in rows}
 current={(k,h['titulo']) for k in changed if k in meta for h in meta[k]['titulos']}
 classification=[v for v in existing if v['bloco'] not in changed or (v['bloco'],v['titulo']) in current]
 known={(r['bloco'],r['titulo']) for r in classification}
 for k,title in sorted(current):
  h=next(h for h in meta[k]['titulos'] if h['titulo']==title)
  if h['nivel']<3 or (k,title) in known:continue
  classification.append({'bloco':k,'titulo':title,'tipo_original':'h3','tratamento':'exemplo' if k=='ritual--pacto-exemplos' else 'subtopico','nivel_editorial':3,'motivo':'R44: aplicar o tratamento já aprovado à função do título novo.'})
 save(R/'CLASSIFICACAO.json',classification)
 nav=json.loads((B/'revisao-r40/NAVEGACAO.json').read_text())
 for row in nav:
  if row.get('destino')=='fabricacao--fab-entidades':row['titulo']='Criação de entidades'
 save(R/'NAVEGACAO.json',nav)
 return rows
