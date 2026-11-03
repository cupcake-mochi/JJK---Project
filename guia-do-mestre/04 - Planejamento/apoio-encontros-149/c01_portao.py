"""C01 — portão: reproduz a tabela 'Vida e tempo para agir' do caso 74 por conta exata.
Premissas do caso 74: ataques normais, crítico só no 20 natural (dobra os dados), Defesa 13,
nível 2: feitiço C1 +4 3d8; espada +4 1d8+3 +1d4 (Canalizar).
Crítico pela R60 (Regras gerais, crítico): dobra só os dados básicos; o 1d4 de Canalizar é acréscimo e não dobra.
nível 6: feitiço C2 +5 6d8; espada +5 1d8+4 +1d4."""
from collections import defaultdict
def dice(n,s):
    d={0:1.0}
    for _ in range(n):
        nd=defaultdict(float)
        for k,p in d.items():
            for f in range(1,s+1): nd[k+f]+=p/s
        d=nd
    return d
def conv(a,b):
    r=defaultdict(float)
    for x,p in a.items():
        for y,q in b.items(): r[x+y]+=p*q
    return r
def shift(a,c): return {k+c:p for k,p in a.items()}
def attack(bonus,defesa,normal,crit):
    # 20 natural sempre acerta e é crítico; 1 natural erra (o caso 74 inclui o 20 no 70/60/50%)
    hit_n=sum(1 for r in range(2,20) if r+bonus>=defesa)/20
    out=defaultdict(float); out[0]+=1-hit_n-0.05
    for k,p in normal.items(): out[k]+=p*hit_n
    for k,p in crit.items(): out[k]+=p*0.05
    return out
def seq(atks):
    d={0:1.0}
    for a in atks: d=conv(d,a)
    return d
def alive(d,pv): return sum(p for k,p in d.items() if k<pv)
D=13
N2F=attack(4,D,dice(3,8),dice(6,8))
N2E=attack(4,D,shift(conv(dice(1,8),dice(1,4)),3),shift(conv(dice(2,8),dice(1,4)),3))
N6F=attack(5,D,dice(6,8),dice(12,8))
N6E=attack(5,D,shift(conv(dice(1,8),dice(1,4)),4),shift(conv(dice(2,8),dice(1,4)),4))
publicado={(2,16):(25.2,2.9,29.1,3.6),(2,24):(43.4,7.1,50.1,9.4),(2,32):(65.4,15.5,73.0,19.8),
           (6,48):(34.6,3.8,55.5,9.7),(6,72):(70.1,13.5,88.0,28.9),(6,108):(96.5,44.2,99.5,70.3)}
ok=True
for (nv,pv),pub in publicado.items():
    F,E=(N2F,N2E) if nv==2 else (N6F,N6E)
    calc=(alive(seq([F]*3),pv),alive(seq([F]*6),pv),alive(seq([E,F,F]),pv),alive(seq([E,F,F]*2),pv))
    calc=tuple(round(100*x,1) for x in calc)
    bate=all(abs(a-b)<=0.1 for a,b in zip(calc,pub)); ok&=bate
    print(f"nível {nv} / {pv:>3} PV  publicado {pub}  calculado {calc}  {'OK' if bate else 'DIVERGE'}")
# chance de acerto publicada: +4 vs 11/13/15/16 = 70/60/50/45; +5 = 75/65/55/50
for b,pub in ((4,(70,60,50,45)),(5,(75,65,55,50))):
    calc=tuple(round(100*(sum(1 for r in range(2,20) if r+b>=d)/20+0.05)) for d in (11,13,15,16))
    print(f"ataque +{b}: publicado {pub} calculado {calc} {'OK' if calc==pub else 'DIVERGE'}"); ok&=calc==pub
print("PORTÃO:", "PASSOU" if ok else "FALHOU")

# Segunda parte do caso 74: "Quantidade importa" — duas tentativas contra Defesa 13
P1=attack(4,13,shift(dice(1,4),3),shift(dice(2,4),3))   # Pancada do Carregador 1d4+3
P2=attack(4,13,shift(dice(1,8),3),shift(dice(2,8),3))   # alternativa 1d8+3
def cai(d,pv): return sum(p for k,p in d.items() if k>=pv)
pub2={("Carregador",14):4.9,("1d8+3",14):27.0,("Carregador",7):50.3,("1d8+3",7):67.3}
ok2=True
for (nome,pv),p in pub2.items():
    c=round(100*cai(seq([P1 if nome=="Carregador" else P2]*2),pv),1); b=abs(c-p)<=0.1; ok2&=b
    print(f"duas tentativas, {nome}, alvo {pv} PV: publicado {p}% calculado {c}% {'OK' if b else 'DIVERGE'}")
# médias por tentativa publicadas: 3,43 · 4,73 · 7,50
S=attack(5,13,shift(dice(2,6),4),shift(dice(4,6),4))
for nome,d,p in (("Carregador",P1,3.43),("1d8+3",P2,4.73),("Sineiro",S,7.50)):
    m=round(sum(k*q for k,q in d.items()),2); b=abs(m-p)<=0.01; ok2&=b
    print(f"média por tentativa {nome}: publicado {p} calculado {m} {'OK' if b else 'DIVERGE'}")
print("PORTÃO, parte 2:", "PASSOU" if ok2 else "FALHOU")
