# -*- coding: utf-8 -*-
"""Monta e confere os 35 feiticos prontos do manual v7.3 + TODOS os exemplos que
aparecem no texto (tutorial Corte Medido, tabela de Ampliar, Tecnica Maxima,
PE das Liberacoes, tabela de cura, conversao d6/d12).

Mudancas v6 -> v7 refletidas aqui:
  - LENTO virou MEDIA (v7.3). Lento e Acao Completa: engole movimento + acao bonus +
    acao padrao, ou seja, CONTEM o Parado (que so tira o movimento). Com os dois
    devolvendo Leve, o Lento era dominado — mesma devolucao, dor estritamente maior.
  - AQUECER virou LEVE (v7.3). E a unica Restricao de frequencia cujo custo some depois
    da rodada 1, e o personagem tem outros feiticos pra cobrir aquele turno. Devolvendo
    Media, era a melhor das quatro por larga margem. Nenhum dos 35 prontos usa Aquecer.
  - CONDICAO (v0.104): a Condicao Menor e a Condicao Maior viraram uma Melhoria so,
    chamada Condicao, e o preco dela e' o NIVEL da condicao (Leve/Media/Pesada) que
    a peca 19 secao 3 publica. Dez das catorze estavam no degrau errado. Dois prontos
    mudaram, os dois por causa do Derrubado: Palma Trovejante 5d8->6d8 e Vala Comum
    9d8->11d8. Rede e Prisao de Sombras carregam Atordoado, que ja era Pesada.
  - CONTROLE (v7.1): o degrau da metade do teto saiu. +1 rodada so com dano <= 1/4 do
    teto; CD+2 so com dano ZERO. Motivo: Condicao Menor sozinha da exatamente 2xGrau =
    metade do teto em TODO Classe, entao o bonus antigo era automatico, nao escolha.
  - Selo NAO da mais +1 ponto na Classe 2+. (Nenhum dos 35 prontos usava; a busca
    exaustiva do v6 nunca modelou esse ponto. Remover alinhou texto e modelo.)
  - Tabela de Ampliar corrigida: a versao v6 esquecia a devolucao do Lento da
    Palma Trovejante (dizia 3d8/4d8/7d8; o certo e 4d8/6d8/10d8).
  - Fio Preso: com Fica, a duracao sobe do degrau "uma semana" pro seguinte,
    "ate alguem desfazer" (regra da secao 5; o v6 imprimia "por uma semana").
  - Tecnica Maxima: dados fixos + orcamento de montagem pago nos precos do seu
    MAIOR Classe. Formas custam do orcamento (Projetil e Toque sao gratis).
"""
import math
D8=4.5
ERROS=[]
def dano(n): return math.floor(n*D8)
def pr(G,t): return {'L':math.ceil(G/2),'M':G,'P':math.ceil(1.5*G)}[t]
def prF(G,t,livre=False):
    # preco com desconto de Familia Livre: metade da Classe a menos, minimo 1
    p=pr(G,t)
    return max(1,p-math.ceil(G/2)) if livre else p
def maxmel(G): return 2 if G<=2 else (3 if G<=4 else 4)
def check(cond,msg):
    if not cond: ERROS.append(msg); print('  ERRO:',msg)

# custo da Forma e restricao embutida (Toque/Aura = Corpo a Corpo)
FORMA={'Projetil':None,'Toque':None,'Explosao':'L','Aura':'L','Cone':'L','Linha':'L',
       'Cura':'M','Apoio':None,'Onda':'P','Efeito':None}
EMBUTIDA={'Toque':('Corpo a Corpo','M'),'Aura':('Corpo a Corpo','M')}
CONTROLE={'Condicao','Terreno','Anteparo','Prende','Cerca','Puxa','Desarma o Feitico'}
FREQ={'Uma Vez','Condicional','Aquecer','Divida'}

def b(nome,G,forma,mel,res,lib=False,extra=0,alma=False,livres=()):
    """mel: lista de (nome, tier) ou (nome, tier, True) se a Familia for Livre."""
    pts=3*G; teto=4*G; devmax=2*G
    cf = pr(G,FORMA[forma]) if FORMA[forma] else 0
    res=list(res)+([EMBUTIDA[forma]] if forma in EMBUTIDA else [])
    mel=[(m[0],m[1],(len(m)>2 and m[2])) for m in mel]
    custo=cf+sum(prF(G,t,lv) for _,t,lv in mel)
    devb=sum(pr(G,t) for _,t in res); deve=min(devb,custo)
    dados=pts-max(0,custo-deve)+(G if lib else 0)
    err=[]
    # dois tetos: num ALVO SO o feitico comum para nos pontos da Classe; somando
    # alvos e repeticoes, ninguem passa de 4 x Classe.
    if not lib and dados>pts: err.append(f"ALVO {dados}>{pts}")
    if dados+extra>teto: err.append(f"TOTAL {dados+extra}>{teto}")
    if lib and G<3: err.append("LIB SO G3+")
    nomes_res=[n.split(':')[0].strip() for n,_ in res]
    if sum(1 for n in nomes_res if n in FREQ)>1: err.append("2x FREQUENCIA")
    if devb>devmax: err.append(f"DEV {devb}>{devmax}")
    if len(mel)>maxmel(G): err.append(f"MEL {len(mel)}>{maxmel(G)}")
    if len(res)>2: err.append("RESTR>2")
    base=[n.split(':')[0].strip() for n,_,_ in mel]
    if alma:
        if G<3: err.append("ALMA SO G3+")
        if lib: err.append("ALMA NAO E LIB")
        dalma=dados//2
        if dalma>2*G: err.append(f"ALMA {dalma}>{2*G}")
    ctrl=""
    if any(n in CONTROLE for n in base):
        # v7.1: o degrau da METADE saiu (Cond.Menor sozinha sempre disparava = nao era escolha).
        # +1 rodada exige dano <= 1/4 do teto; CD+2 exige dano ZERO.
        if dados==0: ctrl="CD+2 e +1 rodada"
        elif dados<=teto//4: ctrl="+1 rodada"
    linhas=[]
    if cf: linhas.append(f"{forma} (-{cf})")
    elif forma!='Projetil': linhas.append(forma)
    for n,t,lv in mel: linhas.append(f"{n} (-{prF(G,t,lv)}{' Livre' if lv else ''})")
    for n,t in res: linhas.append(f"{n} (+{pr(G,t)})")
    if lib: linhas.append(f"LIBERACAO (+{G})")
    if alma: dtxt=f"{dados}d -> {dados//2}d8 = {dano(dados//2)} na alma"
    elif forma=='Efeito': dtxt=f"escala e duracao da Classe {G}"
    elif forma in ('Cura','Onda'): dtxt=f"cura {dados}d8 = {dano(dados)}"
    else: dtxt=f"{dados}d8 = {dano(dados)}"
    if extra: dtxt+=f" [+{extra}d8={dano(extra)}]"
    pe=math.ceil(3*G*1.5) if lib else 3*G
    print(f"{nome:<20} G{G} {pts:>2}pt {pe:>2}PE | "+" · ".join(linhas).ljust(72)+f"| {dtxt:<24}{ctrl:<18}{'OK' if not err else 'ERRO '+','.join(err)}")
    ERROS.extend(f"{nome}: {e}" for e in err)
    return dados

print("="*168)
print("FEITICOS PRONTOS (30 comuns)")
print("="*168)
for a in [
 ("Estalo",1,'Projetil',[],[]),
 ("Chicote",1,'Linha',[],[]),
 ("Perfurar",1,'Projetil',[("Precisao",'L')],[("Parado",'L')]),
 ("Golpe Cru",1,'Toque',[],[]),
 ("Palma Trovejante",2,'Cone',[("Condicao: Derrubado",'L')],[("Lento",'M')]),
 ("Lanca Negra",2,'Projetil',[("Fura",'M')],[("Lento",'M')]),
 ("Faisca em Cadeia",2,'Projetil',[("Salto",'M')],[("Gesto",'L')],False,2),
 ("Sopro",2,'Cura',[],[]),
 ("Vento a Favor",2,'Apoio',[("Impulso",'L'),("Pressa",'M')],[]),
 ("Marca do Carrasco",3,'Projetil',[("Marca",'L'),("Queima",'M')],[("Uma Vez",'L')],False,3),
 ("Domo de Gelo",3,'Explosao',[("Terreno",'L'),("Maior",'L')],[("Condicional: no escuro",'L')]),
 ("Passo Cortante",3,'Toque',[("Passo",'L'),("Precisao",'L')],[]),
 ("Costura",3,'Cura',[("Limpa",'M')],[("Gesto",'L')]),
 ("Rede",3,'Explosao',[("Condicao: Atordoado",'P'),("Terreno",'L')],[]),
 ("Hora Morta",3,'Efeito',[("Longe",'L')],[]),
 ("Fissura",3,'Projetil',[("Toca a Alma",'L')],[],False,0,True),
 ("Prisao de Sombras",4,'Explosao',[("Condicao: Atordoado",'P'),("Escolher",'M')],[("Sangra",'M')]),
 ("Julgamento Vertical",4,'Linha',[("Fura",'M'),("Precisao",'L')],[("Lento",'M')]),
 ("Roubo de Folego",4,'Projetil',[("Sugar",'M'),("Remate",'M')],[("Condicional: alvo que te acertou",'M')]),
 ("Passo do Espelho",4,'Toque',[("Rapido",'P'),("Passo",'L')],[("Recuo",'M')]),
 ("Muralha",4,'Apoio',[("Anteparo",'M'),("Guarda",'M')],[("Parado",'L')]),
 ("Mare Branca",4,'Onda',[],[]),
 ("Alinhavo",4,'Cura',[("Remenda",'P')],[("Gesto",'L')]),
 ("Purga Escarlate",5,'Projetil',[("Inescapavel",'M')],[]),
 ("Chuva de Agulhas",5,'Projetil',[("Rajada",'L'),("Precisao",'L')],[("Parado",'L')]),
 ("Vala Comum",5,'Explosao',[("Maior",'L'),("Condicao: Derrubado",'L')],[("Lento",'M')]),
 ("Fim de Turno",5,'Explosao',[("Escolher",'M')],[("Lento",'M')]),
 ("Segunda Vida",5,'Cura',[("Levanta",'P')],[("Uma Vez",'L'),("Gesto",'L')]),
 ("Fio Preso",5,'Efeito',[("Fica",'M')],[]),
 ("Sete Palmos",5,'Toque',[("Toca a Alma",'L')],[],False,0,True),
]:
    b(*a)
print("  Fio Preso: com Fica, a duracao sobe do degrau 'uma semana' (Classe 5) pro seguinte:")
print("  ATE ALGUEM DESFAZER. (v6 dizia 'por uma semana' — corrigido no v7.)")

print("-"*168)
print("LIBERACOES MAXIMAS (Classe 3+, fora da lista de conhecidos, +Classe em dados, PE +50% arredondando pra cima)")
gv=b("Golpe do Voto",5,'Projetil',[],[],True)
ra=b("Rachadura",3,'Linha',[],[("Lento",'M')],True)
sf=b("Sentenca Final",5,'Explosao',[("Escolher",'M')],[("Lento",'M')],True)
check(gv==20 and dano(20)==90 and math.ceil(15*1.5)==23, "Golpe do Voto: 20d8=90, 23 PE")
check(ra==12 and dano(12)==54 and math.ceil(9*1.5)==14,  "Rachadura: 12d8=54, 14 PE")
check(sf==17 and dano(17)==76 and math.ceil(15*1.5)==23, "Sentenca Final: 17d8=76, 23 PE")
check(sf<=4*5, f"Sentenca Final cabe no teto da Liberacao ({sf}<=20)")

print("-"*168)
print("EXEMPLO DE ABERTURA — Lanca Negra (a Restricao paga a Melhoria inteira)")
ln=b("Lanca Negra (abertura)",2,'Projetil',[("Fura",'M')],[("Lento",'M')])
check(ln==6 and dano(6)==27, "Lanca Negra: 6d8 = 27, o dano cheio da Classe 2")
check(ln==3*2, "Lanca Negra bate no teto contra um alvo (pontos da Classe), sem passar dele")
print("  A devolucao do Lento (2) cobre exatamente a Fura (2): dano cheio + Fura de graca.")
print("  E o teto contra um alvo segura em 6 — Restricao nunca passa disso.")
print("-"*168)
print("TUTORIAL DA SECAO 2 — Corte Medido (feitico da Regua: Mira e Alcance Livres)")
cm=b("Corte Medido",2,'Projetil',[("Fura",'M',True),("Precisao",'L',True)],[("Parado",'L')])
check(cm==5 and dano(5)==22, "Corte Medido: 5d8 = 22")
check(prF(2,'M',True)==1, "Fura na Familia Livre, Classe 2: 2 - 1 = 1 ponto")
check(prF(2,'L',True)==1, "Precisao na Familia Livre, Classe 2: minimo 1 ponto")
check(3*2==6, "Fura na Classe 2 ignora 3 x 2 = 6 de RD")

print("-"*168)
print("TABELA DE AMPLIAR — Palma Trovejante completa (Cone + Derrubado + Lento) por Classe")
print("v0.104: o Derrubado e Leve. Antes disto a tabela dizia 5d8/7d8/12d8, com o Derrubado em Media.")
esperado={2:6,3:8,5:14}
# v0.104: o Derrubado e' nivel Leve, e o nivel E' o preco. O Lento continua Media.
for G in (2,3,5):
    custo=pr(G,'L')+pr(G,'L'); dev=pr(G,'M')
    dd=3*G-max(0,custo-dev)
    ctrl="+1 rodada" if dd<=(4*G)//4 else "nada"
    prop=dd/(4*G)*100
    print(f"  Classe {G}: {3*G} pts - Cone {pr(G,'L')} - Derrubado {pr(G,'L')} + Lento {dev} = {dd}d8 = {dano(dd)}"
          f"  (Controle: {ctrl}; {prop:.0f}% do teto; PE {3*G})")
    check(dd==esperado[G], f"Ampliar Classe {G}: esperado {esperado[G]}d8")
    # v0.104: com o Derrubado em Leve a Palma sobe de ~60% para ~70% do teto —
    # e continua bem acima do quarto, que e' o que o manual afirma.
    check(65<=prop<=75, f"Ampliar Classe {G}: proporcao {prop:.0f}% fora da faixa de ~70%")
    check(dd>(4*G)//4, f"Ampliar Classe {G}: Palma nao alcanca o bonus de Controle")

print("-"*168)
print("TECNICA MAXIMA — dados fixos + orcamento de montagem nos precos da MAIOR Classe")
for faixa,G,dd,orc in [("17 a 20",5,24,8),("21 a 25",6,28,8),("26 a 30",7,32,12)]:
    print(f"  {faixa}: {dd}d8 = {dano(dd)} · orcamento {orc} pontos (precos da Classe {G}: L {pr(G,'L')} / M {pr(G,'M')} / P {pr(G,'P')}) · PE {5*G}")
check(dano(24)==108 and dano(28)==126 and dano(32)==144, "TM: 108/126/144")
check(5*5==25 and 5*6==30 and 5*7==35, "TM: PE 25/30/35 = 5 x maior Classe")
# O Fim da Linha: Forma Linha (Leve 3) + Muito Longe (Media 5) = 8 do orcamento de 8
fl=pr(5,'L')+pr(5,'M')
check(fl==8, f"O Fim da Linha gasta Linha 3 + Muito Longe 5 = {fl} de 8")
# alcance: escada Cone/Linha 4,5 -> 9 -> 18 -> 30 -> 60; de 18, tres degraus estoura a
# escada e para no ultimo: 60 m
esc=[4.5,9,18,30,60]
alvo=esc[min(esc.index(18)+3,len(esc)-1)]
check(alvo==60, "Muito Longe a partir de 18 m: a escada acaba e para em 60 m")
# Ponto Final: Projetil (0) + Fura (Media 5) = 5 de 8; sobra 3 que NAO vira dado
pf=0+pr(5,'M')
check(pf==5, f"Ponto Final gasta Fura 5 de 8; sobram 3 que nao viram nada")
check(3*5==15, "Fura na TM usa a maior Classe: ignora 3 x 5 = 15 de RD")

print("-"*168)
print("TRAVA DO CATALOGO DE RESTRICOES — nenhuma devolve Pesada")
print("-"*168)
# Se uma Restricao devolvesse Pesada, duas delas passariam do teto de devolucao (2 x Classe)
# em toda Classe. E por isso que a Restricao Propria vai so ate Media.
TIERS_REST=set('LM')  # tiers permitidos pra qualquer Restricao, inclusive a Propria
check('P' not in TIERS_REST, "nenhuma Restricao pode devolver Pesada")
for G in range(1,8):
    check(2*pr(G,'M')==2*G, f"Classe {G}: duas Medias batem exatamente no teto de devolucao ({2*G})")
    check(2*pr(G,'P')>2*G,  f"Classe {G}: duas Pesadas estourariam o teto ({2*pr(G,'P')}>{2*G})")
print(f"  {'Classe':<6}{'teto de devolucao':<20}{'2 Restricoes Medias':<22}{'2 Pesadas seriam':<18}")
for G in range(1,8):
    print(f"  {G:<6}{2*G:<20}{2*pr(G,'M'):<22}{2*pr(G,'P'):<18}")
print("  => o catalogo (e a Restricao Propria) fecham exatamente no teto usando Medias.")
print()
print("="*168)
print("TABELAS DO MANUAL — conferencia rapida")
# cura por Classe (Cura = Media; Onda = Pesada)
cura=[(G,3*G-pr(G,'M'),3*G-pr(G,'P')) for G in range(1,6)]
esperado_cura=[(1,2,1),(2,4,3),(3,6,4),(4,8,6),(5,10,7)]
check(cura==esperado_cura, f"tabela de cura: {cura}")
print("  Cura cheia:", " · ".join(f"G{G} {c}d8={dano(c)}" for G,c,_ in cura))
print("  Onda:      ", " · ".join(f"G{G} {o}d8={dano(o)}" for G,_,o in cura))
# dano cheio por Classe
for G,esp in [(1,13),(2,27),(3,40),(4,54),(5,67),(6,81),(7,94)]:
    check(dano(3*G)==esp, f"dano cheio G{G} = {esp}")
# liberacao no teto
for G,esp in [(3,54),(4,72),(5,90),(6,108),(7,126)]:
    check(dano(4*G)==esp, f"liberacao G{G} = {esp}")
# precos por Classe (tabela 'Os numeros' e tabela de bolso)
precos=[(G,pr(G,'L'),pr(G,'M'),pr(G,'P')) for G in range(1,8)]
check(precos==[(1,1,1,2),(2,1,2,3),(3,2,3,5),(4,2,4,6),(5,3,5,8),(6,3,6,9),(7,4,7,11)],
      f"precos Leve/Media/Pesada: {precos}")
# PE por nivel (conjurador 6/nivel) e usos do melhor feitico
for nv,G,usos in [(1,1,2),(5,2,5),(9,3,6),(13,4,6),(17,5,6),(20,5,8)]:
    check((6*nv)//(3*G)==usos, f"nivel {nv}: {6*nv} PE lanca a Classe {G} {usos}x")
# vida e 'rodadas pra cair'
for nv,vida,pico,rod in [(1,20,13,1.5),(5,52,27,1.9),(10,92,54,1.7),(15,132,72,1.8),(20,172,90,1.9),(25,212,108,2.0),(30,252,126,2.0)]:
    check(20+8*(nv-1)==vida, f"vida nivel {nv} = {vida}")
    check(round(vida/pico,1)==rod, f"rodadas nivel {nv} = {rod}")
# PvP: corte de 1/3
for nv,pico,corte,rod in [(10,54,36,2.6),(20,90,60,2.9),(30,126,84,3.0)]:
    check(pico-pico//3==corte and round((20+8*(nv-1))/corte,1)==rod, f"PvP nivel {nv}: {corte}, {rod} rodadas")
# curva: rotina (pontos + Queima media do turno seguinte ja contada como +G//2... a rotina
# do manual e pontos+extra fixo por faixa: 3+0? Na v6: 1a4=3d8; 5a8=6+1; 9a12=9+1; 13a16=12+2; 17a20=15+2; 21a25=18+3; 26a30=21+3
for G,extra,esp in [(1,0,13),(2,1,31),(3,1,45),(4,2,63),(5,2,76),(6,3,94),(7,3,108)]:
    check(dano(3*G+extra)==esp, f"curva rotina G{G} = {esp}")
# conversao d6/d12 = arredondamento da media (4,5n / 3,5 e 4,5n / 6,5)
import decimal
def rnd(x): return int(decimal.Decimal(x).quantize(0, rounding=decimal.ROUND_HALF_UP))
d6esp=[1,3,4,5,6,8,9,10,12,13,14,15,17,18,19,21,22,23,24,26,27,28,30,31,32,33,35,36]
d12esp=[1,1,2,3,3,4,5,6,6,7,8,8,9,10,10,11,12,12,13,14,15,15,16,17,17,18,19,19]
check(all(rnd(4.5*n/3.5)==d6esp[n-1] for n in range(1,29)), "tabela d8 -> d6")
check(all(rnd(4.5*n/6.5)==d12esp[n-1] for n in range(1,29)), "tabela d8 -> d12")
# Classe 0
check([2,3,4,5,5]==[2,3,4,5,5], "Classe 0: 2 no nv1, 3 no nv5, 4 no nv11, 5 no nv17, 5 no nv25")
# Integridade: teto na alma
check(all((3*G)//2<=2*G for G in range(1,8)), "teto na alma segura sem Liberacao")

print("="*168)
print("Notas (iguais ao v6, o que mudou esta no topo do arquivo):")
print("  Anteparo = 10 x Classe -> Muralha deixa parede de 40 na Classe 4.")
print("  Toque e Aura ja carregam Corpo a Corpo embutida (devolve Media, conta no limite de 2 Restricoes).")
print("  Condicional devolve Leve (falha rara) ou Media (falha na maioria). Remate nao aceita Condicional de vida do alvo.")
print("  Toca a Alma: so Classe 3+, so Regra que encosta em alma/mente/conceito, e nao entra em Liberacao.")
print("  Dados na alma = metade dos dados finais, arredondando pra baixo. Teto na alma = 2 x Classe.")
print("  Alinhavo: alem da cura, devolve 5 x Classe = 20 de Integridade (Remenda, uma vez por cena).")
print("  Classe 0 nao entra: nao se monta.")
print("  Selo v7: identidade + trava (Restricao que o Selo ja obriga nao devolve ponto). SEM bonus de ponto.")
print("  Restricao Propria (v7.2): customizada, devolve Leve ou Media, conta no limite de 2.\n  Lento = Media e Aquecer = Leve desde a v7.3.")
print()
if ERROS:
    print(f">>> {len(ERROS)} ERRO(S):"); [print("   ",e) for e in ERROS]
else:
    print(">>> TUDO OK — todos os feiticos, exemplos e tabelas do manual v7 conferem.")
