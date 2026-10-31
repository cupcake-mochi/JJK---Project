import json,re
from pathlib import Path
B=Path(__file__).resolve().parents[1];R=B/'revisao-r40';texts=json.loads((R/'TEXTOS-PROPOSTOS.json').read_text())
old=json.loads((B/'ORDEM.json').read_text());chapters=[c for p in old['partes'] for c in p['capitulos']]
specs={
1:'ab--ab-primeira-sessao ab--ab-mundo ab--ab-sociedade',
2:'geral--atributos geral--testes geral--turnos geral--acoes geral--ataques geral--defesa geral--bloquear geral--manobras geral--movimento geral--carga geral--perceber geral--esconder geral--mundo',
3:'dano--dano dano--tipos dano--condicoes dano--cura dano--zero dano--descansos dano--exaustao',
4:'ab--ab-origem ab--ab-caminho ab--ab-capacidades ab--ab-equipamento ab--ab-conferencia',
5:'origens--legados origens--origem-latente origens--origem-receptaculo origens--origem-descendente origens--origem-encarnado origens--origem-feto origens--origem-sem-tecnica origens--origem-corpo origens--origem-restricao',
7:'pericias--tarefas pericias--fisicas pericias--conhecimento pericias--ambiente pericias--essencia pericias--oficios pericias--fabricacao pericias--reparos',
8:'equip--eqp-protecao equip--eqm-municao equip--eqa-armas equip--eqi-itens equip--eqc-dinheiro equip--eqc-inicial equip--eqf-equipamento',
9:'progressao--prog-xp progressao--prog-tabela-inicial progressao--prog-tabela-avancada progressao--prog-marcos progressao--prog-trilhas progressao--prog-patentes',
10:'fundamento--tecnica fundamento--primeiro fundamento--familias fundamento--repertorio fundamento--pontos fundamento--formas fundamento--combinacoes fundamento--danolimites fundamento--classezero fundamento--liberacao fundamento--maxima',
11:'catalogo--cat-alcance catalogo--cat-area catalogo--cat-mira catalogo--cat-controle catalogo--cat-auxiliares catalogo--cat-castigo catalogo--cat-tempo catalogo--cat-marca catalogo--cat-amparo catalogo--cat-proprio catalogo--cat-restricoes-conjuracao catalogo--cat-passivas-1 catalogo--cat-passivas-2-recursos catalogo--cat-passivas-3',
12:'aptidoes--apt-marcos aptidoes--apt-catalogo aptidoes--apt-protecao-dominios',
13:'rotas--rota-marcial rotas--rota-sem-tecnica rotas--rota-lapidacao rotas--rota-bencaos',
14:'poderes--degraus poderes--criardominio poderes--acerto poderes--sembarreiras poderes--disputa poderes--multiplos',
15:'ritual--ritual ritual--pactos',
16:'campo--inv-ciclo campo--inv-especial campo--inv-talisma campo--inv-corpos campo--inv-liberacao campo--inv-queda',
17:'construcao--entidades-criar construcao--entidades-aquisicao construcao--entidades-basicas construcao--entidades-especiais construcao--entidades-passivas fabricacao--fab-entidades',
18:'consulta--consulta-missao consulta--consulta-conduzir'}
rows=[]
for n,keys in specs.items():
 for k in keys.split():
  title=re.sub(r'^#+ ','',texts[k].splitlines()[0]).strip('*');rows.append({'capitulo':n,'destino':k,'titulo':title,'nivel':2})
# Caminhos e suas Trilhas, com rotas de Batedor um nível abaixo.
cs={
'bastiao':['bas-bastiao','bas-muro','bas-punho','bas-combatente'],
'vanguarda':['van-base','van-estocada','van-yumi','van-besta','van-fogo','van-executor'],
'guia':['guia','guia-arquiteto','guia-analista','guia-socorrista'],
'emanador':['ema-base','ema-condutor','ema-eco','ema-impulso'],
'evocador':['evocador','ev-principal','ev-parceria','ev-multiplas'],
'incursor':['inc-caminho','inc-assassino','inc-pugilista','inc-malabarista']}
for doc,anchors in cs.items():
 for i,a in enumerate(anchors):
  k=doc+'--'+a;rows.append({'capitulo':6,'destino':k,'titulo':texts[k].splitlines()[0].lstrip('# '),'nivel':2 if i==0 else 4 if a in ['van-besta','van-fogo'] else 3})
  if a=='van-yumi':rows.append({'capitulo':6,'destino':'r40-nav-yumi','bloco':k,'cabecalho':'Batedor: Yumi','titulo':'Batedor: Yumi','nivel':4})
# Indicar ramos da Restrição sem inventar um capítulo independente.
ix=next(i for i,r in enumerate(rows) if r['destino']=='origens--origem-restricao')
rows[ix+1:ix+1]=[
 {'capitulo':5,'destino':'r40-nav-restricao-corpo','bloco':'origens--origem-restricao','cabecalho':'Corpo pela Técnica','titulo':'Corpo pela Técnica','nivel':3},
 {'capitulo':5,'destino':'r40-nav-restricao-sem-energia','bloco':'origens--origem-restricao','cabecalho':'Sem Energia','titulo':'Sem Energia','nivel':3}]
for r in rows:
 if r['destino']=='origens--origem-sem-tecnica':r['titulo']='Sem Técnica (Origem)'
 if r['destino']=='rotas--rota-sem-tecnica':r['titulo']='Sem Técnica: criação de Manejos'
 if r['destino']=='rotas--rota-marcial':r['titulo']='Técnica Marcial: criação de Katas'
rows.sort(key=lambda r:r['capitulo'])
(R/'NAVEGACAO.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(len(rows),'seções além dos 21 capítulos')
