#!/usr/bin/env python3
"""Lê as fontes congeladas e monta o texto consolidado, com links qualificados.
Uso: python ler_fontes.py. A diagramação é feita por gerar_livro.py.
"""
from pathlib import Path
from collections import Counter
from dataclasses import dataclass
from xml.sax.saxutils import escape
import argparse, hashlib, json, re, unicodedata, math, sys
from reportlab import rl_config
rl_config.invariant = 1
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether, Flowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader
B=Path(__file__).resolve().parent; P=B/'fontes-editoriais'; E=B/'evidencias'; OUT=B/'output/pdf'; E.mkdir(exist_ok=True);OUT.mkdir(parents=True,exist_ok=True)
args=argparse.ArgumentParser();args.add_argument('--strict',action='store_true');args.add_argument('--passes',type=int,default=6);opt=args.parse_args()
sha=lambda b:hashlib.sha256(b).hexdigest()
def save(n,data): (B/n).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def norm(s):return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',s)).strip().casefold()
order=json.loads((B/'ORDEM.json').read_text()); snapshots={k:(P/v).read_text() for k,v in order['fontes'].items()};source_hash={k:sha(t.encode()) for k,t in snapshots.items()}
paths={str(Path(v)):k for k,v in order['fontes'].items()}
@dataclass
class Block:
 doc:str
 anchor:str
 title:str
 text:str
 @property
 def key(self):return self.doc+'--'+self.anchor
blocks={};all_blocks={};link_issues=[]
for doc,text in snapshots.items():
 found=re.findall(r'<!-- page:([^|]+)\|([^>]+) -->\s*(.*?)(?=<!-- page:|\Z)',text,re.S)
 if not found:raise ValueError('Fonte sem blocos '+doc)
 blocks[doc]=[]
 for anchor,title,md in found:
  b=Block(doc,anchor.strip(),title.strip(),md.strip());assert b.key not in all_blocks,b.key
  assert b.text.splitlines()[0]=='# '+b.title,(doc,anchor,b.text[:100]);blocks[doc].append(b);all_blocks[b.key]=b

chapters=[];selection=[];part_rows=[]
for pi,part in enumerate(order['partes'],1):
 part_rows.append({'titulo':part['titulo'],'key':f'parte-{pi}'})
 for ch in part['capitulos']:
  ci=len(chapters)+1;entry={'titulo':ch['titulo'],'key':f'capitulo-{ci}','numero':ci,'parte':pi,'grupos':[]}
  for spec in ch['fontes']:
   doc=spec['documento'];want=spec.get('ancoras');omit=spec.get('excluir',[]);prefix=spec.get('prefixo');omit_prefixes=spec.get('excluir_prefixos',[])
   if want:
    unknown=set(want)-{b.anchor for b in blocks[doc]};assert not unknown,(doc,unknown)
   chosen=[b for b in blocks[doc] if (want is None or b.anchor in want) and b.anchor not in omit and (prefix is None or b.anchor.startswith(prefix)) and not any(b.anchor.startswith(p) for p in omit_prefixes)]
   assert chosen,(ch['titulo'],spec)
   entry['grupos'].append({'doc':doc,'blocks':chosen,'caminho':doc in ['bastiao','vanguarda','guia','emanador','evocador','incursor']})
   selection.extend(b.key for b in chosen)
  chapters.append(entry)
# Ordem já aprovada no piloto: manobras e contenções no final de Combate.
for ch in chapters:
 for group in ch['grupos']:
  if group['doc']=='geral':
   moved=[b for b in group['blocks'] if b.anchor in ['manobras','contencoes']]
   rest=[b for b in group['blocks'] if b not in moved]
   i=next(i for i,b in enumerate(rest) if b.anchor=='movimento')
   rest[i:i]=moved;group['blocks']=rest
selection=[b.key for ch in chapters for g in ch['grupos'] for b in g['blocks']]
count=Counter(selection);assert len(count)==len(all_blocks) and set(count)==set(all_blocks),{'omitidos':list(set(all_blocks)-set(count)),'extras':list(set(count)-set(all_blocks))};assert all(v==1 for v in count.values()),'Blocos repetidos'

# R23 fornece destinos com identidade exata. Não inferir títulos nem usar páginas antigas.
mapfile=P/'consulta/lote-01/evidencias/DESTINOS.json';dest_snapshot=mapfile.read_text();dest_data=json.loads(dest_snapshot)
def destination(d,term):
 file=str(Path(d['arquivo']));doc=paths.get(file);key=(doc+'--'+d['ancora']) if doc else None
 if key not in all_blocks:
  link_issues.append({'origem':'DESTINOS.json','termo':term,'destino':d,'problema':'fonte/âncora não selecionada no livro'});return None
 # A raiz pode alterar títulos, mas identidade de arquivo/âncora é o contrato.
 return key
maps={kind:{row['termo']:{**row,'target':destination(row['destino'],row['termo'])} for row in dest_data.get(kind,[])} for kind in ['glossario','indice']}

def enrich(b):
 lines=b.text.splitlines();out=[]
 for line in lines:
  line=re.sub(r'\[([^\]]+)\]\(#([^)]+)\)',lambda m:'['+m[1]+'](#'+b.doc+'--'+m[2]+')',line)
  for target in re.findall(r'\]\(#([^)]+)\)',line):
   if target not in all_blocks:link_issues.append({'origem':b.key,'destino':target,'problema':'link interno sem bloco'})
  if b.doc=='consulta' and b.anchor.startswith('consulta-glossario-'):
   m=re.match(r'^\*\*(.*?)\.\*\*',line)
   if m:
    row=maps['glossario'].get(m[1])
    if row and row['target']:
     line=re.sub(r'(\*\*Consulta:\*\*\s*)(.*?)(\.)?$',lambda z:z[1]+'['+row['destino']['titulo']+'](#'+row['target']+').',line)
    elif not row:link_issues.append({'origem':b.key,'termo':m[1],'problema':'termo ausente no mapa de glossário'})
  if b.doc=='consulta' and b.anchor.startswith('consulta-indice-') and line.startswith('|'):
   cells=[x.strip() for x in line.strip('|').split('|')]
   if len(cells)==2 and cells[0] not in ['Assunto','---']:
    row=maps['indice'].get(cells[0])
    if row and row['target']:line='| '+cells[0]+' | ['+cells[1]+'](#'+row['target']+') |'
    elif not row:link_issues.append({'origem':b.key,'termo':cells[0],'problema':'termo ausente no mapa de índice'})
  out.append(line)
 return '\n'.join(out)
enriched={k:enrich(b) for k,b in all_blocks.items()};save('evidencias/DESTINOS-PENDENTES.json',link_issues)
# Adendo solicitado pelo autor em 05/10/2026. A fonte remota permanece intacta.
ficha_url='https://docs.google.com/spreadsheets/d/1u0zWQFVaRTTc_VlrAJsabgAiJ1D4rTYhzG7QQWof1ro/edit?gid=20627004#gid=20627004'
ficha_adendo='> **Ficha digital.** [Abrir a ficha do Projeto - M]('+ficha_url+'). Entre em uma conta Google e selecione **Arquivo > Fazer uma cópia** para salvar uma ficha própria no seu Google Drive. Preencha essa cópia com os dados do seu personagem.'
original=enriched['ab--ab-criacao'];segments=original.split('\n\n',2)
enriched['ab--ab-criacao']='\n\n'.join(segments[:2]+[ficha_adendo]+segments[2:])
save('evidencias/ADENDO-FICHA.json',{'pedido':'Link para a ficha digital no capítulo de criação','url':ficha_url,'bloco':'ab--ab-criacao','texto':ficha_adendo,'alteracao_regras':False})
# Limpeza autorizada pelo autor: registros de produção ficam fora da edição de leitura.
publication_changes=[]
def editorial_change(key,before,after,reason):
 assert before in enriched[key], (key,before)
 enriched[key]=enriched[key].replace(before,after,1)
 publication_changes.append({'bloco':key,'antes':before,'depois':after,'motivo':reason,'altera_regras':False})
key='ab--ab-apresentacao'
before=next(l for l in enriched[key].splitlines() if 'As escolhas de adaptação estão reunidas' in l)
editorial_change(key,before,'> Projeto - M é um material de fã baseado em Jujutsu Kaisen, de Gege Akutami.','Crédito breve, sem remissão ao processo editorial.')
removed='consulta--consulta-referencias'
retained='Quando uma campanha incluir personagens ou acontecimentos da obra, combinem a época e o quanto pretendem seguir essa história. O mestre pode usar uma situação original sem exigir que todos conheçam revelações do mangá.'
assert retained in enriched[removed]
enriched['consulta--consulta-conduzir']+='\n\n## História da campanha\n\n'+retained
publication_changes.append({'bloco':removed,'antes':enriched[removed],'depois':'Orientação sobre época e revelações mantida em Mestrar uma sessão. Demais notas transferidas ao relatório.','motivo':'Fontes de revisão e descrição da adaptação não são instruções de jogo.','altera_regras':False})
for ch in chapters:
 for group in ch['grupos']:group['blocks']=[b for b in group['blocks'] if b.key!=removed]
del all_blocks[removed];del enriched[removed]
# R23: modelos em caderno separado; glossário breve e índice por assunto/página.
supplement_blocks=[b for b in all_blocks.values() if b.doc=='consulta' and (b.anchor.startswith('consulta-ficha-') or b.anchor in ['consulta-registro-missao','consulta-entidades'])]
supplement_enriched={b.key:enriched[b.key] for b in supplement_blocks}
for b in supplement_blocks:
 publication_changes.append({'bloco':b.key,'antes':enriched[b.key],'depois':'Mantido integralmente no Caderno de fichas R23.','motivo':'Modelo para preenchimento separado do livro de consulta; nenhuma regra removida.','altera_regras':False})
 for ch in chapters:
  for group in ch['grupos']:group['blocks']=[q for q in group['blocks'] if q.key!=b.key]
 del all_blocks[b.key];del enriched[b.key]
chapters[19]['titulo']='Consulta rápida'
definitions=json.loads((B/'GLOSSARIO-RESUMIDO.json').read_text())
seen_terms=set()
for b in all_blocks.values():
 if b.doc!='consulta':continue
 if b.anchor.startswith('consulta-glossario-'):
  old=enriched[b.key];ls=[old.splitlines()[0],'']
  for term in re.findall(r'^\*\*(.*?)\.\*\*',old,re.M):
   assert term in definitions and maps['glossario'][term]['target'],term
   target=maps['glossario'][term]['target'];seen_terms.add(term)
   ls.extend(['['+term+'](#'+target+'). '+definitions[term],''])
  enriched[b.key]='\n'.join(ls)
  publication_changes.append({'bloco':b.key,'antes':old,'depois':enriched[b.key],'motivo':'Definições breves com o termo clicável. Procedimentos completos permanecem no capítulo indicado.','altera_regras':False})
 elif b.anchor.startswith('consulta-indice-'):
  old=enriched[b.key];ls=[old.splitlines()[0],'']
  for line in old.splitlines()[1:]:
   if not line.startswith('|') or re.fullmatch(r'[\s|:\-]+',line):continue
   cells=[v.strip() for v in line.strip('|').split('|')]
   if cells[0]=='Assunto':continue
   term=cells[0];target=maps['indice'][term]['target'];assert target,term
   ls.append('['+term+'](#'+target+')')
  enriched[b.key]='\n'.join(ls)
  publication_changes.append({'bloco':b.key,'antes':old,'depois':enriched[b.key],'motivo':'Mesmo assunto e destino. Página clicável substitui o nome extenso da seção.','altera_regras':False})
assert seen_terms==set(definitions),(seen_terms^set(definitions))
# R27: nome oficial solicitado pelo autor, sem mudança das fontes congeladas.
from identidade import nome_oficial
for collection in [enriched,supplement_enriched]:
 for key,old in list(collection.items()):
  revised=nome_oficial(old)
  if revised!=old:
   collection[key]=revised
   publication_changes.append({'bloco':key,'antes':old,'depois':revised,'motivo':'Nome oficial do sistema alterado para Ciclo Maldito pelo autor.','altera_regras':False})
for block in list(all_blocks.values())+supplement_blocks:block.title=nome_oficial(block.title)

# R29: revisão textual autorizada; alterações exatas e rastreáveis.
from revisao_textual import aplicar
textual_changes=aplicar(enriched)
publication_changes.extend(textual_changes)
# R32: alterações de regra e compreensão autorizadas em 08/10/2026.
from revisao_r32 import aplicar as aplicar_r32
r32_changes=aplicar_r32(enriched)
publication_changes.extend(r32_changes)
# R36: duas respostas do autor durante o pente fino da R35.
from revisao_r36 import aplicar as aplicar_r36
r36_changes=aplicar_r36(enriched)
publication_changes.extend(r36_changes)
for key,block in all_blocks.items():
 first=enriched[key].splitlines()[0]
 if first.startswith('# '):block.title=first[2:]

# R31: camada de estrutura aplicada depois das 73 revisões da R29.
# As fontes e os registros mecânicos da R30 permanecem preservados.
base_before_structure=dict(enriched)
from estrutura_editorial import aplicar as estruturar
structural_changes,hierarquia=estruturar(enriched,all_blocks,chapters)
from revisao_r37 import aplicar as aplicar_r37
r37_changes=aplicar_r37(enriched,all_blocks,chapters,hierarquia)
publication_changes.extend(r37_changes)
from revisao_r38 import aplicar as aplicar_r38
publication_changes.extend(aplicar_r38(enriched,hierarquia))
from revisao_r39 import aplicar as aplicar_r39
publication_changes.extend(aplicar_r39(enriched))
from revisao_r40 import aplicar as aplicar_r40
publication_changes.extend(aplicar_r40(enriched,all_blocks,chapters,hierarquia))
from revisao_r41 import aplicar as aplicar_r41
publication_changes.extend(aplicar_r41(enriched,hierarquia))
for key,block in all_blocks.items():
 first=enriched[key].splitlines()[0] if enriched[key].splitlines() else ''
 if re.match(r'^#{1,6} ',first):block.title=re.sub(r'^#{1,6} ','',first)

# A folha digital continua no capítulo de criação; o caderno acompanha o pacote do livro.

save('evidencias/ALTERACOES-EDITORIAIS.json',publication_changes)

if opt.strict and link_issues:raise ValueError(f'{len(link_issues)} destinos pendentes; consulte evidências')
(E/'fontes-capturadas').mkdir(exist_ok=True)
for key,text in snapshots.items(): (E/'fontes-capturadas'/f'{key}.md').write_text(text)

# Fonte única derivada: texto integral e destinos qualificados. Apenas hierarquia e remissões mudam.
md=['# Ciclo Maldito','', 'Livro de regras','']
map_chapter={};suppressed=[]
for ch in chapters:
 if ch['key']==next(c['key'] for c in chapters if c['parte']==ch['parte']):md.extend([f"<!-- parte:{ch['parte']} -->",f"# Parte {ch['parte']} — {part_rows[ch['parte']-1]['titulo']}",''])
 md.extend([f"<a id=\"{ch['key']}\"></a>",f"## {ch['numero']}. {ch['titulo']}",''])
 for gi,group in enumerate(ch['grupos']):
  for bi,b in enumerate(group['blocks']):
   map_chapter[b.key]={'parte':ch['parte'],'capitulo':ch['numero'],'titulo_capitulo':ch['titulo'],'fonte':order['fontes'][b.doc],'ancora_fonte':b.anchor,'titulo_bloco':b.title}
   md.extend([f'<!-- fonte:{order["fontes"][b.doc]}#{b.anchor} -->',f'<a id="{b.key}"></a>'])
   text=enriched[b.key]
   duplicate=(gi==0 and bi==0 and norm(b.title)==norm(ch['titulo']))
   if duplicate:suppressed.append(b.key);text='\n'.join(text.splitlines()[1:]).lstrip()
   text=re.sub(r'^(#{1,6}) ',lambda m:'#'*(len(m[1])+2)+' ',text,flags=re.M)
   md.extend([text,''])
(B/'LIVRO-COMPLETO.md').write_text('\n'.join(md)+'\n')
