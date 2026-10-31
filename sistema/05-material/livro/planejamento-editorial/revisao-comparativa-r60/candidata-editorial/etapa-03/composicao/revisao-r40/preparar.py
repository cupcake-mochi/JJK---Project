from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[1];R=B/'revisao-r40'
before=json.loads((R/'BASE-BLOCOS.json').read_text());texts=dict(before);reasons={}
paths={'bastiao','vanguarda','guia','emanador','evocador','incursor'}
def settext(k,s,why):
 if texts[k]!=s:texts[k]=s;reasons.setdefault(k,[]).append(why)
def rep(k,a,b,why):
 assert a in texts[k],(k,a)
 settext(k,texts[k].replace(a,b,1),why)
# Retirar a antecipação de habilidades de nível 11 antes das de nível 2.
k='incursor--inc-guarda';old=texts[k];cut=old.index('### Desaparecer no Percurso');late=old[cut:]
settext(k,old[:cut].rstrip(),'Nível 11 transferido para depois de todas as habilidades de nível 2 do Assassino.')
settext('incursor--inc-parkour',texts['incursor--inc-parkour']+'\n\n'+late,'Recebe as duas habilidades de nível 11 após Parkour, preservando integralmente seus procedimentos e exemplo.')
# Rajada é uma evolução do Corpo Treinado, apresentada após as habilidades iniciais.
k='incursor--inc-corpo';a=texts[k].index('### Rajada Marcial');z=texts[k].index('### Quebrar o Compasso');raj=texts[k][a:z].strip()
settext(k,texts[k][:a]+texts[k][z:],'Evolução de nível 7 transferida para depois de Recuperar a Base, mantendo juntas as habilidades de nível 2.')
raj=raj.replace('### Rajada Marcial a partir do nível 7','### Rajada Marcial').replace('Ao utilizar essa **Ação Bônus**,','A partir do **nível 7**, Corpo Treinado ganha esta melhoria. Ao utilizar a **Ação Bônus de Corpo Treinado**,',1)
rep('incursor--inc-base','### Guarda Marcial',raj+'\n\n### Guarda Marcial','Nome isolado no título; nível 7 e vínculo com Corpo Treinado explícitos no texto. Evolução posicionada antes do nível 11.')
# Evocador: concluir o catálogo inicial antes de apresentar as entradas do nível 7.
k='evocador--ev-aprimoramentos';a=texts[k].index('## Dificultar a Resistência');late=texts[k][a:]
settext(k,texts[k][:a].rstrip(),'Aprimoramento de nível 7 transferido para depois das intervenções de nível 2.')
settext('evocador--ev-preparacao',late+'\n\n'+texts['evocador--ev-preparacao'],'Dificultar a Resistência abre as opções de nível 7; o restante mantém a sequência original.')
# Habilidades por nível: título com nome, nível em metadado separado, texto intacto.
for k in list(texts):
 if k.split('--')[0] not in paths:continue
 t=texts[k]
 t=re.sub(r'^#{2,3} Nível (\d+) [—–-] (.+)$',lambda m:'## '+m[2]+'\n\n**Nível '+m[1]+'.**',t,flags=re.M)
 t=re.sub(r'^#{2,3} (.+) [—–-] nível (\d+)$',lambda m:'## '+m[1]+'\n\n**Nível '+m[2]+'.**',t,flags=re.M)
 # Vanguarda usava o nome da habilidade como abertura em negrito do parágrafo.
 def inlinelevel(m):
  level,name=m[1],m[2];heading='## '+name
  pre=t[:m.start()].rstrip()
  return ('**Nível '+level+'.**\n\n') if pre.endswith(heading) else heading+'\n\n**Nível '+level+'.**\n\n'
 t=re.sub(r'^\*\*Nível (\d+): ([^\n]+?)\.\*\*\s*',inlinelevel,t,flags=re.M)
 # Marcadores de produção que na verdade são habilidades.
 t=re.sub(r'^\*\*([^*\n]+)\*\*\n\n(?=\*\*Nível \d+)',r'## \1\n\n',t,flags=re.M)
 t=re.sub(r'^\*\*Nível (\d+)\.\*\* +',r'**Nível \1.**\n\n',t,flags=re.M)
 t=re.sub(r'^\*\*Nível (\d+) · ([^*]+)\*\*([, ]*)',lambda m:'**Nível '+m[1]+'.**\n\n**'+m[2].rstrip('.,')+'.**\n\n',t,flags=re.M)
 t=re.sub(r'^### (.+)\n\n(?=\*\*Nível \d+\.\*\*)',r'## \1\n\n',t,flags=re.M)
 settext(k,t,'Padronização editorial: nome da habilidade em título de entrada e nível em linha própria; subníveis de capacidades independentes corrigidos.')
rep('guia--guia-plano-conjunto','\n\nao usar Abrir Caminho','\n\nAo usar Abrir Caminho','Inicial maiúscula após separar o metadado do texto.')
# A abertura da Parceria é um agrupamento, não uma habilidade adicional.
rep('evocador--ev-parceria','## Abertura da Parceria\n\n**Nível 2.**\n\n','', 'Retirado agrupador redundante entre a apresentação e Entrada Ágil; cada habilidade recebe seu nível.')
# Níveis já estabelecidos pelas tabelas ou pelo grupo de origem.
explicit={
 'emanador--ema-familiares':{'Afinidade Técnica':7},
 'emanador--ema-condutor':{'Cadência Técnica':2},
 'evocador--ev-vinculo':{'Vínculo':2},
 'evocador--ev-principal':{},
 'evocador--ev-parceria':{'Entrada Ágil':2,'Treino de Combate':2,'Repertório de Parceria':2},
 'evocador--ev-multiplas-entrada':{'Manifestação em Grupo':2},
 'evocador--ev-multiplas-duplas':{'Aquisição em Duplas':2},
 'incursor--inc-fluidez-avancada':{'Passo Guardado':15},
 'incursor--inc-ritmo':{'Movimento Acrobático ampliado':23},
}
for k,hs in explicit.items():
 for h,lv in hs.items():
  pat=r'^#{2,3} '+re.escape(h)+r'\n\n';assert re.search(pat,texts[k],re.M),(k,h)
  settext(k,re.sub(pat,'## '+h+'\n\n**Nível '+str(lv)+'.**\n\n',texts[k],count=1,flags=re.M),'Nível explicitado a partir da progressão já existente; capacidade com a mesma hierarquia das demais.')
# Duas Atuações Básicas já está nomeada e atribuída ao nível 2 na tabela.
rep('evocador--ev-principal','**Duas básicas no seu turno · Uma invocação ativa.**','## Duas Atuações Básicas\n\n**Nível 2.**\n\n**Duas básicas no seu turno · Uma invocação ativa.**','Dar título à habilidade que a tabela já anuncia, conservando sua condição e regra.')
# Tabelas de progressão faltantes nas três Trilhas do Guia.
newtables={
 'guia--guia-arquiteto':[(2,'Obras de Apoio.'),(11,'Obra em Uso e Obras maiores.'),(19,'Obra de Emergência.'),(27,'Plano Construído.')],
 'guia--guia-analista':[(2,'Ler a Resposta.'),(11,'Apontar a Brecha.'),(19,'Rever a Leitura.'),(27,'Padrão Decifrado.')],
 'guia--guia-socorrista':[(2,'Cuidado Preparado.'),(11,'Tratar e Retomar.'),(19,'Ainda Há Tempo.'),(27,'Atendimento em Cadeia.')],
}
for k,rows in newtables.items():
 a=texts[k].index('\n\n## ')
 table='\n\n## Progressão da Trilha\n\n| Nível | Habilidade |\n|---|---|\n'+'\n'.join(f'| {lv} | {name} |' for lv,name in rows)
 settext(k,texts[k][:a]+table+texts[k][a:],'Tabela de consulta acrescentada com os níveis e nomes já presentes no texto da Trilha.')
# Cabeçalhos de progressão uniformes. A tabela conjunta do Batedor já cobre suas três rotas.
rootkeys={'bastiao--bas-bastiao','vanguarda--van-base','guia--guia','guia--guia-progressao','emanador--ema-base','evocador--evocador','incursor--inc-caminho'}
for k in list(texts):
 if k.split('--')[0] not in paths:continue
 t=texts[k];label='Progressão do Caminho' if k in rootkeys else 'Progressão da Trilha'
 t=re.sub(r'^## Progressão(?: do Caminho| da Trilha)?$', '## '+label,t,flags=re.M)
 t=re.sub(r'^\*\*(?:Habilidades da Estocada|Habilidades do Executor|Progressão do Guia)\*\*$', '## '+label,t,flags=re.M)
 if t.startswith('# ') and '| Nível |' in t and '## '+label not in t and k!='vanguarda--van-yumi':
  t=t.replace('| Nível |','## '+label+'\n\n| Nível |',1)
 t=t.replace('| Nível | Habilidades do Caminho |','| Nível | Habilidade |').replace('| Nível | Habilidades |','| Nível | Habilidade |')
 settext(k,t,'Cabeçalho de progressão e coluna de habilidades padronizados entre Caminhos e Trilhas.')
rep('vanguarda--van-base','| Característica | Valor |','## Características\n\n| Característica | Valor |','Cabeçalho de características como nos demais Caminhos.')
rep('guia--guia','## Características do Guia','## Características','Cabeçalho de características como nos demais Caminhos.')
rep('guia--guia','| | |','| Característica | Valor |','Cabeçalho da tabela de características preenchido, seguindo os demais Caminhos.')
# Navegação: índice com destinos distintos para origem e rota e acesso à Restrição.
for k in list(texts):
 if k.startswith('consulta--consulta-indice-') and '[Sem Técnica]' in texts[k]:
  rep(k,'[Sem Técnica](#rotas--rota-sem-tecnica)','[Sem Técnica (Origem)](#origens--origem-sem-tecnica)\n[Sem Técnica (rota e criação)](#rotas--rota-sem-tecnica)','Distinguir origem e procedimento de criação no índice.')
k=next(k for k,v in texts.items() if k.startswith('consulta--consulta-indice-') and '[Restrição](' in v)
t=texts[k];line=next(l for l in t.splitlines() if l.startswith('[Restrição]('));rep(k,line,line+'\n[Restrição Celestial](#origens--origem-restricao)\n[Restrição Celestial sem energia (criação)](#rotas--rota-marcial)','Índice passa a localizar a Origem e a criação de Katas do ramo sem energia.')
rep('vanguarda--van-feiticos','**Conclusões de feitiço**\n\n## Conclusões de feitiço','## Conclusões de feitiço','Retirado rótulo duplicado imediatamente acima do título da mesma habilidade.')
# Persistir antes/depois de cada bloco modificado, sem editar fontes congeladas.
rows=[{'id':f'R40-T{i:03d}','bloco':k,'antes':before[k],'depois':texts[k],'motivo':' '.join(dict.fromkeys(reasons[k])),'item':'Sumário, hierarquia e ordem de leitura — pedido do autor','altera_regras':False} for i,k in enumerate([k for k in before if before[k]!=texts[k]],1)]
(R/'ALTERACOES-TEXTO.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(R/'TEXTOS-PROPOSTOS.json').write_text(json.dumps(texts,ensure_ascii=False,indent=2)+'\n')
print(len(rows),'blocos')
