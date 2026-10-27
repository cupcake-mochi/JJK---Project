#!/usr/bin/env python3
"""Confere cobertura, fontes e navegação da primeira edição; não certifica equilíbrio ou aprendizagem."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
from collections import Counter
import argparse,hashlib,json,os,re,sys
from bs4 import BeautifulSoup

ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--fontes',type=Path);ap.add_argument('--preparado',type=Path);args=ap.parse_args()
H=Path(__file__).absolute().parent;R=args.fontes or H.parents[1];O=args.preparado;P='04 - Planejamento';E='07 - Edicao de Leitura'
def path(rel):return O/rel if O and (O/rel).is_file() else R/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
state=load(H/'estado-inicial.json');data=load(H/'cobertura-atualizada.json');prior=load(path(state['cobertura_anterior']));problems=[]
def ck(ok,msg):
 if not ok:problems.append(msg)
evidence=0
for group,n in [('pontos',130),('competencias',20)]:
 before={r['id']:r for r in prior[group]};ck(len(data[group])==len({r['id'] for r in data[group]})==n,'Inventário duplicado/incompleto: '+group);ck(set(before)=={r['id'] for r in data[group]},'Inventário alterado: '+group)
 for row in data[group]:
  old=before[row['id']];exc={'evidencias'}
  if row['id'] in ['M051','P20']:
   field='falta' if group=='pontos' else 'restante';exc|={'estado','presente',field,'lote'}
   if row['id']=='M051':exc.add('delimitacao_autoral');ck('descartado' in row['delimitacao_autoral'],'Delimitação autoral ausente')
   ck(old['estado']=='P' and row['estado']=='E' and row[field]==row['lote']=='—','Transição indevida: '+row['id'])
  ck({k:v for k,v in row.items() if k not in exc}=={k:v for k,v in old.items() if k not in exc},'Escopo alterado: '+row['id'])
  for e in row['evidencias']:
   p=path(e['arquivo']);ck(p.is_file(),'Evidência ausente: '+e['arquivo'])
   if not p.is_file():continue
   ck(sha(p)==e['sha256'],'Resumo divergente: '+e['arquivo']);ls=p.read_text().splitlines();valid=1<=e['inicio']<=e['fim']<=len(ls);ck(valid,'Linhas inválidas: '+e['arquivo'])
   if valid:ck(ls[e['inicio']-1].lstrip('# ').strip()==e['titulo'],'Título divergente: '+e['arquivo'])
   evidence+=1
 ck(Counter(r['estado'] for r in data[group])=={'E':n},'Cobertura não concluída: '+group)
ck(data['totais_pontos']=={'E':130,'P':0,'L':0},'Totais de pontos divergentes');ck(data['totais_competencias']=={'E':20,'P':0},'Totais de competências divergentes');ck(all(not r['aprendizagem_observada'] for r in data['competencias']),'Aprendizagem indevidamente declarada')
for b in data['lotes']:
 old=next(x for x in prior['lotes'] if x['id']==b['id']);ck(b==({**old,'estado':'entregue'} if b['id']=='L4' else old),'Lote fora de escopo: '+b['id'])
for name in ['fonte_R53','copia_R53']:ck(sha(Path(state[name]))==state['R53_sha256'],'R53 alterada')
edition=path(E+'/mapa-editorial.json');ed=load(edition);ck(not ed['problemas'],'Gerador registrou problema');ck(len(ed['fontes'])==103 and len(ed['historicos_excluidos'])==2,'Destinos incompletos');ck(len(ed['cortes_editoriais'])==4,'Cortes editoriais divergentes')
covered=set()
for s in ed['fontes']+ed['historicos_excluidos']:
 ck(sha(path(s['fonte']))==s['sha256'],'Fonte da edição alterada: '+s['fonte'])
 if s['fonte'].startswith('06 - Redacao do Guia/'):covered.add(int(Path(s['fonte']).name.split('-')[0]))
ck(covered==set(range(1,104)),'Texto numerado sem destino')
ck(len([p for p in ed['capitulos'] if p['codigo'].startswith('C')])==10,'Capítulos incompletos');ck(len(next(p for p in ed['capitulos'] if p['codigo']=='FICHAS')['consultas'])==17,'Ferramentas incompletas')
htmlfiles=[E+'/index.html',E+'/fontes-e-limites.html']+[E+'/'+p['pagina'] for p in ed['capitulos']];soups={};ids={};links=0;local=0;tables=0;resources=0;images=0
for rel in htmlfiles:
 p=path(rel);ck(p.is_file(),'Página ausente: '+rel)
 if not p.is_file():continue
 soup=BeautifulSoup(p.read_text(),'html.parser');soups[rel]=soup;allids=[str(e['id']) for e in soup.find_all(attrs={'id':True})];ids[rel]=set(allids);ck(len(allids)==len(set(allids)),'ID duplicado: '+rel);ck(soup.html and soup.html.get('lang')=='pt-BR','Idioma ausente');ck(bool(soup.find('main',id='conteudo')),'Corpo principal ausente');ck(len(soup.find_all('h1'))==1,'Título principal divergente');tables+=len(soup.find_all('table'));images+=len(soup.find_all('img'))
def resolve(rel,target,anchor_required=True):
 global links,local,resources
 u=urlsplit(target)
 if u.scheme in ['http','https','mailto','tel','data']:return
 ck(not u.scheme,'Protocolo inesperado: '+target)
 logical=os.path.normpath(str((R/rel).parent/unquote(u.path))) if u.path else str(R/rel)
 if logical.startswith(str(R)+os.sep):dest=os.path.relpath(logical,R);p=path(dest)
 else:dest=None;p=Path(logical)
 ck(p.is_file(),f'Destino ausente em {rel}: {target}');local+=1
 if u.fragment and dest in ids:ck(unquote(u.fragment) in ids[dest],f'Âncora ausente em {rel}: {target}')
for rel,soup in soups.items():
 for a in soup.find_all('a',href=True):links+=1;resolve(rel,a['href'])
 for e in soup.find_all(['script','link','img']):
  target=e.get('src') or (e.get('href') if e.name=='link' else None)
  if target:resources+=1;ck(not urlsplit(target).scheme,'Recurso depende de rede: '+target);resolve(rel,target)
raw=path(E+'/dados-busca.js').read_text();ck(raw.startswith('window.CM_SEARCH=') and raw.rstrip().endswith(';'),'Índice de busca inválido');index=json.loads(raw[len('window.CM_SEARCH='):].strip().removesuffix(';'));expected={s['id'] for s in ed['fontes'] if s['tipo']!='revelacoes'}
ck(len(index)==102 and {s['id'] for s in index}==expected,'Busca inclui ou omite consulta');ck('s087' not in {s['id'] for s in index},'Revelações incluídas na busca')
for s in index:resolve(E+'/index.html',s['url'])
md=path(E+'/GUIA-DO-MESTRE-PRE-1.0.md').read_text();mdids=re.findall(r'<a id="([^"]+)"',md);ck(len(mdids)==len(set(mdids)),'IDs duplicados no manuscrito');ck(expected<=set(mdids),'Consulta ausente no manuscrito');ck('s087' not in mdids,'Corpo com revelações incluído no manuscrito')
for fragment in re.findall(r'\]\(#([^)]+)\)',md):ck(fragment in mdids,'Remissão interna ausente no Markdown: '+fragment)
ck('Yuji e Choso caçando maldições' not in raw and 'Yuji e Choso caçando maldições' not in md,'Trecho de revelação no corpo principal')
ck('fetch(' not in path(E+'/busca.js').read_text(),'Busca requer acesso de rede')
g92=path('06 - Redacao do Guia/92-reserva-condensada-proposta-e-comparacao.md').read_text();ck('Conferência demonstrada' in g92 and 'Último Fôlego' in g92,'Conferência de Reserva ausente');ck(all(x in g92 for x in ['Quantidade guardada por ocasião','Momento permitido','Condições de armazenamento','Máximo acumulável']),'Campo publicado ausente')
preview=H/'previa-da-edicao.jpg';ck(preview.is_file() and preview.read_bytes().startswith(b'\xff\xd8'),'Prévia ausente')
out=dict(etapa=91,evidencias_conferidas=evidence,pontos={'E':130,'P':0,'L':0},competencias={'E':20,'P':0},capitulos=10,paginas_HTML=len(htmlfiles),fontes_incorporadas=103,fontes_numeradas_com_destino=len(covered),consultas_na_busca=len(index),links_HTML=links,destinos_locais_conferidos=local,recursos_locais=resources,tabelas_HTML=tables,imagens_no_corpo=images,IDs_no_manuscrito=len(mdids),cortes_editoriais=4,R53_intacta=not any('R53' in p for p in problems),observacao_no_navegador={'abertura':'capturada e inspecionada em navegador local','busca':'socorro:48 consultas, Quedas e socorro no topo; clique abriu consulta22','apresentacao':'desktop; sem avaliação por leitores externos ou teste móvel real','previa':'previa-da-edicao.jpg'},limites='Integração estrutural, remissões, fontes e navegação. Sem nova revisão semântica integral de cada passagem, aprendizagem observada ou validação de equilíbrio.',problemas=problems)
print(json.dumps(out,ensure_ascii=False,indent=2));sys.exit(bool(problems))
