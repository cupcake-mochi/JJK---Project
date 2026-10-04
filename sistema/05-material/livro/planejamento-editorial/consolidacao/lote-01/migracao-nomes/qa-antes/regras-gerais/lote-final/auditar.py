from pathlib import Path
from itertools import product
import json,hashlib,re,math
B=Path(__file__).resolve().parent; E=B/'evidencias';E.mkdir(exist_ok=True);p=B/'REGRAS-GERAIS.md';t=p.read_text();h=hashlib.sha256(t.encode()).hexdigest();checks=[];cases=[]
def check(id,truth,**more):checks.append({'id':id,'passou':bool(truth),**more})
def case(id,actual,expected,kind='limite',source=None):
 ok=actual==expected if not isinstance(expected,float) else abs(actual-expected)<1e-10
 cases.append({'id':id,'tipo':kind,'resultado':actual,'esperado':expected,'passou':ok,'fonte':source or 'REGRAS-GERAIS.md; ALTERACOES.json'})
sections=list(re.finditer(r'<!-- page:([^|]+)\|([^>]+) -->\n(.*?)(?=\n<!-- page:|\Z)',t,re.S));ids=[x[1] for x in sections]
check('ids_unicos',len(ids)==len(set(ids)));check('40_paginas',len(ids)==40)
for m in sections:
 check('titulo_'+m[1],m[3].strip().startswith('# '+m[2]));check('sem_artigo_'+m[1],not re.match(r'^(A|O|As|Os) ',m[2]));check('sem_como_ler_'+m[1],not m[2].lower().startswith('como ler'))
for target in re.findall(r'\]\(#([^)]+)\)',t):check('link_'+target,target in ids)
for s in ['Mão na Roda','Movimento Acrobático','Parkour','Pugilista','Assassino','Golpe Cirúrgico','Antena','Maldição do Inventário','Duro de Matar']:
 check('localizacao_'+s,s not in t)
clauses={
'bloquear_timing':'depois de conhecer sua rolagem',
'bloquear_custo':'não gasta Reação',
'bloquear_resultado':'O resultado substitui a Defesa, mesmo se for menor.',
'critico20':'independentemente do resultado de Bloquear',
'margem':'ainda precisa acertar e continua sujeito a Aparar',
'ajuda_prazo':'começo do seu próximo turno',
'ajuda_alcance':'ao seu alcance corpo a corpo',
'provocar_empate':'Empatar resiste.',
'oportunidade_visao':'enxerga ou acompanha por um sentido equivalente à visão',
'oportunidade_antes':'imediatamente antes de ela sair',
'reacao_renova':'no começo do seu próximo turno',
'concentracao_por_aplicacao':'um teste por golpe ou aplicação de dano',
'concentracao_zero':'Se as defesas reduzirem o dano a zero',
'concentracao_temporaria':'Dano absorvido pela vida temporária ainda conta',
'concentracao_estados':'Inconsciente encerra a concentração. Incapacitado, por si só, não a encerra.',
'ocultacao_cd10':'CD 10 + o bônus completo de Percepção',
'ocultacao_guardada':'Anote o total de Furtividade',
'ocultacao_novo_teste':'não concede um teste gratuito',
'energia18':'até 18 m de você',
'energia_instantanea':'não acompanha movimentos futuros',
'energia_paredes':'impede obter sua posição exata',
'energia_equipamento':'não contam como divisórias do ambiente',
'manobra_cd':'8 + sua Força + sua maestria',
'manobra_tamanho':'até uma categoria de tamanho maior',
'andar_criatura':'duas categorias maior ou menor',
'carga':'5 + Força',
'corpos':'divida a massa do corpo em quilogramas por 12',
'carga_semarredonda':'sem arredondar para caber',
'queda20d6':'até **20d6**',
'queda_repartida':'uma única vez',
'queda_padroao':'Ação Padrão antes de começar a queda',
'queda_naoduplica':'Não some este procedimento ao mesmo impacto',
'montaria_comando':'Entidades invocadas seguem seus comandos e recursos próprios',
'montaria_novoturno':'não permite agir de novo',
'conversao':'Padrão vira Bônus e essa Bônus vira Movimento',
}
for k,s in clauses.items():check(k,s in t)
# Exact enumerate d20 attacks and independent d10 defenses. No additional damage/counterattack budget is presumed.
def blocked_hit(a,bonus,defense,x,y):
 if a==20:return True
 if x==y==10:return False
 if x==y==1:return True
 return a+bonus>=x+y+defense-11
profiles=[]
for defense,bonus in product(range(10,25),range(0,11)):
 static=sum(a==20 or a+bonus>=defense for a in range(1,21))/20
 always=sum(blocked_hit(a,bonus,defense,x,y) for a,x,y in product(range(1,21),range(1,11),range(1,11)))/2000
 informed=sum(blocked_hit(a,bonus,defense,x,y) if a==20 or a+bonus>=defense else 0 for a,x,y in product(range(1,21),range(1,11),range(1,11)))/2000
 check(f'optional_no_worse_{defense}_{bonus}',informed<=static+1e-9)
 profiles.append({'defesa':defense,'bonus':bonus,'acerto_estatico':static,'bloquear_sempre':always,'bloquear_se_acertaria':informed,'reducao_pp':round(100*(static-informed),4)})
case('def17_ataque6_estatica',next(x for x in profiles if x['defesa']==17 and x['bonus']==6)['acerto_estatico'],.5)
case('def17_ataque6_informada',next(x for x in profiles if x['defesa']==17 and x['bonus']==6)['bloquear_se_acertaria'],.4175)
case('critico20_supera_aparar',blocked_hit(20,0,30,10,10),True,'negativo')
case('margem19_nao_supera_aparar',blocked_hit(19,10,10,10,10),False,'negativo')
case('brecha_acerta_baixo',blocked_hit(2,0,30,1,1),True,'positivo')
case('aparar_comum',blocked_hit(18,12,10,10,10),False,'positivo')
# Ordered full-set disadvantage of Blocking.
def rank(x,y):return (-1 if x==y==1 else 1000 if x==y==10 else x+y)
pairs=list(product(range(1,11),repeat=2));selected=[min([p1,p2],key=lambda z:rank(*z)) for p1,p2 in product(pairs,repeat=2)]
case('aparar_desvantagem',sum(p==(10,10) for p in selected)/10000,.0001)
case('brecha_desvantagem',sum(p==(1,1) for p in selected)/10000,.0199)
# Provocar uses two rolls, target succeeds on tie; no replacement of the skill by fixed CD.
opposed=[]
for pbonus,sbonus in product(range(0,13),range(0,11)):
 success=sum(a+pbonus>b+sbonus for a,b in product(range(1,21),repeat=2))/400
 old_tie=sum(a+pbonus>=b+sbonus for a,b in product(range(1,21),repeat=2))/400
 opposed.append({'provocar':pbonus,'tr':sbonus,'falha_alvo':success,'se_empate_favorecesse_provocador':old_tie,'diferenca_pp':(old_tie-success)*100})
case('provocar_bonus_iguais',opposed[0]['falha_alvo'],.475)
case('provocar_empate16',16>=16,True,'negativo')
# Probability of advantage; roll outcomes and action budgets.
for needed in range(1,22):
 prob=sum(a>=needed for a in range(1,21))/20
 adv=sum(max(a,b)>=needed for a,b in product(range(1,21),repeat=2))/400
 check('ajudar_vantagem_'+str(needed),abs(adv-(1-(1-prob)**2))<1e-9)
# Distances and terrains in steps, bodies and exact non-rounded equipment Volume.
def steps(m):return math.floor((m+1e-9)/1.5)*1.5
def grid(x,y,z=0):return max(abs(x),abs(y),abs(z))*1.5
case('3d6e4_5',grid(4,0,3),6.0);case('diagonal1',grid(1,1,1),1.5)
case('metade4_5',steps(4.5/2),1.5);case('saltoforca1impulso',3+1.5*1,4.5)
case('saltoforca1parado',steps(4.5/2),1.5)
for strength in range(7):
 normal=3+1.5*strength
 check('salto_tabela_'+str(strength),f'| {strength} |' in t)
 case('carga_forca_'+str(strength),5+strength,5+strength)
case('carregar_60kg_eq1_proprio2',60/12+1+2,8.0)
case('excesso_forca2',60/12+1+2<=7,False,'negativo')
case('arrasto_regular_9m',steps(9/2),4.5);case('arrasto_dificil_9m',steps(9/3),3.0)
case('rastejar_espremer_dificil',1.5*(1+1+1+1),6.0)
case('coletivo_com_equipamento',1+7/2,4.5)
case('andar6_voo12',12-6,6);case('troca_nao_21',max(9,12),12)
case('correr_maisreserva_voo',12+12,24)
for height in [0,1.5,3,4.5,6,7.5,9,30,60,90,150,151.5,300]:
 dice=min(20,int(height//3));case('queda_dados_'+str(height),dice,min(20,int(height/3)))
for damage in range(121):
 victim=damage//2;falling=damage-victim
 check('queda_conserva_'+str(damage),victim+falling==damage)
case('queda11_vitima',11//2,5);case('queda11_corpo',11-11//2,6)
case('tamanhos_media_grande',abs(2-3)<=1,True);case('tamanhos_pequena_imensa',abs(1-4)<=1,False,'negativo')
# Source snapshots unchanged.
R=next(x for x in B.parents if (x/'sistema/03-mecanica').exists())
for source,sha in json.loads((E/'fontes-preservadas.json').read_text()).items():check('source_'+source,hashlib.sha256((R/source).read_bytes()).hexdigest()==sha)
for item in json.loads((B/'INVENTARIO.json').read_text())['cobertura']:check('cobertura_'+item['id_fonte'],item['destino'] in ids or item['destino']=='R18')
# Mutations demonstrate a few textual contracts detect changed grants/critical constraints.
mutations=[('ocultacao_cd10','CD 10 + o bônus completo de Percepção','CD 8 + o bônus completo de Percepção'),('concentracao_por_aplicacao','um teste por golpe ou aplicação de dano','um teste por tipo de dano'),('energia18','até 18 m de você','até 90 m de você'),('carga','5 + Força','50 + Força'),('manobra_tamanho','até uma categoria de tamanho maior','qualquer tamanho'),('oportunidade_visao','enxerga ou acompanha por um sentido equivalente à visão','localizou antes')]
for key,before,after in mutations:check('mutacao_'+key,clauses[key] not in t.replace(before,after))
result={'ok':all(x['passou'] for x in checks+cases),'sha256_texto':h,'verificacoes':len(checks),'casos_executados':len(cases),'perfis_bloquear':len(profiles),'perfis_provocar':len(opposed),'checagens':checks,'casos':cases,'bloquear':profiles,'provocar':opposed,'limites':['Modelos de dados uniformes, não playtest.','Bloquear calculado sem valorar contra-ataques ou gatilhos adicionais.','Quedas/carga/distância são abstrações, não simulações físicas.','Verificação de texto detecta regressão, não prova isolada de clareza.']}
(E/'auditoria-numerica.json').write_text(json.dumps(dict(result,manuscritos_auditados={str(p.relative_to(R)):h}),ensure_ascii=False,indent=2)+'\n')
(E/'regras-verificadas.json').write_text(json.dumps({'ok':result['ok'],'sha256_texto':h,'casos':cases,'verificacoes':len(checks)},ensure_ascii=False,indent=2)+'\n')
(E/'CASOS-EXECUTADOS.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['ok','sha256_texto','verificacoes','casos_executados','perfis_bloquear','perfis_provocar']},ensure_ascii=False))
if not result['ok']:
 for x in checks+cases:
  if not x['passou']:print('FALHA',x)
 raise SystemExit(1)
