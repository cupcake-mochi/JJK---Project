#!/usr/bin/env python3
"""Confere os exemplos de L1. --salvar grava somente resultados.json nesta pasta."""
from pathlib import Path
from datetime import datetime,timedelta
import argparse,collections,hashlib,json,re,sys
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--fontes',type=Path,help='Raiz de produção para preparar/conferir antes da instalação.')
ap.add_argument('--preparado',type=Path,help='Sobreposição com arquivos preparados, sem alterar a raiz.')
ap.add_argument('--salvar',action='store_true')
a=ap.parse_args();here=Path(__file__).absolute().parent
root=a.fontes or here.parents[1]
def path(rel):
    if a.preparado and (a.preparado/rel).is_file():return a.preparado/rel
    return root/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((here/'estado-inicial.json').read_text())
data=json.loads((here/'cobertura-atualizada.json').read_text())
original=json.loads(path('04 - Planejamento/apoio-auditoria-cobertura/cobertura.json').read_text())
problems=[]
def check(ok,message):
    if not ok:problems.append(message)
text=path('06 - Redacao do Guia/82-testes-trabalho-em-grupo-e-iniciativa.md').read_text()
group=[]
for name,d,b,total,result in re.findall(r'^\| (Aoi|Nao|Haru|Tomo|Emi) \| (\d+) \| \+(\d+) \| (\d+) \| (Sucesso|Falha) \|$',text,re.M):
    d,b,total=map(int,(d,b,total));check(d+b==total,f'Furtividade de {name}: soma divergente.');check((total>=14)==(result=='Sucesso'),f'Furtividade de {name}: resultado divergente.')
    group.append(dict(nome=name,d20=d,bonus=b,total=total,sucesso=total>=14))
check(len(group)==5,'Faltam participantes do quadro de travessia.')
successes=sum(x['sucesso'] for x in group);limit=(len(group)+1)//2
check(successes==3 and limit==3,'Resultado coletivo principal divergente.')
alternate=[dict(x) for x in group]
for x in alternate:
    if x['nome']=='Emi':x.update(d20=9,total=9+x['bonus'],sucesso=9+x['bonus']>=14)
alt=sum(x['sucesso'] for x in alternate)
check(alt==2 and alt+1==limit,'Ramo de Contribuição Decisiva divergente.')
four=[x for x in group if x['nome']!='Emi'];check(sum(x['sucesso'] for x in four)==2 and (len(four)+1)//2==2,'Metade de quatro participantes divergente.')
init=[]
for name,owner,dex,die,total in re.findall(r'^\| (Haste|Aoi|Nao|Trinco|Dobra) \| (Mestre, inimigo|Jogadora|Jogador) \| (\d+) \| (\d+) \| (\d+) \|$',text,re.M):
    dex,die,total=map(int,(dex,die,total));check(dex+die==total,f'Iniciativa de {name}: soma divergente.')
    init.append(dict(nome=name,controle=owner,destreza=dex,d20=die,total=total))
check(len(init)==5,'Faltam participantes do quadro de iniciativa.')
choice={'Haste':0,'Aoi':0,'Nao':1,'Trinco':0,'Dobra':1}
ordered=sorted(init,key=lambda x:(-x['total'],-x['destreza'],x['controle']=='Mestre, inimigo',choice[x['nome']]))
order=[x['nome'] for x in ordered]
check(order==['Haste','Aoi','Nao','Trinco','Dobra'],'Critérios de iniciativa ou escolhas registradas divergentes.')
start=datetime(2026,10,26,17,40);normal=start+timedelta(minutes=10);cost=normal+timedelta(minutes=20)
check(normal.strftime('%Hh%M')=='17h50' and cost.strftime('%Hh%M')=='18h10','Horários divergentes.')
help_total=max(9,15)+4
check(9+4<14 and 10+4==14 and help_total==19,'Investigação e ajuda divergentes.')

check(len(data['pontos'])==130 and len({x['id'] for x in data['pontos']})==130,'IDs M duplicados/ausentes.')
check(len(data['competencias'])==20,'Competências divergentes.')
check(dict(collections.Counter(x['estado'] for x in data['pontos']))=={'E':96,'P':33,'L':1},'Contagem de pontos divergente.')
check(dict(collections.Counter(x['estado'] for x in data['competencias']))=={'E':16,'P':4},'Contagem de competências divergente.')
before={x['id']:x for x in original['pontos']};changed=[]
for row in data['pontos']:
    old=before[row['id']]
    check(all(row[k]==old[k] for k in ['assunto','natureza','capitulo','previsto','discussao','pagina_inventario']),f"Escopo alterado: {row['id']}")
    if row['estado']!=old['estado']:changed.append(row['id'])
check(changed==['M010','M014','M128'],'Reclassificação além do lote L1.')
check(sum(len(x['pontos']) for x in data['lotes'])==34,'Lacunas restantes divergentes.')
for row in data['pontos']+data['competencias']:
    for e in row['evidencias']:
        p=path(e['arquivo']);check(p.is_file(),f"Fonte ausente: {e['arquivo']}")
        if not p.is_file():continue
        check(sha(p)==e['sha256'],f"Fonte alterada: {e['arquivo']}")
        lines=p.read_text().splitlines();valid=1<=e['inicio']<=e['fim']<=len(lines);check(valid,f"Trecho inválido: {e['arquivo']}")
        if valid:check(lines[e['inicio']-1].lstrip('# ').strip()==e['titulo'],f"Título divergente: {e['arquivo']}")
for field in ['fonte_R53','copia_R53']:check(sha(Path(state[field]))==state['R53_sha256'],f'R53 alterada: {field}')
output=dict(etapa=81,arquivo={'inicio':'17h40','fim_normal':normal.strftime('%Hh%M'),'fim_com_custo':cost.strftime('%Hh%M'),'custo_aceito_minutos':30,'custo_recusado_minutos':10,'dado_falho_total':13,'ajuda_total':help_total},grupo={'participantes':group,'limiar':limit,'sucessos':successes,'ramo_alternativo_sucessos':alt,'com_contribuicao_decisiva':alt+1,'quatro_participantes_limiar':2},iniciativa={'participantes':init,'ordem':order},reclassificados=changed,contagens_M=data['totais_pontos'],contagens_P=data['totais_competencias'],problemas=problems,limites='Conferência documental e aritmética de exemplos fixos, não simulação de combate, validação de aprendizagem ou teste humano.')
if a.salvar:(here/'resultados.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(output,ensure_ascii=False,indent=2));sys.exit(bool(problems))
