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

# ---------------------------------------------------------------------------
# VALIDADOR DE FEITICO AVULSO — use pra checar qualquer feitico que um jogador criar.
# ---------------------------------------------------------------------------
def validar(nome, classe, forma, realces, restricoes, voto=0, mult_total=1.0):
    """
    classe       : 1..7
    forma      : 'Projetil' | 'Toque' | 'Explosao' | 'Cone' | 'Linha' | 'Aura'
    realces    : lista de tuplas (nome, 'L'|'M'|'P')
    restricoes : lista de tuplas (nome, 'L'|'M'|'P')
    voto       : dados extras do Voto de Carne (0 ou ate Orcamento//3)
    mult_total : multiplicador de dano total (Dano Continuo/Corrente/Area Persistente 1.5, Executor 1.25)
    """
    B = ORC[classe]; devmax = math.ceil(2*B/3); teto = B + B//3
    dado = 'd8' if forma in ('Projetil','Toque') else 'd6'
    face = 4.5 if dado == 'd8' else 3.5
    custo = sum(preco(B,t) for _,t in realces)
    devb  = sum(preco(B,t) for _,t in restricoes)
    deve  = min(devb, custo)
    dados = B - max(0, custo - deve) + voto
    total = dados * mult_total
    erros = []
    if len(realces) > 3:            erros.append("mais de 3 Realces (trava 4)")
    if len(restricoes) > 2:         erros.append("mais de 2 Restricoes (trava 3)")
    if devb > devmax:               erros.append(f"devolucao {devb} > maximo {devmax} (trava 3)")
    if voto > B//3:                 erros.append(f"Voto {voto} > maximo {B//3} (secao 6.1)")
    if total > teto + 1e-9:         erros.append(f"dano total {total:.0f} dados > Teto {teto} (trava 2)")
    print(f"\n{nome} | Classe {classe} · {forma} · {B} PF · Teto {teto} · Dev max {devmax}")
    for n,t in realces:    print(f"   -{preco(B,t):<2} {n} [{t}]")
    for n,t in restricoes: print(f"   +{preco(B,t):<2} {n} [{t}]")
    if voto:            print(f"   +{voto:<2} VOTO DE CARNE -> Acao Completa obrigatoria")
    if devb > deve:     print(f"   (!) trava 1: devolucao {devb} limitada a {deve}; {devb-deve} PF perdidos")
    print(f"   => {dados}{dado} = {dados*face:.1f} de dano medio" + (f" (x{mult_total} = {dados*face*mult_total:.1f} total)" if mult_total!=1.0 else ""))
    print(f"   [{'LEGAL' if not erros else 'ILEGAL: ' + '; '.join(erros)}]")
    return not erros

if __name__ == "__main__":
    print("\n" + "="*100); print("EXEMPLOS DE USO DO VALIDADOR"); print("="*100)
    validar("Golpe do Voto", 5, "Projetil", [], [], voto=5)
    validar("Roubo de Folego", 4, "Projetil",
            [("Drenagem",'M'),("Executor",'M')],
            [("Alvo Condicionado",'M'),("Ferida Aberta",'M')], mult_total=1.25)
    validar("[ABUSO] tudo em Restricao", 5, "Projetil", [],
            [("Corpo a Corpo",'M'),("Custo de Carne",'M')], voto=5)
