from pathlib import Path
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib,json,re,unicodedata
import pdfplumber
from pypdf import PdfReader
B=Path(__file__).resolve().parent;ROOT=B.parents[5]
checks=[]
def ck(name,got,want):checks.append(dict(verificacao=name,obtido=got,esperado=want,ok=got==want))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def words(s):return re.findall(r'\w+',unicodedata.normalize('NFKC',s).casefold())
md=(B/'DANO-E-CONDICOES.md').read_text();meta=json.loads((B/'ESTRUTURA.json').read_text())
a=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',md)
sections={a[i]:a[i+2] for i in range(1,len(a),3)}
pdf=B/'output/pdf/Projeto-M-Dano-e-Condicoes-Proposta-01.pdf';r=PdfReader(pdf)
ck('Oito páginas e seções', [len(r.pages),len(sections)], [8,8])
ck('Ordem de leitura',list(sections),meta['ordem'])
ck('Subtítulos não repetem título da seção',[k for k,s in sections.items() if '## '+meta['titulos'][k]+'\n' in s],[])
ck('Todos os títulos coincidem com o mapa', [k for k,s in sections.items() if s.splitlines()[0]!='# '+meta['titulos'][k]],[])
top=[o for o in r.outline if not isinstance(o,list)]
ck('Duas entradas principais',len(top),2)
ck('Grupos iniciam recolhidos',[x.get('/Count') for x in top if x.get('/Count')],[-4,-4])
def flatten(nodes):
 for o in nodes:
  if isinstance(o,list):yield from flatten(o)
  else:yield o
out=list(flatten(r.outline));ck('Marcadores com destinos válidos',all(0<=r.get_destination_page_number(o)<8 for o in out),True)
geometry=[]
with pdfplumber.open(pdf) as doc:
 for n,(p,(key,chunk)) in enumerate(zip(doc.pages,sections.items()),1):
  clean=re.sub(r'\[([^\]]+)\]\(#[^)]+\)',r'\1',chunk)
  t=p.extract_text(x_tolerance=1,y_tolerance=3)
  ck(f'p{n}: sem palavras perdidas',dict(Counter(words(clean))-Counter(words(t))),{})
  chars=[c for c in p.chars if c['text'].strip()];body=[c for c in chars if 48<c['top']<785]
  ck(f'p{n}: limites físicos',all(0<=c['x0']<=c['x1']<=p.width and 0<=c['top']<=c['bottom']<=p.height for c in chars),True)
  ck(f'p{n}: rodapé separado',max(c['bottom'] for c in body)<785,True)
  used={c['fontname'] for c in chars};embedded=[]
  for f in r.pages[n-1]['/Resources']['/Font'].values():
   font=f.get_object();d=font.get('/FontDescriptor')
   if d and any(k in d.get_object() for k in ['/FontFile','/FontFile2','/FontFile3']):embedded.append(str(font['/BaseFont']).lstrip('/'))
  ck(f'p{n}: fontes incorporadas',sorted(used-set(embedded)),[])
  ck(f'p{n}: sem imagens raster',len(p.images),0)
  refs=re.findall(r'\]\(#([^)]+)\)',chunk)
  ck(f'p{n}: referências existentes', [x for x in refs if x not in meta['paginas']],[])
  page_ids={p.indirect_reference.idnum:i+1 for i,p in enumerate(r.pages)}
  destinations=[]
  for ref in r.pages[n-1].get('/Annots',[]):
   obj=ref.get_object()
   if obj.get('/Subtype')=='/Link':
    dest=obj.get('/Dest');destinations.append(page_ids.get(dest[0].idnum) if dest else None)
  ck(f'p{n}: links PDF para destinos esperados',sorted(set(destinations)),sorted(set(meta['paginas'][x] for x in refs)))
  for ref in set(refs):
   ck(f'p{n}: número da remissão {ref}',f"(p. {meta['paginas'][ref]})" in t,True)
  geometry.append({'pagina':n,'secao':key,'final_corpo':round(max(c['bottom'] for c in body),2),'links':destinations})

from math import ceil, floor
# Exercícios numéricos desta candidata. Não são um simulador do combate inteiro.
# Os valores esperados são resoluções manuais; invariantes confrontam cada etapa.
def parcela(dano, resist=False, vuln=False, imune=False):
 if imune:return 0
 fator=Fraction(1,2) if resist else Fraction(1)
 if vuln:fator*=2
 return ceil(dano*fator)
def impacto(parcelas, rd, temp):
 dano=max(0,sum(parcelas)-rd)
 absorvido=min(dano,temp)
 return dict(dano=dano,absorvido=absorvido,vida=dano-absorvido,temp=temp-absorvido)
ck('Exemplo Rina: resistência',parcela(21,True),11)
ck('Exemplo Rina: RD e vida temporária',impacto([11],4,3),dict(dano=7,absorvido=3,vida=4,temp=0))
ck('Ordem resistência antes de RD',impacto([parcela(40,True)],27,0)['dano'],0)
ck('Contraprova: ordem inversa mudaria resultado',parcela(40-27,True),7)
ck('Resistência + vulnerabilidade no dano ímpar',parcela(21,True,True),21)
ck('Imunidade prevalece',parcela(21,True,True,True),0)
ck('Dano zero permanece zero',parcela(0,True),0)
ck('Dano misto: resistência só na parcela',10+parcela(8,True),14)
ck('RD global uma vez',impacto([10,parcela(8,True)],3,0)['dano'],11)
ck('RD maior que dano não cura',impacto([4],9,2),dict(dano=0,absorvido=0,vida=0,temp=2))
ck('Duro: dados crus + Constituição',7+4+3,14)
ck('Casca: dados independentes menos1 + Constituição',6+5-1+3,13)
ck('Reduções somadas no exemplo',40-(14+13),13)
ck('Cobrir-se refino ímpar',[floor(Fraction(3,2)*r) for r in [1,2,3,5,10]],[1,3,4,7,15])
ck('Proteção perdida altera Defesa e Bloquear',[17-4,17-4-11],[13,2])
# Limiares por contagem independente de frações inteiras, sem arredondar o limiar.
def fracao_estagio(maximo,atual):
 return sum(4*(maximo-atual)>=k*maximo for k in range(1,5))
def atualizar(maximo,atual,anterior=0,falha=False):
 return min(4,max(anterior,fracao_estagio(maximo,atual))+int(falha))
ck('Integridade Kaori',20+(1+5)*(2-1),26)
ck('Integridade NPC ímpar',35//2,17)
ck('Limiares exatos max26',[fracao_estagio(26,26-perda) for perda in [0,6,7,12,13,19,20,25,26]],[0,0,1,1,2,2,3,3,4])
ck('Perda de7 e TR aprovado',atualizar(26,19),1)
ck('Perda de7 e TR falho',atualizar(26,19,falha=True),2)
ck('Novo dano sem novo TR mantém estágio maior',atualizar(26,18,2),2)
stage=0
for perda in range(1,5):stage=atualizar(26,26-perda,stage,True)
ck('Risco registrado:4falhas com perda4 chegam ao estágio4',stage,4)
ck('Remenda restaura reserva sem retirar estágio na candidata',atualizar(26,26,2),2)
ck('Metade da Classe não libera acesso novo',[0 if c==0 else max(1,c//2) for c in [0,1,2,3,5]],[0,1,1,1,2])
ck('Alma e vida temporária: perdas de vida/Integridade',[impacto([7],0,3)['vida'],7],[4,7])
# Grade de invariantes: perdas nunca negativas e todo ponto final tem destino.
falhas=[];grade=0
for d in range(51):
 for rd in [0,1,4,27,60]:
  for temp in [0,3,20,60]:
   x=impacto([parcela(d,True)],rd,temp);grade+=1
   if min(x.values())<0 or x['vida']+x['absorvido']!=x['dano'] or x['temp']+x['absorvido']!=temp:falhas.append([d,rd,temp])
ck('1020 combinações: conservação de dano e vida temporária',falhas,[])
ck('Grade cobre1020 casos',grade,1020)
grupos=[]
for grupo in ['Físicos','Elementais','Especiais']:
 linha=next(x for x in sections['tipos'].splitlines() if x.startswith('| '+grupo+' |'))
 grupos.append(re.split(r', | e ',linha.split('|')[2].strip().rstrip('.')))
ck('Tipos:14 sem repetição, grupos3/6/5',[len(set(sum(grupos,[]))),[len(x) for x in grupos]],[14,[3,6,5]])
ck('Condições:13, grupos6/2/5',[len(re.findall(r'^## ',sections[k],re.M))-(1 if k=='medias' else 1 if k=='pesadas' else 0) for k in ['leves','medias','pesadas']],[6,2,5])
ck('Exceção crítica mantida','como Golpe Cirúrgico' in md,True)
ck('Estágio4 encerra Aguentar','O estágio 4 encerra a possibilidade de Aguentar.' in md,True)
ck('Campos de saída sem default inventado','esses campos precisam ser preenchidos antes de entrar em jogo' in md,True)
ck('Metade dos dados distingue metade do resultado','metade dos dados e metade do resultado são procedimentos diferentes' in md,True)
ck('34 casos documentais com IDs únicos',len({x['id'] for x in json.loads((B/'evidencias/casos-documentais.json').read_text())}),34)
rev=json.loads((B/'evidencias/REVISAO-EDITORIAL.json').read_text())
ck('Oito seções avaliadas editorialmente',sorted(x['id'] for x in rev['secoes']),sorted(sections))
ck('Revisão ligada ao texto',rev['sha256_texto'],sha(B/'DANO-E-CONDICOES.md'))
snap=json.loads((B/'evidencias/fontes-preservadas.json').read_text())
ck('Fontes e consolidado anterior preservados',[n for n,h in snap.items() if sha(ROOT/n)!=h],[])
base=ROOT/'sistema/05-material/livro/planejamento-editorial'
inv=json.loads((base/'INVENTARIO-BASE.json').read_text())
ck('Livro e exportações preservados',[x['arquivo'] for x in inv['fontes']+inv['artefatos_publicados'] if sha(ROOT/x['arquivo'])!=x['sha256']],[])
protected=json.loads((base/'regras-comuns/lote-03/evidencias/preservacao-base.json').read_text())
ck('137 arquivos protegidos',[n for n,h in protected.items() if sha(ROOT/n)!=h],[])
visual=json.loads((B/'evidencias/inspecao-visual.json').read_text())
ck('Inspeção visual ligada ao PDF',visual['sha256_pdf'],sha(pdf))
ck('Oito páginas visualmente examinadas',[x['pagina'] for x in visual['paginas']],list(range(1,9)))
ck('Sem defeitos visuais registrados',all(x['resultado']=='sem defeito visual observado' for x in visual['paginas']),True)
ck('34 casos documentais',rev['casos_documentais'],34)
broken=[]
for p in B.rglob('*.md'):
 for href in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if re.match(r'^[a-z]+:',href) or href.startswith('#'):continue
  target=p.parent/href.split('#')[0]
  if target.name=='CONFERENCIA.json':continue
  if not target.exists():broken.append([str(p.relative_to(B)),href])
ck('Links do dossiê',broken,[])
res={'data':'2026-10-03','ok':all(x['ok'] for x in checks),'sha256_texto':sha(B/'DANO-E-CONDICOES.md'),'sha256_pdf':sha(pdf),'verificacoes':len(checks),'checks':checks,'geometria':geometry,'limites':['Não é teste humano ou prova de equilíbrio.','Revisão pelo autor, sem nova revisão independente.','Decisões candidatas e pendências identificadas em DECISOES.md.']}
(B/'CONFERENCIA.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':res['ok'],'verificacoes':len(checks),'falhas':[x for x in checks if not x['ok']]},ensure_ascii=False,indent=2))
raise SystemExit(0 if res['ok'] else 1)
