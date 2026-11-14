"""Integração das Origens v178 sobre R44: fonte final e registro exato."""
from pathlib import Path
import json,re,copy
B=Path(__file__).resolve().parent;R=B/'revisao-r45'
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def aplicar(textos,blocos,capitulos,meta,suplemento):
 rows=json.loads((B/'ALTERACOES-R44-para-R45.json').read_text())
 for row in rows:
  k=row['bloco'];a=row['antes'];z=row['depois']
  assert textos.get(k,'').strip()==a.strip(),k
  if not z:
   textos.pop(k,None);blocos.pop(k,None);meta.pop(k,None)
   continue
  textos[k]=z
  if k not in blocos:
   doc,anchor=k.split('--',1)
   blocos[k]=type(next(iter(blocos.values())))(doc,anchor,re.sub(r'^#+ ','',z.splitlines()[0]),z)
   meta[k]={'bloco':k,'capitulo':5,'titulo_original':blocos[k].title,'papel':'procedimento ou entrada','contexto':'Origens','parent':None,'marcador':None,'sem_titulo_inicial':False}
  headings=[{'titulo':m[2],'nivel':len(m[1]),'papel':'subtópico' if len(m[1])>=3 else 'seção' if len(m[1])==1 else 'procedimento ou entrada'} for m in re.finditer(r'^(#{1,6}) (.+)$',z,re.M)]
  meta[k]['titulos']=headings;meta[k]['nivel_primeiro']=headings[0]['nivel'];meta[k]['titulo_original']=headings[0]['titulo']
 order=json.loads((R/'ORDEM-ORIGENS.json').read_text())
 for ch in capitulos:
  for g in ch['grupos']:
   if g['doc']=='origens':
    g['blocks']=[blocos[k] for k in order];ch['titulo']='Origens'
 context='Origens'
 for k in order:
  first=textos[k].splitlines()[0]
  if first.startswith('# '):context=first[2:]
  if k=='origens--restricao-sem-energia':context='Restrição Celestial / Sem Energia'
  if k=='origens--restricao-corpo':context='Restrição Celestial / Restrição corporal'
  meta[k].update(contexto=context,sem_titulo_inicial=False,parent=None)
  # As seções principais continuam sendo destinos de marcadores e do sumário.
  meta[k]['marcador']=re.sub(r'^#+ ','',first) if first.startswith('# ') else None
 save(B/'revisao-de-estrutura/HIERARQUIA.json',meta)
 classification=json.loads((B/'revisao-r44/CLASSIFICACAO.json').read_text())
 changed={x['bloco'] for x in rows}
 classification=[x for x in classification if x['bloco'] not in changed]
 minorblocks={'origens--latente-beneficios','origens--receptaculo-excecoes','origens--descendente-beneficios','origens--encarnado-beneficios','origens--feto-beneficios','origens--corpo-ninhada-gemeos','origens--corpo-inteiro-manutencao','origens--restricao-beneficios','origens--restricao-menores-corporais'}
 for k in changed:
  if k not in meta:continue
  for h in meta[k]['titulos']:
   lev=h['nivel'];title=h['titulo']
   if lev<2:continue
   role='entrada' if lev==2 or (k in minorblocks and lev==3) else 'subtopico'
   if lev==2 and (title.startswith('Menores') or title in ['Traço e história','Histórias do corpo','Disputa pelo corpo','Outras referências de criação']):role='grupo'
   classification.append(dict(bloco=k,titulo=title,tipo_original='h'+str(min(lev,3)),tratamento=role,nivel_editorial=lev,motivo='R45: entrada nomeada, grupo de catálogo ou subtópico; estilos aprovados preservados.'))
 save(R/'CLASSIFICACAO.json',classification)
 nav=[x for x in json.loads((B/'revisao-r44/NAVEGACAO.json').read_text()) if x['capitulo']!=5]
 selected=['origens--origem-escolhas','origens--legados','origens--origem-latente','origens--origem-receptaculo','origens--origem-descendente','origens--descendente-zenin','origens--descendente-kamo','origens--descendente-gojo','origens--descendente-inumaki','origens--origem-encarnado','origens--origem-feto','origens--origem-corpo','origens--origem-reparo','origens--origem-restricao','origens--restricao-sem-energia','origens--restricao-corpo','origens--restricao-ce4','origens--origem-sem-tecnica','origens--legado-criar']
 for k in selected:
  nav.append(dict(capitulo=5,destino=k,titulo=re.sub(r'^#+ ','',textos[k].splitlines()[0]),nivel=3 if k in ['origens--descendente-zenin','origens--descendente-kamo','origens--descendente-gojo','origens--descendente-inumaki','origens--origem-reparo','origens--restricao-sem-energia','origens--restricao-corpo','origens--restricao-ce4'] else 2))
 nav.sort(key=lambda x:x['capitulo']);save(R/'NAVEGACAO.json',nav)
 for row in json.loads((R/'ALTERACOES-FICHAS.json').read_text()):
  assert suplemento[row['bloco']]==row['antes']
  suplemento[row['bloco']]=row['depois']
 # Validar todos os destinos depois da inserção das novas entradas.
 missing=[(k,t) for k,v in textos.items() for t in re.findall(r'\]\(#([^)]+)\)',v) if t not in blocos and not t.startswith(('indice-especifico-','indice-r37-'))]
 assert not missing,missing
 return rows
