from pathlib import Path
import json,hashlib
H=Path(__file__).resolve().parent;S=Path('/home/mizuki/JJK-v0.341-para-subir');B=S/'sistema/05-material/livro/ciclo-maldito-r41';R=B/'revisao-de-regras';E=R/'editorial-r62';E.mkdir(exist_ok=True)
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def edit(p,a,b,n=1):
    s=p.read_text();assert s.count(a)==n,(p,a,s.count(a));p.write_text(s.replace(a,b))
MOT={'mov':'"Saldo" de movimento vira os metros que restam ou os metros extras.','amb':'Um nome só para o conceito: ambiente propício.','vida':'Vida e PE do momento viram vida atual e PE atuais.','uso':'"Saldo" de usos ou de PE de uma reserva vira o que resta dela.','reacao':'A Reação se escreve como algo que se gasta, não como reserva.','obra':'"Ampliar" fica só para o feitiço; a obra do Arquiteto passa a "Aumentar".','basica':'"Saldo" de básicas vira as básicas que a anterior ainda tinha.','xp':'"Saldo" de XP vira XP guardado.','mont':'"Saldo" da montagem vira pontos que sobram; "reservar pontos" vira destinar.','glos':'Glossário acompanha o nome novo e ganha Ambiente propício.','ind':'Índice acompanha o nome novo e ganha Ambiente propício.','def':'Termo de jogo explicado no primeiro uso, com o texto do Glossário.'}
ops=json.loads((H/'TROCAS-R62.json').read_text())
reg=[{'id':o['id'],'bloco':o['bloco'],'antes':o['antes'],'depois':o['depois'],'motivo':'Linguagem simples decidida pelo autor em 03/11/2026: '+MOT[o['motivo']]} for o in ops]
novo=(H/'LIVRO-CANDIDATA.md').read_text()
# reaplicar a partir do texto e do snapshot da R61, como a cadeia faz
txt=(B/'LIVRO-COMPLETO.md').read_text();snap=json.loads((R/'editorial-r61/BLOCOS-R61.json').read_text())
for r in reg:
    assert txt.count(r['antes'])==1 and snap[r['bloco']].count(r['antes'])==1,r['id']
    txt=txt.replace(r['antes'],r['depois'],1);snap[r['bloco']]=snap[r['bloco']].replace(r['antes'],r['depois'],1)
assert txt==novo
(B/'LIVRO-COMPLETO.md').write_text(novo);(E/'LIVRO-COMPLETO-R62.md').write_text(novo)
dump(E/'BLOCOS-R62.json',snap);dump(R/'alteracoes/R61-para-R62.json',reg)
sha=hashlib.sha256((B/'LIVRO-COMPLETO.md').read_bytes()).hexdigest()
dump(E/'FONTE-PUBLICADA.json',{'revisao':'R62','sha256_texto':sha,'blocos':len(snap),'composicao_local':str(H/'composicao'),'registros':len(reg),'tipo':'Linguagem simples decidida em 03/11/2026: saldo, ambiente propício, Reação, Aumentar e termos explicados no primeiro uso. Nenhuma regra mudou.'})
p=S/'conferir-repositorio.py';s=p.read_text();i=s.index("bloco('12. FONTE R61");j=s.index('# ----',i)
t=s[i:j].replace('R61','R62').replace('editorial-r61','editorial-r62').replace('range(54, 62)','range(54, 63)');assert t!=s[i:j];p.write_text(s[:i]+t+s[j:])
edit(p,"'EDICAO-ATUAL.json', 'REVISAO-R61.json')","'EDICAO-ATUAL.json', 'REVISAO-R62.json')")
edit(R/'editorial-r57/testar-integridade.py','R60-para-R61.json','R61-para-R62.json')
for d in ['editorial-r57','fundamento-r53']:edit(R/d/'testar-integridade.py',"bloco('12. FONTE R61","bloco('12. FONTE R62")
edit(R/'fundamento-r53/testar-integridade.py','fonte corrente R61','fonte corrente R62')
f=S/'sistema/03-mecanica/conferir-fundamento.py'
edit(f,'editorial-r61/BLOCOS-R61.json','editorial-r62/BLOCOS-R62.json')
edit(f,"['As funções e a distribuição do saldo da ficha permanecem','A versão não pode ganhar saldo pela troca']","['As funções e a divisão dos pontos que sobram, registradas na ficha, continuam as mesmas','A troca não pode deixar a versão com mais pontos que sobram']")
print('texto R62 integrado',sha[:16],len(reg))
