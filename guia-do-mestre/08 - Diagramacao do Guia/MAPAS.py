"""Mapas vetoriais: preservam os percursos e posições dos cinco exemplos."""
from reportlab.platypus import Flowable, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white

class Mapa(Flowable):
    def __init__(self, key, width):
        super().__init__()
        self.key, self.width = key, width
        self.height = {'s062':255, 's064':260, 's066':245, 's073':325, 's079':310}[key]
        self.ink=HexColor('#251727'); self.accent=HexColor('#9e2358')
        self.pale=HexColor('#f8f1f4'); self.rule=HexColor('#ded4d9')
    def wrap(self,w,h): return self.width,self.height
    def label(self,x,y,text,size=10.5,font='Body',align='center',color=None):
        c=self.canv;c.setFillColor(color or self.ink);c.setFont(font,size)
        {'center':c.drawCentredString,'left':c.drawString,'right':c.drawRightString}[align](x,y,text)
    def note(self,x,top,w,text):
        p=Paragraph(text,ParagraphStyle('map-note',fontName='Body',fontSize=10,leading=13,textColor=self.ink))
        hh=p.wrap(w,300)[1];p.drawOn(self.canv,x,top-hh)
    def line(self,points,color=None,width=1.5,dash=None):
        c=self.canv;c.setStrokeColor(color or self.accent);c.setLineWidth(width);c.setDash(dash or [])
        p=c.beginPath();p.moveTo(*points[0])
        for v in points[1:]:p.lineTo(*v)
        c.drawPath(p);c.setDash([])
    def box(self,x,y,w,h,text):
        c=self.canv;c.setFillColor(white);c.setStrokeColor(self.accent);c.setLineWidth(.8)
        c.roundRect(x,y,w,h,4,stroke=1,fill=1)
        rows=text.split('\n')
        for i,row in enumerate(rows):self.label(x+w/2,y+h/2+(len(rows)-1)*6-i*12-3,row,11,'Head')
    def dot(self,x,y):
        c=self.canv;c.setFillColor(self.accent);c.circle(x,y,2.5,fill=1,stroke=0)
    def draw(self):
        c=self.canv;c.saveState();c.setFillColor(self.pale);c.roundRect(0,0,self.width,self.height,4,fill=1,stroke=0)
        getattr(self,self.key)();c.restoreState()
    def s062(self):
        self.label(14,234,'DO TRABALHO AO RECUO: DOIS CAMINHOS',15,'Head','left')
        self.box(14,184,88,30,'ENTRADA')
        self.line([(58,184),(58,148)])
        self.label(70,163,'6 m regulares',10.5,'Body','left')
        self.box(14,100,88,48,'ÁREA DE\nTRABALHO\nCAIXA')
        self.box(386,100,88,48,'RECUO\nABERTO\n6 m × 6 m')
        self.label(246,164,'ROTA DIRETA · 18 m EM TRÊS TRECHOS',11,'Head')
        for i,terrain in enumerate(['piso regular','ENTULHO','piso regular']):
            x=110+i*90
            self.line([(x-8,124),(x,124)])
            c=self.canv;c.setFillColor(HexColor('#e4bfd1') if i==1 else white)
            c.setStrokeColor(self.accent);c.setLineWidth(.7);c.rect(x,101,82,46,fill=1,stroke=1)
            self.label(x+41,128,'6 m',12,'Head')
            self.label(x+41,112,terrain,10,'Head' if i==1 else 'Body')
        self.line([(372,124),(386,124)])
        self.line([(58,100),(58,50),(430,50),(430,100)])
        self.label(244,64,'ROTA LATERAL · 24 m DE PISO REGULAR',11,'Head')
        self.label(14,28,'As duas rotas ligam a área de trabalho ao mesmo recuo, com ida e volta.',9.5,'Body','left')
        self.label(14,12,'Distâncias físicas. Desenho sem escala; o entulho altera o custo de movimento.',9.5,'Body','left')
    def s064(self):
        self.label(14,239,'PASSARELA E ROTA INFERIOR',15,'Head','left')
        self.box(15,180,98,33,'OESTE\nGRUPO / PINO')
        self.box(375,180,98,33,'LESTE\nALAVANCA')
        self.line([(113,196),(194,196)])
        self.line([(294,196),(375,196)])
        self.label(153,207,'3 m');self.label(334,207,'3 m')
        self.box(194,180,100,33,'3 m MÓVEIS')
        self.label(184,169,'borda',9.5);self.label(304,169,'borda',9.5)
        self.line([(64,180),(64,59),(424,59),(424,180)])
        self.label(78,153,'3 m até a escada',10,'Body','left')
        self.label(410,153,'3 m até a escada',10,'Body','right')
        self.label(78,113,'descer 6 m',10,'Body','left')
        self.label(410,113,'subir 6 m',10,'Body','right')
        self.label(244,92,'PISO INFERIOR',11,'Head')
        self.label(244,71,'9 m entre as escadas')
        self.label(14,35,'Superior: 9 m físicos. Inferior: 27 m físicos / 39 m de movimento.',9.5,'Body','left')
        self.label(14,16,'Sem escala. Piso inferior 6 m abaixo; a queda não leva até a escada.',9.5,'Body','left')
    def s066(self):
        self.label(14,224,'SAÍDA CURTA E CORREDOR DE SERVIÇO',15,'Head','left')
        self.box(18,151,80,35,'A · PÁTIO')
        self.box(164,151,90,35,'G · PORTÃO')
        self.box(319,151,153,35,'C · TRABALHO / CAIXA')
        self.line([(98,168),(164,168)]);self.label(131,179,'3 m')
        self.line([(254,168),(319,168)]);self.label(286,179,'3 m')
        self.line([(58,151),(58,68),(393,68),(393,151)])
        self.label(70,111,'6 m',10.5,'Body','left');self.label(381,111,'6 m',10.5,'Body','right')
        self.label(226,82,'6 m pelo serviço')
        self.box(36,51,44,31,'Q');self.box(342,51,102,31,'P · PARADA')
        self.label(226,125,'PAREDE ENTRE AS ROTAS',10.5,'Head')
        self.line([(119,113),(333,113)],self.rule,5)
        self.label(14,31,'De C ao recuo: direta 18 m (6 m difíceis) ou lateral 24 m regulares.',9.5,'Body','left')
        self.label(14,12,'Esquema sem escala. Corredores novos com 3 m de largura livre.',9.5,'Body','left')
    def grid(self,cols,rows,x,y,cell,fill=None):
        c=self.canv
        if fill:
            c.setFillColor(fill);c.rect(x,y,len(cols)*cell,rows*cell,stroke=0,fill=1)
        for i in range(len(cols)+1):self.line([(x+i*cell,y),(x+i*cell,y+rows*cell)],self.rule,.6)
        for j in range(rows+1):self.line([(x,y+j*cell),(x+len(cols)*cell,y+j*cell)],self.rule,.6)
        for i,a in enumerate(cols):self.label(x+(i+.5)*cell,y+rows*cell+9,a,10,'Head')
        for r in range(1,rows+1):self.label(x-9,y+(r-.5)*cell-3,str(r),9.5,'Body','right')
    def s073(self):
        self.label(14,304,'SINEIRO · POSIÇÕES INICIAIS',15,'Head','left')
        c=self.canv;x,y,sz=39,50,18
        self.grid('ABCDEFGH',12,x,y,sz,white)
        self.line([(x,y),(x,y+12*sz),(x+8*sz,y+12*sz),(x+8*sz,y)],self.ink,1)
        self.line([(x,y),(x+2*sz,y)],self.ink,2);self.line([(x+6*sz,y),(x+8*sz,y)],self.ink,2)
        c.setFillColor(self.accent);c.rect(x+3*sz,y+5*sz,2*sz,2*sz,stroke=0,fill=1)
        self.label(x+4*sz,y+6*sz-4,'S',15,'Head',color=white)
        c.setFillColor(white);c.setStrokeColor(self.ink);c.setLineWidth(1);c.rect(x+2*sz+5,y+5*sz+5,8,8,fill=1,stroke=1)
        for col,t in [(2,'R'),(3,'M'),(5,'A')]:self.label(x+(col+.5)*sz,y-17,t,11,'Head')
        self.label(x-9,y-17,'0',9.5,'Body','right')
        self.label(x+4*sz,11,'Porta: C–F · 6 m',10,'Body')
        self.note(220,270,248,'<b>Recinto: 12 × 18 m.</b><br/>Cada célula mede 1,5 m.<br/>A linha 0 fica no exterior.')
        self.note(220,203,248,'<b>S · Sineiro:</b> D6, E6, D7 e E7.<br/><b>Quadrado · Caixa:</b> C6.<br/><b>R · Rina:</b> C0.<br/><b>M · Mei:</b> D0.<br/><b>A · Akira:</b> F0.')
        self.note(220,99,248,'De C0 à caixa: 9 m.<br/>Linhas negativas continuam para fora do recinto.')
    def s079(self):
        self.label(14,289,'SALA DE CONSERVAÇÃO · EXPOSIÇÃO AO PÓ',15,'Head','left')
        c=self.canv;x,y,sz=48,52,16
        self.grid('AB',12,x,y,sz,HexColor('#ecd7e1'))
        self.line([(x,y),(x,y+12*sz),(x+2*sz,y+12*sz),(x+2*sz,y)],self.ink,1.2)
        self.dot(x+sz/2,y+12*sz);self.line([(x+sz/2,y+12*sz),(112,y+12*sz)])
        self.note(128,251,340,'<b>Fecho e pino:</b> junto de A12, na parede. Não ocupam o piso.')
        self.note(128,188,340,'<b>Área com pó:</b> A1–A12 e B1–B12.<br/>Sala de 3 × 18 m; cada célula mede 1,5 m. As paredes laterais impedem sair pelas bordas.')
        self.label(x+sz/2,y-17,'M',10,'Head');self.label(x+1.5*sz,y-17,'A',10,'Head');self.label(x-9,y-17,'0',9.5,'Body','right')
        self.line([(x+2*sz,y-13),(112,y-13)])
        self.note(128,79,340,'<b>Vestíbulo limpo:</b> Mei em A0; Akira em B0. Exaustor junto de B0.')
        self.label(14,12,'Posições indicadas. O desenho não representa o tamanho dos controles.',9.5,'Body','left')
