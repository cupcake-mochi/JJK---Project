from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json, re, hashlib, unicodedata
from pypdf import PdfReader
import pdfplumber
L=Path(__file__).resolve().parent;R=L.parent;B=L.parents[5]
checks=[]
def check(name,value,want):
 checks.append({'verificacao':name,'obtido':value,'esperado':want,'ok':value==want})
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def tok(t):return re.findall(r'\w+',unicodedata.normalize('NFKC',t).casefold())
MOV=R/'lote-02/02-SALTOS-E-QUEDAS.md';FUR=L/'03-PERCEPCAO-E-FURTIVIDADE.md'
ms=MOV.read_text();fs=FUR.read_text()
# Conferir a tabela que o leitor recebe, em vez de copiar seus valores no teste.
rows=re.findall(r'^\| ([0-6]) \| ([\d,]+) m \| ([\d,]+) m \|$',ms,re.M)
check('Sete valores de Força na tabela',len(rows),7)
for a,h,s in rows:
 a=int(a);actual=[F(h.replace(',','.')),F(s.replace(',','.'))];horizontal=3+F(3,2)*a;standing=F(3,2)*int(horizontal/3)
 check(f'Salto por Força {a}',[str(v) for v in actual],[str(horizontal),str(standing)])
for h,n in [(1.5,0),(3,1),(4.5,1),(6,2),(7.5,2),(9,3),(10.5,3),(30,10),(60,20),(150,20)]:check(f'Queda {h}',min(20,int(F(str(h))/3)),n)
for p in [MOV,FUR]:
 distances=[F(v.replace(',','.')) for v in re.findall(r'(?<![\w,])([0-9]+(?:,[0-9]+)?)\s*m\b',p.read_text())]
 check(f'Múltiplos de 1,5 m em {p.name}',[str(v) for v in distances if (v/F(3,2)).denominator!=1],[])
check('Rina, percurso simples',[3+4.5,9-3-4.5],[7.5,1.5])
check('Assassino, percurso e teste',[6+4.5,12-6-4.5,10+4>=14],[10.5,1.5,True])
check('Queda curta, Vida final',14-4,10)
check('Ocultação por observador',[15>=8+4,15>=8+8],[True,False])
check('Busca e empate',11+4>=15,True)
check('Busca múltipla',[15>=12,15>=17],[True,False])
check('Manutenção do arco',[min(16,8)+4,(min(16,8)+4)>=12],[12,True])
for bonus,expected in [(4,'11/20'),(7,'7/10'),(10,'17/20')]:check(f'Extensão CD 14, bônus {bonus}',str(F(sum(i+bonus>=14 for i in range(1,21)),20)),expected)
check('Esconder, bônus iguais',str(F(sum(i+4>=12 for i in range(1,21)),20)),'13/20')
check('Manter, bônus iguais/desvantagem',str(F(sum(min(i,j)+4>=12 for i in range(1,21) for j in range(1,21)),400)),'169/400')
check('Queda 3d6 contra 14 de Vida',str(F(sum(a+b+c>=14 for a in range(1,7) for b in range(1,7) for c in range(1,7)),216)),'35/216')
check('Teto 20d6 não zera Incursor30 CON0',20*6<6+29*4,True)
# Regressões concretas das revisões: não são detecção de qualidade literária.
for name,needle,source in [('Dois limites de salto','**nos dois limites**',ms),('Falha combinada anunciada','consequência combinada',ms),('Apoios especiais reservados','pertence ao Parkour do Assassino',ms),('Sem reação universal de borda','nem uma Reação geral',ms),('Manutenção só de ocultação anterior','já não estava oculto',fs),('Sem Ver conservado','localizar por energia não substitui enxergar',fs),('Silencioso conservado','perceber o efeito não revela automaticamente sua origem',fs),('Vulto','**Visão às cegas**',fs),('Escuridão não bloqueia luz ao fundo','Um alvo iluminado além do trecho escuro ainda pode ser visto',fs),('Faro pelo nome vigente','**Faro**',fs),('Grupo','pelo menos metade precisa passar',fs)]:check(name,needle in source,True)
check('Nome de Faro corrigido','Faro de Origem' in fs,False)
# PDF: texto distribuído em páginas esperadas, sem confundir extração com inspeção visual.
results={}
for name,src,pdf in [('movimento',MOV,R/'lote-02/output/pdf/Projeto-M-Movimento-Saltos-e-Quedas-Proposta-02.pdf'),('percepcao',FUR,L/'output/pdf/Projeto-M-Percepcao-e-Furtividade-Proposta-03.pdf')]:
 reader=PdfReader(pdf);chunks=re.split(r'<!-- page:[^>]+ -->\s*',src.read_text())[1:]
 check(f'{name}: páginas',len(reader.pages),4);check(f'{name}: marcadores',len(reader.outline),4);check(f'{name}: destinos',[reader.get_destination_page_number(d)+1 for d in reader.outline],[1,2,3,4])
 pages=[]
 with pdfplumber.open(pdf) as doc:
  for n,(page,chunk) in enumerate(zip(doc.pages,chunks),1):
   check(f'{name} p{n}: texto ausente',dict(Counter(tok(chunk))-Counter(tok(page.extract_text(x_tolerance=1,y_tolerance=3)))),{})
   chars=[c for c in page.chars if c['text'].strip()];body=[c for c in chars if 48<c['top']<785]
   check(f'{name} p{n}: limites',all(0<=c['x0']<=c['x1']<=page.width and 0<=c['top']<=c['bottom']<=page.height for c in chars),True)
   check(f'{name} p{n}: rodapé separado',max(c['bottom'] for c in body)<785,True)
   used=set(c['fontname'] for c in chars);embedded=[]
   for fontref in reader.pages[n-1]['/Resources']['/Font'].values():
    font=fontref.get_object();d=font.get('/FontDescriptor')
    if d and any(k in d.get_object() for k in ['/FontFile','/FontFile2','/FontFile3']):embedded.append(str(font['/BaseFont']).lstrip('/'))
   check(f'{name} p{n}: fontes usadas incorporadas',sorted(used-set(embedded)),[])
   pages.append({'pagina':n,'final_corpo':round(max(c['bottom'] for c in body),2),'bitmap':len(page.images)})
 check(f'{name}: sem bitmap',sum(p['bitmap'] for p in pages),0)
 results[name]={'fonte':str(src.relative_to(B)),'pdf':str(pdf.relative_to(B)),'hash_fonte':sha(src),'hash_pdf':sha(pdf),'paginas':pages,'marcadores':[d.title for d in reader.outline]}
inv=json.loads((B/'sistema/05-material/livro/planejamento-editorial/INVENTARIO-BASE.json').read_text());changed=[]
for x in inv['fontes']+inv['artefatos_publicados']:
 p=B/x['arquivo']
 if not p.exists() or sha(p)!=x['sha256']:changed.append(x['arquivo'])
check('Fontes e exportações da v0.331 preservadas',changed,[])
protected=json.loads((L/'evidencias/preservacao-base.json').read_text());changed=[]
for name,h in protected.items():
 p=B/name
 if not p.exists() or sha(p)!=h:changed.append(name)
check('Retrato de arquivos protegidos preservado',changed,[])
broken=[]
for folder,names in [(R/'lote-02',['LEIA-ME.md','02-DECISOES.md','RELATORIO.md']),(L,['LEIA-ME.md','03-DECISOES.md','RELATORIO.md'])]:
 for name in names:
  p=folder/name
  for href in re.findall(r'\]\(([^)]+)\)',p.read_text()):
   if re.match(r'^[a-z]+:',href) or href.startswith('#'):continue
   target=(p.parent/href.split('#')[0]).resolve()
   if not target.exists() and target.name!='CONFERENCIA.json':broken.append([str(p.relative_to(B)),href])
check('Links locais da entrega',broken,[])
result={'data':'2026-10-02','base':'v0.331','status':'candidatas de integração','ok':all(c['ok'] for c in checks),'verificacoes':checks,'documentos':results,'preservacao':{'fontes':len(inv['fontes']),'exportacoes':len(inv['artefatos_publicados']),'retrato':len(protected),'conjuntos_sobrepostos':True},'inspecao_visual':'As oito páginas finais foram examinadas pelo agente principal. Textos, quadros e rodapés legíveis, sem cortes encontrados.','limites':['Testes conferem contas e integridade; não provam compreensão humana.','Pareceres de agentes anteriores às correções finais; autor conferiu correções.','Não houve teste humano ou validação integral de equilíbrio.','Energia em 9 m é uma proposta nova, sem afirmação de cânone.']}
(L/'CONFERENCIA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(R/'lote-02/CONFERENCIA.json').write_text(json.dumps({'revisao':2,'ok':result['ok'],'documento':results['movimento'],'conferencia_completa':'../lote-03/CONFERENCIA.json'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'ok':result['ok'],'falhas':[c for c in checks if not c['ok']],'preservacao':result['preservacao']},ensure_ascii=False,indent=2))
