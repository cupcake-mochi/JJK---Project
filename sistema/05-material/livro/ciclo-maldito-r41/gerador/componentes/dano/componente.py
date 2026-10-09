from pathlib import Path
from dataclasses import dataclass
from xml.sax.saxutils import escape
import re,json,hashlib,math
from reportlab import rl_config
rl_config.invariant=1
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph,Table,TableStyle,Flowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor,white
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

B=Path(__file__).resolve().parent; P=B.parents[1]
OUT=B/'output/pdf'; OUT.mkdir(parents=True,exist_ok=True)
PDF=OUT/'Projeto-M-Dano-e-Recuperacao-Piloto-B-R18.pdf'
F=B.parents[1]/'fontes-tipograficas'
for name,file in [('Body','Spectral-Regular.ttf'),('Bold','Spectral-SemiBold.ttf'),('Italic','Spectral-Italic.ttf'),('Head','BarlowCondensed-SemiBold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(F/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Italic',boldItalic='Bold')
W,H=A4;M=19*mm;AW=W-2*M;G=7*mm;CW=(AW-G)/2;TOP=H-23*mm;BOTTOM=36*mm
INK,ACC,PALE,RULE,MUTED,EDGE=map(HexColor,['#251727','#BC2A6E','#FDF0F6','#ECC3D6','#65545F','#927583'])
S={
'body':ParagraphStyle('body',fontName='Body',fontSize=10.75,leading=15,textColor=INK,spaceAfter=4,allowWidows=0,allowOrphans=0),
'h1':ParagraphStyle('h1',fontName='Head',fontSize=21,leading=24,textColor=INK,spaceBefore=8,spaceAfter=6),
'h2':ParagraphStyle('h2',fontName='Head',fontSize=17,leading=20,textColor=INK,spaceBefore=5,spaceAfter=5),
'h3':ParagraphStyle('h3',fontName='Head',fontSize=14,leading=17,textColor=INK,spaceBefore=4,spaceAfter=4),
'major':ParagraphStyle('major',fontName='Head',fontSize=32,leading=36,textColor=INK,spaceAfter=12),
'note':ParagraphStyle('note',fontName='Body',fontSize=10.25,leading=14,textColor=INK),
'cell':ParagraphStyle('cell',fontName='Body',fontSize=9.75,leading=12.5,textColor=INK),
'headcell':ParagraphStyle('headcell',fontName='Head',fontSize=10.5,leading=12.5,textColor=white),
'small':ParagraphStyle('small',fontName='Body',fontSize=9,leading=12,textColor=MUTED,spaceAfter=6),
'index':ParagraphStyle('index',fontName='Body',fontSize=10.25,leading=14,textColor=INK,spaceAfter=4),
}
texts={'dano':(B/'fontes-capturadas/DANO-E-RECUPERACAO.md').read_text()}
texts.update(globals().get('_texto_editorial_revisado',{}))
from identidade import nome_oficial
texts={k:nome_oficial(v) for k,v in texts.items()}
blocks=[]
for m in re.finditer(r'<!-- page:([^|]+)\|([^>]+)-->\s*(.*?)(?=<!-- page:|\Z)',texts['dano'],re.S):
    anchor,title,md=[v.strip() for v in m.groups()]
    blocks.append({'doc':'dano','anchor':anchor,'title':title,'md':md,'key':'dano--'+anchor})
assert len(blocks)==20
keys={b['key'] for b in blocks}
starts=['dano','condicoes','cura','zero','descansos']
groups=['Dano','Condições','Cura','Socorro','Descansos']
nav=[('Consulta','consulta')]+[(g,'dano--'+a) for g,a in zip(groups,starts)]
current=0
for b in blocks:
    if b['anchor'] in starts:current=starts.index(b['anchor'])
    b['group']=groups[current];b['group_start']=b['anchor'] in starts
PAGES={};POSITIONS={};EVENTS=[];DRAW=[];PAGE=1;Y=TOP;GROUP='Consulta';INFORMATION=[]
def inline(s,doc='geral'):
    links=[]
    def link(m):
        label,target=m.groups();dest=doc+'--'+target.lstrip('#')
        if target.startswith('#') and dest in keys:
            links.append('<link href="#'+dest+'" color="#BC2A6E">'+escape(label)+'</link>')
        else:links.append(escape(label))
        return f'ZZPROTECTEDLINK{len(links)-1}ZZ'
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,s)
    s=s.replace('–','-').replace('—','-');s=escape(s)
    s=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'`([^`]+)`',r'<b>\1</b>',s)
    s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
    for i,v in enumerate(links):s=s.replace(f'ZZPROTECTEDLINK{i}ZZ',v)
    return s

class Schematic(Flowable):
    def __init__(self,name,w):
        super().__init__();self.name=name;self.width=w;self.height=105
    def wrap(self,w,h):return self.width,self.height
    def draw(self):
        c=self.canv;w=self.width;c.saveState()
        c.setFillColor(PALE);c.setStrokeColor(EDGE);c.setLineWidth(.65)
        c.roundRect(0,0,w,105,5,stroke=1,fill=1)
        c.setFont('Head',14);c.setFillColor(INK);c.drawString(12,84,'Janela sem Sequelas e sem dano posterior')
        points=[35+(w-70)*i/3 for i in range(4)]
        c.setStrokeColor(ACC);c.setLineWidth(1);c.line(points[0],54,points[-1],54)
        for i,x in enumerate(points):
            c.setFillColor(white);c.circle(x,54,11,fill=1,stroke=1)
            c.setFont('Head',13);c.setFillColor(INK);c.drawCentredString(x,50,str(3-i))
            c.setFont('Body',9);c.drawCentredString(x,29,['Queda','1ª volta','2ª volta','3ª volta'][i])
        c.setFont('Body',9);c.setFillColor(MUTED)
        c.drawString(12,12,'Número: rodadas restantes. Cada volta termina no ponto da queda na iniciativa.')
        c.restoreState()

@dataclass
class Part:
    kind:str
    text:object
    key:str=None
    doc:str='geral'
    block:str=None
    def make(self,w):
        if self.kind=='esquema':return Schematic(self.text,w),8,10
        if self.kind=='table':
            rows=self.text;n=len(rows[0]);fr=[1/n]*n
            if n==2:
                mean=[sum(len(row[j]) for row in rows[1:])/max(1,len(rows)-1) for j in range(n)]
                first=max(.18,min(.48,mean[0]/max(1,sum(mean))))
                fr=[first,1-first]
            elif n==3:
                fr=[.24,.38,.38]
                if rows[0][0]=='Integridade perdida':fr=[.23,.09,.68]
                elif rows[0][0]=='Momento':fr=[.44,.28,.28]
                elif rows[0][0]=='Degrau':fr=[.13,.63,.24]
            elif n==4:fr=[.22,.26,.26,.26]
            rendered=[[Paragraph(inline(v,self.doc),S['headcell' if i==0 else 'cell']) for v in row] for i,row in enumerate(rows)]
            t=Table(rendered,colWidths=[w*f for f in fr],repeatRows=1,hAlign='LEFT')
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),ACC),('ROWBACKGROUNDS',(0,1),(-1,-1),[white,PALE]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('BOX',(0,0),(-1,-1),.65,EDGE),('INNERGRID',(0,0),(-1,-1),.25,EDGE)]))
            return t,8,10
        if self.kind=='note':
            t=Table([[Paragraph(inline(self.text,self.doc),S['note'])]],colWidths=[w])
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('BOX',(0,0),(-1,-1),.65,EDGE),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
            return t,4,8
        st=S[self.kind]
        return Paragraph(inline(self.text,self.doc),st),st.spaceBefore,st.spaceAfter

@dataclass
class Unit:
    parts:list
    wide:bool=False
    connected:bool=False
    def measure(self,w):
        result=[];h=0
        for p in self.parts:
            f,b,a=p.make(w);fh=f.wrap(w,H)[1]
            result.append((p,f,b,fh,a));h+=b+fh+a
        return h,result


def parse(b):
    out=[];lines=b['md'].splitlines();i=0;heading_no=0
    while i<len(lines):
        l=lines[i].strip();i+=1
        if not l:continue
        if l.startswith('|'):
            table_lines=[l]
            while i<len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i].strip());i+=1
            rows=[[v.strip() for v in row.strip('|').split('|')] for row in table_lines if not re.fullmatch(r'[\s|:\-]+',row)]
            assert len(set(len(row) for row in rows))==1,(b['key'],rows)
            p=Part('table',rows,doc=b['doc'],block=b['key'])
        elif l.startswith('#'):
            level=len(l)-len(l.lstrip('#'));kind='h'+str(min(level,3))
            key=b['key'] if level==1 else b['key']+'-sub-'+str(heading_no)
            heading_no+=1;p=Part(kind,l[level:].strip(),key=key,doc=b['doc'],block=b['key'])
        else:
            kind='body'
            if l.startswith('> '):kind='note';l=l[2:]
            if l.startswith('- '):l='• '+l[2:]
            p=Part(kind,l,doc=b['doc'],block=b['key'])
        out.append(p)
        if b['anchor']=='defesa' and p.kind=='note' and 'Sousuke tem Defesa 15' in str(p.text):
            out.append(Part('esquema','cobertura',doc=b['doc'],block=b['key']))
    if b['anchor']=='movimento':out.append(Part('esquema','movimento',doc=b['doc'],block=b['key']))
    units=[];i=0
    while i<len(out):
        group=[out[i]];i+=1
        if group[0].kind.startswith('h'):
            while i<len(out) and out[i].kind.startswith('h'):
                group.append(out[i]);i+=1
            if i<len(out):group.append(out[i]);i+=1
        units.append(Unit(group,any(p.kind in ['table','esquema'] for p in group)))
    # Keep each illustrative example with its preceding explanation, and
    # include a short closing qualifier instead of leaving it on its own.
    connected=[]
    for unit in units:
        first=unit.parts[0]
        is_example=first.kind in ['note','body'] and bool(re.match(r'^\*{0,2}Exemplo\b',str(first.text),re.I))
        same_source=connected and connected[-1].parts[-1].block==first.block
        if is_example and same_source and (not connected[-1].wide or any(p.kind=='table' for p in connected[-1].parts)):
            previous=connected.pop()
            connected.append(Unit(previous.parts+unit.parts,wide=previous.wide,connected=True))
        elif connected and connected[-1].connected and first.kind=='body' and len(str(first.text))<100 and same_source:
            connected[-1].parts.extend(unit.parts)
        else:connected.append(unit)
    return connected


# One width per complete source subsection; tables and diagrams require AW.
# Page planning considers the whole chapter, to avoid tiny continuation pages.
atoms=[]
for block in blocks:
    units=parse(block)
    if block['group_start']:units[0].parts[0].kind='major'
    sections=[];current=[]
    for u in units:
        if current and any(p.kind in ['h2','h3'] for p in u.parts):
            sections.append(current);current=[]
        current.append(u)
    if current:sections.append(current)
    if (len(sections)>1 and not any(u.wide for u in sections[0])
        and not any(p.kind in ['h2','h3'] for u in sections[0] for p in u.parts)
        and Unit([p for u in sections[0]+sections[1] for p in u.parts]).measure(AW)[0]<=TOP-BOTTOM):
        sections[:2]=[sections[0]+sections[1]]
    for i,section in enumerate(sections,1):
        ps=[p for u in section for p in u.parts]
        if block['anchor']=='zero' and any(p.kind=='h2' and p.text=='Janela de socorro' for p in ps):
            ps.append(Part('esquema','janela',doc='dano',block=block['key']))
        u=Unit(ps,connected=True)
        atoms.append({'key':block['key']+'--informacao-'+str(i),'group':block['group'],'unit':u,
            'wide':any(p.kind in ['table','esquema','major'] for p in ps),
            'aw':u.measure(AW)[0],'cw':u.measure(CW)[0]})
assert all(a['aw']<=TOP-BOTTOM for a in atoms)
N=len(atoms);CAP=TOP-BOTTOM

def band_options(i):
    yield {'i':i,'j':i+1,'cut':None,'height':atoms[i]['aw']}
    if atoms[i]['wide']:return
    for j in range(i+2,min(N,i+8)+1):
        run=atoms[i:j]
        if any(a['wide'] for a in run) or len({a['group'] for a in run})!=1:break
        for cut in range(i+1,j):
            left=sum(a['cw'] for a in atoms[i:cut])+4*(cut-i-1)
            right=sum(a['cw'] for a in atoms[cut:j])+4*(j-cut-1)
            height=max(left,right)
            full=sum(a['aw'] for a in run)+4*(len(run)-1)
            if height<=CAP and height<=full and abs(left-right)<=max(30,height*.25):
                yield {'i':i,'j':j,'cut':cut,'height':height}
options=[list(band_options(i)) for i in range(N)]

def prune(states):
    distinct={}
    for h,bands in states:
        k=round(h,2)
        if k not in distinct or sum(b['cut'] is not None for b in bands)<sum(b['cut'] is not None for b in distinct[k][1]):
            distinct[k]=(h,bands)
    v=list(distinct.values())
    if len(v)<=24:return v
    chosen=sorted(v,key=lambda x:x[0])[:10]+sorted(v,key=lambda x:-x[0])[:10]
    chosen+=sorted(v,key=lambda x:(sum(b['cut'] is not None for b in x[1]),-x[0]))[:4]
    return list({round(h,2):(h,b) for h,b in chosen}.values())

def page_options(start):
    states={start:[(0,[])]};final=[]
    for i in range(start,N):
        if i not in states:continue
        states[i]=prune(states[i])
        for height,bands in states[i]:
            for band in options[i]:
                h=height+(4 if bands else 0)+band['height']
                if h<=CAP:
                    states.setdefault(band['j'],[]).append((h,bands+[band]))
        if i>start:
            final.extend((i,h,bands) for h,bands in states[i])
    if N in states:final.extend((N,h,bands) for h,bands in prune(states[N]))
    return final

best={N:((0,0,0),[])}
for i in range(N-1,-1,-1):
    choices=[]
    for end,height,bands in page_options(i):
        if end not in best:continue
        score,rest=best[end]
        # Page count first, then page density and the readability of balanced
        # columns for prose. The column preference never adds a page.
        # No font reduction or breaking a subsection is a candidate.
        narrow=sum(b['j']-b['i'] for b in bands if b['cut'] is not None)
        cost=(score[0]+1,score[1]+(CAP-height)**2-30000*narrow,
              score[2]+sum(b['cut'] is not None for b in bands))
        choices.append((cost,[{'height':height,'bands':bands}]+rest))
    assert choices,('Unplaceable source subsection',atoms[i]['key'])
    best[i]=min(choices,key=lambda x:x[0])
PLAN=best[0][1]

def put(unit,x,y,w,mode,group,band):
    height,measured=unit.measure(w);yy=y;uid=len(EVENTS)
    assert yy-height>=BOTTOM-.01,(PAGE,'overflow',yy-height)
    for p,f,b,h,a in measured:
        yy-=b;DRAW.append((PAGE,group,p,f,x,yy-h,w,h,mode))
        if p.key:
            assert p.key not in POSITIONS,p.key
            POSITIONS[p.key]=(PAGE,x,yy)
        EVENTS.append({'pagina':PAGE,'grupo':group,'bloco':p.block,'tipo':p.kind,'x':round(x,2),
            'topo':round(yy,2),'largura':round(w,2),'altura':round(h,2),'modo':mode,'faixa':band,
            'unidade':uid,'exemplo_ligado':unit.connected,'sha256_texto':hashlib.sha256(str(p.text).encode()).hexdigest()})
        yy-=h+a
    return height

def draw_atom(i,x,y,w,mode,band):
    a=atoms[i];start=len(EVENTS);height=put(a['unit'],x,y,w,mode,a['group'],band)
    INFORMATION.append({'chave':a['key'],'pagina':PAGE,'eventos':list(range(start,len(EVENTS))),
        'largura_estavel':round(w,2),'blocos':list(dict.fromkeys(p.block for p in a['unit'].parts))})
    return height

def build_plan(pagemap):
    global PAGE,Y,DRAW,EVENTS,POSITIONS,INFORMATION
    PAGE=1;Y=TOP;DRAW=[];EVENTS=[];POSITIONS={'consulta':(1,M,TOP)};INFORMATION=[]
    u=Unit([Part('major','Dano e recuperação'),Part('small','Piloto de diagramação • capítulo completo'),Part('h2','Consulta')])
    Y-=put(u,M,Y,AW,'uma-coluna','Consulta',len(EVENTS))
    toc=[]
    for group in groups:
        members=[b for b in blocks if b['group']==group]
        for i,b in enumerate(members):
            label=f'<link href="#{b["key"]}" color="#251727">{escape(b["title"])} <font color="#65545F">{pagemap.get(b["key"],"-")}</font></link>'
            p=Part('index',label,block='indice',doc='dano')
            p.make=lambda w,p=p:(Paragraph(p.text,S['index']),0,4)
            toc.append(Unit(([Part('h2',group,block='indice')] if i==0 else [])+[p]))
    heights=[u.measure(CW)[0] for u in toc]
    cut=min(range(1,len(toc)),key=lambda c:abs(sum(heights[:c])-sum(heights[c:])))
    band=len(EVENTS)
    for batch,x in [(toc[:cut],M),(toc[cut:],M+CW+G)]:
        yy=Y
        for u in batch:yy-=put(u,x,yy,CW,'duas-colunas','Consulta',band)
    # O plano antigo do corpo não é usado pelo gerador integral.
    return {k:v[0] for k,v in POSITIONS.items()}
    for page in PLAN:
        PAGE+=1;Y=TOP
        for bi,band in enumerate(page['bands']):
            if bi:Y-=4
            band_id=len(EVENTS);i,j,cut=band['i'],band['j'],band['cut']
            if cut is None:Y-=draw_atom(i,M,Y,AW,'uma-coluna',band_id)
            else:
                for begin,end,x in [(i,cut,M),(cut,j,M+CW+G)]:
                    yy=Y
                    for k in range(begin,end):
                        yy-=draw_atom(k,x,yy,CW,'duas-colunas',band_id)
                        if k+1<end:yy-=4
                Y-=band['height']
    return {k:v[0] for k,v in POSITIONS.items()}
