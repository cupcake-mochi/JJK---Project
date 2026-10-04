from pathlib import Path
import hashlib,json,difflib
P=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial');B=P/'dano-e-recuperacao/lote-final';E=B/'evidencias';current=B/'DANO-E-RECUPERACAO.md';old=E/'R03-TEXTO-LIDO-MAXIMA.md';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();a=old.read_text();b=current.read_text();checks=[]
def ck(n,x,y=True):
 checks.append({'caso':n,'obtido':x,'esperado':y,'ok':x==y})
 if x!=y:raise AssertionError(n)
expected=a.replace(' **Projetar Energia causa dano de Força.**','').replace('arredondada para baixo, salvo uma regra própria de sua ficha.','arredondada para baixo, com mínimo 1 quando a vida máxima for positiva, salvo uma regra própria de sua ficha.').replace('## Incapacitado','## Guarda Aberta').replace('ficar Incapacitado ou Inconsciente','ficar com a Guarda Aberta ou Inconsciente').replace('um inimigo Incapacitado','um inimigo com a Guarda Aberta').replace('e Incapacitado continua','e Guarda Aberta continua')
ck('Diff completo limitado às seis substituições lidas',b,expected)
ck('Efeito GuardaAberta preservado','Você **não pode Bloquear**. Ataques corpo a corpo com arma ou desarmados **que acertarem você** são críticos. Ataques à distância e de conjuração não ganham crítico por essa condição; um feitiço de Toque continua sendo conjuração.' in b)
ck('Fórmula dos personagens preservada','Integridade máxima do personagem = 20 + (Essência + 5) × (nível − 1).' in b)
for hp in range(1,401):
 value=max(1,hp//2);ck(f'NPC vida{hp}: Integridade positiva',value>=1);ck(f'NPC vida{hp}: só1PV difere da metade',value-hp//2,1 if hp==1 else 0)
ck('Exceção de ficha conservada','salvo uma regra própria de sua ficha' in b)
# Releitura dos quatro fechamentos no R03; o quinto está no dono R15 e foi confirmado pela raiz.
for name,parts in [
 ('R03-IM02 queda fora de iniciativa',['Se a queda ocorrer fora de combate','primeira']),
 ('R03-IM03 apósDerrota',['converta o tratamento acumulado em vida','recuperar reservas não devolve sua participação naquela cena','Ao sair da derrota, recebe uma Sequela']),
 ('R03-IM04 descanso longo',['Concluir um descanso longo também encerra a inconsciência causada pela derrota','desde que as duas reservas voltem a pelo menos 1']),
 ('R03-IM05 atendimento',['até **1,5 m**, com acesso físico ao alvo','uma mão livre e meios adequados'])]:
 ck(name,all(x in b for x in parts))
g=P/'caminhos/guia/lote-01/GUIA.md';txt=g.read_text();ck('R03-IM01 exceçãoGUIA38','Enquanto o aliado ainda estiver **Morrendo**, esta cura encerra a queda mesmo abaixo do limiar normal de recuperação.' in txt and 'Ela não permite voltar à cena depois de **Derrotado**.' in txt)
r=json.loads((g.parent/'evidencias/REVISAO-INDEPENDENTE-GUIA38.json').read_text());gpre=P/'consolidacao/lote-01/migracao-nomes/antes'/g.relative_to(P)
segment=lambda text:text.split('## Nível 19 — Ainda Há Tempo',1)[1].split('## Nível 27',1)[0]
ck('GUIA38 recebeu revisão independente da raiz antes dos nomes',r['revisor']=='/root' and r['sha256_texto']==sha(gpre))
ck('GUIA38 parágrafo/requisitos idênticos após nomes',segment(txt),segment(gpre.read_text()))

# Evitar registrar dois manuscritos inteiros dentro de cada comparação positiva.
checks[0]['obtido']='Texto atual igual ao snapshot após seis substituições documentadas.';checks[0]['esperado']='Texto atual igual ao snapshot após seis substituições documentadas.'
report={'ok':True,'sha256_texto':sha(current),'snapshot_integral_previo':sha(old),'revisor':'/root/maxima','escopo':'Releitura localizada após revisão integral de20 blocos; delta completo conferido contra snapshot. Não declara nova leitura integral.','resolucao_achados':'Cinco achados resolvidos; GUIA38 tem confirmação independente da raiz porque maxima é autor do Guia.','verificacoes':len(checks),'casos':checks,'mudancas':['Retirada da referência a Projetar Energia do tipoForça, conservando definição e regra no dono.','NomeGuardaAberta substituiIncapacitado em título, contenção e exemplo; efeitos idênticos.','DR31 mínimo1 para NPC com PV máximo positivo; somente NPC1PV muda frente à metade arredondada.'],'limites':['Modelo matemático e comparação documental; não é playtest ou teste humano.','PDF/visual cabem à raiz.','A aprovação da mecânica original continua condicionada aos riscos descritos no parecer integral; renome e correção de borda não eliminam a necessidade de teste de mesa.']}
(E/'REVISAO-INDEPENDENTE-FINAL-MAXIMA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');(E/'DELTA-FINAL-MAXIMA.diff').write_text(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='snapshot-lido',tofile='R03-final')))
(E/'REVISAO-INDEPENDENTE-FINAL-MAXIMA.md').write_text('# Fechamento independente de R03\n\nTexto: `'+sha(current)+'`. Snapshot integral: `'+sha(old)+'`.\n\n'+report['escopo']+'\n\n'+report['resolucao_achados']+'\n\nGuarda Aberta conserva exatamente os efeitos: não Bloquear, críticos nos acertos corpo a corpo com arma/desarmados, sem crítico extra em tiro/conjuração. O término de Agarrado e o exemplo apenas adotam o nome. A retirada de Projetar Energia evita duplicação do dono, sem mudar Força.\n\nDR31 foi conferida em NPCs com1–400PV: apenas o caso1PV muda (Integridade0→1); os demais conservam a metade para baixo. A fórmula dos personagens não mudou. Foram executadas'+str(len(checks))+' verificações, incluindo comparação exata do delta e fechamento dos achados anteriores. Nenhum novo bloqueador identificado no escopo.\n\n'+ '\n'.join('- '+x for x in report['limites'])+'\n')
print(json.dumps({'ok':True,'hash':sha(current),'verificacoes':len(checks)}))
