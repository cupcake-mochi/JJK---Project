"""Registro 151: refaz os números do caso 104 com o Amontoado em Recarga (5–6), sem PE.
Mesmo motor, mesmas sementes e mesmos N de casos.py; só muda recurso='recarga56'.
O bloco C12 (grade da peça 26) não usa o Amontoado e fica como está."""
import sys; from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import casos_base as cb
R='recarga56'
for alvo in ('lista','espalha','ferido'):
    print(f"\n=== política do inimigo: {alvo} ===")
    print('-- C04 estado de entrada (trio)')
    for ini,seq in ((1,0),(.75,0),(.5,0),(.5,1),(.5,2)):
        cb.roda(f"C04 vida {ini:.0%}, Sequelas {seq}",inimigos=['amontoado'],initial=ini,sequelas=seq,alvo=alvo,recurso=R)
    if alvo=='espalha': continue
    print('-- C05 um corpo contra dois')
    cb.roda("C05 um corpo 32 PV",inimigos=[cb.am(32)],alvo=alvo,recurso=R)
    cb.roda("C05 dois corpos 16+16",inimigos=[cb.am(16),cb.am(16)],alvo=alvo,recurso=R)
    print('-- C11 distância do socorro')
    for at in (0,1,2):
        cb.roda(f"C11 atraso {at}, trio",inimigos=['amontoado'],atraso_socorro=at,ficar_ate_o_fim=True,alvo=alvo,recurso=R)
        cb.roda(f"C11 atraso {at}, dupla",grupo=cb.GRUPOS[2],inimigos=['amontoado'],atraso_socorro=at,ficar_ate_o_fim=True,alvo=alvo,recurso=R)
    print('-- C02 tamanho do grupo')
    for n,g in cb.GRUPOS.items():
        cb.roda(f"C02 grupo {n}, Amontoado 48",grupo=g,alvo=alvo,recurso=R)
        cb.roda(f"C02b grupo {n}, Amontoado {round(48*n/3)}",grupo=g,inimigos=[cb.am(pv=round(48*n/3))],alvo=alvo,recurso=R)
