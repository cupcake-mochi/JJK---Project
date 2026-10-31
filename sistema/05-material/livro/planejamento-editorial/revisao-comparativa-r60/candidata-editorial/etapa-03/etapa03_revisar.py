from pathlib import Path
import json,re
import pymupdf as f
from PIL import Image,ImageDraw
H=Path(__file__).resolve().parent;B=H/'composicao';V=H/'revisao';V.mkdir(exist_ok=True)
a=f.open(B/'output/pdf/Ciclo-Maldito-Livro-de-Regras.pdf');b=f.open(B/'output/pdf/Ciclo-Maldito-Livro-de-Regras-Noturno.pdf');m=json.load(open(B/'FONTES-E-VALIDACAO.json'));old=json.load(open(H.parent/'etapa-02/composicao/FONTES-E-VALIDACAO.json'));s=(H/'LIVRO-CANDIDATA.md').read_text();base=(H.parent/'etapa-02/LIVRO-CANDIDATA.md').read_text();summary=(H/'QUADRO-COMANDOS.txt').read_text();intro='O quadro [Comparar os comandos](#campo-link-comparar-comandos) reúne os recursos, os momentos e os prazos dos procedimentos explicados neste capítulo.'
checks=[]
def check(name,x):checks.append({'verificacao':name,'aprovado':bool(x)})
space=lambda t:re.sub(r'\s+',' ',t).strip()
check('Todo o texto anterior permanece, acrescido apenas do quadro e do acesso inicial',space(s.replace(summary,'').replace(intro,''))==space(base))
check('Termos explicados antes do atalho ao quadro',s.index('Sua **atuação básica**',s.index('## 16.'))<s.index(intro))
check('Consulta rápida da etapa 2 preservada integralmente',s[s.index('## 20.'):s.index('## 21.')]==base[base.index('## 20.'):base.index('## 21.')])
fields=['pagina','tipo','bloco','texto','x','y','largura','altura'];body=lambda j:[{k:e[k] for k in fields} for e in j['eventos'] if not e['gerado'] and e['capitulo'] in range(1,16)]
check('Capítulos 1 a 15 preservam texto e posição',body(m)==body(old))
anchor=m['ancoras']['campo-link-comparar-comandos'];tables=[e for e in m['eventos'] if e['tipo']=='table' and e['texto'][0][0]=='Procedimento'];check('Duas tabelas comparativas em largura inteira',len(tables)==2 and all(e['largura']>450 for e in tables))
check('Abertura da referência acompanha a tabela de recursos',anchor['pagina']==tables[0]['pagina'])
check('As nove opções estão no quadro de recursos',all(t in summary for t in ['[Comando comum]','[Rápido]','[Ordem antecipada]','[Especial preparada]','[Melhoria Reação]','[Segura]','[Armado]','[Carregar]','[Atrasar]']))
check('Sumário e marcador digital incluem o quadro',any(x[1]=='Comparar os comandos' and x[2]==anchor['pagina'] for x in a.get_toc()) and any(r['destino']=='campo-link-comparar-comandos' for p in json.load(open(B/'revisao-r45/SUMARIO-PAGINADO.json')) for r in p['entradas']))
seq=[]
for r in json.load(open(B/'NAVEGACAO-CANDIDATA.json')):
 z=m['ancoras'][r['destino']];seq.append((z['pagina'],0 if z['x']<290 else 1,-z['y']))
check('Navegação de Fundamento permanece na ordem de leitura',seq==sorted(seq))
pages=sorted(set([5,m['ancoras']['campo--inv-campo']['pagina']]+[e['pagina'] for e in m['eventos'] if e['bloco']=='campo--inv-armado']+[m['ancoras']['campo--inv-defesa']['pagina']]))
check('Páginas afetadas têm texto igual nas duas paletas',all(a[i-1].get_text()==b[i-1].get_text() for i in pages))
for palette,doc in [('claro',a),('noturno',b)]:
 for num in pages:doc[num-1].get_pixmap(matrix=f.Matrix(1.3,1.3)).save(V/f'{palette}-{num:03d}.png')
 for start in range(0,len(pages),4):
  im=Image.new('RGB',(1600,2200),'#777');draw=ImageDraw.Draw(im)
  for j,num in enumerate(pages[start:start+4]):
   p=Image.open(V/f'{palette}-{num:03d}.png');p.thumbnail((785,1070));x=j%2*800;y=j//2*1100;im.paste(p,(x,y+20));draw.text((x,y),str(num),fill='white')
  im.save(V/f'contato-{palette}-{start//4+1:02d}.jpg')
res={'resultado':'aprovado' if all(x['aprovado'] for x in checks) else 'revisar','paginas':len(a),'pagina_quadro':anchor['pagina'],'paginas_para_revisao':pages,'verificacoes':checks};(V/'VALIDACAO-ETAPA-03.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n');print(json.dumps(res,ensure_ascii=False,indent=2))
