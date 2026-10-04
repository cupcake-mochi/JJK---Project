"""Contas e regressões dirigidas da abertura; não é um motor de combate."""
from pathlib import Path
import hashlib
import itertools
import json
import re

B = Path(__file__).resolve().parent
P = B.parents[1]
M = B / 'ABERTURA-E-CRIACAO.md'
S = M.read_text()
SHA = hashlib.sha256(M.read_bytes()).hexdigest()
checks = []

def check(key, ok, detail=None):
    checks.append({'id': key, 'passou': bool(ok), 'detalhe': detail})

def read(rel):
    return (P / rel).read_text()

for f, expected in json.loads((B/'evidencias/fontes-preservadas.json').read_text()).items():
    check('fonte-preservada:' + Path(f).name, hashlib.sha256((B.parents[5]/f).read_bytes()).hexdigest() == expected)

kaori = {'F': 3, 'D': 2, 'C': 2, 'I': 1, 'E': 1, 'M': 1, 'nivel': 2}
check('atributos-nove', sum(kaori[k] for k in 'FDCIE') == 9)
check('atributos-limites', all(0 <= kaori[k] <= 3 for k in 'FDCIE'))
distribuicoes = [a for a in itertools.product(range(4), repeat=5) if sum(a) == 9]
check('distribuicao-com-zero-permitida', any(0 in a for a in distribuicoes))
check('sem-sobrar-pontos', all(sum(a)==9 for a in distribuicoes))
check('pv-kaori', (12+2)+(7+2)==23 and '**14 + 9 = 23 pontos de vida (PV)**' in S)
check('pe-kaori', 4*2==8 and '**4 × nível = 8**' in S)
check('defesa-kaori', 10+2+1==13 and 'base 10 + Destreza 2 + proteção 1' in S)
check('tr-fisico', 3+1==4 and '**+4 em Físico**' in S)
check('tr-vigor', 2+1==3 and '**+3 em Vigor**' in S)
check('tr-nao-treinado', '**+1 em Intelecto**' in S and '**+1 em Espírito**' in S)
check('atributo-ja-e-bonus', '**Força 3 fornece +3**' in S)
check('treinos-9-2', 2+5+1+1==9 and '**nove perícias e dois ofícios**' in S)
check('troca-dois-oficios', '**dez perícias sem ofícios**' in S)
check('arma-retira-duas-pericias', 'retire as duas perícias da conta' in S)
check('tr-dois-distintos', 'Escolha dois diferentes' in S)
check('fisico-permanente', 'A escolha permanece na ficha' in S)
check('espacos-nivel2', 2+2//2==3 and '**três espaços conhecidos**' in S)
check('classezero-separada', '**dois feitiços de Classe 0**' in S and 'contagem separada' in S)
check('classezero-fonte', '| Quantidade conhecida | 2 |' in read('fundamento/lote-01/FUNDAMENTO.md'))
check('toque-pontos', 3+1-1==3 and 'Sobram 3 dados.' in S)
check('melhoria-livre-piso', 'Seu preço final nunca fica abaixo de 1 ponto.' in read('fundamento/lote-01/FUNDAMENTO.md'))
check('ataque-kaori', 3+1==4 and 'd20 + 4' in S)
check('cd-kaori', 8+3+1==12 and '| CD de sua técnica | 12. |' in S)
check('dano-sem-soco-atributo', 'não soma o dano de um soco nem Força' in S)
check('arma-permitida-nao-presumida', 'armas permitidas' not in S)
check('invocacao-por-espaco-especifica', 'Usar um espaço conhecido para uma invocação exige um conceito' in S)
check('repertorio-nao-completo', 'O repertório completo e as demais escolhas' in S)
check('criatura-nao-completa', 'mestre precisa de uma ficha completa' in S)
check('protecao-nao-dupla', 'não entram duas vezes' in S)
check('inicio-nivel-e-patente', '**nível 2**' in S and 'Grau 4' in S)
check('uniforme-fundo', '**um Traje 1 e ¥150.000**' in S)
check('carga', '**5 + Força**' in S)
check('iniciativa', 11+2==13 and 16+3==19 and '**16 + 3 = 19**' in S)
check('ataque-inimigo', 14+3==17 and 17>=13 and '**14 + 3 = 17**' in S)
check('dano-inimigo', 3+2==5 and 23-5==18 and '**18 PV**' in S)
check('custo-antes-dado', S.index('passando de 8 para **5 PE**') < S.index('Seu d20 mostra 12'))
check('erro-gasta', 'Se o ataque de Kaori errasse, ela continuaria tendo gasto a ação e o PE.' in S)
check('acerto-feitico', 12+4==16 and 16>=12 and '**12 + 4 = 16**' in S)
check('dados-feitico', 4+5+5==14 and 'saem 4, 5 e 5' in S)
check('alcance', 'a **1,5 m da maldição**' in S)
check('movimento', 9-3==6 and 'Ainda teria 6 m disponíveis' in S)
check('recursos-finais', 23-5==18 and 8-3==5 and '**18 PV e 5 PE**' in S)
check('efeito-sobrevivente', 'aplicar Derrubado e sua duração' in S)
check('sem-restauro-fim-combate', 'não devolve automaticamente' in S)
check('sem-copia-habilidades', all(x not in S for x in ['## Olhos Em Mim','## Alicerce','## Movimento Acrobático']))
check('ponto-virgula', ';' not in S)
check('titulos-artigos', not re.search(r'^#+\s+(?:A|O|As|Os)\s', S, re.M))
check('titulo-como-ler', not re.search(r'^#+.*como ler',S,re.M|re.I))
check('medidas-de-combate', all(abs(float(x.replace(',','.'))/1.5-round(float(x.replace(',','.'))/1.5))<1e-8 for x in re.findall(r'(\d+(?:,\d+)?)\s*m\b',S)))

# Distribuição independente dos dados. Sem Bloquear/Esquivar neste ramo.
d3 = [sum(a) for a in itertools.product(range(1,9),repeat=3)]
d6 = [sum(a) for a in itertools.product(range(1,9),repeat=6)]
check('media-3d8', sum(d3)/len(d3)==13.5)
check('media-critico-6d8', sum(d6)/len(d6)==27)
hit = sum(d+4>=12 for d in range(1,21))/20
check('chance-acerto-kaori', hit==.65)
chance_queda = .6*sum(d>=14 for d in d3)/len(d3)+.05*sum(d>=14 for d in d6)/len(d6)
check('chance-nao-garantida', 0<chance_queda<1)
mean_kaori = .6*13.5+.05*27
mean_foe = .5*5.5+.05*9
check('inimigo-nao-letalo1golpe', max(range(1,7))*2+2<23)

def manter(p,d):
 # Os blocos revisao_delta são a anotação de revisão escrita depois da auditoria; reexecutar a auditoria não os apaga.
 if p.exists():d.update({k:v for k,v in json.loads(p.read_text()).items() if k.startswith('revisao_delta')})
 return d
out={'ok':all(c['passou'] for c in checks),'manuscritos_auditados':{str(M.relative_to(P.parents[3])):SHA},'verificacoes':checks,'resultados':{'distribuicoes_atributos':len(distribuicoes),'estados_dano_3d8':len(d3),'estados_dano_critico_6d8':len(d6),'chance_acerto_kaori_sem_bloquear':hit,'chance_exorcismo_um_ataque_sem_bloquear':chance_queda,'dano_medio_por_ataque_kaori':mean_kaori,'dano_medio_por_ataque_criatura':mean_foe},'limites':['Encontro didático parcial, não ficha de inimigo calibrada para publicação.','Distribuições não simulam decisões, posicionamento ou combate integral.','Regras de morte/Integridade ainda serão reconciliadas no livro.','Nenhum teste com jogadores.']}
(B/'evidencias/auditoria-numerica.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(B/'evidencias/regras-verificadas.json').write_text(json.dumps(manter(B/'evidencias/regras-verificadas.json',{'ok':out['ok'],'sha256_texto':SHA,'verificacoes':len(checks),'limites':out['limites']}),ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':out['ok'],'verificacoes':len(checks),'falhas':[x for x in checks if not x['passou']],'resultados':out['resultados']},ensure_ascii=False,indent=2))
raise SystemExit(not out['ok'])
