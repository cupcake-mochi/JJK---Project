#!/usr/bin/env python3
"""Confere documentação, fontes e contas de L7. Não valida equilíbrio ou aprendizagem."""
from pathlib import Path
import argparse,collections,hashlib,io,json,math,runpy,sys
from contextlib import redirect_stdout
ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--fontes',type=Path);ap.add_argument('--preparado',type=Path);ap.add_argument('--recalcular',action='store_true');args=ap.parse_args()
here=Path(__file__).absolute().parent;root=args.fontes or here.parents[1]
def path(rel):return args.preparado/rel if args.preparado and (args.preparado/rel).is_file() else root/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
s=json.loads((here/'estado-inicial.json').read_text());data=json.loads((here/'cobertura-atualizada.json').read_text());prior=json.loads(path(s['cobertura_anterior']).read_text());problems=[]
def check(ok,msg):
 if not ok:problems.append(msg)
changed=['M124','M129','P14','P15'];checked=0
for group,count in [('pontos',130),('competencias',20)]:
 before={r['id']:r for r in prior[group]};check(len(data[group])==len({r['id'] for r in data[group]})==count,'IDs duplicados/ausentes: '+group);check({r['id'] for r in data[group]}==set(before),'Inventário alterado: '+group)
 for r in data[group]:
  old=before[r['id']];excluded={'evidencias'}
  if r['id'] in changed:
   field='falta' if group=='pontos' else 'restante';check(old['estado']=='P' and r['estado']=='E' and r[field]==r['lote']=='—','Transição indevida: '+r['id']);excluded|={'estado','presente',field,'lote'}
  check({k:v for k,v in r.items() if k not in excluded}=={k:v for k,v in old.items() if k not in excluded},'Escopo alterado: '+r['id'])
  for e in r['evidencias']:
   p=path(e['arquivo']);check(p.is_file(),'Fonte ausente: '+e['arquivo'])
   if not p.is_file():continue
   check(sha(p)==e['sha256'],'Fonte alterada: '+e['arquivo']);lines=p.read_text().splitlines();valid=1<=e['inicio']<=e['fim']<=len(lines);check(valid,'Intervalo inválido: '+e['arquivo'])
   if valid:check(lines[e['inicio']-1].lstrip('# ').strip()==e['titulo'],'Título divergente: '+e['arquivo'])
   checked+=1
check(dict(collections.Counter(r['estado'] for r in data['pontos']))=={'E':129,'P':1} and data['totais_pontos']=={'E':129,'P':1,'L':0},'Totais M divergentes')
check(dict(collections.Counter(r['estado'] for r in data['competencias']))==data['totais_competencias']=={'E':19,'P':1},'Totais P divergentes')
check([r['id'] for r in data['pontos'] if r['estado']=='P']==['M051'],'Pontos parciais divergentes')
check([r['id'] for r in data['competencias'] if r['estado']=='P']==['P20'],'Competências parciais divergentes')
check(all(not r['aprendizagem_observada'] for r in data['competencias']),'Aprendizagem indevidamente declarada')
for b in data['lotes']:
 old=next(x for x in prior['lotes'] if x['id']==b['id']);expected={**old,'estado':'entregue'} if b['id']=='L7' else old;check(b==expected,'Lote alterado fora de escopo: '+b['id'])
for field in ['fonte_R53','copia_R53']:check(sha(Path(s[field]))==s['R53_sha256'],'R53 alterada: '+field)
g92='06 - Redacao do Guia/92-reserva-condensada-proposta-e-comparacao.md';check(sha(path(g92))==s['manifesto_anterior'][g92],'G92 alterada: decisão de Reserva deve permanecer')
x=json.loads((here/'resultados.json').read_text());check(len(x['perfis'])==24 and len(x['referencias'])==144,'Recortes divergentes');check(len(x['composicoes'])==8,'Composições divergentes')
for p in x['perfis']:
 check(max(p['atributos'])<=6,'Atributo acima do teto');check(p['PE']>=2*3*p['classe'],'Reserva não comporta comparação de duas conjurações')
for r in x['referencias']:check(0<=r['sobrevive'][1]<=r['sobrevive'][0]<=1+1e-8,'Sobrevivência inválida')
for r in x['composicoes']:
 check(len(r['resultados'])==3,'Número de conjuntos divergente')
 for z in r['resultados']:check(0<=z['apoio_ativo']<=z['pelo_menos_um_ativo']+1e-8,'Apoio sem participante ativo')
for r in x['concentracao_de_ataques']:
 for z in r['resultados']:check(z['derrotado']<=z['zero_PV']+1e-8,'Derrota confundida com queda')
if args.recalcular:
 with redirect_stdout(io.StringIO()):fresh=runpy.run_path(str(here/'calcular.py'))['out']
 check(fresh==x,'Resultados armazenados não correspondem à reprodução')
m=json.loads((here/'contas.json').read_text())
q=m['socorro'];check(q['tratamento_insistir']==min(math.ceil(q['maximo']/3),15*q['classe'])==46,'Insistir divergente');check(q['tratamento_aguentar']==math.ceil(q['maximo']/4)==35,'Aguentar divergente');check(q['janela']==3-q['sequelas_antes']==2,'Janela divergente');check(q['cura1']==sum(q['dados_cura1'])==36 and q['cura2']==sum(q['dados_cura2'])==10,'Curas divergentes');check(q['PV_final']==min(q['cura1']+q['cura2'],q['maximo'])==46 and q['sequelas_final']==2,'Retorno divergente');check(q['PE_Guia_final']==75-12==63 and q['PE_Bastiao_final']==60-6==54,'Gastos do socorro divergentes');check(q['cura1']<q['tratamento_insistir']<=q['cura1']+q['cura2'],'Parcial de socorro divergente')
z=m['inimigos'];check(z['Haru_vida']==280 and z['Haru_integridade']==140,'Haru divergente');check(z['Vigia_vida']+z['Tessa_vida']==200,'Dupla divergente');check(z['Fita_C2_dados']==6-1-2==3 and z['Fita_C4_dados']==12-2-4==6,'Montagem Fita divergente');check(z['Remendo_C4_dados']==min(12-4,2*4)==8,'Montagem de cura divergente');check(z['Haru_PE_apos_Fita4']==26-12==14,'Custo Fita divergente');check(z['Fita4_PE_estagio2']==12+4==16 and z['Impulso_PE_estagio2']==3+1==4,'Integridade não modifica custo');check(z['Tessa_PE_apos_2curas']==26-2*12==2,'Reserva cura divergente');check(z['fecho_Defesa']==18 and z['fecho_PV']==5,'Objeto divergente')
d=m['doenca'];check(d['primeira_crise']==d['contato']+6==14 and d['fim_maximo']==d['contato']+48==56,'Relógio divergente');check(d['tentativa2_inicio']==d['tentativa1_fim']+6==23 and d['tentativa2_fim']==25,'Retomada divergente');check(d['horas_trabalho']==(d['tentativa1_fim']-d['tentativa1_inicio'])+(d['tentativa2_fim']-d['tentativa2_inicio'])==4,'Trabalho divergente');check(d['PV_final']==40-3-4==33,'Dano doença divergente');check(d['tentativa1_total']<14<=d['tentativa2_total'],'Resultado de atendimento divergente');check(d['sucessos_naturais']==[20,26] and d['tentativa2_fim']<26,'Saída natural/tratamento divergente');check(d['crises_sem_termino_antecipado']==list(range(14,56,6)),'Crise extra no término máximo')
output=dict(etapa=90,contagens_M=data['totais_pontos'],contagens_P=data['totais_competencias'],evidencias_conferidas=checked,reclassificados=changed,pontos_parciais=['M051'],competencias_parciais=['P20'],R53_intacta=not any('R53' in p for p in problems),decisao_Reserva_preservada=not any('G92' in p for p in problems),perfis=24,curvas=144,composicoes_condicionais=8,verificacoes_numericas=len(x['verificacoes']),recalculado=args.recalcular,problemas=problems,limites='Integridade documental, contas e recortes condicionais; sem validação de aprendizagem ou equilíbrio.')
print(json.dumps(output,ensure_ascii=False,indent=2));sys.exit(bool(problems))
