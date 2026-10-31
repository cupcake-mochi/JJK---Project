from pathlib import Path
import hashlib,json
from PIL import Image
from pypdf import PdfReader
B=Path(__file__).resolve().parent;oldB=B.parent/'livro-diagramado-r27'
m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());old=json.loads((oldB/'FONTES-E-VALIDACAO.json').read_text())
r=PdfReader(B/m['pdf']);prev=PdfReader(oldB/old['pdf']);checks=0;issues=[]
def check(ok,label):
 global checks
 checks+=1
 if not ok:issues.append(label)
original=Image.open(B/'capa/Ciclo-Maldito-Capa-Original.png').convert('RGB');base=Image.open(B/'capa/Ciclo-Maldito-Base-Aberturas.png').convert('RGB')
check(hashlib.sha256((B/'capa/Ciclo-Maldito-Capa-Original.png').read_bytes()).hexdigest()=='6253c90e06e04f1121956363abb4140ebec3fb64d51ed5a3ef78f5d10497a4b9','Capa original idêntica ao arquivo recebido')
check(original.size==base.size==(1024,1536),'Dimensões nativas preservadas')
a=original.tobytes();b=base.tobytes();changed=0
for i in range(1024*1536):
 if a[i*3:i*3+3]!=b[i*3:i*3+3]:
  changed+=1;x=i%1024;y=i//1024
  if not (104<=x<252 and 124<=y<1137):issues.append(f'Pixel alterado fora da área das letras: {x},{y}');break
checks+=1
covers={x['pagina'] for x in m['capas_e_aberturas']}
for n,p in enumerate(r.pages,1):
 if n in covers:
  expected=original if n==1 else base
  check(any(im.image.convert('RGB').tobytes()==expected.tobytes() and im.image.size==expected.size for im in p.images),f'Página {n}: bitmap incorporado idêntico à imagem original/base, sem filtro ou reamostragem')
 else:
  check(p.get_contents().get_data()==prev.pages[n-1].get_contents().get_data(),f'Página {n}: conteúdo visual preservado')
check(m['eventos']==old['eventos'],'Todos os textos e posições do conteúdo preservados')
check(m['ancoras']==old['ancoras'],'Destinos internos preservados')
check(m['imagens']==old['imagens'],'Quadros de mangá preservados')
check(m['paginas']==old['paginas']==498,'Paginação preservada')
report={'sha256_pdf':m['sha256_pdf'],'checagens':checks,'problemas':issues,'pixels_alterados_base':changed,'original_sha256':hashlib.sha256((B/'capa/Ciclo-Maldito-Capa-Original.png').read_bytes()).hexdigest(),'capa_principal':'Arquivo recebido preservado integralmente, sem filtro, restauração ou geração de arte.','aberturas':'Somente a área do texto antigo é limpa por difusão clássica. Novos nomes e números são texto vetorial. Couro, bordas, símbolos e restante da imagem preservados pixel a pixel.','paginas_de_conteudo':'Fluxos de desenho de todas as 476 páginas de conteúdo comparados diretamente ao PDF R27.','regras_alteradas':[]}
(B/'evidencias/CONFERENCIA-TROCA-DE-CAPA-R28.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('Checagens:',checks,'Problemas:',len(issues),issues[:5]);raise SystemExit(bool(issues))
