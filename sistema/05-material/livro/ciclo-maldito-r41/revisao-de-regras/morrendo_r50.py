# -*- coding: utf-8 -*-
"""Morrendo do R50: refaz os exemplos do livro e mostra onde o teto de Insistir entra.
CONTRATO (livro R50, Dano e recuperação): Aguentar = 1/4 do máximo de referência, para cima, sem teto.
Insistir = 1/3 na primeira escolha da cena e 1/2 nas seguintes, para cima, com teto de 15 x a maior Classe.
Janela = 3 rodadas - Sequelas; com 3 ou mais, derrota imediata. Vida base dos Caminhos (Progressão)."""
from math import ceil
def classe(n): return 1 if n<=4 else 2 if n<=8 else 3 if n<=12 else 4 if n<=16 else 5 if n<=20 else 6 if n<=25 else 7
def aguentar(mx): return ceil(mx/4)
def insistir(mx,c,vez): return min(ceil(mx/(3 if vez==1 else 2)), 15*c)
ok=True
def confere(rot,obtido,livro):
    global ok; bom=obtido==livro; ok=ok and bom
    print(f"  {'[x]' if bom else '[ ]'} {rot}: a conta dá {obtido}, o livro escreve {livro}")
print("1. OS EXEMPLOS DO LIVRO, REFEITOS")
confere("máximo 93, Classe 3 — Aguentar", aguentar(93), 24)
confere("máximo 93, Classe 3 — primeiro Insistir", insistir(93,3,1), 31)
confere("máximo 93, Classe 3 — metade sem teto", ceil(93/2), 47)
confere("máximo 93, Classe 3 — segundo Insistir, com teto", insistir(93,3,2), 45)
confere("máximo 395, Classe 7 — Aguentar", aguentar(395), 99)
confere("máximo 395, Classe 7 — terço sem teto", ceil(395/3), 132)
confere("máximo 395, Classe 7 — metade sem teto", ceil(395/2), 198)
confere("máximo 395, Classe 7 — os dois Insistir, com teto", (insistir(395,7,1),insistir(395,7,2)), (105,105))
confere("Mei, máximo 23 — Aguentar", aguentar(23), 6)
confere("Mei, máximo 23 — primeiro Insistir", insistir(23,1,1), 8)
confere("Mei — o que falta com 6 de tratamento", insistir(23,1,1)-6, 2)
confere("dano posterior — o que falta com 18 de 31", 31-18, 13)
confere("janela com 0, 1, 2 e 3 Sequelas", [max(0,3-s) for s in range(4)], [3,2,1,0])
print("  >>> exemplos:", "TODOS CONFEREM" if ok else "HÁ DIVERGÊNCIA")
print()
print("2. O TRATAMENTO NECESSÁRIO PELA VIDA BASE (Vanguarda e Guia: (8+Con)+(5+Con)(n-1); Evocador e Incursor: (6+Con)+(4+Con)(n-1))")
print("   nível | Classe | teto | vida | Aguentar | 1º Insistir | 2º Insistir")
for n in (2,6,10,14,18,22,26,30):
    c=classe(n)
    for nome,ini,pn,con in (("4+Con, Con 2",6,4,2),("5+Con, Con 6",8,5,6)):
        mx=(ini+con)+(pn+con)*(n-1)
        a,i1,i2=aguentar(mx),insistir(mx,c,1),insistir(mx,c,2)
        m1=" (teto)" if ceil(mx/3)>15*c else ""; m2=" (teto)" if ceil(mx/2)>15*c else ""
        print(f"   {n:5d} | {c:6d} | {15*c:4d} | {mx:4d} | {a:8d} | {i1:4d}{m1:7s} | {i2:4d}{m2}   [{nome}]")
casos=tot=0; teto1=teto2=0
for n in range(1,31):
    for ini,pn in ((8,5),(6,4)):
        for con in range(0,7):
            mx=(ini+con)+(pn+con)*(n-1); c=classe(n); tot+=1
            casos+= aguentar(mx)>insistir(mx,c,1); teto1+= ceil(mx/3)>15*c; teto2+= ceil(mx/2)>15*c
print(f"   em {tot} combinações de nível, Caminho e Constituição 0 a 6: o teto corta o 1º Insistir em {teto1}, o 2º em {teto2}, e Aguentar pede mais que Insistir em {casos}")
print()
print("3. QUANTO O INSISTIR PEDE A MAIS QUE O AGUENTAR (em pontos de tratamento, e em % da vida máxima)")
for n in (2,10,18,26):
    c=classe(n); mx=(8+3)+(5+3)*(n-1)
    d1=insistir(mx,c,1)-aguentar(mx); d2=insistir(mx,c,2)-aguentar(mx)
    print(f"   nível {n:2d}, vida {mx:3d} (5+Con, Con 3): 1º Insistir +{d1} ({d1/mx*100:.1f}%) | 2º Insistir +{d2} ({d2/mx*100:.1f}%)")
print()
print("4. RECOMPOSIÇÃO: 5 x Classe antes, 3 x Classe agora, contra o tratamento do 1º Insistir (5+Con, Con 3)")
for n in (10,18,26):
    c=classe(n); mx=(8+3)+(5+3)*(n-1); r=insistir(mx,c,1)
    print(f"   nível {n:2d}: cura {5*c} -> {3*c}; o 1º Insistir pede {r}; a Recomposição cobre {5*c/r*100:.0f}% -> {3*c/r*100:.0f}% dele")
print()
print("5. RECOMPOSIÇÃO A 4 x A MAIOR CLASSE (o que o Mizuki disse em 14/10 que era para ser), ao lado do 3 x do livro R50")
for n in (10,18,26,30):
    c=classe(n); mx=(8+3)+(5+3)*(n-1); r=insistir(mx,c,1); er=c*4.5
    print(f"   nível {n:2d}: Recomposição {3*c} (3 x) ou {4*c} (4 x); cobre {3*c/r*100:.0f}% ou {4*c/r*100:.0f}% do 1º Insistir ({r}); Energia Reversa no teto {er:.1f} = {er/(3*c):.2f} vez o Talento a 3 x e {er/(4*c):.2f} vez a 4 x")
