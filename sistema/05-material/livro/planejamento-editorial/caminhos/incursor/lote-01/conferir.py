from pathlib import Path
import runpy,sys
b=Path(__file__).resolve().parent
p=next(p for p in b.parents if (p/'validacao-editorial/PROTOCOLO-COMPLETO.md').exists())
sys.argv=[sys.argv[0],str(b)]
runpy.run_path(str(p/'validacao-editorial/conferir_pdf_candidato.py'),run_name='__main__')
