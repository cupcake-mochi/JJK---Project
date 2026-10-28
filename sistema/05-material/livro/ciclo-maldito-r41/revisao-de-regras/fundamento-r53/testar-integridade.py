# Entrada mantida por compatibilidade; a guarda confere a fonte corrente R58.
import builtins, contextlib, io, json, os, re, runpy, sys
from pathlib import Path
from unittest.mock import patch
raiz=Path(__file__).resolve().parents[6]
fonte=raiz/'sistema/05-material/livro/ciclo-maldito-r41/LIVRO-COMPLETO.md'
registro=fonte.parent/'revisao-de-regras/alteracoes/R52-para-R53.json'
codigo=(raiz/'conferir-repositorio.py').read_text()
inicio=codigo.index("bloco('12. FONTE R58")
fim=codigo.index('# --------------------------------------------------------------------------',inicio)
trecho=codigo[inicio:fim]
texto=fonte.read_text()
abrir=builtins.open
resultados=[]
for nome,mutacao,espera in [('controle',None,False),('cabeçalho',texto.replace('## Famílias','## Famílias alteradas',1),True),('corpo',texto.replace('Cada ponto pode ser usado uma vez','Cada ponto pode ser usado duas vezes',1),True),('bloco retirado',texto.replace('<a id="fundamento--pontos"></a>','',1),True),('registro incompleto','registro',True)]:
    erros=[]
    def ler(p,mode='r',*a,**kw):
        if Path(p)==fonte and mutacao and mutacao!='registro':
            return io.BytesIO(mutacao.encode()) if 'b' in mode else io.StringIO(mutacao)
        if Path(p)==registro and mutacao=='registro':
            return io.StringIO(json.dumps(json.loads(registro.read_text())[1:]))
        return abrir(p,mode,*a,**kw)
    with patch('builtins.open',ler),contextlib.redirect_stdout(io.StringIO()):
        exec(compile(trecho,'guarda-r53','exec'),{'RAIZ':str(raiz),'os':os,'re':re,'bloco':lambda t:None,'erro':erros.append})
    assert bool(erros)==espera,(nome,erros)
    resultados.append({'teste':nome,'rejeitou':bool(erros),'resultado':'passou'})
for nome,injetar,espera in [('voz legado preservado',False,0),('voz legado com novo achado',True,1)]:
    modulo=runpy.run_path(str(raiz/'sistema/05-material/livro/conferir-voz.py'))
    globais=modulo['main'].__globals__
    original=globais['confere']
    def confere(p):
        achados,avisos=original(p)
        if injetar and Path(p).name=='05-introducao.md':
            achados.append((1,'ARTIGO','Achado novo simulado'))
        return achados,avisos
    globais['confere']=confere
    with patch.object(sys,'argv',['conferir-voz.py','--legado-sem-regressao']),contextlib.redirect_stdout(io.StringIO()):
        try:modulo['main']();codigo_saida=0
        except SystemExit as e:codigo_saida=e.code
    assert codigo_saida==espera,(nome,codigo_saida)
    resultados.append({'teste':nome,'codigo':codigo_saida,'resultado':'passou'})
print(json.dumps(resultados,ensure_ascii=False,indent=2))
