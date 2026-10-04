from fractions import Fraction
from pathlib import Path
import re,json,hashlib
R=Path('/media/mizuki/HD Externo II/Claude/Claude 2')
source=R/'sistema/05-material/livro/manual/40-fundamento.md'
t=source.read_text(); sec=t[t.index('**Números da montagem**'):t.index('A coluna **Nível**')]
classes=[]
for line in sec.splitlines():
    row=[x.strip().replace('**','') for x in line.strip('|').split('|')]
    if len(row)==11 and row[0].isdigit():
        classes.append(tuple(map(int,row[:7])))
assert len(classes)==7
rows=[]
for c,n,B,L,M,P,Rm in classes:
 for threshold in (6,11,16):
  phit=sum(x>=threshold or x==20 for x in range(1,21))/20
  for name,cost in [('preco_normal',M),('mira_livre',max(1,M-L)),('reembolso_real_integral',0)]:
   D=B-cost
   normal=sum((2*B if d==20 else B if d>=threshold else 0) for d in range(1,21))/20
   certeza=sum((2*D if d==20 else D if d>=threshold else D//2) for d in range(1,21))/20
   # P(falhaTR) = P(acerto), apenas para confronto normalizado. Não equivale
   # a um inimigo real com Defesa e bônusTR correlacionados.
   tr=B*phit+(B//2)*(1-phit)
   rows.append(dict(classe=c,perfil=name,acerto=phit,dados_normal=B,dados_certeiro=D,dano_medio_normal=normal*4.5,dano_medio_certeiro=certeza*4.5,dano_medio_TR_padrao_metade_dados=tr*4.5,comparacao_probabilidades_iguais=True))
constant=[]
for threshold in (6,11,16):
 D=8
 p=sum(x>=threshold for x in range(1,21))/20
 attack=sum((2*D if x==20 else D if x>=threshold else 0) for x in range(1,21))/20
 certeiro=sum((2*D if x==20 else D if x>=threshold else D//2) for x in range(1,21))/20
 tr=sum((D if x<=int(p*20) else D//2) for x in range(1,21))/20
 constant.append({'acerto_e_falha_TR_normalizados':p,'dados_fixos':D,'ataque_em_dados_medios':attack,'certeiro_em_dados_medios':certeiro,'TR_em_dados_medios':tr})
out={'fonte_precos':str(source),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'metodo':'Enumeração exata dos 20 resultados do acerto;20naturalacertaedobra. Um ataque, semBloquear/VD/bônus externos; TRcomparado comP(falha)=P(acerto), sem afirmar que alvosreais têm essa relação. Certeiro errafinal causa floor(D/2)d8, acerto conserva crítico. TRpadrão nesta simulação também reduzquantidade de dados, nãoresultado. Tudo representa dano antesdedéfesas.','mesmos_dados_sem_custos':constant,'montagens':rows,'limitacoes':['Não mede Bloquear, cujo uso é escolhido após conhecer acerto.','Não certificaCDvsDefesa ou equilíbrio do catálogo.','Média de dados×4,5 é exata; resultadosfracionários são médias, não rolagens.','Reembolso integral requer desvantagemreal e não ébenefício semcusto.','Se TRda candidata dividir resultadorolado, o colunaTR precisarecálculo.']}
Path('/tmp/fundamento-certeiro-resultados.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('63 comparações com orçamento; 3 com mesmosdados.')
for r in rows:
 if r['classe']==5 and r['perfil']=='preco_normal': print(r)
