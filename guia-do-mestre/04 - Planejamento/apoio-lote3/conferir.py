#!/usr/bin/env python3
"""Confere exemplos e cobertura de L3. --salvar escreve só resultados.json nesta pasta."""
from pathlib import Path
import argparse,collections,hashlib,json,re,sys
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--fontes',type=Path);ap.add_argument('--preparado',type=Path);ap.add_argument('--salvar',action='store_true')
a=ap.parse_args();here=Path(__file__).absolute().parent;root=a.fontes or here.parents[1]
def path(rel):return a.preparado/rel if a.preparado and (a.preparado/rel).is_file() else root/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((here/'estado-inicial.json').read_text());data=json.loads((here/'cobertura-atualizada.json').read_text());before=json.loads(path(state['cobertura_anterior']).read_text());problems=[]
def check(ok,msg):
 if not ok:problems.append(msg)
text=path('06 - Redacao do Guia/83-perceber-procurar-e-interpretar-sinais.md').read_text()
rows=[r.strip('|').strip().split('|') for r in text.splitlines() if r.startswith('|')]
rows=[[c.strip() for c in r] for r in rows]
def row(starts):
 hits=[r for r in rows if r[0].startswith(starts)];check(len(hits)==1,'Linha ausente/duplicada: '+starts);return hits[0] if len(hits)==1 else []
observers=[]
for name,expect,located in [('Vigia,',14,False),('Sora,',17,True),('Operadora,',13,False)]:
 r=row(name)
 if not r:continue
 m=re.fullmatch(r'(\d+) \+ (\d+)(?: − (\d+))? = (\d+)',r[2]);check(bool(m),'CD não reconhecida: '+name)
 if not m:continue
 base,bonus,penalty,total=[int(x or 0) for x in m.groups()];calculated=base+bonus-penalty
 check(calculated==total==expect,'CD incorreta: '+name);check((16<calculated)==located,'Ocultação incorreta: '+name)
 observers.append(dict(observador=name.rstrip(','),cd=total,localiza=16<total))
none=row('Funcionário na sala');check(none and none[2]=='Sem comparação','Observador sem acesso recebeu CD.')
check(11+5==16 and 12+4>=16 and 11+4<16,'Busca ativa divergente.')
check(not 16<(10+6) and 16<(10+7),'Empate de novo observador divergente.')
check(3*2==6 and 4.5<=6,'Percepção de Contorno divergente.')
energy=[]
for starts,furt,expected,found in [('Feiticeiro a 9 m',16,18,True),('Outra criatura a 15 m',19,19,False),('Ferramenta no chão a 6 m',None,18,True)]:
 r=row(starts)
 if not r:continue
 m=re.search(r'\*\*(\d+)\*\*',r[2]);check(bool(m),'CD de energia não reconhecida: '+starts)
 if not m:continue
 cd=int(m.group(1));calc=max(18,furt or 0)
 check(cd==calc==expected,'Interferência incorreta: '+starts);check((18>=cd)==found,'Busca energética incorreta: '+starts)
 energy.append(dict(fonte=starts,furtividade=furt,interferencia=18,cd=cd,localiza=18>=cd))
blocked=row('Fonte a 4,5 m');check(blocked and 'Sem teste' in blocked[2],'Obstáculo virou CD.')
memory=[r for r in rows if r[0].startswith('“Qual porta') or r[0].startswith('“O que ele disse') or r[0].startswith('“O que havia')]
check(len(memory)==3,'Quantidade de perguntas da memória divergente.')
check('##### Memória Testemunha' in Path(state['fonte_R53']).read_text(),'Capacidade atual não encontrada na R53.')
check('Lembrança Retomada' not in text,'Nome histórico usado como capacidade no manuscrito.')
check(9+5==14 and 8+5<14,'Ler o Ambiente divergente.')
check(10+4==14 and 9+4<14,'Intuição divergente.')
check(8+6>=14 and 11+6>=14,'Pulso distante divergente.')
check(8+6==14,'Assinatura divergente.')

check(len(data['pontos'])==130 and len({x['id'] for x in data['pontos']})==130,'IDs M duplicados/ausentes.')
check(len(data['competencias'])==20,'Competências divergentes.')
check(dict(collections.Counter(x['estado'] for x in data['pontos']))=={'E':101,'P':28,'L':1},'Contagem de pontos divergente.')
check(dict(collections.Counter(x['estado'] for x in data['competencias']))=={'E':16,'P':4},'Contagem de competências divergente.')
old={x['id']:x for x in before['pontos']};changed=[]
for r in data['pontos']:
 prev=old[r['id']]
 check(all(r[k]==prev[k] for k in ['assunto','natureza','capitulo','previsto','discussao','pagina_inventario']),f"Escopo alterado: {r['id']}")
 if r['estado']!=prev['estado']:changed.append(r['id'])
check(changed==['M025','M026','M027','M028','M029'],'Reclassificação além de L3.')
check(sum(len(x['pontos']) for x in data['lotes'])==29,'Pendências restantes divergentes.')
for r in data['pontos']+data['competencias']:
 for e in r['evidencias']:
  p=path(e['arquivo']);check(p.is_file(),f"Fonte ausente: {e['arquivo']}")
  if not p.is_file():continue
  check(sha(p)==e['sha256'],f"Fonte alterada: {e['arquivo']}");lines=p.read_text().splitlines();valid=1<=e['inicio']<=e['fim']<=len(lines);check(valid,f"Trecho inválido: {e['arquivo']}")
  if valid:check(lines[e['inicio']-1].lstrip('# ').strip()==e['titulo'],f"Título divergente: {e['arquivo']}")
for field in ['fonte_R53','copia_R53']:check(sha(Path(state[field]))==state['R53_sha256'],'R53 alterada: '+field)
output=dict(etapa=82,esconder={'total':16,'observadores':observers,'busca_ativa':{'sucesso':12+4,'falha':11+4},'novo_observador':{'cd16_localiza':False,'cd17_localiza':True}},contorno={'maestria':2,'alcance_m':6,'alvo_m':4.5},ler_ambiente={'cd':14,'sucesso':14,'falha':13,'sem_informacao':'conserva ação e uso; sem dado'},intuicao={'cd':14,'sucesso':14,'falha':13},memoria={'nome_atual':'Memória Testemunha','minutos':1,'perguntas':len(memory),'uso':'diário, gasto ao iniciar'},energia={'rolagem':18,'fontes':energy,'bloqueada':'posição não revelada','sem_interferencia':{'ocultas_cd':[16,19],'ferramenta':'sem dado após gastar ação'}},pulso={'cd':14,'resultados':[14,17],'informacao':'mesma pista do subsolo'},assinatura={'cd':14,'resultado':14,'requisito':'referência confiável e sinal acessível'},reclassificados=changed,contagens_M=data['totais_pontos'],contagens_P=data['totais_competencias'],problemas=problems,limites='Conferência documental e aritmética de casos fixos; não simulação de combate, validação de aprendizagem ou teste humano.')
if a.salvar:(here/'resultados.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(output,ensure_ascii=False,indent=2));sys.exit(bool(problems))
