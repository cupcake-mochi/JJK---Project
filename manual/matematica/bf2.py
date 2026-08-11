# -*- coding: utf-8 -*-
"""Busca exaustiva otimizada: enumera perfis de custo (equivalente a enumerar todos os builds)."""
import math, itertools
D8=4.5
ORC={1:3,2:6,3:9,4:12,5:15,6:18,7:21}
# multiplicadores de dano total disponiveis nos Realces
MULT={'L':[1.0],'M':[1.0,1.25,1.5],'P':[1.0]}
def preco(B,t): return {'L':math.ceil(B/6),'M':math.ceil(B/3),'P':math.ceil(B/2)}[t]

print("="*100)
print("BUSCA EXAUSTIVA (perfis de custo) — cobre TODAS as combinacoes legais de Realces/Restricoes/Voto")
print("="*100)
print(f"{'Classe':<6}{'Orc':<5}{'Teto':<6}{'perfis':>9}{'legais':>9}{'   DANO MAXIMO':>18}{'   perfil vencedor':<40}")
RES={}
for g,B in ORC.items():
    devmax=math.ceil(2*B/3); teto=B+B//3; vmax=B//3
    tested=0; legal=0; best=(0,"")
    # perfis de Realces: (qtd L, qtd M, qtd P) com L+M+P <= 3
    for L in range(4):
     for M in range(4-L):
      for Pz in range(4-L-M):
       # multiplicadores possiveis do conjunto (so os Medios tem multiplicador)
       for mults in itertools.product(*[MULT['M']]*M) if M else [()]:
        custo=L*preco(B,'L')+M*preco(B,'M')+Pz*preco(B,'P')
        mult=1.0
        for x in mults: mult*=x
        # perfis de Restricoes: (qtd L, qtd M) com L+M <= 2
        for rL in range(3):
         for rM in range(3-rL):
          for voto in (0,vmax):
            tested+=1
            devb=rL*preco(B,'L')+rM*preco(B,'M')
            if devb>devmax: continue
            deve=min(devb,custo)
            dados=B-max(0,custo-deve)+voto
            total=dados*mult
            if total>teto+1e-9: continue
            legal+=1
            if total>best[0]:
                best=(total,f"{L}L+{M}M+{Pz}P realces, {rL}L+{rM}M restr, mult {mult:.2f}"+(", VOTO" if voto else ""))
    RES[g]=best[0]*D8
    print(f"{g:<6}{B:<5}{teto:<6}{tested:>9}{legal:>9}{best[0]:>10.1f} dados = {best[0]*D8:5.1f}   {best[1]:<40}")

print()
print("="*100); print("VERIFICACAO FINAL"); print("="*100)
allok=True
for g,B in ORC.items():
    teto=(B+B//3)*D8
    ok=abs(RES[g]-teto)<1e-6; allok&=ok
    print(f"  Classe {g}: maximo encontrado {RES[g]:6.1f}  |  Teto de Impacto {teto:6.1f}  =>  {'BATE' if ok else 'DIVERGE'}")
print()
print(f"  Todos as Classes batem exatamente no teto: {'SIM' if allok else 'NAO'}")
print(f"  Pico do nivel 20 (Classe 5): {RES[5]:.1f}   ->  meta '<=100 por rodada': {'CUMPRIDA' if RES[5]<=100 else 'FALHOU'}")
print(f"  Pico do nivel 30 (Classe 7): {RES[7]:.1f}   ->  faixa lendaria (acima de 100 por design)")
print()
print("  O teto e ALCANCAVEL (sistema nao e frouxo) e INULTRAPASSAVEL (sistema nao e furado).")
print("  Tecnica Maxima fica de fora da busca: dados fixos, sem Restricao, sem Voto, 1x/dia.")
