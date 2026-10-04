from pathlib import Path
from collections import Counter
from fractions import Fraction
import hashlib, json, re, unicodedata
from pypdf import PdfReader
import pdfplumber

L=Path(__file__).resolve().parent
ROOT=L.parents[5]
SRC=L/'05-ENERGIA-E-VESTIGIOS.md'
PDF=L/'output/pdf/Projeto-M-Energia-e-Vestigios-Revisao-02.pdf'
checks=[]
def check(name, got, expected):
 checks.append({'verificacao':name,'obtido':got,'esperado':expected,'ok':got==expected})
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def words(s):return re.findall(r'\w+',unicodedata.normalize('NFKC',s).casefold())
s=SRC.read_text()
r=PdfReader(PDF)
chunks=re.split(r'<!-- page:[^>]+ -->\s*',s)[1:]
check('Páginas',len(r.pages),5)
check('Seções de leitura',len(chunks),5)
check('Marcadores selecionados',len(r.outline),5)
check('Destinos dos marcadores',[r.get_destination_page_number(x)+1 for x in r.outline],[1,2,3,4,5])
geometry=[]
with pdfplumber.open(PDF) as pdf:
 for n,(page,chunk) in enumerate(zip(pdf.pages,chunks),1):
  text=page.extract_text(x_tolerance=1,y_tolerance=3)
  check(f'p{n}: texto editável presente no PDF',dict(Counter(words(chunk))-Counter(words(text))),{})
  chars=[c for c in page.chars if c['text'].strip()]
  body=[c for c in chars if 48<c['top']<785]
  check(f'p{n}: conteúdo dentro da página',all(0<=c['x0']<=c['x1']<=page.width and 0<=c['top']<=c['bottom']<=page.height for c in chars),True)
  check(f'p{n}: corpo separado do rodapé',max(c['bottom'] for c in body)<785,True)
  used={c['fontname'] for c in chars}; embedded=[]
  for ref in r.pages[n-1]['/Resources']['/Font'].values():
   font=ref.get_object();d=font.get('/FontDescriptor')
   if d and any(k in d.get_object() for k in ['/FontFile','/FontFile2','/FontFile3']):embedded.append(str(font['/BaseFont']).lstrip('/'))
  check(f'p{n}: fontes usadas incorporadas',sorted(used-set(embedded)),[])
  check(f'p{n}: sem imagem raster',len(page.images),0)
  geometry.append({'pagina':n,'final_corpo':round(max(c['bottom'] for c in body),2),'fontes':sorted(used)})
# Valores públicos do exemplo: uma rolagem contra os dois totais guardados.
check('Rina: total da busca',10+6,16)
check('Rina: quem encontra',[16>=16,16>=19],[True,False])
check('Chance CD16 com +6',str(Fraction(sum(d+6>=16 for d in range(1,21)),20)),'11/20')
check('Chance CD19 com +6',str(Fraction(sum(d+6>=19 for d in range(1,21)),20)),'2/5')
check('Distribuição do exemplo: nenhuma, uma, ambas',[sum(d+6<16 for d in range(1,21)),sum(16<=d+6<19 for d in range(1,21)),sum(d+6>=19 for d in range(1,21))],[9,3,8])
check('Interferência18 e Furtividade16, busca17: não basta',17>=max(18,16),False)
check('Antena não vence CD27 com +4',sum(d+4>=27 for d in range(1,21)),0)
ds=[Fraction(v.replace(',','.')) for v in re.findall(r'(?<![\w,])([0-9]+(?:,[0-9]+)?)\s*m\b',s)]
check('Medidas em múltiplos de1,5m',[str(v) for v in ds if (v/Fraction(3,2)).denominator!=1],[])
# Guardas de integridade: não são certificação de sentido ou equilíbrio.
for label,needle in [('Sem seguimento energético contínuo','não acompanha movimentos futuros, mesmo dentro dos 18 m'),('Interferência não soma CDs','maior entre a CD da interferência e a Furtividade'),('Sem teste energético adicional','Não faça um segundo teste de supressão'),('Reserva zero não apaga natureza','chegar a zero não torna um feiticeiro uma criatura sem energia'),('Sentido Treinado não perde permissão','Não exige primeiro obter outra pista por Percepção'),('Antena preserva achado','preservando as posições já descobertas'),('Não concede grau à distância','**Aferido** conserva sua leitura do grau ao tocar'),('Referência de assinatura','referência confiável')]:
 check('Guarda textual: '+label,needle in s,True)
base=ROOT/'sistema/05-material/livro/planejamento-editorial'
inv=json.loads((base/'INVENTARIO-BASE.json').read_text())
changed=[x['arquivo'] for x in inv['fontes']+inv['artefatos_publicados'] if not (ROOT/x['arquivo']).is_file() or sha(ROOT/x['arquivo'])!=x['sha256']]
check('22 fontes e cinco artefatos publicados preservados',changed,[])
protected=json.loads((L.parent/'lote-03/evidencias/preservacao-base.json').read_text())
changed=[name for name,h in protected.items() if not (ROOT/name).is_file() or sha(ROOT/name)!=h]
check('137 arquivos protegidos preservados',changed,[])
previous=json.loads((L.parent/'MANIFESTO-DA-REVISAO.json').read_text())
changed=[name for name,h in previous['fontes_revisadas'].items() if not (L.parent/name).is_file() or sha(L.parent/name)!=h]
check('Manuscritos dos lotes02-04 preservados',changed,[])
broken=[]
for p in [L/'LEIA-ME.md',L/'05-DECISOES.md',L/'RELATORIO.md']:
 if not p.exists():broken.append(p.name);continue
 for href in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if re.match(r'^[a-z]+:',href) or href.startswith('#'):continue
  target=p.parent/href.split('#')[0]
  if target==L/'CONFERENCIA.json':continue  # Saída desta própria execução, gravada ao final.
  if not target.exists():broken.append([p.name,href])
check('Links de consulta da entrega',broken,[])
check('Original lote05 preservado',sha(L.parent/'lote-05/05-ENERGIA-E-VESTIGIOS.md'),'e492d40892b28830d9a0a31f301bf7d0a96016f88b4bd2a36d2011fbe19c2d26')
check('PDF anterior preservado',sha(L.parent/'lote-05/output/pdf/Projeto-M-Energia-e-Vestigios-Proposta-05.pdf'),'c9858a872981114a3ec791ce826c33584ef26d23183600e8bae1ca9ce7ee64bf')
for label,needle in [('Vestígio não revela ex-portador','não revela seu antigo portador'),('Convenções declaradas','são escolhas desta proposta de jogo'),('Ação não define percepção canônica','A leitura desta ação é **instantânea**')]:
 check('Guarda textual: '+label,needle in s,True)
check('Revisão documental ligada ao manuscrito',sha(SRC) in (L/'evidencias/CENARIOS-R2.md').read_text(),True)
result={'data':'2026-10-03','ok':all(x['ok'] for x in checks),'status':'proposta candidata; não integrada','sha256_texto':sha(SRC),'sha256_pdf':sha(PDF),'checks':checks,'pdf':geometry,'limites':['Guardas e geometria não certificam leitura ou equilíbrio.','Revisão documental pelo autor nesta r2; revisão independente nova e teste humano pendentes.','Inspeção visual é um registro separado, vinculado ao PDF.','Não houve teste humano.','18 m é alcance de ensaio; matemática de d20 não o valida.']}
(L/'CONFERENCIA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':result['ok'],'verificacoes':len(checks),'falhas':[x for x in checks if not x['ok']]},ensure_ascii=False,indent=2))
raise SystemExit(0 if result['ok'] else 1)
