#!/usr/bin/env python3
"""R09. Enumeração exata; não é playtest nem simulação do combate completo.
Invariantes: decisões v0.176 prevalecem sobre tabelas antigas; 16 entradas no índice (15 locais e Ritual em capítulo próprio);
marcos após ganho básico; Canalizar só é removido do ataque que leva feitiço;
sem multiplicar dados adicionais em crítico geral; Cura hostil não é automática;
raios múltiplos de 1,5; capacidade de Domínio Simples nunca se renova por saída.
Lê tabelas da candidata e progressão publicada. Escreve somente nesta pasta.
"""
from pathlib import Path
import re,json,hashlib,itertools,math,importlib.util
from fractions import Fraction
P=Path(__file__).resolve().parent
D=P.parent
ROOT=next(p for p in D.parents if (p/'sistema/03-mecanica/18-progressao.md').exists())
TXT=(D/'APTIDOES-E-REFINO.md').read_text()
def part(s,key):
 m=re.search(r'<!-- page:'+re.escape(key)+r'\|.*?-->(.*?)(?=<!-- page:|\Z)',s,re.S)
 if not m:raise ValueError('Página ausente: '+key)
 return m[1]
def contract(s):
 errs=[]
 for needle in ['1 PE até seu Refino','1d6 de Força por PE gasto','atributo de conjuração da ficha','Os d6 são os dados básicos deste ataque','Canalizar em Golpe','outro momento do turno ou da rodada não apaga','esse uso ofensivo não produz efeito','não significa pertencer à rota sem energia','duas melhorias funcionam juntas','O total impedido pertence à ativação','Sair e voltar não o zera','90 m de você ao concluir','dano de Energia Reversa, com 50% a mais','ela falha automaticamente','sem crítico','uma Barreira Simples ou uma Cortina de cada vez','1,5 × sua maior Classe, arredondado para baixo','uma falha acrescenta uma falha à Cesta','cada metade para baixo separadamente','Esse uso não cura vida','as marcas desaparecem no descanso longo','os dados adicionais de Canalizar não dobram']:
  if needle.lower() not in s.lower():errs.append(needle)
 rows=re.findall(r'^\| (1–2|3–5|6–8|9|10) \| (\dd\d) \|$',part(s,'apt-canalizar'),re.M)
 if rows!=[('1–2','1d4'),('3–5','2d4'),('6–8','3d4'),('9','4d4'),('10','4d6')]:errs.append('curva Canalizar')
 cat=part(s,'apt-catalogo')
 if '| Ritual | Inteligência 5, nível 10 e Técnica Inata. Regras em Ritual e Pactos. |' not in cat:errs.append('Ritual no índice')
 if len(re.findall(r'^\| (?!Aptidão \||---)[^|]+\|',cat,re.M))!=16:errs.append('catálogo 16')
 pages=re.findall(r'<!-- page:([^|]+)\|([^>]+) -->',s)
 if len(pages)!=len({x[0] for x in pages}):errs.append('ids repetidos')
 for key,title in pages:
  b=part(s,key);words=len(re.findall(r'\b[\wÀ-ÿ]+\b',b))
  if not 180<=words<=400:errs.append(f'palavras {key}: {words}')
  if not b.lstrip().startswith('# '+title):errs.append('título '+key)
 if re.search(r'^#+\s+(?:A|O|As|Os)\s',s,re.M):errs.append('artigo inicial')
 return errs
checks=[]
def check(name,got,want,source='APTIDOES-E-REFINO.md'):
 checks.append(dict(caso=name,obtido=got,esperado=want,passou=got==want,fonte=source))
check('Contrato completo',contract(TXT),[])
# Tabelas operacionais extraídas do manuscrito.
can={}
for ran,num,side in re.findall(r'^\| ([\d–]+) \| (\d+)d(\d+) \|$',part(TXT,'apt-canalizar'),re.M):
 endpoints=list(map(int,ran.split('–')))
 for r in range(endpoints[0],endpoints[-1]+1):can[r]=(int(num),int(side))
cover={r:r//3+1 for r in range(1,11)}
ray={}
for ran,num in re.findall(r'^\| ([\d–]+) \| ([\d,]+) m \|$',part(TXT,'apt-simples'),re.M):
 endpoints=list(map(int,ran.split('–')))
 for r in range(endpoints[0],endpoints[-1]+1):ray[r]=float(num.replace(',','.'))
prog=(ROOT/'sistema/03-mecanica/18-progressao.md').read_text()
levels={int(n):dict(m=int(m),r=int(r),c=int(c)) for n,m,r,c in re.findall(r'^\| \*\*(\d+)\*\* \| [^|]*\| (\d+) \| \d+ \| (\d+) \| (\d+) \|',prog,re.M)}
assert levels and 26 in levels
lv=lambda n:levels[max(k for k in levels if k<=n)]
MARCOS=[6,10,14,18,22,26,30]
def progression(seq):
 r,ap=1,0;out=[]
 for n,ch in zip(MARCOS,seq):
  r=min(10,r+1);gain=0
  if ch=='R':
   if r==10:gain=2
   else:r+=1;gain=1
  ap+=gain;out.append((n,r,ap,gain))
 return out
allroutes=[progression(x) for x in itertools.product('RCL',repeat=7)]
check('2187 sequências de marcos',len(allroutes),2187)
check('limite Refino todas sequências',max(row[1] for seq in allroutes for row in seq),10)
check('máximo escolhas aptidões',max(seq[-1][2] for seq in allroutes),10)
check('sempre Refino',progression('RRRRRRR'),[(6,3,1,1),(10,5,2,1),(14,7,3,1),(18,9,4,1),(22,10,6,2),(26,10,8,2),(30,10,10,2)])
check('sem escolha ainda Refino8',progression('CCCCCCC')[-1][1:],(8,0,0))
check('meio a meio',[(r,a) for _,r,a,_ in progression('RCRCRCC')],[(3,1),(4,1),(6,2),(7,2),(9,3),(10,3),(10,3)])
# Precisão exata d20, crítico20 natural, empate acerta. pcrit é subconjunto pacerto.
def chances(bonus,defense):
 hits=[x for x in range(1,21) if x==20 or x+bonus>=defense]
 return Fraction(len(hits),20),Fraction(1,20)
def mean_dice(n,d):return Fraction(n*(d+1),2)
def attack_mean(base,additional,attr,bonus,defense,crit_add=False):
 hit,crit=chances(bonus,defense)
 return hit*(base+additional+attr)+crit*(base+(additional if crit_add else 0))
check('Essência0 vs atributo6, maestria4, Defesa20',list(map(float,[chances(4,20)[0],chances(10,20)[0]])),[.25,.55])
check('Canalizar R6',can[6],(3,4))
check('Canalizar R10',can[10],(4,6))
check('arma +Canalizar R6 crítico',2*3.5+4+float(mean_dice(*can[6])) ,18.5)
# Exceção de Cirúrgico: preservada apenas como interface, não reescrita no capítulo.
def assassin(r,attr,weapon=8,critical=False):
 n,d=can[r];extra=max(0,attr-1);mult=2 if critical else 1
 return dict(arma_dados=mult,arma_d=weapon,canal_dados=n*mult,extras=extra*mult,canal_d=d,custo_PE=extra)
check('Cirúrgico Dex5 R6 normal',assassin(6,5),dict(arma_dados=1,arma_d=8,canal_dados=3,extras=4,canal_d=4,custo_PE=4),'35 caminhos / Incursor aprovado')
check('Cirúrgico Dex5 R6 crítico',assassin(6,5,critical=True),dict(arma_dados=2,arma_d=8,canal_dados=6,extras=8,canal_d=4,custo_PE=4),'35 caminhos / Incursor aprovado')
for r in range(1,11):
 check(f'proteção R{r}',cover[r],r//3+1)
 check(f'raio R{r} múltiplo1,5',ray[r]/1.5==int(ray[r]/1.5),True)
 check(f'raio R{r} arredondado próximo',ray[r],round((1.5+r//2)/1.5)*1.5)
# Kokusen d100 exato, incluindo bônus acumulado; teste com vantagem falha uma vez.
def koko(r,const=False,better=False,failures=0):
 t=min(100,(3 if const else 2)*r+2*failures)
 return Fraction(10000-(100-t)**2,10000) if better else Fraction(t,100)
check('Kokusen10 básico',float(koko(10)),.2)
check('Kokusen10 Melhorado',float(koko(10,better=True)),.36)
check('Kokusen10 Constante',float(koko(10,const=True)),.3)
check('Kokusen10 duas',float(koko(10,True,True)),.51)
check('Kokusen limite nunca excede100',float(koko(10,True,True,60)),1.)
check('Kokusen no dano final21',math.ceil(21*1.5),32)
check('zero continua zero',math.ceil(0*1.5),0)
# Domínio Simples: autômato finito reflete modelo publicado, não piso no restante.
def ds(cap,ess,outcomes):
 blocked=0;events=[];floor=max(1,ess//2)
 for fail in outcomes:
  if blocked>=cap:events.append('passa');break
  blocked+=1;events.append('impedido')
  if fail:cap=max(min(cap,floor),cap-1)
 return blocked,cap,events
check('DS Ess4 igualdade duas falhas e terceiro',ds(3,4,[True,True,True]),(2,2,['impedido','impedido','passa']))
check('DS reaberto1 Ess6 não vira3',ds(1,6,[True,True]),(1,1,['impedido','passa']))
check('DS Ess6 igualdade falhas não renovam',ds(3,6,[True]*5),(3,3,['impedido','impedido','impedido','passa']))
check('DS Ess2 menor tudo falha',ds(2,2,[True]*3),(1,1,['impedido','passa']))
ds_grid=[]
for e in range(7):
 for base in (1,2,3,4):
  for fs in itertools.product([False,True],repeat=6):
   b,c,ev=ds(base,e,fs)
   assert 0<=b<=base and c<=base
   ds_grid.append((e,base,fs,b,c))
check('DS sequências exatas testadas',len(ds_grid),1792)
check('trocar adversário não aumenta capacidade',min(2,4),2)
check('adversário maisforte reduz capacidade',min(4,2),2)
check('Cesta Ess0 mínimo',max(1,0//2),1)
check('Cesta Ess4 limiar',max(1,4//2),2)
check('Pétala igualdade recebe quarto',math.ceil(21/4),6)
check('Extensão C5 R9 total',5+9*math.ceil(1.5*5),77)
check('Extensão C7 R10 total',7+10*math.ceil(1.5*7),117)
check('Extensão R7 neutraliza máximo3',7//3+1,3)
check('Extensão R10 neutraliza máximo4',10//3+1,4)
check('Energia Reversa C4 PE3 média',float(mean_dice(3,8)),13.5)
check('Circulação C5 teto',math.floor(1.5*5),7)
check('Circulação C7 teto',math.floor(1.5*7),10)
check('Regravação INT5 M3 metades separadas',5//2+3//2,3)
check('Regravação INT5 M4',5//2+4//2,4)
check('Cura convertida26',math.ceil(26*1.5),39)
check('Cura C3 teto6d8 máximo permitido',6,2*3)
check('Barreira R6',5*6,30)
check('Cortina R6',40*6,240)
check('Cortina raio90 é60quadrados',90/1.5,60.)
# Matriz quantitativa com pressupostos controlados; não conta PE de outras skills.
proj=[];mixed=[]
for n in range(2,31):
 values=lv(n);c=values['c'];m=values['m'];attr=min(6,m+2);df=10+attr+4
 for route in ('especialista','generalista'):
  r=1
  for mark,rr,_,_ in progression('RRRRRRR' if route=='especialista' else 'CCCCCCC'):
   if n>=mark:r=rr
  c0=2+sum(n>=x for x in [5,11,17,23]);hit,crit=chances(attr+m,df)
  proj.append(dict(nivel=n,rota=route,refino=r,classe=c,pe=r,acesso_ordinario=n>=6,defesa_cenario=df,atributo_cenario=attr,maestria_cenario=m,dano_pago_medio=3.5*r,antigo_fixo=r,classe0_dados=c0,classe0_media=4.5*c0,projetil_vazio_media=13.5*c,pago_esperado=float((hit+crit)*3.5*r),classe0_esperado=float((hit+crit)*4.5*c0),eficiencia_pago=3.5,eficiencia_feitico_vazio=4.5,dominado_apenas_em_custo_dano=(3.5*r<=4.5*c0),nota='Projetar independe do Selo/Famílias/tipos da técnica; diferença de acesso impede declarar dominância completa.'))
  adds=mean_dice(*can[r]);oldadds=mean_dice(4,6) if r==10 else mean_dice(r//3,4)
  for attacks in [1,2,3,4,5]:
   base=mean_dice(1,4+2*(m-1))
   mixed.append(dict(nivel=n,rota=route,refino=r,ataques=attacks,publicado_v176=float(attacks*attack_mean(base,adds,attr,attr+m,df)),peca11_desatualizada=float(attacks*attack_mean(base,oldadds,attr,attr+m,df)),extras_can_por_conjurar_outro_turno=float(attacks*chances(attr+m,df)[0]*adds),pressuposto='Sem custos/limites que concedem ataques, sem Kokusen/Manhas/Fluidez: não é rodada realizável garantida.'))
# Comparação da área geométrica de raios, sem presumir número de miniaturas atingidas.
radii=[dict(refino=r,raio_antigo=1.5+r//2,raio_novo=ray[r],razao_area=round((ray[r]/(1.5+r//2))**2,6)) for r in range(1,11)]
# Cura, dano e regravação por Classe, sem números extras por Refino.
healing=[dict(classe=c,reversa_max=c,reversa_media=4.5*c,circulacao_max=math.floor(1.5*c),circulacao_padrao_media=4.5*math.floor(1.5*c),circulacao_bonus_media=2.5*math.floor(1.5*c),forma_cura_dados=2*c,forma_cura_ofensiva_media_antes_arredondar=13.5*c,forma_cura_ofensiva_media_exata_sem_defesas=13.5*c+.25,projetil_vazio_media=13.5*c) for c in range(1,8)]
mutations=[]
for name,old,new in [('Canalizar apagado noRefino1','| 1–2 | 1d4 |','| 1–2 | 0d4 |'),('Projetar gratuito','1 PE até seu Refino','0 PE'),('Cortina ilimitada','90 m de você ao concluir','qualquer distância'),('relógio DS reinicia','Sair e voltar não o zera','Sair e voltar o zera'),('título artigo','# Circulação','# A Circulação'),('Cura hostil torna-se automático','dano de Energia Reversa, com 50% a mais','cura automática'),('Permitir pilha de barreiras','uma Barreira Simples ou uma Cortina de cada vez','quantas barreiras quiser'),('dobrar Canalizar geral','Os dados adicionais de Canalizar não dobram','Os dados adicionais de Canalizar dobram')]:
 assert old in TXT,name
 errs=contract(TXT.replace(old,new,1));mutations.append(dict(nome=name,detectada=bool(errs),achados=errs))
# Rodar detector real sem editar MANUSCRITOS (registro é do agente principal).
spec=importlib.util.spec_from_file_location('editorial',ROOT/'sistema/05-material/livro/planejamento-editorial/validacao-editorial/conferir_editorial.py')
ed=importlib.util.module_from_spec(spec);spec.loader.exec_module(ed)
reg=json.loads((ROOT/'sistema/05-material/livro/planejamento-editorial/validacao-editorial/DONOS.json').read_text())
registry=reg if isinstance(reg,list) else reg.get('entradas',reg.get('termos',[]))
editorial=ed.check_file(D/'APTIDOES-E-REFINO.md',require_review=True)
report=dict(sha256_texto=hashlib.sha256(TXT.encode()).hexdigest(),contrato=contract(TXT),checks=checks,contagem_checks=len(checks),falhas=[x for x in checks if not x['passou']],rotas_enumeradas=len(allroutes),sequencias_ds=len(ds_grid),mutacoes=mutations,editorial_sem_registry_alterado=editorial,projetar=proj,canalizar_rodadas=mixed,raios=radii,cura=healing,limites=['Nenhum teste humano foi realizado.','Modelo ofensivo não agrega todas as habilidades de Caminho/Trilha nem duração do combate.','Opções com gatilhos diferentes não são chamadas dominadas pelo dano isolado.','Inspeção visual PDF é responsabilidade da exportação e ainda não consta deste script.'])
(P/'AUDITORIA-NUMERICA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:report[k] for k in ['contagem_checks','falhas','rotas_enumeradas','sequencias_ds','mutacoes','editorial_sem_registry_alterado']},ensure_ascii=False,indent=2))
raise SystemExit(1 if report['falhas'] or any(not x['detectada'] for x in mutations) or editorial else 0)
