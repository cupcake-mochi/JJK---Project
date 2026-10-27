"""Casos determinísticos e integridade da entrega; não é simulador de combate."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, re
from urllib.parse import unquote

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
def read(p): return p.read_text(encoding='utf-8-sig')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,value): p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
initial=json.loads(read(HERE/'estado-inicial.json'))
data=json.loads(read(HERE/'dados-encontro.json'))
r53=HERE/'fontes/LIVRO-COMPLETO-R53.md'
assert sha(r53)=='7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
cases=[]
def check(name,actual,expected):
    assert actual==expected, (name,actual,expected)
    cases.append({'caso':name,'resultado':actual,'esperado':expected})
def volume(massa,itens=0,proprio=0): return F(str(massa))/12+F(str(itens))+F(str(proprio))
def edges(route,drag):
    result=[]
    for section in data['rotas'][route]:
        cost=(F(3) if drag else F('1.5'))+(F('1.5') if section['terreno']=='dificil' else 0)
        result.extend([cost]*int(F(section['metros'])/F('1.5')))
    return result
def advance(costs,budget,start=0):
    i=start; spent=F(0)
    while i<len(costs) and spent+costs[i]<=budget:
        spent+=costs[i]; i+=1
    return {'indice':i,'avanco':float(F(i-start)*F('1.5')),'gasto':float(spent),'sobra':float(budget-spent)}
def destroyed(hp,maxhp,damage,area=False):
    return not area and (damage>=maxhp or max(0,damage-hp)>F(maxhp,2))
enemy=data['inimigo']; a=enemy['atributos']; dom=data['domada']
check('soma de atributos',sum(a.values()),9)
check('CD por Força e Maestria',8+a['forca']+enemy['maestria'],enemy['cd_agarrar'])
check('TR igual resiste',[11>=12,12>=12],[False,True])
check('Integridade do inimigo',enemy['vida']//2,enemy['integridade'])
check('limite normal',5+a['forca'],8)
check('teto de arrasto',2*(5+a['forca']),16)
check('corpo e itens',float(volume(72,2)),8.0)
check('limites sem arredondar',[F(16)<=16,F('16.1')<=16,F(8)<=8,F('8.1')<=8],[True,False,True,False])
check('equipamento próprio reduz teto de arrasto',float(16-F(1)),15.0)
check('carga do socorrista',float(volume(72,2,1)),9.0)
check('socorrista com excesso permitido',7<volume(72,2,1)<=14,True)
check('rota direta andando',float(sum(edges('direta',False))),24.0)
check('rota direta arrastando',float(sum(edges('direta',True))),42.0)
check('rota lateral andando',float(sum(edges('lateral',False))),24.0)
check('rota lateral arrastando',float(sum(edges('lateral',True))),48.0)
first=advance(edges('direta',True),F(18))
check('turno de Agarrar com Bônus convertida',first,{'indice':5,'avanco':7.5,'gasto':16.5,'sobra':1.5})
second=advance(edges('direta',True),F(27),first['indice'])
check('turno seguinte com Correr',second,{'indice':12,'avanco':10.5,'gasto':25.5,'sobra':1.5})
safe=advance(edges('direta',True),F(18),first['indice'])
check('Desengajar não chega no segundo turno',safe['indice']<12,True)
check('restante após primeiro turno',float(sum(edges('direta',True)[5:])),25.5)
check('estágio2 com dois movimentos',advance(edges('direta',True),F(9)),{'indice':3,'avanco':4.5,'gasto':9.0,'sobra':0.0})
stages={}
for current in range(17):
    lost=F(16-current,16)
    stages[str(current)]=max(i for i,threshold in enumerate([0,F(1,4),F(1,2),F(3,4),1]) if lost>=threshold)
check('fronteiras Integridade',[stages[str(x)] for x in (16,13,12,9,8,5,4,1,0)],[0,0,1,1,2,2,3,3,4])
check('vida convertida',5+a['constituicao']+(3+a['constituicao'])*(dom['nivel']-1),14)
check('Integridade convertida',dom['vida']//2,7)
check('perícias da entidade',4+a['inteligencia']//2,4)
check('vagas de especial',int(F(2+F(dom['nivel'],2),2)),1)
check('Defesa com Essência2',10+a['destreza']+2//2,12)
check('domada sem técnica não ganha reserva',not dom['tecnica_propria'] and dom['reserva_propria']==0,True)
check('retorno e cura de vida',dom['vida']//2,7)
check('domada arrasto normal',advance([F(3)]*12,F(9))['avanco'],4.5)
check('domada arrasto difícil',advance([F('4.5')]*12,F(9))['avanco'],3.0)
check('domada Correr sem novo Agarrar',advance([F(3)]*12,F(18))['avanco'],9.0)
for damage,expected in [(21,False),(22,True),(32,True)]:
    check(f'destruição direta a5PV por{damage}',destroyed(5,32,damage),expected)
    check(f'área a5PV por{damage} não destrói',destroyed(5,32,damage,True),False)
check('empurrão depende de separação',[F('1.5')>F('1.5'),F(3)>F('1.5')],[False,True])

newdocs=['04 - Planejamento/66-encontro-do-carregador-de-sinos.md','06 - Redacao do Guia/62-o-carregador-e-o-corredor-de-entulho.md','06 - Redacao do Guia/63-carregador-consulta-e-doma.md']
changed=[r for r in initial['snapshot'] if not r.endswith('manifesto-entrega.json')]
allowed=set(changed)
unexpected=[]; preserved=0
for rel,expected in initial['protegidos'].items():
    if rel in allowed: continue
    if not (ROOT/rel).is_file() or sha(ROOT/rel)!=expected: unexpected.append(rel)
    else: preserved+=1
assert not unexpected,unexpected
for rel,expected in initial['snapshot'].items():
    assert sha(HERE/'historico/antes-do-encontro'/rel)==expected,rel

source=read(r53)
anchors={m.group(1) for m in re.finditer(r'<a id="([^"]+)"',source)}
cited=set(re.findall(r'`((?:geral|dano|construcao|campo)--[^`]+)`',read(ROOT/newdocs[0])))
missing=sorted(cited-anchors)
assert not missing,missing
headings=['#### Agarrar, derrubar e empurrar','#### Escapar de uma contenção','#### Carga','#### Arrastar e transportar','### Fechaduras e contenção','#### Domar uma maldição','### Carga e equipamento','#### Características próprias','##### Leitura de Reservas']
source_evidence=[]
for title in headings:
    pos=source.index(title)
    end=source.find('\n<!-- fonte:',pos+1)
    if end<0: end=min(pos+4000,len(source))
    block=source[pos:end]
    source_evidence.append({'titulo':title,'linha':source[:pos].count('\n')+1,'sha256_trecho':hashlib.sha256(block.encode('utf-8')).hexdigest()})

# Não reclassifica remissões Linux antigas como novos links quebrados.
links=[]; historical=[]; bad=[]
for rel in changed+newdocs:
    p=ROOT/rel
    for match in re.finditer(r'\]\((<[^>]+>|[^)]+)\)',read(p)):
        target=match.group(1).strip('<>')
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('#'): continue
        path=unquote(target.split('#')[0])
        if path.startswith('/home/') or path.startswith('/media/'):
            historical.append({'arquivo':rel,'destino':path}); continue
        if not path: continue
        resolved=(p.parent/path).resolve()
        if not resolved.exists(): bad.append({'arquivo':rel,'destino':path})
        links.append({'arquivo':rel,'destino':target})
# O relatório de verificação é produzido abaixo; remissões a ele são válidas por construção.
bad=[x for x in bad if not x['destino'].endswith('apoio-carregador/verificacao.json')]
assert not bad,bad
g62=read(ROOT/newdocs[1]); g63=read(ROOT/newdocs[2])
for text,label in [(g62,'encontro'),(g63,'consulta')]:
    assert 'experimental' in text.lower(),label
    assert 'Doma' in text,label
    assert any(term in text.lower() for term in ('teste humano','pessoas reais','sessão humana')),label
assert '**32/32 PV**' in g63 and '**16/16**' in g63 and '**14 / 7**' in g63
assert '**25,5 m**' in g62 and '**42 m**' in g62
assert '16,1' in g62 and '8,1' in g63
result={'tipo':'casos determinísticos; não combate simulado','casos':cases,'integridade_por_saldo':stages,'fontes_primarias':source_evidence,'ancoras_conferidas':sorted(cited)}
save(HERE/'resultados.json',result)
report={'data':'2026-10-23','entrega':'P66/G62/G63','fonte_r53_sha256':sha(r53),'casos_automaticos':len(cases),'links_locais_conferidos':len(links),'links_quebrados':bad,'remissoes_linux_historicas_nao_resolvidas_neste_windows':len(historical),'ancoras_r53_conferidas':len(cited),'arquivos_anteriores_preservados':preserved,'alterados':changed,'novos':newdocs,'snapshot_conferido':True,'registro_decisoes_preservado':sha(ROOT/'04 - Planejamento/06-registro-das-decisoes.md')==initial['protegidos']['04 - Planejamento/06-registro-das-decisoes.md'],'base_piloto_preservada':sha(ROOT/'04 - Planejamento/apoio-piloto/base-inimigos.json')==initial['protegidos']['04 - Planejamento/apoio-piloto/base-inimigos.json'],'revisao_documental':['ações e conversões','contenção e saídas','carga e trajeto dos dois corpos','informação e negociação delimitadas','amarras e transporte de feridos','zero/participação/socorro/encerramento','Doma e proposta explícita do talento'],'simulacao_combate':False,'teste_humano':False,'equilibrio_validado':False,'publicado_no_github':False,'limites':'A referência numérica e o talento de Doma continuam experimentais. Remissões absolutas Linux antigas conservam destino histórico; a base original do conceito não foi recuperada nesta etapa.'}
save(HERE/'verificacao.json',report)
manifest_path=ROOT/'04 - Planejamento/apoio-piloto/manifesto-entrega.json'
manifest=json.loads(read(HERE/'historico/antes-do-encontro/04 - Planejamento/apoio-piloto/manifesto-entrega.json'))
for rel in changed+newdocs: manifest[rel]=sha(ROOT/rel)
for p in HERE.rglob('*'):
    if p.is_file() and 'historico' not in p.relative_to(HERE).parts and '__pycache__' not in p.parts:
        manifest[p.relative_to(ROOT).as_posix()]=sha(p)
save(manifest_path,manifest)
assert all((ROOT/rel).is_file() and sha(ROOT/rel)==expected for rel,expected in json.loads(read(manifest_path)).items())
print(json.dumps({'casos_aprovados':len(cases),'manifesto_final':len(manifest),'links_conferidos':len(links),'ancoras_r53':len(cited),'originais_preservados':preserved,'novos_links_quebrados':bad,'teste_humano':False,'simulacao_de_combate':False,'equilibrio_validado':False},ensure_ascii=False,indent=2))
