from pathlib import Path
from fractions import Fraction as F
import hashlib,json,re
from urllib.parse import unquote
H=Path(__file__).resolve().parent;R=H.parent.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
initial=json.loads((H/'estado-inicial.json').read_text(encoding='utf-8'))
changed=[p for p in initial['snapshot'] if not p.endswith('manifesto-entrega.json')]
new=['04 - Planejamento/67-perigo-da-passarela-e-do-guincho.md','06 - Redacao do Guia/64-a-passarela-e-o-guincho.md']
errors=[];preserved=0
for p,expected in initial['manifesto_inicial'].items():
 if p in changed:continue
 if not (R/p).is_file() or sha(R/p)!=expected:errors.append(p)
 else:preserved+=1
assert not errors,errors
assert all(sha(H/'historico/antes-do-perigo'/p)==expected for p,expected in initial['snapshot'].items())
r53=R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
assert sha(r53)==initial['r53_sha256']=='7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
cases=[]
def check(name,actual,expected):
 assert actual==expected,(name,actual,expected)
 cases.append({'caso':name,'resultado':actual})
check('superior',3+3+3,9)
check('inferior físico',3+6+9+6+3,27)
check('inferior movimento',3+6*2+9+6*2+3,39)
check('primeiro turno por três ações',9*3,27)
check('segundo turno preserva Padrão',39-27<=9*2,True)
check('primeiro turno com Padrão na parada não completa inferior',9*2<39,True)
check('intervalo ficcional de três rodadas',3*6,18)
def run(actions,rounds=5):
 active=False;marker=0;broken=False;events=[];motor=False;coupled=True
 for rnd in range(1,rounds+1):
  for action in actions.get(rnd,[]):
   if action=='start':active=True;motor=True
   elif action=='stop':active=False;motor=False
   elif action=='pin':coupled=False;active=False
  if active and coupled and not broken:
   marker+=1
   if marker==3:broken=True;events.append(rnd)
 return {'marcador':marker,'rupturas':events,'motor':motor,'transmissao':coupled}
check('sem ativação',run({}),{'marcador':0,'rupturas':[],'motor':False,'transmissao':True})
check('parada na rodada1 antes da fase',run({1:['start','stop']})['marcador'],0)
check('parada na rodada2',run({1:['start'],2:['stop']})['marcador'],1)
check('parada rodada3 ainda impede',run({1:['start'],3:['stop']})['rupturas'],[])
check('sem parada só uma ruptura',run({1:['start']})['rupturas'],[3])
check('parada depois conserva ruptura',run({1:['start'],4:['stop']})['rupturas'],[3])
check('pino deixa motor desacoplado',run({1:['start'],2:['pin']}),{'marcador':1,'rupturas':[],'motor':True,'transmissao':False})
check('dano acumulado na peça',max(0,5-2-3),0)
check('dano insuficiente conserva peça',max(0,5-4),1)
check('queda6m',min(20,6//3),2)
check('7,5m tem os mesmos dados',min(20,F('7.5')//3),2)
check('impacto ilustrativo',3+4,7)
check('vida após dano',max(0,10-7),3)
check('zero não é saldo negativo',max(0,5-7),0)
def jump(force,impulse):
 n=F(3)+F('1.5')*force
 return n if impulse else (n/2//F('1.5'))*F('1.5')
check('Força0 com impulso',float(jump(0,True)),3.0)
check('Força1 sem impulso',float(jump(1,False)),1.5)
check('Força2 sem impulso',float(jump(2,False)),3.0)
check('extensão do salto parado de Força1',float(jump(1,False)+F('1.5')),3.0)
check('impulso e salto pagos',3+3,6)
source=r53.read_text(encoding='utf-8')
titles=['#### Saltos','#### Quedas e movimento imposto','### Danificar objetos','### Objetos e efeitos','#### Preparar','#### Estudar','#### Arrastar e transportar']
evidence=[]
for title in titles:
 pos=source.index(title)
 evidence.append({'titulo':title,'linha':source[:pos].count('\n')+1})
links=0;historical=0;broken=[]
for rel in changed+new:
 p=R/rel
 for m in re.finditer(r'\]\((<[^>]+>|[^)]+)\)',p.read_text(encoding='utf-8')):
  target=m.group(1).strip('<>')
  if re.match(r'^[a-zA-Z][\w+.-]*:',target) or target.startswith('#'):continue
  target=unquote(target.split('#')[0])
  if target.startswith(('/home/','/media/')):historical+=1;continue
  if not target:continue
  if target.endswith('apoio-perigo/verificacao.json'):continue
  links+=1
  if not (p.parent/target).resolve().exists():broken.append({'arquivo':rel,'destino':target})
assert not broken,broken
save(H/'resultados.json',{'tipo':'contas e sequências determinísticas, sem simulação de grupo','casos':cases,'trechos_conferidos':evidence})
save(H/'verificacao.json',{'data':'2026-10-23','entrega':'P67/G64','r53_sha256':sha(r53),'manifesto_inicial_integro':len(initial['manifesto_inicial']),'arquivos_anteriores_preservados':preserved,'alterados':changed,'novos':new,'historico_preservado':True,'casos_conferidos':len(cases),'links_locais_conferidos':links,'links_quebrados':broken,'remissoes_linux_historicas':historical,'conferencia_documental':['ações e conversões','saltos e quedas','objeto com dano acumulado','momento de Preparar','rotas e apoios','zero/atendimento/encerramento'],'propostas_locais':['cronograma de três rodadas','dispositivo e freio','geografia e operação da parada'],'teste_humano':False,'simulacao_integral':False,'equilibrio_validado':False,'publicado_no_github':False})
manifest=dict(initial['manifesto_inicial'])
for p in changed+new:manifest[p]=sha(R/p)
for p in H.rglob('*'):
 if p.is_file() and 'historico' not in p.relative_to(H).parts and '__pycache__' not in p.parts:manifest[p.relative_to(R).as_posix()]=sha(p)
mp=R/'04 - Planejamento/apoio-piloto/manifesto-entrega.json';save(mp,manifest)
assert all(sha(R/p)==v for p,v in json.loads(mp.read_text(encoding='utf-8')).items())
print(json.dumps({'casos':len(cases),'links':links,'manifesto_final':len(manifest),'originais_preservados':preserved,'links_quebrados':broken,'sessao_humana':False},ensure_ascii=False))
