from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json,hashlib,shutil,re,difflib
P=Path(__file__).resolve().parents[2]
R=Path('/home/mizuki/JJK-v0.341-para-subir')
L=R/'sistema/05-material/livro';B=L/'ciclo-maldito-r41';E=B/'revisao-de-regras/editorial-r66';S=P/'revisao/etapa06';E.mkdir(parents=True,exist_ok=True)
def read(p):return json.loads(p.read_text())
def dump(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def copy(a,b):b.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(a,b)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def edit(p,a,b):
 t=p.read_text();assert t.count(a)==1,(str(p),a,t.count(a));p.write_text(t.replace(a,b,1))
state=read(S/'ESTADO.json');assert state['resultado']=='aprovado'
for f in state['pdfs']:assert sha(Path(f['arquivo']))==f['sha256']
old=(B/'LIVRO-COMPLETO.md').read_text();new=(P/'LIVRO-CANDIDATA.md').read_text()
assert old==(B/'revisao-de-regras/editorial-r65/LIVRO-COMPLETO-R65.md').read_text()
snap=read(B/'revisao-de-regras/editorial-r65/BLOCOS-R65.json');ops=[]
aa=old.splitlines(True);bb=new.splitlines(True)
for tag,i,j,k,l in difflib.SequenceMatcher(None,aa,bb,autojunk=False).get_opcodes():
 if tag=='equal':continue
 before=''.join(aa[i:j]).rstrip('\n');after=''.join(bb[k:l]).rstrip('\n')
 key=re.findall(r'<a id="([a-z0-9]+--[^"]+)"></a>',''.join(aa[:i]))[-1]
 assert before and old.count(before)==1 and snap[key].count(before)==1,key
 kind='frequência aprovada por cena' if 'combate' in before and 'cena' in after else ('atualização da ficha digital' if 'spreadsheets' in before else 'clareza e navegação')
 ops.append({'id':f'R66-{len(ops)+1:02}','bloco':key,'antes':before,'depois':after,'motivo':kind})
 snap[key]=snap[key].replace(before,after,1)
replay=old
for op in ops:replay=replay.replace(op['antes'],op['depois'],1)
assert replay==new
(B/'LIVRO-COMPLETO.md').write_text(new);(E/'LIVRO-COMPLETO-R66.md').write_text(new)
dump(E/'BLOCOS-R66.json',snap);dump(B/'revisao-de-regras/alteracoes/R65-para-R66.json',ops)
dump(E/'FONTE-PUBLICADA.json',{'revisao':'R66','sha256_texto':sha(B/'LIVRO-COMPLETO.md'),'blocos':len(snap),'registros':len(ops),'composicao_local':str(P/'composicao'),'tipo':'Clareza, composição e navegação; frequência por cena aprovada pelo autor.'})
for file in ['ESTADO.json','ALTERACOES.json','APONTAMENTOS-FINAIS.json','REVISAO-TEXTUAL.json','REVISAO-VISUAL.json','VALIDACAO-GERAL.json','CONFERENCIA-ETAPA.json','RELATORIO-FINAL.html']:
 copy(S/file,E/'fechamento'/file)
for n in range(1,7):
 for f in (P/f'revisao/etapa{n:02}').glob('*.json'):copy(f,E/f'etapa{n:02}'/f.name)
for f in ['PLANEJAMENTO-CORRECOES-R65.json','RESULTADO-ANALISE.json']:copy(P/'revisao/analise-total'/f,E/'planejamento'/f)
for f in ['conferir.py','DESTINOS-INDICE-REVISAO.json']:copy(P/f,E/f)
for f in (P/'composicao').glob('*.py'):copy(f,E/'composicao'/f.name)
for f in ['FONTES-E-VALIDACAO.json','GEOMETRIA-CANDIDATA.json']:copy(P/'composicao'/f,E/'composicao'/f)
for f in ['NAVEGACAO.json','SUMARIO-PAGINADO.json']:copy(P/'composicao/revisao-r45'/f,E/'composicao/revisao-r45'/f)
meta=read(L/'EDICAO-ATUAL.json');assert meta['revisao']=='R65'
meta.update(revisao='R66',paginas=422,revisado_em=datetime.now(ZoneInfo('America/Sao_Paulo')).isoformat())
for pal,src in zip(['claro','noturno'],state['pdfs']):
 copy(Path(src['arquivo']),L/meta[pal]['arquivo']);meta[pal]['sha256']=sha(L/meta[pal]['arquivo'])
dump(L/'EDICAO-ATUAL.json',meta)
dump(L/'REVISAO-R66.json',{'revisao':'R66','base':'R65','resultado':'aprovado','paginas':422,'blocos_alterados':sorted(set(o['bloco'] for o in ops)),'trocas':len(ops),'descricao':'Fechamento de seis etapas de revisão: 18 apontamentos e ficha de Bancada; link da ficha atualizado.','conferencia_pdf':read(S/'VALIDACAO-GERAL.json'),'conferencia_final':read(S/'CONFERENCIA-ETAPA.json'),'revisao_visual':read(S/'REVISAO-VISUAL.json'),'sha256':{**{k:meta[k]['sha256'] for k in ['claro','noturno']},'texto':sha(B/'LIVRO-COMPLETO.md')}})
p=R/'conferir-repositorio.py';t=p.read_text();start=t.index("bloco('12. FONTE R65");end=t.index('# ----',start);part=t[start:end].replace('R65','R66').replace("'editorial-r65'","'editorial-r66'").replace('range(54, 66)','range(54, 67)');t=t[:start]+part+t[end:];assert "'EDICAO-ATUAL.json', 'REVISAO-R65.json')" in t;p.write_text(t.replace("'EDICAO-ATUAL.json', 'REVISAO-R65.json')","'EDICAO-ATUAL.json', 'REVISAO-R66.json')"))
for name in ['editorial-r57','fundamento-r53']:
 edit(B/f'revisao-de-regras/{name}/testar-integridade.py',"bloco('12. FONTE R65","bloco('12. FONTE R66")
edit(B/'revisao-de-regras/editorial-r57/testar-integridade.py','R64-para-R65.json','R65-para-R66.json')
edit(B/'revisao-de-regras/fundamento-r53/testar-integridade.py','fonte corrente R65','fonte corrente R66')
edit(R/'sistema/03-mecanica/conferir-fundamento.py','editorial-r65/BLOCOS-R65.json','editorial-r66/BLOCOS-R66.json')
edit(R/'sistema/03-mecanica/livro.py','edição atual, R65','edição atual, R66')
edit(R/'README.md','**Versão v0.375**','**Versão v0.376**')
edit(R/'README.md','[Ciclo Maldito R65, livro completo com 425 páginas]','[Ciclo Maldito R66, livro completo com 422 páginas]')
p=R/'README.md';t=p.read_text();pos=t.index('\n---\n');t=t[:pos]+'\nA R66 reúne a revisão de clareza e diagramação em seis etapas. Os 18 apontamentos e a ficha de Bancada foram resolvidos; os PDFs passam a 422 páginas. A frequência das cinco habilidades foi padronizada por cena, conforme aprovação do autor, e o link da ficha digital foi atualizado. Registros em sistema/05-material/livro/ciclo-maldito-r41/revisao-de-regras/editorial-r66/.\n'+t[pos:];p.write_text(t)
edit(R/'sistema/LEIA-ME.md','**v0.375.**','**v0.376.**');edit(R/'sistema/LEIA-ME.md','O livro atual é a R65','O livro atual é a R66')
p=B/'LEIA-ME.md';tail=p.read_text().split('## Histórico da fonte e da geração',1)[1];p.write_text('# Fonte corrente R66\n\nLIVRO-COMPLETO.md é a edição R66 de 422 páginas usada pelos validadores. Reúne a revisão de clareza, diagramação, navegação e frequência por cena aprovada pelo autor.\n\nO snapshot e a impressão digital ficam em revisao-de-regras/editorial-r66/. O antes e depois está em revisao-de-regras/alteracoes/R65-para-R66.json. Os PDFs ficam na pasta acima, com hashes em EDICAO-ATUAL.json.\n\nA composição local atual está em '+str(P/'composicao')+'. Os scripts e as evidências estão preservados em editorial-r66/composicao e nas pastas de etapa.\n\n## Histórico da fonte e da geração'+tail)
summary='A R66 conclui seis etapas de revisão. São 422 páginas em cada paleta, 18 apontamentos resolvidos e um ajuste adicional na ficha de Bancada. O fechamento passou em 65 verificações gerais e 13 específicas. O texto das duas paletas é idêntico. Inclui o novo link da ficha digital e o limite por cena aprovado nas cinco habilidades e na explicação da dupla.'
p=R/'sistema/ESTADO-ATUAL.md';t=p.read_text().replace('# Edição corrente R65\n\n**Versão v0.375.**','# Edição anterior R65\n\n*Versão v0.375.*',1);p.write_text('# Edição corrente R66\n\n**Versão v0.376.**\n\n'+summary+'\n\nFonte, registros e validações em 05-material/livro/ciclo-maldito-r41/revisao-de-regras/editorial-r66/. A cadeia de integridade cobre R52 a R66. Publicação em preparação.\n\n'+t)
p=R/'logs/CHANGELOG.md';t=p.read_text();mark='## [0.375] - 04/11/2026';assert t.count(mark)==1;t=t.replace(mark,'## [0.376] - 04/11/2026\n\n### Alterado\n\n- '+summary+'\n- Registros de texto, composição e validação preservados em editorial-r66. A R65 permanece no histórico.\n\n'+mark,1);p.write_text(t)
p=R/'finalizado/README.md';oldline=p.read_text().splitlines()[4];assert 'Livro atual: Ciclo Maldito R65' in oldline;newl=oldline.replace('R65','R66').replace('0.375','0.376').replace('425 páginas','422 páginas').replace('que simplifica a redação de Caminhos e Trilhas.','com clareza, diagramação, navegação e frequência por cena revisadas.');edit(p,oldline,newl)
for name in [meta['claro']['arquivo'],meta['noturno']['arquivo'],'EDICAO-ATUAL.json','REVISAO-R66.json']:copy(L/name,R/'finalizado/livro'/name)
copy(Path(__file__),E/'integrar_r66.py')
dump(P/'revisao/publicacao-r66/INTEGRACAO.json',{'estado':'integrada localmente','trocas':len(ops),'blocos':len(set(o['bloco'] for o in ops)),'pdfs':state['pdfs']})
print('Integrada R66:',len(ops),'trocas em',len(set(o['bloco'] for o in ops)),'blocos.')

