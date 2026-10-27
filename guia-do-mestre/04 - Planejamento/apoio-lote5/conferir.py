#!/usr/bin/env python3
"""Confere cobertura, fontes e contas de L5. Não avalia equilíbrio ou aprendizagem."""
from pathlib import Path
import argparse,collections,hashlib,json,math,sys
ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--fontes',type=Path);ap.add_argument('--preparado',type=Path);args=ap.parse_args()
here=Path(__file__).absolute().parent;root=args.fontes or here.parents[1]
def path(rel):return args.preparado/rel if args.preparado and (args.preparado/rel).is_file() else root/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
s=json.loads((here/'estado-inicial.json').read_text());data=json.loads((here/'cobertura-atualizada.json').read_text());prior=json.loads(path(s['cobertura_anterior']).read_text());problems=[]
def check(ok,msg):
 if not ok:problems.append(msg)
changed=['M052','M058','M067','M069','M070','M071','M074','M078'];checked=0
for group,count in [('pontos',130),('competencias',20)]:
 before={r['id']:r for r in prior[group]};check(len(data[group])==len({r['id'] for r in data[group]})==count,'IDs duplicados/ausentes: '+group);check({r['id'] for r in data[group]}==set(before),'Inventário alterado: '+group)
 for r in data[group]:
  old=before[r['id']];excluded={'evidencias'}
  if r['id'] in changed:
   check(old['estado']=='P' and r['estado']=='E' and r['falta']==r['lote']=='—','Transição indevida: '+r['id']);excluded|={'estado','presente','falta','lote'}
  if r['id']=='P20':
   check(old['estado']==r['estado']=='P' and r['lote']=='L4','P20 encerrado indevidamente');excluded|={'presente','restante','lote'}
  check({k:v for k,v in r.items() if k not in excluded}=={k:v for k,v in old.items() if k not in excluded},'Escopo alterado: '+r['id'])
  for e in r['evidencias']:
   p=path(e['arquivo']);check(p.is_file(),'Fonte ausente: '+e['arquivo'])
   if not p.is_file():continue
   check(sha(p)==e['sha256'],'Fonte alterada: '+e['arquivo']);lines=p.read_text().splitlines();valid=1<=e['inicio']<=e['fim']<=len(lines);check(valid,'Intervalo inválido: '+e['arquivo'])
   if valid:check(lines[e['inicio']-1].lstrip('# ').strip()==e['titulo'],'Título divergente: '+e['arquivo'])
   checked+=1
check(dict(collections.Counter(r['estado'] for r in data['pontos']))=={'E':127,'P':3} and data['totais_pontos']=={'E':127,'P':3,'L':0},'Totais M divergentes')
check(dict(collections.Counter(r['estado'] for r in data['competencias']))==data['totais_competencias']=={'E':17,'P':3},'Totais P divergentes')
check([r['id'] for r in data['competencias'] if r['estado']=='P']==['P14','P15','P20'],'Competências parciais divergentes')
check(all(not r['aprendizagem_observada'] for r in data['competencias']),'Aprendizagem indevidamente declarada')
for b in data['lotes']:
 old=next(x for x in prior['lotes'] if x['id']==b['id']);expected={**old,'estado':'entregue'} if b['id']=='L5' else old;check(b==expected,'Lote alterado fora de escopo: '+b['id'])
for field in ['fonte_R53','copia_R53']:check(sha(Path(s[field]))==s['R53_sha256'],'R53 alterada: '+field)
g92='06 - Redacao do Guia/92-reserva-condensada-proposta-e-comparacao.md';check(sha(path(g92))==s['manifesto_anterior'][g92],'G92 alterada: decisão de Reserva deve permanecer')
m=json.loads((here/'contas.json').read_text())
check(m['projeto']==dict(base=4000,resina=6000,consumiveis=2000,servico=18000,orcamento=30000,retomada=8000,total=38000,reserva=40000,saldo=2000,horas_personagem=6,horas_Aya=12,horas_trabalho_total=18,espera=12,dedicacao_inicial=28,dedicacao_restante=22,teste_inicial=12,teste_retomada=17,CD=14),'Contas do projeto divergentes')
p=m['projeto'];check(p['total']==p['base']+2*(p['resina']+p['consumiveis'])+p['servico'] and p['saldo']==p['reserva']-p['total'],'Fluxo financeiro do projeto divergente');check(p['teste_inicial']<p['CD']<=p['teste_retomada'],'Falha/retomada divergentes');check(p['dedicacao_restante']==p['dedicacao_inicial']-p['horas_personagem'],'Serviço/espera debitados da ficha')
check(m['negociacao']==dict(pedido=24000,oferta_anterior=18000,teste=12,CD=14,horas_condicao=2,saldo=26000,diferenca_custo_venda=14000,dedicacao_final=20),'Contas da negociação divergentes');check(m['negociacao']['teste']<m['negociacao']['CD'],'Gatilho de falha ausente');check(m['negociacao']['saldo']==p['saldo']+m['negociacao']['pedido'],'Saldo não corresponde à venda')
check(m['objeto']==dict(volume=0.5,selo_inicio_min=540,selo_fim_min=1020,duracao_min=480,aviso_min=960,entrega_min=930,selo_restante_min=90,ingestao_min=840,residuo_fim_min=850,remocao_condicao_min=842,residuo_apos_remocao_min=8,TR=11,CD=14),'Horários/consequência do objeto divergentes')
q=m['socorro'];check(q==dict(maximo=84,sequelas_antes=1,janela=2,tratamento=21,classe=2,orcamento=6,base=2,forma=0,devolucao=0,melhorias=0,restricoes=0,dados=4,teto=4,PE_custo=6,PE_final=6,cura=22,PV_final=22,sequelas_final=2),'Contas do socorro divergentes');check(q['cura']>=math.ceil(q['maximo']/4) and q['PV_final']==min(q['cura'],q['maximo']),'Cura não encerra Morrendo ou subtrai o requisito');check(q['dados']==q['orcamento']-q['base'] and q['dados']<=2*q['classe'],'Montagem de cura inválida')
v=m['progressao'];check(v==dict(nivel_antes=20,feito_no_nivel=20,XP_anterior=3950,XP_base=100,posicao_semanal=3,XP_missao=50,XP_disponivel=4000,custos=[1500,1500],XP_gasto=3000,nivel_final=22,XP_final=1000,custo_proximo=1500),'Progressão divergente');check(15<=v['feito_no_nivel']<=20,'Faixa do feito inválida');level=20;xp=v['XP_disponivel']
while xp>=(1500 if level<=22 else 1700):
 xp-=1500 if level<=22 else 1700;level+=1
check(level==v['nivel_final'] and xp==v['XP_final'],'Aplicação de XP guardado divergente')
check([r['id'] for r in data['pontos'] if r['estado']=='P']==['M051','M124','M129'],'Pontos parciais divergentes')
output=dict(etapa=89,contagens_M=data['totais_pontos'],contagens_P=data['totais_competencias'],evidencias_conferidas=checked,reclassificados=changed,pontos_parciais=['M051','M124','M129'],competencias_parciais=['P14','P15','P20'],R53_intacta=not any('R53' in p for p in problems),decisao_Reserva_preservada=True,grupos_de_contas_conferidos=5,problemas=problems,limites='Integridade documental, contas explícitas e transições de cobertura; sem validação de aprendizagem ou equilíbrio.')
print(json.dumps(output,ensure_ascii=False,indent=2));sys.exit(bool(problems))
