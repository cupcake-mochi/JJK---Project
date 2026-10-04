from pathlib import Path
import re,json,math,hashlib
R=Path('/media/mizuki/HD Externo II/Claude/Claude 2')
P=R/'sistema/05-material/livro/manual/40-fundamento.md'
t=P.read_text()
section=t[t.index('**Números da montagem**'):t.index('A coluna **Nível**')]
rows=[]
for line in section.splitlines():
    cells=[c.strip().replace('**','') for c in line.strip('|').split('|')]
    if len(cells)==11 and cells[0].isdigit():
        c,n,pts,l,m,p,r=map(int,cells[:7]); rows.append(dict(classe=c,nivel=n,pontos=pts,leve=l,media=m,pesada=p,devolucao_maxima=r))
assert len(rows)==7
turnos=R/'sistema/05-material/livro/planejamento-editorial/regras-basicas/lote-01/TESTES-E-TURNOS.md'
segundos_candidata=int(re.search(r'rodadas de (\d+) segundos',turnos.read_text()).group(1))
assert segundos_candidata==6
rodadas_candidata=60//segundos_candidata
segundos_historico=10
rodadas_historico=60//segundos_historico
out={'fonte':str(P),'sha256_fonte':hashlib.sha256(P.read_bytes()).hexdigest(),'escopo':'Comparação descritiva de extremos, sem concluir balanceamento de área ou persistência. Média matemática não arredondada; nenhum bônus de atributos/caminhos, resistência, RD, crítico ou desconto de Família. Áreas: todos falham no TR; Fica após primeira aplicação tem metade dos dados arredondada para baixo.','regras_candidatas':['Dano direto comprado: 3C; Liberação: 4C.','Área replica dados por alvo sem dividir; esse total agregado não é teto.','Cura final no máximo 2C; Onda de cura no máximo 3C−Pesada.','Fica: aplicação inicial inteira e depois meia quantidade, uma aplicação de dano por criatura por rodada, concentração e 1 minuto. Duração publicada histórica: 10s/rodada, 6 rodadas/minuto. Candidata de Testes e Turnos: 6s/rodada, 10 rodadas/minuto; ambos os regimes são rotulados.'],'areas':[],'fica':[],'cura':[],'liberacao':[],'checagens':[]}
for row in rows:
    c=row['classe']; B=row['pontos']; L=row['leve']; M=row['media']; Pz=row['pesada']; T=4*c
    assert B==3*c and M==c and L==math.ceil(c/2) and Pz==math.ceil(1.5*c)
    for n in (1,2,4,6):
        for label,d in [('explosao_sem_restricao',B-L),('explosao_com_uma_restricao_media_efetiva',B)]:
            out['areas'].append({'classe':c,'alvos':n,'perfil':label,'dados_por_alvo':d,'dados_total_agregado':n*d,'media_total_d8':4.5*n*d,'antigo_teto_global':T,'excede_antigo_teto_global':n*d>T})
    # Fica custa Media e Explosao custa Leve; duas restricoes reais M+L cobrem ambas.
    for label,d in [('explosao_fica_sem_restricao',B-L-M),('explosao_fica_com_restricoes_independentes_media_e_leve',B)]:
        for rounds in (1,3,6,10):
            total=d+(rounds-1)*(d//2)
            out['fica'].append({'classe':c,'perfil':label,'rodadas':rounds,'valido_na_publicacao_historica':rounds<=rodadas_historico,'valido_na_candidata':rounds<=rodadas_candidata,'dados_iniciais':d,'dados_por_pulso':d//2,'dados_total_por_alvo':total,'media_total_d8_por_alvo':4.5*total,'multiplo_de_dano_base':round(total/d,3) if d else 0})
    for shape,cf,cap in [('Cura',M,2*c),('Onda',Pz,B-Pz)]:
        for label,r in [('sem_restricao',0),('uma_leve',L),('uma_media',M),('duas_medias_independentes',2*M)]:
            before=B-cf+min(r,cf,2*c)
            after=min(before,cap)
            out['cura'].append({'classe':c,'forma':shape,'perfil':label,'custo_forma':cf,'dados_por_formula_sem_teto':before,'dados_candidata_com_teto':after,'teto_da_tabela':cap,'media_sem_teto':4.5*before,'media_com_teto':4.5*after})
    if c>=3:
        out['liberacao'].append({'classe':c,'linha_sem_restricao_redundante':4*c-L,'linha_com_atrasar_historico':4*c,'diferenca_dados':L,'pe':math.ceil(3*c*1.5)})
        assert 4*c-L<=4*c
out['checagens']=[{'nome':'7 linhas da tabela dona lidas por coluna','passou':len(rows)==7},{'nome':'escadas preço coerentes em todas as classes','passou':True},{'nome':'todos os resultados candidatos de Cura/Onda respeitam tabelas históricas','passou':all(x['dados_candidata_com_teto']<=x['teto_da_tabela'] for x in out['cura'])},{'nome':'Fica10 rodadas cabe na candidata6s e não no regimehistórico10s','passou':all(x['valido_na_candidata'] and not x['valido_na_publicacao_historica'] for x in out['fica'] if x['rodadas']==10)},{'nome':'explosão com reembolso tem 3C por alvo em todas as classes','passou':all(x['dados_por_alvo']==3*x['classe'] for x in out['areas'] if x['perfil'].endswith('efetiva'))}]
Path('/tmp/fundamento-riscos-numericos.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f"{len(out['areas'])} cenários de área; {len(out['fica'])} cenários de Fica; {len(out['cura'])} cenários de cura; {len(out['liberacao'])} cenários de Liberação.")
for c in (1,3,5,7):
    row=rows[c-1]; d=3*c
    print(f"Classe {c}: área com reembolso (1/2/4/6 alvos) = {[n*d for n in (1,2,4,6)]}d8 total; Fica cheio (1/3/6/10) = {[d+(n-1)*(d//2) for n in (1,3,6,10)]}d8/alvo; Cura {2*c}d8 e Onda {d-row['pesada']}d8.")
print('10 rodadas de Fica cabem na candidata de 6 segundos/rodada; no histórico de 10 segundos/rodada eram 6. Ambas as faixas são rotuladas no JSON.')
print('Todos os 5 checks:',all(x['passou'] for x in out['checagens']))
