from pathlib import Path
import runpy,sys
b=Path(__file__).resolve().parent
sys.argv=[sys.argv[0],str(b)]
runpy.run_path(str(b.parents[1]/'validacao-editorial/conferir_pdf_candidato.py'),run_name='__main__')
