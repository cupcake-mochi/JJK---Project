from pathlib import Path
from collections import defaultdict
from pypdf import PdfReader
from PIL import Image
import json,hashlib,re
from identidade import nome_oficial
B=Path(__file__).resolve().parent;old=json.loads((B.parent/'livro-diagramado-r26/FONTES-E-VALIDACAO.json').read_text());m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());reader=PdfReader(B/m['pdf']);checks=0;issues=[]
def check(ok,label,detail=None):
 global checks
 checks+=1
 if not ok:issues.append({'tipo':label,'detalhe':detail})
def normalized(v):
 if isinstance(v,str):return nome_oficial(v)
 if isinstance(v,list):return [normalized(x) for x in v]
 return v
def body(rows):return [[e['bloco'],e['tipo'],normalized(e['texto'])] for e in rows if e['bloco'] and not e['gerado'] and e['tipo'] not in ['major','h1']]
check(body(old['eventos'])==body(m['eventos']),'Todo o texto, números, tabelas e exemplos da R26 preservados, exceto o nome oficial')
check(m['paginas']==old['paginas']+22,'Somente capa e vinte e uma aberturas acrescentadas')
check(len(m['capas_e_aberturas'])==22,'Todas as aberturas incluídas')
check(m['capas_e_aberturas'][0]['pagina']==1,'Capa primeira página')
check(m['ancoras']['sumario']['pagina']==2,'Sumário após a capa')
for a,ch in zip(m['capas_e_aberturas'][1:],m['capitulos']):
 check(a['capitulo']==ch['numero'] and a['titulo']==ch['titulo'],'Título e número correspondem ao capítulo',ch)
 check(a['pagina']+1==ch['pagina'],'Abertura imediatamente antes do capítulo',ch)
 check(a['sha256_original']==hashlib.sha256((B/a['arquivo']).read_bytes()).hexdigest(),'Original atualizado',ch['numero'])
 check(a['sha256_base']==hashlib.sha256((B/a['arquivo_base']).read_bytes()).hexdigest(),'Base das aberturas registrada',ch['numero'])
 text=reader.pages[a['pagina']-1].extract_text() or ''
 check(ch['titulo'] in text and 'Capítulo '+str(ch['numero']) in text,'Título pesquisável na abertura',ch)
 check(any(list(im.image.size)==[1024,1536] for im in reader.pages[a['pagina']-1].images),'Imagem nativa preservada',ch['numero'])
 annots=reader.pages[a['pagina']-1].get('/Annots',[]);ids={p.indirect_reference.idnum:i+1 for i,p in enumerate(reader.pages)}
 check(any(ids.get(ref.get_object().get('/Dest',[None])[0].idnum)==ch['pagina'] for ref in annots if ref.get_object().get('/Dest') and hasattr(ref.get_object()['/Dest'][0],'idnum')),'Faixa da abertura leva ao conteúdo do capítulo',ch['numero'])
# Compare all body content pages to the R26, ignoring only renamed words and new page offsets.
oldpages=defaultdict(list);newpages=defaultdict(list)
for e in old['eventos']:oldpages[e['pagina']].append([e['bloco'],e['tipo'],normalized(e['texto'])])
for e in m['eventos']:newpages[e['pagina']].append([e['bloco'],e['tipo'],normalized(e['texto'])])
oldordered=[v for k,v in sorted(oldpages.items()) if k!=old['creditos']['pagina']]
newordered=[v for k,v in sorted(newpages.items()) if k!=m['creditos']['pagina']]
check(oldordered==newordered,'Mesmos elementos e agrupamento por página após a inclusão das aberturas')
text='\n'.join(p.extract_text() or '' for p in reader.pages)
check(not re.search(r'\bProjeto\s*(?:[-–—]\s*)?M\b',text,re.I),'Nome antigo ausente da edição para o leitor')
check(reader.metadata.title=='Ciclo Maldito | Livro de regras','Nome oficial nos metadados')
check(m['creditos']['pagina']==m['paginas'],'Créditos preservados no final')
report={'sha256_pdf':m['sha256_pdf'],'checagens':checks,'problemas':issues,'capas_e_aberturas':m['capas_e_aberturas'],'regras_alteradas':[],'comparacao':'R26 com substituição do nome e acréscimo das vinte e duas páginas de capa/abertura. Todas as páginas de conteúdo mantêm a mesma composição por elementos.'}
(B/'evidencias/CONFERENCIA-CAPA-E-NOME-R28.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('Checagens:',checks,'Problemas:',len(issues));print(json.dumps(issues[:8],ensure_ascii=False,indent=2));raise SystemExit(bool(issues))
