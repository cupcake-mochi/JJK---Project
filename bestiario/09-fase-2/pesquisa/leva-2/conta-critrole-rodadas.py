#!/usr/bin/env python3
"""Rodadas por combate no Critical Role (planilhas publicas do CritRoleStats).

Baixa as abas "Combat Times" das campanhas 1, 2 e 3 e as de presenca (C2 e C3),
e imprime a distribuicao das rodadas e as rodadas por numero de jogadores na mesa.
Medido pela comunidade (CritRoleStats); a conta e minha.
"""
import subprocess, os
BASE = "https://docs.google.com/spreadsheets/d/{}/export?format=csv&gid={}"
FILES = {
    "vm-combat.csv": ("1Zx1N0cQcd1fJadUwar7f2hJ2p61qoX7lctsVaIEa5uM", "482828795"),
    "mn-combat.csv": ("1E1DfdXJVu9UpGNG29JMHT3ovk8Ol_UTzol40DMzz-rw", "95756835"),
    "bh-combat.csv": ("1OE7QzSfj89xjY-DqXR468as9j6je7UgMulYCSO2Sdp0", "95756835"),
    "mn-att.csv": ("1E1DfdXJVu9UpGNG29JMHT3ovk8Ol_UTzol40DMzz-rw", "1399380767"),
    "bh-att.csv": ("1OE7QzSfj89xjY-DqXR468as9j6je7UgMulYCSO2Sdp0", "1399380767"),
}
for fn, (sid, gid) in FILES.items():
    if not os.path.exists(fn):
        subprocess.run(["curl", "-sL", BASE.format(sid, gid), "-o", fn], check=True)
import csv,statistics as st
from collections import Counter,defaultdict
def sec(t):
    try:
        h,m,s=[int(x) for x in t.split(':')]; return h*3600+m*60+s
    except: return None
def load(fn):
    rows=list(csv.reader(open(fn)))
    out=[]
    for r in rows[3:]:
        if len(r)<6 or not r[5].strip(): continue
        try: R=float(r[5])
        except: continue
        out.append((r[0],r[1],R,sec(r[2])))
    return out
def att(fn,guestcol):
    rows=list(csv.reader(open(fn)))
    d={}
    for r in rows[2:]:
        if not r or not r[0].startswith('C'): continue
        try:
            n=sum(int(x or 0) for x in r[2:9]); g=int(r[guestcol] or 0)
        except: continue
        d[r[0]]=n+g
    return d
res={}
for nome,fn in (('VM (C1)','vm-combat.csv'),('M9 (C2)','mn-combat.csv'),('BH (C3)','bh-combat.csv')):
    D=load(fn); R=[x[2] for x in D]
    mpr=[x[3]/60/x[2] for x in D if x[3] and x[2]>0]
    print(f"{nome}: n={len(R)} media={st.mean(R):.2f} mediana={st.median(R)} moda={Counter(int(x) for x in R).most_common(1)} "
          f"<=2:{sum(x<=2 for x in R)/len(R)*100:.0f}% 3:{sum(x==3 for x in R)/len(R)*100:.0f}% 4:{sum(x==4 for x in R)/len(R)*100:.0f}% >=5:{sum(x>=5 for x in R)/len(R)*100:.0f}% >=6:{sum(x>=6 for x in R)/len(R)*100:.0f}% >=8:{sum(x>=8 for x in R)/len(R)*100:.0f}% max={max(R)} min/rodada mediana={st.median(mpr):.1f} p90={sorted(R)[int(0.9*len(R))]}")
    res[nome]=D
    print('   top:',sorted([(x[2],x[0][:30],x[1]) for x in D],reverse=True)[:6])
allR=[x[2] for D in res.values() for x in D]
print(f"TODOS: n={len(allR)} media={st.mean(allR):.2f} mediana={st.median(allR)} >=5:{sum(x>=5 for x in allR)/len(allR)*100:.0f}% sem outliers>20: media={st.mean([x for x in allR if x<=20]):.2f}")
for nome,fn,gc in (('M9 (C2)','mn-att.csv',10),('BH (C3)','bh-att.csv',11)):
    A=att(fn,gc)
    by=defaultdict(list)
    for enc,ep,R,t in res[nome]:
        if ep in A: by[A[ep]].append(R)
    print(nome,'jogadores presentes -> rodadas:',{k:(len(v),round(st.mean(v),2),st.median(v)) for k,v in sorted(by.items())})
