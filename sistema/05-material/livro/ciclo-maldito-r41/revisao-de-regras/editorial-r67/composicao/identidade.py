"""Nome editorial vigente; fontes congeladas e identificadores não são alterados."""
import re
NOME='Ciclo Maldito'
def nome_oficial(text):
 def replace(m):return NOME.upper() if m[0].isupper() else NOME
 return re.sub(r'\bProjeto\s*(?:[-–—]\s*)?M\b',replace,str(text),flags=re.I)
