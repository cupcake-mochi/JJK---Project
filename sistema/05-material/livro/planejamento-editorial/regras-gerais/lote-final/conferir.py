from pathlib import Path
import runpy,sys
B=Path(__file__).resolve().parent
P=next(p for p in B.parents if (p/'validacao-editorial').exists())
sys.argv=[str(P/'validacao-editorial/conferir_pdf_candidato.py'),str(B)]
runpy.run_path(sys.argv[0],run_name='__main__')
