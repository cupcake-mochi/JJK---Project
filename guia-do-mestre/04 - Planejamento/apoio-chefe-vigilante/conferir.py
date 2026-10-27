#!/usr/bin/env python3
"""Confere contas restritas da proposta. Somente leitura; não é motor de combate."""
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / 'dados.json').read_text())
UNIT = F(str(DATA['passo']['unidade']))
CAP = F(str(DATA['passo']['teto_reserva']))
DIVISOR = F(str(DATA['passo']['fracao_deslocamento']))


def floor_step(value):
    return (max(F(0), F(value)) // UNIT) * UNIT


def cap(speed):
    return floor_step(min(CAP, F(speed) / DIVISOR))


def reserve(speed, remaining):
    return floor_step(min(cap(speed), F(remaining)))


def allowance(saved, speed):
    return min(F(saved), cap(speed))


def walk(budget, terrain):
    """Cada elemento é um trecho de1,5m:0 regular,1 difícil. Não há adversários."""
    walked = F(0)
    remaining = F(budget)
    for difficult in terrain:
        cost = UNIT * (1 + difficult)
        if cost > remaining:
            break
        remaining -= cost
        walked += UNIT
    return [float(walked), float(F(budget) - remaining), float(remaining)]


cases = []


def check(name, actual, expected):
    if isinstance(actual, F):
        actual = float(actual)
    assert actual == expected, (name, actual, expected)
    cases.append({'caso': name, 'resultado': actual, 'esperado': expected})


check('9m de deslocamento,6 andados:3 reserváveis', reserve(9, 9-6), 3)
check('Todo movimento gasto:sem reserva', reserve(9, 0), 0)
check('Sobram9:capacidade só separa3', reserve(9, 9), 3)
check('Mais movimento por conversão não aumenta teto', reserve(9, 18), 3)
check('Deslocamento4,5:reserva1,5', reserve(F('4.5'), F('4.5')), 1.5)
double_half_speed = floor_step(F(9)/2/2)
check('Lento e Integridade2:deslocamento1,5', double_half_speed, 1.5)
check('Duas reduções:teto não completa trecho', cap(double_half_speed), 0)
check('Agarrado:deslocamento zero impede', allowance(3, 0), 0)
check('Redução posterior limita os3 guardados', allowance(3, F('4.5')), 1.5)
check('Recuperação não aumenta1,5 guardado', allowance(F('1.5'), 9), 1.5)
check('3m em chão regular', walk(3, [0, 0]), [3, 3, 0])
check('3m em chão difícil', walk(3, [1, 1]), [1.5, 3, 0])
check('1,5m não paga trecho difícil', walk(F('1.5'), [1]), [0, 0, 1.5])
check('Trecho regular seguido de difícil:sem fracionar segundo', walk(3, [0, 1]), [1.5, 1.5, 1.5])
check('Retirar reserva do saldo não duplica metros', 6+float(reserve(9, 3)), 9)
comparison = DATA['comparacao']
totals = {k: comparison['movimento_no_turno'][k]+comparison['movimento_posterior'][k]
          for k in comparison['movimento_no_turno']}
check('Três recortes de caminhada,sem Bônus', totals,
      {'sem_resposta': 9, 'preparar': 18, 'vigilia': 9})
check('Padrão ofensiva preservada ou investida', comparison['padrao_ofensiva_disponivel'],
      {'sem_resposta': 1, 'preparar': 0, 'vigilia': 1})
check('Vida convertida nível2,Constituição3', 5+3+(3+3)*(2-1), DATA['conversao']['PV'])
check('Integridade convertida', DATA['conversao']['PV']//2, DATA['conversao']['integridade'])
stages = [sum(F(7-current) >= 7*fraction
              for fraction in [F(1,4), F(1,2), F(3,4), F(1)])
          for current in range(7, -1, -1)]
check('Estágios da domada para Integridade7até0', stages, [0,0,1,1,2,2,3,4])

print(json.dumps({
    'tipo': 'Contas determinísticas restritas; não simula combate, reações adversárias ou decisões humanas.',
    'casos': cases,
    'total': len(cases),
    'erros': [],
    'revisao_documental_separada': [
        'Reserva zero antes do primeiro turno; a capacidade não cria um gatilho de entrada em iniciativa.',
        'Uma resposta antes e outra depois do próprio turno exigem reservas diferentes; mudança de rodada não renova recurso.',
        'Uso consome a reserva inteira; uma sobra não oferece segunda resposta.',
        'Gatilho inválido conserva reserva até prazo; condição melhorar não retroage evento.',
        'Desengajar anterior não protege movimento fora daquele turno.',
        'Oportunidade adversária ocorre antes da saída; derrota/interrupção não devolve custos.',
        'Guarda Aberta conserva ações; Atordoado impede reações; Derrubado impede esta caminhada.',
        'Conter ou transportar criatura impede iniciar; soltar a própria contenção é permitido.',
        'Coletiva única, sem Bônus de entidade; Preparar de entidade não cria metros.',
        'Saída de campo apaga reserva sem refundir metros ao Movimento.',
        'CE1 e parâmetros são propostas, não escolhas autorais ou classificação publicada.'
    ]
}, ensure_ascii=False, indent=2))
