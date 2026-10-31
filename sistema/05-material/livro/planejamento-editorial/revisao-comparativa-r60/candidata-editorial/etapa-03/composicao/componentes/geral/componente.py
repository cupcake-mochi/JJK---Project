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
PDF=OUT/'Projeto-M-Regras-Gerais-Piloto-B-R17.pdf'
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
texts={k:(B/'fontes-capturadas'/n).read_text() for k,n in [('geral','REGRAS-GERAIS.md'),('dano','DANO-E-RECUPERACAO.md')]}
texts.update(globals().get('_texto_editorial_revisado',{}))
from identidade import nome_oficial
texts={k:nome_oficial(v) for k,v in texts.items()}
blocks=[]
for doc,txt in texts.items():
    for m in re.finditer(r'<!-- page:([^|]+)\|([^>]+)-->\s*(.*?)(?=<!-- page:|\Z)',txt,re.S):
        key,title,md=[v.strip() for v in m.groups()]
        if doc=='dano' and key not in ['condicoes','leves','medias','pesadas']:continue
        blocks.append({'doc':doc,'anchor':key,'title':title,'md':md,'key':doc+'--'+key})
assert len(blocks)==44,len(blocks)
# Only the position of these two intact blocks changes in the visual pilot.
# Combat navigation must also reach common grappling and escape procedures.
manoeuvres=[b for b in blocks if b['doc']=='geral' and b['anchor'] in ['manobras','contencoes']]
blocks=[b for b in blocks if b not in manoeuvres]
movement_position=next(i for i,b in enumerate(blocks) if b['anchor']=='movimento')
blocks[movement_position:movement_position]=manoeuvres
keys={b['key'] for b in blocks}
starts=['atributos','turnos','movimento','perceber','condicoes']
groups=['Testes','Combate','Movimento','Percepção','Condições']
nav=[('Consulta','consulta')]+[(g,('dano' if a=='condicoes' else 'geral')+'--'+a) for g,a in zip(groups,starts)]
current=0
for b in blocks:
    if b['anchor'] in starts:current=starts.index(b['anchor'])
    b['group']=groups[current]
    b['group_start']=b['anchor'] in starts

PAGES={};POSITIONS={};EVENTS=[];DRAW=[];PAGE=1;Y=TOP;GROUP='Consulta';LAYOUT=[]

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
        super().__init__();self.name=name;self.width=w;self.height=180
    def wrap(self,w,h):return self.width,self.height
    def draw(self):
        c=self.canv;w=self.width;c.saveState()
        c.setFillColor(PALE);c.setStrokeColor(EDGE);c.setLineWidth(.65)
        c.roundRect(0,0,w,180,5,stroke=1,fill=1)
        def label(text,x,y,center=False):
            c.setFont('Body',9);c.setFillColor(INK)
            (c.drawCentredString if center else c.drawString)(x,y,text)
        def ray(x1,y1,x2,y2):
            c.setStrokeColor(ACC);c.setLineWidth(1.1);c.line(x1,y1,x2,y2)
            angle=math.atan2(y2-y1,x2-x1)
            for off in [-.5,.5]:c.line(x2,y2,x2-7*math.cos(angle+off),y2-7*math.sin(angle+off))
        def diamond(x,y):
            p=c.beginPath();p.moveTo(x,y+5);p.lineTo(x+5,y);p.lineTo(x,y-5);p.lineTo(x-5,y);p.close()
            c.setFillColor(ACC);c.drawPath(p,fill=1,stroke=0)
        if self.name=='movimento':
            cell=30;gx=16;gy=79
            for i in range(6):
                c.setFillColor(RULE if i==3 else white);c.setStrokeColor(EDGE);c.setLineWidth(.5)
                c.rect(gx+i*cell,gy,cell,cell,fill=1,stroke=1)
            # Texture distinguishes rubble even without color.
            c.setStrokeColor(MUTED);c.setLineWidth(.5)
            for dx,dy in [(6,6),(19,18),(11,23),(23,8)]:
                c.line(gx+3*cell+dx-2,gy+dy,gx+3*cell+dx+2,gy+dy)
            ray(gx+cell/2,gy+cell/2,gx+5.5*cell,gy+cell/2)
            c.setFillColor(INK);c.circle(gx+cell/2,gy+cell/2,4,fill=1,stroke=0)
            label('Início',gx+cell/2,gy+cell+12,True);label('Fim',gx+5.5*cell,gy+cell+12,True)
            label('Entulho',gx+3.5*cell,gy-17,True)
            label('Cada quadrado: 1,5 m.',16,42)
            title='Percurso e custo'
            texts=['3 m regulares: gasta 3 m.','1,5 m de entulho: gasta 3 m.','3 m regulares: gasta 3 m.','<b>Percurso: 7,5 m.</b>','<b>Movimento gasto: 9 m.</b>']
        else:
            diamond(37,105);diamond(173,54)
            c.setFillColor(INK);c.circle(173,105,5,fill=1,stroke=0)
            c.setStrokeColor(MUTED);c.setLineWidth(5);c.line(108,83,108,133)
            ray(45,105,166,105);ray(173,62,173,98)
            label('Atirador A',37,127,True);label('Sousuke',173,127,True)
            label('Atacante B',173,34,True);label('Mureta',108,150,True)
            title='Cobertura e direção'
            texts=['Boa cobertura definida na cena.','Defesa base de Sousuke: 15.','<b>Contra A: 20 (+5).</b>','<b>Contra B: 15.</b>','B está do mesmo lado da mureta.']
        x=220;y=161
        p=Paragraph(title,S['h2']);h=p.wrap(w-x-12,180)[1];p.drawOn(c,x,y-h);y-=h+8
        for text in texts:
            p=Paragraph(text,S['note']);h=p.wrap(w-x-12,180)[1];p.drawOn(c,x,y-h);y-=h+5
        c.setFont('Body',9);c.setFillColor(MUTED);c.drawString(16,14,'Esquema de posições. Símbolos sem escala de tamanho.')
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
            elif n==3:fr=[.22,.23,.55]
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


def pagebreak(group=None):
    global PAGE,Y,GROUP
    PAGE+=1;Y=TOP
    if group:GROUP=group


def put(unit,x,y,w,mode,band=None):
    ht,measured=unit.measure(w);yy=y;unit_id=len(EVENTS)
    assert y-ht>=BOTTOM-.01,(PAGE,'vertical overflow',y-ht)
    for p,f,b,h,a in measured:
        yy-=b
        DRAW.append((PAGE,GROUP,p,f,x,yy-h,w,h,mode))
        if p.key:
            assert p.key not in POSITIONS,p.key
            POSITIONS[p.key]=(PAGE,x,yy)
        EVENTS.append({'pagina':PAGE,'grupo':GROUP,'bloco':p.block,'tipo':p.kind,'x':round(x,2),'topo':round(yy,2),'largura':round(w,2),'altura':round(h,2),'modo':mode,'faixa':band,'unidade':unit_id,'exemplo_ligado':unit.connected,'sha256_texto':hashlib.sha256(str(p.text).encode()).hexdigest()})
        yy-=h+a
    return ht


def columns(items,closing=False):
    global Y
    items=list(items)
    while items:
        available=Y-BOTTOM
        # Short prose bands read better across the page than in a single
        # half-width column beside empty space. This also allows a compact
        # explanation and its example to fit below the related table.
        full_height=sum(u.measure(AW)[0] for u in items)
        part_count=sum(len(u.parts) for u in items)
        if GROUP!='Consulta' and full_height<=240 and part_count<=7:
            if full_height>available:pagebreak()
            for unit in items:Y-=put(unit,M,Y,AW,'uma-coluna')
            Y-=6;break
        heights=[u.measure(CW)[0] for u in items]
        if max(heights)>TOP-BOTTOM:
            raise ValueError(('Bloco maior que a coluna; precisa composição ampla',max(heights)))
        # Balance whole blocks when the remaining segment fits both columns.
        prefix=[0]
        for h in heights:prefix.append(prefix[-1]+h)
        possible=[i for i in range(1,len(items)) if prefix[i]<=available and prefix[-1]-prefix[i]<=available]
        if len(items)==1:
            h=items[0].measure(AW)[0]
            if h>available:pagebreak()
            Y-=put(items[0],M,Y,AW,'uma-coluna')+6;break
        if possible:
            cut=min(possible,key=lambda i:abs(prefix[i]-(prefix[-1]-prefix[i])))
            for part,x in [(items[:cut],M),(items[cut:],M+CW+G)]:
                yy=Y
                for u in part:yy-=put(u,x,yy,CW,'duas-colunas')
            Y-=max(prefix[cut],prefix[-1]-prefix[cut])+6;break
        # Redistribute a segment's last two pages instead of leaving just
        # one closing paragraph on an otherwise empty final page.
        full_height=TOP-BOTTOM
        if closing and len(items)>=4 and prefix[-1]<=2*available+2*full_height:
            candidates=[];count=len(items)
            for a in range(1,count-2):
                if prefix[a]>available:break
                for b in range(a+1,count-1):
                    if prefix[b]-prefix[a]>available:break
                    for d in range(b+1,count):
                        hs=[prefix[a],prefix[b]-prefix[a],prefix[d]-prefix[b],prefix[-1]-prefix[d]]
                        if hs[2]>full_height:break
                        if hs[3]>full_height:continue
                        score=(max(hs),abs(hs[0]+hs[1]-hs[2]-hs[3]))
                        candidates.append((score,[0,a,b,d,count],hs))
            if candidates:
                _,cuts,hs=min(candidates,key=lambda row:row[0])
                for col in range(4):
                    if col==2:pagebreak()
                    x=M if col%2==0 else M+CW+G;yy=Y
                    for u in items[cuts[col]:cuts[col+1]]:
                        yy-=put(u,x,yy,CW,'duas-colunas')
                    if col==3:Y-=max(hs[2:])+6
                break
        used=[];consumed=0
        for x in [M,M+CW+G]:
            yy=Y;num=0
            while consumed<len(items):
                h=items[consumed].measure(CW)[0]
                if yy-h<BOTTOM:break
                yy-=put(items[consumed],x,yy,CW,'duas-colunas');consumed+=1;num+=1
            used.append(Y-yy)
        if consumed==0:
            pagebreak();continue
        items=items[consumed:];Y-=max(used)+6
        if items:pagebreak()


def wide(u):
    global Y
    h=u.measure(AW)[0]
    assert h<=TOP-BOTTOM,('Tabela grande demais para página',h)
    if h>Y-BOTTOM:pagebreak()
    Y-=put(u,M,Y,AW,'uma-coluna')


# Each information group is measured as a whole before page placement.
# Prose may use balanced columns inside it, but never an empty second column.
INFORMATION=[]

def prose_band(units):
    full=sum(u.measure(AW)[0] for u in units)
    if len(units)<2:return {'units':units,'height':full,'cut':None}
    hs=[u.measure(CW)[0] for u in units];prefix=[0]
    for h in hs:prefix.append(prefix[-1]+h)
    cut=min(range(1,len(units)),key=lambda i:max(prefix[i],prefix[-1]-prefix[i]))
    left,right=prefix[cut],prefix[-1]-prefix[cut];height=max(left,right)
    # A short paragraph must not create an empty-looking column beside it.
    balanced=abs(left-right)<=max(30,height*.25)
    if balanced and height<=full+36 and height<=TOP-BOTTOM:
        return {'units':units,'height':height,'cut':cut}
    return {'units':units,'height':full,'cut':None}

def compose(units):
    bands=[];prose=[]
    def flush():
        if prose:
            bands.append(prose_band(list(prose)));prose.clear()
    for unit in units:
        if unit.wide or any(p.kind in ['major','h1'] for p in unit.parts):
            flush();bands.append({'units':[unit],'height':unit.measure(AW)[0],'cut':None})
        else:prose.append(unit)
    flush()
    return bands,sum(band['height'] for band in bands)+2*max(0,len(bands)-1)

def render_information(units,key):
    global Y
    bands,height=compose(units)
    assert height<=TOP-BOTTOM,(key,'Conjunto precisa de revisão editorial',height)
    if height>Y-BOTTOM:pagebreak()
    start=len(EVENTS)
    for band in bands:
        band_id=len(EVENTS)
        if band['cut'] is None:
            for unit in band['units']:Y-=put(unit,M,Y,AW,'uma-coluna',band=band_id)
        else:
            cut=band['cut']
            for part,x in [(band['units'][:cut],M),(band['units'][cut:],M+CW+G)]:
                yy=Y
                for unit in part:yy-=put(unit,x,yy,CW,'duas-colunas',band=band_id)
            Y-=band['height']
        Y-=2
    Y-=4
    INFORMATION.append({'chave':key,'pagina':PAGE,'altura':round(height,2),
        'eventos':list(range(start,len(EVENTS))),'blocos':list(dict.fromkeys(p.block for u in units for p in u.parts))})

def split_information(units,block):
    if block=='geral--resistencia':return [(block,units)]
    sections=[];current=[]
    for unit in units:
        if current and any(p.kind in ['h2','h3'] for p in unit.parts):
            sections.append(current);current=[]
        current.append(unit)
    if current:sections.append(current)
    if (len(sections)>1
        and not any(u.wide for u in sections[0])
        and any(p.kind in ['h1','major'] for u in sections[0] for p in u.parts)
        and not any(p.kind in ['h2','h3'] for u in sections[0] for p in u.parts)
        and compose(sections[0]+sections[1])[1]<=TOP-BOTTOM):
        sections[:2]=[sections[0]+sections[1]]
    return [(block+'--informacao-'+str(i+1),s) for i,s in enumerate(sections)]

def record_atom(unit,key,start):
    INFORMATION.append({'chave':key,'pagina':PAGE,'eventos':list(range(start,len(EVENTS))),
        'blocos':list(dict.fromkeys(p.block for p in unit.parts))})

def flow_information(atoms):
    global Y
    atoms=list(atoms)
    while atoms:
        available=Y-BOTTOM
        heights=[u.measure(CW)[0] for _,u in atoms];prefix=[0]
        for h in heights:prefix.append(prefix[-1]+h)
        # Avoid carrying just two short topics onto a nearly empty page
        # before a large, complete table section. Rebalance the whole band.
        if len(atoms)>=3:
            candidates=[]
            for cut in range(1,len(atoms)):
                a,b=prefix[cut],prefix[-1]-prefix[cut];h=max(a,b)
                if abs(a-b)<=max(30,h*.25):candidates.append(h)
            if candidates:
                full=min(candidates)
                if available<full<=.65*(TOP-BOTTOM) and available<.65*(TOP-BOTTOM):
                    pagebreak();continue
        options=[]
        for end in range(2,len(atoms)+1):
            for cut in range(1,end):
                a,b=prefix[cut],prefix[end]-prefix[cut];h=max(a,b)
                if h<=available and abs(a-b)<=max(30,h*.25):
                    options.append((-end,h,abs(a-b),cut))
        if options:
            neg_end,height,_,cut=min(options);end=-neg_end;band_id=len(EVENTS)
            for batch,x in [(atoms[:cut],M),(atoms[cut:end],M+CW+G)]:
                yy=Y
                for key,unit in batch:
                    start=len(EVENTS);yy-=put(unit,x,yy,CW,'duas-colunas',band=band_id)
                    record_atom(unit,key,start)
            Y-=height+4;atoms=atoms[end:]
        else:
            key,unit=atoms[0];height=unit.measure(AW)[0]
            if hasattr(unit,'inner') and compose(unit.inner)[1]<height:
                render_information(unit.inner,key);atoms.pop(0);continue
            assert height<=TOP-BOTTOM,(key,'Conjunto longo demais',height)
            if height>available:pagebreak();continue
            start=len(EVENTS);Y-=put(unit,M,Y,AW,'uma-coluna',band=start)+4
            record_atom(unit,key,start);atoms.pop(0)


# Local corrections to the approved R14 plan. No global pagination changes.
# The original element order and all unselected page coordinates are preserved.
TARGET_LOG=[]
def recompose_approved_pairs():
    global PAGE,Y,GROUP,DRAW,EVENTS,POSITIONS,INFORMATION,TARGET_LOG
    base_draw=list(DRAW);base_events=list(EVENTS);base_info=list(INFORMATION)
    patches={
        4: {'pages':(4,5),'bands':[
            ([75,76],[77,78]),
            ([79],None),
            ([80,81,82,83,84],[85,86,87,88,89])]},
        17: {'pages':(17,18),'bands':[
            ([226,227,228],None),
            ([229],None),
            ([230],[231]),
            ([232,233,234],None),
            ([235,236,237],[238,239])]},
        30: {'pages':(30,31),'bands':[
            ([362,363],None),
            ([364,365,366,367],[368,369,370,371]),
            ([372,373,374,375,376],None)]}}
    removed={pair['pages'][1] for pair in patches.values()}
    old_to_new={n:n-sum(r<n for r in removed) for n in range(1,PAGE+1) if n not in removed}
    DRAW=[];EVENTS=[];POSITIONS={'consulta':(1,M,TOP)};TARGET_LOG=[]
    for old_page,new_page in old_to_new.items():
        PAGE=new_page
        if old_page in patches:
            patch=patches[old_page];Y=TOP
            flat=[i for left,right in patch['bands'] for batch in [left,right] if batch for i in batch]
            original=[i for i,e in enumerate(base_events) if e['pagina'] in patch['pages']]
            assert flat==original,('Local source order changed',old_page)
            GROUP=base_draw[flat[0]][1]
            for left,right in patch['bands']:
                band=len(EVENTS)
                if right is None:
                    unit=Unit([base_draw[i][2] for i in left],connected=True)
                    Y-=put(unit,M,Y,AW,'uma-coluna',band=band)
                else:
                    a=Unit([base_draw[i][2] for i in left],connected=True)
                    b=Unit([base_draw[i][2] for i in right],connected=True)
                    ah=a.measure(CW)[0];bh=b.measure(CW)[0]
                    assert abs(ah-bh)<=max(30,max(ah,bh)*.25),(old_page,'Unbalanced local band',ah,bh)
                    put(a,M,Y,CW,'duas-colunas',band=band)
                    put(b,M+CW+G,Y,CW,'duas-colunas',band=band)
                    Y-=max(ah,bh)
                Y-=2
            assert Y+2>=BOTTOM,(old_page,'Local overflow')
            TARGET_LOG.append({'paginas_r14':list(patch['pages']),'pagina_r15':new_page,
                'altura_conteudo_pt':round(TOP-Y-2,2),
                'mudanca':'Duas páginas reunidas em uma, por faixas medidas de uma e duas colunas.'})
        else:
            ids=[i for i,e in enumerate(base_events) if e['pagina']==old_page]
            for i in ids:
                row=base_draw[i];DRAW.append((new_page,)+row[1:])
                event=dict(base_events[i]);event['pagina']=new_page;EVENTS.append(event)
    assert len(DRAW)==len(base_draw)==len(EVENTS)
    for i,(old,row) in enumerate(zip(base_draw,DRAW)):
        assert old[2] is row[2],('Part reordered',i)
        part=row[2]
        if part.key:POSITIONS[part.key]=(row[0],row[4],row[5]+row[7])
        if old[0] not in {n for pair in patches.values() for n in pair['pages']}:
            assert old[1:]==row[1:],('Approved geometry changed',i)
    INFORMATION=[]
    for info in base_info:
        updated=dict(info);pages={EVENTS[i]['pagina'] for i in info['eventos']}
        assert len(pages)==1,(info['chave'],'Information split')
        updated['pagina']=pages.pop()
        if info['pagina'] in {n for pair in patches.values() for n in pair['pages']}:
            updated.pop('altura',None)
        INFORMATION.append(updated)
    PAGE=max(row[0] for row in DRAW)
    TARGET_LOG.append({'paginas_r14':[11,12],'paginas_r15':[old_to_new[11],old_to_new[12]],
        'mudanca':'Revisadas e preservadas: procedimentos completos, colunas ocupadas e leitura sem compressão.',
        'motivo':'Os blocos totalizam 982 pt em largura inteira e 1664 pt em colunas. Reunir tudo excederia os 674,65 pt úteis por página.'})
    return old_to_new


# Page 34 exception: move its complete table subsection onto the opening,
# and collect the entire hiding procedure on the next page. All other pages
# keep the exact R15 geometry, apart from their updated page number.
LOCAL_R16={}
class PageEndUnit(Unit):
    def measure(self,w):
        height,items=super().measure(w)
        p,f,b,h,a=items[-1]
        # No after-space is needed after the last block on a finished page.
        items[-1]=(p,f,b,h,0)
        return height-a,items

def recompose_perception_opening():
    global PAGE,Y,GROUP,DRAW,EVENTS,POSITIONS,INFORMATION,LOCAL_R16
    base_draw=list(DRAW);base_events=list(EVENTS);base_info=list(INFORMATION)
    ids=[i for i,e in enumerate(base_events) if e['bloco'] in ['geral--perceber','geral--esconder']]
    assert ids==list(range(ids[0],ids[-1]+1))
    start,end=ids[0],ids[-1]+1
    assert end-start==26
    # A revisão de Carga pode deixar o fim de Combate montado na antiga
    # página de abertura. Preserve-o e aplique a mesma composição aprovada
    # de Percepção/Esconder nas duas páginas seguintes, sem sobreposição.
    opening=max(row[0] for row in base_draw[:start])+1
    old_pages=sorted({e['pagina'] for e in base_events[start:end]})
    suffix_offset=opening+2-base_draw[end][0]
    DRAW=[];EVENTS=[];POSITIONS={'consulta':(1,M,TOP)}
    DRAW.extend(base_draw[:start]);EVENTS.extend(dict(e) for e in base_events[:start])
    PAGE=opening;GROUP='Percepção';Y=TOP
    unit=PageEndUnit([base_draw[i][2] for i in range(start,start+12)],connected=True)
    Y-=put(unit,M,Y,AW,'uma-coluna',band=len(EVENTS))
    PAGE=opening+1;GROUP='Percepção';Y=TOP
    for a,b in [(start+12,start+17),(start+17,start+22),(start+22,end)]:
        unit=Unit([base_draw[i][2] for i in range(a,b)],connected=True)
        Y-=put(unit,M,Y,AW,'uma-coluna',band=len(EVENTS))
        if b!=end:Y-=2
    for row,e in zip(base_draw[end:],base_events[end:]):
        number=row[0]+suffix_offset
        DRAW.append((number,)+row[1:])
        updated=dict(e);updated['pagina']=number;EVENTS.append(updated)
    assert len(DRAW)==len(base_draw)==len(EVENTS)
    for old,row in zip(base_draw,DRAW):
        assert old[2] is row[2],('Part reordered',old[2].block)
        part=row[2]
        if part.key:POSITIONS[part.key]=(row[0],row[4],row[5]+row[7])
        if part.block not in ['geral--perceber','geral--esconder']:
            assert old[1:]==row[1:],'Approved R15 geometry changed'
    INFORMATION=[]
    for info in base_info:
        updated=dict(info);pages={EVENTS[i]['pagina'] for i in info['eventos']}
        assert len(pages)==1,(info['chave'],'Information split')
        updated['pagina']=pages.pop()
        if any(start<=i<end for i in info['eventos']):updated.pop('altura',None)
        INFORMATION.append(updated)
    PAGE=max(row[0] for row in DRAW)
    LOCAL_R16={'paginas_r15':old_pages,'paginas_r16':[opening,opening+1],
        'mudanca':'Percepção e visibilidade completa na página 34; Esconder completo na página 35.',
        'motivo':'Eliminar o vão da abertura sem deixar uma página seguinte com apenas um complemento curto.',
        'espacamento':'Removido somente o espaço reservado após o último quadro de exemplo da página 34. Fontes e entrelinhas preservadas.',
        'restante_aprovado_preservado':True}


LOCAL_R17={}
def recompose_movement_opening():
    global PAGE,Y,GROUP,DRAW,EVENTS,LOCAL_R17
    base_draw=list(DRAW);base_events=list(EVENTS);last_page=PAGE
    ids=[i for i,e in enumerate(base_events) if e['pagina']==22]
    assert ids==list(range(303,311))
    for i in ids:
        key=base_draw[i][2].key
        if key:POSITIONS.pop(key)
    DRAW=base_draw[:303];EVENTS=base_events[:303]
    PAGE=22;GROUP='Movimento';Y=TOP
    for a,b in [(303,308),(308,311)]:
        unit=Unit([base_draw[i][2] for i in range(a,b)],connected=True)
        start=len(EVENTS);Y-=put(unit,M,Y,AW,'uma-coluna',band=start)
        if b!=311:Y-=4
    DRAW+=base_draw[311:];EVENTS+=base_events[311:]
    for old,new in zip(base_draw,DRAW):
        assert old[2] is new[2],'Source part reordered'
        if old[0]!=22:assert old==new,'Approved geometry changed'
        if new[2].key:POSITIONS[new[2].key]=(new[0],new[4],new[5]+new[7])
    for info in INFORMATION:
        if info['pagina']==22:info.pop('altura',None)
    PAGE=last_page
    LOCAL_R17={'pagina':22,'mudanca':'Metros disponíveis e Medidas de 1,5 m em largura inteira, sem trocar o número de colunas dentro da explicação.',
        'motivo':'A alternância de um parágrafo amplo com os seguintes em duas colunas criava degraus na leitura.',
        'restante_aprovado_preservado':True,'corpo_e_entrelinha_preservados':True}

def build_plan(pagemap):
    global PAGE,Y,GROUP,DRAW,EVENTS,POSITIONS,INFORMATION
    PAGE=1;Y=TOP;GROUP='Consulta';DRAW=[];EVENTS=[];INFORMATION=[];POSITIONS={'consulta':(1,M,TOP)}
    wide(Unit([Part('major','Regras gerais'),Part('small','Piloto de diagramação • capítulo completo e amostra de condições'),Part('h2','Consulta')],True))
    toc=[]
    for group in groups:
        members=[b for b in blocks if b['group']==group]
        entries=[]
        for b in members:
            number=pagemap.get(b['key'],'-')
            text=f'<link href="#{b["key"]}" color="#251727">{escape(b["title"])} <font color="#65545F">{number}</font></link>'
            entry=Part('index',text,block='indice')
            entry.make=lambda w,p=entry:(Paragraph(p.text,S['index']),0,4)
            entries.append(entry)
        toc.append(Unit([Part('h2',group),entries[0]]))
        toc.extend(Unit([p]) for p in entries[1:])
    columns(toc)
    # O gerador integral usa apenas esta consulta; o corpo flui pela R31.
    return {k:p[0] for k,p in POSITIONS.items()}
    for group in groups:
        if group in ['Testes','Condições']:pagebreak(group)
        else:GROUP=group
        pending=[]
        for bi,b in enumerate([b for b in blocks if b['group']==group]):
            units=parse(b)
            if bi==0:units[0].parts[0].kind='major'
            sections=split_information(units,b['key'])
            if bi==0 and len(sections)>1:
                first_two=sum(compose(section)[1]+6 for _,section in sections[:2])
                if first_two<=TOP-BOTTOM and first_two>Y-BOTTOM:pagebreak()
            for key,section in sections:
                if (any(u.wide or any(p.kind=='major' for p in u.parts) for u in section)
                    or (b['key']=='geral--critico' and any(p.kind=='h1' for u in section for p in u.parts))):
                    if pending:flow_information(pending);pending=[]
                    render_information(section,key)
                else:
                    atom=Unit([p for u in section for p in u.parts],connected=True)
                    atom.inner=section
                    pending.append((key,atom))
        if pending:flow_information(pending)
    recompose_approved_pairs()
    recompose_perception_opening()
    recompose_movement_opening()
    return {k:p[0] for k,p in POSITIONS.items()}
