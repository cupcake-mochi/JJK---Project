"""Caso 102: reconstrução da coluna 'pelo menos um ativo' da dupla Vigia (120) e Tessa (80) contra os perfis de nível 15
do caso 100 (ataque +8, Defesa 14 dos guardas). Conjuntos 'três feitiços' (3 × 12d8) e 'misto' (Bastião: 2 golpes
1d8+6+2d4, crítico dobra só o d8; Emanador e Guia: 12d8). Concentra em Tessa até cair; excedente se perde.
Depois de cada conjunto, com Tessa ativa: ferida → Remendo 8d8 em si; inteira → Impulso.
Regra 'pe': 26 PE, Remendo 12, Impulso 3. Regra 'rotulo': Remendo 1× por luta, Impulso à vontade."""
import random, sys
def d(r,n,f): return sum(r.randint(1,f) for _ in range(n))
def feitico(r):
    x=r.randint(1,20)
    if x==20: return d(r,24,8)
    return d(r,12,8) if x+8>=14 else 0
def espada(r):
    x=r.randint(1,20)
    if x==20: return d(r,2,8)+6+d(r,2,4)
    return d(r,1,8)+6+d(r,2,4) if x+8>=14 else 0
def conjunto(r,tipo): return [feitico(r)]*0+([feitico(r),feitico(r),feitico(r)] if tipo=='feiticos' else [espada(r),espada(r),feitico(r),feitico(r)])
def luta(r,tipo,n,cura,regra):
    t,v=80,120; pe=26; remendo=True
    for k in range(n):
        for dano in conjunto(r,tipo):
            if t>0: t=max(0,t-dano)
            elif v>0: v=max(0,v-dano)
        if k==n-1: break
        if cura and t>0:
            if t<80:
                if regra=='pe' and pe>=12: pe-=12; t=min(80,t+d(r,8,8))
                elif regra=='rotulo' and remendo: remendo=False; t=min(80,t+d(r,8,8))
            elif v>0 and regra=='pe' and pe>=3: pe-=3
    return t>0 or v>0
if __name__=='__main__':
  N=int(sys.argv[1]) if len(sys.argv)>1 else 200000
  r=random.Random(102)
  for nome,tipo,n,cura,regra in (('sem cura, 2 de feitiços','feiticos',2,False,'pe'),('sem cura, 2 mistos','misto',2,False,'pe'),('sem cura, 3 mistos','misto',3,False,'pe'),
                              ('cura PE, 2 de feitiços','feiticos',2,True,'pe'),('cura PE, 2 mistos','misto',2,True,'pe'),('cura PE, 3 mistos','misto',3,True,'pe'),
                              ('Remendo 1× por luta, 2 de feitiços','feiticos',2,True,'rotulo'),('Remendo 1× por luta, 2 mistos','misto',2,True,'rotulo'),('Remendo 1× por luta, 3 mistos','misto',3,True,'rotulo')):
      print(f"{nome:<36} {100*sum(luta(r,tipo,n,cura,regra) for _ in range(N))/N:5.1f}%")
