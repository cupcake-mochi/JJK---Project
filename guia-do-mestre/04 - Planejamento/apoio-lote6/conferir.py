#!/usr/bin/env python3
"""Confere cobertura, fontes e contas de L6. Não avalia equilíbrio ou aprendizagem."""
from pathlib import Path
import argparse,collections,hashlib,json,math,sys
ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--fontes',type=Path);ap.add_argument('--preparado',type=Path);args=ap.parse_args()
here=Path(__file__).absolute().parent;root=args.fontes or here.parents[1]
def path(rel):return args.preparado/rel if args.preparado and (args.preparado/rel).is_file() else root/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
s=json.loads((here/'estado-inicial.json').read_text());data=json.loads((here/'cobertura-atualizada.json').read_text());prior=json.loads(path(s['cobertura_anterior']).read_text());problems=[]
def check(ok,msg):
 if not ok:problems.append(msg)
changed=['M055','M084','M087','M088','M090','M091'];checked=0
for group,count in [('pontos',130),('competencias',20)]:
 before={r['id']:r for r in prior[group]};check(len(data[group])==len({r['id'] for r in data[group]})==count,'IDs duplicados/ausentes: '+group);check({r['id'] for r in data[group]}==set(before),'Inventário alterado: '+group)
 for r in data[group]:
  old=before[r['id']];excluded={'evidencias'}
  if r['id'] in changed:
   check(old['estado']=='P' and r['estado']=='E' and r['falta']==r['lote']=='—','Transição indevida: '+r['id']);excluded|={'estado','presente','falta','lote'}
  if r['id']=='P20':
   check(old['estado']==r['estado']=='P' and r['lote']=='L4,L5','P20 encerrado indevidamente');excluded|={'presente','restante','lote'}
  check({k:v for k,v in r.items() if k not in excluded}=={k:v for k,v in old.items() if k not in excluded},'Escopo alterado: '+r['id'])
  for e in r['evidencias']:
   p=path(e['arquivo']);check(p.is_file(),'Fonte ausente: '+e['arquivo'])
   if not p.is_file():continue
   check(sha(p)==e['sha256'],'Fonte alterada: '+e['arquivo']);lines=p.read_text().splitlines();valid=1<=e['inicio']<=e['fim']<=len(lines);check(valid,'Intervalo inválido: '+e['arquivo'])
   if valid:check(lines[e['inicio']-1].lstrip('# ').strip()==e['titulo'],'Título divergente: '+e['arquivo'])
   checked+=1
check(dict(collections.Counter(r['estado'] for r in data['pontos']))=={'E':119,'P':11} and data['totais_pontos']=={'E':119,'P':11,'L':0},'Totais M divergentes')
check(dict(collections.Counter(r['estado'] for r in data['competencias']))==data['totais_competencias']=={'E':17,'P':3},'Totais P divergentes')
check([r['id'] for r in data['competencias'] if r['estado']=='P']==['P14','P15','P20'],'Competências parciais divergentes')
check(all(not r['aprendizagem_observada'] for r in data['competencias']),'Aprendizagem indevidamente declarada')
for b in data['lotes']:
 old=next(x for x in prior['lotes'] if x['id']==b['id']);expected={**old,'estado':'entregue'} if b['id']=='L6' else old;check(b==expected,'Lote alterado fora de escopo: '+b['id'])
for field in ['fonte_R53','copia_R53']:check(sha(Path(s[field]))==s['R53_sha256'],'R53 alterada: '+field)
g92='06 - Redacao do Guia/92-reserva-condensada-proposta-e-comparacao.md';check(sha(path(g92))==s['manifesto_anterior'][g92],'G92 alterada: decisão de Reserva deve permanecer')
m=json.loads((here/'contas.json').read_text());check(len(m['mescla'])==2,'Linhas da mescla ausentes')
for row in m['mescla']:
 c=row['classe'];L=math.ceil(c/2);M=c;P=math.ceil(c*1.5);damage=2 if c==3 else 3
 expected=dict(classe=c,orcamento=3*c,base=M,aura=L,escolher=M,devolucao=L,melhorias=1,restricoes=1,teto_devolucao=2*c,teto_cura_individual=2*c,teto_cura_coletiva=3*c-P,saldo=3*c-M-L-M+L,parcelas=[damage,1],explosao=M,diferenca=M-L,saldo_remodelado=3*c-M-M-M+L,parcelas_remodeladas=[damage-(M-L),1],PE=3*c,PE_remodelado=3*c+math.ceil(c/2))
 check(row==expected,'Conta da mescla C'+str(c));check(sum(row['parcelas'])==row['saldo'] and sum(row['parcelas_remodeladas'])==row['saldo_remodelado'],'Distribuição incorreta C'+str(c));check(all(1<=b<=a for a,b in zip(row['parcelas'],row['parcelas_remodeladas'])),'Função apagada/aumentada C'+str(c));check(row['devolucao']<=min(row['escolher'],2*c),'Devolução excede Melhorias/teto');check(row['parcelas'][1]<=min(2*c,3*c-P),'Cura excede teto')
check(m['resolucoes_mescla']==dict(CD=14,dano_ampliado=11,dano_resistido=6,PE_ampliado=8,PE_fluida=11,dano_fluida=5,dano_fluida_resistido=3),'Resolução da mescla divergente')
check(m['firmeza']==dict(C2_duas_categorias=dict(precos=[1,1],vagas=2,limite=2,saldo=4,PE_final=8),C2_tres_categorias_cabe=False,C3_tres_categorias=dict(precos=[2,2,2],vagas=3,limite=3,saldo=3),C2_guarda_e_oficios=dict(precos=[1,2],vagas=2,saldo=3),manobra=dict(bonus=4,rolagem=18,CD=14)),'Compras de Firmeza/Guarda divergentes')
check(m['restricoes']==dict(C3_melhorias=[2,3],C3_devolucoes=[3,2,0],C3_resultados=[7,6,4],ataque=6,acerto=18,dano=25,recuo_distancia=2.5,matriz_saldo=6,matriz_ataque=14,defesa=16,matriz_custo=9),'Contas das Restrições divergentes')
check(m['cancelamento']==dict(luz_custo=6,luz_PE_final=9,C1_saldo=2,C2_saldo=4,CD=12,rolagem=11,sem_Maestria=True,C1_PE_final=7,C2_PE_final=4,CE_nao_convertida=True),'Contas de efeito/cancelamento divergentes')
check(m['cancelamento']['rolagem']<m['cancelamento']['CD'],'Falha do cancelamento divergente');check(m['restricoes']['matriz_ataque']<m['restricoes']['defesa'],'Falha da Matriz divergente')
output=dict(etapa=88,contagens_M=data['totais_pontos'],contagens_P=data['totais_competencias'],evidencias_conferidas=checked,reclassificados=changed,competencias_parciais=['P14','P15','P20'],R53_intacta=not any('R53' in p for p in problems),decisao_Reserva_preservada=True,grupos_de_contas_conferidos=5,problemas=problems,limites='Integridade documental, contas explícitas e transições de cobertura; sem validação de aprendizagem ou equilíbrio.')
print(json.dumps(output,ensure_ascii=False,indent=2));sys.exit(bool(problems))
