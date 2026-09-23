#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ideia 11 — versao conferida. Primeiro REGRIDE contra a tabela publicada da peca 2 §3;
so' depois mede. Veredito por if sobre numero calculado."""
MARCOS=[6,10,14,18,22,26,30]; CRIACAO=[3,2,2,1,1]; TR=10
maestria = lambda nv: 1 + (3*(nv-2))//28

def sim(rota, teto, tex=None, qex=0, ref0=1):
    atr, ref = list(CRIACAO), ref0
    def poe(lim_extra, n_extra):
        for i in range(len(atr)):
            lim = lim_extra if (lim_extra and i < n_extra) else teto
            if atr[i] < lim: atr[i]+=1; return
    for i,_ in enumerate(MARCOS):
        poe(None,0); ref=min(ref+1,TR)
        if {'corpo':True,'refino':False}.get(rota, i%2==0): poe(tex,qex)
        else: ref=min(ref+1,TR)
    return atr, ref

# --- REGRESSAO contra a tabela publicada da peca 2 §3, nivel 30
PUBLICADO = {'corpo':([6,6,6,4,1],8), 'meio':([6,6,6,1,1],10), 'refino':([6,6,2,1,1],10)}
print("="*92); print("REGRESSAO — o simulador contra a tabela publicada da peca 2 §3 (nivel 30)"); print("="*92)
erros = 0
for rota,(atr_pub, ref_pub) in PUBLICADO.items():
    atr, ref = sim(rota, 6)
    ok_a, ok_r = (atr == atr_pub), (ref == ref_pub)
    erros += (not ok_a) + (not ok_r)
    ver_a = 'ok' if ok_a else 'ERRO ' + '\u00b7'.join(map(str, atr_pub))
    ver_r = 'ok' if ok_r else 'ERRO ' + str(ref_pub)
    print(f"  {rota:7} atributo {'\u00b7'.join(map(str,atr)):12} {ver_a:<14} refino {ref:>2} {ver_r}")
if erros: print(f"\n  >>> {erros} divergencia(s): o simulador NAO reproduz a peca, e a medida abaixo nao vale.")
else:     print(f"\n  >>> as 6 celulas reproduzem exatas. O simulador vale.")
print()

# --- o que a rota Corpo compra hoje, em BONUS (sem converter em % onde satura)
print("="*92); print("O QUE A ROTA CORPO JA COMPRA HOJE"); print("="*92)
c,_ = sim('corpo',6); r,_ = sim('refino',6)
dif = [x-y for x,y in zip(c,r)]
print(f"\n  Corpo  {'·'.join(map(str,c))}   Refino {'·'.join(map(str,r))}")
print(f"  diferenca por atributo: {dif}  -> total {sum(dif)} pontos")
print(f"  os dois primeiros atributos sao IGUAIS ({c[0]} e {c[1]}), entao a rota Corpo nao compra")
print(f"  acerto nem Defesa: ela compra os atributos 3 e 4, que entram em Teste de Resistencia e pericia.")
print(f"\n  Em Teste de Resistencia, a rota Corpo leva +{dif[2]} no terceiro e +{dif[3]} no quarto.")
print(f"  No d20 cada ponto vale 5 pontos percentuais enquanto nao satura:")
print(f"    terceiro atributo: +{dif[2]} = {dif[2]*5} pontos percentuais")
print(f"    quarto atributo:   +{dif[3]} = {dif[3]*5} pontos percentuais")
print(f"  E ela PAGA o refino no teto e as aptidoes: a peca publica 0 contra 10 aptidoes.")

# --- as duas vertentes
print("\n" + "="*92); print("AS DUAS VERTENTES, no nivel 30"); print("="*92)
VS = [('HOJE',6,None,0), ('A · um atributo estoura para 7',6,7,1),
      ('A · todos estouram para 7',6,7,5), ('B · teto 5, o 6 atras da Corpo',5,6,5)]
print(f"\n  {'regime':32} | {'Corpo':14} | {'Refino':14} | {'acerto':>6} | {'Defesa':>6} | {'espelho':>7}")
base_esp = None
for nome,t,tx,qx in VS:
    ca,cr = sim('corpo',t,tx,qx); ra,rr = sim('refino',t,tx,qx)
    ac = ca[0] + maestria(30); df = 10 + ca[0] + (cr//3 + 1)
    esp = max(1,min(19, 21-(df-ac)))/20
    if base_esp is None: base_esp = esp
    print(f"  {nome:32} | {'·'.join(map(str,ca)):14} | {'·'.join(map(str,ra)):14} | "
          f"{ac:>+6} | {df:>6} | {esp:>6.0%}")
print(f"\n  O ESPELHO (a rota Corpo atacando outra rota Corpo) e' {base_esp:.0%} em TODOS os regimes.")
print(f"  Motivo: o atributo entra nos dois lados — no acerto de quem bate e na Defesa de quem apanha.")
print(f"  E' a licao no 1 do projeto, e ela derruba a ideia como ganho de poder.")

# --- onde o ganho aparece de verdade
print("\n" + "="*92); print("ONDE O GANHO APARECE — e ele e' contra UM numero so'"); print("="*92)
INIM_DEF = 10 + 6 + (10//3 + 1)     # a peca 26 monta o inimigo com teto 6
print(f"\n  A Defesa do inimigo da peca 26 e' {INIM_DEF}, e o teto de atributo dele e' 6 — fixo.")
for nome,t,tx,qx in VS:
    ca,cr = sim('corpo',t,tx,qx); ra,rr = sim('refino',t,tx,qx)
    tc = max(1,min(19,21-(INIM_DEF-(ca[0]+maestria(30)))))/20
    tr_ = max(1,min(19,21-(INIM_DEF-(ra[0]+maestria(30)))))/20
    print(f"  {nome:32} Corpo acerta {tc:.0%} · Refino acerta {tr_:.0%} · separacao {tc-tr_:+.0%}")
print(f"\n  As duas vertentes entregam a MESMA separacao, e ela so' existe porque o inimigo")
print(f"  tem teto fixo. Subir o teto do inimigo junto zera o ganho.")
