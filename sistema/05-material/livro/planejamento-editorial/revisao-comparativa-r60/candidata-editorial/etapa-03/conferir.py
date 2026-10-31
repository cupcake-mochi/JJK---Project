from pathlib import Path
from collections import Counter
import json,re,hashlib,unicodedata
import pymupdf as fitz
from pypdf import PdfReader
from PIL import Image,ImageDraw
H=Path(__file__).resolve().parent;B=H/'composicao';O=B/'output/pdf';V=H/'revisao';O.mkdir(parents=True,exist_ok=True);V.mkdir(exist_ok=True)
light=O/'Ciclo-Maldito-Livro-de-Regras.pdf';dark=O/'Ciclo-Maldito-Livro-de-Regras-Noturno.pdf'
m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());g=json.loads((B/'GEOMETRIA-CANDIDATA.json').read_text());source=(H/'LIVRO-CANDIDATA.md').read_text()
a=PdfReader(light);b=PdfReader(dark);checks=[]
def check(name,ok):checks.append({'verificacao':name,'aprovado':bool(ok)})
def norm(s):
 s=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',str(s));s=s.replace('−','-').replace('–','-').replace('—','-')
 return ''.join(x.lower() for x in unicodedata.normalize('NFKD',s) if x.isalnum())
check('Contagem das duas paletas corresponde ao manifesto.',len(a.pages)==len(b.pages)==m['paginas'])
# Ordem física dos blocos, além da presença do texto.
positions=m['ancoras'];hits=list(re.finditer(r'^## (\d+)\. .+$',source,re.M));order_errors=[]
for i,match in enumerate(hits):
 segment=source[match.end():hits[i+1].start() if i+1<len(hits) else len(source)]
 keys=re.findall(r'<!-- fonte:[^>]+-->\s*<a id="([^"]+)"></a>',segment)
 seq=[(positions[k]['pagina'],-positions[k]['y'],positions[k]['x']) for k in keys if k in positions]
 # Blocos em uma mesma página podem mudar de coluna; só a ordem entre páginas é comparada aqui.
 if [x[0] for x in seq]!=sorted(x[0] for x in seq):order_errors.append(match[1])
check('Blocos seguem a ordem editorial entre páginas.',not order_errors)
check('Regra Própria antecede o primeiro feitiço.',positions['fundamento-link-criar-regra-propria']['pagina']<positions['fundamento--primeiro']['pagina'])

check('Dificultar a Resistência antecede o catálogo de intervenções.',positions['evocador-link-dificultar']['pagina']<=positions['evocador--ev-intervencoes']['pagina'])
check('Fonte da composição é idêntica à candidata.',(B/'LIVRO-COMPLETO.md').read_text()==source)
texta=[p.extract_text() or '' for p in a.pages];textb=[p.extract_text() or '' for p in b.pages]
check('Texto idêntico em todas as páginas entre paletas.',texta==textb)
alltext=norm(' '.join(texta));manifesttext=norm(' '.join(str(e['texto']) for e in m['eventos']))
missing=[]
for line in source.splitlines():
 l=line.strip()
 if re.fullmatch(r'### (?:Glossário: .+|Índice de assuntos)',l):continue
 if not l or l.startswith(('<!--','<a id=','# Ciclo Maldito','# Parte ','## ')) or l=='Livro de regras' or re.fullmatch(r'[|:\s-]+',l):continue
 values=[c.strip() for c in l.strip('|').split('|')] if l.startswith('|') else [re.sub(r'^[#>•\-]+\s*','',l)]
 for t in values:
  q=norm(t)
  if len(q)>2 and q not in alltext:missing.append({'texto':t[:240],'presente_no_manifesto':q in manifesttext})
check('Todas as linhas e células da candidata localizadas no PDF.',not missing)
check('Sem glifos de substituição ou âncoras brutas.',all('\ufffd' not in x and '\u25a0' not in x and '<a id=' not in x for x in texta))
# Geometria dos blocos reais, sem incluir arte e capas no limite do corpo.
margin=[];overlap=[]
for p in g['paginas']:
 if p['tipo'] in ['cover','art','credits']:continue
 rows=p['blocos']
 for i,x in enumerate(rows):
  if x['x']<g['limites']['esquerda']-.5 or x['x']+x['w']>g['limites']['direita']+.5 or x['y']<g['limites']['base']-.5 or x['y']+x['h']>g['limites']['topo']+.5:margin.append({'pagina':p['pagina'],'texto':x['texto'][:90]})
  for y in rows[i+1:]:
   ix=min(x['x']+x['w'],y['x']+y['w'])-max(x['x'],y['x']);iy=min(x['y']+x['h'],y['y']+y['h'])-max(x['y'],y['y'])
   if ix>.5 and iy>.5:overlap.append({'pagina':p['pagina'],'a':x['texto'][:90],'b':y['texto'][:90]})
check('Sem estouro de margem nos blocos de texto.',not margin)
check('Sem sobreposição entre blocos de texto.',not overlap)
refs={p.indirect_reference.idnum for p in a.pages};bad=[];links=Counter()
for n,p in enumerate(a.pages,1):
 for ref in p.get('/Annots',[]):
  ann=ref.get_object()
  if ann.get('/Subtype')!='/Link':continue
  ac=ann.get('/A')
  if ac and ac.get('/S')=='/URI':links['externos']+=1;continue
  z=ann.get('/Dest') or (ac.get('/D') if ac else None);z=z.get_object() if hasattr(z,'get_object') else z
  if not isinstance(z,list) or z[0].idnum not in refs:bad.append(n)
  links['internos']+=1
check('Todos os links internos chegam a páginas existentes.',not bad)
da=fitz.open(light);db=fitz.open(dark);diff=[]
for n,(pa,pb) in enumerate(zip(da,db),1):
 wa=pa.get_text('words');wb=pb.get_text('words')
 if len(wa)!=len(wb) or any(x[4]!=y[4] or max(abs(i-j) for i,j in zip(x[:4],y[:4]))>.01 for x,y in zip(wa,wb)):diff.append(n)
check('Texto ocupa as mesmas posições nas duas paletas.',not diff)
# Páginas para atenção na revisão visual: altura final em cada coluna.
occ=[]
for p in g['paginas']:
 if p['tipo']=='cover' or not p['blocos']:continue
 left=[x['y'] for x in p['blocos'] if x['x']<150 and x['w']<300];right=[x['y'] for x in p['blocos'] if x['x']>250 and x['w']<300]
 if left and right:
  cap=g['limites']['topo']-g['limites']['base'];lh=(g['limites']['topo']-min(left))/cap;rh=(g['limites']['topo']-min(right))/cap
  if max(lh,rh)-min(lh,rh)>.25 or max(lh,rh)<.67:occ.append({'pagina':p['pagina'],'ocupacao_esquerda':round(lh,2),'ocupacao_direita':round(rh,2),'tipo':p['tipo']})
# Conferir a reordenação e a continuação da tabela semanal na composição final.
check('Patentes antecedem as recompensas da guilda.',positions['progressao--prog-patentes']['pagina']<positions['progressao--prog-guilda']['pagina'])
weekly_page=positions['progressao--prog-semana']['pagina']
weekly_geometry=next(p for p in g['paginas'] if p['pagina']==weekly_page)
weekly_tables=[x for x in weekly_geometry['blocos'] if x['texto'].startswith("[['Missão na semana'")]
check('Tabela semanal continua nas duas colunas com cabeçalho repetido.',len(weekly_tables)==2 and min(x['x'] for x in weekly_tables)<150 and max(x['x'] for x in weekly_tables)>250)
# Regras comuns das defesas permanecem antes das entradas específicas.
check('Ativação compartilhada antecede as quatro defesas de domínio.',all(positions['aptidoes--apt-protecao-dominios']['pagina']<=positions[k]['pagina'] for k in ['aptidoes--apt-cesta','aptidoes--apt-simples','aptidoes--apt-petala','aptidoes--apt-extensao']))
apt_source=source[source.index('## 12.'):source.index('## 13.')]
check('Catálogo contextualiza Kokusen antes da tabela.',apt_source.index('**Kokusen** é um reforço')<apt_source.index('| Aptidão | Requisito | Categoria de Efeito |'))
check('Aquisição da Aptidão Própria antecede sua escrita.',apt_source.index('Aptidão Própria usa uma escolha')<apt_source.index('Escreva uma frase de regra.'))
routes_source=source[source.index('## 13.'):source.index('## 14.')]
check('Definição das rotas e montagem comum antecedem os exemplos.',routes_source.index('#### Como montar Manejos e Katas')<routes_source.index('### Exemplo: Fisga'))
check('Lapidação e requisitos de Bênçãos antecedem as entradas.',routes_source.index('### Lapidação')<routes_source.index('### Bênçãos')<routes_source.index('#### Defesa sem Armadura'))
check('Tabela de escolhas de Bênçãos tem quatorze links.',len(__import__('re').findall(r'\| \[.+?\]\(#rotas--.+?\) \|',routes_source))==14)
powers_source=source[source.index('## 14.'):source.index('## 15.')]
powers_dispute=powers_source[powers_source.index('### Disputa de domínios'):powers_source.index('### Manter uma disputa')]
check('Exceção da Incompleta antecede a tabela de disputa.',powers_dispute.index('Uma Expansão Incompleta segue a exceção')<powers_dispute.index('| Ordem | Comparação | Resultado |'))
check('Alerta sobre três barreiras antecede a tabela de disputa.',powers_dispute.index('Com três ou mais barreiras fechadas sobrepostas')<powers_dispute.index('| Ordem | Comparação | Resultado |'))
check('Rescaldo apresentado antes da montagem do domínio.',powers_source.index('Quando a Expansão termina, sua Técnica Inata entra em')<powers_source.index('### Criar um domínio'))
ritual_source=source[source.index('## 15.'):source.index('## 16.')]
check('Exceções das modalidades antecedem o teste de Ritual.',ritual_source.index('Uma Técnica Máxima admite apenas Ritual completo.')<ritual_source.index('#### Teste de Ritual'))
check('Catálogo do Ritual identifica as duas tabelas como dezesseis entradas.', 'As dezesseis Melhorias de Ritual estão distribuídas nas duas tabelas seguintes.' in ritual_source)
check('Vagas de pacto contextualizadas antes de Preço real.',ritual_source.index('Só os pactos permanentes e os pactos de restrição contam')<ritual_source.index('#### Preço real'))
check('Promessas e temporários continuam fora do limite de vagas.','Promessas e pactos temporários não entram nesse limite.' in ritual_source and 'Cada pacto permanente ou pacto de restrição ocupa uma vaga' in ritual_source)
field_source=source[source.index('## 16.'):source.index('## 17.')]
check('Coletiva e gasto da básica contextualizados na abertura.',field_source.index('**Reação coletiva**, chamada de **coletiva**')<field_source.index('### Turnos das entidades') and field_source.index('**gastar a básica** significa gastar esse recurso')<field_source.index('### Turnos das entidades'))
check('Preparar e gatilhos antecedem Ordens pendentes.',field_source.index('#### Preparar uma ação')<field_source.index('#### Gatilhos e ajustes')<field_source.index('#### Ordens pendentes'))
check('Ordem física segue antecipada, preparar, gatilhos e pendentes.',all(positions[a]['pagina']<=positions[b]['pagina'] for a,b in zip(['campo--inv-antecipada','campo--inv-preparar','campo--inv-gatilhos'],['campo--inv-preparar','campo--inv-gatilhos','campo--inv-pendentes'])))
check('Exceção dos corpos antecede a posição de entrada.',field_source.index('Corpos amaldiçoados permanecem no mundo')<field_source.index('Na entrada sem substituição'))
build_source=source[source.index('## 17.'):source.index('## 18.')]
check('Capacidade e atuação básicas distinguidas antes do roteiro.',build_source.index('A **capacidade básica** é uma habilidade de Classe 0')<build_source.index('#### Etapas da ficha'))
check('Classe real contextualizada antes de Família Livre.',build_source.index('A **Classe real** é a Classe em que a especial será usada')<build_source.index('##### Família Livre'))
check('Cão de sombra preservado antes das aquisições seguintes.',positions['construcao--entidade-cao']['pagina']<positions['construcao--entidades-lista-criacao']['pagina'])
check('Vantagem da tentativa seguinte antecede a limitação de fontes.',build_source.index('A tentativa seguinte a uma falha recebe vantagem pela própria regra.')<build_source.index('Além dessa vantagem, esses testes só podem receber vantagem'))
list_intro=positions['construcao--entidades-lista-criacao'];list_first=positions['construcao--entidades-lista-criacao-sub-1']
check('Lista de ritual e criação acompanha o começo da primeira opção.',list_intro['pagina']==list_first['pagina'] and abs(list_intro['x']-list_first['x'])<1)
fp=positions['fabricacao--fab-entidades']['pagina'];fg=next(x for x in g['paginas'] if x['pagina']==fp);fc=[]
for side in [0,1]:
 rr=[x for x in fg['blocos'] if x['w']<300 and (x['x']<150 if side==0 else x['x']>250)]
 fc.append((g['limites']['topo']-min(x['y'] for x in rr))/(g['limites']['topo']-g['limites']['base']))
check('Colunas equilibradas na abertura de Criação de entidades.',abs(fc[0]-fc[1])<=.20)
gm_source=source[source.index('## 18.'):source.index('## 19.')]
check('Preparação da missão antecede a condução da sessão.',gm_source.index('### Preparar uma missão')<gm_source.index('### Mestrar uma sessão'))
check('Ferramentas de consulta apresentadas antes da busca de regra.',gm_source.index('A [Consulta rápida]')<gm_source.index('Procure a capacidade usada e o procedimento geral que ela modifica.'))
check('Recursos no começo da missão explicitados.', 'os recursos disponíveis no começo da missão' in gm_source and 'Trocar de mesa não renova recursos por si.' in gm_source)
gloss_source=source[source.index('## 19.'):source.index('## 20.')]
gloss_entries=re.findall(r'^\[([^\]]+)\]\(#([^\)]+)\)\. (.+)$',gloss_source,re.M)
gloss_map={x[0]:x[1:] for x in gloss_entries}
check('Glossário contém 104 entradas sem duplicatas.',len(gloss_entries)==len(gloss_map)==104)
gloss_alpha=lambda z: ''.join(x for x in unicodedata.normalize('NFKD',z.casefold()) if not unicodedata.combining(x))
check('Glossário em ordem alfabética.',[gloss_alpha(x[0]) for x in gloss_entries]==sorted(gloss_alpha(x[0]) for x in gloss_entries))
check('Remissões de Talento, Expressão e Categoria levam à explicação.',all(gloss_map[x][0]=='fundamento-link-capacidades' for x in ['Talento','Expressão da técnica','Categoria de Efeito']))
check('Glossário preserva momento de Bloquear e recuperação das Sequelas.','antes da rolagem do atacante' in gloss_map['Bloquear'][1] and 'depois de resolver a recuperação' in gloss_map['Sequela'][1])
quick_source=source[source.index('## 20.'):source.index('## 21.')]
check('Resumo de ataque exige escolha da defesa antes da comparação.',quick_source.index('Antes da rolagem de acerto, o alvo escolhe')<quick_source.index('Compare o ataque com a defesa escolhida.'))
check('Ataque separa escolha anterior e resultado de Bloquear.','2. **Antes da rolagem de acerto**' in quick_source and 'conforme a escolha anterior.' in quick_source)
check('Socorro antecede registro de duração.',quick_source.index('#### Dano e socorro')<quick_source.index('### Registro de duração'))
check('Resumo de socorro define tratamento e conserva a exceção de inconsciência.','Personagem jogador a zero de vida' in quick_source and 'a quantidade de cura válida exigida naquela queda' in quick_source and 'Insistir não remove outra causa de inconsciência.' in quick_source)
index_source=source[source.index('## 21.'):]
index_entries=re.findall(r'^\[([^\]]+)\]\(#([^\)]+)\)$',index_source,re.M)
index_key=lambda x:unicodedata.normalize('NFKD',x[0].casefold()).encode('ascii','ignore').decode()
check('Índice contém 452 nomes únicos em ordem alfabética.',len(index_entries)==len(dict(index_entries))==452 and index_entries==sorted(index_entries,key=index_key))
index_events=[e for e in m['eventos'] if e['tipo']=='indexentry']
check('Todas as entradas do Índice foram compostas na mesma ordem.',[e['texto'] for e in index_events]==[f'[{n}](#{t})' for n,t in index_entries])
index_bad=[]
# Rótulo e número da página precisam abrir o mesmo destino prometido no texto.
for e,(name,target) in zip(index_events,index_entries):
 expected=positions[target]['pagina'];x=e['x'];y=e['y'];w=e['largura'];h=e['altura'];pn=e['pagina'];pa=a.pages[pn-1];matches=[]
 for ref in pa.get('/Annots',[]):
  ann=ref.get_object();rect=ann.get('/Rect')
  if ann.get('/Subtype')!='/Link' or not rect:continue
  cx=(float(rect[0])+float(rect[2]))/2;cy=(float(rect[1])+float(rect[3]))/2
  if x-.6<=cx<=x+w+.6 and y-.6<=cy<=y+h+.6:
   dest=ann.get('/Dest');dest=dest.get_object() if hasattr(dest,'get_object') else dest
   matches.append(bool(dest and dest[0].idnum==a.pages[expected-1].indirect_reference.idnum))
 screen=fitz.Rect(x+w-27,da[pn-1].rect.height-y-h-.2,x+w+.2,da[pn-1].rect.height-y+.2)
 printed=da[pn-1].get_textbox(screen).strip()
 if len(matches)<2 or not all(matches) or printed!=str(expected):index_bad.append({'termo':name,'esperado':expected,'numero_impresso':printed,'links':matches})
check('Números impressos e links dos 452 verbetes apontam ao destino correto.',not index_bad)
index_aliases=json.loads((H/'DESTINOS-INDICE-REVISAO.json').read_text());alias_bad=[]
for cfg in index_aliases:
 pp=positions.get(cfg['alias']);events=[e for e in m['eventos'] if e['bloco']==cfg['bloco'] and e['texto']==cfg['titulo']]
 if not pp or not events or not any(pp['pagina']==e['pagina'] and abs(pp['x']-e['x'])<.1 and abs(pp['y']-(e['y']+e['altura']))<1 for e in events):alias_bad.append(cfg['termo'])
check('Novos destinos precisos chegam ao próprio subtítulo.',not alias_bad)
(V/'AUDITORIA-PAGINAS-INDICE.json').write_text(json.dumps({'entradas':len(index_entries),'links_e_numeros_incorretos':index_bad,'aliases_sem_subtitulo':alias_bad},ensure_ascii=False,indent=2)+'\n')
report={'resultado':'aprovado' if all(x['aprovado'] for x in checks) else 'requer revisão','paginas':len(a.pages),'verificacoes':checks,'conteudo_ausente':missing,'margens':margin,'sobreposicoes':overlap,'links':dict(links),'links_invalidos':bad,'diferencas_geometria':diff,'paginas_para_atencao_visual':occ}
(V/'VALIDACAO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');(V/'TEXTO-EXTRAIDO.txt').write_text('\n\n'.join(f'PÁGINA {i+1}\n{x}' for i,x in enumerate(texta)))
print(json.dumps({k:report[k] for k in ['resultado','paginas','conteudo_ausente','margens','sobreposicoes','links','diferencas_geometria','paginas_para_atencao_visual']},ensure_ascii=False))
if '--render' in __import__('sys').argv:
 for palette,doc in [('claro',da),('noturno',db)]:
  folder=V/'visual'/palette;folder.mkdir(parents=True,exist_ok=True)
  for n,page in enumerate(doc,1):
   if n%80==0:print(palette,n,'páginas renderizadas',flush=True)
   path=folder/f'pagina-{n:03d}.png';page.get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False).save(path)
  for start in range(0,len(doc),8):
   sheet=Image.new('RGB',(1800,1320),'#777777');draw=ImageDraw.Draw(sheet)
   for j in range(min(8,len(doc)-start)):
    im=Image.open(folder/f'pagina-{start+j+1:03d}.png');im.thumbnail((440,625));x=(j%4)*450+(450-im.width)//2;y=(j//4)*660+24;sheet.paste(im,(x,y));draw.text((x,y-20),f'{palette} / {start+j+1}',fill='white')
   sheet.save(folder/f'contato-{start//8+1:03d}.jpg',quality=90)
 print('Todas as páginas renderizadas nas duas paletas.')
