# -*- coding: utf-8 -*-
"""Fundamento v7 — validacao da economia, limites, teto e as pecas novas.

DECISOES TRAVADAS (v5, mantidas na v7):
 1. Teto = 4 x Classe em dados, e SO a Liberacao Maxima chega nele. Feitico comum para nos
    pontos da Classe (3 x Classe). O caminho pro teto e sempre sem Melhoria e sem Restricao.
 2. Restricao nao vira dano. (E o motivo de Selo complexo nao entrar.)
 3. Nenhuma Melhoria fura imunidade. Furar resistencia sim, imunidade nao.
 4. Pico do nivel 20 = 90 de dano, e ele agora mora na LIBERACAO MAXIMA (Classe 5, sem
    peca nenhuma). Feitico comum do nivel 20 para em 67 (15d8); com Remate chega a 84.
    A Tecnica Maxima fica fora da conta: dado fixo, segurada pelo recarregamento.
    Se o pico da Liberacao mudar, alguma regra quebrou.
 5. Vida = 20 + 8 x (nivel - 1). Integridade = vida maxima.
 6. Gatilho de Controle e dano final, nao gasto. (v7.1: 1/4 do teto -> +1 rodada;
    dano zero -> tambem CD+2. O degrau da metade saiu por ser automatico.)
 7. Dano na alma custa 2 dados normais por 1 dado na alma.
 8b. (v7) Selo NAO da +1 ponto na Classe 2+. O Selo e identidade + a trava "Restricao que
    o Selo ja obriga nao devolve ponto". O bonus do v6 nunca entrou neste modelo nem nos
    35 prontos; remover alinhou o texto com a matematica validada.
 8. Liberacao Maxima: feitico a parte, Classe 3+, uma no nivel 10/20/30, fora da lista de
    conhecidos. E a unica peca que soma dados acima dos pontos da Classe. A paridade sai de
    1 de alma = 1 de dano + 1 de teto de vida negado. Se a taxa mudar,
    dano na alma vira upgrade estrito.
"""
import math, itertools
D8=4.5
def pr(G,t): return {'L':math.ceil(G/2),'M':G,'P':math.ceil(1.5*G)}[t]
def maxmel(G): return 2 if G<=2 else (3 if G<=4 else 4)

print("="*94); print("1) ECONOMIA DE PE — custo = 3 x Classe (= os pontos do feitico)"); print("="*94)
print("PE por nivel: conjurador 6 · demais 5 · combatente 4\n")
print(f"{'Nivel':<7}{'Classe max':<10}{'PE conjurador':<16}{'custo do topo':<16}{'usos do topo':<15}{'ref. 5e':<20}")
tab={1:1,5:2,9:3,13:4,17:5,21:6,26:7}
for nv,ref in [(1,'2 espacos de 1o'),(5,'~9 espacos'),(9,'~14 espacos'),(13,'~17 espacos'),(17,'~20 espacos'),(20,'~22 espacos')]:
    G=max(v for k,v in tab.items() if nv>=k); pe=6*nv; c=3*G
    print(f"{nv:<7}{G:<10}{pe:<16}{c:<16}{pe/c:<15.1f}{ref:<20}")
print("\n  Tecnica Maxima: custa 5 x Classe maximo de PE (25/30/35 por faixa) e volta ao fim do")
print("  terceiro turno seguinte. A conta esta na secao 7.")
print("  Liberacao Maxima: +50% no custo (arredonda pra cima). Preco na hora: Vazio, Sangue ou Peso.")
print("  Classe 0: gratis. Quantos: 2 no nivel 1, 3 no 5, 4 no 11, 5 no 17. Dano 2/3/4/5/6d8 (25).")

print()
print("="*94); print("2) LIMITE DE MELHORIAS ESCALONADO POR CLASSE"); print("="*94)
print(f"{'Classe':<7}{'Pontos':<9}{'Melhorias max':<16}{'Restricoes max':<17}{'linhas na ficha':<18}")
for G in range(1,8):
    print(f"{G:<7}{3*G:<9}{maxmel(G):<16}{2:<17}{maxmel(G)+2:<18}")
print("\n  Regra enunciada:  2 Melhorias nas Classes 1-2 · 3 nas Classes 3-4 · 4 da Classe 5 pra cima.")
print("  Restricoes: ate 2, sempre.")

print()
print("="*94); print("3) CONTROLE — gatilho por DANO FINAL, nao por gasto"); print("="*94)
print("Regra v7.1: dano final ate UM QUARTO do teto -> efeitos de Controle duram +1 rodada.")
print("Dano ZERO (o Controle levou o orcamento inteiro) -> tambem CD +2 contra eles.")
print("(O degrau da METADE saiu: Cond.Menor sozinha dava exatamente 2xGrau = metade do teto")
print(" em TODO Classe, entao o bonus era automatico e nao uma escolha de montagem.)\n")
print(f"{'Classe':<6}{'teto':<6}{'quarto':<8}{'Cond.Menor':<16}{'Cond.Maior':<16}{'Maior+Media':<16}")
for G in range(1,8):
    pts=3*G; teto=4*G
    dMenor=pts-pr(G,'M'); dMaior=pts-pr(G,'P'); dDuplo=max(pts-pr(G,'P')-pr(G,'M'),0)
    def tag(d):
        if d==0: return f"{d}d8 CD+2 e +1rd"
        if d<=teto//4: return f"{d}d8 +1 rodada"
        return f"{d}d8 nada"
    print(f"{G:<6}{teto:<6}{teto//4:<8}{tag(dMenor):<16}{tag(dMaior):<16}{tag(dDuplo):<16}")
ok1=all(3*G-pr(G,'M') > (4*G)//4 for G in range(1,8))
ok2=all(max(3*G-pr(G,'P')-pr(G,'M'),0) <= (4*G)//4 for G in range(1,8))
print(f"\n  Cond. Menor SOZINHA nao ganha mais nada (o bonus virou escolha): {'SIM' if ok1 else 'NAO'}")
print(f"  Maior + mais uma Media sempre dispara o +1 rodada:              {'SIM' if ok2 else 'NAO'}")
print(f"  CD+2 exige dano ZERO, alcancavel em toda Classe com 2-3 pecas de Controle.")
print("  Restricao nao infla mais nada: o gatilho e o numero final de dados, e Restricao nunca vira dado.")

print()
print("="*94); print("4) BUSCA EXAUSTIVA — dois regimes: feitico comum e Liberacao Maxima"); print("="*94)
MULT={'L':[1.0],'M':[1.0,1.25,1.5],'P':[1.0]}
def varre(G, permite_lib, vals, max_mult=None):
    # max_mult = quantas Melhorias multiplicadoras cabem. O catalogo real tem UMA (Remate),
    # e ela nao e compr?vel duas vezes. None = sem limite (modelo pessimista de robustez).
    pts=3*G; devmax=2*G; teto=4*G; vmax=G; mm=maxmel(G)
    tested=0; legal=0; best=(0,"")
    for L in range(mm+1):
     for M in range(mm+1-L):
      for Pz in range(mm+1-L-M):
       if L+M+Pz>mm: continue
       for mults in (itertools.product(*[vals]*M) if M else [()]):
        if max_mult is not None and sum(1 for x in mults if x>1.0) > max_mult: continue
        custo=L*pr(G,'L')+M*pr(G,'M')+Pz*pr(G,'P')
        mult=1.0
        for x in mults: mult*=x
        for rL in range(3):
         for rM in range(3-rL):
          if rL+rM>2: continue
          for voto in ((0,vmax) if permite_lib else (0,)):
            tested+=1
            devb=rL*pr(G,'L')+rM*pr(G,'M')
            if devb>devmax: continue
            dados=pts-max(0,custo-min(devb,custo))+voto
            total=dados*mult
            if total>teto+1e-9: continue
            legal+=1
            if total>best[0]: best=(total,f"{L}L+{M}M+{Pz}P mel, {rL}L+{rM}M restr"+(", LIB" if voto else ""))
    return best, tested, legal

print("Modelo pessimista (multiplicadores hipoteticos ate 1,5, empilhaveis) — prova de robustez:")
print(f"{'Classe':<6}{'Pontos':<8}{'Teto':<7}{'perfis':>9}{'legais':>9}{'   MAXIMO':>14}{'   como':<30}")
RES={}
for G in range(1,8):
    b,t,l = varre(G, True, MULT['M'])
    RES[G]=b[0]*D8
    print(f"{G:<6}{3*G:<8}{4*G:<7}{t:>9}{l:>9}{b[0]:>8.0f} dados = {b[0]*D8:5.1f}   {b[1]:<30}")
ok=all(abs(RES[G]-4*G*D8)<1e-6 for G in range(1,8))
print(f"\n  Liberacao Maxima bate no teto (4 x Classe) em toda Classe: {'SIM' if ok else 'NAO'}")
print(f"  Pico do nivel 20 (Liberacao Classe 5): {RES[5]:.1f}  (meta 90: {'OK' if abs(RES[5]-90)<1e-6 else 'FALHOU'})")
print()
print("Catalogo real (Remate 1,25, comprado uma vez) — os dois regimes lado a lado:")
print(f"{'Classe':<6}{'pontos':<8}{'FEITICO COMUM':<24}{'LIBERACAO MAXIMA':<24}{'para nos pontos?':<18}")
REAL={}
for G in range(1,8):
    n,_,_ = varre(G, False, [1.0,1.25], max_mult=1)
    l,_,_ = varre(G, True,  [1.0,1.25], max_mult=1)
    REAL[G]=(n[0],l[0])
    cabe = 'SIM' if n[0] <= 3*G*1.25+1e-9 else 'NAO'
    print(f"{G:<6}{3*G:<8}{format(n[0],'g')+'d8 = '+format(n[0]*D8,'.0f'):<24}{format(l[0],'g')+'d8 = '+format(l[0]*D8,'.0f'):<24}{cabe:<18}")
print("  Feitico comum so passa dos pontos da Classe via Remate (+25% contra alvo ferido), e mesmo")
print("  assim fica abaixo da Liberacao em toda Classe. Nenhuma outra peca multiplica dano.")
print(f"  Nivel 20: feitico comum {REAL[5][0]*D8:.0f} · Liberacao {REAL[5][1]*D8:.0f} · Tecnica Maxima 108")

print()
print("="*94); print("5) PASSIVAS COM CLASSE (os Tracos da v4, renomeados)"); print("="*94)
print("  Passiva Livre     gratis, todo mundo tem 1. Nao rola dado, nao muda numero, nao faz ninguem rolar.")
print("  Passiva Classe 1    custa 1 espaco de feitico. Efeito pequeno, condicional ou de informacao.")
print("  Passiva Classe 2    custa 2 espacos. Reativo, com limite de uso.   Libera no nivel 7.")
print("  Passiva Classe 3    custa 3 espacos. Permanente, muda como voce joga. Libera no nivel 13.")
print("  Maximo de 5 Passivas pagas.")
print("  Regra Propria e o unico compravel em Classe 1 desde o nivel 1; sobe pagando a diferenca.")

print()
print("="*94); print("6) FAMILIAS — tres Fechadas na criacao"); print("="*94)
import math as _m
c2=_m.comb(9,2)*_m.comb(7,2); c3=_m.comb(9,2)*_m.comb(7,3)
print(f"  v4 (2 livres + 2 fechadas no nv 1, terceira no nv 9): {_m.comb(9,2)} x {_m.comb(7,2)} = {c2} perfis na criacao")
print(f"  v5 (2 livres + 3 fechadas no nv 1):                   {_m.comb(9,2)} x {_m.comb(7,3)} = {c3} perfis na criacao")
print(f"  Ganho de identidades distintas ja no nivel 1: +{(c3-c2)/c2*100:.0f}%")
print("  Regra nova que acompanha: feitico que deixar de ser legal se reescreve de graca, na hora.")

print()
print("="*94); print("7) TECNICA MAXIMA RECARREGAVEL — 5 x Classe maximo de PE, volta em 3 turnos"); print("="*94)
rot20=76; mx20=108; pe20=120
media_v4=(9*rot20+mx20)/10; media_v5=(2*rot20+mx20)/3
print(f"  Redacao travada: 'Depois de usar, voce nao usa de novo ate o fim do seu terceiro")
print(f"  turno seguinte.' (ancorada no turno de quem usa; 'a cada 3 rodadas' e ambiguo em iniciativa)\n")
print(f"{'Faixa':<9}{'Dano':<8}{'PE (5xG)':<10}{'% do pool nv20/25/30*':<24}{'usos que o PE permite':<22}")
print(f"{'17-20':<9}{'108':<8}{'25':<10}{25/120*100:<24.0f}{pe20//25:<22}")
print(f"{'21-25':<9}{'126':<8}{'30':<10}{'(depende do PE 21-30)':<24}{'idem':<22}")
print(f"{'26-30':<9}{'144':<8}{'35':<10}{'(depende do PE 21-30)':<24}{'idem':<22}")
print("  * o ganho de PE nos niveis 21-30 continua em aberto; o custo 5 x Classe segura a proporcao")
print("    em ~20% do pool se o PE escalar como ate aqui.\n")
print(f"  Media por rodada, nivel 20 (rotina {rot20}):")
print(f"    v4  (1x/dia, 10 rodadas de dia): {media_v4:.1f}  (+{(media_v4/rot20-1)*100:.0f}% sobre a rotina)")
print(f"    v5  (1 a cada 3 rodadas):        {media_v5:.1f}  (+{(media_v5/rot20-1)*100:.0f}%)")
d4_v4=mx20+3*rot20; pe4_v4=60+3*15
d4_v5=2*mx20+2*rot20; pe4_v5=2*25+2*15
print(f"\n  4 rodadas contra chefe, nivel 20:")
print(f"    v4: {d4_v4} de dano, gastando {pe4_v4} de {pe20} PE")
print(f"    v5: {d4_v5} de dano, gastando {pe4_v5} de {pe20} PE")
grupo_v5=220-rot20+media_v5
for vida in (730,880):
    print(f"    chefe de {vida} de vida, grupo a ~{grupo_v5:.0f}/rodada: cai em {vida/grupo_v5:.1f} rodadas")
print("  O chefe de 730 a 880 continua caindo em 3 a 4 rodadas. A conta de inimigos nao quebra.")
print("  Valvula, se ficar disponivel demais: somar 'uma vez por cena' em cima do recarregamento.")

print()
print("="*94); print("8) INTEGRIDADE E DANO NA ALMA — taxa 2:1, teto 2 x Classe"); print("="*94)
print("  1 de dano na alma = 1 de dano agora + 1 de teto de vida negado (~2x o valor de 1 de dano")
print("  normal, antes dos estagios). Dai a taxa: 2 dados normais -> 1 dado na alma.\n")
print("  TOCA A ALMA (Mira, Leve, so Classe 3+, sem Forcar): dados do feitico viram metade, na alma.")
print(f"{'Classe':<6}{'Pontos':<8}{'apos a Leve':<13}{'na alma':<9}{'dano alma':<11}{'equiv x2':<10}{'dano puro':<11}{'razao':<7}")
for G in range(3,8):
    dep=3*G-pr(G,'L'); alma=dep//2; da=alma*D8; puro=3*G*D8
    print(f"{G:<6}{3*G:<8}{dep:<13}{alma:<9}{da:<11.1f}{2*da:<10.1f}{puro:<11.1f}{2*da/puro:<7.2f}")
print("  Fica entre 0,67 e 0,83 do dano puro em equivalencia bruta; os estagios pagam a diferenca.\n")
ok_teto=all((3*G)//2 <= 2*G for G in range(1,8))
print(f"  TETO NA ALMA = 2 x Classe em dados. Maximo alcancavel sem Forcar e 3 x Classe de dados")
print(f"  -> na alma vira floor(1,5 x Classe), que nunca passa de 2 x Classe: {'CONFIRMADO' if ok_teto else 'FUROU'}")
print("  (Toca a Alma nao aceita Forcar, entao o caminho acima do teto nao existe.)\n")
print("  ESTAGIOS (fracao da Integridade perdida): 1/4 desv. pericia · 1/2 desloc. metade e +1 PE/Classe")
print("  · 3/4 desv. ataque e TR, nao conjura acima de metade da Classe · toda: decisao do mestre.")
print("  TR de Integridade contra a CD do atacante decide ESTAGIO, nao reduz dano: o dano entra cheio.\n")
print(f"{'Nivel':<7}{'Integridade':<13}{'1/4 dela':<10}{'golpe de alma da faixa':<24}{'golpes por estagio':<18}")
for nv,G in [(9,3),(13,4),(17,5),(20,5),(25,6),(30,7)]:
    integ=20+8*(nv-1); quarto=integ/4
    dep=3*G-pr(G,'L'); alma=dep//2; da=alma*D8
    print(f"{nv:<7}{integ:<13}{quarto:<10.0f}{da:<24.1f}{quarto/da:<18.1f}")
print("  Um estagio a cada 1,3 a 1,8 golpes de alma, plano do nivel 9 ao 30.\n")
print("  REMENDA (Amparo, Pesada): devolve 5 x Classe de Integridade, uma vez por cena.")
for G in (4,5):
    dep=3*G-pr(G,'L'); alma=dep//2
    print(f"    Classe {G}: devolve {5*G} contra um golpe de alma de {alma*D8:.1f} — socorro, nao torneira.")
print("\n  Tecnica Maxima na alma (24d8 -> 12 na alma = 54, 31% da Integridade de um nv 20 + estagio):")
print("  cabe como momento de chefe; primeira coisa a olhar no playtest.")

print()
print("="*94); print("9) LIBERACAO MAXIMA — o antigo Forcar, agora peca de ficha"); print("="*94)
print("  Classe 3+ · uma no nivel 10, outra no 20, outra no 30 · nao ocupa espaco de feitico")
print("  conhecido · escrita antes da sessao · aceita Melhoria e Restricao · pode ser Ampliada.")
print("  Soma +Classe em dados, custa a rodada inteira, +50% de PE e um preco na hora.\n")
print(f"{'Classe':<6}{'nivel min':<11}{'dados max':<12}{'dano':<10}{'PE base':<10}{'PE +50%':<10}{'% do pool nv20':<16}")
for G in range(3,8):
    nvmin={3:10,4:13,5:17,6:21,7:26}[G]
    pe=3*G; pel=math.ceil(pe*1.5)
    print(f"{G:<6}{nvmin:<11}{4*G:<12}{4*G*D8:<10.0f}{pe:<10}{pel:<10}{(pel/120*100 if G<=5 else 0):<16.0f}")
print("\n  No nivel 20 (120 PE) uma Liberacao de Classe 5 custa 23 PE: cabe 5 vezes num dia,")
print("  mas o freio nao e o PE — e a rodada inteira mais o preco (Vazio, Sangue ou Peso).")
print()
print("  IMPACTO NA LETALIDADE (maior dano numa rodada / vida):")
print(f"{'Nivel':<8}{'vida':<8}{'antes (Forcar em tudo)':<26}{'agora':<26}{'rodadas pra cair':<18}")
for nv,G,temlib in [(1,1,False),(5,2,False),(10,3,True),(15,4,True),(20,5,True),(25,6,True),(30,7,True)]:
    vida=20+8*(nv-1); antes=4*G*D8; agora=(4*G if temlib else 3*G)*D8
    print(f"{nv:<8}{vida:<8}{antes:<26.0f}{agora:<26.0f}{vida/agora:<18.1f}")
print("  Efeito colateral bom: os niveis 1 a 9 ficaram menos letais (1,4 e 1,9 rodadas em vez")
print("  de 1,1 e 1,4), porque o pico de 4 x Classe agora exige uma Liberacao, que so vem no 10.")
print()
print("="*94); print("10) COMBINACOES TRAVADAS"); print("="*94)
FREQ=['Uma Vez','Condicional','Aquecer','Divida']
import itertools as _it
print("  (a) Duas Restricoes de FREQUENCIA nao entram juntas. Pares bloqueados:")
for a,b in _it.combinations(FREQ,2): print(f"        {a} + {b}")
print("      Motivo: devolvem o orcamento inteiro em troca de um feitico que quase nunca sai,")
print("      e o que sai e sempre o pico. Sozinhas continuam valendo.")
print("  (b) Duas Restricoes nao podem cobrar a mesma coisa (dois turnos de preparo, duas")
print("      condicoes no seu corpo, dois jeitos de te entregar). Regra aberta, mestre aplica.")
print("  (c) Rapido + Reacao nao entram no mesmo feitico: incoerencia, nao balanco.")
print("  Nenhum dos 35 feiticos prontos quebra essas travas (conferido em pac7.py).")
