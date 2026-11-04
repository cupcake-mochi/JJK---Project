from pathlib import Path
import json,hashlib
H=Path(__file__).resolve().parent;S=Path('/home/mizuki/JJK-v0.341-para-subir');B=S/'sistema/05-material/livro/ciclo-maldito-r41';R=B/'revisao-de-regras';E=R/'editorial-r63';E.mkdir(exist_ok=True)
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def edit(p,a,b,n=1):
    s=p.read_text();assert s.count(a)==n,(p,a,s.count(a));p.write_text(s.replace(a,b))
MOT={'parcela':'"Parcela" vira "parte".','excedente':'"Excedente" vira o que passa do limite.','sobra':'O excedente da entidade passa a se chamar sobra de dano.','vinculado':'"Vinculado" vira "ligado a"; arma vinculada e Retorno Vinculado ficam, por serem nomes de regra.','elegivel':'"Elegível" vira permitida, válido ou que conta.','efetivamente':'"Efetivamente" vira "de fato".','concessao':'Frase reescrita sem "concessão".','pertinente':'"Pertinente" vira o que faz sentido ou se aplica.','retroativo':'Frase reescrita sem "retroativamente".','vencimento':'"Vencimento" vira "cobrança".','reserva-reacao':'A Reação se escreve como algo que se gasta, não como reserva.','reserva-mov':'"Reserva" de movimento vira metros ou deslocamento.','reserva-temp':'"Reserva" temporária vira vida temporária ou PE temporários.','reserva-integ':'"Reservas" viram vida, Integridade ou o que cada frase nomeia.','reserva-pe':'"Reserva" de energia vira PE.','reserva-vinculo':'"Reserva" de Pontos de Vínculo vira os próprios pontos.','reserva-barreira':'"Reserva de vida" da barreira vira total de vida.','obra':'O nível Ampliada das obras do Arquiteto vira Extensa, e "ampliá-la" vira "aumentá-la".'}
ops=json.loads((H/'TROCAS-R63.json').read_text())
reg=[{'id':o['id'],'bloco':o['bloco'],'antes':o['antes'],'depois':o['depois'],'motivo':'Linguagem simples decidida pelo autor em 03/11/2026: '+' '.join(MOT[m] for m in o['motivo'].split('+'))} for o in ops]
novo=(H/'LIVRO-CANDIDATA.md').read_text()
# reaplicar a partir do texto e do snapshot da R62, como a cadeia faz
txt=(B/'LIVRO-COMPLETO.md').read_text();snap=json.loads((R/'editorial-r62/BLOCOS-R62.json').read_text())
for r in reg:
    assert txt.count(r['antes'])==1 and snap[r['bloco']].count(r['antes'])==1,r['id']
    txt=txt.replace(r['antes'],r['depois'],1);snap[r['bloco']]=snap[r['bloco']].replace(r['antes'],r['depois'],1)
assert txt==novo
(B/'LIVRO-COMPLETO.md').write_text(novo);(E/'LIVRO-COMPLETO-R63.md').write_text(novo)
dump(E/'BLOCOS-R63.json',snap);dump(R/'alteracoes/R62-para-R63.json',reg)
sha=hashlib.sha256((B/'LIVRO-COMPLETO.md').read_bytes()).hexdigest()
dump(E/'FONTE-PUBLICADA.json',{'revisao':'R63','sha256_texto':sha,'blocos':len(snap),'composicao_local':str(H/'composicao'),'registros':len(reg),'tipo':'Linguagem simples decidida em 03/11/2026: palavras raras, reserva quando nomeava outra coisa e o nível Extensa das obras. Nenhuma regra mudou.'})
p=S/'conferir-repositorio.py';s=p.read_text();i=s.index("bloco('12. FONTE R62");j=s.index('# ----',i)
t=s[i:j].replace('R62','R63').replace('editorial-r62','editorial-r63').replace('range(54, 63)','range(54, 64)');assert t!=s[i:j];p.write_text(s[:i]+t+s[j:])
edit(p,"'EDICAO-ATUAL.json', 'REVISAO-R62.json')","'EDICAO-ATUAL.json', 'REVISAO-R63.json')")
edit(R/'editorial-r57/testar-integridade.py','R61-para-R62.json','R62-para-R63.json')
for d in ['editorial-r57','fundamento-r53']:edit(R/d/'testar-integridade.py',"bloco('12. FONTE R62","bloco('12. FONTE R63")
edit(R/'fundamento-r53/testar-integridade.py','fonte corrente R62','fonte corrente R63')
f=S/'sistema/03-mecanica/conferir-fundamento.py'
edit(f,'editorial-r62/BLOCOS-R62.json','editorial-r63/BLOCOS-R63.json')
edit(f,"['Com Mais Um','menor parcela',","['Com Mais Um','menor parte',")
edit(f,"check('Fórmula publicada com o nome novo',","""# R63 (03/11/2026): palavras raras saíram do texto. "Excedente" sobrevive só nos nomes Reserva Excedente e Ritual de Excedente.
_RARAS=r'\\b(?:parcelas?|eleg[ií]ve(?:l|is)|efetivamente|concess(?:ão|ões)|pertinentes?|retroativ\\w*|vencimentos?)\\b|\\bexcedentes?\\b(?<!Reserva Excedente)(?<!Ritual de Excedente)(?<!^Excedente)|reserva (?:coletiva|de Reação)|\\bAmpliada\\b'
def _raras_visiveis(t):
    t=re.sub(r'<!--.*?-->','',t,flags=re.S);t=re.sub(r'<a [^>]*></a>','',t);t=re.sub(r'\\]\\([^)]*\\)',']',t)
    return re.findall(_RARAS,t,flags=re.M)
check('Nenhuma palavra rara visível no livro (R63)',_raras_visiveis(_livro_md)==[])
check('Contra-teste: uma "parcela" no texto é contada',len(_raras_visiveis(_livro_md+'\\nUma parcela volta.'))==1)
check('Contra-teste: âncora e destino de link com parcelas não contam',_raras_visiveis('<a id="ritual--rit-parcelas"></a>[Partes adicionais](#ritual--rit-parcelas)')==[])
check('Fórmula publicada com o nome novo',""")
edit(S/'sistema/03-mecanica/conferir-acao.py',"'Cada tiro elegível de Rajada conta'","'Cada tiro válido de Rajada conta'")
print('texto R63 integrado',sha[:16],len(reg))
