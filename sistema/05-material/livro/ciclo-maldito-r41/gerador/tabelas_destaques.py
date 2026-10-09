"""Provas de tabelas e destaques; mantém literalmente todo o texto editorial."""
import json,re,hashlib
from functools import lru_cache
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor,white
from reportlab.platypus import Paragraph,Table,TableStyle
from reportlab.lib.enums import TA_LEFT,TA_CENTER,TA_RIGHT

INK=HexColor('#251727');ACC=HexColor('#9e2358');LINE=HexColor('#d8d1d4');STRIPE=HexColor('#f2eff0');PALE=HexColor('#f8f1f4');GREY=HexColor('#8c7d85')
def signature(block,text):return hashlib.sha256(json.dumps([block,text],ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def plain(s):
 s=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',str(s));return re.sub(r'[*`]', '',s).replace('−','-').replace('–','-').replace('—','-')

def instalar(Part,ns):
 original=Part.make;root=ns['B'];cfg=json.loads((root/'ESTUDO-TABELAS.json').read_text());variant=cfg['id'];S=ns['S'];inline=ns['inline']
 inventory=json.loads((root/'DESTAQUES-CATALOGO.json').read_text());note_index={signature(n['bloco'],n['texto']):n for n in inventory}
 records={};note_records={};geometry={};baseline_fractions=ns['fractions']
 hstyle=ParagraphStyle('table-clean-heading',parent=S['headcell'],textColor=INK,spaceAfter=0)
 cellstyle=ParagraphStyle('table-clean-cell',parent=S['cell'],spaceAfter=0,splitLongWords=0)
 headstyle=ParagraphStyle('table-clean-head',parent=hstyle,splitLongWords=0)

 def number_col(rows,j):
  if rows[0][j] in ['Propriedades','Aplicação','Efeito','Habilidade','Habilidades']:return False
  cells=[plain(r[j]).strip().rstrip('.') for r in rows[1:] if r[j] and not all(not x for x in r[1:])]
  return bool(cells) and sum(bool(re.fullmatch(r'[+\-\d.,/ ×%]+(?:\s*(?:PE|PV|m|kg))?',x)) for x in cells)/len(cells)>=.8
 def headerless(part):return part.block=='guia--guia' and part.text[0][0]=='Dado de vida, na variante'
 def styles(rows,headerless=False):
  ret=[]
  for i,row in enumerate(rows):
   category=i>0 and all(not v for v in row[1:])
   sr=[]
   for j,val in enumerate(row):
    st=headstyle if i==0 and not headerless else cellstyle
    if category:st=ParagraphStyle('table-category',parent=cellstyle,fontName='Head',textColor=ACC)
    elif number_col(rows,j):st=ParagraphStyle('table-number',parent=st,alignment=TA_RIGHT if 'Preço' in rows[0][j] or 'Volume' in rows[0][j] else TA_CENTER)
    sr.append(st)
   ret.append(sr)
  return ret
 def choose(part,w):
  rows=part.text;key=(signature(part.block,rows),round(w,4))
  if key in geometry:return geometry[key]
  n=len(rows[0]);sts=styles(rows,headerless(part));pars=[[Paragraph(inline(v,part.doc),sts[i][j]) for j,v in enumerate(row)] for i,row in enumerate(rows)]
  minima=[]
  for j in range(n):
   widths=[]
   for i,row in enumerate(rows):
    if i>0 and all(not v for v in row[1:]):continue
    widths.append(pars[i][j].minWidth())
   minima.append(max([18]+widths)+10)
  base=list(baseline_fractions(rows));candidates=[base]
  if n==2:
   candidates.extend([[a,1-a] for a in [.22,.26,.30,.34,.38,.42,.46,.50]])
  elif n==3:
   candidates.extend([[a,b,1-a-b] for a in [.18,.23,.28,.33,.38,.43] for b in [.13,.18,.23,.28,.33,.38] if 1-a-b>=.24])
   if rows[0]==['Forma','Preço','Aplicação']:candidates.append([.23,.14,.63])
  elif n==7 and rows[0][0]=='Arma':
   widths=[0.0]*7
   for j in [1,4,5,6]:widths[j]=max(minima[j],max(pdfmetrics.stringWidth(plain(r[j]),cellstyle.fontName,cellstyle.fontSize) for r in rows)+10)
   left=w-sum(widths)
   for j,f in [(0,.27),(2,.23),(3,.50)]:widths[j]=left*f
   candidates.append([x/w for x in widths])
  options=[]
  for fr in candidates:
   ww=[w*f for f in fr]
   if any(ww[j]+.01<minima[j] for j in range(n)):continue
   hh=[]
   for i,row in enumerate(rows):
    if i>0 and all(not v for v in row[1:]):rh=pars[i][0].wrap(w-10,10000)[1]+6
    else:rh=max(p.wrap(ww[j]-10,10000)[1] for j,p in enumerate(pars[i]))+6
    hh.append(rh)
   score=sum(hh)+(.8*abs(fr[0]-.34) if n==2 else 0)
   options.append((score,fr,hh))
  if not options:
   # Full-width numeric matrices retain their proportions, with minima accommodated.
   if sum(minima)>w:fr=base
   else:
    extra=w-sum(minima);fr=[(minima[j]+extra*base[j])/w for j in range(n)]
   hh=[max(p.wrap(max(1,w*fr[j]-10),10000)[1] for j,p in enumerate(row))+6 for row in pars]
  else:_,fr,hh=min(options,key=lambda t:t[0])
  result={'fractions':fr,'heights':hh,'minima':minima,'narrow_ok':sum(minima)<=w and all(w*fr[j]>=minima[j]-.1 for j in range(n))}
  geometry[key]=result;return result

 def narrow(part):
  n=len(part.text[0]);count=len(part.text)-1
  if n>8:return False
  z=choose(part,ns['CW'])
  return z['narrow_ok'] and max(z['heights'])<=81 and z['heights'][0]<=44
 ns['tabela_larga']=lambda p:not narrow(p)

 def make(self,w):
  if self.kind=='table':
   rows=self.text;n=len(rows[0]);geo=choose(getattr(self,'r38_original',self),w);sts=styles(rows,headerless(self));data=[[Paragraph(inline(v,self.doc),sts[i][j]) for j,v in enumerate(row)] for i,row in enumerate(rows)]
   t=Table(data,colWidths=[w*f for f in geo['fractions']],repeatRows=0 if headerless(self) else 1,hAlign='LEFT')
   cmds=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),('LINEBELOW',(0,-1),(-1,-1),.4,LINE)]
   start=0 if headerless(self) else 1
   if not headerless(self):cmds.append(('LINEBELOW',(0,0),(-1,0),.6,ACC))
   if variant=='linhas':cmds.append(('LINEBELOW',(0,start),(-1,-2),.25,LINE))
   else:cmds.append(('ROWBACKGROUNDS',(0,start),(-1,-1),[STRIPE,white]))
   for i,row in enumerate(rows):
    if i>0 and all(not v for v in row[1:]):cmds.extend([('SPAN',(0,i),(-1,i)),('BACKGROUND',(0,i),(-1,i),PALE),('LINEABOVE',(0,i),(-1,i),.45,LINE)])
   t.setStyle(TableStyle(cmds))
   records[(signature(self.block,rows),round(w,3))]={'bloco':self.block,'conteudo':rows,'largura':round(w,3),'proporcoes_antes':baseline_fractions(rows),'proporcoes_depois':geo['fractions'],'cabeçalho_de_dados':headerless(self),'coluna_possivel':narrow(self),'modo':'coluna' if w<300 else 'largura inteira','motivo':'Dar largura ao conteúdo, alinhar números e reduzir a decoração; tabela pequena acompanha a coluna.'}
   return t,6,7
  if self.kind=='note':
   key=signature(self.block,self.text);info=note_index.get(key)
   assert info,(self.block,self.text)
   typ=info['tipo'];st=S['note'];left=6;right=0;top=2;bottom=2;before=4;after=5;cmds=[]
   if typ=='exemplo':
    if variant=='linhas':cmds.append(('LINEBEFORE',(0,0),(0,0),.7,GREY))
   elif typ in ['formula','regra-chave']:
    st=ParagraphStyle('note-essential',parent=S['body'],spaceAfter=0);left=8;right=8;top=5;bottom=5;cmds=[('BACKGROUND',(0,0),(-1,-1),PALE),('LINEBEFORE',(0,0),(0,0),1.4,ACC)]
   elif typ in ['ficha de exemplo','recurso digital']:
    left=8;right=8;top=5;bottom=5;cmds=[('BACKGROUND',(0,0),(-1,-1),STRIPE),('LINEABOVE',(0,0),(-1,0),.5,LINE)]
   elif typ=='aviso editorial':
    left=9;right=9;top=8;bottom=8;before=4;after=8;cmds=[('BACKGROUND',(0,0),(-1,-1),PALE),('LINEBEFORE',(0,0),(0,0),2,ACC)]
   t=Table([[Paragraph(inline(self.text,self.doc),st)]],colWidths=[w]);t.setStyle(TableStyle(cmds+[('LEFTPADDING',(0,0),(-1,-1),left),('RIGHTPADDING',(0,0),(-1,-1),right),('TOPPADDING',(0,0),(-1,-1),top),('BOTTOMPADDING',(0,0),(-1,-1),bottom)]))
   note_records[key]={'id':info['id'],'bloco':self.block,'tipo':typ,'texto':self.text,'fonte':st.fontSize,'entrelinha':st.leading,'tratamento':'margem discreta' if typ=='exemplo' and variant=='linhas' else 'texto recuado' if typ=='exemplo' else 'destaque de consulta' if typ in ['formula','regra-chave'] else 'quadro leve' if typ in ['ficha de exemplo','recurso digital'] else 'preservado','motivo':info['motivo']}
   return t,before,after
  return original(self,w)
 Part.make=make
 ns['registros_tabelas']=records;ns['registros_destaques']=note_records
