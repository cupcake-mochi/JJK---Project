"""Reexportar somente desenhos afetados pelo elenco; conservar posições e medidas."""
from pathlib import Path
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import ast,re,json,hashlib,subprocess,shutil

A=Path(__file__).resolve().parent;R=A.parents[1];E=R/'07 - Edicao de Leitura/edicao-integrada-136'
OUT=E/'assets/mapas';OUT.mkdir(parents=True,exist_ok=True);(A/'tmp/pdfs').mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for file,name in [('apoio-revisao-textual-121/imagens/passarela.svg','passarela'),('apoio-revisao-textual-121/imagens/portao.svg','portao'),('apoio-revisao-textual-122/imagens/ensaio.svg','sineiro'),('apoio-revisao-textual-123/imagens/po.svg','po')]:
 source=R/'04 - Planejamento'/file;dest=OUT/(name+'.svg');shutil.copyfile(source,dest)
 rows.append({'mapa':name,'origem':source.relative_to(R).as_posix(),'arquivo':dest.relative_to(R).as_posix(),'sha256':sha(dest),'alteracao':'Nenhuma; mesmo cenário e mesmos nomes.'})

class Names(ast.NodeTransformer):
 def __init__(self,archive=False):self.archive=archive;self.changes=[]
 def visit_Constant(self,node):
  if not isinstance(node.value,str):return node
  old=node.value;new=old
  for before,after in [('Ren','Toru'),('Sora','Sayo'),('REN','TORU'),('SORA','SAYO'),('Haru','Daigo')]:new=re.sub(r'\b'+before+r'\b',after,new)
  if self.archive and new=='H':new='D'
  if old!=new:self.changes.append({'antes':old,'depois':new});node.value=new
  return node

for record,ident,name in [(122,'s076','dupla'),(123,'s102','arquivo')]:
 source=R/f'04 - Planejamento/apoio-revisao-textual-{record}/GERAR-MAPAS.py'
 tree=ast.parse(source.read_text());body=[]
 for node in tree.body:
  if isinstance(node,ast.Expr) and isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Attribute) and node.value.func.attr=='mkdir':break
  body.append(node)
 tree.body=body;transform=Names(record==123);tree=ast.fix_missing_locations(transform.visit(tree))
 ns={'__file__':str(A/f'mapas-{record}.py')};exec(compile(tree,str(source),'exec'),ns)
 obj=ns['Mapa'](ident,488);pdf=A/f'tmp/pdfs/{name}.pdf';c=Canvas(str(pdf),pagesize=(488,obj.height),invariant=1);obj.drawOn(c,0,0);c.showPage();c.save()
 dest=OUT/(name+'.svg');subprocess.run(['pdftocairo','-svg',str(pdf),str(dest)],check=True)
 subprocess.run(['pdftoppm','-png','-scale-to','1200','-singlefile',str(pdf),str(A/f'tmp/{name}')],check=True)
 rows.append({'mapa':name,'origem':source.relative_to(R).as_posix(),'origem_sha256':sha(source),'arquivo':dest.relative_to(R).as_posix(),'sha256':sha(dest),'alteracoes_de_rotulo':transform.changes,'limite':'Somente constantes de texto foram substituídas; coordenadas, medidas, símbolos de parede, peças e posições mantidos.'})

# O mapa de duas rotas usa a geometria corrigida do livro preservado.
fonts=R/'08 - Diagramacao do Guia/fontes'
for name,file in [('Body','Spectral-Regular.ttf'),('Bold','Spectral-SemiBold.ttf'),('Italic','Spectral-Italic.ttf'),('Head','BarlowCondensed-SemiBold.ttf')]:pdfmetrics.registerFont(TTFont(name,str(fonts/file)))
ns={};source=R/'08 - Diagramacao do Guia/MAPAS.py';exec(compile(source.read_text(),str(source),'exec'),ns)
obj=ns['Mapa']('s062',488);pdf=A/'tmp/pdfs/carregador.pdf';c=Canvas(str(pdf),pagesize=(488,obj.height),invariant=1);obj.drawOn(c,0,0);c.showPage();c.save()
dest=OUT/'carregador.svg';subprocess.run(['pdftocairo','-svg',str(pdf),str(dest)],check=True)
subprocess.run(['pdftoppm','-png','-scale-to','1200','-singlefile',str(pdf),str(A/'tmp/carregador')],check=True)
rows.append({'mapa':'carregador','origem':source.relative_to(R).as_posix(),'origem_sha256':sha(source),'arquivo':dest.relative_to(R).as_posix(),'sha256':sha(dest),'alteracao':'Exportação vetorial do desenho corrigido, sem alteração de medidas.'})
(A/'mapas-reunidos.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('Sete mapas de casos reunidos; dois rótulos de elenco atualizados, sem mexer na geometria.')
