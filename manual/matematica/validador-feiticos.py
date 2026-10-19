#!/usr/bin/env python3
"""Conta de montagem comum R53 em JSON.

Uso: python3 validador-feiticos.py montagem.json
Sem argumento, executa os exemplos e as regressões da edição atual.
O resultado cobre conta e acessos; os requisitos das peças exigem revisão.
"""
import json
from pathlib import Path
import runpy
import sys

MEC = Path(__file__).resolve().parents[2] / 'sistema/03-mecanica'
sys.path.insert(0, str(MEC))
from fundamento_r53 import calcular


def validar(montagem):
    return calcular(montagem)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        runpy.run_path(str(MEC / 'conferir-fundamento.py'), run_name='__main__')
    elif len(sys.argv) == 2:
        try:
            resultado = validar(json.loads(Path(sys.argv[1]).read_text()))
        except (ValueError, KeyError, TypeError, OSError) as e:
            print(json.dumps({'valida': False, 'erros': [str(e)]}, ensure_ascii=False))
            sys.exit(1)
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
        sys.exit(0 if resultado['valida'] else 1)
    else:
        sys.exit('Uso: python3 validador-feiticos.py montagem.json')
