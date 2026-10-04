"""Auditoria localizada das sincronizações de Insistir e reparo. Sem playtest."""
from pathlib import Path
from fractions import Fraction
import json, hashlib, re
B=Path(__file__).resolve().parent
P=next(p for p in B.parents if (p/'validacao-editorial').exists())
checks=[];models=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def ck(name,a,b=True):checks.append({'id':name,'obtido':a,'esperado':b,'ok':a==b})
if (B/'ROTAS.md').exists():
 F='ROTAS.md';t=(B/F).read_text();s=re.search(r'## Segundo Fôlego.*?(?=## Contragolpe)',t,re.S)[0]
 source=P/'dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md';d=source.read_text();sources=[source]
 for x in ['**Uma vez por descanso longo**','ao escolher **Insistir**','**primeiro custo de vida máxima**','**1/8 do máximo de referência**','custos posteriores e a janela de socorro continuam normais','não concede rodada ou ação adicional nem recupera vida ou Integridade']:
  ck('clausula-'+x,x in s)
 ck('sem-rodada-inexistente','rodada exigida' not in s)
 costs=[int(x) for x in re.findall(r'\| (?:Ao escolher Insistir|Após uma volta completa, se ainda houver janela|Após outra volta completa, se ainda houver janela) \| 1/(\d+) da referência',d)]
 ck('sequencia-da-fonte',costs,[8,4,2]);ck('fonte-custos-para-cima','Arredonde cada custo para cima.' in d)
 ck('fonte-janela-primeiro','Primeiro desconte a rodada da janela.' in d)
 def state(ref,sequelas,passive):
  window=max(0,3-sequelas);maximum=ref;payments=[]
  if not window:return {'janela':0,'maximo':ref,'pagamentos':[],'derrotado':True}
  for i,den in enumerate(costs[:window]):
   charge=0 if passive and i==0 else (ref+den-1)//den
   if maximum-charge<1:break
   maximum-=charge;payments.append(charge)
  return {'janela':window,'maximo':maximum,'pagamentos':payments,'derrotado':False}
 ck('ref80-comum',state(80,0,False)['pagamentos'],[10,20,40]);ck('ref80-passiva',state(80,0,True)['pagamentos'],[0,20,40]);ck('ref80-maximo-passiva',state(80,0,True)['maximo'],20)
 ck('uma-sequela-duas-cobrancas',state(80,1,True)['pagamentos'],[0,20]);ck('duas-sequelas-so-primeira',state(80,2,True)['pagamentos'],[0]);ck('tres-sequelas-sembeneficio',state(80,3,True)['derrotado'])
 ck('referencia1-permiteprimeiro',state(1,0,True)['pagamentos'],[0]);ck('referencia1-naoconseguesequinte',state(1,0,True)['maximo'],1)
 for ref in range(1,161):
  for sequelas in range(4):
   a,b=state(ref,sequelas,False),state(ref,sequelas,True)
   ck(f'janela-preservada-{ref}-{sequelas}',a['janela'],b['janela'])
   if not b['derrotado']:
    ck(f'primeiro-gratis-{ref}-{sequelas}',b['pagamentos'][0],0)
    for i,pay in enumerate(b['pagamentos'][1:],1):ck(f'subsequente-{ref}-{sequelas}-{i}',pay,(ref+costs[i]-1)//costs[i])
   models.append({'referencia':ref,'sequelas':sequelas,'sem_passiva':a,'com_passiva':b,'economia_inicial':(ref+7)//8})
 limit='Modela apenas pagamentos, janela por Sequelas e disponibilidade de saldo. Dano posterior, decisões de abandonar Insistir e cura seguem a fonte. Máximos muito baixos podem ganhar a possibilidade de escolher Insistir quando o custo inicial não caberia; a Passiva não garante pagar o próximo custo.'
else:
 F='INVOCACOES-EM-CAMPO.md';t=(B/F).read_text();s=re.search(r'<!-- page:inv-reparo.*?(?=<!-- page:)',t,re.S)[0]
 sources=[P/'origens/lote-01/ORIGENS-E-LEGADOS.md',P/'invocacoes/fabricacao/lote-01/FABRICACAO-DE-ENTIDADES.md']
 for x in ['uma pessoa treinada','**uma tentativa por corpo**','mesmo que haja outros reparadores','acima de zero','**8 + atributo usado no ofício + Maestria de quem repara + ajuste**','Especialização e outros modificadores entram na rolagem, sem aumentar a base da CD','Reparo não religa Desligada']:
  ck('clausula-'+x,x in s)
 ck('sem-escada-vaga','escada de CD' not in s)
 adjustments={}
 for line in s.splitlines():
  if line.startswith('|'):
   cells=[v.strip() for v in line.strip('|').split('|')]
   if cells[0] in ['Igual','Uma abaixo','Duas ou mais abaixo']:adjustments[cells[0]]=int(cells[2].replace('−','-'))
 ck('ajustes',[adjustments[x] for x in ['Igual','Uma abaixo','Duas ou mais abaixo']],[0,-2,-4])
 for source in sources:
  doc=source.read_text();ck('ajuste-medio-'+source.name,'−2' in doc);ck('ajuste-facil-'+source.name,'−4' in doc);ck('base-'+source.name,'8 +' in doc)
 for a in range(7):
  for mastery in range(1,5):
   for adjustment in adjustments.values():
    dc=8+a+mastery+adjustment
    for specialization in [0,mastery]:
     count=sum(d20+a+mastery+specialization>=dc for d20 in range(1,21));expected=min(20,13-adjustment+specialization)
     ck(f'prob-{a}-{mastery}-{adjustment}-{specialization}',count,expected)
     models.append({'atributo':a,'maestria':mastery,'ajuste':adjustment,'especializacao':specialization,'CD':dc,'probabilidade':str(Fraction(count,20))})
 ck('exemplo-CD',8+3+2,13);ck('exemplo-limiar',8+3+2,13);ck('exemplo-cura',31//2,15);ck('exemplo-final',8+31//2,23)
 limit='Modela reparadores treinados e bônus de especialização na rolagem. Não substitui requisitos de materiais, capacidade de trabalhar ou simulação econômica. A tabela de fabricação fornece a fórmula compartilhada, mas não transforma reparo em criação ou aquisição.'
h=sha(B/F);res={'sha256_texto':h,'ok':all(x['ok'] for x in checks),'verificacoes':len(checks),'modelos':models,'checks':checks,'fontes':{str(p.relative_to(P)):sha(p) for p in sources},'limites':[limit,'Validação localizada por modelo, sem playtest ou teste com leitores humanos.']}
(B/'evidencias/SINCRONIZACAO-FINAL.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'arquivo':F,'sha256':h,'ok':res['ok'],'verificacoes':len(checks),'perfis':len(models)},ensure_ascii=False))
raise SystemExit(0 if res['ok'] else 1)
