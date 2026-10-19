#!/usr/bin/env python3
"""Entrada de compatibilidade: executa a conferência R53.

O modelo anterior está preservado no arquivo histórico. Esta entrada não
é uma bateria independente e não duplica a execução em subir.sh.
"""
from pathlib import Path
import runpy
import sys
mec = Path(__file__).resolve().parents[2] / 'sistema/03-mecanica'
sys.path.insert(0, str(mec))
runpy.run_path(str(mec / 'conferir-fundamento.py'), run_name='__main__')
